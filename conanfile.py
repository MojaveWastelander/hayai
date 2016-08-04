from conans import ConanFile, CMake, tools
import os


class HayaiConan(ConanFile):
    name = "Hayai"
    version = "1.0.1"
    license = "LICENSE.md"
    url = "https://github.com/ebostijancic/hayai.git"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
       self.run("git clone https://github.com/ebostijancic/hayai.git")
       self.run("cd hayai && git checkout v1.0.1")
       # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
       # if the packaged project doesn't have variables to set it properly
       tools.replace_in_file("hayai/CMakeLists.txt", "PROJECT(hayai)", '''PROJECT(hayai)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self.settings)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        self.run('cmake hayai %s %s' % (cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", src="src", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hayai", "hayai_main"]
