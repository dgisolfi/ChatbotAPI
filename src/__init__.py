#!/usr/bin/python3
# routes.py
# 2018-07-28
# Purpose: To serve as a Rest API for ChatBots
# V3

import time
import os
import json
import markdown
import requests
from bot_class import Bot
from flask_restful import Resource, Api, reqparse
from flask import Flask, render_template, redirect, url_for, request, jsonify
 
 #Create instance of flask
app = Flask(__name__)

# Create API
api = Api(app)

#define port for API to run on
apiPort = 5525
apiVersion = 'V3'
chatbot = None


@app.route('/', methods=['GET', 'POST'])
def index():
	#Show Documentation for the API
	markdown_file = open('README.md', 'r')
	content = markdown_file.read()
	# Convert to HTML
	return markdown.markdown(content), 200

@app.route('/registerBot', methods=['POST'])
def registerBot():
    data = request.data
    botArgs = json.loads(data)

    bot_name = botArgs['bot_name']
    bot_id = botArgs['bot_id']
    group_id = botArgs['group_id']
    api_token = botArgs['api_token']

    if 'bot_name' and 'bot_id' and 'group_id' and 'api_token' in botArgs:
        global chatbot
        chatbot = Bot(bot_name,bot_id, group_id, api_token)
        return jsonify({'message': 'Bot registered', 'data': botArgs}), 201
    else:
        return jsonify({'message': 'Bot NOT registered; missing arg(s)', 'data': botArgs}), 206

@app.route('/viewBots', methods=['GET'])
def getBot():
	try:
		return jsonify(
			{
				'message': 'Bot Details',
				'data':	{
						'bot_name':chatbot.getBotName(),
						'bot_id':chatbot.getBotID(),
						'group_id':chatbot.getGroupID(),
						'api_token':chatbot.getApiToken()
					}
			}), 200
	except:
		return jsonify(
		{
			'message': 'No Bot Created',
			'data': 'None'
		}), 404


@app.route('/sendMsg', methods=['GET', 'POST'])
def sendMsg():
	data = request.data
	msgArgs = json.loads(data)

	try:
		msg = msgArgs['msg'] 
		if chatbot.getBotName() in msg.lower():
			msg.lower().replace(chatbot.getBotName(), "")

		post_params = { 'bot_id' : chatbot.getBotID(), 'text': msg }
		requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
		return jsonify({'message':'Message Sent', 'data': msg}), 200
	except:
		return jsonify({'message':'Unable to send message', 'data': msg}), 400

@app.route('/requestMessages', methods=['GET'])
def getMsg():
	try:
		response = requests.get(
			'https://api.groupme.com/v3/groups/' + str(chatbot.getGroupID()) + '/messages', 
			params = {'token': chatbot.getApiToken()})
		messages = response.json()
		return jsonify({'message':'Message Request Successful', 'data': messages}), 200	

	except:
		return jsonify({'message':'Message Request Not Successful', 'data': None}), 404

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=apiPort)