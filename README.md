# AWTRIX Civil Protection Alert 🇮🇹

Blueprint for Home Assistant that displays Italian Civil Protection weather alerts on your AWTRIX3 device.

## ⚠️ Requirements

Before using this blueprint, make sure you have:

1. **Home Assistant** with blueprint support
2. **AWTRIX 3** device configured and connected via MQTT
3. **DPC Alert Integration** installed from [caiosweet/Home-Assistant-custom-components-DPC-Alert](https://github.com/caiosweet/Home-Assistant-custom-components-DPC-Alert)

## 📦 Installation

### Main Blueprint

### Method 1: Automatic Import (recommended)

1. Click the button below to import the blueprint:

   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FRaythekool%2Fawtrix_dpc_alert%2Fblob%2Fmain%2Fawtrix_dpc_alert.yaml)

2. Click "Import Blueprint" in your Home Assistant
3. The blueprint will be available in your automations

### Method 2: Manual Import

1. Go to Home Assistant → Settings → Automations & Scenes → Blueprints
2. Click the "Import Blueprint" button
3. Enter this URL:
   ```
   https://github.com/Raythekool/awtrix_dpc_alert/blob/main/awtrix_dpc_alert.yaml
   ```
4. Click "Preview" and then "Import Blueprint"

### Method 3: Local File

1. Download the `awtrix_dpc_alert.yaml` file
2. Copy the file to the `blueprints/automation/` folder in your Home Assistant configuration
3. Restart Home Assistant or reload automations

### Optional Helper Blueprints

For testing and management, you can also install these helper blueprints:

#### 🧪 Test Notification Blueprint

This blueprint allows you to send test notifications to your AWTRIX devices to verify your configuration is working correctly.

**Features:**
- Send test notifications with different criticality levels (1-4)
- Test icon display
- Test sound notifications
- Configurable message and notification durations
- Choose display mode: Custom App (persistent), Notification (temporary), or Both
- Automatic hold mode when notification duration is set to 0

**Import:**

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FRaythekool%2Fawtrix_dpc_alert%2Fblob%2Fmain%2Fawtrix_dpc_alert_test.yaml)

Or manually import this URL:
```
https://github.com/Raythekool/awtrix_dpc_alert/blob/main/awtrix_dpc_alert_test.yaml
```

#### 🗑️ Clear App Blueprint

This blueprint removes the DPC Alert custom app from your AWTRIX devices when you need to clear the display.

**Features:**
- Quickly remove DPC Alert app from all configured devices
- Useful for troubleshooting or cleaning up
- Manually triggered when needed

**Import:**

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FRaythekool%2Fawtrix_dpc_alert%2Fblob%2Fmain%2Fawtrix_dpc_alert_clear.yaml)

Or manually import this URL:
```
https://github.com/Raythekool/awtrix_dpc_alert/blob/main/awtrix_dpc_alert_clear.yaml
```

## 🎨 Recommended Icons

For better visualization, upload these icons to your AWTRIX:

- **dpc-idraulico** (49300) - Hydraulic risk (floods, overflows)
- **dpc-temporali** (49299) - Storm risk
- **dpc-idrogeologico** (2289) - Hydrogeological risk (landslides, mudslides)
- **dpc-warning** (16754) - Generic alert icon

**Important:** AWTRIX supports GIF format icons. The upload script automatically prioritizes downloading GIF versions over PNG format for better compatibility.

You can find more icons at [developer.lametric.com/icons](https://developer.lametric.com/icons) or create custom ones.

### 📤 Automatic Script to Upload Icons

We've included a script that automatically downloads the recommended icons from LaMetric and uploads them to your AWTRIX device.

**Easiest method - Just run the script:**

```bash
# Linux/Mac - runs with default icons, prompts for IP
./upload_icons.sh

# Windows - runs with default icons, prompts for IP
upload_icons.bat

# Or use Python directly
python3 upload_icons.py
```

When you run the script without any parameters, it will:
1. Prompt you to enter your AWTRIX device IP address
2. Automatically download all 4 recommended DPC icons from LaMetric
3. Upload them to your AWTRIX device

**Quick usage with IP address:**

```bash
# Provide IP address directly (Linux/Mac)
./upload_icons.sh 192.168.1.100

# Provide IP address directly (Windows)
upload_icons.bat 192.168.1.100

# Or use Python directly
python3 upload_icons.py 192.168.1.100
```

**Advanced options:**

```bash
# Display the list of default icons without uploading
./upload_icons.sh --list-default

# Upload specific custom icons (prompts for IP if not provided)
./upload_icons.sh --icon my-icon 12345 --icon another-icon 67890

# Combine default and custom icons
./upload_icons.sh 192.168.1.100 --default-icons --icon custom-icon 99999

# Upload only custom icons (no defaults)
./upload_icons.sh 192.168.1.100 --icon my-custom-icon 54321
```

**What the script does:**
- Downloads icons from LaMetric's public icon library (prioritizes GIF format)
- Converts and uploads them to your AWTRIX device `/ICONS/` folder via HTTP API
- No additional dependencies needed - uses only Python 3 standard library with requests module
- Works on Linux, Mac, and Windows

The script automatically downloads icons from LaMetric and uploads them to your AWTRIX via HTTP. No additional dependencies are needed, it only uses Python 3 standard library.

## 🚀 Usage

1. Go to Home Assistant → Settings → Automations & Scenes
2. Click "Create Automation" → "Use a blueprint"
3. Select "AWTRIX Civil Protection Alert 🇮🇹"
4. Configure the parameters:
   - **AWTRIX Device**: Select your AWTRIX device
   - **DPC Alert Sensors**: Select the alert sensors to monitor
   - **Minimum Alert Level**: Set the minimum level (0-4)
     - 0 = Show all alerts
     - 1 = Green (Ordinary criticality)
     - 2 = Yellow (Moderate criticality)
     - 3 = Orange (High criticality)
     - 4 = Red (Extreme criticality)
   - **Message Duration**: Display time for custom app in seconds (default: 20)
   - **Notification Duration**: Display time for notifications in seconds (default: 0 = hold until dismissed)
   - **Icons**: Customize icon names for each risk type (without extension)
   - **Enable Sound**: Toggle sound notifications
   - **Sound Level**: Minimum alert level to play sound (default: Orange/High)
   - **Display Mode**: Choose how to display alerts:
     - Custom App (Persistent): Stays on screen until cleared
     - Notification (Temporary): Pop-up that auto-dismisses or holds based on duration
     - Both: Send both custom app and notification
5. Save the automation

### 🧪 Testing Your Setup

After installing the test blueprint, create an automation to send test notifications:

1. Go to Home Assistant → Settings → Automations & Scenes
2. Click "Create Automation" → "Use a blueprint"
3. Select "AWTRIX DPC Alert - Test Notification 🧪"
4. Configure:
   - Select your AWTRIX device(s)
   - Choose a test criticality level (1-4)
   - Set message duration (for custom app) and notification duration (0 = hold until dismissed)
   - Enable sound if desired
   - Choose display mode: Custom App (persistent), Notification (temporary), or Both
5. Save the automation and trigger it manually to test

### 🗑️ Clearing the Display

If you need to remove the DPC Alert app from your AWTRIX devices:

1. Create an automation using the "AWTRIX DPC Alert - Clear App 🗑️" blueprint
2. Select your AWTRIX device(s)
3. Save and trigger it manually whenever needed

## 🎯 Features

- **Multi-sensor monitoring**: Supports multiple DPC sensors simultaneously
- **Criticality filter**: Shows only alerts above a certain level
- **Automatic colors**: Messages are colored based on criticality level (vivid colors)
  - Blue: No alert
  - Green: Ordinary
  - Yellow: Moderate
  - Dark Orange: High
  - Red: Extreme
- **Ripple effect**: Visual background effect for high-criticality alerts (levels 3 and 4)
- **Customizable icons**: Use different icons for each risk type (GIF format recommended)
- **Sound notifications**: Optional sound alerts for critical warnings with configurable threshold
- **Display modes**: Choose between Custom App (persistent), Notification (temporary), or Both
- **Flexible duration**: Separate durations for custom apps and notifications
- **Hold mode**: Notifications with duration 0 stay on screen until manually dismissed
- **Multi-device**: Supports multiple AWTRIX devices simultaneously
- **Auto-clear**: Automatically removes alerts when they are no longer active
- **Test mode**: Send test notifications to verify configuration with all display options
- **Manual clear**: Remove apps from display when needed

## 🔧 Advanced Configuration

### Customizing Message Duration

The blueprint provides two duration settings:

- **Message Duration**: Controls display time for custom apps (persistent mode)
  - `0` = use the device's global time setting
  - `1-300` = specific seconds (maximum 5 minutes)

- **Notification Duration**: Controls display time for notifications
  - `0` = hold mode (notification stays until manually dismissed via middle button)
  - `1-300` = auto-dismiss after specified seconds

### Display Modes

The blueprint supports three display modes:

- **Custom App (Persistent)**: Alert stays on AWTRIX as a persistent app until cleared
  - Published to MQTT topic `{prefix}/custom/dpc_alert`
  - Uses message_duration setting
  - Ideal for ongoing alerts you want to monitor continuously

- **Notification (Temporary)**: Pop-up notification that appears immediately
  - Published to MQTT topic `{prefix}/notify`
  - Uses notification_duration setting
  - When duration is 0, includes `hold: true` (dismiss with middle button)
  - Ideal for immediate attention alerts

- **Both**: Sends both custom app and notification simultaneously
  - Maximum visibility for critical alerts
  - Custom app persists while notification provides immediate pop-up

### Visual Effects

The blueprint automatically applies visual effects based on alert severity:

- **Ripple Effect**: Applied only to high-criticality alerts (levels 3 and 4)
  - Creates an animated background ripple effect
  - Uses default AWTRIX settings (speed=3, Rainbow palette, blend=true)
  - Lower severity alerts (levels 1-2) display without effects

### Using Custom Icons


### Using Custom Icons

You can use any icon from LaMetric or upload custom ones to your AWTRIX `/ICONS/` folder. Enter the icon filename (without extension) in the corresponding fields. The blueprint references icons by name, not by LaMetric ID.

**Icon format:** GIF format is recommended for best compatibility with AWTRIX.

### AWTRIX Notifications vs Custom Apps

Understanding the difference between display modes:

- **Custom App**: Persistent alert that stays visible until cleared
  - Topic: `{prefix}/custom/dpc_alert`
  - Duration controlled by `message_duration`
  - Best for: Ongoing weather alerts you want to monitor
  
- **Notification**: Temporary pop-up that overlays current display
  - Topic: `{prefix}/notify`
  - Duration controlled by `notification_duration`
  - When duration = 0: Includes `hold: true` (manual dismiss required)
  - Best for: Immediate attention alerts

- **Both**: Combines persistence and immediacy
  - Custom app provides continuous visibility
  - Notification ensures immediate attention

### Payload Structure

The blueprint generates AWTRIX-compatible payloads with these properties:

```json
{
  "icon": "dpc-warning",
  "text": "Alert message",
  "duration": 20,
  "color": "#FF6000",
  "stack": false,
  "overlay": "clear",
  "effect": "Ripple",     // Only for levels 3-4
  "sound": "alarm",       // Optional, based on settings
  "hold": true            // Only for notifications with duration=0
}
```

## 📝 Notes

- The blueprint uses "restart" mode to avoid duplicates when multiple alerts arrive
- Custom apps are published to MQTT topic `{prefix}/custom/dpc_alert`
- Notifications are published to MQTT topic `{prefix}/notify`
- If there are multiple active alerts, they will be displayed in sequence
- Ripple effect is automatically applied only to high-criticality alerts (levels 3-4)
- Icon files should be in GIF format and uploaded to AWTRIX `/ICONS/` folder
- Notifications with duration=0 automatically use hold mode (manual dismiss required)
- Home Assistant's Jinja2 sandbox restrictions: Uses `dict()` constructor instead of `.update()` method

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or pull request.

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more details.

## 🙏 Credits

- DPC Alert Integration: [caiosweet](https://github.com/caiosweet/Home-Assistant-custom-components-DPC-Alert)
- AWTRIX 3: [Blueforcer](https://github.com/Blueforcer/awtrix3)
- Inspiration from flow: [Blueforcer Flow](https://flows.blueforcer.de/flow/rM3xOBxvA8Lz#)