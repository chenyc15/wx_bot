# Written by Eason Chen
# 07/04/2017

from wxpy import *
from datetime import datetime
import os
import sys

from apscheduler.schedulers.blocking import BlockingScheduler
from weather import DailyForecast
from personal import get_xiaoi_key, get_xiaoi_secret


def send_daily_msg():
    msg_start = "Good Morning! This message is sent by WeChat Bot by Eason.\n"
    f1 = DailyForecast('San Francisco,CA')
    msg1 = f1.construct_weather_forecast_msg()
    f2 = DailyForecast('Berkeley,CA')
    msg2 = f2.construct_weather_forecast_msg()
    msg = msg_start + msg1 + '\n' + msg2
    dan.send(msg)
    me.send(msg)
    print('The following message is sent at {}: '.format(datetime.now()))
    print(msg)

def run_auto_weather_forecast():
    scheduler = BlockingScheduler()
    scheduler.add_job(send_daily_msg, 'cron', hour=6, minute=0, second=0)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

def run_auto_reply():
    # listen to Dan's message and reply
    @bot.register(dan)
    def reply_my_friend(msg):
        if msg.text == "我爱你":
            return "我也爱你❤"
        else:
            xiaoi.do_reply(msg)
    embed()


if __name__ == '__main__':
    bot = Bot()
    bot.self.send('Wxpy logged in!')
    dan = bot.friends().search('丹逗')[0]
    me = bot.friends().search('CYC')[0]
    xiaoi = XiaoI(get_xiaoi_key(), get_xiaoi_secret())

    if sys.argv[1] == 'weather':
        run_auto_weather_forecast()
    if sys.argv[1] == 'autoreply':
        run_auto_reply()
    else:
        print('''
        Usage:\n
        'python main.py weather' OR \n
        'python main.py autoreply'
        ''')


# bot.logout()
