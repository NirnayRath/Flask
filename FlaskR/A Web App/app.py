from flask import Flask, request, render_template, url_for, redirect
import os
from download import *
app=Flask(__name__)

@app.route("/login",methods=['GET','POST'])
def login():
	error= None
	if request.method=='POST':
		if request.form['username']!="CLu" or request.form['password']!="500":
			error ="Wrong credentials!!"
			print(error)
		else:
			return redirect('/insideSys')
	return render_template('login.html',error=error)

@app.route("/insideSys",methods=['GET','POST'])
def insideSys():
	if request.method=='POST':
		downloadhere(request.form[""])
	
	return render_template('downloadrequest.html')


if __name__=="__main__":
	app.run(debug=True, port=5000)