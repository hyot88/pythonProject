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
    backup_path = '/Users/kakao_ent/temp'
else:
    db_host = 'search-hammer-opdb2.dakao.io'
    db_port = '3306'
    db_user = 'hmuser'
    db_password = 'hmuserdb'
    target_db = ['arbiter', 'dsat', 'ringer', 'stormbreaker', 'sven', 'wasp']
    backup_path = '/hanmail/working/hyot'

for db in db_target:
    backup_file = f"{backup_path}/backup_{db}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    subprocess.run(["mysqldump", "--no-tablespaces", f"--host={db_host}", f"--port={db_port}", f"--user={db_user}",
                    f"--password={db_password}", db, f"--result-file={backup_file}"])
    print(f"{db} 백업이 완료되었습니다.")
