import React, { Component } from "react";
import Chart from "react-apexcharts";

class AppChart extends Component {
    constructor(props) {
        super(props);

        this.state = {
            options: {
                chart: {
                    id: "basic-bar"
                },
                xaxis: {
                    categories: props.getColumnData(props.data, 'delivery_date')
                }
            },
            series: [
                {
                    name: "price",
                    data: props.getColumnData(props.data, 'rub_price')
                }
            ]
        };
    }

    render() {
        return (
            <div className="app">
                <div className="row">
                    <div className="mixed-chart">
                        <Chart
                            options={this.state.options}
                            series={this.state.series}
                            type="line"
                            width="100%"
                        />
                    </div>
                </div>
            </div>
        );
    }
}

export default AppChart;