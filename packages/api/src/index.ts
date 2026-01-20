import express, { Request, Response } from 'express';

const app = express();
const PORT = process.env.PORT || 4000;

// CORS middleware for development
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});

// Health check endpoint
app.get('/health', (req: Request, res: Response) => {
    res.json({ status: 'ok' });
});

// Bridge endpoint - fetches from JSONPlaceholder
app.get('/api/albums', async (req: Request, res: Response) => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/albums');

        if (!response.ok) {
            throw new Error(`JSONPlaceholder returned ${response.status}`);
        }

        const albums = await response.json();
        res.json(albums);
    } catch (error) {
        console.error('Error fetching albums:', error);
        res.status(500).json({ error: 'Failed to fetch albums' });
    }
});

app.listen(PORT, () => {
    console.log(`API server running on port ${PORT}`);
});
