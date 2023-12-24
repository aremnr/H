import os

def file_send(path: str, format: str) -> None:
    print(path, format)
    serv_var = os.path.dirname(__file__)
    serv_var = serv_var[:serv_var.rfind("/")]
    os.system(f"python {serv_var}/bg/bg_main.py -p \"{path}\" -f \"{format}\"")
