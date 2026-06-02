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
<img src="https://cdn4.telesco.pe/file/iWqKpB7m6HaYvoUmd9Z4IhqLKmsoNTnvELS6hLArbZiaRZfT737DKmiBh2FaLlpXisDPkLBfSJQ_9iZLOgx1vF-bAOnD-UEDKU8lVe3jUugp3laC6qg3yepVJSG9iW-9M2d6wZLdGC6cLb4l7AymtOxMpQI4eYfGvV1UidbJm4JF0Fg-_E-FYr8Iqsl2CYx7_pgN49xRbgEKxBcVTTU9XnQe0HZE1uIplHQjKwW6-62Ou_SfRg6rwI-NdBW-V21AUzOYpEAHxWEJF6ccU6DpQKTG_7Zz3ylRVy_Q78QWMQHLMpcPju85ZqnZ2kkpGo3JLRHCA0KUk8iycD5GQKlfSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 176K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 00:57:54</div>
<hr>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6HEM-ixABX2xogG7uZC5VDgQXBpnSeHmgZ63N0DubowIqSfdebXYJa-VRSzMqpXG4BKWywVTkZBMQwREqywS7OPBFcZgVAEiDCUEh1cdIANPQZdS-_CG-kKDRAysJ-NAB-2KIe43oZW1e0k1LzzJEIHXetpLplei2gyidOd6zmmUEi-CJn0Lk2-itCCDD-vbjAxxg-q-r8R0QCHc9LzPmKvazU26cqJrNj8mTgREgztVA8XXIzMAXvTep_EyygXIT7PBqrJiPxpZVdOVlX9mgcmEfVX4bQPY7DEHlbH3RNDGLEjuzYsh3I888DL-Limoty-Uof6DUkaodYThAWzwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0TjJvuq7U9fUDOCYOO4TmZtbXQe8QOKFfJpTXClRYqDdWwX9xwKNwYeDlAu0sv-gSstHfffqFxMX6scKBqLGIB05TC13uQtu1pO5SlBoPm-OwT0RnK2QOFkZ85b51aMPum3aONH6wn86I2FvI95-FfaK-KnKMt0pYG9QCRXhKPZUb4xJ5Vk7caSU4UBALHyHUbzIADjeWbQivsT12prfOj8VNnzHvsykggopLftbKwrJf0V0uXGindtEtaBFnfVk6yg5cZjVs5ZoV9FSpUOgRZ1C4UOLbbXkBsoSJfNDNT4zo_cfiR8_VT-LkRdl0R627Nqn9sN6ERJCSv9ZDPGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=TiZ-v0iMw8rh8HUKeCkRlvEFWRQgLBdhO1Nbijm_KCF53cbNYKFNiRVK0ZK9UiaUiS78V7nf8wHxBWcPp0Os0-eBtEZ1CS4xCcTNisRq-sqIWMFJEYgCMxRcCP-lEmUPi_z45xbDn4kwBPVF9bfdXE5NIYquf50Ey2mCWjDq4SEJMUKIJofUViQeuV3hr-SzBKUZVY_lbz7-uVa5BENt6s9PqljQ6wkj50K7ffjgDtKiYTucC39dRZ0CjBHWGzwUfH5Zd-MZajix7wFoOjHFMPl0rU1onSo7_AIW8w0o6Y91F_2IVDAFecFW6ISbcMadplr7lfs3VSDl_1PDKw1ZEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=TiZ-v0iMw8rh8HUKeCkRlvEFWRQgLBdhO1Nbijm_KCF53cbNYKFNiRVK0ZK9UiaUiS78V7nf8wHxBWcPp0Os0-eBtEZ1CS4xCcTNisRq-sqIWMFJEYgCMxRcCP-lEmUPi_z45xbDn4kwBPVF9bfdXE5NIYquf50Ey2mCWjDq4SEJMUKIJofUViQeuV3hr-SzBKUZVY_lbz7-uVa5BENt6s9PqljQ6wkj50K7ffjgDtKiYTucC39dRZ0CjBHWGzwUfH5Zd-MZajix7wFoOjHFMPl0rU1onSo7_AIW8w0o6Y91F_2IVDAFecFW6ISbcMadplr7lfs3VSDl_1PDKw1ZEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW5ZlVoU-oZc6ZZzt6s6FVFCR1qi6l_zRV4RX81Xm9t7ByZ-J8dbQMqlHyjAincTkodxWa-baZQB7KSsPs-XbUK8fwoApPrXlMNSMyvNGjBdONF-Ew9eOzHEYbM00T8jwMVdfC46j94zULsXcgl1PjZrp_nnCE7uqde7LRyGkwitSmZznoOmK-_0YhElh1xx6Xs50TvRHHnAgbWzkgBRwpvdtg1PfDSiCWIelzzS-oAfEMOmjbgPgQBNajpFABvYTwf7-zBczr1UTFKb5K7G0WR16kKlHrTs6Da6_5B4_JcQRLcE4S6JSYlFoB7MqJQxTCxWlfCpA_Q08N1oDbKm7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGfmJgX2ZKyFHTABL0BTAj1aeQ2S3SqgrGnJ3Iw7T1wOZ4BN7K7SQdaWrebYgKZ_fKj6Xvsi80CqBisAspnqSaPo-sin0RU1j80YvVvpZuFeNAzhOD-ezr-4KkiRJGB7i6524ox-OdEcvLgyvxL2aWpSS5-tBN21Bra3A_ey3xrMZQQfvYDZPEQTG4VQicIfvN7-LPRSC9YpnPmj4sUbeHmrnqn8k875QV8iAFRUSKw7RpITlgyID6He1I8ZfOQeun94fc5ShWe4rcBp7l0b9Ruxq33tWf6XyzQETClDODmUIvy51XuR3m3KdHUuaM9zzHp3fJsXJyVLisn2XLu7AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsGxHBOv0EcIqPsxz-ikA_bNGdL-O3ZWfrNLlfve5I1uMDzJqBt4qskzuR2xgkNBH1kSfKew6gBgegyGr8paINYZ5J5pripq9GfXAt4Udn7UGqhIXhOOLSNIPLEJ6RlZPWiwEVPXgZztXnV3x6uButSck6_dDMYMMFgR2UizE0VN6Xdnz6Kvn7ivpUdEOIawG2qyzaOC5OzdWAk3zk46iBEeyDNLDqxxnOi7RtmPrONBNtr3bn01fh38DE0aKGguBaZOi1iqkHJ6Qtm6nW6HXTY3LvFZLLdQI5YOu4h6amMDtv8UHSX8dPICNtRWGO_9SzhSlnK--YO9MKquroG7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=cNTXpjeIVPkiY7AczmGDWegwfNYBcb-5XPVyZlX3EwcN0L_DQkK3C-3nM1xzh6Sn3Vbeh_6fscyz-Yds1sZ1QYua-I2cA6xfm2T3rjB9yFfT4E-fxCzU8406RzKKy1ySBDDsqsh4cptBJsahndXlmYCXTrqEUlpM9pmx7m1Ag3h84tijeUVbrpu33JeAZB38Wc-hK-bGcwWiy1BzljEAjVknUlYXB23hYjcXmL9uSXvKpbUj9Fao-KB9ewe3ml7tiLUBaeK6Hpz03HwyOQvznZbe6r6_gIY1iva0PRHihpP0kS0n6v2TbBvyM1TfjnKLBBIbx3cJSUOIE1ErMFM41g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=cNTXpjeIVPkiY7AczmGDWegwfNYBcb-5XPVyZlX3EwcN0L_DQkK3C-3nM1xzh6Sn3Vbeh_6fscyz-Yds1sZ1QYua-I2cA6xfm2T3rjB9yFfT4E-fxCzU8406RzKKy1ySBDDsqsh4cptBJsahndXlmYCXTrqEUlpM9pmx7m1Ag3h84tijeUVbrpu33JeAZB38Wc-hK-bGcwWiy1BzljEAjVknUlYXB23hYjcXmL9uSXvKpbUj9Fao-KB9ewe3ml7tiLUBaeK6Hpz03HwyOQvznZbe6r6_gIY1iva0PRHihpP0kS0n6v2TbBvyM1TfjnKLBBIbx3cJSUOIE1ErMFM41g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدل‌های ایرانی لئو مسی و رونالدو پیش‌از WC
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILd3YLSDm71dN_rWvCpOgXOViohS0V6D9uaB10cdt7SCe5GCaF6oID4fKEoq_Kgacey7H1ERxbutEDcIfrY8XaP1rShxggujHvqsDk_XMzaU2CrzFEBNuRlVkf5nohssT4brHll5sgAU7Jo2gmAgCfemgvOOyKxEUA9UiVLWk2BwLYDp-j44G9cuxFtYcOdecGGtB4qJbUTmLIPWDnYjI5xBuEq8oT_NKp4REf8L4hOcetpsfnP-o5J8rQPAsq_95FUnyulST-Au-kD9Y_w9KkBD92a4myOhz5RoMkI-P_6tAXCcCq8ohW8SfdseBsnCYrFhjAqUUtK3_-hLBRRXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=SF_SRwN7UboFJK6jm93MIOcLhoDcl37D_nEjHqvUKNedaUPS00zJbOB5sKUVgqKgnUODepi7MztG4we-cvzHZXOljtkgHNoVEletqYebDmratdwwxbHqibzhSX2ucmGcfDbQvPfVFf6YSuZeQTi-3W5Ki3vfCMZ5K5sxOxCVCAqacKPNK0I-qDRjEq3KEhRxUy7NXd8XR_HkPyp0P8pmeRyru-Ww6HBCP_nikSgUOjTCRrh6ahlbphMClP1OtSv4zEH1IByZVLR3yflRFy6mCOjFAx_ENrdiTs-0eS6ZrynK_tgjVTUDD14NO93AO2i-QyMqqwIqMcQBSk3PyVD3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=SF_SRwN7UboFJK6jm93MIOcLhoDcl37D_nEjHqvUKNedaUPS00zJbOB5sKUVgqKgnUODepi7MztG4we-cvzHZXOljtkgHNoVEletqYebDmratdwwxbHqibzhSX2ucmGcfDbQvPfVFf6YSuZeQTi-3W5Ki3vfCMZ5K5sxOxCVCAqacKPNK0I-qDRjEq3KEhRxUy7NXd8XR_HkPyp0P8pmeRyru-Ww6HBCP_nikSgUOjTCRrh6ahlbphMClP1OtSv4zEH1IByZVLR3yflRFy6mCOjFAx_ENrdiTs-0eS6ZrynK_tgjVTUDD14NO93AO2i-QyMqqwIqMcQBSk3PyVD3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM9jXUAB0jYc80_6R7VOZZMlSkGa1KSZXIXJSnDd5iNADzHWWnApP0v3sEUZuWgQmpc7B5aMtzM7WlcHMCFtsJw4rWFtA9qHWtf9eYTgcZ8khna0GEw8MLAUy3dmBBWGPJvOoTlJRMZAF-C45y_C_gDN9s5pOpbKto4KVv-AIr3V4D7yE_Xk6zF9Nylu8PJV7twKYJq9WjZSZe6K3CzavscwRcCy5D3m-4287nB0gZo5qo_Gt2HHAthlyJFJOZ2VI4vU4xUnMBtl0EJEKN06pP4wGVCI2l_KegpN-_f3p6S5Gy8RlYd-UCMPQtSrXLO0pFvReNnPORxvrLe4xmTH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=KJrQxAHs7Hm3dkJBSmVCFB-BwMJOgU7HV_vnpJ2dQ27Hb278r3bx--0Ae4gNHroPiShl7RaLdWnV3anQKj7XUlN_2lBV9XKWBFYCq6y7YwrTcEt7M_lWUxwO0cdRebhTqga_LSRV8AxfrpiEGbSWHKCWLlryXxxCslMiU_04hZVUHCmDRIA00-d4mS92J8LNUsVjWDj3OPZP6kB1PEC1OPYZkDhjeJr5Pvxe8HhC5tpRif_SIkdb0-K4Oey7vqTYpCiH-k3KvPWHoRu-DxuMUjuZl-fj-bc7-8pkcaMqgV3pAk7Y_QbVY2EnhIeGVkpOi-ePlZjd_dUp6ObXELpsWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=KJrQxAHs7Hm3dkJBSmVCFB-BwMJOgU7HV_vnpJ2dQ27Hb278r3bx--0Ae4gNHroPiShl7RaLdWnV3anQKj7XUlN_2lBV9XKWBFYCq6y7YwrTcEt7M_lWUxwO0cdRebhTqga_LSRV8AxfrpiEGbSWHKCWLlryXxxCslMiU_04hZVUHCmDRIA00-d4mS92J8LNUsVjWDj3OPZP6kB1PEC1OPYZkDhjeJr5Pvxe8HhC5tpRif_SIkdb0-K4Oey7vqTYpCiH-k3KvPWHoRu-DxuMUjuZl-fj-bc7-8pkcaMqgV3pAk7Y_QbVY2EnhIeGVkpOi-ePlZjd_dUp6ObXELpsWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCkZVDVRozApnxw76FtMANxMg0f8MOYPDF1vEyRwEYU-vPuy2lj2v3cPCA9jwIt-hiL-Bdr-z9XJZP0oCIRFP2xsXVgCx_I92ImdF_Wbl6LSP2hCAu0Xy8rA8BxsDbrCJCCX3VFJUyfPWu_fx9FBufctoCvnv5KdS90_hPkwzBPocVzInSboF25eqjUwEH3Hw8qNb2xWSNswsfQPmz5xHzMiu8XQ7DwG-cO1zK40iMroCmvx00rR_u4ioq8T-bmE7NmUQ4-QD0ATtS9BghKv6xbjp9LCb6jdHsQZBjdPkjnc311iV_TViWV79I5iAG2uzgpxe-5TaLpqmusHhBxHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJIbKkPASs9oiNRJintKZA8xAvnoCZPCq3ri25JvbXl0RJVIT_BeIXEstv7ikiyywYAL6Y9M8H6OVsuOqCeNcJcruLMmjM4Ihqa3c7LGtgpnxg1P40z4QAKOPBe9vV9iMm4lkBjcBqaitBrEOnF_rG2lYfwhgsm8ghEM842VlhifFeUCxxwoi_t1hHkR0mBh95DnwcFq0rVEOVqfYn1y5ivxOcmvAquD5YgVU6x5rBLd6PAR41qKgl-SQ9UggCmxUC1FBefElZK-AhjS2ivXtu-37sozwfiamdqVT1BbnYBA-83w1K1_2CXuVcLPkPFmUIHxb1aamA-XF3FEq2M0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-YEMn2UxOV9iLOlfFcQvJnXbYLVALq0Pv9eWoALvBhvSgHWtCOhF83TKjpLW9ZA9WQcn77GCvsT7XoFwDTSQZ8hhnVJvdXEZFEyyeO028v21DppLWqVT_Qn0dk83kh5_uERDUMPWmdTThykFd_HgLkPqn8mfkVxjPNh4ZaJx-dWRuNS0AbLyK9uQin8NnIlSfXsEy23C92i0Ew2gJKpIO8qRezs5LimskM2QX9qb5t3oRG0m1jbPUms83PpmKJdqSslk9aRtVuHxGsE-zaOm1WfqlF8e5_mL2OPS9VOP9lgnSjwHvEO5q1XGhTEEpkq33ZxPk1DeIZkGaR4-t9WJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT1C5NRituRP1PkES2LugngbA58IhsAQYy0coNLkyLFgLoQ8GPvk29XMeKKDiyu41Ab_dB2NUZ9Zk3hzJwowEUznNH0JH6Q5aiEpag6RXrY4jNiylV5VrXN7WGAalwfUbUIA-sKYckJERbK_JQ4_DKCxrjdX3b7iGfz3s0cVNRKXFCT5bXAwn4a7-sqjEzCfI2nSokPwEVKqnH1pi7HLqaTahXOI0gtduzoBHfrq-aBqexEXNESE0dMMq2CXYhuIbQ5YYt-HBPDssWLEoNc_LbhoJXKJ3umzjSLE8cPeKX4dDjjECGJ-_B8m_SMC2HZH-ZyzBBhPIN0kaNy2O4Xrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=SQ0ud1HREJssr4tY7QX2ZTklkzPjQq5j-XSGoPUxLcWRMph7Qz3HRGyE-cUARig-zKjfUnkahtSg-HsDAWRQBM7g_wHT-eF_tYgKPbgY-0s0DXaJ50POaYNOInck3SOLVSu4MDMRH2pmbFvxvwoZEdTRoTcYZUtEwcKDJdPsxvo7ueV2UjDNlgV0TN2o2PxCUpIyJMJwrchrEFMIH8GIyXWv6OKeA14yDo_KBa5gCkXkVYXNqiakaxL70-GO25bTXPvycplu44wYr8dwHZLC_c-cQ11rBFtuAs6VMQfKenQ22aT7C4YTjvfEx9F__ALa17gSv3egbRzTOVJgcSd7Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=SQ0ud1HREJssr4tY7QX2ZTklkzPjQq5j-XSGoPUxLcWRMph7Qz3HRGyE-cUARig-zKjfUnkahtSg-HsDAWRQBM7g_wHT-eF_tYgKPbgY-0s0DXaJ50POaYNOInck3SOLVSu4MDMRH2pmbFvxvwoZEdTRoTcYZUtEwcKDJdPsxvo7ueV2UjDNlgV0TN2o2PxCUpIyJMJwrchrEFMIH8GIyXWv6OKeA14yDo_KBa5gCkXkVYXNqiakaxL70-GO25bTXPvycplu44wYr8dwHZLC_c-cQ11rBFtuAs6VMQfKenQ22aT7C4YTjvfEx9F__ALa17gSv3egbRzTOVJgcSd7Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی به ازای هر مهمون پنج میلیون دادی به تالار چشمت به‌پسرخاله‌ت میوفته که با لباس بارسا اومده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg70vCUiqqDzJQQ1yxT9zpMovM9smRml_pcOz1EsUvcT45XLktlzURHRl-EpikuFYCIQjMak7ovsCZScdWkCQgtcoilHEJAkWPVWu9rj6QINeM_7Wrsb_B9vamqsYStrkmWb6jsz_QCBSsLvE7jhetNB4s-Ml3gUmAVYPGNGGqMd8W2EDcMhuFIbFNVRcb3jSung1M55uFCIhZ07YOhhiTyH_cx3sttDTnUb7eOkMFHGWPBFYoi7jBYwMG5Iv1FHgOlRKDm4kGtXwz2Hln-doSRuZORnYWiyp7BKS2Wg38HDlU7URxAyxjnJMWJEf9sq2npQZtl-XwAGplycp7nFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuD4C286E2w1VrJ3myv2n-5Dxw_fNBw3DXEgogaMaXS-7GU1iMjcDKJX1VWGOsiTGPsk02162Lzng1K4dfFMJVrG1hqzaBUL9VOqtAzA2yyyJ1IMRSKl95Ps2tY9hzytX2-QG1Gj8OdP06qSybLybwkW0qJjDW1OqDTR83_hXx1AUXrezO8ajVC0V0b1yU9uJzZthnpJ1Ko7lD1CbhPzBuOQpCja5ylZVYUYySeyXrLXXjsGjmiSQpg2F4KtNZ5WobyT3G56_imt5UGIw-a39zlC6FyOr5Bm4rCc_H2VicR9JtbBjzmDUNJAmKLTkndMJhEfJXS8EXMSPDFOjobeLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxn1dzp3ZuXl9wBefXL4XTn6sr2QjmOI23G1lyGRdIHGedT-CiPaitblhSKmV_lW5uVXWDRS6Q-wMlaoIv_mO0_DKokCCgI2piezxVaTG4PX54zhUHcXSZGO8l1los1ZLTxSTHVoF540jRSnAJuKv1i7UmmrTEz3rE4MwPne0X6BrnKiIeAS6WQv6jXCeLVtimFyyZuJV5ZuXlWf7IuOERUwTFvp6pTZStTKqWeFFxvYdPRer_Uc3ckx01cMC-nKr932eXLhW2iSfBXY475z8M6ymgwSeGK7hyA9jr6rLOpZTnM-r78_7KFUk-aS7gAZ2Si5ajXfCUjcU3Uipfx5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22672" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSaayPErbbxIX_SEGg_BuZmmokKpa7RiNhohHluQzjgsbquQ3dYwM1hllSQTBfNkQcSggPI4Sx8IB6vRstvKBZrF_TcCd-iYhM-t_vzbwXfpbtKh_D7zIjsZVcLYwy2LTaGlzlNmf67LNqqVkLqwYbBdpI4zG-pM5El6wozCNTJH4ztdbZu-K4bbEPtw01zf41Qxuy_UhVIfFawfPfHSTUK750E_bxys3E7eIGh-ZHntwwzDkNWWYi4mvlInpFDGAcAbZ-43niRx1x45YkV1rIBNoFrEOMSp5GGYF4hTXD1cT9gBGaBSAKnbXV5-Kvtb9DhuWnJVzSRi9F_XRPRT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oat-ZeSdjXWOIVhiiOUFQ-_oO79UU4QWqKdzG2fVk36AoFlcIcMwrhLB46Gqq8tS5vO3FWFR0pNjnLCxWc7UMurYcjoX4D9j_NziHZ9mHhzWOaGMF0ccSVc3bXuu4IuCsB86WDyQwYtd_YjreZAVxtNo4K9vtxEM12YO_J6asQvICtOsrD-rCcbchrDNilI0TZ8w3qFpgGCrpazkAFNZ7gp5asLmDQvzdmBNcSOsUQacMBpLTdKL6H65H-FqUeH-zGrZjh5bKLfSgLmc8lCrJ8HLnb3ydm2pnSQ4kltsSo3m0qlH0vB9VjMUH62VrpMRIjrLOzY9m4eATqKPiBn6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXQmvB8rRGTa70FiWUhARawdIOYdfQdD2TFBkeDtQrnCqGFClDxw7Nxw3aP-D1045efENBYVcj2nDHNWM-cOqQLX6Yu7bjulIHo637TGdQ0JDF7-Tk5OFkxLjEYFhThO0a9i5zIQyXXZK08yAjBEuG7iGJ0r_dLblep0WwezxDooA-YnGQ878L3GFPQhEBWjd0hklxrnE-QDJdoJN_GxmTfgrls7IZQyYmmXIDY2Dn4AweIqjzukIeZZZagn1j7li9ktovPVIuDBCr-GMgeHRoVsQJDh4wbW4WzUwTFCx-lhK6XkfywfgI31_6bI2OrUpx-fVT0I5FxS2AqFSF5Wqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbM46susScVz9xwfdHfStpPR1pP9MMbUWc7ExfqP1doE5auc6JsLtZxAH6PbO9Mg_SvR_jzL5R5n9jhSvYVYJjrAMGvc_rs3kAMd4bYLBJ7fGgknnQUiypf1WcZA8Ycuzx3O5KLQtfiSmD1Y5ccdmVO4F913vaJWlWk6XH3yEIDgEKXaqqhcG2JSq4XBwuPxWXEBizdpDF8A_RENuPb0XQ8HgmCjzLKWGBYGmnrcLstAQPsPRxyA3TxObaqct7Eyh346NROMP66zHrBeKH41rxJKo9_bU0_fBt1NTXFVMAeOJGmRCIBAmpSm7W-ceaLItWReOOyNqRhRvsHcOLz5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avG1S1TCyKQ1qwhwtMntvd8riVbZPOGh3D7gOXdN69hICvYevv0ShmGTHS8r3RgcHW64fl2IZmW9eiTVX9yrMpSOOPLmozBa6U6kAIvI6zuJSm8w6i6F6BRwNetacUOcULejX8s9_Xd3Mobb0MPaUusastScIMohEKCJ-BhXxAXGg9U4ms7l0KrdmRKH9irU1sV2A3ziprQWsmX0y_lW2lRTXonIwbwjuDXe9msmKbv5LMDgtvQMzCbGRUfrV-9yMUHzWNqlhxKqRCNNWKHLgehGVML_iXXe4k8FjzEG7AcTDjiH25arnFzaHTaQGuRQkqSkkljjXbC44GU7X-etMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smI72iBjZQMeiC22lJMgNtsJ4CLizjOuH5VFoU_DUJZERYlUFDJHHr5yC0fOhZkFOnaVJSTUp_jfTuBK8ts3PFgs3dfxt6xDcvCKAhgT9_juGZ5pBopomsl5YbwTcVk71ADMjHFHgvAwntww3XfxtE7GlJW1nQhG7M1ps2BFaFi8IixBqxHU3BIsWc4uXk-VXaip8-CTCxA0QIyR8r0Spaj1-htVeEgGI9WJsfTRtpkNZ92xgVouRBiBwr11k7Ef9OApqNJdCo9YrgD76Ush11HEkyEwiY_wlzFUYgZvjmOVngL88G2azsbZpwt19k714-RsDfGmAxRQ0VOohafI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzd1ZgESS86X9P6xtO9lUHWZyGSjhWM4Nz9esB1bAZ3lXLotrvJOhAQbBJVTaT9A2FGa2E2zebwhdscY6kFMLvvkA9HvXPglpI4fHBXJOoTOy_YtS-XU2UTVS8W_2wJwT7jk-25eNtEq0xLAt_MsgubuMMEgqIIAGgtrPU0gqa88WDIPViNKnjQsAFBUhPcyBWc5ioEs4P8k-hd0NNpEcoaFWzWzxWUNgtk2qS9V2B474inpADyis-V_x6DwBKxoph-m1dbi89BH61v3NwNGPfLTz4-hAUjLVzR6gClkLU0x-Iis8zdukgxMmDqf-SeY_wn7yYb_K9tpPVmvlvrRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ-HBQH4QB2Ts9dMQplU7E3JEORB0ROxMfXMgpRch0TZ1QVRF98v9ur6kbwyJROc5CVajyPsiDA7vg-k7fDwRXg0cOe23oinkUawGXGFOSfklASc8tGRTwkatxKBFPAHSGXakvk2VDl5Ra-gtJ5Xlne3cjkpt2mYm60sZAwwhTzC7WIZ-u-eWkbrdAmykgq4uU2cgmzmJhVnzLLUhns70nZbByGOYvsydHnitDeVA2X31PmZV30umI-rvRD5ivgrUZu26CDo-9eN0D_fMEvj3p83NdPc3QKujgMrhRreE-alYWyhw_g3pbZyyou5P_d2wUI-aWW9y2nPKxRz9PTANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTphCkxQyMhPT84QgUYYoxDo2lxbHhUD34pKK-5aFfTCJj6cH66X4JQNxQzcJVAiqGebq4fjnxDS53W0Fy4_cHwztVgoMnqfkZdqzWnSrirDHUVeP4CacbXfRzKFAvhaux6roVZh5PnEEx7nbMqYPhIMJikptPV80wzNb3udZVLHZB7syRkLdXfrTyN7PdH2bjG7SFDz4roeA9zzup5LMWxxT0U7zaiYqy-Ivy1jsFq4TvrNgyUGulcZpnOr-WcKlQMKdKFCenLUNMOiJyBOKGUcdvCnva1STDlXeWmFmpBPBtxvl1SIvciWYj90irUSryIOzwttN4g6xwIr9856LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7xrkZMdes8VFTj4apF1g7ffescdl4vaCn7NuVmcSBJwygUvMV26Z1ixjkfST9EtfgDNpO1BRxAXI6HJa-gDiYvvEWtZqcQpbIYJUBGixj1jWRd1vs3onVwEKWYFp-K8spQ9WtpsL9dYQUyRPRhDYUKF10fGu2TdZRYqiboqi5W0iUE4PGimw6ARZv9kUkk3Ho21t-rIEYp2Mxm9zkXpKkHI00Bg40EdUZO65SbYX9f4RBEHeozsadwTUW4w-m2FPjAOTumGm46PaUmVmoxikfwbbnIx8SX1ukoznZftoRdicSmi6XEdXD5CTgqnR8qro-2khf1Q4-kMHqKCLkFVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOuAq6Y-Lpy7wK_YHSVRac41JxU_im2vGOEHWjzsME5HWJ_pq1Re19L1WJjlus7qTk82EJq_vnAC5sJJ6hbbaknnWur0IXZgiSM-SMm4eB7hgiPoFwbDQA1enngdlAHcYclE8ylFm6aiM1ILGwyIFdL7ctabEDAT41l-bxW4pKSSQ7p66DKnMYU1BFAza4CqUkfv07zH2zLAdm9y5Ea0F_G5mKLT_BeOdQp2iTwfBY3QUFnv7Xocsif3sstgr8sHGao9v2XWl9nDexeE-fhy8JwcHgB4BsNNvCfrwe3COMsMmOSVJoD8O0g5p0P_jB3JgKsSQ7hEIF__lUgZSZS1Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=jq7ZUfCQsCwveoMH8cB0bKwN4kTi-RHhYNnAET5b5kVeMmH2H_pjggBGHvwVSq-hD1XKMw7Gev6emwdwy1MhTCa7c-1y52CNaBUBp4WND1ToDIvQlyF2TIVBBMHwPsy9id4xr1b1RpCJZ3LUfa1lwG30MgacB7hap1juiL8DBSZl7MjqfLs3cZt4z_NZpHUTyUqdWZZTh3pMsCGOhXmx_Z9AaRlHY5PWTDAGVfSmzBtOyqQcfRmxaHYV2ChOKnQyZ8eTMVdb6MfuPvLqsBcqdYsBUDTiUQqYr1crp7NN8fxFAj4zrTYdSQRTi9v3RVdLpKJNckjfcTgbx-4i1k5qLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=jq7ZUfCQsCwveoMH8cB0bKwN4kTi-RHhYNnAET5b5kVeMmH2H_pjggBGHvwVSq-hD1XKMw7Gev6emwdwy1MhTCa7c-1y52CNaBUBp4WND1ToDIvQlyF2TIVBBMHwPsy9id4xr1b1RpCJZ3LUfa1lwG30MgacB7hap1juiL8DBSZl7MjqfLs3cZt4z_NZpHUTyUqdWZZTh3pMsCGOhXmx_Z9AaRlHY5PWTDAGVfSmzBtOyqQcfRmxaHYV2ChOKnQyZ8eTMVdb6MfuPvLqsBcqdYsBUDTiUQqYr1crp7NN8fxFAj4zrTYdSQRTi9v3RVdLpKJNckjfcTgbx-4i1k5qLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های ایرائولا بعد از پیوستن به لیورپول:
خوشحالم‌که اینجاهستم. به هوادارانمان قول میدهم در فصل جدید یک لیورپول جدید و جنگنده خواهند دید و از دیدن بازی‌هایمان‌بی‌نهایت‌لذت خواهند برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22660" target="_blank">📅 13:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HT4CZRds39HcNXOIhSEAaisvXm22BcnyRNXn8ulbKp87-TDwlv5NwNQkCm0-UCKkZNcc4KvX8vD9Jz8GVhvlaWrMuJizlITu5mlYfdF_RaD9WRe4HtEmZdb6ciTCie5TI82ph_uEQxnEGNnOag5BZItZbVFgK6RzyM-8SNR6PlQ5LXjIqPMV3njmaA7vMsVwX-2DZfkehQb-1lfykX29dE503_gwIehhkzzkIfwCFCHR_1uNwDyxrzQkMP0WCYgrkMOsPho46CuLiRZzDl8i_qu1Fbucqzp-0vET6PAzxD3AEWldIg5laEwa-H65YXDEC9v7UQpKbkUdq9fRv3Tw-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LD1v5OZnQS4kd0T9q9bFj56j61LWjSCpZ1dEl69NzYtMc2Czc83yt8D0Qt7k2-PuRSpR92JivXwWTmWRrdUUVz4WlnsIKhJ49jn6jl0fZn-3Zvzysm_S_xQLXwLI9cPk0BD_vs4spNxHm3c7YfD5FMD6hKpSFedOtg9uTKIU3aBBZze9Yb8qsoCfoBKYTIpH-8FnZX_o9CYadaqRJjW_IC1vkXeaUJOUWlcxlSt59F4NmtoM622DeMO4m3Ut-I9UPAn9eGxKUMGzL_SpXbCORzzG7coABeaIlmbZWkwVqsA0O4qGHjkmJW3sD1OZsfxa1AfwDonwPcCwV1WpjHFwdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=oS_fsG2tYPq5V4dw28t-wqNne3hTRe_30iPWGNBsMlrB1uwzm3FPK3ojWp4DhkQ1HULotGAwqZzdUIJYTT9pak1H75BhzuzpCFIcqe0RNHGwxaxsxtir0R-MftfR-pmIZaifsvZMdim7UsE4fmkjoGgMVCTyghSUf-u4h0oUd_yyl9rX_j0lBz7bLL6hkrnM_GR2L-a2XYRS7jN2P0_PlMB4tL20pQAMKZi504sAnRuQ7idy0VDGHGDKX5a6G38AlzCtxPD_IFOgk5Xn_m1a4ZLcdkIvWOoDyG47hnFupGZkHuXGxrFR-UKSfuddPmAplBt2RKYCULF3f0nKysjZ4lXgDg81J01mSnyFUO6bEab2uW9NhVHlHn-C_o2YSadpOkxGBID5PzqKweMGAKhsjfZxl4P7ZI1a7GtjAe0iUTXtJAlHD_gvKiyIW_rWCfkuIfcgC2PSHB_vU6XuklJlhsm93EBSjwx4WEuybizb5vnAX0MhqsaIAFRpOmoKTYtFsGwi3ogr-xvv6O0JHM_hlR-lPGp_bWbrfvVvi3luy7B8NTf-7pR8GhEpqjEQimd3cay1JPxDrEVUr794d5Ekq6w7qA6m9dXZLzaQvMS5cinOjKtOD0L2TIHgFliCNxCs7rVL5qeZEeCJAjtzi9jG8drPSj40NRSCmau-DQQI330" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=oS_fsG2tYPq5V4dw28t-wqNne3hTRe_30iPWGNBsMlrB1uwzm3FPK3ojWp4DhkQ1HULotGAwqZzdUIJYTT9pak1H75BhzuzpCFIcqe0RNHGwxaxsxtir0R-MftfR-pmIZaifsvZMdim7UsE4fmkjoGgMVCTyghSUf-u4h0oUd_yyl9rX_j0lBz7bLL6hkrnM_GR2L-a2XYRS7jN2P0_PlMB4tL20pQAMKZi504sAnRuQ7idy0VDGHGDKX5a6G38AlzCtxPD_IFOgk5Xn_m1a4ZLcdkIvWOoDyG47hnFupGZkHuXGxrFR-UKSfuddPmAplBt2RKYCULF3f0nKysjZ4lXgDg81J01mSnyFUO6bEab2uW9NhVHlHn-C_o2YSadpOkxGBID5PzqKweMGAKhsjfZxl4P7ZI1a7GtjAe0iUTXtJAlHD_gvKiyIW_rWCfkuIfcgC2PSHB_vU6XuklJlhsm93EBSjwx4WEuybizb5vnAX0MhqsaIAFRpOmoKTYtFsGwi3ogr-xvv6O0JHM_hlR-lPGp_bWbrfvVvi3luy7B8NTf-7pR8GhEpqjEQimd3cay1JPxDrEVUr794d5Ekq6w7qA6m9dXZLzaQvMS5cinOjKtOD0L2TIHgFliCNxCs7rVL5qeZEeCJAjtzi9jG8drPSj40NRSCmau-DQQI330" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq_fRMdu25rW_DnO_kMF9a_nFTxHv6HqXnybki7gl07gfmbRHGnnb8Zytv9WPvfolWtquQByOg_i8amAez4Fs3y2Wfnc3AY_y9xOr-LoFEMDXDC0oaJC9dzpTrTUo51MGDXwEDEojTqCFVDRDcs3FX1RIbTiil0zesfxT6YAHGP7nTFOz3iWu872o3Vgl6HBzJpZ9EQgKpt4pqGk7sWLlPn-RdLxounOjU-IMnEFI-TNrSplgUF1SQenXqOLXY3SIeCsoPIbcdJiTLnoiTmD50fWkI0FfJBYD22sQGZvtwB-izmHkIUQLZpjUu2rqIGzGyqVb_wvA2mXi2yy7dfzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=h0rfxb0r_VbpOdUebbRrwZlT4JvLf6weAif6ofzkHzPWCjudQZc1Zg9ojzgmfRoRLv8foJBPr-rprN1C24bnAUKiQk47UqvFyJbBji7mamrdcQcQM9rU3Ck8AW7ia2zdXg9Ocoo_3Hi74B_A9J62fsr2znU8Qkhptn0mvqI6Td6ljT0ki1bVB0mgAdrNjCcvAPhFSA-9S2jDCOEVuOQvbISAoAutYsnDppaZFRKXM46p9PK1867_yIVtn6rYIDr28fWHUATZsclGfhiHjQ5wI45-_2muv99FjsAiR6Ybleo7CqMBsn0SbQM8K9sDeLD7_E6sXdId6RJvtmsmFKyY7g-P3coZFJ20UOT7N1O06xKi3gcIfJp8OBnKRzl3NELf2ZwFcpI8WGe9zh8_zeFXKUpIIwSwcSlUJEmG9Qk09qj8uKpEyuhyE7hfiFEi9EOxEgiwndIk-tqE0H7aea8FSbCgOYgQ1oKnqk3FiGydSm-QKlz0jveZUXbTo0G7_7uFu84JutRi_icVyWl2P0amdx5JZ6pIDCizt1tWnxGW0wuBQ4t5G1yMtzH6yT36t7aCKkKPottdeI87Pl0CWuFCMjnB4YC-vF1ZCrT2QRl8i3nqcHW_i1odWU37R3F9YDuTJLvvx_k6LpfTdRVSgaEzagZ2NZuM7wCkh9QwhM_vNlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=h0rfxb0r_VbpOdUebbRrwZlT4JvLf6weAif6ofzkHzPWCjudQZc1Zg9ojzgmfRoRLv8foJBPr-rprN1C24bnAUKiQk47UqvFyJbBji7mamrdcQcQM9rU3Ck8AW7ia2zdXg9Ocoo_3Hi74B_A9J62fsr2znU8Qkhptn0mvqI6Td6ljT0ki1bVB0mgAdrNjCcvAPhFSA-9S2jDCOEVuOQvbISAoAutYsnDppaZFRKXM46p9PK1867_yIVtn6rYIDr28fWHUATZsclGfhiHjQ5wI45-_2muv99FjsAiR6Ybleo7CqMBsn0SbQM8K9sDeLD7_E6sXdId6RJvtmsmFKyY7g-P3coZFJ20UOT7N1O06xKi3gcIfJp8OBnKRzl3NELf2ZwFcpI8WGe9zh8_zeFXKUpIIwSwcSlUJEmG9Qk09qj8uKpEyuhyE7hfiFEi9EOxEgiwndIk-tqE0H7aea8FSbCgOYgQ1oKnqk3FiGydSm-QKlz0jveZUXbTo0G7_7uFu84JutRi_icVyWl2P0amdx5JZ6pIDCizt1tWnxGW0wuBQ4t5G1yMtzH6yT36t7aCKkKPottdeI87Pl0CWuFCMjnB4YC-vF1ZCrT2QRl8i3nqcHW_i1odWU37R3F9YDuTJLvvx_k6LpfTdRVSgaEzagZ2NZuM7wCkh9QwhM_vNlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بزرگترین و خفن ترین کامبک در تاریخ فوتبال؛
بنظرتون عثمان امسال هم توپ‌طلا رو میگیره یا نه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=aTyesFYz3k60hBI0PR-36W9okcCiFiNI9_9tAa12eU_aQHv4TZX98aVk4gP7WhgvZyWZIxvt-4p8QBN6x8huVDmNBcUmdgQq7mUlCvhJ-UrAIzh7ODmsOMFCEwK_JkvZF_YfDJpd5ctW1xsypX-dMn7JGNF1ZUUCezZs4WwZ4Oanz7ybaTP72UbG3mH5fco4bXalTavHeek63C_cQyqzkEHUQJrFWjpMUbla5uLCA7ntFCVM4iw_K-FvvOdRwS2OG6NzuPdttwvNFbqKQksl_eb2uWaRq-vUvZoYpv4dXVWdvDn-Oby5fyqQV0vpMUexGO8nB01u5YQhqq6E7RyQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=aTyesFYz3k60hBI0PR-36W9okcCiFiNI9_9tAa12eU_aQHv4TZX98aVk4gP7WhgvZyWZIxvt-4p8QBN6x8huVDmNBcUmdgQq7mUlCvhJ-UrAIzh7ODmsOMFCEwK_JkvZF_YfDJpd5ctW1xsypX-dMn7JGNF1ZUUCezZs4WwZ4Oanz7ybaTP72UbG3mH5fco4bXalTavHeek63C_cQyqzkEHUQJrFWjpMUbla5uLCA7ntFCVM4iw_K-FvvOdRwS2OG6NzuPdttwvNFbqKQksl_eb2uWaRq-vUvZoYpv4dXVWdvDn-Oby5fyqQV0vpMUexGO8nB01u5YQhqq6E7RyQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs1EnwjQRiPUhlGOBA_7KFfxDRJz_j5PZvwJzY39qgXhV83swW2DdtdL4tZlfntwFOt1uPGC2vqRCmVaBQEatPrzIzs0Lx2Oarx8rzcXbdtKzvr40u9rEdIwb0WYelelvRPkI8YrGm8u2i9j5RLWP7TbrfarWr1idji2QoQPAeJNdcqCCDEUGvT2UWcJj0faizQ8k_gmzz-56OWEr6t5DwtgA16jppvs48hbkIe4qkdfsmMK7Z45MGXUVFQSaRXbyUPqArd-2fNaMXRD-E2-jB7N8_loYH7aIwAP6LFDmPiJwRQS4An4IR7-0qjZ81IV-TFIMhLrJshbjwiHepp4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22651">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22651" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAn8vhCyXwnFuIuXaU3zcI2XlqBQQ4F01-koPHWciDC4WqjwzMFl_Kuu45DDMy7jsfppB2qS5ETJxZ4aAMsVeinb-cAHOrqXoQ2LVkOuCeZQOXni5SMtEDNHHxyNrW1EPAJlu-ypdLQO7fY0jRo8AGmnmTZ1QC5EO6PjiKcnefsc56KxQdlyFgtWwA4rgpgtB0Y9VIBMdeLtaQ0maGZjvRwsLfv6GycEdCXBFKepDg2-JqS_Wxt5Xtko-k7GtBu-3xYpab1QCmGeGKDKhlKwFs-0o7xzYWn6B3R5iSom0BeVH0avekZlogatBZf9MaY_8fP8-_0b45N-T6rKbYNq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22649">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaOHNvDT-Y-0KJhjWsgphlRduDHKEYxFqfEuz8dW4OmRGknGovcTmreZ6qwTwo9k3MJheS1TFNpUOGRTftYG1_IzCFvB9VKgjWBZgEaTOx0U2_fqZFHlNutEox7oeVudCcz-UC_Ay_c4J2fYROLZFKQvU5qSO7RnX6pliPrwWy4o63SIwqMW1F7J5_x3JN9OJxqe4n9LavKPZs8fBZC5Urv9Z3tD7VpU0CJhn9wDIKUJcYzLQyWoDFSGW5io3_wPdIZgIvnftXVRyZvidu0KIOqgPSCGnf3dBhyYRqJmwk2hhONp2CniW3Q9LirreKYzb2LzKSO903EB8PgP4_ADoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادعای رسانه‌های آلمانی: هری کین یکی از سه گزینه‌اصلی‌ونهایی‌سران باشگاه بارسلونا برای جانشینی رابرت لواندوفسکی لهستانی در خط آتش آبی‌اناری‌ها برای فصل اینده رقابت‌هاست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22649" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22648">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sy0aUb5AOeNjeOPgfXTBK4fgR1NKJQBbi0aXd9JE0SjOLbXZzuTHo4DTVhymM6H-1pKirY7UQiAY6ncjLQn6JiiuDFVOUYIw_jWjMqzKlpJhp0lFaSB3oTumecRDaffjHbrmIVC2uvBgoRF7iqo2-mv7yzvOJT-fwVKDYue1LKTioKJBNALQSTZ8nS-JJtgi1RqQGqoMof_BG9VTI_z7hwIEc2o1Hq45u23vTwhgrDS-8Dq5qKg-oC1E5qlmLwbYVifsZxNhLBuovAWlqA3noMkm0j2vrLhxFT8g1pcu2PHMZSgtbc27oSNSNCpgsQTl2jWx9brPiNKwgDk1w3QwB1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sy0aUb5AOeNjeOPgfXTBK4fgR1NKJQBbi0aXd9JE0SjOLbXZzuTHo4DTVhymM6H-1pKirY7UQiAY6ncjLQn6JiiuDFVOUYIw_jWjMqzKlpJhp0lFaSB3oTumecRDaffjHbrmIVC2uvBgoRF7iqo2-mv7yzvOJT-fwVKDYue1LKTioKJBNALQSTZ8nS-JJtgi1RqQGqoMof_BG9VTI_z7hwIEc2o1Hq45u23vTwhgrDS-8Dq5qKg-oC1E5qlmLwbYVifsZxNhLBuovAWlqA3noMkm0j2vrLhxFT8g1pcu2PHMZSgtbc27oSNSNCpgsQTl2jWx9brPiNKwgDk1w3QwB1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22648" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv-W_xr7beGP3DKGWcH55l3k67riB7kuCPH7E9sLF62pUWoXAJqSy_4n4gXTSsZt8xuonirddlVQWBsvmHOmc_8logkfnC-cihuNWoyHOj0hfg-3zAeoDdqZNYF4t-x9jD5h4xBvEUKK6mlVnDwtGo1SXr5DkYbTN6X7NXo3xL_WWv0VACIL9P7aclJ0XxVYIzhNIAj7HOBdLyef2XJpLD5KpkczbHq7r3ymKyy25j1N-ZMZ0-Ime20Ma9YROAR0trcNumuQdcGrGYr3TJFbpQQNefP0GWj1dqqaWC25Q545bOvGvp7vb3w2xQ0Di77iEWmwVRVIZ5pk57v9HgRhlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از پیرفلک تا شاه کرمی؛ اسامی لایسنس نشده‌ی بازیکنان تیم‌ملی ایران در آپدیت جام جهانی EAFC 26 با نام‌های جاویدهای کشور جایگزین شد. حرکت غیر قابل انتظاری که EA آن را انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22647" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeCUMZ0y-JHa2kqRNdmLV9v_jdBU_FhZSO0HkjIEHhtHtNrXjSXNSlh0ee2DQlbIqlKY9JSbeVMvPWXLxRUWVPVnZ5YpQerqppKy0g_EJUTNiWDeqGTnpJIjcLb_NvOjF1K4lY2KA__ZQZrA3uCj-Z_fcGyvo0cXgqnPT_L7YTvbnpx_o66SigA4l_t4Walyl3rZszaPCUumaUdJrZxwOblYSwwDdAlnIyTq5kBLhpGyXW9Kj9jFmUURfqgb7Uc33METsTUmddaT2zisRdGJ_Blh6GpdORMmnGroxh4fezihT3p5cJJ0ovK7TBhut1ncw414L9XClOyy7u7xEkGwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwKKvlaSjGTPLPwiKIC5nH2y3Rla5UpPiTWoMK2s_8MRU-wdlgzuOB_-KOrHaY5bfm4Tqtg_aqUXaSwGIKjB9l38nbIPXbG5YUyDfaAkdu11Hhx8ydNSbAssh-KKzKRzZ94StK1OSGFa--6ZHbYmovXoOYbhgXqLqNOmxpqMkleU3OXdxXVxWnbRQVCAeqNciPUuIgEA9UOeTO-jFgUqjuo4tFScYRjdm0fIKxV16urA_KHmHsgNe3hcD7_pCQph3xPDt6cuwRnsKJBi5CmSx-GgKV6fZoYNSQgC8z3I1nJ_cCAM092Zf-oQU-FnTJoGe9wrEXsbrEewqvR4SEsMnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLeuwjl8tDKYuoRtUgQNB_Gv-qJLhmMXUGOBNh437hgFR77sEE2PF-rK5ef5xqFFphskWEMBMlO_4tauRONeiAHACJNPl-T4sC7D4PgR9QKpwK9FwjjHvhem2x2swjg3ExppYDfv5PSK_aK4Fn7BKyALvlfcJ8NOc6aBFF5FOlqnQBaz_dVDbD6PhfpjGf-detUozH6zn8rT4PZwO2pobx-9E7gTm5SrrMhIs-xYQ21VBP68do3o36dSsHmkosrQTnMm5eHWi4EjPeQz26GNU6a8J72rtpwnI2IIDzZ8BI0ITpmhf7JvSuRN5ejOLoNCER4nk40PkaIWiS0bqJqEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QBbqyuMKs6a8os9I5tgxS5qCdZ-pjCsKAdjgpLRWt085Kz7STsghfKYW4JTc2L25XDip7omJd7Gsx8n0P_Bca_RmZeKhb5-avRVWM3gxTik1qgwlBXX03UNwrWzkboDF0CGDlaFoJz0iHUwwyRy0NC_yRhdftJ0Sg7RRKlrBonnIfQ8BqvpDR0-ggbIzEpeq7cgLYVv994fYVNhFvKBOPJApnYiKMeVJY5tPgpp35JZhYGuBCfg9UAimCKM8TgDa_l4ad0PN27iKJJXcemYn6dOv4LIsjT496k-E8qpFIxMVl5WP7rwpTpbvUcDq1hfCn8OeLXhMfnHbOc4nWjA_pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=RDzsWmchpWd4sj9UqlRxTpw8CyKLgn1likbCkhvY2Ia4F_DsC0Fk03AhTui_1wTUzz9-9Eq-uWMCzWguLQz1bTcYenN0F4FJ7BJ1kAoJH5faDETV8_oL0s4nWDpK1Nvay00whEODGzYQK8D1SIRCp67a7huk59gcBsahhZavmZv3U7Yw8ognACJdQUb7DTOHTOwM9MmZKc67117HfX0L-s4_04Fp8HpUHN4kOAAJFZamKgV906Mr99rjxqPTJSPlOeF9PPnRwU0dMoA0jyI5pTbWjIeQmv1HEqW06UWV92ak4DuiCjkg_IHHspHtPlWsVkmmg7BwUyEfO3ZDfxjnYp2xszZjeDlQq4CPmiU7Z7o1Ow9Xo532zAMaq8N8SzM9YH5r7m8xQa8ocvwIcWdPmHeGdxOeE8qFvMlZdixWY8dOwuvQwW4F8YOPn__O1Dvob_gZrg0WoCbJfClyHtbzUJGicuDB7lFEWxFl0t2qs5AvMwNCrZjG9QzYki0TpzXKT3jcmCNA_yqF0oQfYIC9n2eHAveAw_eJX6IifVT3LWq8c_XjrgbwneL3EfGjZ5Kiv-OyESDSpljLzGiQf5bFQ8oLG6ClerM-vNDVGWGdo-MrJjV3TNtINClMLtf4542R8VzLS_Emex5xy4HacZnn3f96Sve42sg8jqy_On0n_4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=RDzsWmchpWd4sj9UqlRxTpw8CyKLgn1likbCkhvY2Ia4F_DsC0Fk03AhTui_1wTUzz9-9Eq-uWMCzWguLQz1bTcYenN0F4FJ7BJ1kAoJH5faDETV8_oL0s4nWDpK1Nvay00whEODGzYQK8D1SIRCp67a7huk59gcBsahhZavmZv3U7Yw8ognACJdQUb7DTOHTOwM9MmZKc67117HfX0L-s4_04Fp8HpUHN4kOAAJFZamKgV906Mr99rjxqPTJSPlOeF9PPnRwU0dMoA0jyI5pTbWjIeQmv1HEqW06UWV92ak4DuiCjkg_IHHspHtPlWsVkmmg7BwUyEfO3ZDfxjnYp2xszZjeDlQq4CPmiU7Z7o1Ow9Xo532zAMaq8N8SzM9YH5r7m8xQa8ocvwIcWdPmHeGdxOeE8qFvMlZdixWY8dOwuvQwW4F8YOPn__O1Dvob_gZrg0WoCbJfClyHtbzUJGicuDB7lFEWxFl0t2qs5AvMwNCrZjG9QzYki0TpzXKT3jcmCNA_yqF0oQfYIC9n2eHAveAw_eJX6IifVT3LWq8c_XjrgbwneL3EfGjZ5Kiv-OyESDSpljLzGiQf5bFQ8oLG6ClerM-vNDVGWGdo-MrJjV3TNtINClMLtf4542R8VzLS_Emex5xy4HacZnn3f96Sve42sg8jqy_On0n_4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری
؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAmoNp1sZi8lzTshQ1MFZKxmn4RhBmNFAvLJ7jTiovcv2OWe0prn3Hl_WSgJ0UoxLQC0iUklChS23BQ5C5tS2CD1T9GIRSagXu1pUEvMOl5VnFOAWCuhIbTf5-7A0rTBMiFp6Y2Vqlj5RdY6UvRFwRrg2Ak-X3JsM5L-P5swfkDXQ8gzVBLxERgOrlBDawCzcMbEqxjJPH4w1zwMr5OGTazkkbSggIa8sJpT4pQj1VHVe4PF8CVdMa2qX2QFz1fiDJlD-M1nJR_askrKS5hwcHBs3i5QP6RFyG17_pPuec9aNosJAw0zUiz7WqfpQjF865LVcHHq3LQgD4weuqKUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df595076a3.mp4?token=qV8bOUt_aCVVdxCwrrdOH5ECLiw9lAtq9rkwcyA2IvUVwxxDSqorvVIOb3f0llqiwXabY0qA8Kw3PoOU863NcfugQ9GXLJzR9l1zMDbIpKQkameNnqs6SBcb7uhixlgg6NTcCgi4p5aL0O1mEzLXKdyhC6gE9_Gl-UCA1a7DtUVNN1H-DaRhn0gVzl6_badUQwwEIz1H1EZMoLk5DpuqAMXjjIWVRzIjEB2noNcNEyluUJZe81KQNYLFJW5zW9tvHK6MDz4QxCgKuPlcih69msllPZxuPuvOInum38EtW_ZtDkxORq4FUbDvjReR_lugZ1PigoX2YfJDqhaV-Q1DGEY05tr9flLeOOe7DsVhPXc9qUxOKHRbqlVmgUyzjUF8GJsglwqNX6vfkGOUi-21CxvHbiMVqSs57-uewL0uJOw-bgJ-zA2ZqRN-ormjj5QEqExct0x5ysRJXTipXASRvK_oP4XGhRlQjmgdvfFtmcw5lj0yewXzcA8Qw2Bk93V_nb--LRDm6KJFNiXa4lpjvV3SeCriEu8XMgEqn811n_RIv9dGJzBDJN0pL1nZKm9MDQG_GRCqq4fL5ukYK4joGn6KMeZcb23buK_C3SMK7-F4ZP82v9DclDSrwkHBiTrf3tvLs73b-az8CAzJPBQDysFoZfgy62ffkjBnP2BVVzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df595076a3.mp4?token=qV8bOUt_aCVVdxCwrrdOH5ECLiw9lAtq9rkwcyA2IvUVwxxDSqorvVIOb3f0llqiwXabY0qA8Kw3PoOU863NcfugQ9GXLJzR9l1zMDbIpKQkameNnqs6SBcb7uhixlgg6NTcCgi4p5aL0O1mEzLXKdyhC6gE9_Gl-UCA1a7DtUVNN1H-DaRhn0gVzl6_badUQwwEIz1H1EZMoLk5DpuqAMXjjIWVRzIjEB2noNcNEyluUJZe81KQNYLFJW5zW9tvHK6MDz4QxCgKuPlcih69msllPZxuPuvOInum38EtW_ZtDkxORq4FUbDvjReR_lugZ1PigoX2YfJDqhaV-Q1DGEY05tr9flLeOOe7DsVhPXc9qUxOKHRbqlVmgUyzjUF8GJsglwqNX6vfkGOUi-21CxvHbiMVqSs57-uewL0uJOw-bgJ-zA2ZqRN-ormjj5QEqExct0x5ysRJXTipXASRvK_oP4XGhRlQjmgdvfFtmcw5lj0yewXzcA8Qw2Bk93V_nb--LRDm6KJFNiXa4lpjvV3SeCriEu8XMgEqn811n_RIv9dGJzBDJN0pL1nZKm9MDQG_GRCqq4fL5ukYK4joGn6KMeZcb23buK_C3SMK7-F4ZP82v9DclDSrwkHBiTrf3tvLs73b-az8CAzJPBQDysFoZfgy62ffkjBnP2BVVzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی درواز‌ه‌‌بان‌ ها حوصله‌شون سر میره؛
فقط ادرسون که‌گزارشگرم گفت بی‌دلیل نیست پپ کچله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEkNwRZvFgZt6W2k6S1nsEjeDuA5P6p8h6D3U8K2kNA0CokbBhHRLyLHZFWLtc6cBHhCdYxyOVYtN88D-Nn1Y-07g9VCGawSsiCxMVvPW4SZKcxqf4nba7Va7dJXkkO4ghw7EQpnFzHliRzS0tywr94YbjfkBZ_BVtQ1aENdC0KdLNksB_xZbGM09GHuMEl4OyB4u8txtrErSYmNVXpKvKFUBwcP_gwbnMYk7mMyg1eNmOWUC8NFn8Hem40eNoNljaDqFhko2qn9W_5sg4vcfAS974bMWsIaNaMLX4LoRJJUYibCmEkX9hxi0aOJu_rHi72oTGqHq-GUKYNHxL9fsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR6wCtNZ_cib1DqTeyYyiP8QXbJikTQm7P5YZjUA38Ss1IFr_lAozNwMZCFy15vjlM1zY5gyw1mmV6lCntd0mZZekNM_iN9aJuw7sOOYLMqZeeo_2O1tG8TPLzhmoBAdag1T2ZgvC9wpwA6UEBLQkFQlWpZ_s2wVx-0CHNCGh2x_ZZvrIOy9M0U01wbhsmSq8nkLns708RQydSVCEoTVzBXEMtxznAw0kDx8Qyj6QFVJKFdiEM0B0rPBFTEcH7y7lItW23KquZPYkxa4s6Wv88WKY7Ddi9oi-y_ZqpuxN5KA6vh7X5jxvYej-Dz2q6PTT-41qf3ifLrhcsJ310c3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد پرگل و مهم سلسائو تا برتری وایکینگ‌ها در غیاب اودگارد و ارلینگ هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22636" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=ru5bBmEsHtoTZ95WG53SzvuDK0yCFdlzzfULaWjjMqpukWG-lRUwpkyqguGRCFIOqygENBIdAvZORzVl-y4jphD5Dm5tNHLG12phukKOlAwmqQBacAQ06ynXzelo2Tp7tAKn5wcg9SxqxV0kVb4QVAadETXsSvvxbiNNImxvm7-QKNSOM739kOxACel6odcIIMPXHNGa9ujzfoE97d_HUocrGyhYPO-MIrq-uBeNhUvl8w_EfMV6V4DP5ZISmgX6I0LRIzuUN9DrDzkP9RrkAQVqe9zFlfUSEF1-VMTcqygW7BcROEBtjavKRBVHEQQrcm9ZXp2egwR8wgJtHblhYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=ru5bBmEsHtoTZ95WG53SzvuDK0yCFdlzzfULaWjjMqpukWG-lRUwpkyqguGRCFIOqygENBIdAvZORzVl-y4jphD5Dm5tNHLG12phukKOlAwmqQBacAQ06ynXzelo2Tp7tAKn5wcg9SxqxV0kVb4QVAadETXsSvvxbiNNImxvm7-QKNSOM739kOxACel6odcIIMPXHNGa9ujzfoE97d_HUocrGyhYPO-MIrq-uBeNhUvl8w_EfMV6V4DP5ZISmgX6I0LRIzuUN9DrDzkP9RrkAQVqe9zFlfUSEF1-VMTcqygW7BcROEBtjavKRBVHEQQrcm9ZXp2egwR8wgJtHblhYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دربازی‌ایسلند و ژاپن قانون‌جدید ۱۰ ثانیه تعویض اجراشد و بازیکن‌ایسلندبیشتر از ده ثانیه صبر کرد تا از زمین بازی‌خارج‌شودوطبق قانون داور اجازه ورود بازیکن تعویضی رانداد. به این ترتیب ایسلند بیش از یک‌دقیقه تازمان وقفه بازی ده نفره بازی کرد و ژاپن درهمان زمان گل پیروزی را به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22635" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfX_pkEHMd60il8BQTPUtCfEs7NdKJceyPvJs3HRrQpT-kxsTOrrIzeXbNR6rl45YwC2GRkVmA_ksR7ZGvpL_LveBQvIRksd15PpBOUlvKUDfuhVtfrpNgY5CZzoFByiKb797Q84Y6DIYgNJEPu8ImksVI0wfgvPoPEnXSPZVxKWwrXbU00UQCIDtyzJilpEdV3lfjp5iJTp8NaCoJzlgRRN2049AAkViILF3pIOczltjhRA4NfylF3Zs0UnLC_uhBC4TYD8VlD2e63PyZkBmKzKu9N6ebgSbOlrHCdTckQtM2V2L7ThiKEvB3QwHWUa6H4tXCbN4EOuIfiP4zJgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22634" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvuBKlZWTIjQKWGHdAQNH5iesiiDzqUoKlkf43lSic6570HxdILTnXPyKJrahLPk4Mf2AbfVVLXJHuuhLfu7e5zCyOTkG2D5BbsRH3_-sNiMhFi9z7hYiNaLJfI47NyzQIjCQ2RRHdXjqZ9poqQk_RWTs6GRH6DsPf1KJ8KeCPl5tkhy7ApVsRLqFeyfMvsfT6MJhikcy9ZuImJpXzk4CSaiYUGK2wdiemIJatvPttltut_cmrQWxqpWzjPAHkX9nti2NmeaLOUe5n6uKLI04jVZZunZ1vYAbEoZtOm7QuWC4Fce0cLqVPrrykoSuHHM4SxXOqw4YgQTnfdH46pDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=g1Fs6LWzNKbhsHa8mD3s7rASs1nxDzrN6b27AdP2WP_dQ4w-xoG-RopWWj3ms0Im538N8SlVv72DL_R885hB1ZdocLmKjznZPvsIESnB8DLlW27JTGUVF9TdHmQ--880EikOB1TFBxbh5vt254fK9pi8Pb-HTzoJiljftUjZT3Rd8_43F0n04cYjulNAP0FQAG09PY8PJSOFlBQjrsSi_muog-Eve77JNXODr_hdtjPvypge9657Vq3lCRwRo-7XsA-9j3GGRzh7dKamcqog0DkY3I56zVP-ArsZ8pputRR4hGDrjhxLqZMess8yhwpyufrEwWTGm12XDiD3Ph6XpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=g1Fs6LWzNKbhsHa8mD3s7rASs1nxDzrN6b27AdP2WP_dQ4w-xoG-RopWWj3ms0Im538N8SlVv72DL_R885hB1ZdocLmKjznZPvsIESnB8DLlW27JTGUVF9TdHmQ--880EikOB1TFBxbh5vt254fK9pi8Pb-HTzoJiljftUjZT3Rd8_43F0n04cYjulNAP0FQAG09PY8PJSOFlBQjrsSi_muog-Eve77JNXODr_hdtjPvypge9657Vq3lCRwRo-7XsA-9j3GGRzh7dKamcqog0DkY3I56zVP-ArsZ8pputRR4hGDrjhxLqZMess8yhwpyufrEwWTGm12XDiD3Ph6XpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول‌برام‌سوال شد که چرا بازیکنان پاریس همسر مکرون رو اینجوری نگاه میکنند، گفتم حتما خیلی خوشگله و رفتم گوگل عکسشو واستون بذارم که با این رو به رو شدم
🥸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tT4g9GsTI2dg05-w1-MvclxLLCVkFdoT_V_HqNvqlI5DQmgnl891EOWt4WPR6FTsw_8hMRRRxKhdm2TjvCq6qXG55DG0MT2kfE2EUmh0qf7MVLaKGSS4hBMlgUTwWBQtkSV9BsdjDYwP78v3gvvfnTr-y6b9tO8c6Mez52JYM7AmNf3im04-1EEhrD47Pwg4DZ_IEyYvZUydWGn9LW0VkSGz9lXrJfuqVRaprxzZUKxQuEPzgZ_IWFKYPSDahsL69estlo0LN-nZ6mq_fSQ0ZZjU7LsZONTfIkvStKqp9Z8bEhVzwu1k03bMs0d-gzD7KDdx2tzt2YFF1Y-HSc24xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQA2hLsAKlSlu1OCb9Y2DblO0cEczua2grZoCHMc5xKMh-JN9tpsS6M9_paF9vUrzW_l0vihWCZKwWMRkipUPVJsV_uy1fdbO2gOWiUBKEvPvY-_OmWeQkALcbRtUiLtejVDdPK6tVlrCRRcUB-llCzqYYJn3NqxhSbtGQlBNZRIGwf6d-ncGlAzVkkLsMyX8HTpfTXbpfocXMBMc2pKoUfQzQQXDm-eS2USIA-OZ5pqajNwmVD2p9uUpnxoz05OPphd1DaH7JiHNpRSmfYX26MgNNmehwGL1_GEx6gh073-NKxqwIUAlTP6TazfMTSKqJqu1G5Bnz3N8KiB9T4_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=chrfrE8qV9PSP38mNcyiIH8zq0tJhlPGhmRbE-XVkUgmx0AV4V5hk0Hig26cAPzyaQu2sx0Qhu5U7JJa_mNv-a5K_6enHbBBuvIB9GD-I_5j7eJpTm9TdpYgYrCP7C3hm_hHfPVaKKPTcmI0Gb02OkjdjrG6aHKEufFqvs3dbrvjP0KfA3cQA-HfOYk6PMZAOm5VhSRvLY03c5IqTHz9iRf-VJFk7KCJ9dNv8nb-xJ6GNPqmo94huCNI7n4aqhtMmb22wbIoNy-PV2PUpK9KBJdZxmmg-T77vWgucAu3SsFuSHOVu14yip7HBrJnMeVUWmJkQNiOEMgzm5xBaNdWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=chrfrE8qV9PSP38mNcyiIH8zq0tJhlPGhmRbE-XVkUgmx0AV4V5hk0Hig26cAPzyaQu2sx0Qhu5U7JJa_mNv-a5K_6enHbBBuvIB9GD-I_5j7eJpTm9TdpYgYrCP7C3hm_hHfPVaKKPTcmI0Gb02OkjdjrG6aHKEufFqvs3dbrvjP0KfA3cQA-HfOYk6PMZAOm5VhSRvLY03c5IqTHz9iRf-VJFk7KCJ9dNv8nb-xJ6GNPqmo94huCNI7n4aqhtMmb22wbIoNy-PV2PUpK9KBJdZxmmg-T77vWgucAu3SsFuSHOVu14yip7HBrJnMeVUWmJkQNiOEMgzm5xBaNdWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
پرس‌ سنگین برزیلِ کارلتو در بازی با پاناما؛ حتی وینی هم داره زیر نظر کارلتو وظیفه‌شو انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=AFUdzTMOr1B_8thEWtiTXAFmGrS4nmMxiu0kN8nG_4e7YcOqb_5iiSKkSLATLedQCMMpZriZOySkv1s5_4nSPKflQoX-6Lf1SyQRIWcoIIHQ5Ci6RKSQWbS3-rwelyHYeGwOLOEp5940mbWNlfc2j8mGOzjeJup8G9vNpt-DHXYmSv-O92RqoSVRv-3QSEYnZuNo3Q5sJO2cu0BCad0Hz5g3yJ0M_I3nfAmYv3RNXjb14B9GrJSfhZZjDxxnTC0c47j5iCPRxhgDaeI1AT6JUDwqICDFm0cnuAwnvSrPo3YxC3nCzKrAcrxD2dIPp9D7bzAuRTzV-Ei6jH57jqj4EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=AFUdzTMOr1B_8thEWtiTXAFmGrS4nmMxiu0kN8nG_4e7YcOqb_5iiSKkSLATLedQCMMpZriZOySkv1s5_4nSPKflQoX-6Lf1SyQRIWcoIIHQ5Ci6RKSQWbS3-rwelyHYeGwOLOEp5940mbWNlfc2j8mGOzjeJup8G9vNpt-DHXYmSv-O92RqoSVRv-3QSEYnZuNo3Q5sJO2cu0BCad0Hz5g3yJ0M_I3nfAmYv3RNXjb14B9GrJSfhZZjDxxnTC0c47j5iCPRxhgDaeI1AT6JUDwqICDFm0cnuAwnvSrPo3YxC3nCzKrAcrxD2dIPp9D7bzAuRTzV-Ei6jH57jqj4EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjOcITg7Xu9mrgUocUb0u59Cq04w9CJSuIxidG76dciETmDhZr7Pa3LvlvuNhwO9QQ7cccxIESzxb_3YTOHayQlAygoLzF2L_t9T5Mr1EeY21vreLZHQRVGsNngqzhPrh_ovG5oqlvPEGJjdZjS1zZFSdgyY4Jfbq9AYHsAAqZ-ct1-2meFJK7qQ3F3Vu05L15HZjhgkb1Jdx1aWuKHeOPFoRThvc2ZEJXIl7XgB1s_MWbCXIyCgbWEI-iciHu3ZKB6MxoJsx8MrzAkANgm0gGyDgTUvSiIO_Yl7fYd_nrmIK7pM6f0VPW5oXzB73jk-QB9idQknOV0GHP7Am03r7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbLBUVQyKTs7y8sEpdDq7aX22Z8W0GAG-R7QcuA2c3I02fTe4Zj8hYYNfspvZ5VRJ1Z6_xvjvywG1sYPakzFn9CRyFWen7ZUIG0WMTv3Tl28ZsxyMu7DCLxSspUAgcbpcl0HaAAehVQyZr95G4txxCJhRQoBhCxF1z1VcCaFX_S_fsYFbv_KLZ0SZTVzYBCsASUDmJvKffH0OzQgFevNgmwCWlbJC6K3Wv3vOpWA74_xCMkUYdH1WPlJDgY8JCLE1PUo0tQlbrCO-Ehx2wwRvftUYIYLtVYpxq9bNoPuTaKj8aHxAM74G2WCRtIewcJOlmUggaErJ8QP81FQ4aoTKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=jWe_H8PxqdEv0yks1av7XvdM-MVOWeeXz6jT2xFt3prZgLokpAD3sb3sVpdCvXIr5wfQ-4SE5A4RxS9gNjwLLCCKIe34uDPlLRtC3zTEASGX43tzJDlrPscHktU0iL1xzbXz2NcDVBlHj0KfAx_U_Y2QhOvtG0RIc9o5lk7yLHJSQDTu1R94Q_kkasNOzZcDB2i43JDpblnGxohc8akZIKyhZG9PLWOeXgtktlYd1bVfYBoq9l235dsx3Tqs4f-Uq1v-IoW70DO8oyfpy_5ekOHW_lXkXI_e8pndLd0FIkaiVQBY1QhwurrVZyk6_iivAnVx59UghtsFsUw8DRMfgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=jWe_H8PxqdEv0yks1av7XvdM-MVOWeeXz6jT2xFt3prZgLokpAD3sb3sVpdCvXIr5wfQ-4SE5A4RxS9gNjwLLCCKIe34uDPlLRtC3zTEASGX43tzJDlrPscHktU0iL1xzbXz2NcDVBlHj0KfAx_U_Y2QhOvtG0RIc9o5lk7yLHJSQDTu1R94Q_kkasNOzZcDB2i43JDpblnGxohc8akZIKyhZG9PLWOeXgtktlYd1bVfYBoq9l235dsx3Tqs4f-Uq1v-IoW70DO8oyfpy_5ekOHW_lXkXI_e8pndLd0FIkaiVQBY1QhwurrVZyk6_iivAnVx59UghtsFsUw8DRMfgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر ایرانی سرمربی‌سابق سپاهان خواننده شد؛ همسر ایرانی خوزه مورایس که یه مدت با تیم بانوان سپاهان قرارداد بست با انتشار این ویدیو اعلام کرد بزودی اهنگ جدیدش منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c62242613a.mp4?token=STzHTjNqgwd-xFYKe6EgSYUh6vwUWmwo_t9fsmC1cvEmIryVxu-X9_iBBzi_yg4pED70yGRavFLvbEw3048GUFZhQYrNtkh73FQPW1MN56J2nlelGcQyUZxhIa3BZy5xpLyps4qfV1GBpI1M76zPAftiO8AIvVDVHGQgtu-uFnnA3S2r4eUKKT6GN5euoHdsQ4xleA3iRpBoecR24jESF4aGYa5Wc2T9EncyFTXjRqXEibWIrnZK9YSBlPBKzbJVPVDfl9VtAHozUxyrJNs3KvlVsD77wYNVUM6t20sqYNybZiCNPYJhO7YlOb2ost8HlbuWzj2WnftFz12CMpMhlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c62242613a.mp4?token=STzHTjNqgwd-xFYKe6EgSYUh6vwUWmwo_t9fsmC1cvEmIryVxu-X9_iBBzi_yg4pED70yGRavFLvbEw3048GUFZhQYrNtkh73FQPW1MN56J2nlelGcQyUZxhIa3BZy5xpLyps4qfV1GBpI1M76zPAftiO8AIvVDVHGQgtu-uFnnA3S2r4eUKKT6GN5euoHdsQ4xleA3iRpBoecR24jESF4aGYa5Wc2T9EncyFTXjRqXEibWIrnZK9YSBlPBKzbJVPVDfl9VtAHozUxyrJNs3KvlVsD77wYNVUM6t20sqYNybZiCNPYJhO7YlOb2ost8HlbuWzj2WnftFz12CMpMhlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
بازم‌ این‌یارو با هوش مصنوعی‌ش اومد و اینبار فینال چمپیونزلیگ رو برای آرسنالیا اصلاح کرد. اونایی که روی قهرمانی آرسنالیا شرط سنگین بسته بودند دقیقا یه همچین حسی به این بازی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlXggvXkstZhYNZWnJj9DOTS-h-ja_jYZgEX2qzQXk_976qQHc9tlwOIGd4C0NEx2xuA2Le9rObo658MBP7golmL2JX5Rj-EjIVYKpxl9l6CUorlC3jRKqhhNywklStDoDx7BWrNFVjwj5NwQkAgvmcatefvqR7KjaX3vXpLwtCnq-ORmnBbLKfuQvMibSSlz-F8PCBhfDdbdVQaDOrKoC4LDoPxphUs2RALeoouFtlMWIlsF7SJgkpHkx8kgelbWEIku52qWd-Z7ci08yTMVeAElw8PO3_1GXvXvg03SEvioKwzvzn0ps9OBEeAz6y9S4QDOtVr8WDJeijxpoxG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22621">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGY6_wpsuoCjheyxW-I0TrPzgFN23OP1dnElD0F2TUX_FzYOCqjWaR3nKXN9G-mop5lM41XwqD5u9k6jdZhx3ZRfR7OtPglaV13O2yFJNdymLf3MvKooKxiHokhxOd-pMrZhST5AtIcuSohHNHaaz4PLryiYeDMbwLSBY_2PUqO6LYcMzTkJhQCXRugdpFx4EYOq6-G3AQHHRWimYhuPRHNT8nyuXA1gPoz83rUIbtjd5sP4EtSDZC40pr0AymMhGjhluK624AO7Moi5uCO18Dk_Q5Me-tz7y94ZtiVWFx_KqIvR28v7B3w6raYEh3XNrDop5cWXsZaSjU6lan647w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
‏پاول دروف مالک‌تلگرام: حکومت ایران تلگرام رو به بدترین‌شکل‌فیلترکرده صد تا پیام رسان ساخته ولی ایرانیان هنوز دارن از تلگرام استفاده میکنن و محبوب ترین پیام رسان بینشون تلگرامه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22621" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22620">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9DfuRHFjbavY6VSCIEXRTDKAbcFpCVY3XgNqAUrgXN1Y9IwzYr5ZJFGXfbnJYEm9UMValxg2AQ-lQ4ZD6tM_hwGcbxxic-D8RLWaiJ6hEKZ9UVZnvITWWFslDaUeRwpKL_TZ4NtzFSJnc97uMAQ_vTn2Ppp6RKY60EDv8JPWinRfxa3sGpX6oUMeLL8jEkecF3DUxdFJCkHLEOGKm-Fj9khfWvNWozjs6v3KdrEdkZMU6pSHvXdbr1v2KitklY9dbu0FrIG8vDBSLe-HBC5h2ec3I51bqeSqYjwedGDeE4jBuQ_5AxoK8GA9epytiLpjm30pwTmKBJ56JKns65bgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ با اعلام خبرنگاران نزدیک به لاپورتا رئیس باشگاه‌بارسلونا؛ خولیان آلوارز ستاره آرژانتینی ظرف 48 ساعت آینده قرار داد 5 ساله خود را با آبی اناری ها امضا خواهد کرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22620" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puy8cZoWQGVoifMsdBL8lCEFHMCsxoJoCwGo1NzDahlemrOwzzezFFxrOcr8BKzx47qwPDbLacgRX1l5pexR_ANQzwCA5XwJzE7RRwqvj9UyaR8UatuMG1sPPl_2fd3HUBHymw1Zi0Gv2XewDfR8FjHfTuSe17PyVJHpuQtyPuHMchlQUrYXHos4Kcxd-oKSaFCflWSBTm7TED4ZTtnscKMctb0Zo7inyLb9DeRCRbS8_rhnsirOs0qVomVEKdwwobQz4PatH_95sZnexa-LvvIkvbrlNDwEVRoSVWeOmOETijt1iw3tKTMjIo1bGFIXxbVLtfDL0uKON2IVgCEmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22619" target="_blank">📅 19:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2eOdX5njjcRZO61eW8m_AJrgrCoshDiF6MONpRrGXlwcY3M4OppMTPPldfkPjei88orSSlKYlq1KCIOjV0dQ2ailTF7DylqOWwKOxA0R8E57rxq7_HqrrloGrvZEu0RVQ6kDVnB7MHjThqgusbOkmmKKD2cE4Kj79oLPfw4XnKn_mUH3O6GSI0tHumVMmTYC38yGaCY-gKRQUt-_ZsJUZDr-Wp4yo5z3fyxuOJpfV088D2rzYrgSZrpea4q0GR-Qpx1SVNXPbK4s8aoMr-Ig836tJ094g3YEeAOiViDa9GOMXoExHBoCBujly7za0LbA9ZcBaYR5O9mKGLofsOdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#نقل‌وانتقالات|مدیریت باشگاه پاری‌سن ژرمن آمادگی خود را برای تمدید قرارداد دائم العمر لوئیز انریکه سرمربی این تیم اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22618" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514074c458.mp4?token=NVioAuzSDKJR7XCZCrYFwsbKKg-G2PqA5dWO4LSvf3EkijOptPPBUGO_AM-VJbR-NALH1s2Yhg7zfCVmWDcTnC-6uSmLVfizfcAjK2_BqmlVtFx0bKHfqTEZze39LGLacQHofaUOE49OLUO6q4q_0BxpJUJdLGYsqz7tD8-Z3Wpz8rl6tS8W7tiVktq3IQZwP-6U0f9jQ4v5ZDcsQzvOw-0B6bpsMnKO0YJ_d_ci6HhtYPsSuKz4p8bF2cbAl3sXNKHWrOLdO1hgOUbrgEsGdKsYV9zXomovLTDm6LHoL4-BjQNn6eCmclX7n4oUy28G3B82Q55NBy68KIVgeHO6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514074c458.mp4?token=NVioAuzSDKJR7XCZCrYFwsbKKg-G2PqA5dWO4LSvf3EkijOptPPBUGO_AM-VJbR-NALH1s2Yhg7zfCVmWDcTnC-6uSmLVfizfcAjK2_BqmlVtFx0bKHfqTEZze39LGLacQHofaUOE49OLUO6q4q_0BxpJUJdLGYsqz7tD8-Z3Wpz8rl6tS8W7tiVktq3IQZwP-6U0f9jQ4v5ZDcsQzvOw-0B6bpsMnKO0YJ_d_ci6HhtYPsSuKz4p8bF2cbAl3sXNKHWrOLdO1hgOUbrgEsGdKsYV9zXomovLTDm6LHoL4-BjQNn6eCmclX7n4oUy28G3B82Q55NBy68KIVgeHO6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
5 گل از بهترین گل‌های فینال لیگ قهرمانان اروپا به انتخاب پیج رسمی این رقابت‌ها؛ نظرتون کدومه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22617" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7zPLROLzOp1Vd9iZMGVwrDvBJu0PR6ejCaNBQkCkZUB_1ePYzH1WPzJw5mnTjqkS-uBhtsQxJKx2ZsC9Qqrl3cfURJvEqpdSXsoLeuV3yMfz5b6QH1Aq7zzBSHOk5UPXcjqfZ5x9C8AE858auCYyLmpCEXUwX9bYRqGH0UVDWezBWkhs1ra5UYbEyLYq2jsss73Ini6dlqEnV98gskjpGsr2ufpFm7S1iBPU_qCBrVWrTXmwChKWCtPR85Gmaq8m_PTTLgi7k7KT5QPKaDPVPZsSIcjQUKaff8m00HpyUIEz6E47pfIMB8u38fMFRqsML5u2ZWnUNUU3CXGdUdd7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=lUpNJaqDVVQldT5FRAVEgeoqjKpUwMYcM3L5J4PdtjiA3As6VvL5G0AniRzIWh_ePU0X3WcKlDvYerEWoDV1CMEXvnSft_ddKAQgHqnm1GG23AD-J-wgQPh6UwQYpo2G39HJz6oBQLZISwjEJqqm4AWb4jRLqwxmsfrFl7PFfEXCBol395znZVbp9WzB2X9uTs1EuXSKbXJB_XMvVT9FQnnigVwgVQGdsV9oWkN2JY_6K1XGk6UE7ZpT_kojZCcWGT5jshvYiOvVybuNI82f0MNBUClvCaoKb2cjA68jYLklmW5Dyj32lckbc9sdhxwFppdDC2b5XQQSkMJGVeNZGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=lUpNJaqDVVQldT5FRAVEgeoqjKpUwMYcM3L5J4PdtjiA3As6VvL5G0AniRzIWh_ePU0X3WcKlDvYerEWoDV1CMEXvnSft_ddKAQgHqnm1GG23AD-J-wgQPh6UwQYpo2G39HJz6oBQLZISwjEJqqm4AWb4jRLqwxmsfrFl7PFfEXCBol395znZVbp9WzB2X9uTs1EuXSKbXJB_XMvVT9FQnnigVwgVQGdsV9oWkN2JY_6K1XGk6UE7ZpT_kojZCcWGT5jshvYiOvVybuNI82f0MNBUClvCaoKb2cjA68jYLklmW5Dyj32lckbc9sdhxwFppdDC2b5XQQSkMJGVeNZGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدئوباشگاه‌گلف‌یونایتدحاضر دردسته ۲ امارات برای رونمایی از«آندرس‌اینیستا»سرمربی جدید تیم؛ اسطوره اسپانیایی وارد دوران سرمربیگری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imLFj8ViS-mlaT_KZ9HWom4COCuELm55l4DlDHAChfFIxYHTcccWyyvQYhlc5VYsz3j1ABPvCaktVn7t5_yi9oVNWPbJOUZTIoDHgfdBQJn5HVj0sk6_NNOT8HOmbYN978AWAMSuoAnd0KDI--eiQlcbORaPqLzn62bBJ0gHVrji71TcjwfO9qaj1GalKR5laMDBKy95oXo8DxcSQRyRPBgDwKyg3eucHKSDUDGCVlU_EXtocw7A4gggzZ5L41MJkQJfo-IEeQHkt6N4G4oc3HT5CNhULBuIwa_AnfYn60N0VYymeqIm6KHRaRgWfqJYXvg3C9bqLbHVVRJitmPcLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=qM8xF7hTv6iKqBKjhoqSDlFXflJnvTYJ7VCKcligSGt3EfzHAvGj3exrLKrTUMbSqQBF5rXaN458bef7YGDQ1pyAAVakCaAz3cnyRZMSgamKFBShklIcLPl_tAahWNVtVuGCeR2WmU3Ks1f8-ZVLuxzvHd26u2djl6JULVgN7OJ4z1CGa-cynwiHZvNWdfMPHiSalmKw9Go9FAIbpaGgje0SJLQlgezpti4ZRMuF9sz-ymULk2l0FRW3--1lOwrwMRzbqYkSKnKdFJX_uUHCeKQ4i63XK-AP00Gi45Mpua-VWNHT33k7g0M0rOyHtmpAklcsInC6HhHaVYUMHiGTYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=qM8xF7hTv6iKqBKjhoqSDlFXflJnvTYJ7VCKcligSGt3EfzHAvGj3exrLKrTUMbSqQBF5rXaN458bef7YGDQ1pyAAVakCaAz3cnyRZMSgamKFBShklIcLPl_tAahWNVtVuGCeR2WmU3Ks1f8-ZVLuxzvHd26u2djl6JULVgN7OJ4z1CGa-cynwiHZvNWdfMPHiSalmKw9Go9FAIbpaGgje0SJLQlgezpti4ZRMuF9sz-ymULk2l0FRW3--1lOwrwMRzbqYkSKnKdFJX_uUHCeKQ4i63XK-AP00Gi45Mpua-VWNHT33k7g0M0rOyHtmpAklcsInC6HhHaVYUMHiGTYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAoYnc0UvUEs2Na36TbzxifZ-7NKiqxJU-8SMy0ZcSF8VDHXm95PLucadNIaWZ_9fz67FG43R8FXqAVd9X7YmDWOPPs7xH2_fiH_U0Z4yEp9dku-7GTjQXDWkQTMR9J3643vW9d-zxc9iGaoOegYmYfpygniu0sfir6D3MH3fVzZMNtp-HH-oRS2RQbov0Yy5x40uAuiAXlwmpkIftP3hiEW8PSQVan7Lwzyq-sRerJIwC7SznOZR_WfTBlvVz5EdS8brZes-Ynya4AUCqWp-JgDCBjNLIDFZ5PvfymaLynTMOMD5OCK5tjr2lC4S0NO7RKtHK44b-3oFLoNbPYlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2Cpacok7yjgflsZ5DhPoWTC0HQV7NeAsR8Cg0IIx5okyoSt30waU-tDQFheSVeT4Y53Eq8yxCiJbcp_avKTXoYp40l9RZXQFyrOEGC9U94Z6j8TclUN93KUocFoDnuNYpZirkrQrmG71i_MATU88SIhEk1xJay1pDj0E8bSZt-No2-sCHLld71x8QxQYQXRB3_ABiI5F65RzPAO_16mD8EHJKis4nOBwF1Ceuh4cHhdHJyI2PIM-FQbcKjWCMcz_QlpQOVtF5v8-qOG_aGJmKaJpSD4Gwhr9Cfo-3rUUl7yhty-u-UNLYtHoaccGTgdspDkA2s2ZDm0u4sk78PDGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxU0UW1aF_7Ut1QRiOTpLU95diWGblpHgVF-dWeYZVxW_X4UWw8jBXAlPkUIvW3fMH1uec7WYwzkpAhEUlkI2BP4BI25ns_qun_BTMwAzyhkpVZCLPYnpW0cAl307uUEcRFh76C3gOws2rO-fx9q7XCB8osrdCcpJl-Ou7NhX9KgodtQVNhw-qDLU-8F7SMSqvllAbfgUQQg2OlqVmbJ9d4y9yd-R41EBuCmSXkjPE5nIKybdGCp5VtXr34vipt9AohPARsDyeXoKQMMni_Xt38Zlfhs5lcpsNwKWyJopC-VTgbLjsxmZQ8zWdEf_SWBx8YerQjZr6kC3klmvEm6Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22606" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cO2-oF-VhMdSRocY5BUCPVIqeib5cEs5u_sta4DvorUzGf-raBCmWruAhLB2QFi6IRYR9nUCPnFZSkN4X24WtcleK8LnL9u0dVOj6BEoVP77HeyZzCEShXcl8UbpwYaIk_zoDpfoZ9TztqdKqLIHNVgMPYiu2kovr1nISsBBLedAivPbE5dJPs_omVQfW4w5Z80TDcKd3_Gi8iGTISnBfPJiXdtfVMA7_EYN03Zjr2LSIvxMtp-rPuXBwXITGxBXZoiI_3Mzk19X-erPCTIVoqawQM6m9ClLfxBazF6J7jDPvRxBCgoBK1JcSc3kvxgls1x3iFSg_P8Q1P_P5Vx1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارکینیوش کاپیتانPSG با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22605" target="_blank">📅 15:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHzm4vvE0v3iV9A74iTEc13L6F5LtP009oljT-U_oG-ZLGB71CJ9O1-kw87ddlyeM2wsUCwZpOdQpIeD3KhEjAnv8NFQ18MAhZczZAhtlq1PwJ31Txa-LgZ413eQRjzR9spGC-RD8UKHMkx18sae0DpDIPGT4aNeApoPR_8D7PGvKq7sprGOEpyW_d8ApKCwJcbUnYB2-0PPrN7p_GTo2NbNnnVl1-ylQsRxPtjBqd_f4Q_qetKoTl98BX95y-yswFjSKJDzlNDZfQaEbTh7kPsr4pvgNkcIgkO_tlygqGhCZ-Etnr-9hLNMImbpNkyGqji_TgmgHigO7mV7TnbobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آنسو فاتی ستاره22ساله‌موناکو تاقبل‌از شروع هشتم؛ با 5 گل در صدر بهترین گلزنان لوشامپیونه قرار داره. فاتی در پایان فصل به بارسا برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22604" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBt2Y3yMvktqePh4VzK2sX3y_qxkYJ6wkxnJCd-VGx4CbWVipJdA-8y2s2oNGx469POdGMGFuVje0gyxk3VYRbEOEN3iVK5oK4Tzro-Jyckc2OU7YLi090zH91vPHlMObYuQLNMhc6bRNIw42c9MxGNj6whBNiSmF8o6CMJMAiZmnHLbajgT0ou_Pej6i6ABkcTBSTtFHSJn9-6f-0YP3nimEMxpqf_9ePl1UDjZA5yD7HFNwOepGXZM00QMM4J7MOIGpt1Yxm8UQYrq-nUic4n4ciy0HGR2bnVA9nekKrKR43QUz82_d-mvkCcxCD2VisQTzpYmhvvlvBhhAB-X2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22603" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUfuYAIK98MWYqSmoxkDkPlahIa6GphIJtGV64yVEzteHkaeHWFt0V3ZRjxsKhv2QrWP07bhYp2yGpPTnbjQEfnRi72TkhaMkQVs_Q-9ikvdBTYl1-dzdisHgx_Zpc5LOWmfYAd8FOvCwqR7EoXX_on5buul4KCLi_diU_pg5wJUy3x2latJ-ZvrhiqlPV_kCc3cOXZjTuZritSbtYWyT2CKkSHbnJ-WB0hipox_if9c62Xcn1NQkP-CB5E2Pz3iEuiwqzgmUn1ji1Y7kcbsp-LGC2_JgQGPqpkbfu3qrw1ONjwtJtCcCSpNCYMib6T-b4MDTmdZDAqgoWOgdACyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هرکی‌بهتون گفت که چرا اینقدر به فوتبال علاقه داری؟ چیش به تومیرسه این ویدیو رو براش بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22602" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dddYp4fJsJ8mt0-R-w9INntRTCdeoikyW9xLcsV2pjs4uGmi3x5yzjqs5dH7UB-xMAYGLwUjKO_1wowZ5EUj80bqqXHCTnKcV5aDBG0Mdr-7y-ZoEvSW3xFXIiwSv3E7ySpPJxJDNAsmBvcQHc_nbutIrXnhPjO0j2zXY2avez2ieIeDSXM5bSCHpSfvD06SRAKZxPAmXXWtKd9debrDsxNzw7FvDUTjH5ObijdsFsU3WBXdacDriZUdLUGQuQvHVmgcjrALRRPjM1y4u7ygkibwf6GzKMmduGRMUD0Q3nQigqjap76YkgcNe2Pe2RKgOjoQWdvdSlteRrTnV3AJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا
: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22601" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=rUs0JekmHckQqUva4KLQvyI0HUDv3-hpIJlhRnjWtTuLVXPKjvPYB0ppagwqCZH2Em3bNNR87uaPWD6Lxxh3fawmiQliYUmS0mUbm7aA1bXVTE1g_-R3OsGn9BE4aGPIytf2pEYBijF2efmTTk68NfqopJ-8bfbeXwCEAcFPbDNEcJJaFHlbeS6E2XkRlYyTaCCOCSoRSf364cfteGRCHETpSgOmGAtoJ83qRAGjhCN0BF0cVFggOWCRRfav7k5WQclN9ft0FpDaFLFjo7vmgNUZsiV3QyR0hMOSltvEEGpjOh_0kafoqZEuCAA_7HwP2lCaoHs3j1SUuruwI9g6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=rUs0JekmHckQqUva4KLQvyI0HUDv3-hpIJlhRnjWtTuLVXPKjvPYB0ppagwqCZH2Em3bNNR87uaPWD6Lxxh3fawmiQliYUmS0mUbm7aA1bXVTE1g_-R3OsGn9BE4aGPIytf2pEYBijF2efmTTk68NfqopJ-8bfbeXwCEAcFPbDNEcJJaFHlbeS6E2XkRlYyTaCCOCSoRSf364cfteGRCHETpSgOmGAtoJ83qRAGjhCN0BF0cVFggOWCRRfav7k5WQclN9ft0FpDaFLFjo7vmgNUZsiV3QyR0hMOSltvEEGpjOh_0kafoqZEuCAA_7HwP2lCaoHs3j1SUuruwI9g6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
اکسپوزیتو زید جدیدکیلیان‌امباپه ستاره تیم رئال درحال قر دادن در کنسرت روز گذشته بدبانی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22600" target="_blank">📅 13:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=aSWzts4x_ZcPglnjAz-B8IopWoo9ZcUMT5S_JevE2RkzFuuMlggUNHT3csRLeljhKZcLrCG9qBDe_uvHgIvpbedBAeqqnUrQaTEgoaRwnwtMklFI_xq7LQVEzAter_9Av-MbOACJSZxe6Lv2fPMAn33IHwxFkjqQfvVQ7KnKPGawNQahW85bUDJx2Y-uxnfHXcih5xBYhsQSoJHF0l6j16YQxJSiq3OPSKFbJp9mJgxevr8h2IvKyAwILKbOcxzaLnoAHBXVb0M4Rs2SlrPpxl0k0aUeB--Y0h2nsADd4ySUnk-WUHI_3w6r3mEpuuHKvN9GHUFw40rYAPWC3GbVBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=aSWzts4x_ZcPglnjAz-B8IopWoo9ZcUMT5S_JevE2RkzFuuMlggUNHT3csRLeljhKZcLrCG9qBDe_uvHgIvpbedBAeqqnUrQaTEgoaRwnwtMklFI_xq7LQVEzAter_9Av-MbOACJSZxe6Lv2fPMAn33IHwxFkjqQfvVQ7KnKPGawNQahW85bUDJx2Y-uxnfHXcih5xBYhsQSoJHF0l6j16YQxJSiq3OPSKFbJp9mJgxevr8h2IvKyAwILKbOcxzaLnoAHBXVb0M4Rs2SlrPpxl0k0aUeB--Y0h2nsADd4ySUnk-WUHI_3w6r3mEpuuHKvN9GHUFw40rYAPWC3GbVBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHWo-C22sS7idoUOZcPio9NeEW-tplVTFsdI8JnjlpRV5YTnv4XuJ9_uvVisL3CRwEtruyoGYJYn62gwoJE9_Yp0usM85NSDwShFsvii1_Gll4jhYLnM2KozFCWarmNBf0y50_EtOVfYPIh93JS47Xw1GVNwXh_XUeeoynXQN2AShkMfHrpPjNbojmHqMXzYr9QGVpZT5BkS4PdVVRvw9RHTexxqPSSYpjZL99ga_G-MNcaPA6DYN0NUcDUxzCKVD15XBiakSKcW1okqFR2cDRkPmXkI_CScBxCCdfmwhz9kvuRM-A_Nyk0R4aa6Ybef5CcEPinEfzVzxTcYh6n4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=tZyShRDa8fHNkcO4Yg8Yj30Lu9N4CX_EJ5WCSl6KvXvbMpYEvVVcAQWeS8hyBMX5QZRD0kZt2cwqmiV76S4PQZZsNi8UDVYqb-TCXNx56C_q_I7kgKdsCPEB1o0sxoP6jyvAUsqze3JVHjVPD55U6i1JFDDR20NrJHLli0eMAwZw-WS5GP0cS8EpCLqToIYJnJ97EEL16_4eSLxSPSieAeuz4jlSUWvIZDxVOLcxXHUPqA2O5ii37GIU04Jj7dkav0aDf6EghV48l0RIVxG04NUDf4w8JQ46r_3KdP9GBrRUcHxvAg97AXgQD8E3xyrBn3aFXu2mOwggSO8u_6fRqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=tZyShRDa8fHNkcO4Yg8Yj30Lu9N4CX_EJ5WCSl6KvXvbMpYEvVVcAQWeS8hyBMX5QZRD0kZt2cwqmiV76S4PQZZsNi8UDVYqb-TCXNx56C_q_I7kgKdsCPEB1o0sxoP6jyvAUsqze3JVHjVPD55U6i1JFDDR20NrJHLli0eMAwZw-WS5GP0cS8EpCLqToIYJnJ97EEL16_4eSLxSPSieAeuz4jlSUWvIZDxVOLcxXHUPqA2O5ii37GIU04Jj7dkav0aDf6EghV48l0RIVxG04NUDf4w8JQ46r_3KdP9GBrRUcHxvAg97AXgQD8E3xyrBn3aFXu2mOwggSO8u_6fRqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8DNR2FPSHl8_Iah-CzpgEtso8ZkPaAG8Z7sCfi5lci3Mztm6ABCLmnU5IVw0qkt1fMhfSI26pywZZzbnmaMc09RWdih4uTQsrQX6Ewu66WzqyH10TQ-c0COWmqMbYeGjEua0iBU3K7P-_U9ag9Q_5hNgG2PPWvMGbjQCPOPCdPhoo-59VRFiFpcZ4L2M6AuLebgRedZrhTf2iIFzx_6Po_Vp4JNqnhnmGlivXOuCeelHVfTkn1khytHYI81jqxUdZLs_4KNh2tbpWXpKaIrTbVq9x03Bp91awMyqNUDHeL-9KpJ7xVRyJRp1cgnM7qSZKxIw_Kw4GjBetH-qtuQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjsbS8gcDwAvDcaP67eS4pz0nRpMrYbGbto8AnArm0Pq6CebDnYQHoa5KAfndOpIz0evhwcsyH3wFoD9MkAKjGfAnNUurg8HhOFzZK_aFrRvgxW5VGjgVYwHqI4Zfp3LQ1_3rmFi8YyDpJkxyO9OV60uCKvif6TPVxtSuHSOaU48Q1Rwt5w-0wgYz06ezpM7CT1oc5DEaz7fykcu1sboAf5CDc8iLeKFSKxkTUwYA7O-w-NKskWFpTzdgNVSeZDKL1oyluH0gNpkHAkevBy5P-BW4zTJZwBjHNS8sO7xREqq9XH_sXZF-xYtcbNiH5DNPyv_90FHI7XSY5QQ1G8yTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22595" target="_blank">📅 11:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=ZoDaoGKnDrVvr0s7bbqbpiN7HcysddoGPTdfSFB0DnkIC3C_FHnVHKj5RD9TCp-hj9ht5nRgPvJQ4MA8JHa90Pbtm6Q75JAdf6KX8nTw8v3bNmgDIUnOexjgti7NSI64L27AF20-szVaB7e27_Of3_fZlN3Vo2XfcHwwytZC9mMwaydhZF7qLdWSd_m1eg4d2Op4jFpvCwbXtmyXgEuyWx3r-oSc61dRaA0eKOzCNRkZYqbUvxW1TdwiVAjWSc00pMEO7kQZx52YQE5kLEsmQnojcSZUnE8xIO7nPdYsIplm07fDU9iRutLPGBnX7-NvPh5spAKaMZ7svSs-jd6Sh1xLJtbq4eOq8WJv4Ox2qUFlGVz4I1N0AqLb3Wzw_JPb1SxO1w1ADIjbyOpwIM2W2cx-lIbUWd_r-0PLOvgcGEII_amhkkfQLId3jsqdxhHpdUdi4lNRkc-ung0AsiBegkUCjImqo1T9fktdiqURXqoQ6UVXryOS_jBjAFw2qwPaHK9yWk_GDY3OPm-sxhEmrjh44tMi0w-pmbXJCDU1vh4iEDh0u3FMK0z-tayxfv13-CktFgBe0Y34u2E1ony6PoKyJQIsAb-x9Nkai_zDNeY20cPVaSmb9FTorIKxaBfWTrhRN6sd2Z4GNvOiQcxLb48mWbf-cgY_buDSNGb-324" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=ZoDaoGKnDrVvr0s7bbqbpiN7HcysddoGPTdfSFB0DnkIC3C_FHnVHKj5RD9TCp-hj9ht5nRgPvJQ4MA8JHa90Pbtm6Q75JAdf6KX8nTw8v3bNmgDIUnOexjgti7NSI64L27AF20-szVaB7e27_Of3_fZlN3Vo2XfcHwwytZC9mMwaydhZF7qLdWSd_m1eg4d2Op4jFpvCwbXtmyXgEuyWx3r-oSc61dRaA0eKOzCNRkZYqbUvxW1TdwiVAjWSc00pMEO7kQZx52YQE5kLEsmQnojcSZUnE8xIO7nPdYsIplm07fDU9iRutLPGBnX7-NvPh5spAKaMZ7svSs-jd6Sh1xLJtbq4eOq8WJv4Ox2qUFlGVz4I1N0AqLb3Wzw_JPb1SxO1w1ADIjbyOpwIM2W2cx-lIbUWd_r-0PLOvgcGEII_amhkkfQLId3jsqdxhHpdUdi4lNRkc-ung0AsiBegkUCjImqo1T9fktdiqURXqoQ6UVXryOS_jBjAFw2qwPaHK9yWk_GDY3OPm-sxhEmrjh44tMi0w-pmbXJCDU1vh4iEDh0u3FMK0z-tayxfv13-CktFgBe0Y34u2E1ony6PoKyJQIsAb-x9Nkai_zDNeY20cPVaSmb9FTorIKxaBfWTrhRN6sd2Z4GNvOiQcxLb48mWbf-cgY_buDSNGb-324" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22594" target="_blank">📅 11:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo9vJ6yZwDmptveJGcSK5Ti_PazWORSUmnpCCb8xL-t8XVg3v_Go3M0f_kQOYLFPDiKnPqnz32Z0NRNo2owWCWhViIi3sSbGKdEJCOb4GPmYIyun-NO1Jq2qVdfktzFsH2Dbmej3BGl84L3mkD5soFWBxBV3kZ_3Fk4wy-5k3eY7LNHtQAG5ASuTy4kJHWmmk9A_OzFJcn95Xz6bkHXjd9EpoBtEw2vw7TLuqJpwwjDszBku2NOm-m-jUA-wBoDZswRpjB19zKK6dNTT8XILi92Jrki0yWayPKYIwZ6wORA0C2z2NZeej7HTArw7Eb9i0unFubbK83qfO5gR4Gj5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22593" target="_blank">📅 11:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnc4QtQPPZtu_Hzz3DjIPRrZcT69NwD8dES5817EIncpzkZKMfw6BwJR04rqjpxNqUCjxmEcvJNSZ2rwCQAPueKJai2akhyI66oK2HhYlfWkIsx8n2Hc7uRLgVVS_2OF3-oDZf7j235hOr72ByAyU6_c2jzH-ETM_-0k5ngGTjnYe2gm4o2PRLBR3FlAysjzhvod34Ltd90KwmAMt9OU0tYFmLhyDNLHyjKtj1ozY1Aqv6l8xNRFVodecGSsI0kVyUGm9eM08vMa3OgE6QMcE0d11-jnUPTsaE0HO_TDNKpp__Jmgp4NsYMPDKS7E_8IxPBSkzNi5xv5Yf2E4I4c4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های حاضر در مرحله یک چهارم نهایی رقابت های جام حذفی؛ تراکتور تبریز نیز حدف شد!
✅
استقلال، فولاد، شمس آذر قزوین، ملوان انزلی، خیبر، پیکان، سایپا،گلگهر؛قرعه‌کشی‌این مرحله بزودی انجام میشه و بازی‌هااواخر اسفند برگزار خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22592" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3bWQPSvYJYE2VhS3LSo1fgxgZG886UDJDhlrFQrMxSOcFvk7w6GoGTKbYFh4I9OEvn16bJJ6YpOfqBWmKN5NjWIt37z5aeh8p4-uNq7bXhvU8g-pJKs95rhuiRQDUUAPQ30oAsvwXfhk5yu1_OZfvRkFjnsu9mWZKYVrNMZ_v3UCWE024-r9qmN6u99GvrR5-zlBH4yvZ2DgqiaN1qy3LaBTDHleFn14-Sh2iiGx_0L--haou6kpEiu4GnJtnl66zpHN6xG1GGf2_eEFzaIPvMjv-ToI_SGJwLoH6CF3frDbVMumA50N8Kwn0Mg9dyW4eyhjoLnrqB1KExE71egfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد صلاح فوق ستاره سابق لیورپول از طریق نماینده خود به عربستانی‌ها گفته هر باشگاهی به من دستمزد سالانه میده، قرارداد 3 ساله میبنده و تیمش روبرای قهرمانی میبنده من اوکیم که به آن‌ تیم بروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22591" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMGChURU5Ru2pqKongdD05xrX6chpyQNcE7zeiUAHHdj_NjwkZp-xvbAkaNeE7-CDSKkQLbAqaBfBoRsZBhKL4x9TLyW-thc2X4sByyq1sbIIsSWxZ-dDscXkk_JbGmD2PymIbTvDYdaIdIsJMwtoer5Ms8mR2la_DyJpnP_61T1jAs4QgnhTE9BGnrR91PUkrHLILN_bgqdSa3LcTS0IDncWoDFPuV6OUAUNvp9WnqcF9ZwCDP14sWGvtR6gTCxT_gb76S8JRIN8gnxBzqb-rN8gJS8W0DxReuLxnHDwk1qeP8p23K0ZJ-HYhxRsEHUoAXqnKq-UrCfwZnRSiRPeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|رسانه‌ های معتبر فرانسوی خبر از احتمال مذاکرات‌باشگاه رئال مادرید با ژائو نوس ستاره پرتغالی تیم PSG در روزهای اینده میدهند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22589" target="_blank">📅 10:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFzRkfcnHZcL6Wt1pb4dr-eGQCmuI0gTn8BYov1BPe_Im7gpk2BqtC6IqihYP9aILFufcN90aWLn4S8v9HDBYOhg_Vu4Uhlyql2dPA_LYt856GTyBJYChwhAyOKomwbBUszRZPAwZHTcXajD_gHz7wANratSAFzI2FuxCRw79S52kRBwYLlX0mL2dbQvbeY56LR2XfzUB74cs11Usp9g3WEYz0fAQOYFOE4ETx1Dsa5wdQkCpVeAZJg_PTzCHudk_2DTPubxk3fXeaLXejDCFL34yn82swN5grpFFBAIKrzCZa3VJAAdFmyM74MVY7VDvQFQJC800J5O890-P83s7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی فرعون مصر با هواداران لیورپول با چشمانی اشک‌ بار؛ محمد صلاح فوق ستاره مصری لیورپول بعد از انجام 442 بازی برای این‌تیم بالاخره از جمع لک لک‌ها جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22588" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=sk13KZgc6_X_h7MMinFN_QhAtM_k68cOMybyRdyuIF_PAiRj1tmjjDKlbm2fpRlz-I0xHOwx8zmgUqz2a3vvaVLYTIkp-bGurd2OcxSzVTmkz8BCpa9TwuwblcXJMUotouVD0H4Fo7MbQavvkHGGTb-02oqwUR9UzE_1Bg87MFSvqALVoy00Flt4JqtJtZQR-2Sp9RQLfbKNO0iTGX9aBLUwoEF2ui8YLqRLn6-e-I2wUlNN2c7K29BRDmVly-7-_N6EzUq91drfvl0PanD90V17hVyKcOtgu_ISV1FbnZ-6kgxF2nofF4OiMCyDahylNionk1ddY84RpbFBvriAFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=sk13KZgc6_X_h7MMinFN_QhAtM_k68cOMybyRdyuIF_PAiRj1tmjjDKlbm2fpRlz-I0xHOwx8zmgUqz2a3vvaVLYTIkp-bGurd2OcxSzVTmkz8BCpa9TwuwblcXJMUotouVD0H4Fo7MbQavvkHGGTb-02oqwUR9UzE_1Bg87MFSvqALVoy00Flt4JqtJtZQR-2Sp9RQLfbKNO0iTGX9aBLUwoEF2ui8YLqRLn6-e-I2wUlNN2c7K29BRDmVly-7-_N6EzUq91drfvl0PanD90V17hVyKcOtgu_ISV1FbnZ-6kgxF2nofF4OiMCyDahylNionk1ddY84RpbFBvriAFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به باسن هینکاپیه‌پرداختن؛بن‌وایت میکروفن‌گرفته دست داره اهنگ میخونه هینکااااپیه
🍑
تو نشونمون بده
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22587" target="_blank">📅 09:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEPEpcDslzqs3UEXQA-FyQBb97rYzmtfn566KbVql5HlKLImV40IGZWA6aSg1gD2r_ru-hwr1wp2gDG2vslKm6FiDARvG1wj1S773hFejfqLSG7deiinnO_rS4SzCfb2KC3Im-cgUkqwOX_97-liSyqlghXgUtJLeJul22TsVQ6CWybWUV9pmlYYMKz_F7y8yU32YkymyWr207rMryhy_6D7EHkmODBFM7ccX0O9CK8x6yb4TaR2BtNTEVNWUTuwux6fXbO7Udbmq2ZpDmyHe-3jyGo0dYA5IV0hFjVo2i_j1aKi_a0OSICl6zUphH-9SKzMvw6vC864HF3mf23Slw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛ از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال  بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22585" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=PnVI5nCl8N7AOTKG6W6WPjsdt-NfimtPjAwB9VLnjHkkyVtjMEIfH8hLHMXg_lra_qMfM4i3WQCsowO8B_V1cP673r8Q8kZL4_B1ijZ3twzsmB_e7XpaSeA6FzU0l8ncDQWlZg4w1r10ADUIjb914sEnoP9H4w3zIcftDrCcwx1UtQCbO839UASgTlwdM5ACi9RQF2jV15UmwRD9jpim-exa98aR-qLE15JC5ikS53MBQFXszvsOHlwhYOoYbK0Vt9YQb6WtGWIMr5UhU3ILaIrtVGYHL1xJjGKHRkCCdF5k_dX8jaWkFLf4Y8KNkfVbFf-yfK2lhZxc6ney1-Hj3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=PnVI5nCl8N7AOTKG6W6WPjsdt-NfimtPjAwB9VLnjHkkyVtjMEIfH8hLHMXg_lra_qMfM4i3WQCsowO8B_V1cP673r8Q8kZL4_B1ijZ3twzsmB_e7XpaSeA6FzU0l8ncDQWlZg4w1r10ADUIjb914sEnoP9H4w3zIcftDrCcwx1UtQCbO839UASgTlwdM5ACi9RQF2jV15UmwRD9jpim-exa98aR-qLE15JC5ikS53MBQFXszvsOHlwhYOoYbK0Vt9YQb6WtGWIMr5UhU3ILaIrtVGYHL1xJjGKHRkCCdF5k_dX8jaWkFLf4Y8KNkfVbFf-yfK2lhZxc6ney1-Hj3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌ کنیم از این ویدیو پارسال؛ میکا ریچاردز به‌مارکینیوش‌میگه‌میتونم مدالتو لمس کنم؟ هانری هم میپره وسط و میگه بخاطر اینه تاحالا بدستش نیاورده؛ مارکینیوش هم میگه منم مثل تو بودم
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22584" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVNg6vyJjCA5AvZPmlFWipuL-OPGlcPxONq7vFfzWcoJFeqFXCeYdDn2QzC6852oWajvweYq-gcaXab1Q2WMh55l5tY1HdNiVJHn2UnhofjlmlB9jnXrI22EYEee8kYmUT8YM9_yQMoga05JCSZkQMmW8EQMjTPVrXH7Jg7WeZVoQ21HqmUWM5ALPtVo7K-_LGgti5mxXWAiuhE3XYhnb-YH1T7NsN8YXWlgQtL0x9H7Y7_AcOjgkluxzj3fqUzK2Nms0ULbTfT3qpVFmsXo2mcBhxsQ3AoOPg1ATOhPkiEggelR-ze86nRzUsonPZSONH0OK9n7Vg1BUR6UJnCNeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از جدال یاران هالند برابر سوئد تا تقابل ازبک‌ها با میزبان جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22582" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqjXipfUrz7psqtxSO5tJpOXxo5BiJ6OEcdj5-V1Ah3fdyJvu52GC8_fJusvOUfVHBWeMeHPI5Ynb0MzcZHeM0BIrqQUySZdcbiQ4urFsDNEO7tVLUaVHHNbaxMqyn4LjEDBuGfpiOBjFo9ZJN3eXl-kzuRy46PNXy5HzIPrtiV7UV37zkrJJDnl1G8aCgjg2dNFQicc_H37bIGXj8ZiX5T9euM_Xw9ZWAS5omWzjjrufgCyMzmKWlRzn_6Iot-a2jtNsHV6rn88SNmOAQXonWg6hIJ_53RYfmmRKbk005R6JC99ch63BgDRCHbFyqQ7uz_i6K2zXGhKGuBUq1bbRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛
از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال
بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22581" target="_blank">📅 01:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ki5yrFSx0h42VSdN5Ju5a5wqWIK_YUAEI9PFG1GwMYTn2mqj8BLFQWhS62AKJOn6V5CLCOX30SpPyV9sjoJSVCy24T4wJznQwfuLs2vtNgXW35898tmkooyTpJsy8XQXvfb-DCCH54X027HV06ZEh5vakG0RV1eANtPAkLDa_JM9cz639XXgQwJeM5z0ywOf2JnTTY4iyaWyeQoZnQIN9fkMoAJ01XDu5ESVcMtqPAuTT2sxtpQ8ePg65yqogqIeIFhrO2rfjbTdZF6_ty4ApzLdYc-sshi0LYuBspBbvkZ5y0zK-oXNQs5ScPkI6wAY-0kaitrHEB__MQDkMTdWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mxIm_YiOZ8Rgwc2LQxni3K7yi-wi7qaYAqUuxz20ZjlReAXBqRPYUS5WHCbQOOt1kddZg6rLBHPyQvradjnhZiNWXT-ILJlZyVkfUYHIpTelKXze-K4JK-RNfUSly4ZFh0ib1-hvpzl7yS217CsOchLNjfq77cJlULSS4wYkX0Oc3SVoGGsyXva9hVnFKL_TynRrxICr8Hmf18qqRwOppiYhOii66wvdSJJH-pXlehKCh_pSiBz6xoXAA-lQq2SwBiNkLq3HEmubFQ3vSoqogq4UsPcdH0KkBEoBqUbTzVGRtMiWKDSa-Yp1Y5GP0sNXAkb5nhMX0rbGLNqlo8uwTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مری‌راک مدل اونلی‌فنز قبل بازی فینال لیگ قهرمانان به سافونوف وعده یک «شب پرشور» به ازای هر سیو رو داد. همسر سافونوف که از این موضوع مطلع شده بود گفت: شوهرم اصلاً نمیدونه که «شب پرشور» چیه. برای اون شور و هیجان یعنی حل کردن پازل، تماشای مسابقه تلویزیونی‌وخوابیدن‌راس‌ساعت ۱۱:۳۰ شب چون صبح باید بره‌سرتمرین؛ بخاطر سبک بازی آرتتا، سافونوف در طول ۱۲۰ دقیقه سیوی نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22579" target="_blank">📅 00:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX7llRdzL-dA0lREknisXciI0bTZonBlN7lXMWhuRWPtQjQUc_Dq5os_ZfFhlPOmLL7RTaBbFHjT2oUeNEKfZJLVS9Q6fq5_CQjizDylwo7xvDSc0mxNgLNDjmbCII-BNV2BhUvODOS20FpnTdPLsYRu2cLtD_XFq542kWmGaRQo0ObN8q9a0EK5l0DLm4DT7TGoIlAkvuxFyYgHBjAF7eFr6J3XKqYQuF4F0ODc9HnzwEE_8ZJeKm_epQFLnehofVAIuPkwpSXMhxNqPeAuQOBGlsnVhXmF74jd6yj4QY62bnqtGd3mfAcu7JFFFWDPc8wBCRYTb_84e6QyJRQnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درحالیکه اخیرا رسانه‌ها خبر از مذاکرات باشگاه استقلال با محمدخلیفه گلرآلومینیوم دادند اما اعلام کردیم خلیفه‌ازتراکتور آفر دریافت کرده نه استقلال؛ حالا امشب‌هم علی تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال نیز اعلام کرده که هیییچ گونه صحبتی با او و باشگاه آلومینیوم…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22578" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=kZDrkilnRCBja0erITTzJTJpbBaIJN7cMIb8MvDmj97sOow95vpnZEkTkrDAbxP7kaGFrRrT9hPAQTLZK6ohN5X8nn5M-_HE6jBzIYOWfjj_1W7NBHdPfdBneyL1VDQT1_0g9Qi-x3UPysqWDgauaoTnAdO__S2H7sh6D_sGm1khs-M1_kcCNQ2UcsRsjj0cxSjP-LE-74ijQuoQ3e8tgr_mguBaZlTk_Yozvn3VvMxVFZyUYaRcvJEe1D5Y2yHjvqvSUWriGCjuUn-wYANqWWGWQPeOi6GpUd5KPkbh-wIaEu2qKG5jLVra_RkmrTFVUffrbu954j4xZ_4SyUJY0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=kZDrkilnRCBja0erITTzJTJpbBaIJN7cMIb8MvDmj97sOow95vpnZEkTkrDAbxP7kaGFrRrT9hPAQTLZK6ohN5X8nn5M-_HE6jBzIYOWfjj_1W7NBHdPfdBneyL1VDQT1_0g9Qi-x3UPysqWDgauaoTnAdO__S2H7sh6D_sGm1khs-M1_kcCNQ2UcsRsjj0cxSjP-LE-74ijQuoQ3e8tgr_mguBaZlTk_Yozvn3VvMxVFZyUYaRcvJEe1D5Y2yHjvqvSUWriGCjuUn-wYANqWWGWQPeOi6GpUd5KPkbh-wIaEu2qKG5jLVra_RkmrTFVUffrbu954j4xZ_4SyUJY0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاری سن ژرمن انریکه کاری کرده که دیگه تیم ها برای قرار گرفتن در بین 8 تیم برتر اونقدر تقلا نکنن؛ جالبه که از این 8 تیم 6 تیم رو امسال برده، مقابل سیتی بازی نکرده و فقط مقابل اسپورتینگ باخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22577" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STyUCr0S2jXds1Cpt4TY-9kh6O4lL8IlErndToZmnQW0mlcgG_M_u9CPoGoWXXCUoeKQ-F4ozS5UCC7DQ5_s2PYpcz32LFkRriNgrj3jmUSU0qNJ4nEWk_VWxQEdiVV9jGhsmmhS2K3UuOxKDuGdnoC9zgLj5o-kAw4rAKwGaqRrH_OZvILQQqAbN9CbL0_zMLCNG5ZoFVxekP-W8Lun_66x3R6hRTJfnnOH8KcPrJgWL_3Ub0NmNjJ29uAFTf4TwlU9Rf9Imf0GJzsXFJC4VZxWDW5rfm_rb4rLnGmvcDch1nQtOY8UglFZf-PBv4tK9-xBTU4bomRLvY8lTmTS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22575" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
