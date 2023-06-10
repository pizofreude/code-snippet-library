import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView textView = findViewById(R.id.textView);
        textView.setText("Hello, world!");
    }
}

// This is Java code that defines an Android activity that displays a "Hello, world!" message.

// The `import` statements import the necessary Android classes.

// The `public class MainActivity extends Activity` statement defines a new class that extends the `Activity` class.

// The `onCreate` method is called when the activity is created. It sets the content view to the layout defined in `activity_main.xml`.

// The `findViewById` method finds the `TextView` with ID `textView`.

// The `setText` method sets the text of the `TextView` to "Hello, world!".