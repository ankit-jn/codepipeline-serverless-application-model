## ARJ-Stack: CodePipeline for SAM Deployment

This project has the direction of how AWS DevOps service (CodePipeline, CodeBuild) can be used to create Pipeline for Serverless Application Model deployment

### Resources
This project features the following components:

#### pipeline

This folder contains the CloudFormation Template used for building the CodePipeline for the projects
- `codepipeline-application.yml` - Create Code Pipeline for the project `arjstack-application`.

- Please note that upload the Template files placed in this folder into S3 bucket [S3 Key] `arjstack-devops/pipeline-templates` and use this S3 location `https://s3.amazonaws.com/arjstack-devops/pipeline-templates/codepipeline-application.yml` while creating CloudFormation Stack for CodePipeline 
  - If not, Cloudformation will automatically create a bucket for you if you will go with the approach of uploading template file while creating stack for pipeline

#### application

This folder contains the SAM template (`template.yml`) and Nested Cloudformation Templates used in provisioning AWS resources as well as `buildspec.yml` and corresponding json files for CodeBuild 

- Please note all the files of this folder should be committed in the code commit repository `arjstack-application`.

### Requirements

| Resource | Name | Purpose |
|------|---------|---------|
| <a name="codecommit_repository"></a> [codecommit_repository](#requirement\_codecommit\_repository) | `"arjstack-application"` | CodeCommit Repository where the CFN Templates will be stored to provision the AWS resources |
| <a name="s3_bucket"></a> [s3_bucket](#requirement\_s3\_bucket) | `"arjstack-devops"` | This bucket is used to store the Cloudformation Template used for creating CodePipeline, to store SAM template, Nested Cloudformation templates and artifacts for CodePipeline and CodeBuild |
| <a name="sns_topic"></a> [sns_topic](#requirement\_sns\_topic) | `"arjstack-devops-notification"` | This SNS topic is used for notification in Appproval stage |
| <a name="sns_topic_subscription"></a> [sns_topic_subscription](#requirement\_sns\_topic\_subscription) |  | Subscription to SNS topic so that reviewer is notified (preferably Email based subscription) |

### Inputs - CloudFormation Stack for the Pipelines
---

#### Pipeline of the project `arjstack-application`

| Name | Description | Type | Default | Required | Example|
|:------|:------|:------|:------|:------:|:------|
| <a name="ProjectName"></a> [ProjectName](#input\_ProjectName) | Name of the Project. | `string` | `"ARJStack-Application"` | no |  |
| <a name="ProjectRepoName"></a> [ProjectRepoName](#input\_ProjectRepoName) | Name of the repo which contains SAM and nested CFN template for provisioning Application Infrastructure. | `string` |  | yes | `"arjstack-application"` |
| <a name="ArtifactStoreS3Location"></a> [ArtifactStoreS3Location](#input\_ArtifactStoreS3Location) | Name of the S3 bucket to store the Cloudformation Template used for creating CodePipeline, to store SAM template, Nested Cloudformation templates and artifacts for CodePipeline and CodeBuild. | `string` |  | yes | `"arjstack-devops"` |
| <a name="NotificationTopic"></a> [NotificationTopic](#input\_NotificationTopic) | Name of the SNS topic to send approval notification. | `string` |  | yes | `"arjstack-devops-notification"` |


### Authors

Module is maintained by [Ankit Jain](https://github.com/ankit-jn) with help from [these professional](https://github.com/arjstack/codepipeline-serverless-application-model/graphs/contributors).
