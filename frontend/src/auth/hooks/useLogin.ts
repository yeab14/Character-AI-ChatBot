import axios from "axios";
import { useMutation } from "react-query";

interface LoginParams {
  email: string;
  password: string;
}

const login = async ({ email, password }: LoginParams): Promise<string> => {
  try {
    const { data } = await axios.post("/api/login", { email, password });
    return data;
  } catch (error) {
    // Handle errors here (e.g., network issues, invalid credentials)
    throw new Error("Login failed. Please check your credentials and try again.");
  }
};

export function useLogin() {
  const { isLoading, mutateAsync } = useMutation(login, {
    onError: (error: any) => {
      // Optionally, handle global errors here
      console.error(error.message);
    }
  });

  return { isLoggingIn: isLoading, login: mutateAsync };
}

