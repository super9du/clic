# clic: An easy-to-use tool for adding license to source code.

clic is an abbreviation for create license. Used to help people who want to open source their code to generate open source code that meets the requirements of open source.

Most people's open source is actually non-standard. In general, when we use an open source license to open source, we need to create a complete open source license called LICENSE under the source root directory, and also add a simple description of the license to each source file to declare that the source code is open source.

What this tool can do is add the specified open source license to the head of all source code. At present, it is simply implemented to add Java, golang, and Python source code. License in the root directory of the source code needs to be created manually.

## Usage

First, download python，better latest version。On finish installing，add python to PATH 
environment. And then execute following shell: 

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

for example:

```shell
.\clic.py -l MulanPSL2 -p ./test  -y 2022 -a super9du -s clic
```

License-templates need to be placed in the licenses directory, and each license-template
needs to add '{year}' '{author}' '{software_name}' to the template to the appropriate location.

## License

Mulan Permissive Software License，Version 2. See LICENSE for detail.