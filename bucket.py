import socket
import boto3
import os
import json
from googleBucket import create_bucket, delete_bucket, gcpUploadFile, gcpRemoveFile, list_buckets
from awsBucket import createBucket, deleteBucket, listBuck
from awsFiles import awsUpload, awsRemove
from google.cloud import storage

#Google account credentials (unique) to user, must be change to connect to GCP
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "extended-cable-354615-abf983eae722.json"

storage_client = storage.Client()
s3 = boto3.client("s3")

#HOST = "10.10.94.118"
HOST = "127.0.0.1"
PORT = 1433

def receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(50000)
                if not data:
                    break
                else:
                    jsonDict = json.loads(data)
                    print(jsonDict)
                    return jsonDict

command = receive()

#creates Buckets (storage) in both GCP and AWS
def create(bucketName):
    createBucket(bucketName)
    create_bucket(bucketName)

#deletes Buckets (storage) in both GCP and AWS
def delete(bucketName):
    deleteBucket(bucketName)
    delete_bucket(bucketName)

#upload files to existing buckets in both GCP and AWS
def upload(bucketName, file, blob):
    gcpUploadFile(bucketName, file, blob)
    awsUpload(file, blob, bucketName)

#remove existing files in both GCP and AWS
def remove(bucketName, blob):
    gcpRemoveFile(bucketName, blob)
    awsRemove(bucketName, blob)

#List out existing buckets in both Cloud Service Providers 
def listBucks():
    list_buckets()
    listBuck()


def main():
    if command["action"] == "create":
        create(command["target"]["bucket"]["bucket_name"])
    if command["action"] == "delete":
        delete(command["target"]["bucket"]["bucket_name"])

    if command["action"] == "upload":
        upload(command["target"]["bucket"]["file"]["bucket_name"], command["target"]["bucket"]["file"]["file_name"], command["target"]["bucket"]["file"]["blob"])
    if command["action"] == "remove":
        remove(command["target"]["bucket"]["file"]["bucket_name"], command["target"]["bucket"]["file"]["blob"])

    if command["action"] == "list":
        listBucks()

main()

