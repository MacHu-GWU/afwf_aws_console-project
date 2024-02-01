# -*- coding: utf-8 -*-

from afwf_aws_console.icons.icon_mapping import id_to_icon


def test_id_to_icon():
    assert id_to_icon("ec2") is not None
    assert id_to_icon("ec2-instances") is not None


if __name__ == "__main__":
    from afwf_aws_console.tests import run_cov_test

    run_cov_test(__file__, "afwf_aws_console.icons.icon_mapping", preview=False)
