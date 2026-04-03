import React,{useEffect,useState} from "react";
import axios from "axios";
export default function Dashboard(){
const[user,setUser]=useState("");const[org,setOrg]=useState("");const[results,setResults]=useState([]);
useEffect(()=>{const p=new URLSearchParams(window.location.search);setUser(p.get("user"));},[]);
const scan=async()=>{const r=await axios.get(`http://localhost:8000/scan?org=${org}`);setResults(r.data);}
return(<div style={{padding:30}}>
<h2>Welcome {user}</h2>
<input value={org} onChange={e=>setOrg(e.target.value)} placeholder="org"/>
<button onClick={scan}>Scan</button>
{results.map((r,i)=>(<div key={i}><h3>{r.repo}</h3><p>{r.risk_score}</p></div>))}
</div>)}
