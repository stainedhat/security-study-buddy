FROM node:18-alpine AS builder

ENV NODE_ENV production

WORKDIR /app

COPY study_app/package.json ./
RUN npm install

COPY study_app .
RUN npm rebuild esbuild
RUN npm run build
RUN ls -lah

FROM nginx
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf