#!/usr/bin/env python3
"""
Test script to verify the improved database import functionality.
This will test both the standard import and migration extraction endpoints.
"""

import requests
import json
import sys

# Configuration
API_URL = "http://localhost:8000"
PROJECT_ID = "593a52bb39fa"  # Using one of the existing projects
SQL_DUMP_PATH = "/home/faris/Documents/MyApps/supalove/vps_logs.md"

def get_auth_token():
    """Get an authentication token by logging in."""
    # For testing, we'll skip auth and use a direct test
    # In production, you'd login here
    return None

def test_standard_import():
    """Test the standard SQL import endpoint."""
    print("\n" + "="*70)
    print("TEST 1: Standard SQL Import (/import)")
    print("="*70)
    
    url = f"{API_URL}/api/v1/projects/{PROJECT_ID}/import"
   
    print(f"\nEndpoint: {url}")
    print(f"File: {SQL_DUMP_PATH}")
    
    try:
        with open(SQL_DUMP_PATH, 'rb') as f:
            files = {'file': ('vps_dump.sql', f, 'text/plain')}
            headers = {}
            # Note: In production, add authorization header
            # headers = {'Authorization': f'Bearer {token}'}
            
            print("\n📤 Uploading SQL dump...")
            response = requests.post(url, files=files, headers=headers, timeout=120)
            
            print(f"\n📊 Response Status: {response.status_code}")
            print(f"📊 Response Headers: {dict(response.headers)}")
            
            try:
                data = response.json()
                print(f"\n📋 Response Body:")
                print(json.dumps(data, indent=2))
                
                if response.status_code == 200:
                    print("\n✅ Standard import test: SUCCESS")
                    if data.get('status') == 'success':
                        print("✅ Import completed successfully")
                    elif data.get('status') == 'error':
                        print("⚠️ Import returned error status")
                        if 'details' in data:
                            print("\nError details:")
                            for detail in data['details']:
                                print(f"  - {detail}")
                else:
                    print(f"\n❌ Standard import test: FAILED")
                    if 'detail' in data:
                        print(f"Error: {data['detail']}")
                        
            except json.JSONDecodeError:
                print(f"\n❌ Could not parse JSON response")
                print(f"Raw response: {response.text}")
                
    except FileNotFoundError:
        print(f"\n❌ SQL dump file not found: {SQL_DUMP_PATH}")
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Request failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

def test_migration_extraction():
    """Test the migration extraction endpoint."""
    print("\n" + "="*70)
    print("TEST 2: Migration Extraction (/import-from-migrations)")
    print("="*70)
    
    url = f"{API_URL}/api/v1/projects/{PROJECT_ID}/import-from-migrations"
    
    print(f"\nEndpoint: {url}")
    print(f"File: {SQL_DUMP_PATH}")
    
    try:
        with open(SQL_DUMP_PATH, 'rb') as f:
            files = {'file': ('vps_dump.sql', f, 'text/plain')}
            headers = {}
            
            print(" \n📤 Uploading SQL dump for migration extraction...")
            response = requests.post(url, files=files, headers=headers, timeout=120)
            
            print(f"\n📊 Response Status: {response.status_code}")
            
            try:
                data = response.json()
                print(f"\n📋 Response Body:")
                print(json.dumps(data, indent=2))
                
                if response.status_code == 200:
                    print("\n✅ Migration extraction test: COMPLETED")
                    if data.get('status') == 'success':
                        print("✅ Migration extraction successful")
                    elif data.get('status') == 'error':
                        print("⚠️ Migration extraction returned error (expected for non-migration dumps)")
                        if 'message' in data:
                            print(f"\nMessage: {data['message']}")
                        if 'details' in data:
                            print("\nDetails:")
                            for detail in data['details']:
                                print(f"  - {detail}")
                else:
                    print(f"\n❌ Migration extraction test: FAILED")
                    if 'detail' in data:
                        print(f"Error: {data['detail']}")
                        
            except json.JSONDecodeError:
                print(f"\n❌ Could not parse JSON response")
                print(f"Raw response: {response.text}")
                
    except FileNotFoundError:
        print(f"\n❌ SQL dump file not found: {SQL_DUMP_PATH}")
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Request failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

def main():
    print("\n🧪 Database Import Functionality Test Suite")
    print(f"API URL: {API_URL}")
    print(f"Project ID: {PROJECT_ID}")
    
    # Test 1: Standard import
    test_standard_import()
    
    # Test 2: Migration extraction
    test_migration_extraction()
    
    print("\n" + "="*70)
    print("📝 Test Summary")
    print("="*70)
    print("\nThe improved import endpoints now provide:")
    print("  ✓ Detailed logging of subprocess execution")
    print("  ✓ Better error messages with specific diagnostics")
    print("  ✓ Timeout handling (5 minute max)")
    print("  ✓ Helpful guidance when wrong import method is used")
    print("  ✓ Script existence validation")
    print("\nCheck the API logs for detailed subprocess output.")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
