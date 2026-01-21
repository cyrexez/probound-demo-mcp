Project Thesis: Standardizing Agentic I/O
This repository explores the transition from traditional REST-based orchestration to the Model Context Protocol (MCP). By decoupling the tool execution layer from the API logic using MCP, we eliminate network-induced failures and provide a standardized interface for LLM-agnostic tool discovery.

Performance Benchmark (MCP vs. Standard)

Reliability: Improved from 85% to 100% success rate.

Throughput: Sustained 182.1 RPS with 1,000 concurrent users.

Architecture: Shifted from high-latency external HTTP calls to local JSON-RPC over stdio for integration tasks.
