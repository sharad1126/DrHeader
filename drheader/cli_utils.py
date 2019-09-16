# -*- coding: utf-8 -*-

"""Utils for drheader console script."""

import json

import click


def echo_bulk_report(audit, json_output=False):
    """
    Output bulk report.

    :param audit: audit from core
    :param json_output: json output flag
    :return: None
    """

    if json_output:
        click.echo(json.dumps(audit))
    else:
        for i in audit:
            issues_header = '{url}: {issues} issues'.format(issues=len(i['report']), url=i['url'])
            click.echo()
            click.echo(issues_header)
            click.echo('=' * len(issues_header))
            for _ in i['report']:
                for v, k in _.items():
                    click.echo('{}: {}'.format(v, k))
                click.echo('----')
