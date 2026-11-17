"""All site content, loaded from the JSON files in web/data/ (edit those, not this file).

Each JSON object is turned back into the tuples/lists the themes already expect, so the themes read `content.X` as before.
"""
import json
from pathlib import Path

_DIR = Path(__file__).parent / "data"


def _read(name):
    try:
        return json.loads((_DIR / name).read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"data/{name}: invalid JSON at line {e.lineno}, column {e.colno}: {e.msg}")


def _t(items, fields):
    """[{field: value, ...}, ...] -> [(value, ...), ...] in the given field order."""
    try:
        return [tuple(i[f] for f in fields) for i in items]
    except KeyError as e:
        raise SystemExit(f"data/*.json: an entry is missing the field {e} (expected {fields})")


_school = _read("school.json")
SCHOOL = {**_school["SCHOOL"], "emails": _t(_school["SCHOOL"]["emails"], ["role", "email"])}
QUOTE = _school["QUOTE"]
VISION = _school["VISION"]
MISSION = _school["MISSION"]
SCHOOL_VALUES = _school["SCHOOL_VALUES"]
SCHOOL_MISSION = _school["SCHOOL_MISSION"]
ZAHIR_BIO = _school["ZAHIR_BIO"]
PIONEER_NOTE = _school["PIONEER_NOTE"]
OBJECTS = _school["OBJECTS"]
PANCHGANI_UNITS = _t(_school["PANCHGANI_UNITS"], ["level", "medium", "funding"])
MAP_QUERY = _school["MAP_QUERY"]
MAP_LL = _school["MAP_LL"]
PLACE_INTRO = _school["PLACE_INTRO"]
COACHING_NOTE = _school["COACHING_NOTE"]
CAL_NOTE = _school["CAL_NOTE"]
DAY_NOTE = _school["DAY_NOTE"]

_num = _read("numbers.json")
STATS = _t(_num["STATS"], ["label", "value", "suffix"])
NETWORK_STATS = _t(_num["NETWORK_STATS"], ["label", "value", "suffix"])
EDU_STATS = _t(_num["EDU_STATS"], ["label", "value", "suffix"])
PLACE_FACTS = _t(_num["PLACE_FACTS"], ["value", "label", "text"])
SSC_2026 = _num["SSC_2026"]
HSC_2026 = {**_num["HSC_2026"], "streams": _t(_num["HSC_2026"]["streams"], ["stream", "appeared", "passed", "distinction", "percent"])}
EXAMS = _t(_num["EXAMS"], ["short", "full", "field"])
YEARS = _num["YEARS"]
EXAM_TOTALS = _num["EXAM_TOTALS"]
EXAM_BY_YEAR = _num["EXAM_BY_YEAR"]

_people = _read("people.json")
PRESIDENTS = _t(_people["PRESIDENTS"], ["name", "tenure", "philanthropist"])
BOARD = _people["BOARD"]

_hist = _read("history.json")
HISTORY = _t(_hist["HISTORY"], ["year", "text"])
GOALS = _t(_hist["GOALS"], ["numeral", "text", "when"])
ACHIEVEMENTS = _t(_hist["ACHIEVEMENTS"], ["year", "title", "detail", "category"])

_inst = _read("institutions.json")
INSTITUTIONS = {g: _t(v, ["city", "medium", "name", "funding"]) for g, v in _inst["INSTITUTIONS"].items()}
MARQUEE_INSTITUTIONS = _inst["MARQUEE_INSTITUTIONS"]

_campus = _read("campus.json")
PROGRAMMES = _t(_campus["PROGRAMMES"], ["title", "text"])
ACADEMIC_APPROACH = _t(_campus["ACADEMIC_APPROACH"], ["title", "text"])
FACILITIES = _t(_campus["FACILITIES"], ["title", "icon", "text"])
BOARDING = _t(_campus["BOARDING"], ["title", "icon", "scene", "text"])
ACTIVITIES = _t(_campus["ACTIVITIES"], ["title", "category", "icon", "text"])
DAY = _t(_campus["DAY"], ["title", "text"])
JOURNEY = _t(_campus["JOURNEY"], ["title", "text"])
UNIQUE = _campus["UNIQUE"]
DAYPLAN = _campus["DAYPLAN"]
DAYSKY = [list(r) for r in _t(_campus["DAYSKY"], ["hour", "top", "bottom"])]

_adm = _read("admissions.json")
STEPS = _t(_adm["STEPS"], ["step", "note"])
IMPORTANT = _adm["IMPORTANT"]
FEES = _adm["FEES"]
FAQ = _t(_adm["FAQ"], ["question", "answer"])

_cal = _read("calendar.json")
CAL_TYPES = _cal["CAL_TYPES"]
CALENDAR = [(m["month"], _t(m["events"], ["day", "title", "type"])) for m in _cal["CALENDAR"]]

NEWS = _t(_read("news.json")["NEWS"], ["date", "title", "tag", "url", "image"])
IMAGES = _read("images.json")
