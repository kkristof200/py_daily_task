from dailytask import DailyTask

def f(arg1: str, arg2: str = 'arg2') -> None:
    print('arg1', arg1)
    print('arg2', arg2)

DailyTask.do_daily_task(
    start_time_utc='21:0:0',
    stop_time_utc='23:59:59',
    function=f,
    arg1='arg1',
    arg2='arg2'
)