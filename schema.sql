CREATE TABLE articles (
    author integer NOT NULL,
    title text NOT NULL,
    slug text NOT NULL,
    lead text,
    body text,
    "time" timestamp with time zone DEFAULT now(),
    id integer NOT NULL
);

CREATE SEQUENCE articles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE articles_id_seq OWNED BY articles.id;

CREATE TABLE authors (
    name text NOT NULL,
    bio text,
    id integer NOT NULL
);

CREATE SEQUENCE authors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE authors_id_seq OWNED BY authors.id;

CREATE TABLE log (
    path text,
    ip inet,
    method text,
    status text,
    "time" timestamp with time zone DEFAULT now(),
    id integer NOT NULL
);

CREATE SEQUENCE log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE log_id_seq OWNED BY log.id;

ALTER TABLE ONLY articles ALTER COLUMN id SET DEFAULT nextval('articles_id_seq'::regclass);
ALTER TABLE ONLY authors ALTER COLUMN id SET DEFAULT nextval('authors_id_seq'::regclass);
ALTER TABLE ONLY log ALTER COLUMN id SET DEFAULT nextval('log_id_seq'::regclass);
