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
<img src="https://cdn4.telesco.pe/file/J7CrJOBKNgmDvdO5bIZs5mFAzD9UO1SCVYtqipE4XFFYaVH60gCuQ9gg-JIo4GL7cwo7fxUbaJkv3bTI--Cz749PCqjEXan3hGO9gg3ySTHBEq9k2_pSH3Krxl_UTjVFfb5JHl-OFvkZdRdNW8slTmDUKMjGLPbEoHHcLHy5-JRrQA-T5PY9kAgMcJ63A_Q6o4Dg-QXXbw1X_BH5mFfLrl4mK0S9vSg2yFDkGlwZPCp7Dx6RRKgfThJ4qmI1KINF-3j0uK35QpwYBJ2uRjubQjTyabTm0E3Lw8dQr8hpo7TT2EBTM2ZGETOxdvD600UsweWPGHkmCOo60CQFCS0JBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 10:27:23</div>
<hr>

<div class="tg-post" id="msg-15214">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG-9vD_T_x_9JWEBSGR_jvMCuBi0cF-pg0nog_h6DiW02_LCHN9ct_ko-lCUU9Op9t-22oOzQfKKdbV1HE2YyXzLmrPPXNYIho7Qb3BiYRqfHt4EaDqUv1N3Ilv2ZDVxF7IEJKruz8GYqGJfpsybKdY2FtD50iAP2UzB-M0SAqFusRreGyn14h53h0MXT-Q0c97o82UFgx5cA4B694NuVSjEI4B801CYWLEjY7jpQQvnIAFlwEeCKUqyu9Sk5evZEjfn6bKENtO6w3xNLXj8vcmoFc2SZ-8ct-K-A1b2Q0n4erUy81vv_yk4fWQQEjXLBUqBDAWPNU74enwIjJongw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای مضحک پزشکیان که مانند یک شکلک کارتونی با دماغ بزرگ و دست دراز شده برای گدایی است.
@withyashar</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/withyashar/15214" target="_blank">📅 10:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15213">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دولت سوئیس اعلام کرد که روز جمعه نشستی با حضور نمایندگان آمریکا، ایران، پاکستان، قطر و دیگر کشورهای مرتبط برگزار خواهد شد تا مذاکرات مقدماتی انجام شود.
@withyashar</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/withyashar/15213" target="_blank">📅 10:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15212">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وال استریت ژورنال: ترامپ در حال از دست دادن تندروهایی است که زمانی از جنگ ایران دفاع می‌کردن
@withyashar
الجزیره: موجی از خشم سیاسی واشنگتن را بر سر توافق با ایران فرا گرفته</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/withyashar/15212" target="_blank">📅 10:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15211">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سناتور بلومنتال: سنا قطعا توافق با ایران را تصویب نمی‌کند
محکومیت دو حزبی برای یک توافق ننگین عجیب نیست که شبیه «تسلیم بی‌قید و شرط» است، نه توسط ایران، آنطور که ترامپ خواسته بود، بلکه توسط آمریکا.
بیش از ۳۰۰ میلیارد دلار ثروت بادآورده، لغو تحریم‌ها، فروش نامحدود نفت، عدم بازرسی یا تأیید کامل. همه اینها به خاطر وعده‌های مبهم و غیرقابل اجرا در مورد تسلیحات هسته‌ای است که ادعای ایران برای پیروزی در برابر شیطان بزرگ را تقویت می‌کند.
هر چیزی شبیه به این توافق به محض ورود به سنا از بین خواهد رفت. برای اینکه اثر اجرایی داشته باشد، باید در اینجا تصویب شود.
@withyashar</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/15211" target="_blank">📅 10:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15210">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بلومبرگ از عبور یک نفتکش و یک کشتی حامل گاز مایع از تنگه هرمز پس از توافق آمریکا و ایران خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/15210" target="_blank">📅 10:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15209">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a024bb7519.mp4?token=coNXWnJYPbRsypoyYHKFgLkB3uGV70sKCaCOMnX8SU1bQw5rGJBe1AVIFwc-hCZPClmAyvmYx7coXq9DfkiCiysdZd5tZBEiK0Cjm5TNgWkt3kKUTIJdTlF0lAAgttml9U1_SxMU6XMetL83AVPaOKH4h0UAb8KtKt0acfaKGJU9LDtrg8VAQOBFtZdb3yrlkMxsRW1xKTtdb0LgpO7Vf2Ji9U3ODvufIpdh8_1WYyRNZTY1Vaz26qniQKa9S31-e4yIlL529q0YbBeFWNm0bvDV5l47Sy3VSK8-VB2pPJPMkdw2icCLUk1JkkfgRT9KSQ2IVB255QeD8s17Yf9MoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a024bb7519.mp4?token=coNXWnJYPbRsypoyYHKFgLkB3uGV70sKCaCOMnX8SU1bQw5rGJBe1AVIFwc-hCZPClmAyvmYx7coXq9DfkiCiysdZd5tZBEiK0Cjm5TNgWkt3kKUTIJdTlF0lAAgttml9U1_SxMU6XMetL83AVPaOKH4h0UAb8KtKt0acfaKGJU9LDtrg8VAQOBFtZdb3yrlkMxsRW1xKTtdb0LgpO7Vf2Ji9U3ODvufIpdh8_1WYyRNZTY1Vaz26qniQKa9S31-e4yIlL529q0YbBeFWNm0bvDV5l47Sy3VSK8-VB2pPJPMkdw2icCLUk1JkkfgRT9KSQ2IVB255QeD8s17Yf9MoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه امضا توسط ترامپ در مراسم شام کاخ ورسای
@withyashar</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/15209" target="_blank">📅 09:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15208">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjoFnA3Cjcl2hI8HLwy4rK5l3WqX7cKeiPw1efF9FQtfKteUCb_d04AdBIDZbXEtt-SovmM_mTFQmkeo114EsL8vzOh4fodlbcAQ9fLBQdR6JV5lP5QdH-aL6QtBi9Aa8bhGD5JqB_bxx7rJueJ46Oif3fvn92ZR9ne_5x6jXPhlSadN7naGUqR-STmmgT7AhaLN9wBRc1XYlChALstxJM-PmyIPvp44fTmkiO1Dt_jcFCp2qNYvrgfOiQkAME22G0Eg9mDIB-Vq72ElV-42BbJcpDny2b4kCjb8h0z6xrP1_wBhmJArNoSsz5Dp1UnlG7TpJ6aD9Z91G_adFHxtAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضا توسط ‌پژشکیان
@withyashar</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/withyashar/15208" target="_blank">📅 09:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15207">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دلار و طلا تا بفروشیم یا بالا میره؟ سوالی که اکثر مخاطبین کانال در چند روز اخیر می‌پرسند   اول پاییز اعلام کردیم که دلار تا اخر سال به ۱۹۰ هزا تومان می‌رسد و طلای ۲۲ میلیونی را به درستی همانند قبل پیشبینی کرده بودیم الان هم قیمت قطعی دلار و طلا تا پایان تابستان…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/15207" target="_blank">📅 03:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15206">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دلار و طلا تا بفروشیم یا بالا میره؟ سوالی که اکثر مخاطبین کانال در چند روز اخیر می‌پرسند
اول پاییز اعلام کردیم که دلار تا اخر سال به ۱۹۰ هزا تومان می‌رسد و طلای ۲۲ میلیونی را به درستی همانند قبل پیشبینی کرده بودیم
الان هم قیمت قطعی دلار و طلا تا پایان تابستان و بعد از آن را در کانال زیر اعلام کردیم ، حتما عضو شوید تا با آگاهی از قیمت دقیق در روزهای آینده تمام سرمایه گذاری های خود را مدیریت کنید و از تورم جا نمانید
👇
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/15206" target="_blank">📅 03:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15205">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0641a8394a.mp4?token=sQDx0_wFEqk0Mp6HgpF7oz3reCN_qWiuh0779TDOpLte3za5_P41cG61SHckfdudRUR7Hck5e70q856og7j4bEFhtZnc0HXj9pGg-bKeXdCFIdUsIQq3-BxE-AB1TpKkur9MHbuaKqqfrT2zOJvKUTLRk7SgO0viW7UvF1wpPfKv17xEZh9K1w-putGpfBWWmVYsGo92N8dxA47IStNDJW_JJRnQRNKVqYuKjVSHtN6YTvQGjasZmfHk5DIQn3xJfQZiy_Hl64cKe1iUVPjxDjjBkCVAxnZoFQePuREHlVY2_gy0RixeRfOnlJLQGYAYXygggoK1FBjh3cdukXskxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0641a8394a.mp4?token=sQDx0_wFEqk0Mp6HgpF7oz3reCN_qWiuh0779TDOpLte3za5_P41cG61SHckfdudRUR7Hck5e70q856og7j4bEFhtZnc0HXj9pGg-bKeXdCFIdUsIQq3-BxE-AB1TpKkur9MHbuaKqqfrT2zOJvKUTLRk7SgO0viW7UvF1wpPfKv17xEZh9K1w-putGpfBWWmVYsGo92N8dxA47IStNDJW_JJRnQRNKVqYuKjVSHtN6YTvQGjasZmfHk5DIQn3xJfQZiy_Hl64cKe1iUVPjxDjjBkCVAxnZoFQePuREHlVY2_gy0RixeRfOnlJLQGYAYXygggoK1FBjh3cdukXskxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعت ۳:۱۹  صبح امروز (کمی پیش) چند قایق متعلق به سپاه پاسدارن درحال اقدامی نامشخص در تنگه هرمز هستند.
ناو آمریکایی در بیسیم به زبان فارسی متنی هشدار آمیز را پخش می‌کند که می‌گوید:
جمهوری اسلامی کنترلی بر تنگه ندارد، عملیات را متوقف کنید و به بندر باز گردید، وگرنه نیروی دریایی ایالات متحده به کشتی شما حمله خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/15205" target="_blank">📅 03:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15204">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مذاکرات جمعه ایران و آمریکا در سوئیس الان قطعی نیست
بقایی، سخنگوی وزارت خارجه:
جلسه جمعه تا چند ساعت قبل قطعی بود ولی وقتی قرار شد روسای جمهور دو طرف (ایران و آمریکا) تفاهمنامه را امضا کنند، قرار شد درباره جلسه جمعه فعلاً تامل شود.
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/15204" target="_blank">📅 02:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15203">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/15203" target="_blank">📅 01:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15202">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">https://x.com/yasharrapfa</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15202" target="_blank">📅 01:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15201">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/15201" target="_blank">📅 01:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15200">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کاخ سفید:
ترامپ تفاهم‌نامه با ایران را امضا کرد
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15200" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15199">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">طبق گزارش Axios، رئیس‌جمهور ترامپ شخصاً نسخه‌ای از توافقنامه را در حین صرف شام با رئیس‌جمهور فرانسه ماکرون در کاخ ورسای امضا کرد.
عکسی از توافقنامه امضا شده به ایرانی‌ها و کشورهای میانجی ارسال شد.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/15199" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15198">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تسنیم: متن فارسی تفاهمنامه نیز به عنوان سند رسمی به امضای ایران و آمریکا رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/15198" target="_blank">📅 01:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15197">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0a3d37ce.mp4?token=i_gIDtJ7ig4f49bzpRJxC8YK-zxanqdGAj_sAKdRfiLTeRsuaDSq0L4xJtKrBL4dzh_EVFZI3MhToB3FfCgTjWNqCjjYDjju_bLC4QOoN2nadh6kFZaf49Sf8HnfL0xPh7o5lcCIBgqs0BQoCcRqxIysCjK-AvoBjMku_KLX-LSI__ERfE4mzIEH3muBcI-JjQeO0jJ6RcDAhsMq3Ac4VvQfcSrt0wtwM7_9MWkM1YP_QpXT7Ue8zbn1ote-rT3FEncIqowhGR0sszw7mzvUNL6kncEHqUpMp6QFn4898Q2e5ttFE5b5f4ewA84EIoYocaoSHd2gRWNrCLq0-1BJZrAk0c0gvHFkoWqEHoF0IAJuZmUXh-un7pW9rlwLjwK0Jho64T0qx-Z_q87GlQ7M-pUDpyhzaxUagrifAtlZJPDixC_dzAkrKYKVfuw6KoHW-Y_16L4YOWEn_eqgwOXXVJ9B651QxIxsOMgWy51hB04GoNbrSX6L-THYG6X723DddC-Sg5OL-NoqH5mdWKNUDiqTPvGQqM_oCMbVfiCFRFxBYH-PFrA7pejX_DULVA-kQ6VIez0jAcTjUDxzfrb9tPSFv1990KQPk4hSh9aX26sG7tZIspJjW2uoOimk1rkLrIG9a718Ky6jyYNNykZ_GwPuk6C7QexGfNHOcwP_08U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0a3d37ce.mp4?token=i_gIDtJ7ig4f49bzpRJxC8YK-zxanqdGAj_sAKdRfiLTeRsuaDSq0L4xJtKrBL4dzh_EVFZI3MhToB3FfCgTjWNqCjjYDjju_bLC4QOoN2nadh6kFZaf49Sf8HnfL0xPh7o5lcCIBgqs0BQoCcRqxIysCjK-AvoBjMku_KLX-LSI__ERfE4mzIEH3muBcI-JjQeO0jJ6RcDAhsMq3Ac4VvQfcSrt0wtwM7_9MWkM1YP_QpXT7Ue8zbn1ote-rT3FEncIqowhGR0sszw7mzvUNL6kncEHqUpMp6QFn4898Q2e5ttFE5b5f4ewA84EIoYocaoSHd2gRWNrCLq0-1BJZrAk0c0gvHFkoWqEHoF0IAJuZmUXh-un7pW9rlwLjwK0Jho64T0qx-Z_q87GlQ7M-pUDpyhzaxUagrifAtlZJPDixC_dzAkrKYKVfuw6KoHW-Y_16L4YOWEn_eqgwOXXVJ9B651QxIxsOMgWy51hB04GoNbrSX6L-THYG6X723DddC-Sg5OL-NoqH5mdWKNUDiqTPvGQqM_oCMbVfiCFRFxBYH-PFrA7pejX_DULVA-kQ6VIez0jAcTjUDxzfrb9tPSFv1990KQPk4hSh9aX26sG7tZIspJjW2uoOimk1rkLrIG9a718Ky6jyYNNykZ_GwPuk6C7QexGfNHOcwP_08U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بقایی: همین الان که در حال صحبت هستیم متن توافق رسما به امضا رئیس جمهور های دو طرف رسیده است
قرار بود که بامداد روز ۲۸ خرداد ماه رئیس جمهور دو کشور این متن و توافق رو امضا کنند.
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/15197" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15196">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15196" target="_blank">📅 00:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15195">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/15195" target="_blank">📅 00:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15194">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: ظرف ۴۸ ساعت آینده توافق با ایران امضا خواهد شد و احتمالا برای مدتی ارتش رو در خلیج فارس نگه خواهیم داشت.
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/15194" target="_blank">📅 23:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15193">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">@withyashar
Reeee</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/15193" target="_blank">📅 23:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15191">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مجری شبکه خبر : چرا ایران در روز آخر مذاکره حمله به اسرائیل را متوقف کرد؟
قالیباف: ما هر آنچه که می‌خواستیم با حمله بگیریم را چندین برابرش را با مذاکره گرفتیم. ساعت ۲ صبح ترامپ آتش‌بس را در کل لبنان داد و با آن ادبیات با نتانیاهو صحبت کرد.
قرار بود آمریکا محاصره را ظرف ۳۰ روز بردارد اما ترامپ گفت همین امشب محاصره را برمی‌داریم
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/15191" target="_blank">📅 23:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15190">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/15190" target="_blank">📅 23:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15189">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">۹. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند که تا زمان توافق نهایی وضعیت موجود را حفظ کنند؛ جمهوری اسلامی ایران وضع موجود را در برنامه هسته‌ای خود حفظ خواهد کرد، و ایالات متحده آمریکا هیچ تحریم‌های جدیدی علیه ایران وضع نخواهد کرد و نیروهای نظامی بیشتری را در منطقه مستقر نخواهد کرد.
@withyashar
۱۰. ایالات متحده آمریکا متعهد می‌شود بلافاصله با امضای این یادداشت تفاهم و تا زمان خاتمه تحریم‌ها، اسقاطیه‌های وزارت خزانه‌داری را برای صادرات نفت خام ایران، محصولات پتروشیمی و مشتقات آنها، و تمامی خدمات مرتبط شامل تراکنش‌های بانکی، بیمه‌ها، حمل و نقل و غیره صادر کند.
۱۱. ایالات متحده آمریکا متعهد می‌شود تا وجوه و دارایی‌های محدود یا مسدود شده جمهوری اسلامی ایران را با اجرای این یادداشت تفاهم به طور کامل برای استفاده در دسترس قرار دهد. ایالات متحده آمریکا و جمهوری اسلامی ایران در مورد روال مربوط به آزادسازی این وجوه در طول مذاکرات، به صورت دوجانبه توافق می‌کنند. این وجوه، چه در حساب اصلی نگهداری شوند و چه منتقل شوند، برای پرداخت به هر ذینفع نهایی که توسط بانک مرکزی جمهوری اسلامی ایران تعیین می‌شود، باید به طور کامل قابل استفاده شوند. ایالات متحده آمریکا متعهد می‌شود که تمامی تاییدیه ها و مجوزهای لازم را در این رابطه صادر کند.
@withyashar
۱۲. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند تا یک سازوکار اجرایی برای نظارت بر اجرای موفق این یادداشت تفاهم و پایبندی آتی به توافق نهایی تشکیل شود.
۱۳. پس از امضای این یادداشت تفاهم و منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ این یادداشت تفاهم و تداوم اجرای این اقدامات، جمهوری اسلامی ایران و ایالات متحده آمریکا مذاکرات درخصوص توافق نهایی را منحصرا در مورد بقیه بندها آغاز خواهند کرد.
۱۴. توافق نهایی با یک قطعنامه الزام‌آور شورای امنیت سازمان ملل متحد تایید خواهد شد.
(امضاء) از طرف دولت جمهوری اسلامی ایران
تاریخ
(امضاء) از طرف دولت ایالات متحده آمریکا
تاریخ
( امضاء) در حضور میانجی
از طرف دولت جمهوری اسلامی پاکستان
تاریخ
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/15189" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15188">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یادداشت تفاهم اسلام‌آباد بین جمهوری اسلامی ایران و ایالات متحده آمریکا
به گزارش تسنیم، متن تفاهم‌نامه ایران و آمریکا به شرح ذیل است:
جمهوری اسلامی ایران و ایالات متحده آمریکا، به طور مشترک و با حسن نیت، در تاریخ ۲۸ خرداد ۱۴۰۵ نسبت به موارد زیر توافق کردند:
@withyashar
۱. جمهوری اسلامی ایران و ایالات متحده آمریکا و متحدین آنها در جنگ حاضر، با امضای این یادداشت تفاهم خاتمه فوری و دائمی عملیات‌های نظامی را در تمامی جبهه‌ها، از جمله در لبنان، اعلام کرده و تعهد می‌کنند از این پس هیچ جنگ یا هیچ عملیات نظامی علیه یکدیگر آغاز نکنند و از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند و تمامیت ارضی و حاکمیت لبنان را تضمین کنند. توافق نهایی خاتمه دائمی جنگ در تمامی جبهه‌ها، از جمله در لبنان، و بقیه مفاد این بند را تایید خواهد کرد.
۲. جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌شوند که به حاکمیت و تمامیت ارضی یکدیگر احترام بگذارند و از مداخله در امور داخلی یکدیگر خودداری کنند.
@withyashar
۳. جمهوری اسلامی ایران و ایالات متحده آمریکا به انجام مذاکرات و حصول به یک توافق نهایی در مدت حداکثر ۶۰ روز، قابل تمدید با رضایت طرفین، متعهد می‌شوند.
۴. بلافاصله با امضای این یادداشت تفاهم، ایالات متحده آمریکا شروع به رفع محاصره دریایی خود و هرگونه مزاحمت یا ممانعت علیه جمهوری اسلامی ایران می‌کند، و ظرف ۳۰ روز به محاصره دریایی به طور کامل خاتمه خواهد داد. در طول این مدت، تردد کشتی‌ها متناسب با تعداد ترافیک قبل از جنگ که از سوی جمهوری اسلامی ایران برقرار می‌شود، خواهد بود. ایالات متحده آمریکا همچنین متعهد می‌شود تا ظرف ۳۰ روز پس از توافق نهایی، نیروهای نظامی خود را از حوزه پیرامونی جمهوری اسلامی ایران خارج کند.
۵. با امضای این یادداشت تفاهم، جمهوری اسلامی ایران ترتیباتی را با حداکثر تلاش خود برای عبور ایمن کشتی‌های تجاری، بدون هزینه فقط برای ۶۰ روز، از خلیج فارس به دریای عمان و بالعکس، اتخاذ خواهد کرد. تردد کشتی‌های تجاری بلافاصله آغاز، و با توجه به ضرورت رفع موانع فنی و نظامی و مین‌زدایی توسط جمهوری اسلامی ایران، ظرف ۳۰ روز برقرار خواهد شد. جمهوری اسلامی ایران با سلطنت عمان برای تعیین اداره آینده و خدمات دریایی در تنگه هرمز، مطابق با حقوق بین الملل قابل اجرا و حقوق حاکمیتی کشورهای ساحلی تنگه هرمز، گفتگو خواهند کرد و با دیگر کشورهای ساحلی خلیج فارس نیز تبادل نظر می‌کنند.
@withyashar
۶. ایالات متحده آمریکا متعهد می‌شود، با شرکای منطقه‌ای خود، برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران یک برنامه قطعی مورد توافق طرفین را با تامین حداقل ۳۰۰ میلیارد دلار ایجاد کند. سازوکار اجرایی‌سازی این برنامه، به عنوان بخشی از توافق نهایی ظرف ۶۰ روز نهایی خواهد شد. تمامی تائیدیه‌ها، اسقاطیه‌ها و مجوزهای مورد نیاز برای تراکنش‌های مالی مربوطه توسط ایالات متحده آمریکا ارائه خواهد شد.
۷. ایالات متحده آمریکا متعهد می‌شود به تمامی انواع تحریم‌ها علیه جمهوری اسلامی ایران، از جمله قطعنامه‌های شورای امنیت سازمان ملل متحد، قطعنامه‌های شورای حکام آژانس بین‌المللی انرژی اتمی، و تمامی تحریم‌های یکجانبه آمریکا، اعم از اولیه و ثانویه، برابر یک برنامه زمانی مورد توافق به عنوان بخشی از توافق نهایی، خاتمه دهد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوع خاتمه تحریم‌ها که در بالا ذکر شده است اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
۸. جمهوری اسلامی ایران مجدداً تایید می‌کند که سلاح هسته‌ای تولید یا ابتیاع نخواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت کرده‌اند که وضعیت مواد غنی‌شده ذخیره شده را از طریق یک سازوکار مورد توافق طرفین و مطابق با برنامه زمانی مندرج در بند ۷، حداقل به شیوه رقیق‌سازی در محل، تحت نظارت آژانس بین‌المللی انرژی اتمی، حل و فصل کنند. دو طرف همچنین موافقت می‌کنند تا در مورد موضوع غنی‌سازی، و دیگر موضوعات مورد توافق دو طرف مرتبط با نیازهای هسته‌ای جمهوری اسلامی ایران، بر اساس یک چارچوب رضایت‌بخش که در توافق نهایی مورد موافقت قرار خواهد گرفت، بحث کنند. توافق نهایی مفاد این بند را تایید خواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوعات هسته‌ای ذکرشده در بالا اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/15188" target="_blank">📅 22:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15187">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">طبق برخی گزارش ها نیروهای ارتش جولانی در سوریه برای ورود به لبنان و مبارزه با حزب اللّه آماده میشوند
🚨
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/15187" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15186">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شبکه خبر: انتشار متن تفاهم نامه ایران و آمریکا تا دقایقی دیگر
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/15186" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15185">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شبکه i24News اسرائیل:
متن رسمی یادداشت تفاهم ایران و آمریکا منتشر شده و طبق این توافق، همه درگیری‌ها از جمله در لبنان باید فورا متوقف بشه.
همچنین یک برنامه اقتصادی 300 میلیارد دلاری برای جمهوری اسلامی در نظر گرفته شده.
بر اساس گزارش، ذخایر اورانیوم با غنای بالای ایران داخل کشور و تحت نظارت آژانس رقیق خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/15185" target="_blank">📅 22:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15184">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15184" target="_blank">📅 22:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15183">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3f8b7f61.mp4?token=Kqium351hovlMo_IV89cLmtz6DpU5Ljw_3Yx3yAj6YAHqlVV2hYR7tsXg6JCuQ2PeFPNci6G32sHI5LdSQWm-UWZ4c5MUN25jWZA2tQCLo7DwDLn-vfAFLAHV1tioEx6k3FiBBW3WlxwiLrPMbqk_IqB1aIcgYPJ00obr4PBeDwdW8S-OzaTylOhKbTbj5Wn3aQAwl7CeNj7-TVdA74s_ub5qdFmSLZ8wLE3Qe5OWLw_TTYLt9FxMh8VvAMCdii_ivXRPZpgkOwOUqpUwm8Fdf3TZmxw4BcjfiCw2b7Bgy5nBw4UUdOvs4OoQ3MjWzU59AUv38rbgCRlkKBlFTPSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3f8b7f61.mp4?token=Kqium351hovlMo_IV89cLmtz6DpU5Ljw_3Yx3yAj6YAHqlVV2hYR7tsXg6JCuQ2PeFPNci6G32sHI5LdSQWm-UWZ4c5MUN25jWZA2tQCLo7DwDLn-vfAFLAHV1tioEx6k3FiBBW3WlxwiLrPMbqk_IqB1aIcgYPJ00obr4PBeDwdW8S-OzaTylOhKbTbj5Wn3aQAwl7CeNj7-TVdA74s_ub5qdFmSLZ8wLE3Qe5OWLw_TTYLt9FxMh8VvAMCdii_ivXRPZpgkOwOUqpUwm8Fdf3TZmxw4BcjfiCw2b7Bgy5nBw4UUdOvs4OoQ3MjWzU59AUv38rbgCRlkKBlFTPSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با هواپیما به سمت کاخ ورسای رفت، تا مکرون و رهبران کشوران اروپایی شام بخوره
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/15183" target="_blank">📅 22:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3ueHF48bRD_LMSKKcuUGgPlcsrqvxkuIlcoS8CUZ8EJJ4QiWWPAX7JtfnX8UqaEKJqu9FLX2YLDQkcbjkINnh0J0g8kDiDB2tXfbUmZOpAKEzz_CCiAwMcZbjdUdKTt0OuaXDBIDI5YWTv18i3q-kvmyxsyLTUdEMWA1tDwr86xhH5quNXC-LqJ6bAR-DNdTwXmELhxQD0uJZ6LCzIDBujm7oAdf6fqfTMOp77Xl4N7yBSzG9MC4x54v4EkqWStyCAQa78RcPHrXfrK4qv2oUb2JTV6f68x3GwlaxwBWbcxaQVXqL5H5EPqoQo0dLjTnR6Mph3b7hfU9vmJgeJQew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام: به نظر من امضای این تفاهم‌نامه به نفع آمریکا خواهد بود، چون تنگه هرمز شروع به بازگشایی میکنه و درگیری‌ها با ایران متوقف میشه.
اینکه آیا آمریکا میتونه با ایران بر سر برنامه هسته‌ای و سایر مسائل به توافقی قابل قبول و قابل راستی‌آزمایی برسه یا نه، هنوز مشخص نیست، اما من تلاش برای رسیدن به چنین توافقی رو کم‌هزینه می‌بینم.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/15182" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15181">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزارت امور خارجه ایران: ادامه اشغال جنوب لبنان توسط اسرائیل، نقض تفاهم‌نامه است و ما اقدامات لازم را انجام خواهیم داد
ایالات متحده متعهد شده است که تمام تحریم‌ها از جمله تحریم‌های شورای امنیت سازمان ملل را در یک جدول زمانی که در طول مذاکرات مورد بحث قرار خواهد گرفت، لغو کند
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/15181" target="_blank">📅 21:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15180">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
کانالی که ترور هنیه و نصرالله رو دقیق پیشبینی کرده بود، دلار ۱۶۰ تومنی رو هم دو ماه پیش اعلام کرده بود از تاریخ و نحوه حمله ایران به اسرائیل پرده برداشت!!!
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
🔴
LINK - CHANNEL
🔴</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15180" target="_blank">📅 21:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15179">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الجزیره به نقل از وزارت امور خارجه ایران: در حال حاضر در حال بررسی ایده امضای تفاهم‌نامه از راه دور توسط رؤسای جمهور ایران و ایالات متحده هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15179" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15178">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">معاون وزیر ارتباطات: اینترنت دیگر در شرایط بحران قطع نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/15178" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15177">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یک مقام کاخ سفید: نشست سوئیس برای مرحله بعدی بسیار مهم خواهد بود زیرا سند کنونی نیت‌های طرفین را منعکس می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15177" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15176">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرنگار: آیا اکنون می‌توانید بگویید که آیا کسی را در دولت خود به خاطر حمله به مدرسه‌ای که در اولین روز جنگ بیش از ۱۰۰ کودک را کشت، مسئول می‌دانید؟
پرزیدنت ترامپ:
این سوال عجیبی است که در این تاریخ پرسیده می‌شود، چون شما درباره زمانی صحبت می‌کنید که مدت زیادی گذشته است، اما کسی این کار را عمداً انجام نداد.
فکر می‌کنم باید درباره آن‌ها بگویید، چه می‌شود درباره هزاران سربازی که وقتی در ماشین خود را باز کردند منفجر شدند؟ چه می‌شود درباره هزاران نفری که توسط ایران کشته شدند؟
اشتباهات رخ می‌دهد، جنگ زشت است، می‌دانم که تحت بررسی است. از پیت هگستث این سوال را می‌پرسم زیرا آن‌ها آن را تحت بررسی دارند.
﻿
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/15176" target="_blank">📅 20:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15175">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_C_y44HU1hpq5MpB-GynrosDUgRxiUw4BvH_WhX7MOhTVpsKc4Mfz3xAytJrX1UBvjL7AJVAsx_lF6QvglOsXwzC5oRaBYqJg3UfuRMbSbnynoYniAygLwbWnA_5TUJHAjwdKFLKmlBZVkxjIhrPIJKS94ZbgPlDqwhElwAV3u4-8s9br731bJ_FobWHBd_OPrCPgArNokQE-00YebLR574vL05wb6Eag-ogqPfkqWPDN--bt-8wHySAhkBNFeKlW5f9JaNSgOykUVRSoawiqV912VMbL-bpoFyIwzVTVOAY9_zwvF177hVhQgylgv0XEIaJ2U86QxQgHOF05faMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از وقوع حادثه دریایی در نزدیکی سواحل یمن
گزارش‌های امنیتی از وقوع یک حادثه دریایی جدید در آب‌های نزدیک به یمن خبر می‌دهد.
گزارش شده قایق‌های تندرو و کوچک ناشناس، یک کشتی عبوری را در فاصله ۱۰۵ مایل دریایی شمال شرق عدن هدف قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15175" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15174">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15174" target="_blank">📅 20:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ : به آنها می‌گویم: شما احتمالاً سومین ذخایر بزرگ نفت در جهان را دارید، به چه دلیل به سلاح هسته‌ای نیاز دارید؟
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15173" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج فارس کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
کسی می‌گفت: شما نباید حتی یک موشک هم به آن‌ها بدهید برخی از این آدم‌ها را دوست دارم، اما فکر نمی‌کنم زیاد باهوش باشند.
می‌گفتند: جناب، شما نباید اجازه دهید آن‌ها هیچ موشکی داشته باشند. من گفتم: «خب، پس من باید چه کار کنم؟ آیا باید اجازه دهم عربستان سعودی موشک داشته باشد، اما آن‌ها نداشته باشند؟» گفتند: «بله جناب.»
اما نمی‌شود، کارها این‌طور پیش نمی‌رود، می‌دانید؟ این‌گونه کارساز نیست و موشک‌ها مشکل اصلی نیستند. موشک‌ها فقط به یک نقطهٔ کوچک آسیب می‌زنند، اما کرهٔ زمین را نابود نمی‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/15172" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ : رهبرهای جدید ایران آدم‌های باهوشین، خیلی هم باهوشن؛
به اندازه قبلی‌ها تندرو و افراطی نیستن، فکر می‌کنم واقعاً کشورشون رو دوست دارن و آدم‌های خوبی هستن.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/15171" target="_blank">📅 20:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15170">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: خب، آنها به سرمایه‌گذاری نیاز دارند، چون ما حدود یک و نیم تریلیون، شاید دو تریلیون دلار خسارت وارد کردیم.
پس کسی باید به آنها کمک کند خب، هیچ تضمینی برای کمک به آنها وجود ندارد، و ممکن است همسایگانشان کمی به آنها کمک کنند، نمی‌دانم، اما این مقدار زیادی پول است.
تقریباً هیچ‌کس چنین پولی ندارد این همان نوع خسارتی است که وارد شده است
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/15170" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15169">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: ما موظف نیستیم چیزی به ایران بدهیم، اما ممکن است برخی بخواهند آنجا سرمایه‌گذاری کنند.
آنها از یک نظر فرهنگی ابتدایی دارند، اما این فرهنگ ابتدایی نابغه است، آنها مردم بسیار باهوش و مذاکره‌کنندگان بسیار خوبی هستند
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15169" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15168">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0786cbbc7f.mp4?token=uivEic-0hOhts1KcykzgZ-qcTgahenF5KqcqZGKjAIIdqYfFQI47fQw1xGf1opHwEkoazsCE9Mjqil_u46wjfXRelmU1bICETz4L6d8SWRjwfiPI7F3UGDRhUvPMOeQSHB2GIQUDlxouNjDJe0xrCLsuVfb5A2GQi9nbsdp-BozlYCDfd2z6aHHRsIOz4t1VGWClABVJhkbVpBw4lGcMPCqF1H4WEKhEWr3k5e-fn2Yg7XUF4OUQiFA42153hYicwb8QbKEYs0uheO7AIDFi1LExze7W__Ks6aiI5dY25OiHIBL6uQwKMg3wRo58yAUn_YOIliCLM2k3AM93dIVVHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0786cbbc7f.mp4?token=uivEic-0hOhts1KcykzgZ-qcTgahenF5KqcqZGKjAIIdqYfFQI47fQw1xGf1opHwEkoazsCE9Mjqil_u46wjfXRelmU1bICETz4L6d8SWRjwfiPI7F3UGDRhUvPMOeQSHB2GIQUDlxouNjDJe0xrCLsuVfb5A2GQi9nbsdp-BozlYCDfd2z6aHHRsIOz4t1VGWClABVJhkbVpBw4lGcMPCqF1H4WEKhEWr3k5e-fn2Yg7XUF4OUQiFA42153hYicwb8QbKEYs0uheO7AIDFi1LExze7W__Ks6aiI5dY25OiHIBL6uQwKMg3wRo58yAUn_YOIliCLM2k3AM93dIVVHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما یک نسخه از توافق ایران را به اسرائیل ارسال کردیم
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/15168" target="_blank">📅 20:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15167">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: من با نتانیاهو در مورد لبنان اختلاف نظر داشتم و به او گفتم که مودبانه رفتار کند
نتانیاهو گاهی اوقات کمی از کوره در می‌رود، اما من با او همکاری بسیار خوبی دارم
ما به احتمال زیاد توافق را امضا خواهیم کرد و ایران خواهان آن است؛ آنها به طور مناسب عمل کرده و موافقت کرده اند که سلاح هسته ای تولید نکنند
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/15167" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15166">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: من توافق کردم چون نمی‌خواستم شاهد یک فاجعه اقتصادی باشم.
دو روز گذشته به شدت دشوار بوده است، و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافقی نرسیم، بمباران آن‌ها را برای شب دوم از سر خواهیم گرفت
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15166" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15165">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmc0zDkN9WtdlykrlnUs_Vpup5vHRGH8fbbDDA3sdTVbwDuHpn0JhRNNkb0mzV9eg-zNTgrPSkNpo619ohOB0jJlBb3aYC7c9-9UQK_Sj3SfhhwHoB2HSRdt29MMKgxvKgGBa7AhT6R1yS_OxYt-Lv9PUsTHkGbsNFLHm9UJ__FSyR3kPssaeKdXNH_4JAcszL6xnFgBY7eJEJJlvRYofNVU13n6fTEfAf5WvpxEE1bxdZWSeDsbT2w0cr2jIhdbjh2PLIm3sDXkBfyEFH0hCo2MOX9VHxKN6edKTBKXocH61lk846OfMJV_oD00BgSsLCG342VAaCNUrIyAa4hMuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت ژورنال دارایی‌های مسدود شده ایران را اعلام کرد:
چین: ۲۰-۵۰ میلیارد دلار (بزرگ‌ترین)
قطر: ۲۰-۵۰ میلیارد (شامل ۶ میلیارد بشردوستانه)
عراق: ۱۵ میلیارد (برق و گاز)
هند و کره جنوبی: هرکدام ۷ میلیارد
ژاپن: ~۳ میلیارد
آمریکا: ۲ میلیارد
لوکزامبورگ و عمان: مبالغ کمتر
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/15165" target="_blank">📅 19:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15164">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آکسیوس: حتی اگر زمان امضا تغییر کنه، نشست هیئت‌های آمریکا و ایران به ریاست جی‌دی ونس و محمدباقر قالیباف طبق برنامه روز جمعه در سوئیس برگزار خواهد شد.
انتظار میره دو طرف درباره آغاز مذاکرات پیرامون برنامه هسته‌ای ایران گفت‌وگو کنند.
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15164" target="_blank">📅 19:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آکسیوس
: دیدار هیئت مذاکره کننده ایرانی و آمریکایی در روز جمعه در سوئیس برای امضای یادداشت تفاهم نامه به احتمال زیاد برگزار نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15163" target="_blank">📅 18:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یک منبع نزدیک به تیم مذاکره کننده به تسنیم گفت:
سفر تیم مذاکره کننده به سوئیس در روز جمعه لغو نشده است اما جزییات ترتیبات مربوط به امضای تفاهم نامه همچنان در حال رایزنی است و هنوز هیچ جزییاتی در این باره(چگونگی امضای تفاهم) نهایی نشده است.
@withyashar
اگه تسنیم میگه پس یه خبرهایی هست داره لغو میشه
🤣</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/15162" target="_blank">📅 18:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15161">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئیس جمهور فرانسه، مکرون پیرزن باز:
من فکر می‌کنم توافق ترامپ با ایران توافق خوبی است.
البته که همه چیز را فوراً حل نمی‌کند، نه.
اما اگر ما به جنگیدن ادامه می‌دادیم، این به چه معناست؟ این به معنای بسته ماندن تنگه هرمز بود.
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/15161" target="_blank">📅 18:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ: من وارد توافق‌هایی شده‌ام که ۱۰۰ درصد قطعی بودند، اما عملی نشدند؛ وارد توافق‌هایی هم شده‌ام که هیچ شانسی برای انجام‌شان وجود نداشت، اما اتفاق افتادند؛ فکر می‌کنم توافق [با ایران] انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15160" target="_blank">📅 18:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Parandeh (IG @yashar)</div>
  <div class="tg-doc-extra">Martik (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/15159" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/15159" target="_blank">📅 18:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: اگر ایران یادداشت تفاهم را تکمیل نکند، دوباره به نقطه شروع برمی‌گردیم
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15158" target="_blank">📅 18:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15157">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اخبار اولیه‌ای و تأیید نشده‌ مبنی بر لغو امضای جمهوری اسلامی برای یادداشت تفاهم در روز جمعه، به دلیل حملات به لبنان.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/15157" target="_blank">📅 18:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15156">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK_Ol_TolukguOwqhctciccQoVwhvzZ-UK0F6DvCnGsOvfyEOENAfuIhBUdWfMvuGqBnaMkEM0lZ9DqBaeHBT6ktoy-tIACJ9GowmFAnic7ju2FpmSiDey0YIChZo65pCyrzWmYpTAbR84QF90p58jRmjylje8gSdg3TplHOktHvPeM57AOkGY97kQ1KkMdx5cXYn17AIf46JA16vfoEYLhR3EVUBAfPUrX-Wgmm0ZiDEL38xtFft-fcJEGA7wnY0pXEY8y0sx4F4AWlJVDLyqezRLnwa3ChrVq84gpJ5VzZ8eLdvVM2_aZtIi5Q8RE4M71IB98aH67RijdgdyDEhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : من در عرض ۴۵ دقیقه از فرانسه یک کنفرانس خبری برگزار خواهم کرد. سپس به ورسای برای صرف شام با رهبران فرانسوی و دیگر رهبران اروپایی خواهم رفت و بعد از آن امشب به خانه بازمی‌گردم!
این سفر یک موفقیت بزرگ بود، اما عمدتاً چیزی که همه می‌خواستند درباره‌اش صحبت کنند این است که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد!
شاخص‌های عظیمی در همه بخش‌ها برای اقتصاد ایالات متحده وجود دارد، به طوری که امروز بیشتر از همیشه افراد مشغول به کار هستند.
بیش از ۱۹.۱ تریلیون دلار در آمریکا سرمایه‌گذاری شده است، با تمام کارخانه‌ها و سایر موارد، اما نکته مهم این است که شاخص‌های اخیر بازار سهام به دلیل توافق افزایش یافته‌اند و به همین ترتیب، قیمت نفت به سرعت در حال کاهش است!
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/15156" target="_blank">📅 17:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15155">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">️جی‌دی ونس: برخی افراد فقط می‌خواهند بمباران ادامه یابد، صرف نظر از اینکه آیا برای آمریکایی‌ها دستاوردی دارد یا خیر.
ترامپ سعی در ایجاد بدبختی برای مردم ایران ندارد
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15155" target="_blank">📅 17:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15154">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اسرائیل پرچم خود را در منطقه‌ای از سوریه برافراشت
منابع خبری در سوریه از نفوذ نظامیان ارتش اسرائیل به روستای «القحطانیه» در استان قنیطره خبر دادند و پرچم خود را برفراشتند
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/15154" target="_blank">📅 17:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15153">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانال ۱۳ اسرائیل: آمریکا جزئیات توافق با ایران را از اسرائیل مخفی نگه داشته، زیرا نگران است که تل‌آویو محتوای آن را فاش کند و کارزاری رسانه‌ای علیه آن به راه بیندازد
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/15153" target="_blank">📅 17:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15152">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پاکستان خواستار تعویق انتشار متن تفاهم‌نامه شد
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در گفت‌وگو با CBS اعلام کرد که طرف پاکستانی درخواست کرده است متن کامل یادداشت تفاهم (MOU) فعلاً منتشر نشود.
وی بدون ارائه جزئیات بیشتر گفت که به درخواست پاکستان، متن این سند به‌طور موقت محرمانه باقی خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15152" target="_blank">📅 17:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15151">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سوئیس: امضای یادداشت تفاهم ایران و آمریکا با حضور نمایندگان ۴ کشور ایالات متحده، ایران، قطر و پاکستان برگزار خواهد شد.
بیش‌از ۲۰۰۰ سرباز امنیت محل امضا را تأمین خواهند کرد و برای تضمین امنیت، منطقه پرواز ممنوع اعمال خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/15151" target="_blank">📅 16:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15150">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تسنیم: اختلال خدمات بانکی ادامه دارد , تجهیزات شبکه فرسوده هستند
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15150" target="_blank">📅 16:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15149">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایران امروز یک تفاهم‌نامه با شرکت سهامی خاص هلی‌کوپترهای روسی برای ۲۰ هلی‌کوپتر سری mi-8/17 امضا کرد (۴ تا از آن‌ها قبلاً قرارداد بسته شده است) که باید تا مارس ۲۰۲۷ تحویل داده شوند تا برای مقاصد اطفاء حریق، انتقال پزشکی و نجات استفاده شوند
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/15149" target="_blank">📅 16:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15148">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff486d39a.mp4?token=j5UXQFPvFImS-JA7tRieRPGsBU4ToZm_RXWfe2NI4BdOs_kW95copVjemBRH7zgCA7ZYFnxKcHswWdx__hRl2-_CDTi343gg6eGKSBbL_yScal07np-aql06GrXZfctX9WuhQUymaEOckexiHvpoBbCdYqYk0gJj3aJ_UFZM1BeSiKWH45xBF8db_H2FfIHuvGsSa5RYI2I4aW0ZiKZ-Bj492P_yV6piRh16MG4o2OjXeICwg4BWqGiXJLs-8bg1ooLf_rzbOV4w-FMIxD7_JyL4iaRehZgtAtPdwx_I-rn7_i32P9n1AYXE9nrjLuIh2c6U8rlzou9yQKLRllJeD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff486d39a.mp4?token=j5UXQFPvFImS-JA7tRieRPGsBU4ToZm_RXWfe2NI4BdOs_kW95copVjemBRH7zgCA7ZYFnxKcHswWdx__hRl2-_CDTi343gg6eGKSBbL_yScal07np-aql06GrXZfctX9WuhQUymaEOckexiHvpoBbCdYqYk0gJj3aJ_UFZM1BeSiKWH45xBF8db_H2FfIHuvGsSa5RYI2I4aW0ZiKZ-Bj492P_yV6piRh16MG4o2OjXeICwg4BWqGiXJLs-8bg1ooLf_rzbOV4w-FMIxD7_JyL4iaRehZgtAtPdwx_I-rn7_i32P9n1AYXE9nrjLuIh2c6U8rlzou9yQKLRllJeD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: دلیل پایین ماندن قیمت نفت این است که هر شب کشتی‌هایی را از بین می‌بردیم که حتی شما از آن‌ها خبر نداشتید.
دو روز پیش، سه روز پیش، یک ماه پیش، ۲۲ کشتی را از بین بردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی را از بین می‌بردیم. هیچ‌کس این را نمی‌دانست.
نیروی دریایی ما کار بزرگی انجام داد. هیچ‌کس نمی‌دانست چه اتفاقی می‌افتد. به همین دلیل نفت به ۳۰۰ دلار در هر بشکه نرسید؛ بلکه به ۱۲۵ تا ۱۵۰ دلار رسید.
حالا قیمت آن ۷۲، ۷۳ دلار است. شنیده‌ام که الان حتی کمتر از این است
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/15148" target="_blank">📅 14:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15147">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ: با احمد الشرع، رهبر سوریه، درباره مقابله با حزب‌الله گفت‌وگو کردم.
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/15147" target="_blank">📅 14:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15146">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10b0e16f.mp4?token=ruwOWzNoubn2AY9ZKoRSmHGFWtNwSeplBG8VKE4lNZ1X5yml7m0dXAicqRQHnPuYVYB_qcvzHcEMAid89kfhJ77qVLkKltk_wzDYSyoMd_2p2aRhK1h0K9jft2jv3X9t8EcZSihfc7MT_ENRZzEux3hjyBBw8oLDDYIPiEpkwv4tOpcQKr6IBRuRWIN0s7FIfmz5Yh5NuPQT51WOcDC-92okZPHMM-rLuI8y5P6TaKtNiPZ7n6C5gNa28RGxaG_QIhHUNiI6GEI9zlwII3vO6osOrte8VFGHhPe_O4GVCP7UccMZPzZ_fbRnE4L-mK3b4X2DlAWchwMiG-kG2SRLjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10b0e16f.mp4?token=ruwOWzNoubn2AY9ZKoRSmHGFWtNwSeplBG8VKE4lNZ1X5yml7m0dXAicqRQHnPuYVYB_qcvzHcEMAid89kfhJ77qVLkKltk_wzDYSyoMd_2p2aRhK1h0K9jft2jv3X9t8EcZSihfc7MT_ENRZzEux3hjyBBw8oLDDYIPiEpkwv4tOpcQKr6IBRuRWIN0s7FIfmz5Yh5NuPQT51WOcDC-92okZPHMM-rLuI8y5P6TaKtNiPZ7n6C5gNa28RGxaG_QIhHUNiI6GEI9zlwII3vO6osOrte8VFGHhPe_O4GVCP7UccMZPzZ_fbRnE4L-mK3b4X2DlAWchwMiG-kG2SRLjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ‌ در‌کنار ژنرال السیسی (واقعی): فراموش نکنید، هیچ‌کس هرگز به اندازه من با ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری از افراد دیگر انجام می‌شد.
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/15146" target="_blank">📅 14:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15145">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ: قابلیت پرداخت فقط یک حقه دیگر است. آنها کلمه «قابلیت پرداخت» را ساختند
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/15145" target="_blank">📅 14:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15144">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ: یادداشت با ایران نهایی نیست. اگر از توافق خوشمان نیاید، دوباره به بمباران بازمی‌گردیم @withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/15144" target="_blank">📅 14:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15143">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: یادداشت با ایران نهایی نیست. اگر از توافق خوشمان نیاید، دوباره به بمباران بازمی‌گردیم
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/15143" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15142">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLvyZ3_WfH_X3ZQ-vPaMjHR-n_nXbimsQXOYHEB-ux3erD_N6L3eiSgBN6qheoOaUM4n7p3F3N8NXRmF5u6hPY1VEDQAUvUw4kv_iFLmDUZdnvFG2MvdJoAs-Q_yVsy2WOXWJXT85dCCfOMxGxEUUMIt5zMMhfTqvT-e0vD3FK-b6DUdud3QKWG2ATRm_IXDnmJ0PRN2ambnkjeIBstKbni1wB0IrwzG1Tnab8vsi_zqU-v5PQebGBVxNU3KjWg_w3kqP5OLDKCHq1kg9My_uRk4ivUdpRfs1GkRZL52Oz1Xi-Rt_uLhXbksaaPVvqI_bRC8q587ByO0HNnl7Se3mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندرو تیت که ۱۰۷ بار لیکویید شده، دوباره در صرافی هایپرلیکویید با اهرم ۴۰ و حجم حدوداً ۴ میلیون دلار، روی بیت‌کوین پوزیشن لانگ (خرید) باز کرده و باز هم بخشی از سرمایه‌اش (۱.۳۵ میلیون دلار) لیکویید شد.
اگه قیمت به 64,626 هزار دلار برسه کامل لیکویید می‌شه.
نرخ فعلی بیت‌کوین: 64,800$
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15142" target="_blank">📅 14:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15141">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d627cfcdc.mp4?token=VKizGYFrFv9eQVAGCoxFhC6C7zfkXgn2vb7TPTqpTVCXTwYB0h973tethMKxiTSRe2o0dtWACqSZ6721wGJgCswfzRwxIt3HGSlEb3w9KjBHN2xVDKozNBOg1xuc7ertobDe6RuhOoRGBmy6BQ0nw_7kIQ7cPYlKiCnAgZvSux92mRJ1uAG1l9PsJbj5hO7cPZodWqEdJHs-oEx9zIatvbebgDhy5SWBuJoxNS6NJl3yzB69TOhTzPCBBWMj9bhQFVgBFyr-xVgH43lblqmgDQh5ysayzcEh2saUVReKVdPBtGwNxy5Ziev2__8Ok9LpdkgMCOaS8X_8IyCKjzMyHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d627cfcdc.mp4?token=VKizGYFrFv9eQVAGCoxFhC6C7zfkXgn2vb7TPTqpTVCXTwYB0h973tethMKxiTSRe2o0dtWACqSZ6721wGJgCswfzRwxIt3HGSlEb3w9KjBHN2xVDKozNBOg1xuc7ertobDe6RuhOoRGBmy6BQ0nw_7kIQ7cPYlKiCnAgZvSux92mRJ1uAG1l9PsJbj5hO7cPZodWqEdJHs-oEx9zIatvbebgDhy5SWBuJoxNS6NJl3yzB69TOhTzPCBBWMj9bhQFVgBFyr-xVgH43lblqmgDQh5ysayzcEh2saUVReKVdPBtGwNxy5Ziev2__8Ok9LpdkgMCOaS8X_8IyCKjzMyHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎بخشی از سخنرانی قالیباف که تو رسانه‌ها وایرال شده
دیگه ساختار مدیریتی کشور از فردمحوری خارج شده و گروهی تصمیم میگیریم.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/15141" target="_blank">📅 14:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15140">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزیر دفاع اسرائیل کاتز: تمام روستاهای نزدیک به مرز لبنان به صورت سیستماتیک ویران می‌شوند.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15140" target="_blank">📅 14:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15139">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فاکس نیوز: ترامپ به زودی درباره توافق ایران کنفرانس خبری برگزار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/15139" target="_blank">📅 14:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15138">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تسنیم: متن توافقنامه به صورت کامل در روز جمعه و پس از امضا منتشر خواهد شد
یک منبع نزدیک به تیم مذاکره‌کننده   گفت: تفاهمنامه همانطور که پیشتر اعلام شده ۱۴ بند است و موضوعات مربوط به ۱۴ بند نیز بارها در رسانه‌ها مطرح شده، اما جزییاتی که در بلومبرگ‌ درباره هر بندی آمده است در موارد قابل توجهی ناقص است.
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/15138" target="_blank">📅 12:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15137">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRJhhg01x353xk_oMmnFmjYDI6jqNkiLHlRxQgvhtGmTAljUIQ2dqW1bSb_ydFIwiLyhq9p2jGVAkkGlQVelzKLx3bXsplFoOyFBfqCXiQbCjNw8sQbOjG8CtLIH7DWOnSfO_LEaFt53HltCxZT_8Md7pIoDtiRNEnICFZ9LvV03XzkI_OOuWIjIesVxfqeWOcgDp0OrR_Oz9RMcC5MStgmbKvE-h8xcVxBw9ZJSNJI-u0qRKfgGjH-ZXa9in_v6ac7jiI2Gwcb4u_F2IZq2nNvcJYXK8fGLPmXbYDLky8PhMUhnyXzIN_xAj4us70jZYTqteZl4BcSsnDbzrjuI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودرو پورشه سردار آزمون در کرمان توقیف شد
به گزارش تابناک به نقل از ایسنا، سرهنگ اکبر نجفی ۲۶ در تشریح این خبر گفت: خودروی مذکور که به دلیل تخلفات قانونی و برابر با احکام صادره در لیست توقیفی‌های مصادره اموال سردار آزمون قرار داشت، توسط گشت‌های محسوس و نامحسوس یگان امداد شناسایی و پس از طی مراحل قانونی، به پارکینگ منتقل شد.
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/15137" target="_blank">📅 12:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15136">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صدای انفجار‌ سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15136" target="_blank">📅 12:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15135">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بلومبرگ به نقل از یک منبع آگاه اعلام کرد: واشنگتن شروع به توزیع محتوای تفاهم با ایران به کشورهای متحد در اجلاس گروه ۷ در فرانسه کرده است
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/15135" target="_blank">📅 12:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15134">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری فرانسه: یک گزارش حقوقی دولت آمریکا نشان می‌دهد ارتش این کشور از ابزار هوش مصنوعی گروک متعلق به شرکت اسپیس ایکس تحت مالکیت ایلان ماسک، میلیاردر حوزه فناوری در جنگ علیه ایران استفاده کرده است
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/15134" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15133">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پمپئو وزیر خارجه سابق به فاکس  می‌گوید اگر برداشت ایران از موضع آمریکا درست باشد و تصمیم‌گیران اصلی (سپاه و رهبری) واقعاً تغییر رفتار بدهند، می‌توان به عادی‌سازی و حتی ورود سرمایه‌گذاری فکر کرد، اما احتمال چنین تغییری را بسیار پایین می‌داند. او تأکید می‌کند نباید هیچ پولی—چه مستقیم، چه از طریق واسطه یا حتی
آزادسازی دارایی‌ها—به ایران داده شود، چون به‌جای رفاه مردم، صرف تقویت برنامه موشکی، سپاه و خرید تسلیحات از روسیه و چین می‌شود. در عین حال می‌گوید اگر واقعاً تغییر واقعی رخ دهد، از آن استقبال خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/15133" target="_blank">📅 10:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15132">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsPUIwfB3z29sgAxTLvlBq3Z6Bf5ytadtZISLQVRywAmXq6kWKqEqY-dXK26M0IBcjwV_MNdYoaiz3XnN-RdU1v9tyWNNlrPNHiP0HHGn81B16Ykewp2mNt7uB4jnHqUsraRS2U3c9b26EOiZhplzo2uFckLqsIq8v28xVvbfU9RR_tx07ZGq3kay4N1R38fXg4sW6d85SDU8ZcGAMUuzyAnvatiKYO_vWIFbTamrGltzdJ1l-Uzs59YoOZ-KVY-4xNoL_eKoyl7YWp-N3JNjRvGCR7E6CdSqhnvMzqWkYpaerukTDeR0Y7H4let-Z2vICxADCmrTUqVNiwlDWfMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ایرباس موقت ایر فورس وان که توسط قطر اهدا شده، رنگ‌آمیزی شده و در نیویورک آماده است — درست همزمان با تعهد سرمایه‌گذاری ۱ میلیارد دلاری قطر که دیروز اعلام شد، بعد از آنچه برخی آن را تسلیم کامل آمریکا در برابر خواسته‌های قطر و ایران می‌دانند.»
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/15132" target="_blank">📅 10:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15131">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یديعوت احرونوت ادعا کرده بالای ۵۰درصد از پول‌های بلوکه شده ایران دست چین و عراقه
رقمش هم کم نیست؛ حداقل ۳۵میلیارد دلاره!
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/15131" target="_blank">📅 10:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15130">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرنگار اسرائیلی : این یک اشتباه تاریخی است.
پرداخت میلیاردها دلار به بزرگترین حامی دولتی تروریسم در جهان، فقط باعث تأمین مالی راکت‌های بیشتر، پهپاد‌های بیشتر و حملات بیشتری علیه اسرائیل و غرب خواهد شد. این سیاست «آمریکا در اولویت اول» نیست.
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/15130" target="_blank">📅 10:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15129">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c657925428.mp4?token=KX_d3cpslxhs7UUHbCPsDCAVxNY4IEnEQ71GL0BjerufBa-iQg784ygdWjHkUBxlD58nrVh_fZBvJLglbM4AS_5NESkbYEopOGLOLX52Fs0FwyT_ZNtLisXWATdtkHdIul5Gb24JeEUIX1VspVzbYiEbQL2Hd2jSyaXHy0lfEDNxyHJ1v5f51Cd0oFF0km2UKmj6L1i8FYG2R2YamIpV_77BKYBRIpp-LJKTn3P9szx6rvcEXDpd5kkvUK-1NiXlW5ouNAg7otd5lDzTWokeEuAZmUNTe0DplPNtzrX_QWpZL3hGfUfqY9JQB2GvAY1RoKMRjKGS5IYjRl_xuXBwVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c657925428.mp4?token=KX_d3cpslxhs7UUHbCPsDCAVxNY4IEnEQ71GL0BjerufBa-iQg784ygdWjHkUBxlD58nrVh_fZBvJLglbM4AS_5NESkbYEopOGLOLX52Fs0FwyT_ZNtLisXWATdtkHdIul5Gb24JeEUIX1VspVzbYiEbQL2Hd2jSyaXHy0lfEDNxyHJ1v5f51Cd0oFF0km2UKmj6L1i8FYG2R2YamIpV_77BKYBRIpp-LJKTn3P9szx6rvcEXDpd5kkvUK-1NiXlW5ouNAg7otd5lDzTWokeEuAZmUNTe0DplPNtzrX_QWpZL3hGfUfqY9JQB2GvAY1RoKMRjKGS5IYjRl_xuXBwVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک پنس، معاون سابق ترامپ: «به نظر من بهتر است به نیروهای مسلح ایالات متحده اجازه دهیم کار را تمام کنند، تنگه را باز کنند و قابلیت‌های تهاجمی ایرانیان را از بین ببریم و به مردم ایران فرصتی واقعی برای آزادی بدهیم.»
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15129" target="_blank">📅 10:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15128">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چند ساعت پیش، دونالد ترامپ با استناد به قانون تولید دفاعی (یک قانون از سال ۱۹۵۰ در دوران جنگ سرد)، دستور داد تا تولید مهمات، موشک‌ها و تجهیزات دفاعی آمریکا سریع‌تر شود. این فرمان در ۱۱ ژوئن به وزیر دفاع پیته هگست ارسال شد و مشکلات سیستمی در صنعت مهمات را هدف گرفت: ظرفیت تولید محدود، زنجیره‌های تأمین ضعیف، وابستگی‌های طولانی‌مدت و گلوگاه‌های تولید.
هدف اصلی: تسریع تولید مهمات حیاتی، موشک‌ها و تجهیزات دفاعی برای دفاع ملی آمریکا.
نحوه اجرا: قانون به ترامپ اجازه می‌دهد با شرکت‌های خصوصی توافق‌های داوطلبه ایجاد کند، تولید را اولویت‌دار کند و زنجیره‌های تأمین را تقویت نماید.
توافق مهم: شرکت لاکهید مارتین اعلام کرد با دولت آمریکا برای چهار برابر کردن تولید مهمات حیاتی به توافق رسیده است.
دلیل اقدام: کاهش ذخایر تسلیحاتی آمریکا پس از جنگ با ایران و استفاده از مهمات در ایران و ونزوئلا، که باعث افزایش سفارشات مهمات شد.
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/15128" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15127">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBiweBMA7AUxTD_TZaZhAoYTGeEbjvxLJCar7PtNmUY3ZrsKWdG8_GUErtQYXHOW8BB4EZ1Ie53K_nfXN9mTw4sA2fwcr8dTaAlrilX0baMdjd9oYuFXflDxTiaG4kdzgx2wjFBCm8gh0Ve6bQrCeUPsp-xs_AKOfK_YI-DXgMREF-kK-SW8fBcA-gEoISSM6Je3upJOWotxRZv8REuf9yUvPhcE6F4KiLjxbXTOLKROtqIFjzk1-WnNxAv5eYBgOhAk22516WqYIi01y1dAUsPrtEMSwdyIhrZph5W8YJMKv_4tFUnYdoAJAEwq1IzBrG7fZ2r5-r9M1tm2mARtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️ارتش اسرائیل اعلام کرد یک انبار تسلیحات جدید حزب‌الله حاوی ۵ تن مواد منفجره و ده‌ها پهپاد انتحاری را کشف کرده است
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15127" target="_blank">📅 09:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15126">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15126" target="_blank">📅 09:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15125">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تنکر ترکرز: ۳.۸ میلیون بشکه نفت خام ایران از محاصره آمریکا عبور کرد   تارنمای تنکر ترکز بامداد چهارشنبه گزارش داد، دو ابرنفتکش ایران که مجموعا حامل ۳.۸ میلیون بشکه نفت خام هستند، از محاصره آمریکا عبور کردند @withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/15125" target="_blank">📅 09:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15124">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرنگار العربیه: جنگنده‌های اسرائیلی دو بار به شهرک‌های «انصاریه» و «المنصوره» در جنوب لبنان حمله کردند.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15124" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15123">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بلومبرگ: به گفته مقامات آمریکایی، معافیت فروش نفت ایران فقط شامل محموله‌های نفتی می‌شود که قبلاً بارگیری شده است و شامل مجوز گسترده‌تر برای از سرگیری فروش نفت ایران نمی‌شود @withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15123" target="_blank">📅 08:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15122">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15122" target="_blank">📅 08:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15121">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، با بازنشر گزارشی از شبکه 14 اسرائیل درباره کشتار دی‌ماه، در ایکس نوشت:
«قربانیان سرکوب در ایران و خانواده‌های آن‌ها شایسته حقیقت، شفافیت و پاسخگویی هستند. جامعه بین‌المللی نباید در برابر این وضعیت بی‌تفاوت بماند.»
او گفت: «تاریخ حکومت ایران با رنج مردم خود نوشته شده است؛ اتاق‌های شکنجه، گورهای دسته‌جمعی، ناپدیدسازی اجباری و خانواده‌هایی که بدون پاسخ رها شده‌اند.»
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15121" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15120">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">منابع عربی: اسرائیل حومۀ شهرک نبطیه‌الفوقا در جنوب لبنان را هدف حملات قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/15120" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15119">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وبسایت خبری سمافور: مارکو روبیو، وزیر خارجه دولت ترامپ با انعقاد یادداشت تفاهم نامه با ایران مخالفت کرده و هیچ اظهار نظری درباره رسیدن به توافق با ایران نمی‌کند.
وزیر خارجه آمریکا امیدی به رسیدن به توافق هسته‌ای در مذاکرات با ایران پس از امضای یادداشت تفاهم نامه ندارد و تاکنون درباره امضای یادداشت تفاهم نامه با ایران کاملاً سکوت کرده است
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/15119" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15118">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9ZEtN4ayeje2KLZCy6S2VFB1jpW9eNxHZIN_JH415ASWLqaM6nI_fDDNmeo7eQ0LVPW3YVI0FpJSl91kd4CWWMbdRpx9Rkdxeq-4oGYHDXiN4XCRhsKehRpOD9CZ83VRuQSVhI32m7eUenwiby5-SF9F4b9O93a-amUTNV0HXI63oFHAR2XLCeGrBKSlZM8_LChuOSyaKLLy6_ofHbGh6tcXwhOiIfAlTweKYmyiu7noLDeqNtcvpZWfZEWABlm5FX-AGKceS92L9_W61Ye99mqqiL-At64BjcbrscShdFYahdi5UEKG2pbrSVsdNUczlm8o6hhfbGdDdeKSLBZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: به گفته مقامات آمریکایی، معافیت فروش نفت ایران فقط شامل محموله‌های نفتی می‌شود که قبلاً بارگیری شده است و شامل مجوز گسترده‌تر برای از سرگیری فروش نفت ایران نمی‌شود
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/15118" target="_blank">📅 08:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15117">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdwiDy2m6K7STajp2tKIOiiJ1bAczdB1meCpRxx7A2bj1RkwSKySukhxQWSH1Xipc1rvN7nTelhwM5uP8J8-53zMMIzN0rEYSTUlPiVyXX0o9WGiw8PpLVA8CL1Hvatn9mXMHdeCguJn6077OUgjhKnASxRwc0qNmaUq8dYZYhFx65Zbnw8bPbYlznQVql0RUNhrTY8A34uMgU6ys4mzjXGJ2_2Zv4i0ObzrtcXp-BYzX2JCUSeUNGZ8uMxKxO2_Q_RjPUK9Jmx9xaaUQQAf_IPLKyDQulUfdrpze5JuE17IuOcLhnp0W9LqpACjSk_XnlhuI4O4KHlU-BRZfDzk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید:
«نه سلاح هسته‌ای، نه لغو کامل تحریم‌ها, نه پول»
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15117" target="_blank">📅 08:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15116">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
اگه میخوای بدونی قیمت دلار طلا خودرو .... درسال جدید چقدر میشه این چنل تمام پیشبینی ها همراه تاریخ وقوع رو گفته
🕯
@link
🕯
🕯
@link
🕯
🕯
@link
🕯</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/15116" target="_blank">📅 02:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15115">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr1cVj3GaOcykWgbHNSW5sTTDdEOZsjLqkU4iCVpGZ5IVQ-ZqXN-Oh6pStUm0Ma5a9msBhmEmmaLUeWBlfzIxlAFaOOGANX8YglXWPQPQ0JUm2Lr0FVFcdFD_YeBo5jiqSvl5bOEqkYz7IkyDZWqR8pcOa9B8HgzWURb5MZpc9Zc4LcCjha6dNGQjkZeoCqWF16abq0UuqX_nduhUhavgzKYzUCinFy2vYY8cRN4dLw3rRtoZAmQVpKuxhf20laDX-x-THczf92BR2j-JoJbDOCu-XG_Yp6YV4Vsdjml9241kdqmaJyISRJSdCKo2XFy-D6F8cUZnIAWvKkHco6qEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین  الان ، چه خبره خلیج فارس
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/15115" target="_blank">📅 02:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15114">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/15114" target="_blank">📅 02:26 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
