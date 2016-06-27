from coalib.bearlib.abstractions.Linter import linter


@linter(executable='go',
        use_stdout=False,
        use_stderr=True,
        output_format='regex',
        output_regex=r'.+:(?P<line>\d+): (?P<message>.*)')
class GoVetBear:
    """
    Analyze Go code and raise suspicious constructs, such as printf calls
    whose arguments do not correctly match the format string, useless
    assignments, common mistakes about boolean operations, unreachable code,
    etc.

    This is done using the ``vet`` command. For more information visit
    <https://golang.org/cmd/vet/>.
    """
    LANGUAGES = {"Go"}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Unused Code', 'Smell', 'Unreachable Code'}

    @staticmethod
    def create_arguments(filename, file, config_file):
        return 'vet', filename
