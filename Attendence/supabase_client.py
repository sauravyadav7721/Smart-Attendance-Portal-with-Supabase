from .clients import create_supabase_client

supabase = None
try:
    supabase = create_supabase_client()
except Exception:
    # Fail silently here -- calling code will 
    # handle exceptions when trying to use supabase
    supabase = None