import pymongo,crawl_webpage
arr = []
client = pymongo.MongoClient("<--host-->", "<--port number-->")
coll = client["search"]["key_words"]
sitesList = ['<---URLS---->']
c = crawl_webpage.crawlSites(sitesList)
for site in c.sites:
    val = c.allTagValue(c.urlToParser(site))
    val["url"] = site
    client["search"]["s_data"].insert_one(val).inserted_id
    keys = list(val.keys())[:-1]

    for key in keys:
        for words in val.get(key):
            temp_str = ""
            redSet = set()
            for word in words:
                if word.isalnum()==False and word!=" ":
                    continue
                elif word==" ":
                    if len(temp_str)>=1 and temp_str[len(temp_str)-1]!=" ":
                        temp_str+=word
                else:
                    temp_str+=word.lower()
            if len(temp_str)>=1:
                
                for dat in temp_str.split():
                    redSet.add(dat)
            
            for s in redSet:
                if coll.find_one({"key":s})==None:
                    coll.insert_one({
                        "key":s,
                        "id":[
                            val["_id"]
                        ]
                        })
                else:
                   
                    coll.update_one(
                        {
                            "key":s
                        },
                        {
                            "$push":{"id":val["_id"]}
                        }
                    )
