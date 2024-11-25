from app import db
from app.my_project.auth.dao.dao import (
    CompanyDAO, ClientDAO, TerminalDAO, ServiceTypeDAO,
    PaymentMethodDAO, PaymentDAO, InvoiceDAO, MasterDAO,
    ClientServiceDAO, ServiceFeedbackDAO
)
from sqlalchemy import text


# --- Company Service ---
class CompanyService:
    @staticmethod
    def get_all():
        return CompanyDAO.get_all()

    @staticmethod
    def get_by_id(company_id):
        return CompanyDAO.get_by_id(company_id)

    @staticmethod
    def create(company_data):
        return CompanyDAO.create(company_data)

    @staticmethod
    def update(company_id, update_data):
        return CompanyDAO.update(company_id, update_data)

    @staticmethod
    def delete(company_id):
        CompanyDAO.delete(company_id)


# --- Client Service ---
class ClientService:
    @staticmethod
    def get_all():
        return ClientDAO.get_all()

    @staticmethod
    def get_by_id(client_id):
        return ClientDAO.get_by_id(client_id)

    @staticmethod
    def create(client_data):
        return ClientDAO.create(client_data)

    @staticmethod
    def update(client_id, update_data):
        return ClientDAO.update(client_id, update_data)

    @staticmethod
    def delete(client_id):
        ClientDAO.delete(client_id)


# --- Terminal Service ---
class TerminalService:
    @staticmethod
    def get_all():
        return TerminalDAO.get_all()

    @staticmethod
    def get_by_id(terminal_id):
        return TerminalDAO.get_by_id(terminal_id)

    @staticmethod
    def create(terminal_data):
        return TerminalDAO.create(terminal_data)

    @staticmethod
    def update(terminal_id, update_data):
        return TerminalDAO.update(terminal_id, update_data)

    @staticmethod
    def delete(terminal_id):
        TerminalDAO.delete(terminal_id)


# --- ServiceType Service ---
class ServiceTypeService:
    @staticmethod
    def get_all():
        return ServiceTypeDAO.get_all()

    @staticmethod
    def get_by_id(service_type_id):
        return ServiceTypeDAO.get_by_id(service_type_id)

    @staticmethod
    def create(service_type_data):
        return ServiceTypeDAO.create(service_type_data)

    @staticmethod
    def update(service_type_id, update_data):
        return ServiceTypeDAO.update(service_type_id, update_data)

    @staticmethod
    def delete(service_type_id):
        ServiceTypeDAO.delete(service_type_id)


# --- PaymentMethod Service ---
class PaymentMethodService:
    @staticmethod
    def get_all():
        return PaymentMethodDAO.get_all()

    @staticmethod
    def get_by_id(payment_method_id):
        return PaymentMethodDAO.get_by_id(payment_method_id)

    @staticmethod
    def create(payment_method_data):
        return PaymentMethodDAO.create(payment_method_data)

    @staticmethod
    def update(payment_method_id, update_data):
        return PaymentMethodDAO.update(payment_method_id, update_data)

    @staticmethod
    def delete(payment_method_id):
        PaymentMethodDAO.delete(payment_method_id)


# --- Payment Service ---
class PaymentService:
    @staticmethod
    def get_all():
        return PaymentDAO.get_all()

    @staticmethod
    def get_by_id(payment_id):
        return PaymentDAO.get_by_id(payment_id)

    @staticmethod
    def create(payment_data):
        return PaymentDAO.create(payment_data)

    @staticmethod
    def update(payment_id, update_data):
        return PaymentDAO.update(payment_id, update_data)

    @staticmethod
    def delete(payment_id):
        PaymentDAO.delete(payment_id)


# --- Invoice Service ---
class InvoiceService:
    @staticmethod
    def get_all():
        return InvoiceDAO.get_all()

    @staticmethod
    def get_by_id(invoice_id):
        return InvoiceDAO.get_by_id(invoice_id)

    @staticmethod
    def create(invoice_data):
        return InvoiceDAO.create(invoice_data)

    @staticmethod
    def update(invoice_id, update_data):
        return InvoiceDAO.update(invoice_id, update_data)

    @staticmethod
    def delete(invoice_id):
        InvoiceDAO.delete(invoice_id)


# --- Master Service ---
class MasterService:
    @staticmethod
    def get_all():
        return MasterDAO.get_all()

    @staticmethod
    def get_by_id(master_id):
        return MasterDAO.get_by_id(master_id)

    @staticmethod
    def create(master_data):
        return MasterDAO.create(master_data)

    @staticmethod
    def update(master_id, update_data):
        return MasterDAO.update(master_id, update_data)

    @staticmethod
    def delete(master_id):
        MasterDAO.delete(master_id)


# --- Feedback Service ---
class FeedbackService:
    @staticmethod
    def add_feedback(service_id, client_id, feedback_text, rating):
        try:
            ServiceFeedbackDAO.add_feedback(service_id, client_id, feedback_text, rating)
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def bulk_insert_feedback():
        try:
            db.session.execute(text('CALL bulk_insert_service_feedback()'))
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_feedback_aggregate(operation):
        try:
            result = db.session.execute(
                text('CALL get_feedback_aggregate(:operation)'), {'operation': operation}
            ).fetchone()
            return result[0] if result else None
        except Exception as e:
            raise e


# --- ClientService Service (M:M relation between Client and Service) ---
class ClientServiceService:
    @staticmethod
    def add_client_service(client_id, service_id):
        try:
            ClientServiceDAO.add_client_service(client_id, service_id)
        except Exception as e:
            db.session.rollback()
            raise e


class DynamicTableService:
    @staticmethod
    def create_tables_with_random_columns():
        try:
            # Виклик процедури dynamic_table_creation_with_random_columns
            db.session.execute(text("CALL dynamic_table_creation_with_random_columns()"))
            db.session.commit()
            return {"message": "Tables with random columns created successfully."}
        except Exception as e:
            # Обробка помилок
            db.session.rollback()
            raise e