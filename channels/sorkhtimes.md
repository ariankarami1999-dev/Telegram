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
<img src="https://cdn4.telesco.pe/file/nt0QD6r4PMY3f9C8KgJSoDVGyCNedM2O3oaS8GUg_FCunRK_2YTmprsmGLK-zY_Tpb4H9Z-KsQPaVua3X7aob48tq1AwA_YdlSPVHz1Dt11NNmJG4V2TwQMSGEvaM0cM_WKedHFwfh5_8gS6IHj6sJjxK5Sf0U1ws20mp2Uk-zjag_jF0cITtqLzFXhTyC2ciUjmKwQDf7Cs4FH9iYyGWgQkPZv1XkLYxN4J7OciVehMzDz1RnAi-zooXMLnlMz7aQfIskXozYiA6Tr_dysKM2DZOanfi0F_12wKH1Wy5hyOgAex_-PuHAKzdSOaC1_mjl_7YnhnQFsFz0RCAGEudA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-140316">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
رسانه های مملکت گفتن آمریکا مجوز لازم رو از چند کشور منطقه برای شروع دوباره جنگ علیه ایران رو دریافت کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/140316" target="_blank">📅 17:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140315">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/140315" target="_blank">📅 15:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140314">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
❌
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/140314" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140313">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
⭕️
⭕️
فوری/کانال 13 اسرائیل گفته آمریکا و اسرائیل تو تدارک حمله سنگین به ایرانن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SorkhTimes/140313" target="_blank">📅 15:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140312">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=DTF1gMgSVfRPpIrg6ZIwFKO0NxkJLyjxQY0Xx_Tv5jj-1xdLiKxeaxPbV8Y7yTeHtiVu4w2pDT6s8dZ_wPM86w70xTUnLyJoj6Iu4Bx2FqeUY_7lHAMRqFOSvrnpdbom3FclAV052HUy1skn0DcAzh0URiN7gl9GPxgxQXRyZ1l9CyMF1FlMp7hsw6XVXQlSkydtmvY6OY5mi90jwwFF5cFn3UxVj6MqQXoNzgVSEdw_24ytul8UNL4SBjDVOc1pbGRrSqe9fgMTU2HMbuAHupHisqmS1iJjOdr9Soko03WC9kGflJV7LLeeZQQR2I3jmGvhDavfd7SW2f7yMQUk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=DTF1gMgSVfRPpIrg6ZIwFKO0NxkJLyjxQY0Xx_Tv5jj-1xdLiKxeaxPbV8Y7yTeHtiVu4w2pDT6s8dZ_wPM86w70xTUnLyJoj6Iu4Bx2FqeUY_7lHAMRqFOSvrnpdbom3FclAV052HUy1skn0DcAzh0URiN7gl9GPxgxQXRyZ1l9CyMF1FlMp7hsw6XVXQlSkydtmvY6OY5mi90jwwFF5cFn3UxVj6MqQXoNzgVSEdw_24ytul8UNL4SBjDVOc1pbGRrSqe9fgMTU2HMbuAHupHisqmS1iJjOdr9Soko03WC9kGflJV7LLeeZQQR2I3jmGvhDavfd7SW2f7yMQUk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
| فوری از برنا:
⚪️
❌
ظاهراً عباس کهریزی از ناحیه رباط صلیبی مصدوم شده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/140312" target="_blank">📅 15:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140311">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/140311" target="_blank">📅 14:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140310">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drmUpS-ARIcc0V4h3swJH9UiQNA6rTM3iYGCH68N68KVbhccgHClni6CspAe3sJ_JOiG0YlS41xjgj6669cicce5qbSjbVCa1UzuU6kdNImyCBUjwOM9P9y_I082lE_57NYpGY7YUtCH8GwgSBxq-r77ptmBxNwt7HKXyM688RWpOrf6BEtUoS6qeiIh-qIp9xyUjfIQDiwqg4itmMq2rwSWP05jH1KCSuqIoBU6sDIBDQO-y-heMtGyONmdtrqMhp1j7bFCADlKW-bWHArprcvFP2eXSixkXFQz_nrrw9BNcv8ULMYwkY4JRBSOnwRxO4FVIlEQRWuxIEZXc3hfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مادرید در انتظار یک شب داغ؛ اتلتیکو یا رئال، کدام‌یک حرف آخر را می‌زند؟
[
اتلتیکومادرید
🔴
🆚
⚪️
رئال‌مادرید
]
⚽️
اتلتیکو با بازی فیزیکی و فشار در میانه میدان می‌تونه ریتم رئال رو مختل کنه. رئال اما در انتقال سریع و خلق موقعیت از کناره‌ها، تهدید جدی‌تری برای خط دفاعیه. دربی مادرید معمولاً پرتنشه و استفاده از کوچک‌ترین موقعیت‌ها می‌تونه سرنوشت بازی رو تغییر بده.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/140310" target="_blank">📅 14:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140309">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
اوستون اورونوف و ایگور سرگیف از پرسپولیس به اردوی تیم ملی فوتبال ازبکستان دعوت شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/140309" target="_blank">📅 14:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140308">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
✔️
#تکمیلی؛ فرهاد مجیدی سرمربی سابق استقلال ضمن تشکر از حدادیان‌مالک‌نساجی آفر این باشگاه رو کرده و اعلام کرده در ایران تنها حاضر است سرمربی استقلال و تیم ملی ایران شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140308" target="_blank">📅 14:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140307">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">😰
مدیران نساجی دارن با فرهاد مجیدی مذاکره میکنن تا این سرمربی جانشین مجتبی حسینی بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/140307" target="_blank">📅 14:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdPvNrkQ0TYrIrKVNn06NanZNVy6HgJ24L_6hFxg0bq2lXcxOgXz0Ih2VnpMMfmkysLyfrHeTGfx1Nfo7UYq6vZwzX9nlpmU4iRQf9cQSRLPOe3DGdivqj4avzvb_ZTZZO3HpjlGO4fRE3p-2kFiMBA_cctAYHs0TuqHMNaqQf1ohCqrBJgzLfyF5NgAY9QjK265Ta5jKSEtVPitPx4-hyRUi9wtUyQ9oIwVWOROPaUsVPJVIJCU-i0ECMxEaqfnrFdPc9pDOU8Y69hdXhFKLRe_jLEcUNiFV6IdkwE0fw6lmK3acln2aMQTEZZoXF5pyjJznW9fs6taPDljFPdGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا جهانبخش قصد دارد در پرسپولیس به فوتبالش پایان بدهد
✍️
ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/140306" target="_blank">📅 11:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140305">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqUD2ndD7sFwSXOgEzcznV7mqKZARVxgGgTqz8K1O3JVXYDNsDiCgorvvbXwT2eCf-2rTAZKeElFvS7V65AdQAjwJovWCkGaGOKJDfcymdHwEmjZE4XFwZsvNn4iR1Ceylq-u06jGsEEuLvMMixdUKZUxxx6sWhUfgFsZ5rg9gR6Nh8Aw-zpJh-4ERleHV-YjYQnu0tQ1fl9b9JY2hPo_44GZLDbpp7w9wLxjGXLSxen2TC15Vd9UVg7k34wAlVqiJJTGqc8TbKTtBiAiZ-Yj_QfxkEhV72GVfpx9f-z7O8WZTgzN5ewHzQvvvN5YvWKZ5rUm6_5JAgLuzXr0xlUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/140305" target="_blank">📅 11:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140304">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZCCa6YmageUjgQ11s9uKPYfRPCKq52xIJph_INt9SIJ3p9F3nFoO2z6X5ZKzQgeSlja1FJzB6kXLE_KMfdqpGF9zYsmFYbFsg0pF-XJ_i1Kyve6dhbTXXanUYB2_pTaeXU6ppVtllccK6-xGlUUUUIG0D5XsB0jNcxmQiiTSEspWdvwNx8cURbafEWxwBM_An06FDOwP4riDAOJ5A7LyoXKZE3sUoub9Sy6ZBeXc1zwSOU_DvfYis4QmnFsmhH3EUTUfoWWbZ2DSpNtoCxt-ZghJcdbGt2Wp15CE1ALsE7qu5qR2lHKn9hLXaUgXUjXHIj4iQ8XnCBb2ZDaUbyNhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
✅
امیرحسین محمودی بعد از اتمام فیفادی برای تمدید قراردادش به باشگاه میره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/140304" target="_blank">📅 11:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140303">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚪️
مهدی مهدوی کیا: مجاهد خذیراوی به حقش در این فوتبال نرسید/ حیف شد و واقعا سوخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140303" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140302">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140302" target="_blank">📅 09:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140301">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
ترکیب تیم امید ایران مقابل چین
✅
✅
محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140301" target="_blank">📅 09:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140300">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140300" target="_blank">📅 07:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140299">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">■
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140299" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140298">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7qv9MokZpGj6Ih7pwmBePtjHssBeeuVEi4ZyUS_bPnq4CqfC2TFt0MQ6fMds0B2rD0O1YMXB3mKTU8Ro-FDtJRcpx4-F4MAA56nbnRF1YCFwFhZ7YCs_VzcMciUL8o1h7X9lTCMwcADh6sHQ336sNWbafQ_5pkXjjhr7pKTEjFAj8i8vdEkWw34shPZHcobL6HgeY61BKSiwFBnpIXMzHYFEySzTaRQJqE7-oqaVMMEwnWCslJ4ju_xtpNs_PoXVo61mBZawyR9xllKdOlc__xCwSpZWuBEQy0M52FFaVtTx0O4wtQIFp6vspQOQM5BuyUfXkldoj9dINAQ2pfuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140298" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140297">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
باشگاه نساجی مازندران کسری طاهری رو با 703 هزار دلار خریده و با 863 هزار دلار به سپاهان فروخته!
❌
❌
قطعااااا این انتقال پل محسوب میشه و باشگاه سپاهان تا نیم فصل حق استفاده از کسری طاهری رو نداره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140297" target="_blank">📅 00:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140296">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
❌
دوگزارشگردیگر نیز با صداوسیما قطع همکاری کردند؛ نیما تاجیک و سعید زلفی دو گزارشگر مطرح، خوش صدا و با سابقه تلویزیون بعد از قطع همکاری باصداوسیما به پلتفرم نماوا اسپورت پیوستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140296" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140295">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140295" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140294">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140294" target="_blank">📅 23:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140293">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140293" target="_blank">📅 23:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140292">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHeF9Lpknido5yebaO7DwZVt9TvoqEi5sJZUq79x7PlQ5YTaPNK9d8pWho-Cxt2jh-flq9y8d5hu1cfTd4Azcgi7p-28NFZ6KzJKEQJUsZJeGSZ_zCcGPo9FZ5BDmvMujUta2IP27y_1nylbdqeesXzUk79eMjhSzGf9El8qpc62Pt2pNZGrdmo4FmikudILr9Zyc86Mu74ulvy6Zx0MZ-caOmOZJ-fVT88YDH2sPd3a5COa_O-0DOUwE13Qg3OeAIIks_RJl23gONtfEAM9gp8xfOGTLEuzrUNe6EaiRp-r1uJn1C8e8e37WOpYQ6TOPuf6zGtKk5xRTLbX0O4EFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گزینه جایگزینی یحیی در دهوک مشخص شد
❌
باشگاه دهوک به دنبال توافق با گل‌محمدی برای جدایی است و رسانه عراقی «روداو» این موضوع را تأیید کرده است. مسعود میرال، سرمربی سوئدی، گزینه اصلی دهوک برای جایگزینی یحیی گل‌محمدی معرفی شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140292" target="_blank">📅 22:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140291">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=eKhTf0KGpZwH3XA6qAIL5x5Ymwyub1g5q--o_XyYQpZhkb6BE5zVl9xwFYbo0PS5ZjrpNJ_oBhDMJw8tg9rm5NQjCawqi9wxe6WLlBLpxUgoWSt8eEltfQk9fpDXl3kUuPdIr9jeHRL-exCRxJNExKNXURvvurSEBhPVct3KXaO4ovGEnCb6U38H4I1vZ5dl8DUuTj6-9Jvo4RM9ZtEXsj-qM-PqxzpO1Svzatgs6RLWkx5zJLOMcD1fzdsmQwc7JKVlGQGsJ_wfPHSQY2c74D5A5hFqmnGxobzTjI7egXgDZxZmCXABeZIvnVmmPImA12pZLPoH3_cXuBBwud61Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=eKhTf0KGpZwH3XA6qAIL5x5Ymwyub1g5q--o_XyYQpZhkb6BE5zVl9xwFYbo0PS5ZjrpNJ_oBhDMJw8tg9rm5NQjCawqi9wxe6WLlBLpxUgoWSt8eEltfQk9fpDXl3kUuPdIr9jeHRL-exCRxJNExKNXURvvurSEBhPVct3KXaO4ovGEnCb6U38H4I1vZ5dl8DUuTj6-9Jvo4RM9ZtEXsj-qM-PqxzpO1Svzatgs6RLWkx5zJLOMcD1fzdsmQwc7JKVlGQGsJ_wfPHSQY2c74D5A5hFqmnGxobzTjI7egXgDZxZmCXABeZIvnVmmPImA12pZLPoH3_cXuBBwud61Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
مرتضی پورعلی‌گنجی تو بازی امروز تیمش دقیقه ۹ اینجوری ساق‌پا بازیکن حریف رو قلم کرد و خورد کرد و اخراج شد
❌
بعدش جالبه اعتراض میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140291" target="_blank">📅 21:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140290">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG4EKl7Z0ZATDRQU76OgtOrjn0Vd3jdMht3SqN-qLp2jioBExuqg_uQTlH4ngV9FblAOCMekRJvipFAoExYEWxc9d0b64AtHsIzjSTDXtTsKq-x-RIz03u5tBzyjHzmFNpIssxh5m0wDaXdSLH5GN9NJEbbjCN_buQG16mJZ_5p5oAUz_sDX6IvU2oK6mw0zAJxbLTSEU1DNGDaJaH5_OBBn1WluD0peIEEn4jKTspBYdA8nOgeN0EdmLcTYbpLVxttaHdcTCFW34tjElLF2lIX5hPKq9icBfaX7SJkz8a33z0qgwJXGwNcbP7qadNE9BoXc0vc3oZ3lytKJU8MW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140290" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140289">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140289" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140288">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔄
🔄
محمدرضا احمدی از صدا و سیما به طور کامل حذف شد و حافظ کاظم زاده مجری فوتبال برتر شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140288" target="_blank">📅 21:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140287">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
بشار رسن پست مربوط به بازگشتش به پرسپولیس را لایک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140287" target="_blank">📅 21:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140286">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
❌
❌
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140286" target="_blank">📅 20:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140285">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6gGz_uLLRfIFc2fY7EP1HUOQX2Qu1sKBges6Pntu9bCy0Cdav68xhY6s-YlnfQtGX_ewygCovBlScM4GzbmckkJue0QZp-oROa51d2MQPCRDJqbg2-2VhD6NhBjO-4n0sKxWJv6YAFPbAJOQXqQlZtQVwm5fXtRfalh7kj8e7m3wOjrjc5SARn2aEz_Tn4MljjJ34z2PrrqYupFuRh19GIC6Md6nP-xcFcFsZl0k5XCOkxRW5ZzuxvCIUfvV0a4QxqfCVsH8q4q4YIdwLSfuAaKx7imPMDDnlBgETLyDwHVxL9xsETLupUBe46MuKl2hpiBe-qH9ysxY8AjerOdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزگاری سیدجلال حسینی با وجود اختلاف قدی بیش از ۱۰ سانتی متری که با کیروش استنلی داشت با پرشی فوق العاده سرزنی کرد و رکورد فوق العاده ای از خود به جا گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140285" target="_blank">📅 20:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140284">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140284" target="_blank">📅 20:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140283">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcjEGJoK0mwhPuN3y2FN04WJIF8RbL69KEUJubju0V2yZdrCbAFZrO6rL2cefG83-zb3tNyImW0BXQy-c58NQ8jPIdRry5TC8z4Q-IIPtxkmb-UWamrCylz2r57jbm5YMw8SpHgn54R8T5dWb83Bh6h_RARfsNW7OUPiEbw0Ivpbd7cL3QcwoKBmPQOkuK5fCIMEpSjaLS4NiKw8cfRDnes-zAJ_ALCmaa6sPBcwyGh8ShHeBXPrg_mKnDzKTho_CmLZsaxBtre51-FkynwVNEGKVMbrhwxkGiqi9deDcYx7a_zd02dz-PWx0VHsyFNSdrekdkjPnwfs3k23HumOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبرد آندلوس با کاتالان‌ها؛ سویا سد راه بارسا!
[
سویا
🔴
🆚
🔵
بارسلونا
]
⚽️
سویا با اتکا به بازی مستقیم و فضای هواداری، می‌تواند کار را برای بارسا سخت کند. بارسا از نظر مالکیت و کیفیت فنی دست بالاتر را دارد، اما مقابل فشار سویا باید کم‌اشتباه باشد. تقابل دو سبک متفاوت؛ جایی که مدیریت فضا و استفاده از موقعیت‌ها می‌تواند تعیین‌کننده شود.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140283" target="_blank">📅 20:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140282">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkVve1VrtwkeGkrLeDC0PWATGZlWKx8-PA4521r4JuAMl3DZ8ZJd6iNlZqDUopb6C7FXciidn8FsNgWtfYTzSo4tXOR4WsfgQuc6fW1dfIEXkiVRrMmC0Sg9P2yxrdSgrB91GGstmAzLcfLbiKeBtWjdeS8bEH4JfxmDl2oWGkbiTEm1oGIIyciFx6DiT8C3poBEVmKAOhPVyL7PLF1c6uA72tudmXqeU_k0lb5YSg9BUvzdrb9Bn2t0FvzqAzny2ozbqnQ8WBNp82tETl1lRA7trvjhl24jBP8VQK-9AKpCbLcLBKj0vFNIOUuM3h2wVYDd3_FABWBPp4wtaAExqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140282" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140281">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LznLkvV6Mm73oyHF0LzxzDqwkI_j0vJwwPf3txhrYVVppox-HUb743dugCK-r7SRg-9ak5xblZX7X9UM0v7IXgKZKnax2xpb-eY7rs7Vhg3ROpA4k0GXKShX9DdOw4TzKtXg7WLEu1k3slVIuzwZ5KkZ4PoLRmTkbydHIOvaLMUy8AypINGIi2sjS83wh1GdKV6jih4IegANzq-jFGoT0UElRYy72ujKceEDiIUQE7UStpniwhpddHH7fjy9eV2H06vnXmVQfZ6II6TAL7o1L1KK1r4uhYpwIf5jRdMc7H-6uqir1N6jWKk50Skym28upWJLwsRnV0zyW-JY5CRRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽
بازگشت سرخ‌ها به تمرینات
⏺
تمرینات پرسپولیس پس از 5 روز استراحت امروز با حضور 15 بازیکن از سر گرفته شد.
🔻
ملی‌پوشان و بازیکنان خارجی تیم غایب تمرین بودند.همچنین حسین کنعانی؛علی علیپور؛محمد عمری؛حسین ابرقویی و امیرحسین طاهری به دلیل مصدومیت زیر نظر کادر پزشکی تمرین کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/140281" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140280">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcagy6K3oh8t6mV6BOWUB4ZLAQ2lLpk5qWz9bEWHmeshrybC0nl5zI4eY4YgO9tIVBEOw2NbZFdqfe0R7o0smxgpLpy7c8u6bmeQpZUaRUd0deIsfzyiSDp_cYZcF72OCMd5nrtluwDv2Rs_nYxv0kIrYK12cu1u-YqL7lIHL9_UQLCv0rrVhhnQ5Dh2mpp1lcPclAWVVYCnHGX6bD2TVhN-OaEduT24UF_g1XxKhx4a-e42QJyjQA1hKJQOfsSQ_uKUhFGSgOG0O2MzhJlGZl-J6fNcBBJIfPK_dmv0ardNvgE7Mely2YD2mNA-7bx8QQjKkPGJVvQ7A8eLavv-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری شایعات
🔴
🔁
🇮🇷
ایگور سرگیف پایان فصل از پرسپولیس جدا خواهد شد و مهدی طارمی به پرسپولیس باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140280" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140279">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227e813e97.mp4?token=bj-NoleEN9uOCnN7OIXKOnV-7q_VVNfUrqOPqd22Z-7OhPKod-YB3xb7YCHxjRM5tj9ioIfAPPDmUG8O6nMD_n0n2rI0vKrDHE05zZaRy1TP7cDgIZq3tURzECsLCAa7P_8B5Dw16ORaacDVxeZHsoXAjN2WDr0RJ7X_Cyu71AfPHicGAKmbbdXW_vGqwgf2fXs7PEHT_-9G82amwtdWQOxg9ObDnkIGzST4UCJOwlqLpAr4nayZgRXDLNZLbM-NDavdY6iaL9DHM6dSyt2bcJve_IPNfSYpIgI-xyB3aht4ONSd-fHzfvpF_joU_1SqFEmZ-8zBsPsnR0a4kvY2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227e813e97.mp4?token=bj-NoleEN9uOCnN7OIXKOnV-7q_VVNfUrqOPqd22Z-7OhPKod-YB3xb7YCHxjRM5tj9ioIfAPPDmUG8O6nMD_n0n2rI0vKrDHE05zZaRy1TP7cDgIZq3tURzECsLCAa7P_8B5Dw16ORaacDVxeZHsoXAjN2WDr0RJ7X_Cyu71AfPHicGAKmbbdXW_vGqwgf2fXs7PEHT_-9G82amwtdWQOxg9ObDnkIGzST4UCJOwlqLpAr4nayZgRXDLNZLbM-NDavdY6iaL9DHM6dSyt2bcJve_IPNfSYpIgI-xyB3aht4ONSd-fHzfvpF_joU_1SqFEmZ-8zBsPsnR0a4kvY2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
گلزنی احمدنور در دیدار امشب کلبا مقابل خورفکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140279" target="_blank">📅 20:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140278">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2XVGQpkzG9W9_fLHVVeT8Clz3Jgqmhpj12Zc2cypmweC2eQYhKoQ79B7DIQn-Wj-l_gIKuZsrGQvPmrj-UGi6qmeHOUJ_HF3owBQuSplTOx29yqfUphdVUWPPaHpy0wGunyr6Uub-cyEyuLjySQ2sZ47w1jwyZfzBvghYn-qcLDgcJnLfoEgCoOpkNZodu3I1gEqxaOLIhVr-F8-x5iE7-qEjCNw_xFXh9jLVBtCMOJdAjIP2COnCmxdXeldBOEk8M2UbA-qbhrApAgvwu7xhltGhUiAuXaHnE3yuCmlzo3rQld2CO5O3UmzMoGqqOQsR5PmG-YpcIc8b8_DRVkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
با درخواست علیرضا بیرانوند مبنی بر انجام معاینات پزشکی موافقت شده و او برای بررسی‌های بیشتر به بیمارستان معرفی شده است. این اقدام باعث تعویق موقت زمان اعزام او (که قرار بود اول مهر باشد) شده است. اکنون مشخص نیست که اگر او موفق به اخذ تاییدیه وضعیت پزشکی…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140278" target="_blank">📅 17:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140277">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140277" target="_blank">📅 17:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140276">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140276" target="_blank">📅 17:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140275">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140275" target="_blank">📅 17:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140274">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
پیام صادقیان خطاب به امیرحسین محمودی:
✅
بهش گفتم سرت تو فوتبال باشه و فقط به تمرین فکر کن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140274" target="_blank">📅 17:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140273">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
بیرانوند قصد دارد پیش از رفتن به فجر سپاسی، قراردادش را با تراکتور فسخ کند تا مشکلی بابت چند ماه باقی‌مانده قراردادش نداشته باشد. با توجه به بسته شدن پنجره نقل‌وانتقالات لیگ برتر، بیرانوند از ابتدای نیم فصل دوم می‌تواند برای فجر سپاسی شیراز به میدان برود.…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140273" target="_blank">📅 17:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140272">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7FRPl7gRizlsSHq5MoaTEPIDXm2DqolKDQjAMukh4XF4OcV-l_tSd5yAwqEGvIumLd4EWck0pY2BsVEuL7TjuyZ0dxwXDWkVN_NvIUgbqCPT-zO-ekzXfR299H4BRS_uoU-Hn7Rj4GToao2DXW6o5zeMxdRCG9a6_HwkFXi6V_eq14X6e9yzuXSO5gCuZez1pipyvKOITdxT_KjSTw0F4ghIry6AQkhGmpsc3pHz1bjjFpHRYs2PUwor2-Tb3PewGRXoMI12Z15kRqymX0u26Opo-8LUvaQI5AocVulyI_Q6WkA93cP13qnPMZ7Ilqx5HtRHM7Riun5qJMIkfp_IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
ROMA -
🔵
INTER
⏰
Tonight 19:30
🏟
Stadio Olimpico
🔵
رم در خانه با تکیه بر مالکیت و فشار هواداران، دنبال کنترل ریتم بازی است؛ اما اینتر برای تغییر جریان مسابقه فقط به مالکیت نیاز ندارد. نبرد اصلی در میانه میدان و انتقال‌های سریع رقم می‌خورد؛ جایی که کوچک‌ترین اشتباه می‌تواند ورق را برگرداند. یک بازی نزدیک و تاکتیکی که احتمالاً تا لحظات پایانی، نتیجه‌اش باز بماند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140272" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140271">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc94830254.mp4?token=k-oerIb_XKV08gII9iwR-jNxRPbVGPrjP_N4OpfewxqPMKDOYEr2hfeZCJMwhDpCdZmurz-1QicP-LUOs_nBY2mA4fWy0KyVstzZ2olWbaSkMKa7DpSMO5OGRr-mPlV_ukb7SW-Mdrayy73arBLQxkMr0dO8YhiMRtjf-01TNYjBUxVOP2cG7vDFXFuO3lsGpsQLpORJOjYPQWPQTDoOTDyjj-pyMmivJa5mTZzTQCgbU43uVPwUWOZ78fr2iZJoOW6TupIrwTDEtHBHnWYtOKnSU5aVqsIqd987ibwfabi9yFdJX4otDLeTvL2Vv57I-1Zr3VTPPdg1z86OD3NXYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc94830254.mp4?token=k-oerIb_XKV08gII9iwR-jNxRPbVGPrjP_N4OpfewxqPMKDOYEr2hfeZCJMwhDpCdZmurz-1QicP-LUOs_nBY2mA4fWy0KyVstzZ2olWbaSkMKa7DpSMO5OGRr-mPlV_ukb7SW-Mdrayy73arBLQxkMr0dO8YhiMRtjf-01TNYjBUxVOP2cG7vDFXFuO3lsGpsQLpORJOjYPQWPQTDoOTDyjj-pyMmivJa5mTZzTQCgbU43uVPwUWOZ78fr2iZJoOW6TupIrwTDEtHBHnWYtOKnSU5aVqsIqd987ibwfabi9yFdJX4otDLeTvL2Vv57I-1Zr3VTPPdg1z86OD3NXYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حمید مطهری سرمربی فولاد: پرسپولیس تا الان نتایج خوبی گرفته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140271" target="_blank">📅 16:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140270">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140270" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140269">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
💢
💢
✔️
✔️
مدیران باشگاه پرسپولیس هفته گذشته‌ مذاکرات برای تمدید قرارداد پنج ستاره آغاز کردند
❌
پیام نیازمند
❌
محمدحسین کنعانی زادگان
❌
تیوی بیفوما
❌
اوستن اورنوف
❌
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140269" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140268">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
قراره در فاصله تعطیلی لیگ، برنامه آماده‌سازی پرسپولیس با برگزاری ۲ یا ۳ بازی دوستانه دنبال بشه تا سرخپوشان از شرایط مسابقه دور نشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140268" target="_blank">📅 16:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npfceMzCOrfPr--5wi-q0LIvyGFxly5KYmOWhmaNQWSVU2Vw84v0atFFqjBl3lg3JjDMTErHpqS9ZX3XntIJpQaUPh-29fs7YSn5rYcAfHM_wwF6P7IE1sX6j6VjhQoBMaxVzxkBPmFBd1f0KiNSk0Iw4AUtBiwa6PZWS9CcPkY1UHzwbOWDibTYLyyso2Pu0CWrtUraCCGv3qsH3rhCu7eKR0Z-oPRZVN1OvbfuGRK5laDM2U7EC6hfbdpbcG7dSq8Xk9myqW4uZMjSjZF2xPQZzoeadeDwnUuQmokn8Ae9no9dYRoQn_9Tmj6Pm59yqxe-GpYAd_BDmOuXf8Nyng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تیتر روزنامه‌ گل درخصوص دعوت شجاع خلیل‌زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140267" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140266" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140265">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
فرهیختگان:
❌
مدیران پرسپولیس معتقدند که مدرک کافی برای پیگیری شکایت یاسر آسانی در CAS را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140265" target="_blank">📅 14:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140264">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140264" target="_blank">📅 13:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140263">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
❌
🗞
فوتبال۳۶۰:  بشار برای برگشتن به پرسپولیس پالس مثبت نشون داده.تارتار تأیید بده برگشتش قطعیه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140263" target="_blank">📅 13:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140262">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
آغاز تمرینات پرسپولیس از یکشنبه در تهران
✔️
✔️
تمرینات پرسپولیس پس از چند روز تعطیلی از روز یکشنبه ۲۹ شهریور در تهران از سر گرفته خواهد شد.
✔️
✔️
برخلاف برخی شایعات درباره احتمال برگزاری اردوی خارج از تهران، مهدی تارتار در شرایط فعلی برنامه‌ای برای برپایی…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140262" target="_blank">📅 13:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140261">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052167cdae.mp4?token=MtHc-lmSXwwEcnla-xDnuEPAnw9Gkev3uLdcgT05GUZqFp52VmAVeIyZkhRGhp3QM5FnwQQPOsk0D7_P7D8OzsasmaE6UKKBzwbJZewb85WUVEQz7RZb6l03SMmUDetL1gU4mB4KFXBHesE35GsKf3k4si-4U1obcYliUfAOBU8QFWLFYeJpd7detTEc4dCmKD68PPSOl7fskYThZHb2Jszb3xvn9v_gsrDBrgd3g1vX0FLAbzlFsbo6IalZSs6aBC2N7RTlNG35Xoro2ObXkdPWCdmEH2xx3ritrJFe8uf7XCR3tbWfE8Xix1f5PexXuz0X3lz5G6y0F4jP5z6rqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052167cdae.mp4?token=MtHc-lmSXwwEcnla-xDnuEPAnw9Gkev3uLdcgT05GUZqFp52VmAVeIyZkhRGhp3QM5FnwQQPOsk0D7_P7D8OzsasmaE6UKKBzwbJZewb85WUVEQz7RZb6l03SMmUDetL1gU4mB4KFXBHesE35GsKf3k4si-4U1obcYliUfAOBU8QFWLFYeJpd7detTEc4dCmKD68PPSOl7fskYThZHb2Jszb3xvn9v_gsrDBrgd3g1vX0FLAbzlFsbo6IalZSs6aBC2N7RTlNG35Xoro2ObXkdPWCdmEH2xx3ritrJFe8uf7XCR3tbWfE8Xix1f5PexXuz0X3lz5G6y0F4jP5z6rqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
آغاز مراسم افتتاحیه بازی‌های آسیایی ۲۰۲۶ در ناگویا
❌
مراسم افتتاحیه بیستمین دوره بازی‌های آسیایی در ورزشگاه میزوهو شهر ناگویا ژاپن آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140261" target="_blank">📅 13:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140260">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140260" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140259">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnrnaAE6tRnQ4HqxxqINq-4HqzajKLQ35zXhWBJhUVvWRtTqx_KrMwgiZxBshw2xjDUpRHYJvm69N_PzcOApxZ-d-zDCXkORxVk3II6sNu0Rt1Pdc-9yi90vGmsh71il-_ToYV1rRAn36QwnfDSPfQY5Wm6n0sHSe20mDsKwFhzl4QFdAKYNqklWH8H1p8PBVxFOb4qrJvs_xxArf-ListjaQMNX5uJaE4c3EABpKeR2sEZMq9lxZ0bbLO2RrccAKyhi6csMzWljXNlAFYMGtkqUbD8F3RiuDjHEZGxCjjY89YM49ZGb-53y48s4vdiHoIG83JBnKDjNJSNIccIBgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140259" target="_blank">📅 11:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140258">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140258" target="_blank">📅 10:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140257">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140257" target="_blank">📅 10:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140256">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN7LpelNX8l26L66uWl27VA5Ax1AmeSfpDJf1OetomBavBFG_GlUXmvGQ-N0CRwXvvDy1wRcM6GmGES6qPhDuOCVF3d9UpuiacrMoGJy8jOhz9RqmO_lS1Rryxzw6hbMf577sJNAA1NZjuBw_CAnCv8Z6flZZUC8r7P7fvks7H-hL96blBEdgvmATL-MfZnQZzsjhRepgwjCm9yjX2OWr6RZSGXIkNlctBqNp1gZRSawDnsUxtae0OUcMx8ibXJpWu5wVQZa1gf2S9bt4ZBv2CzaOvLITJijKqU3g_UaW8obeA8Vw54IPs4zFJZ99sGLnN1ufsj4-TtuXfoVbLo18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140256" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140255">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3I9nPgjpV4snQEjBZRKySXBbj7RJ2LrdQUt8JQ6EOTgAQ8EVjROhH4lQoaqUxxfI_UXQKGKOjW_f3PGQksIZRn4JqBLLZ6nyxsY3TPKTTCY2avl3cxZjPKPnupuAtfE6P_AJRXz9AOK2hmI_AMFl9I_yThJyVssrNENaOJfDxTopd-nU1yf8yAJu8yEkDwLvdE3ADbFrzVzg_HnazaruDG2wAT_KANmWUjsLA2uC4vHxXJgOQnVTPr1I_HoAH50Ce8osrkZ5Jzg17sYvUrkoNUPxI1Li1aCfPR6qQMR15a-n04wY38vIC7VDYfR3GFzKq3oVzJF48Pk9ftjosv2R1YM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3I9nPgjpV4snQEjBZRKySXBbj7RJ2LrdQUt8JQ6EOTgAQ8EVjROhH4lQoaqUxxfI_UXQKGKOjW_f3PGQksIZRn4JqBLLZ6nyxsY3TPKTTCY2avl3cxZjPKPnupuAtfE6P_AJRXz9AOK2hmI_AMFl9I_yThJyVssrNENaOJfDxTopd-nU1yf8yAJu8yEkDwLvdE3ADbFrzVzg_HnazaruDG2wAT_KANmWUjsLA2uC4vHxXJgOQnVTPr1I_HoAH50Ce8osrkZ5Jzg17sYvUrkoNUPxI1Li1aCfPR6qQMR15a-n04wY38vIC7VDYfR3GFzKq3oVzJF48Pk9ftjosv2R1YM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140255" target="_blank">📅 01:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140254">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
میلاد محمدی که تو تیم جدیدش حسابی ریده گفته میخوام برگردم پرسپولیس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140254" target="_blank">📅 00:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140253">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
❌
❌
پست خداحافظی میلاد محمدی از پرسپولیس
✔️
✔️
امروز با قلبی پر از احساس، از خانواده‌ای خداحافظی می‌کنم که همیشه بخشی از وجودم خواهد ماند. از هم‌ تیمی‌های عزیزم بابت تمام لحظه‌های فراموش‌نشدنی، و از هواداران پرشوری که در هر شرایطی کنارم بودند، از صمیم قلب سپاسگزارم.تا…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140253" target="_blank">📅 00:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140252">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140252" target="_blank">📅 00:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140251">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⭕️
⭕️
پرسپولیس مهدی تارتار در این فصل ۴ برد ، یک مساوی و یک باخت داشته ؛ ۱۲ گل زده و ۳ گل دریافت کرده امید گل تیم تارتار ۱۲/۲۷ بوده که با این امید گل موفق شدیم ۱۲ گل بزنیم و امید گل مواجه شده ما ۳/۲۴ بوده و از ۳ گلی که دریافت کردیم دو گل روی اشتباهات فردی بوده…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140251" target="_blank">📅 00:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140250">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=pHKTDE5g3fmiEOGgelUiubuAmOcyhfQI2cX4iGgZ6pw9XHby219UnB3rXsA9bsSIYvbWmX1Tfck0Sg0tZejXgtZr_eQCIlN5H7ksldlx9yRpbE5pqmKW_4HwiOn4sZk0OdlMO_e8LuWc93NnNbCQTTdyD9lIPL6LKNsB_8oES0gf880edEMsYQEya0fS_eCaA4_5n4X6ZTiG2Id1JejCOHQ5rN5lCqMakOTbJmZu_KFSP79CRuyQGFbP7aReqSmGU7M33W9hIwS5-VHuaLglvPVMTVcpIsnjUvJMfT7yO8pr_eAFg7fhL1MDW44BX4tlvZ6YblfW43VZlId8bqVF9ECiVKs52bRE17_EO8KgcELZsoMtktDoeFjXY-FS3MO18nxmCKauMsxQgb3meE3tWfJ7s5lFr79tnh11rEHlHK9DsShUNfDthy19cJLQyjlsuigMcrflWg7h2iGh0kkcKZcVLKPF019QjeRPr4ac3cUo3tEA88AHGVWLSXdPRoY-DGsRW2srNSA0Ed-K4ZHTvEgBUm-8uaXT-36nZ5JWA6NYBW0GRJpXEao5KMzYjFGTqBZ5biKDhzlR_4B39iQ4Zm7Z8czar7tA6bz3rmhI_pegBoaK6WjaM0r2tjghiO_R2S8vvz-uXEnYXVKsjXcxUQO1gP4c7ZwcaCpmIZ-NYs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=pHKTDE5g3fmiEOGgelUiubuAmOcyhfQI2cX4iGgZ6pw9XHby219UnB3rXsA9bsSIYvbWmX1Tfck0Sg0tZejXgtZr_eQCIlN5H7ksldlx9yRpbE5pqmKW_4HwiOn4sZk0OdlMO_e8LuWc93NnNbCQTTdyD9lIPL6LKNsB_8oES0gf880edEMsYQEya0fS_eCaA4_5n4X6ZTiG2Id1JejCOHQ5rN5lCqMakOTbJmZu_KFSP79CRuyQGFbP7aReqSmGU7M33W9hIwS5-VHuaLglvPVMTVcpIsnjUvJMfT7yO8pr_eAFg7fhL1MDW44BX4tlvZ6YblfW43VZlId8bqVF9ECiVKs52bRE17_EO8KgcELZsoMtktDoeFjXY-FS3MO18nxmCKauMsxQgb3meE3tWfJ7s5lFr79tnh11rEHlHK9DsShUNfDthy19cJLQyjlsuigMcrflWg7h2iGh0kkcKZcVLKPF019QjeRPr4ac3cUo3tEA88AHGVWLSXdPRoY-DGsRW2srNSA0Ed-K4ZHTvEgBUm-8uaXT-36nZ5JWA6NYBW0GRJpXEao5KMzYjFGTqBZ5biKDhzlR_4B39iQ4Zm7Z8czar7tA6bz3rmhI_pegBoaK6WjaM0r2tjghiO_R2S8vvz-uXEnYXVKsjXcxUQO1gP4c7ZwcaCpmIZ-NYs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشته کریمی، ستاره‌ی سال‌های اخیرِ فوتسال ایران، امروز اولین بازی خودشو در قامت فوتبالیست، برای تیم فوتبال پرسپولیس انجام داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140250" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140249">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140249" target="_blank">📅 23:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140248">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140248" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140247">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdwc-eOalCofXZL6QxU_n6WQtvkyZKvjtslX4dLPut_qgCbqAP7EZ-_DoTRkaDU4Ku3ib1NrdROC2MDyMop6Asp_p41YImyyDkPN5pOLwmU6iW1Xkx9EOiWqvW4wyFBBswiElZqsr4mjk7L5hfCycDkRNW57eNms1DtsJlTJYiQexlQcD3p7HrQVQ0iT_c7j9WlgJTdKMjd0pIInelHzJA4plbEnH6qF3LjnEAmLdrkcA72GOHAU-3F9gWIneHUn_04yKhtuyBFD_TS7tmGOWtSTGJopIwyhVrjGr8jSMjPHnt6Y_E2DN85JxDuA8ggVN_ik_esufFMJevzCK5C9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
اینم تو یه دنیای دیگه‌ست
😂
⚡️
آخه اسکول، تو این گرما این چه لباسیه؟!
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140247" target="_blank">📅 23:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140246">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
❌
اوستون اورونوف به مدیر برنامه ش گفته آینده ی فوتبالیش رو میخاد در پرسپولیس بمونه و با مدیران پرسپولیس برای تمدید قرارداد سازش کنه تا قراردادش مجددا تمدید بکنه
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140246" target="_blank">📅 23:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140245">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140245" target="_blank">📅 21:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140244">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140244" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140243">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140243" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140242">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140242" target="_blank">📅 21:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140241">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKm-Pz102cz1zIqdyiz8KWFgekU0n2s1U6Zx79vC7XTIRhKa3oRFN62oHHeTEw0zUtRovK4tD01WK5wd0oDqAN2mNtXqshFBU0jQ9o0dIMyd1qypApvwGk2yI38RNf9j0mmTT5-5_pJ8DdgrByXVN3rXwrtiCR6LPijVfsMzwWrOn1rMQiigt5IFZz1bZPO_d_vQ3qKa6-HPITaMTSDOhI0SWH54L0iOdYwiMLTqa1A1GpHxU7gr3N__bOVR70LC4GApAX5QpsKQr5tHHz5k9LtPjj2Xu3g4_S9FBb4PG_rRQuNJ8LUQdhb009CarAyhvpUfuRoaf_a5f6WIUyS5kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی بانوان‌ پرسپولیس در فصل جدید
♥️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140241" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140240">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLkAQ7OcPSao6uAaNeZVSmixXTf_ajpnqO2WDXVF6JBVY4lMUMcSoyvcBHJBS6YjjjoA3fKs9Th8f0IoM19k6BbgC761wA4jzcJpCXcXxGE0fmu_ECnwB5h7QCBPyTZRLimolrcnrQEOPw-Sn1xaZVm7fb_gQyw_D5CwC2m_xQRYvKxStV4XOdtcFEv-Dr_35hXEuqRmreIeGoLj-3sVzPfdjiQRoVQMOU-zfRXJcmpg08jbF6pYOe_vLwARpCKFJaKwH7NO1_SonGBXA9rG0poVkA2pVfZwVPX8UOvn_iKZi88Dz8jSTwQ6t6y68BRXsMgEXNwSo7jw5l_W8U7jrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Brentford -
🔵
Chelsea
⏰
Tonight 22:30
🏟
Gtech Community
🟣
برنتفورد مقابل چلسی؛ جدالی که برنتفورد با فشار و بازی مستقیم می‌تواند برای آبی‌ها دردسرساز شود. چلسی از نظر کیفیت فردی دست بالاتر را دارد، اما در بازی‌های خارج از خانه باید مقابل انتقال‌های سریع برنتفورد مراقب باشد. با توجه به سبک دو تیم، انتظار دیداری نزدیک و موقعیت‌ساز از هر دو طرف می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140240" target="_blank">📅 20:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140239">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140239" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140238">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=D4sdSrVPrE4qJXo7kv1EzmB7khJDqrRivhmMo_tGWiU_dWtuXC_vBOXfIeyeEoE-wg_ceSmofTgD2FX7C8I7FQyqijTSaQagObw6SUGqXngO93ragFK6ChHLi7UZIZ_Z2msvYNuBYC-2uJqJiyhS3AcBUZvGa0oBr_FHNh194hQ_V2ZH8ei79Ya2Zesb__ixThg5TJJdOCCb7jJBw9VNKBfNlF0NG_OxhzKT2_xiXS835RakjDa_5vGMP9Gt4vhAxilK3tsCR8nndAXTuczamRuqXrUhfZqqjDmtN6c6S8hd4cla7W7V_4at1VluZLU0r9cpYIyK6ypsJnK85cs08w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=D4sdSrVPrE4qJXo7kv1EzmB7khJDqrRivhmMo_tGWiU_dWtuXC_vBOXfIeyeEoE-wg_ceSmofTgD2FX7C8I7FQyqijTSaQagObw6SUGqXngO93ragFK6ChHLi7UZIZ_Z2msvYNuBYC-2uJqJiyhS3AcBUZvGa0oBr_FHNh194hQ_V2ZH8ei79Ya2Zesb__ixThg5TJJdOCCb7jJBw9VNKBfNlF0NG_OxhzKT2_xiXS835RakjDa_5vGMP9Gt4vhAxilK3tsCR8nndAXTuczamRuqXrUhfZqqjDmtN6c6S8hd4cla7W7V_4at1VluZLU0r9cpYIyK6ypsJnK85cs08w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امید عالیشاه
؛ به جای عزیزانی که اخلاق را در ورزش رعایت نکردند، دچار شرم نیابتی شدم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140238" target="_blank">📅 17:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140237">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140237" target="_blank">📅 17:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140236">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLhxIULlpxI92lizooXuEYC97uvjeHQOTQl9HmrOj5xshZQZO-wXIz3bG9HnRxlKUDB2nlL0ZrMGBhBuGeum_f4msT1k6sZoa7ayo6-omLrF2wz9bR4d7r4Gq20heoORkuzBsQ2Ahv6grbIVIuDkAEl7N-lPFCtCFn1ufFM_f-jXEjP_WY5qd2ZfTVMtYdqruzYrqCSEkkwBchUl8s7TQvFStQ2E6XXooj_SNHXws3oiu8-wLa2YEU3KPiMHdhtEhgt5h5wLC2VfDvykb5x6DPOld8DbQ2ySWHXI-BhtB058kBsDGkklnOYdVK1KUxHMiBrx4N6KldiNDMe_Drpi1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
یکسال پیش در چنین شبی رقم خورد
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140236" target="_blank">📅 15:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140235">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=lY5DLV_6SjKUCN6yJ-ZIiA_IH2DcTtNR6CfBeJ1l6X6kojdUEpVCv2VEWwk2V7yNasAsKSnfi0Cjfc7DOCvVc9OiFckDWGsTkEwwwCY-zVG3DsRz3uPdpGkECu7NC4POTJOEmEghp08mbvBleJ0pxO0IVQuYIRpbY8dFNXNDjd27hfe8g_5rfofq3iKUrWP_vFJ30LC0_5HyP_ad5heJlFZRbD5nucFiCGsTUJw4xgg_c9GX0SaSsP-C7BzLKHFOJF57XHBiVmf36y-rlciJIgIFE2AtY1TjZrv-8ZFf81yPo3YYvQ80nDAo5DgBA2gP8BhcbgKR8c_sM7fvZOGc8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=lY5DLV_6SjKUCN6yJ-ZIiA_IH2DcTtNR6CfBeJ1l6X6kojdUEpVCv2VEWwk2V7yNasAsKSnfi0Cjfc7DOCvVc9OiFckDWGsTkEwwwCY-zVG3DsRz3uPdpGkECu7NC4POTJOEmEghp08mbvBleJ0pxO0IVQuYIRpbY8dFNXNDjd27hfe8g_5rfofq3iKUrWP_vFJ30LC0_5HyP_ad5heJlFZRbD5nucFiCGsTUJw4xgg_c9GX0SaSsP-C7BzLKHFOJF57XHBiVmf36y-rlciJIgIFE2AtY1TjZrv-8ZFf81yPo3YYvQ80nDAo5DgBA2gP8BhcbgKR8c_sM7fvZOGc8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل تیکدری تو بازی دوستانه مقابل شهید قندی یزد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140235" target="_blank">📅 15:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140234">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=QLa6IJk0Xjydg_fPFuRhsI4iKs0rHKQwpoCNJXpFdjOviuTwve4TGlsxeKuDrl7SXFrPbdUhgKLOtS77igjRQxwtDPS_uOd1_439YF8p_XsYkfTR2oAji_jpJmJ19fVvNDxvz8kGhFvqNin6Cymg1edWJrolwUBFl4PZZ9U3Qo0y71bJPqMo7k36rR2NVdjZjQK6j2lP2Gln1WLbozS6yH9ly-CqXq2dyjoy7UiSnSgthKeYlJW5kOHiTt5OVXfIoYrtdVyISW9y4SnF517RaGV5aakpZThNVE-rBdJnHTpq0aD6XojSDPsLcbl8x2gCCY0sNg8ySc-zLD61F8V5xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=QLa6IJk0Xjydg_fPFuRhsI4iKs0rHKQwpoCNJXpFdjOviuTwve4TGlsxeKuDrl7SXFrPbdUhgKLOtS77igjRQxwtDPS_uOd1_439YF8p_XsYkfTR2oAji_jpJmJ19fVvNDxvz8kGhFvqNin6Cymg1edWJrolwUBFl4PZZ9U3Qo0y71bJPqMo7k36rR2NVdjZjQK6j2lP2Gln1WLbozS6yH9ly-CqXq2dyjoy7UiSnSgthKeYlJW5kOHiTt5OVXfIoYrtdVyISW9y4SnF517RaGV5aakpZThNVE-rBdJnHTpq0aD6XojSDPsLcbl8x2gCCY0sNg8ySc-zLD61F8V5xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی: اونایی که به من حمله میکنن مشکلشون من نیستم بلکه تیم ملی عزیزمونه، اونایی که حمله میکنن یه مشت وطن فروش خائن هستن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140234" target="_blank">📅 14:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140233">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
❌
محمد خدابنده لو درحالی به تیم ملی دعوت نشد که در 6 هفته ابتدایی لیگ دوبار در ترکیب منتخب هفته قرار گرفت
✔️
✔️
همچنین این بازیکن با نمره متوسط 7.37 یازدهمین بازیکن برتر لیگ از این نظر بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140233" target="_blank">📅 14:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140232">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌬
پایان بازی  نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140232" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140231">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_zHAnupn1uOgyKu49nNyCOYjFWgy870N-V-SuVx92rU6KvTfHCj1sPLhQNfcg2Cc7RKE3mUAbhRcIhog7WNFmZ7ggJgBsJ6qNKvbjLNPqdvjb-qA4mjZTZYMsqDQAXYF0cR53YLtFCUukP-9LRBjHMML4xSes_s17YTy1Q7z124VoTHWTfZS1imlYn6kdocJDPRScZ41Xy3G-5Ip35TVx_dttH5Ur1eWmMk46iIs3fYOz0re_Vu-lotzyjnibP-pJyT_I0nvCejpwyeyCU8QVcNMwgtAscf3E_9QUjEzXgFguTI5jRJSCKX8iqVbK3yAqm-RWQtaKodFxoOokGlpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140231" target="_blank">📅 13:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140230">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140230" target="_blank">📅 13:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140229">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
❌
#فرهیختگان؛ مذاکرات با ۵ بازیکن برای تمدید قرارداد آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140229" target="_blank">📅 13:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140228">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140228" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140227">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
پشت پرده عدم دعوت کاپیتان‌های پرسپوليس
👀
غیبت کنعانی و علیپور در جمع نفرات اعلام شده لیست تیم ملی سوال‌برانگیز شد اما ظاهرا کنعانی از ناحیه مینیسک و علیپور از ناحیه زانو دچار آسیب شدند و حداقل دو هفته دیگر به تمرینات پرفشار خواهند رسید.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140227" target="_blank">📅 13:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140226">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjpcEIe1L9yLk0TSJyVdHRl4wKOC9aQpx-TIseXInhWu6o_UKRDiI4d3AHAxOpFToXvIkQYrZZ1NQUS3t6O-sWvX4qBkygVJ_4R6mFgeMu6NVS5GEfWiKc94_WM5rsG2jqlP5D945M5oAjK7g0usK2dniR0QzRUAwNUlgtt2BFn1IRyjgyiPuRV3PGof3e9riAKt6VLQag0CJjU-bP5gcLhE12UxaD0p5M1QrZWSNjgr-2B1IM-NqFDLWGh0nBqh0f4q_1nCuztw6f2mOStWQ9J39qN87mjrt61D703albWxdsTNTz14pyOFeT9rlBudC_y3mqir-khVL2gu62tSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن در خانه؛ جایی برای لغزش مقابل یونیون نیست!
[
بایرن‌مونیخ
🔴
🆚
🔴
یونیون‌برلین
]
⚽️
بایرن‌مونیخ با مالکیت و فشار بالا، احتمالاً از همان ابتدا بازی را در زمین یونیون دنبال می‌کند. یونیون برای دوام آوردن، روی فشردگی دفاعی و ضدحملات حساب خواهد کرد و فضای کمی به بایرن می‌دهد. با این حال، کیفیت هجومی بایرن می‌تواند در طول بازی اختلاف را رقم بزند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140226" target="_blank">📅 12:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140225">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
❌
🗞
فوتبال۳۶۰:  بشار برای برگشتن به پرسپولیس پالس مثبت نشون داده.تارتار تأیید بده برگشتش قطعیه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140225" target="_blank">📅 12:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140224">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
شجاع خلیل‌زاده، احسان حاج‌صفی چرا باید به تیم ملی دعوت شوند نسل این ها گذشته است
‼️
🔴
مهدی لیموچی افت کرده و میلاد سورگی که به نام جوان گرایی به تیم ملی دعوت شدند عملکردشان در حد فیکس بازی کردن در تیمشان نیست
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140224" target="_blank">📅 12:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140223">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140223" target="_blank">📅 11:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140222">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
زگوزی: تراکتور بسیار بسیار پرطرفدار است و پرطرفدارترین تیم ایران است، ما فقط در ایران هوادار نداریم و خارج از کشور عاشقان به تراکتوری زیاد وجود داره
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140222" target="_blank">📅 11:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140221">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
✅
زگوزی: تراکتور بسیار بسیار پرطرفدار است و پرطرفدارترین تیم ایران است، ما فقط در ایران هوادار نداریم و خارج از کشور عاشقان به تراکتوری زیاد وجود داره
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140221" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140220">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
زنوزی به خداداد عزیزی قول داده که با توجه به روابطی که او دارد، محرومیتی برایش در کار نخواهد بود و از این جهت خیالش راحت باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140220" target="_blank">📅 11:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140219">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etemwbm_n2Jg-eVUfSmHZMCfqgvUzvscoMIqLPgjiuuVcb0bI9yq9qZTARvQAAgAkhPz45ThM93hZLH3jnxYG7aw7MUIggR8EvOJqhiCahaN7At0MDPyEtNLuHIrPbEvvwU8aYwwVPrndcTO2keXRgf0g7WfDkRP-AlgwM1kCT0cw4yy0ARLof13CYkKxBx5yjvqQku4Uqo9eWGqAq9FwNMvAixQwlrNeA7NKLnrwy0QTq2ckozr7L7kZWEV6t3nYf6jT2-CXEGPWU24zL5EfyL1i0NFBFicIlYT9pHGOlqS_IPUYuuTqcqKBuJcKZenQccJtdqZye_hOTSnjKwZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140219" target="_blank">📅 10:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140218">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🔹
ماریو توکیچ دستیار سابق برانکو به پرسپولیس پیشنهاد شده و درصورت تأیید تارتار به کادرفنی تیم اضافه میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140218" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140217">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140217" target="_blank">📅 10:48 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
