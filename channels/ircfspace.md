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
<img src="https://cdn1.telesco.pe/file/TGflfxRA-F060Y1j_q351efQRz_n8dEuYYGskxw8HQy8MNHoQ7AXsnpX80cr_O3TrDw6WOnjrdbROLMsmTueu7hzppKz-M-1dNrK3MzpD0bjqE2cWThMIpvB8izDbXpB0Ta5dy02klABZXBVh_sscr8hZsuHa7KNr2fVP7qjtrj_zTdZHaUayJBSVgeUEXeCIKj1gmPU66ryJr5z61VArrbR08j2GLWv8xFZNpkwTsAsTyMkrzYG2B1JiDhTBIwlDZWg1_9S-hkTrbWRzWM81buXIDvPJ17hzjhrznJG_i1XltzmFjJzxpTEkGJ5RszQWKK79mt0G2Rj1jjmThX3nQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.6K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 14:44:54</div>
<hr>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gJV67YcPNUma0GVjByok0asZ4XJ5LFoLdqxkC_IWAtCKyuoNVdirK3WJR3o_jLFui_02llNDi1yjp3TN1CqCzvOHZYvDF27FBZPHMQ_IMGgZMlZlP0F-eHSN06ieU16F1-AyTB36pf7x10Vh7LH8uZtpAL_asIkpUo-9X_NcXPSC9NTL3gxtM_pAi9pqLDyussb6vJtCo3lkFyGPW3B0o70wrFxJdTSfdnL8L4aZzVbqZL8tz7lq6XFqKY4bd43pger3HamdJmwGUA_BIZQfNy6IGsSEw5uTUwq85fEvCrcORK8pz_V_FRhdtN9fAEHmDWb7yaBW2UaE4HTup_h1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/il3sXzuflPrLnuvX57y3Oo-Y-gh5IJ21e3mwjKXZ-IJk5VIuqJ69oda9awCtG3Cb4OPnVAiWYZis1qWpdUxe6rKjeeVrDwWvIYIImoLVaViW9iEl1cgE8CMrXiA-v8tjr7OLWFdi0mzH_BZsO1oY8dwraxXIbOx3fVvcatgjE6UjS35qamFF7vMK4GCfPcjk-DpLWNQGeUzb8-uadmE_2OzugdnmJwv38biUPQAmV1tXShEVVF-KClShcLQjVsUaLqQvUtZOUPnKIRXF11q1sL_KWTq_-tpCvY9wsqygEBy-y5eRnlYwoMSwAfmxKTEgBoy25id3zhW3pzkFJSlfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vqKcCujXb0TY5UHEdC8WSoezjABJ3SYYZBU3tRfr_4hGargkVbxD_40hGmTfQq-EACCwg6D3q8Db_vRZ_qiN0VixD1cCmCNZH1fwQ3UQ1_A6SBwCVXa29GOZG2bQTcviCZ7iU6L3-9YRdpwGIGrLEJR4yqyEpHXRvxTwgTGjXvuv9F-rlq0rgXc0Ug1kPCT7pzshSg4lMP6QeNz-WSLUYWueUniyPcmpHqdOoZWpeDcJr8v_mS_6PPqrXISJFeJAoGaqkHRjjk_yDhFXRPBHMQs64Z1mviHBbg6XE28vhFPN_UyT2ns_TZqnue7jOeQKlasPNF0f78nB2CQX2mOJkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fcrki7LZINAQp4YzRSZNmaTzDXidC8giKaGik-Sb9x29tTUeugQ7igZvaLAZ6YilKZUKFdVmPP9R6Cll0z9R1etRR7-8lJKGsDFnm6wM9tU7al0gmMwTcL2KS1AXE-6uWrM3TEXHpI-eauJnWebAFhYQT9Scq7sozCid5Td80Ce0yNoWdLtkvdMErfl9cY3VfvP1GWTDsISnDzQuZVa0zw96auv13e_WJxoS-sEXQtPNrMtI634dC6BakvrSSpvQ2obWlmUcpzCk3dE-L481ufqscQ7Dw61ky7Cc7PhM3iTxMmEaK3lIHA8OR8CJxxlkND5EuZ-byMg4wJ1tM3fQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tugv9vWmnEt9Ez08jFnm6upseDijNm7Zc-IMsmV_B_SF5LhfvLm98zSHEM1sfhVUPDpJ9O78W18cit1N-xuVLaM_xOWWYHxu8izVvF7SH8JDslFe18ktxXcIuNE-LtbV-31TrYwHATf8R8pY_v_y6oiCucjyBulrKn5Q3-4rT1uiW44RFgCjoQuHa2El64npYgqYUpEf7eSHBcCyoFeETADmwxe5AXkWeag_RQfoX1tKFfTLjYJxzd1SVrKqHhy6OKqLRBI7ldaXP9oHlANOsfe3eH5RS3l8GJIbp9YkQH1tW5Pz2trnRBBzLM8eux71UJ2mPQd-yBv4EGtmlA7bbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qXI4ORqOwvy-Saq4FQcrHq9OtNeZn5vEm-Zmp6yKP06S5ul6TbemwR_s_tT0znw7BYfkk6fCXhA7XA_E47qX71KUoZTkV0I79MM5-DSkJcMM3FbxoXRNUXMFQdztzxr4Uep4WVMp0xrTD2_dl_ZYnLCmt349NT7JTaNyu23_mevSnL_Xsawg-cYSJzYSl3B1Vxlcki-bcsho0rBOlhvfQMtTGACnOwnuP2xup634U4xuvzth32oq3VCFenyi__tdyoDL24BGLzNln7jHS6kYY_PNYdSk9rUwGrAB5QWMEygbEIobbidrXPeUnUxHYyLAWx7k83cnhNMyH8GGXtTrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D37B4yc5gmgHpGm3WhOTxz0UEjXOyzamYjXlYofL_Ey43pLugvFMUSKZT1TsnQfnXO52YdXdXyqZs8KUDvFSQjxxeQfN6BLspHGDmylP8t-gieB7nnIWV5zmHfYwouZwZhKIvI_UgatAatb5KIMF-6MmGU2sa5w6wIBt__ZWGGfbVWUC52wQWgN6tNF8wj9rzPlCLjLaJtfR2ajp6x5OZ3AO07p03OM_ossPp-_OJbeoH4Hjq9SIUhnNgsU-76Wz9SVALvJSbiPxPc4FazH2cmXeZxz5Ab3KcAIHljdQKRAxTxzV266TtfTXG7EXp0h3XeuAeRpST1fZuOljm1_B9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hC8875kRdvVhJfOEjyD_ghHq6ez3l5pe4T583YMucH5eHfahZHvPrOXe2HVOYr-7DTHRThlqNOgyCNis1fmXErsjj__dHK2OTMk_7SbntGmHgJlvCbgF_pp0AXvLRukn3K2xuYxmfFQhRtpzL9zokeY1YNu6iXMSJ_57F6i_RyrX5ru04q0MO1XLT0dXji_Agtx0kdkAKKUwJs0koT2-5Of-PeyQ2vNMCo5yVqmaWjlA4JClWFzVAV5kwHKtoW3lxOPgsSbrvvyub-jJdkT4S4OzdGYIqCVExYCNBrUXngKnZ470zF3xTyXQPGSBPV9EmQy3jThW1NOjPDoxSseh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BCuxzjbp8-XAmEXaAEFZ4sDRCIyUfLlhlNp6-h06Yl1E37gCaaYxoCjTUlaHcm8202zPSdVz0jV_XYwsow2eodXZVbDUoIBtHH8B4RV8tkvv3bo3_sPY3CRNILPOX42egfh0OzjpF69vwxeNOtUDz6l8JIj9PH6GiGtssJ8pNH5VLTnE84q6e8zwRKPBzD8U_rF6IIwvRT7Sdi-w1hDbUFazkhEZ_jD1dxQdQflwNQdXeu8E3ZdB2rrtCUH8BQV5kSA4eKOO8NbeKu_VvYFJf11FWl0SeeaAMvOzBibV_DxAoH4XXsDxU8bBVbdQ3wS2cSQzTAf9kN5HJcBC_x7xSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=IVHuDLXulxwrVygUS6LNHY4NOeWCBu_F35NlhKkV6kBOhtLCnDuVMF0MJXS7OCymOg8XVfBqgV8ONjg-x4HT5Jo2mHoLM5K-l5uzz9iZYVcL4qmyxEWZhw_P02TYIoTiX7adMWFzPFmAgDZ5TytXiPvRJhq7lLn00Y-edZHruyq6vilbYn_YxHlB8zWnjIcVuIfBU2EbmeODGdttsMuLCFkVWk2BZ4ft9IW9dVhJC2Gzefm02u1bumOLFvWiuectOYelsmpc5_ckAd6SO6eEOHbUXAm8OSvPYRaVym97lOakQ2xJao9MblEM5_0RnwxcuYsGqZX15pzCtw-OOrqQHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=IVHuDLXulxwrVygUS6LNHY4NOeWCBu_F35NlhKkV6kBOhtLCnDuVMF0MJXS7OCymOg8XVfBqgV8ONjg-x4HT5Jo2mHoLM5K-l5uzz9iZYVcL4qmyxEWZhw_P02TYIoTiX7adMWFzPFmAgDZ5TytXiPvRJhq7lLn00Y-edZHruyq6vilbYn_YxHlB8zWnjIcVuIfBU2EbmeODGdttsMuLCFkVWk2BZ4ft9IW9dVhJC2Gzefm02u1bumOLFvWiuectOYelsmpc5_ckAd6SO6eEOHbUXAm8OSvPYRaVym97lOakQ2xJao9MblEM5_0RnwxcuYsGqZX15pzCtw-OOrqQHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NS-uGaGguTsHdg8Sbk_GVQCurc-yLNXoxPGcAZc6Zz_jpesK9CdDbkclyH4VssHHjCzbdlMa91lhldu-eL2gNUdYKxhyG3IbyfLPViQLJuBFfk94K3kggF7YFqi0yLsvQM6-GvJOk1STBeN3334ZNyuaczdMOgkvom9V44tNeROi5c2ORqBTeScljL81-m7SUIXgStB5TvM4KlN8IXLQ1MukX0vAz1wSQH6G7YkS4RJgAgC8An-pjIUWNULTWIdQgqISlHfCQozCIpOtGVP4l54A5hrc9wz-RKT5xM_0Q4-ZQmBh2GpqIuvRh58tcykJo2-4VWNY4YdzcK-QAj7pOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EPDlXYFAz5oGvwN0_xBcIl2tA0tvVWhy60nyziJVvpzpH1_LgOdVakMZms6rh1Cvvb97866dyjBBLxuyxVhluCgmXbKm8v4DoW2pFPNpVQhO73Vxjz3NWL4_Q8VWGeJVReHtZDd6H81byvz8rvNmSygRmoxhP60xcjzOiKZeesrh3Mwv7xaZZz8QVTtRHeeWnSdUJBOzC4lxN1yI6flle3f6Po5O7ZkALb2NLKhUcO_5DHXihoBA-0ubidXRawnXFR-8lRhtqkCtoE5eQir7WKkn6br-IN_iD9QTRSNVlk0RJZjQLtVpfC5MpwspV1zoKuah9zU8w3_EIeDw6mrX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDKmWnE7GqIJ7P4bFpHGDoIiqweDjg_LqufqQ2rCDwRuAZKIhplalMsAU0WKHeToo4w0AG2dQRHRSsmlabkBVyqWdXv_buRh1JqfJGHXyA8yiXMi5e5MDr9BU9ZLzUq7DhAwXnwTKkGHLshL9AyjtdWtYN6bxMWPdbx-Di-ELLgGZBwnI_YLbk7sqNgs3r0F_mIHy1o0RklyzhSzsr2K0z4ZhReiotmgwmOZIRv_ZOAwmuWxPlR7xy3ukGVMjs4gU9e-O3At_w11-V_QLQs-jSfPbahS5oy6nRI_NgZXd1Dd-ZSRlazCnJlTop25VxHP97qQ_3Of-H-lOhaSEPlRTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sy0VbGpbkIKJBbxp90qFfvlQ9G5WhuyiGFX59O7hiuwhws6340xFd0-PS77t0d11WeH07BYAjdFtFqRUsc646slTtJ04cGcxvJxz85gqbt165ASkGWiAFqPFQ6EwxNiIIQvoYcL0GD83NWWbbj40phsUqtls1vC_Tnpa_eQd0xCtWQ6xHJfLx3qBzMNnkhpIxZVx1fsnPfslihlXNRPFkEEJQ6vOyfiNFxyZ38j0AmtMXNQHr2Spn0iPrQ6FlOqOKEEg4_5D3JDulGap-y7IK0T2IHYPEfTNWTnPl90HZFwhyDVd8dANdhXGGt98dwj4-dxBfzIOjO1AjbRiYUk_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p6PQCohdyfHzCY_3HeSl2Sj-xTUouMw4xa37h0JzWFNLiabLm745EQ9JWqz5v0DaQr8oxJyOg-j5X707NGwnXybSVmD6xgp_INLvfV0yjXpNLoQcGmIKn0HOL0UgoRTtNbUUkGoypw7txmHF9qks37MkzLuRbGr8G2pJ1_Vl_UZ6jTkI8lQx3lxxMeXvlJvQJJWmov-F49ZP9bjcohpK0JSR6VpoZIuDnfeGuPdCxIIsHiESR9QuOvFPKIZ7HkRrU-cIClaPhZsbKowmZFcHL-DMgDG5MyDKaos_ekXOooZJDF-PMYSIE7sF0XU9Bw2apbSIfolLBcVMilbQrEO92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TPBSsSn4yjyMVBXIStcJ08E478mz8cJaR23F8Xmze7ePYEue0O0LPNyRmFFhhwz7T2v1_enYGfwYQwIejwhCo3GfoPzfrsuFModhb1x-en0IJj0rYNOB15W4QP01XFMDto7GB5I_SThgpcUlQdyO29zNK3tJMfu5xDLPPoetQsSVKsGOnh329KCrohh5rxY8plmLkb2YwxZsGHFMFiQBjKFfNF67X-EuM3iMrWHYTwIlqkQOeYMKCIzNaYfDPu7-nUH0Y6Msx1P6HVuHipPchD0T8QTeaZMnqNBrmaXiphOFX5vC4W_-x6aLbHXc4vnaPPSLJ-m62FQLw8Q0X6njdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RwhuGegpydb-Kqbg5BKUO5y2394o58cPg5sLwTRd1m4O2fLKDe8CK8TA0iiB7kqw6UN0oOKZ8F-pfQzLt7x2V-5nrWi1o1xM_aj7PCLBOqdTpivyz5kLpFDljUPEQWX4woGJn0LhK0v2N38DZPUqOT4-fN_6iWeQfcTgW3JsPcaHjYLh_96fySQQDtrpL1uo0FUGd9kMMKXc8vZ7vAhoPHsoFG8QrosA7oHxRUOTx4C6pEWonn3_lyLSkJEjbqJrRV_BFzpEfYDG1Hu5v2dzM_J1sYcSQlDfquT7pTs2ADXpl04RqUMhK5pXbb9J6Mzm_ORe6KtDBjyMajLAT7l37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uvMmw24tc3_A8N91o9JvSLUUe3sOG1tBlhca-jCqGoAQgPS8g-Nt_w47VtPohe2SdrX7IEIdzQjcBvbAeIoUaaizaftTPh7vXmqvipfVISrCKlNec_IcjCH9zwfHKN_HTTUKupF6msuDu91Dc5ByzTJCSqRokQbdHqq7s7JjJP09kCNACb5Javzp8pq9Lpihc3X5SbHIi9dMFuK0rsEMYewpcsiL-9yIXRWe9cVoo4kW7gB-oonlTpYDn31lPcrXJv_Z-dJ0-faiJP3NIoJK45OFcVfAK7y5gcMDuEyARNgahDeahU8ffxdSY2T5PjlM7pUbJFg1NQE54bRhnXjF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KnQ9WD5I8reNIC3rJkHlJQOjzZjv3nwIoWLmjRrqU10jSlm3EWWx-wWJ-wtBaD9nMTcgI1DqJ6xPxTcY7sb8uUceLp9WtOa9IZGtPsM4zAptZSe6Oeu4a7HquZhviPu1UfHTr0VjzktvosZ2XXnO7AY8E5XkkRy4ppHWElbPJJWlbzwDz3KYloKMVIj5j6xKys0s8yqGlUIpjRvFMw3JHtWWAxqi7moJKgWCQN-xaqaHyHNPMG-A1cJkqJG76GX1z35TrYfAmKK4eKIxpKBlndTFep9LNd6ZvIjwbeck-N7SPtTiWu5SBNI1pFZiPHJAy3wYc2_rqcBSqGlxjTwgyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tW3mCH_elPOKiufitLCtCMpCleOrhc128VKcBJ1poD71-TWSsJ-R4EoUQJMDrwr98DkUT9yO77NaYfYqpoMcOCODZjJQJB2ZCNuugRsByP-mpSNq8usPZsYTMx5epNiOMYCiHTO2cWaE58V4b_FxPXA5_BJoboKs64v-AoAifyvWL0_xL2aAfCA-uSnEtcn10esFrmutwrh6KqgWpjFcPpKcaoBJVeUy4ecQxXQNdZkxPwiXvh7vCG68FOuYF9JWtxY0s3i87EDCt_BR7xhQB3K5bz7GkmWQQSRowAiHtWjYaSgTJukZI-luhxStoXv0YNsVvjv9puoJ_daDCM8bwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GjRnr3ftaHAzQm8YrjlJKzpDLSlHhFdhguf0WAbzLaKGubv1oo4NjAZSfFiOJZY16alNDxhDZmV407C5R3BgZCL7BGLCrl3_tZdWwnerzJ3Oj9PnpLfd938NoIL7JFWLrEh9Pa_Kpy6rrHx8AaceKBpUtRrRcb83PzyfRiAAek3yz7Uy-CVDPR3OEF7GrH-qh7Q6d0KLD79IxT2Eoz4Ju-mHc4QWuW4_iK8Y4SZN4Pbx9BUufd9A2I200A1vBtrttCpDjxPVzcp_ybtsfXxZdDp1IvfwH67dFeUAu9cEwCQ2px6SytfR3WwzB_BQVGRDjJ9CPd8EFw8tlrS7wimE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TG0VDAjotS1QQtOgkXAwqSpKUerUgKA0lhdHV8umhxrjxDfhXUgiS-yGx3K5ts0RVeO7tgv6Wn_y_PyseOPfA3riXSDfjVPeoyMezZLvwFeA6jV5bRbv1DlBdi8WGuq53irjsuVJh9NHklfGnbfiF_9_6AJzAGdajXkaMwhtdpabnSybos2VsVB2ppSf26U1ujveTVx5qr9a1dmAGRkMexB2Sslal4QkWllX5gPrQ6syZF9MTg4GranYpgZWLOkBbnB3kfcduS3N1YjD0rOjF651n9LAPX-ypqzin9R2rI5DWgb5Pg0fwLzTmCrFOUCXxDXjXncLc686JgFKdhZfpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GoKhjXuyvyHiSS26QmsOoCS2CJ3lhJh4mBosQhP6mZVU34g6IS5FjryDWrbEcx9G5Go_Sr8KnvqKQhPpwrIgtec4yDHNdp8y1Miyd7Ia_ipzHRfivCItlFtvvX_aGZv2Qe5MSA86p09T-YjAVazIYNWree5ZC0k0EWCrqtf73-OEl7ghzssTGPPJDgf3dLBCXzfIzZI5_jCwt3dRIoJj1qEn38Nb00tRRyyUr18TH2yZ4u_kOPcbrUq8y-JzdWtCTvjuzKmTs43ax98T8tZPco_EW9rZA_Xr_ZT41c36afla5kxo3E7AGYmqPB5YXB1-FGyvjPpkC1b1_baMG2KFug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OHJLnTkNzSjiOvzNH8L1_DqYMwV6Ha0DmECON2mrbfx0fGOJ-ftkt_YF3gPgRQgXBTYSo5s5pqlorNceIymcGFvD7mbi-9f_kseDsr5j0I0FAIxSisD2AraH73NMVQgea3QVSHZLHS7Mnmu7n9Ub7uNNWrGLw-Sj-fNqOkWuABbk4XrKFslMRXdJ-nAp7stTPTPOIKuSReZwgPhYi2xPAibVQSPlR1sEuxfNiJXYLjzrcKPo0ceTKN1EmOASZRpTxynDdN45HmOUBgq1ivrFlgP0qehGhrZIygp_AF8ds7mjKUKsNh6YZLlsJELY-QUVJPxZDVUs1cRwLwH_XgO9lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QpC6Twm_ej1K77Lh7-yEYodu4Yz1bFy5lgFw4MI9FMfsZOdunanpKocWPExhSwHXchgKz5ocGnaq99PJW1fDtVe15zVlvK5Y3g86ZmjjFaRPWgB3IcHFCSqhay9NAuGpVC-pRBGOLpjLeBTuGYJcmVjARZEOu3F04PJDU72Vl3gAPRmIOph5z9E2dhOxzL_fhHYy5TUgRsPkm9VVre827FFLT3vRMztSo5Cs08BK9zc4a8_w2SaFSAbM5aI1dForsL7eJ5uCwpqjIPsLi1PxaPn6oTjE5lR04wmyeUJFshdypdHh9gjdBulV9dpHIqpvthwCsrs20LJannfiax8i9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DdL0R0EQ4IvGTlwDMPJx_DEf2TWCJFkS5tyLc-KBz4epXG2EIhvo1udRFV_Ed7sccHkWFuVFXkx6SP5w5BWFyheRD51kRRcbFPQfLH1p9rSMWe0y4KInC_p4UnnmcUONLConvvVAmwKNEtJvDTQvTqSdQ48UVI2OHncdw1qKXbzyqij-Wkdlavqzvb0yNaxvgw-O4YM7I4mWRL8euAs2upBLey89_ZcEkNCOy_uEHHtZNsmr8cHEIugn9sC62_7BrRjyBn70zlbtaLxjKdgxQk8CryVVRYbHVJUa6pKyVBVV3e990g5dmWxi2vd305RaPyH1_zSOGIDe6Wy-xWNaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b-NvL44UHOM7nGusjSpCpseFzLUxxeIlwWfap8JwJply4ptV_OcJ3ICWEUIAQl_-i1dbU2czH5uidXnF7ycnmDi6evXMAWThvLSaD-ROLCnYSORkx2JF55nPc8SRQ87JLUv6UAQ87gFklKu8b54ei396xzKZeGKoT6_862Qqqv6iC6MPWitbx6mi28kW8-BPLWiVojAadB2OZ5u8ETzq6cQqkk2gCTnS9lXcF9-POxuiUY3doAlr6cMLEz3oqcHmcFUFYiP9q-AEoDzPOLGhZaf-zOHN6X_2-bwUrfWioPUPqFiuuflOodlKWMI3irE0q7qhglRycO_JNU6zLmE8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T64m5DnX9BeUJPCTzv8qaeYil5lkE7NsqZilWQT6spbnW9Ds2tvcEys5B76xpDahZPHeie6XuEYamTbDP7fXcoPaG1EwNcFXa0xrxMOWT0lGOJ7a6VI_UdmLDKdceV4QlZaT79EqCn_nzzuRjHEX5AMIFkKPOW5wzsjQOYqacEBBY99Y7nUaZem9ZDQdSzbxCFOW18ZnsYw0mjw_6Xs3ArnDXsvvC3g1n5S9Y4CMoNTrewS0XGDtHzQDsoWLUvOm95-hKDE6dKUED0JPwYdDIDK2OxQ963zzyvvqcIH2xj5yGMUsVZ2s6-l3cI-Yhs2XYvUqYVkblc5aRnC7f-elWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OekuTNfss3TJijb1r3ySi14lRn5RXYa4VbxU5R8PE07qmRmayO5MWjsOE1T0GXUJYcz0TePHqQepVEZOUlkeOS86VAHqEXyji_zOYZOXUrb1-a-fjtZY7EpkitO4Se-58CiQcP5pWiyzZTjkWkkt2AGmIN0PVvUS-MB7dI-vuPvde_sWcZpbSCQ_e85lw887Jnd2m_jtxhOfouyJ1sQs95BcO9mWAEpSNUROnEHHCK2h-4xsjRC5oxJW-9t6AR7QjDF_gH56WDS6bBwOWNpMB-kYJDTgvmIfrMMHebnoRpD4ZSmaPrBugZzoIBqH6hx-xwdE4S87_VLfyV7rPeLkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ljXG-HsCxO6CIXjugyi6KQnH4Tr9CW7yAMWjsOe80PN8t2fSYTcZ9v76bKUeSedD2sr8PJ4u8GOa1yKcQX8U7nlhpAjEidY2jH8jCJoW50B3_co71NY-LMXX6RExQVc69bh-b34T9bm0nj6MkJftSAdvpKxEAPqcsPHysUMcGoX2vzMv5vN9mZFVsoZK99LiaAjYCKslT6QBCB_ShjpKpbrnu9dGU1rWSiXDUGErRcDCLfn-CE7RMXtwr0kKDmGHd6DQe3-w-FsE7Vi7rdz3xAVfw8Y0iGTrrd2WLIWrlJlIohFBTywjRA7H8k_WGZvJ4vsvC5Nn4bfkUI5tzI_oWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A7jeuitpe2nzOfJ97CN5y0BLUKJrK3mlyPHsiy6rVEa5TUJgMnhcy1QWFihn031xs8wZsdhlTVUUfpwqIft_mILktGKDQ3a1BJozN_eX9fq3nZK6OxycIBeeUUPNBBihtdH1ccW1CnvFIkPKJHBpTBoQUZVu_pAxcBx1QE6iTD6R46axdoTgUvK1k91gS2VGOUleZw0HPeC7YSyNNoJS_tdvNJU60RLRO4_TtFD9C65yuFr8xL1B3rJeKTGgRF51W2MF1USd_pGKrI6WvZtLeyXx3hpkGehWIh9G4YegOtU6C2uyf_qe5FBwkAiVJ9u5nJNBA_1xqqQ7F3ORueFy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OjlKJKYYhEQvnCUGY-14CSafLO4Da1FZJQ6SjNOif1vlrwsqxlCxgBEMGkAxMw65l2b-5Q4SBIcP2u9vhaVDWHq-w1tLOF2jO3Osjy_7hXwkAhHaEDtJYCavBzIl4Tg-3SqJv9XFKk9TzIx4cIs833Ir6nHBTaSQpurp6WhrGqwgxVPfzOoCgQHUfjik9rwKMO31_AFLm7yAPwCWr3Dei-gEEt-Ze5TTt6bLYpXF7djFZUEXC8tn71PRCvHqW9iag1cZpaYxQj18YXcLjmDZ5Q6xmRD32maHE2kk5v4cDgx95LNxzXunsBM1iIMkjMTslBAHCTQgZz7EYNr2N-2MTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YkEo5vVVd1k-KNCMZ0E2n5-PLjtVCps8hZqp1umC5QeBsj3jBIYJL7NWyRDIGMzzj45p-7kIzK68_b-1RJG6vaFedwvSVgg3Dl_U3cc1q3NfJw0lCpiKEH2UL8A9pt-HOpLR5jNEKNwtf8_EE1GNBLmaYlgeMBey6JywYJc7knpwRruvxLoqRp77aCO6qej8V3-n_sJL9bqz8PxBsuYB1RdUAUn_tFV3GhVsdlAn7vOnmcFSmTSjpPQ7VcL7r1NQmEkZ93Bh3c7ndiPQerJAyFa7EsmnFbX4rvPtygNkhb2ADITjYDaQcMabX3WBPpK2f0Yqvgd6oGg8TvEIdan74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LWACQ5tsEV1xY1jQzWRWNt9SQeCfJJZ4hANzr4EzX45EivQiQqBxo6QM4N_mZ3Ih9-uYU4MnbYxEBep1zYZXr4omoWsvTc3Z4Su8S_n1zHPplvO-7CpRcy5F2eXKkWjtqiI8pi_IclZqrqusOU8NXSSm5HYsXmPpuByWQS1DzBckMPlNb9Q65xicZ-RaxVrou09Wyhyy3a7rwsgh_b8JXFjnPb2cnE0FwrCBmfevVpcl7XLKROxJogVDCVm7asKh74962BE1fiHLe4LUycdL4-VMfPynEoTotl4kBih7iNR4Txyai4Lq0vJpxJ7FQhx5qjGh7uaJlQaDXxYG8AsEMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I73WWt_kW7LFa8EVZAuZoEgZZwFFyqoOdgIi-Z0okdXY5mlHSE-ZFHrgkGt6XgLLogt45JZ0UNaspbPZKDt2-pGSHJf5xDSIMIh4tX6WD0NPBL9766ZTKDp2gnx10EsLdBr-t-2gLszJlHahrPWRBlxF2tMiSkBLUwfoqvIFCmr7VfzAqhuTR_meXvjeFddexT7C_FXpgeC_YMUcWGY9LCK-0MA5r0j4DZcnR-Yk0_pAUtnXR4XLR7rccB0sOJRo6j5XEWi_G7KAHP6ACI_-a7STSzEGD2o7zrEk0hx2A_D0gL2xxQNNbLnIiTmAOEde2Y3UNemBC8U1hBkhN66YQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bOUiKxwW7m0bq65x6G8A4udUWMFliVq2BJxKvS2gY16qfXAOm1Q9g9l6XGT5-gewMP8vckS4M-oxIdtc2X9SVTx-N7cqeqZtVt0bynb17iqgTT5A3jEpoEuaFS_cy3hgEAK1uz6gPrCNwM16o5BnziVkT2Q0yICIYTHqnXgy3aoZaU5mnsgLKOO-v05Crh0dKCQITfpPKcB4665HkkDELTK_4WAzsFk0Fpeo23UCHY4M6zXJyp0-19mDLitc6F9cdCDYG4ciMVxxXQiYswdFmL64eLm1jcOZ9I8i1ylLKOSbor0Qw6K05eMPx4yObQVL7ayVC43w83sMbvZomIHPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GnoCnvTwRQlsg8PM_UNvJQ5FvmTxFhtX81kRd9ndmCJAQqg49tYlyTJfL9VMUNtqB2hjeLaj__pgbqM6dBzx8dHu9hrkHxwmeJx04yEnEZgpxIUKfWNR6ivqu-4nFHZ_1pMXNkkHIP5Au3RFV5VR2bnsaNNDknbdvbULzKxSORM_AM5ZbYnq9cc0acyAWrhn3JJ_tLRIrS1tgGSw9d0oAV7O-p52a3u_hqpFMPlPgxPoEg_IPhO7MNQjhsRfUxc3aY42jyEWiYC4U5BkaHHmTbvGPVcJg7BB335uaTWJ8GS2mOQEudoY42gYjspQbx0nlseqWeggzdIW3R2B6Rcvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jnVKBWiIacYoNLIvyz-qKX3pJA_Do29ZJrhMUgJavs2hCq-IOsGFN5dot5uybhydSh2e0UexAA0Z3ZRNBveDzB_0ju7-0s6scRKx59HsSTZG99YNcuqxIN44NRRzAPQuZyk4C8JTQWI11AF67OGfnR7wlSU9GGRvP73RZOYayLpoPm5onL6X-gk3W31HuZCM1yjT7yMZTAWKlUoGvWxgn_Dlnryn0PlzMWF-fZv39meV8VDWAVFxVqh-9QUORj1GAzxmkPo7zwch4aWdMi2_G_EEW8g4I_86CceloCP-EFP_MvPJxUrOn6CJLCq2AoCB2GDEZvltKNHmHraoqoDY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fXgU2bINXhnFRYFqRXObIK4B3iwbTbsQmlr3JrOvd3tcccEmCZCplvsCuU5utEXk2PVwniT9DZD4G_9Al-bUy3moFg09-kHME3fb_Bs8fo6a50jJumJXAEI_PiYjHrFCNbTal93kEpnIzz8Bh0Oeyre0UjZ0DIofFmbuBs7wzvVtIyEZxdYscQpekCcZ0bGaE7mcPvh2Urm-3AcW8NnFikaGaweCT5yDfQ4H9Ag09AsH9CvOtPoIDNf40oUv_U6plk2JIapGlT3nKwDhEkWfnki4u6j5xo-KDqN1niIfPseODh2UqjG1g6kB3YtLgI6FNVwrpVBQm7wPg9kIm5K3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vUC2z371bdS1-LyeiIzUL_RodGia44edbpiK9o4vYj_dWiBLyhkY2A3BlYs6AvZwvvd74nX07hV9J4DlgC4kXFAEqgNaA427IRPiMXvKExMIWmnA1k5gwC_0SJojWncRAo_N7wZAY7vAjVk7VN3vIgJm_FOry2Doe_7dmbVMsn8l1WHG62SgzxSqo6EpbVW8zeqLtC2Nj4j8ALpTT9cWFNUEar5p_fXm_oOe4aLMAxC5XeEdj-zskggEtaVPKIoGP2QpziXrdI37w7yYtXpA4vm4ipvZ-XNHgQ8daHPErQNIVdGpiMAejsIoLzRsp9fJySRHPi6ekN82VlMmoaHCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/guh7r8TWGs_LrlYqKE2Go65tDoi22ogy4DvXr0LWINB7tEt0KXtWg4HipTDmap-3qsFyVa-pQgOKZzH_qDIIfiHu6AAuy9Cw0tguAU3aFocBvXCrLClYrKO1gYaacqFJUE5p0x9bxTsXVUiQtMekNuR_Wa_7VBUfXkhE_cS5kwbUAzHz7SAh2bKLMoKwKPMbUWT6hARWn50c-hpukwz4rQTIJedNTFHSHDQE1VVOEj3u3XTn0p7313bT-HZNy1V4FyjtjiLxHFdVfGlrSAyrnBvT1JDhw9YG0cH0e9g2KNPMCvLdU-Rtt_DMbeKP35peT5kxN29dRny5W10a8TBXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iEXwH_Pt2GDySDZBP636QYvULW_JBC1LwmlW0GJhR4GXQLb_Pje3GAU2PxRkQ7bRocmzZl3gZu-7eEXnX8E7HS1LGBw3_lIqFPu6Nt04ijof75Ty2i4_T-sXpQvuoL5knnEzHd82dBsCrVXhRDlFXm5HYJqf2-uzm3i8Q8yfQBgBwRKEPTOv3cVHSq6O2LST0X7Z3KgIRmA90DE8xBpYTJbiCXh7xPZqH4yaNsiNLHeuN3fBki3OiQK8AtZIxKiO9nC2jt6TD7JW4zcocVbLxuL4Lx3nksha3BA53EPl2JJHX1xzqna34r2Ijbw6ZjzdqT-GpqLKbUSs3pcCJCtfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YMAqPp3dS3B2elmsr1woX7kEAhmAZqQwtkDRgQzytCsR3Dcn3qxp-_NO8UpGuabhJ-Qyzy2YHlCoNyOoBy7b9CKdns2zmWPMs-nv_nkNiNWwbjDssR1-f7Yb98U8hm3QHtFWOWCRg-a2pT9rn0UT7pZ1dRKIcsQ1CPLGrp0aWI-AkaaH4vSbpH_GTAyzvBuPIdntqfHGmexyklGiyq_hEIuML31Vj5EqA7T8cTI2qBorqow6akBqUWGUJkX1jgoWLzAQ5XJoyzEZ4RYwFUkLnvK05AdDNRyLHM9oW4pq6dnhfWlt5yryIpwicljL8yvWB5Bf4FO0KP1AZ6kUg9PQlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H-M35tqqbajVDlqOqgRMOfLUKp2YOONgXnhofQcOwNWA7qouOtBH7w3hjUvRprVWt1OXGQjKk5BfQkT7bXopvd0uZmVL-7KjDCb13s4pe-ncTXPE0jgYb5vWfa3h3Rutp_EllbZrR2ykkUbCOOwWG-AFDRTLYaJUQIiVoMP13kfTV8JY_a2kvQpdXJKblzxpaGDa6jIeNdfi7hxcPGam83tm_nBuFEdD4QBF3xDM9AikBnxEDRT20k5YHU5Ci1YX6VLTUBe8NVSVAH27b1eBec0oTmTwcT1cEM8op1kpYqoZ_VAkCOg4Cb_C9zbSkPI5ChT5VZhYitTd6TiwScBMJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s-1Un6GA_JPkrBsA8ShKpUa_fxBP18t6v5U7hNa2jNh_jMI2Ytnx85ZQZ4oXNY-E0IcfPU2bRGCXy3bOd-MRYoGFwKDzUKMGeZfZF3xtvSARpayE0hrZbVMETkK1rbJ_cj3wuIWvD5jbiSuqm27hGM46XuzBsn35dnw4Na2iLeaoOnX3WUKOvY_0p7UY4iZYhE46zjyFtqAKXkLXBeF5xvPBmhuMhDb2zgwR_UzRHnnR_ISM3sal2JRdcrGu3faBHoyC6CbaJVcb08gZQGbV-d8NUjcvIFWstzC-YZYJL2pOP9woJfNWxcbkoXLn535S4PT5ILOROqpYw6B-6v9J9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u9VYbeA64gzAD5Qt9eZSANj8f0GkgDpN0Z6VWzzmq-ZIroo5EexHb97_yHoRVr8g7qZ6O8taWL_eiYI-RfOclgNDlKjYmiSPHD6AcUuXpOIqtrd5Bq3bcZcFA_0d4f-KJfqyWXo6xlpanr3G_QowLAGgH5L1VqBEz6tlmNSDo91F9OaAiVDsYDWDh-d5WTYkfY8wAc3rmCbWU0F7RZ0adqHsIM7mor5pdzcvizUtDjz457Qlxor39GIW_hXvshce8NqvshRGv15R4pRSMyL8fByN2VF3POoNk8Jaru4-HxUVORJhZj1WSz0w-sqvl-AMeowtQTxCiOIRJIW6vC7OZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ImHD1bo0kPjFxoR0ABKgaLixO0seFSr5uQx_syHlDnkyuPYsLlM3KN8E6kMjnYRbWK1jKblTIVPiL795QHNAZbHIW14f20W15OBJNVe3ZIxymg9Om3v9N8LDRZ-whMFUPzCB1eoC9u6kG1zgSJVkNU-WnJXy1gtS1MC9YjWH8yToJcV9r_JRy1wzOdubssrovSNrg90_9jLj3kmCX2UHlQySLj9dyEDDNoZCuEz58wnOVmqV9LuoS9nbFc_NVtLYS9pxQBf5oScKJqokj-IhwfpqGemsWQv3ybOvMpR3bs1fHroYdjOnJ_7asB8pgsBXGtkj1_KAovpYBg2OFGE7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/seouaAAUd6TLQkt7tOtKhQmwxUVrMjn0Tyf2hNyd1kVC7RBNtkeTgBEWSFKyOLalvAaFznult8ykURe0C7Sb2johdu7ZZ9TViJ24dcvpAQw5s8yaBrZ5sF1AbCNzhEdmj86dyRe4DW6-3X8sDabsQE6vxFdM134iXTJugzDk6HnZiAHlfk8GxERoX32o2ula5eTeJ39VPNQFNUZBufcY-dTwhsVc-JC-rqvU3CzRZ8yQJE8GFjazWHe9oJipEfZRBbVfOX8q5MBtaaBsUJxEtEWGWxwBZw9VLSO5eufyw9lmcRllTmU26W9ytl5MEdxkvBnWQ0hWLsvq1_Y73brIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LkB5wcnLzkZxosUV9HJzRrRyl79YpNmLUG6wh27Bfn_6ZRZd3a2h4CcVbWCd-DkqFWuId--OsYJByZX6QlTy8zjkw6iwvYdHbSc8ih-zVTh2iwlLnUnH_cp57GNUJXpuyHc39LQUfUYE1Ab_TbCPQZsbKWqLemg5QlAb5bbK3S8SokMGGpbiUFiPrIdm9mv04Ka-1G_zxdLFnZK6bJcydYjx4Fo3Y3pd0kh6I-yN2b90mG31scNqhoxGGd3IdqbJAdDOFS-6yFwI0kTGICXoZUILs2rMtUBOhtsSjr3ZGBMOO2e12ZKj_in9NliRjM_pSwClVFPDMeJQvczDcprocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MsnPO5FvHpkGZi_RT9i_YSmD2FUyOFJh-oiP7Wd4ugVJdRcARJTQQwnKIagfRlKOOLNthPqYJzgSbtsVhrDUTsmYNwJ6z36LvCdg_8z7oj6hjOL15K5-k2H2NOGbvfkImaDo3uut9-Mg97U7wCTgXbKtrIvSRdjqtsrmEIFoxp-iXuv3j5JQGUWRcxI73U4CCLQMFpVNs2wlD_1CO4sZUYIA6_Mf2U0E60S-OyUhBUIyW9F4mg3JcbHm7MxW86W0OGLV8EKTBTD7MyVWRwMkqQ54EFlzr6jmYoOfNWAu-k9Eb63ZLiyxKJOwROn3aNjjSsmiaYNGeaZsJ07R9fSLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XisBvaW3AbrbrFq-A1KnLS7dJmHIRU1AyhCM9L0_8p71DoQS58hr0oVlrT-T-FQx_PceMFIpB0jQ6ssiHtk7HwvHB3AxZ8r0OyW1Pnfacpi-qpJLRXZF6pcxGy0LUEZpQV40WD6o7xHCkWNI-D9QJ-FigxzPBGouiQpq8EFvbezXb17a49gfcjbRPN-p7ruzOvDZuZz-E1BkWRFiDPBR9gN2CjDog55kEPSO9auvMTmUthgA2lTbEK_odjg93FuiEQ_mLnup79ZqL9BS9vmb4mVNkuZBtWd8fMkmOISUxWbNMbTd5oqIFjYdOMGvvv_-JoIgoFvBfIKIXfeqRWheWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UYha5ZT_kYAncTkZ5qWjZB-Dfmwome5fZWPfRgebzYqSkoUoopoUQfzWRsjnJFApoW7teHTaaN0u4FCLnb4U528Nd-0h1VKwrkxGitRndH97lO2b_sE1t3WQTrBcy6Oo4w-8q-PTFgQbENQ-nK8g_eaxYERtdDF7MUY7PvbfHILA5IpxyATTIyo70lBqk8dv6BZOiF40I4miAuCX5Bz4tDqGOqVojGC-8wlSW9fjajc4vLT5jUkr2WrM3BjtK6Ouj2DDIRv1xFR5UtHdqJNMup5gdAh7vz4kY8s6gvPv4iU6wBEA7aELl5Q4FHWOz8hgbJfYTcdw0jzMcevFMwgWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i4I_dzwQ_xSEys5o4AEgyBU9JkXmpbfKtJXYO7JM-5ypOPZgtOyffbmmYVadqlpt0DB3Hwgr7Dets6WC6md1F6OvlzRZsKiURt7c9wzMLtaZHMgTAyWDAukVPIzP0Pz1jFgHqdAGRg-zwtLs7hgET_TjpDaANLLt5UO6QPOVLbe8Dt-eAha2lTkYE9j0ukTa0nnqoCkagsMopAVJYUW4s6q7CjGQZOxpFkMP0Pl6S1sU9_h_DLuASIx6BfdNW4FKzRX7VtvJ0Su08vuXuAlpC5c4NTmGpcEuJSbJAeYYeOXQeuHhmtHwDZNXdrS88Hn5sPIZcJmcnHXC3AkZVc6Dqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/owpZ25r7ibBgfl_ksZWH2Et9YbikXoDv8LxGrAFaPccSYWurTwKBY20jSVYZnY7zPaZNnhvjEYvLp91o-peE7bX6nXAbmVE_Ni_gk1v7C9qJRaiFwjqt5AZ_4Jvu36yE-YxkJNn2F0j3W7PsucR3b5l9butH6dGfL1IDobsal5TyG_ctEUbMIRGQDKxkdDlNh2MKo8a2dlKpuWGOCk0Ta2LpjTfM0qed-7WG27KtTcF3bS2QrT7AQiMuHlzS5Hb5i7MuEXoFuIvRMaJxYGK8zoQs-mGS2o-QavnwCjEyYbmzWuJcjmSlLP5_RiIZOKwFQcLSO5IAnmP_OSBo_RM5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i-eiot4JeW7uhi0L4OBKIliDs3ocLjIsTg9ITJAIpFiG-4oqRoTxE33_gEAOY1KseDRvbDM3Wd8pZ9IEE0KG7hL-oqahttPp8x5u9X7UQ7LXUwkwwy6GOXXaEtCHoIfJRMMa72MbUd-7J8t7Enub7XsBDKLJbFZPzbGcB8MU_ox0NbCeVy7D9uaNZzTTzqvC8u7I_pqivWssYsI0MpX6hSmoQODhKWgzrLuevhc0SFLSpLT56CpPwmd5lZuTh5QWhYEgIjEBsE8oCDdueVLK30IUyo2HZK1Y3CJc8QdVV2tIscBE8v94vEePtLVn9-24OAqmWEcIE2UH3nMtbGk37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PK1hLkeuagPeb42LU7Oo193OLtEi8v9kHLfjV4MeD0ZEFx-dnk-Fvis9nsMiCMZFCTMTKFCJ6CtT9vBJyWVKjSH7a1wD_Zn7MjN_no2AprO3jTRYCf6gmIGbk_Iu_0DKsCJvh80yHjhthiwAAO-IOdMRuYYF7CtE3r3wSxUOcelzF4Is865OQubPU2Np9cnTurPNLW94vL8BZUda79gppTHzMRqvJjH57NZrnO0nMasGUPNIwXgm117CoAdGukP2IS7PiLbdQMfBhs8451duJlJCb6hrqf5JtOYO4BdrEuMj_bDVZYinwTA9vcoOGtKd291_qXnxfNVwhMdKAGG7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WosG_EODGespzYzSBgbSFNU3r0Y8AZjyNroL7vA_HtypDEtw6opymej3_7ydvZQ5Dbo0FPxcCRLLi_aJvjSFbkBtBSLfgs_IVN_3jPH1kcmhz9Zq5gYQQh6g_s6vydMtzKsNrQ-EgOfb9S76ERkxHssSFjYNsZ0p4AuoE9nUpT4Ck4RHB2CuUIwtisbsLC6At4O9UZ0dJdUVbQ3YX6qnKyaowu8ZZwOL5DB5fzX2vmS4sbPTtXXgBZ7Sy1ixT826BIU96Y-py28ywswj2gIinVD66Q1PBh4S-qj-2l5sBcudiQRPGgp89XjPnbJkUqJevzmuYmB-y94uQKmw_9iTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ba1dF0ZydTdnx6cJ9Gptb01EamCDeMCTm-JlshVQNacWZdKavOFCS2dZ51gaa_GVlREM8KHqa7IOWm_ONNW833Gul88vIoB6xt4_Koz0A156qv1j9HO6Ce5S-hZ9YfhG9dnzLunqTwvcnpMUR_zvjFc6FqRpVypGE6_1Fd_sSVjTDggKwE1AIQ6G1y2YcfHRpGQSzkT43DJ936Uq120ZADRl0fUgjCS38gNQ_wfE1YlZ9vjBbrLY5ZQEOIaJZtQhxiVAikirsa9yJKrismYZxmjx7MX-6zvooCg46PYFlwZRPrfrSLB95n5SSIwtWf0hdGFrPF8_jCL6kOu2PwpTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qtvoUjrywsZ_iskuHukKZGAqljPn1LUOXuHtY9uxbOgkkUVBnwHGgilMb6NFvIsI8kFNW0GTQVg7wPNfziqIOlcfFf3i8Zf4PH61kUsXiBMYd-5vKyAbU-OBuMt54sDpBl09gU-Uigm9Qvl3IYn_Dod99EsYl2augnCSi88QxrFTWbrOruabrxRVUD75Htw4lmuYIB6UfD3TbqY_RYFhj8k56CDxcj4C7W-w_6B3zui8uc5Q7ndpbwwly42dv-jigbhHhgQdAJGrIov7rNgH_-ziyl8SLC6bxucqkTssP6ec0Nzu6hTf0_I0pf9jXnREP3t19q5TfuU7UlsLaYzs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a9rjSrlON5y2U8iYzBT_JRYWRru8BNfu3v8gt9-HpOlYBtcTM7zflmYikkW4Ih1SfaONEeS_XjXBz7lHplV_gVOmjHbttmjsxe0F2UlYDhXflhkvpx2k_tqSKGhnusCXIf41duycYjvUChxiHHXfWiJROTPzT49RxcQzCo8Gqv_wJHkX7QABqJj9hHFujC9rhV3CZkwazn1PnD9Hvr84SHQU-q7mXqN5F4RdAfS03OLfl1gBa-RHYJb49iuk-8X84wt_195Cra2E_KBClZPOhlydbvZtmvUIklGlFFPSCtBN4z-RY5XhhIwPMPwGg9USWXwRp1719HdQo2EQXJqj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ChTlU7wS3LB8RZOUKxj_WgTOieHcqoQDXOnJ9sP_cldR63-NZddijhuOQP-dW2Ky9Uj8Lthj7HRY8BBsT_Vgzjwdnfjudi_7P0uI0k7fFGs75ScYEImaFZTowXG6HFX89BW5zpmBS8tLzJSzNmoVwhNZmL99EBkXFJRxEdN8GR58LHjmwqhzzSgsYLGyLz-O6hDCfTYSx35FgfjyNd_rDuqpjx-GDzkCo7eMFruJxtxpSnU5VRVd8vMN9N3KHdQFyvvwj9jpCzCdB70XB6IjpyngqMTkTr8_lpmR3DEdXBhfupCNhKuqvz6Ho8O5ve5X3eN_Rqp1fhq5DbL-9K-f4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AcBoUK6YWeJsv9vkpaCxfO7ZLVYILVpkAA12ZEsdT-I0cf-Qqhxy2ThnHrZ2u8ctdQnRuHav9eR9EmyeKWLmFMa6BsZpUW1lmu3GUTqKGqKX1rA2BFf8sCwNNvBWTO5i3wV2_OOg8oO8vR_iXHsTefBKgwzr7KXyJr1uGofJScC2cSOTGzs9il5td7kFxm___uRUs_0O36RC36FyQNZKapW4dOrGmcQbRY6Hsw4v-lAxW_Wl81nAnApABAyuorRBMs1GSKVCFkXX6RHAniHuCo64G1cltAYXT6W7uDIdVDvR77zIm6ZOTAOqLDyHYahoWwI7Y2iMrnIfLOyCQn3Pwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kc2Y8i9L3iqMNym9QXOLp-iMubhGkcFMpAPhisQZwITtfVY_UreNLxfhPvP1qv7SdRr76dgfi2n3J-Q8LhKfz9a-57SAW0YCqo83ErdCdVGLIyBonPr_5YHtb94NXzqS69hWEmS9N5qwgkJ6L3XQ0eT0IqzHV0jrxJd2gQWsRf46K880kdDKYVXpQnaEUD-rLdLYSWisl8fzgcEMCqOJDACk6NDmQNXCSmlZ-ZReLrsCYPG2N96ZHLRNpb-3eThA_QbQDStW8Gi7QJ9dea2lSZ188LZ7fjEQfFCPQ9iJnxLHI6BdiGrbKMAd4Cg9k9umuASsM9ChcwQHig2IUVXk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lk0PaSYT18MdHy1VxkuMoVAfXtCG1d5Wd_Z6CEHTYFxntSSCTTDpEiJD8LBl0xU-8z75ataBClbRRyWzQhOvQgUBljTxvn_mhlqeOfg4o35BfE2ibpf7z5AZG5uauYGBxFop6UDDJmqX_L2-H99T-9W7gt1pq3i190bC5pE_nEsgDzUqm_DwX10pU7AC51aB0DJHqAfcLG7gt4j0rjQSIEPtg_aOr_1CK4qQmGKpVfKFDa2liOXi34KdcIDT501rVqdriyVm-IQn6OGCf-X0Bz-JZQsTE4HC9CEUrMiym0kbG5z-15_mQQINZyvy5dp_PFUI49VRK52_izYTcSuj1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OTYi-dzXeF408vAjFtxDitf2yKAWwAvHnNF7JWFC_Gqc9TBsymARjSRxmOD65OZkq0Tr-v_xKoboNtTzbvvHJjjYV7ELBSI-n5XMU0gNVcdjEYY81ygHkG0p_vdhdJAziGTgTsLEv27Z4ow7w7ClxC5T75QBdKKGBAun8VAgx3Cm9qyzBkAGrdi-3S5uYMohtPygE7xgy9dTuLMag45lS3UD9qZ_9B2VyLq7KkaYxFZUI_5xkTuDn0qBn_NNnl_uHGlbV6N6xbmld57BOJiE7SF4aHzK6DpFc8FSySuNnMgsEKkO8NTujNuENiIw1TFBunutBnm2it5Ibt-2Kc08yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qk56pyM-6KeD0stIuwkI07qsvd3xk_aTnAHy37CXBiEsbYxhreWU2Kaj0HpazsTyl6KY5XmSubeHmzXke7u0DTmSW-G1iTFtzKlVxfZHWMDbLUT0uiAXhtH-lzlV22jHsP2rj7TXL9hRWDZ6TtWTjHyZyBhWTpkQ_Swd20hrNR6273hWgPR5uDoWxM86TCZpOJaqOEbHFMHDnGY_3fRF-em3Y0vHptzpLrFTKv12wtkV3CTrQ8KrrvYP_oeTA5MTc4w7MVQW0yIUyg16ytlKLUWuyRHi6vdA0ZlxyeCBvhqj-DlgVPuRRX_m8DgbGLMY4AEMuV3hQnUIQscvx9PwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jhGDbXSuo_DXXPqrnthMimKt_oNbW2NgMBvscIWAiKBeRsdvjyhUVIFSB_jmNzRgJ1MQVSJhyrE2KcVZhkCwgdK_gD2g5wI7DU-GxH_1RHcNH__Dylj5Xmv_9-QzhPwfu7bf2h9nqo5TZt1UpAplJ7NeBZDaFgVMKUoYSBAkNAEwoVeUfVGGkFF5VTX1tzXXOblKAocaSWu36GPsCjKFmDFDIFBBAbr716OnDkogNjroceG3ZmvyoalI7nJn_gRAd9JTqJh1tWtC7C5thFiTrJJuKOf_FhbEbl3mwDPatCwz6dZUkRlSCpX3I4wk9fJgtsjVBLTBZ9Vuxui3TMpMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nMtgaq1LiRx_Cie5fg2svwZhtZtQJb3YBf3Le_eqdG0NRGUSuKbnl9pY_lKceAaT69JSo-IiVLH3gaT45ERiNjjbM-K4R8sgUDAMUEEcqruGdCeiHmIWwAfUnjg-2rYhnla-_OoM0CG24MgH0hCaxPItnz5sOdJJvtjEKCICucswmFAPoQ-N9IZhKDzV2u3IwDnf98QGEH9CLVjwVOR8QhO6LHrvozgD5Fn_L7nOrBWfc0xC3ruS9m0AmV6Pr3shCaUrTrorpZb1QWMX32qEDnzHFAsIot6UqmVoF3TpHdZcxHVH7tz0bdukNEAKYg1YseXruGGyFv_zXS7oFCgagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XQ0eygPOVlikrZYNs931im0cllrPMRssfaM9r7WhA7kWGBFzmjvvT8FgG67ASJF31N2EHlybys1XcP69uNBhMDbb6IlAfrOv4luzTKZqAIZXsjaN_Kz-RodAP5yMx4fx8yFQAP1N616AiYEqvD2OwNuX0vWiHzjJSvfkO3lUZNz3E9HwKwi_17Hy-IO2kgmXOxy7HQr3Kc08gMtWCauvCWOiPp3zCDe4bJmsoPLwe5bFGn_d2TOtVum-w12TeqbSYdbGlS9QOY1HKPPd2dZ5Ha7G7dPM8vH6R-0oEmI_T6nq2GecxlDnuvyy12v48JMIJ-qgE7Q9jkxnRyTe4i0Q2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fzrdHCtbPLsFN5lRP6IagqqpOQvzymTnZiK_BUOyuAZTdayBERgd2fwRg0QoJYVwOLTujuEDyeXk9-pytydj6CiZhvx2squ1E6ceYg4XgEweuc1USjiHKs0-X-V-nb2bQ7z3MCG3ptI9wIeSdpwSnfcXCg79HBBtqFu5uYtoWAB72hTUlHBWSgoi7yyDN-K5QXHk5jaYGNG6CkQQsK_IYTpQoYE-a1EUoiMVppIvzdTFHgRwMD1onDrpoSDv5-g7fcH_xBWxBM12FHwBvZO0zonisZfHIR6Le8rM28pgXhPON12gGJjvl_f6Nv5S1BPFaUhHAiulXNLergWdn11AaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BIndK0ACdZ6HEvFQdNX7zuMwmCNrWhyx3UUvdH-gUNt7VXbyCMhOuKcnLLX4HDQ6wkD7LEEcx3fHon_8_QCXzjlEboFG-3hOGDnnSxq56KBugPl3QJVRhhuIeLRlIGKHF_5Sp_2rHVGKrunMKb0bKtIY1fk1C3zpBHNU2-UJzkU7G16PxUUE7fKwa0HIIxetN3do7giRDRciya6evKxbWNRXud_JFAY-f0B1bJG7SB8bOQyiXuF3d8m84y2Cdua4y_2eVDunK3fpuVsifbu9zfTYVCqOzdZoV16RZum_8qko5kOGdiTdrnVA2hGZu9NzBAyj3m66tW32yW2_tfXFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
