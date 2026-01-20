# DianPy

DianPy is a small helper library for reading and writing swimming meet files produced by the Dian scoreboard software. It wraps `pydantic-xml` models so you can load an event program from XML/`.swimming` files, inspect or edit it in Python, and write it back.

## Installation

```bash
pip install dianpy
```

For local development:

```bash
poetry install
```

## Quick start

```python
from dianpy import fromfile, tofile, Meet

# Load a meet from a Dian XML/.swimming file
meet: Meet = fromfile("tests/fixtures/sample-meet-01.swimming")

# Inspect fields
print(meet.name, meet.course, len(meet.events))

# Modify data (example: mark first athlete disqualified)
first_event = meet.events[0]
first_event.athletes[0].disqualification = "DSQ"

# Save back to disk
tofile(meet, "out.swimming")
```

Models live in `dianpy.meet`, `dianpy.event`, and `dianpy.athlete`. Empty or missing gender fields are normalized to mixed (`"X"`), and several timing fields default to empty strings to accommodate real-world files.

## Tests

Fixture round-trip tests ensure the bundled sample files stay parseable:

```bash
poetry run pytest
```
