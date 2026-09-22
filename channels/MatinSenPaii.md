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
<img src="https://cdn1.telesco.pe/file/c1oOebAvLuD8-5kEHUwOmRq5vOZRkGsJuPnkmUiEo4NK_9ZocEzCzrU87JY_yCwZzfDWZcgbGxDJ68spyJvzVvqIcToeQxrTk7qORMf5wsIGh4HRkdyvSVFWu9NRekXOJUiHpiIHp9ABS_7kEynyu_po1BuE29EyeDFMsKpKd8w9-i8IdhQFZttCum5WThuGostFMyyHTJ0y3KEE68Lr2082166Co3vyg9_H_RfhvCdVvV8gkLryV4W1gzPeoLEd8iVvm90DcelqchQk98MOW1nzS8NDHTjYn8KtiIkfVA8ZrkSJbeXH5XFViePfxul7cO-hp_NcHZ546DgGeg2twA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kHPn_kIYEdmiPGH8g-teAM5Eo8-L_mcaS51pgufzBSy2USjulHeC8MVLFhFM--IHbKy0GZAk8BCndD_deKmUz2rgsJ1lfUqrfZtyGUDHYrFZatIfX3oiGbp9igi_ANtU6RG8qVShqALrWlEefUh63vlysSTNMN1YxxDGITtoqhuup0pBJ1rzpMLtfbh1GKCcW6cCFNXCuyl1BBMl4V9VSflOyNHo6Q2RV5c2MbqKO8cG-QN9AqBVYFtcN7Hs5IEwaK2RI5qHwfO1o8YY5auydwmx7M23l7hWE4U5tNXB2ERiEVH9-yYfIDk3_rK4kJoGzKWqd1BiS1IkuMiv9DEBww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی 9Router ارور
HTTP 403: [403]: {"type":"error","error":{"type":"FreeTierError","message":"Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"}}
می‌گیرید از اوپن کد، علتش آپدیت نبودن 9Routerتون هست.
برای آپدیت کسایی که با npm نصب کردن، از دستور
npm i -g 9router@latest --prefer-online
استفاده کنن، و کسایی هم که با داکر نصب کردن از
docker pull decolua/9router:latest
docker rm -f 9router
docker run -d \\
--name 9router \\
-p 20128:20128 \\
-v "$HOME/.9router:/app/data" \\
-e DATA_DIR=/app/data \\
-e JWT_SECRET="change-this-to-a-long-random-secret" \\
-e INITIAL_PASSWORD="your-strong-dashboard-password" \\
decolua/9router:latest
استفاده کنن(با پسوورد و JWT دلخواه برای JWT_SECRET و INITIAL_PASSWORD)</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CE2jC44uoo97gK9KNal8KxE6Vg091RdJxUQiv7S2YMo2e9F97Fzj0y0R3DLPO_9cbWV-kKLK3hmRlSufft5YJHSm0FyiFE6rVcGqmXIuZLhbpOrqlgrqsIWq5VRMbsWALzLgHfYPaXDZjaaBHub-V-qOTlaEMow9Vk_YRAmriEKHL2znaydX_iRjrSZRCPzgLhqfp3lXtqp8c16oiUGZHpGLblzYYsop1PBO824tOQULGGkjPoQfhAmqWUBVwd3usSdwDIphLl--sUNb_qMCDJ1VIZgtnOk87q2BGhUHAt1oCIW0LPmTOf3zcpv-F6LPwZP0rs0T5bRz0Qk3x0NL_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fWlwkKKsGn2665gKRV9IhSRPZ8Qe1dnA1C068UJgGc7nkJDP_4XcT5p491jeRTyQDkkP3-Td00XCsVHXK5HuoxfTF8PnZDpCBWLK3LXyXrol0Zq1iC5EoMty94S2k9iQi3-pALBEU_NK9rX33PsruzwoLx7r24JziNUXS6M6F_85det8dFg1Ga-vlMMpCcs_ClA6jqLGZrBUTbbXs9_eO4cEFUrln_wPVMkjfVqACbx19iPtZUxJEeKLVbKgoj8Y5yyAgP6B8Pu52gFcdHr3F7OYRAQIC0Ofua6TGBCIhmAntmQO-I9063p20-j8j3aBVLypiDYPCZroIAuGvhrCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev
توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev
از برادر کوچیکم دعوت کردم بیاد کمی راجب خود ماینکرفت توضیح بده و کاری که ادعا شده ai تونسته انجام بده.
همینطور در مورد Jev صحبت می‌کنیم و اینکه اصلا چه نیازی به این معماری حس میشه در کنار LLM ها؟
و می‌ذاریم ai ای که کدشو نوشتیم، ماینکرفت بازی کنه برای خودش ببینم چه اتفاقی میفته
😂
لینک سایت Typesafeai برای گرفتن 5 دلار اعتبار رایگان:
https://console.typesafe.ai
لینک سایت هوشیار24 برای تخفیف 90 درصدی API از GPT 6 Astra:
https://houshyar24.ir/?ref=B2N4W9SS
پروژه رو هم توی ویدئوهای بعدی که تکمیل‌تر کردیم می‌ذارم گیتهاب واستون
🥰
📹
تماشا در یوتوب:
https://youtu.be/l-o_fQM_9AI</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مدل
Grok 4.7؛ آپدیتی که بیشتر ناامیدکننده بود تا پیشرفت
ببینید Grok 4.5 نسبت به قیمتش واقعاً مدل فوق‌العاده‌ای بود؛ سریع بود، کارکردن باهاش حس خوبی داشت، قابل‌اعتماد بود و به‌عنوان مدل پیش‌فرض عملکرد خوبی ارائه می‌داد.
مدل Grok 4.6 از نظر من یه قدم اشتباه، البته قابل‌درک، برداشت. کندتر و گرون‌تر شد و برای انجام هر تسک، توکن خیلی بیشتری مصرف می‌کرد؛ درحالی‌که فقط یه برتری جزئی از نظر هوش داشت.
البته دلیلش رو می‌شه فهمید؛ بالاخره تیم سازنده باید خودش رو توی بنچمارک‌ها بالا بکشه.
اما بخشیدن Grok 4.7 خیلی سخت‌تره.
1-
مصرف توکن برخلاف وعده‌ها بیشتر شده:
گفته بودن مدل جدید توکن‌بهینه‌تره، اما توی استفاده‌ی واقعی بین ۳۰ تا ۸۰ درصد بدتر عمل می‌کنه.
2-
بنچمارک‌های ضعیف‌تر:
توی چندین بنچمارک، امتیازش از Grok 4.6 پایین‌تره.
3-
سرعت و تجربه‌ی کاربری بدتر:
کندتر شده و کارکردن باهاش دیگه مثل نسخه‌های قبلی لذت‌بخش نیست.
4-
هزینه‌ی واقعی خیلی بیشتره:
هزینه‌ی استفاده‌ی واقعی از Grok 4.7 بیشتر از دو برابر Grok 4.6 درمیاد و حتی از هزینه‌ی Astra هم بالاتر می‌ره.
با توجه به این‌همه تبلیغاتی که برای این مدل شده بود، باید بگم واقعاً ناامیدکننده منتشر شد.
البته بنچمارک‌ها همه‌چیز رو نشون نمی‌دن و Grok 4.7 توی بعضی کارهای مهندسی واقعی همچنان تجربه‌ی خوبی ارائه می‌ده؛ ولی درمجموع حس می‌کنم هنوز خیلی به مدل‌های سال ۲۰۲۵ شبیهه.
مشکل اصلی، قابلیت‌های Frontendـه:
عملکردش توی کارهای Frontend به‌شکل غیرقابل‌قبولی بده. قابلیت‌های 3D تقریباً وجود ندارن و مدل دائماً توی حلقه‌های تصادفی شبیه Gemini گیر می‌کنه.
حرف آخر:
این انتشار واقعاً ناامیدکننده بود. امیدوارم تیم SpaceXAI این موضوع رو بپذیره و توی نسخه‌ی بعدی بتونه دوباره ما رو غافل‌گیر کنه.
✍️
theo</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k4e44i9h65hH5MLgwyTvI1JFG6RVZdjLDFD3_VZ9OPFNyy2vCV2WNf211fBJpjYAdGFqJ2Pwb056vQeVRfGDt3HC2lTG10bYdNRoTlRQOEnPfdBZB6stzG1ctH6_JbsoQC1k9d7jhrt_-c8XX4iW_35bXCLeS5B-GEplt5PL3D0eetmVNVapsjitpsp37EntQOjMepdPntgSFNskXQCIX5rOSh6Z8VLTUxiyhYEOusy7FsihvzgJRORIm7asiOG23zHnIX4S-mUszb4H27NdQ0ud9vrRf7qMMZ8rgI8rSmnLaoOWQPnsww8Ujqrhpp6P-aDe6Qa_tGyj0A3pEgigSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qjJ87iNYnObTAtAtiSpc1JN9vOIDiGKpKlLUZgdNZ8myb3z_6C3_TAA-1twaXXeuBQzQPoyILnFlp4rIdfKCSaxVMO-ysIu8X7gZxWVt51PSHEXUKr7FMha0aQZ_IA2M2BLRpgdb91i1L7mHZo3X8K10gcTEAv_Qhw99sgJ4ZhZixJzcuU7469Zhitfu0vtIrVYWqlMu--fTUxh278eCwARy7fkr-4-_Ab4AL-2c0Hx7IcAGf1JbQXM-7K4yXVNQDeSa2fO_-zPuxFupNygmiw-XeV9crFZdJ4driCvnYcugrXLUhaGuiMQY96-dgCDP-MrAdyEgIpbbwbovXrZTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g1w16IR3l7g3OS8YaytShZB14lW_urvRacbFM_Mr0Am-i-q8Q_Hj9bnMix_KcsZY8Hawdar_-_SVNOot2WzEPg5UGkJLpk8OteBS4FVUhF9RiNedXqwM1z8hp1X3XXh1XfgO0DEe00xTjPz7zIkg_rMqDj-2exeUgkYDau94bWLPmBUKLyixaRI0zfsWumSf2QSGHJJk0p67lw3QBheYiRxl-cmpnTiUK7Dex3qCrUxrH-ix7dTQ4wTxz0xiBojjsaEOFSosLpmRY8v9zKxJn0mZ6CTFm29GwnGzOIbOY7u7h9I_RsAQqoZMibo_18aSx2pwv9NnB0Y-JsoTZM2B0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rM6php1THA6DQfowHcruDr0Yza-4_w4FGUNqOzwkTL1r8YH-2EBfvDfro5lNj_yJ19_R0B_6fh9KQeqaVbrcSuvpKqKDxOnzBz2NAS0szN8-tAgNubh12gdInMAZf9YMI1aU2Rb2xhiocx9A9AKcMBO00F7xE7IXimD7KLQ0fwN4RwXcB2XhvWivdW7c9ao7nDCi4aBED8Sn93c7voE0uc4cnpf6_M6QfDo8wkgWD8ZAXMzfBNf9N1-vexCSGMcrA8--gQobnpbXt6LPf3oZW1OJTqYR5qXKJpU7dw5vQ1fJz3cqp4ppLs19g1JjIFQrEt8lZDZFLcuP9A7Bil4gHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eahwoSVvIGLdVIZZVjObdjj0mDSma_FY6CugLoC-fMYh4aVXCJKmNXAI47up-kbAutDN-wfHhRYJUq95A2hTrz7RY0YlGcskmMNr6rrUhf4UR8_n_Tr4vXtGzg5NiyV5yx5VTcQADSDGoGTiXqUyPzUEHrDOtoZ0jQ2YNFzeYTeLOqhjJoqSt7KVw4b3Ls7Tr279dxUpyg4oKnrD34C8eu_RpHeGihFMkKSbLdEYZWwH_qNvfm8PUsDeNfAEUVWAEudKwAuCzsafsL874YT6xcTvccCxpNTPUrYXtMJ2L4tQxQGR6CvipDd87wjZLuh7ehQfYz4eyllR9crz3oAHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/juqDMstqUqT576pZ4OhvOA6MkGVckmlkvDfvJsTgr728u1CPv5SXwNdcS3_nBPKiwSoVBfAdXknPsG4efiwvAl8Oxa9NmmPhNJT6WiHpOuZonQH_8qtwx8qFtD7fs0gDF7yOQ4Az0FQwgQGR0D375YO7sGVWSw2Izm4ZeENAzHgoAVhpb2HCWxm-jFPCr4cSzCsP_iZPTNANaDrMgMSUNZobL9KArgxGbiPduGECf9ubsq-mEFLmf7sLwKrt4dibD-BDUdxSUIVHaZX9uRwaflMfG_CkFO1Yu_C1QMOCDn1WIk-jVLNTIdVOviiRN4AV4nj_odOhH6ZHI4kRFBhHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vVWGdfXltnsMZtglOR-ERSep6ZTKFp2dDSeuZmZ1TsMcgHQuIEgR9fVTTtEtngzdvUv-7D77YQH2rpt3nmNQsNNm5TynCdHA8v-vCxwAzwX5qfca9Q36BUhtta91SuBOMXV9JlLme180lrYixR_alzUbpo2hrml_z-LaDu1j5lOcfNLlTyIe9Y9Q33qFSnn_E5qCDQBTx6qOMNzpmhXaiSKR7GeMht18O5d34pdJ0YC_ABiiMEvEk59orfMG2oK2rMgv2wOXO1pyNgaa8CN4T-AAlSnQSM7ghx5mVB1u-YuYZta4CqImoVlL8NwMMdJcleMqR4Q5mnN7eKKubhb2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LGgiQ5-YF0zGSmUYASnnjqenkuyoCaW8oiPNO6ZgVVqWqgIK0tTfuM3-mN7ph_8V8VstSpLtS48UwFdKerXi-UDDqPzkbNwOjudC-Qpa4X1RAAGEAbSM5Al79GpEGClYtDePWNAN7uli2D3rfKSqU0IZMeMEGKR7L_OxiHj1nSdLUmSHm3iHUyCF9i9KzQ0iFr4RtsdRTSdMSiN7r7KskxSytKri9rG_QrvrITuLGVjlxA3bF6qojPkGpqSsOAWSSfOXo6VKG2lEjGjLzL4gAgE8XOfqkhoEHZB7x9QOnlqJjNdTCCMWjAeDQETPTaZQOZCliIv-DhhHPTKuWgrEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SRVw-bDjGAx-6C8oeRYhSjByBTt51C13I6uSBTNGBjsmaAXAE26X0rAdcDcqDkrOvUWkWGMHNL707MyJQdnjb5dx5Ogj06471gWvT3F09IRv8f1r4X-A1y2VRiET7Y-FrJnXMNxwJ6UqSOH1M0yY4k7hGWlxEJrgofdZUL5v3AdqjUUVO-W5EfkTCECYcMgKnoHmG-R7ln_EqN00r_4My1b4yq-9usf9xweuUgVIXXBjbovg7Dkbf6COUT6VuT3m0yPg9-imTU1JVrDRvF0xfCcdqQi3j3919KCpvOSjj596kiZPJM0KGQWgqmsyf62-DM6lEgYl33q7zBrscvxKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xw7c1eu59Fkz9vaIMxJli8_soPmA1SNK7HhdVlgvpqaREDoyJ5_v60YW3S6ELBgY8Qq86fwBfWP-AkmzIi2JyjQ5pOASROgvKjx2pN9AeWjKhyVRpmu7B0hcql556Z-8VUrXDvUBWqHdCeZ_RsV4PldxtE_DmKR8jmZctLmrLH0kq-0HBP_fEvqUlBSIq62IRLxRCipdOE43Ml0BxbeGKEM_NvnHwGza-0edcOVdfSEyh0ZFU7Zze___I0lrEJSF91gdeR7JT2Kv-SQ-JPYRHcZMaT9pAzHo64ZCZR09aIpLotPiOCex1TMytv2JddfUbVdP7_5In1ysZZbPeWNwAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه
هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن
به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم
، سعی کردیم با
یزدان عزیز
با استدلال و تجربه‌ی خودمون به این سؤال جواب بدیم. چیزهایی که بررسی می‌کنیم:
— چرا بیشتر بحث‌های این حوزه توی شبکه‌های اجتماعی «حکم» بدون دلیله
— فرق AI با یه ابزار ساده مثل ماشین‌حساب چیه
— تفاوت نوآوری (Novelty) و خلاقیت (Creativity) و اینکه AI کدومش رو داره
— جایگزینی شغلی و تحلیل آینده
— چیزهایی که هنوز دست آدمه و AI نمی‌تونه جاش رو بگیره
— بحث کاهش نیمه‌عمر مهارت‌های تخصصی
— ۵ تا کار عملی که باعث می‌شه بازار کار هنوز بهتون نیاز داشته باشه
📹
تماشا در یوتوب:
https://youtu.be/x8V0w3I9g10</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys7fvENh-WKTbqzFOnpbln0uK6WDRBKPBL7VaPiEFOzV2D9Gp3rj8SGj1-E7jsZMGQfcdsR3qLSgpdf02uV6XMHYh_SyifyLp9y3NQrWsGRdqrKOkLVNLv6qat6gelkPWutJANG9_36WGBrovz056FDsdYfBPZ2lLWeBlk_djVPA5gCPjLjId6PaHZr4d9lVuHOdtNwBtnL6vQk2cv_KjqmtskNCi8ga978Ru-6KoeH8olvhFda0wYjymC1NSwlib-RWM9hVerRYfpAmB5B5DW4Q8o4Qs47qWmU2L54WWt1tLsuCnj5BYlZXYy6MvvzV55XtGaQ-5UkwOjU5lmMGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=M9Zo6_T1BKqVB8oSiJdXuJ-7mFQWDOnSRNI8NfvoNFY2oTQ9lhcyj-7MTzXmfxmfmAN14p6GZ00GWLe3JZWtXESKitJzwuq-QKH-W32UU_-q5hZu_F_Av1pziwcIlGjMQ-YBI5O3tOiliUMoGjrx0P1fRhSaluI4JbSqD653kJs7ohBfwxwAZGX1YuMz_pX55OQBWpAwEPJCMJ1BD0UIl0lfkY4OdvLyQQhC6rX8VMF3IHcw0OPg7CXa2aJmmZW9VS8ouTk-XP5cz4GpzBNsK3VvSchVXkjQCSSWlLnOq0M8TbKK8MxLgsHt-GACWiiFTsltwLh32O4jnhIHYcT13Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=M9Zo6_T1BKqVB8oSiJdXuJ-7mFQWDOnSRNI8NfvoNFY2oTQ9lhcyj-7MTzXmfxmfmAN14p6GZ00GWLe3JZWtXESKitJzwuq-QKH-W32UU_-q5hZu_F_Av1pziwcIlGjMQ-YBI5O3tOiliUMoGjrx0P1fRhSaluI4JbSqD653kJs7ohBfwxwAZGX1YuMz_pX55OQBWpAwEPJCMJ1BD0UIl0lfkY4OdvLyQQhC6rX8VMF3IHcw0OPg7CXa2aJmmZW9VS8ouTk-XP5cz4GpzBNsK3VvSchVXkjQCSSWlLnOq0M8TbKK8MxLgsHt-GACWiiFTsltwLh32O4jnhIHYcT13Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=WEaBMBeiHCM8eNLtS0ZM-bK09iZW7sK724zu3hh5b-Y5EfNzliPIZ5q1tDk29hXoZ4yyNaUdKIpa1yQILcVhxuO-ieDemwtGmvqEv2H5uF_NvE5tv_YZfD7Hj1Cv6Hd1yvN4YwFc7ofFMVTsOfDoZzYwnE7GUCpMfqoHl1EY8mEmNapXBb74qmjcvKtItLbPwDudMdS6qFlUnoTvOa_9sNGLbItW9anHGShUyXAFgs0Vmpyv5-CUkU2Q9bNlLWq1Pih746xitMqs7OFTU8RmnFx8D_oLdUBFnnnsrleoCs44yY8sw2QR-odjvUAynFemp1ZnNYfw8L_E5jeVn88lIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=WEaBMBeiHCM8eNLtS0ZM-bK09iZW7sK724zu3hh5b-Y5EfNzliPIZ5q1tDk29hXoZ4yyNaUdKIpa1yQILcVhxuO-ieDemwtGmvqEv2H5uF_NvE5tv_YZfD7Hj1Cv6Hd1yvN4YwFc7ofFMVTsOfDoZzYwnE7GUCpMfqoHl1EY8mEmNapXBb74qmjcvKtItLbPwDudMdS6qFlUnoTvOa_9sNGLbItW9anHGShUyXAFgs0Vmpyv5-CUkU2Q9bNlLWq1Pih746xitMqs7OFTU8RmnFx8D_oLdUBFnnnsrleoCs44yY8sw2QR-odjvUAynFemp1ZnNYfw8L_E5jeVn88lIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HdOSVwB4gZGACPnzmXZkL0hAZb6Iv7JFIZGidmHZ9Gy3t44IApgjdSiMXaZpbgAOvJx3bwe8QFb21UUCgvcY-R1C5TgbRMqcnf8xVyQESaPVsHdvpfvEhwdZYYrnkvyK6wk32JAzPqBWhGDKdZU_4cCbQnvWYAeXfBR5jRa6tU6vpxZ5Q0Iq1BuMDf-gEF9tVJqcLKRAMALaezptLghJvUQOp0y6UafeT6dD59IDXKUNfxTZZpyhA4-oU9Uu_2jXlvRLwpUmamnvHDL45z_kP0qXbtGR464uwBAJ1nKNIbDwwuI9QIMROL2vt79FcVoUWUcchhlEczxQz7L2SLdXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hOm23LsLOqghiVjJLDJdsfhhDGhl5jmxIVfeL3gZmjYVFueIX8SCiB8sSTl8cy-003FANAX4vCZMxRCbgUnPKe9akbyUja6mzZjlo3WSVgtosjqqGPhiRsWkFA4aHT3PcBPBFKGEp2PQ469DphXry7Z14Qo-VPKNYqPDkdD18MTE6J3IT_lWYQz9nCLbYvOOqloaGSrIxgpXmqKwBe075ncJ7ECB0Q8ugz4bD6YBgT5_TQ0A-G4RRE-YDYj3uNFv_UDMglbx5jSdUbPLIW0N2zrN21i-TOmSZwpOzpa-EzUHWL440WxH_7P-9ERqSPn0GaazuA37v6WPn9KPTUjtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=ZQxMH4Znz7uzZHNJExw6l5rbHDQ9VqOeE1zCl7mwYU3-p3Z8uTGpRPE7IxFffeOpH7_awRBJ0IpPPGlT2R602jkguJU4Tn6by2lB-KKV8rJmGATLxHzw5gfGJt-bCj_2QFy7COUZyuHt5kI0gL0OE79TMFOnPe2ieNX3HKHWOZSxts2GVBQcVxre4o00WUM18bhzv-fnuUzLkWNzK_CCfEt7v0qo6PlLaNecIwoUhfX1WDvpBsjEmax81R8zYaTYz_2LmIWf6vtYR81Sy3iMzVUkJnGUYS89h9dEBgUXi-O11YT7Ci9e4SKXChdyps8Gw73zIAubhdicD2g_HS4nag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=ZQxMH4Znz7uzZHNJExw6l5rbHDQ9VqOeE1zCl7mwYU3-p3Z8uTGpRPE7IxFffeOpH7_awRBJ0IpPPGlT2R602jkguJU4Tn6by2lB-KKV8rJmGATLxHzw5gfGJt-bCj_2QFy7COUZyuHt5kI0gL0OE79TMFOnPe2ieNX3HKHWOZSxts2GVBQcVxre4o00WUM18bhzv-fnuUzLkWNzK_CCfEt7v0qo6PlLaNecIwoUhfX1WDvpBsjEmax81R8zYaTYz_2LmIWf6vtYR81Sy3iMzVUkJnGUYS89h9dEBgUXi-O11YT7Ci9e4SKXChdyps8Gw73zIAubhdicD2g_HS4nag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektCxIQz73AY-wMYrpzQECpOl1G92Bti43ICOiNhz54Z6ApJYE0GKYJlY42wufOYv6fw9J7vOii0qiBOhW9nAKtQQcZhXrZHRWNtpHXO8WwP1Hanb5VOZkotuGOv1TEJyXlzO5PF0FTi9abZNFLjCViU4ubARsBQDB4FC-SpK75BtG2IxfpIRFNG2zS7dIKfdbJG4Hh1xTgd-cOyzAirE913u2LlcR4qTSvUdOVr-1LAlu20qTbjk1YInCVg8oEV3VNsRYkCYpwaBxyCEz4QXpH7CNev0k7UnfrhDUMVtZ6jFLzYYwtP4hyy07BKofDNjBWQ2xmVsrQF9-kA0jLm0ly2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektCxIQz73AY-wMYrpzQECpOl1G92Bti43ICOiNhz54Z6ApJYE0GKYJlY42wufOYv6fw9J7vOii0qiBOhW9nAKtQQcZhXrZHRWNtpHXO8WwP1Hanb5VOZkotuGOv1TEJyXlzO5PF0FTi9abZNFLjCViU4ubARsBQDB4FC-SpK75BtG2IxfpIRFNG2zS7dIKfdbJG4Hh1xTgd-cOyzAirE913u2LlcR4qTSvUdOVr-1LAlu20qTbjk1YInCVg8oEV3VNsRYkCYpwaBxyCEz4QXpH7CNev0k7UnfrhDUMVtZ6jFLzYYwtP4hyy07BKofDNjBWQ2xmVsrQF9-kA0jLm0ly2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eSu9yWDjslKMacVos1n7Pm6aNzIblqEYT-xvRt04qMwp47Y8XcIXjQetC14mLiLq7u70kBvFv4BYCB6G8jikPVMEWMbKwBOTxFuRT2o4Ei7mRXGoXh4QpYYGPPfKcnQpYkkWM3kv7mI7dBQwSTiEk0fmIZ9MKUUm-fR13TEIz8Znl4pmhuHIJ2gUyA6bBc5wB6vFP5GZsjFiIHg5Rwel6fheMznZNDWQw0IPCRV7j-izNsF3QHa7ufqJf5J4wzc6lo0VOkl-ZpNff6nJxUPelZDCr5XLvO3mGdqloaAS7OprX1io9Ds6YuanP5YtszUzbn0uwqM3C2sIZHF90sF8Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wf_0zbbgCkJG9uGCyPEMDBf8Uxh6GtAN3nnxoKqIwlRoktgavCCUAjNXlSwBby-XpokPc3X1Yt-RYnlWL4v32RDts2NLmA0GJf-YKjmE5_RabkVRs77HT3ynRfXY3Hpw42N9ClQfpLf9C-zGWfBsz7jVvQsjvFQAjYVNoPYDCZcs0fG7Rt4Wpq86fiYVuipQOaMPNWd4PS8KJnyxUk7V91dOnrzTb3ydYo8drTEB4hBXUP1QBx8ooyVDNbke1Q-6q4xdZeF8n95di-LAYZH9Hb0yJvdYOSr3oTnYleWDQv1_06jUv3qFD2PUyD1DmO_jNOnb7LWGKRmBTbAJcavi-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rqXNzlHBzlcN78VvynhWtvUjwKGfJTVLA5784K-VfV0SNCyESYDXl8CfCJQT3RDdiD8VzO1tyu61ldREJqXdoNvwPDdCp35k0ttYo-73USqo_myGu0vQH-LoVV3WzTZ7Eujc-zruBQhGGRWwO_TXKOzrgCeqbODSYtKQKM6JxJ-4RRkpcq0Logxb4xTMIVg3Bop6Rnzfcps52rFxxD8BUFJG2V4CoIt15gBv6L0NW8n94paInYG4eDouRvw483ld8G3ghwvMTWkPA7Z9iQtuXost-8RpwJAyR9IfWh45bNTuQODxhZ7xL-U8P8s_j3VkpYwW7yxqw3WgSMjJwdJByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXTkrxzsz1v9_13bsXsZcMgJ3wQt_ZWFuVUXJlbCE6AqUt9EFLHLpR79HdpGaQnQHW0KYDJP13Y7UnPqaag4WPf8b_dq-9blcw5Snfqr-w1mPVxUqdhZdd0mu0GjLG89hQtApH0nUjNl-tSVZPhD68oV38MGWUCeELS1GNGQPA_hZS1Zrx7WlHddlkAjV4gIi6YPsNz6cticffw19rv4gfwnoAW1mzUw-SzAyQ89rFASY391MbpwdRmOqwMnurxY5yZExnxS30Sgmt6EafYXLC0KzBPgRWHheN0Escrr6KiKiJ425jg4jdKVhZIRI-44wBPJvrRJfVOIDK2GMEJ-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VK3TXnEdEirPRpMhdMAV_V4XhmvL2yBB_qs2uUUZ5pbxbJ1cw5nKImyaC3CnU0Azyu2nvA6By6n_1FyBPRJCFPp3wST8AG3-Wa-oaCyrDrN4PkckZhR-sUScfG-g81TAQQOu7KudzcruQlozMXmB0iCVCzZpH94jenPvzoHnI67-1iZEOU8nz1L41yp48H6IVryFjUNegrp2IKpZ_-5H4rXY6KRt3UCVnzkrJiM9b1us5JUJFJNbiJfPDOHMnwKOnX_toHfYTjfU7oJATM_HY6OWNdGzEcis-bOMQFJAthZnFTZCQiyRYxiszeH_fddOM1QAUhtaewd_1uiEhCC7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d8qQfE9PKSpYTk-f2EYHpXpKXO6QqqUQhSgiK6ZyUFMT1rO2ENOqunVr1anqRkOJUlQqjprwSLqtmEW7FJlmgJ54vUZR_cB_9oIx7mDe7V3VC86Y6Vd6X71RKtrtqherJKNMgrbVgcp-J1EQkuQ1XN3IaWV7dfbqaoymhB96bo3KneAGARptCJ6jiWHaU-QXrgKPkpLzqlXnUfGC93mzkVL_Calh66LT5VZpLQp7xXDG3gFoTLqgVDHv1BIfT0j7ryRrRK14amIofRCVdCBFByER3Wr5i-5NXXGrWUHdrPuJR78pDqs2cwgq_WHcifBQr9EvFSnxoGhJ5hwLZ6WTgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n0IcQf5uKHzHJ5AuHaxJvAdV8izsBRfd3dOFaQ_Us9cKABcPa7t51RoD-gETZz4I5EoBbaYq2iOlEzDPfI-T8ugp8qmZiRukfjr_M9bnUt27m9CyCuy38L3Y9XxL10gw4jpQmrhUIcgOBGXb0XRSaMDvi0JlI5sw0KS2CQPVYgTU8t-RX9-j2kVNRJkhGZ5i5bXDt-WSqFz5qaPiEAqkGXwkYWv49ZPpcvHiSIvn2VEk2aaogKucfb47pEOhny8h8Ag8bE3zLJ2mxOKZemXcAQ2rcrv-AinqMVB4iie_tS9G1cq9E24ZXaMBR0sHRs_pOQ-UP7-RRnNrSNd3Smc1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TFfz8_IzwDJXfsU05JhtFDHoe35xbbb-ghfKgsEg77RXwiqZcAqiRxDf7tv8ou4pqFGBjaHtWFV6GN3WLJG9XcIAbshQHmJeEVoGAn_TVc3VrASoHhjbsTw3FpVzIiKoHfyvXkZYAjhS6pQpHQmTF-LDaHzdyKejN7xgm47g-6n70H_DK2P9tOT02_TeO6GytqOWHE1oPwEy3IPxXjq1rGUgEYwpeLDhS1GYvf9l0IjE6Z7gNJu9kClV3bWaYNYQWrgVB2lvM05KeGbJjm68yZd_qOkbcWbHIg_3DYpM6GS3LdtzYA_GGxHl4-c01N3dDW793hfYXdfVQIInnE29bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CgXBuiBQYIw9QKI-54MpKrk1yUee0KDZW04wMHQHtl0pF77gO2PilLbCWblFBU8nfE2fUw1ckaKOBWOD9Ro4piJie-MQ28_E9fLDfGntcPOUYgokolHxctSQzBOph015dA1BbMbA7vl1E5Xlro0oYPjhPtgapgOSwZBSiw0ywq_dIbJKxnpQmHth_HpjFu4JAoV3WfuddUiSPUGx5XRbhRTGfZbyQsHuXaEIqG0x5Y7CE9dg252R4bujcadruTIaSsy8xtdDSvG_6imNxLU3jf3J3rexRSmFA-8w89SRcpgStkq9dVzqdb6pY5hs0GwSRf0d4uMiCSGfAdg5xvgUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFPRZr8brt0wkjS896zh30sMXZuD02ujCgG-0XEmMdNbpuB11wm2P9LcBk0QlVz2G1Rk55-XB6YhowymeMQ_HudfleRk9bJLzQwgi-Oax2KJLakmxCvdOqxT2ORUUHoZ6EV0uXrrE-Ovf2y94cl7rig0nrqhjvaB0teKsOrhtzn6ll1ImgSpU_h6D8uggPNicskGq11TiEqyBm1kOob1yTmimsRr82YWMACC0dpnIryP6MX-j_q6uQn6MlC7z3Q_g8l0_Xj8J9GlQ3iZuq6v6Q2LSNy5Ua8PevzgVL9j0VATKB88I1fBAIcSoo070hLPmCvn_JtDbvXsz6aXUfwyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT6mZ2SYs0RkENUPs1zCwnTAaDaAIoYcy-OBSZXAkcWDZ14qF8B2WqS2-vm55QkArEAXcxebEKdnM2AaqB4A7ijCZ_kMzErWMjdIEOP2A-dPbDhcNql7dkh_J68yD6T-kyekYWoXsdf3kN8qvD6lGzH_meItYM3su51UHYW_Ago9hr5Sj_UgElvCZ8AcQUCLU2ez-l3w9H2ahBd9jX2JT5D5QXvUN-WFWHKayCbvP-xtOmxjrBGYONRFz984zn4VzoykYOqYIynp31h7l6c9yGvCHM_yELYkHjp3SHifrGwB9OiZOS3egPacyigoQ0rIa7-r_Gbu9h0eS-6QagF4QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq9dy90A2LnfA4LdqtHM41JrU7DjxWTNGpbhXbJ3tn5Pln33zF_yvh3cNSsE6mumdHkb_pE4BUeoaA9v9trIg1g-geSLOVU__uCp2oZDhnLrhleDMzbhK1OMCEAOKHT0sDrRCNMQDoTXI0VrBTEHShuMdkl82ywPzBgf8wtH6cfB8UjDBG8NzBW76e43EL5kc44lmIWrHgnlGgsmdEPKQagTQPj8WUS3NF5V2grS8f_u1iahIAzwpkfTv7b5ZTVoYbd2IGixbVbZ7gNlUvhF5Tad0yajET9z8xqaHHdW0fYmzCepV_VPPG6iQ0q3qTiaEMM2y4rlxeaxF6mx5tS3Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GjXp2g-FDlXpcjCU9GUcZyMceS5GbDyTBTo1MCAJZSkc8KCvoCnA6Cd93-PZq3DaM6An3WNppwPkHX8Rt-eV867jZDRM-i7yZp6VVCljVK4XYQfUqFXGDUQsY39i5jR8P9i4J6eJ3sZHIwNi47-yegeH64I--JWWb8OD0fPKXRh4UItrFCJ5PqdgwVkozyeTYb2W-oTWjuVa08PFSf2ihp03Bwsd0FHjbzunX33kFVvsEi_R8KyyV3VAV0xsAOvct2GGz0tnJqvEKp2RfRWo0vXeMtGW5Gnved0sKfHXIYFD2eFlZfw2yc6b8Ss5C8GMIpASJKrCWbdMuBkXe0ojnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCoy4aMSacQ9MJzSK5l_KkzRQhyjn_Yr0Z8eYeyD4rCXjK4aR-7KAGHOMpN6bLCc4s38PYBeleFOOQmSBSOhGlTLdI0SraPAm9pkotpZr7uXh-R65xYUaqiRVPIXWwZ48lX5ZcLyWRJjc-R8LHXO2-tSlEPFVB0NxnxgjkOHH3dGYUFt2avuKhttpyAjofn4bLdgHO0ZSX3bZkjd688Ucwg4GqxzxHwHGrhH2DNDCuvNu7L2jWjU-vSCLx8mB0jQtxWI7lbiAfzwjN6PNQ59f5QYeVGk_rE4cy2ebocBVSb-dr5z2UrpG4iyD8annx9D3jx-JbDEQDGLLTpEW7F9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jCMovnI4ggpdGqZgvxvYeOGASW8gujSZCWAOZvf48LQ8Y9kISa-5-bcRfqN6FZu_Mh8Zb2glrWdaWXm9uwZ-v_006VS9Ghc-jmyTv2yxKP0GTycUDUh4A0JRHr0gX6b78dSQq5jYWWBrTGN1MQ8MDKf0jIYfA_J8a63rRlHHO1eEL_sNkAczLxqsrPNzcaFobjwzxyuZMsIbEL7TX3fWYL0WbzcEQ0TxOSmIN1S8w0asFfTrmZIkDADSF6oxFyPT95SE5CZwV8iIoCTQx9uccaWOXxh77Bhs99fURIxfyFjc1e4KXhw3gbmLftHK1k7wA3VhiP13CVmEr27_ZWGpyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqRyWOG-G4cW3ZT5CQ3MWBR67egBoZ_4xskjR-HzMt5d-sMTQQo0DYsZid4z30Em03JkAfb2HM6vm22K0qYow2BRFps_BIyqc-KmLtHodoMvAyLLyGc0sHq3OPVtQ03Odk9DkyvdWXz2aVEIMUhAKfqvCIj35koaUvKVM0YviAYg0ZzW57MPJs9H9ozZqHSp-EEaxK4D5he_GeL4SbdHGQUEPw1XJd1iWNrTHSZpcb9NlfagZl9Q59pqu8IZfOFc_i6sX7hg4xLQbQp-FYspo4qdTFYlJ5GGMF2jrhwjgxLzntehUr71Pi5XvdNyWypcyMUxV9ms9XsQjhiWKvgX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vDrk6m83lKdKySDKu-IVpv9A9WakQQuC0NdKsTbe7U41Adx__AoLWwIEWo2PHBg9QUsdofINQrICcorl-9mQpXxwfESIeaggnBWVmxa1qYDR61NMkQ1xAIuyztD80fX8alOXisuX-knUC_3P02WaRw0KyVS127ljYYGtJx2w1QjCffPk67d78lv3nlKkJWpQJuAGkK0iAvDzbgvvnzcvBItBJibt9DZ8Z6FqlVXKZBSNMnF2MDtVu3UOZCkcyy-Mx8FwC2R-XsoMu7DqW9b09f87_1BSkBMKs8X0AYnIsicRXpCjKrU6sJV6-3X0RFUehPtx2X1dL9K-azVLMuwWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=VyvtrfhgFfoLXxONCPldYONB88pD4cAiXWxug9M9S3S3NRiFONyXCkNlCr9loS-fuELji1kdGcz3W4llMSt9AmXBJbvmasGHoq9OtD2CZMuamZ0dBm16OfspM1MEzf7PkjvopggbP6tcpbZBq3Q6-a6e5v9PfUL9OnzTdeY2MSnwIpDIJ8lW1wa4kb93rRj-ZVX8901pEfjP2FL1Koxbfq7slv83g34TLHFgXEUtqsXDHZ3rd0GE6JTtqy053wFmI3q1riL3hEtZ6aDWpr-adbxlv2X9sdBOs46CUeb848PlsHTnShgHNUywSGWvcN1HNevmv_7fj_xQvK3aP43tSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=VyvtrfhgFfoLXxONCPldYONB88pD4cAiXWxug9M9S3S3NRiFONyXCkNlCr9loS-fuELji1kdGcz3W4llMSt9AmXBJbvmasGHoq9OtD2CZMuamZ0dBm16OfspM1MEzf7PkjvopggbP6tcpbZBq3Q6-a6e5v9PfUL9OnzTdeY2MSnwIpDIJ8lW1wa4kb93rRj-ZVX8901pEfjP2FL1Koxbfq7slv83g34TLHFgXEUtqsXDHZ3rd0GE6JTtqy053wFmI3q1riL3hEtZ6aDWpr-adbxlv2X9sdBOs46CUeb848PlsHTnShgHNUywSGWvcN1HNevmv_7fj_xQvK3aP43tSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OnY7yRKKi1shCBi1TWOMw7qKGBSQVDdp9A0808yvxip4lQHMzDsNr5hQB2mq-IBS4B0CwyJ-lB1nye5OJIT91ejRSZatOlgtIL_ToYQGj_XV_qNbCqMUB6ThqQgxgdTkPwPnNhC9N8-MnJZ2fLaoI881U9UmdQqex1BDlaVrgX87qDpVTNcQDSsUzVJ48O3AHvn87LOwVcogvFS0K3bfLVFClp8D3ZtXYuC3SRrwFWZOvUpppcRPpLrqjhAlKSG8_ygPKs8AM-dHAtixIWEf5wUu7Eq2ClMsFbkMwwdPofBSBpphOI5VA51mqV2Gtg49q6nIPDpH84pq9BFFjBVWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ilXG-NaJbLKmGSfTDD2Duu1oEaQUxy357UqywZzB0HnNYvKZpb2dqDXabH1CbnM5j2i4TvPJJ1NGvLgLn0D8fnwo-FtPu-FkQaNADqhvqRtcwJzVKDSOayTtrVHipo6QL7SA1gQeqwHSyFDhrV9pS9GaqNIythuFudmWHhWZI0IZn6zjjzmtcd_7gxuSTyr4mmO_LfgK5SRYg6eyuixu35_1FiUIeMms2Ui4D8LtGa-LZbUmUIwWmiogzAhzZbMH65UWmPyJBLfh5kux3-3ZEivfW0B2fOW7AiJgJXVFIQAmVWIR6NCTGCuqNh4qagsGa4keS5mk_ABxbgnvt5KrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9rvID4fYTrwGqRIWUfCx96HyrceAHaQwc2FlEJCb4hq3rtdVzN5LIF5kDKtJDPc9N2YL_wHBdaOxD6dMvQ2Y7Dlr3QAPbbv7zaKznx18y13ZoQ36i_-I7r5BkZeszcVdNd-5xfk44eYobAH1O9Barqe-tWTDuHhMQAD8Zrku4YXKfGO8IKzvF24N4fV4ZliXxiN5wL_1A67daEnqOOeVAmD3ssMahAbzzt2UOm9qo_5vvo-gSISkQQb7HiFvRFwqTr3DwAApN-dN_qX3iCuHso_d5rg8Vd4meFrrnin--bjWlbSik-0LJ61DUqIkvxsaekb_dV4rJq9cS_Cy5_G7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=Jckg-UVTaHlSy3m1sHI57OR1lUxkTzYoNpl92SbmYQ0AYuIGVJxYdbEB3O4wyLWl-gioRxs4r4_l4EyPrOopoickjp4SHuPLIkJE4gPaYZXigcEWLjkX8kyk40_U9IFsQ2rl1GvsYf0WfbZv5KGE28pI0K322HkyDREZ9xY9fVCwtD-VlXYzX8oiYldIP8tkrr5J0hzGGT7sORlOdBrdYterW5JDXCKnToGUwE_DNVEjgia-JujrWmXjXGG9GBZRmx0Nd-M8e4Ll-a32vFqsefy8qDJssYm4mrRQYJdU_ZOXUPGEDwwIt5hOzijH9YQXu5r_RbEyUntf7IUimLCGBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=Jckg-UVTaHlSy3m1sHI57OR1lUxkTzYoNpl92SbmYQ0AYuIGVJxYdbEB3O4wyLWl-gioRxs4r4_l4EyPrOopoickjp4SHuPLIkJE4gPaYZXigcEWLjkX8kyk40_U9IFsQ2rl1GvsYf0WfbZv5KGE28pI0K322HkyDREZ9xY9fVCwtD-VlXYzX8oiYldIP8tkrr5J0hzGGT7sORlOdBrdYterW5JDXCKnToGUwE_DNVEjgia-JujrWmXjXGG9GBZRmx0Nd-M8e4Ll-a32vFqsefy8qDJssYm4mrRQYJdU_ZOXUPGEDwwIt5hOzijH9YQXu5r_RbEyUntf7IUimLCGBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVv2ZQFVRe55G7GJ52wibMr80PXlkItnFdV-9X8BSa1uoqxtrtreufoqBgpbl5_78vz4Iulct8dxswwrYr8mgOtAozoyc-yJl0MiDeAnxZyUxUnnKf7dt1_Wuvl6ECyCJ-jR7yiIjDaUvSLGtPQxs_8IHs3SkkY7txsg7YUJfIQ-F_wqNymlagNo6ASnY4wgE7H2ilimRXaL42qf7U6G0x19jAIj5okzdxF3gp9qyBUbFP4ku4SiLjlS6ittgVG9X1pJG2zjUd83pVAw5foU_1zIxMxmqQg81RXTE7sN6dUvPT1BIRy51nE4jAV4YCTcmodBmoHp9DOE-FLf-N_PBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cHn18cwLf4vGuYs4ffsJrqUGLeYpylr89Vdj40WHrAM5QBiMP4HLCGmYARo0-AkHYY_-cckjIUc553mBRHw_NPvU4Gmm9vO9TU5AbqiLgim9xOqtzUjJ3qfPHQ0xKA3zj3ZmXBY_FJLmwKdGTxq204RHjEpCVbW_lWlPnuTuWrIrnZarGyeYu7MkwVy4sq7-2anakKoFgFJUaH50BeQIJI3uoKzzzghiWNc5Ria9JsUQW35G8I7Idvfv5oZ4G37LJMSfHQPJT-dSUhl7Mt7gT18t5EdFad8qF9jEtCrDD1zk6J3bdu2O-yNcz0Y-pxtV9W8j6nSpwj_0rKkbPcVomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/htxIX1vGil24gvtdwFLlZlPzYHTBRuvexP8t_lwyegtTjNCT9ggdfKerdv58Z9L3j98iS_pCc1ZIlaJHwm7ZVolYyGu6HT7ev-gSXNoGFpCWvocVMNVfRC6C2GqLFLTzBbEkJOpB_q4IW_fdUfb3UuxtMsKEo9WFPgbplA_uKOUMAbNS-XQuZDDit2cDmUKtxNlfgzLGzTBzm1h8gdMCA21Ace9Wb8ui6eiMuM0ZkkX9xaIuDJlKxlRvxl67ynA64UqPDo3FoAVEqT6h1I56tFelecSmO2Ze-KIlTkQ3hD-LZ4yyPhtN5l4sEPihqMvcbPWFNUDuJd0aQHQsyrJ3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u1A5KY0tLELSgw7OCd1e9uYEZPlXPiyYWPFuVZpvWplqwT7cSFw8LLnkSKO1zzA3DX9Zf1uH3v4MbH5q55KMfh5W4UeQ8bQU_orH9JIPQKlaHJ0meIgPTK5C5o-qlaeGZlTu8ubj6EwLvEyTFRgD2t2X7o7OIs4smpd27lkZyZdOIAqBUDBLmGbrj0QUFgJCPi6_BhAg9baJRVG5N21S_5nck5V-N7ATOcznJyYw_rqntkQjQT5Xy5A1M5Vh7o0yC3gGSstZtFvTo33pQy1mPntsDsRdwCK19lwjmYj4GRgZQGA2AI-MHSSVUmlTiQ4BJLAfYGxLTQnzJzo3WaOjLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvFyMxsOIyrS-Txwya6ti_RV1ZzuGMtdwrdiDntkNix8in9iGSFl6mIEiNJbPawV4dZVbZcMnDL9KAe15iQsEhGdq586Ab0XOwhUprj76Nhaw5pb5qDeDKNsbQDzGsSP6tKHCKZZlSRCPRrGjry6u3l_V1_lZg7LGr1bYlCY0grzYm5SvCzEknP9E64ErVcXMUjWMa6BQ0GLeHjtll9ZxlEVx1gztsNjAdDZ5REY6jvZO8730UOiF9OMknayF6lrkdIYCl__Jr2PaK0aCl_k4WwDrXs74IqCcfUIT4rVhUysOEEHLTOBuAeYEl0tcGLn5pVu8AkeGi3szJV5AkE6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8dDDO6S-_2sJ7zhijVs4vOAkcQSTsvVyvwpw7IpirG9TRLLd8ViDUG51jFaGtJIV0ATA7AEGL8LP2ZotMlnF_Xo2kVFBX9ND1i6hce3hGK7lBt7dqJrkEBvEcmDcC0S1yrggvrnoWcpKPTE5SeQrPaU05I3hbjN4UaIgmtYELcuSWyPBN9nGtEoDBBFrZb7yYERD5U1ObhMHnMUaVQVL2i50KmQvTh82kMr0f1n0f5jbs42kOSISTDgHNbSu3pb-sGADJHtkbImysT3updwLEq_cDvORBTPPo_tse5XubUHAKYVnPFWoAEbPrnqMfyHo2oajYKohC3mgAf96nBEQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=jCH1Pp_AhwxBh1AlGxkNh3B2ZGnQ4I4DWaOcmlisuRvV1q1VhJQyzEwNY7E-K5X9TGYWfwdaNaeKfj4dlv7cq8GIgdRXPtRkgSpCbl_ZMH2ZRUGSZtRNxV54ovf8b5_u7x5KEuR5eb0TBgtbpSBL18FjCuIV_of0L_j8DhTFEntrXzncHFG69x1BfaoMDzCv03woPzLKRVxE_ju01HG3qp67Jqt-vinFxfjSfVtgJVuTpfYEOZdMJ1hMTUNOg-_mqWCOhNlAjSu_LdBOoWhhN6mLluAYWXYfqDHvQCfmLnzdereVMMOyewahCfNVzMc-4rBLSzOU6cyeEaKmcO_bGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=jCH1Pp_AhwxBh1AlGxkNh3B2ZGnQ4I4DWaOcmlisuRvV1q1VhJQyzEwNY7E-K5X9TGYWfwdaNaeKfj4dlv7cq8GIgdRXPtRkgSpCbl_ZMH2ZRUGSZtRNxV54ovf8b5_u7x5KEuR5eb0TBgtbpSBL18FjCuIV_of0L_j8DhTFEntrXzncHFG69x1BfaoMDzCv03woPzLKRVxE_ju01HG3qp67Jqt-vinFxfjSfVtgJVuTpfYEOZdMJ1hMTUNOg-_mqWCOhNlAjSu_LdBOoWhhN6mLluAYWXYfqDHvQCfmLnzdereVMMOyewahCfNVzMc-4rBLSzOU6cyeEaKmcO_bGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eun5jp9DF6dSdIF_eJgj0tm3Lc-Eo1437msHyZLbchVqCj3pco1MCWzdckWFWVj_XVYWXJQhiqc3zizV--U9Pf8TR18LrzyHslNRQArnISBUwIZaraGTBl6dlfGVqf_J6MIayGQAL0t3jGxvK2DB_RSn10l3Zjq8WI2y34nv28hN2MFlvTnYxHSJ7luSeGgstRch-HQrvO-KtMkzl7ZQNSEovLJVNZ57kVhMmmuGe3wWkLVX0spYxfLogGHaKuhpgMGHuxGo6-sAb-G9SriY2Ii5FLElp9krp2LyENpJrrUZFVEZIHj3ds9wHqH3VnlIwVGLw9N83EFtpcKdxFMqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TZxjTZfGQdwX0L85NJJoPKvi1MCxAxt5Gxik954xCP_VKryqZz66Va1VPmbIM9d_CyTajbo8WHlG69Oeoy_sQwd8Px3AxsDbPIYdjVmekWxBowkERPV_1OkRzpQthLlaerM4BO0jWxpOo3-RYyIdih0k9BMcbSm_7u081i7S56mwGigcmj_Y3r38EzugOsyh5mr23MFdpILSjZTpoOjieBkFzkV5Nu4Ph7MwXR5i1-rzUTQENig3SwTALkuCanO_k3qyhIRmHGTv9eQ3cueccTiY4kyAoJMBGCj7z1rXQCt-mOoIE2dyNxYEehFP_8h3736_nxpm6nujugYCry8E8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uMB-a0TTJAQq2xfgLzrHVwCCrMBMRyJUpaSkhuBZSFg4CevfA1LGAXH46GtIg8CE5XF2LBxtgmgSuysmtfDnVEXqiz31MpgKMPL0ZggS-CkNqZkhrecOz1eO4vkO45ANgy8tZ1yOAqJManfjBN9tRoBpLR3TMPIrlUrn9l3HHhxugHbzomA_M8clZWKFPBeAf2f1N2JcUrwLRWohadFMaPM3UFIStUaYW1dLRLsE0uredECJSpP8wU-OU4q1HTU9VoDPoS6hRLhcdpSlJnlQcF_CzQOOaqId_isZk3gXZfB21aciRu9n4MLWgzY5QlgLbJfyMEknzmz1AWkVju_ciQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQt3kSQmy0GXo-QIjErhk_H32A7q-7BUPFfHVroVy9-SIv7iXHK5NGdvmMTwP4hKKEdTLTMGfkaCCbeeeC5pUJ5Nm1fokkAMn0R39GidRuBEnI91giJgikrNLTxMdh2AKAObvE8BJIDnlYifGy-hoK_eHuOr5Fcd10Eg5fXeHqHLzyYOZzCsCf2UbDOhEsrUyvPMLBuO3V8_Rf-5BWJy19bDc8PvCZF_bwAvYKmDdAmhOKNfFm7iFyto5koO3W2qNwrw5vFr0PPVRifRMp-eewFY8tyc3vQv2DD56E_szr7o2Tscj7Kt_WpXEd_C_rp6QRrud9LSRAsWgNuu6uf3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSQWHI-pYpLE-Z6TcJ13iobeDFXdg-jVZdH-Ko1gj6Vw0APq1KrIoegOiLzq0HARgNo67bx-KpPaJACFPVa67HNZ0SKb_a-MVBov29LqZQNqs-K3lZDkvFC7V1GFuN2YEPvS9a-iZJfFPIABVV7U8cj3o3n9kgGnG3SduEApNMLSHIEtmjKK_tUn0jJgc_0_s7WKJ71UDhUDr2U1tDiQVZTLsVibkel8wxoUxQ6g9DL435D5I2o39DuVbXXCtR1Sf01sO1ATw42_CFiofa601VG0ErA2-EITxN0iYM8d0gPX1RqBGDvkF4jtY0V3yLgaI8-BF-OA__-XsyWxHfvXxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vBKxWUqXrajlD2MWthy7eBU2nGPe-9evjw6I9nSDiqISiHrFIPcSSZBpcQ9zqh97k2oCq_tNLU1Cgm-FBiQvCj75x7JTJrsfm_yhIZF9x10HuaZ8bxDviKwCwfojf9w4RIGS1IcOA_9VWXgSY7CLyo2SugNRugxyfFSJ4RJj1A85H5OOdDGH7v0Kh8rluZq3N-kNEs-mSCluVJxf1RQnN0ym6T2LugZYlOk4WLhVjlOjdu4FxNdIgaa0Cws3oiOKJpXgUfrAxVjU4_Kb2H-O-Zl1ihmsqMY3RJ0-amGcJoPJwjnflwd_wSAq70hluoZACAobufnn7vaCWv-csmaFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YiP9kWe_vjUnTV8N8vDjhizwLrJTj9VBejAFci075giLuKqf5Z3adzfAy4F5HR8NVTKtVKzNH5Ej2pQZz1P_3Sb5Gc1fpHSCPDkKVOmv1PZIEKRT-bum7GGqgslWzLAEq-e58Nv7Q6HKTMqMxzjyT1blwhnx9HYCQ-Frd3UUrD4dfpmrdHRZzY3oNpi-dZeSfbZq67L3a4tRsBeOD1uF305ggbE1tUMvXdROs7MvbJz-SFnnjVVyFMYebB3uZl03jEqFNz-hP_RNwFUYQcZrQN6WG4owE469ajPRrshZEvR5C_i6RVdhEvQs2wNy04xmnnhf8HeJ129JpkPnD1A9jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lBv0uNhABf9G6EnkpPXM_d7Gej1VYTvI7JpuB2y0L2u5KuvfSFhMl8QGbv5afMmc4EGj8-2IxLCj8kYEKSCP6iCLQJAOm888tDCvJHKx-d0fNB5Ehmnm-Z-2JDix-6iYEmFg9W-utdsjAj0CHVcoETgFNtov7XsRVAM9eh6ObETwREtySvU_lNOBScaVXqMo6Wmr3cQIQKCVoajjY8A9obsObMt7PebJB29Np4Qf5eH9_cRku2pjnUms67EHsSe4CTdvdBsFiT1U8zRET0ePQnGtJzeTXygwn49skz-PrpGmfRpjatLw5e7N7KH3i5FZNkVjSVjPRxuD81n10Iwp9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=L8sR520voapHzjTwbuBDFaT_BnrjjDHxxBfb1UVjyNa9oRDZQxlcGkyPMNddGhUzkjcJsxnGkBgsF46ITyjTQ1lWV6EpXFR4ujjMRvP27Y7Wlcshh7zCd5ZtqLO6eSHys9FnBpn45-72BFzIiGXoeRPwyOYxTls6km81U9oCnVjrtNDn4CXi-Lbbf2U2XV8oRW9sYq2lbqyxOac1xE1vq3kaq1vxZGAY8YoKOQgWn68mNoaUpUypb5dA1ERm9rzSyUkQdNadmdf-sWxtdEfGzCuIpJhqTZHpH1gq8y4_6GUG2ry0SiFV_MLi058P5lXv5PHhSnqQNaIx7mpAKrhqtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=L8sR520voapHzjTwbuBDFaT_BnrjjDHxxBfb1UVjyNa9oRDZQxlcGkyPMNddGhUzkjcJsxnGkBgsF46ITyjTQ1lWV6EpXFR4ujjMRvP27Y7Wlcshh7zCd5ZtqLO6eSHys9FnBpn45-72BFzIiGXoeRPwyOYxTls6km81U9oCnVjrtNDn4CXi-Lbbf2U2XV8oRW9sYq2lbqyxOac1xE1vq3kaq1vxZGAY8YoKOQgWn68mNoaUpUypb5dA1ERm9rzSyUkQdNadmdf-sWxtdEfGzCuIpJhqTZHpH1gq8y4_6GUG2ry0SiFV_MLi058P5lXv5PHhSnqQNaIx7mpAKrhqtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/La1iFpcfR8sc6TDXPnorLgtBMAhOYlE0qOARbi1-KHzGoYLXuxskfzYnhh5nh6Y4kbWhuX3yQDihgSzP6ml6stRT0wtdv6e9pybUnDz2OWtGpkniTlA_T2FPxtTyhCG88kaoBjeKHkqU2k6hZ5FIATB4nqyf3jbB_UqKfcj3gQsjAJkdPOQgQtHXN3uiqnp63wKtLi5NmAC5q3ms3ns1aLOdIPAB-QGAJ1ANAH46q9MJxiYRDPSXVu_RVlyvw0cL4Jut9Ke3TRSjmOlu4_jD7t0t1UTbmnQY_2Tcm-dDVnZZapgpnd3Ld-7s34AjUy4WB2-3QuzuiQ0wfGVHn5AyYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cCV3r3J33ILb1fwCq7GlelDwvCSoGbWGFO7nUmBJSt9nwB_SEnvO49U_RctqqdDIl2tIBzrcvyWkDZi1qQuNoAode1M-EIL0AgtD2ig5fb9XzGkIugUfArE6pINXrxALMrOyZ9DcFGnwRU59pCqe1RRCSWCn5OLw1V4vMa6V8oDKyeEgvo_X73RY5GCU4mnqQxWdImx13GB5W7sfaeSrG0DU99Q3QdtUQzWxabUyUPeH66v7gpbHePjdQjLFJmhyBSvNFVGQlg7wFHZrj3fRaGtKqXgq3-thwIPXequxXisuEayeMJoFL4FBkO_O4h8h7d9SeZQUxEydJa_Ke97SMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7FFii-5fUBJ9U6jKC1VojhsdVju-KVQycQSlC5pj64SD438dRRURs_yOvNdX_jH2s3WhF6fVozWMkABeFDH8PLiwQWHDuNyHBI9jyAlmTjub6tJaWlXxK6tQnAPqa_6mrfwvR6VT2nCNWuFPSxQ8Kjut-HEA3qRZfFMOInFCxINBHz2LojoV88CPAuoGVxMEkpZgujTgA4jkRrtlzKqI0bo-4s-ga6DTbE4R0UPS3AC6eJh9I-xZNyip0ZHzdNMzd3XgBkQ_y-xcgGDjBnMA9SaMtdvkH7ZI6hhiw1KgrEs2ZESVKGS2IbBbj0FtgAdE1oLFa9pbE6LzpzfKyUtxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
