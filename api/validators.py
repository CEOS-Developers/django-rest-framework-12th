from django.core.exceptions import ValidationError

def validate_score(value):
    """평점(score)이 10보다 크면 Validation Error 를 일으킨다."""
    if (value > 10) | (value < 0 ):
        msg = u"'평점은 0 이상 10 이하로 매겨주세요."
        raise ValidationError(msg)