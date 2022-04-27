from app.extensions import db

"""
Models for license
"""

class License(db.Model):
    """
    This class represents the license table
    """
    __tablename__ = 'license'

    id = db.Column(db.Integer, primary_key=True)
    certificate = db.Column(db.Text)
    sku = db.Column(db.String(100))
    tenant = db.Column(db.String(100))
    name_space = db.Column(db.String(100))
    cluster = db.Column(db.String(100))
    client_name = db.Column(db.String(100))
    sku = db.Column(db.String(100))
    exp_date  = db.Column(db.DateTime)
    cluster_id = db.Column(db.String(100))
    pods = db.Column(db.Integer)
    encrypted = db.Column(db.String(1000))
    online = db.Column(db.Boolean) 
   
    def __repr__(self):
        return '<id: {}>'.format(self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()