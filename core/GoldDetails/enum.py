from enum import Enum

class JewelryType(str, Enum):
    RING = "ring"
    NECKLACE = "necklace"
    BRACELET = "bracelet"
    EARRING = "earring"
    CHAIN = "chain"

class GoldType(str, Enum):
    K_22 = "22K"  
    K_24 = "24K"  
    K_18 = "18K" 
    K_14 = "14K"  
    K_10 = "10K"  
