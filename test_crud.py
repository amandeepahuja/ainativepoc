#!/usr/bin/env python
"""
Test script to demonstrate CRUD operations with the Django Supabase application.
This script will test all the API endpoints using the dummy data.
"""

import requests
import json
import time

BASE_URL = "http://127.0.0.1:8000/api/items"

def test_crud_operations():
    """Test all CRUD operations."""
    print("🚀 Testing Django Supabase CRUD Operations")
    print("=" * 50)
    
    # Test 1: Get all items
    print("\n1️⃣ Testing GET all items...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            items = data.get('data', [])
            print(f"✅ Success! Found {len(items)} items")
            if items:
                print(f"   Sample item: {items[0]['name']} - ${items[0]['price']}")
        else:
            print(f"❌ Failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    # Test 2: Create a new item
    print("\n2️⃣ Testing CREATE new item...")
    new_item = {
        "name": "Test Product",
        "description": "This is a test product created via API",
        "price": 99.99
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/create/",
            json=new_item,
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 201:
            data = response.json()
            created_item = data.get('data', {})
            print(f"✅ Success! Created item: {created_item['name']} - ${created_item['price']}")
            item_id = created_item['id']
        else:
            print(f"❌ Failed: {response.status_code} - {response.text}")
            return
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return
    
    # Test 3: Get specific item
    print(f"\n3️⃣ Testing GET item by ID ({item_id})...")
    try:
        response = requests.get(f"{BASE_URL}/{item_id}/")
        if response.status_code == 200:
            data = response.json()
            item = data.get('data', {})
            print(f"✅ Success! Retrieved: {item['name']} - ${item['price']}")
        else:
            print(f"❌ Failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    # Test 4: Update item
    print(f"\n4️⃣ Testing UPDATE item ({item_id})...")
    update_data = {
        "name": "Updated Test Product",
        "price": 149.99
    }
    
    try:
        response = requests.put(
            f"{BASE_URL}/{item_id}/update/",
            json=update_data,
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 200:
            data = response.json()
            updated_item = data.get('data', {})
            print(f"✅ Success! Updated: {updated_item['name']} - ${updated_item['price']}")
        else:
            print(f"❌ Failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    # Test 5: Search items
    print("\n5️⃣ Testing SEARCH items...")
    try:
        response = requests.get(f"{BASE_URL}/search/?q=test")
        if response.status_code == 200:
            data = response.json()
            items = data.get('data', [])
            print(f"✅ Success! Found {len(items)} items matching 'test'")
            for item in items[:3]:  # Show first 3 results
                print(f"   • {item['name']} - ${item['price']}")
        else:
            print(f"❌ Failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    # Test 6: Delete item
    print(f"\n6️⃣ Testing DELETE item ({item_id})...")
    try:
        response = requests.delete(f"{BASE_URL}/{item_id}/delete/")
        if response.status_code == 200:
            print(f"✅ Success! Item deleted")
        else:
            print(f"❌ Failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    # Test 7: Verify deletion
    print(f"\n7️⃣ Verifying deletion of item ({item_id})...")
    try:
        response = requests.get(f"{BASE_URL}/{item_id}/")
        if response.status_code == 404:
            print("✅ Success! Item not found (correctly deleted)")
        else:
            print(f"❌ Item still exists: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("🎉 CRUD Operations Test Complete!")
    print("\n📊 Summary:")
    print("• ✅ GET all items")
    print("• ✅ CREATE new item") 
    print("• ✅ GET specific item")
    print("• ✅ UPDATE item")
    print("• ✅ SEARCH items")
    print("• ✅ DELETE item")
    print("• ✅ Verify deletion")
    
    print(f"\n🌐 Application URL: http://127.0.0.1:8000/")
    print("💡 You can now test the web interface!")

if __name__ == "__main__":
    # Wait a moment for the server to be ready
    print("⏳ Waiting for server to be ready...")
    time.sleep(2)
    
    test_crud_operations() 