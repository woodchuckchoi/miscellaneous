import boto3
import os
import json

BUCKET          = "hyuckcodedeploydemo"
CONFIG          = "config.json"
APPLICATIONNAME = ""
DGNAME          = ""

s3          = boto3.resource("s3")
codeDeploy  = boto3.client("codedeploy")
bucket      = boto3.resource("s3").Bucket(BUCKET)

def read_config():
    data    = s3.Object(BUCKET, CONFIG)
    try:
        body    = data.get()["Body"].read()
        parse   = json.loads(body)
        return parse
    except:
        return {
            "front": None,
            "back": None
        }
    
def write_config(front, back):
    obj     = {
        "front": front,
        "back": back
    }
    string  = json.dumps(obj)
    encode  = string.encode("utf-8")
    bucket.put_object(Key=CONFIG, Body=encode)
    
def parse_title(title):
    prefix = "back"
    if title.startswith("front"):
        prefix = "front"
    
    return title[title.find(prefix)+len(prefix):]

# def delete_obj(name):
#     request = {
#         Objects: [
#             {
#             "Key": name
#             }
#         ]
#     bucket.delete_objects(request)

# ASSUMING APP FILENAME FORMAT IS "front/back{timestamp}"

def get_latest():
    front   = [parse_title(entry) for entry in bucket.objects.all() if entry.startswith("front")]
    back    = [parse_title(entry) for entry in bucket.objects.all() if entry.startswith("back")]

    data = {
        "front": None,
        "back": None
    }

    if len(front) != 0:
        front.sort(reverse=True)
        data["front"] = front[0]
    if len(back) != 0:
        back.sort(reverse=True)
        data["back"] = back[0]

    return data

def update(part, key):
    if part == "front":
        codeDeploy.create_deployment(
            applicationName     = APPLICATIONNAME,
            deploymentGroupName = DGNAME,
            revision            = {
                "revisionType": "S3",
                "s3Location": {
                    "bucket": BUCKET,
                    "key": key,
                    "bundleType": "zip",
                }
            },
        )
    else:
        codeDeploy.create_deployment(
            applicationName     = APPLICATIONNAME,
            deploymentGroupName = DGNAME,
            revision            = {
                "revisionType": "S3",
                "s3Location": {
                    "bucket": BUCKET,
                    "key": key,
                    "bundleType": "zip",
                }
            },
        )

def main(event, lambda_context):
    current = read_config()
    new     = get_latest()

    for part in ["front", "back"]:
        if current[part] != new[part]:
            update(part, new[part])

    write_config(new["front"], new["back"])
