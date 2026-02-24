import boto3
from botocore.client import Config


class StorageClient:
    def __init__(self, access_key_id, secret_access_key, endpoint_url, bucket_name):
        self.client = boto3.client(
            's3',
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            endpoint_url=endpoint_url,
            config=Config(signature_version='s3v4'),
        )
        self.bucket_name = bucket_name

    def upload_file(self, file_path):
        object_name = file_path[file_path.rindex('/')+1:]
        self.client.upload_file(file_path, self.bucket_name, object_name)
