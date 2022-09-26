import { useEffect, useState } from "react";
import AppChart from "./AppChart";
import AppTable from './AppTable';
import AppTotal from "./AppTotal";

const AppContent = (props) => {
    const [data, setData] = useState([]);
    const intervalDuration = process.env.REACT_APP_REFRESH_INTERVAL_DURATION * 1000;

    // function that makes a vertical data slice. For example, the column 'delivery_date'.
    const getColumnData = (data, key) => data.map(row => row[key]);

    const fetchData = async () => {
        const response = await fetch(props.url)
        const data = await response.json()
        setData(data)
    }

    useEffect(() => {
        // fetch data every 'intervalDuration' miliseconds.
        setInterval(function refetch() {
            fetchData();
            return refetch;
        }(), intervalDuration)
    }, [])

    return (
        <div>
            <div className='App-column'>
                <AppTable data={data} />
            </div>
            <div className='App-column'>
                {data.length > 0 &&
                    <AppChart data={data} getColumnData={getColumnData}
                    />
                }
                <AppTotal data={data} getColumnData={getColumnData} />
            </div>
        </div>
    )
}

export default AppContent;