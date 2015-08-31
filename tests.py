from contextlib import redirect_stdout
from io import StringIO
import unittest
import utils

class TestTimeIt(unittest.TestCase):

    def test_timer(self):
        """
        Test to make sure that timeit returns the time it takes for the
        method to run close enough to the time that it actually takes.
        """
        import time

        @utils.timeit
        def time_me():
            time.sleep(0.5)

        str_out = StringIO()
        with redirect_stdout(str_out):
            start = time.time()
            time_me()
            end = time.time()
        out = str_out.getvalue().split(" ")
        time = float(out[-2])
        #print("took %f while test said %f" % (end-start, time,))
        self.assertAlmostEqual(time, end - start, places=3)


if __name__ == "__main__":
    unittest.main()
