from flask import Flask
import random

app=Flask(__name__)

n=random.randint(0,9)

@app.route('/')
def display():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media0.giphy.com/media/tsX3YMWYzDPjAARfeg/giphy.webp?cid=ecf05e47o6nfz99z5wcpkju8tversfh0ce1n7bqqacglb7qb&ep=v1_gifs_trending&rid=giphy.webp&ct=g">'

@app.route('/<int:x>')
def guess(x):
    if x<n:
        return '<h1 style="color:red">Too low!</h1>' \
               
    elif x>n:
        return '<h1 style="color:purple">Too high!</h1>' \

    elif x==n:
        return '<h1 style="color:green">Correct!</h1>' \

if __name__=="__main__":
    app.run(debug=True)