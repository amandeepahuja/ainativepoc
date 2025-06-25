from typing import List, Dict, Optional
from .models import Item
from django.utils import timezone

class LocalService:
    """
    Local database service for CRUD operations when Supabase is not available.
    This allows testing the application with Django's local SQLite database.
    """
    
    def create_item(self, item_data: Dict) -> Dict:
        """
        Create a new item in local database.
        """
        try:
            # Remove id if present
            if 'id' in item_data:
                del item_data['id']
            
            # Create the item
            item = Item.objects.create(**item_data)
            
            return item.to_dict()
                
        except Exception as e:
            raise Exception(f"Error creating item: {str(e)}")
    
    def get_all_items(self) -> List[Dict]:
        """
        Retrieve all items from local database.
        """
        try:
            items = Item.objects.all().order_by('-created_at')
            return [item.to_dict() for item in items]
        except Exception as e:
            raise Exception(f"Error fetching items: {str(e)}")
    
    def get_item_by_id(self, item_id: int) -> Optional[Dict]:
        """
        Retrieve a specific item by ID from local database.
        """
        try:
            item = Item.objects.filter(id=item_id).first()
            return item.to_dict() if item else None
            
        except Exception as e:
            raise Exception(f"Error fetching item: {str(e)}")
    
    def update_item(self, item_id: int, item_data: Dict) -> Optional[Dict]:
        """
        Update an existing item in local database.
        """
        try:
            # Remove id from update data
            if 'id' in item_data:
                del item_data['id']
            
            # Update the item
            item = Item.objects.filter(id=item_id).first()
            if not item:
                return None
            
            for key, value in item_data.items():
                setattr(item, key, value)
            
            item.updated_at = timezone.now()
            item.save()
            
            return item.to_dict()
            
        except Exception as e:
            raise Exception(f"Error updating item: {str(e)}")
    
    def delete_item(self, item_id: int) -> bool:
        """
        Delete an item from local database.
        """
        try:
            item = Item.objects.filter(id=item_id).first()
            if not item:
                return False
            
            item.delete()
            return True
            
        except Exception as e:
            raise Exception(f"Error deleting item: {str(e)}")
    
    def search_items(self, search_term: str) -> List[Dict]:
        """
        Search items by name or description in local database.
        """
        try:
            items = Item.objects.filter(
                name__icontains=search_term
            ) | Item.objects.filter(
                description__icontains=search_term
            )
            
            return [item.to_dict() for item in items.order_by('-created_at')]
        except Exception as e:
            raise Exception(f"Error searching items: {str(e)}") 