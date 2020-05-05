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

try:
  dbutils.fs.mount(
    source = "abfss://enterprise@bjddatalake001.dfs.core.windows.net/",
    mount_point = "/mnt/enterprise",
    extra_configs = configs)
except:
  print("Cout not mount /mnt/enterprise")

# COMMAND ----------

flightData2015 = spark\
  .read\
  .option("inferSchema", "true")\
  .option("header", "true")\
  .csv("/mnt/enterprise/flightdata/2015-summary.csv")


# COMMAND ----------

flightData2015.sort("count").explain()

# COMMAND ----------

from pyspark.sql.functions import max

flightData2015.select(max("count")).take(1)

# COMMAND ----------

from pyspark.sql.functions import desc

flightData2015\
 .groupBy("DEST_COUNTRY_NAME")\
 .sum("count")\
 .withColumnRenamed("sum(count)", "destination_total")\
 .sort(desc("destination_total"))\
 .limit(5)\
 .show()