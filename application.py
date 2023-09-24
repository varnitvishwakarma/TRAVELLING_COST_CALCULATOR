from flask import Flask,request,render_template

application=Flask(__name__)

app=application

@app.route('/home',methods=["GET","POST"])
def home_page():

    if request.method=="POST":
        AVG=float(request.form.get("AVG"))
        FUEL=float(request.form.get("FUEL"))
        DIST=float(request.form.get("DIST"))

        RESULT=(FUEL/AVG)*DIST


        
        return render_template('home.html',result=RESULT)

    else:
        return render_template('home.html')



if __name__=="__main__":
    app.run(host='0.0.0.0')
