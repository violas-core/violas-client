import datetime
from lbrtypes.transaction import TransactionPayload, RawTransaction, SignedTransaction
from libra_client.account import Account
from crypto.ed25519 import ED25519_SIGNATURE_LENGTH
from lbrtypes.transaction.authenticator import TransactionAuthenticator

def create_unsigned_txn(
    payload: TransactionPayload,
    sender_address,
    sender_sequence_number,
    max_gas_amount,
    gas_unit_price,
    txn_expiration,
) -> RawTransaction:
    return RawTransaction(
        sender_address,
        sender_sequence_number,
        payload,
        max_gas_amount,
        gas_unit_price,
        int(datetime.datetime.now().timestamp()) + txn_expiration
    )

def create_user_txn(
    payload,
    sender_account: Account,
    sender_sequence_number,
    max_gas_amount,
    gas_unit_price,
    txn_expiration,
) -> SignedTransaction:
    raw_txn = create_unsigned_txn(
        payload,
        sender_account.address,
        sender_sequence_number,
        max_gas_amount,
        gas_unit_price,
        txn_expiration,
    )
    tx_hash = raw_txn.hash()
    signature = sender_account.sign(tx_hash)[:ED25519_SIGNATURE_LENGTH]
    authenticator = TransactionAuthenticator.ed25519(sender_account.public_key, signature)
    return SignedTransaction(raw_txn, authenticator)


