import logging
import sys

def setup_logger(name=__name__):
    """设置日志配置"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # 避免重复添加handler
    if logger.handlers:
        return logger
    # 格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    # 文件处理器
    file_handler = logging.FileHandler('test.log', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger