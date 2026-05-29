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
<img src="https://cdn4.telesco.pe/file/fc8MANGoyFNWxknRR5CfwsiizoY7uJ93h8rrzsZ-DfY4Th2vF03rWinw67vXyoQzFa4dgKTY0lb9K_ldPqFXbJ4oXMbbO3KbmU4_0hxLDpftP-YW376m7eW3rDHlaBvY-WwjYTp7DY9jj1lcOsxn8PGZ_rdU4KSMz93c4UQq9OuzEnYt_fta2X41BfGNYROmNsB2x0F4CT2Pmdsy9sJEjpcXMMuBo1QtXvTtiH8z_Y4LbkRqx41BWmUL__BK-tzMJoLN9uBu7OtxBCmgx556uKWRx_mnbFH5JtSii3DMBEu66uYmWGT5Q-qCBJCLjGZY2LYV0PhbFeaPA-hvow_i9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 122K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 20:58:16</div>
<hr>

<div class="tg-post" id="msg-90425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تیم ملی ایران موفق شد در یک بازی دوستان ۳_۱ گامبیا رو شکست بده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 307 · <a href="https://t.me/Futball180TV/90425" target="_blank">📅 20:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=SRIdOaTqu7fu0WibDFkDaj8N7IQxorhY4b58eN6CUV0JMmijQgxI0DAaIRCuvTAThw16vsiXCIRyjF-zboNs6_8e7h-kiHCSe7VRtYYqVaEr1NRh60SOKbAC3VeFfyZEikmtD7C8nouc-OgNu7PUahAbzUj-GyJ2X1BB_i9ktCki9l6Wo-UKtxSjP5YMXAeYATPPQxJWE7T-1gQl5Y9h2LPQl-i6B8pWOzPdlzNGe61EbPRT3ErzOsh7id1q6_N1DwSEQs6HhcmRPWc5OV9WZBWEQN08VN4Z-X75QQpEkHgQ4oho4Kog8h57HRiSHgskRmsFzTt_-gl-ti9BTc0lYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=SRIdOaTqu7fu0WibDFkDaj8N7IQxorhY4b58eN6CUV0JMmijQgxI0DAaIRCuvTAThw16vsiXCIRyjF-zboNs6_8e7h-kiHCSe7VRtYYqVaEr1NRh60SOKbAC3VeFfyZEikmtD7C8nouc-OgNu7PUahAbzUj-GyJ2X1BB_i9ktCki9l6Wo-UKtxSjP5YMXAeYATPPQxJWE7T-1gQl5Y9h2LPQl-i6B8pWOzPdlzNGe61EbPRT3ErzOsh7id1q6_N1DwSEQs6HhcmRPWc5OV9WZBWEQN08VN4Z-X75QQpEkHgQ4oho4Kog8h57HRiSHgskRmsFzTt_-gl-ti9BTc0lYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم ایران به گامبیا توسط طارمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/Futball180TV/90424" target="_blank">📅 20:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=bVpZT36cezftsz9UkR0fJl8zNX3wevuy349wyNKogcRQj33dI_cOwdm1xW-6_8bCpAWAUKdKajI19RXcwkNNyfeb-GLs8Muxcdrf16o_qXONPRtk5iTw191YWPghvBwsgxOA63ep6jD6zAzxwdG6Lj5Y0kH7dswf6Ppn-c0uYUOapVCfEt1Sd9334Je8hkyxuE6T4PMXX-28lyEPuOP0TbHR43ZgAZtkD-2m18GHnoVw6ZfVUrXVT9RzlFVKgx7bM-v9CxuwietHUwotPBvWYh8ZpZOGgPtOwACLxgQEJXc0s2zljjgUNoULMiVVrDEra9gqZeWPX5v8fD1znzlA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=bVpZT36cezftsz9UkR0fJl8zNX3wevuy349wyNKogcRQj33dI_cOwdm1xW-6_8bCpAWAUKdKajI19RXcwkNNyfeb-GLs8Muxcdrf16o_qXONPRtk5iTw191YWPghvBwsgxOA63ep6jD6zAzxwdG6Lj5Y0kH7dswf6Ppn-c0uYUOapVCfEt1Sd9334Je8hkyxuE6T4PMXX-28lyEPuOP0TbHR43ZgAZtkD-2m18GHnoVw6ZfVUrXVT9RzlFVKgx7bM-v9CxuwietHUwotPBvWYh8ZpZOGgPtOwACLxgQEJXc0s2zljjgUNoULMiVVrDEra9gqZeWPX5v8fD1znzlA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ایران توسط رامین رضاییان در دقیقه 59
ایران 2 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/90423" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7455525379.mp4?token=kquPwNNFGONdBcBgQPlsZt78rlmLlq05ShdKviPCmLRVH1emYePiVKQ4YRBkLQJi2XXxMxeJ6cQZwxPu0hRWkxfYF8OYw41zZSL5G85o5Iy7IlP6QHNvROF38IpHnqOfxnHe1YtNK301OIqJUc3prHL3UCXSKGDqLcZIwJeW0T088aYlTO_4WJ2wcMaV4T0d2ATHMlz_-o4Q-BTwC8dvdRIX2Eh56oQzeduShFOIgpTVO1DC9dhFB8Ty8ca9nYRzxxhiicTl9aRpl-KchoDRc8UX8aHphvBBS-Jqkd6GQtmbO_e1YQJZirxjifrbr2LzFZNLQgFMAkTHN8fsXlYZGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7455525379.mp4?token=kquPwNNFGONdBcBgQPlsZt78rlmLlq05ShdKviPCmLRVH1emYePiVKQ4YRBkLQJi2XXxMxeJ6cQZwxPu0hRWkxfYF8OYw41zZSL5G85o5Iy7IlP6QHNvROF38IpHnqOfxnHe1YtNK301OIqJUc3prHL3UCXSKGDqLcZIwJeW0T088aYlTO_4WJ2wcMaV4T0d2ATHMlz_-o4Q-BTwC8dvdRIX2Eh56oQzeduShFOIgpTVO1DC9dhFB8Ty8ca9nYRzxxhiicTl9aRpl-KchoDRc8UX8aHphvBBS-Jqkd6GQtmbO_e1YQJZirxjifrbr2LzFZNLQgFMAkTHN8fsXlYZGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول ایران توسط آریا یوسفی در دقیقه 47
ایران 1 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/Futball180TV/90422" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/Futball180TV/90421" target="_blank">📅 19:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=HipReiACZHoFVo75iOTuJurksAOhzg6ljE48ZDaoXOtr97iucCeR5i1fzNLU0NQMTCxWZ200kNgQSqk8z5xLaGNsJ_-Z9reklJBQnRHXa5e28b7WWTk1dz5CToB9Z7JbUZmSYt69imoK-k6JhYfe2crypDr7f-5pHihIhpNCe41Chj3X8P2MjgX_lVm-ZXTU4WvkLYqStRiMW8_ouZ7XimVxRY3F5cGQhv6imme-W4X38h54VUzesoTIo4xxUrfD93pxIlemwZT2TqmdrTeroNvwzr9z0r2eOEcDYvhLbpWaueW4JsniaPSoW6Afb4x4a0lLl_uwnhCT6SMOwvUxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=HipReiACZHoFVo75iOTuJurksAOhzg6ljE48ZDaoXOtr97iucCeR5i1fzNLU0NQMTCxWZ200kNgQSqk8z5xLaGNsJ_-Z9reklJBQnRHXa5e28b7WWTk1dz5CToB9Z7JbUZmSYt69imoK-k6JhYfe2crypDr7f-5pHihIhpNCe41Chj3X8P2MjgX_lVm-ZXTU4WvkLYqStRiMW8_ouZ7XimVxRY3F5cGQhv6imme-W4X38h54VUzesoTIo4xxUrfD93pxIlemwZT2TqmdrTeroNvwzr9z0r2eOEcDYvhLbpWaueW4JsniaPSoW6Afb4x4a0lLl_uwnhCT6SMOwvUxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول تیم‌ فلک‌زده گامبیا به تیم فلک‌زده تر قلعه‌نویی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/Futball180TV/90420" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90419">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISWeTIpSZH9vU-QuXKvB_SwtbE1TiDUCUbgrQOYFNtMOaWQwGddEmnnxQUDU3MBA_-WYLPHDXysg682_CmWeu2gfFrCUPKR0r0AAHcsbIS-4ahSXGNqRbxwpxeq0C4qgz24lYIbL_MLsQsx6eCezi-T2T6FJmpP5sr7tjAuwgOlUCMyXedEG64TaH-7rozEyzPdnwrEy6ZqwOt4NQ-nSW4Z2sBmCw8BZKmaP554fYoQWInzMu0GLYZCImPIEmnhaCMHB_0umw8TT0DOKBbgaxosTWRCUDKQPP3QBXzE15_K8JjfjiNAvsiFSnW52536V2OFnkFZ__viCDq44Sj_5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:
برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/Futball180TV/90419" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90418">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/90418" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90417">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoPTU0nditKWTVjm6FkiSnMuPBVV9CLxfGYWV0ouUzyxjWocOp4GnomHXz2xXqFroJqM1dEhxZ7LRYWLROKoBK52H3wyE1N98BlBHtCWIzARgG9H5sIgdP1SwnIlERICsuvFN0dSO0fQZN7wYikoWRy_gM6nW72zmw7sO1kxEfkh4uhXsH8Vvgv6-P68zhMtu7fU69kriBBoSBaUruOrCqY0WVnCOI5FRL0Uy8SEMGYfAMOhmTdA-klvHejV64zO5mjPFuyxbD0vWprqf6Au8wj__YfSQB3mSsXJ4mXNta-5cTxJnVUUaKVTSNUCGZUBSoePbG84Ly8Yfq22bO1lng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g8
📱
@winro_io</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90417" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90416">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl_oljQWGX71WWhk_W2riclgEvakVJGcOZm082teTxPYnhNyeA19SZ124o34NhdUCj1bWqIDxmaC-epj0NJmfkrm3FeCk9igheeYZhOyptHGA7Ks9XLBMb7S_nYLWJX9OsN70v53k4TXcmnRia9yd_6ZBrY3ym99JtMZnU7Tb7do9eteOJyrAKMYjPalKu4z9eHDCDTrkRNVdSVntzfpfCMZzSDacIdJqmZYNt6xUvUevuOvO5Eu946ni3RSqO_YYqzncI-73ZRlkaBi22MdRdw2sKZlz-s6D0UDHYmwdewjRsmaJdWBqp1zVega8nMavMfz2F858znb-tDgJWSq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
حساب‌رسمی اتلتیکومادرید دست‌بردار بارسا نیست
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/Futball180TV/90416" target="_blank">📅 19:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90415">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb_lVxWJl_o4JygknDnrVdD7w9LohIBpckXlrCyzKmEFdMFSeJTqbsspgytCpBK_ue7CflNTVAPprU1ut098qG22-Gczsj-NRNKE8Zich67VhhSDQryHVMzFgB1XZi6fMRasNxdcDpNdNrOiQO_L3DLsnOSk7-hNKLUIvoKGvYBjAgHI9j-Rw4asS4-WTGrC03nuJyzolnxcCiiYKipoaX_gtXVEpe89Pnqb3p8IsbwOFCTMgKXYPONcIJ31nOyyJFxOPZeLhNDhl_yEb0HH6X2ml_jlLe6xOthrtQVTF9NCmo99W819Nk-gX1w0BuoNkVYrK7fEi3wA2B1UqBfd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/90415" target="_blank">📅 19:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90414">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krEkBobuxPipiwBmC7mcgPZNqyGNGeCdXv_To7Wub4KRToBoHCeWieA5fJNiXFXPWPkHJxMDzuiFZGtWJ6oipUhRsDXg3PBKJHt6BRPtJ92ksDdXkGsxi13MyEUu0oCvN0gn7TOTHjMyuFvosdNL0NqXcon92b69S_sAnaKeyx9_IX0XzdWLWgC7DRbps7aVRTVll2Hw1BkTeCMGGNoiKgkAPuf2LIqdGMoIvFdTb1g-HHcXpoN3iyyEy1QpwLxBq0vnpFa4HtjKopiNzEsO_2RubmGXbZQL49_zl0jxln4P3EYND5mpP2Df9FNKOTdXVv0dtYzJFNQIOs0QJ3CGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/90414" target="_blank">📅 19:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90413">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
دونالد ترامپ اعلام کرد که محاصره دریایی ایران از این لحظه به پایان می‌رسد. همچنین اعلام کرد که تا ساعاتی دیگر تصمیم نهایی درباره ایران اتخاذ خواهد شد. به گفته رئیس جمهور ترامپ، مواد هسته‌ای ایران بزودی از مکان مورد نظر خارج یا نابود خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/90413" target="_blank">📅 18:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90412">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ایجنت الهیار صیادمنش اعلام کرده در صورت تصمیم این بازیکن مبنی بر بازگشت به لیگ ایران، اولویت او بازی برای باشگاه استقلال خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/90412" target="_blank">📅 17:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90411">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDsLOC0yhzu5vP25kCen9Ws75unOemLi3IaN6bzxilu1DQOf-cnDDBZtBxMRxdUYAI-glB9w02lVn-tDspq2YXOlNlyHOuUau67OdD7rzgL2tnnC21N6ol73TLLiJUc89XCMVEy2Fz6VTLwT9fmGXT4TwyhKMYzSqRZa3gWMxROxBXT9M3ejDTMi2c8c_aTMod1zr7_nRBD_mav_DNc28P5v8NgaML5WtdUF3Yt10C3IR6E-zVFPOYvydtxuJ3ZKOzHNSGUVhK4qqG2FcF4TQy524mhtLMOdzEvP5S_72b_E3-nQBG0Tsg27se7AUlPKw1Otbgh6OG4VCvpTNvh3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر آقای‌گل‌های تاریخ ادوار این مسابقات
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/90411" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90410">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Barko VPN_v2.2.apk</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/90410" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90409">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90409" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/Futball180TV/90409" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90408">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97be903d17.mp4?token=JPetItp0ju0cCAm2YGQcdqDIZBeFAzxcqSeQWCv_EEWysKlDO_s4ckd44XE6ncZaFqVKVNcI9j6lvUlmgMEDtyHVWLyzsQw4oc2rB7aQQMFraZti63i5O9wfPmpMHNSTLddwmx_NtCtJ6STF6n-vZ2XVtWZnk0Xaa60TTsNIKbaxKiVaJ9uK24V9UIovn6qAEtabyBz3JkEjTT-xcSaXq-fU4psPOy0bgW0nJUBvQquf3RsFn6kX6kF0FmKFzSZe18zInNSwYgQpHnGTTISEidWHaYIt6RhPaevOO-kIxcjqzQHmMEcUK_1TuVKqdO0vSEKHdW2cqWkS2oQ-QFbmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97be903d17.mp4?token=JPetItp0ju0cCAm2YGQcdqDIZBeFAzxcqSeQWCv_EEWysKlDO_s4ckd44XE6ncZaFqVKVNcI9j6lvUlmgMEDtyHVWLyzsQw4oc2rB7aQQMFraZti63i5O9wfPmpMHNSTLddwmx_NtCtJ6STF6n-vZ2XVtWZnk0Xaa60TTsNIKbaxKiVaJ9uK24V9UIovn6qAEtabyBz3JkEjTT-xcSaXq-fU4psPOy0bgW0nJUBvQquf3RsFn6kX6kF0FmKFzSZe18zInNSwYgQpHnGTTISEidWHaYIt6RhPaevOO-kIxcjqzQHmMEcUK_1TuVKqdO0vSEKHdW2cqWkS2oQ-QFbmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل یاسر آسانی هافبک استقلال به الحسین نامزد بهترین گل مسابقات لیگ قهرمانان آسیا 2 شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/90408" target="_blank">📅 16:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90407">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgM1e_A8qpw-kZYOJ68Qk7s0Zfkwi_8mVah51T9HxxZ0MNnobUdT_aO24_0lP691RWA1esPZ7rKCl3F8lRJaYG_jTdsNbTD2R2ii78_1FpAREROPb6ZhXn7tLCWa5iP4psYrL9WII58_04BM5cr4sAqZS-LKFqnattghyKUXJcdy7QV4QZl1N-oFoTW29VifXlzRA_4R5j3XiSN6VF48w5DsYzUuZtBwfTue-J5KycbkDsuCHEaYc7n8TxiOcKsOQ7QmxL5vLvms2Q4GPswclej6c_6q6NDKJ6N4eCUC0ZyFg6uZW-JsLT08dWWE0658LATtU0TFhMBs-9X5il6pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تریپیر مدافع فصل‌قبل تیم نیوکاسل با عقد قراردادی به ولورهمپتون پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/90407" target="_blank">📅 16:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90406">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ9vvmeIcOf1mD5N-tki_KtXfZSKaUZ4rkUwb-4TFhoZygjeB0EJmeGBZFnJCcFeVOIku0NNKF3dleIQzhNm7KdgaKpivYhB3hAo3JwAR7NmayJfR53Rnr4zrRbJa6Oupe87L_khpcV_ZbolUYBdwVXb359OqXzsjZ5O_s0hpEfP-2KQClDkC0M_ncVHo1fCw9QBeFKkH50eJFdkhL-oVy1jGzIeq6-uOKEnqyDEPYqyIejMUCM_ND6N72y5sluVpiMmjIZopz2cGzA0PgSwGyJ_gq6mTzJ5peD7FFlQcAmcirabvZs66jOMdv8i0uNvDjFaY6AvfrlWBhup6j3Hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مثلث‌های هجومی آرژانتین در ۶ دوره اخیر جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/90406" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90405">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usmMtdsnhEA8K7dh29mDRywEUFTmaR8_uvWGSmbyXiL8Cx9-gcida-J-E8SPrRjdjrbMNtlZvcp7nWW8-j9voBFvHk8Jx2uVgfGgmYBenXk8Ye528K4IKGQGTHHd857ZOjYwZeDfZqoisOfFa6qbKJc8ood2gPMoMMXYrhvumQiyrzGhPefs8ag8zix86KclapSdZnNvfnm9M0xYoiwLFQK8mSiyhPlH4J3ZDucRlfdK6cigtbIbNWVmWYbdIFt0-Bv3h_B7ehl8nZ3NcXNfGyfuEgIyuCnjJ1S2UzBEUArzEmmIswdj9BcXBwABb1kUSvAYNIJVceITL5Wylh0pfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↪️
🏀
سوفی رین، مدل OnlyFans، ادعا کرد که یک بازیکن بسکتبال NBA مبلغ هنگفتی را در ازای بکارت او پیشنهاد داده است.
🔍
اکنون کاربران در شبکه‌های اجتماعی تلاش می‌کنند هویت فردی که این پیشنهاد را داده پیدا کنند و تصاویر جنجالی این دختر به‌ سرعت در فضای مجازی در حال پخش شدن است.
1️⃣
داغ‌ترین عکس‌های سوفی رین در کانال ما!</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/Futball180TV/90405" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90404">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfxgu2NIP9ytYfcFk1lkX-ZpL_o7amC6RHx6pJNNgfiN6Pi8JE_QwFSiYX9P51dxEzMKB0686oXF56uFN2inE9XHYo9r-VVqwre55YihE9QMsZzZ2KIB6OWFPgDnwo5iFQL3mSm3Vhkd_8SJvjG2RtO0Vwt-dOx4xAEX993GttEOJzCq3o5p5u80Ucsc8ezOn2lJcXuvkE24zjpXz4risk-nShI7krYxjqEjX8o4HBFAc2bqya6E4sjai2LARaKPdudV9VGND0j8k7gVYXix96xMQ9mR9jBn_nyVqe094Xfr93ogIBnJRr3SJ-EmhZEuNEoj7rTTBVKR33E4TajBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شانس‌های اصلی کسب عنوان سوپر توپ‌طلا که قرار است در سال ۲۰۲۹ اهدا شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/Futball180TV/90404" target="_blank">📅 16:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90403">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=KuY09Sq7D1fqcpK2EcDoF_pYhvZ0xVyf0TjYkwTEWCtNZHitKyG1FCRSv5V6YAb8g37r5PjDuSthf6TljSk7i_qgCk0JDwRSUu5yQgNRk_QmAhyLrVLPMGBDK5YskQwipMFp9-3FCj8k3QSnsi2T19k6nhHwJmSLai5_1gsZhXq0WDSfCeOjzBairrWZLea15tgt5leXhYsvLI2oWs-AZ4kRlYJoyn8KzhThIVzmR03x2oLuk-6I3rNu1tf8Ht9NLgn0p3TkTKfOvl_PPhNb3Er4ZBdafYVyJZT9CWUOOYo63tKVsTuJlZqIGeEnis_5ISeOSOeXOH-0_RksccR-YrLpXyqGpd4qkXwyvLCV7xdtgLZfYJZ-dsesy9Qm-jIru4mwSBncn70P-r2TjpqSuuOUIKUUXBfJZb9Yd2rk7izE6s_ke3Ru7o9gNCxaTH15-5Oy3q-5ZKNUzsa_Kj4VA6bJ5FjR_uC4ieeTWtUsydqgYvZMQlQJjQ3Xe1L_efcnNegdLOQp9l-aOrKl7Zk0FadSnD_iImc4ZkNEAXj0274f8fv9lykFFxgrdTNaoO6fpNu8s-cgnMudKwCzEMVUJ15xC_ZnqgdCrNakwhZzFbBcJpRCSsuIcI1uT5FphxDJ5Z13iVVV6vseHwaPbnjghW_7_s5A3BEhYviwPls3QuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=KuY09Sq7D1fqcpK2EcDoF_pYhvZ0xVyf0TjYkwTEWCtNZHitKyG1FCRSv5V6YAb8g37r5PjDuSthf6TljSk7i_qgCk0JDwRSUu5yQgNRk_QmAhyLrVLPMGBDK5YskQwipMFp9-3FCj8k3QSnsi2T19k6nhHwJmSLai5_1gsZhXq0WDSfCeOjzBairrWZLea15tgt5leXhYsvLI2oWs-AZ4kRlYJoyn8KzhThIVzmR03x2oLuk-6I3rNu1tf8Ht9NLgn0p3TkTKfOvl_PPhNb3Er4ZBdafYVyJZT9CWUOOYo63tKVsTuJlZqIGeEnis_5ISeOSOeXOH-0_RksccR-YrLpXyqGpd4qkXwyvLCV7xdtgLZfYJZ-dsesy9Qm-jIru4mwSBncn70P-r2TjpqSuuOUIKUUXBfJZb9Yd2rk7izE6s_ke3Ru7o9gNCxaTH15-5Oy3q-5ZKNUzsa_Kj4VA6bJ5FjR_uC4ieeTWtUsydqgYvZMQlQJjQ3Xe1L_efcnNegdLOQp9l-aOrKl7Zk0FadSnD_iImc4ZkNEAXj0274f8fv9lykFFxgrdTNaoO6fpNu8s-cgnMudKwCzEMVUJ15xC_ZnqgdCrNakwhZzFbBcJpRCSsuIcI1uT5FphxDJ5Z13iVVV6vseHwaPbnjghW_7_s5A3BEhYviwPls3QuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روایتی عجیب از کمپ تیم‌ملی ایران در مکزیک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/90403" target="_blank">📅 16:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90402">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAfNhvIz2uv3jNOvHyqBzPuSWU90rtJIYIjWTwMM8JLgM70P7qLBdwSOfBPsMvx0JrlaHd4uTL2nM05QJbpsJ8R75cqNgPfKVbRAc4-6JN8l68HexapRYdVOFLqEdZ4qku2qjYkTtsIVKLBAYPUkhHuOXeRSdKuI7iYLrqWFQmkDSW1v3-wyZ8fsWNi7Z7QaJ-vvUvlIfmNpEEMFBXSIVrexVClSOfVM_w2D6HErceJgxL-LCtNO32yAqfvCxxc7TMr2Se76t-YG3ldYacmWZWiqpQQepT_0FQpNYCV6HIRq3QTppNU66J6x_9hplxjsAS65sf1DyS_fCB5UifzGrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی با بیشترین پاس‌گل در قرن بیست‌ویک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/90402" target="_blank">📅 15:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90401">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=Gm_HKPNlbQ-kGGitWdsog8yN10XrXEFqyDQSqRmfGQx1cnVQIZKfCzB8nnQn5kbKdrFnOYv5ghAU_EEPEfsafM7w9kbXLDieMutw5GTv7qmNsDIZeMWcLsK8ARhQH9F0BNrty6pocSVGWMcJxDyrD6pEawlElzbUuBLK1HxeWvNQD0AaGe-fz2plj5ICKHM7t1SVDhFqzTkg6TxFko-etnozADFqoMi5tBdc17qNUc45NnFrbMAAWkCAV7EHb-5Y8st9y2qmdgKoDZDGDO3FbfL7ol5R7-7fM3pDVXTdXAEweCqZFSl5ZfV0THPDQ0j2-FQCwi7pTPcZYUkNZT0afA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=Gm_HKPNlbQ-kGGitWdsog8yN10XrXEFqyDQSqRmfGQx1cnVQIZKfCzB8nnQn5kbKdrFnOYv5ghAU_EEPEfsafM7w9kbXLDieMutw5GTv7qmNsDIZeMWcLsK8ARhQH9F0BNrty6pocSVGWMcJxDyrD6pEawlElzbUuBLK1HxeWvNQD0AaGe-fz2plj5ICKHM7t1SVDhFqzTkg6TxFko-etnozADFqoMi5tBdc17qNUc45NnFrbMAAWkCAV7EHb-5Y8st9y2qmdgKoDZDGDO3FbfL7ol5R7-7fM3pDVXTdXAEweCqZFSl5ZfV0THPDQ0j2-FQCwi7pTPcZYUkNZT0afA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت لاپورتا رئیس بارسا در ساعات اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/90401" target="_blank">📅 15:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90400">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBbXqgwvtueeo3sCofWVfx0fMrg1YimEDr5_KveaOyzMgW5lBejRYanP0xq5nYeV1TGDiCGzY9wkdAxCA2Jyf648K5OgD5_hIO8qaKF8Rpc-NyQI4Q0I6mUdc6h8w9ELoJRkY817Pc04GPfAbLep7NV9Peo9kJW42MH1Bx4E84g3rP1MdHMCNrtFAjaMD171KyAlDbk6oH-RG2_I5AcB7OMbBAdt6N0ZS0HMu9IAW_rMPttl2-a70cURlOMAQof4o6wa9RS2RcUdfUsDqXnaE34oAiQbXrs776ghOC9wAs29mBovA99vweZ_uwwE2zrqaMOA215PQFPxDT6xRs7M2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
ترکیب احتمالی بارسلونا در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/Futball180TV/90400" target="_blank">📅 14:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90399">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=HuMmEq_98ZXoclSAkERc4xRyMTIIaz-kjdtwlPEwqqwfa-MGnFR7CMVqTmFC8Pugk7PT5dkFyRpHkBwTiqdWJTNDf1tJbYwgwy6Kvo066_hLfYW8_bpXj4s0UqY1jwEp4N_NRmiFjAjIl3TMewqIa0vguoehIFixItn-XOEeuAOLH7SG-Lso5bpuPVmiVxOimJc0-m95ZsFQlFrnwUfXrdIpa1MXplsG4PCT8hkDzKI0V-qLoXMxgGzvrIeLAUNkmi3dh3-TIkTpQUAPyUhtyR9DIht-iWoOdmTe3NGHQJiMakPlV_s8-Rvuu4giIqHUl3aC5IqfPI7WdHfJgyKQLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=HuMmEq_98ZXoclSAkERc4xRyMTIIaz-kjdtwlPEwqqwfa-MGnFR7CMVqTmFC8Pugk7PT5dkFyRpHkBwTiqdWJTNDf1tJbYwgwy6Kvo066_hLfYW8_bpXj4s0UqY1jwEp4N_NRmiFjAjIl3TMewqIa0vguoehIFixItn-XOEeuAOLH7SG-Lso5bpuPVmiVxOimJc0-m95ZsFQlFrnwUfXrdIpa1MXplsG4PCT8hkDzKI0V-qLoXMxgGzvrIeLAUNkmi3dh3-TIkTpQUAPyUhtyR9DIht-iWoOdmTe3NGHQJiMakPlV_s8-Rvuu4giIqHUl3aC5IqfPI7WdHfJgyKQLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
حضور کریس‌رونالدو با جت‌شخصی خودش در پرتغال برای حضور در تمرینات کشورش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/90399" target="_blank">📅 14:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90398">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vC3OUFnDLLUviANm_ImLOsZ6wnRfyj4ylggtCklAZ8V1tv-NqagwY_pyWzJm7u9PjclA26ugxMBa5JTMgdx4TedBUHh4d4IDfyrhssI1MFUNLj9eAFDLGLSLk7rLqWiy7uKG8DCwwEeeBji6_GboLXOOewdPg8xPfSGugdwqah2aMhtfjcL3nWh5dh4ywMCooldB-TR1oPepXvKDIa5dCexsJTbEzzjyv51x3JfOeqoPSBxh-CtBMc4079zaqFd3IWKTg3A4yeXRil5oKXSgRm4jwczEdVUmO2nbsp7JyaqjSZtQwFLhxqod8mDK7781StRTFoSXcxsSLmrLxRcOPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ نیکولا شیرا خبرنگار مشهور ورزشی ایتالیا اعلام کرد که قرارداد احتمالی خولیان آلوارز با بارسلونا تا سال 2031 خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90398" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90397">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcXQEHDx2ViB-uQF8SzSrMAfpgO1fh0wfx3WSssr5TcUzekpPF90X2xqS09z8o5ln8lT0xvpMLjMEMiHKzVQjibtEyLa8c4itejMQFCdueMx7A6sAyZStkFZjcBimcc38AP45cvaZm7dNkYOfzYBeCw9iRjCKzXysGj8szipfNvH4s2husx9iPm7mtYVzeYUnkhWu2w9hmX0IavDRB57z8Sz9DMEcf_qMvd0yhBcXVeD-LHAvtvFS4biJKGoF6CZwvHoUspjErx69hTbk5KGitPHrEcB66z5X0r13YMDKBajop50SahxqZbZrABsUiaM5GeeRbq2rtP9vaGHO8ewKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
به نقل از مارکا، ژوزه مورینیو اعلام کرده که با توجه به نقل‌وانتقالات پربار بارسلونا، رئال‌مادرید برای رقابت با تیم هانسی‌فلیک نیاز به جذب حداقل دو ستاره تراز اول جهانی دارد و برنده انتخابات رئال‌مادرید باید در این مسیر اقدامات لازم را انجام دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90397" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90396">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری از رومانو: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/90396" target="_blank">📅 13:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90395">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ-ltghjRD0Vu4umV3_oj7J9nL686-JIVtKF_MTz3CRZ-U_SzYS9bYDZGrsYFi4KKaJ5573s9WnqkCRFaUC0AzvNAwu7OU-MVFcp5-VvOPrrDGFg897kqavkAxB0rqjEpbzljg3ZtQtgvLwaMxdZxTViMim1lQnYJIwKfXvaz93RJHpWqomKv4SKJB3AOUPOi9Db9hq5Agw_e5Locn0umGuWrq9apPBOrYKQfsR5ERUzDtjxN0m9alETLp65QjbWXRSFXhgtv_dzdu_bIJptHeBJ76qc6WmlWYonRU_2d-amzQ1xcLEvah3lvVgIr1oyhtW_6FYibUH9q4HcWWS1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90395" target="_blank">📅 13:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90394">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAqknjRDFd4HzG3eRFmwPfeCEkPvYrVLg9jjAwuQME2exBSQzNFw7_tCjy1SSp58NuhR3N0n6cDqjnbn--3Tb7YTPOhfr0lEcXn74q_cFOgRb2-OiLH2726jJevyOcEy9iMVIIrv3iaDyCpn5xz1okc0XImI3Ray5q8A_puEUpK3c_caUOZ-rstu9EM9pnvYeKI7br8pOFeyqYem8fjcWLPuG6uZsaz7oLKiAAcPuVKH_W9a32dyDowtxlsnE9eYp0aCnLhlgteM5W9dD1WzVRPcqd8BqntEHbQI92xssj0BTjnR-l53gbEiLpXEdTIRo9W-ieS9JUaJLv5VeBvXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
؛ متئو مورتو خبرنگار اسپانیایی مدعی شد که اتلتیکومادرید به جذب تیجانی ریندرز هافبک سیتیزن‌ها علاقه‌مند است و قصد دارد بزودی با ارائه پیشنهادی این بازیکن را جذب کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90394" target="_blank">📅 13:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90393">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prgTJFe6aFXsaMqptbnixWLzTx1uWNXb0Uv2QoIeuKwGggnUWv5y5TvJw46hQxQJPH8gnMxlWwvt8j2b7e4jwGE4BWMPY6d6bxO_fHPbL0uZnXjtNABgyiIPMsDY2EPaAiWMXOh3ft1S2VnfwmY5si8oA1mVvIDFmFbh8UAgi6ym_SimUn9OKb4pEys5ZeeeWfeHxCKkSAr8NVMfDpRE1Jutg7hKbZiKEnKnbH-7BqpW6jEBelirlFat_8v8UlyXD_T5XjSAYeOhJklJwN2gy7Sd-hK4_wS8sysO24xMBu1OZ_tDk-9eu3oDTKpOBb1TrjSI-HOaEpGCRMx2c9f4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90393" target="_blank">📅 13:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90392">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEEZxaO-VoP1rXJ2U625byYIyx2ERsxl6FEK_RJ9hnWXpOGCVNEohDtWpynbp_v88u5MXYnY2tiipu8W8eZYwlB-iLxX0pobqkbr0rO0m0NdMqB_0kyN3KdUeKIRibqiD_3Xg2oNiwV02QDuRtNGJ80du5QZgr7eRiMzU1-ipxv3-PY-4YMJp1iKR1XooTHp7h2jfHrtGYavTwparfVjOek-P3tqahdq9jHph-df2qUlf1jy6vPA3dSazBG7_g-RNg2kJGmP5NSUfvHuWN-oVOK-bc34EUvRQ50vV5iL5t7DyyKwqnQsZ8ObzLqxKvEkH2kqXIu7RinBzCOKJV5MKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری
از رومانو
: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90392" target="_blank">📅 13:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90391">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg-WUNJRh_hKeBNM78c3dp9AoQAg6E401lOl9r7FvoRox2Lp9La72LYkyrKImPV7dfwqaHrmhxf7SFoeMo83isoub-3wDW06QDRD94-ZTBqzy07WizZuOZFvK3CSW0Q8FiAy65hfpMJduwjXFrX9fBxvxJM5e-Q9umnv0oE1wsDLW4RJ0r9iLbiVTyT59qNXTJdvXjeSFncrXro1Z1zZkb9JYYC5O7jQxgFFt_PfFGZphCdSBueQzvGUlimP4k3Z_uA4Prk7n5uNWMzxsqEsAO50Ilrg_qnczyoDOWrmY72sPRZ7fXjF6j0QgX-9tkIUSGZOZX02MLH9RgU2mKufTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
عمق‌اسکواد ترکیب آرژانتین در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90391" target="_blank">📅 13:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90390">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766445bcae.mp4?token=LvqD09aOp10k3SmsfRTMG8LbFPl6z4cSJXVLmCi4wIgAdUq6cyFcYmVn5WYh-ElhvCZ103rm89meNRhCeqQnQaTY8WG7PCyQ0Y6vFOLi9l4u65KU11qZ0j_OCmFyH48jycuhtrph7RtIaqp99JcF0YJfT5ceoVTm-8J6YBd29QIQ6Re8ZiKmxzGAoQYA84yZzNyusgnu1pwznK04MqkN-3JzJzRunTXdivMUoYEn7s0DBlM7lJaxMi1QIZ0v9C1KN8J2lOdacvzRgcEWuqAPEzEux1TzHfme4RM3DXVLpyzuNT5-ZM4ACkR2abcG_PSZzU_7M9nkFCM0Hz7IVftyKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766445bcae.mp4?token=LvqD09aOp10k3SmsfRTMG8LbFPl6z4cSJXVLmCi4wIgAdUq6cyFcYmVn5WYh-ElhvCZ103rm89meNRhCeqQnQaTY8WG7PCyQ0Y6vFOLi9l4u65KU11qZ0j_OCmFyH48jycuhtrph7RtIaqp99JcF0YJfT5ceoVTm-8J6YBd29QIQ6Re8ZiKmxzGAoQYA84yZzNyusgnu1pwznK04MqkN-3JzJzRunTXdivMUoYEn7s0DBlM7lJaxMi1QIZ0v9C1KN8J2lOdacvzRgcEWuqAPEzEux1TzHfme4RM3DXVLpyzuNT5-ZM4ACkR2abcG_PSZzU_7M9nkFCM0Hz7IVftyKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هایجک گوردون توسط بارسلونا به روایت دیگر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90390" target="_blank">📅 12:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90389">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEeItu8uWZmeAyBGoNivUyebK4b1AZxCVujePv3a0yl5Ody-GEnvFwvxLob40GoKVXv6F1DUrUWkVTuXMlx4mtgP05356zktrFlwT7UG534bfvE7FsbkQIjpYjdfK_VcsCsQbWLbPiBGelOnoTFnQNcpIVONaP-ZEFRP0WjGwCe-5iGKJkgBEzgV5vqI2Z0RWMLZkj0BiiIUnboca3UReaBcOv7LwaNdteUdeVirsLWHRizbkIeE4YaCHIIsb_ozXrnGKFQd75UJHtiKfDo522R5k3r18nRJHpk0XOJ7yyALPqPghlAsv5Nj2jGgqDk52vw2E6a1Et5Yq0PbKknnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ باشگاه بارسلونا پس از تکمیل قرارداد با آلوارز، بدنبال جذب یوشکو گواردیول ستاره خط دفاعی باشگاه منچسترسیتی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90389" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90388">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی…</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/Futball180TV/90388" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90387">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0iAL8u9Z0tj2zpYmpSONqKHCgUGd0BoocHwiR9X0jWUU5V9T3kr5Eq8zZZO-Y01tbXqt74Z7xPrDPe9A-qHlnjgczOf4eFbUZFRvHan-_GzDwHVAjWE2iVeGir59wU0wRrZrNMv8yeIcR4h8Wg1fSxYwSmTovoxIrEbrqzNYAMKyirUGf4XsKm-ymFku4W2E6i5ij6UEPz3aEscK5jLA4h9YzqFDGBnb8PWAHlL7UmVImqHoXarHLXBl219RQJco44OJGAtHgjBROzQmWFw-kOdm5hQZYEDVbEEqd3ttSxKn6t9XIx4fy7tl_dBHnyWe11rj3TO5DrhTdHbFolYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90387" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90385">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A80TyJC48T9BAgZY7ek3TjYK7l1D_Sdb21u88T1jG-844CigNGKXpriYG-RqWLpStCAxom_SHKOtTt8F--mDwPK57YUIaEvJUlUJSC1pGRa9-z6bpMyPDmKJDLlDjdhWmLov5mPC110cNUaCIBZq-GfQJ2CTmtjxxEm1XgScdyaI0JZr3xyi_2kYBfCZGWNNj7qU3Dsbb8F9BN1G3kiPkJbpy31QpBQXSyQ2scYVnhbg-R76fmdVNOnw5CGv-RYyjxqzVCtd1u9r6k-BtSQAd0t5bzuAe31BWVvKjE5xHZqIQwXlu96fkgU87MjM1N0McyrjI2Xy-39TFUHSDDbFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ رئال‌مادرید با ارائه پیشنهاد نجومی ۱۲۰ میلیون یورویی بدنبال جذب ژائو نوس از پاری‌سن‌ژرمن است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90385" target="_blank">📅 12:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90384">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkVoIB7qxpB_sfLFT3hpzhoYkfxVeM35d03xaSn61AL9vPTlsMduGiAlo3wPJrhIJhkZgpc-54r5HgYGm2MrHf48I_XeiVCCDOpReivWz0zlNDjMZJ9HMIgBrcbuFkRf6K3WlYzi09_d0WX5WtVz50DzvSWhp6sI7sckgA9YMiucV1lLGUY5scicOV2D4gjAQqfFdlenbA-RMv0QGtg5u0R-At0oVLA1e6MNypGLbsCGof0VW5V3UDY47mnRMemePVn8o9tcI6blWb0tkXiauYyLjpcVXP4mZqBqHAS9uNyXXV4xUdlvTJdGwaP1pX_h6vyqx09PAQmjMlAWmvtcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
لیست پاری‌سن‌ژرمن برای فینال UCL
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90384" target="_blank">📅 12:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90383">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=muHSykjo9U9rCLwUyPh9fyGVudnHo0DcwhXAb24NtL1CtOtXq8hV4IokfuVeE_1mtTHpezC5dG601mMmXAPkeFgHgovm1AOcFO2pO_cX6qNUnsfepQShayco19fPjDZCsQWk8PNNzxqEgX5AcX2GzDArKpI2lWDd18KJLmfc4rlSQS1CXST27oA3IGFmfaJExYkNxEE8ssNVuiaoSM4OahYSzW7sNGSg-qRYwYJzr5OtnAHPp6lHurXfLjCLkAXC-iz2SC6HjcK5kI6GFL8_qpLI7u1YshKSnG84AAuKnDWrQ4GGxmPFOp8qhu94do4FXhdhfOG3Aweo25LNFGUmpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=muHSykjo9U9rCLwUyPh9fyGVudnHo0DcwhXAb24NtL1CtOtXq8hV4IokfuVeE_1mtTHpezC5dG601mMmXAPkeFgHgovm1AOcFO2pO_cX6qNUnsfepQShayco19fPjDZCsQWk8PNNzxqEgX5AcX2GzDArKpI2lWDd18KJLmfc4rlSQS1CXST27oA3IGFmfaJExYkNxEE8ssNVuiaoSM4OahYSzW7sNGSg-qRYwYJzr5OtnAHPp6lHurXfLjCLkAXC-iz2SC6HjcK5kI6GFL8_qpLI7u1YshKSnG84AAuKnDWrQ4GGxmPFOp8qhu94do4FXhdhfOG3Aweo25LNFGUmpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره مشترک رهبری‌فرد و شاهرودی برای رفتن به کنسرت ابی: پرده‌ها را گره زدیم و از پنجره...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90383" target="_blank">📅 11:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90382">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYobmNA-d1SQM_WcSXjlpiiM79Nb6UBhkfSTOT1eU0SiIS3vegn8ZsVAnpy2bgXIiaisDHi1AF2m5cThlQAdB0TvslWTpoNHx-W6eCUbENW1xvx_jHeIAX_CJGQesa-wevQ5me6WrpB6kPVx4I_NQy6VS_7PmYLrHfeXJLY8VND7QygwankjEyYMBdvRBkwlzTS7mxuNEEXrIyRmaWSyJZ-_HxPxLh1cWHlXGz890i_GvNtJIGi1-eq_gIQemNxm0irQivsHyOxaAApchz2MTeT1au4kiaPWw7enMu5vVcte1FKAe_9H0sNxoB1GlYpo0PudCngbhp4IkdLoQbX3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ اسکای‌اسپورت در خبری اعلام کرد که ابراهیم‌کوناته ستاره فرانسوی لیورپول در آستانه خروج از این باشگاه قرار گرفته است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90382" target="_blank">📅 11:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90381">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nxEJSDFNnm1eX79lfbEYHj-vJC_wAFTCy8KGwm1TpsaqYQcBlGhorRHYLPNqYNgmDbxbi8pR1AKskOw-FqwIDBHk-R8SZLAMT-qJxqIPxERsLYWvNgHFBbY48rqKFqztYym4xeSGytN3w09r29z6YE6jLSbHIvUdeJh5wsR09vvchVmWfLlrOFckI72LIVVvAVhF3qhfHunx4fpSqWkmOWLStFS8ZrxuLqocMlxyD0CUtK6qmD2-FgjrVWr5dFtLmhm2n-_oCIlN5xs-QiqEavV3XQ-hr7jyn7ghsNAFgwTkm4CBw0ba--8HcYIX4lKaJjvBHBnsxvKjMPFV1BBXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#فوری
؛ باشگاه الاتحاد عربستان درحال مذاکرات فشرده با یورگن‌کلوپ است. این سرمربی اعلام کرده که در ۶ بازی اول فصل جدید، دستیارانش هدایت تیم را برعهده خواهند داشت و سپس وی به نیمکت اضافه خواهد شد. درحال‌حاضر منابع عربستانی از بررسی درخواست کلوپ توسط مدیریت الاتحاد خبر می‌دهند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90381" target="_blank">📅 11:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90380">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwNY8CvSO1wXuTOS8HeGorOCD8_8u3QejjUGddJPHtuAsUgMFG6CxgxEccj_3YZUrDJQs-4UJuNRe0Rk0wi91QQXtnH04GP2YGSR6ILXx0KyqS7ff1lnQLrdMcMEx1qZCM_wcy1nvciEQpSVt3hz2LakXYFhjEGK7041rqpKQ8fR8RItu0hO7HTjo3lYadlLuVHvhoenKXhC1ZPa7wZrrAmPYuwM2Hz-L8ZoB8fnLnf-hGFvjvvIaYsW_tumsB4fBbRE2A59Ps1hirIS86loaVwz0XoKghu2JnwJkRKVdR1-JswbI-FsX8lSZGYMVTl22nB9rg7iFjvE33IgZQ3x0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
استوری ژائو پدرو ستاره برزیلی چلسی؛ شایعاتی پیرامون خط خوردن نیمار از فهرست این کشور و حضور این بازیکن در جام‌جهانی در ساعات اخیر منتشر شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90380" target="_blank">📅 11:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90379">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No2r1SQiaOklOOjIdDKLh1xsto4zKqmktJ37JEAIHmuhC8keUoDsg5lnAIonm13bHh_cep8-vBD74hCbbUp8kk6S3c2QN-Yk6bqnCXAACthQbcGv-A5S6Zmqmrnv_XUoPE9Q6d3R6R11OoAvMiB20jsdaxBgy3k6cbGskRamJc9CVqTrWxch1wjQG2NcE0mOATQJg2b6fo--FXf-0uWebmbe1wsElLzSuxIQPbs3JBDvRJm3ROBDSGG_qBHX2VBo4FKCFCgtZQMwLmZHiXNuwMqqN5eTd0qjj_oWZ7jFch4l21oNawOObR1wU_njr89mo3wetC_x6iFHvfq9Wz6IsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🏆
ترکیب احتمالی پرتغال در جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90379" target="_blank">📅 11:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90378">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=VERrc734KlIN_sBoZaD_krzD6hAz0T1NcKiAACdN48o-4t5rnFn2grXW5jeg7Z0imH2MqdQo6RIxxGXY5swQo-XaeuEywG8ti6QKP5khc7tzkmTCX0z8icth60DtFtFxct9A5W_lHzNk19hKEQ3-2KwFyu4g8r56w58Cbplu2CjeGHfNohghUccTowF6PnY6WZAI4ko35ZYdIJwxSrcHSIaAvAOc3OI_adhp4O9dluyW7Og_S1jocGC5E7smbK24ZuUE3LdHdc-QIxgqrKbwszzb4od3bTnHneB5jvXX7JSlnsK75C8HaKcLOuhIBgPy3ndnfft2VCvjw90isngiB3U2HAhfpRfyXWEDWtcJDKCkcCfKZrfyigdlCc48Zhr-PM919NSfKC8T8PO5-y20x4GB8TR7D49ZaYco0cR0ZV8YaEGOk90g3ecx8UpRSqnuVR2xvuFQZq96mUqhmkvj7pw4p3tPcbL3mF-52XCDqju7msSmzLMzWGNWQA0Dal3xhDfW89IZZV5dbgyLGKKumvScuAKbIau7QOgX_5N1MNJ9YOkKk51HibCcUe5iYB34FESQRdrN3yg3oXzbXwDt6GBrXIv0X8PtJNtOYWCyQggWA1WoUAuK74XH32Bi4URmlY4PU81FgwllXjsBB5r1is7rY2KJLu9YkWxuz70ml3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=VERrc734KlIN_sBoZaD_krzD6hAz0T1NcKiAACdN48o-4t5rnFn2grXW5jeg7Z0imH2MqdQo6RIxxGXY5swQo-XaeuEywG8ti6QKP5khc7tzkmTCX0z8icth60DtFtFxct9A5W_lHzNk19hKEQ3-2KwFyu4g8r56w58Cbplu2CjeGHfNohghUccTowF6PnY6WZAI4ko35ZYdIJwxSrcHSIaAvAOc3OI_adhp4O9dluyW7Og_S1jocGC5E7smbK24ZuUE3LdHdc-QIxgqrKbwszzb4od3bTnHneB5jvXX7JSlnsK75C8HaKcLOuhIBgPy3ndnfft2VCvjw90isngiB3U2HAhfpRfyXWEDWtcJDKCkcCfKZrfyigdlCc48Zhr-PM919NSfKC8T8PO5-y20x4GB8TR7D49ZaYco0cR0ZV8YaEGOk90g3ecx8UpRSqnuVR2xvuFQZq96mUqhmkvj7pw4p3tPcbL3mF-52XCDqju7msSmzLMzWGNWQA0Dal3xhDfW89IZZV5dbgyLGKKumvScuAKbIau7QOgX_5N1MNJ9YOkKk51HibCcUe5iYB34FESQRdrN3yg3oXzbXwDt6GBrXIv0X8PtJNtOYWCyQggWA1WoUAuK74XH32Bi4URmlY4PU81FgwllXjsBB5r1is7rY2KJLu9YkWxuz70ml3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🏆
هواداران پرتغال در انتظار جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90378" target="_blank">📅 10:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90377">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=nJb3eEqURVHlpllVNsp8K4XMMGJIlp2OrJKX5rSRNAniQu0r53oU1PGmRwFmwWdyUXVAuVRT02tj8YcDh3ytYPnW_UhZJ6lGPD_JudNzlSoE491-4HtitipQZ44VbIjmLrVizv6_Z6AQGfyQfjs5WXn6M2WQtyC3zIwPpjg1KlN2h7df90DL_zO4kz_QbnR_UojfA7GMxciENTQJi9xlzIV-kMPInfFiVUA11__yBVA7TioH_WvKTmrgSvgXvBicbc-MUGSgnnAf3BdjUP4njlaRTW_A3nlXcwsyPWLx1J9VYG-_eXl1yGxP4Frru9yb9wVbupvvykYb64zcee3p2qb0ggJ_1rgbqGnx2JEBsdM7LGGjONVDhd4LdyZosYu5HINIHdHiDKy3SXD55u0TWg8DHiuSzAUx-4VNP8mK3Rnxr1MtjFid_lpdEoDqRtu57NA2Ux7hDlovRxUVbhFBMih-CZOC2NbopCJgKjuQRd2Di7bt0xh3YKV5Axra6jj7lI24lYwwU9B7L0oiYgXSByRY12vRkK1ixIR7vxjiJs5NoE8hiJQ1WNWAxXkQt2ZBto-cePCFTDQFPfUoIvTbego8_P16OsALcDpQgKF-C3dNvZ9rHRqYPiGgfo1fUOHJrHeqMoT6za8sjMZhDL90JoBG1QXN65GoNod8RaPqhxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=nJb3eEqURVHlpllVNsp8K4XMMGJIlp2OrJKX5rSRNAniQu0r53oU1PGmRwFmwWdyUXVAuVRT02tj8YcDh3ytYPnW_UhZJ6lGPD_JudNzlSoE491-4HtitipQZ44VbIjmLrVizv6_Z6AQGfyQfjs5WXn6M2WQtyC3zIwPpjg1KlN2h7df90DL_zO4kz_QbnR_UojfA7GMxciENTQJi9xlzIV-kMPInfFiVUA11__yBVA7TioH_WvKTmrgSvgXvBicbc-MUGSgnnAf3BdjUP4njlaRTW_A3nlXcwsyPWLx1J9VYG-_eXl1yGxP4Frru9yb9wVbupvvykYb64zcee3p2qb0ggJ_1rgbqGnx2JEBsdM7LGGjONVDhd4LdyZosYu5HINIHdHiDKy3SXD55u0TWg8DHiuSzAUx-4VNP8mK3Rnxr1MtjFid_lpdEoDqRtu57NA2Ux7hDlovRxUVbhFBMih-CZOC2NbopCJgKjuQRd2Di7bt0xh3YKV5Axra6jj7lI24lYwwU9B7L0oiYgXSByRY12vRkK1ixIR7vxjiJs5NoE8hiJQ1WNWAxXkQt2ZBto-cePCFTDQFPfUoIvTbego8_P16OsALcDpQgKF-C3dNvZ9rHRqYPiGgfo1fUOHJrHeqMoT6za8sjMZhDL90JoBG1QXN65GoNod8RaPqhxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌موزیک رسمی جام‌جهانی دوره‌‌های اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90377" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90376">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azelUYSgPxyorT4Gy2pAJZW0YCZmz6MGMlmYHDoD8veROn8Gw3bKYHF7y6RdRhb9xIFkaHJDQJj7LGIJK0DCDlWcHg7tLWBI1CoEEGT65jsUAteygnN-vTp2O8O4ft97beNTpjQeAyDv6pG4CJ8eLUiNJMmNfUybzLMlqItl18vf8WjiYSE7JyYHlNJ1PfXbx90DL_LDPUswa49W_Xn2tJMmCZBxRAJV75JaSVTCQT9LJfhPO0wzu8HtfES1fZIlaD77giOhCmvlf9DpqoTtwHMuiFssRl_XnfLj78PtZzBmwm3199ZfevkaJc7WJdb2aF2ZWKEGtWMfBHYXfOXXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جدید یوفا از جانمایی ۴۳ دوربین پوشش دهنده فینال لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90376" target="_blank">📅 10:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90375">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrinYqgWIBnliSLryVrT36UevfvJWUyNY2Wpdb52o_pJwffGrCLE0qAsOT25sBnHgDbNL0ygvi8xTvSnDserO9R0nnRpwazYCTesnfov6fH3yz_ctcqBcNVnST49NdFlszYo0OUv6CApx0SYHl2CtuehZ4pxPxpOYDwQCFZCauJEumNCvsEAWwvT48bOYa3uFB989UIv9lxKVJvNOM5H-YLd3ne6uWIdYeFwndgub0Hab_nOZvSTsNDBYrZpUbwG3Lg7MJ9PVIhjx9usNzoi_BdMBvP3zxYphZSuaHAmyoG5JhRoybuZGcQkDEHCFSBF-gDSeZUxsTtRa0vSxDBfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ترکیب رویایی رئال‌مادرید که البته بیش از حد رویایی هست و احتمالا محقق نمیشه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90375" target="_blank">📅 09:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90374">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏆
کار گرافیکی فوق‌العاده زیبا از قهرمانان جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90374" target="_blank">📅 09:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90373">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac09312735.mp4?token=gkGO3Jm6wRaEzZ0lxVrO7A588s0LjtkfE7Y-Elswj-fuFh3QRjrcisUr5EMZV5QNYQzbXd-A1bcCvRVnk54-G4LjekDKNxMImLKonZKTW6LqFherdK8GBk5CVX0lx1w33U8uJrpkMQEs02_WpJvNViRGZlcGYZRDr9KRLUkINqVyRqa_FkcuuRoUA2J3MgTxpqOuyEoSlVtbccWRBNru3R4XcxKqm0EThxF9B--O6ugDzc8HsMMbVhHx965b32f29To8NqlLwvO6cjwSEWig_HAPBw7-IpU6tNC6iKNyQuYmtn-QVeeeoaMC_JMzzkZId3okz-xOtpIKidtTibvf2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac09312735.mp4?token=gkGO3Jm6wRaEzZ0lxVrO7A588s0LjtkfE7Y-Elswj-fuFh3QRjrcisUr5EMZV5QNYQzbXd-A1bcCvRVnk54-G4LjekDKNxMImLKonZKTW6LqFherdK8GBk5CVX0lx1w33U8uJrpkMQEs02_WpJvNViRGZlcGYZRDr9KRLUkINqVyRqa_FkcuuRoUA2J3MgTxpqOuyEoSlVtbccWRBNru3R4XcxKqm0EThxF9B--O6ugDzc8HsMMbVhHx965b32f29To8NqlLwvO6cjwSEWig_HAPBw7-IpU6tNC6iKNyQuYmtn-QVeeeoaMC_JMzzkZId3okz-xOtpIKidtTibvf2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سانسور نام علی دایی در سریال صداوسیما
صدا می‌گوید «مهدی طارمی» لب‌خوانی می‌گوید: «علی‌ دایی»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90373" target="_blank">📅 08:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90372">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5yLnlL0mRswyfG3z4m9j4A0vO7G_8nr-nDJFuVpsyYgTIswupvwiYAOLXSIJHvMEXO6jG4xl4hAVbm5BoKIEH-3ozpAg9S2T55QIyb-aAz0LlJaW5V0dWM6PLemDYasdM1HF-lwjw3ssBuh0Tss0NNRx_LI965CwAmoVMVec53kAaQehj2CceMibgc61axwaD1a3dn7AjHKxSaunxG1uahdQRlS-oeDumHcdYbG-pd6ldyUs6hGgc6iZIHZeOsZV63-AoENN6EB-zklc6EFRg8oupNfeI2XuVNhvcpBK7I-yqiPt0PbRaRE6yfkNI1aS8qAO2hkAndskCCRKlQjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
لیست آرژانتین برای جام جهانی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90372" target="_blank">📅 08:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90371">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90371" target="_blank">📅 00:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90370">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqSEs813_zqYzfDky4bWUnAN6y5eiC03tFnVvY3tCur6_U9hOeXg3N4oetielmDtNmnmqCs34NFNo0DNLYHvIXyP8iZzQ1IX-wf0Gm15ifcZ_00aGn7GwULZdxYq86YgXt5MdG9Vh8qXvlwL5X5yIMR6L2QXOizB-Rg7tN8PBQb9foUUrmPuSCXhUzq17XGalQwFECJgadmo5fc2fzntfQmPKYeyD89DxhcdyN3TdMFcRrLfBrEM5gEgcFWlBuTjtidemZC5HM_uODaCo8HaKLbhyaczLo6as-1_tXf3qaJKcBuCWVnDlsc_6nvVPgEkic2SZP9iRJ7ai9ltmp8OCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a7
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90370" target="_blank">📅 00:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90369">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVMXtTY6lEVI2R_q8X-I1TsS-qxqRxhdj-7eVjDyWm-s-ptErOtljDg9ZDJzgUaq4GTULa8Xr9HmLewk3o5GZ7e0j2vnp7GsVIOqjZiO_Y1sN3jGB6Mx57mJZGcoQtMlzD2DQ61kQPu0wjUJyEiAtSUVdWuQlvDgHCIwAL0a_irUuyUN60RSmOOc9oAKIPKMLra3Wy3aYfSjuEhGaFY8gaJ7RS6QhGi0Asvc9qpPfMtHd-tn-iuNSj34xphliathKAUv0svt-6Dyrf28dHnibLYJLYYhdmFUMFwR7dSwOEllPBXB69VG3_Y9EK7U20o2qpPrthAMkQIxudPwbN6CTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل بعد بارسا:
😳
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90369" target="_blank">📅 00:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90368">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=jv4kn0OZaYE8d24TYndKXDKZUgyVdUisin9zIFM8TS9bFc24gsdC7BYc0wmXqzF-vTUgJWA607y9mauA1LBkR6K_eWj9gOM5yrJPwiGA4-pFqZIAIOBd0muYTVDif0O4nqoVH_pzie7zbslIl77hS0Z_KVIkAFiQymXYDspypROD5wa3g_YsLBvd_KsdeMDYWTHQw6hQQ1SPRSBgJFaZ-tqvFk1WCWmF77kkFmcAt_KMslph25JBgplWwsi_1a_81fzZWiozOJzCqQPFc4HNRM3znyBZQNTMBWD4whC_yo2iGTJXl59GsCvuoEZVajfwsnLgnpvhG2LUbqnrDzKvdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=jv4kn0OZaYE8d24TYndKXDKZUgyVdUisin9zIFM8TS9bFc24gsdC7BYc0wmXqzF-vTUgJWA607y9mauA1LBkR6K_eWj9gOM5yrJPwiGA4-pFqZIAIOBd0muYTVDif0O4nqoVH_pzie7zbslIl77hS0Z_KVIkAFiQymXYDspypROD5wa3g_YsLBvd_KsdeMDYWTHQw6hQQ1SPRSBgJFaZ-tqvFk1WCWmF77kkFmcAt_KMslph25JBgplWwsi_1a_81fzZWiozOJzCqQPFc4HNRM3znyBZQNTMBWD4whC_yo2iGTJXl59GsCvuoEZVajfwsnLgnpvhG2LUbqnrDzKvdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
سفیر فرانسه در ایران:
علاقه‌مند هستم همکاری‌ها و تعاملات ورزشی گسترده‌ای با باشگاه استقلال شکل بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90368" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90367">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=v5vffCFIQooZMh8-tMFg7A3gpWhEs5wAHTcGTtjcLK4bKcLwFBNyXpcl7aXpnRxil3mw0Vpi9kBEZL-buzV_5Pga_fLn_qE50lHMVTqmHaAjY_9-422V8x7DEoyw9EyYq7fiFpU9Ox0FLazdvyfOfdqHbM7J3yGrtg-gZWRjb-h5OqC6l0AHnoPpApLVwHcWNeQBfBnalePWi7KvtYarE4J3VzeBOzLSHeIQGznhTzkZG2dzgKJEie-IMqyWgvip2gr4oXe-YMHUFtZC4ZrEuriwVM-NOsyRaoUINZ0tE8XHmfmJ1dzSiLkedjgOzDaeN6_wT3KbjLHd1-QXwoQD1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=v5vffCFIQooZMh8-tMFg7A3gpWhEs5wAHTcGTtjcLK4bKcLwFBNyXpcl7aXpnRxil3mw0Vpi9kBEZL-buzV_5Pga_fLn_qE50lHMVTqmHaAjY_9-422V8x7DEoyw9EyYq7fiFpU9Ox0FLazdvyfOfdqHbM7J3yGrtg-gZWRjb-h5OqC6l0AHnoPpApLVwHcWNeQBfBnalePWi7KvtYarE4J3VzeBOzLSHeIQGznhTzkZG2dzgKJEie-IMqyWgvip2gr4oXe-YMHUFtZC4ZrEuriwVM-NOsyRaoUINZ0tE8XHmfmJ1dzSiLkedjgOzDaeN6_wT3KbjLHd1-QXwoQD1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
رسمی؛ با اعلام باشگاه النصر ژرژ ژسوس از این تیم جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90367" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90366">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پاسخ اتلتیکو مادرید به بارسلونا در مورد جولیان آلوارز:
خولیان آلوارز فروشی نیست و باشگاه هیچ پیشنهادی برای این بازیکن دریافت نکرد و جلسه ای برگزار نشد و از ماه های طولانی دروغ، نیمه حقیقت و داستان های ساختگی مانند خرید خانه ادعایی در بارسلونا خسته شده ایم. این رفتار یک تیم کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90366" target="_blank">📅 22:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90365">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoB1vtRtMWnhbIZ862nJYviPu2aTM261AJ0HKQ0Qfqis5XQb_QZ2aVxq33sdHH1PVgSobyf9bNU62JEkGEWcwF1JmmtAHRDU8bkfV97QtjiR6hGedi7SL06VZBz6jA2nEtLuvcrSlAssBj5nf6dMoq1oqrOb8aAeo8-djhkSBsQS5NOu_xjXZvRHNFJKNBrSIgL7JvLIvtRUQxNc_0IEznZzpb65NBMb252i5hTUG_DVjmQCW_xR725baEIgpQQ_OLj6tTF5CF_hvNplzLocIS-c_N4dsjLGNts4lPto4iGqlIvBQMQbiGmOY8STxfmxw3tp_dd80Q6LM1BrgXj6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییی از سیمون جونز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
:
•
💬
بارسلونا در حال بررسی احتمال به خدمت گرفتن پیرو هینکاپیه مدافع آرسنال است!!
•
💬
اما روند کار دشواری است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90365" target="_blank">📅 21:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90364">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvyf7TFofw8HugI6-UfgEbNvDlR5mPbr3TDAioti4nONZiF4bgmn1bo6uQzyIUSBvO44YcXVpzLU3wxOI5dvMozSdXXnxXFJbhLjIy1dkcz2XnP3llJTVILlXz9nTHTkRA9p41dTf9pZTA2unIuZX6qVHb-y_eE8NfcnnoRqOVGTBgzl8hwHoUul9QKwy5Fk2S1LBAvI9_X3UvNA340QQdxuxz_KxZHA-U3_Qhby0PSLG4FB-CKQ5JvkxXhWUBOGH0Zf8WRYQrBpPkS8NWK5r1Mcao6u2ROUf841eIXDLUkwGps64mg_O8eBAUAf77B3nrpwCMatdxcCcQ67n0ekvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90364" target="_blank">📅 21:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL9_rRLY35J7bWeadPLvXvrEiKi4ackWMIAWM5TV9K9XGBl78_NZrbphFFQUQPLM5LvjBKIS1bhG5JWyCbwxBpMKeDYTV7Noyg4keX3qHcCjcevLnyrCZzYo3s00GqiV2yrZMwu4CBdlTw0Rh7BEZWgOJk0-t9nklmokRACDsjpscF2tZcYdQ70lXp0xm1evTa2zgtgG4EA7X5InlSoQhBtJA5oN0IPPsdTOVqGL1bCkKVjMRkW7TRwnIk628ymMaIu26nWV3FiBnBdQu_XvT0pJyO67CEhO8txXZGtfa4orGhanWHv3mwe7471XUJ9uqfBdZuCEywCvkkqzb_5q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیکولو شیرا :
قرارداد برناردو سیلوا با بارسلونا تا سال ۲۰۲۸ خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90363" target="_blank">📅 21:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90362">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyPl_8Bz1LEh-77SBTIG0quZ-jgCKmDeK9nRr2hjKF2ris54bljG_AiMyh39weyEvYYfu80yvOjO5XL5UTpge5VZQdtfKfqSQTNQosPu-vNUI_U8vARPI9JcJVE5WPVYsIOu0xYugmqaSY2u07XBMEp7Otcr80JRBlyYYpfkllBqJi7cyD74vU4fMdFWrGSmEQtn7GswfTPvuHYfkkbbWEkC9TZk-I2hpnnctheYaywgmdFgAB2ERZm91ZzM6XQR9gdVgaC3WRauLa3nDkkO5RiEGuZcSkpGnQDgMYT7F8anmOQlRe8BK9c6XZvmIbJjSQaoDe51sAxidfnFABmj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم بسکتبال استقلال در بازی برگشت فینال انتخابی آسیا موفق شد در یک بازی جذاب پالایش نفت رو شکست بده و به عنوان تیم اول این تورنمنت شناخته و راهی آسیا شود.
استقلال 93-78 پالایش نفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90362" target="_blank">📅 20:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90361">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clWIXVnsuBY29GLQYjGew8tQ2a49osEdcxEaE0ww6ST0n9thXeEZxa4QkBwiFQdxpYQ2DCsCjWcnEjnqIl_Gb6_3v8uEx8vaTNNR0TXRIn15N0mJL69Hrqj4_T4f-ffWw946pYkej627CYMXa0hmfJytvH2qSvb2fXnKJ97ocnllU6hJKs8y6ibl1kwULnGp1Zr46AmP8RqPKGwFmZvUAB1aIZfr70N6DK93C84fVuMzZdlRmgYdkEOgFyOYhQkwwZgYWMBnFjM96_VV2Yvak9vjV-k3kFp45bN3rGCSH1s7bG31D0NteG_mSzndGF8md9nAdPcWCh8AvK2z3eNiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو : آلگری به ناپولی
HERE WE GO
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90361" target="_blank">📅 20:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90360">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">معاون وزیر ارتباطات و مدیرعامل شرکت ارتباطات زیرساخت:
بهبود کیفیت سرویس‌ها و بازگشت ترافیک بین‌الملل به دلیل طولانی شدن قطعی‌ها چند روزی زمان‌ می برد، در شکل روند افزایشی ترافیک بین‌الملل قابل مشاهده است، کمی صبور باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90360" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90359">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-qW77vMoCxAhdEaECEyD0gxMdYhLZ91ZcnaDlahDxUE6MzZrk_RQ1UhHgRblhAUTs3wifyNsUOCtUjsj1dcOp1mCoeuIpte9sa1HuXgsEXwFusMX05ayAhJHLjnHbmSo60qcuaXzzh_TtdXs7o1tLNon-s-fVp60ERVulvk7NiGhArYM1gqi3hOmWdg5fhr_U3B38zZiMN_n8LxBm8m_eTo02bpN-crpqYdrVUVkm1JOu4jq9dWUfT9DAMeKdo66HMJsJpZNsZpWvpOedEevKYm8PDVWtJqWVt6FQqAJgRiYvqPKf8BudHsD0cmyPPjbCZWoFukaFZ_XfgOzh1idg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو:
تا این لحظه وضعیت مارکوس رشفورد هنوز مشخص نیست؛ خودش هم دقیق نمی‌دونه تکلیفش چیه و منتظر تصمیم بارسلونا تو روزهای آینده می‌مونه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90359" target="_blank">📅 19:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90358">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">💯
اگر هنوز ۵۰۰ هزارتومان رو  نگرفتی همین الان عضو شو‌ و جایزتو بگیر
نیازی هم به واریز نیست
👍
تنها سایت مورد
#تایید
ما  با بونوس های واقعی
🌐
Winro.io</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90358" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90357">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIjkpWoT0EHE8a0Qh8ZLQaME4zu1V83qSQVKv1-luRAUuVvgDoxujJkPBqA_-BLMFpk8F8MlLMFst_qN9gZO2ZduGcIAwzj_t8llpvxXMaBPZtmgNIP7ZrPYEIeBFaNrV5mtYMSap-NdbPm3fi3nbTW4BFrrJXv7TvrtofKXm0HoUcnNK6ep4peTnP4RV2rSuHFpcRt9xr6G56ayLOmWjFziDmX00SYUIuoXvLlcyzdRsKMqA9_x8jOtKQuevM2gy84nxuoXE5QhyQwHaaI_EEa3qezwqRAq7MegnUCv-ypxxMpJCwsTFVB3czje-FqdZyxwLF73rfBl2dWo_5LMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90357" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90356">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICZgNMmpsWzI77q_vKxpOh2WD3ilRL6VziqTOzy1dbzerwM71ogAnqa7aA1d16fi0QsMR8-jlCxcCGSoTe88KM1umFdk2nNXXXoalCE3cP3ifUwMdgFe4HtY0_l_sXDL3gOeC8CEl7nHF1uLs0_PmLUBMCCI6OLsNykuaejk1F6oHLZcD7HAPUU8XqfKAISrCobh7PCd8ZwjEX6l3CLTkC1ocuqzg2aJIOZM6Ebdm4Z7Qxc9Frv8d7dXb0SDgNwka0661YpKRgFbrJbOkK4W7VFsntlvhAYMX6usZ9pNA9qw-WEdzGyS6YDyw57hzHXGtoXqHVVv8K2-InVMo4Mkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
کیت‌های ایران و هم‌گروه‌هایش در جام‌جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90356" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90353">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDu7IqJ6zCHklPUhi1O2rhqhJIa0nED7YrzlVySBM5wIBRfAKkx6y_nyfTii7WRIyTLvZF7np3cKfk9rjc6EDv5boAyCqc89dzIvcTYEOS4IRor7-7eu_p9bxdVje6-1ACdVjejTXQxVOoEBggCmS_YeZ8Dlxt0QmDUYAYU-24l0A4sfnDA6B537Mm51WhKZFWwjQwbj7wrHDwMeVSN26AZzf4WSnrSbeRqdXv1g-_JSkv_jiVSL80bBRKuNG4BVVzKqMtZCncOMdpxRpzNcZ-KRXjpeBNA0-sXAr2MTjgwObOx3ksw79XDmyol_3z-yooWetKWLXZivvTjlafZf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو :
تعجب نمی‌کنم اگر بارسلونا بعد از جولیان آلوارز و آنتونی گوردون هم باز در بازار نقل‌وانتقالات فعال باشد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90353" target="_blank">📅 18:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90352">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیمار سه هفته به دلیل مصدویت غایب خواهد بود
!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90352" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90351">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iqslk-82GTY8hOhm_U0R5CAX75alR9DjpDZBp99f_b-m1RtvCRIWHIqOVj7UXgZeBg4407moaYKZDo4AGewG2AloU8BLqbvGRfYI9gWKzYRZ-CL1LzD8FrvXwGFr6p4rQGYhnzo-SHoTufWydHG8cKvFVM-OUgQ5mFdq37C9ZvSOTywnExwN4xDitCvR3nQJq-Ah2B1Cw0d6CqkMK-otbABk5apW9WGx0AdKRukPKqIKDzpVyc2NCxwwohI7VuwUdhswFh1L5yyIipke3vYcz9ITbDOd23Esd9NAm8D2UVyqe0nU0KwO__HbD6WzMpIOZ4rSfHEOO9Y35pBgJ2LsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتلتیکومادرید به بارسلونا اعلام کرده که هیچ رقمی کمتر از ۱۵۰ میلیون یورو برای فروش آلوارز قبول نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90351" target="_blank">📅 17:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90350">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-cWc-WnRloXRMiTVH0_YPY2tyDirSf_b9IvKoxDK6BLCIACwwKtVyBW1wg4SLJwdPaDHh1hOssTZZPr7uyzmg6U9b7CBc5k4SyDnvfWbcafg0t94mYU3H4ISMCwXsXVKQN2oOHDoJTRy1RRWl1rZQU9PD-558PK-qBZ2GjTm9KvJiPYnW55Vg3qWl5MzSIQDaO98dtHUxIEfVrpfgOBUOgEpXRZnfy6d7FJnGrR4QUmKq-78oWKTxEugg_YOHHf316_YE4ocZmUod6C2dshjvuAB-0EY0XqQUV8U3AEhF-qmLfr-0i4Zuz-6pZk5BwZFlK-XhaYfhogxt-rGZAnAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور گوردون ستاره جدید بارسلونا برای عقد قرارداد و انجام تست‌های پزشکی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90350" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90349">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5UejRyyWqULficXQTG7VdQuX26GsjaemVtMOVBphXkLyDAme1WHEVgXtZdnfGW1DXD4rG6frhAn3OFDrO6_m4rxipyIvKugh0JIVQacwtsWTAwOPQa0UlbDAo7CmE6fpC8k753AaCKmC1x9MzHXQUFzSLTefpDWGBivACVHXYXJdT-U0NDkpAfCKCMco9b4CM7Wyaaf_oWBj5vg6UoDl1Fg09wCejpK18eJMpV0TB3m7P_lu9vGdZjOG0jcF5wqNZ0jcfjOsLfdOz24F1pxHH7KF4vsiGz0oczhg0yFjUa0Kn_AI2GVt9YN0N3uvAHJdRCGcn6HekJK1ws4vgoJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مراسم اهدای توپ‌طلا ۲۰۲۶ روز ۲۶ اکتبر یا به عبارتی ۴ آبان‌ماه در شهر لندن برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90349" target="_blank">📅 16:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpsnMT0zqaFywRzhCjhcTUQLwftkIRQ6tgmv0dkvXNgSvztke1i77AaFGYvaIS23xnBal64uA3jc9KqRH8fkrFTSSsng6Ygv9t5YS_nSUJkUDpfW0Qg-digWC-9SWV0y5-iOXGKLfA5HrFjbnToqfegoNiBpXWirXqHfBqfciJVGcfcbZaxdYlaSI_8HS97zTTBfkNQH5vk1x0w_A1DF9LLzi_fuh7HO8y0Y74266aLgQtSQFFFDeuNRgDKnJQ8hZSEDXyjgESy4oNv7wIDDiHvSbZgKiJvhWNi1p2o8ULXshp4-4ViMBmusvTInuWJk_0crkT-CaaY6--LjjN57WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا: اتلتیکومادرید می‌خواد خولیان آلوارز را با قیمت ۱۵۰ میلیون یورو به بارسلونا بفروشه
💸
‼️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90348" target="_blank">📅 16:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90347">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPtM42DdwKvchG-C6L5H1LIZs5cvpgnt0Zy5DW7yduMsLLwabAkH2za--BEwxTN3r0tsfQ4TQ7X4TnDnfIxRoksOQvxJyx3EwMGfkHXhqB3EdKA3cM_UZgHJeMXg8wxeqdgJm73Qsg7DUFB3eGoqz4gS5tpBSPmwrqn5YcLjejeGVyNjXz-dFM7_AVvw999YigBbWd4MWhYHE9ih2tNoj8GIZFD6dlAiKCiask3EODdHVq2qiZZ_sr5T_9Zbqhho4zOIFscvg-GlcMH3vuOhwKtesXUT51Rn8TeMvdzdwad9t58lUDYoZgNtDYj2wedDbfmLhnDpoGh0Ld-znpqDww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد دیگو مارادونا و لیونل‌مسی در دو دوره جام‌جهانی که قهرمان رقابت‌ها شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90347" target="_blank">📅 15:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90346">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=vX-onrmIX0xUg2AocwbRGIi9FqDAWpVtvoKnd0WOW44UsGxAFwP0ldc0oJ9EIm8rTEeNWIfCQHTGQy7vUrC9VU6tDD3ZvgRENv2Uq_xL2cn0a_JL_mk0hyxByqx7nRn-BmDszh2-fjYCIZi4WderOVtHhKP-NG_frGr5c97IQG5ayTEZi03DH8Trj7WOO3PbtC3Xh1kT9TTxrTVC6PL02uxksCr0dWUs-_Wg1cMt4aMYAIrSVLjt-qACpV8eAzMloTv07XHLb-wTGM3-4LUy2tVjKqguRbDLuYXprRV4kVAXCdAx5Z2gxT9lxqowEziqvK_Mhf3HNQvKY1IT7b5lEaqx5tzYqkt3lfZK3MRxoBgMo1j3CugJKh9m_dc2KG7kZwXTQOUszFTGkmxww_mAUik-x2eteWR0GFOKe9vW35GQZxWEZb7NNP8fr72ZecTj-vKdTTrzd-0SVIhyy1cdSvI9cUBy7ZNis3ylDC7XQJhkxP6s9jGJhnWXMHYM5BMIJYhDY23OCjvAHRA9CVbxwMyyK0JOSvtTwZkHzSvo-HGiFK8_KZL8fUamKWG9GL7BvnSzx6lcOaJjYdAHiAgrtdaUUQ8ox2gUOvDwVTm2msGlt6zyBXCZXLkJYegor8IScxD6Hw60Ny5HMu95PVAu33yuSdpxdg6k1gkjLugTGs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=vX-onrmIX0xUg2AocwbRGIi9FqDAWpVtvoKnd0WOW44UsGxAFwP0ldc0oJ9EIm8rTEeNWIfCQHTGQy7vUrC9VU6tDD3ZvgRENv2Uq_xL2cn0a_JL_mk0hyxByqx7nRn-BmDszh2-fjYCIZi4WderOVtHhKP-NG_frGr5c97IQG5ayTEZi03DH8Trj7WOO3PbtC3Xh1kT9TTxrTVC6PL02uxksCr0dWUs-_Wg1cMt4aMYAIrSVLjt-qACpV8eAzMloTv07XHLb-wTGM3-4LUy2tVjKqguRbDLuYXprRV4kVAXCdAx5Z2gxT9lxqowEziqvK_Mhf3HNQvKY1IT7b5lEaqx5tzYqkt3lfZK3MRxoBgMo1j3CugJKh9m_dc2KG7kZwXTQOUszFTGkmxww_mAUik-x2eteWR0GFOKe9vW35GQZxWEZb7NNP8fr72ZecTj-vKdTTrzd-0SVIhyy1cdSvI9cUBy7ZNis3ylDC7XQJhkxP6s9jGJhnWXMHYM5BMIJYhDY23OCjvAHRA9CVbxwMyyK0JOSvtTwZkHzSvo-HGiFK8_KZL8fUamKWG9GL7BvnSzx6lcOaJjYdAHiAgrtdaUUQ8ox2gUOvDwVTm2msGlt6zyBXCZXLkJYegor8IScxD6Hw60Ny5HMu95PVAu33yuSdpxdg6k1gkjLugTGs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب الجزایر آماده جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90346" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90345">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaCZ7U54AOudCNeeY6KBrIH0QFBpK0b4YfvWWCF06ATc6f5f8xMox2WPQeAeqyYjDnzUQVmutSZf7HM7Uypx-b3TLI9_rjJrH9qBFuKEgV6sgdCk3ZSsA01Bq3dFUm0N4NL91mPtmkqPeuPGeZXugnwQRpGcGlWtoGYAzi18dvp-5Kxp5onZXkiHRoymOFSZlhHBdyZ2A2CDdSHMNpOUVlNSs11ItxxZgUZVZZ4quFNxlGU__5hkBM53hsyUOnwN4GtPSU4W4lZuznhh5VjajwYIgJYJ-HQKhgXq8iKcHX9cXc0afFyk9Aqmt3rSQ1dGgHySxqMTCp52XHgZBrcr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
🎤
امروز دور جدیدی از رأی‌گیری برای عنوان جذاب‌ترین مجری فوتبال را آغاز می‌کنیم.
❤️
عکس‌های جذاب ۸ دختر از دنیای رسانه‌های فوتبالی را تماشا کنید.
1️⃣
و هر چه سریع‌تر در کانال ما به گزینه موردعلاقه‌تان در نخستین تقابل رأی دهید</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90345" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90344">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etbmOwjCvCdTOXw2c5NkUJ8my7bAOdUjLcqhy64liP84bZoYUojkARGrPpGCi7iTY_zuiN9OaX_V2ih6HlQ6UFuvI8p1ZExspuz2jFMBKVZGgtg_hjt1NSHrXVQux0SkZW9H7o35aKJge5RkjUgE9fWveiDjS0h3TTTm5cSK4zmAM702HpkuO75XuBMDSsnAHU3-_AyIj1ti2A31aDWvAYwoqxRzf2v-X-_QKhhyVR2XUSqGnh1VL3zzY6co8ZSQTlW8cM0T4wJT3d06JXf2n5DjVJW68NPBCn22L5xmGiyO2LYIewhAlDvnVHMUK332Y7hSSUnJS6atqSAVbyTXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه جالب نیمار و لیونل‌مسی در بازی‌های ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/Futball180TV/90344" target="_blank">📅 15:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90342">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa-TiNpXl_cQojvGxVumtWHHbssewjHJLBp770nql9sTVmWR8xbhy_zZu3oNtqtXEmCG-MbUsBI1s5dB0ZTCn8Pgq-5ScXCzuWhlPFoxYm4Aly6FSdjhpn2I7hHYmD8wUHqUICjJ3TQAkewiyfoyvfrRTYXxGyWLlXQYADDV57RZjRry59I6QabQ6fxt0Fk4L2rN9Uc1Vgnrza-k9qyU7NGFeVDQ6rUlEpEcQ-tKguc51xYMl8i3C-FGSNNE4-8Z9mPn66RuMZIuEitgLE4yWA60jsog40CzZ7C2tWKnNSbXtEtsReOh8id2rECJvd5jWQs6fgQQSgARv4V_-vltgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترکیب آکادمی تاریخ بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90342" target="_blank">📅 15:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90341">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=oTMcjNJp7pmsOgXEMWLvi3YQZZF-4tKRIb8A9Wl0mQ_-ZaIcYFtzpVdbn3RavM8IXUBeAIqy1ge37_F2qa37YW7A34LXGtqGDUuLpSalJDiEylSQx3-DBfryMC0gx3Z1ZI1Bl190ivDtCF3QXftZqxkDiyVsDWXB9H3o9H4ZOYWOY2HevqWgbHLJe_igp-rI4zT0rz_RLTkrBAAgm7kl5VJYkA2_NfizuI6nB4GOBMSCEt16pk4Q6glCuNWCI__7iU1Ot5fIBtwmqMSlkHIWHpoFYnH-eoR3x6LMrgQ3AeR5iWnyozpAjd58O3TXTqoGtGAOcySNPZA0aEVIltHXUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=oTMcjNJp7pmsOgXEMWLvi3YQZZF-4tKRIb8A9Wl0mQ_-ZaIcYFtzpVdbn3RavM8IXUBeAIqy1ge37_F2qa37YW7A34LXGtqGDUuLpSalJDiEylSQx3-DBfryMC0gx3Z1ZI1Bl190ivDtCF3QXftZqxkDiyVsDWXB9H3o9H4ZOYWOY2HevqWgbHLJe_igp-rI4zT0rz_RLTkrBAAgm7kl5VJYkA2_NfizuI6nB4GOBMSCEt16pk4Q6glCuNWCI__7iU1Ot5fIBtwmqMSlkHIWHpoFYnH-eoR3x6LMrgQ3AeR5iWnyozpAjd58O3TXTqoGtGAOcySNPZA0aEVIltHXUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم‌ و صمیمی از نیمار در اردوی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90341" target="_blank">📅 14:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90340">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=UfsZu0Yv3zg5_Sys8aIPukSMd-TbwYwNcYVObmLQD2t4IfElE_m_q_ISZl_xsYiBv_rWnbsaOXCBzBAp2q2X3ynI8KoIRzxCF2xyvWc23ppw72EST0cWhN2rJsplSsxXI-s8Fr6IUOVPe4sy6mLO0o3i5FIn4zCvjh9jJbuXa1Ms3KjPgVnFSr2cH45-4-7c-YIKHt4jnEs95vCBdXkStjDt_sNtI6G3kMclaDqkHHel_zX_w82jxFeo-Dks0gWocrzfn1s7ZoHd51dDSzfdF5aQVmk6veH9Mz2Vvc3vihdzIc42iUyuAqaam0R93jkdJeTyQm9RxsVCwzxIB_GE0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=UfsZu0Yv3zg5_Sys8aIPukSMd-TbwYwNcYVObmLQD2t4IfElE_m_q_ISZl_xsYiBv_rWnbsaOXCBzBAp2q2X3ynI8KoIRzxCF2xyvWc23ppw72EST0cWhN2rJsplSsxXI-s8Fr6IUOVPe4sy6mLO0o3i5FIn4zCvjh9jJbuXa1Ms3KjPgVnFSr2cH45-4-7c-YIKHt4jnEs95vCBdXkStjDt_sNtI6G3kMclaDqkHHel_zX_w82jxFeo-Dks0gWocrzfn1s7ZoHd51dDSzfdF5aQVmk6veH9Mz2Vvc3vihdzIc42iUyuAqaam0R93jkdJeTyQm9RxsVCwzxIB_GE0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد جالب و شنیدنی هیوا یوسفی از وزیر ورزش و جوانان که هیچ نظری درباره قطعی اینترنت در ایام اخیر نداشت...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90340" target="_blank">📅 14:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90339">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=C6_CCWCgHEezpp1ISbfWEyKRhRA2W9vECnUMP3uZX_vkPNsHVlM8A89ld_vSuUkYLMSd9NDIvHWD2lHKEihdF1jygJ-KB5Yx35pHkeNU-2WpVBgT7gRCtzJjO2gT6QBrz0WNdzo4guEGOW55SI_0nE5Nk6Ojxt1lAbgRgHTGDDr5KSQSyTvZqmz715bwmXD8jg6uyJGLCQdioJ0VA3hNRVFzEKTufKnPlZRF9H4voLOqUX_C8mOfHa3y2nWxrUL4nJ8GBwjiZ6j5FLIJHWE-Z-vacbwOJu_OiIz46Vo-yp5gZYIFtIk1XlH5n92FtrSPzUG1ZpKFv9pqxHevPzd-nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=C6_CCWCgHEezpp1ISbfWEyKRhRA2W9vECnUMP3uZX_vkPNsHVlM8A89ld_vSuUkYLMSd9NDIvHWD2lHKEihdF1jygJ-KB5Yx35pHkeNU-2WpVBgT7gRCtzJjO2gT6QBrz0WNdzo4guEGOW55SI_0nE5Nk6Ojxt1lAbgRgHTGDDr5KSQSyTvZqmz715bwmXD8jg6uyJGLCQdioJ0VA3hNRVFzEKTufKnPlZRF9H4voLOqUX_C8mOfHa3y2nWxrUL4nJ8GBwjiZ6j5FLIJHWE-Z-vacbwOJu_OiIz46Vo-yp5gZYIFtIk1XlH5n92FtrSPzUG1ZpKFv9pqxHevPzd-nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پيش بينى فرزاد آشوبى از عملكرد تيم ملى ايران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90339" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90338">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOQ8hxZB8NHM02S44uy20Rf8u_6iYxZywwVXN17GR-1ZrW_EZo9Fh32ZwKvBZ7N6OTA4bhhmP6xeNC4MRSxUUxTw7gKrc_dk-CNOAdZaHIgZsPSpx4CjCKuRb690gBlAViFZcyjsgUJvn2b2i-WnbVIFGV-ZvhyD1aXOqJB2WN-QdasAd48NMB2kE03kkGaceZDJcTmIj3f7Igoig9mKjpvRDveiAq921sqwnsQmKJ7UK3lblI5URwlyNk0xZDWAK3ACZJ-pkngazoZP2Mshu5irK6QbTgW8cpqZIBphyIDD4u1_c86Lrw0mvrZfbT6_XRX4TRCVH1_OiQUZqdqS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۱۱ ژوئیه، ممکن است شاهد پرتماشاگرترین بازی در تاریخ جهانی باشیم.
🌍
اگر هر دو تیم آرژانتین و پرتغال صدرنشین گروه‌های خود شوند و تا مراحل پایانی ادامه دهند، طرفداران شاهد رویارویی نهایی بین کریستیانو رونالدو و لیونل مسی در مرحله یک‌چهارم نهایی جام جهانی خواهند بود.
🤯
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90338" target="_blank">📅 13:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90337">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqL4cDsMenLsARDmMpGvapIEzrok7pEoYyc9oZDE7WBhyfkTIECjoHYnuLPebviqwWQeuVHBRW3dSgdRSoJqHLdinpaKg77CTK9MWeyUJL18zjfjlaS-qsQTVx_QPkZfaC89b6988Wu8psTixw_-EIeGTf0qxeyYXqOjz358QO701rG5jte7dMP7LKWz1vPCARmOlIKQJ5LlwUmg82QU4EtTkiINroBDgCeVMdpdhW3UyAzPiboiOvab_kC9sRphRsqwo24U1H96Ah40VADdorf_rNs-y0upPixX-Wmr39s7emUMdNWdS3bbZOCErs2SpbwVtbqXcIPsFggVQfm-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره ده‌های تاریخ تیم‌ملی برزیل در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90337" target="_blank">📅 13:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90336">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=ujZQ2bh8O7wXR42GpwIy5_kXKfr1EpDQpzVIZZxUvYNfBxJCNT19QdOx_n5QedJMW4gqtBjNxVD0ZnTw5H1AKImEgCXT1bJK_kgwqyut5M5I7aDondBaq32EjbpCwZUzK45aoOdFoDD_paRUmGZXUbZ7O0lIRZdaPz8Lrcga9nq0sdXkV-WQNHLUjuqLNEtG34-ov1vSQX-lcZF-mpHskaHfV8Jb0IuhCc23tL-DG4nbk-0ZxO9LiPgcKYbLNWRif8QFK8ulzQA8_dNpyyx_1hIEWZROsc-3GGvhdnVIZanaZ76eeH5N-j4zffRVpJ_yF6bGm-oiPIpGK1VZuBovyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=ujZQ2bh8O7wXR42GpwIy5_kXKfr1EpDQpzVIZZxUvYNfBxJCNT19QdOx_n5QedJMW4gqtBjNxVD0ZnTw5H1AKImEgCXT1bJK_kgwqyut5M5I7aDondBaq32EjbpCwZUzK45aoOdFoDD_paRUmGZXUbZ7O0lIRZdaPz8Lrcga9nq0sdXkV-WQNHLUjuqLNEtG34-ov1vSQX-lcZF-mpHskaHfV8Jb0IuhCc23tL-DG4nbk-0ZxO9LiPgcKYbLNWRif8QFK8ulzQA8_dNpyyx_1hIEWZROsc-3GGvhdnVIZanaZ76eeH5N-j4zffRVpJ_yF6bGm-oiPIpGK1VZuBovyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیب منتخب سهراب برای حضور در جام جهانی
👀
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90336" target="_blank">📅 13:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90334">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اولین پیشنهاد بارسلونا برای جذب آلوارز رقم ۹۰ میلیون یورو به علاوه آپشن‌ها خواهد بود. لاپورتا قصد داره قبل جام‌جهانی این بازیکن رو جذب کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90334" target="_blank">📅 13:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری از فابریزیو رومانو :  بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.  خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90333" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90332">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SckIQAO-TS2PUbRU4OrI0Qb7H12YK5otEl_jXDrKRVOt05fPzAolrtGnvDMGKAjBAcVccMOdW1zLIHWr7BKHiQQDtaGeO3XCoYfVDS9fTTMl9feYPfBfzlC3yG7CiG3r2Whjd9Z9DLYtXSh8KeSegT8xxa8u9AJzi7ED830f81g5NX_ReANzOMquVqebMZKKxSX1kOdTVzavaQtaoKJSluZmPmeil_uB4DdGwStPEfcr1E-zsQOESNXOFtq60NiaHYwa5jPEFQgrg6Wp3Q9cnfTYFi-GGqtGgU5xM3THg2b7RbDhZdr0KecuADAYyEyZ_fPYwANeDfcwkfS7Vwus2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری
از فابریزیو رومانو :
بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.
خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.
پس از ملاقات مستقیم با مدیربرنامه‌ها و واسطه‌ها، بارسا پیشنهادی ارسال خواهد کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90332" target="_blank">📅 12:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=QTO1WWmqN16BxSLT-774qJsXq_nBQxuTdAJXKHxu6qfgDk7mfwLrv-uL1m_bLM_JW4o6T5K8AKnsWdmbXTh9FdRZBVSwOzfFt6gLfXgdHhQwV99OX30aJE34lKLhz9Vwvn66nLoYRPu2cB-yyy85Ab6Bby6zcoA5fkwMl45ZRx2KbRRK4hICKiqX3IN9OpwiDtsRx9K8OMqD_N2BGn6uRuGxGcVZUGmywdtzQJqxmUkhwqbhACb8J_jgZGgvWLTrQbJiDTHMR-09ERi7OwEACUeS6-UH1AEnOBU726GIpMjZfptC0c6l0hWiLsb-1JqVxqedEr-87eydsLgdHEmQ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=QTO1WWmqN16BxSLT-774qJsXq_nBQxuTdAJXKHxu6qfgDk7mfwLrv-uL1m_bLM_JW4o6T5K8AKnsWdmbXTh9FdRZBVSwOzfFt6gLfXgdHhQwV99OX30aJE34lKLhz9Vwvn66nLoYRPu2cB-yyy85Ab6Bby6zcoA5fkwMl45ZRx2KbRRK4hICKiqX3IN9OpwiDtsRx9K8OMqD_N2BGn6uRuGxGcVZUGmywdtzQJqxmUkhwqbhACb8J_jgZGgvWLTrQbJiDTHMR-09ERi7OwEACUeS6-UH1AEnOBU726GIpMjZfptC0c6l0hWiLsb-1JqVxqedEr-87eydsLgdHEmQ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینترنت بین الملل وصل شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90331" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👍
👍
#اختصاصی #وینرو :
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90330" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90329">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTonphKWxDQjFEb2A6F6MniqRy59r3Psfhlna8uaUlP2XhzguirYXnXNfdcgGuqg9xQsu6FhnuWTvQFkiaGVvb9gJS-wzK11qiWlh9kUB_g4FYCe0LemRaOzrMSmXxKCSe3p1fP7MIHDilYqfeayfWwr40WsBHu4TDqauR0Dvm0yWLMEMcxGA1aekSaQn9Ue255WN2Scb-W2lrkIeBfuX0pJ_bVQgKeXBC16Rm8n6473XTEMlBXrY30zWPvxDPlxBc-vXlsMvMmf6ubbAKNizJyXnmLVeKXNZ708gGK2lfx8-OnPMkZW_xDP1rL5PMYIr5_WavGuIVG6gZ2Ut1WAMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90329" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90328">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=FbAJqTS_qBwmNySB5vW5A-cE7sjuQ_q9E09yhfA_6LM4tEveUWzNueQ-WNjtEcQ28ZV3eTWxVqR2_BjAbbZ6xygtRg5QRYQ8QDmLIuScSDXBFHqf3E315vwJfrX9nnDWry9JaeXpvRxXmDfQH8gOQw8gk17I1ZzJz1l2mR1wT6qh5pi0S2kXb-P4aI0fqBHf-ARkckiDTZtdQ23kc1iaP7FD_qFHsGtw_nu-kBgg0EiYQAkLVCdLMEJA7KX3_XqXpZZXro4bQqHpBP1EleHwp_x5plQaysF3uDSjZ5myyEDPaCLI5A0JqYjRV_Ygr0JWpJ9bjHEXtEbCgcIefzneeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=FbAJqTS_qBwmNySB5vW5A-cE7sjuQ_q9E09yhfA_6LM4tEveUWzNueQ-WNjtEcQ28ZV3eTWxVqR2_BjAbbZ6xygtRg5QRYQ8QDmLIuScSDXBFHqf3E315vwJfrX9nnDWry9JaeXpvRxXmDfQH8gOQw8gk17I1ZzJz1l2mR1wT6qh5pi0S2kXb-P4aI0fqBHf-ARkckiDTZtdQ23kc1iaP7FD_qFHsGtw_nu-kBgg0EiYQAkLVCdLMEJA7KX3_XqXpZZXro4bQqHpBP1EleHwp_x5plQaysF3uDSjZ5myyEDPaCLI5A0JqYjRV_Ygr0JWpJ9bjHEXtEbCgcIefzneeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشت لامین‌یامال به تمرینات اسپانیا برای حضور در جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90328" target="_blank">📅 12:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90327">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfQCMvh4PJdWNsD3ySUcvxXkg87iKt65xGJQe8psNZppgj57Gse86-GleWWnnbJh6dMjDMnC19IPJ74TZrciKhnm4mGpDwvtLWFTMSr0W-9VT8OlfZSfchrcnenzqxb2S_FCz9bStnJtBWpklqQxuQc4hTCp0W0sA0a3nITRiV3IQih0-2rJYSB6YwLL6cBmuKNy3R7FlJ06sK7UzlcWiV5hACZcsTMkCeorMiiSB4U7NaaipqQSlsWKeI3b61MPGYtFC3kpq3OO2tIFxoHul-YKacJFf6JIeLwcFHu2iYQKQ8EkgtFqMWzeLcUvDJOkr3EgcrB3j4Z377nB2ltZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین حضور توی سطح اول فوتبال انگلیس
آرسنال تنها تیم بدون سقوط
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90327" target="_blank">📅 11:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90326">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=sUtarN_hHSAaz3FK76wwo2_QeRZTj1XszMg7xTDXgcVu-ksMwk0TkZwBsiomu_7akyd6u0uUxnupJ22NUwCqHxrJYVchIn_An_BBkTU3DOg3nB5nE7u7NbdfoHqY9gWTCE2sH7XKZgRATS78KRuEoyY8ZYTQV76MDWvupy0agux_NvjznpKhnCoJkruMuZKpYMSTKLEiVBuBbU5nhzbNjK8Fwn_TZwnKJg1xGAORnMHs-aKPBGvQJfIUqjThwGOwlzbGpqiu6aq0_6prjdXrJISFbdOnMbtCkQ_N5_4eekwFogYpV9B2EzG4mNX6cyT23F3cca3dJpgL8Z6GN5mIYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=sUtarN_hHSAaz3FK76wwo2_QeRZTj1XszMg7xTDXgcVu-ksMwk0TkZwBsiomu_7akyd6u0uUxnupJ22NUwCqHxrJYVchIn_An_BBkTU3DOg3nB5nE7u7NbdfoHqY9gWTCE2sH7XKZgRATS78KRuEoyY8ZYTQV76MDWvupy0agux_NvjznpKhnCoJkruMuZKpYMSTKLEiVBuBbU5nhzbNjK8Fwn_TZwnKJg1xGAORnMHs-aKPBGvQJfIUqjThwGOwlzbGpqiu6aq0_6prjdXrJISFbdOnMbtCkQ_N5_4eekwFogYpV9B2EzG4mNX6cyT23F3cca3dJpgL8Z6GN5mIYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تازه خارجیش رو بهتر بلده ..»
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90326" target="_blank">📅 11:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90325">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔷
#اختصاصی_فوتبال‌180
؛ مونیرالحدادی و یاسر‌آسانی دو ستاره خارجی استقلال برای ادامه حضور در آبی‌پوشان خواستار افزایش دستمزد و پرداخت به موقع حقوق خود شده‌اند. سیاست مدیریت فعلی استقلال بر حفظ این دو بازیکن است زیرا پیدا کردن نفرات جایگزین در شرایط بسته‌بودن پنجره نقل‌وانتقالات عملا سخت و غیرممکن است. قرار است پس از جام‌جهانی و مشخص شدن تکلیف لیگ‌برتر، جلسات ویژه‌ای با نمایندگان این دوبازیکن برای ادامه حضور در جمع آبی‌پوشان برگزار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90325" target="_blank">📅 11:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90324">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB5WEhCrCLPC5mLEWQMHvwiF6CD4bOQ32BYgp_hagdsvU_eBtJdfOZjiagjE0zCFnBkJjSbc0ZgBe-MD-rZOnByANnQecLLFNiSdxkU2mLeP6IMO9GuXeRjUXS0MgBBoPOPkl3k3pPqaRWq21775w73-Sa8p80XoTLUkv2bSmJ7aokLEPauP6E9BZd3FRc2ErK5czkzFW71qbz2zLc7FK1xZg-01GeKvy4ac4evwkCIk8q3F40Jutf4dm-QbVjPvc44T8lgCNrwcyL8aLRFelAOIquwD6ubVr-CMzD5aGyatvHEACsu9W3KHLTA1ogbuJDHd_JWRmINuDeNwGPG1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شب‌گذشته دیدار مهمی بین سران باشگاه بارسلونا و وکلای خولیان آلوارز برگزار شده است. این بازیکن شدیدا خواهان خروج از اتلتیکومادرید و پیوستن به بارسلونا است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90324" target="_blank">📅 11:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90323">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTbVxDSFW_dGdo95BQygUl8vh3iW4Sz9Qq0u7PSslc2mbp9ysFeoY7sG5zVUSUnB3jtMpzw7lThKM-urLRXUWzyd9jpsyjozl9Xp3j2YoJzCheMwny94IIQeC3XE2I13H9KsZmw4OOBSTw7W0nIomRE-1ccYIZWgeLhO30o-UbPYyA3pyi4pyHHh8LNQ2v-nVCISwaUqg5tUJ2YW86-QXoEXC-WmxJL3TExygRmqmMj2KDDpBV3R0nYQttOFjYAZFATKynTEEStx7gpcp9yj0SEAIVnV_Ad8ppL8yyUjhyA4BeeAicY30nJnD6befr5329AGnmda_sO7PCEaGXLtzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان تاریخ‌فوتبال برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90323" target="_blank">📅 11:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90322">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRQStsFmk3enKxg79mwRTMvjGYZxVPI1Tb9Q-Zw6ztwK9F0htggL8ovxETfRUREPGcZZlhzHn34per1c5QUghMi-inSjW7DxnRKAhheBbaEIcQMEN2D5xMZP4CfegSZLDgth6FDCKud5mSq2RNtUJnzNy5MBvdX5JgooUpbfPVdjKXjgelvNOYwLkDke1Aykudr_7tLuCaR5TuJDxsR8EYMu2bV-j31yEsU6h2U2BH7tv7pP5NsVx91_tW5-oHpdUxHZSjiVBL6V__tk8E7PH9anScabi7Z2cWgEmyaehQwi-JlSmPkiAI_kpDXvklGh9RrtRETnKTHx0KU1X5yD4r30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRQStsFmk3enKxg79mwRTMvjGYZxVPI1Tb9Q-Zw6ztwK9F0htggL8ovxETfRUREPGcZZlhzHn34per1c5QUghMi-inSjW7DxnRKAhheBbaEIcQMEN2D5xMZP4CfegSZLDgth6FDCKud5mSq2RNtUJnzNy5MBvdX5JgooUpbfPVdjKXjgelvNOYwLkDke1Aykudr_7tLuCaR5TuJDxsR8EYMu2bV-j31yEsU6h2U2BH7tv7pP5NsVx91_tW5-oHpdUxHZSjiVBL6V__tk8E7PH9anScabi7Z2cWgEmyaehQwi-JlSmPkiAI_kpDXvklGh9RrtRETnKTHx0KU1X5yD4r30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از عجیب‌ترین وقت‌کشی‌های تاریخ
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/Futball180TV/90322" target="_blank">📅 10:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90321">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOToPBoe-r3xHaLwynAYnGuVcAv1bnzVPHzz5N9rOaKWs_mb5rmXXC-0K-WFuI8fUT8KwoGLFSgqxgJOWyekLAjKVcuWsNAtGTAD2TDCgiDobP5VOQtV9IQcTi00eJR0dB9M4FRcaPcaYqqMwB28z2WPzdxlyIpeRLWr2lDTrzrSiIUGQkc03atLCpoY6i2ZlkkLqTIZrFZy4JpC5r_MMzWpYj1b_rB0ycCqhsqXDm1MlBkKaynIn48K1m_0rKQDPl2vF-2pNM8mxa4an0sqecwQMNyyH0f4jqPj1MXur75up-0Ibu2nGdvXXEMWfOBybVt8cprqv6YhU7OpZXEbSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیلیپه‌لوئیز سرمربی جوان برزیلی هدایت تیم فوتبال موناکو را برعهده گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90321" target="_blank">📅 10:21 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
