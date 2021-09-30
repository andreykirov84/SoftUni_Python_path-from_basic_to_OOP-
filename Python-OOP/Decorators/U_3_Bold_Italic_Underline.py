from functools import wraps


def make_bold(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return wrapped


def make_italic(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"
    return wrapped


def make_underline(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<u>" + fn(*args, **kwargs) + "</u>"
    return wrapped


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
# <b><i><u>Hello, Peter</u></i></b>


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
# <b><i><u>Hello, Peter, George</u></i></b>
