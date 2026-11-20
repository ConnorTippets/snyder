from dataclasses import dataclass


@dataclass
class Element:
    tag: str
    inner_html: str
    children: list[Element]
