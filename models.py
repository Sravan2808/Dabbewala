from enum import Enum
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

#OrderStatus (Enum) -> preparing,picked_up,in_transit,delivered
class OrderStatus(Enum):
    preparing = "preparing"
    picked_up = "picked_up"
    in_transit = "in_transit"
    delivered = "delivered"

#Database table for Order
#id(primarykey)
#customer_name(str)
#delivery_address(str)
#items(str)
#Status(OrderStatus)
#created_at(datetime)
#updated_at(datetime)

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_name: str
    delivery_address: str
    items: str
    status: OrderStatus = Field(default=OrderStatus.preparing)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

#Schema for creating a new order
class OrderCreate(SQLModel):
    customer_name: str
    delivery_address: str
    items: str

#Schema for updating an order's status
class OrderUpdate(SQLModel):
    status: Optional[OrderStatus] = None
    delivery_address: Optional[str] = None


#StatusLog
#course_id
#old_status
#new_status
#changed_at(datetime)

class StatusLog(SQLModel):
    course_id: int
    old_status: OrderStatus
    new_status: OrderStatus
    changed_at: datetime