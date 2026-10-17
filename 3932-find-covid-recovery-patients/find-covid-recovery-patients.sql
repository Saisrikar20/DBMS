select p.patient_id, p.patient_name, p.age, datediff(min(ct2.test_date), min(ct1.test_date)) as recovery_time
from patients p
join covid_tests ct1
on p.patient_id = ct1.patient_id and ct1.result ='Positive'
join covid_tests ct2
on p.patient_id = ct2.patient_id and ct2.result = 'Negative' and ct1.test_date < ct2.test_date
group by p.patient_id, p.patient_name
order by recovery_time asc, patient_name asc