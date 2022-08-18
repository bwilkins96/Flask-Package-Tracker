from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from app.config import Config
from app.shipping_request import ShippingForm
from app.models import Package, db

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def head():
    packages = Package.query.all()
    return render_template('package_status.html', packages=packages)

@app.route('/new_package', methods=['GET', 'POST'])
def package():
    form = ShippingForm()

    if form.validate_on_submit():
        data = form.data
        new_package = Package(sender=data['sender'], recipient=data['recipient'],
                              origin=data['origin'], destination=data['destination'],
                              location=data['origin'])

        db.session.add(new_package)
        db.session.commit()

        Package.advance_all_locations()
        return redirect('/')

    return render_template('shipping_form.html', form=form)
