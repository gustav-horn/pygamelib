from colorama import Fore, Back, Style, init  # noqa: F401
import colorama.ansi
import subprocess

"""
The Graphics module hold many variables that aims at simplifying the use of
unicode characters in the game development process.

Explore this file for a complete list of characters, emojis and colored blocks.
All emoji codes from: https://unicode.org/emoji/charts/full-emoji-list.html

This modules defines a couple of colored squares and rectangles that displays
correctly in all terminals.

Colored rectangles:
 * WHITE_RECT
 * BLUE_RECT
 * RED_RECT
 * MAGENTA_RECT
 * GREEN_RECT
 * YELLOW_RECT
 * BLACK_RECT
 * CYAN_RECT

Then colored squares:
 * WHITE_SQUARE
 * MAGENTA_SQUARE
 * GREEN_SQUARE
 * RED_SQUARE
 * BLUE_SQUARE
 * YELLOW_SQUARE
 * BLACK_SQUARE
 * CYAN_SQUARE

And finally an example of composition of rectangles to make different colored squares:
 * RED_BLUE_SQUARE = RED_RECT+BLUE_RECT
 * YELLOW_CYAN_SQUARE = YELLOW_RECT+CYAN_RECT

The complete list of aliased emojis is:
    * COWBOY = \U0001F920
    * DEAMON_HAPPY = \U0001F608
    * DAEMON_ANGRY = \U0001F47F
    * SKULL = \U0001F480
    * SKULL_CROSSBONES = \U00002620
    * POO = \U0001F4A9
    * CLOWN = \U0001F921
    * OGRE = \U0001F479
    * HAPPY_GHOST = \U0001F47B
    * ALIEN = \U0001F47D
    * ALIEN_MONSTER = \U0001F47E
    * ROBOT = \U0001F916
    * CAT = \U0001F408
    * CAT_FACE = \U0001F63A
    * CAT_LOVE = \U0001F63B
    * CAT_WEARY = \U0001F640
    * CAT_CRY = \U0001F63F
    * CAT_ANGRY = \U0001F63E
    * HEART = \U00002764
    * HEART_SPARKLING = \U0001F496
    * HEART_BROKEN = \U0001F494
    * HEART_ORANGE = \U0001F9E1
    * HEART_YELLOW = \U0001F49B
    * HEART_GREEN = \U0001F49A
    * HEART_BLUE = \U0001F499
    * EXPLOSION = \U0001F4A5
    * DIZZY = \U0001F4AB
    * DASH = \U0001F4A8
    * HOLE = \U0001F573
    * BOMB = \U0001F4A3
    * BRAIN = \U0001F9E0
    * BOY = \U0001F466
    * GIRL = \U0001F467
    * MAN = \U0001F468
    * MAN_BEARD = \U0001F9D4
    * WOMAN = \U0001F469
    * WOMAN_BLOND = \U0001F471
    * MAN_OLD = \U0001F474
    * WOMAN_OLD = \U0001F475
    * POLICE = \U0001F46E
    * SUPER_HERO = \U0001F9B8
    * SUPER_VILAIN = \U0001F9B9
    * MAGE = \U0001F9D9
    * FAIRY = \U0001F9DA
    * VAMPIRE = \U0001F9DB
    * MERMAID = \U0001F9DC
    * ELF = \U0001F9DD
    * GENIE = \U0001F9DE
    * ZOMBIE = \U0001F9DF
    * PERSON_RUNNING = \U0001F469
    * PERSON_WALKING = \U0001F6B6
    * PERSON_FENCING = \U0001F93A
    * PERSON_SLEEPING = \U0001F6CC
    * PERSON_YOGA = \U0001F9D8
    * PERSON_BATHING = \U0001F6C0
    * MONKEY = \U0001F435
    * GORILLA = \U0001F98D
    * DOG = \U0001F415
    * DOG_FACE = \U0001F436
    * WOLF_FACE = \U0001F43A
    * FOX_FACE = \U0001F98A
    * RACCOON_FACE = \U0001F99D
    * LION_FACE = \U0001F981
    * TIGER_FACE = \U0001F42F
    * HORSE_FACE = \U0001F434
    * HORSE = \U0001F40E
    * UNICORN_FACE = \U0001F984
    * DEER_FACE = \U0001F98C
    * COW_FACE = \U0001F42E
    * COW = \U0001F404
    * OX = \U0001F402
    * BUFFALO = \U0001F403
    * PIG = \U0001F416
    * PIG_FACE = \U0001F437
    * RAM = \U0001F40F
    * SHEEP = \U0001F411
    * GOAT = \U0001F410
    * LLAMA = \U0001F999
    * GIRAFFE = \U0001F992
    * ELEPHANT = \U0001F418
    * RHINOCEROS_FACE = \U0001F98F
    * MOUSE = \U0001F401
    * RABBIT = \U0001F407
    * CHIPMUNK = \U0001F43F
    * BAT = \U0001F987
    * PANDA_FACE = \U0001F43C
    * TURKEY = \U0001F983
    * CHICKEN = \U0001F414
    * CHICK = \U0001F425
    * EAGLE = \U0001F985
    * DUCK = \U0001F986
    * OWL = \U0001F989
    * FROG_FACE = \U0001F438
    * CROCODILE = \U0001F40A
    * TURTLE = \U0001F422
    * LIZARD = \U0001F98E
    * SNAKE = \U0001F40D
    * DRAGON = \U0001F409
    * DINOSAUR = \U0001F995
    * TREX = \U0001F996
    * WHALE = \U0001F433
    * DOLPHIN = \U0001F42C
    * SHARK = \U0001F988
    * OCTOPUS = \U0001F419
    * SPIDER = \U0001F577
    * SPIDER_WEB = \U0001F578
    * SCORPION = \U0001F982
    * MICROBE = \U0001F9A0
    * SUNFLOWER = \U0001F33B
    * CHERRY_BLOSSOM = \U0001F338
    * FLOWER = \U0001F33C
    * ROSE = \U0001F339
    * TREE_PINE = \U0001F332
    * TREE = \U0001F333
    * TREE_PALM = \U0001F334
    * CACTUS = \U0001F335
    * CLOVER = \U00002618
    * CLOVER_LUCKY = \U0001F340
    * CHEESE = \U0001F9C0
    * MEAT_BONE = \U0001F356
    * MEAT = \U0001F969
    * BACON = \U0001F953
    * EGG = \U0001F95A
    * CRAB = \U0001F980
    * LOBSTER = \U0001F99E
    * SHRIMP = \U0001F990
    * SQUID = \U0001F991
    * KNIFE = \U0001F52A
    * AMPHORA = \U0001F3FA
    * EARTH_GLOBE = \U0001F30D
    * WALL = \U0001F9F1
    * HOUSE = \U0001F3E0
    * CASTLE = \U0001F3F0
    * MON = \U000026E9
    * FOUNTAIN = \U000026F2
    * ROCKET = \U0001F680
    * FLYING_SAUCER = \U0001F6F8
    * HOURGLASS = \U000022F3
    * CYCLONE = \U0001F300
    * RAINBOW = \U0001F308
    * ZAP = \U000026A1
    * SNOWMAN = \U00002603
    * COMET = \U00002604
    * FIRE = \U0001F525
    * WATER_DROP = \U0001F4A7
    * JACK_O_LANTERN = \U0001F383
    * DYNAMITE = \U0001F9E8
    * SPARKLES = \U00002728
    * GIFT = \U0001F381
    * TROPHY = \U0001F3C6
    * CROWN = \U0001F451
    * GEM_STONE = \U0001F48E
    * CANDLE = \U0001F56F
    * LIGHT_BULB = \U0001F4A1
    * BOOK_OPEN = \U0001F4D6
    * SCROLL = \U0001F4DC
    * MONEY_BAG = \U0001F4B0
    * BANKNOTE_DOLLARS = \U0001F4B5
    * BANKNOTE_EUROS = \U0001F4B6
    * BANKNOTE_WINGS = \U0001F4B8
    * DOLLAR = \U0001F4B2
    * LOCKED = \U0001F512
    * UNLOCKED = \U0001F513
    * KEY = \U0001F5DD
    * PICK = \U000026CF
    * SWORD = \U0001F5E1
    * SWORD_CROSSED = \U00002694
    * PISTOL = \U0001F52B
    * BOW = \U0001F3F9
    * SHIELD = \U0001F6E1
    * COFFIN = \U000026B0
    * RADIOACTIVE = \U00002622
    * FLAG_GOAL = \U0001F3C1
    * DOOR = \U0001F6AA

"""
init()

COWBOY = '\U0001F920'
DEAMON_HAPPY = '\U0001F608'
DAEMON_ANGRY = '\U0001F47F'
SKULL = '\U0001F480'
SKULL_CROSSBONES = '\U00002620'
POO = '\U0001F4A9'
CLOWN = '\U0001F921'
OGRE = '\U0001F479'
HAPPY_GHOST = '\U0001F47B'
ALIEN = '\U0001F47D'
ALIEN_MONSTER = '\U0001F47E'
ROBOT = '\U0001F916'
CAT = '\U0001F408'
CAT_FACE = '\U0001F63A'
CAT_LOVE = '\U0001F63B'
CAT_WEARY = '\U0001F640'
CAT_CRY = '\U0001F63F'
CAT_ANGRY = '\U0001F63E'
HEART = '\U00002764'
HEART_SPARKLING = '\U0001F496'
HEART_BROKEN = '\U0001F494'
HEART_ORANGE = '\U0001F9E1'
HEART_YELLOW = '\U0001F49B'
HEART_GREEN = '\U0001F49A'
HEART_BLUE = '\U0001F499'
EXPLOSION = '\U0001F4A5'
DIZZY = '\U0001F4AB'
DASH = '\U0001F4A8'
HOLE = '\U0001F573'
BOMB = '\U0001F4A3'
BRAIN = '\U0001F9E0'
BOY = '\U0001F466'
GIRL = '\U0001F467'
MAN = '\U0001F468'
MAN_BEARD = '\U0001F9D4'
WOMAN = '\U0001F469'
WOMAN_BLOND = '\U0001F471'
MAN_OLD = '\U0001F474'
WOMAN_OLD = '\U0001F475'
POLICE = '\U0001F46E'
SUPER_HERO = '\U0001F9B8'
SUPER_VILAIN = '\U0001F9B9'
MAGE = '\U0001F9D9'
FAIRY = '\U0001F9DA'
VAMPIRE = '\U0001F9DB'
MERMAID = '\U0001F9DC'
ELF = '\U0001F9DD'
GENIE = '\U0001F9DE'
ZOMBIE = '\U0001F9DF'
PERSON_RUNNING = '\U0001F469'
PERSON_WALKING = '\U0001F6B6'
PERSON_FENCING = '\U0001F93A'
PERSON_SLEEPING = '\U0001F6CC'
PERSON_YOGA = '\U0001F9D8'
PERSON_BATHING = '\U0001F6C0'
MONKEY = '\U0001F435'
GORILLA = '\U0001F98D'
DOG = '\U0001F415'
DOG_FACE = '\U0001F436'
WOLF_FACE = '\U0001F43A'
FOX_FACE = '\U0001F98A'
RACCOON_FACE = '\U0001F99D'
LION_FACE = '\U0001F981'
TIGER_FACE = '\U0001F42F'
HORSE_FACE = '\U0001F434'
HORSE = '\U0001F40E'
UNICORN_FACE = '\U0001F984'
DEER_FACE = '\U0001F98C'
COW_FACE = '\U0001F42E'
COW = '\U0001F404'
OX = '\U0001F402'
BUFFALO = '\U0001F403'
PIG = '\U0001F416'
PIG_FACE = '\U0001F437'
RAM = '\U0001F40F'
SHEEP = '\U0001F411'
GOAT = '\U0001F410'
LLAMA = '\U0001F999'
GIRAFFE = '\U0001F992'
ELEPHANT = '\U0001F418'
RHINOCEROS_FACE = '\U0001F98F'
MOUSE = '\U0001F401'
RABBIT = '\U0001F407'
CHIPMUNK = '\U0001F43F'
BAT = '\U0001F987'
PANDA_FACE = '\U0001F43C'
TURKEY = '\U0001F983'
CHICKEN = '\U0001F414'
CHICK = '\U0001F425'
EAGLE = '\U0001F985'
DUCK = '\U0001F986'
OWL = '\U0001F989'
FROG_FACE = '\U0001F438'
CROCODILE = '\U0001F40A'
TURTLE = '\U0001F422'
LIZARD = '\U0001F98E'
SNAKE = '\U0001F40D'
DRAGON = '\U0001F409'
DINOSAUR = '\U0001F995'
TREX = '\U0001F996'
WHALE = '\U0001F433'
DOLPHIN = '\U0001F42C'
SHARK = '\U0001F988'
OCTOPUS = '\U0001F419'
SPIDER = '\U0001F577'
SPIDER_WEB = '\U0001F578'
SCORPION = '\U0001F982'
MICROBE = '\U0001F9A0'
SUNFLOWER = '\U0001F33B'
CHERRY_BLOSSOM = '\U0001F338'
FLOWER = '\U0001F33C'
ROSE = '\U0001F339'
TREE_PINE = '\U0001F332'
TREE = '\U0001F333'
TREE_PALM = '\U0001F334'
CACTUS = '\U0001F335'
CLOVER = '\U00002618'
CLOVER_LUCKY = '\U0001F340'
CHEESE = '\U0001F9C0'
MEAT_BONE = '\U0001F356'
MEAT = '\U0001F969'
BACON = '\U0001F953'
EGG = '\U0001F95A'
CRAB = '\U0001F980'
LOBSTER = '\U0001F99E'
SHRIMP = '\U0001F990'
SQUID = '\U0001F991'
KNIFE = '\U0001F52A'
AMPHORA = '\U0001F3FA'
EARTH_GLOBE = '\U0001F30D'
WALL = '\U0001F9F1'
HOUSE = '\U0001F3E0'
CASTLE = '\U0001F3F0'
MON = '\U000026E9'
FOUNTAIN = '\U000026F2'
ROCKET = '\U0001F680'
FLYING_SAUCER = '\U0001F6F8'
HOURGLASS = '\U000022F3'
CYCLONE = '\U0001F300'
RAINBOW = '\U0001F308'
ZAP = '\U000026A1'
SNOWMAN = '\U00002603'
COMET = '\U00002604'
FIRE = '\U0001F525'
WATER_DROP = '\U0001F4A7'
JACK_O_LANTERN = '\U0001F383'
DYNAMITE = '\U0001F9E8'
SPARKLES = '\U00002728'
GIFT = '\U0001F381'
TROPHY = '\U0001F3C6'
CROWN = '\U0001F451'
GEM_STONE = '\U0001F48E'
CANDLE = '\U0001F56F'
LIGHT_BULB = '\U0001F4A1'
BOOK_OPEN = '\U0001F4D6'
SCROLL = '\U0001F4DC'
MONEY_BAG = '\U0001F4B0'
BANKNOTE_DOLLARS = '\U0001F4B5'
BANKNOTE_EUROS = '\U0001F4B6'
BANKNOTE_WINGS = '\U0001F4B8'
DOLLAR = '\U0001F4B2'
LOCKED = '\U0001F512'
UNLOCKED = '\U0001F513'
KEY = '\U0001F5DD'
PICK = '\U000026CF'
SWORD = '\U0001F5E1'
SWORD_CROSSED = '\U00002694'
PISTOL = '\U0001F52B'
BOW = '\U0001F3F9'
SHIELD = '\U0001F6E1'
COFFIN = '\U000026B0'
RADIOACTIVE = '\U00002622'
FLAG_GOAL = '\U0001F3C1'
DOOR = '\U0001F6AA'

# UI elements
# Box drawings
BOX_DRAWINGS_LIGHT_HORIZONTAL = '\U00002500'
BOX_DRAWINGS_HEAVY_HORIZONTAL = '\U00002501'
BOX_DRAWINGS_LIGHT_VERTICAL = '\U00002502'
BOX_DRAWINGS_HEAVY_VERTICAL = '\U00002503'
BOX_DRAWINGS_LIGHT_TRIPLE_DASH_HORIZONTAL = '\U00002504'
BOX_DRAWINGS_HEAVY_TRIPLE_DASH_HORIZONTAL = '\U00002505'
BOX_DRAWINGS_LIGHT_TRIPLE_DASH_VERTICAL = '\U00002506'
BOX_DRAWINGS_HEAVY_TRIPLE_DASH_VERTICAL = '\U00002507'
BOX_DRAWINGS_LIGHT_QUADRUPLE_DASH_HORIZONTAL = '\U00002508'
BOX_DRAWINGS_HEAVY_QUADRUPLE_DASH_HORIZONTAL = '\U00002509'
BOX_DRAWINGS_LIGHT_QUADRUPLE_DASH_VERTICAL = '\U0000250A'
BOX_DRAWINGS_HEAVY_QUADRUPLE_DASH_VERTICAL = '\U0000250B'
BOX_DRAWINGS_LIGHT_DOWN_AND_RIGHT = '\U0000250C'
BOX_DRAWINGS_DOWN_LIGHT_AND_RIGHT_HEAVY = '\U0000250D'
BOX_DRAWINGS_DOWN_HEAVY_AND_RIGHT_LIGHT = '\U0000250E'
BOX_DRAWINGS_HEAVY_DOWN_AND_RIGHT = '\U0000250F'
BOX_DRAWINGS_LIGHT_DOWN_AND_LEFT = '\U00002510'
BOX_DRAWINGS_DOWN_LIGHT_AND_LEFT_HEAVY = '\U00002511'
BOX_DRAWINGS_DOWN_HEAVY_AND_LEFT_LIGHT = '\U00002512'
BOX_DRAWINGS_HEAVY_DOWN_AND_LEFT = '\U00002513'
BOX_DRAWINGS_LIGHT_UP_AND_RIGHT = '\U00002514'
BOX_DRAWINGS_UP_LIGHT_AND_RIGHT_HEAVY = '\U00002515'
BOX_DRAWINGS_UP_HEAVY_AND_RIGHT_LIGHT = '\U00002516'
BOX_DRAWINGS_HEAVY_UP_AND_RIGHT = '\U00002517'
BOX_DRAWINGS_LIGHT_UP_AND_LEFT = '\U00002518'
BOX_DRAWINGS_UP_LIGHT_AND_LEFT_HEAVY = '\U00002519'
BOX_DRAWINGS_UP_HEAVY_AND_LEFT_LIGHT = '\U0000251A'
BOX_DRAWINGS_HEAVY_UP_AND_LEFT = '\U0000251B'
BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT = '\U0000251C'
BOX_DRAWINGS_VERTICAL_LIGHT_AND_RIGHT_HEAVY = '\U0000251D'
BOX_DRAWINGS_UP_HEAVY_AND_RIGHT_DOWN_LIGHT = '\U0000251E'
BOX_DRAWINGS_DOWN_HEAVY_AND_RIGHT_UP_LIGHT = '\U0000251F'
BOX_DRAWINGS_VERTICAL_HEAVY_AND_RIGHT_LIGHT = '\U00002520'
BOX_DRAWINGS_DOWN_LIGHT_AND_RIGHT_UP_HEAVY = '\U00002521'
BOX_DRAWINGS_UP_LIGHT_AND_RIGHT_DOWN_HEAVY = '\U00002522'
BOX_DRAWINGS_HEAVY_VERTICAL_AND_RIGHT = '\U00002523'
BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT = '\U00002524'
BOX_DRAWINGS_VERTICAL_LIGHT_AND_LEFT_HEAVY = '\U00002525'
BOX_DRAWINGS_UP_HEAVY_AND_LEFT_DOWN_LIGHT = '\U00002526'
BOX_DRAWINGS_DOWN_HEAVY_AND_LEFT_UP_LIGHT = '\U00002527'
BOX_DRAWINGS_VERTICAL_HEAVY_AND_LEFT_LIGHT = '\U00002528'
BOX_DRAWINGS_DOWN_LIGHT_AND_LEFT_UP_HEAVY = '\U00002529'
BOX_DRAWINGS_UP_LIGHT_AND_LEFT_DOWN_HEAVY = '\U0000252A'
BOX_DRAWINGS_HEAVY_VERTICAL_AND_LEFT = '\U0000252B'
BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL = '\U0000252C'
BOX_DRAWINGS_LEFT_HEAVY_AND_RIGHT_DOWN_LIGHT = '\U0000252D'
BOX_DRAWINGS_RIGHT_HEAVY_AND_LEFT_DOWN_LIGHT = '\U0000252E'
BOX_DRAWINGS_DOWN_LIGHT_AND_HORIZONTAL_HEAVY = '\U0000252F'
BOX_DRAWINGS_DOWN_HEAVY_AND_HORIZONTAL_LIGHT = '\U00002530'
BOX_DRAWINGS_RIGHT_LIGHT_AND_LEFT_DOWN_HEAVY = '\U00002531'
BOX_DRAWINGS_LEFT_LIGHT_AND_RIGHT_DOWN_HEAVY = '\U00002532'
BOX_DRAWINGS_HEAVY_DOWN_AND_HORIZONTAL = '\U00002533'
BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL = '\U00002534'
BOX_DRAWINGS_LEFT_HEAVY_AND_RIGHT_UP_LIGHT = '\U00002535'
BOX_DRAWINGS_RIGHT_HEAVY_AND_LEFT_UP_LIGHT = '\U00002536'
BOX_DRAWINGS_UP_LIGHT_AND_HORIZONTAL_HEAVY = '\U00002537'
BOX_DRAWINGS_UP_HEAVY_AND_HORIZONTAL_LIGHT = '\U00002538'
BOX_DRAWINGS_RIGHT_LIGHT_AND_LEFT_UP_HEAVY = '\U00002539'
BOX_DRAWINGS_LEFT_LIGHT_AND_RIGHT_UP_HEAVY = '\U0000253A'
BOX_DRAWINGS_HEAVY_UP_AND_HORIZONTAL = '\U0000253B'
BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL = '\U0000253C'
BOX_DRAWINGS_LEFT_HEAVY_AND_RIGHT_VERTICAL_LIGHT = '\U0000253D'
BOX_DRAWINGS_RIGHT_HEAVY_AND_LEFT_VERTICAL_LIGHT = '\U0000253E'
BOX_DRAWINGS_VERTICAL_LIGHT_AND_HORIZONTAL_HEAVY = '\U0000253F'
BOX_DRAWINGS_UP_HEAVY_AND_DOWN_HORIZONTAL_LIGHT = '\U00002540'
BOX_DRAWINGS_DOWN_HEAVY_AND_UP_HORIZONTAL_LIGHT = '\U00002541'
BOX_DRAWINGS_VERTICAL_HEAVY_AND_HORIZONTAL_LIGHT = '\U00002542'
BOX_DRAWINGS_LEFT_UP_HEAVY_AND_RIGHT_DOWN_LIGHT = '\U00002543'
BOX_DRAWINGS_RIGHT_UP_HEAVY_AND_LEFT_DOWN_LIGHT = '\U00002544'
BOX_DRAWINGS_LEFT_DOWN_HEAVY_AND_RIGHT_UP_LIGHT = '\U00002545'
BOX_DRAWINGS_RIGHT_DOWN_HEAVY_AND_LEFT_UP_LIGHT = '\U00002546'
BOX_DRAWINGS_DOWN_LIGHT_AND_UP_HORIZONTAL_HEAVY = '\U00002547'
BOX_DRAWINGS_UP_LIGHT_AND_DOWN_HORIZONTAL_HEAVY = '\U00002548'
BOX_DRAWINGS_RIGHT_LIGHT_AND_LEFT_VERTICAL_HEAVY = '\U00002549'
BOX_DRAWINGS_LEFT_LIGHT_AND_RIGHT_VERTICAL_HEAVY = '\U0000254A'
BOX_DRAWINGS_HEAVY_VERTICAL_AND_HORIZONTAL = '\U0000254B'
BOX_DRAWINGS_LIGHT_DOUBLE_DASH_HORIZONTAL = '\U0000254C'
BOX_DRAWINGS_HEAVY_DOUBLE_DASH_HORIZONTAL = '\U0000254D'
BOX_DRAWINGS_LIGHT_DOUBLE_DASH_VERTICAL = '\U0000254E'
BOX_DRAWINGS_HEAVY_DOUBLE_DASH_VERTICAL = '\U0000254F'
BOX_DRAWINGS_DOUBLE_HORIZONTAL = '\U00002550'
BOX_DRAWINGS_DOUBLE_VERTICAL = '\U00002551'
BOX_DRAWINGS_DOWN_SINGLE_AND_RIGHT_DOUBLE = '\U00002552'
BOX_DRAWINGS_DOWN_DOUBLE_AND_RIGHT_SINGLE = '\U00002553'
BOX_DRAWINGS_DOUBLE_DOWN_AND_RIGHT = '\U00002554'
BOX_DRAWINGS_DOWN_SINGLE_AND_LEFT_DOUBLE = '\U00002555'
BOX_DRAWINGS_DOWN_DOUBLE_AND_LEFT_SINGLE = '\U00002556'
BOX_DRAWINGS_DOUBLE_DOWN_AND_LEFT = '\U00002557'
BOX_DRAWINGS_UP_SINGLE_AND_RIGHT_DOUBLE = '\U00002558'
BOX_DRAWINGS_UP_DOUBLE_AND_RIGHT_SINGLE = '\U00002559'
BOX_DRAWINGS_DOUBLE_UP_AND_RIGHT = '\U0000255A'
BOX_DRAWINGS_UP_SINGLE_AND_LEFT_DOUBLE = '\U0000255B'
BOX_DRAWINGS_UP_DOUBLE_AND_LEFT_SINGLE = '\U0000255C'
BOX_DRAWINGS_DOUBLE_UP_AND_LEFT = '\U0000255D'
BOX_DRAWINGS_VERTICAL_SINGLE_AND_RIGHT_DOUBLE = '\U0000255E'
BOX_DRAWINGS_VERTICAL_DOUBLE_AND_RIGHT_SINGLE = '\U0000255F'
BOX_DRAWINGS_DOUBLE_VERTICAL_AND_RIGHT = '\U00002560'
BOX_DRAWINGS_VERTICAL_SINGLE_AND_LEFT_DOUBLE = '\U00002561'
BOX_DRAWINGS_VERTICAL_DOUBLE_AND_LEFT_SINGLE = '\U00002562'
BOX_DRAWINGS_DOUBLE_VERTICAL_AND_LEFT = '\U00002563'
BOX_DRAWINGS_DOWN_SINGLE_AND_HORIZONTAL_DOUBLE = '\U00002564'
BOX_DRAWINGS_DOWN_DOUBLE_AND_HORIZONTAL_SINGLE = '\U00002565'
BOX_DRAWINGS_DOUBLE_DOWN_AND_HORIZONTAL = '\U00002566'
BOX_DRAWINGS_UP_SINGLE_AND_HORIZONTAL_DOUBLE = '\U00002567'
BOX_DRAWINGS_UP_DOUBLE_AND_HORIZONTAL_SINGLE = '\U00002568'
BOX_DRAWINGS_DOUBLE_UP_AND_HORIZONTAL = '\U00002569'
BOX_DRAWINGS_VERTICAL_SINGLE_AND_HORIZONTAL_DOUBLE = '\U0000256A'
BOX_DRAWINGS_VERTICAL_DOUBLE_AND_HORIZONTAL_SINGLE = '\U0000256B'
BOX_DRAWINGS_DOUBLE_VERTICAL_AND_HORIZONTAL = '\U0000256C'
BOX_DRAWINGS_LIGHT_ARC_DOWN_AND_RIGHT = '\U0000256D'
BOX_DRAWINGS_LIGHT_ARC_DOWN_AND_LEFT = '\U0000256E'
BOX_DRAWINGS_LIGHT_ARC_UP_AND_LEFT = '\U0000256F'
BOX_DRAWINGS_LIGHT_ARC_UP_AND_RIGHT = '\U00002570'
BOX_DRAWINGS_LIGHT_DIAGONAL_UPPER_RIGHT_TO_LOWER_LEFT = '\U00002571'
BOX_DRAWINGS_LIGHT_DIAGONAL_UPPER_LEFT_TO_LOWER_RIGHT = '\U00002572'
BOX_DRAWINGS_LIGHT_DIAGONAL_CROSS = '\U00002573'
BOX_DRAWINGS_LIGHT_LEFT = '\U00002574'
BOX_DRAWINGS_LIGHT_UP = '\U00002575'
BOX_DRAWINGS_LIGHT_RIGHT = '\U00002576'
BOX_DRAWINGS_LIGHT_DOWN = '\U00002577'
BOX_DRAWINGS_HEAVY_LEFT = '\U00002578'
BOX_DRAWINGS_HEAVY_UP = '\U00002579'
BOX_DRAWINGS_HEAVY_RIGHT = '\U0000257A'
BOX_DRAWINGS_HEAVY_DOWN = '\U0000257B'
BOX_DRAWINGS_LIGHT_LEFT_AND_HEAVY_RIGHT = '\U0000257C'
BOX_DRAWINGS_LIGHT_UP_AND_HEAVY_DOWN = '\U0000257D'
BOX_DRAWINGS_HEAVY_LEFT_AND_LIGHT_RIGHT = '\U0000257E'
BOX_DRAWINGS_HEAVY_UP_AND_LIGHT_DOWN = '\U0000257F'
# Block elements
UPPER_HALF_BLOCK = '\U00002580'
LOWER_ONE_EIGHTH_BLOCK = '\U00002581'
LOWER_ONE_QUARTER_BLOCK = '\U00002582'
LOWER_THREE_EIGHTHS_BLOCK = '\U00002583'
LOWER_HALF_BLOCK = '\U00002584'
LOWER_FIVE_EIGHTHS_BLOCK = '\U00002585'
LOWER_THREE_QUARTERS_BLOCK = '\U00002586'
LOWER_SEVEN_EIGHTHS_BLOCK = '\U00002587'
FULL_BLOCK = '\U00002588'
LEFT_SEVEN_EIGHTHS_BLOCK = '\U00002589'
LEFT_THREE_QUARTERS_BLOCK = '\U0000258A'
LEFT_FIVE_EIGHTHS_BLOCK = '\U0000258B'
LEFT_HALF_BLOCK = '\U0000258C'
LEFT_THREE_EIGHTHS_BLOCK = '\U0000258D'
LEFT_ONE_QUARTER_BLOCK = '\U0000258E'
LEFT_ONE_EIGHTH_BLOCK = '\U0000258F'
RIGHT_HALF_BLOCK = '\U00002590'
LIGHT_SHADE = '\U00002591'
MEDIUM_SHADE = '\U00002592'
DARK_SHADE = '\U00002593'
UPPER_ONE_EIGHTH_BLOCK = '\U00002594'
RIGHT_ONE_EIGHTH_BLOCK = '\U00002595'
QUADRANT_LOWER_LEFT = '\U00002596'
QUADRANT_LOWER_RIGHT = '\U00002597'
QUADRANT_UPPER_LEFT = '\U00002598'
QUADRANT_UPPER_LEFT_AND_LOWER_LEFT_AND_LOWER_RIGHT = '\U00002599'
QUADRANT_UPPER_LEFT_AND_LOWER_RIGHT = '\U0000259A'
QUADRANT_UPPER_LEFT_AND_UPPER_RIGHT_AND_LOWER_LEFT = '\U0000259B'
QUADRANT_UPPER_LEFT_AND_UPPER_RIGHT_AND_LOWER_RIGHT = '\U0000259C'
QUADRANT_UPPER_RIGHT = '\U0000259D'
QUADRANT_UPPER_RIGHT_AND_LOWER_LEFT = '\U0000259E'
QUADRANT_UPPER_RIGHT_AND_LOWER_LEFT_AND_LOWER_RIGHT = '\U0000259F'

WHITE_RECT = Back.WHITE + " " + Style.RESET_ALL
BLUE_RECT = Back.BLUE + " " + Style.RESET_ALL
RED_RECT = Back.RED + " " + Style.RESET_ALL
MAGENTA_RECT = Back.MAGENTA + " " + Style.RESET_ALL
GREEN_RECT = Back.GREEN + " " + Style.RESET_ALL
YELLOW_RECT = Back.YELLOW + " " + Style.RESET_ALL
BLACK_RECT = Back.BLACK + " " + Style.RESET_ALL
CYAN_RECT = Back.CYAN + " " + Style.RESET_ALL

WHITE_SQUARE = Back.WHITE + "  " + Style.RESET_ALL
MAGENTA_SQUARE = Back.MAGENTA + "  " + Style.RESET_ALL
GREEN_SQUARE = Back.GREEN + "  " + Style.RESET_ALL
RED_SQUARE = Back.RED + "  " + Style.RESET_ALL
BLUE_SQUARE = Back.BLUE + "  " + Style.RESET_ALL
YELLOW_SQUARE = Back.YELLOW + "  " + Style.RESET_ALL
BLACK_SQUARE = Back.BLACK + "  " + Style.RESET_ALL
CYAN_SQUARE = Back.CYAN + "  " + Style.RESET_ALL

RED_BLUE_SQUARE = Back.RED + " " + Back.BLUE + " " + Style.RESET_ALL
YELLOW_CYAN_SQUARE = Back.YELLOW + " " + Back.CYAN + " " + Style.RESET_ALL


_exitcode, clear_sequence = subprocess.getstatusoutput("tput clear")
if _exitcode:
    clear_sequence = colorama.ansi.clear_screen()
