class CountFromBy:
    def __init__(self, v: int = 0, i: int= 1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)





"""
만고자 하는 동작들
1. increase : value + increment
2. CountFromBy(m,n) : 생성자, value = m & increment = n
3. CountFromBy(increment = n) : 생성자, increment = n
4.    
"""
