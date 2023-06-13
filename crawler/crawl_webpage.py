import urllib.request 
from bs4 import BeautifulSoup
import requests
import threading
class crawlSites:
    def __init__(self, sites):
        self.sites = sites
    def urlToParser(self, site):
        
        html = urllib.request.urlopen(site)  

        htmlParse = BeautifulSoup(html, 'html.parser')

        return  htmlParse
    def printAllUrlLinked(self, site, depth, visit):
        if depth>=10:
            return
        for url in self.allUrlOfA(self.urlToParser(site)):
            if url not in visit:
                visit[url] = 1
                print(url, depth)
                self.printAllUrlLinked(url, depth+1, visit)
    

    def allUrlOfA(self, parsedSite):
        ret = []
        for tag in parsedSite.find_all('a'):
            try:
                url = tag["href"]

                
                if url.find("https://")==0 or url.find("www.")==0:
                    # try:

                    #     thread1 = threading.Thread(target=self.isAWebssite(url,ret), name="thread1")
                    #     thread2 = threading.Thread(target=self.isAWebssite(url, ret), name = "thread2")
                    #     thread3 = threading.Thread(target=self.isAWebssite(url, ret), name = "thread3")
                    #     thread4 = threading.Thread(target=self.isAWebssite(url, ret), name = "thread4")
                    #     thread5 = threading.Thread(target=self.isAWebssite(url, ret), name = "thread5")
                    #     print(ret)
                    # except Exception as e:
                    #     print(e)
                    ret.append(url)
            except Exception as e:
                print(e)
        return ret
    def getAllHeader(self, parsedSite):
        tag_map = {}
        req_tag = "h1"
        tag_map[req_tag] = self.getDataByTag(parsedSite, req_tag)
        req_tag = "h2"
        tag_map[req_tag] = self.getDataByTag(parsedSite, req_tag)
        req_tag = "h3"
        tag_map[req_tag] = self.getDataByTag(parsedSite, req_tag)
        req_tag = "h4"
        tag_map[req_tag] = self.getDataByTag(parsedSite, req_tag)
        req_tag = "h5"
        tag_map[req_tag] = self.getDataByTag(parsedSite, req_tag)
        req_tag = "h6"
        tag_map[req_tag] = self.getDataByTag(parsedSite, req_tag)

        return tag_map
    def getDataByTag(self, parsedSite, tag):
        try:
            ret = []
            for ti in parsedSite.find_all("h1"):
                ret.append(ti.text.strip())
            return ret
        except Exception as e:
            print(e)
        return []
    def getTitle(self, parsedSite):
        return {
            "title":self.getDataByTag(parsedSite, "title")
        }
    def getInfoFromUrl(self):
        ret = {}
        for url in self.sites:
            temp = []
            for str in url.split("/"):
                if str.find("http")==-1 and str.find("www.")==-1 and len(str)>1:
                    ret_str = ""
                    for ch in str:
                        if ch.isalnum()==False:
                            ret_str+=" "
                        else:
                            ret_str+=ch

                    temp.append(ret_str)
            ret[url] = temp
        return ret
    def getAllP(self, parsedSite):
        return {
            "p":self.getDataByTag(parsedSite, "p")
        }   
    def isAWebssite(self, url, arr):
        if requests.get(url).status_code==200:
            arr.append(url)
            return True
        return False
    def allTagValue(self, parsedText):
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head', 
            'input',
            'script',
        ]
        text = parsedText.find_all(string=True)
        tagValue = {}
        for t in text:
            if t.parent.name =='p' and t.parent.name not in blacklist:
                if 'p' in tagValue:
                    temp = tagValue['p']
                    temp.append(str(t)) 
                    tagValue['p'] = temp
                else:
                    tagValue['p'] = [t]
            elif t.parent.name=='title' and t.parent.name not in blacklist:
                if 'title' in tagValue:
                    temp = tagValue['title']
                    temp.append(str(t)) 
                    tagValue['title'] = temp
                else:
                    tagValue['title'] = [t]
            elif t.parent.name=='h1' and t.parent.name not in blacklist:
                if 'h1' in tagValue:
                    temp = tagValue['h1']
                    temp.append(str(t)) 
                    tagValue['h1'] = temp
                else:
                    tagValue['h1'] = [t]
            elif t.parent.name=='h2' and t.parent.name not in blacklist:
                if 'h2' in tagValue:
                    temp = tagValue['h2']
                    temp.append(str(t)) 
                    tagValue['h2'] = temp
                else:
                    tagValue['h2'] = [t]
            elif t.parent.name=='h3' and t.parent.name not in blacklist:
                if 'h3' in tagValue:
                    temp = tagValue['h3']
                    temp.append(str(t)) 
                    tagValue['h3'] = temp
                else:
                    tagValue['h3'] = [t]
            elif t.parent.name=='h4' and t.parent.name not in blacklist:
                if 'h4' in tagValue:
                    temp = tagValue['h4']
                    temp.append(str(t)) 
                    tagValue['h4'] = temp
                else:
                    tagValue['h4'] = [t]
            elif t.parent.name=='h5' and t.parent.name not in blacklist:
                if 'h5' in tagValue:
                    temp = tagValue['h5']
                    temp.append(str(t)) 
                    tagValue['h5'] = temp
                else:
                    tagValue['h5'] = [t]
            elif t.parent.name=='h6' and t.parent.name not in blacklist:
                if 'h6' in tagValue:
                    temp = tagValue['h6']
                    temp.append(str(t)) 
                    tagValue['h6'] = temp
                else:
                    tagValue['h6'] = [t]
        return tagValue

