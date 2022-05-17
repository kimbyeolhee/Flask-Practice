import pymongo

MONGO_HOST = process.env.MONGODB_URI
MONGO_CONN = pymongo.MongoClient(MONGO_HOST)


def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster')
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        MONGO_CONN = pymongo.MongoClient(MONGO_HOST)
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    return blog_ab
