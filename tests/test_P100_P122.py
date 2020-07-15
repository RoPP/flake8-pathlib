from pytest_flake8dir import Flake8Dir  # type: ignore


def test_full_name(flake8dir: Flake8Dir) -> None:
    flake8dir.make_example_py(
        """import os
import os.path

p = "/foo"

a = os.path.abspath(p)
aa = os.chmod(p)
aaa = os.mkdir(p)
os.makedirs(p)
os.rename(p)
os.replace(p)
os.rmdir(p)
os.remove(p)
os.unlink(p)
os.getcwd(p)
b = os.path.exists(p)
bb = os.path.expanduser(p)
bbb = os.path.isdir(p)
bbbb = os.path.isfile(p)
bbbbb = os.path.islink(p)
os.readlink(p)
os.stat(p)
os.path.isabs(p)
os.path.join(p)
os.path.basename(p)
os.path.dirname(p)
os.path.samefile(p)
os.path.splitext(p)
    """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        './example.py:6:5: PL100 os.path.abspath("foo") should be replaced by foo_path.resolve()',
        './example.py:7:6: PL101 os.chmod("foo", 0o444) should be replaced by foo_path.chmod(0o444)',
        './example.py:8:7: PL102 os.mkdir("foo") should be replaced by foo_path.mkdir()',
        './example.py:9:1: PL103 os.makedirs("foo/bar") should be replaced by bar_path.mkdir(parents=True)',
        './example.py:10:1: PL104 os.rename("foo", "bar") should be replaced by foo_path.rename(Path("bar"))',
        './example.py:11:1: PL105 os.replace("foo", "bar") should be replaced by foo_path.replace(Path("bar"))',
        './example.py:12:1: PL106 os.rmdir("foo") should be replaced by foo_path.rmdir()',
        './example.py:13:1: PL107 os.remove("foo") should be replaced by foo_path.unlink()',
        './example.py:14:1: PL108 os.unlink("foo") should be replaced by foo_path.unlink()',
        "./example.py:15:1: PL109 os.getcwd() should be replaced by Path.cwd()",
        './example.py:16:5: PL110 os.path.exists("foo") should be replaced by foo_path.exists()',
        './example.py:17:6: PL111 os.path.expanduser("~/foo") should be replaced by foo_path.expanduser()',
        './example.py:18:7: PL112 os.path.isdir("foo") should be replaced by foo_path.is_dir()',
        './example.py:19:8: PL113 os.path.isfile("foo") should be replaced by foo_path.is_file()',
        './example.py:20:9: PL114 os.path.islink("foo") should be replaced by foo_path.is_symlink()',
        './example.py:21:1: PL115 os.readlink("foo") should be replaced by foo_path.readlink()',
        './example.py:22:1: PL116 os.stat("foo") should be replaced by foo_path.stat() or '
        "foo_path.owner() or foo_path.group()",
        "./example.py:23:1: PL117 os.path.isabs should be replaced by foo_path.is_absolute()",
        './example.py:24:1: PL118 os.path.join("foo", "bar") should be replaced by foo_path / "bar"',
        './example.py:25:1: PL119 os.path.basename("foo/bar") should be replaced by bar_path.name',
        './example.py:26:1: PL120 os.path.dirname("foo/bar") should be replaced by bar_path.parent',
        './example.py:27:1: PL121 os.path.samefile("foo", "bar") should be replaced by foo_path.samefile(bar_path)',
        './example.py:28:1: PL122 os.path.splitext("foo.bar") should be replaced by foo_path.suffix',
    ]


def test_import_as(flake8dir: Flake8Dir) -> None:
    flake8dir.make_example_py(
        """import os as foo
import os.path as foo_p

p = "/foo"

a = foo_p.abspath(p)
aa = foo.chmod(p)
aaa = foo.mkdir(p)
foo.makedirs(p)
foo.rename(p)
foo.replace(p)
foo.rmdir(p)
foo.remove(p)
foo.unlink(p)
foo.getcwd(p)
b = foo_p.exists(p)
bb = foo_p.expanduser(p)
bbb = foo_p.isdir(p)
bbbb = foo_p.isfile(p)
bbbbb = foo_p.islink(p)
foo.readlink(p)
foo.stat(p)
foo_p.isabs(p)
foo_p.join(p)
foo_p.basename(p)
foo_p.dirname(p)
foo_p.samefile(p)
foo_p.splitext(p)
    """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        './example.py:6:5: PL100 os.path.abspath("foo") should be replaced by foo_path.resolve()',
        './example.py:7:6: PL101 os.chmod("foo", 0o444) should be replaced by foo_path.chmod(0o444)',
        './example.py:8:7: PL102 os.mkdir("foo") should be replaced by foo_path.mkdir()',
        './example.py:9:1: PL103 os.makedirs("foo/bar") should be replaced by bar_path.mkdir(parents=True)',
        './example.py:10:1: PL104 os.rename("foo", "bar") should be replaced by foo_path.rename(Path("bar"))',
        './example.py:11:1: PL105 os.replace("foo", "bar") should be replaced by foo_path.replace(Path("bar"))',
        './example.py:12:1: PL106 os.rmdir("foo") should be replaced by foo_path.rmdir()',
        './example.py:13:1: PL107 os.remove("foo") should be replaced by foo_path.unlink()',
        './example.py:14:1: PL108 os.unlink("foo") should be replaced by foo_path.unlink()',
        "./example.py:15:1: PL109 os.getcwd() should be replaced by Path.cwd()",
        './example.py:16:5: PL110 os.path.exists("foo") should be replaced by foo_path.exists()',
        './example.py:17:6: PL111 os.path.expanduser("~/foo") should be replaced by foo_path.expanduser()',
        './example.py:18:7: PL112 os.path.isdir("foo") should be replaced by foo_path.is_dir()',
        './example.py:19:8: PL113 os.path.isfile("foo") should be replaced by foo_path.is_file()',
        './example.py:20:9: PL114 os.path.islink("foo") should be replaced by foo_path.is_symlink()',
        './example.py:21:1: PL115 os.readlink("foo") should be replaced by foo_path.readlink()',
        './example.py:22:1: PL116 os.stat("foo") should be replaced by foo_path.stat() or '
        "foo_path.owner() or foo_path.group()",
        "./example.py:23:1: PL117 os.path.isabs should be replaced by foo_path.is_absolute()",
        './example.py:24:1: PL118 os.path.join("foo", "bar") should be replaced by foo_path / "bar"',
        './example.py:25:1: PL119 os.path.basename("foo/bar") should be replaced by bar_path.name',
        './example.py:26:1: PL120 os.path.dirname("foo/bar") should be replaced by bar_path.parent',
        './example.py:27:1: PL121 os.path.samefile("foo", "bar") should be replaced by foo_path.samefile(bar_path)',
        './example.py:28:1: PL122 os.path.splitext("foo.bar") should be replaced by foo_path.suffix',
    ]


def test_from_import(flake8dir: Flake8Dir) -> None:
    flake8dir.make_example_py(
        """from os import chmod, mkdir, makedirs, rename, replace, rmdir
from os import remove, unlink, getcwd, readlink, stat
from os.path import abspath, exists, expanduser, isdir, isfile, islink
from os.path import isabs, join, basename, dirname, samefile, splitext

p = "/foo"

a = abspath(p)
aa = chmod(p)
aaa = mkdir(p)
makedirs(p)
rename(p)
replace(p)
rmdir(p)
remove(p)
unlink(p)
getcwd(p)
b = exists(p)
bb = expanduser(p)
bbb = isdir(p)
bbbb = isfile(p)
bbbbb = islink(p)
readlink(p)
stat(p)
isabs(p)
join(p)
basename(p)
dirname(p)
samefile(p)
splitext(p)
    """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        './example.py:8:5: PL100 os.path.abspath("foo") should be replaced by foo_path.resolve()',
        './example.py:9:6: PL101 os.chmod("foo", 0o444) should be replaced by foo_path.chmod(0o444)',
        './example.py:10:7: PL102 os.mkdir("foo") should be replaced by foo_path.mkdir()',
        './example.py:11:1: PL103 os.makedirs("foo/bar") should be replaced by bar_path.mkdir(parents=True)',
        './example.py:12:1: PL104 os.rename("foo", "bar") should be replaced by foo_path.rename(Path("bar"))',
        './example.py:13:1: PL105 os.replace("foo", "bar") should be replaced by foo_path.replace(Path("bar"))',
        './example.py:14:1: PL106 os.rmdir("foo") should be replaced by foo_path.rmdir()',
        './example.py:15:1: PL107 os.remove("foo") should be replaced by foo_path.unlink()',
        './example.py:16:1: PL108 os.unlink("foo") should be replaced by foo_path.unlink()',
        "./example.py:17:1: PL109 os.getcwd() should be replaced by Path.cwd()",
        './example.py:18:5: PL110 os.path.exists("foo") should be replaced by foo_path.exists()',
        './example.py:19:6: PL111 os.path.expanduser("~/foo") should be replaced by foo_path.expanduser()',
        './example.py:20:7: PL112 os.path.isdir("foo") should be replaced by foo_path.is_dir()',
        './example.py:21:8: PL113 os.path.isfile("foo") should be replaced by foo_path.is_file()',
        './example.py:22:9: PL114 os.path.islink("foo") should be replaced by foo_path.is_symlink()',
        './example.py:23:1: PL115 os.readlink("foo") should be replaced by foo_path.readlink()',
        './example.py:24:1: PL116 os.stat("foo") should be replaced by foo_path.stat() or '
        "foo_path.owner() or foo_path.group()",
        "./example.py:25:1: PL117 os.path.isabs should be replaced by foo_path.is_absolute()",
        './example.py:26:1: PL118 os.path.join("foo", "bar") should be replaced by foo_path / "bar"',
        './example.py:27:1: PL119 os.path.basename("foo/bar") should be replaced by bar_path.name',
        './example.py:28:1: PL120 os.path.dirname("foo/bar") should be replaced by bar_path.parent',
        './example.py:29:1: PL121 os.path.samefile("foo", "bar") should be replaced by foo_path.samefile(bar_path)',
        './example.py:30:1: PL122 os.path.splitext("foo.bar") should be replaced by foo_path.suffix',
    ]


def test_from_import_as(flake8dir: Flake8Dir) -> None:
    flake8dir.make_example_py(
        """from os import chmod as xchmod, mkdir as xmkdir
from os import makedirs as xmakedirs, rename as xrename, replace as xreplace
from os import rmdir as xrmdir, remove as xremove, unlink as xunlink
from os import getcwd as xgetcwd, readlink as xreadlink, stat as xstat
from os.path import abspath as xabspath, exists as xexists
from os.path import expanduser as xexpanduser, isdir as xisdir
from os.path import isfile as xisfile, islink as xislink, isabs as xisabs
from os.path import join as xjoin, basename as xbasename, dirname as xdirname
from os.path import samefile as xsamefile, splitext as xsplitext

p = "/foo"

a = xabspath(p)
aa = xchmod(p)
aaa = xmkdir(p)
xmakedirs(p)
xrename(p)
xreplace(p)
xrmdir(p)
xremove(p)
xunlink(p)
xgetcwd(p)
b = xexists(p)
bb = xexpanduser(p)
bbb = xisdir(p)
bbbb = xisfile(p)
bbbbb = xislink(p)
xreadlink(p)
xstat(p)
xisabs(p)
xjoin(p)
xbasename(p)
xdirname(p)
xsamefile(p)
xsplitext(p)
    """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        './example.py:13:5: PL100 os.path.abspath("foo") should be replaced by foo_path.resolve()',
        './example.py:14:6: PL101 os.chmod("foo", 0o444) should be replaced by foo_path.chmod(0o444)',
        './example.py:15:7: PL102 os.mkdir("foo") should be replaced by foo_path.mkdir()',
        './example.py:16:1: PL103 os.makedirs("foo/bar") should be replaced by bar_path.mkdir(parents=True)',
        './example.py:17:1: PL104 os.rename("foo", "bar") should be replaced by foo_path.rename(Path("bar"))',
        './example.py:18:1: PL105 os.replace("foo", "bar") should be replaced by foo_path.replace(Path("bar"))',
        './example.py:19:1: PL106 os.rmdir("foo") should be replaced by foo_path.rmdir()',
        './example.py:20:1: PL107 os.remove("foo") should be replaced by foo_path.unlink()',
        './example.py:21:1: PL108 os.unlink("foo") should be replaced by foo_path.unlink()',
        "./example.py:22:1: PL109 os.getcwd() should be replaced by Path.cwd()",
        './example.py:23:5: PL110 os.path.exists("foo") should be replaced by foo_path.exists()',
        './example.py:24:6: PL111 os.path.expanduser("~/foo") should be replaced by foo_path.expanduser()',
        './example.py:25:7: PL112 os.path.isdir("foo") should be replaced by foo_path.is_dir()',
        './example.py:26:8: PL113 os.path.isfile("foo") should be replaced by foo_path.is_file()',
        './example.py:27:9: PL114 os.path.islink("foo") should be replaced by foo_path.is_symlink()',
        './example.py:28:1: PL115 os.readlink("foo") should be replaced by foo_path.readlink()',
        './example.py:29:1: PL116 os.stat("foo") should be replaced by foo_path.stat() '
        "or foo_path.owner() or foo_path.group()",
        "./example.py:30:1: PL117 os.path.isabs should be replaced by foo_path.is_absolute()",
        './example.py:31:1: PL118 os.path.join("foo", "bar") should be replaced by foo_path / "bar"',
        './example.py:32:1: PL119 os.path.basename("foo/bar") should be replaced by bar_path.name',
        './example.py:33:1: PL120 os.path.dirname("foo/bar") should be replaced by bar_path.parent',
        './example.py:34:1: PL121 os.path.samefile("foo", "bar") should be replaced by foo_path.samefile(bar_path)',
        './example.py:35:1: PL122 os.path.splitext("foo.bar") should be replaced by foo_path.suffix',
    ]
