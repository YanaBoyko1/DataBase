from app.my_project.auth.controller.controller import controller

def register_routes(app):
    app.register_blueprint(controller, url_prefix='/api')
