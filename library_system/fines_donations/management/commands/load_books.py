import csv
from django.core.management.base import BaseCommand
from fines_donations.models import Book


class Command(BaseCommand):
    help = "Load books from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="The path to the CSV file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        try:
            with open(csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Book.objects.create(
                        title=row['Title'],
                        author=row['Author'],
                        publication_year=row['Publication_Year'],
                        publisher=row['Publisher'],
                        bar_code=row['Bar_Code']
                    )
            self.stdout.write(self.style.SUCCESS("Books loaded successfully!"))
        except KeyError as e:
            self.stderr.write(self.style.ERROR(f"Missing column in CSV: {e}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error loading books: {e}"))


