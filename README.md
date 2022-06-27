# clic: 一款简单地创建开源许可协议的工具

[English Specification](README_en.md)

clic 即 create license 的缩写。用于帮助希望将自己代码开源的人，生成符合开源要求的开源代码。
这个工具会将指定的开源协议加到所有的源码开头。目前只是简单地实现了 java、golang、python
源码的添加。源码根目录下还应该有一个名为 LICENSE 的完整的开源协议，需要自己手动创建。

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

比如这样：

```shell 
.\clic.py -l MulanPSL2 -p ./test  -y 2022 -a super9du -s clic
```

license-template 需要放在 licenses 目录下，且每个 license-template 都需要在模板中添加 `{year}` `{author}`
 `{software_name}` 到合适的位置。

 ## 许可证

 本程序使用“木兰宽松许可证，第2版”，详细内容见本程序根目录下的 LICENSE 文件。