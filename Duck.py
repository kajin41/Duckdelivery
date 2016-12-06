import Config
import Models
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    currentUser = '3'
    newOrders = {}
    mOrders = {}
    for order in Config.orders:
        print(Config.orders[order].deliverer)
        if Config.orders[order].deliverer == Config.users['1'].id:
            newOrders[order] = Config.orders[order]
        elif Config.orders[order].deliverer == currentUser:
            mOrders[order] = Config.orders[order]
    print(mOrders, newOrders)
    return render_template('deliverView.html', mOrders=mOrders, newOrders=newOrders, currentUser=Config.users[currentUser])


@app.route('/<user>/<order>', methods=['GET', 'POST'])
def map(user, order):
    if request.method == 'GET':
        if Config.orders[order].deliverer == user:
            return render_template('map.html', order=Config.orders[order], user=user, active=True)
        else:
            return render_template('map.html', order=Config.orders[order], user=user, active=False)
    else:
        if Config.orders[order].deliverer == user:
            if request.form['confirm'] == Config.orders[order].confirmationId:
                del Config.orders[order]
                return redirect('/')
            else:
                return render_template('map.html', order=Config.orders[order], user=user, active=True)
        else:
            Config.orders[order].deliverer = user
            return redirect('/')


if __name__ == '__main__':
    Models.init_data()
    print(Config.users)
    print(Config.users['1'].name)
    app.run()
