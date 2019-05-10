# 4.7   Build Order
class Project(object):
    """A project has a name and a list of prerequisite projects.

    Attributes:
        name: The name
        prereqs: Projects this one depends on.
        successors: Projects depending on this one.
    """

    def __init__(self, n):
        self.name = n
        self.prereqs = []
        self.successors = []


def build_order(project_names: list, dep_list: list) -> str:
    """
    Find a possible completion order for a list of projects with dependencies.

    Runtime: O(n+m)
    Memory: O(n+m)
    """
    projects: dict = {name: Project(name) for name in project_names}
    for proj, successor in dep_list:
        projects[successor].prereqs.append(projects[proj])
        projects[proj].successors.append(projects[successor])

    order = []
    proj_done = True
    while proj_done:
        proj_done = False
        completed = []
        for name, proj in projects.items():
            if len(proj.prereqs) == 0:
                order.append(name)
                _remove_prereq(proj)
                completed.append(name)
                proj_done = True
        for name in completed:
            del projects[name]
    if len(projects) > 0:
        raise TypeError("No valid build order found")
    return ' '.join(order)


def _remove_prereq(p: Project) -> None:
    for child in p.successors:
        child.prereqs.remove(p)
