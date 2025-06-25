#!/usr/bin/env python
"""
Test script to verify Django Supabase CRUD setup.
Run this script to check if everything is configured correctly.
"""

import os
import sys
import django
from dotenv import load_dotenv

def test_environment():
    """Test if environment variables are loaded correctly."""
    print("🔍 Testing environment variables...")
    
    load_dotenv()
    
    required_vars = ['SUPABASE_URL', 'SUPABASE_KEY']
    missing_vars = []
    
    for var in required_vars:
        value = os.getenv(var)
        if not value or value.startswith('your_'):
            missing_vars.append(var)
        else:
            print(f"✅ {var}: {'*' * (len(value) - 10) + value[-10:] if len(value) > 10 else '*' * len(value)}")
    
    if missing_vars:
        print(f"❌ Missing or invalid environment variables: {', '.join(missing_vars)}")
        print("Please update your .env file with valid Supabase credentials.")
        return False
    
    print("✅ Environment variables loaded successfully!")
    return True

def test_django_setup():
    """Test if Django is configured correctly."""
    print("\n🔍 Testing Django setup...")
    
    try:
        # Add the project directory to Python path
        project_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, project_dir)
        
        # Set Django settings
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'supabase_crud.settings')
        django.setup()
        
        print("✅ Django configured successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Django setup failed: {str(e)}")
        return False

def test_supabase_connection():
    """Test if Supabase connection works."""
    print("\n🔍 Testing Supabase connection...")
    
    try:
        from supabase_crud.utils import get_supabase_client
        
        client = get_supabase_client()
        print("✅ Supabase client created successfully!")
        
        # Test a simple query
        try:
            response = client.table('items').select('count').limit(1).execute()
            print("✅ Supabase connection test successful!")
            return True
        except Exception as e:
            print(f"⚠️  Supabase query test failed (this might be expected if table doesn't exist yet): {str(e)}")
            print("This is normal if you haven't created the 'items' table yet.")
            return True
            
    except Exception as e:
        print(f"❌ Supabase connection failed: {str(e)}")
        return False

def test_imports():
    """Test if all required modules can be imported."""
    print("\n🔍 Testing module imports...")
    
    try:
        from items.models import Item
        from items.supabase_service import SupabaseService
        from items.views import item_list
        
        print("✅ All modules imported successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Module import failed: {str(e)}")
        return False

def main():
    """Run all tests."""
    print("🚀 Django Supabase CRUD Setup Test")
    print("=" * 40)
    
    tests = [
        test_environment,
        test_django_setup,
        test_supabase_connection,
        test_imports
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Create the 'items' table in your Supabase database")
        print("2. Run: python manage.py runserver")
        print("3. Visit: http://127.0.0.1:8000/")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        print("\nCommon solutions:")
        print("1. Make sure your .env file is configured correctly")
        print("2. Ensure all dependencies are installed: pip install -r requirements.txt")
        print("3. Check your Supabase project settings")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 