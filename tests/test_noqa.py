from pytest_flake8dir import Flake8Dir  # type: ignore


def test_noqa(flake8dir: Flake8Dir) -> None:
    flake8dir.make_example_py(
        """import os.path

with open("foo") as fd:  # noqa: P123
    print(fd)

os.path.exists("foo")  # noqa: P110
    """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []
