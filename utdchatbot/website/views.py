from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('Utd Bot')

chatbot = ChatterBotCorpusTrainer(chatbot)

# Train based on the english corpus
#chatbot.train("chatterbot.corpus.english")

# Create your views here.

def homepage(request):
    return render(request, 'website/index.html')

def chatbot(request):
    return render(request, 'website/chatbot.html')

def get_response(request):
	response = {'status': None}

	if request.method == 'POST':
		data = json.loads(request.body)
		message = data['message']

		chat_response = chatbot.get_response(message).text
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)

