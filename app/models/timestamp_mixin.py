from tortoise.fields import DatetimeField


class TimestampMixin:
    created_at = DatetimeField(null=True, auto_now_add=True)
    modified_at = DatetimeField(null=True, auto_now=True)
