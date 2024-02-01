# -*- coding: utf-8 -*-

import pytest
from afwf_aws_console.handlers.search import handler


def test():
    sf = handler.handler("")
    for item in sf.items:
        print(item.title)
    # print(sf.items[0])
    # sf = handler.handler("ec2-instances")
    # print(sf.items[0])


if __name__ == "__main__":
    from afwf_aws_console.tests import run_cov_test

    run_cov_test(__file__, "afwf_aws_console.handlers.search", preview=False)
