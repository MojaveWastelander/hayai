from conans import ConanFile, CMake, tools
import os

channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "ebostijancic")

class HayaitestConan(ConanFile):
    name = "HayaiTest"
    version = "0.0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "Hayai/1.0.1@%s/%s" % (username, channel)

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        self.run(os.sep.join([".","bin", "hayai_test"]))