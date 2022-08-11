
'''
   request_response_description_map : is a map of all the possble response types and what the responses signify 

'''
request_response_description_map = {    100 : 'continue',
                                        101 : 'switching_protocols',
                                        102 : 'processing',
                                        103 : 'checkpoint',
                                        122 : 'request_uri_too_long',
                                        200 : 'ok',
                                        201 : 'created',
                                        202 : 'accepted',
                                        203 : 'non_authoritative_information',
                                        204 : 'no_content',
                                        205 : 'reset_content, reset',
                                        206 : 'partial_content, partial',
                                        207 : 'multiple_status',
                                        208 : 'already_reported',
                                        226 : 'im_used',
                                        300 : 'multiple_choices',
                                        301 : 'moved_permanently',
                                        302 : 'found',
                                        303 : 'see_other',
                                        304 : 'not_modified',
                                        305 : 'use_proxy',
                                        306 : 'switch_proxy',
                                        307 : 'temporary_redirect',
                                        308 : 'permanent_redirect',
                                        400 : 'bad_request',
                                        401 : 'unauthorized',
                                        402 : 'payment_required',
                                        403 : 'forbidden',
                                        404 : 'not_found',
                                        405 : 'method_not_allowed',
                                        406 : 'not_acceptable',
                                        407 : 'proxy_authentication_required',
                                        408 : 'request_timeout',
                                        409 : 'conflict',
                                        410 : 'gone',
                                        411 : 'length_required',
                                        412 : 'precondition_failed',
                                        413 : 'request_entity_too_large',
                                        414 : 'request_uri_too_large',
                                        415 : 'unsupported_media_type',
                                        416 : 'requested_range_not_satisfiable',
                                        417 : 'expectation_failed',
                                        418 : 'im_a_teapot',
                                        421 : 'misdirected_request',
                                        422 : 'unprocessable_entity',
                                        423 : 'locked',
                                        424 : 'failed_dependency',
                                        425 : 'unordered_collection',
                                        426 : 'upgrade_required',
                                        428 : 'precondition_required',
                                        429 : 'too_many_requests',
                                        431 : 'header_fields_too_large',
                                        444 : 'no_response',
                                        449 : 'retry',
                                        450 : 'blocked_by_windows_parental_controls',
                                        451 : 'unavailable_for_legal_reasons',
                                        499 : 'client_closed_request',
                                        500 : 'internal_server_error',
                                        501 : 'not_implemented',
                                        502 : 'bad_gateway',
                                        503 : 'service_unavailable',
                                        504 : 'gateway_timeout',
                                        505 : 'http_version_not_supported',
                                        506 : 'variant_also_negotiates',
                                        507 : 'insufficient_storage',
                                        509 : 'bandwidth_limit_exceeded',
                                        510 : 'not_extended',
                                        511 : 'network_authentication_required'
                                    }