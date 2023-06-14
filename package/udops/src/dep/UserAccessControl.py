from udops.src.dep.Handler.AccessControlHandler import UserAuthenticationHandler
from udops.src.dep.Handler.UserLogHandler import User_log
class AccessControl:
    def authenticate(self,ACCESS_TOKEN):
        user = UserAuthenticationHandler()
        return user.authenticate_user(ACCESS_TOKEN)

    def get_user_team(self,user_id):
        user = UserAuthenticationHandler()
        if user.get_user_team(user_id)==0:
            return 0
        else:
            return user.get_user_team(user_id)

    def authorize_user(self,user_id,corpus_id,access_type):
        user = UserAuthenticationHandler()
        if user.authorize_user(user_id,corpus_id,access_type)==1:
            return 1
        else:
            return 2

    def login(self,token,username):
        Userlog = User_log()
        return Userlog.login(token,username)

    def logout(self):
        Userlog = User_log()
        return Userlog.logout()
##*********************************************************************************
## USER MANAGEMENT

    def get_user_list(self):
        userlog = User_log()
        return userlog.get_user_list()

    def update_user(self, first_name, last_name, email, user_name):
        userlog = User_log()
        return userlog.get_user_list(self, first_name, last_name, email, user_name)

    def get_team_list(self):
        userlog = User_log()
        return userlog.get_team_list()

    def update_team(self, permanent_access_token, tenant_id, admin_user_id, s3_base_path, team_name):
        userlog = User_log()
        return userlog.update_team(self, permanent_access_token, tenant_id, admin_user_id, s3_base_path, team_name)

    def add_user_to_team(self, user_name, team_id):
        userlog = User_log()
        return userlog.add_user_to_team(user_name, team_id)

    def corpus_id(self,corpus_name):
        user = UserAuthenticationHandler()
        return user.corpus_id(corpus_name)

    def user_name(self,corpus_id):
        user = UserAuthenticationHandler()
        return user.user_name(corpus_id)

    def default_access(self,corpus_id,user_id):
        user = UserAuthenticationHandler()
        return user.default_acess(corpus_id,user_id)





