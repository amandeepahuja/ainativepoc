from typing import List, Dict, Optional
from supabase_crud.utils import get_supabase_client
from .models import Item

class SupabaseService:
    """
    Service class to handle CRUD operations with Supabase database.
    """
    
    def __init__(self):
        self.client = get_supabase_client()
        self.table_name = 'items'
    
    def create_item(self, item_data: Dict) -> Dict:
        """
        Create a new item in Supabase.
        
        Args:
            item_data: Dictionary containing item data
            
        Returns:
            Dictionary with created item data
        """
        try:
            # Remove id if present (Supabase will auto-generate)
            if 'id' in item_data:
                del item_data['id']
            
            response = self.client.table(self.table_name).insert(item_data).execute()
            
            if response.data:
                return response.data[0]
            else:
                raise Exception("Failed to create item")
                
        except Exception as e:
            raise Exception(f"Error creating item: {str(e)}")
    
    def get_all_items(self) -> List[Dict]:
        """
        Retrieve all items from Supabase.
        
        Returns:
            List of dictionaries containing item data
        """
        try:
            response = self.client.table(self.table_name).select('*').execute()
            return response.data
        except Exception as e:
            raise Exception(f"Error fetching items: {str(e)}")
    
    def get_item_by_id(self, item_id: int) -> Optional[Dict]:
        """
        Retrieve a specific item by ID from Supabase.
        
        Args:
            item_id: ID of the item to retrieve
            
        Returns:
            Dictionary containing item data or None if not found
        """
        try:
            response = self.client.table(self.table_name).select('*').eq('id', item_id).execute()
            
            if response.data:
                return response.data[0]
            return None
            
        except Exception as e:
            raise Exception(f"Error fetching item: {str(e)}")
    
    def update_item(self, item_id: int, item_data: Dict) -> Optional[Dict]:
        """
        Update an existing item in Supabase.
        
        Args:
            item_id: ID of the item to update
            item_data: Dictionary containing updated item data
            
        Returns:
            Dictionary with updated item data or None if not found
        """
        try:
            # Remove id from update data
            if 'id' in item_data:
                del item_data['id']
            
            response = self.client.table(self.table_name).update(item_data).eq('id', item_id).execute()
            
            if response.data:
                return response.data[0]
            return None
            
        except Exception as e:
            raise Exception(f"Error updating item: {str(e)}")
    
    def delete_item(self, item_id: int) -> bool:
        """
        Delete an item from Supabase.
        
        Args:
            item_id: ID of the item to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        try:
            response = self.client.table(self.table_name).delete().eq('id', item_id).execute()
            
            # Check if any rows were affected
            return len(response.data) > 0
            
        except Exception as e:
            raise Exception(f"Error deleting item: {str(e)}")
    
    def search_items(self, search_term: str) -> List[Dict]:
        """
        Search items by name or description.
        
        Args:
            search_term: Term to search for
            
        Returns:
            List of dictionaries containing matching items
        """
        try:
            response = self.client.table(self.table_name).select('*').or_(f'name.ilike.%{search_term}%,description.ilike.%{search_term}%').execute()
            return response.data
        except Exception as e:
            raise Exception(f"Error searching items: {str(e)}") 