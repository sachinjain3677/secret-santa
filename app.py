import json
import random

from flask import Flask, render_template, redirect, url_for
from flask import request


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


wishlist_info = {
                "Abhiruchi Chaudhari": {
                    "address": "",
                    "contact": "",
                    "wishlist": ""
                },
                "Arpan Barman": {
                    "address": "",
                    "contact": "",
                    "wishlist": ""
                },
                "Arpit Gupta": {
                     "address": "",
                     "contact": "",
                     "wishlist": ""
                },
                "Giri Jagumantri": {
                     "address": "",
                     "contact": "",
                     "wishlist": ""
                },
                "Karthik Balasubramanian": {
                     "address": "",
                     "contact": "",
                     "wishlist": ""
                },
                "Manish Barman": {
                     "address": "",
                     "contact": "",
                     "wishlist": ""
                },
                "Mansi Joshi": {
                     "address": "",
                     "contact": "",
                     "wishlist": ""
                },
                "Pallavi Mittal": {
                     "address": "",
                     "contact": "",
                     "wishlist": ""
                },
                "Sachin Jain": {
                     "address": "",
                     "contact": "",
                     "wishlist": ""
                },
                "Shashank Shekhar": {
                     "address": "",
                     "contact": "",
                     "wishlist": ""
                },
                "Sunil Raj": {
                     "address": "",
                     "contact": "",
                     "wishlist": ""
                },
                "Sushaanth P": {
                     "address": "",
                     "contact": "",
                     "wishlist": ""
                },
                "Vibhas Goyal": {
                     "address": "",
                     "contact": "",
                     "wishlist": ""
                }
                }


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


@app.route("/grant_elf", methods=['GET', 'POST'])
def grant_elf():
    if request.method == 'POST':
        if request.remote_addr in santa_map:
            chosen_one = santa_map.get(request.remote_addr)
            msg = "You already picked " + chosen_one + ", DON'T be TOOO GENEROUS..."
            if wishlist_info[chosen_one]['address'] == "":
                msg = msg + " Your Elf has not yet filled in their details, come back to me later!"
            return render_template('elf.html', msg=msg, name=chosen_one, address=wishlist_info[chosen_one]['address'], contact=wishlist_info[chosen_one]['contact'], wishlist=wishlist_info[chosen_one]['wishlist'])

        save_wishlist(request.form['name'], request.form['address'], request.form['contact'], request.form['wishlist'])

        chosen_one = random.choice(names)
        # print("chosen_one: " + chosen_one)
        while chosen_one.split()[0] == request.form['name']:
            chosen_one = random.choice(names)
            # print("chosen_one: " + chosen_one)

        names.remove(chosen_one)
        santa_map[request.remote_addr] = chosen_one

        print(santa_map)
        msg = "Start buying gifts for " + chosen_one + ", in case you forget the name come to me, I will tell again."
        if wishlist_info[chosen_one]['address'] == "":
            msg = msg + " Your Elf has not yet filled in their details, come back to me later!"
        return render_template('elf.html', msg=msg, name=chosen_one, address=wishlist_info[chosen_one]['address'], contact=wishlist_info[chosen_one]['contact'], wishlist=wishlist_info[chosen_one]['wishlist'])
    elif request.method == 'GET':
        if request.remote_addr in santa_map:
            msg = "You already picked " + santa_map.get(request.remote_addr) + ", DON'T be TOOO GENEROUS!!"
            chosen_one = santa_map.get(request.remote_addr)
            if wishlist_info[chosen_one]['address'] == "":
                msg = msg + " Your Elf has not yet filled in their details, come back to me later!"
            return render_template('elf.html', msg=msg, name=chosen_one, address=wishlist_info[chosen_one]['address'], contact=wishlist_info[chosen_one]['contact'], wishlist=wishlist_info[chosen_one]['wishlist'])
        else:
            return redirect(url_for('home'))
    else:
        return "Not a valid HTTP method", 404
