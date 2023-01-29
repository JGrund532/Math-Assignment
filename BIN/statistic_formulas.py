import statistics
import tools.fraction_to_float
import function_formulas
import math 


class DataFunctions (object):

        @staticmethod
        def mean (x):
            return statistics.mean(x)

        @staticmethod
        def range (x):
            return max(x) - min(x)

        @staticmethod
        def median (x):
            return statistics.median(x)

        @staticmethod
        def mode (x):
            return statistics.mode(x)

        @staticmethod
        def stdev_p (x):
            return statistics.pstdev (x)

        @staticmethod
        def variance_p (x):
            return statistics.pvariance (x)

        @staticmethod
        def stdev_s (x):
            return statistics.stdev (x)

        @staticmethod
        def variance_s (x):
            return statistics.variance (x)
