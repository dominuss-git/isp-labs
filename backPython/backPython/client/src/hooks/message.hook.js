import { useCallback } from 'react';
import { useDispatch } from 'react-redux';
import { showAlert } from '../redux/actions/app.actions';

export const useMessage = () => {
  const dispatch = useDispatch();
  return useCallback((text) => {
    dispatch(showAlert(text));
  }, []);
};
