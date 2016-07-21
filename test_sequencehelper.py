import unittest
import sequencehelpers


class TestSingle(unittest.TestCase):
    # TODO test for other types of iterables
    def setUp(self):
        self.empty_list = []
        self.list_len_two = [1, 2]
        self.list_len_one = [5]
        self.dict_len_one = {'test': 'testval'}
        self.zero_error = 'Expected exactly one item but the iterable contained none.'
        self.more_than_one_error = 'Expected exactly one item but the iterable contained more than one.'

    def test_raises_sequence_error_empty_list(self):
        with self.assertRaises(sequencehelpers.SequenceError) as e:
            sequencehelpers.single(self.empty_list)
        self.assertTrue(self.zero_error in str(e.exception))

    def test_raises_sequence_error_list_len_two(self):
        with self.assertRaises(sequencehelpers.SequenceError) as e:
            sequencehelpers.single(self.list_len_two)
        self.assertTrue(self.more_than_one_error in str(e.exception))

    def test_returns_element_if_len_one(self):
        observed = sequencehelpers.single(self.list_len_one)
        self.assertEqual(observed, 5)

    def test_with_dict_len_one(self):
        # returns the key of the dict, not the value
        observed = sequencehelpers.single(self.dict_len_one)
        self.assertEqual(observed, 'test')


class TestSingleOrDefault(unittest.TestCase):
    def setUp(self):
        self.empty_list = []
        self.list_len_two = [1, 2]
        self.list_len_one = [5]
        self.dict_len_one = {'test': 'testval'}
        self.more_than_one_error = 'Expected one or fewer items but the iterable contained more than one.'

    def test_with_empty_list(self):
        observed = sequencehelpers.single_or_default(self.empty_list)
        self.assertIsNone(observed)
        observed = sequencehelpers.single_or_default(self.empty_list, 'test')
        self.assertEqual(observed, 'test')

    def test_with_list_len_2(self):
        with self.assertRaises(sequencehelpers.SequenceError) as e:
            observed = sequencehelpers.single_or_default(self.list_len_two)
        self.assertTrue(self.more_than_one_error in str(e.exception))

    def test_with_list_len_1(self):
        observed = sequencehelpers.single_or_default(self.list_len_one, 'test')
        self.assertEqual(observed, 5)

    def test_with_dict_len_1(self):
        observed = sequencehelpers.single_or_default(self.dict_len_one, 'test')
        self.assertEqual(observed, 'test')


class TestFirst(unittest.TestCase):
    def setUp(self):
        self.empty_list = []
        self.list_len_two = [1, 2]
        self.list_len_one = [5]
        self.dict_len_one = {'test': 'testval'}
        self.zero_error = 'Expected at least one item but the sequence contained none.'

    def test_with_empty_list(self):
        with self.assertRaises(sequencehelpers.SequenceError) as e:
            observed = sequencehelpers.first(self.empty_list)
        self.assertTrue(self.zero_error in str(e.exception))

    def test_with_list_len_2(self):
        observed = sequencehelpers.first(self.list_len_two)
        self.assertEqual(observed, 1)

    def test_with_list_len_1(self):
        observed = sequencehelpers.first(self.list_len_one)
        self.assertEqual(observed, 5)


class TestFirstOrDefault(unittest.TestCase):
    def setUp(self):
        self.empty_list = []
        self.list_len_two = [1, 2]
        self.list_len_one = [5]
        self.dict_len_one = {'test': 'testval'}

    def test_with_empty_list(self):
        observed = sequencehelpers.first_or_default(self.empty_list)
        self.assertIsNone(observed)
        observed = sequencehelpers.first_or_default(self.empty_list, 'test')
        self.assertEqual(observed, 'test')

    def test_with_list_len_2(self):
        observed = sequencehelpers.first_or_default(self.list_len_two)
        self.assertEqual(observed, 1)

    def test_with_list_len_1(self):
        observed = sequencehelpers.first_or_default(self.list_len_one)
        self.assertEqual(observed, 5)
        

class TestLast(unittest.TestCase):
    def setUp(self):
        self.empty_list = []
        self.list_len_two = [1, 2]
        self.list_len_one = [5]
        self.dict_len_one = {'test': 'testval'}
        self.zero_error = 'The sequence contained no elements.'

    def test_with_empty_list(self):
        with self.assertRaises(sequencehelpers.SequenceError) as e:
            observed = sequencehelpers.last(self.empty_list)
        self.assertTrue(self.zero_error in str(e.exception))

    def test_with_list_len_2(self):
        observed = sequencehelpers.last(self.list_len_two)
        self.assertEqual(observed, 2)

    def test_with_list_len_1(self):
        observed = sequencehelpers.last(self.list_len_one)
        self.assertEqual(observed, 5)
        
        
class TestLastOrDefault(unittest.TestCase):
    def setUp(self):
        self.empty_list = []
        self.list_len_two = [1, 2]
        self.list_len_one = [5]
        self.dict_len_one = {'test': 'testval'}

    def test_with_empty_list(self):
        observed = sequencehelpers.last_or_default(self.empty_list)
        self.assertIsNone(observed)
        observed = sequencehelpers.last_or_default(self.empty_list, 'test')
        self.assertEqual(observed, 'test')

    def test_with_list_len_2(self):
        observed = sequencehelpers.last_or_default(self.list_len_two)
        self.assertEqual(observed, 2)

    def test_with_list_len_1(self):
        observed = sequencehelpers.last_or_default(self.list_len_one)
        self.assertEqual(observed, 5)


class TestDistinct(unittest.TestCase):
    def setUp(self):
        self.dupe_list = [1, 2, 3, 4, 4]
        self.unique_list = [1, 2, 3, 4]

    def test_with_dupes(self):
        observed = sequencehelpers.distinct(self.dupe_list)
        self.assertTrue(all([num in observed for num in self.unique_list]))
        observed = sequencehelpers.distinct(self.dupe_list)
        # since I can't call len() on a generator object
        counter = 0
        for num in observed:
            counter += 1
        self.assertEqual(counter, 4)

if __name__ == '__main__':
    unittest.main()
