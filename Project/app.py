from flask import Flask, render_template,redirect,url_for,request,json

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    return render_template('index.html')

@app.route('/my-link/')
def my_link():
  return 'Here is your requested chart'
   
if __name__=='__main__':
    app.run(debug=True)

