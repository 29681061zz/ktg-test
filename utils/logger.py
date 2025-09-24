import logging

def setup_logger():
    """基础logger设置"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # 创建formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 创建console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger