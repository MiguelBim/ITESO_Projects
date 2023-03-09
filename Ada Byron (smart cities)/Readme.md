# ITESO - Ada Byron (Ingeniería en Sistemas Computacionales)

→ Download and run the AWS CLI MSI installer for Windows (64-bit)
```bash
https://awscli.amazonaws.com/AWSCLIV2.msi
```

#### (1) Validate that AWS CLI was installed successfully and that your credentials are defined 
```bash
aws configure list
```

#### (2) Create the Rekognition Collection
```bash
aws rekognition create-collection --collection-id facerecognition_collection --region us-east-1
```

#### (3) Create the DynamoDB table to store images metadata (person's name)
```bash
aws dynamodb create-table --table-name face_recognition --attribute-definitions AttributeName=RekognitionId,AttributeType=S --key-schema AttributeName=RekognitionId,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --region us-east-1
```

#### (4) Move to Images folder
```bash
cd C:\Images
```
