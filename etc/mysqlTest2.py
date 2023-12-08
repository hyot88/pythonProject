import subprocess
import datetime

profile = 'local'

db_host = ''
db_port = ''
db_user = ''
db_password = ''
db_target = []
backup_path = ''

if profile == 'local':
    db_host = '127.0.0.1'
    db_port = '3306'
    db_user = 'hmuser'
    db_password = 'hmuserdb'
    db_target = ['label_craft']
    backup_path = '/Users/kakao_ent/temp/backup'
else:
    db_host = 'search-hammer-opdb2.dakao.io'
    db_port = '3306'
    db_user = 'hmuser'
    db_password = 'hmuserdb'
    db_target = ['arbiter', 'dsat', 'ringer', 'stormbreaker', 'sven', 'wasp']
    backup_path = '/hanmail/working/hyot/backup'

try:
    for db in db_target:
        backup_file = f"{backup_path}/{db}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
        result = subprocess.run(["mysqldump", "--no-tablespaces", f"--host={db_host}", f"--port={db_port}", f"--user={db_user}",
                                 f"--password={db_password}", db, f"--result-file={backup_file}"])
        print(f"처리 결과: {result}")
        print(f"{db} 백업이 완료되었습니다.")
except Exception as e:
    print(e)
finally:
    print("DB 백업 스크립트를 종료합니다.")
