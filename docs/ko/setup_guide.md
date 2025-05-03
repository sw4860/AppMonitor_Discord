# 설정 가이드 (한국어)

`AppMonitor_Discord`는 Android 에뮬레이터 (BlueStacks, Nox Player, LDPlayer 등)에서만 사용 가능하며, ADB를 통해 에뮬레이터와 통신합니다.

## 설정 가이드

`AppMonitor_Discord`를 사용하기 위해서는 몇 가지 설정을 진행해야 합니다. 아래 단계를 따라 진행해 주세요.

### 1. Android 에뮬레이터 설정

각 에뮬레이터에서 ADB 연결을 활성화해야 합니다. 에뮬레이터 종류에 따라 설정 방법이 다를 수 있지만, 일반적으로 아래와 같은 단계를 따릅니다.

#### BlueStacks 5

1.  BlueStacks 5를 실행합니다.
2.  BlueStacks 설정 메뉴로 이동합니다. (톱니바퀴 아이콘 등)
3. "고급 기능 설정" 메뉴에서 "[127.0.0.1:포트 번호]에서 Android에 연결" 옵션을 찾아서 켭니다.
4.  BlueStacks 설정에서 ADB 연결에 필요한 포트 번호를 확인합니다. (일반적으로 5555)

#### Nox Player

사용해보지않아 자세히 모릅니다. 죄송합니다.
1.  Nox Player를 실행합니다.
2.  Nox Player 시스템 설정으로 이동합니다. (톱니바퀴 아이콘 등)
3.  "고급 설정" 또는 "성능 설정" 메뉴에서 "ADB 디버깅 활성화" 옵션을 찾아서 켭니다.
4.  Nox Player 설정에서 ADB 연결에 필요한 포트 번호를 확인합니다. (일반적으로 62001)

#### LDPlayer

사용해보지않아 자세히 모릅니다. 죄송합니다.
1.  LDPlayer를 실행합니다.
2.  LDPlayer 시스템 설정으로 이동합니다. (톱니바퀴 아이콘 등)
3.  "기타 설정" 메뉴에서 "ADB 디버깅 활성화" 옵션을 찾아서 켭니다.
4.  LDPlayer 설정에서 ADB 연결에 필요한 포트 번호를 확인합니다. (일반적으로 5555)

### 2. ADB 연결 확인

1.  `AppMonitor` 폴더를 엽니다.
2.  명령 프롬프트 또는 터미널을 엽니다. (Windows의 경우, `Shift` 키를 누른 상태에서 폴더 내에서 마우스 오른쪽 버튼을 클릭하고 "여기에 PowerShell 창 열기" 또는 "여기서 명령 창 열기"를 선택합니다. 또는 주소창에 "PowerShell"을 입력하여 진입합니다.)
3.  다음 명령어를 입력하고 `Enter` 키를 누릅니다. (각 에뮬레이터의 포트 번호로 대체해야 합니다.)

    * BlueStacks 5: `adb connect localhost:5555`
    * Nox Player: `adb connect localhost:62001`
    * LDPlayer: `adb connect localhost:5555`

    * localhost 부분은 127.0.0.1로 대체되어 있을 수 있습니다.

4.  "connected to localhost:포트번호" 메시지가 표시되면 ADB 연결이 성공적으로 이루어진 것입니다. 연결에 실패하면 에뮬레이터 설정에서 ADB 디버깅이 활성화되어 있는지, 포트 번호가 올바른지 확인해 주세요.

5.  다음 명령어를 입력하고 `Enter` 키를 눌러 연결된 기기를 확인합니다.

    ```
    adb devices
    ```

6.  연결된 기기의 목록이 표시되면 ADB 연결이 성공적으로 이루어진 것입니다.

### 3. AppMonitor 설정

이제 `AppMonitor_Discord`를 사용할 기본 준비가 되었습니다!