# Setup Guide (English)

**This document has been translated from the original Korean version using AI.**

`AppMonitor_Discord` is only compatible with Android emulators (BlueStacks, Nox Player, LDPlayer, etc.) and communicates with the emulator via ADB.

## Setup Guide

To use `AppMonitor_Discord`, you need to perform a few setup steps. Please follow the steps below.

### 1. Android Emulator Setup

You need to enable ADB connection in each emulator. The setup method may vary depending on the emulator type, but generally, follow the steps below.

#### BlueStacks 5

1.  Run BlueStacks 5.
2.  Go to the BlueStacks settings menu (gear icon, etc.).
3.  In the "Advanced Feature Settings" menu, find and turn on the "[127.0.0.1:Port Number] Connect to Android" option.
4.  Check the BlueStacks settings for the port number required for ADB connection (usually 5555).

#### Nox Player

I haven't used it, so I don't know the details. Sorry.

1.  Run Nox Player.
2.  Go to the Nox Player system settings (gear icon, etc.).
3.  In the "Advanced Settings" or "Performance Settings" menu, find and turn on the "Enable ADB Debugging" option.
4.  Check the Nox Player settings for the port number required for ADB connection (usually 62001).

#### LDPlayer

I haven't used it, so I don't know the details. Sorry.

1.  Run LDPlayer.
2.  Go to the LDPlayer system settings (gear icon, etc.).
3.  In the "Other Settings" menu, find and turn on the "Enable ADB Debugging" option.
4.  Check the LDPlayer settings for the port number required for ADB connection (usually 5555).

### 2. ADB Connection Verification

1.  Open the `AppMonitor` folder.
2.  Open the command prompt or terminal. (In Windows, hold down the `Shift` key, right-click inside the folder, and select "Open PowerShell window here" or "Open command window here". Alternatively, type "PowerShell" in the address bar to enter.)
3.  Enter the following command and press `Enter`. (Replace with the port number of each emulator.)

    * BlueStacks 5: `adb connect localhost:5555`
    * Nox Player: `adb connect localhost:62001`
    * LDPlayer: `adb connect localhost:5555`

    * The localhost part may be replaced with 127.0.0.1.

4.  If the message "connected to localhost:port number" is displayed, the ADB connection is successful. If the connection fails, check if ADB debugging is enabled in the emulator settings and if the port number is correct.
5.  Enter the following command and press `Enter` to check the connected devices.

    ```
    adb devices
    ```

6.  If the list of connected devices is displayed, the ADB connection is successful.

### 3. AppMonitor Setup and Explanation

You are now basically ready to use `AppMonitor_Discord`!

The `config.json` file is used to configure settings such as which app `AppMonitor_Discord` will monitor, how often it will check, and where to send alarms and mentions.

```JSON
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
This code is the default value of the config.json file.
Let's take a closer look at each part.

`"device": ""` This part is where you set "which device to check".
In the "", you should put the port value obtained during the ADB setup.

`"package": "com.gear2.growslayer"` This part is where you set "which app to check".
You must enter the package name of the app you want to monitor accurately.
The current default value is to check Slayer Legend.

`"interval": 300` This part is where you set "how often to check".
You write the time in numbers, and the unit is "seconds". For example, if you write 300, it checks every 300 seconds (5 minutes).

`"webhook_url": ""` This part is where you set "where to send alarms".
It uses Discord's "Webhook" feature, which allows the program to automatically send messages to a Discord channel.
The method to find the Webhook is as follows:

Go to the desired channel in Discord.
1. Channel Settings > Integrations > Webhooks > Create Webhook
2. Administrator privileges are required for this.
3. Copy the URL and paste it into the "" of webhook_url.

`"mention": ""` This part is where you set "who to mention when sending a message".
User IDs or role IDs can be found in Discord settings.
The method to find the ID is as follows:
1. Discord Settings > Advanced > Enable Developer Mode
2. Right-click on the user or role to mention > Copy ID
Result examples:
User: <@123456789012345678>
Role: <@&987654321098765432>
You can put "123456789012345678" or "@everyone" in the mention item.

`"default_language": "ko"` This part is where you set the "UI language of the program".
Only the values in the "available_languages" below can be recognized.

`"available_languages": ["ko", "en"]` This part indicates "which languages the program supports".
Generally, there is no need to touch this area.

#### Configuration Example ####
For example, if you want to monitor the app "com.example.myapp" on the BlueStacks 5 emulator every 60 seconds, send information to a specific Discord webhook, mention a specific user, and set the program language to English, you can modify the config.json file as follows:

```JSON
{
    "device": "127.0.0.1:5555",
    "package": "com.example.myapp",
    "interval": 60,
    "webhook_url": "[https://discord.com/api/webhooks/123456789012345678/abcdefghijklmnopqrstuvwxyz](https://discord.com/api/webhooks/123456789012345678/abcdefghijklmnopqrstuvwxyz)",
    "mention": "123456789012345678",
    "default_language": "en",
    "available_languages": ["ko", "en"]
}
```
**Precautions**
You must adhere to the JSON syntax accurately. If you omit or write commas, quotation marks, curly braces, etc., incorrectly, the program may not work properly.
You must enter values that match the data type of each configuration item. For example, the time interval (interval) should be a number, and the webhook URL (webhook_url) should be a web address.
You must complete the webhook setup and user/role ID retrieval settings in Discord before you can properly use webhook_url and mention.