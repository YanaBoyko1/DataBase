# app/my_project/auth/service/service.py

from app.my_project.auth.dao.dao import CompanyDAO, ClientDAO, TerminalDAO, ServiceTypeDAO, PaymentMethodDAO, PaymentDAO, InvoiceDAO, ServiceDAO, MasterDAO

class CompanyService:
    @staticmethod
    def get_all_companies():
        return CompanyDAO.get_all()

    @staticmethod
    def get_company_by_id(company_id):
        return CompanyDAO.get_by_id(company_id)

    @staticmethod
    def create_company(company_data):
        return CompanyDAO.create(company_data)

    @staticmethod
    def update_company(company_id, update_data):
        return CompanyDAO.update(company_id, update_data)

    @staticmethod
    def delete_company(company_id):
        CompanyDAO.delete(company_id)

class ClientService:
    @staticmethod
    def get_all_clients():
        return ClientDAO.get_all()

    @staticmethod
    def get_client_by_id(client_id):
        return ClientDAO.get_by_id(client_id)

    @staticmethod
    def create_client(client_data):
        return ClientDAO.create(client_data)

    @staticmethod
    def update_client(client_id, update_data):
        return ClientDAO.update(client_id, update_data)

    @staticmethod
    def delete_client(client_id):
        ClientDAO.delete(client_id)

class TerminalService:
    @staticmethod
    def get_all_terminals():
        return TerminalDAO.get_all()

    @staticmethod
    def get_terminal_by_id(terminal_id):
        return TerminalDAO.get_by_id(terminal_id)

    @staticmethod
    def create_terminal(terminal_data):
        return TerminalDAO.create(terminal_data)

    @staticmethod
    def update_terminal(terminal_id, update_data):
        return TerminalDAO.update(terminal_id, update_data)

    @staticmethod
    def delete_terminal(terminal_id):
        TerminalDAO.delete(terminal_id)

class ServiceTypeService:
    @staticmethod
    def get_all_service_types():
        return ServiceTypeDAO.get_all()

    @staticmethod
    def get_service_type_by_id(service_type_id):
        return ServiceTypeDAO.get_by_id(service_type_id)

    @staticmethod
    def create_service_type(service_type_data):
        return ServiceTypeDAO.create(service_type_data)

    @staticmethod
    def update_service_type(service_type_id, update_data):
        return ServiceTypeDAO.update(service_type_id, update_data)

    @staticmethod
    def delete_service_type(service_type_id):
        ServiceTypeDAO.delete(service_type_id)

class PaymentMethodService:
    @staticmethod
    def get_all_payment_methods():
        return PaymentMethodDAO.get_all()

    @staticmethod
    def get_payment_method_by_id(payment_method_id):
        return PaymentMethodDAO.get_by_id(payment_method_id)

    @staticmethod
    def create_payment_method(payment_method_data):
        return PaymentMethodDAO.create(payment_method_data)

    @staticmethod
    def update_payment_method(payment_method_id, update_data):
        return PaymentMethodDAO.update(payment_method_id, update_data)

    @staticmethod
    def delete_payment_method(payment_method_id):
        PaymentMethodDAO.delete(payment_method_id)

class PaymentService:
    @staticmethod
    def get_all_payments():
        return PaymentDAO.get_all()

    @staticmethod
    def get_payment_by_id(payment_id):
        return PaymentDAO.get_by_id(payment_id)

    @staticmethod
    def create_payment(payment_data):
        return PaymentDAO.create(payment_data)

    @staticmethod
    def update_payment(payment_id, update_data):
        return PaymentDAO.update(payment_id, update_data)

    @staticmethod
    def delete_payment(payment_id):
        PaymentDAO.delete(payment_id)

class InvoiceService:
    @staticmethod
    def get_all_invoices():
        return InvoiceDAO.get_all()

    @staticmethod
    def get_invoice_by_id(invoice_id):
        return InvoiceDAO.get_by_id(invoice_id)

    @staticmethod
    def create_invoice(invoice_data):
        return InvoiceDAO.create(invoice_data)

    @staticmethod
    def update_invoice(invoice_id, update_data):
        return InvoiceDAO.update(invoice_id, update_data)

    @staticmethod
    def delete_invoice(invoice_id):
        InvoiceDAO.delete(invoice_id)

class ServiceService:
    @staticmethod
    def get_all_services():
        return ServiceDAO.get_all()

    @staticmethod
    def get_service_by_id(service_id):
        return ServiceDAO.get_by_id(service_id)

    @staticmethod
    def create_service(service_data):
        return ServiceDAO.create(service_data)

    @staticmethod
    def update_service(service_id, update_data):
        return ServiceDAO.update(service_id, update_data)

    @staticmethod
    def delete_service(service_id):
        ServiceDAO.delete(service_id)

class MasterService:
    @staticmethod
    def get_all_masters():
        return MasterDAO.get_all()

    @staticmethod
    def get_master_by_id(master_id):
        return MasterDAO.get_by_id(master_id)

    @staticmethod
    def create_master(master_data):
        return MasterDAO.create(master_data)

    @staticmethod
    def update_master(master_id, update_data):
        return MasterDAO.update(master_id, update_data)

    @staticmethod
    def delete_master(master_id):
        MasterDAO.delete(master_id)
