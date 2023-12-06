import React from "react";
import "./style.css";
import Message from "./Message";
import { respond } from "./type";
const Messages = ({messages=[]}:{messages:respond[]}) => {

  return (
    <div className="messagesSection">
          {Array.isArray(messages) && messages.map((message) => {
              return(
            <div className="messagesContainer">
            <Message message={message} />
          </div>
        );
      })}
    </div>
  );
};

export default Messages;