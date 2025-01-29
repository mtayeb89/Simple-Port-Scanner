import socket
import sys
import threading
import time
from datetime import datetime


class PortScanner:
    def __init__(self):
        self.open_ports = []
        self.threads = []
        self.lock = threading.Lock()

    def scan_port(self, host, port):
        """
        فحص منفذ واحد وتسجيل النتيجة إذا كان مفتوحاً
        """
        try:
            # إنشاء socket جديد
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # تعيين مهلة الاتصال

            # محاولة الاتصال بالمنفذ
            result = sock.connect_ex((host, port))

            # إذا كان المنفذ مفتوحاً
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
                    # محاولة الحصول على اسم الخدمة
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "مجهول"
                    print(f"[+] المنفذ {port} مفتوح - الخدمة: {service}")

            sock.close()

        except socket.gaierror:
            print("خطأ: لم يتم العثور على المضيف")
            sys.exit()
        except socket.error:
            print("لم يتم إنشاء socket")
            sys.exit()

    def scan(self, target, start_port, end_port):
        """
        بدء عملية الفحص للنطاق المحدد من المنافذ
        """
        try:
            # تحويل اسم المضيف إلى IP
            target_ip = socket.gethostbyname(target)
            print("-" * 50)
            print(f"فحص المضيف: {target} ({target_ip})")
            print(f"وقت البدء: {str(datetime.now())}")
            print("-" * 50)

            start_time = time.time()

            # إنشاء threads للفحص المتوازي
            for port in range(start_port, end_port + 1):
                thread = threading.Thread(target=self.scan_port, args=(target_ip, port))
                self.threads.append(thread)
                thread.start()

            # انتظار انتهاء جميع threads
            for thread in self.threads:
                thread.join()

            end_time = time.time()

            print("-" * 50)
            print(f"اكتمل الفحص في {round(end_time - start_time, 2)} ثانية")
            print(f"تم العثور على {len(self.open_ports)} منفذ مفتوح")
            print("-" * 50)

            return self.open_ports

        except KeyboardInterrupt:
            print("\nتم إيقاف الفحص بواسطة المستخدم")
            sys.exit()


# مثال على الاستخدام
if __name__ == "__main__":
    scanner = PortScanner()
    target = input("أدخل عنوان IP أو اسم المضيف للفحص: ")
    start_port = int(input("أدخل المنفذ الأول للفحص (مثال: 1): "))
    end_port = int(input("أدخل المنفذ الأخير للفحص (مثال: 100): "))

    open_ports = scanner.scan(target, start_port, end_port)