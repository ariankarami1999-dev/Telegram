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
<img src="https://cdn4.telesco.pe/file/RK_hOJbZZPhcCen0MbD8U4BMtN_iNkDhCtizsqqxJ0lmfG7SIaFslb6bKpGgAvnN1zRoREinKTZWbkkCiG7knstKTJSlwhYX7POvJDxGp5FLmtY70rT9ZowJUmPI301EtXGVGIlSp8-leiw9wnHQ-NAn4z8j5JkLU65n55KaTm7u0Nfewm5lH175C1b4KuKUDNW1xopPYin6xN21jSb1LEkcNTZF4JNA936ZTUW-bIGGw1erX3xpopXkjhI5WXxHPAwXcKg05O3tf2h-2_UDGBVwbt0aC-4ybe7yMiR3R78304IxJCVBTkuobrgjX-cCFSLt6tmJxMT-0Bu--p-89w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 15:01:28</div>
<hr>

<div class="tg-post" id="msg-7807">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpqnl3eFq39-KMt5ILkCJCWx30y-u2TDU90BSCfZq3-ZjS_Ln0yvrGrRRhswz8hh0cxuD63zXhEZeEb12SHaYws9B8d3PzVTobL6IQbPRuzyXZSKBsBFBvyGpZU_JtmW5iqTCzs4B3qeZH-KNQOF1aefs1EeTumRmZ30xzQ7Zlr-toPZEfZAnWlkCuwm24BNcot8KKJrRjPbYOFaChK7whK_ZBqA5jaGT8wd3MKChu8pfk_5FphfpD_aCUfZ2ajmzbIUlvYnZJy9j-ECGItXkRW3IbkPsSFb7idjTYuuXufJhokNOs4-R1xwH7Ir-zfzWtxOB6j51JSdYHDXjFaJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Jev رو رایگان کردن
🤣
console.typesafe.ai
120 میلیون توکن رایگان میده تا هس برین بگیرین، درباره کاربردش بعدا صحبت میکنیم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 582 · <a href="https://t.me/ArchiveTell/7807" target="_blank">📅 13:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7806">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wc4WyY0oonPP8noUzBCrxk9tcDtPV3_nKGj9iNdwDINqjMpfC7XdgM_jksj3nqQEzCihxUngG1Pd7k42fE4xwOBZRqYh5y6DjL_Y-7RQRu_DnqnO06isBFqrEDp8nMKbeAA1ITqEnHXgm3bNINUd7VialcKmPgYW-OVtEMJqu7-MNQx3VK0iWfs5FtxgC37ccoZknNSqId5wgwq0Jkcw6m67RLhXAktZlxrJRhSrZzpIdVMcaG5KCsj3-9zbD6hiqaJvsz4xNeFFLwBFbO7GUHrCXa0iEZLpcKBvlEV5QpTsxpVW8EgmYdsxquOO3SZwmmrAsbPzMA-FVb9ZLywQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود iso ویندوز و آفیس + فعالسازی رسمی رایگان!
همش در وبسایت زیر:
✅
https://massgrave.dev/
سایت قدیمی و معروفیه، سافت ۹۸ و اینا همشون از اینجا اسکی میرن
😱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7806" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7805">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miGEcm0ODBASYiMTElyIT54m5zB9sc1RMCHwhbDlag0JTllqheeoaFg_4vIsS1AnZegJze7y5R924AKftmKgink1M7_pwatFg5LKSwDXRqwAyr28cE_wHXm736rq3TLXHhDNfDwgCRQ1Jeoo6QTi3vr_54elhBlXq8L3Y3rvE5evWJewjYMdEL1Dpx4BUTdN7CaYqxB2vpYysI-TiOqJ3Zxzj_UpACVydc3LBkZ-tEWu2IMXKxMXc2HWXTGev6Ue7ZMg6er4bVl0LBvJd_cDkkJnQDoIPTZbvhCy_xWk3lz3MxLsRMyYkobwwoRyhkVzFf16EP9I_CzS1z_t6u8kAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Cloudflare Quick Tunnel
☁️
یک قابلیت کاربردی از
Cloudflare
برای ایجاد یک تونل موقت بین سرویس لوکال و اینترنت، بدون نیاز به باز کردن پورت یا تنظیم
DNS
✅
با استفاده از
cloudflared
می‌تونی سرویس لوکالت رو با یک آدرس
trycloudflare
در اینترنت در دسترس قرار بدی
🌐
🔺
بدون نیاز به دامنه
🔺
بدون Port Forwarding
🔺
مناسب برای تست API، Webhook و سرویس‌های لوکال
🔺
راه‌اندازی سریع و ساده
📌
این قابلیت بیشتر برای تست و توسعه طراحی شده و برای سرویس‌های دائمی مناسب نیست
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7805" target="_blank">📅 21:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_Qx1MkLgo3p0gmO4gn0dccruuH_gaZdB0fm1sP_zOCj0krNce_YXr6XGLDybgWeI8z1iaWcSFRopT8i1EWcXA8G5Whd9RLaKPOxAeDLzy8kTfpy2CPOWR_MOYtzwzIP7tbpET2kTrg6wkynWkPbED-yiJ7ExNksEwEb22ILigdWSaCdpV-eZnaKVwYqsY9Srh5l2Vkr58Ob0e-dy6rAyElPaXnHqGExxEsoxeih5_Dh2e3u2vR-6-Y6f2yjZ_OYeAbAfYONQdwh6q-J4lCspH35MBaPBF2BV4aN3MijWfcE1DsxWGl4lfN9B5mt1HodezjSj9OvjHgSPYn9nSohUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج طلایی API هوش مصنوعی | قسمت اول
🤖
سایت‌هایی که برای ثبت‌نام اعتبار هدیه می‌دن!
بچه‌ها یه لیست پر و پیمون از سرویس‌های ارائه‌دهنده API آماده کردم که بهتون اعتبار تستی می‌دن؛ خوراک استفاده توی کلاینت‌های مختلف برای دسترسی بی‌دردسر به مدل‌های پولی!
🔥
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
سایت Modeloc
👑
└ خفن‌ترین گزینه لیست؛ همون اول
۱۰ دلار
اعتبار تستی می‌ده!
2️⃣
سایت AAAwinn
└
۱ دلار
اعتبار هدیه ثبت‌نام
🤒
اکانت گیت‌هابتون باید بالای ۹۰ روز عمر داشته باشه.
3️⃣
سایت Jucodex
└
۱ دلار
اعتبار هدیه ثبت‌نام
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
👀
قسمت دوم به‌زودی...
سایت‌هایی که مدل‌های
کاملاً رایگان
دارن و
هر روز
بهتون اعتبار می‌دن
🔜
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7803" target="_blank">📅 13:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔥
دانلود فایل های پولی، کاملا رایگان
- بخش دوم
خوب سری قبل گفتم تورنت چطوری کنیم لینکاشم گذاشتم، حالا یکی میگه من حال نمیکنم تورنت کنم چی کنم؟
یه سایتایی هستن که سرور های قوی دارن مخصوص تورنت، شما لینک تورنت رو میدی به اونا، اونا خودشون  فایل رو دان میکنن، بهت لینک مستقیم میدن!! و شما به راحتی با لینک مستقیم دانلود میکنین!
سایت سیدر یکی از از این سایت هاس برید توش ثبت نام کنین:
✅
www.seedr.cc
✅
با این لینک برید ۲.۵ گیگ بهتون فضا میده، ولی برین تو بخش Get space میتونین تا ۷ گیگ افزایشش بدین با انجام کار هایی که میگه
🏃‍♂️
خب حالا من لینک تورنت رو پیست میکنم تو این وبسایت و فایل ها رو بم نمایش میده، روش میزنم copy link و لینکش رو کپی میکنم، و میام تو تلگرام وارد هر ربات url to file بشین جوابه مثل ربات زیر:
@uploadbot
لینک رو بش میدم! و به همین راحتی فایل تورنت اومد تلگرام.
برای تست فیلم سریع و خشن رو از تورنت میارم تل که ببینین تو کامنتا شمام تورنتاتونو بفرستین
❤️
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6H7H3Zf6WR559kQQadALaQNYRzx_LtEdZQg9K7nkugZozEFK-3cGcG7DVnHfrhVdIxPvWbV6f8H9JiktgByEGIW1Pen5CfepM9CIXSqGEkKRxTajRq6kRDcGaqiTrHE0slzXNQrudmGlFRoqTEl-u8H5lXFg9_ANaId9bv3V0ZqN4GZHP22xRyltsQ62OgVQm2rOee3PrUDIGWDK9xrfkV2xZwQgoRedQ68VefVhy0-8HzQ-FYZfYQXkiKZlHbhID48FLAMh4TPnzsgbmtJHBu2flfHXVI8_I3Aa62BElvfjZT-MG-aSv2E2pp1qapxYTFWWWSpQgZ_bWYNiAnmGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دانلود هر فایل پولی، کاملاً رایگان!
🔥
اصلن به این فک کردین چنلا و سایتای ایرانی(فیلیمو، فارسروید، سافت ۹۸و ...) اینهمه فیلم خارجی و برنامه های کرک شده و کتاب و اینها رو از کجا پیدا میکنن؟
بعله منبع ۹۰ درصد این فایل ها چیزی هس که قراره بگم و کاملا رایگانه!
از جدیدترین فیلم‌های روی پرده با کیفیت اصلی و دوره‌های آموزشی چند صد دلاری کورسرا گرفته، تا برنامه‌های کرک‌شده ویندوز، اندروید و هر محتوای پریمیوم، نایاب و بدون سانسوری که فکرش رو بکنی
🔞
💎
( آره حتی اونام اینجا کاملش هس
🤣
🙈
)
اصلاً داستان از چه قراره؟
اینترنت یه شبکه بی‌نظیر داره به اسم
تورنت (Torrent)
. اینجا خبری از سرورهای مرکزی و محدودیت نیست! همه کاربران دنیا سیستم‌هاشون رو به هم وصل کردن. وقتی تو فایلی رو دانلود می‌کنی، در واقع داری تکه‌های اون رو از هزاران سیستم دیگه در سراسر جهان می‌گیری و همزمان بخش‌های دانلود شده رو به بقیه هم میدی. نتیجه؟ سرعت بالا، بدون قطعی و کاملاً آزاد و غیر قابل فیلتر شدن
🌎
🔗
🛠
قدم اول:
نصب کلاینت
برای وصل شدن به این شبکه، به یک برنامه نیاز داری که کار جمع کردن فایل‌ها رو برات انجام بده. کار باهاش به شدت سادس؛ لینک رو بهش میدی، خودش بقیه کارها رو میکنه.
📱
دانلود نسخه اندروید
💻
دانلود نسخه ویندوز
🌐
قدم دوم: لینکای دانلودش کجاس؟
لینکا اینجاس
🤣
آقا یکی میگف من با تورنت حال نمیکنم. میشه مستقیم تو تلگرام دانلودش کرد؟ بعله اینم تو پست بعدی میگم. نحوه انتقال فایل تورنت به تلگرام
😜
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7801" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🤖
JIJI AI
مدل‌های موجود:
⚡️
GPT-6-astra
⚡️
GPT-5.6-sol
🧠
Claude Fable 5
✨
gemini-3.8-flash
🚀
glm-5.3
🔥
deepseek-v4-pro
روش دریافت API :
1️⃣
وارد سایت بشید و با گوگل لاگین کنید
2️⃣
وارد بخش API بشید و کلید جدید بسازید
3️⃣
شناسه (ID) مدل‌ها داخل پنل سایت مشخص شده
Base URL :
برای GPT:
https://api-slb.jiji.cc/v1
برای سایر مدل‌ها:
https://www.jiji.cc
🔗
www.jiji.cc
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7800" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTmSlJojVovhat1SAFJ9VU0HiVCL1MX71rUIk2Ovisbh2DhNZ_l-w0RriskNjvuLh6L-mr8x0tUDEnyYO1n6_ZKnAf5l9o8rbPr0vl39LFupIF4lBNEw5Y00vJE0ENm4sY8fDW2LlAQnEOYyKM5KdwymX7pXG2Bt7NjstnDZOQB82Zp-Jg8rOBvnZQA0uKeFH7YW4COHOp2BWqktOBdgF-B1hTRcHBiOHz3os8eTOMCsBY6QauS_ULYGfn3GXrAIzsE4jrWKBbkqKSgFZT13cS6gLoirN_2m1mH8fM_jDqLH1XNkVAUHoil58nvQpyivBwhbKf-gBtOStiNa94I60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIb2ZdkobavbpHjECfpExuky9b4a_EIEw_vHGGXL1YppuGrfc_qEB5tVVk5OacGbOv6iDWESvPzNVM-0XJ0InoQ8ScNcf--QjLhBoUs4mqmhdyZxpsq5gSrogPqbCxlDhsSSlVfwk6AlVaCy3_QBvtBChm1IIPgFGQYVmdmvDLc39Wr97Z_wrysXmFDtwSjCuT-omjkCJ9wZ6rxjklYuIPN_L87ymJOxD-sUTgT1UrR2i5Icz-rdeVj34nuVFmFy87J1rlc6FXb1B7ZutbZmZTKOGI9_b-SeImY9XIza429QNpsvr3JliXsERh1Wy8UmTghHKRmek_oWONOq6zAmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcsoYAWVhNbkjhapusaZiVQEIuZTQcDKzT6eA1KZcPbzAAOQebGOfI6E8QDukpeHPWFiKTkIqae7efUVbIQtzqXj55rrclB8zTyXrt7lW2m94pPhuKSO4_1m1HtBdG6S_Puwp27RF8ZqXVVfTQbklPHh9WbBnPjFsPJBo_ukUU_YmNeGlhyeO1HYpD5_U2nHc3yM0CZkm-HMsLXMtKJauCgR41ENLndwqr9oL225E0YMUCubvYBo6RLmjU7Tgjp0fd1YgVQDYOPDz5vSfweLlcrID1CqoM1eMCwNZc8rnb2-EH8aQPLX78M9IhjUye5hRYJhTwv--Y5Idy3ovFWfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل GPT-6 ASTRA به صورت رایگان در MiniApps در دسترس است!
قدرتمندترین مدل شرکت OpenAI، بدون هیچ هزینه‌ای.
آنچه دریافت خواهید کرد:
✦ مدل GPT-6 Astra به صورت رایگان
✦ قابلیت‌های استدلال، کدنویسی و انجام وظایف پیچیده
✦ اجرا در مرورگر، بدون نیاز به نصب
نحوه شروع:
1. این
لینک
را باز کنید.
2. ثبت‌نام کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7796" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhKCeCcYLAtQm0lQ49bgKTVLo24c4hZZ3MPrN7dM4LqRtcqZ-Clalskx2iQN9lGpo1ZuC12TgUIHJfoictulikHBE_MiQRFkZTwgm-jttbYEf41JfmzwFb5iWSL_8_SMxKGWaXl7nncxHh_VN6ff_dGM3dVyuQbewhkhLxn0A0JYtSedMy7rsI-ssQxYw0eDN88WGDtHibkB5gpVCzhcWRgivTmAeeI_RT87lIr6P6w48vb2l71A3wGw7si8j-KtPCs2fKoCrgi0ly5q1okCYClQeKuHsMXzsAUvdaT5m7p7hn9xfbEjc8Onpmq1XmgzRn10YPH9_Z5Ri3cC_S7vCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
مقایسه‌ی تصویری GPT-6 Astra Max در برابر Claude Fable 5.1 Max در تست کدنویسی Code Arena
به طور خلاصه: Astra در انجام وظایف تحلیلی، محصولی و محتوایی عملکرد بهتری دارد. Fable 5.1 در جنبه‌های بصری و تعاملی عملکرد خوبی دارد.
در حال حاضر، GPT-6 Astra Max در مجموع، رتبه اول را دارد. می‌توانید جدول رتبه‌بندی کامل را از طریق
این لینک
مشاهده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7795" target="_blank">📅 16:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCBaIXvjzkxiDA8hIbc5Mlk_4JPDRaUVQ29EkZStcGlL79dIrtcOyvIUVNzMb9089ghKmIbjrnLD7aHZ71Z6asaAWh4GB79NcFGkP-0fywJF0myr7jsIpYtPnOnQfkqiLizEEoQiRb61l5MvcrpfDlcJBcSYUfgTM5mvAJXWfKxTUP-KAwUkMbE6ctaKtZTjbl9mufRWlQdYzV9zTolVTI22S9wZPG1L2FDOYG6D7lazOtgoYZRY7FVudkQ3HNgEuo1Mcgp1X33_Gc_pjn4aHSdzgIAHowvCZ-INXTA2mg3HeWaBWTUR8OQzKwW21IiA7HIyx15YiJiTqyvnBk7mTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
؛Qwen3.8-Flash رایگان تا 30 سپتامبر با 0.0× اعتبار
مراحل:
یک حساب کاربری شخصی در
Qoder
ایجاد کنید یا وارد حساب خود شوید.
یک محصول واجد شرایط از Qoder را باز کنید و Qwen3.8-Flash را به عنوان مدل انتخاب کنید. برای اطلاع از قوانین این طرح، به
صفحه رسمی تبلیغاتی
مراجعه کنید.
از Qwen3.8-Flash استفاده کنید. نرخ 0.0× به طور خودکار در طول این طرح اعمال می‌شود، بنابراین استفاده از آن هیچ اعتباری مصرف نمی‌کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7794" target="_blank">📅 15:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icpCAz8d14eSxqKBPJGp-hxcQsVlhVyTWf-Fs7w43RamZBjYyGsmcUw3CxeXBcLgLXWjlol6K4Z9WgkQm777P6Sizw5_0rOfPEdPOguUajL4h5xU9oftaDAK2J48pg96yLjix0ZTDyD201G6OUHRE4VgNGfATCbUbFM0EJL1kDj0ZBzOC5innNCD_D40N-K-L-i0KhJCb7ZFPuHcTY7U3Ul1tLM62KIc9xVk5-uP9MCaR2mzU8v4HkZJ03f5juvia8FidJcIieM-4-PVVZqEsD2deA9-AOWgy2pn5eE8k1oUkyaz76NT2JYMKU3jAo5NCCXzC69jpfAHa18xAUZhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
چت + تولید تصاویر و ویدیو با Kleo
🔥
آموزش
مدل‌ها:
➡️
GPT-6-Astra
➡️
GPT-Image-2.5
➡️
Kling 3.0 Pro
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7793" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=cBuQLt5s7CMK0g5ikx48Ca4jX9LrxKwUn3ieZPymBLqO_F9DutWvYgCnTsvHJA6suzborzYYg-69LZyfJ3JsWcMsEab9WU1k4ZBXDjNsCfZql0PGoWE4TkCW6_1J_Hdl9GjwrHD2m_tPkIY4johIcjzI8tNAeRC9WtT_NMvWEitoUEMagLdYk71oKSA2h3yvJEBz3tvIMljNbEvKaUBPJk8Cc6psxUzbXhetsqrYBSJvu2E_E4fvwqJoptHyeMH2c8UDphTJg93nM2ywlwAaki9949bwSRs2GqMibReCKRpg6yyXO4ifMNrZaY9Hh-Jgju7ZTBcgxUjoI6pEHrJHbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=cBuQLt5s7CMK0g5ikx48Ca4jX9LrxKwUn3ieZPymBLqO_F9DutWvYgCnTsvHJA6suzborzYYg-69LZyfJ3JsWcMsEab9WU1k4ZBXDjNsCfZql0PGoWE4TkCW6_1J_Hdl9GjwrHD2m_tPkIY4johIcjzI8tNAeRC9WtT_NMvWEitoUEMagLdYk71oKSA2h3yvJEBz3tvIMljNbEvKaUBPJk8Cc6psxUzbXhetsqrYBSJvu2E_E4fvwqJoptHyeMH2c8UDphTJg93nM2ywlwAaki9949bwSRs2GqMibReCKRpg6yyXO4ifMNrZaY9Hh-Jgju7ZTBcgxUjoI6pEHrJHbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
مدل Kimi K3 به صورت رایگان در Cline Desktop در دسترس است!
🤔
شرکت Cline به تازگی مدل Kimi K3 را به خط تولید مدل‌های رایگان خود اضافه کرده است.
🤔
دسترسی رایگان برای مدت محدود.
🤔
از مدل Kimi K3 مستقیماً در داخل Cline Desktop استفاده کنید.
🤔
مناسب برای برنامه‌نویسی و گردش کار هوش مصنوعی.
✨
؛Cline Desktop همچنین از سایر مدل‌های رایگان نیز پشتیبانی می‌کند.
⌨️
برای شروع
اینجا
کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7792" target="_blank">📅 13:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/ln4PxbIQ-Fiv5T7Krdd68OOQRua2QEoVY4O66JJtvIV9Qdi6GXkS008HlAS8VJp-YQzjhix__3N2CnLIhvIrmn-29v8bO46RpOF8bS5kNS2O0IRxLuu-XE4IfrQD4KBFR9IyKj_z5sU8zrd6gGqfK2LPlYQ5yj6MbfQ7o69h8AiRbXxPzQbohiII5xoiMtisND5_w2GJ8R0218NZ1kxci6qk2jhAh92uk0kpw2X2QS3o3PM_PrhTk__3E-xV5_LHHQ_3Awwb1kQFiOmXHIJ33h-YMznX7TFpaJecyFtycKjPIbgeoNI-RlJqeL81NzSv2xHSpEXXBC1eJ4jRRY73bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giOouoVj9STOybVbu7vitnNP_rgqwRbNL2apVrDCxGa7Z-h9E0gERi6MeBbKb_CJozTju2hhk1XQTeeEBfmxkSgImSkAi7uUNIa5KM49j9fBdSnxzxjagXtx_-Crwb5N52ZgwQSN4iAQVKT618hFXez-yWFvxoQAnTAZkM1yP1s4gPNg61rVRYgO8IqVXkhJzUuAEng_6kXWh7zYDstRPcTPG0YZIDr2-m1X61x9qKHwpsLJTQncTlFL5cMB5zTjeEoVNP18jgWkToYjbqarMOXJjF02Ert1mfLU3W77uX0MSuYqmKObdvX5JKsxN-sskTEl7XLXxRPjvpOhKugQPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">seekAI
$2,000 credits
API key:
sk-Ok0xV7Zp4vfigk6qXL8M6hQSeVGa5cRhhfkZ06yre2RUIAfN
base url:
https://seekai.cc/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7789" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJAvkse1kzdv8VnMDvPHIEOLKk2UQxdQ9iZxa0XFq5EQhnEnvALcVtN3fhGAv7ZxsOIV2dGewK3faHCMynC1j78KnKPR6A63wSlK0n_pAlMIQrXXxBCHMI8eNGKMGoviv7eCq6FSzBkNBOOTM0gOYj54wr-SR8Z3TcLoIy__HCqk4uCEWm6SeWSHW2twt27Vlz_eEv93lnN6unn7eRpl6npy5biwCSb4FjL3TJPvdkI7BdVDAqJlk5qBFNL6QvLSI1KTSigjEi7SmwobrL3goBnnPu4AqTpoTZk1r6up90K5iAYfD68k8NI0DzX-o5moLjYlmzfl0n6NQagEgOfEFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Fable 5.1 به صورت رایگان در Freebuff CLI در حال حاضر در دسترس است.
👾
📢
؛Freebuff یک ابزار کدنویسی کاملاً رایگان است که در ترمینال شما اجرا می‌شود (مانند Claude Code / Cursor، اما با قیمت 0 دلار)
🆓
✍️
مدل‌های رایگان دیگر موجود:
🔍
🤔
GLM 5.3 Flash (پیش‌فرض، بدون محدودیت)
🤔
DeepSeek V4.1 Flash
🤔
MiMo 2.5
🤔
GPT-5.6 Luna
🤔
Solar Pro 4 (به مدت محدود)
🤔
Muse Spark 1.2
📌
نحوه شروع:
🤔
ترمینال خود را باز کنید.
🤔
؛Freebuff را نصب کنید:
npm i -g freebuff
🤔
به پوشه پروژه خود بروید:
cd your-project
🤔
دستور زیر را اجرا کنید:
freebuff
🤔
از لیست مدل‌ها، Claude Fable 5.1 را انتخاب کنید.
⚠️
نسخه آزمایشی محدود — فقط 500 جلسه در مجموع (1 جلسه برای هر کاربر)
🚀
از این فرصت استفاده کنید تا زمانی که باقی است!
⭐️
🔗
اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7788" target="_blank">📅 11:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اگه موقع ورود به gemini یا سایر سایت های تحریم به ارور ۴۰۳ برخورد میکنید، میتونید از dns های زیر برای دور زدن تحریم استفاده کنید
👇
dns 1
111.88.96.50
dns2
111.88.96.51
dns1
45.155.204.190
dns2
37.230.192.51
dns1
83.220.169.155</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7787" target="_blank">📅 11:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♊️
جمینای گوگل سه شرکت واقعی را هک کرد !!!
جمینای در جریان تست امنیتی ماه مه ۲۰۲۶ به‌ صورت ناخواسته به اینترنت دسترسی پیدا می‌کند و شرکت خیالی مورد نظر خود را با شرکت‌های واقعی هم‌ نام اشتباه گرفته و با استفاده از اطلاعات ورود لو‌ رفته در سراسر اینترنت وارد سیستم‌ آن‌ها شده و نفوذ می‌کند،  پس از پی بردن به واقعی بودن شرکت‌ها، خود به خود عملیات نفوذ را متوقف می‌کند.
گوگل اعلام کرده هیچ آسیبی به این شرکت‌ها وارد نشده است
✅
منبع
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7786" target="_blank">📅 09:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7785">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سلام بِرارون و خوارون عزیز
حال دلتون خووِه؟
🌟
فردا یه آموزش خفن داریم که حسابی به کارتون میاد!
🚀
مو فردا مِخام یَگ آموزش مَشتی راجب «تورنت» براتون بزارم که کِف کِنِن ینی قشنگ بِتُم مِگُم چطوری انواع و اقسام فایل‌هارِ، هم اوریجینال و هم مُفتِ مُجانی گیر بیارِن و حالِشِ ببرِن.
😎
🔥
بِراگَم، گیانِ دل! از بهترین کیفیت فیلم‌های خارجی بگیر تا همون فیلمای پرده‌ای که تازه لو رفته... اصلاً هرچی برنامه کرکی، موزیک، فیلم و کتاب نیاز داری رو یادت میدم چطوری سه‌سوته رو هوا بزنی!
🎬
🎵
📚
پس فردا حواستون به کانال باشه یاشاسین بچه‌های گل خودمون قشنگ هر فایلی که ایستیسَن رو بدون یه قرون پول دادن یادتون میدم دانلود کنین. منتظر باشین که قراره بدجوری بترکونیم، ساغ‌اولون!
💣</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7785" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7784">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚀
Ashna AI
قابلیت چت مستقیم و یا کلید API
🤖
مدل‌های موجود:
⚡️
gpt-6-astra
🧠
fable-5.1
✨
مدل‌های متنوع دیگه
روش فعال‌سازی:
1️⃣
وارد سایت بشید و ثبت‌نام کنید
2️⃣
اطلاعات حساب رو تکمیل کنید
3️⃣
از بخش Integrate وارد API Keys بشید
4️⃣
روی Create key بزنید
5️⃣
گزینه Dynamic model routing رو روی Off قرار بدید
( نیاز به تایید شماره نیست ولی اگر خواست از این
سایت
دریافت کنید )
base url :
https://api.ashna.ai/v1/api
🔗
app.ashna.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7784" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfpNqp1eDuFUQDgVwSQ6IpIwZHzB19I0sR6OUGLVkTgHMnSOR1VO-Sb7eJ4xRs3EeNMwWvLweVOtjhQEKDk7lmwdBVgqsgapF5Bs96KEE9PV32i3YRBtHkzf_m88R2hw1z4vjU76wJ7-jlsPV25NAuwll3FVJ3ZGe_AFBjMyCojuBSE5W8kA-eyM9Ig21rzfijbgK3UjgQwCjZPrk0tS9hetnDAkI1Q9AOSgtA4EiNsfgLb-0aTcwvDUPhNG4X8BJNH3P3cPcYpanWVKce4SHsgqUUZ_WsqnEAlpfi-_wxGIbrrKg_dx9qOAWlffwaQOeJ9c0gA0tAug1JMeWkayjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gemini 4 pro is out now
💪
😎
گوگل بالاخره پر قدرت به بازی برگشت
تست کنین نظرتونو تو کامنتا بگین
(این پست طنز میباشد)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7782" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUY6DvsIX0MOQS-n9cTxMEK_6CCNFlUd0ITJI5nGf7ozluAPREq6ArK7l1sO46_cId2no1STyki7DCzMGt1oYfcBb1jgmos_RCrHTLzPRIpGb4PTNoLLAEptvmgPGPaqrVwhAgI_Y4n7qU95EUzbSsIW1s_nwMzpoaP-BWA0uGGSEnwtciycYvRnYXZGIxQ6ersqBt4tIQ_pCDnTjOe7Lm_W15hohPlEuj9VoYN3Vau9Ce4Hv8tgKSi1CTOR7ec1v9lJhYgz4Mp-Z19WsHkmsNAAdCVb1EE0gXtdxTvo_lg3xIrezML09YOu7gLqEAgLXo1qTUt5D_TpwFEPgMYMug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تبدیل ایجنت‌های هوش مصنوعی به کارشناس امنیت با ابزار Cloudflare!
بچه‌ها کلودفلر یه اسکیل امنیتی خفن
منتشر کرده که در واقع بیس اصلی سیستم کشف باگ و آسیب‌پذیری خودشونه و هوش مصنوعی رو به یه هکر کلاه‌سفید تبدیل می‌کنه.
✨
ویژگی‌های کلیدی:
🔺
ا
دیت ۶ مرحله‌ای:
ایجنت رو گام‌به‌گام از اسکن و تحلیل کد تا شناسایی عمیق آسیب‌پذیری‌ها جلو می‌بره.
🔺
گزارش‌دهی کامل:
در نهایت یه گزارش تحلیلی، تمیز و ساختاریافته از تمام باگ‌ها تحویلتون میده.
🔺
راه‌اندازی ساده:
کل ساختار در قالب یه پوشه از پرامپت‌ها و دستورالعمل‌هاست که راحت روی ایجنتتون سوار میشه.
💡
نکته/استفاده:
خوراک دولوپرها و تیم‌های DevSecOps که می‌خوان قبل از ریلیز، کدها رو با ایجنت‌های متنی ممیزی امنیتی کنن.
🔗
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7781" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">💎
دسترسی به مقالات و کتاب های
پولی خارجی به صورت کاملا غیر قانونی
https://libgen.im/
https://z-lib.id/
https://annas-archive.org/
https://sci-hub.se/
https://libgen.is/
دوتا اولی فوق العادن
😱
، علاوه بر مقاله، کتاب های پولی رو همشو داره. هر کتابی بخاین.
کاملا غیر قانونی
😂
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7780" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ارسالی
http://64.23.188.133/v1
gpt-6-astra          ←
⭐️
تأیید هویت شده
gpt-5.6-sol
gpt-5.6-terra        ← سریع (۵.۳s) و باکیفیت
gpt-5.6-luna
gpt-5.5
codex-auto-review
gpt-image-1.5
gpt-image-2
API key خالی
سریع بزنین تا تموم نشده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7779" target="_blank">📅 17:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9rF-GRZ-jHGAXSEHycRXGmnX7qzi9-hRUwO9GJjrwdDWhCDQk9qXua_2sX7N6D3F6WefGWce5vid3CAb28cOdG4T-mG17Dd5i6Bn-5Pow_xzyHAK6f_ChmRaa-dI3q5mPO_Edp2CoWEtuH-b6QZeb8t4Hc64_dCrtpbPRT2wh7acUeFRfbhQMlYrFJY8NuyaITk95M3IwvfaPSemU6_Pn7Lqri0N1Df14xb5ROSfFlM_k89phhGYbPaSHmsgGNGYS8CgmLDGxbc9dSm8ToMIz1JnNrxULKdylLzhsbhbjCaFzWp-N_315S3RFRhVTDcoYmxAbJ9iLcvtQLBRa007A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جنریت رایگان تصویر با مدل جدید GPT 2.5 SUNBURST!
بچه‌ها پلتفرم Weavy داره کردیت روزانه میده و می‌تونید جدیدترین مدل‌های تصویرساز مثل GPT 2.5 و حتی ابزارهای تاپی مثل Topaz و Magnific رو رایگان تست کنید.
✨
ویژگی‌های کلیدی:
🔺
کردیت رایگان روزانه:
فقط با اولین لاگین ۱۵۰ کردیت هدیه میده.
🔺
مصرف اقتصادی:
هر جنریت با GPT 2 فقط ۱ کردیت و با کیفیت بالای GPT 2.5 فقط ۳ کردیت کم می‌کنه.
🔺
محیط نود‌بیس:
دستتون برای تنظیمات دقیق پرامپت، رفرنس و تغییر کیفیت کاملاً بازه.
🔺
ابزارهای پیشرفته:
به ابزارهای محبوبی مثل Magnific و Topaz هم داخل محیط کار دسترسی دارید.
💡
نکته:
وارد سایت بشید، یک نود از مسیر image models -> edit image -> gpt 2.5 اضافه کنید، پرامپت یا عکس رفرنس رو بهش وصل کنید و ران بگیرید!
🔗
لینک ورود به پلتفرم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7778" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jx4-INJHr1oisYVh4wWZIcnlgW0wTFAoU5s3XN_MYXj2r4qu3G9cerfUWiEVH5xPUQsmg6slswN83ynt5hGA-F8tlYozdnGoRL8jtC48P7m0EYLHGdeFohLkRtIGRf1RYOyD4drruT1sCz-WbZkkOzH4dcLSyDdAT4cvxk0ltiCOAU--NFS0sKjtNeBk2y8Zmr3s1JpHC1QeHITqCnzPGW4hmYr4U55IYtAOPMVZaLsAULB0iSe8Wc1vj5x0UoeuNB9_u_Y_bb0IzZCnbQ6M_iPDAZk0tutUunx8bygvi-mTcTzrWNvMXkGMFpDKl01B1R5RhHhyx8lSysG6hUhMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
یک میلیون توکن رایگان GLM 5.3 Flash
برای دریافت
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7777" target="_blank">📅 17:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pvKdZlUIdiirKmBeLkWBqpDGWOuoyCyOoL5zi7a9Xk-zHRSxthgtGqPk8HIk1y6doYykg7gxTZiCWo8k3Eo6fDqz8ktwDpBN8x6HknX7xNguRxg-31if1MsoX0Z1acpA53JTc3Q2erAPS2_r6k8dxMYaHVYMytlcybSc03fvxW7YKjaxgLLIYOTEl8bJmenrTZmQhex2p0mRibEW6epEeCzMCMPEExYyeeGIHlVVomBVPN0i8e9pUGzI2L22neOiyt1TpqtWAnKO0Y5dcEGlN0XRwWSP_fiZVe9X8HPKm0oJUcZg-YwN3ZQobndxV2L1pt986T3SqPx4U9Ue6Iz3eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
6 مدل هوش مصنوعی رایگان که همین حالا در Cavoti در دسترس هستند
👾
📣
دسترسی رایگان محدود (تا 25 سپتامبر)
🤔
Hy3
🤔
MiMo-V2.5
🤔
DeepSeek-V4-Flash-0731
🤔
Qwen3.8-Flash
🤔
GLM-5.3-Flash
🤔
MiniMax-M3
✍️
آنچه دریافت خواهید کرد:
🔍
🤔
استفاده کاملاً رایگان
🤔
؛API سازگار با OpenAI
🤔
مدل‌های قوی برای کدنویسی و کاربردهای عمومی
🤔
نیازی به کارت اعتباری نیست
📌
نحوه استفاده از این پیشنهاد:
🤔
به این
لینک
مراجعه کنید.
🤔
ثبت نام/ورود به حساب کاربری خود را انجام دهید
🤔
کلید API خود را ایجاد کنید
🔑
🤔
هر یک از مدل‌های رایگان فوق را انتخاب کنید
🚀
⚠️
دوره رایگان در تاریخ 25 سپتامبر به پایان می‌رسد.
⌛
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7776" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWQOG4VzUHDonPezQPo2igIu-HMExkikRaFuFt8zPBfcbTjpTVoQ3By0GimkwCEShGQZqRyHlbEtuT8s1NeztWwQjrjhebjfVWjk2b8Z514xHEQpqoT2hoE-PGIu25SqbHrGj7gqTDQPPhn52OyFfAYndG4eS2FzdS-6wA2m6EEInfWk0MRsvB-bBS9-P5dQ10J966ylYsrp8ZKV2IY-tXiLKerhV79YXmDKkiX8PN1mfKADBvRkD_fVMsuk9zVPfNLNbJ4ODRsdp62JXk2dYQu0-to6eCw7vhIYC1BcKWRhQLDdNgnR6rxMQHqE93GOzljz0ER60ZszC21EAvf7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تبدیل خودکار هر مقاله به ویدیوی کامل یوتیوب!
بچه‌ها این اسکیل جدید کلود رسماً برگ‌ریزونه؛ با
Anything2Explainer
کافیه یک متن، مقاله یا موضوع بهش بدید تا تحویلتون یک فایل آماده MP4 با موشن و صدا بده.
✨
ویژگی‌های کلیدی:
🔺
فول اتوماتیک:
سناریو می‌نویسه، استوری‌بورد می‌کشه، انیمیشن می‌سازه و زیرنویس اضافه می‌کنه.
🔺
صداگذاری اختصاصی:
روی ویدیو با هوش مصنوعی نریشن و وویس باکیفیت میندازه.
🔺
کاملاً رایگان و متن‌باز:
با یک خط کامند راه می‌افته و خروجی تمیز بدون واترمارک میده.
💡
نکته/استفاده:
آماده‌سازی کل ویدیو با تمام جزییات حدود ۱ ساعت زمان می‌بره و همه پروسه صفر تا صد توسط AI هندل میشه.
🔗
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7775" target="_blank">📅 13:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6370f25b3.mp4?token=B4_kW9xusyrEa-dn6HWy-BcG5caJGcbX47SRbbaL8ImAZI8M13S5q_8hKNCNIWvPbv3_AOO7N5tLkgJHJ7XZgvxhaR_xl9Wa1Xw9n7aLX2bqQ3G0Re_RUXhhI6s9UBYBwHkci7jl30PHiTaA2EiaaTGuagQx-vxfFJNoT8nEgx_HZAhf-JYf4T4h6YsHHGRiON24cX8VKJ0uvt2HqKXaMmlndpJKl0NK4n-FJCmwPb3e85z6HvmtGpwc3RPISPVVkalb1-fN6cg5ClDQ14wJSYmoDb6kIdy4q2LtegXLw97EXIU606uEMnnXwcV0IOfBz_xEqkZdPrUL3xDdfVNixQUTCq6BBH7aKrco9we_LVVLw7ZxqulNFGlbMhBdQDqnqXjtfzl5bdlkcUS8_HDCwSoUCkUMCXyaG54cfxh--5YEKT5jHQOtW2Z4uNagJupxUK0JM-B6X1xQBMPJJxcv8rLbfbKNQoBnM88-HcWhbBf_Ln9OV5Wzn9rgYY7JPIH9baHUGGrfz1RZGkYxEanGD6GZakb93VE-fAP2EqalQyD9MaQ8CRTg2jOTDT2RxAqie51jU5PifhbJ-4_0J9RzLGAgvvRVJMRD5Y2TJg0kugC87y1yNWcR58aNqzltqXWW4kkqyXAuZnJqUU1DDn97h7-Sj6VHwyAkdgVutBOSmVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6370f25b3.mp4?token=B4_kW9xusyrEa-dn6HWy-BcG5caJGcbX47SRbbaL8ImAZI8M13S5q_8hKNCNIWvPbv3_AOO7N5tLkgJHJ7XZgvxhaR_xl9Wa1Xw9n7aLX2bqQ3G0Re_RUXhhI6s9UBYBwHkci7jl30PHiTaA2EiaaTGuagQx-vxfFJNoT8nEgx_HZAhf-JYf4T4h6YsHHGRiON24cX8VKJ0uvt2HqKXaMmlndpJKl0NK4n-FJCmwPb3e85z6HvmtGpwc3RPISPVVkalb1-fN6cg5ClDQ14wJSYmoDb6kIdy4q2LtegXLw97EXIU606uEMnnXwcV0IOfBz_xEqkZdPrUL3xDdfVNixQUTCq6BBH7aKrco9we_LVVLw7ZxqulNFGlbMhBdQDqnqXjtfzl5bdlkcUS8_HDCwSoUCkUMCXyaG54cfxh--5YEKT5jHQOtW2Z4uNagJupxUK0JM-B6X1xQBMPJJxcv8rLbfbKNQoBnM88-HcWhbBf_Ln9OV5Wzn9rgYY7JPIH9baHUGGrfz1RZGkYxEanGD6GZakb93VE-fAP2EqalQyD9MaQ8CRTg2jOTDT2RxAqie51jU5PifhbJ-4_0J9RzLGAgvvRVJMRD5Y2TJg0kugC87y1yNWcR58aNqzltqXWW4kkqyXAuZnJqUU1DDn97h7-Sj6VHwyAkdgVutBOSmVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
با این مدل، هر عکسی رو با یک کلیک تا 4K آپ‌اسکیل کن!
بچه‌ها اگه عکس تار یا بی‌کیفیت دارین که می‌خواین زنده‌ش کنین، مدل خفن
Crystal Upscaler
دقیقاً همون چیزیه که دنبالش بودین.
✨
ویژگی‌های کلیدی:
🔺
خداحافظی با ماتی:
عکس رو مات و غیرطبیعی نمی‌کنه و جزئیات واقعی رو حفظ می‌کنه.
🔺
کیفیت تا 4K:
رزولوشن رو تا بالاترین حد ممکن بالا می‌کشه.
🔺
عملکرد جادویی:
خروجیش رسماً شبیه زوم‌های فوق‌العاده توی فیلم‌های علمی‌تخیلیه!
💡
نکته/استفاده:
نیازی به سیستم قوی نداری؛ می‌تونی مستقیماً روی بستر وب و از طریق FalAI آنلاین تستش کنی.
🔗
لینک تست و استفاده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7774" target="_blank">📅 11:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7769">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kD0zmE90OcV0b0eHJP9-P3_WkFsMhFl7pdx5gz73chrgQydOaMdrK6n2hO67-yPwDcIQz2u54h2meHx6vrVmQuWOkHiqc6A4psNmZc3SipU8j3HpQpviMRiwG9WXdKnBxlsmwFyukGhGWr311ka0b6t7QDzxiTo-iOx8ZqyN5AKgNaeXc3PzU_OseFpFgHdYGpZUuP4hewgnSapsXfG77kPtP5Sl5icqorG4z9bxiQnb1SGapbMEtrDUOtDguq9nKrn8x9FSCsXPOdiVT63chIWO9QLEivW-xFHg1fFbGMz0oKxXA_d4HmQ7iRwbJEOvgTrQsoRCPq5jbQthT-9BWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3RW67KHv8w79tzxeqjXWXvtPTa1cCCDrF2HFwXDNOlmZfMPI6YWlAKeZXsQW7dsBJafAhNND0BZY0-r3rFI8vUz1zqUXgKkaBCbmZqppPxEdAgWYUsrRV3F7IJLJJ6Oqgb3cBYaMkF-yl5E7Hbwi1POZW0dJUOb5-vkUv48TBxlqhl8migT2FHSXmaOx5DjmIhOLvz-kzyIt-yndyHQoJOVClJzZF6PUMGulsXSyOONRIGQ0fCZn5Gj4o1WdAlsa8phtgtH8dVElbm_XtyaupPUtmLfg-E9iGTrnRPL6qvFHiyPFRq10n8O4i17HMCo0NhZD2wU0lv24OrDG_nHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqntB-qaIQ7CqRcTvZqvRX_ilFEdK3FAiqRkr0oFBLD9337Gx_AL4oqVDbQnBt2PAWmUlXhAKEqHFIacT0708iX7nCZ2NA8DSzFXgW2wFr3kpVR5PGhERdtM1NDplS6TN9sXtJo_73YpA1G7Zd41W-ht7D1QGWwvmi3mlt3SLdvyotgQfrs_3Yw-AEDwp4SS_G3ya8Fp_27Y-DBreKfxT829vQObWubUDroe35DQntdokVGO0v8G7oVKciS72b8DmZGADVsC9PhByoATM8N7G61GRmVhspGl6Ds5DfVig7gNfEJ-38A-V4NpFZpDbhMg0deo5KVk2ueH3s59XoTolg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=C5o2qmy18IZW8rj-cy1Dx4aaqWFaGjaX2MZkDs_L2hu84FjdkrJsNZZqOQ2rKZ18PStFpMf5jxjpdFsx8i4VLlZTWWLJoTCx8_eOq2k-KP4Xntqaki38s4izliFLgqL9g1nRNawENwmiltPBokK_Qm6sFLEne-GsYlaV73pgDQl4ZpEyP5lhpvlowMHaCkdVIRhPgDNZJsPaIZ3-y4fsao-8D0eta53TfC7W1-jNtsa5yFcM6hmmpj95xgea4w1jQSTUj__QvmXf_DQU6pBDJTTdEzOGI1sQxj5JrktZmZd8zZW1wx-4Cl65KMl7Yhn4YLBC3v0xzoLGRPE5YqnMeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=C5o2qmy18IZW8rj-cy1Dx4aaqWFaGjaX2MZkDs_L2hu84FjdkrJsNZZqOQ2rKZ18PStFpMf5jxjpdFsx8i4VLlZTWWLJoTCx8_eOq2k-KP4Xntqaki38s4izliFLgqL9g1nRNawENwmiltPBokK_Qm6sFLEne-GsYlaV73pgDQl4ZpEyP5lhpvlowMHaCkdVIRhPgDNZJsPaIZ3-y4fsao-8D0eta53TfC7W1-jNtsa5yFcM6hmmpj95xgea4w1jQSTUj__QvmXf_DQU6pBDJTTdEzOGI1sQxj5JrktZmZd8zZW1wx-4Cl65KMl7Yhn4YLBC3v0xzoLGRPE5YqnMeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
Arrow 2؛ قدرتمندترین مولد تصاویر وکتور!
🎨
‏مدل
Arrow 2
اومده که کار طراحان و تصویرسازها رو خیلی راحت می‌کنه و ساخت وکتور رو به شدت سرعت میده.
‏
🤔
کاربرد متنوع:
ساخت انواع آیکون، لوگو و اتودهای گرافیکی با دقت بالا
🎯
‏
🤔
خروجی حرفه‌ای:
تبدیل پرامپت‌ها به طرح‌های برداری تمیز و قابل ویرایش
📐
‏
🤔
تست رایگان:
دسترسی به دو هفته
trial
برای شروع کار با ابزار
⏳
‏این ابزار خوراک بچه‌های طراح و گیک‌های گرافیکه
🔗
لینک دسترسی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7769" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7768">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یه مدل جدید و قوی برای کدنویسی اومد و فعلاً رایگانه
🔥
‏Union Alpha امروز روی OpenRouter و OpenCode در دسترس قرار گرفت
✨
‏چیزایی که داره:  ‏
✅
Context ۲۶۲ هزار توکنی (تقریباً کل یه پروژه‌ی بزرگ رو یکجا می‌تونی بدی)  ‏
✅
پشتیبانی از تصویر (اسکرین‌شات و دیاگرام…</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7768" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7767">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXARgouWS_SJaloYyWqTCG0seSXFPTxHpl5C7KLhwUcba9IhzK2_rGgxsdqevWJ3Ztptr-bbxp4S3atLya_iU_XSMeddgCmGlmyGB9iJHJfvxK383v27cjf4zqrG9VMcp-dQGFDMW7nl5hq3mUNl1S1HaCgq90MEPQ0xYDjFK2Y8RSQ_BrN16nUCfKNJaHhc0YcAk4FWXtJQFA7veH1iA9BG1RVZLRGeD9mdJz3SryeqgJmguSzczh-EOOweM5zQa5W1_T66KI6ee1nNLNVJgzF3UAYn7B9qo_sqwWoaAn7op-lJCFvJvC-YzZfvhLwOV-5cz7KxBOBC24X6h8djOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مدل جدید و قوی برای کدنویسی اومد و فعلاً رایگانه
🔥
‏
Union Alpha
امروز روی
OpenRouter
و
OpenCode
در دسترس قرار گرفت
✨
‏
چیزایی که داره:
‏
✅
Context ۲۶۲ هزار توکنی (تقریباً کل یه پروژه‌ی بزرگ رو یکجا می‌تونی بدی)
‏
✅
پشتیبانی از تصویر (اسکرین‌شات و دیاگرام هم می‌فهمه)
‏
✅
Tool calling و structured output
‏
✅
بهینه‌شده برای کارهای agentic و کدنویسی خودکار
‏
✅
داده‌هات برای آموزش مدل استفاده نمی‌شه
‏فعلاً کاملاً رایگانه
🆓
‏
🔗
لینک مستقیم:
‏
https://openrouter.ai/stealth/union-alpha
نظراتتون رو بگید
👇
🔹
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7767" target="_blank">📅 21:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7766">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">😎
یک میلیارد توکن Muse 1.3 به صورت رایگان
به کاربران جدید، تا یک میلیارد توکن در Muse 1.3 ارائه می‌شود.
(این توکن‌ها از طریق API ارائه نمی‌شوند، بلکه از طریق وب‌سایت توزیع می‌شوند.)
اینجا
ثبت‌نام کنید (از VPN آمریکا استفاده کنید)
بعد از ثبت‌نام، در تنظیمات، کد تخفیف زیر را وارد کنید:
LYA0IL
+ در opencode، این مدل به صورت رایگان ارائه می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7766" target="_blank">📅 20:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7765">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
بدون یک خط کدنویسی، برنامه‌نویس شو
😱
(جادوی Vibe Coding)
دیگه لازم نیست ماه‌ها وقت بذارید کدنویسی یاد بگیرید.
الان فقط کافیه با زبون آدمیزاد (فارسی یا انگلیسی) به هوش مصنوعی دستور بدید تا براتون برنامه بسازه! به این کار میگن
Vibe Coding
(برنامه‌نویسایی که میگن الکیه کیفیت خوبی نمیده، حتی اونام از این استفاده میکنن
😂
)
برای اینکه مثل یک حرفه‌ای خفن‌ترین پروژه‌ها رو بالا بیارید، این ۴ قدم رو پیش برید (پست رو سیو کنید که به کارتون میاد):
۱. اول نقشه بکش (Deep Research)
همون اول نگید "فلان اپلیکیشن رو بساز". اول بهش بگید:
💬
"ایده‌م فلان چیزه. بهترین روش پیاده‌سازیش چیه؟ چالش‌هاش چیه؟ برام یه دیپ‌ریسرچ (Deep Research) انجام بده."
۲. گیرِ تله‌ی پایتون نیفت!
🪤
هوش مصنوعی عاشق پایتونه، ولی همیشه بهترین و بهینه‌ترین گزینه نیست! بهش بگید:
💬
"سبک‌ترین و بهترین زبان برای این پروژه چیه که اجرای اون دردسر نداشته باشه؟"
(مثلاً خیلی وقتا یه فایل HTML ساده که تو مرورگر باز میشه، کارتون رو راه میندازه).
۳. لقمه‌لقمه پیش برو (توسعه ماژولار)
🧩
بهش نگید "یه فروشگاه برام بساز" چون قاطی می‌کنه! تیکه‌تیکه پیش برید:
۱.
"اول ظاهر صفحه رو بساز."
۲.
"حالا کاری کن دکمه‌ها کار کنن."
۳.
"حالا اطلاعات رو ذخیره کن."
۴. ارور دادی؟ فدای سرت!
🐛
کد رو زدی و ارور داد؟ اصلا نترس! تو وایب کدینگ، ارورها بهترین دوست شما هستن. متن ارور رو کپی کن و بهش بگو:
💬
"این ارور رو داد، مشکل کجاست؟"
خودش باگ رو پیدا و حل می‌کنه.
🔥
با چی این کارا رو بکنیم؟
با همین مدل های زبانی هم میشه انجام داد ولی ایجنت های حرفه ای مثل Claude code و Google Antigravity هم میشه استفاده کرد.
👇
تا حالا با هوش مصنوعی چیزی ساختی؟ تو کامنت‌ها
معرفی کن رایگان تو چنل بزاریم
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7765" target="_blank">📅 18:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7764">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پروژه bkup یک پروژه اوپن‌سورس برای اینه که فرایند بکاپ‌گیری و بازیابی پنل‌ها، ساده، متمرکز و قابل مدیریت باشه.
🎉
نسخه 1.2.0 منتشر شد.
⚙️
تغییرات این نسخه:
اضافه شدن
Restore
برای بازیابی مستقیم بکاپ روی سرور از طریق
SSH
پشتیبانی از
3x-ui، HM Panel، PasarGuard, Rebecca
برای Restore
پشتیبانی از بکاپ‌های حجیم و چندبخشی
➕
امکانات کلی bkup:
بکاپ‌گیری زمان‌بندی‌شده، ارسال مستقیم بکاپ‌ها به
Telegram
، پشتیبانی از بکاپ‌های حجیم و چندبخشی، مدیریت بکاپ‌ها، تاریخچه و لاگ‌ها،
Reassemble
فایل‌های چندبخشی و
Restore مستقیم بکاپ روی سرور از طریق SSH
.
همچنین امکان نصب خودکار پنل در زمان Restore، خروجی گرفتن از تنظیمات و انتقال آن‌ها به سرور دیگر و اجرای پنل به‌صورت
PWA
هم اضافه شد.
⭐️
اگر bkup براتون مفید بوده حتی یک STAR
روی GitHub می‌تونه بزرگ‌ترین حمایت برای ادامه  توسعه پروژه باشه.
🔗
github.com/AliRezaC-xrol/bkup
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7764" target="_blank">📅 16:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7763">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMBU86XjtX0zRTgXP1UCDqMHF_xgaJJ079LP4jsYRBBKZvmzwbHPqQHwy8EssVV0ZtRzXg7NN481mbQ57eCu0fU5699acepFY7UvH5ZV1sJkSjKz3tv6xouEU62o-KpUNuK00Jqr29HdCK8y69xADqpKJsrR5xrUdS_QLZhKJXxUjB6D53rlYzfQGe7wCUNafpFpn9dQWudL6Us-JKhWZnGpOkAZpkWQIY-BVHPJ18Q9t_rPCh2xdy2QavF51ql5aHHUOtqT_3SxNEGLOXjY01iRJUlErkJ2fKY_4iUYlAQHSaiw5GgnPi6DEhoZPrfZp5LMMzOQSv0JTDRe1mkBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل جدید دیگری از شرکت‌های چینی با نام ATRIA عرضه شده است. آن‌ها 100 میلیون توکن را به صورت رایگان برای هر حساب کاربری ارائه می‌دهند.
اینجا
می‌توانید با استفاده از حساب کاربری Gmail خود ثبت‌نام کنید، یک کلید API ایجاد کنید و از آن در صورت نیاز استفاده کنید.
نتایج تست‌های عملکرد در تصویر نشان داده شده است.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7763" target="_blank">📅 14:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7762">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⌨️
آدرس‌های ایمیل رایگان برای استفاده‌های مختلف در سال 2026: یک فهرست کامل - بیش از 60 سرویس
▫️
تکنیک "نقطه" در Gmail - اساس همه چیز
username+anything@gmail.com
→ همه ایمیل‌ها در یک صندوق اصلی. استفاده از IMAP از طریق App Password. هزاران نام کاربری فرعی. محدودیت: سیستم ضد تقلب گوگل - حداکثر 20-30 ثبت نام در ساعت، تغییر IP. سرویس‌های Oracle/Webshare، نام‌های کاربری فرعی را در مرحله اعتبارسنجی مسدود می‌کنند.
؛ SmailPro - آدرس‌های
واقعی
جیمیل ایجاد می‌کند، با بیش از 5000 آدرس در دسترس. تحویل در کمتر از 10 ثانیه. از تست‌های تشخیص ایمیل‌های یک‌بارمصرف عبور می‌کند، زیرا یک جیمیل واقعی است.
▫️
تقریباً همه جا کار می‌کند
؛ SimpleLogin —
نام‌های کاربری فرعی نامحدود
(در اکوسیستم Proton)، فوروارد و پاسخ با استفاده از نام کاربری فرعی. متن باز. نسخه رایگان: 10 نام کاربری فرعی
؛
addy.io
— قبلاً AnonAddy،
رایگان‌ترین سرویس
: نام‌های کاربری فرعی استاندارد نامحدود، متن باز، امکان میزبانی شخصی
؛ Cloudflare Email Routing
*
@your
domain.com
→ فوروارد به هر جایی. رایگان، بدون نیاز به سرور. ایده‌آل با دامنه .pp.ua
؛ ImprovMX — فوروارد رایگان برای دامنه شما، 25 نام کاربری فرعی
؛
33mail.com
— نام‌های کاربری فرعی + پاسخ‌های ناشناس
؛
spamgourmet.com
— نام‌های کاربری فرعی خود تخریبی
؛
erine.email
— فورواردینگ خصوصی
▫️
ارائه‌دهندگان ایمیل IMAP (غیر موقت، در همه جا کار می‌کنند)
-
mail.ru
-
rambler.ru
-
yandex.ru
-
aol.com
-
gmx.com
▫️
ایمیل‌های موقت با API (قابل اسکریپت‌نویسی)
-
mail.tm
-
1secmail.com
-
guerrillamail.com
-
temp-mail.org
-
mail7.io
-
anonaddy.com
▫️
ایمیل‌های موقت بدون API (وب)
yopmail.com
·
temp-mail.io
·
dropmail.me
·
emailfake.com
·
emailnator.com
·
mohmal.com
·
tempail.com
·
getnada.com
·
inboxkitten.com
·
mailinator.com
·
burnermail.io
·
fakemail.net
·
tempmail.plus
·
mail.td
·
mailpoof.com
·
trash-mail.com
·
temp-mails.com
·
emaildrop.io
·
temporarymail.com
·
generator.email
·
mailsac.com
·
tempr.email
·
atomicmail.io
·
emailondeck.com
·
crazymailing.com
·
tempmail100.com
·
tempmail.ninja
·
boomlify.com
·
tempmail.dev
·
internxt.com
·
adguard.com/temp-mail
·
webmail.raoshahzaib.site
▫️
بات‌های تلگرام برای ایمیل‌های موقت
@e2tgPM_bot
·
@mailtemprobot
·
@hidemail_bot
·
@TapMailBBot
·
@botmail_io_bot
·
@temp_mail_bot
·
@fakemailbot
·
@etlgr_bot
·
@DropmailBot
·
@tmpmailbot
·
@TempMail_org_bot
·
@TempMailer_bot
·
@smtpbot
·
@SenthyBot
·
@TempMailBot
@telegaemail_bot
·
@hs_temp_mail_bot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7762" target="_blank">📅 14:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7761">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">😎
دسترسی رایگان به FABLE 5، OPUS 5 و GPT-6 ASTRA
مبلغی معادل 1 دلار به عنوان سرمایه اولیه ارائه می‌دهد، اما با توجه به ضرایب، این مبلغ به موارد زیر تبدیل می‌شود:
🤔
Fable 5 → تقریباً 7 دلار
🤔
GPT-6 Astra → تقریباً 18 دلار
🤔
Opus 5 → تقریباً 20 دلار
استفاده از چند حساب کاربری (Multi-accounting) امکان‌پذیر است.
————————————
📝
نحوه کار:
1. به
وب‌سایت
مراجعه کنید و از طریق حساب Google خود وارد شوید.
2. یک کلید API ایجاد کنید.
3. آدرس پایه (Base URL):
https://www.rsiai.net/v1
4. برای مشاهده مدل‌ها، به وب‌سایت مراجعه کنید.
————————————
💻
نحوه اتصال:
Claude Desktop (Code):
- Help → Troubleshooting → Enable Developer Mode
- Developer → Configure third-party interface
- مقادیر زیر را وارد کنید: baseURL، api-key، model-id
————————————
♾️
دسترسی نامحدود:
1. یک پروفایل جدید در یک مرورگر ضد تشخیص (anti-detect browser) ایجاد کنید و موقعیت مکانی خود را تغییر دهید.
2. یک حساب کاربری جدید ایجاد و کلید را دریافت کنید.
3. کلید API را در کلاینت خود جایگزین کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7761" target="_blank">📅 14:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7759">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/pq6EykuV15rsticE5g5T6pU62QrQhgpXWPF2FeHDFrCi7pUBsKNiJKb0yjVLtpFQPhARQBNJIaOtWYj7F1TVJQh7YNA3oB00j_mnc1eBecvwVwA07ikN7S6pIQ5sUN3-BZ8r6mQhwWCSK4MYWCQOHrpcu03W9pTRLzyNWpjjAQJM2PoADQBokrTGUw_TEiw9kP8pRNf_l37kFzBXNBhtjH5z_6BTcLzlYMOz6Cle8bZ6DpkiwC-Kbp2LIasHqyKVlfEWNFm8bvNetZmfwGKu22M2tebcTfmr3eOGZpVu97PNquNQB4m_WiHvrvFssImBNL_tfBFHF_QR86VYpZ95iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/ulta1YbVT5KUysRBVwP7wW1c08p3u8yLLPAnw-cQaeIF7exkZtgtt0WEYKOgfXg60Rt9X5MdHL7TpfCG2bjyo1je4YyItNUXLG_J-5TPJDOfgr3GO9vOjpbv099Nko12CGsH4d-r1RDL_AUcm5PB8fyssrEXPAYRJHTSZxB6E7CwfJTfZIf84DP7SRQFIfeZFOYmmiiraiuJoBQ2SVGt5RSJkRQaco6r46sWwxi90u1i-NU8vaiun4L83a--3SGoZA5VI9NCXWwjafTGGyWIR4ROAkJJu9UhKHnmO7cTVsTTsRn086iQbzHxu5W9MYrj9syXsChVWh7qfPA2HLqg7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔥
کلونر اتوماتیک و خفن تلگرام روی کلودفلر!
‏بچه‌ها، این ابزار Serverless روی ‌Cloudflare Workers⁩ بالا میاد و خوراکِ کپی کردن و همگام‌سازی کانال‌هاست؛ بدون نیاز به سرور و کاملاً رایگان.
‏
امکانات اصلی:
‏•
🚀
دیپلوی تک‌کلیکی:
بدون دردسر و سریع روی زیرساخت کلودفلر بالا میاد.
‏•
⚙️
فیلترهای پیشرفته:
می‌تونید فایل‌ها رو بر اساس نوع (ویدیو، عکس، سند) یا سایز دلخواه فیلتر کنید.
‏•
🤖
چند بات همزمان:
هر تعداد بات که خواستید اضافه کنید و تسک‌ها رو بدون محدودیت مدیریت کنید.
‏•
⏱️
همگام‌سازی لحظه‌ای:
هم بکلایت تاریخچه رو انجام میده و هم پست‌های جدید رو هر دقیقه سینک می‌کنه.
‏می‌تونید سورس کاملشو از گیت‌هاب (‌
iamLiquidX/telegram-clone-worker⁩
) بگیرید و با یه استار حمایتش کنید.
⭐
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7759" target="_blank">📅 12:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7753">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/BKIjIDVsoTVFpranuUBXxW0tbfAx1Vy7ECrox78veAS_YEqIKkETz_6ZJ9gCofIB2gyd6L6my3rzCj6iwvxUUFw_I0oIe0nNVF1wKKxE9LoXBgf9lirVMLpQrCtfWog7d1jOt2alcx9dIFGePpPC3sWRvGxP_5M4pShETVeqW_wDaPAgHfEv0JGC3toe7C-6sVO6p1HO_D_Mm9KD-3cuTSWp5PMsjVKCCb67fEZZrNzw3Qbto2eMVfI0Blx9GDFCdV-2KyvVmk3cVgAoMAhtK-ke6abnrfLKDeQoGKhlOBCtFYOmn81pHp8AWjj7Ng2K5Y9ad7XXulnvAgPeC1VffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/OeuxOWHcTuujqTre2Z5YRyAZj4HqWusOCNljOK4jupVavZbNCBIpzozJyTlb7GSiZp3LUyPKa3_ZgzNd7jgOEwyvcv-x9-DX0ImQjJKKXUsEZNchhzrENg9Lw9JiKkwIqIV5COM4leeS-6xMv-dq78FSN5XOfDXq8lwiSPwTOHUA9N3WF1bVi9mpEOWa38hN4wHQN5tMyFlibKaUBEjOA6DypUY9E8HAMS0G9Dnmb5EDfr5Y6sXAoJNpqq2JMj6EciqSIMNqq621jGw54pNYQzQoJYhK9sbNWO401bEReqlG_kgAjHPi_KHNZ2_253BI14ewpgKriyEPt9VPSbOd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/XTlw1UDimaMXC6LQ_O97E9eQB0NiEr1e_LjPHWYToTpo-MEKNQxAnbeLPIsp1Uw7aCgSWZsS5IXH8eXzKBGsijd8VYoJ1GIRQTpOCl3JchhjEiOqnXtvNHG07No1BLofsUle8zrHZdc8ewrvUzDEC8QLcBkYR0ZKpvrLjNZufd7yAqb16y_MZfY7haDweQ5vWHMvv4jy7K_ol9afvywAcpn9paU1shW5hUaSStMynFuUQU3XFo7MV3e57My6wNgcNcANkW1L80PiGYmUaPVSACHRJQ-D9U6ePhHPlqC3G6wKqjRB8-JHRvxu6mqixm1Uljf2ZqeCS1F7k89PK_OjZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/ReY6tj7trIVv7rOfCRnclWPeRy8U5zjfW58OyiYq7i8EcuZA0CXv69QwRfk6CrHvgj1dopFlIAD1vtd9iQ_JA8ZrQahfvu_0CydFegAj7FSa-8mTtSK3IFmnRqZKEEA4-kvzhG9oqbNpSu1mSdRB0gFiS0KBEQ-8A9FBsvcBuf-Xsa9rVYoYyKN4ySmmIAAjqyVN-L6uZoHFASE0NofEgApsk1DDoXHkCpIZqbBehtB6dV8u7cC1sNz7xlVEOMtlxUMILi4KzNrlKvxAf-xyOa6AlkTeSuO8TtZMRyvPIiRk7EvgXQnl4gl1uJJXn7weI6WVrDqXp5ujYHAVqy-lJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/bUu6aNXRrEvQ_i0RidFu8VhvD0HJP0-6aVLI3IYVRsTjMRXhmDCIldqzJRYkGlqidcoPCDciWhua79MYeuHzK7h8R97mtHV0fUh2FjTDUIG1iO5VPGZc16z6u3X7seeFzTcTTLpXmIDfuun5GY3cP7SiqmqbVpv6ZvSLYsyXbNTjng2YjVlmaZrWFo6zfxSYntpgrINNrK5suw_o5BkTECgs3DX0WCYNKTecBJJjgVsUcFrU0JH8OwIUPge3rwPipAcymnl-db6AC7f0xPyih1G1x4wcrNNmxeunYN9yuxWzQVB37Yk6ME4yb9alsg69SpVFggmqgPNVqe98NDurSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/sfnecGwIjRFjXgJvT8zt77p1jiPWOa46MjA_zLcrw6aTy0pVw0uDyW2H5pN_V2DnpRWGSTpaky_Ce2QUoNjalCwLoi6We3-n0GwEboe5t9iHSktDlUSwOCsAQAv3Sn9VscRxOkRX7h7DaSxl-KwgnyMjdYAYHYlW35_jL63gXibBWQ72hhP5z0BQKbHXPx6b-YBQnNMAUtZl85J8ZbQXTxu2eOANE8miQgiOx0W9XwhzEj6dj5u8LjiF60rzMDKFI1nnnfUyj_CNaTWyCOrPNeY8egbHjFvdk3q5P0qps9rILm1RXkwaQmqellf92obyOPcAgMe2oxC293gHXoTnyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.
یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار بیشتری به دست آورید. نیازی به کارت اعتباری نیست.
1min.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7753" target="_blank">📅 10:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⌨️
؛ DeepSeek V4.1 Flash، Muse Spark 1.3 و GLM-5.3 Flash به صورت رایگان در Cline Desktop
​تیم Cline یک برنامه دسکتاپ جداگانه با تمام قابلیت‌های یک عامل مستقل را راه‌اندازی کرده است.
​
📌
امکانات برنامه:
🤔
استفاده از ClinePass یا کلیدهای API شخصی
🤔
انتقال یکپارچه وظایف از Codex، Claude Code و سایر عوامل
🤔
برنامه‌ریز برای اجرای پس‌زمینه عامل
🤔
مدیریت سرورهای MCP، پلاگین‌ها و مهارت‌ها
🤔
مرورگر وب داخلی و ورودی صوتی
​
📌
مدل‌های رایگان موجود:
🤔
DeepSeek V4.1 Flash
🤔
Muse Spark 1.3
🤔
GLM-5.3 Flash
​
📌
نحوه شروع کار:
1⃣
دانلود برنامه:
https://cline.bot/desktop
2⃣
نصب و اجرای Cline Desktop
3⃣
ورود از طریق حساب Cline یا اتصال کلید API خود
4⃣
باز کردن پوشه کاری پروژه
5⃣
انتخاب یکی از مدل‌های رایگان از لیست
6⃣
ایجاد یک جلسه و اختصاص وظیفه به عامل
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7752" target="_blank">📅 01:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7751">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz3MrPAVy_ym1kOLMqgj8WrfpbvdSftS9hsgMMYToN5glnF7cpY-Snh2Ax5CUlV-OMvkhlokMzrTiE6rdCKiJRvq1gQmOu9f8-XFf7wQ6vzCUmV0n6dWwzAoBeqs9nJ7PH9uq-PAe9_UP5gQVX5QkZl-FLjYOJaMFtG3kPQxtiIpLaYYijeYhGdWJPROedWN9iV_cfeJgqSkPaiTlv9XLqMQtSv0v_5p7vgSfIzbrIkTd1DynbYabOyA5_vK5ThlqiRKUPACgdFB7y71I0G9eGgAG0XXhTEuqOeAyoOz3w1kKpLN8dI1pypXsbzacKVqmBdaoBdbUtQWiOtLIyVxdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
؛ LIGHTVELA - یک هوش مصنوعی رایگان که 24 ساعته در دسترس است.
4500 اعتبار و 100 میلیون توکن
مزایای طرح رایگان:
🤖
1 هوش مصنوعی
💳
4500 اعتبار در ماه
🖥
2 پردازنده مجازی + 4 گیگابایت رم (محیط تست)
💾
50 گیگابایت فضای ذخیره‌سازی
🌐
دسترسی 24 ساعته
📱
ادغام با تلگرام و سایر پلتفرم‌ها
نحوه دریافت:
به
lightvela.ai
مراجعه کنید.
یک حساب کاربری ایجاد کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7751" target="_blank">📅 22:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7750">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانفیگ مخصوص چنل -
سرعت خداا
vless://e4b11ac9-46f7-4cc0-92ed-bb9dfaaf3600@94.237.92.65:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=lkMM9FR-o7Z6NwmmQVK8rLhCQR1mbJTgjY_0upeS2SY&security=reality&sid=0436301fb0178b&sni=google.com&spx=%2F442987454d44398&type=tcp#@ArchiveTell
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7750" target="_blank">📅 11:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/TR2Qr8R2WbHpYKGuWK8vAdOYxgqAZxVpDJlVfzBX12nTeNYxTIOCCy9zRK1mcW_6ZY5485TC-CCLcJcwvq43bqeZuahTECIloVtbiFLDSHXrb-j3AqPcp5cTXrokC5WWXBVqQBYKCzvkr9ybNFq0vFxBl5y7UP__mKfu8yeWmAD7BLf9yW2QIXQsukFSiINMAGdyW7qGlrApQRTUB3yTUju7tWpM5Znrayt8_IMtLgCxr1DCQce8LmVuoZhpJQGEC82VyOYsb25rQEC77jmcmL3UsYYyuYjQsTDY8_cVGxAzEbnt8OtQ-ruGhC1XERkXYK1KkkyMAqz6oZfpxZ49TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
از تاریخ ۱۴ تا ۱۶ سپتامبر، با ورود به
Z.ai
؛ ۶۰۰ میلیون توکن GLM-5.3 به شما تعلق می‌گیرد، بدون نیاز به اشتراک.
🔗
https://autoclaw.z.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7748" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/dj_UI4zKXkiwPu9H5BqnS9d2_Sk6aQQqg8KX2iMKLr64IihoXpTZr5y-gHDBqGgn2Vb6tjQ6VChYNDDlhTAze3OYO1kbPEEvdDFLg2I2LchnFTaJjGCa05b9XU3U8wVSISgpHoahKjBWfUweCZ2CNq_9WAg3X_GMnA2qwS_mGbdYTFrwX7m0XJhofoqIooSZZDt22zm35Ec4S58Oo57cym6831MtVZSdwOj4uuHM_mHlHpPo3vDMMBOfqmdiDIaYgCPqntLYzTe_xWUSyS697Z1K0ulBV7qGWLThcEJzhGpo6GuGhF_ki2fb9Kjr-M3Ll_07f4n6lWj4vT8aC2uy7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
رفع فوری خطای ریجن و تحریم Antigravity
اگر موقع کار با هوش مصنوعی Antigravity گوگل با خطای تحریم ریجن یا گیر کردن روی Eligibility Check روبرو شدید، ابزار متن‌باز
Open AG Patcher
در چند ثانیه این مشکل رو حل می‌کنه:
▫️
رفع محدودیت ریجن:
بدون نیاز به دستکاری یا تغییر کشور اکانت گوگل
▫️
پشتیبانی کامل:
از Antigravity 2 و Antigravity IDE و ترمینال (CLI)
▫️
امن و خودکار:
اجرای پچ با یک کلیک + بکاپ خودکار برای بازگشت به حالت اول
💡
نحوه استفاده:
ابزار رو اجرا کنید و شماره نسخه مورد نظرتون رو بزنید تا پچ در چند ثانیه اعمال بشه (سازگار با ویندوز، مک و لینوکس).
🌐
دریافت ابزار از گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SH_rsif76mGTGmQ-_EqEiydZ3-Q4A5Gn42dYcM_LLPgd9HZtwUrE6YUlADTSGa75vswfvF7r5h1e6zMv-wPCEThAXkynJ12GWVlP7Whg8WnbuTY62v5hXLENoSVHArt3s9pW8MrxjiHAnBHoxtVaCb3oE_rwDN-Z0WYNf-Akf616Bl312Z54_W1_f_lx01gwIIoQNkn-zPctYt_LzY_JGmSujIe0gjlX-lmqvTl6HOAMh27xCjp6rcZ_mLhJxhf-OrBtysJ_TFtgUiqvegdq_ii_e5F_hP55wElivcsvqeIRmzE6G-72Z4ucPEs4r1Uuytuuy4GMQRw8vuSXEgsE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نحوه استفاده از Claude Opus 5 و GPT 5.6 Sol
به صورت رایگان
📣
حساب‌های جدید در
Verdent.com
، یک دوره آزمایشی 7 روزه با 100 اعتبار رایگان دریافت می‌کنند
💯
🆓
🎉
✍️
آنچه دریافت می‌کنید:
👀
🔍
☑️
Claude Opus 5 / Sonnet 5
✅
GPT-5.6
☑️
Gemini 3.1 Pro
✅
GLM-5.2
☑️
Kimi K3
📌
نحوه دریافت:
🔥
⚡️
☑️
به
➡️
🔗
https://verdent.ai/
مراجعه کنید.
✔️
برنامه دسکتاپ یا افزونه VS Code را نصب کنید.
☑️
یک حساب کاربری جدید ایجاد کنید
✉️
✅
مدل مورد نظر خود را انتخاب کنید.
☑️
از اعتبارها برای شروع استفاده کنید
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔥
KiraAI
روزانه ۵۰ میلیون توکن رایگان
🤖
مدل‌های موجود قابل استفاده :
⚡️
kira-3.5-pro
⚡️
kira-3.5-flash
⚡️
kira-3.0-image
🔗
kiraai.vn
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔎
scite.ai
— موتور جست‌وجوی استنادی برای تحقیق جدی
۷ روز اشتراک رایگان (تریال رسمی سایت)
📑
Smart Citations
نشان می‌دهد هر مقاله توسط مقالات دیگر تأیید شده، رد شده یا فقط اشاره شده — نه فقط تعداد استناد
🧠
Assistant
پرسش پژوهشی‌ات را می‌پرسی و پاسخ با استناد واقعی و لینک به منبع می‌دهد، نه حدس
🤖
دسترسی به مدل‌های تحقیقاتی:
Claude Sonnet 5 | Claude Opus 4.6 | GPT 5.2
🎛
Personalized Feed
فیلتر و شخصی‌سازی حوزهٔ تحقیق ، فقط موضوعات مرتبط با کارت را ببین
🔗
Custom Dashboards
داشبورد اختصاصی برای کلیدواژه، نویسنده یا ژورنال خاص + هشدار مقالهٔ جدید
📊
Analyses & Topic Classification
دسته‌بندی موضوعی، شناسایی روندها و گپ‌های پژوهشی
آموزش فعالسازی
🔗
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1bf18H1eMZWfp5Ed6TPGlczotLNtOZc2SB3oblshLBFfbFO07jAF4e0g7Zqb_FHSeW--VDgbKRaP09sLo8jg_StDczt1G0Z_CF7l_gasUJqYcArgbqP2wfpV-WATgLTPv9srrjxOvrdRBA4U-VYPMiX4KiCGIFUaH4s_cj-YiCdqhTaRT0sVGCP-YCe0A8SF5jZ-vlrqCVwyQ9hC4ygDKNWrlifioyaLK8z5Fi1hvNqNJSJeOdXtGbaVmT0REZ2Ir_dIvoOzRyUVMAb8qZb7lfc3v7d7JCug0Vtv6XgQkNW4GzBBMCw05K5JabPiNB4fVN1vDHgzggE3ixQ-c6ASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">keys.txt</div>
  <div class="tg-doc-extra">2.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان  claude-fable-5 | claude-sonnet-5 |  deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید  @kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url: https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITzU8u561hwnOPYjN9a7VF0INPhu5brd709NQ0vo1uikNQDYvarhoJvCTn8vWgCtQAYq-RpUOnIjBdlIRDTtzt8YXTEzkmMPXRFclMDCoIPCmnxRh51ccqUDmAgeqWCcOnJWHFmU9t39coPYFveVgk9o0L4a8IlT7IGJnQJha0XTKFZc-bYZ2y7xA8lfDfxryQTaiVIpNZpE4zIjh2xjoJy2o0RmvelQzO8H7ScwfgIdW4pIJ7qhXM9FvzKHVWZ460xj_ePJdytE96VZ8xfAwcytsFLmAXIL86qTtvUGp3dLhYvUuxmgKcFaXCHq6bPH5rmqkqOppMfZK7QWZFg-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
دامنه رایگان همیشگی بدون کارت اعتباری!
‏بچه‌ها این
پروژه گیت‌هاب
با نزدیک ۲۰۰ هزار استار، دامنه‌های رایگان دائمی میده که واسه پروژه‌های تستی و سایدپراجکت‌ها کاملاً خوراکتونه.
🚀
‏•
دامنه‌های متنوع:
پسوندهایی مثل
.us.kg
و
.qzz.io
بدون هزینه فعال می‌شن
‏•
کنترل کامل:
دسترسی کامل به
Custom Nameservers
و تنظیمات
Cloudflare
دارید
‏
💬
نحوه استفاده:
کافیه برید به سایت پروژه، اکانت بسازید، دامنه دلخواهتون رو ثبت کنید و نیم‌سِروِرهای کلادفلر رو ست کنید.
‏
🔗
سایت پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⌨️
ترجمه سریع و هوشمند، بدون دردسر!
اگه دنبال یک مترجم ساده و کاربردی هستید که فقط به یک سرویس محدود نباشه، پروژه Translator می‌تونه انتخاب خوبی باشه. این پروژه با پشتیبانی از سرویس‌ها و مدل‌های مختلف ترجمه، امکان ترجمه متن، استفاده از قابلیت‌های صوتی و مدیریت تاریخچه ترجمه‌ها رو در یک محیط مدرن و ساده فراهم می‌کنه.
🤖
قابلیت چت با هوش مصنوعی؛
با استفاده از API Key با مدل‌های هوش مصنوعی گفتگو کنید و پاسخ‌های هوشمند دریافت کنید.
🔑
همچنین امکان استفاده از API Key و ترجمه با سرویس‌های هوش مصنوعی مختلف رو داره.
🌐
نسخه آنلاین:
https://codewave4.github.io/Translator/
🔗
سورس پروژه:
https://github.com/codewave4/Translator
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=MT6N22seV-fSI1hOFeunwuZ5TN3e1lDutfMpLspTNoy6sixy6x6aoTB2HgKx0TmQhgLN-u1Sw2rs3UCtW4BwC6XWJPh1SFCrE_ezmh5gQaXK6gV4YEiXalYILL3hwdXI2ZI70D4TJ23G-kUaVSmV_VBeqWDUczi1mjc0BuvOr7qbS0JsYZMjjzswmiWe8tG0Ln4UiauMvbKYCgvwlMB6CQkrOV0SPkz9PAJPElGKYt1SK_vvw_UEs2OBLyg5WB7ORAoEPJqUZZa97ng3HTYJ4Xmvh__w2UdNstc8qHPCEB6QYv10zCSOGwjAkMlcNkvE635Ccke5P4p-Yg3FRyD2kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=MT6N22seV-fSI1hOFeunwuZ5TN3e1lDutfMpLspTNoy6sixy6x6aoTB2HgKx0TmQhgLN-u1Sw2rs3UCtW4BwC6XWJPh1SFCrE_ezmh5gQaXK6gV4YEiXalYILL3hwdXI2ZI70D4TJ23G-kUaVSmV_VBeqWDUczi1mjc0BuvOr7qbS0JsYZMjjzswmiWe8tG0Ln4UiauMvbKYCgvwlMB6CQkrOV0SPkz9PAJPElGKYt1SK_vvw_UEs2OBLyg5WB7ORAoEPJqUZZa97ng3HTYJ4Xmvh__w2UdNstc8qHPCEB6QYv10zCSOGwjAkMlcNkvE635Ccke5P4p-Yg3FRyD2kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🎬
ساخت موشن‌گرافیک حرفه‌ای با یه پرامپت!
‏این ابزار هوش مصنوعی کل فرآیند ساخت تیزر تبلیغاتی، از استوری‌بورد تا تدوین صدا و انیمیشن رو خودش انجام میده و خروجی رو با بیت موزیک سینک می‌کنه. خوراک بچه‌هاییه‌ که سریع میخوان خروجی باکیفیت بگیرن.
🔥
‏
⚡️
دسترسی به منابع غنی:
۱۵۷ مدل سناریو، ۲۱۴ استایل بصری و کلی الگوریتم انیمیشن آماده
‏
⚡️
شروع سریع:
کلی تمپلیت آماده‌به‌کار داره که کار رو برای پروژه‌های فوری جلو میندازه
‏
⚡️
عملکرد هوشمند:
کافیه ایده‌تون رو متنی بدید تا در لحظه ویدیو تحویل بده
😎
برای دانلود ابزار تولید ویدیو
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nngfLskgUwmfkcYXEorc7yKFXKMiPEV-_x1Na3tVIFqw2UpHxNw4peEHkNmBSjN0tl_8m5pOkTfsljL1MnqPy7V7jJ17mYdMlRfSdBZnHd4snZ_d8bY_4k6lOvRFl2RowukkUkJAttbgoDuFur8zB8XqxUdvCNfhYigOhYQEDcx9MHpE-n1mAJORjaOURoHpMQIJ43E0ftA-nGM92TbWBpLM2DFh6fxSr9ThIMNGKq817MIKDPOexADO-cWLZpGxCCHdI3XP6V5ELrjptpZudB-uBICBIQyhZquqdPsJ17EU5qpeg_vXmylW6oMuvJE3fJpGRzjLV1Iuu6tRmeQhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
مرجع خفن اسکیل‌های ‌Claude Code⁩ و ‌Codex⁩!
‏سایت ‌SkillsMP⁩ یه کاتالوگ تر و تمیز با بیش از ۳۳ هزار اسکیل آماده‌ست که تو کار با هوش مصنوعی کلی جلوتون میندازه.
🤖
‏•
دسته‌بندی جامع:
از برنامه‌نویسی و ماشین‌لرنینگ تا امنیت و کار با ‌API⁩
🔍
‏•
دسترسی سریع:
لینک مستقیم به گیت‌هاب برای هر اسکیل
📂
‏•
کیفیت‌سنجی:
دارای ایندیکاتورهای کیفیت برای انتخاب بهترین ابزارها
⚡️
‏خوراک بچه‌های وایبکودره که بخوان پرقدرت‌تر پروژه‌ها رو ببرن جلو.
🚀
🔗
skillsmp.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🛡
دیگه ایمیل و پسورد اصلیت رو به هیچ سایتی نده!
حتماً براتون پیش اومده که برای ثبت‌نام در یک سایت مجبور شدید ایمیلتون رو بدید، اما بعد از یه مدت صندوق ایمیلتون پر از پیام‌های تبلیغاتی مزاحم شده یا اون سایت هک شده و رمزهاتون لو رفته!
ابزار جالب
AliasVault
دقیقاً برای حل همین مشکل ساخته شده:
💎
این ابزار براتون چیکار می‌کنه؟
⚡️
ساخت بی‌نهایت ایمیل دائمی:
برخلاف ایمیل‌های موقت که بعد از ۱۰ دقیقه می‌پرن، این ایمیل‌ها
کاملاً دائمی و همیشگی
هستن و برای هر اکانت می‌تونید هر تعداد ایمیل دلخواه که خواستید بسازید!
⚡️
دریافت کد ثبت‌نام داخل خود برنامه:
نیازی نیست برید یه ایمیل دیگه باز کنید؛ ایمیل‌های تایید و کدهای ورود مستقیماً داخل همین برنامه براتون میاد!
⚡️
مچ‌گیری از سایت‌های متخلف:
اگر یه سایت ایمیل شما رو به تبلیغاتچی‌ها بفروشه، دقیقاً می‌فهمید کار کی بوده چون برای هر جا یک ایمیل اختصاصی ساختید.
⚡️
نصب روی گوشی و کامپیوتر:
هم اپلیکیشن برای موبایل داره و هم افزونه برای مرورگر، و خودش پسوردها رو سر جای درست پر می‌کنه.
💬
چرا این ابزار فوق‌العاده‌ست؟
•
ایمیل‌ها هرگز منقضی نمی‌شن:
هر زمان در آینده بخواید وارد سایت بشید یا رمزتون رو بازیابی کنید، پیام‌ها باز هم به همین ایمیل دائمی میاد.
•
سقف تعداد ندارید:
برای ۱۰۰ تا سایت هم می‌تونید ۱۰۰ تا ایمیل مستعار و رمز مجزا بسازید.
•
کاملاً رایگان و امن:
بدون هیچ هزینه‌ای، امنیت و آرامش صندوق ایمیلتون رو تضمین می‌کنه.
🌐
ورود به وب‌سایت AliasVault
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5NTBOMW7bt9wMdM-8QDoOw4p4bcb-eHQ8AEt3OEyuYSEIHYxDsF6YHIggJN8O7DYN--X9NOU68SBv8GdtZ3WxqSDljmS1imID4XRZ63CrBxXS_Rl_Fj4yAwYjht1XIknB6esS2FGH-iBvtwwAPMSdBwp9b9EUf74a4GUkC8l-Yw-LPmj-sr7fPUaPMBFQgvgiumJoZyPj4CTo0F0smL4Y8_JQIAOozIpQwkvoSRidw-GuldUyjc0iYJCe82azxK4zkkMLZzkDMp01GkLR3IUKWsV1RLRJaVKa5St8T3LklTJMTioy6F2S8l2KzTspSFAiet9tHNXtFfC7LNTutV-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سایت، ده‌ها مدل و ابزار با اعتبار رایگان روزانه
🎁
💬
Multi AI Chat
GPT، Claude، Gemini، DeepSeek، Grok، Qwen ، Llama
همه در یک چت، با امکان مقایسه جواب‌ها
🎨
تولید و ادیت عکس
تولید تصویر از متن (Flux، Stable Diffusion، Ideogram…)
حذف/تغییر پس‌زمینه، حذف اشیاء و متن از عکس
Face Swap، Upscaler، تبدیل اسکچ به تصویر
ویرایش عکس با دستور متنی + تولید تصویر سه‌بعدی
🎬
ویدیو
تولید ویدیو از متن و از عکس
Face Swap روی ویدیو
خلاصه‌سازی، زیرنویس و ترجمه ویدیوهای یوتیوب
🎵
صوت و موسیقی
ساخت آهنگ (Suno، MusicGen…)، Text-to-Speech با صداهای طبیعی
شبیه‌سازی صدا (Voice Clone)، تبدیل ویس به متن، حذف نویز
✍️
نوشتن و تولید محتوا
تولید محتوا، بازنویسی، خلاصه‌سازی، ترجمه، گرامر
تحقیق کلمه کلیدی و تشخیص محتوای AI
🌐
لینک سایت :
app.1min.ai
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان
claude-fable-5 | claude-sonnet-5 |
deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید
@kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url:
https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🆓
هوش مصنوعی رایگان  — بدون ثبت‌نام
Kimi K2.6 | GPT 5 mini | DeepSeek V3.2
📌
امکانات:
⚡️
چت هوش مصنوعی نامحدود
⚡️
تولید متن و محتوا
⚡️
بدون ایمیل، بدون رمز عبور، بدون کارت بانکی
📌
نحوه استفاده:
🔗
وارد
این سایت
بشید مدل موردنظر را انتخاب کنید و شروع کنید.
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsMpRLp0xOn35J3DLj6l0QKZXpG22MaFLG0bA6mieYxzR8YIdmoHmMrT49FuDyBN-Q1GZI58UF_7HV3kXYhzN-Odrxu0ldhm2gYcARUb6_X02ENwLMIPS7Jch-JN13iepDvVvFhwxGPCZe7DKuF8wLm_j-CpigEfAbh-c88--Y5BrLHqLmYUw0Acm36Ev0E-8SQSnzKnMr3IBX4UtBUaBqmNy-h6G1RmTACQ-DS974N8A3qGFXiHWLALcWXfUDIF5SJ-EUmtOdmFtRxF5UgGIEtyxedEMhngfRiOYMMj7id5JkwTHOBWGYG1oslYkd_cVe_SRyB5nt8Uw7-gS_KZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
۵۰۰ مگابایت پروکسی رزیدنتیال رایگان (
proxyma1.io
)
یک سرویس پروکسی رزیدنتیال که با ثبت‌نام از طریق تلگرام ۵۰۰ مگابایت ترافیک رایگان می‌دهد و API هم دارد.
📌
نحوه دریافت:
1️⃣
وارد سایت
proxyma1.io
شوید و ثبت‌نام کنید
2️⃣
پس از ثبت‌نام، یک پیام برای استارت ربات تلگرام نمایش داده می‌شود که داخل آن یک کد هدیه قرار دارد
3️⃣
ربات را استارت بزنید و کد را برای ربات ارسال کنید
4️⃣
۵۰۰ مگابایت به حسابتان اضافه می‌شود
🚀
📌
ویژگی‌ها:
☑️
پروکسی رزیدنتیال (Residential)
☑️
۵۰۰ مگابایت ترافیک رایگان
☑️
پشتیبانی از API
☑️
ثبت‌نام آسان با تلگرام
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffe2HuL0GmKuEzPHzdU7BN6NT38XjI5tv_EivXwES-8VR50ZB0uSMKeJdJ5UfJekEmTig0R2v-Al6ORDwZ6Nyd1G22T6Lcb_MPOjmPeImzgSt9U_r60BYvc9L5BiYS0pAHsUymHrHPhUaGRu9n3OEw9VCdt8cW-FnDbwe1LHlKQ7-1xK_2OCEViV3-_HmZBMmiUAVkYikqbU8L6ZuaDOn6aH8Aw1dvxH22J7OuNedICjqxSPPx956idsCi5cpFfaTvvxGkHUzsiR0wO9zS-3UqEyjrgDEmdS7jETtTiS3j_X65ijFnbCDyj9b45PH3QD87fEyY63el2ORrltmZV90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۵۰۰۰ اعتبار رایگان برای مدل‌های برتر هوش مصنوعی
پلتفرم جدید در شروع کار ۵۰۰۰ اعتبار به شما هدیه می‌دهد تا با قدرتمندترین شبکه‌های عصبی کار کنید: تولید متن، عکس و ویدیو در یک جا.
📌
امکانات در دسترس:
☑️
چت چندمدلی
☑️
تولید تصویر
☑️
تولید ویدیو
☑️
موجودی اولیه: ۵۰۰۰ اعتبار رایگان
🪙
📌
روش دریافت:
1️⃣
ورود به
getunikey.ai
2️⃣
ثبت‌نام یک حساب کاربری جدید
3️⃣
ایجاد کلید API در تنظیمات پنل
4️⃣
استفاده در رابط چت یا ابزار های واسط
base url:
https://getunikey.ai/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔍
Hidden File Hunter — شکارچی فایل‌های مخفی ویندوز
دنبال فایل‌های مخفی و سیستمی توی ویندوز می‌گردی ولی پیدا کردنشون واقعاً دردسره؟ این ابزار دقیقاً برای همین ساخته شده
👇
؛ Hidden File Hunter یک برنامهٔ دسکتاپ ویندوزیه که تمام فایل‌های مخفی و سیستمی درایوهات رو پیدا می‌کنه و توی یه جدول مرتب و قابل مرور نشونت میده.
✨
امکانات:
✔️
پیدا کردن تمام فایل‌های مخفی و سیستمی در همهٔ درایوها
✔️
نمایش نتایج در یک جدول مرتب و خوانا
✔️
خروجی گرفتن از فهرست کامل مسیرها در قالب فایل TXT
✔️
کپی کردن خود فایل‌ها با حفظ ساختار پوشه‌ها در مقصد دلخواهت
✔️
فقط می‌خونه و کپی می‌کنه — هیچ فایلی رو تغییر نمیده، حذف نمی‌کنه و بهش دست نمی‌زنه
✔️
ساخته‌شده با Python و PySide6
✔️
تم تیره و روشن
✔️
رابط دوزبانهٔ فارسی و انگلیسی
یه ابزار ساده، سریع و امن برای وقتی که می‌خوای بدونی توی سیستمت چه چیزهایی از چشم‌ها پنهان مونده.
🔗
لینک گیت‌هاب:
github
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚀
اپلیکیشن Bifrost (بایفراست)؛ پل ارتباطی فوق‌سبک تلگرام بر بستر ورکر کلادفلر منتشر شد.
بایفراست یک بریج لوکال (Local SOCKS5) مدرن و بهینه برای اندروید است که ترافیک تلگرام رسمی را از طریق پروتکل TWP به ورکر رایگان کلادفلر متصل می‌کند؛ با پینگ پایین، بدون قطعی و با سرعت دانلود فوق‌العاده بالا.
🔒
بدون نیاز به VPN، بدون روت و با مصرف باتری نزدیک به صفر:
این پروژه کاملاً متن‌باز (Open-Source) است و برخلاف فیلترشکن‌ها از VpnService استفاده نمی‌کند (هیچ علامت کلیدی بالای صفحه نمایش داده نمی‌شود و اینترنت سایر برنامه‌ها کاملاً دست‌نخورده و بدون تغییر باقی می‌ماند). مصرف پردازنده در زمان عدم استفاده دقیقاً ۰.۰٪ است و امنیت و رمزنگاری پیش‌فرض تلگرام (MTProto) نیز کاملاً حفظ می‌شود.
📥
دانلود و نصب برنامه (از گیت‌هاب):
https://github.com/Qorvhex/Bifrost/releases
⚡️
کانفیگ تستی برای شروع (بعد از نصب، کپی کنید و داخل برنامه Paste کنید):
twp://telp.qorvhe-x.workers.dev?clean_ip=1music.cc#Bifrost-Test
🛠
سورس‌کد اسکریپت ورکر (TWP):
https://github.com/Qorvhex/TWP
📁
لینک پروژه و سورس‌کد در گیت‌هاب:
https://github.com/Qorvhex/Bifrost
لطفاً تستش کنید و سرعت و عملکردش رو بهم بگید!
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🖥
مرورگر ضد ردیابی Private Browser Pro؛ هویت جعلی و دور زدن بن شدن اکانت‌ها!
​بچه‌ها اگه نیاز دارید روی یک سایت چند اکانت مجزا بسازید بدون اینکه سیستم‌های امنیتی بفهمن همه‌شون مال یک نفره، یا می‌خواید ردپای دیجیتالی‌تون رو کامل مخفی کنید، این مرورگر اوپن‌سورس ویندوزی دقیقاً همون چیزیه که دنبالشید. این ابزار بر پایه نسخه فوق‌امن Ungoogled Chromium و Electron ساخته شده و از زبان فارسی هم پشتیبانی می‌کنه.
​
🎭
جعل مشخصات سیستم (فینگرپرینت):
شبیه‌سازی کارت‌های گرافیک قدرتمند (مثل RTX 4090، سری RX 7900 و تراشه‌های اپل)، اضافه کردن نویز به Canvas و AudioContext و هماهنگ‌سازی هدرها برای عبور آسان از سد کپچاهای Cloudflare Turnstile، hCaptcha و reCAPTCHA
​
📁
مدیریت و تفکیک کامل پروفایل‌ها:
امکان ساخت محیط‌های دائمی (Persistent) برای ذخیره دیتای هر اکانت در پوشه جداگانه، یا حالت موقت و یک‌بارمصرف (Ephemeral) که با بستن پنجره کل ردپا پاک میشه + دکمه پاک‌سازی آنی
​
✅
پروکسی پیشرفته و ضد نشت اطلاعات:
پشتیبانی از پروکسی‌های SOCKS5 و HTTP (با یوزرنیم و پسورد)، حل آدرس‌ها از داخل پروکسی جهت جلوگیری از DNS Leak و غیرفعال‌سازی WebRTC برای مخفی ماندن کامل IP واقعی
​
✨
محیط کاربری تمیز و دو زبانه:
کرومیوم دست‌نخورده بدون واترمارک‌های تستی، تم دارک با کلیدهای میانبر سریع و پشتیبانی کامل از منوی فارسی و انگلیسی
​
💡
بهترین سناریوی استفاده:
ایده‌آل برای مدیریت چند اکانت در شبکه‌های اجتماعی و پلتفرم‌های حساس، تست وب، ریسرچ‌های OSINT و حفظ حریم خصوصی بدون نیاز به خرید اشتراک‌های گران‌قیمت مرورگرهای ضد ردیابی.
​
🔗
گیت‌هاب
​
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📥
تبدیل فایل‌های تلگرام به لینک مستقیم نیم‌بها با ربات Leecher!
بچه‌ها اگه کندی دانلود از تلگرام یا قطعی فیلترشکن موقع دریافت فایل‌های حجیم کلافتون کرده، یا می‌خواید تورنت و ویدیوهای یوتیوب رو مستقیم به فایل تلگرامی تبدیل کنید، این ربات لیچر ایرانی حسابی به کارتون میاد.
🇮🇷
لینک مستقیم با ترافیک نیم‌بها:
تبدیل آنی فایل‌های تلگرام به لینک دانلود پرسرعت تحت وب (سازگار با دانلود منیجرها) با محاسبه مصرف اینترنت به‌صورت نیم‌بها
🌐
دانلودر همه‌کاره (لینک به فایل):
پشتیبانی از دانلود مستقیم لینک‌های یوتیوب، اینستاگرام، وب‌سایت‌ها و حتی فایل‌های تورنت و تحویل فایل داخل چت
☁️
اتصال ابری به گوگل درایو:
امکان لینک کردن اکانت شخصی Google Drive برای ذخیره و آپلود مستقیم فایل‌ها در فضای ابری بدون مصرف حجم گوشی
🎁
شارژ رایگان روزانه:
۱ گیگابایت حجم رایگان در هر ۲۴ ساعت بدون نیاز به پرداخت هزینه یا خرید اشتراک
💡
نکته کاربردی:
لینک‌های ایجادشده بین ۶ تا ۸ ساعت معتبر هستند؛ کافیه فایل رو به ربات بفرستید، لینک مستقیم سرور ایران رو داخل IDM کپی کنید و با حداکثر پهنای باند خط‌تون دانلود کنید.
🔗
استارت ربات
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UapgjYq55d5HYJBBrnQDeDpdYFtoJ9oVHo-xjaAIOUYAbfZ8PckaIwrnOZVs6sZGoRPPRf-AVZ42rquViczFu1eBsI-l1_in-vkLk23f16paot5Jj0SZCaprHcGyMcZmi7wOIbFfnxDejJbWKFyrex8FEGgO7uX_j6HNro7t_2dKLTA-4dsP6AEbIhLUYzNtwvgb-cBGCXGIFoBwd6IH7lUDRJPRKssvwkS_XyK_3rlXuZnJ44rz5BPEXaPmse5yj1vxFuJyKl9IrQphXKUOL337HDd1PaGnJ5AXB2_5zHO0tUiEGe1F64EoMNBg2DvrNZSNvpnprDc2trVBtRZjEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید (1.8.0) برنامه MSN-GUARD منتشر شد :
💢
BOOM
💢
تغییرات :
1- اضافه شدن متد اختصاصی SHARD برای اولین بار
-_-_-_-_-_-_-_-
2- دسترس‌پذیری کامل و پشتیبانی 100% از صفحه‌خوان TalkBack برای عزیزان نابینا و کم‌بینا برای اولین بار
-_-_-_-_-_-_-_-
3- آپدیت هسته
-_-_-_-_-_-_-_-
4- اضافه کردن قابلیت Backup و Restore و Reset Factory از تنظیمات برنامه
-_-_-_-_-_-_-_-
5- برطرف شدن مشکل دکمه Reconnect در نوتیفیکیشن
-_-_-_-_-_-_-_-
6- اضافه شدن Theme کاملا روشن برای استفاده زیر آفتاب
-_-_-_-_-_-_-_-
7- برطرف شدن باگ اتصال خودکار پس از قطعی اینترنت و چند باگ دیگر
-_-_-_-_-_-_-_-
6 روش دسترسی به اینترنت آزاد:
1: متد Masque
2- متد Wireguard
3- متد Warp On Warp
4- متد Psiphon (اختصاصی و اولین)
💯
5- متد Tor (اختصاصی و اولین)
💯
6- متد SHARD (اختصاصی و اولین)
💯
💻
ریپازیتوری گیت‌هاب (متن‌باز):
https://github.com/mbm110/MSN-GUARD
📌
لینک مستقیم دانلود :
برای گوشی های 64 بیت
برای گوشی های  32 بیت
برای تمامی گوشی ها
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✉️
؛ Turbo Mail ایمیل موقت، سریع و بدون دردسر
اگه برای ثبت‌نام یا دریافت کد تأیید به یه ایمیل موقت نیاز دارید، Turbo Mail یه گزینه ساده و سریع برای شماست.
⚡️
ساخت فوری ایمیل موقت
👌
بدون نیاز به لاگین و ثبت‌نام
⏳
اعتبار ۲۴ ساعته
🔒
مناسب برای دریافت ایمیل و کدهای تأیید
🚀
ساده، سریع و بدون مراحل اضافی
کافیه وارد سایت بشید، ایمیل موقتتون رو بسازید و استفاده کنید.
🔗
https://mail.turbocenter.shop
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎧
دستیار هوشمند و همه‌کاره موزیک‌بازها؛ دانلود با کیفیت FLAC با ربات MelodyAddict!
بچه‌ها اگه عشق موسیقی هستید و از دانلود تک‌به‌تک آهنگ‌ها، افت کیفیت یا پیدا نکردن موزیک پس‌زمینه کلیپ‌ها کلافه شدید، این ربات فوق‌العاده با پشتیبانی کامل از زبان فارسی دقیقاً خوراکتونه. همه‌چیز از شزم اختصاصی گرفته تا رصد خودکار پلی‌لیست‌ها رو براتون یکجا جمع کرده.
🔄
سینک خودکار پلی‌لیست‌ها:
زیر نظر گرفتن لایک‌ها و پلی‌لیست‌های Spotify، SoundCloud، YouTube Music و Apple Music و ارسال خودکار ترک‌های جدید با امکان زمان‌بندی ارسال (۳ ساعته، روزانه یا هفتگی با دستور /digest)
🔍
شناسایی جادویی آهنگ:
پیدا کردن نام و فایل موزیک فقط با فرستادن یک وویس کوتاه، زمزمه، فایل ویدیویی یا لینک ریلز اینستاگرام، تیک‌تاک، یوتیوب و توییتر
💎
کیفیت استودیویی FLAC و Lossless:
قابلیت تنظیم کیفیت پیش‌فرض خروجی برای گوش دادن به بالاترین بیت‌ریت ممکن، با سرعت عالی و کاملاً بدون تبلیغات
📂
مدیریت پلی‌لیست‌های ابری:
امکان دسته‌بندی، ساخت و اشتراک‌گذاری مستقیم پلی‌لیست‌های شخصی داخل تلگرام
💡
نحوه استفاده:
ربات رو استارت کنید، زبون رو روی فارسی بذارید و برای شروع کافیه وویس یک آهنگ یا لینک پلی‌لیست موردعلاقتون از اسپاتیفای یا ساندکلاد رو براش بفرستید تا بقیه کارها رو خودش اتوماتیک انجام بده.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u8J44Mz2vfnFV8pH0movhToctbaJEeq4D9qo7Rqp6sn_7jrET05TlZih4FGONRgxM2FBVxxZGLCy4XBIjp0swQm_YV04kcICRQ6Hfs3AOpBwdqwn0Xu3QNHyB6IQUO7-0cCgOAL5E_X5TKqACy4dtsRkNhxGdvbMrm_oC0q-7wy3Mecl5gXw2zKSxTWza8XBExD7LRmFa3poXazryiAPeHFCDNmBleH9fKpVR57EVH-Xys1M3_Z1gHs8ecEZkarIHM6oRMuXLTuWcNmRYmMhZISK9eXNDG-DMkpnjyAtkPj6xHuKECM9tnceku9J2iiBoqJxJNNI1Lc13euNMe5nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید ArasClient منتشر شد!
نسخه جدید با اضافه شدن بخش Free منتشر شد و از این به بعد این بخش به‌صورت مرتب آپدیت میشه.
📱
؛ ArasClient یک کلاینت سبک و کاربردی برای مدیریت و استفاده از کانفیگ‌هاست که تمرکزش روی سرعت، سادگی و اتصال راحت‌تره.
🆕
اضافه شدن بخش Free
⚡️
آپدیت منظم کانفیگ‌ها
📊
تست و مرتب‌سازی هوشمند سرورها
🔄
انتخاب سریع‌تر سرورهای مناسب
📦
پشتیبانی از نسخه‌های مختلف اندروید
🔗
دانلود نسخه جدید:
https://github.com/ArasTey/ArasClient/releases/download/v1.6.8/ArasClient_1.6.8_arm64-v8a.apk
🔗
سورس پروژه:
https://github.com/ArasTey/ArasClient
💬
نظر، انتقاد یا پیشنهادتون رو کامنت کنید.
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhdTr3DndnaD9gGWb7F2VEYiKrtHam02GcYfMgbDEeFiKVOJwl6cYtwWgtSF_bjYiEOkJ4Ek1kSX7JsV-a31Rytb71O62tzS8XIqWeDZaEkIimkpk0Qv3kPrh5_XUYjyQ0a9T5KU2ixNgY6NIGi4RDNdBDarW_GpY9iRnO16Ta5hFZbhxxcedn9NwjDalcnQSN5Pw-TyEuLXLNP358PcEc6iZukrlVCUeFPYokV3C8pbiFgUFQ28V4RhzReZFati9YVVhdcvxPN75FFn8Gz5djFjV31ngTUDNwsHr3Qe5PXuyBKpeQYkQjp5AGt516sL7mVIGNFszol-jWr6xC2j7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
اگر می‌خوای شبکه‌های کامپیوتری رو از پایه تا سطح حرفه‌ای یاد بگیری، نت‌داد دقیقاً برای تو ساخته شده.
از مفاهیم بنیادی مثل آدرس‌دهی IP، سوییچینگ، مسیریابی و امنیت گرفته تا شبکه‌های مدرن، همه چیز با پروژه‌های عملی و مثال‌های کاربردی آموزش داده می‌شه.
✔️
۱۰۰٪ پروژه‌محور
✔️
۵۳ درس تخصصی
✔️
۱۴ بخش آموزشی
شروع یادگیری از اینجا:
🔗
https://netdad.vercel.app
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnmAnwAKCwyp3qQL--_5eywNi4xnvkk1tPPdFBG-yF_wzY7ERUlTO70aFr3r0XMH7SwGac04u8lF9MaDmtL5BDJh3nJJxEDsqqXMpxzXL_n_g6mMnPVVxXyxKEa5GbVZWlojjWvx3C78rqlXj4BRwaPHsiGbXoMxD5zZGDgfchngpERxfjmkAW5GESA6UH04mwQ6Yxz_XX2CFjqiFb0aEeWoeEmTBgYQ1pdQ7as_6QKPe8sYkdQ95wGBlpeDaYhEGVgW8JOzMW4aC_r4OKEK3Hz0uihressxWZRt69d8iRK5rIy_Rc4mzMRBeLAFHJ4cz01yMFL43qk6y170uLmHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MK8zxBcJC1ZC6r673p1QjGOi4jvUWQwtp3a-HKeEkv9L86j0v_VHK-UyUZOoZ8YWaBRwpSCflCfmtupvrNloGK6OWTa6ZVHp4v91x8rwRuL6XEDZaGoyNYmb9Z94-2OoqUglaw9Yu4GqUSXb3vP5qd6WKzJp8K6QV4hgOACwP_mtogtf_sOLAFgXMe0L4P-NCdOmkTUlDCVlf7Y475oAyfoLiaFSfozon2OHd6wkjxPHY4A-4uIi83IkJwMsK1YNMwVcsHj5KRQ3WNLRbfaTnaRDfUXXrpdulSo1Xb-ykoTWcqh0cs7Wi43I3I3PvvVRZ14kyu_QlvuOyOope9XGvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥁
کیبورد لپ‌تاپت رو به یه درامز حرفه‌ای تبدیل کن
پروژه خفن KeyBeat یه استودیوی درامز تحت وب هست که بدون نیاز به هیچ نصبی، مرورگرت رو به یه ساز واقعی تبدیل می‌کنه
🔥
یه پروژه اوپن‌سورس عالی برای برنامه‌نویس‌ها، آهنگسازها و عشقِ موزیکا
🔗
لینک سورس کد و اجرای مستقیم:
https://github.com/faithsaly5-stack/Keybeat
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-xNFBMsXHv9DxyX74PLFK_Zh0fHy_IbA1Qki1vJfkSXiDCkUuptA4_HmRLObluGlVhPQG4OSs2_JwfvV4vPrnkCOGjPVIWmyV3KBKlTcKzipUEOCeefqonkljletIOquQcJmrHMI-pELSSVNfBiWOn0swqwTzizpq3e9XozuYRjLM289nD1oAWqOULk58KoT4D_lHmNWdBavGjZIQ0q6z2KcCjQZv856O5Qwxfto2afJQVFu6jH5cAo0r97LZbT1WnXUJnIINxiBzTsNyADSIQCSEFZM1hVgeb7Lh9n_VtQbvkRgXenpFpfinKL7v5SmLgqKpPlPBVm17TW68CxFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دریافت آیپی رزیندنتال رایگان
💎
با گوگلتون سایت زیر بشید و روی claim offer کلیک کنید.
بعدش برید بخش proxy generator و پرش کنید و بزنین براتون 300 مگ آیپی رزیدنتال میده
🆓
http://rainproxy.io
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py6x8LnoZN2B0Mh7zIW3vLbDNUfmqoScQGeKROIW3nG0ox6F3Pu688tPZO8ZpF3Os7JkQK9_NB8QO15k92vD9hTrRshNTiRnLEBJCcMAaavceHJCbDo1AXfd6VN791qBCGd9n_R7g9V7yH_A7q2jOAiUw6791-qN5xpNxYcUrjvXy99zinIt61d_9q0FPMhXSbPYhqN6QkfT03PAvacKLqM_s7qwasZYnSYyzgIca-gszy9DoVYHezGZrILd1b7cx99XLsxXqS-C6BpGyyOlWgq6x7dNvZ5dUj6tIl7bFCtZgJZ-mV723gbP4evY9xfMoR_Pg0hca4jSMntL8jojCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
15 دلار اعتبار رایگان برای دسترسی به بهترین مدل‌های هوش مصنوعی
استفاده از مرورگر به شما 15 دلار اعتبار می‌دهد تا مدل‌هایی مانند موارد زیر را امتحان کنید:
• GPT-6 Astra
• DeepSeek V4.1 Flash
• GPT-5.6 Luna
• Claude Opus 5
• Grok 4.5
برای دریافت:
🔗
browser-use.com
با استفاده از حساب گوگل خود ثبت نام کنید و شروع به استفاده کنید.
برای دریافت اعتبار بیشتر، از چندین حساب استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🧰
جعبه‌ابزار همه‌کاره و فوق‌سریع تلگرام؛ معرفی آپدیت بزرگ بات Amir Tools!
بچه‌ها اگه کلافه شدید از اینکه برای هر کار کوچیک (هوش مصنوعی، استعلام قیمت ارز، دانلود یوتیوب و تبدیل فایل) یک ربات جداگانه استارت کنید، این بات همه‌کاره دقیقاً خوراکتونه. در آپدیت جدیدش کلی ابزار مدرن با رابط شیشه‌ای اضافه شده تا از ده‌ها بات متفرقه بی‌نیاز بشید.
🧠
هوش مصنوعی با حافظه اختصاصی:
مکالمه پیوسته بدون فراموشی کانتکست چت، سوئیچ خودکار روی مدل‌های پشتیبان و امکان ریست سشن
📥
فایل به لینک مستقیم و دانلودر یوتیوب:
تبدیل آنی انواع فایل، ویدیو، آهنگ و ویس به لینک مستقیم پرسرعت + دانلود مدیا از یوتیوب با بالاترین کیفیت
📈
نرخ لحظه‌ای و چارت زنده بازار:
استعلام آنی قیمت دلار، تتر و ارزهای دیجیتال (BTC, ETH, TON و...) همراه با نمودار اختصاصی و باکس High & Low
🤫
پیام ناشناس امن و دوطرفه:
ساخت لینک اختصاصی با آیدی تصادفی برای دریافت متن، ویس و عکس ناشناس با قابلیت پاسخ‌گویی مستقیم
🎁
سیستم قرعه‌کشی خودکار کانال:
ساخت مسابقات و چالش‌های گروهی با دکمه شیشه‌ای و قرعه‌کشی کاملاً خودکار و عادلانه بین اعضا
🛠
میکروابزارهای روزمره:
ساخت بارکد تصویری (QR Code)، پسوردساز غیرقابل‌نفوذ، مبدل ارز به تومان، هواشناسی و مینی‌گیم‌های کوئیز
💡
نحوه استفاده:
وارد ربات بشید، دکمه شیشه‌ای منو رو لمس کنید و بدون نیاز به رجیستر یا مراحل طولانی، به تمامی ابزارها به‌صورت یکپارچه و رایگان دسترسی پیدا کنید.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpGDLaumB2clMw9zuLSg5q_hoO_zb1ZaQDeljtRwbkcx9GkLl0S7fcfTxETs55_0-UAJNfHDoWeil82kpoqvi3IzeJfKV55vXWPBWwo7isTyZMS540I6jyetGTT3mMgyXL2GIV9Tz4KbuT9v1zaF33FpF_PQxIi073c8ZOlhBb69HGdA6D5dH7z933vHtdVZDNDftg1bpxmkJh-C5oHLbsGaBixT5rGKl8uEneCmd7KB-ctTjnG-DWvV9q-ZYh07earnw-ELftv7lhBn_8r1EmNQ8iambd3NPDevM7NfcA5hpRsBdVX2rvEb0tLsCeuIXUKF64KyXBHbdZuiaPXXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل:
① به
https://arena.ai/
مراجعه کنید.
② حالت
Direct Mode
را انتخاب کنید.
③ در لیست مدل‌ها،
GPT-Image-2.5 Sunburst
را پیدا کنید.
④ به مدت
72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود
.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpLnmiKPj1pN88i_HLPhOupu-01l8uMoiYVgjKQRkyz7jcxxnyNhjPifHllgxOcYxeKl_wY899dXwRE_7qGnSvjRvyZXLPeSesP80jV8n0r6yt3yRWPkIyPFgkqPGq5JcUffUvwACcOLM6QgM365aueYKRdztSo5ugDhZs_2LGVlZOFGzel1Cp_WCsB5yz0ofY-f7aU2A3KBvGnyGWoC1o8ScPLTCpNwXFeTs6fu7eAFwbYKcdwD8xdEebpk0D1o5VMLmasyLsHHhcA7INL46JMZlwctG2JBWQPe0lULCSfY2BA9R2kAXkN5w8QeL11qRly9IsyDyyUoQErsgJnnRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4.1 Flash به صورت رایگان
💥
🆓
این نسخه ۲ روز پیش منتشر شده است. دارای ۱ میلیون توکن متن، قابلیت‌های بصری پیشرفته و کیفیت مناسب برای استفاده در سیستم‌های هوشمند است.
🚀
🔺
رایگان به صورت روزانه
🔺
پنجره متن با ظرفیت ۱ میلیون توکن
🔺
سهم استفاده روزانه هر روز ریست می‌شود.
هنوز مشخص نیست که این سرویس چه مدت به صورت رایگان باقی خواهد ماند.
‼️
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuOvrBMyT0yI8NESnWUGIPZEKQEoFKUV0gASx5rGFknZTs4tWc8gUsW3oYzomth5K8ytrC6ErIAxSzUvFwJg8HU3a1X-9-RXD8_OAV2extTogG_iy8-bNydw1d2732SI2fafLnXjvRocI9z2dgoF9QjsC9k1JzQxreq8SBrVTR08W4rqryb8XC_YBeXX7-PparP0e1CnIos_rCEy1nSs8u_DmsJ-VYUVkIDtwTtJhDYolmUxRKIprnoEsMYjMPTSBfkXnulDCgyLMY17Bb3M1eMdBPoZW7dFA9PstSsRz26rx7o1uzTY_YEKZ1EilknHb3as_K-wPP_eAT507QiNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
📌
Base URL: https://tokenharbor.ai/v1  با جیمیل…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-HbXYKJUN3gkuXUpl3sRmMliq4bHYN4XsiPBhGYMnbSW7Mk8xn4uzDy52X5aFYE_V_sQu74hsZe3KnuAqJsvNK_xNN8YNRZu_AJ3gjaKwj-hYWBXn-unUeIec1wTgBMJ2kiIGH2bebnITGXzUqKFEF2X7I7C1oGWLR81pgElgbMGio6BjZk1cBkL0yxCNsaGIOBWQsYM2Nvh9QxxpKfOOyaeTtBcLwLfmmIuJX2qOWasks69YXSQcZ7qhhRTODRVJe4l0oddbie9CDpbazfe0R4PYzRVC1oRbruAxtAMRNYa9QZ5u29_wpDRrWa4ku7k2cih50xEu0VJtdRRhwH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcUYFKdojYv9TiqLPff6gqOFrvUpQpa3O5QBU_4rmORfmhyRe2UgtfFe_wLEftrrRNENiy2EudjW3PmRlJbn8Ihwqrh3jspdGYKdqttRt71mvMv8WFgLaUl_ToeUcopHwVikqUWfw7B0a5YE_XpI6kzdy-keK_qi0nILLTaqPzUy7ddD2ZDh3VAC3DrLXXGamsNWWLx2GUPmRUTZd5-vCwYJeJxKEPoriolLrTdHcSE3nuaSd1K5F66xaaNhVjk-6GZz3Pf7WaNjxorkejdacKvCUaDnclTGl-yDcJ4DabzNlj7emOiU7G5P8_o3y2ke6BiDvDn7KOpuBN5ikLaMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">150 میلیون توکن رایگان برای مدل های زیر
💥
🆓
GLM 5.3 Flash | Qwen 3.8 Flash | Mimo 2.5 | GLM 5.3 | Hy 3 | Qwen3.8 27b
✅
وارد سایت زیر بشید با جیمیل ثبت نام کنید سپس از طریق منو 50 میلیون توکن امروز هم دریافت کنید
✅
‼️
نکته :
از مدل های با پسوند Free استفاده کنید و احتمالا این دسترسی شامل محدودیت تعداد ریکوئست در دقیقه باشه ، همچنین ممکن هست هر لحظه اشتراک رایگان بپره
📌
Base URL :
https://kiraai.vn/api/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🧠
پروژه OXYGPT — یه ربات تلگرامی که هوش مصنوعی رو حسابی جدی گرفته!
بچه‌ها این صرفاً یه ربات چت نیست، یه اکوسیستم کامل AI روی تلگرامه: چند مدل هوش مصنوعی، مربی‌های حرفه‌ای تریدینگ، sandbox واقعی لینوکس، اخبار فارکس زنده و داشبورد مدیریتی. خوراک کسایی که می‌خوان یه بات production-grade بسازن نه یه دمو دو ساعته
🔥
↔
مسیریابی چند-مدلی AI
: استخر کلید Gemini + سرویس‌های سازگار با OpenAI، round-robin می‌چرخن و روی خطای 429/503 خودشون فالبک می‌زنن
🪟
پنجره‌های مکالمه مجزا
: هر کاربر تا ۵ چت جدا با تاریخچه و state خودش می‌تونه باز نگه‌داره
🧙‍♂️
مربی‌های تریدینگ (Persona)
: چهار شخصیت آماده (ICT، Quarterly Theory، Matrix/369، Price Action) با یه دستور سریع صدا زده می‌شن
📓
ژورنال معاملات
: ثبت و پیگیری ترید‌ها با قالب‌های اختصاصی، مستقیم داخل تلگرام
📰
اخبار فارکس زنده
: رویدادهای پرتأثیر Forex Factory رو با تحلیل کوتاه AI نشون میده
🖥️
قابلیت Sandbox واقعی لینوکس (E2B)
: مدل می‌تونه کد اجرا کنه، پکیج نصب کنه، ریپو کلون کنه و فایل بفرسته/بگیره
🔑
قابلیت BYOK
: کلید API خودتو وصل کن، از محدودیت پیام و quota عمومی بی‌نیاز شو
👁
مانیتورینگ کانال با AI
: کانال‌های تلگرام رو زیر نظر می‌گیره و پست‌های مهم رو تحلیل و تحویل میده
💡
دیپلوی با یه دستور روی Docker/Railway انجام میشه، و هر ۵ ساعت یه بک‌آپ خودکار از کل دیتابیس‌ها زیپ و برات تو تلگرام ارسال میشه — دیگه نگران از دست رفتن دیتا نباش.
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1U7sGBpV5-BENWn882VFTwD1G9wI7wWNBmLqeYmILRG9GdOdnXSYPl7Akq-H9bDa7V5ENlJvwqGSwizDljztbF8NmnsJ1-x6wWr_BdrnW95eGWxVK48NgSE4KGNLdWWm5Wx4-v94m0gy_6zto9R05VGlw8lMx9R9oM6qb8dj4gH5gwWKSRkmLKpPBitA8LL0xrHgjxGlZVeQI6I4eU-vyDLEgG12hCWeXmutlr8THiVQL90exFfL4dArdJMsessguEHy261vCfbA8_DOO7jLs7R6BbPrr03h5nQuLdzbLrKuHbxcKhisuvk65TpTZ77jAXnmoTzZNoPrsMY7pXlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDgUnl__WJGl7DFeZBfoucPQ_YJ3eGOpuAW0TGpYgVNYZMchayj941OUp4QhFdGn3L8uvhaoPtyrcp2P18ioUppvMkee-yEs5zMKffs-ObaNAWPS2GwQ1bbPfK_Sbx1RV79oXHlDEkZNlASUbJ9ey6DpHtWEWSojfXj_ds2zc7wp0PuQWKHKgxadfzp0OEnZvU8bFY_-9KGggWbvZ0dd9XF57yCORm0mFRqBSf8UHOQo4rDxA-zaBFCm_trAcfRlBpwGWt6qHC1ojf4dtvsU5LAK-lPhFAnuh5Oxg0Oa6d7kDR-B59hmqgCLfvxUBmyaLnczqmUntp4iO5EcucvwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه 1 میلیون توکن رایگان برای مدل‌های زیر
💥
🆓
Gemini 3.8 flash | Muse Spark 1.3 |GLM 5.3 Flash | Deepseek V4 Flash | Deepseek V4 Pro | GPT 5.6 Luna | Gemini 3.1 pro
✅
وارد سایت زیر بشید و ثبت نام کنید و یک کلید دریافت کنید
✅
‼️
نکته :
با هر آیپی ۱ بار میشه ثبت نام کرد اگه میخواید چند اکانت بسازید هربار آیپی هارو تعویض کنید
📌
Base URL :
https://apinex.bond/v1
🔗
لینک سایت
🔗
گرفتن کلید
🔗
دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsTPBh9zubwHOX_BOSXE-HGBMm0uu-3U8FfbY9ZFjGp9PILx4JNi14Jjr4dxQzLGL_2dbZ2kHIV24pwqeH8_l8oEgP5Ty0VlywWZT9lR2REYjWr1_rTW3pE_di0svYB8KGm27geYaVwgZ0JtkseCW7ZQS_HX3x0sm7ue-wABcL20uBXJm1UyNuDE9Kcl1ZUHCA0naqjctMGbzzsTY7CuG-dLrnBuvK4A8i8prriNyzUMXLomwYmPPK93yFnvERiRc0P22ub06XTOKyRxK2S65Qp6Ba8mw_yqjlFnS-NiYg8U810blsJmfjaFl5dHs8u46dixEsLsfex_r-vp1Zbnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 میلیون توکن رایگان 1 ساله
💥
🆓
Fable 5 | Opus 5 | GPT 5.6 Sol | Grok 4.6 | GLM 5.3 | Qwen 3.8 max | Kimi K3 | Deepseek V4 Pro 0813
✅
برید داخل
این سایت
ثبت نام کنید
حالا برید داخل
این بخش
پلن سالانه رو انتخاب کنید و این کد تخفیف رو بزنید :
DEVWEEK
بعد اینکه تخفیف اعمال شد تایید کنید و تمام ، یک api بگیرید و استفاده کنید
✅
📌
Base URL :
https://codecraftapi.com/v1
اکثر مدل های جهان رو داره میتونید از Playground چک کنید ، چون سایت شلوغی هست طول میکشه تا ریکوئست ها جواب بدن
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6sUAcFDtFRG99XrI6KF9gjup4AWs4I9yiZKStduzosCwix1W_U0gBHyZURjAccVDuSu9vyDbq_cZiDGhrfQL8XMCf7gpb2ul0ckglkwddYlTE8KJo-lzeJnOhTrcE0PpFB179GPEELD6joI0uB4QpwG-QcMfmQGGRI3G6HQ5STiAGimLBWEX6r4C81rCV6BKEoNlFkJZSW6H-D6oiHrjKCnPK2GQsU3CIO4865tRoiHIOr1yt8-gmIcRFQ3IbKpGnQA_SQt3H9uKRMHhmlCX4mKUPLi1zQfyZgtmdDlW-IPVZIum1aBsHnUbcFdw5vYIYwZiqYBseM3zsiWE_kphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
با فیلتر شکن کشور مقصد یکم برین تو گوگل بچرخین،
بعد به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید.
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود و ایمیلش میاد
✅
بعدش میتونین به راحتی از antigravity و سرویس های دیگه گوگل استفاده کنین.
از توجهتان ممنونم
🙏
✈️
@ArchiveTell
|
#method</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📌
Model :
gpt-6-astra
📌
Base URL :
https://api.eirouter.ai/openai/v1
sk-e76d452dff7eccef0a1b6bde4f8262c7f628f4f2991676cf3188d0cb68023b3f
sk-778bbaffd07397311260074542e405ab11833bf458e0250363ac1afd7db02297
sk-b028d3f23d96d0b0fc96a24985164437fcaf272276caf33548a664a0df424dc1
sk-1f153c31ccd2448b30c2f56287d5dc8fcc8ddafa579d12a797450321d86e9d29
sk-3334618935b09f67a70938d3379971e3ad350fec1154008d3abbaa07565c00b3
sk-242582ef9fc5e53351eb2fd67178b83033a450a61d048cf66be6aacf98a9e2bc
sk-db726cb7cc5b14160f9d8900455fcd34fd56cbb94f3afac65494a5161eee35b6
sk-7e85fc089be2d58f76c236c8ae1efc6062f68a459bdc9f87bcbe896c2d7307e2
sk-cca857a86f2c62b5d704f2234ed5632f8ef4dfbfcc0da509fe0e021516a0406d
sk-3c3eb497a104328775de0ddb333c7c8d596c20a89e25bbe7e204318f35e2b050
موجودی هر کلید هست 5 دلار ولی نکته اینجاست توی سایت قیمت هر یک میلیون توکن این مدل هست 1 دلار
😁
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=FcOvqe41ugfuAR5Y4IO4GoMDJg1qDiOwNwhmLhkY85Yem18sBkoJd4nhBmLWqu62PtBDRVSBGl6l48XxKatzhSrk6fVSqx2SZuGoeqcBHSAxDoZx6AJ6VTAPwUi3qIs4zd96b6mEpPH-w7Onp0rpoQdQHQMip8gx-ClA5Ng8nq8c5i8KoTwMCMNqaQ21WnSMqKHPzWKMrU6NxybBx5XkP6D6D1aSK8xV0Cg-yl5cAoc5pJnxiaI_FccRDEOEbzwb_dfBMse325qLZ1guXwnKQnwdB5T3frFxDeGRZYR4D4lqfKu8zRyi1GL95sBxaGiCtY9NRJWzTLS58a_dFHTwGrwwL8mOQMKfKzUewzoPKuCqHEnI2kGBE_QObkbDKWbW1WUFTVf3pJnM5Ceo6OUBy7J4zQaaJWgksvr0gRksuMskHCT2Bsbz2-jsw4ynl5qizbcUFwKcYI9jqF_6nmymFseOlFUnV2-yZh9HRcoTMNUzPIfF7-1v8Mr02PMeznv1lmTcur6HsLOaPAIHP70Ksem-uhC3FmzQjs2e0IVwU5T2andUqgW0blDaXlAQ_0utGq2Tn83zSs9FqG3Udktek8Ln9E6gojbnXh4mkXlutKX6UibZOlCF5L_VLezmarKTlKySrf-snb9HlKo_-bHQXeybKjAwZAdX_3enB6ShfgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=FcOvqe41ugfuAR5Y4IO4GoMDJg1qDiOwNwhmLhkY85Yem18sBkoJd4nhBmLWqu62PtBDRVSBGl6l48XxKatzhSrk6fVSqx2SZuGoeqcBHSAxDoZx6AJ6VTAPwUi3qIs4zd96b6mEpPH-w7Onp0rpoQdQHQMip8gx-ClA5Ng8nq8c5i8KoTwMCMNqaQ21WnSMqKHPzWKMrU6NxybBx5XkP6D6D1aSK8xV0Cg-yl5cAoc5pJnxiaI_FccRDEOEbzwb_dfBMse325qLZ1guXwnKQnwdB5T3frFxDeGRZYR4D4lqfKu8zRyi1GL95sBxaGiCtY9NRJWzTLS58a_dFHTwGrwwL8mOQMKfKzUewzoPKuCqHEnI2kGBE_QObkbDKWbW1WUFTVf3pJnM5Ceo6OUBy7J4zQaaJWgksvr0gRksuMskHCT2Bsbz2-jsw4ynl5qizbcUFwKcYI9jqF_6nmymFseOlFUnV2-yZh9HRcoTMNUzPIfF7-1v8Mr02PMeznv1lmTcur6HsLOaPAIHP70Ksem-uhC3FmzQjs2e0IVwU5T2andUqgW0blDaXlAQ_0utGq2Tn83zSs9FqG3Udktek8Ln9E6gojbnXh4mkXlutKX6UibZOlCF5L_VLezmarKTlKySrf-snb9HlKo_-bHQXeybKjAwZAdX_3enB6ShfgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده:
جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch:
کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی خودش اونو به آرت نهایی تبدیل کنه
🎯
ادیت موضعی دقیق:
امکان هایلایت و تغییر دادن فقط یک نقطه خاص از عکس، بدون دست‌خوردن بقیه جزئیات تصویر
💡
نکته دسترسی:
تعدادی تمپلیت آماده هم برای تسریع کار اضافه شده و این مدل در حال حاضر به‌صورت عمومی داره برای تمام کاربران فعال میشه؛ حتماً حسابتون رو چک کنید.
🔗
ورود و تست در وب‌سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭐️
۶ پلتفرم برای تست رایگان GPT-6 Astra
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
1⃣
پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
2⃣
پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
3⃣
ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
4⃣
سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
5⃣
پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
6⃣
سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🧠
شیائومی وارد میدان ایجنت‌ها شد؛ معرفی دستیار همه‌کاره MiMo Desktop!
بچه‌ها شیائومی رسماً وارد قلمرو ایجنت‌های سیستمی شده و یه دستیار دسکتاپی معرفی کرده که مثل ترکیب Codex و قابلیت‌های کنترل کامپیوتر Claude عمل می‌کنه؛ این ابزار خوراک خودکارسازی کارهای روزمره شماست.
🖥
کنترل کامل دسکتاپ و وب:
اجرای خودکار تسک‌ها، کلیک، تایپ، کار با فایل‌ها، پر کردن فرم‌ها و امکان ضبط و اجرای مجدد فعالیت‌ها (Record & Replay)
⚡️
پیش‌نمایش تعاملی و ادیت موضعی:
رندر زنده سایت‌ها، گیم‌ها و داشبوردها با قابلیت هایلایت کردن یک بخش و بازنویسیِ انحصاری همان قسمت
🧠
دسترسی رایگان به مدل‌های نسل بعد:
بهره‌مندی تسترها از دو مدل معرفی‌نشده و پرچم‌دار MiMo-X-Pro-Preview و MiMo-X-Flash-Preview
💾
کشینگ فوق‌سریع تا ۹۹٪:
فناوری بهینه‌سازی توکن برای تغییرات مداوم پروژه‌ها جهت جلوگیری از هزینه‌های اضافی
💡
نحوه ثبت‌نام در نسخه بتا:
ظرفیت بتا کاملاً محدوده و اولویت با کاربران فعال اکوسیستم MiMo Open Platform خواهد بود؛ فرم درخواست رو پر کنید تا لینک دسترسی و مدل‌های جدید زودتر براتون فعال بشه.
🔗
فرم ثبت‌نام در نسخه بتا
🔗
صفحه رسمی معرفی
🔗
صفحه رسمی قابلیت ها
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=SbopOWXkJZYEWoll7A9GFQACbjlBFxrjD0l3Bn7QOzOdEWCAuSHvNkNpkIu6JowmQUUIQOWZBNMYn84oIhd4-2rmUv-9MTP1RHJhrPWtVBbDTC_bpsa6jHg7Med16niyEz1waLbXjuysCeL5m4fisd8bHP5a_vcd5lqePPOH43tni54Znc1u_7CuuVGGrBNETMuE8aneix85w5cm1Y2rk-cGMHmzgmTBp-VRHBt8iURwDvgg8YcY4EFnJUli4-Aldm6N2lGOOh5mrP603QIJjJJUDz6TLTdxEyMp2HmowiQ1m1o2YhxeE6oouC1bKOYfZQLRR-vsgVQnBBRhVDoD1a2c5HIbCGw1PpCL7S0O1E-J1fezEk7hbUyO-y41CY_BpUfmAmMbm8po3SQhxjrrg8m4s09hI6BdwL4mP2wTxBKlPbVLGDif6JFTeGoO3gLw_C81rzNbgYn8gjswdJ9J2I20u57xLEhYQLGyAYxD_GQ1s7GHz80_itZBaJdbW-l2p2_pYJTbo6xwFwjTL-P6xif_XONCKmRG94Gp_tVGcosbvH12ayjYqrW9TjxJxSdJuHnCop9urKAIgGIRjCKzNJVGYBWa2W5SrDtxMHAOhC1E-rgGXMkIduszD0_-8MhfBQj6l94cvKQY-d_CTQ9vFOW8qfjdJBUAkfcXyhRkIvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=SbopOWXkJZYEWoll7A9GFQACbjlBFxrjD0l3Bn7QOzOdEWCAuSHvNkNpkIu6JowmQUUIQOWZBNMYn84oIhd4-2rmUv-9MTP1RHJhrPWtVBbDTC_bpsa6jHg7Med16niyEz1waLbXjuysCeL5m4fisd8bHP5a_vcd5lqePPOH43tni54Znc1u_7CuuVGGrBNETMuE8aneix85w5cm1Y2rk-cGMHmzgmTBp-VRHBt8iURwDvgg8YcY4EFnJUli4-Aldm6N2lGOOh5mrP603QIJjJJUDz6TLTdxEyMp2HmowiQ1m1o2YhxeE6oouC1bKOYfZQLRR-vsgVQnBBRhVDoD1a2c5HIbCGw1PpCL7S0O1E-J1fezEk7hbUyO-y41CY_BpUfmAmMbm8po3SQhxjrrg8m4s09hI6BdwL4mP2wTxBKlPbVLGDif6JFTeGoO3gLw_C81rzNbgYn8gjswdJ9J2I20u57xLEhYQLGyAYxD_GQ1s7GHz80_itZBaJdbW-l2p2_pYJTbo6xwFwjTL-P6xif_XONCKmRG94Gp_tVGcosbvH12ayjYqrW9TjxJxSdJuHnCop9urKAIgGIRjCKzNJVGYBWa2W5SrDtxMHAOhC1E-rgGXMkIduszD0_-8MhfBQj6l94cvKQY-d_CTQ9vFOW8qfjdJBUAkfcXyhRkIvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آرشیو ۱۵۰ پرامپت آماده برای خلق ویدیوهای سینمایی با AI!
بچه‌ها اگه با هوش مصنوعی ویدیو می‌سازید ولی خروجی‌ها تخت و مصنوعی میشن، این کالکشن خفن خوراکتونه. یه دیتابیس آماده از ۱۵۰ پرامپت تست‌شده که دقیقاً دستور زبان کارگردانی و سینمایی رو به مدل تزریق می‌کنه.
🎥
کنترل دقیق نور و دوربین:
پرامپت‌های تخصصی برای مدیریت لنز، زوایای حرکت دوربین، نورپردازی و دکوپاژ
🎞
همراه با نمونه ویدیویی:
هر دستور شامل پیش‌نمایش رندر واقعی است تا قبل از خرج توکن، خروجی کار رو ببینید
🎭
تنوع ژانر و اتمسفر:
پوشش کامل انواع سبک‌ها، سناریوها، اکت کاراکترها و فضاسازی‌های سینمایی
💡
نکته استفاده:
تمام پرامپت‌ها آماده Copy/Paste هستند؛ فقط کافیه کپی‌شون کنید داخل ابزارهایی مثل Runway ،Kling یا Luma و المان‌ها یا کاراکتر مدنظرتون رو با کلمات کلیدی دلخواه جایگزین کنید.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYdOyM4orFNpqokpeXSvILo4Ls1_dDNpdeC9J2WnMO4agrYSCWPj8uxprZyXHVL41hwSzabRNsc9pQzmtRW785_5WWfo0UOmlJCrD4pF84LRhSHuF0NXzpJIwqIZm-QC2-BtmiOrZuut86sydswK72itIC1i008oVT1SY7fW9f5lah97TnyYUNEnYxksOIVOS_shVCN7nM5V8hIf7CePgNGZjR-v6zJ-FvgWUyLigsPcj3Pi3vPZ5vIbfD5BVFxCO4xPK28u1yj5GsYMSgoqpG2kY5WJIBQ2owRIBp48VjJAUwdr7G5aTYKPfr0izCgOegEntURnkCuCP5u4wyChqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مایکروسافت آفیس رسماً مرخص شد؛ معرفی غول اوپن‌سورس GenOffice!
بچه‌ها اگه از خرید لایسنس آفیس یا برنامه‌های سنگین خسته شدید، این پروژه جدید خوراکتونه. یک جایگزین کاملاً رایگان و متن‌باز برای مایکروسافت آفیس که ایجنت‌های هوش مصنوعی رو مستقیماً آورده داخل اسناد، جداول و ارائه‌هاتون.
📝
پکیج کامل و همه‌کاره:
مدیریت بی‌دردسر داکیومنت‌ها، شیت‌های آماری، ساخت اسلاید و کار با PDF بدون نیاز به ابزارهای متفرقه
🤖
ایجنت‌های تحلیل‌گر:
اتصال مستقیم به مدل‌های قدرتمندی مثل DeepSeek ،Claude و Kimi برای تحلیل داده، نگارش متن و تولید محتوا
💻
آزاد و مولتی‌پلتفرم:
پشتیبانی رسمی و نیتیو از مک، ویندوز و لینوکس بدون نیاز به پرداخت حتی یک ریال
💡
نکته جالب توسعه:
جالبه بدونید نسخه اولیه این پروژه رو فقط یک مهندس، توی مدت یک هفته و با سوزوندن ۱۰ هزار دلار توکن هوش مصنوعی جمع کرده! ریپو تازه پابلیک شده و سرعت استقبال ازش وحشتناک بالاست.
🔗
گیت‌هاب GenOffice
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=hCGWAlxlCzFYasgo-K4CM-HtAsiWqZPLwH-rys-QtXr6GytHLnaCch2TErS3oUOVhEjZlyIFb6TtVXAn7mSpIgTBfXVztiXaO5bTeVqHNMbXxNxmJgzFi-NC-A2tbPwUXxyEabKu54RYbBPwDuYzhy04VSxG9s0Z5sCW1W4V20nxSigUzlwStD2KMD3VKikA-XUJ1glj8HZgb8988dJRZRb_NwpfwguxK1OmSvVGarF-mZaBWK5w6IEgqT7SjEFN1IxCxCj5OC-S8w2Qg0VTNqSSqlSFVpHUOIgKhgPhkjndzDk0CtbDZo6PS53Qa3LTU-M1iFdk1Qes6NG0mDTnXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=hCGWAlxlCzFYasgo-K4CM-HtAsiWqZPLwH-rys-QtXr6GytHLnaCch2TErS3oUOVhEjZlyIFb6TtVXAn7mSpIgTBfXVztiXaO5bTeVqHNMbXxNxmJgzFi-NC-A2tbPwUXxyEabKu54RYbBPwDuYzhy04VSxG9s0Z5sCW1W4V20nxSigUzlwStD2KMD3VKikA-XUJ1glj8HZgb8988dJRZRb_NwpfwguxK1OmSvVGarF-mZaBWK5w6IEgqT7SjEFN1IxCxCj5OC-S8w2Qg0VTNqSSqlSFVpHUOIgKhgPhkjndzDk0CtbDZo6PS53Qa3LTU-M1iFdk1Qes6NG0mDTnXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خفن: تبدیل هوش مصنوعی Astra به یک بات بازی‌ساز حرفه‌ای!
🎮
🔥
داستان از این قراره که یه دولوپر، Astra رو طوری شخصی‌سازی کرده که عملاً تبدیل شده به یه ماشین بازی‌سازی. اصلاً هم شوخی یا بازی‌های دوبعدی و پیکسلی دم‌دستی نیست؛ کیفیت کار در حدیه که باورتون نمیشه کل این دموی سه‌بعدی خفن فقط توی
یک ساعت
جمع شده!
👀
⏱
سازوکارش چطوریه؟
🛠
همه‌چیز با یه اسکیل (Skill) جلو میره:
* اول Astra باهاتون گپ می‌زنه و از بین ایده‌هاتون، کانسپت اون بازی رویایی که تو ذهنتونه رو درمیاره.
* بعد طبق همون پلن، توی ده‌ها دور آزمون و خطا پروژه رو قدم‌به‌قدم کدنویسی می‌کنه و می‌سازه.
پرامپت استفاده‌شده برای ساخت این دمو:
📝
Prompt (high effort): /dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
🔗
دموی بازی توی مرورگر
🔗
خود اسکیل Astra
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
