# Put your app in here.
from flask import Flask, request

#we import the functions from the oprations.py
from operations import add, sub, mult, div
app = Flask(__name__)
#build a simple calculator with flask
#uses URL query params (forms) to get the nums to calc
#4 different routes

#/add calculation
@app.route('/add')
def add_two_num():
  """add a and b, which are integers"""
  #we need to get the integer as a and b
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  res = add(a,b)
  return str(res) 


@app.route('/sub')
def sub_two_num():
    """subtract a and b, which are integers"""
    #we need to get integers so we use the int
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = sub(a,b)
    #the result is always a string, so we have to stringify it
    return str(res)

@app.route('/mult')
def mult_two_num():
    """multiply two numbers a and b, which are integers"""
    #we need to get the integers so we need int
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = mult(a,b)
    #the result is always a string, so we have to sringify it
    return str(res)

@app.route('/div')
def div_two_num():
    """Divide a by b, which are integers"""
    #again we need the integers of a and b
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = div(a,b)
    #stringify the result as flask wanted it, otherwise err
    return str(res)


#further study, make a single route to deal with 4 kinds of URL
OPERATIONS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

#/math/<oprations> refered to video 11
@app.route('/math/<operations>')
def do_math(operations):
    """to deal with 4 functions with one single route"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = OPERATIONS[operations](a,b)
    return str(res)