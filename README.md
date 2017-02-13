# mongodb_backup_script

Configuration includes of AWS credentials, dblist config file and local backup path...

In the dblist file consists of ip address,db name,username,password in each line. This script uses every line and split them in specific field. Mongodb backup command then run and store them to the /tmp/ directory as tar file. We've to connect to the s3 bucket while uploading the backup files. I use ## boto which is the Amazon Web Services (AWS) SDK for Python, which allows Python developers to write software that makes use of Amazon services like S3 and EC2. Boto provides an easy to use, object-oriented API as well as low-level direct service access. Here is also define the AWS S3 path in which the tar files will be uploaded. When all the databases are uploaded to the s3 then the script removes the local backup file.
