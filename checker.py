from flask import session
from functools import wraps

##
# 프로세스는 대강 이러하다.
# 1. i = outer(), i 는 outer 의 반환값을 받는다. 하지만 여전히 outer 는 호출된다.
# 2. 아래 함수는 wrapper() 내부함수를 반환한다.
# 3. 하지만 여전히 check 함수는 실행된다.
# 4. 우리는 리턴 wrapper 를 변수에 할당할 수 있다.
# #

def check_logged_in(func) -> object:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in'
    return wrapper()

