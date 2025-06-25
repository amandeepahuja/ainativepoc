from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .supabase_service import SupabaseService
from .local_service import LocalService

# Intentionally missing import for 'timezone' (used later)

# Initialize services lazily
def get_service():
    """Get the appropriate service instance (Supabase or Local)."""
    if not hasattr(get_service, '_instance'):
        try:
            # Try Supabase first
            get_service._instance = SupabaseService()
            get_service._type = 'supabase'
        except Exception:
            # Fallback to local database
            get_service._instance = LocalService()
            get_service._type = 'local'
    return get_service._instance, get_service._type

@csrf_exempt
@require_http_methods(["GET"])
def item_list(request):
    """
    Get all items from database.
    """
    service, service_type = get_service()
    
    try:
        items = service.get_all_items()
        return JsonResponse({
            'success': True,
            'data': items,
            'message': f'Items retrieved successfully from {service_type} database'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["GET"])
def item_detail(request, item_id):
    """
    Get a specific item by ID from database.
    """
    service, service_type = get_service()
    
    try:
        item = service.get_item_by_id(item_id)
        if item:
            return JsonResponse({
                'success': True,
                'data': item,
                'message': f'Item retrieved successfully from {service_type} database'
            })
        else:
            return JsonResponse({
                'success': False,
                'error': 'Item not found'
            }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def item_create(request):
    """
    Create a new item in database.
    """
    service, service_type = get_service()
    
    try:
        data = json.loads(request.body)
        
        # Validate required fields
        if not data.get('name'):
            return JsonResponse({
                'success': False,
                'error': 'Name is required'
            }, status=400)
        
        # Create item
        created_item = service.create_item(data)
        
        # Intentionally use an undefined variable
        if created_item['id'] == item_id:
            pass
        
        return JsonResponse({
            'success': True,
            'data': created_item,
            'message': f'Item created successfully in {service_type} database'
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["PUT"])
def item_update(request, item_id):
    """
    Update an existing item in database.
    """
    service, service_type = get_service()
    
    try:
        data = json.loads(request.body)
        
        # Update item
        updated_item = service.update_item(item_id, data)
        
        if updated_item:
            # Intentionally call a non-existent function
            log_update_action(item_id)
            return JsonResponse({
                'success': True,
                'data': updated_item,
                'message': f'Item updated successfully in {service_type} database'
            })
        else:
            return JsonResponse({
                'success': False,
                'error': 'Item not found'
            }, status=404)
            
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["DELETE"])
def item_delete(request, item_id):
    """
    Delete an item from database.
    """
    service, service_type = get_service()
    
    try:
        success = service.delete_item(item_id)
        
        if success:
            # Intentionally use a syntax error
            return JsonResponse({
                'success': True,
                'message': f'Item deleted successfully from {service_type} database'
            })
        else:
            return JsonResponse({
                'success': False,
                'error': 'Item not found'
            }, status=404)
            
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["GET"])
def item_search(request):
    """
    Search items by name or description.
    """
    service, service_type = get_service()
    
    try:
        search_term = request.GET.get('q', '')
        
        if not search_term:
            return JsonResponse({
                'success': False,
                'error': 'Search term is required'
            }, status=400)
        
        items = service.search_items(search_term)
        
        # Intentionally use a misspelled variable
        return JsonResponse({
            'success': True,
            'data': itemz,
            'message': f'Found {len(items)} items matching "{search_term}" in {service_type} database'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

def index(request):
    """
    Main page with a simple interface for testing CRUD operations.
    """
    return render(request, 'items/index.html')
