# Will create an image from local files, and push this to ECR (eu-west-2).
# NEED TO CREATE THE ECR PRIOR TO RUNNING at `https://eu-west-2.console.aws.amazon.com/ecr/create-repository?region=eu-west-2`

echo "Deploying the adapter image..."

aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin <AWSACCOUNTID>.dkr.ecr.eu-west-2.amazonaws.com

docker build -t ecs-template .

docker tag ecs-template:latest <AWSACCOUNTID>.dkr.ecr.eu-west-2.amazonaws.com/ecs-template-image:latest

docker push <AWSACCOUNTID>.dkr.ecr.eu-west-2.amazonaws.com/ecs-template-image:latest

echo "Done deploying the new image to: <AWSACCOUNTID>.dkr.ecr.eu-west-2.amazonaws.com/ecs-template-image:latest"