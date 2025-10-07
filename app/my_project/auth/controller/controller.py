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
    Get a list of all companies
    ---
    tags:
      - Companies
    responses:
      200:
        description: A list of companies
    """
    companies = CompanyService.get_all_companies()
    return jsonify([company.to_dict() for company in companies])


@controller.route("/companies/<int:company_id>", methods=["GET"])
def get_company(company_id):
    """
    Get a company by ID
    ---
    tags:
      - Companies
    parameters:
      - name: company_id
        in: path
        type: integer
        required: true
        description: The ID of the company
    responses:
      200:
        description: Information about the company and its clients
      404:
        description: Company not found
    """
    company = CompanyService.get_company_by_id(company_id)
    if company:
        clients = [client.to_dict() for client in company.clients]
        return jsonify({"company": company.to_dict(), "clients": clients}), 200
    return jsonify({"error": "Company not found"}), 404


@controller.route("/companies", methods=["POST"])
def create_company():
    """
    Create a new company
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
        description: Company created successfully
    """
    company_data = request.json
    new_company = CompanyService.create_company(company_data)
    return jsonify(new_company.to_dict()), 201


@controller.route("/companies/<int:company_id>", methods=["PUT"])
def update_company(company_id):
    """
    Update an existing company
    ---
    tags:
      - Companies
    parameters:
      - name: company_id
        in: path
        type: integer
        required: true
        description: The ID of the company
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
        description: Company updated successfully
      404:
        description: Company not found
    """
    update_data = request.json
    updated_company = CompanyService.update_company(company_id, update_data)
    return jsonify(updated_company.to_dict()) if updated_company else ("", 404)


@controller.route("/companies/<int:company_id>", methods=["DELETE"])
def delete_company(company_id):
    """
    Delete a company
    ---
    tags:
      - Companies
    parameters:
      - name: company_id
        in: path
        type: integer
        required: true
        description: The ID of the company
    responses:
      204:
        description: Company deleted successfully
    """
    CompanyService.delete_company(company_id)
    return "", 204


# --- Client routes ---
@controller.route("/clients", methods=["GET"])
def get_all_clients():
    """
    Get a list of all clients
    ---
    tags:
      - Clients
    responses:
      200:
        description: A list of clients
    """
    clients = ClientService.get_all_clients()
    return jsonify([client.to_dict() for client in clients])


@controller.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    """
    Get a client by ID
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        type: integer
        required: true
        description: The ID of the client
    responses:
      200:
        description: Information about the client and their services
      404:
        description: Client not found
    """
    client = ClientService.get_client_by_id(client_id)
    if client:
        services = [service.to_dict() for service in client.services]
        return jsonify({"client": client.to_dict(), "services": services}), 200
    return jsonify({"error": "Client not found"}), 404


@controller.route("/clients", methods=["POST"])
def create_client():
    """
    Create a new client
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
        description: Client created successfully
    """
    client_data = request.json
    new_client = ClientService.create_client(client_data)
    return jsonify(new_client.to_dict()), 201


@controller.route("/clients/<int:client_id>", methods=["PUT"])
def update_client(client_id):
    """
    Update an existing client
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        type: integer
        required: true
        description: The ID of the client
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
        description: Client updated successfully
      404:
        description: Client not found
    """
    update_data = request.json
    updated_client = ClientService.update_client(client_id, update_data)
    return jsonify(updated_client.to_dict()) if updated_client else ("", 404)


@controller.route("/clients/<int:client_id>", methods=["DELETE"])
def delete_client(client_id):
    """
    Delete a client
    ---
    tags:
      - Clients
    parameters:
      - name: client_id
        in: path
        type: integer
        required: true
        description: The ID of the client
    responses:
      204:
        description: Client deleted successfully
    """
    ClientService.delete_client(client_id)
    return "", 204


# Terminal routes
@controller.route("/terminals", methods=["GET"])
def get_all_terminals():
    """
    Get a list of all terminals
    ---
    tags:
      - Terminals
    responses:
      200:
        description: A list of terminals
    """
    terminals = TerminalService.get_all_terminals()
    return jsonify([terminal.to_dict() for terminal in terminals])


@controller.route("/terminals/<int:terminal_id>", methods=["GET"])
def get_terminal(terminal_id):
    """
    Get a terminal by ID
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
        description: Information about the terminal
      404:
        description: Terminal not found
    """
    terminal = TerminalService.get_terminal_by_id(terminal_id)
    return jsonify(terminal.to_dict()) if terminal else ("", 404)


@controller.route("/terminals", methods=["POST"])
def create_terminal():
    """
    Create a new terminal
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
        description: Terminal created successfully
    """
    terminal_data = request.json
    new_terminal = TerminalService.create_terminal(terminal_data)
    return jsonify(new_terminal.to_dict()), 201


@controller.route("/terminals/<int:terminal_id>", methods=["PUT"])
def update_terminal(terminal_id):
    """
    Update a terminal
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
        description: Terminal updated successfully
      404:
        description: Terminal not found
    """
    update_data = request.json
    updated_terminal = TerminalService.update_terminal(terminal_id, update_data)
    return jsonify(updated_terminal.to_dict()) if updated_terminal else ("", 404)


@controller.route("/terminals/<int:terminal_id>", methods=["DELETE"])
def delete_terminal(terminal_id):
    """
    Delete a terminal
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
        description: Terminal deleted successfully
    """
    TerminalService.delete_terminal(terminal_id)
    return "", 204


# ServiceType routes
@controller.route("/service_types", methods=["GET"])
def get_all_service_types():
    """
    Get all service types
    ---
    tags:
      - Service Types
    responses:
      200:
        description: A list of service types
    """
    service_types = ServiceTypeService.get_all_service_types()
    return jsonify([service_type.to_dict() for service_type in service_types])


@controller.route("/service_types/<int:service_type_id>", methods=["GET"])
def get_service_type(service_type_id):
    """
    Get a service type by ID
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
        description: Information about the service type
      404:
        description: Service type not found
    """
    service_type = ServiceTypeService.get_service_type_by_id(service_type_id)
    return jsonify(service_type.to_dict()) if service_type else ("", 404)


@controller.route("/service_types", methods=["POST"])
def create_service_type():
    """
    Create a new service type
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
        description: Service type created successfully
    """
    service_type_data = request.json
    new_service_type = ServiceTypeService.create_service_type(service_type_data)
    return jsonify(new_service_type.to_dict()), 201


@controller.route("/service_types/<int:service_type_id>", methods=["PUT"])
def update_service_type(service_type_id):
    """
    Update a service type
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
        description: Service type updated successfully
      404:
        description: Service type not found
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
    Delete a service type
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
        description: Service type deleted successfully
    """
    ServiceTypeService.delete_service_type(service_type_id)
    return "", 204


# PaymentMethod routes
@controller.route("/payment_methods", methods=["GET"])
def get_all_payment_methods():
    """
    Get all payment methods
    ---
    tags:
      - Payment Methods
    responses:
      200:
        description: A list of payment methods
    """
    payment_methods = PaymentMethodService.get_all_payment_methods()
    return jsonify([payment_method.to_dict() for payment_method in payment_methods])


@controller.route("/payment_methods/<int:payment_method_id>", methods=["GET"])
def get_payment_method(payment_method_id):
    """
    Get a payment method by ID
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
        description: Information about the payment method
      404:
        description: Payment method not found
    """
    payment_method = PaymentMethodService.get_payment_method_by_id(payment_method_id)
    return jsonify(payment_method.to_dict()) if payment_method else ("", 404)


# --- Client-Service relationship routes ---
@controller.route("/clients/<int:client_id>/services", methods=["GET"])
def get_services_for_client(client_id):
    """
    Get services for a specific client
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
        description: Services provided to the client
      404:
        description: Client not found
    """
    client = ClientService.get_client_by_id(client_id)
    if client:
        services = [service.to_dict() for service in client.services]
        return jsonify({"client": client.to_dict(), "services": services}), 200
    return jsonify({"error": "Client not found"}), 404


@controller.route("/clients/<int:client_id>/services", methods=["POST"])
def add_service_to_client(client_id):
    """
    Add a service to a client
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
        description: Service added successfully
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
    Remove a service from a client
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
        description: Service removed successfully
    """
    ClientService.remove_service_from_client(client_id, service_id)
    return "", 204

@controller.route("/api/client_services", methods=["GET"])
def get_client_services():
    client_services = ClientService.get_all_client_services()
    if client_services is None:
        return jsonify({"error": "Unable to fetch client services"}), 500
    return jsonify([service.to_dict() for service in client_services])
