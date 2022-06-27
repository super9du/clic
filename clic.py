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
# 获取 license 模板路径
license = dic.pop(LICENSE)
# 获取 package 路径
package = dic.pop(PACKAGE)
# key 为后缀名，value 为对应后缀的 license_data
license_data_map: dict[str, str] = {}

# 生成最原始的 LICENSE 数据
with open(license, "r", encoding="utf-8") as f:
    license_data = f.read().format_map(dic)
    license_data_lines = license_data.splitlines()

with open(os.path.join(package, "LICENSE"), "x", encoding="utf-8") as f:
    f.write(license_data)


def append_license(filename: str):
    with open(filename, "r+", encoding="utf-8") as f:
        postfix = os.path.splitext(filename)[1]
        if not license_data_map.get(postfix):
            if postfix == ".java":
                data = ["/*"]
                data.extend([f" * {line}" for line in license_data_lines])
                data.append(" */")
                data.append("\n")
                license_data_map[".java"] = "\n".join(data)
            elif postfix == ".go":
                data = [f"// {line}" for line in license_data_lines]
                data.append("\n")
                license_data_map[".go"] = "\n".join(data)
            elif postfix == ".py":
                data = [f"# {line}" for line in license_data_lines]
                data.append("\n")
                license_data_map[".py"] = "\n".join(data)
        val = license_data_map.get(postfix)
        if val:
            old = f.read()
            f.seek(0)
            f.writelines(val)
            f.write(old)


def reverse_search(filepath: str):
    for filename in os.listdir(filepath):
        # 默认不遍历以点号开头的文件或文件夹
        if filename.startswith("."):
            continue
        fp = os.path.join(filepath, filename)
        append_license(fp) if os.path.isfile(fp) else reverse_search(fp)


# 遍历 package 目录
reverse_search(package)
