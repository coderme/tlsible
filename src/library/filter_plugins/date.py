
# some date utilities

from datetime import datetime, timedelta




def older_than(val, **kwargs):
    '''
    checks if the passed val (timestamp) is older than current time minus computed timedelta 
    kwargs: are passed as is to datetime.timedelta
    supported kwargs: days, seconds, microseconds, milliseconds, minutes, hours, weeks
    '''
    if val is None:
        return val
    try:
        mtime = int(float(val))
    except:
        return None
    offset  =  datetime.now() - timedelta(**kwargs)
    return int(offset.strftime('%s')) > mtime



class FilterModule(object):
    def filters(self):
        return {
                "older_than": older_than,
                }


