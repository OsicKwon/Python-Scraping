import requests
from bs4 import BeautifulSoup
import time

cookies = {
    'CP_IsMobile': 'false',
    'ASP.NET_SessionId': 'flnuaipnxe2te03t0t1ywt2z',
    'dpi': '1',
    'viewportHeight': '946',
    'screenWidth': '1920',
    'screenHeight': '1080',
    '__RequestVerificationToken': '-LP4Gpb2GVHa8-HflmW6cMHJ4B1XWdf1iUNhxMFC1krVTO11Gkr4s-JcxoBMt_mHsPL73MsM-zxzhPX42RCedZe_NlCG3hhCqP53jtweRtc1',
    'CP_TrackBrowser': '{"doNotShowLegacyMsg":false,"supportNewUI":true,"legacy":false,"isMobile":false}',
    'recollect-locale': 'en-US',
    'rCclient': 'B15523F4-5077-11EF-9875-87A648B069BF',
    'ai_user': '7SMDC|2024-08-02T03:13:43.374Z',
    '_gid': 'GA1.2.2103381297.1722568424',
    'ai_session': 'ViUhE|1722568423958.2|1722568423958.2',
    '_ga': 'GA1.2.100497323.1722568424',
    '_ga_QVL1ZEBZ3Y': 'GS1.2.1722568424.1.1.1722568436.0.0.0',
    '_ga_EVME8ZYCG2': 'GS1.1.1722568424.1.1.1722568437.0.0.0',
    'viewportWidth': '1006',
    'responsiveGhost': '1',
}

headers = {
    'authority': 'greenburghny.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'CP_IsMobile=false; ASP.NET_SessionId=flnuaipnxe2te03t0t1ywt2z; dpi=1; viewportHeight=946; screenWidth=1920; screenHeight=1080; __RequestVerificationToken=-LP4Gpb2GVHa8-HflmW6cMHJ4B1XWdf1iUNhxMFC1krVTO11Gkr4s-JcxoBMt_mHsPL73MsM-zxzhPX42RCedZe_NlCG3hhCqP53jtweRtc1; CP_TrackBrowser={"doNotShowLegacyMsg":false,"supportNewUI":true,"legacy":false,"isMobile":false}; recollect-locale=en-US; rCclient=B15523F4-5077-11EF-9875-87A648B069BF; ai_user=7SMDC|2024-08-02T03:13:43.374Z; _gid=GA1.2.2103381297.1722568424; ai_session=ViUhE|1722568423958.2|1722568423958.2; _ga=GA1.2.100497323.1722568424; _ga_QVL1ZEBZ3Y=GS1.2.1722568424.1.1.1722568436.0.0.0; _ga_EVME8ZYCG2=GS1.1.1722568424.1.1.1722568437.0.0.0; viewportWidth=1006; responsiveGhost=1',
    'pragma': 'no-cache',
    'referer': 'https://greenburghny.com/Search?searchPhrase=&pageNumber=1&perPage=10&departmentId=-1',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

page_number: int = 1

while True:
    time.sleep(2)
    params = {
        'searchPhrase': '',
        'pageNumber': page_number,
        'perPage': '50',
        'departmentId': '-1',
    }

    response = requests.get('https://greenburghny.com/Search/Results', params=params, cookies=cookies, headers=headers)
    print(response.status_code)
    print(page_number)
    if response.status_code != 200:
        break
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup.find_all('h3'))

    page_number += 1
