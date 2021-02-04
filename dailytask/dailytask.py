# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Callable, Optional, Union
import time
from datetime import datetime

# Pip
from colored_logs.logger import Logger
from kcu import ktime
import stopit

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ----------------------------------------------------------- class: DailyTask ----------------------------------------------------------- #

class DailyTask:

    # -------------------------------------------------------- Public methods -------------------------------------------------------- #

    @classmethod
    def do_daily_task(
        cls,
        start_time: str,
        stop_time: str,
        function: Callable,
        utc: bool = True,
        *args,
        **kwargs
    ):
        start_s = ktime.time_str_to_seconds(start_time)
        stop_s = ktime.time_str_to_seconds(stop_time)

        try:
            while True:
                cls.__sleep_till_start(start_s, stop_s, utc=utc)
                cls.__wrapper_func(function=function, __timeout=ktime.today_seconds_till(stop_s, utc=utc), *args, **kwargs)
                cls.__sleep_till_start(start_s, None, utc=utc)
        except KeyboardInterrupt:
            exit(0)


    # ------------------------------------------------------- Private methods -------------------------------------------------------- #

    @classmethod
    def __sleep_till_start(
        cls,
        start_s: float,
        stop_s: Optional[float],
        utc: bool
    ) -> None:
        if stop_s and ktime.is_between_seconds(start_s, stop_s, utc):
            return

        log = Logger()
        start_time_str = ktime.seconds_to_time_str(start_s)
        seconds_till_start = ktime.today_seconds_till(start_s, utc=utc)

        try:
            sleep_start_s = time.time()
            log.start_process(
                'Sleeping ~ {} hour(s) till {}'.format(
                    round(seconds_till_start/ktime.seconds_in_hour),
                    start_time_str
                )
            )

            while not ktime.is_between_seconds(start_s, stop_s, utc) if stop_s else ktime.today_seconds_till(start_s, utc=utc) > 0:
                time.sleep(1)

            log.stop_process()
            log.info('Finished sleeping - {}'.format(ktime.seconds_to_time_str(int(time.time()-sleep_start_s))))
        except KeyboardInterrupt:
            log.stop_process()

            raise# KeyboardInterrupt

    @staticmethod
    @stopit.signal_timeoutable(default=Exception('Operation has timed out.'), timeout_param='__timeout')
    def __wrapper_func(
        function: Callable,
        *args,
        __timeout: Optional[int] = None,
        **kwargs,
    ) -> Optional:
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(e)

        return None


# ---------------------------------------------------------------------------------------------------------------------------------------- #