import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'extended-cable-354615-abf983eae722.json'

def create_bucket(bucketName, location = "us"):

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucketName)
    new_bucket = storage_client.create_bucket(bucket, location)

    print(
        "Google: Created bucket {} in {}".format(
            new_bucket.name, new_bucket.location
        )
    )
    return new_bucket

def delete_bucket(bucketName):

    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucketName)
    bucket.delete()

    print(f"Google: Deleted {bucket.name}")


def gcpUploadFile(bucket_name, file, blobName):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blobName)

    blob.upload_from_filename(file)

    print(
        f"Google: {file} uploaded to {bucket_name} as {blobName}"
    )

def gcpRemoveFile(bucket_name, blobName):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blobName)
    blob.delete()

    print(f"Google: {blobName} deleted from {bucket_name}")

def list_buckets():
    x = 0
    storage_client = storage.Client()
    buckets = storage_client.list_buckets()
    print("Google:")
    for bucket in buckets:
        x += 1
        print(f"{x}.Bucket {bucket.name}")

#gcpUploadFile("asfafa", "test.py", "testFile")
#gcpRemoveFile("asfafa", "testFile")

#create_bucket("aaaa_bucket")
#delete_bucket("aaaa_bucket")