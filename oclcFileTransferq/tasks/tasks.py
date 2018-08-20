from celery.task import task
from oclcfiletransfer import transferfile

#Example task
@task()
def add(x, y):
    """ Example task that adds two numbers or strings
        args: x and y
        return addition or concatination of strings
    """
    result = x + y
    return result


@task()
def oclcFileTransfer(localfile, requestdata):
    return transferfile(localfile)
