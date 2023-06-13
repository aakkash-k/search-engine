
import urllib.request 
from bs4 import BeautifulSoup
def reverseStr(url):
    ret = ""
    for i in range(len(url)-1, 0, -1):
        ret+=url[i]
    return ret
#reformatting the string to callable url
def reFormat(url):
    ret = ""
    for ind in range(len(url)-1, 0, -1):
        if len(ret)>=4 and ret[len(ret)-4:]=="www.":
            return reverseStr(ret)
        if url[ind]=='/' and (len(ret)>=1 and ret[len(ret)-1]=='/'):
            return "www."+reverseStr(ret[:-1])
        else:
            ret+=url[ind]
    return str(reverseStr(ret))
url = "<----URL---->"
sites = {'<--ROBOT.TXT-->': ['<---URL IN ROBOT>TXT--->']}
for site in sites.keys():
    for i in sites.get(site):
        # html = urllib.request.urlopen(i)  

        # htmlParse = BeautifulSoup(html, 'html.parser')

        # print(htmlParse)
        print(reFormat(i)[len(reFormat(i))-4:])