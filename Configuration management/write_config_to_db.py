import os

from pymongo import MongoClient
import gridfs
monogDBIP = raw_input("Enter the ip of mongoDB:")
ip_host = monogDBIP+":5000"
conn = MongoClient(ip_host)
monoguser = raw_input("Enter the username of mongoDB:")
monogpass = raw_input("Enter the password of mongoDB:")
conn.admin.authenticate(monoguser,monogpass,source="admin") 
db = conn.configDB
fs = gridfs.GridFS(db)
#files=os.listdir(r"/home/local/PAYODA/yuvaraj.g/mongodb/"SAMPLE_TMSH_F5_GTM_V10_POOL.txt"")
files=raw_input("Enter the full path of configuration file to push in mongoDB:")
files= files.replace("/","//")
files=files+"//"
file_name_list = os.listdir(files)
#files="//home//local//PAYODA//yuvaraj.g//mongodb//"
#file_name_list = ["SAMPLE_TMSH_F5_GTM_V10_POOL.txt"]
for file_name in file_name_list:
	obj= fs.find_one({"filename":file_name})
	if obj != None:
		fs.delete(obj._id)
	with fs.new_file(filename=file_name) as fp:
		#full_path ="//home//local//PAYODA//yuvaraj.g//mongodb//"+file_name
		full_path =files+file_name
		   
		fp.write(open(full_path,"r"))
	
#print "after Pushed",len(list(db.fs.files.find()))
print "Done"