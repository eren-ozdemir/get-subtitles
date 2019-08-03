import os 
from os import path,listdir
from os.path import splitext
import requests
import urllib
import urllib.request
import gzip
import shutil
from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File
from pythonopensubtitles.utils import get_md5

ost = OpenSubtitles()

currdir = os.getcwd()

videos=[]
labels=[]
fullPath=""

ext = [".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", ".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv",".m4v"]

def downloadSub():
    names= os.listdir()

    for name in names:
        if (name.endswith(tuple(ext))):
            file_name,file_ext=splitext(name)
            class Test(object):
                usename = 'ermisss'
                password = '258456++'
                video = name
                path = currdir
            
            # Test.video=file_name
            fullPath=currdir+'/'+file_name

            token = ost.login('ermisss', '258456++')
            assert type(token) == str

            f = File(path.join(Test.path, Test.video))
            hash = f.get_hash()
            assert type(hash) == str

            size = f.size
            assert type(size) == str 

            dataid = ost.search_subtitles([{'sublanguageid': 'eng', 'moviehash': hash, 'moviebytesize': size}])
            id_subtitle = dataid[0].get('IDSubtitle')
            id_sub_movie_file = dataid[0].get('IDSubMovieFile')
            subURL= dataid[0].get('SubDownloadLink')
            assert type(dataid) == list

            urllib.request.urlretrieve(subURL, fullPath+".srt.gz")
            with gzip.open(fullPath+'.srt.gz', 'rb') as f_in:
                with open(fullPath+'.srt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            if os.path.exists(fullPath+'.srt.gz'):
                os.remove(fullPath+'.srt.gz')


downloadSub()
