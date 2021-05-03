import { combineReducers } from 'redux';
import { appReducer } from './appReducer';
import { loginReducer } from './loginReducer';
import { depReducer } from './depReducer';
import { userReducer } from './userReducer';

export const rootReducer = combineReducers({
  app: appReducer,
  login: loginReducer,
  dep: depReducer,
  usr: userReducer,
});
