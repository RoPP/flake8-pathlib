from pytest_flake8_path import Flake8Path


def test_full_name(flake8_path: Flake8Path) -> None:
    (flake8_path / "example.py").write_text(
        """import py

p = py.path.local("../foo")
"""
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == [
        "./example.py:3:5: PL124 py.path.local is in maintenance mode, use pathlib instead",
    ]


def test_import_as(flake8_path: Flake8Path) -> None:
    (flake8_path / "example.py").write_text(
        """import py.path as foo

p = foo.local("/foo")
"""
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == [
        "./example.py:3:5: PL124 py.path.local is in maintenance mode, use pathlib instead",
    ]


def test_from_import(flake8_path: Flake8Path) -> None:
    (flake8_path / "example.py").write_text(
        """from py.path import local

p = local("/foo")
"""
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == [
        "./example.py:3:5: PL124 py.path.local is in maintenance mode, use pathlib instead",
    ]


def test_from_import_as(flake8_path: Flake8Path) -> None:
    (flake8_path / "example.py").write_text(
        """from py.path import local as path

p = path("/foo")
"""
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == [
        "./example.py:3:5: PL124 py.path.local is in maintenance mode, use pathlib instead",
    ]
