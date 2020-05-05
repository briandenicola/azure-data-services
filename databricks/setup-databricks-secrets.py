# COMMAND ----------

# MAGIC %md
# MAGIC ``` apt install python-pip```

# COMMAND ----------

# MAGIC %md
# MAGIC ```pip install databricks-cli```

# COMMAND ----------

# MAGIC %md On the Databricks site, navigate to the user icon on the right-hand side, top, and click on "User setting".  Generate a token, capture to clipboard.

# COMMAND ----------

# MAGIC %md
# MAGIC ```databricks secrets create-scope --scope gws-blob-storage```

# COMMAND ----------

# MAGIC %md
# MAGIC ```databricks secrets put --scope gws-blob-storage --key storage-acct-key```

# COMMAND ----------

# MAGIC %md
# MAGIC ```databricks secrets list-scopes```

# COMMAND ----------

# MAGIC %md
# MAGIC ```databricks secrets create-scope --scope gws-adlsgen2-storage```

# COMMAND ----------

# MAGIC %md
# MAGIC ```databricks secrets put --scope gws-adlsgen2-storage --key client-id```

# COMMAND ----------

# MAGIC %md
# MAGIC ```databricks secrets put --scope gws-adlsgen2-storage --key client-secret```

# COMMAND ----------

# MAGIC %md
# MAGIC ```databricks secrets put --scope gws-adlsgen2-storage --key tenant-id```