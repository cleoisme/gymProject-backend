## Introduction

- **What is System Design?**
  - Crafting architecture and components
  - Balancing trade-offs: Informed decisions between conflicting elements like speed vs. storage, or consistency vs. availability.
- **Why it Matters?**
  - Efficiency and Scalability: A well-designed system effectively utilizes resources and can scale to accommodate growth without performance degradation.
  - Reliability and Robustness: Ensures that the system can handle and recover from faults gracefully, maintaining continuous operation and data integrity.

---

## System Design Fundamentals

- **Performance Metrics**
  - Latency
  - Throughput
  - Bandwidth

---

## System Design Fundamentals

- **Scalability**
  - Vertical scaling: Adding more resources to the existing nodes (like CPU or memory)
  - Horizontal scaling: Adding more nodes to the system or network.

---

## System Design Fundamentals

- **Reliability & Fault Tolerance**
  - Redundancy, Failover mechanisms: Techniques that involve duplicating critical components or functions of a system to increase reliability and availability.

---

## System Design Fundamentals

- **Consistency Models**
  - Strong
  - Weak
  - Eventual

---

## Deep Dive: Key System Components

1. **Databases**
   - SQL vs NoSQL, Sharding, Replication

---

## Deep Dive: Key System Components

2. **Caching**
   - Cache Aside: Data is loaded into the cache only when necessary
   - Write Through: Write operation is done simultaneously to the cache and the database
   - Write Back: Data is initially written only to the cache and then written to the data store after

---

## Deep Dive: Key System Components

3. **Load Balancing**
   - Algorithms, Session Persistence

---

## Deep Dive: Key System Components

4. **API Design**
   - REST
   - GraphQL

---

```
query {
  user(id: "1") {
    username
    posts(limit: 3) {
      title
      comments {
        content
        author {
          username
        }
      }
    }
  }
}
```

---

## Deep Dive: Key System Components

5. **Message Queues**
   - SQS
     - DLQ
     - FIFO Queue
     - Standard queues: Offers maximum throughput, best-effort ordering, and at-least-once delivery.
   - Kafka
     - Pub Sub Model
     - Topics and Partitions: Messages are categorized into topics, and topics are divided into partitions for parallel processing.
     - Fault-Tolerant: Data is replicated, and nodes can be added to the Kafka cluster to prevent data loss.

---

## Deep Dive: Key System Components

6. **Proxies**
   - Reverse Proxy: Secure, protect client
   - Forward Proxy: load balancing, cdn, prevent DDOS, example: Nginx

---

## Design Considerations

- **Trade-offs**
  - CAP theorem: Partition Tolerance, Consistency, Availability
  - PACELC theorem: Partition Tolerance, Consistency, Availability, Latency, Consistency

---

## Design Considerations

- **Data Handling**
  - Data Partitioning
  - Indexing

---

## Design Considerations

- **Security**
  - Authentication
    - 2FA
    - Password
    - Tokens
  - Authorization
    - Role-based access control(RBAC)
    - Attribute-based access control(ABAC)
    - Discretionary access control(DAC)
    - Mandatory access control (MAC)
  - Data Encryption
    - Symmetric encryption
    - Asymmetric encryption
    - Hashing

---

## Design Considerations

- **Monitoring and Logging**
  - Tools
  - Metrics

---

## Practical Approach to System Design Interview

- **Gathering Requirements**
  - Functional
  - Non-Functional: Performance, Security, scalability
  - Results: lists out features and Capacity Estimation

---

## Practical Approach to System Design

- **High-Level Design**

  - API Design
    - protocol
    - input & output schema
  - High Level Design Diagram
    - Load balancer/API Gateway
    - Service
    - Data Storage layer
  - Data Model Schema

  Avoid too much detail!!

---

## Practical Approach to System Design

- **Detailed Component Design**
  - Deep dive into each component(work with interviewer)
    - Ask questions
    - Give at least 2 options
      - Example: Too much load on Read APIs
        - Option 1: Batch APIs
        - Option 2: Change from SQL to NoSQL to handle the load

---

## Practical Approach to System Design

- **Q&A**

---

## Case Studies - Twitter

- Functional Requirements:
  - User Management: Sign-up, sign-in, and profile management.
  - Tweeting: Posting a new tweet, deleting a tweet, and tweet feed generation.
  - Following: Follow/unfollow users.
    Feed: Viewing the aggregated tweets from all followed users plus the user's own tweets.

---

## Case Studies - Twitter

- Non-Functional Requirements:
  - Scalability: Handle a massive number of requests and data.
  - High Availability: Ensure the system is always functional.
  - Consistency: Ensure that the timeline is as up-to-date as possible.
  - Low Latency: Serving feeds should be fast.

---

## Case Studies - Twitter

- High-Level Architecture:
  - Components:
    - Web Servers: Handle HTTP requests and responses.
    - Application Servers: Host the business logic, including user management, tweet management, and feed generation.
    - Database Servers: Store user data, tweets, and relationships (followers/following).
    - Cache Servers: Cache frequently accessed data such as hot tweets or user's timeline.
    - Queue Systems: Handle high throughput and spikes in load, especially for actions like delivering tweets to followers.

---

## Case Studies - Twitter

- Data Storage:
  - User Information: Stored in databases like MySQL.
  - Tweets: Each tweet can be stored with a unique Tweet ID, user ID of the poster, and timestamp, among other metadata.
  - Followers/Following Data: Many-to-many relationship data typically stored in a table with user and follower IDs.

---

## Case Studies - Twitter

- Detailed Component Design:
  - Tweeting Service
  - Timeline Service
  - User Service
- Data Model Considerations:
  - User Table
  - Tweet Table
  - Follow Table

---

## Case Studies - Twitter

- Sharding: Distribute data across multiple databases to improve performance and increase storage.
- Caching: Use cache for read-heavy operations, especially for serving the timeline.
- Load Balancing: Distribute load evenly across servers and prevent any single point of failure.
- Asynchronous Processing: Use queues to handle tasks like sending notifications or email digests.

---

## Case Studies - Twitter

- Logging: Keeping logs of system activities for debugging and analysis.
- Monitoring: Real-time monitoring of the system to catch and address any issues early.
- Data Backups: Regularly backing up data to prevent loss in case of system failures.

---

## Case Studies - Twitter

- Handling Viral Tweets: Ensuring that the system can handle viral content efficiently without degradation of service.
- Data Consistency: Balancing between strong and eventual consistency especially in the context of a distributed system.
- Security: Protecting user data and preventing unauthorized access.
