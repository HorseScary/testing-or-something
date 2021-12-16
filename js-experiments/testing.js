function show(content) {
    let things = [`
    <header>
    <h1>
    JavaScript Experiments
    </h1>
    </header>
    <nav>
    <a href="../index.html">
    Back
    </a>
    </nav>
    <hr>
    <main>
    <button onclick="show(1)">Thing 1</button>
    <button onclick="show(2)">Thing 2</button>
    </main>`,
    `
    <header>
    <h1>List</h1>
    </header>
    <ul>
    <li>this</li>
    <li>is</li>
    <li>a</li>
    <li>cool</li>
    <li>list</li>
    </ul>
    <button onclick="show(0)">Back</button>
    `,`
    <header>
    <h1>Horse Plinko</h1>
    </header>
    <img src="https://c.tenor.com/2go__Sq_LiwAAAAd/horse-plinko.gif">
    <button onclick="show(0)">Back</button>
    `];
    
    document.getElementById("content-container").innerHTML = things[content];
}