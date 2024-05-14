package com.qa.tests;
 
import org.testng.annotations.Test;
import org.testng.annotations.Test;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.AfterTest;
import org.testng.annotations.Parameters;
 
import io.github.bonigarcia.wdm.WebDriverManager;
 
import java.time.Duration;
import java.util.concurrent.TimeUnit;
 
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.edge.EdgeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
 
	
 
 
public class BookStore {
	WebDriver driver;

	@BeforeTest
	public void Browser() {
		WebDriverManager.edgedriver().setup();
        driver = new EdgeDriver();
        driver.manage().window().maximize();
        driver.get("http://54.173.109.51:8080/books/CustomerRegister.html");
	}
	@Test (priority=1)
	public void user_name() throws InterruptedException{
        driver.findElement(By.xpath("//*[@id=\"Email\"]")).sendKeys("pratik@gmail.com");
        driver.findElement(By.id("passWord")).sendKeys("1234");
        driver.findElement(By.id("firstName")).sendKeys("pratik");
        driver.findElement(By.id("lastName")).sendKeys("rathi");
        driver.findElement(By.id("address")).sendKeys("pune");
        driver.findElement(By.id("phno")).sendKeys("1234567898");
        driver.findElement(By.name("acceptance")).click();
        driver.findElement(By.xpath("/html/body/form/table/tbody/tr[2]/td/input[7]")).click();	

  }
	@Test (priority=2)
	public void login() {
		driver.findElement(By.xpath("//*[@id=\"navbarNav\"]/ul/li[2]/span/a")).click();
		driver.findElement(By.xpath("/html/body/table/tbody/tr[3]/td/a")).click();
		driver.findElement(By.id("userName")).sendKeys("pratik@gmail.com");
		driver.findElement(By.id("Password")).sendKeys("1234");
		driver.findElement(By.xpath("/html/body/form/table/tbody/tr[3]/td/input[3]")).click();
	}
	@Test (priority=3)
	public void Books() {
		driver.findElement(By.id("books")).click();
		driver.findElement(By.xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[2]/form/input[3]")).click();
		driver.findElement(By.xpath("//*[@id=\"topmid\"]/form/input")).click();
		driver.findElement(By.name("pay")).click();
	}
	@Test (priority=4)
	public void payment() {
		driver.findElement(By.id("cname")).sendKeys("pratik");
		driver.findElement(By.id("ccnum")).sendKeys("1111-1111-2222-2222");
		driver.findElement(By.id("expmonth")).sendKeys("may");
		driver.findElement(By.id("cvv")).sendKeys("123");
		driver.findElement(By.id("expyear")).sendKeys("2032");
		driver.findElement(By.id("fname")).sendKeys("pratik rathi");
		driver.findElement(By.xpath("//*[@id=\"email\"]")).sendKeys("pr210@gmail.com");
		driver.findElement(By.id("adr")).sendKeys("pune");
		driver.findElement(By.id("city")).sendKeys("pune");
		driver.findElement(By.id("zip")).sendKeys("41103");
		driver.findElement(By.id("state")).sendKeys("maharashtra");
	//	driver.findElement(By.id("checked")).click();
		driver.findElement(By.xpath("/html/body/div/div[2]/div/div/form/input")).click();
	}
//	@AfterTes
//	public void quits() {	
//		driver.quit();
//	}
}