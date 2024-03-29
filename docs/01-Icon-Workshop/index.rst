Icon Workshop
==============================================================================


Overview
------------------------------------------------------------------------------
因为这个 App 是一个 Alfred Workflow, 所以我们需要根据 AWS Service / Menu 的不同为 Item 指定 Icon 图标.


Icon Mapping
------------------------------------------------------------------------------
我们的搜索结果返回的是 `aws_console_url_search/data.json <https://github.com/MacHu-GWU/aws_console_url_search-project/blob/main/aws_console_url_search/data.json>`_ 中的 Service 或者 Menu. 所有的 Service 和 Menu 都有一个 ID. 例如 s3 bucket 是 ``s3-buckets``. 所以我们目前的逻辑是用 path 对 ICON 图标文件进行枚举, 然后给每一个 Service 和 Menu 和 ICON 图标枚举关联起来. 具体的关联逻辑如下:

- 如果 id 有关联图标则用关联的图标.
- 如果 menu 没有关联图标则用 service 的图标.
- 如果 service 也没有关联图标则用 AWS 默认的图标.


AWS Architecture Icons
------------------------------------------------------------------------------
AWS 官方提供了所有的 Icon 的下载. 你可以到 `AWS Architecture Icons <https://aws.amazon.com/architecture/icons/>`_, 点击 ``Asset Package`` 下载 Zip.


Icon Path Enum
------------------------------------------------------------------------------
:func:`afwf_aws_console.icons.gen_code.generate_architecture_icons_enum` 函数能够扫描解压后的文件夹, 只选择我们要的低像素 (小于 96x96) 的 PNG, 然后按照文件路径将其拷贝到 `afwf_aws_console/icons/assets/ <https://github.com/MacHu-GWU/afwf_aws_console-project/tree/main/afwf_aws_console/icons/asset>`_ 目录下. 然后在 `afwf_aws_console/icons/ <https://github.com/MacHu-GWU/afwf_aws_console-project/tree/main/afwf_aws_console/icons>`_ 模块下创建四个子模块, ``enum_arch_group.py``, ``enum_arch_service.py``, ``enum_category.py``, ``enum_resource.py``. 它们是对所有 ICON 图标路径的枚举.

.. note::

    `debug/code_work.py <https://github.com/MacHu-GWU/afwf_aws_console-project/blob/main/debug/code_work.py>`_ 运行该文件可以重新生成图标 Asset 以及枚举模块. 但是 ``icon_mapping.py`` 模块只由人类修改.

接下来我们就可以在 `afwf_aws_console/icons/icon_mapping.py <https://github.com/MacHu-GWU/afwf_aws_console-project/blob/main/afwf_aws_console/icons/icon_mapping.py>`_ 模块中把 ID 和图标关联起来了.
