import psycopg2
from psycopg2.extras import RealDictCursor

# conn = psycopg2.connect(
#     host="localhost",
#     database="Uniphore",
#     user="postgres",
#     password="Sumit@123",
# )


class udops_authorise:
    def authorise_access_to_corpus(self,username,conn):
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        query = f"select access from git_access where username = '{username}';"
        cursor.execute(query)
        rows = cursor.fetchone()
        #print(rows[0])
        cursor.close()
        return rows
       # conn.close()

    def update_user_access(self, username, new_access_type):
        try:
            cursor = conn.cursor()
            query = f"UPDATE git_access SET access = '{new_access_type}' WHERE username = '{username}'"
            cursor.execute(query)
            conn.commit()
            print(f"Access type updated successfully for user '{username}'")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

# new_class = udops_authorise()
# new_class.authorise_access_to_corpus('user1')