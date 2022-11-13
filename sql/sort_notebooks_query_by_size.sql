WITH rounded AS (
	SELECT 
		CEILING(width / 5) * 5 AS width, 
		CEILING(depth / 5) * 5 AS depth,
		CEILING(height / 5) * 5 AS height
	FROM notebooks_notebook
)
SELECT 
	width, depth, height, COUNT(*) AS count
FROM 
	rounded
GROUP BY 
	width, depth, height
ORDER BY 
	width, depth, height


