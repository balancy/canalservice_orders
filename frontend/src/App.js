import './App.css';
import OrderList from './components/OrderList';
import logo from './logo.png';

function App() {
  return (
    <div className="App">
        <div className="App-header">
            <img className="App-logo" src={logo} alt="Logo"></img>
        </div>
        <div className="App-content">
            <OrderList/>
        </div>
    </div>
  );
}

export default App;
