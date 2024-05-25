#create view uv_memberTBL
#as select memberName, memberAddress from memberTBL;

#select * from uv_membertbl;

# 두개의 쿼리를 실행하는 프로시저 작성
DELIMITER //
CREATE PROCEDURE myProc()
BEGIN
	SELECT * FROM memberTBL WHERE memberName = '당탕이' ;
	SELECT * FROM productTBL WHERE productName = '냉장고' ;
END // 
DELIMITER ;


call myProc;


select* from membertbl;


insert into membertbl values ('Figure','연아','경기도 군포시 당정동');


update membertbl set memberAddress='서울 강남구 역삼동' where memberID='Figure';


delete from membertbl  where memberId='Figure';




create table deletedMemberTBL(
	memberID char(8),
    memberName char(5),
    memberAddress char(20),
    deletedDate date
    );
    
select now();
select curdate();

#회원 테이블(memberTBL)에 DELETE 작업이 일어나면 백업 테이블(deletedMemberTbl)에 지워진 데이터가 기록되는 트리거 작성

DELIMITER //
CREATE TRIGGER trg_deletedMemberTBL  #트리거 이름
	AFTER DELETE # 삭제 후에 작동하게 지정
    ON memberTBL # 트리거를 부착할 테이블
    FOR EACH ROW # 각 행마다 적용
BEGIN
	# OLD 테이블의 내용을 백업 테이블에 삽입
    insert into deletedmembertbl values (OLD.memberID, OLD.memberName, OLD.memberAddress, curdate());
END // 
DELIMITER ;


select* from membertbl;

select* from deletedmembertbl;


delete from membertbl where memberID='Dang';







