from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Simple in-memory storage for demonstration
items = {
    1: {"id": 1, "name": "Item 1", "description": "First item"},
    2: {"id": 2, "name": "Item 2", "description": "Second item"},
}


class ItemRequest(BaseModel):
    name: str
    description: Optional[str] = None


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to FastAPI Lab 1"}


@app.get("/items")
def get_items():
    """GET endpoint - Returns all items"""
    return {"items": list(items.values())}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """GET endpoint - Returns a specific item by ID"""
    if item_id in items:
        return items[item_id]
    return {"error": "Item not found"}


@app.post("/items")
def create_item(item: ItemRequest):
    """POST endpoint - Creates a new item"""
    new_id = max(items.keys()) + 1 if items else 1
    new_item = {"id": new_id, "name": item.name, "description": item.description}
    items[new_id] = new_item
    return {"status": "success", "item": new_item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """DELETE endpoint - Deletes an item by ID"""
    if item_id in items:
        deleted_item = items.pop(item_id)
        return {"status": "success", "message": f"Item {item_id} deleted", "item": deleted_item}
    return {"status": "error", "message": "Item not found"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
