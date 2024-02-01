# -*- coding: utf-8 -*-

"""
"""

import typing as T
import attrs
import afwf.api as afwf

from aws_console_url_search.api import (
    BaseModel,
    Service,
    Menu,
    load_data,
    preprocess_query,
    ServiceDocument,
    service_downloader,
    service_index_name,
    service_dataset,
    RegionDocument,
    region_downloader,
    region_index_name,
    region_dataset,
)
from aws_console_url_search.ui_def import ConsoleUrlItem
from aws_console_url_search.ui_init import ui

from ..icons.icon_mapping import id_to_icon

try:
    from rich import print as rprint
except ImportError:
    pass


def get_icon_by_key(mapper: dict, key: str) -> T.Optional[afwf.Icon]:
    if key in mapper:
        return afwf.Icon.from_image_file(mapper[key])
    else:
        return None


T_ACS_ITEM = T.Union[
    ConsoleUrlItem,
]


@attrs.define
class Item(afwf.Item):
    def copy_arn(self, arn: str):
        self.variables["copy_arn"] = "y"
        self.variables["copy_arn_arg"] = arn
        return self

    def copy_id(self, id: str):
        self.variables["copy_id"] = "y"
        self.variables["copy_id_arg"] = id
        return self

    def copy_name(self, name: str):
        self.variables["copy_name"] = "y"
        self.variables["copy_name_arg"] = name
        return self

    @classmethod
    def from_console_url_item(cls, item: ConsoleUrlItem):
        """
        .. note::

            The aws_resource_search cli allow user to use F1 to see detail,
            but we don't want to add this feature in alfred workflow.
            The zelfred framework allows us to use shortcut key to enter
            a sub-session, but sub-session in alfred is another script filter,
            which greatly increase the complexity.
        """
        afwf_item = cls(
            title=item.title,
            subtitle=item.subtitle,
            # uid=item.uid,
            arg=item.variables["url"],
            autocomplete=item.autocomplete,
        ).open_url(item.variables["url"])
        path = id_to_icon(item.variables["doc"].id)
        if path is not None:
            afwf_item.set_icon(str(path))
        return afwf_item

    @classmethod
    def from_acs_item(cls, item: T_ACS_ITEM):
        if isinstance(item, ConsoleUrlItem):
            return cls.from_console_url_item(item)
        else:
            raise TypeError(f"Unknown item type: {type(item)}")


@attrs.define
class Handler(afwf.Handler):
    def main(self, query: str):
        sf = afwf.ScriptFilter()
        items = ui.handler(query, ui, skip_ui=True)
        # rprint(items)
        afwf_items = [Item.from_acs_item(item) for item in items]
        # rprint(afwf_items)
        sf.items.extend(afwf_items)
        return sf

    def parse_query(self, query: str):
        return dict(query=query)


handler = Handler(id="search")
