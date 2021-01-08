import uvicorn

if __name__ == "__main__":
    uvicorn.run("src:app", debug=True,
                reload=True, port=8080,
                host="0.0.0.0", workers=2)