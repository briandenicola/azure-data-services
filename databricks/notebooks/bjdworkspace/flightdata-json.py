# Databricks notebook source
try:
  dbutils.fs.unmount('/mnt/enterprise')
except:
  print("/mnt/enterprise not mounted")

# COMMAND ----------
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": dbutils.secrets.get(scope = "keyvault-screts", key = "client_id"),
           "fs.azure.account.oauth2.client.secret":  dbutils.secrets.get(scope = "keyvault-screts", key = "client_secret"),
           "fs.azure.account.oauth2.client.endpoint": dbutils.secrets.get(scope = "keyvault-screts", key = "oauth_endpiont")}

dbutils.fs.mount(
  source = "abfss://enterprise@bjddatalake001.dfs.core.windows.net/",
  mount_point = "/mnt/enterprise",
  extra_configs = configs)

# COMMAND ----------

df = spark.read.format("json").load("/mnt/enterprise/json/2015-summary.json")
df.createOrReplaceTempView("dfTable")

# COMMAND ----------

df.first()

# COMMAND ----------

df.selectExpr(
 "*",
 "(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry")\
 .show(2)
