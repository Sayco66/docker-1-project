import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["animals_db"]
mycol = mydb["customers"]

mylist = [
  {
    id: 4,
    name: "Elephant",
    type: "wild",
  },
  {
    id: 5,
    name: "Horse",
    type: "domestic",
  },
  {
    id: 6,
    name: "Shark",
    type: "wild",
  },
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)