import React, { useEffect, useRef, useState } from "react";
import { motion } from "framer-motion";
import { SendHorizonal } from "lucide-react";
import botAvatar from "../assets/bot.jpg";
import userAvatar from "../assets/user.jpg";
import logo from "../assets/logo.png";
import chatBackground from "../assets/chat-bg.jpg";

const ChatPage = () => {
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "👋Hello! Welcome to Metropolitan University’s Virtual Assistant.I'm here to help you with admissions, courses, campus services, and anything else you need. Just type your question, and I'll do my best to assist you. Let's make your journey at MU smooth and successful!",
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);
    setLoading(true);
    setInput("");

    try {
      const res = await fetch("http://localhost:8080/api/mubot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ msg: input }),
      });
      const data = await res.json();
      console.log(data);
      const botMsg = { sender: "bot", text: data.answer };
      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      console.error(err);
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "Something went wrong." },
      ]);
    }

    setLoading(false);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="min-h-screen bg-gradient-to-br from-gray-900 to-black flex flex-col items-center px-4 py-6 text-white"
    >
      <div className="w-full max-w-2xl bg-gray-800 rounded-2xl shadow-2xl flex flex-col overflow-hidden h-[90vh]">
        {/* Header */}
        <div className="bg-white flex gap-2 items-center text-stone-800 text-xl font-semibold p-4">
          <img src={logo} className=" h-10 rounded-full" alt="logo" />
          <div className="flex-col">
            {/* <p className="font-sans">MU ChatDesk</p>
            <p className="text-stone-400 text-sm">
              Your virtual university guide
            </p> */}
          </div>
        </div>

        {/* Chat Area */}
        <div
          className="flex-1 overflow-y-auto px-4 py-6 space-y-4"
          style={{
            backgroundImage: `url(${chatBackground})`,
            backgroundSize: "cover",
            backgroundPosition: "center",
          }}
        >
          {messages.map((msg, idx) => (
            <motion.div
              key={idx}
              initial={{ opacity: 0, x: msg.sender === "user" ? -40 : 40 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.3 }}
              className={`flex items-start gap-3 ${
                msg.sender === "user" ? "flex-row-reverse" : "flex-row"
              }`}
            >
              <img
                src={msg.sender === "user" ? userAvatar : botAvatar}
                alt="avatar"
                className="w-10 h-10 rounded-full shadow"
              />
              <div
                className={`rounded-xl px-4 py-2 text-sm max-w-sm shadow ${
                  msg.sender === "user"
                    ? "bg-gradient-to-br from-gray-950 to-blue-800 text-white"
                    : "bg-gradient-to-br from-gray-900 to-black text-white"
                }`}
              >
                {msg.text}
              </div>
            </motion.div>
          ))}
          {loading && (
            <div className="flex items-center gap-3">
              <img
                src={botAvatar}
                alt="bot"
                className="w-10 h-10 rounded-full shadow"
              />
              <div className="bg-gradient-to-br from-gray-900 to-black text-white px-4 py-2 rounded-xl shadow animate-pulse">
                Typing...
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <div className="px-4 py-3 bg-gray-900 flex items-center gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type your message..."
            className="flex-1 px-4 py-2 rounded-full bg-gray-700 border border-gray-600 text-white shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <motion.button
            onClick={sendMessage}
            whileTap={{ scale: 0.95 }}
            className="bg-gradient-to-br from-gray-900 to-black text-white px-4 py-2 rounded-full shadow hover:bg-gray-900 transition"
          >
            <SendHorizonal size={18} />
          </motion.button>
        </div>
      </div>
    </motion.div>
  );
};

export default ChatPage;
