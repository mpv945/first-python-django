# first-python-django
我的python学习

# 配置环境
  1. 下载https://www.python.org/downloads/ 选择需要的版本(web-based ,executable , embeddable zipfile区别:web-based: 透过网络安装的;executable: 离线安装包；embeddable zipfile: python对zip格式的支持；选择Windows x86-64 executable installer进行安装，第一步，勾选add ptthon路径 to path，选择自定义安装；然后跳转下一页默认设置，点击Next，第三步，在下个页面选择安装到全部用户，选择自定义的目录，例如我创建的D:\soft\python3；点击安装......安装完成，最后的结束界面中，一定点击disable path length limit，禁用系统的Path长度自动限制，能给我们避免很多的麻烦。至此，通过cmd命令python就能运行输出了
  2. 如果想多版本共存，请按着上面步骤在另外目录版本下安装，安装完主要把 ；把目录下的python.exe和pythonw.exe为python3.exe和pythonw3.exe；最后输入python3就能运行了；其他平台安装参考https://code.visualstudio.com/docs/python/python-tutorial
  3. 安装vscode 的Python插件ctrl+shift+x 搜索Python 选择Python这个扩展，安装完重启动；（该插件支持国际化）
  4. 选择一个python解析器；Ctrl + Shift + P 输入Python  ，在下拉选择Python：Select Interpreter，默认会在右下角弹出没有找到提示，点击设置按钮，选择本地的Python环境；
  5. 新增一个测试文件，在根目录点击新增文件hello.py ;这是会提示安装pylint，点击install；编辑完文件保存，最后右键，选择“在终端中运行Python文件”; 另外在VS Code中可以运行Python的另外两种方法：
    1. 选择一行或多行，然后按Shift + Enter或右键单击并选择在Python终端中运行选择/行。此命令非常便于测试文件的一部分
    2. 使用Python：Start REPL命令打开当前所选Python解释器的REPL终端。然后，在REPL中，您可以一次输入和运行一行代码
  6. 配置并运行调试器：
    1. 光标置于print通话上并按F9或者鼠标点击行号
    2. ctrl+shift+D 打开调试；然后选择调试工具栏上的设置图标（或使用Debug > Open configurations菜单命令），提示语言环境，选择python 然后会生成一个launch.json
      1. 要在程序启动时自动停止第一行的调试器,请在launch.json的configurations 下第一个{}下添加"stopOnEntry": true,
      2. 如果需要指定包含要用于调试的解释器的确切文件夹，请pythonPath在配置中包含一个条目，例如"pythonPath": "${workspaceFolder}"或"pythonPath": "${workspaceFolder}/.venv"。
    3. 设置好断点，按F5启动debug，顶部显示调试工具栏，从左到右依次显示以下命令：继续（F5），跳过（F10），步入（F11），步出（Shift + F11），重启（Ctrl + Shift + F5），并停止（Shift + F5）。
  7. 安装和使用包在（参考下面 【Django创建项目环境】的虚拟环境，可以直接新建终端ctrl+shift+` 使用python -m pip命令）
    1. 在终端输入：win下cmd运行：python -m pip install matplotlib；mac：sudo python3 -m pip install matplotlib；Debian：sudo apt-get install python3-tk再执行python -m pip install matplotlib
    2. 在hello.py 头部添加import matplotlib.pyplot as plt和import numpy as np（创建图形绘图，这通常与数据科学一起完成。）


# 为Django创建项目环境 官网参考文档https://www.djangoproject.com/start/；
## 创建一个安装Django的虚拟环境
  1. 使用虚拟环境可以避免将Django安装到全局Python环境中，并且可以精确控制应用程序中使用的库。在您的文件系统上，为本教程创建一个项目文件夹，例如first_react_native_app。例如cmd执行cd /d D:\workspace\vscode\first-python-django
  2. 在该文件夹中，使用以下命令（根据您的计算机）创建env基于当前解释器命名的虚拟环境：win下执行（cmd执行）：python -m venv .venv（.venv为环境文件夹的名称）；macOS/Linux执行：sudo apt-get install python3-venv然后python3 -m venv env
  3. 选择python环境，ctrl+shift+p 输入>: Python: Select Interpreter ；选择带.venv的虚拟环境，
  4. 新建终端 ctrl+shift+` 打开终端（在本项目目录下）执行python -m pip install django（可以指定版本Django==2.1.4）；安装完查看版本python -m django --version
  5. 使用django-admin创建Django架构目录：django-admin startproject study_django
  6. 运行测试环境cd .\study_django\  然后执行python manage.py runserver <0.0.0.0:8000> 0.0.0.0 让其它电脑可连接到开发服务器，8000 为端口号。如果不说明，那么端口号默认为 8000。
  7. 调试请查看https://code.visualstudio.com/docs/python/tutorial-django