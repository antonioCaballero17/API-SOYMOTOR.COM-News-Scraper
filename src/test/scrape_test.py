from bs4 import BeautifulSoup, Comment
import urllib.request

from src.utils import clear_html

class NewsSoyMotor:
    def __init__(self, title, href,img,date,tag,importance):
        self.title = title
        self.href = href
        self.img = img
        self.date = date
        self.tag = tag
        self.importance=importance

        
    def get_news(soup,importance,titular):
        newslist=[]
        news=soup.find_all("h2",{'class':titular})
        for eachnews in news:
            title=eachnews.parent.find('h2',{'class':titular}).find('a').get('title')
            href=eachnews.parent.find('h2',{'class':titular}).find('a').get('href')
            date=eachnews.parent.find('span',{'class':'fecha'}).string.split(' | ')[1]
            try:
                tag=eachnews.parent.find('div',{'class':'antetitulo'}).string
            except:
                tag='C'
            try:
                img=eachnews.parent.find('img').get('data-src').split('?')[0]
            except:
                try:
                    img=eachnews.parent.parent.find('img').get('data-src').split('?')[0]
                except:
                    img='None'
            try:
                newsObject=NewsSoyMotor(
                    title=title,
                    href=href,
                    date=date,
                    tag=tag,
                    img=img,
                    importance=importance
                )
                newslist.append(newsObject)
            except:
                print('Fallo')

        return newslist 

def get_image(soup):
    news=soup.find_all("h2",{'class':'subtitulo'})
    for new in news:
        print(new.parent.parent.find('img').get('data-src').split('?')[0])
    return 'prueba'
    
    



def get_unique_news_content(url):    
    req=urllib.request.Request(url,headers={'User-Agent': 'Chrome/41.0.2272.96'})    
    html=urllib.request.urlopen(req).read()    
    soup=BeautifulSoup(html,"html.parser")
    html=[]
    h1=soup.find("h1",{'class':'supertitular'})
    h2=soup.find_all('h2',{'class':'item'})
    img=soup.find('span',{'class':'media'}).find('img',{'typeof':'foaf:Image'})
    tag=soup.find("div",{'class':'cuerpo mb mt'})
    h3=tag.find('h3',{'class':'entradilla'})
    ps=tag.find_all('p')
    html.append(str(h1))
    for h in h2:
        html.append(str(h))
    html.append(str(img))
    html.append(str(h3))
    for p in ps:
        html.append(str(p))
    html_string=''.join(html)
    html_tag=BeautifulSoup(html_string,'html.parser')  
    
    html_tag.find('p',{'class':'rtecenter'}).decompose()
    for div in html_tag.find_all('div',{'class':'display-ad'}):
        div.decompose()    
  
    return clear_html(html_tag)
    
    




