import logging
from logic_bank.logic_bank import DeclareRule, Rule, LogicBank
from database.models import *
from decimal import Decimal
from datetime import date, datetime

log = logging.getLogger(__name__)

def declare_logic():
    """
        declare_logic - declare rules
        this function is called from logic/declare_logic.py
    """
    log.info("declare_logic - active rules")
    
    # Exported Rules:
    # Customer Balance Constraint 
    # The Customer's balance is less than the credit limit
    Rule.constraint(validate=Customer,
                    as_condition=lambda row: row.balance <= row.credit_limit,
                    error_msg="Customer's balance ({row.balance}) exceeds credit limit ({row.credit_limit})")
    
    # Customer Balance Sum 
    # The Customer's balance is the sum of the Order amount_total where date_shipped is null.
    Rule.sum(derive=Customer.balance, as_sum_of=Order.amount_total, where=lambda row: row.date_shipped is None)
    
    # Order Amount Total Sum 
    # The Order's amount_total is the sum of the Item amount.
    Rule.sum(derive=Order.amount_total, as_sum_of=Item.amount)
    
    # Item Amount Formula 
    # The Item amount is the quantity * unit_price.
    Rule.formula(derive=Item.amount, as_expression=lambda row: row.quantity * row.unit_price)
    
    # Item Unit Price Copy 
    # The Item unit_price is copied from the Product unit_price.
    Rule.copy(derive=Item.unit_price, from_parent=Product.unit_price)
    