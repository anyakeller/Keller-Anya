from flask import Flask, render_template
app = Flask(__name__)

#Random Occupation code
import random
# Opens and reads file into stringthing
file=open("occupations.csv", "r")
stringthing = file.read()
file.close()

# Splits the string into an array called splitString
splitString = str.split(stringthing, "\r\n")

dict = {}

'''
# Loops through array line by line
for line in splitString:
	if "Total" not in line:
		if len(line)>0 and line[0]=='"':
			line = line[1:]
			dict[float(line[line.index('"')+2:])]=line[0:line.index('"')]
		elif len(line)>0 and splitString.index(line)!=0:
			#print line
			dict[float(line[line.index(',')+1:])]=line[0:line.index(',')]
'''

for line in splitString:
	if "Total" not in line and "Job" not in line:
		if line.count(",") == 2: # if there are no parenthesis 
			#print line
			splitLine = line.split(",")
			dict[float(splitLine[2])] = [splitLine[0],splitLine[1]]
		elif line.count(",") > 2: #deal with extra commas
			line = line[1:]
			jobTitle = line[:line.index('"')]
			line = line[line.index('"')+2:]
			dict[float(line[line.index(",")+1:])] = [jobTitle, line[:line.index(",")]]
print dict

#because we have to make this a function...
def getRandomOccupation():
	#get a random number from 0 to 997 <-- although the toal is 99.8, we're working with integers and randint() is inclusive of zero
	r = random.randint(0,997)
	temp = 0 #keeps track of probability range
	for key in dict:
		temp += 10 * key
		if r < temp:
			return dict[key]
		if temp == 859:
			return dict[key]

#Start of routes
@app.route("/")
#index
def index():
	l = ["cheese", "queso", "your face", "lmao"]
	return render_template("index.html", potato="turtle", l = l)
	
@app.route("/occupations")

def occupations():
	return render_template("occupations.html", table = dict, occ = getRandomOccupation())

@app.route("/morestuff")

def morestuff():
	return render_template("index.html")

if __name__ == "__main__":
	#app.debug = True #
	app.run()
