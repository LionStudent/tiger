import mysql.connector

 

def connect():

    db = mysql.connector.connect(

        host='sql3.freemysqlhosting.net',

        port=3306,

        database='sql3337629',

        user='sql3337629',

        password='IGseDDutut'

    )

    cursor=db.cursor()

    return db, cursor


def searchTextData(name):

    db, cursor = connect()


    query = 'select isTotal,isRaw,metric,fromDate,toDate,url from covid19 where name="%s"' % name

    cursor.execute(query)

    retval=[]

    for isTotal,isRaw,metric,fromDate,toDate,url in cursor:

        retval.append({

            'isTotal': isTotal,

            'isRaw': isRaw,

            'metric': metric,

            'from': fromDate,

            'to': toDate,

            'url': url

            })

               

    db.close()

    return retval

