from commands.help import help_command
from commands.tasks import make_task


def main():
    print("Task manager. help - справка")
    while True:
        try:
            raw = input("Введите команду: ").strip()
            parts = raw.split()
            cmd, args = parts[0], parts[1:]
            match cmd:
                case "help":
                    help_command()
                case "add":
                    pass
                case "remove":
                    pass
                case "edit":
                    pass
                case "tags":
                    pass
                case "exit":
                    break
                case _:
                    print("Неизвестная команда")
        except Exception as e:
            print(f"Ошибочка: {e}")
        except KeyboardInterrupt:
            print("\n Завершение приложения")
            break


if __name__ == "__main__":
    print(make_task(1, "test", "low"))
    main()
print(__name__)
