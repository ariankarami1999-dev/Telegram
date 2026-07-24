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
<img src="https://cdn4.telesco.pe/file/rp_LUFX0lCTrkEOG8Waw5f5TrwOGt5TpNW_7HbCpFuwUY-Vfv3yQ6lL1MXcq-xw7il9Ewr5AFGpJ3E-KQOXSB7AskIvh8WJR4MQU9VyvYby7v32mG1M7N5u1LWWRQ0JCOmMAyIzuhm4W9NTMiUMdgaAkM-6xTlX4Ae7raIgkDPwLJzfKej209vuZB1lJZEUKPPVqF-MJ9FZWYVuDURd7qtu-d9jtuFBIqJCbYfx9lbpAQV6vZ_2M0SN-oSwThhh-xir21DnTpG7P6pS8UjPQ9Y48JGfn251H4mrLvm6LJL7ABWqwY2wmiG-i0ExYsqrpAM6eFHli5q_RrEe8a-3kUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 571K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 01:03:45</div>
<hr>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arYwPNq70jOGRjMK2BPfAUO0V8vU75l4A3HFyFW6ltt0HMu8GG57oyNjRmy5-3B9j8IEMlD-mJmn1HcgCMcJZLcnrEqWJuGjjCjZHjYtJfSE6lJJ71gWXVLdJH_dSkA3SrILN-DJNoe_yytBNrZt4cKhdXf0DvIHV7OHt3GLyGRA8rEZLsc9D6RKTGdniAUYwOYi_Pa2A4vyKF4_fEzezYXLseibsYz1E7NAEFa6D9y1G1iP4rQMPuqfR9T8aVCr1F35OkmLfZOtlm1UIHCm6COSD-lO13XHmgCWVO2CfcjEAQRVFmLD7Cyoni8gmQvdCz4T49B8irL1w7t4NgJ3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیونانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYOeh3NNTZJWvziDzyMwJ6ZRkrUFigB84Q3T_xo2KUmpxFQCEdkQRGGc8-96DnRS87S0KmruzJpdRiA8iWX8Nv-SxTbcRl5a8ilOBcxP9eVTKjt7QqGzwCUtkGDlnrek_M8FQvostTLV8M716IS6RPmclC9TJ3sqnpG0kiSKOs3kBRLo4BnP-5evivBYfwMVB0T2bipAjIhs05IsnGi-XcMkaGEz4P2LnuD55eLq80Aq1SqLNKJCHyAtx0N8MWLUyqbAWBNQC8r5cWXNGVTI8Fy7B_WtiJR-VjC7o06Uj64nQ4iz9sRyQqbs3h__fL0Xgq6BzYs27zGWzHyysAQCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMufuQDRIdU9WeqSk3z2lIju6QrZdLJ4F1nAAPEW75yA4BD3BRdT3nMMEZ2YwjPsmDYHzuJBPUJBc7fTFNDJANp0rC3ZWt6zznqR1jzVXrq4RtOZQhRL9xmAxflXclS-C4uG8EiXgs6urJTH-FugAG69UAi65Dysf1uAyIDtKnPNdQnRRY4RPdGGD5m74q0WehtQMs-8TzSdbKvm5TvqoK1AsdXnK5hErBprCD-NZhYeZ3Yaba8Sp4lr_Ww2Hy-OSvdcG18uyDiLRsWpXh99Puvf4vfU99ARkHZ4UQ8EOfy74Jtk-p4zjuBo6CC7rnuZbCdUEA9FAkL23N_ijktM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26449">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmubuZK1TY0Fb4SP5bsQ9ZaRrxRza3Cq4EjPsLagt5L09MouvWgViVkn20JP5sOh-0SQeoI-dQKYM6aB8xU7dkOtgwvhOoBkyV7pAPgqBVrNMjuNNf0aEf9ESykCxFg27v5WyfFNxJTQdnYbyHYOI8BBbL_9KE9CGFFUOyGtZF1U51ALW0nsz2f6hVqp75idltJUi3ioiI1ZixQd5bNQLwHykOYQ2BPQDvTdNjbpzLmg3UhnL-VcVONX__q75hMMIHTp6rRYWybVP4qNmOpobIVUWKUaIAo5uGap62gl1UoEDdZ1Dp_z-WjvInApe5HDsD1Kr0z0Vit3N8Rm4mcSHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به‌دنیای‌هیجان‌انگیزفوتبال خوش اومدی!
اینجاقراره‌باهم‌لحظه‌به‌لحظه‌ی‌فوتبال‌روزندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌هاواتفاقاتی‌که‌همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره فوتبال رو متفاوت تجربه کنیم!
▪️
@realsportsnews
▪️
@realsportsnews</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/26449" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKI-ZP0eJSJfvMbxaouVo9GrWazHdytoiHieIElRJ-plV0SJEPWO8FonzBwqdKr-BBqeyIsZdsp-Ql6SrGVfMewgQnC7sWCSZc_1zMKRc0mdVYIyNqUAN27UPAu3pzxGBYuCTmdgLUEguI8dT8vqzPjAfeU8wJP3PEVAA-qKT-c4p-LUj3Qd7KIgi0XVaxQiAPkRwBWcF8K7z7vrj-QZ-GtUSu6M93z2OMulxM00AY_53A2oY6F6a1cAqZ9dVUZqiR4JhbnUI8ut28VZzsmF56XIXlNRyaFzFLbVhEpwCd7TEwCmtsnbHrhwz8XHANX2kdZyOLabP3g1JDYztLLMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDFqYSWoXeji160qeHpj2qrVxYUNGbgijuZjtSf18V-ztxdVZrDfTBzlbkDiy2sA6PUj_XzDNdqnzZUIDm5ibgBZxJzTdtvNrcPWtHOLaAwCmrhYsWL_Q46fHog2aTcG45iDfy4g9orpZ7vktUtZF_zNHnvwQQqDrzNMLMBjVRq85bINuVBnNG9mvHlTK8-fpsxtOS753DVxv5U_wMolMQiYE8IRvn5Denw8Mn5BXd4hrerdH0flCoBD2eCNcAFZaiBnqmUibav16HEQdOYOolJDJmguAeF3Yd1fejGg3_vMkI8SAsY9N8paA9-Ei2C7NWaprxHkwKLba5NIXinzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJg-8f4BrCwk43qsOEgMLKMGKmpERGv0r5TGM35Ewja0lUVkFFuIMNziZP46M-3h07G7bR2IeXLmD6FJEfW4DA_CpW0PCyHkSkvb6EeHSNsPgPv_ljx9K4B83N4p4-Kv8TMBVENXKveJlshU0jsBAfokW3NMgXTJzFs558wiSAQ5Jaut4oCZ4D4s3GYrV2JPvNJatMBjOz08fGcsEMKjh8HbTdNMLY4MtZGiLQEgY-3oHEuiwpT9bb_Xxwas3SIDO1slnp4K46rP3vSv9H6TiO927gYtpKyEilc57bjlubU0BtLd74wErDkd56gtSJ2a-0DdzHiMUF6l7SJFQOU7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fen10W2RKem78DCYolKy9_GMEmtXPe7vic36BtpZgEBq2YS6WWLB2VTeqmhOqPiKX3xeF9Dg8okA3n0s89AGmiMr5T85JVaCE_R_Wb5r0lnRxlleecQm0Ret7kQ5cjpaPKVoEXwUlOUikAd4Qa1IsFjejYP3W3hGno4f24wJRcsxFmT74EMh2zaFXIwPJPG5DIT1h1VBNGzqm1QsAvklGLv10yAthZZMSBeWHqHnM47cxBDF5uJrcDztbqqBtPryqPzVFqaPx6VZQD9tBPFKfsfxELqV0cIIbMQ_kPS_huV3TNq-O6XjdhF-GeOu-1X7VVIfj7CF1v9BYok6_K6KQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nov4oz8TyZVqFeaMcWjBI8G_v4gQJcrmuwTCke_Y1exqPvJYjyD0b4MWNvKCuh9Ai92uYwMGXRbSRRig5dlUSrx3zo0KVNmW0E6L1pQudY9o08I-UZ3sfv2WACK76xa3s-mx1JpIWftb6TeHeArMfd-ymlCPptiBeVLM9UdxnqATLNv9uCD3m1eQzw3gn6cJ5Kb-17Cbuf3gzOfr-_c7ACgmV8REUUkN4h4kUXfAMQsN2luyvpc0mmB7qt9yyBA9tlKowWrMSoOQQSW0BRfx_zG7-_7_2QM9dX2SVY5urLsd9372q33ZiopWoyd9hxfCKqh_MK1b3t_u2KoTIl9Dqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR2gTi1RN3B9sNfYq8DVDyqlgjxD42KWcJJ6py4rOfPXH3D0rz9jdTCvild7m9EQQHWdgESQzVMmNZw1zSuZC_weC1KKqBAtmahf6bey38irIrSPYEVUvZY7NpEICwMeqyhD4ryBRlhP6AFSAv2E8iezIK1p3O2pnNI1DHDnYLCeVVygQfIN9NszO4kwFvh3f8I-gJ7II_ew8q__0YVz5Uh_7-g-G8vWr6ca7i8QL_22FpHc34J-ZDZDGeuCpfkPAcL93cU3ArZuhP-R2V_KQ2trh3O6s1lKfvf24gIpOGiRna0QDLoCUSjSv7hmuH1TMlyPhbopQ_FmboVQhh_oAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTs5gQzUjGN3_l0o5kjkmcSrkCCk7XOFEfk_yYpCJOGShN2ELbQROfnEfZXDi_n_kuJQI2mVLnslaXrCx9GmS-AOuKWtGZJciV4WeZJwVDmUfqSQr17HDFJMSsr7sKN-Gkp9OzX8kLNAjfNWpfjQFGELSUs5GFpixTfl3FpLyyVTsUGb8Fufw27Wbo4NLU7iYfxXqldgk8xSslZz9hfWTBxbj3zKpKuFzIFd2P0sRou9gBcIu1bJ8z1HLii39USnL8WYPrfzrH4V2g8yIyw3lElhJwSCeIQfmZ_6C2Mr2IQzvaUHyCDFEGS9FvHn1Lt4e8tehDz2SBFjarLzpc3l1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Baz6TpqpGM3jO7cDbZfteLMYZaGAkWyZ66lBa0PVRFCqwXEQn_h7tPwT-L9O0JmEEpldo5vbWhOxrh0ytgghC1kGA9bDx8chg08ohZPu-0vKOIzCsm5U0gJvZzK-Vc2xmcQp8hYiJlHvq8mK8QiV8b3DL4f3heb3lZvZG-xlF6ouSNrrK8gOTvtoUAwWRzU850Qjjp9uhQCdDf8WlrKhiK_lKFdN3gFIZ89p2IY8oDYlCBgqz4zVEG6ZHxB7uWf-RDQo8EpLLbZK7lvHGF_4WY7JsfX7xGn4Ize3d8RMyqGCxftoJ7h_J08UXfxKjMdVczC7u-gQN_6wTINWEdkOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=S8AcpVIrVScHJeIiqVq6JCrrVpaOTRQ6nesMMveyw__KDTe2mDopaWzVBF2nIoZ0P5E9CuICizpDBnEvh39kf7PpROwFpf0lglKET2Z79kKfWreWrQfdAXTo0xHfj0GL9VTE5RBo44Y2gD-3-t_FcAxPdBpps6A7-NzEyUuhGJ7KMoN02Rp9ZsA_K027YRyZahvE7Xs6MtQmxlxVkM_uGp2pqyoUdwfzNBUzsAJoKW_LMwLzKZ_B9214Uyc3GSEfbsjm8BqlkD5VO1DBH3h4AuSPjYhVcT00ncHpzjv02C9JK2hNGJPE6nYKlDnlrM5ZL6euluWppirM9tfIT7gN0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=S8AcpVIrVScHJeIiqVq6JCrrVpaOTRQ6nesMMveyw__KDTe2mDopaWzVBF2nIoZ0P5E9CuICizpDBnEvh39kf7PpROwFpf0lglKET2Z79kKfWreWrQfdAXTo0xHfj0GL9VTE5RBo44Y2gD-3-t_FcAxPdBpps6A7-NzEyUuhGJ7KMoN02Rp9ZsA_K027YRyZahvE7Xs6MtQmxlxVkM_uGp2pqyoUdwfzNBUzsAJoKW_LMwLzKZ_B9214Uyc3GSEfbsjm8BqlkD5VO1DBH3h4AuSPjYhVcT00ncHpzjv02C9JK2hNGJPE6nYKlDnlrM5ZL6euluWppirM9tfIT7gN0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsk0LAIjUp4S51ichYWY4t30zvTj_cBdW5TyMHYdGUGVLdP-sqXLp-uScTMTKzQsvBJEsSpqpZCQnVdi7wQrElvKlnU66u26GBaIETQVnbFlsQr1luW73hhECLWVdzqbeWES-nEw91SqT69W6nPFOHoaIn0BryZDqpJnmSB_ucRQp9XYj4kis_87cuIjbdsuTIlGuNBOLXvvt9ciW1eMmW1urJbg6GJNBmss9zvEg179vtAcJetdN_xAejY302btV_2AXLyhE72ioZYlpExGtu0U0fLksOwFPrOhP-9uIwkv_vCIRiUUG5U0Ry5lkOYhjjx8-KItWUkuaxwvMIts_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmGVRUUU9nm9bQO1b19kdPaxBJphKpPn5sc1pYe9GDxvxfWu6hhIUgMTZuuOGuDz3H7i2UQSZsP2a_4VaIBd0URdA9rr-UdmeyaGUeE19YC1bZ8eTQYN5JcBXGZXrWh4FTK5Fs2hzUSsmFY64to9yFxDJlrHH-HrfczQzSqQnsu7CAw7xEFsVs8Be5oh6EvhDnrMsgHBt7QSDgiVJrkFcPQ6LB0FjXNpAPtNIZwJk2bRMVM53qPr-CZQaRf0WYleuiEs50IlYwDuO4dUbCXGASHKO0U3tUb3Ov8D_9k6FAkcr0YfymGNEpmAKwKZumuaUY91lVjVdjXagS_U5uzG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIQvtyPga3SAWJjoE2TC1AQKAlvGc-cQ2z5iSh-CsZ-UgA7g8J7dCS2FcpRT48egzDeb9p6y5mHMvHwgUXJpJGMHGsDWWojJMPVnjzmGvq2yr_DGP97lhEnVnT1hIyMVKS6gJi2ZxAwdjHXngPLBp10g1lUeAFhcUpsrElrooAU9bilM3zGPJoxmMjLzxHhFEie_H9KVed38OjuAMj9_5MLzUFKoyhOgSAuJrnsWGjI5vv2IITuI1ONjwiod1mSnhpWGZSRH7kT8cRAl92ak9OLDvZlbHpSbC3MyDgKqL9qX0sVwR3fwQgn1m81CDmvnX4HmPeuMB1mKrF8pt3YEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtrhUHxPNACw-rlGtC7_14IPVA5auppECpLbKAnLy57fPxQJS-VjmbUATNiBztkGt2VNHfd-XbCgTnZk8im6lsF61q80B60A-ibTRNW06UBaFmRWCQgnkWKGTj6Hruj2szE876pQQXhkOS-mR-6L8_lHLwqJtXzJJ5GS8pB_POS50VmhPbqi_m6koWG7L1t2Dtee7vEoh-Ity5vYjcZekDXh-prO8NWhvn5DSXoSIHmTvVoCRIis7i8mTAzkaW3Yz44uqJNNuC0qtpIXewcwCcdl1l4bT-ClgTORF6L9taSxdxENE_DIb0a3ISyy_uMDlfaolPbjkttkUgSsx0Zn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=YlbFlja9LXWDaSqEKBsNY38M5xAcjHxgqD_L4Hb_2Q8RhxWoqpivkS-p2AMw8CVa9CxszDRMR4fgVEz1RT2CAXN9o-SGcURNBf142mBjgA73uSNk0IL_ZbGG0rX45SCBdo-FloNNizPwomXqumO4E1YWGPqWdegGFW10I0_iOialcx8LiW9OMuVGU6RSSYaS4ZFzCzipjVOkW9GH6CkzqIz4xGHnF3YS4qxuFimERIoixjdbfiaSor2XDQUfcxQAv63GYU0xOK7xyMCiK639CFqRYxLlGxcbjzwmnA8WipBlTi8HwqgmoaoN795LLliIva9uY41MWsQZubpcbwIRMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=YlbFlja9LXWDaSqEKBsNY38M5xAcjHxgqD_L4Hb_2Q8RhxWoqpivkS-p2AMw8CVa9CxszDRMR4fgVEz1RT2CAXN9o-SGcURNBf142mBjgA73uSNk0IL_ZbGG0rX45SCBdo-FloNNizPwomXqumO4E1YWGPqWdegGFW10I0_iOialcx8LiW9OMuVGU6RSSYaS4ZFzCzipjVOkW9GH6CkzqIz4xGHnF3YS4qxuFimERIoixjdbfiaSor2XDQUfcxQAv63GYU0xOK7xyMCiK639CFqRYxLlGxcbjzwmnA8WipBlTi8HwqgmoaoN795LLliIva9uY41MWsQZubpcbwIRMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGEWMtgZ8054rHgHUqOghxdNx_kKvGhXweayA720cMJc_6h8U-uHx3UbzIPs9UsF8bnGJoDi20Oxpfr1rS4gh-LavA6GKAWbECqpwTWoD7rQDOIiu7pxePAJoX4NoD4zIKdH7d6xJtDhvdvPnU8BaF7sNFec4WZch8xKp4juzVMPaY2qHKQ4U89bf3JkV59WM0InW5ic_IBX-Z2IYbrE5KEcavmDGawVMcB86SCO2Cva_W4X7hPztUSjv0pd_7o6voPpXXbdymrJQUlQYT5TVMVzqYd16ICO8M-zYcm765tOuW_cciERBqjihzLoXkXjt5roEkSrIXrbpdTeL8nQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmUPXx0iKhgvNP-a4sBVFhrAvSw7cgl2833NIUIXaNAuWTZIOwtWg5Z5d9Pk_I8N8dAI7xgrsLmiEeRv6HOWaF9IeLZD1HO6qh1eGpuDGjHXraIQv_8LAozaiLzGe7ZYAi8EWb0P_9_j8pfE-PFfYHW8PaI2-rOOmmZUx1w_kQBYoYM-5A8aelvxSXV74uvGSvflDgbjKfoF18J6w-dQWbe5LbGwQiLCMLUVEzgYxneXsMbDnwZLIwGeYUIia-OM4YDj_YxYlSdopEb9fc5g3J70lQUx6FC7_0RxQlkUVb5izBC2giUdLuR_GIO2wYYKk6oGJZ-yQO_oS6AGixnESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D356DfrBjxu-fe15RdbSrf5sk4JrQWdfnktUbcM7kXkkgZbAWb5dAGQuqbkw3VTbYMbKJdafDXZkWnZwptR2EZSGlvoMxFJue46ZJCeyC9yoNOQ3zcUnVxc6JlcEYXh8bQohQ9s8GDJ-ULlinZDXDitFDCOba2sVG3frMmK1Zsxu4vNkvSSZtjGZpWLADk8ol6QY871BMkt9L6BwQsCxKzd7iUmdchRezrGFbMuCR65cc0S92A7xhO2ND1ZlTU-HbTjqv5MAN6IyMFMw1GGn5gbLaCw_hbvRx7lKQd-vBAL3IMpLZI11AMlkr8Bfvi019TTwUY3lOMp9xg7-WLfF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adiHrjmxbOVcdl-NSwNOCoR32RjDiMs-jBNcIXlc9D7vvABBx0UYwa5LYugQTp82HMZedE7Pe0GSbQnqvAtOvQ_DtDvsmP28yqS0S0RpoQSYLLSEi-mH_yeX0Lm4pyNq7GLfqnjpIXlTePM9BM_iNpSY3pkoV8lpjj3p3VaEV_gEXxMsSCjz0rhfl8Ctf_8bJ44y4UerEZXjykiuwR5zfW7F7D3DwaBvTQ6QCT8eLmSAmy0IjxOicbK2HrSKWxFpyuq_W_Qa11-hJfzYxlBit8BKbBEv9F4rcJ4_DEkfPgHpo_7eySD5JFGkPHfkfheXwAhnk1wkuu9_D8GmSFjrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSK5rT8PDCPNoEmxfAzdDKpkaryt-2PzKTSlF_tkIQNZio2Q0yRLjQKKp4fAkjle60QQBYpzrUTJ58ZFeuwn-kX9786J6Jog7gZEM-y7J1PeNGZenfytQZrVn_Ek9XVkCjMXJBVhcV77umG1P-3zmKMLKp5iNkuat2XB1UNwuS1WcQrRbybdY0vBJd585SgyGJZr5royQIhvYjbJ0dcDPNOxKosl6hgl9viAbIiiHzZHFd6Q3LCaXmo0YfpsBz2wEUcG4d906icoDkOKE0CnVG6IWerMci7iP0jSfI6BGCBzBFvAv1hXDSLEM0kyTuu5WpakxaQ1szukM7ZfDv0SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTBKtUloKdBtxGWKn_cM5J-qOXB1Vs8fsvo5IESAqdVhpMQY_f9TjOiKu45dRcZaoiRubumcqrFoUsQnIVASKdFbRcuu3Wtrny8fdCq-zfWMT3y3gp4BckTopbFsmc4ajnVMsXeTvPora5a5uEqcU6it-YFrr1KKK11be59XjOFJxY923tnXcB9QnXwcZ5alTfnaoRcXFRynm2RbAGS7yhGvdeWL_TTenJ5QioBBezUd6xizTkH8sdZYesBX1S0o_Yv99wPlms7xHFr-SxdlfkWm-P09vSbZnLdoVjUD7SV8prz2-uo0oS-mhMGJCaGpCIypqm4ld6puiBfBfnBSgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE0_kpAyX-0VlFZH9G8_xTXVyxCAeMiUPslhAUQxYog_pWoRmil0B8SkvHdTw-Pw91wMSJ1KyJDPaNWkex09vrY1FCHF5XYG3_lDWwuvlKH-mDmCGFPPJahxayBsNyGHf_eB7Zb6IWFBW2E11H5gRDvqGE3z6WExhPISvWnDAimbATnTlBEbkbJcvBsYkr_79itUuYB3QRLsZXaRh_WFBHb3MQx2jDZ8sa_fT3HwjO_wQ6HY3Ohj-sOAT9r5HB4lWW3L0Tp3JKdVFcBFoRY9_-KbmQPKv0DKeEu9OzBF60dDCou6Qn2B1cr0MdTrig5li-cOAflXBhiLLLAtvHRVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF6gJKPQ5le6S9AYAvX4Jd8A6mVkZXDFVE3yAbXgzjTf-rrrWcS9kbGqOU4t2427IMGmXJyPXQ69WwVlcJVvT33YJobPKa38JRSDHjGQVvx3qdpG1HQkKdUWs1RUovdkvbY6X9i7ZHq9vFTGo-qGDoQXZnx88-JW2BtrZMkQRlaFarepnhE15PoDHSSgTg0lOkrgraSlukcAeE6puzKeID_E_GPcd-tUt8akZUNJD0di2UfUMxWZFBrLthZziYRoj6JI4LO-q_-IooYlIDXLWwEXAgL_moHn6Hby86WElFXHR8FvgN646U11xKlv4d5z4QyZ5u4p6g8MpO3axY9ijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8JmbuyclesmmTDJd0i7Th6GBbGY0F13a9iTa8kgSAgRTcq2jYJop8yqlMrS2Wty_qQq6XCqpeCaacak9ZigzoYkG0c1d-rugkTEMvBM6m805YCpZRMNKH-V6YEvBi1D_QGRjDb8mBIbdpwh4yUj0kIu6FAZ8xllxxI7w013RJvNcDhL90WL6Nyr-H_7h3dEneypRPRNhEy_20e2RK3gFr2IN7XsyGt7dnB0aIU2r4Ss4gxapFm6uCr0Y6HTVrLvQ7sLxim4giLrMyff9XCrJ6KRslQXaBaDv3Xgza-qxnk6W_5JfDDVlgFat9nV0dwdzlDH5M75BI4EqEqdGLtfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJYDFRfYfUubrf7oaV5_jDdunHiL6pFBrmXAAz91qlwAAeiiddvZyjsh9Vszq0LWVEutGbDcFGtcczVIoDk-oiCXHIUsSDXS-QGMyyabUA34SsllYqVCcqf5CF7s5JPVW-SvhnNXsj1skDEBUdmL7Jq-IidqXx3FL5tqxldUz5NOmU_62diL31Z3k7xF2kCL5XJ8b_ilvgDFAB4ZXAhlUjB3i3sAr3jhOGBhI5krHULB1F3sux3LDOP4mkEC244BjH1vKj1t0RfA7PVpOCXaFVFoQKTspsmNDDY0HN0177mkPIZCimjVWPTAA6_4yIHTs25q8jQIeC7JGaMFBq0htw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP7An1s7NRi6vVvgAdCO_3Se0UDgzNKbpquHfAc-DWRLfReIorNcf1VyHly4Ug3LuxUU1HK5lyQz1tM6PxEtOp7GqvhiL8d0fl_j3BEtQIKzcLmbIYWV-rFCF6-VPKe95t3kjUYSzr49IuNXL_QUcvzjVvWGer7JGFnCPWsUc7ip4d1a0QKbAHWm6uJODMbNrsmFyomr9TQdcL9tg3Zh6V3F_I4M3aijJpNH52GSaYn9Bm0eGALP2WfrAbVh0mkksrkHnJzn780Fq880dj4Zcab9Br7iV5A1vm6WkvTEHd4prSTUnj2nMoIAxShl7XdHnbch3NXevZhKRkJGPDic3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26422">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای شرطبندی هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
g2
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26422" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5l9OvpWtZTh5vIqAYvAUXepGvQfY3kiFQEs2MW8QnQ0Dx8Q7FXp7N2t8RMgjDemtNYmJQYGHEfNvzCSUV-VidOSEKGYQNDorb6DxBXD_fS_uJp-ZbZrDCN0AX5r32RgA7IEO5AzNZVcvicokmMnbcZtCLh1osvw27C30dg-FaweBG0nC0oZx5qUGFfhUZhYMTycCvkQI7TxpwMQ7hgKE_MmnJQ2BiYMZhV4c3lMjWacwiq-Zy1iLlU_sOByON8vqxcphcAjU-HIwrphefKU4FDIP8jeTGRssB16lV0Q1XjXJ4Eu-vIj2l63sKnola7BaUfdW-80u6sHiN3dR6REMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5r3JqBx383ilFjfwiGncwOijIDK_AFvfowYOQJ8FxADRT1e9pKejaStSRXfaCAQO_2cTye8Y4Eo2YKDFmDZEjtZnp_PkjtU3cEwewDdB9GCW7EjWgCXqs8zLTAIbd8Pfhc0Q5G0pkk-4A_xwSX32mG5JAwaO8p48rtK7MKmnpPmQktjBFdczBpeHhO5QJPBjnGruySQQDokTjGr4t7ehSa0vHZ2Fb85RbWl9qs5-4Rmb1H0Y9V_9bnUBmF9aQ1kYMQOYXlFAYU7-lu_XhA4HIOWlJwm6V5gWvtuuIt_p19chExnwT6JttmQqHzdMVNCL_1J1BN2WacUmfuxdrtBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbyhI9-Tn7p-IlxbP4DcL3z-j_1up07y3z_rrxDlCXi7G-tdFW938dfI9uLSavCE_iNzMDN1_iGOnObcxWIppOAzSucPvvluNK81U2ca73YZkEnZA8kk7gPS12gx94kRfh8d6kpWKaNwZ71hAdpr-865TWQT-DryvQeHLNW71HxsQJc_78cRrfdBgdz0cAPx93Pu9nPSZiVQ-mtzl5RWwtyD0oSULH1sbrYW3Q0m4uiA3FyxJptu_HHzpBoLVe15z5suVRlCTF3uIwLZsycHuCRMCbgOl4bbSsopWlGc0dVfEFc5LM0Tk_ajjalJwO22ZlWxJT3ti5Q4hhK7WZnP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkOSqd5HRi8I80ClCUcKDJ39m-49i4T6CS4UfEp5b9dfzntMD5AXyjie5RsKV8LVSoamsf8Rllhi7vpKQeFUmBgWoXSa-lsi6079m6Mgpx5L5btl93_uF4OE3xX0TAMXpurvmFCXsn8duQxQ3lOPa7TgLScAzqLJDkmwcujvxv0C_LkVUkDe8DvFVbRlIqIWrbfq10GhuFT3AaYpoJ46gWLuF8PgkaT7pAgTZVpBpRguEl8jPNaGH4Om3KjPgmWUyn3QwZeePvqP1-WnownRUzEDAFHzH-GWeUix2X4IZW9CgK1jt2c_2tRzbaOH0LSskzbhY5yEo6BpmOlaW0Hmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoOb9gS_DojrErMGlHwiSzi7WN9zs31oQyWVbhN5NmOBt3wk-kQCjeodQf5XHE0r3b4nnC3VhGWyB9U4yxYpJcKDBXwdyvNCXIA1f1Mi9rEuVSJdBSefV5lKpXATo9AAEv54iynJ5Y3j3j0vi5Yjzwfmj2Zq-cVOolMde3zOfr2cvt1mV5Nw75ujrwTE1TXtGvHBgpq6Da2Jp0F3wE_rkt_NBjynDZ8thN4FGiAryYeD07arRU62OABvFLZlaIvfWd_iz15TGdo1OirjCGEWj1p0027B-nNmPeRdUcQfucqT1uWKtGDad5vtc7jIXwLMr50gCVwDZi2FlE4Y6PtDyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiXDbJl3q8vE5-AuA1PeDBlzYFt-VB52nXiPa5uPZsiRKYwO5a2EtE5m6W41KzgKLPoh4fP9DfYk0rUDtH2dsRGBpKo7rCiB7-FBtEelajYFL4teBuSGBAomBB8Koni8xAEB3rUDF3dpnP1LdqZfiqpZTmndqP1ovcWpSILF0pR19ihrEiSK0rteQQ90k4mi_ZmB_5keHMMEBXUdVwbgSzjmhlWHCJgBkV7P9JQjw1k-zTiMx1yKlyEEH08i5VhZ9xO9U9_5ox3OpdEBTPve4O6ayMj3KAjHbgF17QKFX0kuTgfYTcZcTGSDdRAHZhJzMgmC3I6E_CH3v15iQ7OvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7TxkDVpG3YWzT1YD-YL4gt9tBMCTTb5a-HYPkrQX00WZpsHUUiPOx5sNCVhH-W0caMLQ6BmV_ITQhZ9KR5CZCGSDjKzvrPKbH1AMEuWyFmug525KNULYVrbiGq-QYv06ZezA1fj4YNU4ZZqILB3f39jCO2TVtd_3ib171nLQlvAuAAJcBIbgphPwgUjIgVicD2VmChq2SkKyyY1fo-IUJxyj-MIPHwxCx__HTp9Wo8G19YOXM3DtvrxxdznIBzoQ3-wUGyGQeZopfuANabsrVBUG8eyrZJy6PqnZFtOdw1pWlbK8dBH_YTLEk9sAJ1iMrAeZ_nlEnWkxCFschmPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEeHMwItu2SfLOdZFenNQ0sOxxc1VJVne_ejn9B9GMKbndXfncTGrjwYCIJrRqroI07tByjSUcZClmH0mjmxTURbbySL-e0xa9Hi4fxC_ikJAosdWDgcFrov61u6GOi7F38DRM6DXnyXOzjEd7xOAw7HWq34c-sdjss99ScHz3rGmenf-iR-ySzvm-mUvn00SvBCPXWLDBbsDJKEhZDNgY2VQtcjgmK8n1jvsUp4MUkZbnq9hy39S24jNoIAQVZm5MdKnmtlVg_h0vfkz93Cln0q8KlB5nQkLkeE_ELD8vwLhgIYwGZf6jY8W-KHqIG3j6rHjLFZLyJJPqMMZze6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txUhSa2dPIAziZgGGkv9Z-r_LrB7iJ68LFG-g4Fi-vNPaMO72O64lfRwC6j508sbEzF9nnGG8ISZl6lt6k1iKZ8eBJXAURUvriO9TGl3hqJQxF33mZ6Ffu9eSsQjkuvU73sX2CmIYR3rwygF60thQjDb8p6PqJvv_ntvTuhgIbDel5fA6XcpGrn01F_CNWzWEpThUpOSkZMqIPY2WuRgRt0F0e-1o-WGogKVliyyRCfdXeWO49iaVN461Brj2RiKJP-HLS1hoGZt8QECclyvMLdIpOJuZ5NrbWuO0QVf4gJu10eSWrpCLTgwzHPD4WMt_eiziFGzgJWoInSReNBejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEV5nc1fv7n6Bf-D1u207CKe9GCYxV9Zo3O1XR6nJelEnBaCWrXqpKHH7HsukiUrerSxftAHm21CL1OHmVZwfhG8dhaXC0285cBKCU0NVzhKDqWs9VkeXB9aQDHFUtKzXulMQz-Li68JoVPlMfI4LqttiXJxkiU9F8BSieZfFBH_ufx3fugJk3x-ciu6ZqahrCbKPIhaJgfEPXjwKdqOeol-LBzZ7ulRwTHKl_G4DjrpaXTpBiRa2OMOfQCGkS3y7mJJ06JkTQw-DQl_RSDPuTSK45c-1JW4IYfm4EvQBgHnNQTS7EFia4OORifDo9o_qgrs7Yz4S4OsJUSYkrH9-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVCQ_Pq0znRmnslyZpF7EJvI3Ob0z-BmNjAJdYt6vQxse98y0kX1t37WyTCCwcDgLmnbsFXxtNgaRw0tWwoG0RvYWWn6dXT2Cky6NgoNkjR0XhkDWD4EORO0xAhOeYlbvZ62uE5Ssblz2xNmTRnMcDtr4RGyLFLKegsykxYO23zyacVfq7r3YdcshbVX2TGWP8g4FdXhlvSb4P6qx859vn38UNYfjZ2NDO_VTkVH5YPZY5Z5C0WiD2ArW8KOpYb6JbV1BS1Ga5kCyX508mva9jpNnSVDjnwfhpYZvuxnLRqoLL1YjfU-RkXiWU3obFGFLtfTFJBYAOADgfXRK4LWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E40g4655fHjjugWCuwTiZWy5sIALMM8XYZEdQg7TsrI6q3Jc5JTSNEIwtbrVWgGmtKJ0cHQDHjLOVz-oLZ6APY6x20ZT9vKgMvvQC7sQG_ISYf9a5dvj1-2-IttQTACWmD_3fCAP8PMkKeWd9ZEa_w-JoGWHWEEwnIvJHeQew9HjX1_erznxNPvZp1OwHTTNgLGHtM-sfP6AXwK7yneklMH7MDOWtciwJXCtzllJJ8ptr4mk7_twW9RpEKjI_HjkbDT-66kYbktQLchbEI2uPlzB6GDmGKa8CFJ6voF6B8e9dizV3R72Cp5H6vVBFtnWtwMjcLM435G4me4h23SiHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT8U6zN-_4munaN1uAl1VCAy51AJP_3-USsnwo1TlbtPtHsD9fKxt0r0d4A-qTBTP0kdiZFAUIR1pWInja5muDS3LqI1YaQKbmrf_nIzcxgX70wA7GGC93MK04E99HPw6aMJdS2LYoJWvyHtbS9mfFO3KRd1nRGms3kWXZJnpMJK3gFWgXYFkCdqMi1qZniBHbhEcJIkyUIXiDrtlTvRxAt-W9aep6aaPwO4v65tiQHYL3vP60LcnFDcd22ia5MWvLHhjdTIGDJTHkMr7NBGWMHE4oApIKkWr0OjbjcCg-IokrchezjQQNV195Sp4W6WUbNDELkVJa0_dMmf8acbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj2KPsec5ukmjxLHlh93UiTR5GEsr5pZeNMvIxxo9BIwPboywY1enhk0Qk-CQkOdq6tMmy6QB4ql8LdwyebtSB5_HwMFCapZ0Isa_RwlQjTz8qIMhLNAj3PHU9usegKXfMg2N9ox7C1OUq5ItkXMQ2QPFUglotQGzz5c2vST-6GL76NLqMlNWeZper2YD6AQv57DHItJRpWgfgJUk0pCwRDd0EyoY2qvzWRu96Sor3M2wsGKcHHKCN6U0yzo8N-9WLjGlwPwsdKIDz0Djo-GLa4po6SLrE2Unl6dVFHEDZ2Ty60fxjxt-dgNuzj9wjDdlQk3HFjIdE9M02_57tJGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=YNZ8z-21gnf5_Yg-zcGH80fCrUdgt4lHxuyousxY-cAzjgvGAxltxWk3mxngRgZlzRaAi17EBn0PPTZjoGjOYmMwkkxlKsk46FfzF2hvhOLnaGkIOI_0OcsxS67S_Yb_-f0ItI4_lCTkCWTzKlmjbBHT1oGdrsBLZoyLshF-RmgHiB5A9Mz_uqCpriT0beOb2kTgI46UESiuZF46E-UVSJoNDlfzkKZp0FEZKOp8NiSphygy7pcU00Y8-5_wntSBoKrGijk2CHtsuQCVIYA3he_6dkTJnoBz4Jg8nnPTrTE779wg-W-ZRlvcifsJYivPJglc3ieyeQ3sr0Ri-N1lqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=YNZ8z-21gnf5_Yg-zcGH80fCrUdgt4lHxuyousxY-cAzjgvGAxltxWk3mxngRgZlzRaAi17EBn0PPTZjoGjOYmMwkkxlKsk46FfzF2hvhOLnaGkIOI_0OcsxS67S_Yb_-f0ItI4_lCTkCWTzKlmjbBHT1oGdrsBLZoyLshF-RmgHiB5A9Mz_uqCpriT0beOb2kTgI46UESiuZF46E-UVSJoNDlfzkKZp0FEZKOp8NiSphygy7pcU00Y8-5_wntSBoKrGijk2CHtsuQCVIYA3he_6dkTJnoBz4Jg8nnPTrTE779wg-W-ZRlvcifsJYivPJglc3ieyeQ3sr0Ri-N1lqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1OkavtcgZuxMzzjPXIjhx7RUXK3MMf1x2bFBqg5bq1PYuOUAIr0zXHTQI6gPyY-PuhKgjVA3DV42rc8Ia8CeZT0ExtJho-L9UhQ7xFahKlyFvhJnypReohSKfkDEVl5y3JlN-3dchZ5RZXOu52Il9VqN_4bZWA5AiPKPU9oE5AuEwouaAvM6Qd6d8kfe182q5QcN4La8M-rl1yFOqKkpx67F0bgRxeny-NNqPbnxAP7BZMLS7I-_quZvBNAaB3T8BKwwBQEbxY20LBMOu0b6L91Zz81DzAp9uQT6qfKAZWvF6ro7qMdb1Mk6OeJ9t0cj9LizUeRZpC9yCGnNu1jjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIme_mAvwGhj0X6lLGDCVduP-2mTokFKM-7VI4FluedpBXpf11rzzbOYO3mnHGiyHdCrkLFf9U-luNL98lSe0dg0N6xT1RzF97DIrwGFI_9DCg3siLcWLJUmMTDBGjcbg5bX9pXqPdtv7NxqIVDm2ZrDXdY92yaTa53ddCuFvEXEbjmfFvepaPEyUaPqmjp9rtHr161q3A2_7byx-FiphNSNYQi83PAYSwaFf6IA_8_V4aRv6yCDrhjGPfp0n2IosROGZwohh53cOiVe1Wp65_6wQT9m-Jm1xro5Jhl5zR7P8rtRo6Y3lqlD5MKZKQydTHkVQ4bijW9i8MB7A7XC2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFeZECI18TXggwbb5AE_-VxVCarucB3dv9dTWRa3DTPMY6_9diDxCp-tauBmP_sH2eOayQ1_Ms_xGy35BEYEMqzjCI-P87P0OcSTfW3U-7xlAp426QOYkfj-XpT3_a4sSk964u9zXc0fhcakIGRCk5vRmRvRU8ex1IBo5tTtZzYVO08zfjukMV7IYxwmFrHQiiyfVZathfxepY6zIW4W5zM4XfVgsMrvZZWUi11nuSJus4vWwh5HH3sZ9hG76ulACixKKew94kUhUnAMFhlLhHna-b1aZ0p8BWb7pJToJVDnutYIkQm2Dk28ZqF-0OnD55UzxLb6W4MdmOd7LeRd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=nupw3sJX5d2Pmc72cd3MuW3zymqJnDI8_ssg5-bG4bOJCYEstce2ZQVaoZeyNSV843mdud7z0GVSM9Gzpdt5P7426L_aP2NU9GTO5WFV9bGVKBeZR914D0_lDmbu7zhX7y57LwQW9BWTygZjR2wkWaVEo2hC-u1Tzl_2yhb9QC6LeTqDizWiGBSdDXVNFJ0YrZSg7ay9rSagYJnkbYY5yo3G6Celb0lM7utktQrbCmT8_1lRZwCqKfVSezRggrKCW_8CfwthyEjLo2PkbHQ4XEVbjZ1_6mIR8lOTZr7rXlg2TQYPXbGwjD5wdL49BTqeN5C3ymvmbbfxDjvPbYfiqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=nupw3sJX5d2Pmc72cd3MuW3zymqJnDI8_ssg5-bG4bOJCYEstce2ZQVaoZeyNSV843mdud7z0GVSM9Gzpdt5P7426L_aP2NU9GTO5WFV9bGVKBeZR914D0_lDmbu7zhX7y57LwQW9BWTygZjR2wkWaVEo2hC-u1Tzl_2yhb9QC6LeTqDizWiGBSdDXVNFJ0YrZSg7ay9rSagYJnkbYY5yo3G6Celb0lM7utktQrbCmT8_1lRZwCqKfVSezRggrKCW_8CfwthyEjLo2PkbHQ4XEVbjZ1_6mIR8lOTZr7rXlg2TQYPXbGwjD5wdL49BTqeN5C3ymvmbbfxDjvPbYfiqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt6RZdNj22xl6bGSa_xkN0L3Wr9V_tWS5Wp7kzJugDtTb2QUBOg7rdriOIYlWx7ba8eA0ogn-30ZHowCxD9hJmjwzVZcqSBgXshIiohooca7lD89O-jnHMheZMRUrecFLtMqd-mTJpy8D7vXI-a1LyYN5dFfqYkwhWjRFCTqKSAjEX1DZl7UYcbbNG8CbBAJQlRuCRNX5QxGwYoo81H47n_Wrj_L2vrWyvIZNlaDzKuHDZDFQoIsvg6EzGQWV_d-zNUEZZxjcfYdjmqZdl42yvRZynDgoV4TnuCQKHD-SSojsd2sXHRbOOhrBgvj2X_6igNAEHxKTozTX1SE2CMemw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neHKG7D2rCyX3QxjHI1UKXffblERJLA2jEm4HlXb4pn0WXIVOl1bKzGbR_GNvRUbyosheAb17XgtY-w-STSMOMRcWf4YeI8sTjJ4RpWLehCK1wqI1H2hbpzH8TF5QDWCQxi8xAOckJUPq6wW39UO4AxnJBU9UuXtIOr-ct1CrSya9K9XwMK8d2Jv-WQfanryuCzpXlV8q0bMHRww7HFnQOIeVsm01Vn_e2pcs-FIX3zany-c7sCMdAhdvfkdmFeWj2yJmGVNV9Aonz7n6_DLSCuTP2IX7jd6mjKHrr1KPT6bEcJlKUeNFx0rr_2tnv8KerrZvzEVwd0sal3OHtwdecyY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neHKG7D2rCyX3QxjHI1UKXffblERJLA2jEm4HlXb4pn0WXIVOl1bKzGbR_GNvRUbyosheAb17XgtY-w-STSMOMRcWf4YeI8sTjJ4RpWLehCK1wqI1H2hbpzH8TF5QDWCQxi8xAOckJUPq6wW39UO4AxnJBU9UuXtIOr-ct1CrSya9K9XwMK8d2Jv-WQfanryuCzpXlV8q0bMHRww7HFnQOIeVsm01Vn_e2pcs-FIX3zany-c7sCMdAhdvfkdmFeWj2yJmGVNV9Aonz7n6_DLSCuTP2IX7jd6mjKHrr1KPT6bEcJlKUeNFx0rr_2tnv8KerrZvzEVwd0sal3OHtwdecyY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xuf94N4FrvYke_BWmi3pYH17MAH3N4bb0mhNp6njZR5N_NydbzAoPQY0_UmwiiQj4_SBVdxFScgUvOcvjBNcd2Hfw1N124Zf0fu1XQGKtTCk9ZmTBgU9mffEI8Ysj-1WVhzy9-_St5MRkykW4N4ZMyJt0yjQAg4UpcjFET9WnUvSDhgmnJQYeuOmDAKNrQ1bwSxWQ12vt4keF4O59bp9WKFYJD-epkqi8EpXGPKQM3neGuMS3geXj3kYdlPaJn8bkbWKwEPIEWwiPIRidGN93lHEvx3QGOsMaiHAwYOYQY9G_6eIrVYtLnBdFHRrjWFRSzHlhOWk18Z7ypXcDqg18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJ9ZYh9vBhxwQotEk7G-Oo3FZvLlAwUaSzoAPL1YrIwAi7Kt-dQNKy06zBVN7diql51sT42WxENt-BGDBKI3_4RCVqdZDAGsuslnW87JRaOfhAobPqguM37WvDQkRKi37VBwhPf45YYfPwIQPbT3G3TOV2Q3AvPzsM6ws18Rz5_1C3avsoMUr3WGXTZ0s0gHXrUUFO-D6IiOwzHdcPSqZYO0_hqM57UEfaeuEBUKZzUOm8LqSM8UoaMxqXP19kVem-y7PTJEWlKzYOreSvcUy4A4WwCUOnjApG1sNX-W2AwHfyazgoQ4h4SXpxxVmN4bYzHY-EtJ4T4YYZoP8M3GWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzFDWYdT3T1siHUwLrFHAP8d_UmkT7WjWu304W05E10M4u2oBTRAB0AD8BjLxNXlRCLbPU0XwGO_u8lGM-JRjOKt6ww5IbTkPt2oJzWLl4cY39U112xkVghQ-X8qg84hxflrACUILAgv3qngOuQY9xNQJqjfeR635loRgx9Iy1xX7BjUrWc4NIFEmv4Onlf3Cd4q49wlT16nGL6cm17n8a-Fh9-tBQecgC8lUq9T65F4QYPB89EELR4pvzuxln3qze8Yb9KA-mmSQKKMgHvFKueR7keW8YbO0JCW1t_aD7lqxTmzHwZU3jbUhltP8QCZD0oVg2cDdKz3Uy4fyo3dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-bJ_1utvXCaf0G9sjrnhIvhzIQEMrVVt5ILu5N-vkl3QcVWDn2lvjopFo8O-HtTnHtpMs0-ZTpFXi2dl0efnMLVHSAF0WwWDGqC73XYy-7kcsche3IkA0esjApicCBVwQ40Ibrk0_Wwgr2NBbjVVeRBTFo4w4Lo_CHd-zQ4T3-C78L4QhtNz3e83RNTVYTQ7jhmZlcIIlUY2Eiekd0j09CnDgkquGhBUzvO0wt4kPdphczwOhoC3jSis0ZSqtaexULUw2KQzl9WcDzdmn6vNSZEXx4fBcKtehYBujYHwgAjG8bPxlq8urtBRkzOD1gI9yP8UPD4T_NVy2yyPLXndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFfVg0aEuKEFtX-zf5WW-uoitS4IFX0zkkrkrBQl1HRKqx_0VckwkQud07xyD-MnQvuluoHdjth8h8_YKNQ2N-pjZHwh7PsemSr4TB8VnU1ia_dIdknrrfBknXDIsK4c5yBGteAzck_qYj2X2I5W1XLCBEjeE1IZxDYFlX4XutEBB9ux2wue-yen-H3jK2dMPhi-X36z-_HpSkR2a_B7icM6cQgva9HngCovYUD4L8tHPloutpnkJPnFZQbXlbhQKYHrnSUfZt4-1EhFxLy1SN8ksjtBbO2z7-O0n6v8P74nQ70FypXj2AmDO8lpxWkKP8UiOqDeA_kXGMLW16zsyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPKTV3ETa5YY3XUAj9eYS95lSpzEMybGAnRWTHsr5J6Hx8F4Fh2UdQkf9q-qHF5_neJswCq6f_piPZkkMOM-uzm5CSYUTTLXwsqUQ3mj0e0y3knQq4XePlURcZmLta9p5cLweb98CDZrRyuu_8AWm30mvJ1cUu_AYiFJOmYDoYoMyUV-P7FHJcGPwO51qL11SeZLlnGxTySdD-sqjm06Ql7dJrmYe0XYL01LFCObZSrwPjavPpmn2lBMj6YeBnVY1MSiUtoMeWRYyJTpRXt3h-usNkw2JjgBg-dIvYqrUkN8GUg4AWxOLL6dhPo4-VDs05yV29xZdh9QzlwILU30bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfqxZitD53tDS778DuHGuduB4w3CCu0g0cckKNcvXIi0OpHY1dmUf_Fh8F-sZWhahM4ZS0GzO3P3qn663lbAt3_Khnmy9__5XrcXkRe9QL9qehHXMWRq9YSwbQXGXSA-jk4LSpgJ8UZ72ySx9GRV5DahqVGoPF6KytE-bxmU7bxEgXoz6nJuZU2Tgl1GJJo612nDAXz3HLni0q30b6Q19ZOnataYZP9mslduHMQSA9widVJ2qED1pwdUuBSh2jiFHPbt6Ek_drz8hwAizg89pukzTfGHur0JNIpXkXvPrbdd672BoO5Jj66jKgBV4Yv-lN77SVUb_xEjIOjsGHyjfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A46XGmwGuN82TaSn8sLcIyVEdWMHy2e-tQPwpc03Jol_wUJiNNr06FP7Y6kFn1-uQ9BnQyH5yR7o_gbvyMgbM8fL-isNyVseEeCisSxCZ6vc6g0vf0P6-kDtHrWjO4fAU_zGynkl7uFoYzfOIjbNKzmVYlinCGibIbVbeSLfq9Iz20b8nybkjOzKcBmS-uKyta0rKPF0jYHeQfxCwAMzkn3WovnBWkU2sw5RuSPuaSS5AGrpkXHF946h4bhX5CKDJ57VzCTAlYqNB-ZSIKLK18MNJTTL1Q9BQE-u2Un-FtWrCmnJAYvzVKaIuRB3OlXGSBK4mh_BI7ICJx3CMISxPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMcVWgJgIp3gtFu0RQTd1QH9BUR3lPwfURe39RKAu5glOi8AQzMJJ3JHjt4SKiGZsKYD7bYHwPGoJcSERn7ibf_o_lGCFJjnLU80nI9_sSOFmvG1P2mabk04MDe96jEISzP_uoOEbAUd7J_OrhaajrhBHMC5E-w-9J2V8Xe_ITGVABpRxlsVfx5CFcv0_m5gKqpijvXEwMT5WkS_06C4asGc4ugF-pxdQstMFdf4FJwokCsnpwhu6OVoqkUq8q-EiLYKmaT_mhc3LXctv6h-ez2eNKhEH-uHb8kkPlxX01212qC-xLH82QHaLBR9RI3ytHfHjuwJW0Yi17k43qjKpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SjkCvWPizjyMyfUGrmv_cs_vq6KnX2mecnZ4LqH3X-Lgc8npBMI-GVDhM_99b_eBsoJsUuaKqdJN0wfb2-yGjCaPD2Whb_VQjBXst_g9Xx0f5kO5v7lk8mKw7wEVW-XXOckWYGd63S7zOM97HFJ9Klu_HaTd5or-7Ffv91G9JWEDOoffgfEnb_ahexMJQ38zlJKqCE52OAUGwJjFJCma7_YN-CF-kwh-PEan_8DKgt75q0mMsKn30d5VXY3VFVy1r-OeGxkLXXuSkZZks20mttvq-oof1F1qhcw5UKgWWNcKbk7vcMPZALCJy47pAtfIsubl_EyOssb82ZApBM2p2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_v06eKy_K4h00_awGGOt8xLUjw1yH8JTqsSpM45_6Jnwe2k13rBPSEpOfMcir8SdGGnF5cMkQmKgLuUPaWFXN66s1Nd11RqZLyuuKH-F2BKEkv2ONBdGEtlxAysoc5803yIvOpA2l8pvA4dAcsbh2p_LJC9OFisMuhLnqfvTGnT1O7WmxSHRw93XUrLg8fLPFqVyhw79Z7fP6eEQCWm9h38MuZUKKf3QuZ2I4EJauX3n269XVEsnc3mRFov0vVq87m9VnZqN5q2FsgxDD1pjNVhVcYcbeT2f1xZHpNFDIGq6v07qA-cD4v8uZsg88Virj8AwPZT0j4D_w4WF9S36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pza1pWPA8nUeOXc4y-p0qJZw-Ws606LNotqqpDZiIzjACQHQTyik08SUccpWSiJskRqcqFq0agSaYSkFv_VNVybVoUYRt56dZY1Ic4yRsvp3fzvA3xTDBr8tacEr9papSzUDQj4RoVIyxtJg7mNeVWhU8qX4ojJTFXIPXRQ0RpyKKY2EOSKOkOLOBl0eOBAOSz-Bwb-_oGC17lcazt3_hUCE2i5exhlD-yFz3v3UxmRY0EJd4TBr2xnIZkaw9lxKiTKwbVLmuVenj6iI_1oVT9pvGDWQXPYTf0dAKOcmO1O3BIxP0H8vXGU92P6VF4NRTRUlY4NPCY5aYmaqjuVnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9yGtv1XJPPWWCmWme0FxqmK8ORLt6xX2du59QsBhQ70lihgtqbokyfhXaP_Teh9LglL1PcMG41JasHXXSRXKmXUGHDYIS5pONSYH-m_pnyI5_i_AuG61ezoHS5Mhbj4PP7cjhCReH40pnX0GPcUuL5kSMtJUrJHb_i6CdRN8uFka0u_Gno-bjSI6WKHnnHwXcxHM-TKQCROjPj05XWhcWd4DkMCCEl79_Q2GqaoUTf3IP87zfS2tTEWY0_Fr7Q59CPt9WONcOqtHHW4vNKVqSccy6r8kKKre1FDqlDC1W5bNQ-uDfRecGI1h6rbf5QbcH_PzyBUFZQuYnVpr8wuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH49cbxRfV8Q36fsh_ckIWShMkxCMRD7DsP_afWMsjuToJxsPGDAhIdn27ad6Qv4trnV1eCiE-pLFSk_srGH8XgjJddiFY6pVbhciVdtPCexXZqLVRrZAhChrS-K-Irlg6STC-YHVhjEUgivA9bzhUc07nmnfReSg7WkZ2w-axHDKVIoHWbCFs5FPM0S-5WxECMC-z4u46EzloTP4nGHx769_rfuLHnn-urYv0uW_-ojO8313p6TZGH_K8ebttPOWAn2S7iT8Kt0eglK2uH3yE_EI7zpjnfzTy7BVTR8wp3fXGp8QYOOYYt8Nn59TTxvYgoKxckNGdN45R03S0Iycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=p5BMkxBUwUIQY8YdoGJoLjSpHtsc8HpJvnhDhoN2v1jQHUd7EiaBTqD_J3Xqx7pRIKKsbx85TnlrHcHTPhBbdYDCN5VbWK1xpZ_VtzF-ILMuLR6vUtAx_5kx6wjuO4PKgbeugzGy4zmOr5nHxb28eKtaM6M28djFJdDVax-REUf4cMrdmXxLD_Rbeer5Sa2Ldn1aQQIe3bKVKlA4ZkLh2R7uzlgSs0_f13FhPfSsnnRafxbFhxf4wXMSrUDrCFC_epYLvLKWciO9bl2_lEDnzLLD1sXkDIcdOXgPCOORXd9W2J2emrf6ZuTOPbBh6y1T2fCLiaHIrKwE7TAF_s6E9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=p5BMkxBUwUIQY8YdoGJoLjSpHtsc8HpJvnhDhoN2v1jQHUd7EiaBTqD_J3Xqx7pRIKKsbx85TnlrHcHTPhBbdYDCN5VbWK1xpZ_VtzF-ILMuLR6vUtAx_5kx6wjuO4PKgbeugzGy4zmOr5nHxb28eKtaM6M28djFJdDVax-REUf4cMrdmXxLD_Rbeer5Sa2Ldn1aQQIe3bKVKlA4ZkLh2R7uzlgSs0_f13FhPfSsnnRafxbFhxf4wXMSrUDrCFC_epYLvLKWciO9bl2_lEDnzLLD1sXkDIcdOXgPCOORXd9W2J2emrf6ZuTOPbBh6y1T2fCLiaHIrKwE7TAF_s6E9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWwTHYWnx2EhP8D-VIAtIRZabwe3EbkWUNnUUEbladLm3lljbB9ThZso3X1xZaEvLIf513PIm4cx2RjoMvYRgiJMjW4uf3m4cQQ_nifIjJMF83t-lPXitK-5iE17PNpTPuSmRYHbjWZwqFhPBvUHa9jZscL3xKyWl4dDTM0UqO-Lp0FENAuvrB6sKCvjShcKTQ3xiS7eOFjG13CwzNBtxWH3Y6a3eXhO1RFNFdK5dYQ8k8TdaX8JutCOAQ5TWNpg_7yxMFz2S3BWhbRJpEMjfpgcnS7a3IrwfLdm1ZK_4ojnC2XtOpVmZAH9VsnCaap-HYpAlOLSoHSReJ2QcFRkXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNbPNRWTV4cG49DnaSdn9armakv4fFssWkZaMu7WteHlL7p3YUp5bZvBxN1IuzjAIa-BWrkmpwkVAmUuxVPLjQ5qwJnVrr8hr4yKgh1LHjelcvVKzZE6vZKzGGqQIUsShhvUnrXVzi6TFPXXEVobb2vLPhoBNa8SS-c_WnGnYG-9ojaJ8oFnfIXdw76P_7bRJMlU1GI5JNGUT4H3HVlQ6k9H3dM48hUiFoOswOqi_plcqz_RxaVa8lvSQqhKggfZv8-IhcEDKxwxODG_xpHgjyIR1UrXMa3Do9dNHrxQ7sQrLjgMDO2ds4u99fAfmLZMV_WIpXbN9o_RCwLtxIJakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4drUTnxPZ-TzZi4Pfjb7x_k8LCR2gvyt3EUuMK6LsLwtIUVzA-V-yVd6qmfM9gamhLWz7YX4Y-LU5qsXjWwisZmiWBldU7HP-jJilBU_3Ngi42zmhK_LKFHMSMekqDPrr-lZv_of_-YlLsq13vMc09f8mbnDHOdK4yDenWq0ViHvYvAOYmwXDg96k-1U1x2blb01WGTS-Ds1Jz4RI_RETS4DC7xjCs2Vf1YdQavCCza-Nvw19ABFbjxKNIzgzWPzJ2pBVRRxe_X55nE2O9qJGJAt3dQmHZOGgIPnDdfWwvxN4wyLRCMEJzaaH1l716XqCv5e_fPS2tv2o-88xqZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPDrLcALhOTjciY7tp12OEPqwvf_QEgoveNWojwOza7e9s1k0AVBn-UJ3F4TxvasQsfFda_XXRmR47vGBghVpXYFpv1SBBe0nsgiqaIDRWppzPWDgpJ904IKFZsPDRALjf5Q_6ebwTCBgeFB-CyRXmXvKIB3E8yCidf2kMq6WmIFhFgFcpY1S35vWV5sPKkMvY5PkF7b-RhYtolCriMHlOvwCZ3emDalTadHBygeB4u8yyaeJRFfwjmkhkeZ0flf-jSd2ccFQ29R4nK_tDKTLpL4NCHFVM5ESg6lR1SBw7_Owsga6gbJXiSrMJdk7qaQLN5LcyUlhizpv2YeyTRXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=en_KrdIAwPCMBMI9j-S_axz1we9msyrZiBhTOURwEOz67mLbzLNX2ZlT90P_-9HDcQVrrs3mkEOGC5v7uTtJYmfx7NWCoCRJvKvQ4qLVbIj9U0QPvbH0Jl265GOjlMLeK_AFIZjybm93MfWLQNu4DI8Sj7NyFIeS70-KfOHzUlSNSMETlPRx-vjGIncPyNjbb6-jdiVIqgHsYvgBONHRxXMzxRZtABeP76fTLuG5nOhICC5uV5bYWhKr1-EypXUs6chmDKlSMHLsILJ46wuSIKN6fvmIYcuxLERkPXXzCeeA07JccSHhCBVJmtz35OGLmoYEqrHjTmdGuInJ-eah1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=en_KrdIAwPCMBMI9j-S_axz1we9msyrZiBhTOURwEOz67mLbzLNX2ZlT90P_-9HDcQVrrs3mkEOGC5v7uTtJYmfx7NWCoCRJvKvQ4qLVbIj9U0QPvbH0Jl265GOjlMLeK_AFIZjybm93MfWLQNu4DI8Sj7NyFIeS70-KfOHzUlSNSMETlPRx-vjGIncPyNjbb6-jdiVIqgHsYvgBONHRxXMzxRZtABeP76fTLuG5nOhICC5uV5bYWhKr1-EypXUs6chmDKlSMHLsILJ46wuSIKN6fvmIYcuxLERkPXXzCeeA07JccSHhCBVJmtz35OGLmoYEqrHjTmdGuInJ-eah1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=kxB6WFire2Um2kkuAVA2nzDPjW2DxvZnY2WgQQ5ddjte7jhUb2KspwWmeXw72bwmI3OOcts2mr8CQRTYar55SvLF_sJG2NJsug7p7fEhrgTUH9SDt-1zGDK2nMy0cypqJ0hWYUgMmhfIGQaMANfGBVcSgxwCkA8snsGelJjW4lQhQzkhCk4dgweMitzkKub8H3-na9SFk69WSzj5YHROkK_CTNtJ1zPXT7cz46zlq60WBnF6zP1nrOTPxKFHXUsQRXd2AFUCpg1c5zl96lf_mauhkDh21DzaMNBC5dL4v45jwfmKYt-UmvDmVmwbcbtD1hfF7pSb148-ploi4u6YLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=kxB6WFire2Um2kkuAVA2nzDPjW2DxvZnY2WgQQ5ddjte7jhUb2KspwWmeXw72bwmI3OOcts2mr8CQRTYar55SvLF_sJG2NJsug7p7fEhrgTUH9SDt-1zGDK2nMy0cypqJ0hWYUgMmhfIGQaMANfGBVcSgxwCkA8snsGelJjW4lQhQzkhCk4dgweMitzkKub8H3-na9SFk69WSzj5YHROkK_CTNtJ1zPXT7cz46zlq60WBnF6zP1nrOTPxKFHXUsQRXd2AFUCpg1c5zl96lf_mauhkDh21DzaMNBC5dL4v45jwfmKYt-UmvDmVmwbcbtD1hfF7pSb148-ploi4u6YLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi_qkqHs1VABVZENxxVjrg0P73JTIp-_kbSJFXqq6Y5wXgp4WRS81nFP10rHvqTzROhLJi4McYMHSJ8Fccp8lq-0dodjW_FGO6KWaMgIsCQZiyaPXS2ilw7z6BB-zHiuCw-bbHuCTsaeym7kgejmg0rTY8o7enENs7pcAm0EsAmQP4oPah_r6YxvsplMIcgtnP0WJxoc5cImOvxXSGX8XXosOkU-_Eefu4jCFEZa3XTLVVo597UyxddcGJTBkY_cgycpyYl5sJdrHLzXLg8JMDyn5brBiTcMwEEygijx23Y7kP0V2Qavko6u4VA2N-fGpfC7w5Eq0brvcCeqpeW6yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyWeKsw1yhWFQ7ewyO_K014qbVQRr9hmVZttukoVEOY9bSAv8iqRpIqPyKPHxnbYwMiRRV3OEOAYClevRX5ZDN0tsLRUyDBnwhIZFZeF1xukmdrrL9EYuNA3Ti06zzfSM2WL8QGcoqRyeOudXdmnIAzJeGNtVM429rXskRtndliVS51GHNKtdI8quoTaZgwEBX_uBxpXo2dxwt1DU5L4EcbXNzyxG6yRULp26xiSc4VEhCzvsnPqsMs11rTcP1uiLp1sU8aTkhnaEzMic9VFyfTaZ-NfzjBa8Wo_nNhsxL76eExTnB6BzeX5jqHTZv4gj9TzSoemu1bhue0-4hgZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzd1p2jH3xy_d7WBWe7zBj0e-GbxS8mAu6oLBbT74Mpo5Xkn03YNjd4iDbq5kptFMiU6ea2EXrhvEGZ8kFb7w44LQ0K7408ABB3HHyUPxqZSO279o7mbhHxt0e7p97k0-PZmm99gdBdqvSoAUE38_iCP8S2IxJHRz9niDE_CJQB25jlP23V8Hvs9_Moiano4hsVFygskDRgexHCBd4d0E0JyDniG2FS1GHD5tN5MrFZOXH-ZYj7_yAgxLVSr626RJN0i7W7K20BjQUdWFNy8Jpnx323_qFcpv5GoU1spJmufdOsDSOgace461nS7Y5AImR3oZbTeEHJxNqC06iI-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26371">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lseNwCRSPcr8c2Stg6eAQ6tNVCmhC7uryfwOv23rGhPkDgYQ3DShUOVYbcYf96EevXkwzLT_tuqhdN6jQ09wrusUjrB5e2XmT2aBbZPMxKTtvMottPBIQKiFzpIU1rKJqJPlXmRyiel7Q7UcowO7CDS2EDPWxt5L_lOl_JsYj7xL_jih6OpSSE9OtailItL_pg4mnaMH5IAKynNOk3JmLyNHo0S8ccf_sNyP-mVDAI1tqCXgcBj3EUQZ7ggrIOf2_bzuPqMdQC8TAFXhRAEJ4bzEYSYUx8QY2Ujq8OKqLTfJN3V4J1ZT1P-r2-vTpB1efZihq_YeB1fEEpz7H2MnIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26371" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_2fthrgUSYryKW1VsztHt1fpGrnSFttFttMcDx_kSL6-9nENAqRvcUFIS4b91rQ-BeIGCMe8EqQ2t2d6QdYa3qmUsCXmLL3zrzGfZ0m4Lfh8mWykLH4XoYo1hUxmd95S33FjLFnuZhGLrCzQurOTZeMXc7Y29xJenTgLAx-f8MkDJC8mGjsM8IeQolL93TmUdMeNUP-swpqj9KGztuwH8eWe_lUyEopvj_OsuqgQTAhv5Wu-yzGnSmeGjhtuT4-kweBAsOYia3crdCidOVesTadQeWsyl9dgUVzqOfDlxKjzgD3hrSFXo-zAVtpRhfPs_BSp5HfPZcqD9On4fc7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxeBwGvOd7ApmG0-zJOXpCNbZ-dfwzgipL738Z0psqDwg8OI4oHpl0Gyw1KqAykGUoUnvSyd1BoCXHAtjJgW6EBwHKyCNwqIDjrA3Sf0NJ9LxECQ7bwxhPcW6Qf40L0LsRUcE-PocdXa8DqnSIDCQBFkRjUixD9QVptp5Xtj0VvnGk18QRr6omBYFoxFwRiEXZEpip2SKgcXQeI9BbwqjK_mbB1WVbTDHOuVWtUKTqbmSKOfXtuIIiAtaQcy7RVGZHhow5WJkq1leZHTOEg1KAWjK4Ka4brsoUTFMze4jHeOx-Pxl0JqOZfkf6X9agC5DQa_-qmgXdrDuuQveYtomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFoy3aMMythk6t3vN5dEhV4nsV8foKZF7FRrGavzgiYJ4FvgA6uQcLB8AOXD5uoFFZT4Y8vjhSXOsybiiiktMVQFs_mkD3JjhKe4diZIM-QGGUyl3_ybbmYAwUiFZM7fK34PlulAWLBohyOPqXBP-2574-zuJG0S9u6zOWfEsIdn_J5163ub5RlpQE-8qgdvrTm_u5qcQmWz368T4Pu60U5LTcHImVpRCD5qUyb0k7MEwjmGZTbP2nc9z-TY-joC_pmTjwtRiICfVYVY06_ZcJrpQA5uaAo0ENs8ghcZ5ZbNPcvHE5mdI4oH3e-CA_-cXVmiW4j0dyloDiyoH23eWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSh9LW5iwvshiO8njbfbL4UCJjKTOU7Y4l7d-eUNBpFVL0ePijGB9wRCseZNJtNq8ZQk3vN9fJQeT_nQBEnakBkqQutXxebvsX7oThw1U-eigx-7V6bbFmOyeGzRSk32WUp7WTrYMl5LVpCqQyfLsvX9gKL_iA1Km6amVIl1pjUtEe5GExMm8H-ZSYJR83p0ulxG8OB3iR--wCxyIHfPjA2UPML-RSiWijt-Xiv_5H7FzTGy9a5LuULFvfJm9oyFxi8n7emkXJ57xB-xOJN2SDkqStcgZl9xmbSv6pWFQTbJVd1udLhg8nQ7GkJ0NYfwtEyeVA6ltTpimF0jD70BsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=M1IKlKSHppS37tx6dyXp-oClAlyfIb7HnFJMGeYGfLMt1yxyiU292BvIBP9UARbq5dFWkLOP4mT51ZhN_lUBZ9q0ilFtq_3oQbm-Wjqf_UfRry9jCYhNl92CL1akx-ynDHkzmJbqeHnQtRNFNu18XTNIHsI_6YB1f-4_FfMtIYMfdhcJQ3BGQ9xGAvPXCQUM9oTYwp8vbffC6AraGPGnP6uDcSPa8TSb2HrVN_gqxA-ssmUs1ufMyqAH4E4GmJta06bkjBsd19cjijxMaFN2zz9dg9qb9jmE884Ceq-Try9QnViRy0HMKuJulgPAP4VOyjGZhcfh7zet5Bf880eyhzv3pHwQU3ZblzJBo0u8hzIVGKTUgm4CIIyb5wpJBICmvBfFIA4d5_0snPhQX0MEy6NmMHKzeSqfvY7TFbI5uXkRJDAYIMAekMagfaRjwcKZwsQw_HD1i-khnH7C_NzO5YZQqgEeKVPPGrfx5cSiYdpYkXOvLAroFYIw6BkU_aN_L93ttEYzC6C9BvrOiNKWdm1Mxs370WTd00RD7w5Yb8Nc9ROYFRtCZ8F9cct50srmWzH8PisyQ7tgbl1wd5XncJSmX4rIWhVUYTdFq7JUMMqpUhqBY8RhNmvKyMMJW1oA0vNpdKuKRdjtsit0dyCsBx1rA4s7pC6L9hZ7oDapgeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=M1IKlKSHppS37tx6dyXp-oClAlyfIb7HnFJMGeYGfLMt1yxyiU292BvIBP9UARbq5dFWkLOP4mT51ZhN_lUBZ9q0ilFtq_3oQbm-Wjqf_UfRry9jCYhNl92CL1akx-ynDHkzmJbqeHnQtRNFNu18XTNIHsI_6YB1f-4_FfMtIYMfdhcJQ3BGQ9xGAvPXCQUM9oTYwp8vbffC6AraGPGnP6uDcSPa8TSb2HrVN_gqxA-ssmUs1ufMyqAH4E4GmJta06bkjBsd19cjijxMaFN2zz9dg9qb9jmE884Ceq-Try9QnViRy0HMKuJulgPAP4VOyjGZhcfh7zet5Bf880eyhzv3pHwQU3ZblzJBo0u8hzIVGKTUgm4CIIyb5wpJBICmvBfFIA4d5_0snPhQX0MEy6NmMHKzeSqfvY7TFbI5uXkRJDAYIMAekMagfaRjwcKZwsQw_HD1i-khnH7C_NzO5YZQqgEeKVPPGrfx5cSiYdpYkXOvLAroFYIw6BkU_aN_L93ttEYzC6C9BvrOiNKWdm1Mxs370WTd00RD7w5Yb8Nc9ROYFRtCZ8F9cct50srmWzH8PisyQ7tgbl1wd5XncJSmX4rIWhVUYTdFq7JUMMqpUhqBY8RhNmvKyMMJW1oA0vNpdKuKRdjtsit0dyCsBx1rA4s7pC6L9hZ7oDapgeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHN7_PwNBiVse2HMTjfj7R8IrUJwFC2dQSlo1fH4sOT70rrvo8ZlTvJg6tn5CeAtlfpwsWPZUBAswpgMkKcDPOJVrPHfBdlv4AUAUyLeok88mKzJVyvLg9RklNlT6jUp803Qc_jxOv3F8UkXHANQDpjdirQlIKPn1_IiJ8zNY4Kjc6zHDr6M0YKiV2Y8OmP5I5uawt49ALYva-bqhWUiKHyEwx7Tfsjt3dOtoaAjeW4gbGk8Otn6uBH7Ram6LTk12gt2_cgEXEOv0F52u_CtlaxvO_LCK5lfQMg3jTc-jeiM57qDBdWxwi-vBn3P0zMfNsMS0LGmqw5kyvET4nATzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKgNOVUiFumy_l4czKb_yjP7GqX5opjKI1UtAlZfAQTGTGnx-XhNhArzJfx_Eyv7CLqiHS63AvScmXuFRKfQXQTmN495CKchAlck61kFE0-y1qbsUnFtoZEUjlPfRSFBMJy7L_bDBvefruaTuvCyGx2_nWO8eq6Z_5JQHEQS7qZsvKkjNvEayKQ6ZcavD9pvuOqm19P5FhtqDOx3Fmkmv627Kvgf2KCAG_nN3-1fLT2chfREea6HBT22EgTA6CsLqw8Dz3DNPzXEziRHoCDi8TwuNv8yM-U35WlVFcmKU15-NDoPcov4sqxwBjRSW-2m92aGuxpPwxji5FsWp4pqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RszqBKTdvJMFZmpXJMGa6eWZIeHwT-3cqVMjLHkndZKHJGzhW9w_VCQH6EH9rg8OaWj16qxZ2Kjyelbx4DbEogxgYpzGdeSlo71aHYya3rStPuByaVmAqkJ6OCMYHtZ7sZ6ylh0x9yoLAmo5vGZu7PXL2JFNmBbol5fxDW0ea72g5QjFXoY1GZVVgyhk0uUsi1DPUDCjvV3H3WQ29fx4z-yRUcUsXKl_yUDDS_y4DnzgLAKYkyMMQqFoVO0zt7_1YqPK6PKIinG4A47XhV_MS6RrTdFtgqgtTgVcKHCke67ys5LPCg0J_e0xki7ywabBfXErao2MWNP5Y2fMcgjcVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaPBDulNgYnESQZXY2C9iV1g2NQmj1D-mY-Vu1mPoxqcbs7F8XAutHGUJBdvkDVfkEvtsVFy7i6B98tUHo_GYKFh7BiyVYSFlLE3G1jazElnb0sxX_EpCS-ifnhuci44VXqYWIOgQBoCfarmNyshz0N8hXHkKpFCr9sCyG7tSnJ-nc-OqIvD2GPeSihyccK7b3oc6TC9dGi5EUulIUKliDr6iW9QhqNHNWZlXoxQV7UQhaUUnRrpJXdho5rkArPqdm8ALao1vr86CROPi22pNYWLsRSxe_MLksSrksyTINOOP4w49etPiV94qMtFS0Vpg4KQasad3BCxudKH4Eqj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC1HIVAMhNvosIo5tgSvI622wKql1TqSPVaAapXCWZG1fIY72bpeKUnVBVE-5tbBQkqg1EuEodzxmDJt9c5-VlJC6QgFUZFUMlhnGQbHQJa5QfNZlTH59Rwe5gPFOj3_h8-OIOrC13q-VgwP098k70p07D3QlmUlus63IPVGIRUNgA4qjGW_tFki7apueGA_Iv1ekxYtM2KRl0TqeMzuMZHDJMnUD6NJpNBA2YR5Qwjge9XNmBrRxTSHXtd_pSc1-I2DQzObw4voGlnGs_8PSoLt5Y4ykLgOwMIkaVTFf4TX5he4DAUjuJYCmwcnGIVTzg3aG5y2xXvw4Wpf6n2GwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ3MwusGoFHk2YWMIdmJ24wSnWqOvBka7a9CIX2e2kHFRazMdrCRXiQsL0ig820o56EGlifvKaiP62SvK0I2j9-XnXllfqU-AXfTHLT0veXtrds0F9dyOi2rrDdubAiyA_zDrQqSJHxHQTBl3tOWX6o-hXbETDWM7juCRsV122UUFan2Qh296NLHC31etM0o8JmblY2grIZxK15AupKEcj_IOYQvFsy6o7gUG-7r5wuDQUfw5w0NQaSMi4C7XM6d9E7EuCuc8qsNpcowm9fMOHxVeDw6_eGDYV_J6vjEc6nUZXIZy0baHwapibQ4VKh6gQS1UaFJEigT0mY-z21tbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDJsDnqudqWFdSbTj_qQbRAKj9F12_A4J8rDmwZ8EyFxlXbNJt7fywLeZ984VmkxnnqfKHDdrJqWWrmih-nzKbYxoDXiKZAgRGSdMvz7RfBhdq8h1XTvGJTZOqwp3iww4A52FkClaNY1iis21k7wylHSXvdHBKnWKsRdtDtKYeUXLhfH45ELyvM2nH8BPWuDt9_ZwX-VyO3TI5pkUidis_CM14CZlSIBahpsmLZRgfz0b2tC8DD5g4rlq1Sc7nBtC3ZHBHFUouyBwwr7nSAIvVOno-HYeuUK2OTptYlZsqIf2UWe4t9MdxESygJSZMet16Ke3sRRopHWMQj9EQ-HMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=BHnSdwoszLWGZHgUhTslZaquIHCYE3Z3Kgf8C60fR7snxBem1TILqUUemAs_bGVh9pwlY_s2sOpkOHU6XCsrI_LbVQiEEfSZkgpAa24yv_4B1CzOeIQ9_HCXwuhND5IOD2DaBfTJDBsEubo8deNER5LK-xQ03GI9wt0ntihL2Bsg-SegeLgQP60Z46UOkLk7nTGgmJrbFCYUfIh3ypkqHMXCg3us1jwVF_OdD6U4AxZaJ2VXbKZ61upXyTSLKLvd3Pq4OvAZr2ErOxH0TenGpViowjJX8uaiug5WfOQVAELav4G9dGFTPubLMT74ol9v0OSgeB4pl0JwwU9YafBhNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=BHnSdwoszLWGZHgUhTslZaquIHCYE3Z3Kgf8C60fR7snxBem1TILqUUemAs_bGVh9pwlY_s2sOpkOHU6XCsrI_LbVQiEEfSZkgpAa24yv_4B1CzOeIQ9_HCXwuhND5IOD2DaBfTJDBsEubo8deNER5LK-xQ03GI9wt0ntihL2Bsg-SegeLgQP60Z46UOkLk7nTGgmJrbFCYUfIh3ypkqHMXCg3us1jwVF_OdD6U4AxZaJ2VXbKZ61upXyTSLKLvd3Pq4OvAZr2ErOxH0TenGpViowjJX8uaiug5WfOQVAELav4G9dGFTPubLMT74ol9v0OSgeB4pl0JwwU9YafBhNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=b_LSpL8YtbG18U22QUSdsS6hE2ZqyvJs9PlHf4dcookWYih0vdVDAy3gAX5RAgYPDpLM7X0iIANA4dNx5nFss2dmYp3jsb89vUytKfMo3AA-dgdREy5xK2Fkq8H1YeoHWf6YPwO2RxnTqrSYMbhxvoMulVw3UZRgf6tqOspkhsHi1morIYoRWOKfKzRnLrBPDApe5CEh5hwHHxL_wRHru5SpbqJvEK8RIPsZEysJ97GkPBi5LeFG3mmWY4fwAgk_c2HT7jrsynaAwM-XyETO5XPKyQ4jqtmmJOb2LVOblfShVbxOxjljquC2Tf-nrgyn4wp_eeQjtRmr3kc8sCZd_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=b_LSpL8YtbG18U22QUSdsS6hE2ZqyvJs9PlHf4dcookWYih0vdVDAy3gAX5RAgYPDpLM7X0iIANA4dNx5nFss2dmYp3jsb89vUytKfMo3AA-dgdREy5xK2Fkq8H1YeoHWf6YPwO2RxnTqrSYMbhxvoMulVw3UZRgf6tqOspkhsHi1morIYoRWOKfKzRnLrBPDApe5CEh5hwHHxL_wRHru5SpbqJvEK8RIPsZEysJ97GkPBi5LeFG3mmWY4fwAgk_c2HT7jrsynaAwM-XyETO5XPKyQ4jqtmmJOb2LVOblfShVbxOxjljquC2Tf-nrgyn4wp_eeQjtRmr3kc8sCZd_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRq-cyb4EP4tx5PdOQS9H9xaZfgNKJirS3pNMb2JVvfIDVqZ2OTAtCgEQXAgQSjZeYzzCYwrn_8BkkdhMz8jZfmGI5DeBfY9szHLrbfsIMisk_JWPB6zYqj_-NTdgPS71JmZb5XESrb2XoCxnVRO3o3AT8zx8Qlhm5gsOz2QyViXcG_m98_v-wXhb56zM6YMRP6T6WGh9TCzxqYj1HykPCJWpRqcsEpGLXnxKISbWhLfT52yl-LQOdG-rXN0eFV_-nHJFxtoV4TINABZF7fiZvqoxbT1dEL2FSx-jXufZDvBYAOUX9-1U-tURoi2LNSwS5OL8pg-yBNCbwEO41S1ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnPSVzIzewA5PWicXID_wwkujF_ziQUAdNbIlY1xy6yFP3rgzDyDyN6wIo3w3GWrKemiM6aSv_98dEpIFonD4wdyWkwi2Dj9QsVWIBWOrlhbsYB9U7xVQw9br0JFFgOBcP2_s5IA5r853K_P6zehqVhoUexhT0Owir9FiNFXXHMW1_75pcXQxUfshGLABfVXcfLBmDVJyn2no-EzxWAdi-vw6anC8-xhTSaE0HFxan_jyOMBm-K8gLJRCvl6HWjWJgBM-JouTk3FBVtjJwL-LszBEPVgTa5OoH1_K-S75NVr2r1UM5bDRJtWFx5i63N8HXUf-EvPtBhPzpgwXIopEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7B1G8pVTNeKFyH9Ekt1HxY4N2nbNO3-vYeG9QDKIEzjzL6L4XLYYv1KLkeLz0I6GIL0L0I41CqgFBhvuYvXNNsFeYxf_WmmV-qcIF4BfHY5VQexU736rPD9R6UNQVkESzW2l9GKRsWFedlaFKsDV4F9XlWOM3rDVtpvddnnM8r7_kpm7vq4KdLaw_YWxYkVFDdz4cwpPyBksbdSCkr843qbn41V_Qs1lcn-Yva-7KFpyZAG47FFMKh2TlekXS1iPdYD75VBwNnC7qncz3VPYM6wLgREOoWUJJXTiwYrP7KVzqROsKuYgDs_ubsbmm42l9vlJpoQsheeYvm2pbqg2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYGdsBj8J6_KlZoGSQH8I6du7XbkDkB6gQaseRf8qLaiYktgFQ3m3GH5xiN09ZmY1RulbQIiBMgQRpVKcet22rnv5LU3KtOicrvfvRAeTNTOXOouvKEH2ijh0Fb2flGKCFubQRG0Fvs2StjavE3CxAs6n3306kwtJbp1Y8s1hwbvTiXNNzKuXXq6-myHVXGTWGVxxtMtXwv5vRSxL5i-shLuBeXjSetlzZ-3VLI0SqRQEOESqDbmtQjOJkTDolafBbU9DFG78G1EiPuZJnrRWp1uwH6FeWNE8qnMJ5Y8smG3psJzY2DCN--9gGbd4h2d0FfMCWUvUh2PfBsi4VNatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOrlIQz_faRn21U_1uIGm8BH52IXI8pD33BOrRikDerY45b_hjqAdanfjReqqtGW3Q6dhWjjohM0EdmBKy-cuVOUga_wOkML0B38mX53vfe9tiqXL3BHRleBr-dBEnyl3WasRkOJBxVIjBS0a1FUHgFF0ZvYLgNe12k4P6BKpQsfSFGv6HnvdI80LH6at4sSurRbsLdvJkNv_1WOIPbXMNMc03W6q61D4N06FVRijcXDAaZ34hBf-p0cVKa8c9LfL4-X6L8yaaJILyqi0SXCLTpzBIcovJbBFgMcd4-TVYkUMOE5ZkuEeELGcqxirMi5_o2p7JHC4UOwzP-xamSf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAN4Tk14LAvLlnW6WvIjKePOYAfTy7ndtrBOlwmoRP_auPXDU8-3Fy3fz6lJ8gqjMt3sJBw3rQ4iJ8lPXkE6N_zOoIGBqBuHfrzTPjMRdU8dVQAJ8lnRpyDUqtmWId1UgjFs_DlCJSC5VO5APM1Fxw3IKcJy5INekVjL2xk7DnMtDZAYwp8yqMjNAogT_5LZuV6HsBqHgAs_Ed7HFPy6O2uVNRXFpc0scK-zHeMyvHJhWu5SUUgwvqxBBwqk9Jdvje1SWQnC5XbBfaAoBNCE7HNUTlz3FIHQPiIRnwvTmatuImU5lPOOdsXNbZSiiGsKkveqvy1hs2VKauss3Oxn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoGr2v05DV-2bf0S18fSYjsw4-kXMCxbTe7HoyZVFC9cb3xBuE-duqfX9Wf0zGZQxnOeYYF6K5XUh9rpAr8yQhSl-1iyqoE0WmLW8LdiFmwWeuZYhqpseETXV2TMMG5D6Qis6dthp2qY7bPEV5hqyIEKUwO600MiD1c7Y-zMJspUUyZoh3hyBkS98yF2YfwiQkqy3mELdGw_NmnP4UoxVs6wZSWF4uyDpgqy5yC8TDtQhDKPjEuagWjtNHji1-KhHDB903RhB5NTP741baK_0dg4wnpa4i1GaM4CYYT-rTB8XKtb1P4IoNMhsBWmXiolHdybzXonf2d5YxUNVforDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=l5G4socFYr-YQCFpHA76eIPLPZVrsgTHCE0J9bVBFWLcrhl2c0OkLwJdLHmG7rjWHHJ7z80VVJK1EfgsJeDO6DYaP6vr56n7qlqqZUWOCaGFhZybnQKHJTVV9MKv6dx4REjNnw2KWPCaPiyOuV0MIvtvQSQOPyf4H5rLs_8KkOCP0FZEg83zKA74bcqBxXUF1dJ9u6Jlr6odFnChz4kfxpMS1sVzH2wGj5IUIKGoVH1Iv26dI3r3imLUQtWv91Y0KB9kZZSNuYHsiomHBifgobjCtzImhqP1QAroBpRLwXqQoNdeOAU7imYzL0fQ3ZyuAqxifAph0rF4XKk2sBZEgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=l5G4socFYr-YQCFpHA76eIPLPZVrsgTHCE0J9bVBFWLcrhl2c0OkLwJdLHmG7rjWHHJ7z80VVJK1EfgsJeDO6DYaP6vr56n7qlqqZUWOCaGFhZybnQKHJTVV9MKv6dx4REjNnw2KWPCaPiyOuV0MIvtvQSQOPyf4H5rLs_8KkOCP0FZEg83zKA74bcqBxXUF1dJ9u6Jlr6odFnChz4kfxpMS1sVzH2wGj5IUIKGoVH1Iv26dI3r3imLUQtWv91Y0KB9kZZSNuYHsiomHBifgobjCtzImhqP1QAroBpRLwXqQoNdeOAU7imYzL0fQ3ZyuAqxifAph0rF4XKk2sBZEgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
