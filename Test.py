import unittest
import datetime

from HelloPython import now

class TestNow(unittest.TestCase):
    def test_datetime_now(self):
        nowtest = datetime.datetime.now()
        nowtest2 = nowtest.strftime("%A, %d-%m-%Y : %H:%M")
        now2 = now.strftime("%A, %d-%m-%Y : %H:%M")
        self.assertEqual(nowtest2, now2)

if __name__ == '__main__':
    unittest.main()
