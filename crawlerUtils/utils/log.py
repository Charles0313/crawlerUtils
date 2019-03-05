import logging
import logging.handlers
import datetime


__all__ = ["setLog"]


def setLog(encoding="utf-8"):
    # 日志器
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    # 每天0点自动切割的磁盘文件日志处理器，记录所有日志消息
    rf_handler = logging.handlers.TimedRotatingFileHandler(
        'all.log', when='midnight', interval=1, backupCount=7,
        atTime=datetime.time(0, 0, 0, 0), encoding=encoding)
    rf_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # 无限大的磁盘文件日志处理器，只记录Error以上级别消息
    f_handler = logging.FileHandler('error.log', encoding=encoding)
    f_handler.setLevel(logging.ERROR)
    # 格式包含文件名和行号
    f_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s -" +
        " %(filename)s[:%(lineno)d] - %(message)s"))

    # 流处理器，输出到stdout，输出所有INFO级别以上消息
    sc_handler = logging.StreamHandler()
    sc_handler.setLevel(logging.INFO)
    sc_handler.setFormatter(logging.Formatter(
        "%(message)s"))

    # 把处理器添加给日志器
    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    logger.addHandler(sc_handler)

    return logger