import json
def presentTenseToPast(key):
        if len(key)<=2:
            return key
        elif key[len(key)-1]=='e':
            return key+"ad"
        else:
            return key+"ed"
def presentTenseToContinuous(key):
    return key+"ing"
def continuousToPresent(key):
    if len(key)<=3:
        return key
    elif key[len(key)-3:]=="ing":
        return key[0:-3]
    return key
def pastTenseToPresent(key):
    if len(key)<=2:
        return key
    elif key[len(key)-2:]=="ed" or key[len(key)-2:]=="ad":
        return key[0:-2]
    return key


def isPreposition(key):
        txt = open("dictionary.txt", "r")
        ret = ""
        for i in txt:
            ret+=i
        words = json.loads(ret)
        ref_word = set()
        for s in words["preposition"]:
            tStr = ""
            for j in s:
                if j.isalpha():
                    tStr+=j
            ref_word.add(tStr)
        return key.lower() in ref_word
def generateAllKey(key):
    ret = []
    ret.append(presentTenseToContinuous(key))
    ret.append(presentTenseToPast(key))
    ret.append(pastTenseToPresent(key))
    ret.append(continuousToPresent(key))
    if len(key)>0:
        if key[len(key)-1]=='s':
            ret.append(key[:-1])
    return ret
# def allDiffusedWord(key, retWord, characters):
#     # T(n) = T(n-1)+T(n-1)+T(n-1)
#     if len(key)==0:
#         print(retWord)
#         return
#     else:
#         allDiffusedWord(key[1:], retWord+key[0], characters)
#         allDiffusedWord(key[1:], retWord, characters)

#         # for i in characters:
            
            
#         #     allDiffusedWord(key[1:], retWord+i, characters)
