import re, pytest
from persian_text_normalizer import PersianNormalizer

norm = PersianNormalizer()


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("<h1>سلام دنیا!</h1>", "سلام دنیا"),
        ("برای اطلاعات برو به https://example.com", "برای اطلاعات برو به [URL]"),
    ],
)
def test_html_url(raw, expected):
    assert norm(raw) == expected


def test_pinglish():
    raw = "salam chetori? man khoobam."
    out = norm(raw)
    assert out == "سلام چطوری من خوبم"


def test_spacing_and_halfspace():
    raw = "ما    به مدرسه می رویم و کتاب ها را     میخوانیم."
    out = norm(raw)
    assert out == "ما به مدرسه می\u200cرویم و کتاب\u200cها را می\u200cخوانیم"


def test_digits_and_arabic_letters():
    raw = "عدد عربی ٢٣٤ و لاتین 123 و حرف ك ي."
    out = norm(raw)
    assert "۱۲۳۴" in out and "ک" in out and "ی" in out
    assert "،" not in out and "." not in out


def test_stretching_and_redundant_marks():
    raw = "عاااالی!!!! ☺️"
    assert norm(raw) == "عالی"


def test_emoji_spacing_and_removal():
    raw = "عالیه😊برو"
    out = norm(raw)
    assert out == "عالیه برو"


def test_punctuation_removed_everywhere():
    raw = "سلام؟ خوبی! (امیدوارم، عالی باشی)."
    out = norm(raw)
    assert all(p not in out for p in "?!(),؛،«»")
    assert out == "سلام خوبی امیدوارم عالی باشی"


def test_url_mask_preserved_after_punct_removal():
    raw = "آدرس «www.foo.com/bar» را ببین."
    out = norm(raw)
    assert out == "آدرس [URL] را ببین"
