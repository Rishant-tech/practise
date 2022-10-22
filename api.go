package main

import (
    "fmt"
    "log"
    "net/http"
)

func homePage(w http.ResponseWriter, r *http.Request){
    i := 1
	var j int
	var uName string
	for i>0{
		fmt.Scanln("\n1 : login\n2: register\n3 : Exit",&j)
		if j==1{
			fmt.Scanln("Enter your secret code : ",&uName)
			login(uName)
		}else if j==2{
			userID , code := register()
			fmt.Println("Your Secret code for login is : ",code)
			fmt.Println("Your userID : ",userID)
		}else if j==3{
			i=0
		}
	}
}

func handleRequests() {
    http.HandleFunc("/", homePage)
    log.Fatal(http.ListenAndServe(":8080", nil))
}

func main() {
    handleRequests()
}


package main

import (
	"fmt"
	"log"
    "os/exec"
	//"time"
	"math/rand"
	//"encoding/json"
	//"net/http"
	//"github.com/gin-gonic/gin"
)
func uID() []byte {
	newUUID, err := exec.Command("uuidgen").Output()
    if err != nil {
        log.Fatal(err)
    }
	return newUUID
}

func sCode(n int) string {
	var letters = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
 
    s := make([]rune, n)
    for i := range s {
        s[i] = letters[rand.Intn(len(letters))]
    }
    return string(s)
}

type user struct{
	ID 		string
	code 	string
	name 	string
	email 	string
	dob 	string
	list_of_diary_entries int
}
var u user

type entry struct{
	eID 	string
	date 	string
	title 	string
	content string
	time 	string
}
var e entry

/*func addEntry(){
	
}

func updateEntry()  {
	
}

func deleteEntry()  {
	
}

func showEntry()  {
	
}

func show_Dairy_Of_Month()  {
	
}*/

func login(uName string)  {
	/*if {
		i := 1
		var j int
		for i>0{
			fmt.Scanln("\n1 : Add Entry\n2 : Update Entry\n3 : Delete Entry\n4 : Show Entry\n5 : Show_Dairy_Of_Month\n6 : Logout",&j)
			if j==1{
				addEntry()
			}else if j==2{
				updateEntry()
			}else if j==3{
				deleteEntry()
			}else if j==4{
				showEntry()
			}else if j==5{
				show_Dairy_Of_Month()
			}else if j==6{
				i=0
			}
		}
	}else{
		fmt.Println("User Not Found!!")
	}*/
}

func register() (string,string) {
	var u user
	fmt.Scanln("Enter your Name : ",&u.name)
	fmt.Scanln("Enter your email : ",&u.email)
	fmt.Scanln("Enter your dob DD-MM-YYYY : ",&u.dob)
	return u.ID , u.code
}

func main()  {

	i := 1
	var j int
	var uName string
	for i>0{
		fmt.Scanln("\n1 : login\n2: register\n3 : Exit",&j)
		if j==1{
			fmt.Scanln("Enter your secret code : ",&uName)
			login(uName)
		}else if j==2{
			userID , code := register()
			fmt.Println("Your Secret code for login is : ",code)
			fmt.Println("Your userID : ",userID)
		}else if j==3{
			i=0
		}
	}
}