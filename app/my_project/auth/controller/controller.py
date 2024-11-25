from flask import Blueprint, jsonify, request
from app.my_project.auth.service.service import (
    FeedbackService, ClientService, TerminalService, ServiceTypeService,
    CompanyService, PaymentMethodService, PaymentService, InvoiceService,
    MasterService, ClientServiceService
)

from sqlalchemy.exc import SQLAlchemyError
from app.my_project.auth.service.service import DynamicTableService

from app import db
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

controller = Blueprint('controller', __name__)

controller = Blueprint('controller', __name__)

# --- Company routes ---
@controller.route('/companies', methods=['GET'])
def get_all_companies():
    try:
        companies = CompanyService.get_all()
        return jsonify([company.to_dict() for company in companies])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/companies/<int:company_id>', methods=['GET'])
def get_company(company_id):
    try:
        company = CompanyService.get_by_id(company_id)
        return jsonify(company.to_dict()) if company else ('', 404)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/companies', methods=['POST'])
def create_company():
    try:
        company_data = request.json
        new_company = CompanyService.create(company_data)
        return jsonify(new_company.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/companies/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    try:
        update_data = request.json
        updated_company = CompanyService.update(company_id, update_data)
        return jsonify(updated_company.to_dict()) if updated_company else ('', 404)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/companies/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    try:
        CompanyService.delete(company_id)
        return '', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Client routes ---
@controller.route('/clients', methods=['GET'])
def get_all_clients():
    try:
        clients = ClientService.get_all()
        return jsonify([client.to_dict() for client in clients])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    try:
        client = ClientService.get_by_id(client_id)
        return jsonify(client.to_dict()) if client else ('', 404)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/clients', methods=['POST'])
def create_client():
    try:
        client_data = request.json
        new_client = ClientService.create(client_data)
        return jsonify(new_client.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    try:
        update_data = request.json
        updated_client = ClientService.update(client_id, update_data)
        return jsonify(updated_client.to_dict()) if updated_client else ('', 404)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    try:
        ClientService.delete(client_id)
        return '', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Terminal routes ---
@controller.route('/terminals', methods=['GET'])
def get_all_terminals():
    try:
        terminals = TerminalService.get_all()
        return jsonify([terminal.to_dict() for terminal in terminals])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/terminals/<int:terminal_id>', methods=['GET'])
def get_terminal(terminal_id):
    try:
        terminal = TerminalService.get_by_id(terminal_id)
        return jsonify(terminal.to_dict()) if terminal else ('', 404)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/terminals', methods=['POST'])
def create_terminal():
    try:
        terminal_data = request.json
        new_terminal = TerminalService.create(terminal_data)
        return jsonify(new_terminal.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/terminals/<int:terminal_id>', methods=['PUT'])
def update_terminal(terminal_id):
    try:
        update_data = request.json
        updated_terminal = TerminalService.update(terminal_id, update_data)
        return jsonify(updated_terminal.to_dict()) if updated_terminal else ('', 404)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/terminals/<int:terminal_id>', methods=['DELETE'])
def delete_terminal(terminal_id):
    try:
        TerminalService.delete(terminal_id)
        return '', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- ServiceType routes ---
@controller.route('/service_types', methods=['GET'])
def get_all_service_types():
    try:
        service_types = ServiceTypeService.get_all()
        return jsonify([service_type.to_dict() for service_type in service_types])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/service_types/<int:service_type_id>', methods=['GET'])
def get_service_type(service_type_id):
    try:
        service_type = ServiceTypeService.get_by_id(service_type_id)
        return jsonify(service_type.to_dict()) if service_type else ('', 404)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/service_types', methods=['POST'])
def create_service_type():
    try:
        service_type_data = request.json
        new_service_type = ServiceTypeService.create(service_type_data)
        return jsonify(new_service_type.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/service_types/<int:service_type_id>', methods=['PUT'])
def update_service_type(service_type_id):
    try:
        update_data = request.json
        updated_service_type = ServiceTypeService.update(service_type_id, update_data)
        return jsonify(updated_service_type.to_dict()) if updated_service_type else ('', 404)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/service_types/<int:service_type_id>', methods=['DELETE'])
def delete_service_type(service_type_id):
    try:
        ServiceTypeService.delete(service_type_id)
        return '', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Service Feedback routes ---
@controller.route('/feedback', methods=['POST'])
def add_feedback():
    data = request.json
    try:
        FeedbackService.add_feedback(data['service_id'], data['client_id'], data['feedback_text'], data['rating'])
        return jsonify({"message": "Feedback added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/feedback/bulk', methods=['POST'])
def bulk_insert_feedback():
    try:
        FeedbackService.bulk_insert_feedback()
        return jsonify({"message": "Bulk feedback added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@controller.route('/feedback/aggregate', methods=['GET'])
def get_feedback_aggregate():
    operation = request.args.get('operation', '').strip()  # Видаляємо зайві пробіли та символи нового рядка
    try:
        # Виклик процедури з очищеним параметром
        db.session.execute(text("CALL get_feedback_aggregate(:operation, @result)"), {"operation": operation})

        # Отримання результату з вихідного параметра
        result = db.session.execute(text("SELECT @result")).scalar()

        return jsonify({"operation": operation, "result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@controller.route('/client_service', methods=['POST'])
def add_client_service():
    data = request.json
    try:
        ClientServiceService.add_client_service(data['client_id'], data['service_id'])
        return jsonify({"message": "Client-Service relation added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@controller.route('/create-random-tables', methods=['POST'])
def create_random_tables():
    try:
        # Виклик сервісу для створення таблиць
        result = DynamicTableService.create_tables_with_random_columns()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



# Маршрут для додавання клієнта (активує тригер check_phone_format)
@controller.route('/clients', methods=['POST'])
def add_client():
    data = request.json
    try:
        db.session.execute(
            """
            INSERT INTO client (name, phone)
            VALUES (:name, :phone)
            """,
            {"name": data["name"], "phone": data["phone"]}
        )
        db.session.commit()
        return jsonify({"message": "Client added successfully"}), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@controller.route('/services', methods=['POST'])
def add_service():
    data = request.json
    try:
        # Виконуємо SQL-запит, використовуючи text()
        query = text("""
            INSERT INTO service (terminal_id, date, cost, invoice_client_id, invoice_payment_id, invoice_id, service_type_id)
            VALUES (:terminal_id, :date, :cost, :invoice_client_id, :invoice_payment_id, :invoice_id, :service_type_id)
        """)
        db.session.execute(query, {
            "terminal_id": data["terminal_id"],
            "date": data["date"],
            "cost": data["cost"],
            "invoice_client_id": data["invoice_client_id"],
            "invoice_payment_id": data["invoice_payment_id"],
            "invoice_id": data["invoice_id"],
            "service_type_id": data["service_type_id"],
        })
        db.session.commit()
        return jsonify({"message": "Service added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        # Обробка помилки тригера
        if '45000' in str(e):
            return jsonify({"error": "Modification of service table is not allowed"}), 400
        return jsonify({"error": f"Database error: {str(e)}"}), 500


@controller.route('/invoices/<int:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    try:
        # Спроба видалити запис з таблиці `invoice`
        db.session.execute(text("""
        DELETE FROM invoice WHERE id = :invoice_id;
        """), {"invoice_id": invoice_id})
        db.session.commit()
        return jsonify({"message": "Invoice deleted successfully"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        # Перевірка на помилку тригера
        if '45000' in str(e):
            return jsonify({"error": "Deletion from invoice table is not allowed"}), 400
        return jsonify({"error": f"Database error: {str(e)}"}), 500

