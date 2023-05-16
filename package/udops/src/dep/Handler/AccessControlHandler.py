from udops.src.dep.Manager.AuthenticationControlManager import udpos_authentication
from udops.src.dep.Manager.AuthoriseControlmanager import udops_authorise
from udops.src.dep.config.Connection import *
from udops.src.dep.InputProperties import *
prop=properties()
connection = Connection()
conn = connection.get_connection()

class UserAuthenticationHandler:
    def user_management(self,source_dir):
        authentication = udpos_authentication()
        username = authentication.authenticate_user(source_dir)

        if username == 1:
            return ("invalid user")
        else:
            print("Authentication is successful!!!!")
            authorise = udops_authorise()
            return authorise.authorise_access_to_corpus(username,conn)
