import logging
import logging.handlers
import os,time

class Trace:
    def __init__(self,modulename='Trace',maxfilecount=5,singlefilesize=2048):
        self.__modulename = modulename
        self.__logger = logging.getLogger(modulename)
        self.__logger.setLevel(logging.DEBUG)
        self.__maxfilecount = maxfilecount
        self.__singlefilesize = singlefilesize
        self.__streamhandler = logging.StreamHandler()
        self.__logfilename = self.__modulename + '.log'
        self.__filehandler = logging.handlers.RotatingFileHandler(self.__logfilename,
                                                                  maxBytes=singlefilesize,
                                                                  backupCount=maxfilecount,
                                                                  encoding='utf-8')
        self.__formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(thread)d %(message)s')
        self.__streamhandler.setFormatter(self.__formatter)
        self.__logger.addHandler(self.__streamhandler)
        self.__filehandler.setFormatter(self.__formatter)
        self.__logger.addHandler(self.__filehandler)

    def trace(self,message,streamlevel=logging.WARNING,filelevel=logging.INFO):
        self.__streamhandler.setLevel(streamlevel)
        self.__filehandler.setLevel(filelevel)
        if streamlevel == logging.DEBUG:
            self.__logger.debug(message)
        elif streamlevel == logging.INFO:
            self.__logger.info(message)
        elif streamlevel == logging.WARNING:
            self.__logger.warning(message)
        elif streamlevel == logging.ERROR:
            self.__logger.error(message)
        elif streamlevel == logging.CRITICAL:
            self.__logger.critical(message)
        else:
            self.__logger.exception(message)