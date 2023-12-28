from util_py import sql

# Try to create normal user account and return false if dupplicate
def create_account_user(username,password):
    
    sql_queue = f"SELECT create_user('{username}', '{password}', 0);"
    database="user_content" 
    
    result=sql.executeSQL_expectReturn_clean(sql_queue,database)
    return result

# Get user role and return false if information is wrong
def login(username,password):
    sql_queue = f"SELECT get_user_role('{username}', '{password}');"
    database="user_content" 
    
    result=sql.executeSQL_expectReturn_clean(sql_queue,database)
    return result
