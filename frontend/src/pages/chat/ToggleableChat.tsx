import React, { useState } from 'react';
import Chat from '../layout/Layout'; // Import your Chat component
import like2 from "../../assets/chat.png";

const ToggleableChat: React.FC = () => {
  const [isVisible, setIsVisible] = useState(false);

  const handleClick = () => {
    setIsVisible(!isVisible);
  };

  return (
    <div style={{ position: 'fixed', bottom: 0, right: 0, margin: '16px' }}>
      <div
        
        role="button"
        tabIndex={0}
        onClick={handleClick}
      >
        <img src={like2} style={{width: "30px", height: "30px"}} alt="Mic" />
      </div>
      {isVisible && <Chat />}
    </div>
  );
};

export default ToggleableChat;
