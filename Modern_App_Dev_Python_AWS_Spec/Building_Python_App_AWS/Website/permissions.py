#Uses AWS CLI to create bucket policy for specified bucket name
#Open reads the policy from relative file website_security_policy

import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "<Your S3 Bucket Name>"

policy_file = open("website_security_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("DONE")