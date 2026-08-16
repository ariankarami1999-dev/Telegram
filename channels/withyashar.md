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
<img src="https://cdn4.telesco.pe/file/eGCcVIhc5idjFcTHcrG7wHZ0E2jMGu3CZrrrg8XRiRSciVrF66qW6WlSo3AXQ_j_zHm0OXv8uBhDI69T2cQmpRETezG7DoN1b9edTKAMHyS5gLcwSUj4l6yVSc3gdkv9pvYMCaPNXySRXajpHGti6dipebq93ksMG8cyIy69C3RctMuAoLhBCaFdw898yYaOFVN3_d1RI0lXErO-MsD6qOOOgZ5u_RT74ZQhoqRW5DGGRXpmy_Bwlu1IvE3dVJYUoXGOkCl18g6ID8-wSSuoNQ1rxfx4-sCwZIqyg9iCORQb6FV_Ehh7zoMJleA8-Ykx21Yce0SP3VKHi0OUoyaACQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 444K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 13:43:56</div>
<hr>

<div class="tg-post" id="msg-21045">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ادعای اکسیوس: ترامپ از طریق بارزانی با سپاه تماس می‌گرفت
مقامات دولت ترامپ کاری غیرمتعارف انجام دادند آنها مذاکره‌کنندگان ایران را دور زدند و مستقیماً با رهبری سپاه تماس گرفتند.
فردی که آنها برای کانال ارتباطی انتخاب کردند، نچیروان بارزانی، رئیس منطقه کردستان عراق بود که چیزی داشت که کمتر کسی دارد؛ اعتماد رهبران ایالات متحده و سپاه.
بارزانی در طول جنگ ایران و عراق در ایران زندگی می‌کرد و در دانشگاه تهران تحصیل می‌کرد.
او به زبان فارسی مسلط است و روابط شخصی با بسیاری از اعضای ارشد ایران، از جمله اعضای ارشد سپاه پاسداران دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/withyashar/21045" target="_blank">📅 13:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21044">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیویورک‌تایمز: جنگ آمریکا با ایران وارد مرحله‌ای اقتصادی شده است؛ واشنگتن در کنار فشار نظامی، تلاش می‌کند با ضربه زدن به درآمدهای نفتی و منابع مالی جمهوری اسلامی، توان تهران برای ادامه جنگ و تأمین هزینه‌های آن را کاهش دهد. این رویکرد یادآور سیاست فشار اقتصادی سال‌های گذشته است که هدفش وادار کردن ایران به محدود کردن برنامه هسته‌ای و بازگشت به مذاکره بود. گزارش می‌گوید این فشار اقتصادی می‌تواند برای آمریکا یک اهرم مهم در مذاکرات آینده باشد، هرچند تجربه گذشته نشان داده که تحریم‌ها به‌تنهایی الزاماً ایران را وادار به تغییر سیاست نکرده‌اند. در نتیجه، مسئله اصلی اکنون این است که آیا فشار اقتصادی همراه با حمله نظامی می‌تواند کار آمد باشد یا نه
@WarRoom</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/withyashar/21044" target="_blank">📅 13:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21043">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسکای‌نیوز در گزارشی افشا کرده بیش از ۱٬۳۰۰ کاربر استراوا (اپلیکیشن ثبت و اشتراک‌گذاری فعالیت‌های ورزشی و موقعیت مکانی) از پایگاه‌های نظامی آمریکا در خاورمیانه اطلاعات منتشر کرده‌اند؛ اطلاعاتی که مسیر رفت‌وآمد، برنامه روزانه و جابه‌جایی نیروها را آشکار می‌کرد.
کارشناسان امنیتی می‌گویند ایران می‌توانسته این داده‌ها را در کنار اطلاعات دیگر برای رصد نیروهای آمریکایی و شناسایی اهداف استفاده کند. در مواردی در
بحرین و اردن
، تغییر فعالیت‌های ثبت‌شده ظاهراً جابه‌جایی نیروها را نشان داده و مناطقی که این افراد در آن حضور داشتند، بعداً هدف حمله ایران قرار گرفته‌اند. پنتاگون از سال
۲۰۱۸
درباره خطر چنین اطلاعاتی هشدار داده بود و این مشکل همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/21043" target="_blank">📅 12:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21042">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29877262ff.mp4?token=FQVkhg1C47-X8qlCNVCPVt1MVtc3af-XiYWz9i64gjPvAF5IPVybrpy0StZtxbyZtVlJp_KWCQMvniY1Ne42YCNK0bGiXpKUwE9HnW33YXr5q92RN7lNIUADKrlEEhkVxGZsLBS62vWo3Qju7pde4zQW7vScrbQ0B8ywHerjM2fSLYKI3gI_f6059oTSvp519QJ1PtiVrFZfztKD0WlIdkfEL7x-x0jfJm4NfIZMjIBeYlGYAttPlFy0Atmroi6_PQkOpmf5jtp-YvKMqZMAetQzyBSA8WcA7Av4jBDvA-XTAxzqOxB1WK8yaY6fE6QPw2tnEGLpiMJ91Fgoj1mr7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29877262ff.mp4?token=FQVkhg1C47-X8qlCNVCPVt1MVtc3af-XiYWz9i64gjPvAF5IPVybrpy0StZtxbyZtVlJp_KWCQMvniY1Ne42YCNK0bGiXpKUwE9HnW33YXr5q92RN7lNIUADKrlEEhkVxGZsLBS62vWo3Qju7pde4zQW7vScrbQ0B8ywHerjM2fSLYKI3gI_f6059oTSvp519QJ1PtiVrFZfztKD0WlIdkfEL7x-x0jfJm4NfIZMjIBeYlGYAttPlFy0Atmroi6_PQkOpmf5jtp-YvKMqZMAetQzyBSA8WcA7Av4jBDvA-XTAxzqOxB1WK8yaY6fE6QPw2tnEGLpiMJ91Fgoj1mr7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : پاملا براون گزارشگر سی‌ان‌ان، همین یک ماه پیش در ناو هواپیمابر آبراهام لینکلن حضور داشت و آنها حتی هنگام بازدید از کشتی بستنی هم خوردند و بسیار شاد بودند ! با توجه به این که پنج روز قبل از شروع جنگ ۴۰ روزه و کشته شدن علی خامنه‌ای، خبری پخش شده بود که ناو جرال فورد مشکل توالت و حمام دارد و تمام کارکنان بسیار ناراضی هستند و شرایط خیلی بدی دارند. اکنون با تکرار همان الگو، ممکن است این بار هم یک استراتژی برای حمله دوباره باشد…
@WarRoom</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/21042" target="_blank">📅 11:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21041">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کاخ سفید : موشک کافی برای ادامه جنگ با ایران داریم
@WarRoom</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/21041" target="_blank">📅 11:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21040">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ستادکل نیروهای مسلح: تا شکست کامل دشمنان آمریکایی اسرائیلی در منطقه و احقاق حق ملت قهرمان ایران و تسلیم دشمن، از خواست مشروع مردم و مطالبات رهبر عزیزمان، در برابر آمریکای متجاوز کوتاه نخواهیم آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/21040" target="_blank">📅 10:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21039">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">منم مشکلات زیادی دارم ولی برای شما شاد هستم
😍
🙌🏾
@WarRoom</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/21039" target="_blank">📅 10:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21038">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رویترز⁠ گزارش داده که حزب «یاشار!» به رهبری گادی آیزنکوت، ژنرال پیشین و رئیس سابق ستاد ارتش اسرائیل، با شعار مبارزه با فساد و تغییر مسیر سیاسی اسرائیل شکل گرفته است. نام
«یاشار» (ישר)
در عبری به معنای
«راست، مستقیم و درستکار»
است و ارتباطی با نام ترکی «Yaşar» ندارد. انتخاب این نام نیز حامل یک پیام سیاسی است: معرفی حزب به‌عنوان جریانی که می‌خواهد «مستقیم و درست» عمل کند. آیزنکوت از چهره‌های بسیار سختگیر در برابر جمهوری اسلامی و تهدیدهای امنیتی منطقه است,
یاشار در نظرسنجی‌های اخیر به لیکود نتانیاهو نزدیک شده و حتی در برخی نظرسنجی‌ها جلو افتاده است.
رویترز آیزنکوت را یکی از جدی‌ترین رقبای نتانیاهو معرفی کرده و گزارش کرده که حزب او توان بالقوه تشکیل ائتلاف گسترده‌تری نسبت به لیکود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/21038" target="_blank">📅 10:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21034">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏مارک لوین به وعده خود عمل کرد و نظر سنجی‌را  انتشار داد و گفت : ‏بر اساس یک نظرسنجی اخیر (۱۰ اوت) که توسط تنها نظرسنجی‌کننده‌ای انجام شده که دو دوره انتخاباتی اخیر را درست پیش‌بینی کرده بود، حزب لیکود نتانیاهو پیش‌بینی می‌شود ۳۳ کرسی در کنست به دست آورد و…</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/21034" target="_blank">📅 10:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21032">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw6Tu--gqCQwkgr0Baln2JG_3TuwbjOxX66HsbWsE_a2t2IKD5j25UKWoUx64G8D2F1Op2IvJ92BsXk2ll_W9ormd_p7y7QMO3-iuMFpubGOI07Qs-BPnyKBk4bK5-HkxUxwiXBJwgobArUM9mNGWr9GMc9A8erA7Fo1wfziOwlm0UpDi-IpoV0j811sZncQ9SXWp9yMOMnOgng8OrRNwBBalAsM8kd6XCnVmpWaZfNb50VIPmg4523Bo7V7k7HOzGUaTDOXGGvxy3LAmin241beU5fAI_GRjWy6eZIvUcPz7F7FajWfmYfpI93rdDogm3NbvYmuEfsDkda6FO5QSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : من قویاً معتقدم که پرزیدنت ترامپ باید از نتانیاهو حمایت کند، چون در مقطعی برای ادامه مقابله با ایران به او نیاز خواهد داشت. به احتمال زیاد، نتانیاهو در هر صورت پیروز خواهد شد. اما بر اساس اطلاعات منابع من، در دیدار آنها هیچ توطئه یا زدوبندی در…</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/21032" target="_blank">📅 09:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مانوک : رژیم پاشیده
@WarRoom</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/21031" target="_blank">📅 09:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21030">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b22325bf.mp4?token=p3CGXKs__OUFRGQOsHygiPbJjD56sMxtdbp0I8Tt6-FHQBjp-Xq4cH-7fjDs5SbRa9R2RCK7Rl2ilv22nKfLGMmazQDxYrP2eHUT8HzuFvCunpxs8LDkKJjRu4CT0ED4uDkqUYxcFdD_WqCkYiYdYDnmtbjZx5yJ1dLiWlM2a_rsyFWdZjSOucb9X-7UVBSBVLjm3g0Bfr41MsZ9Zw-NpK2yGD6SPcStZ3lLEivkNcxIjCNtuS0-cKVIiMB2CWtsj4teCP3x8qJvgh_7zs6fKuGp5jJeFxED_9n11SE_KytTDNbttUjharHoWWz_pOeE72vNKPixea1LZ-Q-BorQKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b22325bf.mp4?token=p3CGXKs__OUFRGQOsHygiPbJjD56sMxtdbp0I8Tt6-FHQBjp-Xq4cH-7fjDs5SbRa9R2RCK7Rl2ilv22nKfLGMmazQDxYrP2eHUT8HzuFvCunpxs8LDkKJjRu4CT0ED4uDkqUYxcFdD_WqCkYiYdYDnmtbjZx5yJ1dLiWlM2a_rsyFWdZjSOucb9X-7UVBSBVLjm3g0Bfr41MsZ9Zw-NpK2yGD6SPcStZ3lLEivkNcxIjCNtuS0-cKVIiMB2CWtsj4teCP3x8qJvgh_7zs6fKuGp5jJeFxED_9n11SE_KytTDNbttUjharHoWWz_pOeE72vNKPixea1LZ-Q-BorQKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز با دسترسی نادر به یک پایگاه ارتش اسرائیل، مجموعه بزرگی از سلاح‌های ضبط‌شده از حماس و حزب‌الله را به نمایش گذاشته است؛ مجموعه‌ای شامل راکت، پهپاد، خمپاره، موشک ضدزره، تفنگ تک‌تیرانداز و مسلسل. به گفته اسرائیل، بخشی از این تسلیحات ساخت ایران است و سلاح‌هایی از روسیه و چین نیز در میان آنها دیده می‌شود؛ حتی یک مسلسل آلمان نازی
MG34 مربوط به جنگ جهانی دوم
نیز در این انبار وجود دارد. این مجموعه تصویری از گستردگی و تنوع تسلیحاتی را نشان می‌دهد که اسرائیل می‌گوید از گروه‌های مورد حمایت ایران از زمان ۷ اکتبر کشف و ضبط کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/21030" target="_blank">📅 09:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبرگزاری قوه قضائیه : شهرام صادقی که در ۱۸ دی ماه پس از حمله به مامورین با خودروی پراید ۷ مامور را زیر گرفت به اتهام اقدام عملیاتی به نفع اسرائیل و آمریکا، بعد از اذان صبح امروز، حکم وی اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/21029" target="_blank">📅 08:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21027">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سنتکام :
فرمانده سنتکام پس از سفری ۱۰ روزه به خاورمیانه بازگشت.
دریادار
برد کوپر
در این سفر به
بحرین، عراق، اسرائیل، اردن، عربستان سعودی و امارات
رفت و با مقام‌های ارشد سیاسی و نظامی این کشورها دیدار کرد و همچنین از نیروهای آمریکایی مستقر در منطقه بازدید داشت؛ سنتکام می‌گوید بیش از
۵۰ هزار نیروی آمریکایی
در خاورمیانه مشغول مأموریت هستند. کوپر در جریان سفر خود همچنین برای دومین بار در سال جاری از ناو هواپیمابر
USS Abraham Lincoln
در دریای عرب بازدید کرد. سنتکام اعلام کرده این ناوگروه تاکنون
هزاران پرواز رزمی
در پشتیبانی از عملیات «Epic Fury»، مأموریت‌های امنیت منطقه‌ای و
محاصره دریایی آمریکا علیه ایران
انجام داده است. کوپر درباره استقرار آبراهام لینکلن گفت این مأموریت از نظر شدت و پیامدهای عملیاتی، یکی از مهم‌ترین مأموریت‌های دوران مدرن بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/21027" target="_blank">📅 07:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21026">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عراقچی می‌گوید اساساً چیزی به نام
«آتش‌بس ۶۰روزه برای تمدید
بعد از نقض آن توسط آمریکا
وجود ندارد»
و تفاهم اسلام‌آباد از نگاه ایران
پایان جنگ بوده، نه آتش‌بس ۶۰روزه
. با این حال، اگر مبنا را همان دوره ۶۰روزه و پایان آن در
۱۷ اوت
بگیریم، با فرض ساعت ۰۰:۰۰ واشنگتن، موعد پایان آن در ایران
ساعت ۷:۳۰ صبح ؛ یکشنبه
(اگر مبنا آغاز روز) و
دوشنبه ۲۶ مرداد
(اگر مبنا پایان روز) باشد پایان میابد
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21026" target="_blank">📅 23:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21025">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قطر ادعای ایران دربارهٔ به اسارت گرفته شدن سه خلبان ایرانی توسط این کشور را قاطعانه تکذیب کرد
و گفت تهران تاکنون به دعوت دوحه برای اعزام هیئتی به قطر و بررسی جزئیات عملیات جست‌وجو و نجات پاسخ نداده است.
سوخو-۲۴ ایران روز ۱۱ اسفند ۱۴۰۴ برای انجام مأموریتی علیه یک پایگاه نظامی در قطر اعزام شدند و هنگام بازگشت هدف پدافند قرار گرفتند.
بر اساس روایت ایران، چهار خلبان این دو جنگنده اجکت کردند که یکی از آن‌ها، مجید کاظمی، کشته شد و سه نفر دیگر به نام‌های جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان «زنده توسط نیروهای قطری به اسارت گرفته شدند».
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21025" target="_blank">📅 22:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21024">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دیدبان اتاق جنگ : سیریک هرشب قبل اینکه بزنن یک ساعت برق قطع میکنن بعد که وصل کردن شروع میکنن شلیک
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21024" target="_blank">📅 22:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21023">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش صدای ۳ انفجار/شلیک در‌ سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21023" target="_blank">📅 22:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21022">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏دونالد ترامپ در تروث‌سوشال ویدیویی را منتشر کرد که در آن بهنام طالب‌لو، مدیر ارشد برنامه ایران در بنیاد دفاع از دموکراسی‌ها، بر تاثیر محاصره دریایی آمریکا در کاهش صادرات نفت ایران تاکید کرده و می‌گوید محدود کردن حکومت ایران از نظر بودجه‌ای پس از پایان درگیری‌ها، در کنار محاصره، به آمریکا اجازه می‌دهد از دلار به‌عنوان یک سلاح استفاده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21022" target="_blank">📅 22:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21021">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21021" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21020">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اندی بیکر، یکی از نزدیک‌ترین چهره‌های امنیتی به جی‌دی ونس، در هفته‌های آینده کاخ سفید را ترک می‌کند.
بیکر که سال‌ها مشاور امنیت ملی ونس بوده و در دولت ترامپ نیز در تصمیم‌گیری‌های مهم سیاست خارجی و امنیت ملی نقش داشته،
مستقیماً در مذاکرات آمریکا و ایران حضور داشت
و به جناح مخالف جنگ شناخته می‌شد.  خروج او در حالی رخ می‌دهد که جنگ ایران همچنان موضوعی حساس است؛ هرچند دلیل رسمی برای رفتنش، تمایل به وقت بیشتر با خانواده و سرمایه گزاری های شخصی عنوان شده ، همچنین
در مورد شایعه افشای اطلاعات محرمانه نیز اتهام مستندی علیه بیکر منتشر نشده، اما با توجه به دسترسی او به پرونده‌های حساس و نقش مستقیمش در مذاکرات، این گمانه‌زنی درباره علت واقعی خروجش مطرح شده است
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21020" target="_blank">📅 19:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21019">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مارک لوین : من قویاً معتقدم که پرزیدنت ترامپ باید از نتانیاهو حمایت کند، چون در مقطعی برای ادامه مقابله با ایران به او نیاز خواهد داشت. به احتمال زیاد، نتانیاهو در هر صورت پیروز خواهد شد. اما بر اساس اطلاعات منابع من، در دیدار آنها هیچ توطئه یا زدوبندی در کار نبوده است. آکسیوس این گزارش‌های منفی را با هدف تأثیرگذاری بر سیاست‌گذاری و انتخابات اسرائیل، از دیدگاهی چپ‌گرایانه و افراطی، در زمان‌بندی خاصی منتشر می‌کند.
همچنین نتانیاهو بر اساس آخرین نظرسنجی‌ای که در انتخابات قبلی واقعاً نتیجه را درست پیش‌بینی کرده بود، وضعیت خوبی دارد. آن نظرسنجی را پیدا می‌کنم و جداگانه منتشر خواهم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21019" target="_blank">📅 19:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21018">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بیانیه دفتر نتانیاهو : امروز صبح، حزب‌الله توافق آتش‌بس در لبنان را نقض کرد، زمانی که به سربازان ما در منطقه امنیتی که از شهرک‌های اسرائیلی واقع در نزدیکی مرز محافظت می‌کند، حمله کرد. در این حمله، سه تن از سربازان ما به شدت مجروح شدند. ارتش اسرائیل با بمباران مقر فرماندهی حزب‌الله که دستور حمله را صادر کرده بود، پاسخ داد
…
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21018" target="_blank">📅 18:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21017">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">واشنگتن پست : هیچ توافق خوب و قابل‌قبولی با ایران نمی‌توان منعقد کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21017" target="_blank">📅 17:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21016">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اردوغان به شبکه الجزیره: اولویت ما بازگشایی تنگه هرمز است، زیرا ادامه بسته بودن آن به نفع هیچ‌کس نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21016" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21015">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ستاد کل نیروهای مسلح ایران اعلام کرده است سه خلبان ایرانی به نام‌های
جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان
که در جریان حملات اسفندماه جنگنده‌های سوخو-۲۴ آنها سقوط کرده، زنده مانده و حدود شش ماه است در
قطر به اسارت نیروهای قطری
درآمده‌اند. محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین، گفته این خلبانان هنگام بازگشت از یک مأموریت رزمی پس از هدف قرار گرفتن جنگنده‌ها توسط پدافند، اجکت کرده‌اند. او با استناد به کنوانسیون سوم ژنو خواستار دسترسی کمیته بین‌المللی صلیب سرخ به آنها شده و گفته قطر تاکنون اجازه تماس یا دیدار خلبانان با خانواده‌ها و مقام‌های ایرانی را نداده است.
قطر تاکنون به این ادعا واکنش رسمی نشان نداده است
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21015" target="_blank">📅 16:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21014">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8PDtk261_wBo-N8BXJMrk5zfKHN44-00yQvooYsIaS6rf1Wt5lZF0ulaeBkWOlvZ7Z9ED3BJNy9uWxtB2KFIGnxUspLgIRIKLB167Lod_mhK-XdcLxBbski49QHau0jeVEm_ESwsJueTLZX7DEtXCAZu1SAamuanOJy7vS2Xn5pauwWpqxATm_BU3I6bKV6v36PmkcZ0Ra8gH3UdJXhuxHCcNszrlYjQu8nf_RILb-DNoxz1OL1JCGov4hY7WLNuc9p9RoxeYtarDn-5eRm-CBQDZG-F9OCYTcefwJi6TgfUBuia3wXCJjosvK-0du1GzJSXkYU846GW1HPtg402w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : اندازه هواپیما هایی که ما در اتاق جنگ زیاد سروکار داریم
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21014" target="_blank">📅 15:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21013">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21013" target="_blank">📅 14:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21012">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرنگار الجزیره: ۳ حمله هوایی اسرائیل بامداد امروز، مناطق اطراف شهر النبطیه الفوقا و حومه شهر انصار در منطقه النبطیه را هدف قرار داد. @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21012" target="_blank">📅 12:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21011">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9z0PABk-c1gU00MtGPtQRfDlcSJxiwhuip_-ldsXDuUrumqDsbonk7DFDvEAGalmyKQtkmNC4t65LaTdw9JQ3UloOfMRUyVJTJjBS5lvVoNSry3YntV5KSKsSstHX6rzeb2XceigEDqiPiGtofl6t_s8qMLynIm1pt8by6F31sN5J79S78R7vdirBIWKj1G8D3zBa_-TBSGlfJr_W_Wfqp5X4VtLVH7I3T1unFLG5bpl6ksSS0EWpMeGkYymS81m3vWWtXRWMEL3o4l0vp8ogAnLUSA9VJczHwH2ftozdXvBJDmp--Qv0N43oW5l4t4SAPITWmKyVVZf2SA1E64WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیوار فولادی، محاصره
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21011" target="_blank">📅 11:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21010">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaaScqPw8BQZZqZIMxhKO0Mty_RpAgzNItD9ClFLbD5Zd1UfzG1U53Pap6h_ruzVbYNZ6_MdkHo1TuN1_Dk73LbkgUgtP5VP31Bw0Ceqbd7R5YKWZTAqwI69QSWsk-1upStkDcdDWBjhl9x2F7f91CH1fLo-nglema0QgcgUFhNCFKFtM6ecvNxYXxqirVlzWSvf5BguJe6Lsf-q45zbbuP2UZ82cjkxn8VvAE1-q6EbvNCr8wLCOyj2s6XCrWZZmZYWaKG1olrBZh29t_1xacxkxBr9AH_Z5fiBgoKPqgKBlba__BU4KvEL981cOrbFjiSSzH61aVjX11PSeLQ2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ : تصاویر ماهواره‌ای منتشر شده توسط رویترز: دو لکه نفتی در نزدیکی جزایر قشم و سیری ایران در خلیج فارس مشاهده شد، در حالی که حملات مکرر به کشتی‌ها در این منطقه ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21010" target="_blank">📅 11:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21009">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مستند دیدنی
«جاسوس ۲»
از کانال ۱۴ اسرائیل ، که در آن با مأموران سپاه مصاحبه میشود !
با زیرنویس فارسی
، پیش تر قسمت اول را برای شما قرار داده بودم… از دست ندید…
🌐
@WarRoom
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21009" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21008">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNBVYZihIQwn14INMnbnUWrsvjwgOirygBHQJQOOQZzL2tym1KDc9s-g4UHxximliRhrDXg7wI1jPr7KHDwezWLLJwZwqkjj4TjcRDrDXVcLhTukJBVI0EkkMQqoaFh-XsjXe6oYBKEEuskXAhtd8DXqIER_OnSHvmJq1V47vKSLyurEZ1IDBIO6dwI_RRoNcoklMI4vnlAErw8HDU8NQrdLm9RFV2E6NZLP_Dd3VZlMSH9EYZLYs7MqPUnwp_VALU12KSHn_Mjci8VYQHcw5-uZXWkaZQ7-Rl-2SWCyDwDDYNcXplIlTPq_3gm2Fp3uTmA918heT-p5sqX-AzYA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : خط جدید ترابری لاجستیکی نظامی آمریکا و کد عملیات «مووسی MOOSE» نشان میدهد در جنگ بعدی پایان دهنده کار، آمریکا بر روی پایگاه خود در قاهره حسابی ویژه ای باز کرده و مرکز پشتیبانی عملیات خواهد بود هم نزدیکی به منطقه هم فاصله دورتری نسبت به کشورهای حاشیه خلیج فارس…
سفر قاهره تازه شروع شده…
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21008" target="_blank">📅 10:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21007">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرنگار الجزیره: ۳ حمله هوایی اسرائیل بامداد امروز، مناطق اطراف شهر النبطیه الفوقا و حومه شهر انصار در منطقه النبطیه را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21007" target="_blank">📅 10:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21006">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhGXHDmYC2q2ITvd8pRiLEBBgmL0dXiIMgty6y2r5P-YXVH3_0YMCRSRgyWH6UIlD5fDm5-5goioOvXldeS0ihmISHeuEW0K3unBN6Y20Vlkmt0vkUeXps-BF77QyL6YIbqCSiuocsTkJscQRg1uEjljxgTku4dZzhtyaZX-VWTNCbiFmzU8L93u6RZQNiEoLrfS_K9peW7ddQd6Bw5f75JiVcwiLQTE9Qzum3DaO4aPSf0ohiSskbXWRzTRYsA8p_q-S4QeIrvYMFixxteu0DFgZl3FylwK7t8cbYPWeuwEEPuseNww6Zzyp2yu0rBL4IHUHC_l9FJAaIM2sp8eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏UKMTO گزارش تأیید شده‌ای مبنی بر برخورد یک پرتابه ناشناخته به بدنه یک کشتی فله‌بر دریافت کرده است. خدمه در سلامت گزارش شده‌اند، هیچ ارزیابی خسارتی گزارش نشده است و در حال حاضر تأثیر زیست‌محیطی آن مشخص نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21006" target="_blank">📅 09:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21005">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ادعای نیویورک‌تایمز: مشکل تأمین و تدارکات ناو آبراهام لینکلن پس از آن آغاز شد که ایران، به پایگاه نیروی دریایی آمریکا در بحرین آسیب شدیدی وارد کرد و یک مرکز لجستیکی مهم را از کار انداخت
سپس پنتاگون مرکز تأمین و پشتیبانی منطقه‌ای خود را به دیه‌گو گارسیا منتقل کرد که ۳۵۴۰ کیلومتر از ناو‌های آمریکایی فعال در دریای عمان، فاصله دارد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21005" target="_blank">📅 09:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21004">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYJPLY2_8JqnId7GHQYu0B5DZYGrt370Q2Muqf5LOJjZyRKhskIGp7Y2q1LiTHR6DDlIQVzJvNIKlVTjpaZsb6HsbHZ52gF4nPGhyPMRuhoUIJKbZm5wDK5fA9taTIflkwXAXcqEKIRCM8_NslEdYfpr5NRLcTmCmq6h2GY6_MKW146C13krdv6JxVadXt9W9akTdTPIBsBox6OG7oLHau_wqFz2kj-z4eVPGrjvfrE9LRp0KmTaFX-mGKC07g-BehrnMeSB8bNRN8H1VMGe2NjR4PMIHbHjOvQy1mB-4knQcCqgoLjQb25tW-MpRF8F42MvNL7n_WXa701B1r2ScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز : آقای معاون رئیس‌جمهور، یک لحظه به توافق نزدیک هستیم، لحظه بعد می‌گوییم قرار است حسابی آنها را بمباران کنیم. یک لحظه تنگه هرمز باز است، لحظه بعد بسته است. مطمئنم این نگرانی و سرخوردگی داخل کاخ سفید هم وجود دارد. می‌دانم پیش‌بینی کردن دشوار است،…</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21004" target="_blank">📅 03:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21003">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ در مورد ایران: به زودی تنگه هرمز را جزو قلمرو ایالات متحده اعلام خواهم کرد.  ایران به شدت شکست خورده است. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21003" target="_blank">📅 03:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21002">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH1LRbA3vEvy2XK82WKqv-6WTvR4KHXSLQI7le2uwQiUFLpAJMdKIPBlDHnBb3P7zUZ2TWDsVk1wavyG-JJPScRoef79uODNmMbuRjeWWaE_rcCQnG_pbQCT9nW5mpEl_Q561WR_Y7qJpTjwqDx2qI7psnJ7Oc7ccyLEJ3RZBEZjVUcqWe23J5kYBWvMQDgaxTkt-Z-8ZFoFKDgOvwvvXWaw8s1Hx6twtm_hRQQ2E9IgBepd0lqT_CogIoTbK0KYWCx3qSR37468r-o_Xv-a5pM_SCFgfLDpTM59jIuDoBO0xr-RsFqKmB1q3Ty7fk9QePc24HEKSluFwYcPkSmvjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار هواپیمای C130 سوپر هرکولس از آمریکا به انگلستان و یک C5Mسوپر گالاکسی، یک راست از آمریکا به خاورمیانه میآیند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21002" target="_blank">📅 02:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21001">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وقوع زمین‌لرزه ۷.۴ ریشتری در اندونزی!
دو زمین‌لرزه جدید با قدرت های ۶.۱ و ۶.۶ ریشتر نیز دقایقی بعد رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21001" target="_blank">📅 02:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21000">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvxmYFqsbKchMVCvP8jytaoSoDKker2bi2ChvkI64TeXKvm6rpkugOF4Dwzwm8lccW-ckXVUp3xXWVyEcDkV7koodTXEspLFjTT5yTvs9LouM2m8vHKb4vlbXVgpm3hmTy4w3j7g7sUmRpSIKxn92prfez9J6zzsgwVLQy1j_ecxFQG3d3XjALeYc1crOxW0jm8a9GEmhnOKE07vHa6fc8DV6XS0VV0mC_GtEOszOKNa44hLBfUJU4Z8x7tFQn8zfXlUjHr8MVAmOrUz0LGCS5FFjsTMlWFteQXjMMNws0ZJxozrgPdmuAADcPU6gsqvGMgGfO_eLgT3Bzp-o23dig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام E3B-Sentry با رادار AWACS هم راه با ۴ سوخترسان هم اکنون در منطقه خلیج فارس انجام مأموریت میکنند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21000" target="_blank">📅 01:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20999">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">@WarRoom
مسیر من</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20999" target="_blank">📅 01:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20998">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from………..</strong></div>
<div class="tg-text">درود یاشار
شما بیشتر خرف های جاوید نام روح الله زم رو بیشتر قبول دارین یا استاد مانوک خدایخشیان؟
ممنون میشم جواب بدی</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20998" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20997">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">@WarRoom
مسیر ما</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20997" target="_blank">📅 01:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20996">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">@WarRoom
مقدمه</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20996" target="_blank">📅 00:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20995">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ: تمام کشورهای منطقه در شرایطی شبیه به محاصره قرار دارند، زیرا ایران به عنوان یک کشور زورگو در خاورمیانه شناخته می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20995" target="_blank">📅 00:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20994">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=Ofbpbh_O49I86p8a30_cZkmIIQ_VAeO0kt-plpxTumKL6KkqUgmPyJGCUvSt2Xif67WbpzQRtwtuiTL64FW_Dk4xtuAcJMMLCeqyDYDH4cLu1TDiWrLbziP5tKBuXUZPtcOBy4nR_xv8_dShhk2J-bcg9Kfyj0XdnaZDgFPhb8OtAr1SoT_CsIPYdeJv6gMU1uTjftgVqcMpnzXzLnx45f9rrO3m_Y84aTDTKm7KH_detR3KtXiR_jU9qgiqVF3bjt0ihckA0Oi4RUZrLDgGfmYk1-pvyahTD2UNATkIFtuzkQ80CzNiIpSec2UxyXKroQOwxEC6-LRBLeUCAYMZ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=Ofbpbh_O49I86p8a30_cZkmIIQ_VAeO0kt-plpxTumKL6KkqUgmPyJGCUvSt2Xif67WbpzQRtwtuiTL64FW_Dk4xtuAcJMMLCeqyDYDH4cLu1TDiWrLbziP5tKBuXUZPtcOBy4nR_xv8_dShhk2J-bcg9Kfyj0XdnaZDgFPhb8OtAr1SoT_CsIPYdeJv6gMU1uTjftgVqcMpnzXzLnx45f9rrO3m_Y84aTDTKm7KH_detR3KtXiR_jU9qgiqVF3bjt0ihckA0Oi4RUZrLDgGfmYk1-pvyahTD2UNATkIFtuzkQ80CzNiIpSec2UxyXKroQOwxEC6-LRBLeUCAYMZ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20994" target="_blank">📅 00:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20993">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ4R9a6AkVAXaofXe86McPR-tX9QZEr1WcupmIormq7TZRQ0pmZedCJTSD0hl6MCQ2z-LaAn0CRyuJ675tQu0N_ezH0eS3mAC8bTriMCb4EYJo8jZFJRWCxxiY70v8buospQFJBJ70dltLoDXv1A751Cm_uHvDIDMhSvMxxqhy472K0lDcdY7_qBj8g-90_5a0R9HvpAquWQ8HAJuMfMWf8coOg9LESURDteuUbWXzGTAgfjvnbVykqhqPtUjJXEaTI2sG1pFSLwQYE5SgQ8U5gK5zGTThwzvzMDxLapj3zoaeoMJP9H4NeJEizGbrOX7bGAvKcQgh9vDnAqiQz3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست در اتاق جنگ  در حال شنیدن گزارش نیروهای مستقر در خط مقدم فرماندهی مرکزی آمریکا (سنتکام) در حوزه‌های هوایی، زمینی و دریایی، از جمله ناو هواپیمابر
USS Abraham Lincoln
، هستم.آمریکایی‌های شگفت‌انگیزی که در حال انجام یک مأموریت تاریخی هستند.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20993" target="_blank">📅 00:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20992">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e4825bc3.mp4?token=vBXEMCLyXK49lBzUTJZvZeAF0jbt4Wvt3M-OIrZUnBealCDC1Xw4jA_cZf5ypalyQmEYTLrKyPEUPrboOJoRFjfFIxT0lRxhQvb8zsUsvk806TxFmVNjbNMQNWdxR-3SP6PHb18cIVt6ew4JQJCHam7repwMDGZWqdkL6Xem1L_0yiNxtyXbPKvL81ftRi_RT9QLzGCxBdYOaefFYyDAKdzklKVZGjOOy7VtTw5zFFk5KMmdei9aq4aABXv8SAhcr7zvI7sRcsX4uDypmbFaRmEc4S0t2xocJmf31auVYLCVMrJsvCY1s4dxEu81HTj6zh7U0d79AsFwg0eTft0YuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e4825bc3.mp4?token=vBXEMCLyXK49lBzUTJZvZeAF0jbt4Wvt3M-OIrZUnBealCDC1Xw4jA_cZf5ypalyQmEYTLrKyPEUPrboOJoRFjfFIxT0lRxhQvb8zsUsvk806TxFmVNjbNMQNWdxR-3SP6PHb18cIVt6ew4JQJCHam7repwMDGZWqdkL6Xem1L_0yiNxtyXbPKvL81ftRi_RT9QLzGCxBdYOaefFYyDAKdzklKVZGjOOy7VtTw5zFFk5KMmdei9aq4aABXv8SAhcr7zvI7sRcsX4uDypmbFaRmEc4S0t2xocJmf31auVYLCVMrJsvCY1s4dxEu81HTj6zh7U0d79AsFwg0eTft0YuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما قادر به نابودی کل کشور هستیم. ما نمی‌خواهیم این کار را انجام دهیم.
ما تحریم‌های اقتصادی علیه آنها داریم که هیچ کس قبلاً نداشته است.
اگر آنها حمله کنند، ما ۱۰۰ برابر سخت‌تر پاسخ خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20992" target="_blank">📅 00:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20991">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: ایران همچنان موشک‌هایی دارد، اما این بخش کوچکی از موشک‌هایی است که قبلاً در اختیارش بود.
تولید موشک‌ها در ایران 82 درصد کاهش یافته و توانایی‌های تولیدی آن‌ها تا حد زیادی از بین رفته است.
نرخ تورم در ایران به 350 درصد رسیده و ارزش پول آنها هیچ است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20991" target="_blank">📅 00:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20990">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ: آن‌ها رهبری ندارند. ما رده‌های اول، دوم و سوم آن‌ها را از بین برده‌ایم. این یکی از مشکلات من است، زیرا کسی وجود ندارد که بتوان با او مذاکره کرد.
ما رادارها و تمام تجهیزات اطلاعاتی پیشرفته و مدرن ایران را نابود کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20990" target="_blank">📅 00:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20989">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها ۲۱۲ هواپیمای بسیار خوب داشتند که برخی از آنها به طرز درخشانی از طریق اوباما از ایالات متحده خریداری شده بودند.
همه هواپیماهای آنها از بین رفته‌اند.
یکی از مشکلات ایران این است که کسی برای مذاکره وجود ندارد. این یک مشکل است.
این تنها کشور در جهان است که هیچ کس نمی‌خواهد رئیس جمهور شود.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20989" target="_blank">📅 23:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20988">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: هیچ کس نمی‌داند که ما در ایران تا چه حد موفق بوده‌ایم.
می‌دانید چه کسی می‌داند که ما در ایران تا چه حد موفق بوده‌ایم؟ خود ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20988" target="_blank">📅 23:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20987">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ : به همکارانم گفتم: «ما باید سفری به خاورمیانه داشته باشیم، زیرا باید از یک فاجعه بالقوه، یک آتش بسیار بزرگ که مثل آن را قبلاً ندیده‌اید، جلوگیری کنیم.»
وقتی مجبورید برای بنزین خود کمی بیشتر هزینه کنید، من هرگز عذرخواهی نخواهم کرد. من کار درستی انجام دادم.
یک کشور بسیار بد، نباید سلاح هسته‌ای داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20987" target="_blank">📅 23:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20986">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ درباره ایران:
جنگ با ایران، خدمت بزرگی به جهان است و ما کار فوق‌العاده‌ای انجام می‌دهیم.
من هرگز عذرخواهی نخواهم کرد، من کار درستی انجام میدهم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20986" target="_blank">📅 23:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20985">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: اگر ایران به ما حمله کند، ما با صد برابر قدرت بیشتر پاسخ خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20985" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20984">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: ما نمی‌توانیم اجازه دهیم که ایران به مسیر فعلی خود ادامه دهد. اگر ما آن‌ها را با بمب‌افکن‌های B-2 مورد حمله قرار نمی‌دادیم، آن‌ها سلاح هسته‌ای به دست می‌آوردند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20984" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20983">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ درباره ایران: من هرگز عذرخواهی نخواهم کرد، من کار درستی انجام دادم.
ایران، بدترین حامی تروریسم در جهان است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20983" target="_blank">📅 23:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20982">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ در مورد ایران: آمریکا قرار است زین پس هزینه بسیار کمی برای بنزین بپردازد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20982" target="_blank">📅 23:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20981">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ درباره ایران: محاصره اقتصادی، دیواری فولادی است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20981" target="_blank">📅 23:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20980">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb3349271.mp4?token=wBljB5Z_wazM3dKElYZDzEpB2qRwiI9fYBqQY8hi8rXKz687vP0axbV-mEiOK7UlXO1uy7sf_QciG70os8e7sV1IsV6FlPxiEWO2414nu0tm0axiHlyKUu5F3D4Cy8TMVSwMoLjdowin_M17NmvL47M5LMJVI2b2jey-FV3tqYhC6dqBqWxwh-s2A2hgn6WQsAjHjDIBsDcOJTyNPpp7XwcZI8VzD1sv9719FGwsv7q0l0CxGqVgQniPpoVwV0MjyOH2AZ3ZFGkj3eQ1krsoVKJgUPQDUky9_zNn3BrYOwlC1Z5YdMimajCYho-NvdflOqVgNYRpy817I6xdE2e8ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb3349271.mp4?token=wBljB5Z_wazM3dKElYZDzEpB2qRwiI9fYBqQY8hi8rXKz687vP0axbV-mEiOK7UlXO1uy7sf_QciG70os8e7sV1IsV6FlPxiEWO2414nu0tm0axiHlyKUu5F3D4Cy8TMVSwMoLjdowin_M17NmvL47M5LMJVI2b2jey-FV3tqYhC6dqBqWxwh-s2A2hgn6WQsAjHjDIBsDcOJTyNPpp7XwcZI8VzD1sv9719FGwsv7q0l0CxGqVgQniPpoVwV0MjyOH2AZ3ZFGkj3eQ1krsoVKJgUPQDUky9_zNn3BrYOwlC1Z5YdMimajCYho-NvdflOqVgNYRpy817I6xdE2e8ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: به زودی تنگه هرمز را جزو قلمرو ایالات متحده اعلام خواهم کرد.
ایران به شدت شکست خورده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20980" target="_blank">📅 23:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20979">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">لحظاتی پیش حمله هوایی اسرائیل به المنصوری در جنوب لبنان انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20979" target="_blank">📅 23:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20978">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کاخ سفید: به مجازات ایران و فلج کردن اقتصاد آن ادامه می‌دهیم. ابزارهای بیشتری برای اعمال فشار علیه ایران در اختیار داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20978" target="_blank">📅 22:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20977">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آنا کلی، معاون سخنگوی کاخ سفید، درباره ناو هواپیمابر لینکلن:
رئیس جمهور ترامپ بیش از هر کسی به سربازان اهمیت می‌دهد.
به یاد داشته باشید که جو بایدن تمرکز را از جنگجویان به سیاست‌های حمایت از نیروهای دفاعی تغییر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20977" target="_blank">📅 22:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20976">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">به گزارش کانال 13 اسرائیل، اسرائیل قصد داشته به مواضع ترکیه در سوریه حمله کند، اما ترامپ مداخله کرده و مانع آن حمله شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20976" target="_blank">📅 22:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20975">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ced329bda.mp4?token=VizXhZBtOF71cqOtthpOJgo9NXYCwSwUDI8k_yI0ouc6JZVuhoYzuwqzYgNEVAqQIe4Xb1PrE0yeAu25EiXFqar31ziAmLniSDlTLFWuR4awSpw3vkMa3wgxrmTJpWGc00YdXinFX5_0cD7W0hUC6ZD_jAjy33mzzpDSeTFzVkQnziuC7aug4F6DsdLztPXpyjK-YktmuKqrb4__4hAkd8bkZCGljrlYaA0Rosh3uBGCBlxZC4txA-GueglT3S1iWVww7o8Koc4w8KbTmYzQOzIVHi1mqLS19kbUudx86KwW-iW90D4HHe_X6GpJw93BeAFRAiJMuD7oKtqE8VjNKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ced329bda.mp4?token=VizXhZBtOF71cqOtthpOJgo9NXYCwSwUDI8k_yI0ouc6JZVuhoYzuwqzYgNEVAqQIe4Xb1PrE0yeAu25EiXFqar31ziAmLniSDlTLFWuR4awSpw3vkMa3wgxrmTJpWGc00YdXinFX5_0cD7W0hUC6ZD_jAjy33mzzpDSeTFzVkQnziuC7aug4F6DsdLztPXpyjK-YktmuKqrb4__4hAkd8bkZCGljrlYaA0Rosh3uBGCBlxZC4txA-GueglT3S1iWVww7o8Koc4w8KbTmYzQOzIVHi1mqLS19kbUudx86KwW-iW90D4HHe_X6GpJw93BeAFRAiJMuD7oKtqE8VjNKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های اسرائیلی با انتشار این ویدیو می‌گویند برخلاف تصور رایج، بخش زیادی از پرواز جنگنده‌های اسرائیلی بر فراز ایران نه پرتنش و پیچیده، بلکه شبیه یک پرواز عادی است. به ادعای آن‌ها، اطلاعات لحظه‌ای از موقعیت سامانه‌های پدافندی در اختیار خلبانان قرار می‌گیرد؛ تا جایی که این تصاویر از آسمان تهران، بیشتر به یک پرواز معمولی شباهت دارد تا مأموریتی در دل خاک دشمن
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20975" target="_blank">📅 21:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20974">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امشب تا صبح بیدارم
🙌🏾
روال هر هفته</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20974" target="_blank">📅 21:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20973">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سیریک گزارش صدای انفجار/پرتاب موشک/پهپاد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20973" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20972">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1310e64db.mp4?token=Tw25ezmLJULVju8LrWHy5dw6VsroJ56gSlMNq2U_DiysqGk_lXBPAz9BzJHk77zcnQkiMHaoKUjKU90Lm-0pdg3en1J7PTesNPKI5nXjnHot56RD-SxGuZnhC9FWAzQG86lrvlSqMAjioTeV4OpVGbWeJXVYCPQR9pwFyC4vnTcV7x9afn1UH--Jx5sels2MW9ySTsnozKp04OCKNoQIWWh4mJopWOw5Vt0-OE83MLJTP5jhH8C-WMb33tNsZayCqSf8NTcCYrefUPS0ibbAPR58UkycbxjLvJHCrx_fRh08MZk2NOUy2fUGNRVbBS9GWSSD8a780HvdeTSPhePw8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1310e64db.mp4?token=Tw25ezmLJULVju8LrWHy5dw6VsroJ56gSlMNq2U_DiysqGk_lXBPAz9BzJHk77zcnQkiMHaoKUjKU90Lm-0pdg3en1J7PTesNPKI5nXjnHot56RD-SxGuZnhC9FWAzQG86lrvlSqMAjioTeV4OpVGbWeJXVYCPQR9pwFyC4vnTcV7x9afn1UH--Jx5sels2MW9ySTsnozKp04OCKNoQIWWh4mJopWOw5Vt0-OE83MLJTP5jhH8C-WMb33tNsZayCqSf8NTcCYrefUPS0ibbAPR58UkycbxjLvJHCrx_fRh08MZk2NOUy2fUGNRVbBS9GWSSD8a780HvdeTSPhePw8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : این کشتی با یک کشتی یکسان (جرج واشنگتن) جایگزین میشود
خبرنگار: خانواده‌های نظامیان نگرانند از شرایط ناو لینکلن
ترامپ : «نه، آن‌ها نگران نیستند.»
خبرنگار: آیا این استقرار نظامی بیش از حد طولانی شده است؟
ترامپ: «نه، نه، نه؛ حتی نزدیک به آن هم نیست که بگوییم بیش از حد طولانی شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20972" target="_blank">📅 21:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20971">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfefd33ebd.mp4?token=HV8LgVk92WtgeL8iQKSt00VNiVI0gzc8mlarFoWdd6bU6XSB0jLmIEfzz3LFKQCbSTsrxuRolvZQ2V6R2qxmwagJKjKMk1or2Uj7behNza9UpZ_rbRq1e5MsiAWrnnpxXwXdavqEMUFnVnmPDWYzukDE1cwdc1tEolgdEqefLoLMQyxgu6sTjSuK9Hyzl5AMRhji3BpapAWmg7GaCrved5bYDsorEcsFt7an_kk2KdgSK6DGuhN8Q4tKTmMo5dz5ri9X9b9Ac3ZVsaExetDef20c9D8ud-Z_Ihz0MDCzGeTMBiE22P8gnQZIMAfJpv2a8ZII6oaeTvd2os1YXa74sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfefd33ebd.mp4?token=HV8LgVk92WtgeL8iQKSt00VNiVI0gzc8mlarFoWdd6bU6XSB0jLmIEfzz3LFKQCbSTsrxuRolvZQ2V6R2qxmwagJKjKMk1or2Uj7behNza9UpZ_rbRq1e5MsiAWrnnpxXwXdavqEMUFnVnmPDWYzukDE1cwdc1tEolgdEqefLoLMQyxgu6sTjSuK9Hyzl5AMRhji3BpapAWmg7GaCrved5bYDsorEcsFt7an_kk2KdgSK6DGuhN8Q4tKTmMo5dz5ri9X9b9Ac3ZVsaExetDef20c9D8ud-Z_Ihz0MDCzGeTMBiE22P8gnQZIMAfJpv2a8ZII6oaeTvd2os1YXa74sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم : دود مشاهده شده تو جنوب تهران مربوط به آتش زدن ضایعات پلاستیکیه ( عمو پلاستیکیاهو )
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20971" target="_blank">📅 21:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20970">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">داعش شروع به تهدید علیه اسپانیا کرد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20970" target="_blank">📅 20:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20969">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dd6977b1.mp4?token=N--94gfdHZ_K0vya5NrijoSEb3m9oCHHxEryh8BSehZiBWTpnF98PPrN88UwcZ_bL5d4xr7e_jkfg3RUzW2V8yI5NaEh1x56ORqk_TDOt9L9U58qPYzD753LSLXdrGMeWBu-CwK4yeEFdJPHd9PkMjqk-EbtnuKkP6rt1nfkMdz4OOC6PWIE4V6yV2tlSfoVKRoh-dAUn1epaq5iaIlfKj9jqMCoNjruYDuZyOEpa9299Oncrvzbe2BovRNa436Gk7RAIIPWZPqcQWJ-g2gWFh-1GqOzSFJkwv9bPePFESQMiPwf_3HNYNl_ScJabgsBeHrEtyrum1LKnAkIP72cvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dd6977b1.mp4?token=N--94gfdHZ_K0vya5NrijoSEb3m9oCHHxEryh8BSehZiBWTpnF98PPrN88UwcZ_bL5d4xr7e_jkfg3RUzW2V8yI5NaEh1x56ORqk_TDOt9L9U58qPYzD753LSLXdrGMeWBu-CwK4yeEFdJPHd9PkMjqk-EbtnuKkP6rt1nfkMdz4OOC6PWIE4V6yV2tlSfoVKRoh-dAUn1epaq5iaIlfKj9jqMCoNjruYDuZyOEpa9299Oncrvzbe2BovRNa436Gk7RAIIPWZPqcQWJ-g2gWFh-1GqOzSFJkwv9bPePFESQMiPwf_3HNYNl_ScJabgsBeHrEtyrum1LKnAkIP72cvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزمکس: وقتی یک دموکرات می‌گوید «ایران هیچ‌وقت قوی‌تر از این نبوده»، واکنش شما چیست؟
وزیر خزانه‌داری بسنت: آنها بی‌اطلاع، دیوانه و فاقد هرگونه درک از چیزی هستند که درباره آن صحبت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20969" target="_blank">📅 17:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20968">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">واشنگتن‌پست: ترامپ حتی در برابر کنگره نیز دست بالا را دارد
واشنگتن‌پست در تحلیلی می‌نویسد قدرت رئیس‌جمهور آمریکا در تصمیم‌گیری درباره جنگ، طی دهه‌ها افزایش یافته و کنگره عملاً ابزار محدودی برای متوقف کردن رئیس‌جمهور دارد. حتی اگر در آینده هر دو مجلس کنگره علیه جنگ رأی دهند، رئیس‌جمهور می‌تواند در برابر چنین تصمیم‌هایی مقاومت کند و در صورت تبدیل شدن آن به قانون، از
حق وتو
استفاده کند؛ وتویی که تنها با رأی دوسوم هر دو مجلس قابل لغو است.
این تحلیل در عمل نشان می‌دهد که
نتیجه انتخابات میان‌دوره‌ای به‌تنهایی لزوماً اختیار ترامپ برای ادامه یا پایان دادن به جنگ را از بین نمی‌برد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20968" target="_blank">📅 16:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20967">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزارت جنگ ایالات متحده با شرکت‌های "بوئینگ" و "آر‌تی‌اکس" قرارداد بست تا تولید قطعات یدکی موشک‌های SM-3 را افزایش دهد.
این موشک‌ها برای رهگیری موشک‌های بالیستیک در خارج از جو زمین طراحی شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20967" target="_blank">📅 16:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20966">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoZxyJdV7LLCILDtl28MQ1oCVhxuJWOgPXKOYkHiL_2VmX6_RKWFbZ0L3BNVpceqy2WVDduZXqO3FBmnyB0efrlSkg8W9S4CvGXb3dpksSgS98xoftVvz7JZ9iy4A7oc7BiY4VQCfcbFMmdbZ6xCrNNTb6OEItjucg7sYJgYzW-WW1GIHU9Ta6EUehr0p0yv7QC92Ss8EOrfcCCSI-CPpaM4qzNPnCxPEiD3M_FOqytvSmWsq_mSr2-ZdVTHDko_aFPUjck3fERVGby705v91hcBfylkT5zBNSM5_L3-d6m5_iTJACXnyS9-QEPGj6ox_BGuGNYBzv1U9d4H6eKTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ در تروث :
نیوزمکس : ایالات متحده با انزوای اقتصادی بی‌سابقه‌ای به ایران ضربه خواهد زد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20966" target="_blank">📅 15:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20965">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادعای وال‌استریت‌ژورنال:
ایران و عمان در حال نهایی کردن پیش‌نویس توافقی برای بازگشایی تنگه هرمز بودند که به تهران اجازه نظارت بر کشتی‌هایی که وارد خلیج فارس می‌شوند را می‌دهد، اما اجازه نمی‌دهد عوارض یا هزینه‌های خدمات دریافت کند.
طرفین در مورد نکات اصلی پیش‌نویس که یک خط ورودی در نزدیکی ایران و یک خط خروجی در نزدیکی عمان ایجاد می‌کند  توافق کرده‌اند و آن را با آمریکا، کشورهای منطقه و رهبران ارشد ایران به اشتراک گذاشته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20965" target="_blank">📅 15:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20964">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اکسیوس : به گفته دو نفری که اخیراً با ترامپ درباره نتانیاهو گفت‌وگو کرده‌اند، ترامپ گفته است: “بی‌بی بزرگ‌ترین دشمن خودش است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20964" target="_blank">📅 15:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20963">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اکسیوس : دونالد ترامپ با وجود درخواست‌های مکرر، هنوز از حمایت رسمی بنیامین نتانیاهو در آستانه انتخابات ۲۷ اکتبر اسرائیل خودداری کرده است. در حالی که نظرسنجی‌ها نشان می‌دهد ائتلاف نتانیاهو از اکثریت لازم برای تشکیل دولت فاصله دارد و رقبای او پیشتاز هستند، اختلافات واشنگتن و تل‌آویو بر سر ایران، غزه، لبنان و سیاست‌های منطقه‌ای افزایش یافته است. مقام‌های آمریکایی می‌گویند ترامپ از برخی تصمیم‌های نتانیاهو ناراضی است و ضعف او در نظرسنجی‌ها نیز تمایل رئیس‌جمهور آمریکا برای ورود به رقابت انتخاباتی اسرائیل را کاهش داده است. با این حال، کاخ سفید همچنان امیدوار است دولت اسرائیل در اجرای طرح صلح غزه، مذاکرات منطقه‌ای و برنامه‌های آمریکا برای توافق احتمالی میان اسرائیل و عربستان همکاری کند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20963" target="_blank">📅 15:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20962">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e612920df0.mp4?token=qoDX25cHIk-3M4_uNKUXF3r_rTc7V-W3foiiJxWPfPTy8Eu2w271IH4FXK14_KXZDBkhOwdvcqtqJJ--ukv8Y_0jLu2cAt9paFlQl6pR8h70R1qvf4DmI7dKEJ6imsdnXF5oHmmfbFipslfoxCAjByadii1v4p1X4IsqK4tMuqFBr1H6fRu6mVzs4l9W0OWP5cTKKXt_VjjWYCmcVxGs412AXGZWCDZonRFy19GBXuqsSGe-uI-xdprFqMJtx985JcpLDucK4s5rEVEXNvYlePAwAQXqiFELyjqX-zkMGsqI4__uSwV0B29D2jM_qkKqXSD_e-bDuy6SIOJf5Pdk80sleaUEjpCfjSKb6YyUWTXBkPC-5YjLG8kMex8enb4MfvHquG_JteXnzF8P22tiPhPHEGg7l5C7PSo8Jc_H0Gd4a04znrnfDH63-stWWGExCP572631JU6r9Qym-YoDVqfzlBy7hWe08thIq5xCcjLY9bhsbuAvLqasUHwAjxRD4TEO7TQ7h8w0tcwteQy4EhlkKJoBe2v9umQslKLNi-p_T-CiLmN_f00cJoJ7-4WvysFdGph12JzxlX2nd2xEJFjHT8IL5ncvkZkkU3bP-tKv_zUTO3YKyyDF3j8bbDDgeC2ahciheb9HfuBSOo3vEo6OlbIoqu7WlSoFsRMtpd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e612920df0.mp4?token=qoDX25cHIk-3M4_uNKUXF3r_rTc7V-W3foiiJxWPfPTy8Eu2w271IH4FXK14_KXZDBkhOwdvcqtqJJ--ukv8Y_0jLu2cAt9paFlQl6pR8h70R1qvf4DmI7dKEJ6imsdnXF5oHmmfbFipslfoxCAjByadii1v4p1X4IsqK4tMuqFBr1H6fRu6mVzs4l9W0OWP5cTKKXt_VjjWYCmcVxGs412AXGZWCDZonRFy19GBXuqsSGe-uI-xdprFqMJtx985JcpLDucK4s5rEVEXNvYlePAwAQXqiFELyjqX-zkMGsqI4__uSwV0B29D2jM_qkKqXSD_e-bDuy6SIOJf5Pdk80sleaUEjpCfjSKb6YyUWTXBkPC-5YjLG8kMex8enb4MfvHquG_JteXnzF8P22tiPhPHEGg7l5C7PSo8Jc_H0Gd4a04znrnfDH63-stWWGExCP572631JU6r9Qym-YoDVqfzlBy7hWe08thIq5xCcjLY9bhsbuAvLqasUHwAjxRD4TEO7TQ7h8w0tcwteQy4EhlkKJoBe2v9umQslKLNi-p_T-CiLmN_f00cJoJ7-4WvysFdGph12JzxlX2nd2xEJFjHT8IL5ncvkZkkU3bP-tKv_zUTO3YKyyDF3j8bbDDgeC2ahciheb9HfuBSOo3vEo6OlbIoqu7WlSoFsRMtpd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیپلر
: ترافیک دریایی از تنگه هرمز در ۱۳ اوت افزایش یافت و ۱۳ عبور تایید شده ثبت شد که نشان‌دهنده رشد ۴۴ درصدی نسبت به روز قبل (۹ عبور) است. نه کشتی از طرح یک‌جانبه ایران استفاده کردند، هیچ عبوری در سیستم جداسازی ترافیک هرمز تایید نشد و چهار مسیر نامشخص باقی ماند.
فعالیت در باب‌المندب پایدارتر بود و ۲۹ عبور تایید شده ثبت شد که ۴ درصد بیشتر از ۲۸ عبور روز قبل است. هجده کشتی وارد دریای سرخ شدند و ۱۱ کشتی از آن خارج شدند، در حالی که دو عبور تاریک ثبت شد. در طول روز هیچ حمله جدید تایید شده‌ای به کشتی‌ها گزارش نشد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20962" target="_blank">📅 14:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20961">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f327dcc92.mp4?token=ULYej5E22qjn0zwDDnt0oj7goj7uv10omzEwU1clMBkTqJylgdilYtyPx2Pb-GyKuOtrSKdVpTLlUbxL7yfPcvwhL_2l9zzHTyw8ilxg0Dh7gIRpPB9_pusrlBfFwzt1Mtx18VO73wp3gp-r2bKrpZabTNqs_HKg7DI-qlQAbz3u0mw_WzqZ6hbmWL69OJhgfur3__zJ0jG_xDXqqSHPtDyDrL0cDRid7G7Yh7xmAnqwfYb-hz-RsmZlzKlv_aGWEOjbp5S1qGSH9OxHFy8C9wPoHvWdyyuqcEg6HuaQGyFOAdTgr3EufwB0m-zMXfiRifqNHptZKrTYf3thK8ixOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f327dcc92.mp4?token=ULYej5E22qjn0zwDDnt0oj7goj7uv10omzEwU1clMBkTqJylgdilYtyPx2Pb-GyKuOtrSKdVpTLlUbxL7yfPcvwhL_2l9zzHTyw8ilxg0Dh7gIRpPB9_pusrlBfFwzt1Mtx18VO73wp3gp-r2bKrpZabTNqs_HKg7DI-qlQAbz3u0mw_WzqZ6hbmWL69OJhgfur3__zJ0jG_xDXqqSHPtDyDrL0cDRid7G7Yh7xmAnqwfYb-hz-RsmZlzKlv_aGWEOjbp5S1qGSH9OxHFy8C9wPoHvWdyyuqcEg6HuaQGyFOAdTgr3EufwB0m-zMXfiRifqNHptZKrTYf3thK8ixOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش اسرائیل در حال انفجار ساختمان‌ها در منطقه روستای شیعه‌نشین مرکبا در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20961" target="_blank">📅 13:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20960">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">از امشب ۳ شب مست میکنم
😂
🙌🏾</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20960" target="_blank">📅 12:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20959">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZSvg_FzaNKC988gCJvPiWqFVW3VtgGMzqJeCgWhq_7uTZvsGAdpHwOyMnP8K3oAaJp6Jflt9w2nDZEavayqNolvnbHbUz-Fgy7VGohGSIOowf03UaJrm0G446M7i6eyv3hPqo66vxrowirBQWI9aAg8lTh4gTquny5UNA5f0f3ftX1cHcFzoiYFvnvZM_TZaC0x1BG5tLVMJTRSAkd_UhIoPy4O0A6XV8h8Khn0XsIxCMy9oLWsM10lqRqmhJQQjdeGZSGQOYd6scfquvfQoEGYI3PehBEJ3J3u84lWC4C3qumhJaZXkkewidbAzN972bFzMvXR-d2K847GY4kr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
بر اساس گزارش‌های دریافتی این سازمان از مراجع نظامی، یک نفتکش هنگام عبور خروجی از تنگه هرمز هدف یک پهپاد (UAV) قرار گرفته است. این شناور دچار خسارت جزئی شده، اما تمامی اعضای خدمه در سلامت هستند و حضور همه آن‌ها تأیید شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20959" target="_blank">📅 11:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20958">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‎ اتاق جنگ با یاشار : فلورا جون سر گردنه
هم مسیر شدن ناو هواپیمابر جورج
واشنگتن با یک کشتی کارگو ایرانی به نام «فلورا»که بسیار زیاد شبیه به عکس کاور مجله اکونومیک ۲۰۲۶ است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20958" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20957">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efb82e574.mp4?token=hQKqhXu-C5UO7euUywoTcFHVhqq8Lyry0ouJk-Gghz-y-PzFyDjSn1eJItJu4QwfOKC8qjYG_4SNFhOO_xJcFOL17KIFa9jEbncwtt0TyAO2-Fg5t9A01hIupCd3KaC0XXl7VSEW88wbNsoJaklOXBbM_sInH8d75Nrtz-XphJmUnwwGDqd5DqVFJ_u1oplAFAtxP5YFv_9ZnlpUPfKGRyIg9OMbAqXvmUuVdHgWahmM4tZoffEkL0q0qXO3Gsk36N7ooSz5C8MKGTEH7oUYbaW2311X5p2JH_v5D0Q24GNNig-Q3XBTpoFh9iX4-zDrrdC-bCGD7Cjw7-VS1eHchw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efb82e574.mp4?token=hQKqhXu-C5UO7euUywoTcFHVhqq8Lyry0ouJk-Gghz-y-PzFyDjSn1eJItJu4QwfOKC8qjYG_4SNFhOO_xJcFOL17KIFa9jEbncwtt0TyAO2-Fg5t9A01hIupCd3KaC0XXl7VSEW88wbNsoJaklOXBbM_sInH8d75Nrtz-XphJmUnwwGDqd5DqVFJ_u1oplAFAtxP5YFv_9ZnlpUPfKGRyIg9OMbAqXvmUuVdHgWahmM4tZoffEkL0q0qXO3Gsk36N7ooSz5C8MKGTEH7oUYbaW2311X5p2JH_v5D0Q24GNNig-Q3XBTpoFh9iX4-zDrrdC-bCGD7Cjw7-VS1eHchw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویکتور دیویس هنسون
تاریخ‌دان، نویسنده و تحلیلگر سیاسی محافظه‌کار آمریکایی و پژوهشگر ارشد مؤسسه هوور است. او از حامیان شناخته‌شده دونالد ترامپ به شمار می‌رود، کتابی در دفاع از ترامپ نوشته و دیدگاه‌هایش در رسانه‌های محافظه‌کار آمریکا بازتاب گسترده‌ای دارد, وی پیشنهاد کرده است ترامپ از شاهزاده رضا پهلوی حمایت کند و زمینه تشکیل یک دولت ایرانی در تبعید تحت رهبری ایشان و با مشارکت ایرانیان را برای جایگزینی رژیم جمهوری اسلامی را فراهم سازد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20957" target="_blank">📅 09:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20956">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هشدار خزانه‌داری آمریکا: تحریم‌های «بی‌سابقه» علیه ایران از هفته آینده
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد دولت ترامپ هفته آینده از بسته‌ای جدید از تحریم‌ها و اقدامات اقتصادی علیه ایران رونمایی می‌کند که به گفته او «در تاریخ بی‌سابقه» خواهد بود. جزئیات این اقدامات قرار است هفته آینده به‌صورت رسمی منتشر شود. این بسته بخشی از تشدید سیاست «فشار حداکثری» واشنگتن است و انتظار می‌رود بر مسدود کردن مسیرهای دور زدن تحریم‌ها، ناوگان سایه و کانال‌های مالی و ارزی ایران تمرکز داشته باشد؛ اقدامی که با هدف افزایش فشار اقتصادی بر تهران پیش از هر تحول دیپلماتیک یا نظامی دنبال می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20956" target="_blank">📅 09:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20955">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حقیقت یاب سنتکام در جواب به رسانه های رژیم :  ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» همچنان یکی از بالاترین نرخ‌های تمدید خدمت خدمه را در میان تمام ناوهای هواپیمابر نیروی دریایی ایالات متحده دارد؛ این نرخ ۸۴.۴ درصد است. ملوانان و تفنگداران دریایی گروه رزمی ناو هواپیمابر آبراهام لینکلن، پس از بیش از ۲۶۰ روز حضور در دریا، انجام ۱۰ هزار پرواز و مصرف ۱.۵ میلیون پوند مهمات، همچنان مقاوم و مصمم باقی مانده‌اند. هیچ‌یک از نیروهای نظامی حاضر در این ناو هواپیمابر جان خود را از دست نداده‌اند و تنها ملوانی که در ۳ اوت به دریا افتاد، به‌سرعت و در سلامت کامل پیدا و نجات داده شد. گزارش‌های گسترده و نادرست درباره مأموریت تاریخی آبراهام لینکلن، در حق زنان و مردان نظامی ما و خانواده‌هایشان بی‌انصافی است
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20955" target="_blank">📅 03:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20954">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هم اکنون حملات شدید پهپادی جمهوری اسلامی به مواضع گروه های کورد در اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20954" target="_blank">📅 03:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20953">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چند گزارش داشتم از صدای تیر اندازی سمت غرب (محدوده آزادی)
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20953" target="_blank">📅 02:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20952">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ به فاکس نیوز ‌: محاصره دریایی ایالات متحده در تنگه هرمز کاملاً برقرار است و «یک دیوار فولادی» است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20952" target="_blank">📅 02:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20951">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EinHX2Qz1DR_lv3c2Twkd48ws6wC5kRvvW1h5RUfHRMfQD7prTtEUEipmBRzbtqbXtr0RV8dANoeBmDHblykPwpL6e5ySz_Mi66gsf-dACmx1_bj05-DiUJP3VSde3vENJQN80hesE7Xuuoe714gDzLqbajDVxgosA26sBMZGCwZ0pmEnok1bib58CDWxLCrQzW3c1SamzHepNpsPTHMYuJHbgcScmaIjiLYbsEH9Yr5YMxyj5r5sne-X8QSaQsMXfOO9gjCEExiF4fvxO1Zu2vCvik1FRMk0WyMdOSpbzSR_z5GEGEP5RTSoUPgltEJfi_fDlGtBNzpbZdz1f5JoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای F/A-18C هورنت معمولی نسل اول برای تفنگداران دریایی آمریکا، از سمت تنگه هرمز با ترانسپوندر روشن( فعال بودن سیستم شناسایی و ارسال اطلاعات موقعیت ) با یک چرخش در ابوظبی فرود آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20951" target="_blank">📅 02:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20950">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بعد از مدتها حتی‌ اطراف تنگه هم سوخترسان دیده نمیشه عجیبه…</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20950" target="_blank">📅 01:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20949">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50455ef10.mp4?token=hyJsDvQXe5EQbTh7YgdC5ynk2u3tmsy0EyrsydgGmtPS4P9477yPIBjvBnCIsNPF-xd4xbtIqWWiSHz-WxdVMqtM4PQMh5VTLI0z_e8JgxYesKcyF-ltuJF_mhF1jgipdWJwdiV2xp93_mgfVhQOpSBw5TQVNQbULqJodtKIOxHNO9cGy73gofX1693KzGU35fnZucphqJ8ziDt_AdFKSM4xBBUgXCTE0a_7dmxD7ytnULp6MFB456oLvYDSCtZxpRkPu1waNYtg_GfdToQtUa5EYd2lPQLzPAaDAJ1ctonazNJgSQzr98dhc3Ni9f5MZcV9SevGt5NcuObfy9M-bKiIyL5ycSABGSC94wI9_Swk21GCSDj2PhI1h9lf0LP9vKDXAjWQWWuXtU11mSg8gyT8zwhydcdUzIDCfnxWTqm-8JPUtmaZxrpDJqeBglkNCP3b7DBB2ZOZuTgcPKK2RP_KRcvEdPKOqe8IJhLy6REPSXoYhYRNha8GI7YRzuvEs_aPYBAJVNFP1eVupAm42f99U7LzMMSFvJOR-z1Riaqs2lo2J-8vQKrQcvvkROThd0DyDw75CBNZ2FyC00ydZ1Ffw62FzmoRqcnLIsBKNcfNBa-Jq7t8aUGCgBiAvoHZBhjYitpf4C8Jy0DVLSSLTMSi-OVc99IQTyhVhu66TMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50455ef10.mp4?token=hyJsDvQXe5EQbTh7YgdC5ynk2u3tmsy0EyrsydgGmtPS4P9477yPIBjvBnCIsNPF-xd4xbtIqWWiSHz-WxdVMqtM4PQMh5VTLI0z_e8JgxYesKcyF-ltuJF_mhF1jgipdWJwdiV2xp93_mgfVhQOpSBw5TQVNQbULqJodtKIOxHNO9cGy73gofX1693KzGU35fnZucphqJ8ziDt_AdFKSM4xBBUgXCTE0a_7dmxD7ytnULp6MFB456oLvYDSCtZxpRkPu1waNYtg_GfdToQtUa5EYd2lPQLzPAaDAJ1ctonazNJgSQzr98dhc3Ni9f5MZcV9SevGt5NcuObfy9M-bKiIyL5ycSABGSC94wI9_Swk21GCSDj2PhI1h9lf0LP9vKDXAjWQWWuXtU11mSg8gyT8zwhydcdUzIDCfnxWTqm-8JPUtmaZxrpDJqeBglkNCP3b7DBB2ZOZuTgcPKK2RP_KRcvEdPKOqe8IJhLy6REPSXoYhYRNha8GI7YRzuvEs_aPYBAJVNFP1eVupAm42f99U7LzMMSFvJOR-z1Riaqs2lo2J-8vQKrQcvvkROThd0DyDw75CBNZ2FyC00ydZ1Ffw62FzmoRqcnLIsBKNcfNBa-Jq7t8aUGCgBiAvoHZBhjYitpf4C8Jy0DVLSSLTMSi-OVc99IQTyhVhu66TMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20949" target="_blank">📅 00:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20948">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ونس، معاون رئیس جمهور آمریکا: آمریکا ابزارهای زیادی برای مقابله با ایران در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20948" target="_blank">📅 00:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20947">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اکسیوس : جرد کوشنر، فرستاده ویژه رئیس جمهور ترامپ، قرار است هفته آینده به اسرائیل سفر کند و با نتانیاهو دیدار کند
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20947" target="_blank">📅 23:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رویترز : ترامپ در آستانه یک جنگ پیچیده‌تر قرار دارد و به نظر نمی‌رسد که این مسئله او را رها کند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20946" target="_blank">📅 22:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارش صدای انفجار‌ سیریک ، پرتاب موشک/پهپاد به سمت تنگه هرمز @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20945" target="_blank">📅 22:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اصفهانی معاون پزشکیان:
تغییر قیمت بنزین در کرمان به‌دلیل برخی بی‌تدبیری‌ها متوقف شد.
۱۴ میلیون لیتر بنزین در هر روز کم داریم
دولت برای بنزین برنامه دارد و روزهای آخر تصمیم‌گیری در مورد آن است.
ما ۳ برنامۀ جدی داریم و هرکدام از آن‌ها نهایی شود، قبل از اجرا آن را به مردم توضیح می‌دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20944" target="_blank">📅 22:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737fe5f83b.mp4?token=ePGxew61gGLJngFcZ3iCf2Fvks0tJS6Dwj2Q9WDXcazDOL8P-h5bXEIje-gCU52Khy_8Ja6qThDgCn7v11F38-OQ9EdZ5dOYM22ewtBI4lz3MSZos3MfT2chh85nCSsu7dfwZek3OoJMU0Ar8PY2CD52QMC2q4zQl1PIH9LOHNHSIH1ZA_jp6QizAqIZuhJnnPKiH4AyjLIviAmMoRGKMK9qWbfnQT4l94JcRAHZUF_oh5-aokuBnpf2Rla0UREHJ6YMu0lKLBh_sNWKhPuAQYIwaNucIJiffcy3uXe4Rcymwu70pq79FHTuvugG3z6CcATt-sOYuFNRg9CcSX5_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737fe5f83b.mp4?token=ePGxew61gGLJngFcZ3iCf2Fvks0tJS6Dwj2Q9WDXcazDOL8P-h5bXEIje-gCU52Khy_8Ja6qThDgCn7v11F38-OQ9EdZ5dOYM22ewtBI4lz3MSZos3MfT2chh85nCSsu7dfwZek3OoJMU0Ar8PY2CD52QMC2q4zQl1PIH9LOHNHSIH1ZA_jp6QizAqIZuhJnnPKiH4AyjLIviAmMoRGKMK9qWbfnQT4l94JcRAHZUF_oh5-aokuBnpf2Rla0UREHJ6YMu0lKLBh_sNWKhPuAQYIwaNucIJiffcy3uXe4Rcymwu70pq79FHTuvugG3z6CcATt-sOYuFNRg9CcSX5_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست به نیوز مکس : گزارش‌های مربوط به تخریب شرایط در ناو هواپیمابر ابراهام لینکلن کاملاً تحریف‌شده است و  هیچ کم و کسری وجود ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20943" target="_blank">📅 21:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20942">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سی‌بی‌اس: فقط یک ملوان در پی حادثه از عرشه هواپیمابر آمریکایی "یو‌اس‌اس لینکلن" در اوایل ماه آگوست(۲هفته پیش) به داخل دریا سقوط کرد. این ملوان توسط یک بالگرد جستجو و نجات نجات یافت و پس از دریافت درمان توسط بخش پزشکی، از کشتی منتقل شد تا مراقبت‌های پزشکی بیشتری دریافت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20942" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntaXkEhJYgD0bXKW0LjNrIOzRyw05J2dRFcOPcyXAEmlgary8jHkFi7wNepWYXhFpl6XAutTzvbBKOiGTBVWEya4hFdLzztszliKZmLtAKJDVeejzsU7GcIH6c4vYbKB0Qkrw7CqCLIfeYYh2-TSWi1Z8pFztNUAG4cjfDOx9B3oDGQsxmGBpaoG9OR-vr-8NPJZINbGB2JWL0LRlLe0LJkQPlz-hCMKIucnN_noqLbIM7SBIMXMMbIG2vepeEhCUEUB9Taz7Rib7Y-elFtWVsfk53qq7Y4qA6V_tcnrwB_5x4dwomWzn1RxS2m-cB99vCjKwqkPa1rxsSMDvDbyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ با ارسال این عکس نوشت برایم، من در منطقه ای زندگی می‌کنم که همه عرزشی هستند. دقایقی پیش در کرج رعد و برق مهیبی زد. بلافاصله اکثر این ساختمان ها برقهایشان را از ترس حمله هوایی خاموش کردند. اینها از ترس شب و روز ندارند. خودشان هم میدانند به زودی کارشان تمام است. به مردم بگو ناآمید نشوند ، پیروزی نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20941" target="_blank">📅 21:23 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
