# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import BotEngine

# Create your views here.

def index(request):
    return render(request, 'chatbot/index.html')


def chatResponse(request):
    msg = request.GET["msg"]
    resp = BotEngine.chatbot.get_response(msg)
    return HttpResponse(str(resp))
