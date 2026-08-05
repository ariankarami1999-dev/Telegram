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
<img src="https://cdn4.telesco.pe/file/PBQ5J4dLAQinJakVu3QQnADS88yhS3m8Fm4J3JdNBy9SyomMoDKqm3mDQlr84zyq01YHmIugcJaXuKJvLLOp29s5jwBNQ8GzZk15R6tpL3SRvCrges2WOX_mv7PC4e10ZcfIqhUi1VcAsh6wahPO6mx2jg8hkWazpoYYMDdducCzgZRiZEvvf3wLgMEyHmbsNi9AzEyLC9-jr2L-sySuDFJplVNsw2xTj2l1yo9nG6sompwNdlq7yrXQ5RqyzX-Jr9ONEYHLb0gMpsZiq-njMDfy6sD9ZcQSp1mAbRX-s5vE957lNseNmW5WLAL52eAJ2Ks-_7J6_iQBEUQMwoUhig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 01:10:54</div>
<hr>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG8CkM1-t15cEo4noiK_O_9DQ8gc96tzWoXQAh--d2jQHfB-YY-jTd4JZLJcsBYOKsidZlheB94VMVv_gyfDMTeUI9PwEdVrd276yPcc0LXgV52sh34OIWjcLPNNNc6xQ_CfAjnyyyxWg_W8hEydpitsRgSKdUSPYoll7S5NzSSlyS8LOjXrl4Epr9qq9JaVoeL5HxaydDGb9NPDdGAFqe5bMcI-YHVT5KYdMxatDI8I_zFF4SATMwsfMwY3TMlIFBOYISb1t5jb07Z8FLqO7AP7bv6Op1WmIPmwLW1UTIdA3Yq06g3LMirzubZwwGVUrglmak7K0itwpFzHqtZoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کامنت یه کاربر زیر پست تلگرام در ایکس:
من آدرس مخفیگاه پاول دروف رو می‌خوام
😕
💯
اکانت رسمی تلگرام:
مخفیگاه رو که نمی‌دونم ولی من رو می‌تونی تو خونه پیش مامانت پیدا کنی!
🙈
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 648 · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsxbmghOvaxzmmxJxcWsfrZmSL7cCgvdEMgwb3AJYLkL8-EF4wNsH2oaRZRDs4VgR3dNBe6xMrZsNRDIxx8iKnJlmC9roROseqN-Gmykt-ClUOXWoXyx18hHo8s65lDp-lV3ktLrPL24Fn6WjIWGFxdqD7xqhM4tKqnpjYnugv4PI5BS1yBrguoGwJImObUFM6jw4lEgPelyjM_lDU4hlXtOBW0fiOR0Xll7zHWhncczlj8-AW_NjLSY6_jCa_Jm0DPEGT6GI8PpB5ph5KIyJ2EestC0BMPE-oLCp-o7-31lmXSO6cm8ZPMv9BJBCr2IwX_R1ZfSHtnik_yXvejEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف فوری واترمارک تصاویر و ویدیوهای Gemini
🚀
🔥
دیگه نگران علامت روی عکس و ویدیوهای جمینای نباش؛ با این ابزار رایگان خیلی راحت حذفش کن
❌
😎
✨
ویژگی‌های کلیدی :
1️⃣
100% لوکال و حفظ کامل حریم خصوصی (بدون ارسال به سرور)
📶
💯
2️⃣
پشتیبانی از عکس و ویدیو با کیفیت های 720p و 1080p
🎞
3️⃣
کاملاً رایگان، سریع و بدون نیاز به نصب
🆓
⛓
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb6GOEWtXJNw-0ji8uZNyW8P9h0k_68XW1RgCjDh-GQIWQTPXTfAhQykrV-EkVfdi94dlPyvdJylZkbQskzLYKjcyNB1XPGV9xBJJrRRK8ic_NGTdGRp6FzPnJlnlyFQOY3YEailmJ3AziauLKQ2K--TmvgIM8fJGi0EhFCRqT918XkHghZVtBUOizU4Ctiy3HJSfybOV_mlZLq6bommx9RGb5YqOP8ZUA1aftVAxFvqhQ34Otzxdhq-OzqWOTI7BUVoYpspB89M8k84N-RGEfJOdczY9ANvtZ-58fk6JhwViS_bm6H57uZbNREKrZDuuWjrehKsUOkE5pYqgdDPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت
Dola
مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت روزانه و رایگان
🔺
کیفیت و قدرت بالا در خلق ویدیو
🔺
استفاده آسان و آنلاین
🔗
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSZUo-DS8XikfuWwXYECp7MsPYRkAtHnDh7hT6wmyN7rUlK6AA1wT8l71cdHcylVHMO8sMeTtX1QzeeZlvmfEcsQiB366VRAdC3pdZ8Cfs8JOoyZuiohL7HBTelhdV2xQ98NeTyXccrQcysrAr3gZpeVC62Cc5qt2iUXkIEFGJZZUo7Ogz2y2IJfeM3HXihSVkeXh1cowYuUjNo8zmLgjsTSx6dBq98mVwzZjia8DLdbrqrVZg-j3a8BLMwSZ2ALyw_0yKc3dv194iImdmm5y_PJoZGgobsbKdPKPwl9o2jtXa5qQqREnrh0kFAe7A4BH_py3s4v0cqxXlOFqZI4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
گنجینه API‌ های رایگان هوش مصنوعی
🆓
یک مرجع کامل برای پیدا کردن API‌ های رایگان مدل‌های زبانی (LLM) بدون جستجوی طولانی
🔍
✨
🗂️
1️⃣
freellm.net
بیش از 424 مدل رایگان از +30 ارائه‌دهنده با اطلاعات کامل شامل محدودیت‌ها
📉
📊
2️⃣
freellm.sh
لیستی ساده و سریع از سرویس‌های رایگان با نمایش وضعیت و محدودیت هر API
⚡️
🚀
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjVCPAwyX-iJ8e4YHMsCV9mRViQ3iPsMWsBgiCKYs1850cKKxydDCdZMs9qSonysrtKPeFXthxNHwInON_-CrcTemRgaseLS5viU--D3v024fQRrnyn15ULRadY4D2jXbQHCPreYoaSUeoxuWplhZCNsQfsauI5zUmH3epkoRjwuhnYIl8VKybpEOc-WOtZ587lerhC2Ui-O9-MkADzZTQL-WI6UkSka45qzzd7oACnkMRb4vVtK16RE5OCu7P8GY1kAnT2JSTP-DsHnWo2jM4BEhdocACXyNPfN-319P93L0dNnaJ4WuCSer7gp81mNsgVa7TIhEwmt5Pi61IodCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای اسپارک (Gemini Spark)؛ دستیار هوشمند و همیشه‌فعال گوگل
♊️
🔍
بچه‌ها گوگل با «جمینای اسپارک» رسماً داره هوش مصنوعی رو از یه چت‌بات ساده به یه «ایجنت عمل‌گرا» تبدیل می‌کنه! این دستیار کارهای روزمره و گردش‌های کاری شما رو به صورت خودکار پیش می‌بره.
✨
قابلیت‌های خفن اسپارک:
📄
اجرای ساختاریافته:
اهداف شما رو در قالب وظیفه (Task)، زمان‌بندی (Schedule) و مهارت (Skill) دسته‌بندی و اجرا می‌کنه (پشتیبانی از اجرای همزمان ۱۵ وظیفه).
🌐
وب‌گردی خودکار:
می‌تونه کنترل کروم رو به دست بگیره و پروسه‌هایی مثل جستجو تو سایت‌ها یا رزرو رو کاملاً خودش انجام بده!
😨
مدیریت ورک‌اسپیس:
خوندن و ویرایش فایل‌های Docs و Sheets، زمان‌بندی تقویم و مدیریت کامل ایمیل‌ها.
💻
کنترل مک از گوشی:
اگه اپلیکیشن جمینای روی مک نصب باشه، می‌تونید از راه دور (با گوشی) فایل‌های سیستمتون رو بررسی کنید.
🤒
شرایط و محدودیت‌های نسخه بتا:
❤️
فقط برای مشترکین پولی (Google AI Pro و Ultra) با اکانت شخصی (بالای ۱۸ سال) فعاله.
🔛
ویژگی Keep Activity اکانت باید روشن باشه.
❗️
فعلاً از زبان فارسی پشتیبانی نمی‌کنه و تو بعضی مناطق (مثل اروپا و بریتانیا) در دسترس نیست.
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvMkKPnEsgEfHfSC7hYaG41DWR3-R1e5JiwsMU7g4PL7fgeccBgDIKkJk7iuptLWKtMllwitwVMyULMgWbUQKvodroO-q3XsimkwTwgIhmBAhV5humzunM-E33nEpD5E47CR89x-wvKzryurDlo_ETwy8POzvoC5Jr7hGGOvXK0IMpP7MLpgEOiPAD618ewAjYRvPDJrkesQnRG490VERQpxmS18xQ0JIoHnvQzIffzlpehsQPBp2eoer-PAincZR8eYUYeSw7rxFWjScYYzCcR26d_4ms6PAFgE25Vt8LtuIi2BcmgGp69R9E8LQw5D9Pw1DRnGj9h__PWZrNoyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی سرور اسپیدتست شخصی با OpenSpeedTest
🚀
🌐
〰️
بچه‌ها اگه سرور/VPS دارید، ادمین شبکه هستید، یا کلاً می‌خواد سرعت واقعی کانفیگ‌ها و سرورهای خودتون رو بدون وابستگی به سایت‌های عمومی تست کنید، ابزار
OpenSpeedTest
دقیقاً همون چیزیه که دنبالشید!
🚀
این پروژه یه ابزار متن‌باز و بی‌نهایت سبکه (حجم اسکریپتش کمتر از ۸ کیلوبایته!) که با جاوا اسکریپت خالص و HTML5 نوشته شده و بدون نیاز به هیچ دیتابیس یا فریم‌ورک سنگینی، سرعت آپلود، دانلود و پینگ رو اندازه می‌گیره.
📶
👩‍💻
👩‍💻
✨
چرا این ابزار خیلی خفنه؟
🔺
اجرا روی همه دستگاه‌ها
✅
🔺
نصب بی‌دردسر
✅
🔺
تست فشار (Stress Test)
🔤
🔺
بدون ردگیری
🔞
💡
کاربردش کجاست؟
برای تست سرعت واقعی ارتباط بین دو تا سرور، عیب‌یابی کندی شبکه وای‌فای خونه (LAN)، یا تست کردن افت سرعت موقع استفاده از تانل‌ها و پروکسی‌ها.
📌
👩‍💻
لینک مخزن گیت‌هاب و آموزش نصب
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔥
یه
پلاگین
به اسم
oh-my-hermes
برای
Hermes Agent
معرفی شده
🏥
این
پلاگین
سعی کرده چند
قابلیت
مختلف رو توی یک جا جمع کنه تا نیاز به نصب چندین
پلاگین
جداگانه
کمتر
بشه
✅
😍
از جمله امکاناتش می‌شه به اینا اشاره کرد:
✔️
هماهنگی کدنویسی و مهارت‌های codemode
✔️
سیستم مصاحبه هدف و پرامپتینگ برای برنامه‌ریزی و مهندسی حلقه (ulw-plan، ulw-goal و Loop Engineering)
✔️
معماری حافظه پیشرفته (شامل Dreaming، Pruning و مدیریت کانتکست)
✔️
سیستم حافظه لایه‌ای (بلندمدت و لایه‌های L0 تا L3)
✔️
متخصص‌های دامنه‌ای و قابلیت‌های تحقیقاتی
⚡️
تنظیمات آماده‌ای هم برای استفاده
سبک و سنگین
داره که می‌شه فیچرها رو
روشن
و
خاموش
کرد
GitHub
🐙
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOyVhRnPQdlI6nthYNrf9gUvEA9vXMRlcQVajtLnbNa9WLSzrfvRn6S63cvJDOaywHUZQQKPPxnGohP5OxyE0fpwqZ4ePuAhcb3M5R0GFDHRHsFWroS29vztVinPjYmPWyxNJO7CsVYQa6DUBPFG8lDshxgjzP2OQLZWJBG6oVAyfSNTvsxhirTBq3j5k5wsL8qQ9xSfS1ao883_KcUr60AbPeTG3TCygiC-fPHM2S_g0zs53Yv8Hx1eCZRETnXF9aXVsXRcqIvjxirvrdRnsVPC-6aTHLXfxRuOPAjnL_VjmrpDemgj52IgkdW_tG1B4amRMsWvULC2A1-Upw93bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱ میلیارد توکن رایگان  تا ۱۲ آگوست
🚀
🆓
پلتفرم
InferX
یک کمپین محدود راه‌اندازی کرده و تا
۱۲ آگوست
امکان استفاده
رایگان
از برخی
مدل‌های هوش مصنوعی
را فراهم کرده است
💥
از جمله مدل‌های این طرح:
😐
DeepSeek V4 Flash
😐
Gemma 4 31B IT FP8
😐
Qwen 3.6 35B A3B FP8
و چند مدل دیگر
😍
طبق پنل سرویس، برخی از این مدل‌ها با هزینه
صفر دلار ($0)
برای ورودی و خروجی قابل استفاده هستند و می‌توانید آن‌ها را از طریق
API
سازگار با
OpenAI
در ابزارهایی مانند
OpenWebUI
،
OpenCode
،
KiloCode
،
Dify
،
Hermes Agent
و سایر پروژه‌ها به کار بگیرید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTMmoPAUEXSdmLvM7LL1buwYTw6V14tRez7pEKiTBVWfBTxawxAHrTx2Ggk55BBhI085tqKopYaPmlU99TAfdmJA5laoNVR5vokZu_B29ZtWf_de3FOpCuLKvXNoRsTdWLwJpU7AiKgtkgzKci4lKG0p_hEqLS2SCPb8dXlwSBIIgnvMLN4I_a7H9NYbUUEmAhgWv7KNCJo7kyMshWesRGvfGBHatWQIBlyzs7kBcQDfbzE_6M58tH_8h002IMUQnNg9K7ZWQYyw-XpPTHKnjxBYAK47IDVmSfl5umwESnzhjvsHfo1TYv2lyIAAbV-ffnwZcxiORsklXeKPLN_FWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی CloudSSH؛ ترمینال قدرتمند Web SSH بر بستر کلادفلر
🎶
📱
پروژه متن‌باز
CloudSSH
یه ابزار Serverless و فوق‌العاده برای اتصال و مدیریت مستقیم سرورها از طریق مرورگره. این پروژه با استفاده از TCP Sockets در Cloudflare Workers، یه تجربه کم‌تاخیر و سریع از اتصال SSH رو ارائه می‌ده!
✨
خلاصه‌ای از ویژگی‌های جذاب:
🔒
کاملاً مستقل و امن:
پیاده‌سازی خالص SSH 2.0 با TypeScript (بدون نیاز به کتابخونه واسط) همراه با رمزنگاری اطلاعاتِ اتصال در مرورگر.
👆
رابط کاربری حرفه‌ای:
ترمینال سریع بر پایه (xterm.js + WebGL) با پشتیبانی از تب‌های همزمان (Multi-tab) و تم‌های متنوع.
📁
مدیریت فایل (SFTP):
رابط گرافیکی کامل برای آپلود، دانلود و مدیریت فایل‌ها با کشیدن و رها کردن (Drag & Drop).
☁️
همگام‌سازی ابری:
پشتیبانی از ورود با اکانت گیت‌هاب (OAuth) برای ذخیره امن کانفیگ سرورها.
🤷‍♂️
دستیار هوش مصنوعی:
پشتیبانی از API مدل‌های OpenAI برای کمک به تحلیل لاگ‌ها و اجرای دستورات لینوکسی (مثل Docker و systemctl).
🐙
لینک مخزن پروژه در گیت‌هاب
🌐
نسخه دموی آنلاین
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pb_GZic7G7b8_3Wr5FAC3Se5ntv0pn-Ps5GS66q8MxzpEWaf17UVRrcGPUlphAC-3l9kS-FkPBriT-wRI1PJ8NuzyLLU3JyACGvPGsl2mhULqgfJCTpqnrpwIlnH__NdWrllDzivYoWgDzqiXGBQz5dKQy-l6pDqEdS09zrAt2mOJ_MI0R-WHtN_zKAyrNyf2yzLpJ3Wzt0pI_dnrrsTZYA0LfsTbMnZppwnOqFkFgOiF3fAM7Hu1p5TLsK7wV69eA1uKV1k2AcwzKICqXpW9kMpZayUCmAc2isUPYdiCws4r9PZMYU-1DpLWpOLlnBhpilWHzlNxDsmpqgo-qXoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=gF2h0O-ruqSoTcNvQ6W4QHN2H7MaRp1STWoIBL00yCHb4iBuKvOEO5IYB72B41d_oTt65pkknUmRBKpqO-GljWS7jHN9r8AZwxo1_BgHwi39eNpElZVPTwGHBehGFBBuoci4Q8MKNJPlmWbdfkl-Y61ONTuR8dQbYKiXA8_GlYwzW95x6cFbGQqQ6gQdLljOuNmmjHCt2Pto6ahRjT61TWznZwB9NE8-HHFXaJ1g6qCuxh5Y1DyEtekla6zPGz2Da1uXE8-nHXg5rUmxP3_5OJCScYUsBBi7lZVloIKW5rUUpsTZMpmxPfWTeu1bMmqSabvDYKoRULvE2AmiIukMVWIpVUiUrujOT6dRWkUz8QeKl8pbekoXqJjxDV0Tljx4EQuJXh-nzlg0xYl8bdB9jG6UYy1d1e-6Pz6whz4QNo7PWXFq0jBh7NzkYZQghwSie9-GX5vNlvbFD_hIlKMwIat-9AnNsHj26hlABmzTXH2MFtvJpAuvZVJQ9b7M75oBde_p-1u-W4IpQFZEwnFNwBG8Nqewfr9Pi6-Zv_97E9v4SFjK_pP9ANG-UZHPJ4tXO_LIYZDpd8hk8sXgArWFse1H5HRZLUtxvUXGc8Darc1ZOIx2azlLdNOYElG1dqSNzvw3s65aa2GGdVWsHCAJw7iAKsOqno2j4CQ0fa0XwRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=gF2h0O-ruqSoTcNvQ6W4QHN2H7MaRp1STWoIBL00yCHb4iBuKvOEO5IYB72B41d_oTt65pkknUmRBKpqO-GljWS7jHN9r8AZwxo1_BgHwi39eNpElZVPTwGHBehGFBBuoci4Q8MKNJPlmWbdfkl-Y61ONTuR8dQbYKiXA8_GlYwzW95x6cFbGQqQ6gQdLljOuNmmjHCt2Pto6ahRjT61TWznZwB9NE8-HHFXaJ1g6qCuxh5Y1DyEtekla6zPGz2Da1uXE8-nHXg5rUmxP3_5OJCScYUsBBi7lZVloIKW5rUUpsTZMpmxPfWTeu1bMmqSabvDYKoRULvE2AmiIukMVWIpVUiUrujOT6dRWkUz8QeKl8pbekoXqJjxDV0Tljx4EQuJXh-nzlg0xYl8bdB9jG6UYy1d1e-6Pz6whz4QNo7PWXFq0jBh7NzkYZQghwSie9-GX5vNlvbFD_hIlKMwIat-9AnNsHj26hlABmzTXH2MFtvJpAuvZVJQ9b7M75oBde_p-1u-W4IpQFZEwnFNwBG8Nqewfr9Pi6-Zv_97E9v4SFjK_pP9ANG-UZHPJ4tXO_LIYZDpd8hk8sXgArWFse1H5HRZLUtxvUXGc8Darc1ZOIx2azlLdNOYElG1dqSNzvw3s65aa2GGdVWsHCAJw7iAKsOqno2j4CQ0fa0XwRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJuySkbAZDv8OHDQaYZJfJbBz5_f61VIFHQuuCCWe2yh-sB3TSQquN6GTwgB_a1XXfhAKF1ltGI3SgpijOfhuJzdKnyp9GQ75yX8dQniUBumBLykrMbfTl7FSDY3UV7a5iWLsRR9giOtS5lYat8mFu7y6pwHeT-UMTiWkrOxiSanbsy4IESedsi0yVHGds1FutvXjqWCG66-qB1-_4Q8Quh_U24KUZSHvNZZXY6h6fOb2p4ZSIwuTzv0mwi0A7ZcRHAXwzcNITrSUXdefeOBvxza71LnszuGpoN5pjq9leKkAcDaATGg6dU-7S1KY0TrOke4QwHYyRqMpyyEt7gtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
500 دلار اعتبار رایگان API برای شما!
‏همین حالا کلید اختصاصی را دریافت کنید و از مدل‌های Opus 5 و Opus 4.8 لذت ببرید:
🚀
Api keys:
sk-2UddB27hnFA1z2LKWKnq6BQaffBLe86FU0htxAHm0Q9n5vjW
Base url:
https://agentrouter.org
Model:
claude-opus-5
|
claude-opus-4-8
✨
کلاینت های مجاز :
🔺
‌Claude Code⁩ | ‌VS Code⁩ | ‌OpenCode⁩ | ‌Hermes⁩ Agent | Qwen Code | Kilo Code | Cline | Roo Code | Open Claw
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jox17-_HStcR4oIiit_MeaI-Ri7IbjJb-FOCs3PD1SscHxaGwKy_KOZ7YYp2FTGGo32KAZT_fETFKKk3vHMYQL-hUcccdmRJRiMFMkhusykujqTfJWYHciOI51ZI_wGdvqVwNf1QNUEI6v2xaUX0TYak1BWfU-DzXTZjDQcwbviZ7gT4eNQvlglqE6zNlEPFuV1W5JaDCLV7znS-bPBsxcZiMrd0MaK1QvgEjNSS6g7shcpKs_5M7vS9DFnsmx-w5cd21MhdgZoq49FIxEi7g4p-5tTJq-jba6EUhrpLZIOFSyq0_sCPCBx8bmIiw5wa61yOK1e-HVxy76B-VQooeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آموزش تبدیل کردن صفحه چت سایت Qwen به API
🚀
اگر در موبایل هستید از
Kiwi Browser
استفاده کنید
‼️
✨
آموزش اجرا :
وارد سایت
chat.qwen.ai
بشید و یک حساب بسازید
در سیستم کلید F12 رو بزنید تا Developer mode واستون باز بشه
در اندروید از سه نقطه بالا سمت راست از منو گزینه Developer tools رو بزنید
وارد تب Application بشید و گزینه Local Storage رو پیدا کنید حالا کنار این گزینه یه مثلث هست بزنید روش و سایت qwen رو انتخاب کنید
یک جدول باز میشه و آخراش یه متغیر هست به نام Token اون فیلد روبروش کپی کنید یا توی کنسول این دستور رو بزنید خودکار کپی میشه
copy(localStorage.getItem('token'))
اینی که کپی کردید در اصل api keys هست ، ممکنه بعد چند روز منقضی بشه و دوباره باید بگیرید ، تمام حالا میتونید توی هر جایی که دوست دارید استفاده کنید
Base url:
https://qwen.aikit.club/v1
Model
:
qwen3.8-max
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU1E8mj_d625OIzkNlDHZ4qcFGPf9MWDBmP5sDXNODTm4suBLQTwmYCqy5PXtMeb2Cg3VJucLV6rvzPaKzTbjbhcYsvBOY-QR-8eD_17xwfTk5V44YyuzcdJH8h-4FJe2fpz4zsCbHG1BKIwbe7HsOz8XnNzSjps9O1a05xHHKb1PjQGtJ1nPObW1afLWRry-vkj_A8frHqwVCzJQDnZ6aLvlDdik1_bPl2ti-ChWoid641eUusr8_vizOboqQRjOwO4_shndoERAWpKovefm2IGA9_YbMCeOGrdgZu-a5z4vqynZMotUh1xWOMof8dRRstIK--s0AZw6Zk7uIvQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩
‏وارد سایت ‌
Cline⁩
بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند
این سایت
‏حالا توی ترمینال، ‌Cline CLI⁩ رو نصب کنید:
‌npm i -g cline⁩
‏با دستور ‌
cline⁩
اجرا و لاگین کنید و لذت ببرید!
💻
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url:
https://www.fastaitoken.com/v1
Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471
Model: claude-opus-5
Model: claude-fable-5
دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro
همچنین دارای چند مدل رایگان
:
GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3
به
این سایت
برید یک حساب بسازید و با تلگرام وریفای کنید و لذت ببرید
✨
قابل استفاده در
Vega Agent
✅
📍
Base url:
https://anymodel.org/v1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqhvtAl4aJx9e-JwGmJTt067jblDX8l5jmIM2pV3F8XESjF0xY4NYSt0eORZlWPVasWQG24KnPGQkCDnyW8OTjTKcm7H-Wsweo11t-xEIahlfgr2uNpd3XtQhnbklg557tMkfXGv_aXaqijyeU5jiaASxsq8T50D0F8Nw5Q1Ev-QaU4z83C6G9ZxI2pRiwX80g3D1mcveLmyP6s_xIFd5wQGAmfgPyhYHnTeztHK4WCC3EjqoJ_zOtA0W-sySj2SIsjSAvDxuPbihV6UMU04Xdk2zH8P5RizT6eOiegsFpDE2nOiFDPeNnvCKPAWu-lfJ9MlotxPgX_DbkOcOcRjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏100 کریدیت روزانه برای حرفه‌ای‌ترین مدل‌های ساخت عکس و ویدیو!
🎨
🎥
‏بدون دردسر و کاملاً رایگان؛ فقط کافیه وارد سایت بشی و با کلیک روی پروفایل بالا سمت راست، اکانت خودت رو بسازی و از قابلیت‌های بی‌نظیرش استفاده کنی.
📧
✨
🔗
‌
https://www.creen.ai
⁩
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szqhsmqcpoMVlOb8DU-T3RWgc-y6-xYIVcRCZUTN2aqem3RS37DVJA6Qr1r0_0g6J_UycTXz0DN5ci-T7MRf576TZEPO3w3TOpEjMmR9W_rose4IDqP7FLk8yVtWUF5T7ChZOSplzO6q0rPg_WbATHJsjyn8-0761eiFFlCr7NHdU4a_YExM4Ur3WfKvqbNLFUoaTS-jKAnoQGXfQYb5WMbKS0GMvf_P7r890H2vLM8EEKSJLmXDrdH6lBWnqbd9mhQrgjy8I_sB-94ptv6KZBQcgMenb8WRZRLALyQxGUfoD5HPLjkLC8JzrrOSquWevlEgk1truntDLAZS2GuROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آیپی تمیز کلودفلر
92.53.191.134
66.225.252.96
104.18.14.224
104.25.247.228
104.17.2.54
176.124.223.242
104.16.122.178
188.244.122.16
104.20.14.15
185.148.104.192
104.24.152.74
104.18.2.152
104.27.24.70
154.211.8.196
104.17.88.93
74.49.214.92
195.85.23.208
172.67.114.81
92.53.188.13
104.18.198.203
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMewFQaY0jQb0zKe_TUMgIL8UBPmV7IHK_8MtepEpmpFJfV-5O_i1GRKV9gMPy1h_t3a1J-2z1VTGu1rvVFTzmTSTLIXW2EOEFwZUa3A5kbKVdw8vKS6lt-rjv6Krtq9Q8CYXwxWaNqF1izkhbaCqM8jqenvfaUcvbYSwZG4wZbugMdRyTrfFO8Qk6sL4S_3MaR_pF8rTeWXiz-4YWncLv_AqEeTlSMmMNtSm4EHDSPmt3Zk05Da4qWixXCKlixE2mr7kkkHRlSlzAVfU76tN3YtHYQhHmJcwXeAM4OuWn7NYd5qQ25AUhplWaLyjgO5Wgy9gr0ldBPmW3LWl8ocjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تولید محتوای بصری بدون محدودیت!
‏دیگر نگران محدودیت‌های اعتباری یا کارت‌های بانکی نباشید. با این ابزار قدرتمند، می‌توانید بی‌نهایت عکس باکیفیت و ویدیوهای ۵ ثانیه‌ای جذاب خلق کنید.
🎨
‏
🔺
تولید نامحدود ویدیوهای ۵ ثانیه‌ای
‏
🔺
خروجی عکس با کیفیت بالا
‏
🔺
بدون نیاز به کارت بانکی و پرداخت
‏
🔺
رابط کاربری ساده و بدون محدودیت‌
🔗
https://zsky.ai/create
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLFbBzgZxejATE-VFiUod06LwAUY8aLgK2A7ZMv01qaMuXCLcSHVTsS8B_frEbsCOyhzLlo8cS_tCAfc5zvVV_wJgH47lMiwGI6-bw7nipQCHdOZh6FsuKl4H2Y71dOGIyNQ2X9Uwopw2dgTnram3R0sj6W60oaEZFbmN5wjmPXHveR0oFxHMqfo5BSsf5_2SCMYLkGqeZMhDjAbG4ZAw4ZZMXr6TK1Z2PffH6D2Sn7m3j-yhxyhjXvKnmGP_NeWdKBFabW7Bhqb3hYdr5Kx-zyaogLslBbANwgfVDItSmcK5L5xZi32LpbuEPgF1kbED1U3s43VzWldG1sWlXdZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
200 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 5 | Sonnet 5 | Deepseek 4 flash 0731 | Grok 4.5 | GLM 5.2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://seekai.cc/v1
قابل استفاده در
Vega Agent
☑️
از این
بخش
هر روز 20 دلار بگیرید
☑️
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
200 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wf2fep8E0NCT3KgXhszigNo8hf0q2U_1Cw27J9OEiakHsfeGGJykZ9TjsLvkw6WGoE0Oh9Kp_vUZEbCUbVJ8kPnwofc1m88EMO_oRrMsAmSJqncun_YQMF2ulzA0j-eMeTDm7MfGqJUXTFUtUIckpGphotc9UXMVF7vLjpttigJ9aB0XxqZy8qzjl9UhCY16rKNphtBs9KtJkzjebkV6t5Kh8NxSy08rTS0UYuIS-OjUswdrYDcm-aJ96ZeOgCzsUdk4Bd-bH4dld-rtoWPnTnx0ySqPZtAnGKqQg6nTZy5FOJoPj1oq1CJ36dN8eFHyUCxLf_yHtginj3hcGgxidQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pf1mdruHRogvVhNqKBN2Lhd9ZZ0qfybQMVZIno9YQ9N7q2Hb-PRJsnAGlCabFwmoct90ZNhzL8qpy9GBrd4FAGtwJgjf19CyazjJrK-PkPoDYH7P8HoPkyOj40dHGQZD7e2He5DCouc58suZVmmRo3RZqSzcFVW9LJvxj7PMjLfycPUH-zEnlq_LtWrjjfcYROmA8CdU8GbIS5Nq8DnUYYwh_haeyMfqwlorIgiC3oWLOB86gEA53D7O90UhQqhEdGhxFKzy93yl1nVuPvz70l3iVwaB_otwoQTmVS4HUJ3UKXtDE1nnFHrUH0kYDAY1qhn2-TLdTaVpTBRn9KWZVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی رایگان به مدل قدرتمند ‌Qwen 3.8 max
🚀
‏اگر برای پروژه‌هایتان به یک ‌API⁩ پرسرعت و رایگان نیاز دارید، همین حالا دست‌به‌کار شوید:
‏
1⃣
در این
سایت
با جیمیل ثبت‌نام کنید
2⃣
‏ از این
بخش
با اکانت تلگرام وریفای کنید
3⃣
‏ دریافت ‌API Key⁩s
📍
‌Base URL⁩:
https://api.aigate.shop/v1
‏
⚠️
توجه:
این دسترسی فقط تا ساعت ۲۱:۳۰ امروز فعال است.
⏳
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cp0uixWaOk275xEWioSgjoKVlVwzy2U0jkIhXZ6iNrDltP8R7QbqL_aHop3P7SDr8l44JoBqTYYWWHPrZvjPNhggdryd37NdLN0TZxbNm5NClZdi5jyhWjLxJj3VSPPcJMRqUlFyg6WHzjZ6j4SSbGCwxLTJHcpGJl8i3ckdeuo_JNTkjf_MKFepS46OeseEi8bN0Y5VXUwoADLttNqjooYtA-jibvY8400bIQQhGAeOcI5ByVOprCMK3WU1kVHR2Vez2C7eCuJKuAYDGYCkVF1m3SRB3gfT4ckssO-kHuoB33P2nmRJgTlRE-VEy9bbbL8GAbBuFBhytTKRnuSn7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
30 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 4.8 | Sonnet 5 | Gemini 3.1 pro | Grok 4 | Nano banana 2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب ( قدمت حداقل 14 روز ) داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://routllm.pro/v1
قابل استفاده در
Vega Agent
☑️
🎁
با هر رفرال شما
5 دلار
و شخص دریافت کننده
30 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=rCTCTNroSp8WrWCItmCUo8hjMjTspXk7kth1qN82b4Il1JTADo06dqRsgbVw-WYTUu7idhk9TXKZgzN4yegU3LMIZRdVbo745nC9yAYF6zPC21JCF_JxsLpTKltoQEOYkk9WrHtsn7odbT2h3xlbpkL788_caFOPWcnh-V8xcev0uGrzzLiEZ5eYMjXDXDrg_Jx_9KVg9k3CfR-GABcDlsSTlVXFxgub0ymDKxEWldh9g-VEXtBe1sz5qjy444PFrap1zKeq5xLUfYF-ntCYv6T1et4R4Mpces2rWayeESd9um4q0bR452MEk5t61fdRzhHthTfa4MDnqaEwwktMUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=rCTCTNroSp8WrWCItmCUo8hjMjTspXk7kth1qN82b4Il1JTADo06dqRsgbVw-WYTUu7idhk9TXKZgzN4yegU3LMIZRdVbo745nC9yAYF6zPC21JCF_JxsLpTKltoQEOYkk9WrHtsn7odbT2h3xlbpkL788_caFOPWcnh-V8xcev0uGrzzLiEZ5eYMjXDXDrg_Jx_9KVg9k3CfR-GABcDlsSTlVXFxgub0ymDKxEWldh9g-VEXtBe1sz5qjy444PFrap1zKeq5xLUfYF-ntCYv6T1et4R4Mpces2rWayeESd9um4q0bR452MEk5t61fdRzhHthTfa4MDnqaEwwktMUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
تبدیل هوشمند وب‌سایت به پرامپتِ حرفه‌ای!
🚀
‏دیگه لازم نیست با کپی کردنِ تبلیغات و بخش‌های اضافیِ سایت، وقتِ هوش مصنوعی رو بگیری. این افزونه، محتوای هر صفحه رو به یک متنِ تمیز و استانداردِ ‌Markdown⁩ تبدیل می‌کنه تا دقیق‌ترین پاسخ‌ها رو از ‌ChatGPT⁩، ‌Claude⁩ و ‌Gemini⁩ بگیری.
⚡️
‏
🔹
حذفِ آنیِ تبلیغات و المان‌های غیرضروری
‏
🔹
تبدیلِ ساختاریافته به فرمتِ ‌Markdown⁩
‏
🔹
سازگاریِ کامل با تمامیِ مدل‌های هوش مصنوعی
‏
🔹
افزایشِ چشمگیرِ دقت و کیفیتِ تحلیلِ داده‌ها
🔗
GitHub
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NekoBoxPlus-1.4.2-83-arm64-v8a.apk</div>
  <div class="tg-doc-extra">42.2 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📦
پروفایل پشتیبان NekoBox+
با توجه به
شرایط فعلی
،
اختلالات پیش‌آمده و قطعی بسیاری از کانفیگ‌ها و VPNها،
با این روش می‌توانید به
مجموعه‌ای
از
کانفیگ‌ها
با
پروتکل‌های
مختلف دسترسی داشته باشید و در صورت
قطعی
، گزینه‌های دیگری برای
اتصال
در اختیار داشته باشید
☑️
🔹
روش استفاده:
1️⃣
ابتدا برنامه
NekoBox+
را نصب کنید
2️⃣
فایل
JSON
را دانلود کرده و
Save
کنید
3️⃣
وارد
NekoBox+
شوید و از منوی
☰
به مسیر
Tools → Backup → Import File
بروید
4️⃣
فایل
JSON
را انتخاب کنید
✅
تمام
.
تنظیمات
و
پروفایل‌ها
به‌صورت
خودکار
به برنامه اضافه می‌شوند و می‌توانید از
کانفیگ‌های
موجود استفاده کنید
📌
این پروفایل شامل ۱۴۰ اشتراک و گروه با کانفیگ‌های متنوع است
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=uh5LzE9Z5NqWFCixZMl7v6snPybzLS6CXfdsXYjhDbdvuSv9GK_cMrcp1LWp5I5_K6hwm3ntBOEnXOuH_4YP1QUFxOb6VH6ChrS71nDSnZH4kzpZTYLmeN1OGX8CPlEYW1zonmD5L-Z__uI2n6gYp9Kuqf5WoXxq-CXWsWVqPB_kXcmd0rPWKoUBee_YU1It8FJDCu2kdETFztIkSWWy-d8z3fqjFGHxYFOxBu9zRuIl-4sGOFlx7dM0Z7NV1FtWbRq108iKm4gYsFiRzJ1Ez_3bgnj7KPmhxJk5Ado3iOtliS2Jh-p-4w25j5N7p8uVTIPXmLneH1RvRNJPZt995g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=uh5LzE9Z5NqWFCixZMl7v6snPybzLS6CXfdsXYjhDbdvuSv9GK_cMrcp1LWp5I5_K6hwm3ntBOEnXOuH_4YP1QUFxOb6VH6ChrS71nDSnZH4kzpZTYLmeN1OGX8CPlEYW1zonmD5L-Z__uI2n6gYp9Kuqf5WoXxq-CXWsWVqPB_kXcmd0rPWKoUBee_YU1It8FJDCu2kdETFztIkSWWy-d8z3fqjFGHxYFOxBu9zRuIl-4sGOFlx7dM0Z7NV1FtWbRq108iKm4gYsFiRzJ1Ez_3bgnj7KPmhxJk5Ado3iOtliS2Jh-p-4w25j5N7p8uVTIPXmLneH1RvRNJPZt995g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
کپی‌برداری از پروژه‌های گیت‌هاب با قدرت هوش مصنوعی!
🚀
‏تا حالا شده بخوای یه پروژه خفن رو از گیت‌هاب درک کنی یا مشابهش رو بسازی، ولی غرق در پیچیدگی کدها بشی؟ این ابزار جدید، کل ساختار مخزن رو به یک «پروپوزالِ اجرایی» تبدیل می‌کنه تا بتونی با کمک هوش مصنوعی، اون رو بازسازی یا تحلیل کنی.
🤖
💡
‏
🔹
آنالیز هوشمند:
بررسی دقیق ساختار و معماری کلی پروژه.
‏
🔹
مهندسی معکوس:
استخراج منطق اصلی و اجزای حیاتی کد.
‏
🔹
تولید پرامپت دقیق:
ساخت دستورالعمل‌های گام‌به‌گام برای بازتولید عملکرد پروژه.
‏
🔹
شتاب‌دهنده توسعه:
ایده‌آل برای یادگیری سریع، پروتوتایپینگ و درک پروژه‌های سنگین.
🔗
https://www.gitreverse.com
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ربات تکه‌تکه کردن و آپلود فایل‌های حجیم در تلگرام (بدون دیتابیس!)
🤖
📦
یه سورس
ربات تلگرامی
فوق‌العاده جالب و خلاقانه براتون آوردم که روی بستر کلادفلر ورکرز (Cloudflare Workers) اجرا می‌شه و وظیفه‌اش اینه که فایل‌های حجیم رو از طریق لینک مستقیم بگیره، به پارت‌های کوچیک‌تر تقسیم کنه و بفرسته تو چت تلگرام!
✨
ویژگی شاهکار این سورس:
این ربات کاملاً Stateless (بدون حالت) طراحی شده؛ یعنی برای کار کردن به
هیچ دیتابیس، KV یا فضای ذخیره‌سازی ابری
نیاز نداره!
🤯
شاید بپرسید پس چطوری می‌فهمه تا کجای فایل رو آپلود کرده؟ ربات خیلی هوشمندانه تمام اطلاعات (مثل آفست بایت‌های آپلودشده) رو توی خود متن پیام‌ها و دکمه‌های شیشه‌ای تلگرام (مقدار
callback_data
) ذخیره می‌کنه و از خود تلگرام به عنوان دیتابیسش استفاده می‌کنه!
🔹
قابلیت‌های اصلی:
*   تقسیم خودکار فایل‌ها به پارت‌های ۴۸ مگابایتی (برای رد کردن محدودیت ۵۰ مگابایتی آپلود ربات‌های تلگرام).
*   امکان ادامه فرآیند آپلود در صورت خطا یا قطعی (کافیه دوباره روی دکمه همون پارت کلیک کنید تا فقط همون تیکه دوباره دانلود و آپلود بشه).
*   بدون نیاز به سرور یا هاست (قابل اجرای کاملاً رایگان روی کلادفلر ورکرز).
*   اعتبارسنجی خودکار لینک و حجم فایل در هر بار کلیک کاربر.
سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJrjTlF3FaZvTcnURXsWZ_HslJbdGM8AGah6sFV8lnzZUQRLHLK_YMPcB1l4yMMIwkU8JapECb49xy6MNBce8rnxHDKIdUY99UBoV1Qt9bvPFPqXo0gP_HG52fPYU8XNE9JmrvmUKEpWBqb8DLU5Iu8YT0pILOy7clg3MsCYrF1oEiy9cYzXn3e7iX8exU-LIao8T5W5yhQw2BZZKXRzd4uFZ1r9u--VbH0eGFfuJldT1t6qvSGE4ejcrh6fDSz0UfNoIVPSUhOLnPO899_5co5MSR__Q5VFpFC2XofNpyDFM6sBm1YBt5pBGmOIUsAuDBzzVfLzVEPLExJhhzIxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=IvNsN766ZUZECGtiGG1gUZfvvc9pvZ2uJs9vxhRFrqHZorlYtVx3EmN21n6ZoT0HBc9aKS1jXhDbkHhHWmfR5Ezk1rTuIcALEZo2PxKYZkN07EcGnp8HPsIMmxUwecByddoBam9sq05BKH-jGMpy_5qG-xeLtis5iq-J6B4rDARfj1L-JpYUlhKTlbfyZQvOyoO2wayWIM8FYBKb3dwkXpNwm4NstpSwCDhrvDfbguK3EqUz2Sz1-oRk3Ehtq6ygiSbUvzOe-HRi9uFdla_XzOfKHCBJnq6bc7OSVJZaWVWf-pJBIDeGA2ib3WiUAuO53e2ZKZKhQ9yXov0gd9Q6DSuSyngAgoZhacYPbaG5Ph9Ht_Q8CSjNbVYLQhTXQac_VPcAHFhQNAphjQxOgCGaaRKw0hq1_VAh00DM-q1uyNnVT73JAz8cBW46FgD7yl5RHlNLSS5zJtO69J1AU0A5eUC6_76-eOvMvrDQIVPiVqbRNujTzeafK5jJO7aAt5wmwC-E9zCu4g6jkdbyzsrEY8US5DUJ5rg2IkU24JJpxi4r_H04-Ajx_fmsymPaMPW3oaJOGEGWOcgdpepwgMTEmtUJz6ctkUdtLfurPeRnpSGeGete7qrExIN5Uq4cirDYfRUvGU352VKCfoZgO4pp_nSxtmb95wEHiOkIEVBua74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=IvNsN766ZUZECGtiGG1gUZfvvc9pvZ2uJs9vxhRFrqHZorlYtVx3EmN21n6ZoT0HBc9aKS1jXhDbkHhHWmfR5Ezk1rTuIcALEZo2PxKYZkN07EcGnp8HPsIMmxUwecByddoBam9sq05BKH-jGMpy_5qG-xeLtis5iq-J6B4rDARfj1L-JpYUlhKTlbfyZQvOyoO2wayWIM8FYBKb3dwkXpNwm4NstpSwCDhrvDfbguK3EqUz2Sz1-oRk3Ehtq6ygiSbUvzOe-HRi9uFdla_XzOfKHCBJnq6bc7OSVJZaWVWf-pJBIDeGA2ib3WiUAuO53e2ZKZKhQ9yXov0gd9Q6DSuSyngAgoZhacYPbaG5Ph9Ht_Q8CSjNbVYLQhTXQac_VPcAHFhQNAphjQxOgCGaaRKw0hq1_VAh00DM-q1uyNnVT73JAz8cBW46FgD7yl5RHlNLSS5zJtO69J1AU0A5eUC6_76-eOvMvrDQIVPiVqbRNujTzeafK5jJO7aAt5wmwC-E9zCu4g6jkdbyzsrEY8US5DUJ5rg2IkU24JJpxi4r_H04-Ajx_fmsymPaMPW3oaJOGEGWOcgdpepwgMTEmtUJz6ctkUdtLfurPeRnpSGeGete7qrExIN5Uq4cirDYfRUvGU352VKCfoZgO4pp_nSxtmb95wEHiOkIEVBua74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window $🪟.npvt</div>
  <div class="tg-doc-extra">3.6 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7367" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرعتش از اون یکی کمتره اما بستگی به موقعیت مکانیتون داره از بخش configs پینگ نگیرید.
🇰🇿
-
🇫🇷
-
🇩🇪
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window🪟.npvt</div>
  <div class="tg-doc-extra">4 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر vpn ای که داشتید یکم ضعیف شده و الان به زور وصل شدید
این سرور موقتی میتونید استفاده بکنید تا استیبل شدن سرورای خودتون
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVgK4UPlbnRT1TYhLMmEGtBJpWSxitABI8FK_qJoutkaZxvkC7M_5iam5_s7_nqyhHl1no2BMLSE79IDmeO7NvwLrS1oK9XCGu_Lcr1l_ktXpskEz8Zi7Vr5dY6upc1mAAkcHJFzjgfSG_cgE8brokqmsDZVbFVChBFJF5VFl2i2wH6eGEm7kbcYEC_shtHmshLEaimlnb98rBh72_nwJiLgz6TjUxIJfOFYEJj8hobmMizwYZ2yuLyaJn3jBN7mYZxNokaEGqLEdpjGHXp1LBIrzj5-uIjJeb6OyUqQYilFQquYzKn64C8icy-m50_eyFR0VE-Y-ypuVP7EGzvR7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏
فرار از زندان برای ‌Gemini 3.5 Flash Lite⁩
🔓
‏
⚠️
نکته:
حتماً با جیمیل فیک تست کنید، خطر مسدود شدن اکانت وجود داره.
‏
برای دریافت پرامپت کلیک کنید
✅
🔗
لینک گفتگو جیلبریک شده
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZhvfiOQXktHry1Y0QesQnAUT8nMBf5vdSKMX1h6dDoW_rDJTSGhYMkquDa2rGLZku0bwzX8Ut8YvNPoMbjSvxvqP3B1SiAAYInwdsLuD9c024DTh7MluhIH1wmKuvOftC-05AigRFC4QwffEscqImQl--5Rs7dMz8PL4BhUilqvKNlBdWnG8gghs0peHyZAHSs8qljs3hvgsq07OZIA6624Q4cznmy-7gjlIOSkywUC8vpk8lVAbcZ62L5S7KIel-cPWceSBSTAUWKmtzf8ZgGjIGFsxgXvZAdacom5A-p5z-V7aofWJg8QF-RDUMCKPCjYiSd88YWIYHdjey3pyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوبِ بدون تبلیغ و ردیابی با Invidious
📺
🚀
اگه دنبال یه جایگزین خفن و سبک برای یوتیوب هستید که نه تبلیغات رو اعصاب داشته باشه و نه گوگل بتونه رفتارتون رو ردیابی کنه،
Invidious
خوراکتونه!
🔹
پخش ویدیو تو پس‌زمینه (حالت فقط صدا)، امکان سابسکرایب کانال‌ها بدون نیاز به اکانت جیمیل، و محیط فوق‌العاده سبک.
✅
اصلاً نیازی به نصب اپلیکیشن نداره! فقط کافیه برید تو سایت
invidious.io
و یکی از سرورهای عمومی رو انتخاب کنید تا مستقیم به دیتابیس یوتیوب وصل بشید.
📌
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8jPQiKp4NGjzEimG49_te91X-_0caMJNn8vVQc--JVqvtuH5tdDO8Vnx0Errt1KTAT7iN5J5inV0Jau_ZRDFy17XyPjGMlh1u1xwqYhUQReIkNdcYAKCRl1ywhIz21ykAXG_Trk8ae3Zx5t4CIbBw2saqd9ozDYloRFbaRtu__ErqrutIjsdla33rkRgq1tAmLZO_2elodMu2qGLQ-EQqUxE8uWukGDJFpcOZLaQzX_APYWxZSo2oKUbcgg0tq3tV8igwrDjVZZlSk3PRGvbhKu5A-kRpxHl5HzWz_WhbsPW0f_uxtqaV3nT8JQ6DulQWN8bJouaQgZtktZtQAtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها: •
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه •
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان •
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب •
📝
فقط پرامپت بنویسید…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWyioj6N12tfIXUP7zb19psvY5doR2ny9UaQuWfqosJtKlVPTrCOOkFA9e0mt6CKA0pycphaIDT1drPDxzE3o8sbrn448rud8aipa92MohTR50byV0E8UWQb8Ii2CmlMrY1-zltLocry_Qw5jKjCCTjvxPmnzQ5Xq2Vc-q3ZvFSVJSZ37I1JMqEIR2GWOhRsyZIuytyNUYFNv3kVhRD3lk3GAserchnft-5IiZF3kK0TqZSE6FlYaisxEeJleZrYkMmIXd4sPC2S0o9PsO9C6pxMlsAnQ2ny3rrdZC6ZHmd3nZjwjjGKXgTPwi9gCbzhgo4r59G9xVIXRFjkee_D-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پز نیست
سبک زندگیمه
🗿
جهت دریافت کانفیگ پرسرعت بر بستر کلودفلر عدد ۱ رو کامنت کنین
😎
😂
(شوخی)
متوجه مشکل آپلود شدم و کلی چیزای دیگ
ایشالا رونمایی میشه فردا بصورت کاملا رایگان</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVsskMMzVbCG0oJPZlj00WcTenVLsUy36JQQOAVbcQlMRgwDMA-Z4NjcQ7af0rKx9w3QvDGuEKjzItdtaKzKdUpOcpQ56m3N11V-TZZMqmEwy6ZQoFnkdCPWnK0GDx8JnD4b7RH29ItlbECkp23upw1QdwbkWEbWh6tr4R1qyvaUV554eWX2FL5t3Flxk06iaez8lEqm90yQJr_yIcuDT2tju6A_TIFnhI8QDERfOtVNPfTKYILL-uTlkAj3aWnB3iIEUQF_0jdIW9bE821QnhH3Kn1j5zW5n69MoaBgt1RVB0CfQv8NriiHmZaaJZwWiDnrCAVyvOtE3HyxQGtRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
فرصت طلایی: ساخت ویدیو با هوش مصنوعی گوگل
🔥
‏گوگل تا تاریخ ۱۴ مرداد ۱۴۰۵، امکان ساخت ۱۰ ویدیو با کیفیت بالا رو برای همه فراهم کرده
🎥
‏
✨
ویژگی‌های کلیدی:
‏
🔹
تولید هوشمند:
تبدیل متن به ویدیو در چند ثانیه.
‏
🔹
ویرایش منعطف:
امکان تغییر و اصلاح ویدیوهای ساخته‌شده.
‏
🔹
قابلیت ‌Remix⁩:
بازسازی و تغییر سبک ویدیوهای موجود.
‏
🔹
رابط کاربری ساده:
دسترسی راحت از طریق منوی ‌Tools⁩ در ‌Gemini⁩.
‏
⏳
زمان محدود:
فقط تا ۴ آگوست ۲۰۲۶ (۱۴ مرداد) فرصت دارید از این قابلیت استفاده کنید.
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4anSbuVrdsiJrYUphudFA23lHQA0H96vZ7cpnnenn7dSAMA8DTqxj4y_xt4_mRXi0RLDUGuKYcfDX4nUVB1sx845XkjQ2L8AS0_EZG-OjZ5ckLM6O72tvFIrOFuLVM0Y31-yiEjXC3SPIF3WI3eSQfcDQ77zLV0zGbzM7tq9m4Fjy1l3aEm1csk-r3r1QR-eBd0AaTxsNkucergNVldjGgPWJbeWY2zR_ypV-_JzkYMkFcnVH-o5idZPdROsPPb6lcHkr6FBkzKDJwKLDiwLRK7zwQuVIWPnKSVQh-wSGt3Vf_yoC6cZPd4vjjN6383sw5kyddGFNZGj9cySOh_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API مدل Deepseek 4 flash 0731 به صورت رایگان
🚀
وارد این
سایت
بشید و یک حساب بسازید سپس به این
بخش
بروید و یک کلید بسازید
✨
محدودیت:
هر ۵ ساعت ۵۰۰ ریکوئست
‼️
قابل استفاده در
Vega Agent
☑️
Base url:
https://api.p0.systems/api/agents/v1
Model:
deepseek-v4-flash-073
1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oe3-_yQpC6KOCef2UEJrXCP7KBV-VeYIQLiP72wtgRigSEb6qDnc_giQwuCtRnocz2RntyIMMEUoPdEH6Rnn-zOoz083YQGgbdRr299Qv53ZZxcB4_hKVVclEd33qYeDh_Pyll4cdrjqNROLsaTrc4BygrcCBrcBZtxbr5cMRCVlHE7MgNUoAgUHYvXfAl8JRGXWzPyttLt8hHDvnsVxbQ0gp94vzq7-pwtcSb0QRX-m8gNZuLc4xjyNNZrHL6PAs_VrXp2YAhQ3RRd3zF1JfpqCvQZPsqdM21AejsWRabffPWvcJtuxLlnXCMT8hy-T3TROnyfijiseYjHHzdLVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر خودکار و مداوم IP در لینوکس با IP Changer
🔄
🛡️
اگه برای کارهایی مثل تست نفوذ، دور زدن محدودیت‌ها یا وب‌اسکریپینگ (Web Scraping) نیاز دارید که آی‌پی شما به‌صورت خودکار و مداوم عوض بشه، پروژه متن‌باز
ip-changer
ابزار فوق‌العاده کاربردی و ساده‌ای برای لینوکسه.
✨
ویژگی‌های این ابزار:
🔹
تغییر خودکار آی‌پی:
تو بازه‌های زمانی که خودتون براش مشخص می‌کنید، IP سیستم رو از طریق شبکه امن Tor تغییر می‌ده (Rotate می‌کنه).
🔹
سازگاری بالا:
روی اکثر توزیع‌های معروف لینوکس (مثل کالی لینوکس، اوبونتو، آرچ، دبیان، فدورا و پاروت) به‌خوبی کار می‌کنه.
🔹
دو حالت اجرا:
می‌تونید بدون نصب و فقط با اجرای اسکریپت ازش استفاده کنید، یا اینکه با نصبش (توسط فایل setup) اون رو تبدیل به یه سرویس پس‌زمینه کنید تا همیشه فعال باشه.
⚠️
نکات مهم:
* برای اجرای این اسکریپت باید پکیج‌های
tor
،
curl
،
xxd
و
fq
روی سیستم نصب باشن.
* از اونجایی که ترافیک از شبکه Tor عبور می‌کنه، ممکنه سرعت اینترنت کمی افت کنه و بعضی سایت‌ها آی‌پی‌های خروجی تور رو مسدود کرده باشن.
📌
لینک مخزن گیت‌هاب و آموزش نصب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajo5lIUDTwRj_sa5dBK3r7DcNWMvnUf3L9DUQ9yNdgrBJXwoYb4UoEdR_gvSblXvzgL-a5HWYRMSLKblshvXyW0FcL2AbTzYqVuOfulyC3kYLvLNrykYZf_1gMAOAMo0sU2oS8aeGwOAWoExfU7uURWk2WSGC0DO8icNGTF7G-56EJlmK9YmNRtJz-DMZS-_k3dvFYkiZDVx02jixkbkjCZdUuheYVNqNIc1udcYKkqR6JStSlUTz-N3N2VfhA0ZjdB3NkRTYoZWDtoAP5bA4u1pOn2sEco3xkU86WIIItHQok9DdYh57LXszM3X9R6-xPfrkenaR6GmUOROn-Ed3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Deepseek 4 flash تا 12 آگوست رایگان شد
🚀
میتوانید کلید مدل رو از این
سایت
دریافت کنید تا
12
آگوست بدونه هیچ محدودیتی قابل استفاده هست
⚡️
قابل استفاده در
Vega Agent
☑️
Base url:
https://model.inferx.net/endpoints/v1
Model :
deepseek-v4-flash
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orC6VYWqIXXTJX2ai0keR2iaoxkZ9iivbEnXwAmRHFGPpawyungzJ1ZjOgRdybpPuyq8zzm6PX4XDLyI-xZgtRHkwvqF06f1wx5_ukkjnJY2qT0-FhStMRYLPq7-aj45ZStWa9ZAa9fkowH5488hwJvGTJyfzO0milofD2vB8-GxE6qZkGf74c4YB6rd3biSm8CvxTSEz8uzmczOiSYOxaQdDgFQVq7eGga9WlGbPISm33Mxv5uGzpfWNSHEpSu_oA5Y6xWWgQCqojyPgxG8IO-iKQQfyFRwgmBjB7pb95OUn5-yCvs_q2dbA5V5lkvoFslTCQ0779OH_kJD3qZb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان
Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید و سپس لینک ربات تلگرامی ایی که میده رو استارت بزنید برای وریفای
✅
5
دلار اعتبار برای مدل های پولی
☑️
قابل استفاده در
Vega Agent
☑️
روزانه
5
میلیون توکن رایگان
☑️
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ArchiveTel
pinned «
بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا Vega Agent رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7350" target="_blank">📅 14:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7349">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrq6qJDAH5bHZAvwQRjtShoAw0UIYOnC7i2GfRQYgqUZEzq1J3HO8R26XeW6UzAv4UbX5_JTLfYhjab_OxO5KsiBdFWpoWbkuoQKOAXu6qT_RhwkHpa-mTDbN4V8uygc79SRRZ1bWi22PCh6wVakMUndXm2Avcbj_M5QPRYMtI9l-JFKYzUxYD5OkpDqhVUen8XG_p0GeMJQxNDqbpM8siL8xWxJcmX7hxCRDgSgTVYnWbsrqJuOovsgA6ZgkznXAfTSkuGrl3J5I6GyjJbl242jeaydQWwIBBgAIM1ELHPtNB3icPK4kDJOiqc_jMl4APYLgRtI1zxLW_7fK1MPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 8000 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-jMZY3O9UJ-q6QT1hoXuxzSqGKk7aRyXo941bymtE8CgtcHyxjFmQpZfbGjA7MXmzUFeYgmIfn9Mx8vfCdvC3YayRfnaZI1NLZkSq3hhd5ZeYw6wQXbOs-8YY_WOs4V-tjAcl1Wy90OCfqhpElR5v6774-q4Gv52RMiutU18l-DD3KL0pDwr5VN3f5xQ904rx4hKw_ystkP0INleeKOJ0i4FdAjfbekdSvv6V-LsgEd5LI6_izwBuIPVFhGOl4rX47Mr7J4P0aYOorvciRnlxkm0G78UHhSBiatEkVXTJiPk42hX-buIzaKW09J29W_AiWJ1ax55RCII8DMZjFaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید
✅
قابل استفاده در
Vega Agent
☑️
روزانه بین
5
تا
50
دلار اعتبار هدیه
☑️
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
50 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy3Do3JDDgOzNLC-X7-Nsp8OM1GqCykB_ex5ADEMz0um9ndFZj-Nw6WQCltXyGVoHpDbw8aB14sll6EwAkcfmafBoGVObaf4t3CRQyAK_t7ioGLp_xSHOSrh-31PJ0TFlvMgR5LT__4H-g1sgNZjTC7vX3dTc3W-ampjrdqGmUfgvcL57VKaw44b6GeN9OvleOJQY-8hP8ijS9UKZMFF74z4NTzi666WLZ468H9hz1UfhYmOgobxsmEgR6A3t_y5SUMEqeGAyMmOueGb0PfEPG49bh7T_ZfZlGc8A-q5FfpZe46bvMa_L17uyqxLC6TJ1wc4FOnFsMBt_bSxg39UDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 1200 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fi6gqU5J8r_ziyjBuymbiOzZdd2TA2QkytXO1fm_mQbXUKYfJU-L3yhxAkq0DjW2cuP0XUWRBgXE4-CIHuZOF-vsDm1LKgP1y8AR5rKyCqtj-r_w-x3d1eYeVSbQFG1PzCf2BlBd4YwV5NmnLM2aipScZuHy36VIdk7jt09UyNnGfePIkgqaZVls84qF7Q0jDHe5z-9tZCLp4capEnnN7q7-_NsPF7np6jDScWnFMUMpmIbStlulWB-z0PTNV8tuUVtpD6mKuvhW2OhgeA6v_0tv4xrlWmGiOQDYBR2kWZP5X1QePtj_-sV9293D9kmVfQVnQk-cEkkOJCiXBjI15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcNiQ-upo-UXJ9JEeGL-FnGOR-P-cls8ide_N3IABaLfUxQUEuv2GYM_2ojQtOXOZ-gd8FbkFQwvvQ4Wl0BCWiq8AaSIbKhIK5eMdUPjaAbnbqmv9cBrboS9EbO1NK4ypS4zanYlch_rxogR2oqDKswiNAAhqRUhb1PjfA5kQIB3CNJqFHEphlUp_eJkz4opURLqtiMWuuWXc2wZdnOY6TLcZcOp3Re51gMoGuxZWQfBbzl6zQrxRKrtwHo1kimp1oRKpN-1o2zoy6GQoRjlTMupCVfnC4taeQNI73VbzX4Xnx0C3yCopcyu2snQ-yOWDrU5_WAPqZ7WonN_Byhb2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NScGf_v7Uwm_zNQ5iWejsRen9fNCo9kbGMqQ-mcvZKstnSb_uESStWIC5m9gOY50yvoZwEXilPtu5IJNBT6rri9wNgjjLCdK2mWRk56lA4niD3ZQPaRHTnEqO8L8Bnc90_QXVYKfv58fw-RjntBpkd5HVg7MRoUDKLpdpqyelrvCAY6rS8fZ2UaDe1nJ1DJr9wosiHb92uSNHfds80mcQVynEMGdtz0N12G8nCVopIz3q2KK_a0afZMEoYAfUM_Xhg6TNICsC0Ftb4eA1fZ8iWftZ1jBOgOEm137jj44ndRVoX9luIdXLYGM8fZ_UZeB54WL0wKBjhZn0Pzxpob5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TT_fTzKxfM2oe2M_ZXCBPSlcuZ6GLPYqPIKIbPVGlPtEM-ARFKREh_V-czG_FeEZZNdO8HXAxktUfHfOn9j6s1HEb-PBTlPEYSISUcg-1oIxBqM-8qC9pE1_NZNd79MC3KiKV3aH1CD2uL3304-j4CQs8NPqIz2gb2ZxGN5N4_1pH0S5V7PSM0Bybjlv97q4RRApWs0O3YjPSM-HcVk5ZyooNukClvSh-fqLIgyJsFrsEjHx1nBR4do2lfKSVNJvVQXKTQssFrXH9qBDnGYI3Kp-wvmoLpL_zXKSfy0QuGwzJZ5wxvmdyUB6CbtjCybbWK5IdOS1L6TbQ9VoKH-n4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/in3dhAJW5aqbRKP6lSWIY3P4D8H96P5UbrJj6JkPS3hwrM65Roho1daQ0TkCuwN3SqMtTlYBTaPxPip1jHL_hgeZ6QggDcyJmhzqkWp3MTkzTmfXT-j--D0t85rwhLvQ94GVJhvA7IUza9Ix959279bM6HDtwByFv2dBzi9CHCrrOd19p2xStiYx9ZFtMMVkQX53mot1TvqpXw-o7MvNQEDdg8E7OQ4pigm9l5CN0vqyRYjocUu26vUmVH900IuwL4Y-rw4JW9mmcAP8OVKhqgK6E8Aj00p4sA5nq74HxZtMEktIX6PyiwXqZAWi2dZMs18_7GhToO0qoEn1YkwdBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smYDnNRqAzGvTezynUhXld43v43UI34xOsfQYKNSHUop109NeZgaUPbvcMTxJ0NKmZeRh8xwKiYinCkgdOHJAns5nNmkgpGb4qH0CYaAPvI-Msqb7icQMwRHptnkbzy3OHiE_KrNRnhD9BpM09Bdp5oyKOitvOgWfGMSK_bJzf7jOLpkOh0LgHwRHusziLSs7WEp7pbP7AYZrG6mwsx-WyL3XNupGlCASIZxyjvmBD46nbFByNYDDrtpsxkd4BB-0vjNDoOIst89u4IB-npX4G79PbOm99Upi-vGbkkXDxVUrpCftSVmc4reudCvb6pEwZq8QA8MaHC_M1Mpja9VXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNYvVeYDAJ8jakxBP8XfAi3LIVZXhN-SUen-LbqQ16JiGzccK26pKA8PWWKUwH7SpY9aEYhvoM1n-NLYt-rmYfNezgESXk94y0qE8hgw5PoBecCSX8n2bzGcI3eYkpUODc0y6MNkrUE0CxboIWSQHHwje2ouVRsgC_RBOdgQ-uUo5FvD7DHooWPh6FNHD_AZxgGEqrIEj4XvQbjAnhCnh1ZTnOCxmLBubASRfgg6hG58x4kXON8cteh1-BagXhXidRBl9CMC8I-fdZaxiX3SRw877RSokVHXfo_ZprPVF0g3BkNnoO6n75AvvAj763BTxyxJczIS-dw4itB3vKwl_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7337">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا
Vega Agent
رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ سرور واسطی این وسط نیست) و مستقیماً با کلید API شخصی خودتون (BYOK) کار می‌کنه.
✨
چه کارهایی براتون انجام می‌ده؟
🔹
پشتیبانی از همه مدل‌های معروف:
از OpenAI، Claude و Gemini گرفته تا OpenRouter و حتی سرویس‌های لوکال مثل Ollama.
🔹
مدیریت مستقیم فایل‌ها:
بهش دسترسی بدید تا فایل متنی بسازه، کدها رو ویرایش کنه، PDFها رو بخونه یا فایل‌های زیپ رو استخراج کنه.
🔹
۳ حالت اجرای هوشمند:
برای اینکه کنترل کامل روی تغییرات داشته باشید، می‌تونید روی حالت‌های خودکار (Automatic)، برنامه‌ریزی (Planning) یا تأیید مرحله‌ای (Accepting) تنظیمش کنید.
🔹
مرور و جستجو در وب:
خودش تو اینترنت سرچ می‌کنه و محتوای سایت‌ها رو برای تحقیق و استخراج اطلاعات می‌خونه.
🔹
امنیت بالا:
کلیدهای API رو با الگوریتم AES-256-GCM رمزنگاری کردیم و کاملاً امن روی خود گوشی ذخیره می‌شن.
📥
فایل نصب (APK) و سورس‌کدش رو تو گیت‌هاب قرار دادم. نصب کنید، تستش کنید و اگه خوشتون اومد حتماً با دادن ستاره (
⭐
) به مخزن ازمون حمایت کنید!
📌
لینک دانلود آخرین نسخه از گیت‌هاب
@VegaEnter
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7337" target="_blank">📅 21:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7334">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بالا باشین بچه ها عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7334" target="_blank">📅 21:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7333">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بالا باشین بچه ها
عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7333" target="_blank">📅 21:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7331">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwplZyDQag9ontpsivis9ylq1VjNplcLUrFuajYZwymWZlhSaTTMyWbWSGcfg0sKirhKnZ2VQtdSUpsqGvaM7TbApUAg26IcjsdWIWEDthJBUK_OCOL8ZYP-J1zBNmf8lRTKpmSB5tbAdRnMBLY5X-Iqzi2GzqHo69B8VAoSnzozAK_Z0wXtxpDeoDRj7EW31JRnwbyZ6l9_eWB-gZ4H7pe0w9Ew9cFATTqcnW7F8uvzp_TkKe6mVdSb1EjFRB4_jg_simrZnkCOgzn3pDgrVHJYTKyuBpH6iFj7jtXr71jrub7gbz-TcRHe1buuGXkXtjEVQsaiLThzqPHKoataJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت ویدیوهای حرفه‌ای با هوش مصنوعی، اونم رایگان!
🎬
✨
بچه‌ها با وب‌سایت
Dola
می‌تونید روزانه ۴ تا ۶ ویدیو باکیفیت رو با مدل قدرتمند
Seedance 2
تولید کنید. علاوه بر ویدیو، این سایت ابزارهای چت و ساخت عکس هم در اختیارتون می‌ذاره.
🎨
✨
ویژگی‌های کاربردی:
🔹
تولید ویدیوهای حداکثر ۱۰ ثانیه‌ای.
🔹
امکان دریافت خروجی در ابعاد و سایزهای مختلف.
🔹
کیفیت تصویر بسیار بالا به کمک مدل Seedance 2.
🔹
دارای ابزار ساخت عکس‌های خلاقانه و چت‌بات هوشمند.
🔹
سهمیه رایگان تولید ۴ الی ۶ ویدیو در هر روز.
⚠️
نکته مهم:
برای باز کردن و استفاده از این سایت، حتماً باید از VPN با
لوکیشن اروپا
استفاده کنید.
🔗
ورود به سایت Dola
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7331" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7330">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKURz5VY80HQOv5PGpsQ4TZyD546j_1QABauwrSz8FM9uP0vcymoOLClk1q3043h4arI5IlCfMBa8m-Vt-3Tb7QNqEGekvyekX-3suDYv3mlryWq7S0QxvjVjYet6UnjGglECnEUfmHP07L0Gq-805WkhEOxZhkpC2xgNnsWSAF_Z239sf04aPx4bOKjX5HXDtQ1eRsyCHZUbnEVs-5_fXmtfcgKnXzW2yot4oBEL-gzx4RDo__NqBaFtsHoGP0L0Y-CmRGkqK8HQ53dvyzPI9Q9iiH-FvsLc_KwwiurjcqHhT5A88Zy-F5DGMD00LRGpJA7_pLqpnQ1_m0aS1r2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Türkiye'deki İnternet Kesintisini Aşmak İçin Güncel Yöntemler
🇹🇷
🛡
Herkese merhaba, Türkiye'de yaşanan son ağ kısıtlamaları ve internet kesintilerini atlatmak için şu an çalışan en etkili yöntemler şunlar:
🔹
IP Spoofing (IP Yanıltma):
Şu anda IP Spoofing yöntemleri filtreleri aşmada sorunsuz çalışıyor. Xray/v2ray yapılandırmalarınızda paket parçalama veya IP yanıltma tekniklerini kullanabilirsiniz.
🔹
DNS Yöntemleri:
Bazı ağlarda özel DNS ayarları veya DNS Tünelleme (DNS Tunneling) yöntemlerinin de erişim sağlamada işe yaradığı görülüyor, mutlaka test edin.
Lütfen bu bilgiyi internete erişimi olmayan veya sorun yaşayan arkadaşlarınızla paylaşın!
✌️
#İnternetKesintisi
#Türkiye
#ErişimEngeli
#VPN
#Turkey
#InternetShutdown
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7330" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7329">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ابزار تحت وب «بهینه‌ساز کانفیگ» برای عبور از اختلالات کلادفلر
🛠
🚀
بچه‌ها یادتونه تو پست‌های قبلی آموزش دادیم که چطور با اضافه کردن finalMask و cipherSuites تو اپلیکیشن PattNG مشکل آپلود رو حل کنید؟  حالا برای اینکه نیازی نباشه دونه‌دونه کانفیگ‌ها رو دستی ویرایش…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7329" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7328">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKQvbPA2qZukoY34HikB7pKvwEqcS5vFJLs3MVf0kewEdrxQBUWK3X7eLreGVXOYbBrbfdj4jSg8XUaNQebKTpC5ogJbidkoUPg-0osfWaYR_RYgyMIaj-eJjZi_CIFHdZkJDl-j8fNhW5tRqYLf29Z_wlvapZbkGKr1fhE6UfGjhlbp11ABmYwSJxREPxj3fvpgAvMksw2WWxs1V-ScWyW5g3PPDbutxCrlQ1gkh8DdQmcq4GQKOqroBXZYxsd_oPYIq44uyr9LPzdNB8FuXNvodMjqCq8W4gEL18nN3G9XN0AeKrSTCZsdQ4O6gxsWMmBcHWcHLRpvXVBJkn2tlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به هوش مصنوعی‌های فوق‌سریع و قدرتمند در یک پلتفرم!
🚀
‏با این سرویس، تمام مدل‌های برتر دنیا رو یکجا در اختیار داشته باش. همین الان شروع کن و از قابلیت‌های هوشمندش لذت ببر.
⚡️
‏
✨
ویژگی‌های کلیدی:
‏
🔹
دسترسی به مدل‌های پیشرفته (‌Opus⁩, ‌GPT⁩, ‌Gemini⁩, ‌Sonnet)⁩
‏
🔹
مجهز به سیستم ‌Agent⁩ برای انجام کارهای پیچیده
‏
🔹
۲۵ درخواست رایگان برای شروع
‏
🔹
۱۵۰۰ کریدیت اختصاصی برای استفاده از سایر امکانات
🔗
https://app.clickup.com/login
‏
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7328" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7327">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG: github.com/patterniha/v2rayNG/releases  ۲. ویرایش کانفیگ (
✏️
)  ۳. فیلد Address: یک عدد آیپی تمیز کلودفلر  ۴. کادر finalMask: {"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"]…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7327" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7324">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pxF3VDDa0AGt7mb5vgqYM6JDdj-QRMRrlBtg0NLq1xt7eZSVQnpPS1Db2GO230mP0-VaZR0-33TJX7rmGaMO0Qu7mdthyMl-7tTDHZ9VtGEXD0xg42iALdczjCRIzOPsHV0GKK87CHFri0J6hHgiqDZSmpZqRAwlz7lCAAQlsylYQXI_FHtkllatTf_EsExInXXoQSo-54bMZ8po5hzoqwSzwGHW4k_eA1ichIrFCMRmBWjrzUOwVNM-CDvRvtBTq17MpKKk812KzcRAyqyyPAzeAryzlhKPe0-q4DAXEqyxquTda2od4vRamoqzMC6iVDJ2IObLITm5KJerz8OXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSp53z88BCMRWjY0y0VjE2RbJD2fc49b28X5KjrQAd2BCs_CWyAgamReOoPESQ01QmPZCAykzsF2SRQrigBz5CyBi47qReKncqnl3Kca9FOW38nuJ_XzP_tEw0e8e1YD9CCW6lPHLWi-AiE2ul7qM9885vQhipsAlZSukELthOmUCJzz06Nw84ud0wf-rJPLEjMT-UIEcmGLNuU6KGf_1cUyOWpAzUiAfPjdgGuoxoViaoRaO4OUWRV0VQlh0v2h9giChD1zIRU0UpKE6cEh2_Qvkj3BAO7vjq5Q-IkMwfWPn4bJXOXRzNUk02VYSS1bG3e63ieb8r3z2kK_ajMo7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fglFZLYJj3juyu2rYVQZe1SUaLOxkQxCxKRpuc5tKwZr0wzHyM_tbL_tLVrjqRiayqlAVbHiErUs9RDgJ1f1U4-U_A6tvPFcF3AcCsfnBHCW6Vak05nY8EenqacTCghKSjCkzcLpufDKpfNBEvSj32kS7WCAVgVwB9Sr54PLWENFLz6Th4Z6A7KUIBOi0J-KkbKXoQT3ne1CrlnCaZ1b_Vf_iAXaeSaIz9_JG5a41U3-CyeBULB53t3rjXk9Lzm18_U8kRApxv6zXewPMpyDdEk-NbZGLyYIzkcv42UvAzc157wPYcnzAVvRVsR04F3qKDl2j1Nc5hYu45F_QwUZlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG:
github.com/patterniha/v2rayNG/releases
۲. ویرایش کانفیگ (
✏️
)
۳. فیلد
Address
: یک عدد آیپی تمیز کلودفلر
۴. کادر
finalMask
:
{"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"],"delays":["0"],"maxSplit":"0"}},{"type":"fragment","settings":{"packets":"1-1","lengths":["109","1"],"delays":["1"],"maxSplit":"355"}}]}
۵. فیلد
Fingerprint
:
unsafe
۶. کادر
cipherSuites
:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
۷. ذخیره کنید
✔️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7324" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7323">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PattNG_2.2.6-P2-fdroid_universal.@ArchiveTell.apk</div>
  <div class="tg-doc-extra">68.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7323" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود نسخه یونیورسال PattNG (نسخه v2.2.6-P2)
🚀
📱
بچه‌ها فایل APK این نسخه (Universal F-Droid) روی تمام گوشی‌ها و معماری‌ها به‌راحتی نصب می‌شه.
🔹
پست مرتبط در تلگرام:
🔗
مشاهده فایل و جزئیات بیشتر در تلگرام
💡
*دم توسعه‌دهنده‌اش گرم، واقعاً خیلی زحمت کشیده! اگه دستتون بازه، با زدن استار (Star) توی تلگرام یا گیت‌هاب ازش حمایت کنید کارهای خفن‌تر تحویلمون بده
😁
⭐
*
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7323" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7321">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7321" target="_blank">📅 01:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7320">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فردا شاید ی سورپرایز یا دو تا سورپرایز بزرگ داشته باشیم
🫠
❤️‍🔥
(البته از ۱۲ گذاشته ساعت)</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7320" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7319">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7319" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7318">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHhTsejxGNAsHqU7OSyHjUuBD15B3ljzI2jd0Cf-DvTYvc7pAuL3gPLdM2KYRSgZhnzh0rUTmmzXBwYv63mSVAh1uAyEqMFKfPSfaQbqFFa24h3NyIFajnn0H0RBC_vbpez8S4vrBKf_svc74UFM0N2Vx8AaL_0JAqmIdYD4ppTRDPWEYjkJ89u1Ah55Jy1FcS_x9_SJnx057H5TdRtYthTLEb6TUMpzERaB_whvY5junWKXkOM4AI0jMUd-4vgM2m37HRvZpTr77RzCxJoz1_I03NSDcSfHr6_jceU3o6iaAOgyQhNpngOdi6km7psbmV7TN8z7reViSMYbBsjwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش شدید قیمت API مدل‌های GPT-5.6 شرکت OpenAI
💸
📉
شرکت OpenAI هزینه‌ی استفاده از API مدل‌های سری GPT-5.6 رو به شکل چشم‌گیری کاهش داده؛ اونم به لطف بهینه‌سازی کدهای سرور توسط خود هوش مصنوعی (مدل Sol)!
🤯
✨
خلاصه تغییرات قیمت‌ها:
🔹
مدل Luna (اقتصادی):
۸۰٪ کاهش قیمت! (ورودی: ۰.۲۰ دلار / خروجی: ۱.۲۰ دلار به ازای هر میلیون توکن).
🔹
مدل Terra (متعادل):
۲۰٪ کاهش قیمت! (ورودی: ۲ دلار / خروجی: ۱۲ دلار به ازای هر میلیون توکن).
🔹
مدل Sol (پرچمدار):
قیمت ثابت موند، اما حالت جدید
Fast Mode
بهش اضافه شد (۲.۵ برابر سرعت بیشتر اما با دو برابر هزینه).
🔹
راز این ارزانی:
مدل هوشمند Sol، خودش کدهای هسته‌ی سیستم رو بازنویسی و بهینه کرده که نتیجه‌اش کاهش ۲۰ درصدی هزینه‌های سرور و افزایش ۱۵ درصدی سرعت تولید توکن بوده!
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7318" target="_blank">📅 21:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7317">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbPAO63eck6CcqU6JCI_Xejgx9cElxNh0tQMtJdNN7UK5TqunTc0EJtb5nHb4Q-sZs3VWxgxJdqfj3HVbpiL_RiStrx1yLmGmASnltKuT8kbnv8V1sQHAbCG502HdXDtE_5a0WmInQ9mivIVJ8z2XissBrFkl4UTWOfcdpM1tuD-RCiDDKqbqXvTTDVTjb7a7x7MmLIegsI5c16G93fO21PrOct3vxLzzkXkv7FaqADhVvZtcqBIhQ8iIDKimkaYi0095G4voB-Zz-uCjBIXUXrhcagzdbtX_cYSIt3uxaUf_i--Hendd7nAr6KUAh85gwEWq9GjaTlsRa1ddklSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت ۱ ساله Pro سایت
Beautiful.ai
(رایگان)
🚀
🎨
بچه‌ها این سایت یه ابزار عالی بر پایه هوش مصنوعی برای ساخت اسلاید و ارائه‌های حرفه‌ایه؛ فقط کافیه موضوع رو بهش بدید تا خودش کارها رو انجام بده!
✨
نحوه دریافت اشتراک آموزشی (EDU):
🔹
مرحله اول:
با فیلترشکن وارد
صفحه
بشید و روی
Claim EDU Offer
کلیک کنید.
🔹
ایمیل دانشجویی:
ثبت‌نام رو با یک ایمیل
.edu
انجام بدید (می‌تونید از سایت‌های ایمیل موقت مثل
tempmail.id.vn
کمک بگیرید).
🔹
اطلاعات دانشگاه:
برای اسم و لینک سایت دانشگاه، از یه هوش مصنوعی بخواید اطلاعات فیک و رندوم بهتون بده (سایت گیر نمی‌ده و قبول می‌کنه).
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7317" target="_blank">📅 20:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7316">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9lt1xp66h9mgjGW-z2UIXziXHVu1dkBzNVfC3iTj5frCVmscq8A5Zucc7htMuX6S_sPGUIS31dxCmgZa3J7r2BPP5aIj2wEp3MXgCDrcv2hjSh6PgJuYDpve6gEjk9xTpEwrMH1U0pP9AIpskmkJV_sChFG9b4udTJuH3mJr4xXhpPls1IQHECCGZgylJaYr88mX7X2LmXM4Q2MzceTk6V8qdwliKDEwi6p30dzUv5tSl2mzsvhCBg9St-wEzSpdSalbLUGYee_Ld8ovna2_W8nzDZ59RqLjzmclidXtXcsIirhUOuwYb9TMF3GBhRqKfH1us1ZfvvGzbbXaFgdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی ابزار PDFx؛ ادغام و تفکیک هوشمند فایل‌های PDF
📄
✨
پروژه متن‌باز PDFx یه راهکار خلاقانه برای مدیریت اسناده: ترکیب چندین فایل در یک فایل، اما با حفظ قابلیت جداسازی!
✨
خلاصه ویژگی‌ها:
🔹
ادغام و تفکیک:
چند PDF و عکس رو یکپارچه می‌کنه. این فایل تو برنامه‌های عادی پشت‌سرهم نمایش داده می‌شه، اما تو برنامه PDFx دوباره به اسناد مجزا تفکیک می‌شه!
🔹
کاربری آسان:
مدیریت فایل‌ها فقط با کشیدن و رها کردن (Drag & Drop).
🔹
دسترسی:
دارای نسخه وب و دسکتاپ (ویندوز، مک، لینوکس).
🔹
دستیار هوش مصنوعی:
پشتیبانی از مدل‌های OpenAI، Anthropic و گوگل (با API Key کاربر).
📌
[
لینک مخزن پروژه در گیت‌هاب
]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7316" target="_blank">📅 18:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7315">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه پروژه جدید ساختم برای 3xui دارا که خیلی بکار میاد
دیگه لازم نیس آیپی های تمیز رو دستی اضافه کنین پنل
یه ربات تلگرام هس که به پنلتون وصل میشه، بهش چن تا کانال آیپی تمیز میدین، خودش خودکار آیپی های تمیز رو از چنلا برمی‌داره اضافه میکنه به ساب پنل برای تمام یوزرا بالا بیاد.
سورسشو شب میزارم.
تمام.
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7315" target="_blank">📅 14:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7312">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARjLM-yezCj1hmK0D-0Nmbwv-Ix5WhPgAGW-FLJqb33HDCpBio0D3mCYEGvsNkJQ3TYGQEc0bkGx5SFeAIrrJHXU_YUfCfNiLSxBX2URKRJlTOPsMOGtNpxo7fRDL9QTpZsLUhiuEaF-yvyDzScAPlJ3YNW0hrmoOPIr5Gn__nftsCvemHSfSp0RkLDtP5RxGccry-DH5_tgUcHZN4n-IYbM2pRz7PmzbekInrN4t7CUrlPb6xGYi8-74Wlv7Lum2VfSjEP6YQ4mdSQfA-DICCyl2dv1r3QumnMIdhD7Xw_W-lUcLiK8hRqidt9aTTjvFg83IXSHqvKWZxu-aKOdJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید پنل 3x-ui (نسخه v3.6.0) منتشر شد!
🚀
🔥
نسخه جدید با تمرکز روی امنیت، پایداری و رابط کاربری بهتر منتشر شد.
✨
خلاصه‌ی مهم‌ترین تغییرات:
🔹
ارتقای هسته (xray-core v26.7.28):
(نکته مهم)
ساختار
finalmask
تغییر کرده؛ اگر قبلاً از این قابلیت استفاده می‌کردید باید پروفایل‌ها رو از نو بسازید.
🔹
امنیت بالاتر:
بسته شدن دسترسی آزاد به فایل
openapi.json
، امن‌تر شدن توکنِ نودها و مسدود شدن دیفالتِ آی‌پی‌های لوکال.
🔹
لینک‌های سابسکریپشن:
تشخیص خودکار نوع کلاینت (User-Agent) و قابلیت جذاب چک کردن وضعیت آنلاینِ کاربر مستقیم از لینک ساب (با اضافه کردن
format=info?
).
🔹
داشبورد مدرن‌تر:
بازطراحی کامل صفحه اول پنل با گراف‌های تمیزتر برای مشاهده زنده مصرف سرور و کانکشن‌ها.
🔹
پایداری دیتابیس:
اضافه شدن قابلیت بکاپ‌گیری زنده از دیتابیس (بدون نیاز به خاموش کردن پنل) و رفع باگ‌های ترافیک.
📌
نصب و آپدیت با همون کامند همیشگیه، اما
حتماً قبلش از دیتابیس بکاپ بگیرید!
#3x_ui
#ثنایی
#پنل
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7312" target="_blank">📅 12:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7311">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6Lx6ux07syjE1oRJyfJXUurZBoXdzw1rsnRgjEL0ELcHAV4mK0jj5wY9Y0vwkzXvB8sZHiTfIHm7vONUoNlmvBPYTU6GS1g3TO9KZNpFzcAD0bx-YM0bsRRzBUMa68LmxXT5Uh_Ns3LE7fMa7AM5JFdt8tu8vSxHYuqhPVvZ0eidJPdFt5F7Y7XpWTdY76ktp7QhT61TegsFL5b6W8QTflajlKu86GN-5FCuQTm-x9Uthio_C9_K_o27MMnnX7YCuVptXfdRlzXXN1po3TFZP9wx2f3O3OGi5INsNbfLv7rF7L_MAcv2Ke93WNIFlQcJwP0vGz1iRq9p_PWZ6OLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک ۱ ساله ChatGPT Pro رایگان برای دانشگاهیان
🎓
🎁
بچه‌ها می‌دونم این طرح به خاطر تحریم‌ها و نیاز به کردیت‌کارت و مقطع‌تحصیلی بالا به درد خیلیامون نمی‌خوره، اما اگه دوست یا استادی خارج از کشور دارید حتماً براش بفرستید تا استفاده کنه!
🔹
مخاطب:
اساتید هیئت علمی و محققان پسادکترا (Postdoc).
🔹
شرط اصلی:
داشتن حداقل یک مقاله در ۳ سال اخیر (در سایت‌هایی مثل arXiv).
🔹
تایید هویت:
نیاز به ایمیل آکادمیک (بدون VPN) + کردیت‌کارت (بدون کسر هزینه).
🔹
مزایا:
یک سال اکانت Pro با حفظ حریم خصوصی + ۴ دعوت‌نامه رایگان برای همکاران همون دانشگاه.
📌
لینک ثبت‌نام در سایت OpenAI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7311" target="_blank">📅 10:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7310">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjID3pLgor8w-aQ6d_JN7jU6kzKra794Vq4ao7g7EIvylD7p0ViVpD4rKIB-_kAnp0ByWcrqyL_eveOHuhvXc8yHKLYOKHZYIO4no1OFoMCFF5myJET0T-xDFUIAmzy2l2_dQsZ2w0etCO7yvvBuxnDg9nufBy_PERSJv2Mxf6BnLr1MyYn077tTvj67q_fNr3qEDbcFSx8sDbwo47FjPgeTdPzPDcHVtCQlX3GMouQ1m_1mDY_-1JpC9kulmHU_P5Rp7LRiCAeqgFgMQk5T-yvlK7oZNxiRh3aMAnFQesQSTmxLFarsiXB3C-KCaiZ1ZDyJx5NyLa8TzVhQhojF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از Grok Voice Think Fast 2.0؛ شاهکار صوتی جدید ایلان ماسک
🎙
🚀
شرکت هوش مصنوعی ایلان ماسک (SpaceXAI) به تازگی از جدیدترین و هوشمندترین مدل صوتی خودش پرده‌برداری کرد. این مدل مستقیماً برای پردازش سریع «صوت به صوت» (Speech-to-Speech) طراحی شده است!
✨
نکات کلیدی:
🔹
قدرتمندترین نسخه: به گفته سازندگان، این هوشمندترین و قوی‌ترین مدل صوتی است که تا حالا توسط این شرکت توسعه داده شده.
🔹
پردازش مستقیم (Speech-to-Speech): ارتباط صوتی کاملاً بی‌درنگ، که باعث درک بهتر لحن انسان و کاهش شدید تأخیر در پاسخگویی می‌شه.
🔹
رقیب تازه‌نفس: کاربران به شدت منتظر مقایسه‌ی عملکرد و سرعت این مدل با نسخه جدید gpt-live از شرکت OpenAI هستند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7310" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7309">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تغییر ظاهر لینک سابسکریپشن 3x-ui (پنل ثنایی)
🎨
✨
پروژه
MiTemplateSub-XUI
یه کالکشن عالی از قالب‌های مدرن برای صفحه اشتراک کاربرهاست:
🔹
تنوع بالا:
بیش از ۳۰ تم مختلف (سایبرپانک، مینیمال، شیشه‌ای و...).
🔹
پشتیبانی از فارسی:
کاملاً راست‌چین (RTL) همراه با دارک/لایت مود.
🔹
جذاب و پویا:
نمایش انیمیشنی مصرف ترافیک و چیپ‌های پروتکل.
🔹
مدیریت راحت:
تغییر و نصب سریع تم‌ها فقط با یک دستور (از طریق اسکریپت اختصاصی).
📌
[
لینک پروژه در گیت‌هاب
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7309" target="_blank">📅 23:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7308">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWkt3q1CLJ5_0ck4Kq6FYktD0zobfKn5XII4NgRBL3mzA_NKDNEGJCQjx7aoCKw7OiJe-oCO3kuSQ48AWgzjtLCoinJYArCWyozVHr-cFru2NfZmhbibC7YgCSVmvCY3yB5goHg7oBc4nxJKyth9KC8D_4dhiDTX9_2EyimdFwVutThI86JKeHfm5c_NE5_4YRrhIXVLTabbQFX2W0tWn4jool65AcOoWkoe7yaVgfkdrknUXYrzFL75hNBFTSCfkb2Bv9RPf-a1MVa9SbWAUomGuBf0eozRdGg4G7xjSeeWgaCQo4cHbAjpuEHcOdPuPWEjYWUfOz1iNh656dQ5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ابزار ‌Onlook⁩: انقلابی در طراحی و کدنویسی!
🤯
‏اگر طراح یا توسعه‌دهنده هستید، ‌Onlook⁩ دقیقاً همان چیزی است که به آن نیاز دارید. این ابزار مثل یک دستیار هوشمند، فاصله بین «طرح» و «کد» را از بین می‌برد.
🛠️
‌‏
✨
قابلیت‌های مهم:
‏
🔹
ساخت خودکار:
تولید پروتوتایپ‌های حرفه‌ای همراه با کد تمیز.
‏
🔹
تعامل دوطرفه:
امکان اکسپورت به ادیتورهای کد یا محیط ‌Figma⁩.
‏
🔹
سرعت بالا:
صرفه‌جویی چشمگیر در زمانِ طراحی و فرآیندِ درکِ کد.
‏
🔹
رایگان:
دسترسی به تمام قابلیت‌ها بدون هزینه.
📌
[
لینک پروژه در گیت‌هاب
]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7308" target="_blank">📅 22:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7307">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU7y0XfzRvVWqKlLTezGUpwYkyE2x5GYxA242t4MW6fr-kxAYGJADhBWMM-3T4-wV2TspQxc9hWzJ2QHuCjm7NIxinluBSuMdyhBprsEi48YkPvurJOiEMTsdFuoODjYD1Wrhp4JFgI4jTZ7u6_BlDVAfLolmHp_fQPIi_lVU6tbj_9H7EailCbdXUaj3ckKbKAjuhH_KQRVTuFWPL9txmEnBQjLA9ez4IPF_y35ZeT7TL8uPnnjPKoSC4Rj9UdDmsRCMOTLwSTY3tJuJfal3zYgm1KwZT0sxhKYU6avMzTqrSo49aljmcDFBshWsOuvhgXyFfD7RSSbCGTF7lIUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
گنجینه‌ای از هوش مصنوعی در دستان شما!
🚀
‏اگر به دنبال پروژه‌های آماده و کاربردی هوش مصنوعی هستید، این لیستِ طلایی شامل بیش از ۵۰۰ پروژه متن‌باز در گیت‌هاب، دقیقاً همان چیزی است که نیاز دارید. از چت‌بات‌های تخصصی تا ابزارهای پیشرفته‌ی ترید خودکار؛ همه چیز در دسترس شماست.
✨
‏ویژگی‌های این مجموعه:
‏
🔹
دسترسی کامل به سورس‌کد تمامی پروژه‌ها
‏
🔹
تنوع بی‌نظیر در حوزه‌های مختلف (از بیزنس تا مالی)
‏
🔹
مناسب برای یادگیری، توسعه و شخصی‌سازی
‏
🔹
پروژه‌های تست‌شده و آماده‌ی اجرا
🔗
‏
همین حالا از این مخزنِ ارزشمند استفاده کنید و سطح پروژه‌های خود را ارتقا دهید
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7307" target="_blank">📅 20:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7306">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqel_6lv7XnBf-7T8O7-sC2Z6EMJjgqE-3bUY0l-GOCbSoroPObwubstsZUExshanThUm1z6eR0clOBfbq9H1KBwFamcQApLlEE_qr6pJqCZbiP5FuESVCB5pVNQ6qRQ2CLqPMBEGQ331_tg_Suj1coEysjpjdCqLy0_HiUqyTEYG22YqKigRYx1myBHQ8W_dj_j2gxMkK0VMpAHwbj8OBv3xFA1gFys1djVPvkKc21VO7aQWQjNQRKLhBojMWVYdN_nkkh9lxPgPhqA9cImx5-sFut7G41H_sjLJj3Ve8UkK6odrJAzA8ffngAH5uNFocLY74cjZgdMJDHcqejsXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت تلگرام پس از صدور حکم بازداشت بین المللی روسیه علیه پاول دوروف
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7306" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7305">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpICtF4hSzyQ1vm52AK1wrXLMCkPZ7F7FZW3iduzt8LdeyfI1Fi0p9piR34nub0xfoYhgbQ0Z8sqKwsV05l1HB35UXi1WEyUCtXkkzY73BplYpSlXSsBtJM01LvawjcDhGwSxPNAoGZ7E5A3qQhXsFrxLumwuKKSwoNPQ5y78Ngd6XOFmnTzU2Vpg8FSvm-qmOhIqx0abVMCYk_y4vB4Wh7Qdz7rgbSzThVpsmLAzoY8oUKl3aCAOq9f0sDXYJec_4pq__tbvNNp8xVkJu-JUaGSSEF87uVQFYgfa6RYSTIX1RcJy_5Qwb-_GUg_cI7iutqps0pzCfqXURhNlay0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😂
https://t.me/ArchiveTell/7300</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7305" target="_blank">📅 18:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7304">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIZNxyEGSZnmKgunW7ooOCsESOTxuS0q7TGUOb8oosJ_ckGENGyyzbIV5iLhZ0NMcXYngrrHYmsIwN81OxG7FZD_3lnmAcmBdKxjAvGffODzp-vloS33viE-r3GVBr4adLfw_Tzg8vKDETI1gb1VnF48X0HPFf96wVGnSs9bnYlAci3WgVx5tEMnAvcR7jTpgiTO47AFgxTJjVCxacF_gx4_OMGJp3w9lFyH2fEbg5Bm2VsLRK7WmUh6pK-YRNH2a7wQJ7tcoNBucVUBRu3p4HOdi9PzqtAXsAnDhzs-hR4QcjRSchh15JxjPeq5AbvAqkpTL_TVWAMRpZAnlEA1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏‌APK Converter⁩؛ پلی میانِ وب و اندروید!
📱
🌐
‏این ابزارِ آنلاین، پروژه‌های وب، فایل‌های ‌HTML⁩ یا بسته‌های ‌ZIP⁩ شما را مستقیماً به فایل‌های نصبی ‌APK⁩ یا ‌AAB⁩ تبدیل می‌کند.
🛠️
‏
✅
ویژگی‌های کلیدی:
‏
⚙️
تنظیماتِ اختصاصیِ اپلیکیشن و آیکون
‏
🔑
مدیریتِ حرفه‌ایِ امضای دیجیتال (‌Signing)⁩
‏
📋
نظارت بر لاگ‌های ساخت و مدیریتِ تسک‌ها
🔗
https://gentsergame.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7304" target="_blank">📅 18:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7303">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJlOQMQC7K5hr8tiRMTiaH43SHnj5eJMKqL11F1UXfZhITLKT36I4EeWKhPnaZMr1gOCnjijGopsbRuOfj21dQL2rHZfl3BLG7CzgPOrsrecukljXFQXukDy0-rrafCx0ybmU2BDSrdG2dBTHJ_TwmHBnmfLArvs77v4T7HJussIJOYQwrOn0Qe7zpR8uZpuVEEdQ9isw8l_duUsurEwBsnX0Pw_doQYh40gvpvPO-14maeW1_g3-vNpIfjqovpi2HFAmw2H5oNa1Q3Z9KFOzh5E1zylz8VmG_orFtKtmiGAmUEtzljsCrehh0sdH_vvYA0kGDDdSky_uT9lYELQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
انقلاب در کدنویسی با ‌JCode⁩: سریع‌تر، هوشمندتر و قدرتمندتر از همیشه!
💻
‏اگر فکر می‌کردید ‌Claude Code⁩ سریع است، ‌JCode⁩ با سرعتی ۲۴۵ برابر بیشتر، استانداردهای جدیدی را تعریف کرده است. این ابزار نه فقط یک دستیار، بلکه یک «تیمِ کامل» در سیستم شماست!
🐝
✨
‏ویژگی‌های کلیدی ‌JCode⁩:
‏
🔹
سرعتِ خیره‌کننده: ۲۴۵ برابر سریع‌تر از رقبا با بهینه‌سازی فوق‌العاده.
‏
🔹
مصرفِ ناچیز: هر سشن تنها ۲۸ مگابایت از رم شما را اشغال می‌کند.
‏
🔹
معماریِ کندویی: ایجنت‌ها با هم همکاری می‌کنند، وظایف را تقسیم کرده و کد یکدیگر را بازبینی می‌کنند.
‏
🔹
حافظهٔ هوشمند: با حافظه سراسری، هیچ خط کدی در سشن‌های مختلف فراموش نمی‌شود.
‏
🔹
سازگاریِ کامل: پشتیبانی از تمامی ‌API⁩های بزرگ (‌OpenAI⁩, ‌Claude⁩, ‌Gemini⁩, ‌GitHub⁩ و...) و مدل‌های محلی (‌Ollama)⁩.
‏
🔹
خود-اصلاح‌گر: قابلیتِ عیب‌یابی، بازنویسی و رساندنِ کد به کمال.
‏
🔹
تجسمِ پروژه: تولیدِ نمودارهای درختی برای درکِ عمیقِ ساختارِ پروژه.
‏
🔹
مهاجرتِ آسان: امکانِ وارد کردنِ سشن‌ها از ‌Cursor⁩، ‌Claude Code⁩ و غیره.
‏
🔗
دسترسی به ابزار
‏
📂
مشاهده سورس‌کد
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7303" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7302">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByWI_n4VbVaCaPLH9relDlZi4lMFx01_6xYVlLxORrwrzTq1W9VQ_3QVS5TIojaqr6OfLwrFVAWQhMA5mRMhHjLmv2zp5Nhrz7vc1tFJZWs5HsIWkAJZNIveLxMmsmmJjZC-_T_zvjdKzpeCy8446U8STWsgzYLZ2wPPwuFEDWopVAP4qNs-xTgQi-0DUPlCEuC2ZXN7vscb5CPsxIVDvspL4Whs5ug4-fy3Db0zzIxulNZQ6ZmxcNyOm9uzpOadEcmdSZECvEK1Z5wxl-d8qHrbKVjyZxij7UhVYPBDS_1bl65UVZHbVgFDuQXwnLrfh3iQyGGRMwlCHtq-ZcbayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
70 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Opus 5 | Opus 4.8 | Sonnet 5
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7302" target="_blank">📅 12:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7300">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXbSYn8YeejGRZ299dE_oT8ctj4gqSAultXqJgW21ufAOoQtPybAJoV2B05NAT4fd4WdKhZO7G9yaajyaPUjWW0rRaOl7Qw-Y8c63hlMNmoRHuAwAwEGw_49-w0E7PRY5P-KoqFD2bVSdeiPAl3frhBBY34sBuNnTkhSfsJT5scu7skTY1j7iovRsdPKFRG2g0QkoK0qrldU2JHsT5BMmFmw6hXWybQpoDOJjjL0kOiFEvSIlPr3fJCQDIr5R12WcFW3CUSpe1ABWuxi6imTHrZQ1ic6knZwdZaV1txDx-wLzMx9vjnoBcHTZHUcGO7vtawafeQvBdEuJ58oYksCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتهام جدید و عجیب علیه پاول دورف؛ حبس ابد به خاطر ربات دوست‌یابی!
⚖️
🚨
یه خبر عجیب تو رسانه‌ها و کانال‌های روسی داره دست‌به‌دست می‌شه! ادعا شده کمیته تحقیقات روسیه (СК) پاول دورف رو به خاطر عدم حذف ربات معروف «Daivinik / Leo» (یک ربات دوست‌یابی تلگرامی با بیش از ۱۳ میلیون کاربر) متهم کرده و شایعه شده ممکنه سر همین ماجرا با مجازات سنگین یا حتی حبس ابد روبه‌رو بشه!
🤯
✨
ماجرا از چه قراره؟
طبق ادعای بازپرس‌های روس، سرویس‌های اطلاعاتی اوکراین با ساختن اکانت‌ها و پروفایل‌های فیکِ دخترانه تو این ربات، در حال فریب دادن و جذب نوجوانان و جوانان برای انجام فعالیت‌های تروریستی و خرابکارانه هستن.
اتهام اصلی دورف اینه که چرا با وجود این مسائل و هشدارها، این ربات رو از روی سرورهای تلگرام مسدود و حذف نکرده است.
با این وضعیت و اتهامات امنیتی به این سنگینی، به نظر می‌رسه فشارها روی تلگرام دوباره بالا گرفته و فعلاً نباید منتظر کوتاه اومدن دولت‌ها در برابر پاول دورف باشیم.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7300" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7299">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dockerfile</div>
  <div class="tg-doc-extra">35 B</div>
</div>
<a href="https://t.me/ArchiveTell/7299" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
آموزش ساخت پنل ثنایی بدون خرید سرور (کاملا رایگان!)  با این آموزش می‌تونید بدون نیاز به خرید سرور (VPS) و دامنه‌ی شخصی، فیلترشکن فوق‌العاده سریع و اختصاصی خودتون رو بالا بیارید.
📂
پیشنیاز: فایل Dockerfile ضمیمه‌شده به همین پست رو دانلود کنید.
🔹
مرحله ۱:…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7299" target="_blank">📅 10:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7298">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📌
آموزش ساخت پنل ثنایی بدون خرید سرور (کاملا رایگان!
)
با این آموزش می‌تونید بدون نیاز به خرید سرور (VPS) و دامنه‌ی شخصی، فیلترشکن فوق‌العاده سریع و اختصاصی خودتون رو بالا بیارید.
📂
پیشنیاز:
فایل
Dockerfile
ضمیمه‌شده به همین پست رو دانلود کنید.
🔹
مرحله ۱: آپلود فایل تو گیت‌هاب
۱. وارد سایت
GitHub
بشید و یک مخزن (Repository) جدید بسازید.
۲. اسم مخزن رو
railway-3xui
بذارید و تیک
Add a README file
رو حتماً بزنید و دکمه
Create repository
رو بزنید.
۳. تو صفحه مخزن، دکمه
Add file
➔
Upload files
رو بزنید.
۴. فایل
Dockerfile
(همین فایلی که پست کردم) رو بکشید و آپلود کنید و در نهایت دکمه
Commit changes
رو بزنید.
🔹
مرحله ۲: نصب روی Railway
۱. وارد
Railway.app
بشید (با اکانت گیت‌هاب لاگین کنید).
۲. روی
New Project
➔
Deploy from GitHub repo
کلیک کنید و مخزن
railway-3xui
رو انتخاب کنید.
🔹
مرحله ۳: حفظ اطلاعات پنل (Volume)
(اگه این مرحله رو نرید، با ری‌استارت سرور، اطلاعات اکانت‌ها پاک میشه)
۱. تو صفحه اصلی پروژه تو ریلوی، دکمه‌های
Ctrl + K
(تو گوشی روی آیکون همبرگر) رو بزنید.
۲. عبارت
Create Volume
رو سرچ و انتخاب کنید و به سرویس متصلش کنید.
۳. در کادر
Mount Path
دقیقاً این عبارت رو وارد کنید:
/etc/x-ui/
🔹
مرحله ۴: تنظیم پورت و شبکه
الف) آدرس ورود به پنل:
۱. روی سرویستون کلیک کنید ➔ برید تب
Variables
➔ دکمه
New Variable
رو بزنید.
۲. کادر بالا
PORT
و کادر پایین
2053
رو بنویسید و Add کنید.
۳. برید تب
Settings
➔ بخش
Public Networking
➔ روی
Generate Domain
بزنید. (این آدرس پنل شماست).
ب) مسیر ترافیک فیلترشکن:
۱. تو همون تب
Settings
بیاید پایین‌تر به بخش
TCP Proxies
.
۲. روی
Add TCP Proxy
بزنید و پورت
8080
رو بدید.
۳. یک آدرس TCP (مثل archivetell
.proxy.rlwy.net
) و یک پورت ۵ رقمی (مثل
14841
) بهتون میده؛
یادداشتشون کنید.
🔹
مرحله ۵: ساخت کانفیگ تو پنل 3x-ui
۱. لینک آدرس پنل (مرحله ۴ الف) رو تو مرورگر باز کنید.
۲. با نام‌کاربری
admin
و رمز
admin
وارد بشید.
(بعداً از Panel Settings رمزش رو عوض کنید)
.
۳. برید بخش
Inbounds
➔ دکمه
Add Inbound
رو بزنید و این مقادیر رو ست کنید:
@ArchiveTell
Protocol:
vless
|
Port:
8080
Network:
xhttp
|
Path:
/assets
|
xPaddingBytes:
5-70
Security:
reality
|
Target :
www.samsung.com:443
|
SNI:
www.samsung.com
دکمه
Get New Keys
رو بزنید تا کلیدها ساخته بشن و در نهایت
Add
کنید.
🔹
مرحله ۶: اصلاح و آماده‌سازی لینک نهایی
۱. تو پنل روی
QR Code
کانفیگ کلیک کرده و لینک
vless://
رو کپی کنید.
۲. لینک رو تو نوت‌پد گوشی یا سیستم کپی کنید و این دو قسمت رو جایگزین کنید:
آدرس بعد از
@
➔ آدرس TCP ریلوی (مثلاًarchivetell
.proxy.rlwy.net
)
پورت
:8080
➔ پورت ۵ رقمی ریلوی (مثلاً
:14841
)
تمومه! لینک اصلاح‌شده رو تو نرم‌افزارهای V2Ray بزارین و متصل بشید.
🚀
‎
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7298" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7297">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7297" target="_blank">📅 00:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7296">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPwyUzIZlZ9rtTp1zhnTt64YpjwkOc6SYeeaMeGczMi9RMZEIpx1PlxUP0zlKFoSPuWIIf3xrTa8InN1RmwEuF5iOdAHw4K2XqU6VGmH-rmeN4Y0pnTUc49oKVL-zHNVkILR8qZinD3Q_d5ciXAUmrMp7xkwSuNp8HGlQxiLSWivN56cUQPrKQXJfT8M9it5YKJFfuQDsRouEIPeWYKfL1Sm0QfG_0kiY1nrK2fS0BVAtXszPb-ghMfpEdHijxAaaWEWj1YULCMUGZQRrqAaglroAPSJHCNKBvh0-BSVr6EalomGO6H-qbobFPwHh-pgI3gC4jzMvPX9yZqb80Q2Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
تبدیل گوشی Android به وب‌کم با VCamdroid
‏
‏با
VCamdroid
می‌توانید دوربین گوشی Android را از طریق USB یا Wi-Fi به وب‌کم مجازی Windows تبدیل کنید؛ مناسب تماس تصویری، استریم و استفاده‌ی دوباره از گوشی‌های قدیمی.
🚀
‏
‏
✨
قابلیت‌های مهم:
‌‏
🔹
اتصال خودکار از طریق USB و ADB
‏
🔹
اتصال بی‌سیم با Wi-Fi و اسکن QR Code
‏
🔹
سازگار با Zoom، OBS، Discord و Teams
‏
🔹
اتصال هم‌زمان چند گوشی و جابه‌جایی سریع بین دوربین‌ها
‏
🔹
کنترل دوربین جلو و عقب، وضوح تصویر، فلش و تنظیمات رنگ
‏
🔹
پشتیبانی از Windows 10/11 و Android 7.0 به بالا
‏
‏
⚠️
نکته‌ی مهم:
‏
‏برای اتصال USB باید
USB Debugging
فعال باشد. عملکرد برنامه نیز ممکن است بسته به مدل گوشی، کابل و سخت‌افزار دستگاه متفاوت باشد.
‏
‏
📌
دانلود و مشاهده در گیت‌هاب رسمی پروژه
‏
‎
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7296" target="_blank">📅 00:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7295">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7nn0rUFnK0wNdg0Dn0C5u-imlp29zT7f4F-zJRWSWUBugBk-nXQLobeEBr5DQ1_msbflawRpzRKAkBMwxthb3rNtwkM211EZWP9472WYzXmD5gsRVyjs_zdXNjeJS2ozBLzs7l3F5mZPuOeNHycNbbiENB5ca5afqnv6V-BSDth8ASnjsLqZWiC4W6Z0XI8d52UEPk0ELjaW3sJCNhZwtnkjVii3jWDrDTcV1KGn-7Keces5tRrxzBVdbimACU_cYT8ssWuL3oDp0_amnXGAG3rThH3oVmd2LOIw84ghqLcTrJTTKhdc9JyjxnARqr_SUow5CfdAEg-zGYRjFU1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
Shotcut؛ ویرایشگر رایگان و متن‌باز ویدئو برای کامپیوتر
‏
‏
Shotcut
یک نرم‌افزار حرفه‌ای و کاملاً رایگان برای تدوین ویدئو است که روی Windows، macOS و Linux اجرا می‌شود و از طیف گسترده‌ای از فرمت‌ها پشتیبانی می‌کند. نسخه‌ی جدید
26.6
نیز با تمرکز بر قابلیت‌های HDR منتشر شده است.
🚀
‏
‏
✨
قابلیت‌های مهم:
‏
‏
🔹
پشتیبانی از ویدئوهای 4K و 8K، HDR10 و HLG
‏
🔹
ویرایش مستقیم فایل‌ها بدون نیاز به Import یا تبدیل اولیه
‏
🔹
تایم‌لاین چندلایه با پشتیبانی از رزولوشن و نرخ فریم متفاوت
‏
🔹
ضبط صفحه‌نمایش، وب‌کم، میکروفون و استریم‌های شبکه
‏
🔹
ابزارهای اصلاح رنگ، Chroma Key، Motion Tracking و Stabilization
‏
🔹
پشتیبانی از زیرنویس، تبدیل گفتار به متن و Text-to-Speech
‏
🔹
قابلیت Proxy Editing برای تدوین روان‌تر روی سیستم‌های ضعیف
‏
🔹
نسخه‌ی Portable و بدون نیاز به نصب
‏
‏
⚡️
نکته‌ی مهم:
‏
‏Shotcut بدون تبلیغات، اشتراک ماهانه یا محدودیت خروجی ارائه می‌شود و به لطف FFmpeg از صدها فرمت صوتی و تصویری پشتیبانی می‌کند.
‏
‏
📌
دانلود از وب‌سایت رسمی Shotcut
‏
‎
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7295" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7294">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH3Ove6xdoZLo-l-wHlIFO1OPWtq4EcpWQFZa8iIn9fUXnhEZ7aEbcBLImGzghuUmo7YfbAfrCSrCGPldUr6A60Ay1Kc4_nNLWwFmklx7P9en-H4R8E7yGaI7E3xFnSaqP1jPaX3dJriM0kLr3Quy-_jOliDig4A_3E98kaKWL0Q7GuX3th738Al_yTSMBRbPooaOQQKCSyu_8xDZP3y4dUrzYVNTnQFFkzR0Pm_IxigXnLuMqU4mCm9OcUFYrwgjwY2rN2kBAVRImFY2zvxWoE67_wIQplDcGZJLguqNoHGCsgL7BnHMVOKWDTRpY8fqkWt37p2fWTrRKSCcjW1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏‌CocoLoop⁩؛ هابِ هوشمند و امن برای کشف و نصب اسکیل های ‌AI⁩.
🚀
‏
✨
ویژگی‌های کلیدی:
‏
🔍
جستجوی سریع و دقیقِ مهارت‌های ‌Agent⁩
‏
🛡️
بررسی امنیتِ ابزارها قبل از استفاده
‏
👥
جامعه‌ی فعالِ توسعه‌دهندگان و کاربران
‏
🔥
دسترسی به ترندترین و کاربردی‌ترین قابلیت‌ها
🔗
http://hub.cocoloop.cn
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7294" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7293">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb979dcf62.mp4?token=qf9TFO24jAoTrgL8SFuTxnOFXNfpsiWHPLHy0o9zuud1XepxoZwUcNwzNQhk6d0D4lAh202XuP3HB2zO9Crvr6Dk_YBjHt6qngRm-XjuXuaUNZbXlm9CNQa8j8TFLrjAv3Gha-ZSAfwVs5iIoNm4s7Zjos5x2mioADnA2YlctmF4D-fjlntR-n2qU0HOgkM-loWuMKvKvehQDHdbDV3lem2Y3l4-sQfre_VYDolCMoc723dxbwFYgVDa4e1KoDaz4t5aFuPHUVgtz5a-Vj22tlDeUoXSIh9P4wFgpNbgGU_sLM4h1MQfBEq59XOuEBSx3MN_X5WLJalAqzN0XIEmMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb979dcf62.mp4?token=qf9TFO24jAoTrgL8SFuTxnOFXNfpsiWHPLHy0o9zuud1XepxoZwUcNwzNQhk6d0D4lAh202XuP3HB2zO9Crvr6Dk_YBjHt6qngRm-XjuXuaUNZbXlm9CNQa8j8TFLrjAv3Gha-ZSAfwVs5iIoNm4s7Zjos5x2mioADnA2YlctmF4D-fjlntR-n2qU0HOgkM-loWuMKvKvehQDHdbDV3lem2Y3l4-sQfre_VYDolCMoc723dxbwFYgVDa4e1KoDaz4t5aFuPHUVgtz5a-Vj22tlDeUoXSIh9P4wFgpNbgGU_sLM4h1MQfBEq59XOuEBSx3MN_X5WLJalAqzN0XIEmMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ابزار ‌PromptCard⁩؛ کلیدِ رمزگشایی از دنیای تصاویر!
🔑
🎨
‏با این افزونه‌ی کروم، هر عکسی که می‌بینید تبدیل به یک پرامپت مهندسی‌شده می‌شه تا بتونید دقیقاً همون سبک رو در هر هوش مصنوعی بازسازی کنید.
⚡️
‏
🛠
قابلیت‌ها:
‏
🖼
آنالیز هوشمندِ تصاویر
‏
📝
استخراجِ دقیقِ دستوراتِ متنی
🔗
دانلود افزونه
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7293" target="_blank">📅 21:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7291">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آپدیت 1.0.4 کلاینت UAC-SNI-Spoofer</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7291" target="_blank">📅 18:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7290">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc_Fb2YNsOSRkETVFdGtmgUOBsZTAcIL43ymSnqRPsp6gQV-3ctO6olP1o6hJLfoJNRMG8wXbuOW9nHZg-l7u89cRJcNgu6EeDrJYmDd2eU8HIF2RgGu9xRJMoDpnFhf68S1C2mgmYeXR139d1dZ94E5RXmWtZQtm_fWTW6IJh_Ly0_YVAIcg88IjGFsOgVixVWBoxGdwTwjYzp-ncg97jgiAmBF6dViMicfttynQ3v_HAt0XClR8RLsBYJVrCsTLOH7nF5wbPDfkUgSYYibx24C8bdwMTt22o7fCFau0wy1kWks5fdaU8p-4DFmFlWFvrzDKlfYBaH2C5yrCzS_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  ایجنت روتر (سرویس API چینی) امروز علاوه بر Opus 4.8، مدل‌های GPT 5.6 Sol و Kimi K3 رو هم اضافه کرد
🔥
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7290" target="_blank">📅 17:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7289">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeSrENYJ5Td6AICEZHrIlzG61aS35mv_iek5_i6bpecklE2S-sgsnap_goTeLa-RJFdvb8Nqpq2XjdQhCAYjJE68y6JxaNSr1WpUHudOIMIz_GIP3KXfnkyXk3sPJahXsIqCtNoemfz01HwYcTc-uBjysiuGe6nkK9sfWqNMorXGlO5nh3RK3czwI45LSIxBxS8BKyxyUyTENaFXFcoGXyNlKCUxTsTTS2wIZMrPITMbVCTiro6pYBAkEHCE0ZhbZIpqy_fXP1-kav_qc9Agg8zH6w_-LKUwb318eKuxpXFn5wDBxDtZn9UtEymM2Td8alfTR8UOYf2uxKWaxdWViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💸
جایگزین‌های رایگان و بدون اشتراک برای ابزارهای محبوب
‏
‏سایت
NoSubscription
مجموعه‌ای از نرم‌افزارهای رایگان، متن‌باز و قابل‌خرید با پرداخت یک‌باره را گردآوری کرده تا برای سرویس‌های اشتراکی، جایگزین مناسب پیدا کنید.
🛠
‏
‏
✨
چه چیزهایی پیدا می‌کنید؟
‏
‏
🔹
جایگزین ابزارهایی مثل Photoshop، Microsoft 365، Chrome، Premiere Pro و Zapier
‏
🔹
دسته‌بندی‌های هوش مصنوعی، طراحی، برنامه‌نویسی، بهره‌وری، صدا و ویدئو
‏
🔹
فیلتر براساس سیستم‌عامل، قیمت و مجوز متن‌باز
‏
🔹
ابزارهایی مثل
ONLYOFFICE، DaVinci Resolve، Brave، LocalSend و n8n
‏
🔹
جست‌وجوی سریع و بدون نیاز به ساخت حساب کاربری
‏
‏
⚠️
نکته‌ی مهم:
‏
‏همه‌ی ابزارهای این مجموعه کاملاً رایگان نیستند؛ برخی رایگان یا متن‌بازند و بعضی با پرداخت یک‌باره یا مدل Freemium ارائه می‌شوند.
‏
‏
📌
مشاهده‌ی کتابخانه NoSubscription
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7289" target="_blank">📅 17:30 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
