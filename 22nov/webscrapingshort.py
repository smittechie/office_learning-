import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd


lst=[]
response = requests.get('https://www.google.co.in/search?q=puppy+&hl=en-GB&tbm=isch&source=hp&biw=1707&bih=795&ei=Bo18Y5T2N8WlhwPpyKbAAw&iflsig=AJiK0e8AAAAAY3ybFsUboQwNPh2lQvCdPV3f2jFRVK4E&ved=0ahUKEwiUkZv3s8H7AhXF0mEKHWmkCTgQ4dUDCAc&uact=5&oq=puppy+&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgARQkAZYqA1g8RRoAXAAeACAAXaIAZwFkgEDMC42mAEAoAEBqgELZ3dzLXdpei1pbWewAQA&sclient=img')
html = response.text
b_soup = BeautifulSoup(html, 'html.parser')
print(b_soup.prettify())
images = b_soup.select('div img')
src=[]

for img in images:
        src.append(img['src'])
print(src)
src.pop(0)
print(len(src))


# for i in src:
#     response = requests.get(i)
#     a=random.randint(0, 1000)
#     with open(f'imagename{a}.jpg', 'wb') as file:
#         file.write(response.content)

df = pd.DataFrame(src)
print(df)
df.to_excel("scrap.xlsx")
df.to_csv("scrapy.csv")



# count = 0
# for i in src:
#     count = 0
#     while count < 10:
#         try:
#             response = requests.get(src)
#             with open(f'imagename{count}.jpg', 'wb') as file:
#                 file.write(response.content)
#                 count += 1
#         except KeyError :
#             continue
#         except (InvalidSchema, MissingSchema) as err:
#             raise InvenioConnectorServerError(
#                 "Bad schema, expecting http:// or https://:\n %s" % (err,))
#             continue


# for a in b_soup.findAll('a',href=True):                                                       #('a',href=True):
#     print("Found the URL:", a['href'])                                                               #a['href']
#     # r = requests.get(a['href'], allow_redirects=True)
#     # print(r)