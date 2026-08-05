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
<img src="https://cdn4.telesco.pe/file/TfjLwu_097OoJnoZ44M-Ji9pmihqQz1FjWjyseytQvM5kXS0ZGqnn8_cutxsxKo6T6jJgf8vd2CqPQVoj6t-G1NA56-GIdEWYH1wDV9JldK01dIJNphvdxIg3vvpd61JYlqgIg_Gf7JDWbSoqs_G652deWwyUjA1SbvITEbBfccgT0Pfnr7TpOKj6RTbp2kwHiIMl1nuBEMp63atZWC1zdiPSjMDDhJzf0JsL-yguXDWXTHpT_Mz89dRXcJtPqMadMYZlayostozdqb3OBK4RX9dO4Q0tmcVbIDtIpksecISNeSEsH4JrNXhk_4_GzGKJ3iolp7co1zWyncW9grGhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 134K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 02:19:37</div>
<hr>

<div class="tg-post" id="msg-69605">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=C0kxf-l1Hr2A3Vh4FzIwYIctlfma0IZku8dlF5L2F2B9_Pdpy0Cs1w2OP_hrB1JmoIi4neHzFcloC-UjgMsw0Ha9EGjSjmECqjoR5dWmJtwkjy3ReB9GF03b7Sm5nqerPnN4qEH-zVP_Stcv-hlsX3w2PAKKVRL0svYmHf8FRC-Qv0_JWaK2WtBFpEx-qOZuobifihxZpKjb_IhOB3p2dtOhv3JrijPwKKmz2SpzkOjYKxYDXiOywR73KF6SYciZoSbf6kY8D-hg_hB2Et5neqhtd0SzY1ZCsiMYetBpdgZeY1yxIn4Fi3MgnZdTYWJTNBZ1a5hNrDOg2nDR4Hwj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=C0kxf-l1Hr2A3Vh4FzIwYIctlfma0IZku8dlF5L2F2B9_Pdpy0Cs1w2OP_hrB1JmoIi4neHzFcloC-UjgMsw0Ha9EGjSjmECqjoR5dWmJtwkjy3ReB9GF03b7Sm5nqerPnN4qEH-zVP_Stcv-hlsX3w2PAKKVRL0svYmHf8FRC-Qv0_JWaK2WtBFpEx-qOZuobifihxZpKjb_IhOB3p2dtOhv3JrijPwKKmz2SpzkOjYKxYDXiOywR73KF6SYciZoSbf6kY8D-hg_hB2Et5neqhtd0SzY1ZCsiMYetBpdgZeY1yxIn4Fi3MgnZdTYWJTNBZ1a5hNrDOg2nDR4Hwj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ممکن است دوباره قیمت نفت را «بالا ببریم»:
«قیمت ۷۵ دلار است. ممکن است مجبور شویم دوباره آن را بالا ببریم. خودتان می‌دانید وقتی آن را بالا می‌بریم چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/news_hut/69605" target="_blank">📅 02:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69604">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69604" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/news_hut/69604" target="_blank">📅 01:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69603">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=SuFsuZlEmRCUrVjj50D-sxLa6U_s-AhzT3JjFTJ9EVo9R1ZqdksjqKKDQUx0h_Tis_nKEWNhp4spotVsvm_YtvmEZLYllOxoH34K3SZQe26kYmdpMMiE76Sl_H4qq7sCCQYlUjEo_2uw38UEcrOBRZKS6SmH2VNNumolPFvIiASBIeo6iEZojnfBMWBWwk9UQz4YWr4xHEHe3_MpoM5Caf5J0P2ytv3peRenwQP8uN5pAKOfNBsR1SltQ0rp2QHCvtSE4zJDCIJ_amDUxEYSAzTlgKHyE1W3OPkIHp4wGL6sJvS6n2nLZ_5EM00MOd-N9G0Z2RBalxJ6ljeNcK9opA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=SuFsuZlEmRCUrVjj50D-sxLa6U_s-AhzT3JjFTJ9EVo9R1ZqdksjqKKDQUx0h_Tis_nKEWNhp4spotVsvm_YtvmEZLYllOxoH34K3SZQe26kYmdpMMiE76Sl_H4qq7sCCQYlUjEo_2uw38UEcrOBRZKS6SmH2VNNumolPFvIiASBIeo6iEZojnfBMWBWwk9UQz4YWr4xHEHe3_MpoM5Caf5J0P2ytv3peRenwQP8uN5pAKOfNBsR1SltQ0rp2QHCvtSE4zJDCIJ_amDUxEYSAzTlgKHyE1W3OPkIHp4wGL6sJvS6n2nLZ_5EM00MOd-N9G0Z2RBalxJ6ljeNcK9opA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a14
@betinjabet</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/news_hut/69603" target="_blank">📅 01:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69602">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=k9CAxU4EXlzUDPgejp9VsKrdy0Vf1ZXqSIqH2L6OFot0Dsb2pE8IPlWxYd2owpUtcTsLdXi_K32TtkhSa9znsvgNUaoXms3KjLrKrV8nhi0q3d1hS2kgrv8PyBchmcPphCtnmlRfebssQo5oAS6xGwnCi5bl2E-Q4NRO6V6QlrqBMBSC7nBNJyB-JEq44sfi7UGwfkP9qbiKKRCY6j7OekUsFqJs-vUFWbl8fPr7ThAr9P1-PJCR_OQq1bH1i-w5E_T8DpID3PEnHiJdb5p4Nj7Sitf0oeq-M45VkIgB-nDuD8tYVIuHXl7EW4K02qd47RyrxIBRy4w9qqqrJhBOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=k9CAxU4EXlzUDPgejp9VsKrdy0Vf1ZXqSIqH2L6OFot0Dsb2pE8IPlWxYd2owpUtcTsLdXi_K32TtkhSa9znsvgNUaoXms3KjLrKrV8nhi0q3d1hS2kgrv8PyBchmcPphCtnmlRfebssQo5oAS6xGwnCi5bl2E-Q4NRO6V6QlrqBMBSC7nBNJyB-JEq44sfi7UGwfkP9qbiKKRCY6j7OekUsFqJs-vUFWbl8fPr7ThAr9P1-PJCR_OQq1bH1i-w5E_T8DpID3PEnHiJdb5p4Nj7Sitf0oeq-M45VkIgB-nDuD8tYVIuHXl7EW4K02qd47RyrxIBRy4w9qqqrJhBOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ترجیح می‌دهم با ایران توافق کنم، چون نمی‌خواهم آدم بکشم.
ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.
ما در حال گفتگو هستیم. ببینیم چه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/news_hut/69602" target="_blank">📅 01:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69601">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=pxUSujv-3Rl8OiXXfMvXLYQljw0mo51GFW8ZDb0LvoCtRaVORXWB81jSXuiKBtWH2sd4-Xg2MD7phzG2BMS4XF2Erb4x2xsuRjOYh7nEwtKX9peUiEuMw_pLyfMuQxGMlZl826lDC1UyDVq5TziGq_VT14pmXqWfuje0RWTQQ21CoOc0vB_2W43L1aXhhRC9SrQJu0GhvTa2mzscn0kpvQU-hI-yjZH_bFfE0R2lB2zGR2NWqkSFR9j6PxxC1zOIdaAmU-3K_QxpacqqVMiOot7diJfiEjegIgNHk1Ml3cPEUFaTA24hKdiRWXGdWj4D5Y7DVXAf7j2-WNobMxTvoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=pxUSujv-3Rl8OiXXfMvXLYQljw0mo51GFW8ZDb0LvoCtRaVORXWB81jSXuiKBtWH2sd4-Xg2MD7phzG2BMS4XF2Erb4x2xsuRjOYh7nEwtKX9peUiEuMw_pLyfMuQxGMlZl826lDC1UyDVq5TziGq_VT14pmXqWfuje0RWTQQ21CoOc0vB_2W43L1aXhhRC9SrQJu0GhvTa2mzscn0kpvQU-hI-yjZH_bFfE0R2lB2zGR2NWqkSFR9j6PxxC1zOIdaAmU-3K_QxpacqqVMiOot7diJfiEjegIgNHk1Ml3cPEUFaTA24hKdiRWXGdWj4D5Y7DVXAf7j2-WNobMxTvoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
هیچ‌کس نمیدونه که کلمه «dumb» حرف «B» نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/news_hut/69601" target="_blank">📅 01:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69600">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇷🇺
🚀
ویدئو منتشرشده از شلیک گسترده موشک‌های اسکندر به کی‌یف و حومه آن در روز گذشته.
@News_Hut</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/news_hut/69600" target="_blank">📅 00:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69599">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTaJ9YZPScV5_S6PgHLPuPGYOCuh5GxbxtGcUQR0V3QXgMVcOw-oVPwmw1hbrQ0TdCE_O1wyAOitU94-MfXbvo-C7cah1vfDHvxH_vTRVah6OVFuUa0W_kUusOecySuinwcMtipDk16mfcjmK-cOUjD86xHJ1Wp7x_o27mfyj-AyCNach0GRqu1qOij5QuRVIIbbxWIQ-0wQUUg44iqztcaG4fkRuzbyAl3PXypvNiJmwUcBk7FB9MoGDKtNSq-elXVvfBL90kYXy4djLAV8LTaf73oT2xmUdCBzbUEnfRH8ks0rwIj0PRha9JyfuU4_HY7sBSssI7FWDc-frNNnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مود:
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/69599" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69598">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=f-vbOAVl0rYyNbMDT_37dGmw_H9dCwUD0h-rIoaG4SfcgOvaxhJJnicscVqmmdWNkFvR35KBj09DMP7qJzYc_B_-jy8DuWAuC12WbTms5HKZkXx-z0PwhvsN3-6yDjxVOeMqYRC-i3wqtOqaT6MYUHLh1J2Aobnh0UhqfFxCm8mYXDwxS9gphyKSZJmfJuznswcj70LbmlW47WOYd9zFQ-CNyOj1JS7qNBGJNdOf81kKBfdeo6pwPoVV1g3LEvGbWu2dQhHDsoO90bruaXKVUni0ONPSv0DnHN3yXn1zCXF657kux97hAdiG-1ib71se5yfK7CCJ6Mi7Qf66PS-LDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=f-vbOAVl0rYyNbMDT_37dGmw_H9dCwUD0h-rIoaG4SfcgOvaxhJJnicscVqmmdWNkFvR35KBj09DMP7qJzYc_B_-jy8DuWAuC12WbTms5HKZkXx-z0PwhvsN3-6yDjxVOeMqYRC-i3wqtOqaT6MYUHLh1J2Aobnh0UhqfFxCm8mYXDwxS9gphyKSZJmfJuznswcj70LbmlW47WOYd9zFQ-CNyOj1JS7qNBGJNdOf81kKBfdeo6pwPoVV1g3LEvGbWu2dQhHDsoO90bruaXKVUni0ONPSv0DnHN3yXn1zCXF657kux97hAdiG-1ib71se5yfK7CCJ6Mi7Qf66PS-LDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فیلم وایرال شده از یه کارگاه آموزش فن بیان توی تهران.
چه خبرا؟ به لطف شما:))
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69598" target="_blank">📅 23:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69597">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=kTqoK6RLlKZgYkuUfgt0Ir1O2X3rg5u7WcWX8WZ_qlzeko3jIBZy5NYFEhhTfKvFTSGL6mdD-ylycHO1ccjbu90cEp1MSM9BgiyfAWK6f1Cwuf56W_4E5BKYS5En9amcMgmhPVe9uA1dZab0muU9R6UzgtAflv9BOuPZ8jN3QiZFSqgyq4vi7QHzdD4AiIL-PHNLr9IDr9D-1b1X93ezER87Z_QzEkPUTz-2tyZ5QF4LfANtimEVuaJuYhgL__aMsHqY4Gm1mDoQa5vSZbLn68X4aQM58CQE5r3akXAEDJvoAEVyccQHjGav7cpRNR2Zs1ZedqnmEdUH4PBjOQRF1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=kTqoK6RLlKZgYkuUfgt0Ir1O2X3rg5u7WcWX8WZ_qlzeko3jIBZy5NYFEhhTfKvFTSGL6mdD-ylycHO1ccjbu90cEp1MSM9BgiyfAWK6f1Cwuf56W_4E5BKYS5En9amcMgmhPVe9uA1dZab0muU9R6UzgtAflv9BOuPZ8jN3QiZFSqgyq4vi7QHzdD4AiIL-PHNLr9IDr9D-1b1X93ezER87Z_QzEkPUTz-2tyZ5QF4LfANtimEVuaJuYhgL__aMsHqY4Gm1mDoQa5vSZbLn68X4aQM58CQE5r3akXAEDJvoAEVyccQHjGav7cpRNR2Zs1ZedqnmEdUH4PBjOQRF1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
دیروز یه خبرنگار از بقایی، سخنگوی وزارت خارجه پرسید چرا جواب صحبتای ترامپ رو نمیدید؟
بقایی گفت چون باید رفتار ایرانی داشته باشیم و حرکات زشت دیگران رو الگوبرداری نکنیم. آخرشم یه تیکه از یکی از حکایت‌های عبید زاکانی رو گفت : "فعل و عمل ما را و دعوی ایشان را"
🔴
حکایت کامل عبید زاکانی:
شخصی اَمردی به خانه برد و درهمی به دستش نهاد و گفت: بخواب تا بر نهم. اَمرد گفت: من شنیده‌ام که تو اَمردان را می‌آوری تا بر تو نهند. گفت: آری، عمل با من است و دعوی با ایشان. تو نیز بخواب و برو آنچه می‌خواهی بگوی.
🔴
حالا معنی حکایت:
یه مرَده یه جوون بی‌ریش رو پیدا کرد، یه سکه بهش داد و گفت دراز بکش تا باهات همبستر بشم [ کونت بذارم ].
جوون گفت: من شنیده بودم تو جوون‌ها رو به خونه میاری تا اونا باهات همبستر بشن [ اونا کونت بذارن ] نه تو.
مرد جواب داد: «درسته؛ عمل کردن از طرف منه، اما حرف و ادعا با دیگران. تو هم فعلا دراز بکش، بعدش هرچی خواستی برو درباره من بگو
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69597" target="_blank">📅 23:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69596">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
ترامپ بهترین دوست ماست، اما می‌خواهم یک موضوع رو روشن کنم: "موجودیت اسرائیل قابل مذاکره نیست.با توافق و مذاکره یا بدون آن، هر کاری لازم باشد برای تضمین آینده‌مان انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69596" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69595">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Esgard-VPN.apk</div>
  <div class="tg-doc-extra">42.4 MB</div>
</div>
<a href="https://t.me/news_hut/69595" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پیشنهاد_ویژه
فیلترشکن محبوب اسگارد ‌وی‌پی‌ان
تقریبا با همه‌ی اینترنت‌ها کیفیت اتصال و سرعت خوبی داره. حتما امتحانش کنید
لینک گوگل پلی:
https://play.google.com/store/apps/details?id=com.vpn.esgard&referrer=628035</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69595" target="_blank">📅 23:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69592">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kpAnE54Gyh5M_6D8K0T6vk3GsGNxEFlhNLz5wJ8dOj-RSoOXolR9UqMnz0zxBa5ZqC745bFQS1REPQazzsHQWQ-TLslDfXoO1AOmEYePxSmUf7_2oeDjrz-_4kBO6uLBH4d8nZs6_TLyyRnNogSlvNCF24MkleiZqWiWvcvP04SSxah30bBz7AMw1eRJ7KMx7TFaCVwZ1ZbNR0QJcYsrl4e-M-6GYsAJRpRy469A6wGLgSwu2vmwnazUuYH4KV-74F_zguBvOA5X3ED2h1kAmecd4QhKdoXM96HUul7Bq6ge7VIkFW1eavKeIAZ4zNn-1-4HPYMhzfJrPIqdgGfcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXvIEG8E64z7W5qzBTFGEZb-fvE0yIw42QuftCcgruFKFCX8ZICN1KfAo0KewKrzbEe2B8X9_EIOK3AO1JlF5DrgRls6WnlOTIWE0oBcaKEvj269Ms-y8Of9mRasPoD3OFj5Kin8SSmuymHPxbn0VOvoWYTYEpPGYuzDSkFJVDW4InP1sRIF4YCzVrwMIw95Vt7ufE_6ICzLtS8FMmmHC5N7rFu-u-snB6ZT2KzY3ymGPThm-dkdX42WykzG8-tTUjw_QRiTGjz8RnT86_zW_4c_ctwQIAD_3O9iFXhuM5arc4OYWxTm7Guh9N5qzb68Gg7u_k1JPiDW2LVLbuL_fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=v5wE3m6eAmBAWKBKvSN41YK_ljRbn8FsCp2tHUC9ED5W9qyiNbv9Xl48uT8Cx5rUn1IMn5r1bL6bKrog_mKXl1Odu36ryh07OEI1E1FzF-3aXB2MCI64zrFpDlgKeSgIcmvX3lBeWJBq7sCYLxoC09g8UIGHkYr_iv7LefBUCmiwkPI3NR0FtqDJ9jN0xeRMLZnfUL7ybawRuYmAbR20f6t7ydXGAdDvrgk0gnhBnHWBjE3OY3jTvXpekDacJ9SFmCF0siKj1L7h7XnAYgCrnjgvYOfUDR3uFA4PEX2woKiZMRyfoTKasTLtLuBPvCQDWQEUnJcGLRxgzyekQ1ko-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=v5wE3m6eAmBAWKBKvSN41YK_ljRbn8FsCp2tHUC9ED5W9qyiNbv9Xl48uT8Cx5rUn1IMn5r1bL6bKrog_mKXl1Odu36ryh07OEI1E1FzF-3aXB2MCI64zrFpDlgKeSgIcmvX3lBeWJBq7sCYLxoC09g8UIGHkYr_iv7LefBUCmiwkPI3NR0FtqDJ9jN0xeRMLZnfUL7ybawRuYmAbR20f6t7ydXGAdDvrgk0gnhBnHWBjE3OY3jTvXpekDacJ9SFmCF0siKj1L7h7XnAYgCrnjgvYOfUDR3uFA4PEX2woKiZMRyfoTKasTLtLuBPvCQDWQEUnJcGLRxgzyekQ1ko-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو لیگ دسته سوم تایلند، بارون میباریده، ولی همینطور فوتبال بازی می‌کنن
یهو یه صاعقه میزنه و صاف میخوره به یه بازیکن و اون بازیکن فوت می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69592" target="_blank">📅 22:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69591">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvWg1y3cP7Klh5_CAHbtXxpy_kF9jhy14KFi0X6m200jqjSvx6N2I_ajP803i9w0-EyZqS7dJwgAFujXPE7qfMrCfrYxhKCRyPCTpHeOcJkw84E0LYG0g7HkCHstoGwIdSSF56wwDU-GmNva9POxhZIeI_z7ZDG5HAooKJZfhcnvJZbQDnwMSYzp6sajYsg9inHDvZsXSHe2drNvkEvhEEwZLyt8262jy9Xm2SmQnEwKNoKGp2vn9Pw-BF1BFEqJ3LMKshvV-0uP2Y-qncQOji0uU9FZ0aijlnjLZeratz8oWs5V_OvWuHjRyCW5uwDJfSbMDh9c4Z9zAeHtO4lVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇶
وزارت خزانه‌داری ایالات متحده تحریم‌های اعمال شده بر شرکت هواپیمایی فلای بغداد و چندین فروند از هواپیماهای آن را که در سال ۲۰۲۴ به دلیل ارتباط ادعایی با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بودند، لغو کرد.
این لغو تحریم‌ها، شرکت هواپیمایی فلای بغداد (که با نام عراق اکسپرس نیز فهرست شده است) و دو هواپیمای بوئینگ ۷۳۷ (YI-BAF و YI-BAN) را از فهرست ویژه اتباع تعیین‌شده توسط OFAC حذف می‌کند و به تحریم‌های مرتبط با تروریسم آنها پایان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69591" target="_blank">📅 21:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69590">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPaw0qx88yQMq1jxFX5FY-nOAHIG8Gxx5aUMmCLDDRekkKKMOtLXhLl_C7HE6lzRfiGJTlfu2VgMizad0KFi7jkKvQ1honHiSLQmIzDtepNfoDoWg-W_xml1R7mJGi45kF5av7OR7icUBGSZ7Qrjay0YECSGn6pmGB0tKUm-0IJhnrUxM7fU-ylyP5xgH8T0SVQZrwKABnZiQ8Z-DVHNWoUdFd_ZAdRPonYFp4wnO8cDufZWYwUma_JFVISsRNPd8GiqrubIS1cfDMbtfgrab-_KXBCG19TltHPlTzZbOvFEiBYkgzKz4o5YPrUfnq8MvN4xQCcAkR95x-M9ijnM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی:
ایالات متحده تقریباً ۴ یا ۵ روز پس از آغاز دور جدید درگیری‌ها، پیامی مبنی بر درخواست مذاکره و حل‌وفصل مسائل ارسال کرد.
هرگونه توافق در خصوص تنگه هرمز باید صرفاً میان ایران و عمان باشد.
ما هیچ‌گونه دخالت خارجی در تنگه هرمز را نخواهیم پذیرفت.
با اجرایی شدن توافق جدید، مسیرهای موقت فعلی در تنگه هرمز بسته خواهند شد.
بخش قابل‌توجهی از مسیرهای تردد کشتی‌های ورودی و خروجی به آب‌های سرزمینی ایران از این مسیر عبور خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69590" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69589">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=GQAuoe0pmBOIdAIPeZY8E0BSjVrZWdT8_0ihmgxCcjz48n4-NQRWsPGK23_as7Q1zvwU3_tcc7Cileb3b-14fC1I1erQogllKPncSUF1dXBz481cieZ1UBF4NuTBtjMK_bCZwrEFXe4jle9qSU6Fqm3IZIJIoRZmXrflF7Pf-ldrgNoYl6uHpi6yUBL7w-9TrkQ4XPwFd0XsmCLm3rPsuiCBDhnFm0KYzou9kDdus0_8bQ-MB8eSg9tXy7bSnRafSJAnrk470bE5qDTs6EH2VJKTVzpDO9I5W6kl0ahbnJDo2pq7DlBc5sb1LsjGMz--DmKxsrEGVN5h2U-fze4jVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=GQAuoe0pmBOIdAIPeZY8E0BSjVrZWdT8_0ihmgxCcjz48n4-NQRWsPGK23_as7Q1zvwU3_tcc7Cileb3b-14fC1I1erQogllKPncSUF1dXBz481cieZ1UBF4NuTBtjMK_bCZwrEFXe4jle9qSU6Fqm3IZIJIoRZmXrflF7Pf-ldrgNoYl6uHpi6yUBL7w-9TrkQ4XPwFd0XsmCLm3rPsuiCBDhnFm0KYzou9kDdus0_8bQ-MB8eSg9tXy7bSnRafSJAnrk470bE5qDTs6EH2VJKTVzpDO9I5W6kl0ahbnJDo2pq7DlBc5sb1LsjGMz--DmKxsrEGVN5h2U-fze4jVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
❌
🇮🇱
امروز در پی وقوع انفجار در ساختمانی تله‌گذاری‌شده در «مجدل زون» واقع در جنوب لبنان، دو سرباز اسرائیلی کشته و هفت تن دیگر زخمی شدند.
حالا قراراست بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و یسرائیل کاتس، وزیر دفاع، ساعت ۲۱:۰۰ به وقت محلی نشستی امنیتی برگزار کنند. محور این جلسه، حادثه مرگبار امروز در جنوب لبنان است که منجر به تلفات متعدد در میان نیروهای اسرائیلی شده است.
به گزارش شبکه ۱۴، انتظار می‌رود مقامات سیاسی در این نشست درباره انجام یک واکنش نظامی قابل‌توجه گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69589" target="_blank">📅 20:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69588">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTarrJRbJN6wckK6Rkfk0iK8pT-VU2PM3ri5FVOLkahQt4ZWRlNXa7_eNBeDfJRGncFT7U7X26kh6WHZSfaznAaKPsKferyX-gLT-rsf3XP4sYcpZ7Xyj6WpNvAlixepDX9cfc7xjQDFgcu5JemsQAItZ-D2eeDrdTlOY65LAGZIhZ5__08vBiXLonxu0T_aMeh2fPamNAexFtr4Tozo_wFbg-vDNbro-isi2Kwt7AXPtMKoZtUZHhEPreooHNkD4Fvxc5DfDW9PwiTLnzBYBxYwgP2OuNMmZAZHYtGL1-94Z7RHaMxBM1_A_CrWMKD_WK7D3vLQtT96tCeeHcWH8bPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTarrJRbJN6wckK6Rkfk0iK8pT-VU2PM3ri5FVOLkahQt4ZWRlNXa7_eNBeDfJRGncFT7U7X26kh6WHZSfaznAaKPsKferyX-gLT-rsf3XP4sYcpZ7Xyj6WpNvAlixepDX9cfc7xjQDFgcu5JemsQAItZ-D2eeDrdTlOY65LAGZIhZ5__08vBiXLonxu0T_aMeh2fPamNAexFtr4Tozo_wFbg-vDNbro-isi2Kwt7AXPtMKoZtUZHhEPreooHNkD4Fvxc5DfDW9PwiTLnzBYBxYwgP2OuNMmZAZHYtGL1-94Z7RHaMxBM1_A_CrWMKD_WK7D3vLQtT96tCeeHcWH8bPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله ایران تا آمریکا با موشک فقط چند دقیقه‌ست، اما پیاده باید نزدیک ۱۹٬۳۰۰ کیلومتر راه بری!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69588" target="_blank">📅 20:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69587">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=BKgwkZefWWmNU_pEUzwVR9uWLzELLsOTDfauAyCXg1mh6UlmoKugXza6OexcTq6B1oT_Z11V6QkerukZF_LSAHvkgOVjtOsTOzw2Zo79koYvNis64nbDzosLBr-rth2zlT-YQcb1wW9SJcZ1uQamm-CKoY-CtoHOftWLWpF4zCWZcwTUvBWRXuEYzwixaXOteo4I03LgWKwnm68nDLqUexkZQxp2VVNjaiqc-FJ5klbj2gcbnZojiDKVMdAvH8yrphM7DNU_E_ZWpErqEGhf3rZQSCg3FllmU0vv-Z93Yk3C4D6rAnqnWiOzywKm8e1YrBlsTtXKmr4Azjw1Cutn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=BKgwkZefWWmNU_pEUzwVR9uWLzELLsOTDfauAyCXg1mh6UlmoKugXza6OexcTq6B1oT_Z11V6QkerukZF_LSAHvkgOVjtOsTOzw2Zo79koYvNis64nbDzosLBr-rth2zlT-YQcb1wW9SJcZ1uQamm-CKoY-CtoHOftWLWpF4zCWZcwTUvBWRXuEYzwixaXOteo4I03LgWKwnm68nDLqUexkZQxp2VVNjaiqc-FJ5klbj2gcbnZojiDKVMdAvH8yrphM7DNU_E_ZWpErqEGhf3rZQSCg3FllmU0vv-Z93Yk3C4D6rAnqnWiOzywKm8e1YrBlsTtXKmr4Azjw1Cutn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
ترامپ بزرگ ترین دوست ما هستش اما به صراحت میگم وجود اسرائیل قابل مذاکره نیست.
با توافق یا بی توافق هرکاری که برا آینده مون نیاز باشه رو انجام میدیم.
نیاز های الزامی سیاسی مجبورم میکنه این مراسم رو ترک بکنم.
در حال حاضر توی یه رویداد بسیار مهم نظامی سیاسی هستیم.
این جنگ موجودیتی هستش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69587" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69586">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">خفن ترین تیپستر های ایران با هم جمع شدن و TRUST BET رو تشکیل دادن
👍
هیچ سایت بتی دوست نداره شما این کانال رو پیدا کنین
رایگان بهترین شرط هارو براتون میذاره
حتی هزار تومن هم دریافت نمیکنه
سریع از این لینک جوین بدین کانالشون
👇
(این پست پاک میشه)
g14
https://t.me/+cBQ8n7zLQiUzN2U0
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69586" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69585">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1mVBnOY9Il_iowEyHWyypryntWUbv4xZG88JfOx5l82PU7NxP6LNl0T6UcoyZIqvwpvo7SwYBoi8FXN3KxZSpCE7qhyZS4pqjBHELpJTkf9cnvTp-tMSjTGpH8QAe-nIvmuyxzZoNWbtK8xZBGnmJIs_KEqOhvUbS0Wbts4F4ghFaXN_AfnGUmKSBQCGIn4BvU8yfAv2iI35kVRJaNQo7m3hGxWXD82eQW3iBtFLg6QuCPJamSikHcljwBqe5zv5fPkhNGxotQwPGEkYNSQtxV20hkEF9-Xy2wSanjTQ0H9q8b-XcXKiZgcfjrEFt6tz_dIm9jFX3kLLvi5nWp6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 میلیون تومن برداشت روزانه ی کانال تراست بت
🎁
پول دراوردن از بت تجربه و استراتژی میخواد نه ادعا
برایند ماه تیر توی کانال تراست بت: 78 درصد رشد سرمایه بود
✅
40 بازی اخیر 34 برد
📊
💠
https://t.me/+cBQ8n7zLQiUzN2U0
g14
💠
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69585" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69583">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=GgpTwNeM3J9akqUFNh-tqJc3SM1zGMrp627DForFApulrT8XpLskmUxoz2ErJUp0B92DdOXIQ7qIDxDcL_5bG_1Dz8T4QnNOwgY44-kGl5km6LUFUY1OlnaUFiTaCwZIPkUjbUDtQV5A2_SbpH61uYWu9rj-i_Z3ayLnc6G329_OiNtwtcU5UDaE9VT1DaEdsz7_2ZtjNXYrjnE163Fhay1pWfQ9DkwvOrgIS1ntlpEnMgditxSnV7XPHO-jYgfxJ32waS0HTYcKMuu87_FTR7jgntK_csbgFRmCcoyyhHGClWiCkNj6kmAoJN-DhPe7zUt2cVpjmVr7KGsqGEnGhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=GgpTwNeM3J9akqUFNh-tqJc3SM1zGMrp627DForFApulrT8XpLskmUxoz2ErJUp0B92DdOXIQ7qIDxDcL_5bG_1Dz8T4QnNOwgY44-kGl5km6LUFUY1OlnaUFiTaCwZIPkUjbUDtQV5A2_SbpH61uYWu9rj-i_Z3ayLnc6G329_OiNtwtcU5UDaE9VT1DaEdsz7_2ZtjNXYrjnE163Fhay1pWfQ9DkwvOrgIS1ntlpEnMgditxSnV7XPHO-jYgfxJ32waS0HTYcKMuu87_FTR7jgntK_csbgFRmCcoyyhHGClWiCkNj6kmAoJN-DhPe7zUt2cVpjmVr7KGsqGEnGhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پلیسِ رشت یه ون آورده وسط خیابون و شروع کرده داره به دخترها اخطار میده؛
بعد واسه مشروعیت دادن، یه مصاحبه از این خانم رشتی رو منتشر کرده که‌ با میگه:
گشت ارشاد رو دیدم احساس امنیت کردم.
امیدوارم این کار ادامه‌دار باشه چون اصلا از وضعیت سطح شهر راضی نیستیم.
چهره شهر اصلا عوض و زشت شده.
الان همه فکر میکنن رشت این شکلیه ولی خوب‌هاش رو نمی‌بینن.
گشت‌ارشاد دغدغه اکثر مادرهاست نه فقط چادری‌ها!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69583" target="_blank">📅 19:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69582">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
منابع عربی از حمله موشکی سپاه به بحرین خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69582" target="_blank">📅 19:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69581">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d659457195.mp4?token=LXxipzIWjFSgs5T6CDLXzcGO65-p-fmh8IGu0KITLh_p1Lxj-FBJ3NPs9rzx4-SKi9XGushnNu5o_QGMPjUta-4zg8CfQmuNxI9t22Hzvcz1xhE_M5HFpvc8P1QJ_8H1XwGJH9myFnJuuuzwKX6ssVheEX-e7Ymy3CrM21OnGJ_G2bFfQXo0yUOOptKJHQx-xR1sGvJmaboAX2gsfGmtQly5KWW_jZKvLfYbfhyYjIN_dSAsmgFrX26Pu3W9LLdUL4rI0f3LQ0Y0ZjwjsaMXpVHN5GM3HUh7xJR62RmVAoN4oXYppRuNkATzxQMjK_ipCC3PfRSfVW1_MbKdhE2fTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d659457195.mp4?token=LXxipzIWjFSgs5T6CDLXzcGO65-p-fmh8IGu0KITLh_p1Lxj-FBJ3NPs9rzx4-SKi9XGushnNu5o_QGMPjUta-4zg8CfQmuNxI9t22Hzvcz1xhE_M5HFpvc8P1QJ_8H1XwGJH9myFnJuuuzwKX6ssVheEX-e7Ymy3CrM21OnGJ_G2bFfQXo0yUOOptKJHQx-xR1sGvJmaboAX2gsfGmtQly5KWW_jZKvLfYbfhyYjIN_dSAsmgFrX26Pu3W9LLdUL4rI0f3LQ0Y0ZjwjsaMXpVHN5GM3HUh7xJR62RmVAoN4oXYppRuNkATzxQMjK_ipCC3PfRSfVW1_MbKdhE2fTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصاحبه تاریخی فیلدمارشال رضایی و خنده مجری:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69581" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69580">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tky4zdmcB9VE41RQnjhJ6if7DzftinFqm_thjZMi7skQPtLA1Z3EDd6oRel9xfwlbjUUPBSF6lHykH3VGZkPLmtHLOd3rnreTsVTK_rFuK-S7xNiKQHsfqEvfJ-vZ1l6HEDblr9n1q1Da3uCkdqH4Uiw__KpvpkaETpMcoq7FXUEejds9Mx5-kqR4vqlJUTrWPtw8DGhgJNnPXA8uX2sHTcUm2X1nW39RZpoi71BsSR456VNeNU9UZFjtDYHryGxxCe37Dvt30l1nYKMzlPEbZfZaB2M8TnoljBoLBs-J6K3ZZfvbTpPh2h8UR9qlGKTc_W5Ad11mG4A-8v1iJYBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پهپاد مافوق‌صوت Quarterhorse آمریکا به مرحله آزمایش نظامی نزدیک می‌شود
واحد نوآوری دفاعی آمریکا (DIU) برنامه توسعه پهپاد Quarterhorse شرکت Hermeus را برای ورود به کاربردهای نظامی دنبال می‌کند. این هواگرد بدون سرنشین با هدف آزمایش فناوری‌های پرواز مافوق‌صوت، سرعت بالا و قابلیت استفاده مجدد طراحی شده است.
مشخصات اولیه Quarterhorse:
⬇️
نوع: پهپاد آزمایشی مافوق‌صوت
⬇️
سازنده: Hermeus
⬇️
طول: حدود ۱۲ متر
⬇️
پیشرانه: موتور جت توربینی با فناوری توسعه‌یافته برای سرعت‌های بالا
⬇️
سرعت نهایی Quarterhorse: تا محدوده مافوق‌صوت بالا (هدف نهایی برنامه Hermeus رسیدن به سرعت‌های نزدیک ۵ماخ است)
⬇️
قابلیت‌ها: پرواز خودکار، استفاده مجدد، آزمایش فناوری‌های پرسرعت
⬇️
کاربردهای احتمالی: شناسایی دوربرد، آزمایش سامانه‌های آینده و مأموریت‌های نفوذ در محیط‌های دارای پدافند پیشرفته
پهپاد Quarterhorse هنوز یک پهپاد رزمی عملیاتی نیست، اما آمریکا آن را به‌عنوان یک سکوی آزمایشی برای توسعه نسل آینده هواگردهای بدون سرنشین سریع و کم‌هزینه دنبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69580" target="_blank">📅 18:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69579">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=ljTaYCX2qiRYAkBpqgAKfiQHwdqYAwUyFysrDHWPtbaBcZIHUi6labNPJsZdCv0I6VcVxPnJJ-WxYTcOTxtCm-iRYzUZ1bj_NGkz1mcXu__zO-hzE6R1lHoX30sDGfr2Mr36t3SvZTT9jAzscMnLvc-FyKnqPat5aZKCR86ueQezoNeVod9Ep6beO-YlnQBSQbaCDKRzSCs9kcphDQ4CJVuM3U5_kQi6-Qsn5zRGKVUxFUy10vuVSU39t6xWIaxoIb3SV7Zb8bJpU5R1b9nSA-oNMIh6gDTX0NwFhV9iyDos7MH-clXE06QkyKDDczUmEEdZK_9-5xu79y3j7Jno9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=ljTaYCX2qiRYAkBpqgAKfiQHwdqYAwUyFysrDHWPtbaBcZIHUi6labNPJsZdCv0I6VcVxPnJJ-WxYTcOTxtCm-iRYzUZ1bj_NGkz1mcXu__zO-hzE6R1lHoX30sDGfr2Mr36t3SvZTT9jAzscMnLvc-FyKnqPat5aZKCR86ueQezoNeVod9Ep6beO-YlnQBSQbaCDKRzSCs9kcphDQ4CJVuM3U5_kQi6-Qsn5zRGKVUxFUy10vuVSU39t6xWIaxoIb3SV7Zb8bJpU5R1b9nSA-oNMIh6gDTX0NwFhV9iyDos7MH-clXE06QkyKDDczUmEEdZK_9-5xu79y3j7Jno9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69579" target="_blank">📅 17:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69578">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=Z8dg-Qx0OSbSFlT9LFhE0AYm6Py9IIbJbqPLnY4ORoENUS59po2so73tCinX_CfTzRbFQ0DIu7bAXgxD92Nry5C7mjYfPVlLClwqpcXbtPpCMMl8VPhlvhs8MY2I9Nf209WRECM7YidR5Kw6XCEElzOlO1DPV8gLdCF_KaYc6vuln3LzVVUNeRBD8BrAciTeo05Q1GAHA-nqevKTCUEnZUb6g7WJg5gsFrWuLH_-KX5z3dXWPSifQO5vT5qjT6y08f6pD77pqZnTodiDNvpkzYYTwgvaSLTOie6OW2ynUlv4OkUyc9V37qdV1GTkolOfDDBvtjqfm2UcvvFxJ1WZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=Z8dg-Qx0OSbSFlT9LFhE0AYm6Py9IIbJbqPLnY4ORoENUS59po2so73tCinX_CfTzRbFQ0DIu7bAXgxD92Nry5C7mjYfPVlLClwqpcXbtPpCMMl8VPhlvhs8MY2I9Nf209WRECM7YidR5Kw6XCEElzOlO1DPV8gLdCF_KaYc6vuln3LzVVUNeRBD8BrAciTeo05Q1GAHA-nqevKTCUEnZUb6g7WJg5gsFrWuLH_-KX5z3dXWPSifQO5vT5qjT6y08f6pD77pqZnTodiDNvpkzYYTwgvaSLTOie6OW2ynUlv4OkUyc9V37qdV1GTkolOfDDBvtjqfm2UcvvFxJ1WZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
توی مراسمات اربعین امسال آهوی ایرانی کباب کردن و به زائرین دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69578" target="_blank">📅 16:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69577">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu2t8zjQ699wLlxessi_d8uj-0P7Q84GicATwCZDgeLDuPZurMdZQ08ErbJJWGiFikXSgX8e9lNmFvEZ5Aiqg5TlKZ3yPENSLZl_WbWaLP7LRFEcmpfiW4RX5ck7N3sD5nEt0ktwPijyHvNorm_FIjZJ7KPbHUHvNKMfKwGn6iz-cMJhABd5JtgA7cGtAVABKFut8IqiwROtMhuwW-AHkQhhzJ3Q6n1b1HC5gLisb1id7wMIPk9ZzUY3S6ZX6X1q0ey4jo79FJGikHiKyZ_emU3MfGhbZyoRTjxtfSqjNZLBPOaTk1BTx3m209liR8-nTswSnBdic0Hab333N0Tt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛ ارتش اسرائیل برای شهرک المنصوری در جنوب لبنان هشدار تخلیه صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69577" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69576">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66218d020e.mp4?token=ml2PrSx-0DZIjlXhT3z0o7URLgv-771a1UXxNa-IL4XsVf1ZXcJ1r-GZb5F2NQ_vcBzQzJnDnXzK3N-_VfJTxZQxqG1VwuqgVPOjq7pIWg7kufasSlcjUUzMRB1ZOj1rfAKZlqZgPpPguUApFDfNQpCsVtLIr9ZbyEUnu-5jInhRzB-Yq3A0AQWWzUI8ONww2zS5BsgfPMQjdduaMYw05PNVZ7PhbArxCW9uUxQ1Tb56PI3aeSYwK6gKeqKr2NitWdKvs2tknJalWajViSI7hiqGkEWQnTkHkQinRZ_-nTMDEPrK3Xmi3kvqPI-Hdf7EX_svG4ykb_3NuswwwpHcXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66218d020e.mp4?token=ml2PrSx-0DZIjlXhT3z0o7URLgv-771a1UXxNa-IL4XsVf1ZXcJ1r-GZb5F2NQ_vcBzQzJnDnXzK3N-_VfJTxZQxqG1VwuqgVPOjq7pIWg7kufasSlcjUUzMRB1ZOj1rfAKZlqZgPpPguUApFDfNQpCsVtLIr9ZbyEUnu-5jInhRzB-Yq3A0AQWWzUI8ONww2zS5BsgfPMQjdduaMYw05PNVZ7PhbArxCW9uUxQ1Tb56PI3aeSYwK6gKeqKr2NitWdKvs2tknJalWajViSI7hiqGkEWQnTkHkQinRZ_-nTMDEPrK3Xmi3kvqPI-Hdf7EX_svG4ykb_3NuswwwpHcXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وزارت دفاع روسیه تصاویری از حملات پهپادهای جت‌سوار گران-۴ به سه کشتی باربری در دریای سیاه غربی منتشر کرد.
وزارت دفاع روسیه ادعا می‌کند که این کشتی‌ها تجهیزات مقصد ارتش اوکراین را حمل می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69576" target="_blank">📅 16:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69575">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474cba356d.mp4?token=f_RSnj2iP326U5dXMUV-51ERONSboqSfR1s-nPOHj_DxXuTDAJUtOdyANJZtQXs-2HPvE3PFqzNo9Lu-n8QYH5TlBEMnEytvazVKNGbGfbi6J3UpeCYn-eXhP4KnoRvgQYzOz6qTCZvPTO7WkZOXTQXFcVtz0JRg7xdZmxC6o1hoXxV29mP8XzB2Ze5QO8vX-Ofe4xtoPyJsfEiY-J6VvxHVsOm1tzm1t-QIZlrivFNkdYqtIYlw3VTjOGeaGTS5l1Kjwf6JUDu07d-ydl6zEWObMN8VFT6Vdo3QoSojWEzklIjsfjKIPdzai0J7KgMIcoiHbEH8Si4DI0g8bnFl4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474cba356d.mp4?token=f_RSnj2iP326U5dXMUV-51ERONSboqSfR1s-nPOHj_DxXuTDAJUtOdyANJZtQXs-2HPvE3PFqzNo9Lu-n8QYH5TlBEMnEytvazVKNGbGfbi6J3UpeCYn-eXhP4KnoRvgQYzOz6qTCZvPTO7WkZOXTQXFcVtz0JRg7xdZmxC6o1hoXxV29mP8XzB2Ze5QO8vX-Ofe4xtoPyJsfEiY-J6VvxHVsOm1tzm1t-QIZlrivFNkdYqtIYlw3VTjOGeaGTS5l1Kjwf6JUDu07d-ydl6zEWObMN8VFT6Vdo3QoSojWEzklIjsfjKIPdzai0J7KgMIcoiHbEH8Si4DI0g8bnFl4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی صداوسیما خبر کشته شدن ترامپ رو تمرین کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69575" target="_blank">📅 16:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69574">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd7b_blE597c9V18S60V6KV18xaU2tgBsAhcL1z7icMSs-GIV1gfKogNqtbAHYj6JcFof4Gv21k_OWNiLjpHFIhfeZT7MDWTf7XXCOikGYEJ44tcSigW2b-dxVyqfmNwz229h2338vSfbH5Gcq1xSNTnYctxWV5ozx3U1Pt2hPMsV8OKykWuyYwGlc8kIzbF-qCm4WyRxDmace9hy3bOg8_rwZcM6HNfZ1Fg8Y62YneND2LnFdKuuUWYm15iJsIjiMd_sTRnob_GKfSgsOdvzjcR9AFpK_eJMsnPzmmBC-2iAK4q-3wRiZiyOTCX4PvZhXR4fvn7Uze5wNQRxP78fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💢
📉
قیمت نفت با کاهش های پی در پی به ۷۶ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69574" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69571">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqXC0b22XjlDhzWHAASMitc0FIlfUu7N2cMsZvX0F4SZSIhm7_CrfTZOvgGMfXnAmw1Mx0LoqtAC_Ez8ZOHZU7TIfYqUK3DdJN_lLAUQ9_GWHh1jp3dEDHbfGEjZwhaGMlBB5fDXYFGJIDVB3i26Y3mWJ_DaASeHXWvsMRw4AdYIyhDoI2BNmkPLX0GxDIw5e8xinLYKSSrF0Nr2FbWjaHSY1ublWHjzjN-sieAuqBmz-70l39On8ly_sNLtrB04i1SyWChQgU-7iyZOVSKIh2mJW7f365R-tknJjgcMUo5Q5xVkPOQDW59V9UFXMFBtbHvZg1HhBaWvpKQ9n-yBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q177bzmUaAbbQ9U-sERREHRwvhXz4ZDpONDivU_OsEg_NrYATL1C0MwN7vYH3idtQWbKcAqdHfINxMcfcYsgkqWm_HepLpDw82-NW20AJ9a5Gkb8tKg9LG_Wsog4SgVwdulpDuqzbjk6xSVi_8V80yNbNoO4a2K21YXmI5eWXP2ZhsoNUBzwaOExj7uDd3gsdiOF4lxlfSZrrBhe_SzeM0tlDOWHQuIZSCr3gJqwnNbJoKOHp5uIrc1RHRgAiV1QiIWoON2X0vb88h3lBdnv5cf7OQ_ym8DiWL4QBlMzKKkzrOngfVaXnyTTSiN7Yp7XiAjIx1Ul9OSCsAz3mKYJLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NePd2AjrG-qIKCOGEwSRRJRBu8QPtCXKTg4Jr5xd-M6Al2hvwDNX_KJhsRUYgOP8lPq20xSjliPUH6R3r2mavzA3uHPQWlWiIbOziLmdg3MU65s01bBES8PdA-RlVKKIj9mhZPt0YdpkIPQebwRSo_8H7X1YdHL3-B_4t8EpFUWld94wWP-jENr_-aIvxqaWXPIFKojew1wGpCUUCaH2LII7m_XBcdQOgaHv_0r6XNAnhJLYVnM-OJq0NQb8W70dbbzjo6wnECG-xTuNNJSq8bxuX-vffIRjvyEKXSX1ZGFNThYrgJu2B7kSx6lvqW_yzfT2i4TL5w7siqgbFTgPzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
پست جدید و لاتی کریس رونالدو؛
"
اسباب بازی‌هام
"
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69571" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69570">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhK75q50Te0I-WOm_jBxJ5kce795u2l-mgemADFp8l-CUr7d1oyNUGGERUv_tt8Kb3h9GCsevBzkIE1UL8luLMPKkG_41hP26EVkoU9FTBDiy7-eXSQuOAhOQpC6Ovbd2mQJHHbX0aCQGhqD4QJOsM7yhgOEnMPr5mVUxuSK4FXwL1TW8PoFjMI08cOJINL962WcrteNJS_sv0v2OM01TrPYr_wrbJ2Z0hXqx3mhNY2jpIer3p8pPH-u9WH8qAjRPJswV_qF3ESEAwbjktuSJa2mITuR5Vssd4vh8KLa3aoui3JhmyqfXXUMeiBm_vm9UR5PS975jkqT8otft9sSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دسته‌ جدیدی از سوخت رسان ها برای مذاکره وارد اسرائیل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69570" target="_blank">📅 14:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69569">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db3cnonA-aY3BBQ-RTrETMfG_Pb2Z2pS4P6NAkg2UrswauH9cakLKHhJSf2L4DsoJmXIMt7Ws8y0Yck9jCroTPb1nPvPTxeBKfQozhhGSX6FUj2WMzAKmAhSUGlLWyXZuVp8B-g1ooH34eRX8VppN77TvYAh13dwNSe4cw2ds9xwNNF6DtyX3ROcTD1Ao1-6m03qggxuDdAy5btdZ9n06aW_ieldvBYoduR0IO_qDwjFjEHHewjP1Xz0pwoBj4p-_qoHM7GylzY8M5JDgksTMZChzCjaPzL4rW3q5yJJAGCDl5iLbdml46geB170ySNLIE9QMT5ybOlZHkLVi2Z19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
❌
حمله هوایی ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69569" target="_blank">📅 13:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69568">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=j5y7JDSbRIrjWznonCRx63zZgN6JwdDjwHZ5B8zNh1YMNet2chFXNDyeOMd5cMQCLMVh0N1f95lgfgbUojQyC9jvh5pgGIGX75_iQfboiLIgnlQa0euPNLHqf0JUy8cIGWMrDRfi5PPKmyStfatAJSbNimGXZU-2EEPCFAVFhLAnyz4XMz3VfrpuQcuyc1pciWUCOSDGQsl_p5dhEzXXqVZh1XyGRjqjNmJ9rdZQ64pwXfWXhWELby_Zjt5bJ5fUs6iLjOJ3f1HiwSej7gaITKESyMCDCxeBMR8OfI-6VjfaFV66-yGN21gpx4E6_lfpEc-S4kPOywbMInOtsrxgXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=j5y7JDSbRIrjWznonCRx63zZgN6JwdDjwHZ5B8zNh1YMNet2chFXNDyeOMd5cMQCLMVh0N1f95lgfgbUojQyC9jvh5pgGIGX75_iQfboiLIgnlQa0euPNLHqf0JUy8cIGWMrDRfi5PPKmyStfatAJSbNimGXZU-2EEPCFAVFhLAnyz4XMz3VfrpuQcuyc1pciWUCOSDGQsl_p5dhEzXXqVZh1XyGRjqjNmJ9rdZQ64pwXfWXhWELby_Zjt5bJ5fUs6iLjOJ3f1HiwSej7gaITKESyMCDCxeBMR8OfI-6VjfaFV66-yGN21gpx4E6_lfpEc-S4kPOywbMInOtsrxgXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
دیروز طی یه مراسم تو روسیه، یه چترباز از هواپیما پرید پایین ولی چترش باز نشد و سقوط کرد و درجا مُرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69568" target="_blank">📅 13:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69567">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phgihB6RglSJEha4QerpHlyF7p4wA69xQj7mxULcANw9pyKATSBWbsUgQDwymmPuLRNMWL5WCUfIUW0h1zdefrJSnIIv3TDs4BbCNiryvZqhaBPnyVfCQNlfK4ZZ2SRLDAcO36FoG5lw1NeKFbaYhmSsF7QxGb9DR-ZKxWx5JAz3NdRi7cvjrvaD-7Bab_8yT2FLsfqa7cXx-woF7M0ooZCWF01otCxDTjBTjD2d05lFirweHToUSNCEffFaFxu-1XivNwfR6yEl9UWc4oj333htIwmiuiHW2wLdOPgJx1Fp6C9nGemcqBoIVKsHiW2QAXZzqSBpvu9X5JJYlMTfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دونالد ترامپ تصویری با هوش مصنوعی از خود منتشر کرد که در آن با لباس نظامی در کنار ژنرال پتن و ژنرال مک‌آرتور دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69567" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69566">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=LGcZOONBYTnbLzFwfeB7G6rmAhhxoTQpKExgZ0oNY9wgacToIDTzFLmGQF2Mpx0kDKrWf4gmy4DUfnt_puedoLl4stAO8FxdmTAf-AlUOY_PozX7f7qOzUC-NFvya8YgfYK7MfTNIYmo_6Pevg9QFnZMBmriRDSlR3iBM3QQWTBs4R1VsmtV253jpDohTXFjRc3j55LzrlpkUtRHbq8WDwRT2P8YllBrbzP-HxYgTKCiLiIyFbxUnoAESHmY4HD1w9cF3pNfoYHJELRvxEW0tXqw0cYV-B7Ha3W07vKzj1n0jkDgwRZrKIduaZ1iEkIov3pzwVQ1arE_VTsQKDm1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=LGcZOONBYTnbLzFwfeB7G6rmAhhxoTQpKExgZ0oNY9wgacToIDTzFLmGQF2Mpx0kDKrWf4gmy4DUfnt_puedoLl4stAO8FxdmTAf-AlUOY_PozX7f7qOzUC-NFvya8YgfYK7MfTNIYmo_6Pevg9QFnZMBmriRDSlR3iBM3QQWTBs4R1VsmtV253jpDohTXFjRc3j55LzrlpkUtRHbq8WDwRT2P8YllBrbzP-HxYgTKCiLiIyFbxUnoAESHmY4HD1w9cF3pNfoYHJELRvxEW0tXqw0cYV-B7Ha3W07vKzj1n0jkDgwRZrKIduaZ1iEkIov3pzwVQ1arE_VTsQKDm1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره ایران:
خب، اگر دوباره پا پس بکشند، ضربه بسیار سختی خواهند خورد. آن‌ها این را می‌دانند؛ آن‌ها این موضوع را درک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69566" target="_blank">📅 12:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69565">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=XWIVcwqWRPDuEwRob2pN-TYfie4qpE13N_NYET9sRyJCePjOn_O3DndQRK7AXiD6qq9nJuI_PQ_L0oke5ANfY_9ruZBoUTIIf29-qxjUAEXPt7CiKlt-G422XnW5oxG71Y6iBhheYr3KljBCkZmGxoIDHdOaR9QumPe7e_9I2DeiExxXlIxgR-Lm1eG4EXqoDCz2cbGv_jD-A5Tuc4uqUtSDFb3KGnDGaMcPWVeZYRucnvE9DpI6t_DuCPLW61lvXIZm5TahLdKQq2VELD7pXuGTJYeGudPhnOnvOj197b5VMrzT0m_U4s_QhiEsRdqgqq0kMH_dN8E7-_ji0wmLGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=XWIVcwqWRPDuEwRob2pN-TYfie4qpE13N_NYET9sRyJCePjOn_O3DndQRK7AXiD6qq9nJuI_PQ_L0oke5ANfY_9ruZBoUTIIf29-qxjUAEXPt7CiKlt-G422XnW5oxG71Y6iBhheYr3KljBCkZmGxoIDHdOaR9QumPe7e_9I2DeiExxXlIxgR-Lm1eG4EXqoDCz2cbGv_jD-A5Tuc4uqUtSDFb3KGnDGaMcPWVeZYRucnvE9DpI6t_DuCPLW61lvXIZm5TahLdKQq2VELD7pXuGTJYeGudPhnOnvOj197b5VMrzT0m_U4s_QhiEsRdqgqq0kMH_dN8E7-_ji0wmLGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فریادهای مجری کشمیری(هند)صداوسیما درباره تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69565" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69564">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69564" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69563">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoUC7Nr72cbFM3f1p-UCG20K_XicwfYhKgR8hKnPz6QJ-MPf3GyS4w8HRDL1mPx57AVXvykj7j7pHl_V8YNBB7XZIhZQCOUy7icqMpXkyZXOJdyKDub2F2xq-P7xYzH5QibjUcf8fLl2M2P8qWfjclFfIyIzwDN1VKOu9w_EGd05T6XVW-bd_vYHKxP2bH4xDZGHQq-OtoUHBu_7mxesPM12eWSGrjx52M1bSLFo5LNkzBz0yoU2YhiK7TKn85cfzo8dvsDVaqJ34aV46KVm3SO0MR_ORuiNr6Vp3_S_AlMjtqYOaEdduszIi-n1S_WxVIaSMR3bE6Vx85Rc20NkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69563" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69562">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=gEaNg3PNy9RWfRpqRCHes4ImAjT3A2FFxp3Amx4xiOI0SjJF41JoG1h1OwzIoODJVZCWmDTiIf1upYQFqkhfqCOgb3q4X5zt6NaIfBhWe8V3QdFwJkkyI4fyZqUQnFTiSucdafl3HgdA_So_GQ6QWIUH1wgMeZD9fzDxwCH8MIbTS3LzDwA8_F4d2hScRicQG3-0j4i8jgLJBkdF5-21tk0nJ_XeMqIiQqlGSiVBTwsb7gfb0tl_Oon-1A057-Ca0jrRFMyGkjxvgOtASHhq6vD7B6d_zPT-tyZE0sPwh6h_v6GKDD0bSHSbCFwPJ1u-WMWvl2WyeoIc7MacAIwAAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=gEaNg3PNy9RWfRpqRCHes4ImAjT3A2FFxp3Amx4xiOI0SjJF41JoG1h1OwzIoODJVZCWmDTiIf1upYQFqkhfqCOgb3q4X5zt6NaIfBhWe8V3QdFwJkkyI4fyZqUQnFTiSucdafl3HgdA_So_GQ6QWIUH1wgMeZD9fzDxwCH8MIbTS3LzDwA8_F4d2hScRicQG3-0j4i8jgLJBkdF5-21tk0nJ_XeMqIiQqlGSiVBTwsb7gfb0tl_Oon-1A057-Ca0jrRFMyGkjxvgOtASHhq6vD7B6d_zPT-tyZE0sPwh6h_v6GKDD0bSHSbCFwPJ1u-WMWvl2WyeoIc7MacAIwAAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی :
به عنوان یک سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن. چون ما داریم در کنار آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم. این شرایط گذراست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69562" target="_blank">📅 11:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69561">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=rXEe1-ilUrdTPuKkxUg1rnhycnMfErMf7bQ5cBmg9EZeTVDGm5sjae0oC2aeiVmRNBU-vooX3CnRsCmBSElTmBMft_dA1CxmaBXov8aLOX5yBSo34bqejA5bVk0ug_ZbfDZFkjN2uL0-a9YnMhDkvHGZchYjwdHhMHUQNbmPWK66Bipt4r6P_fZXiG4je9cAMNSEog1aBpic9MzLxYqmvSDthdqrpgC-tybK06thNjTTFz1KFVoLfr22jXFQt16L04h9qK63SPW6m2W9LLthNI5aNmffvJTqavZmcHEOwg---fLK3PptonZJc1E0RDcf25uKsFMqNhFa8vtvhp8ZlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=rXEe1-ilUrdTPuKkxUg1rnhycnMfErMf7bQ5cBmg9EZeTVDGm5sjae0oC2aeiVmRNBU-vooX3CnRsCmBSElTmBMft_dA1CxmaBXov8aLOX5yBSo34bqejA5bVk0ug_ZbfDZFkjN2uL0-a9YnMhDkvHGZchYjwdHhMHUQNbmPWK66Bipt4r6P_fZXiG4je9cAMNSEog1aBpic9MzLxYqmvSDthdqrpgC-tybK06thNjTTFz1KFVoLfr22jXFQt16L04h9qK63SPW6m2W9LLthNI5aNmffvJTqavZmcHEOwg---fLK3PptonZJc1E0RDcf25uKsFMqNhFa8vtvhp8ZlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکیه دلقک:
تا ۴۸ ساعت آینده خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69561" target="_blank">📅 11:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69559">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QfTcTK8NQB3BUkgA2TTkymG-SlWGfMLiZ0INtMfsj19S3p-cHpWS7TvD1r9rrAxSDJYbCSwcQxfhc-Nx2GAkwpIlDJ9Fe3DR-uiKLAaD48pV1LUmfi7UILqndXGm4c4F25_VuyPZkkO958I5wdmV4dpyDF5-7Xg-72IfLJTfYOab5-Q3Vu-SM1VL36XQ2qHuEzBQAlVgYkQjtTaI09XGd0N9MAF255ySKvskleiy48SqVoE4x-Gz53k9Z1tMHlVTnxg_auVfFxYtrai-zTZ_T_bldyYXU9hT3_Qjesuofe9fkHCuM4XimqAyM7oprEiS4lXLrLtgvVgDXIwBE78Abw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=gp2QHTlq6AeWUl9NizQb6SHNb_1WNI_QyaNUP-gNajZ8tI6I6x0wdXr3QOdxglKSHqzKk7mCaffsJPFZ5UXsEWC_IooKZ-rDOYlnHm-dr_M5FaDNk3I38VCTu2NTQDK7mJcm3QvrBbjGr1UyR_Ig3t1zBA5x7TcWwbiH-jP0F4lDQ4hEiiblBrfLig_VdreppNAXQ1JPh_d2Cd3DQENlvg7xwfyawLVTuAcE6r_gEZtsUdHLFlL2s2tla2ROMEckKMmC9YFEjFe8zVDlpUIn3MLx8660IpIrzIzgkCjzqjs8smO2phN9Q7Mfqfkc9PvcpM47_UF_DyznB0F04F0Skw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=gp2QHTlq6AeWUl9NizQb6SHNb_1WNI_QyaNUP-gNajZ8tI6I6x0wdXr3QOdxglKSHqzKk7mCaffsJPFZ5UXsEWC_IooKZ-rDOYlnHm-dr_M5FaDNk3I38VCTu2NTQDK7mJcm3QvrBbjGr1UyR_Ig3t1zBA5x7TcWwbiH-jP0F4lDQ4hEiiblBrfLig_VdreppNAXQ1JPh_d2Cd3DQENlvg7xwfyawLVTuAcE6r_gEZtsUdHLFlL2s2tla2ROMEckKMmC9YFEjFe8zVDlpUIn3MLx8660IpIrzIzgkCjzqjs8smO2phN9Q7Mfqfkc9PvcpM47_UF_DyznB0F04F0Skw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
🇮🇷
جمهوری اسلامی دریای خزر رو فروخت رفت!
در تازه‌ترین قرارداد، جمهوری اسلامی دریای خزر رو تقدیم روسیه کرده و یواشکی دارن میبرن مجلس و تصویبش کنن.
سهم ایران فقط به ۱۱ درصد رسیده! شما ایران رو فروختین و شرمتون میاد بیاین به مردم بگین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69559" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69558">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=Rs7Mf07iPDhPp6vWux9ka23v2BC0KC0qA1hvNkgzd2pmFYWQhnOIYss3Xzn6abClXS3UMZhN9yxCcyoPUDc8vYggqigxSaioryIB5JzNYBK4gFWW5ftEXAn87yHU4AOKN5lU5N7vbVP9ucafsyFHt7OZHi7gA6NupsYsapcdmrEZ2mS7Tl8BsBbS3UDV23kESG0VRlhZOO6nhuqg9-SCdunz-A22Zt6hNeAyMWpxl3YCBFZg-SRGqK4V0kROgbKt4IcTe8wzdPioomzWuCH3L8_PZh-9fDuwxYtRWPMXe0VDAHfmMPdPoHgRp407T3Xn4ZbmMTqosQ5BHBFwopkByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=Rs7Mf07iPDhPp6vWux9ka23v2BC0KC0qA1hvNkgzd2pmFYWQhnOIYss3Xzn6abClXS3UMZhN9yxCcyoPUDc8vYggqigxSaioryIB5JzNYBK4gFWW5ftEXAn87yHU4AOKN5lU5N7vbVP9ucafsyFHt7OZHi7gA6NupsYsapcdmrEZ2mS7Tl8BsBbS3UDV23kESG0VRlhZOO6nhuqg9-SCdunz-A22Zt6hNeAyMWpxl3YCBFZg-SRGqK4V0kROgbKt4IcTe8wzdPioomzWuCH3L8_PZh-9fDuwxYtRWPMXe0VDAHfmMPdPoHgRp407T3Xn4ZbmMTqosQ5BHBFwopkByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پرزیدنت سابق، جورج بوشِ پسر:
مذاکره با قاتلان، گزینه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69558" target="_blank">📅 10:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69557">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2egpaRJ0JMfcWh8KKtrnOLEit8Uqqd7mIORa3gOIK2u0TR3nzWcPLPfaz9YLxBQzFN2aKeDXp3iV8JKpmrBdYGPtImsmVCiWsRVjnnrkGRL8rba-eECTyhP52wGZKAPibgm7FtGb2kH8BJbRXwHFBYDMeSOQdD_O8-3Bn4Q3Bpwn2vtINERI1LK2TkYy7vk2itqvMTyoZh-1p7iyJ-BEoJ4Phpp5SmwncCGkcmIWeGo6vCyrM5QwWA_uz6lVw55ohqpmhCZHnNV2_TUP4kScLwATkb1EuELDFrH937YLDt7g9UxcL3ynpEwbfxYWZybc3b2mmaoewkkJm79fOlmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
🔝
بر اساس گزارش آکسیوس، آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و احتمال دارد این توافق روز چهارشنبه از سوی آمریکا اعلام شود.
🔴
مفاد اصلی توافق:
- کشتی‌های ورودی از مسیر شمالی در آب‌های ایران تردد می‌کنند.
- کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان و با هماهنگی ایران عبور خواهند کرد.
- برای عبور کشتی‌ها هیچ عوارض یا هزینه‌ای دریافت نخواهد شد.
- مین‌های دریایی در مسیر مرکزی ظرف ۳۰ روز پاکسازی می‌شوند و سپس این مسیر برای تردد دوطرفه باز خواهد شد.
- پس از این دوره، عمان و ایران درباره یک توافق دائمی مذاکره خواهند کرد.
همچنین قطر، پاکستان و عربستان سعودی در میانجی‌گری نقش داشته‌اند و کاخ سفید نیز مستقیماً در مذاکرات مشارکت کرده است.
طبق این گزارش، عباس عراقچی با این توافق به‌صورت اصولی موافقت کرده بود، اما تأیید نهایی باید از سوی رهبری جمهوری اسلامی و شورای عالی امنیت ملی انجام می‌شد. یک مقام آمریکایی و یک منبع منطقه‌ای نیز مدعی شده‌اند که این تأیید روز سه‌شنبه نهایی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69557" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69556">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6lZNqvUZ-Igw11S9rZqF5UX6LCMulTMG0WnLszgNDNw7vDkxCa4vvFBRzTAJO0RxyrHzHYWvGZEji0wOsaqnK5-4XVNP0qnq5s2qJ1UtPTNQ-W9-dTR8Ja6nBO_eqHW5CvYUeQRXpFF_ezdWaS1HL9DuTp2GZTaMfthEOomo2BPe-PGbTujMIhyZSCwgxd2Wu2ueeNKB7JebeTyX_9XMccBdhQLN2W8ARYebHd9SPv-3yge_v0ZNqQKstBcnyE__w8D1fek9m9SKKp5EPbkmDTXHIGAGfNxSNb15mUYH-fBSJohEEZmcqSZSo1-5U9dxPaVnPEzRD_ael4NdXn5qpDY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6lZNqvUZ-Igw11S9rZqF5UX6LCMulTMG0WnLszgNDNw7vDkxCa4vvFBRzTAJO0RxyrHzHYWvGZEji0wOsaqnK5-4XVNP0qnq5s2qJ1UtPTNQ-W9-dTR8Ja6nBO_eqHW5CvYUeQRXpFF_ezdWaS1HL9DuTp2GZTaMfthEOomo2BPe-PGbTujMIhyZSCwgxd2Wu2ueeNKB7JebeTyX_9XMccBdhQLN2W8ARYebHd9SPv-3yge_v0ZNqQKstBcnyE__w8D1fek9m9SKKp5EPbkmDTXHIGAGfNxSNb15mUYH-fBSJohEEZmcqSZSo1-5U9dxPaVnPEzRD_ael4NdXn5qpDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
تنگه به زودی باز میشه یا ضربه شدیدی بهشون وارد میشه ک باز کنن
اونا با من مودبانه تماس گرفتن گفتن میتونیم صحبت بکنیم؟
ضربه سخت ایران تو راهه ولی قدری دردناکه نمیخام ازش استفاده بکنم
خیلی بحث هایی خوبی داریم ولی اونا نمیخان اعتراف کنن چون یکم نگرانن
شما میگین مذاکرات فوق العاده داریم ولی اونا میگن دروغ میگین
اونا میخان معامله بکنن و بشدت خواهان توافق هستن
در عرض ۴۸ ساعت خواهیم دید چه خواهد شد
قیمت نفت و گاز دیوونه وار میاد پایین چون سه شنبه مذاکرات فوق العاده داشتیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69556" target="_blank">📅 09:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69555">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d290294320.mp4?token=Jub2NZXfX9lTtHDhKq0O4PYiAAHjKmGA8pyhEz2rgZCTeKn73JP4xjjeaM7lxsTl5KHocKKKz8WFZgxoHJ1egEr9QlClblxYxVsrgz7rqmZpEmc1LrfjbMmExsC9htxkfKSpLai1uailuXlmrLEiObEU8V64KcyED-avaX1o5Rdp6NNltJ-6J09oQFBebzktwVhrE8WVA4DEVT1cNL8eep5r6lu58-XyXPejyUKlc0lhZHFkjcOzofc6UV4JYPNmHHKFxw42jYoLnUR3_O-FGeYuTPbKoXYIvW7R6gdIu79loEGUb20xSbCRn8VSdU2ieYl-Ye4kE3drqTp5nGCkqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d290294320.mp4?token=Jub2NZXfX9lTtHDhKq0O4PYiAAHjKmGA8pyhEz2rgZCTeKn73JP4xjjeaM7lxsTl5KHocKKKz8WFZgxoHJ1egEr9QlClblxYxVsrgz7rqmZpEmc1LrfjbMmExsC9htxkfKSpLai1uailuXlmrLEiObEU8V64KcyED-avaX1o5Rdp6NNltJ-6J09oQFBebzktwVhrE8WVA4DEVT1cNL8eep5r6lu58-XyXPejyUKlc0lhZHFkjcOzofc6UV4JYPNmHHKFxw42jYoLnUR3_O-FGeYuTPbKoXYIvW7R6gdIu79loEGUb20xSbCRn8VSdU2ieYl-Ye4kE3drqTp5nGCkqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اینترنشنال:پزشکیان و مجتبی خامنه ای باهم دیدار داشتن و این دیدار تو یه ماشین بوده
؛
مجتبی خامنه ای صندلی عقب ماشین نشسته و تو یک مکان نامعلوم و پزشکیان صندلی جلو نشسته و حق نداشته عقب رو نگاه کنه فقط صداش رو شنیده
.
پزشکیان از مکان هم بی خبر بود فقط برده بودن ببینه اونو.
پزشکیان قرار بود از فرماندهان سپاه از جمله وحیدی بهش اعتراض بکنه که زیاد در دولت دخالت میکنه.
مجتبی اجازه مذاکرات رو بهش میگه ولی با هماهنگی سپاه پاسداران.
پزشکیان کلی مشکلات اقتصادی رو بهش میگه و میگه که اینطور بره ورشکست میشه دولت.
پزشکیان از این دیدار خسته میشه و میگه میخام مجتبی رو ببینم ولی به هیچ وجه اجازه دیدن رو بهش نمیدن.
پزشکیان که فوقش یه ساعت میشد فقط صدا می‌شنید چهره ای از مجتبی ندیده بود.
پزشکیان اصلا از این کار رضایت پیدا نمیکنه وبه رئیس دفتر اعتراض میکنه.
میگه این کار جز خورد و حقیر کردن من نتیجه ای نداره .
بدجور عصبانی میشه و جلسه خیلی کوتاه تموم میشه.
تصمیم استعفا از این جلسه شروع میشه چون پزشکیان احساس میکنه دیگه قدرتی نداره توی اداره کشور.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69555" target="_blank">📅 09:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69554">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=OJZMAC1HJewufDG6dlfS_dmNn9nOBcH-ExwWX0adhefrD-BbOAtr5hMzZS5g6wuavRM1dA5x_lO7hxgFSMVP-Uh19mWS86_DvhwP18noh14CUj3O7Dj1zMi576OLcg_8cEgFRsvgWMKgFJk5NHwagI9-9NeZ1RZmSJpZH2jBgH3t8Y5eC9URd3lE_QYAjDBIJpdvHvNBeNiuvqq5x7-zO64F-tZr20pvx1Lh2MHsF_mvytG9A87Qyb4iiLnUGH9-SoQwuhdvacol9kfi5A089ByycG_8GeXXAksbhUSC_PElQwlwkQ7VKPxzsQqQ6th-oSBgixJCkYJQQVCsBdDbwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=OJZMAC1HJewufDG6dlfS_dmNn9nOBcH-ExwWX0adhefrD-BbOAtr5hMzZS5g6wuavRM1dA5x_lO7hxgFSMVP-Uh19mWS86_DvhwP18noh14CUj3O7Dj1zMi576OLcg_8cEgFRsvgWMKgFJk5NHwagI9-9NeZ1RZmSJpZH2jBgH3t8Y5eC9URd3lE_QYAjDBIJpdvHvNBeNiuvqq5x7-zO64F-tZr20pvx1Lh2MHsF_mvytG9A87Qyb4iiLnUGH9-SoQwuhdvacol9kfi5A089ByycG_8GeXXAksbhUSC_PElQwlwkQ7VKPxzsQqQ6th-oSBgixJCkYJQQVCsBdDbwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازم ترامپ از ترور جون سالم به در برد:
⏺
فاکس نیوز؛
مقامات اعلام کردند که یک مظنون مسلح به نام «جنین جان تائله»، ۳۸ ساله، در زمین گلف «ترامپ نشنال» دستگیر شده است؛ وی متهم است که پیش از سفر رئیس‌جمهور ترامپ، تدابیر امنیتی را زیر نظر داشته است.
پلیس اعلام کرد که متعاقباً از منزل این فرد، یک قبضه تفنگ مدل AR که به‌طور غیرقانونی تغییر یافته بود، جلیقه ضدگلوله، خشاب‌هایی با ظرفیت بالا، مهمات و دفترچه‌هایی حاوی «مطالب نگران‌کننده» کشف و ضبط کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69554" target="_blank">📅 02:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69553">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش پر حاشیه در آستانه پرسپولیسی شدددددن  https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69553" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69552">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pljd01XEdrcGZ---Rrm6xWGIhGK7fIBVZ_tIaautCTsap9XOBHWnsxpV0IPWvc-LzfOTRixFNyDEkn2Z8ROt23iDetg6uX2kYTDjQHV1PH6g_XRWRuoWrD6z3CRXQbc2_V5sZICViVnKjp1FwoiYFezg5ZXofLCLCP5ImKHbDbIyVmwNlOVcO7vjkUlNdaf9kzxgc-CImTvh0v65UFeZ57Yh-fAUJDPskAxUlGB_70sVc7PNn-orK6a_OktGgznWhytn_nKiJxnJVBdx3w-oQ_W3DknlhyQ4fDlFValJeiWhRSJLGv7y1nnbClXtaloJjndaF59gQ6i7V3gzdc9hLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و پرسپولیس هنوز هم شانس رسیدن به هم را دارند!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69552" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69551">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3zAu8Djl48Doy3-bAX-c9h2bs5awPB5V_aO2m7jd6rPemKfMBMv8MdG1Qng93N64Y2dh6w0vmG5TfCw7cnrsfw1RVHsEOIT2UamvlBBomPa_csZf8krcP-85ckNP8dPGAufaQx2J0PM2YtGnXuT0fYEGUkCqTFaP600BZGsd-Be1aaEMcyWJsq_5WsD_fr_BtSbrobQOtnpCpXfz-5f9YP-duKgwEiU14dIMkmcqMmtLOr90fGoJ5q3xzZQKnj4b11qa3BPr_D85z66yqOJxYNwYJeIFX0zprTNIacf7Q1NkWBWnShaSpptmCCPDsTWZBKHVZ-jIU2Q3GyYNFdiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیزارم اینو یادتون بره
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69551" target="_blank">📅 02:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69548">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbhQe-VJvt1zXWk_s3XHUKjGqg6It45aBEDkXg3RDo6-AWA4Zn3yGc3UazNVYLCruaa1S5DkqqkL3Ub75Sb0EgRBwetYhqtzjaGQFiY6KwSkjtk_YB2e3pVk147Up8pu8YVumrxh2a0tkdlb05Pr75UKiHnsP9e7cilhGJJRMYWobH25D-tgxmeCocuCZWA8I_z3WXyaw2Q-f5YGfDDCJ9fH_oL1SaE0bAmkB9wP8xcnsFX6Ms3X9PlHHSIKNAOroHc1dOuAqLAOYI7o72C1J2sKerUXwcFA4SYyN1aP3QKLLvs_yzbhxOeydPXP6x11QNio8iH3HI8prVp2H9mXeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pN8AtKu0sHvmlWX3Cc3Q6VbzsNZ8ISER2VE7KicktFJayRj1S2nBlFfjmHxzd0r8uc5UaXj4a4UjwEb4DDi-uV_42SvbMN0UyjsbeKKWDK8mEoVruib_AXnkMBNQT4rSQtBsdj4vEXgYfbYKiIydOP-Ey7oouCWf3HG-FlM73uvNtv4nutMwvyBcp4UFsKRdrHIapeT0x2FLto6PG2kFOjsJg7lOxgQE58NnBTPtgdF7AEeiDQ3Sq2AJx_rcMJQM17QnLCf7U4utNQFnpX3vehhCQMwDcoGz7FNsAqsyi-8JogGViyWJRMrQdX7Wu18ZWqrP7UuuqkanrVOzXfuggA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=h3G77l73a-d71TMABbAabxhtozjH0C2rh7utwC43V1uWVNFBI_Bdcz5xAApR0KfgILw-cpxAADXN8cmRoT4zgErR5dx1KJj2bvzfMjQI4jBKY3Hv0XqsFNSrt-z75GWB3FT8lN7p5XN_L1KmQbAEt9q3vWqxn5o8pJfzPIk4bI2k6DATLqOPR8pbERl2BItU62K7TDJWxxsSTRqRdRbjstqwBZmtnAY8sXyb0PGpRJQ0ZzHhAdgJ6VXraXzZ8Dxv4RjKSN5Rp5uHjz3dd5jzElsT832gaB38aNybSxiAvJ-18Enr2FMBLExk1pxTEhYNV6bvIqVNQGA6w6pZqKeTzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=h3G77l73a-d71TMABbAabxhtozjH0C2rh7utwC43V1uWVNFBI_Bdcz5xAApR0KfgILw-cpxAADXN8cmRoT4zgErR5dx1KJj2bvzfMjQI4jBKY3Hv0XqsFNSrt-z75GWB3FT8lN7p5XN_L1KmQbAEt9q3vWqxn5o8pJfzPIk4bI2k6DATLqOPR8pbERl2BItU62K7TDJWxxsSTRqRdRbjstqwBZmtnAY8sXyb0PGpRJQ0ZzHhAdgJ6VXraXzZ8Dxv4RjKSN5Rp5uHjz3dd5jzElsT832gaB38aNybSxiAvJ-18Enr2FMBLExk1pxTEhYNV6bvIqVNQGA6w6pZqKeTzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
حملات شدید و سنگین روسیه به کی‌یف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69548" target="_blank">📅 01:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69547">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzxd1p5jjwRYE3RMt_zeeffgiA-IzLv9_9EVtR2nzNizNRcbgLIU_pgm0EothOCQLdfvHPj48IqW180wWxzLcZ-3gynjKKuUG51WRE6zUcz4d0f3RLkn8ocZ6EnXWCzuX1oosidZk42vf8Zaf1BFz5A21UhmFBdXJ0juKSOxPFeA3s_GN9taTDcGbqy259qloJbnorCLmJ6rD5_KLCMkSqLl3PnAw_vDYL8S_FYihMYtl0m25mXBOJ0MzrPDcst7HOmqni1cQvshsQNy4fS2PQGdWkH6iOVgmGkzI-KvpyGHafMOQERc7n6Cwm-d1c5Qgn_AUYuoducktLniY9m5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
علی قلهکی:به نظر میاد یکی از گره‌های اصلی مذاکرات ایران و آمریکا، ماجرای تردد کشتی‌ها توی تنگه هرمزه و هنوز سر جزئیاتش به توافق نرسیدن.
هنوز مشخص نیست کشتی‌ها دقیقاً از کدوم مسیر باید رد بشن و مسئول امنیت و هماهنگی عبورشون کیه.
ایران می‌خواد کشتی‌ها بیشتر از مسیر آب‌های خودش عبور کنن، اما آمریکا و طرف مقابل مسیر عمان رو ترجیح میدن.
اختلاف اصلی هم روی نحوه مدیریت، امنیت و کنترل تردد کشتی‌هاست.
هر اتفاقی توی تنگه هرمز می‌تونه روی روند مذاکرات هسته‌ای هم تاثیر مستقیم بذاره.
آخرین پیشنهادی مطرح شده مطلوب ایران اینه که کشتی ها حتما مسیر ورودشون، مسیر ایرانی(شمال)باشه و مسیر خروجشون حدود ۴۰٪ کشتی‌ها از مسیر ایران و حدود ۶۰٪ از مسیر عمان (جنوبی) عبور کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69547" target="_blank">📅 01:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69546">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgRASq0EUiLdORmN-Judhmq8pffBJjLdzjd5v8ifHlT10_bfK4FZrzMBf4UbeHHAaX84jMtMV8p0pd_QZ9HV7LM1SsAUB4icHpw8q8SY--hcGY198-jkLWQ-G8t8YySlCO2ZJjG5rS7R8fFhQwBffbmdDgAJ4q9o2ea6UdlhdJqNr7JJOPavD_8VcPes_5vr9oqwKjOaz2TluUN1pRv3FZaPLhx6avD3mn_iNyKNyUmDSN1k1IBqoElGfgO3AACjJ3M2d55s9lojSLeUewz0MqLoO3INnjPYXcUmKt1QIQpyHwtTifmC73ZisAcSftnxfDstuTnvr3iixgBxxm2mWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
بازگشت غول‌های سوخت‌رسان؛ بزرگ‌ترین آرایش هوایی آمریکا از زمان جنگ خلیج فارس ۱۹۹۱.
پس از پایان جنگ جهانی دوم، جنگ خلیج فارس در سال ۱۹۹۱ با استقرار حدود ۳۰۲ فروند هواپیمای سوخت‌رسان، بزرگ‌ترین تجمع هواپیماهای سوخت‌رسان در یک عملیات نظامی به‌شمار می‌رود.
اکنون نیز در سال ۲۰۲۶، با استقرار حدود ۱۹۳ فروند هواپیمای سوخت‌رسان در منطقه برای پشتیبانی از عملیات علیه جمهوری اسلامی، یکی از بزرگ‌ترین تجمع‌های سوخت‌رسان‌های نظامی از زمان جنگ ۱۹۹۱ شکل گرفته است؛ آرایشی که در بیش از سه دهه اخیر کم‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69546" target="_blank">📅 01:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69545">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrYrkj8HiOufua8qH6BPf1xuYDux1fcPoHhggqyzVcki1ijyVTnobHq1MqrRx2iluQL8T7nzQMvUt5fvdHOdle2Gs1su7SzCew336xNP1OBmFQ2qohSjLq0rUYEE2Xf40-b6I7NJuJbkXVkfcbrzH8q2JarBOW7uqL88rPwaGwOdDw0oYlVmULKzF58Jo3n9e6F17jCXjPKbIgo63R_SsEY6xLhYqfnhwqd0W3zdgHJJL-_ispXOSl_oRGtlmMJtZYCOD5gv18xsvOBSSZwZO-y5nrWxGLlLyKmf39dTnjdpkzk8PhLyT5WE7ag634xwZTSYa5jpH39Fhm6YkE-Vvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:مسیر جنوبی از طریق تنگه هرمز برای تمامی شناورهای تجاری که قصد عبور از این آبراه بین‌المللی را دارند، همچنان آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی علی‌رغم اقدامات خصمانه و بی‌دلیل ایران، به بیش از ۱۰۰۰ شناور برای عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند و این ترددها همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69545" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69544">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=ZPdtFhnl3awb1U-16p3F6YAkSN0jUAV_NCuN1Eba5uG3-CGoHeLdNGN35Sy9D3rGRkwv2VF4oy9mo_aGb7sKmFaA32NifwYKffil3pvzZpxrrUJtWXo0qWMGbkuGcV976tMriSf-zgTz6e5iR8YC05rUAXlJR1NHbYsx8blGWKncNJGCOkCzrS8MOqm0WiFi_hHoQrtL6zzbBETcaVR9xbK4Z7_JZsI_bkuCLBN1Ip0ffKv65C9XOfoAlaEyRUr9VwGUCi7gla4Upovo6ZgJONpGZntwi8-2_c-C_CFsilAm9fjPblXChUUYubbiVWOitPP-082X8jQLAp_JudSo6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=ZPdtFhnl3awb1U-16p3F6YAkSN0jUAV_NCuN1Eba5uG3-CGoHeLdNGN35Sy9D3rGRkwv2VF4oy9mo_aGb7sKmFaA32NifwYKffil3pvzZpxrrUJtWXo0qWMGbkuGcV976tMriSf-zgTz6e5iR8YC05rUAXlJR1NHbYsx8blGWKncNJGCOkCzrS8MOqm0WiFi_hHoQrtL6zzbBETcaVR9xbK4Z7_JZsI_bkuCLBN1Ip0ffKv65C9XOfoAlaEyRUr9VwGUCi7gla4Upovo6ZgJONpGZntwi8-2_c-C_CFsilAm9fjPblXChUUYubbiVWOitPP-082X8jQLAp_JudSo6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم.
می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر.
همه مردم برای ایران سختی‌ها را تحمل می‌کنند.
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69544" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69541">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlXkyY_RKlLH3rreZx1tx6cLsabSHG2zKgCzDF0pYGSr0CrQp7UnhoqLa10A_vU0-PhUNAVIJTiAoFDF0ew1O9Dt55W9nWSyh-i_IsziBsgM_QsRzCy2SrV013gscEydOcXjqKgeMn9bydiCwdBzXMs0vKRhEf85HDXVtIeLr3GL88ZwMC07Se0PpDs8hExBfjfEuQNcoL5Yg4myHW2z8K6mlwQgVZBFZ211W5lmDg_YyxjJ1KOcJ1nED49tL2965FqRiMZA5QFBRCsPfnpULV08kSSqak7fn65yi71Ny26zu_Hu0vDZ8YPG7Ku0uJgEqSD0Yv1q2yMJRkGcSvoxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmZMfFIQUwjmnS2S7WGCnd2vfMc9Agic8qoNZzbHTDxzAb4LcIKumOPp14XWVHMqCjoP89oOtrDqLhvviYP4G5K150ikKjvj5L6kHeSjCZ9LzYPI5ac4zUehv-UKEJmvLodg3UaIfWJ4SICjKHEdrpsxvENqyKlhOJpxtBMoZpFbjfjsEoA80wEk2m9MHyZkgi1opWXwaMIWm03JilOW14XBnEUgL-jREBBj_-gVa7Pv-kJZ2mp9ZM2EJgcsQgpKMa8-aLIzFTpuyuweSYnMHl_s7yUT9gTtxACCZbbjgct1i7tovmsLUvviJClmbobiV02AkjwzxPCEEcpfH1soGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▪
🇺🇦
رونمایی اوکراین از ربات رزمی «Droid TW 40»
.
شرکت اوکراینی
DevDroid
از ربات زمینی تهاجمی
Droid TW 40
رونمایی کرد.
این سامانه با حداکثر سرعت
۱۳ کیلومتر بر ساعت
، برد عملیاتی
۵۰ تا ۷۰ کیلومتر
و ماژول رزمی
Wolly
مجهز به نارنجک‌انداز
Mk-19
کالیبر
۴۰ میلی‌متری
عرضه شده است.
برد مؤثر این ربات برای درگیری با اهداف
۱.۵ تا ۲ کیلومتر
اعلام شده و
Droid TW 40
می‌تواند در حالت آماده‌باش تا
۱۲۰ ساعت
در میدان نبرد باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69541" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69540">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6EC-3GrwjyHbswL_V-bxqj4HdbD2Ycnhdw4lJT7iLGW-oKYWwKm9JliC8UcN_AI4Z7M9laqMD1ivRfQyX0HIQhWWlNzMpNyVwCfzu1rQSd0W_7sdMFHYn2sk9d0ghGNDeuUKWHzclTV6IH1F1nPDJj6lOyF86R0sBOCTACPeNPXylEVhwnsm5VxIoenp4VOVBZcPJcF-vR_F14uMe3vgvWvr2cmphJ6QRK4Q7555oG_deqG_t541rdi-CK5IctMEsgorX2ihiCIJ3rTuyIoRx0toJJ2QSXnvZG62YqJOGyx8T16bRKL5DKxZyn_NRkknyLRrn4XLLd4xXPC98xXFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
نقاشی وایرال شده از زمان قاجار:
در زمان قاجار زنان روی یک وسیله تاب مانند میشستن و یک زن قدرتمند، اونارو بالا و پایین میکرد.
شاه یا یکی از سران مملکت هم اون پایین دراز می‌کشیدن تا زن انقد روی آلتش فرود می آمد و بالا می‌رفت، تا ارضا میشد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69540" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69539">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=iOWoyhk1W4Gd1dpLLWNfryNDX2kMC_hoW5tGWR9orY4mNvUTY9IAATJXJtq2r50a1_jnEXSwcxx1rMWLloo1kUygmrNt0bZQ8F2Rm0sbNnIoE0k8lIvxb7XHd0h8g1C2hV8WaSzr0mz58ufnicKV6s_QKZu9uL35aF78KtRJlU2hcISby2xGAtPxi8mgERiafMe6aN6duWkS9Fm9ZJuFqcImwVQGUmWOMMAKz8qmfGyXURFN8QNBWx1tjfv0VH8KotdGci2RACvhIc1NYt2-LV17aFf5uD_PY-fmEHBvOzExXItYLySdzjOne8g50rcz7141E07-GKsP5velXDkXMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=iOWoyhk1W4Gd1dpLLWNfryNDX2kMC_hoW5tGWR9orY4mNvUTY9IAATJXJtq2r50a1_jnEXSwcxx1rMWLloo1kUygmrNt0bZQ8F2Rm0sbNnIoE0k8lIvxb7XHd0h8g1C2hV8WaSzr0mz58ufnicKV6s_QKZu9uL35aF78KtRJlU2hcISby2xGAtPxi8mgERiafMe6aN6duWkS9Fm9ZJuFqcImwVQGUmWOMMAKz8qmfGyXURFN8QNBWx1tjfv0VH8KotdGci2RACvhIc1NYt2-LV17aFf5uD_PY-fmEHBvOzExXItYLySdzjOne8g50rcz7141E07-GKsP5velXDkXMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای از یک پهباد روسی که یک شهروند اوکراین رو تهدید میکنه و در آخر هم خودشو میکوبه به طرف و منفجر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69539" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69538">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3447971507.mp4?token=b7wvZnsF3n4pux01yJj5_Q8sgNdPQjZ6KzqMA7DcNpGZQQkZuWbr_F3uOFFOO0SKYHFNANLUYPo2orDX4Qo6U-2XROhGbDYPjfUqnajAAZQEhd7ARwlf_uJp1xwBqbCERTz7wyGY7OoYNpw_kmiIxcwJbxskkMaTmApCkpn-qiWRmTeIZCMcxVADyZkBLLDY0N2i9vk9OuZnNjpcrR3C_jFKYABDECjdXVUgWPcX4DncvAq0EnH2lR73DRGyD1hUlpLagUfh-AzYCkLK-2aqAOicG3rGMWXIYIshFx-pTb-srmjFMMnpvzYNnpP9mvGgpwG3ERqMIYoSLPv25yOq4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3447971507.mp4?token=b7wvZnsF3n4pux01yJj5_Q8sgNdPQjZ6KzqMA7DcNpGZQQkZuWbr_F3uOFFOO0SKYHFNANLUYPo2orDX4Qo6U-2XROhGbDYPjfUqnajAAZQEhd7ARwlf_uJp1xwBqbCERTz7wyGY7OoYNpw_kmiIxcwJbxskkMaTmApCkpn-qiWRmTeIZCMcxVADyZkBLLDY0N2i9vk9OuZnNjpcrR3C_jFKYABDECjdXVUgWPcX4DncvAq0EnH2lR73DRGyD1hUlpLagUfh-AzYCkLK-2aqAOicG3rGMWXIYIshFx-pTb-srmjFMMnpvzYNnpP9mvGgpwG3ERqMIYoSLPv25yOq4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
چهار سال پیش در چنین روزی، یعنی ۴ اوت ۲۰۲۰، انفجار بندر بیروت — بزرگ‌ترین انفجار غیرهسته‌ای در تاریخ معاصر — پایتخت لبنان را ویران کرد.
هزاران تن نیترات آمونیوم که به‌شکل نامناسبی در آشیانه شماره ۱۲ انبار شده بود، دچار حریق و انفجار شد و موج انفجاری ویرانگر ایجاد کرد که چهره بیروت را در عرض چند ثانیه دگرگون ساخت.
این انفجار دست‌کم ۲۱۸ کشته و بیش از ۷۰۰۰ مجروح بر جای گذاشت، حدود ۳۰۰ هزار نفر را آواره کرد و خسارتی بالغ بر ۱۵ میلیارد دلار به بار آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69538" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69537">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=tVUdk00BFmADi7ypbPvXhJki8GMASaB-pRclsviV_A5G3CQDOp_rucZBn4PnPKkvQj5Ow7yb8w_oI3J4HymvE1EXAGJrVvM42nYJi4_9bVOt3h6lAmW12b6g3zJ1of0HXRz0X0DWNiVEqt22iHiVdFV0JKiNhlir-QrbFpFIfc96ut2lYKbrE_RSMm3KLj_D8CBWdqHjFpLcB2iFXCyzjA8TjTBI3YXOJoFlMAy3MxG4kUD40Y_zZTJ5D1UyOQ5JA3lKnzB5v6tH_NT_l6GRipyq7KTYC9oCj6LSF6CRAffZB5Qc-CBmu4d44r3ANwME5bCPi82riRUq5p9t1xkg0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=tVUdk00BFmADi7ypbPvXhJki8GMASaB-pRclsviV_A5G3CQDOp_rucZBn4PnPKkvQj5Ow7yb8w_oI3J4HymvE1EXAGJrVvM42nYJi4_9bVOt3h6lAmW12b6g3zJ1of0HXRz0X0DWNiVEqt22iHiVdFV0JKiNhlir-QrbFpFIfc96ut2lYKbrE_RSMm3KLj_D8CBWdqHjFpLcB2iFXCyzjA8TjTBI3YXOJoFlMAy3MxG4kUD40Y_zZTJ5D1UyOQ5JA3lKnzB5v6tH_NT_l6GRipyq7KTYC9oCj6LSF6CRAffZB5Qc-CBmu4d44r3ANwME5bCPi82riRUq5p9t1xkg0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ترامپ و تیمش تصور می‌کنند که می‌توانند حماس را به خلع سلاح و غیرنظامی‌سازی غزه وادار کنند.
آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم.
این پیش‌نویسِ ما نیست؛ ما نظرات خود را ارسال کردیم. ضمناً، ما نظراتمان را پیش از آنکه شاهد هیاهوی رسانه‌ای پیرامون این موضوع باشیم، ارائه داده بودیم. موضع ما همین است.
و ما بر سر منافع خود، هم با درایت و هم با قاطعیت، ایستادگی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69537" target="_blank">📅 21:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69536">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8esvWBOnXVyw01pEUawEVUzIJW0SZSckPwiC7Kc148x3LHtFHfeu8-yaHXOScb6klRO5lkS95optsJsZFUMqROe8d-qnBHeILEM3ayPTVKKeV2CuzWAGRRr4DeHx_U5UakvrwJrIe7jwaCJC9FTRQx0yAry11LaK0jy7cYesSPZfekHZn-nmhh2CqTolFPo6QZXDPy1kh0ITJPcNgG3Qr4u8vQx1Bq8e4XTE9KNTvlZVHd_wJvwMGBR9G9DeeTov1zQ-KLJv99TeSqZpWNqvgE1dILXFR1TS3RxuMpWnfzgSZ_ws14Jl_BTj3RrRpmuwpAZuvy7ACk6rWYakmIUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال‌استریت ژورنال: در حالی که دولت ترامپ بر نزدیک بودن احتمال دستیابی به توافق تأکید داشت، وقوع حمله‌ای جدید به یک کشتی در حال عبور از تنگه هرمز و بروز اختلاف بر سر مسئله عوارض در جریان مذاکرات برای بازگشایی این آبراه، چشم‌انداز این کریدور حیاتی انرژی را با ابهام مواجه کرد.
به گفته میانجی‌گران منطقه‌ای، بر اساس پیشنهادی که هم‌اکنون در دست بررسی است، کشتی‌های عازم خلیج فارس از مسیر آب‌های ایران وارد می‌شوند، در حالی که شناورهای خروجی از خلیج بدون پرداخت عوارض از آب‌های عمان عبور خواهند کرد.
میانجی‌گران اظهار داشتند که اگرچه دیپلمات‌های ایرانی در ابتدا از این پیشنهاد استقبال کردند (زیرا تا حدی کنترل بر تنگه را حفظ می‌کرد)، اما تهران خواستار حق دریافت عوارض ــ که احتمالاً با عمان تقسیم شود ــ و همچنین دریافت تضمین‌هایی در برابر حملات مجدد، پایان محاصره دریایی آمریکا و کاهش تحریم‌های نفتی شده است.
مقامات ارشد منطقه‌ای اعلام کردند که آمریکا و دولت‌های منطقه با درخواست دریافت عوارض مخالفت کرده و خواهان تضمین‌هایی هستند مبنی بر اینکه ایران و نیروهای نیابتی‌اش، قلمرو آن‌ها را تهدید نخواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69536" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69535">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSDB0hI0wSme7aeIqNv73QqZSom1A6QlBHX4Qtrqfa0dwkXTrrjroFwk4Q9VaRQ3-64G2_cFaJT3fjNHYagOmPV3MVV6ZWqi-QpeWDFu1RSbKWPtew6sjC98PUGg68Ln4Lj5esT4FN9AyzqgqFv4Sl-zIaMPPTmSLuhzBoAqmz2jK7mxCOmCNWs4Ven2LkYPbQXP4EyRL0kWyvP5TTBLmxhknMveDqLXgFi6xEH1SLASI28D63m9vByGx23ptbC5PoueoWVP-nkd1TByLtnnA6etae7Ev9HVHa8UxXkGb1cD2n-VPR1dquNjg2-dB-GcgytgFecD_RXmTQJdeVoqnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:یک ملوان نیروی دریایی ایالات متحده در «مرکز اطلاعات رزمی» ناو «یو‌اس‌اس باکسر» (LHD 4) مشغول نگهبانی است؛
😃
این ناو تهاجمی-آبی‌خاکی در حالی که از محاصره اعمال‌شده توسط آمریکا علیه ایران پشتیبانی می‌کند، در آب‌های منطقه در حال حرکت است.
تا تاریخ ۴ اوت، نیروهای آمریکایی مسیر ۴۵ کشتی تجاری را تغییر داده، ۲ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی دیگر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69535" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69534">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=p8FatPJcrJXK62JxJWj5mt4RLwaY3-C_dZdNfL4VjR5TNxOUIEVoVoZvhTp6jYIxlzLb-LAtaIcekvFsUdAWCOeSmolUTbWwN0_T4XiXE2vl8xTSOcy8S8VkcGgfNoGxIZFoG05RCHhVdE5y24Kqn0ssiRUvNjDhIzQEj2xI-LN2_qi7bTP_7ZEvGk8EcXvE6tUdWLQi4yKLUqJqk6bbOuKZnn87dfNAnxGih6ggZ9h2-wKiUCHfkukXTvjUBHGgyOFlO2U3ZZ3SnKVJiY3yPRIM15m7ZAo9MPKJ6PvkcrdQh7megeOA7j0F2A33iAhOV4ypq8gJyDzFDst9-pUBjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=p8FatPJcrJXK62JxJWj5mt4RLwaY3-C_dZdNfL4VjR5TNxOUIEVoVoZvhTp6jYIxlzLb-LAtaIcekvFsUdAWCOeSmolUTbWwN0_T4XiXE2vl8xTSOcy8S8VkcGgfNoGxIZFoG05RCHhVdE5y24Kqn0ssiRUvNjDhIzQEj2xI-LN2_qi7bTP_7ZEvGk8EcXvE6tUdWLQi4yKLUqJqk6bbOuKZnn87dfNAnxGih6ggZ9h2-wKiUCHfkukXTvjUBHGgyOFlO2U3ZZ3SnKVJiY3yPRIM15m7ZAo9MPKJ6PvkcrdQh7megeOA7j0F2A33iAhOV4ypq8gJyDzFDst9-pUBjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
یک جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در آسمان خاورمیانه از یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت دریافت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69534" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69533">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpTVHVYwm4n8C3MWk6P6TCowk_gQ16LHMGrDmtZJ-8fh4HEuZ8vCbeLUANmykpzPqOT3WAhwtunVUPXlAk_sH3adwCzpSfV1oVIfqCZloE9shwRvkrjhSr7EuHi1kw2vdpf14WTmoxEIbaLp5DGYemN4KZMmPED8ZmefrEIdxls1ygSkTNz55leMNZAdpYtNZHckkrxpoMXgcgKQUN_yuR4ihzTZ1yOyVKSWLK-bc-FKmujpUxKLDiL8ERo4DwHofbfBwqAETdrxLx_kXz9d3HWD6fNfVJGCFvssE_85PiLu5CJjaiAFJ_l7qs3UXK_-TOZ08frtb__5z-tlbR3K6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ایران در حال بررسی امکان مشارکت کشورهای اروپایی در عملیات مین‌روبی در تنگه هرمز است؛ اقدامی که نشان‌دهنده احتمال تعدیل موضع پیشین این کشور بوده و می‌تواند به تلاش‌ها برای ازسرگیری کشتیرانی و پیشبرد مذاکرات با ایالات متحده کمک کند.
تهران پیش‌تر به‌طور علنی با هرگونه نقش‌آفرینی خارجی در مین‌روبی این آبراه راهبردی مخالفت کرده بود، اما در هفته‌های اخیر و در چارچوب گفتگوهای گسترده‌تر پیرامون عادی‌سازی تردد دریایی و کاهش تنش‌ها، انعطاف‌پذیری بیشتری از خود نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69533" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69532">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=egzpaQ4EtaHObRUeX33TRhcbbykjOBH-nBe8r5zPN-0F46ZSe8tf00rdtmmS576koff21DD2k6IOierwHLwNin9NSXItAgoyVSIYH9V3MzVkla28yxvWfEJQ9aI_0CTyH1-H_YzsRKA6EQU-XIaxrPzLGNM8ywlzmJQl5XP8xKC6gBgUVuyrhzjQ4uWufD_CGVWRTJNK0HvztnBAQtoPDx4LPl4lo1MvjTJ5mnyYgfRpxljmd1XB6h0XU4cOqQsrOXrYxXWVymDQMIUN3DNyJxdcnLNg9Lclqz_wc7wPLoJwAyfqZNIBAtODV_OYMxpVIvyVUDDBM2MetQWf4uDteg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=egzpaQ4EtaHObRUeX33TRhcbbykjOBH-nBe8r5zPN-0F46ZSe8tf00rdtmmS576koff21DD2k6IOierwHLwNin9NSXItAgoyVSIYH9V3MzVkla28yxvWfEJQ9aI_0CTyH1-H_YzsRKA6EQU-XIaxrPzLGNM8ywlzmJQl5XP8xKC6gBgUVuyrhzjQ4uWufD_CGVWRTJNK0HvztnBAQtoPDx4LPl4lo1MvjTJ5mnyYgfRpxljmd1XB6h0XU4cOqQsrOXrYxXWVymDQMIUN3DNyJxdcnLNg9Lclqz_wc7wPLoJwAyfqZNIBAtODV_OYMxpVIvyVUDDBM2MetQWf4uDteg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسن عباسی:
زیر جزایر و سواحل تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69532" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69531">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWf07goC9Mp9R0A0ECNfr17FYSjwKIL5TW7dEeqqOqrSnAo8_fdg35A1dTS0cJ-7KU_p5C8y4AGACylXUcj-Lc0HvrXPPoDrQ5PrxcL34kwjorDQgkjrwTG2hGKDZdUP_5Lm9brlPUtlmmN-DtHMwxscKP2Oj2dQyHVhE67F63aTOu-xhdhurCLXsMSV3DgTw7Ve-E58nklvW9sjZpNvd9968x-DqvMaHQk974j9yIk3ttNL4mt2DPAgez-yuOr1PqFkBfoSeExrE6Hds-1T0mEx-7OIzPs8r8o7iyyCyQiDTCtOT5BieTAz0_xM3cxBo5wUGi9qIlsPDm8vU52VvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69531" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=UbbTUHQyrM29iuBHrGhIPLV3UAdk25O59wurJPmz3XuDCQwGkpDzYZFB8M2fHTsr_2-IL4PJMr4UZ0CvMUTH_3Y3nOsvAcgdhVIY8AbHOPTN1C_MbBGr-mdg5_lwSkWJCSNYtHuHSsLAXPg8Mez4za3_EsG5ZGaLHB_GKQzaqXTqGnQB71FqtZ-B5XodkF81w_DiCN7C-EVc2kGOM0jbilstbj_JTsv4_-c3UDqqw80r_M1H7glLVylWzDxGFpZDr3DvL9BS-JKsVJzKt7HaYcPLAQ5uCRlCjkGL6TiOS1av_KZKwYEsHeNwsEDdzgxLPgqFdTVkCKk_nWXJBr7MXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=UbbTUHQyrM29iuBHrGhIPLV3UAdk25O59wurJPmz3XuDCQwGkpDzYZFB8M2fHTsr_2-IL4PJMr4UZ0CvMUTH_3Y3nOsvAcgdhVIY8AbHOPTN1C_MbBGr-mdg5_lwSkWJCSNYtHuHSsLAXPg8Mez4za3_EsG5ZGaLHB_GKQzaqXTqGnQB71FqtZ-B5XodkF81w_DiCN7C-EVc2kGOM0jbilstbj_JTsv4_-c3UDqqw80r_M1H7glLVylWzDxGFpZDr3DvL9BS-JKsVJzKt7HaYcPLAQ5uCRlCjkGL6TiOS1av_KZKwYEsHeNwsEDdzgxLPgqFdTVkCKk_nWXJBr7MXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
غنی‌سازی اورانیوم چطور انجام میشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm-ZKCWqpmQJsihfGnaVt4UFxvc_Eo8PNzzxAGE5V5f2bVc2i4_o0PedTosBdIAGh6nnUiy8bqvBKDKdsWNFq3wC6ifc2R2OUr9TcIlzlAXj1vPGUOs2i5oavanjhMj-n86DEIrUlbkKBBm_22uyj_HJVmxL__Fqf1SzZssnPOfN09vitwZXaO61zg9q8SqijMJamvnFbUC3y9Aj_qE9o4SIvHYKceSH_ZV4pTlDJWHAz3yR6oboz8gTci2sKn8zO5pt-fkAVCKxMlfgz6e40OpQvmSN_tQDW1W_ghA2Ru_QVfcsP1odQmCprTOM4gLaeF1Y5OGj2f9aK1xlVAfr8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=srkMsv7tMUGH6V-N8f2zlON_ORINsVh4OcdYjfVItIvgW2b7HyjBX5aRyi20EmmbniIulVWS2QlyzV4R8org9_6cp9_pXFioPl1clSHbT7hnhSMOT0nzK-gIkAw7njFM34UnLHCwTlIW65NM9kl-hFYBv1B-NlJ8sM0dEaHpbUPgzEDa0mn0h6QZWUwrrYgV1sDhDaxtJpeQ70bfzTXRmfY39VV6OymbpOXyNsSYUUe7UYoCm_LizLKfzsLOApkM86ShCV13WI4wxtTw7ZJ36nxLmZ2WNSShMUwS0Vn9pvb22WTDD3VfgDGyOfq3uUF3ynS4ttNUqIstkFpE0Auagg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=srkMsv7tMUGH6V-N8f2zlON_ORINsVh4OcdYjfVItIvgW2b7HyjBX5aRyi20EmmbniIulVWS2QlyzV4R8org9_6cp9_pXFioPl1clSHbT7hnhSMOT0nzK-gIkAw7njFM34UnLHCwTlIW65NM9kl-hFYBv1B-NlJ8sM0dEaHpbUPgzEDa0mn0h6QZWUwrrYgV1sDhDaxtJpeQ70bfzTXRmfY39VV6OymbpOXyNsSYUUe7UYoCm_LizLKfzsLOApkM86ShCV13WI4wxtTw7ZJ36nxLmZ2WNSShMUwS0Vn9pvb22WTDD3VfgDGyOfq3uUF3ynS4ttNUqIstkFpE0Auagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:
کشتی‌هایی در حال عبور از تنگه هستند.
هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است.
تنگه باز است.
ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت و هم‌زمان با حرکت به سوی مذاکرات بلندمدت‌تر پیرامون خلع سلاح هسته‌ای، امکان عبور ایمن تعداد بیشتری از کشتی‌ها از تنگه هرمز را فراهم کنیم.
در مذاکرات برای بازگشایی تنگه پیشرفت‌هایی حاصل شده، اما هنوز توافق نهایی صورت نگرفته است.
ما امیدواریم که این توافق به‌زودی نهایی شود
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=m8IyXw1R60Cv0HaV8Hlob63lQl9XJNrw8vGyAqv02yuS50KvOTBHRboYOX7reSvUCHeKkN5V390H58K7QYyjTc8LBG4CieJip2VBYrQiESEEzhShki358cQe43XnRFcuieNQgwxTeO6HApB4de6iXaeIWBcIhGIyUhHo5S6JPzPslrOyKPzs8PIKqflstlCJvS8_kINSiJSJBmvOFQgkXRfv0_KFWfbUXZRu-lI9N1_Am2jaXUIPjvX5AKd5-jMmiPLfVaGXM_SXpmOBr3BYs_Vvl4XVTngZgXDppybvm-x0AunFHfXvN60WJsGoa9OSFC7UUgo8BQuK3ns4v0CTSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=m8IyXw1R60Cv0HaV8Hlob63lQl9XJNrw8vGyAqv02yuS50KvOTBHRboYOX7reSvUCHeKkN5V390H58K7QYyjTc8LBG4CieJip2VBYrQiESEEzhShki358cQe43XnRFcuieNQgwxTeO6HApB4de6iXaeIWBcIhGIyUhHo5S6JPzPslrOyKPzs8PIKqflstlCJvS8_kINSiJSJBmvOFQgkXRfv0_KFWfbUXZRu-lI9N1_Am2jaXUIPjvX5AKd5-jMmiPLfVaGXM_SXpmOBr3BYs_Vvl4XVTngZgXDppybvm-x0AunFHfXvN60WJsGoa9OSFC7UUgo8BQuK3ns4v0CTSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو پاکستان، یه تجمع ضد جنگ برگزار شده بود که وسطش یه گروه جنگی اومدن انتحاری زدن در رفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoKoobgBJ5TDGep3NztMUD8vpT1ayYmOmNE8rbY_dFh8xdRHMHtvpq3ENXQ7RwefxssLSDoiie4hNLAONLE2WX2Cq18OxQ_juEE2OT6g0OKvNVroZFduWd8tO1OVUj2JqvhJJVPFbkJr9ry1QKT0CVx7MibPxZMwJeFnG-4YZRzH1s37M5GhCtpg9oS5zCDcar_2E7V-9ciVefacgGzv4_gDeRKVVjggRoOZODZnChtursWE6lIlnYagIPTYXwpW91Sz7-ilI7dpch1qkRHQM6ig4dfhCMvyNVBvsiiV387mqhtv9dxoWda4fCm2NLyUFIRJdxLzrzZg7rin7uTxbNCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoKoobgBJ5TDGep3NztMUD8vpT1ayYmOmNE8rbY_dFh8xdRHMHtvpq3ENXQ7RwefxssLSDoiie4hNLAONLE2WX2Cq18OxQ_juEE2OT6g0OKvNVroZFduWd8tO1OVUj2JqvhJJVPFbkJr9ry1QKT0CVx7MibPxZMwJeFnG-4YZRzH1s37M5GhCtpg9oS5zCDcar_2E7V-9ciVefacgGzv4_gDeRKVVjggRoOZODZnChtursWE6lIlnYagIPTYXwpW91Sz7-ilI7dpch1qkRHQM6ig4dfhCMvyNVBvsiiV387mqhtv9dxoWda4fCm2NLyUFIRJdxLzrzZg7rin7uTxbNCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=E-uZCY3Vn2USImcGS_DYj4HmfTKxO-CVK_U-TfdN9MN6nkjnvHUGXaQmLxnxJPzVGC7RYgxwFrWw9fYUUzBggWBG6vkM39bst5PPM46VO4cpNaSm5IfdGMUuN_aUmKzfrs_SHfPAFK_60fVBc-eGApMa8YS6Pf-8YPSINIQi81sPOjd0zK1_twJqlqI8q499stxVowikrEs25p74yanaGYComVmB8ImIjaeIhXDzzSr7njVCnlEdwSSwHva8zMqVahrGbN-gLHU3PDCC84oaPBq9dnxrhsFz2M7u-UcRF8N4W0NFKF3jCi_HZrNrSs3jbI4mcNJbsD2e60blZkTBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=E-uZCY3Vn2USImcGS_DYj4HmfTKxO-CVK_U-TfdN9MN6nkjnvHUGXaQmLxnxJPzVGC7RYgxwFrWw9fYUUzBggWBG6vkM39bst5PPM46VO4cpNaSm5IfdGMUuN_aUmKzfrs_SHfPAFK_60fVBc-eGApMa8YS6Pf-8YPSINIQi81sPOjd0zK1_twJqlqI8q499stxVowikrEs25p74yanaGYComVmB8ImIjaeIhXDzzSr7njVCnlEdwSSwHva8zMqVahrGbN-gLHU3PDCC84oaPBq9dnxrhsFz2M7u-UcRF8N4W0NFKF3jCi_HZrNrSs3jbI4mcNJbsD2e60blZkTBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=VNj7ieVMzUaMoqFCYjHJA6RjfuufidLMCIJNN6maVO1no8KWEpojx4Q9X1fdr30mntJZJOmBRmPL_zpn2fYcH6KOyqjRmgzbwj_vBaErjmDQ5XBkgqeYEgxydL124BIX13qcczGgEgRXDr-I7mzrbD9TpgWMU3R6u9LfElSn-uSI981tMZeiIp9uTWAEJTnssl0MxVtP3G1EBycO1005FTXzU4H3FfzOFDboLDo2c5Xap1JHhCNDWmzg2gxqk0GycxMPPvfDJxDh6J4LsrhLMlP_N1Ua-u4ef10DQTOVLOg3DNNdVEQ31FI5ME0Vru6z-gVqve3xYgQTJXO4BpH9gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=VNj7ieVMzUaMoqFCYjHJA6RjfuufidLMCIJNN6maVO1no8KWEpojx4Q9X1fdr30mntJZJOmBRmPL_zpn2fYcH6KOyqjRmgzbwj_vBaErjmDQ5XBkgqeYEgxydL124BIX13qcczGgEgRXDr-I7mzrbD9TpgWMU3R6u9LfElSn-uSI981tMZeiIp9uTWAEJTnssl0MxVtP3G1EBycO1005FTXzU4H3FfzOFDboLDo2c5Xap1JHhCNDWmzg2gxqk0GycxMPPvfDJxDh6J4LsrhLMlP_N1Ua-u4ef10DQTOVLOg3DNNdVEQ31FI5ME0Vru6z-gVqve3xYgQTJXO4BpH9gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUGKbNis_cSBH5fi9MEURtWROw1NyOtCm8QvEJ6Q3MZ-BxuyEoOjnRP30yX3yKEsFnNF4C04A5ilVsM7cTo75wSKB0MI574cmODBN6vzg_44--HpFz5oqDHUltwsTG-pgHsxrfpuiJBxmURd4GrJEAd9mW47uiQOlUGUxI7qyjBuASmMfFJD0501iz4dZtW8R4sQE4ASwnz4odhgJzBj5ORyQuinXNR2aBOjyS9-ma084v3q-ZhZifueD_Jsu-xH2OkAxpx5tYNXYoX7GlQkremxXI7oxazNuDinLU_vW7EebemIVbFOX1QTVVmaSj97HOm4mEBwDo8AHcOvqXeahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇺🇸
🇶🇦
🇮🇷
سخنگوی وزارت خارجه قطر:
تلاش‌ها برای دستیابی به یک راه‌حل کوتاه‌مدت میان ایالات متحده و ایران در جریان است و متن توافق احتمالی نیز تدوین شده است.
این پیش‌نویس هم‌اکنون میان طرفین در حال تبادل و بررسی است، اما هنوز دستور کار مشخصی برای مذاکرات مستقیم میان آمریکا و ایران تعیین نشده است.
تمرکز دیپلماتیکِ فوری، حل‌وفصل تمام اختلافات عمده نیست، بلکه هدف، دستیابی به کاهش تنش در کوتاه‌مدت است که بتواند راه را برای ازسرگیری مذاکرات هموار سازد.
برای بازارها، این تحول سیگنالی مثبت محسوب می‌شود؛ چرا که هرگونه توافقی می‌تواند خطر تشدید درگیری‌های نظامی را کاهش دهد، از تنش‌ها در تنگه هرمز بکاهد و فشار بر بازار نفت را تعدیل کند.
با این حال، همچنان باید جانب احتیاط را رعایت کرد: اگرچه پیش‌نویسی وجود دارد، اما هنوز مشخص نیست که آیا واشنگتن و تهران هر دو آن را خواهند پذیرفت یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFP8mNMsJdDmfCP1Z-YUC0MLdPVFQXpe8SBrsunTjf-VFL155GhiyNiMcYCDpULoBvezlqW7awPx9Kma3YPAWXh1wi4m4TglKt1k8EmJZCBcrTNxnSddGN32W5nW77MO35t3NadW1_luD-ElvBD_rtb-vfTP6sx2XBCG4kuNMAF9U55rm5nTSI_byvMHm7-_dHdgUfoaqkSmEPXzZwyQhRWNGjOCX7S8iG8AtJ-93TeVIUJwF34hp8czezxYQmsAig08Gl8OT-sTCmQEOxCw1qkIOQQFEC9rM--DVQ_IVvL6b2GkVnRkpb3dgKojpJSg_JC2VjxMnZBfXDlMBg9wGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=cOWOttIwF-6zsI7OPhfuk7K4w70zmrmX0V0oDF-8kI_T99k85ltVtYwpSJvShbwLyV3_BMWv90mgUrtYNX0rzLAXFPAp88WS28q_FgrBneByOTuxko6QXuFEog50V3AKC6I7yLOGu_ToiqqWu1hLyXJQSTyer7aVpkb7nNuW5TQ4Ic8ymE3z317pcaAShsjQIVqeTCZhQ0nP-QFLWt8wixKtqxYS69G7nE_M1TqRLBKmypU9xx7UKUKHdSpr5-J9-NLmsA3AvVsd3weFyXBe1dJgvZYmtE41pxh-HsGDmDU7ytuJl4_irBSaUbzmVAxXlqqIc_qBYJB63OlGJB-VWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=cOWOttIwF-6zsI7OPhfuk7K4w70zmrmX0V0oDF-8kI_T99k85ltVtYwpSJvShbwLyV3_BMWv90mgUrtYNX0rzLAXFPAp88WS28q_FgrBneByOTuxko6QXuFEog50V3AKC6I7yLOGu_ToiqqWu1hLyXJQSTyer7aVpkb7nNuW5TQ4Ic8ymE3z317pcaAShsjQIVqeTCZhQ0nP-QFLWt8wixKtqxYS69G7nE_M1TqRLBKmypU9xx7UKUKHdSpr5-J9-NLmsA3AvVsd3weFyXBe1dJgvZYmtE41pxh-HsGDmDU7ytuJl4_irBSaUbzmVAxXlqqIc_qBYJB63OlGJB-VWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMQOcspZbGjiRTtqZge7MVjsRGQgs57XXpXv6k4ykUidRgTakc7pP6fasGV4WQaQiDFL81HMUr4ouJHz24x4IdKsbx4m0BdiVqQ0Mw0ukiWUH0uuakBlf5IS9Qt4WWwm3kIpyo4wZCML6zeZW9sKU4QTi1g4vbviJgwXzg1kGXu7CP-_YUD36KwPAkuyyLBpZ027gOtt-iAu-jCZc20VWzNdROaqlbDORp7Vfn49VKmwaH-kAuAzPKfO2vZ34V24eieQyWkUDMc4Hxxe3UsGoV7wHdc0NNq-0Dh9Utx0tHwzq-U_7lzon7yZkATrNpw0CPwezH6n6xXIaDzdB7ez4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqVWTCHDOBCrF6w_JRzQ-Jo5FbD4vvDWd5y0WuIF2bNvpj_tm9A8vkxGERb5vNDhPaPBsgT8cYrBAbnRbKzoM5mA5zhGH6cBtokBrZge4lNM9eDC2DWV7qCTf6hyEeh9O5sr3fstcB2lxlVWrhOEgL_CsVuJs-xtphpoJ89s_soAwiqFjHybVHk_NGYjYXVy4NvEHd9GD9uvZWz7VRnjzaWzUwgG7tSu-dlGL-xkLQy0hX0XzUXm2ArDUSyprKgmH0gmhjF3p3hk1fzPpCCdSonSVsd4BiaRFpY4cJx6s2c_P4iFkLPxd_7bw2SJ2RteUtN4giyMkEsT3O_9i1jjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUEn7HBO2fF1JjZ-OW2CPyDw0nOJyMdfAzsg4VUnAhpe13LINAeAsbvGWPgQkVw8Hal9YEmGHOtZxg9nGQgFdGO2kAWtVB89L2fAv-XzcDRCZ265fvyJoAVUDpC6N90J2Lhpc2QwMoiknO3Nm5Ybj_nZyXFNyK2bS1GkKNBFMWuARMbq_WA8vdq55RGhRV_GXX6hsvgmVmsVTfq7sqGiKtQ3jlNkxy6znDJ-4F2ikYxIgoaq0YDZOrLb0r36pXV62jCpcq2dPJBY32IQ9eeGqUj_HoziIguUDdobrCFjuPrYwIGwrr-qqF9VdbZuZ4k8510GCh8l4HEo_ti1fW1A-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bfyk7z03gubIHo5LMeAUi29HMR5GlmhdX6ygdzFiuoamxDUfgqiuFlZVn79E-w8Ddz8GMPSwda61VhdxM9Ljh-KWNTImWydG4c1fpTE9fLRoEAGkYiTE2p-ph0iSCVABIvutwM9Ih5K4BaOrl2fgB7y7jgcHDDbulSF14mL2Jo7MhjJQ3C1CTsJ3Uwk6PpT5hDM2sSGoaeWKatlvqdne0PXa00970yroKg_u6hOP3GbVJ1wpmqeecq-Zo3188pV4gJvJJdjH-WCBNsGlOuV-SZDswF709EriO0FZQR5tRMoA8nXbJgtR3c02O9W8wDb1fOeqrz1dbuXZfAT-HnzjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZnrsBQyTCSCMcA0ZCMHCWIRvOtddvgJrw9k9u2WjowoD8XMNfja4k1QUjoXu-pSckcahgNGoxOUyzZqTTN7cbbtLoav4M6L2vrqgSbNUyR1tNd9MC8OjDCOmmrgFKyfcYNYHNVibbLzNzhZQTu3rQ25fFQQMh_TrZghpkT6aJau0T-2S0ZSn3GYPsJdUf2wFqOTDHI9vGHuuITfeZCso_-PCpTloiNFyb6_yIh7AFZUqGbvFV8RcG6oW6iqCCDvoyNAtOJXRo61hT5n81kr1SYZxBRCHg1atsR7t1mG7zKOBsvvzCNbxsr1gtZ_MuLheEZvhN2KOj0mrUCb2JyIBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=t8tvLXLkXHeuiTFePcWxihSFPtCKVmspjRtU18m0dXvm1i6CD2G_YLjqikgFGQnRLeFzcLtRgcKvSyHvBmiB1xTDltsLleRF4uxiTCKilbMaDRXmHjwxoKk-SKv9Jan7E6T7zkvBGEwrIyfScGq6swwbNxqJFJRH6tkCRdItTBI6vOjSNw35KXnNMr3dqg5tuVz5NTO9Lbx88AOR2KXBDuryreBkkP4RovQHBb7366GiVbKm4NKzAs2kqkPw25NFapusi2zlddi3WiE3orIxTPdsO55p8JaZpgIf3ZgB_35VjdcchONPsOSAUfFzE-RKmfCKGmTLrPUhwZlje8g4Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=t8tvLXLkXHeuiTFePcWxihSFPtCKVmspjRtU18m0dXvm1i6CD2G_YLjqikgFGQnRLeFzcLtRgcKvSyHvBmiB1xTDltsLleRF4uxiTCKilbMaDRXmHjwxoKk-SKv9Jan7E6T7zkvBGEwrIyfScGq6swwbNxqJFJRH6tkCRdItTBI6vOjSNw35KXnNMr3dqg5tuVz5NTO9Lbx88AOR2KXBDuryreBkkP4RovQHBb7366GiVbKm4NKzAs2kqkPw25NFapusi2zlddi3WiE3orIxTPdsO55p8JaZpgIf3ZgB_35VjdcchONPsOSAUfFzE-RKmfCKGmTLrPUhwZlje8g4Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=SqCKht47YaJEZuwK5ZvP0VBS1optE-evdNmBjjtcBow5N8JeO44H94VfkMQ9HJ3QUktrRXWC9MGiNzgqDumfWQ6YmXbW_3JRmjEsBtU5mDHJR8xYsZzJkfBCn_ZED_9EHM-qSLz4iKOfj_k8NEuOUPJdua23w4ps3M_Yy9-_6wdSDyxM1vNySHk_qDzK_oB_1Q0ZH3bjYzTxAvPdTaeSqits7144m76ai_kBwEAOPSZw7asd6fXnpn_MbpEDSPX4Lxch-rg0iyZJQFlHEZmld44ax8TQDDbK4KyBzACwR_Q9-EUG0KSC8MReQRv17mLOZKWmb8WpXHnQn9cj0qZKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=SqCKht47YaJEZuwK5ZvP0VBS1optE-evdNmBjjtcBow5N8JeO44H94VfkMQ9HJ3QUktrRXWC9MGiNzgqDumfWQ6YmXbW_3JRmjEsBtU5mDHJR8xYsZzJkfBCn_ZED_9EHM-qSLz4iKOfj_k8NEuOUPJdua23w4ps3M_Yy9-_6wdSDyxM1vNySHk_qDzK_oB_1Q0ZH3bjYzTxAvPdTaeSqits7144m76ai_kBwEAOPSZw7asd6fXnpn_MbpEDSPX4Lxch-rg0iyZJQFlHEZmld44ax8TQDDbK4KyBzACwR_Q9-EUG0KSC8MReQRv17mLOZKWmb8WpXHnQn9cj0qZKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=bn2NsJjJVoaZUEcw8BwSCDp1OggEuntHzSpY3YzsFOUbkoi4gtzueOWP8BPava9bX-N7wd-EsmMqEOw8yde0PonJughh6TJn6ESQGnGhvF6j1CVWFe2kAIMIk6cxiinettZ6nBHBEO7WDRuZE5FjhD0m_cRAqxsJRgBYPTqBSUMkjs1-sVBn2iSpYYXTo-rkooLceXkjDhLgy6Zo0XBVfnV71pAhFtzBiFV5w4DJ38JMohFbHzmRfdc_PJ4Y9WFiZZ0N6WEzb9j7lqtIcI_3LrYbIv1rLE5pFYl3eOBaESBEX4Iislx-Nx_MfCkf1UjaAsou1Yoz5UEzbxQ6CITKTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=bn2NsJjJVoaZUEcw8BwSCDp1OggEuntHzSpY3YzsFOUbkoi4gtzueOWP8BPava9bX-N7wd-EsmMqEOw8yde0PonJughh6TJn6ESQGnGhvF6j1CVWFe2kAIMIk6cxiinettZ6nBHBEO7WDRuZE5FjhD0m_cRAqxsJRgBYPTqBSUMkjs1-sVBn2iSpYYXTo-rkooLceXkjDhLgy6Zo0XBVfnV71pAhFtzBiFV5w4DJ38JMohFbHzmRfdc_PJ4Y9WFiZZ0N6WEzb9j7lqtIcI_3LrYbIv1rLE5pFYl3eOBaESBEX4Iislx-Nx_MfCkf1UjaAsou1Yoz5UEzbxQ6CITKTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuyBVeVn8JphM2TN4TN7GgPeFMrsu7Df50H2PyHGoMA8WtgkZhAT8tg0K1_Y3CD-KK5M6MVWj0dGzIpSjEaPA8oPhHYFI7cwp-GzERvmNMIMADPF2LtYNqqUtYZkdvuEYG-zl-wRcKP_Mlerp6WZgcGLTOKyB-JH9U57Iz1quQm1YttAyPVD_8bUccmeoAOUVkgtOZtj9Fnw4w-Hrq3v_wMFcAHaGLXDVyQLH4tEzH_y3UJ1zRmzgbiV86_wEnUIHHc5I3mEwbk9Dq76Yb45P6aIG1zwapBl1fKmA7F64IQUH834iBALZfvt7MgCcHjBDX-JDspCFjULFztIIJ07CKtM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuyBVeVn8JphM2TN4TN7GgPeFMrsu7Df50H2PyHGoMA8WtgkZhAT8tg0K1_Y3CD-KK5M6MVWj0dGzIpSjEaPA8oPhHYFI7cwp-GzERvmNMIMADPF2LtYNqqUtYZkdvuEYG-zl-wRcKP_Mlerp6WZgcGLTOKyB-JH9U57Iz1quQm1YttAyPVD_8bUccmeoAOUVkgtOZtj9Fnw4w-Hrq3v_wMFcAHaGLXDVyQLH4tEzH_y3UJ1zRmzgbiV86_wEnUIHHc5I3mEwbk9Dq76Yb45P6aIG1zwapBl1fKmA7F64IQUH834iBALZfvt7MgCcHjBDX-JDspCFjULFztIIJ07CKtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=cGSw8eMU0Our3OmGMo-gmz9BX0yIwe046TyxXJNmNe1kzlX0W58LYK47EXmDtzBk3btR2O3a3fLeecLYhVFgzXWZcq5eqz068UlkxmAEG-s58oWKr1G6Avi_bZNRVP3c33NZV-Jul4QmuYqORIBIU5nvCZtf44RQk-53upbg1ZZl6u8BIqDNmkxUccR7w0geUPEIYXVCDkS7EGaM9ueyuNGIVZykKRg6pRNCCZy6MTIneLijVRKhAtM3qLYajL3s1qrSVNtcilSW34WTiw_dCXZ2a1L5UzWe2RMWiYpwuN8uYMInAJHkmehdDLziZnPVz6n7KRx6BFPi8gd04OXgLG_PrrQoD12MdxMztOFyjlW_aHbJ5CtT-CORrFG8akGA34wIUZei7TKlJNhT4yLPlB1kBc7CZ-QsBTg15asHoDQR96VLsROGpbKIKeq6hHAk-6OF9oXt3xk5TZldolPek5Nz6n-kdw5NaZUZC6KpDmLCqwSJTv8a9U6vH-kzncZzZRH4k3NkFI8buXtnxnjdy1OSHkb4g5tnoGuQpmpVucVgkokpQ3xcYmalSg3XG9JsqnnmjcJ_TQvFWmbpEF5YWa8lnGoQQJ4cKWMAgAaU9T4Ft1YyCGEp7Om9GrBMqoOfl1fPtOn0Z3scOOlDb1uBjkRa2K0fUzAIiKR1q-BE4vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=cGSw8eMU0Our3OmGMo-gmz9BX0yIwe046TyxXJNmNe1kzlX0W58LYK47EXmDtzBk3btR2O3a3fLeecLYhVFgzXWZcq5eqz068UlkxmAEG-s58oWKr1G6Avi_bZNRVP3c33NZV-Jul4QmuYqORIBIU5nvCZtf44RQk-53upbg1ZZl6u8BIqDNmkxUccR7w0geUPEIYXVCDkS7EGaM9ueyuNGIVZykKRg6pRNCCZy6MTIneLijVRKhAtM3qLYajL3s1qrSVNtcilSW34WTiw_dCXZ2a1L5UzWe2RMWiYpwuN8uYMInAJHkmehdDLziZnPVz6n7KRx6BFPi8gd04OXgLG_PrrQoD12MdxMztOFyjlW_aHbJ5CtT-CORrFG8akGA34wIUZei7TKlJNhT4yLPlB1kBc7CZ-QsBTg15asHoDQR96VLsROGpbKIKeq6hHAk-6OF9oXt3xk5TZldolPek5Nz6n-kdw5NaZUZC6KpDmLCqwSJTv8a9U6vH-kzncZzZRH4k3NkFI8buXtnxnjdy1OSHkb4g5tnoGuQpmpVucVgkokpQ3xcYmalSg3XG9JsqnnmjcJ_TQvFWmbpEF5YWa8lnGoQQJ4cKWMAgAaU9T4Ft1YyCGEp7Om9GrBMqoOfl1fPtOn0Z3scOOlDb1uBjkRa2K0fUzAIiKR1q-BE4vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=F-jn8FQFFnHeSZnV632euVUHcCSM-y-KNsl8NnP5Rgq0rQfoNg7rP810_1JL1J8j_y5SjtH8tLgUcYR_58xzVcjBx6GhdaG9hvE68zA9aIXHFMvQa-isYyLynZoSeoRGgCWfnnOJUez-AC6u4IGtw5vx2D27_OqogErAZsahe0gDeUa70VpCLDkPPjWCNfsNf2jjUX1YjbmUe0v8310WpUa7Cp1p1pFQB86e0ofH0NS1NypDLiao80bB1DGUHHn_Ef7oxwmCP8_hbJgi99dm0eaNqGnIrOQaXQZvl-6sBCgasiQRfZlu4M7cZ8Dy0WcjvoGtmMePibw__CB5LLOdaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=F-jn8FQFFnHeSZnV632euVUHcCSM-y-KNsl8NnP5Rgq0rQfoNg7rP810_1JL1J8j_y5SjtH8tLgUcYR_58xzVcjBx6GhdaG9hvE68zA9aIXHFMvQa-isYyLynZoSeoRGgCWfnnOJUez-AC6u4IGtw5vx2D27_OqogErAZsahe0gDeUa70VpCLDkPPjWCNfsNf2jjUX1YjbmUe0v8310WpUa7Cp1p1pFQB86e0ofH0NS1NypDLiao80bB1DGUHHn_Ef7oxwmCP8_hbJgi99dm0eaNqGnIrOQaXQZvl-6sBCgasiQRfZlu4M7cZ8Dy0WcjvoGtmMePibw__CB5LLOdaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
محمد باقر خرازی:
اگه پزشکیان یک بار دیگه استعفا بده، مجتبی خامنه‌ای موافقت می‌کنه
.
مسعود پزشکیان تا حالا نزدیک به 28 بار یا استعفا داده یا تهدید به استعفا کرده!
قراره ذوالقدر رو از دبیرکلی شورای عالی امنیت ملی دربیاره و محسن رضایی رو جاش بذاره.
مجتبی به عراقچی هم گفته دیگه به هیچ عنوان حق دخالت تو مذاکرات رو نداری.
همه اینا همیشه تهدید به استعفا میکردن ولی از وقتی مجتبی خامنه‌ای تهدید کرده، دیگه فیتیله‌ها رو پایین کشیدن.
ماشالله مجتبی خامنه‌ای خیلی سفت و بی‌تعارفه ، پدرش یکم تعارف داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69503">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1MS15b02YvYr6p7aqxqBSuXA4Fig8pxKVxHO7ilGHx7qUZKQgehe4wvbQi-3cu0sbC4kDcNUUhxcbf8pA6rqQg4uSqxHk1Og8wmNYYvUvVIGAiwILw1rED8dSRyQaDbOyByzTOBIXifm67LwLCoQX51g4_b3CL4iuvhQKpbb2sO5J8F4d0FqHS8HqnTsgI2qRv5b2ZhCG3ji_DAqQVAfQ0RVJeRoIEX2QwRvCjcqIBMFRX-brxPONMu014xZz4iZ6UGYkmpnkRIeApN1uQitMKlO1t3k4PFcDYDA9iHowiKn47VG49PhMBAlKWHXnNE9ZR3Mso9payGKNguxN7MEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک کشتی باری در فاصله ۲۰ مایل دریایی شمال شرقی «الخصب» عمان، از طریق کانال ۱۶ VHF پیام اضطراری مخابره کرده و مدعی شده است که مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69503" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69502">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های حکومت از حمله به یک پایگاه آمریکایی در شمال کویت خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69502" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69501">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=g0UrDO9srL9FwfBvDlg9Eq7KHoYGJg3_yJSvOshfxbtvkgpeYRx9QkBkhY2dfRoBrd92jltja0Ms5ZD580S5F1lT8bwfKsDo3aJvXPfOtCWPqSExsuzw8B6fxEO7LbjMGNgM8JNDWQSttMrSxz6qZ3xwtJEeFmpWQkPFBABlAWM6loajeAuKSMQKLFODc0sQob1cxhdBf6idTOG93vyyNdEuBCV_-LP21YQPXABs9sd_ihs1qAJxFPZvBd_yVPCUny4nsZKeUT7xnFT51_1gRkjajYAB6Qho77Ny2jUvYnuduUPkuLe32rYz85gIb3z0NFsFruf-kC_YTKu3lnKC_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=g0UrDO9srL9FwfBvDlg9Eq7KHoYGJg3_yJSvOshfxbtvkgpeYRx9QkBkhY2dfRoBrd92jltja0Ms5ZD580S5F1lT8bwfKsDo3aJvXPfOtCWPqSExsuzw8B6fxEO7LbjMGNgM8JNDWQSttMrSxz6qZ3xwtJEeFmpWQkPFBABlAWM6loajeAuKSMQKLFODc0sQob1cxhdBf6idTOG93vyyNdEuBCV_-LP21YQPXABs9sd_ihs1qAJxFPZvBd_yVPCUny4nsZKeUT7xnFT51_1gRkjajYAB6Qho77Ny2jUvYnuduUPkuLe32rYz85gIb3z0NFsFruf-kC_YTKu3lnKC_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69501" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69500">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
منابع عربی:
شنیده شدن صدای انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69500" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69496">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovhE_no2saN-xZrWJv3WZQAKiTN_vPIagzuq-Bgke6VwQOnT9LxHGo9YuUNrQe6nBi-CYnUIT8vlhWq5WK0etWRjIJCdHiWjPVXb7dBL24FmnZ_aC54vEEmBQBwlFM_PH9x0a5aZXZILxbhv1X1JRSbPKd91Wvoq5orfJ6ryoBwD3WW0Rl_qRi3SEimk6hMPsW1xbDKdMkjG0kpRmoJhgTBIkQ1hwdiNL9lT3B7FTEnS7yPii8EaYY9GC8DoZr65-k8R0Ws1ZEE8toOltYpAyRSYvxa_PIUpRws0ci5IG8937VgLWbKM3QZxx6hG3uClPymkAD1yPL7LaSrQr0aH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=AyOAeIP5COWgwFqm2HwAdyhFvz6aN08ume6DRsRggYYh06QGLxHDUsw6fn9URSqm7Ovc9upmNQH8rLwnslSLtg3xDVPjsd0KmNEnpavxJ4jKC0ODeSvgNuJ1X4vhD3ObtP4WRNR2CpGcZKTNJoSuRSejcxQhzUyd-hK63ACoV3mtQ5qCq8APieFFNCJ6V3vCDOhOO-WU0gV29ZWltFlYlZPXGcz3-MogUUT6xix4q2uaY8AGH08XN7ZyhxuR05ISY7emqIPvX8TBKk98QfCAhB7Pvmp8RSJ8KNYYcJxDLpL9EN9HakCHSAGj0kbAIy2vnYoQxBYPgjqaM0nexQbh-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=AyOAeIP5COWgwFqm2HwAdyhFvz6aN08ume6DRsRggYYh06QGLxHDUsw6fn9URSqm7Ovc9upmNQH8rLwnslSLtg3xDVPjsd0KmNEnpavxJ4jKC0ODeSvgNuJ1X4vhD3ObtP4WRNR2CpGcZKTNJoSuRSejcxQhzUyd-hK63ACoV3mtQ5qCq8APieFFNCJ6V3vCDOhOO-WU0gV29ZWltFlYlZPXGcz3-MogUUT6xix4q2uaY8AGH08XN7ZyhxuR05ISY7emqIPvX8TBKk98QfCAhB7Pvmp8RSJ8KNYYcJxDLpL9EN9HakCHSAGj0kbAIy2vnYoQxBYPgjqaM0nexQbh-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقای سیاه‌پوستی که تو تصویر می‌بینید، رکورد ویوهای تیک‌تاک رو جابه‌جا کرده
👀
حالا کارش چیه؟ میره به شهرها و کشورهای مختلف و دخترها، زن‌ها و دوست‌دخترهای مردم رو بلند می‌کنه و باهاشون مثل دمبل وزنه می‌زنه!
جالب‌تر اینکه تو بعضی جاها، دخترا حتی صف می‌کشن تا نوبتشون بشه که ایشون بلندشون کنه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/69496" target="_blank">📅 01:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69495">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b93335655.mp4?token=jwtWt1H_5pxW7rxk_3k510s0Zx6aXqZzebQxuha-anMRIo2jfCAkzyFnVDmz60oBJKsXAjWiXARJuJPxMDIURs6-Z-yhqGLXNJTNwlwIxKiPLzykbVrzaG9jplWIZaXg4Hb3ozZVV0iiNLs9wcQNwV5dLLFiltmb9JVBibvkemErkx5pTJdVcYgbtZtU9TTstss7e66CqvUdC1SWp1CIuQrnCuk1POAAY0brJY5wwHLspxhQ2bVtMBtdji9AtgZt4fnJ1w1JnEGtAD5uOgQpggILApgtRh8Az-GBKm7SpeI4ATM7u5OduUiMU_IvG5d9QfgjAHMfuDLx7UBrRrkmMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b93335655.mp4?token=jwtWt1H_5pxW7rxk_3k510s0Zx6aXqZzebQxuha-anMRIo2jfCAkzyFnVDmz60oBJKsXAjWiXARJuJPxMDIURs6-Z-yhqGLXNJTNwlwIxKiPLzykbVrzaG9jplWIZaXg4Hb3ozZVV0iiNLs9wcQNwV5dLLFiltmb9JVBibvkemErkx5pTJdVcYgbtZtU9TTstss7e66CqvUdC1SWp1CIuQrnCuk1POAAY0brJY5wwHLspxhQ2bVtMBtdji9AtgZt4fnJ1w1JnEGtAD5uOgQpggILApgtRh8Az-GBKm7SpeI4ATM7u5OduUiMU_IvG5d9QfgjAHMfuDLx7UBrRrkmMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دست فرمون پشم ریزون اوپراتور اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69495" target="_blank">📅 00:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69494">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZE1qbhWaaouRpLE9gbWIJUw-ZTt-mnuwBRchlrqP7hwqR3YgLH-7PzXV9swTllSfNc6xte1bNu6BWRdKFh6wdbjj_-Lc7kqeTfHZYDAMJ1sadjZmuxOa95mcHO9cyFaLtvSoij50F---_PjGP0ncu_U6U4e-HVpeshCGp8HShVrJHZi-8aiBRjsaHofcTvQNNtjpcNDp7mN1k3HpJsOHzt9t1mNEJn7QUBxNrdSpQnrhRwxBleYsfFI4jK4gRbzT3qaFHsjNZfZwwJUp_EJYCa4J6SS0LRmYlLg9vY5bFMu363FytrfUX9xaRqIUAISEV_Rc8xpbxPqqrLUdVA49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
ایران هیچ‌گونه قصدی برای مذاکره با رژیم ترامپ ندارد. هرگونه اقدام تجاوزکارانه با پاسخی کوبنده و قاطع از سوی جمهوری اسلامی مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69494" target="_blank">📅 00:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69493">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=R0Kqu2GcqIF-2NPCUAhM1b6DC7NiQnF50u3JvecdP5dHmS2MseplM1VZzO4813uG9m7yRmfdlqSZjZvNHDKyyLdttN17wg1dLZukF6w7pMfSVLUnyYvcKLZhqt_EyecR7ec7oNRo8MR5qCh3QVmfxO3z8yFSyXxC-xP8dBwKZoLbB4XkOOhPw1N2OeR1PlCUeLjzy_huJspIoFPsMqJz7cNrRYDO50o2_waeNIKXppvAlnnl9Y4R_gXwrqOpy43CWpzC9F28wBwSlQumthSY7NrE-xGeZ1x2whuxD5e8Y0ejzIte4rhYCEQ-9T_PevPndgh1E3xUlXRqgaT9ldPgKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=R0Kqu2GcqIF-2NPCUAhM1b6DC7NiQnF50u3JvecdP5dHmS2MseplM1VZzO4813uG9m7yRmfdlqSZjZvNHDKyyLdttN17wg1dLZukF6w7pMfSVLUnyYvcKLZhqt_EyecR7ec7oNRo8MR5qCh3QVmfxO3z8yFSyXxC-xP8dBwKZoLbB4XkOOhPw1N2OeR1PlCUeLjzy_huJspIoFPsMqJz7cNrRYDO50o2_waeNIKXppvAlnnl9Y4R_gXwrqOpy43CWpzC9F28wBwSlQumthSY7NrE-xGeZ1x2whuxD5e8Y0ejzIte4rhYCEQ-9T_PevPndgh1E3xUlXRqgaT9ldPgKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
آماده بودیم به ۳ نقطه از اوکراین حمله بکنیم ولی عذر خواهی کردن کنسل شد
پل های منتهی به هرمزگان رو آمریکا میزد که حمله زمینی بکنه ولی خب طرح هاشون ناپخته بود
تو ۱۷ روز با حملات شدید موشکی پهپادی ترامپ رو مجبور به شکست کردیم
آتش بسی وجود نداره داریم حملات معقولی انجام میدیم
تفاهم‌نامه با موافقت رهبری امضا شد
کویت رو ویران کردیم و فرماندهی سنتکام از قطر به اسرائیل منتقل شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69493" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69492">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571743cf02.mp4?token=ludcAmqDAK4o4pyzAH_VNuPt5NEHjiiofrZbD2WBJ0toP2TW8WZ9vYrE2Ez0Q99uncOrRh3TYOOTNcIW4YIlFuTKRpmlE_jkyAjEZYC9cPQV-kJIP7dfM3wJnh_Gqc6NIT4eMFAiywFxxTEpVUvQJYQA1FMtZwNmgDWiyZ5YvVwwuuV9GlFIBxbkhi59Gsv762tEDY8K5OkJWLrrZfswjWkMlGZGwDxr-3FfMNLK27RGMhiAkWHNoqML7YprjC3ld9Ca-GSBnueZPkHyTTo_aL-u-ROxTOw1vQZWnjMxjW55DVE3a-DUoqR1_WG8V4n7R63HQ5rUq7dXooTcMSVTIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571743cf02.mp4?token=ludcAmqDAK4o4pyzAH_VNuPt5NEHjiiofrZbD2WBJ0toP2TW8WZ9vYrE2Ez0Q99uncOrRh3TYOOTNcIW4YIlFuTKRpmlE_jkyAjEZYC9cPQV-kJIP7dfM3wJnh_Gqc6NIT4eMFAiywFxxTEpVUvQJYQA1FMtZwNmgDWiyZ5YvVwwuuV9GlFIBxbkhi59Gsv762tEDY8K5OkJWLrrZfswjWkMlGZGwDxr-3FfMNLK27RGMhiAkWHNoqML7YprjC3ld9Ca-GSBnueZPkHyTTo_aL-u-ROxTOw1vQZWnjMxjW55DVE3a-DUoqR1_WG8V4n7R63HQ5rUq7dXooTcMSVTIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی وایرال شده از موکب خدمه ام‌البنین که به زائرا آیفون ۱۷ و آیپد و گوشواره طلا میدن!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69492" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69491">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6Q0GRN4j9q72kUWzichZnPt2dNBT2GaMtg87G1j8-gvnjPBnxoS5E67-_AS1D6P8lnHdovhVrsiXxULqXTkEAf-w0GdWuZRDVnpRMZox-fu7ntckjyuYbYV4HQt3l3r6OXhpUYktmCYyEj2dnwk-Z3mHLBAr46FH5YtbJspQ_bRYNjqKGk7CLeBw_35QxSHM3c-zOnUKmsbsCLyzhxRaBZUXrQojdOXsBFbhflfJEBms9DBwdykuO6uLnTmc5Id4yNDMWA1JBOR9DnCqql2YEhJisWDOSGyHgAdC0Ns3zbhp1ZS4wLJN8aWn84lPpZYSR0Sa7NoZyeGku-b87WlCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69491" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69488">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjdXrlPK7E8eddR3KzmNf2YF4WSAy0DW-PIOU7Chc1BCLyoCWuWyeQ-NiynmW432e-g-RhQFR3QDx3WWPHSKrBCuB5F-Wty9sXZ9Oyh-XS0zWIs0TTuClTAuxPi72CgteCkUwM5HxiQ3-DIsIifVTsvkzUkWw93UJ3J7MNC31jrLBWxXsBow3xIctYijz1AMyoXUk2RAQjlflL20JxqnQDVZ10pnMIw-AQSgtlfG1A98kaO6AqaTECXKSMgprDuKGH79gIYRVBPbyyDm3RaXM7YPwsFBDYMNP4TWVFZ7gljuxrrfTMIjiHxCe5I4Qg4C8DZhsxNE8qwbGS38MXhudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLw_Z3E9rj-rNuOxZsCmAMj_xyjCwVFmu3bElTuyKi_q7_2nzTnW_pvW_QVX1Fl44N1AbRv0SEjYNPuekmUHCr8HVvQhaCEYAAWJ70hM0Aer6qBIIpWX8CKG2v2Q5j6pADR7SB0C08NpSjpdTWqoyVVzb2d4tEH8IfmO-Z5VmgG4ticNSJN1X8xtrENND82jZ5BFDcqcWIT9-zkL9ZNxe4yfsq3j6WZGlvTE0CfFB8RI6Q7fztWNCA9rG-4hcHPkjO1OqYA5uyrYRy3H8Es8f7t0nrVoPmTr9UxhOThmAiLLdoBRKUDXF9pU7rkZR71tHW4Gw8dUq_8P3CkpxIOPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwrFdqFwGhkZW575z_Kc9TvZ9bSQXPt8t8qPB5-Y6r2rGTyTJXm8adB14L8j_Wee_Sd1YsncF_rPllDNeNGPgqKrlDahhUrSTd4gr3Fnhrfd4Nk5bU0rDy2YV81tM_xmVLpXkegRAFFVWsAc3vaqf2LwPZZm42Af-MpwNtnJwQDSuf0hTInfdvEPqSXip0dbnA02lL2EzMTU1r7skmvaf5uuwN_X0da24xj9584w_K7aWkORVAvW3D46JHmQqc47fBlonWKhvmApCkJP8UBOaccrDBgAyIUrn_kfyJC0eZS7d3x_3HSPBpPXXc2YrEkwkOKLoIQo9zyKwYWaAYxQeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کامنت های دردناک مردم زیر قیمت PS5 تو سایت دیجی‌کالا
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69488" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69487">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=DNtAxMJYbsdlNIW18FXR90PRXF8lyc2oQvrkJXByYdvn1CF_TWZZsgieZgPweJBFpeayvc8uPC-6fVUr9Mw24fpm2If0C6JN-NlGGXG8OQgXT4ZmCOnIuFzVL8Ad-HRPsT6uX7RclQQpkR21kIGh7sFeWEvVnm783WVQ5Pzq7JA9CDv2uBxVcgwL6lDiZT1K8yjYujOTuTSOT1YEun_GA2TsVeSCbM1dDiZxUUdqQbj3J79__EkaEc-nJlCcAXChrUNBCIPydML5j8URHnSWLhHGPcwyBteu5pQPEuDaQFMbutfpHXLEPnR6wnbln24MZjF9Gk-ug-x9okrZE77MkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=DNtAxMJYbsdlNIW18FXR90PRXF8lyc2oQvrkJXByYdvn1CF_TWZZsgieZgPweJBFpeayvc8uPC-6fVUr9Mw24fpm2If0C6JN-NlGGXG8OQgXT4ZmCOnIuFzVL8Ad-HRPsT6uX7RclQQpkR21kIGh7sFeWEvVnm783WVQ5Pzq7JA9CDv2uBxVcgwL6lDiZT1K8yjYujOTuTSOT1YEun_GA2TsVeSCbM1dDiZxUUdqQbj3J79__EkaEc-nJlCcAXChrUNBCIPydML5j8URHnSWLhHGPcwyBteu5pQPEuDaQFMbutfpHXLEPnR6wnbln24MZjF9Gk-ug-x9okrZE77MkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
✈️
یک جنگنده F-16 نیروی هوایی اوکراین، یک پهپاد انتحاری روسی (Geran-2) را با شلیک توپ ۲۰ میلی‌متری ولکان (M61 Vulcan) در آسمان اوکراین سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69487" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
