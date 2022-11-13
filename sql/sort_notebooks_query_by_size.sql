SELECT  
ROUND(CAST(width / 5  as numeric) , 0) * 5 as width_rounded, 
ROUND(CAST(depth / 5 as numeric), 0) * 5 as depth_rounded,
ROUND(CAST(height / 5 as numeric), 0) * 5 as height_rounded,
COUNT(*) as total_notebooks
FROM public.notebooks_notebook
GROUP BY width_rounded, depth_rounded, height_rounded
ORDER BY width_rounded DESC, depth_rounded DESC, height_rounded DESC