--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2 (Debian 17.2-1.pgdg120+1)
-- Dumped by pg_dump version 17.2 (Debian 17.2-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: results; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.results (
    actual_result integer,
    predicted_result integer,
    "Timestamp" timestamp without time zone
);


ALTER TABLE public.results OWNER TO "user";

--
-- Data for Name: results; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.results (actual_result, predicted_result, "Timestamp") FROM stdin;
\.


--
-- PostgreSQL database dump complete
--

