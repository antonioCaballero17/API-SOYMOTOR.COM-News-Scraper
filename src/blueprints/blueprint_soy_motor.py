import json
from flask import Blueprint, jsonify,request
from classes.news_soy_motor import NewsSoyMotor


blueprint_soy_motor = Blueprint(name="blueprint_soy_motor", import_name=__name__)

@blueprint_soy_motor.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from blueprint_x."}
    return jsonify(output)

@blueprint_soy_motor.route('/get_all_news', methods=['GET'])
def get_all_news():

    final_newslist=[]
    final_newslist=NewsSoyMotor.get_news('A','titular') +NewsSoyMotor.get_news('B','subtitular')+NewsSoyMotor.get_news('C','subtitulo')
    json_data = json.dumps([ob.__dict__ for ob in  final_newslist])

    return json_data

@blueprint_soy_motor.route('/get_unique_news_content', methods=['GET'])
def get_news():
    url=str(request.args['url'])
    
    response={
        'html_content':str(NewsSoyMotor.get_unique_news_content(url))
    }
    
    return response
    

    
    