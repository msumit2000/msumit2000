import os.path

from psycopg2.extras import RealDictCursor
import requests
from udops.src.dep.config.Connection import *
from udops.src.dep.InputProperties import *
prop=properties()
connection = Connection()
conn = connection.get_connection()
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path,'udops_config')
class User_log:
    def login(self,access_token,username):
        try:
            url = 'https://api.github.com/user'
            headers = {'Authorization': f'token {access_token}'}
            response = requests.get(url, headers=headers)
            print(access_token)

            if response.status_code == 200:
                github_username = response.json()['login']
                cursor = conn.cursor(cursor_factory=RealDictCursor)
                query = f"select user_name from cfg_udops_acl where user_name = '{username}';"
                cursor.execute(query)
                rows = cursor.fetchone()
                database_username = rows['user_name']
                conn.commit()

                if username != github_username:
                    print('Wrong username')
                elif github_username != database_username:
                    print('Username Doesnt exist in Udops')
                else:
                    file_path = 'src/dep/config/.udops_config'
                    current_directory = os.getcwd()
                    print(current_directory)
                    directory = os.path.join(current_directory, file_path)
                    print(directory)
                    config = configparser.ConfigParser()
                    config.read(directory)

                    if 'github' not in config:
                        config.add_section('github')
                    config.set('github', 'ACCESS_TOKEN', access_token)
                    with open(directory, 'w') as config_file:
                        config.write(config_file)
                    print("login Successfully !!!")

            else:
                return print(response.status_code)
        except Exception as e:
            print(e)

    def logout(self):
        data_to_erase = 'github'
        with open("/home/user/udops/package/udops/src/dep/config/udops_config", 'r') as file:
            lines = file.readlines()

        modified_lines = [line for line in lines if data_to_erase not in line]

        with open("/home/user/udops/package/udops/src/dep/config/udops_config", 'w') as file:
            file.writelines(modified_lines)
            print()


##***************************************************************************************
##  USER MANAGEMENT
    def get_user_list(self):
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT * FROM cfg_udops_users")
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
            return rows
        except Exception as e:
            print(e)

    def update_user(self, first_name, last_name, email, user_name):
        try:
            conn = connection.get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            query = f"UPDATE cfg_udops_users SET first_name = '{first_name}', last_name = '{last_name}', email = '{email}' where user_name ='{user_name}';"
            cursor.execute(query)
            conn.commit()
            cursor.close()
            return 1
        except Exception as e:
            raise e

    def get_team_list(self):
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("select * from cfg_udops_teams_metadata")
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
            return rows
        except Exception as e:
            print(e)

    def update_team(self, permanent_access_token, tenant_id, admin_user_id, s3_base_path, team_name):
        try:
            conn = connection.get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            query = f"UPDATE cfg_udops_teams_metadata SET permanent_access_token = '{permanent_access_token}', tenant_id = '{tenant_id}', admin_user_id = '{admin_user_id}', s3_base_path = '{s3_base_path}' where team_name ='{team_name}';"
            cursor.execute(query)
            conn.commit()
            cursor.close()
            return 1
        except Exception as e:
            raise e

    def add_user_to_team(self, user_name, team_id):
        try:
            conn = connection.get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            query = f"INSERT into cfg_udops_users(user_name, team_id) values ('{user_name}', '{team_id}')"
            cursor.execute(query)
            conn.commit()
            cursor.close()
            return 1
        except Exception as e:
            raise e





