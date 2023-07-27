import hashlib, json

text = "a"
#https://xorbin.com/tools/sha256-hash-calculator COMPARE
myhash = hashlib.sha256(text.encode()).hexdigest()
#TypeError: Unicode-objects must be encoded before hashing myhash = hashlib.sha256("as").hexdigest()
# #hexdigest hex olarak cıktı olmamızı saglar
print(myhash)

#for ile nonce degerine göre özet degerini cıkartmak
for nonce in range(0, 11):
    myjson = {"text": text, "nonce": nonce}
    myjson = json.dumps(myjson) #Converting json to string
    myhash = hashlib.sha256(myjson.encode()).hexdigest()
    print(nonce)
    print(myhash)
    print(myhash[-2:])


#for ile nonce uretiyoruz ilk satırda
for nonce in range(0, 100000):  #for nonce in range(0, 11):
    myjson = {"text": text, "nonce": nonce}
    myjson = json.dumps(myjson) #Converting json to string
    #myhash = hashlib.sha256(myjson.encode()).hexdigest()
    myhash = hashlib.sha256(myjson.encode()).hexdigest()
    if myhash[-2:] == "bc":   #Nonce degeri 99 iken buldu mining 99 tane yaptı  #sonu bc ile biten özetini bulmaya calısmak demek mining yapmak demek bu kendi kıralımız
        print(myjson)
        print(myhash)
        break
    else:
        # print("Nonce Value", nonce)
        # print("Hash Value",  myhash)
        # print("Hash [-2:] Value", myhash[-2:])
        continue

