#! /home/appviewx/appviewx/Python/bin/python
import paramiko
import sys

ssh = paramiko.SSHClient()
host_name = sys.argv[1]
common_name = sys.argv[2]
sr_no = sys.argv[3]
crt_path = sys.argv[4]
key_path = sys.argv[5]
conf_file_path = sys.argv[6]

import appviewx
import Decrypt_Python3 as Decrypt
connection = appviewx.db_connection()
host = connection.appviewx.device.find_one({'name':host_name},{'ip':1})['ip']
username,password = Decrypt.getpassword(host_name)

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,username = username,password = password,port = 22,timeout=120)

print(host)
print(username)
print(password)

cert_name = "SSLCertificateFile    {loc}/{common_name}_{sr_no}.crt".format(common_name = common_name, sr_no=sr_no,loc = crt_path)
key_name = "SSLCertificateKeyFile   {loc}/{common_name}_{sr_no}.key".format(common_name = common_name, sr_no=sr_no, loc = key_path)


transport = paramiko.Transport((host, 22))
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)

sftp.get(conf_file_path,"/var/tmp/apacheConfFile.conf_old")

ssl_file = open("/var/tmp/apacheConfFile.conf_old")
file_content = ssl_file.readlines()
ssl_file.close()
sftp_file = open("/var/tmp/apacheConfFile.conf","w+")


for i in file_content:
	if "SSLCertificateFile" in i and "#" not in i:
		sftp_file.writelines("\t\t"+cert_name+"\n")
	elif "SSLCertificateKeyFile" in i and "#" not in i:
		sftp_file.writelines("\t\t"+key_name+"\n")
	# elif "SSLCertificateChainFile" in i and "#" not in i:
	# 	sftp_file.writelines("\t\tSSLCertificateChainFile /home/ubuntu/intermediateCa.crt\n")
	else:
		sftp_file.writelines(i)

sftp_file.close()



sftp.put("/var/tmp/apacheConfFile.conf",conf_file_path)
transport.close()

ssh.exec_command("service apache2 restart")
ssh.close()

