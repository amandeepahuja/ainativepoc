# Quick Setup Guide

## 🚀 Get Started in 3 Steps

### 1. Configure Supabase

1. Go to [supabase.com](https://supabase.com) and create a free account
2. Create a new project
3. Go to **Settings** → **API** in your project dashboard
4. Copy your **Project URL** and **anon/public key**

### 2. Update Environment Variables

Edit the `.env` file in your project root and replace the placeholder values:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-actual-anon-key-here
SECRET_KEY=django-insecure-8t_x1)!&l(dhwfznvq@$n*nj!ta_21xol2rzk5(xg9sdes)*eg
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3. Create Database Table

1. Go to your Supabase project dashboard
2. Navigate to **SQL Editor**
3. Run this SQL command:

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
```

## 🎉 You're Ready!

- **Application URL**: http://127.0.0.1:8000/
- **API Endpoints**: Available at `/api/items/`

## 🔧 Troubleshooting

- **"Supabase not configured" error**: Make sure your `.env` file has the correct credentials
- **"Table doesn't exist" error**: Run the SQL command above in Supabase SQL Editor
- **Server won't start**: Check that all dependencies are installed with `pip install -r requirements.txt`

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore the API endpoints
- Customize the application for your needs 