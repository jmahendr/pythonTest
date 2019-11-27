import boto3

def get_s3_client():
    s3 = boto3.client('s3')
    return s3

def list_bucket(bucket):
    s3_client = get_s3_client()
    resp = s3_client.list_objects(Bucket=bucket)

    for bucket in resp['Contents']:
        name=bucket['Key']
        size=bucket['Size']
        print(f"file {name}, {size} bytes")

list_bucket('portfolio.joshuastech.info')