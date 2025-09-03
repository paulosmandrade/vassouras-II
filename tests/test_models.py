from datetime import datetime

from vassouras_ii.models import BRTZ, current_time_brasilia


def test_current_time_brasilia_type():
    """Verifica se a função retorna um datetime"""
    now = current_time_brasilia()
    assert isinstance(now, datetime)


def test_current_time_brasilia_timezone():
    """Verifica se a timezone está correta"""
    now = current_time_brasilia()
    # Checa se o nome do fuso bate
    assert now.tzinfo.zone == BRTZ.zone
