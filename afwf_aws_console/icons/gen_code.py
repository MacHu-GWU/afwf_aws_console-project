# -*- coding: utf-8 -*-

import typing as T
import jinja2
from pathlib_mate import Path

from ..vendor.strutils import slugify
from ..paths import (
    dir_icons,
    dir_asset,
    path_enum_arch_group,
    path_enum_arch_service,
    path_enum_category,
    path_enum_resource,
)

path_enum_py_jinja = dir_icons.joinpath("enum.py.jinja")


def to_snake_case(s: str) -> str:
    return slugify(s, delim="_")


def copy_to(src: Path, dst: Path):
    try:
        src.copyto(dst, overwrite=True)
    except FileNotFoundError:
        dst.parent.mkdir(parents=True)
        src.copyto(dst, overwrite=True)


def generate_architecture_icons_enum(dir_unzipped_asset: Path):
    """
    Recursively scan the unzipped asset directory, and generate the enum for architecture icons.

    - https://aws.amazon.com/architecture/icons/
    """

    def locate_sub_folder(name: str) -> T.Optional[Path]:
        for dir_sub_folder in dir_unzipped_asset.iterdir():
            if dir_sub_folder.basename.startswith(name):
                return dir_sub_folder
        return None

    dir_arch_group = locate_sub_folder("Architecture-Group")
    dir_arch_service = locate_sub_folder("Architecture-Service")
    dir_category = locate_sub_folder("Category")
    dir_resource = locate_sub_folder("Resource")

    enum_template = jinja2.Template(path_enum_py_jinja.read_text())

    if dir_arch_group:
        class_name = "ArchGroupIconEnum"
        pairs = list()
        for p in dir_arch_group.select_by_ext(".png", recursive=False):
            if "_32." in p.basename:
                attr = to_snake_case(p.fname.replace("_32", ""))
                relpath = p.relative_to(dir_unzipped_asset)
                pairs.append((attr, relpath))
                # print(attr, relpath)
                new_p = dir_asset.joinpath(relpath)
                copy_to(p, new_p)
        content = enum_template.render(class_name=class_name, pairs=pairs)
        path_enum_arch_group.write_text(content)

    if dir_arch_service:
        class_name = "ArchServiceIconEnum"
        pairs = list()
        for p in dir_arch_service.select_by_ext(".png", recursive=True):
            if "_64." in p.basename:
                attr = to_snake_case(p.fname.replace("_64", ""))
                relpath = p.relative_to(dir_unzipped_asset)
                pairs.append((attr, relpath))
                # print(attr, relpath)
                new_p = dir_asset.joinpath(relpath)
                copy_to(p, new_p)
        content = enum_template.render(class_name=class_name, pairs=pairs)
        path_enum_arch_service.write_text(content)

    if dir_category:
        class_name = "CategoryIconEnum"
        pairs = list()
        for p in dir_category.select_by_ext(".png", recursive=True):
            if "_64." in p.basename:
                attr = to_snake_case(p.fname.replace("_64", ""))
                relpath = p.relative_to(dir_unzipped_asset)
                pairs.append((attr, relpath))
                # print(attr, relpath)
                new_p = dir_asset.joinpath(relpath)
                copy_to(p, new_p)
        content = enum_template.render(class_name=class_name, pairs=pairs)
        path_enum_category.write_text(content)

    if dir_resource:
        class_name = "ResourceIconEnum"
        pairs = list()
        for p in dir_resource.select_by_ext(".png", recursive=True):
            if "_48." in p.basename:
                attr = to_snake_case(p.fname.replace("_48", ""))
                relpath = p.relative_to(dir_unzipped_asset)
                pairs.append((attr, relpath))
                # print(attr, relpath)
                new_p = dir_asset.joinpath(relpath)
                copy_to(p, new_p)
        content = enum_template.render(class_name=class_name, pairs=pairs)
        path_enum_resource.write_text(content)
