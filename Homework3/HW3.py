# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None

    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        return self.top is None

    def __len__(self):
        i=0
        curr=self.top
        while curr is not None:
            i+=1
            curr=curr.next
        return i

    def push(self,value):
        temp=Node(value)
        temp.next=self.top
        self.top=temp


    def pop(self):
        if self.isEmpty():
            return None
        temp=self.top.value
        self.top=self.top.next
        return temp

    def peek(self):
        return None if self.isEmpty() else self.top.value

#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
            >>> x._isNumber(-2.3333)
        '''
        try:
            float(txt)
            return True
        except ValueError:
            return False

    def _getPostfix(self, expr) -> str | None:
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('     2 ^       4')
            '2.0 4.0 ^'
            >>> x._getPostfix('          2 ')
            '2.0'
            >>> x._getPostfix('2.1        * 5        + 3       ^ 2 +         1 +             4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2*5.34+3^2+1+4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( .5 )')
            '0.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * (           ( 5 +-3 ) ^ 2 + (1 + 4 ))')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('(2 * ( ( 5 + 3) ^ 2 + (1 + 4 )))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('((2 *((5 + 3) ^ 2 + (1 +4 ))))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2* (       -5 + 3 ) ^2+ ( 1 +4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('     2 * 5 + 3  ^ * 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5      + 3 ) ^ 2 + ( 1 +4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^  2 + ) 1 + 4 (')
            >>> x._getPostfix('2 *      5% + 3       ^ + -2 +1 +4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        txt=expr
        if not isinstance(txt,str) or txt is None or len(txt)==0:
            return None
        j=0
        while j<len(txt)-1:
            if self._isNumber(txt[j]) and txt[j+1]==" ":
                k=j+1
                while k<len(txt) and txt[k]==" ":
                    k+=1
                if k<len(txt) and self._isNumber(txt[k]):
                    return None
            j+=1
        txt:str="".join(txt.strip().split())
        #print(txt)
        j=1
        while j<len(txt)-1:
            if self._isNumber(txt[j]) and (txt[j+1]=="(" or txt[j-1]==")"):
                return None
            j+=1
        pemdas:dict[str,int]={"-":1,"+":1,"/":2,"*":2,"^":3}
        pemdas_operators=pemdas.keys()
        operands="+-/*^()"
        items:list[str]=[]
        curr_item:str=""
        j:int=0
        while j<len(txt):
            c=txt[j]
            if c!=" ":
                if self._isNumber(c) or (c=="." and c!=""):
                    curr_item+=c
                else:
                    if curr_item:
                        items.append(curr_item)
                        curr_item=""
                    if c in operands:
                        if c=="-" and (j==0 or txt[j-1] in operands):
                            curr_item+=c
                        else:
                            items.append(c)
                    else:
                        return None
            j+=1
        # print(items)
        if curr_item:
            items.append(curr_item)
        res:str=""
        openParenthesis:int=0
        if items[0] in pemdas or items[len(items)-1] in pemdas:
            return None
        for i in range(0,len(items)):
            if openParenthesis<0:
                return None
            token=items[i]
            if self._isNumber(token):
                if (token=="0" and postfixStack.peek()=="/") or (i+1!=len(items) and (items[i+1]=="(" or self._isNumber(items[i+1]))):
                    return None
                res+=str(float(token))+" "
            elif token in pemdas_operators:
                if i+1!=len(items) and items[i+1] in pemdas:
                    return None
                while(not postfixStack.isEmpty() and
                   postfixStack.peek()!="(" and
                   token!="^" and
                   (pemdas[postfixStack.peek()]>=pemdas[token] or
                    pemdas[postfixStack.peek()]==pemdas[token])):
                    res+=postfixStack.pop()+" "
                postfixStack.push(token)
            elif token=="(":
                openParenthesis+=1
                postfixStack.push(token)
            elif token==")":
                if i+1<len(items) and items[i+1]=="(":
                    return None
                while not postfixStack.isEmpty() and postfixStack.peek()!="(":
                    res+=postfixStack.pop()+" "
                if postfixStack.isEmpty():
                    return None
                postfixStack.pop()
                openParenthesis-=1
            else:
                return None
        if openParenthesis!=0:
            return None
        while not postfixStack.isEmpty():
            res+=postfixStack.pop()+" "
        return res.strip()

    @property
    def calculate(self) -> float | None:
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture

            >>> x=Calculator()
            >>> x.setExpr('4        + 3 -       2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 +          3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('      4 +           3.65  - 2        / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25      * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('2-3*4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7^2^3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ((( 10 - 2*3 )) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('      8 / 4 * (3 - 2.45 * ( 4   - 2 ^ 3 )       ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 +        2 * (         5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 +         3 * (2 + ( 3.0) * ( 5^2-2 * 3 ^ ( 2 )         ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 /3 ) ) - 2 / 3^ 2')
            >>> x.calculate
            1442.7777777777778


            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 ++ 3+ 2")
            >>> x.calculate
            >>> x.setExpr("4  3 +2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 *( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( *10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('(    3.5 ) ( 15 )')
            >>> x.calculate
            >>> x.setExpr('3 ( 5) - 15 + 85 ( 12)')
            >>> x.calculate
            >>> x.setExpr("( -2/6) + ( 5 ( ( 9.4 )))")
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        pf=self._getPostfix(self.getExpr)
        if pf is None:
            return None
        tokens=pf.split(" ")
        operators="-+/*^"
        # print(tokens)
        i:int=0
        while i<len(tokens):
            token=tokens[i]
            if self._isNumber(token):
                calcStack.push(float(token))
            elif token in operators:
                a:float=calcStack.pop()
                b:float=calcStack.pop()
                if token=="^":
                    calcStack.push(b**a)
                elif token=="+":
                    calcStack.push(b+a)
                elif token=="-":
                    calcStack.push(b-a)
                elif token=="*":
                    calcStack.push(b*a)
                elif token=="/":
                    if a==0:
                        return None
                    else:
                        calcStack.push(b/a)
            i+=1
        return calcStack.pop()
#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions:str = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        return isinstance(word,str) and len(word)>0 and word[0].isalpha() and word.isalnum()


    def _replaceVariables(self, expr)-> str | None:
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        tokens=expr.split(" ")
        j=0
        res=""
        while j<len(tokens):
            token=tokens[j]
            if token in self.states.keys():
                res+=str(self.states[token])
            elif self._isVariable(token) and token not in self.states.keys():
                return None
            else:
                res+=str(token)
            if j!=len(tokens)-1:
                res+=" "
            j+=1
        return res


    def calculateExpressions(self):
        '''
            >>> C = AdvancedCalculator()
            >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D + 2 * B')
            >>> C.states
            {}
            >>> C.calculateExpressions()
            {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 61.0}
            >>> C.states
            {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        '''
        self.states = {}
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        ans:dict[str,dict[str,str]]={}
        self.states={}
        expr:list[str]=self.expressions.split(";")
        for e in expr:
            if e.strip()[0:6]=="return":
                r=self._replaceVariables(e.strip()[6:])
                if r is None:
                    self.states={}
                    return None
                calcObj.setExpr(r)
                ans["_return_"]=calcObj.calculate
            else:
                c=e.split("=")
                r=self._replaceVariables(c[1])
                if r is None:
                    self.states={}
                    return None
                calcObj.setExpr(r)
                self.states[c[0].strip()]=calcObj.calculate
                ans[e]=self.states.copy()
        return ans


def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    #c=Calculator()
    #c.setExpr("2^3-3*2")
    #print(c.calculate)
    #print(Calculator()._getPostfix("(3)3"))
    #print(Calculator()._getPostfix(" 2.5 +         3 * (2 + (3) * ( 5^2-2 * 3 ^ ( 2 )         ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 /3 ) ) - 2 / 3^ 2").split(" "))
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    #doctest.run_docstring_examples(Calculator._getPostfix, globals(), name='HW3',verbose=True)
    #doctest.run_docstring_examples(Calculator._isNumber, globals(), name="HW3", verbose=True)
    #doctest.run_docstring_examples(Calculator.calculate, globals(), name="HW3", verbose=True)
    #doctest.run_docstring_examples(AdvancedCalculator.calculateExpressions, globals(), name="HW3", verbose=True)


if __name__ == "__main__":
    run_tests()