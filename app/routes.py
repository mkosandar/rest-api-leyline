from flask import Blueprint, jsonify, request
import time
import socket
from .models import Query, db
import os

main = Blueprint('main', __name__)

@main.route('/')
def root():
    return jsonify({
        "version": "0.1.0",
        "date": int(time.time()),
        "kubernetes": os.getenv('KUBERNETES_SERVICE_HOST') is not None
    })

@main.route('/v1/tools/lookup', methods=['GET'])
def lookup():
    domain = request.args.get('domain')
    ip_list = socket.gethostbyname_ex(domain)[2]
    ipv4_list = [ip for ip in ip_list if '.' in ip]

    query = Query(domain=domain, result=str(ipv4_list))
    db.session.add(query)
    db.session.commit()

    return jsonify({"ipv4_addresses": ipv4_list})

@main.route('/v1/tools/validate', methods=['POST'])
def validate():
    data = request.json
    ip = data.get('ip')
    try:
        socket.inet_aton(ip)
        return jsonify({"valid": True})
    except socket.error:
        return jsonify({"valid": False})

@main.route('/v1/history', methods=['GET'])
def history():
    queries = Query.query.order_by(Query.id.desc()).limit(20).all()
    return jsonify([{"domain": q.domain, "result": q.result} for q in queries])

@main.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})
