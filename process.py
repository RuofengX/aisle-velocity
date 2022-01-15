from subprocess import *
from time import sleep
from config import *
import threading
from time import sleep

# 别名
Thread = threading.Thread


class MainThread(AisleDefault):
    """
    子进程及其管理、异步输出日志等
    """

    def __init__(self, args: str or list, env: dict = {}):
        """
        :perms args: 需要管理的命令，如`sh run.sh`，如果为字符串则需要和真实命令一致
        :parms env: 额外的环境变量字典
        """
        # 多继承单独初始化
        AisleDefault.__init__(self)

        # 设置self.cmd记录子进程命令内容
        self.logger.debug(f'命令为{args}')
        if type(args) is list:
            self.cmd: list = args
        elif type(args) is str:
            self.cmd: list = args.split(' ')
        else:
            self.logger.error(f'意料之外的属性type(args):{type(args)}')

        # 传递额外的环境变量
        self.env: list = env

        # 设置_done标志，该值为None时表示程序正常运行，否则将在延迟之后结束进程
        self._up: bool = False

        # 进程池
        self.thread_pool: list = []
        self.thread_pool += [
            Thread(target=self.err),
            Thread(target=self.log),
            Thread(target=self.daemon)
        ]
        self.logger.debug(f'线程池：{self.thread_pool}')

        # 其他属性初始化
        self.process: Popen

        # 启动线程池
        self.start()

    def start(self):
        # 创建子进程，参考https://docs.python.org/zh-cn/3.7/library/subprocess.html#popen-constructor
        try:
            self.process = Popen(
                args=self.cmd,
                bufsize=-1,
                stdin=PIPE,
                stdout=PIPE,
                stderr=PIPE,
                env={**ENVIRON_DICT, **self.env},
                creationflags=ABOVE_NORMAL_PRIORITY_CLASS,  # 略高于平均的优先级
            )
        except OSError:
            self.logger.error(f'子进程（{self.cmd}）初始化异常，猜想：被执行的文件不存在')
        else:
            self.logger.warning(f'子进程（{self.cmd[0]}...）初始化成功')
            self._up = True

        for i in self.thread_pool:
            i.start()
        for i in self.thread_pool:
            i.join()

    @staticmethod
    def read_pipe(pipe: PIPE):
        """
        :parms pipe: 对管道读取
        :return:返回管道内的内容
        """
        #codec = autodecode.AutoDecode()
        #result = codec.decode(pipe.readline())
        bit_stream = pipe.readline()
        if bit_stream == b'':
            pass
        else:
            try:
                result = bit_stream.decode(GLOBAL_ENCODING)
                result = result.replace('\n', '')  # 删去/n，logger自动会换行
            except UnicodeDecodeError:
                """
                当无法解析时直接输出二进制结果
                """
                result = bit_stream
            finally:
                return result

    def input(self, cmd: str):
        """
        :parms cmd: 向子进程的STDIN输入的字符串，并回车
        """
        with open(self.process.stdin, mode='rt', encoding=GLOBAL_ENCODING) as _:
            _.writelines(cmd+'\n')

    # 以下方法需要使用Thread并行

    def daemon(self):
        """
        检查进程结束后延迟关闭daemon
        """
        while self.process.poll() is None:
            pass
        self.logger.warning(f'亚进程已结束，守护进程将在10秒后关闭')
        sleep(10)
        self._up = False

    def err(self):
        """
        重复将管道self.process.stderr写出到self.logger中
        """
        while self._up:
            pipe = self.process.stderr
            result = self.read_pipe(pipe)
            if result is None:
                pass
            else:
                self.logger.error(f'|STDERR|{result}')

    def log(self):
        """
        重复将管道self.process.stdout写出到self.logger中
        """
        while self._up:
            pipe = self.process.stdout
            result = self.read_pipe(pipe)
            if result is None:
                pass
            else:
                self.logger.info(f'|STDOUT|{result}')
