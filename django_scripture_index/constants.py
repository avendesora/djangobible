from enum import IntEnum
from pathlib import Path


class BookOfTheBible(IntEnum):
    GENESIS = 1
    EXODUS = 2
    LEVITICUS = 3
    NUMBERS = 4
    DEUTERONOMY = 5
    JOSHUA = 6
    JUDGES = 7
    RUTH = 8
    SAMUEL_1 = 9
    SAMUEL_2 = 10
    KINGS_1 = 11
    KINGS_2 = 12
    CHRONICLES_1 = 13
    CHRONICLES_2 = 14
    EZRA = 15
    NEHEMIAH = 16
    ESTHER = 17
    JOB = 18
    PSALMS = 19
    PROVERBS = 20
    ECCLESIASTES = 21
    SONG_OF_SONGS = 22
    ISAIAH = 23
    JEREMIAH = 24
    LAMENTATIONS = 25
    EZEKIEL = 26
    DANIEL = 27
    HOSEA = 28
    JOEL = 29
    AMOS = 30
    OBADIAH = 31
    JONAH = 32
    MICAH = 33
    NAHUM = 34
    HABAKKUK = 35
    ZEPHANIAH = 36
    HAGGAI = 37
    ZECHARIAH = 38
    MALACHI = 39
    MATTHEW = 40
    MARK = 41
    LUKE = 42
    JOHN = 43
    ACTS = 44
    ROMANS = 45
    CORINTHIANS_1 = 46
    CORINTHIANS_2 = 47
    GALATIANS = 48
    EPHESIANS = 49
    PHILIPPIANS = 50
    COLOSSIANS = 51
    THESSALONIANS_1 = 52
    THESSALONIANS_2 = 53
    TIMOTHY_1 = 54
    TIMOTHY_2 = 55
    TITUS = 56
    PHILEMON = 57
    HEBREWS = 58
    JAMES = 59
    PETER_1 = 60
    PETER_2 = 61
    JOHN_1 = 62
    JOHN_2 = 63
    JOHN_3 = 64
    JUDE = 65
    REVELATION = 66
    ESDRAS_1 = 67
    TOBIT = 68
    WISDOM_OF_SOLOMON = 69
    ECCLESIASTICUS = 70
    MACCABEES_1 = 71
    MACCABEES_2 = 72

    def name(self):
        return _BOOK_OF_THE_BIBLE_NAMES.get(self)


_BOOK_OF_THE_BIBLE_NAMES = {
    BookOfTheBible.GENESIS: 'Genesis',
    BookOfTheBible.EXODUS: 'Exodus',
    BookOfTheBible.LEVITICUS: 'Leviticus',
    BookOfTheBible.NUMBERS: 'Numbers',
    BookOfTheBible.DEUTERONOMY: 'Deuteronomy',
    BookOfTheBible.JOSHUA: 'Joshua',
    BookOfTheBible.JUDGES: 'Judges',
    BookOfTheBible.RUTH: 'Ruth',
    BookOfTheBible.SAMUEL_1: '1 Samuel',
    BookOfTheBible.SAMUEL_2: '2 Samuel',
    BookOfTheBible.KINGS_1: '1 Kings',
    BookOfTheBible.KINGS_2: '2 Kings',
    BookOfTheBible.CHRONICLES_1: '1 Chronicles',
    BookOfTheBible.CHRONICLES_2: '2 Chronicles',
    BookOfTheBible.EZRA: 'Ezra',
    BookOfTheBible.NEHEMIAH: 'Nehemiah',
    BookOfTheBible.ESTHER: 'Esther',
    BookOfTheBible.JOB: 'Job',
    BookOfTheBible.PSALMS: 'Psalms',
    BookOfTheBible.PROVERBS: 'Proverbs',
    BookOfTheBible.ECCLESIASTES: 'Ecclesiastes',
    BookOfTheBible.SONG_OF_SONGS: 'Song of Songs',
    BookOfTheBible.ISAIAH: 'Isaiah',
    BookOfTheBible.JEREMIAH: 'Jeremiah',
    BookOfTheBible.LAMENTATIONS: 'Lamentations',
    BookOfTheBible.EZEKIEL: 'Ezekiel',
    BookOfTheBible.DANIEL: 'Daniel',
    BookOfTheBible.HOSEA: 'Hosea',
    BookOfTheBible.JOEL: 'Joel',
    BookOfTheBible.AMOS: 'Amos',
    BookOfTheBible.OBADIAH: 'Obadiah',
    BookOfTheBible.JONAH: 'Jonah',
    BookOfTheBible.MICAH: 'Micah',
    BookOfTheBible.NAHUM: 'Nahum',
    BookOfTheBible.HABAKKUK: 'Habakkuk',
    BookOfTheBible.ZEPHANIAH: 'Zephaniah',
    BookOfTheBible.HAGGAI: 'Haggai',
    BookOfTheBible.ZECHARIAH: 'Zechariah',
    BookOfTheBible.MALACHI: 'Malachi',
    BookOfTheBible.MATTHEW: 'Matthew',
    BookOfTheBible.MARK: 'Mark',
    BookOfTheBible.LUKE: 'Luke',
    BookOfTheBible.JOHN: 'John',
    BookOfTheBible.ACTS: 'Acts',
    BookOfTheBible.ROMANS: 'Romans',
    BookOfTheBible.CORINTHIANS_1: '1 Corinthians',
    BookOfTheBible.CORINTHIANS_2: '2 Corinthians',
    BookOfTheBible.GALATIANS: 'Galatians',
    BookOfTheBible.EPHESIANS: 'Ephesians',
    BookOfTheBible.PHILIPPIANS: 'Philippians',
    BookOfTheBible.COLOSSIANS: 'Colossians',
    BookOfTheBible.THESSALONIANS_1: '1 Thessalonians',
    BookOfTheBible.THESSALONIANS_2: '2 Thessalonians',
    BookOfTheBible.TIMOTHY_1: '1 Timothy',
    BookOfTheBible.TIMOTHY_2: '2 Timothy',
    BookOfTheBible.TITUS: 'Titus',
    BookOfTheBible.PHILEMON: 'Philemon',
    BookOfTheBible.HEBREWS: 'Hebrews',
    BookOfTheBible.JAMES: 'James',
    BookOfTheBible.PETER_1: '1 Peter',
    BookOfTheBible.PETER_2: '2 Peter',
    BookOfTheBible.JOHN_1: '1 John',
    BookOfTheBible.JOHN_2: '2 John',
    BookOfTheBible.JOHN_3: '3 John',
    BookOfTheBible.JUDE: 'Jude',
    BookOfTheBible.REVELATION: 'Revelation',
    BookOfTheBible.ESDRAS_1: '1 Esdras',
    BookOfTheBible.TOBIT: 'Tobit',
    BookOfTheBible.WISDOM_OF_SOLOMON: 'Wisdom of Solomon',
    BookOfTheBible.ECCLESIASTICUS: 'Ecclesiasticus',
    BookOfTheBible.MACCABEES_1: '1 Maccabees',
    BookOfTheBible.MACCABEES_2: '2 Maccabees',
}

with open(Path(__file__).resolve().parent / 'data' / 'verse_ids.txt') as verse_ids_file:
    VERSE_IDS = [int(verse_id) for verse_id in verse_ids_file.readlines()]
