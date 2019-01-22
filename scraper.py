from bs4 import BeautifulSoup
import os
import requests

link =  'https://ww5.readsnk.com/chapter/shingeki-no-kyojin-chapter-000'

for i in range(112):
    if (i<9):
        num= link[-1:]
        num=int(num)
        num+=1
        link= link[:-1]+str(num)
    elif(i>=9 and i<99):
        num= link[-2:]
        num=int(num)
        num+=1
        link= link[:-2]+str(num)
    elif(i>=99 and i<110):
        num= link[-3:]
        num=int(num)
        num+=1
        link= link[:-3]+str(num)
    try:
        os.mkdir('Chapter '+str(i+1))
        os.chdir('./'+'Chapter '+str(i+1))
        response = requests.get(link)
        page = BeautifulSoup(response.text,'html.parser')
        images = page.find_all('img',{
            'class': 'pages__img'
        })

        
        for index,img in enumerate(images,start=1):
            image= requests.get(img.get('src'))
            name=str(index)+'.png'
            with open(name,'wb') as f:
                f.write(image.content)

        os.chdir('..')
    except FileExistsError:
        print('chapter ' + str(i+1)+' already exists')
        
        

        

        

