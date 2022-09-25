import './App.css';
import AppContent from './components/AppContent';
import logo from './logo.png';

function App() {
    const url = `${process.env.REACT_APP_BACKEND_HOST}:8080`

    return (
        <div className="App">
            <div className="App-header">
                <img className="App-logo" src={logo} alt="Logo"></img>
            </div>
            <AppContent className="App-content" url={url}/>
        </div>
    );
}

export default App;
