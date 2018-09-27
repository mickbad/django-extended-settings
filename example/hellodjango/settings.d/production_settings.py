# --------------------------------------------------------------------------------------------
# - Fichier de configuration locale
# --------------------------------------------------------------------------------------------

# debuggage
DEBUG = False

# Make these unique, and don't share it with anybody.
SECRET_KEY = "=oopslala--"
NEVERCACHE_KEY = "--lalaoops=="

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": os.path.join(BASE_DIR, 'testing.db'),
    }
}

# Allowed development hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "::1"]


