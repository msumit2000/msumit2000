from udops.src.dep.Handler.UserManagementHandler import *



class UserManagement:
    def get_user_list(self):
        Userlog = UserManagementHandler()
        return Userlog.get_user_list()
    
    def update_user(self,firstname,lastname, email, existing_user_name, new_user_name):
        user = UserManagementHandler()
        if user.update_user(firstname,lastname, email, existing_user_name, new_user_name)==1:
            return 1
        else:
            return 2    

    def get_team_list(self):
        user = UserManagementHandler()
        return user.get_team_list()

    def update_team(self, permanent_access_token, tenant_id, admin_user_id, s3_base_path, existing_teamname,new_teamname):
        user = UserManagementHandler()
        if user.update_team(permanent_access_token, tenant_id, admin_user_id, s3_base_path, existing_teamname,new_teamname)==1:
            return 1
        else:
            return 2  

        
    def add_user(self,user_name, teamname):
        user = UserManagementHandler()
        return user.add_user(user_name, teamname)

    def delete_user(self,corpus_name, teamname):
        user = UserManagementHandler()
        return user.delete_user(corpus_name, teamname)
    
    def grant_access_corpus(self,user_name,corpus_name,permission):
        user = UserManagementHandler()
        return user.grant_access_corpus(user_name,corpus_name,permission)
    
    def remove_access_corpus(self,user_name,corpus_name,permission):
        user = UserManagementHandler()
        return user.remove_access_corpus(user_name,corpus_name,permission)    

    def access_corpus_list_write(self, corpus_name):
        user = UserManagementHandler()
        return user.access_corpus_list_write(corpus_name)
        
    
    def access_corpus_list_read(self,corpus_name):
        user = UserManagementHandler()
        return user.access_corpus_list_read(corpus_name)
