@click.group()
def cli():
	""" Cli tool for deploying templates to CISCO SDWAN
	"""
	pass
@click.command()
def device_list():
	pass
@click.command():
def template_list():
	pass
@click.command()
def attached_devices():
	pass
@click.command()
def attach():
	pass
@click.command()
def detach():
	pass
cli.add_command(attach)
cli.add_command(detach)
cli.add_command(device_list)
cli.add_command(attached_devices)
cli.add_command(template_list)

if __name__ == "__main__":
	cli()