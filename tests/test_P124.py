from pytest_flake8dir import Flake8Dir  # type: ignore


def test_full_name(flake8dir: Flake8Dir) -> None:
    flake8dir.make_example_py(
        """import py

p = py.path.local("../foo")
    """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./example.py:3:5: PL124 py.path.local is in maintenance mode, use pathlib instead",
    ]


def test_import_as(flake8dir: Flake8Dir) -> None:
    flake8dir.make_example_py(
        """import py.path as foo

p = foo.local("/foo")
    """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./example.py:3:5: PL124 py.path.local is in maintenance mode, use pathlib instead",
    ]


def test_from_import(flake8dir: Flake8Dir) -> None:
    flake8dir.make_example_py(
        """from py.path import local

p = local("/foo")
    """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./example.py:3:5: PL124 py.path.local is in maintenance mode, use pathlib instead",
    ]


def test_from_import_as(flake8dir: Flake8Dir) -> None:
    flake8dir.make_example_py(
        """from py.path import local as path

p = path("/foo")
    """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./example.py:3:5: PL124 py.path.local is in maintenance mode, use pathlib instead",
    ]
