<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/bpf-9HqA-ahH0zBxFS_BKY3lVoFjpBNifcmsaU64Quqj_PfgfdSFbNSPtdJkfMemxx3ma-beubfXvtutG0WKNj32wIUzrjYe1F-AtnYLb2Rjuy0nZksuXn7Ite76rvEC_u9zYAXy7UkN2_3_6YdxJ5MhHN6-DBIHJLrx_T8e-7TiyykvuCV4WVOavEwI1fKRN83QNxIP3goJ3EhKZSxc1BiR82mUrMOYKOmvL07SywQvngfm0CXkJKKMbwojVihf-8EwJHSCZ1ZSy_0voba31PSGpfpBDzaU52hIZeYrCYAMiElwG7BkLGeloDvIT_jUJ4b0iszuBiWpxxbXSxY_jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 40K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 09:59:14</div>
<hr>

<div class="tg-post" id="msg-8978">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
سپاه : عملیات نصر شروع شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/IranProxyV2/8978" target="_blank">📅 09:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8977">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
انفجاررررر در کرمانشاه
گزارش منابع داخلی از فعالیت پدافند در کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/IranProxyV2/8977" target="_blank">📅 09:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8976">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
⚠️
سازمان منطقه ویژه پتروشیمی:  دستور خروج اضطراری کلیه کارکنان روزکار از این منطقه صادر شده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/IranProxyV2/8976" target="_blank">📅 09:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8975">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🆕
کانال ۱۲ اسرائیل: طی چندساعت اخیر به ۲۰ هدف تو ایران حمله کردیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/IranProxyV2/8975" target="_blank">📅 09:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8974">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
کانال ۱۴ درباره یک مسئول اسرائیلی:
تأکید می‌کنیم که یک تأسیسات پتروشیمی در ایران هدف قرار گرفته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/IranProxyV2/8974" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8973">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPansML1yo_kbAQPW0DRxWqwhooQVEUs8jSbn0sj3to-QOwnEeNnVrfRgiaEVr0-fSTThDIfS6XhvAiE0MB27gQOGgPW2kt1UQA89KZ6HCGv7mkLifqN0BWJGZLX_-oyMI1P0KM0e_BnfaiYt525dyJUl0oCjBQMV_CulvMtNjRaY9WemxzJu3t7fEDp6XX5XtRYeOODJVJc1LyVO2ZICPGPN6wYEmj_yEOTLV2ooYS5uPCaJf14NO8C0xWAzJfx1w5PnfZyPwafPkIz31jWUqs3ONFYHLaFDS4_VXB-TMdAM-0A1RC4-VhJ1Vx9D0qOmb_SltvICVZT0a-GV8Qv0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور مورفی:
این جنگ برای آمریکا تحقیرآمیز بود؛
ترامپ دیشب گفت به نتانیاهو زنگ می‌زنم تا جلوی حمله تلافی‌جویانه‌ش رو بگیرم ولی اسرائیل ۲ ساعت بعد از این تماس جنگ رو از سر گرفت و ترامپ و آمریکا رو تحقیر کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/IranProxyV2/8973" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8972">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDRy9mJX1Ms2qYp8Ylj6V-8kQbgZJvMBZiC-9o6iqdFVnBpkMiHvpjD4_1fHNZLywQYUt5a3mFGQeAm-V4dN383rlBXb4wB2rQZYm0t8YGjSMXyLMGnwWLbf3jMeyu4albkjUyayQP2vflh9MyP8GgHxFcaBRFC9VoREo3qRvChyd6pL2gO66zvYRKrN0hTf4iH9J_8g4SXO5qa1T3kj8cztNhBkqWJXtdPAhAEu7xAVtCtyqHF6-rw3IAx8QjVebHEemaubGryCcLRcU-2r9V6eXlEIuJaxT_7F24AxM_flvVXLua2rv8SEXf4EDNVkTa0NHkJKqOC0zR5uyP5Ytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم
:
سپاه موشک خیبر شکن و یک پهباد ناشناخته امروز استفاده کرده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/IranProxyV2/8972" target="_blank">📅 08:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8968">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺⁴.ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ های جدید اختصاصی OpenVPN
با حجم و اعتبار نامحدود
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
بدون نیاز به یوزر پسورد
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/IranProxyV2/8968" target="_blank">📅 08:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8967">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📶
این پروکسی های تلگرام رو داشته باشید متصلن:
https://t.me/proxy?server=www.alp-drtop.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b
https://t.me/proxy?server=167.233.66.2&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=188.245.196.78&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=87.248.129.107&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=178.105.225.211&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=91.107.246.35&port=443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=secure.bits-lab.info&port=443&secret=ee1603010200010001fc030386e24c3ad37765622e79656b74616e65742e636f6d
❗️
با اکثر اینترنت ها تست شده
پیشنهاد میشه کمی برای اتصال صبور باشید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/IranProxyV2/8967" target="_blank">📅 08:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8966">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOe5aelqFDVVAflu2ZYzWzfXb8QsNoHvP2nAHSa-BxvFD0nt5fIAgZdY8En3L3-aO1N4XXzCeKxSNgwvCtN0i6H7y50eE-dVFygnaItgka02V53T_1_Td-lAVImLtzWjQ8TZitjq7prbem_-0iI_3i2m9FhwX9C7WyrLhM0TN9yLE6SDiQ3-koSDwkVbeCOaxNUabK1uXkUh50uYMPFp6nGXrJdB6K7Fo2MwE5wozmAfmHe634tMVrHRH5ULqTQDALdgaAGYc1W_f7FlAg78KfdwX0xXoCJED4_NEQYVRqtuS8OruOyKwSwJLERUHEvPe2vdTM9F2EhUDL4vR3QCZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه وزارت دفاع عربستان:
دارن بهمون حملات موشکی و پهپادی انجام میدن، دستم کم دو انفجار نزدیک شهر ریاض گزارش شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/IranProxyV2/8966" target="_blank">📅 08:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8965">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رادیو ارتش اسرائیل
موج جدیدی از حملات رو شناسایی کردیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/IranProxyV2/8965" target="_blank">📅 08:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8964">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
اصابت چند پرتابه به پتروشیمی کارون ماهشهر تایید شده و بخشی از پتروشیمی در جریان این حملات اسیب دیده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/IranProxyV2/8964" target="_blank">📅 08:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8963">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=KOUnBnvXqTxXPjL44oJcUR7-zn-aSr58Azvd6zngCFFSAgCohE_OEzKNcWIfsa_aiDQWU7k8tJ0YIH0yjez9cS9qp6xvuYa1kzIPGaj2Smb7zidJPNB0fQfsCjtaeLzRa6eI_7hwzRknVDVN-arrcpKTinp3OcBbFv4odJLCAz-gEkUfVpieJni2zw9lA0ZytvNSQigubn_9ZbBON3WqoMx3NPBwWn2tz3YB9pLGiTF6l5gadIepXLX_EhAlyVXUlgtRChMW9TTmRScnQFv_w995BW5TTX5KG4EPiRk70ULzHjZvqFu43ZRw0zy2L8SqLz9JIdps6cmEAiq00i7bEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=KOUnBnvXqTxXPjL44oJcUR7-zn-aSr58Azvd6zngCFFSAgCohE_OEzKNcWIfsa_aiDQWU7k8tJ0YIH0yjez9cS9qp6xvuYa1kzIPGaj2Smb7zidJPNB0fQfsCjtaeLzRa6eI_7hwzRknVDVN-arrcpKTinp3OcBbFv4odJLCAz-gEkUfVpieJni2zw9lA0ZytvNSQigubn_9ZbBON3WqoMx3NPBwWn2tz3YB9pLGiTF6l5gadIepXLX_EhAlyVXUlgtRChMW9TTmRScnQFv_w995BW5TTX5KG4EPiRk70ULzHjZvqFu43ZRw0zy2L8SqLz9JIdps6cmEAiq00i7bEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از موشک‌های ایرانی به یک مرکز نظامی اسرائیلی در نزدیکی نابلس اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/IranProxyV2/8963" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8962">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZjj0U9kvnlrznb_RqW5QD5tzswc2MXWzi6GdgsXpbME3ipJzzE4GmyokCPtOVnrtSrEBSfvLCSMZkGxJLj-gwZFkPrww98SBKnwl4sEOi93r1cT1WGQZDI2FfJhP4PdsmIm1rlaWLhnLsM3p_XL5YoYlscaavqU-e4RDAdIqCShAoTlwdaakxKjhKm5Op3nkk9RZG9jYm36w-uk37I5aaCGfDpoQSuKSPDkhVJ6zzzAt-aK90ZlS5lzdsWiDdG2mNLPtJyykUT6GB80kXre7qxRRMqJmohxUJHORMJFnWKglCbkXKP_8iBk95K6gbzPfrpl0AUtI_lgrPk_14JjHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار اسرائیل:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/IranProxyV2/8962" target="_blank">📅 08:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8961">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
مثه اینکه موج جدیدی از حملات ایران شروع شده
از اصفهان ، ارومیه ، خرم آباد ، کرمانشاه ، ماهشهر و آبادان موشک پرتاب شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/IranProxyV2/8961" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8960">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4bxjOPDuS3SkXHpNICN_BYy5_CWbJB14mmCDRn1uZ-WJUHOMAcMk0Tjc966-hACG-OsMtA32astPKi_bVznQHnKA-t_vgPU3y6agdv_w1Jhn-WiWD_sIfnCFI-r4iIwr_INTHuUFXicak4AxITO-lPhBgMJz36MB0FNDa5P0EE4pOAGERgdNDLV6Pb7ErdGErPpFdLvFiRRfCqAqVgSgRyrnzARUpTQrmwSr7Et7UKKM5sWzBglJYsGaM1uIXiB23fnPQQXviHCh3fQOqbjQOU-sQYA8m84O13v0KVkVRa3bfJZ4sy2Cw0yZHxISkVGMGyNC8NYBXbQzxvotOJ3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در پی به صدا آمدن آژیر خطر در اسرائیل، مقامات این کشور گفتند که یک موشک شلیک شده از یمن را به طور موفق رهگیری کردیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/IranProxyV2/8960" target="_blank">📅 08:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8959">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇸🇦
شنیده شدن انفجار در پایگاه شاهزاده سلطان، الخرج عربستان  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/IranProxyV2/8959" target="_blank">📅 08:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8958">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇸🇦
شنیده شدن انفجار در پایگاه شاهزاده سلطان، الخرج عربستان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/IranProxyV2/8958" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8957">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش به ربات مراجعه…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/IranProxyV2/8957" target="_blank">📅 08:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8956">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
کاخ سفید:
این تنش های بین ایران و اسرائیل هیچ ربطی ما ندارند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/IranProxyV2/8956" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8955">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شبکه «آی ۲۴نیوز» اسرائیل گزارش داد بر اساس گزارش‌های اولیه، اسرائیل تاکنون دست‌کم ۱۵ هدف را در نقاط مختلف ایران هدف قرار داده است. به گفته این شبکه، از جمله اهداف مورد حمله یک مرکز تولید پهپاد، فرودگاه بین‌المللی تهران و تاسیسات راهبردی نفتی بوده‌اند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/IranProxyV2/8955" target="_blank">📅 08:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8954">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هرچی دارین سیو کنید احتمال داره باز قطع کنن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/IranProxyV2/8954" target="_blank">📅 07:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8953">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
🔴
وقوع دست‌کم سه انفجار در اصفهان  گزارش میشود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8953" target="_blank">📅 05:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8952">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
سپاه اعلام کرد به ایران حمله موشکی شده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8952" target="_blank">📅 05:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8951">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClDVO44gFm5iY7kt2QhjUZrDwX_1GANEbtX7prENU0ut4_3c6UPKzCkFRoJuySufBILtACqdCvZKEt-Ai_B0u79kyfHpSO2sQTbe8SlFWtBPoDhKZUwb2tol_Jf6som6OIJYnwxHRDjNhkE0pr7i_PwTpTcZ-3G6P94d1wieLYxVyvTC3WiiLDvcZ2cC50Zy5_dx2R0-mHK6grLxuEbQFNgRaY91KqcRmDJ1deR317SqjlyeiKCd4xY3KDNhy9NyzPkwOv14NP2zPBacBKAxw-qQtuSbsgTkkz1FNKsSOr5CZFGVaKk_0umsG2JCcAuAxCVD6AmKJvODC0Y8N5c9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری-خبرهایی از انفجار در پایگاه موشکی اصفهان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8951" target="_blank">📅 05:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8950">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
🔴
فوری
-
الجزیره: رسانه‌های اسرائیلی گزارش دادند حملات هوایی اخیر فرودگاه مهرآباد تهران و همچنین یک انبار نگهداری پهپادهای انتحاری را هدف قرار داده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8950" target="_blank">📅 05:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8949">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
تا کنون تعداد اهدافی که اسرائیل به آن‌ها حمله کرده 15 هدف بوده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8949" target="_blank">📅 05:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8948">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
حملاتی محدود به چند سایت پدافندی و نظامی تو تهران، کرمانشاه، اصفهان، ارومیه، کرج و تبریز و چند نقطه دیگه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8948" target="_blank">📅 05:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8947">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری-کانال ۱۲ اسرائیل اعلام کرد که فرودگاه مهرآباد تهران مورد حمله قرار گرفته است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8947" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8946">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry2vPuVu4RvSd6pbMZyAVjZl4P6neKPwmiJCEJhA0KdAo-J6eky9Kui9y7hUlTEmi2gTnpYOaAA_xBlRUXOKhok28enEJpPPjyhW7PBWTpYYbJ-hYRiTfVzrLHfFXYzHR2uyPtskq3xPrCOLZScQZTtfHdi3n1KcV2MREBhupiJ8XkJ3bEMWDBKYHyshkirIQPgywAXiTFgqlLASqHpFL-gmTDb-yfRFHUI0qyuoTTPXw7Irqa0LKF3P6b2V62hwB3yAbL9qhPc-05RL2wjy7sVenZHFDyuMG9ITe98K_R3LhS5MklG_yfDpvrCprmYJHTmQDpTF368Ge9mukOzIvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
حمله اسراییل به غرب ایران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8946" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8945">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
آغاز حملات سپاه پاسداران به مواضع اسرائیل به گفته برخی خبرگزاری های محلی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8945" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8944">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b30myZCfrUlkcPOczo5fai4348VpJwCfHvIvFEBz2Z_xSzGjXlwrxHX_DBH13vi2CjgnrNoFvkMQe630BsPa6_ox5xkydEoZkHnRtRMy22WZAS2PrkcE03lOm2jnIoLqC5YNv-FC-zivk3WjIh23bz6-tPISbCIejq3ZfooQJGiNn8H2UvxBkxiwqlz2XOnOUbP1B8xmOLIZE25gzobj4fmiabVaVtFx8YiznoaJhtIVbTP7mOWR--b-PPCJ0YYCHpqSZH2_16GH_J4vYIq41EXXoFacMl5fVEvTO-tfscZJxSRDoQiuy-W1DkAull6VGLz18BNDKDyL42kXo27Jmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8944" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8943">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
کانال 14 اسرائیل:
نیروی هوایی اسراییل با استفاده از موشک های بالستیک هواپایه و موشک های کروز، از طرف دریای مدیترانه به ایران حمله کرده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/IranProxyV2/8943" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8942">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQAibIhPjmkK63aQcx2WxN0nTEx14oHcFUlZKjGFBnzHc77k2jsrT4SXwzIDcarbbhd1IaLIx5ZYWXRFepQIrgKmmrwlwVHGUq2c16ZDdfr9lNvzVDrWK9vsf0zLzZFG7RUMcJwW2z7BzfOwOzjvGcxo0JYIELgJDkFjMrLKG77KOTOE-0IDIHVJigjHAewGuvZiLlSRIgxGrQkE_7hP6G4DCsIUl6G0U93_cFKe1G7ypB1MTeZHxeAER6PvbwIWrvbZo_VbHWdlWS4X-quvLIStoF25Fmij12OPzwlYyBzbUKp2oNQOv5xwvXiVdpdPDL5gi3pGpsctljcYc7YIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کرمانشاه رو هم زدن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8942" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8941">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meCo9UmdNJGddfZ7nvlVWz4gyqzkNZ-gDWDtIWV9JyO4YvWlPVo_qAlnRdnLAZpZ5VsG84ACsu6ScpJnDQB2YIF68DbzYvP4gFHqVMIphm9Tvv0-SI41Lx-taofIgw-KN3CdwMPBYKK4ukOTZbgc1Zb2W7n3u1G4xEyD4O8PrhA-W3Y34p5HghsauO4F8j4DSgqEK9IRh-gbjixFSor6t6QRnKc4cVA7A59RAUQ5Xh028pweiy_gIfCT_348ueU6P2CgAXMPBiHAFGDH7p0VneD3DWXmd_5kpkumbcYuFv97pqGTPA53VF7Pp1u3POWU_KW6hvGBiZmepnLn_A4Phw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه رسمی ارتش اسرائیل: «دقایقی پیش، نیروی هوایی اسرائیل اهداف نظامی متعلق به رژیم ایران را در مناطق مرکزی و غربی ایران هدف حمله قرار داد.»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/IranProxyV2/8941" target="_blank">📅 05:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8940">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jObuobKdLvhtvroUpI-4bnhpn53myVhGr9G4dykXAa4h6BSQott-7sjyANttHYzpxBM6hJImWMRG3ndVTOvV9UvA_bEtdZEjTURhGeywLBvgHkYxyp-z2gvBeVlQVCjSiAzBUfjH7-LaslNsLDOqvhYcg72OlriaiKFUaue3hHaXNntMgOvJmrZGYlC2JjbhAN6pROkU9GRMF8sImod7T_uXRnCR3B3Y_nPdyyvaGUsouuJKr5ALmDHloduqb672ELb2UE1kWHhUO9xDE6VZZdIYKI8pyx_ZU1Iy6i73FJDlb1VJ1NOhfvhY2pZWXmcXqBH49OYnsmIhUSYwRuAS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صدا و سیما حمله رو تایید کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/IranProxyV2/8940" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8939">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sey2buV9Y0xK0z_Yp7zoanA8fdDGCN_YRvJdgz9D1AsWpycdPoJPZeTqoETFYV0pewoK4VWfvWbuWfsMY9Q5kVyua7EATHlL97UApg9Yi040lmvr4ic9hjEKGe7LXpkD9ELh3Qj7YAMiRYxtpz19cO6zOXZGJh6NchPK6nZpThWzDYKFg5jvLm1ub762DPTdVdkiuoPm6UrGoghXjXnjU52jvPgOR1T5kxliZnOJSlbOyPK5xqd_gEE9mRZie-G5gf57r43PODIBb00cW40yWj9ck9e6me9dwVNxUPHHC6DLW1-lMBCcyVyuABD6hQOWHcwrMxHkFDGzsRHl4ioMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار تو تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/IranProxyV2/8939" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8938">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
انفجار در ارومیه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/IranProxyV2/8938" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8937">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrudagpTSCIavF_sIvWv6ZVLly7oD1Dm_RHQMgUTQiJh1LW0j6K_Css9na_ByyW7FqKddA9__F10IkTKoJ7srcMWt2EUOYmr-BBGCwkx753pQhm9BXciolK4RsQLTlsrCW3AE3-Bx_DLppYZkaVVwwCVpP9g7_Gp7uHdHmIhncqmDRTy0VeAQ0xGXWkEmBZ9oFihaKpsbZehtVb-Bupt5rs7XJEebvZPeAcrceMOPSEJHN5bWLXmP0SrCi3RgmYYidHVBOatS8J6erfckRM32ueeyVrwBOpoplE_xRpzUhYKlxXQX7ION2IkvjcRaFLxvBphDSxga5h0czUGG0vbyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شاهین شهر اصفهان،ساعاتی پیش
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/IranProxyV2/8937" target="_blank">📅 04:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8936">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
کانال ۱۴ اسراییل:
جنگنده ها دارن وارد آسمون ایران میشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/IranProxyV2/8936" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8935">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdX0ww33klpsaJEbgoMX7ZCR1zo_lXSclzszwZ24Ws9Hs5c461w6sml0tx-0B8DARPJ86zP8DZp_g3RNhowEdvk9UgA6z2XdSaLErQyBMMfuMokC_1DFkgOThat81CQDqXYbX6cyQlOEytH3vGbriM7QAujVaiLNtBz5HmqCMsiEPviIBF4D-BuKnuVJMyRRs8MZBiH0TAWcCfKk2ixgYavpUl_x53n8QhQSaFOe-uY7yIzf_8-tUg8KTmoxJ-3ggnsadM23LIrcRJbkJgqjTBLwn19DPMABeIF0U2JQs4eZCbHgCKx7wZv8PD00a6HLagU5Gwwqu-kq0A1nEcHGww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یا خدا اصفهان رو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/IranProxyV2/8935" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8934">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUDIXSdO5Q1SZRZfKRvZKoydkhQ0kgW0L5lb8A-cQdZz68lvvb9Z1uQjRscmWMj_JIDUxe2AsLZ-E95dfgIgyZ_NaF7wXzAduNanHOJQ5PEkhydgj3fZG9vdQbNCleV0UgVj3q5F8Kvb4w0NpfK3cKZX2cLQdOB1POvzvZHKRpQmBHyO1QqZMmb3ynRJObPGtihAclQCxin249vnio3mDNBEcG-lZ83kXgmQ6UjFgnOSK__aYsZRW4yhK4E-r51tP0cEcB26wPJ7DyO2eGLL6DLIu1y6UFcwPOzKhMi0qQuso4DZbxuRDhygtguU8PmlW8yAN-wMsDK40ULC1SgwfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نجف آباد اصفهان هم اکنون
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/IranProxyV2/8934" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8933">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پدافندا راحت بخوابید مردم بیدارن
😂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/IranProxyV2/8933" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8932">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">💥
شهر هایی که انفجار گزارش شده
تهران
تبریز
اصفهان
نجف آباد
شاهین شهر
کرج
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/IranProxyV2/8932" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8931">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
همزمان تهران و هم زدننننن تبریز و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/IranProxyV2/8931" target="_blank">📅 04:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8930">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
اصفهان و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/IranProxyV2/8930" target="_blank">📅 04:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8929">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏
🔴
فوری-سفارت آمریکا در اردن با صدور هشدار امنیتی اعلام کرد گزارش‌هایی از ورود موشک‌ها، پهپادها یا راکت‌ها به حریم هوایی اردن منتشر شده و از شهروندان خواست فوراً در پناهگاه‌ها مستقر شده و تا اطلاع بعدی در محل امن باقی بمانند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/IranProxyV2/8929" target="_blank">📅 04:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8928">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تنها حمایتی که میتونید انجام بدین اینه که ری اکشن بزنید و فور کنید برای دوستاتون پست هارو عضو چنل بشن، ری اکشن قلب بزنید رو این پست ببینم چندنفرید
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/IranProxyV2/8928" target="_blank">📅 02:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8927">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">+1 ترابایت دیگه برای شما دوستان فور کنید برای رفقاتون
🎁
❤️
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@deadvix.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%A9%F0%9F%87%A%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@dep2g1.aswall.ir:43582?encryption=none&security=reality&type=tcp&headerType=none&flow=xtls-rprx-vision&sni=play.google.com&fp=chrome&pbk=95vLe0hBBerV1ch9WxJ9iPTi4u7V9NExNADg9-LpcwY&sid=025086f1385a838a#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@dep2g2.aswall.ir:11000?encryption=none&security=reality&type=tcp&headerType=none&sni=refersion.com&fp=chrome&pbk=YWfCdTnr4FAOMYTY2dLrMtQUokyxOGpPhYEEszPj20E#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/IranProxyV2/8927" target="_blank">📅 02:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8925">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">1 ترابایت برای شما دوستان
❤️
🎁
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@VIP-Vanguard.userid:500?encryption=none&security=reality&type=tcp&headerType=none&sni=www.chess.com&fp=chrome&pbk=OfqZPHXqiwjyZEhZtVO1kk9PLxW2ueKdaOjVX_Br2Ek&sid=ce7d30ff97b02e63#%E2%98%98%EF%B8%8F%20980.71%20GB%20%7C%2030%20Days%20Left
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@50.7.5.85:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=dehone.tunnelltwo.ir&sni=dehone.tunnelltwo.ir&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@50.7.5.85:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=deadvi.tunnelltwo.ir&sni=deadvi.tunnelltwo.ir&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@94.140.0.0:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=nlox.nextigo.app&sni=nlox.nextigo.app&fp=chrome#%F0%9F%87%B3%F0%9F%87%B1%20%D9%87%D9%84%D9%86%D8%AF%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@94.140.0.0:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=usaop.nextigo.app&sni=usaop.nextigo.app&fp=chrome#%F0%9F%87%BA%F0%9F%87%B8%20%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7%20%E2%98%81%EF%B8%8F%20
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@45.130.125.60:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=decdnmtn.gozarino.com&sni=decdnmtn.gozarino.com&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@188.114.97.6:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=decdnmtn.gozarino.com&sni=decdnmtn.gozarino.com&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@deluxi.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@devops.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@usaoxp.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%BA%F0%9F%87%B8%20%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@nloxv.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%B3%F0%9F%87%B1%20%D9%87%D9%84%D9%86%D8%AF
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/IranProxyV2/8925" target="_blank">📅 01:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8924">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
ترامپ: اگر توافق به دلیل بندهاش فرو بپاشه، ما گزینه انجام یک حمله کماندویی به ایران رو بررسی خواهیم کرد.
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8924" target="_blank">📅 01:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8923">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
ترامپ به فایننشال تایمز :
من تصمیم‌ها رو می‌گیرم. من همه تصمیم‌ها رو می‌گیرم. نتانیاهو تصمیم‌ها رو نمی‌گیره.
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8923" target="_blank">📅 01:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8922">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇺🇸
فوری، ترامپ: نتانیاهو چاره‌ای جز پذیرفتن توافق با ایران نخواهد داشت!!!!!!!
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8922" target="_blank">📅 01:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8921">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
رسانه‌های اسرائیلی:
ایستگاه‌های مترو در خط قرمز تمام شب باز خواهند بود و طبق دستور فرماندهی جبهه داخلی اسرائیل، به‌عنوان پناهگاه برای ساکنان مورد استفاده قرار می‌گیرن.
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/8921" target="_blank">📅 01:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8920">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🎙
مراد ویسی احتمال پاسخ اسراییل بسیار بالاست.
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/IranProxyV2/8920" target="_blank">📅 01:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8919">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رویترز:
به گفته یک مقام اسرائیلی، ترامپ و نتانیاهو کمتر از نیم ساعت با هم صحبت کردن.
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8919" target="_blank">📅 01:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8918">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مرادویسی درباره حملات امشب:
اینکه سپاه میگه ۳ موج حمله انجام داده ولی فقط ۱۱ تا موشک شلیک شده نشون میده که سپاه دیگه توانایی پارسال رو نداره و تعداد موشک‌هاش در اثر دو جنگ ۱۲ و ۴۰ روزه کم شده و فقط تعداد موج‌های حمله رو بالا میبره.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/IranProxyV2/8918" target="_blank">📅 01:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8917">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⚠️
چیکار کردید که مردم بیشتر از جنگ، از قطع شدن اینترنت میترسن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/IranProxyV2/8917" target="_blank">📅 01:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8916">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک مقام جمهوری اسلامی به دراپ‌سایت:
در این مرحله، دستیابی به توافق با ترامپ واقعا امکان‌پذیر نیست.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8916" target="_blank">📅 01:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8915">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
حرکت سوخت رسان ها در آسمان اسرائیل رصد شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/IranProxyV2/8915" target="_blank">📅 01:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8914">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تسنیم: صدایی که دقایقی پیش در تهران شنیده شد رعد و برق بود. صدای پدافند یا موضوع نظامی نیست.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/IranProxyV2/8914" target="_blank">📅 01:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8913">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hH_FYOQqBaTgzF431kA8X8wYGVnH3F7Otbt0KYa36XV80FXk-1-NuvOXERldaqF9mfWafMJ258TaN-jmEtoYwFZJBonx6dZaitIiLqjulHlnk6_VhMew1sc1f5c_Lj07NYymGsw_zH6-OnpBaqW6nbHYqPrisG7PL2ghiGbgi6Wowvd8EQablZJZIBDQQXBrCgreTAo7jgB3JKXVTVGQ1h7UAFxmrPShAyRUHLMF6NrjnHlQeraxGNxgZOe1Fide1mUdhOgWkARofzoUpRSzaDpCErcmxJBxb19CEQc7uv8Fh7v2zyPi1ojIVt_mYwcrcT2owAC0eNv1KtKRC32zTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پس از شلیک موشک‌ها از ایران به سمت اسرائیل، حریم هوایی در غرب ایران، عراق و سوریه بسته شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/IranProxyV2/8913" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8912">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
یک مقام اسرائیلی به اسرائیل هیوم:
ما به حمله جمهوری اسلامی پاسخ خواهیم داد، حتی اگر الان انجام نشه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8912" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8911">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇮🇱
منابع عبری:
نتانیاهو در تماس تلفنی به ترامپ گفت: اسرائیل به ایران حمله خواهد کرد
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/IranProxyV2/8911" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8910">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♨️
🔴
نخست‌وزیر نتانیاهو در تماس تلفنی به رئیس‌جمهور ترامپ گفت: اسرائیل به جمهوری اسلامی حمله خواهد کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/IranProxyV2/8910" target="_blank">📅 01:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8909">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
کان:
جمهوری اسلامی به اسرائیل پیام داده که حملاتش رو به پایان رسانده و اگر اسرائیل واکنش نشان نده، دیگه حمله‌ای انجام نخواهد داد
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/IranProxyV2/8909" target="_blank">📅 01:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8908">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
شبکه کان اسرائیل: رئیس ستاد کل طی ۲۴ ساعت گذشته دو تماس تلفنی با فرمانده ستاد فرماندهی مرکزی آمریکا (سنتکام) داشته.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8908" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8907">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♨️
🔴
والا نیوز به نقل از یک مقام ارشد اسرائیلی:
پاسخ مورد انتظار به ایران سخت و گسترده خواهد بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8907" target="_blank">📅 01:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8906">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری
جلسه نتانیاهو با سران دفاعی-امنیتی شروع شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8906" target="_blank">📅 01:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8905">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری-منابع عبری:
ترامپ به اسرائیل گفت اگر توافق حاصل نشه طی یک عملیات مشترک به ایران حمله خواهیم کرد!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8905" target="_blank">📅 01:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8904">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
پروازها در فرودگاه بین‌المللی خمینی تهران تا اطلاع ثانوی به حالت تعلیق دراومد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8904" target="_blank">📅 01:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8903">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر پیشین اسرائیل:
خویشتنداری یا واکنشی نمادین، این پیام رو به دشمنان ما منتقل خواهد کرد که ریختن خون شهروندانمان بی‌هزینه‌ست؛ از این‌رو اسرائیل باید با قدرت و به‌طور موثر عمل کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8903" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8902">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
منابع عبری: پایان تماس ترامپ و نتانیاهو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8902" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8901">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH8H_3Q2uKqONN-gBmnjLx8TFFGwJl5Hle8r5EQzgJ4_iKstClz9TWMG7cUwHis727_F1jQ5UknvwXoW4WjyJCU3Q69PPizrbdTAypAD3eIsLp0FlUk_udDfhZVOm_bDg0JbHbYagav9NGcag6g8AS1MkcjjLFe8_dPLIUtb2pewL5p_QFxcJUCiMSQ5w6pJWrFYWuJsvXgtD2qVTcZMfDBkh-aqO9D06c57Wj3BbJEXOkrBAv6p93YSup_CVezXhJdmMN3n1qg3F5A4CbAuo3X308au7piy4n6ITtyRifoIITa6zsIVjenNxXnnwQc_056Jq5jQGIExjt6pkNYlvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سفارت آمریکا در اورشلیم دستورالعمل‌هایی صادر کرده و از تمام کارکنان دولت آمریکا و اعضای خانواده‌هاشون در اسرائیل خواسته تا اطلاع ثانوی در خانه‌های خود بمانند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8901" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8900">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
کانال ۱۵ اسرائیل:
بعد از پایان گفت‌وگوی نتانیاهو و ترامپ، نخست‌وزیر جلسه گسترده‌ای درباره موضوع ایران برگزار خواهد کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8900" target="_blank">📅 01:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
حمید رسایی:
هر چه زودتر اینترنت رو قطع کنین تا دشمن نتونه به ما ضربه بزنه!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8898" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8897">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
کانال ۱۲ اسرائیل گزارش داد نتانیاهو و ترامپ در حال حاضر در حال گفت‌وگو هستن
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8897" target="_blank">📅 00:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8896">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صداوسیما: به هیچ نقطه از ایران تاکنون حمله‌ای صورت نگرفته
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8896" target="_blank">📅 00:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8895">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری - پروازهای فرودگاه خمینی تا اطلاع ثانوی متوقف شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8895" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8894">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWw9JT1M4fWzE0Rvcu4mgwlmxw6tLtVQmhaU4AYo0nCJKhQhOB4nWDWlnSTlnTgAwA-QurTOUUHtdqlW2sauaB7GgTm_S84Ae3FWM3V_tJnGCLr7hyHhwqH7fZleYjiG8ipe6mIKcc0HU_uTYjv4iZhA6liIbS1v-51yByDVNUVtufNIbxHQ2sMgv-Yodgp32xLyIPRd37dyXVLWD9KLzRzNRP3KAuTYfmbJ60COyozl8L5vXVtLKOHxAmV5Ba5FZZi6m_bgrRV0taGdTfsLnLrLSeJqGoOD1s6fnwrYZgfdtmFb48G8m-OCLoOBwB3nm7reRL476dYx0kD5CyVs3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
-
تمام هواپیماهای غیرنظامی تو تهران برای پیش‌بینی حملات اسرائیل جابه‌جا شدن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8894" target="_blank">📅 00:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8893">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1PdCgL_9lHwByXbttWuiplpF6SgM-NtHfuHavI_V0J56WvEtpXBQmhj3_sDnmibKuLSmHH09Z81ShhxmUJC2qA8fwt7yXzV___IRW_n8HDBkLAfAlOglac7blLPMlj0P_eyoGIH-h_2GwJA8rK14SBJlZTWTd8u0va7KO07MVhrnrKtk1syzaY43H48RZ2x33GHQigKdNBz39xVn58actm1OfDvQ_Rq3Sw3aLudFyu2pRKdwuy0qtuzQVDBZRWf4KfPj9426LVTAH0AtaST1ecnXN3oGjB7XKRyjCFLnxobAR2vuJt_-3IASiJrXNY23l81bx6If-T2Drp1q8tr8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
ما بهش میگیم لبنانو نزن
خو اومد زد
الان دوباره بگیم نزن دوباره میاد میزنه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8893" target="_blank">📅 00:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8892">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری -صدای فعالیت جنگنده ها در جنوب تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/8892" target="_blank">📅 00:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8890">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مثل اینکه نتانیاهو ترامپو بلاک کرده
اسراییل مجددا به لبنان حمله هوایی کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8890" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8889">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
تسنیم:
براساس پیگیری‌ها، صدای شنیده شده در‌فرودگاه تبریز تست پدافند بوده و هیچ‌گونه حمله‌ای به این فرودگاه اتفاق نیفتاده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/8889" target="_blank">📅 00:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8888">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری-نزدیک سپاه عاشورا تبریز صدای انفجار اومد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/8888" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8887">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37dbb2f6e4.mp4?token=RbAtliZFWnJFpa_Fd-o2Y2GHzbfHmB_lcj6bFOfLeakXt2oy_wGrYir3W-PPL6PR6brybfcsS-Qk-JohF2cg9ROZJ_7yDTc5LEk7Sc_Mgb1bLc1Qs8fEC4k-xXoPtKA_CRhr3y4oHjSC3KnGo_86vZsf2oOUQqiCKIUMFj3fK9hjEkDm5PvY_dMEB5-Gw4-JzX4qB5HF2y66o7TE5kNRkq1zE9TNZn0baGvvzAu9_zGOl-OLUvrPE6tW34avspoeI5Ba6bWV2ynkeVtUmz3I77nCgnImlRC_lTSmcudMTcIqBWQX5XbUUY0Lyj1tqXxCY93P-sTtCrY7ocv4_8E5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37dbb2f6e4.mp4?token=RbAtliZFWnJFpa_Fd-o2Y2GHzbfHmB_lcj6bFOfLeakXt2oy_wGrYir3W-PPL6PR6brybfcsS-Qk-JohF2cg9ROZJ_7yDTc5LEk7Sc_Mgb1bLc1Qs8fEC4k-xXoPtKA_CRhr3y4oHjSC3KnGo_86vZsf2oOUQqiCKIUMFj3fK9hjEkDm5PvY_dMEB5-Gw4-JzX4qB5HF2y66o7TE5kNRkq1zE9TNZn0baGvvzAu9_zGOl-OLUvrPE6tW34avspoeI5Ba6bWV2ynkeVtUmz3I77nCgnImlRC_lTSmcudMTcIqBWQX5XbUUY0Lyj1tqXxCY93P-sTtCrY7ocv4_8E5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری-فاکس نیوز :
با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8887" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8886">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
یک منبع نظامی به تسنیم: موشک‌های جمهوری اسلامی آماده‌ان در صورت پاسخ اسرائیل فورا شلیک بشن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/IranProxyV2/8886" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8885">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو اگه به جمهوری اسلامی حمله نکنه، باید با نخست‌وزیری خداحافظی کنه!
احتمال واکنش اسرائیل بسیار بالاست...
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8885" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8884">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رادار کلودفلر اختلال شدیدی رو روی اینترنت ایران نشون میده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/IranProxyV2/8884" target="_blank">📅 00:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8883">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
سخنگوی ارتش اسرائیل:
جمهوری اسلامی اشتباه بزرگی مرتکب شد. اسرائیل موازنه‌ای رو که تهران در پی ایجاد اونه نخواهد پذیرفت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/IranProxyV2/8883" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8882">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
کانال 14 اسرائیل: اگه نتانیاهو بخاطر حرف ترامپ به ایران حمله نکنه عملا دولتش تموم شدست چون تمامی سیاست‌مدارای اسرائیلی خواستار حمله به ایرانن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/IranProxyV2/8882" target="_blank">📅 00:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8881">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری
فرودگاه تهران رو دارن خالی میکنن
پشت سر هم هواپیما بلند میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/IranProxyV2/8881" target="_blank">📅 00:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8880">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
ارتش اسرائیل: سیکتیر، ما لبنان رو ول نمیکنیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/IranProxyV2/8880" target="_blank">📅 00:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8879">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
سخنگوی ارتش اسرائیل: رئیس ستاد کل در حال انجام ارزیابی وضعیته و سامانه‌های پدافند هوایی ما در حالت آماده‌باش قرار دارن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/IranProxyV2/8879" target="_blank">📅 00:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8878">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
سخنگوی ارتش اسرائیل: جمهوری اسلامی اشتباه بزرگی مرتکب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/IranProxyV2/8878" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8877">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگه ترامپ چند دیقه دیگه اعلام کرد با همکاری سپاه به اسرائیل حمله میکنن نباید تعجب کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/IranProxyV2/8877" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8876">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa612d6574.mp4?token=o4Enap0DCaz0So9P9zP-P6ISmUaLFleYaADmL5b-CNcJlKeFLLQKZ7Sbc_HJpBI9ZlKgjPrWR00GSSJQTWRVd2FY1mwIkvRvelWcsS6Wvq1FJ9URIa94nXK06cJmSUeOJz2DfbX1CyQqkjvxv-6S9MCa9mlDdNi8zztM-KPS_m-ziqc-tl5MockKjP-8i5aNXgG1B-tCMPaFT9GV_0TkvhnKPenzE5nFtn7d4ZduVtQ4KaL0W4vqq_pVutpQzg_Cj3WGRlfeIvhbrnGJnVKnKbUoMBT3N8VMait00oLesFmaCu43xCCs11i1YWMOOQ8ZUBifxga1tEiHxfSwFpD3Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa612d6574.mp4?token=o4Enap0DCaz0So9P9zP-P6ISmUaLFleYaADmL5b-CNcJlKeFLLQKZ7Sbc_HJpBI9ZlKgjPrWR00GSSJQTWRVd2FY1mwIkvRvelWcsS6Wvq1FJ9URIa94nXK06cJmSUeOJz2DfbX1CyQqkjvxv-6S9MCa9mlDdNi8zztM-KPS_m-ziqc-tl5MockKjP-8i5aNXgG1B-tCMPaFT9GV_0TkvhnKPenzE5nFtn7d4ZduVtQ4KaL0W4vqq_pVutpQzg_Cj3WGRlfeIvhbrnGJnVKnKbUoMBT3N8VMait00oLesFmaCu43xCCs11i1YWMOOQ8ZUBifxga1tEiHxfSwFpD3Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه برخورد یکی از موشک‌های جمهوری اسلامی به شمال اسرائیل:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/IranProxyV2/8876" target="_blank">📅 23:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8875">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری
اسراییل: تهران آخرین شب آرام‌را سپری میکند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/IranProxyV2/8875" target="_blank">📅 23:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8874">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9a9wmyvNUCk9dq1y-h53Eeab39ubo7XE2ulznFSpPsAefU6R38B-PJEzmOQJ6cho-OIM7eQVlaYJEAKmNnx6MHq88I_BjvnUv0PHcteHlYxgQYoPd40Ns8D7BkgZ10pxozx60Wg-VJf16jqZFlIfEpZaGb_-LVdfTcdduoBNxWGa11pCcPS-psOyvevgeCdua6Z9djunq4EFGTYodCHLckhGf3RqlLFJfRyLYde9uSrhlFxtCWINA7RiUOPAocvxyCsHFtAgiIbOr3U-PPrCTABUEk_oAD-ovQ50hNc9wJ-Qtf5_A4It5Wds8ia9azGrPKOmwzCUhY8R_0VBAk55w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری-رئیس حزب اسرائیل بیتنو، نماینده کنست آویگدور لیبرمن: «تحمل کافیست، باید فوراً واکنش نشان داد و به زیرساخت‌های استراتژیک ایران ضربه زد»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/IranProxyV2/8874" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8873">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فعالیت جنگنده‌های ارتش بر فراز آسمان تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/IranProxyV2/8873" target="_blank">📅 23:50 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
