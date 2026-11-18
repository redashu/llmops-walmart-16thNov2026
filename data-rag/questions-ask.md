# RAG Testing Questions for Walmart Retail Customer Support

## Overview

Excellent. Since you've created the index through Manage RAG in Microsoft Foundry, let's test whether retrieval is working correctly.

For our Walmart Retail Customer Support dataset, use these questions.

---

## 1. Basic Retrieval Questions

| Question | What it tests |
|----------|---------------|
| What should a customer do if their order is delayed? | Order tracking |
| What is the process for returning an item? | Return policy |
| How are refunds handled after a return? | Refund policy |
| What should a customer do if they receive a damaged item? | Damaged items |
| What should a customer do if delivery is unsuccessful? | Delivery policy |
| How should payment failures be handled? | Payment issues |

---

## 2. Contextual Questions

These are more useful for demonstrating RAG to students.

1. My order is delayed, and the tracking status has not changed. What should I do?
2. I received a damaged product. Should I return it or request a replacement?
3. My refund has not arrived after returning an item. What steps should I take?
4. My payment was deducted, but the order was not confirmed. How should I proceed?
5. The delivery agent marked my order as delivered, but I haven't received it. What should I do?

---

## 3. Multi-Document Retrieval Questions

These test whether retrieval can find relevant information across multiple documents.

1. My order was delayed and then arrived damaged. Explain the steps I should follow.
2. If a customer returns a damaged item, what should happen next, and how is the refund handled?
3. My payment was deducted, the order was cancelled, and I haven't received a refund. Explain the resolution process.

---

## 4. Grounding and Hallucination Tests

These are particularly important in enterprise RAG.

| Test question | Expected behavior |
|---------------|-------------------|
| What is the exact Walmart refund guarantee in 2 hours? | Should not invent a guarantee |
| Can I return a product after 500 days? | Should not invent a return period |
| What is the phone number of the Walmart CEO? | Should say the knowledge base doesn't provide it |
| What is Walmart's official international shipping policy? | Should not assume unsupported policy details |

---

## 5. What to Observe During Testing

For every question, inspect:

- **Retrieved chunks**: Did it retrieve the correct document sections?
- **Relevance**: Are the retrieved chunks actually related to the question?
- **Grounded answer**: Does the response use retrieved content?
- **Citations**: Can you trace the answer to the source documents?
- **Unknown questions**: Does it admit when information is missing?

---

## Recommended Live Demo Sequence

Use these five questions in this order:

1. "What should a customer do if their order is delayed?"
2. "My order is delayed and arrived damaged. What should I do?"
3. "My payment was deducted, but my order was cancelled. How do I resolve this?"
4. "What is the exact refund guarantee in 2 hours?"
5. "Explain the relationship between order delays, returns, and refunds."

This demonstrates basic retrieval, contextual retrieval, multi-document retrieval, hallucination control, and synthesis.