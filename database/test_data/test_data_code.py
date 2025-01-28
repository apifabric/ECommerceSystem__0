import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not -1216121572446160732 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer1 = Customer(name="Alice", credit_limit=1000, balance=300)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1216121572446160732)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5186914362836266326 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer2 = Customer(name="Bob", credit_limit=1500, balance=700)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5186914362836266326)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -379992576434491713 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer3 = Customer(name="Charlie", credit_limit=2000, balance=1000)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-379992576434491713)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3371162970532209256 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer4 = Customer(name="David", credit_limit=2500, balance=0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3371162970532209256)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6216244231695518969 in succeeded_hashes:  # avoid duplicate inserts
            instance = product1 = Product(name="Laptop", unit_price=1200)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6216244231695518969)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1527731372366132813 in succeeded_hashes:  # avoid duplicate inserts
            instance = product2 = Product(name="Monitor", unit_price=300)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1527731372366132813)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7500605576979855571 in succeeded_hashes:  # avoid duplicate inserts
            instance = product3 = Product(name="Mouse", unit_price=50)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7500605576979855571)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5776840187986575421 in succeeded_hashes:  # avoid duplicate inserts
            instance = product4 = Product(name="Keyboard", unit_price=70)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5776840187986575421)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 9057406443082044415 in succeeded_hashes:  # avoid duplicate inserts
            instance = order1 = Order(customer_id=1, date_shipped=None, amount_total=0, notes="First order")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(9057406443082044415)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5031242693719779665 in succeeded_hashes:  # avoid duplicate inserts
            instance = order2 = Order(customer_id=2, date_shipped=date(2023, 5, 10), amount_total=0, notes="Second order")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5031242693719779665)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6954008902494709177 in succeeded_hashes:  # avoid duplicate inserts
            instance = order3 = Order(customer_id=3, date_shipped=None, amount_total=0, notes="Third order")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6954008902494709177)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8511914262119715134 in succeeded_hashes:  # avoid duplicate inserts
            instance = order4 = Order(customer_id=4, date_shipped=date(2023, 8, 15), amount_total=0, notes="Fourth order")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8511914262119715134)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8834561628660812639 in succeeded_hashes:  # avoid duplicate inserts
            instance = item1 = Item(order_id=1, product_id=1, quantity=1, unit_price=1200, amount=1200)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8834561628660812639)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2461408075079766649 in succeeded_hashes:  # avoid duplicate inserts
            instance = item2 = Item(order_id=2, product_id=2, quantity=2, unit_price=300, amount=600)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2461408075079766649)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3130382929527714873 in succeeded_hashes:  # avoid duplicate inserts
            instance = item3 = Item(order_id=3, product_id=3, quantity=5, unit_price=50, amount=250)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3130382929527714873)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1892604841308150961 in succeeded_hashes:  # avoid duplicate inserts
            instance = item4 = Item(order_id=4, product_id=4, quantity=7, unit_price=70, amount=490)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1892604841308150961)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
