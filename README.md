# flake8-use-pathlib

[![pypi][pypi-badge]](https://pypi.org/project/flake8-use-pathlib/)
[![black][black-badge]](https://github.com/psf/black)

A plugin for flake8 finding use of functions that can be replaced by pathlib module.

[pypi-badge]: https://badgen.net/pypi/v/flake8-use-pathlib
[black-badge]: https://badgen.net/badge/code%20style/black/black/

## Installation

Install from `pip` with:

`pip install flake8-use-pathlib`

## Rules

| Code  | Rule                                                                                         |
| ----- | -------------------------------------------------------------------------------------------- |
| PL100 | os.path.abspath("foo") should be replaced by foo_path.resolve()                              |
| PL101 | os.chmod("foo", 0o444) should be replaced by foo_path.chmod(0o444)                           |
| PL102 | os.mkdir("foo") should be replaced by foo_path.mkdir()                                       |
| PL103 | os.makedirs("foo/bar") should be replaced by bar_path.mkdir(parents=True)                    |
| PL104 | os.rename("foo", "bar") should be replaced by foo_path.rename(Path("bar"))                   |
| PL105 | os.replace("foo", "bar") should be replaced by foo_path.replace(Path("bar"))                 |
| PL106 | os.rmdir("foo") should be replaced by foo_path.rmdir()                                       |
| PL107 | os.remove("foo") should be replaced by foo_path.unlink()                                     |
| PL108 | os.unlink("foo") should be replaced by foo_path.unlink()                                     |
| PL109 | os.getcwd() should be replaced by Path.cwd()                                                 |
| PL110 | os.path.exists("foo") should be replaced by foo_path.exists()                                |
| PL111 | os.path.expanduser("~/foo") should be replaced by foo_path.expanduser()                      |
| PL112 | os.path.isdir("foo") should be replaced by foo_path.is_dir()                                 |
| PL113 | os.path.isfile("foo") should be replaced by foo_path.is_file()                               |
| PL114 | os.path.islink("foo") should be replaced by foo_path.is_symlink()                            |
| PL115 | os.readlink("foo") should be replaced by foo_path.readlink()                                 |
| PL116 | os.stat("foo") should be replaced by foo_path.stat() or foo_path.owner() or foo_path.group() |
| PL117 | os.path.isabs should be replaced by foo_path.is_absolute()                                   |
| PL118 | os.path.join("foo", "bar") should be replaced by foo_path / "bar"                            |
| PL119 | os.path.basename("foo/bar") should be replaced by bar_path.name                              |
| PL120 | os.path.dirname("foo/bar") should be replaced by bar_path.parent                             |
| PL121 | os.path.samefile("foo", "bar") should be replaced by foo_path.samefile(bar_path)             |
| PL122 | os.path.splitext("foo.bar") should be replaced by foo_path.suffix                            |
| PL123 | open("foo") should be replaced by Path("foo").open()                                         |
| PL124 | py.path.local is in maintenance mode, use pathlib instead                                    |
