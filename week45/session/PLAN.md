# Plan for dagen

- Lage en package med funksjoner for db connection and queries
- teste de underveis i main. 

---

**Oppsett for package**
```
session/
├─ main.py
├─ helper_db/
│  ├─ __init__.py
│  ├─ mysql_helper.py

```

**Innhold i mysql_helper.py**

```python
def create_connection() -> Optional[mysql.connector.connection.MySQLConnection]:
    pass

def execute_select() -> list[tuples]:
    pass

def execute_select_dict() -> List[Dict[str, Any]]:
    pass

def insert_one() -> Optional[int]:
    pass

def insert_many() -> bool:
    pass

def execute_query() -> bool:
    pass

# <- !! DENNE ER VIKTIG !! ->
def close_connection():
    pass
```

**Viktige imports**
```python
import mysql.connector
from mysql.connector import Error
#from typing import Optional -Her kommer vi til å importe mere, kommer under'
from typing import List, Tuple, Dict, Any, Optional # <- Her har vi de vi kommer til å bruke ->
```

---
