# Neo4j README

This README shows basic Cypher commands for common Neo4j operations:

- Create a node
- Fetch a node
- Create a relationship between two nodes
- Update a node
- Delete a relationship
- Delete a node
- Delete a node with `DETACH DELETE`

## 1. Create a Node

A node represents an entity such as a person, student, city, or product.

```cypher
CREATE (n:Person {name: 'Alice', age: 25, city: 'Kolkata'})
RETURN n;
```

### Explanation
- `CREATE` creates a new node.
- `:Person` is the label.
- `{name: 'Alice', age: 25, city: 'Kolkata'}` are properties.

## 2. Fetch a Node

Use `MATCH` to retrieve nodes.

```cypher
MATCH (n:Person {name: 'Alice'})
RETURN n;
```

### Fetch All Person Nodes

```cypher
MATCH (n:Person)
RETURN n;
```

## 3. Create a Relationship Between Two Nodes

First create two nodes if they do not already exist.

```cypher
CREATE (a:Person {name: 'Alice'})
CREATE (b:Person {name: 'Bob'})
RETURN a, b;
```

Now create a relationship between them.

```cypher
MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
CREATE (a)-[:FRIEND_OF]->(b)
RETURN a, b;
```

### Explanation
- `MATCH` finds the two existing nodes.
- `CREATE (a)-[:FRIEND_OF]->(b)` creates a directed relationship.

## 4. Update a Node

Use `SET` to update existing properties or add new properties.

```cypher
MATCH (n:Person {name: 'Alice'})
SET n.age = 26, n.city = 'Delhi'
RETURN n;
```

### Add a New Property

```cypher
MATCH (n:Person {name: 'Alice'})
SET n.email = 'alice@example.com'
RETURN n;
```

## 5. Delete a Relationship

Use `MATCH` with the relationship pattern and then `DELETE`.

```cypher
MATCH (a:Person {name: 'Alice'})-[r:FRIEND_OF]->(b:Person {name: 'Bob'})
DELETE r;
```

### Explanation
- `r` is the relationship variable.
- `DELETE r` removes only the relationship, not the nodes.

## 6. Delete a Node

A node can be deleted only if it has no relationships.

```cypher
MATCH (n:Person {name: 'Bob'})
DELETE n;
```

### Important
If the node still has relationships, Neo4j will throw an error.

## 7. Delete a Node with DETACH DELETE

Use `DETACH DELETE` when the node has relationships.

```cypher
MATCH (n:Person {name: 'Alice'})
DETACH DELETE n;
```

### Explanation
- `DETACH DELETE` removes the node and all connected relationships.

## 8. Full Example Workflow

```cypher
CREATE (a:Person {name: 'Alice', age: 25})
CREATE (b:Person {name: 'Bob', age: 27});

MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
CREATE (a)-[:FRIEND_OF]->(b);

MATCH (n:Person {name: 'Alice'})
RETURN n;

MATCH (n:Person {name: 'Alice'})
SET n.age = 26
RETURN n;

MATCH (a:Person {name: 'Alice'})-[r:FRIEND_OF]->(b:Person {name: 'Bob'})
DELETE r;

MATCH (n:Person {name: 'Bob'})
DELETE n;

MATCH (n:Person {name: 'Alice'})
DETACH DELETE n;
```

## 9. Quick Summary Table

| Operation | Cypher Command |
|---|---|
| Create node | `CREATE (n:Person {name:'Alice'})` |
| Fetch node | `MATCH (n:Person {name:'Alice'}) RETURN n` |
| Create relationship | `MATCH (a),(b) CREATE (a)-[:REL]->(b)` |
| Update node | `MATCH (n) SET n.age = 30` |
| Delete relationship | `MATCH ()-[r:REL]->() DELETE r` |
| Delete node | `MATCH (n) DELETE n` |
| Delete node with relationships | `MATCH (n) DETACH DELETE n` |

## 10. Notes

- `CREATE` adds new data.
- `MATCH` searches existing data.
- `SET` updates properties.
- `DELETE` removes nodes or relationships.
- `DETACH DELETE` is useful when a node is connected to other nodes.

This file can be used as a beginner-friendly Neo4j reference for basic CRUD and relationship operations.
