FROM node:21.7.3-bullseye-slim
WORKDIR /app
COPY . .
RUN npm install --omit=dev
EXPOSE 5173
ENTRYPOINT ["npm", "run", "docker"]