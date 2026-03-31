# Contextual Memory Sync

An AI-driven service that bridges the gap between Slack, Notion, and GitHub by maintaining a unified contextual memory.

## Features
- **Unified Sync API**: Receive events from multiple sources.
- **Mock Context Retrieval**: Query the stored context for AI agent relevance.

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   python main.py
   ```
3. Sync context:
   ```bash
   curl -X POST "http://localhost:8000/sync" -H "Content-Type: application/json" -d '{"source": "github", "content": "Added implementation for memory sync."}'
   ```

---
Based on the proposal: [Notion Document](https://www.notion.so/AI-Feature-Contextual-Memory-Sync-33400b4dd98d818ca65fdcc0bf1683c0)
