
# Problem 1 (2 points)
# Assign the 'name' variable an object that is your name of type str.
name = "Josh Mossing"

# Problem 2 (2 points)
# Create a class and implement it for your problem of interest
class Worker: 
    def __init__ (self, first:str, last:str, salary:int):
        self.first = first
        self.last = last
        self.salary = salary
        
    def get_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def get_email(self):
        return '{}{}@gmail.com'.format(self.first, self.last)

# Problem 3 (2 points)
# Create another class and implement it for your problem of interest
class BlueCollar(Worker):
    def __init__ (self, first, last, salary,job:str, years_worked: int):
        super().__init__ (first, last, salary)
        self.years_worked= years_worked
        self.job = job
    def get_job(self):
        return '{} for {} years'.format(self.job, self.years_worked)
    
    def get_raise(self):
        if self.years_worked <=2:
            raise_amount = 1.0 
        elif self.years_worked<10:
            raise_amount = 1.04
        elif self.years_worked<25:
            raise_amount = 1.10
        elif self.years_worked >=25:
            raise_amount = 1.15
        return float(raise_amount)
            
    def apply_raise(self):
        applied_raise = self.salary *self.get_raise()
        if self.years_worked <=2:
            print("{}.apprentice work is tough, just a couple more 'till you get a raise".format(self.get_job()))
        elif self.years_worked<10:
            print("{}.Nice work,thanks for sticking with us".format(self.get_job()))
        elif self.years_worked<25:
            print("{}.Great work on them bigger jobs".format(self.get_job()))
        elif self.years_worked >=25:
            print("{}.When you planning on retiring?".format(self.get_job()))
        # return "New salary with raise amount is: ${}".format(raise_amount)
        return int(applied_raise)
            
            
# Problem 4 (2 points)
# Create another class and implement it for your problem of interest

class Manager(Worker): 
    def __init__ (self, first, last, salary, number_of_workers):
        super().__init__ (first, last, salary)
        self.number_of_workers = number_of_workers
     
    def get_bonus (self):
        if self.number_of_workers ==25:
            bonus_amount = 2000
        elif self.number_of_workers >=26 and self.number_of_workers<100:
            bonus_amount = 5000
        elif self.number_of_workers >=100:
            bonus_amount = 1000
        else: 
            bonus_amount = 0
        return int(bonus_amount)
        
    def apply_bonus (self):
        applied_bonus = self.salary + self.get_bonus()
        if self.number_of_workers ==25:
            print('{},nice work, leading 25  people is challenging. email sent to  {}'.format(self.get_name(),self.get_email()))
        elif self.number_of_workers >=26 and self.number_of_workers<100:
            print('{},nice work, leading 26 or more people is challenging email sent to  {}'.format(self.get_name(),self.get_email()))
        elif self.number_of_workers >=100:
            print('{},nice work, we are considering moving you up to CFO. email sent to  {}'.format(self.get_name(),self.get_email()))
        else: 
            print('{},keep it up, you will get there someday'.format(self.get_name()))
        return int(applied_bonus)
# If you need to, you can create any additional classes or functions here as well.


# Problem 5 (2 points)
# Assign a variable named 'obj_1' an example instance of one of your classes
obj_1 = Worker("Jim", "Lahey", 50000)

# print(obj_1.get_name())

# Problem 6 (2 points)
#  Assign a variable named 'obj_2' an example instance of another one of your
#  classes
obj_2 = Manager("Steve","Jobs",100000, 30)

# print(obj_2.get_bonus())
# print(obj_2.apply_bonus())


# Problem 7 (2 points)
#  Assign a variable named 'obj_3' an example instance of one of your classes
#  that extends another class
obj_3= BlueCollar("Billy", "Buckenmeyer", 70000, "construction", 15)
# print(obj_3.apply_raise())

# Problems 8 through 14 are worth 4 points each.
#    For each problem you must implement a test method in the following
#     TestCase class. Each method name should be unique and start with 'test_'.
#     Each method should test something different about the classes you created
#     above. Use unittest.TestCase's assert methods to check your implementation.
#     You will get 2 points for each test method created. You will get 2
#     additional points for each of these tests that complete successfully.
#     See https://docs.python.org/3/library/unittest.html for examples.

import unittest
import sys
import inspect
###################################################
#DO NOT MODIFY this class's name or what it extends
###################################################
class MyTestCases(unittest.TestCase):

    # Problem 8
    # add test case method
    def test_get_name(self):
        worker1 = Worker("Bob", "Lahey", 50000)
        get_name_case1 = worker1.get_name()
        self.assertEqual(get_name_case1, "Bob Lahey")
          
    # Problem 9
    # add test case method

    def test_get_job(self):
        bluecollar1 = BlueCollar("Bud", "Mossing", 70000, "carpenter", 37)
        get_job_case1 = bluecollar1.get_job()
        self.assertEqual(get_job_case1, "carpenter for 37 years")
           
    # Problem 10
    # add test case method
    def test_apply_raise(self):
        bluecollar2 = BlueCollar("Jim", "Mossing", 85000, "plumber", 18)
        apply_raise_case1 = bluecollar2.apply_raise()
        self.assertEqual(apply_raise_case1, 93500)
           
    # Problem 11
    # add test case method
    def test_apply_bonus(self):
        manager1 = Manager("Tony","Mossing", 140000, 75)
        apply_bonus_case1 = manager1.apply_bonus()
        self.assertEqual(apply_bonus_case1, 145000)
    # Problem 12
    # add test case method
    
    def test_get_email(self):
        worker2 = Worker("Philip","Johnson", 65000)
        get_email_case1 = worker2.get_email()
        self.assertEqual(get_email_case1,"PhilipJohnson@gmail.com")
        
    # Problem 13
    # add test case method
    
    def test_get_raise(self):
        bluecollar3 = BlueCollar("Jason","Mossing", 75000, "pipe fitter", 8)
        get_raise_case1 = bluecollar3.get_raise()
        self.assertEqual(get_raise_case1, 1.04)
        
    # Problem 14
    # add test case method
    def test_get_bonus(self):
        manager2 = Manager("Stephen", "Jobs", 120000, 26) 
        get_bonus_case1 = manager2.get_bonus()
        self.assertEqual(get_bonus_case1, 5000)
    ##################################################
    #DO NOT MODIFY any of these test case methods
    ##################################################

    def get_classes(self):
        clses = inspect.getmembers(sys.modules[__name__], lambda member: inspect.isclass(member) and member.__module__ == __name__ and member is not MyTestCases)
        return clses

    def test_name_assigned(self):
        m = sys.modules[__name__]
        name = getattr(m,"name",None)
        self.assertTrue(name is not None)
        self.assertTrue(isinstance(name,str))
        self.assertTrue(len(name) > 0)

    def test_one_class_created(self):
        self.assertTrue(len(self.get_classes()) >= 1)

    def test_two_classes_created(self):
        self.assertTrue(len(self.get_classes()) >= 2)

    def test_three_classes_created(self):
        self.assertTrue(len(self.get_classes()) >= 3)

    def test_obj_1_instance_created(self):
        clses = self.get_classes()
        m = sys.modules[__name__]
        obj_1 = getattr(m,"obj_1",None)
        self.assertTrue(obj_1 is not None)
        self.assertTrue(isinstance(obj_1,tuple([cls[1] for cls in clses])))

    def test_obj_2_instance_created(self):
        clses = self.get_classes()
        m = sys.modules[__name__]
        obj_2 = getattr(m,"obj_2",None)
        obj_1 = getattr(m,"obj_1",None)
        self.assertTrue(obj_2 is not None)
        self.assertTrue(isinstance(obj_2,tuple([cls[1] for cls in clses])))
        self.assertNotEqual(type(obj_2),type(obj_1))

    def test_obj_3_instance_created(self):
        clses = self.get_classes()
        m = sys.modules[__name__]
        obj_3 = getattr(m,"obj_3",None)
        self.assertTrue(obj_3 is not None)
        self.assertTrue(isinstance(obj_3,tuple([cls[1] for cls in clses])))
        bases = tuple(b for b in type(obj_3).__bases__ if b is not object)
        print(dir(obj_3))
        self.assertTrue(len(bases) > 0)
        
##################################################
#DO NOT MODIFY any of the code below!
##################################################
if __name__ == "__main__":
    unittest.main()

