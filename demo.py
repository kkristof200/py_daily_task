from dailytask import DailyTask

# def f(arg1: str, arg2: str = 'arg2') -> None:
#     print('arg1', arg1)
#     print('arg2', arg2)

# DailyTask.do_daily_task(
#     start_time_utc='21:0:0',
#     stop_time_utc='23:59:59',
#     function=f,
#     arg1='arg1',
#     arg2='arg2'
# )

def main():
    import time

    print('Starting task')
    time.sleep(2)
    print('Task is done')

DailyTask.do_daily_task('21:12:00', '11:50:50', main, utc=False)


# from kcu import ktime

# target = '21:00:00'
# target_seconds = ktime.time_str_to_seconds(target)
# seconds_till_target = ktime.today_seconds_till(target_seconds)

# print(target, target_seconds, seconds_till_target)