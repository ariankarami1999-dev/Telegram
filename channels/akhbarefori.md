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
<img src="https://cdn4.telesco.pe/file/FgUkLoYSNrrEMpnQmIh38a6wND7OXXNxnBcjHY1ff0ky9HFvZ3y6dXyrlKCI3Tcq5GX0KRumJZ1lpZcszQM9LrmfxJV23b4Q5Gp71IgGFhEFIDkx9Gv8FU7yqsOY5aUk0xgGP4mWhCUoMNwI4ex0GWowMTmEWPkmA3_-hTB0RyJDqD2jUAAHDkhxBhT7Zjyx8aNDhaVeq2UU54mMqSOWKg4_NF0o_v_2cD3otR4vU2bWR7guo1766zGr0iIg3Sxe5kwuf_VvAUeLvW1K2XBjGIRtoAPFWXAkaCANW6YlcesESPIz9WWJN3LRq-x5sJCoUpcNshNJtkFLARfacFnL9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.98M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 22:30:47</div>
<hr>

<div class="tg-post" id="msg-692104">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پشت‌پرده هزینه‌های انتخاباتی؛ از پرداخت ۹۰۰ میلیون تومان برای همراهی یک چهره تا شام‌های هزاران نفری از زبان رشیدی‌کوچی، نماینده سابق مجلس
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
بعضی نماینده‌ها بابت هزینه برای رای آوردن از شرکت‌ها و سازمان‌ها کمک می‌گیرند.
🔹
کل هزینه انتخاباتی من در سال ۹۸ مبلغ ۱۲۵ میلیون تومان شد در حالی که آنطور که گفتند یکی از رقبای ما فقط ۹۰۰ میلیون تومان پرداخت کرده بود که یک نفر کنارش عکس بگیرد.
🔹
یکی دیگر از نماینده‌ها پمپ بنزین اجاره کرده بود که هر کسی آنجا می رود هزینه بنزین پرداخت کند .
🔹
یکی از رقبا بطور متقن هر شب ۲ هزار نفر را به مدت ۱۰ روز شام می داد.
🔹
مخالف با تبلیغات نیستم؛ با این مخالفم که شفافیت در این موضوع نیست و فردا چگونه میخواهی پس بدهی؛ بالغ بر ۶۰ تا ۷۰ درصد نماینده‌ها اینگونه هستند‌.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/692104" target="_blank">📅 22:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692103">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران در سخنرانی سالانه مجمع عمومی ملل متحد: آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد. #Devil…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/692103" target="_blank">📅 22:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692102">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2c9a9d6d.mp4?token=mfATQ3-TTafatJ3-kMRb3X-1TSuYkdAlqvP1pgBfj79iVKBEVvzwZ38S2hHzjcE04boNBa26WIt1jA--_cJz743uIWEVpBhZyFGtsv7rhpIBSRCiR-8jS3JRxrAeVCfU-AY4UOc6bOsAPpXeTaNQ7bV0Tz5jut5O66_bhgJpBPQ64lxrKWDahs9iSgvwF4naa8TnHwWbxBeNI4mY64Gg6z6xCQABJG4T254HjEfG1kSQh6027NjPB9Pl-1LS4S3GltAtmMLWc0_APyAzkpCKL2L2khMBQo18Uj5w1_iqOR5M5fhKZiyoFh9sbDqpTjLZOV40ZoTWwPZx0MsU3TqtDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2c9a9d6d.mp4?token=mfATQ3-TTafatJ3-kMRb3X-1TSuYkdAlqvP1pgBfj79iVKBEVvzwZ38S2hHzjcE04boNBa26WIt1jA--_cJz743uIWEVpBhZyFGtsv7rhpIBSRCiR-8jS3JRxrAeVCfU-AY4UOc6bOsAPpXeTaNQ7bV0Tz5jut5O66_bhgJpBPQ64lxrKWDahs9iSgvwF4naa8TnHwWbxBeNI4mY64Gg6z6xCQABJG4T254HjEfG1kSQh6027NjPB9Pl-1LS4S3GltAtmMLWc0_APyAzkpCKL2L2khMBQo18Uj5w1_iqOR5M5fhKZiyoFh9sbDqpTjLZOV40ZoTWwPZx0MsU3TqtDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میوه کاکائو رو دیده بودید؟
🍫
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/692102" target="_blank">📅 22:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692101">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP-a48Lt-sMgZF_Ip9vszcnRcErLAJEOBEoYu1uPBF16wlynIm6wzyQp99q_y2keJi0LotMV7JuCmfAL9RFPy63AXMwZ8lLpQSTAeqI4vHmhSNpWCSqgLPXlSeFV10hRs73h9lN56YN5E1kZKYVCXxut7PMz3tiSEyjiGPZMALA-7pqiuRtrq_oYdP5MW3nDOPkLj6aTupec5YMd5eLM3i_m_5wiSnCcu1Dm_mKj-SUzaXFB9OFBalxkIdu614p10kZa752hZop6K0Q2cuMTChkkrZiYx05TlaT_GYTGaoKBGDv-8bRib1hzz0jpYwXEdu91LWMcps0YCRmyaDDnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از سخنرانی رهبر شهید انقلاب در چهل و دومین مجمع عمومی سازمان ملل، در دوران ریاست جمهوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/692101" target="_blank">📅 22:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692100">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
مدیرعامل شرکت ارتباطات زیرساخت: طبق برآوردها حدود ده درصد از پهنای باند کشور از استارلینک رد می‌شود
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/692100" target="_blank">📅 22:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692099">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a2d3d3b9.mp4?token=UdCpsi1jQ7P5Lljq3iblHCKNw7RdpM68-4KBl_hob_s6g2OO3_c239q0JvEi66ym8P2QNq7a22pO0VhHiDMQBMS0ZlAekpM3W-TfO5muOofrLqQsahMKOEgL9tcnvy8f7qaP4O_tivuy8ExC9dWZC9RvjqOSGWiK4D0U2XI_UlXH70S4hTEcGEpsb1A0LP0z3s1LUrCqv7b3ZYRrQTDxu1J0s8IDG30QNVjiS9reBw5OOZcsEt1CB7taDWETD9ofyZ-NEziQvvBrJ3wfpze0wjTkpBH8SP3WB-DPAc7DchyGkKQymNbvxiL5ukCw2fN3g35XHpTdSRBjXFSueyAJQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a2d3d3b9.mp4?token=UdCpsi1jQ7P5Lljq3iblHCKNw7RdpM68-4KBl_hob_s6g2OO3_c239q0JvEi66ym8P2QNq7a22pO0VhHiDMQBMS0ZlAekpM3W-TfO5muOofrLqQsahMKOEgL9tcnvy8f7qaP4O_tivuy8ExC9dWZC9RvjqOSGWiK4D0U2XI_UlXH70S4hTEcGEpsb1A0LP0z3s1LUrCqv7b3ZYRrQTDxu1J0s8IDG30QNVjiS9reBw5OOZcsEt1CB7taDWETD9ofyZ-NEziQvvBrJ3wfpze0wjTkpBH8SP3WB-DPAc7DchyGkKQymNbvxiL5ukCw2fN3g35XHpTdSRBjXFSueyAJQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری وزیر نیرو در صحن علنی مجلس: اگر حملات نبود در صنعت برق مشکلی نمی‌داشتیم
علی‌آبادی، وزیر نیرو در صحن مجلس:
🔹
در اثر حملات آمریکا ۴۲۰۰ مگاوات برق از ظرفیت برق کشور از چرخه خارج شد.
🔹
برای امسال تلاش کرده بودیم که نه تنها برق خانگی را پایدار نگه داریم، بلکه به صنعت هم برق بیشتری بدهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/692099" target="_blank">📅 22:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692097">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: نماینده‌ها محلی شده‌اند، نه ملی/ دغدغه بسیاری فقط این است که برای دوره بعد دوباره رأی بیاورند
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
یکی مثل من حرف که می زند درس عبرت برای بقیه می شود؛ خانه نشین‌مان می‌کنند.
نماینده‌ها عموما محلی هستند و ملی نیستند.
جای سوال دارد چرا نماینده ها اینقدر ساکت هستند.
🔹
نماینده‌ها به فکر رای برای دور بعدی خودشان هستند؛ واقعیتی است که هر کس منکر شود دارد سر خودش را شیره می‌مالد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/692097" target="_blank">📅 22:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692096">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
خبرهایی از ساقط شدن جنگنده دیگر سعودی در یمن
🔹
یک رسانه عراقی خبر داد که نیروهای مسلح یمن موفق شدند جنگنده اف-۱۵ دیگر سعودی را ساقط کنند.
🔹
نیروهای مسلح یمن هنوز بیانیه‌ای در این باره صادر نکرده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/692096" target="_blank">📅 21:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692095">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
دریافت نخستین سیگنال رادیویی از یک سیاره فراخورشیدی
🔹
اخترشناسان با استفاده از آرایه رادیوتلسکوپی MeerKAT در آفریقای جنوبی، برای نخستین‌بار انتشار امواج رادیویی از سیاره فراخورشیدی Beta Pictoris b در فاصله حدود ۶۳ سال نوری از زمین را شناسایی کردند.
🔹
پژوهشگران می‌گویند این سیگنال‌ها احتمالاً ناشی از شفق‌های قطبی و برهم‌کنش ذرات باردار با میدان مغناطیسی سیاره هستند؛ این کشف به‌تنهایی نشانه‌ای از وجود حیات فرازمینی نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/692095" target="_blank">📅 21:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692094">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
استیو ویتکاف از صحبت درباره دیدار ادعایی با ایران که حدود یک ساعت پیش انجام شد، خودداری کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/692094" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692093">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
مسکن زیر سایه جنگ | هر متر مسکن در ۱۵ ماه دو برابر شد | چرا جنگ قیمت خانه را کم نکرد؟
🔹
بازار مسکن تهران در یک سال و سه ماه گذشته، برخلاف انتظار اولیه، نه‌تنها با کاهش قیمت در مناطق آسیب‌دیده مواجه نشده، بلکه در تمامی مناطق ۲۲گانه شاهد رشد قیمت بوده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3247147</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/692093" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692092">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1o4V3krQKna7F7yH3kJ8W0wsiy4n-KQHEdF81Cmy3kVUVKkzeIg7lyLB59SDhhwpQdWjl-INEg_t-09ioC9rqSgiKP_6P-_kMNt8Fq1e-0t6uFSIRCteCn_oEpEKoX_HCK8HBkUwzifG8tL_09AIuQ2orws4HsuIDv3Xez4ScWx8nOLYQiOkqSScgCRXmjmHirGDFPFgQfmmXckNFCpAgUXhVbvtWoLbUR6NPkYAcq1KWnMxt-eNblPdNA27kqB3sSL_p09TbWzcNLnD3MZXYRKXsw6n-tSaDqSHbk0zi0CXonVa5PqdaUqwdKVBbumaOTyYK7wg1_gu-q95PJh1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران در سخنرانی سالانه مجمع عمومی ملل متحد: آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد. #Devil…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/692092" target="_blank">📅 21:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692091">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/269f77218a.mp4?token=PJppo1sV82xTlgHyf7kp0-DXMwPiPh5ksJ3W46KzXk1oD860W5UpP0TTm7jP1Mg3Pcn4tm9RnTBpxTTj5BOf3WKhjcRayGlL9yESEpICk23n-fxKP3l-547IH2aveqXnVM2KblDYU0G-V6M97bb8o_b8cV1h8-d2zQObVTuV9UZ98Sap5sqLZBCkY6NE6-m2iZQ4laiNn9JVlXfxdGkQrV7yFbZOFdPrnvXLm4bYApEsqOnzKSGe8eBNmdximhqR6dmf6PwZlYaXvAxmnM1obM-EZMBEukf0_2iC7WLEtAHLJzuOF3Msm2M7rYBtPHY0dpMMUynSRZcV2fe1fjqz2CdW3Or_xwYhZyF9LRhjVLZnqgC6xDMfxjdslJ6JUYqjs66pj9F4qVXzPcs4wMVjy3rxnkvETuNItQCRWQG-OvmuKV1gONEgSucDBBxS3Z4EveYSPAWRl0UlOFnm5CLLy4--AlW4x25Gp0zIf6K_o604yopsv2mNQt0pzaZMjyY0gXYcXA4fJiwpXh5lgla21F_gDtP2FBKUHcNLIyJzuNWsje1VpAWRAkYfVErRfkbxAjG5EmKfRi83E6tFEq2Vyblk8nTCX-H25HNH7AcNTL6S0H-Zx_NJ7IfLPWyx4ItMEbX47UmvyCluOuojDYm3IrkPZ2HEcy_K9tBHHG2L7rM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/269f77218a.mp4?token=PJppo1sV82xTlgHyf7kp0-DXMwPiPh5ksJ3W46KzXk1oD860W5UpP0TTm7jP1Mg3Pcn4tm9RnTBpxTTj5BOf3WKhjcRayGlL9yESEpICk23n-fxKP3l-547IH2aveqXnVM2KblDYU0G-V6M97bb8o_b8cV1h8-d2zQObVTuV9UZ98Sap5sqLZBCkY6NE6-m2iZQ4laiNn9JVlXfxdGkQrV7yFbZOFdPrnvXLm4bYApEsqOnzKSGe8eBNmdximhqR6dmf6PwZlYaXvAxmnM1obM-EZMBEukf0_2iC7WLEtAHLJzuOF3Msm2M7rYBtPHY0dpMMUynSRZcV2fe1fjqz2CdW3Or_xwYhZyF9LRhjVLZnqgC6xDMfxjdslJ6JUYqjs66pj9F4qVXzPcs4wMVjy3rxnkvETuNItQCRWQG-OvmuKV1gONEgSucDBBxS3Z4EveYSPAWRl0UlOFnm5CLLy4--AlW4x25Gp0zIf6K_o604yopsv2mNQt0pzaZMjyY0gXYcXA4fJiwpXh5lgla21F_gDtP2FBKUHcNLIyJzuNWsje1VpAWRAkYfVErRfkbxAjG5EmKfRi83E6tFEq2Vyblk8nTCX-H25HNH7AcNTL6S0H-Zx_NJ7IfLPWyx4ItMEbX47UmvyCluOuojDYm3IrkPZ2HEcy_K9tBHHG2L7rM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروع سال تحصیلی جدید
در چهارشنبه امام رضایی
🗓
💚
🔹
پویش سراسری «مهر رضوی»
قرائت صلوات خاصه امام رضا(ع)
📿
🗓
در نخستین چهارشنبه امام رضایی
سال تحصیلی از حرم مطهر رضوی
🔹
همزمان با مدارس سراسر کشور
🤍
به نیابت از امام شهید و شهدای
دانش‌آموز جنگ تحمیلی دوم و سوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/692091" target="_blank">📅 21:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692090">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c556986398.mp4?token=c9kcYM2cpOMJshlb3SBekrhXIRSdaq31QkzfgZszNvdHGFIVnK5QyL7ZMvdrPRM6tJj1kDy--jZXmxCrWhTqb_05HtUWnrf8ljPs0ipvggFRGuMf2GVzV1bzvE4l7MTsVIPvE3f3KZUp6Y-rW2pEDjgoOYNoXzDSdL_MMUVXt0gFU_SQ8t0AvfWe8DDDjT9KW6frxrsJsN0mtQWI3hkmQZTOpunjhkZBfPKYhdcHCQQlweFyaXU8YkkOsrd5RDCLSgaDXxkMoepYCcsrGU1eJYXLlwrkJuQt7TIW6jVvNO2DkyWeYg6_w5K82GHKWXG8ubEI5iEjhhni11a5lmw7YEgya0iDOcFetpGmh6r8jY2n0DvK3mxk9uUV_Vecf1MezYPW4EmWZmdYIdvBoZmwQo7we51_K-6qGUUia1iCHzs_BriN-X3t136mIoyt0METiPBtf5Riqh5tAPPGda86JnhbSAMOzcIWVoR7RnW78T6vSlL3xcO7nzm-rNDDflirPYGVdrdhC-amdyx9mO7rWgGZDQP6AV-6WdwCYn5Sf_AVH-DSilQKjtXlcsZGZgWTvyoCcbH8VTkjH0kZ9iaVripZnIShxI7IwS6HhhxNiOUhIweYaQfnMLakX4A0aWMJtl9_nO-Lsdi4h-2P2dRHekBNAnTp8G1nwPgI-rbk2mc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c556986398.mp4?token=c9kcYM2cpOMJshlb3SBekrhXIRSdaq31QkzfgZszNvdHGFIVnK5QyL7ZMvdrPRM6tJj1kDy--jZXmxCrWhTqb_05HtUWnrf8ljPs0ipvggFRGuMf2GVzV1bzvE4l7MTsVIPvE3f3KZUp6Y-rW2pEDjgoOYNoXzDSdL_MMUVXt0gFU_SQ8t0AvfWe8DDDjT9KW6frxrsJsN0mtQWI3hkmQZTOpunjhkZBfPKYhdcHCQQlweFyaXU8YkkOsrd5RDCLSgaDXxkMoepYCcsrGU1eJYXLlwrkJuQt7TIW6jVvNO2DkyWeYg6_w5K82GHKWXG8ubEI5iEjhhni11a5lmw7YEgya0iDOcFetpGmh6r8jY2n0DvK3mxk9uUV_Vecf1MezYPW4EmWZmdYIdvBoZmwQo7we51_K-6qGUUia1iCHzs_BriN-X3t136mIoyt0METiPBtf5Riqh5tAPPGda86JnhbSAMOzcIWVoR7RnW78T6vSlL3xcO7nzm-rNDDflirPYGVdrdhC-amdyx9mO7rWgGZDQP6AV-6WdwCYn5Sf_AVH-DSilQKjtXlcsZGZgWTvyoCcbH8VTkjH0kZ9iaVripZnIShxI7IwS6HhhxNiOUhIweYaQfnMLakX4A0aWMJtl9_nO-Lsdi4h-2P2dRHekBNAnTp8G1nwPgI-rbk2mc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: از این مجلس چیزی ندیدم جز اینکه چند تندرو به قالیباف و پزشکیان حمله کنند
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
مجلس امروز با نیازهای کف جامعه هیچ همخوانی ندارد.
🔹
این مجلس بعد از چندماه بازگشایی طرح مقابله با نفوذ را آوردند؛ طرحی که آخر آن هر کسی حرفی بزند یک برچسبی به عنوان نفوذی به او بزنید.
🔹
من از این مجلس چیزی ندیدم غیر از اینکه چهار نماینده تندروی خوش مغز، جنگ طلب و بی کله به آقای قالیباف و پزشکیان فحش بدهند.
🔹
قرار است با رسایی پیاده رویی برویم و ببینم مردم نظراتشان چیست.
🔹
از نود درصد مجلس چیز خاصی ندیدم و ده درصد دیگر حرفی می زنند که بیشتر نمک روی زخم مردم می پاشند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/692090" target="_blank">📅 21:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692089">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2b162769.mp4?token=SOhzttq0ZgrZe4ENptNzA83whvMwoUfgKOjCGZsD3l1zpiQ8t5QZp0lXK2xaK75QcF2gXyGen7kPOekvDQXoeRJ6BiSaXPsffylTrT93dtJE4CRc28yWJnKzXdgxBcRrUjlF6cvjA9eWm8xxlpRhzdlHivppwb23rjoSfyLFH5E_OpE6Ie-c64sj7dFqeBvq8DQ1DQLrfYjdGXnM6AMEc1bGTnsnxh2ojxZtqjt-yzY5Mx-rVQpz1YDeaXrat_k1ts3-LHqpnJGuFv17MO_80TpyFeP4-fqw8n7E7_vuTecVg5Z-iKoT8Npj21R_3K2QosnBiYUQlSmwMSKFHC888jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2b162769.mp4?token=SOhzttq0ZgrZe4ENptNzA83whvMwoUfgKOjCGZsD3l1zpiQ8t5QZp0lXK2xaK75QcF2gXyGen7kPOekvDQXoeRJ6BiSaXPsffylTrT93dtJE4CRc28yWJnKzXdgxBcRrUjlF6cvjA9eWm8xxlpRhzdlHivppwb23rjoSfyLFH5E_OpE6Ie-c64sj7dFqeBvq8DQ1DQLrfYjdGXnM6AMEc1bGTnsnxh2ojxZtqjt-yzY5Mx-rVQpz1YDeaXrat_k1ts3-LHqpnJGuFv17MO_80TpyFeP4-fqw8n7E7_vuTecVg5Z-iKoT8Npj21R_3K2QosnBiYUQlSmwMSKFHC888jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره ایران: آن‌ها قرار است در آینده‌ای بسیار نزدیک، جلسه دیگری داشته باشند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/692089" target="_blank">📅 21:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692088">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE25v3SUE90C3NNoT38k1W2mHEa4f6gJfCmbLnioYRXyVuiS7yfG7AyoMich53b3koWZ-JwtD_ytg2mBLD0Zje-nnu4aSDfA-DUyr0LUPz-9QQG7uX9zWphH8hyYyOldK5zp6XnbMLSjwgXfLBrsmey_P8_C0vYMeTe4oNPxlmIa8NHkBXjz5cRAwD3df3RVwKCKFIxFcI-oeyf7g7AWHsmfeGs6itc6j1GLJiv8Pp1lYwxzo8MwxjBl1d5VNpNnekha4dmw75C6j9q_vzYKlSUSB16XPvKdWBcUHRHsLYHe0GDdoVUmON1xQJ6gzeuQ0T2VlTHasIs5K1VYYeZGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از ساعت ۲۴ امشب پروازهای تهران به بغداد و مسقط لغو شد  سخنگوی سازمان هواپیمایی کشوری:
🔹
از ساعت ۲۴ امشب به وقت محلی، فرودگاه بغداد پذیرش پروازهای ایرانی را انجام نمی‌دهد و به همین دلیل در حال هماهنگی و رایزنی هستیم تا پروازهایی که مقصد آنها بغداد است، به…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/692088" target="_blank">📅 21:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692087">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای ترامپ: یک مقام آمریکایی با هیئت ایرانی دیداری سه‌ساعته داشته که به گفته او خوب پیش رفته است
🔹
برای ایران یا عظمت و شکوفایی بالقوه وجود دارد، یا نابودی.
🔹
در یک حالت، نابودی است و در حالت دیگر، عظمت بالقوه. ایران می‌تواند یک کشور بزرگ باشد/ خبرفوری…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/692087" target="_blank">📅 21:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692086">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ترامپ مدعی شد: مذاکرات ما با ایران تا به امروز ادامه دارد و من معتقدم که با آنها به توافق خواهیم رسید #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/692086" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692085">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt4TOLOQZcqFeOPgN_kIhtNEcXH3z7OpE4OFNC_cHA5rQY7v_ea6-GZ2h2AowAEctIQQyZv6NefC0MP0aVNgACSxLedjWO1NXtxbjupaQ7n3u86E37-YKMHh1fa1tfcoZMzK6i90VATNo2TD32gwTAxU7piM5vMc0GFAlqtsa-jzBLDGaWz4VIijA1huXmIYEDd3aiR8UnZmm2rhVaNQ6OmwuLCjsC6jdbKxOBg2QsQjM-D51iDCHq11K95T-hTSYpK7pRL-2cDAth3KmtOJdKST8n5IxOdM7ifYzvwoxJR1Itzv_3nP_3IvxYckoYSwpHmLn6UPyZeBPpxW8FjFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: هیئت ایرانی هنگام سخنرانی ترامپ درباره حملات آمریکا به تهران از مجمع عمومی سازمان ملل خارج شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/692085" target="_blank">📅 21:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692084">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e521a07c.mp4?token=dMLTpoz6Vtp2RSEQJ4405KC_nUvH8jquGwX521JGjqAUsXJuMuKMNsOzncGWRePisXEnjMFXPc8IIjdWKDQrWga6NS1LA-K6iwc8pmx0lyi8ih-hVtIGCyLVJpCjGrM9b9GB_aw-DNW_qYBmsPa2FuYbtfKgcHsf9Rl03cYmcUvy3woamPp_Qk_mXgkzzjH39KVB3Y0VkUFncd65NqxLdpTIwuk85Ek31rHtMEuZGKled-GhCSep7sut7O3gjWdDy40UGVVSoadnvaCrLtwH2G9Bpd5pqANbgtm8xDoXiLZ59meTmzesaeNrh5l0oA9MscH_WnsCTTD3JEWU3HNtxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e521a07c.mp4?token=dMLTpoz6Vtp2RSEQJ4405KC_nUvH8jquGwX521JGjqAUsXJuMuKMNsOzncGWRePisXEnjMFXPc8IIjdWKDQrWga6NS1LA-K6iwc8pmx0lyi8ih-hVtIGCyLVJpCjGrM9b9GB_aw-DNW_qYBmsPa2FuYbtfKgcHsf9Rl03cYmcUvy3woamPp_Qk_mXgkzzjH39KVB3Y0VkUFncd65NqxLdpTIwuk85Ek31rHtMEuZGKled-GhCSep7sut7O3gjWdDy40UGVVSoadnvaCrLtwH2G9Bpd5pqANbgtm8xDoXiLZ59meTmzesaeNrh5l0oA9MscH_WnsCTTD3JEWU3HNtxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب ترین خوراکی دنیا در کشور فنلاند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/692084" target="_blank">📅 21:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692083">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
مدیرعامل سایپا: ۶۰ هزار شاهین تحویل دادیم؛ حتی یک دستگاه هم نفروختیم
🔹
علی شیخ‌زاده، مدیرعامل گروه خودروسازی سایپا: «در یک‌ سال‌ونیم گذشته نزدیک به ۶۰ هزار دستگاه شاهین تحویل مشتریان دادیم، در حالی که حتی یک دستگاه شاهین هم نفروختیم و تا پایان تعهدات نیز امکان فروش این محصول را نداریم.»
🔹
او با اشاره به حجم بالای تعهدات گذشته گفت: «در مقطعی حدود ۵۰۰ هزار ثبت‌نام برای شاهین در سامانه یکپارچه وجود داشت؛ رقمی معادل حدود ۱۰ سال ظرفیت تولید این محصول.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/692083" target="_blank">📅 21:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692082">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: چرا موضوع موتورسواری زنان را این‌قدر پیچیده کردیم؟/ با یک اصلاح ساده قانونی، این مسئله قابل حل است
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
معاونت حقوقی رییس جمهور خیلی نمی‌خواهد بالا و پایین کند من میگویم شما یک لایحه برای اصلاح قانون بدهید که صدور گواهینامه برای مردان و زنان به عهده نیروی انتظامی است؛ یک کلمه «و زنان» میخواهد اضافه کنند.
🔹
عده‌ای خشک مغز می‌نشستند که وقتی با آنها حرف می زدم، غصه می‌خوردم و گریه‌ام می‌گرفت که چرا این همه سال در این مملکت این افراد مسئولیت داشته است.
🔹
استدلالهای احمقانه‌ای برای موتورسواری زنان داشتند که اگر بگویم مردم عصبانی می‌شوند؛ مثلاً می‌گفتند خانم‌ها اگر پشت موتور گاز بدهند، مانتو به پای آنها می‌چسبد و برهنگی آن مشخص است. خب احمق الان مانتویشان را هم در آوردند
🔹
بعضی از این آقایان دین را هم بازیچه دست خودشان کردند.
🔹
شما زمانی باید گشت ارشاد را جمع میکردید که کسی خون از دماغش نیامده باشد؛ بعد از آن همه آسیب و اتفاقات چه ارزشی دارد؟
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/692082" target="_blank">📅 21:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692081">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
یک مقام ارشد در کاخ سفید به الجزیره: هیچ دیداری در برنامه رئیس‌جمهور ترامپ با ایرانی‌ها وجود ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/692081" target="_blank">📅 21:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692080">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سخنگوی سپاه: درباره گمانه‌زنی‌ها پیرامون «کوه کلنگ» نظر قطعی نمی‌دهم، اما اگر آمریکا قصد حمله به هر نقطه‌ای از کشورمان، چه کوه کلنگ و چه غیر از آن را داشته باشد، با قدرت تمام پاسخ خواهیم داد
🔹
ما اهل تبلیغات هالیوودی نیستیم و اسرار نظامی خود را فاش نمی‌کنیم؛…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/692080" target="_blank">📅 21:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692079">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای ان‌بی‌سی: کوه کلنگ هدف اول آمریکاست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/692079" target="_blank">📅 21:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692074">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kV7FyTNN4ouqKXH8y5Iov4YHVTjfCb3IAIIlqSh8hABKU0JMwIwNP22tJx07AEjNgXrRroIpgw7Q5GdTCl2Vmbzlm7wJdrbgqWLJ9UXsXeYGw65ZTZuh1mGB8uVZ3uHcc4l4cmISpS7ouKLDu6FDC3kc5j9syD9l_O0o0Z9QbckLpyw6NjxNXTtgQo5GccUdGI8jCUKo6D5IvC9rXTZOCrvE13WssyPUWL_IcjzjocD2jpZqXJHS3Xz9UUNCb7xRzejMXLLeL5igAtBzWiWeTWRZOHelHceOoYcjvBuSgDXYITmT14g-qAtCcMvbmi4QIwZuNUsfV2lZtDPC5vYFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dBqbGAVxO8z_g_bfK96ywQr4CiqKJuekSLWeffXEN529FwvKdoUzjLvORwYNpI7BHJM3BACiWpHhL5b0_CIz5q-bFaRjaGO2631Vm4xBb52_cGt_CQqlef7ykiRLoW1nzyz4a3alHqfVVW5yncamvPFNmAbRnyFNvASIOr8VmtXaGaVjBL4fwXZLySDSX8AswGgnA_-Cgm5AUp-2_70fNMIBHoihcZ_Jm1tcfRxeqL7XlfMH2-Fasc-LKOv-GnKeZSbUwo5CSb6KJbOmsOQs0vfGTEq2f5QtHxpuv0QJ-ppU5iW-oytTFiwHUNTgZuzRIGyeRd5yD5rRNBX63dhZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RlWaVwveRNSXLUGMuxFX5Wd_i3xozC5rPOb0nHsJpx3Rw41jXLKr3fjh5wCpsU65bJZFH0vcsMWhc8RBrqOc-j9vfbCmsF6-BqRrMTdEvprsQ8D7-yk9WC9edvVmLBED3FnKR3Vy7Nx0dTWEy_4d76t7QqYkFW4FfXm_V_9wuF-Js_C2PSrYfN-c9zn9q765oo9aPux4gi7uLl49hxnQ-_EgmXgJQ1Qsl2-6vHEdveth4Tv-eDenvjfemZRiqQuqsbq1zam8Ja4f_fiMKftWc24wP-X0WjvUgtuqvdlbraWw9oVkkJZyTG8HRIKfMCaMYDiE11QBafq3R1hpOxj4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRJCE6ZN-AkFq8y50jpD-i4vpoFEhjNBZiSksVusbnFU30n6nFNJb5pcIrZFHLnbKtEGj3veSeihgLLIKt30Hy9BwsRBhVFMPYRCboy7nGm8KfSkUB6N0VvtaLIIAx3sPz2dNZnZxvBnZD55_SLRfljI-jKgfyIzGkld6QJXzCTeYOIxcbo6cI5oXu1OxvsJAc_mn9lxxuIojry_MWQAHYxho-DE2mJKWCO-DYWOOWYaG-Oa2akCWcTZO_e2xrmRVQVzvdxKdEdRunIiLt-Oivde7G3CwqoZJ_ZqvbgZWMt_-c-QTy5Mb-3H7nr6O53gLDvYOp67vB6fKEb8jIQf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1TAS3ZE5XasLbSauNaL_Jr34qZgFyQUI6YPb_9ff2m97RKYbh9RKgiHz6V4JPk9QIcT3ZjkTSaRTn0XgiGWHegUE-woxEtDK8HAp870Ywr_zBAecAYCs1Chl_r7xjCExM_6PTP6BS_mASP2OCGdYSGzU35taL8wspHbj3tlgAVOv25nSPtk6K8dSUXG4-mZSoG_Jj4rsTu7hdYnc2lKLKRzUq3lC48MCtoLpjan1IBQJccVlnrdO6uCo9-516Y6aMTMHGAS0tg1NA-hbhqDZhzhTY7m09PZVLBjXAzaAXp4jmxqGOAY4bC2v6Sdz-wqgx08JFRpMQTRGEd-j2vBEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند ترفند کاربردی که ممکنه به دردتون بخوره  #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/692074" target="_blank">📅 21:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692073">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbiklf_4d9vN_iKXKWybQwdJ7qJEwYqFvYoyZy0HuWpw3ylv4leKaZkllbvNBR9kYIzkY7dpaUs-X3sxvcYqE7UKgo3fQ-Q4re5er1TBfjDC7Rsls5jTblOivb3HeDd6lWtHogRvGRRfVgTEctngMuC_lXxSyiWrScGSrdLfRadxwsUTWTMmXDXrE_o_sjHz9eO25_iTaKfbrdIiOnKXyFgHlC2ZQDPNcDHPzVfcdzMxit8xuJ7ijaXm8i5Ce6S0wmo6W7CrWeRiobsWXSeEPfOAMdsQ_Z9JNNwkYfO09XW_HB9Bbdl8czG3LQBZ6BsPAjUq4HyeX0_Rat7r9xTNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از ساعت ۲۴ امشب پروازهای تهران به بغداد و مسقط لغو شد  سخنگوی سازمان هواپیمایی کشوری:
🔹
از ساعت ۲۴ امشب به وقت محلی، فرودگاه بغداد پذیرش پروازهای ایرانی را انجام نمی‌دهد و به همین دلیل در حال هماهنگی و رایزنی هستیم تا پروازهایی که مقصد آنها بغداد است، به…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/692073" target="_blank">📅 21:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692072">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd129974b3.mp4?token=TnORMdYknVzP9K6d1xnWB-22mpNnTrZkx7J82w_R7kXv9gWZNTRKlfKC_hw-fBlQ_L2dFoi5N1-Q8G94bAYmGbwnPwZb15Cqa_4HbQ0Qdxe_p3fYKd18j__BpKWZhvU8eLqBHSsm7eN3Wqc2WdjBKRJe4AFjDjxmYl7UwUpJSzDj9KcR6TJXfLxcVSJZmE0pnpS7AqSmoyYDD0w-0QHzbd8H9_xWIVvIa1oL2gTgOfnD4eX57Gzdc7fgeRNhBQHM-8teBkz8MFNJtCEFaMBxP4ZyHDGT47bF4Z9379tmETU9xfzith2S2IqoWzjUriqv6Kn9FpcU1cLUYOmc_Tc8qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd129974b3.mp4?token=TnORMdYknVzP9K6d1xnWB-22mpNnTrZkx7J82w_R7kXv9gWZNTRKlfKC_hw-fBlQ_L2dFoi5N1-Q8G94bAYmGbwnPwZb15Cqa_4HbQ0Qdxe_p3fYKd18j__BpKWZhvU8eLqBHSsm7eN3Wqc2WdjBKRJe4AFjDjxmYl7UwUpJSzDj9KcR6TJXfLxcVSJZmE0pnpS7AqSmoyYDD0w-0QHzbd8H9_xWIVvIa1oL2gTgOfnD4eX57Gzdc7fgeRNhBQHM-8teBkz8MFNJtCEFaMBxP4ZyHDGT47bF4Z9379tmETU9xfzith2S2IqoWzjUriqv6Kn9FpcU1cLUYOmc_Tc8qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۵ سال بعد از ۱۱ سپتامبر یکی از فرماندهان میدانی القاعده و داعش، سوار بر کادیلاک و با گارد حفاظتی وارد نیویورک شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/692072" target="_blank">📅 21:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692071">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEKGhJ3HkOXspyMydriZ09_5pImPyWDoe2gHEDlgqXJoes8A1m8kDMv1Mc9CFBfK-QA1HYxQwth55Jv7H2Gto5PVC-HxwLViU62tz_CCxk2EMYRPVv4QD-r5uqpLav7LWhfOz-PlkQtgsVL1ok0iLeShrqEyk2erOSXDSYqWTt33DQqBikzf24ms1ms_B450j-Ek1D_RBq2OX2Yk85rxHS8SGgzljZAjsZ-86jzYGvsSVqwSWNwSDP-4nvvb2gB4GKduFSKQmzdmK-BVskVZ2SNNkaTg5cnu-zqw1HRAhRcITDBNpIH9ciZ-CTUeg_UFY6-kd8c3b0LyiD3hx1WJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">THEIR STYLE, THEIR STORY.
هر نسلی، استایل خودش را دارد ...
40% OFF
GERAD Kids & Juniors
تخفیف طلایی | روزهای پایانی
Instagram.com/geradofficial</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/692071" target="_blank">📅 21:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692070">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
از
ساعت ۲۴ امشب پروازهای تهران به بغداد و مسقط لغو شد
سخنگوی سازمان هواپیمایی کشوری:
🔹
از ساعت ۲۴ امشب به وقت محلی، فرودگاه بغداد پذیرش پروازهای ایرانی را انجام نمی‌دهد و به همین دلیل در حال هماهنگی و رایزنی هستیم تا پروازهایی که مقصد آنها بغداد است، به سمت فرودگاه نجف هدایت شوند.
🔹
سایر پروازهای خارجی از جمله استانبول طبق برنامه و روال معمول انجام خواهند شد و در حال حاضر مشکلی برای انجام این پروازها وجود ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/692070" target="_blank">📅 20:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692069">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromعشقه ‌🎒(Seyed Hashemi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSmZGWydWN-_2wOS7QrinBKsJqwBPJ5KB2cqu_ukK43jcnliGj1ObiAV428OW4ybzgePUvWtuEYtyXCz2TuzRqQ0vMqWR1tYaLz922lVPllSbhpMDj1GHVs9ig8AccEKF8quWpQuQMegrwEwYfNZM1SjkyMvNqmAWg32frW5Mdp4PQ7GfaizyueVmmmXviLImRrWOsjlyWIMq9owVESNM9oQVWiq2_P7F0JcmneKic5dPPkvM0LacoB3DOPVh0pdl9l5LJMDqGN92jj1QI3uXZPEluW1L1KTow24-yw-PfD3_PnfzCe26Gey0n4cFHnJwtag4t8k_WI-dwki8ysh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلسفه تأسیس سازمان ملل بعد از جنگ جهانی دوم این بود که کشورها از موضع برابر با هم برخورد کنند و استقلال سیاسی همدیگه رو به رسمیت بشناسند!
حالا این دلقکِ تروریست، رسما در سخنرانی سازمان ملل، یک کشور عضو رو که از قضا جزو بنیانگذاران هم هست، تهدید به نابودی می‌کنه!
حقوق بین‌الملل؟!
اینجا قانون جنگل حاکمه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/692069" target="_blank">📅 20:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692068">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14321ab2e.mp4?token=I66N_K7weY4l6fDN5V4QBYae-_0Lul0X1wOHHkoKm9_Zkkl0pcEHhYKMBzwdMbTADGnlkEg7IqKJFSDdCvJsrVlVdJjbDy3nus1apz-QcGwIFka7lFVVpWMxwDG8ASeH0ihWbHj7la8NRsDjreLVFz3-zqS3OwrpR54VckXdFgAPQ8dc2cXzztv3ai9Iv24yroZ0CitwMlxTpLi0MqGGY_0GgtE2KTlF84J_a1tWKTMdUENu6NUZFcqtxZ44ezhcZ8uO_Xd7kKE9xpSBJYq77RnZ8ptMfIZETSykcePVqRduQ2jBSXfdVJYpURub_bz0i33NohySpmZ-MTGBC522ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14321ab2e.mp4?token=I66N_K7weY4l6fDN5V4QBYae-_0Lul0X1wOHHkoKm9_Zkkl0pcEHhYKMBzwdMbTADGnlkEg7IqKJFSDdCvJsrVlVdJjbDy3nus1apz-QcGwIFka7lFVVpWMxwDG8ASeH0ihWbHj7la8NRsDjreLVFz3-zqS3OwrpR54VckXdFgAPQ8dc2cXzztv3ai9Iv24yroZ0CitwMlxTpLi0MqGGY_0GgtE2KTlF84J_a1tWKTMdUENu6NUZFcqtxZ44ezhcZ8uO_Xd7kKE9xpSBJYq77RnZ8ptMfIZETSykcePVqRduQ2jBSXfdVJYpURub_bz0i33NohySpmZ-MTGBC522ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای کارشناس شبکه سه: با توجه به شواهد منطقه، احتمال اقدام جنگی آمریکا بر علیه ایران زیاد است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/692068" target="_blank">📅 20:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692067">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش ۲۳ درصدی قیمت پوشاک/ قدیری: ۳۵ تا ۴۰ درصد بازار پوشاک در اختیار کالای قاچاق است
سعید جلالی قدیری، دبیر اتحادیه تولید و صادرات نساجی و پوشاک در
#گفتگو
با خبرفوری:
🔹
واحدهای بزرگ صنعتی پوشاک پس از جنگ با کاهش ۲۵ تا ۳۰ درصدی تولید مواجه شده‌اند و با تورم ۴۶ درصدی، قیمت پوشاک حدود ۲۳ درصد افزایش پیدا کرده است.
🔹
حدود ۳۵ تا ۴۰ درصد بازار پوشاک در اختیار کالای قاچاق است و ۶۵ درصد بازار از تولید داخل تأمین می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/692067" target="_blank">📅 20:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692065">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV3Zdkt14OC3p0mtao1ysQV3LPrE_OKzDPWaVoaPb9cdtC8dq2F630J-ClR3Xj5ANWRhrnlTd8kdKHrJSM-WRHkAweeY3nYP2U_S_YXUSHAaCn5c4H4JAMeHMYbk0K5unCB9hpoFsGf1gd_CKglRNmA8KSeAoOOjkO4FuBpNIpZF-i8H5QEX6DzOZ-9WJDc7PwHQIul2cCsqb-Oj5qCAmyOSnudq6elckpI9_mgmhZhzH-1llRZq5OWpq-i2vtkwaOmk5VtEGYmcvY3dNdPjvWduk2q7gx-N4vkvYjArwwl9gDlEdFnoV95ysds8PqN6set7GZ-CxwiwSDKEiCFCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اختلال در عرضه نفت عربستان؛ انتقام سخت از اروپا
🔹
تعطیلی خط لوله «شرق-غرب» عربستان در پی یک حمله، به لغو تخصیص نفت خام به اروپا برای ماه اکتبر منجر شده است.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3247212</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/692065" target="_blank">📅 20:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692064">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0EK2ndxQWP8dgyOmNtpLfDKWYvP1aiAXjRRH7uMpWh-SARzLDrZm72IU6JNB0IbMADpr9UIi_QpXo1uVoCSKWNzy-qok7QD2EyQZSrYZEqjCCxum1TBkjX8lz42p4CPma6b7gfOVXwJJ2-FtWT1Ih5EJX42ZK-v723dd08sU5DHxJlm-JC5x1bS9XfjpBTlOaV2PS0sMLLPsQnLRG0hRNa07-Hqulx3KZvYTNlApaGA_fcXQflwYLYt7hU6pnEceRuCpzVc85Q64c6XxK3NQ6QkJ859kP2v5GjOXBPMofGTTBSxJs-GrAvhYshrr6Khz9db94k9hNEVIBp9u4PUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب «جان‌فدا» در رسانه‌‌ی آمریکایی رویترز: تجمع نظامی جانفدا تهران را پر کرد
🔹
مقامات دولتی ایران گفته‌اند بیش از ۳۱۳ هزار نفر در این رزمایش شرکت کرده‌اند. در این رزمایش نمایشهایی از پهپادها ، سیستمهای ضدهوایی و سایر تجهیزات نظامی را در بحبوحه درگیری های مداوم ایران با امریکا و اسراییل را به نمایش گذاشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/692064" target="_blank">📅 20:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692063">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ترامپ مدعی شد: مذاکرات ما با ایران تا به امروز ادامه دارد و من معتقدم که با آنها به توافق خواهیم رسید
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/692063" target="_blank">📅 20:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692062">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fITJ8zwI8NjeV4-_GOsY7Xo4YtNt7IhahEU6cnGVDkeB5S2FdeBu_Dr6VnXAgYARBHqhbek0vOAOqJ8ohQ9JU5-gVF7W5wB2L2tbwDMn9MxRO1Gd_5HAQfULn9RoeopeQbk-X3_AVwrAUwdjMFRa3BgUCuu20P5zu2-xSrXM1xNYhc-YLLiVQaLck4w24ikxYx4W6JAW1SQ8L1CvrsuDGsUDHsi7d_SDEK7ekhvZ-wz6jg0BJikpMgVS2Rtfi6lPLR6utsLIkogjHgT1Tdfd_uMWDhJWMW7u5Xk-U04WQEg5BixOzdCdLi_-JxBfuSkpWh-PVWZtjSE4EMzzgJKPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش مصرف اینترنت در اینستاگرام
🔹
با فعال‌کردن گزینه Data Saver از مسیر Settings → Data usage and media quality، می‌توان مصرف اینترنت اینستاگرام برای بارگذاری عکس و ویدیو را کاهش داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/692062" target="_blank">📅 20:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692061">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">17-2 Ane Manaee (1404-02-02)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/692061" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هفدهم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
تجربه‌های نزدیک به مرگ، تلنگری برای بیداری دل‌ها. تجلی افعال حیوانی انسان در قالب چهره‌ حیوانات! [00:00]
🔹
مرگ، یعنی کندنِ انسان از تعلقات؛ یا اختیاراً دل می‌کنیم، یا به جبر خواهند کند [07:21]
🔹
تجربه‌ نزدیک به مرگ "ایمان"؛ روایتی از نشانه‌های باطنی، شهودی و شفاعت حضرت عباس علیه السلام [10:22]
🔹
"خوشمان نمی‌آید"؛ آغاز انکار حقیقت و تبعیت از هواست و عاقبتش "کرهُو ما أنزلَ الله"! [15:34]
🔹
تحلیل تاریخی-قرآنی، در تطبیق محتوای سوره مبارکه "محمد" با شناسنامه بنی‌امیه و نفی نگاه ابوسفیانی به دین [19:19]
🔹
تفاوت مؤمن و منافق؛ یکی قرآن در دل، آن یک قرآن بر سر. یکی مشتاق وحی، آن یک درصدد تمسخر و طعن [22:48]
🔹
انحرافِ نگاه منافقان به پیامبر (ص)، با زدن برچسب قدرت‌طلبی، ثروت‌جویی و زن‌بارگی به حضرت! دلالتیست بر «عَلَىٰ قُلُوبٍ أَقفَالُهَآ» [27:29]
🔹
تقوا نور هدایتگر و واکنش صحیحِ دل است به خیر و شر، و سرمایه‌ای برای پاسخ درست به نیازهای انسان [36:18]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/692061" target="_blank">📅 20:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692060">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b56d2c94b8.mp4?token=gMRd2cWHL6vVhkUhnbK6fK6bvHs5MVO-w4gaApRAJmk2Bq0AAcvRXIAGHRkdOjWZiOzNGItEZNOBAblruqLYKfJO0zbqHEcaVLmrDllyb6tGoHzS0suk1XbJn3b5gDC3V7OyJgGsgQu3QGUdJX-5S0cheOFYCJOrqOL-_l5mDBcUy0qpnsZpZpn-1WsKY_fuDTTX6GM9vRBTpJ9Oej8Og83uLE5O8dfqgmnFrNwfoUu_qEfyv2r5kXb8u7ZL5t2jqEaP4lXmk3rGxXv3_YHyZ5OxwTIFMBdwByQc19JKfLZ25xxzsRQCSbTrbKsE_IvzxFYrDEdIVEQXisFGAjW8h7JhHEwRLT5ao49PGbz0R7MC6wsdSQpg_DTEmm5aXYNoD3x7CbFKhom4DIIQVbNOXimCEoPeyxUsfyt9dMEGI3GA_MpKxH0wYhAYOEdBC9y3C93bS6pUX2Z80KeqQk4FsLsKBg-_ogy1KeFZhIJyEZGx_fSPoZI-MjD6GnkPsmRBI1cbHQYBkT5GJ01SEhj1IGP0BQ4zB6XfHkGEJgd_7oDUNgMi04p4RZ-onMED1K98jwq3FXJOl0mF2PgeXSUNbFnwSpACXB4ZtiXPA60BXwcFrXf0OxHzBPxg38j8Uzt7uUA7AVa0PkWy-FMD0JmAsHzM3NZxLSoS4qSKRd0UNpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b56d2c94b8.mp4?token=gMRd2cWHL6vVhkUhnbK6fK6bvHs5MVO-w4gaApRAJmk2Bq0AAcvRXIAGHRkdOjWZiOzNGItEZNOBAblruqLYKfJO0zbqHEcaVLmrDllyb6tGoHzS0suk1XbJn3b5gDC3V7OyJgGsgQu3QGUdJX-5S0cheOFYCJOrqOL-_l5mDBcUy0qpnsZpZpn-1WsKY_fuDTTX6GM9vRBTpJ9Oej8Og83uLE5O8dfqgmnFrNwfoUu_qEfyv2r5kXb8u7ZL5t2jqEaP4lXmk3rGxXv3_YHyZ5OxwTIFMBdwByQc19JKfLZ25xxzsRQCSbTrbKsE_IvzxFYrDEdIVEQXisFGAjW8h7JhHEwRLT5ao49PGbz0R7MC6wsdSQpg_DTEmm5aXYNoD3x7CbFKhom4DIIQVbNOXimCEoPeyxUsfyt9dMEGI3GA_MpKxH0wYhAYOEdBC9y3C93bS6pUX2Z80KeqQk4FsLsKBg-_ogy1KeFZhIJyEZGx_fSPoZI-MjD6GnkPsmRBI1cbHQYBkT5GJ01SEhj1IGP0BQ4zB6XfHkGEJgd_7oDUNgMi04p4RZ-onMED1K98jwq3FXJOl0mF2PgeXSUNbFnwSpACXB4ZtiXPA60BXwcFrXf0OxHzBPxg38j8Uzt7uUA7AVa0PkWy-FMD0JmAsHzM3NZxLSoS4qSKRd0UNpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: مثل آدم گواهینامه موتور را به زنان می‌دادید!/ گشت ارشاد و ماجرای مهسا امینی نتیجه یک تصمیم اشتباه بود
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
گشت ارشاد کاری کرد که آن اتفاق افتاد و ماجرای بنده خدا خانم مهسا امینی پیش آمد.
🔹
فیلترینگ ایجاد کردند و ماجرای مافیای فیلترشکن درست کردند.
🔹
تنها نماینده ای که گفت به زنان گواهینامه بدهید من بودم.
🔹
اگر آن موقع گواهینامه می‌دادند الان زنان قانون شکنی نمی‌کردند که بدون گواهینامه سوار موتور شوند و نیروی انتظامی نگاهشان کند.
🔹
قانون در این باره اشتباه بوده است؛ مثل آدم خودت گواهینامه می‌دادی که امروز نگویند ما مجبورشان کردیم .
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/692060" target="_blank">📅 20:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692058">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38a2196b2.mp4?token=RrneymVz3Z6gSragagQXDppPmY4MAkoNc-lbgFWUQFybEwg8ACh_a9Bf_zs2q4g_lb8d_G3a3ml_e5rB11VwDdRMpA-hRYcnTjPV9GdUV5O6KL-M6P_V4khTzzzV1H0o6NW6hmiKwyfZNVTGUwUdoXtdp2SAeOBXIb9KxQSnQIwY9b6IKSfAo6-RtnvLAAv6pBaUG4d0oqA9IyTGXZ3PtmIvaYkHyxZLSEfjOwh-LxIzV7nxKtFbR83JGJngKzrWQZxY6H7lhsfEpC8-k1mBzL7H0UP5vTZL7Ci4biloB1en09Sqm4N4hWTDoklmf-wx6JzTrH4pb1FY_O32QkXQSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38a2196b2.mp4?token=RrneymVz3Z6gSragagQXDppPmY4MAkoNc-lbgFWUQFybEwg8ACh_a9Bf_zs2q4g_lb8d_G3a3ml_e5rB11VwDdRMpA-hRYcnTjPV9GdUV5O6KL-M6P_V4khTzzzV1H0o6NW6hmiKwyfZNVTGUwUdoXtdp2SAeOBXIb9KxQSnQIwY9b6IKSfAo6-RtnvLAAv6pBaUG4d0oqA9IyTGXZ3PtmIvaYkHyxZLSEfjOwh-LxIzV7nxKtFbR83JGJngKzrWQZxY6H7lhsfEpC8-k1mBzL7H0UP5vTZL7Ci4biloB1en09Sqm4N4hWTDoklmf-wx6JzTrH4pb1FY_O32QkXQSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۵ سال بعد از ۱۱ سپتامبر یکی از فرماندهان میدانی القاعده و داعش، سوار بر کادیلاک و با گارد حفاظتی وارد نیویورک شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/692058" target="_blank">📅 20:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692057">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc71aef13c.mp4?token=K1vUAxc8KV5JQfWJzO_Ipet4rrUnZ1xsnk9jc6Xo2hUQXAzCsx5E0n2RsuhNm-fUY3PbQPiTXtMQXdlddfPhICjMBQZc84bUCUIiCRvpoa5zXjCzYNQQNvPHQaHEiyZQry6sbzlBg5oh5ijYoe35nG01P2wEutvEycjAnbpKJ5lvB0s_jKjoH2YBsxhiaN9ImObdwKuL7XI92BPveM0Lb6b032hXyO4vP9gh23EK_OCHIFzbGB7mlEudcPg3FpNGPL9kMMO-aPavl5hBYR2dowL6Z2zaWjyrEnjmLoG1rH4YUHEJ6gqAoB6yj8jW72FUYAhjdvHwxmCa9f8iw1KHmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc71aef13c.mp4?token=K1vUAxc8KV5JQfWJzO_Ipet4rrUnZ1xsnk9jc6Xo2hUQXAzCsx5E0n2RsuhNm-fUY3PbQPiTXtMQXdlddfPhICjMBQZc84bUCUIiCRvpoa5zXjCzYNQQNvPHQaHEiyZQry6sbzlBg5oh5ijYoe35nG01P2wEutvEycjAnbpKJ5lvB0s_jKjoH2YBsxhiaN9ImObdwKuL7XI92BPveM0Lb6b032hXyO4vP9gh23EK_OCHIFzbGB7mlEudcPg3FpNGPL9kMMO-aPavl5hBYR2dowL6Z2zaWjyrEnjmLoG1rH4YUHEJ6gqAoB6yj8jW72FUYAhjdvHwxmCa9f8iw1KHmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
سرمایه‌گذاری را از همین امروز شروع کن!
✨
🪙
خُردخُرد پس‌اندازت را به نقره ۱۰ گرمی تبدیل کن و برای آینده‌ات سرمایه بساز
📈
💰
💎
نقره ۱۰ گرمی خاتم‌چی؛ شروعی کوچک برای یک سرمایه بزرگ
🚀
🤍
https://t.me/khatamchii
☑
ثبت
سفارش
و
مشاوره
خرید
:
📱
09120715100
☎️
02122477938
خرید
از
وب‌سایت
:
🌐
Khatamchi.com
▪️
@khatamad</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/692057" target="_blank">📅 20:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692056">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگر قصد خرید دستگاه بدنسازی یا تجهیز باشگاه داری
👇
👇
🏋️
می‌خوای باشگاهت رو تجهیز کنی، ولی نمی‌خوای سرمایه‌ات یکجا خرج بشه؟
حتی به صورت از دم قسط و با کمترین پیش پرداخت ، باشگاهت رو راه‌اندازی کن.
✅
قیمت‌های مناسب و رقابتی
✅
۱ سال ضمانت کامل
✅
۱۰ سال خدمات پس از فروش
✅
تحویل حداکثر ۱۴ روزه
خرید و تجهیز بیش 300
محصول باشگاه
(مشاوره رایگان )</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/692056" target="_blank">📅 20:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692055">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf7dd0c45a.mp4?token=dnewg-smQ9yH04_DJvxTpURR-XUBABpsfIrIQsJfznBmJMetwZvtcWo8_Y2akhuBTpTIN_a6qW8Zldd6KLDseWfTKIgTMFv5H3qcgbyzIucMXMBCTgf32PDV5iZesa0KRrpprKZ9l_9fjkkxuM0Z12i8aQSW5ZSLhgdaQtKysw--MIuP3bMM3hYH43izymJCjLlIHLv0P7xS7mRHrLZIWHZq8p37pzQYQ_Ge7cmbz7rXRqVD-U7uSSH6uosiImJ0kjrNHIx-H0v1PTnZhcRqnPp0gN4wNFD4cLbzS8BK-nWWBCodjCuYeL0C-Y3twIk29rm9DJ3eJapRPHQw0Wk6IoR4wHJMdEBmUDwe506y7CVTLctzyUhu2HQMCM0JnOO2bLiBNQWcn2JTs954TpCZSbMqcmsMwgreO8o3zRvPVMXlX_zReSS97wTBzAuBAdJNisBvwbMluBqA5kOD11LNGs6jjRNvVDxH7zmvkzwex4-7yJIJftbA7SzwIqs4jf-GxnhXVYMb-dWMUJLEwvvFj0k2mE5Zt3wj50rhRWg1OR1H4REUye363WHA4WEwnO8WZmSZRL-Lld194tldWkzJ6rrRZw7FfIgi9dSgSkllcC5n1uNUTd8HRb_6nhiY1c1VPvGOyrV0qB6MYrSOGopXfGiTiA5qq8D9fjJgJhl-VzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf7dd0c45a.mp4?token=dnewg-smQ9yH04_DJvxTpURR-XUBABpsfIrIQsJfznBmJMetwZvtcWo8_Y2akhuBTpTIN_a6qW8Zldd6KLDseWfTKIgTMFv5H3qcgbyzIucMXMBCTgf32PDV5iZesa0KRrpprKZ9l_9fjkkxuM0Z12i8aQSW5ZSLhgdaQtKysw--MIuP3bMM3hYH43izymJCjLlIHLv0P7xS7mRHrLZIWHZq8p37pzQYQ_Ge7cmbz7rXRqVD-U7uSSH6uosiImJ0kjrNHIx-H0v1PTnZhcRqnPp0gN4wNFD4cLbzS8BK-nWWBCodjCuYeL0C-Y3twIk29rm9DJ3eJapRPHQw0Wk6IoR4wHJMdEBmUDwe506y7CVTLctzyUhu2HQMCM0JnOO2bLiBNQWcn2JTs954TpCZSbMqcmsMwgreO8o3zRvPVMXlX_zReSS97wTBzAuBAdJNisBvwbMluBqA5kOD11LNGs6jjRNvVDxH7zmvkzwex4-7yJIJftbA7SzwIqs4jf-GxnhXVYMb-dWMUJLEwvvFj0k2mE5Zt3wj50rhRWg1OR1H4REUye363WHA4WEwnO8WZmSZRL-Lld194tldWkzJ6rrRZw7FfIgi9dSgSkllcC5n1uNUTd8HRb_6nhiY1c1VPvGOyrV0qB6MYrSOGopXfGiTiA5qq8D9fjJgJhl-VzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: علی لاریجانی چند ساعت قبل از شهادت، افطاری مهمان پزشکیان بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/692055" target="_blank">📅 19:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692054">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08dd8bdd37.mp4?token=ewmMzFkurw9mGoG6WCZ3H1FxpjszLlie3CXfZAu_7je2XE3JYoj1gww5BhXGqJijnLFzBXQOAAIGzJ5bt9dflqDBhCoEdW7IIwdnMOrc8cpbzWKBLCi_sK_Z2SIleBsJawmddD3ztK9MdeR31vZAxdBoAWMyFa7IaN_17eTZIKj62mUeDGvcWxGMn-OVyRPDN4ZjBpfy4FqPjcLtCXAW6SvmLX0rNS9IrNHmK7Z5WfFGgpR-aMDPvgoQA9_pDFthbexDQAxneeyNlVF-SGpWIocF0kYV5lBWYHXgqNtW5MLYc6M4zfiuaGLlFp7PlmsRga-hSknNc3pnTyuqafgjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08dd8bdd37.mp4?token=ewmMzFkurw9mGoG6WCZ3H1FxpjszLlie3CXfZAu_7je2XE3JYoj1gww5BhXGqJijnLFzBXQOAAIGzJ5bt9dflqDBhCoEdW7IIwdnMOrc8cpbzWKBLCi_sK_Z2SIleBsJawmddD3ztK9MdeR31vZAxdBoAWMyFa7IaN_17eTZIKj62mUeDGvcWxGMn-OVyRPDN4ZjBpfy4FqPjcLtCXAW6SvmLX0rNS9IrNHmK7Z5WfFGgpR-aMDPvgoQA9_pDFthbexDQAxneeyNlVF-SGpWIocF0kYV5lBWYHXgqNtW5MLYc6M4zfiuaGLlFp7PlmsRga-hSknNc3pnTyuqafgjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از فردا ساعت کاری کشور تغییر می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/692054" target="_blank">📅 19:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692053">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a50921ed.mp4?token=SvEyZebcOUfyq48VP1338gmdDiYKyo4jcULsZfcg-jj7C0NcljT6AtDFAYGzgef9ZdDMG4ZKakOtreWdeSN3vRsLPYYS8bQANAJiQATS6CdzxsAP5NL7ndgVYsBpCwWUoR89RMWqt3QjUyIIcT6-2XxNRCNpTltkehMaHuR81jIzXOAJ0isNRzBhU-fDjtyxxKHF8TeMykW0IVuwziv5q2mv60nnOwdS1TsOWOLnxFRR2UCX3RlWtvntzpiwjc6Bvne_jkCIxvQ7_F84o9HmnhoDElF-p7MSMddBsSAwxHy5a6eMBhqd9721iYSdTP4sN6L3J8zfDtWzp6enM5SyiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a50921ed.mp4?token=SvEyZebcOUfyq48VP1338gmdDiYKyo4jcULsZfcg-jj7C0NcljT6AtDFAYGzgef9ZdDMG4ZKakOtreWdeSN3vRsLPYYS8bQANAJiQATS6CdzxsAP5NL7ndgVYsBpCwWUoR89RMWqt3QjUyIIcT6-2XxNRCNpTltkehMaHuR81jIzXOAJ0isNRzBhU-fDjtyxxKHF8TeMykW0IVuwziv5q2mv60nnOwdS1TsOWOLnxFRR2UCX3RlWtvntzpiwjc6Bvne_jkCIxvQ7_F84o9HmnhoDElF-p7MSMddBsSAwxHy5a6eMBhqd9721iYSdTP4sN6L3J8zfDtWzp6enM5SyiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیئت رژیم صهیونسیتی در جریان سخنرانی اردوغان، رئیس‌جمهور ترکیه در مجمع عمومی سازمان ملل، سالن را ترک کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/692053" target="_blank">📅 19:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692052">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
روبیو، وزیرخارجه دولت تروریستی آمریکا: درست است که قیمت بنزین بالا است اما اگر ایران سلاح هسته ای داشت، قیمت سه برابر می شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/692052" target="_blank">📅 19:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692051">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
استیضاح میدری، وزیر کار تصویب شد
🔹
در پی یک جلسه پرتنش چهار ساعته، نمایندگان استیضاح‌کننده احمد میدری، وزیر تعاون، کار و رفاه اجتماعی، از توضیحات وزیر قانع نشدند؛ به این ترتیب، طرح استیضاح میدری تصویب شد و برای بررسی در صحن علنی مجلس ارجاع خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/692051" target="_blank">📅 19:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692050">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mauIdanrkM4OriTpXJTxM29tJgZblgFoPbp-eC7jv0lpo7cJycIEk2ppXoUbVlA0RmATtYorCVIhuzRPSMauq7qZj-GDuUF8_21b-Cc8vxEHQAjNU4WZNdKI7BDq0f1VYEScOhwSKJsgoXvodni1A-7hKwBwUxKBipHWLP3kjHVqlT4pFfWQaq0yjmPO7EB8nAsxCDyXx9FgygHEj2nelWDanoIZXUOEJ_yEtKfyFFyZ3zpBY3PltvNQEiqPktO8EQHF3dCS6plrRNwHMvIp8pvlFD7PkD7dDx8dthCiA8b0NCvPHbUsLOOLo1gAY6xrdA3yQ5Iz7ODH1F2EM-8g7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای مصالح ملی
🔹
مسعود پزشکیان امروز در میانه جنگ ایران و آمریکا راهی نیویورک شد تا در مجمع عمومی سازمان ملل حضور یابد و مظلومیت ملت ایران، جنایت‌هایی که رخ داده و بی‌اعتمادی‌ها به آمریکا را برای دنیا بازگو کند. همزمان سخنگوی سپاه با بیان اینکه مذاکره به معنای سازش و صلح نیست، بلکه صحنه دیگری از جنگ است گفت که اگر مصالح ملی ما در این است که در کنار جنگ، مذاکره هم داشته باشیم، باید مذاکره کنیم. آمادگی صددرصدی برای جنگ، به معنای نفی مذاکره نیست.
🔹
هشتصدوشصت‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/692050" target="_blank">📅 19:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692049">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olk5_RJe1DU8H5ktss1e-89gJV0H_gt4kbHcHy6xI7m_1lEX2YF6b7a6QoE6MmTwS2QzH8nmX-7HGJx_XdlUdIcGVW4jiRR9gLTsOL41C3S87RcAxF145gRahR9iCRy-doxrAmVLBD5J0BpdZfJ9OtHa02JXEF_MGCZPcWWWoW5N7u-CVVA_KP2IOdw6J053GW8w139U4hQR2P6DDijG1tmD6gc-yg1uZJ1vHuf8bURMXoSDBZG1GkYDC6Fnp9Hw1XUOp_3AJrRR3EH32YjvF6HQf7W98Jk1JmyPghnSAbDNpfTpD-ImuXQYIlg9g85UHgXttB26eiL_3csY9Yzm5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران پرچم‌دار مهر
🔹
همزمان با روز پرچم و آغاز مهر، ابرپرچم‌های ایران در ۲۲ منطقه تهران به اهتزاز درمی‌آیند.
🔹
این رویداد با مدیریت سازمان زیباسهری شهر تهران با هدف گرامیداشت نماد ملی ایران، تقویت هویت شهری، ایجاد شور و همبستگی میان شهروندان و پیوند نمادین گستره پایتخت با یک پرچم برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/692049" target="_blank">📅 19:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692048">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
سخنگوی سازمان غذاودارو: کارهای واردات ۲.۸ میلیون دُز واکسن آنفلوآنزا انجام شده و مردم باید چند روزی صبر کنند تا وارد کشور می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/692048" target="_blank">📅 19:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692047">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران در سخنرانی سالانه مجمع عمومی ملل متحد: آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد. #Devil…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/692047" target="_blank">📅 19:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692046">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFe_NYfD64gcjG24sIQ0SE5SblM6GtJPQ89YQ_WmaTsfgBoXVzdSth5yj_K1QPzESmFTOt8s4Bb9sflTAtEPPkQ_eaD0PmyIH0y5GoP97_EVRyt15_2W_zQq4eSZnYTiFVscOvhvo2Wk37OGpNri4krZe_eNVvRO1o6sPKzmeNEPDwUbpHdAAebE8dP3j61j25cGSAsRgLicfX8zeH0Z8kIr9tAacDYzc5g3dEHqjBvPTIQNYJ7f0jJ8KkF-rV45AgWbGBhzi3wOnjhel4Gt13MLRUlrddVKuEodwTaOfgQs6o-dZQs4edhssXtCkvB_sUg4DgtR4A2UD7c_85fPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نکاتی که در اجتماعات شبانه باید رعایت کنیم
🔹
پرهیز از ایجاد ترافیک و اختلال در عبور و مرور
🔹
رعایت حقوق شهروندان و جلوگیری از اذیت و آزار عمومی
🔹
تنظیم صدای باندها در حد متعارف
🔹
خودداری از ایجاد آلودگی صوتی در محله‌های مسکونی
🔹
حفظ نظم و آرامش در برگزاری اجتماعات
🔹
ساعت اجتماعات شبانه: ۱۹:۳۰ تا ۲۱ (با بازگشایی مدارس)
🔹
پرهیز از هرگونه رفتار تنش‌زا
🔸
با احترام، مسئولیت‌پذیری و همدلی ، اجتماعی باشکوه و امن داشته باشیم.
@Alo_fori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/692046" target="_blank">📅 19:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692045">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
جریمۀ عبور غیرمجاز از هرمز: ۲۰ درصد ارزش بار کشتی متخلف
سخنگوی کمیسیون امنیت ملی مجلس:
🔹
بر اساس مواد قانونی جدید تصویب شده در‌ رابطه با تنگۀ هرمز در کمیسیون، متخلفان در عبور از تنگۀ هرمز علاوه بر پرداخت جریمه‌ای معادل ۲۰ درصد از ارزش محموله، با توقیف موقت شناور تا زمان پرداخت جریمه نیز مواجه خواهند شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/692045" target="_blank">📅 19:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692044">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
فعالیت مدارس استان هرمزگان ۲ هفته مجازی شد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/692044" target="_blank">📅 19:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692043">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfPYw4lO6oqb2LRwqThtrbfO4N66DUCHu6gsX0qqPCnOa84DmVxJ2Rp2AVYxtBeuL-R6tYM1o31SLZ1qtOP_jgUstLhVRJN_wEgfYBdr66Td-3LynYkk5eOdKoGfsFFD41liYxgfsmeNCUkDBDMJsdnrlDs8S944w-6OJdUPf8beMik1Mmrm6hmfZLSnBCoIdww9OxN9lEdabPQVjDepWRjDJXVWy5_fFPSwHvAGRYb79X0dwHsvHrzLjVyY805kCurI1cN67R2F1PgNvtub29nV3HOGyyj8m4F5EIUwMD8vsDRoBNTANc1j0g2umfXQAI6rKEPb3OK3Vb6cux3H9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صورت‌های مالی سال ۱۴۰۴ بانک صنعت و معدن تصویب شد
🔹
مجمع عمومی بانک صنعت و معدن با حضور دکتر مدنی‌زاده، وزیر امور اقتصادی و دارایی و نمایندگان اعضای مجمع برگزار و صورت‌های مالی سال ۱۴۰۴ بانک تصویب شد.
🔹
دکتر مدنی‌زاده ضمن تقدیر از عملکرد مدیران و کارکنان بانک، بر حمایت از واحدهای تولیدی آسیب‌دیده از جنگ و بهبود ساختار مالی بانک تأکید کرد.
🔹
دکتر شایان، مدیرعامل بانک صنعت و معدن نیز از کاهش مطالبات غیرجاری از ۳۷ به ۲۹ درصد، وصول ۹۰ همت مطالبات ریالی و ۳۹۲ میلیون یورو مطالبات ارزی خبر داد.
🔹
وی همچنین به رشد ۶۰ درصدی سپرده‌های ریالی و کاهش قیمت تمام‌شده پول از ۱۶.۳۵ به ۱۴.۳۸ درصد اشاره کرد.
🔹
دکتر شایان افزود: در سال ۱۴۰۴، ۱۰۶ طرح بزرگ صنعتی و زیرساختی با تأمین مالی ۶۹ همت به بهره‌برداری رسید و بیش از ۳۵۰۰ شغل مستقیم ایجاد شد.
🔹
همچنین ۴ طرح نیروگاهی با ظرفیت ۸۱۰ مگاوات وارد مدار شد و تسهیلات صنایع کوچک و متوسط ۶۰ درصد و حمایت از شرکت‌های دانش‌بنیان ۶۲ درصد افزایش یافت.
🔹
در جریان جنگ‌های ۱۲ و ۴۰ روزه نیز بیش از ۸۷ هزار میلیارد ریال تسهیلات، به‌ویژه برای زنجیره تأمین غذا و دارو، پرداخت شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/692043" target="_blank">📅 19:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692042">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ce749448.mp4?token=WZDw14h-93XdARVymvZOffwzppcAgsZzm5Tb0gUNQUAdffoETZSRWeqewYMyTJLOY5wAruc_ITNcMF0t0K00G2L_D6uVN-Uzoz3a4hRkvL5CnWcSiFLtMdiN1UFU-i-jMSScsvo_10slNJ9DiWkovqG8-K9OqvrhRbkE77fctNVdVG5CUEGa7G1RC8LeoJsLmJvcIX97lWhv5Z0FovTikmJDVBSH5BZHc8FHfIC6rgu79PAd2GDuJVmZLu0ez6mmjuiwojDpn8M4JtZalHoUoksCkSeN-Pd0t2Wy1wTNwPKHVkW_mid9fraIAD1-4DC-WLBvT8C5TepBmk2wBA1PVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ce749448.mp4?token=WZDw14h-93XdARVymvZOffwzppcAgsZzm5Tb0gUNQUAdffoETZSRWeqewYMyTJLOY5wAruc_ITNcMF0t0K00G2L_D6uVN-Uzoz3a4hRkvL5CnWcSiFLtMdiN1UFU-i-jMSScsvo_10slNJ9DiWkovqG8-K9OqvrhRbkE77fctNVdVG5CUEGa7G1RC8LeoJsLmJvcIX97lWhv5Z0FovTikmJDVBSH5BZHc8FHfIC6rgu79PAd2GDuJVmZLu0ez6mmjuiwojDpn8M4JtZalHoUoksCkSeN-Pd0t2Wy1wTNwPKHVkW_mid9fraIAD1-4DC-WLBvT8C5TepBmk2wBA1PVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون از آپارات شکایت می‌کند اما از تصاویرش برای پخش زنده مسابقات آسیایی بهره می‌برد!
بررسی تصاویر پخش شده از شبکه ورزش و شبکه سوم سیما، نشان می‌دهد که صداوسیما در پوشش زنده برخی مسابقات آسیایی ناگویا، از تصاویر آپارات اسپرت استفاده می‌کند و لوگوی آن را می‌پوشاند!
این در حالی است که تلویزیون از آپارات بخاطر انتشار چند ویدیو از برنامه‌های تلویزیون آنهم از سوی کاربران این سایت کاربرمحور، شکایت کرده و دنبال محکومیت چند هزار میلیاردی است!
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/692042" target="_blank">📅 19:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692041">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXL1I6ZCFUvBPUw8PfSur838UhALGK8qYiwo8GmOr7aTO-fkQQb-zf9Ohnc3vKVn_qgFEZGzlDXEv_0C4zxh6XFuodfSKmCbDGYVjCPwOfwhc4YoHJBtaz4b7Ir0EXPALIZKx4Zum_qmDKfqTvO9NC7zlyKby47dsZQrY0JzmfaExrsyQKvehLlRRtrSSTuta5vxMoGqJcCuI3Rrw-LmA47dNSbmX_kFBeFvlw1nCQsbqKzoEXfuZ1MmCHVmpIlmaHb18ZP57qu2VRIYQ9on1_fRiCZJp2HhJSluQyAglOOCKsMdTmO6CSdTyZ1K8XLWTNGge8ntcuSXofjLwWE89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا مردم طلای فیزیکی را به طلای آنلاین ترجیح می‌دهند؟
🔸
در این نظرسنجی بیش از ۱۹ هزار نفر شرکت کردند؛ سهم روبیکا حدود ۵۱، بله ۲۴ و تلگرام ۲۵ درصد بود.
🔸
بیش از نیمی از شرکت‌کنندگان، بی‌اعتمادی به سامانه‌های آنلاین طلا را دلیل ترجیح طلای فیزیکی عنوان کردند و حدود ۲۸ درصد نیز حس امنیت و مالکیت را دلیل این انتخاب دانستند.
🔸
اعتماد به دارایی ملموس و نگرانی از ریسک پلتفرم‌های آنلاین، از دلایل اصلی این ترجیح است.
@amarfact</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/692041" target="_blank">📅 19:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692040">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-5Bp3BjirKxF9Gm8-XfZg3n6SL9kta-4cniK7bFzQ1sRG6hGyI5BsvJRmNGJG_nH2NrgybY5ZqkmmprJophkCnw9LBTRez8ytF2Zidtvfn8GPs5a6wwuF7McnvqKAbtC4LGBZ-AC5xT5PCHp7Tu_EpKlEI2sF5elpgxW8n0c5kHyjKGNCpHnrgIbkihTKC8841t3fpw76f63NSgS4z78PKOzLArAo8A-ezaLTmq-JLMopZdWnm9BfUTPdHKB5F-yTYq8Kb23lohPdG87nIoT5G81CFGfC8ezZ1GSKqXdwFp3szD1lpn4-mY7agZvdfz5i7M5m_7tpQRZdqfYJQhMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستخط رهبر معظم انقلاب خطاب به سردار سبد مجید موسوی فرمانده هوافضای سپاه
🔹
این نامه در دهم مردادماه نوشته شده است.
بسم الله الرحمن الرحیم
برادر مجاهد و دلیر جناب سردار سید مجید موسوی حفظه الله و ایّده
بعد التحیات و السلام؛
۱) بحمدالله گزارش ارائه شده که قبلا هم نسخه ای از آن را دریافت نموده بودم، دلگرم کننده و دلنشین است.
از مجاهدتهای خود و همرزمان گمنام و مظلومتان خیلی کم نوشته اید؛ همچنانکه رفتار مخلصین همواره اینطور بوده است.
امّا اثری که به حکمت الهیه از این خصوصیت ناشی می شود ان‌شاء الله، محبت و اعتباری است که حضرت حق جل و علا برای صاحبان اخلاص قرار می‌دهند و انواع برکتها و پیروزی ها
۲) در مورد زنجیره تامین ان‌شاء الله تلاشها ادامه یابد و گزارش آن مرتبا به اینجانب منعکس گردد.
۳) مراقبت از جان عزیز خودتان و همه برادران خواسته موکد اینجانب است. امید است با دعای خیر و پر برکت سرورمان عجل اله فرجه الشریف امور سامان گیرد.
سید مجتبی خامنه ای
۱۰/ مرداد/ ۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/692040" target="_blank">📅 19:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692039">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ادعای یک مقام عراقی: به فرودگاه‌های عراق اطلاع داده شده است که از نیمه‌شب امشب ورود هواپیماهای ایرانی به این کشور را ممنوع کنند
🔹
اقدامات انجام شده علیه هواپیماهای ایرانی در راستای تحریم‌های آمریکا است/ هم‌میهن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/692039" target="_blank">📅 18:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692038">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74826c43ce.mp4?token=JIdsk-J6NmRZLu_J6cbiPfn47aI37Ws0eSg9XiqQsCtgr20AwT4kbBt5RJMryhGIq0lidpzqjARriQpXK1qYSAk6qKSwg7MYdKU7Br-ihNMFWBxuZgfDCLEPWzHhs-rtKZsx_yDhD0Xt9P9UpblfylhEAPAK3C0tSb0kq96sN7JeQ13lvc8iSNIsZYlkez2yJ6rwWUJUy1aH9Yv6nfogNBcJlSuE1qfTXBs8qbDLdT9cHCvoQrPiUQNmbsJScIKepg2tNJn6YwiHxBATw5Gy5FABkUcuDpzdd6mMkSuaShi5PBygsko3W6nC8j26UjqyVaIdtGMwLHeqFuz3GuH14w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74826c43ce.mp4?token=JIdsk-J6NmRZLu_J6cbiPfn47aI37Ws0eSg9XiqQsCtgr20AwT4kbBt5RJMryhGIq0lidpzqjARriQpXK1qYSAk6qKSwg7MYdKU7Br-ihNMFWBxuZgfDCLEPWzHhs-rtKZsx_yDhD0Xt9P9UpblfylhEAPAK3C0tSb0kq96sN7JeQ13lvc8iSNIsZYlkez2yJ6rwWUJUy1aH9Yv6nfogNBcJlSuE1qfTXBs8qbDLdT9cHCvoQrPiUQNmbsJScIKepg2tNJn6YwiHxBATw5Gy5FABkUcuDpzdd6mMkSuaShi5PBygsko3W6nC8j26UjqyVaIdtGMwLHeqFuz3GuH14w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: همه باید به‌جای «هوش مصنوعی» بگویند «هوش برتر»
🔹
از این به بعد، در همه اسناد آمریکا و امیدوارم در اسناد سراسر جهان، به‌جای واژه «هوش مصنوعی» (AI) از واژه بسیار دقیق‌تر «هوش برتر» (SI) استفاده خواهد شد. ببینیم این اصطلاح جا می‌افتد یا نه؛ خیلی بهتر به نظر می‌رسد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/692038" target="_blank">📅 18:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692037">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75daafbd18.mp4?token=tsOkshsTw4lgOhRZPdvxDF0vCvB54WnqjEN5ZLkBw0y-2X2I31vNwBu0drc9vhUkBlRCgIIUdpyhNVEbPmTN32QQbh0Nmfm69wVj8wXHO7l-6tw2kSjo1XYLwzrswzB5BgDqIlrBXUMst4IXpnn70z42rr8QEvzcqP86T2FaxTqwBt2FRFVXarewVNT-HJgELRQN43IkTAtWprAIlgQojV2BxNFC2kFDubmwVXbTUiPY7YMYTxu6KkTXlkujl5afYJPjThhSe6-KeMy2NS72BQH4lus6Y5dR-4Tv4UJTpcrnKfzYnprDeR_E44yPesohG_24exszkpWdEqX0F2WJkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75daafbd18.mp4?token=tsOkshsTw4lgOhRZPdvxDF0vCvB54WnqjEN5ZLkBw0y-2X2I31vNwBu0drc9vhUkBlRCgIIUdpyhNVEbPmTN32QQbh0Nmfm69wVj8wXHO7l-6tw2kSjo1XYLwzrswzB5BgDqIlrBXUMst4IXpnn70z42rr8QEvzcqP86T2FaxTqwBt2FRFVXarewVNT-HJgELRQN43IkTAtWprAIlgQojV2BxNFC2kFDubmwVXbTUiPY7YMYTxu6KkTXlkujl5afYJPjThhSe6-KeMy2NS72BQH4lus6Y5dR-4Tv4UJTpcrnKfzYnprDeR_E44yPesohG_24exszkpWdEqX0F2WJkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیئت دیپلماتیک کوبا در اعتراض به سخنرانی ترامپ، صحن مجمع عمومی سازمان ملل را ترک کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/692037" target="_blank">📅 18:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692036">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yco_2uLg7aIN5NHExwoBnonEoj3mOu2YZ-tuxgs7d8Gri8BxgUxYEBNHBpeUjHz3_KA7NQk3Sysfy4jEahIuuJDksvgV6oVUne5BrHGSZAIg-5SZ5gbAS9iG62EM_6oeGXXWUPcDGJSLzR9ZWaL2dCsMAPDNwNJhV-iq-N1T7_TG_z3XzYsINrXu1gL5V8HPoFQQzSnIJf3og5sfZPIobAx6PyW2iVKc8BOKMdALbKb-UmM-c3ZmG34FQk3oRZz-PqrpHjyhBj3cGd38OGWuCo_UI3aI7DgpIXKxR1OTwraBIeEJNRUp4SaSrtMXC0wAhzrfzOW-ja4Jg45nfIjI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
20 روز تا پایان مهلت شرکت در جشنواره حساب‌های قرض‌الحسنه پس‌انداز بانک اقتصادنوین
🔹
بیستم مهرماه، آخرین فرصت افتتاح حساب یا تکمیل موجودی برای شرکت در قرعه‌کشی چهاردهمین جشنواره حساب‌های قرض‌الحسنه پس‌انداز ریالی بانک اقتصادنوین است.
🔻
اطلاعات بیشتر:
🔗
https://enbank.ir/s/mfabaSE
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/692036" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692035">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0a87fd80.mp4?token=oU9XtlHi9vt07xaQtmMDeO2MjKdZMA2hDcSdpNBF0byOYBxrlmuslmIMank99A-eTI1mLlpMTFzhdCzopVFIYr2wk6Rj2aeIf1Vr1hw3o8GdEiTuj3sbnQbQEK_VBzyBe6axEfrSGBPJINrZAgK4CV3nBVUaAgFSpKdzPbgBvxBrwse-NNfdPFibs_ObPqbNLxdRiIISSVGFsOyrSIGWOWsOV_SJxETb775x-WKBVflE68m1LE9mJ-ltCts7fkjh58Dz-vSQax_s9ITDa3cYtlJ2DKKvoeX8TZ6WJY-pinC7xKGltc2wDbs6AQ5T8-iFIomEuJ7iBJf9-7MLa8-wVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0a87fd80.mp4?token=oU9XtlHi9vt07xaQtmMDeO2MjKdZMA2hDcSdpNBF0byOYBxrlmuslmIMank99A-eTI1mLlpMTFzhdCzopVFIYr2wk6Rj2aeIf1Vr1hw3o8GdEiTuj3sbnQbQEK_VBzyBe6axEfrSGBPJINrZAgK4CV3nBVUaAgFSpKdzPbgBvxBrwse-NNfdPFibs_ObPqbNLxdRiIISSVGFsOyrSIGWOWsOV_SJxETb775x-WKBVflE68m1LE9mJ-ltCts7fkjh58Dz-vSQax_s9ITDa3cYtlJ2DKKvoeX8TZ6WJY-pinC7xKGltc2wDbs6AQ5T8-iFIomEuJ7iBJf9-7MLa8-wVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا رسماً از شورای حقوق بشر سازمان ملل خارج شد
🔹
وزارت خارجه آمریکا این شورا را متهم کرده که به ترویج آنچه «ادبیات ضد آمریکایی» خوانده می‌شود، می‌پردازد و در برابر رژیم‌هایی که به سرکوب مردم متهم هستند، رویکردی مماشات‌گرانه دارد.
🔹
این تصمیم آمریکا یک…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/692035" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692034">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14050631_پیام_رهبر_معظم_انقلاب_به‌مناسبت_بازگشایی_مدارس_و_دانشگاه‌ها‌.pdf</div>
  <div class="tg-doc-extra">322.1 KB</div>
</div>
<a href="https://t.me/akhbarefori/692034" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📖
متن کامل پیام رهبر معظّم انقلاب به‌مناسبت بازگشایی مدارس و دانشگاه‌ها
🔗
rahbar.ir/s/2057
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/692034" target="_blank">📅 18:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692033">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4dde1774.mp4?token=ZNYDzFOZCflZf9gUnz8e5cHWvJVJcDj8jow5tZCeb5fjB31zy-aqZ-vXdqVGewm8N47k4v-V0RAN-MDMaeP9oaA8dEDkRYqWWJejM4w7MpqtQHjBDlzuZSPZyDm97IYH8x8AP7-8l94-N_dYqaFcnds9sFpXmeTAhDnZAvykOO3JtuyPT3ZGzi1CKi_WghpP6CKCqbN12PWDxDhRqk9cUzVNaFU7iz1H5IK6bEezcLDQsjxlh3ji-bXkOtHN3336TWmnEP0b4VCQNcYtZCYau4tnwvSbVvb1RkIMD3VjIcBvQlStU0uFLce0vG-UsoDoOaFuT-TD31mlyjb0vV5znA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4dde1774.mp4?token=ZNYDzFOZCflZf9gUnz8e5cHWvJVJcDj8jow5tZCeb5fjB31zy-aqZ-vXdqVGewm8N47k4v-V0RAN-MDMaeP9oaA8dEDkRYqWWJejM4w7MpqtQHjBDlzuZSPZyDm97IYH8x8AP7-8l94-N_dYqaFcnds9sFpXmeTAhDnZAvykOO3JtuyPT3ZGzi1CKi_WghpP6CKCqbN12PWDxDhRqk9cUzVNaFU7iz1H5IK6bEezcLDQsjxlh3ji-bXkOtHN3336TWmnEP0b4VCQNcYtZCYau4tnwvSbVvb1RkIMD3VjIcBvQlStU0uFLce0vG-UsoDoOaFuT-TD31mlyjb0vV5znA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فایننشال تایمز: ونزوئلا ۴ میلیارد دلار ذخایر طلای خود را به آمریکا منتقل می‌کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/692033" target="_blank">📅 18:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692032">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b72628889a.mp4?token=TFq6i1Kl6yYL_4D9JamMy3krEolU0sFfNiWU31DsZY5i81d8yLEbS8TS5-o7Y97sgwEV3tKt4aNT4w5FjL7Fz7-FWrgUldqEEgXiwanW92OTYnInXInN2fh3an-IYpM4WvBxR3H98zO-L_mRXKZiEAR20N0rOZuAGqKcDV4-5_gwIRHqIsTfKbkPX3MaAu3GVTSnCQ1CUtPEPC0KKuMTiNngJY1IhPu8k7ritTVC0c9MwyWd89jCiulIlzJQdCgKsrW3SzFuKC4f-o1fPC_NXLhc9VOWANSJgQK4MYB1Jqci-AvpcCkD5vd_K7oJ54VAZuh8WZOSyYeNyZW-cbYPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b72628889a.mp4?token=TFq6i1Kl6yYL_4D9JamMy3krEolU0sFfNiWU31DsZY5i81d8yLEbS8TS5-o7Y97sgwEV3tKt4aNT4w5FjL7Fz7-FWrgUldqEEgXiwanW92OTYnInXInN2fh3an-IYpM4WvBxR3H98zO-L_mRXKZiEAR20N0rOZuAGqKcDV4-5_gwIRHqIsTfKbkPX3MaAu3GVTSnCQ1CUtPEPC0KKuMTiNngJY1IhPu8k7ritTVC0c9MwyWd89jCiulIlzJQdCgKsrW3SzFuKC4f-o1fPC_NXLhc9VOWANSJgQK4MYB1Jqci-AvpcCkD5vd_K7oJ54VAZuh8WZOSyYeNyZW-cbYPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه یک معلم به والدین پیش از آغاز مدارس
🔹
یک معلم از والدین خواست هنگام تحویل فرزندان از مدرسه، با توجه به حضور دانش‌آموزانی که پدر، مادر یا هر دو را ندارند، از ابراز محبت شدید در مقابل دیگر دانش‌آموزان خودداری کنند تا باعث ناراحتی آنها نشود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/692032" target="_blank">📅 18:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692030">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ترامپ درباره ایران: آمریکا و ایران حتماً مسئله را حل خواهند کرد. ما به هر شکل ممکن این کار را انجام می‌دهیم. این اتفاق خواهد افتاد
🔹
این کار به‌سرعت انجام خواهد شد. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/692030" target="_blank">📅 18:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692029">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
التماس ترامپ دیوانه از سایر کشورها برای منزوی کردن ایران
🔹
من از تمام کشورها می‌خواهم که به ما بپیوندند تا ایران را به طور کامل از نظر اقتصادی منزوی کنیم، تا زمانی که از حملات خود علیه کشتی‌های تجاری دست بردارد، از برنامه‌های هسته‌ای خود منصرف شود و از…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/692029" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692028">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای ترامپ در مجمع عمومی سازمان ملل: من در مورد انتخابات مطلقاً هیچ اعتباری برای آن قائل نبودم و نخواهم بود. این موضوع حتی به ذهن من هم خطور نمی‌کند
🔹
تنها چیزی که برای من اهمیت دارد این است که ایران هرگز به سلاح هسته‌ای دست پیدا نکند.  #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/692028" target="_blank">📅 18:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692027">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای ترامپ در مجمع عمومی سازمان ملل: من در مورد انتخابات مطلقاً هیچ اعتباری برای آن قائل نبودم و نخواهم بود. این موضوع حتی به ذهن من هم خطور نمی‌کند
🔹
تنها چیزی که برای من اهمیت دارد این است که ایران هرگز به سلاح هسته‌ای دست پیدا نکند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/692027" target="_blank">📅 18:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692025">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ترامپ: فکر می‌کنم درست بعد از انتخابات میان‌دوره‌ای با ایران به توافق خواهیم رسید
🔹
من باید در مورد ایران تصمیم بزرگی بگیرم. آیا با آنها معامله‌ای می‌کنیم که به آنها اجازه دهد به کشوری بسیار بزرگتر تبدیل شوند، یا آنها را کاملاً نابود می‌کنم؟ #Devil
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/692025" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692024">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
دونالد ترامپ: ایرانی ها موشکی ساخته بودند که قادر بود اروپا را هدف قرار دهد و به آن بسیار افتخار می‌کردند؛ امیدوارم اروپایی‌ها این موضوع را درک کنند
🔹
هدف ایران این بود که در پشت سپر موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند. #Devil
🇮🇷
…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/692024" target="_blank">📅 18:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692023">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdsT038y706EgDPxRHJEffL4u9Y4je0CyR1lLtHQaUxKJ2fcoBV1PeQDy6bxJGiU4Lf827ucrdqfkZyq6y90gfhUH53mWdvTsj0xEIvshpXsdNuOV7XvPoiZ5z51b6_cc1lSdmkM8TLz45TP2cnlRVgq13G_yKJJHEmP4uUhEzOqnukZLJuZzfKOks_yLu_lIiOfWj1RZh2C5_lKxx6O4wf8O66D2qhmozbPLJZRu_pXyhJ6F-WkVH0WBFAG6t8M0Fi2Zyi6jm02NZ4uXsokOBfz9yiimqwfbaED_W4Hg9WIY2YXuDkGdY6K1Ng-i40pZAEwdDkl8DlgnaNHIbxKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دکتر «علی محمد خانکی» به عنوان معاون مالی و امور شرکت های بانک شهر منصوب شد
⬅️
با صدور حکمی از سوی دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر؛ «علی محمد خانکی» به عنوان معاون مالی و امور شرکت های این بانک منصوب شد.
⬅️
به گزارش روابط عمومی بانک شهر ، دکتر «علی محمد خانکی» طی مراسمی با حضور دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر و جمعی از اعضای هیات مدیره، معاونان و مدیران ارشد؛ به عنوان معاون مالی و امور شرکت های این بانک معرفی شد.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/692023" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692022">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران در سخنرانی سالانه مجمع عمومی ملل متحد: آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد. #Devil…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/692022" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692021">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879fa5c0b0.mp4?token=OwI0vwp8zQVb6nXLGUI7P86PKQuYsJH-Pyl6Pb43gALsy89FYr4MU9PfB3Q0XA-SWm8KfS6AIiKvS_-VLrsohPSJ0EW0cybazKk4ttP1RCkDKssjXFQjdCIY8aYFctpew9tGgYj-SBz4BhKWS3Xl0lXK_OGMmPUChirMV6iV8Bqid9O2zCON0JHcVpbddS2HXkjaMMs25B6Llq00Ab4RVR6Upi09AO8rcNkJnRhIv3uqH2XWSsSaTNcU9eY04Ff9PY0TOOeJAsN8sU3yc5ljas7jpldt-9fYGaFm9_5hla336JaNxLO8MAEJ8eFOEmLf2S1vCY3cCNWhyCG_6Ud1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879fa5c0b0.mp4?token=OwI0vwp8zQVb6nXLGUI7P86PKQuYsJH-Pyl6Pb43gALsy89FYr4MU9PfB3Q0XA-SWm8KfS6AIiKvS_-VLrsohPSJ0EW0cybazKk4ttP1RCkDKssjXFQjdCIY8aYFctpew9tGgYj-SBz4BhKWS3Xl0lXK_OGMmPUChirMV6iV8Bqid9O2zCON0JHcVpbddS2HXkjaMMs25B6Llq00Ab4RVR6Upi09AO8rcNkJnRhIv3uqH2XWSsSaTNcU9eY04Ff9PY0TOOeJAsN8sU3yc5ljas7jpldt-9fYGaFm9_5hla336JaNxLO8MAEJ8eFOEmLf2S1vCY3cCNWhyCG_6Ud1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران در سخنرانی سالانه مجمع عمومی ملل متحد: آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام:
هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/692021" target="_blank">📅 18:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692019">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-GJthSlUsU7p9Qt69pNKNnrlLMxqbigTdm57B5lEaU_Pota1JXgDrDlsj2b1Dzju3kyfPmbQERXqAZ9Mgy4Zi5QF6iCksCRmE9VVUZp3PG4w6vWc5Zv6oST65b8mRh1cYZGg2M6t8eX2_HWq50fYZUqXkI3S_iBnTEc9crnXQATQKjcF9sOLQ7SkeoReIRXtHoOit9e4g267dEXO_8_aXfjjyBFSHmnyQEc2xLsczZgggUOmZyvrMJcvfd2qtprSKNLBMx4wRGGVSx1fhxgw224O1MBwyyxA7bkw3lfjbVVnKi_1eroKx9uEBk9OqYAZt1W1mq9U2ZXdIx9SEv6PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برتری صنعت داروسازی ایران در منطقه
🔹
۱۴۰ کارخانه در ایران محصولات نهایی دارویی و ۸۰ کارخانه مواد اولیه دارو تولید می‌کنند و ایران در تولید دارو رتبه نخست غرب آسیا را دارد.
🔹
حدود ۴۰۰ کارخانه نیز در زمینه تولید محصولات جانبی و بسته‌بندی دارویی فعالیت می‌کنند.
@amarfact</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/692019" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692018">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
معلّمان، شایسته‌اند که مورد تکریم همگان باشند
🔹
ما همه وامدار معلّمان خود در هر مقطعی از دورۀ‌ تحصیلی هستیم. این قشر عزیز و محبوب که اغلب با خالص‌ترین عواطف شاگردان‌شان مواجه می‌شوند، شایستۀ آن هستند که در مجامع و زمان‌های مختلف مورد تکریم همگان باشند.
🔹
مناعت و قناعتی که نوعاً در ایشان مشاهده می‌شود، مسئولین امر را نسبت به وضع فعلی
#معیشت
ایشان قانع نمی‌سازد، و ان‌شاءالله با برنامه‌ریزی حکیمانه، برای بهبود آن تلاش مؤثری به‌عمل خواهند آورد؛ خصوصاً اینکه این مقوله فراتر از انجام وظیفه‌ای قانونی، امری است که از دل برمی‌خیزد.
✍
بخشی از پیام رهبر معظّم انقلاب به ‌مناسبت بازگشایی مدارس و دانشگاه‌ها | ۳۱/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/692018" target="_blank">📅 18:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692016">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oovb-LaEUfjpVg80hhPvjgORzZXaawmwIX00GRhYHBoZXKs7VvpJRFi1TKn7kn0FZYMFFjAEoPSWnZAlQfb-rF3V9z-3DSM8u39mm0q7IVyG3cKIVdfipfwIKlxfrgt47ApFQNf5dTW6OlUGm5J16YETdcM7REZL4Pmng3VUAygfY6QngcBxOKVuiZjakXaUQhqq5S2kKn4gUYAVso_I66Oc7Ei4PHrr0UxyRfhQl9xX3d8geHQN-_tWyoLiS5bc-xLErbJ1gyisfqtnhqNS_ch5vt8ovMNgVzX_hPNLC55BWqbUMGaftkZd-Pj61qEenm4jEXPPwzCnmcIHZr_Fdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آستانه سال تحصیلی جدید یاد دانش‌آموزان شهیدمان را گرامی می‌داریم
🔹
امسال روزهای خاطره‌ساز ابتدای سال تحصیلی، برای ما غمی از فراق فرزندان سفرکرده‌مان را تازه می‌سازد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/692016" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692013">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
♦️
رهبر انقلاب: فتح قلّه‌های پیشرفت، مأموریت تاریخیِ دانش‌آموزان و دانشجویان است
🔹
مسئولیّت امروز دانش‌آموزان و دانشجویان، سعی در مجهّز شدن به علم و تقوا، امید و اخلاق، و دانایی و توانایی و زدودن پرده‌های جهل و تاریکی است تا آنگاه که با شکستن مرزهای دانش…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/692013" target="_blank">📅 18:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692011">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌
♦️
رهبر انقلاب: فتح قلّه‌های پیشرفت، مأموریت تاریخیِ دانش‌آموزان و دانشجویان است
🔹
مسئولیّت امروز دانش‌آموزان و دانشجویان، سعی در مجهّز شدن به علم و تقوا، امید و اخلاق، و دانایی و توانایی و زدودن پرده‌های جهل و تاریکی است تا آنگاه که با شکستن مرزهای دانش و فتح قلّه‌های پیشرفت‌سازِ آن، مأموریت تاریخی خود در جهت اعتلاء ایران اسلامی را به انجام برسانند.
🔹
این مهم در جایی صورت می‌گیرد که خانۀ دوّم ایشان بشمار می‌آید. از این‌رو به این عزیزان عرض می‌کنم که لازم است همواره از حریم‌های آن به بهترین شکل صیانت نمایید و با ارتقاء هر چه بیشتر سطح آگاهی و بینش و تعالی رفتارها و منش‌هایتان، آن را کانون پیشرفتگی وطن خود بنمایید.
🔹
از فرصت حضور چند ساله در این مأمن دانش و ادب و نشاط و امید برای خودافزاییِ هر چه بیشتر بهره بگیرید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/692011" target="_blank">📅 18:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692010">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEgLtnQBpm9f7-pO_NRMQjaM_45LuehPB0TDYHpElsoxxWn8W9WhqnDMWNMnLXMWBn7aQief41IWp77fMt8ZCejVPbON7RApP92PhjvcwjUNkD9LU1OhYuLgf_oKXQc6T2SwLV6WQtyFHpCTfxAZSzb81UAVByGDPlTjPqryNDnezOCwOw86TEsTGZhR25UJHSYZJPftbmsxEiCjLbGfySHAuSxFw43O47V7RvZZDfCizbYIp4OiJek678xF7NRS3SSGRNwKIjmSP3E-JmhSndZFhILg6UFSv-djtCkoJYxhwRPPwMJRcQVZZj1mOA62OusRFPP7t0N5wOHU76qLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه بیش از ۴۰ نماینده به عارف برای بازنگری در ممنوعیت واردات لوازم خانگی
🔹
عضو کمیسیون اجتماعی مجلس، از تهیه نامه‌ای با امضای بیش از ۴۰ نماینده خطاب به محمدرضا عارف معاون اول رئیس‌جمهور خبر داد و گفت: نمایندگان خواستار بازنگری در ممنوعیت واردات چهار قلم لوازم خانگی از مسیرهای قانونی تجارت مرزی هستند.
🔹
احمد بیگدلی تأکید کرد: پیشنهاد نمایندگان، جایگزینی ممنوعیت مطلق با واردات محدود، کنترل‌شده و قابل رهگیری است؛ به‌گونه‌ای که واردات با سقف مشخص، ثبت و رهگیری کالا، رعایت استانداردها و پرداخت حقوق و عوارض قانونی انجام شود.
🔹
بیگدلی گفت: در این نامه از معاون اول رئیس‌جمهور خواسته شده است موضوع با مشارکت وزارت صمت، وزارت اقتصاد، وزارت کشور، گمرک و کمیسیون‌های تخصصی مجلس مجدداً بررسی و نحوه اعمال محدودیت واردات و حذف استثنائات تجارت مرزی مورد بازنگری قرار گیرد.
🔹
در بخشی از این نامه آمده است: حذف یا محدودسازی این اقلام در رویه‌های قانونی تجارت مرزی، ته‌لنجی و کولبری، نگرانی‌های جدی برای مرزنشینان، ملوانان، کولبران قانونی و فعالان اقتصادی این مناطق ایجاد کرده است./
ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/692010" target="_blank">📅 17:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692008">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7861846c96.mp4?token=Da6B4DiUPIkgnaHmRjw5FUIcisoD9FSE3VULXL-l6sffMOIYZefbgXx00Rwq1D4_XlVduxNSo7Yzb-HKeYmTDKF1yKpukIxMT8HXii9Po2zV0VFJuuJFbSXWfuKZJbHRfPKVZPTfZNs-ox6hhpy97hGTeTxfDYVTbBMKzBv88Yv-lILyebjYPYcP3vkSMHMDjrk-WVyYN5UoiBuFUqz8tW6LrhjnZ_LetsbsszZOIDMgI4Rx4kbGGirhjxk6VxFsJBYNGiAGVdibARvT0K0J7yab04O1M-3lt_rQ0hQrTAnOxNYDG-3moxYGGHpISlkyiGuPCY00C6KfdUVYVbowig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7861846c96.mp4?token=Da6B4DiUPIkgnaHmRjw5FUIcisoD9FSE3VULXL-l6sffMOIYZefbgXx00Rwq1D4_XlVduxNSo7Yzb-HKeYmTDKF1yKpukIxMT8HXii9Po2zV0VFJuuJFbSXWfuKZJbHRfPKVZPTfZNs-ox6hhpy97hGTeTxfDYVTbBMKzBv88Yv-lILyebjYPYcP3vkSMHMDjrk-WVyYN5UoiBuFUqz8tW6LrhjnZ_LetsbsszZOIDMgI4Rx4kbGGirhjxk6VxFsJBYNGiAGVdibARvT0K0J7yab04O1M-3lt_rQ0hQrTAnOxNYDG-3moxYGGHpISlkyiGuPCY00C6KfdUVYVbowig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ممدانی، شهردار نیویورک: نتانیاهو در صورت سفر به نیویورک برای شرکت در نشست‌های مجمع عمومی سازمان ملل باید بازداشت شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/692008" target="_blank">📅 17:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692007">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از دیپلمات‌ها: فرانسه با هماهنگی واشنگتن، تهیه پیش‌نویس قطعنامه‌ای را در مورد تشکیل یک مأموریت بین‌المللی برای احیای دریانوردی در تنگه هرمز آغاز کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/692007" target="_blank">📅 17:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692006">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
معاون سپاه: در طول ۴۰ روز جنگ، ۲۳ هزار اصابت و شلیک از طرف دشمن داشتیم که بیش از ۶۰ درصد آنها به مجموعه‌های نظامی، به‌ویژه تونل‌های موشکی و پهپادی، اصابت کرده
🔹
پایگاه موشکی داریم که در طول ۴۰ روز یک هزار اصابت به آن صورت گرفته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/692006" target="_blank">📅 17:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692004">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ممدانی، شهردار نیویورک: نتانیاهو در صورت سفر به نیویورک برای شرکت در نشست‌های مجمع عمومی سازمان ملل باید بازداشت شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/692004" target="_blank">📅 17:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691994">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTxshoYKEkYqydDakpG7yJXD_Xi25YkAjsmV5cdIwJlwXMyAYm1YPULZR0raNfxLoIOj7_0AqEPOKCzBoNZ7I4KYO04YlnKNtGVA4mz9An5PPRatctpaK8153v7ulkNLBCzZh0ubBMgdD6WUiTVAnjn3WESOTCM5PjQvbbw7jaO7_YzLj384lkRluqKH9dhoaIYTTa0HLLgUGeuNhMMiGROfzpPgWinBd_TbynwLZBoQr3yfC24X_rh1hXt7P7vt0iD9_0h1php65EGKGihsg9k41Uxc8zfGsDca_OB8awPJTVqS3NaErlSSSoJVkDLqhr5lsj3C20HKiIxJuvEGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d83XkxgI6h54r3PlvpQ1Tz7yRgn8VKiDbVkYan9F7gOXjxODN-a_AA_5mKDXu3jVM2rLLyekl8xTJRsoizvqEVPxW_yya5kpAeimv19bQ6XOu7nAmovpPr3YGddky93oaNnNq8RfqzAPfXX6ZOp82Twlvb-CChAANmGb_P8_t6Zt7gEE3p18o0Y7AjXK9MHNvn1tCVBEpQDggRcBx69iWJUUXYkqHKLN1QVNXR_nTSXVSdyEH_8MHh4POVRK6Y8p9DV3glu-fjma9udS1ZgXu00WKHmQNc3tQvv_XcZ6hGsjt4NqFcLxCumGG6EaFn2_p_AOZdrm3dbXBTj6I-NzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhg-Vz8_QL_Eo5KUEsX7zVoh_vo12huDUfPTEufkHpUJtLsqb03VkNwjpncqocg2fgFIxpSWOAX0SkDafrskLcFslPEC26rvIJo1EWJ-my0vll8-OIEMs7muUJ-NL6JCGw1r7xtFug1xmc4Ko9ZliS2qdLKkMDeMjyKe9jY2jhM85-Y7GTVEYb7Wnv1nACWmYszg0L4t_xkiFztM7nVSakUPK6fHLdSiXEjT0Diak9QEIRMVjDZduYXMPBKWSCtSPeI6Ukhaowqwef-MhJe56Wo3-DTC9pcKK8SUeE9xZdmUZ-dBR5KukoY6w4J0f4rHpUY0J_G-0ZjGVTfxL-SF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqU4QBwTgH5iIQFgdmyLsHyujEdAMUXCPHXXis_T8K7hUzEuiFIvvteYaF210kLrAHAL3SmDYse2xvRZL63ef2104lVxMZVRDn-tMY6irwBgKhghX-5ejbWgY4WQS_qnxKlXJA2a-N3ULdDUyKcakFUxDUHWOcCYvapH91KYszbd5Iz9nCbvJHtAtcP_5cEOhRKD8w3t4IQImKlpFt4gutuTs-dqaIWcdA2_SJ0QScEBdnEiwdR23-1VqZaSOpJX8jfr5o1SPlvy5U_09YKvd2qBlWRSyNykolPyUp4Jtr5saJTGqWsBVKl14cFfHmw0RKNb-Pn1kwhUiKoVgxk-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhSbHt3Hwlfissavey_jCuK0I9-Tkl0pv2KnWIfivCSUbdLwwPhA1mA-v1RZ-C5YUj04YhH_vdwwLW9DjtOcW8BxLD9Z4hjpcbvVUea9TgF8X23Hl6etpHzBt2_MpNZ3k0vSa0MUeTYcMqCdeyeJR9kCxmdX42S9NQyRiB_n6Ev7nGryhVYOHWt2mBTS2C9j0ARuOHppzEYpvWpZ68fmpiC5kY8JXunEFi4KXReBl3ujcsWy0MowwtLeVum73pPDYsG4hnMYqaAM90uKer7hq006qhUrEKHT_W18lxEPZ3C03K-K6BDgytD3WpKCpoaG8A96Wsd03rXdQ0c35lEVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-1B2lLnC8lPVgt0idexKTjFiRBwwGZjIAquJb71dTnbohcIxe1u4VScdDaOtTLUIKP9_Z079nvNcgTKInUa_46-anyo1V_eAqdCg4gtPHVc8Wtg7sPKOAuliZ5EFDjPyZlcCDVYV2nTK_6HBQtiKjqKDx3n8Me6Fas_Z3Co_q-GTLK2_drzs5FnmEyV0DmNGAEYCvWKxQ1lX-Ov_ddrxm5xb5WbedKdmUF7C-Zi1ipf-yn8XZIJZCM-YSHAYCj0KbNw0IbQgsqgtWxRhDrvIbDW_FNooO0uQCX46fpr7Fi0uCCwBkOGfTIfRraddU8QSpZyuAuLVZF3Nm2Be_Tl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sS-VDRZwlLasMU6GxJY65tMS3n5ZIbIIaERPY2yL4RxR2kwah_K3WGlm1dn9zSJh_8m2snnlESX_ai2lj7LM8N2Qy1vbXIs3h0bsXbgqFmIltI8GbcS5h2I9j6KkQ2qGumThAFQjRIJssg6Hg51jdY4FFxykUJYq2Spr06nKEUM8lRzqUX6qICZ90D1YTW0VCTNRNLAEPgMMIAeLWyNsMUTvt4E9hTiPB2Xyo0WzM-6RokVVozPwRqK9I_h3tER3Mz5ZVjIso_RYBQzT1HuuBhXGf0NI-IyciekaO_DdzlehcgeoOViv67SDvB7d86fb4uJzBVfXuPW45rKMYm07Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JPJQsbcZs1kUA-Yg2YIgU4a4ARxpcg7nCMR1aqlB7ozM13tuofpQcxSjUPqhmvmA847YtM13jdY9oj77Qyasg_35SxFyhYz5d839X2mI6q2bqhUuokSWRszz2tGz_8nwMEUOUApG_lAW1r4XhWKzdXRuxNiwwpAc5_mU-WZERXyQgQEdrH2ea9MNI9CcHEjdhlB2cw_2hH2Zoj3jD4jG7o1g97aHx4G94O_pxzdHZOZdajxlPHr0Au-n9XHSRCsq4Y3UXeOH7KodoJi8-Mzmjq3qBDOYWBTajFqS_MsII4-_sL6W77fNlZCuyOqVMEDoTm09X66tMbriKTP-bfvAVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVzXVJvMOu0xaTqUfHL7GCp6zUe0XGBn6X-Q_nTrZ_O1NCU8oPG30n45sa6Cswc8pP6N75SCnxx5AXWYwfl0ugxW8nJWDlpTBamrkaeSx6TtrD1qXqR2tAvQNNy3k9h7XyJMNOqfbZUhCCshZy7WoaHFBl3P5Bzs9RjC8AY4CZXpbMdkbkJHxtURl6sKjZD1JRiCYjzn89nHmhUpi-41HtvnUSCSTA3rvUZngubJ_6YdLD5HTQ3JT0Kj6khtWnmQHRAcpNqEBMep88ELpdUC0cX1YqXsbBlrQNyk9AnyvzK-avKZo7nXb8PUkwcUyDyP18qKAEB_ECi1FHqJXbmnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4mEqo_TKtoW7zQG0O_jwaaNCZ7PffuVnro1IOXjaDxy2u8ndAC5rvAL6d8HwrYj_FRQj1VmkvBLzGlgj3KvrygdyNgtMJvt2xjwYlkAcucXXhlUHlbiby5ey2tIKHVVs7be4R1P8XnuzmAVGZnSmNSn2OO5whAkq-c21TYgYPNvoNlwVznUEUsNPqBm7FF_XQZOP4uiygrCFAzTumXf7uoTjs9Xo6CZ_Vgj-iCANr0CV70Sz6H_AThwzft3-gL1uZvZxVb1jTce40goB_nOZYfn3e3Ij2URmqsCI-7HbTaVw52jnTgSY4wh2VLpcHpNbdxt-Y1H8TFWtQjarLVWVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
دغدغه‌ها و هزینه‌های سنگین تحصیلی و ثبت‌نام دانش‌آموزان در سال جدید
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/691994" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691993">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
منابع عراقی: تاکنون تصمیمی برای ممنوعیت فرود هواپیماهای ایرانی در فرودگاه‌های عراق گرفته نشده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/691993" target="_blank">📅 17:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691992">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be5e47fe60.mp4?token=IGTqXAWKwKnsoTtpLFQ9BKO0XJddiCA1ogrWQWQ7FEIRA-xbClOgTDZ5skcSEzwVS2neimW6mc1i9ryNOhUHbnk1acPSm-ff0L3N__kdb-8ZtErYF8P_NRHSwkfTvLqq8dpV-4YlqEfhl8nNKcC1rIwtf2szyzwgeNzRDxxQbiYjCTnY83qGkjv1hGcDhAtmEl2GirC0LvYIKfxChQ8uxwEt1xo05cYOq88D14PnJFTe8BbxMp5KLhKWfrZrVF2nqCoENXecFxErgyHGppx_DNgJNobXnNP0cRx0Avn552IPrh62jAVn9AMsKjynDTtdoGKrT1JSHWRJgdhTThy7WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be5e47fe60.mp4?token=IGTqXAWKwKnsoTtpLFQ9BKO0XJddiCA1ogrWQWQ7FEIRA-xbClOgTDZ5skcSEzwVS2neimW6mc1i9ryNOhUHbnk1acPSm-ff0L3N__kdb-8ZtErYF8P_NRHSwkfTvLqq8dpV-4YlqEfhl8nNKcC1rIwtf2szyzwgeNzRDxxQbiYjCTnY83qGkjv1hGcDhAtmEl2GirC0LvYIKfxChQ8uxwEt1xo05cYOq88D14PnJFTe8BbxMp5KLhKWfrZrVF2nqCoENXecFxErgyHGppx_DNgJNobXnNP0cRx0Avn552IPrh62jAVn9AMsKjynDTtdoGKrT1JSHWRJgdhTThy7WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «آقایان، آیا امکان دارد که با هم ملاقات کنیم؟»
🔹
ما با آن‌ها به شکل بسیار متفاوتی برخورد می‌کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/691992" target="_blank">📅 17:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691987">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff20afa1b.mp4?token=iwz6Hn2A6vZNrH7GC2UOLKOOt8i28qgmLFJg3bKEv6AgjBgej7_Qi8SWpkVe2cPonn5PRcC-d0Uy0viH8Fz0sycUoUf9Y71MeZxLE3_c_atLc0HG9sntpyxrUkif4ob63l5_Ci1dlXlBIQSTsDlnuurWbWhhmSXTl-14-bqZCpDq4MqNtWrhcLlBqZq5MU4R5XqmqZbL7pW2NGFyKjico_4oChDKselPXFUO69_4d6K_Gloz3BIu_cwZBIM_SJU3tt6_uu0Pqijsrr2aaZ9fhTI07A40E7Y-kjPAjQ6gUHWvyPUzpfKaDd5-Kp3HC5X2FgtVI_usJTt8UOgztJ84GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff20afa1b.mp4?token=iwz6Hn2A6vZNrH7GC2UOLKOOt8i28qgmLFJg3bKEv6AgjBgej7_Qi8SWpkVe2cPonn5PRcC-d0Uy0viH8Fz0sycUoUf9Y71MeZxLE3_c_atLc0HG9sntpyxrUkif4ob63l5_Ci1dlXlBIQSTsDlnuurWbWhhmSXTl-14-bqZCpDq4MqNtWrhcLlBqZq5MU4R5XqmqZbL7pW2NGFyKjico_4oChDKselPXFUO69_4d6K_Gloz3BIu_cwZBIM_SJU3tt6_uu0Pqijsrr2aaZ9fhTI07A40E7Y-kjPAjQ6gUHWvyPUzpfKaDd5-Kp3HC5X2FgtVI_usJTt8UOgztJ84GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروی BRABUS BODO با قدرت ۱۰۰۰ اسب بخار و شتاب صفر تا صد ۳ ثانیه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/691987" target="_blank">📅 17:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691986">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7015ede6aa.mp4?token=icWciV8_1ma3r7GRsLxnSlh7jB5KOEcmJAq518akwbiDNzwNOsuDbY23dsvmG13n5wFBDZExkOpTVfzrx0TqOk59sLxBo2T6tUO1Kc7RajwjM8f0rVPvKsYcu5t6Ahb38EW6qg0NOy6MoXWiUsZk2fWcmwQ_DFm6gU9m9L4dbU1S1sZgMZK9kLbghYfQqrUSVYbudrDLUcE6-u281Z0eg4wwqZVHRwYCkjTlk5qyZdeiIbEWjGS0agLB_8Uh34eclqh-xGxNbTFq4C63iOdcBQCQ9d8pn2e-4tQKr91hTMU3XsCZhvGxa2Z238iInPAYzM09tFcYNV6-ostugSNugiHXi9H1cIHMdNS698LoCS5Wux3b5SB2bm8iszAMg29f8rJ3McTsxM0TBcCetd8stQ4xIDqRHeeExcgYDj6QP-14JmYR_Kt7Z6iT7UHsXdJX6XO_dNCajXvH_nsSu1BzCqxkZNIr_Ez652WBhD3uHh8L7bTQBNJOmH74NkvQM6OfNOI2RMi7YaN6jQdoMxr3xgsfM9BOJazJpIUOXPW47suFhx2eV6L5zNYp1t1ZpwUIAN7te7HteJiV9VuZlLIhzAP9EzDOLgbhffvqFpI8Vh9vSQrWv_qwY-nQVRNwXzWKXrcRVmbhNJVVyu4JAvNalni6wDYo59fCuEcVGPZTHpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7015ede6aa.mp4?token=icWciV8_1ma3r7GRsLxnSlh7jB5KOEcmJAq518akwbiDNzwNOsuDbY23dsvmG13n5wFBDZExkOpTVfzrx0TqOk59sLxBo2T6tUO1Kc7RajwjM8f0rVPvKsYcu5t6Ahb38EW6qg0NOy6MoXWiUsZk2fWcmwQ_DFm6gU9m9L4dbU1S1sZgMZK9kLbghYfQqrUSVYbudrDLUcE6-u281Z0eg4wwqZVHRwYCkjTlk5qyZdeiIbEWjGS0agLB_8Uh34eclqh-xGxNbTFq4C63iOdcBQCQ9d8pn2e-4tQKr91hTMU3XsCZhvGxa2Z238iInPAYzM09tFcYNV6-ostugSNugiHXi9H1cIHMdNS698LoCS5Wux3b5SB2bm8iszAMg29f8rJ3McTsxM0TBcCetd8stQ4xIDqRHeeExcgYDj6QP-14JmYR_Kt7Z6iT7UHsXdJX6XO_dNCajXvH_nsSu1BzCqxkZNIr_Ez652WBhD3uHh8L7bTQBNJOmH74NkvQM6OfNOI2RMi7YaN6jQdoMxr3xgsfM9BOJazJpIUOXPW47suFhx2eV6L5zNYp1t1ZpwUIAN7te7HteJiV9VuZlLIhzAP9EzDOLgbhffvqFpI8Vh9vSQrWv_qwY-nQVRNwXzWKXrcRVmbhNJVVyu4JAvNalni6wDYo59fCuEcVGPZTHpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوره CEO performance  ماهان؛ آغاز یک مسیر متفاوت برای مدیران عامل
۲۶ شهریور ۱۴۰۵، رویداد معرفی پنجمین دوره CEO Performance ماهان با حضور  مدیران ارشد از برندهای شناخته‌شده برگزار شد.
📍
ﺑﯿﺶ از آﻣﻮزش؛ ﺗﺠﺮﺑﻪ و اﺑﺰار اﺟﺮاﯾﯽ واﻗﻌﯽ
@Mahan_MBS
• ﺟﻠﺴﺎت Insight ﮐﺴﺐ و ﮐﺎر ﺑﺮای اﻧﺘﻘﺎل داﻧﺶ و ﺑﯿﻨﺶ ﮐﺎرﺑﺮدی ﺑﻪ ﻣﺪﯾﺮان ﻋﺎﻣﻞ
🎯
• ﺟﻠﺴﺎت ﮐﻮﭼﯿﻨﮓ ﺗﺨﺼﺼﯽ و ﻣﺴﺘﻤﺮ ﺑﺎ اﺳﺎﺗﯿﺪ و ﮐﻮچ ﻫﺎی ﺑﺮﺟﺴﺘﻪ ﮐﺴﺐ و ﮐﺎر
🌱
• ورک ﺑﻮک ﺟﺎﻣﻊ ﻫﺮ ﺟﻠﺴﻪ ﺑﻪ ﻣﻨﻈﻮر ﻋﻤﻠﯽ ﺳﺎزی و ﻣﺴﺘﻨﺪ ﺳﺎزی ، ﺳﯿﺴﺘﻢ ﺳﺎزی درﺷﺮاﯾﻂ واﻗﻌﯽ
🖋️
• ﺟﻠﺴﺎت ﻣﻨﺘﻮرﯾﻨﮓ ﺑﺎ راﻫﺒﺮان اﻟﻬﺎم ﺑﺨﺶ ﺑﻪ ﻣﻨﻈﻮر اﻧﺘﻘﺎل ﺗﺠﺮﺑﻪ زﯾﺴﺖ ﺑﺮﻧﺪﻫﺎی ﺑﺎ ﻋﻤﻠﮑﺮد ﺑﺎﻻ
📝
• ﺷﺒﯿﻪ ﺳﺎزی اﺗﺎق ﻫﯿﺌﺖ ﻣﺪﯾﺮه ﺑﺮای ﺗﻤﺮﯾﻦ ﺗﺼﻤﯿﻢ ﺳﺎزی اﺳﺘﺮاﺗﮋﯾﮏ در ﺷﺮاﯾﻂ واﻗﻌﯽ
دوره CEO performance ماهان؛ مسیری برای توانمندسازی مدیران عامل و ساختن سازمان‌هایی با عملکرد بهتر.
@Mahan_MBS</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/691986" target="_blank">📅 17:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691985">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLQYvibGCkLjc6vb1emvoiQ4qs9lBTtf50n29n7d6QWo8H2hsplJEbawndXnpIUN64ZxHkt_TF4iSwH1OIJ-eoBGzzSFO-JulIKro-NYPqo3SKK7OCttQX9cVlwrhMk0FkYY6wTf6fiImbQ9j8VZRnzaNi14R3dh6BaKifDqwROwQ3JpGEF0_OJ7NYJ9IG1SGts394KxBJ1r8wGdHJ1NeC8jO74ZKiWz3CCkrmcIb9K2AJrDHhcd6CQTDjdDnDhXuxKqmpiB2vthwNc3TtysHHv9nvrORxWyKT57O4FyOFaQwu8ZAUZdv8_UBI_1OBAn5VBx_oB84cy1KT0juB1_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📞
نوکیا 106 مدل 2018  ساده، مقاوم و کاربردی
🔋
باتری ۱۰۰۰ میلی‌آمپری با شارژدهی طولانی
💾
پشتیبانی از کارت حافظه تا ۳۲ گیگ
🎵
پخش MP3 + رادیو FM بدون هندزفری
🔦
چراغ‌قوه LED
📱
دو سیم‌کارت/ مقاوم در برابر پاشش آب
📦
اورجینال + گارانتی + اقلام کامل جعبه
🔴
قیمت 2,590,000 تومان
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/fast/63670/180124/
مشاهده حراج آخر فصل
https://l.memarket.me/lp/615/180124</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/691985" target="_blank">📅 17:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691984">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: ترامپ به مشاوران خود گفته اگر «شرایط مناسب باشد»، مایل است دیداری با مقام‌های ایرانی در حاشیه نشست مجمع عمومی سازمان ملل ترتیب دهد
🔹
هنوز مشخص نیست که آیا ایرانی‌ها نیز برای برگزاری چنین دیداری آمادگی دارند یا خیر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/691984" target="_blank">📅 16:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691983">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8405ae9d51.mp4?token=jfwGn8B7QXOb3CKXd8rCtuyqSyYv_i_cGOtNuI8F54VsPKHUiJ_dmosRoSqrdxHWqLGb7KwevxXhUBvfsfbxwYoQDk7S4i-AE0hm3EWn8IJ12q1Gxd-WXEyGpG-vw6xefjyHrcIPlvLcOybPkKxEk3RqZJfJA3iTqHFmg5u11iSMNbLW57q6TEnpEPI_vhoUBxtqZ7L6LLBelG-pNzm5R3Rq1zdHVl0Upq4yPqqsNr1wMDlRVNRTeeEnNL1uktjBFITri70OxypxW1V7F4dWL_27vqPcIGFBYIbkkEeKrJmrvirfFRiVYQvTYgwRCsU3IFXoxfCeQjYROCQ9IMXF4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8405ae9d51.mp4?token=jfwGn8B7QXOb3CKXd8rCtuyqSyYv_i_cGOtNuI8F54VsPKHUiJ_dmosRoSqrdxHWqLGb7KwevxXhUBvfsfbxwYoQDk7S4i-AE0hm3EWn8IJ12q1Gxd-WXEyGpG-vw6xefjyHrcIPlvLcOybPkKxEk3RqZJfJA3iTqHFmg5u11iSMNbLW57q6TEnpEPI_vhoUBxtqZ7L6LLBelG-pNzm5R3Rq1zdHVl0Upq4yPqqsNr1wMDlRVNRTeeEnNL1uktjBFITri70OxypxW1V7F4dWL_27vqPcIGFBYIbkkEeKrJmrvirfFRiVYQvTYgwRCsU3IFXoxfCeQjYROCQ9IMXF4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یمن تصاویری از شکار مزدوران سعودی را منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/691983" target="_blank">📅 16:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691982">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf4be7f92.mp4?token=HTTLVu8MKRLGDOS19jwY0l7_zhZZtVhP_k6aJV_Zeugut6a-7QGX3nkgUxB1xv_b_2NVzUaJT35SwzOdc3tmgSpziik_YewfM5gJHQ1yaf0Eu0GOCMxzr8MEUvJoTMV83QMj37n1T_SVcz4pijcb9Gmu6XcXtqiDYHUkg4aCiSwvO6joG0EGfywDVGOqHy6cdiyxpCVKrCQ9CJyAfRlU06sORY9xNaZUqyNq9ROVYICFoFv8oZmHrEOKoTBG60JFjpJzRQ-UNiUcNGFAI3FMo8M5WvhBKOGwC0qvTWxpd8QSo2y1vhirdivE1PA6wRrvyo0cwiVQexQhpa-DH2KhZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf4be7f92.mp4?token=HTTLVu8MKRLGDOS19jwY0l7_zhZZtVhP_k6aJV_Zeugut6a-7QGX3nkgUxB1xv_b_2NVzUaJT35SwzOdc3tmgSpziik_YewfM5gJHQ1yaf0Eu0GOCMxzr8MEUvJoTMV83QMj37n1T_SVcz4pijcb9Gmu6XcXtqiDYHUkg4aCiSwvO6joG0EGfywDVGOqHy6cdiyxpCVKrCQ9CJyAfRlU06sORY9xNaZUqyNq9ROVYICFoFv8oZmHrEOKoTBG60JFjpJzRQ-UNiUcNGFAI3FMo8M5WvhBKOGwC0qvTWxpd8QSo2y1vhirdivE1PA6wRrvyo0cwiVQexQhpa-DH2KhZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز شناور ماندن کشتی‌های غول‌پیکر؛ چطور این همه وزن روی آب می‌ماند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/691982" target="_blank">📅 16:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691981">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
منابع عراقی: تاکنون تصمیمی برای ممنوعیت فرود هواپیماهای ایرانی در فرودگاه‌های عراق گرفته نشده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/691981" target="_blank">📅 16:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691980">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
وزیر بهداشت: کرونا نیاز به واکسن ندارد و شرایط تحت کنترل است
🔹
کرونا مثل یک سرماخوردگی در کشور همیشه وجود دارد و راه مراقبت هم این است که مردم توصیه‌های بهداشتی را رعایت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/691980" target="_blank">📅 16:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691979">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2qbkgHArHstl3FT0P49JLjtrywMKiv8EAIZWQmwRxI5i-WBt19LjxRf--dWC3R7sj6nm7woAkGhwPJhhsG4OBO1o4GGmNrrh2QqOSAmN9G6XZ2CtXmsQiB1Ws-Bot64TIkhOYVKhvBIrAywjGx4zgdQ2Oul_8Ba_endS0BOE42jutf1yZtImbsz1wWC1Myga3OhEewH5ybAytWPjUEbXMyHuX4r8MUGj_Zl9-VU_-zaR1l-0tH6lJnc5WswLSLHBlRhZYreymbPyXYIU1pZwONlccBkl2nROwOeYFa-xSXk_Q19iRRdN0tn7rnrmHQEyy-UN6ZA3ttp8EGEmJx0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای اکسیوس: عراقچی خواستار دریافت تیم حفاظت آمریکایی در نیویورک شده است
🔹
بر اساس این ادعا، پس از بررسی تهدیدهای مطرح‌ شده علیه عراقچی، قرار است تیمی از سرویس امنیت دیپلماتیک وزارت خارجه آمریکا مسئول حفاظت از او در مدت حضورش در نیویورک باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/691979" target="_blank">📅 16:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691978">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgPRW8EMdUX4VKuxkhjrYuMpALAjt1rHaTmZsuYmgnMKp1QIh1Yyt_ca6yDY7wrXnNnZeDyOfzDPstk0QXH8nOf6AaLMvguSZBeVfROcUrYSkW0JFivEn7yWIR8sVJV0kcy5Ncjpso-A7solTNvMgCD8e19thaO2_bc3QwLuHJ6Fr6Ak3HevZJXMbNMzDHbLRwP4HjcN3AM1jYyjOEXny6r1Ptd1FXGKa_3boWS5KYGrxMG1aJVsQw7J3HeghCy_MIfX5HHJu6RaBhHsmnlrVNunQQJ5UCqmmft8ZCxuCUIijCiKD_zo8_NbfnDSX_ps_sdJhENEKx7maDktM6W-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دوازده عادتی که ممکن است اضطراب شما را تشدید کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/691978" target="_blank">📅 16:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691977">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104b583a2f.mp4?token=RoOPazSzNs7wPSfG8a_1F0H2fiUERSYJPWG3YiJ6OoPBfpspwlRABPLql8QINNEJo_azQhrKrwTpXAFNEF8yh0Gh1HBnFO6CmNK9AYMm7kr2eWbeYT7ySOUcMY67Ch3EcKX1oHwZrD9ldxdKA8VzvN1A__5HVKr2LdipW18-58seMmR2DbHgViE056E5ZVuT-_d2B-mHFs6DWYcqeNsALO325yqG2wtmRFIiU4DmLF9oYiAeLWOFc1dbz6sTcgYhTj9QOJ_2QSCGrdW_km4YixfhFkacW3BabunqFxvgcnOBHqhF4QacjcE6fnvK7ymyGAD8Pob7tPOK-t5SpPUAHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104b583a2f.mp4?token=RoOPazSzNs7wPSfG8a_1F0H2fiUERSYJPWG3YiJ6OoPBfpspwlRABPLql8QINNEJo_azQhrKrwTpXAFNEF8yh0Gh1HBnFO6CmNK9AYMm7kr2eWbeYT7ySOUcMY67Ch3EcKX1oHwZrD9ldxdKA8VzvN1A__5HVKr2LdipW18-58seMmR2DbHgViE056E5ZVuT-_d2B-mHFs6DWYcqeNsALO325yqG2wtmRFIiU4DmLF9oYiAeLWOFc1dbz6sTcgYhTj9QOJ_2QSCGrdW_km4YixfhFkacW3BabunqFxvgcnOBHqhF4QacjcE6fnvK7ymyGAD8Pob7tPOK-t5SpPUAHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هادی‌زاده، کارشناس مسائل بین‌الملل: ترامپ به‌ دنبال ساخت تصویری ضعیف از ایران است؛ جهان می‌گوید ترامپ شکست خورده اما او می‌خواهد تصویری نشان دهد و بگوید که ایرانِ شکست‌خورده را پای میز مذاکره کشانده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/691977" target="_blank">📅 16:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691976">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ef500ead.mp4?token=GZ1LjqCQ_pN9i1wqMIxplw5ZBh3Pfh0V1Q0W9ULK060iWJLfmKO2PFm5tUhskZyVoh7h_TPi4HqZl9xetZkDEWK1yvckOG5D5MSPQUhaSTw7yNDowWh5sr0vg7d7pF8Kr1xUT6aud7yZM6aPkTLQscv_FDjirT3x9lt8VmUKNGVi6dYw1iWkbB_PKg55GOwWCT-H3PsRwys5TbcLkVPv6d36j-soi1NBHe-wVFLrxrOX_Xk4C3u5qB6ZGh2hNlhXFk5n4X3im0RdMTGPt1aNSVvL0NAXiQICBR5Labgn_cDM4Osr6GWgy8pmculuUOE190Fm_ja0MBKXOJ4lg5rBB2FjCd1Md4F46_iEaaMuTyiihFtFGWeIbBKs46MCRgrMExOqT57BX-qIxfdIuWK7gcpqYMK21DpiMl6UGKHKIg6jQ8lLNXoZaqq1u5Lt7WY4jwNiMVmV9oswj46WB7vdNoc1wGaLOyvSftrTuK8DprSGjIR5M8Qe3bKUoG81oaZhMuOgJLnhznXFxAlgQtInoUHuuixCsNukWSi5difvylydR4nCjK6dZhox5Msd8lA2D2P_9haAHCJ4J2aqbj086z8ASPW1q6T2SJqdpNrj5Fpiak02j32kGg9ETQwfQyCcWGYgDoDrFQ_KEDjP1hdUQlzDqCyJlmzvHmasJT1u-q4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ef500ead.mp4?token=GZ1LjqCQ_pN9i1wqMIxplw5ZBh3Pfh0V1Q0W9ULK060iWJLfmKO2PFm5tUhskZyVoh7h_TPi4HqZl9xetZkDEWK1yvckOG5D5MSPQUhaSTw7yNDowWh5sr0vg7d7pF8Kr1xUT6aud7yZM6aPkTLQscv_FDjirT3x9lt8VmUKNGVi6dYw1iWkbB_PKg55GOwWCT-H3PsRwys5TbcLkVPv6d36j-soi1NBHe-wVFLrxrOX_Xk4C3u5qB6ZGh2hNlhXFk5n4X3im0RdMTGPt1aNSVvL0NAXiQICBR5Labgn_cDM4Osr6GWgy8pmculuUOE190Fm_ja0MBKXOJ4lg5rBB2FjCd1Md4F46_iEaaMuTyiihFtFGWeIbBKs46MCRgrMExOqT57BX-qIxfdIuWK7gcpqYMK21DpiMl6UGKHKIg6jQ8lLNXoZaqq1u5Lt7WY4jwNiMVmV9oswj46WB7vdNoc1wGaLOyvSftrTuK8DprSGjIR5M8Qe3bKUoG81oaZhMuOgJLnhznXFxAlgQtInoUHuuixCsNukWSi5difvylydR4nCjK6dZhox5Msd8lA2D2P_9haAHCJ4J2aqbj086z8ASPW1q6T2SJqdpNrj5Fpiak02j32kGg9ETQwfQyCcWGYgDoDrFQ_KEDjP1hdUQlzDqCyJlmzvHmasJT1u-q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انواع صندوق‌های بورسی چیه؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/691976" target="_blank">📅 16:10 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
