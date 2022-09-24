import './App.css';
import OrderList from './components/OrderList';
import logo from './logo.png';

function App() {
    const url = 'http://localhost:8080'

    return (
        <div className="App">
            <div className="App-header">
                <img className="App-logo" src={logo} alt="Logo"></img>
            </div>
            <div className="App-content">
                <div className='Half-width'>
                    <OrderList url={url}/>
                </div>
                <div className='Half-width'>Hello</div>
            </div>
        </div>
    );
}

export default App;
