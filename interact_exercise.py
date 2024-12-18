from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets

def func(x):
    return x

####
interact(func,x=['hello','option 2', 'option 3'])

####
interact(func,x=(-10.0,10.0,0.5))

####
@interact(x=(0,20,0.5))
def h(x=5.0):
    return x

####
interact(func,x={'one':10, 'two':20, 'three':30})

####
from IPython.display import display
def f(a,b):
    display(a+b)
    return a+b
w = interactive(f,a=10,b=20)
display(w)