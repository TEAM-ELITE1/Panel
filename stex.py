import requests,json,platform,os,time
from concurrent.futures import ThreadPoolExecutor

loop=0


def _clear_():
    os.system('cls' if os.name == 'nt' else 'clear')

def ____OPENURL____(url):
    if platform.system() == "Linux":
        os.system(f"xdg-open {url}")
    elif platform.system() == "Windows":
        os.system(f"start {url}")
    else:
        pass
    time.sleep(0.5)
    



____OPENURL____('https://t.me/savageautomation')


def main():
    _clear_()
    session=requests.session()
    headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 15; 23090RA98G Build/AP3A.240905.015.A2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7632.26 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Android WebView";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'upgrade-insecure-requests': '1',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',} 
    responseX = session.get('https://stexsms.com/mauth/login', headers=headers)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 15; 23090RA98G Build/AP3A.240905.015.A2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7632.26 Mobile Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Android WebView";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?1',
    'origin': 'https://stexsms.com',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': responseX.url,
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'priority': 'u=1, i',}
    
    email=input(' Email >>> ')
    password=input(' password >>> ')
    try:
        limite=int(input(" Input Limit:"))
    except:
        limite=1000
    
    json_data = {
    'email': email,
    'password': password,}
    response = session.post('https://stexsms.com/mapi/v1/mauth/login', headers=headers, json=json_data)
    mauthtoken=json.loads(response.text)['data']["token"]
    rangename=input(' Range_Name >>> ')

    cookies = {
    'mauthtoken': mauthtoken,}

    headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 15; 23090RA98G Build/AP3A.240905.015.A2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7632.26 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Android WebView";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'upgrade-insecure-requests': '1',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',}

    params = {
    'range': rangename,}
    responseA = session.get('https://stexsms.com/mdashboard/getnum', params=params, cookies=cookies, headers=headers)
    
    with ThreadPoolExecutor(max_workers=2) as savage:
        for i in range(limite):
            savage.submit(fathcer,mauthtoken,session,responseA,rangename,cookies)
    


def fathcer(mauthtoken,session,responseA,rangename,cookies):
    global loop
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 15; 23090RA98G Build/AP3A.240905.015.A2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7632.26 Mobile Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'sec-ch-ua-platform': '"Android"',
        'mauthtoken': mauthtoken,
        'sec-ch-ua': '"Not:A-Brand";v="99", "Android WebView";v="145", "Chromium";v="145"',
        'sec-ch-ua-mobile': '?1',
        'origin': 'https://stexsms.com',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': responseA.url,
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'priority': 'u=1, i',}
    
        json_data = {
        'range': rangename,
        'is_national': False,
        'remove_plus': False,}
        response = session.post('https://stexsms.com/mapi/v1/mdashboard/getnum/number', cookies=cookies, headers=headers, json=json_data)
        print(response.text)
        number=response.json()["data"]["copy"]
        print(f"[SAVAGE-STEX] [{str(loop)}] >>> {number}")
        loop+=1
        open("/sdcard/stex_sms-number.txt","a").write(number+'\n')
    except Exception as e:
        print(e)
        time.sleep(2)



main()