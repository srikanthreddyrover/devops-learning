import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import greet


def test_greet():
    result = greet("Srikanth")
    assert result == "Hello, Srikanth! Welcome to DevOps."
