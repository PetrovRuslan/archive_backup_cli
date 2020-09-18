import os, shutil, sys, argparse, csv, datetime

source = ''
target = ''

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-s', required=True, action='store', dest='source', help="Обязательный аргумент. Директория которую требуется заархивировать")
arg_parser.add_argument('-t', required=True, action='store', dest='target', help="Обязательный аргумент. Директория в которую надо скопировать бэкап")

args = arg_parser.parse_args()

if os.path.exists(args.source):
    parents_dir = os.path.dirname(os.path.abspath(args.source))
    archive_dir = os.path.basename(os.path.abspath(args.source))
    date = datetime.date.today()
    time = datetime.datetime.today().strftime("%H:%M:%S")
    with open('backups_log.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        # writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({f'{args.target}', f'{args.source}', f'{time}'})
        # writer.writerow({'game_data.dump', '2020-07-29', '1627'}) 
    if os.path.exists(args.target):
        shutil.make_archive(f'{args.target}{archive_dir}_{date}_{time}', "gztar", parents_dir, archive_dir)
    else:
        os.mkdir(args.target)
        # with open('бэкапы.csv', mode='w') as csv_file: 
        #     fieldnames = ['source', 'archive', 'date', 'time']
        #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        #     writer.writeheader()
        #     writer.writerow({'file_name': 'game_data.dump', 'backup_date': '2020-07-27', 'file_size': '1024'})
        #     writer.writerow({'file_name': 'game_data.dump', 'backup_date': '2020-07-29', 'file_size': '1627'})
        shutil.make_archive(f'{args.target}{archive_dir}_{date}_{time}', "gztar", parents_dir, archive_dir)
    print(f'{args.target}{archive_dir}_{date}_{time}.tar.gz')
else:
    print('Исходной директории не существует')