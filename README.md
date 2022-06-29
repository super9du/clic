# clic: 一款容易使用的、为源码添加许可协议的工具。

[English Specification](README_en.md)

clic 即 create license 的缩写。用于帮助希望将自己代码开源的人，生成符合开源要求的开源代码。

大多数人的开源实际上不规范、不标准。通常情况我们使用开源许可协议进行开源需要在源码根目录下创建
一个名为 LICENSE 的完整的开源协议，同时还要在每个源码文件中添加一个 license 的简单描述，用于
声明该源码是开源的。

这个工具能做的就是将指定的开源协议加到所有的源码开头。目前只是简单地实现了 java、golang、python
源码的添加。源码根目录下的 LICENSE 需要自己手动创建。

## 用法

要求首先下载 python，最好是最新版。安装完成后，将 python 添加到 PATH 环境变量。然后依次执行如下命令：

```shell
pip install virtualenv
virtualenv -p python310 .venv
# windows 执行：
# & .venv/Scripts/Activate.ps1
# unix/linux 执行：
sh .venv/Scripts/activate
pip install -r requirements.txt
./clic.py -l <license-template-name> -p <source code package> -y <year> -a <author> -s <software-name>
```

查看帮助:

```powershell
> .\clic.py -h
usage: clic.py [-h] -l {Apache2,BSD-3-Clause,GPLv3,LGPLv2,MIT,MulanPSL2} -p PACKAGE -y YEAR -a AUTHOR -s SOFTWARE_NAME

为源码创建开源许可协议

options:
  -h, --help            show this help message and exit
  -l {Apache2,BSD-3-Clause,GPLv3,LGPLv2,MIT,MulanPSL2}, --license {Apache2,BSD-3-Clause,GPLv3,LGPLv2,MIT,MulanPSL2}
                        许可协议文件模板名称
  -p PACKAGE, --package PACKAGE
                        需要添加许可协议的包的路径
  -y YEAR, --year YEAR  首次发表年份
  -a AUTHOR, --author AUTHOR
                        版权人的名字
  -s SOFTWARE_NAME, --software_name SOFTWARE_NAME
                        被开源的软件名
```

例：

```shell 
.\clic.py -l MulanPSL2 -p ./test  -y 2022 -a super9du -s clic
```

license-template 需要放在 licenses 目录下，且每个 license-template 都需要在模板中添加 `{year}` `{author}`
 `{software_name}` 到合适的位置。

 ## 许可证

 本程序使用“木兰宽松许可证，第2版”，详细内容见本程序根目录下的 LICENSE 文件。