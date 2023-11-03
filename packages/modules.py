from pyspark.sql.functions import col

def flatten_df(nested_df):
  stack = [((), nested_df)]
  columns = []

  while len(stack) > 0:
    parents, df = stack.pop()

    flat_cols = [
      col(".".join(parents + (c[0],))).alias("_".join(parents + (c[0],)))
      for c in df.dtypes
      if c[1][:6] != "struct"
  ]

    nested_cols = [
      c[0]
      for c in df.dtypes
      if c[1][:6] == "struct"
    ]

    columns.extend(flat_cols)

    for nested_col in nested_cols:
        projected_df = df.select(nested_col + ".*")
        stack.append((parents + (nested_col,), projected_df))

  return nested_df.select(columns)