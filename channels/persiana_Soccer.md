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
<p>@persiana_Soccer • 👥 572K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 03:26:29</div>
<hr>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3zpc23F2SgfQY-YsM15kpXP6Jv_vIIffL0n8yxujaHaeJIoYAQC10a-7OQT5sTIujt1XvHyXAtSM-tzpNIjCsHRQ7XMO6ZawQyrDX06KpPotG7X_F-6lW2uHbQwa7YgDRdT61JqUINtIkOmaAwTUS9TvPdakZ2go4XIk1Rnu53bu49MHeLNcYSpw1R3vhjR1AvbOlT6QDSkiCAdaOt0-lu42YiRiK8rn3q6c0B8LmUTlpSu5YIzXxIn1r0bMy9xbgcXW72hCNJTvhtc83ZbkZxfZGhQuaDFGr2B_MWFdrOnbKjbH4aLqH7fhEsK3PtokUfAVorH8SyKrxqMwrAO5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arYwPNq70jOGRjMK2BPfAUO0V8vU75l4A3HFyFW6ltt0HMu8GG57oyNjRmy5-3B9j8IEMlD-mJmn1HcgCMcJZLcnrEqWJuGjjCjZHjYtJfSE6lJJ71gWXVLdJH_dSkA3SrILN-DJNoe_yytBNrZt4cKhdXf0DvIHV7OHt3GLyGRA8rEZLsc9D6RKTGdniAUYwOYi_Pa2A4vyKF4_fEzezYXLseibsYz1E7NAEFa6D9y1G1iP4rQMPuqfR9T8aVCr1F35OkmLfZOtlm1UIHCm6COSD-lO13XHmgCWVO2CfcjEAQRVFmLD7Cyoni8gmQvdCz4T49B8irL1w7t4NgJ3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYOeh3NNTZJWvziDzyMwJ6ZRkrUFigB84Q3T_xo2KUmpxFQCEdkQRGGc8-96DnRS87S0KmruzJpdRiA8iWX8Nv-SxTbcRl5a8ilOBcxP9eVTKjt7QqGzwCUtkGDlnrek_M8FQvostTLV8M716IS6RPmclC9TJ3sqnpG0kiSKOs3kBRLo4BnP-5evivBYfwMVB0T2bipAjIhs05IsnGi-XcMkaGEz4P2LnuD55eLq80Aq1SqLNKJCHyAtx0N8MWLUyqbAWBNQC8r5cWXNGVTI8Fy7B_WtiJR-VjC7o06Uj64nQ4iz9sRyQqbs3h__fL0Xgq6BzYs27zGWzHyysAQCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMufuQDRIdU9WeqSk3z2lIju6QrZdLJ4F1nAAPEW75yA4BD3BRdT3nMMEZ2YwjPsmDYHzuJBPUJBc7fTFNDJANp0rC3ZWt6zznqR1jzVXrq4RtOZQhRL9xmAxflXclS-C4uG8EiXgs6urJTH-FugAG69UAi65Dysf1uAyIDtKnPNdQnRRY4RPdGGD5m74q0WehtQMs-8TzSdbKvm5TvqoK1AsdXnK5hErBprCD-NZhYeZ3Yaba8Sp4lr_Ww2Hy-OSvdcG18uyDiLRsWpXh99Puvf4vfU99ARkHZ4UQ8EOfy74Jtk-p4zjuBo6CC7rnuZbCdUEA9FAkL23N_ijktM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26449">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/26449" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKI-ZP0eJSJfvMbxaouVo9GrWazHdytoiHieIElRJ-plV0SJEPWO8FonzBwqdKr-BBqeyIsZdsp-Ql6SrGVfMewgQnC7sWCSZc_1zMKRc0mdVYIyNqUAN27UPAu3pzxGBYuCTmdgLUEguI8dT8vqzPjAfeU8wJP3PEVAA-qKT-c4p-LUj3Qd7KIgi0XVaxQiAPkRwBWcF8K7z7vrj-QZ-GtUSu6M93z2OMulxM00AY_53A2oY6F6a1cAqZ9dVUZqiR4JhbnUI8ut28VZzsmF56XIXlNRyaFzFLbVhEpwCd7TEwCmtsnbHrhwz8XHANX2kdZyOLabP3g1JDYztLLMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDFqYSWoXeji160qeHpj2qrVxYUNGbgijuZjtSf18V-ztxdVZrDfTBzlbkDiy2sA6PUj_XzDNdqnzZUIDm5ibgBZxJzTdtvNrcPWtHOLaAwCmrhYsWL_Q46fHog2aTcG45iDfy4g9orpZ7vktUtZF_zNHnvwQQqDrzNMLMBjVRq85bINuVBnNG9mvHlTK8-fpsxtOS753DVxv5U_wMolMQiYE8IRvn5Denw8Mn5BXd4hrerdH0flCoBD2eCNcAFZaiBnqmUibav16HEQdOYOolJDJmguAeF3Yd1fejGg3_vMkI8SAsY9N8paA9-Ei2C7NWaprxHkwKLba5NIXinzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJg-8f4BrCwk43qsOEgMLKMGKmpERGv0r5TGM35Ewja0lUVkFFuIMNziZP46M-3h07G7bR2IeXLmD6FJEfW4DA_CpW0PCyHkSkvb6EeHSNsPgPv_ljx9K4B83N4p4-Kv8TMBVENXKveJlshU0jsBAfokW3NMgXTJzFs558wiSAQ5Jaut4oCZ4D4s3GYrV2JPvNJatMBjOz08fGcsEMKjh8HbTdNMLY4MtZGiLQEgY-3oHEuiwpT9bb_Xxwas3SIDO1slnp4K46rP3vSv9H6TiO927gYtpKyEilc57bjlubU0BtLd74wErDkd56gtSJ2a-0DdzHiMUF6l7SJFQOU7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fen10W2RKem78DCYolKy9_GMEmtXPe7vic36BtpZgEBq2YS6WWLB2VTeqmhOqPiKX3xeF9Dg8okA3n0s89AGmiMr5T85JVaCE_R_Wb5r0lnRxlleecQm0Ret7kQ5cjpaPKVoEXwUlOUikAd4Qa1IsFjejYP3W3hGno4f24wJRcsxFmT74EMh2zaFXIwPJPG5DIT1h1VBNGzqm1QsAvklGLv10yAthZZMSBeWHqHnM47cxBDF5uJrcDztbqqBtPryqPzVFqaPx6VZQD9tBPFKfsfxELqV0cIIbMQ_kPS_huV3TNq-O6XjdhF-GeOu-1X7VVIfj7CF1v9BYok6_K6KQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nov4oz8TyZVqFeaMcWjBI8G_v4gQJcrmuwTCke_Y1exqPvJYjyD0b4MWNvKCuh9Ai92uYwMGXRbSRRig5dlUSrx3zo0KVNmW0E6L1pQudY9o08I-UZ3sfv2WACK76xa3s-mx1JpIWftb6TeHeArMfd-ymlCPptiBeVLM9UdxnqATLNv9uCD3m1eQzw3gn6cJ5Kb-17Cbuf3gzOfr-_c7ACgmV8REUUkN4h4kUXfAMQsN2luyvpc0mmB7qt9yyBA9tlKowWrMSoOQQSW0BRfx_zG7-_7_2QM9dX2SVY5urLsd9372q33ZiopWoyd9hxfCKqh_MK1b3t_u2KoTIl9Dqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR2gTi1RN3B9sNfYq8DVDyqlgjxD42KWcJJ6py4rOfPXH3D0rz9jdTCvild7m9EQQHWdgESQzVMmNZw1zSuZC_weC1KKqBAtmahf6bey38irIrSPYEVUvZY7NpEICwMeqyhD4ryBRlhP6AFSAv2E8iezIK1p3O2pnNI1DHDnYLCeVVygQfIN9NszO4kwFvh3f8I-gJ7II_ew8q__0YVz5Uh_7-g-G8vWr6ca7i8QL_22FpHc34J-ZDZDGeuCpfkPAcL93cU3ArZuhP-R2V_KQ2trh3O6s1lKfvf24gIpOGiRna0QDLoCUSjSv7hmuH1TMlyPhbopQ_FmboVQhh_oAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTs5gQzUjGN3_l0o5kjkmcSrkCCk7XOFEfk_yYpCJOGShN2ELbQROfnEfZXDi_n_kuJQI2mVLnslaXrCx9GmS-AOuKWtGZJciV4WeZJwVDmUfqSQr17HDFJMSsr7sKN-Gkp9OzX8kLNAjfNWpfjQFGELSUs5GFpixTfl3FpLyyVTsUGb8Fufw27Wbo4NLU7iYfxXqldgk8xSslZz9hfWTBxbj3zKpKuFzIFd2P0sRou9gBcIu1bJ8z1HLii39USnL8WYPrfzrH4V2g8yIyw3lElhJwSCeIQfmZ_6C2Mr2IQzvaUHyCDFEGS9FvHn1Lt4e8tehDz2SBFjarLzpc3l1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Baz6TpqpGM3jO7cDbZfteLMYZaGAkWyZ66lBa0PVRFCqwXEQn_h7tPwT-L9O0JmEEpldo5vbWhOxrh0ytgghC1kGA9bDx8chg08ohZPu-0vKOIzCsm5U0gJvZzK-Vc2xmcQp8hYiJlHvq8mK8QiV8b3DL4f3heb3lZvZG-xlF6ouSNrrK8gOTvtoUAwWRzU850Qjjp9uhQCdDf8WlrKhiK_lKFdN3gFIZ89p2IY8oDYlCBgqz4zVEG6ZHxB7uWf-RDQo8EpLLbZK7lvHGF_4WY7JsfX7xGn4Ize3d8RMyqGCxftoJ7h_J08UXfxKjMdVczC7u-gQN_6wTINWEdkOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsk0LAIjUp4S51ichYWY4t30zvTj_cBdW5TyMHYdGUGVLdP-sqXLp-uScTMTKzQsvBJEsSpqpZCQnVdi7wQrElvKlnU66u26GBaIETQVnbFlsQr1luW73hhECLWVdzqbeWES-nEw91SqT69W6nPFOHoaIn0BryZDqpJnmSB_ucRQp9XYj4kis_87cuIjbdsuTIlGuNBOLXvvt9ciW1eMmW1urJbg6GJNBmss9zvEg179vtAcJetdN_xAejY302btV_2AXLyhE72ioZYlpExGtu0U0fLksOwFPrOhP-9uIwkv_vCIRiUUG5U0Ry5lkOYhjjx8-KItWUkuaxwvMIts_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmGVRUUU9nm9bQO1b19kdPaxBJphKpPn5sc1pYe9GDxvxfWu6hhIUgMTZuuOGuDz3H7i2UQSZsP2a_4VaIBd0URdA9rr-UdmeyaGUeE19YC1bZ8eTQYN5JcBXGZXrWh4FTK5Fs2hzUSsmFY64to9yFxDJlrHH-HrfczQzSqQnsu7CAw7xEFsVs8Be5oh6EvhDnrMsgHBt7QSDgiVJrkFcPQ6LB0FjXNpAPtNIZwJk2bRMVM53qPr-CZQaRf0WYleuiEs50IlYwDuO4dUbCXGASHKO0U3tUb3Ov8D_9k6FAkcr0YfymGNEpmAKwKZumuaUY91lVjVdjXagS_U5uzG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIQvtyPga3SAWJjoE2TC1AQKAlvGc-cQ2z5iSh-CsZ-UgA7g8J7dCS2FcpRT48egzDeb9p6y5mHMvHwgUXJpJGMHGsDWWojJMPVnjzmGvq2yr_DGP97lhEnVnT1hIyMVKS6gJi2ZxAwdjHXngPLBp10g1lUeAFhcUpsrElrooAU9bilM3zGPJoxmMjLzxHhFEie_H9KVed38OjuAMj9_5MLzUFKoyhOgSAuJrnsWGjI5vv2IITuI1ONjwiod1mSnhpWGZSRH7kT8cRAl92ak9OLDvZlbHpSbC3MyDgKqL9qX0sVwR3fwQgn1m81CDmvnX4HmPeuMB1mKrF8pt3YEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtrhUHxPNACw-rlGtC7_14IPVA5auppECpLbKAnLy57fPxQJS-VjmbUATNiBztkGt2VNHfd-XbCgTnZk8im6lsF61q80B60A-ibTRNW06UBaFmRWCQgnkWKGTj6Hruj2szE876pQQXhkOS-mR-6L8_lHLwqJtXzJJ5GS8pB_POS50VmhPbqi_m6koWG7L1t2Dtee7vEoh-Ity5vYjcZekDXh-prO8NWhvn5DSXoSIHmTvVoCRIis7i8mTAzkaW3Yz44uqJNNuC0qtpIXewcwCcdl1l4bT-ClgTORF6L9taSxdxENE_DIb0a3ISyy_uMDlfaolPbjkttkUgSsx0Zn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGEWMtgZ8054rHgHUqOghxdNx_kKvGhXweayA720cMJc_6h8U-uHx3UbzIPs9UsF8bnGJoDi20Oxpfr1rS4gh-LavA6GKAWbECqpwTWoD7rQDOIiu7pxePAJoX4NoD4zIKdH7d6xJtDhvdvPnU8BaF7sNFec4WZch8xKp4juzVMPaY2qHKQ4U89bf3JkV59WM0InW5ic_IBX-Z2IYbrE5KEcavmDGawVMcB86SCO2Cva_W4X7hPztUSjv0pd_7o6voPpXXbdymrJQUlQYT5TVMVzqYd16ICO8M-zYcm765tOuW_cciERBqjihzLoXkXjt5roEkSrIXrbpdTeL8nQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmUPXx0iKhgvNP-a4sBVFhrAvSw7cgl2833NIUIXaNAuWTZIOwtWg5Z5d9Pk_I8N8dAI7xgrsLmiEeRv6HOWaF9IeLZD1HO6qh1eGpuDGjHXraIQv_8LAozaiLzGe7ZYAi8EWb0P_9_j8pfE-PFfYHW8PaI2-rOOmmZUx1w_kQBYoYM-5A8aelvxSXV74uvGSvflDgbjKfoF18J6w-dQWbe5LbGwQiLCMLUVEzgYxneXsMbDnwZLIwGeYUIia-OM4YDj_YxYlSdopEb9fc5g3J70lQUx6FC7_0RxQlkUVb5izBC2giUdLuR_GIO2wYYKk6oGJZ-yQO_oS6AGixnESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuWfneRWN9mkbWeQF8vWDbi0m64OCBbF_QouaCy5EppzVOCSUKDgGIxTAzdF6piizZI3jEfrNs6qnds-d-AZ0LNWJTFzMvS5O0744NLtQokCB8araSDfOMGrmLUZB2HRJJ1SLOInVJPHwHJhG0PCQp3PKYu8wmM-21uCyIFa5Dt61JRy3FVGygJHx5DizIU6qagjdz-_oxGV9ffij9HrRQeMmlkD-P3mNmoKN2yQYxcEzMCXIaX4Uutg8iZGdOWPb7LAFbi6bE95P40mtUYlm6emX11aUS1uFClEEA05zXAOaBQNknCuZS7xdM83U1RBw3cIRFkxXGIXE1e4jrUXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHjvnouF13Dmb-2KsHtehE_yfpeLlyZU_3N_v6kmv0Zfz9BtlEWej_ZAxBkNdZ9VBrS_dNOV_BaaalHtTxVpQEhjLRSXfULN3bBNSIxtlei58tGTaZH8jixvn3WnfHe4a1n_ER2iOCMSMjaPVsC8joTXzNAlo-X_gaQMivCdXn3q1UsPKTMFJHhf0-j1q19Oix2dSYgru3ARaHbpg0qlBae4uCYY7jIIkY4TBUJXvvmT-6gr1Tb6Dw-BF4C2USCYt0U8z79kuOWgpAm-TMIiR6UOCs__a2GmvYqSm6lauYp0zMvx9PG2G3A3SRpRapf1Z6rMD68ymJXEOFU5PB3IZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSK5rT8PDCPNoEmxfAzdDKpkaryt-2PzKTSlF_tkIQNZio2Q0yRLjQKKp4fAkjle60QQBYpzrUTJ58ZFeuwn-kX9786J6Jog7gZEM-y7J1PeNGZenfytQZrVn_Ek9XVkCjMXJBVhcV77umG1P-3zmKMLKp5iNkuat2XB1UNwuS1WcQrRbybdY0vBJd585SgyGJZr5royQIhvYjbJ0dcDPNOxKosl6hgl9viAbIiiHzZHFd6Q3LCaXmo0YfpsBz2wEUcG4d906icoDkOKE0CnVG6IWerMci7iP0jSfI6BGCBzBFvAv1hXDSLEM0kyTuu5WpakxaQ1szukM7ZfDv0SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Clk58e8okXffYi85FI3XhAf5xpW7c7RaKdLZH3gjcBr04-bDgbyuulmlXBD7ogFcWV7BUDX8cwlJ-uCGpjwofijyRV7N_QUNRmw3mrmVr4mnJmJx5QOXvJjqXhPP-C7SZ2Dqg9vBxLkcQCI4o0DXUefxjyPDOu131wn9rawKxfR5tgAv83UQFkBfHP6vHmcHlp-len6UqNr5RCHV3sjzMgKP1S7N16skcEkklZtM-rLM7uTqAS7_NHiB5_POaDVOkvYAuUO0AOvunzIIo1YlLCyQ9j47roh7D2SgnW-JTAFbA80Qis-7FaWCV8wCCpY6zWKfcQv63BmkNlmSYVoFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE0_kpAyX-0VlFZH9G8_xTXVyxCAeMiUPslhAUQxYog_pWoRmil0B8SkvHdTw-Pw91wMSJ1KyJDPaNWkex09vrY1FCHF5XYG3_lDWwuvlKH-mDmCGFPPJahxayBsNyGHf_eB7Zb6IWFBW2E11H5gRDvqGE3z6WExhPISvWnDAimbATnTlBEbkbJcvBsYkr_79itUuYB3QRLsZXaRh_WFBHb3MQx2jDZ8sa_fT3HwjO_wQ6HY3Ohj-sOAT9r5HB4lWW3L0Tp3JKdVFcBFoRY9_-KbmQPKv0DKeEu9OzBF60dDCou6Qn2B1cr0MdTrig5li-cOAflXBhiLLLAtvHRVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF6gJKPQ5le6S9AYAvX4Jd8A6mVkZXDFVE3yAbXgzjTf-rrrWcS9kbGqOU4t2427IMGmXJyPXQ69WwVlcJVvT33YJobPKa38JRSDHjGQVvx3qdpG1HQkKdUWs1RUovdkvbY6X9i7ZHq9vFTGo-qGDoQXZnx88-JW2BtrZMkQRlaFarepnhE15PoDHSSgTg0lOkrgraSlukcAeE6puzKeID_E_GPcd-tUt8akZUNJD0di2UfUMxWZFBrLthZziYRoj6JI4LO-q_-IooYlIDXLWwEXAgL_moHn6Hby86WElFXHR8FvgN646U11xKlv4d5z4QyZ5u4p6g8MpO3axY9ijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgjCPXGn_C3KQEWWHOFDrpF9JO6wC_EkC98IVtsiM6L0E886A-gL42CzHIy-Tys8v64MFxacTpOXQ3-r9cfP9k8NKpa3bon8h50Wkpk9ji6ErwAqXlaXS6UplGziPUCKZKdYYJ4dt2t800v-J_shG82dMfWrAHgjCW2qIXinnjYc6aFoVcRDndNhmB6wVQTTrLFUpnivEvsIRmnpdFIQ1M4AwI7Mng3cU8aSKZd4eYUJ6AnuADE-UkHnjyQCPRLrxbDDvjqk2kfP4WJh6JGk2zthbadZs5EjxyAlycvjgJbt4DSHNwUyooxFf1K_tLmXZ1498Bt9tsEDPycZ9p9R_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJYDFRfYfUubrf7oaV5_jDdunHiL6pFBrmXAAz91qlwAAeiiddvZyjsh9Vszq0LWVEutGbDcFGtcczVIoDk-oiCXHIUsSDXS-QGMyyabUA34SsllYqVCcqf5CF7s5JPVW-SvhnNXsj1skDEBUdmL7Jq-IidqXx3FL5tqxldUz5NOmU_62diL31Z3k7xF2kCL5XJ8b_ilvgDFAB4ZXAhlUjB3i3sAr3jhOGBhI5krHULB1F3sux3LDOP4mkEC244BjH1vKj1t0RfA7PVpOCXaFVFoQKTspsmNDDY0HN0177mkPIZCimjVWPTAA6_4yIHTs25q8jQIeC7JGaMFBq0htw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5NHv9IYPeoZKwKmPOg47ogAL5qEbgyrp4E1N5l-5Wg7g3eRb7Qjf78_-89YDGKn6sUD8x6HfMRzCcYW0OVzBpBDy5u3Fyp6NoUV2u2lQimDEEWJdiho0fUTGw1k_fX4pVHk7SRlTtdNIcFiPy-_Lb8lW7kf4wVAzjQEXKpkI1t0bLFwOy9YrH9sY07xRYjhC7c1UZRuWZgHHCd1cPToYfItCgKH9TT8XlYObIzxfoPm_SclZMfjlrAfAM-1YoamHFUDMKdn7jy5R5lhgJTypTfEdDpcKFiNVZ-t-TqnI7N4UxdEZQjqvcqqFHB77tqMfA8hMeU-9tB4xH8nU2-mzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26422">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26422" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIsB7jquU96J3jyjujVJ6iOGSOQM9ygj4oVlAKjieGSkFXEzkzD5TXGhevU6wF4xMR8YMUnYuZ8M2WlzrhbrQGmhuORq72h1SrhBICLnbCv7zdox3dfZ9i0XyWNhGQbh-is3c4z9DO5mAeP68VCxBpKtTnRJDpuwiHl0oMvoSf4UtjqmAM0zhuHEcIL8Yx09kjWX4Sd-yfW6z103fbVgpJ4etO_ZdqxKrHws0o-MbuVYrGhmx5TTUcyK1kNu71lSLQRbC6IGN4q07efairkqZlVXJNKHqk2u4WR2_sQQZE3pys5Qm0Gy6ZrkRMvmUXDnU5umEGM4LL5aY1ZYHoVMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTav25USuVgu6v0ffuPu4cBrUJLXuqT6ThsBmF2aOK6T3_FxQMOYERH8jmNVT5-v72kaJCpK4yqYrkMa-9QAWnBTiAPEsUqWveziLH4MQv-mTd2tPqLEaJy6GxCfenVqCPXdHo3GRQsMSfi4dFaTHOJkN62G4phYVbgwZVE-y87VR-w17AHeeD78eWJwPQpxSOC1hLbq0vihtcXAxN05uZ5dvSkinMKI1cbuQ1ojT89jzL-5AlNDGHlSzQUUPd1_N4fvGu7DOytbKMLo8w4gFxf0g3GazabVqKYW6OnH8bDxsTEdOkC_IhVjKuIyHLluHIouLRxJFyMi-elApm2srw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbyhI9-Tn7p-IlxbP4DcL3z-j_1up07y3z_rrxDlCXi7G-tdFW938dfI9uLSavCE_iNzMDN1_iGOnObcxWIppOAzSucPvvluNK81U2ca73YZkEnZA8kk7gPS12gx94kRfh8d6kpWKaNwZ71hAdpr-865TWQT-DryvQeHLNW71HxsQJc_78cRrfdBgdz0cAPx93Pu9nPSZiVQ-mtzl5RWwtyD0oSULH1sbrYW3Q0m4uiA3FyxJptu_HHzpBoLVe15z5suVRlCTF3uIwLZsycHuCRMCbgOl4bbSsopWlGc0dVfEFc5LM0Tk_ajjalJwO22ZlWxJT3ti5Q4hhK7WZnP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZUOaCr4z0Dg6mf2axpnEh9D1uEP8Y2etL1BhsZKYva4PjyG80qVD3NkTVbnWPIDbbAWfbQroMJtgsrf0chS-Gt-JBLyf8wEQr3gkpJEK9OLOvjMy3_svCVhpr7XLFFkFc7xe_0PUfFdcjICWSiAlQ3XFI9dpbHK0KN_UcMA8LkUPBaufQD8N-WCNYvFz5G1LXD7OfK5uQzBTt96R26ZGZW0z0rlxtWVQiAR8UooBGDKRZua8Oanwo1I7_MTdB-YQ4foDmgw_grU7yIa0bzSC4qWO3LomfKvoUdqhojqALEWgwc8hs24pF565mMn09nm3EO7nnwnDUgYoqCFpA6kOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoOb9gS_DojrErMGlHwiSzi7WN9zs31oQyWVbhN5NmOBt3wk-kQCjeodQf5XHE0r3b4nnC3VhGWyB9U4yxYpJcKDBXwdyvNCXIA1f1Mi9rEuVSJdBSefV5lKpXATo9AAEv54iynJ5Y3j3j0vi5Yjzwfmj2Zq-cVOolMde3zOfr2cvt1mV5Nw75ujrwTE1TXtGvHBgpq6Da2Jp0F3wE_rkt_NBjynDZ8thN4FGiAryYeD07arRU62OABvFLZlaIvfWd_iz15TGdo1OirjCGEWj1p0027B-nNmPeRdUcQfucqT1uWKtGDad5vtc7jIXwLMr50gCVwDZi2FlE4Y6PtDyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiXDbJl3q8vE5-AuA1PeDBlzYFt-VB52nXiPa5uPZsiRKYwO5a2EtE5m6W41KzgKLPoh4fP9DfYk0rUDtH2dsRGBpKo7rCiB7-FBtEelajYFL4teBuSGBAomBB8Koni8xAEB3rUDF3dpnP1LdqZfiqpZTmndqP1ovcWpSILF0pR19ihrEiSK0rteQQ90k4mi_ZmB_5keHMMEBXUdVwbgSzjmhlWHCJgBkV7P9JQjw1k-zTiMx1yKlyEEH08i5VhZ9xO9U9_5ox3OpdEBTPve4O6ayMj3KAjHbgF17QKFX0kuTgfYTcZcTGSDdRAHZhJzMgmC3I6E_CH3v15iQ7OvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD2UszrhV7kf9GDkTX6XNmpMivDb2hR4O2DH-l4yU3dIdyvA39rz8NdxZk-xeFRy3DJpdAuarKM4d_94UXpY21PeoBJUe-0gc38xIwS79HlHSwaqrF6dXVLcioWoPMLM5K5GtLTzlhAF7B7IWNuOH0apOH0gLQ4WBSHd6W4FqGywdzXGKOvbVbQPyb4YSL4CfUHv9Og7hbvuiPqhTKGschkEnUPYaLOjc5KZY26OxTinVjTAJ9PW8_qYOgT8o1KY3YZhZGT2aGPglySjmzCWKLYmlPFhcQYvcGITPpvA6ouKWhD2NEYAhk96DHs-9tBxGX3y2TBvQu_JY283qts3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuciPhIKjlCCY7FeS63jT_CbB3mN16eSgypRAMJ-5tr0ymW6mjeF-brwDiTQ92kdx6bDFtiLRKRSkcsACXr7iuyJxfW6as37d-2vXVRlgqriefq5l035U1YC3Z9xHXZneuYMOlkRmV_YmCuDRIIHJC8LXeVADtj5DJABL6EKIKs2gTWv19WyZXVRo0mHWuJw3P9IIITH8i0mKBz3uKfN8ijCvjRkNYW6vMV7SGCfzpILtCuV2vj9D-ImiideP6jlLa2DfZzHgAC_pkZ8-AufvlE4ndcIEHwAUrPnAHLI5bmrhbZ5UAEKkAGVQe5XddA0iiGmI7LLOVh9Hgw5XsNLOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giBbqdim8EWNiCgZ03e9vAKwTcCoDbgBOGj8TzHE7fbtcrLR-QZaxs5B7mPH51Sl3nZVC1LKuWS-LSmZ5z3961H4HVaC_H64P0YYkD-oVL1iCWNYUl0jjufP_kH1ahCsGWnii0s-qDEjmbEIfvouijWkWMYv--v-TqH8NGy7ZUyduLA5AriaCaVcP1Y1l9cJGK9luvX9hdbzj6izwDayUiLF7IDvCHLxpophQJooLcGXfhnc2xPc1oFMwHWULMHpnI3BwAxauBbW23rYCBX3MLkiLeJ0nIvqUgI-yN7uRY0Z4QaVXjR7i5TL-rmuonm6104WSBu2xJOvAlt2iQZdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDtAGcEkVPysxK9gylKP6RXrelcPuqRsLHXPTVGk-7xCyGUGfnt89tQYKWI9DFgd7parb3NkSJaKSKEa8BWaLj2rVBpt9V33jAqzh5PFR8ANAKkPUpZqKib5fmaNYKDucoIqpJwppnHE4pdOxi5rdkduUoNlO3kMGa5rPRt8KvtjMkuPajYbYrBGvyft4NJuQNZnbeKGqU76BoSBDskVPuJIN9U_D--15aK6IcDupb5S9y7oX0jlKNooJiDJ9EEnp7ijrC33CZEGEi405HxfNUa_VtI35XB8RGvB4135Waj2xpTJ0tQtpEc1o1cJUI4sW8_VlO8HWdnsyRRe5-S-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPSadOzHsud1uBlpz8yxrfLVBkDKyLz1dlL-oKKvMy2L5pxdU3Xa8_CO7iCJaoxXits0eBbAGPR-vYvc2YokMmpnRvT5LtJ0DpMis9xclFtHRUEehQDOqz8kXmtEAAZoADEOVe_C3fOuukpknhYscq4OUKoeVNnEWjNDjzz5g3C4eai8fyNc2H3V31J6yMKhA71HKcVM-m9Y1CbZKDOiIB97lsJi3TsMnRyeTlsZIXja3YxDi44RkNPucKuFDWFAF2ZuUgxtESi8QTc-Xe_96TTH-2WSfMUdjPt6Y2-yqtcNr85hdTbsMjkNRCOmldGdF3rBUnPQjlh-AtudNNEP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9BjpzP4y_m-p4ObhLLTa1tv3rtXMmZ4kOfKKwJBJn9bg83aeA59211QP5AQ2VqqWJ9QQJ4bpBjmhGVzTNrsfWAMWxZNaj68iDhy0FrNI8auWDUfH82GuE4fOf821TVbqgYl0yzocZD1k7kEdvDsFHNY0Qmo292CqqzUNZgW8VuwHEs0iT2HJQV7UbMVkMRkAwFYEHM28LaWsNpBiMMZKtdl6nWlg_0SZl2sjark9TBKvp9xkWr9cf_nwt2R3x5c6Ime-vyFY0eVfONRIvwgLi4KdDinOpjyhGU41SEKis-cpYDz_tYOvN5n-YFWsLkoKSS8xvTF3tm69XWI0Frrkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKj4tcrmZ84CtPkc9YXs0ZvDYGRFP4fMjJd9qjf7lElrhBBryS374sqsX5stuI1kX7VeGYqLv1KKCtqo-5Q-6EV0ZvQgjw4tYdPvxTSECNKV6xgX9BUHAXP0FkP-mmU_hhkfwiQCsBY8NZaoTO8e2jlgEcgNH9ZgEJ35U_Culdq-8RYLt8x0qbeRvrk0di5OFuWAR3Y63W1o3WvU4dBA_HPi6b-qFDQ3HHAjg1TtihCdGMrfw6ZMXj9-zdYV7HsaEPKhYn5IHTsXExjASC7Bu6jpW22pEJlX2gBYTIVcmWuIDPYZwOdEAXSz5P30YQbsVJVTxVv5o9nm4ZTu-Y9u0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj2KPsec5ukmjxLHlh93UiTR5GEsr5pZeNMvIxxo9BIwPboywY1enhk0Qk-CQkOdq6tMmy6QB4ql8LdwyebtSB5_HwMFCapZ0Isa_RwlQjTz8qIMhLNAj3PHU9usegKXfMg2N9ox7C1OUq5ItkXMQ2QPFUglotQGzz5c2vST-6GL76NLqMlNWeZper2YD6AQv57DHItJRpWgfgJUk0pCwRDd0EyoY2qvzWRu96Sor3M2wsGKcHHKCN6U0yzo8N-9WLjGlwPwsdKIDz0Djo-GLa4po6SLrE2Unl6dVFHEDZ2Ty60fxjxt-dgNuzj9wjDdlQk3HFjIdE9M02_57tJGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPPlrQwYJFL9Px9tWoUsGXGadDncsEjouf0om8A0kw5RR99gCrilOz_wnmjUXnWmnn6w12JWfFASUcifyOVQckxgISJCqUHlCSn2JLHYTlOxI1U5JcjTT7uxb8r72_d7wF8f9rOc4q-HC5-pLri7xNWXTud0rak8f6NLdBr5jluDsF_ArVY3R5fotmcueFFgdyKXrEkFVyhGBzUP_XplUM7jx-WO2NxqZq7qCFcP5HlntJQpmvzWHuQWIUmH-HGDnI0vMhsG62EXr8QeuKnsTjgJ2PGbF34WbSz21lNienfVjYzsl7lgJSW4GIx70fLyW43fdBGQ1ob1dGKFpgPlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXxJwX2SwdORaxW0tz1ywexX_pQLpkBjlBH0RufOVNnX1VvI6km5eXrncdZBrEkq33X7e14hk17xm7p1NnodgekKhzadt8dNg9vblhBCs3wihT3JjPsjFmsfseUxnh8n4iHFH7BfDjwxbXxXzCWfaaPFpzbIt15z_-3SK9KnNFLlXCMEhrLat-o_6DknyQuuTJFfcsd2c85XrWTxS5Z-kdDb6ivoLo5JJAgaOsbSZZBV5cwWU5kP5E00-NnF9-Y-9sjcj_l7o64LZSDh9QQZTQljP4VB8ZrefM4NsCXyOtpc7_WRWy_pY4Tna4la4B5U2_U5pUvvdtV2ASE-xR_gzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFeZECI18TXggwbb5AE_-VxVCarucB3dv9dTWRa3DTPMY6_9diDxCp-tauBmP_sH2eOayQ1_Ms_xGy35BEYEMqzjCI-P87P0OcSTfW3U-7xlAp426QOYkfj-XpT3_a4sSk964u9zXc0fhcakIGRCk5vRmRvRU8ex1IBo5tTtZzYVO08zfjukMV7IYxwmFrHQiiyfVZathfxepY6zIW4W5zM4XfVgsMrvZZWUi11nuSJus4vWwh5HH3sZ9hG76ulACixKKew94kUhUnAMFhlLhHna-b1aZ0p8BWb7pJToJVDnutYIkQm2Dk28ZqF-0OnD55UzxLb6W4MdmOd7LeRd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=DCTRFFHWkvExDKoB0e35vfepMFfJqfBIShg9rIeBJ7yMsFiLpmmZqFNM8y27jL9DZZiDN9E2RODqW4kWrG5250yYrGAc9ZbyDnZqSX180eT3aAr0-Vv8kugV2BSreWkYcZxWSrDJBwiNqPzQmZUrirQWgscq-L9zsfiOg9kkJTqEZmJiGtLkroRnkjhJM9r_hWT4-EA1-5ZJ4vh0zdz7vg3wI4uBCmUgAJebJr3qMhKX8kayG4QqmHo40A8gXTM58KrfLPUD5MsXJh_PdGY5YPdc4tjuMOXafI-yqaOH7w8NyZGnXBFu51YmyUeH7yWuJCo83JSYUG-kbOX2OMQ9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=DCTRFFHWkvExDKoB0e35vfepMFfJqfBIShg9rIeBJ7yMsFiLpmmZqFNM8y27jL9DZZiDN9E2RODqW4kWrG5250yYrGAc9ZbyDnZqSX180eT3aAr0-Vv8kugV2BSreWkYcZxWSrDJBwiNqPzQmZUrirQWgscq-L9zsfiOg9kkJTqEZmJiGtLkroRnkjhJM9r_hWT4-EA1-5ZJ4vh0zdz7vg3wI4uBCmUgAJebJr3qMhKX8kayG4QqmHo40A8gXTM58KrfLPUD5MsXJh_PdGY5YPdc4tjuMOXafI-yqaOH7w8NyZGnXBFu51YmyUeH7yWuJCo83JSYUG-kbOX2OMQ9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVHOzKzDecoN1EwDMULlTIVs2UBhlayhY3snuP4f7qoW_U3xSI1T3BMgONtF3iMpjK408KKuuhKcf4Jw339ONrmwIJ9ctRQRmEZ0caGTNJZMSb6LaVEM_y8bVtQEs0Je17kVM9s3mRAHG-vLFkMjmgYnpHH81agKArNlH9zHi_VrYKxIluNIPoVgUBciM-nUw-3bkxNJkPkua-WVe_q6KbTX7iVMkqoXOUAXTUx25CFqWlQw4mgSIk_ZlFYpx64SvyqOlVkXSxIRJqu0yVjm6jhBsjcq3FQNalsV-PEApFeKtJMr9RVVvrne9ty6BxmBMa2qVDlHDWAsUm2-rPioKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neHDaMSgQyURhOtYE4RFzLoIQXfl5b4o9lxLjjTfKalXHJ5lHixek6DHyB-4h-Fi7vW3mxlM-qQDQyiiynlw5g8akRZqur6c1W8WeIsI0wAMNayCE67tFZpbXsunogi2q_c5VjoQ4Pyj9OvKn2zvkbkOrPY_wIFQBKOCSBn88a636VodG-gfEqtHX7ALuIcwPp7KeJhRoBs3ZX16MsaDyoEggTa6P53MfQ6xd7AGWrGpUvT74UBuoqlTkDVcyG_RUAs3B4JLoePbwXQBKzG_u14nMYibvYmtggs3y1vy3Hf3oi_-0y_aBR_rLCzGxht59T2Z9JLsXCFSr7AFWB-LcABw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neHDaMSgQyURhOtYE4RFzLoIQXfl5b4o9lxLjjTfKalXHJ5lHixek6DHyB-4h-Fi7vW3mxlM-qQDQyiiynlw5g8akRZqur6c1W8WeIsI0wAMNayCE67tFZpbXsunogi2q_c5VjoQ4Pyj9OvKn2zvkbkOrPY_wIFQBKOCSBn88a636VodG-gfEqtHX7ALuIcwPp7KeJhRoBs3ZX16MsaDyoEggTa6P53MfQ6xd7AGWrGpUvT74UBuoqlTkDVcyG_RUAs3B4JLoePbwXQBKzG_u14nMYibvYmtggs3y1vy3Hf3oi_-0y_aBR_rLCzGxht59T2Z9JLsXCFSr7AFWB-LcABw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xuf94N4FrvYke_BWmi3pYH17MAH3N4bb0mhNp6njZR5N_NydbzAoPQY0_UmwiiQj4_SBVdxFScgUvOcvjBNcd2Hfw1N124Zf0fu1XQGKtTCk9ZmTBgU9mffEI8Ysj-1WVhzy9-_St5MRkykW4N4ZMyJt0yjQAg4UpcjFET9WnUvSDhgmnJQYeuOmDAKNrQ1bwSxWQ12vt4keF4O59bp9WKFYJD-epkqi8EpXGPKQM3neGuMS3geXj3kYdlPaJn8bkbWKwEPIEWwiPIRidGN93lHEvx3QGOsMaiHAwYOYQY9G_6eIrVYtLnBdFHRrjWFRSzHlhOWk18Z7ypXcDqg18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R84caoE2J19viA4yw6qagicVYILokBDaGmONpOuSHpuYtTCK9bDnIHeAY24rXqqIMY29kH9SXLR4vgssk1CDCVoMajEsrOoKHx28IlgKR_PO6gyK6QcojOBhqJ8prN8hlrPdlp8g3y8us15HxLjivTdpmUSirtPGAGrtrDOWrs89Zgrg7IQg_frQxYa14B6kvUjoE9If2KunPUBysmkW_yG1EyUCnyF0e6ZwDjt3JVh_-JJr4WKIJxwOiAbxwEFUAe2lHWL4_J3wRr9G4ydSQSOr5U8_M-1ee7tViGZZv95UN_v2KLGyKqGt0t-ili-o1qHFitOdtcGWXYKEDRhekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzFDWYdT3T1siHUwLrFHAP8d_UmkT7WjWu304W05E10M4u2oBTRAB0AD8BjLxNXlRCLbPU0XwGO_u8lGM-JRjOKt6ww5IbTkPt2oJzWLl4cY39U112xkVghQ-X8qg84hxflrACUILAgv3qngOuQY9xNQJqjfeR635loRgx9Iy1xX7BjUrWc4NIFEmv4Onlf3Cd4q49wlT16nGL6cm17n8a-Fh9-tBQecgC8lUq9T65F4QYPB89EELR4pvzuxln3qze8Yb9KA-mmSQKKMgHvFKueR7keW8YbO0JCW1t_aD7lqxTmzHwZU3jbUhltP8QCZD0oVg2cDdKz3Uy4fyo3dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFFLRXfUlWHqfC1SisCnd1MmzZ-7JFqZGUlyqzVLSudPY-4McJJo9bbFeG7lENoZl75Fgqxsasshp6R1CGjeSjmFAI4TssuPXqmnv67SyCffUHdIJ8bcMUcHVgyfzeo1bV3tvdGbWt3Ka5jo-XeR8nYEdPpMiBz_uJyrLJwO1xkCKVYLZcaCe0DfhSAYDMu0TD2VJOkaO8rD5q0rTetVTltDJcgFNow_F4cV_8CWHtfF6IZKNsLg7-3e1tN8ltlVC7kJl4vNqnMihyLRYfchDmJDc6B4R9OXUoweEKBcWCn38qcbbhEasCcVtxCI_8iihTN_faXaRPP-u4ojGtUGXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7zhA7kgJd-taDu3pAUkXs66RkFV3CqmsR2tQgnQpym_9EhlC5cQra6UwHlmiQeA-pRbuTeZpmuGGKpHb91R4vlTGiM2v2YQZw-6zXc5cHwyTler40HRXB-3i-caBh2ln8DH9xPiazH6zt9iKC0bf8XySdE6IvHPGjoRELRMwaykeIGxXHxW-g53ZZEOfhnMZTG6G0pAY4QZINrMwtfEtF-Imwge9U9kYt_wPJSZnHP8Vxt4U_-xnP8XZHckJp2UdIA7RQfZ2hBEd3341v7Uub0cV3LdH7gLiIzxPlZV69wDZ_TFFSNlAR2O1lc7_xWTijafID9V8BMVwlRPietcQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqpc6fvcsBjAeR50DX7ojbE9ZJwXHegv2xdh17fCWwGGoi7iHafbOu1n_nfsG5edJ-cnX7unYNIva2r81P_HH9shcLbV8iARhVFL7PfhmwlZ8VtLRY2op_5S9-kuJYDPZNhEtnXVhvCVeUEK-ETef5NYVPAk9MlQKP4h56Hyqgen9Wfnk20QLc5cep3NTw-wPyPf2ETOZ_x5qXcdTjLvum6mazApCgUzjnCR87geUID-LkRBgOI5H2atcRe09_ZBJVayhIunzrKgHVAiRU7im0TM46k5BpnFFoQvf397bigOVuPdFO83gCSBTTbOc5DjPHOTMBjDgbBVeyMurq1mag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0L7k9Qxvm3iXeHRPZe0NxYeJGVldoWYwrYbxXnz5unh-SCTspTUBhfA0yynMDAxELjOeUSldtaZhTKhowEmsETevIq0onTz6lHZ83Ki05FoEskGShDbp7KI8TUouZwWjJbZHEIOOkMK4MF2Lwlo_ch9uZ-7Tfe1eSev52bJw66S-6EJ8dj7Z7-QeguKjZOyb9E8DyA76Ro25HQ9p7KqYKHZYCSNthU2baBvloDMg7cF1xDHSAujhTzhmC-dGVT_NUewM7IPp8c_4jYZQrOx8uvouXKeUqx-myP7yhJQhh4555zZ3h2btH58uY32ITRU0twppioduM7BJFHxuLUcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCmjpnOEK_6ihOO3DU0eHY37oH_AkO75loU3-ceBZBsmO7EZQJvGVcedPpf4c1NldRl4AD9sIgQ0W4jw6EDcDbwve5XZmxxtb5QrcKVjTPQKAuoHN5jX4GQk8T5viqRApY2leAsI2VPlzM8mk8KeF1_uj6CLMX9mwZzy1d0UOlm8WnXVOsTLmFRSFI-a1jKt53x4-HKpgkzHyEp5az5PX_K-8j-RIFkiTiMvcIoW1-odR-mr80VZx29f_HJVjUrILVtl4g7LJImj26R-pJWhycKATdDiSaOaqjNSezPLAaMZTRJeztGRKn45hZmGfHpAtq_D2954XVgVuz6MJt8vzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sv_ItQ6QSRjfXIvYPSjsPYZFtEklSwB878oinxaS0CHwW7v8DqDStuiUg_eYcfTeFiqaQr5eVQLXlyJuGnxsU6GYlgmsty00Rut_os4jDBx80LRZ-FOwOdJGMo3KUZ2DjdAlpOf5BC6UmXpX8sEZjp0_WWxbKgL_8Ny0WmdbujHRavTeN-EkAYN4tLkTglNR_t8Ovak6LDP24Wa6jZx7gqFmNoHgUO2yUByrW1fs3jZKGMTqD3A9IDWbgNgCOUoN0OOPlt4Bc5jUyOwlvvH9AnBSpfig3EGsW7iaud9_szCDnO_DVxIEByrP9JGMU5nmT8-PkNQNzoEk71sYOJ4s3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boSnjaT62sgCJZsT6I_NoGBHd7f4zaYdl2QYsXHpQTwWmkVH7xJjVPD_N8ZBytfQ2srez7ZgwTCR8RF96FjjXX_l7UGtqclkzWMakQSnRecwbkp0juVlqXrt6cZV7NjNCL_oNIp0k30v_jmGjor8LGcNJlfBq5PFl6oOvieZUhxsQ67s5uXWwPIoG_1JrNkqD62H5jfSMlSpUXr6Cer8Af2jS2xOqCHNwHPKCP9uRFAT8wKezXh4F-s8yfWJZxvhelQPLc8be2Lc8nEuHMlJ16jhPr7yu3dk0igayww5UJnPXRZ5rmdb1vRjzAb_MLatEEzUqhPzbruL6DMqjnHXUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkWBIsw3UOHdOgUmm_oNcvW7mdczVuCBqKKQ1-LA2ZBIKq9ylhALgWoZy0iM5BUizqQ3rh2eBYwm3xkr68b7o7twMVBIrV6j6mIMq_keYugyLgdFPbUBDa0v9yPHpHdoQBz-PCe5qxpnHtw1mQ2P6d79xG0ugm1PLKdIERpzcUi2lIIbM-Ubuaq1gPcncZ0AUGzR1mgOgOPmnluo10iO6t3Sa1dkpg_zZLsn6icaycB9plcPVkO1a8yu8_qQ53sYLWdDPyuN-dEbgQW9ZKuh22p6RkPxjrebaFzeAi36lsSX268Z3QCoqMAE-Lv8HUbJEjauJj1zf4kllIqGHK4D8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pza1pWPA8nUeOXc4y-p0qJZw-Ws606LNotqqpDZiIzjACQHQTyik08SUccpWSiJskRqcqFq0agSaYSkFv_VNVybVoUYRt56dZY1Ic4yRsvp3fzvA3xTDBr8tacEr9papSzUDQj4RoVIyxtJg7mNeVWhU8qX4ojJTFXIPXRQ0RpyKKY2EOSKOkOLOBl0eOBAOSz-Bwb-_oGC17lcazt3_hUCE2i5exhlD-yFz3v3UxmRY0EJd4TBr2xnIZkaw9lxKiTKwbVLmuVenj6iI_1oVT9pvGDWQXPYTf0dAKOcmO1O3BIxP0H8vXGU92P6VF4NRTRUlY4NPCY5aYmaqjuVnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhMFAE5X-Gh2c1dc3TBXwzBphxx95snpD24FWQOLswwvPY6DM7Ft6i3x2lf-aIInkmLjBPcsJ9e67eL_P5rAiSdO8-gRilyjIfRTSH_E8fN9KcxdhxEGd7JkwBiGxaMD9pqZTTCk1Cat2osA1phHaeAHQ6D2tlOLYOnc8xCbR3mJGEeUInEPyNpx9P5qsP_Cm9NA5hqfUkHWjNTYSNqOc5TOUPjRm9tRu4ORmwUF4epLYAalNp_lkvYqruRvTBhkkxzwT46rkengMfAC2NZ5Kiz-urxQLx18Ta6N3upT2Zigcyr9X2JHlQdiuq3DseqK8IWZmtBtH7MjV0tizmYyTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_n6WD9Cj1ZLcr14jTgPeK2OHeTfS0-BvF6u5JYJYUkT2HpYaLkmsf6cwn4SXTyFQsHX_Xu0iGSZaP8Q7cpf8Tk3z8D-BUuxDpyvbrv4-lR1Tb_8B7Sj8pYRAajYxyJWl2XIb4EaFvmGBhrz49-8MMR_uyGGfg3_vClQY2i8a1_LEE9OSq3g6DwS1g83ntHt7iu7bGlemo1Oc-NGZrHoqUcTHlGajWHVxRsOEd7HV89aRnul0XC_XnvamHP_8mTr84uHa6E2Gk9GuiZlkWdKoZ4PfGjAChMzeva4oQ9y01B-eXwopydPWrMCpsVPpPv23KfQNdX6ftgVhikRfr3DAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=BYdTZQ6QeHci_9Cv8-F4N0_27efpl8RdIo_W3zM9scoLUO_A2tKqeGvLHzJW0lC4nXebgOQXWeO1PdVA9I_8qxrcHh555d3-1Op-LPR4EHt3DU-_GohN0yOSWGPfgaJn3S5Z_j81PZK49GymE0-sNIUPvXxUDzoNxXuQuCzanLwkL9kv8PWupO6IqHbOpe0NFKDgDcz2etDRjhfHIWixEtZQrc3Ec39QxV1Y4xLEnG8fMBH2BxBiHPl785VMWZKLRszNJ5-ilaaE4vxCc6nD24j00khi6PFc9bihhJk6Fyl4r22tdJpqtUiqrVcXjkb_boJA05eC3oWO2kPbHIJrjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=BYdTZQ6QeHci_9Cv8-F4N0_27efpl8RdIo_W3zM9scoLUO_A2tKqeGvLHzJW0lC4nXebgOQXWeO1PdVA9I_8qxrcHh555d3-1Op-LPR4EHt3DU-_GohN0yOSWGPfgaJn3S5Z_j81PZK49GymE0-sNIUPvXxUDzoNxXuQuCzanLwkL9kv8PWupO6IqHbOpe0NFKDgDcz2etDRjhfHIWixEtZQrc3Ec39QxV1Y4xLEnG8fMBH2BxBiHPl785VMWZKLRszNJ5-ilaaE4vxCc6nD24j00khi6PFc9bihhJk6Fyl4r22tdJpqtUiqrVcXjkb_boJA05eC3oWO2kPbHIJrjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYo1eZ0QSxLlHfGRYca11fLJ2XDQpwZTMqb2PL7admv0Ruhs7O1KGvyGI6Y7wKK4eipJko5Hzv3t5wwkiCVhCaYq0sRPwNZAhc-XnqM4Wqv-bBch1kTkmpr1xGva5DJNkQ1DwiTrqCCp0ZdNobsor0W27MIV-n-IsAxUaIz3rvQZp15XA4_S_MYbIGG-4zRV2nmzOidq-uDijchKHck4VYY3I-kiyDv1ON9SI0WV57YD750d-FwhxTvlDiRQfCZEXCl5lbFwBqvNrmJD3VcZSLz-YA7Atpu6WzLVCqd-Cx72abLL8YKqEklAvEB0g4RAxyDJVTzLKV6uemHGrATnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8h2f2CCQLokxUCciq5QCDO8pF9eR2-8Y32-wYbifRIkoJyhCvt4g4vx1laRvLossD7MkiAbAVoaJM-CrN_Of9RAjsW4l5RJWy-Ehpl6KsJGvhpHp6YaXXBusdll8rEzy3P7-FXSsbkcCMS1aQXizxRXr16n3O7j_kO0_pqo5RQreZa3vG9vME38O8LNDkSSUghcQ9awXrN3y8u0OI9NA5oVE5fuIXNHUUIQSRWvig81t0915DJA_h0glJeHlb-lJmuTHSKwrRs3qTzR4_eFhrSIJM-3hVvvINSpSOhoBjiFaYYx4GUDnGuS6b8hr2O7BaQT7WTtOxvm7yzkbqgS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIzAAT98qLEBNbxDJFCmVycgla3aYF2G9dlt23v81aRBFmld9VWj8p81C-xAZEInTHy44eCHWQ7bpLAyDv55W8E70t9JsHimdalbCXVbOapR53ujNTFrrRgf3Hw4PAAqraU0cCcP2O5ktJvmWBpLJOS6v57u0sW0Tf_dEfnX72lNsLn8xx6Wvg0rhflKMbpIUjloGbwl_MAZcWq8-4ufdToBG0EcJw0oXjhtr84qc3d00pcvyGdRkUHn6rBdia2MnTwnYPxueOXismec0IwkpehMe0P6-Q0sxV2hXfAMGF_DwKsxuSu-zEGRs6BQFckMXJtPDp1M1jIhlihcZQlXMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlpPV6jf35mx_KxbDNZlyn7KCasshhq9d3EY4iiKrYGkX9I2iNtRfIx6U0I1-sTE8ty47MQoE6GEuzaYtg0ATRBOKUOmPSdTPj3HJJWhXPOgQNmcU1BxQrkhLcevz2qCbXE3OYmjbFcKQTJEONgROHyHeAtW-_Jr9-9mMPBuVj2q4RZsh7D4L9oQnRZXAv4MeYpuqb1r7EB0q4RMaGJI508lfAlEbjs1-eV269bXSJQMjhs8ZIeOZovck4jIaFCVxryRgz109c_IylBIPcZsMQVos6kf3j8zggOXSsxEIyzB0vaVeUVW2yX0NQUVVIjsGp7fMQ88vIH_MAhV_QYVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=baXTWnJiO2_jjI2e4OwAYSl3Xk0xxGnNn7AVj3L0kwE71JsMGKaLRQZezzu_taOvSSYAQ1UQxKKx8QavRmPhigYqRR0nnKH7KT5MZ6om_Wiu-rv_q1To2BCq9v7-V123C-wxSrNsAIVI9Ym6Lg-53Z1MdmMLOIZPiLOBGMKTfWZty0sYSAvXw2wekyiVNvQ3D6BFDmKvSHclPRnHK2YYuArozH86EK1qqsJfIYsInagz23wc0zL8V1ObxtBU_6uyAtLxYRXY8Zn0H06b7ziL2Bf1k3AeWm75gZAftJO9Ycq8wZUjIG4261boMNOHARDCaPp-yQ4I0n5iHpzMBCds0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=baXTWnJiO2_jjI2e4OwAYSl3Xk0xxGnNn7AVj3L0kwE71JsMGKaLRQZezzu_taOvSSYAQ1UQxKKx8QavRmPhigYqRR0nnKH7KT5MZ6om_Wiu-rv_q1To2BCq9v7-V123C-wxSrNsAIVI9Ym6Lg-53Z1MdmMLOIZPiLOBGMKTfWZty0sYSAvXw2wekyiVNvQ3D6BFDmKvSHclPRnHK2YYuArozH86EK1qqsJfIYsInagz23wc0zL8V1ObxtBU_6uyAtLxYRXY8Zn0H06b7ziL2Bf1k3AeWm75gZAftJO9Ycq8wZUjIG4261boMNOHARDCaPp-yQ4I0n5iHpzMBCds0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=WJOR5HavalNHlOvvnZrFVKFDd3QSnqViPnmwSUevG-0rS_YCpjh5FXgzcWtsEQTh-dJ-G3MKr-T3vfIWI2fWKTkPCWh3bcKGIchh7DWMvIp3ZMuSahdqTTGNBsaMzBN9AAG3Xpzj6aeN3MMtR5x_K5Rl7D6A-aPSXublinUORm6ubjfo4_XCD2zv6suJ1OGiSCUTA2Sxw41QNEUdWr0HuFYxxQp94_V8vjGy3W5UKn1HFRx-7izrpCmQCj_Ihdib42V1Va0vi8rCxpdjhvhTOuAY_hx74wr0Lkm_tQt6kyY737vNzzBzOIdMTCZUJTnfYnsqXcsHNk6EexksYnfmKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=WJOR5HavalNHlOvvnZrFVKFDd3QSnqViPnmwSUevG-0rS_YCpjh5FXgzcWtsEQTh-dJ-G3MKr-T3vfIWI2fWKTkPCWh3bcKGIchh7DWMvIp3ZMuSahdqTTGNBsaMzBN9AAG3Xpzj6aeN3MMtR5x_K5Rl7D6A-aPSXublinUORm6ubjfo4_XCD2zv6suJ1OGiSCUTA2Sxw41QNEUdWr0HuFYxxQp94_V8vjGy3W5UKn1HFRx-7izrpCmQCj_Ihdib42V1Va0vi8rCxpdjhvhTOuAY_hx74wr0Lkm_tQt6kyY737vNzzBzOIdMTCZUJTnfYnsqXcsHNk6EexksYnfmKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIXOU36KUEGd1vGrleivVYt4pGfLhevz1ISHTCLVRDVFp0cWug4wVaDY35IQGWSJnTJUsWQRlnFA5pCBgK3w6P6STNHBTmMDkmqHyzDTtQeAIuxrVTLbi2Lwb8oTJJTfYJejjNsfhNMLwQibgkSWAukGBFixjjfaCNu4RVnu6K3OqirJXM5MUuYYVRimSWEL7iabX25SfCzWL1UI7u-E1VTMJ3eupiR5JD7DIg0lh_k0IvefAvdHdLNLHYZSnb9ulT7td3gU7G8G22j5M9u1IKjtZ7yVx3F0gs4S_Qb2PoteJJXnIJsYaegxLMJ6m1K7tuAHvzVN-TBKE5ccdcrpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKStAspdAsZZnVeapHGjqBYmvnuredo6vWjNKQlIYpICvbIE9UYq2RFaTWwfhlYXDs0zgSfar_gOYh_RjcOGA0UQsZ5fpqFzrGTAjCk2j-Jizx8v442Frs1mT-ehZptx0HRVxSm5ixJ7imbe6dk2E-ebNrZUDLgsV-uqZ7lrxmEOBkwIFXLtSRMv5g2GW1hLfD0c18IPgGZ_LTsME6DQWCNSdmI6xOg0FTcpNTXcChravkxweeos4Q_pW4PsdefX88x1Wp-mpdMc9CPV90GRFLMfY_YA44tauc3UJ3t_fWufi1kP5B5wEwloK91qkCf_xnOA-lIBl6uh8Y9TsaD2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOcAsfHmP8MPbHQk0z9e5rCeBq-rS-N1kSN833ymwCwrKZQFk4BW7YjzK6ADZB6ms4ZJDVCVoZdIoTNLq_RUVEQKH6Jpo93CvnAgfevyN70enof1s-S-t7ZBVNHL30rPjSV_zx0cjZXRPPaONCAoO5d1C4je0WguBUomQWpld0PtvOgcelaBRCRWIsD4dDkbhRuaeAqSd4POcrvnS_Q9C6XMUqD_nZLOuLngwlMmHDb2iUadhMqavJ0Q-y_jm09Fvc6ZuWNfUKKTFMkrfcJOVyBt8nSbM-X3s4ZkoWzBwtU58j1hv-SfyvDz1haIeQQdBeDzvm2TUHSmlgrYcPXNgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26371">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGbxIIS3zG5jr3E5hpswufM4f1_vDbuK0polM0yR8wIljkYNTQHZgbJS2x7FDszq4DmfBX1VCt2tZunQm79nhHOuherPlLe5PtD8hqpsKPAE-Ne_C-bqdoVk1Z5G9IK7q6IuOVkpzLV3Nq_WCYDmnjT10PT7cELXdGR_5L-9HINaE23CW-ztaDIKmtyjnz3i0Y0VbVz5Sa4PWngB75vD16jPf-WLwY7iE22riyt5Hd1HCBIuSPOMHhCcollnQVrLzrGj6AXtjuXmQnW2mrp_RxEsF4r-0933t5a2odjAZSv4tI7hHIIKeXaAspODZPNkn9da-6MalmKA6btAN1DV_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26371" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfJJAeybN_8gGiXer1lm8j4Z4Z707QLGGNaLDDz1rfbfAL0slQ0UL35hCnShaOZJXuue_urBFDaXhLdUAyC5kuxlQTbyhbfrphNwkcP72mKYKrYWLxiVV94EmnXXj6AxL4Wt4blEUm-ms-v_WyDxolS0Lu33895KcrGmIPOz0o7TZrY6-tqaSlwUXjmaEFOHa3RPI0HpDjuP4iP6HEAib3L3iAEDssiXgcpDNX6o66tlvxmRQVMdEZPcA7F8SWBmpiLYIgGvb5cMGFE2WoiWW-VJyJo6GWnEAt3gZKK9FYAyYovzuNCkP0vAVl5mQh3UCmUKCMIA_HWUv4KOCXczXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSrp141MxZR3pQCdNGrzXjGPA8CS0TR4FFSnbcNp7afCKFZzjC2vyUgaGUtSBzsZlRVpGr2AVEcm-0SZ0Ek0J6Lm6nleRSrgflLkpAUUv7lB3YTEq7pRoA0R9adxuKYeh-oddVK0ID6x4ZGHm6HUiOCyJouTYy43X7BwhQrGsDXe3DAcb5KsUP9LN7f51KUQ6jdpvtkn0U5UNqpBoVrS9TyLtyunKgzhgWX0nnZjTc2e01f7rhhlmy9dNfK8ueobyGeDBb-uVGl1GgYssebv4b1Oc1kuOU2Q4Dl60IzA_0wllQ4H7J5cyd4GNj93IOt0xZNQUjNkMY83w6SBYZ9ttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojK8nsmAT4DARUI7TnRmBp8Ny4HaTTQkztz2Y1p0rHkBnUyADoPutFXRW2PChrjmrg5rRyUZvOkrwv9x7cX9eSEyq4LQyIGQx3WF20diagCYKvMxLtMjkOaTwgcJ4XS_M-zGwDAuUESjDi88rUCP2GR0an3KsnySV1xMOBylX5aFwRGT_SZEvvtBtQVv3ce3nStwSavCZUAEtuyYfTRTdBD4M51zG1gX4GX3iYNNkqw2EP44Xc5ppstM9A0CT9tgrY613fk3RPzHSTsBpV71XgLrqKCokohZ_0zsdr5SDUTzA-poM_RrsRiFFHzrQnBVIpxLqDypo9baPHqrJj5eZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4uO94tdBhbGRZH0UoTXHqiScgyllnkUJ7iRYPXdJW0xR5qaOVtVbYGEIrHyrEYjt2iBAvEZomPX5Pr_o6pk2jPYkS6t_V1RaJCFS7Gt-9uI3vXKjQDAnjMQW6Y9UHylctH8oNH7TW1N1XRIMhJcSmgtvSG8qWg5UhQfwqDGaL6A17y-Lh1_aTzbUfcH9ICPrL5jEPS6ms9b1AlvWYYvm_xMW04UgLGNI9qnVGDNp3qacVcipraUobBB6E_DcagH_CoaPXunZ_2XQZpD9wiDBlVVZl6DjKO-fgx7B1Sme3Jz3TxsuZgUIpDxvybEjSYN_IB3Od8XPKOfCVuV1MNm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=ilyOPQPCxvee8fgM_CaK0Lqw8sLnKZFCsk18u6XMg2d-tRlS8qE0BCJ4UQ-N8v7IzRmTwaLPSLzF9ZDJi8bluXMkmgBBQYcppFg3pxW9cNx2GsUYpiozMV4LC5cLQwuhIekJMW_tBHzwxGCXDGED6vgTJmUK_0foU0WA1NvKmBkcTLhjJ29YPF1z4qRTxlh5TEjbF-difTiUlcf2bk5yMwA3e1_e2-yYFg-ACEADAFBBWEtzAgjxrWl8IvTBqdBUHqmN9nSyCq1w63AIlRL_yg1Ix5dTnOxx-Lgnm8HACIjyR1nNnUMNyD0sZfCQuhWzA8wxz8qVQBekCJ8BB9Z6Z3rKJuythoZK1n4FdV85Vc6fN7Lr8tSIxCb-6P9bJnihCdoes3AGvy6v90Wyc6ds0v5oEa_BqqlWNalK2y9qz95HA1OG2MRh_cXvmP02Tph2i2Y60PbGWHYGzAWZHWAaI842GiaCC3bDNB9Gnq262V9-bHaThYTFJKdaeZi5pptYAehjX-_ihWEy8IPnz01KlMnzsKuFgOWHbLkTq8h5kw3bz6hdH5EORBiSZGhTUW63SKbCbKq4_Cb1FMOUb3E15cXv60Z5p9HXSfGU-xS57CMHVVdY8dUBgsPnvKKItuIVcN7eO08duNTF-jLsFruVTAlhjDajJVNvhJcoIB1FueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=ilyOPQPCxvee8fgM_CaK0Lqw8sLnKZFCsk18u6XMg2d-tRlS8qE0BCJ4UQ-N8v7IzRmTwaLPSLzF9ZDJi8bluXMkmgBBQYcppFg3pxW9cNx2GsUYpiozMV4LC5cLQwuhIekJMW_tBHzwxGCXDGED6vgTJmUK_0foU0WA1NvKmBkcTLhjJ29YPF1z4qRTxlh5TEjbF-difTiUlcf2bk5yMwA3e1_e2-yYFg-ACEADAFBBWEtzAgjxrWl8IvTBqdBUHqmN9nSyCq1w63AIlRL_yg1Ix5dTnOxx-Lgnm8HACIjyR1nNnUMNyD0sZfCQuhWzA8wxz8qVQBekCJ8BB9Z6Z3rKJuythoZK1n4FdV85Vc6fN7Lr8tSIxCb-6P9bJnihCdoes3AGvy6v90Wyc6ds0v5oEa_BqqlWNalK2y9qz95HA1OG2MRh_cXvmP02Tph2i2Y60PbGWHYGzAWZHWAaI842GiaCC3bDNB9Gnq262V9-bHaThYTFJKdaeZi5pptYAehjX-_ihWEy8IPnz01KlMnzsKuFgOWHbLkTq8h5kw3bz6hdH5EORBiSZGhTUW63SKbCbKq4_Cb1FMOUb3E15cXv60Z5p9HXSfGU-xS57CMHVVdY8dUBgsPnvKKItuIVcN7eO08duNTF-jLsFruVTAlhjDajJVNvhJcoIB1FueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba08rbdZuoqvAsjpHWAvz-1aCxPnEOkm0YlyBqHyeVReAQbtX5jJ_uBW1KADVH5QvZsozyZMmTSiKfwS04qedsOfwC69qkVDI7k7jqQ19fkpsK-VpsdP8xj2aES_8S3EGsGCI6yIErHA2hYROjg3yAcPvo5WcfrCEpCMYGNDDXZqy3zkt3dHhqZHfpjNkhFlEzrECG9kG5O9xgvd6beJ6MUZdJIyBefz2gg25_pS1FStpnEKX8lh52uGV56mRKtB7e1Y1Y0d9hy9DIU3MHDf2Wjit0BX_s4ca4jHFZm-TtBNx05WeHBhmUjaOl3LjjHluJnLA9vrohsS6oN5jbPPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjKL6PG219Q4BdEXON7yIsHyFu7vsLZ9EJAcCvesyVmbXs56VNvRYSkZ3AaHUP6v6YbZT38yIkZaaKXgcuqo9sl8Lgn4tDmo5MVGJQunayCjWupG0Z2iby16ehc4Vo8--6qNDqWbXntzSBfGW2UTl2hNsWm35S76P9WH94XWjL_SmbwlwAZTlT3-9c-Ut6F9Vnl70LjEyIBYj6gVnqVdTole7bdnnBstKsdRxq_7x7eRtoRVXjgon3HbQpDAKZypZycjrcYGWGxahskjvrgiHZFiDbdbUYS4p4oW4xr0xSl0lAbjlMguTRbZ35NxO1Sek-uefi_tbuRZWEKmwOAJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMGgAoziMXHXdQpnH5DNFE17W9dKfL0krz2xwSR5hwaqp_76yVxt6SSDNpBn2GUdM6ej0LVUBvQo4nf1hO2wZXeh-5QTXD8uPc7DsVnqJAaXn1t6xhRC7s47ed_28Iu728SVMvQZnLMwXPhCwBA2mVoUjq9-EhzAItYpqFOSLxv7-buIlrk4srifelI-jCmMNtq7X07yTtk0CeAZuY2FtiaxcNoSNWQccu301dxcAoa_cTUxlk8rC979TE3J_uTNATDsS7L26qMpJ6_IYHxLpsJZQY30eUm1JS3H_WSDJu6b_8rS1mkJU9LKwHQUJzkgUu3PsA0ZpVhjmA4DrX4F3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8uI8BWVFQ3iRHSMH_q7sFoxQ8SOVr8BlB-nY_ODo9BcuABIE6SbAgKeedgaLVi76Y-Jj8G9fgAG0Bd2AU9YNajelolbqYujmpdao3Y5nK7t4m7ohkK9FBcFroDmMX5Sd2zKHW6D7Rle7YSaS1ehUziSdh9ljQFBLj_poLzt8tzvUTbGMtDAAf6hDqFIjbqfH85pnYIv09wMbKIkixlviZJ2BV1ImAfCPi7AXmfJRJ4VeZqrv_LVVFR0_UUfaJo6ztAf1GqipqY_cpYANFMRM_rq2H3J1qGEuEw9EG60B3EyhWx6UxfO0GmhO9owYQbhe5cWw2EBjUjOuAlcguKRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5vuzXPfNJduXhxBh-WV4_IcoNfr1kVW45XI12C_SYSk7NAxzCIYUQzCzyttQ-4PKcslFUJSezYeErOZX5TVLwI_1UpHT879D1tRYDcXG7tG1VQFRme6eZkSjg5_Y-cwBGxKCcxtgQMCnOxoD0rEgOB_lahmV9dJg3a-lU6qVDxUqRwUy_GT9pMfr9VXZ0otoMg4hbP7_8W4OhknAjF_KGOMyfckonxRbZ4qLtGMTpGGsOXpBbYb7t4JBqISS6UsNAXILpCq13bSmH8b-JMG35ApUUpbvUR43pI3JE7Va4CNLKsOn6UzJf15ANKM4N9M-basdoqlaawtJg9yDoxVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UG65SRXrZUXgRpTgf4WUj6ZUoRW5Dqw0GK0HF0CbMtxr2OUAx6gLbQNvrIJEqkE1FCTCbLPnHmNXBt0VdZ9PR9NVOfl4pDGLTt8sV_F2TNoLv6ohSS5d7kGYbWGsrsNWAMFMuzMWhuXHNRPyWz78s2nA1b6-w3WoDRbrOCV02s9-s1OzynN4Gk36-vZyeBgv4xz8BTIf8atIXmEpbwhWDPQz5feTuWfMj2sCndi9V3DYJ5SeeN-MyJZn6hxDQUIWYJgTuhlnaiXbiNfjL4_PJ0SMoHDvpcW1B7vDoH3C2_O9hcARuqLjV_b-khU_KDG9nJGohkWSWTUfClwdjv6KYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGU-XazKbhNcYd7EBEDuv-LBBUkm5czbkh7zC1G0pMX9vrkZh2tmg3MkSCWyXdIDgbgHmjArKc95kQtehrl8h5ulbJ6ABWuB3sqTBJd9Qsxi8ibLoEEL9nMxC8l2BGPr1clffCjONBgnU0DaOpdpFgjQUQ1E-h0wR3iOOoPrYsuukS4aYjCLCkaQD1z3g0Cp-yRFMsQgyNXBEAti7CJlr_MTssqhX4wl8pFsF9wxqGkkSR-C7CD7_iafx7FAYPiGjclzIdIUTGNk_Ba2Av9LyxfiV0nlLaogCHsOzA5Lql8d6pUX5SNNCY3LSMFlOqrtIovN10LNDu9eCGs6DE35XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=f6Ronb2fgC5zYXDE70bKfoDCCagX4ajyCNeiFqy2yUhVtlvzLLYL2zFNZeUgYKcHy0o9OUYVFlihMb6vpXtJzNg9EEcs2sDHAhEl7_28_ijjwhC9S_ijEmlfrPZqR-dt7wMWhWK_yqzV_gmUgz6SbMS6A_CBzwwhJhwTu4I6T9JibF8BQ-SJKfXboOtWAnoXi8RC4KTwO9XH9pXgtanUFof8rE36BdawZBls86I7Ciw3pgfYrWG5er59WLHFR8tKs0SdAf5iKJVvFKhqgW2RBEA_ibJ_Vp60LHQvSth-K_uIt7MEExX87RpZyBp1YbHKnYOc_xg3wt7lGa_KPuC6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=f6Ronb2fgC5zYXDE70bKfoDCCagX4ajyCNeiFqy2yUhVtlvzLLYL2zFNZeUgYKcHy0o9OUYVFlihMb6vpXtJzNg9EEcs2sDHAhEl7_28_ijjwhC9S_ijEmlfrPZqR-dt7wMWhWK_yqzV_gmUgz6SbMS6A_CBzwwhJhwTu4I6T9JibF8BQ-SJKfXboOtWAnoXi8RC4KTwO9XH9pXgtanUFof8rE36BdawZBls86I7Ciw3pgfYrWG5er59WLHFR8tKs0SdAf5iKJVvFKhqgW2RBEA_ibJ_Vp60LHQvSth-K_uIt7MEExX87RpZyBp1YbHKnYOc_xg3wt7lGa_KPuC6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=um8Sd3r52LlTdta0S6BDekew_Msev5WhJdUSot_2Xmu7j1GL6qostb3GQqliJIzLibSjhiNGlaXXKYqpuiAM_kIlTX31Xh9qEiYMEhJTQ85pAUsSbJ7sg5udHzC-y7JyGoZ6OiXZEqsEB6VSAf5pRIl0-Ut0UcVEEwUBljtCcWu_JaHMXjU3ppKMXRA3GHiwUaSpH-XHkbMHPrkvjXHECXGKHUStQYGk2pqgW_nit5AXKJevpdpED6A2s5W03u79f7WOo4SIvFoY8eu9O8Lb09MBypgN25Qy2kVaPh1sJLP6nLx53KGvfw256VK7f8qBsWf7vNVS973LzHQTVxas_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=um8Sd3r52LlTdta0S6BDekew_Msev5WhJdUSot_2Xmu7j1GL6qostb3GQqliJIzLibSjhiNGlaXXKYqpuiAM_kIlTX31Xh9qEiYMEhJTQ85pAUsSbJ7sg5udHzC-y7JyGoZ6OiXZEqsEB6VSAf5pRIl0-Ut0UcVEEwUBljtCcWu_JaHMXjU3ppKMXRA3GHiwUaSpH-XHkbMHPrkvjXHECXGKHUStQYGk2pqgW_nit5AXKJevpdpED6A2s5W03u79f7WOo4SIvFoY8eu9O8Lb09MBypgN25Qy2kVaPh1sJLP6nLx53KGvfw256VK7f8qBsWf7vNVS973LzHQTVxas_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_oQLKlS06OmMEVEsqHYnnmT1RaOrBfd9cIg0EgrbJwsqmV7Xkr3rUGAzoCUGdD-MvA1Wi27q5zbIwh8FE7Ma3VRnwqllBsgi27SFr4BBce7rT3DlPcsoV2FEcrn8M0ZTp-NNqhf2gSCbWR4-YeRqje8M44W_6z6N9-ADf-QAt7vcLdYObGh_FDiXn3qFoHhKJEOlKRna78qn9EJloPmL7pz2wxzoEmJZPO_kXU7_5DhRSAfvxesH6QYVTd-iabD63kZviHvv9__ZhrjIJsNbqnSb9ntWEMX2qz54c6Hz3_S5pxnElmAhq0nWPoc8aCqilFT0H5pnrKwmbxzapOtqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPjkYC-IZnCBd2XFtBxGFFJL-4aTQJJunQAPmcNeJkYTmaDgs-Q4xpvu6gDG9He6hgWOvNSuy0EjoWj6C6PRTUkHTxg-u9lgTY2ZwxHUsgCdKNynV5IdeAOJ0eI8KZH7MgY4ZmTsYBQ0AST0_P31CTjw6wsl5LMJHvEAj9y91Syx6rVak0YKzbFqNNE3lLZwOAV20U-tbyUPql-ZCm0XT1dRG5S8Yyd6LGIdYbu1EJEpm2MlU1sZ-YBaBc-ilYjLWFnTupe3CbumyF-fMsNW-wO-pzpXhXeLFLr59OL_FPEAwizq93C3MQSOin4IDvjKpIV6g8dDZs18eGSrd4qVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTiGm6NlY8b8TmtpFy4ay6oevqyQs9l39uB0aIPJmqT22zWmiWlcq12oRVbAZspzg0HUqCqxz32LySnM8AaNp3_SJet4Z3g9m5tfjhFqecIOkfENPNboGVOhfRq0JXY-uXi04h4CTMo65G-qcyHCgggSsp4HaEZx6BHfpRgvvEUiARtu6-BNj515tHjj7yqgD3dR_duKFFylGPqWkGNlXTrQTJrHdmnDwesualgHF2gCY2tUvZpmNrupkeNaTKQw8ALBH_6M59hpgozSMUbkdsr7T06VSA0WVXOSt9hGj5INulGEL1mN0WxDlCRqY48I0KzB6AyK1DvJdBoue9-sBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM2g3mTt-g8mzroXE9GKw7kpvX2B112vqmVHsD0HFgIDvv9V8WD81UMmW8hj6xujR1-SBejmFVK-BQ4QayfSxO6FDQ_Tai7xdiD8_eCH5oFckNTVmkiJzksjIlk89x-qHUqBT_mDXUkM-TqKo7iL20t5atyO5bCK7863aEh2ugAkbP99VkUb-LxHY1mcc5VT2J6hBMHTpIAeFAf71tEqWvZLjVrU9qUCe4gpOUD9lXMGnXvkQJDdb8SJHDjQ7p_73QcEOdRtcyBFVX_QBfwjfiqyKVNgPN3LyTUJFScXNUD-ebuXftPT6zcUm-0G1gca1Cs1XCrAU-yn3JV1LdtGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7-SqTZgkLgF-vgwOtl_KImG4Ado1ZxmFsGf8deLBkBik6ueat0f_ytGBwgSlSoUzR-XgZlX1XolDg7LU8VNpn_BTsw2FeiADKt-Qi0V1NLq7npW9xzk1a4ZRB9Zl64Uyunhh6aRJt-qP2gXV1myW9XFIVRklJFUoFgIVaSdDQsOhpZbCUOYfJSn3PVt3LsziuVUTMJaxwZr43P8hNsFo6zmEudH-TJzBnODqxBLit944IoL_LTGps0TDvRZZKdv1PAwC_mAtqBY8T2xtFbcmpedQs_9DYVu1apKUpJfBhM7o9fwsnH8AN56WqfGceklmtHut8Wa8lAeLP9ny5dP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKF2iedyx1ZwU8Nklqud4_2ppqe0X6hPsJKmPWSWNRQHwydkbUMheHis9ghL3Ye27dGA_fejUfCMpJHAwfpLD0rVKEPr934xedYwSZsdLQcVcAVlmo8lQM5F3N9i4ubMG2i7tHCgeh92aCgNCIXOvd8x9oe58ufBnnZzUWACZN7pjCtg-gA6_15DXmQ1ILfpnxCbOI0pPxlch6R3BIcm82hsfStMLxc-kFy4WloWiYzI2jmJet53wPZ5mCG512UaxscSmMGD4IGFvjliNyQRefDSeNANB8xO2-sS14VJZX3ctAwsRT5vG-wmrh3momUBS5gADlmddVCD517aqx1kZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCWkUjHkQ5o680NxXtnEdT5MG7x2Qk1LsSpRpzZzsg8tPSp449ekc7tp3lhd4-lsQjIeMDw8Of7tWef_IfQicAWbE_zKjBcOhtAX4YVqk8EXucghHKbrRp0If2Yv01MHFz4ohC-961_o8f7Mg3ynECN5gDVTOZWjxuegId2QepR2UZrcKRq1guZqG_p9XQLLUVRqOHoFK8fiIUatxKUUvG6LXAEazSB2RIxnGUch9iREWqKPdnPbaBpn5xI6HYv3KBbkalrItwld-_cmGpSIM1Pb8QIy9G29Erg43glTxm3lSJQ2FAHMKHvFd1g0BG4yzymBBmBe2bAkrSMz1A88iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
