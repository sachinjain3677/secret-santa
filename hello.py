from flask import Flask, render_template
from flask import request
import random

app = Flask(__name__)

santa_map = {}
names = ["Abhiruchi Chaudhari",
         "Arpan Barman",
         "Arpit Gupta",
         "Giri Jagumantri",
         "Karthik Balasubramanian",
         "Manish Barman",
         "Mansi Joshi",
         "Pallavi Mittal",
         "Sachin Jain",
         "Shashank Shekhar",
         "Sunil Raj",
         "Sushaanth P",
         "Vibhas Goyal"]


@app.route("/getYourElf")
def hello_world():
    if request.method == 'POST':
        if request.form.get('replay') == "It's me":
            print("Button hit!")
    else:
        if request.remote_addr in santa_map:
            return "You already picked " + santa_map.get(request.remote_addr) + ", DON'T be TOOO GENEROUS!!"

        chosen_one = random.choice(names)
        names.remove(chosen_one)
        santa_map[request.remote_addr] = chosen_one
        print(santa_map)
        # return "Start buying gifts for " + chosen_one + ", in case you forget the name come to me, I will tell again."
        return render_template('index.html')
