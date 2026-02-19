import os

def get_db_path():
    appdata = os.getenv("AppData") # C:\Users\Asus\AppData\Roaming
    game_folder = os.path.join(appdata, "Triatris") # C:\Users\Asus\AppData\Roaming\Triatris
    os.makedirs(game_folder, exist_ok=True) # Buat folder Triatris kalau blm ada
    return os.path.join(game_folder, "skoren.db") # C:\Users\Asus\AppData\Roaming\Triatris\skoren.db