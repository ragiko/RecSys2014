package org.eswc2014.challenge.lodrecsys.sparql;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;

import com.hp.hpl.jena.query.Query;
import com.hp.hpl.jena.query.QueryExecution;
import com.hp.hpl.jena.query.QueryExecutionFactory;
import com.hp.hpl.jena.query.QueryFactory;
import com.hp.hpl.jena.query.QuerySolution;
import com.hp.hpl.jena.query.ResultSet;
import com.hp.hpl.jena.rdf.model.RDFNode;
import com.ibm.icu.util.StringTokenizer;

public class QueryExecutor {

	private String resource;
	String property;
	private String endpoint = "http://dbpedia.org/sparql";
	private String graphURI = "http://dbpedia.org";

	public String exec(String resource, String prop) {
		this.resource = resource;
		this.property = prop;
		Query query;
		String q;

		String resourceQuery = "<" + resource + ">";
		String propQuery = "<" + prop + ">";
		// creation of a sparql query for getting all the resources connected to
		// resource
		// the FILTER isIRI is used to get only resources, so this query
		// descards any literal or data-type

		q = "SELECT ?o WHERE { " + resourceQuery + " " + propQuery + " ?o. }";

		try {
			query = QueryFactory.create(q);

			return execQuery(query);
		} catch (Exception ex) {
			ex.printStackTrace();
		}
		
		return "";

	}

	public void exec(String resource) {
		this.resource = resource;
		Query query;
		String q;

		String resourceQuery = "<" + resource + ">";
		// creation of a sparql query for getting all the resources connected to
		// resource
		// the FILTER isIRI is used to get only resources, so this query
		// descards any literal or data-type

		q = " SELECT * WHERE {{" + " ?s ?p " + resourceQuery + ".   "
				+ "FILTER isIRI(?s). " + " } UNION {" + resourceQuery
				+ " ?p ?o " + "FILTER isIRI(?o). " + "}}";
		try {
			query = QueryFactory.create(q);

			
		} catch (Exception ex) {
			ex.printStackTrace();
		}

	}

	private String execQuery(Query query) {

		QueryExecution qexec = null;
		try {
			if (graphURI == null)
				qexec = QueryExecutionFactory.sparqlService(endpoint, query);
			else
				qexec = QueryExecutionFactory.sparqlService(endpoint, query,
						graphURI);

			ResultSet results = qexec.execSelect();

			QuerySolution qs;
			RDFNode node, prop;

			String n = "", p = this.property;

			// iteration over the resultset
			while (results.hasNext()) {

				qs = results.next();

				if (qs.contains("p")) {
					prop = qs.get("p"); // get the predicate of the triple
					p = prop.toString();
					p = p.replace("<", "");
					p = p.replace(">", "");

				}
				if (qs.get("o") == null) {
					node = qs.get("s"); // get the subject of the triple
					n = node.toString();
					n = n.replace("<", "");
					n = n.replace(">", "");

					System.out.println(n + '\t' + p + '\t' + resource);
				} else {

					node = qs.get("o"); // get the object of the triple
					n = node.toString();
					n = n.replace("<", "");
					n = n.replace(">", "");

					return n;
					//System.out.println(n);

				}

			}

		} finally {
			qexec.close();
		}
		
		return "";

	}

	public static void main(String[] args) {


		
	
		// ファイルを読み込む
		try {
			String path = "/Users/tag/programing/RecSys2014_re/DBbook/DBbook_Items_DBpedia_mapping_no_col.tsv";
			BufferedReader br = new BufferedReader(new FileReader(path));

			String line;
			QueryExecutor exec = new QueryExecutor();
			
			while ((line = br.readLine()) != null) {
				String[] r = line.split("\t");
				String url = r[2];
				
				String s = exec.exec(url, "http://dbpedia.org/ontology/abstract");
				System.out.println(r[0] + "\t" + r[1] + "\t" + r[2] + "\t" + s);
				
			}

			// 終了処理
			br.close();
		} catch (Exception e) {
			// TODO: handle exception
		}

	}
}
