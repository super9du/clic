import argparse, locale, yaml
import os

LOCALE = locale.getdefaultlocale()[0] or "zh_CN"

DESC = "description"
PACKAGE = "package"
LICENSE = "license"
YEAR = "year"
AUTHOR = "author"
SOFTWARE_NAME = "software_name"

DEFAULT_DESC = {
    DESC: "为源码创建开源许可协议",
    LICENSE: "许可协议文件模板",
    PACKAGE: "需要添加许可协议的包的路径",
    YEAR: "首次发表年份",
    AUTHOR: "版权人的名字",
    SOFTWARE_NAME: "被开源的软件名",
}

translation: dict[str, str] = {}

if LOCALE != "zh_CN":
    with open(
        os.path.join("translations", f"{LOCALE}.yml"), "r", encoding="utf-8"
    ) as f:
        translation = yaml.load(f, yaml.Loader)


def get_description(key: str) -> str:
    return translation.get(key, DEFAULT_DESC[key])


parser = argparse.ArgumentParser(description=get_description(DESC))
parser.add_argument("-l", f"--{LICENSE}", required=True, help=get_description(LICENSE))
parser.add_argument("-p", f"--{PACKAGE}", required=True, help=get_description(PACKAGE))
parser.add_argument("-y", f"--{YEAR}", required=True, help=get_description(YEAR))
parser.add_argument("-a", f"--{AUTHOR}", required=True, help=get_description(AUTHOR))
parser.add_argument(
    "-s", f"--{SOFTWARE_NAME}", required=True, help=get_description(SOFTWARE_NAME)
)
args = parser.parse_args()

dic = args.__dict__.copy()
license = dic.pop(LICENSE)
package = dic.pop(PACKAGE)

# 生成 LICENSE 文件
with open(license, "r", encoding="utf-8") as f:
    license = f.read().format_map(dic)

with open(os.path.join(package, "LICENSE"), "x", encoding="utf-8") as f:
    f.write(license)
    

