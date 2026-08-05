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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 15:51:59</div>
<hr>

<div class="tg-post" id="msg-69574">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd7b_blE597c9V18S60V6KV18xaU2tgBsAhcL1z7icMSs-GIV1gfKogNqtbAHYj6JcFof4Gv21k_OWNiLjpHFIhfeZT7MDWTf7XXCOikGYEJ44tcSigW2b-dxVyqfmNwz229h2338vSfbH5Gcq1xSNTnYctxWV5ozx3U1Pt2hPMsV8OKykWuyYwGlc8kIzbF-qCm4WyRxDmace9hy3bOg8_rwZcM6HNfZ1Fg8Y62YneND2LnFdKuuUWYm15iJsIjiMd_sTRnob_GKfSgsOdvzjcR9AFpK_eJMsnPzmmBC-2iAK4q-3wRiZiyOTCX4PvZhXR4fvn7Uze5wNQRxP78fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💢
📉
قیمت نفت با کاهش های پی در پی به ۷۶ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/news_hut/69574" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69571">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/news_hut/69571" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69570">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF5vycuiAZPED40pdet7bBmTMcJXa81xLU0ujb_9OwYuw2l18RVpAJTw3pGWBAOW_vS6DDym5AsCa7z4yPc5xtuSv3EkFeRK__zSEjx6Y1zXuH4xlJH3lv5B-cfeYj5CMlOmdjHKTE2y7Z7tp6sn4Ab85K63Q1DOcZjJyWISB05dTR4w657y5-o59d9usF05uVyvptI5fJzZdAHaGUEgw3ywo7OJZ_CLnkyXGRbFk7m_jDpX2uXWckpiYG-ZkLyVKM8p7hbyWUJp9LWNT5clGI-ZC9SmC4fEaR9BT0uc3vjEjdfpNn-K1HCU-SW_zbfAiQGCLgqQ6xsrohkVS6ICZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دسته‌ جدیدی از سوخت رسان ها برای مذاکره وارد اسرائیل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/69570" target="_blank">📅 14:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69569">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db3cnonA-aY3BBQ-RTrETMfG_Pb2Z2pS4P6NAkg2UrswauH9cakLKHhJSf2L4DsoJmXIMt7Ws8y0Yck9jCroTPb1nPvPTxeBKfQozhhGSX6FUj2WMzAKmAhSUGlLWyXZuVp8B-g1ooH34eRX8VppN77TvYAh13dwNSe4cw2ds9xwNNF6DtyX3ROcTD1Ao1-6m03qggxuDdAy5btdZ9n06aW_ieldvBYoduR0IO_qDwjFjEHHewjP1Xz0pwoBj4p-_qoHM7GylzY8M5JDgksTMZChzCjaPzL4rW3q5yJJAGCDl5iLbdml46geB170ySNLIE9QMT5ybOlZHkLVi2Z19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
❌
حمله هوایی ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/69569" target="_blank">📅 13:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69568">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69568" target="_blank">📅 13:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69567">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phgihB6RglSJEha4QerpHlyF7p4wA69xQj7mxULcANw9pyKATSBWbsUgQDwymmPuLRNMWL5WCUfIUW0h1zdefrJSnIIv3TDs4BbCNiryvZqhaBPnyVfCQNlfK4ZZ2SRLDAcO36FoG5lw1NeKFbaYhmSsF7QxGb9DR-ZKxWx5JAz3NdRi7cvjrvaD-7Bab_8yT2FLsfqa7cXx-woF7M0ooZCWF01otCxDTjBTjD2d05lFirweHToUSNCEffFaFxu-1XivNwfR6yEl9UWc4oj333htIwmiuiHW2wLdOPgJx1Fp6C9nGemcqBoIVKsHiW2QAXZzqSBpvu9X5JJYlMTfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دونالد ترامپ تصویری با هوش مصنوعی از خود منتشر کرد که در آن با لباس نظامی در کنار ژنرال پتن و ژنرال مک‌آرتور دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/69567" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69566">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69566" target="_blank">📅 12:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69565">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69565" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69564">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69564" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69563">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/69563" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69562">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69562" target="_blank">📅 11:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69561">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69561" target="_blank">📅 11:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69559">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69559" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69558">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69558" target="_blank">📅 10:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69557">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69557" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69556">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69556" target="_blank">📅 09:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69555">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69555" target="_blank">📅 09:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69554">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69554" target="_blank">📅 02:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69553">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش پر حاشیه در آستانه پرسپولیسی شدددددن  https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69553" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69552">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8GjKeDsmjXIxxnFEomLQ-5ykilfp_a4WJNOuAWdP4ngAIGHJEa0qn9za8M7x84s7oL2IlSu7tBjrrpDRPc_smDrH3TrezIqKVeX53XNdz3c05f14jfzDxxTfc73WJwBgXTFimdqZ0PlTi39if4ml8ed2PAFMcYhl4QeP33wAoxbSNkfIINRdsGaSHRv43Lzp6UwAFd4h2ELbfvScTj7pEe-k8VzaLQw7Q3sD6038gaQcyY5l9-IIMgIiDXmkddy9mYswHIGvk-QHBXxIG3lBG55YDXpKAlcrGPU8hWE38EX4cUtrnD1t10ELk1po6-3pkfIoBWeHAbnzA_1tZQ7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و پرسپولیس هنوز هم شانس رسیدن به هم را دارند!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69552" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69551">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjhTbHSzWrpmmcqdvLYpogz5smzlz4xVlqJArkjTZPcDxOk0AGcVth3XAUyPA_M94LfNyPLNZHG17AqZrJwW0gVWyZesVHOeoeIVjpK1mzgrcjm2fGN02eQ2-WyVSNy1lZY_0ZDsGrzMdQ9q1ZwZNq3hoaaBx3EgcuV_HZ1jTs-uvbunrsTv4PD44sXKOmmgYTGYhr7OghcHFehqGjulNt8rRJNJFdZRsr4TiI0BFinwaHGr3TSncbf-G1qZPTv7z0z_LlrmYcnck8ZFosvZjEdKWwV53D2euDaZxS09pZoE0sCemtNi9oGZywXtFLCHhvKQ-g5bKElrnHwrtxJPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیزارم اینو یادتون بره
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69551" target="_blank">📅 02:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69548">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69548" target="_blank">📅 01:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69547">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69547" target="_blank">📅 01:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69546">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKNadVKoMJvUOBHv1cdMsdv45_D4I4Db54hi7DvcmuqGrfz32sWoxNzS6yvCsvTXAhC_CWOo6lx9-xVZ3n21RYj81Ehpy_Ah2D7LixZ2aUpaXQ8u5ybZ-9Lk_4NtbpN8C-uVvZmlUXUozhUFWnzVcQlXpundYy8fHkvO_4W-sb2mnqurQQhzSpcC-ZUSXbpgC0DZwUdth5VaSatZsTd5nukTjt2qSntXShh8h8SfG5e2ie0a1tlbinczIFsh2lJe5xyVaXHiBlk0H71n36YuX4-H_Qa2IznzxoHDYolJK7h7bSmRnRZKKTtosE4dhIAXULB4G81dUFybIo21I8VauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
بازگشت غول‌های سوخت‌رسان؛ بزرگ‌ترین آرایش هوایی آمریکا از زمان جنگ خلیج فارس ۱۹۹۱.
پس از پایان جنگ جهانی دوم، جنگ خلیج فارس در سال ۱۹۹۱ با استقرار حدود ۳۰۲ فروند هواپیمای سوخت‌رسان، بزرگ‌ترین تجمع هواپیماهای سوخت‌رسان در یک عملیات نظامی به‌شمار می‌رود.
اکنون نیز در سال ۲۰۲۶، با استقرار حدود ۱۹۳ فروند هواپیمای سوخت‌رسان در منطقه برای پشتیبانی از عملیات علیه جمهوری اسلامی، یکی از بزرگ‌ترین تجمع‌های سوخت‌رسان‌های نظامی از زمان جنگ ۱۹۹۱ شکل گرفته است؛ آرایشی که در بیش از سه دهه اخیر کم‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69546" target="_blank">📅 01:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69545">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOtVA9SXgZTpcKpebpq70qLfnxzJA0h8cM3UwMLFDmmHJMuNOOidUGelnvwOrma2uzCU588e_i9WKNtoYTUiTwcLKeA5P56f13zUGf6KE_xQYa2FMf8QaCZUFFV3XBy4pvnkNYpM2tXkNu5hMBYvEVipIRD8O_rDXCZvMcMtalhZ0FiIdyCMK7K9AMK3-33r08MiJ40TtWZts1q9y1SYS0aQgrYPwkPFRoVfMLesjrAuXcLwf5qfWzHGLQyZJ3HfA0FSTzPEK_OKpmTnvPPTne8J17zTibrD4p-HWp69drIthbciroHkhDy5zp2PKDOVk5AGRefPn6HU87Z9QYCMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:مسیر جنوبی از طریق تنگه هرمز برای تمامی شناورهای تجاری که قصد عبور از این آبراه بین‌المللی را دارند، همچنان آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی علی‌رغم اقدامات خصمانه و بی‌دلیل ایران، به بیش از ۱۰۰۰ شناور برای عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند و این ترددها همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69545" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69544">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69544" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69541">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69541" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqlQULPdVJ2g7uzSiDnzDZHk3mWOiJgitPtBC62RbrL-hnoQ_NnKOx0ktKqSv02HHmiLPCBkIjpo6UtaZAw1jB1_Phls2W44yOKTFZ7KIrxq45-8XrEYzITOOMLds6Jpr5hnmMEFEpAaA8eHnmEUqxpbPZbhgWqUg26im84LAaAixIzfg9MnBqS5fRlpgSmZRlazHtb0W-pwJwT8ilr8ittgW9crOMSsbN53HaNXnTZUYFTNMMawQeEGxiwd2i-sZAoIsJeXJZ-szUKzqonLLXsawNJrTKLfBMqw-y-zj9KM_C0Dm72cvZKg_ecKANn_n4y67wCZpbgX73holZQB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
نقاشی وایرال شده از زمان قاجار:
در زمان قاجار زنان روی یک وسیله تاب مانند میشستن و یک زن قدرتمند، اونارو بالا و پایین میکرد.
شاه یا یکی از سران مملکت هم اون پایین دراز می‌کشیدن تا زن انقد روی آلتش فرود می آمد و بالا می‌رفت، تا ارضا میشد!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69540" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69539">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69539" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69538">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69538" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69537">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69537" target="_blank">📅 21:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjVzAoFY2fxI5XqLi5wBFKNJhhZ_NZXUDNJC99bCXvmKLkRNI7ghGf6TuJZ_3f1L-SmoakjKhf88l5NjrvSjhMUuQ30gnb6RqdP4dvHQQmhZP6fJ6ELMnlgfSuG6AruxlmZTLpJ9qPjDXvHvE9w9DvcXtszw58D6k9boIFjKXa1pxD20eyyyT3kXWHAVliTZ1f_eOazPMVzSQeLWXTYkZVUI9sQAj4q1QUJWpKCIp1wxWnRPn6uMJG96IFq5O_eQGm6Jr5ZCAkLvo5_PKgmGHKO7etofYNyNtwHJDG4pb1SJs3RE1FOv0r5Ko0W22qWrU-QRy63LGiSRWKWKoSlQZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال‌استریت ژورنال: در حالی که دولت ترامپ بر نزدیک بودن احتمال دستیابی به توافق تأکید داشت، وقوع حمله‌ای جدید به یک کشتی در حال عبور از تنگه هرمز و بروز اختلاف بر سر مسئله عوارض در جریان مذاکرات برای بازگشایی این آبراه، چشم‌انداز این کریدور حیاتی انرژی را با ابهام مواجه کرد.
به گفته میانجی‌گران منطقه‌ای، بر اساس پیشنهادی که هم‌اکنون در دست بررسی است، کشتی‌های عازم خلیج فارس از مسیر آب‌های ایران وارد می‌شوند، در حالی که شناورهای خروجی از خلیج بدون پرداخت عوارض از آب‌های عمان عبور خواهند کرد.
میانجی‌گران اظهار داشتند که اگرچه دیپلمات‌های ایرانی در ابتدا از این پیشنهاد استقبال کردند (زیرا تا حدی کنترل بر تنگه را حفظ می‌کرد)، اما تهران خواستار حق دریافت عوارض ــ که احتمالاً با عمان تقسیم شود ــ و همچنین دریافت تضمین‌هایی در برابر حملات مجدد، پایان محاصره دریایی آمریکا و کاهش تحریم‌های نفتی شده است.
مقامات ارشد منطقه‌ای اعلام کردند که آمریکا و دولت‌های منطقه با درخواست دریافت عوارض مخالفت کرده و خواهان تضمین‌هایی هستند مبنی بر اینکه ایران و نیروهای نیابتی‌اش، قلمرو آن‌ها را تهدید نخواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69536" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtTBqr9Y7cJXGgnVFOy8H_sdB1-MaofDDq0z1SwI483rFyFyZyGAeGjC_d5p84ZkzcHdEGScrn-WzoPYHlFBthgEB0nXQPZuKkqCw5ZJ4eWeuAFPfzWUkDONwYtVTlHjqHYjrVJII7ScgQZZUWW10aH3KabXyAAmlCxclaKUdNbmqJJSP9bjqimh1jErv5tBkbsGX0dZFLoaSqYc1qZvfaQOYuI27pJNbhqD_J22mafhFP75zdSTpOVQz8gu66UStk3a5UkuSH5ZMM3ZP-A_1WGuqtkvzJOvyqGvAx-RJKTKUT4lT--Vl1EzzWLCIaUeXZ1TDre6SzwB7XwEciiGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:یک ملوان نیروی دریایی ایالات متحده در «مرکز اطلاعات رزمی» ناو «یو‌اس‌اس باکسر» (LHD 4) مشغول نگهبانی است؛
😃
این ناو تهاجمی-آبی‌خاکی در حالی که از محاصره اعمال‌شده توسط آمریکا علیه ایران پشتیبانی می‌کند، در آب‌های منطقه در حال حرکت است.
تا تاریخ ۴ اوت، نیروهای آمریکایی مسیر ۴۵ کشتی تجاری را تغییر داده، ۲ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی دیگر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69535" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69534">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69534" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjfXYc2aFoa5GTdVfNwR7ObAE46CHFE3E8NzVK_FV71P5r6B2PUKmDx1HyBbn5F_SIbiXm7Ps77yX7S1670shZg8dS5RRVoty6kYVsnxaVgVlWztsh7t7-pddX8EYZkTFp-7yDjoCavZ-wDOuxrY9WUt_9fweEpnzu_eHg4Ol3Wdn_9TmtMaPMSCt6Tok_n0xCgILrfJsfu5sjWacf09-utCWzRNswQTPAmVjuSUWyJK9HNbwY2H5_6vRHUIAixOFvKfYXezjUbSmRVrpLl7DPNfB7DhSrISobfiwxfZnj6ZK1XKxIH1MOTEl3LihVsIeLwFK0_81SscnjhJ-Xz6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ایران در حال بررسی امکان مشارکت کشورهای اروپایی در عملیات مین‌روبی در تنگه هرمز است؛ اقدامی که نشان‌دهنده احتمال تعدیل موضع پیشین این کشور بوده و می‌تواند به تلاش‌ها برای ازسرگیری کشتیرانی و پیشبرد مذاکرات با ایالات متحده کمک کند.
تهران پیش‌تر به‌طور علنی با هرگونه نقش‌آفرینی خارجی در مین‌روبی این آبراه راهبردی مخالفت کرده بود، اما در هفته‌های اخیر و در چارچوب گفتگوهای گسترده‌تر پیرامون عادی‌سازی تردد دریایی و کاهش تنش‌ها، انعطاف‌پذیری بیشتری از خود نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69533" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69532">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69532" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69531">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69531" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOpZpz9yUylj63XPoSv_du-T-h_yEzyctl4rWngRAUMhGZZysqeKo4YstryJOsgWzIKiI1s3UtDql0R_nJ8qya1hG3LdCweJxqzl4GvQdLNq4OvtqKJg6GgCvQLb5WatKzCC4A5qD4JPLrKQtlQyPgpthlx3MwerGYFzq0bf7Z2swXCtV-W0_We5ICPhFBM8d64GXBwcKiaqxazCe5F-oe-hZJVm5tINOk0_CsbSAAYpFquIWibsQZnoaHXDAvq_ZIquuFZjsCGoSs6SmnpUNQISHLQv_WVpuIQQdrJQjSi3SYgQ8gzp6NRZv3uE89nILIwcDgq-12x-T2tCc-xtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXMkwvwuoXnsmVJNtX12EZdOXjrTkUraWa7yqCMiLVlKpYksZbf1nDiSkWsSeHuqK0GnJQ1WLUtRoRyZf3G9DlY_xtfj2ib2xSlmB8g4DtAJYTyFUwG3vbYcKoaBvWF4B4f7-p7CZRK0ggT64KF6-PTlZvKStyEWn2Sex7C5WfzK5bIC6_MI493bHM3SOQzWzZr2cAjoDnscY1iY5LUe1GtHxd6pl7sTVximOB2N61u8BPD4pNbhBJHiKL5pDJb5jSzpmE35uEcWk8kR2DqDwxTyS06OFjh9ybN_rNAk8y90NJz7zaESyCRqwHGITO_CfVScHHuX_1G4rAuLDOvf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n102PQDjXdB4hrvgcjdjmEMZP8ZaxFTr-e4P4AAwbDmq4qhZqV-x3Ba7-I26FcuqUaF-ruMvR91rchDI6IMKbdd9BNm7DUTIMc1oHH8UKIJbbkaO5QYaJHpBGTluGC3P_WJRD_vuoZmM-Zn4_JbBfVfo_00UYU0eCdkE72OSTXikwFUoCZf3868fCm6LdEvWcuU1myq22fScEuWVFu3-dcvCbQ6iksQifLaEzoMe7vawHbjwHz9uyDSnoiTNPrcKAkqhgsJIaTK39M4Tn-7JUyMd7oo3sDO9pHzNJmVt11bt50KJOO180vRDDN4COZQIEwa5Nd_AygynRBQq8hQt0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=fkFkkwgg2rALSVtjHpBqI_xdiKI3GnNSDIZDWiW6p7KdS-yGNPvywHo03pxYqGEU7IBhH3C_OVjWcEcTmtSuwJR_H5Gw4mfuMsBvy458e5RmINnV2Ac5_Md0GJdVZZp1Pn95DoHr_c1srYGTqzKWVBtilwKiS5qXqzQOdMV5snh1XOzRuTMeHl4dLSk2lkZ_O12AqcSHerLNpw7BK1cqs6mQ3FWTLq6mwt2AItKjWIvI0og64WowdMf4JLF0uwjPK4QR-ieGqUyza2ZcvE7K4OoroRWzkruQEaH7S56nstu2se9VHRikZQhSNfJcRKEMff9WmcGX4PZER3Di_JpdxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=fkFkkwgg2rALSVtjHpBqI_xdiKI3GnNSDIZDWiW6p7KdS-yGNPvywHo03pxYqGEU7IBhH3C_OVjWcEcTmtSuwJR_H5Gw4mfuMsBvy458e5RmINnV2Ac5_Md0GJdVZZp1Pn95DoHr_c1srYGTqzKWVBtilwKiS5qXqzQOdMV5snh1XOzRuTMeHl4dLSk2lkZ_O12AqcSHerLNpw7BK1cqs6mQ3FWTLq6mwt2AItKjWIvI0og64WowdMf4JLF0uwjPK4QR-ieGqUyza2ZcvE7K4OoroRWzkruQEaH7S56nstu2se9VHRikZQhSNfJcRKEMff9WmcGX4PZER3Di_JpdxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgolDIltu3lL4aM-QaBRcNUwo9nad0-qhOJb7uhGJEqPC9cIQdQWxH4HTj7YubD-Llo-RGMned7JaBa_9gvlw0E2gVDqti8oIDqCb5XULasQofC5RSPxHK2jL0tsC04z-1MN5z3_50jWsi6k3OUCqRbCp_qyFhqZJZxOWJHUMbOArqhQiBzLxGG1XsXHHQMnEtTM_N9UMFiMF2fVjMejfaZp5TrES_WOCvFNucAKykU_uU3GKEeLKNwb2c8vt8kBzBPrYufZIbtQLXrB_Pr9L0H6QGulOsW2-q7JABEEqY1BxexLNHkkwgoSNP6ax4aOtZE_VIn-NiBRf1zcjFtRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USFkPl9e1aarhpWaGz-EdoNRS1fs1-cZCKTx0pSXsvfJvsiexog5fECanyO2zRwbL4VFCDm1r67qDGHjGoKqWIpE2OYBUVdqJnB_MDf0gXQhLq2500aIkmqdxURS__S4mhvyxWmf3RhQ75eErpS5eHviOUQFdSNpTFW3S2wnWwrk1KZiW-q9wlfV4uOf_6krLrI3fDljL7QKnNgSqsTiEANNMlEPhPbI6uVLZJ2DyVheswl8cVxCHUvaVE6OJmn2atNfygtp0lzD-OubycXF8I73_PlwpY1kZe1tFGVaGEKg_tK4kIU_zOgCiifcDBVXgP5qvyk6SKagFAo9U92frw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNtRjr_bO7l92dtIFiik41gU3b3pruClDuC2y7fxM55P0jqNviXv_EUChtsKE325J54UHiIzGSBRKrzrNFbce9iZFXxD9dV4c2GsUwhjcQAnBYBylJoUrdqqI5TCYs3rokdyXSwhC2OIR_yunQog-DqjEjWEqtz7Wco8TxTZzgp3JDGB2DcBDw8N8nKYu7pJxVE7AlkBYf9raSk9GOhAba8ErP76oElO5EXYd88yIY233Hsue0jNnqqfkHuWM4TSrd6maQHAeqdfv7HpY_sD90m4gQCXJGPlIz5-57_g_ZLr7aJWHKvdJY1r2T3kSyXmVJmRVY2H4OD7bMEtGVtAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5EfNKhA7gCkJ3-yyJAMdPd6caOXRqjRiqmK3eDP4KIDxr9boSFwSOD5zhcm23T4QpsQCxnHq4p45YkLvec_oQ4JHJyloaBxfgcy6pOjLUCKDsSTl1GNnnYN-lmUtK3fH7kIWcvKDHOU2CmMul52DMafpiFbKOKEMmYaAxcsDmczSsXDr_sk-LfFxwyJzFed-a3KU10RIE-PGo-Vk0JE7W7ceIkFHFbbJl5b6OC1Zu4eNcw7zAj-XWmtgcPYBXUTyyJorQemD1VoE3vx0wioOfZuqodzK9uuYGLksT_F0t2xtuh3ql5ZHpBoT64fEpIjEyPy9_MPgR1nPayd12jrOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/moim6Oo8aqu1rB06QsQAbIzWsnMzkkVA-Ddi5ygD1dSFA-6RtsIwZVd-c1VJstXEWhTbjVUdcupkbBSE7XBXywM7biJEM2PTRBsSd5BoKYBJXnfzez_Xc5SgDVifiBbMdv4N1otGZViJcLW2lBTp0qFu_MP9qc8-bjs0aYX0QIKqV752nWWp-8oq_j0eAT0FNPmiPN8ZRDQ1oBxES_-4CuRCYfTvhWLcR21S3luUKQxrRSwzH8m-d65rvFfOTvk_X0lDfZJlkmATjOUIEZwqexh7eduXPbZC87MCjxBI1JExab_uuMB7A2QXM8oe6TEIp24yjAgJJk6fLRk4OYaeaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=BuLHPC3_EVXr2RAZgeWD3kQlxqGhIHH3MTQZp8z5ltDmCtd4def4sX654UWPj90Z5jNSRz4JTrtS-f1LkPrmI36Lu6ATz6kCPToG2PvMScBVtvpUggZErNHkMNTAJsDwcaAT1klXVLcOomfiGJ2UmNh4ezdW_n_CkWVsRzZKfdiutqXNH_5WT5T0QKy6G8ESyo5zGHNLr6P0BxhYQhgWd_KXAVDEAhrpnXqBmZDgQElRtQKosduHpKKnjKNwzIU2LQw2TzcYR-zS2fcTrwFW389aQH_xzvD0oZy9QTFDGhZKfLqGGmOaAkpK0RfWIQRvHeG1csdjeeM7PtjJQGfHlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=BuLHPC3_EVXr2RAZgeWD3kQlxqGhIHH3MTQZp8z5ltDmCtd4def4sX654UWPj90Z5jNSRz4JTrtS-f1LkPrmI36Lu6ATz6kCPToG2PvMScBVtvpUggZErNHkMNTAJsDwcaAT1klXVLcOomfiGJ2UmNh4ezdW_n_CkWVsRzZKfdiutqXNH_5WT5T0QKy6G8ESyo5zGHNLr6P0BxhYQhgWd_KXAVDEAhrpnXqBmZDgQElRtQKosduHpKKnjKNwzIU2LQw2TzcYR-zS2fcTrwFW389aQH_xzvD0oZy9QTFDGhZKfLqGGmOaAkpK0RfWIQRvHeG1csdjeeM7PtjJQGfHlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=biadxFrFUMpjyQcUFsc8hXmYVELxajDN5-TNTdcPogVgMTif-4g77KOhERRwVHQ9cVNDSV57X6ZRVe1din7hAO-Y7MLTk_gIPgLI-_6zG7GUuDv3oC4_2hTu7_eyD9dgdXRAGZ47WyvKI8rcUkiiT86IPFvZoHJ74bSvN209ztFKJPKIHeg0oxxeGDEOsq3etXN-GtS8wS-L6bF8ws3Ae3Uxxj66bx4WxeCx0SEmAPy27inkf4FJ-vHYcIoBL9Au9qpHoTFW9RQHpRrxM31CkQBMX5bXoUHJt1Bk2dVUjmD3gFO2YY98IEu0C5ROYoDBLCkbb0OQ4JtCpZoUUmWmkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=biadxFrFUMpjyQcUFsc8hXmYVELxajDN5-TNTdcPogVgMTif-4g77KOhERRwVHQ9cVNDSV57X6ZRVe1din7hAO-Y7MLTk_gIPgLI-_6zG7GUuDv3oC4_2hTu7_eyD9dgdXRAGZ47WyvKI8rcUkiiT86IPFvZoHJ74bSvN209ztFKJPKIHeg0oxxeGDEOsq3etXN-GtS8wS-L6bF8ws3Ae3Uxxj66bx4WxeCx0SEmAPy27inkf4FJ-vHYcIoBL9Au9qpHoTFW9RQHpRrxM31CkQBMX5bXoUHJt1Bk2dVUjmD3gFO2YY98IEu0C5ROYoDBLCkbb0OQ4JtCpZoUUmWmkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=NWhx5AkS7jIlkdJMZpv3DMRkdvL1Syar6mMvdL79uu2KaFzVdCueFsu0GFyvqGulC91h5jl0beQflov_Bena2mOJngfgyXoll9A7tHYxlXYRi0bwEqHwQtJ9jAv3RrXcNtQMmH7mYoGONn1FOKXAcchdyqJv8v_6VRbqBJaL6ah3LAlaNWhrWblAOPPlmtwDOGY99GBO5W7mrf8vkz3PhdzksdEk3zbYr36JaXJemF1x4qoCxOaSAo2_c8X3wlnb2ON9bxJyZcqabYOWTj9m3AQ0a2UGDm6Rcyw7_w_sje7QUlKt4jr8Q3yJWltYfHqFFW4JRJAzH9ArOnpJGSsx5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=NWhx5AkS7jIlkdJMZpv3DMRkdvL1Syar6mMvdL79uu2KaFzVdCueFsu0GFyvqGulC91h5jl0beQflov_Bena2mOJngfgyXoll9A7tHYxlXYRi0bwEqHwQtJ9jAv3RrXcNtQMmH7mYoGONn1FOKXAcchdyqJv8v_6VRbqBJaL6ah3LAlaNWhrWblAOPPlmtwDOGY99GBO5W7mrf8vkz3PhdzksdEk3zbYr36JaXJemF1x4qoCxOaSAo2_c8X3wlnb2ON9bxJyZcqabYOWTj9m3AQ0a2UGDm6Rcyw7_w_sje7QUlKt4jr8Q3yJWltYfHqFFW4JRJAzH9ArOnpJGSsx5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuydkwACQnaIda5O4dQUXAfQ72_-qJR_VKKOEnQCDHFZ4yi3fQZ8JOmBcP8YOUrrBxpbooJ6H6B6YMmu14dAPW9DUkdwg6-Lhg4hbArziXE-HUqrkFFOUF0hyhWd9rgJSVPOLOcXeX8oAtbIL9zk4Po9FjEuzyTBHV5VIS1oP6StzRbQLdOMLiceMYvijJwvwqeEfFH-LbIRfSdX2qgkX5rgagKeuUM0j741D_OKlRrCiIU_VvNur_73nde20MmsDElM9xL4qkLGl67__A6HVqCCCwpFTbFlM_la-bgHwhEYRsU1sUgzNxDM_AsStBYeG8AdrM8TQG_Tgl5A1vRNbUZo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuydkwACQnaIda5O4dQUXAfQ72_-qJR_VKKOEnQCDHFZ4yi3fQZ8JOmBcP8YOUrrBxpbooJ6H6B6YMmu14dAPW9DUkdwg6-Lhg4hbArziXE-HUqrkFFOUF0hyhWd9rgJSVPOLOcXeX8oAtbIL9zk4Po9FjEuzyTBHV5VIS1oP6StzRbQLdOMLiceMYvijJwvwqeEfFH-LbIRfSdX2qgkX5rgagKeuUM0j741D_OKlRrCiIU_VvNur_73nde20MmsDElM9xL4qkLGl67__A6HVqCCCwpFTbFlM_la-bgHwhEYRsU1sUgzNxDM_AsStBYeG8AdrM8TQG_Tgl5A1vRNbUZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=io_q781TT-nRx8FVqrXzjxDzo9z22vtfQIMy3DjBUdpCMk2rie8_DrXdNk7xYEIcICVU-OK7jR6PPL7Xjp1GVEuiWPf0Q-TyNKUPekz0w-wNk8nwo3-olDrj23CL2ApHbsAxSzYm8OdV7RDR270Ipbhqm7RWoDLbjTouCRPtqWIahQz2rDGPkcmfcgDwJXbehGcntInWLNo9Xc70XoTavKKM0YQXKYBf8nhohG352DyAA2HNlD_xQ490ZcG6AvwNTjZT9yHlfnMhT-yf3a-HSKB0Rwvxb4_t1YvCTF3GoxRvt53uQd13IOOWz0piEQINZ-hUqQZUywA_qTjMKwp0qqKZVdp3V4XFsD4sNwYgSSZc-glcu_-7pxBFTX2lfXB9sXSaEbssNH-rbYtFXPolWcEjFVfrgfmcIRPfwS8OPwMJ4xabrT9Vj1liCwDZMhylBQQrf5oC42LbizEDIldID5pOOoTRRPgX8pKLkHiEa57dq4ekM6cPwvzzYKpg5bvBzZohPR0Qm0vwOPzQhRgrZZhIrL9UX0KbngDhcekXIeBdnWI1NcSs4__JV1ownMgGdWu_HGE-Miyh6z6GFCzhvCzNign2T1-GkzVy_cmAlC3MclTB9cPClEi7KKO3htENQzZmqVyy22SUi42LQrkuzCo6MXv10HwlwULu5d9Mcrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=io_q781TT-nRx8FVqrXzjxDzo9z22vtfQIMy3DjBUdpCMk2rie8_DrXdNk7xYEIcICVU-OK7jR6PPL7Xjp1GVEuiWPf0Q-TyNKUPekz0w-wNk8nwo3-olDrj23CL2ApHbsAxSzYm8OdV7RDR270Ipbhqm7RWoDLbjTouCRPtqWIahQz2rDGPkcmfcgDwJXbehGcntInWLNo9Xc70XoTavKKM0YQXKYBf8nhohG352DyAA2HNlD_xQ490ZcG6AvwNTjZT9yHlfnMhT-yf3a-HSKB0Rwvxb4_t1YvCTF3GoxRvt53uQd13IOOWz0piEQINZ-hUqQZUywA_qTjMKwp0qqKZVdp3V4XFsD4sNwYgSSZc-glcu_-7pxBFTX2lfXB9sXSaEbssNH-rbYtFXPolWcEjFVfrgfmcIRPfwS8OPwMJ4xabrT9Vj1liCwDZMhylBQQrf5oC42LbizEDIldID5pOOoTRRPgX8pKLkHiEa57dq4ekM6cPwvzzYKpg5bvBzZohPR0Qm0vwOPzQhRgrZZhIrL9UX0KbngDhcekXIeBdnWI1NcSs4__JV1ownMgGdWu_HGE-Miyh6z6GFCzhvCzNign2T1-GkzVy_cmAlC3MclTB9cPClEi7KKO3htENQzZmqVyy22SUi42LQrkuzCo6MXv10HwlwULu5d9Mcrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=iMc7_Eh6WEBmBdcE8fUByLHyJQE1-QAQVDuxBN8pitCLp_DTS0bXEI1ZhCCMAvyk2tq98GHADZbXkLg2ngHc1IUwtv6dFmtwfvIe2NVNV9uiHP3b05NXDqt1l_Phrp1gBAvO1fPcSjmilECE7Q1sXJew5S5oaqopWRV3RQAPa66dcf6jh-YQNqKgU4f8TCSSebOH7p59QYwN7FMQGmHiGPiyEkQDktZBO0gwpOT9Lsy015WwQe7kZUMe0GUVg8E-dh0HIJYYnoD9hdR4N98gG7bKzsOaO5Ga0vNhG0q1U543pJfw2HHpZxUxfo8OYypBR4RQxfxLU0b2MT4aeD-ZqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=iMc7_Eh6WEBmBdcE8fUByLHyJQE1-QAQVDuxBN8pitCLp_DTS0bXEI1ZhCCMAvyk2tq98GHADZbXkLg2ngHc1IUwtv6dFmtwfvIe2NVNV9uiHP3b05NXDqt1l_Phrp1gBAvO1fPcSjmilECE7Q1sXJew5S5oaqopWRV3RQAPa66dcf6jh-YQNqKgU4f8TCSSebOH7p59QYwN7FMQGmHiGPiyEkQDktZBO0gwpOT9Lsy015WwQe7kZUMe0GUVg8E-dh0HIJYYnoD9hdR4N98gG7bKzsOaO5Ga0vNhG0q1U543pJfw2HHpZxUxfo8OYypBR4RQxfxLU0b2MT4aeD-ZqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69503">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqT3W7agHbYQR40AQh7LcRhIsKDK_jN3hrbWUodbEZlg-y1ErSbGv4iT6RQdvdRmNg-d-cRwPrGByqBP1jCv0mxkwHw7TNm-xcK89gaZi4w_PvvLbUwScPmf_YRlKH6jheE3QfjXZaE4gzwTRd2Rx4bcdy8zBDzR-Hc0JisAsT4OURIG2vnBzb80b65eRv6kI92p0Uj7RaMCk2WP-RALuq--i4wRcdJzkYXWKwvhExtgxZxI6VAYcyo_9Nsn0_3VakQ5YYP-5s0Q6eq-Jl4Ec_d8YQQ5M5XWRIsis9Q123WUWFJ741bINPNtccOThEKtR5PkwLWGqEze4v6TSq8Y5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک کشتی باری در فاصله ۲۰ مایل دریایی شمال شرقی «الخصب» عمان، از طریق کانال ۱۶ VHF پیام اضطراری مخابره کرده و مدعی شده است که مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69503" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69502">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های حکومت از حمله به یک پایگاه آمریکایی در شمال کویت خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69502" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69501">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=o-UNHUZHBwkwCZJcDz1LAupdq5lngYXV7XUFU7hL3DN5QmQn8ZE1xM0yvlXj9umg_ZkAMf8ea-Lk1YR_AuDHpN5_Q7RqRvrj5-PcndnPWTkvg0RvP00yMqInyR2oI4ybUBr3MSlHc0m8uiINzrQXHEUYY2cbY1fQA8pkOXp5c7u5nTHetR7ov9DfTPVIGqq4vhmKSNquTJ5tnfVp9QJfzqYkEBrm9PpzUwMUgEF3ErKM_fy_4olnHXhAeUFhm7cgEZdSu5-LfsmWJ4aY3IQ-pZ7jdW8P0tISsoeJftd9RwN12yD3iOLa0kasn_t8g9Kw2n0UBrZRvrWvj1rGLc0g6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=o-UNHUZHBwkwCZJcDz1LAupdq5lngYXV7XUFU7hL3DN5QmQn8ZE1xM0yvlXj9umg_ZkAMf8ea-Lk1YR_AuDHpN5_Q7RqRvrj5-PcndnPWTkvg0RvP00yMqInyR2oI4ybUBr3MSlHc0m8uiINzrQXHEUYY2cbY1fQA8pkOXp5c7u5nTHetR7ov9DfTPVIGqq4vhmKSNquTJ5tnfVp9QJfzqYkEBrm9PpzUwMUgEF3ErKM_fy_4olnHXhAeUFhm7cgEZdSu5-LfsmWJ4aY3IQ-pZ7jdW8P0tISsoeJftd9RwN12yD3iOLa0kasn_t8g9Kw2n0UBrZRvrWvj1rGLc0g6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69501" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69500">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
منابع عربی:
شنیده شدن صدای انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69500" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrMeQrWYVPHg1H9pZOycyB7jNm8xFRGeKDl9aN_XIubH-YoKfmH9clVdhAYkVK_ISCfUnHHmtaRk05m40itXamukKgmmELNHjjWHSRRO6qh9lLaJEIOnKYIfNrkiONZki6l1g4fCOU_7X_hrJiBlQir5yPLfcUJOnkfjKtjuP-vJcIi2uAqlf3ZgDNLQFPGJTg8Mfd4bSwlkUHwOsT1w-mlXV5hyhEdoHIyIYp3kEvswxrF5Wme6i0dgpEvxQ9_YcnQuSTZSqg6u3h5HurXof70t4VVnVy5hmdirkt3AqH2RHNjiVSweSIO5UlttwHV8u3OxrRcM16yLSTYusXH-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=Mw1umMwi-aM2DRbeYkLcGCBSj0lfGBpeckT2dudT4uL-vxQU2kVj3OONS32evK9Htf61ko3gtatl4ZMmleh3xx67jwax9ZspB2CSy9HqvBWpfr6fWQP7AhSSYhsrcyh9i8pHItvKXUsxAPTg7oJk3zFrJSt09wAkHwXVoHisprTxcQqA1Rx3dmUcM2MKtT4zG_RgHgC-347fGAUsnA7mkuNkeF6xWgnvYi3nZkXMTFfkOHvaE69dYotg6aMUnjBeN6StgscZ5huDKTAEp-J41ypr33SeHsG0fEz2ZeL4WmhSsG12Ap8S1ja0i_4qAeAGxqKD6RfhsbJd43JSU7nG2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=Mw1umMwi-aM2DRbeYkLcGCBSj0lfGBpeckT2dudT4uL-vxQU2kVj3OONS32evK9Htf61ko3gtatl4ZMmleh3xx67jwax9ZspB2CSy9HqvBWpfr6fWQP7AhSSYhsrcyh9i8pHItvKXUsxAPTg7oJk3zFrJSt09wAkHwXVoHisprTxcQqA1Rx3dmUcM2MKtT4zG_RgHgC-347fGAUsnA7mkuNkeF6xWgnvYi3nZkXMTFfkOHvaE69dYotg6aMUnjBeN6StgscZ5huDKTAEp-J41ypr33SeHsG0fEz2ZeL4WmhSsG12Ap8S1ja0i_4qAeAGxqKD6RfhsbJd43JSU7nG2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b93335655.mp4?token=o-FxR0eJ6ajUarTsS-Jpxh8rumSCzOk5gW2hu1UIO0a08wZu1xAC1NWkelY1GJZXwq4648WJVGpkjqV1RgVKckOYjeKXG6iSHVxGBLBtnCQpecb-2VFGfLj3u3oAmdCk9iisKqNOsDshkBvEYbrFFLxzYBT3DIGwf8rDvVc7LqGCRTjTKfV997Y_liQi7goln7tvcpo_4gqKxTdmc8n5ADoGrQW2W8I90s3b4wRI2fU1_5Vf3qAonOfQtFZRbyrB8lA_r_pjfzM5sxlGnQExiJ1O9KXT6KWK2hlFUXayEd7IqORIEtXOlj7QjiFjornnaytUHCmH9jMPMz4K0aI7DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b93335655.mp4?token=o-FxR0eJ6ajUarTsS-Jpxh8rumSCzOk5gW2hu1UIO0a08wZu1xAC1NWkelY1GJZXwq4648WJVGpkjqV1RgVKckOYjeKXG6iSHVxGBLBtnCQpecb-2VFGfLj3u3oAmdCk9iisKqNOsDshkBvEYbrFFLxzYBT3DIGwf8rDvVc7LqGCRTjTKfV997Y_liQi7goln7tvcpo_4gqKxTdmc8n5ADoGrQW2W8I90s3b4wRI2fU1_5Vf3qAonOfQtFZRbyrB8lA_r_pjfzM5sxlGnQExiJ1O9KXT6KWK2hlFUXayEd7IqORIEtXOlj7QjiFjornnaytUHCmH9jMPMz4K0aI7DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دست فرمون پشم ریزون اوپراتور اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69495" target="_blank">📅 00:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69494">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnHjeHFraw8ePwBAw_ZxjS8sTaAJMP96gKTygrFqLfvTITtc6G45Ox_SyTSlGiWyE0H98AJ4xwf3AYWscYHTpWBugFMuxMs1GJ9vIeaUjwI_cI_DvR1ETnF1p0EHqhqvyLVRIkEi3WohqnQ1bI0zQlX_6msjPHw21aiLGDoh6cBxBmVovG9LdJBoItMx7IWwJLB2GZyvU45TrOQ_G8-cVIw8jKWUbMdBfneYkebWyql_g9swWCbrWcsYmBVTTTuouulpApUQatYoctEWwbHrtXqzBzHxG9uqZtfbdJVn7AvW5FKrptUrqLQeiNqmcZbhLOUqVxH9tfNTUTmPOyIDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
ایران هیچ‌گونه قصدی برای مذاکره با رژیم ترامپ ندارد. هرگونه اقدام تجاوزکارانه با پاسخی کوبنده و قاطع از سوی جمهوری اسلامی مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69494" target="_blank">📅 00:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69493">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=mut7w5Dnke-fRWs8H5JALHcsEBkUs4G0dV4HF_fv7NBDQJBz0sPHkHV2q-lHunbI5LDDR8WAO2_ePbSzYNc0GDdS3vCJMcIyKkVaOfpD6fioKfLxHn-TkmzgOT78dzh6S9m1966aJ-W-jsOKykwXms5nPjdi2aKqDpQQ6HHfapU7u0TZN7LWxEkYuNjEt10Z03Z5jMdjR9BvF7JHtMXYwOYWJcruMqce20_XpK6W0yGmq0GsRhIvU68EtRoR1f9UOLWRt2852HPy6tnalsOs8Dm2qa7x2DKj3PHRVlXBwE2ApmecrSpLF4IsgazaJzEhh0k-BNB2rU7cGHnLML2WcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=mut7w5Dnke-fRWs8H5JALHcsEBkUs4G0dV4HF_fv7NBDQJBz0sPHkHV2q-lHunbI5LDDR8WAO2_ePbSzYNc0GDdS3vCJMcIyKkVaOfpD6fioKfLxHn-TkmzgOT78dzh6S9m1966aJ-W-jsOKykwXms5nPjdi2aKqDpQQ6HHfapU7u0TZN7LWxEkYuNjEt10Z03Z5jMdjR9BvF7JHtMXYwOYWJcruMqce20_XpK6W0yGmq0GsRhIvU68EtRoR1f9UOLWRt2852HPy6tnalsOs8Dm2qa7x2DKj3PHRVlXBwE2ApmecrSpLF4IsgazaJzEhh0k-BNB2rU7cGHnLML2WcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571743cf02.mp4?token=PNjbU3ufQ90wEHb-pzCB_5XYltSNF_1-6cXPNx5iIZYYzNqFkvxr1dMgppPLJPAXzUlU7slBUTlSzi7o4nEvrq0gY-mRP2M5FD_4KrpBgzFw8iqd0BQJQRnAk-4cbrlZQEfA6a1yuCTiaVbk0L7uft3GJ6Bqj3-tAJscm0MezjYCGSKv3Ju1cXW0AjiuxnQR1yhC5IzuSslKalT2qqhMXGDF0J0CsYhiJmLwiP--HnPkjrLU1RxzhSOjb2OC46h-8pQ7lRwcMGzJ8gMek0g9KsRQTeP76AECgILpCBucaRBJqQdOdExfuxA-wyS_V584pDwqWyVHnbV8834kHmoc5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571743cf02.mp4?token=PNjbU3ufQ90wEHb-pzCB_5XYltSNF_1-6cXPNx5iIZYYzNqFkvxr1dMgppPLJPAXzUlU7slBUTlSzi7o4nEvrq0gY-mRP2M5FD_4KrpBgzFw8iqd0BQJQRnAk-4cbrlZQEfA6a1yuCTiaVbk0L7uft3GJ6Bqj3-tAJscm0MezjYCGSKv3Ju1cXW0AjiuxnQR1yhC5IzuSslKalT2qqhMXGDF0J0CsYhiJmLwiP--HnPkjrLU1RxzhSOjb2OC46h-8pQ7lRwcMGzJ8gMek0g9KsRQTeP76AECgILpCBucaRBJqQdOdExfuxA-wyS_V584pDwqWyVHnbV8834kHmoc5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی وایرال شده از موکب خدمه ام‌البنین که به زائرا آیفون ۱۷ و آیپد و گوشواره طلا میدن!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69492" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69491">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeCt3Ln_LI6LlrJIqEr-1QsHC_gT2HVm0p2ratRNECtUOPcP6jj8Tfuf2o6ZmTbPk0ZHs_ccgkdAY4oOBx82we0Je9Hx8z8xZueeOe8R2WdW6tTyrqt1I6rPXCAY2PkyzFPmYQgKElbo_Rf3iu2-s-JcouUd9hp5jblcYfy9cb_Pj2VovIQTI5Wg__PWFSUPb3bMJt4Ygz1aVoy2LoQkesE2iEruSw1tRyRsj7C-JWFE39SzHLTHgvZ_XtbpBPq0gDmTW6vY4JuIH84zkpjhtAzApvDYWm0J3GVGycUjo4W_jcS3o0rUxf9ZNSz38IQKZzJGBmDGRvvBPLf17Wpz1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhWXZspdw0pX0q6_C36H4M7vDHH9hurl0rw5pkb2VejXJPPuXlEPiZAzSoF6x3C0123_nu8x3kvTxpwAIWUrUDLCeKeljxnO8kMume002ywYLaj9vuhp-YRojpj-7y4DZ2uD3-_lTRHt_bvUcOswKp086GQ2mMRahDsNXSB_e3yAuXkOnayXXdhfc_ZyEdx-HI6NWl5SsoIqXnYs5cWqVgI99Ha_q_bT7JyXwhvFTENC1Tin9vilGsVZmPwGcTxM69mEnw6UKzq8YkrPHTQ_Fs7r7GRHSCmbj0AUczGsojltVZHMnk__xm5C6RM9TFlUrdXTy4XSrsyY_UL8LvzDrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hjt0_Am44eMBfqjpiFRnjxCs7wBEjVbO-kJUIB3MRlXhhgAgQeJPLdmqQ9BpVpXkBTRveNfljzEwSSacUDORHWtMnvzcENw4FMsI9KmJ_cDh5Z3idE5Xxq4qjdv7RC5RxS-306vS3KYdT3Rvbhi1UP1KoJxO4jDdi1zz5sVIkllvr9V9hXmcufE7nUN707TYSYsk6L3DBpiNHtMOG6g5DTACRW95LEHOXC9fcKSaGzV03-44c4NU0hSNsF-ZSurqmMkxyjSJcbTssAdDqFA2Y8g7R0Y5fpt4kW6C7cfMuRXCNxgne7WO36KqU2cJVGmzhdpMAcr-6GRkCpQG7GRgGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCOwwlbZLWDyHwgXAhqTQUA9ESdPw4byfyfxsp2VNKhNbces4HwKTLsEnt48x6v44UjRlXyCV-Ju6O8Ox-Gfmud2zuQ9TM5Wfm9B8ODm4oJizhddOp1urwLbuN3EC6tZSywI3bUqh_0NoOtGR4A0scREGuDZrmgErcyrWNTZJeFZTDM1OBEErshZl9QIzG1zC5f2SFcr04sDFo5LyEL3GPMqBePCoSbRIacCdaf90_zj7IjCq52EVVluq35AmMA8ygnsC8QV5KYWc63tcJP9vUmHI3zCLhgvl-jVbBU_1ZJdnA7TNeVFA35GepRP0Wi2WUMr0PzYhrMvcK-zUsBqLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کامنت های دردناک مردم زیر قیمت PS5 تو سایت دیجی‌کالا
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69488" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69487">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=b-dRdFp8sgCXmigLuSRbpENHAtHxDbBnL-FJzEKTZBvpsslg_AAAcE8YUoXCDTWwYq-lP9a1wfE_QG2Qr2Es2MagyyRPQVle-5dL9cF46_0-bleE4YxGbuyZsVNIAfxSrsHNSjblRqED-z5xtvkmfEKyT-OTpEAJLqgPmOv_LlZB3j8h129yT89ex0qMRORsw7Qop6ZOnhR0te8ahNOJGZxK1KzY3ekc0PocB7tYudn_8F8jM8DNf00YqUYSKbnq6RGiAuvkKHhD4kcRV5_216pEolvnccRS00L0XOtONPZWhEB6rnSwDNUHOGyUbS5XP1U6LV_-R7Li_IV2V--qug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=b-dRdFp8sgCXmigLuSRbpENHAtHxDbBnL-FJzEKTZBvpsslg_AAAcE8YUoXCDTWwYq-lP9a1wfE_QG2Qr2Es2MagyyRPQVle-5dL9cF46_0-bleE4YxGbuyZsVNIAfxSrsHNSjblRqED-z5xtvkmfEKyT-OTpEAJLqgPmOv_LlZB3j8h129yT89ex0qMRORsw7Qop6ZOnhR0te8ahNOJGZxK1KzY3ekc0PocB7tYudn_8F8jM8DNf00YqUYSKbnq6RGiAuvkKHhD4kcRV5_216pEolvnccRS00L0XOtONPZWhEB6rnSwDNUHOGyUbS5XP1U6LV_-R7Li_IV2V--qug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
✈️
یک جنگنده F-16 نیروی هوایی اوکراین، یک پهپاد انتحاری روسی (Geran-2) را با شلیک توپ ۲۰ میلی‌متری ولکان (M61 Vulcan) در آسمان اوکراین سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69487" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69486">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22887d7155.mp4?token=UxaA15Ysucora_-wJ2nJ2pNKq8vma28wA7x-ArIfG53b-jpsYqT4FUltE4A2L9shX4gnil9ge2gIDb8iAg7J6W4xSz3j976740XCQ4vS5V8klakqDUH-t3TCKQj6_uq7oMrscdt3Z7ne3wyBOZjdKrsRtG29ZY2FIL3RGwIQyCHDO4Myppc_zVB4g8lTm-NErijIDVK9AUThj4SdU67018d8KJ-8WZcjdTRqDDqLFFdS9ha8fK7r1PEm60m-hVadOtJC9dvVd3ghLjK5DRvhu87pyVPVLN1pmLOngwfaxlUTdnObRHRkm6fhGUeIjF8CRCQJLfV7EIZ3sCHrBdz3tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22887d7155.mp4?token=UxaA15Ysucora_-wJ2nJ2pNKq8vma28wA7x-ArIfG53b-jpsYqT4FUltE4A2L9shX4gnil9ge2gIDb8iAg7J6W4xSz3j976740XCQ4vS5V8klakqDUH-t3TCKQj6_uq7oMrscdt3Z7ne3wyBOZjdKrsRtG29ZY2FIL3RGwIQyCHDO4Myppc_zVB4g8lTm-NErijIDVK9AUThj4SdU67018d8KJ-8WZcjdTRqDDqLFFdS9ha8fK7r1PEm60m-hVadOtJC9dvVd3ghLjK5DRvhu87pyVPVLN1pmLOngwfaxlUTdnObRHRkm6fhGUeIjF8CRCQJLfV7EIZ3sCHrBdz3tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که میبینید ۱۲۶ سالشه و اهل کشور برزیلِ؛ در زمان پایان جنگ جهانی دوم تقریبا میانسال بود
این بدبخت نمرد تا جنگ جهانی سوم رو هم ببینه و دبل کنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69486" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69485">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20068f370b.mp4?token=ZLNO0wmsw9UuKKaOV7Gj1EJLURtYHzaKOZ15BW2Bk-oLrbbmbapvPdPa2q3lP3fYk6dF2i8bMYuBUVLQCTNC3FGtEUcCcKdcdf5nIR2EbNKheToNybpkRBoxV9nPvIz15RsknrpnypJmyh9RwQenm7Yx3peTB1Hl2CZ4v4bR1NNqHeh68aIpBrGtKRMA9SB0G1nBeMURhZGTzOQLfXVyuUjqjT35op4prIOIfgj6fYUi_RIUyyC0ismON2UJlaBkz7I0bE47wXDO2b96_icL_xUhPaXLNtsaw0polhkz4eRYdUJ9LRELAaRnRHSKOMC7D4obvHIo8OUIXD2cqkdgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20068f370b.mp4?token=ZLNO0wmsw9UuKKaOV7Gj1EJLURtYHzaKOZ15BW2Bk-oLrbbmbapvPdPa2q3lP3fYk6dF2i8bMYuBUVLQCTNC3FGtEUcCcKdcdf5nIR2EbNKheToNybpkRBoxV9nPvIz15RsknrpnypJmyh9RwQenm7Yx3peTB1Hl2CZ4v4bR1NNqHeh68aIpBrGtKRMA9SB0G1nBeMURhZGTzOQLfXVyuUjqjT35op4prIOIfgj6fYUi_RIUyyC0ismON2UJlaBkz7I0bE47wXDO2b96_icL_xUhPaXLNtsaw0polhkz4eRYdUJ9LRELAaRnRHSKOMC7D4obvHIo8OUIXD2cqkdgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T1mRWTQJvN2_kmM1XKJdZTnhQZaXWRqdOBnNpMdtP5JydEij4bWM5OPJdgb77wIyC8xCAuJyELWIAOXmzIfPt7ReOUeFuZLQTJQY2PTtr1gFs75Nes6UWcClQN_MBO7ZY5EoZxdgTuSB6naoEr6yFVcoxfF8MqPMsmJdQNM1o9vSt19XmLy8DVjJd61LghxKtouCaSAKgThJps89Ti6h7amupW4j8a8ZaELyFlCD1wRX2kCxmT1eNEeWca76__zMOfal-tq8iy8ICRPn3fLvbR-BT2dPU4bx5KoGmRK_HYN2eiCBe5ZK_OKGfWsCfMLliAYSDW6Y8o1V9MqrJuqgxRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T1mRWTQJvN2_kmM1XKJdZTnhQZaXWRqdOBnNpMdtP5JydEij4bWM5OPJdgb77wIyC8xCAuJyELWIAOXmzIfPt7ReOUeFuZLQTJQY2PTtr1gFs75Nes6UWcClQN_MBO7ZY5EoZxdgTuSB6naoEr6yFVcoxfF8MqPMsmJdQNM1o9vSt19XmLy8DVjJd61LghxKtouCaSAKgThJps89Ti6h7amupW4j8a8ZaELyFlCD1wRX2kCxmT1eNEeWca76__zMOfal-tq8iy8ICRPn3fLvbR-BT2dPU4bx5KoGmRK_HYN2eiCBe5ZK_OKGfWsCfMLliAYSDW6Y8o1V9MqrJuqgxRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران حاضر است به وضعیت آزادی کامل کشتیرانی در تنگه هرمز بازگردد؟
🇺🇸
ترامپ:
اجازه نمی‌دهم آن‌ها [بابت عبور] هزینه دریافت کنند. اگر قرار باشد کسی هزینه‌ای دریافت کند، ما خواهیم بود. ما کنترل کامل را در اختیار داریم.
ما سازوکاری در نیروی دریایی داریم که نوعی محاصره محسوب می‌شود؛ آن‌ها به آن «دیوار فولادی ایالات متحده» می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69483" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69482">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=g2dHrj9jiWKS-5HftU6eR-YIAoJDj8xYL0i-Q0hGvHWg6Qd3MrwC3At-eR900kfNd0B9KMuw8KsJFDgriv5rncv_5orNGS58DKbjspVOBlfrJscXlEsZeOStXYaeDScEB-dZiIQQj_um1oUg6ZHPypNxTHldoqjJDMgSjUP6o_hW_UN94E-rzOyzGU_4w9BoIsn8cRZfy3Jxi9km4rdRW_oge3B3jqIWpycPxCOGfvCnk_KNW2IUWsNqFtEG-jvYE9NhSGOHqgQoPxqRuN5o_6LL5TJmmL5DTuOd7J115Kyhy8uQMftAoUGhe-LOfdykVC28AnTYjy7o1OQfRoi3TyQ8z-CJTpv9XMKFYHuUTSGtRS1PcUwudfS2eDOIbS1NKa0VwfS6xatEXEArshncsFPGwdCp6Q_IsYMN0z1TEjeNkdT3BrqK5tqXyrYW7jn2MsBAHKF_ht51cwRhkCO8AcnVeqvCNupohjR_0FsRGCntDdUAyFy4cJmwOW1kT9hV6XlKDSNHtSzK7SATz3otmpIgIVzEG7yi_bnTAvXius7_KUI-RP3W_NijzPfhB7oblRHaiaiSgMaTj_8O-Z0omAV3TLTF12bKVkIXCdQSkdYntCtiuSGSKqnsKxB8HKvJTYk99G6vl4VTgMtk6MiTCkTpJHOaNpSCYmhrN4PU6VM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=g2dHrj9jiWKS-5HftU6eR-YIAoJDj8xYL0i-Q0hGvHWg6Qd3MrwC3At-eR900kfNd0B9KMuw8KsJFDgriv5rncv_5orNGS58DKbjspVOBlfrJscXlEsZeOStXYaeDScEB-dZiIQQj_um1oUg6ZHPypNxTHldoqjJDMgSjUP6o_hW_UN94E-rzOyzGU_4w9BoIsn8cRZfy3Jxi9km4rdRW_oge3B3jqIWpycPxCOGfvCnk_KNW2IUWsNqFtEG-jvYE9NhSGOHqgQoPxqRuN5o_6LL5TJmmL5DTuOd7J115Kyhy8uQMftAoUGhe-LOfdykVC28AnTYjy7o1OQfRoi3TyQ8z-CJTpv9XMKFYHuUTSGtRS1PcUwudfS2eDOIbS1NKa0VwfS6xatEXEArshncsFPGwdCp6Q_IsYMN0z1TEjeNkdT3BrqK5tqXyrYW7jn2MsBAHKF_ht51cwRhkCO8AcnVeqvCNupohjR_0FsRGCntDdUAyFy4cJmwOW1kT9hV6XlKDSNHtSzK7SATz3otmpIgIVzEG7yi_bnTAvXius7_KUI-RP3W_NijzPfhB7oblRHaiaiSgMaTj_8O-Z0omAV3TLTF12bKVkIXCdQSkdYntCtiuSGSKqnsKxB8HKvJTYk99G6vl4VTgMtk6MiTCkTpJHOaNpSCYmhrN4PU6VM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=YoDUSWKhSU6qNHKZB5eg7Uow98KtT-d8bZ0E9J2n7aQR-auf6gXCIFFw4gUM733UWfKlXfYud4aghzB5ArKqwneFyFCnBqWqgLp3MsQ6Rpb4rFlvwgptayg8y_WMpIC--uRuPhlBUNZ8dTcAjZh4anf8qd_po7uLa_4YM8aa2VDcIueVZHOH4caYaeKxYxnH3V7MfvlC6pr1yT231BRL1mRlXyB0vZx5VXqayR4NGfuwCuwEYApKRdAKtiaIKnn7PKX9GDDkmseC4UmEJMj9SVf6sxCK2xdscESQ9ZAMsYEP682rSaURKCSdgNUV23-jZXvoDkykRHc2p023lZz1oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=YoDUSWKhSU6qNHKZB5eg7Uow98KtT-d8bZ0E9J2n7aQR-auf6gXCIFFw4gUM733UWfKlXfYud4aghzB5ArKqwneFyFCnBqWqgLp3MsQ6Rpb4rFlvwgptayg8y_WMpIC--uRuPhlBUNZ8dTcAjZh4anf8qd_po7uLa_4YM8aa2VDcIueVZHOH4caYaeKxYxnH3V7MfvlC6pr1yT231BRL1mRlXyB0vZx5VXqayR4NGfuwCuwEYApKRdAKtiaIKnn7PKX9GDDkmseC4UmEJMj9SVf6sxCK2xdscESQ9ZAMsYEP682rSaURKCSdgNUV23-jZXvoDkykRHc2p023lZz1oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=E0okjwb5tXKW4_DEoeJ00kPrtQO1UxPAhxPIHCieXcAu1O-2a4UbLK91fp2cwNA1mAbFD-YlBesWPRf9Y0f4hPRl8PShz7CxQWaaEpBIknGMZOj_hcktAKR46xpzQk7KrvHfmd9xeMlK_SQbvl4GfM4IkB5-cabP44GHLsGL8AoGWpsSfjJozR9JUe2HKFqBbCgdfWEniwIJRC-X7Ah_TCZvNw5YeB7F_AU64ocEFNjqorbhsP8boXsMb6v-JB8V48VrHPSuNdOLVFTdBy_XwbPtF34tfrt1DZFC7juXTnWCi-VAJl3HSNfGgKPQSOJXmR5MOlh8LvMd_62iqmt__g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=E0okjwb5tXKW4_DEoeJ00kPrtQO1UxPAhxPIHCieXcAu1O-2a4UbLK91fp2cwNA1mAbFD-YlBesWPRf9Y0f4hPRl8PShz7CxQWaaEpBIknGMZOj_hcktAKR46xpzQk7KrvHfmd9xeMlK_SQbvl4GfM4IkB5-cabP44GHLsGL8AoGWpsSfjJozR9JUe2HKFqBbCgdfWEniwIJRC-X7Ah_TCZvNw5YeB7F_AU64ocEFNjqorbhsP8boXsMb6v-JB8V48VrHPSuNdOLVFTdBy_XwbPtF34tfrt1DZFC7juXTnWCi-VAJl3HSNfGgKPQSOJXmR5MOlh8LvMd_62iqmt__g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=BvktWgQLAEZpw3aKEoKWIwTIgeN8FhtNco-Hel0rVwDmDkrTxjw6n1xf7s9idoVINCqOLXCoA9oRvhLFnn16V3THpMv4NSHW8-p6r5_n2uoALXmUiTHAD3TrfwvXzT4uVTh6QE5o2oQzNzl_kXct6PyRc4N2Z6dwhhoCJt2dLQNS7hM1T507RXj8ZMgBCyPppYi2hJbFIfxqPFfC-IGU_lu8ezqFf6rht-fj_wwHNAdU07y8BTSsA4CdR4zrJgRP-BSTTfLl9xU_Mm4Tilu7eZ21KeZyt_SRwOagwUxjG1jTZwXoR6Wp2R7JWaPnnzypAkUcBR9xUXvPRI6iS3rM7lsCZb1JSbvRMYzoqG37ioArbNuC1Ve0zFfBjiU-cKIWOq1ua3BK-9EqjVnSsm-hDquHtL-r_tlmrL2g0FBMYS4vsOnTph2Rgdm_R_Lxv3yidzbFWpVe4SkJnSexia8A8gLEK0dnfrUvGa9r1fGgH1my7NFUZnB2AdYx8ufMvGyimWuLo8Dih0-cBc2ef_SY5Oc4gTVO1w_jp5hz2NNRm16i0i1x0Ao0h7nuhk2JaZqyFrSWadz27-_AR9L1SP5SkPH_-r8gaGEpGToPkDEI48Y1OaRhujobcvOnTmpmO0HcEMbhL9pDOEMA04zTTgke6ewxAF_raphn_zzLy3o1boA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=BvktWgQLAEZpw3aKEoKWIwTIgeN8FhtNco-Hel0rVwDmDkrTxjw6n1xf7s9idoVINCqOLXCoA9oRvhLFnn16V3THpMv4NSHW8-p6r5_n2uoALXmUiTHAD3TrfwvXzT4uVTh6QE5o2oQzNzl_kXct6PyRc4N2Z6dwhhoCJt2dLQNS7hM1T507RXj8ZMgBCyPppYi2hJbFIfxqPFfC-IGU_lu8ezqFf6rht-fj_wwHNAdU07y8BTSsA4CdR4zrJgRP-BSTTfLl9xU_Mm4Tilu7eZ21KeZyt_SRwOagwUxjG1jTZwXoR6Wp2R7JWaPnnzypAkUcBR9xUXvPRI6iS3rM7lsCZb1JSbvRMYzoqG37ioArbNuC1Ve0zFfBjiU-cKIWOq1ua3BK-9EqjVnSsm-hDquHtL-r_tlmrL2g0FBMYS4vsOnTph2Rgdm_R_Lxv3yidzbFWpVe4SkJnSexia8A8gLEK0dnfrUvGa9r1fGgH1my7NFUZnB2AdYx8ufMvGyimWuLo8Dih0-cBc2ef_SY5Oc4gTVO1w_jp5hz2NNRm16i0i1x0Ao0h7nuhk2JaZqyFrSWadz27-_AR9L1SP5SkPH_-r8gaGEpGToPkDEI48Y1OaRhujobcvOnTmpmO0HcEMbhL9pDOEMA04zTTgke6ewxAF_raphn_zzLy3o1boA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=dkclg-EDfjlhdRQgmFQlMDHVApCgwjL4nrvuojdre7zWrP9KL4bAaiIQDL3NNiZpFgsIWzGJZxwa6iNMQTVNXPoGnW9HjJAqB38L_5yiGlTLf4MvJHTvjAKI_sJy-DGcLERODZkQWFE3d5lnW19aFeqbyBqTXSh8kF7vRVi6OzZ7rrxXYRGzi5PCyGpiToh_eBaFWo1zJJydH3hinpuF4wb_4NY6Nj0Ti61_zKe3l6kdRAUNvIJgy8zmKpMVuTGLUx88wWPz1gfq3anyrikuoaw2MUXTl73lNHinB8QYmgV2bhcAi5zktcwJ-cdeXRlgYvN3LiDT3JbSvMkuBCc4Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=dkclg-EDfjlhdRQgmFQlMDHVApCgwjL4nrvuojdre7zWrP9KL4bAaiIQDL3NNiZpFgsIWzGJZxwa6iNMQTVNXPoGnW9HjJAqB38L_5yiGlTLf4MvJHTvjAKI_sJy-DGcLERODZkQWFE3d5lnW19aFeqbyBqTXSh8kF7vRVi6OzZ7rrxXYRGzi5PCyGpiToh_eBaFWo1zJJydH3hinpuF4wb_4NY6Nj0Ti61_zKe3l6kdRAUNvIJgy8zmKpMVuTGLUx88wWPz1gfq3anyrikuoaw2MUXTl73lNHinB8QYmgV2bhcAi5zktcwJ-cdeXRlgYvN3LiDT3JbSvMkuBCc4Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
ما با ونزوئلا اختلافاتی داشتیم که به خوبی حل و فصل شد.
ما با ایران نیز اختلافاتی داریم، و این موضوع نیز به خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69478" target="_blank">📅 21:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69477">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=CITBDiLH68FGipX2BXxmy_UVG3NwYvBdN0udmzVtAR-L6MugDW6rJ9SFCjUsG-evAyY9awqCMFoM6MkG5k6nqMNtVCC9jePTw21S8Pwfkbjus1Log4DZdZiNpB1lrL3XOEvfzESbRdI1VSFfmYoUQyHtgq-o22G8-dztREUu22Tw74MqCV5BGpCGBH1F_kpmZ80QrGcKpeFdNofmB_MEHA1TrBPer3cB2p4Xr6A2WHbD7pMBAYRkVKsfqHs_jLY_1e9i2TBCRwFlNJse4GKB2YjiFzEKT_G84XNQbb8qiSocHN6HzezoqmPtAp5TpnwyBlIQdCiFc-ZacIjDiDIY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=CITBDiLH68FGipX2BXxmy_UVG3NwYvBdN0udmzVtAR-L6MugDW6rJ9SFCjUsG-evAyY9awqCMFoM6MkG5k6nqMNtVCC9jePTw21S8Pwfkbjus1Log4DZdZiNpB1lrL3XOEvfzESbRdI1VSFfmYoUQyHtgq-o22G8-dztREUu22Tw74MqCV5BGpCGBH1F_kpmZ80QrGcKpeFdNofmB_MEHA1TrBPer3cB2p4Xr6A2WHbD7pMBAYRkVKsfqHs_jLY_1e9i2TBCRwFlNJse4GKB2YjiFzEKT_G84XNQbb8qiSocHN6HzezoqmPtAp5TpnwyBlIQdCiFc-ZacIjDiDIY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فرماندهی مرکزی آمریکا (سنتکام) فایل صوتی مکالمه ناو آبی‌خاکی USS Comstock (LSD-45) با یک شناور ناشناس را منتشر کرده است. در این مکالمه که از طریق کانال ۱۶ رادیویی دریایی VHF (فرکانس بین‌المللی تماس و اضطرار) انجام شده، به شناور دستور داده می‌شود مسیر خود را تغییر دهد و هشدار داده می‌شود که در صورت عدم تبعیت، با استفاده از زور وادار به اجرای دستور خواهد شد.
ناو USS Comstock به‌عنوان بخشی از گروه آماده آبی‌خاکی USS Boxer (ARG) و همراه با یگان یازدهم اعزامی تفنگداران دریایی آمریکا (11th MEU) در منطقه مسئولیت سنتکام مستقر است و توانمندی اجرای عملیات آبی‌خاکی و واکنش سریع به بحران‌ها را در اختیار نیروهای آمریکایی قرار می‌دهد.
بر اساس آخرین اعلام سنتکام، نیروهای آمریکایی تاکنون ۴۴ کشتی تجاری را که به‌صورت داوطلبانه از دستورات محاصره تبعیت کرده‌اند، به مسیر تعیین‌شده هدایت کرده‌اند، دو شناور را برای اطمینان از رعایت دستورات بازرسی کرده‌اند و دو شناور متخلف را که با وجود هشدارهای مکرر از اجرای دستورات خودداری کردند، از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69477" target="_blank">📅 21:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69476">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoucOuM6y7I4ImUEJMlABhy0NaSmzHsyZX3KAA5jTHqZcnCNYh7TlmiW66PMoYEyn1u0Q7IFnWPVPSIh4tvL1RdORgmycx1NY0tf26shmfnUv4-KoVE_AdrY2SEGuX_scI2rVDA84myGjLAZbjja5rVX570DK7wURHutW0erExPWENISPA9Jq8GCG0Ea1WIBE6R_LH4kM14m9ivtqejyFTeg5jCx1AWnI1cFrv0ajZFAoCIE48nSr2wXT0wi9SsIK6isrRnE5fFfBqW7AWMsKMethE_6rIJJvdt4TbWVWADfBH9On9haV-QmZCCfM4Nkvf1_4XfDizGUDS2pAWRBIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtGMVlvM90eLGqKc1EdrNWgHzz8XqyBJv25ootUgVBF1NUq0crMHiI-yWtSS2W66rNN6DRO2_YRKbUCivlDWRh8FgkfnDfzCCWTAPwfpoJ5gtknNe78VJYGh7Jo5dV2-4MpPQO3cSEpz4ZSBnn0iN38RBepMHKUOO2b5fffHpWggfEoQefywFssMfWM4U9qsQ0crGhGYf5SEkJBAvOGtQm3vlKDeSKbvsIHrX75YTgwQf5emRbFETglafF-9yOu69d6FRljCZe1Xxj4Z04Ukg8qOgnkf_yaiD38NAe_qCA7EwGah0JknGxMcRT0e5XMf2ffw8VJz0OYsPESvIAJKGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4129d878df.mp4?token=DxhpZ2WxY2qm7EGYbgv0VE-HW2tOHVuUvotDUDdqLOJSnAzqtyHD9zCa3jfXuajs5YFCLr_2dEQ7QIc0NA4bS6malZKJIkUt59smih7CeGymmYcbE04qPxnOL0Sjqx-ToN-SGdw9woArBNn-lyreKjVWyDSXxZ9zQIbu7Ey4U07scKxnfP4JXgv-1xU7q83j3GkXc2PMOOjHcsdX8C-J4C3b333Q9EcKFt3sdPRnmyS-ig8bkp_I6Wwy7Osi8XYJ9gRoEYV7XoqqCtFW8ahlndhTNYyFhrW36jRdnOAbJAfIhQVP6nyoT9f6YzpZViMvZc3ROjnSwOfrRXXJj_31fA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4129d878df.mp4?token=DxhpZ2WxY2qm7EGYbgv0VE-HW2tOHVuUvotDUDdqLOJSnAzqtyHD9zCa3jfXuajs5YFCLr_2dEQ7QIc0NA4bS6malZKJIkUt59smih7CeGymmYcbE04qPxnOL0Sjqx-ToN-SGdw9woArBNn-lyreKjVWyDSXxZ9zQIbu7Ey4U07scKxnfP4JXgv-1xU7q83j3GkXc2PMOOjHcsdX8C-J4C3b333Q9EcKFt3sdPRnmyS-ig8bkp_I6Wwy7Osi8XYJ9gRoEYV7XoqqCtFW8ahlndhTNYyFhrW36jRdnOAbJAfIhQVP6nyoT9f6YzpZViMvZc3ROjnSwOfrRXXJj_31fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=NzBTXzZrt8Sx08T4j9L-oNuXol9W-ExXx6VDd8nhBRjZkU8LUT9UWlpkBRleZcyHt1iV0RTOkY3onaeiT841vpCtuSsGPqJ13lspwV7AN73esa-f5teP2aQqhcTK_QLZwLfb6Y80r2j4t4A2uH5znp5TCDhvIKH4-3sWZsd8vHCsFzMEyvZSCn4UnAO_i7RlXPatxDIdbQIfhIEnqcaajYhh6JCQLHfB9lNHLnMEynxnkSPzmdw6BP_bREVdtInGGGjAE4IFv3hA4xjao0bidjIBWDuWJ_uRCwslRYzpV3f1M8D28lLj7-vACdowc9AJgCsKeNGRMOvqlO4RD7clAT0ah6Ii_NyGfeuCntxnW0abFuNwoSTrItBIUTNjbL3VCNfmre32pvZUpaxlr8Ld2UPTuI48tcaumQKWwpWO6FSt5WBKjyP4yEQuwZXTYSZi4MR8d4VA0tnTednJ1Ox6999D2yDM8Yvu2l7PNaG1EU5M1IG18VdzS-Ys2bepNoOm3jW_ig4B_9EC9ATMlakDZ050d5pQRVDsqcDTDnkjJnTzNMRU6BGK7VHWi9TpMlcj7ESx9bYicwECIeHGB0q7NwVapQWKprH9HshXhSJLAUMfy05P3BUL8AFgAay_I0whnjWuZ8rQUf-aKHRCnu8N5ndEYF6yHrKtt0nbaPDsiw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=NzBTXzZrt8Sx08T4j9L-oNuXol9W-ExXx6VDd8nhBRjZkU8LUT9UWlpkBRleZcyHt1iV0RTOkY3onaeiT841vpCtuSsGPqJ13lspwV7AN73esa-f5teP2aQqhcTK_QLZwLfb6Y80r2j4t4A2uH5znp5TCDhvIKH4-3sWZsd8vHCsFzMEyvZSCn4UnAO_i7RlXPatxDIdbQIfhIEnqcaajYhh6JCQLHfB9lNHLnMEynxnkSPzmdw6BP_bREVdtInGGGjAE4IFv3hA4xjao0bidjIBWDuWJ_uRCwslRYzpV3f1M8D28lLj7-vACdowc9AJgCsKeNGRMOvqlO4RD7clAT0ah6Ii_NyGfeuCntxnW0abFuNwoSTrItBIUTNjbL3VCNfmre32pvZUpaxlr8Ld2UPTuI48tcaumQKWwpWO6FSt5WBKjyP4yEQuwZXTYSZi4MR8d4VA0tnTednJ1Ox6999D2yDM8Yvu2l7PNaG1EU5M1IG18VdzS-Ys2bepNoOm3jW_ig4B_9EC9ATMlakDZ050d5pQRVDsqcDTDnkjJnTzNMRU6BGK7VHWi9TpMlcj7ESx9bYicwECIeHGB0q7NwVapQWKprH9HshXhSJLAUMfy05P3BUL8AFgAay_I0whnjWuZ8rQUf-aKHRCnu8N5ndEYF6yHrKtt0nbaPDsiw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=J1IANGw-8Yzi_SfWrM0fPGRJiKKTk7qwZXa4FGgYs6w82GrG2g4W3NSaTGnrRVfStIRjnWLwSRk7QD-T6yU073M0fHqE9AK8fTo9X_pv7J4xtY-oh5JtWNDfHZPMsBpuJDEuAZ290s8dTMSHRw7iMqhKPliATqoFHEhCBJ1zj5nTC0Rv1-8RbgTGb9GOzeGZJ-GM2FdJI-ljO_F1mg3AI7WRSI69Ffpof2Mss_fxC9glGlKoHt_5D_67Z4FOz7362QLO14baFNsRrIdW13xY8RoLENXWsvpUyMeAmw3ruqVZA5I3xgybN9r6ouZdANl86Z5aYEoyjjPXW8ayiD_WyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=J1IANGw-8Yzi_SfWrM0fPGRJiKKTk7qwZXa4FGgYs6w82GrG2g4W3NSaTGnrRVfStIRjnWLwSRk7QD-T6yU073M0fHqE9AK8fTo9X_pv7J4xtY-oh5JtWNDfHZPMsBpuJDEuAZ290s8dTMSHRw7iMqhKPliATqoFHEhCBJ1zj5nTC0Rv1-8RbgTGb9GOzeGZJ-GM2FdJI-ljO_F1mg3AI7WRSI69Ffpof2Mss_fxC9glGlKoHt_5D_67Z4FOz7362QLO14baFNsRrIdW13xY8RoLENXWsvpUyMeAmw3ruqVZA5I3xgybN9r6ouZdANl86Z5aYEoyjjPXW8ayiD_WyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
اکثریت قاطع ایرانیان، اسرائیل را تحسین می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69470" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69469">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=EZEymKYr_gs9LYpnn9kOxk3TRV45oXWKrvNsTSIDU_6r0mDlcfT8yknWosNyKCrkfS22o6w9W8uS3UA7qqZxhl8KKg14HbkJRMTVbqX6V_85gMqyNUTIzIUyB1nPhl8tqPSqhufaT-9XSCYXHvLejOMLPVTurrJv4eAX-4IOFSgv8PQalYfADUMy81qmoPjGwgT0k_-vU3V2N-LCUKELTvjzZmxaL-vibnHNXLtD6JsmF7psowf6B0CpSXz1XhigYTcEgaNx6OxLzjA-qg8F35ANBWaB4QILZw2Bp44ttB5Kt5HDn6SaXhY5kD4wfupMLslBBLF_DCi5cNUb9JizNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=EZEymKYr_gs9LYpnn9kOxk3TRV45oXWKrvNsTSIDU_6r0mDlcfT8yknWosNyKCrkfS22o6w9W8uS3UA7qqZxhl8KKg14HbkJRMTVbqX6V_85gMqyNUTIzIUyB1nPhl8tqPSqhufaT-9XSCYXHvLejOMLPVTurrJv4eAX-4IOFSgv8PQalYfADUMy81qmoPjGwgT0k_-vU3V2N-LCUKELTvjzZmxaL-vibnHNXLtD6JsmF7psowf6B0CpSXz1XhigYTcEgaNx6OxLzjA-qg8F35ANBWaB4QILZw2Bp44ttB5Kt5HDn6SaXhY5kD4wfupMLslBBLF_DCi5cNUb9JizNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
خاورمیانه دیگر آن خاورمیانه سابق نیست. ایران هم دیگر آن ایران سابق نیست. ضربات سنگینی به آن‌ها وارد شده است.
آن‌ها همچنان توانمندی‌هایی دارند، اما به یک ماه گذشته نگاه کنید؛ آن‌ها به سمت ما شلیکی نکرده‌اند.
چرا شلیک نکرده‌اند؟ چون می‌دانند ما می‌توانیم چنان ضربه سنگینی به آن‌ها بزنیم که بازدارنده باشد. اگر به ما حمله کنند، متحمل ضربه‌ای بسیار سخت خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69469" target="_blank">📅 18:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69468">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=qfs5mS-FvD6cNnz0atJ62UqOfJb0F5c2wJDhj-qDTQporFql1zVR0H14DRGuUeJP-cQZJXfCM85Mwffn3GImnbl-X8851S28kG4yRovqtdwS3uy-P8bsMdsQMQmG_p25zAjS5SF36qjksDOTCCCALSqOeiqbBrHLLY8Ie4AqcdRFX-6sydKIjvwTKhcfZ4tqFVuxQIejb8ZbxZYkoC0uuMNI2U7Iz5y9yib2Za0QQQ03A9tpJwIZmBQFMrSZYrXGaG2-VbjLp33_TQlKSh0BSTNo2RFO2gD771AylP1XdlTpEcCxz8P5_SpeXHOQmBLede6g3AMi6tvFme_qnZV_jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=qfs5mS-FvD6cNnz0atJ62UqOfJb0F5c2wJDhj-qDTQporFql1zVR0H14DRGuUeJP-cQZJXfCM85Mwffn3GImnbl-X8851S28kG4yRovqtdwS3uy-P8bsMdsQMQmG_p25zAjS5SF36qjksDOTCCCALSqOeiqbBrHLLY8Ie4AqcdRFX-6sydKIjvwTKhcfZ4tqFVuxQIejb8ZbxZYkoC0uuMNI2U7Iz5y9yib2Za0QQQ03A9tpJwIZmBQFMrSZYrXGaG2-VbjLp33_TQlKSh0BSTNo2RFO2gD771AylP1XdlTpEcCxz8P5_SpeXHOQmBLede6g3AMi6tvFme_qnZV_jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04343db3da.mp4?token=KdorWwmp45az2fZ4AUAHURC1hqZrO2WMymE6CAHVXbb5fy1946pxKPTlr1hU5SFfDzuoq_dQUhIya8KrbTH8H0qzGrLMk3DGa2icf4zMyPzpIeKPDvVsaNiTlZnBs43_9-LFO1U9HW6E9EBXge0pLjR2pgbyRxB0SO_GVcIK0HT7gzWhorLq_Tv1cTaEs4Mqrkc67hvOLiVEiKklgvce6In7nTl-x12X1qJvn5m-b9ffIPR-CgxwzTnvR68-sAO0fartkZopsuxaQQVo-Yf1fOb9XdyINT6GpDcQzNsanhWN2EgEdPtS9ouT5nJmpNebO_WKvIElL6mjUMYKE2ya_aaqWAw9azV8rcHON2TVT4T2Cjt8AKhFXyA5AanDz7iYQXSdzkJ87G5DoS5WUjrgcyKtoYik1qyKl3FTI-JWjJyfjEq4imSDTSTC9_rNyL8n-busrHGdo77F2ZniS-ScwTvfPVU7XqeARAzBE0qKn1Bc102rGrONxmZ40oxN5F3i2gpMnBS8rC0W_9DGYRk2VGJczW7YWzn3WiY3ejsQc91lpfXRZDlyG676mXShulcANuZ-2gowjm5X1jRVadhIBF9GPnQFeIsaezMwJCAtKOrlSkFackcIiWB2hbia9X5DyoqzkXUEri9ntVtzN7uhC6W0eusCloa9KPtis31EDJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04343db3da.mp4?token=KdorWwmp45az2fZ4AUAHURC1hqZrO2WMymE6CAHVXbb5fy1946pxKPTlr1hU5SFfDzuoq_dQUhIya8KrbTH8H0qzGrLMk3DGa2icf4zMyPzpIeKPDvVsaNiTlZnBs43_9-LFO1U9HW6E9EBXge0pLjR2pgbyRxB0SO_GVcIK0HT7gzWhorLq_Tv1cTaEs4Mqrkc67hvOLiVEiKklgvce6In7nTl-x12X1qJvn5m-b9ffIPR-CgxwzTnvR68-sAO0fartkZopsuxaQQVo-Yf1fOb9XdyINT6GpDcQzNsanhWN2EgEdPtS9ouT5nJmpNebO_WKvIElL6mjUMYKE2ya_aaqWAw9azV8rcHON2TVT4T2Cjt8AKhFXyA5AanDz7iYQXSdzkJ87G5DoS5WUjrgcyKtoYik1qyKl3FTI-JWjJyfjEq4imSDTSTC9_rNyL8n-busrHGdo77F2ZniS-ScwTvfPVU7XqeARAzBE0qKn1Bc102rGrONxmZ40oxN5F3i2gpMnBS8rC0W_9DGYRk2VGJczW7YWzn3WiY3ejsQc91lpfXRZDlyG676mXShulcANuZ-2gowjm5X1jRVadhIBF9GPnQFeIsaezMwJCAtKOrlSkFackcIiWB2hbia9X5DyoqzkXUEri9ntVtzN7uhC6W0eusCloa9KPtis31EDJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FT1OGhg_rOBnK_YNjzV6Zf9rijmRpJof48ZcQGEzMUExaz59zauPy_7EtnnGPhvQfO2jPTMLExR_fmI1bIn--PLPGmwwLe481Uuw5VOKHqBOQ62Lou4-bt1nooSBubN1I9uwaPx5FrJbmsZl8VWDSoUCtWWlTGHgVv2ul0n7jCYIM_ECfD2CT8-iMoCkFWdmOS1hWxgeQKBRPRRpSFGVdOgjCTglUigud91cndpii3gib8aZRxdSFEpE3lxVtWlXXq8yg3n85WY16_JbqpBQUd85hOhi9ollH6Qau9sfwcOwTtaZ0Yk7cnkbSIx7wpnoyROm9QnFW5fDwNdxIIYUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛المیادین به نقل از یک منبع ایرانی:
ایران در پاسخ به آخرین پیشنهاد آمریکا، با بازگشایی تنگه هرمز تا پیش از پایان کامل جنگ مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69466" target="_blank">📅 16:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69465">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmQsNJrpeML5Ru0pGM-J8VEeMGhiv_1fq3mco7QShsm7X2UB8q7ldV6APi5ATFUlGqy6HQnu0uGi2QtiO9y1VJJvuhMkdMShsaag0d7FmAwk_OuDk52eGKn9hWsMvuVu94lAQRTIrj69dtI9CIZQy7tg-uQci0DNswoWWP17BA8RL6U7SeNYmlJt8r5-TiyNigcvBIIXa4WHnGFXZtDbN1YWQkG2ogzFB_9iJPRS7o2Tk3gIz1zJ3X5IZGKu9bMTtpD2L4lBOpxt0j8iPOws6G6yHYA5txxI9w_0GGEskf00mrCw1UohJIrSFPoj9n126S0QtqL8ketjOaWynLZ4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست میانگین IQ کشورهای مختلف تو سال 2026 هم منتشر شد
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69465" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69464">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863fff3357.mp4?token=nJSLOU9rpwXKQmxcb8k_bFzjsb0X81dEKDksWvThF58vrN5jF6YD35JtyY7iH4ItfiYLvOWFr6sZjN_SLLrO6e21uMXqx6bGfhOSOVJFiwJoacorGaUWHnvN3FvrYry8aL42Jx6ziGZkOA6KBwHz8RrIXE2Ta-rR3WnICi7978c7dnVHXiU1PtkjOkA6IHJ5VuIUDP5Pwi0VFPCL--qpzKSh39-nLNqw0z0eyS9UK7eqn_BnBT-bvaohvAmHnao90n41FIakWkFb0x5BceBt6caNK7DX01_umKkFmIWdEXHa5R1QWgtEbRslFslYvME1w7MOnHwhgVhZrkRvLM7Jhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863fff3357.mp4?token=nJSLOU9rpwXKQmxcb8k_bFzjsb0X81dEKDksWvThF58vrN5jF6YD35JtyY7iH4ItfiYLvOWFr6sZjN_SLLrO6e21uMXqx6bGfhOSOVJFiwJoacorGaUWHnvN3FvrYry8aL42Jx6ziGZkOA6KBwHz8RrIXE2Ta-rR3WnICi7978c7dnVHXiU1PtkjOkA6IHJ5VuIUDP5Pwi0VFPCL--qpzKSh39-nLNqw0z0eyS9UK7eqn_BnBT-bvaohvAmHnao90n41FIakWkFb0x5BceBt6caNK7DX01_umKkFmIWdEXHa5R1QWgtEbRslFslYvME1w7MOnHwhgVhZrkRvLM7Jhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69464" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69463">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda203069a.mp4?token=Ff689yeIxt0AclXOvFoOHfx10EbtDi-mBw7xgETY0lXkL0i0RcAtBxa0GIy-vHYoYWQwMls0_HnnhRFAt5PZZmgL_QxwXwmqPrlLZb9U27rLSleFfyfMRWA2pTqzHl2G6uNCHK5f8GL-8evFmKmD0ywAjxlRb65p7NBPgoMiL7L3X0DYD2X09EIDUghs-wdIJDb6GgUejIbtyU3wS-RXXfSl9ZJ-KKI5jAP506_xhhNWnY9IAccEI2zh9qQ7CiDTT6Liwc3AMkcyJ661gO9wwDP8PZt9Apmfm302StXDho6ulZScMSNxrB3P-JijG_jRliwom2GYxcvvwXp0kE8d4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda203069a.mp4?token=Ff689yeIxt0AclXOvFoOHfx10EbtDi-mBw7xgETY0lXkL0i0RcAtBxa0GIy-vHYoYWQwMls0_HnnhRFAt5PZZmgL_QxwXwmqPrlLZb9U27rLSleFfyfMRWA2pTqzHl2G6uNCHK5f8GL-8evFmKmD0ywAjxlRb65p7NBPgoMiL7L3X0DYD2X09EIDUghs-wdIJDb6GgUejIbtyU3wS-RXXfSl9ZJ-KKI5jAP506_xhhNWnY9IAccEI2zh9qQ7CiDTT6Liwc3AMkcyJ661gO9wwDP8PZt9Apmfm302StXDho6ulZScMSNxrB3P-JijG_jRliwom2GYxcvvwXp0kE8d4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
میزان شانس بقای جمهوری اسلامی از زبان مراد ویسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69463" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69462">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b293a286.mp4?token=j9KsfdEo2-AUJQVocYWduQnh9_qve5LPpaF0vKOziQdnVcgX3rLVhoGiUxLR7S5p1i3hnTDGgp5PCzKccWGipjB97NJDiLgH3qreYmLQfkOQypr-hCKmDQbd1skLQuF3gNfp97b0rrooWW0B7h5g1WWyRKmAwubS4EznKKZUnAb0x_kVOhdvLIAgIcNTcKhJidihAVfL_19dU36_aUP7XH2gXmXZNSNM48Ya9rCZ8Nw2gvoc9WzGTpe0npL6E_kNDFL-u8h7pAf_7--hkcrANu_c3_MOpLIX-wP2ZOl2qa5XXh0DQwQVWm0S-P5KrEGywzHSXlomflh1KDpfWFU4Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b293a286.mp4?token=j9KsfdEo2-AUJQVocYWduQnh9_qve5LPpaF0vKOziQdnVcgX3rLVhoGiUxLR7S5p1i3hnTDGgp5PCzKccWGipjB97NJDiLgH3qreYmLQfkOQypr-hCKmDQbd1skLQuF3gNfp97b0rrooWW0B7h5g1WWyRKmAwubS4EznKKZUnAb0x_kVOhdvLIAgIcNTcKhJidihAVfL_19dU36_aUP7XH2gXmXZNSNM48Ya9rCZ8Nw2gvoc9WzGTpe0npL6E_kNDFL-u8h7pAf_7--hkcrANu_c3_MOpLIX-wP2ZOl2qa5XXh0DQwQVWm0S-P5KrEGywzHSXlomflh1KDpfWFU4Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعترافات عبدالباری عطوان (تحلیلگر سرشناس جهان عرب) رو شنیدید؟ کسی که همیشه به مواضع خاصش معروف بوده، حالا لب به اعتراف باز کرده و از کابوس کشورهای عربی پرده برداشته!
عطوان در تحلیل اخیرش (مارس 2026 )به صراحت میگه:
اگر پسر شاه (شاهزاده رضا پهلوی) به ایران برگرده، با توجه به اتحاد استراتژیکی که با اسرائیل خواهد داشت ،ایران به چنان قدرتی تبدیل میشه که تمام کشورهای عربی منطقه باید جلوی عظمتش زانو بزنند و عملاً به نوکرهای ایران تبدیل میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69462" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69461">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=ktyNqoPCknEu9zNo7aNcaGln6OjqVyGR_7p87xNe6Dd1bQ3TLOXzz3k9Gy22ASXqu7Fp8mwgPCr0kfr1KpwOs-UOVZsO-PqtDL-Trk_dBk4TxfPQ43edNnSOlG2ra-33weo8nOqPct99Zg4zhl07I9lm151BZADr5eox2aiCqQ43TnuDgMOoHU4l4-ghOHIOu7v0Vk5iA-LTd-m0Uix06X5BOGRft2pUHHYoEA5wICX80BZxBpzwGBCialEFwCzBiWYvwzvMrYLh_RlfXOsXxs_VnsvVXAYZ4lgn5HJV5SD8q9Op8qiW8ULlMK2E5u-D_HBSPiUZad-daWmmyOe-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=ktyNqoPCknEu9zNo7aNcaGln6OjqVyGR_7p87xNe6Dd1bQ3TLOXzz3k9Gy22ASXqu7Fp8mwgPCr0kfr1KpwOs-UOVZsO-PqtDL-Trk_dBk4TxfPQ43edNnSOlG2ra-33weo8nOqPct99Zg4zhl07I9lm151BZADr5eox2aiCqQ43TnuDgMOoHU4l4-ghOHIOu7v0Vk5iA-LTd-m0Uix06X5BOGRft2pUHHYoEA5wICX80BZxBpzwGBCialEFwCzBiWYvwzvMrYLh_RlfXOsXxs_VnsvVXAYZ4lgn5HJV5SD8q9Op8qiW8ULlMK2E5u-D_HBSPiUZad-daWmmyOe-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
عراقچی داره میره اربعین و ماهم توی تهرانیم.
دوشنبه مذاکره ای نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69461" target="_blank">📅 13:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69460">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
از فرصت تفاهم‌نامه و لحظه‌به‌لحظه آتش‌بس نهایت بهره‌برداری انجام شد
در این مدت، واردات تجهیزات جدید، تعمیر و بازسازی سامانه‌های آسیب‌دیده و همچنین تولید سامانه‌های جدید در دستور کار قرار گرفت.
پهپاد‌های جدیدی که اخیراً از آنها استفاده کردیم نیز حاصل بهره‌گیری از فرصت ایجادشده در دوره آتش‌بس بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69460" target="_blank">📅 13:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69459">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08375903ec.mp4?token=QpxIvC-17VTxdpB_pMQxG2yENFKbJ9mOKtuJMJEIiueSxIy1vyyb8DBtGUia5lZdscq8zPyhjgTshMP4BhhLrwhHsrByEH_cGzfmHbe1AxqEFw-fpURdiTj73YeCCS1B0JKKHl5y-fGJbD1BXTX1vgv7GWqEpyISknnxih77kgyn7N9bIjtilYy7DpAU3J0nRLP-cEWMKHdrv5K10aAdw5gD-_T6ZmxTYy6uHOaLL7A5Khq21O7wdhXLbbDQMq9nyBemqhZYpVawGJXS7XgFIXOBMiJTQ29Ug3YyLq4izcl2j_aq_PExBVRHEeLDXyn5945bWyG1NYWf0ADOYw6iGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08375903ec.mp4?token=QpxIvC-17VTxdpB_pMQxG2yENFKbJ9mOKtuJMJEIiueSxIy1vyyb8DBtGUia5lZdscq8zPyhjgTshMP4BhhLrwhHsrByEH_cGzfmHbe1AxqEFw-fpURdiTj73YeCCS1B0JKKHl5y-fGJbD1BXTX1vgv7GWqEpyISknnxih77kgyn7N9bIjtilYy7DpAU3J0nRLP-cEWMKHdrv5K10aAdw5gD-_T6ZmxTYy6uHOaLL7A5Khq21O7wdhXLbbDQMq9nyBemqhZYpVawGJXS7XgFIXOBMiJTQ29Ug3YyLq4izcl2j_aq_PExBVRHEeLDXyn5945bWyG1NYWf0ADOYw6iGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نیروی تفنگداران دریایی آمریکا ویدیویی از تمرین‌های تیراندازی نیروهای خود منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69459" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69458">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al14QfbCc7arVFwSc6cghjSDmh3piSPKO1uEl6PMRCXA-uT_MzVJf5Iq665Jyha1ldKHyUbDXUXSzDJObMMZex10zSrNS8kMzKq0L5vbIEgoN6uGYO7jzJ9JsGPfljBM4loXdD1_hsyGuhpZYQJ__vwNbDQCYKqBPSRFUFlqG8MurQc6sgVFmV-WthM2lgWl4q6oCrt2ovoLCNEg4SfkE7bSXteNKcD1vZXqD3K0hEqnO_94iOvxG1LLRIzVnUZZFFaJMocaV_hlR2_psoht9mLqCM-zjrxCKRr9l_ni0F1Un_2-3CKihmAf6cMrcehErhCcXQYV_WFy6wICOVunFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی، سخنگوی وزارت خارجه:
ما در حال حاضر هیچ‌گونه مذاکره‌ای با ایالات متحده نداریم و مذاکرات با عمان بر دستیابی به توافقی پیرامون عبور ایمن کشتی‌ها از تنگه هرمز متمرکز است.
هدف، تعیین مسیری موقت است که ایمنی کشتیرانی در تنگه هرمز را تضمین کند.
تا زمانی که محاصره دریایی و اقدامات ایالات متحده ادامه داشته باشد، هیچ تحول قابل‌توجهی در وضعیت تنگه هرمز رخ نخواهد داد.
🇮🇷
اسماعیل بقایی، در واکنش به ادعای جلوگیری عربستان سعودی از حمله آمریکا به ایران:
اینکه همه کشورهای منطقه اذعان دارند که از تحولات و شرایط آتی منطقه متأثر  شد، امری مثبت است.
جنگ ایالات متحده علیه ایران، جنگی علیه کل منطقه است.
طی پنج ماه گذشته شاهد بوده‌ایم که حضور ایالات متحده در منطقه، موجب افزایش ناامنی و بی‌ثباتی شده است.
طبیعی است که کشورها برای جلوگیری از تشدید ناامنی تلاش کنند، اما تجربه نشان داده است که هیچ‌چیز جز قدرت و توان بازدارندگی ایران، مانع دشمن نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69458" target="_blank">📅 12:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=bhBLZV0m3zo2GmmI4jXBWGvvodfoaIPi263cq9PLFKu-goHCECsz3gSZ0hpSYhu2bLczKNhVcsPh3hoAqYhdZ8Dp8GhFXSjV0xD6BVH1_o5nJOffmUCzzEeTF3YlBFl4-lHbaC-nziqWOmdQ0WAmyuouHvlwktby7M8CnB8rqiVYZtA8WxVl8YACPBwrqg3KoVqXDuNETwOTH_kSK4ETkxFgwazpwmVlPl7j4WHhvaQXaPRk-HfvIURqF_2YokuANW9ziHWcTxWfDu5jiRKDTWJT6Xw_-5DLBOtX_Hvd6JA4gY2itG3SjEnSozK3JjP7kkjfK6x4XJa1Rvtzu0oZhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=bhBLZV0m3zo2GmmI4jXBWGvvodfoaIPi263cq9PLFKu-goHCECsz3gSZ0hpSYhu2bLczKNhVcsPh3hoAqYhdZ8Dp8GhFXSjV0xD6BVH1_o5nJOffmUCzzEeTF3YlBFl4-lHbaC-nziqWOmdQ0WAmyuouHvlwktby7M8CnB8rqiVYZtA8WxVl8YACPBwrqg3KoVqXDuNETwOTH_kSK4ETkxFgwazpwmVlPl7j4WHhvaQXaPRk-HfvIURqF_2YokuANW9ziHWcTxWfDu5jiRKDTWJT6Xw_-5DLBOtX_Hvd6JA4gY2itG3SjEnSozK3JjP7kkjfK6x4XJa1Rvtzu0oZhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله پهپادی روز گذشته به مرکز لجستیکی عظیم شرکت وایلدبریز (Wildberries) در نزدیکی سامارا.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69457" target="_blank">📅 11:47 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
