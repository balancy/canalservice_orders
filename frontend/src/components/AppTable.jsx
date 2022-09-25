const AppData = (props) => (
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
        {props.data.length > 0 && (
            <tbody>
                {props.data.map(order => (
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

export default AppData