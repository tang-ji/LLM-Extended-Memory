import unittest

class CustomTextTestResult(unittest.TextTestResult):
    def print_result(self, test):
        pass

    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write('✓\n')
        self.stream.flush()

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.write('✗\n')
        self.stream.flush()

class CustomTextTestRunner(unittest.TextTestRunner):
    resultclass = CustomTextTestResult

if __name__ == '__main__':
    suite = unittest.TestLoader().discover(start_dir='./', pattern='test_*.py', top_level_dir='./')
    runner = CustomTextTestRunner()
    runner.run(suite)