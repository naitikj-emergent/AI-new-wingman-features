import hashlib
import os
from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- Mock LLM and Vector Store Implementation ---
class MockMemoryStore:
    def __init__(self):
        self.memory = []

    def add_entry(self, source: str, content: str, summary: str):
        entry = {
            "id": hashlib.md5(content.encode()).hexdigest(),
            "timestamp": datetime.now().isoformat(),
            "source": source,
            "original_content": content,
            "summary": summary
        }
        self.memory.append(entry)
        return entry

    def query(self, query_text: str):
        # In a real app, this would use vector embeddings
        return [m for m in self.memory if query_text.lower() in m['summary'].lower()]

memory_store = MockMemoryStore()

# --- FastAPI App ---
app = FastAPI(title="Contextual Memory Sync API")

class EventData(BaseModel):
    source: str  # e.g., 'slack', 'notion', 'github'
    content: str

@app.post("/sync")
def sync_context(data: EventData):
    """
    Receives content from external tools, summarizes it, and stores it in memory.
    """
    # Mock summarization logic (Replace with LLM call in production)
    summary = f"Context from {data.source}: {data.content[:100]}..."
    
    entry = memory_store.add_entry(data.source, data.content, summary)
    return {"status": "success", "entry_id": entry["id"], "summary": summary}

@app.get("/context")
def get_context(query: str):
    """
    Retrieves relevant context based on a query.
    """
    results = memory_store.query(query)
    if not results:
        return {"message": "No relevant context found."}
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
