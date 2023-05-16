from udops.src.dep.Handler.AccessControlHandler import UserAuthenticationHandler
class AccessControl:
    def User_Management(self,source_dir):
        user = UserAuthenticationHandler()
        return user.user_management(source_dir)
