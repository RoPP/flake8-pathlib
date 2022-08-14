from pytest_flake8_path import Flake8Path


def test_noqa(flake8_path: Flake8Path) -> None:
    (flake8_path / "example.py").write_text(
        """import os.path

with open("foo") as fd:  # noqa: PL123
    print(fd)

os.path.exists("foo")  # noqa: PL110
"""
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == []
