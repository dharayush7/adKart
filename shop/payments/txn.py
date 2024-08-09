import datetime

def createTxnId():
    x = str(datetime.datetime.now())
    year =x[0:4]
    month= x[5:7]
    day = x[8:10]
    hr = x[11:13]
    mi = x[14:16]
    sec = x[17:19]
    msec = x[20:26]

    txnId = year + month + day + hr + mi + sec + msec
    return txnId