MATCH (s:Student {id: "S001"}), (c:Course {id: "C001"})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {id: "S001"}), (c:Course {id: "C002"})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {id: "S002"}), (c:Course {id: "C001"})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {id: "S002"}), (c:Course {id: "C003"})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {id: "S003"}), (c:Course {id: "C002"})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {id: "S003"}), (c:Course {id: "C004"})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {id: "S004"}), (c:Course {id: "C003"})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {id: "S005"}), (c:Course {id: "C004"})
CREATE (s)-[:ENROLLED_IN]->(c);








MATCH (m:Mentor {id: "M001"}), (c:Course {id: "C001"})
CREATE (m)-[:TEACHES]->(c);

MATCH (m:Mentor {id: "M001"}), (c:Course {id: "C002"})
CREATE (m)-[:TEACHES]->(c);

MATCH (m:Mentor {id: "M002"}), (c:Course {id: "C003"})
CREATE (m)-[:TEACHES]->(c);

MATCH (m:Mentor {id: "M003"}), (c:Course {id: "C004"})
CREATE (m)-[:TEACHES]->(c);



MATCH (c:Course {id: "C001"}), (s:Skill {id: "SK001"})
CREATE (c)-[:TEACHES_SKILL]->(s);

MATCH (c:Course {id: "C002"}), (s:Skill {id: "SK002"})
CREATE (c)-[:TEACHES_SKILL]->(s);

MATCH (c:Course {id: "C002"}), (s:Skill {id: "SK003"})
CREATE (c)-[:TEACHES_SKILL]->(s);

MATCH (c:Course {id: "C003"}), (s:Skill {id: "SK003"})
CREATE (c)-[:TEACHES_SKILL]->(s);

MATCH (c:Course {id: "C003"}), (s:Skill {id: "SK004"})
CREATE (c)-[:TEACHES_SKILL]->(s);

MATCH (c:Course {id: "C004"}), (s:Skill {id: "SK004"})
CREATE (c)-[:TEACHES_SKILL]->(s);

MATCH (c:Course {id: "C004"}), (s:Skill {id: "SK005"})
CREATE (c)-[:TEACHES_SKILL]->(s);



MATCH (s:Student {id: "S001"}), (p:Project {id: "P001"})
CREATE (s)-[:BUILT]->(p);

MATCH (s:Student {id: "S003"}), (p:Project {id: "P002"})
CREATE (s)-[:BUILT]->(p);

MATCH (s:Student {id: "S004"}), (p:Project {id: "P003"})
CREATE (s)-[:BUILT]->(p);

MATCH (s:Student {id: "S005"}), (p:Project {id: "P004"})
CREATE (s)-[:BUILT]->(p);


MATCH (s:Student {id: "S001"}), (c:Company {id: "CO001"})
CREATE (s)-[:INTERESTED_IN]->(c);

MATCH (s:Student {id: "S002"}), (c:Company {id: "CO002"})
CREATE (s)-[:INTERESTED_IN]->(c);

MATCH (s:Student {id: "S003"}), (c:Company {id: "CO003"})
CREATE (s)-[:INTERESTED_IN]->(c);

MATCH (s:Student {id: "S004"}), (c:Company {id: "CO004"})
CREATE (s)-[:INTERESTED_IN]->(c);

MATCH (s:Student {id: "S005"}), (c:Company {id: "CO001"})
CREATE (s)-[:INTERESTED_IN]->(c);