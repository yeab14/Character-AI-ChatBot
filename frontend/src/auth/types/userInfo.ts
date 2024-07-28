
// src/auth/types/userInfo.ts
export interface UserInfo {
  email: string;
  firstName: string;
  lastName: string;
  password: string;
  id: string;
  avatar?: string;
  job: string;
  progress: number;
  role: string;
}
