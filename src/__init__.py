from .dom import Element


class ParseError(Exception): ...


class Parser:
    source: str
    i: int

    def peek(self, ahead: int = 0) -> str:
        try:
            return self.source[self.i + ahead]
        except IndexError:
            return ""

    def consume(self) -> str:
        try:
            tmp = self.source[self.i]
            self.i += 1
            return tmp
        except IndexError:
            return ""

    def consume_whitespace(self):
        while self.peek().isspace():
            self.consume()

    def expect(self, char: str):
        if not self.peek() == char:
            raise ParseError(f"Expected '{char}'")

        self.consume()

    def consume_until_not_alnum(self, err: str) -> str:
        if not self.peek().isalpha():
            raise ParseError(err)

        out = ""
        while self.peek().isalnum() or self.peek() in ("-", "_", "."):
            out = out + self.consume()

        return out

    def expect_whitespace(self):
        if not self.peek().isspace():
            raise ParseError("Expected whitespace")

        self.consume()

    def parse_element(self) -> Element:
        self.expect("<")
        self.consume_whitespace()
        tag = self.consume_until_not_alnum("Expected tag name")

        if not self.peek() == ">":
            self.expect_whitespace()
            self.consume_whitespace()
        self.expect(">")

        print(tag)
        print(repr(self.peek()))

    def parse_html(self, source: str) -> Element:
        self.source = source
        self.i = 0

        root = Element("", source, [])

        self.parse_element()
