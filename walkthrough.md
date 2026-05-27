# Assessment Walkthrough

## Overview

This repository contains submissions for both assessment tasks:
1. Product Scoping
2. Data Pipeline Development

The goal throughout both tasks was to build practical, maintainable, and realistic solutions rather than over-engineering unnecessarily complex systems.

---

# Task 1 - Product Scoping

## My Approach

For the product scoping task, I focused on understanding the actual operational problem rather than immediately thinking about advanced technical solutions.

The core issue identified was that marketing analysts currently spend significant time manually gathering and combining data from multiple platforms to answer recurring performance-related questions.

This process is:
- Slow
- Inconsistent
- Difficult to scale
- Dependent on individual team members

---

## Product Decisions

I intentionally scoped the first version of the product narrowly to keep it practical and achievable.

The v1 solution focuses on:
- Unified marketing performance visibility
- KPI standardization
- Weekly performance monitoring
- Actionable insights
- Faster reporting workflows

---

## Why I Excluded Advanced Features

I deliberately excluded:
- Predictive analytics
- AI-generated recommendations
- Real-time streaming
- Campaign editing functionality

These features would significantly increase implementation complexity and operational overhead without first validating the usefulness of the core workflow.

My priority was to design a tool that analysts could adopt quickly and trust easily.

---

## Design Thinking

The dashboard wireframe and architecture diagram were designed to prioritize:
- Simplicity
- Clarity
- Fast insight generation
- Minimal disruption to existing workflows

The solution integrates around existing tools rather than replacing them.

---

# Task 2 - Data Pipeline

## API Choice

I selected the CoinGecko API because:
- It provides structured financial data
- No API key is required
- The data format is suitable for transformation and analytics
- It allows meaningful derived metrics to be created

---

## Pipeline Design

The pipeline was structured into modular components:
- Data fetching
- Data transformation
- BigQuery loading

This separation improves readability and maintainability.

---

## Data Transformation Decisions

I created additional derived fields such as:
- market_status
- volume_to_marketcap_ratio

These fields add analytical value beyond the raw API response.

---

## BigQuery Integration

BigQuery was selected because it aligns directly with the assessment requirements and demonstrates cloud-based analytical storage capabilities.

The pipeline automatically loads transformed data into BigQuery and allows SQL-based analysis.

---

## Production Thinking

If deployed in production, I would:
- Schedule the pipeline using Airflow or Cloud Scheduler
- Add monitoring and alerting
- Implement retry mechanisms
- Use partitioned tables for scalability
- Add incremental loading strategies

---

# Final Thoughts

Across both tasks, my primary goal was to build solutions that are:
- Practical
- Maintainable
- Clearly scoped
- Easy to explain
- Focused on solving the actual business problem

Rather than maximizing complexity, I focused on delivering clean and reliable solutions with clear reasoning behind each decision.
