import aws_cdk as core
import aws_cdk.assertions as assertions

from cos_lz_automation.cos_lz_automation_stack import CosLzAutomationStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cos_lz_automation/cos_lz_automation_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CosLzAutomationStack(app, "cos-lz-automation")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
