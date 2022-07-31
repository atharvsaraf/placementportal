import mysql.connector as sql
class manager:
    def __init__(self):
        self.conn=sql.connect(database="placement",user="root",password="admin")

    def regester(self,nm,id,email,mob,cgpa,add,branch,year,lang,gender,resume,image):
        cmd="insert into signup(name,id,emailid,mobileno,cgpa,address,branch,year,lang,gender,resume,image)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur=self.conn.cursor()
        cur.execute(cmd,[nm,id,email,mob,cgpa,add,branch,year,lang,gender,resume,image])
        self.conn.commit()
        cmd="select max(srno) from signup"
        cur=self.conn.cursor()
        cur.execute(cmd)
        rec=cur.fetchone()
        srno=rec[0]
        cmd="select * from signup where srno=%s"
        cur=self.conn.cursor()
        cur.execute(cmd,[srno])
        res=cur.fetchone()
        if res==None:
            return False
        else:
            return res



    def login(self,usrnm,pswd):
        cmd="select * from signup where id=%s"
        cur=self.conn.cursor()
        cur.execute(cmd,[pswd])
        rec=cur.fetchone()
        return rec

    def compreg(self,nm,email,tagline,pswd,image):
        cmd="insert into company(name,email,tagline,password,image)values(%s,%s,%s,%s,%s)"
        cur=self.conn.cursor()
        cur.execute(cmd,[nm,email,tagline,pswd,image])
        self.conn.commit()
        cmd = "select max(cid) from company"
        cur = self.conn.cursor()
        cur.execute(cmd)
        rec = cur.fetchone()
        cid = rec[0]
        cmd = "select * from company where cid=%s"
        cur = self.conn.cursor()
        cur.execute(cmd, [cid])
        res = cur.fetchone()
        if res == None:
            return False
        else:
            return res



    def saveresume(self,id,filename):
        cmd="insert into cv(id,resume)values(%s,%s)"
        cur=self.conn.cursor()
        cur.execute(cmd,[id,filename])
        self.conn.commit()
        cmd="select max(cvid) from cv"
        cur=self.conn.cursor()
        cur.execute(cmd)
        rec=cur.fetchone()
        cvid=rec[0]
        cmd="select * from cv where cvid=%s"
        cur = self.conn.cursor()
        cur.execute(cmd,[cvid])
        res = cur.fetchone()


        return res

    def complogin(self,nm,pswd):
        cmd = "select * from company where password=%s"
        cur = self.conn.cursor()
        cur.execute(cmd, [pswd])
        rec = cur.fetchone()
        return rec


    def allcompanies(self):
        cmd="select * from company"
        cur=self.conn.cursor()
        cur.execute(cmd)
        rec=cur.fetchall()
        return rec

    def allstudents(self):
        cmd="select * from signup"
        cur = self.conn.cursor()
        cur.execute(cmd)
        rec = cur.fetchall()
        return rec

    def compstud(self,sid,cid):
        cmd="insert into compstud(sid,cid)values(%s,%s)"
        cur=self.conn.cursor()
        cur.execute(cmd,[sid,cid])
        self.conn.commit()

