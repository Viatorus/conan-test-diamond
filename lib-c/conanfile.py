from conans import ConanFile


class Lib(ConanFile):
    name = "lib-c"
    version = "0.0.1"
    requires = "lib-a/[0]"
