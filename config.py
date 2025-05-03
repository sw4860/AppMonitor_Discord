import json
from tkinter import messagebox
import os

def load_config(path="config.json"):
    config = {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except FileNotFoundError:
        error_message = f"설정 파일 '{path}'을 찾을 수 없습니다."
        print(f"[ERROR] {error_message}")
        messagebox.showerror("설정 오류", error_message)
        raise FileNotFoundError(error_message)
    
    except json.JSONDecodeError:
        error_message = f"설정 파일 '{path}'의 형식이 올바르지 않습니다."
        print(f"[ERROR] {error_message}")
        messagebox.showerror("설정 오류", error_message)
        raise json.JSONDecodeError(error_message)
    
    except Exception as e:
        error_message = f"설정 파일 '{path}'을 불러오는 데 실패했습니다: {e}"
        print(f"[ERROR] {error_message}")
        messagebox.showerror("설정 오류", error_message)
        raise Exception(error_message)
    
    return config

def load_language(lang_code, lang_dir="."):
    lang_file_path = os.path.join(lang_dir, f"lang_{lang_code}.json")
    try:
        with open(lang_file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] 언어 파일 '{lang_file_path}'을 찾을 수 없습니다.")
        messagebox.showerror("언어 파일 오류", f"언어 파일 '{lang_file_path}'을 찾을 수 없습니다.")
        return {}
    
    except json.JSONDecodeError:
        print(f"[ERROR] 언어 파일 '{lang_file_path}'의 형식이 올바르지 않습니다.")
        messagebox.showerror("언어 파일 오류", f"언어 파일 '{lang_file_path}'의 형식이 올바르지 않습니다.")
        return {}
    
    except Exception as e:
        print(f"[ERROR] 언어 파일 '{lang_file_path}'을 불러오는 데 실패했습니다: {e}")
        messagebox.showerror("언어 파일 오류", f"언어 파일 '{lang_file_path}'을 불러오는 데 실패했습니다: {e}")
        return {}