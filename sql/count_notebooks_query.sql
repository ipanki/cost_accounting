SELECT 
	br.title, COUNT(nt.id) AS count
FROM 
	notebooks_notebook nt
	LEFT JOIN 
	notebooks_brand br ON br.id=nt.brand_id
GROUP BY 
	br.title
ORDER BY
	count DESC
 