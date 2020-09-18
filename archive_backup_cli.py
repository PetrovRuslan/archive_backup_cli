import os, shutil, sys, argparse, csv, datetime

source = ''
target = ''
date = datetime.date.today()
time = datetime.datetime.today().strftime("%H:%M:%S")

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-s', required=True, action='store', dest='source', help="Обязательный аргумент. Директория которую требуется заархивировать")
arg_parser.add_argument('-t', required=True, action='store', dest='target', help="Обязательный аргумент. Директория в которую надо скопировать бэкап")

args = arg_parser.parse_args()

if os.path.exists(args.source):
    parents_dir = os.path.dirname(os.path.abspath(args.source))
    archive_dir = os.path.basename(os.path.abspath(args.source))
    if os.path.exists(args.target):
        shutil.make_archive(f'{args.target}{archive_dir}_{date}_{time}', "gztar", parents_dir, archive_dir)
        with open('journal.csv', mode='a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow({f'{args.source};{args.target}{archive_dir}_{date}_{time}.tar.gz;{date};{time};success'})
    else:
        os.mkdir(args.target)
        shutil.make_archive(f'{args.target}{archive_dir}_{date}_{time}', "gztar", parents_dir, archive_dir)
        with open('journal.csv', mode='a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow({f'{args.source};{args.target}{archive_dir}_{date}_{time}.tar.gz;{date};{time};success'})
    print(f'{args.target}{archive_dir}_{date}_{time}.tar.gz')
else:
    print('Исходной директории не существует')
    with open('journal.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow({f'not found;not found;{date};{time};fail'})