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

--
-- Name: insert_timestamp_func(); Type: FUNCTION; Schema: public; Owner: user
--

CREATE FUNCTION public.insert_timestamp_func() RETURNS trigger
    LANGUAGE plpgsql
    AS $$ 
BEGIN
NEW."Timestamp" = NOW();
RETURN NEW;
END;
$$;


ALTER FUNCTION public.insert_timestamp_func() OWNER TO "user";

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: results; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.results (
    model_result integer,
    use_defined_result integer,
    "Timestamp" timestamp without time zone,
    id integer NOT NULL
);


ALTER TABLE public.results OWNER TO "user";

--
-- Name: results_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.results_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.results_id_seq OWNER TO "user";

--
-- Name: results_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.results_id_seq OWNED BY public.results.id;


--
-- Name: results id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.results ALTER COLUMN id SET DEFAULT nextval('public.results_id_seq'::regclass);


--
-- Data for Name: results; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.results (model_result, use_defined_result, "Timestamp", id) FROM stdin;
0	0	2025-02-27 15:06:33.839226	1
8	8	2025-02-27 15:07:19.074902	2
8	8	2025-02-27 15:07:20.903579	3
8	8	2025-02-27 15:07:23.62764	4
8	8	2025-02-27 15:07:25.529431	5
8	8	2025-02-27 15:07:26.218196	6
8	8	2025-02-27 15:07:26.520525	7
8	8	2025-02-27 15:07:26.741514	8
8	8	2025-02-27 15:07:27.249874	9
8	8	2025-02-27 15:07:27.629054	10
3	2	2025-02-27 15:07:48.250099	11
3	2	2025-02-27 15:07:51.10805	12
3	3	2025-02-27 15:08:00.746456	13
3	3	2025-02-27 15:08:02.111903	14
3	3	2025-02-27 15:08:03.279163	15
3	3	2025-02-27 15:08:04.133465	16
6	4	2025-02-27 15:08:15.104298	17
6	4	2025-02-27 15:08:16.558011	18
8	6	2025-02-27 15:08:27.399802	19
8	6	2025-02-27 15:08:28.760979	20
8	1	2025-02-27 17:03:24.230591	21
8	1	2025-02-27 17:06:15.613502	22
8	1	2025-02-27 17:11:27.719015	23
8	1	2025-02-27 17:11:29.568071	24
1	1	2025-02-27 17:11:32.230317	25
1	1	2025-02-27 17:11:34.03892	26
8	0	2025-02-27 17:11:55.923101	27
6	4	2025-02-27 17:17:32.341038	28
6	4	2025-02-27 17:21:51.734398	29
6	4	2025-02-27 17:22:13.682382	30
6	4	2025-02-27 17:24:15.790451	31
8	6	2025-02-27 17:24:56.797825	32
8	6	2025-02-27 17:25:41.851777	33
1	6	2025-02-27 17:32:41.285955	34
1	6	2025-02-27 17:33:18.191118	35
1	5	2025-02-28 16:45:17.234521	36
1	5	2025-02-28 16:47:07.632966	37
1	5	2025-02-28 16:48:43.196741	38
1	6	2025-02-28 16:53:07.610676	39
1	6	2025-02-28 17:00:29.573165	40
8	5	2025-02-28 17:00:43.70653	41
8	5	2025-02-28 17:03:23.042994	42
8	5	2025-02-28 17:03:31.64877	43
1	5	2025-02-28 17:07:53.423779	44
1	5	2025-02-28 17:07:56.415417	45
5	5	2025-02-28 17:08:32.120858	46
8	6	2025-02-28 17:09:09.122328	47
8	7	2025-02-28 17:11:50.228118	48
8	7	2025-02-28 17:12:57.129254	49
8	8	2025-02-28 17:14:19.300263	50
8	8	2025-02-28 17:14:34.940617	51
8	8	2025-02-28 17:14:50.710482	52
9	1	2025-02-28 17:15:23.241639	53
9	1	2025-02-28 17:16:37.209801	54
9	1	2025-02-28 17:18:36.095971	55
6	1	2025-02-28 17:21:40.486955	56
6	1	2025-02-28 17:22:57.42764	57
6	1	2025-02-28 17:24:33.016889	58
8	2	2025-02-28 17:27:10.473962	59
8	2	2025-02-28 17:29:58.92462	60
0	1	2025-02-28 17:45:16.48798	61
0	1	2025-02-28 17:45:34.762414	62
0	1	2025-02-28 17:47:49.693555	63
3	2	2025-02-28 17:48:38.824681	64
3	3	2025-02-28 17:49:25.297948	65
9	0	2025-02-28 17:50:10.599038	66
8	1	2025-02-28 17:51:25.166601	67
4	4	2025-02-28 17:52:27.131332	68
5	5	2025-02-28 17:53:35.622749	69
8	6	2025-02-28 17:55:17.058922	70
2	7	2025-02-28 17:57:40.716123	71
6	6	2025-02-28 17:59:43.191935	72
8	8	2025-02-28 18:02:43.631732	73
0	1	2025-02-28 18:04:14.531053	74
3	9	2025-02-28 18:07:17.287481	75
\.


--
-- Name: results_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.results_id_seq', 75, true);


--
-- Name: results results_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_pkey PRIMARY KEY (id);


--
-- Name: results set_timestamp; Type: TRIGGER; Schema: public; Owner: user
--

CREATE TRIGGER set_timestamp BEFORE INSERT ON public.results FOR EACH ROW EXECUTE FUNCTION public.insert_timestamp_func();


--
-- PostgreSQL database dump complete
--

