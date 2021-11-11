## The Bitly API  
This project will check input link on belonging of Bitly. If link belongs to Bitly, output will show count clicks. If link doesn't belong to Bitly, output will show shorten link. 

## Requirements  
python==3.10.0  
python-dotenv==0.19.1  
requests==2.26.0  

## How to install  
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:  
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
## Examples  
```
asivolap$ python3 count_clicks.py 
Пожалуйста, напишите url: https://google.com
https://bit.ly/3iIygQn  

asivolap$ python3 count_clicks.py 
Пожалуйста, напишите url: https://bit.ly/3iIygQn
('Общее количество кликов =', 2)

asivolap$ python3 count_clicks_argparse.py https://google.com
https://bit.ly/3iIygQn

asivolap$ python3 count_clicks_argparse.py https://bit.ly/3iIygQn
('Общее количество кликов =', 2)

```

