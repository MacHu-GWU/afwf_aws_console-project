# -*- coding: utf-8 -*-

from afwf_aws_console.handlers.open_file import handler


def test():
    sf = handler.handler("")
    assert len(sf.items) == 9


if __name__ == "__main__":
    from afwf_aws_console.tests import run_cov_test

    run_cov_test(__file__, "afwf_aws_console.handlers.open_file", preview=False)
