import { useEffect, useState } from "react";

const AppTotal = (props) => {
    const [total, setTotal] = useState(0);

    const sum = (arr) => arr.reduce((partialSum, a) => partialSum + a, 0);

    useEffect(() => {
        let rub_prices = props.getColumnData(props.data, 'rub_price')
        setTotal(Math.round(sum(rub_prices)))
    }, [props.data])

    return (
        <div className="Total-table">
            {total > 0 && (
                <table>
                    <thead><tr><th>
                        Total
                    </th></tr></thead>
                    <tbody><tr><td>
                        {total}
                    </td></tr></tbody>
                </table>
            )}
        </div>
    )
}

export default AppTotal