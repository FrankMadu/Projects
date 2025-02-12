import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class Task {
    @Id
    private Long id;
    private String title;
    private String description;
    private boolean completed;

    // Getters and setters
}
