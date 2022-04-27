# flutter-conversational-ai
Example of using Stream's Webhook and Huggingface's DialoGPT to Chat with an AI

<p align="center">
  <img src="https://user-images.githubusercontent.com/18029834/165395252-4be9f42e-6710-490c-b0b8-5e6a02494e62.png" alt="Conversaional AI Stream Chat" />
</p>


## Quick Links

- [Register](https://getstream.io/chat/trial/) to get an API key for Stream Chat 🔑
- [Tutorial](https://getstream.io/blog/conversational-ai-flutter/) 📚
- [Chat UI Kit](https://getstream.io/chat/ui-kit/) 💄

## Repo Overview 😎

Flutter Conversational AI is an example project built to demo Stream's Webhook integration with other providers to build bot like applications.

This project contains two projects, a server implementation `server` built with Python and a minimal chat frontend `client` built with Flutter

This application listens for new user messages and sends a generated response based on previous responses, using [DialoGPT from Huggingface](https://huggingface.co/microsoft/DialoGPT-medium)



https://user-images.githubusercontent.com/18029834/165396359-71691ba0-b8c9-4379-a27b-d31a301676b4.mp4



## Requirements 🛠

Before running this project, please ensure you do the following:

- Flutter
- Python
- Ngrok for HTTP forwarding
- An account with Stream

## What is Stream?

Stream allows developers to rapidly deploy scalable feeds and chat messaging with an industry-leading 99.999% uptime SLA guarantee. With Stream’s chat components, developers can quickly add chat to their app for a variety of use-cases:

- Livestreams like Twitch or Youtube
- In-Game chat like Overwatch or Fortnite
- Team style chat like Slack
- Messaging style chat like Whatsapp or Facebook’s messenger

