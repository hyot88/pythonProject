import subprocess
import datetime
import os
import re
import shutil

profile = 'prod'

path_target = ''
path_temp_backup = ''
path_upload = ''
today_datetime = ''
today_str = ''


# 변수 초기화
def init(_profile):
    global path_target
    global path_temp_backup
    global path_upload
    global today_datetime
    global today_str

    today_datetime = datetime.datetime.now()
    today_str = today_datetime.strftime('%Y%m%d')

    if _profile == 'local':
        path_target = '/Users/kakao_ent/temp/target'
        path_temp_backup = '/Users/kakao_ent/temp/backup_temp'
        path_upload = '/Users/kakao_ent/temp/upload/jenkins'
    else:
        path_target = '/hanmail/.jenkins/jobs'
        path_temp_backup = '/hanmail/working/hyot/backup_temp'
        path_upload = '/backup/jenkins1'
        # path_upload = '/backup/jenkins2'


# 파일 백업 및 압축
def process():
    file_backup_tar = f"{path_temp_backup}/jenkinsJobs_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.tar"
    file_exclude = f"{path_target}/*/builds"
    subprocess.run(["tar", "cvfP", file_backup_tar, "--exclude", file_exclude, path_target])
    upload(file_backup_tar)


# 하둡 파일 업로드
def upload(_file_backup_tar):
    if profile == 'local':
        pass
    else:
        subprocess.run(["hadoop", "fs", "-mkdir", f"{path_upload}/{today_str}"])
        subprocess.run(["hadoop", "fs", "-put", _file_backup_tar, f"{path_upload}/{today_str}"])
        print(f"{_file_backup_tar} 업로드 완료")
        os.remove(_file_backup_tar)


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
        # result = subprocess.run(['hadoop', 'fs', '-ls', '-C', path_upload], stdout=subprocess.PIPE, text=True)
        result = subprocess.run(['hadoop', 'fs', '-ls', '-C', path_upload], stdout=subprocess.PIPE, universal_newlines=True)
        folderList = result.stdout.split("\n")
        folderList = list(filter(lambda x: re.compile("/backup/[0-9]{8}").match(x), folderList))

        for folder in folderList:
            date = folder.split('/')[-1]
            td = (datetime.datetime(today_datetime.year, today_datetime.month, today_datetime.day)
                  - datetime.datetime.strptime(date, '%Y%m%d'))

            if td.days > 21:
                subprocess.run(["hadoop", "fs", "-rm", "-r", folder])

    print("하둡 폴더 정리가 완료되었습니다.")


init(profile)
process()
folder_organize()
print("Jenkins 백업 스크립트를 종료합니다.")
