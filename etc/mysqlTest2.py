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
today_datetime = ''
today_str = ''


# 변수 초기화
def init(_profile):
    global db_host
    global db_port
    global db_user
    global db_password
    global db_target
    global path_temp_backup
    global path_upload
    global today_datetime
    global today_str

    today_datetime = datetime.datetime.now()
    today_str = today_datetime.strftime('%Y%m%d')

    if _profile == 'local':
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


# 파일 백업 및 압축
def process():
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
            upload(file_backup_gzip)
            folder_organize()

        print("DB 백업이 완료되었습니다.")
    except Exception as e:
        print(e)
    finally:
        print("DB 백업 스크립트를 종료합니다.")


# 하둡 파일 업로드
def upload(_file_backup_gzip):
    if profile == 'local':
        pass
    else:
        subprocess.run(["hadoop", "fs", "-mkdir", f"{path_upload}/{today_str}"], stdout=subprocess.DEVNULL)
        subprocess.run(["hadoop", "fs", "-put", _file_backup_gzip, f"{path_upload}/{today_str}"])
        os.remove(_file_backup_gzip)


# 하둡 폴더 정리
def folder_organize():
    if profile == 'local':
        folderList = os.listdir(path_upload)
        folderList = list(filter(lambda x: re.compile("[0-9]{8}").match(x), folderList))

        for folder in folderList:
            td = (datetime.datetime(today_datetime.year, today_datetime.month, today_datetime.day)
                  - datetime.datetime.strptime(folder, '%Y%m%d'))

            if td.days > 21:
                shutil.rmtree(f"{path_upload}/{folder}")
    else:
        result = subprocess.run(['hadoop', 'fs', '-ls', '-C', '/backup'], stdout=subprocess.PIPE, text=True)
        folderList = result.stdout.split("\n")
        folderList = list(filter(lambda x: re.compile("/backup/[0-9]{8}").match(x), folderList))

        for folder in folderList:
            date = folder.split('/')[-1]
            td = (datetime.datetime(today_datetime.year, today_datetime.month, today_datetime.day)
                  - datetime.datetime.strptime(date, '%Y%m%d'))

            if td.days > 21:
                subprocess.run(["hadoop", "fs", "-rm", "-r", folder])


init(profile)
process()
folder_organize()

