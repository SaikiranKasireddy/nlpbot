from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from .forms import NameForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.http import HttpResponseRedirect


# from chatterbot.trainers import ChatterBotCorpusTrainer
chat = ChatBot('Ron Obvious')

trainer = ChatterBotCorpusTrainer(chat)

# Train based on the english corpus
#trainer.train("chatterbot.corpus.english.greetings")


# Create your views here.

def homepage(request):
    return render(request, 'website/index.html')

def chatbot(request):
	return render(request, 'website/chatbot.html')

@csrf_exempt
def get(request):
    message = request.GET['msg[text]']
    chat_response = chat.get_response(message)
    print(chat_response)
    return HttpResponse(chat_response)
