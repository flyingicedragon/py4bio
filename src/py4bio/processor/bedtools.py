import subprocess


def bedtools(cmd: list) -> str:
    """Spawn new process to use bedtools. It is a universal Popen maker but is
    adapted to bedtools.
    :param cmd: command args list containing 'bedtools', eg,
    ['bedtools', 'window',
    '-a', bed_path: str,
    '-b', gff_path: str,
    '-w', str(flank_size: int)]
    :type cmd: list
    :return: bedtools output
    :rtype: str
    """
    sp = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    outs, errs = sp.communicate()
    sp.wait()
    outs = outs.decode()
    return outs
