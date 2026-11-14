Program 1


from pyspark.sql import SparkSession
from pyspark.sql.types import StringType

# Step 1: Create Spark Session
spark = SparkSession.builder \
    .appName("Count Non String Columns") \
    .getOrCreate()

# Step 2: Create Sample Data
data = [
    (1, "Abinash", 25, 45000.50),
    (2, "Arun", 22, 35000.00),
    (3, "Kumar", 24, 40000.00)
]

columns = ["ID", "Name", "Age", "Salary"]

# Step 3: Create DataFrame
df = spark.createDataFrame(data, columns)

# Step 4: Display DataFrame
df.show()

# Step 5: Display Schema
df.printSchema()

# Step 6: Count Non-String Columns
count = sum(
    1 for field in df.schema.fields
    if not isinstance(field.dataType, StringType)
)

# Step 7: Print Result
print("Number of columns that are not strings:", count)
