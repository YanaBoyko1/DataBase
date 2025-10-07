from flask import Blueprint, jsonify, request
from app.my_project.auth.service.service import (
    CompanyService,
    ClientService,
    TerminalService,
    ServiceTypeService,
    PaymentMethodService,
    PaymentService,
    InvoiceService,
    ServiceService,
    MasterService,
)

controller = Blueprint("controller", __name__)


# --- Company routes ---
@controller.route("/companies", methods=["GET"])
def get_all_companies():
    """
    Отримати список всіх компаній
    ---
    tags:
      - Companies
    responses:
      200:
        description: Список компаній
    """
    companies = CompanyService.get_all_companies()
    return jsonify([company.to_dict() for company in companies])


# @controller.route('/companies/<int:company_id>', methods=['GET'])
# def get_company(company_id):
#     """
#     Отримати компанію за ID
#     ---
#     tags:
#       - Companies
#     parameters:
#       - name: company_id
#         in: path
#         type: integer
#         required: true
#         description: ID компанії
#     responses:
#       200:
#         description: Інформація про компанію та її клієнтів
#       404:
#         description: Компанію не знайдено
#     """
#     company = CompanyService.get_company_by_id(company_id)
#     if company:
#         clients = [client.to_dict() for client in company.clients]
#         return jsonify({"company": company.to_dict(), "clients": clients}), 200
#     return jsonify({"error": "Company not found"}), 404


@controller.route("/companies", methods=["POST"])
def create_company():
    """
    Створити нову компанію
    ---
    tags:
      - Companies
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            address:
              type: string
            phone:
              type: string
    responses:
      201:
        description: Компанію успішно створено
    """
    company_data = request.json
    new_company = CompanyService.create_company(company_data)
    return jsonify(new_company.to_dict()), 201


@controller.route("/companies/<int:company_id>", methods=["PUT"])
def update_company(company_id):
    """
    Оновити існуючу компанію
    ---
    tags:
      - Companies
    parameters:
      - name: company_id
        in: path
        type: integer
        required: true
        description: ID компанії
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            address:
              type: string
            phone:
              type: string
    responses:
      200:
        description: Компанію успішно оновлено
      404:
        description: Компанію не знайдено
    """
    update_data = request.json
    updated_company = CompanyService.update_company(company_id, update_data)
    return jsonify(updated_company.to_dict()) if updated_company else ("", 404)


@controller.route("/companies/<int:company_id>", methods=["DELETE"])
def delete_company(company_id):
    """
    Видалити компанію
    ---
    tags:
      - Companies
    parameters:
      - name: company_id
        in: path
        type: integer
        required: true
        description: ID компанії
    responses:
      204:
        description: Компанію успішно видалено
    """
    CompanyService.delete_company(company_id)
    return "", 204


# --- Client routes ---
@controller.route("/clients", methods=["GET"])
def get_all_clients():
    """
    Отримати список всіх клієнтів
    ---
    tags:
      - Clients
    responses:
      200:
        description: Список клієнтів
    """
    clients = ClientService.get_all_clients()
    return jsonify([client.to_dict() for client in clients])


@controller.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    """
    Отримати клієнта за ID
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        type: integer
        required: true
        description: ID клієнта
    responses:
      200:
        description: Інформація про клієнта та його послуги
      404:
        description: Клієнта не знайдено
    """
    client = ClientService.get_client_by_id(client_id)
    if client:
        services = [service.to_dict() for service in client.services]
        return jsonify({"client": client.to_dict(), "services": services}), 200
    return jsonify({"error": "Client not found"}), 404


@controller.route("/clients", methods=["POST"])
def create_client():
    """
    Створити нового клієнта
    ---
    tags:
      - Clients
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            phone:
              type: string
    responses:
      201:
        description: Клієнта успішно створено
    """
    client_data = request.json
    new_client = ClientService.create_client(client_data)
    return jsonify(new_client.to_dict()), 201


@controller.route("/clients/<int:client_id>", methods=["PUT"])
def update_client(client_id):
    """
    Оновити існуючого клієнта
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        type: integer
        required: true
        description: ID клієнта
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            phone:
              type: string
    responses:
      200:
        description: Клієнта успішно оновлено
      404:
        description: Клієнта не знайдено
    """
    update_data = request.json
    updated_client = ClientService.update_client(client_id, update_data)
    return jsonify(updated_client.to_dict()) if updated_client else ("", 404)


@controller.route("/clients/<int:client_id>", methods=["DELETE"])
def delete_client(client_id):
    """
    Видалити клієнта
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        type: integer
        required: true
        description: ID клієнта
    responses:
      204:
        description: Клієнта успішно видалено
    """
    ClientService.delete_client(client_id)
    return "", 204


# Terminal routes
@controller.route("/terminals", methods=["GET"])
def get_all_terminals():
    """
    Отримати список всіх терміналів
    ---
    tags:
      - Terminals
    responses:
      200:
        description: Список терміналів
    """
    terminals = TerminalService.get_all_terminals()
    return jsonify([terminal.to_dict() for terminal in terminals])


@controller.route("/terminals/<int:terminal_id>", methods=["GET"])
def get_terminal(terminal_id):
    """
    Отримати термінал за ID
    ---
    tags:
      - Terminals
    parameters:
      - name: terminal_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Інформація про термінал
      404:
        description: Термінал не знайдено
    """
    terminal = TerminalService.get_terminal_by_id(terminal_id)
    return jsonify(terminal.to_dict()) if terminal else ("", 404)


@controller.route("/terminals", methods=["POST"])
def create_terminal():
    """
    Створити новий термінал
    ---
    tags:
      - Terminals
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            company_id:
              type: integer
            address:
              type: string
    responses:
      201:
        description: Термінал успішно створено
    """
    terminal_data = request.json
    new_terminal = TerminalService.create_terminal(terminal_data)
    return jsonify(new_terminal.to_dict()), 201


@controller.route("/terminals/<int:terminal_id>", methods=["PUT"])
def update_terminal(terminal_id):
    """
    Оновити термінал
    ---
    tags:
      - Terminals
    parameters:
      - name: terminal_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            address:
              type: string
    responses:
      200:
        description: Термінал успішно оновлено
      404:
        description: Термінал не знайдено
    """
    update_data = request.json
    updated_terminal = TerminalService.update_terminal(terminal_id, update_data)
    return jsonify(updated_terminal.to_dict()) if updated_terminal else ("", 404)


@controller.route("/terminals/<int:terminal_id>", methods=["DELETE"])
def delete_terminal(terminal_id):
    """
    Видалити термінал
    ---
    tags:
      - Terminals
    parameters:
      - name: terminal_id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Термінал успішно видалено
    """
    TerminalService.delete_terminal(terminal_id)
    return "", 204


# ServiceType routes
@controller.route("/service_types", methods=["GET"])
def get_all_service_types():
    """
    Отримати всі типи послуг
    ---
    tags:
      - Service Types
    responses:
      200:
        description: Список типів послуг
    """
    service_types = ServiceTypeService.get_all_service_types()
    return jsonify([service_type.to_dict() for service_type in service_types])


@controller.route("/service_types/<int:service_type_id>", methods=["GET"])
def get_service_type(service_type_id):
    """
    Отримати тип послуги за ID
    ---
    tags:
      - Service Types
    parameters:
      - name: service_type_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Інформація про тип послуги
      404:
        description: Тип послуги не знайдено
    """
    service_type = ServiceTypeService.get_service_type_by_id(service_type_id)
    return jsonify(service_type.to_dict()) if service_type else ("", 404)


@controller.route("/service_types", methods=["POST"])
def create_service_type():
    """
    Створити новий тип послуги
    ---
    tags:
      - Service Types
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      201:
        description: Тип послуги створено
    """
    service_type_data = request.json
    new_service_type = ServiceTypeService.create_service_type(service_type_data)
    return jsonify(new_service_type.to_dict()), 201


@controller.route("/service_types/<int:service_type_id>", methods=["PUT"])
def update_service_type(service_type_id):
    """
    Оновити тип послуги
    ---
    tags:
      - Service Types
    parameters:
      - name: service_type_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      200:
        description: Тип послуги оновлено
      404:
        description: Тип послуги не знайдено
    """
    update_data = request.json
    updated_service_type = ServiceTypeService.update_service_type(
        service_type_id, update_data
    )
    return (
        jsonify(updated_service_type.to_dict()) if updated_service_type else ("", 404)
    )


@controller.route("/service_types/<int:service_type_id>", methods=["DELETE"])
def delete_service_type(service_type_id):
    """
    Видалити тип послуги
    ---
    tags:
      - Service Types
    parameters:
      - name: service_type_id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Тип послуги видалено
    """
    ServiceTypeService.delete_service_type(service_type_id)
    return "", 204


# PaymentMethod routes
@controller.route("/payment_methods", methods=["GET"])
def get_all_payment_methods():
    """
    Отримати всі методи оплати
    ---
    tags:
      - Payment Methods
    responses:
      200:
        description: Список методів оплати
    """
    payment_methods = PaymentMethodService.get_all_payment_methods()
    return jsonify([payment_method.to_dict() for payment_method in payment_methods])


@controller.route("/payment_methods/<int:payment_method_id>", methods=["GET"])
def get_payment_method(payment_method_id):
    """
    Отримати метод оплати за ID
    ---
    tags:
      - Payment Methods
    parameters:
      - name: payment_method_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Інформація про метод оплати
      404:
        description: Метод оплати не знайдено
    """
    payment_method = PaymentMethodService.get_payment_method_by_id(payment_method_id)
    return jsonify(payment_method.to_dict()) if payment_method else ("", 404)


# --- Client-Service relationship routes ---
@controller.route("/clients/<int:client_id>/services", methods=["GET"])
def get_services_for_client(client_id):
    """
    Отримати послуги для конкретного клієнта
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Послуги, що надаються клієнту
      404:
        description: Клієнта не знайдено
    """
    client = ClientService.get_client_by_id(client_id)
    if client:
        services = [service.to_dict() for service in client.services]
        return jsonify({"client": client.to_dict(), "services": services}), 200
    return jsonify({"error": "Client not found"}), 404


@controller.route("/clients/<int:client_id>/services", methods=["POST"])
def add_service_to_client(client_id):
    """
    Додати послугу клієнту
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            service_id:
              type: integer
    responses:
      204:
        description: Послугу успішно додано
    """
    service_data = request.json
    service_id = service_data.get("service_id")
    ClientService.add_service_to_client(client_id, service_id)
    return "", 204


@controller.route(
    "/clients/<int:client_id>/services/<int:service_id>", methods=["DELETE"]
)
def remove_service_from_client(client_id, service_id):
    """
    Видалити послугу у клієнта
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        type: integer
        required: true
      - name: service_id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Послугу успішно видалено
    """
    ClientService.remove_service_from_client(client_id, service_id)
    return "", 204


@controller.route("/api/client_services", methods=["GET"])
def get_client_services():
    client_services = ClientService.get_all_client_services()
    if client_services is None:
        return jsonify({"error": "Unable to fetch client services"}), 500
    return jsonify([service.to_dict() for service in client_services])
