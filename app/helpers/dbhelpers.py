from sqlalchemy.inspection import inspect 

def serializeResult(model, result):
  if result:
      columns = [column.name for column in inspect(model).c]
      data = dict(zip(columns, result))
      return model(**data)
  else:
      return None

def serializeResults(model, results):
  if results:
      columns = [column.name for column in inspect(model).c]
      return [model(**dict(zip(columns, row))) for row in results]
  else:
      return []