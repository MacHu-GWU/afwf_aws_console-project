# -*- coding: utf-8 -*-

"""
Integrate the `aws_console_url_search <https://github.com/MacHu-GWU/aws_console_url_search-project>`_
with alfred workflow.
"""

import typing as T
import attrs
import afwf.api as afwf

from aws_console_url_search.api import (
    ConsoleUrlItem,
    InfoItem,
)
from aws_console_url_search.ui_init import ui

from ..icons.icon_mapping import id_to_icon

try:
    from rich import print as rprint
except ImportError:
    pass


def get_icon_by_key(mapper: dict, key: str) -> T.Optional[afwf.Icon]:
    """
    Get alfred icon object by the key (id) from the icon mapping.
    """
    if key in mapper:
        return afwf.Icon.from_image_file(mapper[key])
    else:
        return None


T_ACS_ITEM = T.Union[
    ConsoleUrlItem,
]


@attrs.define
class Item(afwf.Item):
    """
    Custom ``afwf.Item`` for this project.
    """

    @classmethod
    def from_console_url_item(cls, item: ConsoleUrlItem):
        """
        todo: docstring
        """
        afwf_item = cls(
            title=item.title,
            subtitle=item.subtitle,
            # uid=item.uid, # don't enable uid, we don't want Alfred to memorize the order.
            arg=item.variables["url"],
            autocomplete=item.autocomplete,
        ).open_url(item.variables["url"])
        path = id_to_icon(item.variables["doc"].id)
        if path is not None:
            afwf_item.set_icon(str(path))
        return afwf_item

    @classmethod
    def from_info_item(cls, item: InfoItem):
        """
        todo: docstring
        """
        return cls(
            title=item.title,
            subtitle=item.subtitle,
        ).set_icon(afwf.IconFileEnum.info)

    @classmethod
    def from_acs_item(cls, item: T_ACS_ITEM):
        """
        todo: docstring
        """
        if isinstance(item, ConsoleUrlItem):
            return cls.from_console_url_item(item)
        if isinstance(item, InfoItem):
            return cls.from_info_item(item)
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
