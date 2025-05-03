import customtkinter as ctk
import threading
import time
from config import load_config
from logger import write_log
from monitor import is_app_running
from gui import AppMonitorGUI
import requests

def send_discord_message(message, config):
    webhook_url = config.get("webhook_url")
    mention = config.get("mention")

    if not webhook_url:
        print("[WARNING] Discord Webhook URL이 설정되지 않았습니다.")
        write_log("경고: Discord Webhook URL이 설정되지 않았습니다.")
        return

    try:
        content = f"<@{mention}> {message}" if mention else message
        data = {
            "content": content
        }
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("🔔 Discord 알림 전송 성공")
            write_log("🔔 Discord 알림 전송 성공")
        else:
            print(f"❌ Discord 알림 실패: 응답 코드 {response.status_code}, 내용: {response.text}")
            write_log(f"Discord 알림 실패: 응답 코드 {response.status_code}, 내용: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Discord 메시지 전송 중 네트워크 오류: {e}")
        write_log(f"Discord 메시지 전송 중 네트워크 오류: {e}")
    except Exception as e:
        print(f"[ERROR] Discord 메시지 전송 실패: {e}")
        write_log(f"Discord 메시지 전송 실패: {e}")

def monitor_app_state(adb_path, device_id, package_name, interval, state_change_callback):
    previous_state = None
    while True:
        if not gui.monitoring:
            break
        running = is_app_running(adb_path, device_id, package_name)
        if running != previous_state:
            state_change_callback(running)
            previous_state = running
        time.sleep(interval)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    config_data = load_config("config.json")

    def start_monitor_thread(adb_path, device_id, package_name, interval, state_change_callback):
        thread = threading.Thread(target=monitor_app_state, args=(adb_path, device_id, package_name, interval, state_change_callback), daemon=True)
        thread.start()

    app = AppMonitorGUI(start_monitor_thread, send_discord_message)
    gui = app
    app.mainloop()