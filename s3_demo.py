import boto3
import uuid
from pathlib import Path

#configuration

REGION = "us-east-1"

#Bucket name 

bucket_name = f"python-s3-demo-{uuid.uuid4().hex[:12]}"

#File upload

file_name = "Demo-file.txt"

# connecting to AWS

session = boto3.Session(region_name=REGION)
s3 = session.client("s3")
sts = session.client("sts")

identity = sts.get_caller_identity()

print("Connected to AWS Services")
print("Account", identity["Account"])
print("Region",REGION)

# Demo creation

file_path = Path(file_name)

file_path.write_text(
	"This is a Demo file made with python, will be uploaded to AWS"
)

print("\nDemo file created", file_name)

# S3 bucket creation 

print("\nS3 bucket creation", bucket_name)

s3.create_bucket(
	Bucket=bucket_name
)

print("s3 Bucket created")

# FIle upload into s3 bucket

object_key = file_name

print("\nuploading file")

s3.upload_file(
	str(file_path),
	bucket_name,
	object_key
)

print("File upload complete")

# Listing objects in the bucket

print("\n list obj in bucket")

response = s3.list_objects_v2(
	Bucket=bucket_name
)

objects = response.get("Contents", [])

for obj in objects:
	print(
		"File:",
		obj["Key"],
		"| Size: ",
		obj["Size"],
		"bytes"
)

# Upload verification

uploaded = any(
	obj["Key"] == object_key
	for obj in objects
)

if uploaded:
	print("\n Success: verified")
else:
	print("\n Fail: Cannot be verified")
