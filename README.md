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

**🧪 Test Notification Blueprint** - Send test notifications to verify your setup:
```
https://github.com/Raythekool/awtrix_dpc_alert/blob/main/awtrix_dpc_alert_test.yaml
```

**🗑️ Clear App Blueprint** - Remove the DPC Alert app from all AWTRIX devices:
```
https://github.com/Raythekool/awtrix_dpc_alert/blob/main/awtrix_dpc_alert_clear.yaml
```

## 🎨 Recommended Icons

For better visualization, upload these icons to your AWTRIX:

- **dpc-idraulico** (49300) - Hydraulic risk (floods, overflows)
- **dpc-temporali** (49299) - Storm risk
- **dpc-idrogeologico** (2289) - Hydrogeological risk (landslides, mudslides)
- **dpc-warning** (16754) - Generic alert icon

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
- Downloads icons from LaMetric's public icon library
- Converts and uploads them to your AWTRIX device via HTTP API
- No additional dependencies needed - uses only Python 3 standard library
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
   - **Message Duration**: Display time in seconds (default: 20)
   - **Icons**: Customize icon IDs for each risk type
   - **Enable Sound**: Toggle sound notifications
   - **Sound Level**: Minimum alert level to play sound (default: Orange/High)
5. Save the automation

### 🧪 Testing Your Setup

After installing the test blueprint, create an automation to send test notifications:

1. Go to Home Assistant → Settings → Automations & Scenes
2. Click "Create Automation" → "Use a blueprint"
3. Select "AWTRIX DPC Alert - Test Notification 🧪"
4. Configure:
   - Select your AWTRIX device(s)
   - Choose a test criticality level (1-4)
   - Enable sound if desired
5. Save the automation and trigger it manually to test

### 🗑️ Clearing the Display

If you need to remove the DPC Alert app from your AWTRIX devices:

1. Create an automation using the "AWTRIX DPC Alert - Clear App 🗑️" blueprint
2. Select your AWTRIX device(s)
3. Save and trigger it manually whenever needed

## 🎯 Features

- **Multi-sensor monitoring**: Supports multiple DPC sensors simultaneously
- **Criticality filter**: Shows only alerts above a certain level
- **Automatic colors**: Messages are colored based on criticality level
  - Green: Ordinary
  - Yellow: Moderate
  - Orange: High
  - Red: Extreme
- **Customizable icons**: Use different icons for each risk type
- **Sound notifications**: Optional sound alerts for critical warnings
- **Multi-device**: Supports multiple AWTRIX devices simultaneously
- **Auto-clear**: Automatically removes alerts when they are no longer active
- **Test mode**: Send test notifications to verify configuration
- **Manual clear**: Remove apps from display when needed

## 🔧 Advanced Configuration

### Customizing Message Duration

The "Message Duration" parameter controls how long the alert remains on screen:
- `0` = use the device's global time setting
- `1-300` = specific seconds (maximum 5 minutes)

### Using Custom Icons

You can use any icon from LaMetric or upload custom ones to your AWTRIX. Just enter the icon ID in the corresponding fields.

## 📝 Notes

- The blueprint uses "restart" mode to avoid duplicates when multiple alerts arrive
- Alerts are published to MQTT on the topic `custom/dpc_alert`
- If there are multiple active alerts, they will be displayed in sequence

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or pull request.

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more details.

## 🙏 Credits

- DPC Alert Integration: [caiosweet](https://github.com/caiosweet/Home-Assistant-custom-components-DPC-Alert)
- AWTRIX 3: [Blueforcer](https://github.com/Blueforcer/awtrix3)
- Inspiration from flow: [Blueforcer Flow](https://flows.blueforcer.de/flow/rM3xOBxvA8Lz#)