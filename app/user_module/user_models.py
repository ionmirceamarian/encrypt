from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

"""
Models for user
"""

class User(db.Model):
    """
    This class represents the user table
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
    password = db.Column(db.Text)   

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<id: {}>'.format(self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()