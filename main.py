from wxpy import *
from weather import DailyForecast
from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

bot = Bot()
bot.self.send('Wxpy logged in!')
dan = bot.friends().search('丹逗')[0]
me = bot.friends().search('CYC')[0]

def send_daily_msg():
    msg_start = "Good Morning!\n"
    f1 = DailyForecast('San Francisco,CA')
    msg1 = f1.construct_weather_forecast_msg()
    f2 = DailyForecast('Berkeley,CA')
    msg2 = f2.construct_weather_forecast_msg()
    msg = msg_start + msg1 + '\n' + msg2
    me.send(msg)
    print('The following message is sent at {}: '.format(datetime.now()))
    print(msg)

# @bot.register()
# def record_message(msg):
#     print("Sender: {}, receive time: {}, content: {}".format(msg.sender, msg.receive_time, msg.text))
#
# # listen to Dan's message and reply
# @bot.register(dan)
# def reply_my_friend(msg):
#     return_msg = 'received: {} ({})'.format(msg.text, msg.type)
#     if msg.text == "我爱你":
#         return_msg = "我也爱你❤"
#     if msg.text == "天气":
#         f = DailyForecast('Berkeley,CA')
#         return_msg = f.construct_weather_forecast_msg()
#     print(msg)
#     return return_msg

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(send_daily_msg, 'cron', hour=6, minute=0, second=0)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

# embed()

# bot.logout()
