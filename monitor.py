import subprocess
from logger import write_log
from tkinter import messagebox

def is_app_running(adb_path, device_id, package_name):
    try:
        subprocess.run(
            [adb_path, "connect", device_id],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW,
            check=False
        )

        result = subprocess.run(
            [adb_path, "-s", device_id, "shell", "dumpsys", "window"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            creationflags=subprocess.CREATE_NO_WINDOW,
            check=False
        )

        if result.stdout:
            for line in result.stdout.splitlines():
                if "mCurrentFocus" in line or "mFocusedApp" in line:
                    return package_name in line
        return False
    
    except FileNotFoundError:
        error_message = f"ADB 경로 '{adb_path}'를 찾을 수 없습니다."
        print(f"[ERROR] {error_message}")
        write_log(error_message)
        messagebox.showerror("ADB 오류", f"{error_message}\nconfig.txt의 adb_path 설정을 확인해주세요.")
        return False
    
    except Exception as e:
        error_message = f"앱 상태 확인 중 오류: {e}"
        print(f"[ERROR] {error_message}")
        write_log(error_message)
        return False