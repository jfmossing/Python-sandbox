from datetime import date
import datetime
import unittest

# NOTE: Make sure to run this file and make sure you unit test methods run
#   successfully!!

# Implement any functions and classes here

def display_fibonacci_sequence (num_of_terms: int):
    n1= 0
    n2= 1
    count = 0
    if num_of_terms <=0: 
        print('Please input a number > 1')
        fibonacci_sequence= ("Invalid entry")
    else: 
        fibonacci_sequence = []
        while count < num_of_terms:
            n_last = n1+n2
            n1 = n2
            n2 = n_last
            fibonacci_sequence.append(n1)
            count+= 1
    print(fibonacci_sequence)
    return fibonacci_sequence


def group_NFL_data (nfl_team: str, wins: int, **kwargs):
    if wins < 0:
        print('It is impossible to have negative wins')
        nfl_data= ("Invalid entry")
    else:
        nfl_data = {nfl_team: wins}
    return nfl_data 

def group_NBA_data (nba_team: str, wins: int): 
    if wins < 0:
        print('It is impossible to have negative wins')
        nba_data= ("Invalid entry")
    else:
        nba_data = []
        nba_data.append(nba_team)
        nba_data.append(wins)
    return nba_data

def parse_date_string(date_str: str):
   
    x= date_str.count("-",0, len(date_str))
    parts = date_str.split('-')
   
    if x ==2:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        d = date(year,month,day)
      
    elif x==1:
        year = int(parts[0])
        month = int(parts[1])
        day = 1
        d= date(year,month,day)
        # print(d)
    else: 
        year = int(parts[0])
        month = 1
        day = 1
        d= date(year,month,day)
        # print(d)
    return d     


###################################################
#DO NOT MODIFY this class's name or what it extends
###################################################
class MyTestCases(unittest.TestCase):
    # Implement your test methods here
    # See https://docs.python.org/3/library/unittest.html for examples.
  
    def test_display_fibonacci_sequence(self):
        testcase1 = display_fibonacci_sequence(8)
        self.assertEquals(testcase1,[1, 1, 2, 3, 5, 8, 13, 21])
        self.assertIsInstance(testcase1, list)
        
    def test_group_NFL_data(self):
        set1 = group_NFL_data('Browns', 10) 
        self.assertEquals(set1,{'Browns':10})
        self.assertIsInstance(set1, dict)
        
        set2 = group_NFL_data('Steelers', -1)
        self.assertNotIsInstance(set2, dict)
        
    def test_group_NBA_data(self):
        set3 = group_NBA_data('Cavs', 64) 
        self.assertIsInstance(set3, list)
        self.assertEquals(set3,['Cavs',64])
        
        set4 = group_NBA_data('Celtics', -1)
        self.assertNotIsInstance(set4, list)

    def test_date_string(self):
        d1 = parse_date_string("2002")
        self.assertIsInstance(d1, datetime.date)
        
        d2 = parse_date_string("2021-03")
        assert isinstance(d2, datetime.date)
        
        d3 = parse_date_string("2020-3-7")
        assert isinstance(d3, datetime.date)
    

    pass
        
##################################################
#DO NOT MODIFY any of the code below!
##################################################
if __name__ == "__main__":
    unittest.main()

