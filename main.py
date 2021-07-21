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
#                                                  #
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
    app.run(host="0.0.0.0", port=5000)
#####################################################
