def s_names(list_names):
    inc_data = False
    if list_names is None:
        inc_data = True
    else:
        for elem in list_names:
            if not elem.isalpha() or len(elem) > 10:
                inc_data = True
                break
    if inc_data:
        return "Incorrect data"
    elif len(list_names) == 0:
        return 'Это никому не нравится'
    elif len(list_names) == 1:
        return list_names[0] + ' лайкнул это.'
    elif len(list_names) <= 3:
        return '{0} и {1} лайкнули это.'.format(', '.join(list_names[:-1]), list_names[-1])
    else:
        return '{0} и ещё {1} человека лайкнули это.'.format(', '.join(list_names[:2]), str(len(list_names) - 2))
