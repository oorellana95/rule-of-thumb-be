from sqlalchemy import or_


def equal(query, value_from_entity, value_from_filter):
    """"""
    if value_from_filter is not None:
        query = query.filter(
            value_from_entity == value_from_filter
        )
    return query


def higher_or_equal(query, value_from_entity, value_from_filter):
    """"""
    if value_from_filter is not None:
        query = query.filter(
            value_from_entity >= value_from_filter
        )
    return query


def in_(query, value_from_entity, values_from_filter):
    """"""
    if values_from_filter is not None:
        query = query.filter(
            value_from_entity.in_(values_from_filter)
        )
    return query


def in_ilike(query, value_from_entity, values_from_filter):
    """"""
    if values_from_filter is not None:
        list_predicate = []
        for item in values_from_filter:
            list_predicate.append(value_from_entity.ilike(f'%{item}%'))

        query = query.filter(or_(*list_predicate))

    return query
