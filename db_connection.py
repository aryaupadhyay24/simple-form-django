from pymongo import MongoClient
client=MongoClient("mongodb+srv://aryaofficial032:1234567aA@cluster0.2ob3vzl.mongodb.net/")


# client is reference of mongo atlas
# now I have to create datatbaase
db=client.form_database