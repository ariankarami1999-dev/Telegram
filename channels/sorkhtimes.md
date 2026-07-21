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
<img src="https://cdn4.telesco.pe/file/bh0qRwdD_nDH1McgSSbJvSm1KnDqrQcMRCmZ2LYLddco1f7Z2UbAX1wquEQqM0njX8R9thd37dvk_iN3LDgVNPgvIvYpKJ_O0XWSTlO2urt0gfIrpZJCO45CqWjzOOFC2BLcTPbe8Syk2PrhfNVeNpodhGtHDCSXiuGIyRK16m5bXa86e4RKYS08XcJTTKHQLjNz-5dwOt7PgI5Ig4VU96x5ImJurqjbVxW1EohErGwu8SmcQ281usxjU5-Cu784R23c6oxlGCl32TELXxfgyy23QjNuH7Ujp4CeisXcKtNSPKRcmlYwB4Wsb8Z0QgGvI9lHQhG0O1XpjsP-UzdVcQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 15:36:11</div>
<hr>

<div class="tg-post" id="msg-136412">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
محمد خلیفه عصر امروز با حضور در باشگاه استقلال قرارداد پنج ساله با این تیم امضا خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/SorkhTimes/136412" target="_blank">📅 15:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136411">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
با پنجره بسته، دفاع چپ جوون هم گرفتن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/SorkhTimes/136411" target="_blank">📅 15:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136410">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
✅
جزئیات اولیه از پیشنهاد قطر برای برقراری آتش بس:
🔹
۱- پایان جنگ و برقراری آتش بس
🔹
۲- تنگه هرمز تحت کنترل ایران به مدت ۱۰ روز باز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/136410" target="_blank">📅 15:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136409">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
✅
مهم ترین خرید های پرسپولیس دانیال ایری، محمد مهدی محبی و کسری طاهری خواهند بود/ خبرنگار فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/136409" target="_blank">📅 15:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136408">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/136408" target="_blank">📅 15:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136407">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlkMkNkbpPPmjPROcw0ZgKSXkM5dq2GjpxSYR_3U4hC3a04A9bMjwFdguUjZ1umBIUGnsD86P6HB8jn0LFILV3JIhQZHBhQYUw7N-DnaSH4PnIB3qIhkVAp68iohAZ64sYPgq1NHh8X4TIkvF9BtMNheOOMKhFmW5V6z6RvRwPUcDzESN6sN8KtrifyH5gHpYSH9nXuNzNP5Ri9vYOnYi10un8da9C3iCNvWcH1JroA5vnqG3rVvsLnUzOefrIXg3ZdmKM5B55AgqR1EHBx63CwpC6rbjH27L7FHhggCpzg9jGFhe0sW9FjExaW2nBO-CCkocx9djeSWNOSqDolvFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
➡️
JOIN
JOIN
JOIN
JOIN
➡️
JOIN
JOIN
JOIN
JOIN</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/136407" target="_blank">📅 15:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136406">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
💣
One Signature. One Earthquake
…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/136406" target="_blank">📅 14:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136405">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
سایت و اپلیکیشن فوتبال 360 ( برنامه عادل فردوسی پور ) چند دقیقه ای هستش که از دسترس خارج شده و خیلیا احتمال فیلتر شدنشو بخاطر حرفاش علیه قلعه نویی میدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/136405" target="_blank">📅 14:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136404">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
🔴
شکاری با استقلال مذاکره کرده و با باز شدن پنجره احتمال جذبش بالاست و اگه الان باز نشه زمستون یاغی میشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/136404" target="_blank">📅 14:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136403">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
با پنجره بسته، دفاع چپ جوون هم گرفتن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/136403" target="_blank">📅 14:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136402">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
✅
طبق شنیده ها ما هم افتادیم دنبال اسمی عجیب به نام زکی پور ....
❌
گودرزی کجا و زکی پور کجا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/136402" target="_blank">📅 14:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136401">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">،
❗️
❗️
شنیده ها : دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها واریز کند.…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/136401" target="_blank">📅 14:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136400">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQjaRbaD5Wbxaqclzt51bh-diqOp7qi5NzniiOJ5zTq4h3lPhxxvEEhhmz2blFm3Kn5AIskgP-kDMM4I2u8gQucz7IG4U0Jd4PPYxKaMmO1JXt77GO6StwMLLXl7qnNVkqrkxnzHCioINU0xMgwqRuQCVXImxU45fi8g3xqbABBFczB0Iz_2BpY3iENsRoACBfkFl5GPj1dbji6RtMqMNyIIILszSjbBFe42enm6P4tVNOpRmAEHU4ccLuD6NlOOWQxraJHeXrvKaXdVlzeG_hdcXHuhPG5s_ysf85ms1T6x7cAa8iQ23Pcx7KW_IcsCHFZhMgLkTScW8okq508e0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
با پنجره بسته، دفاع چپ جوون هم گرفتن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/136400" target="_blank">📅 12:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136399">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
بهرام گودرزی با قراردادی 5 ساله به استقلال پیوست!
🔴
پ.ن قابل توجه آقای حدادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/136399" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136398">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
❌
#فوووووری
✅
باشگاه پرسپولیس با بهرام گودرزی به توافق نهایی رسید در صورت عدم تمدید میلاد از این بازیکن رونمایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/136398" target="_blank">📅 11:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136397">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
تیم ملی امید ایران در اردوی ترکیه مقابل تیم مانیسا این کشور دیدار کرد و 1 بر 0 برنده شد
🔴
تک گل ایران در این دیدار را فرزین معامله گری دفاع چپ پرسپولیس در دقیقه 17 به ثمر رساند، پاس گل را نیز پوریا شهرآبادی مهاجم سرخپوشان ارسال کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/136397" target="_blank">📅 11:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136396">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
👎
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس برنامه ای برای جذب بازیکن خارجی وجود نداره،و حتی در صورت جدایی گرا و بیفوما!
💯
تارتار از شرایط باکیچ،اورونوف و سرگیف رضایت کامل دارد،و اگر گرا تخفیف نده احتمالا ماندنی بشه…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/136396" target="_blank">📅 11:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136395">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136395" target="_blank">📅 10:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136394">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
شنیده ها:پرسپولیس امروز 40 میلیارد تومن + رضایت نامه قطعی کاظمیان رو به فولاد برای جذب ابوالفضل رزاق پور پیشنهاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/136394" target="_blank">📅 10:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136393">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
❗️
واکنش تند گداوند به صحبت‌های اسطوره علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136393" target="_blank">📅 10:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136392">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⌛️
⌛️
فووووووووووووری
🚨
لیگ برتر به صورت رسمی از 23 مرداد آغاز خواهد شد.
🚨
همچنین جمعه 2 مرداد مراسم قرعه کشی لیگ برتر برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/136392" target="_blank">📅 10:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136391">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
بمب سرخپوشان/ پرسپولیس با محبی به توافق شخصی رسید
⌛️
⌛️
طبق شنیده ها مدیران باشگاه پرسپولیس امروز با مدیربرنامه‌های محمد محبی به توافق رسیدند
⚽
قرار است در خصوص دریافت‌ رضایت نامه‌ بازیکن مذاکرات فردا انجام شود
⚽
محبی مشتاق است در پرسپولیس بازی کند تا…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136391" target="_blank">📅 09:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136390">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
چرا هیچ خبری از این بنده خدا نمیاد؟
❗️
حتی باشگاه پوستر خداحافظیم نزد براش
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/136390" target="_blank">📅 09:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136388">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
✅
محسن خلیلی: مذاکرات‌مثبتی با محمدمهدی زارع و باشگاه روسی داشته‌ایم. فعلا قراردادی امضا نشده اما باتوجه به توافقاتی که صورت گرفته بزودی زارع به جمع ما میپیونده و قرارداد رسمی امضا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/136388" target="_blank">📅 09:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136387">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎙
عادل فردوسی‌پور: افتخار می‌کنم دایی و باقری با یک تماس آمدند؛ یک ریال به هیچ میهمانی پول ندادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/136387" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136386">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVnfekoqyPMzc_n-YyUCZlSZwwuYw5WhBJAdWtF8Rz_XAOKEkugwiITBRcXNW0W9WZ13d8bFCroaT9n_QBCar8FzPVpr8suL8ggu_B0onjYUljGHm_zpKlL4useAph2gnqE_yIjbUHLE7Gub3YxkSNolFVSoaiMwS40aV_CIgpK03kSdZ8DEkhNluwbFLtvYhykQV4qtsPqHsHdKMmfGEn7DKZaZLM1twTEvTy9E7xfuqb3HFDKJhw7yALSEPQ7AsdcXchMp0U7dT9W8sXXHgekdV-3RBW6OWnurkqMiCsth6ONohs366JWYTUGLHSb4KEoE1lw1liO7rxCBHKZ29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فارس: محمدرضا اخباری به پرسپولیس پیوست و به زودی امضا می‌کنه و امروز و فردا رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/136386" target="_blank">📅 08:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136385">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎙
عادل فردوسی پور: همه امکانات در اختیار شماست یک رسانه را نمی‌توانید تحمل کنید؟
❗️
❗️
بعضی دشمنان پدر خودشان را درآوردند یک چیزی از من پیدا کنند، نگاه مردم را با هزار و چهارصد میلیارد هم عوض نمی‌کنم! من دیگه سنی ازم گذشته و همه چیز رو به دست آوردم تو زندگی…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/136385" target="_blank">📅 08:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136384">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQAquyVA_xlfKTve4mFfTmgRfcVDkxhfErJlw3EwY5iRsw6nGRjnk9-WSmjf7j-vMA_P_p3gNIJ5DdgFI9iEbTC_Wq179F0CYul3hyx95wOKVZqeWJjg6gwjqEZv0eC0-7oXirJGWGREFwtZvh0lvURUNXYgYEojefk0F9fT6tI9QrkS1uMKx0ak-p_2FYQGo5EQE8FDICMqpUEQZKuwws_vlqaC8Z7kMsVuRp37froQWHiyIHFcpz5hYKUBLcCZyVdd58Kv2TQ0dV-gSkl8FhPVMQ-wzGqfma2Gkz_kvpBj7QE8aPqEJwjrnVlFBw32Hf0NW_juOZTGmalX3POOLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
عادل فردوسی پور:
هر پلتفرمی برای حضور مهموناش چند میلیارد هزینه میکنه ولی من افتخار میکنم که سلاطین فوتبال ایران علی آقا دایی و کریم خان باقری فقط با یک تماس من به برنامم اومدند، به هیچ مهمانی حتی یک ریال ندادم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/136384" target="_blank">📅 08:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136383">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/636f7d426d.mp4?token=jtM1ZsUNy1O_CvDHpJgxgBo087ipDV7Vci-1ur0uUm5gVfn3fbJUYrnFzDObryGJnrFzrboxCqz8MxDL3Jdu4_e4FL12FVuNka2WzP3kuT6U3RE5h2JDW0JMj7Z3vKzdbPG_Vt8r8JBw-2b6Gum0xyW7CssEddiPLIgYci81XhiXb_NR7OASd16d7-aYBtPRxcLZ3wD2uEnVirBPTTKb4MhHJmnAIrO90-REthLeBemjZiPqcT5pdsHRfm4XDbM0nzET6oHsduMO0ETzFDXflkkE-Rgyc5mdsp5-rNyoNxx9dKr_-wJy3W_jHsQC6fdU0pOpPsQ69HhjtknsLrJ8ujlE_FqSh4D7VCSxhv-9YO34PM-QAUlsi21qGczxZdcQKLLVrd7-EJMynKoeyvXyV8potDKu8lpIivSXpuVV6YTNALEfRMUtXUnh6W11IUBTbqMXDzBjcWeR_RBVHgObPw-G18UsKkbhOlYQKvy69IvbR0rhv6ZmFJa_18kxL7hJt7nnRGT2NEPy-k8KKoyoynRNCoAXSRViFbamDdT6WEMmG_cw_xPERYmmyfqyREvWfF68iPxGWZoz6n7ohnnsgc6PIs2YDBwmSbvrd4kq8MOAMDWty01lf2VoxKrAIuH6tDDYiSpp49WlpYRYLkWFtRIo3tDIzkzUuCzbdUzsRkU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/636f7d426d.mp4?token=jtM1ZsUNy1O_CvDHpJgxgBo087ipDV7Vci-1ur0uUm5gVfn3fbJUYrnFzDObryGJnrFzrboxCqz8MxDL3Jdu4_e4FL12FVuNka2WzP3kuT6U3RE5h2JDW0JMj7Z3vKzdbPG_Vt8r8JBw-2b6Gum0xyW7CssEddiPLIgYci81XhiXb_NR7OASd16d7-aYBtPRxcLZ3wD2uEnVirBPTTKb4MhHJmnAIrO90-REthLeBemjZiPqcT5pdsHRfm4XDbM0nzET6oHsduMO0ETzFDXflkkE-Rgyc5mdsp5-rNyoNxx9dKr_-wJy3W_jHsQC6fdU0pOpPsQ69HhjtknsLrJ8ujlE_FqSh4D7VCSxhv-9YO34PM-QAUlsi21qGczxZdcQKLLVrd7-EJMynKoeyvXyV8potDKu8lpIivSXpuVV6YTNALEfRMUtXUnh6W11IUBTbqMXDzBjcWeR_RBVHgObPw-G18UsKkbhOlYQKvy69IvbR0rhv6ZmFJa_18kxL7hJt7nnRGT2NEPy-k8KKoyoynRNCoAXSRViFbamDdT6WEMmG_cw_xPERYmmyfqyREvWfF68iPxGWZoz6n7ohnnsgc6PIs2YDBwmSbvrd4kq8MOAMDWty01lf2VoxKrAIuH6tDDYiSpp49WlpYRYLkWFtRIo3tDIzkzUuCzbdUzsRkU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی پور: همه امکانات در اختیار شماست یک رسانه را نمی‌توانید تحمل کنید؟
❗️
❗️
بعضی دشمنان پدر خودشان را درآوردند یک چیزی از من پیدا کنند، نگاه مردم را با هزار و چهارصد میلیارد هم عوض نمی‌کنم! من دیگه سنی ازم گذشته و همه چیز رو به دست آوردم تو زندگی ولی نگران این 100 بچه نابغم که اینجا کار میکنند، واقعا چرا نمیذارید کار کنیم؟
🔴
🔴
برنامه 90 رو از من گرفتید خودم از صفر با بدبختی فوتبال 360 رو ساختم و اومدم بالا و اینم تحمل نمیکنید؟! اگر قرار باشه به حرف شما گوش بدم دیگر عادل فردوسی‌پور نیستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/136383" target="_blank">📅 08:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136381">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
گریه های عادل بخاطر بستن ناعادلانه سایت و اپلیکیشن فوتبال ۳۶۰ تو لایو یوتیوب و اینستاش.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/136381" target="_blank">📅 07:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136380">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP7T0SOzg-P5-juuByR3eSOvk3FnKbLozl6oE2Bu2lM3TQeTPHB-opkwLqi3kiYUQVfuF3xFcL-a9-nRV81pXT-gqWnH6sZMcDdaY4K2bQfUJCNTmX4yFxoGDc-QQezfSSFsjaz0PZyUfVnzRZD4Y5Owl-GF9MWS6d2LFM3LhHFu2ZH2x6xIXM9cj-YcDdt3QRRG4CGTSM9frcdASS0z-rLggfYXK5M-mAadKhI_ee7kDgDJX96VIYsQSIfnNvrepZ6g5__Vy3W3tQkkOunQa5Uo34gpPE3Uk-5RUiXTalJLF2sNrEBI-iDiwJrQe7tnypXWrW2JVsC5xGoTjbby4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گریه های عادل بخاطر بستن ناعادلانه سایت و اپلیکیشن فوتبال ۳۶۰ تو لایو یوتیوب و اینستاش.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/136380" target="_blank">📅 07:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136379">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
⏺
امیررضا رفیعی با حضور در سازمان لیگ قراردادش را با پرسپولیس به صورت یکطرفه فسخ کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/136379" target="_blank">📅 07:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136378">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
امیررضا رفیعی در تمرین امروز پرسپولیس حضور پیدا نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/136378" target="_blank">📅 07:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136377">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
پرسپولیس ممکنه زندگی نده، ولی
شادی میده
عشق میده
اینه داستان سرخ...
❤️
‌
سلام صبح بخیر پرسپولیسیها؛
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/136377" target="_blank">📅 07:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136376">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136376" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/136376" target="_blank">📅 01:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136375">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m53_fnsSG4oQXxdo8LEXyPHMfUdxHBjKNwJf6Dy6afBZ5wO0ed9DB5zspfnQ2NLb4sJ0_Jp3HUNxs7H9bTcIMT437OeUjGpnNF21YjMZb6hUAx2ws8gXyXQAjZjC-jcjW4LrcQz3Y8u4SckdwD2b8WF7uaVQQVsO-Gf_xFE-ITXCRS3achwEX098AEqeQhsVoiXyTe0Ek-LpE2_OeDc9qTQEdHW_WV1UXt0R9_y8YGIHT61-jrm1ll9Xr9QYxSXkpQ1t0NOKPooI7eISDUGOM5W7_u1PIQRvqAR6-W-CK_nPSxT565tephqjkQsWsO3zbraL_teQKPDjgS5Uvt256A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/136375" target="_blank">📅 01:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136374">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136374" target="_blank">📅 01:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136373">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
امیر قلعه نویی تو جدیدترین اظهاراتش از حکومت خواسته هر کسی از تیم ملی انتقاد کرد اونارو به عنوان وطن فروش سرکوب کنه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/136373" target="_blank">📅 00:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136372">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
قلعه نویی: ما ۳تا دستاورد بسیار بزرگ داشتیم.
🔴
۱. مظلومیت ایران را به گوش دنیا رساندیم.
🔴
۲. دومین دستاورد ما این بود تمام مردم ایران در امریکا با هر نگرشی، متحد و حامی ما شدند. بازی با نیوزلند بچه‌ها یک ربع دور استادیوم چرخیدن.
🔴
۳.  فودبالی بازی کردیم که…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/136372" target="_blank">📅 00:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136371">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=R70ELsAnLkQFVGIMB2zjdL2UQHVQLSo1HqBsPA7-8eueC5pC3sJZigDcV4rizw0IbwuyXAwLyI98Y75MoVVUZlfIDfK34IFPtj7Ut1WshazRdyHAPW20f1UcxhFXWVa6tXfhvbWafkXcrIA6jcCYBybWmZVvHqbhDrJJXEZZe6U0YnhzKvjA8B-CBjBv9-l3QYNimDOaW-vYenSTpKDlTN7_fbefDNAtqpWi-B4TicERrA6JUFgyxOSLo7Xp1mjT2lLpJSidb2a2AWUeHr2fDfhrzBu1UQD3v-aqcAumWGMVw4tZEzzYBnorMN_OUuN5SRXu80nEPd4XASFQTtLseA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=R70ELsAnLkQFVGIMB2zjdL2UQHVQLSo1HqBsPA7-8eueC5pC3sJZigDcV4rizw0IbwuyXAwLyI98Y75MoVVUZlfIDfK34IFPtj7Ut1WshazRdyHAPW20f1UcxhFXWVa6tXfhvbWafkXcrIA6jcCYBybWmZVvHqbhDrJJXEZZe6U0YnhzKvjA8B-CBjBv9-l3QYNimDOaW-vYenSTpKDlTN7_fbefDNAtqpWi-B4TicERrA6JUFgyxOSLo7Xp1mjT2lLpJSidb2a2AWUeHr2fDfhrzBu1UQD3v-aqcAumWGMVw4tZEzzYBnorMN_OUuN5SRXu80nEPd4XASFQTtLseA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🎙
عادل فردوسی‌پور: سایت و اپلیکیشن پلتفرم 360 بخاطر صحبت‌های امیر قلعه نویی بسته شد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136371" target="_blank">📅 00:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136370">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
سایت و اپلیکیشن فوتبال 360 ( برنامه عادل فردوسی پور ) چند دقیقه ای هستش که از دسترس خارج شده و خیلیا احتمال فیلتر شدنشو بخاطر حرفاش علیه قلعه نویی میدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/136370" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136369">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/136369" target="_blank">📅 00:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136368">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
گویا پل فلزی بندرعباس رو هم زدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136368" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136367">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
دانیال ایری به پرسپولیس پیوست/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136367" target="_blank">📅 23:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136366">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
قلعه نویی: ما ۳تا دستاورد بسیار بزرگ داشتیم.
🔴
۱. مظلومیت ایران را به گوش دنیا رساندیم.
🔴
۲. دومین دستاورد ما این بود تمام مردم ایران در امریکا با هر نگرشی، متحد و حامی ما شدند. بازی با نیوزلند بچه‌ها یک ربع دور استادیوم چرخیدن.
🔴
۳.  فودبالی بازی کردیم که…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136366" target="_blank">📅 23:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136365">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYEbACOKJJR18ui8LVuJGuNNjlC_L8KMEx1cAetCZ7EmXW5xO4B-Ho2PFTN26Ptx3finrJzWMRXxv0bgwoUgpabU6U9Li3svN__OA9gEP6TnBnAoNeRkBgaYZ9ZKy24yvKwJfpaRmysxIFQC500sihur9pcgLXKmVwitmyq0A9uBaVLpJnaHe4GRHuLGkM4btV0ku_OV2xlmHUsH1b1sBMymoI2bx118T1-aerUvrU985zgE-X_ABIN36qYWQkQYa_Z8MbH9SLMmznTTnBu91uWgkFVGQPFRuXi_VbykVML8bG88BGNFkdGlwgD6VHrKQ3fMnUtFTtv7OZD6Zgb5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سنتکام:
🔴
حملاتمون شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136365" target="_blank">📅 23:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136364">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
فووووری/سی بی اس:
📌
یک توافق موقت درحال شکل گیری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136364" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136363">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
قلعه‌نویی: من می‌توانستم مساوی با بلژیک رو خیلی بزرگ کنم اما خودم اولین کسی بودم که از خودم انتقاد کردم. ولی یکسری بی‌وطن ِ ایران‌فروش فضا رو خراب کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136363" target="_blank">📅 23:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136362">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
قلعه نویی: در همه جای دنیا انتقاد از سرمربی تیم ملی وجود دارد اما آنجا حسادت و عقده گشایی ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136362" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136361">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
فووووووووووری :
🚨
🚨
سرانجام و طبق شنیده ها پرسپولیس و نساجی به توافق رسیدن و ایری راهی پرسپولیس و ابرقویی راهی نساجی خواهد شد. به همراه مبلغی پول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136361" target="_blank">📅 23:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136360">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⚡️
مهدی تارتار به باشگاه دستور داده که تیم رو تا پایان هفته باید تکمیل کنند تا با نفرات کامل به اردوی ارزروم ترکیه برن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136360" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136359">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
تارتار گفته خودش کاپیتان‌ها و شماره پیراهن‌ها رو تعیین می‌کنه تا این مسائل باعث اختلاف بین بازیکنا نشه.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136359" target="_blank">📅 23:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136358">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
امیر قلعه نویی تو جدیدترین اظهاراتش از حکومت خواسته هر کسی از تیم ملی انتقاد کرد اونارو به عنوان وطن فروش سرکوب کنه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136358" target="_blank">📅 23:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136357">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
قندلی: هرکس از من انتقاد می‌کنه عقده ای هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136357" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136356">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136356" target="_blank">📅 23:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136355">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXidAXHktg2KQrBP6TVSfgXSZhVUGzbeRC8CR59P_HCWA_wqn1uuSIPS-5NZWwpD3WfxuVEmqF2QkBMrQMBjtGQDEG9CBbzTuIYMTjjgACPyLBGGIIm52ReoPFM6W1aCnF-JP05jqBBCmLJ_t4n-QGkkhkS6KDomQluRy5FsxVCIkYd-ehYcPzPD2Hy3_VFC8AipTu8q9SYMZ6eoSpmWmI6lTGyIYWGFFl2cBzUELPZra8AtEInl1vJ2r-n2oT-23MtY4QrT0gPLh0XVbzQ_yK_55qg4-Bvms8WrQIB7n51gApr1F1Xh6uquklttL9wjrcaoYcTprPK7emda0dVBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سید بندی لیگ نخبگان آسیا منطقه غرب
❌
استقلال در سید اول در کنار: الاهلی، العین، السد و ترتر تو سید سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136355" target="_blank">📅 23:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136354">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
❗️
#فوری | کانال 13 اسرائیلی:
🔴
ترامپ پیامی به کشورهای خلیج ارسال کرد:
🔴
اگر در این هفته به توافقی برای آتش‌بس دست نیابید، خود را برای یک تشدید جدی با ایران آماده کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136354" target="_blank">📅 23:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136353">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
سپاهان برای جدایی آریا یوسفی، خواستار انتقال ایگور سرگیف و حسین ابرقویی به این تیم شده که با مخالف باشگاه پرسپولیس رو به رو شده / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136353" target="_blank">📅 23:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136352">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
🔴
اخباری قراره بیاد تهران و با تارتار صحبت کنه و اگه همه چیز برای رقابتی بودن دروازه پرسپولیس اوکی بود قرارداد شو امضا کنه. احتمال اینکه اخباری پرسپولیسی بشه خیلی زیاده/ تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136352" target="_blank">📅 23:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136351">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
گروهبان قندلی مهمان امشب برنامه میساکی در شبکه سه خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136351" target="_blank">📅 23:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136350">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
ادامه حملات عادل فردوسی‌پور به قلعه‌نویی: هرکه از "غار" حرف بزند، قابل توجیه است؛ به جز آن کسی که کل جنگ را در دبی و ویلای آلانیا گذرانده باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136350" target="_blank">📅 22:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136349">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
#فوری
🔴
یاسر آسانی ستاره آلبانیایی فصل قبل استقلال در آستانه پیوستن به تراکتور قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136349" target="_blank">📅 22:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136348">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
❗️
#فوری | کانال 13 اسرائیلی:
🔴
ترامپ پیامی به کشورهای خلیج ارسال کرد:
🔴
اگر در این هفته به توافقی برای آتش‌بس دست نیابید، خود را برای یک تشدید جدی با ایران آماده کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136348" target="_blank">📅 22:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136347">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
دانیال ایری به پرسپولیس پیوست/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136347" target="_blank">📅 22:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136346">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136346" target="_blank">📅 22:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136345">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136345" target="_blank">📅 22:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136344">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
فیلمی که از تجهیزات نظامی ایرانی از خوزستان به سمت مرزهای کویت در حرکت است و در حال پخشه قدیمیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136344" target="_blank">📅 22:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136342">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
مجید عیدی خرید جدید پرسپولیس با شماره 2 که سالها بر تن امید عالیشاه بود برای پرسپولیس به میدان خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136342" target="_blank">📅 22:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136341">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
مجید عیدی خرید جدید پرسپولیس با شماره 2 که سالها بر تن امید عالیشاه بود برای پرسپولیس به میدان خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136341" target="_blank">📅 22:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136339">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136339" target="_blank">📅 22:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136336">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
🤝
پرسپولیس تا آخر هفته با چهار بازیکن جدید قرارداد امضا خواهد کرد / خبرنگار فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136336" target="_blank">📅 22:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136335">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136335" target="_blank">📅 22:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136334">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136334" target="_blank">📅 22:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136333">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136333" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136332">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEBkD6JgyU9DcsV6eQV3vXwa4NX_RIMvyVTq2FShZRl7ftRKZZKnQs123rDoUVqp-uDfbYq6Wuz8NfNGWpX6I_q_nuU04km6kzOIR5bI3bLPCLK7TUZf8wmBIzLKA81ioC787AzFo0bqw9PpCdMr0Bl6qYwBe9npPaEsyU5v_OyklmuzT9kcnZGsRqTNlwaEFZZ35leoQqEsbGwCG-sY6qSMBb9ut5q7FrF6bNfMmm2ClrxUpFvA2Hl4JT-VlbqsZwdCmApQvk5lp8qeaoM1lOJov3OWzFluGmNLfdh-SEKT1l1yammSPhqgMyBe1qr4XnM8YXPFFBDC8iDtkJkq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب حتی با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🤷‍♂️
@PeakyBetBlinders
@PeakyBetBlinders
@PeakyBetBlinders</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136332" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136331">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_aE9Hg-yQHzwPy0pme99r2RztqA-dJREfgLi5I_tF1TdbxaEdIwn9mfVwzbs819jMzdu2KN13KHX0q0yFKCR_9gakII-TR0DL4bTVwm5wG-FDfMhDYTqTjQmocFR7L-78Fzv3p2JDwFGdTY0-jrO3X7yu_guvK-mZBanTj4EM52gdb-9DidTeihOBml69G0CNCiGWnTwLFuFzHwckjjxmj7uyxzMhNB8EI-YH6ddQXWUv3x1B0HWUJ5VBT9g3BvtMSnIbjBXxSb4fjC4UxB5K4eiqJJzN7ewJmZd_HohfdN5fjVvXh4dT0Yfl44EXqaa_tuRhb-mxAai7oEx8Duow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووووووووووری :
🚨
🚨
سرانجام و طبق شنیده ها پرسپولیس و نساجی به توافق رسیدن و ایری راهی پرسپولیس و ابرقویی راهی نساجی خواهد شد. به همراه مبلغی پول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136331" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136330">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXxccNDY35iNhxZXD7mH3xt02n68a_UsKQiVO3WP0k1MBQUQsxIk7j86oR9bhSXprvqaPDTUc96SFWXRS8uL4XPa2hQdUjY1JfOR0E9mvHYRU9oprqLekR0gilZCnLn_TQLH6_MwljpQpOBVs6FoTc1XQIeYmBDJE-CROQmri3jWarOjJIIZYkkU774RE6tUzsmGx6WuWZ1kBRJWHeuH_V2Y53_wATjXXdOWR9TlwWrurF6pVNFNaCoZapRfphYi8vFc7KuiUcEyHe0OiRlME5qAfeSTRQ0qmNyQebsdAP2KK7ypJuO-9awzb3JvL4vQ_aAe-2RIydJeODJSddbb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136330" target="_blank">📅 21:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136329">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
شبکه "فاکس نیوز": نیروهای ویژه ارتش آمریکا سال‌هاست که برای ورود زمینی به ایران آموزش می‌بینند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136329" target="_blank">📅 21:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136328">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p01MRwD7mnKCMrm4MZptWsw5fgRVk1tXDBaB7Ksoczt62xB0C5RYzFdwbwcbiGkOHnEFUItK90zMQokdsURKYdaC63KQBrbfxk6Pj-NBlm0euxPqfsVkd7MbI3miWqq-OgH0i7HO7M9-7xPaCGJhlVkuY0udTwPt5BEdwrEMaKarMd3L41uSgZqDAXTlPLDgATDaz7_Am5U1TQZM4eOumk4DsqmVXIdmQw_GSc1Rs2-_-QL8lHlOoE-kdMUm7D6bLcR9BmLtk36h7Sh023TFDWpWvIRIklOuN5gr9bg1zW1WsV9ir6iYBbl-R5DAYJbTTuN-2mbbcFSVvLQ8K22ZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی 2030 به‌مناسبت صدساله شدن تورنومنت، با 64 تیم برگزار میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136328" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136327">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
سپاهان برای جدایی آریا یوسفی، خواستار انتقال ایگور سرگیف و حسین ابرقویی به این تیم شده که با مخالف باشگاه پرسپولیس رو به رو شده / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136327" target="_blank">📅 21:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136326">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از فرهیختگان
🚨
🚨
کسری طاهری در آستانه عقد قرارداد با پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/136326" target="_blank">📅 21:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136325">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
باشگاه پرسپولیس برای جذب کسری طاهری از فیفا استعلام گرفته و منتظر جواب فیفا ست تا برای جذبش اقدام کنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136325" target="_blank">📅 20:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136324">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
بمب سرخپوشان/ پرسپولیس با محبی به توافق شخصی رسید
⌛️
⌛️
طبق شنیده ها مدیران باشگاه پرسپولیس امروز با مدیربرنامه‌های محمد محبی به توافق رسیدند
⚽
قرار است در خصوص دریافت‌ رضایت نامه‌ بازیکن مذاکرات فردا انجام شود
⚽
محبی مشتاق است در پرسپولیس بازی کند تا…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136324" target="_blank">📅 20:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136323">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
تمام تمرکز پرسپولیس روی جذب محبیه و خیلی هم بهش نزدیکن ولی  اگه اوکی نشه کاظمیان میمونه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/136323" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
شنیده ها:پرسپولیس مقدمات لازم برای مذاکره با محبی رو شروع کرده و این مذاکرات در حال پیشرفته
🚨
جذب محبی نیاز به رضایتنامه باشگاه اماراتی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136322" target="_blank">📅 19:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری / آنا
🔴
جذب ایری توسط پرسپولیس منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136321" target="_blank">📅 19:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
سپاهان به پرسپولیس اعلام کرد هیچ‌جوره آریا یوسفی رو نمیفروشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136320" target="_blank">📅 19:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
محمدحسین میساکی: درحال حاضر کسرا طاهری رسماً بازیکن نساجی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136319" target="_blank">📅 19:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فرهیختگان:
🔴
تارتار یه وینگر تکنیکی می‌خواست، اما بعد از مذاکرات با یوسفی، هاشم‌نژاد، لیموچی، کوشکی و چند گزینه دیگه، مدیران پرسپولیس به این نتیجه رسیدن که محمدامین کاظمیان رو حفظ کنن و روی خودش حساب باز کنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136318" target="_blank">📅 18:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
فوووووووووری از حسین قهار
🔴
حسین قهار: هدف از مازاد کردن ابرقویی ؛ بازگشت مرتضی پورعلی گنجی به پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136317" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
تارتار از عملکرد حسین ابرقویی در تمرینات راضی نیست و به دنبال انتخاب جایگزین برای این بازیکن است‌...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136316" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136315">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
#فووووووووووری
🔴
تارتار علاوه بر پورعلی‌گنجی، برای حسین ابرقویی نیز اعلام عدم نیاز کرده و‌ معتقد است این بازیکن در ضد حملات حریف کند عمل می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/136315" target="_blank">📅 17:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136314">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
فوتبالی: مهدی تارتار به اخباری قول داده اگر توی تمرینات بهتر از پیام نیازمند باشه، فیکس پرسپولیس می‌شود. همین اعتماد به قول تارتار یکی از دلایل اصلی قبول پیشنهاد پرسپولیس بوده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/136314" target="_blank">📅 17:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136313">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
شهریار مغانلو به تراکتور پیوست
🚩
خط حمله تراکتور برای فصل بعد ؛
🔖
هاشم نژاد
🔖
ترابی
🔖
حسین زاده
🔖
اشترکالی
🔖
مغانلو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136313" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136312">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voFBWZkxpm_qZ1rmXeUCveYDzZbeegRfdUNBVybNG450HgidGY9RUF5Q4aosWdF71To4_jPuomhs47LCp7ehrzRGgIrtobEToS4Vzm9amTzqSjAQiM5yCKVCBki1wHfQyqyUWNBbihe_xnNoP05-N4NaOg-fRHRoK3ltPze3qA_vKttqNXSUHqRxygzB7z_6ThNq8HVp3uFou9pfNPed99CXA86fH-7Zds-RpJdgzv9-MRj0h83BwJ_FSNCfKsKz2Ny7dyosL53Y6HzjZu2Dx_G0w7YrwhWi7TGLN1LRJTLDj7KudTkd0IQe2RAiDzqjXvd5HzRWDXZ5CXRC_ItyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری / آنا
🔴
جذب ایری توسط پرسپولیس منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136312" target="_blank">📅 16:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136311">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
محمد عمری 3 ساله با پرسپولیس تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136311" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136310">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
شنیده ها:پرسپولیس امروز 40 میلیارد تومن + رضایت نامه قطعی کاظمیان رو به فولاد برای جذب ابوالفضل رزاق پور پیشنهاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136310" target="_blank">📅 16:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136309">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEQCEXTp3zaVmOt1vPWJMs3fpFtv7YxGJsu44CshkEYqmONE4MDL7naDFTgrZuZ2GmjuqgbtEwsWuNT7_EfL4LpBwUBp7J3f9YKaSzbTSKM4ITAC6rAazZPLefRI6w-0HfpfoVDE3oCdJSPYoKm8CM3B-AC9ZSMWes0ipeahJimcYvKicd01K-oD2r3oG71VkT6DQwvzyLOZ2JY1CNUcmFBw0VI71WLIABmYbOe4UNQK7eQdA8DsJ-CFlBlWTSIcWy7uCPmwu9tkA2lPK-DGKydY2QZ2ozu3oYYXGSAl5fV7hGw2JbJpJuOravzM1qHJMf0p5-sUtkkd-t2bXzyCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمد عمری 3 ساله با پرسپولیس تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136309" target="_blank">📅 16:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136308">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
❗️
پرسپولیس برای رزاق پور پیشنهاد پول به علاوه بازیکن به فولاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136308" target="_blank">📅 15:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136307">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
شنیده ها:پرسپولیس مقدمات لازم برای مذاکره با محبی رو شروع کرده و این مذاکرات در حال پیشرفته
🚨
جذب محبی نیاز به رضایتنامه باشگاه اماراتی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136307" target="_blank">📅 15:53 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
