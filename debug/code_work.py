# -*- coding: utf-8 -*-

from pathlib_mate import Path
from afwf_aws_console.icons.gen_code import generate_architecture_icons_enum

dir_unzipped_asset = Path.home().joinpath("Downloads/Asset-Package_10232023.af3b989c8f30fad5f9c6161440af5cc2f0746e49")
generate_architecture_icons_enum(dir_unzipped_asset)

