import requests
from bs4 import BeautifulSoup

cookies = {
    # cookies
}

headers = {
    # headers
}

base_url = ""
page_number: int = 1


def main():

    while True:
        params = {
            'pageNumber': page_number,
        }
    
        response = requests.get(base_url, params=params, cookies=cookies, headers=headers)
        print(response.status_code)
    
        if response.status_code != 200:
            break
            
        soup = BeautifulSoup(response.content, "html.parser")
        print(soup.find_all('h1'))
    
        page_number += 1


if __name__ == "__main__":
    main()
    
