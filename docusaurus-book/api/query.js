// docusaurus-book/api/query.js
import fetch from 'node-fetch';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    try {
      const { query, selected_text } = req.body;

      // Hugging Face API endpoint
      const API_URL = 'https://hf.space/embed/zartashakhan/physical-ai-backend/api/predict/';

      // Prepare payload
      const payload = { data: selected_text ? [query, selected_text] : [query] };

      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      const answer = data?.data?.[0] || 'Sorry, I could not find an answer.';

      res.status(200).json({ answer });
    } catch (err) {
      console.error(err);
      res.status(500).json({ answer: 'Sorry, server error occurred.' });
    }
  } else {
    res.status(405).json({ answer: 'Method not allowed' });
  }
}
