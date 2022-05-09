# CDK-ECS-Python-With-Requirements

Project template to show how to use CDK to create a basic ECS with some pip/python requirements.

## Debugging

Occasionally you might get: `The maximum number of addresses has been reached. (Service: AmazonEC2; Status Code: 400; Error Code: AddressLimitExceeded; Request ID: 0219b706-a011-4a2d-af00-d1fd92823878; Proxy: null)`.

This means that we have over-allocated Elastic IP addresses. To fix this, roll back the deployment manually.
1. Go to `https://eu-west-2.console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks?filteringStatus=active&filteringText=&viewNested=true&hideStacks=false`
2. Select the stack.
3. Hit `delete`

Then you have to go to:
1. Go to `https://eu-west-2.console.aws.amazon.com/ec2/v2/home?region=eu-west-2#AllocateAddress:`
2. Try to allocate a new one. If this fails it means it maxed out addresses.

`ResourceInitializationError: unable to pull secrets or registry auth: execution resource retrieval failed: unable to retrieve ecr registry auth: service call has been retried 3 time(s): RequestError: send request failed caused by: Post https://api.ecr....`

This means it cannot access the internet. you need to do:
`assign_public_ip=True,  # NEEDED FOR ECR & OWN VPC`

 