-- Write a query to print the IDs of the owners who have at least 100 million worth of houses and own more than 1 house

-- select the buyer id and the added up prices
SELECT house.BUYER_ID, SUM(price.PRICE) AS TOTAL_WORTH
-- from the house table
FROM house
-- join the two tables based on the house ID's
LEFT JOIN price ON house.HOUSE_ID = price.HOUSE_ID
-- group by the owner
GROUP BY house.BUYER_ID
-- they have to have a total house price of over 100 and own more than 1 house
HAVING SUM(price.PRICE) >= 100 and COUNT(house.HOUSE_ID) > 1