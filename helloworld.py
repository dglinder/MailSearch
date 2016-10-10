from flask import Flask
app = Flask(__name__)

from time import gmtime, strftime

#import time;
#ticks = time.time()

@app.route("/")
def hello_world():
    return "Under construction - please check back later: %s" %  strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

@app.route('/hello')
def pagetwo():
    return "Page two without arguments."

@app.route('/hello/<username>')
def pagetwo_user(username):
    return "Page two: %s" % username

if __name__ == "__main__":
    app.run(host='143.95.40.76',port='32320')
    #app.run(port='32320')

