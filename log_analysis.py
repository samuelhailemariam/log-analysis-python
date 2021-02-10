import re
import csv
import operator

errors = {}
user_stat = {}

pattern = r"ticky: (\w+):([\w ']*) \[(#\d+)\] \((\w.+)\)"
with open('syslog.log', 'r') as log_file:
    for line in log_file.readlines():
        result = re.search(pattern, line)
        if result:
            username = result.group(4)
            if not user_stat.get(username):
                user_stat[username] = {'error': 0, 'info':0}

            if result.group(1) == 'INFO':
                user_stat[username]['info'] += 1
            else:
                user_stat[username]['error'] += 1
                error_msg = result.group(2).strip()
                if not errors.get(error_msg):
                    errors[error_msg] = 1
                else:
                    errors[error_msg] += 1

errors_sorted = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
user_stat_sorted = sorted(user_stat.items())


with open('error_msgs.csv', 'w') as err_rep:
    csv_columns = ['Error', 'Count']
    writer = csv.DictWriter(err_rep, fieldnames=csv_columns)
    writer.writeheader()
    for data in errors_sorted:
        to_write = {'Error': data[0], 'Count': data[1]}
        writer.writerow(to_write)

with open('user_stat.csv', 'w') as stat_rep:
    csv_columns = ['Username', 'INFO', 'ERROR']
    writer = csv.DictWriter(stat_rep, fieldnames=csv_columns)
    writer.writeheader()
    for data in user_stat_sorted:
        to_write = {'Username': data[0], 'INFO': data[1]['info'], 'ERROR': data[1]['error']}
        writer.writerow(to_write)       

