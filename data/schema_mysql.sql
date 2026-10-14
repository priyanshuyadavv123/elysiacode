-- =====================================================================
-- Elysia School - Production MySQL / MariaDB Database Schema
-- Optimized for High-Concurrency, Row-Level Locking & Zero-Lag Scaling
-- =====================================================================

-- 1. Create Database (if not already created)
-- CREATE DATABASE IF NOT EXISTS elysia_code CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- USE elysia_code;

-- 2. Users Table
CREATE TABLE IF NOT EXISTS users (
    id                  VARCHAR(64) PRIMARY KEY,
    username            VARCHAR(128) NOT NULL UNIQUE,
    name                VARCHAR(128) NOT NULL,
    email               VARCHAR(255) NOT NULL DEFAULT '',
    password_hash       VARCHAR(255) NOT NULL,
    avatar              LONGTEXT NOT NULL,
    motto               VARCHAR(255) NOT NULL DEFAULT '',
    xp                  INT NOT NULL DEFAULT 0,
    streak              INT NOT NULL DEFAULT 1,
    completed_subtopics LONGTEXT NOT NULL,
    today_seconds       INT NOT NULL DEFAULT 0,
    total_seconds       INT NOT NULL DEFAULT 0,
    created_at          VARCHAR(64) NOT NULL DEFAULT '',
    INDEX idx_users_username (username),
    INDEX idx_users_email (email),
    INDEX idx_users_xp (xp)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. Sessions Table (Stateful auth with cascade delete)
CREATE TABLE IF NOT EXISTS sessions (
    token_hash VARCHAR(64) PRIMARY KEY,
    user_id    VARCHAR(64) NOT NULL,
    created_at DOUBLE NOT NULL,
    expires_at DOUBLE NOT NULL,
    INDEX idx_sessions_user (user_id),
    INDEX idx_sessions_expires (expires_at),
    CONSTRAINT fk_sessions_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. Application Meta & Migrations Table
CREATE TABLE IF NOT EXISTS meta (
    `key`   VARCHAR(64) PRIMARY KEY,
    `value` LONGTEXT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
