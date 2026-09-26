MATCH (s:Student {id: $student_id})
      -[r:INTERESTED_IN]->
      (c:Company {id: $company_id})
DELETE r;

CREATE (:Skill {
    id: $skill_id,
    name: $skill_name
});



MATCH (s:Skill {id: $skill_id})
DELETE s;

MATCH (p:Project {id: $project_id})
DETACH DELETE p;