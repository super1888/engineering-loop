"""Small static structural check; does not claim browser validation."""

from html.parser import HTMLParser
from pathlib import Path


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.controls = []

    def handle_starttag(self, tag, attrs):
        if tag in {"input", "button", "label"}:
            self.controls.append((tag, dict(attrs)))


page = Page()
page.feed(Path(__file__).with_name("index.html").read_text(encoding="utf-8"))
assert page.controls == [
    ("label", {"for": "description"}),
    ("input", {"id": "description", "name": "description", "required": None}),
    ("button", {"id": "save", "type": "submit"}),
], "Form control semantics changed"
print("Static form structure passed; browser behavior was not tested.")
