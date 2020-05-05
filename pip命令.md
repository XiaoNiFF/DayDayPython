# pip常用命令
## 安装package
### 常用命令 
- 在python用pip命令：
  
  `python -m pip [--default-timeout=100] install <package name>`

- 直接在命令行用pip命令：
  
  `pip install <package name>`

### 出现的问题及解决方法
1. 若由于一些局域网的原因，使用 pip 出现 “connection timeout”，连接超时可以使用国内的镜像网站下载：  
http://e.pypi.python.org  
http://pypi.douban.com/simple
>

- 解决方法如下:

    *#packagename是要下载的包的名字*  
    `pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com packagename`

    *#安装pip*  
    `pip install -i http://e.pypi.python.org --trusted-host e.pypi.python.org --upgrade pip`

## 升级package
### 常用命令
`pip install --upgrade -i http://pypi.douban.com/simple --trusted-host pypi.douban.com pip`

### 出现的问题及解决方法
1. 命令行提示以下错误ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 拒绝访问。: 'C:\\Users\\bailong\\AppData\\Local\\Temp\\pip-uninstall-jk6d_cjx\\pip.exe'
Consider using the `--user` option or check the permissions.

- 解决方法如下:
  
    *加入--user选项*  
    `pip install --user --upgrade -i http://pypi.douban.com/simple --trusted-host pypi.douban.com pip`

## 其他常用命令
- *查看已经安装的package*  
`pip list`

- *查看可以升级的package*  
`pip list -outdated`

