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
<img src="https://cdn4.telesco.pe/file/T8fTVauWYWc2vY7wODxtSi6FWD2eMVKWjWNo9xHMIyh23g5Eiu08EEhFl9vJMJHlNW6bfD-9rOMu0-I0md56QAgVzmlEx6mUqPFUaUakt4sqlOd-7uHila4RW7nKZEU85dBABMhgFl4zlhPv5mGK8LiDNbcKj_zk5PVOM2R9xG_1Wspz7SwEmmLSG-9uyleQ7GDR4nHNoo7U45n0r6pSz9SL-1J1SpqD0MTEyIEDdpL5UDAa2vncgmaq-xoSzUJHxNzMLEUYqpnC13C4rp5hS892e8OeGmog6FYTdYBxdggrGdXUg_ifllO6pfBJYp32DWMLJ9Ayhut50M1HwA6M1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.17M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 17:11:32</div>
<hr>

<div class="tg-post" id="msg-679708">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس سازمان بازرسی: با وجود شرایط دشوار، کمبود کالا در بازار نداشته‌ایم.
🔹
کارت امید مادر برای بیش از ۲۵۷ هزار نفر شارژ شد.
🔹
واکنش حماس به مخالفت نتانیاهو با طرح شورای صلح غزه: متعهد باشید تا متعهد باشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/akhbarefori/679708" target="_blank">📅 17:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679707">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
رویترز: بیشتر بورس‌های خلیج فارس در حالی که سرمایه‌گذارانشان منتظر اخبار توافق درمورد تنگه هرمز بودند، کاهش یافتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/akhbarefori/679707" target="_blank">📅 17:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679706">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ_gsbQNBAAKzruZOY7dSqHvN51XNLqOxJsaLwCIq-fJTv_CI3j5jtGU2yT_8LkgxTDkGXsbof_AFg4fr4AoXdmN2qlJDAwkl1cZuW2qZ3Xh5qMf5O0dGoEjU0QupZ9XCKJoqHb7YYxTy1FOF2qyoi4uU0SpkJC1K0dJXX1snZkHnihTy7sbJaBl-tIrPj7gBblDfttf8970l9k0q2z5Dbfa891RWz3wO7HyuMc5RFoTRZLG1P-jyVRICqBbY_3eBDiHsIyMF9aSVK3nIhZMlAATGGz0De09O9VJ7cuu0Sg5J6nytSc-q2LQ751XPCZo95Y6iXnhZhM2jyLXgs0aew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از نیمه دوم سال، طلایی شوید
🔵
اگر قصد سرمایه‌گذاری در طلا را دارید، بهتر است پیش از آغاز نیمه دوم سال و قبل از انعکاس عوامل اثرگذار در قیمت‌ها اقدام کنید.
🟢
بازدهی مثبت طلا در بیشتر نیمه‌های دوم سال
🟢
افزایش تقاضای ارز و اثر آن بر قیمت طلای داخلی
🟢
سرمایه‌گذاری در صندوق طلا بدون اجرت ساخت و ریسک نگهداری فیزیکی
🟢
پشتوانه فیزیکی شمش و سکه در انبارهای بورس کالا
🟢
ترکیب بهینه گواهی سپرده شمش و سکه در رز ترنج
🟢
شروع سرمایه‌گذاری در رز ترنج از ۱۰۰ هزار تومان
🟢
قابل معامله در تمام کارگزاری‌ها با نماد «رز ترنج»
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/679706" target="_blank">📅 17:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679705">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1bd32f01.mp4?token=llevXAutXfnktwgw-GM7HalEQwNNGdhxhaQf4bUHTmPdEHn3Kp7Mj5cr_rIQ5XcUq-BUhUnVTryVJ2WYSBnnsWCuF5WnKZ-E9ORIbmSeoAQd3jPwfJluoaMbhSBkIdwurFIomXrP7vutXH9aJOVi0y7kdTp0jMUygX5F0UZ9pMqsBsmjLVDcEesyY0clR7-1gBHOr_7WZmbqgltemTeW26KAf-YYiAk-VZZYCgEZ8qcS3Kw21hJwiJyPZ5BQ3HCW_FdsrFMbPdA8et7PtGHdJz-4h9sgMcpXp9kNvFbqK7nEKnxEAUvq7-YQFPRpR44IgmeFzaBM4D5Ngo0oQoX-Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1bd32f01.mp4?token=llevXAutXfnktwgw-GM7HalEQwNNGdhxhaQf4bUHTmPdEHn3Kp7Mj5cr_rIQ5XcUq-BUhUnVTryVJ2WYSBnnsWCuF5WnKZ-E9ORIbmSeoAQd3jPwfJluoaMbhSBkIdwurFIomXrP7vutXH9aJOVi0y7kdTp0jMUygX5F0UZ9pMqsBsmjLVDcEesyY0clR7-1gBHOr_7WZmbqgltemTeW26KAf-YYiAk-VZZYCgEZ8qcS3Kw21hJwiJyPZ5BQ3HCW_FdsrFMbPdA8et7PtGHdJz-4h9sgMcpXp9kNvFbqK7nEKnxEAUvq7-YQFPRpR44IgmeFzaBM4D5Ngo0oQoX-Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین در محاصره طوفان دلفین
🔹
طوفان شدید «دلفین» در استان چجیانگ چین با بادهای شدید باعث اعلام وضعیت اضطراری شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/akhbarefori/679705" target="_blank">📅 16:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679704">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
۴۲ کشته و زخمی در حملات ارتش یمن به بندر المخا
🔹
منابع خبری یمن از کشته شدن ۷ نفر و زخمی شدن ۳۵ نفر دیگر در حملات امروز نیروهای مسلح یمن به بندر المخا واقع در استان تعز خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/679704" target="_blank">📅 16:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679703">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2ca95668.mp4?token=h4EkLXTPZnnV8iQCXHUrc5uVriblsYP2XgJuqJ1Zf0s_PVwz7ab8XkfG7L18s_kUiUWiud-5nZ2HNYFYrJvljAUDuv9iwzD9hvITJRzESKXrFWhFoZIfsi4gq8TZrfP6oqMuoC3SiNdDwlh20rkp5vJRezn5q6o4MdUJzzINyqFcAyq4-a67eaqaepnJQ3RRDw6DVEVXE5iDchxfwPla6Sg_Ymxkzl9Fg-ChRf54WFa9V6YkH7gMzQhMHw48eYSSQKBYulwQP9qmwtDggpwY9v5yXwZCxlCsmuRSa62ZhKKnldkGJspUvi4LEtgraVvph5l41q9JFhNVhXXIeZuR6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2ca95668.mp4?token=h4EkLXTPZnnV8iQCXHUrc5uVriblsYP2XgJuqJ1Zf0s_PVwz7ab8XkfG7L18s_kUiUWiud-5nZ2HNYFYrJvljAUDuv9iwzD9hvITJRzESKXrFWhFoZIfsi4gq8TZrfP6oqMuoC3SiNdDwlh20rkp5vJRezn5q6o4MdUJzzINyqFcAyq4-a67eaqaepnJQ3RRDw6DVEVXE5iDchxfwPla6Sg_Ymxkzl9Fg-ChRf54WFa9V6YkH7gMzQhMHw48eYSSQKBYulwQP9qmwtDggpwY9v5yXwZCxlCsmuRSa62ZhKKnldkGJspUvi4LEtgraVvph5l41q9JFhNVhXXIeZuR6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکنیک سنتی که توسط چوپانان جوان قبیله بنا اتیوپی انجام می‌شود
🔹
چوپانان جوان برای مراقبت از دام‌ها و دوری از مارها و شکارچیان روی چوب‌های بلند راه می‌روند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/679703" target="_blank">📅 16:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679702">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بیانیه شدیداللحن سازمان حشد شعبی عراق و حمایت از فالح الفیاض
🔹
سازمان حشد شعبی عراق اتهامات مطرح‌شده علیه رئیس این سازمان را افترا خواند و با تأکید بر اینکه دستورات هوشیاری و آماده‌باش پیش از حمله صادر شده بود، از پیگیری قانونی علیه شایعه‌سازان خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/679702" target="_blank">📅 16:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679701">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sa3kddMkGv45JHanzQSDgVWWTNGsK0Ga1hgGOvp482hFICeOOic5_qgd304hGcEE4sn71WKF24be6WFX6iZDcALxrOgInlcynCTKPfZt7sT6wSmJHOFv2HZwS-fP_RI1FMmDmb9nEfMM7SonS0atajCfikPxGsFCdYjnYItocvkWjaO-k0lXxQqpTiz2scs0Nay8AEXHzkWwn1DiSXoFOR8imzuDFKdsd703KiqK-H_fo0rz9Na6c24FLAD1Id7uyD-wJ-92IQ1NrR0NNHdAFpRg3MieaK4NQd5poua5nf_AozIF-pIJ7XU_KjkLlU03N8NGksy-rK9b3za0o7CegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
قیمت طلا منتظر جمع‌شدن پول ما نمی‌مونه.
اگه خرید طلا رو گذاشتی برای وقتی که پولت کامل جمع بشه، باید بدونی که با ازکی‌وام امکان دریافت اعتبار خرید قسطی طلا تا سقف ۲۰۰ میلیون تومان رو داری و می‌تونی آنلاین طلا بخری.
✅
فوری
✅
بدون نیاز به چک و ضامن
✅
با اقساط منعطف ۶ تا ۲۴ ماهه
شاید این همون فرصتی باشه که شروع خرید طلا رو دیگه به آینده موکول نکنی
👇
https://azvm.co/ptw0</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/679701" target="_blank">📅 16:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679700">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b463873e3.mp4?token=lhGwyay97ab50Qz9HPSYeMK6bSHjjZ79Cv01J-6ceigPxgVspdNTOu-HGAQGQXe8xU04YWym40d2kRzOQ2gHfPEPn3RnUjRFy6hJ59WfvQhrT7WN-OZJAQaShCn0JDi7kzvjfrVLrsULqwVSGbEXLJR6sHrHc2Y2FX7DOZbD4qoowGq-h4lm5iu8iNpSJplMfx-gy3BCqL_oQtDF9QdNZeaK3c34zHYZmXOhG5zHIuAZuOdItNZjn_iB4-V7oxhEbdRcXO1WCtJuta-Lsp9qbVX0kvtVDCY324nB8kDFU9nNuMeePpyhxzRIe5jFZjnHEaAmfLNf2YfqChPGK4BNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b463873e3.mp4?token=lhGwyay97ab50Qz9HPSYeMK6bSHjjZ79Cv01J-6ceigPxgVspdNTOu-HGAQGQXe8xU04YWym40d2kRzOQ2gHfPEPn3RnUjRFy6hJ59WfvQhrT7WN-OZJAQaShCn0JDi7kzvjfrVLrsULqwVSGbEXLJR6sHrHc2Y2FX7DOZbD4qoowGq-h4lm5iu8iNpSJplMfx-gy3BCqL_oQtDF9QdNZeaK3c34zHYZmXOhG5zHIuAZuOdItNZjn_iB4-V7oxhEbdRcXO1WCtJuta-Lsp9qbVX0kvtVDCY324nB8kDFU9nNuMeePpyhxzRIe5jFZjnHEaAmfLNf2YfqChPGK4BNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های خارجی درباره جنگ ایران و آمریکا چه می‌گویند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/679700" target="_blank">📅 16:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679699">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
الجزیره: وزارت خارجه سوریه اعلام کرد با روسیه درمورد پایگاه‌های طرطوس و حمیمیم که در اختیار ارتش روسیه هستند به تفاهم رسیده است
🔹
طبق این تفاهم، قرار است در ۳ ماه آینده روند اجرایی برای تبدیل پایگاه‌های نظامی روسیه به مراکز آموزشی مشترک طی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/679699" target="_blank">📅 16:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679698">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c1573314.mp4?token=BHz4oh2YQm5J-qbq33CkMmvTEroogblRbybZRx8NYQVkeQBuluydBVwGXVP2jhs8O1ybwrn3WqnM8Qd3PUyeg9_bsXGghewGNtbKvsX9XBkfknBeTkKHYu97ltF1kfxwo6-6WVHH9h6upWnrR12U-xWl-e69aHvHFkubRtecKPYC97cEZCZSK8IA_6mFef-30sdPVLkUc1HP0O8M2NFwn6n7gOH1c-ghicqta9uDOnNj9X4P29u6hk266SpxSOpp9Kj5IZwCbsvWuqDDUgvRCmJb1SFVCxvUUP-zw7c3FsLJ1Jg2U_YIw1BwIsKfRoj7MjohjF8F2XLRbXBrkyMLqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c1573314.mp4?token=BHz4oh2YQm5J-qbq33CkMmvTEroogblRbybZRx8NYQVkeQBuluydBVwGXVP2jhs8O1ybwrn3WqnM8Qd3PUyeg9_bsXGghewGNtbKvsX9XBkfknBeTkKHYu97ltF1kfxwo6-6WVHH9h6upWnrR12U-xWl-e69aHvHFkubRtecKPYC97cEZCZSK8IA_6mFef-30sdPVLkUc1HP0O8M2NFwn6n7gOH1c-ghicqta9uDOnNj9X4P29u6hk266SpxSOpp9Kj5IZwCbsvWuqDDUgvRCmJb1SFVCxvUUP-zw7c3FsLJ1Jg2U_YIw1BwIsKfRoj7MjohjF8F2XLRbXBrkyMLqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور بعضی از خرید‌های ساده به‌جای این که پولدار نشون‌مون بده، تبدیل به یک سقوط مالی میشه؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/679698" target="_blank">📅 16:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679697">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بورس کالای ایران: ساعت پایان معاملات بازارهای مالی بورس کالا به ۱۸ افزایش یافت
.
🔹
عضو هیات رئیسه مجلس از وصول ۱۰ سوال نمایندگان از وزرای آموزش‌وپرورش و راه‌وشهرسازی خبر داد.
🔹
پاکستان: هدف پیمان دفاعی جدید، تقویت صلح منطقه‌ای است.
🔹
انتشار اطلاعیه ثبت‌نام آزمون دفتریاری ۱۴۰۵ در سایت سنجش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/679697" target="_blank">📅 15:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679696">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
۴۲ کشته و زخمی در حملات ارتش یمن به بندر المخا
🔹
منابع خبری یمن از کشته شدن ۷ نفر و زخمی شدن ۳۵ نفر دیگر در حملات امروز نیروهای مسلح یمن به بندر المخا واقع در استان تعز خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/679696" target="_blank">📅 15:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679695">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
چرا سقف ۲۵درصدی افزایش اجاره رعایت نمی‌شود؟/ مالک می‌گوید تورم ۶۰درصد است، چرا اجاره ۲۵درصد افزایش پیدا کند
علیرضا نوین، عضو کمیسیون عمران مجلس:
🔹
افزایش سقف ۲۵ درصدی اجاره‌بها مشخص است که رعایت نشده و در عمل مالکان آن را اجرا نمی‌کند.
🔹
باید با متخلفان برخورد جدی شود. اگر ۱۰ متخلف را شناسایی کنیم و محل فعالیت آنها را ببندیم و حتی روی آن پلاکارد بزنیم که این واحد به دلیل گران‌فروشی یا اجرا نکردن مصوبه دولت پلمب شده است، دیگران نیز متوجه می‌شوند که قانون باید اجرا شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/679695" target="_blank">📅 15:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679694">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
رئیس اتاق تعاون ایران:
بخشی از سود سهام عدالت ۱۴۰۴ تا هفته دولت واریز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/679694" target="_blank">📅 15:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679693">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY9aF2x4i1WDyzFS_7bd1KDk4bEw5TnsDEnJ-8PP9_sW_2vX8gHL1QakW7MRsduGCu279hH7ElMNETMIZzEZFmwz8_c2YpljgsSRYGVnoIs09YAbR5Y_u98paZsIkRkxSpaXS-eSaNHlD7KfKdAb4IwBSE6hlIi8hbdMUeTbyLsJi0G7ngu-B3E3eLz9K-ICwXPODMYfKRnK262_safqpcJo76zvOSoG6LE8MYPa7PQu0m7ebmF_8HncyldjGCoHUiix-tmDDSenc43xsMrG_KCLJWp9VHSKZv1Gp-AzmFF0cfRsbD5xXJmtAp97AvbpXAgBV1vAgErD79le038jEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک سوءبرداشت تکراری از ردیف تبلیغات در صورت‌های مالی فولاد مبارکه
🔹
هر ساله با انتشار صورت‌های مالی شرکت‌های بورسی در سامانه کدال جهت ارائه به مجامع عمومی، موجی از تحلیل‌ها از زبان برخی تحلیل گران بازار سرمایه و در رسانه‌های مختلف شکل می‌گیرد.
🔹
یکی از بندهایی که همواره و در سال‌های گذشته نیز مورد سوءبرداشت رسانه‌ای قرار گرفته و این ابهام درباره آن هرساله تکرار می‌شود، ردیف هزینه‌های تبلیغات است. تحلیل‌گران شتاب‌زده معمولاً کل این ارقام را به پای هزینه‌های جاری روابط عمومی و رپورتاژ رسانه و یا تبلیغات رسانه ای می‌نویسند، در حالی که ساختار تفکیکی این سرفصل‌ها ماهیت کاملاً متفاوتی دارد.
🔹
بخش عمده‌ای از آنچه در گزارش‌های مالی گروه فولاد مبارکه به عنوان هزینه تبلیغاتی ثبت می‌شود، در واقع بودجه باشگاه سپاهان است. این بودجه در قالب یک قرارداد رسمی تبلیغاتی ثبت می گردد و ماهیت آن با هزینه‌های مرسوم تبلیغات تجاری کاملاً متفاوت است.
irasin.ir/xKCh
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/679693" target="_blank">📅 15:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679692">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
الجزیره به نقل از جی‌دی‌ونس: آمریکا به توافقی درمورد تنگه هرمز نزدیک شده است که ممکن است در روزهای آینده منعقد شود
🔹
نورالدین بوزیان، خبرنگار شبکه الجزیره در واشنگتن، به نقل از معاون رئیس‌جمهور آمریکا، گزارش داد که ایالات متحده به توافقی دربارهٔ تنگه هرمز نزدیک شده است که ممکن است در روزهای آینده منعقد شود./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/679692" target="_blank">📅 15:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679691">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
خاموشی‌ها تا دو هفته آینده به حداقل می‌رسد
رجبی‌مشهدی، معاون برق و انرژی وزارت نیرو:
🔹
خاموشی‌ها­ در مناطق عادی ۲ ساعت یا کمتر است و مناطق گرمسیر به دلیل شرایط خاص، از تخفیفات ویژه برخوردار هستند.
🔹
عمده مشکلات ما برای تأمین برق در ساعت ۱۱ تا ۱۸ است که ساعت ۱۵ تا ۱۸ اوج بار را تشکیل می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/679691" target="_blank">📅 15:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679690">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
دو انفجار مهیب شهر تعز را لرزاند
🔹
منابع خبری یمن از وقوع دو انفجار شدید در شهر تعز، واقع در جنوب غربی این کشور، خبر دادند. تاکنون گزارشی درباره ماهیت، محل دقیق و تلفات احتمالی این انفجارها منتشر نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/679690" target="_blank">📅 15:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679689">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: تهران برای بازگشایی تنگه هرمز ۵ شرط کلیدی تعیین کرد
وال‌استریت ژورنال:
🔹
ترامپ امیدوار بود که بازگشایی تنگه هرمز به او امکان دهد پیروزی را اعلام کند و درگیری با ایران را به پایان برساند، حتی بدون دستیابی به یک توافق هسته‌ای. اما تهران خواسته‌های خود را به شدت افزایش داده است.
🔹
ایران خواهان خروج نیروهای آمریکایی از منطقه، لغو محاصره دریایی، برداشتن تحریم‌ها، آزادسازی دارایی‌های مسدود شده و دریافت میلیاردها دلار غرامت جنگی پیش از بازگشایی کامل تنگه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/679689" target="_blank">📅 15:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679688">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGAahADD6aegGinVZkaA3TKyY_1aO9CYZ2LdAfBa2cVIAJA6qeqngWkwLNpVrabBPMsxfcYiQnmkqGWq1236VdJJxG2ehHjq6jmjsYB6rpDVKVGMavPdHoaSPEHWfMrytwJ8LL46QPHu09tqkEqS8BYK_MF8YYYmkkFL7wfiuDn8cJqZhvDIKoEi5UDMEmATLBDQcdz1N1QPB3rn5wn8JzgK9x6pYkJn7Yth_4HbdeRoQVrb4gU_FCfq-QNnrGkUoNGbaTdPj07Lc5SOC9fRKmdNNTUbHCLL0T6FxNwpbc0uNiysBx6u8yoV2mPw3F5hu_qtCpBmMqPLiINNnS2q1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضاییان در فهرست پرسپولیس جایی ندارد
🔹
در روزهای گذشته شایعاتی دربارهٔ احتمال بازگشت رامین رضاییان به پرسپولیس مطرح شده؛ اما پیگیری‌ها نشان می‌دهد این بازیکن در فهرست خرید سرخ‌پوشان قرار نداشته و باشگاه پرسپولیس برنامه‌ای برای جذب او ندارد./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/679688" target="_blank">📅 15:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679687">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCeUeL4aYEwsIhEkDTAkZVJW_t2z052LtDeG4Y4dcNFEpKwenoLFwEcTyyjTByRo63XJhT61qIsGHcqda_FqporaDVCxHP_8r1mqJUEAPyDKMYZ9cwyXzZi0IvfsoIa5A_l8P-H6yWaZ94X3cHdA4W9mjGLOAbyI0X5kxxTM4jAoYaez-sVrsOvq_kZm56J5HMrJ1HZP6pAb6DiV1BCf_4UGanjdVdVGfd59z6zUC1bnd0BUVe8fI3T17Xhw5AMoqYqLE3uM9YWmuRD-bwxXzA7dc4-btiunPhuhTxCT0y_vGgJJLO2zBT4Ss808mfi9DImn5g-QDJv1401qSTvBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
‏
استوری بهنوش بختیاری: آمریکا در هیچ مقطعی از زمان، دوست هیچ کشور صاحب تمدنی مثل ایران نبوده، نیست و نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/679687" target="_blank">📅 15:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679686">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
نتانیاهو: تا زمانی که نخست‌وزیرم، کشور فلسطینی در غزه و کرانه باختری تشکیل نخواهد شد
🔹
نخست‌وزیر رژیم صهیونیستی، با اعلام موضعی صریح درباره آینده غزه و کرانه باختری، هرگونه تشکیل کشور فلسطینی را در زمان نخست‌وزیری خود به طور کامل رد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/679686" target="_blank">📅 14:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679685">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1NELEV8tUCLLHRRuZb7UpjA_qDqGSLGMKmZN-ZuQTdG0OyohZsiQgrVqFd2s8Ha2IjaR6_gVfBbt7CFCwHpc-zB6_VpSL6jWXTH6r-CVtQ728fZDeIFx9_nFJu6hPIBx5nFHt-kzGWOJJIqeRt28dA3BBZFxU_TOzuGrgo3Fv_oFjwIRDzEEKs125jwz0QPvvAGmaGKB9QVA3Uq2geGrpiwZwEb5pA7V2uN3-jaqRKStB7--5PdsgU5a7Mf_hFXNPuJYaTWXRlMRDO4Pad_kCMCvjjo-soIyX6kmpHRC3BTNK6nsGSVoA-fOkj4whdqUuJq73urPGxwgjSXyuZpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۲
🔹
سپرده‌های بانک کشاورزی طی سه سال گذشته ۳ برابر شد
🔻
حجم منابع بانک کشاورزی با افزایش ۵.۵ برابری طی ۵ سال اخیر، از ۱۷۹ همت در تیرماه سال ۱۴۰۰ به ۹۸۳ همت در تیرماه ۱۴۰۵ رسید که ظرفیت این بانک را برای ایفای نقش مؤثرتر در حمایت از امنیت غذایی کشور با تأمین مالی بخش‌های مولد، به‌ویژه کشاورزی و صنایع غذایی تقویت کرده است.
🔻
شتاب رشد منابع این بانک در سه سال اخیر، به طور محسوسی افزایش یافته و از ۳۰۲ همت در تیر ۱۴۰۲ به ۹۸۳ همت در تیر ۱۴۰۵ رسیده که بیانگر افزایش ۶۸۱ همتی و رشد بیش از سه برابری سپرده‌های بانک در این بازه زمانی است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/679685" target="_blank">📅 14:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679681">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bd56a25b.mp4?token=uUZJAR__eB3L5kh8I-QHbpxomRfAxF0rkmxh-kUhCO0AHecaklcswAgjbM9fM_uzs8LSM8uhvgZEuhy4rvB3IZi4x_ZKtgUid4Me8uWP6OQ6Mtj7YvWtxCpV5nJuPya6Upc-PyN2qGZqu-8-H6Yghu-ReViRBKnfsA-Uz5dqf612ihihVNMB9EmG37XBV9NL0ybuc-jBadEYzycFejS4VIMWv-ONUZnp4XfC6BLsst0_DefnTB6jFFyzsFdfReGIZkPgNeFBcT89ElgTUQuxYDhlXu_rUoU1y2gOkwgt1inc9h5akqhCcRQ7RyOvotTOYGTnrT2QX7XlkNFzYBnNz1wWLiaAPyUCwNbbdvfPdObvz6O-9JVzTYwNFAjkqbm4ggmAGu7a1IZK-3fjDd4_6OqOcw5g73UQn96SNS-ETT0Lzr1Zs4_VWtMqnH4Z-Y0bzxV8bwYxEGm_5Eb4OL5RB_yXI2uUs1CN2CzC8Bm-6cvFwg2jfyRsXv_PwPXL_AOwGCVqIQ-jRTFSUjElCH7EwUqYM99UY-nuBb_GwGBoUagd_2Q0axfrnUPyvrU9eBnIFhwn6Qu1_Ct8XSi1sL87ELU_Mm51yVVQwtLnQCmLryniUIq8ecPtb-b_LZVktJ-M5M5VymLSU2ol9eTNMrSzS1zNfo2KVpo8hEm0tJ4cs1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bd56a25b.mp4?token=uUZJAR__eB3L5kh8I-QHbpxomRfAxF0rkmxh-kUhCO0AHecaklcswAgjbM9fM_uzs8LSM8uhvgZEuhy4rvB3IZi4x_ZKtgUid4Me8uWP6OQ6Mtj7YvWtxCpV5nJuPya6Upc-PyN2qGZqu-8-H6Yghu-ReViRBKnfsA-Uz5dqf612ihihVNMB9EmG37XBV9NL0ybuc-jBadEYzycFejS4VIMWv-ONUZnp4XfC6BLsst0_DefnTB6jFFyzsFdfReGIZkPgNeFBcT89ElgTUQuxYDhlXu_rUoU1y2gOkwgt1inc9h5akqhCcRQ7RyOvotTOYGTnrT2QX7XlkNFzYBnNz1wWLiaAPyUCwNbbdvfPdObvz6O-9JVzTYwNFAjkqbm4ggmAGu7a1IZK-3fjDd4_6OqOcw5g73UQn96SNS-ETT0Lzr1Zs4_VWtMqnH4Z-Y0bzxV8bwYxEGm_5Eb4OL5RB_yXI2uUs1CN2CzC8Bm-6cvFwg2jfyRsXv_PwPXL_AOwGCVqIQ-jRTFSUjElCH7EwUqYM99UY-nuBb_GwGBoUagd_2Q0axfrnUPyvrU9eBnIFhwn6Qu1_Ct8XSi1sL87ELU_Mm51yVVQwtLnQCmLryniUIq8ecPtb-b_LZVktJ-M5M5VymLSU2ol9eTNMrSzS1zNfo2KVpo8hEm0tJ4cs1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرزند شهید لاریجانی: شهید لاریجانی درباره حوادث ۱۴۰۰ [ رد صلاحیت] گفتند: «آبروی هر کسی متاعی است که خدا به او می‌دهد و ما باید وظیفه خودمان را انجام بدهیم اگر وظیفه را درست انجام بدهیم خدا می‌داند کی و کجا آبروی ما را تدارک کند»
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/679681" target="_blank">📅 14:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679680">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaAH7EGaSzhwr2iNuxq8mPkoiHNycr84bUYxUJwocofoF6wo9jRFiKXlXqU7NB6Fe4qxDBPk1k8MaOw6JBAapbz9KBr_SPYlHKh0bfM_85NhZzZQ1GF0gxmaVyqSe_xG4tWZ5TcOjykD9UHej4vYVlPqd4WOvMSOeGqf923leeuLb0uNBrlIqTdrh-Q37LsDAR5S_KBxMYo52deSSfqQX1DRyscQhNlyc256gVNuqbcoXaX4QgufU_q45KONsTrvL5X3c_lUu5qJCCyDDWsGqR5APsySCPcgopA0ECS8C820egqJIwY638ayJX1bR2YMc03Hc46b4QLNK3PqdSr1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قریشی: تصاویر حضور رهبر معظم انقلاب در جلسات با فرماندهان منتشر می‌شود
جانشین سازمان بسیج مستضعفین:
🔹
تصاویر و مستنداتی که در آینده از حضور رهبر معزز و فرمانده کل قوا حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای (حفظه‌الله) در میان مردم و کوچه و خیابان و جلسات با فرماندهان نیروهای مسلح منتشر خواهد شد، بار دیگر موجب رسوایی دشمنان و بدخواهان ملت ایران خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/679680" target="_blank">📅 14:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679679">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcKP7evuI99gs1KwAAqPgW8DVmvn7E4hDJfzVvtv_VE0XQR3W7IYwo0XlwMFjoZ_e1GUnrl6xZUUiBvo0D1s3oIPCs5gblLue2Q3gLmPOxTP77wRblSbKs0Y-XHy_8w5qyTBze_uQleBv55WeHg3m2xuvi3dE0tawuwvcP9Xwo_KpPpeYaOSMcjSMU8-8ijoSPmDTMctt8Csv2QzYPElvJGRJD_XQJJs5MVdyijpT0YnLzEL02GCjwWpr_5ra068t4EuialrZYqqVMKPMB54byIvcwBD0EGV1OaXDi4ErWAtS2YIKmPTp4G-_CyAkV5fyR9u5AO0a1gDA-Y0qnNaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
۳ ماه استفاده رایگان از سوپرپوز بارکد!
اگه دنبال یک راه ساده‌تر برای مدیریت فروشگاهت هستی، سوپرپوز بارکد می‌تونه مدیریت فروش و صندوق رو برات راحت‌تر و دقیق‌تر کنه.
🧾
📊
❇️
حالا می‌تونی با یک پیشنهاد ویژه،
۳ ماه رایگان از سوپرپوز بارکد استفاده کنی.
⏰
برای استفاده از این پیشنهاد فقط تا
۲۴ مرداد
فرصت داری.
📩
برای اطلاعات بیشتر، روی لینک زیر کلیک کن!
https://Snappbarcode.com/product/superpos</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/679679" target="_blank">📅 14:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679678">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما بزرگ‌ترین آسیب استفاده بیش از حد از شبکه‌های اجتماعی چیست؟</h4>
<ul>
<li>✓ افت تمرکز</li>
<li>✓ اختلال در خواب</li>
<li>✓ اخبار زرد و شایعات</li>
<li>✓ آسیب به ارتباطات حضوری</li>
<li>✓ کاهش بهره‌وری</li>
<li>✓ سایر</li>
</ul>
</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/679678" target="_blank">📅 14:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679676">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcacf87c4c.mp4?token=vaYpcNabbFNi5vLBL0t87GdE4J5PwFrkPe9hy1gi-iGrBX1O2fD4klyj3LhlNOkIX-YmPXCFj2m3vvA-v5y7_bvwuDSHM_1oqg3o2OcNReri9NiNWGCz7F5kkWezMyEu8sVaG8KmuvuH7jDv6qkZwAMk8ZJqVdL2z4Yl3P0yiH3hoZDm7bj_RnjYWnIfIH1mkDfKZy-ePl-1IK7QaXc6Xhg-YMsYMrscLOKApD2crUKh6Ni5BpognsYRZgN6gPR9QRNzmQCN9AHPaau5-nMq1dGdJmJD9MvEBAZobnJIZeXZYidg8wLVuGGS4TRaAeXio7j_QEaupZaUKE4DECZqPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcacf87c4c.mp4?token=vaYpcNabbFNi5vLBL0t87GdE4J5PwFrkPe9hy1gi-iGrBX1O2fD4klyj3LhlNOkIX-YmPXCFj2m3vvA-v5y7_bvwuDSHM_1oqg3o2OcNReri9NiNWGCz7F5kkWezMyEu8sVaG8KmuvuH7jDv6qkZwAMk8ZJqVdL2z4Yl3P0yiH3hoZDm7bj_RnjYWnIfIH1mkDfKZy-ePl-1IK7QaXc6Xhg-YMsYMrscLOKApD2crUKh6Ni5BpognsYRZgN6gPR9QRNzmQCN9AHPaau5-nMq1dGdJmJD9MvEBAZobnJIZeXZYidg8wLVuGGS4TRaAeXio7j_QEaupZaUKE4DECZqPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: دشمن آدم‌هایی را ترور می‌کند که گره‌گشا هستند
🔹
برادران نظامی در سپاه و ارتش کاری کردند کارستان؛ با ایستادن مقابل دو قدرت اتمی، دنیا را به حیرت وادار کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/679676" target="_blank">📅 14:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679674">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/560ac12c6d.mp4?token=V4Fsq01Pv_mqesKZp3gz7bOkpceDD6oNuSdKovue88o08vz99PHmPLkFbk5FAKpdzJuNHKRI40tG_yi7hewSVgpo2gxq7RM-dy0ZBvT5qUQELNvHue9GkRMNiWIX_Z6ajPsYwZMf6fPF603jAutMksbCFyAcjFsNc_mlEnpqOtsFilzOX_MsBGoCbGAv9UQQ-E_rwXq2meTmACEzpjlg2TTEDlCuY--hMFCFtL4MPDaN1i8QKYiz0szd5Tr6eZnfRNoKUiUbFe5Bq85Y4NVbfTN72SWIKmaxJ98c7qiEiErTND4Dco3ufFCFfWFf2VYsyWzn4mT__kMnh4QBlqNcQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/560ac12c6d.mp4?token=V4Fsq01Pv_mqesKZp3gz7bOkpceDD6oNuSdKovue88o08vz99PHmPLkFbk5FAKpdzJuNHKRI40tG_yi7hewSVgpo2gxq7RM-dy0ZBvT5qUQELNvHue9GkRMNiWIX_Z6ajPsYwZMf6fPF603jAutMksbCFyAcjFsNc_mlEnpqOtsFilzOX_MsBGoCbGAv9UQQ-E_rwXq2meTmACEzpjlg2TTEDlCuY--hMFCFtL4MPDaN1i8QKYiz0szd5Tr6eZnfRNoKUiUbFe5Bq85Y4NVbfTN72SWIKmaxJ98c7qiEiErTND4Dco3ufFCFfWFf2VYsyWzn4mT__kMnh4QBlqNcQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرشایمر، استاد مشهور روابط بین‌الملل:
ترامپ فهمیده امکان پیروزی در جنگ علیه ایران وجود ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/679674" target="_blank">📅 14:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679673">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f7a472772.mp4?token=dISdG4DFEttwUbPytxVcj5O85O0JbdX_Whpqwwt-7pvV6-nz_E3_fftll9Z_kFwU9VYoUasyNtqcVyO86iH3YW4y3WV7mAHOxxdYn6KKNRFogBLgMhhOyKW3YM-u8QxjrSz9kfNltxbykJOz4X9q_nj8OPC5rIh-H-PGCLGzhIZ7SAdsFNDA-kZz8K4N84dSiNjNh3hoE_V4v9cTGjyJjN8Cu1eeNExvwoH0eCg3JWhxdqbiW3XR6pPHVODLx1G8P6MWh-N_dvgkwWkzgrnYDpnX9O-HwvR0gBCY7oWHAlX9ajzsVaWGsV-OSeqdGgj9y0q-nJN8PY0SlhGHn742UYS-MpgnJM1HyiYOmccmpf8Fz4WdQIsDXC8uDx8NNstAri4ixA0oGYnAZ8djV0B5ujKyv7-GwEnZsiZp3VUR0Wlyqa5vtOxHf0HiS9xKhMOg0ThwWRI9MKq1XiHf1ZcKEclRvWkXQvgte9uywhW1V41lJ_0jxOEheTWkheme0xoKuK7buYoKDg5wMjzjh_xibnEkb9GGbjBc3zGDARwQ-VqMitiqxcs5hnjNs9NCVXNrUFxQ9LjQYqqVd57mtRHWgRUOKS89gyhCumboJYtJUqGEge0VoHClb-XTkRQVDDFCPdHyF6IaP2vhYeX1Wmh8S_5K5AR1JtwBQ0QhiLzuNTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f7a472772.mp4?token=dISdG4DFEttwUbPytxVcj5O85O0JbdX_Whpqwwt-7pvV6-nz_E3_fftll9Z_kFwU9VYoUasyNtqcVyO86iH3YW4y3WV7mAHOxxdYn6KKNRFogBLgMhhOyKW3YM-u8QxjrSz9kfNltxbykJOz4X9q_nj8OPC5rIh-H-PGCLGzhIZ7SAdsFNDA-kZz8K4N84dSiNjNh3hoE_V4v9cTGjyJjN8Cu1eeNExvwoH0eCg3JWhxdqbiW3XR6pPHVODLx1G8P6MWh-N_dvgkwWkzgrnYDpnX9O-HwvR0gBCY7oWHAlX9ajzsVaWGsV-OSeqdGgj9y0q-nJN8PY0SlhGHn742UYS-MpgnJM1HyiYOmccmpf8Fz4WdQIsDXC8uDx8NNstAri4ixA0oGYnAZ8djV0B5ujKyv7-GwEnZsiZp3VUR0Wlyqa5vtOxHf0HiS9xKhMOg0ThwWRI9MKq1XiHf1ZcKEclRvWkXQvgte9uywhW1V41lJ_0jxOEheTWkheme0xoKuK7buYoKDg5wMjzjh_xibnEkb9GGbjBc3zGDARwQ-VqMitiqxcs5hnjNs9NCVXNrUFxQ9LjQYqqVd57mtRHWgRUOKS89gyhCumboJYtJUqGEge0VoHClb-XTkRQVDDFCPdHyF6IaP2vhYeX1Wmh8S_5K5AR1JtwBQ0QhiLzuNTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وششم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ دو بانو که هر دو بزرگوار در هنگام عمل جراحی زایمان روح از جسم‌شان جدا شده و موارد ماورائی از جمله جسم بلوری زنده، هم صحبتی با نوزاد در حال متولد شدن و رفتن به مکان بهشتی و رویت درختان رنگارنگ و آب روان گوارا را مشاهده و لمس کرده اما به خاطر وابستگی به فرزند، بازگشت به زندگی دنیوی را از خداوند طلب می‌کنند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود
#تجربه‌گران
: نفیسه متعبد/ منیره محمدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/679673" target="_blank">📅 14:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679672">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
دیدار و گفتگوی رئیس‌جمهور با رهبر معظم انقلاب درباره مسائل اقتصادی و نظامی کشور
🔹
مسعود پزشکیان همزمان با شروع سومین سال ریاست‌جمهوری با حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای دیدار و گفتگو کرد.
🔹
در این دیدار به تفصیل درباره مسائل و مشکلات کشور به‌ویژه تأمین نیازهای معیشتی مردم، شرایط موجود جنگ تحمیلی سوم و آینده پیش‌رو، تحولات حوزه نظامی، راهکارهای ناظر به تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی» و همچنین تعامل اقتصادی با طرف‌های خارجی تبادل نظر شد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/679672" target="_blank">📅 14:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679670">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13d19fe1d8.mp4?token=b0i1vPtBLogPGLGc4zTi5bpx5gIkUVwcNNP23U1Evm0DqD89lworBoWcvVNJCoV9YmSWXxduYhYgzw5wtjG1f358tRigV-ZE1pWPlstNNsIhGt04JoMNKzNiPuxTi5LMoPN-XZLyEikAKKrIXcw6v0SWdE5naNB3A8ABSFQhUj6lIpzzeYm8hgj3-MVN17Vuvl0zbWI1Nc-r6y9VHTt9PkGqFc_WOfupPOZve4DC4gYMLtUEAadH88qQmVyYTMIYY2_7tjIs10uT5K9jj_FrSd8BohvVi5uN_lbheLUpcHC__9zJzmYiS7094-AHb96QF1Htl4_JjVnhC3pd-aCQgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13d19fe1d8.mp4?token=b0i1vPtBLogPGLGc4zTi5bpx5gIkUVwcNNP23U1Evm0DqD89lworBoWcvVNJCoV9YmSWXxduYhYgzw5wtjG1f358tRigV-ZE1pWPlstNNsIhGt04JoMNKzNiPuxTi5LMoPN-XZLyEikAKKrIXcw6v0SWdE5naNB3A8ABSFQhUj6lIpzzeYm8hgj3-MVN17Vuvl0zbWI1Nc-r6y9VHTt9PkGqFc_WOfupPOZve4DC4gYMLtUEAadH88qQmVyYTMIYY2_7tjIs10uT5K9jj_FrSd8BohvVi5uN_lbheLUpcHC__9zJzmYiS7094-AHb96QF1Htl4_JjVnhC3pd-aCQgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با هر رنگ شلوار چه رنگ لباسی ست کنیم؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/679670" target="_blank">📅 14:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6880194a73.mp4?token=vrvtqV1CUTMLLtst4nVv0rUNHaYL8kGyC525KnsTyXD6YtI_A77bN0b539JMNFiQvchCeik_CnqLWKVAReG7reIBJ5CclVGOIuSfvUpAT5qrFa99CNUCB97w0Z6lUYCi5hKsHynDTScAOvB6L2p739qSNSP-9kA374MWZ8gtHYfAPNa378Nfsy6ibxRuJS2SnH7bCqTiZVFt3bwoac7h38xPblgfYEMcTHuWo3oU9Z-eX7QueGllB0XX4xXb8gL03a9IV1Ecv6crOxE1RxB3E-RKfNzuECT1fulIxs7zE5JvjnZOOduzek-3kbm9_aQJvF2Hzzo6qSrk-vs9YyHVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6880194a73.mp4?token=vrvtqV1CUTMLLtst4nVv0rUNHaYL8kGyC525KnsTyXD6YtI_A77bN0b539JMNFiQvchCeik_CnqLWKVAReG7reIBJ5CclVGOIuSfvUpAT5qrFa99CNUCB97w0Z6lUYCi5hKsHynDTScAOvB6L2p739qSNSP-9kA374MWZ8gtHYfAPNa378Nfsy6ibxRuJS2SnH7bCqTiZVFt3bwoac7h38xPblgfYEMcTHuWo3oU9Z-eX7QueGllB0XX4xXb8gL03a9IV1Ecv6crOxE1RxB3E-RKfNzuECT1fulIxs7zE5JvjnZOOduzek-3kbm9_aQJvF2Hzzo6qSrk-vs9YyHVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیکنی از باشگاه برزیلی کوریتیبا هنگام شادی پس از گل، به داخل تونل رختکن افتاد
🔹
پس از این حادثه، گل مردود اعلام شد و بازیکن به دلیل مصدومیت تعویض شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/679668" target="_blank">📅 13:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679664">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFoZiW3wIfZPfsaxeGhbfn4LZdfsOG3-5yd-wAiKBOZc_VI3sDnWlZd7HsNDhGL4Zuf4T9v2kWWTvHlGe7ALI6tNCSPYuohA1Cp56mGG70iJ7QaJQjvr7eQ3CgKZ65SwvQ8BGTM8Q_JCSM2wBHc1f8Rme3ltazmYAs_8zaHQLZKBgHV1FxJUAtra1pI2P7Y_A38PxnF31W5RumtzsmlORbhsgGIixvCiNrX5EkFHyQHMvtey0yhWOlwcUSPP3WIhtVbMHKIVlCNMKJrePIBqRnKS94DiO8KcfMxJ757DY1QLBxAmIzpMGCb-VHPLww2K839Pglr_9mfgckMpKrgZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۸ مرداد ۱۴۰۵؛ ساعت ۱۳:۲۵
🔹
بازار ارز امروز تقریبا در سکون سپری شد؛ قیمت دلار که روز گذشته نوسانی بود، امروز در پی ابهامات سیاسی و رویکرد محتاطانه معامله‌گران، با تغییر کمی نسبت به روز قبل به ۱۸۶ هزار و ۴۹۰ تومان رسید./ تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/679664" target="_blank">📅 13:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679663">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
توضیحات سخنگوی وزارت کشور درباره پلمب برخی کافه‌ها به دلیل بی‌حجابی
🔹
تغییری در تعلیق قانون حجاب بوجود نیامده است.
🔹
این موارد پلمب در شورای امنیت کشور مطرح می‌شود و در مسیر خود پیگیری می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/679663" target="_blank">📅 13:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679661">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزارت نفت، نهاد ریاست جمهوری را به پرداخت ۱۳۸ هزار میلیارد تومان خسارت محکوم کرد!
🔹
در‌ یکی از کم‌سابقه‌ترین‌ دعواهای حقوقی در دولت، شرکت سرمایه‌گذاری اهداف زیر مجموعه وزارت نفت، نهاد ریاست جمهوری را به پرداخت ۱۳۸ هزار و ۵۶۰ میلیارد تومان خسارت محکوم کرد.
🔹
طبق گزارش سایت دیدبان ایران؛ این دعوی که در شعبه ۹۲ دادگاه عمومی حقوقی مجتمع عدالت قضایی تهران علیه سازمان‌ خصوصی‌سازی و نهاد ریاست جمهوری مورد بررسی قرار گرفته بود ،ششم مرداد منجر به برائت سازمان خصوصی سازی و محکومیت نهاد ریاست جمهوری از سوی این دادگاه شد.
🔹
وزارت نفت به دلیل از بین‌ رفتن وصف مدیریتی خرید بلوکی ۱۲ درصدی شرکت صنایع پتروشیمی خلیج‌فارس ، ناشی از مصوبات بعدی هیئت وزیران که مابقی سهام دولت در «فارس» را هم به صورت بلوکی عرضه کرد ،شکایت کرده بود.
🔹
وزارت نفت (شرکت سرمایه‌گذاری اهداف )تاکید کرده با استناد به وصف مدیریتی این سهام در مزایده سازمان خصوصی‌سازی در آذر‌ ۱۴۰۱ این معامله را انجام داده بود و با مصوبه بعدی دولت در دی ماه همان سال حالا نمی‌تواند برای ۱۲ درصد سهم بلوکی خریداری شده یک عضو هیات مدیره در شرکت صنایع پتروشیمی خلیج‌فارس را از آن خود کند.
🔹
این رأی در مهلت اعلامی قانونی ۲۰ روزه قابلیت تجدیدخواهی دارد و باید دید آیا نهاد ریاست جمهوری این رقم هنگفت را به زیر مجموعه وزارت نفت می‌پردازد یا این دعوی حقوقی وارد فاز جدیدی می‌شود؟/منبع: دیده‌بان ایران
https://www.didbaniran.ir/fa/tiny/news-328534</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/679661" target="_blank">📅 13:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679660">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53546a9df0.mp4?token=XmJmuc9iumVX5AFMbRTAa362pQ_CTdjRCOj4vUToqIMlL3XHsK2zhjmF-myB_j5fB0Juy9p9QjgWj902DXx2T0O7NJga_Ri6KEv6n3LxaebB-fBzwfforZrbP7vSoralCg-WYszysVMkflBileA0bXXQpcYzpinSIwKLSnhaioda2Sd9Tf5sOZMGRobqRMXj5fqXBVNlD-n7j0gI_0-wRocYgG4uRPV7UNRbfS6LDqbEplx3SorH_NHlB1oTYGdxdeVGkK9h76sAJxNnjh7MPIOJcOaLusPo5ZHVljCqokjBeZ-SVUPJ6956IOvrPzUt98ovRXN7RlXPJsSo1InYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53546a9df0.mp4?token=XmJmuc9iumVX5AFMbRTAa362pQ_CTdjRCOj4vUToqIMlL3XHsK2zhjmF-myB_j5fB0Juy9p9QjgWj902DXx2T0O7NJga_Ri6KEv6n3LxaebB-fBzwfforZrbP7vSoralCg-WYszysVMkflBileA0bXXQpcYzpinSIwKLSnhaioda2Sd9Tf5sOZMGRobqRMXj5fqXBVNlD-n7j0gI_0-wRocYgG4uRPV7UNRbfS6LDqbEplx3SorH_NHlB1oTYGdxdeVGkK9h76sAJxNnjh7MPIOJcOaLusPo5ZHVljCqokjBeZ-SVUPJ6956IOvrPzUt98ovRXN7RlXPJsSo1InYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده نیروی زمینی ارتش: پای نظامی آمریکایی به ایران باز شود، آن را قطع می‌کنیم؛ به هرگونه اقدام دشمن، پاسخی قاطع و بازدارنده خواهیم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/679660" target="_blank">📅 13:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679655">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07b738d82.mp4?token=EZaTZY6n0E7NoO5vHmGUHwnJ6FGFRSRV2N5ve19LvGw9gidzK0fZPIXj_j-zX-xFMgKa2kQVp33pMyojIQ0bTL_4COCnCW3OKsRhoI5IY-k9Z78up-5AosDd8DepMRRBG03cJLdKZs4wZA3xihBgV0d0mNZET9uXCNLWExewqHPNiD4MtHMKsVZ16FbmwaU59DHOdVb5BN1BqqULu5F36LTWSjvsqeKBYlCrmZROIGOxkQ-CGx9CRYbyAAdm9hofkIN15tROI0HIcK9k_wj0Mm81H8wB9luK5vjCIa1tVBQw8LFPvC6pK_B4zGZubbJr4Xw19SmL_gmUvG1fvUS4cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07b738d82.mp4?token=EZaTZY6n0E7NoO5vHmGUHwnJ6FGFRSRV2N5ve19LvGw9gidzK0fZPIXj_j-zX-xFMgKa2kQVp33pMyojIQ0bTL_4COCnCW3OKsRhoI5IY-k9Z78up-5AosDd8DepMRRBG03cJLdKZs4wZA3xihBgV0d0mNZET9uXCNLWExewqHPNiD4MtHMKsVZ16FbmwaU59DHOdVb5BN1BqqULu5F36LTWSjvsqeKBYlCrmZROIGOxkQ-CGx9CRYbyAAdm9hofkIN15tROI0HIcK9k_wj0Mm81H8wB9luK5vjCIa1tVBQw8LFPvC6pK_B4zGZubbJr4Xw19SmL_gmUvG1fvUS4cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه وحشتناک حین مسابقات سوارکاری در قرقیزستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/679655" target="_blank">📅 13:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679652">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/672ca2289c.mp4?token=vVIo4VHszlmglr746oe0YcrNv5RwU36c5x4yx_tdAQsamCsC_Kj_BxI97IZDBhybotILIg_zCRLO5TOVnZCnxa-RwsHTylN2mpgyVVdZL7aMz4yL8yegXKEIJH_a4yTs1kx5s2Mp-1siyLyWCx7ONRGXlp1IJidz8QdDplP8SGJH34W4iFa16-Dg6zCafTdZnsqGm3L8jz0AQdfXvYaY3KL2_yNXoVVhtcDFHOOcQj-vVAziqXrCUuBa_-K_eFrWUUrbXdpMGlPigv61-10UBQ4FZgENyc0zAKyrx-hbR_IxZi8CmYJy6nIIU--FxqaCKYQmNdpSPXMo2HZrLQxYTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/672ca2289c.mp4?token=vVIo4VHszlmglr746oe0YcrNv5RwU36c5x4yx_tdAQsamCsC_Kj_BxI97IZDBhybotILIg_zCRLO5TOVnZCnxa-RwsHTylN2mpgyVVdZL7aMz4yL8yegXKEIJH_a4yTs1kx5s2Mp-1siyLyWCx7ONRGXlp1IJidz8QdDplP8SGJH34W4iFa16-Dg6zCafTdZnsqGm3L8jz0AQdfXvYaY3KL2_yNXoVVhtcDFHOOcQj-vVAziqXrCUuBa_-K_eFrWUUrbXdpMGlPigv61-10UBQ4FZgENyc0zAKyrx-hbR_IxZi8CmYJy6nIIU--FxqaCKYQmNdpSPXMo2HZrLQxYTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنرنمایی آهن و الگوریتم در فنجان قهوه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/679652" target="_blank">📅 13:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679651">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7cf5c281.mp4?token=IXj-FaEGkyYLnyUZlURM-rJrm4633VuNErlME75V9zUqqMA8KHGQEA9uzfasXRjE7qj4Hngw1zNY_t-7khfAxoPyOFWyorhO0zGroUYDYuW-tYnMcWlEWomxJTMKNq1grnmDyuybBbhHxfMFbvX_15zLDceLk5uNqaUvpqFR-gbWd3kOHwmpZmIhtAN3NqOIVYYJfzVdF1xJzd9iYwnN8oAaQYFbuMLBCkvEpvI0GHKT4JFpj7LbOpvAceplQ6LYaAgIjUCI64-j1rBkrC_iOTVir6jjV1jeNkK4kT5exJBrJfrTGUZG8l1eduiiI6Ds1Ew3xrfeJgoQjvlof8vHxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7cf5c281.mp4?token=IXj-FaEGkyYLnyUZlURM-rJrm4633VuNErlME75V9zUqqMA8KHGQEA9uzfasXRjE7qj4Hngw1zNY_t-7khfAxoPyOFWyorhO0zGroUYDYuW-tYnMcWlEWomxJTMKNq1grnmDyuybBbhHxfMFbvX_15zLDceLk5uNqaUvpqFR-gbWd3kOHwmpZmIhtAN3NqOIVYYJfzVdF1xJzd9iYwnN8oAaQYFbuMLBCkvEpvI0GHKT4JFpj7LbOpvAceplQ6LYaAgIjUCI64-j1rBkrC_iOTVir6jjV1jeNkK4kT5exJBrJfrTGUZG8l1eduiiI6Ds1Ew3xrfeJgoQjvlof8vHxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرزند شهید لاریجانی: شهید لاریجانی درباره حوادث ۱۴۰۰ [ رد صلاحیت] گفتند: «آبروی هر کسی متاعی است که خدا به او می‌دهد و ما باید وظیفه خودمان را انجام بدهیم اگر وظیفه را درست انجام بدهیم خدا می‌داند کی و کجا آبروی ما را تدارک کند
»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/679651" target="_blank">📅 12:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679649">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f3dde333.mp4?token=Dsisq19lh0-nbFUPZjEuTetSgTjhIVdAGCwF0TVgPjHRD9rodauMlq0OrBVW_Lr6acPKo4_n240creB5fT3mMOJ3xuNAGRnXG90KBzAEkGJHolU6iXxgRgxOoJn8JfYoRNIbeX4uj9jXquuJs1eXAQY9ZGvvAaWJLezGBPDD4Ck_FKK1a8sRzxhEMlhX28YgYkLrkitfcExpA1LQn8UrLxf_G4PXu-OpYHp6_MQNFHb3cEWSUK0Oj6y3PMkSaH-9WamZ7ugPqW9EzIQLrn5nvl7ER_Z6wRpOVugibwERmKWsu1efIv4rzrs2xwFurFL5xd9jPUYDcdvo9EOnJlErTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f3dde333.mp4?token=Dsisq19lh0-nbFUPZjEuTetSgTjhIVdAGCwF0TVgPjHRD9rodauMlq0OrBVW_Lr6acPKo4_n240creB5fT3mMOJ3xuNAGRnXG90KBzAEkGJHolU6iXxgRgxOoJn8JfYoRNIbeX4uj9jXquuJs1eXAQY9ZGvvAaWJLezGBPDD4Ck_FKK1a8sRzxhEMlhX28YgYkLrkitfcExpA1LQn8UrLxf_G4PXu-OpYHp6_MQNFHb3cEWSUK0Oj6y3PMkSaH-9WamZ7ugPqW9EzIQLrn5nvl7ER_Z6wRpOVugibwERmKWsu1efIv4rzrs2xwFurFL5xd9jPUYDcdvo9EOnJlErTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از سرگرمی‌های تابستان برای بچه‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/679649" target="_blank">📅 12:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679648">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمرکز اطلاع رسانی بانک صنعت و معدن</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoXSO7E1ETtP5VL9RS0ABopTextNtRaL4LY4C6Fm7Dp8tgLWdba5h_lpHGkT1mZh8NZmff7paMKwupX4_ePF1qQtVWDZkD0_KBDvMqnS-Hopb3iwn6uCmuRb3W3P302iQIIhn42W-bR9OFZyTUNSGGIX4h5so2NmOl0a1A2HhtJW7cC4Hz7nEuAxkxichC7W0IM5L-3Sys9RZuIVJE191MVTL15aAknWeI3D5ptj0R8FRvcOqy0Ak4NS2dueGTIsCx2MjFamz7C9TzflEHnI0mwck-OIw6muZT4VFTaT4VWz_KbvzvZTd3GG8zUspey2VZBo97uayJBAjmZ4Zd1sxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بانک صنعت و معدن؛ پیشران تأمین مالی صنایع راهبردی و توسعه تولید کشور
🔹
بانک صنعت و معدن با تأمین مالی هدفمند در صنایع پیشران و زیرساختی، نقش مؤثری در توسعه تولید، تکمیل زنجیره ارزش و ایجاد اشتغال پایدار ایفا کرده است.
▫️
بیش از ۱۳.۲ میلیارد یورو تأمین مالی ارزی
▫️
بیش از ۲.۵۹۲ هزار میلیارد ریال تأمین مالی ریالی
▫️
ایجاد حدود ۹۷ هزار فرصت شغلی مستقیم
▫️
این حمایت‌ها طیف گسترده‌ای از صنایع از جمله نفت، گاز و پتروشیمی، فولاد، نیروگاهی، صنایع شیمیایی، غذایی، دارویی، خودرو، ساختمان و صنایع فلزی و پایین‌دستی را دربر گرفته است.
سایت
|
بله
|
تلگرام
|
اینستاگرام</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/679648" target="_blank">📅 12:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679647">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
دخانیات پای ثابت ۴۰ درصد سرطان‌ها در مردان ایرانی
وزارت بهداشت:
🔹
۴۰ درصد سرطان‌ها در مردان و ۲۱ درصد سرطان‌ها در زنان ایرانی با عوامل شناخته‌شده‌ای مانند مصرف سیگار، قلیان، تریاک و چاقی ارتباط دارد.
🔹
دود سیگار، قلیان و ویپ بیش‌از ۷ هزار مادهٔ شیمیایی دارد که دست‌کم ۷۰ مورد آنها سرطان‌زا هستند؛ قلیان هم برخلاف تصور رایج، گزینه‌ای کم‌خطرتر از سیگار محسوب نمی‌شود.
🔹
در گروه سنی ۱۸ تا ۲۴ سال، مصرف دخانیات در زنان ۹۰ درصد و در مردان ۳۴ درصد افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/679647" target="_blank">📅 12:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679645">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی وزارت کشور: توهین به رییس جمهور جرم است.
🔹
اعضای باند تولید و فروش سکه‌های طلای تقلبی در قم بازداشت شدند.
🔹
ایمان انوری، مجروح حمله اخیر آمریکا به سایت راداری جبالبارز کرمان شهید شد.
🔹
نخست‌وزیر و وزیر جنگ اسرائیل دستور دادند که تاسیس شهرک جدید در منطقه رفح غزه آغاز شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/679645" target="_blank">📅 12:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679640">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svWbvSigPHf3P0GBVHRjuBANFPUugoqsfsmY8sG9BsYURRXdWug1jd5GgyTZAgy8KNPhMds-7y7toluKJsDMxZfaFFB-zGtGp9nDXeOom77jt4F-iE6D8oA6f2HEok-7CGvK-b8snmPebGsVOfgJm3myZkH4bJ-l9btQbEo-eFr8iOuDFe7hAtNjEdgpRXfF1XkH_QZoqacnAYQ8Jn3OH2c0ZM4Lmr290QhSH0Zf2yh7r0ekDeR6JtsDm_OAk1qxXBqwdNuGw3L-bB0WIbj7MBFmL0Dafp70ZKQ62Tf_gN3yLig-jSj2tl_Wwe4SajuPfA4umB47PJvZ6PHoyIIL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۰ ابزار عالی و رایگان برای دانشجویان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/679640" target="_blank">📅 12:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679638">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9172d880e3.mp4?token=e5JloZQ7U4qiPVxhFxKDHyY4CGo-3axGTviNoWH66eOhkWYT4q9l5Vbf913F7J1Pstwe28zE8xXmtYQpHeHKaLbdEFi593zofNz5TP76XUTstVicuzybZcsN7iXLcWvjnfR9TZQmkvEAL-_SWkQZddW2BtE6M2WRex6VlFy9D0CntArKU2eny3dXezZDo-h4Ph5qmg-h4XX8meHRN-IHqMxvJ0XF4DpavGop1IJeGqOVrhZHM8SNHNm-99szMARZ-r93pWWifqDilCFAg92ipZGUGpyi4P2QTVzbcoB0cfUaQd8ZS_iVLe_aS6omrgeyo-NWqrQqEN9rHHBRM3AUSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9172d880e3.mp4?token=e5JloZQ7U4qiPVxhFxKDHyY4CGo-3axGTviNoWH66eOhkWYT4q9l5Vbf913F7J1Pstwe28zE8xXmtYQpHeHKaLbdEFi593zofNz5TP76XUTstVicuzybZcsN7iXLcWvjnfR9TZQmkvEAL-_SWkQZddW2BtE6M2WRex6VlFy9D0CntArKU2eny3dXezZDo-h4Ph5qmg-h4XX8meHRN-IHqMxvJ0XF4DpavGop1IJeGqOVrhZHM8SNHNm-99szMARZ-r93pWWifqDilCFAg92ipZGUGpyi4P2QTVzbcoB0cfUaQd8ZS_iVLe_aS6omrgeyo-NWqrQqEN9rHHBRM3AUSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از حملهٔ سنگین دشمن صهیونیست به ارتفاعات علی‌الطاهر برای اشغال این منطقه با سو‌ءاستفاده از فرصت آتش‌بس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/679638" target="_blank">📅 12:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679636">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEcWRMmRNUQRWXEJ5BPLy31OhH4V31dX8rWvVJYBEnli8RBySkQGy8h7cV_lp6l5K0mPum280P9x6CvU9pm32BIaikwfBYShsw_fwzQfmHi_3Fvw1hvMQIVF8Sp4DYurx1bC85XbBLrTZ-ppaL0gNs481wLE3PAtKoghb_ZoJN48_OBk8qu2rzu5d3Z5wfgdGfn0K_2PK_TKmLP0ccPN94t8ktuyAlN4WQfNqrMr3fw9NReXZ3NPJFglyPYYRYznE1pUobxOG8nvYCwwbZ2UqDjCgTZ8INWQGcLArX-qkVGYVhDwd4dqVvdDw8-wI4kWWOdvJyBd68YXN04nN_OLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این هفته در دنیای فناوری چه گذشت؟ #نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/679636" target="_blank">📅 12:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679635">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6949e4f923.mp4?token=fc4668iEvgja1I5n0nn_vUfj266kPzMoAEpbqbq6yTtNGvO6EOd2V848nk5Ooo5X7NOw6j8MCABupKndxWJmthMo-8jMhXdmR81ADliKFXZMyOXgwidEUot8CQNheRGvGe70E6uMCzVX11v65S205BpbREyUW07if0x5U6FvvY_VQVR0vI_YJpNTN-gyda4KtNCefgJ9h6S8jDpDc2qMgHv1fOsa1jt8SbR24gym-3tIbXdXU4lqcOP4BQZw_1uE1Vji_ERkX01TJ86Mu2vqWRCElJAl8XAERbtcLiElYt872zCC0tqYueskXdGcp_V5WTd_bP7gaCivmwSu0Wemv19uPLHM2-nl-zzTEpOfpKIVY3UMRhMAS3vrqixcEdNMpP78IVC19cshGNOGHakR6rw9R8bI5F7H7MKy89dWcQ1JG-yLUmX6I37RlxodOLpNDlgt13L9usFpHvyufXZAQkrj_HkwcHAeVvXNa9oKM6VsmFz8AG2NEXGNAkZJ-BKctQ4FjdkEL5LfxOKMRcXaQAxLZulUIqZ2AvcIdhaxyT5rs3WyO0ItaQoKYm5XVMy05CFHygAQCtLvsdvDD3cNQBpyGdFvgapD_fSo-NaOmXrxix0GOpLrG4baj0vXDusmBOQBDDo_gGp3SAM4WWX1GX8rdekYRCHuyQxXvjoEHDU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6949e4f923.mp4?token=fc4668iEvgja1I5n0nn_vUfj266kPzMoAEpbqbq6yTtNGvO6EOd2V848nk5Ooo5X7NOw6j8MCABupKndxWJmthMo-8jMhXdmR81ADliKFXZMyOXgwidEUot8CQNheRGvGe70E6uMCzVX11v65S205BpbREyUW07if0x5U6FvvY_VQVR0vI_YJpNTN-gyda4KtNCefgJ9h6S8jDpDc2qMgHv1fOsa1jt8SbR24gym-3tIbXdXU4lqcOP4BQZw_1uE1Vji_ERkX01TJ86Mu2vqWRCElJAl8XAERbtcLiElYt872zCC0tqYueskXdGcp_V5WTd_bP7gaCivmwSu0Wemv19uPLHM2-nl-zzTEpOfpKIVY3UMRhMAS3vrqixcEdNMpP78IVC19cshGNOGHakR6rw9R8bI5F7H7MKy89dWcQ1JG-yLUmX6I37RlxodOLpNDlgt13L9usFpHvyufXZAQkrj_HkwcHAeVvXNa9oKM6VsmFz8AG2NEXGNAkZJ-BKctQ4FjdkEL5LfxOKMRcXaQAxLZulUIqZ2AvcIdhaxyT5rs3WyO0ItaQoKYm5XVMy05CFHygAQCtLvsdvDD3cNQBpyGdFvgapD_fSo-NaOmXrxix0GOpLrG4baj0vXDusmBOQBDDo_gGp3SAM4WWX1GX8rdekYRCHuyQxXvjoEHDU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط در ۴ دقیقه با ترفند‌های مختلف شعبده‌بازی آشنا شوید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/679635" target="_blank">📅 12:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679633">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHM6iFbsg64ZDJqE_HcJb1oI7iJMZ3Vk3oFla9HwvnxM5IlDwBf4saYbItUqgznEq92jl6QtorB0s9ZeZFNjeh_aOxFWOjIG6_YAbfVGkHvTC98_n3STK88r32B9s_f_LSy4YEiHknkbx7EBlcOAPdVBbaFuLYe-eryp2MFwMHrK0oYxzr9_Asq2pcJ9bpHjUK6KA4XoqXmSciFcv_0YXQBM39taNswWZYIb27zNLAu86ca0Q98cTa8Ci8VO8aski2zy7XtQEQU1s12FXvxftsXL9JBRjQbt5ZPM8j2Uxr_JW__aGx4OF08jiSium1jF_CShBU68mQ4P8JCdnI2Xgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ب
رنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🏸
شروع روز با انرژی و حفظ سلامتی
ورزشی |
#ورزش_صبحگاهی
| ساعت ۸
🍱
انواع دستورهای خوشمزه
آشپزی |
#آشپزی
| ساعت ۱۰
🧠
سبک زندگی بهتر و ذهن آرام
روانشناسی |
#سلامت_روان
| ساعت ۱۲
✂️
آموزش داشتن استایل خوب و مناسب
فوری استایل |
#فوری_استایل
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
💡
معرفی انواع ترفندهای کاربردی
|
#ترفند_فوری
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/679633" target="_blank">📅 12:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9c3b5e72.mp4?token=iGfiXa4OWkbeA0ZF18IbxM3OeZ7p8vsgOsdnqhVa7Mw_OJRc5zsfUogf3pXp5y96b68Cf9w0CPW5s6IVvx-v5asFplbA9TThxpxqEtFV8yE0M9OmG7i4eXFkn7SjAz4JRS04_3awKkyIf__ldFExWnmuprmc6h8RIW11ne14vdUNSxNfcz54-Z0wmEpqK7hkvdZluHU1DLGO9a5HYFdKcZ9WL5FwcIQ6Rgin5S8YJwsUD5mbmrrnnLP6Ajsd46v-On38lNS1Kj0gFBaf_9tR19c1qJ-jVCeOprF6TiO2vc9tpYQy-HVFAKjRjOcVN1bk2aR1BtHzzcOejbbrJURfdr2UX4pR2SRciW6YUtWL3akwY4svrglJkf8TDEPH1eCqpwVf2Oz9AlayFf4i6dcNNlxN04GY7k7rGummmaML4ohv46ZpV0SvrujXceoz0tvPBxOkUK8bXFBifvbPRvu5hBkab_nOR_J5oxHgmSxq8wpF2A5_a0vhxrNtI17yfg7IS5BmzFBE5uVdu5erFcNZneWJccGVk5YutwBrW2TgA-CF9OHxOa8rVkjlOEHZAqHtyig8IU02_TBtW1MubEng4E6dcB1sZR0gDJTRaAN3VoDPQK37vVkS00ve9Enoy0kRpchEYpGsSBfKOEIWt2Oherw_cXgJjF8YSu4frgrFlnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9c3b5e72.mp4?token=iGfiXa4OWkbeA0ZF18IbxM3OeZ7p8vsgOsdnqhVa7Mw_OJRc5zsfUogf3pXp5y96b68Cf9w0CPW5s6IVvx-v5asFplbA9TThxpxqEtFV8yE0M9OmG7i4eXFkn7SjAz4JRS04_3awKkyIf__ldFExWnmuprmc6h8RIW11ne14vdUNSxNfcz54-Z0wmEpqK7hkvdZluHU1DLGO9a5HYFdKcZ9WL5FwcIQ6Rgin5S8YJwsUD5mbmrrnnLP6Ajsd46v-On38lNS1Kj0gFBaf_9tR19c1qJ-jVCeOprF6TiO2vc9tpYQy-HVFAKjRjOcVN1bk2aR1BtHzzcOejbbrJURfdr2UX4pR2SRciW6YUtWL3akwY4svrglJkf8TDEPH1eCqpwVf2Oz9AlayFf4i6dcNNlxN04GY7k7rGummmaML4ohv46ZpV0SvrujXceoz0tvPBxOkUK8bXFBifvbPRvu5hBkab_nOR_J5oxHgmSxq8wpF2A5_a0vhxrNtI17yfg7IS5BmzFBE5uVdu5erFcNZneWJccGVk5YutwBrW2TgA-CF9OHxOa8rVkjlOEHZAqHtyig8IU02_TBtW1MubEng4E6dcB1sZR0gDJTRaAN3VoDPQK37vVkS00ve9Enoy0kRpchEYpGsSBfKOEIWt2Oherw_cXgJjF8YSu4frgrFlnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اختلال اضطراب با بدن ما چه ‌کار می‌کنه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/679631" target="_blank">📅 12:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
عراقچی: باز شدن تنگه هرمز منوط به یک سری شرایط است
وزیر امورخارجه:
🔹
مذاکره با عمان درباره تعیین مسیر دریایی جدید در تنگه هرمز است. ما در مرحله پایانی هستیم.
🔹
مسیرهای قدیمی با مسیرهای جدید جایگزین می‌شود. متخصصان در حال کار بروی مسیرها هستند.
🔹
البته این به معنای باز شدن تنگه هرمز نیست. این توافق ممکن است صورت بگیرد اما باز شدن تنگه هرمز منوط به یک سری شرایط است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/679630" target="_blank">📅 11:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679629">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سخنگوی پلیس: نفر اصلی دخیل در قتل حمیدرضا رجب‌زاده دستگیر شد/ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/679629" target="_blank">📅 11:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679627">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f780ae15a.mp4?token=MpVMfQGoitrogE9dj5VjkTDGoY595YS4yAZDZxKuoGR_ZjlO6AnvnPzCTxZxSy8MndD3UxRH-2xXb3z3Z9qUAVb43Xmzov5MHMD8LPsIrvgkpubxAiGA6PcUSYdOewYECgQkNQQG8DJIB49oE-STShvV9ll6q_k8UQZFzMSRNuTRJPDEiBHrxm8merD8VeXxiPRZryEkqjznvRew7Y5qJe7XB9FH-aByH3pzf2sA7eEcl8ur1gPTgzF447JgReEbOfC3YuYJlaf3fVO0rKsP9bYmWpJoKh83v-M0N6cphMBDItx_ftjF9UZl54EJtlWTGjx2dRIvNIdOKTGWMurdK2EXaQ1lt2ChGmKaY-7HNLq9dbeF93f5uJp-RPYK_raehkBrR10gqEdfaJo2q2OemRa-r73Yn-SUxifFY6vKW9Hj23SuM2Lt-vnqCGphjDoXIw-kDyKrwNy5GRSJz-lGKzuVNo4ZqwN8h4W4NF0_AzBpus46umhSVe0exEBc24z-Ocwv8AjSt_oRV2f5xomulh0fs71QUnBn5x-Bz7MFzsv4djXz-fykldyIiFeUD5m7Wwhle6kNa21BaMJtdMs2GWDPha_lOqUhjFZsB-EfPvztcRs4AcGnziialoBRtDNq5U6aldjc8quyw7v2kJRyLxstxaY_eqLJOdlNfmQiYNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f780ae15a.mp4?token=MpVMfQGoitrogE9dj5VjkTDGoY595YS4yAZDZxKuoGR_ZjlO6AnvnPzCTxZxSy8MndD3UxRH-2xXb3z3Z9qUAVb43Xmzov5MHMD8LPsIrvgkpubxAiGA6PcUSYdOewYECgQkNQQG8DJIB49oE-STShvV9ll6q_k8UQZFzMSRNuTRJPDEiBHrxm8merD8VeXxiPRZryEkqjznvRew7Y5qJe7XB9FH-aByH3pzf2sA7eEcl8ur1gPTgzF447JgReEbOfC3YuYJlaf3fVO0rKsP9bYmWpJoKh83v-M0N6cphMBDItx_ftjF9UZl54EJtlWTGjx2dRIvNIdOKTGWMurdK2EXaQ1lt2ChGmKaY-7HNLq9dbeF93f5uJp-RPYK_raehkBrR10gqEdfaJo2q2OemRa-r73Yn-SUxifFY6vKW9Hj23SuM2Lt-vnqCGphjDoXIw-kDyKrwNy5GRSJz-lGKzuVNo4ZqwN8h4W4NF0_AzBpus46umhSVe0exEBc24z-Ocwv8AjSt_oRV2f5xomulh0fs71QUnBn5x-Bz7MFzsv4djXz-fykldyIiFeUD5m7Wwhle6kNa21BaMJtdMs2GWDPha_lOqUhjFZsB-EfPvztcRs4AcGnziialoBRtDNq5U6aldjc8quyw7v2kJRyLxstxaY_eqLJOdlNfmQiYNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: اکنون هیچ مذاکره‌ای با آمریکا نداریم
وزیر امورخارجه:
🔹
واسطه ها همچنان دارند تلاش می‌کنند تا راه‌های مذاکره را مجدد پیدا کنند.
🔹
تا موارد نقض یادداشت تفاهم از سوی آمریکا به پایان نرسد و آمریکا انچه را که نقض کرده جبران نکند، از نظر ما امکان شروع مجدد مذاکره وجود ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/679627" target="_blank">📅 11:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679626">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f821f75237.mp4?token=oMmmvFF4ooGhNlQ-Azly_VW7xWONwmhzubCefXten3sIoM7qdwGa-6nvOWJhYQZcMusrSOf5AUaRWwDulomwJAvsnTwMxFM-RO7qzrJxt_-NK_bmiDjMRxrANG3VQDsU_W0zjVHJOJQVDh3UEbRJOEe9txOYg_SWyxuQlwVOD52z6rx5Vv15UqA89c1V5rOjxXBAEvjnbWYXrQlmjkQtNFyE8ENr6fxOJflLynezKYGlzevlihQBtVuS_0wykbCH-5v5ndyHERMJJDEeodScGERT7aEpw6WM2u_MoTMo-CQ0xAMPp-8YxCsKQPEL8OsnutnBA1cjH0qwPnBa2hK1hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f821f75237.mp4?token=oMmmvFF4ooGhNlQ-Azly_VW7xWONwmhzubCefXten3sIoM7qdwGa-6nvOWJhYQZcMusrSOf5AUaRWwDulomwJAvsnTwMxFM-RO7qzrJxt_-NK_bmiDjMRxrANG3VQDsU_W0zjVHJOJQVDh3UEbRJOEe9txOYg_SWyxuQlwVOD52z6rx5Vv15UqA89c1V5rOjxXBAEvjnbWYXrQlmjkQtNFyE8ENr6fxOJflLynezKYGlzevlihQBtVuS_0wykbCH-5v5ndyHERMJJDEeodScGERT7aEpw6WM2u_MoTMo-CQ0xAMPp-8YxCsKQPEL8OsnutnBA1cjH0qwPnBa2hK1hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش گره ژاپنی فوق‌العاده کاربردی
که حتما به کارتون میاد
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/679626" target="_blank">📅 11:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679623">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
برادر شهید رجب‌زاده: پیکر برادرم هنوز پیدا نشده است  مصطفی رجب‌زاده، برادر شهید حمیدرضا رجب‌زاده:
🔹
از ۳ مرداد حوالی ساعت ۱۱ برادر شهیدم مفقود شدن و ما هم کربلا بودیم، به محض اینکه متوجه ماجرا شدیم به سمت تهران برگشتیم.
🔹
قبل از شهادت ایشان هیچ پیام یا تماس…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/679623" target="_blank">📅 11:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679621">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9d00efa4.mp4?token=E4HKPqUpbe1Kprr59IXacCJcLprelnXw0ImjXKsfi-k6hW2dpo4a8eMCGJC8VYdI5YWya_0QUQzCR8Ocqrs6iK1lksJQvK7oT7vg0heTbNPze8EHGpgS2A9vmCYS-sVlWKULxKvIcRMpZbHsuG3E3EijlH3CmYRHa1e_D9COI-3VJJYB3WpapNPpOlCCTYW-mUXLnY6IBEQJkmOX7iScIFZ8DvjE6ssGE38GFE184LyFrSLXzvOBNF3Aos14DiFKICqdRrFn5_7IVqD2D3LJERLF9vbQdI5Es2F7t1xMO5vfQ93VqFVoVFnvFFb0_jjiHBt1ljyrYV8yJsTb2PpykQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9d00efa4.mp4?token=E4HKPqUpbe1Kprr59IXacCJcLprelnXw0ImjXKsfi-k6hW2dpo4a8eMCGJC8VYdI5YWya_0QUQzCR8Ocqrs6iK1lksJQvK7oT7vg0heTbNPze8EHGpgS2A9vmCYS-sVlWKULxKvIcRMpZbHsuG3E3EijlH3CmYRHa1e_D9COI-3VJJYB3WpapNPpOlCCTYW-mUXLnY6IBEQJkmOX7iScIFZ8DvjE6ssGE38GFE184LyFrSLXzvOBNF3Aos14DiFKICqdRrFn5_7IVqD2D3LJERLF9vbQdI5Es2F7t1xMO5vfQ93VqFVoVFnvFFb0_jjiHBt1ljyrYV8yJsTb2PpykQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمونه‌ای از عشق مادری در دنیای حیوانات
🔹
دوربین
‌های مداربسته در استان یون‌نان چین، صحنه‌ای جالب از یک خانواده فیل ثبت کردند؛ وقتی پای بچه‌فیل میان سیم‌های ایستگاه شارژ خودروهای برقی گیر کرد، مادرش ابتدا او را نجات داد و سپس برای جلوگیری از تکرار حادثه، ایستگاه شارژ را تخریب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/679621" target="_blank">📅 11:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679618">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: دلیل تشکیل پیمان مکه، ناامیدی عربستان از آمریکاست
احمد بخشایش، نماینده مجلس:
🔹
پیمان مکه صرفاً قراردادی روی کاغذ است و اقدامی عملیاتی نخواهد داشت. عربستان از آمریکا ناامید شده و برای دفاع از خودش به لایه دوم امنیت پناه برده که پیمان دفاعی با ترکیه و پاکستان است.
🔹
پاکستان خودش درگیر جنگ‌های زیادی است و ترکیه نیز شرایط اقتصادی خوبی ندارد و این باعث می‌شود بخواهند پولی از سعودی‌ها دربیاورند.
🔹
درگیری حوثی‌ها با عربستان، ایران با پایگاه‌های آمریکا در عربستان و نبرد اسرائیل با ترکیه در سوریه، از دلایل اصلی تشکیل این پیمان بوده است./ همصدا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/679618" target="_blank">📅 10:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679616">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b461717e1.mp4?token=urZNpq_XQ2M-62GUcCsRyEzqn2mj9o5ddJBo7v3zXmowTgK2YWo5pjomMJ3B7NNRVVEGtivKjVB60INgt4Z-SPWgBVVL3Xv39kShCx1vNbuiuR0eFRXGvr20gMzfnQvbytGIaKmxp7ni7HX88Q3JVsfeCfVq8O__sbcLvI9jYTAYkLEaA0YsLhku2LEono8dvZOQfHoGdkPyPWHelZA0WPJ9dcKSuSxMTJlH8_Bp7ZUsxC8dADc3cX_AqNlGBYRbGIwBa4EtQLfcEDvmix0OpNcwMObsybwuSjdtjrzkxrcB1olSGdbVlQzxJ5MlRkM2Kp93nqrjUHMvbyCtdi4BjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b461717e1.mp4?token=urZNpq_XQ2M-62GUcCsRyEzqn2mj9o5ddJBo7v3zXmowTgK2YWo5pjomMJ3B7NNRVVEGtivKjVB60INgt4Z-SPWgBVVL3Xv39kShCx1vNbuiuR0eFRXGvr20gMzfnQvbytGIaKmxp7ni7HX88Q3JVsfeCfVq8O__sbcLvI9jYTAYkLEaA0YsLhku2LEono8dvZOQfHoGdkPyPWHelZA0WPJ9dcKSuSxMTJlH8_Bp7ZUsxC8dADc3cX_AqNlGBYRbGIwBa4EtQLfcEDvmix0OpNcwMObsybwuSjdtjrzkxrcB1olSGdbVlQzxJ5MlRkM2Kp93nqrjUHMvbyCtdi4BjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک دستگاه جدید و جالب برای سرخ کردن ماهی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/679616" target="_blank">📅 10:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679615">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
وزیر امور خارجه: نه فراموش میکنیم و نه میبخشیم
عراقچی:
🔹
ما بر عهدی که با سیدالشهدای زمان شهید سید علی حسینی خامنه‌ای بسته‌ایم ایستاده‌ایم؛ اجازه نخواهیم داد این خون‌های به ناحق ریخته شده فراموش شوند.
🔹
میهن‌پرستی واقعی، وفاداری کورکورانه به سرزمین نیست بلکه وفاداری به ارزش‌هایی چون آزادی و عدالت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/679615" target="_blank">📅 10:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679612">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تاسیسات آرامکو عربستان منفجر شد
🔹
وزارت انرژی عربستان حمله به تاسیسات آرامکو در منطقه جازان طی بامداد یکشنبه را تایید کرد. طبق منابع عربی چندین انفجار در این تاسیسات گزارش شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/679612" target="_blank">📅 10:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679611">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای جدید محمدباقر خرازی: کلیپ‌ها جعلی و ساخته هوش‌مصنوعی است
🔹
من این حرف‌ها را نزدم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/679611" target="_blank">📅 10:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679609">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
این دسر موزی یخچالی مخصوص مهمونی‌های ویژه‌است
😍
موادلازم‌:
🔹
بیسکویت پتی‌بور ۲۰۰گرم
🔹
موز ۳عدد
🔹
شکر ۳قاشق غذاخوری
🔹
شیر۲پیمانه
🔹
نشاسته ذرت ۳قاشق غذاخوری
🔹
کره ۲قاشق غذاخوری
🔹
خامه قنادی
🔹
وانیل نصف قاشق چای‌خوری #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/679609" target="_blank">📅 10:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679608">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtw8c77ljEmBz-rRO6J7Mmn_xZaIA4ekQ6obgCb1RNpOEVXWSz2QQHD0Vf5H-s3r_1yhIzeaWcdmIop6pLfnibhOI1l2CqaqMu8WlZMT5Z0iGviu2mGEUsNy4gfJI0Mm5jDLHXlcuqpv6TLtOY7V0vv5ddIium4FuszhgmraRkskhRqJHFJvJEso8ZhEI_WLzylmwEd-HA6-mLjkp1xQMcRVRrmke0GRJ9AGBB5qo-AL5LVcKfXUJescYfJ4pX6EH8B-xyAhzWn3b-VHQPvVvcqyuVfajFbMyWNhsQOPHNUQ16jTb1cz42AafDIU-8ZwOx8M-7JtcUbx1ta0M7Xc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پولِت نقد نیست؟
🤨
مودم + اینترنت LTE پیشگامان رو ۴ قسطه بخر
✅
همراه با سیم‌کارت هدیه و ارسال رایگان
💳
خرید ۴ قسطه از اسنپ‌پی و ترب‌پی
👈
راه‌اندازی سریع و آسان
⚡
بدون نیاز به خط تلفن ثابت
🎯
خرید آنلاین:
https://pte.ir/GNwsN
☎️
تلفن سراسری: ۱۵۷۷
🆔
کانال پیشگامان |
@pishgaman_official</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/679608" target="_blank">📅 10:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679607">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c657f68dd9.mp4?token=dLAgWbUEWVM9cJCglqKp49u_BMPvGqVpUP7Lw44trg5vk35LJb7JvZXATs9JbEuebNLUgK3WSc-ejjWXl5J7mG08wwBajKgy0M94eNT5d5jUkyQU5Dv6GsQeF_4xlpZ5n6yrcy1LkuRdTRxmimj-yg_9EgyetKxoaHw1LPJtJ0y0rAhkWwbUL0apVlXcbioQtQSg0O4ZJtezDl43wmlag0BSIczoYHhJB7erzpFEP7uBE1BvyAUYRhkk71AyUM512P_dzjTqVyWPia4siF2QCyUDDyksLVceTCJ6Ga7XrOOGj4lUHmZhFATM1ucUcSIg6OTn6Icjivf_P3iohqVkqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c657f68dd9.mp4?token=dLAgWbUEWVM9cJCglqKp49u_BMPvGqVpUP7Lw44trg5vk35LJb7JvZXATs9JbEuebNLUgK3WSc-ejjWXl5J7mG08wwBajKgy0M94eNT5d5jUkyQU5Dv6GsQeF_4xlpZ5n6yrcy1LkuRdTRxmimj-yg_9EgyetKxoaHw1LPJtJ0y0rAhkWwbUL0apVlXcbioQtQSg0O4ZJtezDl43wmlag0BSIczoYHhJB7erzpFEP7uBE1BvyAUYRhkk71AyUM512P_dzjTqVyWPia4siF2QCyUDDyksLVceTCJ6Ga7XrOOGj4lUHmZhFATM1ucUcSIg6OTn6Icjivf_P3iohqVkqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای بسیار زیبا از خانه خدا در مکه
❤️
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/679607" target="_blank">📅 10:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679605">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmyQ7uSLjZyg1a-rfqSx1eO-2k9-L31oWKI57esrBtehNgcB1ubPttiHljmzbBMNwRTcrqT30ielM6ohEErTzFz8DblmZREvT7ia8NgVtmfL1x1-6FuqJMLKk4TJihl1ZsYGGEtcabW9pCItaIHGHu5Xpygb3W-sn8iQErfEVaNxwwS0u0Pd5xVCsZGpt6DHZ7JpSCAhH4yxyk_LfktMoQUyuEKfK4rJY9qQqxTRQYoOIOLLgU8DmTCWCjy86WNmtabIrSwZW-_q23yymwemKLkadToFn9Km26bW9AjA8nCfvsmvWyppNmRqveMIky9DeNdA6qO-NcUNrl5SS5lleg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش تلویحی ظریف به توافق مکه
محمدجواد ظریف:
🔹
همان‌گونه که یک سال پیش در مقاله «اسرائیل بزرگ و منطقه قوی ما» نوشتم، سیاست نژادپرستانه و تجاوزکارانه «اسرائیل بزرگ» که این روزها آشکارا از سوی سران رژیم صهیونیستی دنبال می‌شود، ضرورت پیمان‌های دفاعی فراگیر میان کشورهای اسلامی را بیش از پیش آشکار می‌سازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/679605" target="_blank">📅 09:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679604">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
دبیر ستاد ملی جمعیت: تعداد ولادت‌ها در ۱۴۰۴ نسبت به ۱۴۰۳ کاهش یافته
دستجردی:
🔹
در سال ۱۴۰۴ تعداد رخدادهای ولادت به ۸۹۲ هزار و ۲۸۲ مورد رسید که نسبت به سال ۱۴۰۳، ۸.۹ درصد کاهش نشان میدهد.
🔹
با یک شیب کاهشی مستمر در آمار تولد مواجهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/679604" target="_blank">📅 09:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679598">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGXnFGXgGzA17YcTuvho2bsinxHEE0q2GB8Lxq-uVlILain-p_t6ks0lLeeBvDV8cgP3LikRuKFFj9Ukwa5IILI_kdONbdLOvKHp6fK4AlqR84B3OnNYtesu85obSx3S3xgQo8xLpd2PVM-XPiKM9fLblRkUVa1-laGst1KYwfOwOjK--GiET76ZDa1sa4wCDhgd2fGBNP91QvyJ8RHxQgep_9E7m4NKYRWhCDVwUS66M1k1Ja5qihPVy5eMchnSu-SGnihee3SQrYjoE1nleJOZ-ej282BNYoco-RjBZRpmrNRplZPTwPppcCga8vsEPYAKBIrv-AAjlS_g3lj5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مالکی: مذاکرات ایران و عمان درباره تنگه هرمز در آستانه نهایی‌شدن است/ آمریکا اجازه حضور در مذاکرات را ندارد
فداحسین مالکی، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس:
🔹
مذاکرات تاکنون پیشرفت‌های خوبی داشته و عمانی‌ها نیز پذیرفته‌اند که به هر حال به‌طور موقت از مسیر جنوبی استفاده نشود.
🔹
اگر این توافق تحقق پیدا کند، کنترل تنگه هرمز کماکان در اختیار ایران خواهد بود و کشور ثالثی نمی‌تواند در مدیریت و کنترل آن نقش داشته باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/679598" target="_blank">📅 09:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679597">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R24lwAbvbZ8-G51Cyh_qcgsC-56Ca6c_qalqu_6AS0IjKHagnZanvCG80WawIN0NZJURWOptl1edCd1WjYqM1Da2nfFL2CkZkQOKBmZ5I2Mm0AyL6gpKfODwMJUY76kzDoVZQllumYRMo97B09M0qrUgqYVq-PNWvTVxmghbh3qPVXVK8pe3syYt3colB-GbIRmhYPFckH4g9GKgNsEVnLm0eDh-6PKDG0rkJ83drj1CgWSGq7EmPEM8czxXbYJ1gZhlXC3-eTQfXt9QoYyGdbZ4v1RokjmAAKrdojbYprypRrhxrUa0vwiaru_GCjkneU6Hl6lPp_7PlJNqSR63SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای العربیه: عربستان سعودی، ترکیه و پاکستان «توافق‌نامه دفاع مشترک مکه» را امضا کردند  توافق‌نامه دفاع مشترک مکه:
🔹
هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
🔹
هدف این توافقنامه، تقویت بازدارندگی جمعی در برابر هر گونه اقدام…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/679597" target="_blank">📅 09:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679595">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
صدورگواهینامه موتورسیکلت برای زنان؛ در آینده نزدیک
رئیس مرکز امور زنان و خانواده وزارت کشور:
🔹
تردد بانوان با موتورسیکلت از نظر اقتصادی به‌صرفه‌تر و کم‌هزینه‌تر است.
🔹
از نظر ما، مطالبه زنان و دختران جهت اخذ گواهینامه موتورسیکلت یک خواست اجتماعی قابل تحقق است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/679595" target="_blank">📅 08:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679594">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
سخنگوی دولت:
هنوز درباره افزایش قیمت بنزین جمع‌بندی نشده است/ کالا برگ قطعا افزایش می‌یابد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/679594" target="_blank">📅 08:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679592">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6bece62d0.mp4?token=G9J1S5owBe_tnbx1npg8JeuFMbyMsAJzKBBnukIiGPfcLO3eWwQ-kVBkv40APgyiVctLzObJ-lKYosix4vdKMSlkYT3_d1T88Ec-hqWgSQfeLXMCJxI6O83_9YjH836c0c_qv3uUQaEsxgkwSd2pvAVR5mrEZ-dFqI7q8Q6EjQWnMUJSv142Gv-s5_WL55P5d_cZtb5ek6pumBTOk9svahQkc8jezOIQ8V--B9eGPmCCqMWOlDzs6AIxsX-GXIDjmww17r4uKgpWMMGU39KbbRRN0-JGsH1Ts9c3aGWf15kLJ54n4IggK5Rl9kvV12idu_BgU9gSc0SJj7gKBO_b5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6bece62d0.mp4?token=G9J1S5owBe_tnbx1npg8JeuFMbyMsAJzKBBnukIiGPfcLO3eWwQ-kVBkv40APgyiVctLzObJ-lKYosix4vdKMSlkYT3_d1T88Ec-hqWgSQfeLXMCJxI6O83_9YjH836c0c_qv3uUQaEsxgkwSd2pvAVR5mrEZ-dFqI7q8Q6EjQWnMUJSv142Gv-s5_WL55P5d_cZtb5ek6pumBTOk9svahQkc8jezOIQ8V--B9eGPmCCqMWOlDzs6AIxsX-GXIDjmww17r4uKgpWMMGU39KbbRRN0-JGsH1Ts9c3aGWf15kLJ54n4IggK5Rl9kvV12idu_BgU9gSc0SJj7gKBO_b5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکذیب آتش‌سوزی در شهرک صنعتی نصیرآباد؛ حادثه آتش‌سوزی در یک کارگاه تولید اسپری
🔹
در پی انتشار خبری درباره وقوع آتش‌سوزی در محدوده نصیرشهر، به اطلاع می‌رساند حادثه مذکور در شهرک صنعتی نصیرآباد رخ نداده است و محل وقوع حادثه، یک کارگاه تولید اسپری خوشبوکننده بدن در خیابان پیامبر اکرم(ص) نصیرشهر و خارج از محدوده شهرک صنعتی نصیرآباد بوده است.
🔹
بنابراین، این حادثه هیچ ارتباطی با شهرک صنعتی نصیرآباد و شرکت شهرک‌های صنعتی تهران ندارد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/679592" target="_blank">📅 08:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679588">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8271d784e.mp4?token=o9v3ofEzoe6LBmjve06qmGE6VzVwIvmILGDlyJXwwxNw2jBxNBPlLHIntojb8e0i59FryhgyMfxX1iWW0x2Zqn-cxOKtB9xaZ_Fu701M1yWj2l2yfwwIr4_nWbtuwhdfrPt0MdFy9Wk4znqa8lV7VltxBHAb92YrBo7O3ITICBN7jm95i0hlBhRk5y-TY_4vtptEL-yGpI5hNnkI59rBPYVhHPRUdzNA6ZN6o5fSBYUCK5NOCthdeNe88lel3h3hPS7c0HMC2qBgz8S973GS7dR1J0rJJ77aQeF-PXpXBfl_JanScCYlsxAzPdE71YnW1BkEtyVm1j5DPD9wJDKKMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8271d784e.mp4?token=o9v3ofEzoe6LBmjve06qmGE6VzVwIvmILGDlyJXwwxNw2jBxNBPlLHIntojb8e0i59FryhgyMfxX1iWW0x2Zqn-cxOKtB9xaZ_Fu701M1yWj2l2yfwwIr4_nWbtuwhdfrPt0MdFy9Wk4znqa8lV7VltxBHAb92YrBo7O3ITICBN7jm95i0hlBhRk5y-TY_4vtptEL-yGpI5hNnkI59rBPYVhHPRUdzNA6ZN6o5fSBYUCK5NOCthdeNe88lel3h3hPS7c0HMC2qBgz8S973GS7dR1J0rJJ77aQeF-PXpXBfl_JanScCYlsxAzPdE71YnW1BkEtyVm1j5DPD9wJDKKMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
وقتی پای وطن در میان است، پرچم ایران همیشه بالاست #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/679588" target="_blank">📅 08:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679586">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dff62e807.mp4?token=Th_r9GDtl4AI2kcFqgzhhJPJqeDAM35RXD2BIseWfQP1bFnEcCKz1QCSp2Lxf1yczNCvQo8FG-_fi2Z2D0K73EPrSzl3a9CjMj--ZZa52vvwezZIXpFPPvPOq8rbfHQ5kolnbVyw-vuCiwZCC0zft_AoL9hoa8lJ_pL7hw2w_39J6GIUJ5Ww8BsAeXtQMhgKe4RwCqpVw8TgYrGRGmG0X6AWmS004C3P4WX5w224oh23mqoGlVy-nDa7zXs_2XPoYJ9yhsquwCZy3nJEVGOnt0-BBkC6_6qS2wYm4rH50-kERYkh_NEKklR72i5OFsaEfYoKX-6BTvWfi_xP93QIjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dff62e807.mp4?token=Th_r9GDtl4AI2kcFqgzhhJPJqeDAM35RXD2BIseWfQP1bFnEcCKz1QCSp2Lxf1yczNCvQo8FG-_fi2Z2D0K73EPrSzl3a9CjMj--ZZa52vvwezZIXpFPPvPOq8rbfHQ5kolnbVyw-vuCiwZCC0zft_AoL9hoa8lJ_pL7hw2w_39J6GIUJ5Ww8BsAeXtQMhgKe4RwCqpVw8TgYrGRGmG0X6AWmS004C3P4WX5w224oh23mqoGlVy-nDa7zXs_2XPoYJ9yhsquwCZy3nJEVGOnt0-BBkC6_6qS2wYm4rH50-kERYkh_NEKklR72i5OFsaEfYoKX-6BTvWfi_xP93QIjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کابل‌های پهپادهای روسی، جنگل‌های خارکیف را پوشاند
🔹
استفاده گسترده روسیه از پهپادهای فیبر نوری در اطراف ووفچانسک، کیلومترها کابل را در جنگل‌های منطقه خارکیف برجا گذاشته است. این پهپادها به‌دلیل اتصال کابلی، در برابر اختلالات رادیویی مقاوم‌اند و شناسایی‌شان دشوارتر است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/679586" target="_blank">📅 08:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679584">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/031ccc639f.mp4?token=DdjnZX66BXUbMmpqe1o972EoQhIEP2iOgW_k7ye_ptMvufQ-vd7_PMij-wrjLI4GeGaIyBaDSuVBW9v14WDT7y3Eh_7BtDDEfj86oaSZHwfoPuMn9jZOapYQeR1GcA4MmBXYXWWDQvmyT9pmMEAb8vu2_3dLYx-pL2Fb9K5MY0mCwdc00nrzjvAXxU_-6cMqqC4Ok9l7vbMfgmPdyzW1jndEMc_CQJmLS9gnsw00z6CIwPUODDA9jz_1_wn4kUVMRS1fUc_cJSvbhAZIoKRuTQZ8qZV8yhqgZoSGBZgwZFn8_j2edHI5cUl8Gs0QtQJrCRDt2eC-rZqeG7gg48bcDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/031ccc639f.mp4?token=DdjnZX66BXUbMmpqe1o972EoQhIEP2iOgW_k7ye_ptMvufQ-vd7_PMij-wrjLI4GeGaIyBaDSuVBW9v14WDT7y3Eh_7BtDDEfj86oaSZHwfoPuMn9jZOapYQeR1GcA4MmBXYXWWDQvmyT9pmMEAb8vu2_3dLYx-pL2Fb9K5MY0mCwdc00nrzjvAXxU_-6cMqqC4Ok9l7vbMfgmPdyzW1jndEMc_CQJmLS9gnsw00z6CIwPUODDA9jz_1_wn4kUVMRS1fUc_cJSvbhAZIoKRuTQZ8qZV8yhqgZoSGBZgwZFn8_j2edHI5cUl8Gs0QtQJrCRDt2eC-rZqeG7gg48bcDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همین الان تست کن ببین سیاتیک داری یانه!
🔹
اگه سیاتیک داشتی این تمرینات رو سیو کن و انجام بده و بفرست برای دوستات #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/679584" target="_blank">📅 08:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679576">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست‌ کافئین |</div>
  <div class="tg-doc-extra">رابعه بلخی</div>
</div>
<a href="https://t.me/akhbarefori/679576" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
رابعه بلخی (شکستنِ تله‌ی خودسانسوری)
🔹
در این قسمت، بزرگترین کلاس درس تاریخ را برای «پایبندی به اصالتِ برند و خویشتن»، «شجاعت در برابر فشارِ ساختارهای متعصب» و «پرداختِ هزینه‌ی شفافیت» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/679576" target="_blank">📅 07:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679575">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4d9bf69f.mp4?token=CWGmoLevB0528Eu6jGzEirD2lofIYu2Ouhzfu3LjHRWkCMLIQJAK-5jPALyhAU2EGFAoh-BRD1mdeZ1gGJhd-qMtduKf48KyZ4Rpm1xmDw00vTvDxeh_K1q4Z-tWuz58UHIrubw-VLDAKBjHg7Xvus0KgoVKkiJ_00XnhqJ2zcRdEui7hJ3557u0mQFJWulmVC8sKLzb2z-D8oLL6mWwpU-RA3scin5ucj1zDEXNCkcyEc0FdZIaDM-Gblr6A7gmHYeIrcEj0xe0aMeqdtytlqznmlZKStwm-6vdhiJuRAdcwhgEY9HAvF5RWIw_YrKiQmiXjXbYKQyJ8yWy-gtaQ6uEioqV9YoYmU4TRuwpmf_HRA3yicGMbt-mldzXvYPP5SZ-CUqfxnCYGjWMuVFRQrYBMwYL16vz2BtK4LyAXq8FL7G8M4JJVrnnB8w6egjFGcE5tWBawby0THqS-tMYH5on3ZhJmVaPOF4iLpRO47WwnEMZqy7R2akrKLpOoVNXupVsQ3wMlNnNmkKwRqRCpuAOxjxyH6uJY6XFYKpme6Oley15lwXTYgVlxUiQDLKl41n_krfRuwGJcgY6d5IYJp4SUe1AbVpdG8sD7E3LhFExNAkwrX6cyGEAo_KKZ09gehTFAAiFTF4GdFbWPEqpMls-qOE4MCEK8UQxQsUOqPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4d9bf69f.mp4?token=CWGmoLevB0528Eu6jGzEirD2lofIYu2Ouhzfu3LjHRWkCMLIQJAK-5jPALyhAU2EGFAoh-BRD1mdeZ1gGJhd-qMtduKf48KyZ4Rpm1xmDw00vTvDxeh_K1q4Z-tWuz58UHIrubw-VLDAKBjHg7Xvus0KgoVKkiJ_00XnhqJ2zcRdEui7hJ3557u0mQFJWulmVC8sKLzb2z-D8oLL6mWwpU-RA3scin5ucj1zDEXNCkcyEc0FdZIaDM-Gblr6A7gmHYeIrcEj0xe0aMeqdtytlqznmlZKStwm-6vdhiJuRAdcwhgEY9HAvF5RWIw_YrKiQmiXjXbYKQyJ8yWy-gtaQ6uEioqV9YoYmU4TRuwpmf_HRA3yicGMbt-mldzXvYPP5SZ-CUqfxnCYGjWMuVFRQrYBMwYL16vz2BtK4LyAXq8FL7G8M4JJVrnnB8w6egjFGcE5tWBawby0THqS-tMYH5on3ZhJmVaPOF4iLpRO47WwnEMZqy7R2akrKLpOoVNXupVsQ3wMlNnNmkKwRqRCpuAOxjxyH6uJY6XFYKpme6Oley15lwXTYgVlxUiQDLKl41n_krfRuwGJcgY6d5IYJp4SUe1AbVpdG8sD7E3LhFExNAkwrX6cyGEAo_KKZ09gehTFAAiFTF4GdFbWPEqpMls-qOE4MCEK8UQxQsUOqPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رابعه بلخی و جسارت عاشق شدن
#پادکست_کافئین
| فصل‌دو،قسمت‌سیزده
🔹
نخستین شاعرِ زنِ تاریخِ ایران که نشان داد چطور یک روحِ آزاده می‌تواند با ابزارِ هنر و اصالتش، تمامِ خط‌قرمزها و ساختارهایِ طبقاتیِ زمانه را به چالش بکشد؛ حتی اگر بهایِ آن، نوشتنِ آخرین اشعارش با خون بر دیوارهایِ حمامِ بلخ باشد.
🔹
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/1r5Ic2zOt5Q?si=4BsA2eVTJROtKpW9
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/679575" target="_blank">📅 07:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679574">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neUECBx_UM7fXVlwytLImSoCNfX-Qt-hWA_5NZKTEoL-Kvow66ZwLfLtSrDv8zpER55IV_-TlqbQxJ61NkPP2oQ0cj2762lFwIB0uPQw-to-JuDjppdO49kyxsYtq1T6Jz5lP0A0iq6S6tykzSafdBLL3iY8dCfoKxbcMgp-f7Dk6TmegFS-owyLBzD3qfbONw9fkEESRFZ9M93RZW4zYHjXP-UmZ55B3fXTePoBQLXBhXVjFzWitzdkKo6zrcmB-LcYV81UWZQFrjJw0k-h4PdXqATfx_IGcoKZX2mqbIwc5RbkMUXNdS7xitSvY03GD59yDcFNK4n-XbzkUFlhPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۸ مرداد ماه
۲۵ صفر ۱۴۴۸
۹ آگوست ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/679574" target="_blank">📅 07:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679573">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
تاسیسات آرامکو عربستان منفجر شد
🔹
وزارت انرژی عربستان حمله به تاسیسات آرامکو در منطقه جازان طی بامداد یکشنبه را تایید کرد. طبق منابع عربی چندین انفجار در این تاسیسات گزارش شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/679573" target="_blank">📅 07:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679572">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
منابع عربی از هدف قرار گرفتن تاسیسات گاز در شهرک صنعتی جبیل عربستان سعودی و شعله‌ور شدن آتش در آن خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/akhbarefori/679572" target="_blank">📅 04:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه نیک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDS2iLHbjLcOqH0IX4qQ71BHuk81kY-yncJZJYQrfNwxunsb7mDY73nnJz0EVeZ7yNVGfGga4vV_Q2ojUadrt3Fw_L5UzmBMq9PqK0rn-AzTyxKrGS7A8hmZkg4QXz6BsgvPJlvCqDQuFAtMdth2OdVnsJ00UGlzZFa9CPKGtxY7DIjzNXshRQjqBQbYRYXWvYQ8hWsNlkwlZYXYb4T9NQWtH_eqSdxjB8BApqs6gUVbME8RJOqd-Zxt-a6upELUFw9hzXhBQCV11AIkve9DX2oJ3_UwVcEu7zmcvavrn_JriyiLn8TpVI_XLgYlbWnxlA0PMMqCRUE4YLF6HlVelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهمِ پرنسا ۴ ساله، به‌جای خنده و بازی، تخت بیمارستان و شیمی‌درمانی‌های طاقت‌فرسا شده است
😭
💔
پرنسا برای ادامه نبرد با سرطان خون به داروهای ضروری نیاز دارد، اما خانواده‌اش با درآمد اندک کارگری و خانه استیجاری، توان پرداخت هزینه‌های درمان را ندارند.
😢
بیایید نگذاریم کودکیِ پرنسا روی این تخت‌های سرد جا بماند.
🥺
🤲
✨
شماره کارت/شبا خیریه نیک:برای کپی کلیک کنید
6037691990491185
6280237094218423
IR110190000000216777746001
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام نیک
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
⚠️
مازاد کمک‌ها صرف امورات مؤسسه و یاری به سایر کودکان محروم خواهد شد.
💚
آدرس کانال ما :
👇🏻
👇🏻
https://t.me/+YQ8wu_Q7QahjNmNk
https://t.me/+YQ8wu_Q7QahjNmNk</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/679569" target="_blank">📅 01:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679566">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
مطالبات غیرجاری ۲۲ بانک به ۹۳۰ همت رسید
🔹
مطالبات غیرجاری ۲۲ بانک به حدود ۹۳۰ هزار میلیارد تومان رسیده، رقمی که نسبت به خرداد ۱۴۰۴ حدود ۴۰ درصد افزایش نشان می‌دهد.
🔹
مطالبات غیرجاری به وام‌هایی گفته می‌شود که بیش از دو ماه از سررسید آنها گذشته و هنوز بازپرداخت نشده‌اند.
🔹
در این میان، شنیده‌ها از آن حکایت دارد که یک بانک دولتی به‌ تنهایی حدود ۵۰۵ همت از این مطالبات را در اختیار دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/akhbarefori/679566" target="_blank">📅 00:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679562">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نمایندگان مجلس تا کجا مصونیت دارند؟
🔹
آیا آن‌ها هر حرف هزینه‌سازی را می‌توانند بزنند؟ قانون برای نمایندگان متخلف چه می‌گوید؟ در این ویدئو ببیند.
@TV_Fori</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/akhbarefori/679562" target="_blank">📅 00:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679561">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn0mddYCMu9Qypl7bf3dnxeHuTSmsETjbM1MoRUpBVrwWp-PvQPpej-wKTV3iZ1_cJX5qownEuy3fDNRLPAvWb0-RiER05bPhRM1ten6r-JtimPdIvvGnQZMmzSM9BMBmvgP-34QQfJGgKkEmhAleYTq2vwyNwMhMPkftAYhY6YTzZBe1OUXPpvcnEctZymNIihZK0-s6iYtRkN_ALn0o2oi6i075kxmNkmdAg0Q22JNRmPfHmoOU_XPZtgX1GSoIXEFsz27yzYCYdxXgrt3l-VOrxtPORAVXHF85g39kql7cPW1x3MwFijaCQpx8SamptAxhkc85ckr3Kq1UE2utw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«خورخه مسی»، پدر لیونل مسی درگذشت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/akhbarefori/679561" target="_blank">📅 00:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679560">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه نیک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecmL18F-TRFcDYFLvO9s7nnMX_yarUaGZJqckB6KsdvR42GErf7t7mziUxBE9oGOmq7Tdi0AuURp7AfabRVV9tKCdvHAEm1tqlT0SukNCqRyOYJk6jevC0GN215SX7p6Z7nyuh-SPXFJ6zKYF9Gq2XbVUfIH0xovxgBU8cJ8Dl7ClNe-yyZTvT-aAElZv9ucZz11R11cLxexn_i37PMrRWOI7VPptr8DNJC8RCiQ-fHoN24rTolLDWN7DXYdlwF20-gudEn1j4NeyETvWwObSt6-fcKIgHQwdnTUTP0Mq9FSWQO4IMm6qoOFYWe12R3300Gnsh410h5nDeTun9b7Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهمِ پرنسا ۴ ساله، به‌جای خنده و بازی، تخت بیمارستان و شیمی‌درمانی‌های طاقت‌فرسا شده است
😭
💔
پرنسا برای ادامه نبرد با سرطان خون به داروهای ضروری نیاز دارد، اما خانواده‌اش با درآمد اندک کارگری و خانه استیجاری، توان پرداخت هزینه‌های درمان را ندارند.
😢
بیایید نگذاریم کودکیِ پرنسا روی این تخت‌های سرد جا بماند.
🥺
🤲
✨
شماره کارت/شبا خیریه نیک:برای کپی کلیک کنید
6037691990491185
6280237094218423
IR110190000000216777746001
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام نیک
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
⚠️
مازاد کمک‌ها صرف امورات مؤسسه و یاری به سایر کودکان محروم خواهد شد.
💚
آدرس کانال ما :
👇🏻
👇🏻
https://t.me/+YQ8wu_Q7QahjNmNk
https://t.me/+YQ8wu_Q7QahjNmNk</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/679560" target="_blank">📅 00:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679559">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFgMt9dxYHuxp1N416757o2zmc4EHax51yoihEORJ_SojR5HIdG1Is-9bGxlPT_ODnrzffByMLYDz4ZDjylR8FGQyRZ5kFM9bgSNj4j3y7W6PRRy_F61VrGV9PxtUauT6tAH9qqLI-zSTV2csrwHhXlKbPXzFF6-UZZyfhZCsVbwQQz1RXm2pf66xP41HBpRbhW8YmOYxd6Beoytxte9uAhz5cG7A-LnsWpAWcjbvMF84bF3DX1rIbemCIQFOAPB1qlPjdXEuBE6Ms_OvGe9V_1XA69vXSe4POpcv0z_Fxy4dth_rrrJjqB_trZiFTIwnpPNdoCC0ZRLzFKyZMM4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خط دادن سناتور آمریکایی/ تدکروز: باید معترضان ایرانی را مسلح کنیم
🔹
تد کروز، سناتور جمهوری‌خواه آمریکا در گفتگو با فاکس‌نیوز، خواستار مسلح کردن معترضان ایرانی شد.
🔹
کروز با تأکید بر اینکه آمریکا نباید نیروهای خود را وارد جنگ زمینی در ایران کند، گفت به جای به‌خطر انداختن سربازان آمریکایی، باید معترضان ایرانی مسلح شوند تا «خودشان سرنوشت کشورشان را تعیین کنند»/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/679559" target="_blank">📅 00:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7aa4b748.mp4?token=JhWyVi6svHGO63cAZS69-BnQ5cMoioMXAlQGuguAEuApk05pL_itZB3G1xhgnNV9Mg1ktDRP8_wUSqe6Qz0nAltklhg61GGi5i_GsYRIhBIQs9ky_krTRo_zwV4euALE5T9JSGERi6qO-DpEfYfuH29JD49A1xP6YFHWlbu_KjU9efVrv7WUPE0Jz8X6T5BWrpeXQWlbYZRl_U87XY5eqIJ7Tiu4kqjxNz_4gHtgpGHGioK4hIDdTsmr937nqfHQtMISifnWCI7nJn9fnGQ5DMdiWN1C6D88WJOGgorZZsgoULzh8KFst77ZsXjAgsbxXF4cDn-oMCXhebJsNQDPpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7aa4b748.mp4?token=JhWyVi6svHGO63cAZS69-BnQ5cMoioMXAlQGuguAEuApk05pL_itZB3G1xhgnNV9Mg1ktDRP8_wUSqe6Qz0nAltklhg61GGi5i_GsYRIhBIQs9ky_krTRo_zwV4euALE5T9JSGERi6qO-DpEfYfuH29JD49A1xP6YFHWlbu_KjU9efVrv7WUPE0Jz8X6T5BWrpeXQWlbYZRl_U87XY5eqIJ7Tiu4kqjxNz_4gHtgpGHGioK4hIDdTsmr937nqfHQtMISifnWCI7nJn9fnGQ5DMdiWN1C6D88WJOGgorZZsgoULzh8KFst77ZsXjAgsbxXF4cDn-oMCXhebJsNQDPpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش برف تابستانی، امروز در قله دماوند
❄️
#اخبار_البرز
درفضای مجازی
👇
@akhbare_alborz</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/akhbarefori/679556" target="_blank">📅 00:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679555">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78330a5903.mp4?token=PfLxt3Bu0fZFB5uVMk-ms1SDGbKkl3WH4ofX1y_VZdWkX_Bq2X4YEbzxo1fU5rRzwU-O5S7p8Ys5g1P7amL03L25aZPKPWlmjzT-Mp4f02_xRQVn_5C83TL17jTHeb8iuyv7aZaG_XxCSqMcB34criTVQjWJb6FyxpicvGqVSoXa67VGNaylRz-oy3Q6ogVR5amJtYs2s1xxwjzf9YQWr-qarg9kqnM3ldgRB3mHqwNmL9VxBpz3FrBC-9OQ3d8yZ4UNrrYMYld6XMrZj-2tgg2OX1obJOQ0I7m_gVEvIfOSi0AGaBNttovh1NDrJBiD4Xm9PZ2dwR5ky_rnHZPaZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78330a5903.mp4?token=PfLxt3Bu0fZFB5uVMk-ms1SDGbKkl3WH4ofX1y_VZdWkX_Bq2X4YEbzxo1fU5rRzwU-O5S7p8Ys5g1P7amL03L25aZPKPWlmjzT-Mp4f02_xRQVn_5C83TL17jTHeb8iuyv7aZaG_XxCSqMcB34criTVQjWJb6FyxpicvGqVSoXa67VGNaylRz-oy3Q6ogVR5amJtYs2s1xxwjzf9YQWr-qarg9kqnM3ldgRB3mHqwNmL9VxBpz3FrBC-9OQ3d8yZ4UNrrYMYld6XMrZj-2tgg2OX1obJOQ0I7m_gVEvIfOSi0AGaBNttovh1NDrJBiD4Xm9PZ2dwR5ky_rnHZPaZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلینتون، ترامپ را به صدام حسین تشبیه کرد
وزیرخارجه سابق آمریکا:
🔹
من در برخی از کاخ‌های صدام حسین جلساتی داشتم، آنجا یادآور چیزی است که اکنون در کاخ سفید شاهدش هستیم، این بازتابی از شخصیت خودشیفته اوست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/679555" target="_blank">📅 00:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679554">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت: باید از حالت پدافند خارج شویم و وارد فاز آفندی شویم
محمدرضا محسنی ثانی، عضو کمیسیون امنیت ملی در
#گفتگو
با خبرفوری:
🔹
در حال حاضر آمریکا در مقابل هر تهدیدی که می‌کند، اثراتش را در منطقه می‌بیند و دست‌وپا زدنش بر این اساس است که بتواند خودش را تا حدودی از معرکه خارج کند.
🔹
آنچه تا به حال در موضع پدافندی داشتیم باید به حالت آفندی درآوریم. مردم آمریکا در جریان مسائل منطقه نیستند و درصدی از آنچه ترامپ می‌گوید، مورد توجه مردم آمریکا قرار می‌گیرد و ترامپ هم برای خودش آبروداری می‌کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/679554" target="_blank">📅 00:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679552">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLf7xMyH6fV4mbXwiU-4FS0bmL-16YRyyIXY9815joO_pXzq_JOa-8Q7ON1kRIhrMDyiGFNV_iV-ri5SCW8pVEChv0Zz5_2cRRM4NH515gfWONFsVyhpsd60FMkqjGA7p_etiYHkMJa2sGFI6ktYRNKTVlxiMeymP3FmuiAa84_hZxPXoX5_3iWcA4dtrQQjT_xcejW7NDa3h5MUNryuwpxMLbOVGqUK0QlLy1BEynae-idtlQVde-a1CPfQZk0wT0rUnE8r7eEtNUXsjfrB7Q4N4gMCQ4xTQXtLAQw0lJ8NmBzLab9TZAMalPpJKT48-neArs3DVK4NOo4eL6SzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/679552" target="_blank">📅 00:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679550">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8caf8f6a0.mp4?token=nDagQnFS3BJfJCZcv75izHLBdRrih5555Pb3DYRdpusVhMDQojEoDnsRKghyST2GCyOggt6ICwVrDUc9nnMhl728-EmYX04mbgXYIXeKUDM0z3VY4uJgKT9Fkm2zCHx48cASE2R3fU3KOckdW4pHycsikEYVjTOOp9KSzqgbmOi0FG4wrzlcYM1qoL_ScFpWWcAlFtp4xD-XfNbcWKMK-Nd-U7DLpa7mCcZKriWtoQj1dZZLPg0UodYLzBwY_d43hkFeyekCxv590ml6D7ZwISqKfeclanuhDFk4xF_A_mby2u2mGzwr2tHC0iHUO-AMuXEe2-iEZZeqQSD7PZceUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8caf8f6a0.mp4?token=nDagQnFS3BJfJCZcv75izHLBdRrih5555Pb3DYRdpusVhMDQojEoDnsRKghyST2GCyOggt6ICwVrDUc9nnMhl728-EmYX04mbgXYIXeKUDM0z3VY4uJgKT9Fkm2zCHx48cASE2R3fU3KOckdW4pHycsikEYVjTOOp9KSzqgbmOi0FG4wrzlcYM1qoL_ScFpWWcAlFtp4xD-XfNbcWKMK-Nd-U7DLpa7mCcZKriWtoQj1dZZLPg0UodYLzBwY_d43hkFeyekCxv590ml6D7ZwISqKfeclanuhDFk4xF_A_mby2u2mGzwr2tHC0iHUO-AMuXEe2-iEZZeqQSD7PZceUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرنگون کردن پهپاد اوکراینی با آتش رگبار روس‌ها
🔹
نیروهای روس با تفنگ به سمت یک پهپاد کامیکازه اوکراینی که در حال نزدیک شدن است شلیک می‌کنند و در نهایت موفق به سرنگونی آن می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/679550" target="_blank">📅 23:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679549">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: ارتش آمریکا به صورت مخفیانه به دنبال خروج از جنگ است
سی‌ان‌ان:
🔹
ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، به‌طور پنهانی به دنبال خروج از جنگ ایران تحت رهبری ترامپ است. کین به‌طور خصوصی درباره محدودیت‌های اقدامات نظامی بیشتر با سایر مشاوران ارشد ترامپ گفتگو کرده و هشدار داده که بمباران مداوم ممکن است برای تضمین آتش‌بس کافی نباشد.
🔹
این ژنرال ۵۷ ساله درباره این موضوع با جان رتکلیف، رئیس سیا، مارکو روبیو، وزیر امور خارجه، و جی‌دی ونس، معاون رئیس‌جمهور، گفتگو کرده و ترامپ از آن خبر ندارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/679549" target="_blank">📅 23:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679546">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حاجی‌‌دلیگانی: ۴۲ میلیارد دلار پول بلوکه شده در خارج از کشور داریم
حاجی‌دلیگانی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
بر اساس برآوردهای موجود، ایران حدود ۴۲ میلیارد دلار دارایی بلوکه‌ شده در خارج از کشور دارد که عمدتاً مربوط به درآمدهای نفتی فروخته‌شده در سال‌های گذشته است.
🔹
این دارایی‌ها شامل وجوه نقد بلوکه‌شده در کشورهای مختلف و همچنین اموال با ارزشی در کشورهایی مانند انگلستان است که نیاز به پیگیری جدی توسط معاونت حقوقی رئیس‌جمهور و وزارت امور خارجه دارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/679546" target="_blank">📅 23:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679544">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
پزشکیان: در جنگ باید هزینه‌ها را کم کنیم؛ مدیرانی که هزینه‌ها را کم نکنند نمره منفی می‌گیرند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/679544" target="_blank">📅 23:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679543">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
پولی که ناگهان راهی بورس شد؛ چه خبر است؟
🔹
بورس تهران امروز یک روز سراسر سبز را پشت سر گذاشت. ۹۷ درصد نمادها مثبت بودند و خریداران برای ۷۴۳ نماد، صف خریدی به ارزش ۲۳ همت تشکیل دادند. بازگشایی «فولاد» نیز از مهم‌ترین اتفاقات بازار بود.
🔹
در این میان، حقیقی‌ها با تزریق ۸.۸ همت پول به بازار، نقش پررنگی در تقویت تقاضا داشتند و ارزش معاملات خرد نیز از ۱۹ همت عبور کرد.
🔹
اما در سوی دیگر بازار، صندوق‌های درآمد ثابت با کسری نقدینگی ۴.۵ همتی مواجه‌اند و صندوق‌های طلا نیز شاهد خروج ۴۴۰ میلیارد تومان پول بودند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/679543" target="_blank">📅 23:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679542">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4bdbd833.mp4?token=oqTlPyNgH4umYqNLU-6aBbNYuPyX96ZLuUrGNbUMc7O2bZ8m2U1_ycaRLpyWCuAyDh3bdAh6K55P6JwQ329yguAP5FE5jB5MytgYrCLCg1XJ6eo57FBCGNIio4jYS2qZG9tg8K3bibFS02JQ6xCEA9TCUvYdbUnB3GtatrMGgUxMmjDyJcySCcoaEfhlPzW5MfYkEzpDV84sUP73CDnqVGNyYc70SpGEU1dj6b_pGQ-uQVeeG7N6_gtbxfw9vZhyVUv3OdIiUHrY1qCTgJOhos7c3ftVR8VDX6y4iKh5oBNkZePsx0nk41_PWLdtwq7K_YBHo6pe_6F2NGdtkRELXLYxehDbmiEWNDQ_SnHCAnsiYxkDDAbP_KP3H1h_RP5URl_GNmGejotJozleCOlvwYaoa_VUMPb7EDX4Vgiq7lE3ce9Lmno4LWBuz41eExv5jChLdTUf5N5TS7BFkeThfpISt0vctQ2GdjcNP1b3Ab3fef0-Jt5-DzbHii4QxQNBp0E-GBLwh5FRADJQJGK4p59uWU_Eox4wu4IlAaJ_LyjshGzyHwIwBtvsK0AdXLHt8_e80dQusXUnXAx7BbRxlSodluKcKLVcAwgfWYV0-9ugjKyvCmT7iULWYvT9bmlqs_3cbQAGEVf9qex2SQVZNevjorbpkUoyhPc-MCSA3jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4bdbd833.mp4?token=oqTlPyNgH4umYqNLU-6aBbNYuPyX96ZLuUrGNbUMc7O2bZ8m2U1_ycaRLpyWCuAyDh3bdAh6K55P6JwQ329yguAP5FE5jB5MytgYrCLCg1XJ6eo57FBCGNIio4jYS2qZG9tg8K3bibFS02JQ6xCEA9TCUvYdbUnB3GtatrMGgUxMmjDyJcySCcoaEfhlPzW5MfYkEzpDV84sUP73CDnqVGNyYc70SpGEU1dj6b_pGQ-uQVeeG7N6_gtbxfw9vZhyVUv3OdIiUHrY1qCTgJOhos7c3ftVR8VDX6y4iKh5oBNkZePsx0nk41_PWLdtwq7K_YBHo6pe_6F2NGdtkRELXLYxehDbmiEWNDQ_SnHCAnsiYxkDDAbP_KP3H1h_RP5URl_GNmGejotJozleCOlvwYaoa_VUMPb7EDX4Vgiq7lE3ce9Lmno4LWBuz41eExv5jChLdTUf5N5TS7BFkeThfpISt0vctQ2GdjcNP1b3Ab3fef0-Jt5-DzbHii4QxQNBp0E-GBLwh5FRADJQJGK4p59uWU_Eox4wu4IlAaJ_LyjshGzyHwIwBtvsK0AdXLHt8_e80dQusXUnXAx7BbRxlSodluKcKLVcAwgfWYV0-9ugjKyvCmT7iULWYvT9bmlqs_3cbQAGEVf9qex2SQVZNevjorbpkUoyhPc-MCSA3jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌پرده راهبرد جنگی ترامپ درباره ایران
🔹
اتاق‌های فکر غرب که در قالب اندیشکده به فعالیت می‌پردازند، راهبرد ترامپ را واکاوی کرده‌اند. دیدگاه‌های آنها را در این ویدیو مشاهده کنید.
@TV_Fori</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/679542" target="_blank">📅 23:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679541">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad35aacb5.mp4?token=UoxEiUyXDtgKTALqjfcZLhBktqvSuoVuXjeaXKPCV_bPTomJXcFLfQsdqhJxT9Zk8oWcf3Ghs4VjxXk7CTW1ePSCFbdYBlCgW0rvxfqwHvbS1_yhMYuGRaDHfBhEeMgeoyOLiSFSeVBNcvO5aFvn7liHSyBdyNLxWYG0ciUtNbrrXFzqoRK3eDNzylOTqLAEF2eo6ttANwfuvSCzJyMa_A5ZlYGMVSnG7aD6IN7FzI3QRbwhnjFMXEOtyeTQajXTeEJjD2zRd5RgYr-dpjPIDDADlMyJGlMUBa9ag4bOVH1E7xYoBPSiokvHYytaoYHLYkYZuBCWEvsl5ra8KQOQfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad35aacb5.mp4?token=UoxEiUyXDtgKTALqjfcZLhBktqvSuoVuXjeaXKPCV_bPTomJXcFLfQsdqhJxT9Zk8oWcf3Ghs4VjxXk7CTW1ePSCFbdYBlCgW0rvxfqwHvbS1_yhMYuGRaDHfBhEeMgeoyOLiSFSeVBNcvO5aFvn7liHSyBdyNLxWYG0ciUtNbrrXFzqoRK3eDNzylOTqLAEF2eo6ttANwfuvSCzJyMa_A5ZlYGMVSnG7aD6IN7FzI3QRbwhnjFMXEOtyeTQajXTeEJjD2zRd5RgYr-dpjPIDDADlMyJGlMUBa9ag4bOVH1E7xYoBPSiokvHYytaoYHLYkYZuBCWEvsl5ra8KQOQfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: چه کسی در حال حاضر دست بالا را دارد؟
رئیس سابق mi6:
🔹
ایران؛ از اینکه به این نتیجه رسیده‌ام متأسفم
🔹
در عمل، رژیم ایران مقاوم‌تر از آن چیزی بوده که فکر می‌کنم تقریباً هر کسی انتظار داشت. آنها در واقع از همان ژوئن گذشته تصمیم‌های خوبی گرفتند؛ از جمله پراکنده کردن توانمندی‌های نظامی خود و تفویض اختیار استفاده از این تسلیحات.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/679541" target="_blank">📅 23:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679540">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
عراقچی: تعیین مسیر جدید دریایی میان ایران و عمان به معنای باز شدن تنگه هرمز نیست
وزیر امور خارجه:
🔹
وضعیت فعلی نتیجه نقض یادداشت تفاهم از سوی آمریکاست و این کشور باید موارد نقض را به‌طور کامل جبران کند.
🔹
دخالت آمریکا در خدشه‌دار کردن حاکمیت ایران بر تنگه هرمز، خلاف مفاد یادداشت تفاهم بود.
🔹
ما تحمل نمی‌کنیم نقض یادداشت تفاهم بدون پاسخ بماند یا حاکمیت ایران بر تنگه هرمز به چالش کشیده شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/679540" target="_blank">📅 23:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679539">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35bd9022f8.mp4?token=uO5_vsfRcq3rgD-v1vSqn9mOxvLUbe0GSl2Qt66gXcOCHm3IQNEKVnl8Hw1nlHaHpA07kGfYSqlb3J0zwjZ6pSiFUP2YxahRYEOivVRgb4zFXzK4tS628_B_GNzmySfPTony06b5C1EHZtVEZ4DfLynriiyYHjEeeDBGFxTew80hOTx23xHIH_jAr7LFD2NKnW82ojibFIJAcUfMxX5wNwjwNgdQbzPkObFo9HMdgHBYSS_ngrmnGJIvqNx9w5cVLio4yeqXrnF6aR15ymf_mKt-_sqrHY9n5L5mg5ean3IUq1hRgOajZJ0TNRXlxHkDEEU3rM3Jr_TuIQKhiX_U6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35bd9022f8.mp4?token=uO5_vsfRcq3rgD-v1vSqn9mOxvLUbe0GSl2Qt66gXcOCHm3IQNEKVnl8Hw1nlHaHpA07kGfYSqlb3J0zwjZ6pSiFUP2YxahRYEOivVRgb4zFXzK4tS628_B_GNzmySfPTony06b5C1EHZtVEZ4DfLynriiyYHjEeeDBGFxTew80hOTx23xHIH_jAr7LFD2NKnW82ojibFIJAcUfMxX5wNwjwNgdQbzPkObFo9HMdgHBYSS_ngrmnGJIvqNx9w5cVLio4yeqXrnF6aR15ymf_mKt-_sqrHY9n5L5mg5ean3IUq1hRgOajZJ0TNRXlxHkDEEU3rM3Jr_TuIQKhiX_U6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: برخی توقع دارند در آمریکا و اروپا گرانی باشد اما در کشور ما که در جنگ هستیم گرانی نباشد؛ این در ذهن من نمی‌گنجد
🔹
وقتی در جنگ باشیم کمبود پیدا می‌کنیم و باید برای مقابله با سختی‌های آن آماده باشیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/679539" target="_blank">📅 23:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679538">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
واشنگتن‌پست: هزینه هر آمریکایی برای جنگ با ایران ۱۰۰۰ دلار شد
واشنگتن‌پست:
🔹
ارتش آمریکا میلیاردها دلار هزینه می‌کند و هر خانواده معمولی آمریکایی به خاطر این درگیری ۱۰۰۰ دلار پرداخت خواهد کرد.
🔹
هزینه‌هایی که بر دوش مالیات‌دهندگان و مصرف‌کنندگان گذاشته می‌شود، همچنان در حال افزایش است و فراتر از آن چیزی‌ست که تاکنون به طور کامل محاسبه شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/679538" target="_blank">📅 23:17 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
