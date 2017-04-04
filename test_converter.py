import unittest


def convert(area=None, direction=None):
    # converts area from sq miles to acres and vice versa

    from numbers import Real
    # operations defined
    operations = {'to_miles': float.__truediv__, 'to_acres': float.__mul__}
    # conversion factor
    acres_per_sqm = 639.997

    # validate inputs
    assert isinstance(area, Real), 'not a real Number'  # area is real number
    assert area > 0, 'not a positive number'  # number positive
    assert direction in ['to_miles', 'to_acres'], 'direction incorrect'  # conversion is either 'to_miles' or 'to_acres

    # calculation
    return operations[direction](float(area), acres_per_sqm)


class TestConverter(unittest.TestCase):
    # tests area converter function for proper input parameters

    def test_inputs(self):
        # test that invalid inputs are raising assertion errors
        incorrect_inputs = [
            (0, 'to_miles'),
            (-1, 'to_miles'),
            ('10', 'to_miles'),
            (5, 'xxx'),
            (5, 10)]

        [self.assertRaises(AssertionError, convert, *incorrect_input) for incorrect_input in incorrect_inputs]

    def test_convert(self):
        # test that function returns correct outputs for valid inputs
        correct_answers = [
            ((1, 'to_miles'), 0.0015625073242530826),
            ((10, 'to_miles'), 0.015625073242530825),
            ((26.0, 'to_miles'), 0.040625190430580146)
            , ((1, 'to_acres'), 639.997),
            ((10, 'to_acres'), 6399.969999999999),
            ((26.0, 'to_acres'), 16639.922)]

        [self.assertEqual(convert(*inputs), correct_answer, msg='function output not matching test value ') for
         inputs, correct_answer in correct_answers]

if __name__ == '__main__':
    unittest.main()