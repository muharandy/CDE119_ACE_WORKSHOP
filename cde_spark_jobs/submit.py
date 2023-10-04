cde job create \
  --name fajarmuharandy-cde-job \
  --type spark \
  --mount-1-resource fajar-resource \
  --application-file cdejobjar_2.12-1.0.jar \
  --conf spark.sql.shuffle.partitions=10 \
  --executor-cores 2 \
  --executor-memory 2g


cde job create \
  --name admin-cde-job \
  --type spark \
  --mount-1-resource admin-resource \
  --application-file cdejobjar_2.12-1.0.jar \
  --conf spark.sql.shuffle.partitions=10 \
  --executor-cores 2 \
  --executor-memory 2g


cde job create \
  --name admin-iceberg-job \
  --type spark \
  --mount-1-resource admin-resource \
  --application-file cdejobjar_2.12-1.0.jar \
  --conf spark.sql.shuffle.partitions=10 \
  --executor-cores 2 \
  --executor-memory 2g


cde job create \
  --name admin-iceberg-job \
  --type spark \
  --mount-1-resource fajar-resource \
  --application-file 02_PySpark_Iceberg.py \
  --conf spark.sql.shuffle.partitions=10 \
  --executor-cores 2 \
  --executor-memory 2g