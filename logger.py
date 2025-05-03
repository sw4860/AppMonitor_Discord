import datetime

def write_log(message, log_file="log.txt"):
    """로그 메시지를 지정된 파일에 기록합니다."""
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log = f"{timestamp} {message}\n"
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log)
    except Exception as e:
        print(f"[ERROR] 로그 파일 '{log_file}'에 쓰기 실패: {e}")