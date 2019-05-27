import time

from six import add_metaclass
from abc import ABCMeta, abstractmethod, abstractproperty

from conf import ConfManagement
from logs import SetLog
from pprint import pprint


@add_metaclass(ABCMeta)
class Global(object):

    def __init__(self):
        test_logpath = ConfManagement().get_ini("TEST_LOG_PATH")
        status_logpath = ConfManagement().get_ini("STATUS_LOG_PATH")
        self.test_log = self.read_logs(test_logpath)
        self.status_log = self.read_logs(status_logpath)
        self.data = {
            "default":
                {
                    "httpd": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {}, "golang": {},
                    "node": {}, "openjdk": {}, "ruby": {},
                },

            "clear":
                {
                    "httpd": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {}, "golang": {},
                    "node": {}, "openjdk": {}, "ruby": {},
                },

            "status_def":
                {
                    "httpd": {}, "golang": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {},
                    "node": {}, "openjdk": {}, "ruby": {},
                },

            "status_Clr":
                {
                    "clearlinux_version": {}, "httpd": {}, "golang": {}, "nginx": {}, "memcached": {}, "redis": {},
                    "php": {}, "python": {}, "node": {}, "openjdk": {}, "ruby": {},
                }
        }

 #   def read_logs(self, file_name):
 #       with open(file_name, 'r') as f:
 #           return f.readlines()

    @abstractproperty
    def serialization(self):
        pass

    # @abstractproperty
    # def save(self):
    #     pass

    def exception_to_response(self, match_result, message):
        if match_result == []:
            SetLog().info(" %s Not getting" % message)
