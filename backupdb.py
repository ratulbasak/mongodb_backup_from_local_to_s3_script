import datetime
import os
import string
import tarfile
import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from datetime import timedelta

# Configuration inlcudes of AWS credentials, dblist config file and local backup path

aws_access_key = 'your_access_key'
aws_secret_key = 'your_secret_key'
aws_bucket = 'bucket_name'
dblistfile='db_list_filename'
path='/tmp/'

with open(dblistfile) as file:      
    array = file.read().splitlines()

for line in array:
    words=line.split(",")
    #each line words will be extracted and classifed here
    ip=words[0]    #first parameter is ip -->127.0.0.1 means local machine
    db=words[1]    #second parameter is database name
    uname=words[2] #third paramter is username
    pwd=words[3]   #fourth parameter is password
    
    #database backup command
    cmd="mongodump -h '"+ip+"' -d '"+db+"' -u '"+uname+"' -p '"+pwd+"' --out '"+path+"'"
    os.system(cmd)
    
    #configuring flepath and tar file name 
    today = str(datetime.date.today())
    archieve_name=db+today+".tar.gz"
    db_path=path+db
    archieve_path=path+archieve_name
    s3_path=db+'/'+archieve_name      #s3 path: tarfile name under the dbname folder

    print('[FILE] Creating archive for ' + db)
    cmd='tar -czvf '+archieve_path+' '+db_path
    os.system(cmd)

    # Establish S3 Connection
    s3 = S3Connection(aws_access_key, aws_secret_key)
    bucket = s3.get_bucket(aws_bucket)

    # Send files to S3
    print ('[S3] Uploading file archive ' + archieve_name + '...')
    k = Key(bucket)
    k.key = s3_path
    print(k.key)
    k.set_contents_from_filename(archieve_path)
    k.set_acl("public-read")
    os.system(cmd)

    print('[S3] Clearing previous file archive ' + archieve_name + '...')
    os.remove(archieve_path);
