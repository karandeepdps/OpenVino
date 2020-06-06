def async_inference(exec_net, input_blob, image):
    '''
    Performs asynchronous inference
    Returns the `exec_net`
    '''
    exec_net.start_async(request_id=0, inputs={input_blob: image})
    while True:
        status = exec_net.requests[0].wait(-1)
        if status == 0:
            break
        else:
            time.sleep(1)
    return exec_net
