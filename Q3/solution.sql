SELECT O.owner_id, O.owner_name, COUNT (*) AS different_category_count
FROM owner AS O, article AS A, category_article_mapping AS C
WHERE O.owner_id=A.owner_id AND A.article_id=C.article_id
GROUP BY A.article_id
ORDER BY different_category_count DESC;