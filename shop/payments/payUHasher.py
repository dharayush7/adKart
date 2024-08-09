import hashlib
from . import payUCreads



def generate_hash(params):
    credes = payUCreads.merchant_key()
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