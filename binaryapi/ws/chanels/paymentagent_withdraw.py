"""Module for Binary paymentagent_withdraw websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#paymentagent_withdraw

class PaymentagentWithdraw(Base):
    """Class for Binary paymentagent_withdraw websocket chanel."""

    name = "paymentagent_withdraw"

    def __call__(self, amount, currency: str, paymentagent_loginid: str, verification_code: str, description: str = None, dry_run: int = None, passthrough=None, req_id: int = None):
        """Method to send message to paymentagent_withdraw websocket chanel.
        Payment Agent: Withdraw (request)
        Initiate a withdrawal to an approved Payment Agent.
        :param amount: The amount to withdraw to the payment agent.
        :type amount: 
        :param currency: The currency code.
        :type currency: str
        :param paymentagent_loginid: The payment agent loginid received from the `paymentagent_list` call.
        :type paymentagent_loginid: str
        :param verification_code: Email verification code (received from a `verify_email` call, which must be done first)
        :type verification_code: str
        :param description: [Optional] Remarks about the withdraw. Only letters, numbers, space, period, comma, - ' are allowed.
        :type description: str
        :param dry_run: [Optional] If set to 1, just do validation.
        :type dry_run: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "paymentagent_withdraw": int(1),
            "amount": amount,
            "currency": currency,
            "paymentagent_loginid": paymentagent_loginid,
            "verification_code": verification_code
        }

        if description:
            data['description'] = str(description)

        if dry_run:
            data['dry_run'] = int(dry_run)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
