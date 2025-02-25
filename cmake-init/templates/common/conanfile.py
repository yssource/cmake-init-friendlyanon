from conan import ConanFile


class Recipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps", "VirtualRunEnv"{% if not catch3 %}
    default_options = {
        "catch2/*:with_main": True,
    }{% end %}

    def layout(self):
        self.folders.generators = "conan"

    def requirements(self):{% if c %}{% if exe %}
        self.requires("hedley/15"){% end %}
        self.requires("json-c/0.16"){% else %}
        self.requires("fmt/9.1.0"){% end %}

    def build_requirements(self):{% if catch3 %}
        self.test_requires("catch2/3.3.1"){% else %}
        self.test_requires("catch2/2.13.9"){% end %}
