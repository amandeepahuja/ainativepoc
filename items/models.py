from django.db import models
from django.utils import timezone

class Item(models.Model):
    """
    Item model for CRUD operations with Supabase.
    This model represents the structure of data we'll store in Supabase.
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'items'  # This will be the table name in Supabase
        
    def __str__(self):
        return self.name
    
    def to_dict(self):
        """
        Convert model instance to dictionary for Supabase operations.
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': float(self.price) if self.price else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'is_active': self.is_active
        }
