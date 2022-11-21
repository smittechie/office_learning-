from urllib.request import urlopen
import os
import requests
from bs4 import BeautifulSoup


'''
#tried in different way but indexing was not found properly   

r = requests.get('https://www.google.com/search?q=fog&tbm=isch&ved=2ahUKEwis_6y1mb_7AhVljNgFHe09DCQQ2-cCegQIABAA&oq=fog&gs_lcp=CgNpbWcQAzIECAAQQzIECAAQQzIHCAAQsQMQQzIECAAQQzIICAAQgAQQsQMyBAgAEEMyBAgAEEMyBAgAEEMyBQgAEIAEMgUIABCABFC3CVjnDGCZDmgAcAB4AIABngGIAa0EkgEDMC40mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=yWR7Y-z2POWY4t4P7fuwoAI&bih=795&biw=1707')
print(r)
print(r.content)
print(r.url)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent.name)

# s = soup.find('div',class_='OcgH4b Oqwwc')
# print(s)
'''


Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

Image_Folder = 'Images_1'

def main():
    if not os.path.exists(Image_Folder):
        os.mkdir(Image_Folder)
    download_images()

def download_images():
    data = input('Enter your search keyword: ')
    num_images = int(input('Enter the number of images you want: '))

    print('Searching Images....')
    search_url = Google_Image + 'q=' + data

    response = requests.get(search_url, headers=u_agnt)
    html = response.text
    b_soup = BeautifulSoup(html, 'html.parser')
    results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
    print(results)

    count = 0
    imagelinks = []
    for res in results:
        try:
            link = res['data-src']
            imagelinks.append(link)
            count = count + 1
            if (count >= num_images):
                break

        except KeyError:
            continue


    print(f'Found {len(imagelinks)} images')
    print('Start downloading...')

    for i, imagelink in enumerate(imagelinks):
        response = requests.get(imagelink)

        imagename = Image_Folder + '/' + data + str(i + 1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)

    print('Download Completed!')


if __name__ == '__main__':
    main()