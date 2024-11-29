from app import db

class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(255))
    phone = db.Column(db.String(20))

    # Вилучено зв'язок з клієнтами
    # clients = db.relationship('Client', backref='company', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone
        }


class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    phone = db.Column(db.String(20))

    # Вилучено зв'язок з компанією
    # company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    # Зв'язок з сервісами (M:N)
    services = db.relationship('Service', secondary='client_service', backref='clients')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone
        }



class Terminal(db.Model):
    __tablename__ = 'terminal'

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'))
    address = db.Column(db.String(255))
    gps = db.Column(db.String(100))
    manufacturer = db.Column(db.String(220))
    date = db.Column(db.Date)

    company = db.relationship("Company", backref=db.backref("terminals", cascade="all, delete-orphan"))

    def to_dict(self):
        return {
            "id": self.id,
            "company_id": self.company_id,
            "address": self.address,
            "gps": self.gps,
            "manufacturer": self.manufacturer,
            "date": self.date
        }


class ServiceType(db.Model):
    __tablename__ = 'service_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class PaymentMethod(db.Model):
    __tablename__ = 'payment_method'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Payment(db.Model):
    __tablename__ = 'payment'

    id = db.Column(db.Integer, primary_key=True)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_method.id', ondelete='CASCADE'))
    date = db.Column(db.Date)
    payment_amount = db.Column(db.Numeric(10, 2))

    payment_method = db.relationship("PaymentMethod", backref=db.backref("payments", cascade="all, delete-orphan"))

    def to_dict(self):
        return {
            "id": self.id,
            "payment_method_id": self.payment_method_id,
            "date": self.date,
            "payment_amount": self.payment_amount
        }


class Invoice(db.Model):
    __tablename__ = 'invoice'

    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id', ondelete='CASCADE'), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id', ondelete='CASCADE'))
    date = db.Column(db.Date)
    total_amount = db.Column(db.Numeric(10, 2))

    client = db.relationship("Client", backref=db.backref("invoices", cascade="all, delete-orphan"))
    payment = db.relationship("Payment", backref=db.backref("invoices", cascade="all, delete-orphan"))

    def to_dict(self):
        return {
            "payment_id": self.payment_id,
            "id": self.id,
            "client_id": self.client_id,
            "date": self.date,
            "total_amount": self.total_amount
        }


class Service(db.Model):
    __tablename__ = 'service'

    id = db.Column(db.Integer, primary_key=True)
    terminal_id = db.Column(db.Integer, db.ForeignKey('terminal.id', ondelete='CASCADE'))
    date = db.Column(db.Date)
    cost = db.Column(db.Numeric(10, 2))
    service_type_id = db.Column(db.Integer, db.ForeignKey('service_type.id', ondelete='CASCADE'))

    terminal = db.relationship("Terminal", backref=db.backref("services", cascade="all, delete-orphan"))
    service_type = db.relationship("ServiceType", backref=db.backref("services", cascade="all, delete-orphan"))

    def to_dict(self):
        return {
            "id": self.id,
            "terminal_id": self.terminal_id,
            "date": self.date,
            "cost": self.cost,
            "service_type_id": self.service_type_id
        }


class Master(db.Model):
    __tablename__ = 'master'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    specialization = db.Column(db.String(45))

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "specialization": self.specialization
        }


class ServiceMaster(db.Model):
    __tablename__ = 'service_master'

    service_id = db.Column(db.Integer, db.ForeignKey('service.id', ondelete='CASCADE'), primary_key=True)
    master_id = db.Column(db.Integer, db.ForeignKey('master.id', ondelete='CASCADE'), primary_key=True)
    work_duration = db.Column(db.Numeric(5, 2))
    cost = db.Column(db.Numeric(10, 2))

    service = db.relationship("Service", backref=db.backref("service_masters", cascade="all, delete-orphan"))
    master = db.relationship("Master", backref=db.backref("service_masters", cascade="all, delete-orphan"))

    def to_dict(self):
        return {
            "service_id": self.service_id,
            "master_id": self.master_id,
            "work_duration": self.work_duration,
            "cost": self.cost
        }


# Зв'язкова таблиця для M:N між Client та Service
class ClientService(db.Model):
    __tablename__ = 'client_service'

    client_id = db.Column(db.Integer, db.ForeignKey('client.id', ondelete='CASCADE'), primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id', ondelete='CASCADE'), primary_key=True)

    client = db.relationship("Client", backref=db.backref("client_services", cascade="all, delete-orphan"))
    service = db.relationship("Service", backref=db.backref("client_services", cascade="all, delete-orphan"))

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "service_id": self.service_id
        }
