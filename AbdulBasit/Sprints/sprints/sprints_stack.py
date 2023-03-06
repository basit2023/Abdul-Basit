from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_  #some
    # aws_sqs as sqs,
)
from constructs import Construct

class SprintsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        Hello_word= self.create_lambda_function("basit",'./resource', 'Hello_word.lambda_handler')
        # The code that defines your stack goes here
    def create_lambda_function(self,id_,asset, handler):
        return lambda_.Function(self, id_,
                                code=lambda_.Code.from_asset(asset),
                                handler=handler,
                                runtime=lambda_.Runtime.PYTHON_3_7
                                )

        # example resource
        # queue = sqs.Queue(
        #     self, "SprintsQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
