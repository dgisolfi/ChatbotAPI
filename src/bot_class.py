#!/usr/bin/python3
# bot_class.py
# 2018-07-29
# Purpose: create a class that represents each instance of a bot 
# interacting with the groupme chatbot API

class Bot:
	def __init__(self, bot_name, bot_id, group_id, api_token):
		print('bot:%s created' % bot_name) 
		self.bot_name =  bot_name
		self.bot_id =    bot_id
		self.group_id =  group_id
		self.api_token = api_token
	
	def getBotName(self):
		return self.bot_name

	def getBotID(self):
		return self.bot_id

	def getGroupID(self):
		return self.group_id

	def getApiToken(self):
		return self.api_token
