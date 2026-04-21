#!/usr/bin/env python3
"""
Daily Reflection Tree Agent
A deterministic reflection tool that walks employees through structured end-of-day reflection.
No LLM calls at runtime - fully deterministic based on decision tree.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
from collections import defaultdict


class ReflectionAgent:
    def __init__(self, tree_path: str):
        """Initialize the agent with a tree data file."""
        self.tree_path = Path(tree_path)
        self.tree_data = self._load_tree()
        self.nodes = {node['id']: node for node in self.tree_data['nodes']}
        self.state = {
            'answers': {},  # Store all answers by node ID
            'signals': defaultdict(lambda: defaultdict(int)),  # Track axis signals
            'path': []  # Track the path taken through the tree
        }
        
    def _load_tree(self) -> Dict:
        """Load the tree structure from JSON file."""
        if not self.tree_path.exists():
            raise FileNotFoundError(f"Tree file not found: {self.tree_path}")
        
        with open(self.tree_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _interpolate_text(self, text: str) -> str:
        """Replace placeholders like {A1_OPEN.answer} with actual answers."""
        result = text
        for node_id, answer in self.state['answers'].items():
            placeholder = f"{{{node_id}.answer}}"
            if placeholder in result:
                result = result.replace(placeholder, answer)
        
        # Replace axis dominance placeholders
        for axis in ['axis1', 'axis2', 'axis3']:
            placeholder = f"{{{axis}.dominant}}"
            if placeholder in result:
                dominant = self._get_dominant_signal(axis)
                result = result.replace(placeholder, dominant)
        
        # Replace summary reflection
        if '{summary_reflection}' in result:
            reflection = self._generate_summary_reflection()
            result = result.replace('{summary_reflection}', reflection)
        
        return result
    
    def _get_dominant_signal(self, axis: str) -> str:
        """Determine the dominant signal for an axis."""
        signals = self.state['signals'].get(axis, {})
        if not signals:
            return "neutral"
        
        # Find the signal with the highest count
        dominant = max(signals.items(), key=lambda x: x[1])
        return dominant[0]
    
    def _generate_summary_reflection(self) -> str:
        """Generate the final summary reflection based on the path taken."""
        axis1 = self._get_dominant_signal('axis1')
        axis2 = self._get_dominant_signal('axis2')
        axis3 = self._get_dominant_signal('axis3')
        
        # Map signals to template keys
        axis1_key = 'internal' if axis1 == 'internal' else 'external'
        axis2_key = axis2 if axis2 in ['contribution', 'entitlement', 'transactional'] else 'transactional'
        axis3_key = axis3 if axis3 in ['altrocentric', 'team', 'self'] else 'self'
        
        template_key = f"{axis1_key}_{axis2_key}_{axis3_key}"
        templates = self.tree_data.get('summary_templates', {})
        
        return templates.get(template_key, "You showed up today. That's what matters.")
    
    def _record_signal(self, signal: Optional[str]):
        """Record a signal from a node (e.g., 'axis1:internal')."""
        if signal:
            parts = signal.split(':')
            if len(parts) == 2:
                axis, value = parts
                self.state['signals'][axis][value] += 1
    
    def _get_next_node(self, current_node: Dict, answer: Optional[str] = None) -> Optional[str]:
        """Determine the next node based on current node and answer."""
        # If node has explicit target, use it
        if current_node.get('target'):
            return current_node['target']
        
        # If it's a decision node, evaluate routing rules
        if current_node['type'] == 'decision':
            return self._evaluate_decision(current_node)
        
        # If it's a question node, find the decision child
        if current_node['type'] == 'question' and answer:
            # Find child decision node
            for node in self.nodes.values():
                if node.get('parentId') == current_node['id'] and node['type'] == 'decision':
                    return node['id']
        
        # Otherwise, find first child
        for node in self.nodes.values():
            if node.get('parentId') == current_node['id']:
                return node['id']
        
        return None
    
    def _evaluate_decision(self, decision_node: Dict) -> Optional[str]:
        """Evaluate decision node routing rules."""
        rules = decision_node.get('options', [])
        
        for rule in rules:
            # Parse rule: "answer=Productive|Mixed:A1_Q_AGENCY_HIGH"
            if ':' not in rule:
                continue
            
            condition, target = rule.split(':', 1)
            
            if condition.startswith('answer='):
                # Extract the parent question node
                parent_id = decision_node.get('parentId')
                if not parent_id:
                    continue
                
                # Get the answer from state
                user_answer = self.state['answers'].get(parent_id)
                if not user_answer:
                    continue
                
                # Check if answer matches any of the options
                valid_answers = condition.split('=', 1)[1].split('|')
                if user_answer in valid_answers:
                    return target
        
        return None
    
    def _display_node(self, node: Dict):
        """Display a node to the user."""
        text = self._interpolate_text(node['text'])
        
        if node['type'] == 'start':
            print(f"\n{'='*60}")
            print(text)
            print(f"{'='*60}\n")
        elif node['type'] == 'question':
            print(f"\n{text}")
        elif node['type'] == 'reflection':
            print(f"\n{'─'*60}")
            print(f"💭 {text}")
            print(f"{'─'*60}")
        elif node['type'] == 'bridge':
            print(f"\n{'·'*60}")
            print(f"→ {text}")
            print(f"{'·'*60}")
        elif node['type'] == 'summary':
            print(f"\n{'='*60}")
            print("📊 YOUR REFLECTION SUMMARY")
            print(f"{'='*60}")
            print(text)
            print(f"{'='*60}")
        elif node['type'] == 'end':
            print(f"\n{text}\n")
    
    def _get_user_choice(self, options: List[str]) -> str:
        """Get user's choice from a list of options."""
        print()
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        
        while True:
            try:
                print()
                choice = input("Your choice (enter number): ").strip()
                choice_num = int(choice)
                if 1 <= choice_num <= len(options):
                    return options[choice_num - 1]
                else:
                    print(f"Please enter a number between 1 and {len(options)}")
            except ValueError:
                print("Please enter a valid number")
            except (KeyboardInterrupt, EOFError):
                print("\n\nSession interrupted. Goodbye.")
                sys.exit(0)
    
    def _wait_for_continue(self):
        """Wait for user to press enter to continue."""
        try:
            input("\n[Press Enter to continue]")
        except (KeyboardInterrupt, EOFError):
            print("\n\nSession interrupted. Goodbye.")
            sys.exit(0)
    
    def run(self):
        """Run the reflection session."""
        current_id = 'START'
        
        while current_id:
            node = self.nodes.get(current_id)
            if not node:
                print(f"Error: Node '{current_id}' not found")
                break
            
            # Track the path
            self.state['path'].append(current_id)
            
            # Display the node
            self._display_node(node)
            
            # Record signal if present
            self._record_signal(node.get('signal'))
            
            # Handle different node types
            if node['type'] == 'question':
                options = node.get('options', [])
                if options:
                    answer = self._get_user_choice(options)
                    self.state['answers'][current_id] = answer
                    current_id = self._get_next_node(node, answer)
                else:
                    current_id = self._get_next_node(node)
            
            elif node['type'] in ['reflection', 'summary']:
                self._wait_for_continue()
                current_id = self._get_next_node(node)
            
            elif node['type'] in ['start', 'bridge', 'decision']:
                # Auto-advance nodes
                current_id = self._get_next_node(node)
            
            elif node['type'] == 'end':
                # End of session
                break
        
        return self.state
    
    def get_transcript(self) -> str:
        """Generate a transcript of the session."""
        lines = []
        lines.append("="*60)
        lines.append("REFLECTION SESSION TRANSCRIPT")
        lines.append("="*60)
        lines.append("")
        
        for node_id in self.state['path']:
            node = self.nodes.get(node_id)
            if not node:
                continue
            
            text = self._interpolate_text(node['text'])
            
            if node['type'] == 'start':
                lines.append(f"[START]")
                lines.append(text)
                lines.append("")
            elif node['type'] == 'question':
                lines.append(f"[QUESTION]")
                lines.append(text)
                answer = self.state['answers'].get(node_id)
                if answer:
                    lines.append(f"→ Answer: {answer}")
                lines.append("")
            elif node['type'] == 'reflection':
                lines.append(f"[REFLECTION]")
                lines.append(text)
                lines.append("")
            elif node['type'] == 'bridge':
                lines.append(f"[BRIDGE]")
                lines.append(text)
                lines.append("")
            elif node['type'] == 'summary':
                lines.append(f"[SUMMARY]")
                lines.append(text)
                lines.append("")
            elif node['type'] == 'end':
                lines.append(f"[END]")
                lines.append(text)
        
        lines.append("")
        lines.append("="*60)
        lines.append("AXIS SIGNALS")
        lines.append("="*60)
        for axis, signals in self.state['signals'].items():
            lines.append(f"{axis}: {dict(signals)}")
        
        return "\n".join(lines)


def main():
    """Main entry point."""
    # Determine tree file path
    tree_path = Path(__file__).parent.parent / "tree" / "reflection-tree.json"
    
    if not tree_path.exists():
        print(f"Error: Tree file not found at {tree_path}")
        print("Please ensure the tree file exists at: tree/reflection-tree.json")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("DAILY REFLECTION TREE")
    print("A deterministic reflection tool")
    print("="*60)
    
    # Create and run the agent
    agent = ReflectionAgent(str(tree_path))
    agent.run()
    
    # Optionally save transcript
    save = input("\nWould you like to save a transcript? (y/n): ").strip().lower()
    if save == 'y':
        transcript = agent.get_transcript()
        transcript_path = Path("transcript.txt")
        with open(transcript_path, 'w', encoding='utf-8') as f:
            f.write(transcript)
        print(f"\nTranscript saved to: {transcript_path}")


if __name__ == "__main__":
    main()
