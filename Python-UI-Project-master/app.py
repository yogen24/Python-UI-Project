from flask import Flask, render_template,redirect,url_for,request,json

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    return render_template('index.html')

@app.route('/filters/',methods=['POST'])
def my_link():
  array = request.json['get']
  print(array)
  return "x"
   
if __name__=='__main__':
    app.run(debug=True)

