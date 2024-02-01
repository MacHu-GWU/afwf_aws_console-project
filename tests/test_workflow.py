# -*- coding: utf-8 -*-

from afwf_aws_console.workflow import wf
from afwf_aws_console.handlers import (
    search,
)
from rich import print as rprint


def test():
    sf = wf._run(arg=f"{search.handler.id} s3")
    assert sf.items[0].autocomplete == "s3"


if __name__ == "__main__":
    from afwf_aws_console.tests import run_cov_test

    run_cov_test(__file__, "afwf_aws_console.workflow", preview=False)
