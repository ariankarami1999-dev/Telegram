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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 15:56:08</div>
<hr>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivJpf7zj5w-Zy5c9b_aFKPfw8jwOD8b48CpvkABR4ABZ8SpBXTM5c7kWOHRkvd5XnexUweP7eIQD4-74JupGmdz3dbbP1q-vHfOmKIYHOG95G79IC3Oj--Dar-1q6pzh0jR2tB9ro5PYmJH-6K_uwC7PQeo64b-rTOhf20ckQWLv4ftKP83IuoMBGXF42V55-UX4ywOtIuulf9kwBzKHBtWCY6qOK6bQOifETzOcGsKdx6XIlBDA6VjpNmXWhNUbgLnHI9WNJikZrcICnMl2QQB7ba96lAYHCIHv8zH52AnUJ3_yjvlIaYuJSu8M0dLF0aOPgKxe0RP5vc66aj0LKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به Kimi K3 و Qwen 3.8 Max
❤️‍🔥
🆓
بدون نیاز به کارت اعتباری کافیه وارد
app.clusy.io
بشید، با ایمیل ثبت‌نام کنید و توی پروژه جدید مدل مورد نظرتون رو انتخاب و استفاده کنید.
😎
⭕️
فقط ۲ روز از این فرصت باقی مونده! به دلیل ترافیک بالا ممکن هست سرعت سایت کمی کند باشه
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 545 · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuFpV3Nh56Zb9NsiPWYAMfTo8Hctsh5j9fumWTwCT-lDU9pmvVgS7yDekPhWNqZKAwbyb35FEczxhvCRhggp6uwKaOUF_e8E9CJPHGdHXnBKnaCg1OPJJyae78xzI1IB4pMu0YOZy23wTxGRu9OcmOc6Zj3ftXOSrpVwHPvgeBc9yzcgduwC76EcNJhFZ0IGnaIt9pNhSwC3WRWhnd_Wpe_WBp54MAAiNCy6h93FjZS610lMtAFOvgJ64a_LPGuGJrt6UrSeBvbM_fabI9RhjY1bwZw0NpNiQOFS8aJiK_1gQaf-vJ9dmMruP6MY59EIJgPirZvwkSzgXsU5rN7i4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان:
امروز از ساعت 12:30 تا 20:30 به وقت ایران
⭕️
🛠️
مراحل راه‌اندازی سریع:
1️⃣
وارد
سایت
شده و با اکانت Google ورود کنید.
2️⃣
به بخش Account رفته و اکانت خودتون رو از طریق تلگرام فعال (Verify) کنید.
3️⃣
به بخش API Keys برید، یک کلید جدید بسازید و اون رو کپی کنید.
4️⃣
برنامه OpenCode (یا محیط دلخواهتون) رو باز کرده و اطلاعات زیر رو تنظیم کنید:
🔺
Base URL:
https://api.aigate.shop/v1
🔺
Model:
muse-spark-1.2
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e59uHivCjbs-67TQOEufjJJEoHqOpuIGJ_33-BHB5rYUItLHAf_tCrTfdgqYf6VMQVI0cYQTqbyWxegxnjm1eSt3XTeHJVSYhbLASbqopmvAPKSS7yu-NTNPf0Jk8Fsl_BTjO8YCw0PGZE9Hlhv5g7zYkvVsH8k2ElHuQbFVxKKE6lGy6AKWmu7tcNE_Duix-GCnvYB7ks5CTcadbtu7Y2GyDbGZ5-gZSaOWSMvT7mCASfAfIaoc9Q6HpodpkhtSB3oXhYwA7wXZ70DqrfR7TGuE66z-McYjQxEqlNPtnZGj1DRUylZVayi6AggdUF8GhLX-AjpV82JWJgvwD-mokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ‌سیک V4 Flash
به‌صورت
نامحدود
و
رایگان
تا
پایان
سال
6️⃣
2️⃣
0️⃣
2️⃣
به آدرس
cnb.cool
مراجعه کنید
➡️
هر
ریپازیتوری
که خواستین را باز کنید
➡️
عبارت
@codebuddy
را تایپ کنید
➡️
حالت
Work for me
را فعال کنید
➡️
تسک
مورد نظر را وارد کرده و اجرا کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 989 · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mw_O_mtXbwJQ9Lu69FxU3kMebHh-k3StC1Fx2kVDtSZv7TysR3rWTyPGLsyZ-Ata56jQrPGSn7QM0ypPV8cpVkaHpIdDR85gY8IW_fHLQWskuRGxzZR5aPzyNqRMh4_OwJXsNhf0sRxSkibmkQOAMFkYPSQJQJ2ugOsbc2c6e1jgQjLGXqN6LW-l_zEji7bhEAg2gPaHIKToDgfw8eb-Ajr88n1WPEPxvxkJcdIeI1G_nPUBjpauyLT5LcHWS7BY4LnIdAUoAhztcqm_Ln6Z8H7v7cjLUOfw3dihJWZdGWBxc5mvqNYHUHT5ehQfxWLr3jaPnxJ7bRg306iK4KXQ_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flvAeiLud2qBxH__tfsAMI4h4pI6B1WeoJLyHmRqs2l0gsiXQXxIqSsMPJvo1hikyWP8dFqTwwV2b37r0pQkS8BcOAACVceeEE1yQdDoY_oLcu97PxdXaIashLOwHN-GUEyMMi7AMudhHe1GJQ5XtV8mI_lYhJdkIi7UD26SSbaH2NTJU-HelsdFCca_cSbKDAXDS1TXrHOU78SKKhFSukoUjam2CKdL9tvIsQKsDBwCQix-4r-JH62zQNsFzX0wcKNtj0_oU1rGHArp7E_E_sByMmU8F4Oc2CyZAXHkcg4Mc7E9zrx9ytEvOtQzhyFPCYccqacCyv6oIt1BVEJU6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iebh8NIdxc4K0CyqXS2a8s5VSiRVNmaJE1YcknOI_JjK1MgGz4qgMJDLQj6frxI_kJ6p0HthcVVCAC7B5a2l7lAG6FeeIHxrW7Gn94fXcSt_Sh_NMSmez3rahnhOx8TiDc9tVJ9sVAW1MwjGLZr7SS_ZfS1jw4REwWpHoxlNwXIs1xZkGm6BneP2mpmtHVRo5zvHtCjMHo6ALk94hbP83VL-faJoopMp1UHlYbT_gAXvTBnhizS9mnMMRbxH5jyGNArIf5xI4fHPeQstxeWOSw3b1_Fp0ASYv6xZfM35TsYvY_tsgF8oCsvWfR_mBLp-0COkhvjjNOQL31fny45o7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8xbrDai3qNBtduJVxYnHios_-pauOpdFstyEOxh_RYLykJiBI2u7tbU-CPBNAoV6LzB8qB91bT37cAWYcJBPQ_32VyAnzVzKZhGSPXXWKlf9Q2Hki_XPE25ybzD_2czQ-tb-jxSwwyPw_DUTuzsvVoLmrBNPkh08eoYBlS0NmxhaPBvOi5IgFwvKRtIQDs_xXbWFiJygCyrqaK1kk8fJRIhmfxI5iCu0gKEJMMNSfgQGHDryRpIF8yDKT6uwBNc7G9tnFbg4i9XKHHaQJ117M-G7MMBevFFPaLlH0yUEO-syrKudVx1_r8XEXNM2VTN3xyTy96GT6v1SWrj7x1vPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=p_jsBU6Nbf4GGQ2jFMlpoT6pSYJX4HbB7pPewL-GWpgshc8DHZOV_Wfmba_qZg2R8Bf3mzNMfyxEtj55a6N4-A2kHaS3TBFOA3fxzJ-0vvyqzEmDaR1XY0lZSc7iciRfQZHu3AaIgUUWrywzN6T0ccsIU2_4dMDPtpdKzJLrRRzyj_DVC1RbDcTbWVyN2q4vR7rSw_v2zPZcAEOuh8AyM7J5ZXUsF9Jsx9uiwYLyV7bGQU0NEoDfmZi0qqA_RFPzyLnSJFJB9MFjTPgz4u9m7IPbG6SQ0CA4sRVWVuuWFJDn3rn_bypt1W_Iz6gjeFvqFddHbxVw5lruDURhnndGoDTHYM2Bi3Q3ySvCAuegm4T6yY2lwWN8XeKxx_1HvhMBSYKCorgtLkmm8PDo_rKvdyvnPpZpXJ0ib9x6Vl8uemp3e52xGJ7G2puhcwfv5C7tiFFBHlcoeo3Xap2x8o81xXM2iYqkbq_-ual3jQccf9v1tHtdbxUkLBm5jLa0zjm2d81W2NYc-d9qzw7Vb5u1urBiWwS96JkAaLeUX-_c_0uS7bDm9hREAbKFB52a8s2AYSlOqUX1B0WCjOkRy2kHVunw82vyGTwMQqG4DU3Rk_6dXkUHQpGbnqnaSqNRN-7lbaLcJB33Hf1nkLlKwtcTdSoQrtxAwyAqUvZqN-PiOiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=p_jsBU6Nbf4GGQ2jFMlpoT6pSYJX4HbB7pPewL-GWpgshc8DHZOV_Wfmba_qZg2R8Bf3mzNMfyxEtj55a6N4-A2kHaS3TBFOA3fxzJ-0vvyqzEmDaR1XY0lZSc7iciRfQZHu3AaIgUUWrywzN6T0ccsIU2_4dMDPtpdKzJLrRRzyj_DVC1RbDcTbWVyN2q4vR7rSw_v2zPZcAEOuh8AyM7J5ZXUsF9Jsx9uiwYLyV7bGQU0NEoDfmZi0qqA_RFPzyLnSJFJB9MFjTPgz4u9m7IPbG6SQ0CA4sRVWVuuWFJDn3rn_bypt1W_Iz6gjeFvqFddHbxVw5lruDURhnndGoDTHYM2Bi3Q3ySvCAuegm4T6yY2lwWN8XeKxx_1HvhMBSYKCorgtLkmm8PDo_rKvdyvnPpZpXJ0ib9x6Vl8uemp3e52xGJ7G2puhcwfv5C7tiFFBHlcoeo3Xap2x8o81xXM2iYqkbq_-ual3jQccf9v1tHtdbxUkLBm5jLa0zjm2d81W2NYc-d9qzw7Vb5u1urBiWwS96JkAaLeUX-_c_0uS7bDm9hREAbKFB52a8s2AYSlOqUX1B0WCjOkRy2kHVunw82vyGTwMQqG4DU3Rk_6dXkUHQpGbnqnaSqNRN-7lbaLcJB33Hf1nkLlKwtcTdSoQrtxAwyAqUvZqN-PiOiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jox17-_HStcR4oIiit_MeaI-Ri7IbjJb-FOCs3PD1SscHxaGwKy_KOZ7YYp2FTGGo32KAZT_fETFKKk3vHMYQL-hUcccdmRJRiMFMkhusykujqTfJWYHciOI51ZI_wGdvqVwNf1QNUEI6v2xaUX0TYak1BWfU-DzXTZjDQcwbviZ7gT4eNQvlglqE6zNlEPFuV1W5JaDCLV7znS-bPBsxcZiMrd0MaK1QvgEjNSS6g7shcpKs_5M7vS9DFnsmx-w5cd21MhdgZoq49FIxEi7g4p-5tTJq-jba6EUhrpLZIOFSyq0_sCPCBx8bmIiw5wa61yOK1e-HVxy76B-VQooeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwxeek7ZB5TY8f58tnKcbnk_MV0i2z7VrolJYrT0AVBLtJfsWF4TXc-XSlDmCrdeV-agZhpcvtA1w8ET3ExeCj397_4kzr20QBBTnf1B08Hzm9tZNi8w6DhMG-kf7mdWKnIeXmwfBqUMmbe5VhZPXN83waP_3284lZnHGXp4rjOb2CES6P4Muh1YEFIR_EvwjN228NeJdqVD3JNcmgV9slkjR9W5ZgSC46J3tudzaMpz3xSlUu232a0zE7aEdwBtpNY6UeKLu_jfk2RXGNGWx_tPzonBEx357NQ5rKz3rPUtWrEE1ubdPAAFwfcTmO2iZcxylteXteWZ2p2YKkxOQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhQ95NUxT0LuWK_bVih6xluSqls6s2ZMTr7sPKeOuEiGqfbIvnQONZaOrhMR5OdLCVKIakOSmXJvkaKhEQxYO5JbyfiO0UIkUiiM5ePiVEgMzcHZvXgy4H7WhcSpk1oqI08JogmPCgRDqHzvW8rV6jjxAL9ODyOStOcgKL_ibyUZ_wP8TxnmS3RGT1ezBpvMDu5Yo6zsD5aOcKzwmLsc6m0_6AScjlCwxXJd2gvcK8Y9NUHkOU3mpMtLMYcD2JFgjYGIJsC7mim0oZOnFmRbB0yn6-ErT9YOUlvLbYn_ajt8_UY7wiN9-rYdkYJosyRlnHLs9wqYpx8EeuT2R7bAew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wf2fep8E0NCT3KgXhszigNo8hf0q2U_1Cw27J9OEiakHsfeGGJykZ9TjsLvkw6WGoE0Oh9Kp_vUZEbCUbVJ8kPnwofc1m88EMO_oRrMsAmSJqncun_YQMF2ulzA0j-eMeTDm7MfGqJUXTFUtUIckpGphotc9UXMVF7vLjpttigJ9aB0XxqZy8qzjl9UhCY16rKNphtBs9KtJkzjebkV6t5Kh8NxSy08rTS0UYuIS-OjUswdrYDcm-aJ96ZeOgCzsUdk4Bd-bH4dld-rtoWPnTnx0ySqPZtAnGKqQg6nTZy5FOJoPj1oq1CJ36dN8eFHyUCxLf_yHtginj3hcGgxidQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=j22R7KbXSOdB_-f-x96dLGwtk82BHre_92TiHTBquE_gAZXS75Qdv2cAHncjZyZ5wKA_rocj2HS3fICCentnWDaJxtVdy0yfFQWQLN51x-ZqtVdvQ43pv0QxH5sTaVrAop2sDFZr3QZxM3RUIbtKJ7n_ebkp6vB75DfGWpj30S3JaqVzyOAedelpQ8KfsdCwIiNa1f4Zp38KhlGuNKEWTI9IwjQNrTr-AZKXGyxSq0tUy1KEFgK5HMc6OwDbqgaSrag5hcDl6HIG0aeK9WSoekleOwUndTSy8O6fYlr_Rr-83kK9afv6OmkJAEV36Vc8H8Woyhp2XiRCL4kSUas-7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=j22R7KbXSOdB_-f-x96dLGwtk82BHre_92TiHTBquE_gAZXS75Qdv2cAHncjZyZ5wKA_rocj2HS3fICCentnWDaJxtVdy0yfFQWQLN51x-ZqtVdvQ43pv0QxH5sTaVrAop2sDFZr3QZxM3RUIbtKJ7n_ebkp6vB75DfGWpj30S3JaqVzyOAedelpQ8KfsdCwIiNa1f4Zp38KhlGuNKEWTI9IwjQNrTr-AZKXGyxSq0tUy1KEFgK5HMc6OwDbqgaSrag5hcDl6HIG0aeK9WSoekleOwUndTSy8O6fYlr_Rr-83kK9afv6OmkJAEV36Vc8H8Woyhp2XiRCL4kSUas-7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-Z36HDfXEDHqHYPcAmGO2KaxLjR3vYRrU8Yaw9mpIwoIBFmdYkK9MNjSCBaPRArPGQFuvdNfpcZpEjvVWQBf7dHHg2Tk4E630ZbKdXgRJj88qglLSnJhxPCX-S1QJ8smAhLVsIVRVCdRstTA-dI11G1kLgKunQmASWudI3iQBRvzi2vk8pdnK0EkH6swpPxV7gopT54zvFJaZEY4PjIpzdWrDA9djD68R7NV-uWcYGHldSW19X80uqXzhrtnQBLBX9DW-pRjXRytgy7-sH8jqA6MyKW445UbjzfpJsxR3z77wiomGHPuNCbr1PXLKvp8eFjmQ_m4tScjti89_WKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2GUz9Hvc-3EmhxVHG7fWO8g1-yI9-3OkyJoeHsSqzKTZ4h5S29PcAItjdj7fDuTLaL7Zm1tsKxNZyW0hd_3N6BwLN0oLNkPf9j8x4sX5cb-3EJRidBoZdvCThPppwKF895_aqtBCzsMttx3-8cpjOTBlr8-4_-xSx2zOwoqdO2bnvNZMWdQSqfVYPHlmWdDix8g3whieeG0FhzZ6guvX42_md3USXO4MysTp-9ABu3i-z4YgGYw6kGZ9c9gyfGa9QZXqHET3seAPmISBSnEOmarV18rCvN7b8Jm6bK3UTmt6H5xPvdHhbeupeZUa4eg5DJgGyU_TRSIE2U-vZAAC3Rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2GUz9Hvc-3EmhxVHG7fWO8g1-yI9-3OkyJoeHsSqzKTZ4h5S29PcAItjdj7fDuTLaL7Zm1tsKxNZyW0hd_3N6BwLN0oLNkPf9j8x4sX5cb-3EJRidBoZdvCThPppwKF895_aqtBCzsMttx3-8cpjOTBlr8-4_-xSx2zOwoqdO2bnvNZMWdQSqfVYPHlmWdDix8g3whieeG0FhzZ6guvX42_md3USXO4MysTp-9ABu3i-z4YgGYw6kGZ9c9gyfGa9QZXqHET3seAPmISBSnEOmarV18rCvN7b8Jm6bK3UTmt6H5xPvdHhbeupeZUa4eg5DJgGyU_TRSIE2U-vZAAC3Rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVgK4UPlbnRT1TYhLMmEGtBJpWSxitABI8FK_qJoutkaZxvkC7M_5iam5_s7_nqyhHl1no2BMLSE79IDmeO7NvwLrS1oK9XCGu_Lcr1l_ktXpskEz8Zi7Vr5dY6upc1mAAkcHJFzjgfSG_cgE8brokqmsDZVbFVChBFJF5VFl2i2wH6eGEm7kbcYEC_shtHmshLEaimlnb98rBh72_nwJiLgz6TjUxIJfOFYEJj8hobmMizwYZ2yuLyaJn3jBN7mYZxNokaEGqLEdpjGHXp1LBIrzj5-uIjJeb6OyUqQYilFQquYzKn64C8icy-m50_eyFR0VE-Y-ypuVP7EGzvR7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8jPQiKp4NGjzEimG49_te91X-_0caMJNn8vVQc--JVqvtuH5tdDO8Vnx0Errt1KTAT7iN5J5inV0Jau_ZRDFy17XyPjGMlh1u1xwqYhUQReIkNdcYAKCRl1ywhIz21ykAXG_Trk8ae3Zx5t4CIbBw2saqd9ozDYloRFbaRtu__ErqrutIjsdla33rkRgq1tAmLZO_2elodMu2qGLQ-EQqUxE8uWukGDJFpcOZLaQzX_APYWxZSo2oKUbcgg0tq3tV8igwrDjVZZlSk3PRGvbhKu5A-kRpxHl5HzWz_WhbsPW0f_uxtqaV3nT8JQ6DulQWN8bJouaQgZtktZtQAtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fi6gqU5J8r_ziyjBuymbiOzZdd2TA2QkytXO1fm_mQbXUKYfJU-L3yhxAkq0DjW2cuP0XUWRBgXE4-CIHuZOF-vsDm1LKgP1y8AR5rKyCqtj-r_w-x3d1eYeVSbQFG1PzCf2BlBd4YwV5NmnLM2aipScZuHy36VIdk7jt09UyNnGfePIkgqaZVls84qF7Q0jDHe5z-9tZCLp4capEnnN7q7-_NsPF7np6jDScWnFMUMpmIbStlulWB-z0PTNV8tuUVtpD6mKuvhW2OhgeA6v_0tv4xrlWmGiOQDYBR2kWZP5X1QePtj_-sV9293D9kmVfQVnQk-cEkkOJCiXBjI15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcNiQ-upo-UXJ9JEeGL-FnGOR-P-cls8ide_N3IABaLfUxQUEuv2GYM_2ojQtOXOZ-gd8FbkFQwvvQ4Wl0BCWiq8AaSIbKhIK5eMdUPjaAbnbqmv9cBrboS9EbO1NK4ypS4zanYlch_rxogR2oqDKswiNAAhqRUhb1PjfA5kQIB3CNJqFHEphlUp_eJkz4opURLqtiMWuuWXc2wZdnOY6TLcZcOp3Re51gMoGuxZWQfBbzl6zQrxRKrtwHo1kimp1oRKpN-1o2zoy6GQoRjlTMupCVfnC4taeQNI73VbzX4Xnx0C3yCopcyu2snQ-yOWDrU5_WAPqZ7WonN_Byhb2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NScGf_v7Uwm_zNQ5iWejsRen9fNCo9kbGMqQ-mcvZKstnSb_uESStWIC5m9gOY50yvoZwEXilPtu5IJNBT6rri9wNgjjLCdK2mWRk56lA4niD3ZQPaRHTnEqO8L8Bnc90_QXVYKfv58fw-RjntBpkd5HVg7MRoUDKLpdpqyelrvCAY6rS8fZ2UaDe1nJ1DJr9wosiHb92uSNHfds80mcQVynEMGdtz0N12G8nCVopIz3q2KK_a0afZMEoYAfUM_Xhg6TNICsC0Ftb4eA1fZ8iWftZ1jBOgOEm137jj44ndRVoX9luIdXLYGM8fZ_UZeB54WL0wKBjhZn0Pzxpob5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TT_fTzKxfM2oe2M_ZXCBPSlcuZ6GLPYqPIKIbPVGlPtEM-ARFKREh_V-czG_FeEZZNdO8HXAxktUfHfOn9j6s1HEb-PBTlPEYSISUcg-1oIxBqM-8qC9pE1_NZNd79MC3KiKV3aH1CD2uL3304-j4CQs8NPqIz2gb2ZxGN5N4_1pH0S5V7PSM0Bybjlv97q4RRApWs0O3YjPSM-HcVk5ZyooNukClvSh-fqLIgyJsFrsEjHx1nBR4do2lfKSVNJvVQXKTQssFrXH9qBDnGYI3Kp-wvmoLpL_zXKSfy0QuGwzJZ5wxvmdyUB6CbtjCybbWK5IdOS1L6TbQ9VoKH-n4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/in3dhAJW5aqbRKP6lSWIY3P4D8H96P5UbrJj6JkPS3hwrM65Roho1daQ0TkCuwN3SqMtTlYBTaPxPip1jHL_hgeZ6QggDcyJmhzqkWp3MTkzTmfXT-j--D0t85rwhLvQ94GVJhvA7IUza9Ix959279bM6HDtwByFv2dBzi9CHCrrOd19p2xStiYx9ZFtMMVkQX53mot1TvqpXw-o7MvNQEDdg8E7OQ4pigm9l5CN0vqyRYjocUu26vUmVH900IuwL4Y-rw4JW9mmcAP8OVKhqgK6E8Aj00p4sA5nq74HxZtMEktIX6PyiwXqZAWi2dZMs18_7GhToO0qoEn1YkwdBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smYDnNRqAzGvTezynUhXld43v43UI34xOsfQYKNSHUop109NeZgaUPbvcMTxJ0NKmZeRh8xwKiYinCkgdOHJAns5nNmkgpGb4qH0CYaAPvI-Msqb7icQMwRHptnkbzy3OHiE_KrNRnhD9BpM09Bdp5oyKOitvOgWfGMSK_bJzf7jOLpkOh0LgHwRHusziLSs7WEp7pbP7AYZrG6mwsx-WyL3XNupGlCASIZxyjvmBD46nbFByNYDDrtpsxkd4BB-0vjNDoOIst89u4IB-npX4G79PbOm99Upi-vGbkkXDxVUrpCftSVmc4reudCvb6pEwZq8QA8MaHC_M1Mpja9VXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNYvVeYDAJ8jakxBP8XfAi3LIVZXhN-SUen-LbqQ16JiGzccK26pKA8PWWKUwH7SpY9aEYhvoM1n-NLYt-rmYfNezgESXk94y0qE8hgw5PoBecCSX8n2bzGcI3eYkpUODc0y6MNkrUE0CxboIWSQHHwje2ouVRsgC_RBOdgQ-uUo5FvD7DHooWPh6FNHD_AZxgGEqrIEj4XvQbjAnhCnh1ZTnOCxmLBubASRfgg6hG58x4kXON8cteh1-BagXhXidRBl9CMC8I-fdZaxiX3SRw877RSokVHXfo_ZprPVF0g3BkNnoO6n75AvvAj763BTxyxJczIS-dw4itB3vKwl_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7337">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7337" target="_blank">📅 21:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بالا باشین بچه ها عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7334" target="_blank">📅 21:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7333">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بالا باشین بچه ها
عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7333" target="_blank">📅 21:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7331">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7331" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7330">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7330" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7329">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ابزار تحت وب «بهینه‌ساز کانفیگ» برای عبور از اختلالات کلادفلر
🛠
🚀
بچه‌ها یادتونه تو پست‌های قبلی آموزش دادیم که چطور با اضافه کردن finalMask و cipherSuites تو اپلیکیشن PattNG مشکل آپلود رو حل کنید؟  حالا برای اینکه نیازی نباشه دونه‌دونه کانفیگ‌ها رو دستی ویرایش…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7329" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7328">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALMyATOrrC58QCAw7UjRVrTV6ouVSIED4lHiTZ5jj1uRHAf9o1G8C8CV1h3SHePGen-r78HGaHWt9oaz6lLOxd8Irru780ttzxjwbpOcWdxSnJGCb4mJbSTqtsnCa1R4wtToqszJR54AY3k5hy3HL3TKnHsMuNnWBVKXE1GZfzSvv6qegv4mnHjR5CHmWpCygzayX1l-5j77D4xOGulKxTcG0AL95VEtrfZGPu6wtTCfAWvSxYahbYtDL4N9tzVwFl7QuXPau44WJw4m47WpDl9kMciqAKLApufHx9GF8R7WkGe94vR8w3APociD-N7OL6KrZIXw_6hghGxB3IEilw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7328" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7327">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG: github.com/patterniha/v2rayNG/releases  ۲. ویرایش کانفیگ (
✏️
)  ۳. فیلد Address: یک عدد آیپی تمیز کلودفلر  ۴. کادر finalMask: {"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"]…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7327" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7324">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UN4bURg0vSdsURClXXvV8kbIl-KBNVqMjhx8biAtGKb0G4HTcEpMBwXXpW2hu0v2H43XLR7aZ6uoyO5E19wPhUB14VFOsMBFERcXeBUbHzmRzMMIS_5fT4OWsxPrgeZ8Y4oYZCX8vPSAhBAbJHtl30wAEK537u3BsrchA2BcGIDJ2AW0wntlR-Q3vYx2TT7JWMJVmRNLEiJ-yoinWzOE4BNKWJNzKeMKA1_K42qbj_yWNJa_bXk2VO_zdcv46QKrhKYEc-3d22FPEFir66dggVe1ZhvagEd4upkK94UuDWGYTfi6_FxhOL1oXvFwNMxfzu0OJ_sl10pc-LDGakJQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QBAyMHJgvrlIgqGg4Vgc4vyK8-2-y_FCVZbAK7lkHudqULhHBnLWATa2T03eCliwer2c3tYfkKpe_XAC2p4IfwznQNHCOuhdSHxzK1m1d5-hvG1ZJawVUyBkEr5_AMcI_LmIA8XNF-gPXcGYIuQE1XcnpjyJBd_YNn5PR5uoJLnaKM5-VYkknyovhGLtI6YkzzjIMQwoAtNfyEIdZKuJBwwxWKsm2HeDBl_lwi8THXZCaZSbYy__uZiezAbk5K-AMsBmcdXvwMjFiqU456vJV-lxlXF5PX7qzCeybMau_cDD7wZ_wF2eyNK3gmKwO0sJI4PREyA5dv-fYswqmTI0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SXPS7wFrFYMRL_5prhBhvxQA-D0qKX0wU8BoL4wZPm_CRILME24ISEHj2OVgwM2TvLY_pUpkqgLtKPPctJXYi9v5DkGxUqykBCZUY0bIPdxnsCLeqdi1w9OjX5WuPqVwMFr0Pj2i-XRbRDj_1P1lpOfDHkdSphPiIIfcvB_xmfQsgX1tWRhM-zEszRHupmtbHYlS4gkcbw8B8dmXiuEjmbhx4XzIMYVQwL9V1Fv4a8boi7_pwSQhpTnoubOxavjHuN9YZw6nKobSIiFBeEATQ9ep1XKA6QjOf-dPSSw4j0IdlQI-eEfAScZpedxN-R3NYnqe1Tdpa_Z0uF_vDWzl3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7324" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7323">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7323" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7321">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7321" target="_blank">📅 01:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7320">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فردا شاید ی سورپرایز یا دو تا سورپرایز بزرگ داشته باشیم
🫠
❤️‍🔥
(البته از ۱۲ گذاشته ساعت)</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7320" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7319">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7319" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7318">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoHi9vS-OONnKnu2DXzGAPxrMNnJNB6OzMv5moTEGtrZwLUs1eFl7EcMidDBaKYU9LMKMkbD89C8iJvNiA0Zjc6tC6XKG_TvE5NrpSZnzNP0nsRjttGrj-0sdt3Ar1OBz1jqKGTeDAcw8HAue_90NuiXfB_6Gv_k0gKVS2aPXLrWi4B2lblKWe7uhUeLgrkPkx0RhKBbC9q24OjfBGpvMX0vU94XWiapwgl-5aGeWrkhegQx-_BUzGvpVaDzqnUOSbRjaOiafuOXhPzLaNcfrBg3xY64bWQT9x4W-m4Lt6K6gLN_piyU7j_6RXUCew8Ww1DKcCWBg0iG5DOjv0iOkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7318" target="_blank">📅 21:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7317">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8hIg8mSLr2FppfvmMVMQZauEnYMKVJJNaGBEesnhvOe-ttkX0izsbJ0QEYeE1-z9lyGEDzMkkZTMBM9vmqr6OzYYRqBGe-MroB2rx7O5_iUZjwN6ketW7UWnAm-1hCZmTULazq8XVLeeRmsG5M3x5yfuil_R0hsPiWFboK9zTqwyLZHFEN0yqzfYtC8mLoHvxv1EjAh42xM5l7p283tiS_IUv2WpRU-dYBZE7iD99h2q9bH9gYu6gJ4ajiBVX504W5ySlkGm8-ujjRTPXb5DLVzQnIZULsubWTAKqUu3-J6ngGopl8zX9XwfAw9d5qBvpV8JNwRoSvViMSm_XAzwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7317" target="_blank">📅 20:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7316">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGj6IuDh-FImghVabnRA_cDcEmrxF0gEVR_khJ0jCEPeH0L58o5OIn8qtElSkOKrlj7xsbmeVy1S862gX1NoxWwgiW0HDoKx8if26MVN97r0mgIOiahLiigPpa53rJbIpTyl4h2JgVAyoynWWSytuDFxEwYLL6gAMogNj4o7dLdHIgiHvhwufu7l4ikmK1ldS1hUlkd-_7oboG0cBPfBIm6Pl_NY3azg4J2cpUJ3hLz_R56OsPQPKwNJ1y2p6fqaxDMZnWhdvNANKYeAugmgvTjZ5tGJOJj-DF6x9Tixce0nsMt68rgGGOILOwJwkiC-VC7zaocuclp62xmbx7XnzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7316" target="_blank">📅 18:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7315">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یه پروژه جدید ساختم برای 3xui دارا که خیلی بکار میاد
دیگه لازم نیس آیپی های تمیز رو دستی اضافه کنین پنل
یه ربات تلگرام هس که به پنلتون وصل میشه، بهش چن تا کانال آیپی تمیز میدین، خودش خودکار آیپی های تمیز رو از چنلا برمی‌داره اضافه میکنه به ساب پنل برای تمام یوزرا بالا بیاد.
سورسشو شب میزارم.
تمام.
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7315" target="_blank">📅 14:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7312">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLYsm9VE4RQZQKAsS_6d7ZYj9BQ6_MVJKD_4sjo_c81fwPgH6Kxg8fRu8LsM9MwDkzVrJm_g3NQ1oufBwsAkuFnavVcRhrKCLyWXmNT-zxWGUcwWXAfeLikQqkfpAjwoDQBvjpOxbZhoJMt0aC2U6sdOZikG49U893ZfxYCx5jhYZrxYXwAVC9512NzQMm9k88DJsy4AyGQ5CZN4lQk9LsI0XkrgtSFzAeAO4SWHbHkd2isatJFrU0H_c30p71BpDhw9JDyxIm0tKh-y3f30aLEqVt8iGbEfNUR5iZwsvaUEGCqq7UUv40vgcxsCua_RQmWExBrb3VhQ86_6zsYXXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7312" target="_blank">📅 12:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnEe4ney8W4chLHa7cYw5WyOy5Aw8QFci_RSJZGk9vmrqDxrGTv_gGmKJLn8iNKb_AcWN1J_Qphjq0HKTEAbfKW0bXossLMudnQZgepFj7Z_acIbUMmcpkFnTfgTyHR_5k7AVnGF2i4J7x9DXxNbrTAn-_U4cDcKmjN-58orpeeOt8JJeVHZcb66cSC0OyiGXZOlKQ5P7_mZI4C48mXYSlFFWR4GWp2aIvFkSEWEaMAFlPsi0emmCx-Iaf1A6HGYuZWGbn5-vUkYWkvX1sBADwFoPH7k6aDR6qj4kdEDGPHbl3lLhDlWRJdlUxQPk1oH_IK8wpqnx6jIGSIsKqTDcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7311" target="_blank">📅 10:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7310">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDw569otHyaOnOVWlXzoypxaLFs1oUS5SozafhvvlVecFYySbThr4Poizh8huVajYIdBIMgN1STx0-4TPdT41pkTU20IXOPJMN-ttWS-QsUj7J2XvMVWwEPUDlSkt8wEDmnkks-iNn1hwUKw5ZqtHvd_w21fBA9eLu2lI8CfS05MB-GL5PY0zpCpVbTHclcHY24h7GAyL5MJQXKspFnhr8W9KMaU8hNFZN_vzfTPiVUZYdya776XYif0sLZWCUgFLhpfGkICUXTqLVAhA920M5xriU5OpGNlAWK3IHifmKjIOgXZkhAZj-s8xTfI2JcgsFSMDsMtuBJq687w7Ty5YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7310" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7309">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7309" target="_blank">📅 23:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7308">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6hazYVmPMiR9rpflipUpq9CXBIRBMUMr_OI4WmCHbl-drJoxW5TM1eHk8FSeb5P88GFauVMJhMrzxhwJXk7S95r8Fj0B-2gBJWGFbE7aR3vm5v2JFvjivUmYfFlyxSJInD7AotceswJA2pd2cL2EAN_alnIQ1Ag-BAiNCv3LLLRsYUQ_XzpZAyzq-jnU1tuZ6onaPFXryyhI043MkC8dF3e54unxFuZKr88Ko8Xubtm1Ju_j3sM_mwwEJ1WnDALkntdD8eV5hKylsBNm2fjjlrqFBY2LMdV5ISO_eBEtyfEsUPIRIW2k7ZJ7yEyru-kCYAtc_KNbnAVdaEsWO0g-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7308" target="_blank">📅 22:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7307">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaLjiv8zaMfQmDGGfi5-OseyuMdHCzzJxtp4qmMe4YB4VkiYvjCpYe_dHUfFsGOgyyv3CWlhSL03j0tLpXnm68vMseoDphth5tO1_ueCmY6La6nCc1oweoyScMCnplc6Xt0yQmb99a8TbQ8J0q11wMAOgNnX3JkGqtRP_ohzHx0O_uNCuaFEFYYZ7y-83mWfLqcUEEM4vTsnwQ4fje818Dh0LUMzkGDVIafqSxIAIGgRAaquLIsi75fHEJkhxyCfLjVzWZCf-mPNO_cmOXaXU-o2ghsIMybhh3F5bO2AT_qvIlVsjdeVsogzOPx3BpRIKdwP0jHzS7Z6f0167p0lvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldrBaIpU16Xc8rcmFdn4biwxnt1XFbx4bZNA8dFcA5xA6RmIIByWqrIMv5s7kmzeNjpF11oK4b-4GbHfHVhM6XaAa1pkMxaDvpIyHd6wcl416wi6ngZ9J73ul5tyw4NQ7D0HNG-3c8gAtbkPxg3gnFJCgM82L0VZf7nWXr4YVYf3KYA18hOXztQ9_Z6X6nn-SW5EDDwOoewjU4mvBdcZxUoBIRSbX1LcjLMJrk9eYUX2nSyJBBRFnAXA5difoAv9QfdpnbsXjlp1Gz0EKh6TlueqKwOcmudqr0Qkx97jbPtIP0NTmaTruayzadj1IKMiy01_4Y3pNIO1jQkY0w-aUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت تلگرام پس از صدور حکم بازداشت بین المللی روسیه علیه پاول دوروف
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7306" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7305">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Msa8vpV1wReXBGHvXUyylt6zlYDdVzisI-mEYe3uZGz6ld7EwTZDX6tsq7iuvaEMtJapCN6ek89FOfMN3zkP21RBHpHPPJ54-Dbe-23-SArmtuH2wcCrBtbJF4xmSOJlozSoL3GgME-_msEi6UzUxlpZk5hVR72lDBGLw_be1hbysRuJIaKNgU0qJTOuJlg6sf-6Wloa05YRROMY4TZi6I4vaBoqQ3YII1quDSeakUrQ8xtzDriDRtzAY-M1CnGXSIxAL8qwnOYTaA5GnCANEsfy2rD4BIw-hqDbYUgritMaPb8XXoGj6-u-qI2UpubMV_MKrhaJXlPli7BOROGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😂
https://t.me/ArchiveTell/7300</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7305" target="_blank">📅 18:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7304">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7PAyPYiZoV9z_4quCo08Kx5M4AfhwfHlc_07QCD_Mmfg2jd9KDs3dD_QFCP2Kr5n7FxWXLQWTDhq-KJwtI7Aq08FinwYuCwrohkdqVDlDos2UyXWiH1WDOEeaQYV4S4aflPg4Nd0lhH5SnVNPhteOBy357K4NntwYUb0NcH1adyfbyaPfnN4QON1TgGuxC2PyVtiTq_iEcoKYi5vfSM8AKBUFfz824aCSGYnykmtZlHHK1LM6LVrmlTzUtOLQZ6pUbGICBz85PBLuomAi_THaMMSSOvKSh0JjPr4CJg65e4cjmEyWGJNm_4Br-_gZ-_ZYKdHy2P00go85HcOl7KTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7304" target="_blank">📅 18:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7303">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccKiac4Kzd9bdpJcb4SOOk2K6WGBMzNxBBB5iPYc5xf1kwZ1WZIyG6zPsHBYZHfeN15orJ-GkrK4FpW9u1nWHpmovPJ0Ac6P1qsRXHK9B6Ew_EuLOdQ8tzXlIHu7D0HhMQJ5bskLhw6Qav7KstduLmVFqBHQSCv5yJtNK6gK4KNlhpuldPBhVexWlU4ioC-Eo37ggIxtyN-9pn-C0A6tPhwrGkj8nCPxaHCVb0gq2Bp5MI82qs-SorwATbkAqq0Qxv01-zJGvafSa7k1t5QsyvNFCAmWI5S3Mkp7zRUq3rGHSCuS48MY-V18_3qHtoppTr5WgWrxelAvl7HvUXECZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7303" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7302">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLDJ6CKiBMnMq2bKeKGLrw0sFK5Jn4TQbk3cQLTR-abyv2wEioKVFnzv_EDQMIAtWfqMiQtTJxkwRF_QYsgEgsx4cTr_6ZQNQTU6GEKvqaN8_rGV9u4vr-m6FIUH6NMon54jHO_OYVNEYQ2B_8uNQzE6LPpNjTcT5zVaaeOBP6dhJwL5h2cnDr2ml5FWkZBirmD1JTxnQILBRCEizajt07CA_CVXZqXR30ffhRlh0WNBxSpTCcnHpeyYOOEhlodU4gY0UcTaAJEFA2Lyzl17utLG17p1YYcp72AueHguFrHFonsS_-c0yRt0yZuATqYY4KNNx-MBPA06BUxVTeliuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7302" target="_blank">📅 12:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7300">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCm6IiCoAwWat-8hM9jQSdwtaUZFld-QZSsPHDBAlDPOAfE3ort7KuatJCefZxPJ_KNEgi4etirJSVT6OisOdAWnl5x-4yAWGWBDWGcoAQdYimDveslq0m7wTxAYy1VKdJecYoLOABiG9zIaL28i_2vrtoJYPBc1XWXB_zJmiCZmYCE8KbZst5XWxn6GA6VTNnBJd5zus-JK4V14v9SM-e9zp70zpYBu_vdJrV9uO4v1qbwefJaKY1FPxsu96JKT0hngXOkYNAaeA3GaQ7LS8MiFb1OjhEVR1OPCnmTWtB_O49lcr--RMYg82MKAT0Z_bs8q_c5aM98TAlJPMPeqmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7300" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7299">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7299" target="_blank">📅 10:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7298">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7298" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7297">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7297" target="_blank">📅 00:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7296">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvAGbQVc2z7vP9gHyTImWRn9o3QMoGuaNcvrih2bk5k4pwxBLLrCqP_QeNNPEfzFcF9z0BCYiFmF-VrxM-GmMimy-ZCeGBVlvAlheTV2i4V_P9AKKHqFxaOfQEeai-Gchu93WDVVS1Y7xDkaiYJCKjy0frSe8IrDmWUct9oaPC8CEyyTSV1evFfULM7cVfI5xZc4134XBLLHHOSq2SHSGAoHZkuhTICyT0C6taB0arApq90tNQCt3h1hLwummPsrhYcXF3M6Kys333sLoxIkSxNDI1pKpS9hAld1llFL_QLAXBSRBjk6kUgPoNPaMAmZBxXxlZzHoTEC6epMSZK94g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-kaL-K5ZnVEOJ2FSKGo7O5HYEoB6bkZhi0BUmpc1LznJmv_59ui7XQUT9Wm6ckRTa2__zKBFB7c0LbxOmINBLD2nF-5riAMoBBnD3jBT7mqugxj29oa7VfX_53N2SsG6AM6DiZ1tz6Pue2wYdsSwQze2wGkgg_yq1Nw871V83vSeFx5hpDINoleW6yWPQWqOwxuHaBWP2te5HdRsXMRNYPFrLULROo_6fuf6-21WiQh5NEU60vyE9uDG5A7POjxssnewcB07Q82bVuKC8fPHiZl1Drx5DUHRvmUOvCCD-5a_-BqqT20D4J5qxKQgkLjx92to5TiYAWZN9ZiL_pkEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7295" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7294">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc74InMzj_2Xi1WDmaP3eFADvZgED0TyvN17A5bq2eRAYGWjUHwiKYrGNwZYnXEnPDfcJrzfI1-i_G3LUU3EWppr-jxiOLXRPoI4H-J6kuCUlWODTz8qBVAv8TahJcMOIPlxrP2xN8YjSJXDbPez2fmoWGhE7Qm_JF0YQ0vFrwH4Acb04J-iJkIRzo5G-h9Vt6UMRr75lpOufkLXe9vH84N4rbjPw-ND8MdN4Oh6SmvVS8NjbU4g8OnnkjpHRfsoGym4EgeAIMgsCduI_JNiCwxjF5_UPm3oflKEa8vGcJjwGLKiHN9IdTOvqbl3eouAVgzv6IN5mvTiaS6wD3aOYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7294" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
