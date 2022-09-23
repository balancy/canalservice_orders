import { useState } from "react";

const OrderList = () => {
    const [orderList, setOrderList] = useState();

    return (
        < div >
            <ul>
                <li>What</li>
                <li>Ist das?</li>
            </ul>
        </div >
    )
}

export default OrderList