import sys
import os
import unittest

# Add the src folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import the gpt4_api module
from tools import gpt4_api

# Load a testing API Key from the environment
gpt4_api.openai.api_key = os.environ.get("OPENAI_API_KEY")

class TestGpt4Api(unittest.TestCase):
    def test_gpt4_chat_request(self):
        print("Running test_gpt4_chat_request...")
        messages = [
            {"role": "system", "content": "Set the behavior"},
            {"role": "assistant", "content": "Provide examples"},
            {"role": "user", "content": "Set the instructions"}
        ]

        response = gpt4_api.gpt4_chat_request(messages)
        self.assertIsNotNone(response)
        self.assertIn("choices", response)

    def test_decode_response(self):
        print("Running test_decode_response...")
        messages = [
            {"role": "system", "content": "Set the behavior"},
            {"role": "assistant", "content": "Provide examples"},
            {"role": "user", "content": "Set the instructions"}
        ]

        response = gpt4_api.gpt4_chat_request(messages)
        decoded = gpt4_api.decode_response(response)

        self.assertIsNotNone(decoded)
        self.assertIn("id", decoded)
        self.assertIn("response", decoded)

class CustomTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write('✓')
        self.stream.flush()
        
    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.write('✗')
        self.stream.flush()

class NotDotsTestRunner(unittest.TextTestRunner):
    resultclass = CustomTextTestResult


if __name__ == '__main__':
    unittest.main(testRunner=NotDotsTestRunner())
    unittest.main()