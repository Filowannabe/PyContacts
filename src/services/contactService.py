from models.contact.contact import Contact
from config.db import db


def get_contacts():
    contact_list = Contact.query.all()
    return contact_list


def get_contact(id):
    task = Contact.query.get(id)
    return task


def create_contacts(fullname, email, phone):
    contact = Contact(fullname, email, phone)
    db.session.add(contact)
    db.session.commit()
    return contact


def update_contact(id,fullname, email, phone):
    contact = Contact.query.get(id)
    contact.fullname = fullname
    contact.email = email
    contact.phone = phone
    db.session.commit()
    return contact


def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return contact
