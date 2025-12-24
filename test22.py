import unittest 
from test2 import BankAccount 
class TestBankAccount(unittest.TestCase): 
    def setUp(self): 
        self.account = BankAccount(1000) 
    def test_deposit(self): 
        self.assertEqual(self.account.deposit(500), 1500) 
    def test_withdraw(self): 
        self.assertEqual(self.account.withdraw(300), 700) 
    def test_withdraw_more_than_balance(self): 
        with self.assertRaises(ValueError): 
            self.account.withdraw(2000)