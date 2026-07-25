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
<img src="https://cdn4.telesco.pe/file/iAxVfNDfbUhAPEbjiIMNtdLkwvqpQHsCe0S8vEat5uo-iijOSsuWHSiq4GvpfneEbRlmUFO7yGEftEiNAO_iR2XgfkdYB9ZPThUSwqJCEVLY4h0tXkvca3AuUU6J9hzoWvrayX6hDOZeeoilcw31Tw7I_m4h9k0FIJ8nGOZOdZFOjDaRv6QsdaW_ClIl_cBpinRveKR5B09GvVcGSIDljUzHuGwdGOQL-VSkwL5d-ilgxI3FgaAf-yVYQgLmynJySXAk6pAygGxPLEFHUqtJcWoyCCkAmBaKKvxU9CL0RILHTv8vowh2fo-XsHUcEMFF3x2vq84yxCI4ZbJZEdb3KA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 21:22:00</div>
<hr>

<div class="tg-post" id="msg-137543">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDZ7lZykvzN7mAi9BLJ2_5CLOu8MbE_HvBx9JX02H4lkETIIOK4w2RkPnAMuPXBymyVfpNEDx4GQuOzJ78p3k-aDa5uNNnWl5mL4pVSoIp9rMLr204bR2OZJ-UFsB6pyy6Rr2obUhot9bsdU1mqk4v3Fr7wVT3SJtqQvRPZqoqI12fQVD_pJy5ocdyiyat111x4t253hP2UaJeVNJ2s04hDB-bXCDaAEOmMSNIykEE9jIKwOe3mN4zPepf86bhn2-kwRZciVa_bmSZ8t1mY9rkzHN8gT8d5gGjtnH25Qll-chpwBW0lloFliiHUzQgR0meZZog48LerbNwetkBBJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقاد کتی پری از کاخ سفید بخاطر استفاده از آهنگش در ویدئویی از حمله به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/alonews/137543" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137542">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سازمان رادیو و تلویزیون اسرائیل: در حال حاضر بیش از 90 هواپیمای سوخت رسان آمریکایی در اسرائیل مستقر شده اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/alonews/137542" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137541">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
گزارش زلنسکی از برنامه های روسیه برای ادامه جنگ: پوتین در حال آماده‌سازی مقدمات برای یک بسیج گسترده‌تر است.
🔴
ما همچنین شاهد همکاری روسیه با کره شمالی هستیم. روسیه قصد دارد 30 هزار سرباز دیگر را از کره شمالی دریافت کند و آمادگی‌ها برای پذیرش آن‌ها از ماه ژوئن در منطقه وورونژ آغاز شده است.
🔴
کره شمالی نیز در حال آماده‌سازی برای انتقال سامانه‌های پرتاب جدید برای موشک‌های بالیستیک به روسیه است.
🔴
روسیه به کره شمالی کمک می‌کند تا نحوه جنگیدن را بیاموزد، سلاح‌های آن‌ها را بهبود می‌بخشد و به آن‌ها تجربه استفاده عملی از این سلاح‌ها را در دنیای واقعی می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/alonews/137541" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137540">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ad5f15cf.mp4?token=GcrzXgwWGGm7v2nAUZf09DXz1jOQKjeLIBuKGXYR-QGbUO3psimBox4PGNc3_mRNZw3qiHpSugz33rJ6R8dUdiY_g5tjiYs5Rhy3elvpR1LnOH-piv1JZ-JMUGv-UUjXL1WF8bJ4zTXSjYiiiMKZtwimq5WQLboPebMtAkY2OcwUHcGoNdZ7gEcsUn5vZEeT63QDu5N57Gf3y9yHQg8vowOayh7_hj-c26vOeAwyjphqLTA0svdrhoDuXqs3bS9RQNsHCQaD-l_9kXJB3dNhmkpQI-7_Woo_sWi6YK-vp2rTHuRoh4qBIJlnl8VKqqwHmACrET9DjE_91PZayiQeO2AgfYBdxgEYFQfGZMZIj43uy9zFBKUS2TSNIIipxhNFO1H2Aa-_b7Mpy56YxgrnSRBE8IP4LPiWjwUsAT-l_Og78MEb_XLvxUP3K7gZA9RgyeHqvSlyYlgryFwS_kyI8bzZO0VmYtppT4bnDYtQ5nwzgc9IZUO-RQr_xeZw-LFVi61nE5vzRCwbDrYdpuKx10SK0PeBYCUPg5udAtuGyzins76LThQy6QlqzQ4k7YP6F4ZwkN0vUWUn7KQo5WvqPw69xx_44HV7C4VCEV6N8zW16moL-W2MWz5I9gJpRFb8uCmAQLRfXQwzGT_V9cOTBuM73UcIY2WBO_v2_Te5Eyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ad5f15cf.mp4?token=GcrzXgwWGGm7v2nAUZf09DXz1jOQKjeLIBuKGXYR-QGbUO3psimBox4PGNc3_mRNZw3qiHpSugz33rJ6R8dUdiY_g5tjiYs5Rhy3elvpR1LnOH-piv1JZ-JMUGv-UUjXL1WF8bJ4zTXSjYiiiMKZtwimq5WQLboPebMtAkY2OcwUHcGoNdZ7gEcsUn5vZEeT63QDu5N57Gf3y9yHQg8vowOayh7_hj-c26vOeAwyjphqLTA0svdrhoDuXqs3bS9RQNsHCQaD-l_9kXJB3dNhmkpQI-7_Woo_sWi6YK-vp2rTHuRoh4qBIJlnl8VKqqwHmACrET9DjE_91PZayiQeO2AgfYBdxgEYFQfGZMZIj43uy9zFBKUS2TSNIIipxhNFO1H2Aa-_b7Mpy56YxgrnSRBE8IP4LPiWjwUsAT-l_Og78MEb_XLvxUP3K7gZA9RgyeHqvSlyYlgryFwS_kyI8bzZO0VmYtppT4bnDYtQ5nwzgc9IZUO-RQr_xeZw-LFVi61nE5vzRCwbDrYdpuKx10SK0PeBYCUPg5udAtuGyzins76LThQy6QlqzQ4k7YP6F4ZwkN0vUWUn7KQo5WvqPw69xx_44HV7C4VCEV6N8zW16moL-W2MWz5I9gJpRFb8uCmAQLRfXQwzGT_V9cOTBuM73UcIY2WBO_v2_Te5Eyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار علیه شهریاری در تجمعات شبانه؛ مرگ بر جیره خور آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/137540" target="_blank">📅 21:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137539">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وای‌نت: اسرائیل خود را برای حمله گسترده آمریکا به ایران در فاصله شب جمعه تا بامداد شنبه آماده کرده بود، اما دونالد ترامپ برای دادن فرصت بیشتر به مذاکرات، این اقدام را به تعویق انداخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/137539" target="_blank">📅 21:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137538">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
تايمز  اسرائیل: ترامپ از ارتش آمریکا درخواست کرده بود که حمله به ایران را به تعویق بیندازد. او در حال حاضر ترجیح می‌دهد که به مذاکرات ادامه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/137538" target="_blank">📅 20:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137537">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی سپاه: طی ۱۵ روز نبرد (از ۱۷ تیر تا ۳۱ تیر)، ۱۱ هواپیمای جنگنده و بالگرد آمریکایی را روی زمین و در حالی که در پایگاه‌های آمریکایی در منطقه مستقر بودند، منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/137537" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137536">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
آکسیوس به نقل از دو منبع: ارتش آمریکا در حال کار بر روی طرح‌هایی برای عملیات بزرگ احتمالی علیه ایران است، اما ترامپ هنوز دستوری نداده است.
🔴
تصمیم ترامپ برای توقف حملات در روز شنبه، ساعاتی پس از ورود هیئت عمانی به تهران برای مذاکره در مورد تنگه هرمز اتخاذ شد./ ممکن است تا پایان هفته، توافقی بین ایران و عمان در خصوص تنگه هرمز حاصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/137536" target="_blank">📅 20:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137535">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
دو شرکت زیرمجموعه لوفت‌هانزا آلمان پروازهای تل‌آویو را تا سه‌شنبه لغو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137535" target="_blank">📅 20:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137534">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):  در پی گزارش در مورد یک تیراندازی در منطقه جامعه سوسیا، کمی پیش از این یک درگیری خشونت‌آمیز بین شهروندان اسرائیلی و فلسطینیان در منطقه شکل گرفت، که در آن هر دو طرف سنگ پرتاب کردند. این یک حادثه تیراندازی نبود.
🔴
سپس یک تروریست سلاح یکی از شهروندان را دزدید و به سمت آسمان شلیک کرد. علاوه بر این، یک شهروند اسرائیلی در نتیجه پرتاب سنگ‌ها مجروح شد و برای دریافت درمان پزشکی تخلیه شد.
🔴
سربازان IDF در حال تعقیب تروریست هستند و در منطقه چک‌پوینت‌های جاده‌ای برپا کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/137534" target="_blank">📅 20:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137533">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
معاون نخست‌وزیر و وزیر امور خارجه پاکستان، ایزاک دار، با شاهزاده فیصل بن فرحان آل سعود، وزیر امور خارجه عربستان سعودی، گفتگو کرد تا در مورد آخرین تحولات منطقه‌ای تبادل نظر کنند.
🔴
آن‌ها همچنین در مورد امنیت مسیرهای کشتیرانی در خلیج فارس و دریای سرخ گفتگو کردند.
🔴
هر دو طرف مجدداً بر روابط نزدیک بین پاکستان و عربستان سعودی تأکید کردند و بر اهمیت ادامه دیپلماسی تأکید نمودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/137533" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137532">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
الحدث: وزیر خارجه عربستان تماس تلفنی از همتای پاکستانی خود دریافت کرد و درباره تلاشها برای کاهش تنش در منطقه گفت‌وگو کردند.
🔴
وزیر خارجه عربستان و همتای پاکستانی‌اش درباره تلاش‌ها برای تأمین امنیت و ایمنی آبراه‌ها بحث و تبادل نظر کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/137532" target="_blank">📅 20:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137531">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رسانه‌های عبری: احمد وحیدی و مجید موسوی در صدر فهرست اهداف ترور اسرائیل قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/137531" target="_blank">📅 20:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137530">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU7T2uI8ochagAYINdINXI_FKYp4Ef3T8Mcif86IizbrOgvu3nhJoKbEao0n7QJD40lazc2-vfVRNeDtmI0p1aWOervYZJO12uIYj6z2aelci_mNnR4KsZZUpoJK7hAv_Fech_Xkv2ulw65nOTdUMyvOX5scUKz7xAD4boJmKH4nL5bouQBexn0iJg1iHrS9DTSL7jznNg8jT9A1_Wyypx5BA_jkljrrU_zlZmoHArp12-F-EEHoSW_T_nKC9-RxEvyI2rH6LoHrbEQz8wG0lxQklxfTDVsOWpORoVtB5E2ed-FjsRCgLbo3vbpdujh7sJyxFMIDboTdVVcg9PxYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صفحه رسمی سفارت آلمان در تهران شایعات تخلیه کارکنان این نمایندگی دیپلماتیک رو تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137530" target="_blank">📅 20:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137529">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c6d15482.mp4?token=fcn5F9m5FEn9BPfFNxLkqZKsyJX0VHVwixMvFiYUZClbWb93IrvZ4nzQHO_OmyB2oept68szq1dQF4HZM4T0uBCzhHT5NaqZpBxKW88woP4JM7BziB6aWxDs2Pcq7Ic5tD28ELf13eGLcdt3rh_Pvae8WIUIwZJRpLAyNsRAiqmpskbqCcNurO2al8NsZCyTAa5IHp6XYq2sMLBdhaXpY57zHivKnmY-0Yi94Gn9A5_oTeyZDJioimNHoRk4ZeRi75kGcHT7x6BAkxAxkE1ntSQT7IBms88vD0BAlVgwG2qOAXLqnlv4qB1Wt1MGacOOLQQARFethYgYvIzodoTKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c6d15482.mp4?token=fcn5F9m5FEn9BPfFNxLkqZKsyJX0VHVwixMvFiYUZClbWb93IrvZ4nzQHO_OmyB2oept68szq1dQF4HZM4T0uBCzhHT5NaqZpBxKW88woP4JM7BziB6aWxDs2Pcq7Ic5tD28ELf13eGLcdt3rh_Pvae8WIUIwZJRpLAyNsRAiqmpskbqCcNurO2al8NsZCyTAa5IHp6XYq2sMLBdhaXpY57zHivKnmY-0Yi94Gn9A5_oTeyZDJioimNHoRk4ZeRi75kGcHT7x6BAkxAxkE1ntSQT7IBms88vD0BAlVgwG2qOAXLqnlv4qB1Wt1MGacOOLQQARFethYgYvIzodoTKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ موقع تعریف‌کردن ماجرای تیراندازی در ضیافت شام خبرنگاران کاخ سفید یاد نیکی میناژ افتاد: «بعد از اینکه صدای تیر اومد، مردم داد زدن: "بخوابید زمین! بخوابید زمین!" همین باعث شد نیکی میناج شروع کنه به رقص و تکون دادن و قر دادن! باورتون میشه؟ خدایی فقط اون بود که فهمید منظور اصلی “Get down” چی بود!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137529" target="_blank">📅 19:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137528">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
برخی منابع می گویند:  با افزایش احتمال شدت‌گیری قابل توجه تنش‌ها، بار دیگر میانجی‌های مختلف پاکستانی، عمانی، قطری و... هر یک با موضوعات و طرح‌های مختلف در ۴۸ ساعت گذشته فعال شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/137528" target="_blank">📅 19:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137527">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پس از اتریش و ایتالیا، دو شرکت دیگر از گروه لوفت‌هانزا پروازهای تل‌آویو را لغو کردند
🔴
پس از شرکت‌های هواپیمایی اتریش و ایتالیا، دو شرکت دیگر زیرمجموعه گروه هواپیمایی لوفت‌هانزای آلمان نیز تمامی پروازهای رفت‌وبرگشت خود به تل‌آویو را تا روز سه‌شنبه لغو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137527" target="_blank">📅 19:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137526">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
مقاومت عراق: هیچ عملیاتی علیه اربیل و کویت انجام نداده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137526" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137525">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
حوثی های یمن دقایقی پیش یه کشتی دیگه نزدیک عربستان رو مورد هدف قرار دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137525" target="_blank">📅 19:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137524">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e37e5e25.mp4?token=UrbXwah1TACZKycEf8uSlf910Jui9HcMJ-ExtY7XQJnt94s-Qjtw6XGsO2s1roauVS7AiZnvvePIsfzG6Q9bnbX3iFM_CU7LR2ARtOdIvldG3uLYYUELgehY0KrTFblHK00Laj_4gKVyjUGWOb7BvFQ632F6BYrnHIXNUQrpvxMl39Tm5UEVjF7h2gftfvJFYDMVVU-oIS6DChVbXj9yU5IgiVmpWpddbYxkFptUBJp-x0fu81FLyQdLdj0O0DpAJe4QdJWfCoYkkhOrETAqx2TlvQQzeeXdjoMznKFdhPoRMl1b6w7k3_ZcF_Mt7dExFezD3Sd2b1vQWPoHKBV-WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e37e5e25.mp4?token=UrbXwah1TACZKycEf8uSlf910Jui9HcMJ-ExtY7XQJnt94s-Qjtw6XGsO2s1roauVS7AiZnvvePIsfzG6Q9bnbX3iFM_CU7LR2ARtOdIvldG3uLYYUELgehY0KrTFblHK00Laj_4gKVyjUGWOb7BvFQ632F6BYrnHIXNUQrpvxMl39Tm5UEVjF7h2gftfvJFYDMVVU-oIS6DChVbXj9yU5IgiVmpWpddbYxkFptUBJp-x0fu81FLyQdLdj0O0DpAJe4QdJWfCoYkkhOrETAqx2TlvQQzeeXdjoMznKFdhPoRMl1b6w7k3_ZcF_Mt7dExFezD3Sd2b1vQWPoHKBV-WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو عجیب منتشر شده توسط وزارت جنگ اوکراین از سرنگونی یک پهپاد شاهد در آسمان کی‌اف
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137524" target="_blank">📅 19:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137523">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1gwe0D34HU7MnnO_CgLXAwHr8gS0PpjTkj1uFzw5fLZi_idrA2Br4VIYG4-t6zf_r73rERqTNEQrX_vsv_IgVRJa6JIfmYU_cfB_i6Yr0USeWAcaOE2eT8tWfJ-Le2roYYM1PmKjxFklAexB9FIi17v-Clf45iE6vUGazGx3ckL3gvgr0C1bZ3JxpY0JUDHOfAJ7AtsG-4ox0pmawkTd884mSBrrTvo8_KrbUJTIhqsnai0ZmJyc3QpOQ-rX8vaC6Gz_XwTqB_Ldyp2S9Fu7zq4SNQATblpMDfLaMnDZXzzPEtn7W4gU2wky608y6JJMrobrUKKeguOXO9DoTikXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر منتشرشده از فرودگاه اربیل نشون میده ده‌ها فروند هواپیمای نظامی آمریکا در حال فرود و برخاست هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137523" target="_blank">📅 19:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137522">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXsiKbPRJGpPCMIsSnD_p6iwfE-KgMEWc6HZj2z7TUH4-4zIEkKnT24gWh3B6EbkdqCttmolhN6oclGiHvH5s7bOSW79vA0upWc81v6eLkVW3EvXCQB7h2lSJXEVrpnCnR59ed6cFa8QRtU9ReOn-spc0NVNNJXdxHM07E7_rp74NK4yGANGAhpoc8kGsXAtU5SQmYAGpjBB7L-2Ml_2LLx2z0dBJrXSKDP8O-p6bExdeYuzBSoUo2CVPXRsCEOwO_Hd8Vz5RboLNQh5uNFgMipp9OSeQDnuyZR-CZ3hoSV8VzwGlNlLCbjhJvHbZYVz6teabuhPg1T5_fPVTaLncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تروث سوشال ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/137522" target="_blank">📅 18:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137521">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
عراقچی: ما در تماس مستمر با کشورهای منطقه هستیم و توضیح می‌دهیم که هیچ دشمنی با آنها نداریم.
🔴
برخی کشورهای منطقه اکنون دریافته‌اند که حضور پایگاه‌های آمریکایی در برخی موارد به عاملی تهدیدکننده برای امنیت آنها تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/137521" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137520">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اردستانی، عضو کمیسیون امنیت ملی:
شاید آمریکا با سرگرم کردن ما به «تنگه هرمز» و «کوه کلنگ»، یک رده از مسئولان را بار دیگر ترور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137520" target="_blank">📅 18:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137519">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
اکسیوس : آمریکایی‌ها دیشب برای عملیات بزرگ‌تر علیه ایران آماده نشده بودند
🔴
برنامه‌شون فقط حمله‌ای در همون حد و اندازه حمله‌های دو هفته قبل بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137519" target="_blank">📅 18:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137518">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سپاه: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در غرب زنجان در روز یکشنبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137518" target="_blank">📅 18:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137517">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری/ کانال۱۱ عبری: ترامپ، شب گذشته یک حمله بسیار گسترده در سراسر ایران را به تعویق انداخت، به این امید که بتواند به مذاکرات بازگردد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137517" target="_blank">📅 18:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137516">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزارت حمل و نقل قطر: فعالیت‌های کشتیرانی برای تمامی انواع حمل و نقل دریایی و شناورها از ۲۶ جولای به طور کامل از سر گرفته می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137516" target="_blank">📅 18:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137515">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upjVtKGkC1wYUHxyNgr7IIjjbhbKQLJL7TS18adKS9H9jbhou5vbWIOY1w8c-1nR1HrqZo9e9nXIDkwh4ZzZBe69JJtvvKSI8XKMRn_Zst9Ll-oKEK34F6K1eCoV8LtSATo5OwGqPXTJQZ3gWy5s_XoQmIiHZRXGH3CviMvTEWSP3888m7TzWWNQ1eVembp8g6fTLdD1W14c4kOE6NsIUUM72qdDBiZxaljYM3G1SQxXKmMjUacv3xGSLxO6J0GkmYG462oNyxM_XcDgBEYFGnfQJEwO24UVPYa_T1aiIjAkxt858UA8vEnPeZxkyuVn6YOdPaH6jtobsINSHBC6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبری مبنی بر " ارائه طرح جدید آتش‌بس از سوی میانجی‌ها به امریکا و ایران" در فضای مجازی درحال وایرال شدن است، بایستی اشاره کرد که این طرح و خبر جدید نیست و مربوط به هفته قبل (۲۰ جولای) است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/137515" target="_blank">📅 18:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137514">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ادعای کانال ۱۲ اسرائیل: آماده‌باش در سطح بالا در اسرائیل برقرار است؛ آنها منتظر تصمیم ترامپ در مورد آینده رویارویی با ایران هستند
‏
🔴
شرکت‌های هواپیمایی خارجی لغو پروازهای خود به مقصد و از مبدأ اسرائیل را آغاز کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137514" target="_blank">📅 18:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137512">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKoaSGPvYyqgM6x7bAts-L90SLIdCvs34YgoVSsapqJ-2bn3D6VOmrJr8IcqasmEH7P1JRsIuxHCyJTy89eX4DsHmTqWqvVPkHp8DtWktbp5rUVhS_Tmylb5jMedMxpkyb9GU4lR4G-Rz5NNlEMtIYmCW6hXE0smk2XGud_2mJ1OEUAfop5GIksnJ9C81QeBfuv8x4_Djsoc8eVxhMBchEZkPSy9qdb58pSI_5TGjvdgV4Fv310FzW6QNTOCBOJBcXshO17tsPPI2WyjoAieUAiDF7ItB_-3ruHVBsTUI7AuQO-Lx3lcsPoZcWiB_UVy-t4UvksWRs-PXvd-fnGkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEpoeKHHNICx2at2eJGpeXoUS40q4DycT2f0ZUuILJBv0JWfw5Dihno8LrtsgOVsQbQvXaxRZxduhQOMfN-LTSASfy2bxaP4Q_llDWnEiKNVdIHSekxaf0mAa4lLiPoThP8oIi_TGv6-RUJKpZrSTF1XuMyrDIIbAFMR3GV5t-_uAcP_nbr1AKPKIlg_csoZBAOxCCvmxAWNdnDiGPKvhgUxMTwzl2w67FpZyHMQJCbJsNeZb7mwbauv1fD7OEofQ4dzErX5Me5550B_4aW1vUCUh3jK_15EA4-zjrsz7wI8DaRTv2gt-PY3ftZ6i_ZcjFjWM79nL7F_FWV_NxzaZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137512" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137511">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0579d0de.mp4?token=S_FFb5sj2jfhZ4yDgvjw7ME1xvoue1-4vT1H0tCQUofTFaftgMSJ9u9G9sdP3T40KTYa4baIuCpT-7sSmQWBkqFSB1F5A-9OMFq6TgoujovDCd9gNc49uPQ0pHrHQx8wcf5b0mX2Fu1CvTVl2VllXw3kai7FAIHN4Zg6qMt8itw5aShzLP4F4dm52LDFHYaJi86sGSJggEucBH8TkTxm_Ykf9_vAlW4KKMzwc48e_Gxz5c2ooG1AG5Lt0-OEecdfI59TqAl6qIJMWnVmCeTyp6Ch18DhGn6SoTtKbWKt9aP-ZYbg9dEvOzPz5LIZqVZ8aE3UIU6ZIj0fSD6MHauNlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0579d0de.mp4?token=S_FFb5sj2jfhZ4yDgvjw7ME1xvoue1-4vT1H0tCQUofTFaftgMSJ9u9G9sdP3T40KTYa4baIuCpT-7sSmQWBkqFSB1F5A-9OMFq6TgoujovDCd9gNc49uPQ0pHrHQx8wcf5b0mX2Fu1CvTVl2VllXw3kai7FAIHN4Zg6qMt8itw5aShzLP4F4dm52LDFHYaJi86sGSJggEucBH8TkTxm_Ykf9_vAlW4KKMzwc48e_Gxz5c2ooG1AG5Lt0-OEecdfI59TqAl6qIJMWnVmCeTyp6Ch18DhGn6SoTtKbWKt9aP-ZYbg9dEvOzPz5LIZqVZ8aE3UIU6ZIj0fSD6MHauNlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای آمریکایی اکنون در فرودگاه بین المللی جده فرود آمده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137511" target="_blank">📅 18:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137510">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLi6jc7bql_z7-z3Y4Rsg9lvSqmMykBdKCNWoUvt2uoIQ5HTCT30FonqEOaZzJGZhbfjhJbQ1GRxfUq5DnhiRSJ6ULP8keFIk_rpim0sxNQNAN0q1-rck2tiqObh65GmDwWGuwVpPPqZuiqRgXbu38OlxWyxQcHdBeAPtn2uGq4QCxQxUMVDG1sLRvGd7SksiaX3dlyQwuJ-1LOH_W6lvzXC9h0f2DWceXVpJAUgNxAv5SAi78jIx86YtIuIpS4--1F5xR_2so0ZUm6bpcis0-4SnzI13jNelqUTAOIQynxqYgzTYtR52J9HUa-eSlqKnLQlYMNn00ZYMb76WJjJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
آموزش تیراندازی با سلاح به کودکان در میدان آزادی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137510" target="_blank">📅 18:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137509">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLLPVZM7HGJrePOthYQHr6J3kqu3ETOQByioUIynFzIKv9wxYUoHdZ5OxwnL_zd8WJimTOf2_a4hIit2nnxiD4IrvLp4LUOZEfakEZHAzDt_j8Rw4VdA1SseBMk-tKXOTTZzykPhGOH7zdM6chxZQt4hukr8i_rT6MernoLneNu35c1dhim-27q9kymqfQK83kflBsFy_niZce5FjVKieRTr4-OSrzy5yEgmQaJWImz94x7fiSogPwEkJqvtQ_L4A-CqtzYLPlK5p_nlz-svcx8RpXMXmuzzh3eOrgy5UaTrWqLU8HHNwOndubxcm0HhAi2LvSZYnNme5LK14W5-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
لورا لومر خبرنگار نزدیک به ترامپ:
‏در اعتراضات دی ماه ایران، 100 هزار نفر کشته شدن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137509" target="_blank">📅 18:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137508">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
حملات اسرائیل به شهرک کونین در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137508" target="_blank">📅 17:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137507">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS3P0tkWgV86zKFvsXDZ1blB_JU7qB_ag1i3LsHuevi3SzzGhqHS0bgCIwNkcfgdumu-3m_DucSmgoZ8su3lFYgIFI3iguQjrLpwb9UvnPHL0CJLCrkDtq3wn9YRiMdTVHrSWkmX25hmSNZbWyenEh_HrmRz4fe7YnDUeJO6m50Dm9jlpHNxZLwQ_bl06U5w364l2GYPoA-bN00N04sBFHB7QQRNqLbod9Hg85q6w-53MnM-27iYJr-dc6oVhOUnVGJL3_OfBAmyZR-h5OrKrAoAIjSVdYhs9Q2xA5uDQphb26KN49AKXIOF7pRlhFU7lLYYVvV3LUOtxujsWRFEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس
شلتر
:
اول اسرائیل رو نابود میکنیم بعد میریم سراغ عربستانی‌ها و بعد امام زمان میاد
🔴
پ.ن: عجب پوست شفافی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137507" target="_blank">📅 17:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137506">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
لغو پروازها به مقصد یا از مبدأ اسرائیل آغاز شده؛ این احتمالاً نشانه‌ای است از آنچه در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137506" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137505">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شهریاری: ثابتی با فساد وارد مجلس شده و هیچ رزومه‌ای نداره و با رانت اسم خودشو جزو ۳۰تا نخبه تهران رد کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137505" target="_blank">📅 17:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137504">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXT6-bA6UUg10KSE4ood6GgToEJ49JxF9OAdMXnWE8ysJrL2nN-EyOMPQ3BImXfAK3bPoKDfz0F_LeE3Mn45x-CHtwXRFPnndV-1FZulk81-_GJ9i_tXGGlJQqf5GN3oUr6JeHDlo6czm6v7T1q2Z7ORi5fXrU5BxfVe_REohYNmeg6jSVC35L42sKYww9LkEX-969IqOCdSesmeJ4JmdBH4RC9A2veDk-XLiQNIK1vojvmXixHMlmwisEcBaMqvpj0LyGUiGX7ZxEWOLz9YdRONnxFcJsbgJGWiitH1pCSsmeDsKHYLiyfY-cexsOIEQ_kysme8ficlgBXtgia93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ام‌جی لاریجانی:
آقای شهید اینترنت رو به کشور آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137504" target="_blank">📅 17:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137503">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHQoFRl7Qv5dCWZJ99Mlh3DRkOryBh8FoL3S4VkakdSaj8nMmiptLY4j3_ebnh3uw8P7lLA5H9OoK5z_4uKsxAtuzFFLwVW5QZ8QX0xTBsOOPbIwA_vhn6hWt_zv6yNQjvGJLU5Tpg5N4hCE3q2eNI9efsCpXHI8bW2QZgElakTN61F8UDbnpR-7YhK-JBj4hwR1kLWAiHAX3m6CNa5FcTCW7WnaOyduJxgcTJp4-kYfsF1C7v2giddoSokU_TQMaE5195453GAfUnAaZMp60NhrXdDxAu0hOiRR2hy6tjDxujoAtpwpXaO8ElfpCG_ZHbAazCqdRK6Jbve_Wxp3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس :  ایالات متحده درخواست آتش‌بس موقت با ایران را مطرح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137503" target="_blank">📅 17:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137502">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
نیویورک پست:
ایالات متحده در حال بررسی طرحی برای خارج کردن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137502" target="_blank">📅 16:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137501">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS6oQQ7sIDlQraeeJWxnCTomcUCP2J74LTwX0gJqH5UDgg9OI4A4G--kT_7Irn4J9XwLyBQGWr-fd_EBA0Xw_G6wXDWJRCoNAKO1LZR4ikwcpxtIv5A9czproEtlvg6kSfWVeVuzZ2R9cBBGKK2MJCwE9hYsELPfnLuCIYZUp2CeGRgpXBPtKBuXrkSqjC50sTWadZetMuxMihIvyWfe5sd_Hzd4CxY1C75W7tbOJCTBxHDofIzImYuHMHr8JVpug4psM0aXoCVoIT0Wb0O5oiefv5Uo3a-9GwUpDBMA0oGcuf79p0tJWf-O0viuo_nmGpMzxjdQpyEi0ahK9PJmYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیری ابیانه: آمریکا برای حمله زمینی به ایران آماده شده و این حمله ممکنه پیش از انتخابات کنگره آمریکا و حتی در روزهای آینده انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/137501" target="_blank">📅 16:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137500">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/137500" target="_blank">📅 16:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری/باراک راوید:
طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/137499" target="_blank">📅 16:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e22034d8.mp4?token=UDCyPOn4lKTq0ZPGkX2xZTVRPXwCqKnT5HaqYl0CSpjFtiK3cspL1mO8Ft1IhWdx_b-KD7Luxim0GxpYHDl2upTs4lsg7dvDgb6w40I_oiRbU-HFl7XVDrx9tAP2YflmchYDfTjYxsKVtpJlI-l1DFyIQADaZ2PsGJ1G9duOnSPHluC2X4ejxspYmSNfSBVepV16moIDcgTYTVh5f6N4hJKVvfuufzBb4cHV_DJCwvsFGFFN54XT-FNYz7qL6hKlQx5Z0pdXzMyMh8NBdxC7vvMLgB2N2beT5fFJnkO3MMhBeH9bsKNMZc0brMXQQ3TSFBK2ircrSxh8wv7sNHQ7zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e22034d8.mp4?token=UDCyPOn4lKTq0ZPGkX2xZTVRPXwCqKnT5HaqYl0CSpjFtiK3cspL1mO8Ft1IhWdx_b-KD7Luxim0GxpYHDl2upTs4lsg7dvDgb6w40I_oiRbU-HFl7XVDrx9tAP2YflmchYDfTjYxsKVtpJlI-l1DFyIQADaZ2PsGJ1G9duOnSPHluC2X4ejxspYmSNfSBVepV16moIDcgTYTVh5f6N4hJKVvfuufzBb4cHV_DJCwvsFGFFN54XT-FNYz7qL6hKlQx5Z0pdXzMyMh8NBdxC7vvMLgB2N2beT5fFJnkO3MMhBeH9bsKNMZc0brMXQQ3TSFBK2ircrSxh8wv7sNHQ7zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد یاراحمدی، دوبلور پیشکسوت سینما و تلویزیون درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/137498" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رادیو رسمی اسرائیل: ارتش در کرانه باختری دستور گسترش دامنه عملیات‌های تهاجمی خود را دریافت کرد.
🔴
ارتش اسرائیل تصمیم به استقرار ۸ گردان در لبنان، ۵ گردان در غزه و ۲۶ گردان در کرانه باختری گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137497" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137496">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
اکسیوس:  طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137496" target="_blank">📅 16:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137495">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e4bbc306.mp4?token=sCw6nGG3kqeYVAKq8Lksn-VyYU-XyIJrG3HR_u6si1gHRbYh2_kKJ5-aOGLqdK51qubS5hAvdGbqso_zZOvaz-9n6zKifd9yDR6DXPkbWknAg6oZVH_Naq06xAi3IcJ7IgAtbo2GMRohTgRbge2AH9xrNSUHpR6d4ul9hroE9TKktnC4Cy0fQYRMNfTIF4FX8U8QNngpwq1eFzneLk05Q4uAUOLD4juGRKqFaUmJFyK3iOoc3IJI-PblBL4BCVYPIYWWcX-vhWOzVHGCmTZvqumwVzr5goHMyLgcmyMK4CbPCCAa0T52UuJI_y3NWey4Gre4ZvSdAp170rBUCmrfTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e4bbc306.mp4?token=sCw6nGG3kqeYVAKq8Lksn-VyYU-XyIJrG3HR_u6si1gHRbYh2_kKJ5-aOGLqdK51qubS5hAvdGbqso_zZOvaz-9n6zKifd9yDR6DXPkbWknAg6oZVH_Naq06xAi3IcJ7IgAtbo2GMRohTgRbge2AH9xrNSUHpR6d4ul9hroE9TKktnC4Cy0fQYRMNfTIF4FX8U8QNngpwq1eFzneLk05Q4uAUOLD4juGRKqFaUmJFyK3iOoc3IJI-PblBL4BCVYPIYWWcX-vhWOzVHGCmTZvqumwVzr5goHMyLgcmyMK4CbPCCAa0T52UuJI_y3NWey4Gre4ZvSdAp170rBUCmrfTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین تصاویری را منتشر کرده که نشان می‌دهد چگونه پهپادهای روسی با شلیک از سلاح‌های سبک از داخل یک هواپیمای یاک-52 سرنگون کرده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137495" target="_blank">📅 16:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137494">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exW9rCBxfJmlvtYoaGUgBMXPIT8FuHZKdQak_xmI19xeR5OVQk8QRhsrW_fDMIXWxGMIi8LbAf2rp9weNpHJBhJ-lCydc6I2hjG9Q3HKfOZFYgZxGwCaDn2lIKtf-MJgiiqCCVy8Z1xFUm6stIbqNTSB7oWMQ76zSYHggUivLTkeOu-th6A35SNpChKCmp-mrzne_dnMOQ6P3ZTMJSA0JeLsteMWvDz1a6Us-yeeucYQsdnYxUhw3CP6bUqj8d7ZXOvCNHG_fyuD_Ws7f61_-UdcI6QJBKHI_UnQPjBmp4s2xxGebZUr3B2hg9loUqdFeUEggnqwodVbhT-D3dZamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله عربستان سعودی به هدفی در مأرب یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137494" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137493">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
منابع عربی از حمله به پایگاه آمریکا در نزدیکی فرودگاه اربیل خبر می‌‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137493" target="_blank">📅 16:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137492">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن:
دو عملیات منحصر به فرد علیه عربستان انجام دادیم
🔴
اهداف حساسی در تأسیسات آرامکو در جیزان و ینبع هدف قرار گرفت
🔴
محاصره دریایی اعمال شده نیز همچنان پابرجا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137492" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137491">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی: مذاکرات در هماهنگی با مسئولان ارشد کشوری انجام می‌شود
🔴
عباس گلرو: مذاکرات در هماهنگی با مسئولان ارشد کشوری انجام می‌شود و مذاکرات اخیر نیز در نهایت تصمیم نظام بود.
🔴
آمریکایی‌ها پس از مذاکرات اسلام‌آباد نیز دوباره مرتکب نقض تفاهمنامه شدند، بدیهی‌ست که در مقابل ما نیز تفاهمنامه را نقض کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137491" target="_blank">📅 16:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137490">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuBPF0pdOitz5Dnp2ArlfZ-TNfwSz5bloSpNqel7UcMqaUyOTCqr6Pgd_Oo95ksdT7LfzryTVhBN6T4N3Za8_cplCeQJ6vY69mOqJxbhKFmLFNvaaRJ5K_tbP6zI5naUYGFg2tlIrGHzHbKkgqCzeFdnF7xXY_FlPYH2rx4PZta1xmLVcMXBfGbEP_ucMrqW_SLYTmHZG4_lvMmHC-LHFuRUwdJby8cAWv5M8XmluwzxuT-_cj9LQqii7BtX26rzNnYem4-diNuKd4pi4h8orXklWx7qcKT5xU8SM4O0dlv-inGL7hnVbO-5-ZAJnRsSbwLHMBJipWRX2MdySA_6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش‌سوزی‌های گسترده، 200 هزار نفر را در فرانسه و اسپانیا به فرار وادار کرد.
🔴
آتش‌سوزی‌ها در فرانسه و اسپانیا شدت گرفته است. آتش‌سوزی‌های نزدیک به مادرید از کنترل خارج شده‌اند و 141 هزار نفر در مناطق ژیِروند و لاند فرانسه به تنهایی تخلیه شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137490" target="_blank">📅 16:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137489">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRZV4srZASgqSel_4uEISgF_pv-tiqTQGcinizpJ23KIrb0CoYXIoteE6cIFyVQWhnZiChJlSoBpHG05AAhvfh_8M8liI6OwzSniz4DkImFR9wfGW0r2bguy4yEtFXPDZkMnwW5Y0ZLSSf4FF1DWQZ0Lajhw0lLUbn-qdTXMhCAa5FztZQdx1ElUeBcvmE96MD2PutHtO6VL2Ytx5gmjTW9H3in3cW_PXg5ZYaP8II-AuqMqH2Pd9h-R2S2lRGNcB8VRRo8qQObwJWOBA-2wu6gogAuwr9cG1Xgnb8bUD4JZ-b7_5uC6irq66Croor_8qk0Z0_fOfB8RJ-HQ2OT3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رصد پرواز نظامی آمریکا به سمت شمال عراق
🔴
برای نخستین بار، یک فروند هواپیمای ترابری راهبردی C-17 Globemaster III متعلق به نیروی هوایی آمریکا به‌صورت آشکار در حال پرواز به سمت اربیل عراق مشاهده شده است.
🔴
این هواپیما که از اصلی‌ترین ستون‌های لجستیکی ارتش آمریکا به شمار می‌رود، توانایی حمل بیش از ۷۷ تن تجهیزات و محموله نظامی را دارد.
🔴
بر اساس ارزیابی‌ها، احتمال می‌رود این پرواز با هدف انتقال تجهیزات یا مهمات به نیروهای مستقر در اقلیم کردستان عراق انجام شده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137489" target="_blank">📅 15:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137488">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نیویورک تایمز: ایران در ماه‌های اخیر برای مقابله با یک حمله احتمالی، با تقویت استحکامات و ایجاد موانع و تله‌های انفجاری در اطراف برخی از تاسیسات هسته‌ای خود، آمادگی لازم را کسب کرده است. این امر، اجرای هرگونه عملیات زمینی را بسیار پرخطر می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137488" target="_blank">📅 15:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137487">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878fcc76b7.mp4?token=B-sC4z6xCSEauzKhjJthkVNYMyzDGnE9-sy9-DhTjwi0yIx2GOJYWunbuAJ7bTOYwYlg4at0dLtkciKae6CMJFJNlKCA-Hf4iDDV38tVnPmb2MErmCzATDm7D_F622N2IDNu4RUh3up8Xs-xPVAlyji6_TKbkQNWuEG909fJGAb21gKz7crtV2pYNakDDe1ffPP_e1x3bZIDQlGMX_F9PguwRIQTW1S4IEuFfuhsslY_UgkK8N_uVq8mT6pUzDPPDfwr8t1Vn2JXOyv4kjGwjG1vdhJ0mwvFPwYuA-JAJk1gNsLLIu5LIJCkJPaK0lSeSSvVxYYTbbGEXKSiq5kymQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878fcc76b7.mp4?token=B-sC4z6xCSEauzKhjJthkVNYMyzDGnE9-sy9-DhTjwi0yIx2GOJYWunbuAJ7bTOYwYlg4at0dLtkciKae6CMJFJNlKCA-Hf4iDDV38tVnPmb2MErmCzATDm7D_F622N2IDNu4RUh3up8Xs-xPVAlyji6_TKbkQNWuEG909fJGAb21gKz7crtV2pYNakDDe1ffPP_e1x3bZIDQlGMX_F9PguwRIQTW1S4IEuFfuhsslY_UgkK8N_uVq8mT6pUzDPPDfwr8t1Vn2JXOyv4kjGwjG1vdhJ0mwvFPwYuA-JAJk1gNsLLIu5LIJCkJPaK0lSeSSvVxYYTbbGEXKSiq5kymQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای که اخیراً گرفته شده‌اند، نشان می‌دهند که یک نقطه برخورد مستقیم وجود دارد. به نظر می‌رسد این نقطه، ناشی از اصابت موشک‌های بالستیک ایرانی جدید باشد که به ظاهراً به مخازن سوخت در پایگاه هوایی موفق السلطی در اردن برخورد کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137487" target="_blank">📅 15:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137486">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d777d53bf.mp4?token=hjTLiroKnKL6tiRS9xpdBvfd0WbO4AHTODFThTrY-fh1lxKNpyeu0cnW2nQRakIeZTP51UwUmjH4Yq0L9kqGuh2mGG5Kb1ZhmvknXh7Clep4RTudH0Hxd7VxYMnzG295HD0dSy46VD0GZrqbTNTEVPeJ3RBctHL59d0SPlDHakVCk8uKieeyxoBBlMAKcYMnB5-H9D6uH7JOEUTq4z26clxi-jGhvIMfETlp1KQjRCbAe28k3wC1s9b0ov7uHKeUQabtEBIgA3lFGb18JxU1-axcxKjrZ0reVG9SVJK1BoYtQL7odRVCzxMWVZGRDILkJYVkKAYn_RRmgpatbYesBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d777d53bf.mp4?token=hjTLiroKnKL6tiRS9xpdBvfd0WbO4AHTODFThTrY-fh1lxKNpyeu0cnW2nQRakIeZTP51UwUmjH4Yq0L9kqGuh2mGG5Kb1ZhmvknXh7Clep4RTudH0Hxd7VxYMnzG295HD0dSy46VD0GZrqbTNTEVPeJ3RBctHL59d0SPlDHakVCk8uKieeyxoBBlMAKcYMnB5-H9D6uH7JOEUTq4z26clxi-jGhvIMfETlp1KQjRCbAe28k3wC1s9b0ov7uHKeUQabtEBIgA3lFGb18JxU1-axcxKjrZ0reVG9SVJK1BoYtQL7odRVCzxMWVZGRDILkJYVkKAYn_RRmgpatbYesBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه با انتشار این ویدئو، آمادگی برای نبرد زمینی با ارتش آمریکا را به نمایش گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137486" target="_blank">📅 15:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137485">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75853bc80.mp4?token=lhO4N1uMtRgT-JRAMzoCZeMMFYhLeb-iOOwKZu7F3zro75ICV6e6OFSYgBD9a33m1ffI4MOTqZz2pbcwuniQx3t1Mvn_hlPao26NHWGnHXzEkwUiE1pKFECRR51jyB-w20FTKRcwb-SW094a2FjPQXD3aAD4fFR0KQvKBBdQvW87kXZ69l3xtYcIBKyjp_pOjvkd_zVNl8fceEOORRQZFkStQ4s0UhHZsLq9cx9hvFXboDN8tqwtuXo7ITeT2ns33E6RixymN29jo_JhljtjNvpVExBTfn3kD7rmb3eHJxKKXbdxn3R_9SIhj7lRlT-oHkNzdlLJGY-oJasJ_PtdOAFgdyZRXbN3CDZ6YtB8HgvLQOu3ktX6fzfa3wVaTSEIS8MJcMxwJclZqD05ylFIgXJBKxLl3l2gNm5huS0aj8bFcBtUr4G8_z-x8arJfN6OeX4yDxoUW6dYSgYrWugba5N9vK_noxZTQ4YwaRPir-Mu737rG-1yzNmY5FC9CPOVVxCRowmZHLr-WcyWhbZH1BEg1nPUwucGTN3Dm4cDHtj8BTj6UfKVhXK2S0a76Pc7TN3iNA3WLRAy-U4E4BOmUOFTaY9uVdii3wtcgLwG37GSXHQRpfb4Qxe31fWY1YJjpcgHwCB70J5YiJM6TCN-Atx049bMb8LCQz2JXuZiqMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75853bc80.mp4?token=lhO4N1uMtRgT-JRAMzoCZeMMFYhLeb-iOOwKZu7F3zro75ICV6e6OFSYgBD9a33m1ffI4MOTqZz2pbcwuniQx3t1Mvn_hlPao26NHWGnHXzEkwUiE1pKFECRR51jyB-w20FTKRcwb-SW094a2FjPQXD3aAD4fFR0KQvKBBdQvW87kXZ69l3xtYcIBKyjp_pOjvkd_zVNl8fceEOORRQZFkStQ4s0UhHZsLq9cx9hvFXboDN8tqwtuXo7ITeT2ns33E6RixymN29jo_JhljtjNvpVExBTfn3kD7rmb3eHJxKKXbdxn3R_9SIhj7lRlT-oHkNzdlLJGY-oJasJ_PtdOAFgdyZRXbN3CDZ6YtB8HgvLQOu3ktX6fzfa3wVaTSEIS8MJcMxwJclZqD05ylFIgXJBKxLl3l2gNm5huS0aj8bFcBtUr4G8_z-x8arJfN6OeX4yDxoUW6dYSgYrWugba5N9vK_noxZTQ4YwaRPir-Mu737rG-1yzNmY5FC9CPOVVxCRowmZHLr-WcyWhbZH1BEg1nPUwucGTN3Dm4cDHtj8BTj6UfKVhXK2S0a76Pc7TN3iNA3WLRAy-U4E4BOmUOFTaY9uVdii3wtcgLwG37GSXHQRpfb4Qxe31fWY1YJjpcgHwCB70J5YiJM6TCN-Atx049bMb8LCQz2JXuZiqMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف بنزین در اربیل، طبق گزارش ٩٠ درصد پمپ بنزین ها بنزین تموم کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137485" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137484">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رسانه‌های لبنانی از حمله توپخانه‌ای اسرائیل به کفرتبنیت در جنوب لبنان خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137484" target="_blank">📅 15:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137483">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
آنتونیو گوترس، دبیرکل سازمان ملل متحد: نقض‌های اسرائیل در منطقه جولان سوریه غیرقابل قبول است.
🔴
جولان، خاک سوریه است و سازمان ملل متحد از تمامیت ارضی، استقلال و حاکمیت خاک سوریه حمایت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137483" target="_blank">📅 15:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137482">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
آکسیوس خبری درباره آتش بس منتشر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137482" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137481">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وزارت بهداشت: در سال ۱۴۰۴، ۴۹ مورد ابتلا به تب کریمه کنگو و ۵ مورد مرگ ناشی از آن در هرمزگان، فارس، کرمان و اصفهان گزارش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137481" target="_blank">📅 15:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137480">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نیویورک پست:ایالات متحده در حال بررسی طرحی برای تصرف اورانیوم غنی‌شده از تاسیسات هسته‌ای ایران است.
🔴
جوزف رودجرز، معاون مدیر مرکز مطالعات استراتژیک و بین‌المللی، گفت: "متاسفم که این را می‌گویم، اما به نظر من محتمل‌ترین راه، اعزام هزاران نیروی زمینی به تاسیسات هسته‌ای ایران است - با در نظر گرفتن تله‌های انفجاری، استفاده از تیم‌های ساختمانی و حفظ یک نیروی دفاعی بزرگ که اطراف این مکان‌ها را محاصره کند.
🔴
از آنجا، یک تیم کوچک از نیروهای ویژه، عملیات واقعی تصرف را انجام خواهد داد - که عملیاتی "بسیار خطرناک"، از نظر لجستیکی پیچیده و در یک محیط پر تنش، دشوار است. ارتش ایران تا حد زیادی نابود شده است، اما هنوز از نظر تجهیزات، پیشرفته‌تر از نیروهایی است که مادورو را محافظت می‌کردند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137480" target="_blank">📅 15:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137479">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO8AVzHsABkEf2BsebM-u-ROFw14tWna8TM4EbhHQFcetcDxWmYGAfG7eO6W5xTMYHZ0UWZlw7NLcSAeh8Lux79KiQA3MTmAB_QVoNlPaocugcEPgJQ9j79AYdCddDv6PEUIED4PdI3AehWMgpbxKoMc7BqiMjM28S3GNTIpfKqfFcsJGI7UOAG8-hze7WUX0yM835-I1IQmOTZmxEe5CBjQk6C_16yhPwwbbj7IDCdl9ojXo6Kq_RJbui6jo2Trb_g5RB75JoOpG5Pcfc84kzuuzc5_PRRO16byS31ZHfXdSG7ruAlHdo0jZzXce3zpky-1mmFNiQowsfzCCgg6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخورد دو اتوبوس مسافربری در مسیر دیر الزور- دمشق در سوریه باعث کشته شدن ۱۹ نفر و زخمی شدن ۲۷ نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137479" target="_blank">📅 15:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137478">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/entDWYFI7SPLuyR1i9rweZlBptxZv8rikO1M5mYemB0ikASRIzwNNrmQ6bSdABuMdgEKYIkg5lx4cNAetsaPXqN5Fdz8uhyAnrSEnaQT9DhcKDA7HVwuVPBdCQpY4tO86zsmvHn2hNMCv_R-le8xzb82iI6BMK38uEhK8whoV2hf396m6Lv9FGe3SfOgNT_IRGBFL8DcKuFis-3uoxBgqEyisyZX03YE4KLGomIM7Q9SY9ippepesSg9mgDmNsV3fANXTCg9x8WqZ2END_TfSO3ze8TfkyzG8_3r4p7Eeo2HX1QEwnJtaWmE3SzFn3NDs9tWldtdvbht0VwPmcTIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: اگه وزیر نبودم میرفتم پشت لانچر
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137478" target="_blank">📅 15:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137477">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a782cab2.mp4?token=V1oD-uQbYbk4UZ9jSqJEzRVZ5ee2p5KyoC9jKdXHHe5R43VK8-V_elMReM7K_TFR81QRPncJTsz6fU6A8nPunRkS8lcV3IPeFEIuOnBZxjwYW2lYJgY3eg80yLrvbxAByjRCSZk-pkRvN03_YuX6yXLmKdre6teauYJMzajk0je1kx1v6ZT7WmR0QqF9652RKVzL9CifC1rZJp8L-NyoQ0Kzc7Lz4uQNLQCmFijykKqJ46NRylpVvQ1RZZ1YZH8Ue_2nNguAOS1U5t-cuioy4bDe0BelulLimO2NJjdFuIDyPiG1yew2q7yTGGIjBZXkB_voxNU26MTSFDMfsCcN0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a782cab2.mp4?token=V1oD-uQbYbk4UZ9jSqJEzRVZ5ee2p5KyoC9jKdXHHe5R43VK8-V_elMReM7K_TFR81QRPncJTsz6fU6A8nPunRkS8lcV3IPeFEIuOnBZxjwYW2lYJgY3eg80yLrvbxAByjRCSZk-pkRvN03_YuX6yXLmKdre6teauYJMzajk0je1kx1v6ZT7WmR0QqF9652RKVzL9CifC1rZJp8L-NyoQ0Kzc7Lz4uQNLQCmFijykKqJ46NRylpVvQ1RZZ1YZH8Ue_2nNguAOS1U5t-cuioy4bDe0BelulLimO2NJjdFuIDyPiG1yew2q7yTGGIjBZXkB_voxNU26MTSFDMfsCcN0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ثابتی: بعد از جنگ با عرب‌ها کار داریم و نباید اجازه دهیم تنگه هرمز را از طریق خاک خودشان دور بزنند
🔴
شهریاری، عضو کمیسیون امنیت ملی مجلس: به چه حقی؟
🔴
ثابتی: چون قدرت داریم و رئالیست هستیم!
🔴
شهریاری: خدا نکنه قدرتِ آمریکا دست شماها بیفته وگرنه پدر دنیا رو درمی‌آوردین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137477" target="_blank">📅 15:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137476">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وال استریت ژورنال: موشک‌های خیبرشکن ایرانی با ترکیبی از مسیر‌های پروازی، مانور‌ها و سرعت‌ها، سامانه‌های پدافند هوایی را گیج می‌کنند
🔴
تهران از این موشک‌ها در حملات پیچیده استفاده می‌کند
🔴
خیبرشکن‌ها می‌توانند مسیر خود را بیش از برخی موشک‌های بالستیک دیگر تغییر دهند تا تشخیص آن‌ها دشوارتر شود
🔴
این موشک‌ها همچنین بسیار ارزان‌تر از رهگیرهایی هستند که برای انهدام آن‌ها استفاده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137476" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2877734558.mp4?token=nL0tjJjogezJgNhuhskX4_1Lw3JuXW_CmcYwOYQXvEYVII6CchICdOd-vWvnbyMLDCzQBC91bUeOa8lzQheZr29PfrCnvWx3_UH4twIhqYmPNZhUVXnAKA6YuOtb2lhghH3lnlM7-HCsSq6_7luBidgApkh2MbZHWnxKFsb9MvsloqyYItuV6xZS0QVpnGY6eSaKIjDr8csAJ07AtXSTVcfXGxncqwT9QZch_FoFNU8MQBSdHg_s9sTA04SV2RK0V_AnTrEeymxNm8fGx_vDV4Nquw2ysfbRGf67BFk_Ot8kXwQ4c74heQDRlRztg39MKmefD4GVWm4CTCAtoPMshQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2877734558.mp4?token=nL0tjJjogezJgNhuhskX4_1Lw3JuXW_CmcYwOYQXvEYVII6CchICdOd-vWvnbyMLDCzQBC91bUeOa8lzQheZr29PfrCnvWx3_UH4twIhqYmPNZhUVXnAKA6YuOtb2lhghH3lnlM7-HCsSq6_7luBidgApkh2MbZHWnxKFsb9MvsloqyYItuV6xZS0QVpnGY6eSaKIjDr8csAJ07AtXSTVcfXGxncqwT9QZch_FoFNU8MQBSdHg_s9sTA04SV2RK0V_AnTrEeymxNm8fGx_vDV4Nquw2ysfbRGf67BFk_Ot8kXwQ4c74heQDRlRztg39MKmefD4GVWm4CTCAtoPMshQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: اهالی جاسک اسلحه‌ به‌ دست منتظر آمدن نیروهای آمریکایی هستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/137475" target="_blank">📅 14:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137474">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAPnCowLEAzsz85SUmbTL6e1niTR8OvAajhuFzA2tEZ3hZc4G_EBubkm7Fj9f7zBWeaDVH42gcKK5hFrDjjp3F5SylwPxWEK51RRcjPwZCvc1mnfsS5r8i5PDADxzm1zOQRIWllIS3hM7FVXS6FpKUB2RWmI7C8IEFXtTQC4S23pAj2AhdVRcggx1_moleND_OIEKQZdo0IzmmYbFXW-78g1FOO6aGQCqKvxsDV_BIL-QzmTbUJtST6f2OCZNtovq2d7ivkDGcvH_YSoRN2zpm1EuEecsNvUXc5dfVtwkQLHoy6jSKZ0ScAmaM-ZBazqIbPrP7GRjtRTFUUIp4G4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آموزش تیراندازی با سلاح به کودکان در میدان آزادی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/137474" target="_blank">📅 14:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137473">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjJwtu91LTVifa42C84OdtHz98U6dQ3ujFenu_OJdYWcEJ8SRWF4IaDgsAhf8EkWTWpxFo58lGgTZi4PbCbO_G62P3hBZMw5Xg6nxmoSRmVFq6daojFZladt9JP8RqxHDrrJh1AHYDli4y1Fe5g1THj6ou4Q29x3sv3ZDVrmKSYM_1k-wwapTfwc93O_Jgpgy_6FxNzuTiI8kGFSjfHo1UzCsV0Y6AedvDOs1hcnG_jE3ds2E8X8DHd9a9Mll3Q_YdSE3pclqfi-07Wbi0aGinuyxw-aJPLB74dIgVPT6nx9IXoJpM4nSbO3RMH6Db-dHFQ7BYlm7X6bKSNwRLO6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه لبنانی المدن مدعی شد: بحرین و کویت از محمد جولانی،خواسته‌اند در صورت وقوع جنگ زمینی با ایران، نیروهای این گروه را به جنگ اعزام کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137473" target="_blank">📅 14:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137472">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
صداوسیما: در ۲۴ ساعت گذشته ۴ کشتی با شلیک اخطار نیروی دریایی سپاه متوقف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137472" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137471">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9eae7c3a.mp4?token=T4JoR7ZyzHyM6-HxjVKgPcvfdybKqyHrwhUUOR8GmASbun3ce0P88d93drQgHue5Rz4h9KUxM2La6qwqheayh8AdP6G37BPHB7lj6xIEBGM_lyA3U0ll1CpR0RjnsgsNiaManW7ymnPybuAi09jU3jPz-HkH3GeNbTnisnNsQEJDDv738XKpwOybhBkp8GnylfKEQqLi1vNXin7uszN6ABD_3tNR_RhllSQn-7wXhuYQk37uM8IZ4drhjVxY8iqqDCA8VkFlitkF3LXReGBZ3Kl7MkzEAtwtBbKls28UjxGDgL_pYUVQJULLxTmnNQMkK4XMYwb8k7jgNpC69sHHqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9eae7c3a.mp4?token=T4JoR7ZyzHyM6-HxjVKgPcvfdybKqyHrwhUUOR8GmASbun3ce0P88d93drQgHue5Rz4h9KUxM2La6qwqheayh8AdP6G37BPHB7lj6xIEBGM_lyA3U0ll1CpR0RjnsgsNiaManW7ymnPybuAi09jU3jPz-HkH3GeNbTnisnNsQEJDDv738XKpwOybhBkp8GnylfKEQqLi1vNXin7uszN6ABD_3tNR_RhllSQn-7wXhuYQk37uM8IZ4drhjVxY8iqqDCA8VkFlitkF3LXReGBZ3Kl7MkzEAtwtBbKls28UjxGDgL_pYUVQJULLxTmnNQMkK4XMYwb8k7jgNpC69sHHqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
الجزیره: ایران بانک اهداف جدیدی در داخل اسرائیل تهیه کرده است/اهداف جدید از نوعی خواهند بود که تعمیر یا بازسازی آنها برای سال‌ها غیرممکن خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137471" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137467">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqAriM3Sabi7Wxaha64u0i0EEU8A4EXgaqvl-Wb_tE00zOmN02ute8u2jj_un5_cpaaul6uiDFUzrypYH0pwQjF9cnWFkE-sjR3PHSPb6W2JR13Z0whgqQPxUkZSKhu29Yf-4pyf7LBdGDSKfYK3Ke7SaPe2HiayoZZ5V00d7EQvmtrDR7cka1SHsQQ9RAAJBy2cfbDPbp6AHPXbiutRFiru3-vSJLs3Ir9pxTvEeLJzbRPtpTfO9bFXO-_hcUGRb-v0_rQKkS9d2vma0J9nYRveVfV82UrpnEU1zHHXuwTSKboL4wnTvuzMb9IP9Q_doK_5xKxwRYQ7YtZhSRTgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4ku3c2Jeey6VW64AxLl4OjVFtvmeZ0xqaxp3bBkIRVE6ZIQFpphZu-OSkPEsxyKWmEY52rwECNFaTeCLB-l7ThyFeVg3Z2BuD39UfMJDi4ANrQYnlmPjMi49V6K-gY5snssXucqYdY6Jde3Y26gf0BR_IiQu3_xFQaqtUx5C0o2x-266U9Koxbbew4z_RE27X3z3xf0v_G6myqvQp6pbYshXw7VRy_gvCz-BZu3oR4V9sEC11GJ7d6jvLaT6mZvbaTjXvzbJoFJsaZ5Y4mgahj8Ed6xBajBN_dWOADC1J1o8pzsmXXMR_vo80M3_AoffUnm_suRLZmOMxd5NG3B-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdwNmRXROr0Q6meXQO97Nl5it9_D6Xks6GFruJAFlU7_w6Z9FPSby0RqEv-njjT3P2vD1WrrjSR7mtyqSpsBcSTl7xhAyITtYAuepXWisajH9GEkRrosTeAjCCGfDJ7oz9WIEbj4W7C2lWohGbF03LWvtSzHomWvP3P4vpjocH1V9fhh0yJPz0Ik5Lt2fsMFA02EoIT_nW-mZebGhyKwoUtOQDeDoE141TBrzXrxQGCXbJGxlObWJ8x5J-1JiZNWe-O92J3GlaoUsNf1XdqhCjWrT8GrxqNbsFGzvL4kE4wrIzSRwwAXpmEKKc9QAwVS8GHbTrMkffUGA54jadN2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2FoSK4bwpriq8h1cRjB4GPDfE0T0BNogGOG7TBbCnf7drSHzflW898RGIGKSo86MfCPSOfQPgfB7LSwV_D-obviyfNLGVkyBWIpVZrh3MhwfWjiiFLadeG5bstyurshe1VxDgEryiDmdcRSrdvoONA7D74IxGQx3j7iCYWQvBKkUEtUR6aiDJKSODq_NcAZUgFH6P-n80nddncF6N1aeJJrG6Lr80kU6Xs9a3HZgJwS0SS-wFGL5sdCWY5GIuuk253HKvdDD-l7V4tDbitdfEz5D_rUTTeoxMzJMbUjHmljP81Sg8eZC9TVgy3-_XxPP6pUIqq5Um4hD6fDM5dSXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از دونالد ترامپ در مراسم شب گذشته ضیافت شام با خبرنگاران در هتل والدورف آستوریا
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137467" target="_blank">📅 14:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137466">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ثابتی: بعد از جنگ با عرب‌ها کار داریم و نباید اجازه دهیم تنگه هرمز را از طریق خاک خودشان دور بزنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137466" target="_blank">📅 14:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137465">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
شرکت هواپیمایی ایتالیایی ITA، پروازهای خود به اسرائیل را، از جمله پروازهای فردا، لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137465" target="_blank">📅 14:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137464">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سفیر کویت در آمریکا در واکنش به خبر وال استریت ژورنال: «دولت کویت در هیچ گونه عملیات نظامی علیه ایران شرکت نکرده است و نیز اجازه نداده است که از خاک آن برای انجام عملیات تهاجمی علیه هیچ یک از کشورهای همسایه استفاده شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137464" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137463">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCMtpFXjUFibtblof8PTomT86GqJpiRP0mb3zeUPH7HRPfm2KxWI4zRbpcSid4HjQu7aZIvKdRZjHZaG4xHGV_p_Om47xTKM6pjvxtXg_Ww-r-dK8aROqcsI0vrOu2XnTLLz5YBfsp6fd0bHg0TBPLzUvBh3I-vdg6Pf1W14M5kAtvos2ZA-EX5DXYhCB5_xFLdV3al8NIPjxGg0ur9ZJtpzo3npDgugn_1XU1N1juhZr9ewBPDFSGWpT8QaSZpqBEFo4wHlzsxM0VJspJk5TKcIxaTAcaTqtRGyT595U53wFSnhxko0bDEFsC71XxaandEJYsIqDzE96g6Szt36Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شیخ خطیب، رئیس مجلس اعلای اسلامی شیعیان لبنان: فریب آمریکا و اسرائیل را نخوریم، به ایران تکیه می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137463" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137462">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
دولت آلمان ۲ فروند شناور نیروی دریایی خود را که برای مشارکت احتمالی در ماموریت بین‌المللی تامین امنیت تنگه هرمز در حالت آماده‌باش قرار داشتند، از خلیج عدن خارج و به دریای مدیترانه منتقل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137462" target="_blank">📅 14:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137461">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
خبرنگار العربیه: وضعیت کشتیرانی در تنگه باب‌المندب به‌صورت عادی در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137461" target="_blank">📅 13:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137460">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نیرو های دفاعی اسرائیل هم اکنون در حال ورود به شهرک ها و روستا های کرانه باختری فلسطین هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137460" target="_blank">📅 13:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137459">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
زلنسکی : کشتی‌هایی رو توی دریای خزر هدف قرار دادیم
🔴
اونا محموله‌های نظامی مرتبط با ایران رو جابه‌جا می‌کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/137459" target="_blank">📅 13:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137457">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/994ea698fa.mp4?token=G59eJecGB9-Pkdet6d12opEmgm9I6rS0lHLAwEsEndTUkOHB1py2h7Lp_TicpWz96MsNUGs6-FlD2KYYVgBopTHKa0gHjWdK4jvhGfqLmDW521tLfysHy2iXMF74luhd3LY3maePR0OyVj3eqrqyURMd3Q8V_KBuODTyuCSeYxQS92B9EUfXF44zJByjBQzucmCebFPOresmDaUq_G9fpxSGJDXYOYj66yoGPjz5W7QLBbJV82d-8Befrz8AT7WYqGHDwK3rEuWxao3vFO2_K2qeENT4T2YGAA_K6dDNFPtMyDenTy9Gz8OoyrfGuo2cHePOIC7UXIFCSIJB3E13pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/994ea698fa.mp4?token=G59eJecGB9-Pkdet6d12opEmgm9I6rS0lHLAwEsEndTUkOHB1py2h7Lp_TicpWz96MsNUGs6-FlD2KYYVgBopTHKa0gHjWdK4jvhGfqLmDW521tLfysHy2iXMF74luhd3LY3maePR0OyVj3eqrqyURMd3Q8V_KBuODTyuCSeYxQS92B9EUfXF44zJByjBQzucmCebFPOresmDaUq_G9fpxSGJDXYOYj66yoGPjz5W7QLBbJV82d-8Befrz8AT7WYqGHDwK3rEuWxao3vFO2_K2qeENT4T2YGAA_K6dDNFPtMyDenTy9Gz8OoyrfGuo2cHePOIC7UXIFCSIJB3E13pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل در آنکارا حادثه آفرید
🔴
بارندگی شدید در آنکارا باعث ریزش بخشی از یک خیابان شد و خودروی در حال حرکت به داخل گودال سقوط کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137457" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137456">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
اخبار حاکی از حملات سعودی به منطقه مأرب در یمن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137456" target="_blank">📅 13:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137455">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rX1cUYZI-Ux_rJuvba9E2GAKLlgbU3CUKfHwsdasR-u_w_o_KCtc1cBKPXEYny4KMoi6iFfpDTQdjA5ufSvxEBwPfRsYBxJFUbuEC9dKO5ApgDHJQzcMXj5LJ964aYsvj4NQd0jPzK6xcMFVQ_-7QUq9TPovlaE5-bykPV4g8r9i3xwVqTjip28DLMw3tpeTjs82Us3BGcx9bHLrVzK7MxZS0sSBKfZPFElfwHzVQ3CJk1JPNSySjRlqV9fndrhL5VVfBQV9RAHRhjDnaI6Dq5vFL2BhbJdyU4USg9i1v5KP64aJ8QNP9WTpvL0-qDHbJX-8AYS9jWxFOPLs4M6CIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی: هر ستون دود در منطقه، یعنی هدف قرار گرفتن یک مرکز نظامی یا امنیتی و یا مالی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137455" target="_blank">📅 13:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137454">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
روسیه گردشگران خارجی را برای جنگ در اوکراین به خدمت می‌گیرد
🔴
رسانه های اوکراینی  مدعی شده است که روسیه از یک روش جدید برای جذب نیروی انسانی استفاده می‌کند؛ به این صورت که برخی اتباع خارجی با وعده کار یا سفر وارد روسیه شده، اما پس از ضبط مدارک هویتی، در برابر انتخابی اجباری قرار می‌گیرند: پیوستن به ارتش یا ناتوانی در بازگشت به کشورشان.
🔴
بر اساس این گزارش، این افراد عمدتاً از کشورهای در حال توسعه هستند و پس از امضای قرارداد، به مناطق جنگی در اوکراین اعزام می‌شوند. همچنین ادعا شده که برخی از این نیروها بدون اطلاع کامل از ماهیت مأموریت خود، وارد چرخه جذب شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137454" target="_blank">📅 13:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137453">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=McUqpLEbIDzlpkskt9E2LD6WBINzaJz3A9FCDbWmcV-6Wf_xJdZRie5pNEnuwpakopAoSJ13hq9V1mN95U_Z5Sh8i-JPVg61BRYSqx2nerFq1137rEpFIPCmkAN5wUuHFIixeS1LWTlY1fMz-soIce5SPLUbWNmh8YqIepXumU2eHHMNcvkX-EoF6EwWxDS68pRZYwyKQjQSHWUE7xgy6ClIJLzy3X2xDJJ0jNuWnhqCribPd1Z7JECN1QE7cpoFoTrMUUyWfzkEj_amaO_Rvw90IX1erbBnUn0a_GDk8OA_7W_zf1J0nlvYZ5K7a3GiR_JJKXUbPGV4No9G5gNPoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=McUqpLEbIDzlpkskt9E2LD6WBINzaJz3A9FCDbWmcV-6Wf_xJdZRie5pNEnuwpakopAoSJ13hq9V1mN95U_Z5Sh8i-JPVg61BRYSqx2nerFq1137rEpFIPCmkAN5wUuHFIixeS1LWTlY1fMz-soIce5SPLUbWNmh8YqIepXumU2eHHMNcvkX-EoF6EwWxDS68pRZYwyKQjQSHWUE7xgy6ClIJLzy3X2xDJJ0jNuWnhqCribPd1Z7JECN1QE7cpoFoTrMUUyWfzkEj_amaO_Rvw90IX1erbBnUn0a_GDk8OA_7W_zf1J0nlvYZ5K7a3GiR_JJKXUbPGV4No9G5gNPoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: تغییر قیمت یا سهمیه بنزین قطعی است
‏
🔴
مبلغ کالابرگ افزایش نمی‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137453" target="_blank">📅 13:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137452">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
اخبار حاکی از حملات سعودی به منطقه مأرب در یمن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137452" target="_blank">📅 13:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137451">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
خبرگزاری های داخلی از یک برخورد دیگه به ساختمان مرکز داده‌های شرکت آمازون در بحرین خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137451" target="_blank">📅 13:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137450">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
شرکت ملی فراورده های نفتی: سوخت کم داریم، مردم از حمل و نقل عمومی استفاده کنند و در مصرف سوخت صرفه جویی کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137450" target="_blank">📅 13:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137449">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8vX-mViBUResNYzZaQHXDXCcqVo38egQVd7l4iPW5MpYdCMjjxw25bcAX_11kNdJnW-NGLjDLglCL2w-8sF1y_fl64ta1rNyWNl5bSpw4bsu4Dinq_EXfhoNrtAT22E5PJc7hjq-Rjb7VA3JehXEHH79A2WqWhJAvdyUr9evXRtK0iAs7vYqn373qJF8HC0hevRNw6oWfRpWX3xz4el3ZtNZuyOe4VSPXWBHyA4odXqiRHmlKx5KZYOC7SJKanZ3ouKkv4jIR44ued6lp-8_VB_UTnqhvnm3KkoXU8eXsOwAb3Zk3QoIWPjH6cxygAjQK6RE_y5TTmszDKKyxvaKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال جهانی در سرویس ChatGPT گزارش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/137449" target="_blank">📅 13:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137448">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqZkJVlPT76FqFOAyYOlIsYQLTX_hmrsmUXzepcGjbM77Iio_6jU8v4kSW23M6t24lltREsRTdz1GEKpuF-Rw3fho2RuvJPDYIdP9Vcvv1wSyc3Q8HR_rjEuH1XRakEL5Dv6CeGy6Uf0ijK4MJiCxO_VLEEC99L3_RfXN5SABdLX0CSwRcwaUVufSuCHCktmB8lx8LtOa6JxGxN8r2tpuFGyg5juzwy6kEHc5ej6iVC44KNWUDq59HAxq3GP7n5-0GPHL6zFdYEnfo-KcrtjpJUHfGNOOCx4_kW9lfIk8-UGmoO-_wp8lxgjjfB-m9oF_4-kxZhkAgecIQadqKlKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیکوشور دان، رئیس‌جمهور رومانی:
این صبح، ساعت 8:30، یک پهپاد جدید در حریم هوایی رومانی، در فاصله 10 کیلومتری غرب شهر سنت جورجه (در دلتای دانوب) سرنگون شد. این پهپاد توسط یک خلبان رومانیایی از یک هواپیمای F-16 مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137448" target="_blank">📅 13:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137447">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وای نت به نقل از مقامات اسرائیلی: بعد از آزادسازی تمامی گروگان ها، دست اسرائیل برای انجام ترورهای هدفمند در غزه زیاد شده و اینکار با شتاب بیشتری انجام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137447" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137446">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFxs3M9EYZbs-UNyreqCVCxfg3CV7R7DBKeuAym7U8loj0YE78KMfQQKuXBcKOOovkMxvgx6VoYqm-oxe49_MGHLRTru8lNL9KqYvhHWFufIJ3Gvzan94zmUpeu3UJO3B3WrahsxETtccA5QyrM7kI7llbd-olDEnUklySW3-7jWfFcASI0K1O0lLjBcE7uHnlC7KyzRaPRe7aR-DbK-D1qExdPpqJHWJ4X2isd6QLOyAfsvyXTSedHSTOJw2FmQ4bmlSx76BpFM8SB4kk35b7ROprUKGRJX8RT5mv57_YTs1HCNnQ3U3ZGHXgyunzUiGiKohPFY_yKMbqS2oDty4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره : چراغ سبز عراقچی به شروع مذاکرات
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137446" target="_blank">📅 13:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137445">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8394759b84.mp4?token=d3bbkwLsEgp0521f8eGRxTSrw3IYlhdQ5yL6l4JCQpy4v6dTZlP8YOJ0uWqh8KjdUMrTg3rVUGaH41hpvCr85E9StsMR5cwltuaiHGqFL7Kp9UwrMQDd3fWZLXOMnWPReHgxHiI_fLu3YOMH4GEUfe4nLjue_nIvYFOhGJITj_bEr-dU4GPGsdunLO_DnnjcS76ughG2FnlVIGL6hvoxjWtNton163unyvaB0SpIUEwiQVlVRZUkF2yymdj0pLqGGK2LLDNyPhCAmWS0lVD2c6_KYUx_xTA0_KYAc8qESl5gD8chqT3yl1plucFtuB4F0A0GCIs4lB4jVD02QxAIfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8394759b84.mp4?token=d3bbkwLsEgp0521f8eGRxTSrw3IYlhdQ5yL6l4JCQpy4v6dTZlP8YOJ0uWqh8KjdUMrTg3rVUGaH41hpvCr85E9StsMR5cwltuaiHGqFL7Kp9UwrMQDd3fWZLXOMnWPReHgxHiI_fLu3YOMH4GEUfe4nLjue_nIvYFOhGJITj_bEr-dU4GPGsdunLO_DnnjcS76ughG2FnlVIGL6hvoxjWtNton163unyvaB0SpIUEwiQVlVRZUkF2yymdj0pLqGGK2LLDNyPhCAmWS0lVD2c6_KYUx_xTA0_KYAc8qESl5gD8chqT3yl1plucFtuB4F0A0GCIs4lB4jVD02QxAIfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درحالی که یه سکوت عجیبی تو خاورمیانه حاکم شده؛ ارتش آمریکا داره خودش رو برای هر سناریویی تو خاورمیانه آماده می‌کنه، به همین خاطر، تعدادی بمب‌افکن B-2 در حالت آماده‌باش کامل قرار گرفتن و هواپیماهای سوخت‌رسان بیشتری هم به منطقه اعزام شدن تا اگه لازم شد؛  عملیات هوایی طولانی‌مدت راحت‌تر انجام بشه. گزارش‌ها همچنین از تقویت حضور نظامی آمریکا در منطقه خبر میدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137445" target="_blank">📅 13:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137444">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سخنگوی انصارالله یمن: محاصره دریایی عربستان، اولین گام در نبرد محاصره در برابر محاصره است
🔴
ریاض از هر نظر به اسرائیل شباهت دارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137444" target="_blank">📅 13:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137443">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce10267406.mp4?token=Sx8OeI1WHYftYYR7649esIayUL1KXn7xTq3nVBknAD1KNl71CdhEeqJf40kh0q7CBBTNdtdpFJjmye4g1sltOLvYsfhuxLfl1ZzgBvJG9ky6H-z7sxT80ueJLJK52dAXwopg1_JyOABdnryLG-giorJ3VkJB5smWzlgGhN2zVQERNQ5sAyN0YkP2xeJdYp7n8C6s55kdjow7cBy0TdLBTnV_fbkyat9SLdSvqLzZPL35eAAtNY8ZOQQAVV3pPxNR2LFUfjYp2yCzruVUCqBpcvwhihEPs_nyDgv2vBTTbkKmdHVmsbKeO_wRS2itf2VrotpjBRpE23I7c-P710viTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce10267406.mp4?token=Sx8OeI1WHYftYYR7649esIayUL1KXn7xTq3nVBknAD1KNl71CdhEeqJf40kh0q7CBBTNdtdpFJjmye4g1sltOLvYsfhuxLfl1ZzgBvJG9ky6H-z7sxT80ueJLJK52dAXwopg1_JyOABdnryLG-giorJ3VkJB5smWzlgGhN2zVQERNQ5sAyN0YkP2xeJdYp7n8C6s55kdjow7cBy0TdLBTnV_fbkyat9SLdSvqLzZPL35eAAtNY8ZOQQAVV3pPxNR2LFUfjYp2yCzruVUCqBpcvwhihEPs_nyDgv2vBTTbkKmdHVmsbKeO_wRS2itf2VrotpjBRpE23I7c-P710viTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
یان دیومانده:
الگوی من کریستیانو رونالدوئه.
- مسی یا رونالدو؟
🎙️
یان دیومانده:
مسی قطعا.
@AloSport</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137443" target="_blank">📅 13:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137442">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ادعای تلگراف: جمهوری‌اسلامی از شبکه‌های قاچاق انسان برای انتقال عوامل خود (نیروهای انقلابی) به بریتانیا استفاده می کند تا تو خاک این کشور عملیات ترور انجام دهند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137442" target="_blank">📅 13:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137441">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83b077ce4.mp4?token=YkRAM8f4pzf6SsSxCPJXaiuTGRj_UtG8D570donBLO_DmAVzVEHC-QTB-r1XIlUj2tFaepHktNjzcPzqdDeCs_4oFJfSDr4zrkfW437SRvcU9n0RZyW17x2K0N4BFfMZ-n6j8bZy_Z12P8LxCz025FcjVyata-mPNwtDZX1rDpljozkOTs_KLXigWUQMQbmmG67dHTi9iKWfLs7NyEQuwci84SxPdLp2nPznuQiXx-wphO08Y1C_BcTmhVS5l30769TlbzpTdd8A38n6vQ1mdNwGftbwJSzNFPHJKnGMCes8lxMYm_7-i63RIpxrb-9NBPg8lULsdbblOB1lhUGwhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83b077ce4.mp4?token=YkRAM8f4pzf6SsSxCPJXaiuTGRj_UtG8D570donBLO_DmAVzVEHC-QTB-r1XIlUj2tFaepHktNjzcPzqdDeCs_4oFJfSDr4zrkfW437SRvcU9n0RZyW17x2K0N4BFfMZ-n6j8bZy_Z12P8LxCz025FcjVyata-mPNwtDZX1rDpljozkOTs_KLXigWUQMQbmmG67dHTi9iKWfLs7NyEQuwci84SxPdLp2nPznuQiXx-wphO08Y1C_BcTmhVS5l30769TlbzpTdd8A38n6vQ1mdNwGftbwJSzNFPHJKnGMCes8lxMYm_7-i63RIpxrb-9NBPg8lULsdbblOB1lhUGwhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حرف های استاد اکبر عبدی رو باید طلا گرفت.
🔴
همیشه سیاست های دینی و ایدولوژی جمهوری اسلامی باعث شد که این هنرمندان نتونن به حق واقعی خودشون برسن.
💔
روحش شاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137441" target="_blank">📅 13:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137440">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
عراقچی: صداوسیما هیچ‌ یک از مصاحبه‌های مهم من را پخش نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137440" target="_blank">📅 13:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137437">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZL7YeIG7KacqWaRJsuM6XdTaPPngWVMtB2YOWgWaCt37elOjS1qmXat9aT3l7jIj_f53KbnrCDTLT9EXE6WFQkrkPuEy5RhAaBpTAUZ_eVwryN3HcEUSfYv3BQhkfzSABuBxvr2AfZo1_pjlOQmDd32edZeSMgoqAFu5sAJ8tPGAHkyP5tlCOSJpV8ahwhtXnEtIyKSq5io9Kwa2C_q_L3b1XgKE7OLSGLfJEp-FI51vCHmaNhRtuIr7MCBO4Tpoh9qBEhR3CHhNG6uIhWRNajihoO5FyiS5pPtuKeKKPhvvQkr5ncZEogGXW1qDo7nCGUb-ya7cYIbarr8fUQAFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1LfRP0HC1WA5mOey68MuickqfPftHSdWWIidSSWSZGRqIXLRu_oZJvBKcvH5lH7EkZ26mwZD9yS4ICZRfzHU4NX1TED9WUYOWQ_CcP4-68FbZc4I9_7lgDpTsr8LeT3tutNi9ElZ6xq46jyXTot-kbpTwRthTQPcj5z-UoEkMworvZqZhnIAqB4INE2Um_H4oUJfHnt6152VN2B12NutyISptNiQ54NPULrwS97c05vQq27i15YGdkOaCnRQeibK3h3uEtLwgTIgqjNhKBhPNzAXHOV0jKVka08XFYTJAslOosN055jvkrKva3nWIu79YjVJfuQpD2slytglZfxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1gvcoKOmtnXY7Zcm2Mx0leFBN083eyubWnC8h78A0Pv3Dk5V7m8v0OqSDDHDVyk3KxtY2kl6ZnHnrSJp4DL-6VguQoCz8WFjB84c-sCM3e0E6L0rnASPiDGioWsh5pjTiu1fHXjivgRPt_cDaZUj_sPdkDvy16EoxtE4qdNTp5iuF7e9XCwGuK0Jnud1sKsQpVlGxwk5fqpHR3sFlcl33K4XxoZUKuhG9ZhCJkJ8VAmQy-X-eLlnKAV3HD08L5FsbK6dt1QmrzfLMLOpzr7InGD8KJD4kmIqJptkGcos_HLLiQiHNOQgo4-yX-ACETx5MrDn5-RkiyP737XqCnv0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از انهدام کامل سوله مهمات نیروهای ویژه ارتش امریکا -پایگاه ملک فیصل، اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/137437" target="_blank">📅 13:01 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
