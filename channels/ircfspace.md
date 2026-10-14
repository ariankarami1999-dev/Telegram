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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/ircfspace/2677" target="_blank">📅 08:32 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/ircfspace/2676" target="_blank">📅 08:22 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/ircfspace/2675" target="_blank">📅 08:06 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/ircfspace/2674" target="_blank">📅 08:01 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/ircfspace/2673" target="_blank">📅 07:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2672">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dlt5BobAsiycDg7b_broWrjpuu_quto6Q_5vHrJwOa5MQiY0RGr9DMEBgmLD8mftqlmVtcAssY33uEu-IM_Xhu954mMPvoQ0lx2GjA6vkrzCfVxRxjqHSXJ1euEHZRgpaCHXjT_ZofgK3TYt3MHYqI22p_3YAA7ep7EFJa8tTwaOKirdbqdMp04h-SkArEGWn-A7EgIj_gJ10Zf60ZF0rMwg5tdUJlVG1_MZKWHLpXb5lPsPnOwm-cQ0qHZMbRwTgN4ECqN9FkCWSB0NwswTVio5XOZBT4k2uRCKEHXfp4NGKp2A08gLhHKaWYBVy5r2YuW-xxjBPfsxd5HsWq3PNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلد مارشال محسن رضایی: در صورت ازسرگیری جنگ به کابل‌های اینترنت و دیتاسنترهای خاورمیانه حمله می‌کنیم /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2672" target="_blank">📅 22:12 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/ircfspace/2671" target="_blank">📅 22:03 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2670" target="_blank">📅 21:59 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/ircfspace/2669" target="_blank">📅 21:52 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/ircfspace/2668" target="_blank">📅 21:44 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/ircfspace/2667" target="_blank">📅 07:47 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/ircfspace/2666" target="_blank">📅 07:31 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2665" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2664" target="_blank">📅 22:14 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/ircfspace/2663" target="_blank">📅 22:08 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GcVx5Qo1GwxG0eYe-3W0eiTF7BIx97kMs5_7f_F_r1fpuOMefC1-mtxdwAa7W9_aHqtJXPoEUJL6Akj3VWvhZPqrQgbBJMonF5NaSG3LNVr69dJGqEmd_t2yrfsw8tecx4Ulhqbhon6PK3vlIOR9It3FbfMsMedaS0m7BukWULOjQbmi2g0BQ9vmhKHgPRdLBvZV_gL8mt3Gy668nB7Wo7Na4q9bSfmz0rhSWCuwxu9SWmLBI8QCJC8ziYwo-1q3zAfQsc1Wg46qTMEOJkvV-BJuSXxSqHO-N6vkmg5N_Vrc15UGCpEYTaThosGm8HEcXMYwtxc1zv2A2bMWCoJJew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PVEh7j3YQcyVwE3ZWUu8cg_Fq5thkyQn6QuMwBoK57s1BkaoYzkIB8fHD1uXgoRejZ3E_36CljdC2tBA4CSbkPiW0ckYcWKo_2iXOwtkmqUgVIKYWkx1HWvWjuomW8_fS1XOcTBz4D9xkeijtDk_gxP5A89w6-1FlcJLmN4wb1YdeZRt5EbopBD3QpdGdv-3cAykD7NfPCRMm3VlmdZ9N_3RCQEaX49PNfn94sOcb-3P_3RuTfpSw1FWXLpAxzQFbIgupJfKg_czZcphZkr0jVABZ_f0ytnZ-pi3x0f8b6i8Cjy-hiNsk4aUrGy1_i-aprx2Urvjkoxm57Ujpei9YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qZCGJQjsFbl2FJJx8R4QcVZhdTguWLh1AZzL5eqsSMKxpH_scfIiYVSy4xIgfP6SMC-dYw0B0TOrh7WcuDlhAXPENIh2LCkXiVJ_7pBL8Rhb93AYU3udIzQAcveMd3dH9IWJ8xHqpajCcTFdpt3h9FFDarZ_lK27DJIKh8BhtlmYxWRnGemEZLCsQHzkWYbvhZB75vWTB0bG0AE-uMLP7WswMpo0BRFctcl2A-DAndNou-QiGjMUW6KVVm5sHJNlB0vHUFNjH6q-Sw0eUSnSP0pY70so9Kt97tUpbclGdxQ8gUa8MphCVcQKEdsv8wZdWk2M-gxDtmicoPx-RJG3_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgbQvTP7lm9Aiowxv4hvIfBt3Yy_XPmAJoiAO1o2Rydxn8GvDAGhImOnxnOkFxWgdb8f1jk0qKMxzJcU0ECOF3DlDwiVeB7N1-xc3_vhrn1zQ73X5OQKgN7cpulAF5sSTgD-yexgsLKZoUh1rCEnHfS4TqPliW2V7TqPnyuvOxh4L6qTZ-J4OIYh_7G5Esp81H0XeYzDB8bBThpIdRywjOeZwEgU_-Sbx87OxmJNlLpF2xI50ber6BX27d_bK28mcqOo9FHVnqwq77y5FdunyQyZOc4wdzmK-VyMaKW28pXmU3GBmQiCmqdU-cJhk9xhPNl-WxPFU025ux050nv4sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I2AX7upzsQCAD0FNrU1IrVWIaPhykM6hSdI5KqRGOmzqx_8KbyRj0wH4aRyvgLbMqeXFwdpSDDD2SWg63TQDyuvYQsvJfB_-Ymd-TL3fZfFsdtVbPM_Yh2nUuw0ANCy9kRl_Ns-_4ONPqsJpb-ntvvhIwX6NLrkuIiBge2TFasLZtfhKqUBJS31ZDdXS7VDMbD9xH7T7GaWUyQIDy9STNqc5P97cSbkdrXIhhWJN0tOaO839-BXqXSGqGyuJxw-1uEV71QoPsv6O8Vax3aDdYE4pk-a4ZxPSjpTsN5Vm0ea8oG92kXGs7l9xEmlj286alqiRH2CZwurag4d8uhsRsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MbSyBwJ3BqM3GDYjJsJxtdXPDnRzgbe6cTFKHTBCluD7BFwx5c_uD5OjtJI6CmEmTEUofX0kIuKHjQOzMKJ1_y_HG6JXixSlIGovYoWY8ZF0s9Fzl3jrlAXAE4y5uHv7PZMqY5E5FCu8QCUVI3NWWLqBwjaaZeRHzpFswRZXoR0cyAaj7k7f7swOI235leNO8_0s_8ilFwFDBOkzSBXw3N8MrNsQlzCD8atphBKxhQ42G3DHFELee34jhXGLkWbf2UhDbcwsS41HoaCsvMnLwgYY6davFGtJRnv_jTwc2SZdX_7UP6tkVe5N-jXgwutDFw2FS_YD42epORl3cs2hWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CFe11_SBQFVALPTTg7wvEe5WuXSuC_0p3sw6IwpTSXODoVAdxzd8nm2Ilsw_wLM8dytZOk7hkkA0Utyp2k8FsYEMgaeyxhdnrNFIU31lzgrfz9bLifQt8z4ZlkL9M4y7WspXVJAt-pC75zQ2Hubg2TnLUNH4oBV-0XGK8a3qqGabvdoq24dKhq3ekML4j3kiVKvaxCpHEAQ_ZkiR-L4Sap05D362M-InjFM013L4Gh6ctHsF6Cz7DrV_0Cuu_9fjLxfLtJ_Yhhxy8eZJYeaI1NEXDCgE652_3BvvVuaRoT8Wmua2J5jfwOJ3yohYHUQb9soNWImdvTcVyqV41ux9RA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qCwdyS1wbaAWeEuWyhAahTacy8docCAJn6LsCrybnnjBW4DJ9LjajtpiQFz_ADP2FmH_cUB3xiMZ0AFawDZuMX2a-plk6Dy6PJ_ZMk1MYqm3f6PeIWyFH2ulqcCNijcuMiX9mvykMU_Vp_-xxCLOYtyAgyNJ2Wl3ippVp64RQf0kMUdsJ1A9DlfTw8y2q4nAiPbKVgTZBd3wmma3lwDH588Sd9eK-LBX5ro0LirBjJ6F-6hIpux_Z4y3uvlMFxcv0gYho7MkbhriL95_uIanIxwHDoZkKJhsjrvAf3SY6UHEAx8sNWm1GI2a8xLx4BvcY22OzXB-flOkm1HXJKiYWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hx8KHlU1HrW57fYQrcV8aBFjLSoMQayCiZUhqe2ADqHrICDTm7r91SNBczFo6SfUB8nXCl6u5ThdPIwGfJfvAVsNIt3_hD-kwoCim2suW11s87x7KCvDimkcmlXjkcC4nGgV4KpraZJl2uLuJXLFa6UiG_z59hONtdOXFroVc8NfEZ9FsQk4xrBuOTtIS1NouaFHFBPtSAfH57sw9acGYBGZKr3iUVbKiWqMkUb0tJzCX1wta1kaipojbPZLgXWCw4Bv-D3Ari59vucTo4Z2YfVbHUnlPu-XTng4k_6wFVWfpuo-zuJeebcqYBlWW9RH6k-TeO4pee3WkFLZ7UxABA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fmV9RfqLjxLoRdCgry35mffNVzg_tC0URZ4ZzbBmtmVVxM1kUrmFmmNOeGjbu8p1XvFJpSfhUAtHGd2yZm9AvdSx21Z9VhZol5L_cT03gcernPSNr4gL-zROzfOwAf8pEJAy-_JdW6qYbyLFthgnlxU54INdKkmbrFuNAsx6V5y3Y5eZK0YTIdZEHbZXsLNnqgDtqG-30ZwqhC_JtDJfI6rp5UMyBQ3Gfx10qFCunZRwm9Z5DYi4-K-XtrcfwiZo2SIBkYVY-t5IrR9nItNojm7SLtBnpY97WCf2a64IEcS3Voppc5Gto5issUIqoylSV1ERhGySzx8ij4wcmSV1xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OOZnkQQEGANeqFuZW7jrqlxZi5CoDgmGiM6UQrqb0S9whoR7aQU7I8yi4iBTLl2vpzB1t6tqU80S8vztPGhDXqyVhWHIhL1SlfqCHl7tyK3YqY7uU1gFAz9xfj7OPkQbGVeIPqFOKB997LVA3E80FYCuY2ho6LKGE-r3aCdPFTqdd8_AbyYNWNNN6wG5qjbMuDI5jOjffqfUciYjwOwsObCGOocKK2TWxqwW4Q9UQoRtwkiVibuWglr54V9XC3zl9a-_epxsGVm3qAVPXziOPoSnVt_iN1CNL3CVY0TkMC3iVJLwgNnw-uoiUo4LFiDzJJXMh-mZz01qCIMDcBTYEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J9teEVPJE5bKFJgU-sz8kyYXs_4Go7L9ERENaPGiAaDm6TrtTVgID3ujBKxdoKdBfjzT-j7DlIcNc_CyoE1WTF9M8oWYkG3rA2uWlKeaR_IgBo1sGIoQvm6VBTwMcsiSS6aexBOGIVjDLhsaAQpSWX5R8GhIZkzg212O3t1uqeniAlfu8ukchjYiryky-BjJ2GmdkH5RopkYUMUbjNOy-tfY--xasDDuZoVd-OahhFvg61bU2WGVT8MulTrdzgY8KAF4WDM9Da6z1OH2rYMOV_4fKJwfLXuD8ajPCte1k5YQwFkvgrKV2gQ5Djj4QBJpBq9iMHPpPD9bFI4HnfTDMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vuf6-MIFZ1hGrLWxJvSZ_dE7artaG56BnbjcNEvn7bjmrXzJ9XIuridd_7c7WY24Llb33dAwzc8QZrnZA-t6ClGkBLraGoXzeByecZ2GTh0WdBH_fCRbUdtQct05q5FNNbVDe1RfDOXmGvIX3D2yc9KzUea4ChAgkoHzYokYmyBL7988kIMoIFJVQCIMeyortdp-LC91ZZf1oBM9IreqmJs4TBQ49H2lz2SvJmVELpA62HIL-ktkV_tutcgeg7rztI8574ccg3pqvn4mHVIi1oFOe035Q-Q4n0i3_P4Iz5IgPzUzoQNbEEX2G-udHVp-TB6ut82TKj9NqoSHcJIjGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gS1b_LdMVmYlU1qqg2sWbYmbqLQhWvsMWx4UKqhPhEgMJen4TVA0G-sX4oW19xtt7WuKtst_6WxPpdER-4NFMTcq82d2h4zeBKKxySkN_kR2KJt9LWKWNCwPIAD8X5iXi6udO3B3XC8bBN9jj92Qi3fT1wguJeRJeSDl2xfelKCmbcGDnhMp9KDogdOQz4tUgeET9uzdzDIz6vOA0OccLF6EPhhI6_cB1XO-NCRJywb6wQubxZxjN_rO74Z2HK6Bearm9EmApIHiRK-DrfCTFiuE-SOliqKnWVgdY1_llPpdnz3pFqyUFTBgCudXM_OsgSMatSxeIoeGLQGvfzTAeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PUNqertVuGWxV7mKYpYsa143r7RR2kdcANauOCTIlSA1_bkwbbkDW-PfDwDPOHkp3hmNNRvl6WK2dPBe1HHGtnoKtvJv_fLyPhYjp1Rfu0Liqbw5XpTU4TjcGSx0oWVXONMtTa0Vw4RTtrLit3CbOyS6QtItrkzCwTWzyCYohPYTpFXxLii53weFx9G_9x8at2UYeBuHKxp_l_yZTF62og3ZP7xD2E8hV9gkDcSdn7Nn26xsUZyL6Opf4xPxKUCCbnOWQujU2MgwPxZMbKi4YM7mB_rGrZzGtL2ezYsConMu4ZWNkVk4ESjAI6ZW9TVZLaENKdQa47a2rYN7JfxVkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QEVA9uMMD3b5xYmbQMez342Trf3DyT4nrE_0m3aUD6g3Ofs6gYnh4JYCXDhbi50W1CBN29RXm8PrtH9IW8EZ8W0BwPwNANkawBb8W4NvPOwAD4SoRh2Y6RIdbeE1LIeNJc94cxxO52wEczM750eO1I3l7bMCr4L6HqON0mtQJhvwwYUVip0UFsuANhackD5GgoxIzw8b5y_o1IqYlBh1_RJLB0J8GvrFzmQe6B70an1vYg9aP7IlLLA23cDxduva2xu8acn2s5IjtFMWpRPfYoT6UdJZM_9C9f-4Y-f6n1WcPf6ZDhsda-9r7EsX4OgFx1D4XkL2_WPG7r40AyBOpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NCwhk-ovTbUI1ESfgr_vKcpJ7WOys8W4dQK7wRM6MbuyHCOO6F7hDUuRBxi3ugyU8T5pItIdIjkRqTNhng_lXnfUe4lar3OYygUrIkOjSIx3tYeNZeJRyoVY8UCoPFIl4yoqv63MvN0e3NQRKcx54BWSY3wW1GYSSd7m0VJ_SbfI3_keYsSB_Y9YvTt4LyrUXKhvhgi2ga4lxtvpPWLcxlF2Lnh38SpGoPN3Viu048zWtterb93XG8CHprNiMtj1mT1FLyPYuvLIBNxxxYljhLoCkMxsI6CO0dt-7_3QMnkdUPOWEcJjR_TKA9d7aTHQLvKeAMlaRONKDKVCzRZzMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 91K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uiXOki2VPJNvyLZjwKmwbMMF4YkZ1DyLE2VqLSx281eAIU3glveVbhwnZOggJfVa7_jOmd4fUQU9aGA4Lq5zWBAl6BdNrMcp2Hnhookq4rIGqImbYKNUuGHy8Rzb1dLcYRGTQmSRUqYX25bzB3dxg1KcWanTH-DXYdhQAxJ3zEofD9j_hcdVTPk89crmiNE6ShXeNTSmT_vF5k0GD8H6yRQVII2gIXU-1WCJtavewCCaUOkdyGWQFOYr64QMVShfMg92OTdYvv45sXQq_US89ueY1YjLrkW0nRh94d_23M2_LrxkGg3NXi-s_LiGXa1zAiUWk0ILMDPEJac-2gb4pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NXfeJIV13XUhzisRI9xRIwGnVF0RNLi4RuWxeV0YPL3itKwHiGh54Yr_76RW1ZogbHXL-HnXioxI0pH5bSlDEzXAmZDXPcvVuadzQPwYoaBgmOtmDrbnsH0fxr0mLJ2q33NN7VyDU9JqwgzvMTdIoUOVag2iIUAgFrsFDv6bHBgvyW1V2J698-DlILTusQrF0hqWGS_VxGxPQlBdfsUNBZEa1xMQ70JJURjAcrpTfeoRAu_ktYWBU00G88DX0O7POjH63NP7TRXcStGIEEv9GBm4iWKWdnlPNkZP-pTztHGPH8ZxFP-4nCIpGGag6te8fHWuiXiIiEK67UlMRou_EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UddtOU1xEpKKhkpBImi080OxSB3L_JPrNOmYPopAlVbYg_sDDbLXyfzEg1tU3bEqajApSc_JU4l--v0xKZTwU0r_8CDSoNKcwSh3ZOdPUZWw_2bPG9lK6sR43oZOqIUKP7RyzspFs9i2JIZFe-y2qmnCrBOXkZNOmIkweGr2_hHM-okeqs95hXJDC7vMUoKdcSz3WLZrZ6a4UXUy-AG0FNEmMS9rBx1jO56n0vlGL72953jNpFYBpzRtHoXNqSNhOei1eZW1jAhd8437GUb-4iVh0QYUy5V9nJkiHbuDDAvR7aut8HZlGLaO_Qy3mX4K4LGG_F9aEAE5eKsgkWHIlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4UZZ5qMLHkIsnLfNDlpbC01H2M23OYN8YeSkNrWbwp_5PNhvpghrMiBn01a5wRPuFfHq0aXWLh51Ry0i1azL-nlPuY-Qdo-zmiE47uwI9femdZjNC_FmT90SKdftINRbKOe3R9bCEKvT7PZFN0NJeZd6a7HgsIAcn2VQXq3y9XLh2p96Shhg_W6O2tRn08tMZwXx56FVeMMdOFx8FmJcZGlFe2PB4A--3VsMEGt5bTs8u7O0ZXGJbE5d_d9odjlB5Nb3JSj8Ir86yCh_uWNPJoG0q6Jev_tzlKme4E6i4Nm9bOPgobUNVi-fFVV0l4vxtCRuvPaWDuEyWG5R1XXcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QPltjqCJnogyAlZlL96G2VwrIf8cYRRseV0zJ18MDs1xkTUB7X8S0wohb8pSU3d-dCNpdmhYv50QEBW4IRjKVRSAo4yPapE0g26ORdl70KivzvTEDiCJ4vILSa1nZDuHflUYlil4BC1hDAo5dcb44UXAI59d1AKdDLPZUFiHbyXzf7ujUeqgIWHg-as8vSGptfoLM91fMrXcKMiQoFDaF3UoUzqbD7UXoSHcgCKo9N6e_IKPKVhfAuRgXyeI8cuCwTjJm2b3OKBHG65qh9LvOrtk0OEjp5mC2WX_oiInRurOsgrwTHyg8FomHpbLDr3SqL50HmGGfI8ogbZ9e7JQfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GpMQbwYXY1bpRthZcYqDxNDfPcTQYSPDYzG2UxYXitGBWe2GOHIIDBWG7W4N6bAgrycIz2lpH6m0-SW6c5mQnIYRcP9asJKMGDastLDOPYEcsaA5se4pU6EmytB1w-kKp6Mdg2u4C9-JLoUvi1VW7J3JX_lwao9nvN24bQL242eWGoFuh-kK_YeguNJun-R7ykq6BMVRDPZh36LANNsbVx4f5R766oWpAg9vh6FQBStQ3fwoqJrTRyBoQiwyCrPwCat0jYBt21G-0sBetBtBykGTWNm2saTLQ1xZ9cgJULtN0KJYaA2Tp2AyNeDpLHhL3M3wLWACeavDm_YyA3NCcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rbP673SIXNA8l2GfuSsaF8LpxkInTF0UPCdbf5TcCrrLi-7IxAHZbFNGLVbe6JGj03Iv__zeqhlMK2AHLvmwLU-RpUauMtYGV81ENwyuFlSNnKjizQQawS5MMnCu3lMUURiQyPndrDjBJ-MKan2DE2MHhnywzyY9YKTfD9dor3vOgCg9QncwXTzDFu7A2UQZvv92FSdHC7gFt3Jf_gsoSNCqUtCd9RuFiX56CTxsOAfu9Y-e41fptZ4VPiiMzeq9X3GjBuwPxVdqMMSwUMpnny-wvahk50CSpLomkpW9Ls7H9JfmYffPghVzi4VPerKItrUYmAK7Llcw5cN-iI0r1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gl649CoG1EL0vL51H-VCjG-EHeEhvDYiZM2iXqrEmplMxtxjQbAYLXd9feFRoqd9OEcDWc2EXHQqmfsR6b8YPAUvwpF7xX_1KqVDaM_91q8o3fjA96JTewIhkgnPfj9erO2TKopmRO-H3UCCKQnHtE1exl_xMRuaiRRKFXfAfhU9kiAId7sbU0PlXZt59GmReTPFGlDUuKElrdQUwIpp73W4CvY-JznOS5pK6AH8m3cbiRUKjFp6C6ulg4zhyt9MVoMtcCf7MgPhXxU5fXBbbPH0toyZP_yp3Y4xI63ESbtXTzPrAYMF0J6_DtagtN6IkfxnOZ7lBEe0pFFgPyWIQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d309k_OiCQj-8KtUhcWkD4B6Qelrct-tvpZjMOCnVUQS8k2jvpgQHPQXqus7OoNWYqSc1lp_23BgLfWD3E62MxLu6NLI2mmPeDsTfk_WUP1EAjaM1oFDXEKFqe39lppd0cTFHzbFcMheBZMZgBoltsVrxZGrrZ9LgyjhiGuhm4MMubNaouTJaQ-_hA-QQXpQlhOOJQC5Ncn7mzcrDsPIwCyCtrrk0nfyEDVAdSm5D3t5PldvxvMu5e9FMLikpuBWp2jM9gu74IpWtoPx951czIAs-RmTO37qQoU0uLhlEe11gu2UfGVX4GUUvIwggL8StfjgRhCMh-RpwSOpks-F-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qmxXPpKdpGpJN4f3y9pnme3_sLlLSnp2bDWFMwCgHOXw7pDV8ITwJFCcXeUkmPCdAu8bolw-Ntc0OvXW1uxfoRAGmW83c9Kw_gb2h2Lzt7NA7RbVgpsP0iDhAwdj_19dnvuedIm0ZrBhh60pmRQqORNPtuSNnUvSglwLo4EOQ1kYkkD8h2wwCrTnWX7BLRQWLFaf7K11i-4N-fy6rFOYd5DnWAMxQLOyr_ojHuYNig17GgSs6zaxlilm2jHnH6x91uJOvtvTVBWeBzSn_GlMaOZhy4qEPHKusWXEC6hSubrJ-iIquiNR8yeaStIkNuHSPf5dyH-SnkNT2KgqBNBIkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J9H3j_BOpAMgFp-68EmNDmfDX8f1dMs2Qu9XW0AXZV2hPI07VqjhrT98OFlqlfVSmpm2ABo7J44L06lke44reOihU70tS1bSpIwnazD1_--VWvK_hGJwlO9TyK1rhNMw2v--ZbEZWl5MPRyFzLUel1JxdeSjkwrbUaanPAU4FzXVlcHoh8zJ5JsF5_OJWGTMEdKOOY6JBUS2HVjNq_bo6UtLdmfNpXzH5gll3VoEvT3uZLVJYTk_s3R5fqAv80B677z0NVsMeOsupWsnHSzW5_szvc8T7Qh71hUvpplBfxLZRywt-8JlO2bUSowQmI9A_BU5e1S62B60ivcIDvXcsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y2uKl2EsQf4xsDPXXjEruygj6r_uu7ynSnL2rV6ykWboKD2XNCv6SEe2RZ9Q0UenmCo4y8kOsq2Q_0IrRTAaS_h4F6nOMDYJcFV1DVxoQyZR8Frd0IYK4Q3x45u4pFdZWP--VOjMlpGtz5xWwbch4lS2M3Mnpli2TFWNWxVccypKV9KsBgbGZSuyIwIaVypZQ1OrIgu16jRE4l5-b5S73e6clfLuf7Tu9nWB30f3d-E4xkHRh8BzIR0gh7MO8JJ-GUsv_IEgMsE-ZaVobGvJfBdBpigtG5yVi1HOkQt0NCdPlKQ_m2hOhPO4DwK3kT6wvedRhjGkfnlSbw4I-177Ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DUpryk188lviBlUF87BiJ6OZAOVUKo0OsSnaGUiNtJkASaGaqJCluEVxJNRNTd4M0Myx5_d-Hs0omd7QvePZ9xKX-EFcOaDeBwjdixqExVODeAtS6rD6doygLISE8Vrx7odoogRvghO-3a3BPvLqTRvKZE6vz4ESEhxo_E746aLO__tGDnxwZguW2t2gXccRBcAqv2Lexds2jD7yIlCY86LvoI0TDU3CMmuHeApqvqBXCEvWdRg35cNPDnBCQg_AjTKEKLXHBAgOjxV2inMq9hmCUV8194p8OBwGiiPmdv6r0bZRMHxhaUCg6P5Vx0bRrNQUIvS1csK6TFjQlxP1mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HVqyrhnGosXu9nUcNaRga4OwAkmWPZSDUTP9I77ZEwMRDxvQnebkT8UcFV9RE-sX8LIXICYXyz05BzZlSt1VKqgRzzpJvxHUp5eXmLEOeBztASp4NVH0yi1mH96XT5VzuQ79W8q9OF3hWBSMIupckIWDixkkd6vb2MxFDsVhw0jI-GjZXWi-geiJlw1nakAWO8XJ_RVXY2nfTg_Ll_EIiD2QWcWMsmfqIpMskqXCbvcdvW17IIru7ieThI4NLcy9cyBlK2BbXPYyWcDpbG8aqKbMJ7PIHVJQukmNhNi3YgejTGM6ziXb7bASsptwZF0QnsYrmf20ZdyNvy0x7oNhxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pkv9r3Qg30rkBE7FPsYtmurEvzSkbeTunMwWN15rB2lNcFaThoQhoveJNuPAsFO3UG5thPdEu52rNLR1qO4Ybf_EPFOgz70K_vqSm084ahIXTwRZN1daPtnqLOMdVRZBROX-QFrp3BH8iVHcxcStckJU3GHhq44JYWAUGfMymjCg7-yLsH3KxuxsMGa8oVI9C1qToLWBgibgAkD-lzukyJjCKP-IwoKIgWuRUfTIA4jZhepdiAaCvf74aGk0SFGaXOQQEx8KfoR_xbYg8SA6CP0etRWUX4ISWPbmIhITazIJitdUkNx3w1tHHLYtB2g7x8fR62-MRmRZDmwjBprdmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JPAD9aL6x0pcY7c-AuM6RY21jNZq8PdVpr85dYkXFlFMMGW-Y7omjIl-UC6vLy2bJqQCjW5nlyErObYVYgwxmfpn5BH3N9R7FG_tZvD7K8Ei1OvTRSfWW70QiKKjNEuGgqF_Gz41m4cCwuv3BK0qzwjwlJbISc2dEckyph_znPHAYmDEGWCUuT1S9EP40BsCPMQtxkgx8MHttB9kf9vQ-ou040pdkXg5ZYSeIM7OmwNym7uCDaKIt0I7aWEAdyTUEX3RU4k5GsbcTLOgt0oUOxRvkO2niQk4uemrtML2wRc6ix9wDRa7CrByfWZcB71oJf7NvNbdsh0njf2ZndKifA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cFZPeboGzl5UOKnCv2OTP1hyxIk2ZydunnKmsmvpwutQ2kBAMeBKU-D4sblGBndWpqD1jF4Df45aNRw1FflldSaq5k3vbZFQrKfPg_8z-ZzsyCZskVJwMP0eQOorlwnKQW2NmScLOFoZU4p-uULPR0DENNwARq4WstexDkkRx8fCYVuPGoSR-tZNUxQ1hpaZkfEP_7w1rgtbRUCiom4g8piU_xiwASTUzLRkPsKh66gfvDiVLRpNb6zgAp9JEudHmywzy-TRUwBWZYe01mFw5z0tmy28piGxUsP4nAE1FCy5HgLjn1Kz3GNmqCCcKG7UeUPjQbKOHNORxkI19Gg2lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AY3Rsxmb7LSRm-JvvpXjnOYsVs9PhkkLN2Jpmdwt9uDnEVUUAUcjaTzLJ710k-kvHHtsncqnv0_qqN65q7sZuc0_3R3EZph4p3TUpYL4CMkabd6H0ZjLy6Vve_OPxoRaGXcK2ajvF3J9p9KQ0glImTO3hP4_p6uW112Q_rvzl1tWj93WWp4jE83BT-xh0eR1wwsuPRfTu2truiVLyfPRMQ8jqrsvYTh6VwHGY4dHI_Fim5GZ51Do9sozYI53Mg-KCNGa3bIYcQozdUELMCJdT9VQRon1KJZSp-aE43pQqeYPpm4mefRSl6PhBLu3JxyS54mBD9qFcZGKNiYs7ZdSSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P9dtfZ1s_m2isIVGJ_Pf8MqXjfO63E7xwtIzPiIaWVr94QD6qPZXuF-jOW-nn-jrZx05u2dl-Pi2A7Bee4WLLQF67yU5QUnLPhsHAOONvFAsvZ0w69ieIU6a30F7UJyTJt1RlJvWxkqD_LYN_j4GfQIX0qRUKg7Bmj6gXvyqt01zU0HJ8xAzEWKdOwQlLLkpc29vBrs2pERdxtMBRpsCiTwmoZmL-jh2KoBHVZP31gfS5U_ELEaIi2S3YWp39j3PsgHUVDdzUI6o9bQmpJAtAgV1y553Y9usn0UPzGufFZeKU9X-4_eFz1xZWKL0G1Vyqk7UodoccVNdm5lGwEX-Nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fXp8tl_G7ypYJMw8KuyOppgHCPB6-dpHhj605IxK3QzQmZ6kEHperwajQGC7LYe9dDPbsy2u9Qc4ECDBZHbBD9a5GsdLmQIAK2fQzPpXKa97WADMq1VHFDWODJzoLjcmaD1a8ZEieyu_LJJJVYU3JdePcJAs8yKWLvqrm3eySX3PvarZln-vkEXh1EnxrOrVOSxMu1s2DkiXCwOtO1PvuIu6Jnf8SeQJPZHBg0BlNrJBMBxKLHwYaRyiH4k32mMmJSFVE-WldTLRKKhpketXSY-qTz20_kY8h6xj9K7dRE7ixFVJ9bVxPLHP6ara_vbXgMPlHygHhS-vFi-74G7gQQ.jpg" alt="photo" loading="lazy"/></div>
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
