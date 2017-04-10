Configuration includes of AWS credentials, dblist config file and local backup path...

Daily mongodb backup script is saved which depends on another file named dblist.config. This scripts backups all the secured mongodb databases in a single ec2 instance to a specified S3 bucket. Write over the target database information in the following order,

        IP,databasename,db_username,db_password

The above information can be obtained from db-passlist file which is already stored in the keyfile directory. Since python backup script along with dblist.config file needs to be stored to target instance containing mongodb database so IP address is advised to 127.0.0.1. A sample configuration of dblist.config file is

        127.0.0.1,DB_NAME,DB_USER,DB_PASSWORD

Assumed that dblist.config file with backup script is stored in remote db instance. If multiple databases need to backup from the same instance then it is recommended to write the information in a list manner with no extra .Due to separation of S3 backup buckets for different databases it is recommended to copy both files in remote machines.

After putting backupdb.py & dblist.config files in remote machine set the following crojob to autbackup is specific bucket at specific time. To do so first install boto framework in the remote machine.

        pip install boto

Then add the cronjob for daily databse backup at 1:00 A.M.

        crontab -e

        0 1 * * * python backupdb.py > mongo-bkg-s3.log 2>&1 && mail -s "backup of mongodb stage is successful" user@gmail.com
This above cronjob emails to specifed email address if relayhost is configured in the remote machine where cronjob is running.
