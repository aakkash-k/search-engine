from flask import Flask,request
from pymongo import MongoClient
import random, keywords_generator
import search,json
app = Flask(__name__)

def client():
    return MongoClient("<--host-->", "<--port-->")

@app.route('/previous_user', methods=['GET'])
def previous_user():
    uid = request.args.get("uid")
    res = client()["search"]["userId"].find({"uid":uid})
    if res!=None:
        d = {}
        for i in res:
            d = i
            del d["_id"]
        return d
    else:
        return {
            "result":"No result found!!!"
        }
    return request.args.get("uid")

@app.route('/search', methods=['GET'])
def getRes():
    if request.args.get("q")==None and request.args.get("location")==None:
        return {"result":"enter words to search"}
    elif request.args.get("q")!=None and request.args.get("location")!=None:
        uid = uniqueId()
        cli = client()["search"]["userId"]
        while cli.find({"uid":uid})==None:
            uid = uniqueId()
        
        retVal = []
        for k in request.args.get('q').split():
            tem = getAllPossibleKeys(k.lower())
            if len(tem)==0:
                retVal.append(k)
            else:
                retVal.extend(list(set(tem)))
        if request.args.get("location")!=None:
            retVal.append(request.args.get("location").lower())
        result = {
            "result":search.retAllRes({
                "keys":retVal,
                "q":request.args.get('q')
            }),
            "userid":uid
        }
        client()["search"]["userId"].insert_one({
            "uid":uid,
            "key":request.args.get("q"),
            "result":result
        })
        return result
    elif request.args.get("q")!=None:
        uid = uniqueId()
        cli = client()["search"]["userId"]
        while cli.find({"uid":uid})==None:
            uid = uniqueId()
        
        retVal = []
        for k in request.args.get('q').split():
            tem = getAllPossibleKeys(k.lower())
            if len(tem)==0:
                retVal.append(k)
            else:
                retVal.extend(list(set(tem)))
        result = {
            "result":search.retAllRes({
                "keys":retVal,
                "q":request.args.get('q')
            }),
            "userid":uid
        }
        client()["search"]["userId"].insert_one({
            "uid":uid,
            "key":request.args.get("q"),
            "result":result
        })
        return result
    elif request.args.get("location")!=None:
        uid = uniqueId()
        cli = client()["search"]["userId"]
        while cli.find({"uid":uid})==None:
            uid = uniqueId()
        retVal = []
        for i in request.args.get("location").split():
            retVal.append(i.lower())
        result = {
            "result":search.retAllRes({
                "keys":retVal,
                "q":request.args.get('location')
            }),
            "userid":uid
        }
        client()["search"]["userId"].insert_one({
            "uid":uid,
            "key":request.args.get("location"),
            "result":result
        })
        return result
    return "no result"  
    
def getAllPossibleKeys(key):
    ret = []
    cStr = ""
    for k in key:
        if k.isalnum():
            cStr+=k
    for sp in cStr.split():
        if keywords_generator.isPreposition(sp)==False:
            ret.extend(keywords_generator.generateAllKey(key))
    return ret

def uniqueId():
    alpha = ""
    for f in range(0,4):
        alpha+=chr(ord('a')+random.randint(0, 25))
    for s in range(0,3):
        alpha+=str(random.randint(0,9) )
    for f in range(0,2):
        alpha+=chr(ord('a')+random.randint(0, 25))
    alpha+=str(random.randint(0,9))
    return alpha


if __name__ == '__main__':
   
    app.run()

