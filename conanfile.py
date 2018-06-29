from conans import ConanFile, CMake
from conans.errors import ConanException
import os


class XmscoreConan(ConanFile):
    name = "xmscore"
    version = None
    license = "XMSNG Software License"
    url = "https://github.com/Aquaveo/xmscore"
    description = "Support library for XMS products"
    settings = "os", "compiler", "build_type", "arch"
    options = {"xms": [True, False], "pybind": [True, False]}
    default_options = "xms=False", "pybind=False"
    generators = "cmake", "txt"
    build_requires = "cxxtest/4.4@aquaveo/stable"
    exports = "CMakeLists.txt", "LICENSE"
    exports_sources = "xmscore/*"

    def configure(self):
        # Set version dynamically using XMS_VERSION env variable.
        self.version = self.env.get('XMS_VERSION', 'master')

        # Raise ConanExceptions for Unsupported Versions
        s_os = self.settings.os
        s_compiler = self.settings.compiler
        s_compiler_version = self.settings.compiler.version

        if s_compiler != "Visual Studio":
            self.options['boost'].fPIC = True

        if s_compiler == "clang" and s_os == 'Linux':
            raise ConanException("Clang on Linux is not supported.")

        if s_compiler == "gcc" and float(s_compiler_version.value) < 5.0:
            raise ConanException("GCC < 5.0 is not supported.")

        if s_compiler == "clang" and s_os == 'Darwin' and float(s_compiler_version.value) < 9.0:
            raise ConanException("Clang > 9.0 is required for Mac.")

    def requirements(self):
        if self.options.xms:
            self.requires("boost/1.60.0@aquaveo/testing")
        else:
            self.requires("boost/1.66.0@conan/stable")
        self.requires("pybind11/2.2.2@aquaveo/stable")

    def build(self):
        xms_run_tests = self.env.get('XMS_RUN_TESTS', None)
        run_tests = xms_run_tests != 'None' and xms_run_tests is not None

        cmake = CMake(self)

        if self.settings.compiler == 'Visual Studio':
            cmake.definitions["XMS_BUILD"] = self.options.xms

        cmake.definitions["IS_PYTHON_BUILD"] = self.options.pybind

        cmake.definitions["BUILD_TESTING"] = run_tests
        cmake.configure(source_folder=".")
        cmake.build()

        if run_tests:
            print("***********(0.0)*************")
            try:
                cmake.test()
            except ConanException:
                raise
            finally:
                if os.path.isfile("TEST-cxxtest.xml"):
                    with open("TEST-cxxtest.xml", "r") as f:
                        for line in f.readlines():
                            no_newline = line.strip('\n')
                            print(no_newline)
                print("***********(0.0)*************")

    def package(self):
        self.copy("*.h", dst="include/xmscore", src="xmscore")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("license", dst="licenses", ignore_case=True, keep_path=False)

    def package_info(self):
        if self.settings.build_type == 'Debug':
            self.cpp_info.libs = ["xmscore_d"]
        else:
            self.cpp_info.libs = ["xmscore"]
