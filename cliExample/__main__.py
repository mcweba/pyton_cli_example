#!/usr/bin/env python3	
import click 			
import sys 

@click.command()							
@click.argument('argument1', nargs=1)	
@click.argument('argument2', nargs=1)
def executeMe(argument1, argument2):
    """
    CLI tool used to demonstrate
    """
    #sys.exit("something was wrong. cancelled script")

    click.echo("param 1 was: " + argument1 + " and param 2 was: " + argument2)

if __name__ == '__main__':				
    executeMe()			
