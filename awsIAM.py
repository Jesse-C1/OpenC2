import boto3
import json
import sys
from argparse import ArgumentParser


iam = boto3.client("iam")

class UserManagement:

    def __init__(self, path):
        with open(path, "r", encoding = "utf-8") as f:
            a = f.readlines()
            b = " ".join(a)
            self.jsonDict = json.loads(b)

    def actions(self):
        if self.jsonDict["action"] == "create":
            create = iam.create_user(
            UserName = self.jsonDict['target']['new_user']['username']
            )
            return(create)
        
        if self.jsonDict["action"] == "delete":
            delete = iam.delete_user(
            UserName =self.jsonDict['target']['existing_user']['username']
            )
            return(delete)

    def userList(self):
        for users in iam.list_users()["Users"]:
            print("Username: " + users["UserName"] + "\nUserID: " + users["UserId"] + "\n")

def main(file):
    select = UserManagement(file)
    select.actions()
    select.userList()
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("file", help = "file path")
    args = parser.parse_args(arglist)
    return args

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)