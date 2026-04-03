import {BrowserRouter,Routes,Route} from "react-router-dom";
import Dashboard from "./Dashboard";
function Home(){
return(<div style={{padding:40}}>
<h1>ActionHunter</h1>
<button onClick={()=>window.location.href="http://localhost:8000/auth/login"}>Login</button>
</div>)}
export default function App(){
return(<BrowserRouter><Routes>
<Route path="/" element={<Home/>}/>
<Route path="/dashboard" element={<Dashboard/>}/>
</Routes></BrowserRouter>)}
