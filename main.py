from bs4 import BeautifulSoup as BS
from colorama import init
from colorama import Fore, Back, Style
import requests

init()

HEADER = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}


def sound_cloud_downdload(link_sound_cloud):
    data_link = {'value': link_sound_cloud}

    try:
        r = requests.post('https://www.klickaud.co/download.php', data=data_link, headers=HEADER)
        soup = BS(r.text, 'html.parser')

        name = soup.find_all('td', class_='small-10 columns')[1].get_text().strip()
        link_music = soup.find('tr', class_ = 'mobile-grid').find_all('td')[1].find('a').get('href')
        photo_link = soup.find_all('td', class_='small-10 columns')[0].find('img').get('src')

        #Music
        r = requests.get(link_music)
        with open(f"{name}.mp3", "wb") as file:
            file.write(r.content)

        print(Fore.GREEN + f"[+] Good! File saved {name}.mp3")
    except:
        print(Fore.RED + "[!] Error")

    inputUsers()


def tiktok_download(link):
    data_link = {
        'id': link
    }

    r = requests.post(
        'https://ttsave.app/download?mode=video&key=c679452f-fbe4-44ca-827f-8ac7565b0143', data=data_link, headers=HEADER)

    soup = BS(r.text, 'html.parser')
    download_link_div = soup.find('div', {'id': 'button-download-ready'})

    download_link_a = download_link_div.find('a')
    name = soup.find('a', class_='font-extrabold text-blue-400 text-xl mb-2').text.strip()
    if download_link_a:
        download_url = download_link_a['href']
        r = requests.get(download_url)

        with open(f"{name}.mp4", "wb") as file:
            file.write(r.content)

        print(Fore.GREEN + f"[+] Good! File saved {name}.mp4")
    else:
        print(Fore.RED + "[!] Error")

    inputUsers()

def check_link(link):
    if "https://www.tiktok.com/" in link or "https://vm.tiktok.com/" in link:
        tiktok_download(link)

    elif "https://soundcloud.com/" in link or "https://on.soundcloud.com/" in link:
        sound_cloud_downdload(link)

    print(Fore.RED + "[!] Error\n\nSupported TikTok and SoundCloud")
    inputUsers()

def inputUsers():
    link = input(Fore.GREEN + "Enter URL---> ")
    check_link(link)
    link = ''


if __name__ == "__main__":
    inputUsers()