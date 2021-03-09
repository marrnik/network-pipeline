from aws_cdk import core

from .network_pipeline_stack import NetworkPipelineStack

class NetworkStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = NetworkPipelineStack(self, 'Network')