from curses import has_key
from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    job_types = list()

    for each in [jobs["job_type"] for jobs in read(path)]:
        if each not in job_types:
            job_types.append(each)
    return job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """

    jobs_ = [job for job in jobs if job_type.upper() == job["job_type"]]
    return jobs_


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    industries = list()

    for each in [industry["industry"] for industry in read(
        path
            ) if industry["industry"] != ""]:
        if each not in industries:
            industries.append(each)
    return industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    industries = [job for job in jobs if industry.lower() == job["industry"]]
    return industries


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    salaries = [int(salary["max_salary"]) for salary in read(
        path) if salary["max_salary"].isdigit()]
    return max(salaries)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    salaries = [int(salary["min_salary"]) for salary in read(
        path) if salary["min_salary"].isdigit()]
    return min(salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    min_salary = job.get("min_salary", 0)
    max_salary = job.get("max_salary", 0)

    if type(min_salary) != int or type(
     max_salary
         ) != int or min_salary > max_salary or type(salary) != int:
        raise ValueError()

    in_range = min_salary <= salary <= max_salary

    return in_range


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
