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
<img src="https://cdn4.telesco.pe/file/jQV0XEJScMwG65mE4pqDSE_QZ2ZA4QeUAiANM4FICxPZGOXDdJFQzbDGRkuovz5Kbzr_W2DuPxrYHwSYgQ6FRAhm_vEtwrIXVv87FUBlEKAt8GS1j53El0SB6KFqRBkjqZgxQf8skju9-0ofZ2ccOSTWHnPHiEvrWjR45j8Zb4mtG5IY7j5fNiGdNfXBAZIyUyJL1Miua5__WRIIeM10O10DLYzbuIRNX7MoVxi5Cs5gwR6JTqtmr53AnakK4VS8q_VbAE7iXTXcNcBfLy5ferlPoWwfLV04M8EZLzQR4yW-bVcDFoZN7IWDTKr0dotFMSLec9JG6rFhuEKtjt5DVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 179K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 11:10:51</div>
<hr>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/funhiphop/78706" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده
از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/funhiphop/78705" target="_blank">📅 10:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB-O3R4PMHMqBdZAQvaLssK_tWEYp0JoTgX850_dUYYKDWdUyHPa8qKEWpaBW66BOa3h1pWYH324fszfsvBYlnt3EYSgmt0cH67AHpCnyhYn4edg00R9a85lkpi5ENlcdw48ArJN50II-x84rWfon-v4MzE8T8EC7QMa1tH7Y6_7917znK1ojS6JBhTMzuwSsIfbRm9Rwt1bRKmhRhARGYpQ4GyGBS4ediLBkGXniJr5rVyxwwDAuVKMUHI360QTA3y6759NqhRI0g9kJLrE4ebr8um3w9oLfAKxOXYQcddqptgGoWth4l5bOEvcRodc09xTLev0Xge89PfwkU53aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب 20 دقیقه بازی کرد و حتی یک بار هم مصدوم نشد
اینه شاهزاده فوتبال
🔥
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/funhiphop/78704" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBZfgYbufgyDXGVBqtyLjPD5ksR7mVdF0eL7uZ9-FNmoe-vR3FkAbmYVomu9xjs4Wjhzfr-xeqdceTI0dm3mw9nB3f62BPzAMNRnEiNbHc32Cg5S4aPgAflwcO0teGGt4_FymXQ3tdV8VK1FQtraDHazW4hsNPmEVDyHG-LWfSusy2RZ1Hp0srxuKl2IO8BUOrm8LqJ4r0jaTKU_Yx_a-qNGa-53KJAyyu_9Hol0QzQfDsxdDdD7x9npdJrAPNJ1B31CVUP1om8iQM44dsQSua_QffEL3PGCzK3bcpH5M4eM5x_xMtBAdhlbX57DN_yubNSF8NaLHe51VK9GK73DfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
برای اولین بار در ایران
🇮🇷
تا
0️⃣
0️⃣
1️⃣
🔣
سود اضافه روی شرط‌های ترکیبی
🤩
ده تا بازی میکس کن، سودت رو
2️⃣
برابر کن
⏩
فقط کافیه بازی‌های موردنظرت رو توی یک میکس قرار بدی. هرچی تعداد انتخاب‌هات بیشتر باشه، درصد بیشتری به سود بردت
اضافه میشه
🛍
🆗
تا
0️⃣
3️⃣
🔣
سود بیشتر با 3
انتخاب
🆗
تا
0️⃣
5️⃣
🔣
سود بیشتر با 9 انتخاب
🆗
تا
0️⃣
0️⃣
1️⃣
🔣
سود بیشتر با 10 انتخاب
همون برد، پول بیشتر!
میکس حرفه‌ای بچین و از ACCA Boost
نهایت استفاده رو ببر
💵
💵
📺
تلویزیون لایو برای پوشش بازی ها
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
🎰
همین الان وارد شو و اولین شرط ترکیبی‌ت رو بساز
R4
🅰
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/funhiphop/78702" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=Oog6rtFlN7vI2ZQcEl2e84gcD4C2TwGgssZP5RqFMC06v7OzdpTjuQoRX9J0uXr6RWqkwANXJp30f9AteMzeWUIY1F2n-xyW7UVcUjTSjf6C6XgfGrHmg1-b8U0-uCPmxXfUzCoHEVdpdFHPfv51BbJNqv9qQyZ6sXJZKE5H3OI0h2i6L4hiFUC925L7JrE1ri9eOVspTrPG7hXU5D4PVop2uQW9FiuUnXa4HzBMwfTw0Hn8Bl2Sq5OW0K0YmR30TfxdSeYtN6LoRw66KGMvpp5_eoeFIViFIoeO_SoQKhNSixlBrkKzeDZpHBIUdjJSbSJRLjJ6Wm0wZt4sWoj4mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=Oog6rtFlN7vI2ZQcEl2e84gcD4C2TwGgssZP5RqFMC06v7OzdpTjuQoRX9J0uXr6RWqkwANXJp30f9AteMzeWUIY1F2n-xyW7UVcUjTSjf6C6XgfGrHmg1-b8U0-uCPmxXfUzCoHEVdpdFHPfv51BbJNqv9qQyZ6sXJZKE5H3OI0h2i6L4hiFUC925L7JrE1ri9eOVspTrPG7hXU5D4PVop2uQW9FiuUnXa4HzBMwfTw0Hn8Bl2Sq5OW0K0YmR30TfxdSeYtN6LoRw66KGMvpp5_eoeFIViFIoeO_SoQKhNSixlBrkKzeDZpHBIUdjJSbSJRLjJ6Wm0wZt4sWoj4mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج اقا بنظر شما آقای روحانی کلید تدبیرش کار انجام میده؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/funhiphop/78701" target="_blank">📅 10:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هیچوقت فکر نمی‌کردم با صدای علی اکبر که داره آماده میشه بره نبرد از خواب بیدار شم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/funhiphop/78698" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خب دوستان یک ساعت استراحت کنید تا بریم سراغ بازی جذاب چک و مکزیک
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/funhiphop/78694" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وینیسیوس تو بهترین شبش هم باید ثابت کنه کصخله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/funhiphop/78692" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuTY8bQ3CyuwQeX8pFhiZ9OwKlPM4GcmnW9Aydbk3htl07AE5VZdK4ecCSDJFks2hvOr0R8KnknaV5ymuqRB31FMoh3br-l2keECbwVRHko8w3VlJb77X4dJxbQsf2cy4afIdDoUsQtUiyKd4iIvQwbd69ly4L16_pHVyofn-3Un-jSvXWJRqlPKkbEYp7ROrICcCFnImBn-x6mO8U94a9U86xuk5anUhKIcYxPJVRYK_Au0QJJZ2XtK51YyjEX5KbBKdRWHVSpYbqF6pulbqfPw4TXbYZ8sBbegp6ReePLXFvfdC89_lcD5XP8Hx-Gy6S6JHtmTQPsz9qMn4nNMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بایرن عجب جواهری قاپید</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78690" target="_blank">📅 03:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78688" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">با این جدول تیمای سوم که همشون دارن سه امتیازی میشن، ایران از مصر امتیاز نگیره نمیره بالا</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78684" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">من یچیو نفهمیدم، تیم ملی فوتبال تیم جمهوری اسلامیه تیم ملی والیبال تیم پهلوی؟
خب خار هردو رو بگایید چرا تبعیض</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78682" target="_blank">📅 02:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کصخلا آدم فضاییا یه فرد باهوش میبرن به دردشون بخوره، میمونو میخوان چیکار</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78681" target="_blank">📅 02:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">من دقت کردم از وقتی که دیگه کشتی کج ندیدم کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78677" target="_blank">📅 01:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ی پیشگوی شیشه ای خارجی گفته امشب مسی و رونالدو(آدم فضاییا)، وینی و نیمارو میدزدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78674" target="_blank">📅 01:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شاید باورتون نشه ولی تیم ملی ایتالیا دوازده ساله که تو جام جهانی هیچ باختی نداشته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78673" target="_blank">📅 01:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قضیه لست دنس رو جمع کنید، مسی گفته اگه بدنم یاری بده ۲۰۳۰ هم هستم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78672" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfWGy5g0WqXTnt_4TnVHVpeZVIP_GrhFY3uXnJhDq12Rx-ZHpfZeF77823_Y0WlRJqU1IEmaHYZFPBqYb_wjAdKHRkd7DolXsLP4RLuZBIkRmi9jHNi717DPXiHJt_JSP_gBY5FCLi22hy7__a3P80FjYlraECW8W1ePgOX_K86DtgDl_cihwSLOTPgzBWH1Gst_MG8ajCshGOQyFWp37W4B8Oh59V7RJ3EC12JrymbPak3JCPcsOf2rAOrvvcDhdA71d_n86K7TikXZzKNeZsocLryIjBiAGuioswL75iSG2PL79tcEU6PA-7WuaFRPmDNlfu7--TB3ngdH2g9Dbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سخنی هم از مادر عروس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78671" target="_blank">📅 23:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تلگراف: ترامپ با توافقی که الان با ایران کرده؛ فقط میخواست جنگ رو تموم کنه و تنگه هرمز رو باز کنه تا قیمت نفت پایین بیاد و از فشارهای دموکرات ها کم کنه. ترامپ بعد از انتخابات ۱۲ آبان ماه کنگره و سنا این توافق الان رو کنار میذاره و دنبال توافق جدیدی میره که هرچی ایران داره رو ازش بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78670" target="_blank">📅 22:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g - کاربر و زمان نامحدود - 480000 تومان
🟡
سرور 100g - کاربر و زمان نامحدود - 540000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78669" target="_blank">📅 21:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWNy1W2PmqeKauy4b-_Rlj7_bd12NYXP7FUq0PTIfhsoQrC0KtU0598JtaCH5u11uohUqms42ynXWyTrLNxdo7IX67xhXD9TrhJEvob_tyIfT6-A6ciLyMCvhGVN2xPxqRj18J26SIKlawOKL3-Ev7ut7sz897bGgmi-2oe-Q8FexgGNXeKXDYp_lxEp2QHMQWgju05h0iO9NUuJA-bUZ6TDfhpBxnyap3KIB55en1eBX3c0NIRamCND7uJNAMKb1DP7r-ZbPY0O_4_8GPoorFHEC12kQbGlk-WDckBbWLzbnL7LM1OLLRkGG16HMzvGlbjXIAPwqWDnJF4Cvo478Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام آقا ببخشید این رپر کیریاتون چند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78668" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLsEow-KlVB9cV8zXT89LkmXaG6-q59q6d5XjQeWnISWJKzocSLvuHzoT29bGJKYIg_dGmBT8ypkJf3TOE70Te2VlrFzdsL9BQxrjcrMHQkl7McUSuS14wkceVTZQtmiAbP4bHwcsFkr20IS7y0KqGD9RD7aJkjrGjJrBsZv8aKBevf1QT3VAlun309HYQG2DPWU_cD0hfVDPV9p2xMREsBNqwRl1N2G0px7lF2LJgNm2iqNq-WDqRbuDCDCJ3bLqyDLLbt18JMAg3PpAewx3w7k_hlkfehu0og_7dnkGJDjO0aVV_h0Yiw-wmJQTvEPfCp0wNuB-jyfMwGGVaTOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا زده ها شما چرا اینجوری صحبت میکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78667" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بنیامین نتانیاهو: چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78666" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بنیامین نتانیاهو:
چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78665" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=kiX4PeX6okYYvdKfk-ggwnYVUiiXOmPhbB1L_-10sq4V49ed5KHQkB95ybMAKUXzruafBc04HNf8HW9Q1d___wDRx2vTUQsVM6VYNTkBZPAeAcEZI5g2QGh4pxnbsQaLI3Pqtuk7m4UAUrJAY_dXznv5F_cTNy0D6tlh--w62j4S75vCoeYD_3G4P4ouPfEg-WQ1RTwFLKlkp_5e8hhxseTJEJpQ2HyP3JNHWI5BIMhHdR1fh0wT60ZXSSNh36B5r-S8HOvxvpWO2zux3_ZZJUwnVwOvVxeyOQseWZniDhW0Hg-NkjYFSnpXb1PCze7rWInI4OwM3saicRvF3tGtUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=kiX4PeX6okYYvdKfk-ggwnYVUiiXOmPhbB1L_-10sq4V49ed5KHQkB95ybMAKUXzruafBc04HNf8HW9Q1d___wDRx2vTUQsVM6VYNTkBZPAeAcEZI5g2QGh4pxnbsQaLI3Pqtuk7m4UAUrJAY_dXznv5F_cTNy0D6tlh--w62j4S75vCoeYD_3G4P4ouPfEg-WQ1RTwFLKlkp_5e8hhxseTJEJpQ2HyP3JNHWI5BIMhHdR1fh0wT60ZXSSNh36B5r-S8HOvxvpWO2zux3_ZZJUwnVwOvVxeyOQseWZniDhW0Hg-NkjYFSnpXb1PCze7rWInI4OwM3saicRvF3tGtUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماشالا مهدی، ماشالا به این تاکتیک پسر
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78663" target="_blank">📅 18:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خدایا کاش سریعتر GTA 6 بیاد که GTA 5 ارزون شه بتونم GTA 4 بخرم بازی کنم</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78660" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">راکستار:
نسخه فیزیکی GTA 6 فقط شامل کد دیجیتال هست؛ دیسکی در کار نیست (البته فعلا به خاطر جلوگیری از لیک شدن بازی)
- پلی‌استیشن: GTA 6 بهترین تجربه خودش رو روی PS5 ارائه میده؛ همکاری سونی و راکستار گیمز تأیید شد
-گیم GTA 6 روی PS5 تقریبا بدون هیچ لودینگی اجرا میشه!
-ظاهرا داستان GTA 6 مثل Red Dead Redemption 2 به صورت فصل‌بندی‌شده و اپیزودی روایت میشه
-بازی GTA 6 در استور پلی‌استیشن به‌عنوان یک تجربه کاملا سینگل پلیر ثبت شده
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78659" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=HF7KxQZ4LVAg6EnE9z2D-iFq1ZHEpR6iqfpS_1b5ppBLWE8jS7MQBwAjHsG1WLtdBoD5FgVbzS-iCxvej1xeVHCsoVzE8qe1Uy-59zBCMLn3bs9O6CTUMRyl6oSum9YCwLNopcSxuYKhi1lXlcJHnmsJ1NX-1OjvLS0EqcZerWkAEKVivr1MrG6YyK9CEsMbkvE37NcPbEWIFUCl4qMnSXMYmLCXs1zDJkxyKWJAOrOlcJCcxP6XExIMzkaKT9l5aUn54_27qwpPD-wIwdAWzIEcX74qwW7uuxWNmF3_y97HU0IHYS2uFv9VuAnOh8ZWQ9Y1UVAFRIPzYy_GAHNDfx0nLI4Nnq-ry4yhLw21pAdOam9ZspcGHJV7waaK9pBlesTAb8yqnEBWc2wAEToYY8iXobTRYbwgyDv4r1p0Pk3tV2_blOqkHAtYMIzr3S9hsF07NNOFv2rJGVZcX0aFu2Y_VbZg5H3LOeU4zbUQLcmAD3XEs86B5EvN1yDZr4PcTJt9Yo4oLnzQXTqQkYntpdYz3SOR4lQkClNDYvhyDwHj14zrxNozGl2CS9NAHj-ywDo-xicAB9kg_YzDyNTbuqmmySVMxtsOwXbLXRaQDyj1-aF9AcM9vGCrQ3M9AEMvt2dKv-zDVtvxDle3M_8g_5Pj4HTDPJL6LSXSjsiDJf8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=HF7KxQZ4LVAg6EnE9z2D-iFq1ZHEpR6iqfpS_1b5ppBLWE8jS7MQBwAjHsG1WLtdBoD5FgVbzS-iCxvej1xeVHCsoVzE8qe1Uy-59zBCMLn3bs9O6CTUMRyl6oSum9YCwLNopcSxuYKhi1lXlcJHnmsJ1NX-1OjvLS0EqcZerWkAEKVivr1MrG6YyK9CEsMbkvE37NcPbEWIFUCl4qMnSXMYmLCXs1zDJkxyKWJAOrOlcJCcxP6XExIMzkaKT9l5aUn54_27qwpPD-wIwdAWzIEcX74qwW7uuxWNmF3_y97HU0IHYS2uFv9VuAnOh8ZWQ9Y1UVAFRIPzYy_GAHNDfx0nLI4Nnq-ry4yhLw21pAdOam9ZspcGHJV7waaK9pBlesTAb8yqnEBWc2wAEToYY8iXobTRYbwgyDv4r1p0Pk3tV2_blOqkHAtYMIzr3S9hsF07NNOFv2rJGVZcX0aFu2Y_VbZg5H3LOeU4zbUQLcmAD3XEs86B5EvN1yDZr4PcTJt9Yo4oLnzQXTqQkYntpdYz3SOR4lQkClNDYvhyDwHj14zrxNozGl2CS9NAHj-ywDo-xicAB9kg_YzDyNTbuqmmySVMxtsOwXbLXRaQDyj1-aF9AcM9vGCrQ3M9AEMvt2dKv-zDVtvxDle3M_8g_5Pj4HTDPJL6LSXSjsiDJf8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78656" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
پسر چی داره میشه تو این دنیا
ترامپ دو ساعت پیش: همه از نتانیاهو متنفرن
قوه قضائیه یه ساعت پیش: ازین به بعد هر کس علیه آمریکا شعار بده یا حرف بزنه، 1 سال حبس یا جریمه نقدی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78655" target="_blank">📅 18:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7gqU3ULP2sy-0jSq621mDqLF1zZ_QTWFjXwmruynD1j9HXl6e49RuLfRZuKnmOhCKiAW7BGQCtVZoBPHRS_OhKQPo_WwbOLeXOL_qdYpjFl5YefwoFLzuIZd2BlOGsoJMkzznIyrc7Y5YlVDKv6pFl4DjrZ_9GznBH1aSewWCuVkU0nWmTmPb1ZTCNZBkZtLK4Gwjy5jhPRC-v2TPbZ_kzf2AP5Ek5qQNTTs8jmCoIt9dim2kWLYyhQbTMoa0jrYiL7Owy2d7Eg6QtMMrzi9ZhDTdiKITX_GrseDHoDUnoyhLBmZXz7NeStbs7FUjkytYKW20oRCUPkSOwk4i_CcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا بخدا داری اشتباه میزنی، سیستم بدنی باید حین پیر شدن افت کنه نه پیشرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78654" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccjqiSeI4PphVloDoJe9gFWPSLS8fCtwXOhd1WKQJ_-aKhcaTBYAA5Z1CZ3YB_dZ39mLGvCxapFQZ_F3HXz29O7cLuSpNP0wdzAnC8-BkVSQQE0cxIDYCwnxTgoZmQ9LxUPpOUaigda60hNBxSbwzJELXYCkz-BzjnXLKT_OYKUXQjZTLAsc4eQ5kOI5XtutAMSeUMzxf0LklMTt-H_OqTq1qw2NqowizjflEZMmF0iRg8HwQr_NRuLY3uds8dC6lXLGW6tSAXgowuyRhz4Urx5XI2kahhDlhV5mCXDEW0JqeoZR9xp_UyZu6riZnMk9JVxiFa5FcZsVyKjz2BdP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🤩
میلیارد ریال جایزه‌ی تورنومنت  جدید Winro
🥇
تورنومنت‌های هفتگی و ماهانه
وینرو
رو از دست نده
🔥
جوایز شگفت‌انگیز و فوق‌العاده
🎟
⭐
بدون محدودیت تعداد شرکت‌کننده
💳
با مبلغ ورودی دلخواه
🔝
بالاترین بونوس‌ها در سایت وینرو
🎯
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
ضرایب ویژه و رقابتی
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش مسابقات
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
G3
🅰
همین الان وارد شو و در تورنومنت‌های فوق‌العاده‌ی وینرو شرکت کن
🎯
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78653" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">از این ۲۰.۳۰ روز نهایت استفاده رو از کل کل سر مسی و رونالدو ببرید، فردا روزی که اینا نیستن بشینید راجب یامال و وینی بحث کنید همتونو فحش کش میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78652" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نفت wti شده 70دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78651" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f81be11.mp4?token=ajlOGFPN-Vn3904g7T2l-tY8hS2_KM2yXlV1UBSKYdqf5AKAyUcKuOLojzNsHkVzQZzCiUFf97KKk5JNzkHc6G2nuaK99xMXqtLuY5zE3YWMDIPta1umLMj3idfQnEtq76lprHmR8MHDLmY8Mtn0JnFj5i3nuCRLvjKRntPPNnubCZI5l-hRpkduaXrVgDNcInJYUim0un-TWByjDWCi2VXPyqVsIWbCxMdNxozFdGElMAM1BZxky7dDp1mU4lIO63xUeWMdo_xQc-XahJ8HSNxrBni2JqfezRfFX9qbD5Gze1zOIEjFGVbiy0WRYn2m9oLP-hVI3nmrVCwF6j-AQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f81be11.mp4?token=ajlOGFPN-Vn3904g7T2l-tY8hS2_KM2yXlV1UBSKYdqf5AKAyUcKuOLojzNsHkVzQZzCiUFf97KKk5JNzkHc6G2nuaK99xMXqtLuY5zE3YWMDIPta1umLMj3idfQnEtq76lprHmR8MHDLmY8Mtn0JnFj5i3nuCRLvjKRntPPNnubCZI5l-hRpkduaXrVgDNcInJYUim0un-TWByjDWCi2VXPyqVsIWbCxMdNxozFdGElMAM1BZxky7dDp1mU4lIO63xUeWMdo_xQc-XahJ8HSNxrBni2JqfezRfFX9qbD5Gze1zOIEjFGVbiy0WRYn2m9oLP-hVI3nmrVCwF6j-AQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">که ترامپ گفته آمریکا میخواد به ایران ذرت بفروشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78650" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سامان خب آخه...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78649" target="_blank">📅 16:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmRnwRLTy4qSVVRIXfcag51vOktAhsCBGqytgpRyYhdpuM5IcciZHd--IefMRJq6krTsz6OjMGB9l112qKmNmgZOdrai9qvjQASHcere2Axr46_L4SxtsZwuX7wKFyEYA3bWbQJAf5GZJSEjgpLQJS5N9JNNPoaEJriAqWpMeHAbqvoz59U2EGgZ7F6qu_An4UXY3viK1bdDaKHm0_NcLw6R0jF9lgUYG7gI66EqpuAUHM_a5X8eOg7Sxbb9dV5klA7r-_AwGwJk2sb1Lp5yZ3YEyAD7hyrozD5G_lFYSi9FcvWCteBRE3r56diD_J4N6-d75UMlQbiFr3vVf68TJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام مهنام نواب صفوی، از معترضین دی ماه صادر شد
فرصت ۲۰ روزه برای اعتراض به حکم داده شده و اگه اعتراض مورد تایید قاضی قرار نگیره، حکم اجرا میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78648" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78647" target="_blank">📅 14:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsqhyV2MWCP7Rmj5ZeK7FuZ6AedsFvSboSbNIUjED4y6V7tOcRrMPDTMkCh7m4M1RZWa6TPBFECNCydLP_yxDJD0t0iB-KWPSg9RADpP_D90izjPPpYitcV_lCbW5ajY2_dRt6CEkkQ1FoD1i-01Z_euiR97W_djkKkHeIzI8nbVN-w3bdrdo8fj8dYd7Zz8Q4fNDsgznIZ5PnofNyXEgF8E1KM-nnU7frkvZq6ZdKj9N4C4RnUQ1Zaqhw-_yiLrrqL8XmKjV5skEskMD9ADla404matQsPvaLwBsL5YBCqhJGIwzTGnZXzf6bHXh9w3O-QxARy7qlca5zA-AtC1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78646" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyRzsINNhA3GSDM5O5W7eeLJDFCmKsJiVWtM4EU-GeYwEeo2_dKJ-uzEHE4UDop886KXlfRZML5G_O82dXdQKBqxvxHNuiTTP_B3ZPEi-YrgZ_VLRGnsQSbSHH3mbIC9Bao0UzgIXsyPZ-O0pmK6WddLqGP9Zm5R0YE4nfsWMKoHeTYtCSrhh4zxtMw0KOiCRJWFdTPkfzDcFLpbCgGUwWEgBdTSvmLGyqSGSkD5-s2dv1MfiTlh50DrofaV4L5qblDa_ybcvhXJ0zWCOukAPFTLUnzvBVFJnJrgOd-x5FjvdyT01u8zIJE8eN65odLi01S4dBV-Pu2rbwY-4qgumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بازی GTA VI مشخص شد:
نسخه Standard به قیمت 80 دلار یعنی تقریبا 12 میلیون و 800 هزارتومان
نسخه Ultimate Edition به قیمت 100 دلار یعنی تقریبا 16 میلیون تومان
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78645" target="_blank">📅 14:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قبض تلفن تماسا تتلو رو کی میده یعنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78644" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78643" target="_blank">📅 13:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcHT-T8q8NUtlOU-brVYGLh8u_F1DGWVXkZvb7aG-7sS0WdJPbVcSjdf7lbAHnDPErVlyzrOONF9lVVdE4PLYDTGwqoh1SBSFDFVUqfP2_IAhdcKH8--OOx9XX8JJYysUXRyUS8bqqPA3L9GxbV75uwa0tFGwVLwSdnEanLszyu_icwEKxdKAYBIf2e4ojp9kHGYd5YYgPKGIqp6o6Ry_LLiqQSYT4ySDcljmJUT6YbvkC5XVwDTMS4i1kMq3mhMw7RGDLwmExD-Ufn8ZEyfzQ5uEwNTD7TqbPJiZe5KEP-ctjFU_uoeFJWMF4plG9eJ6cURkJpFRWXC3G4vxPxX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو مغز پدر مادر شماره 2 پاناما چی گذشته که اسمشو این گذاشتن
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78642" target="_blank">📅 12:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOiyUwdVhinGc1d09NnBDzN1moyNeut2YdA_PzWiRfiVT8lqylCj4h0DdnzDmKUSySEeutsxYNBVNI2FhfwVJfskueZKnI6VGIRhKeCoLA9MCgM-cVVw3-1WbsyOyjL5mvtNF5S5Ws_iW3URyLfw_jo2vc_MNXbwitIUEWF0uDxNZB02ikgWxBRhXAbbgjn9JQhqAwoQX-KTHuJ0B7q_KCna_DcB9Sgq1lhxh_vqXFOcAwbIDd7LX7fUz9G8h2RfFjzbMsAadUq7Xb-E42Js0uuzJqExiDmpdStUfuXEYlAbbVl0feIpiv0Q3lguQ0UOTJdMOEMIn381Ec2osKTSYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر شمارشو برای ژنرال گیر بیارید
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78641" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78640" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt2u2wq08pPxd6pc0FMDqWvJB7hD8B7wa2fLkIbn4_38G3mgY-4NrqZXKDQoC0oOZXelo2vbVtd6KVNMaDmOsRnzTDUSvC8hfDPTS58TFFw37dEaHb9C3AKiIKJB1WX4A0vr5F-Sh4wvktmvOKeIqEyzDL84zNlP9dNpZSUCoJy10wg-mUQTL6v7Qt3H3hmaawTxpkwPW0psBssUVbCnEg1swrGITIU5_pLYiJHQJvY8bh8bRGC1yeQY46WHDKZFEaX_oKeQ5e_D5RRC2zuYKKc5YWFxmJTCtIJUJpVcE-Gi2FezuipopqRbXU8FB39UisLcO7M-rIxpCrwzQXxkiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R3
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78639" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">و تمام
انگلیس موفق شد غنای آماده کارلوس کیروش رو متوقف کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78638" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">توخل از سبک بازی کیروش کلش کیری شده</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/78636" target="_blank">📅 01:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بزرگ‌ترین اشتباه تاریخ فدراسیون فوتبال ایران قطع همکاری با کیروش بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/78634" target="_blank">📅 00:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joDFd76O0J7sHzTvgb9AWoxxfF6XzUDHVkQ9m6viA7BrHv8B9hlwLp135Umj6pPxY_EEnNLSaYHQpoVQHkYyAMlAIW35_2CcwZS_JU8rg-OVL41CcSpsrUSctkfFqiFpXwoRxOw-n-yk2LlAMKeKX7busyD-SFpsWlBOi8me36n42kOnVqI4Bbc08kVvGee7ReAavvWiFnDhPHIPOIyvXqYdjn8GMZnfWD7NkV7JLVw5lkh2lMQtC6MIeWbjy84a66Mvc4N8aHKhN1RmlGd3PCrDmk3bGuxmk2CuRaNH2Y3ouPfcmDOXbQxJlUG1LSXZuteYUL3xKZ8OhGU2of_bbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد ۳۹ سالگی بزرگ‌ترین، بهترین و با ابهت ترین بازیکن تاریخ فوتبال هست
مردی که با وجود خودش به فوتبال شخصیت و اعتبار داد
تولد لیونل آندرس مسی بر‌تمامی فوتبال دوستان عزیز مبارک باد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/78633" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کیروش عجب تیم سفتی ساخته دمش گرم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78632" target="_blank">📅 23:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=ifisAoAZw3Af9KUWbvr441vx32K-x9lw10N36-y0YKniyBSj1U6vFaG14KmzYBlk5UFD5UME4GvC4cHdm1pJehui29LTqtfVVhIKbLQ-lswnsZI263tFvyJVQMBInqJsQS9pLRdPHSeRRD6ToqGot2pBJfMjMkxRLyCai8MGzVRT4KoLuegWAve_VOKm33A4cdUkx6injIyHbokudEcBv4a75AdHu5W1YSl9AcbuUtAlRarxHYLg6R6SGXSMNw8kI0RP0qzXL8Rb9Xgb1bbsvYX7tUS2TKax7uqH6l0LD94QHbmcCXshRxbtZhhcXVC1kDCbAjkLuOu9o3b7fuUDnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=ifisAoAZw3Af9KUWbvr441vx32K-x9lw10N36-y0YKniyBSj1U6vFaG14KmzYBlk5UFD5UME4GvC4cHdm1pJehui29LTqtfVVhIKbLQ-lswnsZI263tFvyJVQMBInqJsQS9pLRdPHSeRRD6ToqGot2pBJfMjMkxRLyCai8MGzVRT4KoLuegWAve_VOKm33A4cdUkx6injIyHbokudEcBv4a75AdHu5W1YSl9AcbuUtAlRarxHYLg6R6SGXSMNw8kI0RP0qzXL8Rb9Xgb1bbsvYX7tUS2TKax7uqH6l0LD94QHbmcCXshRxbtZhhcXVC1kDCbAjkLuOu9o3b7fuUDnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهره هوشی:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78631" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">واقعا افتخاری که تیم ملی نروژ به اصالت و تاریخشون میکنن رو میبینم حسودیم میشه بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/78630" target="_blank">📅 22:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این سری کیروش کمتر از ۶ تا گل از انگلیس میخوره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78629" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شانس اصلی رو پرسپولیس آورد که کاناوارو به اورونوف بازی نداد وگرنه درجا تمام تیم های بزرگ دنیا مشتریش میشدن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78628" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بازی تموم شد مبارک رونالدو فنا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78627" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پرتغال امروز با پرتغال مقابل کنگو 180 درجه فرق داره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78626" target="_blank">📅 22:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خوسانوف از کنعانی و شجاع  هم کیری تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78625" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LamBs9oTTafQAvfuGWrJzhFbEZE32hDC2gV5lyojfoNnTEsnSoHgTQmrv_0HcejyLCHXne2owRe_exLKId_YYMRqVwu-EG3bGGmHd_9A2oam5w5uahcizW95wdhsqCBkTCFPFKJb6hzlrG1vbOtHpjT65vcPUZ3OGSyf7PVRvUXlTEgIRp5nnwMrigzmELEQpIHe3XrEwGILloNxODdZx6TLEFN65FR7VGCBbleOB1sL1OMd8l3-K6xImf7LtyVsKrTv1bBrqTkSyUvMQtrIEbunwE-z0Xpcsogzc920TQ1d4P-xpbVsw9FC-2xUsZZJNrmx2yhV3ReP1UTaHLv7zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مسعود دکترای افتخاری دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78615" target="_blank">📅 21:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0DAuG-_YYCem5Gmsbyw4HbKcmjWihkVM3hgJN-_H4_BEJ5oK4RW6-B3rMBT97yh87l4sIx2vA96ZgT6LXz7BNZPltOKqm7MEdLQxc2AtOO1iiK8IkkofbXOk1ptdVUh4NHGjmaV32drg9kEzxi1omsUIY2c_WiMMoLGI_ROWddWgM4LF8RQPO44Yz65P1SF1qZ0Uh0bn9wxnTGTUzMqhfPMw-Ltrj9KJ3rMq9-cbrZehKB7RjssOFAcJBVzvQVY-nE4DQCXipcgYJy6Z1H_ta4SxHD94--YnsJXtssDxLeSX1TC9gJeF4NiYtdf7OrLM_seuR39LoHUoCckvTm_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو بعد گلش سایز کیر ترامپ رو نشون داد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78596" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">امشب تعداد گل های کریس تو جام جهانی دو رقمی میشه؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78595" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXFe3aSPgn9biNF3fQuJaBtGKLZfrKpLxbnCudDTgdPlMWSWa5AQdUuOlqDCszfe7DiVjp9UvbWO3xma0-_y4-hDIC9a4fUL-GPKB7PYUO4jUhAaHuWSdBwXTSMCCUEmLi0sCnTdm3I3N7ziUcdXjhEYjhzkK0HWKpC1r3hex8yFqdMWJwjt_-F_EgU553DEjF8e1wm7wNquOmEl7yFQ4Zjv_khDjT07i8ah4y7oTKcWWaQfHug7LdTW3KfLCFkrtebFLjUmBQ1adPC_kCuwnt6TgJYHJB8L7IskT4SY0h8-0JPLS6PqZTmZUvyFXpLlonni_Qb899qPfRcn9q7jdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نوسو بغل کرد
😂</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78589" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78588" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره  بماند به یادگار  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78587" target="_blank">📅 19:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسپویل:
رونالدو امشب با پنالتی گل میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78586" target="_blank">📅 19:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78585" target="_blank">📅 19:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvA2tymhzHviriGlBmMqxYFEO3uYaeT_NujYE9VHrqh09Se_g0BwVdPBk6U2i0hLLcOWkYSOY8sEvmBanzox5mGfhKb9BFBWADszlyqhxo_HLyGFoHEXslqO2aN9WFcjoIMNM1EUmkJAgWuJtmnf5LdLjXyGcqmfNkowC8W0ODsETRj-dAhtMBLD5Kw6ywSdH6tGn2ZyqljAzhKTCUifIW_tZ8b8nI6xZ_Awh6AhHr1zANR7J4baxhX_lhF7nPWh9o25pqjXh_B43GO1WAR7t5KGM7w-jYI9Anl0iZKyKNNj8fThIuuvF9Ap3i1LIq3eMiXBLYfdxyqCg3Z57W_E2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSYbw34wK9t-jgs_k6emyENvtxwp1ga55RfeWNwYqUVX9UWL9M7PVl0F2dJUm_uSP4KHxPdUPXxd5okaDk8cjoYLkd_kZ6zSbK02-3tWGzSrdCNPkIxqg82YXwz-3A7hsmD6lgfWQ9XZJrR3snjmNDwrRkVo4VCHyaoMi8TKYowSWHhCfIXVBBJ02F2kFwXqI2L44zOK7cMgYRqTwlJmFn8BKMz9GOq_MYVgI9A0Lr36Z7HFkV2T2t-9vS7oDedQHIGsGy3eeOIQK91aiVRCSP_JppK0JD_DGZhs_T7sbYqYp_Ei7qg1deqswVKYSO_tb-zJbjKR2GMrwIgf5gJ3BA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب پرتغال و ازبکستان برای بازی امشب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78583" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=Y2dLhKSco5FNtqEZMGr_OI84B2f3CiZKCP-90BdhpBQ-_iSw6Q73UtFqq15OHo8bO8t6V_zg3Y7noOseUbSuk8LKF3gQdES-L9T9H-u6rgwP6_ELkdcTQ3rZZpDjWURYLP1tSAqGphqMMIcrqmBIzMSk_l3cs_tSeGXTz85_Inwkb1sZUZ7uC10WgsuP6fkxTh8PtZCTtK_3OwweZpmGVqSjPndRTeqHGkxsgSzvIo3SitMUTV4pbrMadpFPE5xduULfWvKkJBGAExEaZLEkkaUshnj8goANeBJ8R24Ax_DHoysGxFDepNEzbTl-Z-32X9-8emiJS6rVnJvKRC-jVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=Y2dLhKSco5FNtqEZMGr_OI84B2f3CiZKCP-90BdhpBQ-_iSw6Q73UtFqq15OHo8bO8t6V_zg3Y7noOseUbSuk8LKF3gQdES-L9T9H-u6rgwP6_ELkdcTQ3rZZpDjWURYLP1tSAqGphqMMIcrqmBIzMSk_l3cs_tSeGXTz85_Inwkb1sZUZ7uC10WgsuP6fkxTh8PtZCTtK_3OwweZpmGVqSjPndRTeqHGkxsgSzvIo3SitMUTV4pbrMadpFPE5xduULfWvKkJBGAExEaZLEkkaUshnj8goANeBJ8R24Ax_DHoysGxFDepNEzbTl-Z-32X9-8emiJS6rVnJvKRC-jVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سریالی که دکی قبل نوشتن ترک نگاه کرده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78582" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbNaQOPdvDX6wF-DqlEPTWDRS5VbE2AwFypgS7Td-JQHJgn7_UHIVDhV6_sIxTCV7EFO7dclz7Xqjr5nqnOjOk8iEqmJrUCtxDav3hxfH_eqWubp7SVIRwQ-OC6aELDbvzAlrIAm1e2QBPhyi82lcRrMCWkhvUZkV2kLlvIO8RGU4CHZ5zaDIuaO8WYF9Vp4x9cqGkHL0jGP0hO0qVJ1gQUgly4OSo9MYDVGEQ3yaHQdcbuhxlqOJ--pWfe06RaoN7sTdGaoUhkOW1MoN3wDo0WSgoBg6W1TKUSBuIjRwPAk6mwt9w2MkTTRqSH9EOT75MEULedzYWbyjmWoUQYnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیت دانیال اصلی و مهراد جم بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78578" target="_blank">📅 18:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXf8kDbH6PqiIpq7VcnAU6ewxzjb0NNan8SuQgWH200FvsTagEYmW15C6f_5qwngFz5MzMrCm6s04or3zzx8oPmoDDnDuQSpaHI2BMO55RJkkMpTMQxJeaox76HKu2YxFV1Um3sEYz3JIy9atuuPrVpJLPWeOgxKjDL6mrnXhnQhvb-jBuuzz2I2xI-JC8YzTVftS1ZmH6lc3Edlm75UNa3OD8wnmlsMcZ-r_2C6QSElUeLBQnIIVraDF7eNADEJY59HS8Ee4Qb4sGHPMCMWud4R-NKUjtq5mmrtJ3Dy8oVn6rhufuWQeoH4J0z9twdOgRmygoBNeUa9phd4hmhxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که سپاه قراره با غلات بکنه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78577" target="_blank">📅 17:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78576">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حرومزاده این همه ناله کردی که آه ۴ ماهه زنمو ندیدم تروخدا زنمو بهم بدید دارم می‌میرم که در نهایت ببینیش این کصشعرا رو راجع بهش بگی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78576" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فک کنم پدر زن دکی پوریه، وگرنه هیچ توجیه دیگه ای نداره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78575" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78574">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78574" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78573">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ PlaylistShip ]</strong></div>
<div class="tg-text">فقط اون بدبختایی که فک کردن لاوه فور زدن برا زیداشون</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78573" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78572">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خجالت نکش داداش از سکستون فیلم بگیر بعنوان موزیک ویدیو اپلود کن یوتوب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78572" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دکی: صدبار تو اون خونه کردمت، جای بد نرو جون جدت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78571" target="_blank">📅 17:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دکی: مثل بابات عاقلی مثل مامانت کص
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78570" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78569">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اونجا که میگه چسبوندمت به دیوار با صدف بود یا مامانش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78569" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza𓆃</strong></div>
<div class="tg-text">دکی وسط سکس نمیتونه چیزی بگه چون پای صدف دهنشه</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78568" target="_blank">📅 17:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فکر این که دکی وسط سکس به صدف میگه مادرتو گاییدم داره مغزمو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78567" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1BDIo9RJs1DVVf9BEd2QtvonVADOthELZIbSWW4bc3_1hN9YX6rkx47WP5qqubxNB4m5GKX5Ji98gJibLQ4P-R_jP-ptsr4CSElpj0zgxAcYV3VNDVQYjSUE7Bp6JBbT5bZjvAbVcxUWB9pg24dd-dQycRVgNI497P5IJsSZOQX78utHjbVw7nMoLNsVRFPjZ1LK-9-NwWERVjNCNwyE1TQ9YYocX4Xm9W8QIHX-6LvxxLg_IpjF7h1dCr46C5-VjEjy-ENKiJ92NAko9HRgCMWjvvjC62aFyYPlxrOfpkuJTlPzsnSuxjRFPSWDRUgBKOCG4l8ejN3oHgR45fwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBp3FGgnR4OLtSIJCl5pli2sdesX7m4tzKgygxXhaKRaGwMHiboMskqiB95DlOIqOHKb7HRe5BjOV-m8wgvw0VU5tdajniGwhoucxdGEC3EwTV_CnA9ImBwFBvQzze_fHcsa1ONNJmOJn-PFZwEkk-U0u70Uqq3oJmk7wVzfqxP-GYKbeEsys_44XY45HyxpeTjAcT7e0488jmvFVwyt72Uk8WBlGCcrOjaHBp3B6YAKSlbJtxEubrgXA9McbdxpYNf82YaeUifWmJQw41UC5ZH_PYDae6E9eXyjT3f-2a9FAnHkJ4doeFgX-HHvkH0Kb5uR6HYLT5R6eVFLufpuaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78565" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf96FO3e8yGVFnwZg08Oxqnh8dNJCoHm1qxvm8E1-kEpgo1P64GSXODCP6sfxLu1oVXomvIWLUkZNFYkZeMgscvGHxKnnp207jhm7WIzL_8s6NonAMapy7Ac3hpZ060M8dKe-9AU3MKBOWt4d5ktlfq4neOL2e57dUIBjofczBBrWhg0vXke5US5fHnSTHWX8-mLdmBXF_ZncPMc9ZKeVuW_nnFZWvBAS0iYhu2LD9txg4dphTmyDFTW7_Ph6dspPQjznnzS7gvNvCW3Xr3EwcOsNGCVMtfC6kSwLFXmfjdUm5W7Dn151IoIdTSb81axBvbIieGLEA_-kmNpKtnwcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.
Youtube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78564" target="_blank">📅 17:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78563">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کونی رو ترک عاشقانه این چه اسمیه گذاشتی</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78563" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دکی کونی موقع ماشین شستن من چه وقت ترک دادنه</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78562" target="_blank">📅 17:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78561">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تنها چیزی که اَ بابام میخوام عشقه فقط
من برا بابام قیمه میبرم من من عرضشو دارم
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78561" target="_blank">📅 16:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHFMk_X7ZqyW4UfGHyGT-VyooSs0AD-lDkhR74zYzllCFnyH2BrIFmPGLT-mM8ThZrs8Q8KRIeXGmhm5koCwULjjdrCXZuVG_NLfciHGqfyTBDwCopTRDnNRkBZRgy1TSEwIrMpxBa_p5C3GW1U2QYrhdP0pnE01LUT1VJHBwKM3coF7OluuF293FwivGadxZjJ8GZLoeSb1aUnGKEGnGtAzihlwBokwbMka7Yw-DGXCdbOeoSsp8OEp3eWafoxX3S_Z7XOBwpfhBaNQvP0BF5RZTlyKPl0eTAwnKAC-H3bVK0JbnW3uvLoChRN-AlBDJHDb_Mj-f1kLf8w2KNcsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو رسانه‌های آمریکا به جز فاکس‌نیوز کلا یدونه نیویورک پست برا ترامپ مونده بود که اونم کیرشو کرد دهن ترامپ و توافقش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78560" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFBVe3UAaqQLaN4MHGOvC51_9fwFJNJ0-GnMk1-bPXAnnFVpkiQiXmTYQSPBIv1zT7t0_6VNuLqFBKtxb8yFVVc13NLvHh9wCiRtcSKZhKTLKqMyy1-tG6ZZQpKzsyYHAh-BGzwujDJTnL4zNnCd6sTeUPMbCitsKnNTdP42QZDYV6YBNbtJCFTvtoyI9SPz7aG1goYSyH-88V5IKYWcepE92hxyfk3nPBZ2jZBsOoQCVBBRlb_m72Uu-7owogS7RBjBP83R6GSIYCUbfM0m8_T2B7pWnWxJHOsikm6wysdXfi6VfLa_YrBZzbzWUIu5yHywirc-vd_r2MVwIn8ROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا با دست مسعود روی شهبازو کاری ندارم
چتر چی میگه اونجا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78559" target="_blank">📅 15:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78558">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پزشکندر و عراقچی رسیدن اسلام آباد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78558" target="_blank">📅 15:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">علی گرامی بخدا خصومت شخصی باهات ندارم به عنوان یه شخص بی طرف دارم میگم، یه آدم رندومو تو خیابون نگه دارم بگم بیا رو این بیت رپ بخون از تو بهتر میخونه، روی این مسئله شرط میبندم، پس لطفا فاز نقش اصلی سریالو تو یکی نگیر بزار یه نفر این کارو کنه که بهش میاد
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78557" target="_blank">📅 15:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مسی و رونالدو جان جدتون زودتر خدافظی کنید فناتون مغز مارو گاییدن
هر سری یکیشون گل میزنه فناش مثل زامبیا تا یه ماه میوفتن تو گپو چنلا سوراخمون میکنن که ابر ستاره تاریخ فوتبال گل زد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78556" target="_blank">📅 15:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8XnBLIk3qTUR3E-BW4t5q18QWS8wC94nMsuuJ3LUuXx5MgEkFVZnCvQ7-mq135E95sSYd3ey9frG96b5Xwp0kewgiITXeYnL_5a2V4VzYiaplw7fHKSC-W0UYqy2v4OMpnT_F9gKOHGZUT6ybB4AMFK3i5H9OH9-OMH9V5ArSyFPshMQQuxKXYrQmkQocgud_E2vrqeHWBJ3Qdjy6lMjUxQ1YqcJKDm_F7muXmDPgJxAcvlDR7vToN98lGEF7uNHKtXf6xSMirTVJ19WEVt46aPDpXfoq372q0imQOOy41sDPO-zvUub0qLJnMSzWswP9ODfl4qdbXoY6gbNV0iIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78555" target="_blank">📅 14:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">من ک میدونم بانک هارو بگا دادن تا حواسارو از عروسی دختر شمخانی پرت کنن ولی نمیتونم ثابت کنم:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78554" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مثل اینکه اکثر بانک های کشور بگا رفتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78553" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آلوارز گفته از سبک بازی اتلتیکو خوشم نمیاد، اتلتیکو چی گفته باشه خوبه؟ گفته خب بیا برو آرسنال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78552" target="_blank">📅 12:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حمید سحری عزیزم تو ویدیو هاش به کصشر ترین تیمای جام هم اشاره کرده ولی به ایران نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78551" target="_blank">📅 12:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeVJros8zeyy_ZB-w7jlUj2Wo2CDkJfb-B8d4d181Nnsq8Ae-uqarzR1vQAbABuaWyypEg6BMcBKj_ZmRAGLBea2xKURQO5uOXVUuYSV90BykwarmkOjYaFxZdI4DNcL6A4R1sDD8XwYD6c1gzd0IKWAHYweLgJfMBZR-lGHtP5K-lSLycPVnj5lfJYWubZyP592ARjfao4dN55otCpBTW0jxGNkLNW7Yvb9_EqVlcktuWT5ivYB1cuEm8WTjzaUlGng2Pr5-pVVyNBgYtlB_cLOSaLig85WXB4L4s99fvM9pYok69xkgZUBI3UEF_ad_5agjPPcY3VMEP84GpF9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78550" target="_blank">📅 12:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TimaGrHr_mgn_bMUM-UMomSNDC6zTylzuA5RD2mU1XO6mXVJ5Z-gGh9HYVb5I6sFPcAsX22q6YbDdjkooOLXu6Tn5BDgxGZpX8D94-JZ0jczLZsKIs8VU3MjBIe4wWBvrTmexwBfvkAwh0dLJsnaFehacq_TYyjhfGnK0q33k8JPEwA3zEy9gU7r5uasE0DR6-PDSJwvFg0pLD9Ez0YkM7ZZciVIIWGR7YafVGojCIcoZk-jt4-uo2s8lQsMGBXOaKVgUpcu4zv0a_QZsXnBLe5Bny1SsyPJcdKeMySD3ie_37ZPhpEEJGAuIoDp8oV667w7HXv8bH0Qu7u7ar3jIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان از ارث محروم میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78549" target="_blank">📅 11:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VnxRhOoy6rpeE6GlTA0M1r_-MNbC7VlkF0f4WKGBiC0skp-fGovIpX_GpdHjBtzXDzBQU_h2RTRmDAOCh7gtY7q-LSaK5szWsOcrkqo_cpvQYRRqN0tILjUaVtgyYsAVhs3g_t9nk5y3kguHJDo57XpPNu0p5NRRGPHhtcpxJiTJA762rlIEn9bQX-LSKV76rx0-gTCUfZwnreh6XBWAXrb5alYsPxedwEr_n68IzhLqs7ySbJc0825-K6AG-_VSM2y8mEY9Ii9pLL6DU4Mal3WF2HRnClLmpJnJClM7Q2zWlI2vfsOxf5wzxwCeHWNxqGhH9cqVJxuF-d2Jw8srlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ هالند: راستش بازی با فرانسه زیاد برام مهم نیست چی میشه؛ احتمالاً اونا ما رو میبرن و حتی احتمالاً قهرمان تورنمنت میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78548" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTZRAVlRcUdqdoRFfiJIltQo0TKGo-safWMDhh2_Q_NaMS6dnwBWDT1HImYxt0tc2xL2QX3I2pJqJvPnY50VAzfz4-Y4zqdilr4wfKB823OLy4IYW76Kh3iyHLaCpbJoqNPEgjGPLvlVzmQUYRmSzrRLTjWqth03pk89VRm7s4NyABLwfkC2jA61OcfMEXMfyu4COSaO6QkthVJsR0B2W1lfga7F3o5phdH2-HD27A0C0sgA49NyBMmbEzBldHQS3Wxp5xe-gFKPgM-KzEpOqzfPdmHVzhb1saVZLfiYata0jvjDYKqfZDsC7ePhm0M4F4MrYD_4BMIbIV0fNZ6Hhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این الان تو حالت طبیعی به وانتونز و ویناک گفت فید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78545" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78544" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0Lvn-778DSvpLsjv7bNmEolB9fWkmFENcvRrYGajdo7OeL5pv-UtFB0k61tmOnMSsv_AKWquCMpfLJIxdUf-o_I1eoL1pcZLLtXKqLYsVNhanRwy-589bgPDw3Opj_gNPeWfI8SiTHVr6tV6HA53LIp-vK1eTB1kulP3UY3ocNZsx8SoobzZuMQIdti69sF5J6FPqjNp7ilKFtlB1SBel6BqLW8soh1LgwkGJFi6jdQALWg7JJIwt-OMFHp65iYVU4NpYkCI0iDOrqxRmTOtkwmQ2DnzrpiwEg1-QYNsFwcBl8SPwd3eYgemXGIJ8pCau4ZYqP_E-DezusoYTGxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون مسی رو ول کنید کصکشا مثلا بزرگتونه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78543" target="_blank">📅 10:54 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
