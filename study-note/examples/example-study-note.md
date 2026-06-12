---
type: study
title: "Retrieval-Augmented Generation"
date: 2026-06-13
source: paper
status: complete
area: AI-ML
tags:
  - rag
  - retrieval
  - llm
---

# Retrieval-Augmented Generation

## Summary

- Retrieval-augmented generation, shortened to RAG, gives a language model access to an external store of documents at query time, so the model answers from retrieved evidence rather than from its training weights alone.
- The store is searched for passages relevant to the question, then those passages are placed in the prompt, so the model grounds its answer in current and specific material.
- RAG reduces fabricated answers and lets a system stay current without retraining, at the cost of a retrieval step that must itself be accurate.

## Detail

A RAG system has two stages that run on every query. The first stage retrieves, where the question is turned into a query against a document index, often a vector index built from embeddings, then the top passages are returned. The second stage generates, where those passages are concatenated into the prompt and the model writes an answer that cites or relies on them.

The quality of the answer depends as much on retrieval as on the model, because a model given the wrong passages will write a confident wrong answer. Retrieval quality rests on the chunking of documents, the embedding model and the similarity search, so a weak link in any of those three shows up as a weak answer.

RAG suits questions over a known corpus, for example internal documentation or a research library, where the answer should come from that corpus rather than from the model's general knowledge.

## Sources

- Lewis et al. (2020), Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## Connections

- [[Vector databases]]
- [[Embedding models]]
- [[Prompt construction]]
