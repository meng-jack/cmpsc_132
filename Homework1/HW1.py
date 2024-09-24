# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

def get_path(file_name):
    """
        Returns a string with the absolute path of a given file_name located in the same directory as this script

        # Do not modify this function in any way

        >>> get_path('words.txt')   # HW1.py and words.txt located in HW1 folder
        'G:\My Drive\CMPSC132\HW1\words.txt'
    """
    import os
    target_path = os.path.join(os.path.dirname(__file__), file_name)
    return target_path


def rectangle(perimeter, area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    # - YOUR CODE STARTS HERE
    length = (perimeter + ((perimeter ** 2) - (16 * area)) ** 0.5) / 4
    width = area / length
    if length.is_integer() and width.is_integer():
        return int(length if length > width else width)
    else:
        return False


def to_decimal(oct_num):
    """
        >>> to_decimal(237)
        159
        >>> to_decimal(35)
        29
        >>> to_decimal(600)
        384
        >>> to_decimal(420)
        272
    """
    # - YOUR CODE STARTS HERE
    dec = 0
    i = 0
    while oct_num > 0:
        dec += (8 ** i) * (oct_num % 10)
        oct_num //= 10
        i += 1
    return dec


def has_hoagie(num):
    """
        >>> has_hoagie(737)
        True
        >>> has_hoagie(35)
        False
        >>> has_hoagie(-6060)
        True
        >>> has_hoagie(-111)
        True
        >>> has_hoagie(6945)
        False
    """
    # - YOUR CODE STARTS HERE
    num = abs(num)
    if num < 100:
        return False
    r = num % 10
    m = num // 10 % 10
    l = num // 100 % 10
    if r == l:
        return True
    while num > 0:
        if r == l:
            return True
        num //= 10
        if num % 10 == 0:
            return False
        r = m
        m = l
        l = num // 100 % 10
    return False


def is_identical(num_1, num_2):
    """
        >>> is_identical(51111315, 51315)
        True
        >>> is_identical(7006600, 7706000)
        True
        >>> is_identical(135, 765)
        False
        >>> is_identical(2023, 20)
        False
    """
    # - YOUR CODE STARTS HERE
    prev_1 = None
    prev_2 = None
    new_1 = 0
    new_2 = 0
    while num_1 > 0:
        if prev_1 != None and prev_1 != num_1 % 10:
            new_1 = new_1 * 10 + (num_1 % 10)
        prev_1 = num_1 % 10
        num_1 //= 10
    while num_2 > 0:
        if prev_2 != None and prev_2 != num_2 % 10:
            new_2 = new_2 * 10 + (num_2 % 10)
        prev_2 = num_2 % 10
        num_2 //= 10
    return new_1 == new_2


def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    # - YOUR CODE STARTS HERE
    seq = [num]
    while num > 1:
        if num % 2 == 0:
            seq.append(num // 2)
            num //= 2
        else:
            seq.append(3 * num + 1)
            num = 3 * num + 1
    return seq


def overloaded_add(d, key, value):
    """
        Adds the key value pair to the dictionary. If the key is already in the dictionary, the value is made a list and the new value is appended to it.
        >>> d = {"Alice": "Engineer"}
        >>> overloaded_add(d, "Bob", "Manager")
        >>> overloaded_add(d, "Alice", "Sales")
        >>> d == {"Alice": ["Engineer", "Sales"], "Bob": "Manager"}
        True
    """
    # - YOUR CODE STARTS HERE
    if key not in d:
        d[key] = value
    else:
        if type(d[key]) == list:
            d[key].append(value)
        else:
            d[key] = [d[key], value]


def by_department(d):
    """
        >>> employees = {
        ...    1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},
        ...    2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},
        ...    3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},
        ...    4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},
        ...    5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}
        ...    }

        >>> by_department(employees)
        {'Sales': [{'emp_id': 1, 'name': 'John Doe', 'position': 'Manager'}], 'Finance': [{'emp_id': 2, 'name': 'Sara Miller', 'position': 'Budget Advisor'}, {'emp_id': 4, 'name': 'Bob Johnson', 'position': 'Analyst'}], 'Engineering': [{'emp_id': 3, 'name': 'Jane Smith', 'position': 'Engineer'}, {'emp_id': 5, 'name': 'Clark Wayne', 'position': 'Senior Developer'}]}
    """
    # - YOUR CODE STARTS HERE
    temp = {}
    for key in d:
        new_fmt = {"emp_id": key, "name": d[key]
                   ["name"], "position": d[key]["position"]}
        if d[key]["department"] in temp:
            temp[d[key]["department"]].append(new_fmt)
        else:
            temp[d[key]["department"]] = [new_fmt]
    return temp


def successors(file_name):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> returnedDict
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:
        # You might change .read() for .readlines() if it suits your implementation better
        contents = file.read()
    # --- YOU CODE STARTS HERE
    items = []
    for item in contents.replace("\n", " ").split(" "):
        if item.isalnum():
            items.append(item)
        else:
            curr = ""
            for char in item:
                if char.isalnum():
                    curr += char
                else:
                    if curr:
                        items.append(curr)
                        curr = ""
                    if char.strip() != None:
                        items.append(char)
            if curr:
                items.append(curr)
    all_words = {}
    if len(items) > 0:
        all_words["."] = [items[0]]
    for i in range(0, len(items) - 1, 1):
        if items[i] not in all_words:
            all_words[items[i]] = [items[i+1]]
        elif items[i+1] not in all_words[items[i]]:
            all_words[items[i]].append(items[i+1])
    return all_words


def addToTrie(trie, word):
    """
        The following dictionary represents the trie of the words "A", "I", "Apple":
            {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}}

        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    # - YOUR CODE STARTS HERE
    for c in word:
        if c not in trie:
            trie[c] = {}
        trie = trie[c]
    trie["word"] = True


def createDictionaryTrie(file_name):
    """
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:
        # You might change .read() for .readlines() if it suits your implementation better
        contents = file.read()
    # - YOUR CODE STARTS HERE
    trie = {}
    for word in contents.split("\n"):
        word = word.lower()
        level = trie
        for c in word:
            if c not in level:
                level[c] = {}
            level = level[c]
        level["word"] = True
    return trie


def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    # - YOUR CODE STARTS HERE
    level = trie
    for c in word:
        if c not in level:
            return False
        level = level[c]
    return True


def run_tests():
    import doctest
    # Run start tests in all docstrings
    #print(successors("items.txt") == {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': [
    #      'some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']})
    # doctest.testmod(verbose=True)
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    # doctest.run_docstring_examples(
    #    successors, globals(), name='HW1', verbose=True)


if __name__ == "__main__":
    run_tests()
