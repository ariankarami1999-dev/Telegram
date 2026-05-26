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
<img src="https://cdn1.telesco.pe/file/pReWTzLaUgCh-bxcrgBazGaCix02BMVHbEiU-sqi2dhuFoBwvDnIaUz2_yctSI550SUduN1O__tPRNirrU9vsbJZ6kHIReF94e_fWHOANN9sO73YBn0Dp5hTTk3tb045laon4OsbFM9Z64bhnFWDU5JaN-9OM0SW0TVgjekvYds24GqQ66G3So_5r6rJ7bebYy_lxRwKGdWMsyGnP7ubDZPqD3u2VJiXIG5JXm35t5KbnQ1XDXh9grGQsZyhbsgxejwlywiRvHzBvGyKHoAjtAEiAKmOqxERuNp8V2eRH1AXLyQjvJp_-yL6qJor18oIV9ZgVlqRZJPeeBNpOs0SAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 153K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 03:28:01</div>
<hr>

<div class="tg-post" id="msg-3434">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قول میدم اگر فردا و پس‌فردا اسپوف همچنان وصل بود، یه سری آموزش باحال داشته باشیم ازش. همینطور یه سری آموزش راجب چیز میزای برنامه‌نویسی و ستاپ کردن IDE ها و نصب کردن آفلاین اکستنشن‌های Ai و این قبیل موضوعات چون خیلی آسون با اسپوف میتونم واستون ویدئو ضبط و آپلود کنم و کارم هزار برابر راحتتره</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/MatinSenPaii/3434" target="_blank">📅 03:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3432">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OrPFlA1CGSkFeNLeg5DgJc7Y3Xdjjk3ZdCBP81Pf8MkFsogIUIRNzLcU_RgPiHJbPM4Q4XcBwPnTtvM0BuWjIACejl7X63rf4Z4RvVizvWkCKNpGC7zoNPcOnkSHCTgRqms5uwS0Rr_nYQKSNPCLnTkuNsoTI7ONrOpFQ_S4h2WxzDb5Gc10-O213nqk8pxQ2heGhadfH6caVxNK1lQtyyAhF89KgsVpkWjRawRhTAGMEIM8Nf0mFrnOt5-yg9rYWDU4eI_Xe5rbiuYgn1ja9ijRmWClj4kC29dCEoM4ma6SR26PFnT0au3E2YwIp13YngKl7NWvU3foxFQWAF1I5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/grhUBbewf9lZGV_n7YYkmMbIkbSfj9Y4YrTve3vsBVREmKNFBkBbQZ28l7KFcbAgwHNbRxpejJ0UNtVRvPrMjt9kJiK8ZpUPw5D1doYTyzBLV78lADpP2cISKGYwnfRUgojceXOgx5aShlLFyeSbFmypg7PgZhvL5c_wf6ai7kj7kQgsnayKm24-CKjkWZWvMXIeOHHahA0wjWzssjm2vm-2J_B3rYomOgFahECzUorIzbDQPi3VW__-VT_dnfHX7AcSJaUB8X7q-IkKmP-tD0u9OXS6GC1lw6kkd79a51z_RbuqZXSU_YUs27Mo0huJ2bdT3AlYeeHZSI-PmIVo_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پولی که قراره آمریکا آزاد کنه: 6 میلیارد دلار
ضرر قطع 80 روزه اینترنت طبق گفته خود دولت: 6.4 میلیارد دلار</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/MatinSenPaii/3432" target="_blank">📅 02:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3431">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">صدای تیراندازی سنگینی که در نزدیکی بندرعباس شنیده شد، پس از آن آغاز شد که سپاه پاسداران یک شناور را در دریا هدف قرار داد و در پی آن، جنگنده‌های آمریکایی قایق‌های تندروی نیروی دریایی سپاه را در خلیج [فارس] بمباران کردند.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/MatinSenPaii/3431" target="_blank">📅 02:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3430">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نمی‌خوام دلسردتون کنم اما باز شدن Spoof روی فقط و فقط یک دامنه، به معنی اقدام برای سخت‌گیری "کمتر" نیست لزوما. مسئله اینجاست که فقط و فقط
hcaptcha.com
روی sni باز شده. مابقی سایت‌هایی که وجود داشتن برای ابتدای متود، هیچکدوم باز نشدن و الان ده تاشون رو تست کردم با config.json های مختلفشون.
اگر واقعا شل‌تر شده بودش، روی اونها هم باز میشد. بیشتر اینطور به نظر میرسه که دولت الان بهش نیاز داشته که بازش کرده و هروقت هم بخواد می‌بنده.
هرچند همین متدها، هزینه‌های بسیار گزاف روی دست دولت می‌ذاره. هم برای مجددا فیلتر کردن، هم برای خود فیلتر بودن این سایت‌های ضروری.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/MatinSenPaii/3430" target="_blank">📅 02:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3429">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/3429" target="_blank">📅 02:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3428">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انقدر چیز میز می‌خواستیم دانلود کنیم زمان قطعی، حالا که Spoof وصل شده دیگه یادمون رفته چی می‌خواستیم بگیریم</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/3428" target="_blank">📅 01:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3427">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jDZKqdGBSRFWXU7C4x3NlOImP9bnC5polaoIDEGFVXgXxO4ilCZ7s7HmeIAAN_LMDGCXnTkpDlTyrN_LxWtr-NdyMLOTGb3rOianZ57epPgMtPm8ILQfvgSEB9gzlkZml_LdSRwyxZZk9XUmhUUwnDMWsVuQkgOmGTUJKWuL-LuYb3_865t_Cr3Ufp9Ae91D-JOoa-jKJiQBAZ8-Ojfhl0ZlLzwNJwiifZLzoUZq0CKYb8cgj7rilNx5f_4X3Rmd8ugRZUepo4bYu5u4GKTjoFBYP8IF2TwrdUSejtjLvw0FFD8YuLc1DpuZJlP6T9xz01txZQFFjXKxN5VgT97bnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aleskxyz
:
واسه sni spoofing من یه اپ با go نوشتم که به جای اون template واسه client hello که توی کد اصلی هست، از utls استفاده میکنه که میتونه رفتار مرورگرهای مختلف رو تقلید کنه.
همچنین fragment و ارسال چندباره fake sni رو هم بهش اضافه کردم.
توی تست خودم واسه لینوکس و ویندوز کار میکنه ولی نمیدونم داخل ایران هم جواب میده یا نه.
اگه sni spoofing روی نت شما جواب میده، این رو هم تست کنید، هر دو نسخه‌اش رو. ببینید کار میکنه یا نه
از firefox واسه utls استفاده کنید. خیلیا مشکلشون حل شده:
-utls firefox
توی نسخه جدید (v0.3.0) میتونید کانفیگ رو داخل فایل config.ini بنویسید و بذارید کنار فایل exe رو فایل رو run a admin کنید. نمونه محتوای فایل:
listen =
127.0.0.1:40443
connect =
104.19.229.21:443
fake-sni = hcaptcha[.]com
utls = firefox
قبل از اینکه بخواید از این روش استفاده کنید، لازمه این دو تا شرط برقرار باشه.
اول اینکه لینک زیر برای شما بدون vpn باز بشه. اگر این لینک باز شد مقدار ip رو بخونید و یادداشت کنید:
hcaptcha.com/cdn-cgi/trace
‎
بعد این لینک رو باز کنید و ببینید ip داخل ایران شما چیه:
ipmyp.ir
‎
اگه هر دو این ip ها یکی بود، این روش احتمالا برای شما کار کنه وگرنه قطعا کار نمیکنه.
https://github.com/aleskxyz/SNI-Spoofing-Go</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/3427" target="_blank">📅 22:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3426">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/3426" target="_blank">📅 22:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaFVhU5H8flh_AlkMRCit2hL8t_23Zt6SzJAjXjWCyBoDRPhrHh5ky3USe3-laojJYhJvV8IiDmLZU0sLrWUSbwJnwsCfDU5El_c7604ef0fJ4DigsIdRXzpyVEifOs0meuvC3ouUjoqB70XWPD2dofuKNZKtxDuouFx9TZz7Uxk-OpFEH8RuenKTvd2QSnFUEQa2-mbOirb-kORA9BKDVDt1Lqhuo1ECLU-FEKNB2WLzgoW1nAC1y_72DkWlR2fEwJE0uOmyhg7WBfV9vD74HYVb7kGaORhapnvxYx6znxQpQNcTa8f9xNpTrAxnbJnKQfxu5U9_hbPBRPXOfPrwSiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaFVhU5H8flh_AlkMRCit2hL8t_23Zt6SzJAjXjWCyBoDRPhrHh5ky3USe3-laojJYhJvV8IiDmLZU0sLrWUSbwJnwsCfDU5El_c7604ef0fJ4DigsIdRXzpyVEifOs0meuvC3ouUjoqB70XWPD2dofuKNZKtxDuouFx9TZz7Uxk-OpFEH8RuenKTvd2QSnFUEQa2-mbOirb-kORA9BKDVDt1Lqhuo1ECLU-FEKNB2WLzgoW1nAC1y_72DkWlR2fEwJE0uOmyhg7WBfV9vD74HYVb7kGaORhapnvxYx6znxQpQNcTa8f9xNpTrAxnbJnKQfxu5U9_hbPBRPXOfPrwSiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/3425" target="_blank">📅 20:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3424">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو: https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3424" target="_blank">📅 16:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kgV8pdDw1dPJ_PQFYhguVm_fjAo8WlyOpJ60_7ewQeeIVFgCCvcPZzkzvbTxxejA_kz6dUNmUIkWrCEedfpUzAyRQCMETYfyPna29W2lvK5oXHBQB-Vnn2cQcLjhbKckbVDit4dkcS-WC0W5zCXnmEmzIPe_x48DB7Q4VHSL4c8EE13wNs3ts2YEFCnTLzU0Yfg4jzWZmZLT3DisD7Ki82qV_W1c2Su86ReIIBNBmqc1n-_XyV_3CkM-R9nxttqAmM9b8hkN5n54t7fvnyrGqlGCLxxoYjBdIhtaDqbg2yRhupxP2Bw4R_uX8ard8McF11QIRFUNx9jhAgldl6yXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو میگیرید روی دسکتاپ،
۱- چند بار تست کنید و تلاش کنید برای اتصال
۲- گزینه Parallel test رو با تمامی گزینه‌ها بزنید تا شروع کنه به گشتن
۳- اگر باز هم نشد، یک بار MasterDns رو حذف و مجددا روی سرورتون نصب کنید و با تنظیمات اولیه‌ی خودش تلاش کنید برای اتصال. اینکریپشن و اینها رو تغییر ندید ترجیحا و دقت کنید که دامنه و اتصال و دستورات رو مو به مو مثل ویدئو انجام دادید</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/3423" target="_blank">📅 15:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وقتی می‌بینم یه سایتی که پیداش کرده بودم و توی یه ویدئو معرفی کرده بودم، توی آموزش‌هایی که بقیه می‌سازن هم استفاده میشه حال می‌کنم واقعا.
وقتی می‌بینم یکی یه پروژه‌ی خوب نوشته، خیلی خوشحال می‌شم از share کردنش.
وقتی می‌بینم یکی یه ویدئوی آموزشی خوب ساخته، لذت می‌برم از به اشتراک گذاشتنش
شخصیت من اینه. و حسادت، دورویی، دزدی، بدجنسی و رفتارها و صحبت‌های ناسالم و غیرانسانی توی کامیونیتی اینترنت آزاد جایی نداره
✌️</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/MatinSenPaii/3422" target="_blank">📅 14:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3421">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانفیگ ترکیبی متصل با تمامی نت‌ها
😎
بزنید بترکونید
❤️
آموزش اتصال ترکیبی
👉
ویتورای+سایفون</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/MatinSenPaii/3421" target="_blank">📅 14:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3420">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WD8quxSa79EzG9VxlVymd6J7Qy3vuqXi2Y93MWk_hX-wgvDJuj6hvMHyGbacfvIwHwePA965r8Zxe7lrWZ68kCrEQq2p_rUbGQcQ3ckj2vkfLvkltEjJFwhWw-D4ZTAzeZR9t7g2J8OlyMozHP26Obdco48zXiV98YeuIsGv1YHqk_jL897rVxI6MdXwrR7pB7_ohAbEnm_uxOtAFztBQ8j7X4qFxbmmOJnM43WC4NEZZ56l0rg_HN3odgu7FVs9YWK4Ha-z9uxPd_fccb7tEZVcgaiucSCwPBsJyyyADZx5h0N1kk8Q4R7Vr03LEk1RDDBnv4CfJlCgiMkK-l_ryQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر وصل نشد، این خبر رو هفته‌ی بعد دوباره بخونید</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3420" target="_blank">📅 13:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3419">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">برای کدنویسی با هوش مصنوعی، به شخصه دیگه Antigravity گوگل رو توصیه نمی‌کنم به خاطر rate limit بسیار پایینش که با چند مرحله تا یک هفته شما رو محدود می‌کنه. حتی برای اشتراک Pro هم صادقه این قضیه. پیشنهادم اینه که اولا اگر در توانتون نیست هزینه بدید، دوتا کار…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3419" target="_blank">📅 11:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3418">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برای کدنویسی با هوش مصنوعی، به شخصه دیگه Antigravity گوگل رو توصیه نمی‌کنم به خاطر rate limit بسیار پایینش که با چند مرحله تا یک هفته شما رو محدود می‌کنه. حتی برای اشتراک Pro هم صادقه این قضیه.
پیشنهادم اینه که اولا اگر در توانتون نیست هزینه بدید، دوتا کار کنید. ۱- از Codex استفاده کنید که کمپانی Open AI توسعه‌اش داده و از مدل GPT 5.3 High برای دیرتر پر شدن rate limit استفاده کنید. مثل آنتی گرویتی هم دردسر تحریم و... نداره. فقط یه vpn می‌خواید که Chatgpt رو باز کنه عملا. اپلیکیشن هم داده برای ویندوز اما به عنوان Extension VsCode هم می‌تونید نصبش کنید. و محدودیتش هم سخاوتمندانه هستش و به صورت هفتگی هم صفر میشه. کما اینکه میتونید از ایمیل‌های متفاوت استفاده کنید و یه گفتگوی یکسان رو باهاش ادامه بدید!
۲- وسط کارهاتون هم می‌تونید از خود Ai Studio و مدل Gemini Pro به همراه گزینه‌های Google search و Url context با thinking budget بالا استفاده کنید.
اگر هم می‌تونید هزینه بدید، پلن‌های پولی Claude code و یا Cursor رو تهیه کنید. به مدل‌های چینی Kimi هم نگاهی داشته باشید.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3418" target="_blank">📅 10:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3417">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">متاسفانه دید همه به dns، کلا dnstt و ساعتها اسکن بی‌نتیجه و دنبال ریزالور تمیز گشتن و سرعت دو سه کیلوبایتیه. نمیدونن که من با همین WhiteDNS به راحتی میرم اینستاگرام و یوتوب و تیک‌تاک و...
چیزی که بهش دقت کردم، روی اینترنت‌های متفاوت نتیجه ممکنه زمین تا آسمون فرق کنه. در حدی که یکیش تلگرام به زور لود بشه، یکیش بشه به راحتی مثل قبل از دی‌ماه رفت اینستاگرام</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/3417" target="_blank">📅 07:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3416">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NUb5DnngsvoyUetv7J7JnDTHeiSilJjIARnimIFGdKBMUFeQ2YXfykvqDdFYDO3qE2ABhfM_DD2DNQkA3SxGCB7e0Al6qojbZ_XEmFyqBY7hN8prHMsYI5WjkrCAWv8Pd3hFIy5uhLcx5levskNgGMfJlSS7AgrKLhocSf_4Lqk9Uxi5jAeQRIWFpwxEOphUAPMExfum8O7YyqPlxqas_lvTleGmR5Ge7SXuvA-o_PMUfZb7xVA8UAQnVz7c6SSAl-LXnUVV_jpFl3hzVbLoFdvBGhODkgBeyME3lL5PF-eZbeboJ0VHU4h1JZGOvqewUQ0wG86T1aMriWgmU5zj-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر خارج از کشور هستید، برای خانوادتون نمی‌تونید V2ray کانفیگ کنید و بفرستید چون ارتباط از داخل به خارج و خارج به داخل قطعه. اما به راحتی می‌تونید واسشون روی سرور مستر دی ان اس نصب کنید و همه‌شون رو با WhiteDNS وصل کنید. که برای شرایط ابتدای جنگ تا به الان…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3416" target="_blank">📅 06:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3415">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jsM-KsI86uxb16lnyHXt-yh8U42TbT5-2MIgc4NZfKzEI6pesg4IQ4Px5j8F5jLl7Kfh_7t6MmVjjl02rNY4RyplUV9rIjQE99TL5gnsuw_OgG5UI5rc_qf21HmjBIryWSNWmbkw-gP99nSiSqryC7EG8RoOe7iqG9vKQ2o1IvhIu88_74uCwgEVl8MvZFckNomFZLTjvRrgvFOzmfyfqYH7y_2Bh4vupO-m64RL69k484OBdAuJHa7nRt96-raa-iVhSrfX7cHi1N9hd5m6SfUuQ75luYFPxULcT_zddi8sDyijnIS3pNXtKqA_mDK6mFAhoUk1TFZmFfJwear5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر خارج از کشور هستید، برای خانوادتون نمی‌تونید V2ray کانفیگ کنید و بفرستید چون ارتباط از داخل به خارج و خارج به داخل قطعه.
اما به راحتی می‌تونید واسشون روی سرور مستر دی ان اس نصب کنید و همه‌شون رو با WhiteDNS وصل کنید. که برای شرایط ابتدای جنگ تا به الان کاملا پاسخگو بوده. اینم آموزشش:
https://t.me/MatinSenPaii/3372</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3415" target="_blank">📅 04:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3414">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zv6PCnXQeb5rju7RE6OnJYycylDJXQTopNVF339BT3bsQR-FSnbtiPSX8PrnnAmRI0uE3LIgchNsMai_WK-9ssiEeHRV13zmc1md132eUs31AvYlz0wbix4NrvVFZ2bmB4CpJHA_iD3IP3wcKgBpufDAYEaon_oB-EauHA1Nu0uQHS_CmOcyPg1ORklmNRMdXcYOFW41CuiwbD3m9vsbj7Ibp4It26hxnYI5tpZs1t-UAeQxsUA4HJhsABGrl2nNosNULyZvr2ZJjkf_BwTRhjA2rOOwdfgqfmAJ_-s_C-E0lVV3osXt0dXok54PksdwbMOtHfGMBfxYv8kwLx5g-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنان SNI وصل هستش
گزارشاتی دادن بچه‌ها که براشون کانفیگا پینک میده و کار نمی‌کنه، که خب باید بگم اختلال از سمت اپراتوره. یعنی شما دو بار پشت هم پینگ بگیری، بار اول پینگ میده بار دوم پینگ نمیده‌. در این حد هستش روی بعضی اینترنت‌ها
اما خلاصه تا وصل هست، استفاده کنید</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/3414" target="_blank">📅 03:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3413">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bmtbgt5QJFcZu79KsobnV_-QsgFRYRXUpCVMmGpmmkmZMVCbUfsF6um8jWTHoVkKDdzfD-nS2Q1HDebmU9C0MhN_ln11hpYgmIn3gug5onYL14isMOcdrD1ksOY32hKDa85giKwF6nD_rP6NW-b0xzA3e74y-c6v3tVbK--E2aDJcmWc-B0CDzmIzYqR06qZ15g9-D6gB0tbS83QfMQiLOH5TMXxIKSLs-XB31nXSCEn61h2Grfn_8iQ6XWXh3pfCwOW8NxDU0MshgI-3Y3_BTazCFcqvCJqXAQEgEdPGI2Tv-DjB2J4jF_8oCdDD5vPNETSmqGY-101YVfNQhjuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی آدما انقدر خودخواه و بی‌شعورن که انتظار دارن کل کار و زندگیت رو ول کنی، و تک تک ۱۵۰۰ تا پیامی که روزانه می‌گیری رو بشینی جواب بدی.</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/MatinSenPaii/3413" target="_blank">📅 03:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3412">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3412" target="_blank">📅 21:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">برای SNI SPOOFING روی Mac می‌تونید از پروژه‌ی خوب Cloak استفاده کنید:
https://github.com/g3ntrix/Cloak</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/MatinSenPaii/3411" target="_blank">📅 20:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گویا پولی که از صرافی‌های ایرانی میاد رو بلوکه می‌کنه کلا. حتی از Trust wallet هم ممکنه این بلا سرش بیاد. ترجیحا از این سایت نگیرید اصلا</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3410" target="_blank">📅 20:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/MatinSenPaii/3409" target="_blank">📅 19:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3407">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3407" target="_blank">📅 19:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3406">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">زبان‌های مختلف برنامه‌نویسی، هر کدوم قاعده و قانون خودشون رو دارن و به درد یه جایی می‌خورن، اما یکی از پارامترهایی که می‌تونیم اونها رو بر اساسش مقایسه کنیم، «کامپایلری» بودن یا «مُفَسِّری» بودن(از تفسیر میاد) اون زبان هستش.
۱- زبان کامپایلری (Compiled) چیه؟
توی این زبان‌ها، قبل از اینکه برنامه اجرا بشه، کل کد به زبان ماشین(کد باینری) تبدیل می‌شه. این کار توسط کامپایلر انجام می‌شه. این که ماهیت کامپایلر چی هستش، بماند.
مزایا:
۱- سرعت اجرای خیلی بالا
۲- اکثر خطاها قبل از اجرای خود نرم‌افزار پیدا می‌شن (Compile-time error)
۳- پرفرمنس بهتر
﻿
معایب:
- باینری تولید شده معمولاً فقط روی یه سیستم‌عامل و معماری خاص (مثلاً Windows x64) اجرا می‌شه. و برای پشتیبانی از پلتفرم‌های مختلف باید کراس‌کامپایل کنیم که پیچیده هست و دردسرهای خودش رو داره.
۲- تغییر کد و تست دوباره سخته (باید دوباره کامپایل بشه)
مثال‌های معروف:
زبان C --> سیستم‌عامل، بازی‌سازی
زبان C++ --> بازی‌سازی (با انجین Unreal Engine)، نرم‌افزارهای سنگین
زبان Rust --> سیستم‌های امن(به خاطر مموری سیفتی) و سریع (در حال رشد و توی هایپ شدید)
زبان Go(گولَنگ) --> بک‌اندهای Scalable(مقیاس‌پذیر)، میکروسرویس‌ها
زبان Swift --> اپلیکیشن‌های مک و iOS
۲. زبان مفسری (Interpreted) چیه؟
کد خط به خط، موقع اجرا ترجمه و اجرا می‌شه. نیازی به کامپایل قبلی نداره.
مزایا:
۱- توسعه‌ی نسبتاً سریع‌تر (تغییر رو میدی، فوری اجرا می‌کنی)
۲- یه سری به عنوان مزایا می‌گن خوندن کد راحت‌تره که من قبول ندارم اصلا
۳- در کل Portablity بهتری دارن. هرچند شما عموما مجبوری سورس کد رو کامل تحویل بدی چون نرم‌افزارت همونه!
معایب:
۱- سرعت اجرای پایین‌تر (چون هر بار باید ترجمه بشه)
۲- مصرف منابع بیشتر
۳- خطاهای سینتکس و DataType، معمولاً زمان اجرا (Runtime) تشخیص داده می‌شن، در حالی که توی زبان‌های کامپایلری، خیلی از این خطاها زمان کامپایل گرفته می‌شن. این موضوع برای پروژه‌هایی که با این زبان‌ها نوشته شدن، باعث می‌شه دیباگینگ پیچیده‌تر بشه.
مثال‌های معروف:
زبان Python --> هوش مصنوعی، مهندسی داده، اسکریپت‌نویسی(ابزارهای قدرتمندی داره)، وب (Django/FastAPI)
زبان JavaScript --> فرانت‌اند وب (بک‌اند با Node.js و فرانت)
زبان Ruby --> وب (Ruby on Rails)
زبان PHP --> وب (WordPress و لاراول)
(هرچند جاوااسکریپت و php رو دیگه نمیشه کاملا مفسری دونست. به خاطر JIT Compilation که بعدا توضیح می‌دم)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/MatinSenPaii/3406" target="_blank">📅 19:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3405">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4659a46672.webm?token=byIPUkqQhTcmMZDv7GFTh6GsFUx8lK2CgXJvlGqL-uAMTus0eMjoqqsx-w98BCzF7LbLPPi4uMSGsrBziP3UsYeYUzGaHSuBDho9qrcDi33MsqBviAQoAsdCDTP_6uDq9XiQ14L3uwIip3AL3icTg9MVF7JPeeGuOJAF9ty-YFg9sUJYS1DG68L7djhKLgl3_4Ia7r5-SprVnQD0GaFC7qhIzeRI9THPfYgC883vOjaDilgMvdtBLJtrKSp6FD7nM3Do9JdASl5USnJA5nd3e2R6Sfpvi9CGwN4bp5eoLMVr87yRsX2BpvyE8xl_J4tPlArEcuhXWU2c5KDTTmcRdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4659a46672.webm?token=byIPUkqQhTcmMZDv7GFTh6GsFUx8lK2CgXJvlGqL-uAMTus0eMjoqqsx-w98BCzF7LbLPPi4uMSGsrBziP3UsYeYUzGaHSuBDho9qrcDi33MsqBviAQoAsdCDTP_6uDq9XiQ14L3uwIip3AL3icTg9MVF7JPeeGuOJAF9ty-YFg9sUJYS1DG68L7djhKLgl3_4Ia7r5-SprVnQD0GaFC7qhIzeRI9THPfYgC883vOjaDilgMvdtBLJtrKSp6FD7nM3Do9JdASl5USnJA5nd3e2R6Sfpvi9CGwN4bp5eoLMVr87yRsX2BpvyE8xl_J4tPlArEcuhXWU2c5KDTTmcRdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3405" target="_blank">📅 15:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3404">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:
1- آموزش پایه:
https://t.me/MatinSenPaii/2627
2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید:
https://t.me/MatinSenPaii/3168
3- و کانفیگ‌های این پست:
https://t.me/MatinSenPaii/3183
ترجیحا با ایرانسل یا سامانتل
4- سؤالات متداول راجب این متود:
https://t.me/MatinSenPaii/3189
و تبریک میگم! شما به اینترنت آزاد دسترسی دارید.</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3404" target="_blank">📅 14:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3403">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اسپوف روی یه سری از اپراتورها برگشت. هرچند با وضعیت دیروز، و گزارش یک سری از دوستان توییتر، اختلال شدیدی انداختن و در تلاشن برای یه سری CDNها بدون اینکه مردم بتونن تانل بزنن، دسترسی خارج باز کنن. که احتمالا سر همینه این وضعیت:
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
hcaptcha.com
"
}
﻿</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/MatinSenPaii/3403" target="_blank">📅 14:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">توی دایرکت چنل یکی داره میگه شیر و خورشید جدیده زیر پنج ثانیه وصل میشه، یکی میگه دو ساعت هم شده و وصل نشده.
به نظرم باید بذارید حالت هواپیما و با rangeهای متفاوت تست کنید. انقدر زیاد منتظر موندن هم دیگه فایده‌ای نداره.</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3402" target="_blank">📅 14:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3400">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیم ساعت تا یک ساعت شنیدم بچه‌ها گذاشتن تا وصل شده.
اما طبق گفته‌ی برنامه‌نویس پروژه، خوبیش اینه که بعد از اون دیگه نیازی نیست انقدر منتظر بمونید و به همون آیپی تمیزی که برای شما پیدا کرده وصل میشه
خلاصه که اگر گوشی بیکار دارید، بذاریدش سر کار</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3400" target="_blank">📅 12:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3399">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.24.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3399" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/MatinSenPaii/3399" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3395">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qg6SIJp1bIePMYdjOp8HeK-_spn0VfL7HaZhIltAU0KAUm9m_D19DhV2GhNGYkeyvqvu2gVeLWshTA9HP_sdvBVktvIcgIC3WfCnOfv6Go5C15VC2Qk5H0Vqwd5BiVyYR1Bb4yruc95Qncj6X34cqABwDlx3W6hcod9VYyYXr7mgCHHMb2CZff69psfyuoA94VHLnlnilUwuX6DesCIQnUKUpDoBF-gxlvWYBadn22p7SPxP2ZEjDBoaw9TjYZeSOD9DEoMGiwkhr-CarUqetiXJDCPN70T5KlKCeEo9uUd4CQVZgxiVjys4B8Z_sSvvsjbOgZmXX_NIyVQX-YxZQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h4Pf7fYiRlDBrvLy0aTJL80aalhCZeSLuFsTUxZ5Vp91VhRyAb2qDzoakqTTmYqvMIGWqTRXJfaJ5MEjfFMclxjMUmJYpU0eQ4edjXQ22BKZ-gmFV2Dv0VXTYy4UN1BtJOt_VRW9KV_UwAi_DGKAMtyPUqjPNCM5LbiL6yzTwRR67KDB2GSlkiugXEUSP8_YEGgvJrShPZlvaS3jp7OBx_HXrQUc5srWXFFxldhTXMN4LAEc_MYxyyINZ1aS9m-WFbuHZyT-bi9eWB5kRjfny9VJblx7_3gFmi8lMKOetg3q74Kd5olV7EiWi84LkftZ0hVKJMAbhXSrEtr44hX3tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XNMmgzDTIY83hkHBU2UOmftym0kbzMT9vrpevfUhp9eG3Fm1sgJ9s2hiRLM9UojdGkIyo_U08oi3XhbHZfGumeruMDQAwXMlMPU1vGB7gC2otseQaW_CzrOq7_aSL_oYZR7NmBLoMPCFsRaasoFLIU-YsrRAYRafF_s_3d3yL-syQ0uxn7dPMYkrNXE3LY7Ds9SkpQFdBTfRdMPTboLysFLZlQXeGr-mjv-GcUFLZq1ZbSFr0OiNWhKNsObYvhZdF-w5hNEXhQFcx2WeRZp4hypN1ssYHLf5lpD8GcNFtda7aLLJpPvlGajYo2_vcUho_IE_LZxS3dXz0tMrOdzm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/loSyT4mhB1EV_U-NoA6XcQpfXTvOJMQu-dtt_tQTKVZ3o7etjdrcfb2hycWNED6Z8zwp5kEWEAdHQbMWOka6cui11YfckRZ3J0lmrqQoINqAFgI-N9p4HaRDcB3pE-BjTB4GcnQTUY40tQvK_1K1b7wOpsvAW8-usOUR1HwltawXBsV73UI4uH86ahPUBEdjB4543Jq7YWW6W2oH_lMXLY1AEbR4KZalRQ_mIFBAPFJdE56ZsfWc1K9-CeYrEvJN4pTeRVS1Q8CbZ2SBsMFC7X3604R69LPyL4-pny7j1ZtnNzz2OLtmEhuWQj0z5xPI_AQ1efvum2GqQDFatwX6-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید کلاینت شیر و خورشید 2026.05.24:
- آپدیت Beast Mode برای درست کار کردن روی CDN Fronting
- اضافه شدن اسکنر ای‌پی. برنامه لیست خیلی بزرگی از ای‌پی های ممکن را داره٬ پس اگر در اتصال مشکلی دارید پیشنهاد میکنم تنظیمات قدیمی ای‌پی ها و SNI رو از قسمت settings برنامه حذف کنید (خالی باشه)‌ و اجازه بدید برنامه خودش کار رو انجام بده. دقت کنید ممکن هست بار اول خیلی طول بکشه٬ حتی چند ساعت!
- اضافه شدن پروتکل های بیشتری که با CDN Fronting کار میکنند. احتمال اتصالتون و سرعت باید یکمی بهتر باشه الان
- قابلیت غیر فعال کردن سایتی که زمان اتصال٬ سایفون باز میکنه!
- قابلیت تنظیم پورت مورد نظر خودتون برای LAN Proxy ها.
- قابلیت تنظیم username و password مورد نظر خودتون برای LAN Proxy ها. این تنظیم دلخواه است و اگر تنظیم کنید فقط با این username و password در شبکه خانگی میتونن به شما وصل بشوند.
- آپدیت شدن هسته سایفون
میتونید از اینجا دانلود و نصب کنید و ممنون میشم اگه به اشتراک بگذارید که تعداد بیشتری ببینند:
https://github.com/shirokhorshid/shirokhorshid-android/releases/tag/v2026.05.24-a3b91cf</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3395" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3392">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNSJuISAFjefXDh8Fo0FM7uwWlkjYTLDtZOdDgitiuE4lQadodOarWzyCTYBOIB0cD8HwvYOLDmgt1DSy-Skgrb8HFQWuYrgrm1445HLFmBxRsHzUePxj_fjPVl5tM7t4iURZT4MXLtnfh-5TFGD0ZyaLXono6Zi0Gsmq7aP8QcZqsUUwwnxj8rRpgHuGpbt9d-NVtibXxni4cYV7wYdLaqhvcRctxBXaLNSqpMuZdnHST0QnligVaCm2evRkSXqBRBCN2IqE5Ob8i8CdjFmITGI9SzFuj87u6NyqFT6aqln0hRO6jAKH30a7ACosGGkktQyXEMyMAXmvHGQFn1UZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3392" target="_blank">📅 09:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3391">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه همراهان عزیز
ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.
تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.
من پیشنهاد میکنم برای راحتی کار شما، بعد از خرید دامنه و اتصال DNS از ربات
@WhiteDNS_installer_bot
استفاده کنید.
اگر از این‌ ربات استفاده کنید، فقط با پروکسی کردن تلگرام‌ میتونید سرور خودتون رو مدیریت کنید و در شرایط بحرانی فقط از طریق تلگرام همه چیز رو مدیریت بکنید.
ممنون
@WhiteDNS</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3391" target="_blank">📅 09:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3390">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اما تا ۵۰-۶۰ گیگ روزانه نباید موردی داشته باشه. سرور رایگان هم خواستید از سرورهای کانال مسیر سفید می‌تونید استفاده کنید ولی خب تفاوت سرعت رو توضیح دادم توی ویدئو که به چه شکلی هستش:
https://t.me/Masir_Sefid</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/3390" target="_blank">📅 08:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jN4aHKhdi_lRFHqtNz1qOD_tr1bW7o48bc-L3kjtJ1HagbDmMtVD15tqekIDdrGHCQjl69sqy4tLZN4WEfHrlDl_F_bKBY1Kp9XZLMdZH_TttlG6ftrpDWIiCjdjvvNQ9oSTopbD2qvhKA7wodxRTTumJaOX4tJel-SehosphT64RXAr-jyhaapakGzqEh7EC9ZycWpSmrLyRA2jxOF8J_e97S-4y6CNlQRw2hwhIF87vpDCelshlvXdKZyF4suyZOOig-VuwRadj5ntLLvIdRGT0hRxYpxbDly2ruyb4-psl5DSNZeVY1C74BU1NIOdwVV2DCPvKmiHZqubWBqfMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ حجم دقیقی وجود نداره عزیزان. اما از چند ده گیگ متفاوته تا ترابایت حتی
گاهی اوقات فیلتر شدنه کاملا شانسیه متاسفانه</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3389" target="_blank">📅 08:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3387">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ProxifierSetup.exe</div>
  <div class="tg-doc-extra">5.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3387" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این هم پروکسیفایر و یه لیست از Activision Key های مادام‌العمرش (برای مک و ویندوز)</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/MatinSenPaii/3387" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3382">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3382" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه Universal اندروید لینک داخلی:
https://up.theazizi.ir/download.php?t=e8a7a62516394e4aecbd26ca36dbb113e0aa</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3382" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3374">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه ویندوز X64 لینک داخلی:
https://up.theazizi.ir/download.php?t=4b31fefbad0c08f180216f8e4c1eecc316d7
نسخه لینوکس amd64 Debian لینک داخلی:
https://up.theazizi.ir/download.php?t=bb6cfd1d86d4ed7a1826a4850b901ed46c58
نسخه مک amd64 لینک داخلی:
https://up.theazizi.ir/download.php?t=acbf869993172d51c2286fc812931ef48fd4</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3374" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3373">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Master-White-DNS-@MatinSenPaii.zip</div>
  <div class="tg-doc-extra">25.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3373" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حاوی فایل دستورات سرور
فایل لینک تمامی سایت‌ها
فایل 5800 ریزالور جمع‌آوری شده توسط بنده از سرتاسر تلگرام
لینک داخلی:
https://up.theazizi.ir/download.php?t=b9162802b5da63cf5b39b02133170f4ad2bf</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/3373" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3372">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو:
https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو:
https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- خرید دامنه و سرور ارزان با کریپتو(+آموزش)
2- تانل کردن ترمینال با Proxifier و ssh زدن با خود ترمینال
3- تنظیم دامنه در کلودفلر و راه‌اندازی ساده‌ی سرور MasterDNS
4- استفاده از سرور MasterDNS در کلاینت های ویندوز و اندروید WhiteDNS
5- توضیح استفاده از Parallel Testing در WhiteDNS
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به خریداری یک عدد سرور لینوکسی و دامنه داره(مجموعا 5 دلار نزدیک به 800 هزار تومان) کافی برای اتصال نزدیک به 5 نفر
کانال مستر دی ان اس:
1-
https://t.me/masterdnsvpn
گروهشون:
2-
https://t.me/MasterDnsVPNGroup
کانال وایت دی ان اس:
1-
https://t.me/whitedns
گروهشون:
2-
https://t.me/whitedns_group
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/MatinSenPaii/3372" target="_blank">📅 03:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3352">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r29XjmaxcULYubuB3p54TZpRCnygpq23gi2i1jVbEwGo-7An66DvCLVHRbuVPqhYF8wlYiHlYL6XkHrcCN-4ZPIXJuHZqBtmOS8xL8s7_dUstihnpSYykGpOJddgxCqbCkjCv8tPztIV-_izhWneaYrUgapSJIQD8T0CtAMy19JBkOIhWQgol5pkD3ouiJ3urNPcdHqRpYSj7_V7aW7iUags29S2tUoGUbGzzRi8Y6obrPkMm2SWrXJMElQ6KglloyGJcwPxOI0ZBKUduR48S6JFoITWYSucDSdHX3lyubG5yC7YtjxprHwl03v_seuOb5eQdFTiuoKmSutD5hHzxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرام وقتی
یه پروژه جدید
میزنه و مردم میریزن سرش هی سؤال میپرسن ازش:</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/MatinSenPaii/3352" target="_blank">📅 22:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3351">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آموزش بعد از یک ساعت و نیم تایم نفس‌گیر تموم شد ضبطش(خودش شاید اخرش نیم ساعت بشه اما مشکلات فنی‌ای پیش اومد اواسطش که متأسفانه باعث شد طول بکشه اما در عوض خیلی کامل و جامع شد)
نیم ساعت دیگه میرم برای ادیت، تا ۲-۳ صبح ایشالا حاضر میشه
با تشکر از همه‌ی بچه‌های گل تیم وایت دی‌ان‌اس و مستر دی‌ان‌اس</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/3351" target="_blank">📅 22:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3350">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">Matin SenPai
pinned «
ببینید همراه اول میتونید وصل بشید؟  {   "LISTEN_HOST": "127.0.0.1",   "LISTEN_PORT": 40443,   "CONNECT_IP": "85.9.112.219",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com" }
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3350" target="_blank">📅 19:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3349">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U2rMszaDzAA3CXH_m5YpLvTVVxYevUi6-db95xSw_KqYz7qRLSEjtZXC9q5rJYBGG5pWkvl2DoRhV2lZGePV_Sc5NZ9q_wpK5T1gJxnJAU_6mFJDoAHZddSuT4WJXwN8IWnHK73yA1qdAs_-ZYoYt67jCJcl5XZ1n3DoYcC_eY3LFGFH1-ktETOm7eriHXB2K05q90mlKbyY8jxbHtfCEyan5osQfpgNhdrhenk-RRThT9WZBLXXQb0BHTKojbz44XjC_AqgI5z--MZG030X5TWleZLDrjBJ0YWkaFC0YOWHZL35-7dTBEKytvANwWSWf68bmAlZkKZhLY4r7Hg6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متد مستر دی‌ان‌اس که توی WhiteDNS ازش استفاده می‌کنیم، مبتنی بر DNS و برای شرایطی که گوگل هم قطع هستش. لطفا انتظارتون رو ازش بالا نبرید در حد دانلود و پینگ پایین و...
بهش به چشم برادر ارتقا یافته‌ی dnstt نگاه کنید. که نیازی نیست در به در دنبال تک تک ریزالور بگردید واسش.
و یک متد اضطراری هستش هرچی نباشه. شاید بهترین کارت و برگ برنده‌ی اضطراری ما باشه، اما همچنان اضطراریه.
برای شرایط الآن، شاید Goose یا Skirk یا Mhr برای شما بهتر جواب بده. به این دقت کنید لطفا. Dns برای خاموشیِ مطلقه.
پینگ و سرعتش نوسان داره، اما مقابل خاموشی‌ای که هفته‌ی اول جنگ تجربه کردیم؟
بهشته عملا.</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/MatinSenPaii/3349" target="_blank">📅 18:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3347">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h3vgBgYmpCGTdKelhCTrCwLyBaYElOc-RAuWVRMqOAgz8p_qTF5CocNPztSh6FeMBSaCoqQ94eYcU8BPuUnEP6pfsG-8ft028oaLdgG_GCqNI1AruX4_UkFblueUYOwO2mQR6vmkWIRwML-8sstqxf3KsxWPlXFbAid6Nd8yWievVKydx67ZrEDyOOj9RPrMqxQuwNjyhNexBNvufBReBmK6JIw1J39vmddCiB0hSfA-CFgFhmuaFNg_uA3k-zWbgOUqvUmBBeX8ICpcFWd3TvzB1if1Wewwy56YPU1N1NGo3KOOLxfwpPH7QcPQ9ziVTagqQw271zXD4f22esu0IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lRtLBNPqhsdJj9W1IHIbQiEQa-OnvqZXd9eDnpQ484oKEdaldKErBU9rpRYNIbhVxCDLPAS99U9MTQ3s4ejKkcko8snXq78d8_99IK70X4vSSoaJWBT9py6eYdnhUqSZD5l0uF0F1CyOlJe0OrEbTeCvfqfmMopY8Fx7YkuW2TfTdSWMRzI9GinqGPaec6qxbrCFD_IsbBY9rSmwg6bH4fHoaGk5mT_OTl3KdlotMkwJf_p72TC7UG7-Jeba5Pq6gsK855CggCBczh0vgPK23_14h9eF6BmU3Vxo2W3PgHz15lhgatzbEOb-Ku9-QHJ9-xGBc4crtcv9U2z1tAQtEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حدودا ۳۰ به ۷۰ انگار وصله توی یه سری مناطق
هم همراه اول شنیدم هم ایرانسل</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/MatinSenPaii/3347" target="_blank">📅 18:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3346">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3346" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/MatinSenPaii/3346" target="_blank">📅 18:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3345">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ببینید همراه اول میتونید وصل بشید؟
{
"LISTEN_HOST": "
127.0.0.1
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
85.9.112.219
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
www.hcaptcha.com
"
}</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3345" target="_blank">📅 18:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3343">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/viimghStQl4-mxYUqYt6RddrIi5S7_VKnJa-2bCpo47THxNlpfRy5d2i6H_hsYEqcvVYdU-E7qKCckVVwoFXYBM_7tkSIFT91j_3ZTrTMvEvYySSXuZuzayPJgsZROYDEpR0ncSqdJQb84a3bjMqmzeFjoSTSXlh8Da8s3tfvCihkhbhK5ycY-UcK6ys7pP8nuHwGgijFa3-X2M3c8l-mK8gbdc3pneKV2WvXHtTkA99R0ebRzwpZ_X9vpQIRwYUjOX_GQvbyXMUpam8xAt0dc48uoG5pPTZNcm9W8_dYAnjDEImrfePGgTfg5Lq5Ro8APBoEyDMBRwy0n1QolArjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت خوب برای خرید سرور با رمز ارز بهتون معرفی میکنم که قیمتش حدودا فکر کنم 4 دلار بیفته با کارمزد و اینها، و میگم که چه شکلی با صرافی‌ها کار کنید و از طریق چه ارزی بخرید.
منتها نکته‌ی مهم اینه که تصور شما اشتباهه از بسته بودن دیجیتال اوشن.
دوست من الان همه چیز بسته‌ست. همه چیز
و اگر چیزی باز بود که دیگه از DNS استفاده نمیکردیم.
پس بله، شما اگر VPS بیکار داشته باشید، میتونید این رو ستاپ کنید. دوستان خارج از کشور هم میتونن واستون ستاپ کنن طبق آموزش اگر که حوصله کنن. هرچند برای تعداد بالای 255 تا، قوی‌ترین سرور هم جوابگو نیست که خب این رو هم مجددا توضیح میدم که چه کار کنید. فلگ شدن دامنه هم توسط کلودفلر و هم توسط DPI ایران رو هم همینطور</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3343" target="_blank">📅 16:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3342">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NNiCivVRY-PzFC30xo6fBtEVAaeiK-84A0cc7XIaQ2e1CvAKY0gikebAy3pCo2H88NVo7vHUlq0ZastafqsMgvTlRir06KXlo8SxCsik8Tv-w3vuNxGCXhffCi173iSorVp654hvify2Xj7UrFVNO3RHjAslFtYIT2QdFBLiOPZcGkACOynol4AtiJmse2C8UpiFRrMGAPX7dtt74-_26qlU5BYPxa26UvLgfmanoP8cVVrrJneEGeqwlBmWQa7cosSAIMS6H8HDpb5WtRJmGnUUKFGZ5C_rODlse9X3Aa56w2QHIwjw2gBo3CYeuuJkgVzV6wRmCEUGd-Dj9FwMGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصلا آموزش "برای" سرور شخصی هستش. و برای ios هم تنظیمات به همین شکله چیز متفاوتی نداره. خودم آیفونی ندارم که بشه روش یاد داد متاسفانه اما طبق آموزش پیش برید، همین مسیره</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/MatinSenPaii/3342" target="_blank">📅 16:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3341">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u4hadt6ZGd0jEvG2lUC35hjU4-hwFiJOd2g53AYajyzHXbJ0emwVLiF03k4Ag5V79xoUhgUOwaAPLXEmU-hg-TDbI6WJtkibCIjsigCXGofI5P0lmiBvxJVo09oR6UXqV2RqJXYvUXMeu9zkdO9tPpu2JolvJ45Dy_hfohpPihD_i_y_jxIfFswswe6zMOeiLuo5JFswvQd53knjxMWSOPFdJS2q2CU5Gc5sT0-Ha1tGcTVTeAag2twJsXJ5-sP1havSv6Jvz1SAJ7Ulj9b_PJvRHxSbYgJdRh9UveWMGEtRjHzEVdwbVMhH2q-Bi1DgQi5NwqwRvTFrMYD3Mcm7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ترفند جذب مخاطب نیست واقعا:)) بلکه هیجان خودم از متدیه که به شدت خفنه و میتونه ما رو نجات بده توی شرایط خاموشی مطلق
خیلیا پرسیدن که چطوری داری این سرعت رو میگیری؟ مگه میشه اصلا؟
بله میشه و توی ویدئویی  که تا شب می‌ذارمش 2-3 تا علتی که باعث میشده شما سرعت خوبی نگیرید و کندی تجربه کنید رو بهتون میگم</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3341" target="_blank">📅 16:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3340">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ebddd60447.mp4?token=mCQG-D3QalukdA_pYuj9JUX5vzbS7FEMFfiJrIBvgCenRgForq3eE7UDN3uKCkfej-0Idn0qBRjj4b4fL6tabISaP9HJrGWefNbaRPXOyLjb5uU-1P-QKRLB0fHXEoM1S1YE-vS6cumYCxznF1ys4P6XjtSqvpvwHGAiQbIVDpE-qwpQ1yjkuvIKWe1QENOb38ypVjqkF95fJ1ZMzzsep9XxR8kvxEs1toukRhGs2mFj70tGdf0vhAAr5CSzbKRewsDZ9KNg7rmaD_6p7SyrCFdyjK5JZZCx6YsNSqNxGw3sYv99nup-VdEz1IQ0QMyaNN8-DjStt39s5etTmQUNJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ebddd60447.mp4?token=mCQG-D3QalukdA_pYuj9JUX5vzbS7FEMFfiJrIBvgCenRgForq3eE7UDN3uKCkfej-0Idn0qBRjj4b4fL6tabISaP9HJrGWefNbaRPXOyLjb5uU-1P-QKRLB0fHXEoM1S1YE-vS6cumYCxznF1ys4P6XjtSqvpvwHGAiQbIVDpE-qwpQ1yjkuvIKWe1QENOb38ypVjqkF95fJ1ZMzzsep9XxR8kvxEs1toukRhGs2mFj70tGdf0vhAAr5CSzbKRewsDZ9KNg7rmaD_6p7SyrCFdyjK5JZZCx6YsNSqNxGw3sYv99nup-VdEz1IQ0QMyaNN8-DjStt39s5etTmQUNJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حقیقتا به نظرم سرعت Master+White برای شرایطی که جنگ بود و هیچ چیزی جز DNS و کانفیگ گیگی خدا تومن کار نمیکرد، مقابل مابقی روش‌های DNS مثل Dnstt و slipstream خیلی خیلی بهتره. کما اینکه نیازی نیست در به در دنبال ریزالور بگردید به اون صورت. نیاز به اسکن و... هم که ندارید</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/MatinSenPaii/3340" target="_blank">📅 16:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3339">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ws0woHvxfPS6vMvyggbMbjLTXFazhZOPerS4LIteZv45jexEgztknsObKjugjS2IU_0E2mpng5GDLY0kxEFM3oqMWH_7_QBIJX7usGvO_n-KdVAJpHcC1sPk103TpSeNhT5-9R5aBy2-ddhoXUBAhi5Dfh37If4cJeywoMyligKt8kxu1MsVmcjDqLgnwg2VizIzigE6q6m-Tdv8gGm8Q16eNv5wJUGXpxgDGqXLhusiRnSqyjFdNBZ4-RfWWaEBdHFpQfe23P2tQDtRXuu2Y4Le6Qhyct5OMbVYA3hH-iW2K7SVztwoQNFgDfYfCV0eSt0sS8q9ZgqwFDLTRViUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزدیک به یک ساعته وصلم، کلا 100 مگ رفته
اینم برای اونایی که از ورژنای قدیمی میترسیدن که یهو دو دقیقه 200 مگ میرفت</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/3339" target="_blank">📅 15:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3338">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">از MHR و Goose relay واقعا لذت‌بخش تره</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3338" target="_blank">📅 15:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3337">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این عکس‌ها و پست و همه چیز رو هم دارم الان با همین متد ارسال میکنم</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3337" target="_blank">📅 15:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3336">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خب دوستان، باید بهتون بگم که WhiteDNS روی سرور شخصی خداست.   با MasterDNS ستاپ کردم. که خیلی خفن تر از Storm بهم پرفرمنس داد تمام تنظیماتش رو هم ویدئو میگیرم و بهتون یاد میدم. به همراه یه لیست 6 هزارتایی ریزالور که جمع‌آوری کردم  به شدت ساده‌ست و بچه‌های تیم…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/MatinSenPaii/3336" target="_blank">📅 15:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3334">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hCxNAkd3nataCBpqB37ROrB5xciKmtzh8pXzRs6yij2lapwCAnDlJ9fww5u4XStIFx3PzmO8dSEIJUYQ7biGtB9tEvV53bb4NHV7C_au_FIschHI5PwgTkfysokGHwqnqdqvTZU9foYR-wCnDY8dUmPKrSI8mBmYLiETSEa2bjgGzb1B8bvVHPuDoUebi9d3ftbwV3363n1lTGr2a9xUHFHyesiMdLmqAqWQc1SMVKn1uZzcXApow6ys1-DS6lGgX-IImAjtyOH7oFErEisQDfZq1_9W2BTARh4zOsPEm085M7zkKXnN2sx8Cxe4aAKVjwsJBQznYcOIPU0YCSqNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q6GV2Tod3YPU4h3Opj2e8tMYvORw12-YO7oJwoie3FZHY98a5sWc9CbuMh37Bizie5YZh1xDzqk4Ei1z43h0yooNwnSuFVv8xf1KMVZKtwGzVW7gL7PvkZQ3yI70ExQcRuRDTp5gM4noj7cLqKsXSkB-NqcKV-hBCYkzJ40LirA9AgdHkxj83G1fL4pQzlisAL2_LWNX2iVPUGCTlJCG2EIwmIb9QCMHVQdUoZ0OJYYSxoqQ5zEtVk3-4b1DL3JrynGPUY3pZast2WAqhDkdNqSkZ_mUqUbCXvMEWWclpafqOCb_yH3Vym3qyyLHyDS-mhW4QlyJQLJoq3wgGMcLsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب دوستان، باید بهتون بگم که WhiteDNS روی سرور شخصی خداست.
با MasterDNS ستاپ کردم. که خیلی خفن تر از Storm بهم پرفرمنس داد
تمام تنظیماتش رو هم ویدئو میگیرم و بهتون یاد میدم. به همراه یه لیست 6 هزارتایی ریزالور که جمع‌آوری کردم
به شدت ساده‌ست و بچه‌های تیم در تلاش هستن ساده‌ترش هم بکنن واستون
سرعت دانلود تقریبا 500 کیلوبایت بر ثانیه. بیشتر هم میشه بسته به نت و ریزالور
اینستا راحت باز میکنه
توییتر همه چی به راحتی لود میشه
و مصرف حجم مثل ورژن‌های قبل اصلا بالا نیست</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3334" target="_blank">📅 15:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3333">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آموزش Goose Relay رو می‌تونید از اینجا ببینید: https://www.youtube.com/watch?v=tzjVg4O6dVs  چیزی که دیدم، روی اینترنت‌های متفاوت از بد تا خیلی عالی جوابگو بوده</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3333" target="_blank">📅 15:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3332">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آموزش Goose Relay رو می‌تونید از اینجا ببینید:
https://www.youtube.com/watch?v=tzjVg4O6dVs
چیزی که دیدم، روی اینترنت‌های متفاوت از بد تا خیلی عالی جوابگو بوده</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3332" target="_blank">📅 15:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3331">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3331" target="_blank">📅 13:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3330">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XApHa9L6KeTyJSnSlBwb-CQEKoI72Dsk3wb-SNywV0KjpN_GygYsVUeEeZHkktZ2YLNjG8I_csdW19sc-zR8p4FVDgec1wF-vpNotC732unfHtj9ukl7CtPePku-VeMs7krbbw21lOnr0xu2XYlpp1YJKAp_FQZGVgdKB-1UqVkKzR0hDvTCfvYQtUD-QMH5glrflhApxM9gO5Fdv3FoJO0tPNLRReXtAdG64GV60oTPulvvNtX_EChR3dpuQ_Fgt5NPXuLNUpfIDTccGTtvUszk-Lb4GkSkljHdJrgDc0LforH2ahFubQE9MqJjCfAyLuyYRGnUpXgSrZI0u9vr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سری از دوستان روی مخابرات و اینترنت‌های خونگی دارن با SNI-Spoof وصل میشن مجددا. زیاد دیدم از صبح  hcaptcha.com  46.38.137.156 81.12.32.136  امتحانش ضرری نداره</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3330" target="_blank">📅 11:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3329">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z_udugstwffgafdr67_K_sdOemTfvZbe3J_F9O-h5Fv9x5BCb5JLAp0IeFfKVq1OT8dgbsM9m5YbsfjP-c7pC5nFy88HXiGhntWcHkGrlhG0djuJeI1cWOH-xwy0mLmCO1Zo9WWfIzdsopiRVao1M_DTvxiieH_Yz0-N28ihkmx6n3vT-_VG-wQaD6oF-0ymGm29N0qYmr7UOWz8DAYbemv-tn8mUu3EsNSndZeFM-gzH2zflCAnDMhhyWoBvi9yeGOxcblao2BG-2EDYM7C0UNTXiFuA2SwVBdm6-4nNI_vLDwxJDDQG7pDG4eATFXqS5pph3XSUyI6ZyfXgKc1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر خاطرتون باشه دی‌ماه حدودا دو هفته میگفتن فردا وصل میشه، این هفته وصل میشه، پس‌فردا وصل میشه، آخرشم تک و توک روی یه سری اینترنتای خاص آیپی‌های کلودفلر رو باز کردن و بعدش هم من Paqet رو یاد دادم و ادامه‌ی ماجرا
برای همین خیلی دل نبندید به این صحبتای صد من یه غاز</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3329" target="_blank">📅 11:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3328">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مجددا آموزش share کردن اینترنت از شیر و خورشید بر روی تمامی دستگاه ها(باید به یه اینترنت وصل باشن)</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3328" target="_blank">📅 11:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3327">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ny6pE6GQ9_2pxIyGQPXkfaNI2m2sEiroTYk95JW1oEIoN4djvnKZMIobMjoTksycOwzOC4yY1qRVEcsxnvy93QVt6g5H33TAeFNiFZ7Qxl0OgKaL2eiwmQRomyB4e-neVRiXnGfecKt99_UUtGNVvNwI2iJ9AwnTDRufceiwOi-PC2qw2Be0-rjqrrugoXX8zmA-je9tOXLmk-Ek8Bpwh5tABT-vnNgyCWJdjRgUluAaWz37G8yC_FSVYwYPKKb1BDzdel9BIyUqu49lBygVCPHKR23XlXsLjNRMDnG9THYJ3Xu1cJcIJpirDL6_joy_2zHXUO6_qThOZXmbussFkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سری از دوستان روی مخابرات و اینترنت‌های خونگی دارن با SNI-Spoof وصل میشن مجددا. زیاد دیدم از صبح  hcaptcha.com  46.38.137.156 81.12.32.136  امتحانش ضرری نداره</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/MatinSenPaii/3327" target="_blank">📅 11:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3326">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یک سری از دوستان روی مخابرات و اینترنت‌های خونگی دارن با SNI-Spoof وصل میشن مجددا. زیاد دیدم از صبح
hcaptcha.com
46.38.137.156
81.12.32.136
امتحانش ضرری نداره</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/MatinSenPaii/3326" target="_blank">📅 11:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3325">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">150 مگابایت همراه اول مصرف کردم با VPN، بسته‌ی اینترنتم نزدیک به 1 گیگ مصرف شد
چه خبره؟؟؟ ضریب زدین روی نت بین‌الملل یا آب قاطیشه؟!</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3325" target="_blank">📅 11:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3324">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ui5VhpxSmNHNjCWeJ--EmxzZk4SciX0QnElgUxuJe-3vEGm829VItnTSl_1DrzCh3RFoYBjFjEj_fGqddCwbC2pSHkQz1exvPYWhORAHaWMt1hvkQf6cL9ML8Zp5AuCUwKJ3AAdFJK-sMbY7rijNzyAuWUdwC4o_PC-FWzi45Z29NFA5GPz30Yoyd08IZ0odmAVqt3o-r2BRwVZdseqQ75JNl8o9Xo3lX3ay30shpdMLOLnRwLcPf73Hdw1AtygmTc1J_1FQ4_h0bOkkq10lgSdKc4-8EOHqk1CBHj90w8c1cvT0WXPD4D0scN5oq6zlsMhv-gcZyPxOM37c5UMibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده از نانو بنانا و Veo گوگل برای تولید تصویر و ویدئو با هوش مصنوعی، رایگان و با اینترنت ملی:
⚡️
پیش‌نیاز: ابتدا متد رایگان و کم دردسر MITM( https://t.me/MatinSenPaii/3151 ) رو برای خودتون ستاپ کنید.  1- سپس وارد وبسایت vids.google.com بشید.
❗️
نکته‌ی…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/MatinSenPaii/3324" target="_blank">📅 10:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3321">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kxtOOrldhwkzDGUDu1X4s4QdwlAieyHLfESEnMXN_DmKT5rxJbqbTtXhFupTPSg_ydf5n18buxSAg-4Z6DXtuNvoKvO6rLTDY_jOcWYmlk1ku1im5iro6JRxoJ80HVBn0C05gBOSbQaXlsv-_H-ynIWu3P4ucZ4rcMS1gu1OzQ9NJxnaJqdnUEItyLe0XRZIhnj3ayB7EJ9ZXYjW_l8ggpjrCICYwWSsgVxI64UwpVnIPlqi18HqFE8HXqNhMH4w6kvE3O3K-9qfnVwK7z3C-rg7w8QFQbKnL7OfeFXDlHutuI0IUnvGB9xIjbqqLM22mJ4PcosbbUEuwNJnHFdx7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RaZwJ9FS1BCr_wcFV2_VA6XxkyimfgdsXYnDWeA5V3efOI7Dub8sRWFmQUUdiWv3uKIha-O2mJmXrvccgvMREJQIk2YDOMp8xzQKJ20PUtnHXio-LUvR4FYb_tVxm3jR5qNk1XWj7CVHfdrihgX4wIlXsCM3JstqZ1VZnq39Oc1llxNbN1hRzYkdg4AOWKK-E89hURCBLT1YdEvQrJP8lPUErY2JvPlLYxg9NoFNejyHzXyF5R_81OCbMpmvcV9tquI1_SuRNR62O2O8A9g-VlSnEO0M8QY41DwK-4ZBu18UXsAJv76MvZ3WjXYzh8dT8cedGsmMfByAGlsXbBD3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hF7VNGclkxaUjcSyv1uJb-fjKiKUT94Xc2LvdH133JaSMc_GmC8gvaY79wLzrGZlhPROCxw5NVXpDtyKdQmvMZxzxj4TmJ8_6PJvd__SJuyGXXQgrHiTUwzLJ_jkvWnOqKSNj2q8Tlea_1Jz57K3zFyX2xj_aZP63dGVI06GrFIUCsozbuAFMJIGLLszzeiMKoa23SXDZzr7kbxhqMCcnJ35fnZkmZDP8DgD6AyGkKsu7FOdWOc4CH4f0vEpUVj2aGB5mfAjXtIMjshRRv_rxW7HLG8F8rgMyoexVYoKidrgoVnH6kojloD5I5JC6UlvhRmsjujMKb1iZu59f0-36w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده از نانو بنانا و Veo گوگل برای تولید تصویر و ویدئو با هوش مصنوعی، رایگان و با اینترنت ملی:
⚡️
پیش‌نیاز: ابتدا متد رایگان و کم دردسر MITM(
https://t.me/MatinSenPaii/3151
) رو برای خودتون ستاپ کنید.
1- سپس وارد وبسایت
vids.google.com
بشید.
❗️
نکته‌ی مهم: اگر با گوشی وارد می‌شید حتما روی Desktop Mode بذارید تا لود بشه.
2- برای تصویر از قسمت image استفاده کنید.
3- برای ویدئو از قسمت Veo استفاده کنید.
4- اگر برای ساخت ویدئو با سقف روزانه مواجه شدید از اکانت‌های دیگه‌ی جمیلتون استفاده کنید.
❗️
نکته: در صورتی که در بار اول تصویر و یا ویدیو جنریتش تموم شد و چیزی نمایش نداد مجدد صفحه رو رفرش کنید و مجدد پرامپت وارد کنید و مجدد جنریت کنید، بعدش درست میشه و نمایش میده.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3321" target="_blank">📅 10:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3320">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3320" target="_blank">📅 09:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3318">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizi’s Warm Corner((AZIZI)⚡️)</strong></div>
<div class="tg-text">دوستان پرسیدید که روی
آپ موز
زیاد اگر آپلود کنیم چی میشه و ممکنه سرور کم بیاری و این حرفا
باید بگم که نه موردی نیست اونقدری سرور دانلود ها جا دارن که مشکلی پیش نیاد راحت باشید فقط مشکل دانلود شروع نشدن روی سرور لبه 5 دست من نیست دست آسیاتکه و خب 2 شبه میخوان درستش کنن والا دیگه نمیدونم کی قراره پیگیری کنن</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3318" target="_blank">📅 09:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3317">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سیمکارتی که خیلی شنیدم ازش جواب بگیرن بدون هیچ تنظیمات خاصی، سامانتل بوده تا الان طبق گزارش بچه‌ها
به علاوه رایتل و ایرانسل بهتر از همراه و شاتل بودن</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3317" target="_blank">📅 09:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3316">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک سری از دوستان هم گفتن برای اینکه روی همراه اول و ایرانسل وصل بشه، باید از بخش About Phone, Status, Ip address آیپی رو ببینید و برای همراه اول باید با 29 شروع بشه، برای ایرانسل با 26 و باید انقدر بزنید روی هواپیما و بردارید تا روی این عدد بیفته ابتدای آیپی.…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3316" target="_blank">📅 07:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3315">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آیپی ارسالی شیر و خورشید، رایتل:
142.54.178.211
5.144.129.174
80.191.243.226
2.16.53.50
79.175.169.59
95.38.201.199
5.160.13.85
2.23.170.80
193.148.67.117
2.16.53.11</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3315" target="_blank">📅 07:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کلا وضعیت اتصال به شیر و خورشید خیلی بهتر شد از دیشب تا به الآن. خیلیها رو دیدم حتی بدون آیپی وصل شدن، کسایی که یک بار هم واسشون وصل نشده بود.
با زمان‌های متفاوت
برای یکی ۵ ثانیه‌ای، برای یکی ده دقیقه‌ای</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3314" target="_blank">📅 07:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3312">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">☠️
دانلود از یوتوب و Torrent با اینترنت ملی، به صورت نامحدود!(پارت2)  توجه: ابتدا باید قسمت اول این ویدئو(https://t.me/MatinSenPaii/3151) رو دیده باشید.  لینک داخلی: به زودی قرار میگیرد
⚡️
لینک پروژه عزیزی: https://github.com/TheGreatAzizi/AzuDL-GC2GD (با استار…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3312" target="_blank">📅 03:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3310">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizi’s Warm Corner((AZIZI)⚡️)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeO-tw6oi9vSPQMg12C1QagkZ7DBN00M_xtFN-IRD5k4HYH7jzMhhs7EKTqN27ho2NaC9X3rnyhrgZvJPTGohuAVxCuRLq4yOTO-iz1sEClFj-bRS2oSADj4WQZIMn3fEP1VFDCjU8tF3Kx65esAw9Pca4j3WqFAtvc7rzAxIZuqAb8i3RN0Yo3bRUa4PRbxYpxjYd3SBe1j3oRfbTqJrMq2ejMySpFxom6_0BQQX__9FeHHy2ZK_hrjXlYK9rL04jA_BApM3tIECD198UWCnDVddHvKOZLqMyqudOnkGg1ATe_GD6Hdfprai0CzgIXfmOX6L9r6Su9j2t_LLH5eMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2PPOSqCtOAG5Opp8-6JnUQpTXEpIi4UHe1a9NZEqyJ_bd_QF1U6YGtjVOnhExNhfBCUWim-kDzAHnBQq3wHjvIYnVE0weK9Qjw4n--EZKhvcCofAghrHUsKsZz5HKTXomyrmG7YjmkYUv58RL73-eO0NyFkDv-9s_TdUKsMIy-3YiziYj7S6_X8urPkwVksCflcf2ZfkFXWKZFarU25HcDHyHHQ6hz_7uBzeKuJXwX2N6_Nd057LOm4lCFLndEB3a7qK4jMsoDA3WmRXchTnoJIerpwy6iUFC5krN1kxKTppWv-Ox1el3Y28T70M-v0Xi3VzARpwGykOkti9XF4sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپ موز
🍌
یک آپلودسنتر سریع، ساده و امن برای اشتراک‌گذاری فایل!
📌
با آپ موز می‌توانید فایل‌های خود را آپلود کنید، لینک دانلود اختصاصی دریافت کنید و در صورت نیاز برای فایل‌ها رمز عبور قرار دهید.
✔️
از امکانات آپ موز:
➕
آپلود فایل با رابط کاربری ساده و سریع
➕
امکان رمزگذاری روی فایل‌ها
➕
دانلود با ترافیک داخلی (نیم‌بها)
➕
دریافت فایل از نزدیک‌ترین سرور در کشور به شما (تهران، اصفهان، مشهد، تبریز، شیراز)
❗️
آپ موز با هدف ارائه یک تجربه سریع، امن و سبک برای آپلود و اشتراک‌گذاری فایل طراحی شده است.
🗣️
پ.ن: احتمال خطا و مشکلات پیرامون لینک دریافتی به علت تازه اجرا شدن پروژه و همچنین اختلالات پیرامون شبکه لبه آسیاتک بالاست!
برای کاهش رخداد خطا های احتمالی به صورت zip و یا rar آپلود کنید.
👀
توسعه و برنامه‌نویسی توسط
theazizi.ir
با مشارکت
MatinSenPai
لینک پروژه:
🍷
🌐
https://up.theazizi.ir
🗣
@luluch_code
🏠
theazizi.ir</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/MatinSenPaii/3310" target="_blank">📅 01:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3308">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یک سری از دوستان هم گفتن برای اینکه روی همراه اول و ایرانسل وصل بشه، باید از بخش About Phone, Status, Ip address آیپی رو ببینید و برای همراه اول باید با 29 شروع بشه، برای ایرانسل با 26 و باید انقدر بزنید روی هواپیما و بردارید تا روی این عدد بیفته ابتدای آیپی.…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/3308" target="_blank">📅 01:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3307">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک سری از دوستان هم گفتن برای اینکه روی همراه اول و ایرانسل وصل بشه، باید از بخش About Phone, Status, Ip address آیپی رو ببینید و برای همراه اول باید با 29 شروع بشه، برای ایرانسل با 26
و باید انقدر بزنید روی هواپیما و بردارید تا روی این عدد بیفته ابتدای آیپی. من خودم حقیقتا ۱۵-۲۰ بار گذاشتم نشد اعصابم نکشید. شما چک کنید محض اطمینان</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3307" target="_blank">📅 01:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3306">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eUI85aSEbD7HCYxTVE8Hjt9lmdAN5M1EDXNhAK8iAEQtSLU6dlSs1wddP5dThPGr7RpixhfmzTnKR7UEuX-AWqALwk0lrI2wzGHsfsoLudDhhYIln9BrRWSz3GuGWN7XYl1reNZfs5bso58UDp-tgS10fqMsX4OHMiIAGBmTYSxcFt2Dk9cewtmpR0dweOwXYA3h_GYcp2Trn-8a-9AI4p4YNSQO0qnZywsEvyI32wK5yQc2Al-KR6drOSCbeEvV__SIKFmQmPNzT5DIXQGokHqsUNhV8B6va3m4xjoDCTi5wzMepHbb-af4ldjh2CQcex8MUBJh3_hDI26rDo59oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والله مع‌الصابرون
😂
😂
😂
اگر گوشی بی‌کار دارید، با آیپی‌هایی که بالا گذاشتم تست کنید و Beast mode رو هم روشن کنید و بذارید بمونه.</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/3306" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3304">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/inT4df1mQFuyZqGkfCJdy8PIQ7qWxxeA2Tu4RlecrNEjidAS_cx42RmPIZCfT8nL8DuQ1cYeigFwaj-u0Bw3Lp5YU6VpfJDUmr09U-2YIKJKmwHr20bBbkTm14394l2GkdUAeEpS_7r68ccTh120OPVDo35iS7jTIfv4CjCrLjtNzpH9yJEZIDgAxj4wy3ial7T8MsECcYvfiRszNNS46DikpBWoYwnmpq9WSgJeo26JlM3mTdnnZyy41XjuPRVwZorB25LIHlOZ1gUvJsoSXQi2N_mAajT62u5fmFkbMcR_SQoDt2srSVBrMCISa8iiakZX8uGX0T35htSuwv1cJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/shyGaNnRm9f5ra-xpVuKeD34nCiC9xj_6cPM9XXlKSPx3BVO3_Ap8nqwr39Xe6kxy9d_4guCdrkM6L7mKfsgVy3W8ePSYRZaIJ836BGZQA0NKRnta19KAsk8egNUnHbPuTbrk89a2I9Mk4e6QR2x6AvRa-4KOThphofiEMDG580vkTfmMsxlhVSlQ9LW7iAWd_ijV0AB46VEpwd9lUhN32WUjxXaH1EPNZHZ52k7T8Fd-C7M2PfPpteOKtGrMPM1KAif-3QoxD9l0yagdsT2KPUa6sQ5iOsssAcIdG6ksFNoB5z4ePyDTi46tgwtg3039VcO10N-Aaw9CJJBhRXrTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آیپی ارسالی برای شیر و خورشید: اقا سلام ایرانسل شیر و خورشید وصلم الان ۵ دقیقه زمان میخواد 5.160.13.85 2.16.53.11 2.16.53.50 167.82.48.223 2.16.221.37 167.82.48.223 151.101.192.223 2.16.19.136 172.237.127.6 2.21.2.104 185.200.232.43 2.23.168.7 2.23.169.111…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/MatinSenPaii/3304" target="_blank">📅 23:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3301">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vyzlx04fXckVBPmYa0FPlG0V61b7KgRV0V5mikjPD7QWdSIimGujX0xsog-Sr0a_iU_5vH1ExihkNsqW6M3q_Yoox4lPJqVClY3Kzlx8tkMxd1TapvNiu-EXr3mwfCPH5VCG3KofMBQRa7UmKSaPJUu6KfhAib6Ib2TUUypDrAfd3yaQ7Y7j7htDq5M6_CVV8eRM9esC4iTzUm34brzBA_D3VZ44lXNfLz3yKswzNro2X4eHb_P_de3I82Qffj_Q3x3esmyA5TTcFBW82ry62mvAF-1d4tSMeCOBLZRfOA-Yk6Xo_9MXS1x2Qlv5eV4VIuOiPwdg3b2fQ2iiIkIITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gobOM0DoL1L8MGfL7iCC6Yfm3BWmlHuBES65V60H2aHxt_5aoI6HK7pLiNrofmgyuWnbwFMiyv5U8O8o-tX9mm517DEff2FeoF2rdpNry-b53WX6oajQbycWHNC3QO1xElcG4fod6x8r60-q2Mm-88REqNQ7-ZH4kr5UdtWFM47tNpDdz5kxTyKE3a6UvMA7dbMx3VjsO_-F5_HW_2F2BsPMuuLPaPRew4Pb-6ANFBxAKlvLl3L6jLhDR2wRkLk5jHbknz_mjg3Mdci1rddRp5mEHyRUCSMXRzGmuGfVxOrsrdMzwPhIelv-IJzmSi0ce3LfYAhHX_GXub8CpJIIow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hi_K45KFSOtg-7Tcsj9hUADEoGgIiUZC3clegznud8w8E7dwkwcFeT1hU3AEGowqAN1TaCdrsMLtD46jwyQeY2t0zTPEfzAvHoDxrR1BlBc-1uCJ8gpwQiBhDvnctQ5PchSvdtfcVICMO8NWpB1L_W5-2rTIvjsJoxL8hQsm7mIHWZIdK9Qg-DearAgn3HNgK5rhJNma40NwiRahHY6Q6545C1xsC1_pTPO3m6KJL3rWkH76C6aKsKpY0UZt7ZXBXEp37QRfVYCgm0eWsCxiK546NEc81bvawwzSnzf_RucoSOcl2aqq7lsG3TYgbp46wwKKl055X2s-xSeO_I2gmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
گزارش اختلال:
یکی از دوستان روی ایرانسل دوتا از آیپی‌های BPB اش روی پورت 443 شروع کرده به کار کردن.
محض اطمینان یه پینگ بگیرید.
آموزش ساختنش رو اینجا دادم:
https://t.me/MatinSenPaii/1965
منتها اگر نداشتید از قبل، دست نگه دارید و وقتتون رو الکی سر این نذارید ببینیم اختلاله یا شروع شده به وصل شدن</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3301" target="_blank">📅 23:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3300">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/3300" target="_blank">📅 23:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آیپی ارسالی برای شیر و خورشید:
اقا سلام ایرانسل شیر و خورشید وصلم الان ۵ دقیقه زمان میخواد
5.160.13.85
2.16.53.11
2.16.53.50
167.82.48.223
2.16.221.37
167.82.48.223
151.101.192.223
2.16.19.136
172.237.127.6
2.21.2.104
185.200.232.43
2.23.168.7
2.23.169.111
151.101.128.223
185.200.232.25
2.23.169.105
185.200.232.24
2.23.169.105
2.16.53.50
2.16.53.11
185.200.232.50
185.200.232.42
95.101.133.42
151.101.128.223
2.23.168.254
2.16.19.136
2.23.168.213
2.23.168.144
151.101.192.223
2.23.169.12
2.23.168.174
185.200.232.11
2.23.168.254
2.23.169.111
2.23.168.174
2.23.168.213
2.23.168.213
2.23.168.174
185.200.232.43
185.200.232.43
2.23.168.144
2.23.169.42
2.23.168.144
185.200.232.43
104.103.65.5
2.23.168.7
172.234.159.58
172.234.159.58
172.234.159.58
172.234.199.15
172.234.199.15
172.234.199.15
184.84.221.34
2.23.41.22
﻿</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3299" target="_blank">📅 22:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3298">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اتصال به اینترنت آزاد با کمک گوگل درایو!
😮
🔥
آموزش متد جدید اسکیرک!
📣
برای این متد نیاز دارید به یه سرور لینوکسی ضعیف خارج کشور!
📹
لینک ویدیوی آموزشی روی یوتیوب
🔗
لینک ویدیوی‌ آموزشی از زیرساخت داخلی  (مدت زمان یک روز)(اختصاصی)
🔗
لینک ویدیوی آموزشی از…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3298" target="_blank">📅 20:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3297">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">چیزی که می‌تونم بگم به اندازه‌ی قطعی اینترنت روی اعصاب و روان من اثر گذاشته، اختلال GPS هست
سه بار توی شهرهای مختلف گم شدم توی جاده تا الان</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3297" target="_blank">📅 19:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3296">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizi’s Warm Corner((AZIZI)⚡️)</strong></div>
<div class="tg-text">اتصال به اینترنت آزاد با کمک گوگل درایو!
😮
🔥
آموزش متد جدید اسکیرک!
📣
برای این متد نیاز دارید به یه سرور لینوکسی ضعیف خارج کشور!
📹
لینک ویدیوی آموزشی روی یوتیوب
🔗
لینک ویدیوی‌ آموزشی از زیرساخت داخلی
(مدت زمان یک روز)(اختصاصی)
🔗
لینک ویدیوی آموزشی از زیرساخت داخلی دوم
(مدت زمان یک روز)
📱
گیت‌هاب پروژه اسکیرک
💳
حمایت مالی از من
🗣
اینترنت برای همه، یا هیچ‌کس!
🗣
@luluch_code
🏠
theazizi.ir</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3296" target="_blank">📅 18:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3295">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کلا باگ پنل سنایی بود. از اون طرف باگ سایفون هم بود
متد ترکیبی یه روز کار کرد، تا دو روز بعدش هممون سر کار بودیم حتی با چند تا از بزرگان من صحبت می‌کردم نمی‌تونستیم بفهمیم چه خبر شده</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3295" target="_blank">📅 15:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3294">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/abafd93842.webm?token=BbrA2QK1ryKGgOglHFGoTOHuXeomWipPg-9KL-oJ6mlw37Oi6GqitP5GQ7Rqqp2C_Kr5-1_WVjCyoZoDJEkZGnXicE5maDd4CoaD-n0uJQ50_rPjjE_07Lbli3uHXx7ABDlLQRoslYi4ODy6rQZkRRcKPyjGNrmFcP7cBLh3pNrXwrWu0uCzMfLZ8YIgy9n4-oRe2gLmwSyYBKoV5A3aG1CMkla0Rvu1oZEOL8DhsZ2C3NLs-Cx8r_ZYUszPQB7Xk15mDPEcTTcJjepaezHjNOlXt9QuAUh8UkBil-EMQI35Ih2nglFNLsNBN7fYcFXcMONjc5RICE0cMoeDS2Q_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/abafd93842.webm?token=BbrA2QK1ryKGgOglHFGoTOHuXeomWipPg-9KL-oJ6mlw37Oi6GqitP5GQ7Rqqp2C_Kr5-1_WVjCyoZoDJEkZGnXicE5maDd4CoaD-n0uJQ50_rPjjE_07Lbli3uHXx7ABDlLQRoslYi4ODy6rQZkRRcKPyjGNrmFcP7cBLh3pNrXwrWu0uCzMfLZ8YIgy9n4-oRe2gLmwSyYBKoV5A3aG1CMkla0Rvu1oZEOL8DhsZ2C3NLs-Cx8r_ZYUszPQB7Xk15mDPEcTTcJjepaezHjNOlXt9QuAUh8UkBil-EMQI35Ih2nglFNLsNBN7fYcFXcMONjc5RICE0cMoeDS2Q_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3294" target="_blank">📅 15:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3293">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ORCbZVxfIzooWflZXNO-Bp152X-AyzLWfcrX32IyBK6YL_dZmzBwY8g-N-NYV5uwWqdiW7F_MbetHKz-hdn5YXv4FPub2EM6aIYEbfQItFgOC3-gIHu6Z4-T6eUVi7yIv5u4Hz9XH4m8F_UagMy_Bjy_bILR0OYAd4In1sEX3XpcX63W9NZNqgG1P7yhzkP0iTS1uK5dS6F5SiEwhl5LUme4DMuO3ODjDqo05NFvLMFiP2Lmd31KFavnlAzm3wiAUc101oxsCfS_95tT_kBaChSbFZ-MhOL9uxmqe7ktEaezDo77-1Myb123slXsnSUN6TEhMet-id6K9pQE5oBDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز، همونطور که عزیزانی که از زمان ترکیب با سایفون(اواخر اسفند) یادشون هست، این کار به ظاهر جادویی(!) باعث نمیشه از حجم کانفیگ جدیده مصرف بشه. بلکه همچنان از حجم کانفیگ پولیتون داره استفاده میشه. خواهشا همچین مطلب اشتباهی رو نشر ندید</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/MatinSenPaii/3293" target="_blank">📅 15:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3292">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nAITxhblpnpcLo3iZ7enrxrn6feowcelOVu8k8BVJlgzYHcTvLpMau133zTa4EM4Imb3RSrZkBE2_7jJOe6rIQhrw_hevPvm3uWDFq3baqpld4hg7ksldAKkJr23oOUt-3Nsk_JBFueqs8TRJBmT8SlUDKwpTFmkb8cHq5sMYUES0SYKAwT-NxMmMwuj5l5tCkaUEU155SsNQP_e63W8aIsDMBD4tPe68rYYAAMc4eZIb03Ey8JqNqCFB8n9QE7RyeYEWtuPN74eKUHbuLkLEuEFDseDrpJrXcxmN2UJPvXCR7SqFqZdxnuNAJUKZg8ikNWmIa_2NuZjtUgeekek4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز، همونطور که عزیزانی که از زمان ترکیب با سایفون(اواخر اسفند) یادشون هست، این کار
به ظاهر جادویی
(!) باعث نمیشه از حجم کانفیگ جدیده مصرف بشه. بلکه همچنان از حجم کانفیگ پولیتون داره استفاده میشه.
خواهشا همچین مطلب اشتباهی رو نشر ندید</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/MatinSenPaii/3292" target="_blank">📅 15:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3291">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه سری تک و توک هنوز بهم میگن که اسپوف وصله اما خب ۹۹ درصد بسته شده. روی سرورهای ایرانتون تست بگیرید
✅</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3291" target="_blank">📅 14:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3290">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZBTSnTc94BDGXaU_HEUT4jr-Hw3Shb-Lyd1Oq9pOgaZPxseJ7XblB4OgKCvPA_zmNzxLQ_itvMI41tTd80XmvyLI21i4UJsOjiovVi4oFbUdRB9wNEPlsdpb67FIFG5bt9Q14t18usk8WvU9-mJjxe89nitUgf1Rwg8nO2KUWtlzOKBxdDnLTVa6pu1f35v3NZZ2o9PK3_oKslguKDf_2JZvesne_hdSWPCW1cWsXRgLUp1PvnyUfBti6jmwlekOxEfKmO93Stel0x6KyADK7v2PN6cIJe4YLury-_AlZGHEZZXSNIeyk1Dg3_4c2AMmBy0l7MTD4DQowjOYc8vBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر آیپی تمیز کلودفلر داشته باشید، ۱- آدمای عادی(مثل من) می‌تونید با
https://youtu.be/svYBcv4bSzo
به صورت رایگان پنل ادج بسازید، و جای address هرکدوم از کانفیگا، اگر آیپی تمیزتون رو بذارید کار میکنه.
۲- کسایی که پنل دارید می‌تونید یه inbound وب سوکت(WS) یا Xhttp بسازید با هاست و sni روی دامنه‌ای که به آیپیتون point کنه و پروکسی کلودفلرش روشن باشه، و جای address، آیپی تمیزتون رو بذارید. این شکلی باید کار کنه</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/MatinSenPaii/3290" target="_blank">📅 14:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ppjkdVCwkd6ZesJEBjn7IECufEqVE6SLCPaPUPwVb5hdusStHWfv9cabWmtbFNaKKapt8n8KX9BDRQ5wUEoaFQXxfjE85FHQlzk7XoO002I9_zCfx-F8BQY-NkgYbi_SYGDTqsUPo_NSaWdaYpuxMRbDBF47hy_oznRPMGaAyrqi0mMeQ1qqmONrLpZxQ5s1C1w1aACmgDcpqrY6LNtIeYdE0j6JkJGZI6Liyy_Qy5CDjVfNCXEFavoBi90UsuFNjgCFczut-XZdEVDTKx02mDv2eHDgD6yzN9OZvqHZnoUayXdlHoly_BQMEaXrh0KnQdCPs4xISuhuO5vHvzHvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری تک و توک هنوز بهم میگن که اسپوف وصله اما خب ۹۹ درصد بسته شده.
روی سرورهای ایرانتون تست بگیرید
✅</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/MatinSenPaii/3289" target="_blank">📅 11:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Df_BnK7HTbAq3ka-mbI5CjRSW0_dsd2Wkdg99b3zxQ6u0j_7ozithkouvfGfJaDg5kpHSJeBIKd8xnrYEsuJpEGIddbvkFA4sqsyEJehUvl80Y07uvaJEaL49-3r0kbkpOnE4ekqMJTaUQvTnXC5J0clhvmA2RkBuCEjr4bpKo-FI1EkXXBkJYGX5Tj6Iu03BxPqvcxEapwW3TQncdWW3zRbUccv8ocx6F2rv33MzV1t-F4maraaH-VbOE-WRmfio2HmJXEwyr2wCzdhUWkLWnqjho3Lfc7t6FpCk_0bg4I4dV3WJhQCeF7prLTJ50fT89joJWxVheCocspQJSiJzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنین بود، افسانه‌ی شیر و خورشید
🫠</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/MatinSenPaii/3288" target="_blank">📅 23:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/du_AEt8hfCZFQDvQUprv21tBenxcylFugTslzFwlFiQ0HxHQu5j1nndmgwtpg1Kv7Eo0QgjlK7AJugDhYeismhRmi21SL7lzBiuolUAgY8RfvhGASrnyK7HgAfy6WYCQFQaR7HGZ-KAHUF9Ap5hiPX5HvBxdK8c_Yvd_iLQ6nsnwYqsxz9DRm3QqXqrDMjHHJOCmh8h2axMW_iNNmSexIzxKKIy8h8ts2UuxL_xJpR298I2Q6o_ZGuAbdt68Wlk_cowuUJFzXoRKkgFKd1YBZ3p94uRbUzzWTXsKOgLLV_s7ssSet8MNjiJAkWUh8_SSSYwnHIxnm8k0T99cm0yA4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3287" target="_blank">📅 22:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نکته‌ی مهم راجب سرورهای StormDNS و MasterDNS که روی WhiteDNS استفاده می‌کنیم:
هر سرور و پورت 53، فقط ظرفیت 255 کانکشن رو داره و دامنه برای تعداد بالاتر باید لودبالانس(توزیع بار) بشه.
خلاصه اینکه اگر با سرورهای رایگان سرعت نسبتا پایینی رو تجربه می‌کنید، به خاطر تعداد بالای کانکشن روی اون سرور هستش. اگر سرور شخصی خودتون رو راه‌اندازی کنید(که آموزشش رو ضبط می‌کنم واستون) به هیچ وجه سرعت پایینی نخواهید داشت</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/MatinSenPaii/3286" target="_blank">📅 19:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نیاز داشتم روی هاست X ایرانی که اسمشو نمی‌برم یه سرویس بخرم
می‌گه دامنه می‌خواد
رفتم دامنه گرفتم
میگه فقط دامنه .ir قبوله
حالا رفتم از خودش دامنه گرفتم
میگه احراز هویت سطح 3 نداری توی ایرنیک
رفتم ایرنیک میگه سامانه هدا نصب کن داخلش احراز کن
سامانه هدا نصب کردم عکس قیافه الان منو با عکس ۱۵ سالگیم که روی کارت ملیم هست می‌خواد تطبیق بده و نمیتونه
میرم میبینم نوشته شماره پشتیبانی ۱۵۱۰ هست. حالا هرچی زنگ میزنیم هیچکس جواب نمیده
و دیدم هرچی دامین داشتم هم پریده نمیتونم تمدید کنم با اینکه پولشو ازم گرفتن
رسما دیوونه خونست</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/MatinSenPaii/3285" target="_blank">📅 19:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ورژن جدید WhiteDNS Desktop واقعا خفنه. الانم با سرور رایگان وصلم هر سؤالی هم دارید توی کانال تیم جواب داده شده: @WhiteDNS</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/MatinSenPaii/3284" target="_blank">📅 16:57 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
