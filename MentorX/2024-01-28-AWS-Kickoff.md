# AWS 云部署的常规流程

## AWS Services involved

- RDS: Managed Relational Database Service -> Database
- ECR: Elastic Container Registry -> Repository
- ECS: Elastic Container Service -> Auto-scalable Server

The primary difference between Amazon ECR and ECS is that while ECR provides the repository that stores all code that has been written and packaged as a Docker image, the ECS takes these files and actively uses them in the deployment of applications.

### AWS Service Region Setup

- Speed
- Price
- functionality feature: Premium network

### AWS Authentication Management

- Root User: Top level of authentication
- IAM User: Developers/Employees

## Project Dependencies

- Docker: Dockerfile
- AWS: AWS Command Line Interface (CLI)

## 流程

- Download Docker and creare the Dockfile in the local project
  - run the local docker commands and see if the docker is correctly set up
    - Docker Build:
      - `docker build -t gymproject .`
        - t == 'tag'
      - `docker run -d -p 8000:8000 gymproject`
  - [ ] Explain why I need to run docker locally before deploy to the AWS
- Set up the RDS on AWS
- Connect the endpoint generated in RDS to the Django Project Database settings
- Run local project to verify the database connection
  - if verified, upload the local project to the ECR
- Upload the code base to ECR

  - AWS Config: helps you record configuration changes to software within EC2 instances in your AWS account and also virtual machines (VMs) or servers in your on-premises environment.
  - Authenticate Docker to your ECR registry:

    `aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 851725592427.dkr.ecr.us-west-2.amazonaws.com`

- Deploy the project to ECS
- 更改域名
