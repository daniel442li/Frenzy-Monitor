import pymongo

myclient = pymongo.MongoClient("mongodb://daniel442li:KANQzahn5dF3VzZ@cluster0-shard-00-00-jq2na.mongodb.net:27017,cluster0-shard-00-01-jq2na.mongodb.net:27017,cluster0-shard-00-02-jq2na.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

print(myclient.list_database_names())

mydb = myclient["sudufrenzy"]


mycol = mydb["movieScratch"]

x = mycol.find_one()

print(x)

mydict = { "name": "Peter", "address": "Lowstreet 27" }
print(mydict)
x = mycol.insert_one(mydict)
print(x.inserted_id)