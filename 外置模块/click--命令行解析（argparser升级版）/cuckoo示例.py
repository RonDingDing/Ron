import click
@click.group(invoke_without_command=True)
@click.option("-d", "--debug", is_flag=True, help="Enable verbose logging")
@click.option("-q", "--quiet", is_flag=True, help="Only log warnings and critical messages")
@click.option("--nolog", is_flag=True, help="Don't log to file.")
@click.option("-m", "--maxcount", default=0, help="Maximum number of analyses to process")
@click.option("--user", help="Drop privileges to this user")
@click.option("--cwd", help="Cuckoo Working Directory")
@click.pass_context
def main(ctx, debug, quiet, nolog, maxcount, user, cwd):
    print(ctx)
    print(debug)
    print(quiet)
    print(nolog)
    print(maxcount)
    print(user)
    print(cwd)
    


main()
