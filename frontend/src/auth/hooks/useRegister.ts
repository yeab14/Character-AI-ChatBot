import axios from "axios";
import { useMutation } from "react-query";
import { RegisterInfo } from "../types/registerInfo";

const register = async (userInfo: RegisterInfo): Promise<RegisterInfo> => {
  try {
    const { data } = await axios.post("/api/register", userInfo);
    return data;
  } catch (error) {
    // Handle error in registration
    throw new Error(error.response?.data?.message || "Registration failed");
  }
};

export function useRegister() {
  const { isLoading, mutateAsync } = useMutation(register);
  return { isRegistering: isLoading, register: mutateAsync };
}
