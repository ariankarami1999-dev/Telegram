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
<img src="https://cdn4.telesco.pe/file/p55QLV82DLAinGhqLUeLVvV6oXyjZpjkLwteuGRTGmT3p5BKExY4JDulxVB5JwMjTB6291_r3kUgsq51ryBecyz6gtGhjAa-PuNUGUCzLyZIb1bOUyXidKCJSCyrxYTxttmLNLtvqnUl7wJOBAAnQ8MnEAi7jINfYD29COx4Af6BB5DEJAh2CJ8XSfdu6C9_IAjgDRZ1JYpOCGlmGkgrW1hCMAMErjKTNInhxa02UQYFgcoNSmSYKk2R7oE0KSHhauKDvho9d4Fi0qIdKUeNX19AkD0bJ2W4pPRgv8lDXc3MTni9G0Z8bm5UyCWo28SPfYxm0ERT8W9wyuWzGsR6FQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 147K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 20:18:30</div>
<hr>

<div class="tg-post" id="msg-75102">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خارکسده یواش تر</div>
<div class="tg-footer">👁️ 36 · <a href="https://t.me/funhiphop/75102" target="_blank">📅 20:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75101">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پشمامممممممممممممم</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/75101" target="_blank">📅 20:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75100">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یجوری خونه لرزید خایه کردم</div>
<div class="tg-footer">👁️ 36 · <a href="https://t.me/funhiphop/75100" target="_blank">📅 20:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75099">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c616c935d.mp4?token=g9BRAbvy9HD6fjzdutxEM4wj_S0JW2EuTs10oYFuc9Y7Az5sjiBmH3cgyZkSivgK7lTVMAIbbp8ATWGKTqiaoM7Y-bE366M3smeYk8On2zn1OZmL9gRzhcTwSlKdzs8RoKWab8VClC9S9D4JMujW2NfOnerjUMxfVOloSSy-Tbq-wZxyJtDC7w0d7EfP7a547h_6yj9qka-cAPUg3mlOKcs6UNnGbBwFbPvDw5dFLCqAw67lEqWob6JBxV2m3kiFJh-j5gIP6g9w8TLra8RWTyzqE-NNBeSb2XZEf52gQ0159X4J5VMTeDDKr9ZoISNAwzh4XB3fPHpXT9q6CF4z1rKEy5FUw5hgdlKJ-dCdgrCgaUoMkEgeexywuBOFDmvwsRUoCE8mq5wgZ83EdgpELKn2d_feOkD8I4Q4XZSjro_wLKTMrSWiYLxlMNYr3NwGIUQStrZydcxicnLH15fgQpT-4uWou2eRsQmP79NfPei_znWPoQNIeRkoTPO9DYcR2JcT6E_vYJVZGcFQxNDMo1UQ_p6oB-Ha-nMOO_wVisMkzRGF8rLJXUpNOwW-Ym-meXcX-d7qlgv5GkiNt7esbGdDJGf6jW5dl4Rk2ErwLylIuISM9kJkhmDWf2H-D1vbKlV-PkLaB907lDPFPZRadyo2adBccxFvBvqujwPr3q8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c616c935d.mp4?token=g9BRAbvy9HD6fjzdutxEM4wj_S0JW2EuTs10oYFuc9Y7Az5sjiBmH3cgyZkSivgK7lTVMAIbbp8ATWGKTqiaoM7Y-bE366M3smeYk8On2zn1OZmL9gRzhcTwSlKdzs8RoKWab8VClC9S9D4JMujW2NfOnerjUMxfVOloSSy-Tbq-wZxyJtDC7w0d7EfP7a547h_6yj9qka-cAPUg3mlOKcs6UNnGbBwFbPvDw5dFLCqAw67lEqWob6JBxV2m3kiFJh-j5gIP6g9w8TLra8RWTyzqE-NNBeSb2XZEf52gQ0159X4J5VMTeDDKr9ZoISNAwzh4XB3fPHpXT9q6CF4z1rKEy5FUw5hgdlKJ-dCdgrCgaUoMkEgeexywuBOFDmvwsRUoCE8mq5wgZ83EdgpELKn2d_feOkD8I4Q4XZSjro_wLKTMrSWiYLxlMNYr3NwGIUQStrZydcxicnLH15fgQpT-4uWou2eRsQmP79NfPei_znWPoQNIeRkoTPO9DYcR2JcT6E_vYJVZGcFQxNDMo1UQ_p6oB-Ha-nMOO_wVisMkzRGF8rLJXUpNOwW-Ym-meXcX-d7qlgv5GkiNt7esbGdDJGf6jW5dl4Rk2ErwLylIuISM9kJkhmDWf2H-D1vbKlV-PkLaB907lDPFPZRadyo2adBccxFvBvqujwPr3q8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو هواپیمابر USS Gerald R. Ford پس از 326 روز در دریا به نورفولک بازگشت که طولانی ترین ناو هواپیمابر از زمان جنگ ویتنام است.
در ژوئن 2025 برای یک چرخش معمولی مدیترانه حرکت کرد و مدام گسترش یافت: ونزوئلا، دریای سرخ و در نهایت عملیات ایران.</div>
<div class="tg-footer">👁️ 379 · <a href="https://t.me/funhiphop/75099" target="_blank">📅 20:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75098">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!   دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 149 هزار تومان!
😈
( فقط 300 گیگابایت موجوده! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin…</div>
<div class="tg-footer">👁️ 905 · <a href="https://t.me/funhiphop/75098" target="_blank">📅 20:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75097">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تلگراف
بر اساس گزارش روزنامه تلگراف، برخی مقامات و چهره‌های نزدیک به
دولت
ترامپ
از امارات متحده عربی خواسته‌اند نقش مستقیم‌تری در درگیری با ایران ایفا کند
؛
حتی تا حد تصرف یکی از جزایر ایران در خلیج فارس
.
یک مقام ارشد سابق امنیتی دولت ترامپ گفته برخی افراد نزدیک به ترامپ پیشنهاد داده‌اند امارات جزیره لاوان را تصرف کند؛
جزیره‌ای که اوایل آوریل هدف حملات مخفی منتسب به امارات قرار گرفته بود.
به گفته این مقام، حامیان این ایده معتقد بودند: «
بروید و آن را تصرف کنید؛ در این صورت به‌جای نیروهای آمریکایی، نیروهای اماراتی روی زمین حضور خواهند داشت.
»
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/funhiphop/75097" target="_blank">📅 19:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75095">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به امید قهرمانی تیم محبوب چلسی در بازی امروز  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/funhiphop/75095" target="_blank">📅 19:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75093">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 149 هزار تومان!
😈
(
فقط 300 گیگابایت موجوده!
)
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/funhiphop/75093" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75092">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عزالدین الحداد آخرین فرمانده رده بالای شاخه نظامی حماس هست که با تایید چنین موضوعی (ترور) یک آسیب بزرگی به گروهک نظامی حماس وارد میشه.  اسرائیل تایمز هم گفته به احتمال خیلی بالا این فرمانده نظامی ترور شده.  تا این لحظه بیانیه رسمی از حماس, گردان های قسام و…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/funhiphop/75092" target="_blank">📅 18:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75091">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1AT1xD33iBvEYsuqHSUT4Iutzlos2DBycDj6wLtR1N48o0pQDpYydXOWZQiEN8EbIIwhqid3hl1MBsWol50GYpRp6SJT18mBvED8nLZVh9Sp22D9UqsqlogxvSlptYFjS2YmWxU4ZVh_pjlL4CBX-t9aSuFK0NxnEAvE-rrBrULmItASqYDIKrCaffmBNppLaIymEo-jiDSdeadIzV_ID7nLPG_Ph6COds5xIMy0Kp7nN75vivxdJVZhcTr08ChYhGVs6nUGkOfUsZ9RW1vQwjpScTq5yoHQ5Ndbf8lsvjJLlzUSVru49F18YeSrj-XY2LiE6CQjuNNiGCMdk7JDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیتر چک مناطق محروم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/funhiphop/75091" target="_blank">📅 18:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75090">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">😵
بحران دارویی که راجبش صحبت میشه چیه اصلا؟ بررسی عملکرد 36 شرکت و 121 محصول دارویی نشون داده که قیمت 24 دارو در فروردین ماه بین 101 تا 3380% افزایش داشته : بطوری که قیمت پرداختی بابت بعضی دارو ها تا 34 برابر در یک ماه افزایش پیدا کرده.
👍
مهمترین دلایل تشدید…</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/funhiphop/75090" target="_blank">📅 18:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75088">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">از اون 682 نفر یکیش قطعا رضاست
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/funhiphop/75088" target="_blank">📅 18:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75087">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWiaA4W_u2rZdV04CueT1dM3v_64Egj3M1ZGDbyTk0qEmpu_kVXpo0_H7Dyyc2a3-qA3b8VlPRWJsZsMdvAnlgWDx3CykDI-MxxxwKCJjAUavbv1Ewyot_JN7516b0Gyy0zqAaMQT_l-hDgsMNff4FWhwgOdd_3iY0pMYgHmFUGUi4I4CuL29EaOebZUdUk1YNtZDIkVskN6KME6BGhCzr5CZJGJf7EMNwRT71FJHXXvLCOJWll3syQLwbXCO8DO_BXsMxbRx3N9cJvgwax95o2zQNqkDKRZj6nwq-Vm0Msty_2mePqfILpTiHUIFZ7yZglOnHawWl1jGM-PgI-Z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ کله زرد:
شوخی نداریم!!! ببین قراره بعدش تو موضوع مورد علاقت چه اتفاقی بیفته!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/funhiphop/75087" target="_blank">📅 18:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75082">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">😵
بحران دارویی که راجبش صحبت میشه چیه اصلا؟
بررسی عملکرد 36 شرکت و 121 محصول دارویی نشون داده که قیمت 24 دارو در فروردین ماه بین 101 تا 3380% افزایش داشته : بطوری که قیمت پرداختی بابت بعضی دارو ها تا
34 برابر
در یک ماه افزایش پیدا کرده.
👍
مهمترین دلایل تشدید چنین بحرانی موارد زیر هستند
🖤
اختلال در زنجیره تامین و تولید
🖤
آسیب به روند تامین مواد اولیه
🖤
کاهش ظرفیت تولید
🖤
مشکلات صادرات و تجارت در شرایط بحرانی
😞
در پی افت تولید و کاهش فروش و صادرات کارشناسان حوزه سلامت هشدار میدهند که
ادامه این روند موجب تشدید چنین بحرانی میشود و امنیت و سلامت جامعه را میتواند به شدت به خطر بیندازد
.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/funhiphop/75082" target="_blank">📅 18:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فعالیت جنگنده های ارتش بر فراز تهران
🔥
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/funhiphop/75081" target="_blank">📅 17:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75079">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پاشید جنگه
منابع عبری تأیید شده :
ایالات متحده در روزهای آینده آماده‌سازی برای حمله دوم به ایران را آغاز خواهد کرد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/funhiphop/75079" target="_blank">📅 17:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75077">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVEH16aNPUtI_kSQWcK6QA9yKujTQ_WTkonsD0p7FAgbEE598vbDHMgSGTxQTjb7SxjrgsNh2s6gQuauVE_e_jDGvqZNei1VicQblTXgdi-nKXLGO5N-QciERJgw5lYJv-Qpqy6U53_JnukIC2wWrUpRhyX_erebMkncK9IW2uVxZZCNRjoiBbLz2zZjvA5vXvPa6rHPX58pNaatjJOxZYudp_MtlThODqd7wpBdYRSlit_SkQJQMVQVtvsP6AO0Goc4V1EvuKs-QEmFzXZ7JP8_FN8RI2w9CtSNy__D0487N6d09i6rbp3Z-jnqyysYTrtajPkyy6UtkGHV0PFnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEwaMROtPPblYoVOBwB_qheELFSd1Dr1AcDs_z7PdoLpkOjHDO7a0kNXplAwM85SoXsET4zQ34Yegn0DetZl-rt43w3JkgXDLzdr6AS6V0J2DO7BZ3uiW6HDDCeKmRn5zsUlgAesfK_bHUTrLpQVmqHp6c0zQpr4uE_ytOTZ_AN1QPG2pdoBd47XNcNfYDwKx-LkpyGniBsZJ5T9lQpEWrxitMSoPsTndCAYspLTC8xyozY8XnaV4ksf6bpEH3qmDhvJnUQOtgtZxHRt4LLkhH05hPYLab2RRd21dq7mI1unKwdvjvKaNj6Lwxnhze-YwhHO7C7-l_mV2t0gmp2N3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر یو اس اس لینکلن یا شاید یو اس اس بوش امروز در شمال اقیانوس هند در حالی که توسط یک ناوشکن در ۷ کیلومتری شمال شرقی اسکورت می‌شد، مشاهده شد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/funhiphop/75077" target="_blank">📅 17:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75075">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پاول دوروف
دوبی دوباره حسابی شلوغ و پرترافیک شده. از همین حالا دلم برای
«آتش‌بازی‌های ایرانی»
تنگ شده؛ چون باعث شده بود آدم‌های زودباور از شهر بروند و دوبی خلوت‌تر شود.
پدافند هوایی امارات
هم عالی عمل کرد. جالب است که اینجا با
مالیات
صفر
درصد،
امنیتی بهتر از بعضی کشورهای اروپایی داری که مردمشان
نصف درآمدشان را مالیات می‌دهند
.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/funhiphop/75075" target="_blank">📅 17:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75074">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">با کشته شدن عزالدین حداد، تنها ۲ فرمانده حماس از ۳۲ فرمانده که مسئول حادثه هفتم اکتبر بودند زنده هستند
بقیه به دست اسرائیل کشته شدند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/funhiphop/75074" target="_blank">📅 17:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75072">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شایعاتی درباره آغاز دور جدید مذاکرات ایران و آمریکا هست.  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/funhiphop/75072" target="_blank">📅 17:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75071">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شایعاتی درباره آغاز دور جدید مذاکرات ایران و آمریکا هست.
@FuunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/funhiphop/75071" target="_blank">📅 17:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75070">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">😠
ترامپ
ابو بلال المنوکی
، یکی از رهبران ارشد فعالیت‌های
داعش
در غرب آفریقا و که به عنوان
دومین فرمانده داعش
شناخته می‌شود، در عملیاتی مشترک آمریکایی-نیجریه‌ای
ترور
شده است.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/funhiphop/75070" target="_blank">📅 17:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75069">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سنتکام
تا امروز، ۷۸ کشتی تجاری تغییر مسیر داده‌اند و ۴ کشتی غیرفعال شده‌اند تا اطمینان حاصل شود که قوانین رعایت می‌شوند.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/funhiphop/75069" target="_blank">📅 17:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75068">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRQpFnkrTwBRytRaCqHfaHBfN9A_L9aPJUXiQlc03hAU3glqNE2ZHAJRWiJnqbo6chFAUHSlGHFv4opMO4dq3rcBS-dSkXaZBxZY6UxkRp6q9Ty7SAxziVweCLEHTsa3ElByn3jZLT_phlGp2yQXtyiD2TZZtFzzbyzLNRcP5GRYS1TV18OSIj8GyGbQfWKsPrb2R9l5eXXYWuIOhbyvlnVesBzc6KdyOC0xqJ_D7KAZ4wRFiN-IP6y4mPihgv8ZDKi1IAMDhyP0qicyvJBiOJ199_J1KktcqX6oGS-ydcpwtg4GpaGmiNqixgTumOrIh2fAGSEm0CiELEPx1SLhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده باش آماده باش
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/funhiphop/75068" target="_blank">📅 16:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75067">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioX0D60aJCjCYjK9F8mSWUp6jT-GMKCv1i654rB56pRUBHAKcu4Ako38WjQqEUPJrWHotNrKtNoxUwJbKYG0nQkjYo7PoDCQqvaOKoPjInBjx5YagP0V9k69WzFYKUueIyfzUA1QXsa9EeC4bBmF3_pgFCPTd2_us0O9acIwk8iLZYWr8iSIDb0tB-mxC6YQCOTu7qNTWFzG_mi_SkfLR6ucI0vqWDnkHJQUjOYcKcolIFNb5ckEUT9MHpK6b3h4-3Nj29RUSmUzYrnPlI2qgnMNpOI1NpHnLUxqh_ZD9DOJjcsVumKQTZQIrJ62vevpJOMCBD1HZgFgKzaCeRl2mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به امید قهرمانی تیم محبوب چلسی در بازی امروز
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/funhiphop/75067" target="_blank">📅 16:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75064">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بهترین نوک تاریخ لواندوفسکی از بارسا خداحافظی کرد.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/75064" target="_blank">📅 15:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75063">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKHzs2rStIT-GB7OXBpwsCLRjR8iY6EykiuRG2ABmx8tQX7ZeKDxLa621AQQ2E6FVCP2eQaDfyo7vMEFFe-VWsWfTgc3_jNeVKpPU3rr0pIFkeMTM-xlVE5d6dlYtlRjhOqo0JH7LwoYkcl9MsuVU6PSS4o6WKL-K4t9SgFKxuy_ET6ltXzVUtX42bK1wTZg6Lhqbq0uaRTZAGgdF4E7XWT1ygTFWkiCagaCI5pQJqbnOL9jFJQaFbyiDOnlzxY0wE9gtyxAQ_wnd8mB1Rq_bb3h9aAIH6QVNbhGCQX6zlkoYoU7fgy5jffxubvH85uS8COy0hoMg1ZGpo0WUz9vzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین نوک تاریخ لواندوفسکی از بارسا خداحافظی کرد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/75063" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75062">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قبر بهار شاه‌مهری، جاویدنام ۱۷ ساله نیشابوری که در ۱۸ دی‌ماه جان خود را از دست داد، در روز تولدش توسط افراد ناشناس تخریب و شکسته شد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/funhiphop/75062" target="_blank">📅 15:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75061">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">در همین حین که رسانه های جمهوری‌خواه معتقدن آمریکا جنگ ایران رو دوباره از سر میگیره، رسانه های دموکرات میگن ترامپ دنبال یک راه خروج از جنگه و نمیخواد ادامه پیدا کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/funhiphop/75061" target="_blank">📅 14:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بارسا داره یه رافینیا دیگه میخره
ژائو پدرو مهاجم چلسی</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/funhiphop/75058" target="_blank">📅 13:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0jSSvEvCVO1i5spzBJknvbcWc-1IwCQxjuktF_nt2JSJOROE1zQlk0SM05mgFga36F7B2-JGQsKdzehwUUw9CsELxLFXLDWG4stVL-9KwBIPd1vJ5VN2oHQex8x_KLyeGtQMAADq_MgXacYKaCL6DaW6Qf5oyQ43P4EiCfY_oj1kmjDlOi-hqZ1jA99Jt1JfLNIDUdUbOxgg8N5_347DUK21woSicZbObqR3s_wRXu0JP7oLX3CAHIVOD7Fei2DgfI65VkqLkdJ8V2yn5sSlBAU0ICy6KXYuj5zm3wa8NkI-L48RpKBbScaiYKWlXcmhouTYpmyWFX2fAK5EHUE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی محمدی مشاور قالیباف :
ای لشکر صاحب الزمان آماده باش
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/funhiphop/75057" target="_blank">📅 10:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رسانه‌های آمریکایی: ممکنه دوشنبه جنگ شروع شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/funhiphop/75056" target="_blank">📅 08:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جسی واترز، مجری فاکس نیوز:
ترامپ درحال آماده‌شدن برای دور جدیدی از حملات نظامی به ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/funhiphop/75055" target="_blank">📅 08:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">علی یک تنه ی پایگاه رو با سیگنالاش پولدار کرده دیگه شبا نمیرن تجمع بخاطر ۶ تومن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/funhiphop/75054" target="_blank">📅 07:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فعلا برای هر معامله ای چه خونه چه طلا چه دلار و کریپتو تا اخر این هفته دست نگه دارید ببینیم وضعیت چطور میشه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/funhiphop/75053" target="_blank">📅 06:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75052">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">از ساعت ۵ تا ۶:۳۰، چندین پرواز در ارتفاع پست توسط چند جنگنده میگ۲۹ و F4 خودی در غرب تهران انجام شد، که صدای شدید آنها در بسیار مناطق غرب و مرکز تهران گزارش شده است
تا کنون دلیل این نوع پرواز در این زمان اعلام نشده است به احتمال زیاد شکار پهپاد متخاصم(انفجاری گزارش نشده است) یا پرواز آموزشی بوده است
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/funhiphop/75052" target="_blank">📅 06:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75046">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">درس امروز اشخاصی که پرچم های
🇺🇸
🇮🇱
میزارن جلو اسمشون هیچ تفاوتی با اشخاصی که پرچم های
🇵🇸
🇱🇧
🇾🇪
میزارن جلو اسمشون ندارن هر دو از یک میزان ضریب هوشی برخوردار هستن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/funhiphop/75046" target="_blank">📅 04:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75045">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">درس امروز
اشخاصی که پرچم های
🇺🇸
🇮🇱
میزارن جلو اسمشون
هیچ تفاوتی با اشخاصی که پرچم های
🇵🇸
🇱🇧
🇾🇪
میزارن جلو اسمشون ندارن
هر دو از یک میزان ضریب هوشی برخوردار هستن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/funhiphop/75045" target="_blank">📅 04:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75044">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyn-0CHoqhxIEoppKaH9LzN5HsTQ54y2b5v_hvyBeGZfje6QJMvfSNccNPqhbAzaXq0IB-suL0EIa-3lw_vHa9CBXZ2NGLBNxYQ8agtQGAxlL11kdkgzm3WBvq0eW8_CdEaPCAcd_XyIJJ1RulPEQ9HM1RtgnMZ6XTgI2jb2IlxURT0Y-n_MnXijpDG1ZLJRZO9rQ8R2WAdWQiswz77G7kWOvXlmPj1nI81o_vU7VSXwocjo8cloWoljAQI-gkFXubh3AqyIpx85ERkUThWVzfKr81KRSkLiB504gkoHBqlR-tMjRC6T19ckX4mWhH04iQEbeyf9wqiLQr-oAxxAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجله
جدید تایم درباره دیدار ترامپ و شی جین‌پینگ
دنیا دیگه مثل قبل نیست که آمریکا تنها قدرت اصلی جهان باشه.
😊
🔜
الان چین خودش رو هم‌سطح آمریکا می‌بینه و این دیدار بیشتر شبیه گفت‌وگوی دو ابرقدرت بود تا مذاکره یک کشور قدرتمند با رقیب ضعیف‌تر.
حتی اگر توافق بزرگی هم امضا نشده باشد، خودِ تصویر کنار هم نشستن ترامپ و شی یک پیام مهم داشت:
دنیا دارد به سمت چندقطبی شدن می‌رود
.
👍
🤯
چین با قدرت اقتصادی، صنعت، فناوری و نفوذش در زنجیره تأمین جهانی کاری کرده که آمریکا هم مجبور شده با احتیاط بیشتری با آن برخورد کند.
خلاصه
آمریکا هنوز قدرتمندترین کشور دنیاست، اما دیگر تنها کشوری نیست که بتواند به‌تنهایی مسیر دنیا را تعیین کند.
👀
😎
مطالعه بیشتر >>
لینک
مرتبط با مجله اخیر تایم
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/75044" target="_blank">📅 04:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ببین اینقدر این هکرای چینی خطرناکن که آدم میمونه چی بگه جدیدا رباتای چینی زیرپستای فان هیپاپ (
💞
) میزارن.  @Funhiphop | reza</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/funhiphop/75042" target="_blank">📅 02:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75040">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ببین اینقدر این هکرای چینی خطرناکن که آدم میمونه چی بگه
جدیدا رباتای چینی زیرپستای فان هیپاپ (
💞
) میزارن.
@Funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/funhiphop/75040" target="_blank">📅 02:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75039">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUyoKTqEsNtnyYH_GRKKq4irBh05tjef548IqXrSxTqMbNVA9OCZ0hwXbY5FuKTKidl1Ns__4CM03iRBkI-OTbO3u8KJZETfvcdA-sxbGZo2BZdyA-_DEha3mufKUuNZHXt_gx_IRmJlARmq9P_zj9HbyYA1BvesK3TQo1ojeDA6TGQhLBoVPEdxeb_JRtoW_Zpw8Wuz-yvWnIRvwAKVKsWdhujQkbzZnEs1qg--G49D9xkxiDXtpe2L7NrNUp-mxFdVs2pGWmjIv4gFK5M6IiCPBu1HQWn-HE2_vmzaRAH2dStxwKHQ9FV2wq7H68hT45l8AWOpdzdf0e4sXntmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید از آلبوم دریک حمایت کرد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/funhiphop/75039" target="_blank">📅 01:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75038">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دست مغول‌ها چهارتا آجر میدادن تا الان اسرائیلو نابود کرده بودن
😁</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/75038" target="_blank">📅 01:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75037">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تایوانم پوشش بدیم؟
@Funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/funhiphop/75037" target="_blank">📅 01:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75036">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مورینیو:
سری آخری که سرمربی رئال در الکلاسیکو بودم ۲۵ تا موقعیت پنالتی داشتیم هیچکدوم رو نگرفتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/funhiphop/75036" target="_blank">📅 00:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75035">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مورینیو:
خیلی خوشحالم که این افتخار نصیبم شده که سرمربی وینیسیوس باشم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/funhiphop/75035" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75034">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فوری از فرید رومانو:
مورینیو سرمربی رئال شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/funhiphop/75034" target="_blank">📅 00:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75033">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">[ Fun HipHop ]
pinned «
رئال بازی خودشو برد و یک قدم دیگه به قهرمانی لالیگا نزدیک تر شد
🔥
🔥
@FunHipHop | Farid
»</div>
<div class="tg-footer"><a href="https://t.me/funhiphop/75033" target="_blank">📅 23:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75032">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCL3KGC2G9XO63gKImQ8iZuQ8joO5g2CVL0ozO4XJHllyvHBq5HhlXZXsTeJU_BhEE4hNsNgZx-mooht4Yr84yJQTSCapjnvrHS3iDVaUcENR7V61c2lo6Pu3qVJIZJ8TYteiml4FZknKzUQzfgeuI4uad6xWXOWfRPWrkRXLfH9ThGEdllqh2G2laimf03Go88vglL0FZ_IplE-8-g988LFxBl0-wXVNj60CoZur3iHL2MYnn7WdFbWPP_AZJT2xBsQV66-FRn_scR5zdeh5mRLIl62f9XJNARWlMakwe0oxpk1p7lBim9Hs7i4eVyJJn0mpGoAtsJCoGiAmc_SMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">د اتلتیک: راب دیپرینک هلندی که قرار بود یکی از داور های VAR جام جهانی باشه به دلیل تجاوز به یک پسر 17 ساله دستگیر شده و از لیست داوران جام جهانی هم خط خورده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/funhiphop/75032" target="_blank">📅 22:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75031">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیایید بالا دلقک شدیم.
هادی چوپان: ما با زحمت و هزار دردسر به قله رسیدیم، نباید بازیچه دلقکان مجازی شویم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/75031" target="_blank">📅 22:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75030">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👑
دنبال کانفیگ استارلینک با قیمت پایین هستی؟
🫰
🚨
بدون‌ محدودیت‌ زمانی
❤
کاربر نامحدود
📞
بدون‌ قطعی و اختلال و کیفیت عالی
🧭
بدون ضریب
✉
دارای لینک ساب
👍
مناسب انواع بازی های آنلاین بدون لگ
🍿
مناسب یوتیوب، اینستاگرام و برنامه های حجم بالا
👑
یکبار خرید کنید و مشتری…</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/funhiphop/75030" target="_blank">📅 22:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75029">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6p1BFlKyx1LkkjXKLJqyNI-2IlvdhdkHviVxbwoqU134Oypu6mkPfWWgxqX8LmwSvdCaUS-90vNHimLzGg7ve0tsRvBQwu8r-Bb0kfJrqMFBv8_iQ095buJBciCnqXNvdnlafFR26yMz6bdHmp-lPHaM8DdAjosg0AOnGJtf0NeVZqOcDjBmKLM57mzWZ5zYxjp5kWL8lQFSOvNTMqXmD_se3NHRLb0y-BsxVglCRGKvUziQyAI4JT4exgHjs4CHE37Www8krj1hZiUdpsIdoUo170knzTeZfSdYW8SdulRwZLZuiRTd6kDtpuffDLHvXfNDlho2qjvUvVU5LbLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
دنبال کانفیگ استارلینک با قیمت پایین هستی؟
🫰
🚨
بدون‌ محدودیت‌ زمانی
❤
کاربر نامحدود
📞
بدون‌ قطعی و اختلال و کیفیت عالی
🧭
بدون ضریب
✉
دارای لینک ساب
👍
مناسب انواع بازی های آنلاین بدون لگ
🍿
مناسب یوتیوب، اینستاگرام و برنامه های حجم بالا
👑
یکبار خرید کنید و مشتری دائمی ما باشید
👇
👩‍💻
@ConfigRahNet</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/funhiphop/75029" target="_blank">📅 22:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75028">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd67VsawsojBitvGptVY6B9SISb-AObG_MWC61hiFU5J312lSHU5vB6U_-8DKMzPqgIJY45OdZO7cRJESNFacnUGmN7KbETgRVqygnjLWasu5U849OxUKp-GglzgbgNkiRr5PdBgsnXjLukKER5oPXe_CXfhT8zeUnuuRK0uhubE8Tncw_JlqAYl1-1VgdQYaKHN9-y8mDIteXSatEAW1L-MBQ-zz1ufMo4Bk2Q1g-EIx1-B6osnBtcvWyVqwerbCDjGruz6DWPrX6vFvMf8m306arTCeAUibFb7ay5qqOtVrTLXIVEuKHotNDDwtLlTjSD8B780m44-wa48wwZEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/funhiphop/75028" target="_blank">📅 21:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75027">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش های تایید نشده از ترور فرمانده حماس  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/funhiphop/75027" target="_blank">📅 21:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش های تایید نشده از ترور فرمانده حماس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/funhiphop/75026" target="_blank">📅 20:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75025">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">امشب میزنن</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/75025" target="_blank">📅 20:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تحلیلگر های بازار های مالی نسبت به
قیمت نفت
یک دید
صعودی
دارن و تو تحلیل هاشون
راجب جنگ دارن سناریو نویسی میکنن
که با از سرگیری درگیری های
خاورمیانه
قیمت نفت میتونه تا
بشکه ای 140 دلار
رشد داشته باشه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/funhiphop/75024" target="_blank">📅 20:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نشد یبار یه سامسونگ بگیرم دستم داغ نکرده باشه</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/funhiphop/75023" target="_blank">📅 20:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO9KhyURk4yD1eZFnsU4KTALg7AGEWWthDrsxYED0xk3JLde3oi5AmxYbZWiKYGOiwiDYpD9Z-n3q61x1sv5OVwOj2rvpU2nBL9_lXFQZiAcRyGf9-6beC2s4GZrZuG6azy_IEtiY6p4_jfCeL6vt3H8UQc7PzksqQ1o31ElgjV-4jTDjee6PZhAfu9JDlh-zZ5ShWYhvoxJSqy6woAdx2lz5ZE8hD6k2zAC0EVrfv3rbi3sBILLl5O9judO0CrOXiMHpG_Y-tHslXMIJE3EkqqmHCyLCr5zzFBdd5B5E93MBV56wfgGYHlcmDGIhqvMWvB6pG2s8x6bOKNFGSnQ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا وضعیت اقتصادی خیلی خراب شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/funhiphop/75022" target="_blank">📅 20:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پشمام دریک میخواد برا تیم ملی ایران سرود بخونه</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/funhiphop/75021" target="_blank">📅 20:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Duc1nrleLW6Yh5B9KQjeT3zXbr637BesZfToPmTzc9JEjWalOeBqtGN-o4Hby55jMnqEhGUstdU_QO5KCd_DkhnhWH_BEgOGXHdjwgIBIq6lci5myMPwhdw6zqWozCoz1fVqakKECwk3DBQwtOwrZJHkUQW0aYaYkR4fgC9wPNVUA9P_PqM0KU9viz6f6czFOjvGKKqhh855xcdgReo8Xf5LZkq0WvLn8T0b1Rnj4-nZnd--HmBGk0BYcCFF7Lz9oqtTqj7uzw21pGw6dH_hracz493RsMyC5lMAlYafQUWMfi2QfTDZG0EnTo2xm15JUiv0qTAKyhzRE5YSAXd0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/funhiphop/75020" target="_blank">📅 18:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75018">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزارت نیروهای مسلح فرانسه:
ناو هواپیمابر شارل دوگل در دریای عرب است و احتمالاً ماموریت آن بازگرداندن ناوبری در تنگه هرمز است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/75018" target="_blank">📅 18:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75017">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kgckf69mg0rZduW-VBm3Vyr3pac979F--YpvHkl1IfcDfc60_2TisSiLdz2Sya3ybVg6Q2HrqY14J0RqHiminm7NOS93vSSsXYmNseukPh_FAHL13thpOM-IERGDYNTwx3sC-L1IWgLVt0Va8oXyAesvbyIA4nhwhuif_7TK-nWhN78Nxbhh5MDFkmgji4Eyog3CBcM4rk_8p5y1VdEyH5feuASon545i13Q76DLLPmOceZpYvgg40aFPB7pK0hWJ1_gwU2RX2FBqW366f7r7cPxvSBz-D9_zD61htiC8YxAu9z34Gm4rHVxAy98nDKYNqApGmkQkkk0miVNKVmgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artist: Drake
📋
Title: ICEMAN
🛑
Featured: Future, 21Savage  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/75017" target="_blank">📅 18:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFo19d1M7YQtL9vw6VhpnSpkjlHslU4DlseEdDfsOMOiyjhIFPSTiK3jkuZ4PzAYDbLILWyBQHfLpAlt71DE2uZbG4WnotAetWGDTgIXSA3-YCCbzhM6pthynu0YI4848LCT9MaKADNvI9tVfptsmYjJztxPlzav-onE22Ykry-5jLMMRKU-D1EPSvChAzlpElMoFFj4BTazX804W35PLLY5qIWPOfg_DpGswhivsFXzdv_xgZMr1_7HGExH4HEJFtSzgA-dHAybrChpJS8v5jBEJEfEOwib0QB9cBfjQab18gCE47-34F1_tpiqHkTVpq5MeBvZUp-EDRQJzN8iCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیتکوین بگا رفت
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/75016" target="_blank">📅 17:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75012">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwL-o2FWiLfvgEugpqjT0bbir_hO5YOiTkYU9gjlE_iQIE-eKe-4zbmabDnZ-MADQDCTbh_QP57PE77vtpVgp87t7KhDx5kmHoWLWzeyMF-VymMTkfBQTWEGPT4BCCrp0jdd3bTFLPm7EJ7fNlggMk8YJ5uT6K5KVQo7Y4lJoww915a8uYU1DVFLL293NJVL_HwyR_M3y5BZ0RXyA7ENyscT82oqgv-EOxSncLE8yQllzG-sKeB6bWtz8R_S2DCHtmWCX6_dpA1bj8tEOyt1TbIKbyx0H_uv0UBXODC46HYdvhnt_V1jVmvcpPfwnjzasKOSciCr4CxJtcKaP3Cz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک Little Birdie  "همه ی دختران عرب یک طوری با من رفتار میکنن که انگار شاهزاده فارسی ام"   @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/75012" target="_blank">📅 17:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75010">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">موزیک Little Birdie
"همه ی دختران عرب یک طوری با من رفتار میکنن که انگار شاهزاده فارسی ام"
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/75010" target="_blank">📅 17:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حس میکنم تو پکن ترامپو دزدیدن یه نسخه چینی‌اش رو ساختن فرستادن آمریکا</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/75008" target="_blank">📅 16:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75007">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546804485e.mp4?token=E3XoVrOcx9GvN3qHBXnGblzdW-Nxee8pgQNQmnna0oZJ7AqnVz4tS41ly15gudWGsD3xF73HRH7eWbWgT6XpMOQ_MV0fTHTTpDq2XkbQ3XqKWNOqcX4Ki2RnQrhIVZmc3ysgBz17z3FwqGowFZnRZy0RankwGS0_ikxEHDhgQd1jbsPgjloy2523VnBFK4_M9CkBz4LR-hCiDIszh3OJWDM1xkQnopRnS6UtXEC0ZfSKjxbjMLP3zFe0c-HU1AI6EzTOVTwIfQWUP3nfdTGM7I2fMJQLtVZ5QX16L2IgjjvKnMw6p01uUPDghjYCx1g5aCnO6dmH6XuAcjkh5I6p9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546804485e.mp4?token=E3XoVrOcx9GvN3qHBXnGblzdW-Nxee8pgQNQmnna0oZJ7AqnVz4tS41ly15gudWGsD3xF73HRH7eWbWgT6XpMOQ_MV0fTHTTpDq2XkbQ3XqKWNOqcX4Ki2RnQrhIVZmc3ysgBz17z3FwqGowFZnRZy0RankwGS0_ikxEHDhgQd1jbsPgjloy2523VnBFK4_M9CkBz4LR-hCiDIszh3OJWDM1xkQnopRnS6UtXEC0ZfSKjxbjMLP3zFe0c-HU1AI6EzTOVTwIfQWUP3nfdTGM7I2fMJQLtVZ5QX16L2IgjjvKnMw6p01uUPDghjYCx1g5aCnO6dmH6XuAcjkh5I6p9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سؤال که آیا درباره حملات سایبری علیه آمریکا با شی جین‌پینگ حرف زده یا نه:
'آره، بهش گفتم. اونم شروع کرد درباره کارایی که ما تو چین کردیم حرف زدن.
خب می‌دونی، هر کاری اونا بکنن ما هم می‌کنیم. ما هم حسابی ازشون جاسوسی می‌کنیم.
بهش گفتم ما یه عالمه کارها علیه شما می‌کنیم که اصلاً خبر ندارین.'
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/75007" target="_blank">📅 16:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZy29Gdb97VwQ3YgRBU_lV8w6H-wqWfeQzCnN8MEHqYuYmAXn1VHPlyj3n4WLK7VIkeHLYjyz0n6_fHCn759V9LV8Q_ObKoIEm79gPx5Gj_v9IQLdjAa_WZgbErg9YrfJyKxRzCODwbNIli_-Npa5CXNARujoQigcndRCaG5C4JY2fyXxmUr05HzR301Z1gqXmrrYJ6xxgkesy6blkTBVTPmvd7Po3L3j5IjB34zFQ504-GUh588he3GPOQu6G1nrYrDXmG2pRyprPylBrJtAk6z0eUQo_bR5ZWCAeEaxJfDCt8zx4CQcjjMQHJn54rIuMmkI_3B-APg1TI2FHNBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتلو داره برا جام جهانی آماده میشه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/funhiphop/75006" target="_blank">📅 16:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75005">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📣
جشنواره تخفیف نت اسپید
📣
🗣️
پایین ترین قیمت و بالاترین کیفیت
🔄
⭐
اشتراک‌های حرفه‌ای شروع قیمت از ۲۴۹ با ضمانت پایداری
🔸
اشتراک‌های پایه شروع قیمت از ۱۵۰ بدون ضمانت پایداری همه طرح ها V2ray و با لینک ساب
🔗
بدون محدودیت تعداد کاربر
👻
بدون هیچ گونه ضریب
⭐️
…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/75005" target="_blank">📅 16:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75004">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snDCKsYrU1IKV-2abjk_WM61zTOCQrHnyRp9LQuA7Wk7Bdbi5S2k0WG8IDepmFVH_kOj4-djmcxzC70KLGnALZ4rYu5lT0K72PHaq3c2J7KFUBxWVyDHkHpiNqT7lDdFA1tJSzDIEEbMb890acptzqPbgsE1_U33Pc97L94K5c3nBwTRpvLsEpo1lGfRAW5KM7cmEMla9idj3ugQK49z6eeFU8gKyb2IwqM15pUDCRR_24dkA3-Qm2hpdFC8cDAt_tP-mL_m-C46vd8iyfSxfQQG7uXc5gldzKvtC38ezsuA3MOa1IeotEkWAnLBkBJHLH0aBgl56YitXnDPnrMXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
جشنواره تخفیف نت اسپید
📣
🗣️
پایین ترین قیمت و بالاترین کیفیت
🔄
⭐
اشتراک‌های حرفه‌ای شروع قیمت از ۲۴۹ با ضمانت پایداری
🔸
اشتراک‌های پایه شروع قیمت از ۱۵۰ بدون ضمانت پایداری
همه طرح ها V2ray و با لینک ساب
🔗
بدون محدودیت تعداد کاربر
👻
بدون هیچ گونه ضریب
⭐️
مناسب تمامی اپراتورها
💡
مناسب آیفون، اندروید، ویندوز، مک و...
🎮
خرید و دریافت کاملاً اتوماتیک از طریق:
🔒
@NETSPEEDxBot</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/funhiphop/75004" target="_blank">📅 16:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فریدریش مرز، صدراعظم آلمان:
من یک تماس تلفنی بسیار خوب با دونالد ترامپ در راه بازگشت از چین داشتم.
ما توافق کردیم:
ایران باید اکنون به میز مذاکره بیاید.
باید تنگه هرمز را باز کند.
نباید اجازه داده شود تهران سلاح هسته‌ای داشته باشد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/funhiphop/75002" target="_blank">📅 15:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بیایید از تأثیرات محاصره تو بازار الکل بهتون بگم
آبجو کرونا تو بندر عباس شده ۲ تومن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/funhiphop/75001" target="_blank">📅 15:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خب دیگه ترامپ بسه. ادامه‌ی سخنان قصار دکتر عراقچی: بزرگ‌ترین مانع در روند دیپلماسی، پیام‌های متضادی‌ست که از آمریکا دریافت می‌کنیم که هر روز مواضع متفاوتی می‌گیرند. گاهی اوقات در یک روز دو پیغام کاملا متفاوت دریافت می‌کنیم. البته این وسط جنگ طلبانی وجود دارند…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/funhiphop/75000" target="_blank">📅 15:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f637359e4.mp4?token=ZdzL7EERV43m00gp-p4BZXYr7yuutcPbFY210t8hpEl__iAh71_hz5WuLiNYIicouzHsX1qDQDJXNyO1gGeb-XlOBRB_gP8qXkB94WaQRF5hBj9fHDPcxpP6bbNVHAp3sB6O7fvM9pYkUw1CsztO-l2GwEm7eIvhLm-yi08Lu98nD2naPLT_g2_8pLy6Q924wXJ1bZUNH6SXw39Z6q9ybGqZJilXkQMwK4gqgvA2_lkdmR3UdQsNjxwoCvLsvH9SiYv9CJJi0xomC4qjM8tyUhnOya9gGkJK-41Xd4zuBVbnPawyKhfb1IjDnZkeE75AV3YTA5pWOUh0pJwSaNgSWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f637359e4.mp4?token=ZdzL7EERV43m00gp-p4BZXYr7yuutcPbFY210t8hpEl__iAh71_hz5WuLiNYIicouzHsX1qDQDJXNyO1gGeb-XlOBRB_gP8qXkB94WaQRF5hBj9fHDPcxpP6bbNVHAp3sB6O7fvM9pYkUw1CsztO-l2GwEm7eIvhLm-yi08Lu98nD2naPLT_g2_8pLy6Q924wXJ1bZUNH6SXw39Z6q9ybGqZJilXkQMwK4gqgvA2_lkdmR3UdQsNjxwoCvLsvH9SiYv9CJJi0xomC4qjM8tyUhnOya9gGkJK-41Xd4zuBVbnPawyKhfb1IjDnZkeE75AV3YTA5pWOUh0pJwSaNgSWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب دیگه ترامپ بسه.
ادامه‌ی سخنان قصار دکتر عراقچی:
بزرگ‌ترین مانع در روند دیپلماسی، پیام‌های متضادی‌ست که از آمریکا دریافت می‌کنیم که هر روز مواضع متفاوتی می‌گیرند.
گاهی اوقات در یک روز دو پیغام کاملا متفاوت دریافت می‌کنیم.
البته این وسط جنگ طلبانی وجود دارند که می‌خواهند ایالات متحده را دوباره به یک جنگ دیگری بکشند.
ما عمیقا امیدوارم که آمریکا این اشتباه را دوباره تکرار نکند.
ما معتقدیم در نهایت این دیپلماسی است که پیروز خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/74999" target="_blank">📅 15:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ: نیروی نظامی ایران رو از بین بردیم ولی شاید نیاز باشه که یک عملیات پاکسازی سبک انجام بدیم. وقتی به پیشنهاد ایران نگاه کردم، تو همون نگاه اول از جمله‌ی اولشون خوشم نیومد پس پیشنهاد رو دور انداختم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/funhiphop/74998" target="_blank">📅 15:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مارکو روبیو:
اگر ایرانی‌ها تصور می‌کنند که ما برای رسیدن به یک توافق امتیازاتی خواهيم داد، سخت در اشتباه هستند.
تحت هیچ شرایطی یک توافق بد با ایران را نخواهیم پذیرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/74997" target="_blank">📅 15:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: نیروی نظامی ایران رو از بین بردیم ولی شاید نیاز باشه که یک عملیات پاکسازی سبک انجام بدیم. وقتی به پیشنهاد ایران نگاه کردم، تو همون نگاه اول از جمله‌ی اولشون خوشم نیومد پس پیشنهاد رو دور انداختم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/funhiphop/74996" target="_blank">📅 14:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74995">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ:  آخرین چیزی که الان نیاز داریم یک جنگ است. در چند روز آینده درباره رفع تحریم‌های اعمال شده بر شرکت‌های نفتی چینی که نفت ایران را می‌خرند، تصمیم خواهم گرفت. اورانیوم غنی شده ایران می‌تواند به چین یا ایالات متحده تحویل داده شود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/funhiphop/74995" target="_blank">📅 14:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">طبق گزارش خبرنگار الجزیره، انگار واقعا اون ۵ تا شرط پایان جنگ فقط برا مصرف داخلی نبوده و جدی جدی اون ۵ تا شرط رو به صورت رسمی و مودبانه به آمریکا داده بودن و آمریکا هم به صورت رسمی و مودبانه یه تک تک اون شرط‌ها قهقهه زده.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/funhiphop/74994" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74993">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ:  من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم، اما این باید یک تعهد واقعی باشد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/74993" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74992">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترلمپ:
هیچ پیشنهادی مبنی بر تعلیق ۲۰ ساله‌ هسته‌ای وجود ندارد،</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/funhiphop/74992" target="_blank">📅 14:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بخشی از ریلیز جدید رهبر جدید انقلاب: همه‌ی اقوام و اقشار ایران را در حفظ هویت، اصالت و استقلال خود و مبارزه با «ضحّاک‌» متجاوز، همدل و همراه و همساز هستند. از سوی دیگر مقاومت غیورانه و پیروزی افتخارآمیز در برابر تهاجم دیوسیرتان و شیاطین جهان، ملت را برای پاسداری…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/funhiphop/74991" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74990">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بِعَون‌ِ الله تعالی.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/funhiphop/74990" target="_blank">📅 14:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74989">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بیانیه جدید سید مجتبی خامنه به مناسبت روز بزرگداشت فردوسی زودی ریلیز می‌شه.
❤️
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/funhiphop/74989" target="_blank">📅 14:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74986">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بیانیه جدید سید مجتبی خامنه به مناسبت روز بزرگداشت فردوسی زودی ریلیز می‌شه.
❤️
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/funhiphop/74986" target="_blank">📅 13:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74985">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVAHID</strong></div>
<div class="tg-text">عشقم لبات مزه دموکراسی میده</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/funhiphop/74985" target="_blank">📅 13:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74984">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSeuW_kYo6Mk3zLOcYjLIB8ufJzGCKg-pPmoCkWZtU7Dp9Gc32Fw0FUDJyeIFZntIXvQpagGI8uC9aOS0mv3VQ0wdhiDr73jPm2N5DWNqA8gLpoZ3PAXgisBIwylTt2ttNHnHbm-z52utnppZOJqscH0_WQwMZebHyd7JTjPZaH8TGmP5hNn836zz4oqqL0goYJskucj-6l1-J9y4QUGzX_DSWvbuFY1i0JUFl2rOgUA9A1LP5fSEGZCbLLjVFCPW2ayFivyXLu4iELVxgVll9ZYV-fb8v-oefI5TR5oKt2h6WQfdfRcv8k5-GpBrUzMp5eyvjm843wSN4oSbO9TUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/funhiphop/74984" target="_blank">📅 13:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دکتر عباس عراقچی:
آتش‌بس بسیار شکننده است.
هیچ راه‌حل نظامی در مورد هر چیزی که به ایران مربوط باشد وجود ندارد.
ما فقط در صورتی به مذاکره علاقه‌مندیم که طرف مقابل جدی باشد.
ما به طور جد به آمریکایی‌ها اعتماد نداریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/funhiphop/74983" target="_blank">📅 13:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74981">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرهایی به گوش میرسه که ایلان ماسک با بریکس حساب می‌کنه پول جنده هارو.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/funhiphop/74981" target="_blank">📅 13:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74980">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd7ioXz1YKoI_HM5OCGeLEtVlI2MRXwMQDR38VqrSoDoBQxj4eSfcDfspWNpMeEkCkbHUcAsn2-NSDrefPZKW6Rkij-C1M8yB_qllh-cb3vdK86vZIEtMQ3xBIjKko-dTa8TIO1j4lE7xRVgbSx6sc_8vsjdMQ8aywiZkxbiTldFC4t2nBzVXpja9QDS3djnGkqPslb0yefs1dkxu97aj9Nu0ktdJxXTpdXLkmjfbCfwsOnAnpv3LOyB1qjHMD9sShQzGEY2Ee2VSh0GsyahUmsgtsNO7Cf8FU4icQ--js79M2yPavonSgy6zrTJoHZg_qu7GXQCx3SamkNt-b9lww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایکس تو چین فیلتره
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/funhiphop/74980" target="_blank">📅 13:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74979">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPMOjaQlOR4PmM1IlBLtxAVaFjjb6JmlZVeCgHFNDiZipmX7ehewu5WtZU2hBX0wSTIsUqqNukQgkh8nL6w0OHFR4rCRQEUgB6rTBLXh4zcp-PlFEK7u2bRpk9Y5rvC_wNauGaApffs9DGmUDWchpSvJ-KbFXi5Mk3m0uOvbr6zspZd-Ig3Q5MXKvMfNod2JuW3JSIN7Wgx0bArElq5mmVyn2KcMwJD5sxyTkQKP4IY1JJNOd3YJYR3FwgYP62q54kgz76109V6LLgnEDGS8-N-WG3KqEHtiPKU973W_BM6OHUVbYNHdkWhDcAZgdZlRl03LcV2FgHVJVxoAB2cStg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: رهبری ایران پنج شرط را برای آمریکا تعیین کرده است که باید قبل از ورود به مذاکرات پرونده هسته‌ای برآورده شوند: — پایان دادن به جنگ در همه جبهه‌ها (خصوصا لبنان) — رفع همه تحریم‌ها — آزادسازی همه‌ی دارایی‌های مسدود شده — جبران خسارات و زیان‌های جنگ —…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/funhiphop/74979" target="_blank">📅 13:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74978">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دریک تو آلبومش: ایسپ راکی، ریانا، بچه ی ایسپ و ریانا، کندریک لامار، دی‌جی خالد، پلی بوی کارتی، جی‌زی، لبران جیمز و پسرش رو دیس کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/74978" target="_blank">📅 12:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74977">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">از سیاست چخبر؟
دریک تو آلبوم آیس‌من خایه مالی فلسطینو کرد، خایه مالی ایرانو کرد، خایه مالی کانادا رو هم کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/funhiphop/74977" target="_blank">📅 12:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74976">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جمهوری اسلامی به مناسبت سه تا آلبوم جدید دریک در سه موج به مقر های گروه های کرد عراق حمله پهپادی و موشکی کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/74976" target="_blank">📅 12:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74975">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artist: Drake
📋
Title: ICEMAN
🛑
Featured: Future, 21Savage  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/funhiphop/74975" target="_blank">📅 11:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74973">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">۳۰ اردیبهشت پوتین به چین میره و با رئیس جمهور این کشور دیدار میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/funhiphop/74973" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74972">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بخاطر آلبوما امروز دریک اسپاتیفای بخاطر هجوم مردم چندبار از دسترس خارج شده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/funhiphop/74972" target="_blank">📅 11:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74971">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">قیمت اشتراکشم نسبت به شرایط اقتصادی هر کشور تعیین میکنن، اگه تو ایران آزاد بود و قیمت براش تعیین میکردن احتمالا ماهانه زیر ۱۰ دلار میفتاد</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/funhiphop/74971" target="_blank">📅 11:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74970">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قیمت جهانی دیش مینی استارلینک شده ۲۰۰ دلار  تو ایران چنده؟ زیر ۳ هزار دلار پیدا نمیکنی  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/funhiphop/74970" target="_blank">📅 11:15 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
