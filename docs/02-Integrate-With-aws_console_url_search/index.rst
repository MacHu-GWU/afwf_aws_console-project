Integrate With aws_console_url_search
==============================================================================
This project is based on my project `aws_console_url_search <https://github.com/MacHu-GWU/aws_console_url_search-project>`_, a cross platform, Alfred similar, CLI app that can search AWS Console menu interactively. This project is just a wrapper to integrate ``aws_console_url_search`` with Alfred Workflow.

和 ``aws_console_url_search`` 项目的整合非常简单, 在 `afwf_aws_console/handlers/search.py <https://github.com/MacHu-GWU/afwf_aws_console-project/blob/main/afwf_aws_console/handlers/search.py>`_ 模块中, 我们调用 ``aws_console_url_search`` 的 API, 并把它返回的 items 转化成 ``afwf.Item`` 对象即可.
