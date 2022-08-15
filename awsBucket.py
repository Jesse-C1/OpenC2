import boto3

s3 = boto3.client("s3")

def createBucket(bucketName):
    response = s3.create_bucket(
        Bucket = bucketName
    )
    print (response)
    print("AWS: Created bucket " + bucketName)

def deleteBucket(bucketName):
    response = s3.delete_bucket(
        Bucket = bucketName
    )
    print (response)
    print("AWS: Deleted " + bucketName)

def listBuckets():
    response = s3.list_buckets()

    for i in response['Buckets']:
        print(i["Name"])

def listBuck():
    response = s3.list_buckets()
    x = 0
    print("AWS:")
    for i in response['Buckets']:
        x += 1
        print(f"{x}.Bucket {i['Name']}")