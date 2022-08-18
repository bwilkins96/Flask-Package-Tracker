from flask_sqlalchemy import SQLAlchemy
from map.map import advance_delivery

db = SQLAlchemy()

class Package(db.Model):
    __tablename__ = 'packages'

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(255), nullable=False)
    recipient = db.Column(db.String(255), nullable=False)
    origin = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255))

    @staticmethod
    def advance_all_locations():
        packages = Package.query.all()

        for package in packages:
            if package.location != 'Delivered':
                package.location = advance_delivery(package.location, package.destination)
            else:
                db.session.delete(package)

        db.session.commit()
