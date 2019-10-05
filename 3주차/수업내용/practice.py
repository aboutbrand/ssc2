from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 특정 결과값을 뽑아보기

target_movie = db.movies_practice.find_one({'title': '사운드 오브 뮤직'})
target_star = target_movie['star']

# print(target_star)

sameStar = list(db.movies_practice.find({'star':target_star}))

# print(sameStar)

# for sameStars in sameStar:
#     print(sameStars['title'])
#     print(sameStars['rank'])

starDelete = db.movies_practice.update_many({'star': target_star}, {'$set' : {'star': 0}})