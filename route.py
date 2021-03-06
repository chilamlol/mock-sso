from flask import request

from api_request import *
from app import app
from flask import render_template
from datetime import *

iplist = {}


def get_my_ip():
    return request.remote_addr


def getTodayDate():
    today = date.today()
    return today.strftime("%d/%m/%Y")  # 15/02/2022


@app.route('/', methods=['GET', 'POST'])
def home():
    print(iplist)
    if get_my_ip() in iplist:
        return render_template("successful.html")
    else:
        if request.method == 'POST':
            username = request.form["name"]
            iplist.update({get_my_ip(): username})
            return render_template("successful.html")

    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')


"""
def completeAssignment(username):
    try:
        assignmentList = getMethodJsonFromApi(getAssignmentListApiUrl(username))
        if assignmentList:
            for assignment in assignmentList:
                mealDetailList = getMethodJsonFromApi(getMealCollectionDetailApiUrl(username, assignment["processId"]))

                for mealDetail in mealDetailList["data"]:
                    if mealDetail["c_menudate"] == getTodayDate():
                        postMethodJsonFromApi(getCompleteAssignmentApiUrl(username, assignment["activityId"]))
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
"""