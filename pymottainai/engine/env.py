from enum import Enum
from .card import Card

HAND_SIZE = 5

ALL_CARDS = [
    Card(name="Poem", material=""),
    Card(name="Pinwheel", material=""),
    Card(name="Scroll", material=""),
    Card(name="Curtain", material=""),
    Card(name="Crane", material=""),
    Card(name="Fan", material=""),
    Card(name="Lampshade", material=""),
    Card(name="Plane", material=""),
    Card(name="Straw", material=""),
    Card(name="Deck of Cards", material=""),
    Card(name="Sketch", material=""),
    Card(name="Doll", material=""),

    Card(name="Statue", material=""),
    Card(name="Pillar", material=""),
    Card(name="Frog", material=""),
    Card(name="Tablet", material=""),
    Card(name="Stool", material=""),
    Card(name="Go Set", material=""),
    Card(name="Fountain", material=""),
    Card(name="Tower", material=""),
    Card(name="Daitoro", material=""),
    Card(name="Amulet", material=""),
    Card(name="Bench", material=""),

    Card(name="Kite", material=""),
    Card(name="Umbrella", material=""),
    Card(name="Socks", material=""),
    Card(name="Quilt", material=""),
    Card(name="Robe", material=""),
    Card(name="Flag", material=""),
    Card(name="Tapestry", material=""),
    Card(name="Handkerchief", material=""),
    Card(name="Puppet", material=""),
    Card(name="Mask", material=""),
    Card(name="Cloak", material=""),

    Card(name="Vase", material=""),
    Card(name="Haniwa", material=""),
    Card(name="Teapot", material=""),
    Card(name="Dice", material=""),
    Card(name="Bowl", material=""),
    Card(name="Jar", material=""),
    Card(name="Brick", material=""),
    Card(name="Figurine", material=""),
    Card(name="Bangle", material=""),
    Card(name="Cup", material=""),

    Card(name="Ring", material=""),
    Card(name="Flute", material=""),
    Card(name="Sword", material=""),
    Card(name="Shuriken", material=""),
    Card(name="Gong", material=""),
    Card(name="Pin", material=""),
    Card(name="Coin", material=""),
    Card(name="Turtle", material=""),
    Card(name="Bell", material=""),
    Card(name="Chopsticks", material=""),
]


class Phase(Enum):
    setup = 0
    morning = 1
    noon = 2
    night = 3
