from pathlib import Path

import pytest

from dianpy import Meet

FIXTURES_DIR = Path("tests/fixtures")

FIXTURE_PATHS = [
    p for p in FIXTURES_DIR.rglob("*")
    if p.is_file() and p.suffix.lower() in {".swimming", ".xml"}
] if FIXTURES_DIR.exists() else []


@pytest.mark.skipif(not FIXTURE_PATHS, reason="No fixtures found")
@pytest.mark.parametrize("path", FIXTURE_PATHS)
def test_fixture_roundtrip(path: Path):
    Meet.from_xml(Path(path).read_bytes())
