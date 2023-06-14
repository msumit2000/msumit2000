from udops.src.dep.Manager.UserLogManager import *


class Userlog:
    def login(self,token,user_name):
        Userlog = User_log()
        return Userlog.login(token,user_name)

    def logout(self):
        Userlog = User_log()
        return Userlog.logout()

##********************************************************************
##    USER MANAGEMENT

    def get_user_list(self):
        userlog = User_log()
        return userlog.get_user_list(user)

    def update_user(self, first_name, last_name, email, user_name):
        userlog = User_log()
        return userlog.get_user_list(self, first_name, last_name, email, user_name)

    def get_team_list(self):
        userlog  = User_log()
        return userlog.get_team_list()

    def update_team(self, permanent_access_token, tenant_id, admin_user_id, s3_base_path, team_name):
        userlog = User_log()
        return userlog.update_team(self, permanent_access_token, tenant_id, admin_user_id, s3_base_path, team_name)

    def add_user_to_team(self,user_name,team_id):
        userlog = User_log()
        return userlog.add_user_to_team(user_name,team_id)