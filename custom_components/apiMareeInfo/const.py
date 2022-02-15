""" Constants """
import datetime

ISSUE_URL = "https://github.com/saniho/apiMareeInfo/issues"

DOMAIN = "apiMareeInfo"

# delai pour l'update http, toutes les 3 heures
SCAN_INTERVAL_http = datetime.timedelta(seconds=60 * 60 * 3)

__VERSION__ = "1.0.2.0"

__name__ = "apiMareeInfo"
