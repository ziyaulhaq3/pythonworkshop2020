import time
from datetime import datetime as dt
website_list=["www.facebook.com","www.instagram.com","www.youtube.com","www.crunchyroll.com","www.zomato.com"]
host_path=r"/etc/hosts"
temp = r"hosts"
redirect="127.0.01"
while True:
    if dt.now ().weekday()<=4:
        if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
            print("working hours",dt.now())
            with open (host_path,"r+") as file:
                content = file.read()
                for website in website_list:
                    if website in content: 
                        pass
                    else:
                        file.write(redirect+" "+website+"\n")
    else:
        with open (host_path,"r+") as file:
            content= file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("fun hours")
    time.sleep(10)
