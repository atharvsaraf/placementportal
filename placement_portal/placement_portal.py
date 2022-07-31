from flask import *
from os import *
from manager import *
app = Flask(__name__)
app.secret_key="art@12ka4"
db=manager()


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/reg',methods=["GET","POST"])
def regestration():
    if request.method=="GET":
        return render_template("regestration.html")
    if request.method=="POST":
        nm=request.form["nm"]
        id=request.form["id"]
        email=request.form["email"]
        mobno=request.form["mobno"]
        cgpa=request.form["cgpa"]
        add=request.form["add"]
        branch=request.form["branch"]
        year=request.form["year"]
        lang=request.form["lang"]
        gender=request.form["gender"]
        resume=request.files["resume"]
        image=request.files["photo"]
        resume.save('static/resume/' + resume.filename)
        image.save('static/image/' +image.filename)
        rec=db.regester(nm,id,email,mobno,cgpa,add,branch,year,lang,gender,resume.filename,image.filename)
        if rec:
            msg="Account created successfully."
            return render_template("student.html",rec=rec)
        else:
            msg="Try Again Later."
            return render_template("regestration.html",msg=msg)

@app.route('/studlogin',methods=["GET","POST"])
def studlogin():
    if request.method=="GET":
        return render_template("studentlogin.html")
    if request.method=="POST":
        usrnm=request.form["username"]
        pswd=request.form["id"]
        rec=db.login(usrnm,pswd)

        session["id"]=pswd
        if rec==None:
            msg="Username or password is incorrect"
            return render_template("studentlogin.html",msg=msg)
        else:
            return render_template("student.html",rec=rec)

@app.route('/adminlogin',methods=["GET","POST"])
def adminlogin():
    if request.method=="GET":
        return render_template("adminlogin.html")
    if request.method=="POST":
        nm=request.form["name"]
        pswd=request.form["password"]
        if nm=="GCOEA" and pswd=="gcoea@123":
            return render_template("admin.html")
        else:
            msg="Username or password is incorrect"
            return render_template("adminlogin.html",msg=msg)





@app.route('/apply',methods=["GET","POST"])
def apply():
    rec = db.allcompanies()
    return render_template("application.html",rec=rec)

@app.route('/studentapplied',methods=["GET","POST"])
def studentapplied():
    cid=request.args["cid"]
    id=session["id"]
    print("comp",cid)
    print("stud",id)
    

    return render_template("student.html")




@app.route('/compreg',methods=["GET","POST"])
def compreg():
    if request.method=="GET":
        return render_template("compreg.html")
    if request.method=="POST":
        nm = request.form["name"]
        email=request.form["email"]

        tag=request.form["tagline"]
        pswd=request.form["password"]
        print(pswd)
        photo=request.files["image"]


        photo.save('static/companyimg/' +photo.filename)
        rec=db.compreg(nm,email,tag,pswd,photo.filename)
        if rec==None:
            msg="Try after sometime."
            return render_template("compreg.html",msg=msg)
        else:
            msg = "Account created successfully."
            return render_template("company.html",rec=rec)

@app.route('/companylogin',methods=["GET","POST"])
def companylogin():
    if request.method=="GET":

        return render_template("companylogin.html")
    if request.method=="POST":
        nm=request.form["username"]
        pswd=request.form["pswd"]
        rec=db.complogin(nm,pswd)
        if rec:
            return render_template("company.html",rec=rec)
        else:
            msg="Username or password is incorrect"
            return render_template("companylogin.html",msg=msg)

@app.route('/faq',methods=["GET","POST"])
def faq():
    return render_template("faq.html")


@app.route('/companyinfo',methods=["GET","POST"])
def companyinfo():
    rec=db.allcompanies()
    return render_template("allcompany.html",rec=rec)

@app.route('/studinfo',methods=["GET","POST"])
def studinfo():
    rec=db.allstudents()
    return render_template("allstudents.html",rec=rec)
if __name__ == '__main__':
    app.run()
