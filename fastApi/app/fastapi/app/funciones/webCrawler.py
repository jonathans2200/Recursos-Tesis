from bs4 import BeautifulSoup
import requests
import pandas as pd


def webVideoLink(inicio,final):

    lista_video=[]
    lista_descripcion=[]
    lista_identificador=[]
    for num in range(inicio,final+1):
        
        url = 'https://wikinclusion.org/index.php/'+str(num)
    
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        identificador=soup.find('h1',{'class':'firstHeading'})
        
        
        video=soup.find_all('iframe')
        video=[i.get('src') for i in video]
        for i in video:
            cut=i[24:-1]
            lista_video.append(cut)
            lista_identificador.append(identificador.text)
            
        #descripcion=soup.find_all('div',{'class':'embedvideo thumb ev_center autoResize'})
        descripcion1=soup.find_all('div',{'class':'embedvideo ev_center autoResize'})
        for a in descripcion1:
            lista_descripcion.append(a.text)
        
        descripcion=soup.find_all('div',{'class':'embedvideo thumb ev_center autoResize'})
        for j in descripcion:
            lista_descripcion.append(j.text)
        

    df1= pd.DataFrame({'identificador':lista_identificador,'link':lista_video,'descripcion':lista_descripcion})

    return df1





def webProgramaLink(codigo):
    lista_programa=[]
    lista_links=[]
    lista_descripcion=[]
    lista_codigo=[]

    contador=0 
    url = 'https://wikinclusion.org/index.php/'+codigo
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    identificador=soup.find('h1',{'class':'firstHeading'})

    programa= soup.find('dl',{'class':''})
    datos=programa.find_all('dd',{'class':''})
    for i in datos:
        etiqueta=i.find('a')
        url2 = 'https://wikinclusion.org'+etiqueta.get('href')
        page2 = requests.get(url2)
        soup2 = BeautifulSoup(page2.content,'html.parser')
        descripcion= soup2.find('p')
        lista_programa.append(etiqueta.text)
        lista_links.append('https://wikinclusion.org'+etiqueta.get('href'))
        lista_descripcion.append(descripcion.text)
        
        contador+=1
        lista_codigo.append('pro'+str(contador))
        
        
    dfprograma= pd.DataFrame({'codigo':lista_codigo,'identificador':identificador,'nombre':lista_programa,'link':lista_links,'descripcion':lista_descripcion})
    return dfprograma