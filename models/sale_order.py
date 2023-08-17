from osv import fields, orm,osv
from tools.translate import _
from .. import requests
import json
class SaleOrder(osv.Model):
    _name= 'sale.order'
    _inherit = 'sale.order'
    _columns = {
        'partner_id':  fields.many2one('res.partner', 'Recipient'),
        'mobile':   fields.related('partner_id',  'mobile',type='char',string="Mobile", readonly=True),
        'message': fields.text("Message", required=False)
    }
    def send_message_template(self, cr, uid, ids, context=None):
      wizard = self.browse(cr, uid, ids[0], context)
     
      url = "https://graph.facebook.com/version/the_number/messages"
      
      payload = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": wizard.mobile,
        "type": "template",
        "template": {
          "name": "generic",
          "language": {
            "code": "en_US"
          },
          "components": [
            {
              "type": "body",
              "parameters": [
                
                {
                  "type": "text",
                  "text": ",",
                }
              ]
            }
          ]
        }
      })
      headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer code'
      }
      requests.request("POST", url, headers=headers, data=payload)

    
        
       
    



