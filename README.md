# Django Supabase CRUD Application

A complete Django web application that demonstrates CRUD (Create, Read, Update, Delete) operations using Supabase as the backend database. This project includes a beautiful, modern web interface for managing items with full API endpoints.

## 🚀 Features

- **Complete CRUD Operations**: Create, Read, Update, and Delete items
- **Supabase Integration**: Uses Supabase as the backend database
- **Modern UI**: Beautiful, responsive web interface
- **RESTful API**: Full API endpoints for all operations
- **Search Functionality**: Search items by name or description
- **Real-time Updates**: Immediate UI updates after operations
- **Error Handling**: Comprehensive error handling and user feedback

## 🛠️ Tech Stack

- **Backend**: Django 5.2.3
- **Database**: Supabase (PostgreSQL)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Authentication**: Supabase Auth (ready for implementation)
- **Styling**: Custom CSS with modern gradients and animations

## 📋 Prerequisites

- Python 3.8 or higher
- A Supabase account and project
- Git

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ainativepoc
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory with your Supabase credentials:

```env
# Supabase Configuration
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key

# Django Configuration
SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Set Up Supabase Database

1. Go to your Supabase project dashboard
2. Navigate to the SQL Editor
3. Create the `items` table with the following SQL:

```sql
CREATE TABLE items (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10,2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    is_active BOOLEAN DEFAULT TRUE
);

-- Enable Row Level Security (optional)
ALTER TABLE items ENABLE ROW LEVEL SECURITY;

-- Create policy for public access (for demo purposes)
CREATE POLICY "Allow public access" ON items FOR ALL USING (true);
```

### 6. Run Django Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

### 8. Access the Application

Open your browser and navigate to:
- **Main Interface**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 📚 API Endpoints

The application provides the following RESTful API endpoints:

### Items API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/items/` | Get all items |
| GET | `/api/items/<id>/` | Get item by ID |
| POST | `/api/items/create/` | Create new item |
| PUT | `/api/items/<id>/update/` | Update item |
| DELETE | `/api/items/<id>/delete/` | Delete item |
| GET | `/api/items/search/?q=<term>` | Search items |

### Example API Usage

#### Create an Item
```bash
curl -X POST http://127.0.0.1:8000/api/items/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sample Item",
    "description": "This is a sample item",
    "price": 29.99
  }'
```

#### Get All Items
```bash
curl http://127.0.0.1:8000/api/items/
```

#### Update an Item
```bash
curl -X PUT http://127.0.0.1:8000/api/items/1/update/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Item",
    "price": 39.99
  }'
```

#### Delete an Item
```bash
curl -X DELETE http://127.0.0.1:8000/api/items/1/delete/
```

## 🏗️ Project Structure

```
ainativepoc/
├── supabase_crud/          # Main Django project
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   └── utils.py           # Supabase client utility
├── items/                  # Items app
│   ├── models.py          # Django models
│   ├── views.py           # API views
│   ├── urls.py            # App URL configuration
│   ├── supabase_service.py # Supabase CRUD service
│   └── templates/         # HTML templates
│       └── items/
│           └── index.html # Main interface
├── venv/                  # Virtual environment
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SUPABASE_URL` | Your Supabase project URL | Yes |
| `SUPABASE_KEY` | Your Supabase anon/public key | Yes |
| `SECRET_KEY` | Django secret key | Yes |
| `DEBUG` | Django debug mode | No (default: True) |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | No |

### Supabase Setup

1. **Create a Supabase Project**:
   - Go to [supabase.com](https://supabase.com)
   - Create a new project
   - Note down your project URL and anon key

2. **Database Schema**:
   - The application expects an `items` table
   - Use the SQL provided in the setup section

3. **Row Level Security**:
   - For production, configure proper RLS policies
   - For development, you can disable RLS or use permissive policies

## 🎨 Customization

### Adding New Fields

To add new fields to the items:

1. Update the `Item` model in `items/models.py`
2. Update the `to_dict()` method
3. Update the HTML form in `items/templates/items/index.html`
4. Update the JavaScript functions for form handling
5. Update the Supabase table schema

### Styling

The application uses custom CSS with modern design principles:
- Gradient backgrounds
- Card-based layouts
- Smooth animations
- Responsive design

You can customize the styling by modifying the CSS in `items/templates/items/index.html`.

## 🚀 Deployment

### Production Considerations

1. **Environment Variables**:
   - Set `DEBUG=False`
   - Use a strong `SECRET_KEY`
   - Configure proper `ALLOWED_HOSTS`

2. **Database**:
   - Use Supabase production database
   - Configure proper RLS policies
   - Set up database backups

3. **Security**:
   - Enable HTTPS
   - Configure CORS properly
   - Implement proper authentication

4. **Performance**:
   - Use a production WSGI server (Gunicorn)
   - Configure static file serving
   - Set up caching

## 🐛 Troubleshooting

### Common Issues

1. **Supabase Connection Error**:
   - Verify your `SUPABASE_URL` and `SUPABASE_KEY`
   - Check if your Supabase project is active
   - Ensure the `items` table exists

2. **CORS Issues**:
   - Configure CORS settings in Supabase
   - Check browser console for CORS errors

3. **Environment Variables**:
   - Ensure `.env` file is in the root directory
   - Restart the Django server after changing `.env`

4. **Database Schema**:
   - Run the SQL commands in Supabase SQL Editor
   - Check table structure matches the Django model

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section
2. Review the Supabase documentation
3. Check Django documentation
4. Open an issue on GitHub

## 🔮 Future Enhancements

- [ ] User authentication and authorization
- [ ] File upload functionality
- [ ] Real-time updates with WebSockets
- [ ] Advanced search and filtering
- [ ] Pagination for large datasets
- [ ] Export functionality (CSV, JSON)
- [ ] Bulk operations
- [ ] API rate limiting
- [ ] Comprehensive test suite

---

**Happy Coding! 🎉** 