from graphqlclient import GraphQLClient
import pandas as pd
import json
import time

API = 'https://api.github.com/graphql'
TOKEN = 'token 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'

args ={'after': None}

query =  """
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
    """



client = GraphQLClient(API)
client.inject_token(TOKEN)

df = pd.DataFrame()

for i in range(100):
    response = json.loads(client.execute(query= query, variables=args))
    print(response)
    args['after'] = response['data']['search']['pageInfo']['endCursor']

    data = response['data']['search']['edges']
    df = pd.concat([df, pd.json_normalize(data)], ignore_index=True)

    time.sleep(1)
    


# Renomeia as colunas do dataframe
df.columns = ['ID',
              'URL',
              'Name',
              'nameWithOwner',
              'Stargazers',
              'createdAt']

# df = df.drop(df.columns[-1], axis=1)

# Salva o dataframe em um arquivo CSV
df.to_csv('repositorios.csv', sep=';', index=False)