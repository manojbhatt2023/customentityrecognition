import logging
from MYRASAMODEL import EntityExtract

# queries = [
#     "I need a sales report by chain and fiscal quarter.",
#     "Generate a sales report by product category and fiscal quarter.",
#     "Show me the purchase report for a specific product line and fiscal month.",
#     "Provide a profit summary by product group and fiscal year.",
#     "I need a sales report for a particular product and fiscal week.",
#     "Generate a purchase report, including profit, by product category and fiscal year.",
#     "Show me the profit details for a specific product line and fiscal quarter.",
#     "Provide a sales and purchase report by product group and fiscal month.",
#     "I'm interested in a profit report for a particular product and fiscal year.",
#     "Give me a sales and purchase summary by product category and fiscal quarter.",
#     "Show me the purchase report for a specific region and fiscal month.",
#     "Can you provide a profit summary by district and fiscal year?",
#     "Generate a purchase report, including profit, by area and fiscal year.",
#     "Show me the profit details by region and fiscal week.",
#     "Provide a sales and purchase report by district and fiscal month.",
#     "I'm interested in a profit report by chain and fiscal year.",
#     "Give me a sales and purchase summary by area and fiscal quarter.",
#     "Generate a sales report by region and fiscal week.",
#     "Show me the purchase report for a specific district and fiscal year.",
#     "Can you provide a profit summary by chain and fiscal quarter?",
#     "I need a sales report by area and fiscal month.",
#     "Generate a purchase report, including profit, by region and fiscal year.",
#     "Show me the profit details for a specific chain and fiscal week.",
#     "Provide a sales and purchase report by district and fiscal quarter.",
#     "I'm interested in a profit report for a particular area and fiscal year.",
#     "Give me a sales and purchase summary by region and fiscal month.",
#     "Generate a sales report by chain and fiscal quarter.",
#     "Show me the purchase report for a specific area and fiscal week.",
#     "Can you provide a profit summary by region and fiscal year?",
#     "I need a sales report by district and fiscal month.",
#     "Generate a purchase report, including profit, by chain and fiscal quarter.",
#     "Show me the profit details for a specific region and fiscal week.",
#     "Provide a sales and purchase report by area and fiscal year.",
#     "I'm interested in a profit report by district and fiscal quarter.",
#     "Give me a sales and purchase summary by chain and fiscal month.",
#     "Generate a sales report by region and fiscal quarter.",
#     "Show me the purchase report for a specific district and fiscal week.",
#     "Can you provide a profit summary by chain and fiscal year?",
#     "I need a sales report by area and fiscal month.",
#     "Generate a purchase report, including profit, by region and fiscal quarter.",
#     "Show me the profit details for a specific chain and fiscal week.",
#     "Provide a sales and purchase report by district and fiscal year.",
#     "I'm interested in a profit report for a particular area and fiscal quarter.",
#     "Give me a sales and purchase summary by region and fiscal month.",
#     "Generate a sales report by chain and fiscal quarter.",
#     "Show me the purchase report for a specific area and fiscal week.",
#     "Can you provide a profit summary by district and fiscal year?",
#     "I need a sales report by region and fiscal month.",
#     "Generate a purchase report, including profit, by chain and fiscal quarter."
# ]
# queries=[
#     "Generate a report on sales broken down by chain and fiscal quarter.",
#     "Show me the purchase report categorized by product category and fiscal quarter.",
#     "Provide a summary of profits based on product line and fiscal month.",
#     "I'm interested in a sales report for a specific product and fiscal week.",
#     "Generate a comprehensive purchase report, including profit, for product category and fiscal year.",
#     "Display the profit details associated with a particular product line and fiscal quarter.",
#     "Give me a consolidated sales and purchase report categorized by product group and fiscal week.",
#     "Provide insights into profits for a specific product and fiscal month.",
#     "Share a detailed sales and purchase report categorized by district and fiscal year.",
#     "I'm keen on understanding the profit scenario for a particular area and fiscal quarter.",
#     "Present a sales and purchase summary categorized by region and fiscal month.",
#     "Generate a sales report categorized by chain and fiscal quarter.",
#     "Show me the purchase report for a specific area and fiscal week, including profit details.",
#     "Can you provide a comprehensive profit summary based on district and fiscal year?",
#     "I need a detailed sales report categorized by region and fiscal month.",
#     "Generate a purchase report, including profit, based on chain and fiscal week.",
#     "Show me the profit details for a specific district and fiscal quarter.",
#     "Provide a sales and purchase report for a particular area and fiscal year.",
#     "I'm interested in a profit report categorized by chain and fiscal month.",
#     "Give me a sales and purchase summary based on region and fiscal week."
# ]
queries=["Generate a comprehensive report detailing the purchase trends, including profit margins, across various product categories and fiscal years",
         "Show me a detailed breakdown of profit metrics, considering both product and district parameters, for the current fiscal month.",
        "I need an extensive sales report, incorporating data from specific product groups and geographical areas, for the entire fiscal year.",
        "Generate a sophisticated purchase report, inclusive of profit analysis, based on a hierarchical view involving chains, regions, and fiscal quarters.",
        "Provide a nuanced overview of profit details for a targeted product category, taking into account the variations across different districts and fiscal weeks."       
         ]
extractedEntities=[]
for index, query in enumerate(queries, 1):
    EntityList=EntityExtract.get_entities(query)
    extractedEntities.append(EntityList)

for index, query in enumerate(extractedEntities,0):
    print(f"Query{index}:{queries[index]}")
    print(extractedEntities[index],"\n")

