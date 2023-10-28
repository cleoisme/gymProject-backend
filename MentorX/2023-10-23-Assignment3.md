# Assignment 3 - 2023-10-23

## Tasks

- [x] 将 Notification 的部分分割成另一个 App
- [x] 将每个 Class 转化成一个 file，并将所有 Classes 放入到一个叫做 models 的 folder 里，以 models.py 为 top-level 的 file 和对 external folder 的接口
  - [x] Update the User class
    - Add the `is_admin` attribute to the User class
    - remove the admin class
    - update the `password` to the Django built-in password field
  - **Question**: Relationship definition practice
    - Since Django will help create the reverse relationship, how to decide where to put the definition?
    - Recap of the foreign keys/primary keys?
    - Distinction between foreign keys/primary keys in code
- [x] 用类似方式在 gymCMS/views 中分流 Routing
- [ ] views.py 中如何区分 post, put, get 等 operations
- [x] VSCode extension to check duplicate imports - pylint installed
- [x] Fix Github Action

  - within the project directory and activate the virtual environment, then run `pip freeze > requirements.txt`
  - upload the `requirements.txt` to the project-level of folder
  - push the `requirements.txt` to the repo and trigger another round of Pipeline

  **Question**:

  - How to locally test this pipeline first? or trigger the pipeline on the Branch?
  - local `Django==4.2.6` but update the `requirement.txt` to be 3.2.22 as the latest supported version. Is this a bad practice or acceptable? how to fix if not?

## Notes

- `.yml` / `.ymal` files:
  - Usually used to define the environment to be the same as the local
    - CI/CD Pipeline
    - Docker Instances
    - AWS CloudFormation
  - Why not leverage UI workflow
    - review
    - reproduce
- AWS 功能介绍：

  - EC2 + S3: The fundamentals that support most AWS services
  - S3: 类 Google Drive 的储存平台，可以存任何形式的对象文件。
    - 在本项目中主要用来储存图片、视频等媒体文件。
    - to log in: Access Key ID 和 Secret Access Key
      - 与其他服务不同的是，S3 的 login info 是 Global 的，也就说可以忽略 Area Zone (AZ)的限制。
  - Dynamic DB: fully managed, serverless, key-value NoSQL database, 以 JSON 形式储存数据。
    - 在本项目中可用作数据库储存数据使用。
    - 将数据迁移到 DDB 后 AWS 会自动备份

- AWS S3 connects to Local:

  - install the AWS SDK for Python: `pip install boot3`
  - verfify if the SDK is correctly installed: `aws sts get-caller-identity`
  - import boto3 to .py files: `s3 = boot3.client('s3')`

- 如何避免把关键信息上传至云数据库
  - Approach1: environment keys (in `settings.py`) - Amazon s3 Django storage
  - Approach2: IAM Role, set 'local assume role'
