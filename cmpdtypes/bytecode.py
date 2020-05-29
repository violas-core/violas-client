from enum import IntEnum
from lbrtypes.move_core.account_address import AccountAddress

class CodeType(IntEnum):
    BANK = 2000
    BORROW = 2001
    ENTER_BANK = 2002
    EXIT_BANK = 2003
    LIQUIDATE_BORROW = 2004
    LOCK = 2005
    PUBLISH = 2006
    REDEEM = 2007
    REGISTER_TOKEN = 2008
    REPAY_BORROW = 2009
    UPDATE_COLLATERAL_FACTOR = 2010
    UPDATE_PRICE = 2011


bytecodes = {
    "bank": b'\xa1\x1c\xeb\x0b\x01\x00\x0e\x01\x85\x00\x00\x00\x0e\x00\x00\x00\x02\x93\x00\x00\x00/\x00\x00\x00\x03\xc2\x00\x00\x00\x81\x01\x00\x00\x04C\x02\x00\x008\x00\x00\x00\x05{\x02\x00\x006\x02\x00\x00\x07\xb1\x04\x00\x00*\x05\x00\x00\x08\xdb\t\x00\x00 \x00\x00\x00\x06\xfb\t\x00\x00$\x00\x00\x00\x0f\x1f\n\x00\x00\x01\x00\x00\x00\n \n\x00\x00w\x00\x00\x00\x0b\x97\n\x00\x00\x04\x00\x00\x00\x0c\x9b\n\x00\x00\xfd\x10\x00\x00\r\x98\x1b\x00\x00(\x00\x00\x00\x0e\xc0\x1b\x00\x00\x06\x00\x00\x00\x00\x00\x01\x01\x01\x02\x01\x03\x01\x04\x01\x05\x01\x06\x00\x07\x01\x00\x00\x08\x01\x01\x01\x00\t\x01\x00\x00\n\x01\x00\x00\x0b\x01\x00\x00\x0c\x01\x00\x00\r\x01\x00\x00\x0e\x01\x00\x00\x0f\x02\x00\x03\n\x01\x01\x01\x01\x13\x01\x01\x02\x03\x10\x00\x01\x01\x01\x03\x11\x02\x03\x01\x01\x03\x12\x01\x03\x01\x01\x01\x14\x04\x01\x01\x02\x01\x15\x01\x05\x01\x02\x04\x16\x03\x01\x01\x01\x04\x17\x06\x03\x01\x01\x06\x18\x07\x01\x01\x01\x06\x19\x08\t\x01\x01\x06\x1a\n\x0b\x01\x01\x06\x1b\x01\x0c\x01\x01\x06\x1c\r\x06\x01\x01\x06\x1d\x0e\x01\x01\x01\x05\x1e\x01\x06\x00\x02\x1f\t\x0f\x01\x01\x00 \x10\x11\x00\x00!\x06\x01\x00\x00"\x06\x06\x00\x00#\x12\x06\x00\x00$\x13\x01\x00\x00%\x14\x01\x00\x00&\x15\x06\x00\x00\x19\x16\x01\x01\x01\x00\'\x06\x06\x00\x00(\x12\x06\x00\x00)\x17\x01\x00\x00*\x06\x06\x00\x00+\x01\x18\x00\x00,\x19\x06\x00\x00\x10\x1a\x01\x00\x00-\x1b\x01\x00\x00.\x06\x01\x01\x01\x00/\x06\x06\x00\x000\x06\x01\x01\x01\x001\x18\x01\x00\x002\x1c\x13\x00\x003\x1d\x01\x00\x004\x1e\x01\x02\x01\x01\x005\x1f\x01\x00\x006\x16\x01\x01\x01\x007\x17\x01\x00\x008\x11\x06\x00\x009\x11\x06\x00\x00: \x01\x00\x00;\x11\x06\x00\x00<\x14\x01\x00\x00=\x0f\x01\x00\x00>\x16\x01\x01\x01\x00?\x17\x01\x00\x00@\x1e\x06\x01\x01\x00A\x16\x01\x01\x01\x00B\x14\x01\x00\x00C\x17\x01\x00\x00D\x06\x01\x00\x00E\x06\x01\x00\x00F\x06\x01\x00\x00G\x01\x01\x00\x00H\x01\x01\x00\x00I!\x13\x00\x00J\x01\x06\x00\x00K\x06\x06\x00\x00L\x06\x06\x00\x00M \x01\x00\x00N"\x01\x00\x00O\x06\x01\x01\x01\x00P\x11\x01\x00\x00Q\x06\x01\x01\x01\x00R\x11\x01\x00\x00S#\x06\x00\x00\x11\x11\x13\x00\x00T\x14\x13\x00\x00\x12\x06\x13\x00\x08%\t%\x0b\x13\x08\x13\x08-\t-\x0e\x06\x07/\n/\x0b%\n\x0f\x0c%\x0e\x18\t\x13\x034\x06+\x00+\x01+\x05+\x0c\x13\x0c-\n\x13\n-\x044\nC\n\x06\n%\x02+\x02\x07\x0b\t\x01\t\x00\x0b\t\x01\t\x00\x00\x02\x07\x0b\t\x01\t\x00\x03\x01\x0b\t\x01\t\x00\x02\x07\x0b\n\x01\t\x00\t\x00\x01\x0b\n\x01\t\x00\x01\x03\x02\x07\n\t\x00\n\t\x00\x02\x06\n\t\x00\x03\x01\x06\t\x00\x02\x07\n\t\x00\x03\x01\x07\t\x00\x01\n\t\x00\x01\x06\n\t\x00\x02\x07\n\t\x00\t\x00\x01\n\x02\x04\x05\x03\x03\x03\x02\x03\x03\x02\x03\x05\x01\x08\x03\x03\x03\x05\x03\x04\x03\x03\x03\x03\x02\x03\n\x02\x03\x03\x03\n\x02\x01\x05\x04\x05\x05\x03\n\x02\x02\x05\x08\x03\x03\x03\n\x02\n\x02\x02\x08\x03\x08\x03\x02\x07\x08\x03\x08\x03\x03\x05\x03\n\x02\x05\x03\x05\x03\x03\n\x02\x04\x03\x05\x03\n\x02\x02\x07\x08\x03\x03\x04\x03\x05\x05\x03\x01\x06\x08\x03\t\x03\x03\x03\x03\x03\x03\x03\x06\x08\x04\x06\x08\x05\x01\x08\x04\x07\x03\x03\x03\x03\x03\x07\x08\x04\x07\x08\x05\x03\x06\x08\x03\x03\x06\x08\x06\x04\x03\x07\x08\x04\x03\x07\x08\x05\x03\x08\x03\x07\x08\x04\x07\x08\x05\x01\x06\x0b\x01\x01\t\x00\x01\t\x00\x04\x06\x08\x00\x06\x08\x04\x06\x08\x05\x06\x08\x06\x01\x08\x00\x0b\x03\x07\x08\x00\x05\x03\x03\x07\x08\x04\x01\x03\x07\x08\x05\x07\x08\x06\n\x02\x01\x02\x07\x03\x06\x08\x03\x06\x08\x04\x03\x06\x08\x05\x06\x08\x06\x03\x04\x03\x03\x07\x08\x05\n\x02\x04\x03\x07\x08\x03\x07\x08\x06\x03\x01\x07\x08\x07\x01\x08\x08\x03\x07\x0b\x01\x01\t\x00\x0b\t\x01\t\x00\n\x02\x06\x06\x08\x03\x06\x08\x04\x06\x08\x04\x03\x07\x08\x05\x06\x08\x06\x04\x07\x0b\x01\x01\t\x00\x08\x03\x0b\t\x01\t\x00\n\x02\x04\x03\x07\x08\x05\x07\x08\x06\x03\x06\x03\x03\x01\x03\x03\x03\x04\x03\x01\x03\x03\x02\x06\x0b\x01\x01\t\x00\x06\x0b\x01\x01\t\x01\x01\t\x01\x0f\x03\x03\x03\x03\x05\x03\x03\x01\x03\x01\x03\x01\x03\n\x02\x03\x02\x04\x04\x04\x08\x03\x07\x08\x04\x07\x08\x05\n\x02\x06\x04\x04\x04\x01\x03\x01\x03\x08\x03\x01\x03\x03\x05\x01\x03\x01\x08\x02\n\x03\x05\x03\x03\x07\x08\x04\x01\x03\x03\x07\x08\x05\n\x02\x02\x03\x07\x08\x05\x07\x03\x07\x08\x00\x07\x08\x04\x01\x03\x07\x08\x05\x07\x08\x06\x02\x01\x03\x04\x06\x08\x04\x01\x03\x07\x08\x05\x04\x06\x08\x04\x01\x03\x06\x08\x05\x03\x01\x03\x06\x08\x05\x01\x06\x08\x05\x02\x06\x08\x04\x06\x08\x05\x03\x07\x08\x04\x07\x08\x05\n\x02\x05\x07\x08\x04\x01\x03\x07\x08\x05\n\x02\x04\x07\x08\x03\x01\x03\x07\x08\x06\x0bViolasToken\x05Event\x03LCS\x05Libra\x0cLibraAccount\x0eLibraTimestamp\x06Vector\nBorrowInfo\nLibraToken\x05Order\x01T\tTokenInfo\x0eTokenInfoStore\x06Tokens\x08UserInfo\x0bViolasEvent\x07deposit\x08withdraw\x04zero\x0bEventHandle\nemit_event\x10new_event_handle\x11deposit_to_sender\x14withdraw_from_sender\x06append\x06borrow\nborrow_mut\x05empty\x06length\tpush_back\x10now_microseconds\x08to_bytes\x11account_liquidity\x0faccrue_interest\x07balance\nbalance_of\tbank_burn\tbank_mint\x11bank_token_2_base\x0eborrow_balance\x11borrow_balance_of\x0cborrow_index\x0bborrow_rate\x10contract_address\x0ccreate_token\x0bemit_events\nenter_bank\rexchange_rate\texit_bank\x12extend_user_tokens\x04join\x05join2\x10liquidate_borrow\x16liquidate_borrow_index\x04lock\nlock_index\x0cmantissa_div\x0cmantissa_mul\x04mint\x0cnew_mantissa\x0fpay_from_sender\x07publish\x06redeem\x0credeem_index\x14register_libra_token\x0crepay_borrow\x10repay_borrow_for\x12repay_borrow_index\x16require_first_tokenidx\rrequire_owner\rrequire_price\x11require_published\x12require_supervisor\x05split\x0btoken_count\x0btoken_price\x0ctotal_supply\x08transfer\rtransfer_from\x18update_collateral_factor\x1eupdate_collateral_factor_index\x0cupdate_price\x12update_price_index\x05value\rwithdraw_from\tprincipal\x0einterest_index\x04coin\x05index\x01t\x0epeer_token_idx\x11peer_token_amount\x05owner\x0etotal_reserves\rtotal_borrows\x05price\x0cprice_oracle\x11collateral_factor\x0blast_minute\x04data\x0ebulletin_first\tbulletins\nsupervisor\x06tokens\x02ts\x07borrows\rviolas_events\x06orders\x0forder_freeslots\x05debug\x05etype\x05parasrW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x10rW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x05\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02U\x03V\x03\x01\x02\x02W\x0b\t\x01\t\x00X\x03\x02\x02\x03Y\x08\x03Z\x03[\x03\x03\x02\x02X\x03S\x03\x04\x02\x0c\\\x05L\x03]\x03^\x03)\x03_\x03`\x05a\x03b\x03c\n\x02d\n\x02e\n\n\x02\x05\x02\x02f\x05g\n\x08\x04\x06\x02\x02h\n\x08\x03i\n\x08\x00\x07\x02\x05j\x0b\n\x01\x08\x08c\n\x02k\n\x08\x02l\n\x03m\n\x02\x08\x02\x03n\x03o\n\x02c\n\x02\x01+\x01<\x0f\x00\x02\x05\x06$h\x00\x11;\x0c\x08\x06\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x07\x06\x00\x00\x00\x00\x00\x00\x00\x00\x0c\n\x06\x00\x00\x00\x00\x00\x00\x00\x00\x0c\t\n\x07\n\x08!\x03\r\x00\x05\x0e\x00\x05e\x00\n\x07\x06\x01\x00\x00\x00\x00\x00\x00\x00\x16\n\x00\x11\x12\x0c\x04\n\x07\x11 \x0c\x06\n\x07\n\x00\x11\x18\x0c\x05\x11\x1b+\x05\x0c\x0c\x0b\x0c\x10\x00\n\x078\x00\x0c\x0b\n\n\n\x04\n\x06\n\x0b\x10\x01\x14\n\x0b\x10\x02\x14\x11\x15\x16\x0c\n\n\t\n\x05\n\x0b\x10\x02\x14\x11*\x16\x0c\t\n\x07\n\x01!\x03<\x00\x05^\x00\n\x02\x06\x00\x00\x00\x00\x00\x00\x00\x00$\x03A\x00\x05M\x00\n\t\n\x02\n\x06\n\x0b\x10\x01\x14\n\x0b\x10\x02\x14\x11\x15\x16\x0c\t\n\x03\x06\x00\x00\x00\x00\x00\x00\x00\x00$\x03R\x00\x05[\x00\n\t\n\x03\x0b\x0b\x10\x02\x14\x11*\x16\x0c\t\x05]\x00\x0b\x0b\x01\x05`\x00\x0b\x0b\x01\n\x07\x06\x02\x00\x00\x00\x00\x00\x00\x00\x16\x0c\x07\x05\x08\x00\n\n\n\t\x02\x10\x00\x02\x05\x06&J\x00\n\x00\x11\x1a\x0c\x01\x11\x1b*\x05\x0c\x07\x0b\x07\x0f\x00\n\x008\x01\x0c\x06\x11\r\x06<\x00\x00\x00\x00\x00\x00\x00\x06\xe8\x03\x00\x00\x00\x00\x00\x00\x18\x06\xe8\x03\x00\x00\x00\x00\x00\x00\x18\x1a\x0c\x04\n\x04\n\x06\x10\x03\x14\x17\x0c\x02\n\x01\n\x02\x18\x0c\x01\n\x04\n\x06\x0f\x03\x15\n\x06\x10\x04\x14\n\x01\x11*\x0c\x03\n\x06\x10\x04\x14\n\x03\x16\n\x06\x0f\x04\x15\x06\x01\x00\x00\x00\x00\x00\x00\x00\x06\x14\x00\x00\x00\x00\x00\x00\x00\x11,\x0c\x05\n\x06\x10\x05\x14\n\x03\n\x05\x11*\x16\n\x06\x0f\x05\x15\n\x06\x10\x06\x14\n\x06\x10\x06\x14\n\x01\x11*\x16\x0b\x06\x0f\x06\x15\x02\x11\x01\x01\x06\x01\x04\x00\n\x00(\x11\x12\x02\x12\x01\x01\x06\'\x1a\x00\n\x01+\x06\x0c\x04\n\x00\n\x04\x10\x078\x02#\x03\n\x00\x05\x14\x00\x0b\x04\x10\x07\n\x008\x03\x0c\x02\x0b\x02\x10\x08\x14\x0c\x03\x05\x18\x00\x0b\x04\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\x0b\x03\x02\x13\x00\x01\x05(\x15\x00\x0b\x00\x13\x03\x0c\x01\x0c\x03\x11\x1b*\x05\x0c\x04\x0b\x04\x0f\x00\n\x038\x01\x0c\x02\n\x02\x10\t\x14\n\x01\x17\x0b\x02\x0f\t\x15\x02\x14\x00\x02\x05\x06)\x18\x00\n\x00\n\x02\x12\x03\x0c\x03\n\x01\x0b\x03\x11\x1d\x11\x1b*\x05\x0c\x05\x0b\x05\x0f\x00\n\x008\x01\x0c\x04\n\x04\x10\t\x14\n\x02\x16\x0b\x04\x0f\t\x15\x02\x15\x00\x00\x06\x0e\x00\n\x00\n\x01\x11*\x0c\x04\n\x04\n\x02\x11*\x0c\x04\n\x04\n\x03\x11*\x0c\x04\n\x04\x02\x16\x01\x04\x01\x05\x06\x07*\n\x00\x11\x1b=\x00\x0c\x02\x0b\x027\x00\x14\n\x00\x0b\x01\x11\x19\x02\x17\x00\x02\x05\x06\x01\x04\x00\n\x00(\x11\x18\x02\x18\x00\x02\x05\x06,\x1c\x00\n\x01+\x06\x0c\x05\x0b\x05\x10\x0b\n\x008\x04\x0c\x02\x11\x1b+\x05\x0c\x04\x0b\x04\x10\x00\n\x008\x00\x0c\x03\n\x02\x10\x0c\x14\x0b\x03\x10\x06\x14\x11*\x0b\x02\x10\r\x14\x11)\x02\x19\x01\x03\x05\x06\x07.W\x00\x118\n\x00\x115\n\x00\x117(\x11"(\x0c\x05\n\x00\x11\x10\n\x05\n\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\n\x01\x11\x0f\x0c\x06\x0c\x07\n\x07\n\x06&\x0c\t\x0b\t\x03\x19\x00\x05\x1a\x00\x05\x1c\x00\x06v\x00\x00\x00\x00\x00\x00\x00\'\n\x00\x11\x17\x0c\x03(*\x06\x0c\x0c\x0b\x0c\x0f\x0b\n\x008\x05\x0c\x04\x11\x1b*\x05\x0c\x0b\x0b\x0b\x0f\x00\n\x008\x01\x0c\x08\n\x08\x10\x04\x14\n\x01\x16\n\x08\x0f\x04\x15\n\x03\n\x01\x16\n\x04\x0f\x0c\x15\x0b\x08\x10\x06\x14\x0b\x04\x0f\r\x15\n\x00\x11\x1b\n\x05\n\x01\x11?\x0e\x008\x06\x0c\r\r\r\x0e\x018\x068\x07\r\r\x0b\x028\x07\x06\t\x00\x00\x00\x00\x00\x00\x00\x0b\r8\x08\x11\x1e\x02\x1a\x00\x02\x05\x060D\x00\x11\x1b+\x06\x0c\x06\x0b\x06\x10\x07\n\x008\x03\x0c\x02\x11\x1b+\x05\x0c\x05\x0b\x05\x10\x00\n\x008\x00\x0c\x03\n\x02\x10\x08\x14\n\x03\x10\x05\x14%\x03\x19\x00\x05"\x00\x0b\x03\x01\x0b\x02\x01\x06\x01\x00\x00\x00\x00\x00\x00\x00\x06\x01\x00\x00\x00\x00\x00\x00\x00\x11,\x0c\x04\x052\x00\n\x03\x10\x04\x14\x0b\x02\x10\x08\x14\n\x03\x10\x04\x14\x16\x0b\x03\x10\x05\x14\x17\x11,\x0c\x04\x0b\x04\x0c\x07\x06\x05\x00\x00\x00\x00\x00\x00\x00\x06d\x00\x00\x00\x00\x00\x00\x00\x06<\x00\x00\x00\x00\x00\x00\x00\x18\x06\x18\x00\x00\x00\x00\x00\x00\x00\x18\x06m\x01\x00\x00\x00\x00\x00\x00\x18\x11,\x0c\x01\n\x01\n\x01\n\x07\x11*\x16\x02\x1b\x00\x00\x01\x02\x00\x07\x00\x02\x1c\x01\x03\x05\x06\x071J\x00\x118\x119\x11\x1b*\x05\x0c\x06\n\x06\x10\x008\t\x0c\x04\x06\x01\x00\x00\x00\x00\x00\x00\x00\x06\x01\x00\x00\x00\x00\x00\x00\x00\x11,\x0c\x05\n\x06\x0f\x00\n\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\n\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\n\x01\n\x02\x11\r\x06<\x00\x00\x00\x00\x00\x00\x00\x06\xe8\x03\x00\x00\x00\x00\x00\x00\x18\x06\xe8\x03\x00\x00\x00\x00\x00\x00\x18\x1a\x0e\x03\x148\x088\n\x12\x048\x0b\x0b\x06\x0f\x00\x07\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\n\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\n\x01\n\x02\x11\r\x06<\x00\x00\x00\x00\x00\x00\x00\x06\xe8\x03\x00\x00\x00\x00\x00\x00\x18\x06\xe8\x03\x00\x00\x00\x00\x00\x00\x18\x1a\x0e\x03\x148\x088\n\x12\x048\x0b\x11\x1b\x11"\x0e\x008\x0c\x0c\x07\r\x07\x0b\x038\x07\x06\x01\x00\x00\x00\x00\x00\x00\x00\x0b\x07\x0e\x048\x06\x11\x1e\n\x04\x02\x1d\x00\x02\x05\x062\x17\x00\n\x00\x11"\x0b\x01\x13\x03\x0c\x05\x0c\x02\n\x00*\x06\x0c\x04\x0b\x04\x0f\x07\n\x028\r\x0c\x03\n\x03\x10\x08\x14\n\x05\x16\x0b\x03\x0f\x08\x15\x02\x1e\x00\x01\x073\x0b\x00(*\x07\x0c\x03\x0b\x03\x0f\x0e\n\x00\x0b\x01\x0b\x02\x12\x088\x0e\x02\x1f\x01\x04\x01\x05\x06\x075\x1d\x00\n\x008\x0f\x0c\x02\x11\x1b<\x00\x0c\x01\n\x016\x01\x0b\x028\x10\n\x017\x00\x14(\n\x00\x11\x14\x0b\x017\x008\x06\x0c\x03\r\x03\x0e\x008\x068\x07\x06\r\x00\x00\x00\x00\x00\x00\x00\x0b\x038\x08\x11\x1e\x02 \x00\x02\x05\x066;\x00\x11\x1b+\x06\x0c\x06\x0b\x06\x10\x07\n\x008\x03\x0c\x01\x11\x1b*\x05\x0c\x05\n\x05\x10\x00\n\x008\x00\x0c\x02\x0b\x05\x10\x00\n\x00\x06\x01\x00\x00\x00\x00\x00\x00\x00\x168\x00\x0c\x03\n\x03\x10\t\x14\x06\x00\x00\x00\x00\x00\x00\x00\x00!\x03\x1e\x00\x05)\x00\x0b\x03\x01\x0b\x02\x01\x0b\x01\x01\x06\x01\x00\x00\x00\x00\x00\x00\x00\x06d\x00\x00\x00\x00\x00\x00\x00\x11,\x0c\x04\x059\x00\x0b\x01\x10\x08\x14\n\x02\x10\x04\x14\x16\x0b\x02\x10\x05\x14\x17\x0b\x03\x10\t\x14\x11,\x0c\x04\x0b\x04\x02!\x01\x04\x01\x05\x06\x077\x1f\x00\x11\x1b<\x00\x0c\x01\n\x016\x01\n\x008\x11\x0c\x03\x0b\x038\x12\n\x017\x00\x14\n\x00\x11E\x0c\x02\x0b\x02\x11\x13\x0b\x017\x008\x06\x0c\x04\r\x04\x0e\x008\x068\x07\x06\x0e\x00\x00\x00\x00\x00\x00\x00\x0b\x048\x08\x11\x1e\x02"\x00\x02\x05\x068*\x00\x11\x1b*\x05\x0c\x02\x0b\x02\x10\x008\t\x0c\x01\n\x00*\x06\x0c\x03\n\x03\x10\x078\x02\x0c\x04\n\x04\n\x01&\x03\x13\x00\x05\x16\x00\x0b\x03\x01\x05)\x00\n\x03\x0f\x07\n\x04\x06\x00\x00\x00\x00\x00\x00\x00\x00\x12\x038\x13\n\x03\x0f\x0b\x06\x00\x00\x00\x00\x00\x00\x00\x00\x06\x01\x00\x00\x00\x00\x00\x00\x00\x06\x01\x00\x00\x00\x00\x00\x00\x00\x11,\x12\x008\x14\n\x04\x06\x01\x00\x00\x00\x00\x00\x00\x00\x16\x0c\x04\x05\x0e\x00\x02#\x01\x009\x18\x00\x0b\x00\x13\x03\x0c\x06\x0c\x02\x0b\x01\x13\x03\x0c\x07\x0c\x03\n\x02\n\x03!\x0c\x04\x0b\x04\x03\x0f\x00\x05\x10\x00\x05\x12\x00\x06l\x00\x00\x00\x00\x00\x00\x00\'\n\x02\n\x06\n\x07\x16\x12\x03\x02$\x01\x00:\x1b\x00\x0b\x01\x13\x03\x0c\x05\x0c\x02\n\x00\x10\x10\x14\n\x02!\x0c\x03\x0b\x03\x03\r\x00\x05\x0e\x00\x05\x12\x00\x0b\x00\x01\x06m\x00\x00\x00\x00\x00\x00\x00\'\n\x00\x10\x08\x14\n\x05\x16\x0b\x00\x0f\x08\x15\x02%\x01\x04\x01\x05\x06\x07;\x11\x00\x11\x1b=\x00\x0c\x03\x11\x1b=\x01\x0c\x04\x0b\x037\x00\x14\n\x00\n\x01\x0b\x047\x02\x14\x0b\x02\x11&\x02&\x01\x03\x05\x06\x07=\x82\x00\x118\n\x00\x115\n\x03\x115\n\x00\x117\n\x03\x117(\x11"\n\x01\x11"\n\x00\x11\x10\n\x01\x06\x9f\x86\x01\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x11\x0f\x0c\n\x0c\x0b\n\x0b\n\n#\x0c\x0c\x0b\x0c\x03\x1d\x00\x05\x1e\x00\x05 \x00\x06x\x00\x00\x00\x00\x00\x00\x00\'\n\x00\n\x01\x11\x18\x0c\x06\n\x02\n\x06%\x0c\x0e\x0b\x0e\x03+\x00\x05,\x00\x05.\x00\x06y\x00\x00\x00\x00\x00\x00\x00\'\n\x02\x06\x00\x00\x00\x00\x00\x00\x00\x00!\x033\x00\x055\x00\n\x06\x0c\x02\n\x00\x11<\x0c\x07\n\x03\x11<\x0c\x08\n\x02\n\x07\x11*\x0c\x05\n\x05\n\n\n\x0b\x17%\x0c\x10\x0b\x10\x03H\x00\x05I\x00\x05K\x00\x06z\x00\x00\x00\x00\x00\x00\x00\'\n\x00\n\x01\n\x02\x113\n\x02\n\x07\x11*\x0c\x13\n\x13\n\x03\x11 \x11)\x0c\x13\n\x13\n\x08\x11)\x0c\x13\n\x13\n\x13\x06\x01\x00\x00\x00\x00\x00\x00\x00\x06\n\x00\x00\x00\x00\x00\x00\x00\x11,\x11*\x16\x0c\x13\n\x03\x06\x01\x00\x00\x00\x00\x00\x00\x00\x16\n\x01(\n\x13\x11?\x0e\x008\x06\x0c\x12\r\x12\x0e\x018\x0c8\x07\r\x12\x0e\x028\x068\x07\r\x12\x0e\x038\x068\x07\r\x12\x0b\x048\x07\x06\x0b\x00\x00\x00\x00\x00\x00\x00\x0b\x128\x08\x11\x1e\x02\'\x01\x04\x01\x05\x06\x07*\n\x00\x11\x1b=\x00\x0c\x02\x0b\x027\x00\x14\n\x00\x0b\x01\x11(\x02(\x01\x03\x05\x06\x07 )\x00\x118\n\x00\x115\n\x00\x117(\x11"\n\x00\x11\x10\n\x00\x11 \x0c\x03\n\x00\x11\x1b\n\x01\x11-\n\x01\n\x03\x11)\x0c\x05\n\x00\x06\x01\x00\x00\x00\x00\x00\x00\x00\x16(\n\x05\x11\x14\x0e\x008\x06\x0c\x06\r\x06\x0e\x018\x068\x07\r\x06\x0b\x028\x07\x06\x07\x00\x00\x00\x00\x00\x00\x00\x0b\x068\x08\x11\x1e\x02)\x00\x00>\r\x00\n\x0051 /\x0c\x02\n\x02\n\x015\x1a\x0c\x03\n\x034\x02*\x00\x00>\r\x00\n\x005\n\x015\x18\x0c\x02\n\x021 0\x0c\x03\n\x034\x02+\x01\x03\x05\x06\x07?3\x00\x118\n\x00\x115\n\x00\x116(\x11"\n\x01\x11"\n\x00\n\x02\x12\x03\x0c\x04\n\x01\x0b\x04\x11\x1d\x11\x1b*\x05\x0c\x06\x0b\x06\x0f\x00\n\x008\x01\x0c\x05\n\x05\x10\t\x14\n\x02\x16\x0b\x05\x0f\t\x15\x0e\x008\x06\x0c\x07\r\x07\x0e\x018\x0c8\x07\r\x07\x0e\x028\x068\x07\r\x07\x0b\x038\x07\x06\x02\x00\x00\x00\x00\x00\x00\x00\x0b\x078\x08\x11\x1e\x02,\x00\x00@%\x00\n\x0051@/\x0c\x02\n\x0151 /\x0c\x03\n\x02\n\x03\x1a\x0c\x04\n\x042\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"\x03\x13\x00\x05\x16\x00\x08\x0c\x07\x05\x1a\x00\n\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00!\x0c\x07\x0b\x07\x0c\x05\x0b\x05\x03\x1f\x00\x05 \x00\x05"\x00\x06e\x00\x00\x00\x00\x00\x00\x00\'\n\x044\x02-\x00\x02\x05\x06A\x12\x00(\n\x01"\x0c\x04\x0b\x04\x03\x07\x00\x05\x08\x00\x05\n\x00\x06p\x00\x00\x00\x00\x00\x00\x00\'\n\x00\n\x02\x11E\x0c\x03\n\x01\x0b\x03\x11\x1d\x02.\x01\x03\x05\x06\x07B(\x00(\x0c\x01\n\x01)\x06 \x0c\x02\x0b\x02\x03\t\x00\x05\n\x00\x05\x0c\x00\x06q\x00\x00\x00\x00\x00\x00\x00\'8\x158\x16\x12\x06-\x068\x17\x0e\x00\x148\x188\x198\x08\x12\x07-\x07\n\x01\x11\x1b!\x03\x1d\x00\x05!\x00\x11\x1b8\x1a\x12\x05-\x05(\x11"\x06\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x008\x08\x11\x1e\x02/\x01\x04\x01\x05\x06\x07*\n\x00\x11\x1b=\x00\x0c\x02\x0b\x027\x00\x14\n\x00\x0b\x01\x110\x020\x01\x03\x05\x06\x07D_\x00\x118\n\x00\x115\n\x00\x117(\x11"(\x0c\x04\n\x00\x11\x10\n\x00\x11 \x0c\x03\n\x01\n\x03\x11)\x0c\n\n\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00!\x03\x17\x00\x05 \x00\n\x00\x06\x01\x00\x00\x00\x00\x00\x00\x00\x16\x11\x11\x0c\n\n\n\n\x03\x11*\x0c\x01\n\x04\n\x00\n\n\x06\x00\x00\x00\x00\x00\x00\x00\x00\x11\x0f\x0c\x05\x0c\x06\n\x06\n\x05&\x0c\x08\x0b\x08\x03.\x00\x05/\x00\x051\x00\x06u\x00\x00\x00\x00\x00\x00\x00\'\n\x00\x06\x01\x00\x00\x00\x00\x00\x00\x00\x16\n\n\x11E\x13\x03\x01\x01\x11\x1b*\x05\x0c\x0b\x0b\x0b\x0f\x00\n\x00\x06\x01\x00\x00\x00\x00\x00\x00\x00\x168\x01\x0c\x07\n\x07\x10\t\x14\n\n\x17\x0b\x07\x0f\t\x15\n\x00\x11\x1b\n\x04\n\x01\x11?\x0e\x008\x06\x0c\x0c\r\x0c\x0e\x018\x068\x07\r\x0c\x0b\x028\x07\x06\x08\x00\x00\x00\x00\x00\x00\x00\x0b\x0c8\x08\x11\x1e\x021\x01\x03\x05\x06\x07E\x13\x00\x118\x119\x11\x1b*\x05\x0c\x04\x0b\x04\x10\x008\t\x0c\x038\x1b\n\x039\x00?\x00\x07\x01\n\x00\n\x01\x0b\x02\x11\x1c\x022\x01\x04\x01\x05\x06\x07*\n\x00\x11\x1b=\x00\x0c\x02\x0b\x027\x00\x14\n\x00\x0b\x01\x114\x023\x00\x02\x05\x06F>\x00\n\x00\n\x01\x11\x18\x0c\x03\n\x02\n\x03%\x0c\x06\x0b\x06\x03\x0b\x00\x05\x0c\x00\x05\x0e\x00\x06w\x00\x00\x00\x00\x00\x00\x00\'\n\x02\x06\x00\x00\x00\x00\x00\x00\x00\x00!\x03\x13\x00\x05\x15\x00\n\x03\x0c\x02\x11\x1b*\x05\x0c\x08\x0b\x08\x0f\x00\n\x008\x01\x0c\x05\n\x05\x10\x04\x14\n\x02\x17\n\x05\x0f\x04\x15\n\x01*\x06\x0c\t\x0b\t\x0f\x0b\n\x008\x05\x0c\x04\n\x03\n\x02\x17\n\x04\x0f\x0c\x15\x0b\x05\x10\x06\x14\x0b\x04\x0f\r\x15\n\x00\x11\x1b\n\x02\x11-\x024\x01\x03\x05\x06\x07\x0f\x1c\x00\x118\n\x00\x115\n\x00\x117(\x11"\n\x00\x11\x10\n\x00(\n\x01\x113\x0e\x008\x06\x0c\x03\r\x03\x0e\x018\x068\x07\r\x03\x0b\x028\x07\x06\n\x00\x00\x00\x00\x00\x00\x00\x0b\x038\x08\x11\x1e\x025\x00\x00G\r\x00\n\x00\x06\x02\x00\x00\x00\x00\x00\x00\x00\x19\x06\x00\x00\x00\x00\x00\x00\x00\x00!\x0c\x01\x0b\x01\x03\t\x00\x05\n\x00\x05\x0c\x00\x06i\x00\x00\x00\x00\x00\x00\x00\'\x026\x00\x01\x05H\x15\x00\x11\x1b*\x05\x0c\x04\x0b\x04\x10\x00\n\x008\x00\x0c\x01\x0b\x01\x10\x11\x14(!\x0c\x02\x0b\x02\x03\x11\x00\x05\x12\x00\x05\x14\x00\x06h\x00\x00\x00\x00\x00\x00\x00\'\x027\x00\x01\x05I\x15\x00\x11\x1b+\x05\x0c\x04\x0b\x04\x10\x00\n\x008\x00\x0c\x01\x0b\x01\x10\x02\x14\x06\x00\x00\x00\x00\x00\x00\x00\x00"\x0c\x02\x0b\x02\x03\x11\x00\x05\x12\x00\x05\x14\x00\x06k\x00\x00\x00\x00\x00\x00\x00\'\x028\x00\x00G\n\x00()\x06\x0c\x00\x0b\x00\x03\x06\x00\x05\x07\x00\x05\t\x00\x06f\x00\x00\x00\x00\x00\x00\x00\'\x029\x00\x01\x05J\x10\x00\x11\x1b+\x05\x0c\x02(\x0b\x02\x10\x12\x14!\x0c\x00\x0b\x00\x03\x0c\x00\x05\r\x00\x05\x0f\x00\x06g\x00\x00\x00\x00\x00\x00\x00\'\x02:\x01\x00G\x1c\x00\n\x00\x10\x08\x14\n\x01&\x0c\x02\x0b\x02\x03\t\x00\x05\n\x00\x05\x0e\x00\x0b\x00\x01\x06n\x00\x00\x00\x00\x00\x00\x00\'\n\x00\x10\x08\x14\n\x01\x17\n\x00\x0f\x08\x15\x0b\x00\x10\x10\x14\n\x01\x12\x03\x02;\x01\x01\x05K\x07\x00\x11\x1b+\x05\x0c\x00\x0b\x00\x10\x008\t\x02<\x00\x01\x05L\x0c\x00\x11\x1b+\x05\x0c\x02\x0b\x02\x10\x00\n\x008\x00\x0c\x01\x0b\x01\x10\x02\x14\x02=\x01\x01\x05L\x0c\x00\x11\x1b+\x05\x0c\x02\x0b\x02\x10\x00\n\x008\x00\x0c\x01\x0b\x01\x10\t\x14\x02>\x01\x03\x05\x06\x07\x0f\x1e\x00\x118\n\x00\x115(\x11"\n\x01\x11"\n\x00\n\x01\n\x02\x11-\x0e\x008\x06\x0c\x04\r\x04\x0e\x018\x0c8\x07\r\x04\x0e\x028\x068\x07\r\x04\x0b\x038\x07\x06\x03\x00\x00\x00\x00\x00\x00\x00\x0b\x048\x08\x11\x1e\x02?\x00\x02\x05\x06A\x13\x00\n\x01\n\x02"\x0c\x05\x0b\x05\x03\x07\x00\x05\x08\x00\x05\n\x00\x06r\x00\x00\x00\x00\x00\x00\x00\'\n\x00\n\x01\n\x03\x11F\x0c\x04\n\x02\x0b\x04\x11\x1d\x02@\x01\x03\x01\x05\x07*\t\x00\x11\x1b=\x00\x0c\x01\x0b\x017\x00\x14\n\x00\x11A\x02A\x01\x02\x05\x07M\x1c\x00\x118\n\x00\x115\x119\x11\x1b*\x05\x0c\x03\x0b\x03\x0f\x00\n\x008\x01\x0c\x02\n\x01\x0b\x02\x0f\x01\x15\x0e\x008\x06\x0c\x04\r\x04\x0e\x018\x068\x07\x06\x0c\x00\x00\x00\x00\x00\x00\x00\x0b\x048\x08\x11\x1e\x02B\x01\x03\x01\x05\x07*\t\x00\x11\x1b=\x00\x0c\x01\x0b\x017\x00\x14\n\x00\x11C\x02C\x01\x02\x05\x07N)\x00\x118\n\x00\x115\x11\x1b*\x05\x0c\x05\x0b\x05\x0f\x00\n\x008\x01\x0c\x02\n\x02\x10\x13\x14(!\x0c\x03\x0b\x03\x03\x14\x00\x05\x15\x00\x05\x19\x00\x0b\x02\x01\x06t\x00\x00\x00\x00\x00\x00\x00\'\n\x01\x0b\x02\x0f\x02\x15\x0e\x008\x06\x0c\x06\r\x06\x0e\x018\x068\x07\x06\x06\x00\x00\x00\x00\x00\x00\x00\x0b\x068\x08\x11\x1e\x02D\x01\x00\x01\x04\x00\x0b\x00\x10\x08\x14\x02E\x00\x01\x06\x01\x05\x00\n\x00(\n\x01\x11F\x02F\x00\x01\x06O"\x00\n\x01*\x06\x0c\x06\x0b\x06\x0f\x07\n\x008\r\x0c\x03\n\x03\x10\x08\x14\n\x02&\x0c\x04\x0b\x04\x03\x11\x00\x05\x12\x00\x05\x16\x00\x0b\x03\x01\x06o\x00\x00\x00\x00\x00\x00\x00\'\n\x03\x10\x08\x14\n\x02\x17\x0b\x03\x0f\x08\x15\n\x00\n\x02\x12\x03\x02G\x01\x00\x01\x04\x00\n\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x12\x03\x02\x05\x01\x04\x07\x04\x05\x04\x08\x04\x03\x04\x02\x04\x04\x06\x00\x03\x01\x04\x01\x01\x01\x06\x01\x00\x00\x00\x01\x07\x00\x01\x00\x03\x00\x04\x00\x05\x00\x04\x06\n+\x0f+\n<',
    "borrow": b'\xa1\x1c\xeb\x0b\x01\x00\x07\x01F\x00\x00\x00\x02\x00\x00\x00\x03H\x00\x00\x00\x06\x00\x00\x00\x04N\x00\x00\x00\x02\x00\x00\x00\x05P\x00\x00\x00\x08\x00\x00\x00\x07X\x00\x00\x00\x13\x00\x00\x00\x08k\x00\x00\x00\x10\x00\x00\x00\t{\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x02\x03\n\x02\x00\x01\t\x00\x0bViolasToken\x06borrowrW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x01\x01\x00\x01\x04\x00\n\x00\x0b\x018\x00\x02',
    "enter_bank": b'\xa1\x1c\xeb\x0b\x01\x00\x07\x01F\x00\x00\x00\x02\x00\x00\x00\x03H\x00\x00\x00\x06\x00\x00\x00\x04N\x00\x00\x00\x02\x00\x00\x00\x05P\x00\x00\x00\x06\x00\x00\x00\x07V\x00\x00\x00\x17\x00\x00\x00\x08m\x00\x00\x00\x10\x00\x00\x00\t}\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x01\x03\x00\x01\t\x00\x0bViolasToken\nenter_bankrW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x01\x01\x00\x01\x03\x00\n\x008\x00\x02',
    "exit_bank": b'\xa1\x1c\xeb\x0b\x01\x00\x07\x01F\x00\x00\x00\x02\x00\x00\x00\x03H\x00\x00\x00\x06\x00\x00\x00\x04N\x00\x00\x00\x02\x00\x00\x00\x05P\x00\x00\x00\x06\x00\x00\x00\x07V\x00\x00\x00\x16\x00\x00\x00\x08l\x00\x00\x00\x10\x00\x00\x00\t|\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x01\x03\x00\x01\t\x00\x0bViolasToken\texit_bankrW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x01\x01\x00\x01\x03\x00\n\x008\x00\x02',
    "liquidate_borrow": b'\xa1\x1c\xeb\x0b\x01\x00\x07\x01F\x00\x00\x00\x02\x00\x00\x00\x03H\x00\x00\x00\x07\x00\x00\x00\x04O\x00\x00\x00\x02\x00\x00\x00\x05Q\x00\x00\x00\x0b\x00\x00\x00\x07\\\x00\x00\x00\x1d\x00\x00\x00\x08y\x00\x00\x00\x10\x00\x00\x00\t\x89\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x01\x00\x01\x02\x01\x01\x00\x02\x03\x05\x03\n\x02\x00\x02\t\x00\t\x01\x0bViolasToken\x10liquidate_borrowrW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x02\x01\x01\x00\x01\x05\x00\n\x00\n\x01\x0b\x028\x00\x02',
    "lock": b'\xa1\x1c\xeb\x0b\x01\x00\x07\x01F\x00\x00\x00\x02\x00\x00\x00\x03H\x00\x00\x00\x06\x00\x00\x00\x04N\x00\x00\x00\x02\x00\x00\x00\x05P\x00\x00\x00\x08\x00\x00\x00\x07X\x00\x00\x00\x11\x00\x00\x00\x08i\x00\x00\x00\x10\x00\x00\x00\ty\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x02\x03\n\x02\x00\x01\t\x00\x0bViolasToken\x04lockrW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x01\x01\x00\x01\x04\x00\n\x00\x0b\x018\x00\x02',
    "publish": b'\xa1\x1c\xeb\x0b\x01\x00\x06\x01=\x00\x00\x00\x02\x00\x00\x00\x03?\x00\x00\x00\x05\x00\x00\x00\x05D\x00\x00\x00\x04\x00\x00\x00\x07H\x00\x00\x00\x14\x00\x00\x00\x08\\\x00\x00\x00\x10\x00\x00\x00\tl\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\n\x02\x00\x0bViolasToken\x07publishrW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x00\x00\x01\x03\x00\x0b\x00\x11\x00\x02',
    "redeem": b'\xa1\x1c\xeb\x0b\x01\x00\x07\x01F\x00\x00\x00\x02\x00\x00\x00\x03H\x00\x00\x00\x06\x00\x00\x00\x04N\x00\x00\x00\x02\x00\x00\x00\x05P\x00\x00\x00\x08\x00\x00\x00\x07X\x00\x00\x00\x13\x00\x00\x00\x08k\x00\x00\x00\x10\x00\x00\x00\t{\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x02\x03\n\x02\x00\x01\t\x00\x0bViolasToken\x06redeemrW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x01\x01\x00\x01\x04\x00\n\x00\x0b\x018\x00\x02',
    "register_libra_token": b'\xa1\x1c\xeb\x0b\x01\x00\x07\x01F\x00\x00\x00\x02\x00\x00\x00\x03H\x00\x00\x00\x06\x00\x00\x00\x04N\x00\x00\x00\x02\x00\x00\x00\x05P\x00\x00\x00\x0b\x00\x00\x00\x07[\x00\x00\x00!\x00\x00\x00\x08|\x00\x00\x00\x10\x00\x00\x00\t\x8c\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x03\x03\x05\x03\n\x02\x01\x03\x00\x01\t\x00\x0bViolasToken\x14register_libra_tokenrW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x01\x01\x00\x02\x06\x00\n\x00\n\x01\x0b\x028\x00\x01\x02',
    "repay_borrow": b'\xa1\x1c\xeb\x0b\x01\x00\x07\x01F\x00\x00\x00\x02\x00\x00\x00\x03H\x00\x00\x00\x06\x00\x00\x00\x04N\x00\x00\x00\x02\x00\x00\x00\x05P\x00\x00\x00\x08\x00\x00\x00\x07X\x00\x00\x00\x19\x00\x00\x00\x08q\x00\x00\x00\x10\x00\x00\x00\t\x81\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x02\x03\n\x02\x00\x01\t\x00\x0bViolasToken\x0crepay_borrowrW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x01\x01\x00\x01\x04\x00\n\x00\x0b\x018\x00\x02',
    "update_collateral_factor": b'\xa1\x1c\xeb\x0b\x01\x00\x07\x01F\x00\x00\x00\x02\x00\x00\x00\x03H\x00\x00\x00\x06\x00\x00\x00\x04N\x00\x00\x00\x02\x00\x00\x00\x05P\x00\x00\x00\x06\x00\x00\x00\x07V\x00\x00\x00%\x00\x00\x00\x08{\x00\x00\x00\x10\x00\x00\x00\t\x8b\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x01\x03\x00\x01\t\x00\x0bViolasToken\x18update_collateral_factorrW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x01\x01\x00\x01\x03\x00\n\x008\x00\x02',
    "update_price": b'\xa1\x1c\xeb\x0b\x01\x00\x07\x01F\x00\x00\x00\x02\x00\x00\x00\x03H\x00\x00\x00\x06\x00\x00\x00\x04N\x00\x00\x00\x02\x00\x00\x00\x05P\x00\x00\x00\x06\x00\x00\x00\x07V\x00\x00\x00\x19\x00\x00\x00\x08o\x00\x00\x00\x10\x00\x00\x00\t\x7f\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x01\x03\x00\x01\t\x00\x0bViolasToken\x0cupdate_pricerW\xc2A~M\x108\xe1\x81|\x8f(:\xce.\x01\x01\x00\x01\x03\x00\n\x008\x00\x02',
}

type_to_code_map = {
    CodeType.BANK: bytecodes["bank"],
    CodeType.BORROW: bytecodes["borrow"],
    CodeType.ENTER_BANK: bytecodes["enter_bank"],
    CodeType.EXIT_BANK: bytecodes["exit_bank"],
    CodeType.LIQUIDATE_BORROW: bytecodes["liquidate_borrow"],
    CodeType.LOCK: bytecodes["lock"],
    CodeType.PUBLISH: bytecodes["publish"],
    CodeType.REDEEM: bytecodes["redeem"],
    CodeType.REGISTER_TOKEN: bytecodes["register_libra_token"],
    CodeType.REPAY_BORROW: bytecodes["repay_borrow"],
    CodeType.UPDATE_COLLATERAL_FACTOR: bytecodes["update_collateral_factor"],
    CodeType.UPDATE_PRICE: bytecodes["update_price"],
}

code_to_type_map = { v:k for k, v in type_to_code_map.items()}

default_module_address = bytes.fromhex("7257c2417e4d1038e1817c8f283ace2e")

def get_code_type(code: bytes):
    if isinstance(code, str):
        code = bytes.fromhex(code)
    type = code_to_type_map.get(code)
    if type:
        return type
    return CodeType.UNKNOWN

def get_code(type, module_address=None):
    code = type_to_code_map.get(type)
    if code:
        if module_address:
            module_address = AccountAddress.normalize_to_bytes(module_address)
            code = code.replace(default_module_address, module_address)
        return code