# AWS 云部署的常规流程

## AWS Services involved

    - RDS: Managed Relational Database Service -> Database
    - ECR: Elastic Container Registry -> Repository
    - ECS: Elastic Container Service -> Auto-scalable Server

### AWS Serice Region Setup

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
      - [ ] Inser the command used here
      - [ ] Explain why I need to run docker locally before deploy to the AWS
    - Set up the RDS on AWS
    - Connect the endpoint generated in RDS to the Django Project Database settings
    - Run local project to verify the database connection
      - if verified, upload the local project to the ECR
    - Upload the code base to ECR
    - Deploy the project to ECS

Docker Build:

- docker build -t gymproject .
  - t == 'tag'
- docker run -d -p 8000:8000 gymproject

TODO: Run ECR
