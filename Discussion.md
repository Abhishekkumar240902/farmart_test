# **Log Extraction from Large Files (1TB)**

## **Solutions Considered**
### 1️⃣ **Loading Entire File into Memory**
- ✅ Fast lookup.
- ❌ Not feasible for large files (1TB+).

### 2️⃣ **Database Indexing (Elasticsearch, SQLite)**
- ✅ Fast indexed search.
- ❌ Requires extra storage and setup.

### 3️⃣ **Multi-threaded Processing**
- ✅ Can speed up extraction.
- ❌ Complex file pointer management.

### 4️⃣ **Line-by-Line Streaming (Final Solution)**
- ✅ Minimal memory usage.
- ✅ Simple and scalable.
- ✅ Works efficiently on large files.

## **Final Solution Summary**
The best approach is **line-by-line streaming** to extract logs **without loading the entire file** into memory.

