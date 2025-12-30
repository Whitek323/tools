#!/usr/bin/env python3
"""
url_to_qr.py
แปลง URL เป็น QR code (บันทึกเป็นไฟล์ PNG)
ใช้งาน:
    python url_to_qr.py "https://example.com" output.png
หรือแบบโต้ตอบ:
    python url_to_qr.py
"""

import sys
import qrcode
from qrcode.constants import ERROR_CORRECT_M

def make_qr(url: str, output: str = "qrcode.png",
            box_size: int = 10, border: int = 1,
            error_correction=ERROR_CORRECT_M):
    """
    สร้าง QR code จาก url และบันทึกเป็นไฟล์ output (PNG)
    - box_size: ขนาดของแต่ละ "จัตุรัส" ในพิกเซล
    - border: ขอบรอบๆ QR (หน่วยเป็น box)
    - error_correction: ระดับการแก้ไขข้อผิดพลาด (L, M, Q, H)
    """
    qr = qrcode.QRCode(
        version=None,  # auto-size
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output)
    print(f"Saved QR code to: {output}")

def main():
    if len(sys.argv) >= 2:
        url = sys.argv[1]
        output = sys.argv[2] if len(sys.argv) >= 3 else "qrcode.png"
    else:
        url = input("Enter the URL to convert to QR code: ").strip()
        output = input("Output filename (default qrcode.png): ").strip() or "qrcode.png"

    if not url:
        print("No URL provided. Exiting.")
        return

    try:
        make_qr(url, output)
    except Exception as e:
        print("Error creating QR code:", e)

if __name__ == "__main__":
    main()
