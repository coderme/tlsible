# Copyright (2018) CoderMe.com




class Unexpected(Exception):
    pass


def acme_get(value, key):
    '''
    Search for http-01 inside challenge_data
    raise an exception if value not found
    '''
    if 'challenge_data' in value:
        sub = value['challenge_data']
        try:
            domain = list(sub.keys())[0]
            return sub[domain]['http-01'][key]
        except: pass
    raise Unexpected('unexpected dictionary ', value, 1000000, key)




class FilterModule(object):
    def filters(self):
        return {
                "acme_get": acme_get,
                }


