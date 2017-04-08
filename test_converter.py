import unittest


def convert(area=None, direction=None):
    #############################################################
    # converts area from sq miles to acres and vice versa       #
    # inputs: area (positive real number), direction in         #
    # ['to_acres','to_miles]                                    #
    # output : conversion value                                 #
    #                                                           #
    #  kel                                                      #
    #                                                           #
    #############################################################

    from numbers import Real
    # operations defined
    operations = {'to_miles': float.__truediv__, 'to_acres': float.__mul__}

    # conversion factor
    acres_per_sqm = 639.997
    # validate inputs
    if not isinstance(area, Real):
        raise TypeError("area is not a real Number".format(area))  # area is real number
    assert area > 0, 'are is not a positive number'  # number positive
    assert direction in ['to_miles', 'to_acres'], "direction must be 'to_miles' or 'to_acres'"
    # conversion is either 'to_miles' or 'to_acres

    # calculation
    return operations[direction](float(area), acres_per_sqm)


class TestConverter(unittest.TestCase):
    # tests area converter function for proper input parameters
    def test_inputs(self):
        # test that invalid inputs are raising assertion or type errors with message
        incorrect_inputs = [
            ('A', 'to_miles'),
            (0, 'to_miles'),
            (-1, 'to_miles'),
            ('10', 'to_miles'),
            (5, 'xxx'),
            (5, 10)]
        # checks that incorrect inputs return TypeError or AssertionError
        [self.assertRaises((AssertionError, TypeError), convert, *incorrect_input) for incorrect_input in
         incorrect_inputs]

    def test_values(self):
        # test that function returns correct outputs for valid inputs to 2 decimal places
        #
        correct_answers = [
            ((639.997, 'to_miles'), 1),
            ((10, 'to_miles'), 0.016),
            ((26.0, 'to_miles'), 0.0406)
            , ((1, 'to_acres'), 640),
            ((10, 'to_acres'), 6399.97),
            ((26.0, 'to_acres'), 16639.92)]
        # assert that function returns correct_answers from above

        for inputs, answer in correct_answers:
            self.assertAlmostEqual(convert(*inputs), answer, places=2,
            msg='Function with parameters {} returned {} instead of {}'.format(inputs,
            convert(*inputs), answer))


if __name__ == '__main__':
    unittest.main()
