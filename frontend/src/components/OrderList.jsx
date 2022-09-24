import { useEffect, useState } from "react";

const OrderList = (url) => {
    const [orders, setOrders] = useState([]);
    const intervalDuration = 10_000

    const fetchData = async () => {
        const response = await fetch('http://localhost:8080/')
        const data = await response.json()
        setOrders(data)
    }

    useEffect(() => {
        setInterval(() => {
            fetchData()
        }, intervalDuration)
    }, [])

    return (
        <table>
            <thead>
                <tr>
                    <th>№</th>
                    <th>заказ №</th>
                    <th>стоимость, $</th>
                    <th>стоимость, ₽</th>
                    <th>срок поставки</th>
                </tr>
            </thead>
            {orders.length > 0 && (
                <tbody>
                    {orders.map(order => (
                        <tr key={order.id}>
                            <td>{order.id}</td>
                            <td>{order.number}</td>
                            <td>{order.usd_price}</td>
                            <td>{order.rub_price}</td>
                            <td>{order.delivery_date}</td>
                        </tr>
                    ))}
                </tbody>
            )}
        </table>
    )
}

export default OrderList