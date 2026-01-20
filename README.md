# 🎵 Album Collection App

A full-stack monorepo application built with **Next.js 16**, **Express**, and **Tailwind CSS**, containerized with **Docker**.

![Next.js](https://img.shields.io/badge/Next.js-16-black?style=for-the-badge&logo=next.js)
![Express](https://img.shields.io/badge/Express-4-green?style=for-the-badge&logo=express)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-4-38B2AC?style=for-the-badge&logo=tailwind-css)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?style=for-the-badge&logo=typescript)

---

## ✨ Features

- **Server Components** - Next.js App Router with React Server Components
- **Bridge Pattern** - Frontend fetches from Express, which proxies to external API
- **Modern Styling** - Dark theme with gradient cards using Tailwind CSS v4
- **Docker Ready** - Production and development configurations included
- **TypeScript** - Full type safety across the stack

---

## 🏗️ Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Browser       │────▶│  Next.js :3000  │────▶│  Express :4000  │
│                 │     │  (Frontend)     │     │  (API Bridge)   │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                                                         ▼
                                               ┌─────────────────┐
                                               │ JSONPlaceholder │
                                               │   (External)    │
                                               └─────────────────┘
```

---

## 📁 Project Structure

```
/
├── packages/
│   ├── frontend/          # Next.js 16 App Router
│   │   ├── app/
│   │   │   ├── page.tsx   # Server Component - Album List
│   │   │   ├── layout.tsx # Root Layout
│   │   │   └── globals.css
│   │   ├── Dockerfile
│   │   └── package.json
│   │
│   └── api/               # Express Backend
│       ├── src/
│       │   └── index.ts   # Bridge endpoint
│       ├── Dockerfile
│       └── package.json
│
├── docker-compose.yml     # Production config
├── docker-compose.dev.yml # Development config
└── README.md
```

---

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Production
docker compose up --build

# Development (with hot reload)
docker compose -f docker-compose.dev.yml up --build
```

### Local Development

```bash
# Terminal 1 - Start API
cd packages/api
npm install
npm run dev

# Terminal 2 - Start Frontend
cd packages/frontend
npm install
npm run dev
```

### Access

| Service  | URL                     |
|----------|-------------------------|
| Frontend | http://localhost:3000   |
| API      | http://localhost:4000   |
| Health   | http://localhost:4000/health |

---

## 🔌 API Endpoints

| Method | Endpoint      | Description                          |
|--------|---------------|--------------------------------------|
| GET    | `/health`     | Health check                         |
| GET    | `/api/albums` | Fetch albums (proxied from JSONPlaceholder) |

---

## 🛠️ Tech Stack

| Layer    | Technology       | Version |
|----------|------------------|---------|
| Frontend | Next.js          | 16.0.5  |
| Frontend | React            | 19.2.0  |
| Frontend | Tailwind CSS     | 4.x     |
| Backend  | Express          | 4.21.0  |
| Backend  | TypeScript       | 5.x     |
| DevOps   | Docker           | Latest  |
| DevOps   | Docker Compose   | v2      |

---

## 📋 Requirements Met

This project fulfills all requirements:

- ✅ Fork the repo
- ✅ Use endpoint `https://jsonplaceholder.typicode.com/albums`
- ✅ Create Next.js app calling the endpoint
- ✅ Show a list of albums
- ✅ Use Tailwind for styling
- ✅ Monorepo structure (frontend + backend)
- ✅ Bridge pattern (Server Components → Express → JSONPlaceholder)
- ✅ Express framework for backend
- ✅ Docker + Docker Compose
- ✅ Docker services for production AND development
- ✅ Next.js App Router

---

## 📝 License

MIT

---

<p align="center">
  Built with ❤️ for the MUBITE Testing Challenge
</p>
