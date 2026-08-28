# Chuong trinh dem san pham bang tai Smart Factory
import time 

san_pham = 0
ton_kho_toi_da = 10 

print("---HE THONG BAT DAU HOAT DONG---")
while san_pham < ton_kho_toi_da:
      san_pham += 1
      print(f"Cam bien phat hien san pham moi! Tong so SP:{san_pham}/{ton_kho_toi_da}")
      time.sleep(0.5)
print("---BANG TAI DUNG: DA DAT TOI DA DUNG LUONG---")