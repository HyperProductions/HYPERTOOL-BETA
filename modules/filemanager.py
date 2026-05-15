import os

def run():
    print("\n=== FILE MANAGER ===\n")
    print("[1] Dosya Listele")
    print("[2] Dosya Oku")
    print("[3] Klasör Değiştir (cd)")

    choice = input("\nSeçim: ")

    if choice == "1":
        list_files()
    elif choice == "2":
        read_file()
    elif choice == "3":
        change_dir()
    else:
        print("Geçersiz seçim!")

def list_files():
    path = input("Klasör yolu (boş = mevcut): ")

    if path == "":
        path = os.getcwd()

    print(f"\nİçerik: {path}\n")

    try:
        items = os.listdir(path)

        for item in items:
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                print("[DIR] ", item)
            else:
                print("      ", item)

    except Exception as e:
        print("Hata:", e)

def read_file():
    file_path = input("Dosya yolu: ")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        print("\n=== DOSYA İÇERİĞİ ===\n")
        print(content)

    except Exception as e:
        print("Dosya okunamadı:", e)

def change_dir():
    path = input("Yeni klasör yolu: ")

    try:
        os.chdir(path)
        print("Klasör değiştirildi ✔")
        print("Yeni konum:", os.getcwd())

    except Exception as e:
        print("Hata:", e)