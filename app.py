#!/usr/bin/env python3

from aws_cdk import core

from network_pipeline.network_pipeline_stack import NetworkPipelineStack


app = core.App()
NetworkPipelineStack(app, "network-pipeline")

app.synth()
