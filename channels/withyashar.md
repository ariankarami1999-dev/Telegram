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
<img src="https://cdn4.telesco.pe/file/HIiTTgNODJgdgDCjd92rHMri5swFFzSE9yB8-obzknmdngr2V6dL50FItWQhBg1r13MrhQ43LhQ7lGWGr1REjyZiQ1Hmf5joZ83Xn9IciWSGcivDFE5uC0LkOLwIYdspZVQGk4iTNa-VOMuEibeEhfOy2qkbcWsMnT-FykkB0lA1LSqPDsFtdFq-1tRQFMBaDURC-G7619ayCzRXmlIELtR9ulc9i_tFby-WrfW_nJ-4PWM_IeXU7HeVfpokXG9qnwVX_8-nDyACpDxRS-J4sAlW9jN0MgQELrMU5g8PMM0PCdFWG6BXlZYnhpNfloMHvrlNa9nM1Xrl2PolzYfwMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 444K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 21:42:30</div>
<hr>

<div class="tg-post" id="msg-20973">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سیریک گزارش صدای انفجار/پرتاب موشک/پهپاد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/withyashar/20973" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20972">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1310e64db.mp4?token=oAImxmd-ECaDsuKtBSj6hjW4o-pAzby35RXi10Oo6k1r9EBjMZxgH8cVzSvlhbO-jh-sy8E7-W8wbLaR3P1hnyjwf7VAmcdwnzI56ZkjaAEHnP48uzDAlNfFgSw7vERfLNKef-6NFZqh416XVcWEj72K6rC_tmnP-6vmidqB3i8gvJfWCuSsyZH0jmbgPyUHw2AC9BIpM7SRkpgv_DzA-t9r-sr0Xgdk89LMgiA8Tn5l6XVvowWKAoL4aLIUTu6XjF8DJVCRQouHuEfVq0DwGUWzzRmJfQKtJeLGJQc3JiEVOdxJdOcV5ZlmQOPLxen0PCAoxxo-kqMDiQb01Ia0SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1310e64db.mp4?token=oAImxmd-ECaDsuKtBSj6hjW4o-pAzby35RXi10Oo6k1r9EBjMZxgH8cVzSvlhbO-jh-sy8E7-W8wbLaR3P1hnyjwf7VAmcdwnzI56ZkjaAEHnP48uzDAlNfFgSw7vERfLNKef-6NFZqh416XVcWEj72K6rC_tmnP-6vmidqB3i8gvJfWCuSsyZH0jmbgPyUHw2AC9BIpM7SRkpgv_DzA-t9r-sr0Xgdk89LMgiA8Tn5l6XVvowWKAoL4aLIUTu6XjF8DJVCRQouHuEfVq0DwGUWzzRmJfQKtJeLGJQc3JiEVOdxJdOcV5ZlmQOPLxen0PCAoxxo-kqMDiQb01Ia0SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : این کشتی با یک کشتی یکسان (جرج واشنگتن) جایگزین میشود
خبرنگار: خانواده‌های نظامیان نگرانند از شرایط ناو لینکلن
ترامپ : «نه، آن‌ها نگران نیستند.»
خبرنگار: آیا این استقرار نظامی بیش از حد طولانی شده است؟
ترامپ: «نه، نه، نه؛ حتی نزدیک به آن هم نیست که بگوییم بیش از حد طولانی شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/20972" target="_blank">📅 21:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20971">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfefd33ebd.mp4?token=IkCW6mTavH37uvC5-V1-HGI9MMwONEWdssZ9K8KttuUcug8obAe4FH2ET8WvnLmTXvfbuqWJ_d9InyxRN8qMDweLZaW34H-Sm5F9-nJJYqOuwYiWbZlYG6Bc8mK6XA6Xq_GPjGjx5Xad1ZzhJXzNs3-5aapEcTRn5CcN2nilVcR8ep1r3F5rK-MQKV8IMQHBGDJLytqf-7FPM8C_krbU_moRbTUXZHcqUrY6cBlh7TGIdGYLqS_TFpC827xGssYyS47GWYEXUfynNPpzZH6t3kSx4kAIEPjj6O_rrSfWHk92IKQKT3wkQmXOnZQU7wPR_5Ky8SN7eiyxy4ssfrXl7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfefd33ebd.mp4?token=IkCW6mTavH37uvC5-V1-HGI9MMwONEWdssZ9K8KttuUcug8obAe4FH2ET8WvnLmTXvfbuqWJ_d9InyxRN8qMDweLZaW34H-Sm5F9-nJJYqOuwYiWbZlYG6Bc8mK6XA6Xq_GPjGjx5Xad1ZzhJXzNs3-5aapEcTRn5CcN2nilVcR8ep1r3F5rK-MQKV8IMQHBGDJLytqf-7FPM8C_krbU_moRbTUXZHcqUrY6cBlh7TGIdGYLqS_TFpC827xGssYyS47GWYEXUfynNPpzZH6t3kSx4kAIEPjj6O_rrSfWHk92IKQKT3wkQmXOnZQU7wPR_5Ky8SN7eiyxy4ssfrXl7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم : دود مشاهده شده تو جنوب تهران مربوط به آتش زدن ضایعات پلاستیکیه ( عمو پلاستیکیاهو )
@WarRoom</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/20971" target="_blank">📅 21:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20970">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">داعش شروع به تهدید علیه اسپانیا کرد
@WarRoom</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/20970" target="_blank">📅 20:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20969">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dd6977b1.mp4?token=KviXypy9zVwAQy8y8nSZob3a4Z4ETgrbSX6b3IMlwAfNP5KngPDfqs3Smu_dLO4ooTFg3ezdl0bNj022whbCuqxBvsH47ssxslZVYAB_3QblkTrIIk7CR2G6_0ffyONIXRr72D0KPkIUaAXRur32893sQhH8c6n0r2Anup69jPkgiDnAS25ONMtpDRRhjjF2I4jHkuicFLs8c-QU6D5qWQtE52KcT1xzmDuNM1j0ZWomGcYvEJZhxxvgXVHmLd6m5NmnShEJWVVYZLoCM8lwbqHzgDCb4rEX9qUmyojXze-PeR8sJqBAgWKdZfzM9Thy3fBRrdu9vUl7vNEZzZYgiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dd6977b1.mp4?token=KviXypy9zVwAQy8y8nSZob3a4Z4ETgrbSX6b3IMlwAfNP5KngPDfqs3Smu_dLO4ooTFg3ezdl0bNj022whbCuqxBvsH47ssxslZVYAB_3QblkTrIIk7CR2G6_0ffyONIXRr72D0KPkIUaAXRur32893sQhH8c6n0r2Anup69jPkgiDnAS25ONMtpDRRhjjF2I4jHkuicFLs8c-QU6D5qWQtE52KcT1xzmDuNM1j0ZWomGcYvEJZhxxvgXVHmLd6m5NmnShEJWVVYZLoCM8lwbqHzgDCb4rEX9qUmyojXze-PeR8sJqBAgWKdZfzM9Thy3fBRrdu9vUl7vNEZzZYgiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزمکس: وقتی یک دموکرات می‌گوید «ایران هیچ‌وقت قوی‌تر از این نبوده»، واکنش شما چیست؟
وزیر خزانه‌داری بسنت: آنها بی‌اطلاع، دیوانه و فاقد هرگونه درک از چیزی هستند که درباره آن صحبت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/20969" target="_blank">📅 17:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20968">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">واشنگتن‌پست: ترامپ حتی در برابر کنگره نیز دست بالا را دارد
واشنگتن‌پست در تحلیلی می‌نویسد قدرت رئیس‌جمهور آمریکا در تصمیم‌گیری درباره جنگ، طی دهه‌ها افزایش یافته و کنگره عملاً ابزار محدودی برای متوقف کردن رئیس‌جمهور دارد. حتی اگر در آینده هر دو مجلس کنگره علیه جنگ رأی دهند، رئیس‌جمهور می‌تواند در برابر چنین تصمیم‌هایی مقاومت کند و در صورت تبدیل شدن آن به قانون، از
حق وتو
استفاده کند؛ وتویی که تنها با رأی دوسوم هر دو مجلس قابل لغو است.
این تحلیل در عمل نشان می‌دهد که
نتیجه انتخابات میان‌دوره‌ای به‌تنهایی لزوماً اختیار ترامپ برای ادامه یا پایان دادن به جنگ را از بین نمی‌برد
@WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/20968" target="_blank">📅 16:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20967">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزارت جنگ ایالات متحده با شرکت‌های "بوئینگ" و "آر‌تی‌اکس" قرارداد بست تا تولید قطعات یدکی موشک‌های SM-3 را افزایش دهد.
این موشک‌ها برای رهگیری موشک‌های بالیستیک در خارج از جو زمین طراحی شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/20967" target="_blank">📅 16:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20966">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPfMxpMXul2jJCNHfGzxs1fH0JoyHtcFt4LumCGzhDK3fU2GrE7-HMEtvI8OdPAdtZY2U9hHPyApo4BzHeX2LcbxkotoYCKw38HvWggi5T7kWMh30_xzAuG8pUu2H2IPxf5CQxaiehUH8VxVs5OUpHD7Ih2nfXlnDoYffjC2KZay6NydAn74OJBLhj2bCW2vnuVPhQpM9bGcQ38hgWToSdBpXERYXWbimqmum2qswMz590tfw9j6atAcOnfQbz9Oq-LYfoWZEdgKeBmOa_m5Ttnz6-wGJnmgMdGGCJ4O0uexPNjJ1X3J631X7-j4VvJWc-2SeWCJY2pipNNBQZgT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ در تروث :
نیوزمکس : ایالات متحده با انزوای اقتصادی بی‌سابقه‌ای به ایران ضربه خواهد زد
@WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/20966" target="_blank">📅 15:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20965">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ادعای وال‌استریت‌ژورنال:
ایران و عمان در حال نهایی کردن پیش‌نویس توافقی برای بازگشایی تنگه هرمز بودند که به تهران اجازه نظارت بر کشتی‌هایی که وارد خلیج فارس می‌شوند را می‌دهد، اما اجازه نمی‌دهد عوارض یا هزینه‌های خدمات دریافت کند.
طرفین در مورد نکات اصلی پیش‌نویس که یک خط ورودی در نزدیکی ایران و یک خط خروجی در نزدیکی عمان ایجاد می‌کند  توافق کرده‌اند و آن را با آمریکا، کشورهای منطقه و رهبران ارشد ایران به اشتراک گذاشته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/20965" target="_blank">📅 15:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20964">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اکسیوس : به گفته دو نفری که اخیراً با ترامپ درباره نتانیاهو گفت‌وگو کرده‌اند، ترامپ گفته است: “بی‌بی بزرگ‌ترین دشمن خودش است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/20964" target="_blank">📅 15:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20963">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اکسیوس : دونالد ترامپ با وجود درخواست‌های مکرر، هنوز از حمایت رسمی بنیامین نتانیاهو در آستانه انتخابات ۲۷ اکتبر اسرائیل خودداری کرده است. در حالی که نظرسنجی‌ها نشان می‌دهد ائتلاف نتانیاهو از اکثریت لازم برای تشکیل دولت فاصله دارد و رقبای او پیشتاز هستند، اختلافات واشنگتن و تل‌آویو بر سر ایران، غزه، لبنان و سیاست‌های منطقه‌ای افزایش یافته است. مقام‌های آمریکایی می‌گویند ترامپ از برخی تصمیم‌های نتانیاهو ناراضی است و ضعف او در نظرسنجی‌ها نیز تمایل رئیس‌جمهور آمریکا برای ورود به رقابت انتخاباتی اسرائیل را کاهش داده است. با این حال، کاخ سفید همچنان امیدوار است دولت اسرائیل در اجرای طرح صلح غزه، مذاکرات منطقه‌ای و برنامه‌های آمریکا برای توافق احتمالی میان اسرائیل و عربستان همکاری کند
@WarRoom</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/20963" target="_blank">📅 15:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20962">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e612920df0.mp4?token=qZx1z-eFgm9_H-dC0odqGyQtyA0sEaVJxejRASuMxTsuoECrJRJnY6RfalxB9lLXLaw2CayirUpKctoJLebq55BnARm3vKf3_GmEjNnWVWjP-MDYXIImGX9yd4TTK3ISJxHD_RwUFK_L34ZCVtpNIoBmoMzwyCK06w9INlj8Q2plZhOrOj-mSxFn-5-Iy3nL4Xwg44QIStJR1-rS8Rv18asEhHl7jANrEExLoVxx3IY8xUDobC_R8kunApBEFkzA9VFd0VW9iyvE8JB4y2nuc3-GO63qFJnCFvhIS-MzzK9Iwhe3ZYET4CYf-v7T64lIELJ696FCUQrjuKZUl3tN5hZf99Pr76dj-H8TlKe7KiZa2KHbc5pT6GztbrK4_P6LsSXIBwwA7EX8fW4PUohHqzxfKP2UXBNpNDxgsAk8-B7w0QB0yg1QcjPYEKyhYK_BScEasG02f-t4ugnD5M8cBWtyPzs97X3WY23hCc21yY8yCg78He6DNl8SX1Jo3kPszXslRYi9CXYlMyc6rpDTeGuuaG2BBpFgDOQLv-gStiM7SxReqAxKGftr7C9JS03Zebm0HqbL8huhtlgODkmXIGZI3B901G2KN0FYcLMOKaPwWUmyqxiB3Wy73IHccHd_ZOVE20YrGlTdTuEWLewuaEfDdQNCSC76U6Ql-r2VNVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e612920df0.mp4?token=qZx1z-eFgm9_H-dC0odqGyQtyA0sEaVJxejRASuMxTsuoECrJRJnY6RfalxB9lLXLaw2CayirUpKctoJLebq55BnARm3vKf3_GmEjNnWVWjP-MDYXIImGX9yd4TTK3ISJxHD_RwUFK_L34ZCVtpNIoBmoMzwyCK06w9INlj8Q2plZhOrOj-mSxFn-5-Iy3nL4Xwg44QIStJR1-rS8Rv18asEhHl7jANrEExLoVxx3IY8xUDobC_R8kunApBEFkzA9VFd0VW9iyvE8JB4y2nuc3-GO63qFJnCFvhIS-MzzK9Iwhe3ZYET4CYf-v7T64lIELJ696FCUQrjuKZUl3tN5hZf99Pr76dj-H8TlKe7KiZa2KHbc5pT6GztbrK4_P6LsSXIBwwA7EX8fW4PUohHqzxfKP2UXBNpNDxgsAk8-B7w0QB0yg1QcjPYEKyhYK_BScEasG02f-t4ugnD5M8cBWtyPzs97X3WY23hCc21yY8yCg78He6DNl8SX1Jo3kPszXslRYi9CXYlMyc6rpDTeGuuaG2BBpFgDOQLv-gStiM7SxReqAxKGftr7C9JS03Zebm0HqbL8huhtlgODkmXIGZI3B901G2KN0FYcLMOKaPwWUmyqxiB3Wy73IHccHd_ZOVE20YrGlTdTuEWLewuaEfDdQNCSC76U6Ql-r2VNVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیپلر
: ترافیک دریایی از تنگه هرمز در ۱۳ اوت افزایش یافت و ۱۳ عبور تایید شده ثبت شد که نشان‌دهنده رشد ۴۴ درصدی نسبت به روز قبل (۹ عبور) است. نه کشتی از طرح یک‌جانبه ایران استفاده کردند، هیچ عبوری در سیستم جداسازی ترافیک هرمز تایید نشد و چهار مسیر نامشخص باقی ماند.
فعالیت در باب‌المندب پایدارتر بود و ۲۹ عبور تایید شده ثبت شد که ۴ درصد بیشتر از ۲۸ عبور روز قبل است. هجده کشتی وارد دریای سرخ شدند و ۱۱ کشتی از آن خارج شدند، در حالی که دو عبور تاریک ثبت شد. در طول روز هیچ حمله جدید تایید شده‌ای به کشتی‌ها گزارش نشد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/20962" target="_blank">📅 14:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20961">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f327dcc92.mp4?token=CFLeL2nr-cUqwN9uxq_ZxJvycoa3XPOI2yiU6E16RQK49XiWNJ6JOvHRxIRrfPNq3nCTCzlx2N3PJEiISMG9bKllR1Ru9-9wlSCmwqHaq3aJBxihx1n5x1mB-02Ht70-nLXs-6MSoMyLy-INSTZHRQOqGkyKvoPmxowHkyZbQEWDyyfnGnPSpW5SUmQMIx_Was4zA6pfBLNJ1IIhFggF-qZiIEBCKADAFBocY6_ZSz564ceW84zgKYceUn-kg2bguYIA8F45xPnY0ge4uhT2QdC998zUsCkozfBmFiNdaH1myCi6oCU-ftWqbA4iF9CMov2U276W9iQSC1zf8JowTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f327dcc92.mp4?token=CFLeL2nr-cUqwN9uxq_ZxJvycoa3XPOI2yiU6E16RQK49XiWNJ6JOvHRxIRrfPNq3nCTCzlx2N3PJEiISMG9bKllR1Ru9-9wlSCmwqHaq3aJBxihx1n5x1mB-02Ht70-nLXs-6MSoMyLy-INSTZHRQOqGkyKvoPmxowHkyZbQEWDyyfnGnPSpW5SUmQMIx_Was4zA6pfBLNJ1IIhFggF-qZiIEBCKADAFBocY6_ZSz564ceW84zgKYceUn-kg2bguYIA8F45xPnY0ge4uhT2QdC998zUsCkozfBmFiNdaH1myCi6oCU-ftWqbA4iF9CMov2U276W9iQSC1zf8JowTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش اسرائیل در حال انفجار ساختمان‌ها در منطقه روستای شیعه‌نشین مرکبا در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/20961" target="_blank">📅 13:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20960">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">از امشب ۳ شب مست میکنم
😂
🙌🏾</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20960" target="_blank">📅 12:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20959">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxAn3Wv-T6QS7XN2gJj-R3FBMaf6TyFK_YiXzPCmo_tUnE0aXa_2yUNDCexVE0wCyAmWHrcOXlilvwJjywes3qN7XQCHr4pOIvBgsH9YXbFDl1oHLg0OLyDyo2HzEA_OVfXNa6Lcvh-kgyZx0iDpVESqvY1Nh52tVUZ8jIOIyarx4vTinf3NiaihJ2wD9R-27MXpSoAjOdRmLbqIeJxxftRacS8KNSz62aY-cvQz8qkgEtH9aCCJsyWgzSfSA4DSmzfefRfG3qyqYiAMVcrdoe_1Najr8XrvSCUjDOSLiOs_vHaYeKCSzy1mMfUumUWEMrxjVa5pouxAtIN76diQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
بر اساس گزارش‌های دریافتی این سازمان از مراجع نظامی، یک نفتکش هنگام عبور خروجی از تنگه هرمز هدف یک پهپاد (UAV) قرار گرفته است. این شناور دچار خسارت جزئی شده، اما تمامی اعضای خدمه در سلامت هستند و حضور همه آن‌ها تأیید شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20959" target="_blank">📅 11:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20958">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‎ اتاق جنگ با یاشار : فلورا جون سر گردنه
هم مسیر شدن ناو هواپیمابر جورج
واشنگتن با یک کشتی کارگو ایرانی به نام «فلورا»که بسیار زیاد شبیه به عکس کاور مجله اکونومیک ۲۰۲۶ است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20958" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20957">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efb82e574.mp4?token=DVFN3ojYaeYexdT_sqxn_7qIcgAxnA1cRE38o5pyZGpKgrWDhWqbrCInFWl5zRgJEFVnX6sLLFyABTvOfgOXBBhvpQ1vYZJg8AXk7tQZ7jXWTc2FXEE9BsfQ1oCxNRp3p94V14CCAoRDhHWN4dl7KC9b0Gy7-k7E55lw5QG_ldjcnxtyJ_0xuz7PeeIdBCkHVOhY00Mf2oZlljibZwp_xlu_OU9ufiWTOJjhmsGPW67_9E7qpZQzcunTspgt-VTxauDbSZJxjVv4Z0HZ0GfOr6gxqkARaKSbACN6JYHx12-unQa9kUo1bnS64jn6c9OarJj_ObcqTL71Ktj2FgwAAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efb82e574.mp4?token=DVFN3ojYaeYexdT_sqxn_7qIcgAxnA1cRE38o5pyZGpKgrWDhWqbrCInFWl5zRgJEFVnX6sLLFyABTvOfgOXBBhvpQ1vYZJg8AXk7tQZ7jXWTc2FXEE9BsfQ1oCxNRp3p94V14CCAoRDhHWN4dl7KC9b0Gy7-k7E55lw5QG_ldjcnxtyJ_0xuz7PeeIdBCkHVOhY00Mf2oZlljibZwp_xlu_OU9ufiWTOJjhmsGPW67_9E7qpZQzcunTspgt-VTxauDbSZJxjVv4Z0HZ0GfOr6gxqkARaKSbACN6JYHx12-unQa9kUo1bnS64jn6c9OarJj_ObcqTL71Ktj2FgwAAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویکتور دیویس هنسون
تاریخ‌دان، نویسنده و تحلیلگر سیاسی محافظه‌کار آمریکایی و پژوهشگر ارشد مؤسسه هوور است. او از حامیان شناخته‌شده دونالد ترامپ به شمار می‌رود، کتابی در دفاع از ترامپ نوشته و دیدگاه‌هایش در رسانه‌های محافظه‌کار آمریکا بازتاب گسترده‌ای دارد, وی پیشنهاد کرده است ترامپ از شاهزاده رضا پهلوی حمایت کند و زمینه تشکیل یک دولت ایرانی در تبعید تحت رهبری ایشان و با مشارکت ایرانیان را برای جایگزینی رژیم جمهوری اسلامی را فراهم سازد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20957" target="_blank">📅 09:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20956">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هشدار خزانه‌داری آمریکا: تحریم‌های «بی‌سابقه» علیه ایران از هفته آینده
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد دولت ترامپ هفته آینده از بسته‌ای جدید از تحریم‌ها و اقدامات اقتصادی علیه ایران رونمایی می‌کند که به گفته او «در تاریخ بی‌سابقه» خواهد بود. جزئیات این اقدامات قرار است هفته آینده به‌صورت رسمی منتشر شود. این بسته بخشی از تشدید سیاست «فشار حداکثری» واشنگتن است و انتظار می‌رود بر مسدود کردن مسیرهای دور زدن تحریم‌ها، ناوگان سایه و کانال‌های مالی و ارزی ایران تمرکز داشته باشد؛ اقدامی که با هدف افزایش فشار اقتصادی بر تهران پیش از هر تحول دیپلماتیک یا نظامی دنبال می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20956" target="_blank">📅 09:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20955">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حقیقت یاب سنتکام در جواب به رسانه های رژیم :  ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» همچنان یکی از بالاترین نرخ‌های تمدید خدمت خدمه را در میان تمام ناوهای هواپیمابر نیروی دریایی ایالات متحده دارد؛ این نرخ ۸۴.۴ درصد است. ملوانان و تفنگداران دریایی گروه رزمی ناو هواپیمابر آبراهام لینکلن، پس از بیش از ۲۶۰ روز حضور در دریا، انجام ۱۰ هزار پرواز و مصرف ۱.۵ میلیون پوند مهمات، همچنان مقاوم و مصمم باقی مانده‌اند. هیچ‌یک از نیروهای نظامی حاضر در این ناو هواپیمابر جان خود را از دست نداده‌اند و تنها ملوانی که در ۳ اوت به دریا افتاد، به‌سرعت و در سلامت کامل پیدا و نجات داده شد. گزارش‌های گسترده و نادرست درباره مأموریت تاریخی آبراهام لینکلن، در حق زنان و مردان نظامی ما و خانواده‌هایشان بی‌انصافی است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20955" target="_blank">📅 03:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20954">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هم اکنون حملات شدید پهپادی جمهوری اسلامی به مواضع گروه های کورد در اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20954" target="_blank">📅 03:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20953">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">چند گزارش داشتم از صدای تیر اندازی سمت غرب (محدوده آزادی)
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20953" target="_blank">📅 02:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20952">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ به فاکس نیوز ‌: محاصره دریایی ایالات متحده در تنگه هرمز کاملاً برقرار است و «یک دیوار فولادی» است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20952" target="_blank">📅 02:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20951">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LALVR1xc8twVqeqsZm6pFv_HuHg779BNockzgGVZ9bU-17CsJL5_UOM9cArNQq-K-11jogUgF07Meehgxa5Xb--kYjf9XclzI17gNQYVTssZrg28taBJ3Ea-UN9ZjxQKeDAKe7T0ROIFrukmngcM-qhNZfBBBXy-80J95laBnafLzuvpJ6dZGPciIVTIrAkzrzfefE6sRQcfML7HRahhPCkjxf6pHxdtfH20qEtmLyNBrKzAHkNlCw7HqQzwQqGgAC7VjSLsYHFC8hd2hj_Wn-vMxJhAP6xP-MqENWRqOEzpliprEHS3G3D2MveoYPEAzxhqiVAkaHRKOTFGX08m9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای F/A-18C هورنت معمولی نسل اول برای تفنگداران دریایی آمریکا، از سمت تنگه هرمز با ترانسپوندر روشن( فعال بودن سیستم شناسایی و ارسال اطلاعات موقعیت ) با یک چرخش در ابوظبی فرود آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20951" target="_blank">📅 02:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20950">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بعد از مدتها حتی‌ اطراف تنگه هم سوخترسان دیده نمیشه عجیبه…</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20950" target="_blank">📅 01:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20949">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50455ef10.mp4?token=hyJsDvQXe5EQbTh7YgdC5ynk2u3tmsy0EyrsydgGmtPS4P9477yPIBjvBnCIsNPF-xd4xbtIqWWiSHz-WxdVMqtM4PQMh5VTLI0z_e8JgxYesKcyF-ltuJF_mhF1jgipdWJwdiV2xp93_mgfVhQOpSBw5TQVNQbULqJodtKIOxHNO9cGy73gofX1693KzGU35fnZucphqJ8ziDt_AdFKSM4xBBUgXCTE0a_7dmxD7ytnULp6MFB456oLvYDSCtZxpRkPu1waNYtg_GfdToQtUa5EYd2lPQLzPAaDAJ1ctonazNJgSQzr98dhc3Ni9f5MZcV9SevGt5NcuObfy9M-bIqYjIFboTgBVKq0R1Ev_TaSTlK9OyRtKLdJ5mHedtpdV_fuT6GT3mJzW5lwwfhgt8hosmKcVCZxA0s2rxIAhgS0QYq9Y2rVdOdNGgaXa5NFMvdjs-0RIOuPTN6iHYCaVqhrLaoe5oPaCY6qo1O-zL8aXRMZB5MEscdfr041z-7wrrUngbHtvaOU5Q1o7D4jFqzt-XYfuLWC_OJeluOJXF8XUupkby78X6nMmX-R-HIzUZskNH5PZWFFUSlOj-GvYitCOL6glUe1g-8abjvXmychWkCbJTOYQ6wrqP-6Y0fUVHDSlT-fZaNKdlOz-xVkFHPFG7QzCYQHDLQTClx1B3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50455ef10.mp4?token=hyJsDvQXe5EQbTh7YgdC5ynk2u3tmsy0EyrsydgGmtPS4P9477yPIBjvBnCIsNPF-xd4xbtIqWWiSHz-WxdVMqtM4PQMh5VTLI0z_e8JgxYesKcyF-ltuJF_mhF1jgipdWJwdiV2xp93_mgfVhQOpSBw5TQVNQbULqJodtKIOxHNO9cGy73gofX1693KzGU35fnZucphqJ8ziDt_AdFKSM4xBBUgXCTE0a_7dmxD7ytnULp6MFB456oLvYDSCtZxpRkPu1waNYtg_GfdToQtUa5EYd2lPQLzPAaDAJ1ctonazNJgSQzr98dhc3Ni9f5MZcV9SevGt5NcuObfy9M-bIqYjIFboTgBVKq0R1Ev_TaSTlK9OyRtKLdJ5mHedtpdV_fuT6GT3mJzW5lwwfhgt8hosmKcVCZxA0s2rxIAhgS0QYq9Y2rVdOdNGgaXa5NFMvdjs-0RIOuPTN6iHYCaVqhrLaoe5oPaCY6qo1O-zL8aXRMZB5MEscdfr041z-7wrrUngbHtvaOU5Q1o7D4jFqzt-XYfuLWC_OJeluOJXF8XUupkby78X6nMmX-R-HIzUZskNH5PZWFFUSlOj-GvYitCOL6glUe1g-8abjvXmychWkCbJTOYQ6wrqP-6Y0fUVHDSlT-fZaNKdlOz-xVkFHPFG7QzCYQHDLQTClx1B3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز : آقای معاون رئیس‌جمهور، یک لحظه به توافق نزدیک هستیم، لحظه بعد می‌گوییم قرار است حسابی آنها را بمباران کنیم. یک لحظه تنگه هرمز باز است، لحظه بعد بسته است. مطمئنم این نگرانی و سرخوردگی داخل کاخ سفید هم وجود دارد. می‌دانم پیش‌بینی کردن دشوار است، اما اجازه دهید بپرسم:
این ماجرا چگونه تمام می‌شود؟ اگر و زمانی که مسئله ایران تمام شود، وضعیت چگونه خواهد بود؟
جی‌دی ونس:
خب ویل، چیزی که با اطمینان می‌توانم بگویم این است که فکر می‌کنم این ماجرا با
قرار گرفتن ایالات متحده در موضعی قدرتمندتر
پایان خواهد یافت؛ در شرایطی که ایران
سلاح هسته‌ای نداشته باشد
و
تنگه هرمز دوباره به وضعیتی بازگردد که قیمت نفت و گاز برای مردم آمریکا باثبات باشد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20949" target="_blank">📅 00:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20948">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ونس، معاون رئیس جمهور آمریکا: آمریکا ابزارهای زیادی برای مقابله با ایران در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20948" target="_blank">📅 00:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20947">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اکسیوس : جرد کوشنر، فرستاده ویژه رئیس جمهور ترامپ، قرار است هفته آینده به اسرائیل سفر کند و با نتانیاهو دیدار کند
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20947" target="_blank">📅 23:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رویترز : ترامپ در آستانه یک جنگ پیچیده‌تر قرار دارد و به نظر نمی‌رسد که این مسئله او را رها کند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20946" target="_blank">📅 22:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش صدای انفجار‌ سیریک ، پرتاب موشک/پهپاد به سمت تنگه هرمز @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20945" target="_blank">📅 22:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اصفهانی معاون پزشکیان:
تغییر قیمت بنزین در کرمان به‌دلیل برخی بی‌تدبیری‌ها متوقف شد.
۱۴ میلیون لیتر بنزین در هر روز کم داریم
دولت برای بنزین برنامه دارد و روزهای آخر تصمیم‌گیری در مورد آن است.
ما ۳ برنامۀ جدی داریم و هرکدام از آن‌ها نهایی شود، قبل از اجرا آن را به مردم توضیح می‌دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20944" target="_blank">📅 22:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737fe5f83b.mp4?token=k4OEt0DslRr0V2jkphH7TldeiYFLlvWwftdrQPkGsY7sYXmB4CzmKmqP43zk6IBhxyxc9D1qSILNSfkCgUzhwPBgkG5kMpmfG2HCUfcYRs5QIIiPEJ-8Qecvh1AEet5U-t5FR7xB-dxqGgmAOmp_VAUNpMIHCQm91stkBOjyrxYw7uWEDykTLjfqMCTp1OFpHcOCoWjCzQ96rCnk2n1-dz45_VqM9jChz_d7k9JUoP5S8WTgdYOmllSnrXFXPqxuW13O9G473hX0KJcleBjwi6OU38uAGwWdePa3XC6SluNgoXvCCtLxc69nHT4xFNto7btLDDfVboj0CtHliDYxOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737fe5f83b.mp4?token=k4OEt0DslRr0V2jkphH7TldeiYFLlvWwftdrQPkGsY7sYXmB4CzmKmqP43zk6IBhxyxc9D1qSILNSfkCgUzhwPBgkG5kMpmfG2HCUfcYRs5QIIiPEJ-8Qecvh1AEet5U-t5FR7xB-dxqGgmAOmp_VAUNpMIHCQm91stkBOjyrxYw7uWEDykTLjfqMCTp1OFpHcOCoWjCzQ96rCnk2n1-dz45_VqM9jChz_d7k9JUoP5S8WTgdYOmllSnrXFXPqxuW13O9G473hX0KJcleBjwi6OU38uAGwWdePa3XC6SluNgoXvCCtLxc69nHT4xFNto7btLDDfVboj0CtHliDYxOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست به نیوز مکس : گزارش‌های مربوط به تخریب شرایط در ناو هواپیمابر ابراهام لینکلن کاملاً تحریف‌شده است و  هیچ کم و کسری وجود ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20943" target="_blank">📅 21:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20942">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سی‌بی‌اس: فقط یک ملوان در پی حادثه از عرشه هواپیمابر آمریکایی "یو‌اس‌اس لینکلن" در اوایل ماه آگوست(۲هفته پیش) به داخل دریا سقوط کرد. این ملوان توسط یک بالگرد جستجو و نجات نجات یافت و پس از دریافت درمان توسط بخش پزشکی، از کشتی منتقل شد تا مراقبت‌های پزشکی بیشتری دریافت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20942" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dESio2k5oCX-XMllH1wuPkLaDqZQqR3tLp7jzx9Jz20a3Pd269oIRA3COuoo3mZ4FGi8XUFIfEwGZpgk4AJB1iIlQ3Ao5Y1RF5JBzTeu7MHv1Dw979HUhWqdNUewfpxYftGI-UvP9-XBpYkjtlYhAThU6tJaQy2kD0vJx99rr1DKHmPzwpbKWpW27iuryQNXVrKFEECGobnaYJC8Mr7NWEfTEhRsY8dt539f1YlixGwR42gdaXbG1-wbt_98K_7IbGV0MsabuZAffGbqUCr_G-x7tjQGaOsUKKA9PNgagos_SWRF-UbUdhoJIhRaOKHWreh6FX0vU1UQ6SQ7E3YuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ با ارسال این عکس نوشت برایم، من در منطقه ای زندگی می‌کنم که همه عرزشی هستند. دقایقی پیش در کرج رعد و برق مهیبی زد. بلافاصله اکثر این ساختمان ها برقهایشان را از ترس حمله هوایی خاموش کردند. اینها از ترس شب و روز ندارند. خودشان هم میدانند به زودی کارشان تمام است. به مردم بگو ناآمید نشوند ، پیروزی نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20941" target="_blank">📅 21:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20940">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک منبع دیپلماتیک به شبکه خبری ام تی وی لبنان اعلام کرد که مقامات رسمی در بیروت، اطلاعیه مهمی دریافت کرده‌اند مبنی بر اینکه مقامات سیاسی اسرائیل، به ارتش اسرائیل اجازه داده‌اند تا منطقه علی طاهر در ارتفاعات نبطیه را کاملا منفجر کند (گفته میشود در این منطقه صدها نفر از نیروهای حزب‌الله و سپاه پاسداران در تونل‌هایی به دام افتاده‌اند)، انتظار می‌رود به زودی این انفجارها رخ دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20940" target="_blank">📅 21:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانال ۱۳ اسرائیل : فرمانده سنتکام، برد کوپر به مقامات اسرائیلی گفته که در تلاشه تا جنگ علیه ایران رو از سر بگیرن چون معتقد است که این جنگ موضع ایران رو در مذاکرات هم تغییر میدهد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20939" target="_blank">📅 20:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سنتکام قصد دارد یک نیروی جدید پهپادی به نام
«فالکون استرایک»
تشکیل دهد؛ نیرویی چندملیتی که نیروهای آمریکایی و کشورهای منطقه را در یک ساختار مشترک کنار هم قرار می‌دهد. هدف این نیرو استفاده از
پهپادهای تهاجمی یک‌طرفه
(پهپادهایی که پس از حمله به هدف خود نیز از بین می‌روند و شبیه مهمات سرگردان یا «پهپاد انتحاری» هستند) در سه حوزه
هوا، سطح دریا و زیر آب
است. این طرح زیر نظر فرماندهی عملیات ویژه آمریکا شکل می‌گیرد و بر تجربه گروه
«اسکورپیون استرایک»
ساخته می‌شود؛ گروهی که طبق این گزارش، پهپادهای آن پیش‌تر در عملیات علیه ایران استفاده شده‌اند. سنتکام اکنون از کشورهای منطقه دعوت کرده به «فالکون استرایک» بپیوندند تا یک
توان مشترک و یکپارچه پهپادی در سراسر خاورمیانه
برا عملیات ایجاد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20938" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از تنگه صدای پول های بلوکه شده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20937" target="_blank">📅 20:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش صدای انفجار‌ سیریک ، پرتاب موشک/پهپاد به سمت تنگه هرمز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20936" target="_blank">📅 20:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW7fPeADpavdwufebjTeGo-NPCFjjMvxvx2eyJoeTg_BvMYhE7e1oGZN2LTw7xbnd83_lL81XkSydj_uvhQu_zxEgfWnk1JEoiMxY103aCGVHUeqX1uIsIgrgCXKlRedRQTSGSnf_JhREkKchxlpeq_10lBp0Pss-N12JysenJBPo-FCO8Q0tdWe5wdaGrppfwekCciWaRaqm4WloAPkYO6bGy9Q1ABchDIUWTdkqJxAzmtwGwqw2Rm1BWAR2JJwLs4ShIfErKLsiBSQ2Oeaw3s4QiKiVitrmRA6tGWwFl56WIERhQKwtJmA1V0t2L5kKKY47J07qM6Bv_yJG7Yjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هگست وزیر جنگ ، امروز در پاناما و پس از دیدار با خدمه ناوشکن USS Gridley گفت :
محاصره وابسته به حضور یک ناو یا یگان خاص نیست؛ نیروها می‌توانند یکی‌یکی تعویض و جایگزین شوند و بنابراین از نظر نظامی آمریکا می‌تواند آن را برای مدت نامحدود ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20935" target="_blank">📅 20:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرگزاری حوثی‌ها «سبا» به نقل از یک منبع نظامی گزارش داد که حوثی‌ها با استفاده از دو پهپاد به پالایشگاه شرکت آرامکو در منطقه جیزان عربستان سعودی حمله کردند. همچنین اعلام شد: «این حمله در پاسخ به نقض حریم هوایی یمن توسط سعودی در مناطق صعده و حجه انجام شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20934" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال ۱۴ اسرائیل:  رئیس ستاد کل نیروهای مسلح اسرائیل ، ایال زمیر، به وزرای کابینه اعلام کرد که محاصره دریایی ایران بسیار موثر بوده است. طبق ارزیابی‌های اولیه ایالات متحده، مقامات ارشد اکنون بر این باورند که تداوم این فشار شدید اقتصادی هم‌زمان با وخامت سریع بحران مالی داخلی در تهران ،مؤثرترین راهبرد برای وادار کردن رژیم به تسلیم یا زمینه‌سازی برای فروپاشی آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20933" target="_blank">📅 19:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">@WarRoom
بالون</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20932" target="_blank">📅 19:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=B6eJzY8tTSE0YROviR1boWk4Rw1HghrVdRDzoLUPO1l9zJZqDSUnhbrE_w2PnZ-o9Fa1lnje6dMw68zwQCTN_MGMuC7Q35_R5_NPS2AlgZog8K6u4iHknOYxvXZGvHqsZvvWzfIKjjSKhd6Kv126JkX60_thfS58Bx4zMe_YFgMYwHvAenk_PE-SqXQeunL7CxTGlKo9pnBRPXgeo7HYNsQMml0ToOgCqZtZhibSPcTrwB6bS-jNUbAFyy1bScoUKJ-JIofb0zi1_BVMsrIlPV-OHdPq6MLHphzkXEfqd4cA4yiN8Iw-mHr4d_opqPEIvjb8EySwaS3fqwcP1c5IQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=B6eJzY8tTSE0YROviR1boWk4Rw1HghrVdRDzoLUPO1l9zJZqDSUnhbrE_w2PnZ-o9Fa1lnje6dMw68zwQCTN_MGMuC7Q35_R5_NPS2AlgZog8K6u4iHknOYxvXZGvHqsZvvWzfIKjjSKhd6Kv126JkX60_thfS58Bx4zMe_YFgMYwHvAenk_PE-SqXQeunL7CxTGlKo9pnBRPXgeo7HYNsQMml0ToOgCqZtZhibSPcTrwB6bS-jNUbAFyy1bScoUKJ-JIofb0zi1_BVMsrIlPV-OHdPq6MLHphzkXEfqd4cA4yiN8Iw-mHr4d_opqPEIvjb8EySwaS3fqwcP1c5IQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20931" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : جوجی‌جون ، ناو هواپیمابر جورج واشنگتون و اسکورتش به سمت منطقه می آیند
🚨
🚨
🚨
کارهای اداری یادتون نره⁩ https://www.instagram.com/reel/Db-HXkWoJz-/?igsh=NHNmZ3ZhYnhhdDJi</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20929" target="_blank">📅 19:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وال استریت ژورنال : ایالات متحده در بحبوحه تنش‌های جنگ با ایران، ناو هواپیمابر جورج واشنگتون را به خاورمیانه می‌فرستد
@WarRoom
یاشار : خیلی عقبید
😁</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20928" target="_blank">📅 19:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a73c9be9f.mp4?token=FEp42VJUVY5ui8TTdN9HyLXitPNXyv6_0W-zNbgUNZUCQwmToU9wcr0QTWZf3HxJw3t0TyxvpZyikvZ9UI_GnpnKkEen8nUUOrRZY-VINaJmuqCu9d13YKp1ps_9A9X0Z4rluTbySmZiDshZWzgMYO-JojGXPuvBTHSKgy_wIjd_1Tia3aKPKwYjSPyjmLeKBYjP8LRwNwYLWECWTfHNS350GADd6cxbClmRqLe5oKoLJpY3BJO3qAbMYRNICUErgKLbIg40ke9VBuAbbDXeGBjw2tbRoTJvFa7U73YBbW9MwtiRen-vgZgxlJadxzEAK5mmKl_I2-C_y6CHk5dVcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a73c9be9f.mp4?token=FEp42VJUVY5ui8TTdN9HyLXitPNXyv6_0W-zNbgUNZUCQwmToU9wcr0QTWZf3HxJw3t0TyxvpZyikvZ9UI_GnpnKkEen8nUUOrRZY-VINaJmuqCu9d13YKp1ps_9A9X0Z4rluTbySmZiDshZWzgMYO-JojGXPuvBTHSKgy_wIjd_1Tia3aKPKwYjSPyjmLeKBYjP8LRwNwYLWECWTfHNS350GADd6cxbClmRqLe5oKoLJpY3BJO3qAbMYRNICUErgKLbIg40ke9VBuAbbDXeGBjw2tbRoTJvFa7U73YBbW9MwtiRen-vgZgxlJadxzEAK5mmKl_I2-C_y6CHk5dVcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رابرت اف کندی جونیور:
دانا وایت گفته که او هیچ‌وقت ندیده ترامپ آب بنوشد. او فقط نوشابه رژیمی دایت‌کُک می‌نوشد.
او از هر آدم دیگری که تا حالا دیده‌ام، انرژی بیشتری دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20927" target="_blank">📅 18:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جمهوری اسلامی از طریق ترکیه به سوریه اطلاع داد که در صورت دخالت ارتش سوریه در لبنان علیه حزب‌الله، صدها نقطه در سراسر سوریه، از جمله کاخ ریاست‌جمهوری، با پهپادها و موشک‌ها مورد هدف قرار خواهند گرفت.
یک تحلیل اخیر هم صراحتاً می‌گوید ترکیه واشنگتن را متقاعد کرده که از دولت احمد الشرع(پیش‌تر با نام ابومحمد الجولانی)در رویارویی با حزب‌الله در لبنان استفاده نکند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20926" target="_blank">📅 18:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏اوپک: افزایش تولید نفت کشورهای منطقه در حالی که ایران درجا می‌زند
‏گزارش جدید اوپک نشان می‌دهد تولید روزانه نفت عربستان سعودی، کویت و عراق در مجموع طی ماه گذشته نسبت به ژوئن حدود ۱ میلیون و ۶۴۰ هزار بشکه افزایش یافته، در حالی که افزایش تولید نفت ایران تنها ۲۶ هزار بشکه بوده است. پیش از انسداد تنگه هرمز حدود یک پنجم نفت مصرفی جهان از این آبراه عبور می‌کرد، اما کشورهای عربی حوزه خلیج فارس اکنون با استفاده از مسیرهای جایگزین در دریای عمان و دریای سرخ و روش‌های دیگر، صادرات نفت خود را ادامه می‌دهند. در حالی که همسایگان ایران ظرفیت تولید و مسیرهای صادراتی خود را گسترش می‌دهند، صنعت نفت ایران زیر حاکمیت رژیم جمهوری اسلامی عملاً از این رقابت منطقه‌ای عقب مانده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20925" target="_blank">📅 18:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYCk_eD3C2ZvvjkMuMX6zFjYJfeMx3RSVHJr-M6ykgfas14aoPgA9xKf34xpNhgNuN7xqgCdd_5wbdMkWc6BALnqYhA166EDKPUFbVVdlALz7LYPaZem7w-wy73zNFDikzGZcYt320t3-Zy8HwB_rG9H22ROfFuaVLCUGFrTq0Q7zWqlBb3_adXl7i3PJlJQC6ds7LnJ50JLS29Z-ksWNs1YvdrVWHhePxJl18XNOlSjPo4yfSKTkVF_ZLyDQtba6fB6J1UVPKf-Rb34lex_PekWXLUOaaSDT8rxV-EiFx_hDRpr1mIY0KhcfAzTwMqsmxbfYopktn_vmlc9h4b5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : جوجی‌جون ، ناو هواپیمابر جورج واشنگتون و اسکورتش به سمت منطقه می آیند
🚨
🚨
🚨
کارهای اداری یادتون نره⁩ https://www.instagram.com/reel/Db-HXkWoJz-/?igsh=NHNmZ3ZhYnhhdDJi</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20924" target="_blank">📅 18:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwxxnGJQtpoOkyjzDlBpBLa0o0E_PKg-bqh0IyHrFyeRBBxXxovEeot4Ixa3-HYaCKHVUrnsBtCAyFsyXl7my23MM2cTGQ8pOhanlFTvJ0O98OlXYtc9Brn458BCqBNRK5fhl3s3eMzDHBR4rZTBkvl4s80LDjq-oaKOUaxE6t8lah6dNvusILREPcU2Gt_50WZwWBIXLDHZeD3EkDC9odasJpTlut-mwY7neVsgopghiGMXy5mYT6Lag4qRaUCVOvBFNQagEIAWLtW3gAQsX5MVJswcbjhORUNZF36ikFTbvfPNEFrxOiuY-hU0rdkgJUFkRKfSbMs2ZPEamzajOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عروس معصومه ابتکار(شامپانزه دیوار سفارت) که اقامت دائمش در آمریکا لغو شده، وکیلی حرفه‌ای گرفته و از دولت آمریکا شکایت کرده، به این امید که اقامتش برگردد و غرامتش را از اموال بلوکه‌شده بگیرد. او نامه‌ای خطاب به مردم آمریکا نوشته: «من عاشق آمریکا هستم، فرزندم فارسی بلد نیست و مادربزرگم در اشغال سفارت آمریکا فقط مترجم بود.» استدلال نامه و وکیل ایشان این است که فرزندان نباید به‌جای والدین مجازات شوند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20923" target="_blank">📅 17:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8PnWuFhx73pb_rcPybBoi82h-mA3gt380tJKfmxGA7bZVJOnFMtuJwJNXJ88OsH-FinzpIoECNGmlakluhZIvDOn8OKSMxeh7e3vqsurrW-FL4IhkOA5zOUP2ZB-QGFUBpygc-VqYPOFszIQXT5eCHIzYFSdBUwzXmgRNFgbplQyZ0Dkijx5XFKSJcxAb1DibW-YpY5eKaZUCb6DvmFdes5C1blFgvvpd5njgiiZDrrf5Mn2eoAU_noLKgXExFtS7Ur5bf1wkiDHk6TLW7n1GJpogc2PqHzpK9o6y7p-moDKt9En62Nnxx5l2NlJAH3IL96WrT7_rmpgxh8iRtAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواب بودم ، پیج روزدن
دیر برگردوندم
🙌🏾
😂
instagram.com/yashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20922" target="_blank">📅 17:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76aaa280.mp4?token=FotA-24OhZ79a6lrMPsSu-GZrtUtQUCtj4yN5pUnBTI3z6f4yWGLDGgV62vP3F-TZJJYOy1be96ngs6YaZXNLEGNYEr63oG9oje6cTFAaGame7zs9m_iZevIoLMuo7xAUhOcRPBc_lsLDE6TtX27yysnhaVD6Mg5Lh4awAUCmf33v6c44ivFa40hTkQ7PmJIXsMg72y0tgNWeORzqWQR5Q13oOplDX1ZE5lzaBWUQWpbqcglI7eRoMPhzF7iU3xBEHoA66y52hKS937LI5sxqvKdBzq9NLPgCS7VbSt7alXn5Wt5cak3MrUNJ562wKWaA_H41nDUnMMdAiFe_kakWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76aaa280.mp4?token=FotA-24OhZ79a6lrMPsSu-GZrtUtQUCtj4yN5pUnBTI3z6f4yWGLDGgV62vP3F-TZJJYOy1be96ngs6YaZXNLEGNYEr63oG9oje6cTFAaGame7zs9m_iZevIoLMuo7xAUhOcRPBc_lsLDE6TtX27yysnhaVD6Mg5Lh4awAUCmf33v6c44ivFa40hTkQ7PmJIXsMg72y0tgNWeORzqWQR5Q13oOplDX1ZE5lzaBWUQWpbqcglI7eRoMPhzF7iU3xBEHoA66y52hKS937LI5sxqvKdBzq9NLPgCS7VbSt7alXn5Wt5cak3MrUNJ562wKWaA_H41nDUnMMdAiFe_kakWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: شاید بتوانید بریتانیا را «جمهوری اسلامی بریتانیا» نامید
یک نفر گفت که اولین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
ما داریم مطمئن می‌شیم که یه مورد دیگه مثل این، یعنی ایران، نداشته باشیم
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20921" target="_blank">📅 17:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1jeOz3XT3ILs-89od2hxCw4on1KZYiezXj6seEq12lQ4WHbkbeqxmP4g4BJ_1N8qB-JJMMAyh0vzHb0LrQRbvth_z8l1ovFdL0kVjB7ZhsIDmPYB5HGanImFCVaclG_z3CPq4VXKL327w7UDn-mf0hW9qiyA3j3moPmU7newwHIR3eoOB_t0zQg9z3b-qnBH3X-axu8QMjsWcIcH1yaQYzXXhYeAd8wCzMNbVNoiVMsjaUH0RPhWF1ey74s_b57hCCKPveE5QqasL1qu-FhTxlMicwCmML46ingBKHpNJZxmdb5o12zWk6j70nSXQowlLNBmWfYC5_q_K2BIZXm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گفته کنعانی، مدیرکل حفاظت محیط زیست ایران، سطح آب دریای کاسپین به پایین‌ترین حد خود در نزدیک به ۲۰۰ سال گذشته رسیده است.
کارشناسان می‌گویند یکی از عوامل اصلی، روسیه است که با ساخت بیش از ۴۰ سد عظیم، رودخانه ولگا - شریان حیاتی اصلی دریا - را مسدود می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20920" target="_blank">📅 14:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjS5pxK4nE3br6wk4dYe7tAG7a9kfdkpLV6veMI3JQPxgvXklm7DjLJqPIpyNZoRjpoErtBTfm7zQfq_i76SHivJzVVCqsqE-4e4tN_cu75YnkHN6Irq_WmLr-wMUqIKLsmku7bePYo_1hquQXqnqKetGVocb9Z8soBe44VTgwmJDMDLgUCP-u4zBi0IHuJ3t_z3Wcgraea0kgh9KVIkAp4GYd4by6wKrKgyTgzBhptf9BHfidtVO921gyq1EVjAaQl6ujcRFAcBou6-VoaZxjwTsH1-eliyPLpZRVj3OxmGOLQRNlCM_Hf5kfsLqXT3Mg4rdmxNDRHuXE-_1lsnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرگرد ابوالفضل حیدری، نیروی هوافضای سپاه ، امروز در یک سوء قصد با موتورسیکلت در زابل، استان سیستان و بلوچستان، به شدت زخمی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20919" target="_blank">📅 14:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96bba2676.mp4?token=nuzocsq1yuxhm7WbGNe8OlqIDbs6baPsUYAKaIBpgn_iOi9hpwqYzpnehYHh2e--uDXjlGr0rF6WlfDI7pmbiacsMy6mgKZndqTmBiYQMcIsGTgeYGSzWDlzIGI8En6VeGFLP5i9lkiC_E8qtrxh0zAYKDECOzLPx1pyrNv0fmoksHdXHSV4vhtFxUBURmkH2lmJspFRGlTjE20fVgjNLUIP2WkVK3ZTwcHrnF3f7qMlZRMRTTEgDkAYcJvZ-A11xjrJJt4P4LKupoBqbBnLnD90Yz049iL5qsbVePk5ip5RmQA7s4S7yg2ltCap6qnFD8nemey0gUawhvtGmMCK-TH9KSZ2sUokHhPiBwWLZOR6R0DdtMB272P0uh7nKmR1fmDYZetRt4gm9xVJGrz0tdzAaiyCoKh2QnZ1XYwTt0WZQPz5IlT5iZMcx2kpc57228ETkYGGP57VDFkNCOvUhdK5vJZd06_prXwVoVeLo6jJroGUNVVd_v-EEvrDbx5vHT5hhgSIO-dsVIsLZe4sFINLvxdK1MUW8iftgu4Tqt89NZ_kISTbI--zekDZFnPAnpnKyPx4RQolstW-9EEeVxLJba0RbUWVH0aOfJnC9PrpT6YD9zc2V-9sTDm8BYPw-1p1RtV3E8Ifu9FxkHKYcFgns86W1FHdeGeIe77ATmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96bba2676.mp4?token=nuzocsq1yuxhm7WbGNe8OlqIDbs6baPsUYAKaIBpgn_iOi9hpwqYzpnehYHh2e--uDXjlGr0rF6WlfDI7pmbiacsMy6mgKZndqTmBiYQMcIsGTgeYGSzWDlzIGI8En6VeGFLP5i9lkiC_E8qtrxh0zAYKDECOzLPx1pyrNv0fmoksHdXHSV4vhtFxUBURmkH2lmJspFRGlTjE20fVgjNLUIP2WkVK3ZTwcHrnF3f7qMlZRMRTTEgDkAYcJvZ-A11xjrJJt4P4LKupoBqbBnLnD90Yz049iL5qsbVePk5ip5RmQA7s4S7yg2ltCap6qnFD8nemey0gUawhvtGmMCK-TH9KSZ2sUokHhPiBwWLZOR6R0DdtMB272P0uh7nKmR1fmDYZetRt4gm9xVJGrz0tdzAaiyCoKh2QnZ1XYwTt0WZQPz5IlT5iZMcx2kpc57228ETkYGGP57VDFkNCOvUhdK5vJZd06_prXwVoVeLo6jJroGUNVVd_v-EEvrDbx5vHT5hhgSIO-dsVIsLZe4sFINLvxdK1MUW8iftgu4Tqt89NZ_kISTbI--zekDZFnPAnpnKyPx4RQolstW-9EEeVxLJba0RbUWVH0aOfJnC9PrpT6YD9zc2V-9sTDm8BYPw-1p1RtV3E8Ifu9FxkHKYcFgns86W1FHdeGeIe77ATmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏اظهارات کم‌سابقه سناتور تام کاتن درباره راز وقایع مرداد ۱۳۳۲ در برنامه هفتگی پربیننده مارک لوین در شبکه فاکس‌نیوز
‏«اوباما ادعا کرد که ما نخست‌وزیر منتخب دموکراتیک ایران را در ۱۳۳۲ سرنگون کردیم. این یک افسانه کامل است. او (مصدق) نخست‌وزیر دموکراتیک نبود. او اساسا سرنگون نشد...
..(برعکس)، مصدق کسی بود که سعی کرد قدرت را تصاحب و به طور غیرقانونی حفظ کند. ولی باراک اوباما با مغز استخوانش باور داشت و بارها درباره آن نوشت و سخنرانی کرد که آمریکا برای دهه‌ها تنش با ایران سزاوار سرزنش است و برای همین هم به دنبال توافق بهتری نبود.»
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20918" target="_blank">📅 12:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فرمانده ستاد کل نیروهای دفاعی اسرائیل، ایل زمیر، به وزرای کابینه در مورد وضعیت اقتصادی ایران گفت: تحریم‌ها علیه ایران بسیار موثر بوده است. بحران اقتصادی در آنجا رو به وخامت است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20917" target="_blank">📅 12:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سناتورهای دموکرات کنگره آمریکا خواستار بررسی شرایط ناو یواس‌اس آبراهام لینکلن شدند؛ این درخواست پس از گزارش‌هایی درباره کمبود غذا، خرابی لوله‌کشی و بحران‌های سلامت روان در طولانی‌ترین مأموریت تاریخ ناو مطرح شد.
سناتور روبن گایگو نیز خواستار بازدید رسمی و نظارتی یک هیئت دوحزبی سنا از ناو برای بررسی شرایط گزارش‌شده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20916" target="_blank">📅 11:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20915" target="_blank">📅 11:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEx7hRJYM7g_AZfVBpQYMS6IScT3zJaMFVjB3YnjxCGH3CQQV7Ptz1EiggbLupTJZGBLZRa8RI3ILXBb5BJfAE2yO-nvlpHjMZMFvSP4BmrY1GOA135jZNhZXVpoXj4S_INDiVl2033ZTNX5ftqSIjyV1oos1h9H7ug_ntLKWZh5p6kuZDQOPFSINxcTjZ34pnTQX48P3m_uFNYsr4yzo2QCysjgCJ4g_4zHQc4tCKxlCyjOlqt8IhWHssMLYvb2qxgQ_Cq7APYIApaj4HuAYPEYcoqg8O9UDR9seMlALJQhn5QfAk18Qmmf1HCQ3nIyI1KjS28RQhnE89eRCQAfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : جوجی‌جون ، ناو هواپیمابر جورج واشنگتون و اسکورتش به سمت منطقه می آیند
🚨
🚨
🚨
کارهای اداری یادتون نره⁩
https://www.instagram.com/reel/Db-HXkWoJz-/?igsh=NHNmZ3ZhYnhhdDJi</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20914" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20913" target="_blank">📅 09:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20912" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شب گذشته از ترس شروع اعتراضات و انفجار جامعه افزایش قیمت بنزین هشتاد و هفت هزار تومانی در کرمان، کمتر از یک ساعت پس از آغاز اجرا متوقف شد و قیمت بنزین به نرخ قبلی برگشت.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20911" target="_blank">📅 08:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کانال‌های عبری : خبر گران شدن بنزین در ایران باعث شد خبر انتقال پنهانی طلا و دلار به ایران، در حاشیه قرار بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20909" target="_blank">📅 04:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پیت هگست، وزیر جنگ : رئیس جمهور ترامپ، سوءاستفاده را برنمی‌تابد. ما اینجا برای بازی کردن نیامده‌ایم.
شهروندان و ملت‌های ما شایسته و منتظر اقدامات واقعی و ملموس هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20908" target="_blank">📅 23:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی امروز کشتی باری «ولا نوا» با پرچم پاناما را هنگام حرکت به سمت یکی از بنادر ایران در خلیج عمان متوقف کردند. پس از بی‌توجهی خدمه به هشدارهای آمریکا، یک بالگرد MH-60 دو موشک هل فایر به اتاق موتور کشتی شلیک کرد و سامانه هدایت…</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20907" target="_blank">📅 23:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ در تروث : کارولین لیویت، سخنگوی فوق‌العاده کاخ سفید و یکی از مورداعتمادترین دستیاران من، در پایان این ماه از سمت خود کناره‌گیری خواهد کرد تا بتواند زمان بیشتری را با فرزندان خردسال دوست‌داشتنی و خانواده‌اش بگذراند
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20906" target="_blank">📅 23:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">@WarRoom
ترامپ پوکر باز</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20905" target="_blank">📅 22:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20904">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20904" target="_blank">📅 22:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=cRONNzL2JuixrA8LxCjPxweeL4Ri4FFc2AFeZeXG-sExb4kzmIOPXHQsVye_GYui3YEnXyfPx91Wx4PlA8h_0W7FQRGGwZt5V0955dMCo6Jtby0Y4wAZg1gjYcarJK3BicIR3ZoEXTrTMM6O0HfRM9hA5sqmN--w1AvKb6VoQxglhHlRBbyUcyR8xnkSzTO69j8iPvdt0T7G7n9yv_5fYQoxrYTC0Mi4lFBT1J8TToUOge0RRC9acyKqhjnhIUZVldq0i7XAnk6tq2BZflZBz4u6aeqQBMqQjmqZQ9RKS1OO5XrqzijSqRYWnKsJ-LDowuR3lTuNbzIY6Vq9b5_rkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=cRONNzL2JuixrA8LxCjPxweeL4Ri4FFc2AFeZeXG-sExb4kzmIOPXHQsVye_GYui3YEnXyfPx91Wx4PlA8h_0W7FQRGGwZt5V0955dMCo6Jtby0Y4wAZg1gjYcarJK3BicIR3ZoEXTrTMM6O0HfRM9hA5sqmN--w1AvKb6VoQxglhHlRBbyUcyR8xnkSzTO69j8iPvdt0T7G7n9yv_5fYQoxrYTC0Mi4lFBT1J8TToUOge0RRC9acyKqhjnhIUZVldq0i7XAnk6tq2BZflZBz4u6aeqQBMqQjmqZQ9RKS1OO5XrqzijSqRYWnKsJ-LDowuR3lTuNbzIY6Vq9b5_rkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20903" target="_blank">📅 22:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صدای موشک اقتصادی
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20902" target="_blank">📅 21:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">طرح امتحانی بنزین ۴ نرخی آغاز شد!
نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان
نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان
نرخ سوم: ۴۰ لیتر با نرخ ۵۰۰۰ تومان
نرخ چهارم: ۸۷,۲۰۰ تومان
این طرح هنوز به طور رسمی کامل اجرا نشده و اکنون محدود به ۲۰۴ جایگاه سوخت در استان کرمان میباشد.
﻿
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20901" target="_blank">📅 21:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کانال ۱۱ اسرائیل : با کمک ماهواره‌های روسی ، حملات حوثی‌ها به عربستان سعودی و نیروهای آن در یمن هم افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20900" target="_blank">📅 21:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گاردین به نقل از چند منبع : ناو هواپیمابر «آبراهام لینکلن» پس از حدود ۹ ماه مأموریت مداوم و ۲۵۰ روز حضور پیوسته در دریا، با افت شدید روحیه و فشار روانی خدمه مواجه شده است. خانواده‌ها و برخی ملوانان از مشکلاتی مانند محدودیت غذا و آب، اختلال طولانی در شست‌وشوی لباس‌ها و دست‌کم یک مورد تلاش برای پریدن از کشتی که مهار شده، خبر داده‌اند. نیروی دریایی آمریکا نیز در حال آماده‌سازی ناو «تئودور روزولت» برای جایگزینی لینکلن است، هرچند زمان دقیق این جابه‌جایی به دلایل عملیاتی اعلام نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20899" target="_blank">📅 21:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏وزیر دفاع اسرائیل: من به ارتش اسرائیل دستور داده‌ام که تمام اقدامات لازم را برای حضور طولانی مدت در منطقه امنیتی لبنان، سوریه و غزه انجام دهد. ‏ارتش در منطقه امنیتی لبنان، سوریه و غزه برای دفاع از تمام اسرائیل باقی خواهد ماند. @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20898" target="_blank">📅 20:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مشاور ارشد قالیباف :آ مریکا و اسرائیل برای یک حمله نظامی پیش از انتخابات سراسری در اسرائیل و انتخابات کنگره آمریکا در آبان ماه،آماده می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20897" target="_blank">📅 19:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزیر کشور پاکستان در ایران به عراقچی، وزیر امور خارجه، اطمینان داد که "توافق دفاعی مکه" به عنوان یک ائتلاف علیه رژیم ایران طراحی نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20896" target="_blank">📅 19:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42557aaa83.mp4?token=O2fRc82F7n-TF8sRA_QCYrJsXIuXHbjYoVcTooxtZTd-JbBmdUebNEQIWdADtsV5DFpkL7z2uJVeZ92H8jVQDdW-dc-9bNK0E0s84y5mpIsKAsFiF3SvN-rghf-qxYaFoEvnbti1uYXM7ExzeswQ1vizQKN9tVvEdt6jk3YV1ta0MFg5_uBf3adX7158yR6FoMuqflaDpAI_gcV6I0h54szgWmUjNUgcq4BriAPbOeX0vnmCUshDCXeYw6GdXc5_4GYQkMKGdrGEyLi7-xy5VUBTz8xrJTe-hQgKfuKcbM1OTHRGhWTwX4T2FTdv5idJkKqeTH0z0CsycrJzpW38cgjcOesTrtJxySBgffGMnrP40SWg0fUlhyqmIeD7pznKvLKzTQWAbfNFXHUez3DfB3-h-NgUpRlIeFBloo2hdT7NoK46LYCAVinQLBpLGiqZGxkyA6O978oC16dQwNFyURbu4Ve0R749duXDzOM_UQedt3RdR2vHmth5NX58VRbWYjrkVJKMRM-e7BI3ZSMjZjBjYdQGAb0g4P3s0vskNwpkDF7iweMOvNDmg0YXgi5a_t69heIAnGQjoffQhCYbJRRI-c23pnsxmqsJm1qSPFafO7avv_XOQ5pgpNHPxt-sgYCZRFzfG4sbjwpDFnPKzEcWh8WBjYUEHu2U_gk6Xy4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42557aaa83.mp4?token=O2fRc82F7n-TF8sRA_QCYrJsXIuXHbjYoVcTooxtZTd-JbBmdUebNEQIWdADtsV5DFpkL7z2uJVeZ92H8jVQDdW-dc-9bNK0E0s84y5mpIsKAsFiF3SvN-rghf-qxYaFoEvnbti1uYXM7ExzeswQ1vizQKN9tVvEdt6jk3YV1ta0MFg5_uBf3adX7158yR6FoMuqflaDpAI_gcV6I0h54szgWmUjNUgcq4BriAPbOeX0vnmCUshDCXeYw6GdXc5_4GYQkMKGdrGEyLi7-xy5VUBTz8xrJTe-hQgKfuKcbM1OTHRGhWTwX4T2FTdv5idJkKqeTH0z0CsycrJzpW38cgjcOesTrtJxySBgffGMnrP40SWg0fUlhyqmIeD7pznKvLKzTQWAbfNFXHUez3DfB3-h-NgUpRlIeFBloo2hdT7NoK46LYCAVinQLBpLGiqZGxkyA6O978oC16dQwNFyURbu4Ve0R749duXDzOM_UQedt3RdR2vHmth5NX58VRbWYjrkVJKMRM-e7BI3ZSMjZjBjYdQGAb0g4P3s0vskNwpkDF7iweMOvNDmg0YXgi5a_t69heIAnGQjoffQhCYbJRRI-c23pnsxmqsJm1qSPFafO7avv_XOQ5pgpNHPxt-sgYCZRFzfG4sbjwpDFnPKzEcWh8WBjYUEHu2U_gk6Xy4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏وزیر دفاع اسرائیل: من به ارتش اسرائیل دستور داده‌ام که تمام اقدامات لازم را برای حضور طولانی مدت در منطقه امنیتی لبنان، سوریه و غزه انجام دهد.
‏ارتش در منطقه امنیتی لبنان، سوریه و غزه برای دفاع از تمام اسرائیل باقی خواهد ماند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20895" target="_blank">📅 18:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امروز،
۱۲ اوت ۲۰۲۶
، آسمان شاهد هم‌زمانی
چهار پدیده نجومی
است:
صف‌آرایی شش سیاره
شامل مشتری، عطارد، مریخ، زحل، اورانوس و نپتون که پیش از طلوع خورشید در امتداد بخشی از آسمان دیده می‌شوند؛
خورشیدگرفتگی کامل
که اوج آن حدود
۲۱:۱۷ به وقت تهران
خواهد بود و در ایران دیده نمی‌شود؛
اوج بارش شهابی برساوشی
که از امشب تا بامداد ۱۳ اوت ادامه دارد و در شرایط مناسب می‌تواند ده‌ها شهاب در ساعت ایجاد کند؛ و در نهایت
ماه نو
که یعنی ماه تقریباً بین زمین و خورشید قرار می‌گیرد و از زمین دیده نمی‌شود. نبود نور ماه باعث می‌شود آسمان تاریک‌تر شده و شرایط برای تماشای برساوشی‌ها بسیار مناسب باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20894" target="_blank">📅 18:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0sRhxwrwKcZYGOS-pBW5pqWALkAZXc5aP1KUCTzFIQvmWoJ_LJsItrkGt2wjHAA6Ibws67mIJEKxny1WzZmqM6DcZkgn1G7RxjCdZCbiPmTOaB-jDeRS0syCqhxIanA2OIBKShUzpToWCt6kDxezHR9PYnrPZdmAS3zzg4IZY-eeInFPQA30yr7URWIfVMeV6Dsm52ATdW2XpaFx0AJvIRMX6OiI7HGErNruP_locoLzrBpHShOoZQarZxyqUxGFz2DaKx4RfGv-_d52_W6gwJYxnKDLkvrYiMsfKeilmr0_wIa1OQ2883PJFJeHeF1TRlGQoaNZb3AHgYFLDdvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد! محاصره دریایی ما از سوی همه «دیوار فولادی» نامیده می‌شود و ایران هیچ کاری از دستش برای مقابله با آن برنمی‌آید. آنها نیروی دریایی ندارند، نیروی هوایی ندارند، سربازان باقی‌مانده‌شان حقوق دریافت نمی‌کنند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است و «رهبری» آنها، در بهترین حالت، نامطمئن است! آنها پولی ندارند؛ کشورشان «ویران» شده است. تنها چیزی که دارند اخبار جعلی و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر می‌شود! ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند؛ دیگر قلدر خاورمیانه نیست. ستایش از آنِ الله باد!
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20891" target="_blank">📅 18:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7908fd3c.mp4?token=UsyngqWskNSG5KDLCQ0WL7mEkSvMICUg_P1SV9WE5dSThfyPOziiwmj_yoVQzIrnCQAcAkTNTpJIj73ozYWDMsj9rOPdug0Tt6a7Wyl8ZCq2p-yv-etStsYVFaGFZs2KkzNWQcwAhNpQefrr0oFNVeFr0vGl-uyv2Wyz9-RQnXbySg14OKsmZZI3F736Wkk9xgGRbleIoQhWsELm0Kp7-jDXHMQfamvt2jYeqOZ5VSWiJHKakZ1C7sJcB02lP1FS60Q342GqSP3zOIH1vKMDmG47qnPdd-yfjgN83bktuKY6Nri_ypOGh9iAJcxX3mDYWGpef2YY51JoWyfY_qFEzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7908fd3c.mp4?token=UsyngqWskNSG5KDLCQ0WL7mEkSvMICUg_P1SV9WE5dSThfyPOziiwmj_yoVQzIrnCQAcAkTNTpJIj73ozYWDMsj9rOPdug0Tt6a7Wyl8ZCq2p-yv-etStsYVFaGFZs2KkzNWQcwAhNpQefrr0oFNVeFr0vGl-uyv2Wyz9-RQnXbySg14OKsmZZI3F736Wkk9xgGRbleIoQhWsELm0Kp7-jDXHMQfamvt2jYeqOZ5VSWiJHKakZ1C7sJcB02lP1FS60Q342GqSP3zOIH1vKMDmG47qnPdd-yfjgN83bktuKY6Nri_ypOGh9iAJcxX3mDYWGpef2YY51JoWyfY_qFEzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منم مشکلات زیادی دارم ولی برای شما شاد هستم
😍
🙌🏾
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20890" target="_blank">📅 18:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20889" target="_blank">📅 18:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش CNN: وزارت امور خارجه آمریکا به دلیل تنش های احتمالی به سفارت‌های این کشور در خاورمیانه دستور داده است تا برنامه‌هایی را آماده کنند که به آن‌ها اجازه دهد با تعداد محدودی از کارکنان به فعالیت خود ادامه دهند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20888" target="_blank">📅 17:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6ab93f52.mp4?token=fQ2yTSZ1N9Nt2d_iSFlKpWA8uHSecdyAggpqBJ4tf-yMUkBprsviKx7tBGbX0OYrM5m1fUD8E0OWOOb259JosrBKtRbhV_zp5ZSvw5DMZ-WVSrwnFSARs2erj6D9DTX63wpxcWv1pLcR9voH_-ZSddhSMPlqtfrSeQnCvEo-M3KjoSKFZpxKZYL8KVqQ7FSlIE1MojDZOkafTM1O-HTRk2UGluMlmdg7qX_L_k7vDYzeRf4mh7G9p6Nvbr1mPG7fPTzu7KjCcb18-km5vG8sYwlZnm991ypu1qzg343lc96JUrSRm4a-svvMLKN3PNrAfw2ohy5NxIc1K5fXjHJHVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6ab93f52.mp4?token=fQ2yTSZ1N9Nt2d_iSFlKpWA8uHSecdyAggpqBJ4tf-yMUkBprsviKx7tBGbX0OYrM5m1fUD8E0OWOOb259JosrBKtRbhV_zp5ZSvw5DMZ-WVSrwnFSARs2erj6D9DTX63wpxcWv1pLcR9voH_-ZSddhSMPlqtfrSeQnCvEo-M3KjoSKFZpxKZYL8KVqQ7FSlIE1MojDZOkafTM1O-HTRk2UGluMlmdg7qX_L_k7vDYzeRf4mh7G9p6Nvbr1mPG7fPTzu7KjCcb18-km5vG8sYwlZnm991ypu1qzg343lc96JUrSRm4a-svvMLKN3PNrAfw2ohy5NxIc1K5fXjHJHVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری پی بی اس: چرا مجتبی خامنه‌ای در طول این جنگ هرگز در ملاء عام دیده نشده است؟
محمدرضا نقدی: استراتژی متعل به اوست. دشمن ما جنایتکار است و به هیچ قانونی پایبند نیست.
مجری: آیا این به دلایل امنیتی است؟
نقدی: طبیعتاً به دلیل امنیت است. مطمئناً دلیل دیگری وجود ندارد.
مجری: آیا او را دیده‌اید؟
مجری: بیایید این موضوع را کنار بگذاریم.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20887" target="_blank">📅 17:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7137b6f963.mp4?token=KAl7nx6BIdWfADkYf__TuCXsx1ONgIEVcVpNlMLBmcBUnDfsef3Pln2R5WxuaDrHQCfQMdeqDpfumaKrPfn9HEROUljMYcHQ7Iw19n05h4yUZWjCWbBTaqBLnWoPzkFWU8Yn_5v5UEKHS1GJw8bdv_QEt0VKohn6DqRgawP78ENHH6hqZ9ScBlHk49vxaYfJpSP8BBIIIYsfh788G5LRWjYMGCE9EKJTM_En5ZIk_Tc4sD0F5LhxoqXbOWuWYBTdC1m84AIdoR-6YjjXQJqoYAJJvTOBeX0tvbmZC_wDRRaR8rVb4Dm6lz1DEyqDjiSLilzmA--bAiO3WGDu8RStJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7137b6f963.mp4?token=KAl7nx6BIdWfADkYf__TuCXsx1ONgIEVcVpNlMLBmcBUnDfsef3Pln2R5WxuaDrHQCfQMdeqDpfumaKrPfn9HEROUljMYcHQ7Iw19n05h4yUZWjCWbBTaqBLnWoPzkFWU8Yn_5v5UEKHS1GJw8bdv_QEt0VKohn6DqRgawP78ENHH6hqZ9ScBlHk49vxaYfJpSP8BBIIIYsfh788G5LRWjYMGCE9EKJTM_En5ZIk_Tc4sD0F5LhxoqXbOWuWYBTdC1m84AIdoR-6YjjXQJqoYAJJvTOBeX0tvbmZC_wDRRaR8rVb4Dm6lz1DEyqDjiSLilzmA--bAiO3WGDu8RStJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری آمریکایی پی‌بی‌اس : آیا هدف ایران این است که این جنگ را طولانی‌تر کند، شاید تا زمانی که آقای ترامپ از قدرت کنار برود؟
نقدی، فرمانده سپاه: ببینید، ما باید به بازدارندگی برسیم تا دشمن هرگز جرات حمله به ما را نداشته باشد تا بتوانیم با امنیت زندگی کنیم.
یک راه این است که این جنگ را تا رسیدن به دوره بعدی ریاست جمهوری ادامه دهیم و فرسایش ایجاد کنیم تا اگر کسی بخواهد به ایران حمله کند، بداند که هزینه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20886" target="_blank">📅 16:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn0_9iv1BnVPusJilN58RJRPlM5pQVWDqLq7JQ3_BAylvmfRx2LoPUBtY7Sh39sPePlvXi-_Ma5AVuabn2li8NITQyFq4ahHt0RiI9BHfylM8OqslRV9Zn7Wv8koozljhKUiWZzT68924EhPd6N2upUyijPr2FKgTWGN2K8ctr97P7mhSbvygzy0XIBfM6Ft2-9XW93Gujzxw3naiaXES85IzuZ2QVXJkMQISeGfQlt9m4MgyAyGiIKXucYrXTmwhB0qg9AMnYUaSKFGGMtnyfqgJcu4cRchHI40jEMrnQEA_pBmM53AY1jMJsykwMlPXS_jwSDDTwfGafr9gzRfCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهلوان آواز ، «ایرج» خواجه امیری،  خواننده قدیمی در ۹۴سالگی درگذشت
بخش بزرگی از ماندگاری صدای ایرج در سینمای پیش از انقلاب، به ترانه‌هایی برمی‌گردد که صدای او روی تصویر
محمدعلی فردین
است. ایرج خودش گفته بود در
۲۶ فیلم
به جای فردین آواز خوانده است. در مجموع هم گفته بود برای
۱۳۵ فیلم
خوانندگی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20885" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجار های جاسک رو اعلام کردن کنترل شدست ، هم اکنون باز‌ داره گزارش‌ میشه
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20884" target="_blank">📅 16:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">«الحدث» به نقل از منابع آگاه گزارش داد که اسماعیل قاآنی، فرمانده نیروی قدس سپاه، در سفر غیرعلنی اخیر خود به بغداد با رهبران حشدالشعبی، گروه‌های مسلح و چهره‌هایی از ائتلاف‌های سیاسی عراق دیدار کرده و
پرونده حصر سلاح در دست دولت
را بررسی کرده است. طبق گزارش‌های تکمیلی، قاآنی از گروه‌ها خواسته از هرگونه درگیری با نیروهای دولتی جلوگیری کنند، اما هم‌زمان با
تحویل کامل سلاح به دولت عراق موافقت نکرده
و بر حفظ توان نظامی این گروه‌ها در برابر آنچه «تهدیدهای آمریکا» خوانده شده تأکید کرده است. دولت عراق برای تعیین تکلیف سلاح گروه‌های مسلح خارج از نهادهای دولتی،
۳۰ سپتامبر ۲۰۲۶
را مهلت نهایی تعیین کرده و پس از آن قرار است با فعالیت مسلحانه خارج از چارچوب دولت برخورد شود.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20883" target="_blank">📅 15:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پزشکیان: جنگ کنونی از قبلی بسیار پیچیده تر است و دشمن قصد فروپاشی نظام از داخل کشور را دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20882" target="_blank">📅 15:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبرگزاری آناتولی به نقل از منابع دولتی پاکستان گزارش داد تفاهم‌نامه قرار است در ۱۷ اوت منقضی شود. به گفته یک منبع نزدیک به روند میانجیگری، دو طرف موافقت خود را با اصل تمدید مهلت به میانجی‌ها اعلام کرده‌اند، اما هنوز درباره مدت دقیق تمدید تصمیم نهایی گرفته…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20881" target="_blank">📅 15:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرگزاری آناتولی به نقل از منابع دولتی پاکستان گزارش داد تفاهم‌نامه قرار است در
۱۷ اوت
منقضی شود. به گفته یک منبع نزدیک به روند میانجیگری، دو طرف موافقت خود را با اصل تمدید مهلت به میانجی‌ها اعلام کرده‌اند، اما
هنوز درباره مدت دقیق تمدید تصمیم نهایی گرفته نشده و تهران و واشنگتن در حال تبادل پیام برای تعیین بازه تمدید هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20880" target="_blank">📅 15:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یک منبع ارشد ایرانی به رویترز گفت:
هیچ بحثی برای تمدید آتش‌بس بین آمریکا و ایران وجود ندارد و در عوض، مذاکرات بر بازگشت احتمالی آمریکا به توافق‌نامه تفاهم (MOU) و یک جدول زمانی برای اجرای تعهدات متمرکز است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20879" target="_blank">📅 14:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش صدای انفجار‌ در‌ جاسک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20878" target="_blank">📅 14:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:
فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند. ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20877" target="_blank">📅 13:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بلومبرگ : ایران در دور بعدی جنگ، به سمت یک وضعیت نظامی "تهاجمی" پیش می‌رود. این کشور در حال بازسازی ارتش خود است تا آن را انعطاف‌پذیرتر و تهاجمی‌تر در برابر تهدیدات خارجی کند. این اقدام، در سایه جنگ با ایالات متحده و اسرائیل، نشان‌دهنده آمادگی ایران برای یک رویارویی طولانی‌مدت است، حتی اگر درگیری فعلی به پایان برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20876" target="_blank">📅 13:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نیویورک تایمز: در نزدیکی اجلاس ناتو در ترکیه شخصی با موشک دوش پرتاب شناسایی شد!
نیویورک تایمز گزارش می‌دهد که تهدید ایران که ماه گذشته باعث تبادل مخفیانه هواپیمای رئیس جمهور ترامپ شد، در حالی آشکار شد که او در آخرین روز حضورش در اجلاس ناتو در آنکارا، ترکیه، در 8 ژوئیه حضور داشت.
سازمان اطلاعات ایالات متحده چندی  جریان اطلاعاتی دریافت کرد که نشان دهنده یک تهدید موشکی زمین به هوا علیه هواپیمای رئیس جمهور بود، صرف نظر از اینکه کدام هواپیما حامل رئیس جمهور بود.
همچنین شخصی در نزدیکی اجلاس ناتو با یک موشک دوش پرتاب مشاهده شد، در حالی که عوامل ایرانی دقیقاً می‌دانستند ترامپ در آنکارا کجا اقامت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20875" target="_blank">📅 13:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سازمان بین‌المللی دریانوردی:
نشت نفت از نفتکشی که در شمال شرق جزیره قبلیه عمان به گل نشسته است.
انتظار می‌رود نشت نفت از نفتکش کارولین بیزینجی به عمان برسد.
بادها دسترسی به نفتکش به گل نشسته در نزدیکی عمان را محدود کرده و عملیات نجات را به تأخیر می‌اندازند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20874" target="_blank">📅 12:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بلومبرگ
:
سامانه دفاع موشکی «گنبد طلایی» آمریکا نخستین آزمایش‌های اولیه خود را با موفقیت پشت سر گذاشته است.
به گزارش بلومبرگ به نقل از یک مقام ارشد نظامی آمریکا، این مرحله از آزمایش‌ها شامل انتقال داده از حسگرها به رهگیر و همچنین ارزیابی سامانه پیشران فضاپیمای رهگیر بوده است. به گفته این مقام، آزمایش عملیاتی گسترده این سامانه برای اواخر سال ۲۰۲۸ برنامه‌ریزی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20873" target="_blank">📅 11:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تحریم‌های آمریکا، صادرات نفت ایران را محدود کرده و باعث شده بخشی از
مشتقات نفتی، از جمله قیر،
به‌جای صادرات در پروژه‌های آسفالت‌سازی مصرف شود؛ تا جایی که علاوه بر خیابان‌ها، بسیاری از کوچه‌ها و جاده‌های خاکی نیز آسفالت شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20872" target="_blank">📅 11:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مذاکرات ایران و آمریکا درباره تنگه هرمز به نقطه اول برگشت
خبرنگار الجزیره در تهران:
مذاکرات ظاهراً به نقطه آغاز بازگشته و توپ در زمین واشنگتن است؛ تهران ممکن است به این نتیجه رسیده باشد که نحوه عبور از تنگه هرمز نمی‌تواند صرفاً بر اساس خواسته‌های آمریکا تعیین شود.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20871" target="_blank">📅 10:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97fd9de97.mp4?token=m8jGh73Ua7i_-S_Gc3Vmbw5lKZ0nWv2uuBLSMj8X5TJdblS33iWEBcpcMjmW0bJfk_k_hk-3d8qbLs0pUS_sayerrn31ztulQz4T6HO2NdirDSTEEOeLG4R7mxEHItsAs6LP9Q7uzna6ICUlMUKBhAhtFFlDMbjWbSCGJYXNj_zyMIwBJnbPYZD_digjjlG50Yg6VseuVdHOEH--Ww8lmFX1RF_OaMwwLgjuVU92AheorUe0246iEdd_Oa0aB5kaa1sy0wO0JAJf1uu6GJ-WgupqrlITn84LLOjxOiKu3VajUu9qDwYuJsl4MQ3oL-VGUHSauOIzYzFBPt8VIlGH2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97fd9de97.mp4?token=m8jGh73Ua7i_-S_Gc3Vmbw5lKZ0nWv2uuBLSMj8X5TJdblS33iWEBcpcMjmW0bJfk_k_hk-3d8qbLs0pUS_sayerrn31ztulQz4T6HO2NdirDSTEEOeLG4R7mxEHItsAs6LP9Q7uzna6ICUlMUKBhAhtFFlDMbjWbSCGJYXNj_zyMIwBJnbPYZD_digjjlG50Yg6VseuVdHOEH--Ww8lmFX1RF_OaMwwLgjuVU92AheorUe0246iEdd_Oa0aB5kaa1sy0wO0JAJf1uu6GJ-WgupqrlITn84LLOjxOiKu3VajUu9qDwYuJsl4MQ3oL-VGUHSauOIzYzFBPt8VIlGH2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ : «من از طریق سرویس مخفی و ارتش اقدام می‌کنم. آنها می‌خواستند من با پرواز دیگری، با هواپیمای دیگری بروم... من هر کاری که آنها بگویند انجام می‌دهم... حدس می‌زنم تهدیدی وجود داشته است. من واقعاً زیاد در مورد آن سوال نکردم. تهدیدهای زیادی دریافت می‌کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20870" target="_blank">📅 09:21 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
