from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

def fake_useragent_useragents_(is_):
    ua = UserAgent()
    if is_ == 'random':
        return ua.random

def quiktrak_user_entry_check(email_is, proxy_url_):
    try:
        cookies = {
            'ASP.NET_SessionId': 'ugcedvj5mesgfx45v3lwpy45',
            'sgOnPage': '',
            'sgSubPage': '',
            'sgFromPage': '',
            'sgDrillDown': '',
            'ASPSESSIONIDCWBATDRB': 'AOBMJKNCDIEEMCMNKOCPNKEL',
        }

        headers = {
            'authority': 'secure.quiktrak.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'ASP.NET_SessionId=ugcedvj5mesgfx45v3lwpy45; sgOnPage=; sgSubPage=; sgFromPage=; sgDrillDown=; ASPSESSIONIDCWBATDRB=AOBMJKNCDIEEMCMNKOCPNKEL',
            'cp-extension-installed': 'Yes',
            'origin': 'https://secure.quiktrak.com',
            'referer': 'https://secure.quiktrak.com/ext/shared/LoginAssistance.asp?username=',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': fake_useragent_useragents_('random'),
        }

        data = {
            'ForgotOption': 'Password',
            'Username': '',
            'Email1': email_is,
            'Email2': '',
        }

        response = requests.post('https://secure.quiktrak.com/ext/shared/LoginAssistance.asp', proxies=proxy_url_, cookies=cookies, headers=headers, data=data)

        # print(response)
        # print(response.text)

        soup = BeautifulSoup(response.text, 'html.parser')

        pattern_is_not_found="User not found."
        pattern_is_found = ""

        # _ = soup.find_all('body', string = pattern)

        is__ = pattern_is_not_found in soup.text

        if is__:
            return False
        else:
            return True
        
    except:
        return 'Try Again'
