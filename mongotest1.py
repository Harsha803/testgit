import pymongo
client = pymongo.MongoClient("mongodb+srv://harshaa:harsha123@dellinspiron.kgnjiyr.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
"har":"var",
"mar":"gar",
"bar": "far"
}
db1 = client['mongotest1']
coll = db1['test']
coll.insert_one(d)

