# 基于密保问题，自动解锁Apple ID，自动关闭双重认证，提供前端账号展示，支持多账号

import requests

def get_ip():
   response = requests.get('https://api64.ipify.org?format=json').json()
   return response["ip"]

def get_location():
   ip_address = get_ip()
   response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
   location_data = {
       "ip": ip_address,
       "city": response.get("city"),
       "region": response.get("region"),
       "country": response.get("country_name")
   }
   return location_data

print(get_location())
