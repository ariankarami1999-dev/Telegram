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
<img src="https://cdn4.telesco.pe/file/h0yr2mf64EF-ABJFnqeoDtAjdlARmH9SCdZticZDNwGS_NBOFdkrqhO-0bEswmYg_V0A_6hHp2Tt4Qin2m5rTpRz2Pfby9o0HfsicQQwAOtg8oDnwRIAApIkXMrYuKMFq_nuQI-eEFC5BW91ACXtKLqumoQDg3x3Tcr_pM7j17lJ4pL7zEaxrhfccc4j7FMVYj9zo8H6K-eyAdOqREA2HTcu4p8ZDI6PO63qCM8k2xqCHWtE-XL-RUKzft1Re_bov4WoKtXh5gYSjDLODBby8ZNbz8tu0aokKB6F_th03kPGF-W4-PAtioszLzRfChQENJlOPmJn-AfmLNqY37Ihyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 13:44:23</div>
<hr>

<div class="tg-post" id="msg-20132">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh1HFX9DutdSVaXoRcC1Pd9iIQcViXNsZ-RFLNHkK-WEEOME2CfzfAqVsmUQV215tlOQjizHhK6oJnLK7qKPTweRGn1FMae3903cn322zSSTMxrz2SH9JiKn7e6Oi8adTk-c9a-gbNQN0XYHRtUJMGKwun1ojP4DAHNIKNUEkbcLlhiN3a7QE-3tAAGo3oRI71MRzvdV1oOmJ2pe355biHzIsl8q0eVINb6u6jEGZ0kTEF3bbRsFgWdlsdLRw8M9Ss1XffWdFCUwz7HNUCgSqdrW1b7CNsljRj4ouZqQv0zqA9B__aaLwiNujA6QmTTSHxNmHmu36enzuGogfNrAeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=Yc-4hDvN0O5vW99eGCIo6czFYeNofk-uBUMz-Ej1dIfOdcID_UhMoYyvv_znL9sWXIz8w3DEBBhdHIYm9qv5vS2-bwGiPKusDpO710Oo6ecgJ195KjLIS365U2TlUiM8rKxN4j5Xjk-FCORwcuEdM1QOA0-m5ZDZmsQvKigaf6R6z6lBlaX4dhyZbls8JcznRnXl1k_Pk10EU4K_RVarMmPUCFPPGKaCe1HVat651PAuJHnVgcs5aoVBPk4SN8ei6xzN-YlBr9IIiJyamvM1zi2kcmqstsnZwO0WtXurzXMKgN9ial7se5j74UUaCL6qMKH3LBuhb0mKiVNhq41PfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=Yc-4hDvN0O5vW99eGCIo6czFYeNofk-uBUMz-Ej1dIfOdcID_UhMoYyvv_znL9sWXIz8w3DEBBhdHIYm9qv5vS2-bwGiPKusDpO710Oo6ecgJ195KjLIS365U2TlUiM8rKxN4j5Xjk-FCORwcuEdM1QOA0-m5ZDZmsQvKigaf6R6z6lBlaX4dhyZbls8JcznRnXl1k_Pk10EU4K_RVarMmPUCFPPGKaCe1HVat651PAuJHnVgcs5aoVBPk4SN8ei6xzN-YlBr9IIiJyamvM1zi2kcmqstsnZwO0WtXurzXMKgN9ial7se5j74UUaCL6qMKH3LBuhb0mKiVNhq41PfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاریکاتور اکونومیست با عنوان «کمبود رهگیرها» تصویری طنزآمیز اما هشداردهنده از یکی از مهم‌ترین آسیب‌پذیری‌های جنگ‌های مدرن ارائه می‌کند یعنی محدود بودن ذخایر موشک‌های پدافندی در برابر حجم بالای حملات موشکی و پهپادی.
در تصویر، سربازانی که ظاهراً نماینده آمریکاییها و متحدانشان هستند، در حالی که تعداد زیادی تیر دشمن ایرانی در سپرهایشان فرو رفته، زیر بارانی از تیرهای دیگر گرفتار شده‌اند.
دیالوگ بالای تصویر نیز به‌صراحت می‌گوید که جهان به رهگیرهای بیشتری نیاز دارد، اما بخش بزرگی از ذخایر موجود برای دفاع از آسمان خاورمیانه مصرف شده است.
نکته جالب‌تر، شباهت بسیار آشکار ترکیب‌بندی تصویر به صحنه معروف فیلم
300
است؛ جایی که سربازان اسپارتی در برابر سپاه عظیم ایران هخامنشی، زیر باران تیرهای پرشمار، سپرهای خود را بالا می‌برند. این ارجاع تاریخی، پیام کاریکاتور را تقویت می‌کند: مدافعان امروزی نیز با وجود فناوری پیشرفته، در برابر «اشباع» شدن سامانه‌های دفاعی با همان مسئله‌ای روبه‌رو هستند که سربازان اسپارتی به‌صورت نمادین با آن مواجه بودند.
طنز پایانی تصویر نیز تلخ است: سرباز سمت راست می‌گوید «امیدوارم دیگر چنین اشتباهی نکنیم»؛ اشاره‌ای به این واقعیت که مصرف سریع رهگیرها می‌تواند در جنگی طولانی، خود به یک بحران راهبردی تبدیل شود.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/20132" target="_blank">📅 08:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20131">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خب دیگر بس است بخوابیم.</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/20131" target="_blank">📅 01:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20130">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هر ایرانی در سال یک بار معتاد بشود و 2 بار ترک کند تا اینطوری تعداد معتادان کشور کاهش یابد و وابستگی کشور به تریاک وارداتی کاهش یافته و صرفه جویی ارزی کنیم.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/20130" target="_blank">📅 01:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هر خانواده ایرانی در خانه اش یک نفر را به عنوان سرباز آمریکایی اعلام کند تا ما دستگیرش کنیم و به آن خانواده 30 هزار دلار بدهیم.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/20129" target="_blank">📅 01:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مردم در خانه شان تنگه های هرمز پرورش بدهند تا ببندیم و از کشتی های عبوری عوارض بگیریم!</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/20128" target="_blank">📅 01:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20127">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfRobaa7wwT3JR9Wh_-kxGWM0BhtEroeK2yGm7EvYipQsc7qp0oIcVMgBW6UinZGDEB9pMTzhgDVIq0Npd8vbOXjeFnH4RXiwkJ5aaGEUFFIz9tYXO_3FBmssCqWEhEUweHRVd56kqENiuYzLESA4R8gEEslxzEktPOIYkUQdp311pKbIrOKtMlU92MGbrsn0ZfaiNNQyZc03CAplpJtYPmdTh3sN81IVo1TXQ8-u95c0B3MPBZMVTtnG3b7xmWoYeUCLyjWbHBAhUc2FZpJNpY_UMNObNN8WelQgrLcK0pHpGS_pO0RVyThqiULFgySPUG6eusQqG0KInOv9Tz-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/20127" target="_blank">📅 01:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20126">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBo4moLvoxzQsePoKBttft4h3TwSCNbFJhihF76QgqkTXt9SRh3NkPZ0sAyacZWabjSwztNG2ydyIX_blSWKhiyZNsAyi0wvLFGTOQ5EQsyet1VSWJp3QR4FkQFYoqCPT6hprszzhFjzYPBVrvgo-8vqHwdQCnWWEMQV9Jif4n7gI6QJ5yDBXpDG4WfFGSy4GcZseDFLRgiX305RxBepmXIKOR4Qjsl4YkMkBwkNrlz44rlq2EPYxLsT63vvoi2PiHYIlzT6f-YZHruwUKh4lTBXFJDwjCYI9cVyF6G5DBNDSkTbj61CxCFH0Z51FcxUpDL4nXAXG3Obd-SaMazymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربران اسرائیلی با انتشار این تصویر، به تهدید اردوغان پرداختند.  جالب است که این تصویر شباهت بسیاری به صحنه دستگیر کردن عبدالله اوجالان رهبر PKK دارد که اتفاقاً با کمک مستقیم موساد صورت گرفت.</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/20126" target="_blank">📅 00:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20125">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KImCeOjgxrZV5AdeamarcV7P0826QpNJRKdAjFEQS9uK12K8VhAM94eOGG73JLtFPtw2-Ug5uYqfvc2RyLv4ZLEwASf1ZObCpj-A-l_B5DaO53k6a9baNOuj5aL8WXIJkIFKKnLEtcLXukuPRyFVA4x3W_KwDiyLJ1yzycVLvaV_H1rDwD63arlEAN6ERDzr8uxXJBOMJaTBlGDa9SzKefah-WDH9G1hGZ0P-c6bgg051ft0Q0YJ1bKM_a8vehuJxxdQdqfSdCYpBPEQj6baw-Gl_FNONhU7MrvgqySIkBqoICWgKuUC8PCmoGNdBrldMzhA6t1QbAgROmZxGfliJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربران اسرائیلی با انتشار این تصویر، به تهدید اردوغان پرداختند.
جالب است که این تصویر شباهت بسیاری به صحنه دستگیر کردن عبدالله اوجالان رهبر PKK دارد که اتفاقاً با کمک مستقیم موساد صورت گرفت.</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/20125" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20124">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/20124" target="_blank">📅 00:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20123">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/20123" target="_blank">📅 00:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20122">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مردم فلافل بخورند و در خانه شان نیروگاه بادی راه بیاندازند</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/20122" target="_blank">📅 00:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20121">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayb6eoRMwAocxv482dL5vnjhHuyVrT0JxK6xEqSAhMQ6LpaPrFxkbZDg5mwEuOgsGqy_T4EsvfyTxjp2nq9ip-ZLpQkynkZYGgVy8-D91ln809HrsOvt22Yi2AvcJoagNvOVRQYQxXVNVzqRlVrt4MW4KQmLFL2ur8mYlqxd332IceOb6h7yRgtDVOk2akopF1tSsiX4ZeSddTwKaG-2ETw8965DtVFPz-H-LC5TTPM-TQm7pAYvAIHhoxiAhkyHJis6HA5eCGsRiXrFr2CY6fvBAsx6GNfP0vBj1uqrSUr0g9RUIiSMpAtoo8msud5tUxZbA5AGQxtEpUR6h2V1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!
ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/20121" target="_blank">📅 00:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20120">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT6fiOFzz3F4k-hF6xtCi8vzv5rtRBwTvcFK5lde89_2J47dYf4aAO80dSfXIYxdDGlGkTDJQbcPfDZBUrejaqNBY2yIN6EHEnV9WDSs4TEydE5DwOKoveOu_odX2ySJ9D7bFKTF8TrLRalbVyCHd6xGw9rYGXJ-FZugEA1Uzzu_iXEtEaRAGRss-InqJ-XUHPaIYG77jQF6uQZs8gdqioOq1AgJ5bGNNQTC7X15x2DkDO6RKqecCYLgCn7iXHh0xfNUUAs873ZxA92Dk5fMsoJ3mjoZo_Ce0i8QC5rHTPFkFhdAMRMiG-JZva4f8x3iSC2HJhdepbWx_lXm4BcUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید یادتان نباشد ولی این نخبه نابغه کشورمان — دکتر حجت عبدالملکی — که حتی رییسی او را از کابینه اش اخراج کرد یک بار گفته بود با 1 میلیون تومان میشود کار ایجاد کرد!
یک نفر خوش ذوق هم زیر پستش کامنت کرده بود بله 700 هزار تومان دستگاه تقطیر با 300 هزار تومان کشمش!
البته الان با 1 میلیون تومان نهایتاً یک پیتزا با یک دوغ به شما می دهند و آبش را هم میدهند Meساکی بخورد.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/20120" target="_blank">📅 00:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20119">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باید در هر کوچه یک شیره کش خانه باشد و بعد کنارش یک کمپ ترک اعتیاد بزنیم تا مردم هر کوچه از هم پول بگیرند و گردش مالی ایجاد بشود و مالیاتش را هم بدهند به ما.</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/20119" target="_blank">📅 00:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20118">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">محسن رضایی:   مردم در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه کنند</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/20118" target="_blank">📅 23:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20117">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محسن رضایی:
مردم در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه کنند</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20117" target="_blank">📅 23:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20116">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f676cce991.mp4?token=HXkNd49pDsDBesCTME24uHEmABOJgFbJkBhoibbTG6Woy5GnrhFhQq_GJzu666BdCWvrKYZFWCPMj-0Xu23UahvWmb97iFsaLxRZFHqT7nHz4Xn4lOBAji9o7UVuPQJukrsKhiPybHrh3R1oxe5oeW6SJD6WHr_gbJFhhgRvuwbPOu3yXah1dnLtDF33smdux2MU8J-kMrc-JiN2TawFIUJ-0cbp80yQe9ioStQh0XXF_C2cqBrpQ2pulpEKS8C2qO_8oS2edPuRxTj6huloisk5nSx9qJ-li-QZ9TTNoAdVeLRKLLoXZS5pkAVjXiwHJneIIkZ0SFOlf1ojxe1kSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f676cce991.mp4?token=HXkNd49pDsDBesCTME24uHEmABOJgFbJkBhoibbTG6Woy5GnrhFhQq_GJzu666BdCWvrKYZFWCPMj-0Xu23UahvWmb97iFsaLxRZFHqT7nHz4Xn4lOBAji9o7UVuPQJukrsKhiPybHrh3R1oxe5oeW6SJD6WHr_gbJFhhgRvuwbPOu3yXah1dnLtDF33smdux2MU8J-kMrc-JiN2TawFIUJ-0cbp80yQe9ioStQh0XXF_C2cqBrpQ2pulpEKS8C2qO_8oS2edPuRxTj6huloisk5nSx9qJ-li-QZ9TTNoAdVeLRKLLoXZS5pkAVjXiwHJneIIkZ0SFOlf1ojxe1kSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخستین تمرین رزمی جنگنده سبک یاک روسی در نیروی هوایی ایران    ‌
👍
جنگنده یاک در کنار دو فروند جنگنده میگ ۲۹، در عملیات رهگیری و منهدم کردن پهپاد هدف مشارکت داشت و خلبانان جنگنده‌های میگ ۲۹ با مهارت بالا موفق به شناسایی و رهگیری پهپاد هدف شدند.
👍
در ادامه، جنگنده…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/20116" target="_blank">📅 22:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20115">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسراییل در حال بمباران جنوب لبنان است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20115" target="_blank">📅 21:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20114">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMlnn4u32gRQckoCz1ZL80qv5aV2rmFnw7NU_1CPuO8qjaBhQu54ybIPRzxk_WYFKQn6s4gHE5zjFYbI5e7W7oEGfrA_GiwfnTZpPo8opGG3fzW0LhNKmolc9_ydQ9gXPF0_Q91idEuSTk2-ABO1UXBguxI4lT5vXt0Pi9rMZU5nR-viAw1mIs8gJgKnjueNEt-w2iTqV14qN5HBxCmJVW6FWo8_Ktsc7E8g8O_RqUtv7xIhULVW_74jrvq_OG1GH0Ydzr5CNzdKqT5RwzRSS2y6IPzDjKrQQz-DOy4hFUclN6-AkJPBrLMY8Po4nkq0xBMIefZ1FmcaQKDtSkZlvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقاله در روزنامه اورشلیم پست اسرائیل خواستار آن شده است که اسرائیل، ترکیه را به عنوان یک تهدید نظامی در سطح ایران در نظر بگیرد، و این جمله تحریک‌آمیز را مطرح کرده است:
از ادلب تا استانبول، اسرائیل در صورت لزوم، حمله خواهد کرد، نه اینکه دفاع کند.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20114" target="_blank">📅 20:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20113">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یک صوتی مفصل در این خصوص خواهم داد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20113" target="_blank">📅 18:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20112">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اوه اوه!    بنگلادش در حال بررسی امکان پیوستن به پیمان مکه است!</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20112" target="_blank">📅 18:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20111">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">باز سعودی ها دستکم کتک خوردن ترک‌ها در سوریه از اسراییل برای بار پنجم را محکوم کردند!  شهناز جوراب که کلا خودش را زده به کوچه علی چپ!   نه حملات یمنی ها به سعودی را محکوم کرد نه حملات اسراییلی ها به ترک‌ها را !  سبحان الله عجب پیمانی شد این پیمان ناتوی اسلامی…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20111" target="_blank">📅 18:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20110">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20110" target="_blank">📅 18:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20109">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20109" target="_blank">📅 18:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20108">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خیلی عجیب است.   خود ترامپ در مارس ۲۰۱۹ منطقه جولان را به عنوان بخشی از خاک اسراییل به رسمیت شناخته آن وقت سفیرش در ترکیه صحبت از «اشغال» جولان می‌کند!  حدس میزنم عمر سیاسی  — و شاید زیستی — تام باراک (که عرب تبار است) بزودی به پایان برسد.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20108" target="_blank">📅 18:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20107">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-poll">
<h4>📊 تاریخ شروع جنگ ایران و‌ عراق از دید عراقیها چه تاریخی است و چرا؟</h4>
<ul>
<li>✓ ۳۱ شهریور ۵۹ — حمله همه جانبه ارتش عراق</li>
<li>✓ ۳۰ شهریور ۵۹ — حمله هوایی ایران</li>
<li>✓ ۱۰ مرداد ۵۹ — سخنان تحریک آمیز رهبران ایران</li>
<li>✓ ۱۳ شهریور ۵۹ — گلوله باران مندلی و خانقین توسط ایران</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20107" target="_blank">📅 14:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20106">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این هم جواب آمریکا:  ایالات متحده در حال پیشبرد قانونی است که هلند را مجبور می‌کند تمام فروش و خدمات باقی‌مانده دستگاه‌های لیتوگرافی ASML به چین را ممنوع کند.  قانون MATCH به دستگاه‌های DUV قدیمی‌تر که هنوز تحت قوانین هلند مجاز هستند، هدف می‌گیرد.  چین ۳۳…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20106" target="_blank">📅 14:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20105">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چین می‌گوید تهدید رئیس‌جمهور ترامپ برای آغاز «جنگ اقتصادی» علیه ایران و شرکای تجاری آن کارساز نخواهد بود.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20105" target="_blank">📅 14:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20104">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دنیس اشتایلرمن، رئیس شرکت فایر پوینت، تولیدکننده موشک‌های «فلامینگو»، پیامی با تهدید علیه ایران منتشر کرد.  این تصویر، فلامینگوهای صورتی را نشان می‌دهد که در امتداد مسیری که اوکراین و ایران را به هم متصل می‌کند، پرواز می‌کنند و لوگوی شرکت و عنوان زیر آن آمده…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20104" target="_blank">📅 13:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20103">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20103" target="_blank">📅 13:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20102">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ایران اجازه عبور چندین تانکر نفتی عراقی از تنگه هرمز را پس از درخواست عراق صادر کرد: ایرنا  چنین اقدامی در اوج فشارهایی که روی اوراق قرضه خزانه داری آمریکا آمده به صورتی که باعث شده اسکات بسنت دست به طرح عجیب و غریب بازخرید اوراق قرضه بلندمدت بدون تقاضا بزند،…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20102" target="_blank">📅 12:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20101">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20101" target="_blank">📅 12:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20100">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20100" target="_blank">📅 12:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20099">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rtc-FDdaXPym41W8sXMbpsDES-VjAehjjt6-DI-VkPFLfmdm38VIJ3oAQG4v0I9jNEeP_e9csedVaqG4VmMZIGWgLNvUoy-CJ_8c0wq9T3aaNa4XG62emVmln4eRQRSVL0Zic98QQMgAqwrVoHTrQKMF69ZGTFRZgHxgCuBPmcjHEPMG2lhM2qGgbTY2audUjnv746aD8LqfinG9He213vhTVFMvkXMsTFM_z4nw8THg3EqoQy0DpE7SyOzBQfkxbnA98wfC6JMuPr7yEuKrRWxzkT1x3FrWvpy8GocBXZz1HEkcW2D-EaIh0HMnLmR5yqmjJDI6go6gFRtzvx1jbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.
اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد بخشی از حاکمیت بیش از گذشته به این جمع‌بندی رسیده که ادامه جنگ و فشار اقتصادی می‌تواند هزینه‌ای سنگین تر از جنگ برای نظام ایجاد کند.
پزشکیان دیروز صراحتاً گفت بهتر است جنگ در مقطعی پایان یابد و «اکنون» پایان دادن به آن ترجیح دارد. قالیباف نیز هشدار داد که حتی قدرت نظامی بالا، بدون گردش مالی، رشد اقتصادی و تولید داخلی، نمی‌تواند کشوری را که مردمش تحت فشار معیشتی قرار دارند، پایدار نگه دارد. مهم‌تر از همه، همتی اذعان کرد که صادرات نفت ایران تقریباً متوقف شده و کشور با کمبود ارز، هزینه‌های بازسازی و افزایش بیکاری جوانان مواجه است.
این اظهارات را می‌توان نشانه‌ای از شکل‌گیری یک کارزار هماهنگ در بخش میانه رو جمهوری اسلامی برای مهندسی افکار عمومی جامعه ایرانی در جهت باز کردن دوباره باب دیپلماسی و فاصله گرفتن از فضای پرتنش کنونی ارزیابی کرد.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/20099" target="_blank">📅 12:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20098">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی قرار دارد و پیش بینی می شود طلا یک اصلاح نزولی دستکم در حد 300 الی 500 پیپ داشته باشد.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/20098" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20097">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4df224890.mp4?token=Skw86Pmz5KHyPyb1Hith0oYN6btdpc70knx16rkQ2hXKwDgShz9yEerAhMCVL3lQxlSKeScVS4V5qKI2wgD_SINM7AN4UDWuasT2TcLPxzKfCdnUj4Vx6IqZ_O1ZqEngJmONouW7ez-D0t9CtXq824Fu5tNNCY7-zbnoinTEmtFmFklKUUB1fnSHzHbkCa0Y4YT7GBscEvFqz1lUusP7M_kZVDZ7OPT5rcexHrJ62znRX02ZdHnjtqxfGuRiX85E1rTsoJxT3GIGGRcTdINuAzYPFQVj3299w7qv_HvCDIM6QA5mOWyyzoLreknQnLp8SPMr7dpDsoohDHKF1mxKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4df224890.mp4?token=Skw86Pmz5KHyPyb1Hith0oYN6btdpc70knx16rkQ2hXKwDgShz9yEerAhMCVL3lQxlSKeScVS4V5qKI2wgD_SINM7AN4UDWuasT2TcLPxzKfCdnUj4Vx6IqZ_O1ZqEngJmONouW7ez-D0t9CtXq824Fu5tNNCY7-zbnoinTEmtFmFklKUUB1fnSHzHbkCa0Y4YT7GBscEvFqz1lUusP7M_kZVDZ7OPT5rcexHrJ62znRX02ZdHnjtqxfGuRiX85E1rTsoJxT3GIGGRcTdINuAzYPFQVj3299w7qv_HvCDIM6QA5mOWyyzoLreknQnLp8SPMr7dpDsoohDHKF1mxKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20097" target="_blank">📅 11:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20096">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مدیرعامل شرکت نفت ستاره خلیج فارس از عملیاتی‌شدن استفاده از متانول به‌عنوان جزء اکسیژنه در ترکیب بنزین تولیدی این پالایشگاه خبر داد.   این تغییر می‌تواند برای بخشی از خودروهای موجود در بازار، به‌ویژه قطعات لاستیکی و پلاستیکی مسیر سوخت، ریسک فرسودگی زودرس ایجاد…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20096" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20095">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مدیرعامل شرکت نفت ستاره خلیج فارس از عملیاتی‌شدن استفاده از متانول به‌عنوان جزء اکسیژنه در ترکیب بنزین تولیدی این پالایشگاه خبر داد.
این تغییر می‌تواند برای بخشی از خودروهای موجود در بازار، به‌ویژه قطعات لاستیکی و پلاستیکی مسیر سوخت، ریسک فرسودگی زودرس ایجاد کند.
به گزارش شبکه اطلاع‌رسانی طلا و ارز، مدیرعامل شرکت نفت ستاره خلیج فارس روز جمعه ۳۰ مرداد ۱۴۰۵ (۲۱ آگوست ۲۰۲۶ (۳۰ مرداد ۱۴۰۵)) از
افزودن متانول به بنزین
تولیدی این پالایشگاه خبر داد. به گفته او متانول در حال حاضر به‌عنوان یکی از اجزای اکسیژنه در ترکیب سوخت مصرفی خودروها به‌کار گرفته می‌شود.
اکسیژنه‌ها ترکیباتی هستند که به
بنزین
اضافه می‌شوند تا احتراق کامل‌تر شود و عدد اکتان سوخت افزایش پیدا کند. عدد اکتان بالاتر یعنی سوخت در برابر خودسوزی زودهنگام در موتور مقاوم‌تر است؛ همین ویژگی باعث می‌شود پالایشگاه‌ها از این نوع افزودنی‌ها به‌جای ترکیبات گران‌تر مانند MTBE استفاده کنند.
چرا متانول نگران‌کننده است؟
متانول
برخلاف بسیاری از افزودنی‌های رایج، خاصیت خورندگی بیشتری روی قطعات لاستیکی و پلاستیکی سامانه سوخت‌رسانی دارد. اورینگ‌ها، شیلنگ‌های سوخت، دیافراگم پمپ بنزین و برخی مخازن پلاستیکی از جمله قطعاتی هستند که در تماس طولانی‌مدت با متانول، سریع‌تر از حد معمول فرسوده می‌شوند. نتیجه عملی برای مالک خودرو، احتمال نشتی سوخت یا کاهش عمر همین قطعات و افزایش هزینه تعمیر است.
کدام خودروها بیشتر در معرض‌اند؟
خودروهایی که سامانه سوخت‌رسانی آن‌ها برای درصد بالای الکل یا متانول طراحی نشده، بیشترین آسیب‌پذیری را دارند. این گروه شامل بخشی از خودروهای مدل پایین‌تر و برخی خودروهای وارداتی قدیمی‌تر می‌شود که استانداردهای سوخت انعطاف‌پذیر (فلکس‌فیوئل) در آن‌ها رعایت نشده است. خودروهای جدیدتر با قطعات مقاوم به الکل معمولاً ریسک کمتری دارند.
مدیرعامل
ستاره خلیج فارس
تأکید کرده است که درصد متانول در ترکیب بنزین در چارچوب استانداردهای مصوب کنترل می‌شود. با این حال، جزئیات دقیق درباره سهم متانول در هر لیتر بنزین و نظارت مستمر بر کیفیت آن، اطلاعاتی است که مصرف‌کننده هنوز به‌طور شفاف در اختیار ندارد.
استفاده از افزودنی‌های داخلی به‌جای واردات ترکیبات اکسیژنه، برای پالایشگاه‌ها از نظر اقتصادی مقرون‌به‌صرفه‌تر تمام می‌شود. این رویکرد در سال‌های اخیر در چند کشور دیگر نیز با هدف کاهش وابستگی به واردات آزمایش شده، اما همواره با هشدارهای فنی درباره سازگاری آن با ناوگان خودرویی موجود همراه بوده است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20095" target="_blank">📅 11:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20094">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این موشک های دوش پرتاب حرارتی صرفا برای زدن بالگردها، پهپادها و هواپیماهایی که در ارتفاع پایین پرواز می‌کنند مناسب هستند.  به نظر می‌رسد هدف از تسلیح ایران به این سلاح ها، ایجاد فرسایش در نیروهای آمریکایی است که محتملا در حمله زمینی به جنوب ایران درگیر خواهندشد.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/20094" target="_blank">📅 10:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20093">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:  آیا تا به حال کمونیست شاد دیده‌اید؟  آیا تا به حال دیده‌اید که یک کمونیست بخندد؟ من هرگز چنین چیزی ندیده‌ام. من با کمونیست‌ها آشنا بوده‌ام. آن‌ها افراد بسیار ناراحتی هستند.  ما می‌خواهیم شاد باشیم!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20093" target="_blank">📅 03:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20092">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ:
آیا تا به حال کمونیست شاد دیده‌اید؟
آیا تا به حال دیده‌اید که یک کمونیست بخندد؟ من هرگز چنین چیزی ندیده‌ام. من با کمونیست‌ها آشنا بوده‌ام. آن‌ها افراد بسیار ناراحتی هستند.
ما می‌خواهیم شاد باشیم!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20092" target="_blank">📅 03:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20091">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سفیر ایالات متحده در ترکیه، تام باراک:  اسرائیل هنوز جولان را در اشغال خود دارد، برخلاف قطعنامه‌های سازمان ملل، برخلاف کل نظم بین‌المللی که جولان را متعلق به سوریه می‌داند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20091" target="_blank">📅 03:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20090">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سفرای ترامپ مثل خودش متناقض حرف می زنند.  سفیر ترامپ در ترکیه یعنی تام باراک از اسرائیل شدیداً انتقاد کرده بود اما سفیر او در اسرائیل اینطوری قضیه را ماست مالی می کند.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20090" target="_blank">📅 03:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20089">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سفرای ترامپ مثل خودش متناقض حرف می زنند.  سفیر ترامپ در ترکیه یعنی تام باراک از اسرائیل شدیداً انتقاد کرده بود اما سفیر او در اسرائیل اینطوری قضیه را ماست مالی می کند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20089" target="_blank">📅 03:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20088">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ درباره ایران:
نمی‌دانم با چه کسی در ایران مذاکره کنم. این واقعاً یکی از بزرگ‌ترین مشکلات من است.
هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران باشد. می‌گویند: «چه کسی می‌خواهد رئیس‌جمهور باشد؟» «نه، نه، من نمی‌خواهم رئیس‌جمهور باشم.»</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20088" target="_blank">📅 03:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20087">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارشگر: با توجه به اینکه ایران به سمت جنگ اقتصادی پیش می‌رود، آیا این بدان معناست که گزینه‌های نظامی برای ایالات متحده محدود شده است؟
ترامپ: خیر، اصلاً.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20087" target="_blank">📅 00:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20086">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">روسیه برای اولین بار در بیش از یک دهه، هیچ کشتی جنگی در مدیترانه ندارد، زیرا مسکو کشتی‌ها را برای محافظت از تانکرهای نفتی تحریم‌شده از دستگیری توسط ناتو منحرف کرده است.
منبع: تلگراف</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20086" target="_blank">📅 21:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20085">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نماینده مجلس  ابراهیم عزیزی:
آمریکایی‌ها ثابت کرده‌اند که زبان دیپلماسی را درک نمی‌کنند، بنابراین نه تحریم‌ها را برمی‌دارند، نه منابع را آزاد می‌کنند و نه به دزدی دریایی در دریاها پایان می‌دهند.
اما تاریخ نشان خواهد داد که با زبان قدرت، نه تنها به این اقدامات مجبور خواهند شد، بلکه منطقه را با عذرخواهی از ملت بزرگ ایران ترک خواهند کرد.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20085" target="_blank">📅 19:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20084">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">افزایش تنش ها میان اسرائیل  و ترکیه    دولت ترکیه حکم بازداشت نتانیاهو را صادر کرد.  دولت ترکیه درخواست صدور اعلان قرمز اینترپل را برای بنیامین نتانیاهو  به دلیل جرایم علیه فعالان ناوگان جهانی "صمود"، از جمله جنایات علیه بشریت و نسل‌کشی، صادر کرده است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20084" target="_blank">📅 18:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20083">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اظهارات  هاکابی، سفیر آمریکا در اسرائیل، درباره حملات اسرائیل به سوریه:  به نظر من این کار عمدی نبود. اگر به آنچه واقعاً اتفاق افتاد نگاه کنید، تعدادی از مهمات در یک فرودگاه قرار داده شدند. هیچ تلفاتی نداشت.  به نظر من، این بیشتر یک هشدار بود تا تلاشی برای…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20083" target="_blank">📅 16:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20082">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اظهارات  هاکابی، سفیر آمریکا در اسرائیل، درباره حملات اسرائیل به سوریه:
به نظر من این کار عمدی نبود. اگر به آنچه واقعاً اتفاق افتاد نگاه کنید، تعدادی از مهمات در یک فرودگاه قرار داده شدند. هیچ تلفاتی نداشت.
به نظر من، این بیشتر یک هشدار بود تا تلاشی برای ایجاد تنش.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20082" target="_blank">📅 16:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20081">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اخبار تاییدنشده از حرکت انبوه نیروهای زرهی و توپخانه ترکیه به سمت سوریه</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20081" target="_blank">📅 16:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20080">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترکها در ظاهر می گویند اردوغان موفق شده ترامپ را متقاعد کند تا از این طرح جلوگیری کند اما به نظرم این پلن A شان بوده و پلن B شان شامل ورود مستقیم نظامی به ایران همراه باکو برای اشغال شمال غربی ایران بوده که پیشتر اشاره کرده بودم.  در هر صورت، در راند بعدی…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20080" target="_blank">📅 16:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20079">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دولت باغچلی، سیاستمدار ملی‌گرای ترکیه، نسبت به حمله هوایی اسرائیل به پایگاه هوایی در سوریه، هشدار شدیدی صادر کرد:  وقتی ملت ترکیه قیام می‌کند، هیچ نیرویی نمی‌تواند در برابر آن مقاومت کند.  ترکیه، کشوری نیست که در برابر حملات به حقوق حاکمیتی خود، منفعلانه عمل…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20079" target="_blank">📅 15:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20078">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-text">🔥
نفت ایران در بازار چین کمیاب شد و تخفیف منفی!
🔹
رویترز: پیشنهادهای فروش نفت ایران به خریداران چینی کاهش و قیمت محموله‌ها افزایش یافته.
🔹
برخی محموله‌های ایران به‌جای تخفیف معمول، با قیمت بالاتر از شاخص برنت عرضه می‌شوند.
🔹
صادرات نفت ایران در ماه جاری به ۵۳۴ هزار بشکه کاهش یافته؛ در حالی که میانگین صادرات در سال گذشته ۱.۴ میلیون بشکه بوده.
🔹
همچنین ذخایر نفت ایران روی آب از ۱۰۵ به حدود ۸۰ میلیون بشکه کاهش یافته و پالایشگاه‌های مستقل چین برای تأمین خوراک به دنبال نفت جایگزین از کشورهایی مانند عراق و برزیل هستند.
@khate_energy</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20078" target="_blank">📅 14:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20077">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Usmdn4c1WhJPF8IdeVENuaSq0E79RjhBnMLjvUbjS11dbuQd1Ngesrgnm6auAqaPxCsUEUYiB1p7fiV_lb3GDZ8KBd390mIHPYBFi86Yy8_qpPW_bG8Hetc2Y-_ut_tWvgyZHcAxiKC-kk7Z670gQpEifAHTwoGrGxOIhnDtMHIpf2lJUMsxewQgBJ-VCqF32vBBUGA7bJrotYN1tZolCV92KmQoluJEGa9F5exxrqAFIGqhwwjtqEyLmHjiSthl9Oy_adVXmW4hZuoLhvbENtnSmxRS_ZzULloejF_OevdpG11EbYxk_KdbWMw3P68Krrg5I3YcdqzJuhd6yrt85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعات استخباراتی اسرائیل حاکی از آن است که ترکیه در حال آماده‌سازی برای ارسال سلاح‌های تهاجمی و دفاعی به سوریه، از جمله سامانه‌های پیشرفته دفاع هوایی، است</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20077" target="_blank">📅 13:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20076">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixZNUDhGnp5lfkH4SS9bWKw0Tx_LN2avCZ4TjvwNF-Df-TcB6DwjLGjeOkkdHz8HTKV3CklkuWzgFQdQpu5Dgjv1CM_-KAq0N9t3hprBRKf4xXFP1K7ldDdCY-ineD8UhdfxtiPJxEEynUlkkSH7aLchu8ZBGU2GtKdOdkWu9e14MVQ-716jPSfXj-vJLIrZRbXp0V3rqSgqLb_kyEG7bpGe0OeyZ7X4LGnAqOvlYJe7VzYBGZPT_5sidZoNZqF5Hfo6yg59-hhMSmZyft9zHiXPv3V996u_cgcxHu9HC-WHedrLWY-snfbNBn3UJfwpGYobbHpQmlnSFQ9s56yEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی قرار دارد و پیش بینی می شود طلا یک اصلاح نزولی دستکم در حد 300 الی 500 پیپ داشته باشد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20076" target="_blank">📅 13:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20075">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">– طبق گزارش رویترز با استناد به داده‌های کپلر، تعداد کشتی‌هایی که از تنگه هرمز عبور می‌کنند همچنان در محدوده تک‌رقمی است.
فقط ۷ کشتی در روز پنجشنبه از تنگه عبور کردند که ۴ کشتی وارد و ۳ کشتی خارج شدند. برخی از این کشتی‌ها از مسیر ایران استفاده کردند، از جمله یک کشتی بزرگ حمل گاز. هیچ کشتی بسیار بزرگ حمل نفت خام (VLCC) در هیچ‌جا دیده نشد.
ترافیک در تنگه بابرالمندب نیز کند شده است؛ به طوری که تنها ۲۳ کشتی در روز پنجشنبه عبور کردند، در حالی که این عدد در روزهای سه‌شنبه و چهارشنبه ۳۴ کشتی بود.
این در حالی است که ترامپ و اکسیوس ادعا کرده‌اند که روزانه ده‌ها میلیون بشکه نفت با هدایت ایالات متحده از تنگه عبور کرده و به بازارهای جهانی رسیده است.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20075" target="_blank">📅 09:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">- یک مقام ارشد ایرانی اظهار داشت که ایران در حال آماده شدن برای آسیب رساندن به ریاست جمهوری ترامپ از طریق جنگ اقتصادی است، با هدف اینکه او در انتخابات میان‌دوره‌ای نوامبر شکست بخورد.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20074" target="_blank">📅 08:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20073">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اطلاعات استخباراتی اسرائیل حاکی از آن است که ترکیه در حال آماده‌سازی برای ارسال سلاح‌های تهاجمی و دفاعی به سوریه، از جمله سامانه‌های پیشرفته دفاع هوایی، است</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20073" target="_blank">📅 01:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20072">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3ayup9Ls-r0kYi95RPIzoZKQGZ0c1KR10nhC1ybzeelQulkB5hXHNzI5KUmtmLt4wm7u3zHwGLjMyE1KSDsZHuJVQfy_Uy8geQYuzn_gVYBFK44fEzrrbswV3QDs9yLkJoG0VXCKr1tzg3P-__bc0H6mQrN_5RHMqb9gtGXqoOQrYVz9LzZ25T0CLRLnF4jmaHJES-TdolA93VIj92UxZMXwLuiODw25xa3tG2SWEC7ZNR2VXmoEDK2uK3gh6ZLyiDEK-S0wE4kS0XcQQSy4SOqpR52pblaEkUImpQOuV2PgKre9U5RNruixaEENTI9RMqi0x4tS0EziD6Q96LmKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلن ایر دیپلمات سابق ارشد آمریکایی خطاب به ترامپ</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20072" target="_blank">📅 01:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20071">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اظهارات معاون رئیس‌جمهور، جِی. دی. ونس، درباره ایران:
ما اکنون در یک مرحله جدید قرار داریم که موثرترین ابزاری که در اختیار داریم، فشار اقتصادی است که می‌توانیم بر آنها وارد کنیم.
این یک تعادل ظریف است، زیرا ما فشار اقتصادی بر آنها وارد می‌کنیم. آنها نیز تلاش خواهند کرد که فشار اقتصادی بر ما وارد کنند.
اما آنچه در چند هفته گذشته صادق بوده این است که آنها احساس فشار بسیار بیشتری نسبت به آنچه ما تجربه کرده‌ایم، داشته‌اند.
ما این روند را ادامه خواهیم داد، زیرا معتقدیم که این بهترین راه برای دستیابی نهایی به هدف مورد نظر است.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20071" target="_blank">📅 00:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20070">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20070" target="_blank">📅 23:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20069">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBNZARFIC1oxJoDWFkH-pDt49wsnDdVBg-J7v02X9hevxCRfvHQzsn3gpP9cBodpIgtYunVYRcQ3XM5ypp65vVZkcN6qdBs8-7uBgT53EoHp4P0EgQmDvImboW108kv1wwiudf1h_aJiuEZHlE_TOnP4cMtNKnpUkkbt3KnQmRFClaNpoZNc_j2mNdRP-mWlEtX1dH2wAAaUYvFisj-pAiXIdiDgJeFc9Chm8fkoGP7snAbI9Z0W5tl3_vuWSG6IOgppQ_rHFHC6JFNTImx2FnitHgJ4IdEbYAEY17uCH6nsAZzZEbUeD8Yr7hNhcnrFjC7EDUCwVh_h_DE-F3P-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس عراق در واکنش به این عکس قالیباف، از خود عکسی منتشر کرد که در پشت سر او، بجای خلیج فارس، نام نجس خلیج عربی نوشته شده!</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20069" target="_blank">📅 21:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20068">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایالات متحده آمریکا تحریم‌های جدیدی علیه حزب‌الله اعمال کرد و آن را مجدداً تحت یک قانون مربوط به تروریسم طبقه‌بندی کرد تا بر پیوندهای آن با نیروی قدس سپاه پاسداران انقلاب اسلامی ایران تأکید کند.
واشنگتن همچنین ۱۰ نفری را که متهم به قاچاق پول نقد برای حزب‌الله هستند، تحریم کرد.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20068" target="_blank">📅 21:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20067">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چین می‌گوید تهدید رئیس‌جمهور ترامپ برای آغاز «جنگ اقتصادی» علیه ایران و شرکای تجاری آن کارساز نخواهد بود.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20067" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20066">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20066" target="_blank">📅 20:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20065">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ضرغامی:   از اول انقلاب تحریم بودیم ولی کشور رشد کرده، پیرزن رو از تاکسی خالی نترسونین!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20065" target="_blank">📅 19:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20063">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ضرغامی:
از اول انقلاب تحریم بودیم ولی کشور رشد کرده، پیرزن رو از تاکسی خالی نترسونین!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20063" target="_blank">📅 19:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20062">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20062" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20061">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حوثی‌های یمن اعلام کردند که دو حمله پهپادی را علیه فرودگاه ابها و تأسیسات آرامکو در عربستان سعودی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20061" target="_blank">📅 17:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20060">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">— مرکز فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد که گروه ضربتی ناو هواپیمابر یواس‌اس جورج واشینگتن به خاورمیانه رسیده و اکنون در منطقه مسئولیت خود عملیات می‌کند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20060" target="_blank">📅 17:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20059">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رئیس مجلس عراق در واکنش به این عکس قالیباف، از خود عکسی منتشر کرد که در پشت سر او، بجای خلیج فارس، نام نجس خلیج عربی نوشته شده!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20059" target="_blank">📅 16:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20058">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QF_QNUIYCKGFS-7em5XnB-6_s7aNzTWCp6FPsa4kMP5n02-Rm85nx5kisPtRPAtW0aMdVvC-vtw_VtTHBva1e-7OJczkFhWUY3B1LS-4LmhTh0yR61uJvQEl6QXnAp-EZTTehUADqxJNcAiBp5FGELI2WIgID2IPZ7q6wLcSNop7-9PI5EQTdueozUCuNVg6BqnaQB64MV4J6GpMoVbWcmQmq7hBUqB2mkjTsR3NyrAS9-K3cstCfZcBJRU1Br3N4SBoIPT8l_qsfQkCMBn1Lu20R-3g-czqXCc35etQmjqmwEmP_Kouh3I38gU2RH7MYr8RtXuUTUqJP1khheeSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله این چه فیگوری است دیگر!  انسان گمان می کند که نعوذبالله دارند با کله نورانی شان روده بزرگ کشورمان را کلنوسکوپی می کنند!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20058" target="_blank">📅 16:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20057">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اردوغان: «ترکیه در دامی که نتانیاهو برای سوریه چیده است، نمی‌افتد»</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20057" target="_blank">📅 15:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20056">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اردوغان:  «توافق مکه» علیه هیچ کشوری نیست و تمام دولت‌ها می‌توانند به آن بپیوندند  نباید این توافق را به بعد نظامی محدود کرد، زیرا هدف اصلی آن تقویت بعد بازدارندگی و امنیتی است</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20056" target="_blank">📅 15:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20055">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در بالاترین سطح خود قرار دارد و تقریباً در چنین شرایطی محال است که امروز شاهد سقف جدیدی در طلا باشیم.  انتظار افت دستکم 400 پیپی دیگر در طلا دارم.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20055" target="_blank">📅 15:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20054">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9QwSgOFCr4GgFS04Gahulbo7bTVapOjlSiovJNbIee0IFi_MvsHn5QfUzE72kGceskUoslCw0ZTDevZM2ANQFQQXzGpzEf-inu1uIGSe6ktfql6gMMwgTuH1orQwUgj9A1b_EseOyCZqgHqSKL59FOeXpTVrM1V6cjz-UjQ3Gnpdz-SNZjLgHT9RNtRxepMSRnRd_Epqe0_-Ra0Gkzb3uIQpfH-f1e_ONXjygxd70PGJIPSmkkL1hCAa1SJxbKBSko_dNyPube0UHvr-yt3gbo8OvbWrvka2UCaYnLEwpBSwRhBS7e0XlyEsN0JfttSGKuvxq-R0G5N61musqvgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله این چه فیگوری است دیگر!
انسان گمان می کند که نعوذبالله دارند با کله نورانی شان روده بزرگ کشورمان را کلنوسکوپی می کنند!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20054" target="_blank">📅 15:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20053">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بفرمایید:  ‏ فواد ایزدی: اگر ۲۰درصد نفت دنیا را حذف کنیم؛ اقتصاد آمریکا فرومی‌پاشد!  با این کار نفت ۲۰۰ دلار خواهد شد؛ باید تصمیم بگیریم که تاسیسات نفتی منطقه را طوری موشک باران کنیم که دو سه سال برای بازسازی زمان بگیرد. ‎</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20053" target="_blank">📅 14:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20052">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نه دارو داریم نه بنزین نه برق نه نت نه گاز با تورم 300 درصد و رشد اقتصادی منفی و ریاست جمهوری دکتر پزشکیان و 2 جنگ بزرگ در 1 سال اخیر با گرمای 50 درجه تابستان و سرمای 20 درجه زیر صفر زمستان اما دغدغه جوان ما این است که رامین رضاییان به آن دختره چی دایرکت داده!…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20052" target="_blank">📅 14:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20051">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20051" target="_blank">📅 14:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20050">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20050" target="_blank">📅 14:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20049">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBLF2XDLvoxElxYJ3_hgwRJwXNVkwj34nQh_wg_y793I_Obu1qmRW7215h-DvBwkS-w_B5mY_Ijg03LiP4rnwfa002KZhdIhQDYRV0Dx8a8N3QhExDlazbXO9uEEAm0EkW34u3JkuLAE2gORb6xkrxbe4syVtzsBg8q5-GUA6EzctNk8mSW6rubgoHmsratpVkNOXzJ0IuMiK5aj3hxl1dBmQUZ-1AXKy-A8WPbPOh6j-ZX0tR_617XT6WRtetoXagS_dmOrW6NXCXYUirbBE_wxDB6fz0WwGYAExZ-HRlM_qNRmS9MLWMX7K5-ofEUar5Mm4hCPuncwSvaTBraDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای یک نفت کش در خلیج عدن!
به نظر می رسد حوثی ها تصمیم دارند کشتی را بدزدند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20049" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20048">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اگر آلمانی ها به جای ما در این میهن اهورایی می زیستند تا الان نسلشان افتاده بود.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20048" target="_blank">📅 13:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20047">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">طبق داده‌های دولتی، آلمان در این تابستان ۱۴۰۰۰ مورد مرگ ناشی از گرما را ثبت کرده است</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20047" target="_blank">📅 13:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20046">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📌
وخیم تر شدن وضعیت صنعت آلمان در اثر جنگ خاورمیانه  صنعت آلمان که پیش‌تر هم تحت فشار بود، با آغاز جنگ خاورمیانه، افت تولید صنعتی، کاهش رشد صادرات و افت محسوس مازاد تجاری در مارس، وارد وضعیت ضعیف‌تری شده و احتمال بازبینی نزولی رشد اقتصادی سه‌ماهه اول را بالا…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20046" target="_blank">📅 13:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20045">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل:  «ما حضور نیروهای نظامی ترکیه در سوریه را که اسرائیل را تهدید می‌کنند، تحمل نخواهیم کرد.  ما به روشنی گفته‌ایم که حضور نظامی ترکیه در سوریه را تحمل نخواهیم کرد و به نظر می‌رسد که آنها حرف ما را خوب نشنیده‌اند. بنابراین، ما اقداماتی…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20045" target="_blank">📅 12:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20044">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نماینده مجلس ایران، ابراهیم رضایی:
بهترین پاسخ به تشدید جنگ اقتصادی توسط ترامپ، خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) است.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20044" target="_blank">📅 11:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20043">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سخنگوی سپاه پاسداران انقلاب اسلامی:
قدرت تخریبی سر جنگی موشکهای مورد استفاده در موشک‌های جدید سپاه، بسیار بیشتر از سر جنگی هایی است که در جنگ‌های قبلی استفاده می‌شد.
اگر جنگی آغاز شود، سلاح‌های ما در تمام جنبه‌ها کاملاً با گذشته متفاوت خواهند بود.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20043" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20042">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqLfzGZnxzBBKpD17GkkOyovmPG411YD0A2hHTIVTo4Mq3TdZyYYtnkb7yJPQalOitxLkbVQgjxSScirbLkiobTqb9zCoKnkH8M67Au8tCOiYgZLyUuh2qinFfEhRtLumqNrzUFjnIx5fj6Ptql-GCKlUJuqyyTnsU4b9pdOBjh964ylWu0c0xXaqsE3X-mYHSSLjSeheXrlbXK09-qAqdK-lvRflzjmbMLQdnZDYhBZEZqyje-dNWjk2OyYuxuAg3shZp8eUJxew8PZ7tpF2CF0Gch2fYOwINhIgI1FNU2CgOcgiPR6JK5tuN_5UMbENpstsPD4RTDBfRP-ZujqHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در بالاترین سطح خود قرار دارد و تقریباً در چنین شرایطی محال است که امروز شاهد سقف جدیدی در طلا باشیم.
انتظار افت دستکم 400 پیپی دیگر در طلا دارم.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20042" target="_blank">📅 11:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20041">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20041" target="_blank">📅 02:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20040">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20040" target="_blank">📅 02:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20039">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ:  هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.   بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20039" target="_blank">📅 02:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20038">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:  هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.   بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20038" target="_blank">📅 02:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20037">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ:
هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.
بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی آنها نابود شده، نیروی هوایی آنها نابود شده، کارخانه‌های نظامی آنها ویران شده، پول آنها بی‌ارزش شده و کشورشان در آستانه فروپاشی است.
علاوه بر این، من امروز اعلام می‌کنم هر کشوری که به مؤسسات مالی، شرکت‌ها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع حمایتی از ایران ارائه دهند، با عواقب شدید اقتصادی روبرو خواهد شد.
قاچاق نفت، خطوط مبادله، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها و شرکت‌های پوششی - همه اینها باید اکنون متوقف شوند. خودتان می‌دانید. این یک روز اقتصادی محوری خواهد بود و ما به همه متحدان خود نیاز داریم تا در کنار ایالات متحده بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها در آستانه فروپاشی هستند و این اقدامات تاریخی آنها را فلج می‌کند و توانایی آنها را برای گسترش ترور در سراسر جهان از بین می‌برد. ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع متشکرم.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20037" target="_blank">📅 02:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20036">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ: من خردکننده‌ترین عملیات اقتصادی علیه ایران را اعلام می‌کنم</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20036" target="_blank">📅 02:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20034">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromExciton Computer Missile Program</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da68894d0f.mp4?token=X4W6U7l-61SyAtS2I8YI-sB8sYK34KkCmoXYc4NVAyJ-xB6pEbS4hhJuHfnNtPvJWM_nTCw87t7lbOwxfOAB2nZ2xzj4Y9y7CgN0rYwEGICP3A4ZsFN10ciaZWUMM-X4lnkHRUEMV5mBpMVTYQRQFMHisRCkvjAIUVUsxTrrt5n0AFg3JVxSfSuT7qRqdPL7n6Gv-AS5tRam8MGdPG_LKHkqSjBCGGtL9ZEaW6plCD06k3KOrexhTt2p5zL-lQCmiagoSUrSVqxkQO0qpsWFW0YKh_vR7sz1SqKpgrQ3zGk-xgRgkbifaOwNkHOCg1dHQCXvcazkp8UEfFWXLHuSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da68894d0f.mp4?token=X4W6U7l-61SyAtS2I8YI-sB8sYK34KkCmoXYc4NVAyJ-xB6pEbS4hhJuHfnNtPvJWM_nTCw87t7lbOwxfOAB2nZ2xzj4Y9y7CgN0rYwEGICP3A4ZsFN10ciaZWUMM-X4lnkHRUEMV5mBpMVTYQRQFMHisRCkvjAIUVUsxTrrt5n0AFg3JVxSfSuT7qRqdPL7n6Gv-AS5tRam8MGdPG_LKHkqSjBCGGtL9ZEaW6plCD06k3KOrexhTt2p5zL-lQCmiagoSUrSVqxkQO0qpsWFW0YKh_vR7sz1SqKpgrQ3zGk-xgRgkbifaOwNkHOCg1dHQCXvcazkp8UEfFWXLHuSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حمله امشب به کیف این احتمالا موشک اسکندر نیست. این احتمالا موشک بالستیک سری KN کره شمالی است که با سرعت بیشتری روی هدف فرود می آید. مانور pull-up شاید کمتر باشد. اما باز هم زاویه نزدیک به عمودی و تیز را مشاهده میکنیم. سرجنگی هم مشخصا بسی سنگین است.
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20034" target="_blank">📅 01:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20033">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیروهای ایالات متحده به‌صورت پنهانی یک کریدور حمل‌ونقلی محافظت‌شده از طریق بخش جنوبی تنگه هرمز را گشوده‌اند که به ۱۵ تا ۲۰ کشتی تانکر اجازه می‌دهد هر شب از آن عبور کنند.  مسئولان می‌گویند این عملیات اکنون تقریباً ۱۰ میلیون بشکه نفت در روز را جابه‌جا می‌کند—که…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20033" target="_blank">📅 00:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20032">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ:  ما کنترل کامل و بی‌چون و چرا را بر تنگه هرمز در اختیار داریم.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20032" target="_blank">📅 00:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20031">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل:
«ما حضور نیروهای نظامی ترکیه در سوریه را که اسرائیل را تهدید می‌کنند، تحمل نخواهیم کرد.
ما به روشنی گفته‌ایم که حضور نظامی ترکیه در سوریه را تحمل نخواهیم کرد و به نظر می‌رسد که آنها حرف ما را خوب نشنیده‌اند. بنابراین، ما اقداماتی انجام داده‌ایم تا مطمئن شویم که آنها این موضوع را بهتر درک می‌کنند.»</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20031" target="_blank">📅 22:43 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
