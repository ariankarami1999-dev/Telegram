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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 22:30:47</div>
<hr>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hlIWL06yH3h5FTIWgjT07iPawDB7Lrl35L8RUuz8qRefIqABCad0LgRvhRHP4yG-jlNhR-3zei6-WtXWhQEMaDMdmVw-jXrPCJDDpTCmU_fM_80rduhYB1nUBpseBhbe2vI2NeoAnOGLXrzbotI-hR0F7mwEHlzHjS-vrAj3TQ5MSSJAr6GnKejGUyaLwBBKFoELgIEXZNzFpDqlUmmGJ6wUnpzoJtJlHxTlVWL99lQGEK9UEo_HkOuZCK50YpS6DTE0sNPleQ_5qok_P4cpteeLX-_mfORcy23PHNTzV0LN_vryyKLc3cp3NG0M0FBXBKd2cmChKNdG5tzh_IVotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mJP_b_laUGvNeJr1bbB30RWqtn2wW9gptkTVGLTH8-f_dtn2RWy1j2dihPZZ6mJ9lmpJ0x0mXfC88TBfVMl1S-1WDwrDAK4S1SY2G093tWNhXdNWeTkO7iNY-oulyljUCH3Tar3VcB6TtlzdUYwGV3w5U6KW1g92s6NP_CsXDNd2ecOYW_f51cMvAb4r6f4SsjH7GZ_RFPxXuX-a-SrkTrAmZQKMrk0wEV6s_pY_0Fs6D7JtQhLCVG5k922fCsSShw5qQqz5tJc2TRNAWFpHSq1-p9v2vfa6Qq1l9Wl_07nTBWZ44nSrrCMs8O8EesipKSA6HsJKhqliysWwCJn0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GIw-s61MobSs1w9HpcY_kPbqNfAEU3cXWBJxToW8IfdMCjjrAI3uH3g840pL0vCWhn6h7K6d9XFwge-YKucVCCsw1a_--su5Kdg6f62kdbeP_EJJ0qrhH5rQK1D9Hu1fwHsWmjvhW-Q3D4fA6KN9C2rRPjFsJgjSIOcuuwg_Sw0gPZIQybfEUD6xcTkY1B9HASKaKRWrKXnD_L3-dcJSz6wW7MnSAUeDBP0FBJwOXCjOtxrnOvD5NEF3hFvtZ3zGlvY399kvt3GEDcss3tgw0pyqsK3xrYTW1KF-rvToSl_A2WqwLOnQzY8QHiv19FAuwc65p_utipAI8sR5T-OajA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CE2jC44uoo97gK9KNal8KxE6Vg091RdJxUQiv7S2YMo2e9F97Fzj0y0R3DLPO_9cbWV-kKLK3hmRlSufft5YJHSm0FyiFE6rVcGqmXIuZLhbpOrqlgrqsIWq5VRMbsWALzLgHfYPaXDZjaaBHub-V-qOTlaEMow9Vk_YRAmriEKHL2znaydX_iRjrSZRCPzgLhqfp3lXtqp8c16oiUGZHpGLblzYYsop1PBO824tOQULGGkjPoQfhAmqWUBVwd3usSdwDIphLl--sUNb_qMCDJ1VIZgtnOk87q2BGhUHAt1oCIW0LPmTOf3zcpv-F6LPwZP0rs0T5bRz0Qk3x0NL_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k4e44i9h65hH5MLgwyTvI1JFG6RVZdjLDFD3_VZ9OPFNyy2vCV2WNf211fBJpjYAdGFqJ2Pwb056vQeVRfGDt3HC2lTG10bYdNRoTlRQOEnPfdBZB6stzG1ctH6_JbsoQC1k9d7jhrt_-c8XX4iW_35bXCLeS5B-GEplt5PL3D0eetmVNVapsjitpsp37EntQOjMepdPntgSFNskXQCIX5rOSh6Z8VLTUxiyhYEOusy7FsihvzgJRORIm7asiOG23zHnIX4S-mUszb4H27NdQ0ud9vrRf7qMMZ8rgI8rSmnLaoOWQPnsww8Ujqrhpp6P-aDe6Qa_tGyj0A3pEgigSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qjJ87iNYnObTAtAtiSpc1JN9vOIDiGKpKlLUZgdNZ8myb3z_6C3_TAA-1twaXXeuBQzQPoyILnFlp4rIdfKCSaxVMO-ysIu8X7gZxWVt51PSHEXUKr7FMha0aQZ_IA2M2BLRpgdb91i1L7mHZo3X8K10gcTEAv_Qhw99sgJ4ZhZixJzcuU7469Zhitfu0vtIrVYWqlMu--fTUxh278eCwARy7fkr-4-_Ab4AL-2c0Hx7IcAGf1JbQXM-7K4yXVNQDeSa2fO_-zPuxFupNygmiw-XeV9crFZdJ4driCvnYcugrXLUhaGuiMQY96-dgCDP-MrAdyEgIpbbwbovXrZTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g1w16IR3l7g3OS8YaytShZB14lW_urvRacbFM_Mr0Am-i-q8Q_Hj9bnMix_KcsZY8Hawdar_-_SVNOot2WzEPg5UGkJLpk8OteBS4FVUhF9RiNedXqwM1z8hp1X3XXh1XfgO0DEe00xTjPz7zIkg_rMqDj-2exeUgkYDau94bWLPmBUKLyixaRI0zfsWumSf2QSGHJJk0p67lw3QBheYiRxl-cmpnTiUK7Dex3qCrUxrH-ix7dTQ4wTxz0xiBojjsaEOFSosLpmRY8v9zKxJn0mZ6CTFm29GwnGzOIbOY7u7h9I_RsAQqoZMibo_18aSx2pwv9NnB0Y-JsoTZM2B0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g2JgrQzWeXSt9CO_vVNiPjAwdhgcx05AHTxw_d5JH3ZgDHJp70pbIRGmdwE9hhSoNHJaOZ7s14n-90qKD_aQxqwlLx-iE7ja-3AYcW7hJGg0ErUnXaNklCnVrQZ2phFuz-KssjdIi7_LLa6PSKGlWTBvOip5vUZ4PS0FWyYZMEfHMZ7wyJKMTLCd-uVrhnscLpxRefXSnro_r7Hgy8dPFaYJkYAcipuVCF-zAEf2L4fczklEHzl50XkZdsdiSBnX4qCj9bYGstNTYGRnT7jnxbylNO3rk68YomahiIlASc0rHAfFXhlzT23R27RMUsTi22ryqgEktX-CYn-rIrHdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FBNOFHjtgAYDts1EJISbh4C238ShLVqng7cahEWhIJTrMFBU3KR55XZs2vopJzf5AuUDOb9IXXTCSAg62gKvZMakHJvXn2_LpMTVetPYN-CnIiamoqBRsg6KqiU8B6O11UWVTMS6XeQ0TTWwE7seaPGknXyItcKvvihCLOGnScGVvqJILeTH2LUMItYsrbVBXQYVv_QMqFpgwWNmCaxQv0P0k70UOHIeuqYa1ackjGiF6vVPWOzWkuThDjcp5rIB9PCkaN4UokfaixjZMrHMIv5jDb51g6_5OwjDeiAFsTddEUL4g6gcL5qrLAceyYF8Ql8G75U-NhBhW37cVb2qng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/juqDMstqUqT576pZ4OhvOA6MkGVckmlkvDfvJsTgr728u1CPv5SXwNdcS3_nBPKiwSoVBfAdXknPsG4efiwvAl8Oxa9NmmPhNJT6WiHpOuZonQH_8qtwx8qFtD7fs0gDF7yOQ4Az0FQwgQGR0D375YO7sGVWSw2Izm4ZeENAzHgoAVhpb2HCWxm-jFPCr4cSzCsP_iZPTNANaDrMgMSUNZobL9KArgxGbiPduGECf9ubsq-mEFLmf7sLwKrt4dibD-BDUdxSUIVHaZX9uRwaflMfG_CkFO1Yu_C1QMOCDn1WIk-jVLNTIdVOviiRN4AV4nj_odOhH6ZHI4kRFBhHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vVWGdfXltnsMZtglOR-ERSep6ZTKFp2dDSeuZmZ1TsMcgHQuIEgR9fVTTtEtngzdvUv-7D77YQH2rpt3nmNQsNNm5TynCdHA8v-vCxwAzwX5qfca9Q36BUhtta91SuBOMXV9JlLme180lrYixR_alzUbpo2hrml_z-LaDu1j5lOcfNLlTyIe9Y9Q33qFSnn_E5qCDQBTx6qOMNzpmhXaiSKR7GeMht18O5d34pdJ0YC_ABiiMEvEk59orfMG2oK2rMgv2wOXO1pyNgaa8CN4T-AAlSnQSM7ghx5mVB1u-YuYZta4CqImoVlL8NwMMdJcleMqR4Q5mnN7eKKubhb2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LGgiQ5-YF0zGSmUYASnnjqenkuyoCaW8oiPNO6ZgVVqWqgIK0tTfuM3-mN7ph_8V8VstSpLtS48UwFdKerXi-UDDqPzkbNwOjudC-Qpa4X1RAAGEAbSM5Al79GpEGClYtDePWNAN7uli2D3rfKSqU0IZMeMEGKR7L_OxiHj1nSdLUmSHm3iHUyCF9i9KzQ0iFr4RtsdRTSdMSiN7r7KskxSytKri9rG_QrvrITuLGVjlxA3bF6qojPkGpqSsOAWSSfOXo6VKG2lEjGjLzL4gAgE8XOfqkhoEHZB7x9QOnlqJjNdTCCMWjAeDQETPTaZQOZCliIv-DhhHPTKuWgrEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SRVw-bDjGAx-6C8oeRYhSjByBTt51C13I6uSBTNGBjsmaAXAE26X0rAdcDcqDkrOvUWkWGMHNL707MyJQdnjb5dx5Ogj06471gWvT3F09IRv8f1r4X-A1y2VRiET7Y-FrJnXMNxwJ6UqSOH1M0yY4k7hGWlxEJrgofdZUL5v3AdqjUUVO-W5EfkTCECYcMgKnoHmG-R7ln_EqN00r_4My1b4yq-9usf9xweuUgVIXXBjbovg7Dkbf6COUT6VuT3m0yPg9-imTU1JVrDRvF0xfCcdqQi3j3919KCpvOSjj596kiZPJM0KGQWgqmsyf62-DM6lEgYl33q7zBrscvxKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IDn0JIWMBN7VAjbCw_6FUSSBu_4mYGwUyuX7sWAtHH4GJCOsxwMLNSYUsCywIjzW_s7w6_bSpn-l1gGtgGYyOaUCTZIm9iMrMjDr5upxs5AJCFXpjb_71GSg5By9VIawMBoEh0aGQvQmRtFvjNDDL6SnrknkZf367jpvT4tusrV_nMqy7neTjGimXgkRqJ3QAktisBCg5JwWDmkRO6-QjzVlGi7alTVxz6ko2ZoBfq_NXSJSqYWUu6eRmAC_PBHlEJdMIdwha7r1vfFoJEFc5yvrEogDxKE5g0ZTTJe04z93hFprgHMnRIpzq9FRKFOeOFaF3oRza3pZK0NV_XCboQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmQzeh6887eNGyqP3R02zL7TTCDPV6iOFTxbxFge1KYAUnrFFCnlIUYjdOOTPUhRTnJTW35zaHUcw-7efURwKAUM86YmMiDj_Uq9ChEzIQSgMCVIl3ITRG4GiPJT63dFbYDVmzHxz7rhPm1nyYuAZKJywXlOItCn5c4sf0TLFt71umxKzwjEBhMRXJL1-g3PwvkhPipx0OPUY2A_gV3F1toHKXGqaTMMPRcWAFKAoPM-gqWUxEA1wqgDVVd5zLRycV86z-ijxOB66v3wybdSFBHpAFNgETM03yJ4kQTX8ZNFo1dXrI-EW_LTSxZHuI2uYN_da-ipjf-qlemKGVbJxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HdOSVwB4gZGACPnzmXZkL0hAZb6Iv7JFIZGidmHZ9Gy3t44IApgjdSiMXaZpbgAOvJx3bwe8QFb21UUCgvcY-R1C5TgbRMqcnf8xVyQESaPVsHdvpfvEhwdZYYrnkvyK6wk32JAzPqBWhGDKdZU_4cCbQnvWYAeXfBR5jRa6tU6vpxZ5Q0Iq1BuMDf-gEF9tVJqcLKRAMALaezptLghJvUQOp0y6UafeT6dD59IDXKUNfxTZZpyhA4-oU9Uu_2jXlvRLwpUmamnvHDL45z_kP0qXbtGR464uwBAJ1nKNIbDwwuI9QIMROL2vt79FcVoUWUcchhlEczxQz7L2SLdXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hOm23LsLOqghiVjJLDJdsfhhDGhl5jmxIVfeL3gZmjYVFueIX8SCiB8sSTl8cy-003FANAX4vCZMxRCbgUnPKe9akbyUja6mzZjlo3WSVgtosjqqGPhiRsWkFA4aHT3PcBPBFKGEp2PQ469DphXry7Z14Qo-VPKNYqPDkdD18MTE6J3IT_lWYQz9nCLbYvOOqloaGSrIxgpXmqKwBe075ncJ7ECB0Q8ugz4bD6YBgT5_TQ0A-G4RRE-YDYj3uNFv_UDMglbx5jSdUbPLIW0N2zrN21i-TOmSZwpOzpa-EzUHWL440WxH_7P-9ERqSPn0GaazuA37v6WPn9KPTUjtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=QKDi-uUl8UKY3hBSHQPwndDr0cPXurfjibeAFePyuzHdYOEZxcYc-QhPqwNiAJeQGWTVd3tj1F7oAo8scaxpuvU5Axgvc37rJtTODCnxnVdS5EUYjeqTHWDHqwEs2pw5jGZ4StcrLx_IpFNOsqniSJZ5rUWsDYwt7VS5qvVKDPC_5ZIwhN506Q0AG4mGH5EVMJl3De_jNTCr7i8GfQF3oIvGCgdajqWeDdluWRkbUDrDFbhXJD62R-sh-NYbxPqiaWlZX-jmewpexBSw2WPIi_sn93Vx8jn28I-t9b-hUYayG4sIstADjKj6wwFsGMpcH36-tk8pPi-xAn9CzjEBug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=QKDi-uUl8UKY3hBSHQPwndDr0cPXurfjibeAFePyuzHdYOEZxcYc-QhPqwNiAJeQGWTVd3tj1F7oAo8scaxpuvU5Axgvc37rJtTODCnxnVdS5EUYjeqTHWDHqwEs2pw5jGZ4StcrLx_IpFNOsqniSJZ5rUWsDYwt7VS5qvVKDPC_5ZIwhN506Q0AG4mGH5EVMJl3De_jNTCr7i8GfQF3oIvGCgdajqWeDdluWRkbUDrDFbhXJD62R-sh-NYbxPqiaWlZX-jmewpexBSw2WPIi_sn93Vx8jn28I-t9b-hUYayG4sIstADjKj6wwFsGMpcH36-tk8pPi-xAn9CzjEBug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektCxIQz73AY-wMYrpzQECpOl1G92Bti43ICOiNhz54Z6ApJYE0GKYJlY42wufOYv6fw9J7vOii0qiBOhW9nAKtQQcZhXrZHRWNtpHXO8WwP1Hanb5VOZkotuGOv1TEJyXlzO5PF0FTi9abZNFLjCViU4ubARsBQDB4FC-SpK75BtG2IxfpIRFNG2zS7dIKfdbJG4Hh1xTgd-cOyzAirE913u2LlcR4qTSvUdOVr-1LAlu20qTbjk1YInCVg8oEV3VNsRYkCYpwaBxyCEz4QXpH7CNev0k7UnfrhDUMVtZ6jFLzYYwtP4hyy07BKofDNjBWQ2xmVsrQF9-kA0jLm0ly2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektCxIQz73AY-wMYrpzQECpOl1G92Bti43ICOiNhz54Z6ApJYE0GKYJlY42wufOYv6fw9J7vOii0qiBOhW9nAKtQQcZhXrZHRWNtpHXO8WwP1Hanb5VOZkotuGOv1TEJyXlzO5PF0FTi9abZNFLjCViU4ubARsBQDB4FC-SpK75BtG2IxfpIRFNG2zS7dIKfdbJG4Hh1xTgd-cOyzAirE913u2LlcR4qTSvUdOVr-1LAlu20qTbjk1YInCVg8oEV3VNsRYkCYpwaBxyCEz4QXpH7CNev0k7UnfrhDUMVtZ6jFLzYYwtP4hyy07BKofDNjBWQ2xmVsrQF9-kA0jLm0ly2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eSu9yWDjslKMacVos1n7Pm6aNzIblqEYT-xvRt04qMwp47Y8XcIXjQetC14mLiLq7u70kBvFv4BYCB6G8jikPVMEWMbKwBOTxFuRT2o4Ei7mRXGoXh4QpYYGPPfKcnQpYkkWM3kv7mI7dBQwSTiEk0fmIZ9MKUUm-fR13TEIz8Znl4pmhuHIJ2gUyA6bBc5wB6vFP5GZsjFiIHg5Rwel6fheMznZNDWQw0IPCRV7j-izNsF3QHa7ufqJf5J4wzc6lo0VOkl-ZpNff6nJxUPelZDCr5XLvO3mGdqloaAS7OprX1io9Ds6YuanP5YtszUzbn0uwqM3C2sIZHF90sF8Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wf_0zbbgCkJG9uGCyPEMDBf8Uxh6GtAN3nnxoKqIwlRoktgavCCUAjNXlSwBby-XpokPc3X1Yt-RYnlWL4v32RDts2NLmA0GJf-YKjmE5_RabkVRs77HT3ynRfXY3Hpw42N9ClQfpLf9C-zGWfBsz7jVvQsjvFQAjYVNoPYDCZcs0fG7Rt4Wpq86fiYVuipQOaMPNWd4PS8KJnyxUk7V91dOnrzTb3ydYo8drTEB4hBXUP1QBx8ooyVDNbke1Q-6q4xdZeF8n95di-LAYZH9Hb0yJvdYOSr3oTnYleWDQv1_06jUv3qFD2PUyD1DmO_jNOnb7LWGKRmBTbAJcavi-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eEDJCUnH4_5g7hgK5NXJ6FGe_FisJspv61ymNzE13UkASApeqwQPQipOJs0jX0tiE6gYRzWIGBLIdOQrfqoWOW818N8adBb-LzpS3R81r2-kfX766C3q4u8N-OEKcN9aT-qRWzVUVpqPT0Ri60g0zm469CZHqzSZMFiI5ZcvzrCoqTuQ8gxvNLxOk3w2alKUDD2-QX-iF6TU4-fWCPLOxLDZrLZuyYxKkLSQhNi62nLALzLLlQ7JBgjlLgKSvdiGUfxGNMu4afSBZOPEp4x2ltwgORot88hIx6SZ3ApNZo5eV-w7pxfzq2lXxNxqmsgoHP4_nwjhfTVeZUE86CbtzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dlhuGMiehhwzYlhtwSEghgKUFhxNnLohnQUD9YQwohbbpvReIGTKw6qBQVt6_ro9tB0IDGwt0vuzL_GQIHWFU0MA7YOzqZYlsOltQBDB9DhptH3S9L_ilOAoONy5hg-pRI0NDNRy5opYbQcNs9XO80I5oOj2S1B3czkoQKZGppp0le8TcZlHxXWN8zhfjBd_AyoCCaecF_4G9T3_jwWTKU54_cpzP-HBNju6PbyBctdYmOobVbDE7lBaNm2FoEdFKqx-mPbHl35nLvl7B9HsOkzNadhlaOPPemqJwGle-tNmj4ishND53k6C7pODqE-Yyt9aMIRaV-cMg7lT4Y8HKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mLRVX3o2HVuH2iSSo36RHzxgab_gHRR1yOyclSCHq5g3_D7c7o3tA3KBavMrYq6tIU2CD1CNRGejvm_suYDdOKeBIOiD9kLGANxl6hHdPiGRDr04XKByU82RPdaXpukQTlIsIDxaE8lrcOer_7X0U3-rebGQ66H_cGr18x3eGau5SxDlqaszXdVn15ttUEvChKHq-w_6WPOuv7MRkmiji9OBrUykHRa6NROQeboeDQByvwotlwgmKKuIFYUyVum9itODD4r7fKSBG8SH_OOAUq5W2IvwuwJ4AS9buHjyrmgbTE50pamFcHNCwSQvJlLWTBeftB-8y5SFT_ostbvAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d8qQfE9PKSpYTk-f2EYHpXpKXO6QqqUQhSgiK6ZyUFMT1rO2ENOqunVr1anqRkOJUlQqjprwSLqtmEW7FJlmgJ54vUZR_cB_9oIx7mDe7V3VC86Y6Vd6X71RKtrtqherJKNMgrbVgcp-J1EQkuQ1XN3IaWV7dfbqaoymhB96bo3KneAGARptCJ6jiWHaU-QXrgKPkpLzqlXnUfGC93mzkVL_Calh66LT5VZpLQp7xXDG3gFoTLqgVDHv1BIfT0j7ryRrRK14amIofRCVdCBFByER3Wr5i-5NXXGrWUHdrPuJR78pDqs2cwgq_WHcifBQr9EvFSnxoGhJ5hwLZ6WTgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n0IcQf5uKHzHJ5AuHaxJvAdV8izsBRfd3dOFaQ_Us9cKABcPa7t51RoD-gETZz4I5EoBbaYq2iOlEzDPfI-T8ugp8qmZiRukfjr_M9bnUt27m9CyCuy38L3Y9XxL10gw4jpQmrhUIcgOBGXb0XRSaMDvi0JlI5sw0KS2CQPVYgTU8t-RX9-j2kVNRJkhGZ5i5bXDt-WSqFz5qaPiEAqkGXwkYWv49ZPpcvHiSIvn2VEk2aaogKucfb47pEOhny8h8Ag8bE3zLJ2mxOKZemXcAQ2rcrv-AinqMVB4iie_tS9G1cq9E24ZXaMBR0sHRs_pOQ-UP7-RRnNrSNd3Smc1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TFfz8_IzwDJXfsU05JhtFDHoe35xbbb-ghfKgsEg77RXwiqZcAqiRxDf7tv8ou4pqFGBjaHtWFV6GN3WLJG9XcIAbshQHmJeEVoGAn_TVc3VrASoHhjbsTw3FpVzIiKoHfyvXkZYAjhS6pQpHQmTF-LDaHzdyKejN7xgm47g-6n70H_DK2P9tOT02_TeO6GytqOWHE1oPwEy3IPxXjq1rGUgEYwpeLDhS1GYvf9l0IjE6Z7gNJu9kClV3bWaYNYQWrgVB2lvM05KeGbJjm68yZd_qOkbcWbHIg_3DYpM6GS3LdtzYA_GGxHl4-c01N3dDW793hfYXdfVQIInnE29bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFPRZr8brt0wkjS896zh30sMXZuD02ujCgG-0XEmMdNbpuB11wm2P9LcBk0QlVz2G1Rk55-XB6YhowymeMQ_HudfleRk9bJLzQwgi-Oax2KJLakmxCvdOqxT2ORUUHoZ6EV0uXrrE-Ovf2y94cl7rig0nrqhjvaB0teKsOrhtzn6ll1ImgSpU_h6D8uggPNicskGq11TiEqyBm1kOob1yTmimsRr82YWMACC0dpnIryP6MX-j_q6uQn6MlC7z3Q_g8l0_Xj8J9GlQ3iZuq6v6Q2LSNy5Ua8PevzgVL9j0VATKB88I1fBAIcSoo070hLPmCvn_JtDbvXsz6aXUfwyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GjXp2g-FDlXpcjCU9GUcZyMceS5GbDyTBTo1MCAJZSkc8KCvoCnA6Cd93-PZq3DaM6An3WNppwPkHX8Rt-eV867jZDRM-i7yZp6VVCljVK4XYQfUqFXGDUQsY39i5jR8P9i4J6eJ3sZHIwNi47-yegeH64I--JWWb8OD0fPKXRh4UItrFCJ5PqdgwVkozyeTYb2W-oTWjuVa08PFSf2ihp03Bwsd0FHjbzunX33kFVvsEi_R8KyyV3VAV0xsAOvct2GGz0tnJqvEKp2RfRWo0vXeMtGW5Gnved0sKfHXIYFD2eFlZfw2yc6b8Ss5C8GMIpASJKrCWbdMuBkXe0ojnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCoy4aMSacQ9MJzSK5l_KkzRQhyjn_Yr0Z8eYeyD4rCXjK4aR-7KAGHOMpN6bLCc4s38PYBeleFOOQmSBSOhGlTLdI0SraPAm9pkotpZr7uXh-R65xYUaqiRVPIXWwZ48lX5ZcLyWRJjc-R8LHXO2-tSlEPFVB0NxnxgjkOHH3dGYUFt2avuKhttpyAjofn4bLdgHO0ZSX3bZkjd688Ucwg4GqxzxHwHGrhH2DNDCuvNu7L2jWjU-vSCLx8mB0jQtxWI7lbiAfzwjN6PNQ59f5QYeVGk_rE4cy2ebocBVSb-dr5z2UrpG4iyD8annx9D3jx-JbDEQDGLLTpEW7F9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mmis3Zf2l7rfKSuJx_q1e2-xj781z-rBcLrSwjdvCD7KxCeGjnRUdz-ETWsmrPBVToDAod2Tf49qiL5utNHQEL1xm7l0yL-maKzAcHq3cWP8y22ape6fM1HITProIrTIU9UVln0ipMJKOAIWHKHVcWyzMe5CXHIUHUxiStxXya61HFwM3vCkuvb88i5xdR1yI85jZ_sO2M-9xUW0OJ9sWOCseb0_aVK7CBPqnnv6lbdGyo8dLXgV6OTbZFC1bi22dAysOP889giu9nK8AmcRTN3bnyn5BWnAUgkMin-Q6JQo-N2bPNQw6pWUtVLSvEtpA1X0zZrV4Dqh-dCO51axwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6nm7tpKiTJDlZA20E9WxFzuYht0o1SeropOTOscK0RYVV9a8wnlaPOIdpk4d31ihLKl99Yhi1QAXNxEJTeDbVd9Lbd5jydzlW7XBvucMK5RcOui0lv6WuOGaU6mLataQiwWjDVCkYY6RKlxJPZc3JR9AD6qvNbH49W6XY2YwnH51JIvLWlY4_payuneXKVKBblcomzrFigu6q0bW-mBMw4tsrhNheM3TBDrA7oTEK5fGAvro2xhx0x-79li_WhGGBk5Oj3mwAB3gWAnDcX7IJkOIYsuBdO6SWFBOhW-w4S44vldZUwUxEpRX633X0HOO3lNXe2x6DrQr5MoDzw68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vDrk6m83lKdKySDKu-IVpv9A9WakQQuC0NdKsTbe7U41Adx__AoLWwIEWo2PHBg9QUsdofINQrICcorl-9mQpXxwfESIeaggnBWVmxa1qYDR61NMkQ1xAIuyztD80fX8alOXisuX-knUC_3P02WaRw0KyVS127ljYYGtJx2w1QjCffPk67d78lv3nlKkJWpQJuAGkK0iAvDzbgvvnzcvBItBJibt9DZ8Z6FqlVXKZBSNMnF2MDtVu3UOZCkcyy-Mx8FwC2R-XsoMu7DqW9b09f87_1BSkBMKs8X0AYnIsicRXpCjKrU6sJV6-3X0RFUehPtx2X1dL9K-azVLMuwWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=ZQ_j7OGxGM7J_RlZsv4wqaf4QiAau623pVrUCAdcVn0v4wa-NsFsfSl9GT1aiLmnz6um-fCDGZ1Fy83NRe8yt_XUBhMZiuT60-mjCrdlUVtqWZDDjq9IiKPjgsS21F_Zxp9MZeQBWAdN438rcLkKzw253gZTaw174Jki4DX8dq5Mf8kwApKCUAINjQok69IRVepXfMrjwATxfTGI7iP5ew1HTXqCUHPofD3gebsp3RVWniIJfe_rIQwr-sBi54mbuuk5Dk--XwYGAZQHbqHvQNr5TwAyHpwYZkpX_rZLOiomLiyoKcBFVtWlFOB-Zce4eu0aDYqS8elC0KuWk82rCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=ZQ_j7OGxGM7J_RlZsv4wqaf4QiAau623pVrUCAdcVn0v4wa-NsFsfSl9GT1aiLmnz6um-fCDGZ1Fy83NRe8yt_XUBhMZiuT60-mjCrdlUVtqWZDDjq9IiKPjgsS21F_Zxp9MZeQBWAdN438rcLkKzw253gZTaw174Jki4DX8dq5Mf8kwApKCUAINjQok69IRVepXfMrjwATxfTGI7iP5ew1HTXqCUHPofD3gebsp3RVWniIJfe_rIQwr-sBi54mbuuk5Dk--XwYGAZQHbqHvQNr5TwAyHpwYZkpX_rZLOiomLiyoKcBFVtWlFOB-Zce4eu0aDYqS8elC0KuWk82rCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCGH4MJcUQ5FyVClmscTkAJ6HivgFnZbtQVujwp01_emIckfFyJ0d7NG6Rmx3F0EwVGQbWvLkkJ1XIgD1qFD8KVCFr4IPUganwAElE7HoCVQUwJIkKFi8YPczEyYyfvVZAws4DnFvz5jRQ44HaIMB1LJodRWAhDeQ9I-koQO-9JyXiVxuTeXSood5nOgygdu0EBu0I0ym8uwiiDeUKYXha0PY7D3vLCiMZMbD1KPxTodv0L89xizg072yk5zxAfbTuCORKz0uCJgwpQkfPqbWbhqa0jxQtP0q0DTljqIA2jEI_D9snYhQtOc63aBNO-v_EN4XUPDw_fatPoGmWJVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ilXG-NaJbLKmGSfTDD2Duu1oEaQUxy357UqywZzB0HnNYvKZpb2dqDXabH1CbnM5j2i4TvPJJ1NGvLgLn0D8fnwo-FtPu-FkQaNADqhvqRtcwJzVKDSOayTtrVHipo6QL7SA1gQeqwHSyFDhrV9pS9GaqNIythuFudmWHhWZI0IZn6zjjzmtcd_7gxuSTyr4mmO_LfgK5SRYg6eyuixu35_1FiUIeMms2Ui4D8LtGa-LZbUmUIwWmiogzAhzZbMH65UWmPyJBLfh5kux3-3ZEivfW0B2fOW7AiJgJXVFIQAmVWIR6NCTGCuqNh4qagsGa4keS5mk_ABxbgnvt5KrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-EpzMOQF4yU4VGYtXJIpCy__R13PEOp38W0kOCnWFHwXOU-n5jC3HRIPHaXTLCyduSDB-6_sx-VhdMgDbOW536Y1xNO31_lk1lBicJ_kg_XZouSAgg7Em6qorfBZ9C6vY55opnZaKE4_qeGtkj8kf9nbb6MR5CC5c20cggbDHn76b-UAkmZiRl3v-2xruyfnUd4NW56OJd0VCa7tYnoqn0qotjik-rUda2k015WpQd8gSjCkLFs6rJoH7P3s1V0V-QXD7Z3O_dBQojRhVqokzYquZj9wZb-TgAaKIHqoKG5-BQ5cgTqZVCnioftlRJNO2R5jqqDJSnguKnSEwxCZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=Jckg-UVTaHlSy3m1sHI57OR1lUxkTzYoNpl92SbmYQ0AYuIGVJxYdbEB3O4wyLWl-gioRxs4r4_l4EyPrOopoickjp4SHuPLIkJE4gPaYZXigcEWLjkX8kyk40_U9IFsQ2rl1GvsYf0WfbZv5KGE28pI0K322HkyDREZ9xY9fVCwtD-VlXYzX8oiYldIP8tkrr5J0hzGGT7sORlOdBrdYterW5JDXCKnToGUwE_DNVEjgia-JujrWmXjXGG9GBZRmx0Nd-M8e4Ll-a32vFqsefy8qDJssYm4mrRQYJdU_ZOXUPGEDwwIt5hOzijH9YQXu5r_RbEyUntf7IUimLCGBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=Jckg-UVTaHlSy3m1sHI57OR1lUxkTzYoNpl92SbmYQ0AYuIGVJxYdbEB3O4wyLWl-gioRxs4r4_l4EyPrOopoickjp4SHuPLIkJE4gPaYZXigcEWLjkX8kyk40_U9IFsQ2rl1GvsYf0WfbZv5KGE28pI0K322HkyDREZ9xY9fVCwtD-VlXYzX8oiYldIP8tkrr5J0hzGGT7sORlOdBrdYterW5JDXCKnToGUwE_DNVEjgia-JujrWmXjXGG9GBZRmx0Nd-M8e4Ll-a32vFqsefy8qDJssYm4mrRQYJdU_ZOXUPGEDwwIt5hOzijH9YQXu5r_RbEyUntf7IUimLCGBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-YCBMKeffHB7AVDE8Fes2uanEMYnEKYzzrBSGNSZIWKRaiDiYSOrwPs4HPtv6zHyFjLTtYYHTULPI_NPawLyGjE5AjYR2gdgSQ0l7kA3PxvY2ovWdjnuwFRhd0X3N5NN4uzTPbjKo-MYac83KnC1zuLuDW3upo0zANHo2ydfeR-9TGzcIs9WrLtAVM7bhYwPEZY1zRj5Sl4DLZUF-dFzatVLYfKK0NDgwzZvoAKTrJaPK6t9j4qNVv-IbaiFD8UwDk0XJ-NaJbE5SGaoC8VqdSAfwU-VzUhl95VtS71pc4-E39ESFWczHZ48ax1byzJDDvnz7eCSIZg83AGL3iC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cHn18cwLf4vGuYs4ffsJrqUGLeYpylr89Vdj40WHrAM5QBiMP4HLCGmYARo0-AkHYY_-cckjIUc553mBRHw_NPvU4Gmm9vO9TU5AbqiLgim9xOqtzUjJ3qfPHQ0xKA3zj3ZmXBY_FJLmwKdGTxq204RHjEpCVbW_lWlPnuTuWrIrnZarGyeYu7MkwVy4sq7-2anakKoFgFJUaH50BeQIJI3uoKzzzghiWNc5Ria9JsUQW35G8I7Idvfv5oZ4G37LJMSfHQPJT-dSUhl7Mt7gT18t5EdFad8qF9jEtCrDD1zk6J3bdu2O-yNcz0Y-pxtV9W8j6nSpwj_0rKkbPcVomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/htxIX1vGil24gvtdwFLlZlPzYHTBRuvexP8t_lwyegtTjNCT9ggdfKerdv58Z9L3j98iS_pCc1ZIlaJHwm7ZVolYyGu6HT7ev-gSXNoGFpCWvocVMNVfRC6C2GqLFLTzBbEkJOpB_q4IW_fdUfb3UuxtMsKEo9WFPgbplA_uKOUMAbNS-XQuZDDit2cDmUKtxNlfgzLGzTBzm1h8gdMCA21Ace9Wb8ui6eiMuM0ZkkX9xaIuDJlKxlRvxl67ynA64UqPDo3FoAVEqT6h1I56tFelecSmO2Ze-KIlTkQ3hD-LZ4yyPhtN5l4sEPihqMvcbPWFNUDuJd0aQHQsyrJ3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QYbrPSZrvv6RNKg4jkbLxY1sFMtdlz9R89qRL2GotIfcv9R9aajk6RQnK_6w1HLtDnNDpBpKLwpMhoZQpLhjL5dW4mECLumHAqHNta9mDnyOTzo9ysNaXh65zVojYa4sblY9u08EVqLA4Qe3UbRMdfPn3xQGqL2MRirhNL8yjnr6iZlijReFUhvxkWKkLA2sFJMkR5v5HUTKsifw1JLl-ui8JgXkuXBGVRjyka5_1hEKw9BEDHNox6JpRo8WskLYCqQ8u0ubyHzkKed9llhoclHToNZfB9odBdz9MnkClS0sdEjpXkK6aKpqD9465EvZR74sfa7lpGjcqo7gO8UVug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8dDDO6S-_2sJ7zhijVs4vOAkcQSTsvVyvwpw7IpirG9TRLLd8ViDUG51jFaGtJIV0ATA7AEGL8LP2ZotMlnF_Xo2kVFBX9ND1i6hce3hGK7lBt7dqJrkEBvEcmDcC0S1yrggvrnoWcpKPTE5SeQrPaU05I3hbjN4UaIgmtYELcuSWyPBN9nGtEoDBBFrZb7yYERD5U1ObhMHnMUaVQVL2i50KmQvTh82kMr0f1n0f5jbs42kOSISTDgHNbSu3pb-sGADJHtkbImysT3updwLEq_cDvORBTPPo_tse5XubUHAKYVnPFWoAEbPrnqMfyHo2oajYKohC3mgAf96nBEQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z5YOvK6moBQIKtdKPHcA7jygYgXEBj_UhUC6U27tT9pnQ1UlssbfDTKc10R5vN4xnFIQE4IZZgLd-6QYV8zRAAfGYdzj-jkePW-wsf9NNHoxK3WfU_3dsQ61_EYEJJnVMln2rJjeoxRndWMNDLswez7KR3O_x6W7XVKpVeNpuGWr1psXv2LWxLhlFbvTSJuKTQ9dujEjpbljAbgGEUeTA0T3ZiWQ-ujiR_E1IJealZLTgbkPlJMfhNtsZcIq6GJAW4nfSF3c9UXkNbzi2Q6Bx-MX5f00Uig21aFYZkeOtmMLK1iIDv1U3nlxLMjQatHoAfeeXxNTBkm6vm3Xn0MkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TZxjTZfGQdwX0L85NJJoPKvi1MCxAxt5Gxik954xCP_VKryqZz66Va1VPmbIM9d_CyTajbo8WHlG69Oeoy_sQwd8Px3AxsDbPIYdjVmekWxBowkERPV_1OkRzpQthLlaerM4BO0jWxpOo3-RYyIdih0k9BMcbSm_7u081i7S56mwGigcmj_Y3r38EzugOsyh5mr23MFdpILSjZTpoOjieBkFzkV5Nu4Ph7MwXR5i1-rzUTQENig3SwTALkuCanO_k3qyhIRmHGTv9eQ3cueccTiY4kyAoJMBGCj7z1rXQCt-mOoIE2dyNxYEehFP_8h3736_nxpm6nujugYCry8E8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uMB-a0TTJAQq2xfgLzrHVwCCrMBMRyJUpaSkhuBZSFg4CevfA1LGAXH46GtIg8CE5XF2LBxtgmgSuysmtfDnVEXqiz31MpgKMPL0ZggS-CkNqZkhrecOz1eO4vkO45ANgy8tZ1yOAqJManfjBN9tRoBpLR3TMPIrlUrn9l3HHhxugHbzomA_M8clZWKFPBeAf2f1N2JcUrwLRWohadFMaPM3UFIStUaYW1dLRLsE0uredECJSpP8wU-OU4q1HTU9VoDPoS6hRLhcdpSlJnlQcF_CzQOOaqId_isZk3gXZfB21aciRu9n4MLWgzY5QlgLbJfyMEknzmz1AWkVju_ciQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQt3kSQmy0GXo-QIjErhk_H32A7q-7BUPFfHVroVy9-SIv7iXHK5NGdvmMTwP4hKKEdTLTMGfkaCCbeeeC5pUJ5Nm1fokkAMn0R39GidRuBEnI91giJgikrNLTxMdh2AKAObvE8BJIDnlYifGy-hoK_eHuOr5Fcd10Eg5fXeHqHLzyYOZzCsCf2UbDOhEsrUyvPMLBuO3V8_Rf-5BWJy19bDc8PvCZF_bwAvYKmDdAmhOKNfFm7iFyto5koO3W2qNwrw5vFr0PPVRifRMp-eewFY8tyc3vQv2DD56E_szr7o2Tscj7Kt_WpXEd_C_rp6QRrud9LSRAsWgNuu6uf3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qult8L_6F6MLd1rLTLD-dnpWtHJqDSQMbDm6YrSOfH2wRuciSQCl3Te7QlEETeokXBk74VHl7f9dKIgLW0zMnwdD636kGxCqHFN74v3jw-k11KzgAOCvoKW3bLeU467RZfosFg2CSf3i6owa4bNRLyABprda42wkKV3lil4aPBXYpHL9Z9ByHYAlDwQuwGXuTLAB4vZqO-wxSycGqOEVFMWGjc2hAfFQGJxwY_Dw-L6hjmNPprA9DINaFre14B9epes6t3X8Rp8wpd1bpNkqViiiw2ozfMiJXFVwLSEPxC1guOmwE4DoxIkfmunqrqouaZeLj2-9Vd-ySERDtn9Eww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vBKxWUqXrajlD2MWthy7eBU2nGPe-9evjw6I9nSDiqISiHrFIPcSSZBpcQ9zqh97k2oCq_tNLU1Cgm-FBiQvCj75x7JTJrsfm_yhIZF9x10HuaZ8bxDviKwCwfojf9w4RIGS1IcOA_9VWXgSY7CLyo2SugNRugxyfFSJ4RJj1A85H5OOdDGH7v0Kh8rluZq3N-kNEs-mSCluVJxf1RQnN0ym6T2LugZYlOk4WLhVjlOjdu4FxNdIgaa0Cws3oiOKJpXgUfrAxVjU4_Kb2H-O-Zl1ihmsqMY3RJ0-amGcJoPJwjnflwd_wSAq70hluoZACAobufnn7vaCWv-csmaFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YiP9kWe_vjUnTV8N8vDjhizwLrJTj9VBejAFci075giLuKqf5Z3adzfAy4F5HR8NVTKtVKzNH5Ej2pQZz1P_3Sb5Gc1fpHSCPDkKVOmv1PZIEKRT-bum7GGqgslWzLAEq-e58Nv7Q6HKTMqMxzjyT1blwhnx9HYCQ-Frd3UUrD4dfpmrdHRZzY3oNpi-dZeSfbZq67L3a4tRsBeOD1uF305ggbE1tUMvXdROs7MvbJz-SFnnjVVyFMYebB3uZl03jEqFNz-hP_RNwFUYQcZrQN6WG4owE469ajPRrshZEvR5C_i6RVdhEvQs2wNy04xmnnhf8HeJ129JpkPnD1A9jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lBv0uNhABf9G6EnkpPXM_d7Gej1VYTvI7JpuB2y0L2u5KuvfSFhMl8QGbv5afMmc4EGj8-2IxLCj8kYEKSCP6iCLQJAOm888tDCvJHKx-d0fNB5Ehmnm-Z-2JDix-6iYEmFg9W-utdsjAj0CHVcoETgFNtov7XsRVAM9eh6ObETwREtySvU_lNOBScaVXqMo6Wmr3cQIQKCVoajjY8A9obsObMt7PebJB29Np4Qf5eH9_cRku2pjnUms67EHsSe4CTdvdBsFiT1U8zRET0ePQnGtJzeTXygwn49skz-PrpGmfRpjatLw5e7N7KH3i5FZNkVjSVjPRxuD81n10Iwp9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=CmNS9kYtaaufuaDIk4GsgxLfoaeBY_OChNOw8_QI9WoB0GgWUTaDy-beHVOkfe8hC1YBpZdc8xlh6uNcceOhD1NxEcQn_DslZLUp3KrRq1jjQfrewbIRkLodwBwkXicTq2jBlHCXJ0E-dfeRMXqtpsvvqbQjaCRh2BD3VbX0P5Egl5zUEXwmVRD-Hrowe3jwn_trBZESY3XeCtVRydDU7jjie8xOLcnkVtnz--dIy7e02jVLJbtRHkmL357yscVng_uxPljYFDdM3pRBrhFereAjtZfEBa9XpN6xSsh3VzR1gyUCh53xspMWbAjk2bD9Q4OjlMG8deevPVgRuovijQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=CmNS9kYtaaufuaDIk4GsgxLfoaeBY_OChNOw8_QI9WoB0GgWUTaDy-beHVOkfe8hC1YBpZdc8xlh6uNcceOhD1NxEcQn_DslZLUp3KrRq1jjQfrewbIRkLodwBwkXicTq2jBlHCXJ0E-dfeRMXqtpsvvqbQjaCRh2BD3VbX0P5Egl5zUEXwmVRD-Hrowe3jwn_trBZESY3XeCtVRydDU7jjie8xOLcnkVtnz--dIy7e02jVLJbtRHkmL357yscVng_uxPljYFDdM3pRBrhFereAjtZfEBa9XpN6xSsh3VzR1gyUCh53xspMWbAjk2bD9Q4OjlMG8deevPVgRuovijQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f5JDDYYHc1VymhXGxXS6-0vCxyTveE8THfo6j9Ttu4t8F_fGIG-O4039tHAk6QfPgqJ-2csr4GK4vt0ybsBOJA4AHpzwYZ4DWJeJImjsLLK3BVKDkzIXkIPJ3s1OpNwG7ZHNTFYvC-Qt5hrqqcLMeXqmE5RffygUucv3b2htrx7mMLXpSxthfwAZZplEBabkIgLFJm1KYy1kHCj18_TRJ5JSX60v3JJ4-dOV1MzzBx5a5VWMMe1mF1KZBNZ3t7gh8cjefFHu3CmUmJa3vSwHRhEckBFrSSsfGx3Mvs7L74TLYJHDFd1ayUnWj-etfM9uxX6kxNvgvsvNU6vMXKmk4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
