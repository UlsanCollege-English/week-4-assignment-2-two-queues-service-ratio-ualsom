import pytest
from src.gate import Gate

def test_basic_fastpass_first():
    g = Gate()
    g.arrive("fastpass", "f1")
    g.arrive("regular", "r1")
    g.arrive("regular", "r2")
    g.arrive("regular", "r3")
    g.arrive("regular", "r4")

    assert g.serve() == "f1"
    assert g.serve() == "r1"
    assert g.serve() == "r2"
    assert g.serve() == "r3"
    assert g.serve() == "r4"

def test_empty_raises():
    g = Gate()
    with pytest.raises(IndexError):
        g.serve()

def test_peek_next_line():
    g = Gate()
    assert g.peek_next_line() is None
    g.arrive("regular", "r1")
    assert g.peek_next_line() == "regular"

def test_serve_pattern_loops_correctly():
    g = Gate()
    g.arrive("fastpass", "f1")
    g.arrive("fastpass", "f2")
    g.arrive("regular", "r1")
    g.arrive("regular", "r2")
    g.arrive("regular", "r3")
    g.arrive("regular", "r4")

    assert g.serve() == "f1"
    assert g.serve() == "r1"
    assert g.serve() == "r2"
    assert g.serve() == "r3"
    assert g.serve() == "f2"
    assert g.serve() == "r4"

def test_long_mixed_arrivals_and_service():
    g = Gate()
    # Add 6 regulars and 2 fastpass to match 8 expected serves
    for i in range(1, 7):
        g.arrive("regular", f"r{i}")
    g.arrive("fastpass", "f1")
    g.arrive("fastpass", "f2")

    served = []
    for _ in range(8):
        served.append(g.serve())

    # Expected serving order: F, R, R, R, F, R, R, R
    assert served == ["f1", "r1", "r2", "r3", "f2", "r4", "r5", "r6"]
