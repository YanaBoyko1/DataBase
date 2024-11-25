from app import db

# Company Table
class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(255))
    phone = db.Column(db.String(20))

    terminals = db.relationship('Terminal', backref='company', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone
        }

# Terminal Table
class Terminal(db.Model):
    __tablename__ = 'terminal'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    address = db.Column(db.String(255))
    gps = db.Column(db.String(100))
    manufacturer = db.Column(db.String(220))
    date = db.Column(db.Date)

    services = db.relationship('Service', backref='terminal', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "company_id": self.company_id,
            "address": self.address,
            "gps": self.gps,
            "manufacturer": self.manufacturer,
            "date": self.date
        }

# Service Type Table
class ServiceType(db.Model):
    __tablename__ = 'service_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    services = db.relationship('Service', backref='service_type', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

# Client Table
class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    phone = db.Column(db.String(20))

    feedbacks = db.relationship('ServiceFeedback', backref='client', lazy=True)
    invoices = db.relationship('Invoice', backref='client', lazy=True)
    client_services = db.relationship('ClientService', backref='client', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone
        }

# Payment Method Table
class PaymentMethod(db.Model):
    __tablename__ = 'payment_method'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))

    payments = db.relationship('Payment', backref='payment_method', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

# Payment Table
class Payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_method.id'), nullable=False)
    date = db.Column(db.Date)
    payment_amount = db.Column(db.Numeric(10, 2))

    invoices = db.relationship('Invoice', backref='payment', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "payment_method_id": self.payment_method_id,
            "date": self.date,
            "payment_amount": self.payment_amount
        }

class Invoice(db.Model):
    __tablename__ = 'invoice'

    client_id = db.Column(db.Integer, db.ForeignKey('client.id', ondelete='CASCADE'), primary_key=True)
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id', ondelete='CASCADE'), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "payment_id": self.payment_id,
            "id": self.id,
            "date": str(self.date),
            "total_amount": float(self.total_amount)
        }


# Master Table
class Master(db.Model):
    __tablename__ = 'master'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    specialization = db.Column(db.String(45))

    service_masters = db.relationship('ServiceMaster', backref='master', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "specialization": self.specialization
        }

# Service Table
class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    terminal_id = db.Column(db.Integer, db.ForeignKey('terminal.id'), nullable=False)
    date = db.Column(db.Date)
    cost = db.Column(db.Numeric(10, 2))
    service_type_id = db.Column(db.Integer, db.ForeignKey('service_type.id'), nullable=False)

    feedbacks = db.relationship('ServiceFeedback', backref='service', lazy=True)
    service_masters = db.relationship('ServiceMaster', backref='service', lazy=True)
    client_services = db.relationship('ClientService', backref='service', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "terminal_id": self.terminal_id,
            "date": self.date,
            "cost": self.cost,
            "service_type_id": self.service_type_id
        }

# ServiceFeedback Table
class ServiceFeedback(db.Model):
    __tablename__ = 'service_feedback'
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    feedback_text = db.Column(db.Text)
    rating = db.Column(db.Integer, nullable=False)
    feedback_date = db.Column(db.Date, default=db.func.current_date())

    def to_dict(self):
        return {
            "id": self.id,
            "service_id": self.service_id,
            "client_id": self.client_id,
            "feedback_text": self.feedback_text,
            "rating": self.rating,
            "feedback_date": self.feedback_date
        }

# ServiceMaster Table
class ServiceMaster(db.Model):
    __tablename__ = 'service_master'
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)
    master_id = db.Column(db.Integer, db.ForeignKey('master.id'), primary_key=True)
    work_duration = db.Column(db.Numeric(5, 2))
    cost = db.Column(db.Numeric(10, 2))

    def to_dict(self):
        return {
            "service_id": self.service_id,
            "master_id": self.master_id,
            "work_duration": self.work_duration,
            "cost": self.cost
        }

# ClientService Table
class ClientService(db.Model):
    __tablename__ = 'client_service'
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "service_id": self.service_id
        }
