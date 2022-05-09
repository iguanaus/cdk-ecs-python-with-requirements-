"""Main entrance for AWS CDK deployment.

BEFORE RUNNING THIS, make sure to run `sh deploy_image.sh`, to deploy the image to ECR.
"""
from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_iam as iam,
    aws_ecs_patterns as ecs_patterns,
    App, CfnOutput, Duration, Environment, Stack
)
from constructs import Construct


# External resources that this app depends on.
AWS_ACCOUNT_ID = 'AWSACCOUNTID'
AWS_REGION = 'eu-west-2'
# VPC
VPC_ID = "<>"
# Security Group
ECS_ROLE = "arn:aws:iam::<AWSACCOUNTID>:role/<role_name>"
IMAGE = "<AWSACCOUNTID>.dkr.ecr.eu-west-2.amazonaws.com/ecs-template-image"


class AutoScalingFargateService(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # We import the VPC here, because otherwise it will make a new VPC, new subnets, and allocate Elastic IPs
        # for them (which is a very rare resource).
        vpc = ec2.Vpc.from_lookup(
            self,
            "Our-VPC",
            vpc_id = VPC_ID
        )

        cluster = ecs.Cluster(
            self,
            "Template-ECS-Cluster",
            vpc=vpc
        )

        execution_role = iam.Role.from_role_arn(
            self,
            id="ecsTaskDashboardExecutionRole",
            role_arn=ECS_ROLE,
        )

        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_ecs_patterns/ApplicationLoadBalancedFargateService.html

        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            f"ecs-demo-service",
            cluster=cluster,
            desired_count=1,
            health_check_grace_period=Duration.seconds(100000000), 
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry(IMAGE),
                environment={
                    'FUNZIES': "ONE"
                },
                # execution_role must be granted access to ECR (as the image is stored there)
                execution_role=execution_role
            ),
            # assing_public_ip must be True. This is needed for the service to be able to
            # connect to the internet and also you specifying your own VPC.
            assign_public_ip=True,
        )


app = App()
AutoScalingFargateService(app, "Template-ECS", env=Environment(account=AWS_ACCOUNT_ID, region=AWS_REGION))
app.synth()
