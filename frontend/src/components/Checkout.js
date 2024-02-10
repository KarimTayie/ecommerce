import React from 'react'
import {PayPalButtons, usePayPalScriptReducer} from '@paypal/react-paypal-js'

import Loader from '../components/Loader'

function Checkout({amount, onApprove}) {
    const [{options, isPending}, dispatch] = usePayPalScriptReducer()

    const onCreateOrder = (data, actions) => {
        return actions.order.create({
            purchase_units: [
                {
                    amount: {
                        value: amount
                    }
                }
            ]
        })
    }

    // const onApproveOrder = (data, actions) => {
    //     return actions.order.capture().then((details) => {
    //         const name = details.payer.name.given_name
    //         alert(`Transaction completed by ${name}`)
    //     })
    // }

  return (
    <div className="checkout">
        {isPending ? <Loader/> : (
            <PayPalButtons 
                style={{ layout: "vertical" }}
                createOrder={(data, actions) => onCreateOrder(data, actions)}
                // onApprove={(data, actions) => onApproveOrder(data, actions)}
                onApprove={onApprove}
            />
        )}
    </div>
  )
}

export default Checkout