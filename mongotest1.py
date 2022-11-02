import pymongo
client = pymongo.MongoClient("mongodb+srv://harshaa:harsha123@dellinspiron.kgnjiyr.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
"harsha" : "greesu",
"varsha:":"geetu",
"garsha":"gee"
}

d = {
"harsha" : "greesu",
"varsha:":"geetu",
"garsha":"gee"
}

d = {
"harsha" : "greesu",
"varsha:":"geetu",
"garsha":"gee"
}

d = {
"harsha" : "greesu",
"varsha:":"geetu",
"garsha":"gee"
}
db1 = client['mongotest1']
coll = db1['test']
coll.insert_one(d)

