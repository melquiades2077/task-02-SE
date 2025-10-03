import os
import webbrowser

def pascalNotFoundEmergency() -> None:
    print("Что-то пошло не так и я не нашёл PascalABC.NET на компьютере...");
    webbrowser.open_new("https://pascalabc.net")

def hailMihalkovich() -> None:
    try:
        content = os.listdir(r"C:\Program Files (x86)")
        if content.__contains__("PascalABC.NET"):
            print("Крутой программист")
            webbrowser.open_new("https://youtu.be/-KTWKUctFq4?si=t8JhbyOA-g_OFc3W")
        else:
            pascalNotFoundEmergency()
    except FileNotFoundError:
        pascalNotFoundEmergency()

    return
if __name__ == '__main__':
    hailMihalkovich()