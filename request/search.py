from pymongo import MongoClient
import math
def listObj(keys, ind, s):
    if ind>=len(keys):
        return []
    else:
        lis = []
       
        for k in keys:
            for obj in client()["search"]["key_words"].find({"key":k}):
                li = set(obj["id"])
                for i in li:
                    for j in client()["search"]["s_data"].find({"_id":i}):
                        lis.append(j)

        return lis
def retAllRes(keys):
    key = keys["keys"]
    ret = listObj(key, 0, set())
    allSumCoor = {}
    for v in ret:
        txt = ""
        for i in v.keys():
            if i!="_id" and i!="url":
                for j in v[i]:

                    txt+=j+" "
        coor = getCordinates(toGraph(txt, set(key)))
        sumCoor = 0
        for co in range(len(coor)-1) :
            sumCoor+=math.sqrt( ((coor[co][0]-coor[co+1][0])**2)+((coor[co][1]-coor[co+1][1])**2) )
        allSumCoor[sumCoor] = v
    retRes = []
    for i in sorted(list(allSumCoor.keys()), reverse=True):
        tem = allSumCoor[i]
        del tem["_id"]
        retRes.append(tem)
    

    return retRes
def getCordinates(g):
    coor = []
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j]==1:
                coor.append([i, j])
    return coor
def toGraph(txt, k):
    retStr = ""
    countSp = 0
    for tx in txt:
        if tx.isalnum():
            retStr+=tx.lower()
        elif tx==' ':
            if len(retStr)>0:
                if retStr[len(retStr)-1]!=' ':
                    countSp+=1
                    retStr+=tx
    g = []
    inarr = []
    for sp in retStr.split():
        if sp in k:
            inarr.append(1)
        else:
            inarr.append(0)
        if len(inarr)==countSp//2:
            g.append(inarr)
            inarr = []
    return g


def client():
    return MongoClient("localhost", 27017)


