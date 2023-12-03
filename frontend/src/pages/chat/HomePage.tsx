import React, { useState } from 'react';
import Chat from './Chat'; // Import your Chat component
import ToggleableChat from './ToggleableChat';

const HomePage: React.FC = () => {

  return (
    <div>

      < ToggleableChat/>
    </div>
  );
};

export default HomePage;
