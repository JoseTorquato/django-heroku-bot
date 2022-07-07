from __future__ import print_function

import datetime
import os.path
from asyncio import events
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from bot.screenshot_organizer import google_calendar


def index(request):
    if request.method=='POST' and request.POST.get("value", ""):
        google_calendar(request.POST.get("user_telegram", ""))

    if request.method=='POST' and request.POST.get("Calendar", ""):
        events = google_calendar()
        
        return render(request, 'cadastrando.html', {"events": events})
    return render(request, 'cadastrando_base.html')
    