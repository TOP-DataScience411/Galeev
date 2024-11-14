errors = []

while True:
    err = input('Введите код и название ошибки: ')
    if err == '':
        break
    err = err.split()    
    errors.append(err)
    
errors = dict(errors)
err = input('Введите название ошибки: ') 

found = False

for code, name in errors.items():
    if err == name:
        print(code)
        found = True
        
if not found:
    print('! value error !') 

# Введите код и название ошибки: 1004 ER_CANT_CREATE_FILE
# Введите код и название ошибки: 1005 ER_CANT_CREATE_TABLE
# Введите код и название ошибки: 1006 ER_CANT_CREATE_DB
# Введите код и название ошибки: 1007 ER_DB_CREATE_EXISTS
# Введите код и название ошибки: 1008 ER_DB_DROP_EXISTS
# Введите код и название ошибки: 1010 ER_DB_DROP_RMDIR
# Введите код и название ошибки: 1016 ER_CANT_OPEN_FILE
# Введите код и название ошибки: 1022 ER_DUP_KEY
# Введите код и название ошибки:
# Введите название ошибки: ER_CANT_CREATE_DB
# 1006   

# Введите код и название ошибки: 4107     ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# Введите код и название ошибки: 4108 ER_GIPK_COLUMN_EXISTS
# Введите код и название ошибки: 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
# Введите код и название ошибки: 4113 ER_DA_EXPIRE_LOGS_DAYS_IGNORED
# Введите код и название ошибки: 4114 ER_CTE_RECURSIVE_NOT_UNION
# Введите код и название ошибки:
# Введите название ошибки: ER_CANT_OPEN_FILE
# ! value error !