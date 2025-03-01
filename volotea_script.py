from bs4 import BeautifulSoup as bs
import requests as rq
import re

def html_to_find(url,proxi,tag,string):
     
    def get_html(url,proxi):
        html = rq.get(url,proxi)
        print(html)
        return html

    def make_soup(html,tag,string):
        soup = bs(html.text,'lxml')
        data = soup.find_all(tag,string)
        return data    
    
    
    
    data =get_html(url,proxi)
    soup_filtered =make_soup(data,tag,string)
    return soup_filtered
    
    
    
    


proxi={'http':"127.0.0.1:58183",'https':"127.0.0.1:58183"}
url='https://www.airlinequality.com/airline-reviews/volotea/page/3/'



data=html_to_find(url=url,proxi=proxi,tag='div',string={'class':"text_content" ,'itemprop':"reviewBody"})
data=[(''.join (str(data[i])[3:]))for i in range(len(data))]
# data=', '.join(data)
# data.replace('/n','')
d = [re.findall(r'.*</strong>(.*)</div>',st)for st in data]
    


print(d)
