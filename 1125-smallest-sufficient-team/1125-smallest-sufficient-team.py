class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_possessor_lookup = [set() for _ in req_skills]
        skill_ID_lookup = {skill: pos for pos, skill in enumerate(req_skills)}

        for person_id, person in enumerate(people):
            for skill in person:
                skill_ID = skill_ID_lookup[skill]
                skill_possessor_lookup[skill_ID].add(person_id)
        
        queue = deque([(skill_possessor_lookup, [])])

        while queue:
            top_skills, curr_group = queue.popleft()
            rarest_skill_possessors = min(top_skills, key=len)
            for person_id in rarest_skill_possessors:
                remaining_skills = [possessor for possessor in top_skills if person_id not in possessor]
                if not remaining_skills:
                    return curr_group + [person_id]
                queue.append((remaining_skills, curr_group + [person_id]))