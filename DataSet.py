from pyspark.shell import spark
from pyspark.sql.functions import explode, col

'''
    В описании задания было указано ,что свои вопросы и догадки я могу указывать в комментариях к коду:
        Как я понял из документации, в pyspark.sql.DataFrame нет заготовки тестового датафрейма.
        Так что я создал его сам, как было указано в задании.
        Надеюсь, что понял правильно.
        
    А код на моем компьютере не запускается из-за проблем в Java(?), поэтому я проверял его в Google Colab.
    Хотя ниже тот же код, что и в колабе, приложу ссылку и на блокнот - https://colab.research.google.com/drive/1zMcTQ2gyw8OGzt72JXkMLyGI7S5Uyils?usp=sharing
'''

def get_product_categories(products_df, categories_df):
    exploded_df = categories_df.select(col("product_id"), explode(col("categories")).alias("category"))

    # объединение по left join
    result_df = products_df.join(exploded_df, products_df["product_id"] == exploded_df["product_id"], "left")
    result_df = result_df.select(products_df["product_name"], exploded_df["category"])

    return result_df

# Создание датафреймов для продукта и категории
products_df = spark.createDataFrame([(1, "Product A"), (2, "Product B"), (3, "Product C")], ["product_id", "product_name"])
categories_df = spark.createDataFrame([(1, ["Category A", "Category B"]), (2, ["Category B", "Category C"]), (4, ["Category D"])], ["product_id", "categories"])

# получение объединения
result_df = get_product_categories(products_df, categories_df)
result_df.show()