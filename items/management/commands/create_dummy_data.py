from django.core.management.base import BaseCommand
from django.utils import timezone
from items.models import Item
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Create dummy items for testing CRUD operations'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of dummy items to create (default: 10)'
        )

    def handle(self, *args, **options):
        count = options['count']
        
        # Sample data for generating realistic items
        item_names = [
            "Laptop Computer", "Smartphone", "Wireless Headphones", "Coffee Maker",
            "Fitness Tracker", "Bluetooth Speaker", "Tablet", "Gaming Console",
            "Digital Camera", "Smart Watch", "Portable Charger", "Wireless Mouse",
            "Mechanical Keyboard", "USB-C Cable", "Power Bank", "Webcam",
            "Microphone", "Monitor Stand", "Desk Lamp", "Office Chair"
        ]
        
        descriptions = [
            "High-quality product with excellent features",
            "Perfect for daily use and professional work",
            "Compact and portable design",
            "Advanced technology with user-friendly interface",
            "Durable construction for long-lasting performance",
            "Modern design with cutting-edge features",
            "Affordable option with great value",
            "Premium quality for demanding users",
            "Versatile product for multiple applications",
            "Innovative design with smart functionality"
        ]
        
        # Price ranges for realistic pricing
        price_ranges = [
            (10.00, 50.00),    # Budget items
            (50.00, 150.00),   # Mid-range items
            (150.00, 500.00),  # Premium items
            (500.00, 2000.00), # High-end items
        ]
        
        created_items = []
        
        for i in range(count):
            # Generate random item data
            name = random.choice(item_names)
            description = random.choice(descriptions)
            price_range = random.choice(price_ranges)
            price = Decimal(str(round(random.uniform(price_range[0], price_range[1]), 2)))
            
            # Create the item
            item = Item.objects.create(
                name=f"{name} #{i+1}",
                description=description,
                price=price,
                is_active=random.choice([True, True, True, False])  # 75% chance of being active
            )
            created_items.append(item)
            
            self.stdout.write(
                self.style.SUCCESS(f'Created item: {item.name} - ${item.price}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully created {len(created_items)} dummy items!'
            )
        )
        
        # Show summary
        total_value = sum(item.price for item in created_items if item.price)
        active_items = sum(1 for item in created_items if item.is_active)
        
        self.stdout.write(f'Total items: {len(created_items)}')
        self.stdout.write(f'Active items: {active_items}')
        self.stdout.write(f'Total value: ${total_value:.2f}')
        
        # Show sample items
        self.stdout.write('\nSample items created:')
        for item in created_items[:5]:
            status = "✅ Active" if item.is_active else "❌ Inactive"
            self.stdout.write(f'  • {item.name} - ${item.price} ({status})') 