# Databricks notebook source
# MAGIC %sh
# MAGIC nslookup bjddatalake002.dfs.core.windows.net

# COMMAND ----------
spark.read.csv("abfss://data@bjddatalake002.dfs.core.windows.net/cdc.csv").collect()

# COMMAND ----------
configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class":   spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

dbutils.fs.mount(
  source = "abfss://data@bjddatalake002.dfs.core.windows.net/",
  mount_point = "/mnt/enterprise",
  extra_configs = configs)

# COMMAND ----------
dbutils.fs.ls("/mnt/enterprise") 

# COMMAND ----------
dbutils.fs.unmount("/mnt/enterprise")
