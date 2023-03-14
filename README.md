# Laboratorio02

### query que busca os 1000 repositórios mais populares em Java:

```
query ($after: String) {
  search(query: "stars:>100 language:Java", type: REPOSITORY, first: 10, after: $after) {
    pageInfo {
      hasPreviousPage
      hasNextPage
      startCursor
      endCursor
    }
    edges {
      node {
        ... on Repository {
          id
          url
          name
          nameWithOwner
          stargazerCount
          createdAt
        }
      }
    }
  }
}
```
