from flask import Flask
app = Flask(__name__)



@app.route("/")

def hello_world():
	return "No hablo queso"

def yala():
	print "Bissli Group!"
	
@app.route("/home")

def home():
	return "Homework 24/7"

@app.route("/school")

def school():
	return "cry"

if __name__ == "__main__":
	app.run()
