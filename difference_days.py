from datetime import datetime

def difference_days(last_login):
    current_date = datetime.utcnow()
    last_login_date = datetime.strptime(last_login, '%Y-%m-%dT%H:%M:%S.%fZ')
    if last_login_date != None:
        days_difference = (current_date - last_login_date).days
        return days_difference