from dataclasses import dataclass

@dataclass
class LC:
    # in MS
    runtime: int
    # in MB
    memory_used: int
    # faster than x % of other submissions
    faster_than: int
    # LC problem number
    lc_num: int
    # LC problem URL
    url: str
    # Problem title
    title: str

    def __repr__(self):
        return f'''LeetCode Problem {self.lc_num} {self.title} stats:
        \tRuntime: {self.runtime} ms
        \tMemory used: {self.memory_used} MB
        \tFaster than {self.faster_than * 100}% of submissions
        See {self.url} for problem details'''
