from flask import Flask, render_template, redirect
from app.config import Config
from app.shipping_request import ShippingForm

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def head():
    return 'Package Tracker'

@app.route('/new_package', methods=['GET', 'POST'])
def package():
    form = ShippingForm()

    print(form.validate_on_submit())
    print(form.origin.data)

    if form.sender.data and form.recipient.data:
        return redirect('/')

    return render_template('shipping_form.html', form=form)
