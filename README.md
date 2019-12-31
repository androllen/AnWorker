# AnWorker

### 学习来源:
[ Flask 教程 ](http://docs.jinkan.org/docs/flask/)

[安装 Python 虚拟环境](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

[Pyhton 教程中文文档](https://docs.python.org/zh-cn/3/tutorial/classes.html)

[Flask-Bootstrap 教程中文文档](https://flask-bootstrap-zh.readthedocs.io/zh/latest)

[Jinja2中文文档](https://www.w3cschool.cn/yshfid/thlnsozt.html)

### for Windows
``` bash
# Creating a virtual environment
py -m venv env
# Activating a virtual environment
.\env\Scripts\activate
# Leaving the virtual environment
deactivate
```

### for Linux
``` bash
# Creating a virtual environment
python3 -m venv env
# Activating a virtual environment
. env/bin/activate
# Leaving the virtual environment
deactivate
```

### install dependencies
``` bash
# install all of the dependencies
pip install -r requirements.txt
# Installing packages
pip install flask
# export a list of all installed packages
pip freeze > requirements.txt
```