#!/usr/bin/env python3
"""
Script to download icons from LaMetric and upload them to AWTRIX device.

This script helps you easily upload the necessary icons for the DPC Alert blueprint
to your AWTRIX 3 device.
"""

import argparse
import sys
import urllib.request
import urllib.error
import json
from pathlib import Path
from typing import List, Tuple


# Default recommended icons for DPC alerts
DEFAULT_ICONS = {
    "dpc-idraulico": 49300,
    "dpc-temporali": 49299,
    "dpc-idrogeologico": 2289,
    "dpc-warning": 16754,
}


def download_icon(icon_id: int) -> Tuple[bytes, str]:
    """
    Download an icon from LaMetric by its ID.
    
    Args:
        icon_id: The LaMetric icon ID
        
    Returns:
        Tuple of (icon_data, file_extension)
        
    Raises:
        urllib.error.URLError: If download fails
    """
    # Try PNG first, then GIF
    for ext in ['png', 'gif']:
        url = f"https://developer.lametric.com/content/apps/icon_thumbs/{icon_id}_icon_thumb.{ext}"
        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                data = response.read()
                if data:
                    print(f"  ✓ Downloaded icon {icon_id} ({ext.upper()})")
                    return data, ext
        except urllib.error.HTTPError:
            continue
    
    raise urllib.error.URLError(f"Could not download icon {icon_id}")


def upload_icon_to_awtrix(device_ip: str, icon_name: str, icon_data: bytes, file_ext: str) -> bool:
    """
    Upload an icon to AWTRIX device via HTTP.
    
    Args:
        device_ip: IP address of the AWTRIX device
        icon_name: Name for the icon file (without extension)
        icon_data: Binary icon data
        file_ext: File extension (png or gif)
        
    Returns:
        True if successful, False otherwise
    """
    # AWTRIX uses an /edit endpoint for file uploads
    url = f"http://{device_ip}/edit"
    
    # Create multipart form data
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    
    # Build the multipart body
    body = []
    body.append(f'--{boundary}'.encode())
    body.append(f'Content-Disposition: form-data; name="data"; filename="/{icon_name}.{file_ext}"'.encode())
    body.append(f'Content-Type: image/{file_ext}'.encode())
    body.append(b'')
    body.append(icon_data)
    body.append(f'--{boundary}--'.encode())
    body.append(b'')
    
    body_bytes = b'\r\n'.join(body)
    
    # Create request
    req = urllib.request.Request(
        url,
        data=body_bytes,
        headers={
            'Content-Type': f'multipart/form-data; boundary={boundary}',
            'Content-Length': str(len(body_bytes))
        }
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status in [200, 201]:
                print(f"  ✓ Uploaded {icon_name}.{file_ext} to AWTRIX")
                return True
            else:
                print(f"  ✗ Upload failed with status {response.status}")
                return False
    except urllib.error.URLError as e:
        print(f"  ✗ Upload failed: {e}")
        return False


def process_icon(device_ip: str, icon_name: str, icon_id: int) -> bool:
    """
    Download an icon from LaMetric and upload it to AWTRIX.
    
    Args:
        device_ip: IP address of the AWTRIX device
        icon_name: Name for the icon
        icon_id: LaMetric icon ID
        
    Returns:
        True if successful, False otherwise
    """
    print(f"\nProcessing {icon_name} (ID: {icon_id})...")
    
    try:
        # Download icon from LaMetric
        icon_data, file_ext = download_icon(icon_id)
        
        # Upload to AWTRIX
        return upload_icon_to_awtrix(device_ip, icon_name, icon_data, file_ext)
    
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Download icons from LaMetric and upload them to AWTRIX device.',
        epilog='Example: %(prog)s 192.168.1.100 --default-icons'
    )
    
    parser.add_argument(
        'device_ip',
        nargs='?',
        help='IP address of the AWTRIX device (e.g., 192.168.1.100)'
    )
    
    parser.add_argument(
        '--default-icons',
        action='store_true',
        help='Upload the default recommended icons for DPC alerts'
    )
    
    parser.add_argument(
        '--icon',
        action='append',
        nargs=2,
        metavar=('NAME', 'ID'),
        help='Add a custom icon (can be used multiple times). Example: --icon my-icon 12345'
    )
    
    parser.add_argument(
        '--list-default',
        action='store_true',
        help='List the default recommended icons and exit'
    )
    
    args = parser.parse_args()
    
    # List default icons and exit
    if args.list_default:
        print("Default recommended icons for DPC alerts:")
        print()
        for name, icon_id in DEFAULT_ICONS.items():
            print(f"  {name:20} - ID: {icon_id}")
        return 0
    
    # Validate device IP is provided
    if not args.device_ip:
        print("Error: device_ip is required when uploading icons")
        print("Run with --help for more information.")
        return 1
    
    # Build list of icons to upload
    icons_to_upload = {}
    
    if args.default_icons:
        icons_to_upload.update(DEFAULT_ICONS)
    
    if args.icon:
        for name, icon_id in args.icon:
            try:
                icons_to_upload[name] = int(icon_id)
            except ValueError:
                print(f"Error: Icon ID must be a number, got '{icon_id}'")
                return 1
    
    # Validate we have icons to upload
    if not icons_to_upload:
        print("Error: No icons specified. Use --default-icons or --icon to specify icons to upload.")
        print("Run with --help for more information.")
        return 1
    
    # Process all icons
    print(f"Uploading {len(icons_to_upload)} icon(s) to AWTRIX at {args.device_ip}")
    print("=" * 60)
    
    success_count = 0
    for icon_name, icon_id in icons_to_upload.items():
        if process_icon(args.device_ip, icon_name, icon_id):
            success_count += 1
    
    # Summary
    print()
    print("=" * 60)
    print(f"Summary: {success_count}/{len(icons_to_upload)} icons uploaded successfully")
    
    return 0 if success_count == len(icons_to_upload) else 1


if __name__ == "__main__":
    sys.exit(main())
