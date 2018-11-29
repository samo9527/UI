import os

def get_config_yaml_path(dir='config',dir_low='config.yaml'):
    """获取config.yaml文件路径"""
    a = os.path.dirname(os.path.dirname(__file__))
    b = a + '/{}/{}'.format(dir,dir_low)
    return b

def get_chrome_driver_path(dir='package',dir_low='ChromeDriver.exe'):
    """获取谷歌浏览器驱动包路径"""
    a = os.path.dirname(os.path.dirname(__file__))
    b = a + '/{}/{}'.format(dir, dir_low)
    return b

def get_excel_path(dir='package',dir_low='ExcelReport.xlsx'):
    """获取Excel路径"""
    a = os.path.dirname(os.path.dirname(__file__))
    b = a + '/{}/{}'.format(dir, dir_low)
    return b

def get_error_img_path(dir='img',dir_low='15422765199665.png'):
    """获取错误图片路径"""
    a = os.path.dirname(os.path.dirname(__file__))
    b = a + '/{}/{}'.format(dir, dir_low)
    return b

def get_login_img_path(dir='img',dir_low='log.png'):
    """获取测试项目的log图片"""
    a = os.path.dirname(os.path.dirname(__file__))
    b = a + '/{}/{}'.format(dir, dir_low)
    return b

if __name__ == '__main__':
    print(get_error_img_path)
