import boto3

def upload_file(file_path, bucket_name, key):
    s3_client = boto3.client('s3')

    try:
        s3_client.upload_file(file_path, bucket_name, key)
        return True
    except Exception as e:
        print(f"An error occurred while uploading the file: {str(e)}")
        return False
