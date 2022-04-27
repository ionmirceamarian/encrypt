from flask import Blueprint, request
from app.auth_tools import protected_endpoint
from .license_facade import LicenseFacade

license_controller = Blueprint("licenses", __name__, url_prefix="/")


@license_controller.route("/add_license", methods=["POST"])
@protected_endpoint()
def add_license():
    if request.method == 'POST':
        new_license = request.get_json()
        certificate = new_license.get('certificate')
        pods = new_license.get('pods')
        return LicenseFacade().add_license(certificate, pods)

@license_controller.route("/generate_license", methods=["POST"])
@protected_endpoint()
def generate_license():
    if request.method == 'POST':
        new_license = request.get_json()
        pods = new_license.get('pods')
        sku = new_license.get('sku')
        tenant = new_license.get('tenant')
        name_space = new_license.get('name_space')
        cluster = new_license.get('cluster')
        client_name = new_license.get('client_name')
        exp_date = new_license.get('exp_date')
        online = new_license.get('online')
        return LicenseFacade().generate_license(sku, pods, tenant, name_space, cluster, client_name, exp_date,online)


@license_controller.route("/register_license", methods=["POST"])
def register_license():
    if request.method == 'POST':
        license = request.get_json()
        certificate = license.get('certificate')
        cluster_id = license.get('cluster_id')
        return LicenseFacade().register_license(certificate, cluster_id)


@license_controller.route("/check_license", methods=["GET"])
def check_license():
    if request.method == 'GET':
        certificate = request.args.get('certificate')
        cluster_id = request.args.get('cluster_id')
        return LicenseFacade().check_license(certificate, cluster_id)

@license_controller.route("/decrypt_license", methods=["GET"])
@protected_endpoint()
def decrypt_license():
    if request.method == 'GET':
        req = request.get_json()
        encrypted = req.get('encrypted')
        return LicenseFacade().decrypt_license(encrypted)
