from app import db
from app.my_project.auth.domain.models import (
    Company, Client, Terminal, ServiceType, PaymentMethod,
    Payment, Invoice, Master, Service, ServiceMaster,
    ClientService, ServiceFeedback
)

# --- Company DAO ---
class CompanyDAO:
    @staticmethod
    def get_all():
        return Company.query.all()

    @staticmethod
    def get_by_id(company_id):
        return Company.query.get(company_id)

    @staticmethod
    def create(company_data):
        new_company = Company(**company_data)
        db.session.add(new_company)
        db.session.commit()
        return new_company

    @staticmethod
    def update(company_id, update_data):
        company = Company.query.get(company_id)
        if company:
            for key, value in update_data.items():
                setattr(company, key, value)
            db.session.commit()
        return company

    @staticmethod
    def delete(company_id):
        company = Company.query.get(company_id)
        if company:
            db.session.delete(company)
            db.session.commit()


# --- Client DAO ---
class ClientDAO:
    @staticmethod
    def get_all():
        return Client.query.all()

    @staticmethod
    def get_by_id(client_id):
        return Client.query.get(client_id)

    @staticmethod
    def create(client_data):
        new_client = Client(**client_data)
        db.session.add(new_client)
        db.session.commit()
        return new_client

    @staticmethod
    def update(client_id, update_data):
        client = Client.query.get(client_id)
        if client:
            for key, value in update_data.items():
                setattr(client, key, value)
            db.session.commit()
        return client

    @staticmethod
    def delete(client_id):
        client = Client.query.get(client_id)
        if client:
            db.session.delete(client)
            db.session.commit()


# --- Terminal DAO ---
class TerminalDAO:
    @staticmethod
    def get_all():
        return Terminal.query.all()

    @staticmethod
    def get_by_id(terminal_id):
        return Terminal.query.get(terminal_id)

    @staticmethod
    def create(terminal_data):
        new_terminal = Terminal(**terminal_data)
        db.session.add(new_terminal)
        db.session.commit()
        return new_terminal

    @staticmethod
    def update(terminal_id, update_data):
        terminal = Terminal.query.get(terminal_id)
        if terminal:
            for key, value in update_data.items():
                setattr(terminal, key, value)
            db.session.commit()
        return terminal

    @staticmethod
    def delete(terminal_id):
        terminal = Terminal.query.get(terminal_id)
        if terminal:
            db.session.delete(terminal)
            db.session.commit()


# --- ServiceType DAO ---
class ServiceTypeDAO:
    @staticmethod
    def get_all():
        return ServiceType.query.all()

    @staticmethod
    def get_by_id(service_type_id):
        return ServiceType.query.get(service_type_id)

    @staticmethod
    def create(service_type_data):
        new_service_type = ServiceType(**service_type_data)
        db.session.add(new_service_type)
        db.session.commit()
        return new_service_type

    @staticmethod
    def update(service_type_id, update_data):
        service_type = ServiceType.query.get(service_type_id)
        if service_type:
            for key, value in update_data.items():
                setattr(service_type, key, value)
            db.session.commit()
        return service_type

    @staticmethod
    def delete(service_type_id):
        service_type = ServiceType.query.get(service_type_id)
        if service_type:
            db.session.delete(service_type)
            db.session.commit()


# --- PaymentMethod DAO ---
class PaymentMethodDAO:
    @staticmethod
    def get_all():
        return PaymentMethod.query.all()

    @staticmethod
    def get_by_id(payment_method_id):
        return PaymentMethod.query.get(payment_method_id)

    @staticmethod
    def create(payment_method_data):
        new_payment_method = PaymentMethod(**payment_method_data)
        db.session.add(new_payment_method)
        db.session.commit()
        return new_payment_method

    @staticmethod
    def update(payment_method_id, update_data):
        payment_method = PaymentMethod.query.get(payment_method_id)
        if payment_method:
            for key, value in update_data.items():
                setattr(payment_method, key, value)
            db.session.commit()
        return payment_method

    @staticmethod
    def delete(payment_method_id):
        payment_method = PaymentMethod.query.get(payment_method_id)
        if payment_method:
            db.session.delete(payment_method)
            db.session.commit()


# --- Payment DAO ---
class PaymentDAO:
    @staticmethod
    def get_all():
        return Payment.query.all()

    @staticmethod
    def get_by_id(payment_id):
        return Payment.query.get(payment_id)

    @staticmethod
    def create(payment_data):
        new_payment = Payment(**payment_data)
        db.session.add(new_payment)
        db.session.commit()
        return new_payment

    @staticmethod
    def update(payment_id, update_data):
        payment = Payment.query.get(payment_id)
        if payment:
            for key, value in update_data.items():
                setattr(payment, key, value)
            db.session.commit()
        return payment

    @staticmethod
    def delete(payment_id):
        payment = Payment.query.get(payment_id)
        if payment:
            db.session.delete(payment)
            db.session.commit()


# --- Invoice DAO ---
class InvoiceDAO:
    @staticmethod
    def get_all():
        return Invoice.query.all()

    @staticmethod
    def get_by_id(invoice_id):
        return Invoice.query.get(invoice_id)

    @staticmethod
    def create(invoice_data):
        new_invoice = Invoice(**invoice_data)
        db.session.add(new_invoice)
        db.session.commit()
        return new_invoice

    @staticmethod
    def update(invoice_id, update_data):
        invoice = Invoice.query.get(invoice_id)
        if invoice:
            for key, value in update_data.items():
                setattr(invoice, key, value)
            db.session.commit()
        return invoice

    @staticmethod
    def delete(invoice_id):
        invoice = Invoice.query.get(invoice_id)
        if invoice:
            db.session.delete(invoice)
            db.session.commit()


# --- Master DAO ---
class MasterDAO:
    @staticmethod
    def get_all():
        return Master.query.all()

    @staticmethod
    def get_by_id(master_id):
        return Master.query.get(master_id)

    @staticmethod
    def create(master_data):
        new_master = Master(**master_data)
        db.session.add(new_master)
        db.session.commit()
        return new_master

    @staticmethod
    def update(master_id, update_data):
        master = Master.query.get(master_id)
        if master:
            for key, value in update_data.items():
                setattr(master, key, value)
            db.session.commit()
        return master

    @staticmethod
    def delete(master_id):
        master = Master.query.get(master_id)
        if master:
            db.session.delete(master)
            db.session.commit()


# --- ClientService DAO ---
class ClientServiceDAO:
    @staticmethod
    def add_client_service(client_id, service_id):
        new_client_service = ClientService(client_id=client_id, service_id=service_id)
        db.session.add(new_client_service)
        db.session.commit()
        return new_client_service


# --- ServiceFeedback DAO ---
class ServiceFeedbackDAO:
    @staticmethod
    def get_all():
        return ServiceFeedback.query.all()

    @staticmethod
    def add_feedback(service_id, client_id, feedback_text, rating):
        feedback = ServiceFeedback(
            service_id=service_id,
            client_id=client_id,
            feedback_text=feedback_text,
            rating=rating
        )
        db.session.add(feedback)
        db.session.commit()

    @staticmethod
    def delete_feedback(feedback_id):
        feedback = ServiceFeedback.query.get(feedback_id)
        if feedback:
            db.session.delete(feedback)
            db.session.commit()
