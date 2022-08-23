#without import fields, you have to import every single field(StringField, EmailField...)
from mongoengine import Document, connect, fields
from bson.json_util import loads, dumps

#"mongoUserDB" is the name of DB
connect("mongoUserDB", host="127.0.0.1", port=27017)

#Users will be collection name in mongo db but in lower case.
class Users(Document):
    userID = fields.StringField(unique=True)
    password = fields.StringField(required=True, max_length=8)
    email = fields.EmailField(unique=True)
    firstname = fields.StringField()
    lastname = fields.StringField()

    
    #explain for class method https://builtin.com/software-engineering-perspectives/python-symbol
    @classmethod
    def collectInfo(cls, userID):
        #This will retrun an empty list if object does not exist
        print(Users.objects().filter(userID=userID))

        #Using get(),this will retrun error "DoesNotExist" if object does not exist.Can be used with try/except to check object status
        print(Users.objects(userID=userID).get())

        #You can get value of each key for each object
        for user in Users.objects(userID=userID):
            print(user.userID)

Users.collectInfo("a")

#create a new document in the collection
# Users(userID="a", password='a',email="a@a.com",firstname='a',lastname='a').save()
