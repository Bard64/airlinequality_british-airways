from bs4 import BeautifulSoup as bs
import requests as rq
import re
import pandas as pd

def html_to_find(url,proxi,tag,string):
     
    def get_html(url,proxi):
        html = rq.get(url,proxi)
        print(f'url:{url} is {html}')
        return html

    def make_soup(html,tag,string):
        soup = bs(html.text,'lxml')
        data = soup.find_all(tag,string)
        return data    
    
    def make_df(data):
        data=[str(data[i])for i in range(len(data))]
        df={}
        for st,i in zip(data,range(0,len(data))):
            df[i] = ''.join(re.findall(r'.*</strong>\s*.(.*)</div>',st))
        
        df=pd.DataFrame(df.values())
       
        return df
    
    data =get_html(url,proxi)
    soup_filtered =make_soup(data,tag,string)
    df=make_df(soup_filtered)
    return df
    
    
    
proxi={'http':"127.0.0.1:58183",'https':"127.0.0.1:58183"}
df1=pd.DataFrame(columns=['body'])

for i in range(1,4):
    url=f'https://www.airlinequality.com/airline-reviews/volotea/page/{i}/'
    
    df=html_to_find(url=url,proxi=proxi,tag='div',string={'class':"text_content" ,'itemprop':"reviewBody"})
    df1=pd.concat([df1,df])

print(df1.info())








