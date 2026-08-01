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
<img src="https://cdn4.telesco.pe/file/groI5xTpwv63gfZoi6J4nCDzOlcRYiL7alhPvmfSys8QS9iuFLn3N4KNX-dCNvym4v7j0bdQxS-ogrXW9QKkfhpqlFGC3LOOBlCFSi8DRxzRuhYuE12uKp8IWm5Q8oYnn5Dd6VABPOEdQ4RbRomkd5R03bDxF0BH2YU7It7nbLOcUU9Cvz57HF-l9sqznIzP27GAnZa4Wd98L-up_IT86s7Q0swHckr9_HxE5knU8gqfbWkSkbl1uv0dmCtMAmd5XZjW_L0lexBSNtKYIUgxAC_TWi6gkWzI0GZNdqQS4Ab_2Urlor3LYszHLvS5KhYuyEDAEpu4KLX0Q9TxtVkY0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 19:05:43</div>
<hr>

<div class="tg-post" id="msg-69375">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=R_YOXNtR5wfhaNV86wfRkXXxhRXQ6QTM17KIGc2OPCJ92b1UTjjvIio5xTNtgps3EV_qGBa4avDap5v6fqtYXhOARvoDJcyFKC-dQk4jl1EkmdMuWTk6rIQHSfJ6Ed3Au2PPvLbKGAJ_WXPKuLc2-88xYrNvfZDbHLRUTuSrPOg0vu2D-wq1uewmQTHROaINrATOS0-Nu3iiemtYlcBD3c0TT7r8XjHBQfJksBmnpF3xLBoTlGW7bT8V717LbneMNgEKtDx48k9WfTombTpTOiNtrxGj_W8KPzYwA-dVtH6yIj8LvTSQxrgYBuCyjxBlD1kZLH0HL_ugrbWl0BsAFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=R_YOXNtR5wfhaNV86wfRkXXxhRXQ6QTM17KIGc2OPCJ92b1UTjjvIio5xTNtgps3EV_qGBa4avDap5v6fqtYXhOARvoDJcyFKC-dQk4jl1EkmdMuWTk6rIQHSfJ6Ed3Au2PPvLbKGAJ_WXPKuLc2-88xYrNvfZDbHLRUTuSrPOg0vu2D-wq1uewmQTHROaINrATOS0-Nu3iiemtYlcBD3c0TT7r8XjHBQfJksBmnpF3xLBoTlGW7bT8V717LbneMNgEKtDx48k9WfTombTpTOiNtrxGj_W8KPzYwA-dVtH6yIj8LvTSQxrgYBuCyjxBlD1kZLH0HL_ugrbWl0BsAFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
دونالد ترامپ، رئیس‌جمهور آمریکا، و ولادیمیر پوتین، رئیس‌جمهور روسیه، در قالب «زوج در حال بوسه» در رژه کانال‌های آمستردام:
@News_Hut</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/news_hut/69375" target="_blank">📅 18:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69374">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=mcC25WNjfPpe3mFYw0muWlLVsSB0vrKpW-YRQPiZ5QQbbQqNzhf7jPx-xrI-ZBCBDrqzBfxZmTHbpdGNyRhz-M6uuWl8R9cG5fb4jR2mEc1t2Hx2v2iTJdcBBC3XbbPVblnmHegpjQ_R8e7FGRLDRUy7A99i7o3abFXj2uZKqcHnTalpI_fGKk8zdchHUPeiaEutMU3ENc_epEPndef9VR2iNt7LKWq8bpSKkY66F4e5X86RQ2Ta-_CdTPd0o_yUJ4YaN2Lm-jnM7wHMXvvOmozGzKSq6t1-9pt_s9A8MgpMezmOezyr1YuJutrPzoZd37z4oqCzlMg5BJm_wAdLIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=mcC25WNjfPpe3mFYw0muWlLVsSB0vrKpW-YRQPiZ5QQbbQqNzhf7jPx-xrI-ZBCBDrqzBfxZmTHbpdGNyRhz-M6uuWl8R9cG5fb4jR2mEc1t2Hx2v2iTJdcBBC3XbbPVblnmHegpjQ_R8e7FGRLDRUy7A99i7o3abFXj2uZKqcHnTalpI_fGKk8zdchHUPeiaEutMU3ENc_epEPndef9VR2iNt7LKWq8bpSKkY66F4e5X86RQ2Ta-_CdTPd0o_yUJ4YaN2Lm-jnM7wHMXvvOmozGzKSq6t1-9pt_s9A8MgpMezmOezyr1YuJutrPzoZd37z4oqCzlMg5BJm_wAdLIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
فاکس نیوز:
رئیس‌جمهور ترامپ در حال تشدید فشارها بر ایران است و می‌گوید در صورتی که مذاکرات دیپلماتیک به نتیجه نرسد، انجام حملات نظامی جدید همچنان یکی از گزینه‌های روی میز است.
ترامپ پس از دیدار با اعضای کابینه خود در «کمپ دیوید» اظهار داشت که توان نظامی ایران به‌طور قابل‌توجهی تضعیف شده، اما این کشور همچنان از برخی قابلیت‌های موشکی برخوردار است.
مقامات آمریکایی می‌گویند این حملات ممکن است حتی در همین آخر هفته انجام شود؛ در مقابل، ایران اعلام کرده است که در صورت هدف قرار گرفتن زیرساخت‌های حیاتی‌اش توسط آمریکا یا اسرائیل، آماده پاسخگویی است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/news_hut/69374" target="_blank">📅 18:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69373">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=Wsrh4nd74zoXL9T5nXTjTYJ8-Q3XT-JcbwUWtz6T8kU0zzP953rz2heaVh5ncByg0Ld46SiEGn4QLZmt2DUh7b6H8Oaa8eDUYI5A0O9O9sutmowrqGETfApIjpLj_WU2k1wAoYqJZWhhVhBm6efYsNPqvKD0XE4BEA37Z4myKaiC5EWh1swSAvXsb3n9u5EPc4MHp3qfk4ewd3-FHBI2RaF0ggkaRGizZNhXuu9kJv7dXQ_JdCaOaQjLrzO18IFD9nBvub0nHP1TnXFQQIcYwYpTgrGPj8Lv3vZ56UuEY8bTbJd3LnucOLos8Unznz9lCJTSPA_-o3ZH7-MjOXl3Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=Wsrh4nd74zoXL9T5nXTjTYJ8-Q3XT-JcbwUWtz6T8kU0zzP953rz2heaVh5ncByg0Ld46SiEGn4QLZmt2DUh7b6H8Oaa8eDUYI5A0O9O9sutmowrqGETfApIjpLj_WU2k1wAoYqJZWhhVhBm6efYsNPqvKD0XE4BEA37Z4myKaiC5EWh1swSAvXsb3n9u5EPc4MHp3qfk4ewd3-FHBI2RaF0ggkaRGizZNhXuu9kJv7dXQ_JdCaOaQjLrzO18IFD9nBvub0nHP1TnXFQQIcYwYpTgrGPj8Lv3vZ56UuEY8bTbJd3LnucOLos8Unznz9lCJTSPA_-o3ZH7-MjOXl3Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک هواپیمای سبک قاچاقچیان کلمبیایی در حال فرار از رهگیری توسط جت جنگنده ونزوئلایی.
@News_Hut</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/news_hut/69373" target="_blank">📅 18:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69372">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=THLCWQM79ZxNrfw7RzWz96Y4rwNzr8EpZSTFPhJPWrRfJC9maZYQ8MmN7vPZMDBgjoD-9If6U5izPKSgHEeceUgQZfQDERzeq2ZsUvFpanNceZpznoI93yIH7FetrLikmcwtew-PxT8fBlHyeBE1fLRRte-jhjcutUQ2ZAqWGLjUdYnL0EZ2mVBUizqV-osEMkyvA7BefaOwOjQZkYqL23iGl6tIBPVHFcnCP8QK34lYCoTm8oY3W5GN1YuVJXwrUQY2HZkdliaXWCVfAemcU2H1K5LqhpTNgmNpHEflp2bXt01esHz5ubjuurIML-D6J2FyOBNC0EoZrtyCM4auzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=THLCWQM79ZxNrfw7RzWz96Y4rwNzr8EpZSTFPhJPWrRfJC9maZYQ8MmN7vPZMDBgjoD-9If6U5izPKSgHEeceUgQZfQDERzeq2ZsUvFpanNceZpznoI93yIH7FetrLikmcwtew-PxT8fBlHyeBE1fLRRte-jhjcutUQ2ZAqWGLjUdYnL0EZ2mVBUizqV-osEMkyvA7BefaOwOjQZkYqL23iGl6tIBPVHFcnCP8QK34lYCoTm8oY3W5GN1YuVJXwrUQY2HZkdliaXWCVfAemcU2H1K5LqhpTNgmNpHEflp2bXt01esHz5ubjuurIML-D6J2FyOBNC0EoZrtyCM4auzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح تو یکی از حوزه‌های امتحانات نهاییِ اردبيل، 9 تا از بچه‌ها مونده بودن پشت در و داشتن گریه می‌کردن؛
طبق ادعای خودِ دانش‌آموزا، مسئول حوزه ساعت 07:03 در ورودی رو بسته!
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/69372" target="_blank">📅 17:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69371">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
ویدیو وایرال شده از این هموطنمون که در زمان شاه حضور داشته :
زمان شاه به دانشجو هایی که میومدن اینجا درس بخونن ماهی 400 دلار حقوق میداد
اون زمان صدتا نارنگی یک دلار بود
یه اپارتمان سه خوابه تو نیویورک میگرفتیم با سه تا توالت و حمام اجاره اش 210 دلار بود ما ماهی 400 دلار اونوقت حقوق میگرفتیم از شاه
شورلت کامارو یکی از ماشین های اسطوره ای امریکا بود سه هزار و صد دلار
با یک سال تونستم ماشینو بخورم
امریکایی ها میگفتن کجایی هستی میگفتم ایرانی همشون میگفتن شاه شاه شاه
کدوم شاه شما دیدید بیاد تو امریکا براش با کلی عزت مراسم بگیرن که برای شاه ما گرفتن
چه افتخار و عزتی و لوکی بود شاه واقعا نوع بیانش و لباس پوشیدنش هرچیزی نگاه میکردی لذت میبردی
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/69371" target="_blank">📅 16:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69370">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE9fLWH6pOFQDtAWaRrlGBSZHeflZZk9HVBfdCAbeoMNCA_hEe_mdk8qPJHRWjAbTJ8vpNSxDKD47MPHHSYvBxB_rm6kSaZ4nWGlLy35_g8U1kXkBurxq5yNDCHl87VZ-00lA7WBgyffGYYb2xmopWLPcqNE_11r3kjdTJLqRn5TSbQZowJKf5R5uf3beCl7xbXEAPBgDnnGlW9qyJYgR2pSjP1-cOlm57o2S36hgeJwdip_DO_HV-hU8dNnZ3Yng5NL3AWtKAZ8YjYtqm-S8DK_oPghQRoh5oeEgQqWmrKiTai7jBEprtKH2vOzigB0SyGluDkVNMhrovR8fi1UpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سفارت آمریکا در مصر هم برای شهروندان آمریکایی هشدار صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69370" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69369">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=I0WVpleK8FhuxlwBYV3jnDSbd3zr6pAhciMpRuLs8dJCHjJT-hdPSrPJTOaWCVIAH1AWOTkuo1d4-_uf1aHCisCiptLRmOoiOrQ6UAutglBeX1Rl5RhVCIY8AyWb_Vkp1mGudCMGa3lqX4aCmlvHHJ5rw1EG2sOD7vSFaL8FLRBx3L4l9JBoIp-UzMPuqQeNVFgLX5hBEU7lBhrcyXXqEFrSSbE_j-okh65N0gSMY2zz9ZUtP9tSHKfVMq3YlsMjREXeHwqGYlf6LAsqEJAKuQhXiOWcTFyw04iIchKff_GE9cKMAYvCmdIu3gcqagM4ogSOe7_sss1L5pHR29Ioxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=I0WVpleK8FhuxlwBYV3jnDSbd3zr6pAhciMpRuLs8dJCHjJT-hdPSrPJTOaWCVIAH1AWOTkuo1d4-_uf1aHCisCiptLRmOoiOrQ6UAutglBeX1Rl5RhVCIY8AyWb_Vkp1mGudCMGa3lqX4aCmlvHHJ5rw1EG2sOD7vSFaL8FLRBx3L4l9JBoIp-UzMPuqQeNVFgLX5hBEU7lBhrcyXXqEFrSSbE_j-okh65N0gSMY2zz9ZUtP9tSHKfVMq3YlsMjREXeHwqGYlf6LAsqEJAKuQhXiOWcTFyw04iIchKff_GE9cKMAYvCmdIu3gcqagM4ogSOe7_sss1L5pHR29Ioxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیرزن ایرانی توی مراسم اربعین، برای اینکه از یه زن عراقی صندلی‌شو بگیره، بهش حمله‌ور شد
😔
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69369" target="_blank">📅 16:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69368">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حالا ما کجا بریم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69368" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69363">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eh3fX4vDRDMJLy6yTLWL-2smCQh__1TilPtaFOYeHh9rEcPOh6E9YD6A_5pcLwe6WsKRxx85VTZ2muu3M53ecf_zhbahSIxDlWPjDeUU3kZAMDgfSJPjIFezAsTYSBCURHgB7eJCkZJkar2YTpIkVh4yQQHCOHPMmQr0A0UxXfQH6EKbwjLFLgSH_B3hjfGahvWDi-1isXdHD6IlcCr2KJlhqbhGXrUAV-BjWJlXpGuPyw2XtRUEotx6GRNgY6U1_XqQrbxbL1ox2p9IQY2-Uejq1zgFlBp7SfhAKORO4-cEF1XhuHVwK4cZx2eFNRf2uxZpl-T2IakeaTsL2QjQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBQR8FinZQPg_rF83P-491OUCBhjH4gWDgSw0nxtVCLy336gvZ8vmcb4Bl5l3TofbdIicjwxwuTUsgf6Ho8hwF-PwVxPm5Tp7eqqHS_hU8AlCVLyPyGZ4g5RTi8iRRiItLB5ke5q1SBdKxQ1kxzqgDsKIs31LIyZLL_VK0Ellc7jkTSqxKOcZ930ie_3jk97U_EKQFelsatVsY7Z1TJpulDOlu4ui44wAGYvv5J2O5agnazyYUMCfT1FtZcEFOrxHvMWYXVNVo3AqYQ76V8FfZgB4zWNiDbnubyE9ymRtoM42ZDAAGtL0o75WWoj_VQK1V3NiFVL4z8eoZoRpKsxsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzPDK1d78ZZrNveDda3ibRqfh7XAgfgc4SHhHbyw3iwYn5diBasuWFCqOzlmT-NzWOLFZMu7YgqueKGGKTfKp5u9Z113lCUsTw5h6NvjsFUsNjLzy5eM3niN60frbq4zXaL4EB8SdCZJBMQJXzbdqvUMhU49CUIzCzcyP2XGW6P8UCwQh0YSO246C6flJ44Dw5h1xvxV3zwdZSMpyHi6P6F0sKpj6dp7MKflBeLqNIBGvGej9OvmgtkxWXb172G71DGIe_-M2CNR-I-kyfNPdXxWkZJ-7xJTEpt3ye2z9XFl1HeNthcswPd6CoThmLeYB7kfGEaxVfVoh9MShysgcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdyGZEQu2mAS4NnT3tL_aBrONKD8G3ZGd67v5Je3jTQ0lz4DQ9iNyq6UGTnEVU2F__dVUgdjfVL6V0bPFhiKoa9PVBfi3_A2pa2CEMV5PCUKq5Tc7XPMJfoHQL-0K-PrOIyt3rCEG67_J-zdOZQe-gOGluziWzkMvfGzMPBlNJhCu0p9kZukAHJZoEtm-HcNtn514ZKd__xLwqxNATn77Uprzbwl4OUf3bI04JG30jG-k_E3LvWy4zg2kVxnn-Eyg5_-pk30jakyPx4xFGp1rUz8oNnvnk0-JE6iDFYCU-12dEF5ldRsZf57jwwhFl4BP4kQWp0lZxpMMtwmBzRqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2Qr-t9v5KPtgHn63Lbn21DoaFI0jeMST9-f6SIhVguyRbl-ShzxF_5AUIjMS314AiEUV4S1xj7pku7Y5H1-ZkwYFeIwqSzBqs10YZihMRHS9-DeIUecELIrsEZHcpiCtIfG2AmqoaTKpZHQ0Sp8Lxj0Fh53U-WmX6WW1YV74E7UOVJCO84EvkHHAK4PGwciH8y6wDeIcJVV0MOjYDwA646DwAveXVO6s9_ZQDYvrbJSkLyM-hhXxt7O-DRSunfVuEu2CY48auz1js-3HEljPofKbLUnwk5sgz43ClzIhREKAn7qqdTv2QQpcGvYKWPgcXUbU-7h0l4GkqXYOhDuJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارتخانه‌های آمریکا در خاورمیانه یکی پس از دیگری درحال صدور هشدار به شهروندان خود هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69363" target="_blank">📅 15:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69362">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=B8VmWDOsz0J-fflxwKHSmJe4vn5DgMS_Jb73GbvA4jsXP0tvAxOOAcrUOiMJtKzNVZlKzbSpiICX9hP1H0CAD24uWW3tqbo4slN-bH7HzPgfHF_PxLwjWfGSUPBQS585bqqUlSPT84gXgnMSwjM2_C-ErMKZhzWyZmcvnPiFmqPdsNxjDpcM1VUnZHdsGHqKdl49Nff4-hkvAbjM4tvJtD5zozQcOBxMBUNG-bT_Cc60P5NSxzIaUjpcjhejp9wLEjp5ujP7pd7JEmQIsjCMsKOMLJG4ByFuI-kdO7qBPqOx8B3l0RPOUFN0lMZNTiWRaySjfRFUHamI6BH3qi0r0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=B8VmWDOsz0J-fflxwKHSmJe4vn5DgMS_Jb73GbvA4jsXP0tvAxOOAcrUOiMJtKzNVZlKzbSpiICX9hP1H0CAD24uWW3tqbo4slN-bH7HzPgfHF_PxLwjWfGSUPBQS585bqqUlSPT84gXgnMSwjM2_C-ErMKZhzWyZmcvnPiFmqPdsNxjDpcM1VUnZHdsGHqKdl49Nff4-hkvAbjM4tvJtD5zozQcOBxMBUNG-bT_Cc60P5NSxzIaUjpcjhejp9wLEjp5ujP7pd7JEmQIsjCMsKOMLJG4ByFuI-kdO7qBPqOx8B3l0RPOUFN0lMZNTiWRaySjfRFUHamI6BH3qi0r0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده‌یاد مانوک خدابخشیان: دو شعاری که کار این رژیم را تمام کرد؛
رضاشاه، روحت شاد.
اصلاح طلب اصولگرا دیگه تمومه ماجرا.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69362" target="_blank">📅 15:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69360">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MF55sVkMx6tJwMq7iEV5cmHfiEJgNyK8dZvkvfK944Mc897vksBO9OS0yd3I0h-THTlgugwUVO-B_ODfh2Wp-DKWhMFn7NR02zXKjjo-3zI7ldgeRe27UkbWIZ8111oy7F5fDRtQCpoXTG4BfVFCycrZtixftIzj_HbTQyrA6Ybr17Q3J-Lf6UdA3S6Cj7rIt_waVLcJKOKZ5PqlddpRBlEoM5Dk4wC7SUgZRP67OYo_pae7KEWEASDmC2b4UOHl-7Oy_UTBxr0uAz8FUv5g3I2Z2v1Fh39Mf6bnDND6MFnNO8QE431UPXtuepmnv_AHAhehJedc2TKzvQfxUg4b_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_dyHqVFbzlAhCW9qC6bLeHjS_1dIPa4DH_BaaTYBGsqNKrcBWipWFWz7lDHK1uREA84ElSyN4EHmQ9scU9s4C5iaJs_Zu0G02Ja_moEAwEeRFJ--ePMO7NPAhniL1RE2Z-vLznvERf6r8HGEFnqWNx5x34zD4bd8hG6MEm4u-lyVzXxvi3ZzCHL8qsajtVIGVmL9hg1VNFHxCTENVPmSAgIgTVFV7BJP8lBbdP6kFl6wMBkWXv7z56rP7Oft8_38ShP2hNJXiPYgRrOONwS7XocW8Vj8BfG_KqojCRofNYwMVVLlN--A7lVKpWB8zpj6DmNsv-ou9IPAvH1toKIXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارت آمریکا در اسرائیل و عراق:
آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69360" target="_blank">📅 14:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69359">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz4SiBeuFip66tG-OMYnXwo44le9Vwu22SxgprTP-et7LAUIGMR9kIir3J25MvRZyqJdfzzN5Qi0psPkRoniGE1RBBguqrAqaq_WBMRktVOGbNUcW_az-BaYfN2mu7eTthunjhdzRQyn9EfzGIaRmoV_uyFBXADFgaOFFS5jkEkG6iJ-B3gycrow3mvvR3uO0juIZwNyQqn4i6TQtw5wfnks_22t3wzcyY66OgZ7nkbFWerkLGaJ2tAyza7Ucfwgr3wp8HZfO69PlCXpTe2UESYNuoWRXRhEhe-5GkvkiMCtmk3GedwkjrnAlCXlLxjDQG4c1FTcafoHsjJS7aLAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:  بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69359" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69358">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
تسنیم:
بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69358" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69357">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
دقایقی پیش از حوالی اسلام‌آباد غرب کرمانشاه، صدای چند انفجار شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69357" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69356">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=OirU70hTBtw_mLwloGcQ_8J4RTiPedGODYFn5UXdTuxNCwIyyzQTDpT1Gp_QTv0fzXmNJAQgHZUHQaZmqkwnWlsp1i6Q20vYpgytzSMgSS7ryxMbyXS0Hif3jOH4RlKzvSaoDPt4Z5ZCxzJhUITYTtHPOWkPweicXzoqeGmzmG1Jvju0RdPWhZp9U-A7lvHz-ybWmd6FNP5Ya6_C99liVVjonmq8zVDtopaAHmVwxS5Qo3790HGQ86uhVmRkP9aDjtWT8ASLcLNaowE0cBhdp2bR5I7khIGgPCqMRmAlnT12dmRnei4FjvVv8iVR44C_KS1A8V3AlsYEN5E59YlEVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=OirU70hTBtw_mLwloGcQ_8J4RTiPedGODYFn5UXdTuxNCwIyyzQTDpT1Gp_QTv0fzXmNJAQgHZUHQaZmqkwnWlsp1i6Q20vYpgytzSMgSS7ryxMbyXS0Hif3jOH4RlKzvSaoDPt4Z5ZCxzJhUITYTtHPOWkPweicXzoqeGmzmG1Jvju0RdPWhZp9U-A7lvHz-ybWmd6FNP5Ya6_C99liVVjonmq8zVDtopaAHmVwxS5Qo3790HGQ86uhVmRkP9aDjtWT8ASLcLNaowE0cBhdp2bR5I7khIGgPCqMRmAlnT12dmRnei4FjvVv8iVR44C_KS1A8V3AlsYEN5E59YlEVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه جوون عرب داشت به زائرا میگفت بیاید آب انگور بخورید که یه ایرانی رسید و بهش گفت:
آب‌انگور نه، بگوآب‌شنگول
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69356" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69355">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69355" target="_blank">📅 13:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69354">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه لیلی فیلیپس پورن استار معروف که تو 24 ساعت با 2 هزار نفر سکس کرده بود!
دوس پسر لیلی: من اصلا از این موضوع ناراحت نیستم، چون اون واقعا زحمت می‌کشه.
مهم اینه که آخر شبا میاد پیش من، و اینکه من بوسیدن رو براش ممنوع کردم، اگه با بقیه سکس کنه مشکلی نداره، ولی فقط باید منو بوس کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69354" target="_blank">📅 13:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69353">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26851041.mp4?token=IClJstb4n9BxDgS6YI5eTi1Gx-1KeKlKpd1Vw5r9dEju63Q9w8EzA9QKcS7E4mVefY6TxEh5hvZHCwOIikv9lpo4FFxQTkHnPPhRIjEWCQYJScSBYUbl5gSbEdsjmobqo-799NccpAQp4GDYNRdl5e3q639mYbJ7RykqJubsC_VzyayxTaI85fFYm4gWuuvH24dquET7Dfo3UUcPTIer5PDS7CbvUJeQ7aSzCPHnxkllTruearGM0vy7WG-rjwzGK60kbKeo-REro8bSbCQ4fCzKh70Bf0QlmMzG3pmtjPR9QIe4G_pZGvgvxN3iHnY9AUdH8js78t_X4mVcoyjjBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26851041.mp4?token=IClJstb4n9BxDgS6YI5eTi1Gx-1KeKlKpd1Vw5r9dEju63Q9w8EzA9QKcS7E4mVefY6TxEh5hvZHCwOIikv9lpo4FFxQTkHnPPhRIjEWCQYJScSBYUbl5gSbEdsjmobqo-799NccpAQp4GDYNRdl5e3q639mYbJ7RykqJubsC_VzyayxTaI85fFYm4gWuuvH24dquET7Dfo3UUcPTIer5PDS7CbvUJeQ7aSzCPHnxkllTruearGM0vy7WG-rjwzGK60kbKeo-REro8bSbCQ4fCzKh70Bf0QlmMzG3pmtjPR9QIe4G_pZGvgvxN3iHnY9AUdH8js78t_X4mVcoyjjBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عوارض خوردن ساندیس زیاد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69353" target="_blank">📅 12:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69352">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=BNe1uKx6bCyWZ4ar9S3OjP6zKZZUBM7MpoiiYYm6LzYqIPyQq68Vaoj_DwaTyV2iPY05BwHmRcf7IcNnPVJDoXY_asKPfeawpSdjxbLo-o4I6EBCaF3GcE3rkBtldsMpmvzYKmL05JuNu-TS1i3ls-X7CIAlXLXA7HMD1blhlY7HIILFAW7rDDftbWCTAoz6FfaLt6DLxGasp7xHa3-7huoyam_C1GhszJnveZQlEo2c-pWreMQ9J_ZeSaQrXDLM0uSspY0AiphnWLOx3Z7ujUGe9ze2oZdDCkN9aZlP3vtjCQgJjiIxG_U0tuXAPvTzSD6uhOXE3ZdvAFXP1cIOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=BNe1uKx6bCyWZ4ar9S3OjP6zKZZUBM7MpoiiYYm6LzYqIPyQq68Vaoj_DwaTyV2iPY05BwHmRcf7IcNnPVJDoXY_asKPfeawpSdjxbLo-o4I6EBCaF3GcE3rkBtldsMpmvzYKmL05JuNu-TS1i3ls-X7CIAlXLXA7HMD1blhlY7HIILFAW7rDDftbWCTAoz6FfaLt6DLxGasp7xHa3-7huoyam_C1GhszJnveZQlEo2c-pWreMQ9J_ZeSaQrXDLM0uSspY0AiphnWLOx3Z7ujUGe9ze2oZdDCkN9aZlP3vtjCQgJjiIxG_U0tuXAPvTzSD6uhOXE3ZdvAFXP1cIOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: میخواستیم خبر شهادت رهبر را ساعت ۸ صبح اعلام کنیم اما تلویزیون‌های خارجی، زودتر اعلام کردند
.
در روز نخست جنگ و تنها یک ساعت پس از بمباران بیت، شهادت رهبر قطعی شده بود.
تا همدیگر را پیدا کنیم و هماهنگ شویم، ساعت ۸ شب شده بود.
قرار شد خبر را فردا ساعت ۸ صبح اعلام کنیم و از مردم بخواهیم به خیابان بیایند. اما تلویزیون‌های خارجی، [ منظور اعلام رسمی ترامپ]  خبر را ساعت ۹ و نیم شب اعلام کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69352" target="_blank">📅 12:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69351">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⏺
سفارت آمریکا در اردن:
از شهروندان آمریکایی مقیم در خاورمیانه درخواست می‌شود که برای ترک در صورت تشدید اوضاع آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69351" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69349">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=eAjWgnd6GnvSl34MLUwmtEhwGII3ZfU7RA3p2yCXyTvGBn1aGiEtFGf1fQ4DaxhE0gyLdbS5GMeuwArdj_tWLudRP5Y2jh35VSHVAYLKhU6Xw538qHMu_s6MbIeMl3pcEA0Rh8ztWY2UwubY_Da31gS_nWNA8kGZyM_3yOaR6cAba-0ty7hMLwebOaEEoi6KRxViI1zO7uMtcGyaJV3dOzpTgACfOvanl0BxFuRrg_YUDW44-Apb2m-k55Ex-NVrTehjmFkKJsaQAY0evst-A2yUcgPUu2_Y0hcmgtKHYwcOcvjQ-tP_TH0Cl2jeUkB3Lf8fBZr3-6k_5lMVJ2BMDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=eAjWgnd6GnvSl34MLUwmtEhwGII3ZfU7RA3p2yCXyTvGBn1aGiEtFGf1fQ4DaxhE0gyLdbS5GMeuwArdj_tWLudRP5Y2jh35VSHVAYLKhU6Xw538qHMu_s6MbIeMl3pcEA0Rh8ztWY2UwubY_Da31gS_nWNA8kGZyM_3yOaR6cAba-0ty7hMLwebOaEEoi6KRxViI1zO7uMtcGyaJV3dOzpTgACfOvanl0BxFuRrg_YUDW44-Apb2m-k55Ex-NVrTehjmFkKJsaQAY0evst-A2yUcgPUu2_Y0hcmgtKHYwcOcvjQ-tP_TH0Cl2jeUkB3Lf8fBZr3-6k_5lMVJ2BMDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک انفجار بسیار بزرگ در یک انبار مهمات در شهر خملنیتسکی، واقع در غرب اوکراین، رخ داده است که پس از آن، انفجارهای ثانویه گسترده‌ای نیز به وقوع پیوسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69349" target="_blank">📅 11:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69348">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=d4x8oB1GNsfqsmTRGHs-cDkcsXkgS666U4-nv4bGgo1V0We-h7dke5LFh3ZEcq1CJmdQ4eu29S1FcAy2khdeaS1vVjydNFzBT3NCD1BXVvjQ2qQt4Ncn2-qJYF28IVupAj1CwgJ-4W-zQWjPaod_HBsfbSh-CrMzbOqfF072gdKu8MZEbVLIOdg0s5vWlBJA4P_-bg-2SwM7rYlA5WDex4ohS9vzMr-w_pTgHBw2W1juZCDY3dO7XnuQrLEErknYeedYUM7EOf_AMFiA5H6nrHjUO3pRnOF1BDMUd42kDdE-45mw3o06sFfnXMNba1aKxp4zjpSSqKzhKR9YdrpMnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=d4x8oB1GNsfqsmTRGHs-cDkcsXkgS666U4-nv4bGgo1V0We-h7dke5LFh3ZEcq1CJmdQ4eu29S1FcAy2khdeaS1vVjydNFzBT3NCD1BXVvjQ2qQt4Ncn2-qJYF28IVupAj1CwgJ-4W-zQWjPaod_HBsfbSh-CrMzbOqfF072gdKu8MZEbVLIOdg0s5vWlBJA4P_-bg-2SwM7rYlA5WDex4ohS9vzMr-w_pTgHBw2W1juZCDY3dO7XnuQrLEErknYeedYUM7EOf_AMFiA5H6nrHjUO3pRnOF1BDMUd42kDdE-45mw3o06sFfnXMNba1aKxp4zjpSSqKzhKR9YdrpMnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
آمریکا و اسرائیل برای شدیدترین بمباران در روزهای شنبه و یکشنبه آماده شدن و ترامپ دستور حمله رو صادر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69348" target="_blank">📅 11:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69347">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruV1XNtft5MxRVys6gWCf-_-mDJYagp3XCRk-qCyl8IwUGa1rLdSCVWY1zUTxuC8zrnL_77kk1OJDCZa0k_Kl20cAYDsPDOGHfvEH34Jr4weQUSbp651L_P9vPct3IEJQsclDeoIvGDJE4FwNwJA9P7PT3cR-TuUsn7w6_4fFrtVCXsrB8ywJTA-MiawdYa7sGFQtzWVDNb45nmSdyvfe06Xw02fvnT3Lktrq4FohXLLKo83wfagiuwOqBIcXzqwNoM-VJgCr11DICmJmfdtMBMttxhApVwcEEFgjWu9T_IswMIgs9H1xyWEt-hl9YezJHUfgfAn6nstJzDYMFIbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دقایقی قبل یک کشتی در نزدیکی خصب عمان مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69347" target="_blank">📅 10:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69344">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=UF0Ks1yl7qf4eAs__FRpSs85WvLn79oU61w8Gn39chXugy2h1a87DbgTtaOHTL_2VDtObxEPH21Sc_2fL4pI4pyT2I7xMdN1QNzEQ4FKApNIPMqz3GDo0N9UvfD6GW_cKpqQLSe1c8cIG1zwPMRr_w-YXeQDQkgUUWy_8s996o06X2cZXX5xrYV6jdom_vqkrWjG9eQdgpGjvTk5189zUpKHTK5_VDy0rXpSXpQDnYZ3G-gQWlv4chLoi30oBzoOzYPmWWP64SKp6UJbtutgkQHjTpj4b6eGpNOl2GNOqrT2dnpqQA-rXqFh2PrNLq00T0QBvxTSuC5sdgVUD0AhVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=UF0Ks1yl7qf4eAs__FRpSs85WvLn79oU61w8Gn39chXugy2h1a87DbgTtaOHTL_2VDtObxEPH21Sc_2fL4pI4pyT2I7xMdN1QNzEQ4FKApNIPMqz3GDo0N9UvfD6GW_cKpqQLSe1c8cIG1zwPMRr_w-YXeQDQkgUUWy_8s996o06X2cZXX5xrYV6jdom_vqkrWjG9eQdgpGjvTk5189zUpKHTK5_VDy0rXpSXpQDnYZ3G-gQWlv4chLoi30oBzoOzYPmWWP64SKp6UJbtutgkQHjTpj4b6eGpNOl2GNOqrT2dnpqQA-rXqFh2PrNLq00T0QBvxTSuC5sdgVUD0AhVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
بروزرسانی از اسپانیا:
نزدیک ۵۰ هزار نفر از مراکش و الجزایر فرار کردن و غیرقانونی ریختن اسپانیا!
برای کنترل این مهاجرای غیرقانونی پلیس فرستادن که پلیس هم کتک زدن.
این مهاجرا ریختن توی فروشگاه‌ها دارن غارت میکنن، از مردم دزدی میکنن و...
مثلا از یه مراکشی رندوم میپرسن چرا اومدی؟ میگه توی مراکش رفیقمو به قتل رسوندم، مردم هم باهام بد رفتار میکردن، منم فرار کردم اومدم اسپانیا.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69344" target="_blank">📅 10:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69343">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=JolGq-8ytr0C6mPmrV4KRi76ydNyRHbrf3Dy_CZLfTJQFO0b39t4IMqqFMz9frFEdLKTUh25vBnc18pjTsGltnVLG71ftaM8O_h-vKZhnL4XPj9pd0f6S2r8m-WOSgfPVNRr1HPazVjNrX1ySJindUSlc8OSI-6ZGc6cJGA5y0EFN5U2W8wdzacnP3ehnZzRRYM_toBcdhHAutaHl8ETMquF7RO3FnIkrYcgokjjx53cLeQt_8d4f0jB_CUKPb66KT2n4ILJmY7-Y8POJOstNxKN71YgVBTDZoPsKpltmP569OKEVQSLTMuQMhcoKTYnmPv8QCz_PNaI4aNyGkGGdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=JolGq-8ytr0C6mPmrV4KRi76ydNyRHbrf3Dy_CZLfTJQFO0b39t4IMqqFMz9frFEdLKTUh25vBnc18pjTsGltnVLG71ftaM8O_h-vKZhnL4XPj9pd0f6S2r8m-WOSgfPVNRr1HPazVjNrX1ySJindUSlc8OSI-6ZGc6cJGA5y0EFN5U2W8wdzacnP3ehnZzRRYM_toBcdhHAutaHl8ETMquF7RO3FnIkrYcgokjjx53cLeQt_8d4f0jB_CUKPb66KT2n4ILJmY7-Y8POJOstNxKN71YgVBTDZoPsKpltmP569OKEVQSLTMuQMhcoKTYnmPv8QCz_PNaI4aNyGkGGdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
صحبت‌های عادل فردوسی‌پور درباره ماجرای دست‌بوسی عباس صالحی :
تو عُمرم دستِ مسئولی رو نبوسیدم!
عباس صالحی وارد مسجد شد و کاملاً اتفاقی روی صندلی کنار من نشست. به شوخی بهش گفتم اگه یه روزی فیلتر 360 برداشته بشه، همه این نشستن شما کنار من رو ربط میدن به رفع فیلتر!
همون موقع که داشتیم دست می‌دادیم و روی صندلی جا‌به‌جا می‌شدیم، شب دیدم یه ویدیو وایرال شده و با یه تیتر زشت نوشتن که من دست عباس صالحی رو بوسیدم.
اگه قرار بود دست‌بوس باشم که الان برنامه 90 رو داشتم و 360 رو هم فیلتر نمی‌کردن.
چطور ممکنه من برم تو اون مسجد، بین اون همه آدم، بیام دست عباس صالحی رو ببوسم و برای خودم حاشیه درست کنم؟
من همین چند روز پیش هم گفتم؛ بله‌قربان‌گو نبودم، نیستم و نخواهم بود!
همیشه روی اصول خودم ایستادم و سعی کردم کنار مردم باشم. واقعاً این حجم از هجمه‌ای که به من وارد میشه حیرت‌آوره.
من عاشق کارمم و اینو خودشون هم می‌دونن، ولی نه به هر قیمتی. اگه شرایطش فراهم باشه، تو فوتبال 360 به کارم ادامه میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69343" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=IpNdKsbFCVakW5lkUGrk-35kE3EgbM72fSK1FrY7-zh8iPHCMrjaJBO89bVRPe-ub7bGL5erjS12AYsGvRLE2z8lyPEwLZvMe6cxai8l4JkFvUen1hRVN63HWvA2a2JXCHVjBSZp-BZYlrshDyG3VoZv2Mk6yc-0EOtAktA9qxF7QN_s_b-VT8wq61mlRlUazdC8tbt9-lHgTakyHH2I7n4NTU9WlNrihXhRRplZldixryv2rhY-ySoIdqnA2DeUYHXLiCSuxkp1b-5E1aH-Iuo9iCpVLeHQw_wPP_ofKMkOosLFQq0zTPkkdWgLEo_1H2emdFsb-o4_OmiFgBNUww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=IpNdKsbFCVakW5lkUGrk-35kE3EgbM72fSK1FrY7-zh8iPHCMrjaJBO89bVRPe-ub7bGL5erjS12AYsGvRLE2z8lyPEwLZvMe6cxai8l4JkFvUen1hRVN63HWvA2a2JXCHVjBSZp-BZYlrshDyG3VoZv2Mk6yc-0EOtAktA9qxF7QN_s_b-VT8wq61mlRlUazdC8tbt9-lHgTakyHH2I7n4NTU9WlNrihXhRRplZldixryv2rhY-ySoIdqnA2DeUYHXLiCSuxkp1b-5E1aH-Iuo9iCpVLeHQw_wPP_ofKMkOosLFQq0zTPkkdWgLEo_1H2emdFsb-o4_OmiFgBNUww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سیدمحمود نبویان، نماینده مردم تهران، درباره شاهنشاه آریامهر؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69342" target="_blank">📅 09:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69341">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69341" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69340">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=IfX_rlc0VMMfZ3KLMRHoUzQVYyfqtKYPC3QgyK4dCJOKWmA0AA1h1bz59Wa9iIWdtECmSulxRFBnV3W1iSXfEJmWerVSoi368x5h-9slkUxIFhSCEaI2RfpknhEI6oTy77EW1sAnK8tkSuCv1TL1hNULVTZhj8d3Va34WoDh-F-2elqA1wAwX8FF05L1hZFRt9iN25kM9KF-mmQGjOixbNAkFneW2Ihko-UHEQCfuVOeo2CF7L175rI-KoQz4AzXU6GnC2v25nialGXfR0K8BXFyRRpygJDBfRwxXtWWJdHuc2FPt3H6p9LoB666RkJC2BWPlnV2ozTylPjAt9AunQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=IfX_rlc0VMMfZ3KLMRHoUzQVYyfqtKYPC3QgyK4dCJOKWmA0AA1h1bz59Wa9iIWdtECmSulxRFBnV3W1iSXfEJmWerVSoi368x5h-9slkUxIFhSCEaI2RfpknhEI6oTy77EW1sAnK8tkSuCv1TL1hNULVTZhj8d3Va34WoDh-F-2elqA1wAwX8FF05L1hZFRt9iN25kM9KF-mmQGjOixbNAkFneW2Ihko-UHEQCfuVOeo2CF7L175rI-KoQz4AzXU6GnC2v25nialGXfR0K8BXFyRRpygJDBfRwxXtWWJdHuc2FPt3H6p9LoB666RkJC2BWPlnV2ozTylPjAt9AunQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69340" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69339">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس لیست اهداف انرژی منطقه رو منتشر کرد:مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی؛
❌
میدان نفتی غوار در عربستان
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
❌
تأسیسات ابقیق و خریص عربستان
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
❌
پالایشگاه الرویس و میدان نفتی زاکوم در امارت
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
❌
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
❌
میدان نفتی برقان کویت
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
❌
پالایشگاه ستره و تأسیسات المعامیر بحرین
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
❌
میدان‌های گازی لویاتان و تامار اسرائیل
ویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69339" target="_blank">📅 02:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69338">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L48-Po4pf4hBhAMP1L4yys7LfB6uxvyCd1jF5GqRB6773T6ZwCQVVkyfwV4l73cunIJbT943CT8hkgSUvNHqGdxua3MnrLgFYcpsp-5yGb76UQR-WJ3u4mZOUcLXo43oI3wVVLPbiDeRVYIC3tPB4W2b7JBqvtw7w0s3DwheCVrtvikRdT4IR6UdhReGHY12n8sU8TFfOTFTw8ulWdbLQ_G9QGeDKNPoopCzY0-8TPEV8yOeAKzRWJJrZRUaNye9_3zttApkF-FGs0LYcgTH7PLZ4uR4VPMG6bM9WExJDg1od3bUToe3Ss7eK1NNcyDjFVONYKw-g6UPar1b6b3NYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:یه مقام ارشد امنیتی به ما‌گفته؛اگه آمریکا یا اسرائیل بخوان به زیرساخت‌های ایران حمله کنن؛
ایران از قبل یه برنامه گسترده برای جواب دادن آماده کرده.
به گفته این مقام، توی این برنامه، زیرساخت‌های حیاتی اسرائیل و تأسیسات انرژی آمریکا تو منطقه هم جزو اهداف در نظر گرفته شدن.
نیروهای مسلح ایران توی جنگ 40 روزه و اتفاقات هفته‌های اخیر نشون دادن هم توان انجام چنین عملیاتی رو دارن و هم برای انجامش اراده لازم رو.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69338" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69337">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIbuiSC-wOEqKgMfniEcqCbvPARZfGG29FcGlsDmxY7i0oDl4rF7-UcFE23LIX5tRIUcoK5U943G8cbQ_2jESg_u_lPPCfdYKgADD7XQ155t5LvRVF1ykZAm_sz7A6qGrAg0tYz_2h8w0NyzAq1fOrXsvkB08S4XgraFA3RheyAhEJX1r8jvtWwFdr1bdbUv787fIjzgrMaDWSNUTuVYi9ThHTDeHdfChj8hE3AUqQzmP5WsdKMVlZsmCVtTflbFZcG_EQ5e-BuVaf5NHPZsYj0hjOuqw1ju9jHKFo-A8qujoPJg4tVMuOf5E4lr4VBxrmcuJnFQlFoO59RhhGtzmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛آکسیوس:ترامپ در حال بررسی حمله به تأسیسات انرژی ایران ظرف چند روز آینده است.
یک مقام آمریکایی روز جمعه به «اکسیوس» گفت که رئیس‌جمهور ترامپ به‌طور جدی در حال بررسی انجام حملاتی علیه تأسیسات انرژی ایران در چند روز آینده است، اما هنوز دستور نهایی برای اجرای آن را صادر نکرده است.
این حملات همچنین ممکن است برای نخستین بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدید تنشی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین بار درباره حملات احتمالی گزارش دادند.
ترامپ در آغاز جلسه روز جمعه کابینه، با اشاره به حمله احتمالی گفت: «خب، ما ضربات بسیار سختی به آن‌ها وارد خواهیم کرد و می‌دانید، بالاخره زمانی فرا می‌رسد که آن‌ها خواهند گفت دیگر تاب و تحملش را نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69337" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0T3YjtTV8_44kIumMxe-w20cJVNBaa8XZTv1To5uwq08wkFRviClgb9f8xnlusZQZKS8FWWJ0EzrMA1FsqPSfsXNSKgmDeRsVojwgi24FqjEk_alAnOWWcyUSWvExZhwyjCP3P9VLO54uex4dsCj0JUZWvwUdxC9gapM9mkyrLfydbPM1DFtE2PN3F64yZuVR_shsz5lm8L80ll2HlllTbn3rMXczNc-gTJ7gKnsWHo3nu3QH44XHVCjx9H92XAcjOf9Gp4RU-MD-ak_gGoCgOlMO5c_Kg90VNVnqM4pDz5aqdMDbULTR-R30RmsiDfM5PuvkVKtIZeKkQVPbpWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
سی‌بی‌اس نیوز:
ایالات متحده و اسرائیل در حال آماده‌سازی یک کمپین بمباران مشترک بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده است، اما حملات ممکن است این آخر هفته آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69336" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69335">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5040574e14.mp4?token=oy_yaktAHIE2v7kKZkkhOWpFDC2OiSj7ys6PfiAp73fLl0zmXgNMyxHUU8sz1y6T2WsrpcQZKldT2V7Ll8o7qGwCbX9twX_sugoIG9-IDe3869Y0wxkohw8cMAeAbbMcBPFqVl7YxFLTYZLI-OqfhAZgTzWq_p_7mPLeQTQnO_mR7QVYDQJXhn_RUfIkyTqggdy2V6ayhNsTJ0a6t8kzWwCrwBPUxvHJzkG1MIMqxMaB8OvNVRioy-q62-uEfZ2vrxjbYRgRsRd9DduQ9PZQQ0aieGE_Uw4VdpPP5BWBHM7q_f6Vn4_k-91xJF2QdT5YkdmulEdREXuf-NsWZsMhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5040574e14.mp4?token=oy_yaktAHIE2v7kKZkkhOWpFDC2OiSj7ys6PfiAp73fLl0zmXgNMyxHUU8sz1y6T2WsrpcQZKldT2V7Ll8o7qGwCbX9twX_sugoIG9-IDe3869Y0wxkohw8cMAeAbbMcBPFqVl7YxFLTYZLI-OqfhAZgTzWq_p_7mPLeQTQnO_mR7QVYDQJXhn_RUfIkyTqggdy2V6ayhNsTJ0a6t8kzWwCrwBPUxvHJzkG1MIMqxMaB8OvNVRioy-q62-uEfZ2vrxjbYRgRsRd9DduQ9PZQQ0aieGE_Uw4VdpPP5BWBHM7q_f6Vn4_k-91xJF2QdT5YkdmulEdREXuf-NsWZsMhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مهاجر مراکشی درحال رفتن به منطقه برون‌بومی اسپانیایی «سئوتا»
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69335" target="_blank">📅 01:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69334">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.   مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69334" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69333">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2gNc_iAh5vLtoh26AEH2_6tExozItsiNwT_L1CyTsRqprswnXiCT58P__XLxQTNYdLqezbYM8UrnDn0G2s0AIu9s2qWzeyAjYefO7c-nr9zZE7FwafKcLgFn_-LJZrVxmf0L9otPVmBZiM6CnTZ7OgAZSrs90pZQ63Om7TFCZEWZ_GJd3FV4ixkrytLTfn39ZSNdWgffyLGYBShD6xR9hzCnbYtaU8BQhiscy05J3_ss7bySTX3lgYN-_K_c833eBG3LQac3rfhD83EAYbCB3t6vpYPciFpcnfjfGMJTi_b-yNE6XBukJ-nw3NVIGPWgn4wrif9ZiWh0gkxpQlJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.
مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند روز به طول انجامد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69333" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69332">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">چندین منبع به CBS News گفته‌اند که حملات ممکن است در طول آخر هفته انجام شود</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69332" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69331">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=m74oMBGtcYlaMgJP9hUKLjNnG4wLW5IuvtkQf6UmM78VxwASukLoQFlez1aUUhA_Hi45uXKfq6tqUq7eMptk-Jqd6k1DqUmytfLZg0s_Ab1wXy3gu16JDJFRayoDHoMvsSP_XIB-AjtxEVDBquqqRwkupYPeYAR_V90_u2bMI7lMpStgcNM-8el4DcMWKNIw3EHXepc9R5quSgvrAMMRrsArmdbGr4t5h27IcbKIIqMOF3ZLNMjShjqmWfUtGv1XOW2qjug-va97y_k7avvsFQ3-z63PHcnnfotBjuJ3NTDmaxshBLCfk65oSFmfoLQPZuVKZGX62-e2knqHtBJx26Hop4imHpRYls4aJwD8gN8okZnLeoDgUuLTzuPhV6fcFGxrwNGNSkXJmUyGWzVnTvSaR7qklxWtPbDZeZDR0AJYolU4fUw1L2M4TNKaLPsUikoN5PI7422IdiuF20Zl0ArkY-cVfz-4flGVOcgGNoVoEP3WlTCual0bBA2RBqT5cZRlQZ9VZ3ckH7iXc8bOxkU5Q1I5mKGsWD-qxHTXDTiYexoZyy_Nyr0EV9fw7kjXaY8csUVoq_zAIhdi2Xp3J2E2fHun2g63zGkJ7EoZO3vIkC6IvWrG8StIL64gIJ9A4_kbLt79PzuvKUECOje0hbr4cA3aAYx0Ms4AIn8ICmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=m74oMBGtcYlaMgJP9hUKLjNnG4wLW5IuvtkQf6UmM78VxwASukLoQFlez1aUUhA_Hi45uXKfq6tqUq7eMptk-Jqd6k1DqUmytfLZg0s_Ab1wXy3gu16JDJFRayoDHoMvsSP_XIB-AjtxEVDBquqqRwkupYPeYAR_V90_u2bMI7lMpStgcNM-8el4DcMWKNIw3EHXepc9R5quSgvrAMMRrsArmdbGr4t5h27IcbKIIqMOF3ZLNMjShjqmWfUtGv1XOW2qjug-va97y_k7avvsFQ3-z63PHcnnfotBjuJ3NTDmaxshBLCfk65oSFmfoLQPZuVKZGX62-e2knqHtBJx26Hop4imHpRYls4aJwD8gN8okZnLeoDgUuLTzuPhV6fcFGxrwNGNSkXJmUyGWzVnTvSaR7qklxWtPbDZeZDR0AJYolU4fUw1L2M4TNKaLPsUikoN5PI7422IdiuF20Zl0ArkY-cVfz-4flGVOcgGNoVoEP3WlTCual0bBA2RBqT5cZRlQZ9VZ3ckH7iXc8bOxkU5Q1I5mKGsWD-qxHTXDTiYexoZyy_Nyr0EV9fw7kjXaY8csUVoq_zAIhdi2Xp3J2E2fHun2g63zGkJ7EoZO3vIkC6IvWrG8StIL64gIJ9A4_kbLt79PzuvKUECOje0hbr4cA3aAYx0Ms4AIn8ICmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«قیمت‌ها حسابی اومده پایین، به‌جز نفت.
دو هفته پیش، وقتی همه فکر کردن توافق نزدیکه، قیمت‌ها مثل سنگ سقوط کرد.
ولی ما یه
توافق واقعی
می‌خوایم، نه یه توافق الکی.»
🎙
استیو گروبر:
درباره ایران، فکر می‌کنید چقدر طول بکشه تا این ماجرا تموم بشه؟ یه ماه؟ یه سال؟
🇺🇸
ترامپ:
«پیش‌بینی کردنش همیشه سخته.
ما ماجرای ونزوئلا رو توی کمتر از یه روز جمع کردیم.
اگه می‌خواید همه‌چیز خیلی سریع تموم بشه، کافیه به یه عده سلاح هسته‌ای بدید!
اون‌وقت همه‌چیز خیلی سریع تموم می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69331" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69330">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=HHY0_4q77aVLXd5kR3VPA9GwhXGfGfzT3_TyiBNKCaroWyrqSs3mX5jQvO_1PgeXvxTOD_Lluaab1tRnPvYnXz090bImWxxabU9sYKNplDcUTmKzNhegvrGyNQNV9QB4lXFGB2fRcXnplNQQs2yK3vEtj4rZFgGmHCeA3PHl4XIareMxqmV_biGcmLfLhV7bXJXTfNXF2_OoBKE4pFtU1YHz7hVfqJIWR5SOMgfbcw1ArirxOJtZALdMsF48ixY4vlfGyPD2gZAZb7GK8e2ntYV6E-r6zVOXfzm37Iq9GIJOX4q6sGTowhWbqJpr9_IZcwOBX02AYcjuekenkZFLsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=HHY0_4q77aVLXd5kR3VPA9GwhXGfGfzT3_TyiBNKCaroWyrqSs3mX5jQvO_1PgeXvxTOD_Lluaab1tRnPvYnXz090bImWxxabU9sYKNplDcUTmKzNhegvrGyNQNV9QB4lXFGB2fRcXnplNQQs2yK3vEtj4rZFgGmHCeA3PHl4XIareMxqmV_biGcmLfLhV7bXJXTfNXF2_OoBKE4pFtU1YHz7hVfqJIWR5SOMgfbcw1ArirxOJtZALdMsF48ixY4vlfGyPD2gZAZb7GK8e2ntYV6E-r6zVOXfzm37Iq9GIJOX4q6sGTowhWbqJpr9_IZcwOBX02AYcjuekenkZFLsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توی درگیری با ایران، بسته به اینکه چه آماری رو حساب کنید،
16 تا 18 نفر
از نیروهامون رو از دست دادیم؛ که همین هم خیلی زیاده، چون حتی از دست دادن
یه نفر هم زیاده.
جنگ ویتنام
21 سال
طول کشید. ما تازه وارد
ماه پنجم
شدیم، ولی همون‌ها که آمریکا رو 21 سال توی ویتنام نگه داشتن، حالا می‌گن "چرا ماجرای ایران این‌قدر طول کشیده؟"
من الان دارم کاری خیلی بزرگ‌تر از چیزی که اول گفته بودم انجام می‌دم. قرار بود فقط وارد بشیم، توان نظامی ایران رو نابود کنیم و برگردیم.
ولی بعد دیدم اگه فقط این کار رو بکنیم و بریم، دوباره خودشون رو بازسازی می‌کنن. برای همین باید یه جور
کنترل و نظارت
هم وجود داشته باشه، وگرنه دوباره همه‌چیز رو از نو می‌سازن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69330" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69329">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=V5xUaGuglRR8hLcEN8UpseaGEk59tVhjgVAZhy47Z1knApOhIq5dus_rSs3U4I0PoR1xAti8XVY_G0y57ScOmhHFspGfEpt0P47_W8MoJQH-EqsT3bxOfF-umuxrCAMUZ4FzDJ_CcpFwsigrW26xo8NUTwbDBTqK0y0HWktSB0KdZq2QCqpzxEagJiN3XXYprUo8h6mVVPbK3LVoby1_nqEQOZNK3lB5vuKfASFFO7v9k95BR9XACWBvzlAqhxJmPw4TmenF5gmSheCc_B2JVURkEEy7t0Cvy1LjHA6exD0HBVu8TtXoLz17EaZJlo2o47HONuUMK77kx7KN9Rz0jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=V5xUaGuglRR8hLcEN8UpseaGEk59tVhjgVAZhy47Z1knApOhIq5dus_rSs3U4I0PoR1xAti8XVY_G0y57ScOmhHFspGfEpt0P47_W8MoJQH-EqsT3bxOfF-umuxrCAMUZ4FzDJ_CcpFwsigrW26xo8NUTwbDBTqK0y0HWktSB0KdZq2QCqpzxEagJiN3XXYprUo8h6mVVPbK3LVoby1_nqEQOZNK3lB5vuKfASFFO7v9k95BR9XACWBvzlAqhxJmPw4TmenF5gmSheCc_B2JVURkEEy7t0Cvy1LjHA6exD0HBVu8TtXoLz17EaZJlo2o47HONuUMK77kx7KN9Rz0jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه هموطن که تو خونش کره خر نگهداری میکنه و بردتش رو تردمیل تا دلتنگی بیرونو نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69329" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YobqDl3wKZ85Yt5v2DndDjK0gIJPf6KobH2EPx0FTNMbdKlnUEUWxaLjwVKjh3m7AUG6tIRvERm-6C_z5C5qFU42jUgNubAyDbjRxX8LThZYUB6IuSJ6BqtAksrg7FLgqBQIviEacadEGyT3N1i1Vi195Bckp0qLOUz-o4oeasOpBlpn1RoVa2Ujc4wY9EErU90zsQPDvEHK3zI6a_hBUAySOoQAdiONu49hYlXDdsFnRVWEB_qZVj3VPys3dkWk53m7m6KqMCXRkN5ZNXXR8KcKBt9tiRxzbw_Wyc0pA7X8JGm-clXANskU-VJyGRZ-7Qll0whWdt73tFNPTYx7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=JocuZK_NjVzZu0d-VBT67t39pCirESX2jzTRAHKrzRVHjHDZftCjzwSJsPzHdP61tYSbeMowR5GADHzzLZcEceBgCbAdZZ0mQOMtj-PIYvfU5idJtq1c3TzX63Q-jBOnBPPG3PmOhFR8SqmNBMg5XzY1PpMb9cJK14wFcmCIUoZ1hTuCEHuxmxbarkMiYneXwPQrpQ2EUNZw_8c341UaiR3Q8lEs1qSXLRiRHK2da7TZiUwXtt5TOADCDSfBlXvBwuPZ0tbTEfXJk4SAListGu1EH8EoSBVaH2XSc-u_I_IlUS_6DW6SCjHCnxNo055T7vM2UnU5yLpV6HzwVoykhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=JocuZK_NjVzZu0d-VBT67t39pCirESX2jzTRAHKrzRVHjHDZftCjzwSJsPzHdP61tYSbeMowR5GADHzzLZcEceBgCbAdZZ0mQOMtj-PIYvfU5idJtq1c3TzX63Q-jBOnBPPG3PmOhFR8SqmNBMg5XzY1PpMb9cJK14wFcmCIUoZ1hTuCEHuxmxbarkMiYneXwPQrpQ2EUNZw_8c341UaiR3Q8lEs1qSXLRiRHK2da7TZiUwXtt5TOADCDSfBlXvBwuPZ0tbTEfXJk4SAListGu1EH8EoSBVaH2XSc-u_I_IlUS_6DW6SCjHCnxNo055T7vM2UnU5yLpV6HzwVoykhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=MebkZY7kznL_uQqKnaqkeWe-lTttjUNnyc5oeoPCuEEKHbQPjA-NtmXjuJrZQ66SVb8kD-OqRblwLlhs6SMVDYF3tSohfplTgCSpPQnflqEgWA1GRjrKe9cFruFtS3pp6Lxr8xfzcQZYE6Ky3h53TUP2rIZFZVNQ-6DX8F3QxNtULQF93C6kNhYRvbPd8ovNTU38lIGsR856xNE6589XA5_zwLKrvRaM0e8sy2buwd8ncvLGbpNg3PMYWnAo2AljMjQU1xSLBVWDuubJn5sNuXySAJ-M7uJVMZ9Q1_0OAfu38kZF-b-80T7fjzc76cZpd0R-M1J7h8xew7bsddyKAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=MebkZY7kznL_uQqKnaqkeWe-lTttjUNnyc5oeoPCuEEKHbQPjA-NtmXjuJrZQ66SVb8kD-OqRblwLlhs6SMVDYF3tSohfplTgCSpPQnflqEgWA1GRjrKe9cFruFtS3pp6Lxr8xfzcQZYE6Ky3h53TUP2rIZFZVNQ-6DX8F3QxNtULQF93C6kNhYRvbPd8ovNTU38lIGsR856xNE6589XA5_zwLKrvRaM0e8sy2buwd8ncvLGbpNg3PMYWnAo2AljMjQU1xSLBVWDuubJn5sNuXySAJ-M7uJVMZ9Q1_0OAfu38kZF-b-80T7fjzc76cZpd0R-M1J7h8xew7bsddyKAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=v7l0U3msJAMepSaJAq2V-dRgqS8hzusIiSyIs_fzBrDAEd0bZ40EY60thHovBV3c0328bxrhwS50c861wnB2Ps97UcfA6rOyK7-FiSERCwHOI6zXE3DGDZ4knZOO-HyALizfkJ9iMM1_8oIpFJjXxsGWj08fIwccSXo22ndGsU-a59ksfw29bqC1mmgJsg4ZZRskX9PJHs-1Tl3-85Xslt6h5qi4Etc2ngQLoZHYB5ZejvSAo_j8y0iy1S8bWE5izpLV25c4Am8SFG4mNOyQWCc39otQHC3ge-M26zH5oSET6_9PhcpXJTy5kGHCklkUgfxlKlMwUJ6FJZVEqEQIKSTYOqlh7bFHT0vlNb0xxOt0WN0-hOeI23pHQYRW4M3BlUCE_HnLGP-ZchPtYwQOxhN4sfEbIBun0QID51gOTyVlvBZ74G8W31wOyzhQtF2aUIDvvXC6wYpRmJW8IVbl2axcAo-gpu4So10ALFN5BdYfsCEOu9h2VWaWMdclaX6puwp3RSOLx_jFc8MEoP8pPhBOWbwaTfKBbTFni4VEbl8SJmKubSbXtSDmNaa5ggSBI7lH1ERlYYWcrjnIabTb_J2cyw6QEtEL9ibVVN5WBykxzHXsHPzyqGL5_zHUvm3bWCgjSHgLYlLhC5jBltBXDCUISo8C5iLcFKb76mP9KgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=v7l0U3msJAMepSaJAq2V-dRgqS8hzusIiSyIs_fzBrDAEd0bZ40EY60thHovBV3c0328bxrhwS50c861wnB2Ps97UcfA6rOyK7-FiSERCwHOI6zXE3DGDZ4knZOO-HyALizfkJ9iMM1_8oIpFJjXxsGWj08fIwccSXo22ndGsU-a59ksfw29bqC1mmgJsg4ZZRskX9PJHs-1Tl3-85Xslt6h5qi4Etc2ngQLoZHYB5ZejvSAo_j8y0iy1S8bWE5izpLV25c4Am8SFG4mNOyQWCc39otQHC3ge-M26zH5oSET6_9PhcpXJTy5kGHCklkUgfxlKlMwUJ6FJZVEqEQIKSTYOqlh7bFHT0vlNb0xxOt0WN0-hOeI23pHQYRW4M3BlUCE_HnLGP-ZchPtYwQOxhN4sfEbIBun0QID51gOTyVlvBZ74G8W31wOyzhQtF2aUIDvvXC6wYpRmJW8IVbl2axcAo-gpu4So10ALFN5BdYfsCEOu9h2VWaWMdclaX6puwp3RSOLx_jFc8MEoP8pPhBOWbwaTfKBbTFni4VEbl8SJmKubSbXtSDmNaa5ggSBI7lH1ERlYYWcrjnIabTb_J2cyw6QEtEL9ibVVN5WBykxzHXsHPzyqGL5_zHUvm3bWCgjSHgLYlLhC5jBltBXDCUISo8C5iLcFKb76mP9KgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=ZnKmj01sPbIc4OpuAa65HUFKcb0GxI9YklznBkifuZ1pHZdTkkJD1jPGFlVbNFEvB8TAkVuwctSzTZh_LuHncTKvZU8WK2Nwcxv0WoVE5Ic_hVFA3mNiNmtxkmG0F7B8SqB1xuAeGWmVeCW7b2rVcyvTAAUoTCpaaROIVSrjr66r39fhGHAKB6ttE2xwebweOwx3w5Oz7xbGHfVJAFCCrY4-pX-fc-0CbLepysjYwKjYRkLwZXoyUkVO7IkIZ10NWf6RnTK2eSmPQEOecjTVzZfXsMeMcE__E_OGdOUroZQGR2m7AbepD1tro1rQIUa-IbaeabjUKtbVsjE2vCBKejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=ZnKmj01sPbIc4OpuAa65HUFKcb0GxI9YklznBkifuZ1pHZdTkkJD1jPGFlVbNFEvB8TAkVuwctSzTZh_LuHncTKvZU8WK2Nwcxv0WoVE5Ic_hVFA3mNiNmtxkmG0F7B8SqB1xuAeGWmVeCW7b2rVcyvTAAUoTCpaaROIVSrjr66r39fhGHAKB6ttE2xwebweOwx3w5Oz7xbGHfVJAFCCrY4-pX-fc-0CbLepysjYwKjYRkLwZXoyUkVO7IkIZ10NWf6RnTK2eSmPQEOecjTVzZfXsMeMcE__E_OGdOUroZQGR2m7AbepD1tro1rQIUa-IbaeabjUKtbVsjE2vCBKejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=glZCWxsBg04CjoutBFAUhnB4rafQs3TFKbSEoVIxspdKwbuTLLHNGd3Q0GuFSGqzVFb7p7OcStIF-sg8EIZHnTl4T0wOTwz69yUWsoOPh0R_d8E9k2-F8ARYJyrQG3bJ6jvwCK6LsB_WrGRucxKWCnUqtBKdKd3MuWHc7JT0mk4WY2UeMSy93g0ky4GSe-jaFADhCFwnP0BlTtwzlf4I8KuxKWbFyhDiS92wjZNynhds5n1jHm-L7FjKL6lum8k6E7Dg7tD90fUsbuSQTYkyODhbxz9lsDR5e8GN2m5PEiAl6zBJJcdkyhdudJSSbHYuaVucjIWUEMr3Demsy5XX1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=glZCWxsBg04CjoutBFAUhnB4rafQs3TFKbSEoVIxspdKwbuTLLHNGd3Q0GuFSGqzVFb7p7OcStIF-sg8EIZHnTl4T0wOTwz69yUWsoOPh0R_d8E9k2-F8ARYJyrQG3bJ6jvwCK6LsB_WrGRucxKWCnUqtBKdKd3MuWHc7JT0mk4WY2UeMSy93g0ky4GSe-jaFADhCFwnP0BlTtwzlf4I8KuxKWbFyhDiS92wjZNynhds5n1jHm-L7FjKL6lum8k6E7Dg7tD90fUsbuSQTYkyODhbxz9lsDR5e8GN2m5PEiAl6zBJJcdkyhdudJSSbHYuaVucjIWUEMr3Demsy5XX1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=NW8WqqNvlQ-xjsMmlWajrnUzg0VnCnXgQQP3Sm5EHCRi6uXNR07EzJWitUm9SrzBKguZy_irkk2pa7038_Z4bDg5Bj3Nx3-JkncGhLQzgvGirzpq8LwcycFAfa5kqtkVkBwOhIGx3AbyAo5LWzUsyDO-0BiLfEm27HLBn7ehlsw4t1zcatpUOo0taU80QO5BTqvDXg4qjOa6JquKUj7B8k65bt94zmnj6Rxa7xuSWcmeqIh2073GXMs6LNw9R-sw5cFlErzAFtpeTF_rIwNVUVltxsMC75A2VTyCKbWpBcAnicrVBUSSAtnUll66lhlaO5P5c1ZdV1CNyANp4gE-jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=NW8WqqNvlQ-xjsMmlWajrnUzg0VnCnXgQQP3Sm5EHCRi6uXNR07EzJWitUm9SrzBKguZy_irkk2pa7038_Z4bDg5Bj3Nx3-JkncGhLQzgvGirzpq8LwcycFAfa5kqtkVkBwOhIGx3AbyAo5LWzUsyDO-0BiLfEm27HLBn7ehlsw4t1zcatpUOo0taU80QO5BTqvDXg4qjOa6JquKUj7B8k65bt94zmnj6Rxa7xuSWcmeqIh2073GXMs6LNw9R-sw5cFlErzAFtpeTF_rIwNVUVltxsMC75A2VTyCKbWpBcAnicrVBUSSAtnUll66lhlaO5P5c1ZdV1CNyANp4gE-jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=TmFepIH9bc83sFKBTe19z3XIHbb-niPulmzonATGeNxQ_RBhPEOAEPRvyf_4D9NYbl5aNNx0uxr2T61pT3EcxzqEJBZpgr439BCWw10mteDGcrpvuKjYeMr-7hlP4vN0JX3skyWFBVswuujvK9DtL7kxrluiYbf5beFTcjVcq6yWmxKrzNrnYpWaEa48IuGDZo55S-6D_83_ISk0s-ajENMUyf9vklf5E4YIoNl3xmak_bthvC8qjz0CSK7xcfXJiLuYgIlgUYWpxSOxWUMJ1jXcAwC-MBAjpAE3JWoRdbDqi2HqdFitTtDcnVCfNClx9iX1nKRWRHoEwh8jCGTlOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=TmFepIH9bc83sFKBTe19z3XIHbb-niPulmzonATGeNxQ_RBhPEOAEPRvyf_4D9NYbl5aNNx0uxr2T61pT3EcxzqEJBZpgr439BCWw10mteDGcrpvuKjYeMr-7hlP4vN0JX3skyWFBVswuujvK9DtL7kxrluiYbf5beFTcjVcq6yWmxKrzNrnYpWaEa48IuGDZo55S-6D_83_ISk0s-ajENMUyf9vklf5E4YIoNl3xmak_bthvC8qjz0CSK7xcfXJiLuYgIlgUYWpxSOxWUMJ1jXcAwC-MBAjpAE3JWoRdbDqi2HqdFitTtDcnVCfNClx9iX1nKRWRHoEwh8jCGTlOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=cxMMKzVDxq9UmXBxjzCG-mOtTQ6OkqphFrAQJrLVjFw7DemJ7OgCuQ-WYLzNt2vAq4Zs0P9drQ2x74UCg9O6TaO1G-6hbHcisL4uqoTLmYjV_8bkxnJqlCm8JEz-kWtqc7JvDnHJgclqxBdmKK6G-yCW23dBXPiXuH7QhSaLP4_if0-B3NndgO1pq_Y7qvDIsyPtRJVOVzJ9JNjYNJkMakCyEcbSMoTXWXKf8f-rWUD-pwR7uKY0i0u2FEC67I6iC6x0GP0lmfy6UCiPjGdZiNFOoIsh7ehuQPv5ZlpWAmQx34wpqVDmE4r8LmdKXn2Mko-bo8R62jP0maSBExzgwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=cxMMKzVDxq9UmXBxjzCG-mOtTQ6OkqphFrAQJrLVjFw7DemJ7OgCuQ-WYLzNt2vAq4Zs0P9drQ2x74UCg9O6TaO1G-6hbHcisL4uqoTLmYjV_8bkxnJqlCm8JEz-kWtqc7JvDnHJgclqxBdmKK6G-yCW23dBXPiXuH7QhSaLP4_if0-B3NndgO1pq_Y7qvDIsyPtRJVOVzJ9JNjYNJkMakCyEcbSMoTXWXKf8f-rWUD-pwR7uKY0i0u2FEC67I6iC6x0GP0lmfy6UCiPjGdZiNFOoIsh7ehuQPv5ZlpWAmQx34wpqVDmE4r8LmdKXn2Mko-bo8R62jP0maSBExzgwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=sYEWLjplIgZ4XiEhwCsGGmQACZ7-3AzwDkw8glHSW6u2RhOVkMzg2dMJl0y7rjt_ZLl6BZdkQ2yMjiOaX8z4jIPtSmd3z6plevreBLtUFEw9xyVz9KSvgdJLzS406hX5pT5mcKxJ2nMdS6Q95tckFAwYd-i6qSdtB1eA2Amy4dB8uPMwJBeVsghugXOdc-JlfILghLwuTSGk4mgQOXQ6MmC3k41EarPQ32pTV8sBksU3jFLVnfXX-04NcOWi97M1JA8glL5E7BaSpyDfbphAj6W3_UrKuXB9HtVibc6pKPY-JxwycyJmUEC1bZpqSB-WWk6exciBJZXXZiuLRu_ofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=sYEWLjplIgZ4XiEhwCsGGmQACZ7-3AzwDkw8glHSW6u2RhOVkMzg2dMJl0y7rjt_ZLl6BZdkQ2yMjiOaX8z4jIPtSmd3z6plevreBLtUFEw9xyVz9KSvgdJLzS406hX5pT5mcKxJ2nMdS6Q95tckFAwYd-i6qSdtB1eA2Amy4dB8uPMwJBeVsghugXOdc-JlfILghLwuTSGk4mgQOXQ6MmC3k41EarPQ32pTV8sBksU3jFLVnfXX-04NcOWi97M1JA8glL5E7BaSpyDfbphAj6W3_UrKuXB9HtVibc6pKPY-JxwycyJmUEC1bZpqSB-WWk6exciBJZXXZiuLRu_ofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=uw8YLsjy6v7TOpcbZ9JMyfClbdRBi2d74q4h07fYicAQbpkmXB_gxVYnEuARbHsEKJZXpsE02r9wmcRcCuwMq4X3RjRCzZyerHx6Jq3_h4-OpxAwG0JSGhkGKWeRB_ALs4qxv2RT0U6Nc7FWpy4Y44IBHm3YttV0ebsyczwKG_VkOPpTCWl7gmT_qF6u99t-oGWPRjaXAck-J-TQizHQKnpP4itvCu2EdMb0Wgci7Go-6h8UKqEQK3nsiGGrPbP0qTw8ByIJ_td8TX9pMvMgJKBP_3jt1-20zTlP7QaYQ77h-00dILF-a2spDECNnaeOwJkQ0DrfQ7IfwJrLYS4c8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=uw8YLsjy6v7TOpcbZ9JMyfClbdRBi2d74q4h07fYicAQbpkmXB_gxVYnEuARbHsEKJZXpsE02r9wmcRcCuwMq4X3RjRCzZyerHx6Jq3_h4-OpxAwG0JSGhkGKWeRB_ALs4qxv2RT0U6Nc7FWpy4Y44IBHm3YttV0ebsyczwKG_VkOPpTCWl7gmT_qF6u99t-oGWPRjaXAck-J-TQizHQKnpP4itvCu2EdMb0Wgci7Go-6h8UKqEQK3nsiGGrPbP0qTw8ByIJ_td8TX9pMvMgJKBP_3jt1-20zTlP7QaYQ77h-00dILF-a2spDECNnaeOwJkQ0DrfQ7IfwJrLYS4c8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=qp6sI0L2p3KXcmNZrM7xT1dMetZWRvmcfMcxxfdPyVwf4XeRAfBGCCVcQrBavugQRgckOhbosVwVCwwqJJuLDH13y8TUm4Z535PH4XwP5if0OTgxP-OqSJlDi5hfdlRTEfy7Sw-6AfWtdwgCYFwdPXJr-X-6Zqmbfnzw05Mk2l51ykovT_6WkZlt2wLM64fo7d-hw2H_w4hrEMfNHMEkX4_ThsGLX_sihrCuePQg7rMhs9QBNsB2une3zHqSNDIySNU1-JQ6eK3Km4jesNkpoREuOmAUqSEvgpzmEYoKwwNWMR1spdIVR18NktpzQAsLy1V6TsyhdZdIDB-cghq-DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=qp6sI0L2p3KXcmNZrM7xT1dMetZWRvmcfMcxxfdPyVwf4XeRAfBGCCVcQrBavugQRgckOhbosVwVCwwqJJuLDH13y8TUm4Z535PH4XwP5if0OTgxP-OqSJlDi5hfdlRTEfy7Sw-6AfWtdwgCYFwdPXJr-X-6Zqmbfnzw05Mk2l51ykovT_6WkZlt2wLM64fo7d-hw2H_w4hrEMfNHMEkX4_ThsGLX_sihrCuePQg7rMhs9QBNsB2une3zHqSNDIySNU1-JQ6eK3Km4jesNkpoREuOmAUqSEvgpzmEYoKwwNWMR1spdIVR18NktpzQAsLy1V6TsyhdZdIDB-cghq-DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2yUCUYNqbVVYzztx0cLZXtpHzCHkW-1UkANewCtNmSWGMHsI1nH5L8MbwaXX4b9vVFBP7kJN2CZut-ErohaivIZK0EHauvOBUbtx0enGXBgDpDl3JnBe-5U22ulcYqBAGZuwBTYqxuRVpfRSKtSWQUagFO8ocbg2Uk9nJtushnCSpzPO2v8gvNcQFosdtLznhrFE8qyWqdaVmPRaXwJaja2c8koFRTWyd9ZX1S4qkbH0jhlM3Cd4YFt7YagAdoyOcPfjvHTTMpZjTzaoZNddPeURsjgWEQzSpMRj8GoZ_PZlK5omXRgEfS3l_6VRoWQ9tU8_6JUXp0LwuCLQy7QiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=lvGiM84D1tgs23ueDWQuqyj-RDtSgFg5Bp9E3eUBYnZoeFZP40b42CVDqRUyhR0sccI6NaUAhpJCO8CitUGt3qhDY0w_A7kUYXF3NZ-d9XBu3DZeaM1R9fURwZ-BRwgSSJninFhVEBcPLU-GxpJFwkqslvfzik9381eUnKK718mAXD7Iqqo3Gzj9QqJ072U1B4JusXGkMrQmcHtowsp2ALg5RR2HSp25mMW17KvG_6pxNne-DvItBh6HsjKSKRqQBwquLn6Z8_Y3uX4T5e5mGbr5MXOrpLYj3TmaZA83xM46ZtnYlrb272OoCjBmCZ-DDe64JZ_-_FX6TLLkyHG0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=lvGiM84D1tgs23ueDWQuqyj-RDtSgFg5Bp9E3eUBYnZoeFZP40b42CVDqRUyhR0sccI6NaUAhpJCO8CitUGt3qhDY0w_A7kUYXF3NZ-d9XBu3DZeaM1R9fURwZ-BRwgSSJninFhVEBcPLU-GxpJFwkqslvfzik9381eUnKK718mAXD7Iqqo3Gzj9QqJ072U1B4JusXGkMrQmcHtowsp2ALg5RR2HSp25mMW17KvG_6pxNne-DvItBh6HsjKSKRqQBwquLn6Z8_Y3uX4T5e5mGbr5MXOrpLYj3TmaZA83xM46ZtnYlrb272OoCjBmCZ-DDe64JZ_-_FX6TLLkyHG0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0dh5OVWNvJZWWjZs5vk349zNyOGu3023Vs3gLXchcDUkpnuL2QbtywdkaFtjBxj8ECRgAKCb5wzFm3SPWRNjjhV8-O3DB3ZMVW6qRcCmsWn0SGutoy3H3L-G6PVux0nzrTLKAA3hBW98s5CWLB6qZeIyJKeif7WcWvY6hxESaPtFIHbpp1kg8PidNcl-FtmPjQnj4_rnfAK008AWwoRyElOE7o0-EL36DMM0pqP9mpW7dz3pb08n36fc_9rc6esNaIp2kJX_9yuj3FdRvCATHlhAHOWKR_-73kCnDxL-CtLQJkrGjUKIdCniVAWbMBg0Utkrc4cScvc4hMehy_FjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=fLC_r_ERXcvHkQatcSx4yRtgDIzyiSrndeiPyTNkl9QM8CnZYReLQSMceb7C529lfE4TfC8fT2CkwSh1P_9XBDlCcBUKcgDDxifIDkKTN4CDKh4bpfTHbEQ9YgX8-50bJfcZI_i-AgpsoIAHnriX4ZhMut2QsXUJ-VsOSB3-_9l2fNanV8dKCK1YNZpQRp89wNldrtY8vLAP4_DXLjoYNnKY6vZ1HXhr3Gn-Te_3YDPUlUlpRPrllcRkCTTctsGeMEMd1Jm6vHx0rbkVXOVRA0JFw2PMJgoH7v64F_2AD2ukf6w72ga32ydSluzmhH8YrVbn5H_CjpTrljPy3yxzCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=fLC_r_ERXcvHkQatcSx4yRtgDIzyiSrndeiPyTNkl9QM8CnZYReLQSMceb7C529lfE4TfC8fT2CkwSh1P_9XBDlCcBUKcgDDxifIDkKTN4CDKh4bpfTHbEQ9YgX8-50bJfcZI_i-AgpsoIAHnriX4ZhMut2QsXUJ-VsOSB3-_9l2fNanV8dKCK1YNZpQRp89wNldrtY8vLAP4_DXLjoYNnKY6vZ1HXhr3Gn-Te_3YDPUlUlpRPrllcRkCTTctsGeMEMd1Jm6vHx0rbkVXOVRA0JFw2PMJgoH7v64F_2AD2ukf6w72ga32ydSluzmhH8YrVbn5H_CjpTrljPy3yxzCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=oxVNYD0b6X00UBsUayhVKJSSrDG8dJJEth2LVMSlf4wIVUBNqJ6l_lAXiutUZZdc-iFdC4h_JBtirQYTDUSJQ4gcBBHzvh2H36kz1CI2UGU1GMdlEoEgFPJPil4uv76lbqndnSXh2OeF_wC9ELPJS-fFceiOyGk_wVITpAeJLATORjz89efBXWl5eOn_JF7iA5XWXfP0_XXtgaTe3x4D4z3zKlmxB0NAs4cLHUIepn7h0H2LMP-7lfna6Wr8w6lj88Y0JeaeIUWozWh88Oh3hUhU1S_r0ddluVt3NxA9M5bVtfN9iMxiy40ueJH8jmbVVKiitIzHhjebIeBQbOdpuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=oxVNYD0b6X00UBsUayhVKJSSrDG8dJJEth2LVMSlf4wIVUBNqJ6l_lAXiutUZZdc-iFdC4h_JBtirQYTDUSJQ4gcBBHzvh2H36kz1CI2UGU1GMdlEoEgFPJPil4uv76lbqndnSXh2OeF_wC9ELPJS-fFceiOyGk_wVITpAeJLATORjz89efBXWl5eOn_JF7iA5XWXfP0_XXtgaTe3x4D4z3zKlmxB0NAs4cLHUIepn7h0H2LMP-7lfna6Wr8w6lj88Y0JeaeIUWozWh88Oh3hUhU1S_r0ddluVt3NxA9M5bVtfN9iMxiy40ueJH8jmbVVKiitIzHhjebIeBQbOdpuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfU8z8ZZ--XTpo-fX0qRmU-4ZXVNGC5jBadIAWvu6UU7RL1fb8TeKvSyhrSHGBIGyi7kGPCY1IkbtIKo1NTmbN70eJooPOr0alkBvwkX1jvVDP7xBPbwiDT6-UEgfnqnvV0pNbaJ8upaM4Dmh9oIYvQLX-ipeiMYLoikBPvLjDqfc3PirF-nc2l12QHXSB6k5P06dxBAt4Hx2RM8J8iujg97CotRNpL2bU27fiZiVY9l9W0z71tT01t3w6mJGkAOevsTeQ1RjYbV0aKpmb8Fddoz0VPNxnrHUrNlx9T7Z2zGuM5KvyLgmSk8JdFZp2B5y7Qz1ikA3FYcSEOOKbQaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKR6hWX1e8ljjwC4Vr0UaprTkqjNjR6TTxSEHqaOkbLc1GzL9rIhXepnswCKtwvrjXR7hTwoLU3ojQwpNquz5BR4kehYDV_ze6DNZ4VajagmsxGc1ZQL-JgIZxbT42XReNzENbD1E3bom4D_-_bEi8Vz5704CN-OZzRh9AkoHruVs1BCQVw46iP26ONXYvnDafkyO3LgT8QfLv3NYURHoM0byMrCSZc-l_jIgq7H03CsoxrRjvyQ7r6qSL8JLV8mrWsa_ghcIPMwsCW_Y6N6PYdGnyhS_jr_q-00honZq7AyDe_Mi5EZ7O_ypqcOCdiQYQ-NeVmHMn37igZTbo98Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z91Lp2iSaBIY-1NBeesGcMjIL3iFjsPO_qYD_z25C4JRPtbZTshbyIbgYBH0g0KTclm7M6hyrGR6KHywpydqwzNFmmt4sT49265ef3tK3iH18lb2OK6000G3S0xUcN9sU5XlEaNMKoXyMe9v99QVzKxaefKlRljDlF-c5unBK3bn4qtwrZw-Z-2vs2NVdrsyEfJuvlQXtqa4Y2fPp7NS6Z_UUopVsGnc2p475GzzEEy5ikXaCNT5KSZ27q4aPdPi4hmN2_QKoHB4lfn0T0nzkSHiTpjEp5LRi_6p3uTNQnL6NPa21xsVPqXVDROypHiVSisAP5f14stePUjMyfE-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=dKnanYsIliwTK4AbaNrDUcqUQKeGIha3DFrYecIcZhC-JCcFa5_IiVYf9uXemGMbBiQYH_QwO6sic_USl6loG-yc_ocFYGaHWsmX2cydFCjZ6wLJpoHtdZJIzQHeVdpzaWNZ03ceFqxhww9yO_v37XfgzY9NDcJjiBVfi9akSiCPNmW9eHM8WL3mQUfISKKxFtjIvsLFfbUkFlehAJ2RvCuVcX0I9sBRBbRV4VXImW3I75XobzjOrJa85e5-f51W_-0MScXZSKkYq4S5_VzLAgcs3fEzJcRJsRpi0I2H_kNtcCs_AkLcXtd4c1bqcFm36ml_bjS0ScUY-dKi4nzasA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=dKnanYsIliwTK4AbaNrDUcqUQKeGIha3DFrYecIcZhC-JCcFa5_IiVYf9uXemGMbBiQYH_QwO6sic_USl6loG-yc_ocFYGaHWsmX2cydFCjZ6wLJpoHtdZJIzQHeVdpzaWNZ03ceFqxhww9yO_v37XfgzY9NDcJjiBVfi9akSiCPNmW9eHM8WL3mQUfISKKxFtjIvsLFfbUkFlehAJ2RvCuVcX0I9sBRBbRV4VXImW3I75XobzjOrJa85e5-f51W_-0MScXZSKkYq4S5_VzLAgcs3fEzJcRJsRpi0I2H_kNtcCs_AkLcXtd4c1bqcFm36ml_bjS0ScUY-dKi4nzasA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=gBqf6VYu9V8cKlOj7URWj5dbBulW1p3_LAW1U0EHJl-4eyGHPSNGeHfxOml5VAXGE2M6MRWMZz_uU9Xx2wKS_qS6fR3h5Nws574QJgKOYWhLjKbaSJVHjw3dNRxEbqS5nP9K5qGUGoT6uJGYlF2_iwXZPPuqEcnSHOA1nFDdbKgDl4Ku_roS2rJxWLe0M8URNKsikIN_3kGcX5byauhvwM0xHET3Mej1Byx5XbmPf3SfoYNI-fZ4LI3gBYOzln5o58ErFco3aiGprw6CFuU1gQEs8iv9YCNN-8SfozjewzYCAaeQIuw8mah5w49keMuJYV4jYelLvuKkXas1SEIw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=gBqf6VYu9V8cKlOj7URWj5dbBulW1p3_LAW1U0EHJl-4eyGHPSNGeHfxOml5VAXGE2M6MRWMZz_uU9Xx2wKS_qS6fR3h5Nws574QJgKOYWhLjKbaSJVHjw3dNRxEbqS5nP9K5qGUGoT6uJGYlF2_iwXZPPuqEcnSHOA1nFDdbKgDl4Ku_roS2rJxWLe0M8URNKsikIN_3kGcX5byauhvwM0xHET3Mej1Byx5XbmPf3SfoYNI-fZ4LI3gBYOzln5o58ErFco3aiGprw6CFuU1gQEs8iv9YCNN-8SfozjewzYCAaeQIuw8mah5w49keMuJYV4jYelLvuKkXas1SEIw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=DsSKNdhYCvs_gb9KOzjasBR2JYfo32U4cr1eEv9JPFEk57e6EEwSXOtKRsgapLGYDz6nWCyR3mpG1Nqc7AdkrgBt0FfnZ3jBGTSzvPlxTONrTuKFsrBAb43oHxpgB-8iCDp6nWz38BhyT6MP5OaRRF8yrQ8Jf3HJtOubCH5mWHo6MXBUVOtAAlg3qMMZ-__zK3a2Q-DeguOzV4bPfLUPmU1-1pb-smL_VdtD7K-xxEFSeLIMww9sPm5_lKA5JFg8gAYgr68t6Qe5yFh_pwy82mK2G8F9GICPKU8-oIHk26bRRvEfxypOQxEevOM0dilFDRAe6Rq6p3Cm2h2DjR3Y2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=DsSKNdhYCvs_gb9KOzjasBR2JYfo32U4cr1eEv9JPFEk57e6EEwSXOtKRsgapLGYDz6nWCyR3mpG1Nqc7AdkrgBt0FfnZ3jBGTSzvPlxTONrTuKFsrBAb43oHxpgB-8iCDp6nWz38BhyT6MP5OaRRF8yrQ8Jf3HJtOubCH5mWHo6MXBUVOtAAlg3qMMZ-__zK3a2Q-DeguOzV4bPfLUPmU1-1pb-smL_VdtD7K-xxEFSeLIMww9sPm5_lKA5JFg8gAYgr68t6Qe5yFh_pwy82mK2G8F9GICPKU8-oIHk26bRRvEfxypOQxEevOM0dilFDRAe6Rq6p3Cm2h2DjR3Y2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D_DzgP_a9eVAkZ_HN_N46PMnWR-L2iqL7EuWTwIqh60BQDKVylIgJrhJDAYjSpETRt7I0iSTmiBve07odaF8tTsyl2USdAmBE5UqBBK-xeBWMqF4DLXlEe2uMJ0pfHXun3tpHiJyjpgKsfoG1EF6ACOMjdbdhO-t44MeEFeDtiYiZer-fIbjhvfkhfce2AsYyZjvJ92htnhcDDnjyHawN0eh4OHnP0mM7uE-hFI9G60-3FpjlFyS8gauDZAQDwVRfhOrveGb_wLVrost3CWWi9h6TzVcoeN6wc_i-XRi6uj2S29ANZPfMMzf8T50atKeqQ8ihz9UoUwFTtEjvXBcRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=FqbUm46kz1CmtZGSL7u8KwKbTQ1cRnhelpQ29ESkVkQa1NG39Yj3DYfPn-Na8h7TV6EPtENuRkrqrp0a3kOCdZmMLnZc2bxXkfTKLeXxHu4bAdkzVUC0Lkcd7ZGUwPw0-7I6ACljoWVyeESVY3aeS9oeJx_6uFHceTDgSgmrVzO5wtckjYcPRsLIzt-uHEddhp7JduxwUS_RVNQUQkPL_BDz-uWsKW27mL81o6iURfnR2AFrAcwuuaWcrcQy-pugLJPcHJZM7VUASptRuNgPQqdG1Mkq5FGPdwPll6IdtbvjgtWLJdJvIB6ZWfrmCg8ngKmNPLVqIAjJgCpiZh9seA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=FqbUm46kz1CmtZGSL7u8KwKbTQ1cRnhelpQ29ESkVkQa1NG39Yj3DYfPn-Na8h7TV6EPtENuRkrqrp0a3kOCdZmMLnZc2bxXkfTKLeXxHu4bAdkzVUC0Lkcd7ZGUwPw0-7I6ACljoWVyeESVY3aeS9oeJx_6uFHceTDgSgmrVzO5wtckjYcPRsLIzt-uHEddhp7JduxwUS_RVNQUQkPL_BDz-uWsKW27mL81o6iURfnR2AFrAcwuuaWcrcQy-pugLJPcHJZM7VUASptRuNgPQqdG1Mkq5FGPdwPll6IdtbvjgtWLJdJvIB6ZWfrmCg8ngKmNPLVqIAjJgCpiZh9seA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep2dEaMQlkj9ENCAWw3gpaTIFii5puK5hi5SJaoXxFMaPzblV9PTMjgPnv-lS-MszqITiRL_MW1o-CruvZBvmcT1n1Feynvp-lL-CIDfWSUw0OgoN8UDDu5OISUZhbAGl3R0qpOMb_VeZOsUPiqRWeOkYwmr3205V9H2uAs1gSSIU5NxuLjJSgCmNWxluRoIM3BaEbyCI8vBgd--hVa75rOwjcAVOp5C7TT0UbKECkS7NahoVeP9MENTpkNODq299Qn3JNwiVwO-prLUOc90iJZTZnR-9rZyE9RCeaVTODqn5I2mbQ5txXirH-hg3Yij4-bWRjixwXBR-ZIXaoo0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXd5H9WkYQc6Nioj13rKZFOK_mKzH-JoscrBnEFr1Rk4iBYiYlCUv393TMIlZDIcoVJ60fkRErQPCXdunSxCTJ9TSm3jEkLRdo_A-GQsX438SaWwdsxdUF9IV5p906KQ6TkOD3aeAZPrtS2uhVlKKW8ZXUX_yD9YV3_VjZfD6pk2gPaq_aOkdM2Wrd8SmdPnY8RH-zWYzqK5ljs7jNWJ0ps5ZxqEGq7Pd52Qhhc30j2sP8SOUu3CytRaWKairpLzW1owMKjj_b_SGzV5ox5jtVRTlcxcYgHbZDJnwXuOopUvfVkheaFcUZvzFYhQMdpZbyVpcIeZWvYjaNpfIC7MfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=mcP9hhLqZXuPL0ae5qSz--K4V_rlQD4BpmsdM1gpwOwLFJv1sXKAK7Je6DXBuK6hwpTxTJTbKZOg-D8aLBLQyb9YHwGo1g4-G1tnYuKcncySZfRGrVPFr-OnW8muEixZF05ZKd2yXPVPZgtKcGLe9jWQo0mmgYgPhIyN_Q2sC7Rqp54Xo_YMO6_7ygW2goXYhRrunGflHPvQB3ZSfxeXggHwNS-Nky1785k6GNNqc5zeEdwQ-MNxFoJ02T1bAEhgW1iY1M3c35EqeTzFhxao-ysFONpVPn32p5SoURHlDN382r0wRsF7J4TFeYOe6dtIArY4e4d4tjpnmCNxXI8kpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=mcP9hhLqZXuPL0ae5qSz--K4V_rlQD4BpmsdM1gpwOwLFJv1sXKAK7Je6DXBuK6hwpTxTJTbKZOg-D8aLBLQyb9YHwGo1g4-G1tnYuKcncySZfRGrVPFr-OnW8muEixZF05ZKd2yXPVPZgtKcGLe9jWQo0mmgYgPhIyN_Q2sC7Rqp54Xo_YMO6_7ygW2goXYhRrunGflHPvQB3ZSfxeXggHwNS-Nky1785k6GNNqc5zeEdwQ-MNxFoJ02T1bAEhgW1iY1M3c35EqeTzFhxao-ysFONpVPn32p5SoURHlDN382r0wRsF7J4TFeYOe6dtIArY4e4d4tjpnmCNxXI8kpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDdGLmAEuupwphu7Q2hC1JfyhCcw6tmSX_Jw7bugfOW-j5LKinEAC7ql4dNVGZZV1beQ5Yr5YFIeuE8WH9liTtwAO28Cii0ycCFGqmeERLFNxO66v-uMMfvBS7cZo2EQCWwbReU2881w6WxmqMqD4emkIxjhqzpad9z7qn1b4N12474wL7zG8IiVqjV34Iwebo5ti5WkRes6vtWwfYy93AAnAEmyaalv8hXftSIp2Uuhuf7hm1Jqt_Cffyd4HxlGj70mlKXUkuSI63Vl5jZSxf18ohIjzgTcFesb0a2YYu-piqMytBMWVK3jyXXFreabOJR0fVp2DfKIYcCrlS_g5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=L9zIdYLjuiPWWfUOmhM1Wo5HrDZ5YGHxSChpFuWxXj7lmME2Bo_P-RYWkdSHLye5hbKwVoToD2okFKwgPLFpf503ij1u-qGpFag0Zv4E8nMUSzKy3A0o6nXL2kLzFJtFCpteIk7OxEKb5E3oIzXSjXZHsKmKKz9y_9ogE2AA8eDXf1EnbfgE05aNXJts9yhGPHjUQEcfL0DvoIuXNBY1cGsSnunJa1oVQNGM8nutvKxZj6H24jA54Fx_4iCpcbsvaOan6V_atydXId3TtVyPQ6AyOegzlMpJu_5W_s6LxlhO9W-0BEGNJqwB_f6bi6ZEkDmqeIQBWYxa07f8MVK8Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=L9zIdYLjuiPWWfUOmhM1Wo5HrDZ5YGHxSChpFuWxXj7lmME2Bo_P-RYWkdSHLye5hbKwVoToD2okFKwgPLFpf503ij1u-qGpFag0Zv4E8nMUSzKy3A0o6nXL2kLzFJtFCpteIk7OxEKb5E3oIzXSjXZHsKmKKz9y_9ogE2AA8eDXf1EnbfgE05aNXJts9yhGPHjUQEcfL0DvoIuXNBY1cGsSnunJa1oVQNGM8nutvKxZj6H24jA54Fx_4iCpcbsvaOan6V_atydXId3TtVyPQ6AyOegzlMpJu_5W_s6LxlhO9W-0BEGNJqwB_f6bi6ZEkDmqeIQBWYxa07f8MVK8Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=Cg3GgE70kY-mMqweCDdGNyfMsUclKWpaCyY4nS71Fzg-cW7pyi_id4L6RfW_DXFAONqabkOs4keslG-i5qmgXiVmtzSIxSDTo3D4l5w8ec0e6xR700LjLXkmaP-tOIq7ULiwm1B52bBNOxUz0cUHfCd5Mbv2-P_dgj46QIBd508hxqBJu_dAvJDAlUR82qdyoCXROn_jJCNONTbgBf9xNusUjDqUyfKtqiPnn9V1xKQl5mnM8569I0ofe0Q2UzEzc_BIzPP_tqL-1-iEac-2ysLPDhtttyCU0QzIg93cALsaHKvdEKKRQm_sDQR24Fycj8MXh8xhznf7tIZMCaqlnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=Cg3GgE70kY-mMqweCDdGNyfMsUclKWpaCyY4nS71Fzg-cW7pyi_id4L6RfW_DXFAONqabkOs4keslG-i5qmgXiVmtzSIxSDTo3D4l5w8ec0e6xR700LjLXkmaP-tOIq7ULiwm1B52bBNOxUz0cUHfCd5Mbv2-P_dgj46QIBd508hxqBJu_dAvJDAlUR82qdyoCXROn_jJCNONTbgBf9xNusUjDqUyfKtqiPnn9V1xKQl5mnM8569I0ofe0Q2UzEzc_BIzPP_tqL-1-iEac-2ysLPDhtttyCU0QzIg93cALsaHKvdEKKRQm_sDQR24Fycj8MXh8xhznf7tIZMCaqlnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi7dXnAPJjqpOWSicO8v3gdKhtLKaxVkCj04Y7vT5IX2jWnqqSMhpRdjxwJjcmqu0BmIUhwLeIDEDsLCzQlRnWF6A1EIegPOWYAmK5XS1vM5PUUssdSNKuN0D0ZuYLswK8oU3M0nVpvVq_q5Wi21BDBxGi7b4xkCGag2rpR_kfcZwQhmQ2Gr4RMhOXMdA4f5tV2imifUbK9PSBVqhnyOddCFoDDWpcyiiTOJNmJvhxwkgGYVSRxfAgrjZkEblUCDG3tsPtFqTH2gWMT6DfZneySNShQMelUb5B56klugvxH3XnQFCxd4atHEcjJWGHS1CnA2Xp6tyB2ijhNdv_NBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocaopJAHQfFVm7eI4ETP91pdIia-ITi0cmHS68Kc9znFauih2rOn5PkuPPSCKDJadVpqIcBcXjcnkLJzlZB-9TxDj9y6-eqwfY1z6w2scuHetV8OCdl4VA2LXqre9_2PH0ETp3KwKvBFuHVFL68WUMDaIChcfqHLnUtBUpDEt2bXfv1ux9kwII-QKfMNNEfzZX2MvinYg65RDMAh5QhfqNJq-jSI344fv5NX5EyM8YXcg0JiM3HtaM09B-eFa7_pUD2iZ5ovP9EJttzOQ64eLNuTQm9SizzJ-pjoKrQmwybb2ssGMJt6O3wCJJbab9yDNTH8YJ9HBMRYXi23iMoC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=M1BteSSyueeHCVgHVfZPlo4Rm_MXXyMEYNFTuaJG26esSdIc9U-SH2lVoCqM3XPe1LlxAmoQhU4AuSlnuFN1yDi3VWqtKdPKkMZWBbJyPEX7Albvoak2qUYk6rQbghwb-RrKC6UfCvUye5A5IzjqMo1ZnWlV1e5uUvovMvVjj39FoNAgouDoXYVYDbk5lOuiFBTS_yZBN-fO6E6CQ9CUisf7CHdmBOvfwwuT5tXn6EXsuEKw01CkYKVgv0V1xDcR5l6qFw9Jv6aZRdbU0xRaaTA9lx5pTKRMO1W3cTYU5e6OStKbYnS0jjUCiNdGFdUqPZrJofPo5k4E6AQ5n8sXKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=M1BteSSyueeHCVgHVfZPlo4Rm_MXXyMEYNFTuaJG26esSdIc9U-SH2lVoCqM3XPe1LlxAmoQhU4AuSlnuFN1yDi3VWqtKdPKkMZWBbJyPEX7Albvoak2qUYk6rQbghwb-RrKC6UfCvUye5A5IzjqMo1ZnWlV1e5uUvovMvVjj39FoNAgouDoXYVYDbk5lOuiFBTS_yZBN-fO6E6CQ9CUisf7CHdmBOvfwwuT5tXn6EXsuEKw01CkYKVgv0V1xDcR5l6qFw9Jv6aZRdbU0xRaaTA9lx5pTKRMO1W3cTYU5e6OStKbYnS0jjUCiNdGFdUqPZrJofPo5k4E6AQ5n8sXKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6nYKxSQhQiEMtIEiA_ZyNAy7hmhQeqDy1qtOv28JwIK86QMCcV8cBZM_GSWuowEVQrOT3zQLvedGM5acYgnnHJuL6cT7DFimeozf_yTOacS3Lz8BS7mZj-hdJVoLxqV-I2zW3Xa6pOkoQayYHC_WfL9lN2nQmkbhdNtxBE0CpdwFUEUhxviqQ8c127PoptKf4t6zjIdkDI3fsTljhkHcSqKES3PWhDE80uzE7pbdSEdjxwEAf_mgHazpV9UpVj3qYoSaRhDgbm5sCh570Jjo5Yb_M_IjhtwKGjmWkdUX9jyRl4eZ_DI7DMdZ8JAIrMMrYEMfxEit0ztboxoTHemJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=oGNHP_DYkaKy1F_AUrC-Q5oGmU3FGwWnGD3-NUCJP1GrTAk0GqhyDvIruYs83D09w68tujFl_CJshQYugWp6Efl5iVgCFwlASCh0s6NzL9t8ZNHRlGzV2ihVA6aowuPMvbwNTcicB5Q5I40G4zlr6rY4rq49m-XQKnclFc-cOqeVY_JGTmUjLu6kE8a-DNVuG82QesNMpYsTcwLAcLyj2IXHP9AxF-DKwU6vZVO2rMN_7KJQbTDakBSBLBBZ7PquWbDk42ltAuPK8D4tXozrXnbKIj0OH8IgYBtVkAcVh6Go9WHnxtAMnPTppcbxeL0widv6dHski1dYgHRw0VlNFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=oGNHP_DYkaKy1F_AUrC-Q5oGmU3FGwWnGD3-NUCJP1GrTAk0GqhyDvIruYs83D09w68tujFl_CJshQYugWp6Efl5iVgCFwlASCh0s6NzL9t8ZNHRlGzV2ihVA6aowuPMvbwNTcicB5Q5I40G4zlr6rY4rq49m-XQKnclFc-cOqeVY_JGTmUjLu6kE8a-DNVuG82QesNMpYsTcwLAcLyj2IXHP9AxF-DKwU6vZVO2rMN_7KJQbTDakBSBLBBZ7PquWbDk42ltAuPK8D4tXozrXnbKIj0OH8IgYBtVkAcVh6Go9WHnxtAMnPTppcbxeL0widv6dHski1dYgHRw0VlNFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwSFwgvsWyrBciiWqAO__ay2Q3gFTL5RztHbIwlqve85fZB7VpfWeGkT5sNVtyO2RxL5IpkZCYJ49TIb5zBvDwRxZ_UbkUXverKTCcgeh179VMIH_tqabKltt4sIY8qnblVZWsd0qrV1XeV2V-5U8ARArKXgvex_XKK0CIXW9mK_ffMmsW0Z6i83LTewqqlZaA6HCkq6ncgb0CejgTgE2J_IawBVZ9IlEZsyis36BKVyMya0vSebCKCk78ORWevtVZYmBs3yLHKvY9kZu91y3r0HtYjwz0ywyClmVdHiV830ls1335k1SjNmLb3In0UL_o8Q4dzMAHxNVnnMZANTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=CsJ8VnGzYKdyW55EY_dS-g7oGoKq_o1tpo0MerZgqkeRkbVeAmaquz_J78F526Zshw6ivYguq7hVkt6kLGYQgDf9YGXYdeDBv-w9R8opkzGF2bmYNRQEqFsOXClMhCOj6XdWb0YLLB45Bi13Sw3x41mAzjgCKOO42K-_AfZvk5tV0kesznINFOTVmF3Ixrm2_xwPR5dy74rFMXRYKJK_5Aq2_zrNYcjA5aHzOaPmClwO94nuy0R6kAp4FuVagUv2jcGEmo9An_tLr461sOE4O_WN7n63u-hRtuqQS3zwk98uC5qn3RJz4Lg0sQ3BMvsG2LjD05JOADXv0-3E0YAaQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=CsJ8VnGzYKdyW55EY_dS-g7oGoKq_o1tpo0MerZgqkeRkbVeAmaquz_J78F526Zshw6ivYguq7hVkt6kLGYQgDf9YGXYdeDBv-w9R8opkzGF2bmYNRQEqFsOXClMhCOj6XdWb0YLLB45Bi13Sw3x41mAzjgCKOO42K-_AfZvk5tV0kesznINFOTVmF3Ixrm2_xwPR5dy74rFMXRYKJK_5Aq2_zrNYcjA5aHzOaPmClwO94nuy0R6kAp4FuVagUv2jcGEmo9An_tLr461sOE4O_WN7n63u-hRtuqQS3zwk98uC5qn3RJz4Lg0sQ3BMvsG2LjD05JOADXv0-3E0YAaQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=FoJyKqECYqiLfQVwgJdKB8T7-qwJZe7NleO9Yhvt13uwpVp_XnpuwLClu2vV6U5OAT2LLm621kAHxcIGMP1EYoTFxir54HKcWuNVb6PFdonrZiH52E9e6ZY9EC2VcYJ0EA4s795JFpPlBUOK_B8M8O4gxJBQgQfOk8BZXsKntxMTgFZwSXNhmfCjkaKV6wETgXtxZKFJVVL6IEEAIQWahj9zhwS-Lw7MXWtVwwGhMXGxll4thDHvhugbTMaqO-XllvXI3xRGjWtPhBsn0VCVvSxeC2KY6unSL5hSLuGPrrHXdzD62JNmGmTD3xttuE7_O61K2z8T2EWEu4qkfDsQxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=FoJyKqECYqiLfQVwgJdKB8T7-qwJZe7NleO9Yhvt13uwpVp_XnpuwLClu2vV6U5OAT2LLm621kAHxcIGMP1EYoTFxir54HKcWuNVb6PFdonrZiH52E9e6ZY9EC2VcYJ0EA4s795JFpPlBUOK_B8M8O4gxJBQgQfOk8BZXsKntxMTgFZwSXNhmfCjkaKV6wETgXtxZKFJVVL6IEEAIQWahj9zhwS-Lw7MXWtVwwGhMXGxll4thDHvhugbTMaqO-XllvXI3xRGjWtPhBsn0VCVvSxeC2KY6unSL5hSLuGPrrHXdzD62JNmGmTD3xttuE7_O61K2z8T2EWEu4qkfDsQxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuRDkgFdp-535RCghCW3mJMWrv2bvumaOK_bJo1pSlqv99bjiLfdTyWG8NFcGIGyJDpkxhuqmD7Kh7qAB7kD4ttSe2w6nBolm6UoMoyPNdYXdqlyoETAh6FC5pLVUpf2wegRBxJW9aUvK9BHt9kRi7WQCsv1eRkWR1pj6TK-W2mDXL75sH5Fj8P8m3JDwRceD24V5ADSpZL4NdHOza6gldx-gnbaN_SdDOKxzDNQL3WdSp7Wh1NC4wV6jQKl9Xwe0Hu10KT6kM05cAAVOVtGgvqjzVvjqJbqAKzbP4UUw-mPZpaqdA3M36G3EMiwrrBJdqM-7tunyy-qtikKU2DcGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhqeIckdGncmHyUERVnLBnV_X-DPbjysgNJAYpVGhJciIwmTDSy5RhcLd7XG7p01L54ethB5DX5LKHvcJQaAje0T1_4c5EbhX72CfGPf8i4I-uuu2RyEl0J1ciB-nj9De0AAACiQEGvqgbMv0jGSGUG9O-PsdAOwoClqHiKwu3GsA-Ay8ldYS6ewuD7_wQzyDDx9UWgGGJlpmYJShq5e7M1s30L_PkYuyAum6BEMOozwhzYYdx8gYfNQ8jG4QMqYQL-I-x1np2Od83I8XYVCi7IapVTG5QbeaRMOhaoFbtFvmiFni2sO3qqAGYQVIA3cAzSyj5V_6ZtohcQ_62zzyBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhqeIckdGncmHyUERVnLBnV_X-DPbjysgNJAYpVGhJciIwmTDSy5RhcLd7XG7p01L54ethB5DX5LKHvcJQaAje0T1_4c5EbhX72CfGPf8i4I-uuu2RyEl0J1ciB-nj9De0AAACiQEGvqgbMv0jGSGUG9O-PsdAOwoClqHiKwu3GsA-Ay8ldYS6ewuD7_wQzyDDx9UWgGGJlpmYJShq5e7M1s30L_PkYuyAum6BEMOozwhzYYdx8gYfNQ8jG4QMqYQL-I-x1np2Od83I8XYVCi7IapVTG5QbeaRMOhaoFbtFvmiFni2sO3qqAGYQVIA3cAzSyj5V_6ZtohcQ_62zzyBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFxoOY3rRd21VV1SZdlYbIQuDVLugv-BzhiwCI3mM4tUIZTLLQG94WIZfqUOcc9-pjTOv58oruMQw8nOTycc0I3WAAKZHnivY1fgU_lYzbmCwqEY7yIaJVmtiO2nN7ITZdPoW8Stiq4tdczfE9dz4ZuKOTkNn6naxT2vzkh8J0TbWbGM9dMc8uqkU77HBmxozvO4VrDP8-kzkzOJZys3gwCnJH1uM6KAmV3feKhk_WUklnpVOLXnk8ZFIJlXU6pjZl7CospM0NR7Lmm9BFyzkPZw2-1kOur_dRI0wXxbbliCaak9QBlvZSx9TQW9RPwavh-hNU5RyyDmtK-XZVS-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/apP3yDhHMUhYk9iSR1dXU1s3b1U8-hkzy209jcBmI_qHYKn7aMSoKeW7pC2os7JJutHB78Ry5eNv2fUcvNYpdkAQ_0qqnyOedvT0Uzx0UC0IgSeFwC2uOH6wgoBEAu4rP_hI92P4PBxQgqJeLwCtUmz-a26QlPbLGLqwerLHJ-qkE4yZgEm0N9dOWzSp5E00nPnZCFF6ivg-v9kTDmpWbg0CY9LzbzCneKHAe-dsK53pk10UP1q7WOTPExAkbtguazmyi-yxD15ll7QfWHgomtwwvsuFR7U2vZ8SiQwLBAuBs4GIO6R3TYaUyAr1GB-HjLun6r9b9dpEw5mPbQSFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=mZRjFct7WX7CDJ5EME-2Xj11Wm8J2oSaE6Y26ur5R9PkQ6SbTz6CckjQElI3REZHNhLJKYCVm_l5L_4Bv-JsusIytZoPwYgULNCwjGeGpC-RCosMRisWn0eDsz8ydTkYIe-ZuhUKDl1sTQrPh6uSpIPwQuEq9A_wWSMhNw02DCBaHmRDpcqvfg1AzViVLxaJc4p_-Id0rXg-mKgrSV4G1BDRrY95IdRxixoJpvrGKdepNpfY2i3RkaPyl09XZHpotDYaXrbnMEV2nardbjb8AEi7D3M_Wy_C_ioFPVWHk96hGPUZ-R9wPqVglZhaPgT_-cQZ1ljOg_kDSgSJ62X_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=mZRjFct7WX7CDJ5EME-2Xj11Wm8J2oSaE6Y26ur5R9PkQ6SbTz6CckjQElI3REZHNhLJKYCVm_l5L_4Bv-JsusIytZoPwYgULNCwjGeGpC-RCosMRisWn0eDsz8ydTkYIe-ZuhUKDl1sTQrPh6uSpIPwQuEq9A_wWSMhNw02DCBaHmRDpcqvfg1AzViVLxaJc4p_-Id0rXg-mKgrSV4G1BDRrY95IdRxixoJpvrGKdepNpfY2i3RkaPyl09XZHpotDYaXrbnMEV2nardbjb8AEi7D3M_Wy_C_ioFPVWHk96hGPUZ-R9wPqVglZhaPgT_-cQZ1ljOg_kDSgSJ62X_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=chwaq9DzWpl0mxieOJFQ9WCjESFVbu14GtIl8BThmr9NMaVlyymgIvUwD6GfqNOfLhnBebqKeShJhqhoIiZc8vNcpFHwzhyt9ShzPlkDdFUJ5SktORpJuaAHlukfRMbroQG3fv_viVEOEQQkpFvMKDJzMYxQTI08NNUyQVmTFkumMM1S-1jtr-nIrZGM4vsYiLEZ_GYUMkqUEtXCFU632UEbTsV4uGVAe0IEYQ27SoGCtwi4m6xcIaJFOkIB4Q-MYUSS0Hh3VSw0bBmObF9AU3JZB_xSgjW4hS9FFmWAuXJNh_Y9HqmSv0mCQJn74oTN7DrmG8VaGLJdPWmH63E50g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=chwaq9DzWpl0mxieOJFQ9WCjESFVbu14GtIl8BThmr9NMaVlyymgIvUwD6GfqNOfLhnBebqKeShJhqhoIiZc8vNcpFHwzhyt9ShzPlkDdFUJ5SktORpJuaAHlukfRMbroQG3fv_viVEOEQQkpFvMKDJzMYxQTI08NNUyQVmTFkumMM1S-1jtr-nIrZGM4vsYiLEZ_GYUMkqUEtXCFU632UEbTsV4uGVAe0IEYQ27SoGCtwi4m6xcIaJFOkIB4Q-MYUSS0Hh3VSw0bBmObF9AU3JZB_xSgjW4hS9FFmWAuXJNh_Y9HqmSv0mCQJn74oTN7DrmG8VaGLJdPWmH63E50g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=EUFxJXf-4AsIulICx4G80rt69VBMw5X3T7LJeR3HEdLdhMRVEAoQK2NiexGYZEyRDtjBArElZzbRsjvPgwGi_nJYXzyGOFCRK1nXwo9GO4SMO5wShneEfRf2py7FiRsIGXIq4ziYAdXSwpbuSJ67tT895vzYX3IjzSIn3k-_8X5WLbyR4DwiwGTMsMJ2NysOkyW2mduEO4spFmbzG1kyn_pUYerUtT-xbCfosM5975L2n4siknX1ff5uC0HIU2VMwndhL3Oc1p4DXJf4mOfGa4gmid-q7nTJIMK28HdAKfgFfLG0gk2XWcOzSVhzDM-GY4AR5OF76gy5CTsWov9Lcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=EUFxJXf-4AsIulICx4G80rt69VBMw5X3T7LJeR3HEdLdhMRVEAoQK2NiexGYZEyRDtjBArElZzbRsjvPgwGi_nJYXzyGOFCRK1nXwo9GO4SMO5wShneEfRf2py7FiRsIGXIq4ziYAdXSwpbuSJ67tT895vzYX3IjzSIn3k-_8X5WLbyR4DwiwGTMsMJ2NysOkyW2mduEO4spFmbzG1kyn_pUYerUtT-xbCfosM5975L2n4siknX1ff5uC0HIU2VMwndhL3Oc1p4DXJf4mOfGa4gmid-q7nTJIMK28HdAKfgFfLG0gk2XWcOzSVhzDM-GY4AR5OF76gy5CTsWov9Lcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=kctUDsENWIQDkGj7eNjrTG65DMXmxHizjV_2V9W-dx7HFgvFBq3uXFdV92Yrn6F3onAMzH-BqrQ-lJJcapb8kDape6G7bnJSm8pe91_WDixuFL_sJdZDikzyItqfDlqOQq2n9qff01-ye1mCclEZWhBSt97fjdvnq0p-CXrgymYMiF5VUdAGV9uIj220cw7cu1a4VL0p2GLPu5Xm5M9GI41BT_Qa1i6EV3O1Zvo17MDrTtEo4sv1Dq0APnF3Wwjs42D_ypGciD1koxvaSYWsb2pB75Q8lkft_iUsnSI_PFw8DvpkmxKs9Ovt5SDb6A_jJVJelQoeSubye3CMITk2Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=kctUDsENWIQDkGj7eNjrTG65DMXmxHizjV_2V9W-dx7HFgvFBq3uXFdV92Yrn6F3onAMzH-BqrQ-lJJcapb8kDape6G7bnJSm8pe91_WDixuFL_sJdZDikzyItqfDlqOQq2n9qff01-ye1mCclEZWhBSt97fjdvnq0p-CXrgymYMiF5VUdAGV9uIj220cw7cu1a4VL0p2GLPu5Xm5M9GI41BT_Qa1i6EV3O1Zvo17MDrTtEo4sv1Dq0APnF3Wwjs42D_ypGciD1koxvaSYWsb2pB75Q8lkft_iUsnSI_PFw8DvpkmxKs9Ovt5SDb6A_jJVJelQoeSubye3CMITk2Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=THnUG5SvW839sbaqHON85-6qKiSWNkTFBCddQfQkR5M0qYnCGN4Vd-H0LkwihtNHbJWDhla9Db_nTu2lIrdV3FFiqIKfVlQP0TYW33_8e4GCCdinSXo-t2xKc3qaSJM69VEtMhhJ55sGZASQbnAZLTGUIQW4Hjb7z36lrzGTtoPhE52N8J77Jd67_64blRNrmj8fEJXx0HWStbTLuqbVtIqxO9s6OQ0HCgz10zxwuwJFxzRUpjqY73CsmIPyUy1JKb7jlrLNfXoZy4lun3OGOv5uB7mtbPCSc-M3YVTxUaeLFuse5Ovtye6ROvSL-PDq9cm5x7E_oHJ7CP6_TVJUE4XgeD0GOYlXsivAD1i2FwB4zctJvJS8OJ0q_nO9LJsuvWXSFy-bHnA5zCuU66XIYiYAFT7nD98ltsB1G_j-E2_mF7Ew-eiAeReBw1OmNrlZvmEiTmd9knd8H06F6Dc1wHehBiM5lfS8aemfssvYQQYAEjjyFSNyJVq3LysktKQTriuAd9eOqBupLeD1sp_5-J7evLx38z71-XcwT_TkWReAGfTA3GF7-UkuzFnD3b2K5WfV5v7fPpPOx25oVAMqIneZV5v3Ez3qd7gWdS1VrdX75MV-5dIkYCNzhl_zDI2oM6ZjFBJ6YEDelcHwQUVOAksNm8uRy0c35lTLeChk8q8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=THnUG5SvW839sbaqHON85-6qKiSWNkTFBCddQfQkR5M0qYnCGN4Vd-H0LkwihtNHbJWDhla9Db_nTu2lIrdV3FFiqIKfVlQP0TYW33_8e4GCCdinSXo-t2xKc3qaSJM69VEtMhhJ55sGZASQbnAZLTGUIQW4Hjb7z36lrzGTtoPhE52N8J77Jd67_64blRNrmj8fEJXx0HWStbTLuqbVtIqxO9s6OQ0HCgz10zxwuwJFxzRUpjqY73CsmIPyUy1JKb7jlrLNfXoZy4lun3OGOv5uB7mtbPCSc-M3YVTxUaeLFuse5Ovtye6ROvSL-PDq9cm5x7E_oHJ7CP6_TVJUE4XgeD0GOYlXsivAD1i2FwB4zctJvJS8OJ0q_nO9LJsuvWXSFy-bHnA5zCuU66XIYiYAFT7nD98ltsB1G_j-E2_mF7Ew-eiAeReBw1OmNrlZvmEiTmd9knd8H06F6Dc1wHehBiM5lfS8aemfssvYQQYAEjjyFSNyJVq3LysktKQTriuAd9eOqBupLeD1sp_5-J7evLx38z71-XcwT_TkWReAGfTA3GF7-UkuzFnD3b2K5WfV5v7fPpPOx25oVAMqIneZV5v3Ez3qd7gWdS1VrdX75MV-5dIkYCNzhl_zDI2oM6ZjFBJ6YEDelcHwQUVOAksNm8uRy0c35lTLeChk8q8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=go1fF5FBb4fM2nZej0Wa3QOXpQhKfcUySN7877nsV1B7MvxupvGIDn6wsYuYGdD8gWfNbgiBvahkFuW75xxTbbHjndxfnT1svP9FeKiBzo_qXbfNPXXYcB2fBt7Uf_6ROJswPTehbXUaGMr9X5__KHUntUgsc_O2I3IiVhAomvRUTagsOwwLO-jP5IGNzIPsdgvqjMdeEY6c4rLz7yhbFdOcNR2dSYB0JKVLsdhL09Z66CWSmj9LpNW--4u1OJb5Jl0hlpV7OsDB5ug0Itgv4PF33HsoO8HRu8SJx3y8KSupJAnK7PafP32DGLg0Q6bQ626xewK-Du5NhDuX0PGGZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=go1fF5FBb4fM2nZej0Wa3QOXpQhKfcUySN7877nsV1B7MvxupvGIDn6wsYuYGdD8gWfNbgiBvahkFuW75xxTbbHjndxfnT1svP9FeKiBzo_qXbfNPXXYcB2fBt7Uf_6ROJswPTehbXUaGMr9X5__KHUntUgsc_O2I3IiVhAomvRUTagsOwwLO-jP5IGNzIPsdgvqjMdeEY6c4rLz7yhbFdOcNR2dSYB0JKVLsdhL09Z66CWSmj9LpNW--4u1OJb5Jl0hlpV7OsDB5ug0Itgv4PF33HsoO8HRu8SJx3y8KSupJAnK7PafP32DGLg0Q6bQ626xewK-Du5NhDuX0PGGZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=UVP3hItcuCNt6WWJTK-CjcDEOXwVUmaY0wpFlx-zRmiZLS41bqf0J4vtQOYcxj4wJKfCpHot-8qg_8FRS_D2Neq7ztn4HtOXoaYx4Lx1VRDeLcjpayFl6phqcLtlT-9-VwK4Cqo1-T7-gyLpOgtWRIAdby0BT0lxKKVsk7wsoR6_V-yE-Ii7Zwfc7YXWNJdjCiA11lXDn2YsSQjED6-4Z2FMa-kB3hm95VymO7w9ywz8KwrTR2gbaVyvB1Ej_GFfrkZbaBbDEFeayzj7myJxUBOFA8B53oz4hKM2oLKtK93Ds23OeHb_PXv2xpGUqsjgbV-JEEVB6Zfizfv1HLkUiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=UVP3hItcuCNt6WWJTK-CjcDEOXwVUmaY0wpFlx-zRmiZLS41bqf0J4vtQOYcxj4wJKfCpHot-8qg_8FRS_D2Neq7ztn4HtOXoaYx4Lx1VRDeLcjpayFl6phqcLtlT-9-VwK4Cqo1-T7-gyLpOgtWRIAdby0BT0lxKKVsk7wsoR6_V-yE-Ii7Zwfc7YXWNJdjCiA11lXDn2YsSQjED6-4Z2FMa-kB3hm95VymO7w9ywz8KwrTR2gbaVyvB1Ej_GFfrkZbaBbDEFeayzj7myJxUBOFA8B53oz4hKM2oLKtK93Ds23OeHb_PXv2xpGUqsjgbV-JEEVB6Zfizfv1HLkUiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tggv_KUvYOrz5kgNweVB6ytvaFFbUfVOQvRxTeGYVtv78HcgIK-LgcXRQCceDtxxkK3Bf6eb0ZQskxRDjrwawghkOpnuYYFOUqmXkrueAgc6lPCKiatfR4uUclXqytjY6LFBoF1Qe26ftcwIz5VB8PqFS-DyEMPE-MGin3nFUj1Yfn6TyUrZ2yXU9kyoV23VaPt0lmB1X6b9DdfYj9Q4ru121xH6C1hNlndTUCCx6DAPlPcIXVcVQ0moy3mReav2SxnVe1UwHJhmbOMkkSWDz-ZK0wK8A4_OTXfufXV69ypFaG3C4vJ-xoBzsmFfvohe-CnSEWphj3MCxpRhR72pPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
