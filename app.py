import json
import random
import logging

from flask import Flask, render_template, redirect, url_for
from flask import request


app = Flask(__name__)

logging.basicConfig(filename='output.txt', level=logging.DEBUG, format='')

with open('santa_map.json', 'r') as f:
    santa_map = json.load(f)
f.close()

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

with open('wishlist_info.json', 'r') as f:
    wishlist_info = json.load(f)
f.close()


@app.route("/home")
def home():
    return render_template('home.html')


# @app.route("/save_wishlist", methods=['POST'])
def save_wishlist(name, address, contact, wishlist):
    # save info
    print('SAVING INFO')
    # print(name, address, contact, wishlist)
    wishlist_info[name]["address"] = address
    wishlist_info[name]["contact"] = contact
    wishlist_info[name]["wishlist"] = wishlist

    # Serializing json
    json_object = json.dumps(wishlist_info, indent=4)

    # Writing to sample.json
    with open("wishlist_info.json", "w") as outfile:
        outfile.write(json_object)
    outfile.close()


@app.route("/grant_elf", methods=['GET', 'POST'])
def grant_elf():
    if request.method == 'POST':
        if request.form['name'] in santa_map:
            chosen_one = santa_map.get(request.form['name'])
            msg = "You already picked " + chosen_one + ", DON'T be TOOO GENEROUS..."
            if wishlist_info[chosen_one]['address'] == "":
                msg = msg + " Your Elf has not yet filled in their details, come back to me later!"
            return render_template('elf.html', msg=msg, name=chosen_one, address=wishlist_info[chosen_one]['address'], contact=wishlist_info[chosen_one]['contact'], wishlist=wishlist_info[chosen_one]['wishlist'])

        save_wishlist(request.form['name'], request.form['address'], request.form['contact'], request.form['wishlist'])

        chosen_one = random.choice(names)
        # print("chosen_one: " + chosen_one)
        while chosen_one == request.form['name']:
            if len(names) == 1:
                logging.info(request.form['name'] + " has no elf and is no one's elf")
                # logging.info("FLAG!!" + santa_map.get("Sachin Jain"))
                # logging.info("FLAG2!!" + request.form['name'])

                santa_map[request.form['name']] = santa_map.get("Sachin Jain")
                temp = santa_map.get("Sachin Jain")
                # logging.info("flag3!!" + santa_map[request.form['name']])
                santa_map["Sachin Jain"] = chosen_one
                chosen_one = temp
                break
            chosen_one = random.choice(names)
            # print("chosen_one: " + chosen_one)

        names.remove(request.form['name'])
        logging.info(names)
        santa_map[request.form['name']] = chosen_one
        json_object = json.dumps(santa_map, indent=4)
        with open("santa_map.json", "w") as outfile:
            outfile.write(json_object)
        outfile.close()

        # print(santa_map)
        msg = "Start buying gifts for " + chosen_one + ", in case you forget the name come to me, I will tell again."
        if wishlist_info[chosen_one]['address'] == "":
            msg = msg + " Your Elf has not yet filled in their details, come back to me later!"
        return render_template('elf.html', msg=msg, name=chosen_one, address=wishlist_info[chosen_one]['address'], contact=wishlist_info[chosen_one]['contact'], wishlist=wishlist_info[chosen_one]['wishlist'])
    elif request.method == 'GET':
        return redirect(url_for('home'))
    else:
        return "Not a valid HTTP method", 404
