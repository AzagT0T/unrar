import os
import time
import subprocess

#TR_TORRENT_DIR
#TR_TORRENT_HASH
#TR_TORRENT_ID
#TR_TORRENT_NAME

torrent_dir = '/media/downloads/misc'
torrent_name = 'Prison Architect Alpha'
output_dir = '/media/downloads/rartest'

work_dir = torrent_dir + '/' + torrent_name
dir_list = os.listdir(work_dir)
print dir_list
if dir_list != []:
    for i in dir_list:
        if i.lower().endswith(('.rar', '.zip')):
            rar_file = work_dir + '/' + i
            p = subprocess.Popen(["unrar", "x", rar_file, output_dir], stdout=subprocess.PIPE)
            output, err = p.communicate()
            print output