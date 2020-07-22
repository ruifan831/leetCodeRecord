class MinStack {
    private Stack<Pair<Integer,Integer>> stack;
    /** initialize your data structure here. */
    public MinStack() {
        stack = new Stack<>();
        
    }
    
    public void push(int x) {
        if (stack.empty()){
            stack.push(new Pair(x,x));
        }else{
            if (stack.peek().getValue()>x){
                stack.push(new Pair(x,x));
            }else{
                stack.push(new Pair(x,stack.peek().getValue()));
            }
        }
        
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.peek().getKey();
    }
    
    public int getMin() {
        return stack.peek().getValue();
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */