from bs4 import BeautifulSoup as bs
import requests as rq
import re
import pandas as pd

def html_to_find(url,proxi,tag,string):
     
    def get_html(url,proxi):
        html = rq.get(url,proxi)
        print(f'url is {url} html cod is {html}')
        return html

    def make_soup(html,tag,string):
        data ={}
        soup = bs(html.text,'lxml')
        data_body = soup.find_all(tag[0],string[0])
        data_stars = soup.find_all(tag[1],string[1])
        data={'stars':data_stars,'body':data_body}
        return data 
    
    def make_df(data):
        df={'body':[],
           'stars':[]}
        
        data_body =[str(data['body'][i])for i in range(len(data['body']))]
        data_stars =[str(data['stars'][i])for i in range(len(data['stars']))]
        print(f'data_body{data_body} ,data_stars{data_stars}')
        for body,star in zip(data_body,data_stars):
            df['body'].append(''.join(re.findall(r'.*</strong>\s*.(.*)</div>',body)))            
            df['stars'].append(''.join(re.findall(r""" ('*<span class="star[ fill]*">.</span>['"])""",star)))
            
       
        return df
    
    data =get_html(url,proxi)
    soup_filtered =make_soup(data,tag,string)
    df=make_df(soup_filtered)
    return df
    
    # http=127.0.0.1:51214;https=127.0.0.1:51214;socks=127.0.0.1:51213
proxi={'http':"127.0.0.1:51214",'https':"127.0.0.1:51214"}
df1=pd.DataFrame(columns=['body','stars'])
c=0
for i in range(1,5):
    c+=1
    print(f'c is {c}')
    url=f'https://www.airlinequality.com/airline-reviews/volotea/page/{i}/'
    
    df=html_to_find(url=url,
                    proxi=proxi
                    ,tag=['div','span'],
                    string=[{'class':"text_content" ,'itemprop':"reviewBody"},
                           {'class':"star"}])
    # print(df)
    df=pd.DataFrame(df)
    df1=pd.concat([df1,df])
    df1.reset_index(drop=True,inplace=True)
# print(df1.info())
# print(df1)

