from logging import handlers
import logging
import time

class SingletonInstane:
  __instance = None

  @classmethod
  def __getInstance(cls):
    return cls.__instance

  @classmethod
  def instance(cls, *args, **kargs):
    cls.__instance = cls(*args, **kargs)
    cls.instance = cls.__getInstance
    return cls.__instance

class Logger(SingletonInstane):

    formatter = logging.Formatter('[%(asctime)s],[%(name)s],[%(levelname)s],[%(message)s]')

#    stream_handler = logging.StreamHandler()
#    stream_handler.setFormatter(formatter)
#    __logger.addHandler(stream_handler)
    timestr = time.strftime("%Y%m%d")
    #file_handler = logging.FileHandler('my.log')  #파일핸들러 생성 및 파일 이름설정
    file_handler = handlers.TimedRotatingFileHandler(filename='n2d_'+timestr+'.log', when='midnight', interval=1, encoding='utf-8')
    file_handler.setFormatter(formatter)
#    file_handler.suffix = "%Y%m%d"

    __logger = logging.getLogger("N2D_Logger")      # N2D 로거생성
    __logger.setLevel(logging.DEBUG)   # 로깅수준 설정
    __logger.addHandler(file_handler)

    @classmethod
    def debug_logger(cls, tag, message):
        cls.__logger.debug('['+ tag + ']' + message)

    @classmethod
    def info_logger(cls, tag, message):
        cls.__logger.info('['+ tag + ']' + message)

    @classmethod
    def warning_logger(cls, tag, message):
        cls.__logger.warning('['+ tag + ']' + message)

    @classmethod
    def error_logger(cls, tag, message):
        cls.__logger.error('['+ tag + ']' + message)

    @classmethod
    def critical_logger(cls, tag, message):
        cls.__logger.critical('['+ tag + ']' + message)

#if __name__ == "__main__":
 #   Logger.error_logger('ho','hello')