MATCH (s:Student)
RETURN s;

MATCH (c:Course)
RETURN c;

MATCH (s:Student)-[:ENROLLED_IN]->(c:Course)
RETURN s.name AS Student,
       c.name AS Course;


MATCH (m:Mentor)-[:TEACHES]->(c:Course)
RETURN m.name AS Mentor,
       c.name AS Course;

MATCH (c:Course)-[:TEACHES_SKILL]->(s:Skill)
RETURN c.name AS Course,
       collect(s.name) AS Skills;

MATCH (s:Student)-[:BUILT]->(p:Project)
RETURN s.name AS Student,
       p.name AS Project;


MATCH (s:Student)-[:ENROLLED_IN]->(c:Course)
      -[:TEACHES_SKILL]->(skill:Skill)
RETURN s.name AS Student,
       c.name AS Course,
       skill.name AS Skill;

MATCH (s:Student)-[:INTERESTED_IN]->(c:Company)
WHERE c.name = "Microsoft"
RETURN s.name AS Student,
       c.name AS Company;

MATCH (s:Student)
WHERE s.experience >= 3
RETURN s.name, s.experience;

MATCH (p:Project)-[:USES]->(s:Skill)
WHERE s.name = "Python"
RETURN p.name AS Project;

MATCH (c:Course)
WHERE c.level = "Advanced"
RETURN c;