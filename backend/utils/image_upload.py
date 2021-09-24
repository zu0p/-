import os
import boto3
from botocore.exceptions import ClientError

access_key = "AKIATZKW3HN46UET5BQ7"
secret_key = "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"
bucket_name = "greeda-recommend"

"""
connect to S3
"""
client_s3 = boto3.client(
    's3',
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key
)

"""
upload file to S3
"""
async def upload_file(local_path, s3_path, client, bucket_name="greeda-recommend"):
    try:
        client.upload_file(
            local_path,
            bucket_name,
            s3_path,
            ExtraArgs={'ContentType': 'image/jpg'}
        )
        print("upload")
    except ClientError as e :
        print(f'Credential error => {e}')
    except Exception as e :
        print(f"Another error => {e}")

# upload file example
# upload_file("./static/image/diary/test_test.jpg", "test_image")
# https link 
# => https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/test_image