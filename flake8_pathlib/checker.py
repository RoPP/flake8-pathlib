import ast
import typing
import dataclasses
import functools

import pkg_resources

pkg_name = "flake8-pathlib"
pkg_version = pkg_resources.get_distribution(pkg_name).version


@dataclasses.dataclass
class NameResolver(ast.NodeVisitor):
    import_alias: typing.Dict[str, str]
    _name: typing.List[str] = dataclasses.field(init=False, default_factory=list)

    @property
    def name(self) -> str:
        try:
            a = self.import_alias[self._name[-1]]
            self._name[-1] = a
        except (KeyError, IndexError):
            pass
        return ".".join(reversed(self._name))

    def visit_Name(self, node: ast.Name) -> None:
        self._name.append(node.id)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        try:
            self._name.append(node.attr)
            self._name.append(node.value.id)  # type: ignore
        except AttributeError:
            self.generic_visit(node)


@dataclasses.dataclass
class PathlibVisitor(ast.NodeVisitor):
    filename: str
    errors: typing.List["Error"] = dataclasses.field(default_factory=list)

    import_alias: typing.Dict[str, str] = dataclasses.field(
        init=False, default_factory=dict
    )

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for imp in node.names:
            if imp.asname:
                self.import_alias[imp.asname] = f"{node.module}.{imp.name}"
            else:
                self.import_alias[imp.name] = f"{node.module}.{imp.name}"

    def visit_Import(self, node: ast.Import) -> None:
        for imp in node.names:
            if imp.asname:
                self.import_alias[imp.asname] = imp.name

    def visit_Call(self, node: ast.Call) -> None:
        name_resolver = NameResolver(self.import_alias)
        name_resolver.visit(node.func)

        self.check_for_call_errors(node, name_resolver.name)

    def check_for_call_errors(self, node: ast.AST, name: str) -> None:
        try:
            partial_error = call_errors[name]
            self.errors.append(partial_error(lineno=node.lineno, col=node.col_offset))  # type: ignore
        except KeyError:
            pass


@dataclasses.dataclass
class PathlibChecker:
    name = pkg_name
    version = pkg_version

    tree: ast.AST
    filename: str = "(none)"
    visitor: typing.Type[PathlibVisitor] = dataclasses.field(
        init=False, default=PathlibVisitor
    )

    def run(self) -> typing.Iterable[typing.Tuple[int, int, str, type]]:
        visitor = self.visitor(filename=self.filename)
        visitor.visit(self.tree)
        for error in visitor.errors:
            yield error.as_flake8_tuple()


@dataclasses.dataclass
class Error:
    lineno: int
    col: int
    id: str
    message: str
    vars: typing.Dict[str, typing.Union[str, int]] = dataclasses.field(
        default_factory=dict
    )
    type = PathlibChecker

    def as_flake8_tuple(self) -> typing.Tuple[int, int, str, typing.Type]:
        return (
            self.lineno,
            self.col,
            (f"{self.id} {self.message}").format(**self.vars),
            self.type,
        )


partial_error = functools.partial(functools.partial, Error)
call_errors = {
    "os.path.abspath": partial_error(id="P100", message="os.path.abspath found"),
    "os.chmod": partial_error(id="P101", message="os.chmod found"),
    "os.mkdir": partial_error(id="P102", message="os.mkdir found"),
    "os.makedirs": partial_error(id="P103", message="os.makedirs found"),
    "os.rename": partial_error(id="P104", message="os.rename found"),
    "os.replace": partial_error(id="P105", message="os.replace found"),
    "os.rmdir": partial_error(id="P106", message="os.rmdir found"),
    "os.remove": partial_error(id="P107", message="os.remove found"),
    "os.unlink": partial_error(id="P108", message="os.unlink found"),
    "os.getcwd": partial_error(id="P109", message="os.getcwd found"),
    "os.path.exists": partial_error(id="P110", message="os.path.exists found"),
    "os.path.expanduser": partial_error(id="P111", message="os.path.expanduser found"),
    "os.path.isdir": partial_error(id="P112", message="os.path.isdir found"),
    "os.path.isfile": partial_error(id="P113", message="os.path.isfile found"),
    "os.path.islink": partial_error(id="P114", message="os.path.islink found"),
    "os.readlink": partial_error(id="P115", message="os.readlink found"),
    "os.stat": partial_error(id="P116", message="os.stat found"),
    "os.path.isabs": partial_error(id="P117", message="os.path.isabs found"),
    "os.path.join": partial_error(id="P118", message="os.path.join found"),
    "os.path.basename": partial_error(id="P119", message="os.path.basename found"),
    "os.path.dirname": partial_error(id="P120", message="os.path.dirname found"),
    "os.path.samefile": partial_error(id="P121", message="os.path.samefile found"),
    "os.path.splitext": partial_error(id="P122", message="os.path.splitext found"),
    "open": partial_error(
        id="P123", message="open('filename') found, use Path('filename').open() instead"
    ),
}
