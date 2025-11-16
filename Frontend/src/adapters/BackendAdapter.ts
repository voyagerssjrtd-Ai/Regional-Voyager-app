import { ChatBackend, Message } from "../types/chat";

const API_URL = "http://localhost:8000/chat"; // adjust if needed

export const BackendAdapter: ChatBackend = {
  sendMessage: async (content: string) => {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: content })
    });

    const data = await response.json();

    return {
      id: Date.now().toString(),
      role: "assistant",
      content: data.response,
      createdAt: new Date().toISOString(),
    };
  }
};
