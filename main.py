from bs4 import BeautifulSoup as BS
import requests
import threading

def sound_cloud_downdload(link_sound_cloud):
	header = {
	    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
	}


	data_link = {'value': link_sound_cloud}

	try:
		r = requests.post('https://www.klickaud.co/download.php', data=data_link, headers=header)
		soup = BS(r.text, 'html.parser')

		titles = soup.find('td' ,class_ = 'no-mobile1')
		name = soup.find_all('td' ,class_ = 'small-10 columns')[1].text.strip()
		link_music = titles.find('a').get('href')
		photo_link = soup.find('td', class_ = 'small-10 columns')
	        
		#Загрузка трека
		r = requests.get(link_music)
		with open(f"{name}.mp3", "wb") as file:
			file.write(r.content)

		#Загрузка фото
		r_photo = requests.get(photo_link.find('img')['src'])
		with open(f"{name}.jpg", "wb") as file_photo:
			file_photo.write(r_photo.content)


	except:
		print('😕Ошибка!')


if __name__ in "__main__":
	link_sound_cloud = input("Enter URL--->  ")
	threading.Thread(target=sound_cloud_downdload(link_sound_cloud))