from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field, fields
from dataclasses import replace

@dataclass
class Card:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        return Card(**d)

    def to_dict(self):
        return asdict(self)


def test_field_access():
    c = Card("something", "brian", "todo", 123)
    assert c.summary == "something"
    assert c.owner == "brian"
    assert c.state == "todo"
    assert c.id == 123


def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_equality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian", "todo", 123)
    assert c1 == c2


def test_equality_with_diff_ids():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian", "todo", 4567)
    assert c1 == c2


def test_inequality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("completely different", "okken", "done", 123)
    assert c1 != c2


def test_from_dict():
    c1 = Card("something", "brian", "todo", 123)
    c2_dict = {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123,
    }
    c2 = Card.from_dict(c2_dict)
    assert c1 == c2


def test_to_dict():
    c1 = Card("something", "brian", "todo", 123)
    c2 = c1.to_dict()
    c2_expected = {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123,
    }
    assert c2 == c2_expected


def test_direct_copy():
    c1 = Card("something", "brian", "todo", 123)
    c2 = c1

    assert c2 == c1


def test_direct_copy_mod_origin():
    c1 = Card("something", "brian", "todo", 123)
    c2 = c1

    c1.summary = "completely different"
    c1.owner = "okken"
    c1.state = "done"

    assert c2 == c1


def test_direct_copy_mod_copy():
    c1 = Card("something", "brian", "todo", 123)
    c2 = c1

    c2.summary = "completely different"
    c2.owner = "okken"
    c2.state = "done"

    assert c2 == c1


def test_iterative_copy():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card()

    for f in fields(Card):
        setattr(c2, f.name, getattr(c1, f.name))

    assert c2 == c1


def test_iterative_copy_mod_origin():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card()

    for f in fields(Card):
        setattr(c2, f.name, getattr(c1, f.name))

    c1.summary = "completely different"
    c1.owner = "okken"
    c1.state = "done"

    assert c2 != c1


def test_iterative_copy_mod_copy():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card()

    for f in fields(Card):
        setattr(c2, f.name, getattr(c1, f.name))

    c2.summary = "completely different"
    c2.owner = "okken"
    c2.state = "done"

    assert c2 != c1

def test_replace_copy():
    c1 = Card("something", "brian", "todo", 123)
    c2 = replace(c1)

    assert c2 == c1


def test_replace_copy_mod_origin():
    c1 = Card("something", "brian", "todo", 123)
    c2 = replace(c1)

    c1.summary = "completely different"
    c1.owner = "okken"
    c1.state = "done"

    assert c2 != c1


def test_replace_copy_mod_copy():
    c1 = Card("something", "brian", "todo", 123)
    c2 = replace(c1)

    c2.summary = "completely different"
    c2.owner = "okken"
    c2.state = "done"

    assert c2 != c1
