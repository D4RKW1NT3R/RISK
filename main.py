############ main.py ##################
# Author - c00lhawk607                #
# Company - N/A                       #
# Email - jordandixon2004@outlook.com #
#######################################


from flask import *
app = Flask(__name__)


####################################################
#                Home Routes                       #
@app.route("/")
def home():
    return render_template("/pages/home.html")
#                                                  #
@app.route("/home")
def home2():
    return redirect("/")
#                                                  #
@app.route("/index")
def home3():
    return redirect("/")
#                                                  #
####################################################

####################################################
#                Routes for ...                    #
@app.route("/jordan")
def jordan():
    return render_template("/pages/ee.html")
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#####################################################

#####################################################
#                  Runs the website                 #
if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=os.getenv("PORT"))
#####################################################
