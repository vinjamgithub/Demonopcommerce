import inspect
import logging


'''class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename="C:\\Users\\vvinjam\\PycharmProjects\\Demonopcommerce\\Logs\\automation.log",
        #                  format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger("C:\\Users\\vvinjam\\PycharmProjects\\Demonopcommerce\\Logs\\logfile.log")
        logger.setLevel(logging.INFO)
        return logger'''

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger