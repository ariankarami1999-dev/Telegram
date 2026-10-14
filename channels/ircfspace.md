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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/ircfspace/2677" target="_blank">📅 08:32 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/ircfspace/2676" target="_blank">📅 08:22 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/ircfspace/2675" target="_blank">📅 08:06 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/ircfspace/2674" target="_blank">📅 08:01 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/ircfspace/2673" target="_blank">📅 07:55 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/ircfspace/2672" target="_blank">📅 22:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2671">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZV3Ze2aDLSyQ3PHvd-dnqcUg8OyPjZMYlmDIHA5uEgge-qi2dAgTdGs9fmG7a3REmVeW-fByH-iqNRYs0bWi7PvN35xbuLNlCflyLYqUyNPLHChNP6BxmQsGTsX6GOFt_FVs9sqbBG8ME1WA9mHvgscN90qq1e101rTVGCG9x9Ls2Uj1RdV3clCtusEL5VA4K78Wg2tJwkyfI75KJJLoUtFcnEO1m5kaBaYpPEB9iJJw3_ywZOUgdHuIKYtTYQzZSZER5r1eFT396X1D9Oy39RFqKHB9kxDY7a9WEKO2WmjphEM7E8E9Fn91Gm2mKghSQiUIsqKLocdUptX2gIfHCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/ircfspace/2671" target="_blank">📅 22:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2670">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rkLdcKMxcf6fQGaZwA9FxHSMsvOwxI42Kg_SxV1e9ibyCnns3hP7zU2bMgo8liWN0nEw-HQFB827pUHSJPPSNCJ7_BOUsOXecpsiKX5uzFhtxO5WuXWF2jsPICTUnAcD5qwnGsMUqq59JLpVSE0hhEpU-xk7VE8AF0ANdDxalAdjhlC7GLDE6gsh5o_zpjZUO91v2eZoXS0gPBGzTOg2mrjNxL01N7iBUYZye6JJcQ8PffjN26cBU2ESIJ5KgWOwZHiowNgND8AdfwV_PN3vPhPvljyjlN9sl5EhOaw1eYPoiBUliVLxMEBvuwQWZ0qPZYdZnPZ5U25JXzZAXPPlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌بانک مرکزی تسویه ریالی ۵ صرافی رمزارز نوبیتکس، بیت‌پین، رمزینکس، ارزینجا و تترلند را به مدت ۳ روزه محدود کرد.
دلیل این تصمیم تخلف از ابلاغیه مربوط به API اعلام شده و می‌تواند فرایند برداشت و تسویه ریالی کاربران را با تأخیر مواجه کند. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/ircfspace/2670" target="_blank">📅 21:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2669">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K3Xo0b9w2_wXo_y7IV6PQnypKusHvZJrVyEeSLL9sROUzvMPhgDbR_DhGJWPVJ6d_-ws0ecCBqYUKhx36iP4mVGghKSZit6SudbfM5nnzJizryAlVbEPupmQRx8_T6hWUtPb6a0najs0F1vw8Cyvxh5HaGwAKPKtniodfz9g-Gyg3thwMk1ZlYkhG3jV6EgJelm5KuzoFldEeySPm9uYZtY_tkb9S9wKKEw7ENxUylHwEUeUbKROFUtOpuVvMUnN-2DTypmBm7e6wa_Da_zlF18MrYI_2NgtPo-ekjVYZosAN9p_1XlQk77PO_-tZHF48ZmqTCQkeFogZoPrrcOM6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/ircfspace/2669" target="_blank">📅 21:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2668">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iNm7fcUNzJGV1aNdtHaBSHQVCkfDDw26vb3isSssnqk3mNbW9a1Mn5saoaqoNXOJyMel1Vyu2q-hv6_RnsEK5LWzCUKpx100oZyPpb6oZNMPcwWYlop1ZtDjwjjPdNvK1HId1XzW-Bi-5bmHwUvubpvQ9dHhMglRRZdyUbxvCYL-h3eVbGsZV_qKwE6pBjow9KF-pbqddoeyjdh2Kqb85nXs2qpS8-Y70V27QJnj85BJ51nX_odW-XGMj3QVGj4lg_QvHp4tDSuqS3wrTbsP0znjZ7JOF_U8sLy82iMCMxTsjbVeABQIYmFzvtkjvlKuVcX3QfIEBQoT7B17b2JUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی حماقت امثال شریعتمداری حساب باز شده!
حسین شریعتمداری مدیرمسئول روزنامه کیهان: آیا حق مسلم ما نیست که برای به زانو درآوردن و قطع نفس این جرثومه‌های پلیدی، مانع عبور کابل‌های اینترنتی از عمق آب‌های خلیج‌فارس و تنگه هرمز بشویم؟ کابل‌ها برایمان دست تکان می‌دهند و با هزار زبان می‌گویند چرا نقش ما را در این جنگ فراموش کرده‌اید؟ /اکوایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/ircfspace/2668" target="_blank">📅 21:44 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/ircfspace/2667" target="_blank">📅 07:47 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/ircfspace/2666" target="_blank">📅 07:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2665">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F1qLZn4t4NvzlchncjmaBhJQDR8gAxdVAdWtfYf66BOGkZ5p_B1ARW94NF74EbzE0WAt-wd93jOfbV8RziFwcySsvwwb4fnZKL1Qu8lvW0xxpsAcv4t8Hz6XSSgD3h8BpKlyo27z7D8fqYMz1bQTaDn9s580i5yIRIywhUmH2kGdGoHzZRkyXBwMTR6qdqHfoPLbDt2GRPb806E2cvWRJJrdOouE-NAeAUZZsUTnVjT3G4Or6Ry2TnCaOaajHExajnZFvVczLe3brDRvLdy6L_3NqOd4wQql23Clnoi0wTQBuzrs3tLXtf4XXXgOO3q6PWAvNrJrE6GMGK9YR4rf3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/ircfspace/2665" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M1nH7uuKka2IB8kTejr_64AvMtYrdjbB_CeeEHFM5C8v7pWczgJjoSyaIfdWpezkEnCr_l9R_ZGHdFxe2NGh-HG9icZDKsrQU3DQnD_qSe7Eo5NexzzqBeRD0RbXGQ90xN7Lg19Jyw7UOiQRY35OgpL8yUk628Mb2Ngc_3emkTEMNRwLQbXeSX6S8BaW_lJgT62YhRpaotSpPMZDgD4ozeIl9Yxni3kN0JYFOYuX17Z5UaCMj207T_eEBZpIzhdMFD15rbvs1Mp1gamPlHwIPJHKWoG1tjD9N6zMebwct96pU9DkLpP3pjqoa78OaQjIOEAuChWBaG_JZiRW2u8amQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2664" target="_blank">📅 22:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EgbvxOw85TkLeBx84s2GN4jY9ytUA-UyvVQQ6u8JB24Q4eVkvEry9Mi1mfgfdTeTMea8mZxqLljiwNrUi7G_sUZkb86bYezsT2gFSepiNsQd28s13kd25rp0H0_UGxLrIW3m_1g6dLEaBTonIkUpwxZvFxQn-0ZbLJR_nr8FuCGAAOw6udFTwdGPc7JEcb6uIMUrLDHElgtvmcSz_ZqQImTWoXef4OJ_yYCSBs4RtmPvqUTUAauWxsXgubn05pIZFHzoz13cpRjzo-84yz8sJeI4KRoTR3rqkeMEET84xoH6h0UEF2_qG4QKLvpYy2Un1f0gT1a2qL-GD1_culkCSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2663" target="_blank">📅 22:08 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bb1imAeWI3V3tGr16iN6j2w0y4TF4oY-y8pfIEbKjMm9viuhSDiafUWOxgmVvzZ2PYhCrlG0yJoGjXOXNSCpDYBzWiKgAlmevAIiRE28ruEXxbVBQWelgeraXoqE254s9BatIakC27_eQmX8-01u2Qq_8k5Nn1OTmrL7KSm-vWQMlBwS7s-nG_Uxso94FesrVO8LNc7AJ9mpRvRQrpFCHYHy6nS6NX9bhSDkQ97AET84ZsXJt2aFFAbh3aj_v_ORCwlcovUPIiOfB_sAnsdhzsXeHQO12V6AeaH5KFgividJr9hVCOTHnicxlKEgD8odiShkSFwOhS4w2jtMkxoJ5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MXZ0xusb45PnttyczHAaEFXD-aGgSLLLoBWjdDZjpSL72jgXgSy_2bTZzYBDDeeeGEGrrrNTQ03qPeUdD783sTD-9bRU7msz2tgWkCL0qlIvSCor3ZldaaQzU9ZQ2YuRPSKLZkzOzv2hq3ldd1R4d7Po4lSXrD64GmOISQoCCsExKx_5xY3axMp922zl33D88ygRndURb9vt44EAbw4MHwMVaszm7Xk4CX4GTfsUAR6Jjc-KWLRhx3G8laIeBOoH6qJf6WkX8VjdS-KTNNIJxmhkrmL_pQrmYkqUYhcUG4JHH7epaRh95KHa49X56i4zx0UJx6cJXhC935eka59lHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NU7rNvClzN475wWe3PlTO0u9FMYLrBmBZfbCrTmRaeFS7dRmD3W4pgf9_RMLeI4Cvee6XM69CMEcryDrdOA5iS1ryR2IotbZPYaHPRCmOUsWzqV4Rpf7gtACU3TCW1LW9tcBgfRxdkeZXhK2sATlFfg-NyHNwb75m6n6msK-RVN1INUmMYJvqsyVrHp57uqX9Mob8ey11eU-zuMcduhjDaJkL9M6gzz4HMyxueN2hymlDlk_wKHHw3ggNkFiDA498UsC6P3pQWlhlNpWKivcEUqpVc1nLykeAPo8S0m9M62nGjaZCZjMAgCcU_XkD27docFRaNCVGRbq_Mwb94c7Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O750OwEotWM3ZRP-wCqbMoTGO9GPQChN2t_zV6knBIPDxu_nYSbi7-Ccngwiys5uuNtSQVbWtuXxkTkGMk5a8xOWKNZBM0itdlUEspsO5pJl4AOYhp5SWyYHChy3uyuy-yczkcykHz1oo-seJKH0cGO6QtzWe2xouHjqDXLBIPiO8aujUKJaVLAtwcj67Q-_0kTPxgeoRwEDmVW3Hu9ryoddUkYWmvS12kFy2n_LVC9jUKXmVgKPiV9tGE1nMTZNG2nYT5Y4vqZ-jWYQYwYnEkeFYEY_n5mVBT7bmURiNphcJhS7HpM67FHsafzPRhEidyY-fyOytX9aPuLG9SazNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GPvSdKdSDTSClij692C-yLt3dPS1DAaVW-si0F76FCzmZVQyFbp94TA1A1O2KH2LKoIVUXNUsQyMWFIU22qfqRGRZ6SYa1smzbdyU6dfYECCk382LQH9yeSPEVNrY9h2TAbg5ANcuj8j2J7YYH-9EIbiHvHChS_Slva1hxcA0yelSSc4zBrq1C8gDAjuqyF8WMUkYNf-uM2HPNFwGFzZMiuH42EkKOU9eNTR0fRYiCSYhbjWsGSCs0FxWIx_nZhXCkuUEnk41lLOy55nqoj4mTApzxi4rTxDdQCzvDD2NaESE4f5T81-_M387W3f6aIQTgJj83lJZU7UtgClxwEcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vVNQNAQyncyv_Yy_VewKNetl5qj_9zxbLrD1BxqXWH9atSLN1vDdInMDt7dn611fD6_6GBKQ6S-nLoOAwNo9qAzQ3mtkDAP_oq36bBmYhEskmZzP5FeeGR7Xd4ZnK1xeaBLsNHW5sjyjZph_lSeUb5_rgjyYmL9NnfJ2r7JGs4sWH-DCR5Ro10WfFdlVeLLww2c3XkPuCtfPB8HkKfkFxAUcZhdITlRQ-1z0E-UMVxW9VdXCrcXWgs3FU-AYM1FuE2FR8jXKeTtgA5KBjm4H8AzihCKhJWaZCWUu9yFegcuUr8YZvm0eaFwnLIBG3tCFmJyfOUZSkuZbJkDZSCeUUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F_vCQinDuLnVE9CbF77OxSUuzPqYt13OqcHX6iBfSoRnG1xKvLbdTezhTNTGCuaZTrYixdZ4srV2FeXn30wogC6boG9q6qlY5OHCI9tiP_99WHhzn4tT1RaIcGB-JVfddPM99NenpBCosy04gj2F4vhkT5PzeXGe_kVQ52VkO6blca8KSxJwc3q6Khexs9pjp-HInknP-FpjcBhs7L680fHf_QAlquouu6WWK8Zt-dW-AWaRtHtS6_hfdxjYpL74hbjJm9EUcpLPAm3GRhEjuRO9mhXpXWEadaPQpyRFzWuPfwAVoVVEzpbL7wPHLli54cADJvetbVS1nx6L44u-2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 80K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WKnkvBe5E6AXMbTa0RaOeNoGoyvRaXLz8hiaicHQStuknjwmFbLj4VOGWoK5HDGYtxYFI9fGY8KNRoFWglOhqm7mFueyBJv6EeQLpUg12ElYShxYL_MbkOMmZtwPpInQTHaxp7aVXeUR8EFKGYGpED5ixvKxatxKZAUAJv4OiFVIbKM5iLn4DQN9oUHcZqWjiifX6Oa3vFqnybfP4GLdSdSOPfP9yfFaOSyJlqf2ug4TAOzlJTdXz1a5zfAwMqE83nxMyUXHrBD6zsIN9uCioWYmU2Ukk681h_OZkAT_Z2lgfAtTP9CnPq4jLOAOde9nj9UGAQlQhruk6W37dvI0xQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FKb9afPyUqV28Mj3hTtqxODaODQ5MvPi149jCG_SPHdf6hRXIvJm6VYkecTeh7RkQW2C3lOFIMR4WNCLcMqBM96EabefbvNHvTkohBYNWAC7f4jBGBKYTxy3xs2L5DcoaM9Rq6shkRnuN1CsCetJUrfKlS0JCoe71HKFqRHAuw-2aDIkfgh5qDfF_A8HZcQG6n1XTYm51-0wlw6o5ugphUektet_k4HnMk4KqvViRRUD0aXOo-Bjhos5EqfN0FXA8NS3wzFom3wTygxsBI2aswfeadrFx5tp9DGXPMsYsRZvhi0eDJOzhGGMRKlT-Ezy4D3Z6UO-bsxm6QGfPGNR1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sg_4sHlQ6QtffkJPPwTWa8gLuDgyRVkOrqF9XhdD_41IueIzNk6vM2V4_IiK3sEC9_mP3fhGhLdsSwtdVzFBUuZi6zcspAnoHJBLoY2muHHP0Yg5z83eokd5dzHz8oobXbZCabeLeskMlbkVFfjFUasbQiAEY5ibaAjPhdqFJrZt2TOq7ItxPjS8Jw_MzfLPty2JwrdsOIkQugD24Bqh_hAl5rl-lwr2IXQUQhYRS79aFW2VYg7PjuJD-MThJH9fej4081BYWn12T53Vr8Im_6qEocorXujAc5mCMbKeC8rd-hpAJcAgW7kLnVGThweQUpzoQFgnodLWmPQwAVxVGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BDvWe454PniS3q0uhR3UrpPn3Qbw-TK490aIz7SPjeSwjiq_-UeIjwSQCJbUEDwjeSTA1BWdSU7W5Vui-A6tGoUJGZsHlEkd5PtFDcQpqvtJh7KRxAYvj0cOf7wYt9T-pN4JMDNA6A4jeggVerufI7MzkK8ejUGJWjOyLXmKLASr3b-BTk3D16D2j-oAW_Jud4LFhE59-B3nk1mQs9XOfddV86FFHhREEsws3gxJPvt0OI0DnnBS_NMlEN2TZZvGkNivD57m2iTA_tnd19t7qRmZrPESfcLZfsdA0SK0NA9ewj8RqNYTJTpIcbYMC5GaPDPbkJcdapvWvClpB22dcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MYu4niqcWwbf-g5Y9ubSjy7y6dEY-P_8k1zuT6PLZdlNh-BsCjxTiEQJ1EZsbHTzuy3P5af0W4aLd0RcwQ9J8HmGhLF74qgo2vxVtTYAPgdG1jir_leKbO2dxCDJwNf3dhNTbkN6LLLE5GD49HzFH62efIP1cbQfQV72x9yV8Sn_IybUTo7k_k-qZ_A1uxzXPyHlbXMxyJKN8JIHL5a9-li-80bCtSTR7twzFOQMp26NpZDf7Rtl7uDkAc9CVpoC_l7MW4xz0tLsToAfFaQT7eopeHV_y_6wA1cMDZuk-flUqE4y97jfmttPNCRzjNJnucI7_K1eVfkx4-1nrbbfgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HjcSnhsUPEvRjymucbkpETGFrnz6fRWaA5zkKJezngZqDas0xPSlh1bhcl2mgBl6YRTueiR7DyW_FxRX0lUhfjvylGtPsxvhG9iIsB7twEODhpda10C6JVbNvHn1iO-CI9fA8zNhZuiRpkltNpYGvu78d9sDIWzBk3E1Cm78V-VYauCBQaPDxz3eqwL4zRDsFDlBiqP07vAAc0mL4_I6pOuqpc8aLXkkW1ehgEHGRZWAEJtexXqpnA6DxZn7w9HGNSRz5G4RE2pJZPJv6DxmDv84tdnuM1rYMol78eouzEAWpJaJktLzBItXOmonfaFBIApuK-1AA04DIUxW2Irozg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IYh1okvww0EfyUEUHemjxzwFemqtc7Mr6B86HUH7FiqXxICXAKjl9St-o6qemGC0yDNot0ZeiT7QiysHg95Na7lNwAQzbhGmmDAFvBvEThCR6zpAVZhDezwEEyvX5SQr6fQtNWY0ixzYbr9hS7SdcnN3bY4OIbGpDtMFtHJSRbMbtC_39Tv24kLvu-yMxfBWTmg0pUSEihe-uVF9tUvYsg3rVBlVWBv96MMReekRNptXc3QhCZwaoJVUtYNHTTXDENQ8BAwEGMM7PVJZpPVuIcamKYLftNtLIvRBGtpHBUDykqIihffVhkyjERg0RZJJtBuNLSklaM0h5beMvbayGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HPPchZddjt-a4f1ptZMcPGAHc5RmMuGer4YRuIBB76Gdh_EB5DBlVA2GYON5mk3XsLfn8Vf2ZPI0N6B9Bu3k5jnr1aoAbWv2Um4Ypp1DH2CW9i9-67e7CF2hHBOVlhTIXC1ItXU-NW4pI0JVDlb5p4Bzd5aEK2FiP0x71T9wax5xlQ6r5NzZpYgY9q7RPjH_NQ-KAwowojmX-Z42tN74U5ov7PMgtYq6J207nBde21IOhJc_2fUZ-FjHEkIUcU5qSj4VLbCirajC1ckE3TfRqC3VUISSFMzFp7nkEZpAlAEK4twe7cXyUbdoYaXjvqsb4ewtTI9uF8lpC3M_fDzhmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PrnEPOsNG-7mWNtgBiXR3EQw_iweEaKZCMErDoAIQvvDHUVfF5ysSV8f0cvg0fQdYbUgvRhlMPNXNt35PBMGK3nNHOLGFE2O2bVtBKmQW1blsPcbNhWEOMBVQCHnQ_tCvNslbk7-jkN2cs8bhW6OBoEO2oECT2j_HXMRylPJkq8g7iUl_g8no9vLxbYUgXmAUBm8j06RuOj9isz1VPXB4wIg0MBsMemOgpDZkZtTgBIt-Zip3gP5nkD2PksZsrN8OMqEdfaMDmhusBjaH2qRUrnLA4gz1ucmsk1lBoMh8_X4MikKf-eUJCk0Ww3ghzbvHtocG3Bt9SPDzFup5hlWUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lpOWAkT6OmuQ0TvWego18OSNDWtFBxLZyNyvQ4f6DSPrg0Eo10rO7W4VmXJVU-BvVbc-IKo7tXUiOmgn92KMlsERHQ9mFEICCysE_y5V91SIQTswPRFmXyay1bMLZC5bQKeSjrG9i9bikvhUfWOvQCG2oOg6vzXFJIRQMCjaM6qe-SMLo0nB4JDehSBAZRufYPc2-3XYEcg1SziKFrYkZcvOqeNKRUM57zMVk4zv3sxmprBmFHxVjyzSNpprWSQ_iEn-D68ImOA3l8ylgDNLGoQPudKPhGh023P8V-3KL4jhT8IkWOQSnqAEqszvU2FILcf6FMLCbEsiUulNR1Z8TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QxXvL-PjzXSudRc8fFO24rdJKoXpdQob35Auho2wQ2lr_Cb_wJkKOaNBf9SylrWKX7d2gs5Ib64C7hmyy_xfHU_rZAse7NCJAMiNjsNEu2xMzJqXcIDueTPG5-Qm9wfChFxQiETrpgAZvkDQHmjAFUVFl3DbgboLgqjvIT_PN6Ahe6QpRx9fRJcNbWu4Bt_GH5RPNRDocqx6pgogDhUw4yZyhARneGn4Fd9cYATXe8vHQ50vj0GBX9XJCA0vwdQucNGt-l0W8m2bXzG7YsoDPEy0tGJPfuzCm685yBruj98suZOVKuvWRb01fzOZXN2RXJ-bdi5AqcjW4sgvvxgY4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SNtRVVYzsJEFurREY1gAtIRt_0sTQRkAAziBLnI6BHDIon9Njq8lEhN-bLj2Kbu69wl1fs2DSp4ahQVgq9KasGAPDkEvv6Ro0j2MAekrxTOb9z2mYoa6lZmlb5ypN9tGRYBOwJULE2sH6juetRXqHkF00zyOw6Pj73Wq_qfJvcHjknv6lyjM7h1J73HoAR9TYSRt5gAiptfCx5xVrYA7esQj_jUAbwSMPgwF0V06XEfIH8KycmA4Ge893LZfQ8AYXs2YaS2RU6bhRk2kagRZcoe_Tp8PE-AopoFI1NhXopyXPwzc3cYAP28_9q07HYCv0zjHJTW4J5GoW5mYS31OFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lg0jtwuODAY2OIIUfLUTY9teaNKQFTy_-6FdvcUne2odhVa786QBrU-HPKpITHXUj2y4Me8N_CbhDx12gUezoNC4g0_x6tr89IdTgC878N6d0-ITk_GjyTBobQVA3f2DhojtlFYJnesIcVPWx42GjHRou_BPtAgg4l5bOElgrQapaZTT_Kfvd77bXbUAapKpiK64Gck5rll9UdDacQ_3rLFpL6a4rqURyy43d9i_7zozFiYxfA6hSbjGXoXPSyKvX4duvrRH-LoRaPX4w5-rjGTTt8qv9OR5H5Aaod20vG6CwVacJart6KZ0DVI3Bc50Oi2Ri2uNFJAWyIlc4XsW5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TYdau9hAJ6KpFGIaarLYnwlxPibwvKZeiC0RK7K8_0Cpcvc3nh6fCY1gqKgG0se6PtgeN1twn1YqNbUg49tg-lwKOc9G7CGfFiPNaJQIrOYwwRllFw45_6gw1J51FMGZdubsYimsgGvKCK167lPTLJnexjUxkRyj3szFqrMrp-8UB4mr0ZYEfpJ9zJrxlCdpyjKjrMDCiI3awDA1Mcc1xEcb0PLVSzKF3Luw_wXxaDmV-CH_tCdNh1TqynMCVzYXyY1zi4jbb7CHoNaH4bpGlT8l0KVWmDP8cT2YUh-x5b3D-BsidorA4cNZyTfNGYmpUyEG4mfInf3bz4aL2oa5jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K8cqTl8n80pDl_iicgL2VGe2jbexPtFfpoakbacj-Xt3SLJpnPxdpDzlMNo2AF3K70_-hA0k1fbJYChUQF1yXViBv0WcH_KXTDIaSBzAhapy3V2OfeBhJRhPZZkBgj6pMVIQ_RbP5jjoBQOjW5nByrdTD1nLQ1rkkWXjKggHDK6Qh5v0sO8p2gUsQ8QbYtnFN3KDkkgvThN1l_P5xu6Mo0k-sO1Km4RUK0Jzx0lJgZglJL3db9HowfomBkCSGxrjQjaDR7e6PztW9HDHr0bOZsriGoCFZMNIV2o-8yL5pGvxRmsH5xvw2y_la7cZz9Xyv92cT-5cdZsaT48SThsO_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XlRQX-1vjXIXENv4j4E28-ehEUc4e-Kml_oxt9lykbQSKcyAeaa48U4XDRh2FZWhp9c4MGT6BSVdOACSwxHwNGYfJfw6iss4z7TIiHN2x1AO_3kMceHQaqBQEjJoP8uSX8XMYVXixAVjc1u2O0TdGgRGRkzCmQVsnMEvbQLdmU-tVswzVfwNw0mXzwYglw5eHmTHNjvWw2Vh36HxQxk7ERwRQHsglo3fcxKr4-pahHf5lNjgU0DK11HMWiHSbkVv6A0Diw4bh4Sc1siqmdg5yEtw2uajM-k4KeR567h7T2LEkwC4PQ22tnC39JihH8ZNgRDnT05SHxgrzB-v9Axitw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LDghNXhuM_T26bAMXw9gV3Zpp9561M7EqIKUK3bATUv4EzRbX3zk9vjGisl7DcIVdzn-pZvK9gcXLbSyuc7bAPzIkDo4JOC78Kfi2s-PVKvGOMg6BOjaDQfi-WvdWyCbha4C-r1oTTVxORyVtnXUXCLVioVSDh2OoPy23OHOLV8yTq3dQ5Gkc9JUCTrD9DiXm1f4LpKypVIUJ_-Kaqo6R9I3_3yFbZHWEM_Z01WlgJrXycRkE-8LbaT8x-0PXt6uec_o3LCQalVkDRtRuXOAZbL9JOLl2mvGvB2bL6dKFyVkg_OqOE-veckEwzfCv9CkI-4U9ymqsQodUNPLnAm6tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lqHv5wzo6HUfX7Yn604d15ojVu-0RD-2gQkFa4qPRc6LXjSkJn51jR1XUxZgDiWmlWavPKY2W318kDMbFiHUkS5K4zxbVy2FL3xwOCoWbLDKVIGAyDQh8K576E4lnk7JQwLNDLpPOr_7FQa3HzKccqOlfmSDAdGIest64B4bVqtOoPXd2-gEnHEXTCk2x-QwoT0PUeL52K0WXn701C7vsd_l8wkCiumjTlekoh7e6OEA7VQG_rCfGoallqW3N1vL0RrexUI40qsE171886pyV8dYYPxKhC15iheGdmiza6Qo118khD68eOhHX1CnIrxJDVNSJVVqi6hW_y6bsIJD9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ou4aQyoZRIZrXAKc4DggxMPahMZ_BvJds0dP6eIGCIud1qWHp0DxeLGW8nQC1T4Px_Hfy3IAGEiFW_bwfiXyvoo5Ph4fq7tV0D58WxuzwqjsSB2QUo4m45oOokRVn9jd_EZjijLC7fngIf20EzY9W5g6SikehVcSdWndX9j1qntbJ4X1ZNqaa5XlhOqxeUNL1gDTtLQrqfDg5HURnex0TTVOaJkKlB7K5hCEq5imsyV5CeOmjhqSDznBn37C9JQCdHIo9KZ4-rKcfz2wWqr92sQV2i3xHQTVdO8Y-b9b9P6hcqPUuZurFQkh22rdnvjsF3XMXRegsX0-BzO-35E5dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HfYBczu46v1nM0yDdRO91Qn69nLW-9tv8jKKyO8UFqdj5fGY93vPz2euErBTi1cyuWO-FWJz-_qEKpUybKXAjnbC-4AUeim8j495FO6XGxQQoxnZCSDJSqCdDm19A-UrQ7gNHsNXACs2EUEOhHXWvT1TK35JASKQV_F-coKUuFM25J9i7SJC_d672-YeVTlxPsRwKzEVKn_tsMxOdz3FEs9buZqaRoBrj284nhi8nq0vFOZvtZIyq6WQQBSvy36Mdn7zkuI74e9uvQpmmAYzijCoErTzh03ILCcGPxDHp-qUZQylqpCnQ143UJVPBuWulERTeQDoIM8q3pp3oJe10A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NZo2gv0XoyKjxle7ztb2sgtxxEw44lRQPjuv9Vja3sWmgKlqqgTlmawi0MgUz4SwMwNadTKfsf2yAMKBfinh650l9BiSLPgJvaN74AWGspbajAYr63O0SetMbeKKLyaja_Em69m-OOlRntfTPVrXSyV8Ofe6fTil_Y14W1k1GKhZT1nLlP1s-cr5-WAyOBsF3KEL0jcZN9yC6slGytm8f_2UBRJA77Xeco3QKSlIiVFZ63zGq-4uBJyAFnIxb3H1XYPVoVnsWm_8P6seqJWzs3Y5sadfqpltZtzj1MQ9iiV_hnoGTFpP33Qh3Mk1HAWJdkXCilm8OlT2J3fDEsaCgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NA2xHHvq8BH6EqN6syTv8EbY8p8b6_nfH6bBbgICitKBf2kAX9YAf1rX1rgMT3yESC9FAt0ZGepJtD-UY73PqJXKtDhH-uXZdiEc1f9nbOuzgfSu4fquGFnDRuNLg-sWzjy3HpZ0o1EJVXmjDQGj8HQZ059M5F61IWh7xaSuvxwxMTpdUumb2FEtiqINt_WPz1bJxuUulY_hYPImI9J2Jz9BgxFZziVHlyiyc6KUtclQmyoduOwpZIygE9D4QcFiP7YS0_GpMaD21ahq_Se2nbZCr8HYlohMH71CjLGV1pL7Iwfu-aWLjXuL5uly4vBHD7MgYbkk4cJNlB0j4PqqIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IbCOTeP9aAun34FFnSLXvGIIsMMf_l62aEgn2u-W9kf3VT2oYF7xQY_W3ktDS16HKHmOU4ZoAZ4E8briP58a1MKHMNbhEbKj5Zi-H8JouSc-rhX6SKFmwt09b3LUandY89_lE_hLE5Ok4VcofDWRgKXFkhokTJM13RrcBBiTqFBnE37OlQt3VkHvwVUTG6t2-7fYyrH_3CDX90P2gN6hSirQUgIadh8-htIPBE-3FVeWYzFhTzh9FF7zm03Fq42xAk5b6liWqj5Dt26ww4BNZ9XcS-X2MaxNxZFuEJdPB4P7Rwk3_f99xQiyRR_JRMA2kZkOJ-BRwu8emV2IR-aphg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oOJTLRw9rh1fw5N19fTYDAAADpGfUgbr_WpOFrMj2dEvyr7xnxCxmzgBJepo6p3hYxHt8q6s0XYvsx_XyvZY2QtJ_io5g-fwxed0qPAMIhO-z0SZHURL-zP1LzS8jplptwN9a_MztWYzCy3Qe-sdCdvEtL0rpMs6_j7RkyZPVzGmYlkdZmuwurvYsU-6VaoqvQ5sN1RE1EY_rtssaOoGsYzKkFfUlWA0Fqco1G6bDfP-lvvwFIvnk-JJZqBOoKflwSBJfWvhBWwvEHzAZq6tUfyOCdDULuPP4wMv4qYxNHDb_TDp3KXzelbvwwUzr5rjUFDOpPAMJqhqXpdjw0oK7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B8GeT1SbgKqnKjZJmrKxS5y_6db7ZXE-DHsTtqC_MktE5KleiK3iAPh880yXibgzQ0yQ3ay_iQ9p62DdG8p9NgEhUoNJ55Ig8jNuyQxw9IH0dzZdAvStP44LwJ7oROfzkaRZKVcYBGaZMnCGd8mjkvJfS_IvhUYyiyWYR29DU8rfRTIE2tiFAKBHmMj2-i_JSeDc_DK8P8tdCGTUQyLb8mrQWivixc789sQqAbhxpXfr2CWcRIrhXRGlp1uW-vNF4kgHjRO6T4p1L1NkQgtln2SQmFW7CxqLZusLh-bG1Ord8FZGeLc56zC3EDcqCDhFrpRX-OqGrcJC0jnsN9suJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OEUU1SvkEeoFZwWZKPN87_1-gZBXML7oCC2uhpko95OrnBtUGbcGyN8f7uvhluFqA0zhsodrFjnfRA7aI3HUf1x7TbLw8ARsMFVZsvXtRFaFsVxS6u2K1FWrDav8EW9-UKxEyrpj1wf9pHwkya1F_exrVOFxPVjqXSE4jE8G2CrUCzf7Z2oOp3WrJYQYcwhQ7Yy1avtsQXlY9zaFu7yE7HMaL3cqpooVyTMX5jGgCwfNM_qbGLnLtS0nk3JfVTUdJmwLqscR5D9SU3D_yqTwLWCIJxJA8zWgBVD_0GuI3bkmzVFeJqOkANC_UbVpjosoU8DxmVv85Xpi9D9mKbxKCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KnG7DmZcma8rp5AZ6zzTpkpxXh2NnKRaaR1g6ivNP6CjDQ7Bsx_IumQcptmBJ1UrTAO7nwk1pKriihrLP-Cffnr-WEVmti3lFJ1KveFQ0M9Vvz9xlrYmAcDAs7RieChrdkjuEUTnMTQS7NooGKPFXafFxCJdj0nsZmdRi1B8UzURSMz4yxq_58YsTUUNVj32K-5ITjYKReTVH8_XBDdezdUfb2Uu30pCe-r6bvws9iOZDKfy30WQvYG4Uu4oNKnuN7XrieY7yx7F59O6gxFSx5hSYCwPH_XV7mkiAhyvulLgHtPhuSU8j-qqCLTx2KwYBLO_H0vZBPSCxp_PjYB6Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UnHwEDXOsGxAdsgRJLTypvVM1h1uHdU9RKSrNrXXStiJ-3XbLNA6HKTM4vXK5XIZvz-FTCRntDw7zcCK_0JnuZ64ehanpIDIBzZzd93IemW8G5V_9U_fjKj7jzsYhWuffjzQUXhg2VBvvUunxxQPR0_aFlC2UzxvnHA-23CDus9YS2EPC65o6XKAwqH1IpP330Fhzv8PGpYX4xFsBQF34JU7wkpblvbyPrBlbdw5e1XGX8Nreck5OZoy9VF_RgoeZlKRe9urveCoSbPmK3i3yiSWi55z9O72lvJt_sQWOU2G2V6ff__LupwnqwunahFhNLQIYzQBs9PduoZ9Kyr0nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/grKRju4sLkzg1KkMfNwPJDNlS5yMVkYWVL4z8UIpvJWH92M3lNHPgh8X0IlMLNEW2zmQIzPPyc1j_WC0qaMOjYze7HHmqRQSKx0zP-_KxJTpfuMTOY5-TkkmYVsxdw8HiSJ5FOr-EJYjsFYDTpheXbLDVqjsAoBUb8Dzy80eZ9e-q0y9-uAJEzA1Pcn6OUF11Lb8l5LAKiPUaL-opBKr2guNNEFhowgpOEX6K9kdT17RF0kwfAHjBQ605n7n7WnQk17PZ72BgGuoSuvtAt92CanfFhXKnQp6ilnfuopkR0mqxzOLf63KfPaCgtM8AG6SeEm8IY3rvsPmDflAWfDYqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oMWiaIDv_xQsrCdKURZNXdKMqV6e0W0JMY7Q5AnwD5NJDfSB9PQKOLZ92BHeIpslW-GDenSjNQagL9VTkUkG345wnzASb1vs4nN--gQSiEQKUGP7Zhzxf_H21rZik6jB2I7HGscBlZI4x-qWgOsiEAVOm-7Xs9tKQV8IaAThYJBXyfp4u62RDpgWP9LqQH6WG6ENoaaffpAnXZg4lMlkIYOjav6jT7xyg3fcFG_MTrWjP_f4O7xbpjbAuitSQzXOFMnX1cy4_NVmPLX6jgzXdVPK03_15jXiLPyJy3trsv7XMYCYoFWDYggwGaN8syGFSN_GoTsHzMDmwryyOKpptg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pq5pbke8VTeLDt9jXZhBk95-3oaI0FW5MYxiF6BAtha7FRS4F96NvwjsysLSohVgRgVL-dwdC9nGg8OI6rWUE8o4yG515-NSC3HLUcmb_aSV2t5p_mwDrEg-JwlT4EcWg3c--F-NSvh_wSHNxtlj5W4iApQlLJS5Ax7LlXXfZhV9NwFjMAhwuhsermdCcAkyxxX8PhnYrlWeJkUaq6ZKxtSH_lGu_a0ii7k2URXUbwbWk-qOE8ULOcC0NJsh7lcuZ3iny5V6vwL6cbVqfh5GugGISUamNgjJsPvhNhEspOLjUIKgemj271ChKUZE4ZB41oOpKPRsAmpiC14mV-7Pqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tFWENvPBG1lqvDHjWil7fHzXxHyp1C51O94Eie7UxZIODVPZnuT2_I6C567fVHGm9cXmDZu3wobrNRbGtAara9tRHmf7-7Z9-KIm-PM6BfmOPhKnE0-oumxS50vfntOkMe_C9Kh5ytQ6ZCI5GRWSnW8LewwxRIUoqYeeZA8jkaJXg8V01qZY2bhl8vNu2JkNcVZ6HaEWuY6S4YnqhY48CqbXSxCkV_2dhnEOAornnOqSoNZ1DCY8UWK5alSNWhtQWMRxtjq-0hDF55rIG937izJuCB49ieD7TvGMGCpfylj54Is367Vw7a3jJtrQdk3bYVWoZBvl3iEqpZ_O9QUFMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PiFessrjkgQMdqNe9sjjSvaE8Xadv-C3NbkWVygjws94oK1ZuD1JSNNTLMlKfUQ1MWdYCQ4073oM2wmYP5F5-gaSDoLVCqylYQo73dWu5Vit8FLDF7u76_3pNwO6ZcIpzPOs1q7MLv4cDo8zpJAn-Ydkw-8c-P2gmgddUcXYrevug1qEiWDGsOmdP_p-_hVvSKY3qVxXEnghffyo2LeTv_kU9EfDkLyUrtMXjbMzHzIO0oNHBGwod4WhClFxPmzEgj_3eKDETxVkqPRZFB421JqJdzUWuxrAiZBTKXsiQeA_ZTkoHxnVB8QkyUKDgxJJjgl9P3L6HKp33Mgx2nPw_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LaolsPRa6_8smFmS_TSNWz1OVJqAkPx-QKJ_Gejx8SBQh7jA1TCRuQztwCBv0b5vGbjhLXbDm8nSS-9sBamAsYWGO0bdc5cuD1YbobSAu9FGE6avLrNdfzumzzXJpGbeX9NJGZL3tUuhYrcLKtBA_dsvGFTz4sbXAEP6udoQYq3GNL4nPV7BxpH7LiSkyirvFZH0fqKwr1szxvoC51HGIVT6AdAAWinILSjt72YmoVT1joOHSGJonP_6v8mviwVwrOfjBDfcf7qU_bUyE1huZkIAj8USS3-k9rYqpCZlfBToMiaU6VynKP4f8gz5w5hnZhwxLkpsc3iAhgROJ2za1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V42BLPN23Iv9WVx93cALeaIlBUnr37qvy6gYkVp-My_5rLYu3GnSWiaO5pNbaLnq5PWnl643Qsha07HujUbq622ZvfemJSERJDILyEnz4gJ8j-Bbjxlz7z7yW7nB2CwwE1Nho14XzF6Jg1xRl-aYFDNhToCxe0ITpp_KIHDMbSi1x2g9lq1TDBFLFLP-dq9wasf5ZDjBHxchsoh5pd_i7Sygau_1BirBhxgTmzs2zTNaGdhVnMDBFk0s3feURULsn1obZmNVhORPVfkR38KlgzQ7Z-De0Ibz-HFTn_V1mdM1bIDG5c4i8YmsXFEOY3AWQzHKLTWp1RijQecRSWncFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AlEmGF-ydz6fxq3hJea5lxdJXXuFm8hgNDxiYa-ZK9WoIOy4Wh153JaU0AmX3oXyq5KHZP4d1XiJ3uCCLNga3yRD5jGY05_2QJU7__4ENKgHzhA2eWMZdrWQcm_s4RrLoYVT-hwUNn-0f3GEeCPJuVz8VRnfAf_zIK_mT5WV8xbYi0qa0fuT4s2q_bzzpKTtMoBbi-uyA8xeROKoa64Pgl1mMO6OMFO3Ihb6fzT3rRpjxRVmzjtAlzJTwdvuYNcvjbRY7eVbKDs2F-fGvtpDlJazRuyV8m9qhRfgPLMJ5qbuFv-ye-Pia-Vf7w8NfNEg2uEjolISXfLsUyj1DXbROA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MwCnV801X3ljA4-Csg9CAQD77nLseWawG3MoY2CxY5onjZLgT_Y33cM-WwN7s0KsU5SvxJ2QgmesxGiECJ2-JifqhtHnDzr4MHjIbWpRyWEAnmesDGutNNXpMmA0bAMKYKV384KfNDLFbf_EuYBrQNq0sJHZk-S6cFgtwq5JcLQUVgufV-5xCv4xY-02Y0HUtcSo_gy8QSbADnjLOf37p7I0AW6CpiSzr-eKCAS4bV3AHoekScGol0WQ4rUU1tdywaGtucoZSCmOTfku9jBKOD6Z6WaG_nqRvyM6HF93efRjA4uiCR96kM3dqgt6UiyL_wFoMlWZY6F3bH0JqsdmBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NyEk8l0RlJKfdPtsT9WoAtGAxJTStPCSfLC6bsxm6zA6cDlzqZYZZYiIpkxDbaDp5piNMG3x-KI2M01AZmn5LTcUvvfySN7amFPiA25WcIGV7vlKDP1rU5PrPrFB3KZ7NBpiBNET2pDiwj5YSlxt2AxlyAAb6dyJcyOqxAGvB3auZRd6AIWx-FjJWGkFK4YtzCG_5Fzzs0-ZEIJUE6AZczUsY1x2Apj_k-4-SKuQv3hpJGAdR3L3jWZ0IljZi5grdRWg-tTmgx6AmaR-EQZGluFndeV3Cyki4foSpezxhvCusyvRsNtdomcuc0cifVdxE2VJqx7jqIw-HjB4WqRjuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TFEcMdfoMiLH21upkgUxoZ8BUHOkDWjZ1kOH-m7Sd6HJZiuoYSn9CM5iHss-7vujpgKJgcWmC3BVpR3HsRhQqOCiyyf1zKeeKjo4QnU5wdiqUmk7jamaZiKlzFjUpbLyNRRUOKO56zivlVW-JZqLWxG2aFZ5ijrXAbJyfvpEMBE4e1ljzq5NsKbmsZbNd4xPdZdiz9IItTbtd6z5XNOuz8a3fY7y83XPpDcZGvnHh-t1vBH6L4suGasUnYMKeaFIrbp2-1paogMswXIL05by71R-VVIXaF1dMDvBZFY4WyFXJWbipvkaeCwZaLibk3fCmZPmqNyYJJLI2X8WOevxIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/quy57YB_R12ZzHItlb8gzFPeXpiXo3wlqgZei7ATL3RskXDD0HEbmeiAxqpzq74610jFimLZ4MxNJZ5eek2KIfOu5o_T7zv6dPAzE1NTLvI6ELd_kfdTTAmDSfCOQtiarl9yIBkhMJltRCyCrXIpVUeP6V7e8boFo4-oaR_0lunmcUncf57gixpOFnHwpRLPyDu48vWt3K9qu5U2cU7eQNtPXgkPWFuq77Dy5ck3W0tgLLFuwLRU_-S-UezDKbt1AvJpcR3Cvk25Y46_nuNP8U6qbS2zX6Ji8VYLJP22YMfxe4o3EMQOmv_I4WMvWpCQjb5d1IexrhL058vguV_-Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lMXY3zwrTcC4xRW-Q64_k5yPBfamEOKiSanYSJDoDN1QEFidK6tNpYzQ9ZyXene9_847Nfbns7B_RMj5kdkxyhhTRKVUtfmhXCFBLrbIhD8nGsU85B3Zc5iP4MEgP0p1q-100NxjNIAZOzm2zWIENweEg5p6Oh6_vEuNTSu5X_d3qmmLP13KVMijXCueCsOvgLKwlNbiZ40fsC3Cx6Ht_xBhXpvA5sapA8tkzxHuRvlQSqynWXyOw2QSJmMuLcEUorY84pF5OCYnpCLRNMSdORM5ku9Po0pVfXLO8Jbgff9-r9wV58pZF_Pwdtqg11FrMDDF-e6nr0tgaoa_ZEu62g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYhkRTjE6wGnS94W7x9b_7nwDe4Yxl61Wa65QoQ7qq8B8I5S_DVT-DHFYei47XOIJWQcQuxoRkr4muUys4q2Kmmbfk2fgq_pQ1VP0p7YUyHNdZKi4kPjlnQ2i-t37tVjsL81Dd6ybtyTxnMQj5wq_9GUioIxZq41Iod3P9C_pd6Pv6zloxheLsGrnbGi-pWmMH4vY76nQZkxk8MC8oxJz2Jo1Q7-IEainjLhFcnTzbf_LvzfEeBlP0Dck4zxq9yAfhNf74UVigQELFe-VTjoozw-h6kjeZRaZEBOroonTnDExPsRixGczW_h9q-Ax1qqzti3E3CdJeUAS54jXIegmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MvT7zHTk-M7u1SbC2UhKWFTMBnkiusSWWqXJeZgIq1666SZyxgXuhaiYk83b7a34Vmn-RWlaBPWixtZW77Psr8Ub6WQKuAfHaj42hJagcvsnA7uAeg342CUTUoWTFT33AVLaCrR9IPQ8LBf5Ti3oLH1GZ6xDIaBHjU3gzqS3v8PWl844AkJ5LH_-PLMWqywxtli6DhcX9wbMLCgabAORMJnJmjTmo_w2jpA9V83KiGtlR3wl0H0TeC4foqhnZj7JbnOz5Tomp_wp9YNkTbR0xSYq-7IYrmP5J_UDb0Zl89VV-AVzZsOg6vAnfeiZ95k7CGf1pyx1lYt8WLC8_WnKLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MZ0nnUbrvJ8oQyO8pp0v03Wt-wyEjqYepbJBHCQJiIdzprbfgBdZZqSnHA3xuQ9UaLScVjaiAyPXOIwksTO9050Kb11I_nXQwqipsih-MNR7FNNgvdEDbCfNkP52U_wyY18NQWgNvjL57HgEZ3S9wGMqVPVoj-3U02PUjq93qVaUQ604Kdk4VfsMPMdnFvNsIormlAnZb8s7cp5E4njtCfFd6PXlrcogdQ0enIPCUTvEkohgxoXLJgbqPwzv3lTrj6f7T1nwOL68d6rkWaR5Vj3KUdAOslgMERLknkwmAbEqKV8MR0Ke4U98rfjSEBNpY3pwKAzbw0Lr9MKKoS3cog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rus2nWTYz6YcAyhc5qiaXVgaf9BIhNqPDvLX12nciqh6LcBMgZLHzHcBvjIVxqbj-K4_ttxjp5ATwsmOELPrL-puSV3ySS901wb_KdMxMZUFS9dvJACE7EeSF-85qfftgDGYTHnwKYXaBuj9QSOe-EzOWSaqOb4TXIvb1jPUamQzhSq8-AXEb5dbgat4kgaKZ7CvrremD50BTR3kWFeFG9EIxeoRfu_DJnYTS8R_3sFWJAvfG9bVkG1gPqzOjwtcLKFE_vxsf4xiGexpDDamvf0uxAzvjx2Hdc7-byMnYtTISb7eFjKTYpKdoF5pQhGcC3T2JsOCy5SG6c40iBE0CA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sPjxxErHytrKlLR1NzUCZQHRilR2bnRNEry-JXE8D_njgzdQgFXSkiprjjWKtluzpBjKA9fSVN_sLCfsmonVuULzGCQjpQQH0Piwi7KDF5j9-7m_ZJfgEkg7KhEaSJbpGKVMTMM4tBrZUPEYoV_9isRNEs3TcOR_nhWecR4FU2m6PXJsZxMT88R01JZPPXucYSHXQguvVfH94h28WcNexC3UUuV0pRwU8wgCUqjMNL3--pP5v_L9iwHl8VGW9xJWT0LSvdqzxLcDm0eEEl_bMOBOsKWutxQIXz1nXiLxEcPSf70OUON3BNd7tVDfr6yEqdgOM6-FYzJ-ylHQnEv7Ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aAzRcBK-_7qZp5GLpt6KLeZAK0BrXpMi0LpaPyz5dcq8eCpV0Pd_cZjJNBpTbaFbG_Z47QCNu6-MoNpGrfCUysAUvuaUHzENm19n3cIkQOxKQHoXurjSiHZmOxgSIPdoN0PJUXCSn7F1a7CYUEgLNLo0DdMHlvk1RBUN_N-1EzUF5_gdaHZn1NCGnQ2eg4tTFfe_rxwxfrire3McwIxYto6XxA6JROwaH0Y9bAk94fNuW9IqFUGxwrTcA-EVF0qxdDWQP1IC7DgVTzPl-kgL5Jd9nu5EbXii_W7G7bHJ7KRsiqDLTDZmXiIKjvkvrDPOpub-vx1MLdUpVKmtAvpcsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CyaeVTvBGRrJf1w_ucg5ImsEo5nD1t5qwS1ZQP9pdrtouIURI1rVvmRYBPdAGqGj9h9iKI6LE1O_kO9kD5CZWvbfCcKL9lHiIY7LnQByXgAb0kSpBdV2sywJVDJIoXGGZKv6PMhaedx3o79teZcIYOY0ajZJu7n_Pe15jZzTZHNEATVxpf3CPUiBvzitMTP0myTTFlAKvTqy05DQuv2uMEs4pkfhWj4ED7dtorlFvePRf5ebvhv0KfrdTNDXO-4ecs3s93mD_TWVSmGOs2cTH0tFJzYQtFZi97imEDc4I4v7eUdOouU6RLlkQPQsjzgVNntBekhrb4zWCh5kFglzCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J1Ww_lhJmuPGtwATbBY1iPNV9g3SeBdoNzO8qRbDZOGe4xMdX4dAJMWFDOLQ7UeosMAIe6OAbyYXMGmt82kRqnZkhgn7OkdRxrvbeg0UrsRl5evZepf_6uW4vFfUYOiJ6WbA1FVwAWqpA3hoOrCskC49T35RirZbio7hzH4QROFFTP7jp8n7kDgoPsweA3VWG56nXAvpYwAozE9ofwrZucd_x3AVFcfIw5vt7ZrpbLQU9unFHYuyrCN3RT8B5nIAdwlhqNv480jraYrMUZqXyzpMNMmvmHScbAMAIr49tjEkWhlgJT0FG_iqFO8JRb3cRvnARdXSRIXbFu6nYcLVaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t5V634OHs9R_psz9vCtKW7zrjjM10V_k9L2sM1dAub6hCPW1_3E2IJ-arLhTej1Fh8GezkxBxUM6eUHhI7ktvgswDTRTDu8_wikBIq2a0qHk01gM4_00N6QcWmejoChB73-v-q0Ap74cy6lSisoLDlUXyGx6ILecsFCdKEX3WBblabAdjJc1oECs2wZlhs9ZK6DhYbjUHsMvoiIBMVEAiVWfo_U2kaZbBOdSgSx-N8ananizRLM1aQ8NCbl2vUTv0mSiSa-ZoYxR4P75Hbi6x0pxkrWQVGjfB7XMjLGLZoyW9KQ7lK4kug2pp_V725mjZhWtkf2alCEJZG0AIgG3mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TGwKQa5jyNlU-2p9bmDthRvqrd1XyIqgq1LV95QH9ACaVKGIiPUPD0kNsq7GIHgLRH6KpeZvvplb-EN4yGNWOVVkEGKvctVyDylpmlmrCX0Ld9-yrQcUS1h1T0Ddh9ho-f86zVKmUIF0x9Ct4pbF-12DH4525_zVYYK3zmotJgEnX97_hu7OwG9UhOx8AIhna0LIa2IqdaX8stU7seki_59b6VDW7OFpGb4DFa-CgASZSxdlmRIyid1-g5r2d5xbc5FhCQfZgyV-R771P4icyln1s7N1pdvZShojmTHlA1TDVRAqYcxU7r7ZSEvLcPDtejmaf1wLnokEG43ktzOpqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MhTNhnJFGVka3JV7T1Fx6Q2dpcCIXYtMiBKunDpVBu-AkU1Y4CJmzAYNqKWoKiqjHnrHRZjWGEJovPCzJTrF3kxvI0xKoXDzYd8JaYu0ja9f-jzuMZ2vFh8pBrtrM_RUssKrlLXb6s6h9GOGRSCHEVX7ioRcV_OkKmS66woB7bDH7zXxYq8ECJTIHoUF_LtBhgK5EGWFCDLFOVClYdcEp35BaMo_7B4T9s3_kD5up5HbzEsBmnjUCkddZL_w5nfRrDDNnY2mOSiXZ5WEHadyFd_XvjCQ-BeeDgq5AWtNRKZP6VCqhz0mf5l1IL_88vNeBk7uE4J91q65ltko22GCLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KH3QDn8zPZQfsLm4cCIMfwUd8irKX_qX6-0DnzRjKczRmN4WZ6TmugnzRWvgw5i3RV81jnfZ8ZyeZqiCyLnJKO5p1QDCV6OhD_VIdYxdDk4ljMxUtUysbkhFUAoKkLc7Woj6ARALpJEJf61L7UsSBYaSlUXDfn0oUr0_baGVPRmVbmUaov63Xm4ddSTmzmPDZ5Ckymt9jp_uuaIW7oeo1UW7PSxRa0Ps1HNjydECU473fpFJmrStxHcRJUZxVnajwKEOoNdmVUB_Q9EYGgFuvQpz6Vtqt1Dt4vMj63lC3ZkiSGGScyw0tTKzUExY4ysoHz5QaXph1HA7srabuGxNlQ.jpg" alt="photo" loading="lazy"/></div>
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
