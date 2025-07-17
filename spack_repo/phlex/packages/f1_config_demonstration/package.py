# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *
from spack_repo.fnal_art.packages.fnal_github_package.package import *


class F1ConfigDemonstration(CMakePackage, FnalGithubPackage):
    """A demonstration of multi-language configuration handling for Phlex."""

    homepage = "https://github.com/Framework-R-D/dune-framework-design/"
    repo = "Framework-R-D/dune-framework-design"

    git_sparse_paths=["f1_config_demonstration"]

    maintainers("greenc-FNAL", "knoepfel")

    license("Apache-2.0", checked_by="greenc-FNAL")

    version("develop", branch="main", get_full_repo=True)

    depends_on("cxx", type="build")

    depends_on("py-fhicl-py@4.04:4 cxxstd=20")
    depends_on("fhicl-cpp@4.19:4 cxxstd=20")
    depends_on("jsonnet@0.21:")
    depends_on("python@3.9:3")

    conflicts("%gcc@:13")

    @cmake_preset
    def cmake_args(self):
        return []
