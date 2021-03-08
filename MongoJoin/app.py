import pymongo
from flask import Flask, request, jsonify
from bson import json_util
from pymongo import MongoClient

app = Flask(__name__)

connect = MongoClient(
    "mongodb://admin:SRPfhl64026@node9148-advweb-10.app.ruk-com.cloud:11012"
)
db = connect["my_db"]


@app.route("/")
def index():
    text = "Hello my DB"
    return text


@app.route("/all", methods=["GET"])
def get_join():
    data = db.job_db
    pipel = data.aggregate(
        [
            {
                "$lookup": {
                    "from": "company_db",
                    "localField": "company_name",
                    "foreignField": "company_name",
                    "as": "company_db",
                }
            },
            {"$unwind": "$company_db"},
            {
                "$project": {
                    "position": 1,
                    "company_name": 1,
                    "location": 1,
                    "phone": "$company_db.phone",
                    "about": "$company_db.about",
                }
            },
        ]
    )
    return json_util.dumps(pipel)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
