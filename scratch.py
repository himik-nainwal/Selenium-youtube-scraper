import requests
import warnings 

from bs4 import BeautifulSoup
youtube_link ='https://www.youtube.com/feed/trending'

response =requests.get(youtube_link)
'''' print('Status code',response.status_code) 200 is success 404 is not found
print('Output',response.text) 
with open('trending.html','w') as f:
  f.write(response.text)
'''

doc=BeautifulSoup(response.text,'html.parser')
video_divs =doc.find_all('div',class_='ytd_video-renderer')
print(f'Found {len(video_divs)} videos')
