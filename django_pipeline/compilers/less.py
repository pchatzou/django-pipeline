from os.path import dirname

from ..conf import settings
from ..compilers import SubProcessCompiler


class LessCompiler(SubProcessCompiler):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith('.less')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        # Pipe to file rather than provide outfile arg due to a bug in lessc
        command = (
            settings.LESS_BINARY,
            settings.LESS_ARGUMENTS,
            infile,
        )
        return self.execute_command(command, cwd=dirname(infile), stdout_captured=outfile)
