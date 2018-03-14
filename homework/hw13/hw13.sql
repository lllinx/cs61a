create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select a.name, b.size from dogs as a, sizes as b where height>min and height<=max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select parents.child from dogs, parents where dogs.name=parents.parent order by dogs.height desc;

-- Sentences about siblings that are the same size
create table sentences as
  with sibling(name1,name2,height1,height2) as (
    select a.child, b.child,c.height,d.height from parents as a, parents as b, dogs as c, dogs as d 
    where a.parent=b.parent and a.child<b.child and a.child=c.name and b.child=d.name
    )
  select name1 || " and " || name2 || " are " || f.size || " siblings" 
  from sibling as e, sizes as f where e.height1>f.min and e.height1<=f.max and e.height2>f.min and e.height2<=f.max;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  select a.name || ", " || b.name || ", " || c.name || ", " || d.name, a.height+b.height+c.height+d.height as total
  from dogs as a, dogs as b, dogs as c, dogs as d where total>170 and a.height<b.height and b.height<c.height and c.height<d.height
  order by total asc;

####how to create recursive local table#### 
-- create table stacks as
--   with stack(name,height) as (
--     select name, height from dogs union
--     select stack.name, dogs.name,  from stack, dogs where 
--     )

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
-- create table non_parents as
--   with gran(granparent,granchild) as (
--   select a.parent,b.child from parents as a, parents as b where a.child=b.parent
--   )
  

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
    select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table primes as
    select "REPLACE THIS LINE WITH YOUR SOLUTION";
