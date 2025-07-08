import collections

class Thing:
    def __repr__(self):
        """
            Phương thức __repr__ trả về một chuỗi biểu diễn đối tượng khi nó được in ra (ví dụ, khi gọi print(thing)).
            Nếu đối tượng có thuộc tính __name__, chuỗi sẽ sử dụng giá trị của __name__. Nếu không, nó sử dụng tên của lớp (self.__class__.__name__).
            Kết quả có định dạng <tên>, ví dụ: <Food> hoặc <BlindDog>.
        """

        return f"<{getattr(self, '__name__', self.__class__.__name__)}>"

    def is_alive(self):
        """
            Kiểm tra xem đối tượng có "sống" hay không.
            Một đối tượng được coi là "sống" nếu nó có thuộc tính alive (được kiểm tra bằng hasattr(self, 'alive')) và giá trị của alive là True.
            Mặc định, các đối tượng Thing không có thuộc tính alive, nên phương thức này trả về False.

            =============================================================
            Ví dụ:
            - Lớp Agent (trang 2 của tài liệu) định nghĩa thuộc tính alive = True trong phương thức __init__, nên các instance của Agent (như BlindDog) sẽ trả về True khi gọi is_alive.
            - Ngược lại, các instance của Food hoặc Water không có thuộc tính alive, nên is_alive trả về False.

            =============================================================
            Phương thức này hữu ích để phân biệt giữa các đối tượng "sống" (như tác nhân) và các đối tượng "không sống" (như thức ăn, nước) trong môi trường.
            Trong bài thực hành, nó có thể được sử dụng để kiểm tra trạng thái của con chó mù (ví dụ, để dừng mô phỏng nếu con chó không còn "sống").
        """

        return hasattr(self, 'alive') and self.alive

    def show_state(self):
        """
            Phương thức này được thiết kế để hiển thị trạng thái nội tại (internal state) của đối tượng.
            Trong lớp Thing, phương thức này chỉ in ra thông báo mặc định: "I don't know how to show_state."
            Các lớp con (như Agent hoặc BlindDog) được khuyến khích ghi đè (override) phương thức này để hiển thị trạng thái cụ thể của chúng.

            =============================================================
            Phương thức này chủ yếu dùng cho mục đích debugging hoặc hiển thị thông tin chi tiết về trạng thái của đối tượng.
            Trong bài thực hành, nó dường như không được sử dụng trực tiếp, nhưng có thể được mở rộng trong các phiên bản phức tạp hơn của mô phỏng.
        """

        print("I have no idea how to show_state")

    def display(self, canvas, x, y, width, height):
        """
            Phương thức này được thiết kế để hiển thị một hình ảnh hoặc biểu diễn đồ họa của đối tượng trên một canvas (bề mặt vẽ).
            Trong mã nguồn, nó chỉ là một phương thức rỗng (pass) với ghi chú "Do we need this?", cho thấy nó có thể là một placeholder cho các ứng dụng có giao diện đồ họa (GUI).

            ==============================================================
            Trong bài thực hành này, môi trường Park là một mô phỏng tuyến tính 1D (con chó di chuyển theo một đường thẳng), nên phương thức display không được sử dụng.
            Tuy nhiên, trong các phiên bản mở rộng (ví dụ: môi trường 2D với giao diện đồ họa), phương thức này có thể được ghi đè để vẽ các đối tượng như con chó, thức ăn, hoặc nước trên màn hình.
        """
        pass


class Food(Thing):
    pass


class Water(Thing):
    pass


class Agent(Thing):
    """
        Lớp Agent là một lớp con của Thing, được thiết kế để biểu diễn các thực thể có khả năng tương tác chủ động với môi trường (Environment),
        chẳng hạn như con chó mù (BlindDog) trong bài thực hành. Không giống như các đối tượng thụ động như Food hoặc Water, một Agent có khả năng:
        - Nhận thức (percept) về môi trường xung quanh.
        - Quyết định hành động (action) dựa trên nhận thức thông qua một hàm program.
        - Duy trì trạng thái nội tại (như sống/chết, hiệu suất, hoặc các vật đang giữ).
        Lớp Agent đóng vai trò trung gian giữa lớp cơ sở Thing và các lớp con cụ thể như BlindDog.
        Nó cung cấp các thuộc tính và phương thức cơ bản để hỗ trợ hành vi của tác nhân trong môi trường.
    """


    location = 1

    def __init__(self, program=None):
        self.alive = True                           # Chỉ trạng thái sống của tác nhân (kế thừa từ Thing, liên quan đến phương thức is_alive).
        self.bump = False                           # Chỉ trạng thái va chạm (chưa được sử dụng trong bài này, có thể dùng trong các môi trường phức tạp hơn, ví dụ: khi tác nhân va vào tường).
        self.holding = []                           # Danh sách các đối tượng mà tác nhân đang giữ (chưa được sử dụng trong bài, nhưng có thể dùng để mô phỏng việc nhặt hoặc mang đồ vật).
        self.performance = 0                        # Điểm hiệu suất của tác nhân, có thể được tăng khi thực hiện các hành động thành công (như ăn hoặc uống, nhưng không được triển khai trong bài này).

        if program is None or not isinstance(program, collections.abc.Callable):
            """
                Nếu program là None hoặc không phải là một hàm khả thi (collections.abc.Callable), một hàm mặc định được tạo.
                Hàm mặc định này yêu cầu người dùng nhập hành động thủ công dựa trên nhận thức (percept), in ra thông báo lỗi và sử dụng tên lớp (self.__class__.__name__) để báo cáo.
            """

            print(f"Can't find a valid program for {self.__class__.__name__}, falling back to default.")

            def program(percept):
                return eval(input(f'Percept={percept}; action?'))

        self.program = program

    def can_grab(self, thing):
        """
            Kiểm tra xem tác nhân có thể "nắm" (grab) một đối tượng (thing) hay không.
            Mặc định trả về False, nghĩa là tác nhân không thể nắm bất kỳ đối tượng nào.
            Phương thức này được thiết kế để các lớp con (như BlindDog) ghi đè (override) nếu cần triển khai khả năng nắm giữ đối tượng.
        """
        return False

if __name__ == "__main__":
    """
        Vai trò của repr: Cung cấp cách hiển thị dễ đọc cho các đối tượng, giúp debugging và theo dõi trạng thái trong mô phỏng.
    """

    t = Thing()
    print(repr(t)) # repr(text) gives the precise representation with escape characters so that the output can be recreated in code.
    print(t)


"""
    Trong bài thực hành "Lab 02 Agents.pdf", lớp Thing đóng vai trò nền tảng để xây dựng mô phỏng một con chó mù (BlindDog) 
        di chuyển trong môi trường (Park) để tìm và tương tác với các đối tượng như Food và Water. Cụ thể:
    - Biểu diễn các thực thể vật lý: Mọi thứ trong môi trường, từ con chó, thức ăn, đến nước, đều là một instance của lớp con của Thing.
    - Quản lý vị trí: Mỗi Thing có một thuộc tính location (dù không được định nghĩa trực tiếp trong lớp Thing mà được thêm vào bởi môi trường Environment) 
        để xác định vị trí trong không gian mô phỏng.
    - Hỗ trợ kế thừa: Các lớp như Food, Water, và Agent kế thừa từ Thing, cho phép chúng sử dụng các phương thức như __repr__ và is_alive, 
        đồng thời mở rộng thêm các thuộc tính và hành vi riêng.
    
    Ví dụ ngữ cảnh: Trong môi trường Park, con chó mù (BlindDog, một lớp con của Agent, vốn là lớp con của Thing) di chuyển từ vị trí 1, 
        gặp Food tại vị trí 5, và Water tại vị trí 7. Tất cả các đối tượng này đều là Thing và được quản lý bởi môi trường thông qua danh sách things.
        
    ======================================================================================
    Trong bài thực hành, lớp Agent là nền tảng cho các tác nhân thông minh, chẳng hạn như BlindDog. 
    Vai trò chính của nó bao gồm:
        - Biểu diễn một thực thể chủ động: Agent không chỉ có vị trí (location, kế thừa từ Thing) mà còn có trạng thái nội tại (alive, bump, holding, performance) 
            và khả năng ra quyết định thông qua hàm program.
        - Cung cấp khung cho hành vi: Hàm program là "bộ não" của tác nhân, nhận nhận thức (percept) từ môi trường và trả về hành động (action) tương ứng.
        - Hỗ trợ kế thừa: Các lớp con như BlindDog kế thừa từ Agent để định nghĩa các hành vi cụ thể (như di chuyển, ăn, uống).
"""