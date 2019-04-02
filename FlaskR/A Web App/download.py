#This is the downloading module for the webapp..

import requests

def down(fname, lname):
	print(fname,'\n',lname)
	req=requests.get(lname).content
	with open(fname,'wb') as img_file:
		img_file.write(req)
