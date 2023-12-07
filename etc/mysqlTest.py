import pymysql

connection = pymysql.connect(host='127.0.0.1', user='hmuser', password='hmuserdb', db='label_craft', charset='utf8mb4')
cursor = connection.cursor()
targetTables = ['moderator_project', 'moderator_task']
# targetTable = ['arbiter', 'dsat', 'ringer', 'stormbreaker', 'sven', 'wasp']

for table in targetTables:
    copyTable = table + '_copy'
    cursor.execute('DROP TABLE IF EXISTS %s' % copyTable)
    cursor.execute('CREATE TABLE %s LIKE %s' % (copyTable, table))
    cursor.execute('INSERT INTO %s (SELECT * FROM %s)' % (copyTable, table))

connection.commit()
connection.close()
