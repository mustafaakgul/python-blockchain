import hashlib, json


# http://shakespeare.mit.edu/hamlet/full.html
for nonce in range(0, 10000000):  #for nonce in range(0, 11):
    # Genesis Block
    myjson = {
              "who": "BERNARDO",
              "text": "Long live the king!",
              "nonce": nonce,
              "previoushash": "949c74700ad241b65d8354ab2aae2ef3fef0e07c90a6262330c8f373acbb0001"
            }
    myjson = json.dumps(myjson) #Converting json to string
    #myhash = hashlib.sha256(myjson.encode()).hexdigest()
    myhash = hashlib.sha256(myjson.encode()).hexdigest()
    if myhash[-4:] == "0001":   # Son 3 hanesi 0001 olanı kazmak
        print(myjson)   # Hangisini buldu
        print(myhash)   # Hangi hash degeri var bulunan icin
        break
    else:
        # print("Nonce Value", nonce)
        # print("Hash Value",  myhash)
        # print("Hash [-2:] Value", myhash[-2:])
        continue

# First Block
# First JSON myjson = {
#               "who": "BERNARDO",
#               "text": "Who's there?",
#               "nonce": nonce,
#               "previoushash": "000000000000000000000000000000000000000000000000000000000000000"
#             }
# First Data Found : {"who": "BERNARDO", "text": "Who's there?", "nonce": 101669, "previoushash": "000000000000000000000000000000000000000000000000000000000000000"}
# First Hash 77c4963da65a0021bc5350ada545c97d2be517f94a33f845a405899859ac0001

# Second Block
# Second JSON myjson = {
#               "who": "FRANCISCO",
#               "text": "Nay, answer me: stand, and unfold yourself.",
#               "nonce": nonce,
#               "previoushash": "77c4963da65a0021bc5350ada545c97d2be517f94a33f845a405899859ac0001"
#             }
# Seconda Data Found {"who": "FRANCISCO", "text": "Nay, answer me: stand, and unfold yourself.", "nonce": 11989, "previoushash": "77c4963da65a0021bc5350ada545c97d2be517f94a33f845a405899859ac0001"}
# Second Hash 949c74700ad241b65d8354ab2aae2ef3fef0e07c90a6262330c8f373acbb0001

# Third Block
# Third JSON myjson = {
#               "who": "BERNARDO",
#               "text": "Long live the king!",
#               "nonce": nonce,
#               "previoushash": "949c74700ad241b65d8354ab2aae2ef3fef0e07c90a6262330c8f373acbb0001"
#             }
# Third Data Found : {"who": "BERNARDO", "text": "Long live the king!", "nonce": 7564, "previoushash": "949c74700ad241b65d8354ab2aae2ef3fef0e07c90a6262330c8f373acbb0001"}
# Third Hash e7a01893e42d5bff52811c73745743348d79944faae050af774ccaeaa4510001

# Boyle boyle bulacak devam etcek  birbirlerine oncekinin hash degerini yaparak her buldugu bir mining yapmıs olması bir para dusurmus olması
# Butun blocklar birbirine baglı o yuzden hic bir degisiklik yapamıyoruz ilk 3 diyalogunu 3 block yaptık yapılanlar veritabanına yazılması gerekiyor bunları daha yapmadık