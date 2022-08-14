from pytest_flake8_path import Flake8Path


def test_open(flake8_path: Flake8Path) -> None:
    (flake8_path / "example.py").write_text(
        """with open("foo") as fd:
    print(fd)
"""
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == [
        './example.py:1:6: PL123 open("foo") should be replaced by Path("foo").open()'
    ]
