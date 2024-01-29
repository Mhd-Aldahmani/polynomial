class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, x):
        
        if isinstance(self.p2, Add):
            val2 = Add.evaluate(self.p2,x)
        elif isinstance(self.p2, Sub):
            val2 = Sub.evaluate(self.p2,x)
        elif isinstance(self.p2, Mul):
            val2 = Mul.evaluate(self.p2,x)
        elif isinstance(self.p2, Div):
            val2 = Div.evaluate(self.p2,x)
        elif isinstance(self.p2, X):
            val2 = x
        else :
            val2 = self.p2.i   

        if isinstance(self.p1, Add):
            val1 = Add.evaluate(self.p1,x)
        elif isinstance(self.p1, Sub):
            val1 = Sub.evaluate(self.p1,x)
        elif isinstance(self.p1, Mul):
            val1 = Mul.evaluate(self.p1,x)
        elif isinstance(self.p1, Div):
            val1 = Div.evaluate(self.p1,x)
        elif isinstance(self.p1, X):
            val1 = x
        else :
            val1 = self.p1.i  
        return int(val1) + int(val2)
            

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self, x):
        
        if isinstance(self.p2, Add):
            val2 = Add.evaluate(self.p2,x)
        elif isinstance(self.p2, Sub):
            val2 = Sub.evaluate(self.p2,x)
        elif isinstance(self.p2, Mul):
            val2 = Mul.evaluate(self.p2,x)
        elif isinstance(self.p2, Div):
            val2 = Div.evaluate(self.p2,x)
        elif isinstance(self.p2, X):
            val2 = x
        else :
            val2 = self.p2.i   

        if isinstance(self.p1, Add):
            val1 = Add.evaluate(self.p1,x)
        elif isinstance(self.p1, Sub):
            val1 = Sub.evaluate(self.p1,x)
        elif isinstance(self.p1, Mul):
            val1 = Mul.evaluate(self.p1,x)
        elif isinstance(self.p1, Div):
            val1 = Div.evaluate(self.p1,x)
        elif isinstance(self.p1, X):
            val1 = x
        else :
            val1 = self.p1.i  
        return int(val1) * int(val2)


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, x):
        
        if isinstance(self.p2, Add):
            val2 = Add.evaluate(self.p2,x)
        elif isinstance(self.p2, Sub):
            val2 = Sub.evaluate(self.p2,x)
        elif isinstance(self.p2, Mul):
            val2 = Mul.evaluate(self.p2,x)
        elif isinstance(self.p2, Div):
            val2 = Div.evaluate(self.p2,x)
        elif isinstance(self.p2, X):
            val2 = x
        else :
            val2 = self.p2.i   

        if isinstance(self.p1, Add):
            val1 = Add.evaluate(self.p1,x)
        elif isinstance(self.p1, Sub):
            val1 = Sub.evaluate(self.p1,x)
        elif isinstance(self.p1, Mul):
            val1 = Mul.evaluate(self.p1,x)
        elif isinstance(self.p1, Div):
            val1 = Div.evaluate(self.p1,x)
        elif isinstance(self.p1, X):
            val1 = x
        else :
            val1 = self.p1.i  
        return int(val1) - int(val2)
    
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)
    def evaluate(self, x):
        
        if isinstance(self.p2, Add):
            val2 = Add.evaluate(self.p2,x)
        elif isinstance(self.p2, Sub):
            val2 = Sub.evaluate(self.p2,x)
        elif isinstance(self.p2, Mul):
            val2 = Mul.evaluate(self.p2,x)
        elif isinstance(self.p2, Div):
            val2 = Div.evaluate(self.p2,x)
        elif isinstance(self.p2, X):
            val2 = x
        else :
            val2 = self.p2.i   

        if isinstance(self.p1, Add):
            val1 = Add.evaluate(self.p1,x)
        elif isinstance(self.p1, Sub):
            val1 = Sub.evaluate(self.p1,x)
        elif isinstance(self.p1, Mul):
            val1 = Mul.evaluate(self.p1,x)
        elif isinstance(self.p1, Div):
            val1 = Div.evaluate(self.p1,x)
        elif isinstance(self.p1, X):
            val1 = x
        else :
            val1 = self.p1.i
        
        return  val1/val2



poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))

poly = Add(Int(3), Mul(X(),X()))
print(poly, " = " , poly.evaluate(3))