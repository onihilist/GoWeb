package tests

import (
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/onihilist/WebAPI/pkg/routes"
	"github.com/stretchr/testify/assert"
)

func TestUserDetailLabel(t *testing.T) {

	router := routes.SetupRouter()
	username := "onhlt"

	w := httptest.NewRecorder()
	req, _ := http.NewRequest("GET", "/profile/"+username, nil)
	router.ServeHTTP(w, req)

	assert.Equal(t, http.StatusOK, w.Code)

	expectedLabel := `onhlt's Profile Details`
	assert.Contains(t, w.Body.String(), expectedLabel, "Response body should contain the expected label")

}
