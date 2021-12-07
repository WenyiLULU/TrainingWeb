from pydantic import BaseSettings

CONTACT_MAIL = "luwenyi1991@gmail.com"
CONTACT = {
        "name": "Wenyi Lu",
        "url": "https://github.com/WenyiLULU/TrainingWeb",
        "email": CONTACT_MAIL,
    }
DESCRIPTION = """
The awesome Wenyi's API ! 🚀

## Users
You will be able to:
* Create users.
* Read users.
"""
LICENSE = {
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
TAGS_METADATA = [
    {
        "name": "default",
        "description": "Some basic routes.",
    },
    {
        "name": "Users",
        "description": "Operations with users. The login logic is also here.",
    },
]
VERSION = "1.0"


class Settings(BaseSettings):
    app_name: str = "Awesome App !"
    admin_email: str = CONTACT_MAIL


SETTINGS = Settings()
