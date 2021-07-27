import React from 'react';
import './App.css';
import { AttackPage } from './Pages/AttackPage';
import { Show } from './Pages/Show';
import {
  BrowserRouter as Router, Switch, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path='/'>
            <AttackPage/>
          </Route>
          <Route path='/:id'>
            <Show/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App; 