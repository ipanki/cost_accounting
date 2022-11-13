SELECT br.id, br.title, COUNT(nt.id) AS total_notebooks
    FROM public.notebooks_notebook nt
    JOIN public.notebooks_brand br ON br.id=nt.brand_id
	GROUP BY br.id, br.title
	ORDER by total_notebooks DESC
 