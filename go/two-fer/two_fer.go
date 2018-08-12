package twofer

import (
	"fmt"
	"strings"
)

func ShareWith(name string) string {
	name = strings.TrimSpace(name)
	if len(name) == 0 {
		name = "you"
	}
	return fmt.Sprintf("One for %s, one for me.", name)
}
