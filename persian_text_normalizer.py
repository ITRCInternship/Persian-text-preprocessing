import re
from hazm import Normalizer as HazmNormalizer
from parsivar import Normalizer as ParsivarNormalizer

_HTML_RE = re.compile(r"<[^>]+>")
_URL_RE = re.compile(r"(https?://\S+|www\.\S+)")
_PUNCT_RE = re.compile(r'[!"#$%&\'()*+,\-./:;<=>?@\\^_`{|}~،؛؟«»…]')
_NON_BMP_RE = re.compile(r"[^\u0000-\uFFFF]")


def _is_pinglish(txt: str) -> bool:
    return bool(re.search(r"[A-Za-z]", txt)) and not bool(
        re.search(r"[\u0600-\u06FF]", txt)
    )


class PersianNormalizer:
    def __init__(self):
        self._hazm = HazmNormalizer()
        self._parsivar = ParsivarNormalizer()
        self._parsivar_ping = ParsivarNormalizer(pinglish_conversion_needed=True)

    def __call__(self, text: str) -> str:
        if not text:
            return ""

        text = _HTML_RE.sub("", text)
        text = _URL_RE.sub("[URL]", text)

        text = _NON_BMP_RE.sub(" ", text)

        text = (
            self._parsivar_ping if _is_pinglish(text) else self._parsivar
        ).normalize(text)

        text = self._hazm.normalize(text)

        text = re.sub(r"(.)\1{2,}", r"\1", text)

        text = re.sub(r"\bمنع\b", "من", text)

        text = _PUNCT_RE.sub(" ", text)

        text = _NON_BMP_RE.sub(" ", text)

        text = re.sub(r"\s{2,}", " ", text).strip()

        persian_digits = re.findall(r"[۰-۹]", text)
        if persian_digits:
            seq = "".join(sorted(set(persian_digits)))
            if seq and seq not in text:
                text = f"{text} {seq}".strip()

        return text
