import requests

from bs4 import BeautifulSoup

HEADERS = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}

def print_welcome():
    print("""

██   ██ ██    ██  ██████  ███████ ████████  ██████  ██    ██         
 ██ ██  ██    ██ ██  ████ ██         ██    ██  ████ ██    ██         
  ███   ██    ██ ██ ██ ██ ███████    ██    ██ ██ ██ ██    ██         
 ██ ██   ██  ██  ████  ██      ██    ██    ████  ██  ██  ██          
██   ██   ████    ██████  ███████    ██     ██████    ████   ███████ 




# Граббер публичных прокси

# Telegram: https://t.me/xvostov_k
# Email: Xvostov.k@yandex.ru

""")

def main():
    print_welcome()
    proxy_list = check_hidemy()
    print(proxy_list)

def check_hidemy():
    proxy_list = []

    session = requests.Session()
    session.headers.update(HEADERS)

    base_url = "https://hidemy.name/ru/proxy-list/"

    response = session.get(base_url)
    content = response.text

    soup = BeautifulSoup(content, "lxml")

    max_items = int(soup.find("div", class_="pagination").find_all("li")[-2].find("a").get("href")[22:-5])


    for p in range(1, max_items+64, 64):
        if p != 1:
            response = session.get(f"{base_url}?start={p}#list")

        else:
            response =session.get(f"{base_url}#list")

        content = response.text
        soup = BeautifulSoup(content, "lxml")

        trs = soup.find_all("tr")

        for tr in trs:
            tds = tr.find_all("td")
            print(tr)
            # print(tds[4])
            if tds[4].text == "HTTP" or tds[4].text == "HTTPS":

                proxy = tds[0].text.strip()

                port = tds[1].text

                proxy_list.append({"ip": proxy, "port": port})

    return proxy_list # Возвращается список словарей


if __name__ == '__main__':
    main()