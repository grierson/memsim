''' TEST MEMORY '''
from source.memory import Memory
import tkinter
import unittest


class TestMemory(unittest.TestCase):
    ''' TEST Memory Class '''
    def setUp(self):
        ''' Create Memory Panel '''
        parent = tkinter.Tk()
        self.ram = Memory(parent)

    def test_check_process_exists(self):
        ''' Test that a process name is in the Process List '''
        self.ram.create_process('Style', 200, 0)
        self.assertTrue(self.ram.check_process_exists('Style'))

    def test_get_process_size(self):
        ''' Test Return Process Size '''
        self.ram.create_process('Blankspace', 123, 0)
        self.assertEqual(self.ram.get_process_size('Blankspace'), 123)

    def test_get_process_address(self):
        ''' Test Get Process Address

        Note: create_process(process_name, process_size, address)
        '''
        self.ram.create_process('Red', 333, 111)
        self.assertEqual(self.ram.get_process_address('Red'), 111)

    def test_kill(self):
        ''' Create Process then Kill it '''
        self.ram.create_process('Dave', 666, 0)
        self.assertTrue(self.ram.check_process_exists('Dave'))
        self.ram.kill('Dave')
        self.assertFalse(self.ram.check_process_exists('Dave'))

    def test_get_process_list(self):
        ''' Test Get process List '''
        self.ram.create_process('Style', 200, 0)
        self.ram.create_process('Red', 333, 111)
        self.assertEqual(self.ram.process_list, ['Style', 'Red'])

    def test_find_holes(self):
        ''' Test

        Note: create_process(process_name, process_size, address)
        M_HIGHT = 450

        |----------------------------| Address: 0
        |    FavouriteThings: 100    |
        |----------------------------| Address: 101
        |    Hole: 50                | * Process to big for this hole
        |----------------------------| Address: 151
        |    IWillSurvive: 49        |
        |----------------------------| Address: 200
        |    Hole: 50                | * Process should go here
        |----------------------------| Address: 251
        |    Hello: 99               |
        |----------------------------| Address: 350
        |    Hole: abs(memory)       | (M_HIGHT - hole address = hole size)
        |----------------------------| (450 - 350 = 100)
        '''
        self.ram.create_process('FavoriteThings', 100, 0)
        self.ram.create_process('IWillSurvive', 49, 151)
        self.ram.create_process('Hello', 99, 251)

        # Kill Favourite Things to create hole at top of memory
        self.ram.kill('FavoriteThings')

        self.assertEqual(self.ram.find_holes(), [{'address': 0, 'size': 151},
                                                 {'address': 200, 'size': 51},
                                                 {'address': 350, 'size': 100}])

    def test_first_fit(self):
        ''' Test First Fit Allocation

        Creating Process with a Size of 110
        * The process is 10 Bytes too big for the first hole
        * However the process is small enough to fit into the next
        |----------------------------| Address: 0
        |    FavoriteThings: 99      |
        |----------------------------| Address: 100
        |    Hole: 100               | * Process to big for this hole
        |----------------------------| Address: 201
        |    IWillSurvive: 99        |
        |----------------------------| Address: 300
        |    Hole: abs(memory)       | * Process should go here
        |----------------------------|
        '''
        # Create Processes to simulate real world example
        self.ram.create_process('FavoriteThings', 99, 0)
        self.ram.create_process('IWillSurvive', 99, 201)

        # Actually Past Process through First Fit allocation
        self.ram.first_fit('Summertime', 110)
        self.assertEqual(self.ram.get_process_address('Summertime'), 300)

    def test_best_fit(self):
        ''' Test Best Fit Allocation

        Process Size: 110
        * The process should skip the first hole because there may be more
        * efficient holes within the memory
        |----------------------------| Address: 0
        |    Hole: 200               |
        |                            |
        |----------------------------| Address: 201
        |    FavoriteThings: 99      |
        |----------------------------| Address: 300
        |    Hole: 130               | * Process should go here
        |----------------------------|
        |    IWillSurvive: 11        |
        |----------------------------| Address: 300
        '''
        self.ram.create_process('FavoriteThings', 99, 201)
        self.ram.create_process('IWillSurvive', 11, 431)

        # Actually Past Process through Best Fit allocation
        self.ram.best_fit('Summertime', 110)
        self.assertEqual(self.ram.get_process_address('Summertime'), 300)

    def test_worst_fit(self):
        ''' Test worst Fit Allocation

        Process Size: 110
        * The process should skip the first hole because there may be more
        * efficient holes within the memory
        |----------------------------| Address: 0
        |    Hole: 100               |
        |----------------------------| Address: 101
        |    FavoriteThings: 99      |
        |----------------------------| Address: 200
        |    Hole: 130               | * Process should go here
        |----------------------------| Address: 331
        |    IWillSurvive: 15        |
        |----------------------------| Address: 346
        |    Hole: 104               |
        |----------------------------|
        '''
        self.ram.create_process('FavoriteThings', 99, 101)
        self.ram.create_process('IWillSurvive', 15, 331)

        # Actually Past Process through Best Fit allocation
        self.ram.worst_fit('Summertime', 110)
        self.assertEqual(self.ram.get_process_address('Summertime'), 200)

    def test_compact(self):
        ''' Test Compact

        |----------------------------| Address: 0
        |    Hole: 100               |
        |----------------------------| Address: 101
        |    FavoriteThings: 99      |
        |----------------------------| Address: 200
        |    Hole: 130               | * Process should go here
        |----------------------------| Address: 331
        |    IWillSurvive: 15        |
        |----------------------------| Address: 346
        |    Hole: 104               |
        |----------------------------|

        After
        |----------------------------| Address: 0
        |    FavoriteThings: 99      |
        |----------------------------| Address: 99
        |    IWillSurvive: 15        |
        |----------------------------| Address: 116
        |    Hole: N                 |
        |----------------------------|
        '''
        self.ram.create_process('FavoriteThings', 99, 101)
        self.ram.create_process('IWillSurvive', 15, 331)

        self.ram.compact()

        self.assertEqual(self.ram.get_process_address('FavoriteThings'), 0)
        self.assertEqual(self.ram.get_process_address('IWillSurvive'), 99)
