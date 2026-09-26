MATCH (s:Student {id: $student1_id})
SET s.experience = $student1_experience
RETURN s;


MATCH (p:Project {id: $project_id})
SET p.status = $project_status
RETURN p;


MATCH (c:Course {id: $course_id})
SET c.duration = $course_duration
RETURN c;


MATCH (s:Student {id: $student2_id})
SET s.experience = $student2_experience,
    s.level = $student2_level
RETURN s;