from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from blaster import blasterFunc
from flask_cors import CORS


#importing functions for adding new users..scraping new users... scraping posts... and updating the DB with them
from Folder.parentFunctions.AddNewUsers.bulkWrite import addNewUsers
from Folder.parentFunctions.AddNewUsers.addUserPosts import newUsers_addUserPosts


#importing functions for updating
from Folder.parentFunctions.Updates.UpdateDBSingleUser import updateSingleUser
from Folder.parentFunctions.Updates.UpdateDBUserPosts import updateUserPosts
from Folder.parentFunctions.Updates.UpdateDBUsers import updateUsers




#initializing app, api, and cors
app = Flask(__name__)
api = Api(app)
cors = CORS(app, origins={"origins": "*"})

#setting reqparser
scrape_post_args = reqparse.RequestParser()
scrape_post_args.add_argument("sec_uid", action='append', help="Please send an array sec_uids to update...")

#definiing endpoints and actions
class Home(Resource):
    def get(self):
        return "Hello World"


#defining update function endpoints

class updateSingleUser(Resource):
    def post(self):
        args = scrape_post_args.parse_args()
        updateSingleUser(args.sec_uid)
        return "Success"
    def get(self):
        return "Nothing to GET"

class updateAllUsers(Resource):
    def post(self):
        updateUsers()
        return  "Success"
    def get(self):
        return "Nothing to GET"

class updateAllUserPosts(Resrouce):
    def post(self):
        updateUserPosts()
        return "Success"
    def get(self):
        return "Nothing to GET"


#defining addUser function endpoints
class oldDB_AddUser(Resource):
    def post(self):
        addNewUsers()
        newUsers_addUserPosts()
        return "Success"
        


#adding resrouces for updating endpoints
api.add_resource(updateSingleUser, "/updateSingleUser")
api.add_resource(updateAllUsers, "/updateAllUsers")
api.add_resource(updateAllUserPosts, "/updateAllUserPosts")

#adding resrouces for adding from oldDB endpoints
api.add_resource(oldDB_AddUser, "/oldDB_AddUser")

#Home
api.add_resource(Home, "/")

if __name__ == "__main__":
   app.run()
