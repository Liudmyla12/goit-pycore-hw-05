"""
Головний файл бота з циклом обробки команд.
"""
from typing import Dict, Tuple
from contact_manager import add_contact, change_contact, show_phone, show_all


def parse_command(user_input: str) -> Tuple[str, Tuple[str, ...]]:
    parts = user_input.strip().split()
    if not parts:
        return "", tuple()
    cmd, *args = parts
    return cmd.lower(), tuple(args)


def main() -> None:
    contacts: Dict[str, str] = {}
    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "exit": None, "close": None, "quit": None,
    }

    while True:
        user_input = input("Enter a command: ").strip()
        cmd, args = parse_command(user_input)

        if cmd in ("exit", "close", "quit"):
            print("Good bye!")
            break

        handler = commands.get(cmd)
        if handler is None:
            if cmd == "":
                print("Enter the argument for the command")
            else:
                print("Unknown command. Available: add, change, phone, all, exit")
            continue

        print(handler(args, contacts))


if __name__ == "__main__":
    main()
