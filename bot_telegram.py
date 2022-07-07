from __future__ import print_function

import asyncio
import csv
import datetime
import os.path
import subprocess
import time

import pytz
import requests
import schedule
import telebot
import telegram

from bot.screenshot_organizer import google_calendar_bot

CHAVE_API = "5186043948:AAH7zvUZMCWcsZpZt7W4HZzXVoGdO_UMSo4"
def send(chat_id="699687173", msg="olá"):
    bot = telegram.Bot(token=CHAVE_API)
    print(bot.get_me())
    print(bot.send_message(chat_id, msg))
    # link = f'api.telegram.org/bot={CHAVE_API}/sendMessage?chat_id={chat_id}&text={msg}'
    # response = requests.get(link)
    # print(response)


app = telebot.TeleBot(__name__)


def geeks():
    with open('registry.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        for row in csv_reader:
            print(row)
            tele(row[0], row[1])

# Task scheduling
# After every 10mins geeks() is called.
schedule.every(1).minutes.do(geeks)

def start_schedule(a,b):
    while True:
        schedule.run_pending()
        time.sleep(10)
        print(".......")



@app.route('/registry ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    username = message.get("from", {}).get("username", "")
    print(chat_dest, username)
    with open(f'registry.csv', 'a') as token:
        token.write(f"{chat_dest};{username}")
    send(chat_dest, f"Muito obrigado por registrar {username}")
    # events = google_calendar_bot(username)

    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     end = event['end'].get('dateTime', event['end'].get('date'))
    #     event_start_date = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S%z')
    #     event_end_date = datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M:%S%z')
    #     now = datetime.datetime.now(tz=pytz.timezone("America/Sao_Paulo"))

    #     dif = int((event_start_date - now).total_seconds())

    #     event_title = event.get('summary', '')
    #     if dif < 600 and dif >= 0:
    #         msg = f"Nao se esqueca seu proximo compromisso comeca em 10 minutos\n Data inicio: {event_start_date}\n Nome: {event_title}"
    #         app.send_message(chat_dest, msg)

@app.route('/agenda-ativar ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    username = message["from"]["username"]
    # start_schedule(chat_dest, username)


def tele(chat_dest, username):
    events = google_calendar_bot(username)
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        event_start_date = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S%z')
        event_end_date = datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M:%S%z')
        now = datetime.datetime.now(tz=pytz.timezone("America/Sao_Paulo"))
        
    
        dif = int((event_start_date - now).total_seconds())
        print(dif)
        event_title = event.get('summary', '')
        if dif <= 600 and dif >= 0:
            msg = f"Nao se esqueca seu proximo compromisso comeca em 10 minutos\n Data inicio: {event_start_date}\n Nome: {event_title}, usuario: {username}"
            result = send(chat_dest, msg)
            print(result)


if __name__ == '__main__':
    app.config['api_key'] = CHAVE_API
    app.poll(debug=True)
