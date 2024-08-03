from enum import Enum
from typing import TypedDict


class ReleaseType(Enum):
    ALBUM = "album"
    EP = "ep"
    SINGLE = "single"
    LIVE = "live"
    COMPILATION = "compilation"
    BOOTLEG = "bootleg"


class Release(TypedDict):
    title: str
    type: ReleaseType
    year: int
    tracks: list[str]


AE_RARITIES_1992_2020 = Release(
    title="AE_RARITIES 1992-2020",
    type=ReleaseType.BOOTLEG,
    year=2020,
    tracks=[
        "The Egg",
        "Crystel",
        "Chatter",
        "Lanx 3",
        "Puch",
        "Stop Look Listen",
        "Coenc3",
        "nu-Nr6d",
        "6852",
        "SYptixed",
        "spl47",
        "JNSN CODE GL16",
        "Carni",
        "Medrey",
        "Nonima",
        "Inhake 3",
        "Xektses sql",
        "ClnChr",
        "ts1a",
        "18 (keyosc)",
        "sinistrail sentinel",
        "p1p2",
        "n Cur",
    ],
)

INCUNABULA = Release(
    title="Incunabula",
    type=ReleaseType.ALBUM,
    year=1993,
    tracks=[
        "Kalpol Introl",
        "Bike",
        "Autriche",
        "Bronchus 2",
        "Basscadet",
        "Eggshell",
        "Doctrine",
        "Maetl",
        "Windwind",
        "Lowride",
        "444",
    ],
)

AMBER = Release(
    title="Amber",
    type=ReleaseType.ALBUM,
    year=1994,
    tracks=[
        "Foil",
        "Montreal",
        "Silverside",
        "Slip",
        "Glitch",
        "Piezo",
        "Nine",
        "Further",
        "Yulquen",
        "Nil",
        "Teartear",
    ],
)

TRI_REPETAE = Release(
    title="Tri Repetae",
    type=ReleaseType.ALBUM,
    year=1995,
    tracks=[
        "Dael",
        "Clipper",
        "Leterel",
        "Rotar",
        "Stud",
        "Eutow",
        "C/Pach",
        "Gnit",
        "Overand",
        "Rsdio",
    ],
)

CHIASTIC_SLIDE = Release(
    title="Chiastic Slide",
    type=ReleaseType.ALBUM,
    year=1996,
    tracks=[
        "Cipater",
        "Rettic AC",
        "Tewe",
        "Cichli",
        "Hub",
        "Calbruc",
        "Recury",
        "Pule",
        "Nuane",
    ],
)

LP5 = Release(
    title="LP5",
    type=ReleaseType.ALBUM,
    year=1998,
    tracks=[
        "AcroyearII",
        "777",
        "Rae",
        "Melve",
        "Vose In",
        "Fold4, Wrap5",
        "Under BOAC",
        "Corc",
        "Caliper Remote",
        "Arch Carrier",
        "Drane2",
    ],
)

CONFIELD = Release(
    title="Confield",
    type=ReleaseType.ALBUM,
    year=2001,
    tracks=[
        "VI Scose Poise",
        "Cfern",
        "Pen Expers",
        "Sim Gishel",
        "Parhelic Triangle",
        "Bine",
        "Eidetic Casein",
        "Uviol",
        "Lentic Catachresis",
    ],
)

DRAFT_7_30 = Release(
    title="Draft 7.30",
    type=ReleaseType.ALBUM,
    year=2003,
    tracks=[
        "Xylin Room",
        "IV VV IV VV VIII",
        "6IE.CR",
        "Tapr",
        "SURRIPERE",
        "Theme Of Sudden Roundabout",
        "VL AL 5",
        "P.:NTIL",
        "V-Proc",
        "Reniform Puls",
    ],
)

UNTILTED = Release(
    title="Untilted",
    type=ReleaseType.ALBUM,
    year=2005,
    tracks=[
        "LCC",
        "Ipacial Section",
        "Pro Radii",
        "Augmatic Disport",
        "Iera",
        "Fermium",
        "The Trees",
        "Sublimit",
    ],
)

QUARISTICE = Release(
    title="Quaristice",
    type=ReleaseType.ALBUM,
    year=2008,
    tracks=[
        "Altibzz",
        "The Plc",
        "IO",
        "plyPhon",
        "Perlence",
        "SonDEremawe",
        "Simmm",
        "paralel Suns",
        "Steels",
        "Tankakern",
        "rale",
        "Fol3",
        "fwzE",
        "90101-5l-l",
        "bnc Castl",
        "Theswere",
        "WNSN",
        "chenc9",
        "Notwo",
        "Outh9X",
    ],
)

OVERSTEPS = Release(
    title="Oversteps",
    type=ReleaseType.ALBUM,
    year=2010,
    tracks=[
        "r ess",
        "ilanders",
        "known(1)",
        "pt2ph8",
        "qplay",
        "see on see",
        "Treale",
        "os veix3",
        "O=0",
        "d-sho qub",
        "st epreo",
        "redfall",
        "krYlon",
        "Yuop",
    ],
)

EXAI = Release(
    title="Exai",
    type=ReleaseType.ALBUM,
    year=2013,
    tracks=[
        "FLeure",
        "irlite (get 0)",
        "prac-f",
        "jatevee C",
        "T ess xi",
        "vekoS",
        "Flep",
        "tuinorizn",
        "bladelores",
        "1 1 is",
        "nodezsh",
        "runrepik",
        "spl9",
        "cloudline",
        "deco Loc",
        "recks on",
        "YJY UX",
    ],
)

ELSEQ_1_5 = Release(
    title="elseq 1-5",
    type=ReleaseType.ALBUM,
    year=2016,
    tracks=[
        "feed1",
        "c16 deep tread",
        "13x0 step",
        "pendulu hv moda",
        "curvcaten",
        "elyc6 0nset",
        "chimer 1-5-1",
        "c7b2",
        "eastre",
        "TBM2",
        "mesh cinereaL",
        "acdwn2",
        "foldfree casual",
        "latentcall",
        "artov chain",
        "7th slip",
        "pendulu casual",
        "spTh",
        "spaces how V",
        "freulaeux",
        "oneum",
    ],
)

NTS_SESSIONS_1_4 = Release(
    title="NTS Sessions 1-4",
    type=ReleaseType.ALBUM,
    year=2018,
    tracks=[
        "t1a1",
        "bqbqbq",
        "debris_funk",
        "l3 ctrl",
        "carefree counter dronal",
        "north spiral",
        "gonk steady one",
        "four of seven",
        "32a_reflected",
        "elyc9 7hres",
        "six of eight (midst)",
        "xflood",
        "gonk tuf hi",
        "dummy casual pt2",
        "violvoic",
        "sinistrailAB air",
        "wetgelis casual interval",
        "e0",
        "peal MA",
        "9 chr0",
        "turbile epic casual, stpl idle",
        "clustro casual",
        "splesh",
        "tt1pd",
        "acid mwan idle",
        "fLh",
        "glos ceramic",
        "g 1 e 1",
        "nineFly",
        "shimripl air",
        "icari",
        "frane casual",
        "mirrage",
        "column thirteen",
        "shimripl casual",
        "all end",
    ],
)

WARP_TAPES_89_93 = Release(
    title="Warp Tapes 89-93",
    type=ReleaseType.ALBUM,
    year=2019,
    tracks=[
        "Warp Tapes 89-93 Part 1",
        "Warp Tapes 89-93 Part 2",
    ],
)

SIGN = Release(
    title="SIGN",
    type=ReleaseType.ALBUM,
    year=2020,
    tracks=[
        "M4 Lema",
        "F7",
        "si00",
        "esc desc",
        "au14",
        "Metaz form8",
        "sch.mefd 2",
        "gr4",
        "th red a",
        "psin AM",
        "r cazt",
    ],
)

PLUS = Release(
    title="Plus",
    type=ReleaseType.ALBUM,
    year=2020,
    tracks=[
        "DekDre Scap B",
        "7FM ic",
        "marhide",
        "ecol4",
        "lux 106 mod",
        "X4",
        "ii.pre esc",
        "esle 0",
        "TM1 open",
    ],
)

CAVITY_JOB = Release(
    title="Cavity Job",
    type=ReleaseType.SINGLE,
    year=1991,
    tracks=[
        "Cavity Job",
        "Accelera 1 & 2",
    ],
)

ANTI = Release(
    title="Anti",
    type=ReleaseType.EP,
    year=1994,
    tracks=[
        "Lost",
        "Djarum",
        "Flutter",
    ],
)

ANVIL_VAPRE = Release(
    title="Anvil Vapre",
    type=ReleaseType.EP,
    year=1995,
    tracks=[
        "Second Bad Vilbel",
        "Second Scepe",
        "Second Scout",
        "Second Peng",
    ],
)

GARBAGE = Release(
    title="Garbage",
    type=ReleaseType.EP,
    year=1995,
    tracks=[
        "Garbagemx",
        "PIOBmx",
        "Bronchusevenmx",
        "VLetrmx",
    ],
)

KEYNELL_KEYNELL = Release(
    title="Keynell / Keynell", type=ReleaseType.SINGLE, year=1996, tracks=["Keynell"]
)

WE_R_ARE_WHY_ARE_Y_ARE_WE = Release(
    title="We R Are Why / Are Y Are We?",
    type=ReleaseType.SINGLE,
    year=1996,
    tracks=[
        "We R Are Why",
        "Are Y Are We?",
    ],
)

ENVANE = Release(
    title="Envane",
    type=ReleaseType.EP,
    year=1997,
    tracks=[
        "Goz Quarter",
        "Latent Quarter",
        "Laughing Quarter",
        "Draun Quarter",
    ],
)

CICHLISUITE = Release(
    title="Cichlisuite",
    type=ReleaseType.EP,
    year=1997,
    tracks=[
        "Yeesland",
        "Pencha",
        "Characi",
        "Krib",
        "Tilapia",
    ],
)

EP7 = Release(
    title="EP7",
    type=ReleaseType.EP,
    year=1999,
    tracks=[
        "Untitled",
        "(silence)",
        "Rpeg",
        "Ccec",
        "Squeller",
        "Left Blank",
        "Outpt",
        "Dropp",
        "Liccflii",
        "Maphive 6.1",
        "Zeiss Contarex",
        "Netlon Sentinel",
        "Pir",
    ],
)

GANTZ_GRAF = Release(
    title="Gantz Graf",
    type=ReleaseType.EP,
    year=2002,
    tracks=[
        "Gantz Graf",
        "Dial.",
        "Cap.IV",
    ],
)

QUARISTICE_VERSIONS = Release(
    title="Quaristice (Versions)",
    type=ReleaseType.EP,
    year=2008,
    tracks=[
        "Altichyre",
        "The PlclCpC",
        "IO (mons)",
        "Phylopn",
        "Perlence range3",
        "SonDEre-ix",
        "Tankraken",
        "fol4",
        "90101-61-01",
        "chenc9-x",
        "nofour",
    ],
)

QUARISTICE_QUADRANGE_EP_AE = Release(
    title="Quaristice.Quadrange.ep.ae",
    type=ReleaseType.EP,
    year=2008,
    tracks=[
        "The Plc ccc",
        "Perlence range 7",
        "Perlence Suns",
        "90101-51-6",
        "9013-2",
        "Tkakanren",
        "90101-51-19",
        "Perlence subrange 3",
        "chenc9-1dub",
        "9010171-121",
        "Perlence losid 2",
        "notwotwo",
        "Perlence subrange 6-36",
    ],
)

MOVE_OF_TEN = Release(
    title="Move Of Ten",
    type=ReleaseType.EP,
    year=2010,
    tracks=[
        "Etchogon-S",
        "y7",
        "pce freeze 2.8i",
        "rew (1)",
        "nth Dafuseder.b",
        "iris was a pupil",
        "no border",
        "M62",
        "ylm0",
        "Cep puiqMX",
    ],
)

L_EVENT = Release(
    title="L-event",
    type=ReleaseType.EP,
    year=2013,
    tracks=[
        "tac Lacora",
        "M39 Diffain",
        "Osla for n",
        "newbound",
    ],
)

JNSN_CODE_GL16_SPL47 = Release(
    title="JNSN CODE GL16 / spl47",
    type=ReleaseType.SINGLE,
    year=2017,
    tracks=[
        "JNSN CODE GL16",
        "spl47",
    ],
)

PEEL_SESSION = Release(
    title="Peel Session",
    type=ReleaseType.EP,
    year=1999,
    tracks=[
        "Milk DX",
        "Inhake 2",
        "Drane",
    ],
)

AE_LIVE = Release(
    title="AE_LIVE",
    type=ReleaseType.LIVE,
    year=2015,
    tracks=[
        "AE_LIVE_KRAKOW_200914",
        "AE_LIVE_BRUSSELS_031014",
        "AE_LIVE_UTRECHT_221114",
        "AE_LIVE_DUBLIN_191214",
        "AE_LIVE_KREMS_020515",
        "AE_LIVE_NAGANO_300515",
        "AE_LIVE_GRAFENHAINICHEN_170715",
        "AE_LIVE_DOUR_180715",
        "AE_LIVE_KATOWICE_210815",
        "AE_LIVE_PORTLAND_240915",
        "AE_LIVE_SEATTLE_250915",
        "AE_LIVE_VANCOUVER_260915",
        "AE_LIVE_CHICAGO_290915",
        "AE_LIVE_TORONTO_011015",
        "AE_LIVE_MONTREAL_021015",
        "AE_LIVE_NEW_YORK_031015",
        "AE_LIVE_BOSTON_041015",
        "AE_LIVE_PORTSMOUTH_051015",
        "AE_LIVE_PHILADELPHIA_061015",
        "AE_LIVE_WASHINGTON_071015",
        "AE_LIVE_ASHEVILLE_081015",
        "AE_LIVE_ATLANTA_091015",
        "AE_LIVE_ORLANDO_101015",
        "AE_LIVE_MIAMI_111015",
        "AE_LIVE_AUSTIN_131015",
        "AE_LIVE_LOS_ANGELES_151015",
        "AE_LIVE_SAN_FRANCISCO_161015",
        "AE_LIVE_DENVER_171015",
    ],
)

AE_LIVE_2016_2018 = Release(
    title="AE_LIVE 2016/2018",
    type=ReleaseType.LIVE,
    year=2020,
    tracks=[
        "AE_LIVE_ZAGREB_061116",
        "AE_LIVE_MELBOURNE_210618",
        "AE_LIVE_TALLINN_131116",
        "AE_LIVE_NIJMEGEN_221116",
        "AE_LIVE_HELSINKI_141116",
        "AE_LIVE_DUBLIN_150718",
        "AE_LIVE_OSLO_171116",
    ],
)

AE_RELEASES = [
    AE_RARITIES_1992_2020,
    INCUNABULA,
    AMBER,
    TRI_REPETAE,
    CHIASTIC_SLIDE,
    LP5,
    CONFIELD,
    DRAFT_7_30,
    UNTILTED,
    QUARISTICE,
    OVERSTEPS,
    EXAI,
    ELSEQ_1_5,
    NTS_SESSIONS_1_4,
    WARP_TAPES_89_93,
    SIGN,
    PLUS,
    CAVITY_JOB,
    ANTI,
    ANVIL_VAPRE,
    GARBAGE,
    KEYNELL_KEYNELL,
    WE_R_ARE_WHY_ARE_Y_ARE_WE,
    ENVANE,
    CICHLISUITE,
    EP7,
    GANTZ_GRAF,
    QUARISTICE,
    QUARISTICE_QUADRANGE_EP_AE,
    MOVE_OF_TEN,
    L_EVENT,
    JNSN_CODE_GL16_SPL47,
    PEEL_SESSION,
    AE_LIVE,
    AE_LIVE_2016_2018,
]
