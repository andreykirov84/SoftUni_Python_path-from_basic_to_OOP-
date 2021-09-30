from unittest import TestCase

from lab import Worker


class TestWorker(TestCase):
    def test_workerInit_whenCorrectNameSalaryandEnergy_shouldBeInitialized(self):
        """
        Test if the worker is initialized with the correct name, salary and energy
        """
        name = 'Worker name'
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)

