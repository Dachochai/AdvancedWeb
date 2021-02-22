import pymongo
from flask import Flask,request,jsonify
from bson import json_util
from pymongo import MongoClient

app = Flask(__name__)

connect = MongoClient("mongodb://admin:SRPfhl64026@node9148-advweb-10.app.ruk-com.cloud:11012")
db = connect["my_db"]

@app.route('/')
def index():
    text = "Hello my DB"
    return text

@app.route("/all", methods=['GET'])
def get_all():
    data = db.job_db
    output = data.find()
    return json_util.dumps(output)

@app.route("/one/<position>", methods=['GET'])
def get_one(position):
    data = db.job_db
    output = data.find_one({'position' : position})
    return json_util.dumps(output)

@app.route('/all', methods=['POST'])
def add_job():
  data = db.job_db
  position = request.json['position']
  age_range = request.json['age_range']
  job_duties = request.json['job_duties']
  salary = request.json['salary']
  company_name = request.json['company_name']
  location = request.json['location']

  
  job_id = data.insert({'position': position,
                        'age_range': age_range,
                        'job_duties': job_duties,
                        'salary': salary,
                        'company_name': company_name,
                        'location': location})
  new_job = data.find_one({'_id': job_id })
  output = {'position' : new_job['position'],
                        'age_range' : new_job['age_range'],
                        'job_duties' : new_job['job_duties'],
                        'salary' : new_job['salary'],
                        'company_name' : new_job['company_name'],
                        'location' : new_job['location']}
  return jsonify(output)

@app.route('/all/<position>', methods=['PUT'])
def update_job(position):
    data = db.job_db
    x = data.find_one({'position' : position})
    if x:
        query = {'position' : x['position'],
                        'age_range' : x['age_range'],
                        'job_duties' : x['job_duties'],
                        'salary' : x['salary'],
                        'company_name' : x['company_name'],
                        'location' : x['location']}

    position = request.json['position']
    age_range = request.json['age_range']
    job_duties = request.json['job_duties']
    salary = request.json['salary']
    company_name = request.json['company_name']
    location = request.json['location']
    
    newdata = {"$set" : {'position' : position,
                        'age_range' : age_range,
                        'job_duties' : job_duties,
                        'salary' : salary,
                        'company_name' : company_name,
                        'location' : location}}

    data_id = data.update_one(query, newdata)

    output = {'position' : position,
                        'age_range' : age_range,
                        'job_duties' : job_duties,
                        'salary' : salary,
                        'company_name' : company_name,
                        'location' : location}
    return jsonify(output)

@app.route('/all/<position>', methods=['DELETE'])
def delete_character(position):
    data = db.job_db
    x = data.find_one({'position' : position})
    data_id = data.delete_one(x)
    output = "Deleted complete"
    return jsonify(output)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=81)