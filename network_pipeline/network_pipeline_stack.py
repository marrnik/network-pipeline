from os import path

from aws_cdk import core
import aws_cdk.aws_ec2 as ec2

class NetworkPipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
#    def __init__(self, scope: core.Construct, id: str, cidr_range: str, tgw_asn: int, **kwargs) -> None:
#        super().__init__(scope, id, **kwargs)
        this_dir = path.dirname(__file__)

        # VPC Creation
        self.vpc = ec2.Vpc(self,
            "TransitVPC",
            max_azs=1,
            cidr="172.16.0.0/24",
            # configuration will create 1 subnet in a single AZ.
            subnet_configuration=[ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.ISOLATED,
                    name="Isolated",
                    cidr_mask=25
                    )
            ]
        )

        # Transit Gateway creation
        self.tgw = ec2.CfnTransitGateway(
            self,
            id="TGW-USe1",
            amazon_side_asn=64512,
            auto_accept_shared_attachments="enable",
            default_route_table_association="enable",
            default_route_table_propagation="enable",
            tags=[core.CfnTag(key='Name', value="tgw-us-east-1")]
        )

        # Transit Gateway attachment to the VPC
        self.tgw_attachment = ec2.CfnTransitGatewayAttachment(
            self,
            id="TGW-Attachment",
            transit_gateway_id=self.tgw.ref,
            vpc_id=self.vpc.vpc_id,
            subnet_ids=[subnet.subnet_id for subnet in self.vpc.isolated_subnets],
            tags=[core.CfnTag(key='Name', value=f"tgw-{self.vpc.vpc_id}-attachment")]
        )