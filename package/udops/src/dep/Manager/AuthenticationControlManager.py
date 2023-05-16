import requests
import configparser

from psycopg2.extras import RealDictCursor

class udpos_authentication:
    def authenticate_user(self,source_dir,conn):
        config = configparser.ConfigParser()
        #config.read('/home/user/Desktop/.udops_config')
        config.read(source_dir)

        ACCESS_TOKEN = config.get('SECTION_NAME', 'ACCESS_TOKEN_KEY_NAME')
        url = 'https://api.github.com/user'
        headers = {'Authorization': f'token {ACCESS_TOKEN}'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            username = response.json()['login']
            print(username)
           # return username

            cursor = conn.cursor(cursor_factory=RealDictCursor)
            query = f"select access from git_access where username = '{username}';"
            cursor.execute(query)
            

        else:
            return 1
