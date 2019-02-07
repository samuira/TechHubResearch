import re

class RegTest(object):

    def regtest(self, pattern, str):
        pattern = re.compile(pattern)
        return re.match(pattern, str)
