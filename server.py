from flask import Flask
import random

random_number = random.randint(1,9)
print(random_number)
too_hight_gif = 'https://media1.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3OWs4dDBzdTZlMzBoa2duMnAzNDJxazBxZGQ5MmgxY2xlb252eW9ncSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/YKroe55zFMIwpmBCu6/giphy.webp'
too_low_gif = 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWlkYmpkMjF1bXVydWRndHk2dXZmNGUwd2ZsYm9zbzB5ZmdtZGZpNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3osxYjAburqkbbOPeg/giphy.webp'
correct_number_gif = 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2V2amxvZzJrbDN4d3o0cjUzdjZuZGl4d2RjNnluazZ3a2pra2g3ZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/oH8UEvjQ6y8RgRrRRF/200.webp'

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Guess a number between 0 and 9</h1> <img src = 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzJ5bWJheHg2OTFwbWpoYXhidXJlZHYzaGRmOTJlbTI4ZDFmNGc2MCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MAuWs1rqbfHFMWUCYH/200.webp'>"

@app.route('/<number>')
def guess_number(number):
    number = int(number)
    if random_number < number:
        return f'<h1>Your number is too high!</h1> <img src={too_hight_gif}>'
    elif random_number > number:
        return f"<h1>Your number is too low!</h1><img src={too_low_gif}>"
    else:
        return f"<h1>That's right boy!</h1><img src={correct_number_gif}>"

if __name__ == '__main__':
    app.run()