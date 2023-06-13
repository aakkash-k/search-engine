import json
import requests
class collectData:
    def __init__(self, fileUrl):
        #parsing the 
        self.fileUrl = fileUrl
    #function which returns the file in json format 
    def fileToJson(self):

        sites_data = open(self.fileUrl, "r")
        strBud = ""
        for i in sites_data:
            strBud+=i
        loadedFile = json.loads(strBud)
        return loadedFile
    #returns the allowed sites to crawl
    def getAllowedSites(self):
        retSites = {}
        for site in self.fileToJson()["sites"]:
            req = requests.get(site).text
            tempHol = []
            for line in req.split("\n"):
                tempData = line.lower()
                if tempData.find("sitemap")>=0 or (tempData.find("allow")>=0 and tempData.find("disallow")==-1) and self.notAnComment(tempData):
                    tempHol.append(self.formatToUrl(line))
            retSites[site] = tempHol
        return retSites
    #remove errors and format the correct url
    def formatToUrl(self, inStr):
        retStr = ""
        flag = False
        for ch in inStr:
            #removing all special characters to format the string so that it can be parsed
            if ch==':':
                flag = True
                continue
            if ch=='\r' and len(retStr)!=0:
                break
            if flag and ch!=' ':
                retStr+=ch
        return retStr
    #to differentiate between a url and an comment in the robots.txt file
    def notAnComment(self, inStr):
        ret = ""
        #Iterating through the string
        for i in  inStr:
            #If a string has '#' symbol in the begining then it's an comment
            if i=='#' and len(ret)==0:
                return False
            elif i!=' ':
                ret+=i
        return True


