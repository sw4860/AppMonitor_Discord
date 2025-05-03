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

### 3. AppMonitor 설정 및 설명

이제 `AppMonitor_Discord`를 사용할 기본 준비가 되었습니다!

`config.json` 파일은 `AppMonitor_Discord` 프로그램이 어떤 앱을 모니터링할지, 얼마나 자주 실행을 검사할지, 어디로 알람, 멘션을 보낼지 등을 설정하는 파일입니다.

```json
{
    "device": "",
    "package": "com.gear2.growslayer",
    "interval": 300,
    "webhook_url": "",
    "mention": "",
    "default_language": "ko",
    "available_languages": ["ko", "en"]
}
```

이 코드가 config.json 파일의 기본 값 입니다.
하나씩 자세히 알아보겠습니다.

`"device": ""` 이 부분은 "어떤 기기에서 검사를 할것인지"를 설정하는 곳입니다.
`""`안에는 위에 ADB관련 설정할때 알아낸 포트 값을 넣으면 됩니다.

`"package": "com.gear2.growslayer"` 이 부분은 "어떤 앱을 검사할건지"를 설정하는 곳입니다.
모니터링하고 싶은 앱의 패키지 이름을 정확하게 입력해야 합니다.
현재 기본값은 `슬레이어 키우기`를 검사합니다.

`"interval": 300` 이 부분은 "얼마나 자주 검사를 하는지"를 설정하는 곳입니다.
숫자로 시간을 적으며, 단위는 "초"입니다. 예를 들어, 300이라고 쓰면 300초 (5분)마다 검사합니다.

`"webhook_url": ""` 이 부분은 "알람을 어디로 보낼것인지"를 설정하는 곳입니다.
Discord의 "웹훅"이라는 기능을 사용하는데, 이걸 쓰면 프로그램이 자동으로 Discord 채널에 메시지를 보낼 수 있습니다.
웹훅을 알아내는 방법은 아래와 같습니다.
1. Discord에서 원하는 채널로 이동
2. 채널 설정 > 통합 > Webhook > 새 Webhook 생성
    * 이를 위해선 관리자 권한이 필요합니다.
3. URL 복사 후 webhook_url의 ""안에 붙여넣기

`"mention": ""` 이 부분은 "메시지를 보낼 때 누구를 멘션 할것인지"를 설정하는 곳입니다.
사용자 ID나 역할 ID는 Discord 설정에서 확인할 수 있습니다.
ID를 알아내는 방법은 아래와 같습니다.
1. Discord 설정 > 고급 > 개발자 모드 활성화
2. 멘션할 사용자 또는 역할에서 우클릭 > ID 복사

결과 예시:
    * 사용자: <@123456789012345678>
    * 역할: <@&987654321098765432>
mention 항목에 "123456789012345678" 또는 "@everyone"과 같이 넣을 수 있습니다.

`"default_language": "ko"` 이 부분은 "프로그램의 UI 언어"를 설정하는 곳입니다.
아래의 `"available_languages"`에 있는 값만 인식할 수 있습니다.

`"available_languages": ["ko", "en"]` 이 부분은 "프로그램이 어떤 언어를 지원하는지"를 알려주는 곳입니다.
일반적으로는 건들 필요가 없는 구역입니다.

#### 설정 예시 ####
예를 들어, BlueStacks 5 에뮬레이터에서 "com.example.myapp"이라는 앱을 60초마다 모니터링하고, 특정 Discord 웹훅으로 정보를 보내고, 특정 사용자를 멘션하고, 프로그램 언어를 영어로 설정하고 싶다면, config.json 파일을 다음과 같이 수정하면 돼요.

```JSON
{
    "device": "127.0.0.1:5555",
    "package": "com.example.myapp",
    "interval": 60,
    "webhook_url": "https://discord.com/api/webhooks/123456789012345678/abcdefghijklmnopqrstuvwxyz",
    "mention": "123456789012345678",
    "default_language": "en",
    "available_languages": ["ko", "en"]
}
```

**주의사항**
JSON 문법을 정확하게 지켜야 합니다. 쉼표, 따옴표, 중괄호 등을 빠뜨리거나 잘못 쓰면 프로그램이 제대로 작동하지 않을 수 있어요.
각 설정 항목에 맞는 종류의 값을 넣어줘야 합니다. 예를 들어, 시간 간격(interval)은 숫자로, 웹훅 URL(webhook_url)은 인터넷 주소처럼 써야 합니다.
webhook_url과 mention은 Discord에서 웹훅 설정과 사용자/역할 ID를 얻는 설정을 먼저 완료해야 제대로 사용할 수 있습니다.