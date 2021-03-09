#!/usr/bin/env python3

from aws_cdk import core

from network_pipeline.pipeline_stack import PipelineStack
from network_pipeline.network_pipeline_stack import NetworkPipelineStack

NETWORK_HUB_ACCOUNT = '260212010872'
app = core.App()
PipelineStack(app, 'PipelineStack', env={
    'account': NETWORK_HUB_ACCOUNT,
    'region': 'us-east-1'
})

#network_stack_us_east_1 = NetworkPipelineStack(app, "network-stack-us-east-1",
#        cidr_range="172.16.0.0/24",
#        tgw_asn=64512,
#        env={
#            'region': 'us-east-1',
#        }
#    )


app.synth()
