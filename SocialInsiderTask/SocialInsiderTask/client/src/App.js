import './App.css';
import React, { useState, useEffect } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { 
  Route,
  Routes,
  useParams,
 } from 'react-router-dom';


export default function Link() {
  //Cream rute
  return (
      <Routes>
          <Route path="/" element={<App />} />
          <Route path="/calc_sum_fans/:id" element={<Fans />} />
          <Route path="/calc_sum_eng/:id" element={<Eng />} />
      </Routes>
  )
}

//Elementul pentru ruta in care calculam numarul total de engagements
function Eng()
{
  let {id} = useParams()

  //Imaprtim parametrul Id pentru a ne lua informatiile necesare
  var splitID = id.split(".")
  var pId = splitID[0]
  var startDate = splitID[2]
  var endDate = splitID[3]

  // Convertim data de start si data de sfarsit in zile-luna-an
  var sDate = new Date(Number(startDate))
  var stDate = `${sDate.getDate()}-${sDate.getMonth()+1}-${sDate.getFullYear()}`
  var eDate = new Date(Number(endDate))
  var enDate = `${eDate.getDate()}-${eDate.getMonth()+1}-${eDate.getFullYear()}`

  //useEffect pentru a fetch-ui informatiile din Profile data
  const [data, setData] = useState([])
  useEffect(() => {
      var url = `https://socialinsidertask.herokuapp.com/profile_data/${id}`
      fetch(url)
      .then((res) => res.json())
      .then((data) => {
        setData(data.resp)
      })
  }, [id])

  console.log(data)

  //Functia e calcul pentru suma de Engagements
  function calcSum(data) {
    if(data === undefined)
      return 'Cannot be computed'
    var myId = data[pId]
    var s = 0
    if(data) {
      
      for(const c in myId)
      {
        if(myId[c].engagement)
          s = s + myId[c].engagement
      }
    }
    return s
  }

  //Html-ul returnat
  return (
    <div className="App">
      <div className="App-header">
      < div>
          <span>The Total Number of Engagements between:</span>
          <span className='sDate'> {stDate}</span>
          <span> and </span>
          <span className='sDate'>{enDate}</span>
          <span> is </span>
          <span className='sDate'>{calcSum(data)}</span>.
        </div>
      </div>
    </div>
  )
}

//Elementul pentru ruta in care calculam numarul total de fans
function Fans()
{
  let {id} = useParams()

  //Imaprtim parametrul Id pentru a ne lua informatiile necesare
  var splitID = id.split(".")
  var pId = splitID[0]
  var startDate = splitID[2]
  var endDate = splitID[3]

  // Convertim data de start si data de sfarsit in zile-luna-an
  var sDate = new Date(Number(startDate))
  var stDate = `${sDate.getDate()}-${sDate.getMonth()+1}-${sDate.getFullYear()}`
  var eDate = new Date(Number(endDate))
  var enDate = `${eDate.getDate()}-${eDate.getMonth()+1}-${eDate.getFullYear()}`

  //useEffect pentru a fetch-ui informatiile din Profile data
  const [data, setData] = useState([])
  useEffect(() => {
      var url = `https://socialinsidertask.herokuapp.com/profile_data/${id}`
      fetch(url)
      .then((res) => res.json())
      .then((data) => {
        setData(data.resp)
      })
  }, [id])

  console.log(data)
  
  //Functia e calcul pentru suma de Fans
  function calcSum(data) {
    if(data === undefined)
      return 'Cannot be computed'
    var myId = data[pId]
    var s = 0
    if(data) {
      
      for(const c in myId)
      {
        if(myId[c].fans)
          s = s + myId[c].fans
      }
    }
    return s
  }

  //Html-ul returnat
  return (
    <div className="App">
      <div className="App-header">
      < div>
          <span>The Total Number of Fans between:</span>
          <span className='sDate'> {stDate}</span>
          <span> and </span>
          <span className='sDate'>{enDate}</span>
          <span> is </span>
          <span className='sDate'>{calcSum(data)}</span>.
        </div>
      </div>
    </div>
  )
}

//Elementrul pentru pagina principala
function App() {
  const [data, setData] = useState([])
  const [startDate, setStartDate] = useState(null);
  const [endtDate, setEndDate] = useState(null);

  //Fetch-uim brand-urile
  useEffect(() => {
    fetch("https://socialinsidertask.herokuapp.com/brands")
    .then((res) => res.json())
    .then((data) => {
      setData(data.result)
    })
  }, [])
  
  console.log(data)

    //Mapam brand-urile pentru a le fisa in tabel impreuna cu Id-ul acestora
    var brandName = data.map((obj, i) => {
      //Verificari
      if(data.error != null)
      {
        console.log(data.error)
        return <></>
      }
      else {
        //Profilele din data e un vector de obiecte pe care il parcurgem
        return obj.profiles.map((pObj, j) => { 
          // Verificari pentru data de start si de sfarsit 
          if(startDate != null && endtDate!=null)
          {
            //Cream link-urile care ne trimit la calcule
            const urlSumFans = `/calc_sum_fans/${pObj.id}.${pObj.profile_type}.${startDate.getTime()}.${endtDate.getTime()}`
            const urlSumEng = `/calc_sum_eng/${pObj.id}.${pObj.profile_type}.${startDate.getTime()}.${endtDate.getTime()}`
            
            //returnam tabelul
            return (
              <tr>
                {/* Numele brand-ului */}
                <td>{obj.brandname}</td>
                {/* Id-ul */}
                <td>{pObj.id}</td>
                {/* Link-ul care ne trimite catre numarul total de fans */}
                <td><a target="_blank" rel="noopener noreferrer" href={urlSumFans}>Find out</a></td>
                {/* Link-ul care ne trimite catre numarul total de engagements */}
                <td><a target="_blank" rel="noopener noreferrer" href={urlSumEng}>Find out</a></td>
              </tr>
            )
          }
          else
            return <></>
        })   
      }
    })
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <div>
          <div>
            {/* Date-pick-urile */}
            <div className='edit'>
              <span>Start Date: </span>
              <DatePicker 
                className='sizeDatePicker' 
                dateFormat='dd-MM-yyyy'
                selected={startDate} 
                onChange={(date) => setStartDate(date)} 
                isClearable
                showYearDropdown
                scrollableMonthYearDropdown
              />
            </div>

            <div className='edit'>
            <span>End Date: </span>
              <DatePicker 
                className='sizeDatePicker' 
                dateFormat='dd-MM-yyyy'
                selected={endtDate} 
                onChange={(date) => setEndDate(date)} 
                isClearable
                showYearDropdown
                scrollableMonthYearDropdown
              />
            </div>
            <table className='table'>
              <thead>
                <tr>
                  {/* Head-urile tabelului */}
                  <th>Brand Name</th>
                  <th>ID Profile</th>
                  <th>Total Fans</th>
                  <th>Total Engagement</th>
                </tr>
              </thead>
              <tbody>
                {/* Apelarea functiei care ne returneaza tabelul */}
                {brandName}
              </tbody>
            </table>
          </div>
        </div>
      </header>
    </div>
  );
}
