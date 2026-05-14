import os
import tempfile

def run():
    print("\n=== SYSTEM CLEANER ===\n")

    temp_path = tempfile.gettempdir()
    print(f"Temp klasörü: {temp_path}")

    confirm = input("Temp dosyaları silinsin mi? (y/n): ")

    if confirm.lower() != "y":
        print("İptal edildi.")
        return

    deleted = 0
    errors = 0

    for root, dirs, files in os.walk(temp_path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                os.remove(file_path)
                deleted += 1
            except:
                errors += 1

    print("\n=== SONUÇ ===")
    print(f"Silinen dosya: {deleted}")
    print(f"Hata: {errors}")
    print("================\n")