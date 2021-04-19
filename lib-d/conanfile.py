from conans import ConanFile


class Lib(ConanFile):
    name = "lib-d"
    version = "0.0.1"
    requires = "lib-b/0.0.1", "lib-c/0.0.1"
