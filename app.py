import util.testmod, util.occupations
from flask import Flask, render_template
app = Flask(__name__)


#Start of routes
@app.route("/")
#index
def index():
	l = ["cheese", "queso", "your face", "lmao"]
	return render_template("index.html", potato="turtle", l = l)
	
@app.route("/occupations")

def occupations():
	return util.occupations.render()
	#return render_template("occupations.html", table = dict, occ = getRandomOccupation())

@app.route("/testmod")

def testmodPage():
	return util.testmod.test()

if __name__ == "__main__":
	#app.debug = True #
	app.run()
