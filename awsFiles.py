import boto3

s3 = boto3.resource('s3')

def awsUpload(filename, key, bucketName):
    s3.Bucket(bucketName).upload_file(filename, key)

    print(f"AWS: {filename} uploaded to {bucketName} as {key}")

#awsUpload("test2.py", "test file" ,"asfafa" )

def awsRemove(bucketName, key):
    s3.Object(bucketName, key).delete()

    print(f"AWS: {key} deleted from {bucketName}")
#awsRemove("asfafa", "test file")

