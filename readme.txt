1. for downloading all requirements at once use 
#pip3 install -r requirements.txt

2. to run the application in docker and kubernetes cluster we need to create a docker file ( to deploy this as a cointainer)
3. After creating the docker file we need to create a docker image from it 
   docker build -t my-flask-app . ( . is used to tell docker that we want to run the docker file present in the CWD)
   
   # while creating the docker cointainer using the cmd terminal got the below error 
   /bin/sh: 1: flask: not found
   it is because we have to use python as a terminal , in order to change the default terminal we need to change it on vscode press 
   shift+ctrl+p , and select preferences as python and press play button .
   ( then execute the commands on python terminal and it will work)

   4. since we have created the docker image , now we have to create a cointainer out of it 

   docker run -p 5000:5000 (image-id or name ) .


   5. Boto3 - it integrates python application, library or script with the aws or it used to create , configure and manage AWS services

   6. Got the error - botocore.exceptions.NoRegionError: You must specify a region. 
      # for this we need to add the default region in C:\Users\sande\.aws\config file 
      [default]
      region=us-east-1
   
   7. now we have to push the docker image to aws ECR for this we need to follow the steps given in the AWS ECR 

   8. After this we'll use Amazon Elastic kubernetes services to deploy our cointainer into kubernetes pots
      i. first create a cluster in EKS
      ii. create a node group
      iii. Create deployment and services
      #Note - Make sure to edit the name of the image on line 25 with your image uri

   9. once you run the file #python3 Eks.py deployment and services will be created 
      Check by running the following command 

      kubectl get deployment -n default (check deployments)
      kubectl get service -n default (check service)
      kubectl get pods -n default (to check the pods)
   
   Once your pod is up and running, run the port-forward to expose the service

   kubectl port-forward service/<service_name> 5000:5000 