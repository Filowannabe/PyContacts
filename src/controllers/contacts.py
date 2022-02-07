from flask import Blueprint, request, jsonify
from models.contact.contacSchema import ContactSchema
from services import contactService

contacts = Blueprint('contacts', __name__)


contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)


@contacts.route('/contacts', methods=['GET'])
def get_contacts():
    contact_list = contactService.get_contacts()
    result = contacts_schema.dump(contact_list)
    return jsonify(result)


@contacts.route('/contacts/<id>', methods=['GET'])
def get_contact(id):
    contact = contactService.get_contact(id)
    return contact_schema.jsonify(contact)


@contacts.route('/contacts', methods=['POST'])
def create_contacts():
    contact = contactService.create_contacts(
        request.json['fullname'], request.json['email'], request.json['phone'])
    return contact_schema.jsonify(contact)


@contacts.route('/contacts/<id>', methods=['PUT'])
def update_contact(id):
    contact = contactService.update_contact(id, request.json['fullname'],
                                            request.json['email'], request.json['phone'])
    contact.fullname = request.json['fullname']
    contact.email = request.json['email']
    contact.phone = request.json['phone']
    return contact_schema.jsonify(contact)


@contacts.route('/contacts/<id>', methods=['DELETE'])
def delete_contact(id):
    contact = contactService.delete_contact(id)
    return contact_schema.jsonify(contact)
