import time 
import asyncio
import websockets
import pytest
import allure

# Public Echo WebSocket server for secure (wss) real-time testing
WEBSOCKET_URI = "wss://ws.postman-echo.com/raw"

# TEST 1: Latency Measurement and Basic Functionality

# The @pytest.mark.asyncio decorator allows pytest to run this asynchronous (async) function
@pytest.mark.asyncio
@allure.title("Test 1: Check Connection and Latency Performance")
async def test_can_connect_and_measure_latency():
    
    # Save the precise start time before sending the message
    start_time = time.time()
    
    # Embed the timestamp in the message to verify it hasn't been altered during transit
    test_message = f"Hello Gemini QA Project, Sent at: {start_time}"

    # Establish the WebSocket connection
    async with websockets.connect(WEBSOCKET_URI) as websocket:
        
        await websocket.send(test_message) # Send the message
        response = await websocket.recv() # Receive the response (Echo) from the server
    
    # Calculate the Round Trip Time (RTT) in milliseconds
    end_time = time.time() 	
    latency_ms = (end_time - start_time) * 1000 
    
    # Assertion 1: Latency Check - Verify response time is below the set threshold (2000ms for external servers)
    assert latency_ms < 2000, f"Latency is too high: {latency_ms:.2f} ms"
    
    # Assertion 2: Functional Check - Verify the content returned is exactly the same as the original message
    assert response == test_message, "Received content does not match the sent content"
    
    print(f"Latency: {latency_ms:.2f} ms")


