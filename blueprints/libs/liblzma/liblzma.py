# -*- coding: utf-8 -*-
# Copyright Hannah von Reth <vonreth@kde.org>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

import info
from CraftCore import CraftCore
from Package.CMakePackageBase import CMakePackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        self.description = "free general-purpose data compression software with high compression ratio"
        self.webpage = "https://tukaani.org/xz"
        self.releaseManagerId = 5277
        self.targets["5.8.4"] = "https://github.com/tukaani-project/xz/releases/download/v5.8.4/xz-5.8.4.tar.xz"
        self.targetInstSrc["5.8.4"] = "xz-5.8.4"
        self.targetDigests["5.8.4"] = (["4ce24038fd4221e0d13bc1a2de7a4db56e90b92b3bf75321f6c14be73f65de4b"], CraftHash.HashAlgorithm.SHA256)
        self.defaultTarget = "5.8.4"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None

    def registerOptions(self):
        self.options.dynamic.registerOption("buildPrograms", not CraftCore.compiler.isAndroid)


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.configure.args += [
            "-DXZ_NLS=OFF",
            f"-DBUILD_TESTING={self.subinfo.options.dynamic.buildTests.asOnOff}",
        ]
        for tool in ["XZ", "XZDEC", "LZMADEC", "LZMAINFO", "SCRIPTS"]:
            self.subinfo.options.configure.args += [f"-DXZ_TOOL_{tool}={self.subinfo.options.dynamic.buildPrograms.asOnOff}"]
