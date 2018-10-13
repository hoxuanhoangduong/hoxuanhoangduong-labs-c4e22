from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db['posts']
customers = db['customers']

post = {
    'title':'Hongkong1',
    'author':'Hoàng Dương',
    'content':'Và giờ anh biết chuyện tình mình chẳng còn gì. Khi nắng xuân sang lời mật ngọt còn thầm thì. Em bước sang ngang đợi chờ một điều diệu kì. Như lúc ban đầu.'
}

posts.insert_one(post)
