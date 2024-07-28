import { useState } from "react";
import axios from "axios";
import { UserInfo } from "../types/userInfo"; // Adjust the import path as necessary

const useRegister = () => {
  const [isRegistering, setIsRegistering] = useState(false);

  const register = async (userInfo: UserInfo) => {
    setIsRegistering(true);
    try {
      const response = await axios.post("/api/register", userInfo);
      return response.data;
    } catch (error) {
      console.error("Registration failed:", error);
      throw error;
    } finally {
      setIsRegistering(false);
    }
  };

  return { isRegistering, register };
};

export default useRegister;

