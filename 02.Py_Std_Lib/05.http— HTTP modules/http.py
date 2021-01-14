import http 
import http.client

connection = http.client.HTTPConnection('www.python.org', 80, timeout=10)
print(connection)

#print (http.HTTPStatus.OK == 200)
#print (http.HTTPStatus.OK.value)
#print (http.HTTPStatus.OK.phrase)
#print (http.HTTPStatus.OK.description)
#print (list(HTTPStatus))



"""
Code        Enum Name                       Details         
100         CONTINUE                        HTTP/1.1 RFC 7231, Section 6.2.1            
101         SWITCHING_PROTOCOLS             HTTP/1.1 RFC 7231, Section 6.2.2
102         PROCESSING                      WebDAV RFC 2518, Section 10.1
200         OK                              HTTP/1.1 RFC 7231, Section 6.3.1
201         CREATED                         HTTP/1.1 RFC 7231, Section 6.3.2
202         ACCEPTED                        HTTP/1.1 RFC 7231, Section 6.3.3
203         NON_AUTHORITATIVE_INFORMATION   HTTP/1.1 RFC 7231, Section 6.3.4
204         NO_CONTENT                      HTTP/1.1 RFC 7231, Section 6.3.5
205         RESET_CONTENT                   HTTP/1.1 RFC 7231, Section 6.3.6
206         PARTIAL_CONTENT                 HTTP/1.1 RFC 7233, Section 4.1
207         MULTI_STATUS                    WebDAV RFC 4918, Section 11.1
208         ALREADY_REPORTED                WebDAV Binding Extensions RFC 5842, Section 7.1 (Experimental)
226         IM_USED                         Delta Encoding in HTTP RFC 3229, Section 10.4.1
300         MULTIPLE_CHOICES                HTTP/1.1 RFC 7231, Section 6.4.1
301         MOVED_PERMANENTLY               HTTP/1.1 RFC 7231, Section 6.4.2
302         FOUND                           HTTP/1.1 RFC 7231, Section 6.4.3
303         SEE_OTHER                       HTTP/1.1 RFC 7231, Section 6.4.4
304         NOT_MODIFIED                    HTTP/1.1 RFC 7232, Section 4.1
305         USE_PROXY                       HTTP/1.1 RFC 7231, Section 6.4.5
307         TEMPORARY_REDIRECT              HTTP/1.1 RFC 7231, Section 6.4.7
308         PERMANENT_REDIRECT              Permanent Redirect RFC 7238, Section 3 (Experimental)
400         BAD_REQUEST                     HTTP/1.1 RFC 7231, Section 6.5.1
401         UNAUTHORIZED                    HTTP/1.1 Authentication RFC 7235, Section 3.1
402         PAYMENT_REQUIRED                HTTP/1.1 RFC 7231, Section 6.5.2
403         FORBIDDEN                       HTTP/1.1 RFC 7231, Section 6.5.3
404         NOT_FOUND                       HTTP/1.1 RFC 7231, Section 6.5.4
405         METHOD_NOT_ALLOWED              HTTP/1.1 RFC 7231, Section 6.5.5
406         NOT_ACCEPTABLE                  HTTP/1.1 RFC 7231, Section 6.5.6
407         PROXY_AUTHENTICATION_REQUIRED   HTTP/1.1 Authentication RFC 7235, Section 3.2
408         REQUEST_TIMEOUT                 HTTP/1.1 RFC 7231, Section 6.5.7
409         CONFLICT                        HTTP/1.1 RFC 7231, Section 6.5.8
410         GONE                            HTTP/1.1 RFC 7231, Section 6.5.9
411         LENGTH_REQUIRED                 HTTP/1.1 RFC 7231, Section 6.5.10
412         PRECONDITION_FAILED             HTTP/1.1 RFC 7232, Section 4.2
413         REQUEST_ENTITY_TOO_LARGE        HTTP/1.1 RFC 7231, Section 6.5.11
414         REQUEST_URI_TOO_LONG            HTTP/1.1 RFC 7231, Section 6.5.12
415         UNSUPPORTED_MEDIA_TYPE          HTTP/1.1 RFC 7231, Section 6.5.13
416         REQUESTED_RANGE_NOT_SATISFIABLE HTTP/1.1 Range Requests RFC 7233, Section 4.4
417         EXPECTATION_FAILED              HTTP/1.1 RFC 7231, Section 6.5.14
421         MISDIRECTED_REQUEST             HTTP/2 RFC 7540, Section 9.1.2
422         UNPROCESSABLE_ENTITY            WebDAV RFC 4918, Section 11.2
423         LOCKED                          WebDAV RFC 4918, Section 11.3
424         FAILED_DEPENDENCY               WebDAV RFC 4918, Section 11.4
426         UPGRADE_REQUIRED                HTTP/1.1 RFC 7231, Section 6.5.15
428         PRECONDITION_REQUIRED           Additiona   HTTP Status Codes RFC 6585
429         TOO_MANY_REQUESTS               Additiona   HTTP Status Codes RFC 6585
431         REQUEST_HEADER_FIELDS_TOO_LARGE Additiona   HTTP Status Codes RFC 6585
451         UNAVAILABLE_FOR_LEGAL_REASONS   A   HTTP Status Code to Report Legal Obstacles RFC 7725
500         INTERNAL_SERVER_ERROR           HTTP/1.1 RFC 7231, Section 6.6.1
501         NOT_IMPLEMENTED                 HTTP/1.1 RFC 7231, Section 6.6.2
502         BAD_GATEWAY                     HTTP/1.1 RFC 7231, Section 6.6.3
503         SERVICE_UNAVAILABLE             HTTP/1.1 RFC 7231, Section 6.6.4
504         GATEWAY_TIMEOUT                 HTTP/1.1 RFC 7231, Section 6.6.5        
505         HTTP_VERSION_NOT_SUPPORTED      HTTP/1.1 RFC 7231, Section 6.6.6
506         VARIANT_ALSO_NEGOTIATES         Transparent Content Negotiation i   HTTP RFC 2295, Section 8.1 (Experimental)
507         INSUFFICIENT_STORAGE            WebDAV RFC 4918, Section 11.5
508         LOOP_DETECTED                   WebDAV Binding Extensions RFC 5842, Section 7.2 (Experimental)
510         NOT_EXTENDED                    A   HTTP Extension Framework RFC 2774, Section 7 (Experimental)
511         NETWORK_AUTHENTICATION_REQUIRED         Additiona   HTTP Status Codes RFC 6585, Section 6
"""