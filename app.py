# modules
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from cs50 import SQL

app = Flask(__name__)
db = SQL("sqlite:///static/database.db")


#INDEX PAGE
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/iWaitlist")
def iWaitlist():
    waitdata = db.execute("SELECT * FROM waitlist")
    return render_template("waitlist.html", data = waitdata)

# app.config["MAIL_PASSWORD"] = "Vg@02022006"
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# app.config["MAIL_USERNAME"] = 'getquickblood@gmail.com'
# mail = Mail(app)
# def send_mail(emails, donor):
#     text = "We noticed that we could not help you with your request when you came to us on our website getBloodHelp.com. We are delighted to inform you that we have a new donor who we think might be able to help you. \n Donor details: \n", donor
#     sub = "HELP FOUND!!!"
#     msg = Message(body = text, recipients = emails, subject = sub, sender='getquickblood@gmail.com')
#     mail.send(msg)


###REQUESTING BLOOD

# for recipients requesting blood
@app.route("/help", methods = ["GET"])
def help1():
    return render_template("help.html")

# Sending data and showing appropriate donors for the recipient
@app.route("/helpdata", methods = ["GET", "POST"])
def help2():
    gotHelp = request.form.get("gotHelp")
    name = (request.args.get("name")).capitalize()
    bgroup = request.args.get("bloodGroup")
    email = request.args.get("mail")
    mobile = request.args.get("mobile")
    pin = (request.args.get("pincode")).capitalize()
    state = (request.args.get("state")).capitalize()
    country = (request.args.get("country")).capitalize()
    link = "/helpdata?name=" + name + "&bloodGroup=" + bgroup + "&mail=" + email + "&mobile=" + mobile + "&pincode=" + pin + "&state=" + state + "&country=" + country
    if gotHelp == "y":
        return render_template("helpdata.html", message = True, link = link)
    elif gotHelp == "n":        # If name in waitlist
        db.execute("INSERT INTO waitlist (name, blood_group, email, mobile, country, state, pincode) VALUES (?, ?, ?, ?, ?, ?, ?)", name, bgroup, email, mobile, country, state, pin)
        waitdata = db.execute("SELECT * FROM waitlist ORDER BY blood_group")
        return render_template("waitlist.html", data = waitdata)
    else:
        COUNTRIES = db.execute("SELECT DISTINCT country FROM donors")
        STATES = db.execute("SELECT DISTINCT state FROM donors")
        for i in COUNTRIES:
            if country == i['country']:
                for j in STATES:
                    if state == j['state']:
                        if bgroup=="B-":
                            DAT = db.execute("SELECT * FROM donors WHERE country LIKE ? AND state LIKE ? AND (blood_group=? OR blood_group=?) ORDER BY blood_group, pincode", country, state, 'B-', 'O-')
                        elif bgroup=="B+":
                            DAT = db.execute("SELECT * FROM donors WHERE country LIKE ? AND state LIKE ? AND (blood_group=? OR blood_group=? OR blood_group=? OR blood_group=?) ORDER BY blood_group, pincode", country, state, 'B-', 'B+', 'O+', 'O-')
                        else:
                            DAT = db.execute("SELECT * FROM donors WHERE country LIKE ? AND state LIKE ? AND blood_group IN (SELECT blood_group FROM compatible WHERE donatesto LIKE ?) ORDER BY blood_group, pincode", country, state, ('%'+bgroup+'%'))
                    else:
                        if bgroup=="B-":
                            DAT = db.execute("SELECT * FROM donors WHERE country LIKE ? AND (blood_group=? OR blood_group=?) ORDER BY blood_group, state, pincode", country, "B-", "O-")
                        elif bgroup=="B+":
                            DAT = db.execute("SELECT * FROM donors WHERE country LIKE ? AND (blood_group=? OR blood_group=? OR blood_group=? OR blood_group=?) ORDER BY blood_group, state, pincode", country, 'B-', 'B+', 'O+', 'O-')
                        else:
                            DAT = db.execute("SELECT * FROM donors WHERE country LIKE ? AND blood_group IN (SELECT blood_group FROM compatible WHERE donatesto LIKE ?) ORDER BY blood_group, state, pincode", country, ('%'+bgroup+'%'))
            else:
                if bgroup=="B-":
                    DAT = db.execute("SELECT * FROM donors WHERE blood_group=? OR blood_group=? ORDER BY blood_group, country, state, pincode", "B-", "O-")
                elif bgroup=="B+":
                    DAT = db.execute("SELECT * FROM donors WHERE blood_group=? OR blood_group=? OR blood_group=? OR blood_group=? ORDER BY blood_group, country, state, pincode", 'B-', 'B+', 'O+', 'O-')
                else:
                    DAT = db.execute("SELECT * FROM donors WHERE blood_group IN (SELECT blood_group FROM compatible WHERE donatesto LIKE ?) ORDER BY blood_group, country, state, pincode", ('%'+bgroup+'%'))
                return render_template("helpdata.html", name = name, data = DAT, message2 = True, link = link)
            return render_template("helpdata.html", name = name, data = DAT, link = link)


###DONATING BLOOD
# For donors who want to donate blood
@app.route("/donate", methods = ["GET"])
def donate():
    return render_template("donate.html", message = False, message2 = False)

# Add donor data to database
@app.route("/confirm", methods = ["GET"])
def confirm():
    password = request.args.get("password")
    fname = (request.args.get("first_name")).capitalize()
    lname = (request.args.get("last_name")).capitalize()
    bgroup = request.args.get("bloodGroup")
    email = request.args.get("email")
    mobile = request.args.get("mobile")
    age = request.args.get("age")
    state = (request.args.get("state")).capitalize()
    country = (request.args.get("country")).capitalize()
    pincode = (request.args.get("pincode")).capitalize()
    extra = request.args.get("extra")

    # check for password repetition
    data = db.execute("SELECT password FROM donors")
    for i in data:
        if i["password"] == password:
            return render_template("donate.html", message2 = True, fname = fname, lname = lname, email = email, mobile = mobile, age = age, state = state, country = country, pin = pincode, extra = extra)      # To make sure the password does not repeat

    # if password agreed
    db.execute("INSERT INTO donors (first_name, last_name, blood_group, email, mobile, age, pincode, state, country, additional_info, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", fname, lname, bgroup, email, mobile, age,  pincode, state, country, extra, password)

    # sending mails to people in waitlist
    # waitlistdata = db.execute("SELECT email FROM waitlist WHERE blood_group = ? AND country = ? AND state = ?", bgroup, country, state)
    # if waitlistdata:
    #     donor = db.execute("SELECT * FROM donors WHERE password = ?", password)
    #     send_mail(waitlistdata, donor)
    #     db.execute("DELETE FROM waitlist WHERE email IN ?", waitlistdata)

    return render_template("donate.html", message = True)



###COLLABORATING ORGANISATION AND PEOPLE
@app.route("/collaborators", methods = ["GET"])
def coll():
    donors = db.execute("SELECT * FROM donors ORDER BY first_name")
    return render_template("collaborators.html", donor_data = donors)

###IF DONOR WANTS TO OPT OUT
@app.route("/deactivate", methods = ["GET", "POST"])
def deactivate():
    password = request.args.get("cancel")
    confirmation = request.form.get("confirmation")
    if confirmation == "y" or confirmation == "Y":
        email = request.args.get("row")
        db.execute("DELETE FROM donors WHERE password = ? AND email = ?", password, email)
        return redirect(url_for('coll'))
    elif confirmation == "n" or confirmation == "N":
        donors = db.execute("SELECT * FROM donors ORDER BY first_name")
        return render_template("collaborators.html", donor_data = donors)
    else:
        name = db.execute("SELECT first_name, last_name FROM donors WHERE password = ? ORDER BY blood_group", password)
        if name:
            fname = name[0]['first_name']
            lname = name[0]['last_name']
            link = "/deactivate?password=" + password
            return render_template("delete.html", fname = fname, lname = lname, link = link)
        else:
            donors = db.execute("SELECT * FROM donors ORDER BY blood_group")
            return render_template("collaborators.html", donor_data = donors)


# Frequently Asked Questions
@app.route("/faq")
def faq():
    return render_template("faq.html")


if __name__ == '__main__':
   app.run(debug = True)

