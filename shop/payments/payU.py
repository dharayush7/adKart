import datetime
import hashlib
import urllib.parse

def merchant_key():
    MID = "JPM7Fg"
    SALT = "TuxqAugd"
    credes = {
        "key":MID,
        "salt": SALT
    }
    return credes



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

def payUHasher(params):
    credes = merchant_key()
    key = credes.get('key')
    salt = credes.get('salt')
    txnid = params.get("txnid")
    amount = params.get("amount")
    productinfo = params.get("productinfo", "")
    firstname = params.get("firstname", "")
    email = params.get("email", "")
    udf1 = params.get("udf1", "")
    udf2 = params.get("udf2", "")
    udf3 = params.get("udf3", "")
    udf4 = params.get("udf4", "")
    udf5 = params.get("udf5", "")
    if params.get("additional_charges") is not None and params.get("additional_charges") != "":
        additional_charges = params.get("additional_charges")
        payment_hash_sequence = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}|{additional_charges}"
    else:
        payment_hash_sequence = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}"
    hash_value = hashlib.sha512((payment_hash_sequence).encode('utf-8')).hexdigest()
    return hash_value


def payUParse(body):
    bobyStr = str(body, 'utf-8')
    bodyMaxJson = urllib.parse.parse_qs(bobyStr)
    bodyJson = {}

    for i in bodyMaxJson:
        bodyJson[i] = (bodyMaxJson.get(i))[0] # type: ignore
    return bodyJson