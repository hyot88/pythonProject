import subprocess
import datetime
import gzip
import os
import re
import shutil

profile = 'local'

db_host = ''
db_port = ''
db_user = ''
db_password = ''
db_target = []
path_temp_backup = ''
path_upload = ''

if profile == 'local':
    db_host = '127.0.0.1'
    db_port = '3306'
    db_user = 'hmuser'
    db_password = 'hmuserdb'
    db_target = ['label_craft']
    path_temp_backup = '/Users/kakao_ent/temp/backup_temp'
    path_upload = '/Users/kakao_ent/temp/upload'
else:
    db_host = 'search-hammer-opdb2.dakao.io'
    db_port = '3306'
    db_user = 'hmuser'
    db_password = 'hmuserdb'
    # db_target = ['arbiter', 'dsat', 'ringer', 'stormbreaker', 'sven', 'wasp']
    db_target = ['arbiter', 'dsat']
    path_temp_backup = '/hanmail/working/hyot/backup_temp'
    path_upload = '/backup'

today_datetime = datetime.datetime.now()
today_str = today_datetime.strftime('%Y%m%d')

try:
    for db in db_target:
        file_backup_name = f"{path_temp_backup}/{db}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        file_backup_ori = file_backup_name + '.sql'
        file_backup_gzip = file_backup_ori + '.gz'

        subprocess.run(
            ["mysqldump", "--no-tablespaces", f"--host={db_host}", f"--port={db_port}", f"--user={db_user}",
             f"--password={db_password}", db, f"--result-file={file_backup_ori}"])

        with open(file_backup_ori, 'r') as f_ori:
            data = f_ori.read()
            with gzip.open(file_backup_gzip, 'wb') as f_gzip:
                f_gzip.write(data.encode("utf-8"))

        os.remove(file_backup_ori)

        if profile == 'local':
            folderList = os.listdir(path_upload)
            folderList = list(filter(lambda x: re.compile("[0-9]{8}").match(x), folderList))

            for folder in folderList:
                td = (datetime.datetime(today_datetime.year, today_datetime.month, today_datetime.day)
                      - datetime.datetime.strptime(folder, '%Y%m%d'))

                if td.days > 21:
                    shutil.rmtree(f"{path_upload}/{folder}")
        else:
            subprocess.run(["hadoop", "fs", "-mkdir", f"{path_upload}/{today_str}"])
            subprocess.run(["hadoop", "fs", "-put", file_backup_gzip, f"{path_upload}/{today_str}"])
            os.remove(file_backup_gzip)
            # 하둡 폴더 리스트 가져오기
            # 하둡 폴더 삭제하기

    print("DB 백업이 완료되었습니다.")
except Exception as e:
    print(e)
finally:
    print("DB 백업 스크립트를 종료합니다.")
