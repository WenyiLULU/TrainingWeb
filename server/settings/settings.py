# API settings
API_ROUTE = "/api/v1"
API_HOST = "localhost"
API_PORT = 5200
API_NAME = "TrainingWenyi"

# Database settings
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = API_NAME
DB_TYPE = "postgresql"
DB_USER = "postgres"
DB_PASS = "postgres"
DATABASE_URL = f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
