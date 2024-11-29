from flask import Blueprint, jsonify, request
from app.my_project.auth.service.service import (
    CompanyService, ClientService, TerminalService, ServiceTypeService,
    PaymentMethodService, PaymentService, InvoiceService, ServiceService, MasterService
)



controller = Blueprint('controller', __name__)

# Company routes
@controller.route('/companies', methods=['GET'])
def get_all_companies():
    companies = CompanyService.get_all_companies()
    return jsonify([company.to_dict() for company in companies])

@controller.route('/companies/<int:company_id>', methods=['GET'])
def get_company(company_id):
    company = CompanyService.get_company_by_id(company_id)
    if company:
        clients = [client.to_dict() for client in company.clients]  # Виведення клієнтів компанії
        return jsonify({"company": company.to_dict(), "clients": clients}), 200
    return jsonify({"error": "Company not found"}), 404

@controller.route('/companies', methods=['POST'])
def create_company():
    company_data = request.json
    new_company = CompanyService.create_company(company_data)
    return jsonify(new_company.to_dict()), 201

@controller.route('/companies/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    update_data = request.json
    updated_company = CompanyService.update_company(company_id, update_data)
    return jsonify(updated_company.to_dict()) if updated_company else ('', 404)

@controller.route('/companies/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    CompanyService.delete_company(company_id)
    return '', 204

# Client routes
@controller.route('/clients', methods=['GET'])
def get_all_clients():
    clients = ClientService.get_all_clients()
    return jsonify([client.to_dict() for client in clients])

@controller.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = ClientService.get_client_by_id(client_id)
    if client:
        services = [service.to_dict() for service in client.services]  # Виведення послуг клієнта
        return jsonify({"client": client.to_dict(), "services": services}), 200
    return jsonify({"error": "Client not found"}), 404

@controller.route('/clients', methods=['POST'])
def create_client():
    client_data = request.json
    new_client = ClientService.create_client(client_data)
    return jsonify(new_client.to_dict()), 201

@controller.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    update_data = request.json
    updated_client = ClientService.update_client(client_id, update_data)
    return jsonify(updated_client.to_dict()) if updated_client else ('', 404)

@controller.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    ClientService.delete_client(client_id)
    return '', 204


# Terminal routes
@controller.route('/terminals', methods=['GET'])
def get_all_terminals():
    terminals = TerminalService.get_all_terminals()
    return jsonify([terminal.to_dict() for terminal in terminals])

@controller.route('/terminals/<int:terminal_id>', methods=['GET'])
def get_terminal(terminal_id):
    terminal = TerminalService.get_terminal_by_id(terminal_id)
    return jsonify(terminal.to_dict()) if terminal else ('', 404)

@controller.route('/terminals', methods=['POST'])
def create_terminal():
    terminal_data = request.json
    new_terminal = TerminalService.create_terminal(terminal_data)
    return jsonify(new_terminal.to_dict()), 201

@controller.route('/terminals/<int:terminal_id>', methods=['PUT'])
def update_terminal(terminal_id):
    update_data = request.json
    updated_terminal = TerminalService.update_terminal(terminal_id, update_data)
    return jsonify(updated_terminal.to_dict()) if updated_terminal else ('', 404)

@controller.route('/terminals/<int:terminal_id>', methods=['DELETE'])
def delete_terminal(terminal_id):
    TerminalService.delete_terminal(terminal_id)
    return '', 204


# ServiceType routes
@controller.route('/service_types', methods=['GET'])
def get_all_service_types():
    service_types = ServiceTypeService.get_all_service_types()
    return jsonify([service_type.to_dict() for service_type in service_types])

@controller.route('/service_types/<int:service_type_id>', methods=['GET'])
def get_service_type(service_type_id):
    service_type = ServiceTypeService.get_service_type_by_id(service_type_id)
    return jsonify(service_type.to_dict()) if service_type else ('', 404)

@controller.route('/service_types', methods=['POST'])
def create_service_type():
    service_type_data = request.json
    new_service_type = ServiceTypeService.create_service_type(service_type_data)
    return jsonify(new_service_type.to_dict()), 201

@controller.route('/service_types/<int:service_type_id>', methods=['PUT'])
def update_service_type(service_type_id):
    update_data = request.json
    updated_service_type = ServiceTypeService.update_service_type(service_type_id, update_data)
    return jsonify(updated_service_type.to_dict()) if updated_service_type else ('', 404)

@controller.route('/service_types/<int:service_type_id>', methods=['DELETE'])
def delete_service_type(service_type_id):
    ServiceTypeService.delete_service_type(service_type_id)
    return '', 204


# PaymentMethod routes
@controller.route('/payment_methods', methods=['GET'])
def get_all_payment_methods():
    payment_methods = PaymentMethodService.get_all_payment_methods()
    return jsonify([payment_method.to_dict() for payment_method in payment_methods])

@controller.route('/payment_methods/<int:payment_method_id>', methods=['GET'])
def get_payment_method(payment_method_id):
    payment_method = PaymentMethodService.get_payment_method_by_id(payment_method_id)
    return jsonify(payment_method.to_dict()) if payment_method else ('', 404)

@controller.route('/payment_methods', methods=['POST'])
def create_payment_method():
    payment_method_data = request.json
    new_payment_method = PaymentMethodService.create_payment_method(payment_method_data)
    return jsonify(new_payment_method.to_dict()), 201

@controller.route('/payment_methods/<int:payment_method_id>', methods=['PUT'])
def update_payment_method(payment_method_id):
    update_data = request.json
    updated_payment_method = PaymentMethodService.update_payment_method(payment_method_id, update_data)
    return jsonify(updated_payment_method.to_dict()) if updated_payment_method else ('', 404)

@controller.route('/payment_methods/<int:payment_method_id>', methods=['DELETE'])
def delete_payment_method(payment_method_id):
    PaymentMethodService.delete_payment_method(payment_method_id)
    return '', 204


# Payment routes
@controller.route('/payments', methods=['GET'])
def get_all_payments():
    payments = PaymentService.get_all_payments()
    return jsonify([payment.to_dict() for payment in payments])

@controller.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = PaymentService.get_payment_by_id(payment_id)
    return jsonify(payment.to_dict()) if payment else ('', 404)

@controller.route('/payments', methods=['POST'])
def create_payment():
    payment_data = request.json
    new_payment = PaymentService.create_payment(payment_data)
    return jsonify(new_payment.to_dict()), 201

@controller.route('/payments/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    update_data = request.json
    updated_payment = PaymentService.update_payment(payment_id, update_data)
    return jsonify(updated_payment.to_dict()) if updated_payment else ('', 404)

@controller.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    PaymentService.delete_payment(payment_id)
    return '', 204


# Invoice routes
@controller.route('/invoices', methods=['GET'])
def get_all_invoices():
    invoices = InvoiceService.get_all_invoices()
    return jsonify([invoice.to_dict() for invoice in invoices])

@controller.route('/invoices/<int:invoice_id>', methods=['GET'])
def get_invoice(invoice_id):
    invoice = InvoiceService.get_invoice_by_id(invoice_id)
    return jsonify(invoice.to_dict()) if invoice else ('', 404)

@controller.route('/invoices', methods=['POST'])
def create_invoice():
    invoice_data = request.json
    new_invoice = InvoiceService.create_invoice(invoice_data)
    return jsonify(new_invoice.to_dict()), 201

@controller.route('/invoices/<int:invoice_id>', methods=['PUT'])
def update_invoice(invoice_id):
    update_data = request.json
    updated_invoice = InvoiceService.update_invoice(invoice_id, update_data)
    return jsonify(updated_invoice.to_dict()) if updated_invoice else ('', 404)

@controller.route('/invoices/<int:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    InvoiceService.delete_invoice(invoice_id)
    return '', 204


# Service routes
@controller.route('/services', methods=['GET'])
def get_all_services():
    services = ServiceService.get_all_services()
    return jsonify([service.to_dict() for service in services])

@controller.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = ServiceService.get_service_by_id(service_id)
    return jsonify(service.to_dict()) if service else ('', 404)

@controller.route('/services', methods=['POST'])
def create_service():
    service_data = request.json
    new_service = ServiceService.create_service(service_data)
    return jsonify(new_service.to_dict()), 201

@controller.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    update_data = request.json
    updated_service = ServiceService.update_service(service_id, update_data)
    return jsonify(updated_service.to_dict()) if updated_service else ('', 404)

@controller.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    ServiceService.delete_service(service_id)
    return '', 204


# Master routes
@controller.route('/masters', methods=['GET'])
def get_all_masters():
    masters = MasterService.get_all_masters()
    return jsonify([master.to_dict() for master in masters])

@controller.route('/masters/<int:master_id>', methods=['GET'])
def get_master(master_id):
    master = MasterService.get_master_by_id(master_id)
    return jsonify(master.to_dict()) if master else ('', 404)

@controller.route('/masters', methods=['POST'])
def create_master():
    master_data = request.json
    new_master = MasterService.create_master(master_data)
    return jsonify(new_master.to_dict()), 201

@controller.route('/masters/<int:master_id>', methods=['PUT'])
def update_master(master_id):
    update_data = request.json
    updated_master = MasterService.update_master(master_id, update_data)
    return jsonify(updated_master.to_dict()) if updated_master else ('', 404)

@controller.route('/masters/<int:master_id>', methods=['DELETE'])
def delete_master(master_id):
    MasterService.delete_master(master_id)
    return '', 204


# Client-Service relationship routes
@controller.route('/clients/<int:client_id>/services', methods=['GET'])
def get_services_for_client(client_id):
    client = ClientService.get_client_by_id(client_id)
    if client:
        services = [service.to_dict() for service in client.services]  # Виведення послуг клієнта
        return jsonify({"client": client.to_dict(), "services": services}), 200
    return jsonify({"error": "Client not found"}), 404

@controller.route('/clients/<int:client_id>/services', methods=['POST'])
def add_service_to_client(client_id):
    service_data = request.json
    service_id = service_data.get("service_id")
    ClientService.add_service_to_client(client_id, service_id)
    return '', 204

@controller.route('/clients/<int:client_id>/services/<int:service_id>', methods=['DELETE'])
def remove_service_from_client(client_id, service_id):
    ClientService.remove_service_from_client(client_id, service_id)
    return '', 204


@controller.route('/api/client_services', methods=['GET'])
def get_client_services():
    # Викликаємо сервіс для отримання всіх записів ClientService
    client_services = ClientService.get_all_client_services()

    if client_services is None:
        return jsonify({"error": "Unable to fetch client services"}), 500

    # Якщо записів немає, повертаємо порожній список
    return jsonify([service.to_dict() for service in client_services])

