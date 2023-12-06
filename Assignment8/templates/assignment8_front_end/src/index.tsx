import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
// import React from "react";
// import ReactDOM from "react-dom/client";
// import "./App.tsx";
// // import  Index  from "./screens/Index.tsx";
// import App from "./App";
//
// // const app = document.getElementById("app");
// // console.log(app);
// // if(app==null) throw new Error("No app element");
// const root = ReactDOM.createRoot(
//     document.getElementById('root') as HTMLElement
// )
// root.render(
//     <React.StrictMode>
//         <App />
//     </React.StrictMode>
// );

// const root = ReactDOMClient.createRoot(app);
// // root.render(<Index />);
// root.render(<App />);
