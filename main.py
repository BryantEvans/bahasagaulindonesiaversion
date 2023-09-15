meme_dict = {
    "mager": "Ketika anda malas gerak"
    "kepo": "Pengen tau aja"
    "gercep": "gerak cepat"
    "jamber": "jam berapa"
    "santuy": "santai"
    "ygy": "ya guys ya"
    "gaje": "ga jelas"
    "tbl": "takut banget lho"
}

for i in range(5):
    word = input("Ketik kata yang tidak kau mengerti: ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("kata gaul tersebut tidak ada di kamus")
