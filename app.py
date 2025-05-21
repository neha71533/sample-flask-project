from flask import Flask,render_template
app= Flask(__name__)
@app.route('/')
def hy():    
     fruits=["apple","orange","mango"]
     return render_template("hy.html", items =fruits)



@app.route('/users')
def users():  
     users=["nia","sia","lia"]   
     return render_template("users.html",users= users)
if __name__ =='__main__':
    app.run(debug = True) 