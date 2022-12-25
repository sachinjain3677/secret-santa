# secret-santa
Manage all your secret-santa needs in one place

# pre-requisites
* Python 3.9.13 - https://www.python.org/downloads
* Flask 2.2.2 - `pip3 install --upgrade Flask`

# setup
* `git clone git@github.com:sachinjain3677/secret-santa.git`
* `cd secret-santa`
* `export FLASK_APP=app.py`
* `export FLASK_RUN_PORT=<port>` default is 5000

# add your friends
* `app.py`, line 17
* `home.html`, line 146
* `wishlist_info_template.json`

# fresh run of the server
* `cp wishlist_info_template.json wishlist_info.json`
* `cp santa_map_template.json santa_map.json`
* `flask run`
* Find logs in `output.txt`

# resume server post intermittent halt
* Update `names` variable in `app.py` line 17 with names of remaining `Elves (people who have not been assigned to any Santa till now)`, this can be copied from the most recent log in `output.txt`
* `flask run`

# host for the world using ngrok
* get your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken
* `./ngrok config add-authtoken <authtoken>`
* `./ngrok http <port>`, must be same as flask
* pick the `Forwarding` URL given by ngrok and share with your friends to access at `<url>/home`
* Note: for a server resume post intermittent halt on flask side doesn't require a ngrok restart
* Note: an intermittent halt of ngrok doesn't require a restart of flask

## potential pitfalls
There might come a situation if case of odd number of people that a person is left without a santa and an elf.
To counter this situation just add name of anyone from your group at `app.py, line 71, 72`. Just be sure that this person is **not** the last one to fill in their wishlist.