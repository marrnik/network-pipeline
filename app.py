#!/usr/bin/env python3

from aws_cdk import core

from network_pipeline.network_pipeline_stack import NetworkPipelineStack
from network_pipeline.pipeline_stack import PipelineStack

app = core.App()
NetworkPipelineStack(app, "network-pipeline")
PipelineStack(app, 'PipelineStack', env={
    'account':'260212010872',
    'region': 'us-east-1'
})

app.synth()
