from canoser import Struct
from lbrtypes.move_core.move_resource import MoveResource
from crypto.ed25519 import Ed25519PublicKey
from crypto.x25519 import PublicKey
from crypto.multi_ed25519 import Multiaddr

class ValidatorConfig(Struct):
    _fields = [
        ("consensus_pubkey", Ed25519PublicKey),
        ("validator_network_signing_pubkey", Ed25519PublicKey),
        ("validator_network_identity_pubkey", PublicKey),
        ("validator_network_address", Multiaddr),
        ("fullnodes_network_identity_pubkey", PublicKey),
        ("fullnodes_network_address", Multiaddr)
    ]

class ValidatorConfigResource(Struct, MoveResource):
    MODULE_NAME = "ValidatorConfig"
    STRUCT_NAME = "T"
    _fields = [
        ("validator_config", ValidatorConfig)
    ]