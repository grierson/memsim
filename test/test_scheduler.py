""" Test Process Scheduler """
import unittest
import tkinter as tk
from memsim.scheduler import Scheduler

class SchedulerTest(unittest.TestCase):
    """SchedulerTest"""
    def test_scheduler_is_empty(self):
        """test_scheduler_is_initially_empty"""
        root = tk.Tk()
        scheduler = Scheduler(root)
        self.assertEqual({}, scheduler.processes)
        self.assertEqual(len(scheduler.processes), 0)

    def test_validate_process_details(self):
        """test_validate_process_details"""
        root = tk.Tk()
        scheduler = Scheduler(root)
        self.assertTrue(scheduler.validate_process_details("Vim", 200))

    def test_add_process(self):
        """test_add_process"""
        root = tk.Tk()
        scheduler = Scheduler(root)
        scheduler.add_process("Vim", 200)
        scheduler.add_process("Nano", 321)
        scheduler.add_process("Emacs", 666)
        self.assertEqual(len(scheduler.processes), 3)

    def test_get_process_size(self):
        """test_get_process_size"""
        root = tk.Tk()
        scheduler = Scheduler(root)
        scheduler.add_process("Vim", 200)
        self.assertTrue(scheduler.get_process_size("Vim"), 200)


if __name__ == '__main__':
    unittest.main()
