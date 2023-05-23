# Project IV CUSTOMER BEHAVIOUR ANALYSIS & MARKETING CAMPAIGN

![seg](fig/seg.png)

# Customer Segmentation for SuperStore

## Description
The Customer Segmentation for SuperStore project aims to analyze customer data to launch a targeted campaign to increase customer recurrence and cart value. The dataset used for analysis is named SuperStore. The project utilizes SQL, Python, and Tableau to extract insights from the data and develop an effective marketing strategy.

In this project, we have obtained the RFM (Recency, Frequency, Monetary) scores from the provided data. RFM analysis is a powerful technique used to segment customers based on their purchase behavior and value. By leveraging RFM scores, we can identify different customer segments with varying levels of engagement and prioritize marketing efforts accordingly.

## Strategy
The strategy employed in this project involves the following steps:

1. **Data Retrieval**: Utilizing SQL, customer data is extracted from the SuperStore database. This data includes information such as purchase history, customer demographics, and order details.

2. **RFM Analysis**: Using Python, RFM scores are calculated for each customer based on the recency of their last purchase, the frequency of their purchases, and the monetary value of their transactions. These scores provide a quantitative measure of customer engagement and value.

3. **Segmentation**: The RFM scores are used to segment customers into distinct groups using appropriate clustering techniques. This segmentation helps identify customer segments with different characteristics and behaviors.

4. **Insights and Visualization**: Tableau is utilized to visualize the segmented customer groups, allowing for a clear understanding of their distribution and characteristics. Key insights are derived from the visualizations to guide the development of targeted marketing strategies.  

5. **Campaign Development**: Based on the insights gained from the segmentation analysis, a targeted marketing campaign is designed to increase customer recurrence and cart value. This may involve personalized recommendations, exclusive offers, or tailored messaging for each customer segment.

## Methodology
The following methodology will be followed to achieve the customer segmentation and campaign development:

1. **Data Extraction**: SQL queries are used to retrieve relevant customer data from the SuperStore database.

2. **RFM Calculation**: Using Python, the RFM scores are calculated by analyzing customer purchase history and transaction data.

3. **Customer Segmentation**: Clustering algorithms, such as K-means or hierarchical clustering, are applied to segment customers based on their RFM scores.

4. **Visualization**: Tableau is utilized to create visualizations that represent the customer segments, their characteristics, and distribution.
https://public.tableau.com/app/profile/leticia.martinez.iruela/viz/ProjectCopy/ProfitSalesCategorySegments?publish=yes


5. **Insights and Campaign Strategy**: Key insights are derived from the visualizations to develop targeted marketing strategies that aim to increase customer recurrence and cart value.

6. **Campaign Execution**: The designed marketing campaign is executed using appropriate channels and personalized approaches for each customer segment.

## Getting Started
To get started with the Customer Segmentation for SuperStore project, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies as specified in the `requirements.txt` file.
3. Set up the SQL environment and ensure connectivity to the SuperStore database.
4. Run the SQL queries to retrieve the required customer data.
5. Utilize Python to calculate the RFM scores and perform customer segmentation.
6. Use Tableau to visualize the segmented customer groups and derive insights.
7. Based on the insights, develop and execute a targeted marketing campaign to increase customer recurrence and cart value.

## Dataset
The SuperStore dataset used for this project should be accessible via the SQL environment. Make sure the necessary tables and data are available for the analysis. The dataset should include customer information, purchase history, order details, and transaction data.


## Conclusion
The Customer Segmentation for SuperStore project leverages RFM analysis and clustering techniques to identify distinct customer segments. By understanding customer behavior and preferences, targeted marketing strategies can be developed to increase customer recurrence and cart value. The combination of SQL, Python, and Tableau provides a comprehensive approach to extract insights, visualize results, and execute an effective marketing campaign. Some key concluions and key points are:

-Effective discount promotions have increased sales, but careful control and targeting are necessary to minimize losses.
-The Copiers, Accessories, and Phones subcategories in Technology are the most profitable.
-Customer loyalty has not significantly improved over the years.
-Target the New Customers, Promising, and Potential Loyalty segments in the campaign.
-Offer a 20% discount on the total basket for new customers to increase frequency and profit.
-Provide a 20% discount on the 4th purchase for promising customers to boost their Monetary Score.
-Offer a 20% discount on the 3rd purchase for potential loyalists to increase their Monetary Score.
-Analyze metrics regularly for insights to optimize campaign strategies.

For a detailed explanation of the project's methodologies, analysis steps, and results, please refer to the documentation and files provided in the repository.