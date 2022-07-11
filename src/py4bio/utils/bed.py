import pandas as pd


class Bed:
    """A bed like class. This class can import and export bed file."""

    def __init__(self) -> None:
        pass

    def as_bed(self, bed: list) -> None:
        """Import bed like content from a list.
        :param bed: bed like list
        :type bed: list
        """
        self.bed = pd.DataFrame(bed)

    def read_bed(self, bed_path: str) -> None:
        """Import bed from a bed file.
        :param bed_path: bed file path
        :type bed_path: str
        """
        with open(bed_path) as bed_file:
            self.bed: pd.DataFrame = pd.read_table(bed_file, header=None)

    def read_csv(self, csv_path: str) -> None:
        """Import bed from a csv file with a header.
        :param csv_path: csv file path
        :type csv_path: str
        """
        with open(csv_path) as csv_file:
            self.bed: pd.DataFrame = pd.read_csv(csv_file)

    def read_tsv(self, tsv_path: str) -> None:
        """Import bed from a tsv file with a header.
        :param tsv_path: tsv file path
        :type tsv_path: str
        """
        with open(tsv_path) as tsv_file:
            self.bed: pd.DataFrame = pd.read_table(tsv_file)

    def load(
        self, bed_content: str, sep: str = '\t', header: bool = False
    ) -> None:
        """Load a bed like string
        :param bed_content: string contain bed like content
        :type bed_content: str
        :param sep: delimiter to use, defaults to "\t"
        :type sep: str
        :param header: first row is column name or not, defaults to False
        :type header: bool
        """
        new_bed_content: list = bed_content.split('\n')
        while '' in new_bed_content:
            new_bed_content.remove('')
        if header:
            column_name = new_bed_content[0].split(sep)
            new_bed_content = new_bed_content[1:]
        new_bed_content = [line.split(sep) for line in new_bed_content]
        self.bed = pd.DataFrame(new_bed_content)
        if header:
            self.bed.columns = column_name

    def to_bed(self, bed_path: str) -> None:
        """Export bed to a bed file.
        :param bed_path: bed file path
        :type bed_path: str
        """
        self.bed.to_csv(bed_path, sep='\t', header=False, index=False)

    def to_csv(self, csv_path: str) -> None:
        """Export bed to a csv file with a header.
        :param csv_path: csv file path
        :type csv_path: str
        """
        self.bed.to_csv(csv_path, index=False)

    def to_tsv(self, tsv_path: str) -> None:
        """Export bed to a tsv file with a header.
        :param tsv_path: tsv file path
        :type tsv_path: str
        """
        self.bed.to_csv(tsv_path, sep='\t', index=False)
