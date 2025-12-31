import boto3
from botocore.exceptions import ClientError

# ==============================
# AWS CREDENTIALS (EDIT THESE)
# ==============================
AWS_ACCESS_KEY_ID = "ACCESS_KEY"
AWS_SECRET_ACCESS_KEY = "SECRET_KEY"
AWS_REGION = "us-east-1"
BUCKET_NAME = "assaf-s3-demo-bucket"

# ==============================
# S3 CLIENT
# ==============================
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

# ==============================
# FUNCTIONS
# ==============================
def upload_file(local_path, s3_key):
    """Upload a local file to S3"""
    try:
        s3.upload_file(local_path, BUCKET_NAME, s3_key)
        print(f"Uploaded: {local_path} → s3://{BUCKET_NAME}/{s3_key}")
    except ClientError as e:
        print("Upload failed:", e)


def download_file(s3_key, local_path):
    """Download a file from S3"""
    try:
        s3.download_file(BUCKET_NAME, s3_key, local_path)
        print(f"Downloaded: s3://{BUCKET_NAME}/{s3_key} → {local_path}")
    except ClientError as e:
        print("Download failed:", e)


def delete_file(s3_key):
    """Delete a file from S3"""
    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=s3_key)
        print(f"Deleted: s3://{BUCKET_NAME}/{s3_key}")
    except ClientError as e:
        print("Delete failed:", e)


# ==============================
# EXAMPLE USAGE
# ==============================
if __name__ == "__main__":
    # Upload
    upload_file("local.txt", "bla/remote.txt")

    # Download
    download_file("bla/remote.txt", "downloaded.txt")

    # Delete
    delete_file("bla/remote.txt")
