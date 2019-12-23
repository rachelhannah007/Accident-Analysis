def predict_traffctl(data={}):
    """ Predictor for TRAFFCTL from model/5c9ceebceba31d57320008b6

        Predictive model by BigML - Machine Learning Made Easy
    """

    import re

    tm_tokens = 'tokens_only'
    tm_full_term = 'full_terms_only'
    tm_all = 'all'

    def term_matches(text, field_name, term):
        """ Counts the number of occurences of term and its variants in text

        """
        forms_list = term_forms[field_name].get(term, [term])
        options = term_analysis[field_name]
        token_mode = options.get('token_mode', tm_tokens)
        case_sensitive = options.get('case_sensitive', False)
        first_term = forms_list[0]
        if token_mode == tm_full_term:
            return full_term_match(text, first_term, case_sensitive)
        else:
            # In token_mode='all' we will match full terms using equals and
            # tokens using contains
            if token_mode == tm_all and len(forms_list) == 1:
                pattern = re.compile(r'^.+\b.+$', re.U)
                if re.match(pattern, first_term):
                    return full_term_match(text, first_term, case_sensitive)
            return term_matches_tokens(text, forms_list, case_sensitive)


    def full_term_match(text, full_term, case_sensitive):
        """Counts the match for full terms according to the case_sensitive
              option

        """
        if not case_sensitive:
            text = text.lower()
            full_term = full_term.lower()
        return 1 if text == full_term else 0

    def get_tokens_flags(case_sensitive):
        """Returns flags for regular expression matching depending on text
              analysis options

        """
        flags = re.U
        if not case_sensitive:
            flags = (re.I | flags)
        return flags


    def term_matches_tokens(text, forms_list, case_sensitive):
        """ Counts the number of occurrences of the words in forms_list in
               the text

        """
        flags = get_tokens_flags(case_sensitive)
        expression = ur'(\b|_)%s(\b|_)' % '(\\b|_)|(\\b|_)'.join(forms_list)
        pattern = re.compile(expression, flags=flags)
        matches = re.findall(pattern, text)
        return len(matches)


    term_analysis = {
        "ward_name": {
            "token_mode": 'all',
            "case_sensitive": False,
        },
        "division": {
            "token_mode": 'all',
            "case_sensitive": False,
        },
        "street1": {
            "token_mode": 'all',
            "case_sensitive": False,
        },
        "street2": {
            "token_mode": 'all',
            "case_sensitive": False,
        },
        "offset": {
            "token_mode": 'all',
            "case_sensitive": False,
        },
        "redlight": {
            "token_mode": 'all',
            "case_sensitive": False,
        },
    }
    term_forms = {
        "division": {
        },
        "street1": {
        },
        "street2": {
        },
        "ward_name": {
        },
        "redlight": {
        },
        "offset": {
        },
    }
    if (data.get('loccoord') is None):
        return u'No Control'
    if (data['loccoord'] == 'Intersection'):
        if (data.get('redlight') is None):
            return u'Traffic Signal'
        if (term_matches(data['redlight'], "redlight", "yes") > 0):
            return u'Traffic Signal'
        if (term_matches(data['redlight'], "redlight", "yes") <= 0):
            if (data.get('road_class') is None):
                return u'Traffic Signal'
            if (data['road_class'] == 'Major Arterial'):
                if (data.get('accloc') is None):
                    return u'Traffic Signal'
                if (data['accloc'] == 'Non Intersection'):
                    if (data.get('date_month') is None):
                        return u'No Control'
                    if (data['date_month'] > 7):
                        if (data.get('impactype') is None):
                            return u'No Control'
                        if (data['impactype'] == 'Cyclist Collisions'):
                            if (data.get('date_day_of_week') is None):
                                return u'Pedestrian Crossover'
                            if (data['date_day_of_week'] > 1):
                                return u'No Control'
                            if (data['date_day_of_week'] <= 1):
                                return u'Pedestrian Crossover'
                        if (data['impactype'] != 'Cyclist Collisions'):
                            return u'No Control'
                    if (data['date_month'] <= 7):
                        if (data.get('index_') is None):
                            return u'No Control'
                        if (data['index_'] > 80491570):
                            if (data.get('offset') is None):
                                return u'No Control'
                            if (term_matches(data['offset'], "offset", "east") > 0):
                                return u'Traffic Controller'
                            if (term_matches(data['offset'], "offset", "east") <= 0):
                                return u'No Control'
                        if (data['index_'] <= 80491570):
                            if (data.get('impactype') is None):
                                return u'Traffic Signal'
                            if (data['impactype'] == 'Angle'):
                                return u'No Control'
                            if (data['impactype'] != 'Angle'):
                                return u'Traffic Signal'
                if (data['accloc'] != 'Non Intersection'):
                    if (data.get('index_') is None):
                        return u'Traffic Signal'
                    if (data['index_'] > 80673732):
                        if (data.get('date_month') is None):
                            return u'Traffic Signal'
                        if (data['date_month'] > 9):
                            if (data.get('ward_name') is None):
                                return u'Traffic Signal'
                            if (term_matches(data['ward_name'], "ward_name", "centre") > 0):
                                return u'Stop Sign'
                            if (term_matches(data['ward_name'], "ward_name", "centre") <= 0):
                                return u'Traffic Signal'
                        if (data['date_month'] <= 9):
                            if (data.get('street1') is None):
                                return u'No Control'
                            if (term_matches(data['street1'], "street1", "ave") > 0):
                                if (data.get('date_day_of_month') is None):
                                    return u'No Control'
                                if (data['date_day_of_month'] > 12):
                                    if (data.get('longitude') is None):
                                        return u'Traffic Controller'
                                    if (data['longitude'] > -79.40935):
                                        if (term_matches(data['street1'], "street1", "park") > 0):
                                            if (data.get('impactype') is None):
                                                return u'Traffic Signal'
                                            if (data['impactype'] == 'Pedestrian Collisions'):
                                                return u'Traffic Signal'
                                            if (data['impactype'] != 'Pedestrian Collisions'):
                                                return u'No Control'
                                        if (term_matches(data['street1'], "street1", "park") <= 0):
                                            return u'Traffic Controller'
                                    if (data['longitude'] <= -79.40935):
                                        return u'No Control'
                                if (data['date_day_of_month'] <= 12):
                                    if (data.get('impactype') is None):
                                        return u'No Control'
                                    if (data['impactype'] == 'Angle'):
                                        return u'Stop Sign'
                                    if (data['impactype'] != 'Angle'):
                                        return u'No Control'
                            if (term_matches(data['street1'], "street1", "ave") <= 0):
                                if (data.get('division') is None):
                                    return u'Traffic Signal'
                                if (term_matches(data['division'], "division", "d32") > 0):
                                    if (data.get('impactype') is None):
                                        return u'Stop Sign'
                                    if (data['impactype'] == 'Sideswipe'):
                                        return u'No Control'
                                    if (data['impactype'] != 'Sideswipe'):
                                        return u'Stop Sign'
                                if (term_matches(data['division'], "division", "d32") <= 0):
                                    if (data.get('acclass') is None):
                                        return u'Traffic Signal'
                                    if (data['acclass'] == 'Non-Fatal Injury'):
                                        if (data.get('ward_name') is None):
                                            return u'Traffic Signal'
                                        if (term_matches(data['ward_name'], "ward_name", "scarborough-rouge river (42)") > 0):
                                            return u'Traffic Controller'
                                        if (term_matches(data['ward_name'], "ward_name", "scarborough-rouge river (42)") <= 0):
                                            if (term_matches(data['ward_name'], "ward_name", "trinity-spadina (20)") > 0):
                                                return u'Streetcar (Stop for)'
                                            if (term_matches(data['ward_name'], "ward_name", "trinity-spadina (20)") <= 0):
                                                return u'Traffic Signal'
                                    if (data['acclass'] != 'Non-Fatal Injury'):
                                        return u'No Control'
                    if (data['index_'] <= 80673732):
                        if (data.get('street2') is None):
                            return u'Traffic Signal'
                        if (term_matches(data['street2'], "street2", "blvd") > 0):
                            if (data.get('hour') is None):
                                return u'Traffic Signal'
                            if (data['hour'] > 18):
                                if (data.get('date_month') is None):
                                    return u'Stop Sign'
                                if (data['date_month'] > 6):
                                    return u'Stop Sign'
                                if (data['date_month'] <= 6):
                                    if (data.get('impactype') is None):
                                        return u'Traffic Controller'
                                    if (data['impactype'] == 'Pedestrian Collisions'):
                                        return u'Pedestrian Crossover'
                                    if (data['impactype'] != 'Pedestrian Collisions'):
                                        return u'Traffic Controller'
                            if (data['hour'] <= 18):
                                if (data.get('division') is None):
                                    return u'Traffic Signal'
                                if (term_matches(data['division'], "division", "d14") > 0):
                                    return u'Traffic Signal'
                                if (term_matches(data['division'], "division", "d14") <= 0):
                                    if (data.get('latitude') is None):
                                        return u'Stop Sign'
                                    if (data['latitude'] > 43.75743):
                                        return u'Traffic Signal'
                                    if (data['latitude'] <= 43.75743):
                                        if (data.get('street1') is None):
                                            return u'Stop Sign'
                                        if (term_matches(data['street1'], "street1", "dr") > 0):
                                            return u'Traffic Signal'
                                        if (term_matches(data['street1'], "street1", "dr") <= 0):
                                            return u'Stop Sign'
                        if (term_matches(data['street2'], "street2", "blvd") <= 0):
                            if (data.get('latitude') is None):
                                return u'Traffic Signal'
                            if (data['latitude'] > 43.73659):
                                if (data.get('ward_name') is None):
                                    return u'Traffic Signal'
                                if (term_matches(data['ward_name'], "ward_name", "centre") > 0):
                                    if (data['index_'] > 44001700):
                                        return u'Traffic Signal'
                                    if (data['index_'] <= 44001700):
                                        if (data.get('fid') is None):
                                            return u'Traffic Signal'
                                        if (data['fid'] > 2634):
                                            if (data.get('date_day_of_month') is None):
                                                return u'Traffic Signal'
                                            if (data['date_day_of_month'] > 21):
                                                if (data.get('impactype') is None):
                                                    return u'No Control'
                                                if (data['impactype'] == 'Pedestrian Collisions'):
                                                    return u'Traffic Signal'
                                                if (data['impactype'] != 'Pedestrian Collisions'):
                                                    return u'No Control'
                                            if (data['date_day_of_month'] <= 21):
                                                return u'Traffic Signal'
                                        if (data['fid'] <= 2634):
                                            if (data.get('street1') is None):
                                                return u'No Control'
                                            if (term_matches(data['street1'], "street1", "road") > 0):
                                                return u'Traffic Controller'
                                            if (term_matches(data['street1'], "street1", "road") <= 0):
                                                return u'No Control'
                                if (term_matches(data['ward_name'], "ward_name", "centre") <= 0):
                                    if (data.get('date_year') is None):
                                        return u'Traffic Signal'
                                    if (data['date_year'] > 2012):
                                        if (term_matches(data['ward_name'], "ward_name", "willowdale") > 0):
                                            if (data.get('date_month') is None):
                                                return u'No Control'
                                            if (data['date_month'] > 6):
                                                if (data.get('hour') is None):
                                                    return u'No Control'
                                                if (data['hour'] > 14):
                                                    return u'No Control'
                                                if (data['hour'] <= 14):
                                                    return u'Traffic Signal'
                                            if (data['date_month'] <= 6):
                                                if (data.get('hour') is None):
                                                    return u'Traffic Signal'
                                                if (data['hour'] > 16):
                                                    return u'Traffic Signal'
                                                if (data['hour'] <= 16):
                                                    return u'Stop Sign'
                                        if (term_matches(data['ward_name'], "ward_name", "willowdale") <= 0):
                                            if (data.get('date_month') is None):
                                                return u'Traffic Signal'
                                            if (data['date_month'] > 3):
                                                return u'Traffic Signal'
                                            if (data['date_month'] <= 3):
                                                if (term_matches(data['ward_name'], "ward_name", "agincourt") > 0):
                                                    return u'No Control'
                                                if (term_matches(data['ward_name'], "ward_name", "agincourt") <= 0):
                                                    return u'Traffic Signal'
                                    if (data['date_year'] <= 2012):
                                        if (data['index_'] > 4165249):
                                            return u'Traffic Signal'
                                        if (data['index_'] <= 4165249):
                                            if (data.get('impactype') is None):
                                                return u'Traffic Signal'
                                            if (data['impactype'] == 'Turning Movement'):
                                                return u'Traffic Signal'
                                            if (data['impactype'] != 'Turning Movement'):
                                                return u'Pedestrian Crossover'
                            if (data['latitude'] <= 43.73659):
                                if (data.get('hour') is None):
                                    return u'Traffic Signal'
                                if (data['hour'] > 3):
                                    if (data.get('fid') is None):
                                        return u'Traffic Signal'
                                    if (data['fid'] > 3942):
                                        if (data['latitude'] > 43.72125):
                                            if (data.get('street1') is None):
                                                return u'No Control'
                                            if (term_matches(data['street1'], "street1", "st") > 0):
                                                return u'Traffic Signal'
                                            if (term_matches(data['street1'], "street1", "st") <= 0):
                                                return u'No Control'
                                        if (data['latitude'] <= 43.72125):
                                            return u'Traffic Signal'
                                    if (data['fid'] <= 3942):
                                        if (data.get('rdsfcond') is None):
                                            return u'Traffic Signal'
                                        if (data['rdsfcond'] == 'Wet'):
                                            if (data.get('division') is None):
                                                return u'Traffic Signal'
                                            if (term_matches(data['division'], "division", "d14") > 0):
                                                return u'Stop Sign'
                                            if (term_matches(data['division'], "division", "d14") <= 0):
                                                return u'Traffic Signal'
                                        if (data['rdsfcond'] != 'Wet'):
                                            if (data.get('division') is None):
                                                return u'Traffic Signal'
                                            if (term_matches(data['division'], "division", "d32") > 0):
                                                if (data.get('impactype') is None):
                                                    return u'No Control'
                                                if (data['impactype'] == 'Pedestrian Collisions'):
                                                    return u'Stop Sign'
                                                if (data['impactype'] != 'Pedestrian Collisions'):
                                                    return u'No Control'
                                            if (term_matches(data['division'], "division", "d32") <= 0):
                                                if (data['fid'] > 3541):
                                                    if (data['latitude'] > 43.66687):
                                                        if (data.get('street1') is None):
                                                            return u'Stop Sign'
                                                        if (term_matches(data['street1'], "street1", "bayview") > 0):
                                                            return u'Traffic Signal'
                                                        if (term_matches(data['street1'], "street1", "bayview") <= 0):
                                                            return u'Stop Sign'
                                                    if (data['latitude'] <= 43.66687):
                                                        if (data.get('date_hour') is None):
                                                            return u'Traffic Signal'
                                                        if (data['date_hour'] > 4):
                                                            return u'No Control'
                                                        if (data['date_hour'] <= 4):
                                                            return u'Traffic Signal'
                                                if (data['fid'] <= 3541):
                                                    if (data.get('date_month') is None):
                                                        return u'Traffic Signal'
                                                    if (data['date_month'] > 2):
                                                        if (data.get('date_day_of_month') is None):
                                                            return u'Traffic Signal'
                                                        if (data['date_day_of_month'] > 10):
                                                            if (data.get('street1') is None):
                                                                return u'Traffic Signal'
                                                            if (term_matches(data['street1'], "street1", "dr") > 0):
                                                                return u'No Control'
                                                            if (term_matches(data['street1'], "street1", "dr") <= 0):
                                                                if (data['date_month'] > 11):
                                                                    return u'No Control'
                                                                if (data['date_month'] <= 11):
                                                                    if (term_matches(data['street2'], "street2", "dr") > 0):
                                                                        if (data.get('impactype') is None):
                                                                            return u'Traffic Signal'
                                                                        if (data['impactype'] == 'Rear End'):
                                                                            return u'Traffic Signal'
                                                                        if (data['impactype'] != 'Rear End'):
                                                                            if (data['impactype'] == 'Turning Movement'):
                                                                                return u'No Control'
                                                                            if (data['impactype'] != 'Turning Movement'):
                                                                                return u'Stop Sign'
                                                                    if (term_matches(data['street2'], "street2", "dr") <= 0):
                                                                        if (data['fid'] > 1302):
                                                                            return u'Traffic Signal'
                                                                        if (data['fid'] <= 1302):
                                                                            if (data['latitude'] > 43.66697):
                                                                                if (data.get('date_day_of_week') is None):
                                                                                    return u'No Control'
                                                                                if (data['date_day_of_week'] > 5):
                                                                                    return u'Traffic Signal'
                                                                                if (data['date_day_of_week'] <= 5):
                                                                                    return u'No Control'
                                                                            if (data['latitude'] <= 43.66697):
                                                                                return u'Traffic Signal'
                                                        if (data['date_day_of_month'] <= 10):
                                                            if (data.get('ward_name') is None):
                                                                return u'Traffic Signal'
                                                            if (term_matches(data['ward_name'], "ward_name", "centre") > 0):
                                                                if (data.get('date_day_of_week') is None):
                                                                    return u'Traffic Signal'
                                                                if (data['date_day_of_week'] > 3):
                                                                    return u'Traffic Signal'
                                                                if (data['date_day_of_week'] <= 3):
                                                                    return u'No Control'
                                                            if (term_matches(data['ward_name'], "ward_name", "centre") <= 0):
                                                                if (data.get('date_day_of_week') is None):
                                                                    return u'Traffic Signal'
                                                                if (data['date_day_of_week'] > 5):
                                                                    return u'Stop Sign'
                                                                if (data['date_day_of_week'] <= 5):
                                                                    if (data.get('longitude') is None):
                                                                        return u'Traffic Signal'
                                                                    if (data['longitude'] > -79.31232):
                                                                        if (data['latitude'] > 43.67683):
                                                                            return u'Stop Sign'
                                                                        if (data['latitude'] <= 43.67683):
                                                                            return u'Traffic Signal'
                                                                    if (data['longitude'] <= -79.31232):
                                                                        return u'Traffic Signal'
                                                    if (data['date_month'] <= 2):
                                                        if (data.get('date_day_of_month') is None):
                                                            return u'Traffic Signal'
                                                        if (data['date_day_of_month'] > 14):
                                                            if (data['hour'] > 16):
                                                                return u'Traffic Signal'
                                                            if (data['hour'] <= 16):
                                                                if (data['latitude'] > 43.64606):
                                                                    return u'Stop Sign'
                                                                if (data['latitude'] <= 43.64606):
                                                                    return u'Traffic Signal'
                                                        if (data['date_day_of_month'] <= 14):
                                                            if (data.get('impactype') is None):
                                                                return u'Traffic Signal'
                                                            if (data['impactype'] == 'Approaching'):
                                                                return u'No Control'
                                                            if (data['impactype'] != 'Approaching'):
                                                                return u'Traffic Signal'
                                if (data['hour'] <= 3):
                                    if (data.get('date_year') is None):
                                        return u'Traffic Signal'
                                    if (data['date_year'] > 2013):
                                        if (data['latitude'] > 43.70193):
                                            return u'Traffic Signal'
                                        if (data['latitude'] <= 43.70193):
                                            return u'No Control'
                                    if (data['date_year'] <= 2013):
                                        if (data.get('impactype') is None):
                                            return u'Traffic Signal'
                                        if (data['impactype'] == 'SMV Other'):
                                            return u'No Control'
                                        if (data['impactype'] != 'SMV Other'):
                                            return u'Traffic Signal'
            if (data['road_class'] != 'Major Arterial'):
                if (data.get('impactype') is None):
                    return u'Stop Sign'
                if (data['impactype'] == 'Angle'):
                    if (data.get('street1') is None):
                        return u'Stop Sign'
                    if (term_matches(data['street1'], "street1", "ave") > 0):
                        if (data.get('date_year') is None):
                            return u'Stop Sign'
                        if (data['date_year'] > 2009):
                            if (data.get('date_day_of_week') is None):
                                return u'No Control'
                            if (data['date_day_of_week'] > 4):
                                if (data['date_day_of_week'] > 6):
                                    return u'Pedestrian Crossover'
                                if (data['date_day_of_week'] <= 6):
                                    return u'Traffic Signal'
                            if (data['date_day_of_week'] <= 4):
                                return u'No Control'
                        if (data['date_year'] <= 2009):
                            return u'Stop Sign'
                    if (term_matches(data['street1'], "street1", "ave") <= 0):
                        return u'Stop Sign'
                if (data['impactype'] != 'Angle'):
                    if (data.get('latitude') is None):
                        return u'Traffic Signal'
                    if (data['latitude'] > 43.69994):
                        if (data.get('date_day_of_week') is None):
                            return u'No Control'
                        if (data['date_day_of_week'] > 3):
                            if (data.get('date_year') is None):
                                return u'No Control'
                            if (data['date_year'] > 2010):
                                if (data['latitude'] > 43.77313):
                                    if (data.get('date_month') is None):
                                        return u'Traffic Signal'
                                    if (data['date_month'] > 8):
                                        return u'No Control'
                                    if (data['date_month'] <= 8):
                                        if (data.get('hour') is None):
                                            return u'Traffic Signal'
                                        if (data['hour'] > 17):
                                            return u'No Control'
                                        if (data['hour'] <= 17):
                                            return u'Traffic Signal'
                                if (data['latitude'] <= 43.77313):
                                    if (data.get('injury') is None):
                                        return u'No Control'
                                    if (data['injury'] == 'None'):
                                        if (data['date_day_of_week'] > 5):
                                            return u'Traffic Signal'
                                        if (data['date_day_of_week'] <= 5):
                                            return u'No Control'
                                    if (data['injury'] != 'None'):
                                        if (data['latitude'] > 43.76073):
                                            return u'No Control'
                                        if (data['latitude'] <= 43.76073):
                                            if (data['road_class'] == 'Minor Arterial'):
                                                return u'No Control'
                                            if (data['road_class'] != 'Minor Arterial'):
                                                return u'Stop Sign'
                            if (data['date_year'] <= 2010):
                                if (data.get('date_day_of_month') is None):
                                    return u'No Control'
                                if (data['date_day_of_month'] > 25):
                                    return u'Stop Sign'
                                if (data['date_day_of_month'] <= 25):
                                    return u'No Control'
                        if (data['date_day_of_week'] <= 3):
                            if (data.get('acclass') is None):
                                return u'Stop Sign'
                            if (data['acclass'] == 'Non-Fatal Injury'):
                                if (data.get('longitude') is None):
                                    return u'Stop Sign'
                                if (data['longitude'] > -79.48769):
                                    if (data.get('index_') is None):
                                        return u'Stop Sign'
                                    if (data['index_'] > 7835902):
                                        if (data.get('hour') is None):
                                            return u'Stop Sign'
                                        if (data['hour'] > 17):
                                            return u'Traffic Signal'
                                        if (data['hour'] <= 17):
                                            if (data['date_day_of_week'] > 1):
                                                if (data['impactype'] == 'Approaching'):
                                                    return u'No Control'
                                                if (data['impactype'] != 'Approaching'):
                                                    return u'Stop Sign'
                                            if (data['date_day_of_week'] <= 1):
                                                return u'No Control'
                                    if (data['index_'] <= 7835902):
                                        if (data['latitude'] > 43.70095):
                                            if (data.get('street1') is None):
                                                return u'Stop Sign'
                                            if (term_matches(data['street1'], "street1", "road") > 0):
                                                return u'Traffic Signal'
                                            if (term_matches(data['street1'], "street1", "road") <= 0):
                                                return u'Stop Sign'
                                        if (data['latitude'] <= 43.70095):
                                            return u'Traffic Signal'
                                if (data['longitude'] <= -79.48769):
                                    if (data['impactype'] == 'SMV Other'):
                                        return u'Traffic Signal'
                                    if (data['impactype'] != 'SMV Other'):
                                        return u'No Control'
                            if (data['acclass'] != 'Non-Fatal Injury'):
                                return u'Traffic Signal'
                    if (data['latitude'] <= 43.69994):
                        if (data.get('date_year') is None):
                            return u'Traffic Signal'
                        if (data['date_year'] > 2013):
                            if (data['latitude'] > 43.66488):
                                if (data.get('date_day_of_week') is None):
                                    return u'Traffic Signal'
                                if (data['date_day_of_week'] > 6):
                                    return u'No Control'
                                if (data['date_day_of_week'] <= 6):
                                    if (data['impactype'] == 'Pedestrian Collisions'):
                                        return u'Pedestrian Crossover'
                                    if (data['impactype'] != 'Pedestrian Collisions'):
                                        return u'Traffic Signal'
                            if (data['latitude'] <= 43.66488):
                                if (data.get('fid') is None):
                                    return u'No Control'
                                if (data['fid'] > 2347):
                                    if (data.get('invage') is None):
                                        return u'No Control'
                                    if (data['invage'] == '35 to 39'):
                                        return u'Stop Sign'
                                    if (data['invage'] != '35 to 39'):
                                        return u'No Control'
                                if (data['fid'] <= 2347):
                                    if (data['impactype'] == 'SMV Unattended Vehicle'):
                                        return u'No Control'
                                    if (data['impactype'] != 'SMV Unattended Vehicle'):
                                        return u'Traffic Signal'
                        if (data['date_year'] <= 2013):
                            if (data['impactype'] == 'Pedestrian Collisions'):
                                if (data.get('division') is None):
                                    return u'Stop Sign'
                                if (term_matches(data['division'], "division", "d14") > 0):
                                    return u'Traffic Signal'
                                if (term_matches(data['division'], "division", "d14") <= 0):
                                    return u'Stop Sign'
                            if (data['impactype'] != 'Pedestrian Collisions'):
                                if (data['impactype'] == 'Turning Movement'):
                                    if (data['latitude'] > 43.67765):
                                        if (data.get('date_day_of_week') is None):
                                            return u'Stop Sign'
                                        if (data['date_day_of_week'] > 2):
                                            return u'Stop Sign'
                                        if (data['date_day_of_week'] <= 2):
                                            return u'No Control'
                                    if (data['latitude'] <= 43.67765):
                                        if (data['latitude'] > 43.63615):
                                            return u'Traffic Signal'
                                        if (data['latitude'] <= 43.63615):
                                            if (data.get('street1') is None):
                                                return u'Stop Sign'
                                            if (term_matches(data['street1'], "street1", "st") > 0):
                                                return u'Stop Sign'
                                            if (term_matches(data['street1'], "street1", "st") <= 0):
                                                return u'Traffic Signal'
                                if (data['impactype'] != 'Turning Movement'):
                                    if (data.get('hour') is None):
                                        return u'Traffic Signal'
                                    if (data['hour'] > 14):
                                        if (data['hour'] > 16):
                                            if (data.get('street1') is None):
                                                return u'Pedestrian Crossover'
                                            if (term_matches(data['street1'], "street1", "road") > 0):
                                                return u'Traffic Signal'
                                            if (term_matches(data['street1'], "street1", "road") <= 0):
                                                return u'Pedestrian Crossover'
                                        if (data['hour'] <= 16):
                                            return u'No Control'
                                    if (data['hour'] <= 14):
                                        if (data['road_class'] == 'Minor Arterial'):
                                            return u'Traffic Signal'
                                        if (data['road_class'] != 'Minor Arterial'):
                                            if (data['impactype'] == 'Sideswipe'):
                                                return u'Traffic Signal'
                                            if (data['impactype'] != 'Sideswipe'):
                                                return u'No Control'
    if (data['loccoord'] == 'Mid-Block'):
        if (data.get('street1') is None):
            return u'No Control'
        if (term_matches(data['street1'], "street1", "dufferin") > 0):
            if (data.get('impactype') is None):
                return u'Traffic Signal'
            if (data['impactype'] == 'Approaching'):
                return u'Stop Sign'
            if (data['impactype'] != 'Approaching'):
                if (data.get('division') is None):
                    return u'Traffic Signal'
                if (term_matches(data['division'], "division", "d13") > 0):
                    return u'No Control'
                if (term_matches(data['division'], "division", "d13") <= 0):
                    if (data.get('ward_name') is None):
                        return u'Traffic Signal'
                    if (term_matches(data['ward_name'], "ward_name", "centre") > 0):
                        return u'No Control'
                    if (term_matches(data['ward_name'], "ward_name", "centre") <= 0):
                        return u'Traffic Signal'
        if (term_matches(data['street1'], "street1", "dufferin") <= 0):
            if (data.get('accnum') is None):
                return u'No Control'
            if (data['accnum'] > 7001414514):
                if (data['accnum'] > 7001722787):
                    if (data.get('division') is None):
                        return u'Traffic Signal'
                    if (term_matches(data['division'], "division", "d42") > 0):
                        return u'No Control'
                    if (term_matches(data['division'], "division", "d42") <= 0):
                        return u'Traffic Signal'
                if (data['accnum'] <= 7001722787):
                    if (data.get('latitude') is None):
                        return u'No Control'
                    if (data['latitude'] > 43.65844):
                        return u'No Control'
                    if (data['latitude'] <= 43.65844):
                        return u'Stop Sign'
            if (data['accnum'] <= 7001414514):
                if (term_matches(data['street1'], "street1", "finch") > 0):
                    if (data.get('division') is None):
                        return u'No Control'
                    if (term_matches(data['division'], "division", "d42") > 0):
                        return u'Traffic Signal'
                    if (term_matches(data['division'], "division", "d42") <= 0):
                        if (data.get('hour') is None):
                            return u'No Control'
                        if (data['hour'] > 1):
                            return u'No Control'
                        if (data['hour'] <= 1):
                            return u'Traffic Signal'
                if (term_matches(data['street1'], "street1", "finch") <= 0):
                    if (term_matches(data['street1'], "street1", "st") > 0):
                        if (data.get('index_') is None):
                            return u'No Control'
                        if (data['index_'] > 4180515):
                            if (data['accnum'] > 7000584324):
                                return u'Stop Sign'
                            if (data['accnum'] <= 7000584324):
                                return u'No Control'
                        if (data['index_'] <= 4180515):
                            if (data.get('hour') is None):
                                return u'No Control'
                            if (data['hour'] > 13):
                                return u'No Control'
                            if (data['hour'] <= 13):
                                if (data.get('impactype') is None):
                                    return u'Stop Sign'
                                if (data['impactype'] == 'Angle'):
                                    return u'Stop Sign'
                                if (data['impactype'] != 'Angle'):
                                    return u'Pedestrian Crossover'
                    if (term_matches(data['street1'], "street1", "st") <= 0):
                        if (data.get('street2') is None):
                            return u'No Control'
                        if (term_matches(data['street2'], "street2", "finch ave e") > 0):
                            if (data.get('ward_name') is None):
                                return u'No Control'
                            if (term_matches(data['ward_name'], "ward_name", "agincourt") > 0):
                                return u'No Control'
                            if (term_matches(data['ward_name'], "ward_name", "agincourt") <= 0):
                                return u'Pedestrian Crossover'
                        if (term_matches(data['street2'], "street2", "finch ave e") <= 0):
                            if (data.get('offset') is None):
                                return u'No Control'
                            if (term_matches(data['offset'], "offset", "12") > 0):
                                return u'Pedestrian Crossover'
                            if (term_matches(data['offset'], "offset", "12") <= 0):
                                return u'No Control'