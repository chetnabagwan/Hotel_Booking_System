from marshmallow import Schema,fields

class AuthSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True,load_only=True)

class AddRoomSchema(Schema):
    r_type  = fields.Str(required=True)
    r_price = fields.Int(required=True)

class DelRoomSchema(Schema):
    room_no = fields.Int(required=True)

class RoomUpdateSchema(Schema):
    room_no = fields.Int(required = True)
    r_type  = fields.Str(required=True)
    r_price = fields.Int(required=True)

class AddReceptionistSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True,load_only=True)
    emp_email = fields.Str(required=True)
    emp_age = fields.Int(required=True)
    emp_phone = fields.Int(required=True)
    emp_gender = fields.Str(required=True)

class ReceptionistSchema(Schema):
    emp_id = fields.Int(required=True)

class CheckinSchema(Schema):
    pass

class CheckoutSchema(Schema):
    pass

