from flask import request
from flask import jsonify
from app import app
from flask import render_template, url_for, redirect

iplist = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    if get_my_ip() in iplist:
        print(iplist[get_my_ip()])
    else:
        if request.method == 'POST':
            iplist.update({get_my_ip(): request.form["name"]})

    return render_template('home.html')


def get_my_ip():
    return request.remote_addr


if __name__ == '__main__':
    app.run(host='0.0.0.0')
