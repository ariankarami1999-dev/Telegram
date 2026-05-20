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
<img src="https://cdn1.telesco.pe/file/AxHGH008aAcbgTsajHC0-ByfktHnXaKD8ENhbLQSBW0QzOnCnCawtNbgVWCPTMmNupWHtLU2Ev6fyA-B13BUfPcGVWZujrkHH7K03VONH4aVXvZ4jv-e32I4uFWlLONlC_qroNU_GB5mpuVrDRbvB0JeAA7a2-seo2C5P6zHsrS3vXBp1TrFLzaC6-T5qFoYXvvI8FeYQ1NVnw_OaHYs3ZWKtFa1HA1cBbsJWDa_reaXFAm_CwP_ULh_jzR6vG3sFDf7qnf1dD6wBS83PXAcGAxOL7Xb7dSGwpmcC-07sUZhl5nK8h9X7AngFBSUNYTmcFZGv_jjrxB9cJ3O2OSzbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 134K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 14:55:14</div>
<hr>

<div class="tg-post" id="msg-3217">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔭
خب گویا GitHub دیروز یه بمب سنگرشکن(
😂
) امنیتی خورده. خودشون تو توییترشون اومدن جزئیات رو دادن. خلاصه‌ش اینه:
⚠️
یه اکستنشن آلوده‌ی VS Code نصب شده بوده رو دستگاه یه کارمندشون. این افزونه مثل یه تروجان عمل کرده و دسترسی به ریپازیتوری‌های داخلی گیت‌هاب داده. هکرها ادعا کردن حدود ۳۸۰۰ تا ریپو دزدیدن که گیت‌هاب هم می‌گه "تقریباً درسته". اما عمق فاجعه اینه که هکرها تونسته باشن به ریپوهای سازمانی و API key ها و غیره شرکت‌هایی که از گیتهاب استفاده میکنن، دسترسی پیدا کنن.
و خود کارمندهای گیت‌هاب هم در مقابل:
- سریع اکستنشن رو از marketplace وی‌اس کد برداشتن.
- دستگاه رو ایزوله کردن.
- کلیدها و سیکرت‌های مهم رو همون روز عوض کردن (rotate کردن).
- الان دارن لاگ‌ها رو می‌گردن، چک می‌کنن چیزی مونده باشه یا نه، و منتظر فعالیت بعدی هکرها هستن.
گیت‌هاب گفته فعلاً فقط ریپوهای داخلی لو رفته، نه کد مردم. قول دادن گزارش کامل‌تری رو بعداً ارائه بدن.
👋
چرا این خبر حسابی وایرال شده؟
- طنز تلخ: مایکروسافت/گیت‌هاب که خودشون VS Code و marketplace رو مدیریت می‌کنن، با یه افزونه مسموم هک شدن! و برنامه‌نویس‌ها توی توییتر و Reddit دارن می‌گن "ما سال‌هاست التماس می‌کردیم marketplace رو درست کنید، حالا خودتون خوردید!"
- ترس عمومی: نشون می‌ده حمله به supply chain developer tools چقدر خطرناکه. تو دیگه کدت رو هرچقدر امن نگه داری، اگه اکستنشن VS Codeت هک بشه، همه چی تمومه.
- مردم دارن می‌گن: "دیگه به هیچ اکستنشنی اعتماد نمی‌کنم"، "device protection لازمه"، "Self-Host و گیت‌لب بهتره تا گیتهاب" و اینها.
و نکته‌ی جالب توجه اینه که این جور حمله‌ها دارن تبدیل به یه روند می‌شن چون هکرها می‌دونن توسعه‌دهنده‌ها ابزارهای زیادی نصب می‌کنن و permission دسترسی‌شون به افزونه‌ها هم معمولاً بالاست.
این نشون می‌ده که حتی توی دنیای امروز، هیچ چیزی ۱۰۰٪ امن نیست
📚</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/MatinSenPaii/3217" target="_blank">📅 14:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3216">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سؤال: چرا نمیشه روی اندروید به تنهایی این متد رو راه انداخت؟
جواب: دقیقا مثل روش Paqet، اگر خاطرتون باشه متد SNI spoofing هم نیاز به دسترسی ادمین داره و برای همین باید گوشی اندروید، طی یه فرآیند پیچیده‌ای(که جز ضرر هیچی برای گوشی من و شما مردم عادی نداره)، Root بشه.
سر همین تا قطع نشده یه لپ تاپ ویندوزی‌ای گیر بیارید و انجامش بدید و استفاده کنید</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/3216" target="_blank">📅 14:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3215">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو: https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/3215" target="_blank">📅 13:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3214">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو:
https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری تنظیمات خاص، لوکیشن ثابت آمریکا بگیرید.
با تشکر از کاربر توییتر
Kharabam
که اون قضیه‌ی رجیستری رو یاد داد(توی ویدئو توضیح دادم)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
ابتدا ویدئوی اصلی SNI-Spoof رو باید دیده باشید و راه‌اندازی کرده باشید:
https://t.me/MatinSenPaii/3186
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/3214" target="_blank">📅 13:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3213">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شاید دوستانی که تازه اومدن ندونن. اما رفقا من بارها از دی‌ماه که فعالیتم رو شروع کردم این قضیه گفتم.
من برنامه‌نویس بکند هستم اما متخصص شبکه نیستم. صرفا کامپیوتر رو دوست دارم و متدهایی که خودم یاد میگیرم رو سعی میکنم به زبان ساده واسه‌ی شما هم قرار بدم.
کار اصلی رو هم توسعه دهنده‌هایی که متخصص شبکه هستن و اون پشت دارن زحمت میکشن انجام میدن و من کوچیک همه‌شون هستم و تشکر بسیار زیاد دارم ازشون.
یک سری چیزها رو هم صرفا از سر کنجکاوی یاد میگیرم یا ترکیب کردن یه سری چیزا با همدیگه و صرفا محتواش رو ضبط میکنم و می‌ذارم
❤️
کانال یوتوبم هم قبل از دی‌ماه موضوعش انیمه و مانگا ژاپنی بود
😕</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/3213" target="_blank">📅 13:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3212">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هردوتا ویدئو(دانلود با نت ملی از یوتوب(بدون روبیکا و بله) و ارورهای رایج و ثابت کردن لوکیشن sni-spoof) رو ضبط کردم، منتها چون گفتم SNI ممکنه قطع بشه، اونو زودتر ادیت میکنم و میذارم. ویدئو یوتوب هم بعدش ادیت میکنم و قرار میدم واستون(همون که دنباله‌ی روش MITM بود)</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/3212" target="_blank">📅 12:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3211">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر اینترنت نداشتیم الان که اسپوف وصل شده موندیم با اینهمه اینترنت چیکار بکنیم:))</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/3211" target="_blank">📅 12:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امروز اگر برسم هم ویدئوی ادامه‌ی MITM رو داریم(سر یوتوب) و هم ویدئوی تغییر آیپی اسپوف برای گیم زدن</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/3208" target="_blank">📅 09:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3207">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رفقا اسپوف همچنان وصل؟</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3207" target="_blank">📅 07:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3206">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KylARx7eMErEDWncLsaJuWkytF7-dzQqgHA6qxSTyihee2VpZl4dweSLwP5FFgLh7dDWuTvdaWqzYFO31HMnITQpUqUKNc-32TwY_8luFmGU5QC8G9LcwYE73qFKBbZGfg68pxZrrMHI-YRF1K4PK31CQ0b2oNOAGqtfB2VP3ie70Wj9NMe-mPqbTr9T_hxbkY5HTFjiroTZBu_uNnNldYkhvz9Xg9EdFdGOBlSHybkZfuS-PnHhDrUbOJ_othMyuN3Z8t3-nBQEcgklliCx2U2nmOFCHePNBwM5_UnTvWt9WNHNcvz2FgTC0Gy-4u4LIXT6HtHl3vbGqMTIhgUBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت رایگان برای یادگیری باگ بانتی :
vulnweb.inst.lk
@Linuxor</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/MatinSenPaii/3206" target="_blank">📅 23:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3205">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">خب این هم آموزش SNI Spoof برای مک.
فرآیندش برای ویندوز و لینوکس کاملاً مشابه هم هستش. فقط باید فایل اجرایی‌ای که برای sni spoof هستش رو مطابق سیستم‌عاملتون دانلود کنین.
فرقی هم نداره که از چه برنامه‌ای برای کانفیگ‌ها استفاده کنین.
لینک دانلود برنامه SNI Spoof برای مک و لینوکس
برنامه آپلود شده در تلگرام
لیست کانفیگای جمع آوری شده توسط متین عزیز.
کانفیگ JSON
لینک دانلود ویدئو بالا برای اینترنت ایران.
@khosrow_v2ray</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3205" target="_blank">📅 22:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3204">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3204" target="_blank">📅 22:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3203">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KXw2agzSKARmKVxrZIo90t1yTjDOVOQKrVr1XOmAoD1j-R2NssJxKUru5yX36_AJFpPZJZQhoiRNr5CWTJvWlb-jU0NkD6qYpE1ZnzwxcgliudgW1tyO-nfzivtM9YMu_uVZt1EpnREH4_Mjk4lPcKGj5vC_LQ0ty_0tIGpgr3-bpkbjEjCk5hURYtvjsKo18RLQdPVH2XHjc91g84RaHq7zWmsiaisY5I-Vj0pYXFjYQRaEtBk4RqsZhYPhaa29kyNeZfxUFuiULs7BrSOvJareSlXXh9imDOL6cbNzuWLuM4ExOMfCIwnhaDJQNkJ6Dh0d51qer-OdYBqOAzlBOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ارور به علت پایین بودن ورژن ویندوزه</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/MatinSenPaii/3203" target="_blank">📅 21:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3202">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یک سری آیپی‌های کلودفلر وایت شدن گویا.
اما اختلال زیاد دارن
میرن و میان
اسکنرها رو روشن کنید، با تایم‌اوت بالا. ببینم چه می‌کنید</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/MatinSenPaii/3202" target="_blank">📅 20:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3201">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یه حسی بهم میگه حکومت یهو باز میکنه این متدها رو که ملت بپرن بسته اینترنت بخرن و مجدد قطع بشه، نمیدونم واقعا. قشنگ یه الگو شده
هر دو سه هفته یک بار یهو اسپوف یا یه متد خیلی راحت برای اتصال باز میشه و مجدداً بسته میشه. اعصاب خورد کن شده. نه دارن باز میکنن نه دارن میبندن</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3201" target="_blank">📅 20:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3200">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mN1DPPFrKikT0NH3ayZ7tTBdbfBmrqJewi6iTxGzAjn41mUAbMn9aIqQDP1TnxJN-itW-mj5ou60Rf3P8WFY2uxGM8Dw-SNsMFAGX2YXTF4p_HZbiHaG11x0c2sEIOCj99164D1xTGOELmSCEtAACiONX-aOidJoJbKTYG2bO6zB3fgfpxfmwPh8n53riIy1NNW_hx-I8b0IgX83sFTc0ObJBzd9BHUZrqVvGK9hnyZuLP4qlDqAMtXUOjnoxIec7JGUUVB9T-DNOQIdImFTbXqPySVwE5GkH-JGJpYryAeCz7FI4-OtGDTM2ZFf8oRM8kWLUc9X3XxmM1YJAK2Y1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر پنجره باز شد، و از کانفیگتون پینگ گرفتید، و -1 داد و اینجا هیچی ننوشت،
یا مجدد، WinError6 داد و بازم -1 گرفتید، یعنی اسپوف با این کانفیگ json(hcaptcha) روی اپراتور سرویس‌دهنده‌ی اینترنت شما بسته هستش</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3200" target="_blank">📅 20:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3199">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آیپی‌ای که اینجا بهتون میده، صد درصد کار میکنه روی شیر و خورشید و MahsaNG
❤️</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3199" target="_blank">📅 17:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3198">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j0nv7N92tHvzJoYYQu89Sqm9hjaNiZjUW3zZdici3R6PDxjPsxu-hXqc1V1_cBHMGlPGSGISPwt5Yn9iu6oM71NJLu3mZTudMifJ83ZT6F5S9VBBoF261bLXabtggssIpqQFwBKpmUa8KR61kG48SOBMUi4_r8V-BmA_IjOnXkKw-ARe5-n3j8adQ-r58bNJtfOu425BiZHtGwWFqO56XCh4UfaGX9R7det6UgS6WUqXuBfb9Z-TnD0IrVgSnSgskE58KXLHPltlIPfyS2th4JLgr_2MxjrqPqMnMIKxPmtKNpUSte3rw3wyBQ6yy2nQyw89NIUjFRhyzUGCeV7n-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ رو هم چک کنید، اسکنر برای Akamai و کاربردی برای شیر و خورشیده https://github.com/mirarr-app/network-checker</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3198" target="_blank">📅 17:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3195">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tsT3wJnpvUVePAgs8I5Nsfr35RtdnNytJtCOMK8SoDkb9aXZNvP9Fwka3JalIQjblbX1tLzVZch4bbN4CuKuzQNZzmxnG7GO8-xMOQJ9c3WSK73R8pzi2ObxiUALwWO6gKyNMW8K8JBamTLng0pYRABL1syfsTy2FS8XvUjq6giue8LvbTEgXCLp-ggXH3cSdubXrdvfqRcqEK1JJoQe5Eg35eshKSYU9endxa_iEHV7yIGZ36Mqy3jLb9rczfI_woZ6dyeW3NrD1l5d1N5gv6QXYeEq6a1_j8Aaz7uXaqbhqvAAfsCjQW_6bLjKXctBVxG4IDAKKYjo5HlPj4FgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3195" target="_blank">📅 15:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3194">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دقت کنید، اگر خود Spoof لاگ داره
و V2ray هم لاگ داره اما پینگا -1 هستن همچنان
یعنی مشکل از اپراتوره. اپراتورتون رو عوض کنید و با هرچی سیمکارت توی خونه دارید تست کنید. روی اینترنت خونگی هم به کرات دیدم توی طیف وسیع‌تری پاسخگو هستش</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/3194" target="_blank">📅 15:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3193">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/MatinSenPaii/3193" target="_blank">📅 14:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3192">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h9d-QDSaQjFT8wNHyhKf9WMRSmHsMwjRDAOsjHt5fGg6h2oVRHdvXAs2-dm4879rNvw3ovlgFaMZVrzmgQxJmmKA07Z-OjhGgr61Pr2zx8jo5wX3aowO58Ch4Ca3CkHCT0XG7JcItUNFB_8pzUi6MHujU54PQFh6toYg6S-EHTOmiUp1kb2aubgr47DMKKzmvMBiAdNLwyr5x-eFxe1fmH-x7l4D0WBYCkpg6e_Pmote8e-KhwT4spf0efgNF1ViSTy47ozUkxHodflS38JCEE9jSuRe0msqyjdsDDBEDJvvz8ksg4MqeV67fsozgLTzxSRWRZ58K29rsCynA-_wEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا داریم قله‌های پیشرفت رو فتح میکنیم</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/MatinSenPaii/3192" target="_blank">📅 13:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3191">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یکی از دوستان گفتش که روی آسیاتک، خود hcaptcha پینگ نمیده اما کانفیگ‌ها وصلن روی Spoof
یعنی json شما باید همون hcaptcha باشه، خیلی عادی ران میکنید و پینگ میگیرید و بعدش کانفیگ‌ها بهتون پینگ میدن.
راهنمای کامل</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/MatinSenPaii/3191" target="_blank">📅 12:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3190">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9a90f10d4b.mp4?token=U1X-00oigNovf55m0o2_YaPV4QpTjHYdZRR241cyZ0-kHA-P3P6o6YG12GMgly33uTcTHklnzGrN11f16PKZ1I59kW4Sc5u-uTeKdRgAg_c3kG0Rv9jHo8BqTTcgreUk4l4yhUibE5PaIc63edvVTmahxhg4ZPqfj0_sgN9o7G3ppWiGOcPDI2SJgdvUfE55uqfbAqCaH_NUuvpg1f4zPJ3mapXKRFdrUhKMIr2SMpf0bcrxiRyN_3_3iwzU2mdZMdtgKP7fz0lP53wRylUzNVrHzSFRPQ4D6HDj0Y6dN5rH3RVVTrKJ84BzCpL8X9Cnv1qkimtI7JjNVidw6fEDgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9a90f10d4b.mp4?token=U1X-00oigNovf55m0o2_YaPV4QpTjHYdZRR241cyZ0-kHA-P3P6o6YG12GMgly33uTcTHklnzGrN11f16PKZ1I59kW4Sc5u-uTeKdRgAg_c3kG0Rv9jHo8BqTTcgreUk4l4yhUibE5PaIc63edvVTmahxhg4ZPqfj0_sgN9o7G3ppWiGOcPDI2SJgdvUfE55uqfbAqCaH_NUuvpg1f4zPJ3mapXKRFdrUhKMIr2SMpf0bcrxiRyN_3_3iwzU2mdZMdtgKP7fz0lP53wRylUzNVrHzSFRPQ4D6HDj0Y6dN5rH3RVVTrKJ84BzCpL8X9Cnv1qkimtI7JjNVidw6fEDgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/MatinSenPaii/3190" target="_blank">📅 11:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3189">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✍️
سؤالات متداول راجب SNI-Spoof:
1- ارور WinError2 میگیرم توی اپ؟
این ارور به این معنیه که شما نرم‌افزار رو با Run as Administor ران نکردید. اگر مطمئنید که این کار رو کردید و باز هم این اروره رو میگیرید، به سادگی یک بار ببندید و مجددا باز کنید.
2- ارور WinError6 میگیرم توی اپ؟
این طبیعیه کاملا. باید هم بگیرید. اصلا اگر این رو نگیرید یعنی کانفیگتون کار نمیکنه. همینجوری پشت سر هم تکرار میشه و این اوکیه. مشکلی هم نیست
3- پس اگر ارور WinError6 میگیرم یعنی وصله؟
نه لزوما. ممکنه همچنان Hcaptcha روی اپراتورتون بسته باشه. پینگ هم بده اما کانفیگا -1 بدن بهتون با اینکه WinError6 هم میگیرید. با اپراتور دیگه‌ای امتحان کنید.
4- اگر
Hcaptcha.com
بهم پینگ بده توی ترمینال یعنی وصله قطعا؟
نه لزوما. توی سؤال قبلی عرض کردم
5- اگر
Hcaptcha.com
بهم پینگ نده توی ترمینال یعنی قطعه و کار نمیکنه؟
نه لزوما. توی یه برهه‌ای Hcaptcha پینگ هم نمیداد اما وقتی با اپ پترنیها ران میکردیم، کانفیگ‌هامون پینگ میداد
6- با چه اپراتوری بهتر جواب میگیرم؟
منطقه به منطقه فرق داره. همراه اول به طور مثال یه جا وصله، یه جا قطع. اکثر اپراتورهایی که دیدم وصل باشن، ایرانسل و سامانتل و رایتل و فیبر مخابرات و مبین نت بودش و adsl خونگی
7- کی این متد رو میبندن؟
به قول یکی از بچه‌ها هروقت ثبت نام ایران‌خودرو تموم شد:))
اصلا مشخص نیست کی میبندن و چرا باز شده و...
اما تا وصل هستش کارهای ضروریتون رو برسید لطفا. آپدیت‌های سیستم عامل و...
فقط روی اندروید حواستون باشه سیستم عاملتون نیاز به لاگین نداشته باشه بعد از آپدیت
8- دقت کنید، اگر خود Spoof لاگ داره
و V2ray هم لاگ داره اما پینگا -1 هستن همچنان
یعنی مشکل از اپراتوره. اپراتورتون رو عوض کنید و با هرچی سیمکارت توی خونه دارید تست کنید. روی اینترنت خونگی هم به کرات دیدم توی طیف وسیع‌تری پاسخگو هستش
9- چرا نمیشه روی اندروید به تنهایی این متد رو راه انداخت؟
دقیقا مثل روش Paqet، اگر خاطرتون باشه متد SNI spoofing هم نیاز به دسترسی ادمین داره و برای همین باید گوشی اندروید، طی یه فرآیند پیچیده‌ای(که جز ضرر هیچی برای گوشی من و شما مردم عادی نداره)، Root بشه.
سر همین تا قطع نشده یه لپ تاپ ویندوزی‌ای گیر بیارید و انجامش بدید و استفاده کنید</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/MatinSenPaii/3189" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3188">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v3zGQ4b0ndkn4_rOmJH-0Sq71vWM-TBXs7X-9szmWS_f1c3elDrry3Kdk37pfAqbGRveUm4-bpeen4IAsif45xsHD8wx6Scr_CzXavgBx_cyQ_v2kBWEBjVZt_tKdv5PjLxWKcKj8RlXvwXuDiE2b3rE4FCxybON-3Ri5qxt3bCp0MSjCahD-YQpjbgf2GTMU3X_BUEV6xlaf0yXv7tFbZTrdgcGFSTof_pk7Z3ZPqxA3JSH98SbtQ5-wSmvSFkKPVZjBkvt-hncdUEDs2xH9mv4f60gai2pRWaeIotQSPmL30bCsYX8GXWxL8f-mbw7pRppIxNly7Ft9HU_zod9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)))))))))))))))))))</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3188" target="_blank">📅 10:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3187">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">Matin SenPai
pinned «
⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:  1- آموزش پایه: https://t.me/MatinSenPaii/2627 2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید: https://t.me/MatinSenPaii/3168 3- و کانفیگ‌های این پست: https://t.me/MatinSenPaii/3183…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3187" target="_blank">📅 10:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3186">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شاید شبیه کلاهبردارا به نظر برسم اما می‌خوای نامحدود به اینترنت آزاد وصل بشیییییییی؟
😂</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/MatinSenPaii/3186" target="_blank">📅 10:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3184">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BwJhz-ip_jGbSp8a6BYIDoCMdLCX4Oq1b-l20VMQzcWs5DXmNECsrKFa39NfSo-ukRtCNzpsA9g03C7X9Ng0U3VC2pcAB25wEo0SWpzEYzTr4KhVlLh2Ylpo90TtNJAq6KYCAO9vAZfN_QGtdX-wTU2fKGqNE4yurTSo8Ww906a3_eHPyl6b-It_faBrvCLbHQcX7tul87EaggMwvPfPhI7k6IafopU1uFKpHRSl4jftu8soZYdX64Qz07xbiQsnP7g5W25K6fkoQyzcCJsWyFAfclX8rHrLnrLPShUzT5PKYaWE6Vgy9PyFDjWFsyLXu72pFeYF5WJJcZIjy0Os5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ml9beVVhNi_RhyprZEzjm-VZO88R0bv6AmvF1lhq-9h9fRr0X6b4qW1HvBiT6I_g3L6lu6QeY9pjlMXTni0JW5ghSWOjjbSM3L_fvVcn-Npy-W4YuH7KJSF9kw_0uJ-Ta5dkpDu2TeJA0Vg5UGpaLlvZ2leSXaSCss5rIABX1OiYOIMZF-khz7mGXXwwSalmefTM8OHG2p3RA3LZVt-x9bLmmpWdtgP4DbmrThGJXx0-PjabP9Kq5L6u6L3EGxdQ_w9k56tbxm-pBstU8ww2EREPPEgAFhLtkURxPQw94beb-pDurT0kwHidyFyHy9mbuLmtlSJcd3fY5viVtJp7-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاید شبیه کلاهبردارا به نظر برسم اما می‌خوای نامحدود به اینترنت آزاد وصل بشیییییییی؟
😂</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3184" target="_blank">📅 10:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3183">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/MatinSenPaii/3183" target="_blank">📅 10:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3182">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اگه spoof وصل بمونه یه هفته قیمت کانفیگ به زیر گیگی 10 هزار تومن سقوط میکنه
😂
این خط و این نشون</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3182" target="_blank">📅 10:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3181">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خب دوستان نتم رو کردم ایرانسل مجددا متصل شد
همراه اول و شاتل برای منطقه من جواب نمیده</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3181" target="_blank">📅 09:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3180">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">☠️
آموزش روش جدید و قدرتمند SNI Spoofing - اتصال رایگان و بدون هزینه به اینترنت آزاد!   دانلود فایل نرم افزار: https://t.me/MatinSenPaii/2617 آموزش edge tunnel روی کلودفلر: https://youtu.be/svYBcv4bSzo   توی این ویدیو آموزش کامل و قدم‌به‌قدم می‌دم که چطور بتونید…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3180" target="_blank">📅 09:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3179">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mKW7RF7-bT3CTHQwvc_ORGkJ5krX8kZQcfc_vjyNnbpiXtxhV7e-3P5dQLh3kkaCbkxjkCDyCaVNPLrNwrNU8JPrlZ-2MdUsaijftYdHTCl63BBShrl30Ha8rfq3Vc21AQjAkwTrpQBP5HAqsYXYGzoJPgPEVWrG824X6G-brAx4hOQwUvg7vrYq-cyN9OJQsX4FwUvOiKrXg10RzeICGCb7-KoQW-9ZZdgBbBeCEMkfC9TQTEvinWCyUdRGxnhQOVI0r6lFrBeflVWe0M4SDh0Ruwfn4hloTNCa2fwVNHbq9ikpGeMVtSIPi8Dp974ir4-9TgLnp8bpKDKJu9gkjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
اگر hcaptcha بهتون پینگ میده اما هیچ کانفیگی هیچ جوره وصل نمیشه، علتش اینه که هنوز پشت NAT هستید.
حالا چطوری مطمئن بشیم؟
اینو چک کنید اگه IP خودتون رو نوشته بود یعنی باید وصل بشه و مشکل یه جا دیگس
hcaptcha.com/cdn-cgi/trace
‎
و اگه IP خودتون نبود یعنی هنوز پشت NAT هستید.</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3179" target="_blank">📅 08:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3178">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">همچنان وصلید؟</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3178" target="_blank">📅 03:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3177">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اینور کلا تعطیل شد آپدیتی چیزی دارید سریع انجام بدید</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/MatinSenPaii/3177" target="_blank">📅 03:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3176">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NGYIaznrdWczj77JfPBsEBIHTOfpi4eBpD-2Xz4kJ-s2KEGslLQh1Ix1y3pauotzl4sDMZaw0KE3pHYEtRowr3NDT4SHSB0XJOv0kbrePsIukpuFOJUP7uLLjko4MtzhoqwzUs4K8BLf92e1NFo_lQGhXSqlVNqdxWRlj0GiTaGIvoSaD3SYtwobo6kQFsuNKWbGKRWQq76GG0kZ687QGs2GgFG7N_tCOhv4EcF-Ax9-4eURa4PhhGD__C5-wUr2rqwLaLaWao3Gr7Gap4a2TEqAmE1smJTQm9mBJudBEzlb2wypDSvMoBb9JHmyLiWO9QI122D9gmVdDhr-0z9vFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینور کلا تعطیل شد
آپدیتی چیزی دارید سریع انجام بدید</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3176" target="_blank">📅 02:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3174">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Spoof-SNI-Configs-List-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">12.5 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3174" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">هرچی کانفیگ ویژه‌ی SNI Spoof با پورت 40443 بود واستون جمع کردم از کانفیگای خودم و بچه‌ها و هرچیزی که توی کانال‌ها گذاشتن، توی این فایل txt واستون قرار دادم</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3174" target="_blank">📅 02:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3173">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">با این کانفیگ‌ها تست کنید:
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&type=ws&host=www.creationlong.org&path=%2Fassignment#1
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?encryption=none&security=tls&sni=sni.111000.indevs.in&fp=chrome&type=ws&host=sni.111000.indevs.in&path=%2F#2</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/MatinSenPaii/3173" target="_blank">📅 02:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3172">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یکی از دوستان توییتر گفته تامکت به قید وثیقه سنگین آزاد شده. امیدوارم که درست باشه این خبر
🔥</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3172" target="_blank">📅 02:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3171">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">Matin SenPai
pinned «
انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست: https://t.me/MatinSenPaii/2627 جیسونش هم این: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "104.19.229.21",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com"…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3171" target="_blank">📅 02:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3170">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uFSSr0_qjfhAYU9sgm2PTlo8UkFGf_lUEDYuiDS7q9sYLqETrfRgeo77I_yzZYDHwVtM_Wd5gpFVezRxOxSYCDrZxxYbBiSAYgxhTjC5gi-USdrexmG7Pu08ewdyoQ1PO75MUaKJCkVtUb_xN8xOS-u6pYz_JbE7zya85-LMcUId1nBBDeupRxLD9Y1jO3w8Ex_F9MjDBeoAQQ9N-GgNLLbkt6tJH6Cr7agUFIHj7xpezOKB0hxZDXIr00r44_7VvTbz16AnQMc5dmbiQVhJVu5igmWb5StxLV5ku6BCnT67ccfwLrvxqEWzd97iyaPEWFxo_k0W-L-Js7DF6_bQhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها واسم فرستاده از اسپوف
برید ببینم چه می‌کنید</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/MatinSenPaii/3170" target="_blank">📅 01:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3169">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست: https://t.me/MatinSenPaii/2627 جیسونش هم این: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "104.19.229.21",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com"…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3169" target="_blank">📅 01:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3168">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست:
https://t.me/MatinSenPaii/2627
جیسونش هم این:
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
www.hcaptcha.com
"
}
پینگ بگیرید ممکنه به جای 229، 230 نیاز باشه بذارید</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3168" target="_blank">📅 01:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3167">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">thefeed-android-v0.18.10-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/MatinSenPaii/3167" target="_blank">📅 01:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3166">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مجددا، از تمام کسایی که استار میزنن زیر پست‌ها و یا دونیت‌های کوچیک و بزرگ می‌کنن تشکر می‌کنم. من قدردان همه‌تون هستم
❤️</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3166" target="_blank">📅 23:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3165">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">Matin SenPai
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3165" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3164">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://guardts.ir/f/19995aceb6bb…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3164" target="_blank">📅 23:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3163">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hgXs-VzEeTFZlzv0Xx1SQP3wj401ZRkUMfG7rLY_EN_6yZJOfaAfUQweszAYFYLX6Ogbo6_Ce-sDTPZJwNEMFXu2vR9HxpQ_Hgb3mXpneRiF4lCZMLdttLNGdfyd0Zp5cBAsZwVSrEIbh2yx2ESDUP3KgYhcF-MVqlLaDKPIf1KNeV53fISvOoJPS2RP4-eyin-3p4QTgmBKuqkqfp01lywp5qhl-zPxWr0TDTiVQf3BUr5XErWrDIxy9lASM_eSC9gP2MXvKga9hc1gft0CRpYvYorUD-ybGFpLudEEWyR4ITlL2COX6yt9h4QHb8hAkJtNwTrDSroefFlCBT2N8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای میت، من با گوشی و لپ تاپ خودم روی دوتا جیمیل چک کردم و تماس برقرار شد و همون صدای Echo گوش‌خراش معروف میکروفون هم بین گوشی و لپ رد و بدل شد. نمیدونم چرا برای این دوستمون جواب نداده</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/MatinSenPaii/3163" target="_blank">📅 23:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3162">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3162" target="_blank">📅 23:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3161">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3161" target="_blank">📅 23:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3160">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting.json</div>
  <div class="tg-doc-extra">17.1 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3160" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ورژن 20 اومد چهل دقیقه پیش(توی ویدئو ورژن 19 استفاده شده بود)
و روی این ورژن،
Github.com
هم باز میشه به راحتی</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3160" target="_blank">📅 23:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3157">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">moein.bpf</div>
  <div class="tg-doc-extra">4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3157" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یکی از دوستان این رو دادش:
این برا سینگ باکسه اپ ها هم میاره یعنی لازم نی از مثلا سایت گوگل میت استفاده کنی با اپش میری</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/3157" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3156">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">متأسفانه جمنای و گوگل کولب باز نمیشن چون ما تحریم هستیم. یعنی از خارج تحریم هستیم</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3156" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3154">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">با تشکر از
@patterniha
، برنامه‌نویس پروژه، علت ضبط این ویدئو اول این بودش که مقدمه‌ای باشه بر روشی که برای یوتوب می‌خوام بگم، دوما این بودش که حس کردم این پروژه به اندازه‌ی کافی دیده نشده.</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/3154" target="_blank">📅 21:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3152">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">certificate_generator.bat</div>
  <div class="tg-doc-extra">56 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلهای سرتیفیکیت جنریتور(ویژه ویندوز)
و
کانفیگ MITM (ویژه اندروید و ویندوز)
لینک گیتهاب پروژه:
https://github.com/patterniha/MITM-DomainFronting
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/3152" target="_blank">📅 21:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3151">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود
این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.
لینک داخلی ویدئو:
https://guardts.ir/f/19995aceb6bb
لینک داخلی V2rayNG:
https://guardts.ir/f/7ae1503cd755
https://c224731.parspack.net/c224731/v2/v2rayNG_arm64-v8a_v2.1.7.apk
لینک داخلی V2rayN:
https://c147793.parspack.net/c147793/v2rayN_windows64_v7.20.2.zip
⚡️
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
لینک سایت Regery برای سرتیفیکیت جداگانه روی اندروید:
https://regery.com/en/security/ssl-tools/self-signed-certificate-generator
لینک فایل‌های مورد نیاز:
https://t.me/MatinSenPaii/3152
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد MITM، تحریم سرویس‌های گوگل رو دور بزنید.
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
💰
دونیت</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/MatinSenPaii/3151" target="_blank">📅 21:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3150">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یکی از دوستان توییتر گفته تامکت به قید وثیقه سنگین آزاد شده. امیدوارم که درست باشه این خبر
🔥</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3150" target="_blank">📅 21:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3149">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عالی بود
تمام 133.9 کیلوبایتی که برای این ویس دادم ارزششو داشت
🤣
🤣</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3149" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3148">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirmohammad</strong></div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3148" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3147">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">rdnbenet-windows.zip</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3147" target="_blank">📅 19:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3146">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W0sQhDQktlI8AyoWl5olzkns6iNwE-fWMWUTeAtWNb5_WTwSvpuPdLoNE6JeOhGxjgHaap54cRMhBzEH4wkAbdW8aYJg42hiWAORRHIVkDdxjzLYSKRA08JW6dICw6VuO_ywgYJ1uW9zdYTSY2bf80WiX_QOCcCOIVAO35jowpLHQRfFmLe-N2jS-mMJUTMFA3UhbHIIv9BJ7Wd36iy8iz_3z6E5o1Yu8WuSrLfNcpQgaGr3820YgVs8I66c50i8q3joXKe74wTq0xWqHTWhVsSA4Fsvj1LDLVlGeLhTeeQtxWbZYPGaobGhPk6Cwk_z3JUdg8ns6a2a8R3pTa8v7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه متد یوتوبه زیاد ساده نیست، اما خب قابل تحمله و زیاد هم پیچیده نیست. اون شکلی نیست که بتونید راحت برید توی یوتوب بچرخید، اما خب محدودیت حجمی و... هم نداره.</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3146" target="_blank">📅 19:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3145">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رفقا متد بله رو چندتا از دوستای متخصص توصیه کردن که اصلا نه انجام بدیم نه من آموزشش رو بدم. بر پایه‌ی سروش هم یکی الان دیدم نوشته بود و واسم فرستاده بودین. چون حتی سر متدای ارسال فایل هم اکانت یه سری از بچه‌ها بسته شده بود توی روبیکا و بله</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/3145" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3144">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خب با این اوصاف من آموزشه رو می‌ذارم. چیز پیچیده‌ای هم نیست اصلا
دوتا ویدئوی مجزا میشه اما چون خلاف قوانین یوتوبه فقط اینجا می‌ذارم</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/MatinSenPaii/3144" target="_blank">📅 17:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3143">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-poll">
<h4>📊 اینایی که میزنن دیدن نتایج ایران نیستن یا حال ندارن چک کنن؟</h4>
<ul>
<li>✓ ایران نیستم</li>
<li>✓ ایرانم. حال ندارم چک کنم</li>
<li>✓ دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3143" target="_blank">📅 17:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3141">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-poll">
<h4>📊 بفرمایید که،</h4>
<ul>
<li>✓ meet و drive بسته‌ان یا یکیش بسته‌ست❌</li>
<li>✓ هر دو واسم بالا میان راحت✅</li>
<li>✓ دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/3141" target="_blank">📅 17:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3138">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گوگل میت چی؟ :)</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3138" target="_blank">📅 17:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3137">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nNOR-0C5YHXvkdc-v3hQ1d62abciT6LyFZKgEB8b4rR-kGmPaMpeMjA_aRHX3UfLZBNpfzZ4vGGsmbhfyV32OPX3KrWG2qP6_GP9c2py1wx3KJvYAHm8eoAtWo16PMvzFKQTxEI9Zg-pf9cZEd3-fl67TOth2uAMZt7fvbGjsZ6iPuTZi1YUYhLAhmAN_eRBvA2tfPY_Kz3UvTd9Tfo_OY4taX9sEJeE6EQjjT1O1zkvup3_nrW-1F2VpIIJ2EFtumY9LNz-WjBMVZgpZ1hme9EJg7GIEQJn7K6wqwOGjqg0qNLHZYjlZl28QKQP6V5TEVBayAe5Uw74uuZRdyv5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان، drive.google.com روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3137" target="_blank">📅 17:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3136">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوستان، drive.google.com روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/3136" target="_blank">📅 17:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3135">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوستان،
drive.google.com
روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3135" target="_blank">📅 16:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3134">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بذارید بگم که چرا از زبان پایتون خسته شدم برای توسعه‌ی Back-End:
اول از همه، magic methodهای افتضاحش. یعنی هی باید __init__،__ str__،__ repr__، __add__، __getitem__ و هزارتای دیگه رو یادت باشه. که این باعث میشه هی دست به دامن ai بشی. و همینطور باعث اینکه خیلی وقتا نفهمی  چی داره پشت صحنه اتفاق می‌افته. یه operator ساده می‌نویسی، و یه magic method جادویی صدا زده می‌شه که اصلاً معلوم نیست کجاست. وقتی می‌خوای دیباگ کنی، باید بری دنبال این متدهای مخفی قبیله‌ی برگ(!) بگردی. و کلاً خیلی implicit و غیرشفافه.
دوم اینکه اینترپرتری یا مفسریه. یعنی خط به خط اجرا می‌شه. تا نرسه به خط ۲۰۰، نمی‌فهمی اون خط مشکل داره. باید کل برنامه رو ران کنی تا به اون خط برسه و بعد بفهمی "آها، اینجا یه typo داشتم" یا "این متغیر تعریف نشده بوده". یعنی عملا یه کد بیس بالای 5 هزار خط پیرت میکنه. از اون طرف توی زبان‌های کامپایلری مثل Go یا Rust، قبل از اجرا خود compiler همه‌چیز رو چک می‌کنه و بهت می‌گه کجاش اشتباهه. همه‌ی ارورا، یک جا. ولی توی پایتون باید خودت خط به خط بری و ارورا پیدا کنی.
سوم اینکه type safety نداره. یعنی یه متغیر الان string هست، یک ساعت دیگه int می‌شه، بعدش list می‌شه. تو runtime متوجه می‌شی که "اوه، اینجا یه list بود و برنامه کرش کرد". Type hintها هم که فقط تزئینین، اجباری نیستن و موقع runtime چک نمی‌شن.
چهارم اینکه performance خیلی ضعیفه. برای یه API ساده که ترافیک بالا داشته باشه، باید چندتا سرور بزنی بره بالا. حالا همون کار رو با Go بنویسی، با یه سرور راه می‌افته.
پنجم، dependency management و packaging اش یه فاجعست. pip، virtualenv، conda، poetry، pipenv... هرکس یه سازی میزنه برا خودش و شما باید به اون ساز برقصی. requirements.txt هم که دچار conflict میشه خیلی وقتا. Python 2 هم هنوز توی یه سری از پروژه‌ها هست که تبدیل کردنش بدبختیه.
خلاصه اینکه پایتون برای scriptهای کوچیک و زمینه‌ی هوش مصنوعی و ماشین لرنینگ خوبه، ولی برای production backend واقعاً اعصاب خورد ‌کنه. و من رفتم سراغ یه زبان compile شده که از همون اول بگه کجا اشتباه کردم، نه اینکه وسط شب production کرش کنه. مثل گولنگ یا حداقل حداقل تایپ‌اسکریپت.</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/3134" target="_blank">📅 16:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3133">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">WhiteDNS-1.5.0-x86.apk</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3133" target="_blank">📅 14:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3128">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3128" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر از مطمین نیستید، ورژن یونیورسال رو دانلود بکنید.</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/3128" target="_blank">📅 14:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3127">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bDlDGSWrCWFHEYWwCHMq8XZDWW1PHNthGa-wl4iejaRQxeZLGrjmRHLNpXj6SZk7j9p9OmZCG9thUYDI4bgMnxRgANTrhq3vgZUvoC_px1C3kbZeLRRCu6o32NbvpScOPw8OsOflkecV2i1QBjDxg7WKrNbAmrM99mNMTZ1glY42ZBZNhnplP9MNILAARay2OiS3vZUO5q3y1SRvJ9sRd6V5xQ-GjnhTxFEgnxjfHdXcVnGYEtYLQ-pjf76UnyPutze5Rt0MtJkkcQm08ZntZVhwv-tWjoYNQt1MTihzPT7IUpULj9AucRBOQLWpWIbsUCAGhqIzROE_FgpRKtHHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچین موردهایی رو زیاد واسم میفرستید دوستان. مسئله‌ای نیست؛ من که چیزی رو اختراع نکردم که زده باشن به اسم خودشون
😁
صرفا زحمت جمع‌آوریش رو کشیدم. منبع هم نذاشته، نذاشته. مهم نیست که.  هدف، وصل شدن مردمه</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/MatinSenPaii/3127" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3126">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">با گوشی هم میتونید باز کنید دیگه اون Index رو
یکی توییتر پرسیده بودش</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3126" target="_blank">📅 12:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3125">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه چیز جالب توجهی پیدا کردم که راجبش ویدئو بسازم. به درد خیلیا میخوره
ترکیب یه متد حال حاضر هست، با یه سایتی که اصلا هیچکس نمیشناسه. انقدر گشتم که پیدا کردم
برای VPN نیستش. برای دسترسی رایگان به محتوای یوتوبه
سر کار هستم الان، تموم که شدم واستون ویدئوش رو میگیرم</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3125" target="_blank">📅 11:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3123">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mgoFa1-ZkMpfplnoQuzj07MAc8BTWado9P2YxXFOs-8mXL_0GwzAOunO8MJMWKEYIP0mTC07iM6aINfYJ75uy8tGov7N7BKwpU2MdYMbLjlUIonZEQHK_D8BKqJ9GMbVEbdgomMJGC2cKOG0oEGbwGB6Ig6nW1uafsXbNp9YCxwTs75cYAGiCfi-fcVu7csFzuYeI7WKzBpvJbbvqo6tY0MlT2CFEuqWET4L1wBJCha2cDYSNnNeMnPKXN6sjgUggQ3fEE8ksnGrWkQODR8IsWZAYtFlEyYJXAaSfwA9hcylI-eNubgIyBfdrZJaZldQ456hOesul-Aaj4DwuWIq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kJ1coHYqMIHf_H-UoR2Najh4f0qR3yKaTTBS3kF459MD8x6K9ybI60Q5Ym5vIp8uiLklrbZ--DXbhsSWQNJLHUOVGPlomicTdRJ-u7-VwZR45Mn8rF3ldTecorCnA_iOmQ98RXm-Rq5kPXoaHWgZwptaKxbiebn-vYJoJdQ17DiQCyUPULCvL_6yOe-X2svRDvb3QbldWlnYuqI_cY_73voSFwZE4XiNoJGao88N6gWSF14cLW4zT3ugPOL7z6_-4PXvPSYmFO2N12pZeKK_wLajF4Vrc3Fp7LsAuKRMI3zzUMrA7Jh-aKgfh2D-GhG2dWqn10TJwXW0PjABhQz2dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فایل رو روی سیستم Extract کنید و بعدش راست کلیک کنید روی index.html و Open with chrome رو بزنید</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/3123" target="_blank">📅 10:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3122">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">cdn-ip-finder-main.zip</div>
  <div class="tg-doc-extra">723 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3122" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/MatinSenPaii/3122" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3121">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gzXz3-yQ-xSkc1B_9hgv5bZ6s54w6wIkUF4qhRakop2gOoFKHUtZP8ae0cVZ1taLZnb3kLTZ8autH0DY9PrObBqrh0Y8Z0CxD4lPSJMSESv9XO8vAOnM8nqzYyZSHoX6ZdyWAeQODQIi-9gh2oeAaWzAAVIoKwHjwVQtGM2rMDV6w6EOIFwKY7zgbtgKP-QRFzFwW-k2vG7FYiQn86wRfapxx6WEf_UEkai5LP4RbfyvaDk1AXdXuffZaNeUsJXxvF2-lmd-B2ldewLTPj72oL6YEDNnehec334olar8xtqfcfgpls8t0SOmNqC0mELNkl3UpROeUekwI3Ai1K_Fhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفر اسکنری که دیروز توی کانال قرار داده شده بود رو برداشته، و توسعه‌اش داده و تبدیلش کرده به یه اسکنر پر و پیمون تر. این هم پروژه‌اش هست:
https://github.com/hossein8360/cdn-ip-finder</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3121" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3120">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ایرانسل:
95.100.69.108
104.83.5.203
92.122.166.146
104.66.70.133
104.121.0.17
104.83.5.65
92.122.166.168
104.83.5.82
92.123.104.67
104.110.191.57
92.123.104.7
104.109.250.232
96.16.122.74
23.40.63.69
23.73.2.161
138.201.54.122
144.76.1.88
94.130.33.41
95.216.69.37
185.137.25.214
94.130.70.160
94.130.50.12
37.255.133.30
104.81.104.13
92.122.73.138
96.16.122.55
104.81.108.51
23.72.248.214
104.126.37.185
104.83.5.201
92.122.166.141
104.83.5.216
172.237.127.6
104.81.108.10
23.73.2.148
81.91.145.2
65.109.34.234
81.12.72.218
185.143.232.122
96.16.122.66
88.221.168.138
92.122.166.175
96.16.122.82
96.17.207.149
96.17.207.151
23.220.113.51
5.160.13.85
142.54.178.211
63.141.252.203
96.17.207.135
2.23.168.144
2.23.168.254
2.23.168.250
2.23.168.96
2.21.239.29
184.86.103.210
23.36.162.202
95.101.29.30
2.23.170.80
185.200.232.16
2.16.245.188
95.101.23.82
185.200.232.34
184.28.230.87
2.16.19.136
2.23.168.174
50.7.5.83
2.23.168.47</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/MatinSenPaii/3120" target="_blank">📅 10:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3119">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMliNSmGErEIH1GHJVhly8PR0C7EbmAdbFABUW4Zf83yrRcNiqvSSby5_cMHQi6c8vUzu8hf7-mfhbJ9EdagAd9MWx5jpqeLDKC-0Fkvf42Pdvs8q3W4wPDb7xHwHXKpNSPiQxvShkV5NUd79MsFO7c31mLOO0lG38erBiLAtiy_5qOvKOeui2trv5w7V1JtqgmuCbew0-H8RXkpAIqw99L8XdRiTBlCr-r9za0sXCyAaxEXLDDjoqQjpL5RD9H9nVyqH9lekn45IBD-0oAqG40Kr1O5OYdiYYN6rY19RDh8KQLR3w-pS3rAeCIRv2PdBSpi_aE3C973MTabzJ5neQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همینطور تغییر APN به
google.com
رو هم امتحان کنید. گویا روی ایرانسل بیشتر جوابگو بوده. من خودم روی همراه اول فقط با همون لیست آیپی‌هایی که دیروز گذاشتم وصلم به شیر و خورشید</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/3119" target="_blank">📅 10:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3118">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یکی از دوستان این نکته رو گفته بودش در مورد وارد کردن آیپی‌ها:
من چندین دفعه هم با سامسونگ هم شیائومی تو برنامه مهسا‌ان‌جی امتحان کردم
و یه چیزی فهمیدم که خیلی عجیب بود اما درست بود.
هنگامی که آی‌پی ها رو پس از اسکن، کپی می‌کنید که داخل برنامه وارد کنید حتما باید آی‌پی ها هرکدوم یک خط رو جداگونه داشته باشن
اینجوری مثلا
20.68.81.211
20.63.74.811
و اگه جداگونه نباشن و مثلا اینجوری کنار هم وارد بشن
23.96.52.41
86.52.17.76
و...
برای من متصل نمیشن و این رو امشب فهمیدم و با برنامه MahsaNG از سر کنجکاوی امتحانش کردم و در کمال ناباوری جواب داد و متصل شد الانم دارم آپدیتای گوشیمو انجام میدم.
و برای این که بدون زحمت خاصی جدا جدا هرکدوم یک خط رو در بر بگیرن، پس از اسکن کپی کردم، تو تلگرام ارسال کردم و از تلگرام کپی کردم و تو برنامه وارد کردم و درست شد.</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3118" target="_blank">📅 09:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3117">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3117" target="_blank">📅 00:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3116">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gb9wzOAYpQuAyidFDGEzPwrvbVg9v2C2_jXIfihycMoh81kULa6DRfpOAYpRbK7TOHWNT9O6zIke8PDdTywVDjHISkbyQzvLgJDyaWNY96dvTvyl0rKuA8BZdjB4NNXs0Yg-rNVwKxG8cYCPolqPeyfsRM34Oj_h_-CECdL00hPnaAPuCjyrnGWnrIQo5vNon36-b-bxDSy3drUI4GhFZSR-NLAbZKlStdF39y41_qf3nFIzYKd2vPXNc8csa6izo4pD7JShpb5zMHXy0QLQMq4gu1Nj4lNu-Qd6HKRVm4wgoTtjehKMOm4g1VL06MM-Lyt7Vl4oegi8c-b4n0YdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جدی جدی روز جهانی ارتباطات رو تبریک گفته
😐
تمام آدم‌هایی که شبا گرسنه خوابیدن و پول اجاره خونشونو نتونستن بدن و به فکر خودکشی بودن به خاطر اینکه کسب و کارشون نابود شد سر قطعی اینترنت از جلوی چشمام رد شدن</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3116" target="_blank">📅 23:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3115">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حس میکنم ضبط کردن ویدئوش ارزشی نداره زیاد.. خودتون اذیت میشین
اگه تا فردا دووم آورد می‌ذارم واستون</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/MatinSenPaii/3115" target="_blank">📅 23:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3114">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حدسم اینه تا صبح بیشتر نکشه که ببندنش متأسفانه. بله آخه دست خودشونه طبیعتا.
فیچر تماس تصویریش رو به راحتی میندازن سطل آشغال. یه ماه تمام کل دی ماه تمام اپلیکیشنای چت بسته بود اگر یادتون باشه</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/MatinSenPaii/3114" target="_blank">📅 23:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3113">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این ریپو رو هم چک کنید. متفاوته:
https://github.com/theermia/BaleTunnel</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/MatinSenPaii/3113" target="_blank">📅 23:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3112">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/3112" target="_blank">📅 23:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3111">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد می‌رسه.
https://github.com/kookoo1sabzy/BaleVPN/tree/main
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3111" target="_blank">📅 23:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3110">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">thefeed-android-v0.18.10-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3110" target="_blank">📅 23:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3109">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.18.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3109" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه‌ی جدید نرم‌افزار TheFeed برای خواندن اخبار کانال‌های تلگرام در شرایط قطعی اینترنت(کل جنگ با ریزالورا وصل بود)
کانفیگ‌های این اپ:
@thefeedconfig
لینک پروژه بر روی گیتلب:
https://gitlab.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3109" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3108">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a1u4j4tKJbxVe6mkTrHSpMUB6h5HWUt_RBEahvK94MmgFOzOWyUheXgQtzWwH7Dlvy6LgiuKC-lbsmU_U5LmGGpu_luP1f-YModY956VHU7Enk3c_aQhzLC4SGpFBz1XAmL8vB5HS56M7p6CWXKoAPOMKsyWH_JBKToCW2daNI9Zrb9hm-9lhDbF0Fu21Du1Tt8fLf9CLUOHP90tq4sLzz8i7YaCrCjwPeNHTn2J2rWmIYiGpD1Sflq-JHR4gIa2zw6cUk2CMJgZkHH6Fc82gOkoohq-WOIoGE_Oux4VTYcG7O5vLuWrGgw4yYX0oTyoDgMHho6G3xZONl4y-jLYLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیزاین با ai
:)))
دیزاینرای حرفه‌ای هرچند قرار نیست بیکار بشن. مخصوصا UI-UXکارها
آیدی طراح(پرامپت‌نویس؟!)</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3108" target="_blank">📅 21:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3107">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2PSuURFhESrqcVS1owAiB8PtW0hn1GzKRTYRWOcrPfyglH_ro3tXQBW4H9ZBTfnSfsoc7E2FAgOUFy5cYtbSya_Ocx5fRXOHDNp9K4iVODXas080l5FzNJ7JrkqG2MDIrpopkd-KfyX0x4KxdaJ3KaQ53500bgqRfDbVd9tQCsUeEp6X6N8-Rhc8ztj212B_WCwjpY7zUGlcoNmWAeb7e3udusJkeeFL_NGL-2qNZOUtPWC1eDyDm8VF2ycxYpwis9DG06NpePKkUYbCQFSV71TjA6XCFK-D3KRfcITg_9rPEzUKyJH5wc99NDjwJaF-6yTncHyWAFq69wcAkS5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان این اسکرین شات فیک هستش و ساخته‌ی دست یه سری از VPN فروش‌هاست. یه دور بخونید از روش میفهمید یارو خیلی هم عجله داشته
🤣
لذا خواهشمندیم زیرا</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/MatinSenPaii/3107" target="_blank">📅 18:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3106">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">CDN-IP-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/MatinSenPaii/3106" target="_blank">📅 16:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3105">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AHXxjZdP2-iWVuijAGz6UPxFfla2qlHMccg1z095PAdiZL9OvkFcDgZGoQj2isp-wQ4vm8eymd1rWUU9K5KvdgdTcf4aladOVyK504oVPws6oD_qS6i8l7r1Vrv6Fv5o2MoplwM4fil5IY-dBVGdckwYTPsWBIOzWrAP-C5XFiUmFph3JLY2nSFWwbc7XSIGpWXh48IBnEc2wfpNRtoeFmCMQqMLiouX8D74Kx6Hr6EpiaixhkfRLmSEDjjfQBjh5n3OJtHbYmBFZ6PmUpUdL4s5fT3y6mFDcu5BTrb-b0sUyWb7hJb3SugW57iu9K_Fup2LlTEBHmBST8omljWkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچین موردهایی رو زیاد واسم میفرستید دوستان.
مسئله‌ای نیست؛ من که چیزی رو اختراع نکردم که زده باشن به اسم خودشون
😁
صرفا زحمت جمع‌آوریش رو کشیدم. منبع هم نذاشته، نذاشته. مهم نیست که.
هدف، وصل شدن مردمه</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/3105" target="_blank">📅 15:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3104">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CDN-IP-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">4.7 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3104" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">هرچی آیپی CDN و ... از اول اومدن این متد توی توییتر و کانال‌های تلگرامی گذاشته شده بود رو جمع کردم، دادم AI تکراری‌هاش رو پاک کرد و واستون گذاشتم توی این فایل تکست. یه تست با اسکنر بکنید و بذارید متصل بشه.
صبور باشید
!</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/MatinSenPaii/3104" target="_blank">📅 14:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3103">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگر با شیر و خورشید وصل می‌شید، گزینه‌ی Share proxy on network رو فعال کنید. سپس به یه WiFi وصل بشید و کانکت کنید VPN رو. بعدش با هر دستگاه دیگه‌ای اگر این کانفیگ رو بزنید(با توجه به عدد و پورت خودتون تغییر بدید): socks://Og==@192.168.1.147:46597#ShirOKhorshid…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3103" target="_blank">📅 13:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3100">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MahsaNG_16_arm64-v8a.apk</div>
  <div class="tg-doc-extra">59.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3100" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش اتصال با آیپی‌های CDN از طریق نسخه‌ی جدید MahsaNG:
1- وارد نسخه‌ی 16 میشید(نیازی به هیچ کانفیگی نیست)
2- اون بالا روی حرف F میزنید
3- گزینه‌ی Psiphon Only رو روشن می‌کنید
4- روی Psiphon Setting کلیک می‌کنید
5- بخش Protocol رو می‌ذارید روی cdn_fronting
6- بخش Aggressive رو قرار میدید روی ON
7- توی بخش CDN Fronting Settings، آیپی‌هایی که من بالا واستون می‌ذارم برای هر اپراتور رو قرار میدید
8- روی Save Psiphon Setting میزنید
9- برمیگردید به منو اصلی برنامه، روی دکمه‌ی گرد پایین سمت راست(اتصال) میزنید
10- یه نوتیفیکیشن Psiphon tunnel connecting میاد بالا. اون وقتی تبدیل بشه به connected یعنی وصل شده
توضیحات:
1- نسخه arm64 برای اکثر گوشی‌های 2020 به جلوتر مناسبه
2- نسخه arembi برای گوشی‌های قبل 2020 عموما
3- نسخه‌ی universal روی هر گوشی‌ای نصب میشه فقط حجمش بالاتره چون تلفیق تمام نسخه‌هاست اما حجم نهایی نصب شده روی گوشی شما همون دوتا بالاییه
لینک‌های داخلی:
1- نسخه arm64 داخلی:
https://guardts.ir/f/ee1f60ae6d33
2- نسخه arembi داخلی:
https://guardts.ir/f/9d474d75a4fb
3- نسخه universal داخلی:
https://guardts.ir/f/7af85b518302
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/MatinSenPaii/3100" target="_blank">📅 12:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3099">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompng(Asal)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.html</div>
  <div class="tg-doc-extra">21.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3099" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📍
اسکنر سبک آیپی برای شیر و خورشید
-فایل بالا رو با مرورگر باز کنین
-رنج آماده آیپی رو انتخاب کنین(با میتونین دستی رنج‌های آیپی مد نظرتونو وارد کنین در بخش لیست بازه /ip)
-بدون وی پی ان اسکن کنین .
-لیست آیپی‌های سازگار با نتتون در انتهای صفحه در دسترستون قرار میگیره و میتونین وارد شیرو خورشید کنین.
@p1ctok</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/MatinSenPaii/3099" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3098">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef65e3054f.mp4?token=ZJrfOxJHeTf1D9f5qZAXqThFX0S5nlRvYIGlDwXO4BMw4fpOTg0nux0EGk4rZd5ziZsdRXuIPTqJ2gbiXJy-yhCXv-URpxVD8FseNaIrMTCh5xr33WqDjl-U7kJjt2KyQOyYvjquxFhqRjG61_-6qH8J-aGraf52WtK6OpUAZYSsSNekdmTHfHHoRsrqyqYa1b9AOV28kEyArI-_h-La6zQmsIa8jTFW2M5G0S6mtMkC8F5RwnkR8OvAAsP4uA8vSUSkswCMMfd4Amxzql8XjUpEUgxnnjR_TZWpm6_8kpOWWoOnKSeifiExPqSFZAvEg8fY6vjn7NzM64Qc9HPbnzQIekdDfbgNsFuqkEkLIhV8O1g-5nPsfUfkDM-2AqcVkHekK3csH9Il0l317lDAEbSPy2flg9NvRM5x8SHzSSV9616VFu6PDDRY5eBbeDznRE7cKEsllQ7AHguNt9z61X34Tky9Bs89JyjhPl8xNjIDJGbRtqPN6iyjWjErXq9XDpjZytfASagXtCpov44ScdgukFjycSP32_-V2wP4q2n5vaNHGmQaEdE6uTFzUzLUvbsLONxhkUfDu5jlL_xivMVpGe8GTaDTJxITHp7YyQ2OZ2dJRen-vuJCnUGAZml1skIjmyB2nzmgykfPLk-XtYONUuwAKTvlda6aZq3S3k0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef65e3054f.mp4?token=ZJrfOxJHeTf1D9f5qZAXqThFX0S5nlRvYIGlDwXO4BMw4fpOTg0nux0EGk4rZd5ziZsdRXuIPTqJ2gbiXJy-yhCXv-URpxVD8FseNaIrMTCh5xr33WqDjl-U7kJjt2KyQOyYvjquxFhqRjG61_-6qH8J-aGraf52WtK6OpUAZYSsSNekdmTHfHHoRsrqyqYa1b9AOV28kEyArI-_h-La6zQmsIa8jTFW2M5G0S6mtMkC8F5RwnkR8OvAAsP4uA8vSUSkswCMMfd4Amxzql8XjUpEUgxnnjR_TZWpm6_8kpOWWoOnKSeifiExPqSFZAvEg8fY6vjn7NzM64Qc9HPbnzQIekdDfbgNsFuqkEkLIhV8O1g-5nPsfUfkDM-2AqcVkHekK3csH9Il0l317lDAEbSPy2flg9NvRM5x8SHzSSV9616VFu6PDDRY5eBbeDznRE7cKEsllQ7AHguNt9z61X34Tky9Bs89JyjhPl8xNjIDJGbRtqPN6iyjWjErXq9XDpjZytfASagXtCpov44ScdgukFjycSP32_-V2wP4q2n5vaNHGmQaEdE6uTFzUzLUvbsLONxhkUfDu5jlL_xivMVpGe8GTaDTJxITHp7YyQ2OZ2dJRen-vuJCnUGAZml1skIjmyB2nzmgykfPLk-XtYONUuwAKTvlda6aZq3S3k0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
آموزش کار با اسکنر آیپی برای اتصال از طریق CDN با هسته‌ی سایفون اپ MahsaNG ورژن 16
این آموزش رو فربد عزیز زحمت کشیدن ضبط کردن و برای من فرستادن
فایل‌های مربوطه رو هم در ادامه قرار میدم واستون، و دارم فایلهای MahsaNG نسخه 16 رو واستون روی لینک داخلی هم آپلود میکنم</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3098" target="_blank">📅 12:08 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
