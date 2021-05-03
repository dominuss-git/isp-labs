import { useState, useCallback } from 'react';

export const useHttp = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const request = useCallback(async (url, method = 'GET', body = null, headers = {}) => {
    setLoading(true);

    url = `http://192.168.31.5:8000/api${url}/`;

    try {
      if (body) {
        body = JSON.stringify(body);
        headers['Content-Type'] = 'application/json';
      }

      const response = await fetch(url, {
        method,
        body,
        headers,
      });

      const data = { body: await response.json(), status: await response.status };

      setLoading(false);
      return data;
    } catch (e) {
      throw e;
    }
  }, []);

  const clearError = useCallback(() => setError(null), []);

  return {
    loading, request, error, clearError,
  };
};
