from conans import ConanFile


class Lib(ConanFile):
    name = "lib-b"
    version = "0.0.1"
    requires = "lib-a/0.0.1"
