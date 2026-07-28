function Header({ siteName, count }) {

    return (

        <header
            style={{
                background: "#1565c0",
                color: "white",
                padding: "20px",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center"
            }}
        >

            <h2>{siteName}</h2>

            <nav>

                <a href="#" style={{ color: "white", marginRight: "20px" }}>Home</a>

                <a href="#" style={{ color: "white", marginRight: "20px" }}>Courses</a>

                <a href="#" style={{ color: "white", marginRight: "20px" }}>Profile</a>

            </nav>

            <h4>Enrolled : {count}</h4>

        </header>

    );

}

export default Header;
