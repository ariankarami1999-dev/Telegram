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
<img src="https://cdn4.telesco.pe/file/IAp0lxosLpzmXajifemzV0lrtYevhYkhQGChPvGRd57HMR6sMQyEfKw3DXyE_S3eZGf0Va4qqSIMv7NP-K8-C3ow_sT935BmghzcPtOE55Z3s4SOcXu7P7n1KufUFDmso8R3xzeWRIMcrqcRpAogN96pIKtsuKjPNtk47E45V1xMJz1uaS6BOUacuqHHSBeBRk1JjtC0HE2tcC7epAZGccZm86GOB-D1YMgnrIQdtjBNefKpek94QydNrHhYxhfu5jnGkGUYud-AIqdJ7zv6bjO2a4BJmesqIleKW24frv_jl8vD7-XK3ZdAzon2yb3Eh4wZfl3mTtmfLUdw1jPJKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 134K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 18:13:32</div>
<hr>

<div class="tg-post" id="msg-69579">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/news_hut/69579" target="_blank">📅 17:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69578">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/news_hut/69578" target="_blank">📅 16:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69577">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu2t8zjQ699wLlxessi_d8uj-0P7Q84GicATwCZDgeLDuPZurMdZQ08ErbJJWGiFikXSgX8e9lNmFvEZ5Aiqg5TlKZ3yPENSLZl_WbWaLP7LRFEcmpfiW4RX5ck7N3sD5nEt0ktwPijyHvNorm_FIjZJ7KPbHUHvNKMfKwGn6iz-cMJhABd5JtgA7cGtAVABKFut8IqiwROtMhuwW-AHkQhhzJ3Q6n1b1HC5gLisb1id7wMIPk9ZzUY3S6ZX6X1q0ey4jo79FJGikHiKyZ_emU3MfGhbZyoRTjxtfSqjNZLBPOaTk1BTx3m209liR8-nTswSnBdic0Hab333N0Tt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛ ارتش اسرائیل برای شهرک المنصوری در جنوب لبنان هشدار تخلیه صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/69577" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69576">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69576" target="_blank">📅 16:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69575">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/69575" target="_blank">📅 16:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69574">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd7b_blE597c9V18S60V6KV18xaU2tgBsAhcL1z7icMSs-GIV1gfKogNqtbAHYj6JcFof4Gv21k_OWNiLjpHFIhfeZT7MDWTf7XXCOikGYEJ44tcSigW2b-dxVyqfmNwz229h2338vSfbH5Gcq1xSNTnYctxWV5ozx3U1Pt2hPMsV8OKykWuyYwGlc8kIzbF-qCm4WyRxDmace9hy3bOg8_rwZcM6HNfZ1Fg8Y62YneND2LnFdKuuUWYm15iJsIjiMd_sTRnob_GKfSgsOdvzjcR9AFpK_eJMsnPzmmBC-2iAK4q-3wRiZiyOTCX4PvZhXR4fvn7Uze5wNQRxP78fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💢
📉
قیمت نفت با کاهش های پی در پی به ۷۶ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69574" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69571">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/69571" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69570">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF5vycuiAZPED40pdet7bBmTMcJXa81xLU0ujb_9OwYuw2l18RVpAJTw3pGWBAOW_vS6DDym5AsCa7z4yPc5xtuSv3EkFeRK__zSEjx6Y1zXuH4xlJH3lv5B-cfeYj5CMlOmdjHKTE2y7Z7tp6sn4Ab85K63Q1DOcZjJyWISB05dTR4w657y5-o59d9usF05uVyvptI5fJzZdAHaGUEgw3ywo7OJZ_CLnkyXGRbFk7m_jDpX2uXWckpiYG-ZkLyVKM8p7hbyWUJp9LWNT5clGI-ZC9SmC4fEaR9BT0uc3vjEjdfpNn-K1HCU-SW_zbfAiQGCLgqQ6xsrohkVS6ICZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دسته‌ جدیدی از سوخت رسان ها برای مذاکره وارد اسرائیل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69570" target="_blank">📅 14:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69569">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db3cnonA-aY3BBQ-RTrETMfG_Pb2Z2pS4P6NAkg2UrswauH9cakLKHhJSf2L4DsoJmXIMt7Ws8y0Yck9jCroTPb1nPvPTxeBKfQozhhGSX6FUj2WMzAKmAhSUGlLWyXZuVp8B-g1ooH34eRX8VppN77TvYAh13dwNSe4cw2ds9xwNNF6DtyX3ROcTD1Ao1-6m03qggxuDdAy5btdZ9n06aW_ieldvBYoduR0IO_qDwjFjEHHewjP1Xz0pwoBj4p-_qoHM7GylzY8M5JDgksTMZChzCjaPzL4rW3q5yJJAGCDl5iLbdml46geB170ySNLIE9QMT5ybOlZHkLVi2Z19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
❌
حمله هوایی ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69569" target="_blank">📅 13:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69568">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69568" target="_blank">📅 13:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69567">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phgihB6RglSJEha4QerpHlyF7p4wA69xQj7mxULcANw9pyKATSBWbsUgQDwymmPuLRNMWL5WCUfIUW0h1zdefrJSnIIv3TDs4BbCNiryvZqhaBPnyVfCQNlfK4ZZ2SRLDAcO36FoG5lw1NeKFbaYhmSsF7QxGb9DR-ZKxWx5JAz3NdRi7cvjrvaD-7Bab_8yT2FLsfqa7cXx-woF7M0ooZCWF01otCxDTjBTjD2d05lFirweHToUSNCEffFaFxu-1XivNwfR6yEl9UWc4oj333htIwmiuiHW2wLdOPgJx1Fp6C9nGemcqBoIVKsHiW2QAXZzqSBpvu9X5JJYlMTfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دونالد ترامپ تصویری با هوش مصنوعی از خود منتشر کرد که در آن با لباس نظامی در کنار ژنرال پتن و ژنرال مک‌آرتور دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69567" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69566">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69566" target="_blank">📅 12:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69565">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=ifpHp6iNapfj6SbkxiKKGRS1bkQOTDDqGW4z5XBexaO9pfW2r4MU0EiPVBmBh-5Is8Qh1Im7jtO-UEyttdLCRoxm13ONCsIR3nOmzE4AOSH8kqkBuIxiX3ZTFrletD77b3D2IXRwd31tcUE2HVx7rBCplebI1BXJY323iRan6OGf_2GfLY95-1AAloVRZkRUeK3WF7oJiaDFi4r9xJfndoCuJAAfCdW-sguKiJMrFq-5c4JK-9lf1Gb3DHE8Bch9Roji7oNKydcVwI3CmKaA_MgmpM0F2dyPR4X78rism7HUXL-D--8CmhNtGUStRvt0CYco2is1XRmV8HIa9afgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=ifpHp6iNapfj6SbkxiKKGRS1bkQOTDDqGW4z5XBexaO9pfW2r4MU0EiPVBmBh-5Is8Qh1Im7jtO-UEyttdLCRoxm13ONCsIR3nOmzE4AOSH8kqkBuIxiX3ZTFrletD77b3D2IXRwd31tcUE2HVx7rBCplebI1BXJY323iRan6OGf_2GfLY95-1AAloVRZkRUeK3WF7oJiaDFi4r9xJfndoCuJAAfCdW-sguKiJMrFq-5c4JK-9lf1Gb3DHE8Bch9Roji7oNKydcVwI3CmKaA_MgmpM0F2dyPR4X78rism7HUXL-D--8CmhNtGUStRvt0CYco2is1XRmV8HIa9afgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فریادهای مجری کشمیری(هند)صداوسیما درباره تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69565" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69564">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69564" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69563">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/69563" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69562">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69562" target="_blank">📅 11:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69561">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=qWN8rEHJn6kfPrawv8SZ2sumGFcIcOAzfzX-i5NDvx1imgI6EJgpk-9hyiPyHlT3xSDa-joXwigfBS9ru8OD12NyTIaB75BGluDvpuhzq8dIbA0QH9lU0jSRaRjwr3GEO4brHTzZipRUDSLzgUlhImtOkoGWvRFaMst-SO0vYvnTOasP6Oap9i6o-V4UYDDgD8uDCusLlRluKiDLpm3HZMuNnVgDVIlXsqCwOkIpaA9tyOpASfVibF1tDqWd2sL3TaBs2dUn6par3vC1gC0UOdFYS9BiGBfBzDrNzlLrukYlEEJl74pRitVm-6SNMH0yIYkPvljZXf87Zxf-7l_nNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=qWN8rEHJn6kfPrawv8SZ2sumGFcIcOAzfzX-i5NDvx1imgI6EJgpk-9hyiPyHlT3xSDa-joXwigfBS9ru8OD12NyTIaB75BGluDvpuhzq8dIbA0QH9lU0jSRaRjwr3GEO4brHTzZipRUDSLzgUlhImtOkoGWvRFaMst-SO0vYvnTOasP6Oap9i6o-V4UYDDgD8uDCusLlRluKiDLpm3HZMuNnVgDVIlXsqCwOkIpaA9tyOpASfVibF1tDqWd2sL3TaBs2dUn6par3vC1gC0UOdFYS9BiGBfBzDrNzlLrukYlEEJl74pRitVm-6SNMH0yIYkPvljZXf87Zxf-7l_nNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکیه دلقک:
تا ۴۸ ساعت آینده خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69561" target="_blank">📅 11:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69559">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjSZUxtcYmQnuZ8I6JcM4NEJA0LgJ3tqJ3DlKo3xrfR4-qiLyLJftYrEikIqemF68aa7XzCnCNGEkkCXch5MAzVR9FLLZ0fftHkBQbiKn-q---jFqA75TCOsqFO8kN0HwkSzHtLi4_ECwrq538g_Si2EcPbxGInUwIpyecEwHHpTNvZZYqXJkZoTYwZsa1BuksHAMzLJb9oSZl1XtEAmHFiD3GUrYUMS2C1SwXpcbwh1Os5YSX9Yg8BTGsLCzOf4gaL9I-m3ewlinEqrIgKkyqytTsaVZGky2KRktciVBXgou4YhzIXBiI6dI9-mrQLNovHfKwJZddT7W6GG6pj22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=d9yubhK-8Sb5vq7G-badToAdPKxBXJDkpMay0Xjls14Fn9CzW_igDY8mTVxV6pSmPnRZQiOmHMOZSPSOmZfjpOSuBRsT01_ZaEpYiCdRO2MtxAe0yGBal3ZINivOAJyymdGVPgOksahEm4L7ZHI2Zvb2sPhC8Q6NGIkjmDMdwyx6qfTt79REjafTGStY0Iqf81kDT4Pm1w1eSEz8-WNocrYHWwUBsud31yAhPiCA8W93CybCjVFGJhdIcDWcWBNQYFAio06901XGaYzgyZwkzLgocHwQQOb0us34Cnl5MOzjVDC8mFlkkdCyE6Q1I67wy2v-kcIjTuR6HvmgQF-_kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=d9yubhK-8Sb5vq7G-badToAdPKxBXJDkpMay0Xjls14Fn9CzW_igDY8mTVxV6pSmPnRZQiOmHMOZSPSOmZfjpOSuBRsT01_ZaEpYiCdRO2MtxAe0yGBal3ZINivOAJyymdGVPgOksahEm4L7ZHI2Zvb2sPhC8Q6NGIkjmDMdwyx6qfTt79REjafTGStY0Iqf81kDT4Pm1w1eSEz8-WNocrYHWwUBsud31yAhPiCA8W93CybCjVFGJhdIcDWcWBNQYFAio06901XGaYzgyZwkzLgocHwQQOb0us34Cnl5MOzjVDC8mFlkkdCyE6Q1I67wy2v-kcIjTuR6HvmgQF-_kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
🇮🇷
جمهوری اسلامی دریای خزر رو فروخت رفت!
در تازه‌ترین قرارداد، جمهوری اسلامی دریای خزر رو تقدیم روسیه کرده و یواشکی دارن میبرن مجلس و تصویبش کنن.
سهم ایران فقط به ۱۱ درصد رسیده! شما ایران رو فروختین و شرمتون میاد بیاین به مردم بگین.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69559" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69558">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=HEIY2iQxUM20jNzPn4NZN7vdR_SYxEm094lqFeUl-237XJ0Hh1nr43WBy6mV3f57MKNXxNbPcxyaJxSSC-Eb9cY8s7wrnHmNRwSvTX8IorIm85kRafz1LubeiLiYXmzgd5ac9tUv_DYQqO2-I6WrhiocATFzIOw10Mdawl2LLWL2YmLm1R36XIktg5roYJ0KDuYRv-OkTNeMFHV23u8S920QTiZtzUYfHS6YOkZywZgBhhZrCVW2pNKMZx6pHJInRw6598Bnhlhij0nXywXBnhf18XxOU4fmAyd49VJUX8onDrb-ex3C02uKqseNMj_wpCNaD2JFtGp06zH2lez_DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=HEIY2iQxUM20jNzPn4NZN7vdR_SYxEm094lqFeUl-237XJ0Hh1nr43WBy6mV3f57MKNXxNbPcxyaJxSSC-Eb9cY8s7wrnHmNRwSvTX8IorIm85kRafz1LubeiLiYXmzgd5ac9tUv_DYQqO2-I6WrhiocATFzIOw10Mdawl2LLWL2YmLm1R36XIktg5roYJ0KDuYRv-OkTNeMFHV23u8S920QTiZtzUYfHS6YOkZywZgBhhZrCVW2pNKMZx6pHJInRw6598Bnhlhij0nXywXBnhf18XxOU4fmAyd49VJUX8onDrb-ex3C02uKqseNMj_wpCNaD2JFtGp06zH2lez_DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پرزیدنت سابق، جورج بوشِ پسر:
مذاکره با قاتلان، گزینه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69558" target="_blank">📅 10:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69557">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcljIWTQq1fJwSx03X_Cwed5Ku6pdpNWwKDPMBFXEKIazQ90U6zObHPGOAT5wv1Tudmm6VGCvpvFavCaDVacM_LnSj5AmdkQNGyKphl6KEYOnX0ZWx2TEg8NVRpau7XcsQOAZU8ERW0Y2w7ea6SDoL4KQCH5WdpFa7V_jXXKtH-muXAIcRT2M8hBHq-ggrWpuMF5isRSdNwJb53r3UBoOfwKRL98s4oXHjRiDd6K8g7mI74rxDshJFymeHij1L-fT_1EKqYPcZxS-v-w8YwiC3huHCawEl6nR7UY7GTfakf9AZigz3D_K0lYZfR1bvD7Mt4fMhCSKGoHMgnFQ2-_ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69557" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69556">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=aV6SOQAACF1NtH7Rs-r08wZG9dyrI791jv_mVJXybMHHltmZSwEKxWNpX_vlU2oAUnjsLfTkpT8uE0igCfJ0YkjGqpzHvYZ9jS-PlBd6Mcs-AZirceNcvdaOpq28SgMAZ6k1UeEOaavwC8JIy-8QLSkuz-FPqTuSGF3tuGSbRJVtLYZcHyQgNffWvdOa2mXLQxtW4ErQt994R1Rmo7RRaLom5Ikqu6J8NELqIekhT9UcM31YWZAKmlrOIDGEaTxMB78ZT1YTo3XtunErhH6aPWTDPPy1KzP5NiQWVqQMoWOJcFU1r7bhxMOus4-H7EzU2e-LUlkRuGDOLCL2k2KFR7pGhzbmCf9adhpRrEiQS8FDd78DojIyURUf5ZJRpftVUDkcDUzRmFV9Nb8OuJYlJldYLS9SFTai04vkzjlPLAD_0xt-G_YUYr8GlN3W4vpm9zVcCaN2-k3c0KAU7vKV_5r_4onpFFR4i4NR5z-p4AeBXgcV_nw_SxRn4qP7GD0RTyQ7nXTkaaFIizQiw8kdHwhG9mOQyNbW7lgb72N_AcNg8gMgeZYCH6MY2m2dOmESPUvJc1A7q9B-UE8vxvYnCg49h2x0Tbln233xAGb1dUDiJlwdLdxT79Rn963mppmBIeTihuab-KMvdl3-lzuiWE5fq8XyGImTXLCwW5LMke4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=aV6SOQAACF1NtH7Rs-r08wZG9dyrI791jv_mVJXybMHHltmZSwEKxWNpX_vlU2oAUnjsLfTkpT8uE0igCfJ0YkjGqpzHvYZ9jS-PlBd6Mcs-AZirceNcvdaOpq28SgMAZ6k1UeEOaavwC8JIy-8QLSkuz-FPqTuSGF3tuGSbRJVtLYZcHyQgNffWvdOa2mXLQxtW4ErQt994R1Rmo7RRaLom5Ikqu6J8NELqIekhT9UcM31YWZAKmlrOIDGEaTxMB78ZT1YTo3XtunErhH6aPWTDPPy1KzP5NiQWVqQMoWOJcFU1r7bhxMOus4-H7EzU2e-LUlkRuGDOLCL2k2KFR7pGhzbmCf9adhpRrEiQS8FDd78DojIyURUf5ZJRpftVUDkcDUzRmFV9Nb8OuJYlJldYLS9SFTai04vkzjlPLAD_0xt-G_YUYr8GlN3W4vpm9zVcCaN2-k3c0KAU7vKV_5r_4onpFFR4i4NR5z-p4AeBXgcV_nw_SxRn4qP7GD0RTyQ7nXTkaaFIizQiw8kdHwhG9mOQyNbW7lgb72N_AcNg8gMgeZYCH6MY2m2dOmESPUvJc1A7q9B-UE8vxvYnCg49h2x0Tbln233xAGb1dUDiJlwdLdxT79Rn963mppmBIeTihuab-KMvdl3-lzuiWE5fq8XyGImTXLCwW5LMke4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69556" target="_blank">📅 09:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69555">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d290294320.mp4?token=rbDd-MLPSkqIp3va4q9ewfqOa_FNzyuqiqeWPsldh4MGMrH0fr9HiaaFne_-GOc_EwTa2k06f38QxNahpNz-u0BZymvulbSQOPnf7DYomXkltmG0qiMhPyizsH6PWe4dkFH77J5hdnt9Ss88nBtTr6MV2jEUfpU3ba5tthz-jJ3GsEQ0rYftrpGawdQoL7YjTgVF0QTZXwlowa-nM03qK8XkDg9Gc8AaJubIzajnFeHi7WL9yArLJhcVneIvXrW2jwIfgWXfi0UaaGUMCcau0MOf0kjR626TlT3fKDOuKB6YUHu4Tvi-h4eTiGWx71xFm1mE4cNAh2GmNs17n4GcDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d290294320.mp4?token=rbDd-MLPSkqIp3va4q9ewfqOa_FNzyuqiqeWPsldh4MGMrH0fr9HiaaFne_-GOc_EwTa2k06f38QxNahpNz-u0BZymvulbSQOPnf7DYomXkltmG0qiMhPyizsH6PWe4dkFH77J5hdnt9Ss88nBtTr6MV2jEUfpU3ba5tthz-jJ3GsEQ0rYftrpGawdQoL7YjTgVF0QTZXwlowa-nM03qK8XkDg9Gc8AaJubIzajnFeHi7WL9yArLJhcVneIvXrW2jwIfgWXfi0UaaGUMCcau0MOf0kjR626TlT3fKDOuKB6YUHu4Tvi-h4eTiGWx71xFm1mE4cNAh2GmNs17n4GcDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69555" target="_blank">📅 09:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69554">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=agHeGS9OsGj0xZkKIJT1scMTMy2EyarruO8HtvTra_m5gGz8R-ezq7okB9iFt_Ne3ASGO9AuBdxq9MM-m0RFFeyyk1DWpJi9_WHjOUe3_LYGQ2c-nXWxRjnYG3VtdTwfEHNVwAMyHwko6ozS6aZcctmJaS5BN9Qe7UTroAhW3MjGnE5uNGdOnrJ6PW9epXsj_zwBygct4aAn3TAB3KD5uZKk4g7BauibZ4PnIlUsbl5c8hnIyJDDAkGGviZbHsAvcYLottEqMC9G4aHpg1QzFeT9ThFE6EhNdzFuQyo837fBWnrCCiT049-XX91gmR2TcfhayS7dJ760GGV9azKg-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=agHeGS9OsGj0xZkKIJT1scMTMy2EyarruO8HtvTra_m5gGz8R-ezq7okB9iFt_Ne3ASGO9AuBdxq9MM-m0RFFeyyk1DWpJi9_WHjOUe3_LYGQ2c-nXWxRjnYG3VtdTwfEHNVwAMyHwko6ozS6aZcctmJaS5BN9Qe7UTroAhW3MjGnE5uNGdOnrJ6PW9epXsj_zwBygct4aAn3TAB3KD5uZKk4g7BauibZ4PnIlUsbl5c8hnIyJDDAkGGviZbHsAvcYLottEqMC9G4aHpg1QzFeT9ThFE6EhNdzFuQyo837fBWnrCCiT049-XX91gmR2TcfhayS7dJ760GGV9azKg-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازم ترامپ از ترور جون سالم به در برد:
⏺
فاکس نیوز؛
مقامات اعلام کردند که یک مظنون مسلح به نام «جنین جان تائله»، ۳۸ ساله، در زمین گلف «ترامپ نشنال» دستگیر شده است؛ وی متهم است که پیش از سفر رئیس‌جمهور ترامپ، تدابیر امنیتی را زیر نظر داشته است.
پلیس اعلام کرد که متعاقباً از منزل این فرد، یک قبضه تفنگ مدل AR که به‌طور غیرقانونی تغییر یافته بود، جلیقه ضدگلوله، خشاب‌هایی با ظرفیت بالا، مهمات و دفترچه‌هایی حاوی «مطالب نگران‌کننده» کشف و ضبط کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69554" target="_blank">📅 02:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69553">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش پر حاشیه در آستانه پرسپولیسی شدددددن  https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69553" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69552">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8GjKeDsmjXIxxnFEomLQ-5ykilfp_a4WJNOuAWdP4ngAIGHJEa0qn9za8M7x84s7oL2IlSu7tBjrrpDRPc_smDrH3TrezIqKVeX53XNdz3c05f14jfzDxxTfc73WJwBgXTFimdqZ0PlTi39if4ml8ed2PAFMcYhl4QeP33wAoxbSNkfIINRdsGaSHRv43Lzp6UwAFd4h2ELbfvScTj7pEe-k8VzaLQw7Q3sD6038gaQcyY5l9-IIMgIiDXmkddy9mYswHIGvk-QHBXxIG3lBG55YDXpKAlcrGPU8hWE38EX4cUtrnD1t10ELk1po6-3pkfIoBWeHAbnzA_1tZQ7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و پرسپولیس هنوز هم شانس رسیدن به هم را دارند!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69552" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69551">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjhTbHSzWrpmmcqdvLYpogz5smzlz4xVlqJArkjTZPcDxOk0AGcVth3XAUyPA_M94LfNyPLNZHG17AqZrJwW0gVWyZesVHOeoeIVjpK1mzgrcjm2fGN02eQ2-WyVSNy1lZY_0ZDsGrzMdQ9q1ZwZNq3hoaaBx3EgcuV_HZ1jTs-uvbunrsTv4PD44sXKOmmgYTGYhr7OghcHFehqGjulNt8rRJNJFdZRsr4TiI0BFinwaHGr3TSncbf-G1qZPTv7z0z_LlrmYcnck8ZFosvZjEdKWwV53D2euDaZxS09pZoE0sCemtNi9oGZywXtFLCHhvKQ-g5bKElrnHwrtxJPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیزارم اینو یادتون بره
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69551" target="_blank">📅 02:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSpbY4Bn7879deH84mNvbQG6eEY5xp8YLtbpWlTY_Y7i0cNlWwI0EgFY3lpPilI4TvtI1lG_zpIQOZfcl5Rg3iPuiGDHYUkJUZp02BJ1d81gCMUhhNmOFz5PO_aLy3_89wgxnnQFHe8FSjLjuXUD94qPcWGFOOeECLwlgtcCYsMaSRpsYH8VnPVR5iJZ4zk45vTD8xaEzRQ9lF49xb9GjEZ2j7GV9Yzl8XqvL1volnmbTLdiDJP6fmn2b4vfRzW097i75HRR87LCo-QeTTfeogAsgEq3kG-tQZGVaXHNY2dxhcu24vfWFoITJsQPBflWrGhzs2FLYl56z4Hp7mF3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RI9qXqxAS-W5IjzCRJbc0VhJf0UkgZUBJFu_6KyEF93fBFENUWLTI2MfpMBom6UBOmkK8ZMYzGYjfl9H3hIwltjIftU7NxhPvqbbCSctnyUHvBsZawSEKOA4xOHp5MmgxSab01T1_cnkPm9Fi3X8qC5G6OjQnlnVN9GPY97dOm6MJnZX2iEFRoW0k6AmPFMfNh_lJXmD7rWweKfP2BabbUngtA-WeVjxkuuX_6ftpiM7H6ZcLTNqQio3JOVGeDUvNcsVNFuUUSzYg9rk8f9aruKdJu3SnZ6831cErQjxT__lp18asxCZPTQwrxJ_12l3Mr-csTWTTkeWdoSM6E9u5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=bShf72abCQ-80qSUO8L1lesfjTCtcXbmyrDs5jm44qxVQuHBBIWpPWobSB4eui4RzFKIh4P-XzeIv_RC6XtxAf0aWQRgPX8XHkJLzq2OCuQ4fB1gEWyhb04Wh1N1nLxY9-65PVNeTBXXmljd4KiVLGeZwYa4KXdLOmcOIozBBC22lVC_zIg0EZi8PE8WKgmBVm-8k4R0qBKYtXqXPyPf4phRWqYeFwavuEUfDKgsU75v6j5jN1pz1A84SRRPbQ3D0Q2VSYblWzD-7Ra7LRBgYiyHxdZrsPEiL1GnwnD9t59XFyPp-7W7oP9F_dCZppW67tMohygvP8j0CmVrfCs5LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=bShf72abCQ-80qSUO8L1lesfjTCtcXbmyrDs5jm44qxVQuHBBIWpPWobSB4eui4RzFKIh4P-XzeIv_RC6XtxAf0aWQRgPX8XHkJLzq2OCuQ4fB1gEWyhb04Wh1N1nLxY9-65PVNeTBXXmljd4KiVLGeZwYa4KXdLOmcOIozBBC22lVC_zIg0EZi8PE8WKgmBVm-8k4R0qBKYtXqXPyPf4phRWqYeFwavuEUfDKgsU75v6j5jN1pz1A84SRRPbQ3D0Q2VSYblWzD-7Ra7LRBgYiyHxdZrsPEiL1GnwnD9t59XFyPp-7W7oP9F_dCZppW67tMohygvP8j0CmVrfCs5LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
حملات شدید و سنگین روسیه به کی‌یف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69548" target="_blank">📅 01:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwegdNTHBifrCNGBYkygHXxegJAtLzJ0gy0XVuQg9cqbu5Tb_JUR4qnuDx9M0nPGgkQW20_Dtc7YJ8SvQuFKuQhiDddKBIAYvvAj4-1VcShCCowlGtSuPxOvGrv43LHOLCk1sKpS0hsx1oPPT-iKCSCwQ9DQrIESA-gfgeIKSil8ttHge-mvj1ZgtyBTVOQWrWtfILl7Y9OToksYePyK0Y4Y_z4CtCRHYSAVuugll1RWITzgvNMVTyQQW7Co0A_GklGMMrLrNqanr_fLnqGwGhUzeSa-I70N75xumWrpIUW4hVCZO2k7exzxFrHawFsXiM6UPeerLnzn-D0zH78lPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69547" target="_blank">📅 01:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKNadVKoMJvUOBHv1cdMsdv45_D4I4Db54hi7DvcmuqGrfz32sWoxNzS6yvCsvTXAhC_CWOo6lx9-xVZ3n21RYj81Ehpy_Ah2D7LixZ2aUpaXQ8u5ybZ-9Lk_4NtbpN8C-uVvZmlUXUozhUFWnzVcQlXpundYy8fHkvO_4W-sb2mnqurQQhzSpcC-ZUSXbpgC0DZwUdth5VaSatZsTd5nukTjt2qSntXShh8h8SfG5e2ie0a1tlbinczIFsh2lJe5xyVaXHiBlk0H71n36YuX4-H_Qa2IznzxoHDYolJK7h7bSmRnRZKKTtosE4dhIAXULB4G81dUFybIo21I8VauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
بازگشت غول‌های سوخت‌رسان؛ بزرگ‌ترین آرایش هوایی آمریکا از زمان جنگ خلیج فارس ۱۹۹۱.
پس از پایان جنگ جهانی دوم، جنگ خلیج فارس در سال ۱۹۹۱ با استقرار حدود ۳۰۲ فروند هواپیمای سوخت‌رسان، بزرگ‌ترین تجمع هواپیماهای سوخت‌رسان در یک عملیات نظامی به‌شمار می‌رود.
اکنون نیز در سال ۲۰۲۶، با استقرار حدود ۱۹۳ فروند هواپیمای سوخت‌رسان در منطقه برای پشتیبانی از عملیات علیه جمهوری اسلامی، یکی از بزرگ‌ترین تجمع‌های سوخت‌رسان‌های نظامی از زمان جنگ ۱۹۹۱ شکل گرفته است؛ آرایشی که در بیش از سه دهه اخیر کم‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69546" target="_blank">📅 01:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOtVA9SXgZTpcKpebpq70qLfnxzJA0h8cM3UwMLFDmmHJMuNOOidUGelnvwOrma2uzCU588e_i9WKNtoYTUiTwcLKeA5P56f13zUGf6KE_xQYa2FMf8QaCZUFFV3XBy4pvnkNYpM2tXkNu5hMBYvEVipIRD8O_rDXCZvMcMtalhZ0FiIdyCMK7K9AMK3-33r08MiJ40TtWZts1q9y1SYS0aQgrYPwkPFRoVfMLesjrAuXcLwf5qfWzHGLQyZJ3HfA0FSTzPEK_OKpmTnvPPTne8J17zTibrD4p-HWp69drIthbciroHkhDy5zp2PKDOVk5AGRefPn6HU87Z9QYCMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:مسیر جنوبی از طریق تنگه هرمز برای تمامی شناورهای تجاری که قصد عبور از این آبراه بین‌المللی را دارند، همچنان آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی علی‌رغم اقدامات خصمانه و بی‌دلیل ایران، به بیش از ۱۰۰۰ شناور برای عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند و این ترددها همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69545" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=NF8r_k3izn7kM5-PnxUIThmfeLFPbBf2iVGbm0fgpNaG3doGaSXjaUkRvV2pDuUjYrWkBMcRFhgaoVOT5v299wDLbpK8q6xzH6TvgOYyQeEfcOfz3M4YYK1dzYsj1-VPcD73f5VYKKvN8RMJ1wARO4bQ7a0y1rzQAEGgPY0ddgE1j3tDt1_UEl6TgxgqlT7erpa-JbifGHHklzYb613MtGavgLEK5rWkY_ZXJsgHChyShbDT7WOkx11gGVz-R4MNCiL7giUMUfnhg9Rz5ATyd4MMMMvSmAEkC4Ktp0cobeAeiLt-AaY-3Ugg4VcoxE2L3DU6TRY8Xc-0pClAKzkgxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=NF8r_k3izn7kM5-PnxUIThmfeLFPbBf2iVGbm0fgpNaG3doGaSXjaUkRvV2pDuUjYrWkBMcRFhgaoVOT5v299wDLbpK8q6xzH6TvgOYyQeEfcOfz3M4YYK1dzYsj1-VPcD73f5VYKKvN8RMJ1wARO4bQ7a0y1rzQAEGgPY0ddgE1j3tDt1_UEl6TgxgqlT7erpa-JbifGHHklzYb613MtGavgLEK5rWkY_ZXJsgHChyShbDT7WOkx11gGVz-R4MNCiL7giUMUfnhg9Rz5ATyd4MMMMvSmAEkC4Ktp0cobeAeiLt-AaY-3Ugg4VcoxE2L3DU6TRY8Xc-0pClAKzkgxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم.
می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر.
همه مردم برای ایران سختی‌ها را تحمل می‌کنند.
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69544" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69541">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/My3Bmz3aIJEFchM_cPpyN4ENUzealH2VlLpsAQhBk4Is4hXFuFYxcjtj9Ka5UlVYtQww5bsSVhJLRAMQQWjsY86VYibpd0ZaNAsssCxYFXnvvRhAcskhi1KTxqgsk66atQNq7BaZXckEgruKREnYoDeKT2mGxL4_r94O-G2BNvjAT_e-Yrhop_l-sHMrJu_wQoAtb2t47XNC3pwKIVjv5buk4NWakWy1GJPm6LtCbSmyh3r3DpbuDgVEpivtuSFnVm-TQy5y4WKbyMDWXTlbWZT2NxFunzwrhqcyGjkb93Fc9zLzMB0qye42EHqDpCVVTzuHYZgwAmvttvGICcb-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KBULGeAgwqa5u_Sp_hgTFEL35SwXNO6tBLVG1VC1fZLesRD6638B0U-ebN8tv6G5Qjy3sGg8C3wUUYivpmwlnUr2HuMf4ZSWWy5XX5a9CLJMdM6294jnNGR6HmBpHM9i89DGaZtdktnAKeThIKPXl9XqJl5SBeAtbGl9mBe2v633B7Km9rL399HQ7qQ8vx9LiN_YdCReGOGGiyL77fYLrbdXoxW64EmIp_w79Hi7rQ20D50e74PXUL7j5rfYhaddn6LKplpmuJayMiXuhym5SBhLnUwyvUCWAC6GAnHiFnUrXn_z9kqF9x5DwkN_0W0txXfI42dk2KKvRDWd8c7ung.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69541" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69540">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqlQULPdVJ2g7uzSiDnzDZHk3mWOiJgitPtBC62RbrL-hnoQ_NnKOx0ktKqSv02HHmiLPCBkIjpo6UtaZAw1jB1_Phls2W44yOKTFZ7KIrxq45-8XrEYzITOOMLds6Jpr5hnmMEFEpAaA8eHnmEUqxpbPZbhgWqUg26im84LAaAixIzfg9MnBqS5fRlpgSmZRlazHtb0W-pwJwT8ilr8ittgW9crOMSsbN53HaNXnTZUYFTNMMawQeEGxiwd2i-sZAoIsJeXJZ-szUKzqonLLXsawNJrTKLfBMqw-y-zj9KM_C0Dm72cvZKg_ecKANn_n4y67wCZpbgX73holZQB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
نقاشی وایرال شده از زمان قاجار:
در زمان قاجار زنان روی یک وسیله تاب مانند میشستن و یک زن قدرتمند، اونارو بالا و پایین میکرد.
شاه یا یکی از سران مملکت هم اون پایین دراز می‌کشیدن تا زن انقد روی آلتش فرود می آمد و بالا می‌رفت، تا ارضا میشد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69540" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69539">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=BhTGwk1KNBVa_dce1-udH4-IPaiDIC3Krs2pkI6yQFibYkcMMLIeJaWf7G0rm07XBlWdcATYoin8bugTOLioUUW3cOr2On3BtEisITPbKzbkeMFLSriCmApUt3Oh429d3dLhpzCbBSkS2HFcWbEO_UbhBqdq-78kZk2QfSJAjgxh2EzMX6xTi1tlYiBXw5w-XE5IRO4O2ImxzKtRC3NVN6x1wosEYetXECNE1sVQG2jOSNiTGCbT9gin-Hfe3HGneQUefqh5MeXAz2w6v_HGT2YrpGJ2DibfHyYkGAfCqZ20WqB0JjYwRuq-uaQqER-nN99QwRZjojxf_gkTLdHC7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=BhTGwk1KNBVa_dce1-udH4-IPaiDIC3Krs2pkI6yQFibYkcMMLIeJaWf7G0rm07XBlWdcATYoin8bugTOLioUUW3cOr2On3BtEisITPbKzbkeMFLSriCmApUt3Oh429d3dLhpzCbBSkS2HFcWbEO_UbhBqdq-78kZk2QfSJAjgxh2EzMX6xTi1tlYiBXw5w-XE5IRO4O2ImxzKtRC3NVN6x1wosEYetXECNE1sVQG2jOSNiTGCbT9gin-Hfe3HGneQUefqh5MeXAz2w6v_HGT2YrpGJ2DibfHyYkGAfCqZ20WqB0JjYwRuq-uaQqER-nN99QwRZjojxf_gkTLdHC7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای از یک پهباد روسی که یک شهروند اوکراین رو تهدید میکنه و در آخر هم خودشو میکوبه به طرف و منفجر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69539" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69538">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3447971507.mp4?token=MCgzKMqe9-Gnb2v8cMzWCsCeftEzNfR-ctdysxOL_Ct5gj0rRmmtFPW2HipRoRE0xQzRrdw3HyRh5KEyaInXvjmaaJfcSFaYkAL7FRg9uvSDTUSBkm-yrmzKSAMg5g6xo1wf8LsPc-6qJtc8wuUWY4w8Q3cmlKS7ZbUFp6T18EG6h6Y_CQHp7KpMJQZqKdDyDtV1D3zPBltmNKk6ECengDIBNY5YGlC-2wLlHXpB3y-oHxDc0aCesBHClKSoMh1wKUEb2Kh_sPngDOwkpHuVJ5EOforh2rPfxxhHEC9c8St-vkyXC_OD2k9MobzW0u0QU01bzizq4zT6qnKJTbgZ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3447971507.mp4?token=MCgzKMqe9-Gnb2v8cMzWCsCeftEzNfR-ctdysxOL_Ct5gj0rRmmtFPW2HipRoRE0xQzRrdw3HyRh5KEyaInXvjmaaJfcSFaYkAL7FRg9uvSDTUSBkm-yrmzKSAMg5g6xo1wf8LsPc-6qJtc8wuUWY4w8Q3cmlKS7ZbUFp6T18EG6h6Y_CQHp7KpMJQZqKdDyDtV1D3zPBltmNKk6ECengDIBNY5YGlC-2wLlHXpB3y-oHxDc0aCesBHClKSoMh1wKUEb2Kh_sPngDOwkpHuVJ5EOforh2rPfxxhHEC9c8St-vkyXC_OD2k9MobzW0u0QU01bzizq4zT6qnKJTbgZ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
چهار سال پیش در چنین روزی، یعنی ۴ اوت ۲۰۲۰، انفجار بندر بیروت — بزرگ‌ترین انفجار غیرهسته‌ای در تاریخ معاصر — پایتخت لبنان را ویران کرد.
هزاران تن نیترات آمونیوم که به‌شکل نامناسبی در آشیانه شماره ۱۲ انبار شده بود، دچار حریق و انفجار شد و موج انفجاری ویرانگر ایجاد کرد که چهره بیروت را در عرض چند ثانیه دگرگون ساخت.
این انفجار دست‌کم ۲۱۸ کشته و بیش از ۷۰۰۰ مجروح بر جای گذاشت، حدود ۳۰۰ هزار نفر را آواره کرد و خسارتی بالغ بر ۱۵ میلیارد دلار به بار آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69538" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69537">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=MXekHXz3KebBU53S8sr9JIg8LV_RbBzKuibwoxpVQC3PMiLR43GdOd7HLaZ-BI7mQ2hST_RSuZHOH4YhU2mGLGt5rGo89hHQJsjPn_wD_m0uTA4SseDJD5jH2MyDHGPG_E-aCSDcSpYM83x2SQ96mLh3x5sr_CLMzPNjYfpeAL88HUtvuoz_n4N_yF2sZ79DpWpD78kz54DbsXiOJsp7fMdLEpXATiMSIw7OxHQZh2IoySGP6EeO8IVthGFbCQIOIwzaeW9zo40gATXV6Deoh7MYGZM_NCJmPpmbLKAzqukA3gUKrVElConOyXR0SybKUhbdjdIdnkjrSBaonBaIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=MXekHXz3KebBU53S8sr9JIg8LV_RbBzKuibwoxpVQC3PMiLR43GdOd7HLaZ-BI7mQ2hST_RSuZHOH4YhU2mGLGt5rGo89hHQJsjPn_wD_m0uTA4SseDJD5jH2MyDHGPG_E-aCSDcSpYM83x2SQ96mLh3x5sr_CLMzPNjYfpeAL88HUtvuoz_n4N_yF2sZ79DpWpD78kz54DbsXiOJsp7fMdLEpXATiMSIw7OxHQZh2IoySGP6EeO8IVthGFbCQIOIwzaeW9zo40gATXV6Deoh7MYGZM_NCJmPpmbLKAzqukA3gUKrVElConOyXR0SybKUhbdjdIdnkjrSBaonBaIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ترامپ و تیمش تصور می‌کنند که می‌توانند حماس را به خلع سلاح و غیرنظامی‌سازی غزه وادار کنند.
آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم.
این پیش‌نویسِ ما نیست؛ ما نظرات خود را ارسال کردیم. ضمناً، ما نظراتمان را پیش از آنکه شاهد هیاهوی رسانه‌ای پیرامون این موضوع باشیم، ارائه داده بودیم. موضع ما همین است.
و ما بر سر منافع خود، هم با درایت و هم با قاطعیت، ایستادگی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69537" target="_blank">📅 21:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69536">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjVzAoFY2fxI5XqLi5wBFKNJhhZ_NZXUDNJC99bCXvmKLkRNI7ghGf6TuJZ_3f1L-SmoakjKhf88l5NjrvSjhMUuQ30gnb6RqdP4dvHQQmhZP6fJ6ELMnlgfSuG6AruxlmZTLpJ9qPjDXvHvE9w9DvcXtszw58D6k9boIFjKXa1pxD20eyyyT3kXWHAVliTZ1f_eOazPMVzSQeLWXTYkZVUI9sQAj4q1QUJWpKCIp1wxWnRPn6uMJG96IFq5O_eQGm6Jr5ZCAkLvo5_PKgmGHKO7etofYNyNtwHJDG4pb1SJs3RE1FOv0r5Ko0W22qWrU-QRy63LGiSRWKWKoSlQZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال‌استریت ژورنال: در حالی که دولت ترامپ بر نزدیک بودن احتمال دستیابی به توافق تأکید داشت، وقوع حمله‌ای جدید به یک کشتی در حال عبور از تنگه هرمز و بروز اختلاف بر سر مسئله عوارض در جریان مذاکرات برای بازگشایی این آبراه، چشم‌انداز این کریدور حیاتی انرژی را با ابهام مواجه کرد.
به گفته میانجی‌گران منطقه‌ای، بر اساس پیشنهادی که هم‌اکنون در دست بررسی است، کشتی‌های عازم خلیج فارس از مسیر آب‌های ایران وارد می‌شوند، در حالی که شناورهای خروجی از خلیج بدون پرداخت عوارض از آب‌های عمان عبور خواهند کرد.
میانجی‌گران اظهار داشتند که اگرچه دیپلمات‌های ایرانی در ابتدا از این پیشنهاد استقبال کردند (زیرا تا حدی کنترل بر تنگه را حفظ می‌کرد)، اما تهران خواستار حق دریافت عوارض ــ که احتمالاً با عمان تقسیم شود ــ و همچنین دریافت تضمین‌هایی در برابر حملات مجدد، پایان محاصره دریایی آمریکا و کاهش تحریم‌های نفتی شده است.
مقامات ارشد منطقه‌ای اعلام کردند که آمریکا و دولت‌های منطقه با درخواست دریافت عوارض مخالفت کرده و خواهان تضمین‌هایی هستند مبنی بر اینکه ایران و نیروهای نیابتی‌اش، قلمرو آن‌ها را تهدید نخواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69536" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69535">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtTBqr9Y7cJXGgnVFOy8H_sdB1-MaofDDq0z1SwI483rFyFyZyGAeGjC_d5p84ZkzcHdEGScrn-WzoPYHlFBthgEB0nXQPZuKkqCw5ZJ4eWeuAFPfzWUkDONwYtVTlHjqHYjrVJII7ScgQZZUWW10aH3KabXyAAmlCxclaKUdNbmqJJSP9bjqimh1jErv5tBkbsGX0dZFLoaSqYc1qZvfaQOYuI27pJNbhqD_J22mafhFP75zdSTpOVQz8gu66UStk3a5UkuSH5ZMM3ZP-A_1WGuqtkvzJOvyqGvAx-RJKTKUT4lT--Vl1EzzWLCIaUeXZ1TDre6SzwB7XwEciiGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:یک ملوان نیروی دریایی ایالات متحده در «مرکز اطلاعات رزمی» ناو «یو‌اس‌اس باکسر» (LHD 4) مشغول نگهبانی است؛
😃
این ناو تهاجمی-آبی‌خاکی در حالی که از محاصره اعمال‌شده توسط آمریکا علیه ایران پشتیبانی می‌کند، در آب‌های منطقه در حال حرکت است.
تا تاریخ ۴ اوت، نیروهای آمریکایی مسیر ۴۵ کشتی تجاری را تغییر داده، ۲ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی دیگر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69535" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69534">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=YXUIqEmlANW7R3PJ0uO_mxc_NEmurAiBX_VKsJTAVwi6wv1RFs1NcBYFVFzflsATgT3t87ovmoVvq3aGV5plrmiyuOwCgE0KIvlT5MQ7vgXjp0yjOT-q7EkR5jGOphrmq5nLCR1selLQDb7RsRHS-ds6iQvmTrRKKuEhXRbIMZnxz5dr9uRosJ_XMtvZUOuhWdhDFFvsUi0I8s4mwoRgUQGw_Z0t6z1nMmo-wXF8DEsxhjkeXn2uMM7MYYTr3taODhpgPieBR-ywwt6qsQukviqXpyNSErc767XclgNncwqH_FzMAZxZRNDWc-52Sk7Yuq_hNOdlN1FhSZKYLKBCrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=YXUIqEmlANW7R3PJ0uO_mxc_NEmurAiBX_VKsJTAVwi6wv1RFs1NcBYFVFzflsATgT3t87ovmoVvq3aGV5plrmiyuOwCgE0KIvlT5MQ7vgXjp0yjOT-q7EkR5jGOphrmq5nLCR1selLQDb7RsRHS-ds6iQvmTrRKKuEhXRbIMZnxz5dr9uRosJ_XMtvZUOuhWdhDFFvsUi0I8s4mwoRgUQGw_Z0t6z1nMmo-wXF8DEsxhjkeXn2uMM7MYYTr3taODhpgPieBR-ywwt6qsQukviqXpyNSErc767XclgNncwqH_FzMAZxZRNDWc-52Sk7Yuq_hNOdlN1FhSZKYLKBCrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
یک جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در آسمان خاورمیانه از یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت دریافت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69534" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69533">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjfXYc2aFoa5GTdVfNwR7ObAE46CHFE3E8NzVK_FV71P5r6B2PUKmDx1HyBbn5F_SIbiXm7Ps77yX7S1670shZg8dS5RRVoty6kYVsnxaVgVlWztsh7t7-pddX8EYZkTFp-7yDjoCavZ-wDOuxrY9WUt_9fweEpnzu_eHg4Ol3Wdn_9TmtMaPMSCt6Tok_n0xCgILrfJsfu5sjWacf09-utCWzRNswQTPAmVjuSUWyJK9HNbwY2H5_6vRHUIAixOFvKfYXezjUbSmRVrpLl7DPNfB7DhSrISobfiwxfZnj6ZK1XKxIH1MOTEl3LihVsIeLwFK0_81SscnjhJ-Xz6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ایران در حال بررسی امکان مشارکت کشورهای اروپایی در عملیات مین‌روبی در تنگه هرمز است؛ اقدامی که نشان‌دهنده احتمال تعدیل موضع پیشین این کشور بوده و می‌تواند به تلاش‌ها برای ازسرگیری کشتیرانی و پیشبرد مذاکرات با ایالات متحده کمک کند.
تهران پیش‌تر به‌طور علنی با هرگونه نقش‌آفرینی خارجی در مین‌روبی این آبراه راهبردی مخالفت کرده بود، اما در هفته‌های اخیر و در چارچوب گفتگوهای گسترده‌تر پیرامون عادی‌سازی تردد دریایی و کاهش تنش‌ها، انعطاف‌پذیری بیشتری از خود نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69533" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69532">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=ZY2IiGg26ug4sir1WcCm_JeJfmd9zO0Z4bUDBK4Y1mPTP6UXKwu8NepcBaBdF4S4Rh8Rk5e7S_W8NAbMrflKkz0qDT9uV1JPc-OKbHcFCaZODS7FEQmQNx7Ht68ES3uPrh2vefgahPRvS5tvpYTro4nAF2vZD2MBS1uhxZVR-4LxTIRWqkA_aVmsUeIsjVjsrQbyJGMj6U7P635HeBRX6wn8M16duRJwqb_ruHEH1qVgIv3BLt7rFuoROzZ7IZ94O7QBXCrOB4eSVqAZF1jQGXNXfUHtW8kDkpYVWnEV7NZUaaNHZxq2XGSQ1l1_3kVTa3C4Y1ewWpjweh76wvolrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=ZY2IiGg26ug4sir1WcCm_JeJfmd9zO0Z4bUDBK4Y1mPTP6UXKwu8NepcBaBdF4S4Rh8Rk5e7S_W8NAbMrflKkz0qDT9uV1JPc-OKbHcFCaZODS7FEQmQNx7Ht68ES3uPrh2vefgahPRvS5tvpYTro4nAF2vZD2MBS1uhxZVR-4LxTIRWqkA_aVmsUeIsjVjsrQbyJGMj6U7P635HeBRX6wn8M16duRJwqb_ruHEH1qVgIv3BLt7rFuoROzZ7IZ94O7QBXCrOB4eSVqAZF1jQGXNXfUHtW8kDkpYVWnEV7NZUaaNHZxq2XGSQ1l1_3kVTa3C4Y1ewWpjweh76wvolrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسن عباسی:
زیر جزایر و سواحل تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69532" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69531">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfGpF1JfB0fr8WX3X9CHH9RVKVabMb4uz2BrW2TlgaqEBQVyrHg3k7-ubr64CWG1rvdFMpZe7fdnT0tzm4j5yC8kWODtZUVeEr6UEVcBfOoLoCicTdLxRvhc7KkfbRxukqfnIZigAgB0Ypby4PXqJ2aXYhSkPzy10jYT_yl6xVJpvGB39zGwaRYFj4NHOgJwzGaqz4a3Tt9DjxLz--qjijfV1kCeKFjAcMSsdIFJLjGap7UTVGF2tbnGw_SjG5tbDduf8mkDMlzu0KjnfkAFwXe0OWSkFB915_qyV6_H8Xg7lLx8wya0i3D1kv6738Bs8tp6_znRTDWJ1cMrt3C6eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69531" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=G9Vr5L9z-FlvoMBulbWG9arRTYlzBrD0s2OqgrX8x-8a3wApdrR06dZbAfJho-dDuTH-4QGW8KS-NKaTNly-k3HeUYKoDfaNRZpoJDFZIwzIZNx6YprJDBOQba7TKDlE4atybL1RROfjZV6cDm6UIK2ONjug9yv-9NIpwIa_rxF06LLU099tEV2ahPKCBKGQ9_ZPioerif-MBLCCVHPLFmvQuwhh5t32ROZolU1tF1xjnMfofiacpPLtBi2mEZWDIaTxswgY9ckTm0y-psvWuUU4dVFdFMOYf2unP9JYqB4vkAMuK2oDOQUz_dnbxVxPSHgiMC1g-vtc-i5U-MyKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=G9Vr5L9z-FlvoMBulbWG9arRTYlzBrD0s2OqgrX8x-8a3wApdrR06dZbAfJho-dDuTH-4QGW8KS-NKaTNly-k3HeUYKoDfaNRZpoJDFZIwzIZNx6YprJDBOQba7TKDlE4atybL1RROfjZV6cDm6UIK2ONjug9yv-9NIpwIa_rxF06LLU099tEV2ahPKCBKGQ9_ZPioerif-MBLCCVHPLFmvQuwhh5t32ROZolU1tF1xjnMfofiacpPLtBi2mEZWDIaTxswgY9ckTm0y-psvWuUU4dVFdFMOYf2unP9JYqB4vkAMuK2oDOQUz_dnbxVxPSHgiMC1g-vtc-i5U-MyKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
غنی‌سازی اورانیوم چطور انجام میشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOpZpz9yUylj63XPoSv_du-T-h_yEzyctl4rWngRAUMhGZZysqeKo4YstryJOsgWzIKiI1s3UtDql0R_nJ8qya1hG3LdCweJxqzl4GvQdLNq4OvtqKJg6GgCvQLb5WatKzCC4A5qD4JPLrKQtlQyPgpthlx3MwerGYFzq0bf7Z2swXCtV-W0_We5ICPhFBM8d64GXBwcKiaqxazCe5F-oe-hZJVm5tINOk0_CsbSAAYpFquIWibsQZnoaHXDAvq_ZIquuFZjsCGoSs6SmnpUNQISHLQv_WVpuIQQdrJQjSi3SYgQ8gzp6NRZv3uE89nILIwcDgq-12x-T2tCc-xtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=OT4zhjbxqyJNWX1fNFNgtNoHLYyG8LmEwB6WH7fKVUyRZJuY7e7jWgnXzQjdioKFnmqRI72PLaNPvh50q6c-y4aU-pB8uQN7JsEzPs4GXSm_mbdhQL6pGo0qduaLoQavixBJFP1uHaFHKse5_5iqOiwBuNCKx75vogvn5wO3dGzut-IqQYlcqTCxucAt2dEBcnD-DwwfFYg6-tWh2a3S4ERiSJh6W4TJhlbdRpdnms_AynyllKdFaoRwIWNtq1s_6ucsKp2ruZ6_5CkhJ357t4nT4-3hMNTR-d5SiIkmAbAqadiaD8Wn4iE5QsNwibZMFWw_wK9u_-G2L8UoZrLHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=OT4zhjbxqyJNWX1fNFNgtNoHLYyG8LmEwB6WH7fKVUyRZJuY7e7jWgnXzQjdioKFnmqRI72PLaNPvh50q6c-y4aU-pB8uQN7JsEzPs4GXSm_mbdhQL6pGo0qduaLoQavixBJFP1uHaFHKse5_5iqOiwBuNCKx75vogvn5wO3dGzut-IqQYlcqTCxucAt2dEBcnD-DwwfFYg6-tWh2a3S4ERiSJh6W4TJhlbdRpdnms_AynyllKdFaoRwIWNtq1s_6ucsKp2ruZ6_5CkhJ357t4nT4-3hMNTR-d5SiIkmAbAqadiaD8Wn4iE5QsNwibZMFWw_wK9u_-G2L8UoZrLHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=T4flvaw_lbYtNQiKzYVQw_oxYfvv_hAPQtXypwCFGxTDEPy43FYy0FUrIuPqJjXxLr2a_wsn8NayMG8MWNPQxDum7CnqZcSe3SbYHEfF_imvG14LDq_gvWfwLUKdXo4TsBkwVUhscp7MbAI8fLNX_UbiB7CfSK0u4GT3e6K3EihBzh8rWesM-qeV8aehzOtq9QKFQWTFIE6qdEREr1huYSxKw8w3wOrw029w_Hd1qdCyMmigzmm6Wx3iAWSeKx1efCsdr7WnliocWJL0ebKl7POPHn9-0BGlBWSrmCFTVrbFyGjYBEmtxopKZsWclCKxhm8JX6R_kQhLlRlP0bNd3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=T4flvaw_lbYtNQiKzYVQw_oxYfvv_hAPQtXypwCFGxTDEPy43FYy0FUrIuPqJjXxLr2a_wsn8NayMG8MWNPQxDum7CnqZcSe3SbYHEfF_imvG14LDq_gvWfwLUKdXo4TsBkwVUhscp7MbAI8fLNX_UbiB7CfSK0u4GT3e6K3EihBzh8rWesM-qeV8aehzOtq9QKFQWTFIE6qdEREr1huYSxKw8w3wOrw029w_Hd1qdCyMmigzmm6Wx3iAWSeKx1efCsdr7WnliocWJL0ebKl7POPHn9-0BGlBWSrmCFTVrbFyGjYBEmtxopKZsWclCKxhm8JX6R_kQhLlRlP0bNd3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو پاکستان، یه تجمع ضد جنگ برگزار شده بود که وسطش یه گروه جنگی اومدن انتحاری زدن در رفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=ctSlnAtD_d5BYNb5qPTIScQ8K4N9pZxm-tSzhry1Ut6nF8ygp-sSA5hQK72tD3gurANNuQ7Spn46-12C8OshHSzZewx5vJZ_UfC0oWQlmGmTsnzOhzKGhOHfbYF2ybDgoz_gYrfQjNrVo8xcxKbFc9YG73hTM3b8LGoLk_oObISa5dw9H_spJWRfKtYckl35k_p3pN2oXki2ljOBj5BUkXkyaCc5hIOEVDMPUlSgxRVcy4wISQxgLitaugvtfdAlh0ea2Vwc7A3BewKiAeGIwa6a3BYElwD1WDyTl6Q1byYuxdcZULgQDfgZDMxYHsOqOp3geqW7sHAo5vBFVL36lpm9Y1V8NSLK-XwAWBQoeEs_wfylCcaHhBvCvkKL2LIDibRV9s3ZbYHuJabCb0jON0lY8i--w33DCOEVJdOVhL1G0aRA89FEygid09m1mVxGIhlfjsM08uxZy_slMp4GBFI0k8KxRt_pGZCXXMvZNLad2qarKf1zOHeZLaQi0B5wCxdCBLYr1kdFeRx5pCylOqNqjNfxEJ6hdZLflYLlxn96oS2YJvPCNRjppVcFpx-LAx5nEkY-rKbWpBGPioSUMQrndpJs4jWX3u7FB652hDUR3QwJRoKSaV7sMmmqQ3f6EgbpSgpvoRk4zhGEQp8oSz1b7on38IuXfFNRHSbGszs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=ctSlnAtD_d5BYNb5qPTIScQ8K4N9pZxm-tSzhry1Ut6nF8ygp-sSA5hQK72tD3gurANNuQ7Spn46-12C8OshHSzZewx5vJZ_UfC0oWQlmGmTsnzOhzKGhOHfbYF2ybDgoz_gYrfQjNrVo8xcxKbFc9YG73hTM3b8LGoLk_oObISa5dw9H_spJWRfKtYckl35k_p3pN2oXki2ljOBj5BUkXkyaCc5hIOEVDMPUlSgxRVcy4wISQxgLitaugvtfdAlh0ea2Vwc7A3BewKiAeGIwa6a3BYElwD1WDyTl6Q1byYuxdcZULgQDfgZDMxYHsOqOp3geqW7sHAo5vBFVL36lpm9Y1V8NSLK-XwAWBQoeEs_wfylCcaHhBvCvkKL2LIDibRV9s3ZbYHuJabCb0jON0lY8i--w33DCOEVJdOVhL1G0aRA89FEygid09m1mVxGIhlfjsM08uxZy_slMp4GBFI0k8KxRt_pGZCXXMvZNLad2qarKf1zOHeZLaQi0B5wCxdCBLYr1kdFeRx5pCylOqNqjNfxEJ6hdZLflYLlxn96oS2YJvPCNRjppVcFpx-LAx5nEkY-rKbWpBGPioSUMQrndpJs4jWX3u7FB652hDUR3QwJRoKSaV7sMmmqQ3f6EgbpSgpvoRk4zhGEQp8oSz1b7on38IuXfFNRHSbGszs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=apFBff4hlRm6LaXHZlcsaDr5O26Va42WdGu9IewLK5u8NLe3BTS89F6cZQuT-eT37rhUvEQMZTrKrGEvfOiHBDuA_7ahnaFsRXANoB610OhCTxm3bsLAhogL_JFYg1bOiPgkTMY9xfpp6AdsEELi6YELPU72DncqYw9xDcYm66rm3Mz-mfC6m1VKpH6oVwyAE67nuJ7RrxSO9N0-QkGe3_83eIwUFoya0YtNr3PYWdaGvgamYf9Kz6qXE7fF91bGP4NHHhWfY4nb9L9byYvrug-XwUHQroWSKum6KLVOqWuMbg55W6D36SYqBJzXfwZFvn9hwiyh02z7F2tqTYCxIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=apFBff4hlRm6LaXHZlcsaDr5O26Va42WdGu9IewLK5u8NLe3BTS89F6cZQuT-eT37rhUvEQMZTrKrGEvfOiHBDuA_7ahnaFsRXANoB610OhCTxm3bsLAhogL_JFYg1bOiPgkTMY9xfpp6AdsEELi6YELPU72DncqYw9xDcYm66rm3Mz-mfC6m1VKpH6oVwyAE67nuJ7RrxSO9N0-QkGe3_83eIwUFoya0YtNr3PYWdaGvgamYf9Kz6qXE7fF91bGP4NHHhWfY4nb9L9byYvrug-XwUHQroWSKum6KLVOqWuMbg55W6D36SYqBJzXfwZFvn9hwiyh02z7F2tqTYCxIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=eBavtZ-mBHN_26pL4jtFq8SwTUt4iW4Be5K1tkO-fkM9Kyrk23jitmsFpKga5PJ19waKmGSUntHQNEdNtQoIvX-5ekIp91Fib7toLNbgWziEnL7MyZXct58ZKxV4b7YegvKQwNdccAoIKe4DW_nAvPBwHtNhCYel8l0b4O3uBoGWQEG-sFTnH6TDQ2PUlS5NquQ-tvx8Y9TRSfi5o03DE6VU0wQfKJItbpfn80rD8f_vzZUHINZtqzu_gO2LOF8PU5W643TUoERD2z_ZeFnut7iN-zBnvR_WkSmrfpTWcpOTOdAVZo0mR4W9d2fcjrhLrd7s2U6DeOMwR_SsfwdfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=eBavtZ-mBHN_26pL4jtFq8SwTUt4iW4Be5K1tkO-fkM9Kyrk23jitmsFpKga5PJ19waKmGSUntHQNEdNtQoIvX-5ekIp91Fib7toLNbgWziEnL7MyZXct58ZKxV4b7YegvKQwNdccAoIKe4DW_nAvPBwHtNhCYel8l0b4O3uBoGWQEG-sFTnH6TDQ2PUlS5NquQ-tvx8Y9TRSfi5o03DE6VU0wQfKJItbpfn80rD8f_vzZUHINZtqzu_gO2LOF8PU5W643TUoERD2z_ZeFnut7iN-zBnvR_WkSmrfpTWcpOTOdAVZo0mR4W9d2fcjrhLrd7s2U6DeOMwR_SsfwdfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXMkwvwuoXnsmVJNtX12EZdOXjrTkUraWa7yqCMiLVlKpYksZbf1nDiSkWsSeHuqK0GnJQ1WLUtRoRyZf3G9DlY_xtfj2ib2xSlmB8g4DtAJYTyFUwG3vbYcKoaBvWF4B4f7-p7CZRK0ggT64KF6-PTlZvKStyEWn2Sex7C5WfzK5bIC6_MI493bHM3SOQzWzZr2cAjoDnscY1iY5LUe1GtHxd6pl7sTVximOB2N61u8BPD4pNbhBJHiKL5pDJb5jSzpmE35uEcWk8kR2DqDwxTyS06OFjh9ybN_rNAk8y90NJz7zaESyCRqwHGITO_CfVScHHuX_1G4rAuLDOvf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n102PQDjXdB4hrvgcjdjmEMZP8ZaxFTr-e4P4AAwbDmq4qhZqV-x3Ba7-I26FcuqUaF-ruMvR91rchDI6IMKbdd9BNm7DUTIMc1oHH8UKIJbbkaO5QYaJHpBGTluGC3P_WJRD_vuoZmM-Zn4_JbBfVfo_00UYU0eCdkE72OSTXikwFUoCZf3868fCm6LdEvWcuU1myq22fScEuWVFu3-dcvCbQ6iksQifLaEzoMe7vawHbjwHz9uyDSnoiTNPrcKAkqhgsJIaTK39M4Tn-7JUyMd7oo3sDO9pHzNJmVt11bt50KJOO180vRDDN4COZQIEwa5Nd_AygynRBQq8hQt0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=fE8INQvoXQIRkTuHa70kyi7qZmnGaSEK-SVCzwkHtkvBZugQQsX_7ln7aB7bE-1agG9mcVVY8o_rB3wKxFnlkKSqzw_M7DRU_xUegwGXibVVgMFQDnzNPDqEKhhv_O9piXtnmjI2NrPhQTEbUXUv6STI41cBnsdjcqcMVOkwWom96vIA2qXEICCrZutse0yirGuRogGIjgXQ2R23PJxuo8PKBkTWF0aW491rl-JfRhUM3XSA8DtS0BIzYAL85SbWp15JSo2o6jt_E0MoN8-hf46p0S4DFW7v_iSncOVN3_wiYtquPJW3wUAED4KWj20nXxVUBwid9FsjvoDiLDxgeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=fE8INQvoXQIRkTuHa70kyi7qZmnGaSEK-SVCzwkHtkvBZugQQsX_7ln7aB7bE-1agG9mcVVY8o_rB3wKxFnlkKSqzw_M7DRU_xUegwGXibVVgMFQDnzNPDqEKhhv_O9piXtnmjI2NrPhQTEbUXUv6STI41cBnsdjcqcMVOkwWom96vIA2qXEICCrZutse0yirGuRogGIjgXQ2R23PJxuo8PKBkTWF0aW491rl-JfRhUM3XSA8DtS0BIzYAL85SbWp15JSo2o6jt_E0MoN8-hf46p0S4DFW7v_iSncOVN3_wiYtquPJW3wUAED4KWj20nXxVUBwid9FsjvoDiLDxgeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNDfRnuJceMxMrC1bfREWWU8sxH3nmf7bp0Tcx3TTux3tALSNI6wsjzNVVat8o67jUCyaLKP7PRsZjXXxTEqcP0utq9sYJVXsZmZxog3WSWt_XpKBiNOx0l0-bX9yVAjDoyrwfruD6xxw9OhVjPPZ44EJKQBdLV8R0bmF8Y91EpZb3mO0dpGzCIeLxnhqjeHhje9kpUwMfflLOyOL4puoWL3x-99xTIUv_mFSRU5_xN4uhc3RH3Te_BUOnV1hopkPZT0xQ6bLnR7YZRdDHiRR-mL6uBmsinNznM_RcIdleER0Zpeef17XCKbN9hSK1N04d_W0hLkEeQiWYNpr5edzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9fI_6mTXfvxyflrFV8_bMAOcmPUfx_QaWIgzPJuV7qE2NhwPe3BQD6XkbFGlvay3qjDOWAjTyHxaQp6AZvFyyndL1d3q5R6BpgqjJwTp2KJe9hFT9h_kLSdscvKBt6ZgT7WG2T8AvIhAQp5YT2P-Oi5-FI3DTPmsL9GcXYuC7vCiHIEXLd5iCsdKaCvmubwpXpYJ6h80-UugEnpBD9jo--f_mBxyLHEKxrDSTiihs65PHF44omlQFBkDGbADjPjnYHKqfxCafm-72FFKj7keNvmYdAKmf_ZL_uXQty7iyOZZWoD-a_D70L2_qRXmyhgHX7HBmyPj4rRp4rHtgPhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdGxMecJqY_f1inlMAe4ixCe0XbmMnoASFWHEuQALnBzVd-9LIjqcbU1pUW-7hyqVlkPwPKMIWEG0gyN3CYOyPmGBk8BzxA-UEjjxRHCKC9yS5MgnWo7SOnUG4oc6E_rT56A-QdLvjXg6gX5_Z7MtSSo70pOwa8v2o-qxZYe4eiRBOfQYF6hEFEhh3aFgITBFIe-vOoDIVOmE496h_q7f3XbBVY0__LNInJTx2HnTVA41p135fpWRAo7flnwkxwNrIuMPsfQY2jTuEjx31zEF4U3Uj9tyct8IOXVDAQipjuhaiVrd0hCt0A4mGSMMEfRDKXweqaES9MrT3PqHUPa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovaRBLelIZFUM3Upp1HCmm0mGUFCDJ1W9pP6hXvVlOGRSlRftseTgScg6FExmj6Tfvrr_6mFRPRgvqoQDKxDjr89DUPdiYD1RUURXS7n8y4jjvxmMLMzGj15Z1vzyZjkT9kk4q2ZGT5xvv474T9MbGpqpQ3F7dLwyLSISS3vOjYHb-YKtuL0IrgRvaDfKokgW3uA0JGSLZTZ0WvciF183NWbN48hstjBS19ebNHBSYS3fhPAkipfrSqR3C6DMHBOYrmwJv8J99STCi4MhNxEVX-3AY9ltG_NYfBZpH00BGdr9stSnPpAiEQ8xxZfl9riI1YvWzwqYSvnScx_AhcMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9m-ZaeWCci8Ja77Hm-63njECVLZTh3NSpOOQ_Ii0n9Zc_t17nzkN6AW7CJzhYJf0rG5fu-pxKooSHFuHiaradMQF90rrbWo_1qzBzeSEr4igS5IgkskV1fbG1Z6IIrkOrcqiUZWVKzgf54oIhWkBq84k2wO1LOgKmTrrynKr8PW9JuU1D68P11M1PhybVrJEclbD-tTACWVSKkOJj3agylX9nxV93WwolzHyhyBWGfB77R3y_7IQsm7EUKEP1IqGfy9bet3CxnDEm2vvbpKq9t3GyGgCY5UMdCzqFx-aX3AvQpfK8Vcl0R1r04cYjFBWOTDBrdgp_EeWX9tw_47yQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=cjDBrKqVz9-CvYKLJIRyF-qd0wRkoI734dF0xXryoJTRtDVVFj4JtTtZ3s4c8aHeIraSQeJ9PfRBMpKvKiDoMuugyLpzfjZGpFV6KRWaAJOPVf5Y73KJcOYUMfT9pm3kEO2P6oZafpzizkVKnp7wQBGVNsl95-N09PzWoaiZSEEFbLB1OK0eaib-LhYU5BmA9cQ8NqEXSJ1KuPlCaQo5qCpaIByxomgMpICW8g1DuQClnPchcgxs_8mczozAMbDYR8cyttpy7BtTYcsGjPXfDvMGxwKI6QhVBmdspxgdhZhvCh7rEklQGUjd5-xUhBaFK7YYj-TOIxT10gTonm6GGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=cjDBrKqVz9-CvYKLJIRyF-qd0wRkoI734dF0xXryoJTRtDVVFj4JtTtZ3s4c8aHeIraSQeJ9PfRBMpKvKiDoMuugyLpzfjZGpFV6KRWaAJOPVf5Y73KJcOYUMfT9pm3kEO2P6oZafpzizkVKnp7wQBGVNsl95-N09PzWoaiZSEEFbLB1OK0eaib-LhYU5BmA9cQ8NqEXSJ1KuPlCaQo5qCpaIByxomgMpICW8g1DuQClnPchcgxs_8mczozAMbDYR8cyttpy7BtTYcsGjPXfDvMGxwKI6QhVBmdspxgdhZhvCh7rEklQGUjd5-xUhBaFK7YYj-TOIxT10gTonm6GGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=hkYEohTxEWhP9OWFRfVG_3wjvF-jaqp2wMYPRdnxDWwYP_RWcKqQ2wjsUUAG5KuPbGz5lTxU_ovAVhYiiNQntwY_uC7_pJdX6bh0IlphDvDGgbIH5W_LZCXtwW8IF4_tGDO-FeUU5sHkF98Wu2kPpDtdTxFkHTnua8h7yuFKcPf3MgEBFlCoLOgowGf2_XQVblGFbi1wfRa-NTGCaz1CGrDNQJpTf_DUMiA0al9KAGllC9ywrhg5KOdi7zO9oDSSm6qRo0zI4pJyRG_IgZ5AcaZNwq64jWip5__IX5pN_jk5mx-Ki-gx5ihUGuwWPfaXKIn7xFUoChY24wXrE4slDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=hkYEohTxEWhP9OWFRfVG_3wjvF-jaqp2wMYPRdnxDWwYP_RWcKqQ2wjsUUAG5KuPbGz5lTxU_ovAVhYiiNQntwY_uC7_pJdX6bh0IlphDvDGgbIH5W_LZCXtwW8IF4_tGDO-FeUU5sHkF98Wu2kPpDtdTxFkHTnua8h7yuFKcPf3MgEBFlCoLOgowGf2_XQVblGFbi1wfRa-NTGCaz1CGrDNQJpTf_DUMiA0al9KAGllC9ywrhg5KOdi7zO9oDSSm6qRo0zI4pJyRG_IgZ5AcaZNwq64jWip5__IX5pN_jk5mx-Ki-gx5ihUGuwWPfaXKIn7xFUoChY24wXrE4slDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=cfmjeH6cY2a3wLS55gSuhtysSKP_GUUO8IQKAD76zloKEmj5PfFRjZUE4hnpMlkrVsO5woa9hZ6elDbE2ZHPDmeYh51n8XH5ZDm0VeIolqKqRUueDf4BKDosDGd9ai-lLUhafgCgO_2r-4myuOqCmAD95a3ikoAjIdQOeKKG19FtglNeMmHEEZ67wFzEelLJw_oS47ncinmOgPKt1QocjcouSeChxInwmweocI6ZwAyq40R4YGW0AG6-2s6dL5LcfkM4GPNsQ0pPcUcJ7n3GfULUFpCfInxAb901VPhBbegdQd_sRAmFvU7FPNeo_f2feNMFEB21eahzI4kJjNqPcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=cfmjeH6cY2a3wLS55gSuhtysSKP_GUUO8IQKAD76zloKEmj5PfFRjZUE4hnpMlkrVsO5woa9hZ6elDbE2ZHPDmeYh51n8XH5ZDm0VeIolqKqRUueDf4BKDosDGd9ai-lLUhafgCgO_2r-4myuOqCmAD95a3ikoAjIdQOeKKG19FtglNeMmHEEZ67wFzEelLJw_oS47ncinmOgPKt1QocjcouSeChxInwmweocI6ZwAyq40R4YGW0AG6-2s6dL5LcfkM4GPNsQ0pPcUcJ7n3GfULUFpCfInxAb901VPhBbegdQd_sRAmFvU7FPNeo_f2feNMFEB21eahzI4kJjNqPcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu3w2kNCKDIxQOr8qn__iyo4LST_CdhDhYr7RcrTQNGk94q8ZHKuiSL5M7xQfHaTToAHMyrQPYGvybmseMgNKdDRHFndLnUtMtItmyL9OfzMPSz2L-DyaM3gK_W2Dmv8if3o8gWcai2JIRSJihpHLnqFvc8m5ilVwd6Pw9EICwHEgLNRu1Xomf_wpi1dOrPLvYc3ILorYPzYlP82EGQojNTtBnxpKampCnk6cAbX3jouVCrN7xMU6V3dZZHqRw52bSHGA3RkZdCj2qYGOniv355S75yC8oQSc7H1IK9CEluu4Ptj17j1jmvxKGcj6nZJ6oR31vFvW10irshKXeBgtWPs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu3w2kNCKDIxQOr8qn__iyo4LST_CdhDhYr7RcrTQNGk94q8ZHKuiSL5M7xQfHaTToAHMyrQPYGvybmseMgNKdDRHFndLnUtMtItmyL9OfzMPSz2L-DyaM3gK_W2Dmv8if3o8gWcai2JIRSJihpHLnqFvc8m5ilVwd6Pw9EICwHEgLNRu1Xomf_wpi1dOrPLvYc3ILorYPzYlP82EGQojNTtBnxpKampCnk6cAbX3jouVCrN7xMU6V3dZZHqRw52bSHGA3RkZdCj2qYGOniv355S75yC8oQSc7H1IK9CEluu4Ptj17j1jmvxKGcj6nZJ6oR31vFvW10irshKXeBgtWPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=DVA93ug-HT4Mj4CS2SNt7BQmNdUyIaU4xuTkBrqDCtKCRhE8s-bwI56Ya91G60culyjv0Jh0nWLtghidYjFApMDXRRtIZlenmFo_TFl-VUE7It83pMT0BA-sR_mIhk_QE5cxST-ACQnKYA4-BMjnBogp5b-5HKoXBs_n6CILC6V2Dnq2ASmiOdI15ImzfHkDSUqr-P7mJxc8yThj8qEP5ryy8DACnrzFf4NHo6AuuQDCAi-CXVMs1mIB8paM479-PcgsoeFTVopWALzQ_SoFJr0Fiogu_nV_Anyh_ChCUav9f8Ll22F07gKBwg96GR6r4IK6Ujg10A_k5VfpZ3byo5AikHZOrVmG3T9i5QCr3RmU5n862AdMVH0NZ6Vgv7Yjcc8Fe4w7HdelPosDd84iSx4pErSAa8kQ9EWl2lfQws6KMAAYPseuht0u7gwY3ekuFDNaPjTEDTRiO1bM6AJdpqSxAtW3AVxzQbMyh6eZZ9B8NAI7GQTNp8OJ9jf4HOf7Au8D-JJ--CjCE-WWPA1nb5gNFISFz5mWhRwmoL9n7E74WFS5o0ypzMTqfL243lJdFEfT83jMOhIQKrSgfs3RcvaC-EO9dptrajp4NYeKmxWtNG4pX4a4urhJHkkuK-ihLq9YzhJVchtKoA4pAF4oHT6BNuOLxW4G8LHwkwvNv_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=DVA93ug-HT4Mj4CS2SNt7BQmNdUyIaU4xuTkBrqDCtKCRhE8s-bwI56Ya91G60culyjv0Jh0nWLtghidYjFApMDXRRtIZlenmFo_TFl-VUE7It83pMT0BA-sR_mIhk_QE5cxST-ACQnKYA4-BMjnBogp5b-5HKoXBs_n6CILC6V2Dnq2ASmiOdI15ImzfHkDSUqr-P7mJxc8yThj8qEP5ryy8DACnrzFf4NHo6AuuQDCAi-CXVMs1mIB8paM479-PcgsoeFTVopWALzQ_SoFJr0Fiogu_nV_Anyh_ChCUav9f8Ll22F07gKBwg96GR6r4IK6Ujg10A_k5VfpZ3byo5AikHZOrVmG3T9i5QCr3RmU5n862AdMVH0NZ6Vgv7Yjcc8Fe4w7HdelPosDd84iSx4pErSAa8kQ9EWl2lfQws6KMAAYPseuht0u7gwY3ekuFDNaPjTEDTRiO1bM6AJdpqSxAtW3AVxzQbMyh6eZZ9B8NAI7GQTNp8OJ9jf4HOf7Au8D-JJ--CjCE-WWPA1nb5gNFISFz5mWhRwmoL9n7E74WFS5o0ypzMTqfL243lJdFEfT83jMOhIQKrSgfs3RcvaC-EO9dptrajp4NYeKmxWtNG4pX4a4urhJHkkuK-ihLq9YzhJVchtKoA4pAF4oHT6BNuOLxW4G8LHwkwvNv_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=vDeLZ6MfTFVXwt83dhOWu4efPVYamHCQvejHqo34KcHrdtQPx4TIiuHDGB93y5SFmfMzfyjeej7imjNQGrQdrGSvGGDXvuG8u_wtHWLDPE1EvuyXZiaLSnNw7nGZ-VO7fTjymcz-YD6tOzDK9dJCUoBg765pZtsJhFmu_5yB76pZyoHdghgtQhopmpJJ076IyvNAC5TyGIWbTUhU3UqlzJkZ2Bf6hnFkjXuqoefbiOk_qPaDTlZk5Gbt7D0LvS2GeI-PviVD7tuzM8lkkZN38r4thUBum3BPEPoa7P-NjbBjYgUrL164_gJJjfBjQPVH3WjtRh1yEuPvf4KCiJsWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=vDeLZ6MfTFVXwt83dhOWu4efPVYamHCQvejHqo34KcHrdtQPx4TIiuHDGB93y5SFmfMzfyjeej7imjNQGrQdrGSvGGDXvuG8u_wtHWLDPE1EvuyXZiaLSnNw7nGZ-VO7fTjymcz-YD6tOzDK9dJCUoBg765pZtsJhFmu_5yB76pZyoHdghgtQhopmpJJ076IyvNAC5TyGIWbTUhU3UqlzJkZ2Bf6hnFkjXuqoefbiOk_qPaDTlZk5Gbt7D0LvS2GeI-PviVD7tuzM8lkkZN38r4thUBum3BPEPoa7P-NjbBjYgUrL164_gJJjfBjQPVH3WjtRh1yEuPvf4KCiJsWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69503">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyUPU7NvGprtLSzakCAe5Xqzew-T0Vz2RvMVbNtIX36_lTpENibf1lzH-kYD2C56egmcleRotmfiPl6zIUPBed9VEA3-TXMC6Qt1d1AFDMvGx1xDqepnM3wbsGpjd2ODaMWmUd4gPCTjcqwQl1vE_LQJLb959YdBL8r-e-MejZUpu43QAUAEn6HxalSBietdzrpM-88U21LWvpXw5Q8aw51lb3BkRYf2ojwMTlHKqds-8IV-9kGf9ZiZISDuLRF_HgM-Ai17rJSpWyZ0bznHVcpvD3P_qRa5zwp06j34MCVK0TRAAE6LXY5cZ2T9-mr1tORjlzCBfLsswsXtZpQYPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک کشتی باری در فاصله ۲۰ مایل دریایی شمال شرقی «الخصب» عمان، از طریق کانال ۱۶ VHF پیام اضطراری مخابره کرده و مدعی شده است که مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69503" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69502">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های حکومت از حمله به یک پایگاه آمریکایی در شمال کویت خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69502" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69501">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=YCwRUZUAhm_bM48wl3jNdf6mCG-xyn4P64i1u3s1dpw9gsbC46-XtmvfozOo22w9SfGWBfPmUshwUR5oXbYDmhDlksFHUWIoM_reCUVuPoZtHqR2T0Z7-SdDCmJ_gzBYOzUe-m1fLep7uhLxciD0-rmkxMTxyOf4V-A4TX7_cvDHDsd8ESQTM-bpUxpvgSpj_T8M8FVL6z4ThLxbB2IlmEotj4t0vKITbj9THuzYMNEjC_o7FpIb5NIsVHvRX7vtkoZOWwla9jojjRDO1STdIBPq-BW6IXb8WqEdUFW6Un_uQ3ytahWhmhqgva4pvCm-LPyUxAAlm8ADBWgOa6oY_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=YCwRUZUAhm_bM48wl3jNdf6mCG-xyn4P64i1u3s1dpw9gsbC46-XtmvfozOo22w9SfGWBfPmUshwUR5oXbYDmhDlksFHUWIoM_reCUVuPoZtHqR2T0Z7-SdDCmJ_gzBYOzUe-m1fLep7uhLxciD0-rmkxMTxyOf4V-A4TX7_cvDHDsd8ESQTM-bpUxpvgSpj_T8M8FVL6z4ThLxbB2IlmEotj4t0vKITbj9THuzYMNEjC_o7FpIb5NIsVHvRX7vtkoZOWwla9jojjRDO1STdIBPq-BW6IXb8WqEdUFW6Un_uQ3ytahWhmhqgva4pvCm-LPyUxAAlm8ADBWgOa6oY_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69501" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69500">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
منابع عربی:
شنیده شدن صدای انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69500" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69496">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjNuX4BrHH0HLcnn-lsSKTSgqQSJlFO_von9MZiPk7Szrh_e1NT2NTYAGTz1ievufHwnhRfB7Y9K20jPOpJ1HNsOZk4zfUGLrNUzN9EQsJbmawbo_nXkXbR8qz7iVUheR2TVMhsZzKsPHLC6zUwxBUvdVGqFsXCCuf-ZczAUUMcyZzmByVLjAdzDkXXm1g8P4i7j72WpbGSI5t1seW-bnm9jOSt0puVwQ0u8JZpepK0_3lM0_nT-djGOFdUOkV026O3bMb7K4v4Uxz-0MfgoQ9awXK9aU6jfhz0_A1rFXLL3SqQsepH8-nAlP9TOGNSwKwBMPqfQ-WQfXr9UPzOsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=LkhoQjjUdHg092HljJxWH5sk-aG4E0tJ8Jsq4u_ELl2G_1vE5mBIdHSjEc8NSstd4Tq2YfcG2Njm-bnPBYKXDfl4YzO9IfRoH8rc1HwZvsAnDTSuwFcIu-s0cbGNaUogvWshuxW7xB7zYZY16VhVcOMehZEz5iT1Wi7VVpThRn8TfS3-WWlO-aL0Njn-uiO_cyT_i9vi5lEpg3Md3sZvnB5K-wozB1bD0PDbaqNzKoqeoI9XFdr8QbbVqajylYDRb5Rzros5XLIVQjpde8cO91Zg9MoUorvar5swyGwZQZQq4nCHjEYFmJYXzX2Id5ZwIpFvfqrLdUZstpFjeIrhcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=LkhoQjjUdHg092HljJxWH5sk-aG4E0tJ8Jsq4u_ELl2G_1vE5mBIdHSjEc8NSstd4Tq2YfcG2Njm-bnPBYKXDfl4YzO9IfRoH8rc1HwZvsAnDTSuwFcIu-s0cbGNaUogvWshuxW7xB7zYZY16VhVcOMehZEz5iT1Wi7VVpThRn8TfS3-WWlO-aL0Njn-uiO_cyT_i9vi5lEpg3Md3sZvnB5K-wozB1bD0PDbaqNzKoqeoI9XFdr8QbbVqajylYDRb5Rzros5XLIVQjpde8cO91Zg9MoUorvar5swyGwZQZQq4nCHjEYFmJYXzX2Id5ZwIpFvfqrLdUZstpFjeIrhcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقای سیاه‌پوستی که تو تصویر می‌بینید، رکورد ویوهای تیک‌تاک رو جابه‌جا کرده
👀
حالا کارش چیه؟ میره به شهرها و کشورهای مختلف و دخترها، زن‌ها و دوست‌دخترهای مردم رو بلند می‌کنه و باهاشون مثل دمبل وزنه می‌زنه!
جالب‌تر اینکه تو بعضی جاها، دخترا حتی صف می‌کشن تا نوبتشون بشه که ایشون بلندشون کنه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/69496" target="_blank">📅 01:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69495">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b93335655.mp4?token=gss4qwl-C9C0hfosWthcQvLrfspsHXH_mE4aBM622TibPRu3rWqGPocqHycI9W9MTvOR7nAVWzLVSoMLZ11oyV_NP4AgcRliXV4OfKHVoJ8FRRKDM3tnw3ZvZ6l8znPpg_U1jTLabx3ICvHvipBiuRS2odDpf-yRdUNpa7CNihISvqEmvIGMenX_zehRirRrD6ZAzbVotkCnRvLFMp1qmVpGni_Tmd_uUdLqAUnC6vxzyt2lpUlpoFV6pa5nb6hINKN5aq5o0g4loF685IPONSx6_AEDrJBWV3P1MkJmzQqmWoGkHpgN8_Hljg6l27dAM5US5G52ow7qZSJexEBmVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b93335655.mp4?token=gss4qwl-C9C0hfosWthcQvLrfspsHXH_mE4aBM622TibPRu3rWqGPocqHycI9W9MTvOR7nAVWzLVSoMLZ11oyV_NP4AgcRliXV4OfKHVoJ8FRRKDM3tnw3ZvZ6l8znPpg_U1jTLabx3ICvHvipBiuRS2odDpf-yRdUNpa7CNihISvqEmvIGMenX_zehRirRrD6ZAzbVotkCnRvLFMp1qmVpGni_Tmd_uUdLqAUnC6vxzyt2lpUlpoFV6pa5nb6hINKN5aq5o0g4loF685IPONSx6_AEDrJBWV3P1MkJmzQqmWoGkHpgN8_Hljg6l27dAM5US5G52ow7qZSJexEBmVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دست فرمون پشم ریزون اوپراتور اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69495" target="_blank">📅 00:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69494">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmbtiPjTFmX6o_D4Q4uR1QnUtxP7_ia1V8f-fmaojp8myJXamUhiJtHDAaZ5QiZqK60E7iiYcImYFmtKV7XWKlNCCoWfR2bwDFLuFPs9xwZJSsDbTnxPko1JlL8l_E0RWraDyLvmSw38w3o227JLkv83thGkHPhZqCydmhH1dNcamueoF6AOCz4DQ4UZD8CUYJ0nGuAkgxgqM6Muq2tGqUDmmDQzKTthkOrJvV7a_Dn54ykzeIoSq94XuqSpiUMWY4wmo3NG1a4zGjWcRVJuBhwMsZszN7IXU7LVSOXetfJAJhNUm8sL5EfFQo3vAEHdKctZTvWiNpMNkWOGvqEgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
ایران هیچ‌گونه قصدی برای مذاکره با رژیم ترامپ ندارد. هرگونه اقدام تجاوزکارانه با پاسخی کوبنده و قاطع از سوی جمهوری اسلامی مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69494" target="_blank">📅 00:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69493">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=LB_g6HLYw8kbcxuuAQ9Ft3XgKvJ1NI8kh82XaZ0eOHsOcWh83H8gs_kInPvpEWLFQqYisUMvh4m16sOeJTplfS13XfAfk6T-VO4H5ZI_NcFpkwRLOFLmyiMNqnBB-P6-SqcOb13k5RcVwUgY7_WQy0PjZ2p74Hbr16OomufAIRC3jWzUuyUvFbFD32cOgriI6Eg17TjkbazEBvlQzX7VgM4rLzJO157frpnmcDzNDamuw8kjXYPyGLMN128T3Z4L3yHQwBIYxOaMCidRrGec1L2MBIysPKpUorYlpbZN_My81ZfNycbtvr6-sk88CJxgfwWi2NsgZlnpgNIM9QOAsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=LB_g6HLYw8kbcxuuAQ9Ft3XgKvJ1NI8kh82XaZ0eOHsOcWh83H8gs_kInPvpEWLFQqYisUMvh4m16sOeJTplfS13XfAfk6T-VO4H5ZI_NcFpkwRLOFLmyiMNqnBB-P6-SqcOb13k5RcVwUgY7_WQy0PjZ2p74Hbr16OomufAIRC3jWzUuyUvFbFD32cOgriI6Eg17TjkbazEBvlQzX7VgM4rLzJO157frpnmcDzNDamuw8kjXYPyGLMN128T3Z4L3yHQwBIYxOaMCidRrGec1L2MBIysPKpUorYlpbZN_My81ZfNycbtvr6-sk88CJxgfwWi2NsgZlnpgNIM9QOAsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69493" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69492">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571743cf02.mp4?token=DhPZPeWwMF7TJsumBkZ9UXTbVNv4KygK8ywf_SqcwfsPaYHOZ2_XXALZiNQmzg9o-zlwmqjjrYvu9O6dG_UVNYJme-f2pEQUkMsGBV02FINFF5B7TZYukrh0k4rpPpbS5XW8oEscMzXGFvqGHEgmu6aMnh9seUOIsueSVn2W1aF11_t179OpSMglqJpxK2whHJ5FV8Dx_9qmsDLGDV9pcQ4tvFEDAmq8eOEik8Flp3PcmF7lj-k8Q658hRaZfVOV9WsJjaQFRXNTaqdrmD4sU9xAM8ynRDMuXC0F3hDI5wWobk_v3FS-YMbHR235U46vsNCvQfkwV5RE5vLGyMY5Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571743cf02.mp4?token=DhPZPeWwMF7TJsumBkZ9UXTbVNv4KygK8ywf_SqcwfsPaYHOZ2_XXALZiNQmzg9o-zlwmqjjrYvu9O6dG_UVNYJme-f2pEQUkMsGBV02FINFF5B7TZYukrh0k4rpPpbS5XW8oEscMzXGFvqGHEgmu6aMnh9seUOIsueSVn2W1aF11_t179OpSMglqJpxK2whHJ5FV8Dx_9qmsDLGDV9pcQ4tvFEDAmq8eOEik8Flp3PcmF7lj-k8Q658hRaZfVOV9WsJjaQFRXNTaqdrmD4sU9xAM8ynRDMuXC0F3hDI5wWobk_v3FS-YMbHR235U46vsNCvQfkwV5RE5vLGyMY5Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی وایرال شده از موکب خدمه ام‌البنین که به زائرا آیفون ۱۷ و آیپد و گوشواره طلا میدن!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69492" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69491">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvnrhByqJUtY0pEypjCoor-6JQOviwMfxXEPLI8Ozx5U8xwBajD4dda2e1k9KgrGUAC-zWl1aaoKs4WHDwlakthFFobMSeTDY1MVSecF0xy8pDFh2gNp96q9nAffN7U2nNih8HDdRPCAD4GiUSpPxuDoHhEZojOjSlzqCkWLiLXP7iqHD-_oDL_-CxaJ9238YzI9B0iWd-w2aYXfhlbBybnDNJms4f3OLCiAufTCEOdyda1ulMKZA6JRXAdLyh1QusirUoL9aDfoJvG2jCnr6Vau6UjCF1P5RYBoWsrzNlf1FcmUD3Xkhv3K-kqr980ZIYVHYc0V4P4HrOOKglRdcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69491" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69488">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WN43NXbZdBXrSpUm7cG9kW303rRDwXLwU5FQO4dLxnPrEKQvfu4Grbwz0Vt27iph2QGnc6wykrxjwABsVFXcfQfawD2exyA0JiUOGAXvFEXYUHrm_pt-zXMyW6qJtybfAyb1YTuMR5YM7KcV9tvq2DHY0RUv5-xT3j8hK8-wjQU8ACQPc_55-TqSldq6AsUexY5AH-1axtSfqnGAglQHyLtdCOsZcqY4gvk7Yr2Wz8q9bLFCgjqj_UmV7im4hE4-k_4oQN-KKtPwGiBjysjn_cYIImL9svL-OmC7Vgx4fudogEn_9gfuzfZNQ7VujZ6D1xlX1GCeamSFcFVDlLEoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjS-ypXC_DqhX6P32f2m6PtQz9PvofKQEVxQvX2yC-VQeIEKNrnAn5QD5U5cg7vvWu3kDMDv7fIMyC2qaNGePNuXvM3RVWLAC5TtqAg3cQ01jXHy-jfSRlI-jzbCb6G8WCY1IUqiUzdqgkcrKLht0wxbIk0KQOkgj42dFo6wngGzglmPVBhFzNpdFB6e9nSiBB9i_CbWAkf0NInxApQCTpw_YQVuNx-vFaU5X8v7QmMn9RjbNHPfKEuwDfj_RxdFmoISg1X4JlYyjIem5r4yU1jrvt3cXJk7RhfOJHQIz8NChhnR1cBbyq8jJMQaZoqs2AvCnXckpT1rt-en64_2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjK4TXjY7R_7N2kL5MldrppEQUyqDMxu23WbBSxVkbaLLBGKZrzHFZTBrSJ5K7pU1WyADLV3GGiWW3J8abcADhbVsUlDYj2ZdOyNRYGuml5scHv7LA0zCggpKhI9w2cbfVZ-wknn2oV9Xs9odyPJGYTF7pZgr3POafF8M83nFTQ7ofkR59NLwPr0-GtqSXA7ly3DK4q2XyPWHG-RJxE-YWzZjfOqeIIAPcx9nNhtyUv5cM0t1NM30DrLZ6FW5ZELY417HdSl7AqZFF66aFIsbNRtnLbrjkNkOOEPBculTjCEIMUvB_djRKf1Wlzj8MquSutUhi0nkh12hywKtDeHVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کامنت های دردناک مردم زیر قیمت PS5 تو سایت دیجی‌کالا
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69488" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69487">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=QCN9Z-m7VdsGXpOMtH5nABCGd8-DqvpKFZPp4frXvMLkVyYpHTs6bj1GZng5Fp3kkVdtoFESApFoEOEr5aqQ3XxR9VFS2vdeFN-xUZ5WiQrtLhaATwcyxbuGNJuW2YFLqSfQhXh7usR1wynVWCufRN0qZR6-ZiD0C6wLtLwTyOXelCzbEPG91vTVO_VeUoPnKxlcJGBAPmRfA-U4bsTDLmEjruUu4Sp0og7SMUOvEWeu4YIMyGHauq64cNyTpub5r877gYD6HGGVzxmqER-Oyms8fLwBrW4NLp1Fw4wxRJdgz49MDIc0W93LzRVuR4ZE-lQ0gR8PvEkdtlRswVgtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=QCN9Z-m7VdsGXpOMtH5nABCGd8-DqvpKFZPp4frXvMLkVyYpHTs6bj1GZng5Fp3kkVdtoFESApFoEOEr5aqQ3XxR9VFS2vdeFN-xUZ5WiQrtLhaATwcyxbuGNJuW2YFLqSfQhXh7usR1wynVWCufRN0qZR6-ZiD0C6wLtLwTyOXelCzbEPG91vTVO_VeUoPnKxlcJGBAPmRfA-U4bsTDLmEjruUu4Sp0og7SMUOvEWeu4YIMyGHauq64cNyTpub5r877gYD6HGGVzxmqER-Oyms8fLwBrW4NLp1Fw4wxRJdgz49MDIc0W93LzRVuR4ZE-lQ0gR8PvEkdtlRswVgtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
✈️
یک جنگنده F-16 نیروی هوایی اوکراین، یک پهپاد انتحاری روسی (Geran-2) را با شلیک توپ ۲۰ میلی‌متری ولکان (M61 Vulcan) در آسمان اوکراین سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69487" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69486">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22887d7155.mp4?token=dzq8lppHT55fD5fbSoyJscjljTvZnat4s9VWmcBi3O6OyZFKJyaMYtsE9e0P9NxD50q-5cWrmUZpGjsvCspXmyZouS47WNgkLen0QDUd50xELrug11JBnCKJB6j7H0SvNtX8hUIl4UUlnMokvC8RD_iidyJsKajTTwbEVwBZFxXhhwc9v15KGwtUFxkM3_hFS5HI2DzPlr87UxSGB6qpw2ttdJM9NO7i3xqX0-cOKTuv7Z-6juFsn9qwhMGAWlbh3_kwlb73aFsnpqcBKOoWMxgQbKtwmJjmyPhjpwAp1_-1WJizgIvrrOAM3OUs3I1wCDMYkPjxTFaF3OimAf3Q3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22887d7155.mp4?token=dzq8lppHT55fD5fbSoyJscjljTvZnat4s9VWmcBi3O6OyZFKJyaMYtsE9e0P9NxD50q-5cWrmUZpGjsvCspXmyZouS47WNgkLen0QDUd50xELrug11JBnCKJB6j7H0SvNtX8hUIl4UUlnMokvC8RD_iidyJsKajTTwbEVwBZFxXhhwc9v15KGwtUFxkM3_hFS5HI2DzPlr87UxSGB6qpw2ttdJM9NO7i3xqX0-cOKTuv7Z-6juFsn9qwhMGAWlbh3_kwlb73aFsnpqcBKOoWMxgQbKtwmJjmyPhjpwAp1_-1WJizgIvrrOAM3OUs3I1wCDMYkPjxTFaF3OimAf3Q3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که میبینید ۱۲۶ سالشه و اهل کشور برزیلِ؛ در زمان پایان جنگ جهانی دوم تقریبا میانسال بود
این بدبخت نمرد تا جنگ جهانی سوم رو هم ببینه و دبل کنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69486" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69485">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها با من تماس گرفتند و گفتند: «لطفاً حمله نکنید. ما توافق خواهیم کرد.»
این حقیقت محض است و همه آن را می‌دانند. چه کسی تماس نمی‌گرفت؟
کسانی که اطلاعات را به بیرون درز دادند کمک کردند، چون شدت حمله را فاش کردند و ایران هم از آن آگاه شد.
آن‌ها می‌دانستند چه چیزی در راه است.
قرار بود دیشب [حمله] انجام شود و مدت زیادی هم ادامه یابد، و [در نهایت] چیزی باقی نمی‌ماند.
اگر فرصتی داشته باشم که به افراد زیادی اجازه زنده ماندن بدهم، می‌خواهم آن فرصت را فراهم کنم.
بنابراین، هیچ محدودیت زمانی‌ای ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69485" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69484">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20068f370b.mp4?token=uxnyLSVdKD-iz7k_hUPtm2ooeKCMMDV5dlj_mPqIyKvVSNmZnu4zAf5GHE21lV_elg-BrW4tqd3Fmipy8wojHeMynuLKxGSEOHvo95bx6W8tWlb2-xN19082DLOU2KWGZS-NjIROhytVMHREKLuGHUcuTk48c1HZ5wCU7JjgX-JDr2pDClzhmjywcmzzMfMnfTqkMtTaq0FsEIJaS_EYodOexRYq_eCc21oL2uu7X45HP6jn95JMaXCjQRUP_yD6ejh53akNKB7joDZdUSPkKAyn4E2cFCsiv2URD7g8cuDEXDeXYbJiCNpnIifuyEtRddx7czNYgOXMhp2QiRaSHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20068f370b.mp4?token=uxnyLSVdKD-iz7k_hUPtm2ooeKCMMDV5dlj_mPqIyKvVSNmZnu4zAf5GHE21lV_elg-BrW4tqd3Fmipy8wojHeMynuLKxGSEOHvo95bx6W8tWlb2-xN19082DLOU2KWGZS-NjIROhytVMHREKLuGHUcuTk48c1HZ5wCU7JjgX-JDr2pDClzhmjywcmzzMfMnfTqkMtTaq0FsEIJaS_EYodOexRYq_eCc21oL2uu7X45HP6jn95JMaXCjQRUP_yD6ejh53akNKB7joDZdUSPkKAyn4E2cFCsiv2URD7g8cuDEXDeXYbJiCNpnIifuyEtRddx7czNYgOXMhp2QiRaSHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در مورد ایران:
می‌خواهم قبل از نابودی کامل، آخرین فرصت را به ایران بدهم.
امیدوارم سر عقل بیایند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69484" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69483">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T5Ud0I4wrA-nKu1Zew8tMRQSNj3rXWzNBo2tfVwX8EVdsXAVwpYJquOPgh8mowdJHnt7j0NTxJgd1v1JXmAojk_bpkG30t52pZ_VmqLelZq1rhJ0F2IWYKfF3HDXrRR--MvumojF2gwZlmKfVfxCqVnqBhtgKEBGAFuhLHrTjb4SqGvdX-JgnoUfngETgdW-75oWYE4_WtZG5LL81gtzT9B_jyHPsW0oWghYqdCFD-ES0Alc-AlE1gehoneZZO2eK66RiSo1asiW8yBz1XjOl57fMmZJR_2IC65dpGb3hPfae147jnux9IIBhMa9WHOQNNxQJ2ukz6VC_2FYK3SDttY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T5Ud0I4wrA-nKu1Zew8tMRQSNj3rXWzNBo2tfVwX8EVdsXAVwpYJquOPgh8mowdJHnt7j0NTxJgd1v1JXmAojk_bpkG30t52pZ_VmqLelZq1rhJ0F2IWYKfF3HDXrRR--MvumojF2gwZlmKfVfxCqVnqBhtgKEBGAFuhLHrTjb4SqGvdX-JgnoUfngETgdW-75oWYE4_WtZG5LL81gtzT9B_jyHPsW0oWghYqdCFD-ES0Alc-AlE1gehoneZZO2eK66RiSo1asiW8yBz1XjOl57fMmZJR_2IC65dpGb3hPfae147jnux9IIBhMa9WHOQNNxQJ2ukz6VC_2FYK3SDttY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران حاضر است به وضعیت آزادی کامل کشتیرانی در تنگه هرمز بازگردد؟
🇺🇸
ترامپ:
اجازه نمی‌دهم آن‌ها [بابت عبور] هزینه دریافت کنند. اگر قرار باشد کسی هزینه‌ای دریافت کند، ما خواهیم بود. ما کنترل کامل را در اختیار داریم.
ما سازوکاری در نیروی دریایی داریم که نوعی محاصره محسوب می‌شود؛ آن‌ها به آن «دیوار فولادی ایالات متحده» می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69483" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69482">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=eoNGrZSJITsqSGQP43tJ70IwWv1y3-QDOX4g8Y6rEh3RiNsnBVEF7ea_Mmdojupto0sUQPDOiuJWliAZ-6teLg_lGo8493DnEX6TTUv_xvqtVLuccuqbGDFg2ThQTVUB29oKSiQ0GCVYLaWpj4bOaJpibxFr-bWNWSAWEeUgiHfGa0QA3UwAAP5vaX0WG_F-3eQdvao5b59IMKo8WqOFpOkm3E_CSS-3rKqEMtTdLRm-kDBjl3Sc3N1Gd7w64O_mcogkizva8MCj7WU5mYGwXKQlm_RLdPea68iVQYBWKk11EPpwDaQkhj68Qf3d38ExwqbPx9WL2pkVi26jl6LxzgUoLV_KoQe_Kw_s4CAdYEAjj4yhpzIElg-Si4HPfVz7Reo1ClB9-fE5m6s9sudq2OeZzayJkOJlcL3p8pmTOSsCH-ngMX_ZE5Q73fWXSzZXraKgSpxaVXHURJY0BlBWKbPq6uqXtvlsPMuC7rbiVBgBXh1uTT1RyjvnYFiNGbzFqAyeMZaTuzrv1scQDoNvS3mdOxDTInV3gB-qQS5mNWwjtXLlhyFDnes6yl8ZI9QVhPwrftHqcg0kCLnUIMxqlnlCXpBS2OYiPO-GcpghEFJLpGlTkq4pg9NfC9OxgF-MfR9vxQu_bTvktPClxvESvJR8n7R13E8U_SYewBEN3GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=eoNGrZSJITsqSGQP43tJ70IwWv1y3-QDOX4g8Y6rEh3RiNsnBVEF7ea_Mmdojupto0sUQPDOiuJWliAZ-6teLg_lGo8493DnEX6TTUv_xvqtVLuccuqbGDFg2ThQTVUB29oKSiQ0GCVYLaWpj4bOaJpibxFr-bWNWSAWEeUgiHfGa0QA3UwAAP5vaX0WG_F-3eQdvao5b59IMKo8WqOFpOkm3E_CSS-3rKqEMtTdLRm-kDBjl3Sc3N1Gd7w64O_mcogkizva8MCj7WU5mYGwXKQlm_RLdPea68iVQYBWKk11EPpwDaQkhj68Qf3d38ExwqbPx9WL2pkVi26jl6LxzgUoLV_KoQe_Kw_s4CAdYEAjj4yhpzIElg-Si4HPfVz7Reo1ClB9-fE5m6s9sudq2OeZzayJkOJlcL3p8pmTOSsCH-ngMX_ZE5Q73fWXSzZXraKgSpxaVXHURJY0BlBWKbPq6uqXtvlsPMuC7rbiVBgBXh1uTT1RyjvnYFiNGbzFqAyeMZaTuzrv1scQDoNvS3mdOxDTInV3gB-qQS5mNWwjtXLlhyFDnes6yl8ZI9QVhPwrftHqcg0kCLnUIMxqlnlCXpBS2OYiPO-GcpghEFJLpGlTkq4pg9NfC9OxgF-MfR9vxQu_bTvktPClxvESvJR8n7R13E8U_SYewBEN3GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره مذاکرات با ایران:
امروز یا فردا متوجه خواهید شد که وضعیت مذاکرات در چه مرحله‌ای است.
مذاکرات به هر طریقی که باشد، به‌سرعت پیش خواهد رفت؛ موضوع پیچیده‌ای نیست.
ما درباره بازگشایی تنگه [هرمز] در روز آینده صحبت می‌کنیم؛ بازگشایی کامل آن.
سپس درباره توانمندی هسته‌ای ایران گفتگو خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69482" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69481">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=TV_qvbNqpzRPJfcmRXLggdubwvYmEuL8w_3vz76oNaVTobJKLDOnjVX6sURuR8dUMF3hByzTfL-UEYMMIs5zjntvKMNKA7RWGH5RuUsaVKpFGxcLQQ2fTS43JljoGFG3ZCtEX0X-MzY6sly3aQjCCGzsZH2OTXbtciYZV-TChGijsJ3YWyH4NlCv-Ac3Kt-nFWfSTMcVh3R_AogH-QBZLfuZvk4_B-SPvwqZJ0DJZi9aRbrs6DlqK8GJdltLV7_-CSJqslFHYjtvVH0xAteEW5VtIIN1fi-xdzADOd7NIu3kz7_uUJqZneOnER6KTrIw3Frv1e3Gf956SrmXnOxXxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=TV_qvbNqpzRPJfcmRXLggdubwvYmEuL8w_3vz76oNaVTobJKLDOnjVX6sURuR8dUMF3hByzTfL-UEYMMIs5zjntvKMNKA7RWGH5RuUsaVKpFGxcLQQ2fTS43JljoGFG3ZCtEX0X-MzY6sly3aQjCCGzsZH2OTXbtciYZV-TChGijsJ3YWyH4NlCv-Ac3Kt-nFWfSTMcVh3R_AogH-QBZLfuZvk4_B-SPvwqZJ0DJZi9aRbrs6DlqK8GJdltLV7_-CSJqslFHYjtvVH0xAteEW5VtIIN1fi-xdzADOd7NIu3kz7_uUJqZneOnER6KTrIw3Frv1e3Gf956SrmXnOxXxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک سند خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69481" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69480">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=B3YqfOBmrLTDlgdxc37PeYz21C_FBzNOPMYfjwCJ4VGD17fcQVKb4ZQm3yji9MaXa8iRQJV9PWiaM_qt74X3vqHoPha70d1NqMOHkciV6-ZxI8j3i6uj1AWM9k_qkOGV-RNLd3t_wXUpZjm7bK19TNP3Qo1sN0QIpSOIIrsDakBCLuClR3jByLtwLzNpdAUCPOoXbBJwqpFuYedfepj6P_V3E7COMWILcw1jKZDvUSyQRnixdrE3OWKwhJgmjHSrzY8ZpCpaF8T5pMm78PmBSwzRaezbwPKYj9pT9dgttK_aPHErZew9uC7cavlRt8hhNPNwvLrk5GUhLvpyhmQA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=B3YqfOBmrLTDlgdxc37PeYz21C_FBzNOPMYfjwCJ4VGD17fcQVKb4ZQm3yji9MaXa8iRQJV9PWiaM_qt74X3vqHoPha70d1NqMOHkciV6-ZxI8j3i6uj1AWM9k_qkOGV-RNLd3t_wXUpZjm7bK19TNP3Qo1sN0QIpSOIIrsDakBCLuClR3jByLtwLzNpdAUCPOoXbBJwqpFuYedfepj6P_V3E7COMWILcw1jKZDvUSyQRnixdrE3OWKwhJgmjHSrzY8ZpCpaF8T5pMm78PmBSwzRaezbwPKYj9pT9dgttK_aPHErZew9uC7cavlRt8hhNPNwvLrk5GUhLvpyhmQA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
قرار بود دیروز ضربه بسیار سختی به آن‌ها وارد کنیم؛ بسیار بسیار سخت.
سخت‌تر از هر حمله‌ای از زمان جنگ جهانی دوم. این اقدام بسیار بزرگی محسوب می‌شد و ما کاملاً آماده اجرای آن بودیم.
در حال حاضر، به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و بسیاری دیگر، مشغول گفتگو هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69480" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69479">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=ERraPrTpatfvWo__AnvX14quzUhryXJvJl7FLd5BwsDi-j2tGpmRL_kQqAdSDIwg7PDo9AVpa60kAZxVeGkozyPFAznaAvv2UV6fXyunbefAx8vlv29YDh1heF0vlUmIiDEBbA-2OAREVvbiVksGTvYqMeB2sbeHNUVbWA9-4-gr0D-ZsyKqwgyWcIhyqy0dD3OcIW4dHhOU3x2PP0NkJ_WKnlCDqs4I7u-FxHGDiK22iCOl5gtFf2ryfAFZqJnodNZDhzK1iaNxPHQiVNq4W3dXTRnbSLby5_jz8T9x6H80ozKODy9rRg_DvKA2J75b5AxnvH390vGs-WaNRqPDtCUBuEb-XEYtbkVii2Jc1Qvl5eDDUIvFAu75J3RFX388aWO58wu0iEbIGE_BRorQSa61BMQBBuwKGeAqXrKoY4-oC6Qz6_dmJWbjRe_pV-m-mANqNfax7Ei5shlntSlUwKJIwtORErXN5RpJTF6_bBQcCQT3w7yTDq4gdi7H9Ur8SD_SpNVHPMqwvFG-gIMP9TcogMOpDtsPAEKsFgJlRnnOvH5bvj67vTNjZJ29ljdxn1kr4RLCBmY4W1ppXvX2MCkjRha6ZjCbPNLY3qF_kf-2y8sfn2SFgk8cMZZAfgkq2P2nonT2WVht4U5rjO83VNqkDu0E3bmLeU5qTdprbCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=ERraPrTpatfvWo__AnvX14quzUhryXJvJl7FLd5BwsDi-j2tGpmRL_kQqAdSDIwg7PDo9AVpa60kAZxVeGkozyPFAznaAvv2UV6fXyunbefAx8vlv29YDh1heF0vlUmIiDEBbA-2OAREVvbiVksGTvYqMeB2sbeHNUVbWA9-4-gr0D-ZsyKqwgyWcIhyqy0dD3OcIW4dHhOU3x2PP0NkJ_WKnlCDqs4I7u-FxHGDiK22iCOl5gtFf2ryfAFZqJnodNZDhzK1iaNxPHQiVNq4W3dXTRnbSLby5_jz8T9x6H80ozKODy9rRg_DvKA2J75b5AxnvH390vGs-WaNRqPDtCUBuEb-XEYtbkVii2Jc1Qvl5eDDUIvFAu75J3RFX388aWO58wu0iEbIGE_BRorQSa61BMQBBuwKGeAqXrKoY4-oC6Qz6_dmJWbjRe_pV-m-mANqNfax7Ei5shlntSlUwKJIwtORErXN5RpJTF6_bBQcCQT3w7yTDq4gdi7H9Ur8SD_SpNVHPMqwvFG-gIMP9TcogMOpDtsPAEKsFgJlRnnOvH5bvj67vTNjZJ29ljdxn1kr4RLCBmY4W1ppXvX2MCkjRha6ZjCbPNLY3qF_kf-2y8sfn2SFgk8cMZZAfgkq2P2nonT2WVht4U5rjO83VNqkDu0E3bmLeU5qTdprbCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: مذاکرات با ایران حالا دیگه متوقف شده.
🇺🇸
املاکی: نه، همین الان هم مذاکرات در جریانه. واقعاً اتفاق عجیبیه.
این بار دیگه اصلِ مذاکره رو انکار نمی‌کنن.
فقط نمی‌دونم چرا، هر وقت دارن مذاکره می‌کنن، دوست ندارن بگن که دارن مذاکره می‌کنن.
با ونزوئلا یه درگیری داشتیم که خیلی خوب جمع شد.
الان هم با ایران درگیر یه پرونده هستیم و اون هم داره خیلی، خیلی خوب پیش میره.
شما هم دارید فوق‌العاده کارتون رو انجام می‌دید.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69479" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69478">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=Mx9LzWOIXdiYjzugNHKb3NgGeGnZh6vuM0X16iFXJUt-_yV67aGXI75Jww__1F-_6wJk4E_z54JkoL1tgsPNmAzVwQaZgwfZKtuC5yDIkhMV2eCKo8at_IrEY3drDzCkct5XSjVKjSzDD7f0xaQpMK1UXG2gIwWY6LNgtHqaYrLS6gMP8h4gAO8vSZaf-ojr9VWw6TvsJGSq2Q5kFMOUuVHUAAL0Ao2r6r-abedfyT2OgOrxp2DFxx9z1DvXoXw7vXTqaIdJt4qtaBJffLzIY0nwjh1NegwZopVfOQBBBwjZxlV6QyskJ5ybptOrcw4LWYIWmfqiEVxQAjKgEXJxlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=Mx9LzWOIXdiYjzugNHKb3NgGeGnZh6vuM0X16iFXJUt-_yV67aGXI75Jww__1F-_6wJk4E_z54JkoL1tgsPNmAzVwQaZgwfZKtuC5yDIkhMV2eCKo8at_IrEY3drDzCkct5XSjVKjSzDD7f0xaQpMK1UXG2gIwWY6LNgtHqaYrLS6gMP8h4gAO8vSZaf-ojr9VWw6TvsJGSq2Q5kFMOUuVHUAAL0Ao2r6r-abedfyT2OgOrxp2DFxx9z1DvXoXw7vXTqaIdJt4qtaBJffLzIY0nwjh1NegwZopVfOQBBBwjZxlV6QyskJ5ybptOrcw4LWYIWmfqiEVxQAjKgEXJxlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
ما با ونزوئلا اختلافاتی داشتیم که به خوبی حل و فصل شد.
ما با ایران نیز اختلافاتی داریم، و این موضوع نیز به خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69478" target="_blank">📅 21:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69477">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=mICiwmqxVGVh3uoMinkCk0n9mlD3aUAY6NT5IxAxg0po73AaL7VSdv_Arl_FCeUl3-_QtdfoAP_YvMsYmvROavEf9weYLMYuy9vnB9pPG35RlDrL9QNkdGcc1HuON5KLVOUgghwQRp43t6L_Y73PdnJyz-eWcTQr08W7bwyRHTosCkdOM0RNffzII29aTVBTbGr-hi8CSC0pHNAKG24VSkWcgHP3oICkI8X_smzmUtHq1ruC5_Uvijcoc9O5WqXW-UD9I4-0OPtb_UE1Sf6E8-OvUHcHco8nHYtKfQYPWn85E3QLjmJ3zZt0RJ1orA7815IOGY0lo_pJz6LAbsImrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=mICiwmqxVGVh3uoMinkCk0n9mlD3aUAY6NT5IxAxg0po73AaL7VSdv_Arl_FCeUl3-_QtdfoAP_YvMsYmvROavEf9weYLMYuy9vnB9pPG35RlDrL9QNkdGcc1HuON5KLVOUgghwQRp43t6L_Y73PdnJyz-eWcTQr08W7bwyRHTosCkdOM0RNffzII29aTVBTbGr-hi8CSC0pHNAKG24VSkWcgHP3oICkI8X_smzmUtHq1ruC5_Uvijcoc9O5WqXW-UD9I4-0OPtb_UE1Sf6E8-OvUHcHco8nHYtKfQYPWn85E3QLjmJ3zZt0RJ1orA7815IOGY0lo_pJz6LAbsImrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فرماندهی مرکزی آمریکا (سنتکام) فایل صوتی مکالمه ناو آبی‌خاکی USS Comstock (LSD-45) با یک شناور ناشناس را منتشر کرده است. در این مکالمه که از طریق کانال ۱۶ رادیویی دریایی VHF (فرکانس بین‌المللی تماس و اضطرار) انجام شده، به شناور دستور داده می‌شود مسیر خود را تغییر دهد و هشدار داده می‌شود که در صورت عدم تبعیت، با استفاده از زور وادار به اجرای دستور خواهد شد.
ناو USS Comstock به‌عنوان بخشی از گروه آماده آبی‌خاکی USS Boxer (ARG) و همراه با یگان یازدهم اعزامی تفنگداران دریایی آمریکا (11th MEU) در منطقه مسئولیت سنتکام مستقر است و توانمندی اجرای عملیات آبی‌خاکی و واکنش سریع به بحران‌ها را در اختیار نیروهای آمریکایی قرار می‌دهد.
بر اساس آخرین اعلام سنتکام، نیروهای آمریکایی تاکنون ۴۴ کشتی تجاری را که به‌صورت داوطلبانه از دستورات محاصره تبعیت کرده‌اند، به مسیر تعیین‌شده هدایت کرده‌اند، دو شناور را برای اطمینان از رعایت دستورات بازرسی کرده‌اند و دو شناور متخلف را که با وجود هشدارهای مکرر از اجرای دستورات خودداری کردند، از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69477" target="_blank">📅 21:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69476">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI1F4x3s3imPUaXjKULPyQ3NJlFsNuu1RbsrpfESBbVJs2qPfawCCWlH9H8q4gCNY8xsQ6CXuorN8cDjxzL56B6Rs16_vhTDFHX8NlJH4SXDNrVVShbK0p686rv-p_IoJ6JQX5jNsxrmGcEoHKrzT8Y4mEHY_wsMERCkDMg7c3n0BwDQ5DuEzaveSL7OkmFvtlhuwlVOi7y3UOle2WEXMFGEtsWMp-2Ro4lDEVUMwMJJXiOkQkUJXVNcuIaEb3RGUMcyotQ9gHk_2jKN3CV5JnWA6pAsha6YSmQwzotQDglyPEZyBh7ze6lRsqfCirECS8Y0DaxgDo5LSDv_Y12nFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مارک لوین:
من از اسرائیل حمایت می‌کنم.
من از اوکراین حمایت می‌کنم.
من از تایوان حمایت می‌کنم.
من از مردم ایران حمایت می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69476" target="_blank">📅 20:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69475">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwwKJ7nq4MFpQvzVZzFpqRDlbotrCJdS-6JFPXrJ-ifSyEYv4x5LU_WTwPPOGeZedZQBVAWe4lSuljKSC32W2B2_TcfhPBgWMcN27BrLIaPG93Xtbg_as_ArwR3x-aGikp0ZiKZYzA1pEoYrD1fjQMhO5wp4vjITZn1ieedPyRrCeAEpusVARGL2jOUBTgutq6FSRXEG1kvzd1SsClVIqxn1NHHvsPZYz4jKoDkr6dKJ7bW0GG-yneZaROVhpGEQWpNVe_OBKwEsQmW78Q-ybjPmCZELvKnGHS6dQGV24N5ckOX9Ycg1X3qoRUuZsXreJq3dy7YacjoLEmdFXt3cJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ : رهبری ایران واقعاً یه جورایی دو‌رو و ریاکاره که باورنکردنیه؛
خودشون می‌خوان مذاکره کنن، بعضی‌ها حتی میگن التماس می‌کنن، مذاکرات شروع می‌شه، جلسه بعدی هم قراره به‌زودی باشه، بعد علناً و با افتخار میگن که هیچ مذاکره‌ای در کار نیست، هیچ صحبتی نمیشه و فقط با «عمان» کار دارن!
بعدش هم همون چرت‌وپرت همیشگی‌شون رو تحویل می‌دن که می‌گن تنگه هرمز رو با قدرت خودمون اداره می‌کنیم، در حالی که از قبل کاملاً تحت کنترل نیروی دریایی آمریکاست و همون «محاصره» یا همون‌طور که بعضی‌ها می‌گن «دیوار فولادی ایالات متحده»!
هیچی به ایران نمی‌رسه مگر اینکه ما بخوایم، و هیچی هم نخواهد رسید مگر اینکه یه توافقی بشه یا اینکه کامل تسلیم بشن.
فرقی نمی‌کنه ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم درباره‌ی راه‌حل مشکلی حرف می‌زنیم که خودشون دهه‌هاست ایجاد کردن، خیلی ساده‌ست:
ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69475" target="_blank">📅 20:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69472">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4129d878df.mp4?token=r5v16AvfBwSMcmi8Nr-qGcVQEgZ36zf4HxgE6oOVmbYWb0rp4icYcvx_jKKLlyAHl6GWfDJ0Kv563tHYFptfrfI_tPW4rmy3xtYhrzTi39xoukhaup30SK7Y7hTAPEf8i7fgpowBwakfecDsNRjHm5ADWpXRd_QeMHBXyfzq0oF1KQxx6V31YXvae1ZQoUyRt6iHVKZ6cuU7OzwW8tFONdG342Hb0O3VWgvhqKl4zM2SnFrzuudC7bUW82UeYeRmOi-cPRmBVzRxFdv3ZBt8T-XDPVaQgdj1ueJe8rZrTF1ooOyQzUjSGeK9CHGEFwyYN4VO-bBPi5inxGH2RtcEmA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4129d878df.mp4?token=r5v16AvfBwSMcmi8Nr-qGcVQEgZ36zf4HxgE6oOVmbYWb0rp4icYcvx_jKKLlyAHl6GWfDJ0Kv563tHYFptfrfI_tPW4rmy3xtYhrzTi39xoukhaup30SK7Y7hTAPEf8i7fgpowBwakfecDsNRjHm5ADWpXRd_QeMHBXyfzq0oF1KQxx6V31YXvae1ZQoUyRt6iHVKZ6cuU7OzwW8tFONdG342Hb0O3VWgvhqKl4zM2SnFrzuudC7bUW82UeYeRmOi-cPRmBVzRxFdv3ZBt8T-XDPVaQgdj1ueJe8rZrTF1ooOyQzUjSGeK9CHGEFwyYN4VO-bBPi5inxGH2RtcEmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
درگیری عرزشی ها و پلیس عراق در کربلا:
توی عراق یه روحانی به اسم صادق شیرازی، مخالف جمهوری اسلامی و خامنه‌ای هست، اون معتقده که فقط باید گفت لبیک یاحسین، نه لبیک یا خامنه‌ای.
حالا عرزشی‌ها دیشب افسار پاره کردن و هجوم بردن سمت موکب این روحانی و شعار مرگ بر آمریکا و لبیک یا خامنه‌ای سر میدادن.
عرزشی‌ها شروع کردن به کتک زدن مردم عراق تا اینکه پلیس وارد شد و با شوکر و باتوم عرزشی‌هارو کتک میزد.
طی این درگیری بیش از ۱۰۰ نفر به بیمارستان منتقل شدن و عراقی‌ها میگن دیگه نباید ایرانی‌هارو راه بدیم، غذای مفت میخورن و مارو کتک میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69472" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69471">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=JkG2n7spigo0svZqeiHcBIBE0Ade8ubEQajxC-4e_aX4xqSwK4yL5ehjS6qhY8VTS2JXnix5ShJg_oJCq0wef8ObdyOe_SlmWdGNhqxyB3WQvkqRcIOBYMNdnkimm7gFJq2ZBUrcBWXIoJkOiHEG9LXEErXEXn4fXgJzgQVAib26SCivsvSDskPt8zNC-agOVM6pstirrhDR_wJr3f_gxCWSZxgk1OruErK3JXhkwUESWQ_NK8iGjI8yxeI32aHs-65eJELTmsEBCIvy8hQBrElAoRW5zept3C5b5kWbZaVbGmt-2XGQLfOoU4xBvP4GInqKhaaapljBo3pgRYEWj5cJAOfNq8wJ8313wwWBffW-WsUN7IP6PrCZdSDq8MRG34xkRcBPhpxO4FYP7NGaH-zbqhxTFOZB9CeiKPNRoLByn155hTHUscNlKJ7OOvcdBMVc0LfsRCIwRGQU36r4dDgP2wGp6ubub4kuKL0_zY9GIZ0eRMh0ZHaTOtQ7Zky3LknL1Gzhd88T5Uxl4WPwD6ELSd0N-wju6Ug4gNDFaSB6xw_5uGIQwVV8uOyN2d3yUw6whrvQG6L3EF9zi0CGaphoCMJb49ha_eFrlH59qMvhIT6VJKNNrYKFchZDHYZ7CumXqvyCxdw46Cxt7u_GzbTSd6QHZh2mw4Of3Tle65M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=JkG2n7spigo0svZqeiHcBIBE0Ade8ubEQajxC-4e_aX4xqSwK4yL5ehjS6qhY8VTS2JXnix5ShJg_oJCq0wef8ObdyOe_SlmWdGNhqxyB3WQvkqRcIOBYMNdnkimm7gFJq2ZBUrcBWXIoJkOiHEG9LXEErXEXn4fXgJzgQVAib26SCivsvSDskPt8zNC-agOVM6pstirrhDR_wJr3f_gxCWSZxgk1OruErK3JXhkwUESWQ_NK8iGjI8yxeI32aHs-65eJELTmsEBCIvy8hQBrElAoRW5zept3C5b5kWbZaVbGmt-2XGQLfOoU4xBvP4GInqKhaaapljBo3pgRYEWj5cJAOfNq8wJ8313wwWBffW-WsUN7IP6PrCZdSDq8MRG34xkRcBPhpxO4FYP7NGaH-zbqhxTFOZB9CeiKPNRoLByn155hTHUscNlKJ7OOvcdBMVc0LfsRCIwRGQU36r4dDgP2wGp6ubub4kuKL0_zY9GIZ0eRMh0ZHaTOtQ7Zky3LknL1Gzhd88T5Uxl4WPwD6ELSd0N-wju6Ug4gNDFaSB6xw_5uGIQwVV8uOyN2d3yUw6whrvQG6L3EF9zi0CGaphoCMJb49ha_eFrlH59qMvhIT6VJKNNrYKFchZDHYZ7CumXqvyCxdw46Cxt7u_GzbTSd6QHZh2mw4Of3Tle65M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
عملیات آزادی عراق؛
در ۱۷ مارس ۲۰۰۳، جورج بوش بزرگ رئیس جمهور آمریکا در یک سخنرانی تلویزیونی به صدام حسین و پسرانش (عدی و قصی) ۴۸ ساعت فرصت داد تا عراق را ترک کنند.
او هشدار داد که در غیر این صورت، حمله نظامی در زمان انتخابی آمریکا آغاز خواهد شد؛
پس از پایان اولتیماتوم، بوش در اتاق وضعیت کاخ سفید  او در آنجا دستور رسمی حمله را امضا کرد.
بیش از ۱۰۰۰ بمب که بعضی آنها ۱ تن وزن داشتند و ۵۰۰ موشک کروز تاماهاوک را به سمت مواضع ارتش صدام شلیک کردند، بین ۱۵۰۰ الی ۱۷۰۰ سورتی در ۲۱ مارس انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69471" target="_blank">📅 19:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69470">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=DnJefNHqR2wlEdPy8DpqQ6CX2f1Y6UrEx4o_0UgXoQ2RUrx5-olhPtpGGTeU--0_lsE8S8KtjDwHTcUPJGM_NnslgueKyJoqry97oPoY94QyfzjBDvrLDzNqCY6Wjz-KodQ0yRh7NjGc2eavdxqTM5cvrfxVc3At0p3Tb8jr7C3mCwoU27nMC7aa-5IfvNsOV_vpa7VhyBxIyx7WWsUQ6QVZ406qcAGiHZBtpI1qa-EBN270_c7-ylgzQE61qKtrFfLz22cVcomoWkeAtZRvJZCsBHeDQyATh9ay2XTf1qKnV7ivCjKCRS0-0-TGPagpLqPNQZNsrQrVDzz4DibAMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=DnJefNHqR2wlEdPy8DpqQ6CX2f1Y6UrEx4o_0UgXoQ2RUrx5-olhPtpGGTeU--0_lsE8S8KtjDwHTcUPJGM_NnslgueKyJoqry97oPoY94QyfzjBDvrLDzNqCY6Wjz-KodQ0yRh7NjGc2eavdxqTM5cvrfxVc3At0p3Tb8jr7C3mCwoU27nMC7aa-5IfvNsOV_vpa7VhyBxIyx7WWsUQ6QVZ406qcAGiHZBtpI1qa-EBN270_c7-ylgzQE61qKtrFfLz22cVcomoWkeAtZRvJZCsBHeDQyATh9ay2XTf1qKnV7ivCjKCRS0-0-TGPagpLqPNQZNsrQrVDzz4DibAMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
اکثریت قاطع ایرانیان، اسرائیل را تحسین می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69470" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69469">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=W6kn0fBIGeKx3wHrx47C3bfE-iscNerF_TR9VY466gmot9OyGf4XVGsLWsBFMOU3wSis8CUlzwMN467GRuM7O5Aha8t_zJ4vhFWbJeI6h5tZvyDQrfpUhmBima0glijKJgs3IxX__bSL1BLj1DWC9n33WgibiKxj7TwD30lgjxcZvueGqERmcbl_7Im2VIONADtVZMIlvmgGpsc8xIhw4yBzzlc2WJDWPhDYaG_IV7DOKv_ima2xHSHyLu6Um4rVk5YWlUfGWofOoXxEjoK7wLy5KPgV9K2MPMICGX5LIB7ZvxAMcOXUr2tzvTFSM0rmRRuHTb2lKSeziXRLcb2lEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=W6kn0fBIGeKx3wHrx47C3bfE-iscNerF_TR9VY466gmot9OyGf4XVGsLWsBFMOU3wSis8CUlzwMN467GRuM7O5Aha8t_zJ4vhFWbJeI6h5tZvyDQrfpUhmBima0glijKJgs3IxX__bSL1BLj1DWC9n33WgibiKxj7TwD30lgjxcZvueGqERmcbl_7Im2VIONADtVZMIlvmgGpsc8xIhw4yBzzlc2WJDWPhDYaG_IV7DOKv_ima2xHSHyLu6Um4rVk5YWlUfGWofOoXxEjoK7wLy5KPgV9K2MPMICGX5LIB7ZvxAMcOXUr2tzvTFSM0rmRRuHTb2lKSeziXRLcb2lEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
خاورمیانه دیگر آن خاورمیانه سابق نیست. ایران هم دیگر آن ایران سابق نیست. ضربات سنگینی به آن‌ها وارد شده است.
آن‌ها همچنان توانمندی‌هایی دارند، اما به یک ماه گذشته نگاه کنید؛ آن‌ها به سمت ما شلیکی نکرده‌اند.
چرا شلیک نکرده‌اند؟ چون می‌دانند ما می‌توانیم چنان ضربه سنگینی به آن‌ها بزنیم که بازدارنده باشد. اگر به ما حمله کنند، متحمل ضربه‌ای بسیار سخت خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69469" target="_blank">📅 18:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69468">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=jsCaKBlHiofEc89YbSUtwgh1p2ha0DBX_hEeIpN0qX7AHAZFs1M52PPPJr5-kG8zvTMOTgx3Llmm0f5rPQc_0My90PZ-srKvFNqxHvZxi5mYFY3A8CNUOnyQxRI3R4Km79bzZKDUPCPRintaQfS-USrqxo1mAKCiUCxUQTPpxdohueWFwbaznhKPrLmTFOijbZDIrF4HC-2UgSlP8wF7fPeWSOpjOKDwyCdhvyhAEiPy8-X8WZL9bDMpinCdhlNdF3TLCqzvCQrqRE-DFGcXttzdMp0lT8pS-sMT4iH3j5aQ55i5JAmHtjG0sLRr9UI4TjcRfYvYXR5ulaWZtWHkUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=jsCaKBlHiofEc89YbSUtwgh1p2ha0DBX_hEeIpN0qX7AHAZFs1M52PPPJr5-kG8zvTMOTgx3Llmm0f5rPQc_0My90PZ-srKvFNqxHvZxi5mYFY3A8CNUOnyQxRI3R4Km79bzZKDUPCPRintaQfS-USrqxo1mAKCiUCxUQTPpxdohueWFwbaznhKPrLmTFOijbZDIrF4HC-2UgSlP8wF7fPeWSOpjOKDwyCdhvyhAEiPy8-X8WZL9bDMpinCdhlNdF3TLCqzvCQrqRE-DFGcXttzdMp0lT8pS-sMT4iH3j5aQ55i5JAmHtjG0sLRr9UI4TjcRfYvYXR5ulaWZtWHkUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دیروز روسای دانشگاه تو جلسه‌ گله کردن که چرا حقوق اعضای هیئت علمی دانشگاه رو با تاخیر دادین؟
پزشکیان هم تو جلسه کلش خراب شد گفت:
نامه نمیخواد، اون گوشیو بده من بینم...
📞
«سلام؛ حقوق هیئت علمی دانشگاه‌ها رو ۱۰ روزه ندادین. خداوکیلی این درسته؟... بده دیگه... دستت درد نکنه، خداحافظ.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69468" target="_blank">📅 18:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69467">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04343db3da.mp4?token=NDArEDr5GfZsJ0KkqIWa0g-AweKPsp-UmO2RflTOUuxAvenQPc75HZQ6YZHim9TTbGQo7__N0P7nTv0cxYK81RsfpNfhta2WUQjpqMMxqR1tAwHO672dk_JPeI6JTU30mBRILCoX1AtwBNReEkGUDldDRrk-tAoIi7l8J6pczr98kVVwojypmhGgEvo9gPMJRSiGN80hB0cg7g1CzsdS610a7OBO3UGUI7d4GfFXP1KnTWXL4F9Pht7tR80vwY1DSVyrriJTHxnaR2lb6VxkzPDHpq0MpSLGqIgyX7BOSZSWzmfkFIpbrXZNE9gHhsHY-wFWKibVvWRdDfZafoK_-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04343db3da.mp4?token=NDArEDr5GfZsJ0KkqIWa0g-AweKPsp-UmO2RflTOUuxAvenQPc75HZQ6YZHim9TTbGQo7__N0P7nTv0cxYK81RsfpNfhta2WUQjpqMMxqR1tAwHO672dk_JPeI6JTU30mBRILCoX1AtwBNReEkGUDldDRrk-tAoIi7l8J6pczr98kVVwojypmhGgEvo9gPMJRSiGN80hB0cg7g1CzsdS610a7OBO3UGUI7d4GfFXP1KnTWXL4F9Pht7tR80vwY1DSVyrriJTHxnaR2lb6VxkzPDHpq0MpSLGqIgyX7BOSZSWzmfkFIpbrXZNE9gHhsHY-wFWKibVvWRdDfZafoK_-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو ای از یک طرفدار حکومت که میخاد ترامپ رو بکشه:
میرم خون رهبرمو از ترامپ بگیرم یه دهنی ازش سرویس بکنم از یادش نره
از لحاظ دفاعی یا هجومی همه جوره دهن ترامپ رو میارم پایین
حرکت های رزمی‌شو ببینید فقط
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69467" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69466">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIrHK0PGPNCBwifkGkhUK8CiBo1_v2IZgDAB_81VK5XxyYya76stmx1JO53Ww_o1BXjPbQFVmP2H0DsKBsflGsQ3SjfsdpRJhJ5SwqzDWTbPqwVpeUvxuKZXBZ8ljU5wSa45wr3W0O_NQCcvVGyXCS2w9-eStDZEaw9eummUJ5qYhYpWc_AZRnCBd2dIUd-it-YtmHlv8yafmxaj9OF9A2ckCmZNmiyKvrL4gkmkZcyfNhuMaZgrGufmwEOe4sxtE6R8WNbyzVEcm06CrlG4N44VD7HAivW9EjJvwkxu7wJe_CYAq6Sv9allk2mbKxMMBuE7sC4jt_GEpUv-3LEhmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛المیادین به نقل از یک منبع ایرانی:
ایران در پاسخ به آخرین پیشنهاد آمریکا، با بازگشایی تنگه هرمز تا پیش از پایان کامل جنگ مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69466" target="_blank">📅 16:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69465">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcXeqYoUIFTTdaVyEgC6YgSHE_Us7GkG5go8oEYZHooD0mjl6o18aDAtYIFMcvBawpYis17mDKNJjYr5MvIx6WdZ2cEe-c-b6itU_jAbZunbX9UIT_JJ0K6vu5_exe_GpO2iR5sdOj15srRoq9CrcoMvBlDl5thVJ7Tceq8xU6GFLViENzly8-ODL2ktPQZjhv3fq57-qhObVeY-XtQSbmxwI_0HH5xed17PnR5LY0rFC02rDClLSKyVpZq2_WCt1oANPyj_A06zjJLoWB0mWvuKyhcDKoM9tdQjnHNqfKKKUSnRuQGqiXzdW0RxS_zKnHZxLGA0h7MTks_9zhRrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست میانگین IQ کشورهای مختلف تو سال 2026 هم منتشر شد
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69465" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69464">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863fff3357.mp4?token=BFHz-4B0rd_Ki55RlKxSnH_gPukLrvnp0Gr6oxhvAE64y0fcE_SPSRIZBjcAfe3ku8xW8KjL9loAWew55hIV9ELoNEFfq8PY99LfyxpxcfLBNVxYPVBFf18Y84FtepCHBoeq2b0oxzvPeUebQqlrcjpOiIJdi_JWsHXD9pofa1rH2W7DDkP4YFGAE6ikmj3VBxUvoAcT5OoB1gjUbjPjQ7pHe7ta2GdcZZtJ-ha6ORYGjJbv1xFTnW7szkz8zyAHolRqY32PDiCwmoi8Xww09IQTyZTlP3tViCg6uJq60-9UTkttybqmXPuSCnvZC_3MA52bYalLBTZNd7Rtbu3uTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863fff3357.mp4?token=BFHz-4B0rd_Ki55RlKxSnH_gPukLrvnp0Gr6oxhvAE64y0fcE_SPSRIZBjcAfe3ku8xW8KjL9loAWew55hIV9ELoNEFfq8PY99LfyxpxcfLBNVxYPVBFf18Y84FtepCHBoeq2b0oxzvPeUebQqlrcjpOiIJdi_JWsHXD9pofa1rH2W7DDkP4YFGAE6ikmj3VBxUvoAcT5OoB1gjUbjPjQ7pHe7ta2GdcZZtJ-ha6ORYGjJbv1xFTnW7szkz8zyAHolRqY32PDiCwmoi8Xww09IQTyZTlP3tViCg6uJq60-9UTkttybqmXPuSCnvZC_3MA52bYalLBTZNd7Rtbu3uTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مشهد یه دوره‌ی آموزشی گذاشتن برای افراد بالای 60 سال که توش مبانی اولیه‌ی استفاده از موبایل رو یاد میدن؛
موضوعات آموزش:
آشنایی مقدماتی با برنامه‌ی بله
آشنایی مقدماتی با اینستاگرام
وصل کردن فیلترشکن
ارسال لوکیشن
تماس تصویری
ویرایش متن تو واتساپ و بله
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69464" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69463">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda203069a.mp4?token=AxyIK4NPDFBwP96FOlkFHCZIJHwQ70sAy45fFf-uRTH5U23Obyl_RzvY_4N3mYo8hujLtZSEjX-i1sZMQ3279IPuYaS2UDklq7nGnEaCRMyn2RqZ4ifyLKmZOHc-zhZzxzJ1bXrWwUvQcf2U2d-683k2ZPo123R1USoRiwz9Bafsau2-IOnWjShX0i6DLQgtwH7AmjdnUZTpnFE6X9x4RNI4dmrRLdRXstyUkKlo622wpkfLkCC-Cx5AKOrhllEos2IjC_Qt6qHCZS0IDzbJu_1gtUoqqYKXNDhnDxM0e-TpCaLzqXXKSVp9NQzdwAyR64rqHSwRbR7iYJVa1rNQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda203069a.mp4?token=AxyIK4NPDFBwP96FOlkFHCZIJHwQ70sAy45fFf-uRTH5U23Obyl_RzvY_4N3mYo8hujLtZSEjX-i1sZMQ3279IPuYaS2UDklq7nGnEaCRMyn2RqZ4ifyLKmZOHc-zhZzxzJ1bXrWwUvQcf2U2d-683k2ZPo123R1USoRiwz9Bafsau2-IOnWjShX0i6DLQgtwH7AmjdnUZTpnFE6X9x4RNI4dmrRLdRXstyUkKlo622wpkfLkCC-Cx5AKOrhllEos2IjC_Qt6qHCZS0IDzbJu_1gtUoqqYKXNDhnDxM0e-TpCaLzqXXKSVp9NQzdwAyR64rqHSwRbR7iYJVa1rNQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
میزان شانس بقای جمهوری اسلامی از زبان مراد ویسی:
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69463" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69462">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b293a286.mp4?token=PP7gJd9z7NFc9EFJMGZdKV2HeeMFkrX9iFOdiLEtIfx-3Mnw5TVPYkR9eFOr6B3EUby-Y_VZkkYZI89KHUbEXWWWDMCwDRHMH11WAaZCYm1HG2htgOMb_pA6nAUg8ncSJ6Hfw9hpUh4bgJTHl9uUV4AieSKnw-hKCT-vYOluc1-4JmP5-xUzW1cUEI9W4Dgjcj1rawAyPJbdcZr3oafmJcGGhkEsMd7EF7fgu0_l5updYc3fRPR8OFpzmlddfcfk6nTP9EPaYqfvz8jL5qrroVudhhwX8CGnWt_m1fo8HSLNt4IRnA8bVE6c4RV9SIj1StJ_6A6F-lOUOInoRcPzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b293a286.mp4?token=PP7gJd9z7NFc9EFJMGZdKV2HeeMFkrX9iFOdiLEtIfx-3Mnw5TVPYkR9eFOr6B3EUby-Y_VZkkYZI89KHUbEXWWWDMCwDRHMH11WAaZCYm1HG2htgOMb_pA6nAUg8ncSJ6Hfw9hpUh4bgJTHl9uUV4AieSKnw-hKCT-vYOluc1-4JmP5-xUzW1cUEI9W4Dgjcj1rawAyPJbdcZr3oafmJcGGhkEsMd7EF7fgu0_l5updYc3fRPR8OFpzmlddfcfk6nTP9EPaYqfvz8jL5qrroVudhhwX8CGnWt_m1fo8HSLNt4IRnA8bVE6c4RV9SIj1StJ_6A6F-lOUOInoRcPzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعترافات عبدالباری عطوان (تحلیلگر سرشناس جهان عرب) رو شنیدید؟ کسی که همیشه به مواضع خاصش معروف بوده، حالا لب به اعتراف باز کرده و از کابوس کشورهای عربی پرده برداشته!
عطوان در تحلیل اخیرش (مارس 2026 )به صراحت میگه:
اگر پسر شاه (شاهزاده رضا پهلوی) به ایران برگرده، با توجه به اتحاد استراتژیکی که با اسرائیل خواهد داشت ،ایران به چنان قدرتی تبدیل میشه که تمام کشورهای عربی منطقه باید جلوی عظمتش زانو بزنند و عملاً به نوکرهای ایران تبدیل میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69462" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
