#!/usr/bin/env python3
"""
Unit tests for Python CLI File Manager TODO Tasks
Testing completion of TODO tasks in file_manager.py
Uses only unittest from standard library.
"""

import unittest
import sys
import os
import io
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import patch

# Import the modules
import file_manager
import cli


class TestFileManagerTODOTasks(unittest.TestCase):
    """Test cases specifically for TODO tasks in file_manager."""

    def test_display_welcome_blank_line_todo(self):
        """Test TODO: Add a blank line after the welcome message."""
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            cli.display_welcome()

        output = captured_output.getvalue()

        # Check if welcome message ends with a blank line
        # The output should end with two newlines (one from last print, one blank line)
        # Count the newlines - should be at least 6 (5 from prints + 1 blank line)
        newline_count = output.count('\n')
        ends_with_double_newline = output.endswith('\n\n')
        
        self.assertTrue(
            ends_with_double_newline and newline_count >= 6,
            f"TODO: Welcome message should end with a blank line. Got {newline_count} newlines, ends with double newline: {ends_with_double_newline}"
        )

    def test_format_file_size_algorithm_todo(self):
        """Test TODO: Students implement the conversion algorithm in format_file_size."""
        # Test if the format_file_size function works correctly
        try:
            # Test with various sizes
            result_1024 = file_manager.format_file_size(1024)
            result_1536 = file_manager.format_file_size(1536)
            result_1048576 = file_manager.format_file_size(1048576)
            
            # Check if function returns proper formatted strings (not undefined variables)
            self.assertIsInstance(result_1024, str, "format_file_size should return a string")
            self.assertNotEqual(result_1024, "Invalid size", "Should handle valid size correctly")
            
            # Check for floating point precision
            if "1.50" in result_1536:
                self.assertTrue(True, "Floating point division working in format_file_size")
            else:
                self.fail("TODO: Implement conversion algorithm with proper floating point division")
                
        except NameError as e:
            if "formatted_size" in str(e):
                self.fail("TODO: Implement the conversion algorithm - undefined variable 'formatted_size'")
            else:
                raise e

    def test_get_user_choice_return_todo(self):
        """Test TODO: Add code to return the choice."""
        with patch("builtins.input", return_value="help"):
            captured_output = io.StringIO()

            with redirect_stdout(captured_output):
                choice = cli.get_user_choice()

            # Check that function actually returns the choice (not None)
            self.assertIsNotNone(
                choice, "TODO: get_user_choice should return the choice"
            )
            self.assertEqual(
                choice, "help", "TODO: get_user_choice should return the correct choice"
            )

    def test_process_user_command_keyword_arguments_todo(self):
        """Test TODO: Set keyword arguments with default values."""
        # Test if function can be called with default arguments
        try:
            # This should work if default arguments are properly set
            result = cli.process_user_command("help", True)
            self.assertIsNotNone(result, "process_user_command should return a value")
        except TypeError as e:
            if "missing" in str(e) and "required positional argument" in str(e):
                self.fail(
                    "TODO: Set default values for keyword arguments in process_user_command"
                )
            else:
                raise e

    def test_process_user_command_custom_keyword_args(self):
        """Test process_user_command with custom keyword arguments."""
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            # Test with custom goodbye message
            result = cli.process_user_command(
                "quit",
                True,
                show_goodbye=True,
                goodbye_message="Custom goodbye!",
                invalid_choice_prefix="Oops:",
                valid_commands="test commands",
            )

        output = captured_output.getvalue()
        self.assertIn("Custom goodbye!", output)
        self.assertFalse(result, "Should return False when quit is chosen")

    def test_process_user_command_invalid_choice_custom_message(self):
        """Test process_user_command with custom invalid choice message."""
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            result = cli.process_user_command(
                "invalid",
                True,
                show_goodbye=True,
                goodbye_message="Bye!",
                invalid_choice_prefix="Custom error:",
                valid_commands="custom, commands",
            )

        output = captured_output.getvalue()
        self.assertIn("Custom error:", output)
        self.assertIn("custom, commands", output)
        self.assertTrue(result, "Should return True for non-quit commands")

    @patch.object(cli, "display_welcome")
    def test_main_display_welcome_todo(self, mock_display_welcome):
        """Test TODO: Call the function to display the welcome message."""
        # Mock get_user_choice to return 'quit' immediately
        with patch.object(cli, "get_user_choice", return_value="quit"):
            with patch.object(cli, "process_user_command", return_value=False):
                try:
                    cli.main()
                except NameError:
                    # Expected if running variable is not initialized
                    pass

        # Check if display_welcome was called
        mock_display_welcome.assert_called_once()

    def test_main_running_variable_todo(self):
        """Test TODO: Initialize a variable to control the loop."""
        # This test checks if the main function can run without NameError
        with patch.object(cli, "get_user_choice", return_value="quit"):
            with patch.object(cli, "process_user_command", return_value=False):
                with patch.object(cli, "display_welcome"):
                    try:
                        cli.main()
                        # If we get here, the running variable was properly initialized
                        self.assertTrue(
                            True, "Running variable is properly initialized"
                        )
                    except NameError as e:
                        if "running" in str(e):
                            self.fail(
                                "TODO: Initialize running variable in main function"
                            )
                        else:
                            raise e

    def test_list_directory_tree_return_statements_todo(self):
        """Test TODO: Add return None statements in list_directory_tree base cases."""
        # Check if the source code has explicit "return None" statements
        import inspect
        
        try:
            source = inspect.getsource(file_manager.list_directory_tree)
            # Count explicit "return None" statements in the function
            explicit_returns = source.count("return None")
            
            # Should have at least 3 explicit return None statements for the base cases
            self.assertGreaterEqual(explicit_returns, 3, 
                f"TODO: Add explicit 'return None' statements to base cases. Found {explicit_returns}, need at least 3")
                
        except Exception as e:
            self.fail(f"Could not inspect source code: {e}")

    def test_find_files_by_extension_initialization_todo(self):
        """Test TODO: Initialize found_files as an empty list."""
        # Test if function handles invalid directory
        try:
            result = file_manager.find_files_by_extension("nonexistent_dir", ".txt")
            self.assertIsInstance(result, list, "Should return a list")
            self.assertEqual(result, [], "Should return empty list for invalid directory")
        except NameError as e:
            if "found_files" in str(e):
                self.fail("TODO: Initialize found_files as an empty list")
            else:
                raise e
        except UnboundLocalError as e:
            if "found_files" in str(e):
                self.fail("TODO: Initialize found_files as an empty list")
            else:
                raise e

    def test_find_files_by_extension_return_base_case_todo(self):
        """Test TODO: Return empty list for invalid directory base case."""
        result = file_manager.find_files_by_extension("nonexistent_directory_12345", ".py")
        self.assertIsInstance(result, list, "Should return a list")
        self.assertEqual(result, [], "TODO: Return empty list for invalid directory")

    def test_find_files_by_extension_recursive_call_todo(self):
        """Test TODO: Implement recursive call and extend found_files."""
        # Create a temporary directory structure for testing
        import tempfile
        import shutil
        
        temp_dir = tempfile.mkdtemp()
        try:
            # Create test files
            sub_dir = os.path.join(temp_dir, "subdir")
            os.makedirs(sub_dir)
            
            with open(os.path.join(temp_dir, "test1.py"), "w") as f:
                f.write("# test file")
            with open(os.path.join(sub_dir, "test2.py"), "w") as f:
                f.write("# another test file")
            
            # Test the function
            try:
                result = file_manager.find_files_by_extension(temp_dir, ".py")
                
                # Should find files in subdirectories too
                if len(result) >= 2:
                    self.assertTrue(True, "Recursive search working")
                else:
                    self.fail("TODO: Implement recursive call to search subdirectories")
                    
            except (NameError, UnboundLocalError) as e:
                if "found_files" in str(e):
                    self.fail("TODO: Initialize found_files and implement recursive extension")
                else:
                    raise e
                    
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def test_list_directory_tree_recursive_call_todo(self):
        """Test TODO: Perform recursive function call in list_directory_tree."""
        import tempfile
        import shutil
        import inspect
        
        # First check if the source code has the recursive function call
        try:
            source = inspect.getsource(file_manager.list_directory_tree)
            
            # Look for the recursive function call pattern
            has_recursive_call = ("list_directory_tree(" in source and 
                                "item_path" in source and 
                                "next_prefix" in source)
            
            if not has_recursive_call:
                self.fail("TODO: Add recursive function call: list_directory_tree(item_path, next_prefix, max_depth, current_depth + 1)")
            
            # Also test that it actually works with deeply nested directories
            temp_dir = tempfile.mkdtemp()
            try:
                # Create nested structure: temp_dir/sub1/sub2/file.txt
                sub1 = os.path.join(temp_dir, "sub1")
                sub2 = os.path.join(sub1, "sub2")
                os.makedirs(sub2)
                with open(os.path.join(sub2, "deep_file.txt"), "w") as f:
                    f.write("test")
                
                captured_output = io.StringIO()
                with redirect_stdout(captured_output):
                    file_manager.list_directory_tree(temp_dir, max_depth=3)
                
                output = captured_output.getvalue()
                
                # Should show nested structure if recursive call is implemented
                if not ("sub1/" in output and "sub2/" in output and "deep_file.txt" in output):
                    self.fail("TODO: Recursive call not working properly - should show nested directory structure")
                    
            finally:
                shutil.rmtree(temp_dir, ignore_errors=True)
                
        except Exception as e:
            self.fail(f"Could not test recursive call: {e}")

    def test_todo_completion_summary(self):
        """Summary test showing which TODO tasks are completed vs pending."""
        todo_status = {
            "display_welcome_blank_line": False,
            "format_file_size_algorithm": False,
            "get_user_choice_return": False,
            "process_user_command_defaults": False,
            "main_display_welcome_call": False,
            "main_running_variable": False,
            "list_directory_tree_return_statements": False,
            "find_files_initialization": False,
            "find_files_return_base_case": False,
            "find_files_recursive_call": False,
            "list_directory_recursive_call": False,
        }

        # Test 1: Welcome blank line
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            cli.display_welcome()
        if captured_output.getvalue().endswith("\n\n"):
            todo_status["display_welcome_blank_line"] = True

        # Test 2: Return statement in get_user_choice
        with patch("builtins.input", return_value="test"):
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                result = cli.get_user_choice()
            if result is not None:
                todo_status["get_user_choice_return"] = True

        # Test 3: Format file size algorithm
        try:
            result = file_manager.format_file_size(1536)
            if isinstance(result, str) and "1.50" in result:
                todo_status["format_file_size_algorithm"] = True
        except (NameError, UnboundLocalError):
            pass

        # Test 4: Default arguments in process_user_command
        try:
            cli.process_user_command("help", True)
            todo_status["process_user_command_defaults"] = True
        except TypeError:
            pass

        # Test 5: Display welcome call in main
        with patch.object(cli, "display_welcome") as mock_welcome:
            with patch.object(cli, "get_user_choice", return_value="quit"):
                with patch.object(cli, "process_user_command", return_value=False):
                    try:
                        cli.main()
                        if mock_welcome.called:
                            todo_status["main_display_welcome_call"] = True
                    except (NameError, UnboundLocalError):
                        pass

        # Test 6: Running variable initialization
        with patch.object(cli, "get_user_choice", return_value="quit"):
            with patch.object(cli, "process_user_command", return_value=False):
                with patch.object(cli, "display_welcome"):
                    try:
                        cli.main()
                        todo_status["main_running_variable"] = True
                    except (NameError, UnboundLocalError):
                        pass

        # Test 7: List directory tree return statements
        # Check if the source code has explicit "return None" statements
        try:
            import inspect
            source = inspect.getsource(file_manager.list_directory_tree)
            explicit_returns = source.count("return None")
            if explicit_returns >= 3:
                todo_status["list_directory_tree_return_statements"] = True
        except:
            pass

        # Test 8: Find files initialization
        try:
            result = file_manager.find_files_by_extension("nonexistent_dir", ".txt")
            if isinstance(result, list):
                todo_status["find_files_initialization"] = True
        except (NameError, UnboundLocalError):
            pass

        # Test 9: Find files return base case
        result = file_manager.find_files_by_extension("nonexistent_dir", ".py")
        if isinstance(result, list) and result == []:
            todo_status["find_files_return_base_case"] = True

        # Test 10: Find files recursive call (basic test)
        import tempfile
        import shutil
        temp_dir = tempfile.mkdtemp()
        try:
            sub_dir = os.path.join(temp_dir, "sub")
            os.makedirs(sub_dir)
            with open(os.path.join(sub_dir, "test.py"), "w") as f:
                f.write("test")
            
            try:
                result = file_manager.find_files_by_extension(temp_dir, ".py")
                if len(result) > 0:
                    todo_status["find_files_recursive_call"] = True
            except (NameError, UnboundLocalError):
                pass
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

        # Test 11: List directory recursive call (basic test)
        try:
            import inspect
            source = inspect.getsource(file_manager.list_directory_tree)
            # Look for the recursive function call pattern
            if "list_directory_tree(" in source and "item_path" in source and "next_prefix" in source:
                # Also test that it actually works with nested directories
                temp_dir = tempfile.mkdtemp()
                try:
                    # Create nested structure
                    sub1 = os.path.join(temp_dir, "sub1")
                    sub2 = os.path.join(sub1, "sub2")
                    os.makedirs(sub2)
                    with open(os.path.join(sub2, "deep_file.txt"), "w") as f:
                        f.write("test")
                    
                    captured_output = io.StringIO()
                    with redirect_stdout(captured_output):
                        file_manager.list_directory_tree(temp_dir, max_depth=3)
                    
                    output = captured_output.getvalue()
                    if "sub1/" in output and "sub2/" in output and "deep_file.txt" in output:
                        todo_status["list_directory_recursive_call"] = True
                finally:
                    shutil.rmtree(temp_dir, ignore_errors=True)
        except:
            pass

        # Print summary for students
        completed = sum(todo_status.values())
        total = len(todo_status)

        print(f"\n=== TODO TASK COMPLETION SUMMARY ===")
        print(f"Completed: {completed}/{total} tasks")
        print("\nTask Status:")
        for task, completed in todo_status.items():
            status = "✓ DONE" if completed else "✗ TODO"
            print(f"  {task}: {status}")

        if completed == total:
            print("\n🎉 All TODO tasks completed! Great work!")
        else:
            print(f"\n📝 {total - completed} TODO tasks remaining.")

        # This test always passes - it's just for information
        self.assertTrue(True)

    def test_todo_hints_and_solutions(self):
        """Provides hints for completing each TODO task."""
        # First, check which tasks are completed (same logic as summary test)
        todo_status = {
            "display_welcome_blank_line": False,
            "format_file_size_algorithm": False,
            "get_user_choice_return": False,
            "process_user_command_defaults": False,
            "main_display_welcome_call": False,
            "main_running_variable": False,
            "list_directory_tree_return_statements": False,
            "find_files_initialization": False,
            "find_files_return_base_case": False,
            "find_files_recursive_call": False,
            "list_directory_recursive_call": False,
        }

        # Test 1: Welcome blank line
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            cli.display_welcome()
        if captured_output.getvalue().endswith("\n\n"):
            todo_status["display_welcome_blank_line"] = True

        # Test 2: Return statement in get_user_choice
        with patch("builtins.input", return_value="test"):
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                result = cli.get_user_choice()
            if result is not None:
                todo_status["get_user_choice_return"] = True

        # Test 3: Format file size algorithm
        try:
            result = file_manager.format_file_size(1536)
            if isinstance(result, str) and "1.50" in result:
                todo_status["format_file_size_algorithm"] = True
        except (NameError, UnboundLocalError):
            pass

        # Test 4: Default arguments in process_user_command
        try:
            cli.process_user_command("help", True)
            todo_status["process_user_command_defaults"] = True
        except TypeError:
            pass

        # Test 5: Display welcome call in main
        with patch.object(cli, "display_welcome") as mock_welcome:
            with patch.object(cli, "get_user_choice", return_value="quit"):
                with patch.object(cli, "process_user_command", return_value=False):
                    try:
                        cli.main()
                        if mock_welcome.called:
                            todo_status["main_display_welcome_call"] = True
                    except (NameError, UnboundLocalError):
                        pass

        # Test 6: Running variable initialization
        with patch.object(cli, "get_user_choice", return_value="quit"):
            with patch.object(cli, "process_user_command", return_value=False):
                with patch.object(cli, "display_welcome"):
                    try:
                        cli.main()
                        todo_status["main_running_variable"] = True
                    except (NameError, UnboundLocalError):
                        pass

        # Test 7: List directory tree return statements
        # Check if the source code has explicit "return None" statements
        try:
            import inspect
            source = inspect.getsource(file_manager.list_directory_tree)
            explicit_returns = source.count("return None")
            if explicit_returns >= 3:
                todo_status["list_directory_tree_return_statements"] = True
        except:
            pass

        # Test 8: Find files initialization
        try:
            result = file_manager.find_files_by_extension("nonexistent_dir", ".txt")
            if isinstance(result, list):
                todo_status["find_files_initialization"] = True
        except (NameError, UnboundLocalError):
            pass

        # Test 9: Find files return base case
        result = file_manager.find_files_by_extension("nonexistent_dir", ".py")
        if isinstance(result, list) and result == []:
            todo_status["find_files_return_base_case"] = True

        # Test 10: Find files recursive call (basic test)
        import tempfile
        import shutil
        temp_dir = tempfile.mkdtemp()
        try:
            sub_dir = os.path.join(temp_dir, "sub")
            os.makedirs(sub_dir)
            with open(os.path.join(sub_dir, "test.py"), "w") as f:
                f.write("test")
            
            try:
                result = file_manager.find_files_by_extension(temp_dir, ".py")
                if len(result) > 0:
                    todo_status["find_files_recursive_call"] = True
            except (NameError, UnboundLocalError):
                pass
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

        # Test 11: List directory recursive call (basic test)
        try:
            import inspect
            source = inspect.getsource(file_manager.list_directory_tree)
            # Look for the recursive function call pattern
            if "list_directory_tree(" in source and "item_path" in source and "next_prefix" in source:
                # Also test that it actually works with nested directories
                temp_dir = tempfile.mkdtemp()
                try:
                    # Create nested structure
                    sub1 = os.path.join(temp_dir, "sub1")
                    sub2 = os.path.join(sub1, "sub2")
                    os.makedirs(sub2)
                    with open(os.path.join(sub2, "deep_file.txt"), "w") as f:
                        f.write("test")
                    
                    captured_output = io.StringIO()
                    with redirect_stdout(captured_output):
                        file_manager.list_directory_tree(temp_dir, max_depth=3)
                    
                    output = captured_output.getvalue()
                    if "sub1/" in output and "sub2/" in output and "deep_file.txt" in output:
                        todo_status["list_directory_recursive_call"] = True
                finally:
                    shutil.rmtree(temp_dir, ignore_errors=True)
        except:
            pass

        # Map task names to hints
        hints = {
            "display_welcome_blank_line": ("cli.py - display_welcome() blank line", "Add: print() at the end of the function"),
            "format_file_size_algorithm": ("file_manager.py - format_file_size algorithm", "Implement loop with: while size >= divisor and unit_index < len(units) - 1"),
            "get_user_choice_return": ("cli.py - get_user_choice() return", "Add: return choice"),
            "process_user_command_defaults": ("cli.py - process_user_command() defaults", "Add default values like: show_goodbye=True, goodbye_message='Thank you...'"),
            "main_display_welcome_call": ("cli.py - main() display_welcome call", "Add: display_welcome()"),
            "main_running_variable": ("cli.py - main() running variable", "Add: running = True"),
            "list_directory_tree_return_statements": ("file_manager.py - list_directory_tree returns", "Add: return None after each base case print statement"),
            "find_files_initialization": ("file_manager.py - find_files initialization", "Add: found_files = [] at the beginning"),
            "find_files_return_base_case": ("file_manager.py - find_files base case return", "Replace 'pass' with: return []"),
            "find_files_recursive_call": ("file_manager.py - find_files recursive call", "Add: found_files.extend(find_files_by_extension(item_path, extension, sub_path))"),
            "list_directory_recursive_call": ("file_manager.py - list_directory recursive call", "Add: list_directory_tree(item_path, next_prefix, max_depth, current_depth + 1)"),
        }

        # Only show hints for incomplete tasks
        incomplete_tasks = [task for task, completed in todo_status.items() if not completed]
        
        if incomplete_tasks:
            print("\n=== TODO TASK HINTS (Incomplete Tasks Only) ===")
            for task in incomplete_tasks:
                if task in hints:
                    location, hint = hints[task]
                    print(f"\n{location}:")
                    print(f"  Hint: {hint}")
        else:
            print("\n🎉 All TODO tasks completed! No hints needed.")

        # This test always passes - it's just for information
        self.assertTrue(True)


def print_todo_summary():
    """Print the TODO completion summary."""
    # Import here to avoid circular imports
    import tempfile
    import shutil
    
    todo_status = {
        "display_welcome_blank_line": False,
        "format_file_size_algorithm": False,
        "get_user_choice_return": False,
        "process_user_command_defaults": False,
        "main_display_welcome_call": False,
        "main_running_variable": False,
        "list_directory_tree_return_statements": False,
        "find_files_initialization": False,
        "find_files_return_base_case": False,
        "find_files_recursive_call": False,
        "list_directory_recursive_call": False,
    }

    # Test 1: Welcome blank line
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli.display_welcome()
    if captured_output.getvalue().endswith("\n\n"):
        todo_status["display_welcome_blank_line"] = True

    # Test 2: Return statement in get_user_choice
    with patch("builtins.input", return_value="test"):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            result = cli.get_user_choice()
        if result is not None:
            todo_status["get_user_choice_return"] = True

    # Test 3: Format file size algorithm
    try:
        result = file_manager.format_file_size(1536)
        if isinstance(result, str) and "1.50" in result:
            todo_status["format_file_size_algorithm"] = True
    except (NameError, UnboundLocalError):
        pass

    # Test 4: Default arguments in process_user_command
    try:
        cli.process_user_command("help", True)
        todo_status["process_user_command_defaults"] = True
    except TypeError:
        pass

    # Test 5: Display welcome call in main
    with patch.object(cli, "display_welcome") as mock_welcome:
        with patch.object(cli, "get_user_choice", return_value="quit"):
            with patch.object(cli, "process_user_command", return_value=False):
                try:
                    cli.main()
                    if mock_welcome.called:
                        todo_status["main_display_welcome_call"] = True
                except (NameError, UnboundLocalError):
                    pass

    # Test 6: Running variable initialization
    with patch.object(cli, "get_user_choice", return_value="quit"):
        with patch.object(cli, "process_user_command", return_value=False):
            with patch.object(cli, "display_welcome"):
                try:
                    cli.main()
                    todo_status["main_running_variable"] = True
                except (NameError, UnboundLocalError):
                    pass

    # Test 7: List directory tree return statements
    # Check if the source code has explicit "return None" statements
    try:
        import inspect
        source = inspect.getsource(file_manager.list_directory_tree)
        # Count explicit "return None" statements in the function
        explicit_returns = source.count("return None")
        if explicit_returns >= 3:  # Should have at least 3 explicit return None statements
            todo_status["list_directory_tree_return_statements"] = True
    except:
        pass

    # Test 8: Find files initialization
    try:
        result = file_manager.find_files_by_extension("nonexistent_dir", ".txt")
        if isinstance(result, list):
            todo_status["find_files_initialization"] = True
    except (NameError, UnboundLocalError):
        pass

    # Test 9: Find files return base case
    try:
        result = file_manager.find_files_by_extension("nonexistent_dir", ".py")
        if isinstance(result, list) and result == []:
            todo_status["find_files_return_base_case"] = True
    except:
        pass

    # Test 10: Find files recursive call (basic test)
    temp_dir = tempfile.mkdtemp()
    try:
        sub_dir = os.path.join(temp_dir, "sub")
        os.makedirs(sub_dir)
        with open(os.path.join(sub_dir, "test.py"), "w") as f:
            f.write("test")
        
        try:
            result = file_manager.find_files_by_extension(temp_dir, ".py")
            if len(result) > 0:
                todo_status["find_files_recursive_call"] = True
        except (NameError, UnboundLocalError):
            pass
    except:
        pass
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    # Test 11: List directory recursive call (basic test)
    # Check if the source code has the actual recursive function call
    try:
        import inspect
        source = inspect.getsource(file_manager.list_directory_tree)
        # Look for the recursive function call pattern
        if "list_directory_tree(" in source and "item_path" in source and "next_prefix" in source:
            # Also test that it actually works with nested directories
            temp_dir = tempfile.mkdtemp()
            try:
                # Create nested structure: temp_dir/sub1/sub2/file.txt
                sub1 = os.path.join(temp_dir, "sub1")
                sub2 = os.path.join(sub1, "sub2")
                os.makedirs(sub2)
                with open(os.path.join(sub2, "deep_file.txt"), "w") as f:
                    f.write("test")
                
                captured_output = io.StringIO()
                with redirect_stdout(captured_output):
                    file_manager.list_directory_tree(temp_dir, max_depth=3)
                
                output = captured_output.getvalue()
                # Should show nested structure if recursive call is implemented
                if "sub1/" in output and "sub2/" in output and "deep_file.txt" in output:
                    todo_status["list_directory_recursive_call"] = True
            finally:
                shutil.rmtree(temp_dir, ignore_errors=True)
    except:
        pass

    # Print summary
    completed = sum(todo_status.values())
    total = len(todo_status)

    print(f"\n=== TODO TASK COMPLETION SUMMARY ===")
    print(f"Completed: {completed}/{total} tasks")
    print("\nTask Status:")
    for task, is_completed in todo_status.items():
        status = "✓ DONE" if is_completed else "✗ TODO"
        print(f"  {task}: {status}")

    if completed == total:
        print("\n🎉 All TODO tasks completed! Great work!")
    else:
        print(f"\n📝 {total - completed} TODO tasks remaining.")

    # Show hints for incomplete tasks
    hints = {
        "display_welcome_blank_line": ("cli.py - display_welcome() blank line", "Add: print() at the end of the function"),
        "format_file_size_algorithm": ("file_manager.py - format_file_size algorithm", "Implement loop with: while size >= divisor and unit_index < len(units) - 1"),
        "get_user_choice_return": ("cli.py - get_user_choice() return", "Add: return choice"),
        "process_user_command_defaults": ("cli.py - process_user_command() defaults", "Add default values like: show_goodbye=True, goodbye_message='Thank you...'"),
        "main_display_welcome_call": ("cli.py - main() display_welcome call", "Add: display_welcome()"),
        "main_running_variable": ("cli.py - main() running variable", "Add: running = True"),
        "list_directory_tree_return_statements": ("file_manager.py - list_directory_tree returns", "Add: return None after each base case print statement"),
        "find_files_initialization": ("file_manager.py - find_files initialization", "Add: found_files = [] at the beginning"),
        "find_files_return_base_case": ("file_manager.py - find_files base case return", "Replace 'pass' with: return []"),
        "find_files_recursive_call": ("file_manager.py - find_files recursive call", "Add: found_files.extend(find_files_by_extension(item_path, extension, sub_path))"),
        "list_directory_recursive_call": ("file_manager.py - list_directory recursive call", "Add: list_directory_tree(item_path, next_prefix, max_depth, current_depth + 1)"),
    }

    # Only show hints for incomplete tasks
    incomplete_tasks = [task for task, is_completed in todo_status.items() if not is_completed]
    
    if incomplete_tasks:
        print("\n=== TODO TASK HINTS (Incomplete Tasks Only) ===")
        for task in incomplete_tasks:
            if task in hints:
                location, hint = hints[task]
                print(f"\n{location}:")
                print(f"  Hint: {hint}")
    else:
        print("\n🎉 All TODO tasks completed! No hints needed.")


if __name__ == "__main__":
    # Create a test suite and run all TODO tests
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Always print the summary and hints at the end
    print_todo_summary()

    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
