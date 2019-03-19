import sys
import idaapi

import ifred.plugins.packagemanager
from ifred.package.package import LocalPackage

class PackageManager(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX | idaapi.PLUGIN_HIDE
    comment = "Package Manager"
    help = "Package Manager for IDA Pro"
    wanted_name = "Package Manager"
    wanted_hotkey = ""

    def init(self):
        for pkg in LocalPackage.all():
            pkg.load()
        return idaapi.PLUGIN_OK

    def run(self, arg):
        pass

    def term(self):
        pass


def PLUGIN_ENTRY():
    return PackageManager()
