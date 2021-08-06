from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

#importing function for gettin user from old db
from Folder.db.Finders.dbFindUserId import findUserId


#importing functions for adding new users..scraping new users... scraping posts... and updating the DB with them
from Folder.parentFunctions.AddNewUsers.bulkWrite import addNewUsers
from Folder.parentFunctions.AddNewUsers.addUserPosts import newUsers_addUserPosts
#for adding by usernames
from Folder.parentFunctions.AddNewUsers.newUser_addUserByName import addNewUsersByUName



#importing functions for updating
from Folder.parentFunctions.Updates.UpdateDBSingleUser import updateSelectUsers
from Folder.parentFunctions.Updates.UpdateDBUserPosts import updateUserPosts
from Folder.parentFunctions.Updates.UpdateDBUsers import updateUsers




#initializing app, api, and cors
app = Flask(__name__)
api = Api(app)
cors = CORS(app, origins={"origins": "*"})

#setting reqparser
scrape_post_args = reqparse.RequestParser()
scrape_post_args.add_argument("sec_uid", action='append', help="Please send an array sec_uids to update...")
scrape_post_args.add_argument("userNames", action='append', help="Please send an array of usernames to add to the DB...")


#definiing endpoints and actions
class Home(Resource):
    def get(self):
        return "Hello World"


#defining update function endpoints

class updateSingleUser(Resource):
    def post(self):
        args = scrape_post_args.parse_args()
        updateSelectUsers(args.sec_uid)
        return "Success"
    def get(self):
        return "Nothing to GET"

class updateAllUsers(Resource):
    def post(self):
        updateUsers()
        return  "Success"
    def get(self):
        return "Nothing to GET"

class updateAllUserPosts(Resource):
    def post(self):
        updateUserPosts()
        return "Success"
    def get(self):
        return "Nothing to GET"


#defining addUser function endpoints
class oldDB_AddUser(Resource):
    def post(self):
        user_ids = findUserId('influencer-database')
        users = addNewUsers(user_ids)
        newUsers_addUserPosts(users)
        return "Success"
        
class addNewUserByUserName(Resource):
    def post(self):
        args = scrape_post_args.parse_args()
        addNewUsersByUName(args.userNames)
        return "Success"





#adding resrouces for updating endpoints
api.add_resource(updateSingleUser, "/updateSelectUsers")
api.add_resource(updateAllUsers, "/updateAllUsers")
api.add_resource(updateAllUserPosts, "/updateAllUserPosts")





#adding resrouces for adding from oldDB endpoints
api.add_resource(oldDB_AddUser, "/oldDB_AddUser")
api.add_resource(addNewUserByUserName, "/addUserByUserName")


#Home
api.add_resource(Home, "/")

if __name__ == "__main__":
   app.run()