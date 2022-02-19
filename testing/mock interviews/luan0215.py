import unittest
import pprint


def get_diff(person1: dict, person2: dict) -> dict:
    """"""
    # trivial case: there is a key that exists in one dictionary and not the other
    # common case: different values for the key
    # if not person1 and person2 we can just return an empty dictionary
    # person1 == person2 we can just return an empty dictionary as well
    '''
    
    algorithm: find the dict with longest length
    dict.keys() -> name, preferred name .. etc we can put this in a set
    loop through both dictionaries and a grab the key
    1. key present, key not present
    2. key not present, key present
    3. key present in both but value different
    '''
    res = {}

    for i in person1.keys():
        if i not in person2:
            res[i] = [person1[i], None]
        elif i in person2:
            if type(i) == dict:
                temp = get_diff(i, person2[i])
                res[i] = tempdwuwqudws
            else:
                if person1[i] != person2[i]:
                    res[i] = [person1[i],person2[i]]

    for i in person2.keys():
        if i not in person1:
            res[i] = [None, person2[i]]
    pprint.pprint(res)
    return res


class Test(unittest.TestCase):
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        
        self.person1 = {
            "name": "Hoang Truong",
            "preferred_name": "Luan",
            "age": 20,
            "address": "1 Washington Sq",
            "city": "San Jose",
            "state": "CA",
            "nationality": "Vietnam",
            "bank": {
                "name": "Chase",
                "routing_number": "0123456789",
                "account_number": "0123456789"
            },
        }
        
        self.person2 = {
            "name": "Shubham Goswami",
            "age": 21,
            "address": "1 Washington Sq",
            "city": "San Jose",
            "state": "CA",
            "nationality": "India",
            "bank": {
                "name": "Chase",
                "routing_number": "0123456789",
                "account_number": "0123456789"
            }
        }
        
        


    def test1(self):
        
        print("\nTest Case 1:")

        actual_result = get_diff(self.person1, self.person2)
        
        expected_result = {
            "name": ["Hoang Truong", "Shubham Goswami"],
            "preferred_name": ["Luan", None],
            "age": [20, 21],
            "nationality": ["Vietnam", "India"]
        }
        
        self.assertEqual(expected_result, actual_result)
        
    
    
    
    def test2(self):
        
        print("\nTest Case 2:")
        
        self.person1["bank"]["name"] = "Wells Fargo"
        self.person1["bank"]["routing_number"] = "9876543210" 
        
        actual_result = get_diff(self.person1, self.person2)
        
        expected_result = {
            "name": ["Hoang Truong", "Shubham Goswami"],
            "preferred_name": ["Luan", None],
            "age": [20, 21],
            "nationality": ["Vietnam", "India"],
            "bank": {
                "name": ["Wells Fargo", "Chase"],
                "routing_number": ["9876543210", "0123456789"]
            }
        }
        
        # self.assertEqual(expected_result, actual_result)
    


if __name__ == "__main__":
    unittest.main()