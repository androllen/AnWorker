# AnWorker

基于 `flask` 编写的 `web` 网站

### 包含

- 多数据库读取
- 分页加载
- 路由带参与不带参的页面跳转
- jinja2 模板
- 框架的解耦
- 日志
- 足迹

### 不包含 - TODO

- 成语大全与中华大词典 没有通过 `python` 爬取数据
- 壁纸没有完成分页加载
- 历史壁纸写入到数据库中

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

### build

```sh
.\env\Scripts\activate
cd src
py server.py
```

### 学习来源:
[Flask 教程](http://docs.jinkan.org/docs/flask/)

[安装 Python 虚拟环境](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

[Pyhton 教程中文文档](https://docs.python.org/zh-cn/3/tutorial/classes.html)

[Flask-Bootstrap 教程中文文档](https://flask-bootstrap-zh.readthedocs.io/zh/latest)

[Jinja2 中文文档](http://docs.jinkan.org/docs/jinja2/)
[Jinja2 英文文档](https://jinja.palletsprojects.com/en/2.10.x/)

[Bootstrap 英文文档](https://getbootstrap.com/)
[font-awesome](https://www.bootcss.com/p/font-awesome/#)  
[jQuery CDN ](https://code.jquery.com/)  

<br>
<br>
<p style="text-align: center;font-size: 12px;" >数据来源于<a href="https://github.com/chinese-poetry/huajianji">花间集</a></p>
<p style="text-align: center;font-size: 12px;" >如果侵权请联系我删除</p>