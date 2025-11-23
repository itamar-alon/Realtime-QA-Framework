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


# TEST 2: Multi-Client (Chat) Flow Simulation
@pytest.mark.asyncio
@allure.title("Test 2: Multi-Client Concurrent Chat Simulation")
async def test_multi_client_chat_flow():
    
    # Open two concurrent WebSocket connections (Client A and Client B)
    async with websockets.connect(WEBSOCKET_URI) as client_a, \
               websockets.connect(WEBSOCKET_URI) as client_b:
        
        # Round the timestamp to avoid assertion failures due to floating-point precision differences
        current_time = round(time.time(), 6) 
        message_from_a = f"Hello Client B, I am A. Time: {current_time}"

        # 1. Client A sends a message to the server
        await client_a.send(message_from_a)

        # 2. Use asyncio.gather to wait for both clients to receive the echo concurrently
        results = await asyncio.gather(
            client_a.recv(), # Response for Client A (should be its own echo)
            client_b.recv()  # Response for Client B (should be Client A's message)
        )
        
        client_a_response = results[0]
        client_b_response = results[1]

        # DEBUG
        print(f"\n DEBUG ")
        print(f"Sent: {message_from_a}")
        print(f"B Received: {client_b_response}")
        print(f"A Received: {client_a_response}")
        # END DEBUG
        
        # Assertion 1: Verify Client A received its own echo back
        assert client_a_response == message_from_a, "Client A did not receive the expected echo"
        
        # Assertion 2: Verify Client B received the message sent by Client A
        assert client_b_response == message_from_a, "Client B did not receive the chat message echo"