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
<img src="https://cdn4.telesco.pe/file/KGLweOkIemECS-0TQp20LXRBnaiAcZU23X-6SZkxkslwiU_Tfjw3StoDzbRdHcHxxGueun7KLrT2Y-HFVp8m0edc8-HcZpPzu53UYWooddtKyhTJ3i0uL9zG4pQ6t7Ina2OaAszvdklbqHYAqzfOD_EsuXzgAyBEghe-6WFPDX4eteoW_TQXs--w8F3ZCTo27diQoGm1W4-5cykpbcxZVZw-5UuFUFB8MntJeKWzQloj-zKV9Q7M3eHygbW4XrZ3-gMpeTq-vdHkgY8Su9h0RGvfRhW1dVBRdf8w25cPNEsurX3k3UcVlBmfr0zC3zPFbhMp5UdLsUl6-n88HVVsoQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 288K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-13383">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">️بیانیه نیروی دریایی ایران:
فقط مسیر تعیین‌شده ایران برای تردد امن در خلیج فارس است / شناورهای متخلف هدف قرار می‌گیرند
@withyashar</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/withyashar/13383" target="_blank">📅 15:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13382">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ : ما خیلی خوب با هم کار کردیم. من «بی‌بی» رو خیلی دوست دارم و همکاری خیلی خوبی باهاش داشتم
می‌دونی، ما تو شرایطی بودیم که اون نخست‌وزیر زمان جنگه و من هم رئیس‌جمهور زمان جنگ هستم
ولی در کل رابطه خیلی خوبی دارم. با هم خوب کار کردیم، نتیجه هم گرفته شده
همیشه هم همین‌طوره. بدون آمریکا اصلاً نمی‌شد انجامش داد، همه اینو می‌دونن. ولی ما تونستیم
@withyashar</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/withyashar/13382" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13381">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PebnkRN28McbYk0N8Dq0ng-AV4KIwH74eC1PKUHHAG-EUFTkvwBPlyuahKnRPKWJnKmb3wbgXb1SLvpmvBg44P-efgRe9rX3aoOZEvW9TPmTN3Z3-QJ1AEntiZ60A6qBqx5q_W-GFYZwHY0HJDNOyyQi3RangMQbcUwWv-tJXxUWDiQ5mAht5Qt3qOvW9qcfKTKVdiIGYr6Hclfcxraa8GOofsq2ehi6___S-N_DXtFcUnClEgWDGwiN5VizzBmM5haZUqGAlnz6W5JCyiDqmP96eXVUFNNmmHFE4JIW3zYamiQI1JyIuNG8KwIJcDvzoIc8pY3A_Z334unxzglKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در پست جدیدی در تروث با تلقین حس مخفی‌کاری و چند چهره بودن در قالب جیمز باند مأمور مخفی شکست ناپزیر ظاهر شده
@withyashar</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/withyashar/13381" target="_blank">📅 14:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13380">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYVrutj9E36pMSSJUJPfJy4DqGbtG4-VYK1X_vkVL9XwcXDa5m23FU1VqXv81QiHCo-Sb3Jc4II_C8ffcF2lQ8NYJ0QOYAdqHT8nZr2LqeLWmSa3icsVgP3qTLW1RcX6qUl-TwIThVbF6wiM6M4YaopeItAPD0xyk34xML8y4duB5ZwXxo6B7inA3OzkxS7vFmzR5QzHLC-p6bH0xghn7wZ6uGL9-9W2iqvpQjpEJaj8g2iJ5YEpGZ_5SW69lPCXEcj6nMJ7pInbquG2pTRag-TfSYSLoYkLHYLaR0I27jY8vD2FQidvbLWmnT5Xb2jsJmIRlyi0k19q6IOCshRrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان تحرکات سنگین دارن
جهیزیه را میارن
🎉
@withyashar</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/13380" target="_blank">📅 14:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13379">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ دربارهٔ سال ۲۰۲۸:  من هر دو نفر، جی‌دی ونس و مارکو روبیو را دوست دارم. دوست دارم که با هم باشند. جی‌دی و مارکو تیم فوق‌العاده‌ای خواهند بود. هر دو بسیار با استعداد هستند. @withyashar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/13379" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13378">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ دربارهٔ سال ۲۰۲۸:
من هر دو نفر، جی‌دی ونس و مارکو روبیو را دوست دارم.
دوست دارم که با هم باشند. جی‌دی و مارکو تیم فوق‌العاده‌ای خواهند بود.
هر دو بسیار با استعداد هستند.
@withyashar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/13378" target="_blank">📅 14:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13377">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ درباره ایران:
ما نیازی به حضور نیروهای زمینی نداریم. با بمباران، بخش زیادی از نیروی نظامی آن‌ها را نابود کردیم.
آنها نه نیرو دریایی دارند و نه نیروی هوایی همچنین سرباز‌ زیادی هم ندارند
@withyashar</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/13377" target="_blank">📅 14:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13376">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ایالات متحده به تازگی یک جزیره کلیدی ایران را بمباران کرد.
این یک تشدید تنش بزرگ است.
کینگ ترامپ با ملاها بازی نمی‌کند و آنها دارند متوجه می‌شوند.
اوضاع به سرعت در حال وخیم شدن است.
@withyashar</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/13376" target="_blank">📅 14:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13375">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ : گروه‌های مختلفی از آدم‌ها هستن؛ گروه اول دیگه نیست، گروه دوم هم نیست، بخشی از گروه سوم هم حذف شده
و اون آدم‌هایی که الان باهاشون طرف هستیم، همونایی هستن که الان کشور رو هدایت می‌کنن
@withyashar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/13375" target="_blank">📅 14:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13374">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ: اگر من نبودم، الان اسرائیلی هم وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/13374" target="_blank">📅 14:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13373">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:
هر کسی که من حمایت می‌کنم برنده می‌شود. منظورم این است، همه. هفته گذشته دیدی، درست است؟
هر فردی که من حمایت می‌کنم برنده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/13373" target="_blank">📅 14:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13372">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ:
می‌توانم پاسخی بدهم و سپس، ۲۰ دقیقه بعد، وارد دفتر بیضی‌شکل شوم و متوجه شوم پاسخم اکنون نادرست است.
می‌دانی، تغییر می‌کند. حقایق تغییر می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/13372" target="_blank">📅 14:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13371">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
یعنی من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من شروع‌کننده بودم چون نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.
اگر من نبودم، اسرائیل هم وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/13371" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13370">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ: به نتانیاهو گفتم او کاملاً دیوانه است، چون از درگیری او با لبنان نگران بودم.
من رابطه خوبی با نتانیاهو دارم
@withyashar</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/13370" target="_blank">📅 13:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13369">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزارت امور خارجه کویت : حمله ایران به فرودگاه کویت یک کشته و چند زخمی در بر داشته !
@withyashar</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/13369" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13368">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صدای انفجار در‌ قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/13368" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13367">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ تعریف میکنه نشونه زدنه
😁
🚨
@withyashar</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/13367" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13366">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ در پادکست :
: احتمالاً تا روز کارگر (Labor Day) بتونیم محاصره ایران رو برداریم
هیچ‌وقت به دیدار با هیچ‌یک از مقام‌های ایرانی فکر نکرده‌ام
آیت‌الله ایران تو مذاکرات با آمریکا نقش داره و تو جریان گفت‌وگوهاست.
احتمالاً یه زمانی با آیت‌الله ایران دیدار خواهم کرد
قیمت بنزین به زودی کاهش می‌یابد
وضعیت ایران خیلی سریع داره تغییر می‌کنه، و در نهایت اوضاع خیلی خوب پیش می‌ره
@withyashar</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/13366" target="_blank">📅 13:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13365">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: ایران موافقت کرده است که سلاح هسته‌ای نداشته باشد.
@withyashar</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/13365" target="_blank">📅 13:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13364">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صدای انفجار بندر عباس (گفته بودن ۳ روز مهمات عمل نکرده است که دیروز روز سوم بود )
@withyashar</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/13364" target="_blank">📅 13:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13363">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcSqayzfk7ulgobQiIt__TAZF8aj0MaUZP8w_t0soe-r6WSlgnXH3kxxjqoO1OpScvuUAi7R7fp_BeHDJpVv0I17OeqdCeOBQiFVTV98OvT1cVlb6cnNOuCE3gMElWDA1T2tOkfw5SIKFaTWOI7TJGNFnVOporUA6OBpnvFeLJODT6N4Vlzr_KQ9WWpz9cPHCa0Mh_JIbqUBd5ajtUrgSpIB3J4EFWt91FMiykhFmbwVg1V9Dkk33wwFP34LyX86jkmF0w135I_G6ERKQExQOL9WzQuALQXum5Qj3RvmGE7XzvnbhS_ihI33cSb1w3WaeSF2bRhcj2isdcgZ2z8AIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای مربوط به دیروز ، آخرین موقعیت ناو هواپیمابر آبی خاکی یو‌اس‌اس تریپولی (LHA 7) را نشان می‌دهد که بسیار جلو و در نزدیکی رأس الحد عمان آمده!!!
🚨
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/13363" target="_blank">📅 13:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13362">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b108e3f2b1.mp4?token=H1eAYLPs9_W7_tBziPZseMZllKioOR2li9u3ORdkH8BJ28LESVdmq-JDO_Hw_RlApTTwyFjVkY-6kV1-7crcDtLTeA4PVIBrTXlXpme1tntPPWldwt0p67B-Xy_e5VFeC_aomqnnunVD28K-cfL8z6e0V7NIn65nMdhplHMKKc6j5zW8RRFQdWan1UmP7vqZlhnXue3mrlu03qrvXS1l0mdBfxn6qYizmr-xfQxoSdOhz2yjzXQnr9jy_NQPvs9liExIXkWJO0UnPwyuiPmPJRz2D7IZVRiQkmj3sC_Zr0yBysM4FmxmU7CPDRRNhGeQU1rKQG_Mn252wHkKXnwmmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b108e3f2b1.mp4?token=H1eAYLPs9_W7_tBziPZseMZllKioOR2li9u3ORdkH8BJ28LESVdmq-JDO_Hw_RlApTTwyFjVkY-6kV1-7crcDtLTeA4PVIBrTXlXpme1tntPPWldwt0p67B-Xy_e5VFeC_aomqnnunVD28K-cfL8z6e0V7NIn65nMdhplHMKKc6j5zW8RRFQdWan1UmP7vqZlhnXue3mrlu03qrvXS1l0mdBfxn6qYizmr-xfQxoSdOhz2yjzXQnr9jy_NQPvs9liExIXkWJO0UnPwyuiPmPJRz2D7IZVRiQkmj3sC_Zr0yBysM4FmxmU7CPDRRNhGeQU1rKQG_Mn252wHkKXnwmmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون فرودگاه بین المللی کویت
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/13362" target="_blank">📅 13:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13361">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دیروز، مدیرعامل شرکت هواپیمایی کویت ایرویز از سرگیری فعالیت فرودگاه بین‌المللی کویت خبر داد و تصاویری از کارمندان فرودگاه در حال انجام آخرین مراحل بازگشت به ظرفیت کامل آن منتشر کرد ولی
لحظاتی پیش، شرکت هواپیمایی کویت ایرویز از به تعویق افتادن فعالیت‌های عملیاتی خود تا اطلاع ثانوی خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/13361" target="_blank">📅 13:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13360">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16168fdf19.mp4?token=D2syapI70oBkRSW40yRrHhmVUhUZcX2-JHgb55fr075Ok96J0F9hcuJOdhVr3DGAjSY994IBotQ0NwIAc85tsj0Yi-Nf9rQuWPVGVwzC1g7-F4arL9b9ULs6oUVtLnQyM1BP1yCm6HwuZdpTV5oc8PDaYz7ZVWN0MVlKdAndt1W1NmJ5KemKaHRLLYJpZW5dFK_ss6hgZey6ZWet9VkoEk2SK0aCp0sc7dGrxrjCC6gsTRX5hE7RrLJWABi2gQzInDxv38aeglRihKtu3UO_Ap3_csL2T69IJAdRi9lPFSsqmn1XvRz14r_78cQqUfKF_RJP1zU7qmPeYXbQWGeiRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16168fdf19.mp4?token=D2syapI70oBkRSW40yRrHhmVUhUZcX2-JHgb55fr075Ok96J0F9hcuJOdhVr3DGAjSY994IBotQ0NwIAc85tsj0Yi-Nf9rQuWPVGVwzC1g7-F4arL9b9ULs6oUVtLnQyM1BP1yCm6HwuZdpTV5oc8PDaYz7ZVWN0MVlKdAndt1W1NmJ5KemKaHRLLYJpZW5dFK_ss6hgZey6ZWet9VkoEk2SK0aCp0sc7dGrxrjCC6gsTRX5hE7RrLJWABi2gQzInDxv38aeglRihKtu3UO_Ap3_csL2T69IJAdRi9lPFSsqmn1XvRz14r_78cQqUfKF_RJP1zU7qmPeYXbQWGeiRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت پس از حمله رژیم جمهوری اسلامی
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/13360" target="_blank">📅 12:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13359">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ادعای ای‌بی‌سی به نقل از مقامات آمریکایی: ترامپ، از تهران می‌خواهد که امتیازات مشخص هسته‌ای را به صورت مکتوب به عنوان بخشی از یک توافق مقدماتی ارائه دهد
تا بتوان بر بن‌بست طولانی میان آمریکا و ایران غلبه کرد.
ایران در حال بررسی شرایط به‌روز شده است و مذاکره‌کنندگانش نشان نداده‌اند که آیا تهران این شرایط را می‌پذیرد یا خیر
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/13359" target="_blank">📅 12:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13356">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from₃₆₄</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V94l52pW-H1zUvTLlvGb_JpkjYAD6czEnvUJhbEbI-fcESLGG1bzGPXPr6zJoO0JNDUDJ-AXaBLnYeU6LKKbfZbi8RqV29y_Lb5ooGZCtfTPM0lZe5Fc4duIDFmSqyUKu3ZlMUw2o8rJaPdl6uFWwO-iL3aG80NkEYXXX0KKhwj63TvaiLPyinD0Iy2wxqVAc0bl5ICO7ENCOoZ13MWV1KT8jI8KWkGs1uG3h0zdlD9SZKUrj10z1nFDRCGfTvVWArJyNakOZLCe0QDrj8MEY8Ik_gvY-B32Gaja8EowFlPkI5vnDKTYsTAoiYQ-ytQwhRqvMwF7P2wVyn1i4TYN9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا یاشار مهربان</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/13356" target="_blank">📅 12:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13355">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/13355" target="_blank">📅 12:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13354">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🍁┅┅✿❀𝒩𝒾𝓃𝒶❀✿┅┅🍁</strong></div>
<div class="tg-text">درود آقا یاشار مهربان
تحلیل هاتون خیلی جالبه
جوری توضیح میدید که درکش برای همه راحت باشه
سپاس از شما
🙏
🌹
😊</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/13354" target="_blank">📅 12:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13353">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرهای تایید نشده از اینکه که سه نفر از وطن پرست ها مجری محمدرضا شهبازی رو گیر میارن و بهش تجاوز میکنن  به همین دلیل هم برنامه پاورقی فعلا متوقف شده @withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/13353" target="_blank">📅 12:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13352">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/13352" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13351">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=T31QcSjm6MS8bpXnCQzDa6r6A_rym0RqhYnCMs8HLbilMLD3nKyhKEDqOe2_AzWXoUSVemBGaRYXlRj2S8owM-wpUY4TsVpGetgGDQAMyLru1qCDt4xA7nfpceX1VUs0KR45kC1ZglxWO79Jxjx4byNk_sUwk5pGFpqLK3ejdrfBk3Pa4Z2-fvySz6G3SV99gY9jv7Oc49xet00SwtyWGRgIsW0sfO1PifZEJdxLYq9b3WJccnbfamSfgbZdwqgo-UFqJEg2OEBK8RiJq-DQVr2EJFpozQYZvnHwN0g_2NAyhHpd2i-2CyYXBNHY38rNw_HeNJhwsYgDnU_XPAJaWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=T31QcSjm6MS8bpXnCQzDa6r6A_rym0RqhYnCMs8HLbilMLD3nKyhKEDqOe2_AzWXoUSVemBGaRYXlRj2S8owM-wpUY4TsVpGetgGDQAMyLru1qCDt4xA7nfpceX1VUs0KR45kC1ZglxWO79Jxjx4byNk_sUwk5pGFpqLK3ejdrfBk3Pa4Z2-fvySz6G3SV99gY9jv7Oc49xet00SwtyWGRgIsW0sfO1PifZEJdxLYq9b3WJccnbfamSfgbZdwqgo-UFqJEg2OEBK8RiJq-DQVr2EJFpozQYZvnHwN0g_2NAyhHpd2i-2CyYXBNHY38rNw_HeNJhwsYgDnU_XPAJaWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/13351" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13350">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromToranj</strong></div>
<div class="tg-text">درود یاشار عزیز ، چرا حملات اخیر جمهوری اسلامی به کشور های منطقه نقض آتش بس نیست ؟ و واکنشی خاصی از امریکا و اسرائیل دیده نمیشه ؟</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/13350" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13347">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orAjsAxFxEk_HEBT-DzP3K0io7Vt_NsoBKsm52OaVif4wm5iXtvgmFAa_jFDpUvklAczeniKpvqVV3ouvJT37pwUSkBy64lxB2Ot16K3x5MokUKtXtJbdJwQJV9XjYaZdlnXjat3JrkiKxGH1rvhHYdQWJMwNFVr4PNr59IYVHPtpjuQWPNCkoj636gD1WWWMqYNDAuRGasqG13rU80Wd1_GYyMVAVN_egfw8uzhA8nIUNRJ3RCOXAJ2RzVWCiHdkpWq6uJ2t-rP_ybv9KNb-4kDmz385_H5tVxxB-nT40VOsZGQag7l7lLpkkpjGQLDbr5a_ZMwTqOt1WF54I5Wjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMCPV8loTWA4y-7AR04j8WXkRfnGoeU0j_4M8TNaRVP8ACZbi2vlKQZgBZGAQAK1otL8L6-a9Bbvt5d8hfGBJ-LTytIs5gOeExXm8kMtCgbIbUUROQP8a0Z3hhE94riZWE0W5vcNmGBvO0QAAjUF1-BeVZcmc8lOIb7bc2lWO7reDasLNxAWtug9Q0wQcF7nJ-YWryuf0clIMTyxBhenLjPny3CaIJ3Tvd57bcTFfEnpJJ7mCv_mlNGKbgJcuVaV1z8uQGwyk9-U8MaKYg6MUXNqYDY3lQh2lJz5FxXaFNeVV07_Xm-QWx9rKOpPHq34gfpwBzvrAmceuV4CsIt6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMPseFl6AKMy4JFWweKrIS1PKyul-9o0LB-hf5dgR6O9YtENZC5NMr_Z076_uIYN4_VDe8vTHKKxh323lafX-41AwJxudmHgFrzQwW643Amx8GRDEoZ6BsxdOTEki7A8giVgw3hPtbdBapoIrXWoRgdelPpLW5-HZT7yZuipEgdGj2m9bTS5XQFlSmuYxOZkSyQiVBbGtFQXu9xJmA6_SEhv2pOJ-mhIQzqFuK8HDmBLZ-ymEnIp6K8SpWIxTRA-PMVXggJTc293GN-g0_n5Tc1pM3fDs2U_4HH95nVShq3xXzEpRroK2kjaR-eYeWts9CbTA51DqyaDLM-vPEBBVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همکنون وضعیت فرودگاه کویت
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/13347" target="_blank">📅 11:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13346">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwfyk93nR10_H9QMv63t2ycBLP5KcqgXCVbrherX325eJgAOvJytimbidimQgRhqL8fVVEelQAQeVmRT2MNWLCpPZwhcjS5b_wT1Dh3mEOsnIZzoQ4JN4rH0WQlvZkQIydOQxmTa4t-1FWCZpsAMkV7V_u23hUrFWO-AYD0WBorM1WXaYH7KtCk3EiM1JgGhItD1InIXAGUqK8vidYOm2xdrXdldPeHx-QcQZdXSgpD2uSsH8QwB58JQuY1D1evu32dsgs98epMIAe_VhIhodnc22iXE8_wysrAMk2k7MtVli47WmsQ08jFyxmldAeDjivnIS6UTUj6nGvN-ou2Djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با شما : مشاهده شدن سه ستون دود غیر معمول سمت آزادراه تهران پردیس
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/13346" target="_blank">📅 10:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13345">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرهای تایید نشده از اینکه که سه نفر از وطن پرست ها مجری محمدرضا شهبازی رو گیر میارن و بهش تجاوز میکنن
به همین دلیل هم برنامه پاورقی فعلا متوقف شده
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/13345" target="_blank">📅 10:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13344">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نایب رئیس مجلس: موشک‌هایی که به بیت اصابت کرد تنها چند کروز بود نه سنگرشکن
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/13344" target="_blank">📅 10:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13343">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سی‌ان ان : شدیدترین تبادل آتش از زمان آتش‌بس!
هم‌زمان با دور تازه حملات آمریکا، ایران کویت و بحرین را هدف قرار داد.
یکی از شدیدترین تبادل‌های آتش از زمان آغاز آتش‌بس در شرایطی رخ داده که مذاکرات همچنان شکننده و ناپایدار توصیف می‌شود.
۹۴ روز بن‌بست؛ تنگه هرمز همچنان در وضعیت انسداد باقی مانده است.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/13343" target="_blank">📅 10:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13342">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce930b592.mp4?token=KfBpz6fPBxu9gbuqjjeniKuYlDcdyfO4y6gnPb1gbmkLcRkJTJrEF3v9YIZP0loWNqXRH-8Np5i4swRvOPa7ny1ytxsKtg1svmMo59MNn4w2ddt9pSw5Mrvpreb1Zx4xrdBA3TdDuwxp7ENaz8CpgeNiJyid0goXK3qyFysIwSXjXCc2dJ2BlZmHCFD2csy7_uH4YikYmsOeOqwDGgzBtKyS8uhu5nPfV5OrKc6L-gwhXAGasfif9gufv_t13OqObyuiLK-NcQdbtzZGzy_ZRbfSMpq5vsYNsIImH6ZORcIRvxSpBNh-Lv3L00qHmPp4xihdy3qCHSsK25PwUgR726D1WzpzKhJDhDcr4Q07B0mrqjS_V-X2o2cdX8ZtnRipSybePzW_tfdxHY63UtStQDtyHprRkiBEvOTG-jsqXVby-qQnBWQFChFjoKFDMU7XvxQCK86gNA7Z1VFy_JUiCObLBQtN114hwH60QPchT9p1pRcY4ep1I8jb1cCOTK7loxLud0mNyr1w54iqfg7bz9lstAyzgX32Hd21X8H1rC4d0FO_67A4C8A7GAN9dAbECqosZU3bGkGOzAgHTPRla3vmjHtLFED2crN6ZPsCb-_cY7BFVhoI0YvMLp-hOFmiCQ0sPg4aLtv1W3h2QyO1SE9jOKBoqQgs6xfahw-vN2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce930b592.mp4?token=KfBpz6fPBxu9gbuqjjeniKuYlDcdyfO4y6gnPb1gbmkLcRkJTJrEF3v9YIZP0loWNqXRH-8Np5i4swRvOPa7ny1ytxsKtg1svmMo59MNn4w2ddt9pSw5Mrvpreb1Zx4xrdBA3TdDuwxp7ENaz8CpgeNiJyid0goXK3qyFysIwSXjXCc2dJ2BlZmHCFD2csy7_uH4YikYmsOeOqwDGgzBtKyS8uhu5nPfV5OrKc6L-gwhXAGasfif9gufv_t13OqObyuiLK-NcQdbtzZGzy_ZRbfSMpq5vsYNsIImH6ZORcIRvxSpBNh-Lv3L00qHmPp4xihdy3qCHSsK25PwUgR726D1WzpzKhJDhDcr4Q07B0mrqjS_V-X2o2cdX8ZtnRipSybePzW_tfdxHY63UtStQDtyHprRkiBEvOTG-jsqXVby-qQnBWQFChFjoKFDMU7XvxQCK86gNA7Z1VFy_JUiCObLBQtN114hwH60QPchT9p1pRcY4ep1I8jb1cCOTK7loxLud0mNyr1w54iqfg7bz9lstAyzgX32Hd21X8H1rC4d0FO_67A4C8A7GAN9dAbECqosZU3bGkGOzAgHTPRla3vmjHtLFED2crN6ZPsCb-_cY7BFVhoI0YvMLp-hOFmiCQ0sPg4aLtv1W3h2QyO1SE9jOKBoqQgs6xfahw-vN2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاباری استیون براون که در مسابقه معروف «۱۰۰ خلبان برای یک جت خصوصی» متعلق به مستر ‌بیست برنده یک جت شده بود ، توسط مقامات پاراگوئه در جت خصوصی که از میامی و از طریق پاناما وارد شده بود و حدود ۲۶۱٫۶ کیلوگرم ماری‌جوانا با THC بالا به ارزش ۳.۶ میلیون دلار حمل و نقل میکرد دستگیرشد !
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13342" target="_blank">📅 10:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13341">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حرکت پهپاد شاهد۱۳۶ ، فعالیت پدافند و در پایان برخورد و انفجار در فرودگاه کویت !
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13341" target="_blank">📅 09:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13340">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سازمان هواپیمایی کشوری کویت: یک ساختمان مسافربری در فرودگاه
کویت هدف پهپادها و موشک‌های ایرانی قرار گرفت و حالت اضطراری فعال شده.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/13340" target="_blank">📅 09:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13339">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وال‌استریت ژورنال: حمله سنتکام به جزیره قشم، قیمت نفت را صعودی کرد و چشم‌انداز بازگشایی تنگه هرمز را کمرنگ ساخت.
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/13339" target="_blank">📅 09:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13338">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">منبع آمریکایی: اگر پاسخ ندهیم، باید به رهبری کاخ سفید شک کرد
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/13338" target="_blank">📅 03:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13337">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ الان میاد میگه چون موشک ها از رو آب رد شده مسافر حساب‌ میشن و رعب و وحشتشون شکسته حساب میشه پس این جنگ نیست !!! هرچی شده رفع بلا بوده فکر کنین دادین خمس و زکات ، حالا هم آشتی و من به  یک جنگ دیگه پایان دادم و رژیم هم تغییر کرد ولی سلاح هسته ای نباید…</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/13337" target="_blank">📅 03:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13336">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گروه کومله کردستان در بیانیه‌ای اعلام کرد که ساعت ۲۳:۰۰ به وقت محلی دیشب ، دو موشک ایرانی به مقر حزب کومله در دره آلانه، واقع در شمال شرقی اربیل، اصابت کرده است
در این خبر جزئیات دقیقی از تلفات احتمالی ارائه نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/13336" target="_blank">📅 03:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13335">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ الان میاد میگه چون موشک ها از رو آب رد شده مسافر حساب‌ میشن و رعب و وحشتشون شکسته حساب میشه پس این جنگ نیست !!! هرچی شده رفع بلا بوده فکر کنین دادین خمس و زکات ، حالا هم آشتی و من به  یک جنگ دیگه پایان دادم و رژیم هم تغییر کرد ولی سلاح هسته ای نباید داشته باشن
@withyashar
👱🏽‍♂️
📿</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/13335" target="_blank">📅 03:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13334">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانال ۱۴ اسرائیل: اگر رژیم ایران امشب حتی یک گلوله به سمت اسرائیل شلیک کند، تمام دروازه های جهنم به رویشان باز خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/13334" target="_blank">📅 03:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13333">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی با موفقیت چندین موشک بالستیک و پهپاد ایرانی را سرنگون کردند و در پاسخ به حملات احتمالی ایران در سراسر خاورمیانه، امروز ، حملات دفاعی به جزیره قشم انجام دادند.
ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای پرتاب کرد؛ اما همه آنها نتوانستند به اهداف مورد نظر خود اصابت کنند. دو موشک ایرانی که به کویت شلیک شده بودند، کوتاه آمدند یا در مسیر شکسته شدند و سه موشک پرتاب شده به بحرین بلافاصله توسط نیروهای دفاع هوایی آمریکا و بحرین رهگیری شدند.
لحظاتی پیش‌تر، نیروهای فرماندهی مرکزی آمریکا (سنتکام) سه پهپاد حمله یک‌طرفه را که ایران به سمت دریانوردان غیرنظامی که به‌حق در حال عبور از آب‌های منطقه‌ای بودند، شلیک کرده بود، سرنگون کردند. نیروهای آمریکایی همچنین حملات دفاعی به یک ایستگاه کنترل زمینی نظامی ایرانی در جزیره قشم انجام دادند.
هیچ یک از پرسنل آمریکایی آسیب ندیدند. نیروهای سنتکام هوشیار باقی مانده و آماده دفاع در برابر تجاوزات بی‌دلیل ایران در طول آتش‌بس جاری هستند.
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/13333" target="_blank">📅 03:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13332">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اصابت در عربستان
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/13332" target="_blank">📅 03:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13331">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">امارات هیچ آلارمی ‌نیست سایت فرودگاه هم کنسل شدن پرواز نشون نمیده فیکه !
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/13331" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13330">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اخبار تایید نشده از صدای آژیر خطر در عربستان
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/13330" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13329">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/13329" target="_blank">📅 02:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13328">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حملات جدید به کویت
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/13328" target="_blank">📅 02:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13327">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رژیم جمهوری اسلامی به بحرین حمله  کرد پدافند بحرین فعال شد @withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/13327" target="_blank">📅 02:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13326">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۳‌پا
اعلام کرد در پاسخ به آنچه «حمله آمریکا به حاکمیت ایران در جزیره قشم» خوانده، پایگاه‌های نظامی آمریکا در کویت را با حملات موشکی هدف قرار داده و این اقدام را «پاسخ اولیه» توصیف کرده است.
در این بیانیه به آمریکا و هر کشوری که خاک یا آسمان خود را برای عملیات علیه ایران در اختیار بگذارد هشدار داده شده که هرگونه اقدام جدید با پاسخی شدیدتر و فراتر از «قواعد متعارف» روبه‌رو خواهد شد.
۳پا همچنین تأکید کرده است که دوران «بزن و فرار کن» پایان یافته و نیروهای آمریکایی و متحدانشان باید منتظر پیامدهای اقدامات خود باشند.
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/13326" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13325">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حمله دوباره جمهوری اسلامی به اقلیم کردستان
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/13325" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13324">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مهر: یک موشک به ساحل ایران برخورد کرد
خبرگزاری مهر گزارش داد یک پرتابه در محدوده ساحلی بین شهر سوزا و روستای ماسان برخورد کرده است
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/13324" target="_blank">📅 02:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13323">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/13323" target="_blank">📅 02:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13322">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUC8xM5kNGTcyblezICt_uovjUAjX1mrpVYc6rTzXO4voQySZvFFYgkdKGJcGLtWzONgtvxEC0unGUw8J3cPxvuRLRRqSsADEG9Ukz_Zaj6ZrZfHSmgPC8yoYNDGcIhrM_lLpNNIB_TkWyQaiLZqbqDRuoIWiF1Eh2lR-fw_1KnOaaabgfzZfEcyiGyj7RNw2Ou41UOymUN1PULvt4-BDnp6sSLTLmq2ge_rhq-JGbgAy86lVaxbrPWaE6rS6U7XvedFcAj3nFwpjs7NEU3hzyh1_Z68CusdS1Na4nA3IgmO_wuoRlV7ieLab2Piavh_u-SM28tzAGFHSdS6L9psZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم جمهوری اسلامی به بحرین حمله
کرد
پدافند بحرین فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13322" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13321">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dee78f961.mp4?token=WYq1NHqRcpjnhzIG0PvNASG4pIKZwlNlFRPTuLHXxqXAquUo6cNa7rNjCfd7EI2E-GAC-jd-Rx0ZlRqEXhAeeFXpHSFmFM4WFmgY9nIvd5yENCamevirrrIsfRSO6bECkhy9q_gfA5MG_rTGprju_Hc4x3ILRiRQa9mGiMszh46_WoxwdzU6ByYVJCj6ZUXFiEODU9uvBsSw6ipeQEzHACqUkbxKgrf2Vl2tLkgVPVg1koAlx7QWQetw5J7twobn9jE7QygaHMAarHuHfFl4DtYuVQYjznzTXe7942__GjpVOd4qDwajKOIef0Gziw0voNv8kIBZqMWqGdHBRpShhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dee78f961.mp4?token=WYq1NHqRcpjnhzIG0PvNASG4pIKZwlNlFRPTuLHXxqXAquUo6cNa7rNjCfd7EI2E-GAC-jd-Rx0ZlRqEXhAeeFXpHSFmFM4WFmgY9nIvd5yENCamevirrrIsfRSO6bECkhy9q_gfA5MG_rTGprju_Hc4x3ILRiRQa9mGiMszh46_WoxwdzU6ByYVJCj6ZUXFiEODU9uvBsSw6ipeQEzHACqUkbxKgrf2Vl2tLkgVPVg1koAlx7QWQetw5J7twobn9jE7QygaHMAarHuHfFl4DtYuVQYjznzTXe7942__GjpVOd4qDwajKOIef0Gziw0voNv8kIBZqMWqGdHBRpShhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصادف در خیابان های کویت بر اثر تماشای موشکهای ایران
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/13321" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13320">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7e3bcc.mp4?token=jLc26G_N3B3OT2aCmnVijnmWg67f4Zd-DJKEJRdxRitkXHTUKsJnqsPvaPo29cYHdV7KlTmaFqowGotPcygE3-26NVCEFKp6BmVtLgn-DXORU77KS0ESr7EUgmKorKhXb3QD6vg7wtQNoXCkoKTky0-FB4mInDU81h2KOwaXWw5Ct9bidTzqQ8Aeo2CdAGPW5Kt6gowyVEWpI0wrt2iXcMsv5s-zgJygdtd8HgwsmQ23bbvDWyKwp3rynzFOeUHnki0zKA63xgnmx-JEk3Y9D2lSttTvkfpT6q3GQYzgMU-q4gaxpqiy0hbxsbL7fMirPFmAzCwJzOnOn8KV0NPA_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7e3bcc.mp4?token=jLc26G_N3B3OT2aCmnVijnmWg67f4Zd-DJKEJRdxRitkXHTUKsJnqsPvaPo29cYHdV7KlTmaFqowGotPcygE3-26NVCEFKp6BmVtLgn-DXORU77KS0ESr7EUgmKorKhXb3QD6vg7wtQNoXCkoKTky0-FB4mInDU81h2KOwaXWw5Ct9bidTzqQ8Aeo2CdAGPW5Kt6gowyVEWpI0wrt2iXcMsv5s-zgJygdtd8HgwsmQ23bbvDWyKwp3rynzFOeUHnki0zKA63xgnmx-JEk3Y9D2lSttTvkfpT6q3GQYzgMU-q4gaxpqiy0hbxsbL7fMirPFmAzCwJzOnOn8KV0NPA_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیکه دیگری از لاشه موشک
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/13320" target="_blank">📅 02:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13319">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2918449436.mp4?token=B3ZfSlZv5W4UTdvy1uVA_1nOOeu6RCN0i6EBLKg-cj2amLg9dh26CwoeCQLJWPcdbRnEp3ftq9Lb9ptWqmKV7DPZyxphQKFD13otGbPvLJg5uMyfdm6o-iZWAlbbeGug18f12xFHP5jPLsT7o9LB99qLICIKp3ibc0FBaYyvapNbfWq_ZG1tZi986Cl-KMz9zeoTtNN506paSaSimMiB7Wx89blSZqgjLEJ_lhHOTr6lDoKy7o0LoueTHxuPRfgqTOjy6asuER2bPPNjAS0fG_434b4k1ZvCmSBoFAPduUvb1wBzXpEmuhiXQpUjBngDMuJtNDo2yE3cDw1OJz5ldw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2918449436.mp4?token=B3ZfSlZv5W4UTdvy1uVA_1nOOeu6RCN0i6EBLKg-cj2amLg9dh26CwoeCQLJWPcdbRnEp3ftq9Lb9ptWqmKV7DPZyxphQKFD13otGbPvLJg5uMyfdm6o-iZWAlbbeGug18f12xFHP5jPLsT7o9LB99qLICIKp3ibc0FBaYyvapNbfWq_ZG1tZi986Cl-KMz9zeoTtNN506paSaSimMiB7Wx89blSZqgjLEJ_lhHOTr6lDoKy7o0LoueTHxuPRfgqTOjy6asuER2bPPNjAS0fG_434b4k1ZvCmSBoFAPduUvb1wBzXpEmuhiXQpUjBngDMuJtNDo2yE3cDw1OJz5ldw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشه موشک منهدم شده ایرانی‌توسط پدافند امریکایی کویت
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/13319" target="_blank">📅 02:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13318">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اینترنت ایران داره به همین سرعت محدود میشه
🚨
😞
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/13318" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13317">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9349aaf84.mp4?token=vb3Eg2Ny4-5K72NnASC1AVJ8tEOi_jmVo5uTwaUaMzRYKX1IrV1gank-ioLM25jKvZDhTybI0QM5GTtLoNQ5duTyZ0dfwdyDzRUJQ5svvXvhvWfnhEKrE0KBy8LObVJQrw3nMhIBFCQXxXbkmk-0FlX6KSUAWWps92skc_socv-EL7LW8HoqrVtg21sldEhnAE7J1NVQ8d-K78x73kYsanZLoKe3fg5UBIe8uHypar1ap_Waw9msf2SiKnkEWEatTEbJk1iGkh_wnzydG0jTp2Lr0JvlHeyCwxNnRJFVXtbLx1VTsRR-BX5R1-OL3jnYwPO_ivc9D5fAm8bKG76K3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9349aaf84.mp4?token=vb3Eg2Ny4-5K72NnASC1AVJ8tEOi_jmVo5uTwaUaMzRYKX1IrV1gank-ioLM25jKvZDhTybI0QM5GTtLoNQ5duTyZ0dfwdyDzRUJQ5svvXvhvWfnhEKrE0KBy8LObVJQrw3nMhIBFCQXxXbkmk-0FlX6KSUAWWps92skc_socv-EL7LW8HoqrVtg21sldEhnAE7J1NVQ8d-K78x73kYsanZLoKe3fg5UBIe8uHypar1ap_Waw9msf2SiKnkEWEatTEbJk1iGkh_wnzydG0jTp2Lr0JvlHeyCwxNnRJFVXtbLx1VTsRR-BX5R1-OL3jnYwPO_ivc9D5fAm8bKG76K3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان کویت کمی‌پیش
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/13317" target="_blank">📅 02:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13315">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جنگنده‌های اسرائیلی پرواز کردن
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13315" target="_blank">📅 02:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13314">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13314" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13313">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پست جدید از صحبت‌های بسیار زیبای شاهنشاه آریامهر  ارتباط قلبی ما
❤️‍🩹
فرا مرزی شده  https://www.instagram.com/reel/DZGNeRLxq-Y/?igsh=MXQ1dTZmdXk2bGZpdQ==</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13313" target="_blank">📅 01:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13312">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b76b57549.mp4?token=m6kgWvXP_U8H4UiX3ulbrtICpcg_XoJYS4zkAyg5Bl8M9TVoDhQo0vQrov8zAKfRuEJp__NL3NjCJWwSsEIXUSG0r6f-lRQIgklWPrs-zVRRiZ1gB4-t4fWZAtfYtKU3e2pE3M1LGwoUVZ-tHoy9MaqngxmXG0KaOdKy95QvtJkGJMzHwiUzopxuUzO9JGqLp0kXKRYlq5-vzKZb0nofSMlnoVhhKsxBDookFPRa_2cvC_khadvb2BrLG13ubp59203BsuTBb55qR1A1_IyARhCURT3S0G-oxW-pFT9jpOPzzswM7-5TdK7Zg3RZBf21_Ito54XvPgrtUV56lrp01let2-TiAYFxZBgKPkBlU-Tt_cIxMfLnDe6TTrCAt9xOC10paO2jHZVWe9evpQ6rX9jv5frTGFqURiQNvLam1mj0jrOhRcT01mgkyhnbGfPb7WbyWMJea23UdbWqkN6JBHTM98ofKuX6Dz47OAQ5HwVegvFxZMNKhwWAoyzMYgias1PZibFuDoZVIrvhwjQqDUkBZ__6F2DoTsvIIqMEYFDOiM9HNds5QEfP2AhVeQuklp3DmVpFdrVtzESOTAc8zxvavPQ7jUemLneJqdapEua65HfSQpmbmWufVeeKCJe0oENTNuW9B5MaAvMIu2t4fu-x4q-MXq0K4SuArFDcNVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b76b57549.mp4?token=m6kgWvXP_U8H4UiX3ulbrtICpcg_XoJYS4zkAyg5Bl8M9TVoDhQo0vQrov8zAKfRuEJp__NL3NjCJWwSsEIXUSG0r6f-lRQIgklWPrs-zVRRiZ1gB4-t4fWZAtfYtKU3e2pE3M1LGwoUVZ-tHoy9MaqngxmXG0KaOdKy95QvtJkGJMzHwiUzopxuUzO9JGqLp0kXKRYlq5-vzKZb0nofSMlnoVhhKsxBDookFPRa_2cvC_khadvb2BrLG13ubp59203BsuTBb55qR1A1_IyARhCURT3S0G-oxW-pFT9jpOPzzswM7-5TdK7Zg3RZBf21_Ito54XvPgrtUV56lrp01let2-TiAYFxZBgKPkBlU-Tt_cIxMfLnDe6TTrCAt9xOC10paO2jHZVWe9evpQ6rX9jv5frTGFqURiQNvLam1mj0jrOhRcT01mgkyhnbGfPb7WbyWMJea23UdbWqkN6JBHTM98ofKuX6Dz47OAQ5HwVegvFxZMNKhwWAoyzMYgias1PZibFuDoZVIrvhwjQqDUkBZ__6F2DoTsvIIqMEYFDOiM9HNds5QEfP2AhVeQuklp3DmVpFdrVtzESOTAc8zxvavPQ7jUemLneJqdapEua65HfSQpmbmWufVeeKCJe0oENTNuW9B5MaAvMIu2t4fu-x4q-MXq0K4SuArFDcNVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفع موشک های ایرانی در کویت
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/13312" target="_blank">📅 01:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13311">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/13311" target="_blank">📅 01:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13310">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پایگاه عریفجان در جنوب کویت، نیز هدف قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/13310" target="_blank">📅 01:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13309">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/13309" target="_blank">📅 01:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13308">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMhdi</strong></div>
<div class="tg-text">یاشار این به معنای شروع جنگ هست بنظرت یا امریکا میخواد بگه نقض نشده</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/13308" target="_blank">📅 01:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13307">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLj0LcLo5rtiWKzvpl4ap3VHJtv-takLyQqH__NsQ2SygbE5Tua7vr02Qc5dPx05o0WwGX5vg5cEsR0MVlRFr2_5Tba7e1R_R-UkzCstQWlfrG3wGiWpgrnV8ShaBUT29S4bScyeIpva4_8asStWbDqNJ5nzW7j1uJ1YbVsegRgakAy8OxJrVifa-b7es3ov1k3nQYJVlBXJw6lp5fYB7On2jJdUjDtK9pN6tVJ7vJadDU4IQ97N69hW7NTHqcSKNdg9GWZGROJn8m3oSE_Tlh4E9oBD150Uhegia-vH09lI4Y-8BWO2bv0-ozbBbIIWBl9ap8s2Fj89Yy4_fvvkag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رد موشکهای بالستیک در آسمان شیراز
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/13307" target="_blank">📅 01:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13306">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الان شلیک ۲ موشک از سایت موشکی زین آباد داراب احتمالا به کویت @withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/13306" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13305">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=MfLhW12i0KDSxqXXMGdDuhwL_-_11MuNyDzfugxvKIrs3qRl6wC6trF7RvD5yqE-k9a8UnKCTGECY6FYQOZy04ME1lVg8CAklDeJmXWSVr98cdsqI_WA9XHQmKFPngxvPCHAyb7zGU8vxe3VZHuY8JrPpUfkqK2s6Lmuh3YYqaYHn2DWzDjtI-6mRD27R1_L1AbI44yXbaVv522ElXCR-JEK0xZ6P8ArkgLQxhS-E9v9AmsvT-uBDJZxz7GwzMYnfDQqY0FuKLjOFbAMO3ApUAAJSzhfaRCSZZNLYzMEiXQj1_VLlvHQ3j2qWPl0c78uutWCOU7PugQb6Lw1ij7G6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=MfLhW12i0KDSxqXXMGdDuhwL_-_11MuNyDzfugxvKIrs3qRl6wC6trF7RvD5yqE-k9a8UnKCTGECY6FYQOZy04ME1lVg8CAklDeJmXWSVr98cdsqI_WA9XHQmKFPngxvPCHAyb7zGU8vxe3VZHuY8JrPpUfkqK2s6Lmuh3YYqaYHn2DWzDjtI-6mRD27R1_L1AbI44yXbaVv522ElXCR-JEK0xZ6P8ArkgLQxhS-E9v9AmsvT-uBDJZxz7GwzMYnfDQqY0FuKLjOFbAMO3ApUAAJSzhfaRCSZZNLYzMEiXQj1_VLlvHQ3j2qWPl0c78uutWCOU7PugQb6Lw1ij7G6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/13305" target="_blank">📅 01:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13304">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsAbZKL7pLT8F2JdwkcqE5C9vua12eDy0gaomkfz-O6fJE03X3CPV9rm1_U_VzQF2oGegm2tgswOboDpqFLVZe5CDPMxejbfVfiQ62jas6bnsRXAlx5zsD9fpSeoDWovu7tGWXx-t-yuyydb-bBqKUoo4K1pGgpsHX26JwMv0qTEYvZwCJTTcR3_CcQnY6V1cVS6TJkTUPRNLXyghBFuipTu--USgipxO3wPhYkqh3N8v7_y4Pys9yx3rn68XNOuuccC-TFfTXeKL9SMJtoy9zG-dIdcR1ZcNlehqYMUhsF7x99CSl7PXkSDnuEYwpvqtqgafMvcb2CoFU0HC4YJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کویت تأیید کرد که به موشک‌ها و پهپادهای پرتاب شده از ایران پاسخ می‌دهد
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/13304" target="_blank">📅 01:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13303">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آژیر در کویت
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/13303" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13302">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jgb3Z2olUuPPsGGK59tBo5BZ51Lj2uMcOxziMunu9OTvs70k6lHSiTPihiqP8qZxaC3Zt_XyrfkGBd1eRsJHyyJzasmQE9vaTjkCSiH9Ybfyv0T9QTGzZllsn7cMy19hADPNl9lS_9iBsaOkXrDK3CCllMCaExAVmam9mkRHC9Q2Lm2fpHCqj_k4OwLuhYQB6_3CUHLjML1pouESQB2ShD4MPw5rpqvl7VEsr7kBvwMN7PfKE9tM0hljsjFaDlnMjxF6nZphlIY3ny6aJNfRPSXrQ2uN_Zt-GlFx_1KwvnqyS2oMw98mIScPErJmIVaHks8KlOQOlYSGElUJPCtURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان شلیک ۲ موشک از سایت موشکی زین آباد داراب احتمالا به کویت
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/13302" target="_blank">📅 01:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13301">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرگزاری مهر بعد از  ساعتی چک کردن چنل ما گفت : بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
پیگیری‌ها برای کسب اطلاع از ماهیت دقیق این انفجار  ادامه دارد.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/13301" target="_blank">📅 01:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13300">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خاورمیانه جنگشم مثل آدمیزاد نیست !
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/13300" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13299">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اتاق جنگ با شما : صدای انفجار از سمت دریا نبود
به اون کوهه زدن که پر از مهماته نزدیکمونه قشنگ به چشم دیدیم
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13299" target="_blank">📅 01:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13298">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارش انفجار قشم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13298" target="_blank">📅 01:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13297">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffea244ab.mp4?token=YwSe5QPPgYeXlZLRAi1rDosP1NbaqZO2tle8d0SYKEbAHs5uszoECALdnzss88o6dGN-4kuThuwy7CiZMmwcKRpgeHaSn-IOPikPailbRA2jGDihUC8c1h6d7jhekZp9PJ6QRFc9augye7ZojbijAJHjEBysgoXamwDLdiERYSDEqbOqmFAJgQ6OkegRv_OfXl13IlwFeV9Uou5u70rrxIUb6ij5Pds6NZij9txaHuxM_e4Yqtshli0xgPh_aBSrNWeu3UsFZsEYGRluDFDkcKfHoicDjXa4ccocF3wH1FUKkHAXwivQcNo0yXtARI9OOOncsa3FMP_rdGkPTy9oGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffea244ab.mp4?token=YwSe5QPPgYeXlZLRAi1rDosP1NbaqZO2tle8d0SYKEbAHs5uszoECALdnzss88o6dGN-4kuThuwy7CiZMmwcKRpgeHaSn-IOPikPailbRA2jGDihUC8c1h6d7jhekZp9PJ6QRFc9augye7ZojbijAJHjEBysgoXamwDLdiERYSDEqbOqmFAJgQ6OkegRv_OfXl13IlwFeV9Uou5u70rrxIUb6ij5Pds6NZij9txaHuxM_e4Yqtshli0xgPh_aBSrNWeu3UsFZsEYGRluDFDkcKfHoicDjXa4ccocF3wH1FUKkHAXwivQcNo0yXtARI9OOOncsa3FMP_rdGkPTy9oGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای ایالات متحده ساعاتی پیش یک نفتکش خالی از محموله را که در حال حرکت به سوی یکی از بنادر ایران در خلیج فارس بود، از کار انداختند.
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که اقدامات مربوط به محاصره دریایی را علیه نفتکش
ام/تی لکسی (M/T Lexie)
با پرچم بوتسوانا، در حالی که از آب‌های بین‌المللی به سمت جزیره خارک در حرکت بود، اجرا کرده است.
به گفته سنتکام، خدمه کشتی هشدارهای مکرر را نادیده گرفتند و طی یک دوره ۲۴ ساعته چندین بار از تبعیت از دستورات نیروهای آمریکایی خودداری کردند.
در نهایت، یک هواپیمای آمریکایی با شلیک یک موشک
هلفایر
به اتاق موتور کشتی، آن را از کار انداخت و مانع رسیدن نفتکش به ایران شدند
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/13297" target="_blank">📅 00:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13296">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش انفجار قشم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/13296" target="_blank">📅 00:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13295">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رسانه‌های ترکیه اعلام کردند که ویزای مکزیک کلیه اعضای تیم ملی فوتیال ایران برای سفر صادر و تحویل سفارت ایران در آنکارا شده است.
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13295" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13294">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13294" target="_blank">📅 00:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13293">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پست جدید از صحبت‌های بسیار زیبای شاهنشاه آریامهر
ارتباط قلبی ما
❤️‍🩹
فرا مرزی شده
https://www.instagram.com/reel/DZGNeRLxq-Y/?igsh=MXQ1dTZmdXk2bGZpdQ==</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/13293" target="_blank">📅 00:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13292">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آمریکا ۴ صرافی بزرگ ایرانی
نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.
@withyashar
این صرافی ها ولت هاشون فلگ بود و از قبلم هر ولتی که با این صرافی ها ارتباط داشت کثیف میشد
اما الان خطر فریز شدن دارایی در صرافی است</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/13292" target="_blank">📅 23:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13291">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">العربی الجدید: مذاکرات لبنان و اسرائیل در واشنگتن به پایان رسید و قرار است فردا ادامه یابد
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/13291" target="_blank">📅 23:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/13290" target="_blank">📅 23:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13289">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/13289" target="_blank">📅 23:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13288">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/13288" target="_blank">📅 23:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13287">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دایرکت باز شد بریم برای پاسخ به سوالات
💥</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/13287" target="_blank">📅 22:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13286">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کرج صدای پدافند
🚨
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/13286" target="_blank">📅 22:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13285">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش ها از درگیری شدید مرزی میان هند و پاکستان
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/13285" target="_blank">📅 22:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13284">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش زیاد شیراز صدای پدافند / انفجار
🚨
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/13284" target="_blank">📅 22:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13283">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/13283" target="_blank">📅 21:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بریم برای سوال و جواب، هر سوالی دارین توی متن کامل بنویسین و دایرکت کنین، فقط در یک پیام.</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/13282" target="_blank">📅 21:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b925d659.mp4?token=KrKGVihU7S-hEoGU17Sd2lt6lulBPZm3MvSmfZg5PT3kpM6LP6V92DZppN4AGyFzJtbAuWTR70DCCiVciETNWvsIuCzZRzAdTqM_OMBwM4NwQVPkfbgoQpy16rFxbO1w3UyslgjEjIhWldyjC4u7gzCLgwY5iQ8n70DPgp1C-hD4mNf0ThpBwaZhy_aglfPWeImHRrA-MvW7Zk-WdqiRNaYNxv7wrUgrb4fAzEyv64iDicCJ_xxOz97NcsiMYBK8pmjyQhF_FEIr5zCOx0AJQloaJ24ADmTdhTuVa5ktnoWCHaaUuDB-Bwa6In8PUiEzIFDJVpWhK6M7TYaEoeBdLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b925d659.mp4?token=KrKGVihU7S-hEoGU17Sd2lt6lulBPZm3MvSmfZg5PT3kpM6LP6V92DZppN4AGyFzJtbAuWTR70DCCiVciETNWvsIuCzZRzAdTqM_OMBwM4NwQVPkfbgoQpy16rFxbO1w3UyslgjEjIhWldyjC4u7gzCLgwY5iQ8n70DPgp1C-hD4mNf0ThpBwaZhy_aglfPWeImHRrA-MvW7Zk-WdqiRNaYNxv7wrUgrb4fAzEyv64iDicCJ_xxOz97NcsiMYBK8pmjyQhF_FEIr5zCOx0AJQloaJ24ADmTdhTuVa5ktnoWCHaaUuDB-Bwa6In8PUiEzIFDJVpWhK6M7TYaEoeBdLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: «موساد همچنان در خط مقدم نیزه در نبرد ما علیه تجاوز ایران باقی خواهد ماند.
ما اجازه نخواهیم داد رژیم ایران چرخ تاریخ را به عقب برگرداند. ما اجازه نخواهیم داد به سلاح هسته‌ای دست پیدا کند. ما اجازه نخواهیم داد موجودیت ما را تهدید کند.
این رژیم محکوم به زوال که پایانش فرا خواهد رسید و ما به رسیدن آن به این سرنوشت کمک خواهیم کرد.
این رژیم دیگر باز نخواهد گشت تا ما را با بمب‌های هسته‌ای و هزاران موشک بالستیک مرگبار تهدید کند.
این دستور من است و این مأموریت شماست، رومن.»
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/13281" target="_blank">📅 21:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ربطی نداره ناو لینکلن ، بوش و ناو آبی خاکی‌ تریپلی و کلی‌ ناوشکن هستند و کافیه!</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/13280" target="_blank">📅 20:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ادعای شبکه ۱۲ اسرائیل : دستور تخلیه ضاحیه جنوبی بخشی از هماهنگی نتانیاهو و ترامپ برای فشار به ایران تو مذاکرات بوده و نه برای حمله مستقیم به ضاحیه
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13279" target="_blank">📅 20:42 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
