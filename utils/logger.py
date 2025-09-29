import logging
import sys
import os


def setup_logger(name=__name__):
    """设置日志配置，将日志文件固定保存到当前脚本所在的utils目录下"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 避免重复添加handler
    if logger.handlers:
        return logger

    # 获取当前脚本(logger.py)所在的目录（即utils目录的绝对路径）
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 拼接日志文件的绝对路径（utils/test.log）
    log_file_path = os.path.join(current_dir, 'test.log')

    # 格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # 文件处理器 - 使用绝对路径确保日志生成在utils目录
    file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
