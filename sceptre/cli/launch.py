import click

from sceptre.context import SceptreContext
from sceptre.cli.helpers import catch_exceptions
from sceptre.cli.helpers import confirmation
from sceptre.cli.helpers import stack_status_exit_code
from sceptre.plan.plan import SceptrePlan


@click.command(name="launch", short_help="Launch a Stack or StackGroup.")
@click.argument("path")
@click.option(
    "-y", "--yes", is_flag=True, help="Assume yes to all questions."
)

@click.option(
    "--wait", type=click.Choice(["yes", "no", "wait_only"]), default="yes",
    help="Wait for status completion.")

@click.pass_context
@catch_exceptions
def launch_command(ctx, path, yes, wait):
    """
    Launch a Stack or StackGroup for a given config PATH.
    \f

    :param path: The path to launch. Can be a Stack or StackGroup.
    :type path: str
    :param yes: A flag to answer 'yes' to all CLI questions.
    :type yes: bool
    """
    context = SceptreContext(
        command_path=path,
        project_path=ctx.obj.get("project_path"),
        user_variables=ctx.obj.get("user_variables"),
        options=ctx.obj.get("options"),
        ignore_dependencies=ctx.obj.get("ignore_dependencies"),
        wait=wait
    )

    plan = SceptrePlan(context)

    confirmation(plan.launch.__name__, yes, command_path=path)
    responses = plan.launch(wait)
    exit(stack_status_exit_code(responses.values()))
