# coding:utf-8
#! python3

class TestCase:
    
    def __init__(self, name):
        self.wasRun = None
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
    
class WasRun(TestCase):

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

    def testMethod(self):
        self.wasRun = 1

class TestCaseTest(TestCase):
    
    def setUp(self):
        self.test = WasRun("testMethod")
    
    def testRunning(self):
        test.run()
        assert(test.wasRun)

    def testSetUp(self):
        test.run()
        assert(test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()