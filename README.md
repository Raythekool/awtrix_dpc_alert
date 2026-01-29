# AWTRIX Civil Protection Alert 🇮🇹

Blueprint for Home Assistant that displays Italian Civil Protection weather alerts on your AWTRIX3 device.

## ⚠️ Requirements

Before using this blueprint, make sure you have:

1. **Home Assistant** with blueprint support
2. **AWTRIX 3** device configured and connected via MQTT
3. **DPC Alert Integration** installed from [caiosweet/Home-Assistant-custom-components-DPC-Alert](https://github.com/caiosweet/Home-Assistant-custom-components-DPC-Alert)

## 📦 Installation

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

## 🎨 Recommended Icons

For better visualization, upload these icons to your AWTRIX:

- **dpc-idraulico** (49300) - Hydraulic risk (floods, overflows)
- **dpc-temporali** (49299) - Storm risk
- **dpc-idrogeologico** (2289) - Hydrogeological risk (landslides, mudslides)
- **dpc-warning** (16754) - Generic alert icon

You can find more icons at [developer.lametric.com/icons](https://developer.lametric.com/icons) or create custom ones.

### 📤 Automatic Script to Upload Icons

We've included a script that automatically downloads the recommended icons from LaMetric and uploads them to your AWTRIX device.

**Quick usage:**

```bash
# Upload all recommended icons for DPC alerts (with IP provided)
./upload_icons.sh 192.168.1.100 --default-icons

# Or let the script prompt you for the IP address
./upload_icons.sh --default-icons

# Windows users can use the batch file
upload_icons.bat --default-icons

# Or use Python directly
python3 upload_icons.py --default-icons
```

If you don't provide the IP address, the script will prompt you to enter it interactively.

**Advanced options:**

```bash
# Display default icons
./upload_icons.sh --list-default

# Upload custom icons (will prompt for IP if not provided)
./upload_icons.sh --icon my-icon 12345 --icon another-icon 67890

# Combine default and custom icons with IP provided
./upload_icons.sh 192.168.1.100 --default-icons --icon custom-icon 99999
```

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
5. Save the automation

## 🎯 Features

- **Multi-sensor monitoring**: Supports multiple DPC sensors simultaneously
- **Criticality filter**: Shows only alerts above a certain level
- **Automatic colors**: Messages are colored based on criticality level
  - Green: Ordinary
  - Yellow: Moderate
  - Orange: High
  - Red: Extreme
- **Customizable icons**: Use different icons for each risk type
- **Multi-device**: Supports multiple AWTRIX devices simultaneously
- **Auto-clear**: Automatically removes alerts when they are no longer active

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