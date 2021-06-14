#!/usr/bin/env python

from aws_cdk import core as cdk

from stacks.cdk_stack import MyStack


app = cdk.App()
MyStack(app, "MyDemoStack")

app.synth()
