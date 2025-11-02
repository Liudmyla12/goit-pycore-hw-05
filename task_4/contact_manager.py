"""
Функції-обробники для керування контактами.
"""
from typing import Dict, Tuple
from decorators import input_error

Contacts = Dict[str, str]


@input_error
def add_contact(args: Tuple[str, ...], contacts: Contacts) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: Tuple[str, ...], contacts: Contacts) -> str:
    name, phone = args
    if name not in contacts:
        raise KeyError(name)
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: Tuple[str, ...], contacts: Contacts) -> str:
    (name,) = args
    if name not in contacts:
        raise KeyError(name)
    return f"{name}: {contacts[name]}"


@input_error
def show_all(_: Tuple[str, ...], contacts: Contacts) -> str:
    if not contacts:
        return "No contacts yet."
    return "\n".join(f"{n}: {p}" for n, p in contacts.items())
