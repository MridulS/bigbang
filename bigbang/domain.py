"""
Functions for extracting parts of an email address, such as its domain.
"""

import math
import pandas as pd
import re

email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
domain_regex = r"[@]([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$"


def domain_entropy(domain, froms):
    """
    Compute the entropy of the distribution of counts of email prefixes
    within the given archive.

    Parameters
    ---------------

    domain: string
        An email domain

    froms: pandas.DataFrame
        A pandas.DataFrame with From fields, email address, and domains.
        See the Archive method ``get_froms()``


    Returns
    --------

    entropy: float
    """

    domain_messages = froms[froms["domain"] == domain]

    n_D = domain_messages.shape[0]

    entropy = 0

    emails = domain_messages["email"].unique()

    for em in emails:
        em_messages = domain_messages[domain_messages["email"] == em]
        n_e = em_messages.shape[0]

        p_em = float(n_e) / n_D

        entropy = entropy - p_em * math.log(p_em)

    return entropy


def extract_email(from_field):
    """
    Returns an email address from a string.
    """
    match = re.search(email_regex, from_field)

    if match is not None:
        return match[0].lower()

    else:
        return None


def extract_domain(from_field):
    """
    Returns the domain of an email address from a string.
    """
    match = re.search(email_regex, from_field)

    if match is not None:
        return re.search(domain_regex, match[0])[1]

    else:
        return None
