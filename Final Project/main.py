############################ QUESTION 1 #########################

class BankAccount:
        """Base class for both the Savings and Checking Account
        """
        def __init__(self,acct_holders_name,balance):
                self.acct_holders_name=acct_holders_name
                self.balance:float=balance

        def deposit(self,amount):
                """Adds money to this account. It checks first if the amount to deposit is positive

                Args:
                    amount (num): Amount to deposit
                """
                amount=float(amount)
                if amount>=0:
                        self.balance+=amount

        def withdraw(self,amount):
                """Subtracts money from the account, also checks if there is not enough money before.

                Args:
                    amount (num): The amount to withdraw
                """
                amount=float(amount)
                if self.balance-amount>=0:
                        self.balance-=amount

        def get_balance(self):
                """Returns the balance in this account

                Returns:
                    num: Balance
                """
                return self.balance

        def __str__(self):
                return f"BankAccount: {self.acct_holders_name} has ${self.balance}"


class SavingsAccount(BankAccount):
        """A special type of Bank Account that can apply interest rates
        """
        def apply_interest(self):
                """Applies a tiered dynamic interest to the balance
                """
                if self.balance<=1000:
                        self.deposit(0.03*self.balance)
                elif self.balance<=5000:
                        self.deposit(0.05*self.balance)
                else:
                        self.deposit(0.07*self.balance)
        def __str__(self):
                return f"SavingsAccount: {self.acct_holders_name} has ${self.balance}"


class CheckingAccount(BankAccount):
        """You can deposit and withdraw money with an overdraft feature
        """
        def withdraw(self,amount):
                """Allows withdrawals even if the balance is negative

                Args:
                    amount (num): some numerical value to withdraw
                """
                amount=float(amount)
                new_bal=self.balance-amount
                if new_bal<-500:
                        return
                self.balance=new_bal
                if self.balance<0 and self.balance+amount>=0:
                        self.balance-=25.0 # overdraft fee

######################### QUESTION 2 #########################

class ListNode:
        """A node in a singly linked list
        """
        def __init__(self,val=0,next=None):
                self.val=val
                self.next=next

def sample_linked_list():
        """sample linked list
        """
        a=ListNode(1)
        b=ListNode(2)
        c=ListNode(3)
        a.next=b
        b.next=c
        c.next=a
        return a

def find_cycle_length(head)->int:
        """If a cycle is found, returns the length of the cycle
        If no cycle is found, returns -1.

        Args:
            head (ListNode): The head of the singly linked list
        >>> node1=ListNode(1)
        >>> node2=ListNode(2)
        >>> node1.next=node2
        >>> node2.next=node1
        >>> find_cycle_length(node1)
        2
        """
        if head is None:
                return -1
        slow=head
        fast=head.next
        while fast is not None and fast.next is not None and slow is not None: # condition to make sure the 2 ptrs dont run out of sync
                slow=slow.next
                fast=fast.next.next
                if slow==fast: # cycle, find how long it is
                        sz=1
                        last=slow
                        while last.next!=slow: # loop through the cycle until we find how long it is
                                sz+=1
                                last=last.next
                        return sz
        return -1

######################### QUESTION 3 #########################

def findSmallestIndex(nums,target):
        """Finds the smallest index such that all elements after this index are strictly
        greater than the target.

        Args:
            nums (list[int]): numbers to search in
            target (int): target

        Returns:
            int: the index (-1) if it is not possible
        """
        for i in range(len(nums)):
                flag=True
                r=nums[i+1:] if i+1<len(nums) else []
                l=nums[:i]
                # check the right side to make sure all numbers
                # on the right side are strictly greater
                if len(r)==0: # edge case
                        return -1
                r_i=0
                while flag and r_i<len(r):
                        if r[r_i]<=target:
                                flag=False
                        r_i+=1
                if flag:
                        return i+1
        return -1

######################### TESTS ##############################

import unittest
class TestMain(unittest.TestCase):
        def test_savings_account_deposit(self):
                savings = SavingsAccount("John Doe", 500)
                savings.deposit(200)  # Deposit $200
                assert(savings.get_balance() == 700)  # New balance should be 700
        def test_savings_account_interest_below_1000(self):
                savings = SavingsAccount("John Doe", 800)
                savings.apply_interest()  # Interest at 3% for balance less than 1000
                self.assertAlmostEqual(savings.get_balance(), 824, places=2)  # 800 + 3% of 800 = 824
        def test_savings_account_interest_between_1000_and_5000(self):
                savings = SavingsAccount("Jane Smith", 1500)
                savings.apply_interest()  # Interest at 5% for balance between 1000 and 5000
                self.assertAlmostEqual(savings.get_balance(), 1575, places=2)  # 1500 + 5% of 1500 = 1575
        def test_checking_account_overdraft(self):
                checking = CheckingAccount("Alex Lee", 200)
                checking.withdraw(300)  # Withdraw $300, which goes negative
                self.assertEqual(checking.get_balance(), -125)  # Balance should be -125 after overdraft and fee
        def test_no_cycles(self):
                node1=ListNode(1)
                node2=ListNode(2)
                node1.next=node2
                node3=ListNode(3)
                node1.next.next=node3
                self.assertEqual(find_cycle_length(node1),-1)
        def test_cycles1(self):
                node1=ListNode(1)
                node2=ListNode(2)
                node1.next=node2
                node2.next=node1
                self.assertEqual(find_cycle_length(node1),2)
        def test_cycles2(self):
                node1=ListNode(1)
                node2=ListNode(2)
                node3=ListNode(3)
                node4=ListNode(4)
                node5=ListNode(5)
                node6=ListNode(6)
                node7=ListNode(7)
                node1.next=node2
                node2.next=node3
                node3.next=node4
                node4.next=node5
                node5.next=node6
                node6.next=node7
                node7.next=node4
                self.assertEqual(find_cycle_length(node1),4)
        def test_q3_1(self):
                self.assertEqual(findSmallestIndex([1,3,3,5,7],3),3)
        def test_q3_2(self):
                self.assertEqual(findSmallestIndex([1,3,5,7],8),-1)
        def test_q3_3(self):
                self.assertEqual(findSmallestIndex([5,6,7,8,9],5),1)
        def test_q3_4(self):
                self.assertEqual(findSmallestIndex([1,2,3,4,5],5),-1)
        def test_q3_5(self):
                self.assertEqual(findSmallestIndex([1,4,8,12,5,2,10],3),6)
# unittest.main()
# import doctest
# doctest.testmod(verbose=True)