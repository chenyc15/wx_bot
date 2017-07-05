# WeChat Bot


## Version
- v1 (07/04/2017)
Project start
- v1.1 (07/04/2017)
Add XiaoI for auto reply

## Introduction
This bot automatically send daily weather forecast to certain users in the morning.

## Usage
Modify the **personal_template.py** (see details in the file) and run the following in terminal/cmd:
Run Auto Reply using XiaoI(See [XiaoI](http://www.xiaoi.com/))
```
python main.py autoreply
```
Run daily weather forecast notification:
```
python main.py weather
```

## Dependencies
- Wxpy 0.3.9.8 ([doc](http://wxpy.readthedocs.io/zh/latest/))
- APScheduler 3.3.1 ([doc](http://apscheduler.readthedocs.io/en/latest/index.html))
- OpenWeatherMap API (See [OpenWeatherMap](https://openweathermap.org/))


## TODO
- Integrate multiple functions
