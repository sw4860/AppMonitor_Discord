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
3.  In the "Advanced" settings menu, find and turn on the "[127.0.0.1:Port Number] Connect to Android" option.
4.  Check the BlueStacks settings for the port number required for ADB connection (usually 5555).

#### Nox Player

I don't know much about it. Sorry.
1.  Run Nox Player.
2.  Go to the Nox Player system settings (gear icon, etc.).
3.  In the "Advanced Settings" or "Performance Settings" menu, find and turn on the "Enable ADB Debugging" option.
4.  Check the Nox Player settings for the port number required for ADB connection (usually 62001).

#### LDPlayer

I don't know much about it. Sorry.
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

### 3. AppMonitor Setup

You are now basically ready to use `AppMonitor_Discord`!