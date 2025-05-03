import customtkinter as ctk
import os
import datetime
import subprocess
from tkinter import messagebox
from logger import write_log
from config import load_config, load_language

class AppMonitorGUI(ctk.CTk):
    def __init__(self, monitor_callback, send_discord_callback):
        super().__init__()

        # 기본 설정
        self.title("AppMonitor")
        self.geometry("500x500")

        # 설정 및 언어 불러오기
        self.config_data = load_config()
        self.available_languages = self.config_data.get("available_languages", ["ko", "en"])
        self.current_language = self.config_data.get("default_language", "ko")
        self.lang_data = load_language(self.current_language)

        # 모니터링 관련 변수
        self.adb_path = os.path.join(os.getcwd(), "adb.exe")
        self.device_id = self.config_data["device"]
        self.package_name = self.config_data["package"]
        self.interval = int(self.config_data.get("interval", 300))
        self.previous_state = None
        self.monitoring = False
        self.monitor_callback = monitor_callback
        self.send_discord_callback = send_discord_callback

        # 언어 설정 관련 변수
        self.language_variable = ctk.StringVar(self)
        self.language_variable.set(self.lang_data.get(self.current_language, "ko"))
        self.language_variable.trace_add("write", self.change_language)

        # 위젯 생성 및 초기 적용
        self.create_widgets()
        self.apply_theme(ctk.get_appearance_mode())
        self.apply_language()

        # 레이아웃 확장 설정
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

    def create_widgets(self):
        # 상태 라벨
        self.status_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=18, weight="bold"))
        self.status_label.grid(row=0, column=0, pady=(15, 10), padx=15, sticky="ew")

        # 옵션 프레임 (언어, 테마 변경)
        self.option_frame = ctk.CTkFrame(self)
        self.option_frame.grid(row=1, column=0, padx=15, pady=(0, 10), sticky="ew")
        self.option_frame.grid_columnconfigure(0, weight=0)
        self.option_frame.grid_columnconfigure(1, weight=0)
        self.option_frame.grid_columnconfigure(2, weight=1)

        # 언어 선택 라벨
        self.language_label = ctk.CTkLabel(self.option_frame, text="")
        self.language_label.grid(row=0, column=0, padx=(10, 0), pady=5, sticky="w")

        # 언어 선택 드롭다운
        self.language_menu = ctk.CTkOptionMenu(self.option_frame, values=[],
                                               variable=self.language_variable, command=self.change_language_callback)
        self.language_menu.grid(row=0, column=1, padx=(5, 100), pady=5, sticky="ew")

        # 다크/라이트 모드 토글 스위치
        self.theme_switch = ctk.CTkSwitch(self.option_frame, text="", command=self.toggle_theme)
        self.theme_switch.grid(row=0, column=2, padx=(30, 10), pady=5, sticky="e")

        # 시작/중지 버튼 프레임
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=2, column=0, pady=10, padx=15, sticky="ew")
        self.button_frame.grid_columnconfigure(0, weight=1) # 시작 버튼
        self.button_frame.grid_columnconfigure(1, weight=1) # 중지 버튼

        # 모니터링 시작 버튼
        self.start_btn = ctk.CTkButton(self.button_frame, text="", command=self.start_monitoring, width=150)
        self.start_btn.grid(row=0, column=0, padx=(0, 5), sticky="ew")

        # 모니터링 중지 버튼
        self.stop_btn = ctk.CTkButton(self.button_frame, text="", command=self.stop_monitoring, width=150)
        self.stop_btn.grid(row=0, column=1, padx=(5, 0), sticky="ew")

        # 로그 출력 창
        self.log_box = ctk.CTkTextbox(self, font=ctk.CTkFont(size=14))
        self.log_box.grid(row=3, column=0, padx=15, pady=15, sticky="nsew")
        self.log_box.configure(state="disabled")

        # 장치 정보, 패키지, Webhook 등 표시 프레임
        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.grid(row=4, column=0, pady=5, padx=15, sticky="ew")
        self.info_frame.grid_columnconfigure(0, weight=1) # 정보 라벨

        self.info_label = ctk.CTkLabel(self.info_frame, text="", font=ctk.CTkFont(size=14))
        self.info_label.grid(row=0, column=0, sticky="ew")
        self.info_labels = [self.info_label]

        # 로그 파일 열기 버튼
        self.open_log_btn = ctk.CTkButton(self, text="", command=self.open_log, width=150)
        self.open_log_btn.grid(row=5, column=0, pady=10, padx=15, sticky="ew")

    def apply_language(self):
        # 다국어 문자열 반영
        self.title(self.lang_data.get("app_title", ""))
        self.status_label.configure(text=self.lang_data.get("app_status", "").format(status=self.get_status_text()))
        self.start_btn.configure(text=self.lang_data.get("start_monitoring", ""))
        self.stop_btn.configure(text=self.lang_data.get("stop_monitoring", ""))

        # 언어 변경 시 업데이트
        if self.theme_switch.get():
            self.theme_switch.configure(text=self.lang_data.get("light_mode_toggle_on", "Light On"))
        else:
            self.theme_switch.configure(text=self.lang_data.get("light_mode_toggle_off", "Light Off"))

        self.open_log_btn.configure(text=self.lang_data.get("log_open_button", ""))

        device_info = self.lang_data.get("device_info", "").format(device_id=self.device_id)
        package_info = self.lang_data.get("package_info", "").format(package_name=self.package_name)
        webhook_key = "webhook_status_on" if self.config_data.get("webhook_url") else "webhook_status_off"
        webhook_status = self.lang_data.get(webhook_key, "").format(status="✅" if self.config_data.get("webhook_url") else "❌")
        interval_info = self.lang_data.get("interval_info", "").format(interval=self.interval)
        self.info_label.configure(text=f"{device_info}\n{package_info}\n{webhook_status}\n{interval_info}")

        self.language_label.configure(text=self.lang_data.get("language_select", ""))
        self.language_menu.configure(
            values=[load_language(lang).get(lang, lang) for lang in self.available_languages]
        )

    def get_status_text(self):
        if self.previous_state is None:
            return self.lang_data.get("status_unknown", "")
        elif self.previous_state:
            return self.lang_data.get("status_running", "")
        else:
            return self.lang_data.get("status_stopped", "")

    def apply_theme(self, mode):
        text_color = "black" if mode == "Light" else "white"
        btn_fg = "#F0F0F0" if mode == "Light" else "#3B3B3B"
        btn_hover = "#D0D0D0" if mode == "Light" else "#555555"

        self.start_btn.configure(text_color=text_color, fg_color=btn_fg, hover_color=btn_hover)
        self.stop_btn.configure(text_color=text_color, fg_color=btn_fg, hover_color=btn_hover)
        self.open_log_btn.configure(text_color=text_color, fg_color=btn_fg, hover_color=btn_hover)
        self.status_label.configure(text_color=text_color)
        self.info_frame.configure(fg_color=self.cget("bg"))
        for label in self.info_labels:
            label.configure(text_color=text_color)
        self.log_box.configure(text_color=text_color, fg_color=self.cget("bg"), font=ctk.CTkFont(size=14))
        self.theme_switch.configure(text_color=text_color)
        self.button_frame.configure(fg_color=self.cget("bg"))
        self.language_label.configure(text_color=text_color)
        self.language_menu.configure(fg_color=self.cget("bg"), button_color=btn_fg, button_hover_color=btn_hover, text_color=text_color)

    def start_monitoring(self):
        if not self.monitoring:
            self.monitoring = True
            self.previous_state = None
            self.log(self.lang_data.get("monitoring_started", ""))
            self.monitor_callback(self.adb_path, self.device_id, self.package_name, self.interval, self.on_state_change)
            self.start_btn.configure(state="disabled")
            self.stop_btn.configure(state="normal")

    def stop_monitoring(self):
        if self.monitoring:
            self.monitoring = False
            self.log(self.lang_data.get("monitoring_stopped", ""))
            self.update_status(False)
            self.start_btn.configure(state="normal")
            self.stop_btn.configure(state="disabled")

    def on_state_change(self, running):
        if running and self.previous_state != True:
            self.log(self.lang_data.get("app_running_log", ""))
            self.previous_state = True
        elif not running and self.previous_state != False:
            self.log(self.lang_data.get("app_stopped_log", ""))
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = (
                f"{self.lang_data.get('discord_notification_title', '')}\n"
                f"{self.lang_data.get('discord_notification_device', '').format(device_id=self.device_id)}\n"
                f"{self.lang_data.get('discord_notification_package', '').format(package_name=self.package_name)}\n"
                f"{self.lang_data.get('discord_notification_time', '').format(timestamp=timestamp)}"
            )
            self.send_discord_callback(message, self.config_data)
            self.previous_state = False
        elif running and self.previous_state is None:
            self.log(self.lang_data.get("app_running_initial", ""))
            self.previous_state = True
        elif not running and self.previous_state is None:
            self.log(self.lang_data.get("app_stopped_initial", ""))
            self.previous_state = False
        self.update_status(running)

    def update_status(self, running):
        self.status_label.configure(text=self.lang_data.get("app_status", "").format(status=self.get_status_text()))

    def toggle_theme(self):
        mode = "light" if self.theme_switch.get() else "dark"
        ctk.set_appearance_mode(mode)
        if self.theme_switch.get():
            self.theme_switch.configure(text=self.lang_data.get("light_mode_toggle_on", "Light On"))
        else:
            self.theme_switch.configure(text=self.lang_data.get("light_mode_toggle_off", "Light Off"))
        self.apply_theme(mode.capitalize())

    def open_log(self):
        try:
            os.startfile("log.txt")
        except AttributeError:
            subprocess.run(["open", "log.txt"])
        except Exception as e:
            messagebox.showerror(self.lang_data.get("log_open_error_title", ""), self.lang_data.get("log_open_error_message", "").format(error=e))
            write_log(f"로그 파일 열기 오류: {e}")

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_line = f"{timestamp} {message}\n"
        self.log_box.configure(state="normal")
        self.log_box.insert("end", log_line)
        self.log_box.see("end")
        self.log_box.configure(state="disabled")
        write_log(message)

    def change_language_callback(self, selected_lang_display):
        for lang_code in self.available_languages:
            lang_display = load_language(lang_code).get(lang_code, lang_code)
            if lang_display == selected_lang_display:
                if lang_code != self.current_language:
                    self.current_language = lang_code
                    self.lang_data = load_language(self.current_language)
                    self.apply_language()
                return

        if selected_lang_display.lower() in self.available_languages:
            if selected_lang_display.lower() != self.current_language:
                self.current_language = selected_lang_display.lower()
                self.lang_data = load_language(self.current_language)
                self.apply_language()

    def change_language(self, *args):
        pass