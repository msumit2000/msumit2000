from psycopg2.extras import RealDictCursor
import json
import requests
from udops.src.dep.config.Connection import *
from udops.src.dep.InputProperties import *
from django.db import IntegrityError
prop=properties()
connection = Connection()
conn = connection.get_connection()

class UserManagementManager:
    ########################### User Management #######################

    def get_user_list(self, conn):
        try:
            
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT user_name,firstname,lastname,email FROM udops_users")
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
          #  conn.close()
            return rows
        except Exception as e:
            print(e)

    def update_user(self,firstname,lastname, email, existing_user_name, new_user_name):
        try:
            conn = connection.get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            query = f"UPDATE udops_users SET firstname = '{firstname}', lastname = '{lastname}', email = '{email}', user_name='{new_user_name}' where user_name ='{existing_user_name}';"

            cursor.execute(query)
            if cursor.rowcount == 0:
                return 2
            else :
                conn.commit()
                cursor.close()
                return 1
        except Exception as e:
            raise e  
    
    
      

    def get_team_list(self, conn):
        try:
            conn = connection.get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            # query = f"SELECT teamname, permanent_access_token, tenant_id, admin_user_id, s3_base_path FROM cfg_udops_teams_metadata;"
            query = f"""SELECT t.teamname,t.permanent_access_token,t.tenant_id,t.admin_user_id,t.s3_base_path, ARRAY(SELECT user_name FROM cfg_udops_users WHERE team_id = t.team_id) AS users FROM cfg_udops_teams_metadata AS t;"""
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
          #  conn.close()
            return rows
        except Exception as e:
            print(e)

    def update_team(self, permanent_access_token, tenant_id, admin_user_id, s3_base_path, existing_teamname,new_teamname):
        try:
            conn = connection.get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            query = f"UPDATE cfg_udops_teams_metadata SET permanent_access_token = '{permanent_access_token}', tenant_id = '{tenant_id}', admin_user_id = '{admin_user_id}', s3_base_path = '{s3_base_path}', teamname = '{new_teamname}'  where teamname ='{existing_teamname}';"

            cursor.execute(query)
            if cursor.rowcount == 0:
                return 2
            else :
                conn.commit()
                cursor.close()
                return 1
        except Exception as e:
            raise e   
        
    def add_user(self, user_name, teamname):
        try:
            conn = connection.get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            # query = f"INSERT into cfg_udops_users(user_name, team_id) values ('{user_name}', '{team_id}')"
            # query = f"INSERT INTO cfg_udops_users (user_name, team_id) VALUES ('{user_name}', (SELECT team_id FROM cfg_udops_teams_metadata WHERE teamname = '{teamname}'))"
            # query = f"INSERT INTO cfg_udops_users (user_name, team_id, tenant_id) SELECT '{user_name}', team_id, tenant_id FROM cfg_udops_teams_metadata WHERE teamname = '{teamname}'"
            query = f"INSERT INTO cfg_udops_users (user_name, team_id, tenant_id) SELECT '{user_name}', team_id, tenant_id FROM cfg_udops_teams_metadata WHERE teamname = '{teamname}' RETURNING user_id"

            cursor.execute(query)
            if cursor.rowcount == 0:
                return 2
            else :
                conn.commit()
                cursor.close()
                return 1
        except Exception as e:
            raise e  
        
    def delete_user(self, user_name, teamname):
        try:
            conn = connection.get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            query = f"DELETE FROM cfg_udops_users WHERE user_name = '{user_name}' AND team_id = (SELECT team_id FROM cfg_udops_teams_metadata WHERE teamname = '{teamname}')"

            cursor.execute(query)
            if cursor.rowcount == 0:
                return 2
            else :
                conn.commit()
                cursor.close()
                return 1
        except Exception as e:
            raise e

    def grant_access_corpus(self,user_name,corpus_name,permission):
        try:
            conn = connection.get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            # query = f"UPDATE cfg_udops_acl SET permission = '{permission}' WHERE user_name = '{user_name}' AND corpus_id = (SELECT corpus_id FROM corpus_metadata WHERE corpus_name = '{corpus_name}')"
            user_names_str = ", ".join([f"'{name}'" for name in user_name])

    # Construct the SQL query using f-strings
            query = f"""
            UPDATE cfg_udops_acl
            SET permission = '{permission}'
            WHERE corpus_id = (
                SELECT corpus_id
                FROM corpus_metadata
                WHERE corpus_name = '{corpus_name}'
            )
            AND user_name IN ({user_names_str});
            """
            cursor.execute(query)
            if cursor.rowcount == 0:
                return 2
            else :
                conn.commit()
                cursor.close()
                return 1
        except Exception as e:
            raise e      
        

    def remove_access_corpus(self,user_name,corpus_name,permission):
        try:
            conn = connection.get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            # query = f"DELETE FROM cfg_udops_acl WHERE permission = '{permission}', user_name = '{user_name}' AND corpus_id = (SELECT corpus_id FROM corpus_metadata WHERE corpus_name = '{corpus_name}')"
            user_names_str = ", ".join([f"'{name}'" for name in user_name])

    # Construct the SQL query using f-strings
            query = f"""
            DELETE FROM cfg_udops_acl
                WHERE permission = '{permission}'AND corpus_id = (
                SELECT corpus_id
                FROM corpus_metadata
                WHERE corpus_name = '{corpus_name}'
            )
            AND user_name IN ({user_names_str});
            """
            cursor.execute(query)
            if cursor.rowcount == 0:
                return 2
            else :
                conn.commit()
                cursor.close()
                return 1
        except Exception as e:
            raise e         

    def access_corpus_list_write(self, conn,corpus_name):
        try:
            
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            query = f'''SELECT user_name
                        FROM cfg_udops_acl
                        WHERE corpus_id IN (
                            SELECT corpus_id
                            FROM corpus_metadata
                            WHERE corpus_name = '{corpus_name}'
                        )
                        AND permission = 'write';
                    '''
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
          #  conn.close()
            return rows
        except Exception as e:
            print(e)

         
    def access_corpus_list_read(self, conn,corpus_name):
        try:
            
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            query = f'''SELECT user_name
                        FROM cfg_udops_acl
                        WHERE corpus_id IN (
                            SELECT corpus_id
                            FROM corpus_metadata
                            WHERE corpus_name = '{corpus_name}'
                        )
                        AND permission = 'read';
                    '''
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
          #  conn.close()
            return rows
        except Exception as e:
            print(e)     
