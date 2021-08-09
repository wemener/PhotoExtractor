import requests
import http.cookiejar as cj
import os
import json
from bs4 import BeautifulSoup


login_url = "https://filomenaphotography.shootproof.com/gallery/15708568/auth"

session = requests.session()
jar = cj.CookieJar()
response = session.get(login_url, cookies=jar).text
soup = BeautifulSoup(response, 'html.parser')

username = "kmedina729@gmail.com"

login_headers = {"Origin": "https://filomenaphotography.shootproof.com/",
                 "Upgrade-Insecure-Requests": "1",
                 "Connection": "keep-alive",
                 "Accept": "application/json",
                 "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
                 "Referer": "https://filomenaphotography.shootproof.com/gallery/15708568",
                 }
data = {
    "email": username,
}

login_post = session.post(login_url, headers=login_headers,
                          cookies=jar, data=data)
if login_post.status_code != 200:
    print(
        f"Error trying to retrieve Log In: {response.status_code}. Please check your credentials")
else:
    photo_url = "https://filomenaphotography.shootproof.com/gallery/15708568/home"
    get_photo_headers = {"Origin": "https://filomenaphotography.shootproof.com/",
                         "Upgrade-Insecure-Requests": "1",
                         "Connection": "keep-alive",
                         "Accept": "application/x-www-form-urlencoded",
                         "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
                         "Referer": "https://www.yext.com/taskprocessing2/users",
                         }
