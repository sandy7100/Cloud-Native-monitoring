import boto3

#assigning the region name 
#kms = boto3.client('kms', region_name='us-east-1')

#setting the client , creating ecr client
ecr_client = boto3.client('ecr')



#define the repo name , creating new ecr repo
repository_name = "my_flask_app"
response = ecr_client.create_repository(repositoryName=repository_name)

#used for container image push and pull operation
repository_uri = response['repository']['repositoryUri']
print(repository_uri)

