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
<img src="https://cdn1.telesco.pe/file/bkL9TdiPCo6d_SLB2VyLherJZwzgbGk2vaq0T24Zi_8z7N5WrUQIHbVbnRU4BP0AR8S1f7eB2RARuckkwiG0-Pf93FJjJmzTNBUzldKbAIvKdSYhMqVkOB9ZChnX-cgCfK59cp2FqApAqktC-RdrJHCLysYXqPT-UgekbOwsAW13GFJbtz7KTi-PCkE4jBUX3HonFTGw0AkZVkfxRA4HQejeu9lI_mLD02XkI3NmGOOy76TRRS_1xrGxbXGYRGG4AruG3L6T68P591tUOuKq6aufyc1LiPoj9sAjiyWWN1dpZa8cWdGFQGyYH9J0oXti_OLrUD_DLpuIBnh4uefwqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-2677">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">توی یکسال اخیر فقط در یک نوبت ۸۸ روز اینترنت رو قطع کردن، بعد با
وقاحت
از ضرورت مدیریت مقتدرانه و شرایط جنگی حرف می‌زنن، انگار بقیه سال اینترنت برقرار بوده!
اینترنتی که ازش حرف می‌زنن، یه شبکه وایت‌لیست‌شده، پر از اختلال و محدودیته که حتی سایت‌ها و سرویس‌های داخلی هم درست کار نمی‌کنن و اطلاعات خصوصی مردم کف اینترنت پخشه! اسم این وضعیت رو هر چیزی مثل ملانت، آشغال‌نت، ‌اختلال‌نت میشه گذاشت، اما اینترنت نه.
اگه مدیریت شرایط جنگی و بستن پروازها رو بلد بودن، فاجعه PS752 رقم نمی‌خورد. اگر زبان انتقاد رو می‌فهمیدن، ده‌ها هزار نفر توی دی‌ماه قتل‌عام نمیشدن؛ اما دست از سرکوب برنداشتن و برنمیدارن!
استارلینک هم نتونستن متوقف کنن؛ همونطور که نتونستن (یا نخواستن) جلوی فروش IP سفید رو بگیرن و بازار سیاه برای کانفیگ‌های گیگ/میلیونی شکل گرفت. همونطور که سیم‌کارت سفید رو به نماد تبعیض و رانت تبدیل کردن.
از جاسوسی و فرماندهی دشمن حرف می‌زنن! دشمن کیه؟ مردمی که می‌خوان به اینترنت آزاد دسترسی داشته باشن، یا کسانی که با قطع ارتباط مردم، رانت‌فروشی و تحریف واقعیت، اعتماد عمومی رو نابود کردن؟
بین ما و شما دریایی از خون فاصله هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/ircfspace/2677" target="_blank">📅 08:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2676">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I2xH_KzuQOmfBnItoSx3JrxIGzgXMJbvdalK0gpi1fM-nEAaN445O9mooazvWoKGgB8q25slLoLWWwjrb-SlpO7wAyH_H2qQpJM1qDayfEXdGQFoh77ePUUzuEAQfU6CBMP5s66TFN-by6IRX2QcBFfu68Qty1jFkqGfDSM0JcoV0Yj4ACECWokwjrOKubAVe7EbpHmdZJgaIlQFneLSH5iIhjNHMmhEXhT921lXwP0s_ZV9mox3zbIvRwqWpBRd_EaUINXbrHj_LoVpSsHxKPtFQwHQZl3HXnJW_N-ymGR--RaNiW-Cd_AaWP4ZAgOJ0v6EKxJljLlSONLzORgCfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه اظهارات
گوه‌هربار
آقامیری، دبیر شورای عالی فضای مجازی: به نظر می‌رسد استارلینک بیشتر ابزار جنگ است تا ارتباط؛ برای فرماندهی و کنترل دشمن، جاسوسی و جمع‌آوری اطلاعات استفاده می‌شود. فناوری‌ای که نه قوانین را رعایت می‌کند و نه رویکرد خدمت‌رسانی دارد، مسئله‌ای جدی است که باید مقتدرانه مدیریت شود. ما هم سامانه شناسایی پایانه‌های استارلینک را داریم و هم فناوری‌هایی برای قطع ارتباط. متخصصان کشور بسیار خوب کار کرده‌اند؛ محصولات آماده و آزمایش شده‌اند. در دی‌ماه از یکی از این فناوری‌ها استفاده کردیم و ارتباط آن قطع شد.
ما شبکه ملی اطلاعات داریم، اگر اینترنت بین‌الملل قطع شود، هیچ دستگاه پوزی از کار نمی‌افتد؛ درحالی‌که در فرانسه سیستم‌های پرداخت از کار افتاد.
تنها یک‌بار در دی‌ماه، برای چند ساعت اینترنت را به‌طور کامل قطع کردیم تا مسئولان امنیتی بتوانند صحنه را مدیریت کنند. بقیه موارد صرفاً محدودسازی بوده است.
هیچکس دوست ندارد اینترنت قطع شود، همانطور که هیچکس ترجیح نمی‌دهد در دوره جنگ، پروازها بسته شود اما چاره‌ای نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/ircfspace/2676" target="_blank">📅 08:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2675">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gL3_qN8dKdxAcgUQQf2JgouwAFX1ZjMl_7UoKHM1aYO4CK9xXvlAV8IiPA72Hrp5k1gAE1iooGbj9uXMtI2kqWC_N7uP4NyV6ZKEig3iUWn598ScAsHu8LCjO6Y8KcGUjVDsJVAcSoBV5Hrs98BDJ2E3cQ6jPULGNDGprwHwKCcNY7EJ7hd_KBVDNjtEin6_XYiP7U_7H42o0dhdmgzA2JIRtKzXH8tJjWlNvn5J_abEwvtLUh_gcMFfgqgFEQ26QzFKKqBO2bZmGf_mdWYiUzyWsZ5sTHXz7z8PvlRstoUXgjDX7D5qgLHVry8XMmL-98PSNIWJjQJnXMjFzo_aDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهاجرانی، سخنگوی دولت: دستگاه‌های متولی به‌جهت اهمیتی که پایگاه‌های داده ما و خدمات مبتنی بر اینترنت دارند، گاهی مجبور می‌شوند سرعت اینترنت را پایین بیاورند!
این موضوع را اصلا انکار نمی‌کنیم؛ اتفاقا اعلام می‌کنیم که در راستای صیانت از دارایی‌های کشور است. /رویداد۲۴
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/ircfspace/2675" target="_blank">📅 08:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2674">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7cd1369485.mp4?token=bdaWZCHZeBnLqaCo9aM8ECteQydkW9SecnpS0CRUfP7g8CGWIMM-gN1J-hBDr8JWWZFHZI8wO8jaC5mt_W1HskZ_SNMnq3VyNO99kZTkLwjkKUFjz9XpeLoQ1uFhvTEk86L9gO9cUKwbKZsYsZ2Xwz2CLlKBnH9Mn7EBbE53zvCz-X7n60gG1MfATzt3812lyUIMfoSCU_MHdmfwrkBLoYLydQschRAI9wwp6ayi_RHkpey22DaXMmVUZU1JabGcT8QfrMrORs93EzRKwApyTYFihlKfdmob2uJpxhUGWLVddYa_BV2wUeS9d_zVD6_3bZ8fga76RisdjVrreP5eYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7cd1369485.mp4?token=bdaWZCHZeBnLqaCo9aM8ECteQydkW9SecnpS0CRUfP7g8CGWIMM-gN1J-hBDr8JWWZFHZI8wO8jaC5mt_W1HskZ_SNMnq3VyNO99kZTkLwjkKUFjz9XpeLoQ1uFhvTEk86L9gO9cUKwbKZsYsZ2Xwz2CLlKBnH9Mn7EBbE53zvCz-X7n60gG1MfATzt3812lyUIMfoSCU_MHdmfwrkBLoYLydQschRAI9wwp6ayi_RHkpey22DaXMmVUZU1JabGcT8QfrMrORs93EzRKwApyTYFihlKfdmob2uJpxhUGWLVddYa_BV2wUeS9d_zVD6_3bZ8fga76RisdjVrreP5eYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک لحظه زندگی در ایران
©
geedook13
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/ircfspace/2674" target="_blank">📅 08:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2673">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uw5OAalLcD1z6UNoa5PgN3_NGQphCmjzJjL9GpEK7tO09KxcPSAJZttvRGcGBNvQ5pFzDYliO1Gaf4Nb-DACtmeH3HmQRFVn90dcgJ789BuyPOhsaULiOZ7E3Pg-X1GUaS3Op1OWgHTIOz59KbHv9q-Hqutwa9dqSCHjif0WlJ3DR4BKDHr4JEcbbqhCbE5c5bVvWYUrMUn-FnbQmgETUQ_s4a3EB7dO7ztFrnnfGa0MeNB4ja1cLt_PporA0yprZXqbP9FF1RSrseAEOcgQCJzz2NqYX_Kx_v1KvIwn6BT6Q33iWUpWZ7hdARAo1TF8gycqcqtseMyWyYYAblW1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسدودسازی سیم‌کارتها اول در رابطه با روزنامه‌نگاران، منتقدان، فعالان سیاسی و فعالان مدنی بوده، اما حالا روایت‌های تازه‌تر از گسترش این مسئله به کاربران عادی، صاحبان کسب‌وکارهای اینستاگرامی و زنانی حکایت داره که به دلایلی مثل حجاب با مسدودشدن خط مواجه شدن.
شرق در گزارشش نوشته که این موضوع به قطع تماس و اینترنت ختم نمیشه؛ بلکه رمز پویا، حساب بانکی، خرید اقساطی، درخواست تاکسی اینترنتی و حتی دسترسی به حساب‌های کاربری و اداره یک کسب‌وکار آنلاین با این مدل اقدامات از دسترس صاحب خط خارج میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/ircfspace/2673" target="_blank">📅 07:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2672">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DQtsOWPPzqCTbI_SK0gmj51_S-p4e43DgEi4-X76_QjMBSaoYENJ2PVtr1zNnjSqvAvuahx183N476FpnrTaXkrq0r_W2bPO5fLEqDXrBUK_nOOtyqu4N-1UyeH4o0xueBHex1nmWwRBeB25DuMNNLr3SSuO7bpxwBEsgeBu6a1taea9T9gYZaxhaZu2An0EqllU2BRTHUGc2cRZZDh2PJedu_utedjVGG8JORGAs2H72YY4xaq-skMwra3DlUUC0taERiwOY9FZz9oYiiw9cim_Y8ljIn4Vqf9-pAFiemRG508gaQP1lCP8BFK5i2ZkUB-7CTaxSJGoMhqL6fchVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلد مارشال محسن رضایی: در صورت ازسرگیری جنگ به کابل‌های اینترنت و دیتاسنترهای خاورمیانه حمله می‌کنیم /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2672" target="_blank">📅 22:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2671">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bh69suXM2ndn2iJsyM3k4fJNwf2HI6s986hyggqoZSGGjetCLo5HRuU8Df9HuOnMxR3D_HPwdq1ZXvVkmjua_hSZUM4Bm3snMfbnxB3JLmUwqC2jXVC58WJXThe7U6WmuRXUasNC6QI1Ufs5g8uyEqI1Zg6SZXqm3c7_6oC1A3mRuyxxIlQek2z_IpX3Riz4uLYSeDko_w-KqFA4ZpmnUNqOKSxwl2j5XwFDJojsovTmlAjiede554X2AW_PH57IYLtdbzaroqsGhMcVHfRjIwadVpkyDktlFtmlqyyOmETmR9hhJIEsBPYwlw9rU8eLdsgwUPsX8RKd3UI3yeSlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که در زمینه
محدودیت
دسترسی ۵ پلتفرم رمزارز به خدمات برداشت غیرحضوری بانکی وجود دارد، اختلاف بر سر نحوه دسترسی نهادهای مسئول به اطلاعات کاربران و ضرورت مشخص‌ شدن هدف جمع‌آوری داده‌ها، حدود دسترسی به آن‌ها و مسئولیت حفاظت از این اطلاعات است.
پلتفرم‌های فعال در این حوزه پیش از این گفته‌اند که بخشی از فشارها و محدودیت‌های اعمال‌شده به پافشاری بر حفظ حریم خصوصی کاربران و خودداری از ارائه اطلاعات بدون شفاف‌ شدن شرایط دسترسی مربوط می‌شود. /زومیت
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/ircfspace/2671" target="_blank">📅 22:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2670">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DhPtv8K6S9MRY69Gs-fRiXAgtp_b6i9hrCXx7YvxUVGX5oeCdlhI-kZakJZ0TDtpxXaTOHEZsw9c4vPORgeKC4ybIBEhRY9KmCsvv_II5S1mTPybak6ACPQAgP34lCsDjJwyb30x6Vuq1C-qARAOZ1tno0WMSDQGmLvrx61g34ciRYahLb2qgOpi-E77CzSxcmwc1TGJygxt4QMWvGvLwmO0YMffWyNgnDXQe4CMMHKnNDcf-rbVVb0hjTo9XZpy4512qtcX0d6NdNfWWDWZR3NJsZ5uJ_zDqAS1E154uTXBjNEq3onKHJrDyJ-jAGgg1em1NyytyiD6M-I9yp-XOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌بانک مرکزی تسویه ریالی ۵ صرافی رمزارز نوبیتکس، بیت‌پین، رمزینکس، ارزینجا و تترلند را به مدت ۳ روزه محدود کرد.
دلیل این تصمیم تخلف از ابلاغیه مربوط به API اعلام شده و می‌تواند فرایند برداشت و تسویه ریالی کاربران را با تأخیر مواجه کند. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/ircfspace/2670" target="_blank">📅 21:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2669">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rEX2bJnfnz-TqrSknX4DylyVolEyB2u9gGfJRYyN7ayZlWXeupe3iRp7PIcQkcO9VubFGcfMH3bffHkHAB_YXq5WFNgEIYPU4fojxLLZaJTTdljUZ3PAdeNNFUnmw2hIhfHtLjfxYTIRBKto5shXKzKPL0RscURUVI-2xhFnPmuYH2GxlmsfhERf4MMP0qb3dzFROkUvw9C7xECE03-9bu_BU9KKJxpUlmvt7uH0HMGuSJmLRhlHVChREU64210Mrr60RulSqbTPRb9Zg_R473IlVqn_a_ZfvCTpP2pOf_3sFSW35bMkM5BEAmvWMFq4L2E5vmmpLUEnhjiwEwtf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن متن‌باز و رایگان PyWarp که برای ویندوز، لینوکس و مک ارائه شده، امکانات بیشتری برای مدیریت اتصال از طریق وارپ لحاظ شده.
حالا می‌تونین بین پروتکل‌های وایرگارد و مسک سوییچ کنین، مسیر اتصال رو هوشمندانه‌تر مدیریت کنین و از تنظیمات پیشرفته برای سازگاری بهتر با شبکه‌های محدود استفاده کنین. امکان مدیریت حساب‌های شخصی و Zero Trust، مشاهده کیفیت شبکه و بررسی خودکار بروزرسانی‌ها هم در رابط کاربری جدید این‌برنامه قرار گرفته.
👉
github.com/saeedmasoudie/pywarp/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/ircfspace/2669" target="_blank">📅 21:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2668">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tBJT966AjP7rWEOxmzRryk-v1BO4Yjj5cDSG-MeRVh_04Ml4qajeu1qe5Goq087JMj5doS6YItR_7D4wpZ7wLwYJOWEoCoqSBZEQzrSH12Q_3yGtL9MvzrVi7P7p67S-vNKXiiUcFfqZ6yH-doIyvNqiG7HxlucfGdRSyAcdHYq8NZ90uoAbL15AsAv4S1TNYY6w6svcGLis8CIJ8IPHEA7AnMSmjYGSze3InaNml9aoDTWJpcoddHLe22qnN969AS4cCKstW7STxQBFF2K07gU2KruTVUuZkA6y_nA7hIKRVWl-DFwI5ofEf-yXVbIxNm86nlMxnFKotkBhC75qFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی حماقت امثال شریعتمداری حساب باز شده!
حسین شریعتمداری مدیرمسئول روزنامه کیهان: آیا حق مسلم ما نیست که برای به زانو درآوردن و قطع نفس این جرثومه‌های پلیدی، مانع عبور کابل‌های اینترنتی از عمق آب‌های خلیج‌فارس و تنگه هرمز بشویم؟ کابل‌ها برایمان دست تکان می‌دهند و با هزار زبان می‌گویند چرا نقش ما را در این جنگ فراموش کرده‌اید؟ /اکوایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/ircfspace/2668" target="_blank">📅 21:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2667">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J5xQaPRkT6Ck5Jy0AlG6BlNjwEsSvNBIGJDaAIYyxk2qCsbG7nHh7G_9U3mXvYXBQHxa9GIkH4uhPlO4GouBU8ccsb7ERpaUVGEEVHqOa4KiexfaAe5mHX1EW9cYXBjV7aaPhTwltwMtTW18ZvvBRS3jiVU7tuXZu3hOvVKPGllyW5GTawxqZXovZJCWHumuPRiFnIEO2h0V8BKznCXDv_Php8cZHHbJjlbeF4iAx-mDO4Y85H2liqgqvX4Zk-RFW5ezJdcCEIvK_G80Xc2TgviUpnnYpKiA8Cq-mbsa8alPVVZkXGEHvDgXPQ1_rMsJ2zwKoweUYZ76K3itttUcfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه CLI ابزار متن‌باز و رایگان GNet برای ویندوز، لینوکس و مک منتشر شده. جی‌نت که قبلاً بعنوان یک اپلیکیشن اندرویدی شناخته می‌شد، حالا با نسخه خط فرمان، امکان اشتراک‌گذاری اتصال VPN با دستگاه‌های دیگه رو هم فراهم می‌کنه.
با GNet CLI می‌تونین سیستم خودتون رو به یک سرور پروکسی تبدیل کنین و اتصال VPN رو از طریق پروتکل‌های HTTP و SOCKS5 در اختیار دستگاه‌های دیگه قرار بدین. به این ترتیب، می‌تونین ترافیک گوشی، تبلت، تلویزیون هوشمند و سایر دستگاه‌ها رو از طریق اتصال VPN سیستم عبور بدین. این اشتراک‌گذاری از راه‌های مختلفی مثل وای‌فای، لن، هات‌اسپات، اتصال USB یا ... امکان‌پذیره.
👉
github.com/frank-vpl/gnet-cli/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/ircfspace/2667" target="_blank">📅 07:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2666">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MpQWg8eeITnSP_RrPTolJ9DmXX6nzHDtrsRzzGWTJW8KWFpGoUf9m49vxctTs1E7KxzjxIZzwy8XXSr__cVN7tPvYwwuwptU6ns9f0Xa1sqNoQUU7Q_boFr47ElbV1fqvwxrO9_oU0wZ47EN-02nKhs7dIc4XY1tCTzJFo8ax8kLkEd5bygprFAv7YDbT_5VvaMM-oSyGmkaDIFOJBI3XK2w2FwOyc1F2vus89p9LHEoQOj_p5K2HqXpb0gvSTqJvjE1RgLg9voyUfaxwJCUdJu-EDoggK1GxMgvlXI5_hTa5eYbgNr72dj8-ohkMF-X1aVHaD42c5mKhmLDqDJtiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست در گزارشی نوشته افرادی که از داخل ایران به ChatGPT دسترسی داشتن، با استفاده از هوش مصنوعی و هویت‌های جعلی، نزدیک به ۱۰۰ مقاله درباره جنگ ایران و آمریکا تولید کردن و تونستن بعضی از اون‌ها رو در رسانه‌های آمریکایی منتشر کنن!
این افراد خودشون رو نویسنده و تحلیلگر سیاسی معرفی می‌کردن و از ChatGPT برای نوشتن مقاله‌ها و حتی ایمیل زدن به سردبیرها کمک می‌گرفتن.
طبق گزارش OpenAI، هنوز مشخص نیست چه کسانی پشت این عملیات بودن و شواهدی هم ارائه نشده که نشون بده مستقیماً توسط جمهوری اسلامی هدایت شده. این ماجرا نشون میده هوش مصنوعی چطور می‌تونه برای فریب رسانه‌ها و انتشار محتوای ساختگی استفاده بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/ircfspace/2666" target="_blank">📅 07:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2665">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XRWkPWfOSLlk2Horl9J7eZuBGIIxcfqX53Y1xrimPCbLA84JKyunUScdKPruINxW9aSLFFvrGnq0gZHmXyyuxqpkbF9gvM62nrZoFvKOOam5omdSp4L0UDxkS40BlHOdJhPwKf9I7pBTpscOH7_Eau81AoPr4TchDpF9y-LMKPbzPJF4lA4dyJJ1tQjxUOjY93L4e_sFdkwR4h1rZ3f5vg-8U-gZg2bqiTlT4Y85L3KSqYuMpX8SyK0vhl7OhbgUdej8kuof0JQR9z8xlcatrvD0sY0P8zXnHSf-jgcOdJ3TsEtAnwnLEGJbg3w3DMrifX6Jxgg6ERTogj-sn0pKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانل WatTunnel یه اسکریپت متن‌باز و رایگانه که برای انتقال ترافیک بین سرور ایران و خارج طراحی شده. باهاش می‌تونین پورت‌های TCP و UDP رو از طریق یه تانل رمزنگاری‌شده منتقل کنین و اگر این پورت‌ها مختل شدن، ترافیک رو از طریق ICMP عبور میده.
این اسکریپت از روش‌های مختلفی مثل ICMP، TCP، UDP، TLS، WebSocket و gRPC پشتیبانی می‌کنه، امکان استفاده از کلودفلر رو در اختیارتون میذاره و مدیریت همزمان چند تانل، تغییر پورت بدون قطع اتصال، پشتیبانی از ICMP معکوس و داشبورد مانیتورینگ از قابلیت‌های دیگه‌ش هست.
👉
github.com/JohnWatsoon/WatTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2665" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4RQtjeWVH7EL-umCcmNdqqLXMYyBCG75BYgTsYi7d3Ccbmf6blGLrTigml_uBVgNYGDghYUu54U5maUuCHIpZHQOyvfWoQXb1Ncp9oaf-ehVSvuynN_TjgU7RO7ge_N4ymr5CCeOVDGsvoyyUvvvKFnH7qBGaxms0CykREkLtfMzBGaS_8gVTBg7TY0YQ5PZc3OMR5M_CGvnbmTf-m8RAE7X8mBCYM_qTWZo_qRilPYPcfXBP6nfFCmNW-lBNmUZexU8amtHm8Fi_-9mDAvkH8M6tykPwqFmlTELfPRfsv92-s24UZPxxOPuzNHcnYzDWrAFnV23k-X0p96_PXgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون توسعه شبکه ملی اطلاعات وزارت قطع‌ارتباطات: اگر جنگ یا ناآرامی رخ دهد،
احتمال دارد بار دیگر شاهد قطع اینترنت باشیم
؛ اما مشخص نیست که این موضوع در چه سطحی انجام شود. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2664" target="_blank">📅 22:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KrWRogYuh2GLZ9Oew8wMxXIYZNPspSmvYX6GAfKEZ4gUe5TrDH-qVWmPto8pGskXltW2d2U-8fYdo91Ln_DHHeG1gdejuY4srFd56eNxgp8bT7j2dkRHzFV9IYGlIlgN8cgQ5CE-pf8QX_4eMNjql_QTWqhosnz5iakkCD3q5YFUvqZaSSDFqcflDd30WkmfbfKTyyToafLPXWkjW_3j9yB8-dDMfJO_W3GfiRoefJ4Rx2nWfcBPBpcAisVLpS_fGm1wIdOmtTYKFdBOf2LkCWd_4ZS3kseFULpKDMUj9fLsRv93uvuoqb8Z_IQNu0slLWOfgjtoSsZ43988rFrKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخیرا یک آسیب‌پذیری امنیتی مهم با شناسه CVE‌-2026-‌107181 در تلگرام دسکتاپ شناسایی شده، که باعث میشه در نسخه‌های پایین‌تر از ۷.۲.۹، با کلیک بر روی یک لینک مخرب خاص، امکان سرقت سشن و تصاحب کامل حساب کاربری تلگرام فراهم بشه.‌
تلگرام بی‌سروصدا این آسیب‌پذیری رو حدود ۳ هفته پیش در نسخه ۷.۲.۹ رفع کرده و لازمه حتما اپ دسکتاپ رو به آخرین نسخه بروزرسانی کنین.
👉
beaksec.github.io/posts/telegram-desktop-one-click-account-takeover
©
MilaDnu
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2663" target="_blank">📅 22:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2662">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LwMzp-UbeTCTMO1OiRTEKTPjPHa7HVDVHTH9gnjcMWnSbUEWlAvD8sy1H8QQo4FWoBMiVKBulKIjV7Zaj70eEhAZ_fBYBwyhti0Vge83_Kvfa8j-PDe9Kj5pfH_jWDKuI53tQjMPK4iHnIAXltJ88OUFlCKqoKRvGPTEovgR_Hp2vt45xeiiUt0yCoxG8_ySC6b3LToR5TdZElO2hoJDuibbn5A4mUMSiSa3OdmYnzKOT2kjgKmppfjmx5O3pmql4exWsIxl79ovljiG8ykkUi6Ut4L6pKSI9SC3JoG4UZGi8uqKW6Kc3rAXSKcTXXEJQGfi9AS1yj4K5NJ9iWfCag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل NoRoot VPN یه ابزار متن‌باز و رایگان برای راه‌اندازی کانفیگ VLESS/XHTTP روی هاست‌های اشتراکی معمولیه، که فقط با PHP کار می‌کنه و برای نصب و راه‌اندازی به دسترسی روت، SSH یا باز کردن پورت عمومی نیاز نداره.
این پنل از هسته واقعی ایکس‌ری استفاده می‌کنه و ترافیک رو از طریق یه اندپوینت PHP عبور میده تا حتی روی هاست‌های محدود هم بشه با هزینه کم کانفیگ VPN ساخت و مدیریت کرد. اگرچه باید سراغ هاست خارج از ایران برین، اما این روش به معنای ناشناس‌بودن یا تضمین امنیت و حریم خصوصی نیست؛ پس بهتره برای مصارف شخصی و محدود ازش استفاده کنین و مراقب اطلاعات هویتی، آی‌پی و ردپاهایی باشین که ممکنه از طریق هاست یا سرویس‌دهنده قابل شناسایی باشن.
👉
github.com/mr-r0ot/NoRootVpn-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b-tSciRcm2Uudk58A7afJUhj0dUhKP422n_V4_WTMLgOn39w5c-f6CyQeWcq9AejSRSEKjTQ6cLfIXjHrX_xi-9kWrzZMQLbhng_UnYFY3hLOT6NAiGFNkdnrFjhKjgbPTrv_Qk1UtHbjyn6lQNQfYb71iX0vwPbUAQwNXwfWpHiEaj_fYj-OApKJLWyQjiSoIXAFai5qyxUIVSeUTbiypNRNNEJfIRtP6ZC0BQKHwBkun9yY92_AlAszGv1yumqKroOa6lJQ4hYSaPKv-fn4iuXKtQtFipkP6cUzhJsHBmJcC82U1iriOpzNQY887a8rY2qr-bL-ucEJiaDnSzX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌کوچه در مورد Jet VPN که بیش از یک میلیون بار از گوگل‌پلی دانلود شده، گفته معماری این فیلترشکن دارای آسیب‌پذیری‌های امنیتی، با شدت بالاست!
این گروه قبلا در مورد خطرات استفاده از JumpJump هم به دفعات هشدار داده بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CgwP1To6McJAe5jpsxZYSD8E6jqv7N2z7PiLKg53CKu6jU-JbIOBEbQLlMHTE1zrga4PJvVOi011cUcsCSZR06sNfu2-fLvJoimkbqUjEhhNuXDHChSiF_IZHhZSklzr9rZG-nVPdMW8q_ceuYy5x2MZa8lqIJqMzV4FSxGcgJWZKpXrMAEWR7p5Qj_VZogLDKaxrYjQb15O4CYDe9uGH_qNTvTHEZbFfanuJVwOCVM81ygO49_PUO5Qc2KN7jsOk7SS_kHZDhvI-XWNbeD0-kIngYJ2FVbuXLCdnTXNf9ybRU0tZLdRXHzlX60ZiuJ41sEjDdwEFZK71xlpy2Qm-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاونت توسعه بازرگانی وزارت صمت در نامه‌ای به پلتفرم‌های خرید و فروش آنلاین طلا، از آنها خواست اطلاعات کاربران و میزان طلای تعهدشده به کاربران را به‌صورت کامل و صحیح، در قالب لوح فشرده (CD) به این وزارتخانه ارسال کنند.
در شرایطی که شرکت‌ها برای حفاظت از داده‌های کاربران و زیرساخت‌های خود هزینه می‌کنند، مشخص نیست اطلاعات کاربران پس از انتقال روی CD چگونه محافظت خواهد شد؟ /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCOYTfvAzDmsfcx_cDMNjwW11_lpnH7zH8FXyMCN_UNtpOFF0QnHJ8LQ4BFO87oK4LeAzI_y-abDz8R4ZnaYZmRuXMRn9XrQaEAhpfCtNGC1Z0cbxpPmxR4ZuUDTYBb3ENI22aPr1gSYEmoCinwmJZHWhdcbvq_sLjo65k9zoJHcRYyAJLBBnsHgtxbKtFkN93UkZoLZDiJffjquZP6I1beyR6ue-rc-fghNZOErqVkpu676t_1siraqFa7Eezih0V4kGGy1oOPoYuxLzn6EtcnSlSRMJHuh1CbswgNQ3zYEF_qTdpHtshnf4c7Y8529DGbNM4gd6xEgtbUv19ADyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه Void Verge مدعی شده با توجه به تغییراتی که دارن توی شبکه ایجاد می‌کنن، اختلال‌هایی که روی اینترنت و همینطور اتصال VPNها دیده میشه و مهمتر از همه خبرهایی که به گوش میرسه،
شبکه زیرساخت برای قطع خیلی از پروتکل‌ها آماده شده و فقط منتظر مجوز برای اجراست
!
روش‌های مبتنی بر کلودفلر، ایکس‌ری، سایفون، DNS و حتی تور جزو روش‌های اصلی اتصال فعلی هستن که فینگرپرینت شدن. تجربه جنگ‌های اخیر هم نشون داده روش‌هایی که عمومی شدن، زودتر شناسایی و مسدود میشن.
این گروه معتقده در چنین شرایطی به جز استارلینک که البته دسترسی بهش محدودیت‌ها و چالش‌های خاص داره، به مرور باید پروتکل‌های ناشناخته و ایده‌محور جای روش‌های اتصال فعلی رو بگیرن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S6TNoxNdrdVQFb-Ruy4TrgRDn051VbmGRRB4vGkWlpwLqo-MfoPeDt1VOrv4bOUsTTRh3D3wnwI7zGy8JmXB4ORPd02L7oBuYmsM7sJlT_aIx1oW0_xChqHbZoXTejqdwrC4m8SPUTHi__DCtn9wvJKaqeFQrlJ_JACQYsAJnK4tJ5jBap1SuwsGikBPUz1ijeZ2iJABAhhjif-mnHjv_YllVreZ5L8IZ1qvNGkoLx0OH3FFrtMZn__VQUYszeAqS5BjdjS7nOK4-Z4BFu6-eXafOzeWRaO5vwDN4PGX5_2FdCt9xW4cw9591AaqBHo3wvL7V6ZDn7L2tAoO0bERUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت متن‌باز و رایگان ZedSecure آپدیت جدیدی برای اندروید، ویندوز، لینوکس، مک و NixOS منتشر کرده. در این کلاینت از هسته‌هایی مثل سینگ‌باکس، ایکس‌ری، اسلیپ‌نت و شیروخورشید پشتیبانی میشه و در کنار پروتکل‌های DNS، امکان استفاده از OpenConnect (سیسکو)، IKEv2، OpenVPN و AmneziaWG فراهم شده.
همینطور OpenConnect روی دسکتاپ بصورت VPN سیستمی قابل استفاده هست و امکان اجرای زنجیره‌ای روش‌های اتصال مختلف اضافه شده؛ مثلاً میشه سایفون، تور یا SSH رو از طریق یک کانفیگ Xray اجرا کرد. روی اندروید هم قوانین مسیریابی میتونن بر اساس نوع شبکه (مثل وای‌فای، دیتای موبایل یا اترنت) تنظیم بشن و با تعویض شبکه، بصورت خودکار تغییر کنن.
👉
github.com/CluvexStudio/ZedSecure/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u4VBuYkXF_fCjy-cS8UFfy9GvaxiDA2PhL2SphKICQcu-TswrxRjcT_fTh-V_jJaI4d4T6KF9obXrl4wXYw0GJoJjipqEaYwLSx315BZHXrnaPi4uWvj6caNoiwSgojdwc4tOM5HZ2nrWByVDRSwB3mBai2jBodKz5Scd-mdrwL8-LsffVPPvl0uuo9-i3joUpcx8Fvpf8kGKQZJ8ZOaTlPYwXqYQZEU8MKYNhajMJNWlgbN8QChqIcjZeTZqoKyXcgA8x0VdqrXzbVeMGSDvs6ug-jBaiMRxxmm1c-5rBAsW_8wFBbsdSPhaueREmqDjB4Rqza57xjNxmih7klunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rw9AqRxkWKNnG021ZJNhiKTJGuk2ir1y9txQpiRkPBUST3zvnJXshTxOgFq_48Hvm97jwkkFMYpHkeE8LZqtZDaUhpI2qq4b-7pAG2FC-eTx475FbZffnkOPcteCkUD94TBSNH9Dsh3U7jEMy2cQfdoQpkw9IdgXuXD24aNBoplzckiwScAjcz5Pp9CTNcYCtY_5rEmIbnLotE1ZSnZOKrTYcj7lU9tncZ60oeEDS5hbSMVkuCPZX7cNehCr3Oh8AAS1ZDtxNI-xiMEOJHl07gTyG_wYC9oEgXdrGfG6SX3B0lrYX_dkq9jcVqT_-HAGNsO-2Vt7oHDxvz0CFq3mvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twJfD5bUsxx5xgMXv8bOXtbezw97gEITm0ND1AYnrt5xeqhrXxZyZrfg1TW8jsCEA5tcVggy8KA1IO9GWicwAtNpnB4dDdtGYCgwGRz4LxdwUdadE4jO3cCzXRkYMaVYREqCNeFByjOH7dwKzzY8Ftw3iG88qGWZWMcJyiC-IibDDtHK_WHKbwiBOSjuJthcUWGqYnFk5dNL1dEyFviqWTsme0kTShYv3yi76wQx2IiPmM6rBSjfNNqYG93D_OXu22UVmFDLIMStaY13mTW7CabAmtfnd37dtsNVKGBT5ON79BAeUUFWK5_LlQnwLVuMYxs8fGByv_3nyOYekfTwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اسکنر متن‌باز و رایگان SenPai Scanner برای ویندوز، لینوکس، مک و اندروید منتشر شد، که توی این آپدیت قابلیت Anti-DPI اضافه شده و با تکه‌تکه کردن ClientHello (مشابه چیزی که در PattNG انجام میشه) امکان دور زدن بعضی از محدودیت‌های DPI رو فراهم می‌کنه.
حالت Gentle هم برای اینترنت‌هایی که وسط اسکن آیپی‌های تمیز کلودفلر قطع میشن اضافه شده و حالا می‌تونین آیپی، رنج یا دامنه رو مستقیماً وارد کنید و اسکن رو از فاز دوم ادامه بدید. امکان ذخیره اسکن و ادامه دادن اون بعد از قطعی هم اضافه شده.
👉
github.com/MatinSenPai/SenPaiScanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2653">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شستا ۱۰۰ درصد سهام رایتل و ۵ کرسی مدیریتی این شرکت را به مزایده گذاشت. قیمت پایه واگذاری ۱۳۰ هزار میلیارد تومان تعیین شده که با نرخ امروز دلار آزاد، تقریبا معادل ۴۸۳ میلیون دلار است. فروش به‌صورت نقدی و از طریق مزایده دومرحله‌ای انجام می‌شود.
©
stup360
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dq6w9MskrRP5mz2u1CdGvPyeR8jsp7dTnZQIZOVMrVHIq9CTg1hkXqizvJk13q-VlanyNKN0AIiqqH2xwp0pcUZthfSQgevjHnEU2WRm_4E8T3cgQn6Q0cWKQghH_fqVKB7lrmvUvqJo0XdCenYZX0ThFdyiCUNoHwKVJIscLvliZ4cEflwnJESpC-bLUfCxD7G-2Hy19yCJYpR1qWX5Dd7cn9LxTHfj72KgONuRVpkkvMQCviXxkqYNxg08Oee1808emwVkaI3_yJX8rZKyWGoiVEj1tp1BD3-ydVnPoW4q92Ym6-l_5loY7spXjG7n46GtWVBhLJZPSl0oRWG4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها در تحلیل وضعیت فیلترینگ ایران، جمع‌بندی روش‌های فعلی اتصال به اینترنت آزاد از طریق کلودفلر روی فایروال همراه اول و ایرانسل رو منتشر کرده.
بر اساس این جمع‌بندی، روی فایروال همراه اول میشه برای اتصال به CDN یا Worker از روش ECH با یک IP مناسب استفاده کرد. استفاده از IPv6 هم یکی دیگه از روش‌های فعلیه که بسته به فیلتر بودن یا نبودن دامنه، تنظیمات متفاوتی برای finalMask داره. برای WARP هم میشه از متد WARP-in-WARP در اتر روی IPv6 استفاده کرد و با اسکن، IP مناسب رو پیدا کرد.
روی فایروال ایرانسل، برای CDN و Worker میشه از متد F&F استفاده کرد که نیاز به تنظیمات مشخصی برای finalMask، cipherSuites و فینگرپرینت داره. WARP هم روی این فایروال قابل استفاده هست و محدودیتی برای نوع IP وجود نداره. علاوه بر این، روش MASQUE/H2 با اسکن IP و تنظیمات مشخصی برای فینگرپرینت و finalMask می‌تونه برای اتصال به کلودفلر از طریق هسته اتر مورد استفاده قرار بگیره.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HyCxs5M7U8n4yMHxUtP44an8rnoJb9U-7k74phKo0xeYHX9IHfES5Aj6e7ZymENMAkxn49f7j_V8zpK32PsZnV4a2N-C23h4GVQPlRGdKh-T1BPklPIwBVy-iAPhC7HyvuEorirGWiHHIEQUUWLxjqAsNb0pn1gP1FL22rl50YuFroQa3Wxd7iP4gUKCxvRr7UF0E124peMwwsGsVXyNkCpdGxPC_fvaXrH0kw5pkuRrTOxX8rHSnhnJ6-5Vc6Vdeti02Q8OHX5uA-k2dCEIRdHmHSNuBrH25TKAxuKdD5PABVaJkpLi6kIHXHGBw6NZKdrz_fedvERWoJ2J5_1lIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن دیفیکس توی جدیدترین بروزرسانی خودش قابلیت تانل‌کردن کل سیستم رو بصورت آزمایشی برای ویندوز و لینوکس اضافه کرده.
در این بروزرسانی عملکرد کلی تانل بهبود پیدا کرده، مشکل نمایش پرچم کشور محل اتصال رفع شده و چند ایراد جزئی برطرف شدن. این نسخه درحال حاضر روی گیت‌هاب و گوگل‌پلی منتشر شده و بروزرسانی مایکروسافت‌استور و اپل‌استور هم بعد از تکمیل ریویو، در دسترس عموم قرار می‌گیرن.
👉
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R7oKLpud3iJJTSJTEye0KnXTX-dtnsLMuxMQTRsuvQOzxgtvwIxjXnM69KAIL8kuXeWM6OuaUXWdbdou0fsg6vl89IzTCCSKFWNAW8A7BwcqWacavfG8anWcijwt8Fbx293PMrc8QM_kR4Jfhyw_zX4t2_BoXvhzMkQtdBATeXRAN1KYoMRzf3Ho968X-Oe3mzX2LFrJ7Mr-VJI-fnE3iuXXW7zI6a8tVA6fyJ_uQHVognGuRwyhbVs5ZrjprmQ3VzNOjLP9PNYiRFLyfPOZ7ramsmduhVhsdRe6jprV-Cqj-17itzD2zVoOv1WVX9enV5E4fqqxFQIBSi-48FxnQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MD3bA5A_sfYzm7OdfqpUwfUwxBtausVkh6thi3zu0x0ihviRZ6QPmdYxkEsS42jstJ5W1RtCWugNUMulZK8V7qTgD-IaW6z8fJUVGLrKZ-FOnU9bkIeI38mkpChHdO-dDQSedg1I8dAcNHBODMtpMOl1KLikOk2pEndqeinzDBtdIGJ1BUYFTetAOMKiMoGdHj3XWWrJjJXw7YHzrWVz2HGgfZVt8FY2Dd8pbhl2CbSN8_w1sPFXzwJboeRqA5_qvBdJc6I2XmbFJ4RjLkMDYAapQOh1gIyNKMNpjDjB84kYWd-0CLai9OMlXQIjwPTyfFn2wV66gbkeCiR8Jv95iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در جریان اعتراضات دی‌ماه تونست با جمینگ و GPS spoofing روی
استارلینک
اختلال ایجاد کنه و حتی تو بعضی مناطق کیفیت اتصال رو به‌شدت پایین بیاره، اما اینکه بتونه استارلینک رو کلاً از کار بندازه، دور از واقعیته!
اسناد ITU نشون میدن که با وجود این اختلالات، ترمینال‌های استارلینک همچنان تونستن به اینترنت بین‌المللی وصل بشن. حتی راهکارهایی که SpaceX برای مقابله با این اختلالات اعمال کرد، باعث شده سرویس در بعضی مناطق دوباره پایدارتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U8zPYIkf-9s1fFwQhcCP1bZnle98IVvKeM69gJPXcQRdR8Nlnm2TEgp97gwUIyYGL_ePMnQc_EVbuCWz7CXmpcJPpnhUARbggoIPdhrXW82ujI7t33hNCZVOovrccoJyRaQuK4PPOTfoyGPAhPRVesHXUaPz3erQau8rKBY0-ILPiZsVW5lC5ZIV-YAYM17aUbaJz8_tO6i7XlGf12lYlTf_i2FnEJm-nRVdt3YlP0pAJyU_3_X4vtoa3UnFQCHEQTVgeLOcG6pCZZ6-a-NezTmrwGWUjwoGjS4uMmO7rCefy3X3wWjzbDbqGy0PgEazX3EK9xKe-3ZuxA3a7spqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DU_fYazoFQ5mFST2-qN2TSwzOa5cepVDvK7OHbI8AOkQrFbpRS8qyuU4q_HBjApS_iFa67BAyw3wpPftuyBds9LKMrMeuHPhkls79xZPnsV3SZQl3CAE1zTtK69_BRX8UTYkXCzKbwxFl6DtRkgQhVKsOEP9MTU28iEczNjclE39RqfSz0vcCDDOVS14ulHYntVNMR2EbAufjPbj16LeSG5kjHFhPYsO0rd9OWpRPrQwTgLBs2ZDoEpUCrX6Ckf2HYk2opR8FgeaS1gi3eqOpNWWMPh8QdrCAUcwXk9sM-hR-lK6LHZ99-GXaPuX6iBBdoBgVQwlL1AAZOf2Kd32oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از فیلترشکن متن‌باز و رایگان Aether-GUI با آپدیت هسته اتر به جدیدترین نسخه و اضافه‌شدن متدهای اتصال سایفون، تور و مسک‌این‌مسک برای ویندوز، لینوکس و مک در دسترس قرار گرفت.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lP1JuXWj2CZYO71-e89l6ZImU55XsbHB5qg_sFYzITxYiO91agwj8N9cdHlz_RPKvFDYQ80OxUHXcAZgRtwPRb8l5xRf8MnrnGsHe0UyDmqwRODvhO4ue0KL9E_Hor5KSd09yKM02zwxW65hIy1VejQYDAlSJlItqyzQfXYci_qKKQmwXAy_3aMyeHoIgg3YM9ravDQgN1_6ujsdm3d-_gRBOahM20_bZqX2_vEiQakt8EmpDKPCRYyJbZkqQVkRthZmrr5a4zVLTpREtLP3q_M3yM-KjjgYy1ES7yf2Xh0DF9iXrfdOzs_HbZSsTq8XryedZ-cYem5Mcs3sWjS3Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NqYcW9agQ9w3R9mNj6rfoKKWsqW44neg7gdrZIP8AfW3xvPYhYGW4SlAp3nMljnPA_aS3HEJrf5CvXirfQtPnR27WQYhxdF3-iziH-7gAeW90enc2VlcrUdAw7tYAjnrxqgSiyscZNKVxC2GoWLSnIPgRhdCGqyldaYCigrEzwE6UOpWzYGCk6kul5VDheZ_oByo0QB5xxjOpOhwowG6kR7lifVlwaTcHNz_SS6A9iQrNBuqSJh_7di-dPczOiPwnyXli1Zn7aZJq5fZD6u80yyUYUQoq1m3tvGqUfxaP9RG7ao2ExIF9FKndhYXfz5f5K-na-dJ9EN10PijBiUOyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زومیت در گزارشی نوشته که در حال حاضر دو راه رایج برای دانلود فیلترشکن JumpJump وجود داره، که یکی از گوگل‌پلی و دیگری در گروه‌های تلگرامی هست؛ اما بررسی کارشناس‌های امنیت سایبری نشون میده هر کدوم از این جامپ‌جامپ‌هارو دانلود کرده باشین باز هم در خطر هستین. فقط خطر یکی بیشتر و اون یکی کمتره!
جامپ‌جامپی که از گوگل‌پلی دانلود نشده احتمالا یک فیلترشکن دستکاری‌شده هست و به نظر می‌رسه این فایل یک exploit یا آسیب‌پذیری قابل سوءاستفاده داره که می‌تونه دسترسی root در اندروید بگیره و رد پای دولت‌ها در نسخه دستکاری شده دیده میشه.
حتی اگر نسخه کرک‌شده رو دانلود نکرده باشین، بازم برنامه اصلی دسترسی‌های نامتعارفی از دستگاه می‌گیره که نشون‌دهنده ناامن بودن این فیلترشکنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UF4oG7J3tmu96OFeAKWwnbIq30XmVoU_NFV7OrAoJU1o8MT5-QkdhYXpruAUK5GPlkkziW-OsmmUcGBKhB-83XPH-QxqnFUxZcA2TWaRy_0WUAvaqbxTXvIih2jM4EtlCOna7sFRtZkeXISJnuoZVZseRNiQs2PU4KVKy5vVwu5QjUIYtB3V6ppo81q7ux2PZz66z20JpuyhEO_aITI64kMOEeHW2YV96R4yubOlrYcxfeLsGTrFUCio614l6jllbiJx6enDZ9bajvHwToN3FvlhTNWffapQBcjQi2flFaumJFUxnrBApnTcJ7g3MDOMjbprOC8LwbXVRbazK1Hm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اپ سایفون چندروزه روی اپل‌استور در دسترس قرار گرفته.
👉
apps.apple.com/us/app/psiphon-vpn-secure-access/id1276263909
💡
play.google.com/store/apps/details?id=com.psiphon3
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qenLW_WgtcCGI_xpjqSOv7YB-8G4MuHVgrJJW6XRCTFGA6a_jI3YdB5MP__B2WxIvKJAxx2dYyxRfWrNSDliNrSBqqJnDo3wANr24EB87CYx3GMXOh1NkCvDXRdR6Fzzly1WiNcQYLkPiWragvunmOm_07osrXS6Tbis64_IPONXn2MRY0adhs85N0R2hMFWxLWQaGFWfQY-XggjbGLuOQSFofgm-4Mejyn9uXzzzGJ0Ehye_jkWIoH3xxaV-rWR04uhZ-p4AFgPhGStslSwFZmTeaamCyeRRLNjZGy2LkSKTDTbSOgmsTxa_FAliXKucd_UUNHv9uEVKWX6O1LAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HAgSnLUZ1D4BbsoHuZvM_PAJxKzWc0c_zYMO5fJyiaow-waU6GcTalAx6Q77ZbsWg_anzYeJMrJNj1DrhaJXcO1tlnYd0T4gQ7hcc-pBFTYCnk9Bxqqt9nCSIXH9JtRyoNyVNblYRdLabKAKkL93J7ZA1mgGpulQ9PXiLIjls5hAFjz24wOG_4K5FidsHytSFNOrs6JLqRSN9XK5cWe3ccCVcqWSARjiR2ZvZBlJDTVjZ1iGfDc6ypAaXe40Bx4a6XHFtxPaGXwPmB2i8V5gK9Oi7hOWuEfgpDMc0TdjOVLw4XDLGnBpU6x1OwQcSnoVNtRzuXl8OFJfgF2JCbsDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحوه استفاده از برنامه‌های PattN و PattNG برای دورزدن فیلترینگ
📽
youtube.com/watch?v=CnEQipAJ2hE
💡
t.me/ircf_toolbox/25
©
𝐀𝐥𝐢
👉
github.com/patterniha/PattNG/releases
👉
github.com/patterniha/PattN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U_XDwGCd-IrRdY8qVb7UVd-OO3omOod7BUlM8sszxC2Zcuh6m1we7M6NTuA4axVBpunV0qeofqxs7p7yUc6-qse-s4zyzYd7JCHIVhw2ReQxYWIrFXR8-WanKKch3au1frRLdfyJFbpKuLEnv_f8m93d6Ba2tQZabCOmG-7OTV51Xk8rF3ams9XFzOS3hziLQSzUisUZAfRLSAu1fLeb1CSF0nuV8nua8wOOigcgT3ZPmdjx_zcIC4qkoetwsErWmdbb4OS2pCB7Rs9BmRySGYXxk3XPdwH4vgI9tkBn8gDDm2dUXEb0rIxjGL_YUrae3FVl4PBH5n9Ud_LwznmZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از هسته Aether مشکل برگشت آیپی ایران در متد اتصال Gool رو برطرف کرده و محدودیت اخیر دریافت کلید وارپ و مسک رو روی بعضی از اینترنت‌ها دور زده.
اگه H2 روی سرویس دهنده‌هایی نظیر ایرانسل به هردلیلی ایراد داشت، میتونین طبق داکیومنت از فلگ فرگمنت استفاده کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RwXde8zfWsexgBN3-YPEpmAQ3FeSjS2TwTaPLu2QeDu_xMNWfvxu-gHOK65U2lDnLFSk9d6yM1wmjNlNLXhjJxDKWRr3o3sT1JolQjMpB1XZ0j5uQgNxZv_1OsG42cEtNXO0jhmHR2DJQbFf7a6LUUQcIV2-SeQQdJ_rglgZ0btFZ6ryQ1qQ1GSA5lBh44AS5z5EOUjNAE2vatHj3Zf5B74f1ZIyiYCh_oa8AggtZeFfl3CQL9VEIQzT7ct7CRkzZwS07Q61dwpvbVuaZr2kxCmG1p5Ulg1FF26ma4mEXGDPQnlKeNNXN6BEOhouC0TNXzqMTA1J_OC_A5d1PbUCNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۸ از فیلترشکن اندرویدی MahsaNG منتشر شده و توی این نسخه هسته Xray مهسا آپدیت شده و پشتیبانی از پروتکل MASQUE رو اضافه کردن.
برای وایرگارد و مسک حالا یک اسکنر IP اختصاصی در دسترسه که از نویز و پورت پشتیبانی می‌کنه و میشه کانفیگ‌های این دو پروتکل رو با کلید Auto ساخت. امکان بکاپ از کانفیگ‌های شخصی، صفحه پروکسی تلگرام برای کپی و تست سریع پروکسی‌ها و بهبود Fragment و حالت Auto هم اضافه شدن.
چند نویز جدید برای عبور از فیلترینگ UDP، کانفیگ‌های جدید یوتیوب و پشتیبانی از Cipher Suite برای افزایش سرعت آپلود در متدهای پترنیها به این نسخه اضافه شده. FinalMask حالا روی پروتکل‌های جدید MASQUE و Hysteria در دسترسه و علاوه بر رفع یک سری از مشکلات، ابزار زنجیره‌ساز کانفیگ هم از Fragment، Hysteria و MASQUE پشتیبانی می‌کنه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s60KdsYqQiteDbKco_j8ZsPTMfYj4TtAmlATysS42zn2F18DOJW4QZwILp5Srw7bgMECggLbQNFwOFFkmh0OFAqn5nvVbtCRSuGmQonNG7hXcUDrYk62BHVBOMzvZ6Yni2B1DmVypHoi8ptwPs_C6aKtWsoRqedL5q98ujiKDeLNFSOGUxKY8Qcb5VRNEere4DEEmKSJLSBBvG0edMdqb2fJx1BE-OnOURyxRwioBXWzn8N_TnUMYEaFDapr5P-2HWBe_z0m8IHoYXj68k90kUIcj9LI7-pLn9BjP0cQWM6vb2zo3TY3TtLNQ0elOFSUqYx5lHoztFRLZSERHD1ePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل از نسخه iOS ۱۸.۱ قابلیتی گذاشته که اگه آیفون ۷۲ ساعت آنلاک نشه، خودش ری‌استارت میشه. این کار باعث میشه اطلاعات گوشی دوباره وارد حالت محافظت‌شده‌تری بشه و ابزارهای فورنزیک مثل GrayKey سخت‌تر بتونن قفل گوشی رو باز کنن.
حالا شرکت Magnet Forensics که سازنده GrayKey هست، ظاهراً راهی پیدا کرده که قبل از این ری‌استارت خودکار، گوشی رو در همون وضعیت نگه داره تا مأموران بتونن فرصت بیشتری برای استخراج اطلاعات داشته باشن. این قابلیت با نام GrayKey Preserve و همچنین Evidence Preservation Mode معرفی شده. البته فعلاً این موضوع بر اساس یک ویدیوی تبلیغاتی لو رفته از شرکت مطرح شده و جزئیات فنی روش منتشر نشده. در واقع جنگ بین اپل و ابزارهای بازکردن قفل گوشی همچنان ادامه داره.
ناگفته نمونه مأموران توی ایران برای باز کردن قفل گوشی بازداشت‌شده‌ها، نیازی به GrayKey و این ابزارها ندارن؛ زور و تهدید راه ساده‌تر و دم‌دست‌تریه واسشون!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پروژه Nexora یک پنل برای مدیریت چندسروری VPN هست، که تا ۲۵ کاربر و ۱ نود رو بدون نیاز به لایسنس و با تمام امکانات پنل در اختیارتون میذاره و میتونه برای مصارف شخصی یا گروه دوستان یا خانواده قابل استفاده باشه.
نکسورا مدیریت کاربران، نودها، اشتراک‌ها و پروتکل‌ها رو از داخل یک پنل انجام میده و از پروتکل‌هایی مثل VLESS با REALITY، XHTTP و Encryption، VMess، Trojan، Shadowsocks، Hysteria2، TUIC، AnyTLS، Naive، ShadowTLS، Snell، Mieru، MTProxy و SSH پشتیبانی می‌کنه؛ در کنارش پروتکل‌های کلاسیک VPN مثل OpenVPN، OpenConnect و WireGuard هم قابل استفاده هستن.
از قابلیت‌های دیگه Nexora میشه به تانل بین نودها، پشتیبانی از CDN و چند آدرس برای هر نود، همگام‌سازی بدون نیاز به ری‌استارت، Rule-set برای مدیریت ترافیک، مسدودسازی تورنت، محدودیت دستگاه بر اساس HWID و انجام عملیات گروهی روی کاربران اشاره کرد.
برای مدیریت و نگهداری پنل هم امکاناتی مثل احراز هویت دوعاملی، بکاپ رمزنگاری‌شده، بروزرسانی خودکار و Webhook در نظر گرفته شده، امکان مهاجرت از پنل‌هایی مثل S-UI، 3X-UI، X-UI، Marzban، PasarGuard، Hiddify، Marzneshin و Remnawave رو داره و از زبان‌های انگلیسی، فارسی، روسی و چینی پشتیبانی می‌کنه.
👉
github.com/nexora-vpn/panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rCXBtqnE-jCEX4wzuOZZbzC8A_jDN5h2D2cACdNCy7K7VdgLZdA_OrB5xabRNXl-wNSbdP1imhohWIkISKS6rxMKcwAjYvF4ldsvtmDA-TvuLpvd-P6DB95brwZ89BDParSFcxRd3Y4Rb71wbnO_lzIY2DfnZPWBWcCSXnAb_z61x45suFTJCuFSyJChDVXdYQ-AFqUWs39N_ctTNU3FfAv7iY09eFViYIvXtPmyRefcnqdZVz-0yOgBetI_gsOr5n_JUrRC5MyrRYwE-Hvtpv6GpzYfSsD87aHSaIqSuU1sxddVV8bfWAWkLnifE0v6Lg-tgFCcKnqJM938reeJkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد و مهاجما از اون برای تبلیغ یک رمزارز جعلی با نام $Clippy استفاده کردن.
هنوز مشخص نیست چطور به حساب دسترسی پیدا کردن و تحقیقات ادامه داره. مایکروسافت هم اعلام کرده هیچ ارتباطی با این رمزارز نداره و پیگیر اقدامات قانونیه.
©
theverge
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AWF1r3BUX7xYzVUGEL73H3mNIY2h4_srjXb_ygSb6wIzftll0Bc5HNWPtWfDeoKmQ0vQ9ewm7f5-7K5tn_fqLJkJWfOYNEaRQroZeZ2-D5YjI3TjK6Yr_60MYsCBiM0cORihKZYG7mGBYzEOqBfuPuwcd4Tw3XSYv1sIAC5TBQMfEMMD9fOSINP2ZC1zvlQlhb90AfC9etEGCv7XNqQoMF6HCYbBLwJKoUzH8EN65MMmnNSSRVLmD2jfbUfk5gJV8KY3M1DFxUkWdUyDKfzPpm1sx0FGZ7vqoJntFEP0yb_fZjtqjzw3nq8JDEiKtI_MYLy_7L9xssce-8ybuaP7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GQOXzQ9y_JfA1UPMxdB2v8bdJLIpqDfWa0cdnMJbThhRvA8XqIR-CQj3U71Cep3C-EgPg9stnFPETkBHELn7es_HfXR3TX6-AXVTTMrL4r6oc1ZkkMCq45ti_HeIF0oZNFsF3JsN6v9xrfnHAz2ifgPEJJkTvoz0vPlj7O2-UsHzDDvfWq8MV49-wsDlQHpPatgooTk2AKG-MfhvUD1kIzHaRmlbN6QxiobiU8R9vJew_6SHNupThv55ucBsiSFJUJOYHnWYrjOZYIHv_4YgyNu1v7XoU5_6k0mKXk4uDRZLegJq4xzHT-rSwnFG8LZqMmaIyTyAibao9PrNv7t4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه از TeamViewer استفاده می‌کنین، چند آسیب‌پذیری امنیتی با شدت بالا پیدا شده که در بعضی شرایط می‌تونه به مهاجم اجازه دسترسی غیرمجاز و حتی اجرای کد روی سیستم رو بده، که مهمترین مورد CVE-2026-92370 با امتیاز ۸.۸ هست.
فعلاً TeamViewer گفته شواهدی از سوءاستفاده فعال یا انتشار کد اکسپلویت عمومی برای این آسیب‌پذیری‌ها ندیده، اما در نسخه ۱۵.۸۲ این مشکلات رو برطرف کردن و لازمه آپدیت کنید.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pVLK4Eqlr6lzpTLXdKbawulkgel10xChNd9w7r32x-3nEol8YABINe7IQGxLtcpJy1p0Y_1RPellDiyT4-ofE-CMvJsJIYv5am0x2jk5bfxL1xyCkjTe1MCEjrUKEVzMXxJrK614A7p1KOacDpdMqZxmuZO5dg_eG8btJqfOhEg8xfnDaejrlgdPX1zVVWlcfk-f8aNEAdpp34vIldsQYh_ugmCTEJJE9usHoBEMJwyHYEVDiXroMGNs12jSMpf95B3Wfp2fb1mHC8Oa9OGRK34zz3gJgbvMeJto3ZLydwJb6bqpQx1Gx76_JSdmz3eMNvguYUmjR-TbpSv0eiQe0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ج.ا در سال ۲۰۲۶ رسیده به راهکار ماه‌های پایانی حکومت قذافی در برخورد با مخالفان: قطع سراسری برق!
©
ArminSoleimany
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c3eTo91B6DiFbDTNtcmvuExsOOPNUS2EgWxlX7tQrB1-PfOi2INQehgcqMxftt6nUmc0eBjGzxjWs86pdwEJYS_mGpA807Z3_QxSM-HkPF8EAQ7I31aM46llJ7gUjVL4GW1vYvCeh72YgW89-6Q5v6BiclAYlWd6WBAjZEF9zMewg5jCwf9zKm9RtLjO_vM4gtxnUlC3ZcaYmDjTek_hioSwQc59VA1QpcJprHNExhIYhEcvIysv4CWsDuRw_lA2MXOJEDqJhO1Ti4iTmZJpfBbMoyK5c-wblOPau0qtN80_dnyX-zsDw-V1mOJttvTToC8IXgKWdhtEjpFRIcPeaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه این و اون خبر چند وقت پیش در مورد تغییر شرایط استفاده letsencrypt می‌شه گواهی ریشه داخلی و پایان بازی. از مسائل فنی اجرایی صرف نظر کنیم، بحث‌های مهمی باقی است: «حریم شخصی» و «امنیت».
در کشوری که با مداخله در پیامک احراز هویت ۲ مرحله‌ای حساب کاربری مردم رو تصاحب می‌کنند و پاسخگویی هم در نبود قانون و ضمانت اجرایی نیست، امکان جعل گواهی برای شنود به خصوص برای موارد بدون SSL pin هست.
©
Hamed
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cuL6OW7xDxZ0oY5afmXU84lwmzEeAOhMsXYwwOPK_7tetqG5Ug1XpZVOYWdxJnvwdmQoUjvZv-r4Ks_snyUQ7Jg8P_XSM7khpGGzAbgoOQDUOi4_4mBzRZMdAJ7zlK3-_VaZZfZC5EDVsoEVii28_FEEm2ZLJJmZFC59Hns_PXuWaAaDIDqXkO6EGaWzWUjTviUZRRrPKiVoCDeDEBdvppuQ5E9l5uSU3miirSR0wStTWGeF3um1J2ARjHDR03_idhcXxi7X3LBU5IHjsrvO-bdbYrBBYyWjEqwvq3F2zejJPCRDyS58d_z84DQcyMA71zqwRISFcoPz1wfrLh0mtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکارشون برای مدیریت قیمت تتر چی بود؟
نمودار قیمت رو غیرفعال کردن!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RkmAjr77xD3NoKynkzlKP3eBDF4JBsPblR4O3VmOnzzKx6K92GSJ4JKpFq-gDdEjcDDVGnXBIzUA8rErzOAPWenyKXvOwWiRIjRfciKzJPArH56F8VIkwxJwjZs1wkx3MxbcBuQVjfVvCV0GjHV7AlS36yBC2pMHYHTdNvylT20GCAM4v8ioCKAlJHwgo_KORDkGXyF8bKPYETFE5lU3Vp_4aC7m8zTqpjjiJ_tOHysK4R_30wApaRp8XeEzyvnSDGaMif0S7PsZCCp7sj_f6EQZZacFJbi0MW4i1aGrRGrdS93YU9frZBQLm5WF7iXPcgV6gxKnaw20CCgEPE7FnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اتفاقات امروز و تصمیمات هوشمندانه‌ای که برای مدیریت اقتصادی کشور گرفته میشه، کله هممون رو خراب کرده احتمالا.
ساتوشی می‌تونست وایت‌پیپر بیت‌کوین رو خیلی کوتاه‌تر بنویسه: دست به دست هم دهیم و دستگاه چاپ پول رو در
ماتحت
بانک‌های مرکزی فرو کنیم.
حالا تقاضا رو سرکوب کن، حساب‌هارو ببند یا سلطان فلان و بیسار رو اعدام کن، این باتلاقیه که خودتون درست کردید، توش دست و پا می‌زنید و ازش خلاصی نیست. این وسط، عمر ما هم رفت سر ایدئولوژی شما.
©
GrizzlyBTCloverr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XhxM3nGaLqqGplNPvvXXCHiDyyw1XOZk6qYbllLjgoOiVQC0Cx6EmxlqQxfU091I0_prRuPJV4DHEW0p9_MiHmAuQ6Ug4PE1CEkallfSXbHOtO9H1fdF9k20Pbg2aqZah85wX-ecjL5kGTpd18fPizCQYfeyhrNco_bd9FE4Auxq70MPpy-9sguuLaU-7prgW0VM8yZpI768YCpRm_VpKqwf0gaNbGiJzkJ-2xnajvzYOmmzCwq1U7EpfUWUgJOWg62ZnVIblPt_E3Dr9sQjUnDyEJkllibR2nhtINnmrPAspOMSB-OY-QXEBvUpifCiafGvWSbD1aGZMMzlHeGESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m7tfDCQdJeH0r2M7HRXQU6pTDT-G2zjdrme5qU9TrDP-snu_HrhtLLFhElY4eWfPmo9YP3lrkLqWHlJ3W2G0QXyM5CvwPnVf3ywWhABNt7V_ARRsXQV9zTRCCHScc5Qqs-Vskm_xRqppmeoi_-wWX6_gNWfmrCxYzdpkc2vl1H_uf-IknS5A4qEM-xgnnHnDvVSlfIFTYApn65C4OYem4Az0EPIVFVHMxUvtnNUWdV4ltoRTgxdl-lsEOoJOMu6xdc6ARanfUcih2WUkmN65iZnDWgpmpkC3MLf4CHWiUORytNgsM50fN9zLuqKB8O5L9w6WkZ6J5qLUq0u1wH5W0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مجموعه‌ای در حدود ۷۵۰ هزار رکورد از اطلاعات مرتبط با کاربران صرافی ارز دیجیتال والکس مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱، در فهرست فروشندگان بانک‌های اطلاعاتی غیرمجاز مشاهده شده.
این داده‌ها شامل اطلاعات هویتی مانند نام، نام خانوادگی، شماره ملی، تاریخ تولد، شماره تلفن، آدرس، ایمیل، اطلاعات مرتبط با احراز هویت و همچنین اطلاعات مالی از جمله شماره کارت بانکی، شماره شبا، اطلاعات صاحب حساب، آدرس و موجودی کیف‌پول‌های رمزارزی و سایر اطلاعات مرتبط با کاربران است.
افشای این اطلاعات می‌تواند زمینه‌ساز فیشینگ هدفمند، کلاهبرداری مالی، مهندسی اجتماعی و سوءاستفاده از اطلاعات هویتی و بانکی کاربران شود. به کاربران توصیه می‌شود در صورت فعال بودن کارت، برای تعویض آن اقدام کنند، نسبت به تماس‌ها، پیام‌ها و لینک‌های مشکوک هوشیار باشند و از ارائه اطلاعات شخصی خود به افراد ناشناس خودداری کنند.
©
leakfarsi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B3rnKefweFjhvdrYXwoDfwqDZdj0nN7MtJgw9ozwmL90EVINplH9YsaWlYFkZMQePmDkwAkLbd3PGClgCRXWMnBfA62z2Ew6Ly1PlVoOo4oWzL58w3cp5s_9L_bZrkkCGT1IcnY-xaRYxou8nbpFu-iqt2qYlaMVW5n3FXc8C-Bw70ceViTjLa4WmSnPhY0_YHQIGn_PqlR3Rpo7YWXpxqAxVQVS2V80ihID-7gzFMmdjH1nXrUIgzd3cB85poxXRHyNxyHN6CJTkjzy9d6JQ_fQ4TPYQCpzjzrGMG45UCXc7zIOeux536AlcC_9YUrK0OC8qn8Mxyy4ehhi6S73wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErnCx6OALPBd1VUlDTqpzMcUt_IPXXJmgLckWkOG7S6p4tkZJXQCe5ydrUYgwywrWNH0xmhKG4AaaabzxQofibxsD28AZ71nECmBvaPGqYKSeGBzaJYPF6Tr2gvZ_t2FUHfJa44EcqDI6jvHeOCZNONwuJxi8BNdyaUg6j_I0wwc5E1yi50TeUns2qXZJ6GtMN5rdt9XEbpwMyIrAqHhqMmR7Nev8Qn6xUM1NYXf2-s9PBgrx6DjqUuNZhj6yZLpoj--XYy_rDwFcn4XKaTkWBtGccNinfkugtz39eONk0CRS0ieTZhWnBuL7pzvcFvrndy85O68G2hv9aSMC6AlBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNNhfO88wIpStYEdj75sb8Jy4k7xPZmVKvTcnzg8heUVAiol3xy36w9DIW6gwVZxCLwCp5-XClEx1GfQT_I86ed3HcTInidKje9WpISeEEAd7P7ZdyiLRWpj_Wn8j9mNxfu4O0razswh_rs-MxGBobaKX0OJdLbdjpd_xzX2TIRvwy_Y_8UsfN3wAVjJ10thNTkfzxJ4G-_yxynSWi5z6vXe4c8723B3adX3XUGLRhAwSUJ4RGiS1bUp2FdR7behmJhAPGOe8FiitEZLetnsUYPqq9sCOqLyYRwcg2TqkDcMGkAZmLGioGG0DWbk86oijaw4eNbbGWroJgl6D_jITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هم خبر تحریم ساخت ایمیل برای ایرانی‌ها توسط گوگل قدیمیه، هم خبر مسدود کردن ۶۰ اکانت مرتبط با صداوسیما توسط گوگل.
فعلاً اون لجنی که توشیم هیچ تغییر جدیدی نکرده
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a4Lha6dm6vOcZjGOkGH6Msd1oiAZ6dgwJJDqQ-ChffBCIqEd5ohbAMXatJbi-Gq_LKGB2SZuqmrLDZP4trl5tTm2OS5iJerdQrDfQyMWSJOS3HgXjEQajO4gR6iNh-7raKkvCa_6qBn_bJqAYJ1Loqs6rvFvxBbQU5AhhtgOLgu2L2f4VABU4MKL6LuLSZXE_Z6iVoeK3VbAOXzCid1LdtUs0KCoGseEkQw8P58unGcSjJWVFdPEUkUu2nd3F3LdKTlHc-rGiBsXqdael8UF9MNM-dr2BQcJdBacWn5wvAOVDtwT1YL61IQHzEg3YqaB4tnimCVbCNLAIgrpXoAbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ sushTun یک کلاینت متن‌باز و رایگان برای هسته ایکس‌ری هست، که از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard پشتیبانی می‌کنه و تمام ترافیک سیستم رو از طریق تانل ایکس‌ری عبور میده.
یکی از بخش‌های کاربردی این‌برنامه که برای ویندوز، لینوکس و مک ارائه شده، مسیریابی هوشمنده؛ تا بتونین مشخص کنین ترافیک ایران، روسیه، چین، تبلیغات و دامنه‌ها یا IPهای دلخواه از تانل عبور نکنن. امکان تنظیم DNS، فرگمنت برای TLS، Multiplexing و چند قابلیت دیگه هم وجود داره. حالت کم‌مصرف هم اجازه میده ترافیک‌های پس‌زمینه سیستم مثل Telemetry و آپدیت‌ها مستقیماً به اینترنت وصل بشن و از پروکسی عبور نکنن.
👉
github.com/soroushdeimi/sushTun/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNH81ZBNI7vr2inMs24IJldXOxCpaGkRQvrkrI8pTlXta3sgRjY3FrVF6yPsO4ZEFz7Wj31y_AZz2Yw-yf-nrcoLH3x1nnnAshrt0hrw_-sn9OiuIDH87rFKXIYzLcNQrhtf_eviPco4FdiQgIOB8LkQ5HgfZ_5ML3kOt4tRLgiwTts9tMIiS-PdWhVBj7R2i9mEmkVbSXXZ5kcLYznBb0wiqDb4vpXFGMxEwkIO16NWNGj0g4XzqM7N2HpB4aAfBLubConJYwICyzwxErk7tCriJmDB52DENB5eYAblzFQYgLUjREbgKcDXYOfDY7Z0C-plkDbiJIlnM69rIkfZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vE7jn9V1sUEVt1Ka96salSJgFAWRjKL7v30RVJDhyIyEs-ItRpCWnUtBVKZ6rYGEhFMD1EQ3YfV3BDw8UPJIDn3tsJS0WllAbJW2wpelpIXTy9O4mbvQkf4wS5wSTx9FEGcHC5VVMoIci36Iw1lFwwyej3guyiKB8ewG3OmqJUmj1LSdKvUeHEfurwNPVoKRfXg6cti4y4L47zKm8AEKiZaLakmyrmtxVDLX9lDSaDK5Ve0prhcgCfuPrbKg9SDr0sCzUX-Z0RCv_Hj_Aojk7pc-atWfLxIwOQ2b_Tlf72-amJWwghYjNv29x2RBKeroeC9tqXdeodJiZLYrUX-nCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XckosxnH3HVu5q8xv-6ZMBkheIX-8viljMC5WmsKm3b4nxNMzW-AsbqoUXJQAFTh2dGHVEq4zygF720JeMugSsEbYmW5tP0fvjINd9VUSSC73p_OwLC-KPk8KJ_5a4APCEuj3nGDOuYEZPED1CsbMzkOMx6wWC7y-1FdWl9FeG4YVkaUP4uBQL7h6MoK3RDDV81XlU5cOZn3STMUed3SJUzpGbTqxyX9wLciSEVHq59QsaQyY1cI8cvz0vz4aTB0UVOereoPfMjT8GY9i-PxfwzSzz1ORXpTRvXlAgI47NYhBLxRcvBRt9Yv5DF65RZv2LJXxF9qOr7zL2BVhpv10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/agNKeDERnvWzIUpXR-HtWWONN8hng_H9nZs2Vc4vJeArWt-oDzRLY9mYRbZ3rKieEJOD3d3PiA1zFyYpCMPagKHE40oGRp_q02PiO4ajyl3F-SEsiQfWvtknwzSnxU7Ip3ufw288lNixy7EHhxVpE2HIKoH4O7tj7y9Sk1PefzeDVJ1-nyFnqVZ5WeamKyfDUjaAYyX6cJMPBP9xdJqIQROw_LdLmGnGV_4Yjdoi21EMEL3EnShfk283C_3sR24VZGkjj74Rt2L6Xq-lyb-FUbAWbHY1GWPAdO-bDI6m80-nsN0ZxW_gzX_QOg44-y7fUH36sBYKayWIspD5tgu69Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fvWOXjwiehqj30WFdhcV16Gy55TfTAbbHas4J8Hu6QS3kYf_IePhWE3LJgB0J1YuNDkaMnheU9dBP-KZRLYhg0Vg-0QfaAFA2JFqgnIma0TFtDZ6NRJMPNZNkLh90NkCKuPJm5Bm07vR3sT8UUAaexoPY524mwu9tBtB1FCJ1DSzepDJFT_hc9W7-tTF__N-FbwfSuxlRwNiEASYbe4qTMCDR5_lsM2bvAui7gEQQcEZl8qN7gstYwBfeR5QnM9JU5b1he5voIzdsvjjamtu6EArumqExm7rOsHJ-g4ZxpTxdXmgo8KpYaW-hlwVw8qf9jhISRCGUA6Kg7gbWU960Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F5gjQM_pKcMct_eXdLBXiuLUxXU05eNCbue91GSCNxSm5gUIoN7Xp0qwY2nqs4g9sbK1I71peqVaU957apFOvKXDAUIyaGAGN9aVHJUPGWIgw4tpdP4aaPvatCVzIR7dg-tSgnevxiECNsAEZoY5IaWd4-Paw1d0c15YaoI7iZO3xFqGJZofNqLoyscWqsQunOxVz3XPkoWWy5lwE8vn6ZnkqCI_Ojliz1hLKpUL1bSubgFCXRV8PJ4IjRmtjx1kB3qaIPBtzsC3vtRM8MjkDOrmy0Xp9a5hUQibaEPZE-yOWVSxyH2t9wJiRzAsmgbTEGjcGIpexwfGiZpkAbgeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P6zn7_LDO2-y8x53Z0LMmM7YxxgapONteSjoewGlOcF_OQ1nOiIBRv-hW4qAjC2UBVn1X0smIjQlTp37M2mX_f3H4h-TPQofkQ5r51f4n8lFqtPzNCPFIksHF2Ic0mNgvlZyMoiyrp3Wy-F1AMQsdWu8fT068MLu6EPIacdtovgVfYCWceMF3nRRM1iQ44S2X5evef69HRV26zHvJU1KNvPMelbMnHIVrgkJbhKIaLMoTeu2E-yuOeBNzQJwFExnmpSiJZ8oM7t1fzRqzgqYEQ7eYRoG6NOK83lvhGAzk-wb5w9-4ry617XL0lai9aNHH1A5p9t0_xzsprWYxGcJ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sSdJ3WwdGU8DUjy_GF_CXy4X3tCbvcntBcEqB5G5dgKQZOuDPDefOGNYgBipPJjpT8M4pJW5XQt1haGz0pPeU39AjmTj6AfTYPN6yIStli8PxjX_2xdJMZ4hQKYL4uxeLxr_Xu6W4OZPd-4Wr41v660PsUXo1qPdNQJieS-iiNQ1r9dJOoBjGtJAl6QCjy1fRQ26-viJdnCOXYs585bZiSISczfeyelwnwOAHqWL3kaJcOEjNC8UOVJ8Wwe1Bl4-XJ_zX_DMPylIk60N9MoWsyFx6XkgLulQjCZN0Fz6zBN2rw1ar5tm39w92tsLyG-GvHoYo3ziV_BkYdMhf2H6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OOZ9sduw-HOf6xT3F3IuwEmk_C0xXHyOvIEKcPiOMnLSlZKpnwaqeyfMqGnt7rjhcyToatg6N2kKUH2cgwb9QNlUNfx5sidvfA07g-hnYt5jhc1yYhkTNtxLk_2_tKiUFniSYw_qmskvAkCcyGvfml-z2GfihOKlOBCL2uapnQn3W5dq_Xs6gyaGGJWsy5vb3EOtl7A3HR4AT195jm9saVbitGBLujqa-7A11WUibFXDwhyQundW6Lmq_psVUzGlekcamS6pKz1LB5k1Oqw2ENJcFrMPP8hbZQa4XKxB8R9avHswqSPctH5L4-y9eCXl03Be8OhW6rl4jN5_QWC7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcILlK4oWD9DvmbRz0JtZT429uAuVV0-2easCrrIg6CGMzQRuqU8Qfedat05O0A4gxB62z6vr41om1v2zh39LUSqnpWOPAnUAO_A2z3xXkoacWES99QOsJOCHlj6gdla4Tb-_KkxEtotb4vAkvWw8um8C9Bizd195rSMoKSXyHSBPoOb_2qqO62A5XQ3qusIeW7d5nCNkXIzUzWvyI7sgEXTFXES_nplBN5f62uceFneUQ80bmNp-hxoCnP2Oi7M5lS6shwOuLVQtyUs4n8e_xM5BczaK9D0SGgBdwupBz9RP6yIbOWYeKQs1m0_lM5X20BmEwzZ0VSLTWCj0oCRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IrTF3JYJ7qLpZ_PDYd1hrY-RcMZ1xRdMvgKBj6LyU4tzNpqC8rE9SQDIk9k3rw1vsj-f5ABLZk8cFBeoUplGNME43B_myhDPplr0DfSs4tlaLeae7bYm2tGoEjj5kpGk-N6o4pNNM-7WN68iuZToCAm0O-LCJbzFsv46OYdOt2r3q5PBRI979EktaUPH9h2TPPminGTc78u9kWTAViMpbzszZv3hqIgU0svV-Dp_VPngD24MCgpjQGd7oDfzsZ3H7LgR_p2mL-fpVGbb-h3-SLYz04nArx7vxRML9SfUjTtpO6ziu9IZZJL0wunKl6yy2ujt8xUf9rVC2EJhG3Qc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q6ojh5hQbZWiq5U4Kzg4ot0r8Iesz72bYfPrMw-i4VEc7Gv0pLut9x1qtDD1RWYpRAth8RlALAy0GD7ae91NJIUGukZ_d7mnp9qAND7FTTIHLSsts7ESQXwAdHwtPkz2tU-TjMA7WteIdM6gKAoAcWQk_pAbxwshpC7_v8fSzDJH-36hcRX6Qc9DGV-cjk8paUI7WvfkQB2f2tWc9dhHm23k_zHOdWDSEBJMHtxv5KZEVzNUWJYeAgfI1iL67V8Wm5clq9UomzI7645rov_FtRUrlr7E85KLvICV9Ewg4RSo1F-CqRndb9TeN-ZRSQwkvpoJ5DPWDpNNnGHYHPO_OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bjqqsKOIMIR1rWZ0qEDWoZFxCgoyujQEOoRXzN3ThBgx12v_hSie3vQIjgqojwReJ3uVZKSwxM5pyhOBszHUly7wn2UME0u7V9GFSpKNa1n6weXKmcM2zfg2LE0TpWQFdtZKpBRtCGa4IS4qHuVUj_j7osIzoJpQa4AX4Cewvh5V_0Nz1XdDonupzw2g5SdMkS57v-ggpGRVSQeqoqr_AkZvEWzqaQLqULvBaSinqg1IYrBFo0aIuqa1pp1vRwcc9mhLIlOpeNlsSalzRSjh8Om0Pw0ItRj_cHMGhQ5I9n_jGFCMGyE-7uNgp5B3k7t4cHIOHHvfSHCdJwUxOdgzeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TGp95qM8CNmNKLQZQq4cZ2qbju_WtHX2OitdKcX2ze8RvP7zY9elCY9XHOu8IZT-6AgaQBOTxNZ41Goh5zTEcPh-upDjuLh046HNE2bn4gmA_QyjnS0ERyUhkKBpnoTYJ-JMFxAObVr-9MHvLHC5ULHVrZVf4Ot0QDQtqOSOgdrKAP4WBwDqmImpLSqlRE5G0eQAET_u2H2htxEwe-p3IbY9JYeQWGUznCegcUUiSX9SBGg-2MB5KRLxIG5KMFhwtdO6SfFx6IxemnbhoD9wC1UmGFrIiuGZaSEAVjYhj3V5Wfq2CE5TsTyxQfUlmaMBj1s5RwiiUfzUQlOdmNaqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/quMeQpZ7JoE4h9yqf1v697EBSHrdukt2gK8Ptkpog8a9h8x6L17Abut57z2L-s1Cy2Qdrozqp_vraXw_1FuHrvkO98hkV9yHXphKT2njCgMKQttBUZDv2suOXaJnqbdj-dHFr2rPTuD2GpUlbZ4H9gVWMW9D3cUvSTIJ52HUa87Lsvu-v8o1DIKJXteLJkAoP9hfgmGgpP1t1en1IqPNmYbmhs7TCZgwEXMm7OVzm-szi6XmTVefam1_1qA_HbUPcnCql7x3cxyRNBYxHbwzn0JhBDsOQbebFzL4qXlmDGKKwFeXcGDQLl4QyPRPYLii4Xzcpq4aEKEmYI1EXyLRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i9JVXe7FtL9jWVkGTkhj2qAKOeduVxJBksgCqDUw1GBY01AN2NasJV_9D7EFmVnnzzRnkNBiFmfYeqyVyjzmKs6sK2bSNpvEQhqLbxe0ligRd-o_ZeweRa_ZmY-i51JRNgKsSxxFfG4U6N8x56b5tPQozvkEvXklJBz_Dyw84t4z1VUvbJQkJAcBqv1VGqKrdJQZ-ekVM2AqWay4w5pcBGcLAxQAla4LDPCbBxbf_s2xnozdT7K7AVmA2rT5RNLTHfX5fW6r-_KXm2FTYyiL8zlkSq5M0N7w0OHd2gh5gB4QlWxwLzDNyHxiipKA33xNnl6SMwdPw9gcaPUIO70fTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c7Fi6MZ2GyRV66S_H7hsZevAPQ9JM1f6OguwK1opUxgvstjyjKcGdPEHrXVUyWAnVhEKcA1wVRnm__bj3oJ6kw2Oq0-unLyUfNP3ZXWtNkyf7gviozccQzTl7P0AxEgK4mzCHbCKzOBM2f4Q23BMlrs_zVB8x4FeeCqxLYKzCrywHmkIkceEoTsNFGh_K0tLBS29shBnxNCPCQqVsymeT687KgAMLBxHtLK7h36n3VquxPRLs9GdzmvxQwzUlonI29BLDcVyxkBIJ3hUsSeaxaWhdZXAnm65lWClSLQLNmCKz02n71-x5pEU8cdKg5x4uyADEFI21au2vlv6YTsmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hH28F-83DMozoHLIrorNIXEqUXF4-0UCrggJfNk3AQJ9EJ69EnEOqfqDm18fGFVeLM-ExJe1GBO-y0dOP4uzrCY2Io4jiWuI55oD8S1EJFOvBflQDKOAUHy9lOwpxjzUimTktE6CUf1VYuRtZ20udEO7rsPjD33eyd1rvWOD_1ZMHKxY-BMAHp39yps7VtK2X7YK6rK_1JU1lM2HVkRWc7xyS-KnrV4PtYc1VGm8TpetUPlyt9w1r4f6U-tqazO1cjxofgp83utlGqerk91XNDrzh9wPOUruzy1g-H9h6hn5y_dolRneuqOc55r1ism49AU5SsNc0RPWnMMvV5_ldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pjhfQzxbmgXw8-mdT974TdJVzOOAv9pdTvH2GydwAUtAGjGWnomqj88btiyCrpfiZgPO6-2DYnd5kkkMJP5Y826xn9bwKv74_ha4j6N2yReUuOpwv14UMQphe3jzefDl4pgXo9-WszjLOcaRgg7jLZ8PT5z0p8ZTgXEam6ABeqgf6zWYhFRFdwHVqSLwXq3Y3ZCf7VsVjoDYTcfS37VYSi5ZoArJX5faBqsOiICmLYt5sVLkqtY-9_ez6aK_3QNvpIJLk4ReVVh9ThPbXg3oVyXeLYktcMo6Va85Z3kROQlsTxOcGTZ8xbl_3CbmC57HjGxhDDQpU4H2hm3PW2NDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ba1WnAR5XibXYEIq9EMzoVFiRi_B9kEkTtOKPL48YSoAxPaPHpX7tUiApJNeHkr8hh3JRZi8At1TyyjCXZfLThsOvin9d0FRN93GZyKxPQaLa-X1j9o6WA4e09gYgsJ0Jpx6T6RsStnWS5YAgDVfQ_yyyBu6t6xaOLGm8OpB-dPmrPibTQbnawpJ_HPQwJcFEgVEfvdYuvFbSPLD7Th-pcmhtEOS7Pe8BMaIFZ2chsnDso6ZLJsGGwLGgaJQLWEVWmf6YbFNXNAm2uNg92tGCFHWYxvpFkfZxoAY2b90E1mlKtJK1Y2WE7-AKx93x3mXcs9wePO6duZB7wJnemC5Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dg6sXmCVKWxV8dt4RwOeJycF-zMrzsN_Py7nDr6SHTZCKr70y1qMvymoNEbDAPrIpH1h2xMxdTI2xJqB3w135wMPkI5p9bjRllrzPgDQpZJvaEGimod8a_pXBbuet5E1qouAhLBheT2TBlvh8KzB1lijHRYa_KN2RlU7-vd9L1O0kyYDY71YvAqvzY2IrsDbWUDu3BUoPqAgayFsA4OmEMnQAwz0sGUe185Y3bfslRD0b9QoQr0nuDNixWB9jF4INCwX9zk0NEJydYBDalvBtykt67EpUr8in8Qi7l4hQYKKjW16-3exPgh_lGwu4khJoFXbkGrQR0_GwpqMWw8BFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UPZIDYvh24ZNdDD5JamE5V8cZgz9PEU--9h5HYOa-lBxibyrosAqdMuXsFY7xoBG_hEtv3_Qq_C7hLUpHvirQNEragU-U1OALZ_C4nGNSnCxMB9wt82bh8tAflVYhfeLW7pbwlM-f4QFRILMS6RwNWeJ5Zh3qqnSQYOgULyyqCrUCwg-PwT6K1M-hwEjWe21CX-iqFzaMilMbBlAyLfqrRx4OQYHc708hx94UJRnnAMXsnJnGlZzVYhQQnxcwJ3pOHbi77fRer7oKOHdDKZWviIqaZLEBFvM1nlNC1qlL1VwJ1dOweJrfLMpQOnRoSh6ndae3K7MCM_5Cpu7WOdwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VbGMtW7fNQ3UPu7CJjsBeDhK2kOvh6JVdFbGWUyACHyssk1bvSvHzo2nyhtiFfkBBrSHpAKh2VHie3OR5iqcPWApnZ07DSs3JUN_TInsMJ7ZB117UrQbh0VIfkWgINiZNsY40_pautGbWMO8MPcdr7ux0n_tRtT02FRRdImNBT9IvIvQIPCiNeHZgfA3dvkDvL7ym8kUJQi3Q995iVJqtbojL87gGVx-6Pm1zwZi6FbACWsQK4mEsyPA06FdsunOD-zM1FlpDfxKmAezmo3fYRcZeSuiLme_NyNnhw9KghO9606NZ0hs2tWgY60w1tdAUwGKhjlTSskBzgfNTGwnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MHkvxij0aX8yM-EbOz35d4mg1_LEKoJ3eXNwFL1vF0OGRtSRgsgkfdAw88SXuubGmhyAEPpQowKPwRuV64adunKQaegk9Oah2aBl_x1_MYb_ZA8WP2mz_J485p8aRHLBDyrX7kK7YBx-B84IeUtzRUgAoGTGkb-9jNDxEXx_eAVSiWBgj4dBEvMI_IWNRNk8UubVn3AUXem6LxNJJzEU0wLQnqkD2GU9yZBlBbEt1tT80A_rm6oCJeGOGhc8pXy47_OhifjuTzbCJBiKrMFeBLSXRV04tG6GQMSNXmpjJVG2mObcoMlnmVEFinYjhB-We0zR7Fb7Y7YpRMIVi8ysFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PpfPFZZSf4dhwgi8jAu-ZJrZTZff_HKIM14taJ24H_zo7BpbRKpd_iU-6846DOVdvKzSfm_NGio_wMY1j61IgeCV7mbVnAE75XQPxxoF0gTOpfYUuxG3QCmvU07Ja90f8zdVCX7lecTmo0yl2ipmPHX3LFVJWmEyq3Z5GXF84x5jZ-K9pfKI-_Y46tazsavl49P9YezsCy6V8-P_H7ZXlyxO5UZRv-ORJqxHkkikeWKzamfHVO3ugRt1mwtrLD7d3a00VZ2uW71XTLOHDcYwG330I3-rlKDUHIeTwUyXZMr991upyxB6_02YiR4Jbp4D0B8yzg8HLBOGtj3AzeVQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aQTpMZZlmccBhZnJYfEPSDfXuIFb3uLQfsmPycUZpoClGaI2aoLnFVO1rHjgRN6IDCM0TgT4kZ2M88jzGuiy8R3Kot4rH2v2thcss4NPP-exS12HovNXwp8hjhUxr9A9wQmOztgy8-c-Wu7jJPoszCjOWYQgAQqnmheuVC7qOBSwuJwtpiHlPz4kuY025Yh-0lFGIFDtpI9bZym3ZnZxnygGVaQVGozo9BMUA3Tr3RgC8hEBGymzhVrvOmeajhkS8zIqh9LeHHL_zq6n49FZYPauz15t1WoDM2A12PydFVn7L-k8QI-63eGkgbSNcm0UkPL50ATOaz3V6VhjjhkUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iz1lst6fnpymBCMBEip3ea6pqqvkzWsYtGAo9vlU2m2_u7DBLYoWMIzcShQl774oiZGn4njrsyWeDfC8oWlGKmKtD4qRxX5ihCxMwc2cJcQEPJXxKY3_-srN8yx1--77_sN4rV9Rvr1A1RIbuiVB1o3dmpCOcmn5GwPX-rQZZC7CR3kFjDdTN0Eniw-_NRB_L5aK0ra_vwXji7GKW-utxgvv-68Pdv3JXzOf0GQaZfKaCzrd6aMMTf1cKDIYYD72mLIVBCKg_ENcAEExsnpqoxp9R7iBnzFKuNIhBcc94LEx4vcOOdwCcY50vLOtUAAqSpySMj-iP6nZ4vbO-SUIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fundRPfAiei-ujZD1h4qTFhXIxRtiUgkxhJaIYhsqlD5CAUI_COqB9G8B2ZayJY5Ih3BAULX95U5qJUlUsW3ErTa8Fu0iii0QHHKpRvK7kJfDNVl0WW8GQNsfE50BPzos2VeYGZ4YWJHvMte2W14G0RPQ8zti5_Rd7OCL3xNoUAVlfs3aQv9KskJReGOkzRQH7MAThnOGnySG9zMaBhjLOZ6tqmnv0ShsEDGObnMqhjKwA0VlEUqsVyFDU42YwssYLsn9UyJWrJD_NXUcQC-z9-4lwCn5R794dR-WvTW_zpdqPZEILVR54xEduHTMM5rBnQ_Ua2frAN5--QdyaIOvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iU3U5v2_T61hVVUa4uHlJDxwqtz7hb5O_TGd75oDI_i75kzOHoRCrF4dflP5Gccw_JyGpoFY7DmkimHZHz6JgcgM3o_2GCrgyyqdfiUXF86bdNP8jyUplx_IjGvuPeZa8cxMr33gluqoTwcGryRDPZLBJRAJ8LXxh-iW3bt_Fl7U0Sf3x_lBUYUjgM2MSrmPngt9dm78dBchbaf95MaImhbTOXRrnn3B2YZnqib29mZH7HweO-pe9A34bL1_tXS9SMCwwK5OaQZ8nUVOZcZa5HD-o9gemwQUX1kDQb343y0WxU6eSekKF5IdedRls2k9eWlrJev1-iLTTYo0uBWY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jVG5GliklC7HxZXjfsSlS_G98DSB2tDHNwhlStk8kFjehGdfwSMjpL6IRuPo8pZbHSa2VzHQBB1d5gho_8r-MvUwNbrbrb8xrCRFQDpp3-jutd-KWtYuU9gkbVdLKhJ-bftHOKwSnYCKfnQiBoe9PG1B4u723FeIgDZ9Pnqa074hTGbe5iD5uBYe0gAfqQYrLLmHRUX4S8QFopydW4ynRhUrBIOgilWlWMSjmGJTo-ULpbMd5EnLGY1eA-NxypKJsinYQsYJmR2gn0b2qj6vzO11lbNGzYcgjNYCC2TbUIgrxMQwdfIZM3lOHz3kv-1zNKQ74C1GFN8Fas8mrVU_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dEdKG7eZTJM8TNh-Yq5ueojS6kAB0T1YM7ycqoYeh5R4gTwc8L6fYFm1MKnW-789FQiBUOA6Pjdcw8BMDDL0yuDKzHZNa6n4I_IImRIPW2nRB2ydGFe7i6ivkFXFCWKdRL6r08g8wDTxLgTk-F6qVMPEnNT9y7yWxfcC7pjwxz1B1gUIEnGtgKIMVSIjeZc90KJJf2ZxkM2-XFFv49WWpNJNjrgucccpQ8mMq5TVGFmpEmfVuJVO01NprzGtbzoviZMPfuc7cUTueFA03jGZFlu_mR3YmGlPnsHd3dXFb3GvnH2Sz44Bab6e8jux8AjSbYm5ORhvlGlOMZZQvnVDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L_JkKDFFfRwQgoaSEW4NWD799yUuz_8rNPtJzmg05BbSxSQmNjjd2wxrzVZghGADunr7OyEN2sHtuO74oBS0-MEsQcQFOuFKaPe45MFiNxS7uvuYsSs7dapnixDWpAQYyDPIJBIMk4oLJR9nFQVogcKjpW0D4qvOQodcNuirpETf2tEtyQ5cdX4ejlQIUUSKeg3mX08znUtxKgz6cUNeBWwhdfd1oP5t5AjxEDLiRM1umBBiPrQ4Koasil6HBTDzej8tPw1JwOji1JpVnCriSXJuphVmL9_DC3ZvCVNaydAf7RX6F7pXkqEPtneIhY4Udvq018-QSDzzRuQeb0MZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YWa8nALOxF2sS2ZohW6_ZikFecfZnPRHN1NPXJv1pldD2GmME066rdIzh_9nPXChAk6MMjxGKHg3Q5Ksn4qCe472hPwtgHYPky-0AN_g9Q4venFdfUo7bgVFqWkHHBj_GRKKbLd8Cho8KJ7WZKLbbG9LdyL7oTrKrsnvot-V8D_lRIu5VL15d9Wjqm9ouNgY2xCIt2jC1uTgYc3tg90KwaWZdWEQBe7PE8qdY1PSEUGdHdQ2s6EvO9egpMdJxUfFk6IXLK_zTDmcW21pqDwbG93WJk2UuZWWN3rwoCVxR8mM1_UsVFcI7hVYAvFyVVGUfN2rjWhprmhqkOM-pgG7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FiM4TVnG6iN-QSrGV_U28x_dZeg2U5tZBLaKU4Xacc1ngySdcs0Xy-G7rjXiaOCn_Gzv12C9CW5OufCU1L_3UiwhWBArj_49-V8EXAWt8zkEninaVFaLLe9vxo8BiEBYPvT7ru2GxnTq4I52777RIXbGijPyc5pgVT1Ayg83G-IvQrrlP4ZbgaszDneqA1l6ezIW7YbxKjQ22kruAyKVP8BCLq0c6JZXd9TkulFsYdpeLHYWZtq3Fgs58-gzinJ6CodrCy8r_AhR4StgFC7A3VF-bYqW04EyLRYtDlXrkjjLvfVS014Ffwt0pLvRzZ7QKw-ja8S4yM9b-ggRvmRf6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZyVG7_HlJw_Q7p7aSv5n0BvYWTHAhG9s-PQ3om_ADwXuGJfWqr5PQkCUUW4OAS3PpRgODCCjfVEh5RsZtfMZG32-ynejD320FgPsRMKhVzBpqwlOhB3l7kuAwv0QjWifiY6AN8pCSikFQBh5G1Mlyi6IsrQvf-N4-nUvKyVz5ttu7PidE8gFuL5FtB5KhD2AAoxAe_5Hno7L_Vb2k8LrOGq2gr-nHTwGZibt2xL5qr7vaGFqWMCfqvJ3WwM0ZBISUhTygx5FaEA0TNkFooXLvBYH0RVsRW8_aSRiXSzR_NaZgwvUjOCYeQe45QNmyKEpbebPO5hEZUwhglobuby8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S2cbXsYXJieX_GYB64IzywMMVxE-LuPIgb0Zdwjk6jGQ_owsnDEUUSOfQ1DpzhFA_coieypmhvOLlD3fJzMrGeCcKsjn7HnRRuHGda2QcaMHOeCBslgTJYN20r-4zRwgrKR1jup2_Kmtd0Higdmr2LxE6nD5UiWZDs0UyZOt5pJwm_EdqZAC7BY9zYCaqP0Z9nx71M9ADS-cA1gJGzuRw3BWIusnhQOg9E9MOQZLLl1jFZhF7er3yF0EijkuEQx6hVtZNv_XM3C9KxMKKTuJ5DAFiqU1y_jbvOr3CTTm52Mug4VLaYcdGIS79NEYTfBZ9rEEzVVCncx0orktNADqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SsAp00kFI8Ib38ACLYrSc3bMx4DEZvjS3v02iNEb1wU0x2I1m5EKUbgBiQFRdSpRZer1lMpHklTkWWO_H5_x77j6o5sU-W0ujCQgE-H1gl1kr8-_eNjVRNisRVE6IAfFWRqE9ggs4WSrhrTKWa9fB5YXRYtjny2AOn8oG5Y6lNiTo5LXfZ1BytYabJxkqwmNoSCpiWIc89omvBC5MzRTz_moDEc09DwRllbSblESD8L5U6U7Ni_D34Ka0nRl6jIufan6ezFaeu2mGPjr3cAaktvKW66qp6WP1L3BgRVkMNcDmpEkCPvJcjTA5CSS2of8d_-3b8TYQifhVbcCzOom-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KLb5UzraDFEodhO1bXVD1pe3fhy1vGMfFwJRQGNjhXlDqNTKWUL8ayKnQXYftxThnIKyMt4qMntLMyqv5IedjxwnVRgxhXONzFei87I8JJWA63LK6sjc_70cw-qw0KgYOPqaIwP1umQRLyhWdwjhpGDPwMMUiZ0rBsfVIwMzcJd1JsEHG5TnfoSEL9PUKSiivtBDKZglcxfiUfFfGJ_jmKZgMWgaGRU6x3Yta0t6pHrwzyJNa32O-6wyy5n7sHXqgW7ZpT81p3oCDuiHCmIWMLyJjfUZ0r3_HY2Bum5QN0Q1iyh_g9pJtK7fIxnafL-HQp2MInmzuTmGB-m-aMxbiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
