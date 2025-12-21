delete from person where id in 
(select id from person a where exists
(select 1 from person p where p.email = a.email and p.id < a.id))
