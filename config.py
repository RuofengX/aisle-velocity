# config.py存放了设置文件和初始化配置文件
import sys
import colorlog
import os
# 跨语言兼容性
GLOBAL_ENCODING = 'GB2312'

# 偏好设置
GLOBAL_LOGGER_NAME = '全局'
GLOBAL_EXCEPTION_LOGGER_NAME = '全局异常捕获'

# -------DEBUG区域-------
# 日志等级， in ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET']
LOG_LEVEL = 'DEBUG'
NO_DEL_TEMP = False  # 启用后：临时文件夹的文件将不会删除，以供程序运行结束后查看

# -------创建元类-------


class AisleDefault(object):
    def __init__(self):
        # 配置类的日志输出
        self.logger = colorlog.getLogger(self.__class__.__name__)
        self.logger.setLevel(LOG_LEVEL)
        if not self.logger.handlers:
            self.logger.addHandler(CONSOLE_HANDLER)
        self.logger.debug('日志功能启动')


# -------模块设置-------
# ---logging相关配置---
# 配置着色的Handler
CONSOLE_HANDLER = colorlog.StreamHandler()
CONSOLE_HANDLER.setFormatter(
    colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s [%(levelname)s]<%(name)s>%(funcName)s|%(message)s')
)

# 配置全局logger
# 添加全局LOG，避免使用logging.debug()时创建新的handler混淆日志
LOG = colorlog.getLogger(GLOBAL_LOGGER_NAME)
LOG.setLevel(LOG_LEVEL)
LOG.addHandler(CONSOLE_HANDLER)

# 感谢Sam Clements
LOG.info(f'多彩日志，来自Sam Clements的colorlog, https://github.com/borntyping/python-colorlog')

# --Traceback输出设置--🕵️
# 添加全局LOG，避免使用logging.debug()时创建新的handler混淆日志
EXCP_LOG = colorlog.getLogger(GLOBAL_EXCEPTION_LOGGER_NAME)
EXCP_LOG.setLevel(LOG_LEVEL)
EXCP_LOG.addHandler(CONSOLE_HANDLER)


def exception_handler(exception_type, exception_value, traceback):
    # All trace are belong to this!
    EXCP_LOG.error(
        f"检测到异常！{exception_type.__name__}({exception_value})")


if LOG_LEVEL != "DEBUG":
    sys.excepthook = exception_handler

# 关于DEBUG的警告
if LOG_LEVEL == "DEBUG":
    LOG.warn('警告！您已开启DEBUG模式，日志内容可能存在换行，请手工查阅需要的信息。')

# 获取环境变量
ENVIRON_DICT = os.environ
