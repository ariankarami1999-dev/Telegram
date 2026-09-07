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
<img src="https://cdn1.telesco.pe/file/LcX8vxMqe0lI1XuHYAL8Yeejm4uNZ7HzfqMwyRYhyGzcjPmZo1A5CBSySV1m9IgKl6SbzruXO6lEBvRL3PPXoF6fnUGraQiBoIrsfOSxa53g04xNefZFosIzW8N49qJTruIt9kwW0m3gwEX2D66om-lRTMhWuc-yohxGg8pGsOgSB6GuoMJ5k4UrGJtjJT74Cy3FsIaZxUu7KwootcRau6CchLTGALkmcfpOJik_1vEJ5FF1iHryybFf1iEdK8jbT-b8jniRnDPs5QinRUVTzKFHARq5BbTafNJxpbdslQnBJ6KQPzv0d59by-TWMaPVqYj6uRUP7A-fpiQJPacpbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.3K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 08:58:46</div>
<hr>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QGNSDLzjX1bKTkzvGnivegJ2PKp-HTr33bsAJax3LtVm_UwPHxeXySi7RIHl9rCztZrxXHrRK9V2s_KuL2gCQ3bdMDckarVuKOVcPEANe3z99n5wULcxNR8gjgaaL0TFBk8nAeCzfXfwdFQN6XltLn5FNGMoc31YjS7E7-Y09mMV3vQh72nabx0IbgW0L4khuzcQRxJOR7rXNT0krdPO7L0MnpcrqfkSIVjRf6B5VhJiKZqBl0UCP3aJRNg64l65QR8KrZnqJOhKjjVFZACtDLkaqgKIlmh5ZOx5d0GpXb2yR3GwYjE-B2mdrcEPnadNnx37vkZuiCtyBhWDd_NIfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 828 · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MnWeNcG8UXj-GlFahMKYsbQ7puOjkY24em1myKtxjPriocccsjv7n6FYBzzKq7jIMjAoJwohRW3zPf0bPiKvqsZZYr87xgR2V1oD4E6zTwAITpaEO4nfMIlhzSt6r-Q81TqM9dKCwqyNx_i3a2K_4RAHetQabdNXlAG-7JHFcKVdt5UC3srlIxuwhvan7qnVEPOkQhQxRJzhtfq-1wUpN0sPvoyea6Slmi3ES6PwLhcw1CIKSgXmhbVTbncj7lKcmyZrXK_MApbkfAAbCCao2EvzGLiY8dhrgnAWG9MxOakm_ncxXnBU0ohIPbMu6fQ_cTLyP9fgqSyGuZlcvkagUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wCG3OKZkHtH67AAfWzY_52oI7SKGbdlLvkQOxDgGUhjb18jodi_u_0iVbR5kbvPjfb2WxK8aFNNWqOhepecB-D8ccltobvEWDfZI_mMks8qfr22y6WsdaP678BMcGTrEypdKN_6Pe6V9J7Lq1J-KnLjgTG3mL3jX2GRHMm0pO-TeTPodoSxe14F1SS82QLmbQWM0piPAeLbpRZm-ChvOnFd8dtNTW9Sh1zLyM6sBC1loPVbjB6y5YQOcRSmVg97jFQJtZYt4gLzoKO1z3o5YwakDxYEss4AnyHjLsAYOB0CDBbDUsbH7_gdu05h2AYM7fXfJdJR_XyO1Io5txPNmSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gs4CdB10b7qlx3pdCT5IZgmxPK-tfCgw_ILnJ_JElgzIdYA8KpxRuZIj8we7uow6C0lFcSD2c8L_z01ziYJ6jIG6R4NZcW43ba8Lu57y8fyA5W3LhhYeR8q79cTuVrpRQfCVZzzc-9VOby-oDZ1ml4FWTo5wi111mViVTL-qgZFL6PrlAjyfD5D-MnIU6qVhbewTIvNKkEi0r0OzcSGvZoPV4lMqnAM9SzaMEBPXC9D3k4nEoD7X-N5TkVfQaUanIQpvLUJ-71vcqAuqSnsmdhoMKO-Lz2uf1r94zz-Rpxie4c34wGPun53v2qTV8eEybc14jfOmrDPTvTiqe4Vu4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kVQN77xovcqCshq-GEhzlSjTc5d1yxl9RDNQHjc6dUN8QeZDZ7njxAtEyTMlSRH-IL3VZH-99MDnC7unijwOuS2wdJ2I9vql6pjBYye5yhKOieD0e5bI67fQVp_cKZXU7PspvzY_HXYUkoezq5jLNA_KZ4mAt3gdFRo1rXt3NLTHlMWtQ8G1u2aT7UKlVUKHQs7cPiMsSZs0llMd4ApPVjtrcI9czXjxkSHgIGzJK-g7EvLCJ7G-vWqQ1y-0wWSQXK2bXwPOoL-d3npK2q3QP5vHzE9j6LfKpS30hulxC5gE1dfFmzXZUgpqZZ-Ta5sCNbRQ95QG5InPENdh_3TGAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QQqkezqIoWSTqMG_072r1Ohw6Tk8jaKu2Em4AMwCTvsBmTbqO7KVsTp4YB97yWfV9m64e3uit_zOg2QBgMgNBicG51MfVOauFCm6MSv5p7egmW54ziBx39jkpRtzCv4koUlLHf0vlAyHkzODj9bUWu41yN_X9FwQtWbZxBB2a_fzj6fRoOjVwF1vSArTcUNdXzZuuG7IWz9d8mSJKnsbR3hyTJpj8N_qnktRp9oFCsyrpaG_zhCv-e-vYUJSfeCOStn53J66p6hdgo8VWKPjDfUyiVg6LnoGU_Czu1SbiqDjMbzpNh3z6FG1wnKzta0A_K3Cpu5Grch-Yj97M4kBZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPG_dPjUDf2s1W-rGnlRk7gQrMMrfgaWpsGmLsxA64Dw62McJ7HB_CosTYgY6ETtAIPEippBgn9dB3BPquz-ahvwcu4ktbVGtKIHshPY8fx7aUlVA2e7spaaVfMWjj9Wd8AhChN5qN-1by9-xLReMKOnY8Um1kMVPAKPUXNzxEdZiiLyTpCKPoM3ZmPWdXB72qIJWhTfK3QihOyXdkPtxrsK_l9mNAFWYJIQbxFiSEHCpPagvKGDHd0ihRfWvazQkrtHwMyOp_NgZHuMDAxINooCoFLcl0REkMDWM1x5vga4LNoMtkAGa8ygcN8IRJjkk5ClebyyVbe1qizXKXMTWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uvfjaq8-sIMJM49KR1S4MLGIJfntiz5UzHF2YccUTTgv37H9CM6BIonIH1_T9_lB2bhvLPDAmnKbP9Y8nDO-jS-XhpzveN_QRwWVj3Vn4fxwSw101RhsYrQydWEf54bTJhTtGyM4jIoOFU_NZ9CSsQCIl5hnr0EAjiVh3aPzzuXpvwk_p_E2YX2Ph6TWE8J279r1e5xUp6VU5EC1pCvJ2-8h_Avl0VtnibRVawReOZtIof3a_DlA5kz-Vcp4bb0ensFMF_DLBCRk_7UO3eMdc2HbsC-L1oyK_9tZDgHI_h692RsWyBWEIZ8F5oFB8QSCN5bNP5dTJRhOxW-jApJ7eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aP3xz9qeipJVb2TjtMZaBaDR9ctCAg-xv_mY5fhEwISzQVLlS7lrepIgt-loeoO8HxqxzcyRSnrzIj5XycUFY4j3NHiefZkfb7ejViAGk-TjH0ACWfg_mOgVt6J6htFPSJOvRCReNjImHXkgVewHTm-A4O-vxct40Y36wUIOcKdq1QAMYYMptkus7d4D69cafH9bCsesdnkREHcpregL8adkNe7fzXGWR0KBzNTo05vjMVaxao6phfK9vP9UflmYQU578zN4CIJ7HYP6mOrwREHrTr0nXAgQAlF0ZAFlwmRM_dlJ7B7q7OmC3IbV1cIt11WwbRzdnfXndEWQmBimjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frJit_GqAfjbdGgzDtJ56E7EK0Bm0nCwGI5MO5ZCK53uyiRGjZB9B0QfL3VhzTQYYgxCfxq5AtTY5p-lCqT1fiOwHGa905zvSBkFWFTKmawun4rHLNpC2tWqqFhgtEqCe6xwb93Ir3Vgtec-53srk_SzejuNawOz5RQBfSRqeOHo_0eqPIhJ0jMyfXx-mL-pZbIHsqV68JfavpTWQ-GB2ycwMIgQpgis7IFA88Ztm1vCc1PbdGH9Pw3r1OvYw1cHCHz-9kWYGdxclVXRRF9JlmfXrxBjCEZUGAJ7HI_eglfzjZ2OznVN6n2MmcCt89zulw1JNcVHkKE7jdI_b3hSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y_pF1px2XEy6Fz7OTmzN-i8NS-McaFH43PAIxYSPNfGLY6FC2Niy2sKClRrtaG6VVmHAhAqiAh0i7B-hTQlm-fLI3juvqDY_PCNL1OgXhTvzUwtMwNQzG2Wg5mkVYJ6O2Zi6pREvU20N73G1y4cGUSwnKU2VVli8zY7aeu40NRFCp36LTQu3c72iiSNYn0yp8AHUklNaQW1DiAFCwIO5jx7QX4OiAklZ3oOiLXzC9KsQXzjmtyorUnE3Hf-080vjlwkEP06UuJ6gKcTAXBZrpJYjBwjQWntoNDB3su9KAPaq8w_oGMvYRZQ2WVS3EPe41tJ2F4JbN-TLMBzPH6Aqqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_prETj8_rdMFSXBMwrfWRjBzP7U9nGDwdP2MTN1XKqRhAVCaM5OfiP3HxJwugrasXJPptnKql2hFINPihwvKpx4peIiPzM9w_Kd7-9pklrR6BrQw3vd9A2PSr-1mKME1rS8WFPLXu69xXJ275v6TG2uQKXuwAbx9Put4gMrwaNr3Y_pKBIKp1H2yWRqBDAkLHzIYF2SOklIW3MGVMgEuPsLdLvOfY6EdSUTgH5zpFoYo3IP9WEN0CCgsk9YFaBa_7avHSXgpvxEUImtfq7H6PEoJ7JyJxmFTLahRf5UOOYllBwXljTn3rbvXnXz_T_k58JrD_tilp6P6UU5NNvCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i4jT5TxgorsBy8H50Lb6NExGrwG3oDfFo1J9KhxoTu7mu3UsDMrQsyRnroxWql_ckW1BzakXzXTWfJ6y-W_kL0H2-hIda2RON2OM_tHAPMOV4JddR1-zcv6UW8pyEK2oxJJM9tTvDyY4GreNJaVfLRIIdQWg-0fRCcmdoEDGqtg0zZlHbxPPO8ulue3ZQXNYS8vJ0i9M615QvcQ-gXb6yBizrbArx-RkoHFavSA3yibGeFQNEW9PsCPGHxsFaDbyIRRGW0smQYeFuTd7RAoUFPEPVDV8-QlKCgmsEuwNwCCTFBBgLbdNfO59EBYpXc-zyhv2dO0LlHykuz0nviwtwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X3dFpRVlmsKQ8xcIWoncLeVKgc6NXpUDl9pKw-geFwdpuDmfqQrAggr4Ij55wGJuquYkIM05LQJ4tD5oApibnQIDcq4Ho7aBo8-3vqZqTwF81YRkxsqVs5D4WEzwkvtxLCrziO9i_E-yEZf9N51KvFZK7Xyc__o0Ly2sIHSVqnzEJxP5-pswOIsbPVeSd23HyTakcf9iWDdSKLFaV8AiJHuh2r8hC35tTwP9Pst4qssFuA6U1kDUpe_dJYxjYWaMazHOAyjzvqH0zpmHDFcAFd385zDc_7i8ievhzx5vhbf99diQ3Z7pST-Vf7DmsVp800LRGiKzng2LU33Jb5lPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EVPbzKkXFht2foFDqsqR6ALsdKBbz2UoOQg4yGaerVjk6HjBhtjlRc08QgZc52B5-xxgCTa0H0atn5CWpQi1MYMY1esmPJyGlKxHGFmdSQnjQeVyaaShAXbOI1inZjp8LF1lS2bt9bsQsR_ylqZhjr4ybYeEOv0FImlnONYkDijkjP3qyjcyb8cjWWsk2vqsmB_kBMVarhmgFlQTC3oUh9mRFyXwLQzKF_kDkmSJnwpTx74V9tlu-5ANTZa6E3kQlxyXpHa9NGoR3a2uNhecevMq3tbG-4-4aGrb-mONcbqtQb8LED42qe-uRv9nKoXatSJ0QubwgEqHjdtdzFi0IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SKCzhR4BfLblJ_uud8VKocwOu3Ipgo3QudD_jymN7jPyCr4xKVbVV9ONoBpafgO8fU59eSX0nklStm_Ieod9NGuY0JwMf4xPDbA08s85whHdlK5LMkGo7p1IQk04_lCsyeAhApMHqF8p_UK9NdMjTrLe6qYEFN46FlKXP8hwqGSVajzLqHNe3EkmN2H5bn6fWg4lPTwNpBAHkG-FdbK0lnDWOQI2AVfdCsW_tCuKFhUlp8d2kq-_tATFg_e2RxgVaVsIlOWVXU1wOyR8yow9a7Ab2T5i8OI138xkEPQ2yQGvZacYJDcVQm2hFF9MO4vfgt7YdoSoGTFSlue_dO_5Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mDOCZkBP7yGVvNFoEW_for63P3Ex945TxNBQtY-uzb1rNxRHWrOmvKGZdtNF7BCiwRiv1ejQmFw9lbF6hHhu4hjaIf609CRJN1_IvpT9Oa-iwp5rsv5ytWa_fgELaCLrZgjQHUpZQgFmJ7FMEJfH_JctKkR-6nO6gLGnhrP94_f8YcbRfrA66X7cmn2rlmjzUXPq72sFJaseIcQNsBH4Ae_yvSxCT2GRmgnK93p8ya7H-LA4pEsAe5H-mMoshLq_v0__48-QGQmSldGmX2HZUe3k3HE5nzhyDwiC7KDzzq3UWHgROHwseshVHiO0g2mOOwzpgBT2dPfro7IuzO6abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nEIn3zEalZbNhagdCbtR8l-ZYmgGSsoW5IiSc5wWFHmnDyEJHmuTxhfwn5kC3vIWIv7MIp-qR465NEuvRNXK0c11fthaZ0VIM9l2bH5CmaMedcjYvG4HUM95-Z4prXCjvKadpcF0XD7F4Z4DJP3o0TaeFOrR1jfUtJIojMQuXzLr5YhnmcEElWiZakQ6sG0AQCMQ4rgoT_5TzHl1q-lxSBry123EzGwVCjab5ecw8nh2qCDGDdJf24GY0Fff74mM8hJ1gKCqlCl5wPAsFDOLb63BmoF9FoUDGwMT11qn90ga9nYJIKXc8jZoZSKaK6awnMbgNlTCeqSkweAeT77dwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vjS6D2tAcavJJD3PMUaf3zYAs_BHKUcE3f9i5ratRWjeGI_xIE8sUGorvqJEml5MCC0nqKJA6U-p6nEGYmqOb1hHm5i_4SxQ_cgdBhPYA8xPjJ1YtnT6wgA_Rfqwc1oMnujrBMRjM-_C8s_gaP_GaEBB1CW_jzjFmErPw9eKZV10aKTH0XQlKPhOy9ZUdf-h7VpOOBOsTW3pdwzeSgLVTitpenM5L3FbyONAVshdNdZH1HOqbcxOHYMMiTaZuUVlqnMKtHpNNEiXN7-ybmdyKd4x8Cht71kM8l5X3kXhiTz_vOeOu1k-FxsOt507a2dEvlFKAwvNSWclTYLOTHz54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RawMpfbPqgF3Q5VVmeb6UMoVfE2vip7regea0-WTNAH55n1yLeVAMuB5ClDj39HcJ-rXmD4BXdWUB9QxCUd-H5LfuHEr1yJqya2jAWBo1F4QTEMlVtF_giV8o7_rdqdzsYBcWppPWWqHo9L0NVlAf0_oN3Kg_hT0sC---nBTJCwC80rjL3eRPQH0W_JR_SSip2yUZP1zdPEDbkbZnuqpLTe4EPBBuAmP4Sn00d4HNTKWah2-XSBryugZU4k6OkutSKZkEEZjA3A2i7J9-RLO-TdacdhMLDKLcx_Z6Rk0YvjmZiK5O1VJ3kDfDzn0sisss9vO6oiN_R6DP2UvDAix9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SuQ3k17CyX9PO08KpAx8crjG4Fk5pBcD8jvlABtO_iC-OuYrXPkFkywaeUzcnljXC7yiI2vZj4DpRBPcRq6J3R4Cqw_2WNe1fzzlQXx4_RyvfD0IoMJbB1uMhvFZKvvq91yaGNOoDHtCucpIbjjWE4NSi5wVlo1YuhGT8OEOVZNA10uR5_gpN4MyvuZyW3cP_G_Qle5vipkKfzFpvlAXimkVe9Cxy0sJdvXUFP7_kr-8raI_hCi2O9Z2uwxXbWNeCriSElosi9X_uO4EGP3FRpxpftDZUZC4ydBkZqUKk-gvVg7ozFaSUz1im2MVzNoLlOelRmRBcrG6ltU1rOkkIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=cuBWP4dfjqZA9derC6S4gyAjtHhieIp8P5mYmBU3CH6kqMFp0LizfkQPH6HTbnSNAXHc8AbsjVHrjGBW5xHK437Zcjq_2G8Hk4oBuvp54ksVf3gfKYgl5AqVaD67ReGHrOCUgLjsDvqvmFd43EHHeXdbuWvY_9-PmGNcccSnczeacpNTfC2IJH4y3piQe5Sp6FqV7k4f63JazAH1J_pmbpdMGJWfJ_d_S5xmjgl-Zkv_Ayzys6W2BjNOG6RCnIyTbR5iTyF92z8EVns5-ULHUpmuaOEX5rNGXTe9cqiQjJUxs-7f-isRpfn88ObDYwb0kBLRQ0F73LYEu3QlpAHXbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=cuBWP4dfjqZA9derC6S4gyAjtHhieIp8P5mYmBU3CH6kqMFp0LizfkQPH6HTbnSNAXHc8AbsjVHrjGBW5xHK437Zcjq_2G8Hk4oBuvp54ksVf3gfKYgl5AqVaD67ReGHrOCUgLjsDvqvmFd43EHHeXdbuWvY_9-PmGNcccSnczeacpNTfC2IJH4y3piQe5Sp6FqV7k4f63JazAH1J_pmbpdMGJWfJ_d_S5xmjgl-Zkv_Ayzys6W2BjNOG6RCnIyTbR5iTyF92z8EVns5-ULHUpmuaOEX5rNGXTe9cqiQjJUxs-7f-isRpfn88ObDYwb0kBLRQ0F73LYEu3QlpAHXbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IVrnCtJrB3BUgt04Ded_rlJgm_fWMLR0ntHMHEK2jHhcLs2imJoKE8-M_iezvNkgGoeHwi5hGsjVYkf1wD0LpfWcfIWq-rZE5XmNIBpYTexwTx6PczOt-m_t2QtnvX4e-bHALfV7omtQAfLKKOGYd329RiTKSWXLMvRIqoiH9buCJU87K0ZlneRFIV5gMJxzeygFVGCryHQzrFHWUByTbvDk_4yzjQovxmP1AeMxRkFh853HQ9AclHuWZvT6iCveuZQbS0fVTlJCSXEdPqEtvvcOnjJFIvzPVY7FLeIb_4lboQoUqY1lUE-cFx8CQ0OVvka7Pn_MInDUI2PS8JJRuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfiE7rUU_ETRHQEfwHJt1g9_xn-kU75rmYRSRXlK86Mjp4zzWMbYixGxq4BX7uSORePWjt_onPbYtv2sx2zh5to7i9mCZ_yAE86weXPTJPwz23e8wMmLBjtEmY2Kb4898TWK_jiR_fQMOdvIZ70efe35j_AGw__vlN59Hyp6u8E3KrxICe990M9W5f3xNu0a6Qm53j83O-JNA6epMM1hkd8Kz9E14YgdIaiXhAl8QRkkZ3p26KC4jE9seY7r6LV33qG2cLYwA6kGFlXr7yUcjJK3MREko7CYFKkLXOr5BPFhTAUIozTX4rOgQS7LmpPh7CdC-J9fK-kWHuuh4aQxNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hahlmEsqbq_ne0EyHKwgBFm9PCg3KO1AS0_0hawo9-eVNcxo7XHhMXQssdnwPfZvqXGNVDsqpo2PBRr6636Jv1bwiDqix1d0LzcF9RmstrQY7b9CFjW7paCPkPqSz1OU8UKt0uNQrkPOaqGAgSp3lTLFWffUJK7XZ5sMQTgAqYl9Se2wVQ6HGtB3KD8GTL9oVBqsCV74XuK8__CHNrlBPqAcnZgE2vt5wN0Moq_nufkrIi6xcfydYEGhT__Vs527zZPNf6xRoxm5jUoLKF35oaCstxSagHcixYlJwLkt-Fg0Sf-6a1hfGQdclijZ4cDbxGQrnP5Qf8_GxgO-S6dALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KD2bf-QF1cRSsVIQcauZOUN5GdSajBcQ3xzKnzU2pYQLJGyrvn8vDNp-WzsaRUAy3uKDQ453hW8D8i377168YSIDU29F92WUDZoXFpe0Q3iiX4HGUbpHv5eBck0KVZPSXADX2D2NYYGAkVppzrrRX2MKXXz4YHGy837wWIzXufpTalPxjbzVJGELElcvRxrFEP_8dK-H8DkRXb_nAznf91FF64fNq-e5IUxxNKByekzlfK44Kf4GUCnbpJMl3T8rMFhepOtvdYhlA0nMX6ZlZCnUF4mLrsjUHpXriwdLSvROVVmf743bBJVlG3evw1_XthWFtKIAIjS_Gz8xD89ZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LiKhpEVBxX8mxYkJLuoMQETsySGDmyNB7lVW_-7dsgPrTEIN5tLv5Yet96zprPObR-BwVbPdcFMRhk6sletjT7bsLOW_068R4m8az94LViM8zMNNkyHok_n0zgNZtQrCxaW9aBCHk_87LRMC0TwqI6kJfYFeIv2KtOKmfQkE0JOO_dXQGjrJvL9sypAi3grFtz5lEYyU6B9iEjWDU3bl6Q4q-pgwNMYhs-hZsKPmlhU7qf7uhj_E74k1aCl_HwelGp_tcvV4Jl9fZKFbX6jhnA5qipJoKrQiYtx3Y0rLiIG0I1v2a6a2zl5gn89B0dHP9lkzvcogQZTO0rQjpsDE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/amZPpYlB5PlB8zmC1QxTn-aSQcUqrPrDQuK_L9LUdDBh_rMsehQcTcz56sZMAlWaZZm_kOIvl5jHLtOHd9cbAUtVG5eyTDM6Yzbm5Bmo0VOWJRm35Rr6FDqYuHIugUQWMdLT-rEPYpbN7ckZ7HC0w8Hi-TkzupeBP7GSSmlOtaOwQMUEPTWxNF7W-VDtT21W1-FzVZG6kSqW_E5Xs0yFDz6kmzmWvtZTs9gxGBGsrPvm8vOzf55FxTehZmQ2AQ1cFmr1cZ_zwkb90AWz34JN866Wr4ZamI_d_zk9IHYtoWGRQTA88uANmtmEQ19CYOvNYq68EdxTbWJWbuI8yi3WaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qzUR4ymUcOYEz-GBYUcEDBzgbEzIqoh5YfWGy2_ff3p7t3CffXmjkVrYRsdIjMJQC871mF9IwgPbojbIt7PiRT85WpRTAbDZrAVsideArJ1DLMhCHsLVbJH-sQKzxv10tIx7YhxbdVpNpcxBx3NXNJs0kxFypsYYMNshBCaNobWOv5619PcEwpJP4S9HG9WcrqLU769rcwJKLxNSA9ldTwA-H1A51DXEQDhrO_to0iD-4gr4Zl3G1uZIDIgJaw22igJXG3caJVvcFzMpFe35tYjYJj5b27jM87IFJPdE7gP7AR0OWTXgT44kIAFx_h7K2U6q47GYz5oIPyKAvoKAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJOZ4msDuG5nIJRMhZEFAyxtMfE7ryjDS17gPsRjSHS87XDJWInUIa3EXKeInF3HHCMCuIrQQ4qk9F3TAHDon3ah1hq5tTlrHczWxVl2WI-02BoTFEvBuUnIInTjjf3aerTisCaa_lOn6vB_TunxO4sMkZl-Hp1sD36V2dx4Azpnje8I2VaExj-1mN0j5XoCGQukRvwwnC1tNDkKUBkzTZzx7yTKIAU4Fa_S-I66W-ACyJzM4wlJB7LvDgDuhudsLOWNb4udJAyFGJm8XZwFZ9T8dbcpO5awTDkbPHGxRv5hgcEwGhrbqIoBNYOasiq1lyh5XGM6OqXzyAqbcpcgtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tZyiRp4s_Xj0wwYgRDMcN0pjKjmbWDlzFaiQlncWyjubYw2V26_FyG-u-jl6-Wb7AafHOuc3gU8VM0jx8F39GM2DOzgGXsqFd8T_5MbU5KMbs7sYSRTtXkzZGVhEDOBQqPdfAhWqJg9bQwO2XFQFnAByNdticdTkWC0IRhjTiHYdpd4qR2XWZcfXrq_-QA3OjE_LhMKrKaDpneJOQMrzSnl150ft6jbp_0vzLK7BnqWe0vTx-W8EibKMpRF847SWQBmJwxS4Bijycy8zkXgpP0hErVc61cMM0WmaZ7Y7C6mM_AdsH1iGGZ4Gl0SkDKEjp8O95RIcYGuTEuXB4p0Ixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EHhR5FmisMV5pxzFUmmqru1TOPWssG8ZAkART2TqQfAZuaHML91stUBasRoCkP9Eve6Z6tox-dojPhzlJxQzv4RuS2fR3abMUKDrwFbn2Bn5snr_vWbmVxMlvOGc68FGarPPFIx96uO6AySIKUQ7WgbR9STuZ1nMofnmvKtgyhdziNXjUJxyc2ybLxRkWdpl4iHGOJeqpbxZaaIyiiLgkGG8JS1LbCLcd4UM7XVgRVXcH1zsw90KaT3yd9a4kWe8sEmKJfMFZdB1AZXVqgbhUg5ALjc67WspeESfizg8Uoq8Jy0YOsmjd_DnMj0KS2XLSEonqSj1-SbXHdwCaUS3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JiS9k40Y7TNoDyaWzyqs6fdnOX4dgqmP_6s6m8W0U_6d25F4ODA9MKOQRMKtPrHm-J0Ur-tRpw1ymDFIvL-dOINXFbR0y1i1GoHwd-hbDm711ZU1VDiUyKh7j9FuSbXaf61HBjiR1isSCPRjh8lhs9GPqVhajCOOxWbOJJK8mmxGpfhiE9YhlgtNkEjiLuWkJdJynb12dCSkv4gNj3Mg4fmDGbyMN4TqvnsKhOLNkSleNdsru0gXQp7Q5IWxlXjtpLGIbX1itSPjz1JgEtYi9e1ExsTWO2hF3plHTFkyKOxHcj4ZM4fzzdWlB7bi2qwXufb-DTNgEpr-CX3_VVXyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TA1BOszdYAxAJJO69WVNobQkvIo3j7IztoC39m4iQH4GTVbJitZDfPZGJD_-T0TMbaBYcJ50ydGj2ksihcJAfrqzZpJsediEs37dCjR7dOTYOl5o5LAMI67yASCF9DC-MWNtVeOtmBDTKUJtZLnxe69FH7FY1msuM_IJ_yHA-Lqr9gjNLwUHpUg6SjD7ldKx5Owxpo5IZRIGGNAuhoPuH6CZ4f1UNmya8PEx0Hx0pFMw1ebaL-cekP3Zkph_oBtGd6e9n_UM5jhqrjkIX_l7xcFqw6GxYFnxW7fwGdXS0KQVCHkTE5zmPe3hr2Gj3BDJA19VQMqKY45nFmFrCtyPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DIPwBcFP0I8noyAFIVH6zFuE66SQvxX5u7B2JYJNKCuY0f9G3PnxYpcFv15uwi-u4roU_nHa_RRUtJoT8Y4womWC6YaRlJOT_Wb8T09NHcik59wzl4CX9wejxc5VI1nqPd9npn-mkifF0VRhFfeYYZhpD2u7GR4tUAsflckJbce0vtLvrlQMgnGjLiUe2RiC5YivVTtDVQDzqeSd-IAWx2w1vZO1joEMhGWzNiHl2nY8H0paZdZa-nAm0cn_10a4xX8v6M79bo90Q7z9Ce6hgNQAKDeByYZfX3iACE6LScPdXNGiBiYsi4abAs1kavP2jzxSltt2TFVS6B166ZH5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_bjiKfXmUDJ6inAW_sLTMUpiLn4iW6xJAvoEU0F3R6nFM8xAag2q8Gok3UuxtQttTIP-DM2pGOWmS_UVznGqWN8bgBmIVZLjmzoMzavuxSCWQa9VVangf-MAwzbpwGQOwcBnaqa41b2ztWnXozoyBjDZ5nToD2rGQNN8QhBGR1OXFIgGwwy_I3PvQfj8Pe2t3ZYdScy0WyBal8s5rC-cpEoPyVGhJ3Kb9pufdWJJ4iNqczadlDViw5qs_e8k2f6zPoc1bETB--3jHQnBoNdJADmO4xxDqRKWyuLjwpr8u1y8SFPh6mxkYYN9oqEVuVAotaPEDpwbYx5tft9PIBTnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ee7cGhDJXYrtsqbKm3QLy_hOgZN4sNhjDIklwYjaRLvXqAF0e3wakwvRrkavvmJI_nlsgER-JQyGToAropcFn8xopzHZnrRhjYB54ZRmJwRTv_VBDPM-bA7fTX9LgxcYbTFqBU8U9AwDvmfnaYOG3nZft3vEO8fxH0SeWHcf1xO1iH5V6xFc2INd6KIc2UzWCCwHlfmRIbxICz522uHJr4flVBi23D7pLYUs-nwwDcw_6tGnHHyXkafeutZF4hBvJ1O4uhoLSC9oDp0sMxJ5XMb2n1drNDNXy_MA9oIU9O2PqBxwSBm_oAu_auzxavM6xWyfLMC273wXH0Ahbee8DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OiSXqsgUkZ3858-A-e3ASDoTgXOXlreYq3wf_vqKAlzW64vE1TdZtWqPdJKjRbviuexea_pV4WzJ0J5MXnsfWMGy04WDlJRGhW48edXm7xtHYEj9lioa8BoGGP2xUsne3kVDbUMyyqGq5UAlvOrcA9KJv54VOsU56fJEa6UpR9kIjt0VH9Py4zi8OHlBuYU9urogW2PJWVomdmPrraSjKo1WND1JEZ9kWh5KyOgVg_U1EtIGZO0A6jq4JxqAbIrX8wdSqHBSt7tIO9Zg4GEv3DdT4GOGghB97-Rvx6w5sGC1s_NcCVe6keb3v7I3fjqYxvqGH1-X9OpoSLQ6IL_b8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NVhH7bRL9tyham-wqmmKvpMcCPV9YlNoJWTXZGbOjzKu1-NY-j_3vL_Y8sbIw8w0Vd0MmdmCccgtbj4T8sgymDBmul8qxSGONNgy-wpBOJPoZ8wAqRmPf2n-2vhSV1whwQ05wG0_eVmsxOD8sm5B_JuuGHsM4rt4TxSNPaBsEBUq4EUHaJidPpU2ut_GNRODvQrUsm6-hrCQZKiMBV5R3wewGsxJkobTvyZycxkt70cTz_GZAth-Hwfhlmp-E216h3HgI7-Jb6ad9BOKMkTSX4n-DuxrtH5rL_wSO6d4opBZAVNoN1ebRXNOaJKRnQs6ik78l_YV0rsNxjma182xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LzFSxXUPruQdpgsj_83xvTglIWB9Vh16SFv9CPddgR2xLX0zZbTKsu0KrODdAGrmc9UGm3u0aeBbXraAPlyBzetvwmQ3HWajEGPrK9cAADrJQGlpgHTKz9ZX9VuiYIth2mhtM9AysuPsv0eF0zVaEtIZJPMfZBqqdOgSAxpSjNZpoYNwJONbsMzDgVrLBPh1XP3sstVnq-68lOaULcZdUj33t2Nv86Yr7Xme1esgLLp6fslDoyttwNj2KrcK3q033s_Ya1hrdxzH_2nY8bVGc-wVQwg_4cF5hRaBsuUw9h-uZQ_nScImozUaU6DywPmgQLooQHb5vY3-VirUaRPSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d2oLi3u0DVKQBjel4vYQM7UhfwMkNjVpdSRNCcyFExSGkqucTmFj8bLXPclrEGmELs6xhyakQMhR3Se-18VP3lqs_kf7wOAuGRChet6gGhpv5P5yOdIRCbBzOTX4qFtFDCuGqzKBolsiRtOMxF8o3PsWuGgo1fWbt6uJCBP-azHQ3tSjHu4kGgqonNvg4woycjqvYcyn9vqdOrww963KhDvxlJU7qJH49HxCBBzLTfFJgj9FXfAGkqrIuaxKd-AEz8LGXIiav3plNSruw5RxZ5JpJ0ZaV2_E59fEZn2tDFDCjUWaoE0iP5fPxLaitcO20y-wHlRHxI39eKDJHaQtJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uA60zddr-QesB34JkDd3UnZMcfBvH19coDtcbATXD6_DA6KP9yg1sKwuFLY0AFqN8sagWbfTsHPrA5If8jlk-Ssv_YkZ9mdivf-H38Xa3zfUWubWFCk_8QEbZRIABVVuY7GD8cAkWm3aoxb-I0x41OX5AGQfWZNggk4lihK3a9JdVq6A3uNqTFPYkHoEsUm9FpJ-wRckn_X13nptXdJscoiGH39AIUb_kKgjXEwJ7KxcoiEL5bOJ7WXaMXqUo00NsxrdVqL0UImVl0XdM59zgLWte7OkODmmw_0QtFPuyTjr9G9PLfTjpR_ce7-OGQuO7FnCWWXlJxlUMhPB5Hjd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BZitFPhky9LIZHrvUyMM-C9C8FKPScjCms-gDRurMifYuiKOpKaNx6vl4QgYogtKW-0xX0qF6plRzTVolB09_B38EaWzpcHdZGU8UgyFzNUpu5u9xWlu7K0lAhvE3_3o8KfVdg6lVfbC-6cganzp8XqgAhD2KqOFx25VdEQMdjQ0cB8rM4hqa_0f9XgifMLnq_TSNdZN1Tt2bOnyB7F7RNessc0BF5s3teGQX-JzYqhfDJ-RzWbTZdM7DF-shMXy5b6OH1kJ3u-RUygyZoDXIJaKLkiAJu4M1jGAJfjiHvjQVYZz82WRxMcBvSxP0tKdb9nRN14kj_kzak9DGqp-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xc2EFPiFbalnuG5c0Ifcri8BTlEOJxuff4XY2YBRvWgRB7gkSxyJ6qsOaal8r7kXzFBj3l4AtYMfXRVq84M1xvrUEAgaTAgV-bdybgBgPP2X0eP4FfoFZKeHwc_2voRJ17krlgeUw7AG8YcoyfhGfpRxvjCp6p79m_4DS97RSuWCQvwiMWKMlWSBms96y2uzQCkQR3MwhT6JPBg-pVSgyinbn7tn-TM6DxZhQU2DAGR7Ns1sd5kauYhASnkVoCt6on6z-pLl-SQjZHZ7bMZjQuHJ6bQxOEcFrYWEpxEG2wfYQSsWe3IPfNU6OfD2RP1vGL8UsTL8Y1nHx_NXvi4KjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LnyVpQ_zzcIKF7GOOKUcPo-wHzQVuQ1SZxA-sVkzdeOCOV4ckiPFB8imuwT3VlvuA3mB5uE8uykxCSO78NzWZRkjmWDNl7XHlFnxz1HduprLNYKsRWhkqV4wNjVB4jTsvJwaMyOXRiSvOhVxMwqtq6XRwcuqAqTYWHD5JQUKOopxc5C6iVTn_H2Z4dsfZPp-U6-TBxuEICqNhhHQJzqxxVmxXtDbuL1bzRBstIjdqyJoEpp-N8Y0y3V8jN_OEm-bXZNFLwZ8vOj6xASHNfYi8n_7vqsaXEYROd-Md25UvC6TPU-KUgRpFXu6DLRrHaubz30cFRSp8hjXwReSgiYhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pdrxw8NFe5OJnCKbKmO6c-RqvlUt7ajA2PEcMeCtljwYF_S7_vC4M5ZEOz8tb-Pwptruq2gFq0D4Magkapxg1G4CANAtzY89nD6PMnMjbkKXmpvoDzmGBu-OFkcXWx-Klq-aNs1X3uhT0TIUQ8jC-IuyqAu7HTC7ANQlTjZWT1O_toGnSGxMVgOkLQOx_QEI5vFysFCuIrORLdqJ4WvL1CYUPTP8GsUT_rgiIWzIZ3KTAwOeqdIKpFnsE_lXEqKN7XF4hUx8uiU9yjjv8SQKcOMl_jSQ-W14EjxyVDxFBSWxIHsfQybPfy0uradkzqfneCTlhwapqkq-OUvBiV33Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DeYbvU8m0B-jY-TUNNvdBYo8AUUlxU3eLdIAmFHR7va8BSJ1oDZn12UpPyphla5-_8JjCarxlA9_dsy8fVlgjAu10wfgUymC2jU-eIC5YiLCZqSFIvjAWbm4L7egT0pW5ioMgRhNs4gg39SHSgMBvQ48yb05iJpeKjpSiHzu0Vf764YolJ-wCxoRoiFZ76nfgS2p20Ew-XTiL6TbdnJ1ztvbA-CHFVJ63g6He0Ilc7kg7BiC-w4UTt5Dd6ltsVeeMUVLdJCrxrm66XpRxemn9iB1L2vsNHl_iAL4XqRm1P9cmRykC_6Og0XgC8nJOuUMVl5ql-_C2CEgpAaMOrWl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lecaEra4KOBe0CzRYC-wIip96c14dvVEwUNQZ1DKmgfTcKKvqeWyvtTRdAGvaTaVZSZMGWXaYhFzAue99GsOT8VgZYFRUF_uufm88Z82jC39e8vUCtm8Jw_0mQIWr6mMwGWL954eDBLsDrblKvxKZeq2IzqcYHujecnQtucI4FhTGMyEdAvWaXavwyz10ap0SYKZtTPelFTuyxEX2mJQtHRukveLEUw_DEqkQTR6PVciFjELOYj8-CanwemsGul1NUeQuHMBgTsfrNGAxUICugAN-RdPzcNw44dnBh7iKjUR4lQ6U16MEW88hpZCD_Iudk2Q5XYAcB6hYXwDl5sI6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aEyCxBXN92GXv-i61LpBuj4ufxWbtlF_V4lGvmR83Y-Kavwk_qeXmTrh_-chvNb5ymPPN9bA6TW6dGQgjDh3CdhOZsgjC44QMc35GkiodjBlBg_rphS6MMsiVkyMEv5OXbyK7pPoA6iWSJP4auUDa6rTMwOYasdL5fjkS4vBM1_iLWNtj8slXrhTm3IDOQwEG1MCLixM1mWYBhfLvkVHWcbHxpyIGBVMpMSW0UXxNxLGz1ZgmEjEHQfpIxed81XFEDIdJQv_mZUfd1CgCToFESx0uHZsapdw_BOlHwEej9e6Xwy8XONANImCGexcFePFhCNyTGcL23gA12mIjJ5qAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xq6SyuPwJeGCHNyzVm2zSR9y4Hvw4Koq0XdI6HkhMH42kIEtX_JlMrJ3yOPbFt2Y2wcd2IlTQ20hMDsIGy4X-NOB4URN-B-huxwvQr7TnxBe8yoGuzthJ_7VWh51J5EaAWi_bBtIcZ9nDO7O29kxUMSoXe8s7OdEK6pSJJb22_VhTwzo4HiDQKuNMDCT7CsKKmU8QPVJOl0QxJbTa_8LgLKLTRnRX6Y_fpiT_FLDDSO94WfETnGjwZwQrEztzTy5zpzNlV-kFIOyZkWOm9MNriBOTtb2JfGkwZmHOV1ezejhWLjVd8aNSBq3nK0UVfdnzT3wi0I0WRHxPpVe6sHhbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qEVE7gBYWsUfoDpTTRuvhnf_2SfWlKPFVbtn12r7oK2YK6J_ZUBFCQ3-IYs9T4XZpyluxaZMf76ZG6EJJkKPSezAO44s2Vk1RSJ9gg0IFeCzMq9AWlPqxBj6ZY3fQNHH5bwGGDP6AtH-4TjpXMA9WUiGGO9R6DYFI2fGk0attXl5c_0LVV_8-lOn0rn8NfQaUchIXHUu-Bht1p6_GWi0jEjnjiXoS2CmEGgs6ioxVRJPiJeGA100teFtx4INt5DJakC4au2jhLUkk0d7bkYFvkSqaO0dXdYVn-zr0wrH4f_8YzmAPgJjECniAgi8qY8QtvB2d52_vsx6jV0g01_9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J-ULnCMKz8rkRfP7hnnmiO3QxGFK3vZuYVoCg24A6gvA1xpgDcLUADQNKBs8R075wH5ydjh8DD4Fa8ShNI45Q0zWrcTXpysOpFhzvQz2f-fZJ9FgJqubQ2JxDclanHJDUS4utwoTr0AfKMQEjjf9wwaMJ_GAuvVjvFaXvAY9HF5EjoUjR-s2rGdCBed64VKGZnRO42H-Q9iNOwGEOftyaQVsvCixkuVHwluplPjit93-LxkgVlu0kK9Nt3zeu-GFjS5jgg4kHU0DRTWh0KMy5jdtHK7nNKcqROXj_85Qz1QOufXeFwdLUKPJgoLebIw9bEySj5tROg0sG_FUv5m7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eHhEmUa46xcFAO1HEWTYChLnwHF_RFqO6U6emEzNoHL17jBwfVAAlaW0gQ1P5W62d63jR8BuX-kgih54Qme_ehpfxPmXY92EYByLOicIS7R5MeaLYowbjzDWvBZK8AEgC1x2rA1uM5jgvlBEoXMk8-5YvqabtjU0d3ryKXVut_E3jo1h0mcutxR2mEE1erjPD0XawpE_NSsXtsE2WFyagW-qm4bxGEwIN8wAjWpDzhyhG1PgKd-BKMGKL70_RuGaJAYnKAUZRNw0O99xqqxaty5ytr7Me4OUWYuhABGy95rGsqLjPNcEOyKzWQXvTkHYMuFGVYRsZxxUIrNQUJ8nRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lh0fjGJmuujXfO7xPS3YwUjqYl2sDY0N4gOu6btfiKVH-Hv6ktvEg9KDq0XqzIOa_tppaeLO2DXSWePHGpZxSTPTJeeeWE2b-Yw7_lmPCev2oyHlfxeYIK457f7FLlCxh0mBpmVnFTusO5rvcHop4RFKTDA6bllLvqvVLeV8uI9GBRJ3KY-9zpIblrVhwc6cGImPIxlh4eqwT73PV8tb062by9GlMqP-4IEnccMMK7ojBZq1X7gYRYIQNsk5WAu-rJ1VdNxYmBUlVBsvC0zayA80M9J8EwyuI9QLMXr-amJm1usHHNFfpKH5udAxQvv7NE6PzJAIeE5UkcM0PNfacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QFXuW8yppfYx1mpjsWpKh9AREqHH0NLpBts96HsG80lK8E2aEz6qq9hxggObRzlRHfmUCHBAximF62K352Ic2Ku3D5CLwrwO5sRTlK4j6Jngb9yUCZAaV32B7-txurY2M5zhbNYZ13_p-atyHZZhlx5LNij7rHgWy20hfiIy8cvbeU0PyLwuGG-dTdTKLGK1VnYbzF81glUFJ0Il1QsKroTF_pfDcsmJcOi176LCVA0ZuPP8pLxcgLhEKvnqW5KH5vTBt5YYBznuShRFNFKUtS5nl0YRxfn_7oG0ZkFMGd_AmC652XwyfIlg-7GS3NNYYlEZSMpHgLpl-eGY68gmRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nPgARRrWSxNVnaKz4vFvQuzqBhYWBcQzA4w23IFHwwHjyeZq7cqkSJoPnT2zXNqMSyqAMM06oUWzfFinsqloMaB-B_PkvqIjO3ltOonNESI3W-g6edr546xcPQ1E5MsU71FXGxPy8iTXziOwnAKaeYttQJKP7_Sk0dcuxJch83BCnSDSfdRPNFnvaGH2sCIrQD-O_th6Cm2PP2XttNRYzC7TA-ihT50h1hWhCmu3nXx-PrAUJ8jctUdTDNYjX0Ub6OtyIz4fOq9GKz6dwv_s5GQ5Ix8H-67tqys-PrmE4AWFpf6xQTlN7yNBFgyJPQ3dEBlqQVc7hRcCal4Iuyogvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PPNDa1hHK6DjZwTnbf03bqHtKfQVotr_9sPuC17R8g--Py8SOeVBplU4AtCq9pKSmshK_AHJ7ma7hq71qCWufsnqoN14CCyBpHAFoWxAjhMBlPpBa6aMLVOZIPk68ElLi_cyasZRHNs1G7yKttsEWuEze9AEHu5rL47oO4DBYTX6LmjdZ7Q7pvh95Ly7ODLefaHxosD_GI7sBqQPTZhnJ45pf9ChuvkgWkryXkimttJbBdQkihx9IMWI0Vcz2lTvhRoDwUjWyOgRP80Iz2kHkDXNphazhff4zwVoD5Fgc53DWXhdzDz_gQtNWdrj3ucYwf6Xw28M9KTmL39qmV6-gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NBeI-76IYM1LuOo1sjx98-LxuGr3qEwvjACNzB-Pp3U48Z7iF_dowdHjh7mUo_quWM5mFKDkmO-MlUEcvqYpC4RlEXy-astjYbIz2vJ9P6Eks1hQHj3PJwjXnlziCn0WSKOc9oc6f1pFwUyGD_YeFHBqBjw6V3ygV0wO_PLW6MS6RlKii3Spqy_dC98_zf8v3ZXQ_IDAKgI8OCEDDFBQPLVwQmggmTeCgXysdQQUAIdlofN5Z2j6KlzCgc56hMlmOn71YJ5b9I9lPaMseWV7NsQRvaj9BC3ewitlabM3Ek28-IfAZdZ7_6-8gN-LACDQU-oyB5hYsgmSS8uIAoxdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vjv1zGibz-gop5YLz3LRqOPBPUepA7WYM5Xm7z3g3QdLbCK82MImBGgfzbUFz9DuXalIt49nnhp1Elu34VTI82Yw8cfNRUmBz_-Bx69Pg8pf6k45b0sjZdjApM42X3lRtEQ2MU4H4NqkxRGrkedOCuJI3jZdzgINAjHUod-Bzx4xDsAYhaHYSA0LaCgNo2zdSxQjpE8E0ru91pRZgYY98uvxP7gH6bOzoJlgz7kOCb7bX7FCGAHh0TlLPJXBAcwCd7JoaY9mnPL0xtZIx3NhtxkJT7S_zhmL04g7_WAq6lbK8NWwByW4bL7zDaRVnLzr3N-8xMOXSYgLLbJQSVBCFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YVXQDs02M45PY6wKZ34rmUl8BKec82LACsfGn_lOYEaMCJWsVV6ur4vyuVKzWl5h8CEJBDgmaMDzIvDsz2PUUzy_s7qZrBz360Zc2vk-v82vgLG3eJmERQVlNL8Zr9sagRxeafpw3VujtSOGlBs2EPgo8ERR6WxfZoFxWGaNCYgBaF2_jKvlPECxRStXb1EDqM5Mbak2Yak21aE-0yZe7OEJVu4_xUIYTdERbS0pH5-hAIKzAnnKXGGFgmx0B-vh2xLG_NYB65Ssv_eaB6pfjPvuRSwAHw6gWy-yY58IBBp3sQuSphzIwGU3tEPxEaJsbZvEzmzfrDk_OIzHHDGi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y7Ev34yUV0szNuqOqYWziMf_h5cOI40TKAbi1juzWSSa6pNOjZ5jYpLyT_wDat-M7-bTcrHvdN3DqDw_Xvek5KqiUiRUU22xA6KtiIGA6HHQHEKPeeX1VExfs6GnRdr--7odYWkC2-qDmlt1tXyD5t2p9lysyEn3N4bdt_v4cuJ3QWZLsOG9trSnhTT6CDYJuSOp5mTYlOdv6Th8TbnZffJEF24axWu2Zi_Q1JOEkhnuRzfL540hF9eyjjSBya5uVYO0uRb6EGNKj0DiecjDw9zDEEotpl1k9ugd_bgrB09HM7JRyGQnuuqpZbG6fOfxbCZvu8jrAGcxLLPLY6SkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q45FR1oW3UPRjDc8TNNmnkcOTpum8iT-6y-geIQ2KURN7Y_0inzO3cfnUWauA7c8qOzhXSKQJTRZtepiVM26PG8rcgDnkSNp14TG--JUzfRbdjSfZV_32Aa52yeq8ZY_xLiHMXR_xRgFYOtymj-2mk0526rK1qIEnb0PKsr-kxejS1CIq-otPM-j-ozobJRrI0lR9zANqK1abI0TnBgWi33n-yIlJqJA2KF9xvG8LuCP8tLyHFFSe2OWFHVHIwbW21qwKa_R36T5MLsVMJKYtcDrqk4ly-EWIBalxPQ2JqU_3TjCG02VqZpoCRt7RahHFrfvqiIZxdX5n7iPzR8wFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NXkyf3YEl_neQOkAm3iF51dNy1b9nbBCnH_csri8Fa5-jPivePp40Xm59ydRvxbu7gPzUm6NB__AAYxwa0ioNbac4TF1sAns4JUEVMvLv-zk44ER-H-w2gLauJHRsU87bBE7FyWZ0bN8F90LxgPPMetEadoIR_Wows5XgEq0vr_JKv0lC-e9X4F14QPElOTD_00hc1FZMk7wWWfuvzja2eicXXNKBA9xd4r30xzMR0Wjc3FsQcwPJ0930Ojr8vePmgAO-OGICfcCNIWb0lHIK_zY_57D-PlsBnHKSub0x4K0GUVfSSH8QF-55ZhksXJGAoY4NdQXEoC9FTVJoAQIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ubs7XeaGotvCI2ri_KhDcA9SavPhYoR6JWVfJ7MZbuT7Gx-BGyZXXJ5_yURz-rBy3p7qiSQ66q3n8czD3beXUEDGmh_nnzYj3s-2YxaDhWJTJvorwQC8wWQSr62tNfFRvPlmw5e23Vg2nvuJXyVBjaxtd-opxzwf7bOr4V5bQrNTQrPR5lOmUGI7ECloJwm_hwOwjLTRDx_TMOax1-oRjMe_Y_PCDqo88cFVaEbX4dpmQfAmX_KqMrhYqYUwmo6lkoQYzdQGdvuu0WN4khzvG6qpGtI9nlpOD06UYyhAdOegzU0jqAlariYDn4jmQ7ednvQUN4A6SzlMgoTar8wA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rqpUH3_lFlOT9okDsQBoPHLbBBZOO2YIkOXr-4gjNtS_TwMlD9geSQSaxvZ2B35pvIYGGoD9SSDsg3sHYCagVqbXmAo7oni9LSqfIgUbV8X5ZQjsMYnu6mcNzr-ZLZQCLb2_Smc5rlZduzw9nj0kPu7JA8ogbBazAiQ9IRLclof4CQvf5E2oBb85R-3LtjzoajymOfTZUyAISSibeGNkFfdXg_vF998UrAJP9_p6CiQPSQ5P0I8itk2zil1fMkDXMgJ7Z2i0X_m_ajsf7CG4KiCQvAtT-BE-C_0KZYu_GXJtJY4fdYJ2zMyMQAgedknhUr2r1HkQgbsEF4WUhQoKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b4CzS07zvkMFU08HrTRNO8ghsWt2szcT7co07P3rnbD1QkDdEP_mE8hJSXt8mQ6z9WEDOLQMqqFoExU79px5i13_nR9MpsRQixreA8iWYcyv0lADMc_rvyC-2QHK4yY0b6LSzabGVdtAPMKVVMgBKr3uMHSOG7q0E1y1fW09fBsErzMasIJSkgd3GX9CrWQRgZ16Yfu6qczI4V-FHXFvrEt9btyK89pPPbnkuaZzKNjYHtFaRGyNc8mn-RWXJDnEa1lZCJMkh7IID1PoSzlNdNCTxJV-tk5PSOFRHTKBAuz3ff3ZQs1hbAq81AHRLmcRckTFnSen8RAAv6bzRDZArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VI4t61b_Fo3UEwleGuLd0VydnvG67UJ5EU2xMdi87rYY8_XmjnvwZ1U3E5XrirhCliw1Bp5kI0V17U0yPS7j6DxuiLuQET1o5-lvuCDGyTuCsUy3zNvdRUh_7giXq93adJHyik_dOJzvVYCOPMK_F2ZN089P8j_VMsl57t37CmeJmA2B_NqEd_g6kr_zpcpB3mUeRUhKQ8pS_KWStsfdJQtGMdciamPrdQcRDfz85YiSiBrbGkZ8nJqdRpyPyDYUdkFFzFYz7LYYBm9XSz6VwMbCGvXjCrHRx17p9HZ4H4zS3GUmvDRR_OjVZgztn1IFTHdqVU-PKejwpW2EuqX91Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7tIO6WUzTFfPHWXFHdrd3qpWwM2GRHPurOuPF4AdganUz3vzenrkVbAMLAogADuOell4e9qY0myyDsQpRwx3jKx8WliqmEgLPHztU1bCS-QtPScvMiPFn6hEp1dPBBjdG83OhA6Nk_Ci-qMRG39Pbf-jV2PgtOFWorFjKzjENSL2epiQN7QyZxHW8QfQUc16Ksr3rd9FkbGwslKegWYtSz4_tdUO-CQbErtkaAVVb-dbhFUyfZ30vnpnxK7w7pqqPveXHuuFPFiBVUgWF3IVoj9TeyzuZy-urbQqpuwYczVzsyy8f-p-LmnB1p8L-3otga9GAJhQpbnwpIv-U_p0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hW5Hz3z0ulxXBnkO17TRN5MpBZNsdmqUDjtBwibfMai-N_pmOka8Dx8xLSnVpcipgwwT6TRrR2-vvlRTPv3o_3RPWzb3W6GmBdlYC25AcP_GT6lzwDeMv_gsF0gqC38OtkurTar3mew5JLStZejbCzm-GHQpgNBfWFBnI6wwXH8qn2sFDEXxlVRw75XIeByWTHK9gYhMgvCVL-ESrClXA5PfnLd2rSK9C2aszbo_Jh6XuPkG712DqG67-H78n_SI_z8rKMH9F6GcySFgtp8C3Dmy3_kGPThCpe4j4BUEhxd67QFCHsdVCw3k98ui6Lyq_G4cAaHndLdRKAIN9x5yWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MS1pMMqidBGk6J3sMn13dHeFNM76SU-dmGKodVg-RxNIGNHyFMEqi3i7yw-5CSGqMtZTkJbbJajnku-VE3zi5BqGkehF23Q0M4mEDUMvinHjOHihKx6_p0FRRQJT9nnLmYwxKKkbpd54PBChVnh7_hAFz9PvPMC_hsdZJ2cLQYTDHJY98mZ3dfjveN2tSuOPWSVte7NOmph8OjfSJE4UcjKugq9-kwXRSSKaTTniK1_lArt1R0r1m0zF-H7bM893IXAQlVQ4o1vAXWcXsC9OwIpniU94isXTsmfKGwdH43oi0n_L7k9FMPHAVF-AsnsCkm-OKfj1idJztSRpwKLXfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kVSJcXvhyWvkrHfRkdoTVRUVx5RLjfxfNknmkpenKU1pxXQIEg9otKvDofAr1qe3ZKqItvvLYB--2-bPmI1xSPCCzgwV-RUYnOeihNhllAC1AxldkdPS4nZ25RHhgXrbwprPXXrD5wmdMG6UHkuYAOY3ilngF8QDIUAUDC7mvTsqlVcVsVx9jcqcBTd7thBRdU_i11HGNn7eh3163jG5rqAc-9UCpKdJdCoT2BnJ6pAj411WeISnx2ZfVe4ruxEH33P42MjXmtzLhe2eyg691gyi2DZwUEVLN9yjsO8U1g4kNl_qzjmwKCGMGmtppcQeA74gZWUv8PAEaTddpxeH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
