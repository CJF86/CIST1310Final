from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)
import sqlite3 as sql

#sets app route for the AboutUs.htm page
@app.route('/', methods = ["POST", "GET"])
def AboutUs():
    return render_template("AboutUs.htm")

@app.route('/IceCreamHome')
def IceCream():
    return render_template("IceCreamHome.htm")

@app.route('/result')
def result():
    return render_template("result.htm")

@app.route('/IdeaSubmit', methods = ["POST", "GET"])
def IdeaSubmit():
    # return render_template("IceCreamHome.htm")
    if request.method == 'POST' or request.method == 'GET':
        # try:
        CreamName = request.form["FlavorName"]
        CreamFlavor = request.form["FlavorType"]
        CreamCreator = request.form["CustName"]
        CreamContact = request.form["CustPhone"]
        CreamAmount = request.form["CreamAmount"]

        with sql.connect("IceCreamDataBase.db") as con:
            Connection = con.cursor()
            Connection.execute("INSERT INTO IceCream (IcecreamName, Flavor, Creator, CreatorPhone, Amount) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(CreamName,CreamFlavor,CreamCreator,CreamContact,CreamAmount))

            con.commit()
            return render_template("result.htm")
            con.close()
                

        # except:
        #     return render_template("AboutUs.htm")

        # finally:
        #     return render_template("IceCreamList.htm")
        #     Connection.close()
    
            

@app.route('/list', methods = ["POST", "GET"])
def list():
    DBCon = sql.connect("IceCreamDataBase.db")
    DBCon.row_factory = sql.Row

    CurrentConn = DBCon.cursor()
    CurrentConn.execute("SELECT * FROM IceCream")

    rows = CurrentConn.fetchall()
    return render_template("IceCreamList.htm",rows = rows)







if __name__ =='__main__':
    app.run()
