import React, {useState} from "react";
import axios from "axios";
import "./style.css";
import {respond} from "./type.ts";
import Messages from "./Messages.tsx";


 const Index = () => {
    const [responses, setResponses] = useState<respond[]>([]);
    const [chatHistory, setChatHistory] = useState<string[]>([]);
    const [currentMessage, setCurrentMessage] = useState<string>("");
    const handleMessageSubmit = (message: string) => {
    const data = {
        question:message,
        id:chatHistory.length > 0 ? chatHistory[chatHistory.length] : []
    };
    console.log(data);

    axios
        .get(" http://localhost:3001/text_to_SQL")
        .then((response:any) => {
            const responseData = {
                text : response,
                isBot : true
            };
            setResponses(responses=>[...responses, responseData]);
            setChatHistory(chatHistory=>response.data["id"]);
            console.log("response", response);
        })
        .catch((error:any) => {
            console.log("error", error);
        })

}

  const handleMessageChange = (event:React.ChangeEvent<HTMLInputElement>) => {
    setCurrentMessage(event.target.value);
  };

    const handleSubmit = (event:React.KeyboardEvent) => {
    const message = {
      text: currentMessage,
      isBot: false
    };
    if (event.key === "Enter") {
      setResponses(responses => [...responses, message]);
      handleMessageSubmit(message.text);
      setCurrentMessage("");
    }
  };

  return (
    <div className="index">
      <div className="div">
        <div className="overlap-group">
          <div className="text-wrapper">Travel Agent</div>
        </div>
            <Messages messages={responses} />
        <div className="frame">
          <input
              className="enter-input"
              value={currentMessage}
              onChange={handleMessageChange}
              onKeyDown={handleSubmit}
              placeholder={"Enter your message"}
          /><button className="button">send</button>
        </div>
      </div>
    </div>
  );
};
 export default Index;
