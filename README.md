# Landlords
In this project we studied the real estate rental market of the four major cities in Saudi Arabia: Jeddah, Riyadh, Alkhobar and Dammam. We explored the relationships of prices with other features. The dataset used is found on kaggle <a href = "https://www.kaggle.com/datasets/lama122/saudi-arabia-real-estate-aqar">Saudi Arabia Real Estate (AQAR) dataset</a> It was collected and scrapped from <a href ="https://sa.aqar.fm">Aqar.fm</a>
This report will help officials from the Ministry of Housing understand the current rental landscape for the average consumer (families and singles) in each city. 
A report of the initial <a href="https://jainlo.github.io/Landlords"></a>[data exploration](./report.html)

## Main features discussed in our report
- City: location of the house
- Price: monthly rent (by building an assumption and performing needed calculations)
- Front: which way is the house front facing; north, west, east, south, south-east, south-west, north-eat and north-west
- Districts: which district the house is located in
## Main issues
After exploring the dataset we found significant issues with it
- Not many observations (total of 1500 units after deleting duplicates)
- District distribution is not fair
- Price periods are ambiguous 
## Solutions
- Combining the dataset with additional datasets to get more complete answers to our questions
- Build an assumption for the price period based on research done on the website "aqar"
## Main questions
- Which feature is more prominent in expensive real estate?
- Is there a preferred front?
- Is there a front that is more expensive?
- Which side of each city is considered more expensive?
## Key conclusions
- Real estate has higher prices in Jeddah compared to Riyadh, Dammam and Alkhobar (on the date of data collection)
- The features that are more prominent in expensive real estate in order are:
    1. house includes a driver's room
    2. house has a frontyard
    3. house has a garage
- The most expensive front out of the 4 main directions is "East", while "North-east" is the most expensive overall


