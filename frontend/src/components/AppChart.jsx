import React, { useEffect, useState } from "react";
import Chart from "react-apexcharts";

const AppChart = (props) => {
    const [options, setOptions] = useState({});
    const [series, setSeries] = useState([]);

    // recalculate points for the chart when data in props chaned
    useEffect(() => {
        setOptions({
            chart: {
                id: "basic-bar"
            },
            xaxis: {
                categories: props.getColumnData(props.data, 'delivery_date')
            }
        })
        setSeries([
            {
                name: "price",
                data: props.getColumnData(props.data, 'rub_price')
            }
        ])
    }, [props])

    return (
        <div className="app">
            <div className="row">
                <div className="mixed-chart">
                    <Chart
                        options={options}
                        series={series}
                        type="line"
                        width="100%"
                    />
                </div>
            </div>
        </div>
    );
}

export default AppChart;