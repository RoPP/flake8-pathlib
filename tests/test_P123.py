from pytest_flake8dir import Flake8Dir  # type: ignore


def test_open(flake8dir: Flake8Dir) -> None:
    flake8dir.make_example_py(
        """with open("foo") as fd:
    print(fd)
    """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./example.py:1:6: PL123 open('filename') found, use Path('filename').open() instead"
    ]
