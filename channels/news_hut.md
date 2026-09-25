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
<img src="https://cdn4.telesco.pe/file/ixCl_7hTwlV-GdJeN2zUWdxaHdnA9WeV_9_KlDpPCwBlEW-TrUh61Iu2p18HP83kaL_wrPp95HsTLIml63xGg5fbGvWc9Glvx113zT4voOkr-KX0Y2A69VIuuvgEsC6eIMTh4mzll80bV7pHsatYqG5ehHxav5sIgitZuuTtzcvE5eGnAU0YHlohFufNXxp9PY28wHOBb0vwF1a7gPY7LD73ye1hGbwIkob6uYt2dSfew1Qb4nJfFkZheBtqFSjvPCm7hlkQHj_jElyfhEVli7BjopthXgQ-zstfV-a0cjPtWR066aSUJgxOf4-8RH1nXgOGzJapB5Mi4Xlqc24IrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 20:53:33</div>
<hr>

<div class="tg-post" id="msg-72279">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=n-hP-pTSXZS0KmjgfJDAhjFkMEa8aBOyISM-PxVe-72yOW7sJXt7FtevctddQTbKog2Q-RLZu0dkSho5sI9LG0SgMEKpSNAsJtKg1W-2V975SeigLI65zxSQEPwYUbrzg11N5fL2BeXDQ8sfsgo_vjDcfr0S-fR2my1dWHg9FKxbPni96sqCVA3P9VkYz24mElRero58A93FJvqWvT9FR1MzT4ridC2sOOtbbK2Mhvt2j_vyJYeFDgQ_UovCcQ5V3DY0KyJ2HQiaZrRMOKhcD7kUMRRxNorRecaEVspGinwOQIiMk4dPhKOR0np2Y2kuLfTjDYwcfHuMxVrv8xRVoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=n-hP-pTSXZS0KmjgfJDAhjFkMEa8aBOyISM-PxVe-72yOW7sJXt7FtevctddQTbKog2Q-RLZu0dkSho5sI9LG0SgMEKpSNAsJtKg1W-2V975SeigLI65zxSQEPwYUbrzg11N5fL2BeXDQ8sfsgo_vjDcfr0S-fR2my1dWHg9FKxbPni96sqCVA3P9VkYz24mElRero58A93FJvqWvT9FR1MzT4ridC2sOOtbbK2Mhvt2j_vyJYeFDgQ_UovCcQ5V3DY0KyJ2HQiaZrRMOKhcD7kUMRRxNorRecaEVspGinwOQIiMk4dPhKOR0np2Y2kuLfTjDYwcfHuMxVrv8xRVoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌بی نتانیاهو یه شوخی برا میلی رئیس جمهور آرژانتین کرد و اونم یهو زد زیر خنده
@News_Hut</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/news_hut/72279" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72278">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=KKJAMZnHHWWUU4jvYUNrbFpYlKMNicBTh4G8AD7K9eatQlRZDzqRiEOhSxSi_EDZS-78MrVsztggf8pkxR-iM1vxDZyaZp6ZmFuzMFd6DqfL7Mesz3rYOQqW6dHk0QGoIuSjqcERH2ZGYDbNVST9dnCwcfy6EWggYdNYpjPuhR9bp0xD5kHFj7YORmK3PazsvBR5rDT-GfBLekskKdgbFCdsoAttYMIPhpSmL0oQ0YyLm_xFjGNGXYcGqcTRBbkQDNwRKPnks3lA63nGdglbLJutDVLIbK611_7yCl9Oh7YTI60n9K4Y3D6-mhuCw3xTFR_xxYRFZQo8LaWGBdHFBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=KKJAMZnHHWWUU4jvYUNrbFpYlKMNicBTh4G8AD7K9eatQlRZDzqRiEOhSxSi_EDZS-78MrVsztggf8pkxR-iM1vxDZyaZp6ZmFuzMFd6DqfL7Mesz3rYOQqW6dHk0QGoIuSjqcERH2ZGYDbNVST9dnCwcfy6EWggYdNYpjPuhR9bp0xD5kHFj7YORmK3PazsvBR5rDT-GfBLekskKdgbFCdsoAttYMIPhpSmL0oQ0YyLm_xFjGNGXYcGqcTRBbkQDNwRKPnks3lA63nGdglbLJutDVLIbK611_7yCl9Oh7YTI60n9K4Y3D6-mhuCw3xTFR_xxYRFZQo8LaWGBdHFBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای ۲۴ و ۲۵ سپتامبر (دیروز و امروز)، افزایش فعالیت‌های ترابری ایالات متحده در ارتباط با خاورمیانه مشاهده شد که شامل هواپیماهای ترابری و پشتیبانی آمریکا—مانند مدل‌های C-17، C-5M، C-130 و KC-135می‌شد...
تدارکاتی در جریان است!
@News_Hut</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/news_hut/72278" target="_blank">📅 19:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72277">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=CR5jOmyiLlZ518y6qce0cojp2nxnQnNFIUXmsm3AqpLohfQ6buOm_RPg9EQd7xtKwx06oP2CJMAEMuYgzBddeBwKw1OsKk_y1XNnPwEK9EEVTpNm9cbD6yFJDnxjW5y0tW3Wlfe_NG79DoDSl0ubVKnQP9e3CiVxLbLqvdZnwy_Xlb46CiHxoAl-PUA_iK2ImQ7Trr9qy_AYvDFbb5SJxp7tbcTId2v0ZJY0grPz0Sh0k6YZNxyUNc70xt6AHpAZMXElT_RwWwTAmCvz9JMJlHuR14XPbEYRvZQnUQwlSDJUyMjgOoI-YcO0yKSqBkbcbg3YAJP28lTaOre6d2OBaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=CR5jOmyiLlZ518y6qce0cojp2nxnQnNFIUXmsm3AqpLohfQ6buOm_RPg9EQd7xtKwx06oP2CJMAEMuYgzBddeBwKw1OsKk_y1XNnPwEK9EEVTpNm9cbD6yFJDnxjW5y0tW3Wlfe_NG79DoDSl0ubVKnQP9e3CiVxLbLqvdZnwy_Xlb46CiHxoAl-PUA_iK2ImQ7Trr9qy_AYvDFbb5SJxp7tbcTId2v0ZJY0grPz0Sh0k6YZNxyUNc70xt6AHpAZMXElT_RwWwTAmCvz9JMJlHuR14XPbEYRvZQnUQwlSDJUyMjgOoI-YcO0yKSqBkbcbg3YAJP28lTaOre6d2OBaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شی رئیس جمهور چین میگه عکس روی دیوارو ببین؛
ما خیلی برات احترام قائلیم!
@News_Hut</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/news_hut/72277" target="_blank">📅 18:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72276">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=GB0WDZ6SS51PP8xIAoFA1MwrADOf5E5EWrXB8XX8bBy9o8TVvxkF141B3-FLBPvziAP9rVegPmDJ0aWHMZGn62s3zU4N6QrfTUaBJGPSiR_x25sAAcUWF_7Y085bGQpaUxxNkMr_rdT8r9Ie7TDAi_PpUE2E9yubh8oQTFF7VWde3d6kHYj7MbvbuLeQb-ISzGwM-js6ckBClNVqwRrpBZywp4ElM51O5D7cT5tD7LRtbi2PaLiCDUCZjiS53kZKfkGk_H4EGqNOoyniWMTOH63bxO_zHtl6vJUqJVuH-J3hQMyvdOY5wkRCH2c0HLEgl1LmHiFQE6AqIrF7fzfdjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=GB0WDZ6SS51PP8xIAoFA1MwrADOf5E5EWrXB8XX8bBy9o8TVvxkF141B3-FLBPvziAP9rVegPmDJ0aWHMZGn62s3zU4N6QrfTUaBJGPSiR_x25sAAcUWF_7Y085bGQpaUxxNkMr_rdT8r9Ie7TDAi_PpUE2E9yubh8oQTFF7VWde3d6kHYj7MbvbuLeQb-ISzGwM-js6ckBClNVqwRrpBZywp4ElM51O5D7cT5tD7LRtbi2PaLiCDUCZjiS53kZKfkGk_H4EGqNOoyniWMTOH63bxO_zHtl6vJUqJVuH-J3hQMyvdOY5wkRCH2c0HLEgl1LmHiFQE6AqIrF7fzfdjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده با این شرح:
مردی در مشهد با انداختن 100 میلیون از امام رضا شفای همسرش رو طلب کرد ولی همسرش شفا نگرفت و درگذشت و اونم برگشت تا 100 میلیون رو پس بگیره
😑
😑
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/72276" target="_blank">📅 18:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72275">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72275" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/news_hut/72275" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72274">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzNejnkF-pFGWQZz6vcup8nrO6bov2KgLG23_fCE_ND3yEH6pDfoTJAQwPoTWI891F-hzhlXqZRa6w6BYi7KfAoBLwLG5goTGOVAPP4uu4gd-29Mn0bkDUztcje8IkjTvyz0egsMByEORD0_AgNexTcVdvINJSBNoRzyNLfBFiX6-S_ztV3-YRQSooHawhY5dyE0Z8fym3OXtlY5PnKxquHCHEOBmskgbEHwclJEHC8-5tsUp9cDhfddBi7C7RTZc-Qi_hJI6koVzheaqytjMrmSJSpWUi-KUkKOpVbg7Ml4qPWqBEvwK9vIPo4UqzAMHNu9bV5jaz0aT8IrAzJmuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/72274" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72273">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=VswouGp2dgT1EYXIaF-GeoO_WN-dryYPQsHkKgl7-wQPpudq3FvgPgWHClyTZggVs1lNLhQoS3kPJ_GuBT3m4akVdsdJ4wPtdHqVOL2fNsXseDl4bq7GKa4Opi52HIom-DNL4HsDoxB8mUmHEL4oTa52iNnfV-Y_0ncmPN4_QTcp0uuBe94XddGM99Cvwi9TEKlA4MXMUQef_7QMRvg1dyTnDM6aDteY8PG5_xTm4m5f2nkJhdkA8j48vPjBU3psY63eifd2KA56LxrXam60O5-K7utYF8XbRtngMaheA7VJxqgLpGWre9Xn5aPIaggRMeEqqu5gbgohvODALFWZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=VswouGp2dgT1EYXIaF-GeoO_WN-dryYPQsHkKgl7-wQPpudq3FvgPgWHClyTZggVs1lNLhQoS3kPJ_GuBT3m4akVdsdJ4wPtdHqVOL2fNsXseDl4bq7GKa4Opi52HIom-DNL4HsDoxB8mUmHEL4oTa52iNnfV-Y_0ncmPN4_QTcp0uuBe94XddGM99Cvwi9TEKlA4MXMUQef_7QMRvg1dyTnDM6aDteY8PG5_xTm4m5f2nkJhdkA8j48vPjBU3psY63eifd2KA56LxrXam60O5-K7utYF8XbRtngMaheA7VJxqgLpGWre9Xn5aPIaggRMeEqqu5gbgohvODALFWZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی گسترده در یک کشتی حامل خودرو با پرچم یونان در شمال جزیره میکونوس
این کشتی ۲۹سرنشین و نزدیک به۲۰۰دستگاه کامیون و خودرو داشت
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/72273" target="_blank">📅 17:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72272">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=vSffitEXfSKrcCpSegrztS-VcWXRWGiDqmeRYkCpR9p1dA8wOGnCXqjY8WglGZbwOUjzbLrb5BFBBv2mlJzW2Ar-_TEbOGd7_AGo44yxrHuX102XMmig5iEBtyfbA3nm2ZRqQZFf0CzklLIdxdw1iqf8P6cehmfqm9KYv769jFuqd2K-IncOLoU3r4YzS6sD2wqwBM7JKdqaqEXlgqIwGv-ZSxabWYRtfBwzbcUYmEkpnG1EFbDWtjT4r3oSZN6ICjNpAqUjJJzaDN93ZwdYJ774ULEsbv2sWIHEiIM_yvEQTtBz5RhGihwoZyNphNiRGLqJfslrSVNAWmc9o1iTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=vSffitEXfSKrcCpSegrztS-VcWXRWGiDqmeRYkCpR9p1dA8wOGnCXqjY8WglGZbwOUjzbLrb5BFBBv2mlJzW2Ar-_TEbOGd7_AGo44yxrHuX102XMmig5iEBtyfbA3nm2ZRqQZFf0CzklLIdxdw1iqf8P6cehmfqm9KYv769jFuqd2K-IncOLoU3r4YzS6sD2wqwBM7JKdqaqEXlgqIwGv-ZSxabWYRtfBwzbcUYmEkpnG1EFbDWtjT4r3oSZN6ICjNpAqUjJJzaDN93ZwdYJ774ULEsbv2sWIHEiIM_yvEQTtBz5RhGihwoZyNphNiRGLqJfslrSVNAWmc9o1iTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت اسرائیلی در سازمان ملل اسامی کشور هایی رو که حین سخنرانی بنیامین نتانیاهو سالن رو ترک کردن یادداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/72272" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72271">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=ELwO2j6r9HBAhGCetSrbLowzcxj-WUUHphEZDx0et_1U9SuYIboWNN9LWVd66-KdVsNPbZZ3_wYUPvdUvTo1jzvuEWB_3-VYK4nWdbWeyFQ5OTwteB5nvcsDYz89IVNv3EQmd3wFBYJlTPlFhatWqNQLQ0rCXqZwcOT8dhGgBYvYTBWgh0U-4K0SFuodY6SJtQ5hCggp1GxD0TjBmOMWY6JQy8fWzpJm4qWWFalRAHrmc7PzRzY9PzGbk9I78gqPYvNH96SE3JV8wYmwAWqrRjvEKPGi-wi1kdYMqXgxsSPGB-2KjEpBzIhg-rOgUz85iKrJFPGggum5ysg4Owr1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=ELwO2j6r9HBAhGCetSrbLowzcxj-WUUHphEZDx0et_1U9SuYIboWNN9LWVd66-KdVsNPbZZ3_wYUPvdUvTo1jzvuEWB_3-VYK4nWdbWeyFQ5OTwteB5nvcsDYz89IVNv3EQmd3wFBYJlTPlFhatWqNQLQ0rCXqZwcOT8dhGgBYvYTBWgh0U-4K0SFuodY6SJtQ5hCggp1GxD0TjBmOMWY6JQy8fWzpJm4qWWFalRAHrmc7PzRzY9PzGbk9I78gqPYvNH96SE3JV8wYmwAWqrRjvEKPGi-wi1kdYMqXgxsSPGB-2KjEpBzIhg-rOgUz85iKrJFPGggum5ysg4Owr1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پزشک کودکان : امروز تو تهران ی دختربچه ی ۴ ساله ی بسیار زیبارو آوردن پیشمون با خون ریزی شدید واژن، معاینش کردیم و کاملا مشخص بود بهش
تجاوز
شده، از پدرش پرسیدیم میگه با واژن افتاده رو جاروبرقی درصورتی که دروغ میگفت و مادر بچه وقتی رفته بود بیرون این کودکو با پدر کودک و دوست پدرکودک تنها گذاشته بود...
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72271" target="_blank">📅 16:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72268">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6YNoaxrszibr1JU9AevuOw5Dr1q_pQLlTDY2_qXOBG1KU2arxSx1QuzKpISqZiOvtbIR40v3uYDzIhFRncI5uyjXmerKpoOxl7avcNyYMLP38z6PpQ5Wo__st-mNJNeLVrk_HL1QghygGsfjQ9uG_chB9uesp1kzcplh63Wj5_fOHqs4-8Bqhs3Z2B9HOiwUtku1l6DU0LQ4qqhoPYeZnyHjSR1q9BtGGtGK-RxUMTlFB4JyHkZRObr3KtkzJS7Iwpaq2I7ekGWh1kaG79SgO37iQpvkk6Tp4Osx3oAWCQDl-zBGu97nSLGfXMCEaxf7-PZCz44lFzdVJ31EsWheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=KeAT6xmxHd7Ao8Qq_7lqF5q1HGZ-53FMxw_h4C9yz-sDywstCb-Cp9KRzS43ekbKlXdS3yuzblBPTAB5bofvA3lc9w7KDyj3QFixI4VhsymI___JYeL3j4ypWa3nSmrPV55T74l-Nr0Zu-MxQKiE0QXbeT1mTuUkBovTagOsYVckyTQC_i0_CXL1Z5ag33O_B5QrFMYP3UMtdP5aPVo59zCVnHVdAWcxILO6D-oSk90eKuso8ykbcYesGYTNQPe1oukdk0RBSxtB-tLsYfjadoAbL8_aS4JbZyykGU-WnufM-_CDu-L5ynI9rLOlPHSNxGqDDlOpQdmZC4pDGRNW_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=KeAT6xmxHd7Ao8Qq_7lqF5q1HGZ-53FMxw_h4C9yz-sDywstCb-Cp9KRzS43ekbKlXdS3yuzblBPTAB5bofvA3lc9w7KDyj3QFixI4VhsymI___JYeL3j4ypWa3nSmrPV55T74l-Nr0Zu-MxQKiE0QXbeT1mTuUkBovTagOsYVckyTQC_i0_CXL1Z5ag33O_B5QrFMYP3UMtdP5aPVo59zCVnHVdAWcxILO6D-oSk90eKuso8ykbcYesGYTNQPe1oukdk0RBSxtB-tLsYfjadoAbL8_aS4JbZyykGU-WnufM-_CDu-L5ynI9rLOlPHSNxGqDDlOpQdmZC4pDGRNW_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای اوکراینی به چندین تأسیسات صنعتی در روسیه، از جمله پالایشگاه نفت «پرم»، کارخانه «ایسکرا» در اولیانوفسک و تأسیسات «وورونژ‌سینتزکااوچوک» در وورونژ، حمله کردند.
پالایشگاه پرم که یکی از بزرگ‌ترین پالایشگاه‌های روسیه است، در پی این حمله دچار آتش‌سوزی در واحد فرآوری «AVT-5» شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/72268" target="_blank">📅 16:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72267">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که یک موشک رهگیر به سمت یک «هدف هوایی مشکوک» که بر فراز جنوب لبنان (منطقه فعالیت نیروهای اسرائیلی) شناسایی شده بود، شلیک کرده است.
ارتش در حال بررسی این حادثه است. هیچ‌گونه آژیر هشداری در شمال اسرائیل به صدا درنیامد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72267" target="_blank">📅 15:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72266">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=dnUkFoKNLYMJ-kEZ7dcwWefejFIyRorlcE4dl9rSjQoa4X-owFFnlE4Fh0W_MauzpHKcbCutZnIRMt7PeEAQNrqTYYsT-ee5S__cROvjA1R6Z1100jgN4dWmeaZKBbQCXAg-0Q-UHEcS1yETsl1EYjbgluhDLPASc_Ke9XIm2l3yc6_1ceytpBbQLR3Phelx8ocKp-NPswGWjPkl7On516KytYaNENGPXMFC9ZTI8INCZ2feNdS7IyZd0yqebNUclDPuAlu1t2_C1SeuyOjY7YO_G4KMIOFH8aJ9K6jWMmKqraFwyZi56kTV1ZxTZudKOKeJOjv4Kbn9yEs1YweW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=dnUkFoKNLYMJ-kEZ7dcwWefejFIyRorlcE4dl9rSjQoa4X-owFFnlE4Fh0W_MauzpHKcbCutZnIRMt7PeEAQNrqTYYsT-ee5S__cROvjA1R6Z1100jgN4dWmeaZKBbQCXAg-0Q-UHEcS1yETsl1EYjbgluhDLPASc_Ke9XIm2l3yc6_1ceytpBbQLR3Phelx8ocKp-NPswGWjPkl7On516KytYaNENGPXMFC9ZTI8INCZ2feNdS7IyZd0yqebNUclDPuAlu1t2_C1SeuyOjY7YO_G4KMIOFH8aJ9K6jWMmKqraFwyZi56kTV1ZxTZudKOKeJOjv4Kbn9yEs1YweW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از پزشکیان پرسید که میخواید بمب اتم بسازید یا نه اونم میگه نهههه نههه اصلا،
بعد بهش میگه اگه بمب اتم نمیخواید چرا اورانیوم رو بردید زیر زمین ۶۰ درصد غنی کردید؟
گفت اونو که میخوایم رقیقش کنیم! یعنی غلیظ کردید که رقیق کنید؟! بمب نمیخواید بسازید؟!
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72266" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72265">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROqAPsN_vPouGQyLQdRSu1P081EYtSRuULd7yd9LLWaWdoLoTUYHzcq6Xm1O0EupPzqviiKP2YhAqDbe2ZMfKRi2IjiBQ8TBp0q6sj0_8RofM_YczPhne5NR-GKXCCuMvBtlxkcl0ZYxBkqux98yc-1PfHwDpNAZXDLqsQgMBYkjGtyd5BNCwZ6g9EmjeoZq-yHTqmIcSBEIDDvNXG-A8wuAtEGG7RCo6KsaRlFhnf_lEwZ35D5IIf-kFY8MZWuBcNuHDtyyRZE1nJG-0GGR2vAmSEcSsBJ2ubIlPO7ZnV11-O8vth_pHguDd9x0c-8TyLP9lpSVmXr4-3nvrqGcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران طرح جدید ۷ روزه‌ای را برای پایان دادن به جنگ پیشنهاد می‌کند؛
به نقل از نیویورک تایمز و به واسطه وزیر امور خارجه ایران:
• توقف کامل تمامی خصومت‌ها، از جمله در لبنان
• آزادسازی بیش از ۱۲ میلیارد دلار از دارایی‌های مسدودشده ایران توسط ایالات متحده
• لغو تحریم‌های نفتی
• پایان محاصره دریایی توسط ایالات متحده
• روز هفتم: بازگشایی تنگه هرمز
• آغاز فوری مذاکرات هسته‌ای
عباس عراقچی، وزیر امور خارجه، این چارچوب را علناً تأیید کرد اما جزئیات تمام شرایط را بیان نکرد و اظهار داشت که این طرح تا حد زیادی مشابه توافق ماه ژوئن است.
نکته مهم اینکه او نگفته است که عبور از تنگه هرمز برای همیشه رایگان خواهد بود؛ در چارچوب توافق ماه ژوئن، امکان عبور رایگان برای مدت ۶۰ روز پیش‌بینی شده بود تا در این فاصله درباره نحوه مدیریت آتی آن مذاکره شود.
ایران اعلام کرده است که آمادگی دارد این طرح را حتی پیش از موافقت واشنگتن اجرایی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72265" target="_blank">📅 14:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72264">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=lfowCFvWSfaVJsOyxu9-uz4IU8oOwrjdHNGSHawu6NBvlcpqnnR2waytU26ELVai56Buht7UUyPKY4ohPBVXPIFtfVR7Xc4O6pq346q7pxvZbwNgGHDqDMjuo68OgeG-_OKgRrnUQ1SVSdeMD7OkWbP2il5zGe-sfA0kfhB_lebcNT-aktUpshXCgKd5H77Xlnd6IlScj40eJ5XLXuPLKVpv1BJHj9Z0b4zHWRebNnww6cTdbOYh_PGtgZ3eZ21bossZd-Hylt9N3pp_nHMbvL51dxZen_dgaEZcHynvzltHMOxmvJ6A-wiXWM_vrunJFBJMT3nyPxdP3Ac2TthqeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=lfowCFvWSfaVJsOyxu9-uz4IU8oOwrjdHNGSHawu6NBvlcpqnnR2waytU26ELVai56Buht7UUyPKY4ohPBVXPIFtfVR7Xc4O6pq346q7pxvZbwNgGHDqDMjuo68OgeG-_OKgRrnUQ1SVSdeMD7OkWbP2il5zGe-sfA0kfhB_lebcNT-aktUpshXCgKd5H77Xlnd6IlScj40eJ5XLXuPLKVpv1BJHj9Z0b4zHWRebNnww6cTdbOYh_PGtgZ3eZ21bossZd-Hylt9N3pp_nHMbvL51dxZen_dgaEZcHynvzltHMOxmvJ6A-wiXWM_vrunJFBJMT3nyPxdP3Ac2TthqeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم #hjAly‌</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72264" target="_blank">📅 14:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72263">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وال استریت ژورنال:کشورهای حاشیه خلیج فارس در مورد تلاش‌ها برای از سرگیری مذاکرات ایالات متحده و ایران اختلاف نظر دارند.
عربستان سعودی و امارات متحده عربی از دولت ترامپ می‌خواهند که فشار اقتصادی و تحریم‌ها علیه تهران را حفظ کند، در حالی که قطر برای مذاکره، از جمله پیشنهاد توقف هفت روزه درگیری‌ها برای بازگشایی تنگه هرمز، تلاش می‌کند.
عربستان سعودی با اشاره به حملات به کشتیرانی خلیج فارس و اقدامات حوثی‌ها در یمن، استدلال می‌کند که ایران باید قبل از هرگونه توافقی با فشار بیشتری روبرو شود.
قطر و عمان از بازگشایی مرحله‌ای تنگه هرمز و یک راه حل دیپلماتیک حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72263" target="_blank">📅 13:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72259">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZzmViQVCqAzesoPE17IIqn9A6JGMCJzwxEYnyvSM7Hmk2jnNeslMEzjN71pJaoisYomKi3WHroB6KM43jrrzr2nezELN0K02Fq65fN3j2VfHGSS5mKIpcxtvW3Ne2LFgkumU3LYZneQdRDTCrkqCxYOX2hj7Slcio0W9Kc7_6ILzXmjaNQvKcGNx3V18c7yzASV49PPU1MaHbkUsn4dhYcvxO8rCSeLUy5AIy7BjKbHnCxe7DuiET5tl7Ktj2h98Ybi2BvUw1SK3skqZ9D_xuknEImqCg8y6l_okuoXIy4R-tpt7fO6S083P-KzfcDWt9C5IMGd2jhW_gOtGleq_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZVNIs29jpewDUHb_IXa7fs_atEjJynlIfPA2tRX7mkhrp3kgiH5o_rXfDsnCg--8lifaICFth-VFZqiD5jTTzrRpSmjR2a-eSpX4dcjv9VJSb5tA7fRo4S-yAoRrT1N1yFEvPT1OHzH64uQUkytIUK1uzSoJ9V0nyGWFKwqU3sedCKKo9x4riB3wM16gTihNzRrtzEr7o1QcZBblahKKCmrl926w4v-eSnj2-dAVf7Gl01UTps6LUXuFn3Y6ePlHcvlmTmik9-l_WuWKQnvh_8DaaVp9fgP9BpaekJOAFBYu7EnWEz9tQE-ufymZM_Nz33B23sBSVZXX9cDPNXROWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gjFnm2U0jRRrJ5avULf5DZNTUktOd9JYNIMiU90j_6k1YibnpVwcArAJz7e3w55CPloIVwLCwlPzPb5SV9jXgdG6y2Sq6gXMIWvRofx-rBhW969sCdyikpUffHYOlSfJNduZgAT0mc98m-3xARaeRcRabhYvaeWpMjmGSaT60ZTdKXm6h3ksIEOydHfyxLZQETzu3rpB3_9fnLTZo8A-eECBTt7dsWpm23fSRbdeLVKFwONIJTAQwga3s5LkiPcSO8YJ-m7YRL9Q0Q59TnEz5LDjwTGB44KMeMlxCubJgFtG9N1RPOKOyjkU9UE4yvg5ujvqpHLnpsPzntjwTSTtoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aopbI8R00m8duGMYPFkrv8mLqo-Vq36zq7c9CmQPjZpJi8K5wIMowTAMASX70Z9X5DqAJjF6JiLlARaSQMstQVCH23G0YOhTizEVzG2iA9a0SOVp52l8K81SW2lBuYz5kqTBwu3RYqAF1sDPmdUsBA2ISOxsuQmB-oJZwKuxiw6DfMxEspIkyJV8EcDiqbE3Ok5pVxWY_OqIudLWujwmoLLimjG9IopNltwcbtGHhUSLBorAyTIGOT5T8Rdzym1eMwFIKgrXawP2gr0_DeevUNJ6WKvEXh1C7nZc3fEUL5wFILJEdPwvQCuZS9nBKKFbO5ocgZjqZVwxCPp9-JULRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگولی ترین دانش‌آموز امسال معرفی شد
این دختر کوچولو به اسم
گندم
لقب کوچولو و کیوت‌ترین دانش آموز امسال رو از طرف مردم کسب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72259" target="_blank">📅 12:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72258">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72258" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72258" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72257">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X34z499UA6W5eWICMpDLf_hvc_rp3V3v1IjciMzi0BkkJNxOcV0nTXiiYGvDzxw5HIo549qVpr5krDhrq6GeBtBVrvTZeqkf8SFEkndPRrmaCxw1PXrNx-Ic13R1o_Ciskon4hLs1iU0T2VoHRnMP7xr-IBtEbEh9eP32wEaGCiCWwnjb2FzCOpVuJC1e_HkQWe3TkhIEWvqgWw7QyrGuHCA9WRVtKuLNqg634qVWxWcS-AqPUfz3jATKRt00MKdn5o65HrhUBuNmcAgJee6PGNsI1a_WAlzSxPgPvQgTI5uly969G5ZH0qC89VvkihyCM74fbrWX6ohafpjr16sBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72257" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72256">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtTT4vVi7jo9vPrydY_0MJ1DDlfM6nZg7uHBOlxn1E-msNv8RiW-V9WVh21bjPcwohhS4wzuiE0rvCXVIXS-dUGWel9qbbsJDpsOwtxX3PwgkB2tRt-hrYmeZqHFoe1uXLL0vGWpKFNHdm-V9unwDkbPBtMYgHKmQ5wnOqQqHq5VhZ5BAdYpEUIciHB41TI2sX1tEfgfWOtYbqlcUYyB9pWACfbILlf55mcitbW8plGWNGw1bALOj6t4B-KSjsZQri9wu4iOji0JjwiXmzO4Zm2cd7L2_wjRhbxfwKa5fSDwa0anzWyCYuiw9YG52h09Wak_rQBuwvjgpS9AzdOf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
مذاکره‌کنندگان در حال بررسی توافقی مرحله‌ای هستند که بر اساس آن، تهران در ازای کاهش محاصره اقتصادی ایران توسط واشنگتن، تنگه هرمز را بازگشایی خواهد کرد.
این مذاکرات با مانعی بزرگ روبروست، زیرا هر دو طرف خواهان حفظ اهرم فشار خود هستند: ایالات متحده کنترل فشار ناشی از تحریم‌ها را در دست دارد و ایران کنترل دسترسی به یکی از مسیرهای حیاتی انرژی جهان را.
ممکن است ایران در ازای دریافت امتیازات اقتصادی، از درخواست خود برای دریافت حق ترانزیت صرف‌نظر کند، اما همچنان خواهان حفظ کنترل اجرایی بر این تنگه است. کشورهای حوزه خلیج فارس با هرگونه ترتیبی که به ایران اجازه دهد از تنگه هرمز به عنوان اهرم فشار استفاده کند، مخالف هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72256" target="_blank">📅 12:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72254">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSsLa7t_QloWFs09jHFhrdM1KnGCVezu-c1pPyfK2hzCrcHAq5CYh7832wYRd-V_EjXCOXQPisnUx9SMF_8jYtAdEDxwydtB8JV_M6U9R-vO6uoPB0sYPbA77T8ZMxMbVq5poCwqvzWE1UUGbBpJ60FcSgqFP8VOea3eIl44yxoQ69wzWdBKBD2Gw6NBZcxnpGKOEjZoaYU7hk_Z5WjxcVjHqPM3ocC0YkVP3sEgrJ7XvIWeLWplLcbqprjz9OMAyMju6bQxsHBdtzUvT5ABXdwvgaOjwPmTJ29K7Xl3wkzBnpLX0i1WRqHrDxPj5kdQ1kZvFWhSmH44bd4l8h5kfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=Zp9hUgnPUyyAO5-wgm-uHuqrug5hWOkHSezjj9pAjyiIPwNWCFeMUaPN-IeEu4xIggwmLq354kZNEeSNUzhlMaaGHL5r7U5-_3ZfArVgtGh57FKs00L1rMZW5gKGxK5DQ2L1cZqsjw6z3KhC4Y7T6ZowNKhm8-n9PlxRLSBLDfdEsARbC2UXwIQ2E-GflXKzWnXYRulrSEmkGE4HhM8HQcybIFw6iVKBpBpINhyBKoVRaYHM8x0upmI37b2GnVX-2M0lLoR9vJs7dBzJ_e94nlgszsppmeVqMDb6K4hTyvImR169a0bQAjbGiqWBFOV0H69o7P1ihZY8gk_2d7btyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=Zp9hUgnPUyyAO5-wgm-uHuqrug5hWOkHSezjj9pAjyiIPwNWCFeMUaPN-IeEu4xIggwmLq354kZNEeSNUzhlMaaGHL5r7U5-_3ZfArVgtGh57FKs00L1rMZW5gKGxK5DQ2L1cZqsjw6z3KhC4Y7T6ZowNKhm8-n9PlxRLSBLDfdEsARbC2UXwIQ2E-GflXKzWnXYRulrSEmkGE4HhM8HQcybIFw6iVKBpBpINhyBKoVRaYHM8x0upmI37b2GnVX-2M0lLoR9vJs7dBzJ_e94nlgszsppmeVqMDb6K4hTyvImR169a0bQAjbGiqWBFOV0H69o7P1ihZY8gk_2d7btyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نایا:مقام‌های فرودگاه مانع سوار شدن مسافران به پرواز شرکت هواپیمایی معراج ایران از نجف به مشهد شدند. این هواپیما بدون مسافر در حال بازگشت است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72254" target="_blank">📅 11:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72253">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=bpyPcLj6oYBaihR0YZ2Sy4jiI14lVU7zhkKrrif9NgRkHBNapfFnmRW0tZnhhWizGYuOCxyaAnuEoU-dAKSWw2K5EpAtGIFLqQW-BbPj8iEjJOS27sZnXks5iBuA2jmTX3MxDVa7bg2UYpekFL2OELwtX2bucPmu1ryX3P1PWjyQWhlk-RhYNTYDo1eCzK1_r_uuT3Xuom-ICc5jwMqN-xa9349LoR2YMAeiVvh-OWOBaVlaFUW0J-Cp14UWXylEmptOl-xaz7bZ9ddYis8ZsWiIcXsX322Nifr9FuW-7xvPfXIQT8AeSLj_hckcUMzk-FxteQiYdDtNNBlSyq6K-rkNILD3B-fRKHr8gCkasTszDaDJaCxBcYZi88XheaOsT-57fSJHvP9sW_iaL2b6tLUgYpCBfBf2bdV_ekKs0TIN4oCVLRF1Addvy9M6c_hgMGwXPJipQeckoy3e8oRkz_GxYv1sP70h7jRIEVz5Q-KSzeOsQu4GcL1posp68t5Z9AWtNwj_m1kNgMSX1iGtq5e90cjY4dDVVsE5ZSyhwy4MgHq3502dF1mZDoGQqbOyumSk_hITz8BPwlK9Fx6tsMqMvG1xqYUgBNJ0PLhubWq-J8yGIjZXPgZyUfLSOS4FYsYEy1kiTDR6OPslYK_1deCjNmeL9424Rj9gaOaCjGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=bpyPcLj6oYBaihR0YZ2Sy4jiI14lVU7zhkKrrif9NgRkHBNapfFnmRW0tZnhhWizGYuOCxyaAnuEoU-dAKSWw2K5EpAtGIFLqQW-BbPj8iEjJOS27sZnXks5iBuA2jmTX3MxDVa7bg2UYpekFL2OELwtX2bucPmu1ryX3P1PWjyQWhlk-RhYNTYDo1eCzK1_r_uuT3Xuom-ICc5jwMqN-xa9349LoR2YMAeiVvh-OWOBaVlaFUW0J-Cp14UWXylEmptOl-xaz7bZ9ddYis8ZsWiIcXsX322Nifr9FuW-7xvPfXIQT8AeSLj_hckcUMzk-FxteQiYdDtNNBlSyq6K-rkNILD3B-fRKHr8gCkasTszDaDJaCxBcYZi88XheaOsT-57fSJHvP9sW_iaL2b6tLUgYpCBfBf2bdV_ekKs0TIN4oCVLRF1Addvy9M6c_hgMGwXPJipQeckoy3e8oRkz_GxYv1sP70h7jRIEVz5Q-KSzeOsQu4GcL1posp68t5Z9AWtNwj_m1kNgMSX1iGtq5e90cjY4dDVVsE5ZSyhwy4MgHq3502dF1mZDoGQqbOyumSk_hITz8BPwlK9Fx6tsMqMvG1xqYUgBNJ0PLhubWq-J8yGIjZXPgZyUfLSOS4FYsYEy1kiTDR6OPslYK_1deCjNmeL9424Rj9gaOaCjGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های یکی از خبرنگارای رسانه های فارسی خارج از کشور با معاون عراقچی، کاظم غریب آبادی:
خبرنگار:
ترامپ‌ گفته میخواد جمهوری اسلامی رو نابود کنه ولی هنوز به توافق فرصت داده، فکر میکنید چقدر فرصت دارید؟
غریب آبادی:
ما با رسانه های فارسی زبان خارج از کشور که موافق مردم کشورشون نیستن مصاحبه نمیکنیم
خبرنگار:
ولی با ⁦CNN⁩ رسانه ی آمریکایی که رهبرتونو کشته مصاحبه میکنید
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72253" target="_blank">📅 10:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72252">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=URXZaldr1oQutpmakKrFbcBoV3XMjvclV5H0aIQRDlHcutVm8GfzLcubSDu-ytZjJ5kvhUZt_3TMPFsU_dGti-bEviDcu3H8z8ja22sVmEHWF3jqhUIHgUDEnL0yJvSepEoSnaBfAZnqNwBqejebXlH9D1mti5zAems3MX0ow178N_9q-97p80oEe3pw3rTHpyweq1uoef0BJSEt44j55ZeMESmjb82Qk75_KlXg1rBJ7oHzXgCe5cuixfK9VQYMlv2mOj9bRGfaMDH88ty2nslOXtQ1ukyTsx7cSzMnvhxH6AcIXjJN4NMS22nLQPwgZ00QbymVOji5n_flAqgdxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=URXZaldr1oQutpmakKrFbcBoV3XMjvclV5H0aIQRDlHcutVm8GfzLcubSDu-ytZjJ5kvhUZt_3TMPFsU_dGti-bEviDcu3H8z8ja22sVmEHWF3jqhUIHgUDEnL0yJvSepEoSnaBfAZnqNwBqejebXlH9D1mti5zAems3MX0ow178N_9q-97p80oEe3pw3rTHpyweq1uoef0BJSEt44j55ZeMESmjb82Qk75_KlXg1rBJ7oHzXgCe5cuixfK9VQYMlv2mOj9bRGfaMDH88ty2nslOXtQ1ukyTsx7cSzMnvhxH6AcIXjJN4NMS22nLQPwgZ00QbymVOji5n_flAqgdxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس سنا با ۵۰ رأی مخالف در برابر ۴۹ رأی موافق، قطعنامه‌ای را که هدف آن محدود کردن اختیارات جنگی ترامپ در قبال ایران بود، رد کرد.
چهار جمهوری‌خواه — شامل سوزان کالینز، لیزا مورکوفسکی، رند پال و تام تیلیس — در حمایت از این قطعنامه با دموکرات‌ها همراه شدند، در حالی که جان فترمن تنها دموکراتی بود که با آن مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72252" target="_blank">📅 10:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72251">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhHndGQPgC_AJviyHpKrQ4WDF8Vnp17ssYBvPonBRp71rR0SWJEck9DNWcgKMmvi1UGz3MKLVKUimwjpBrgj6GkS5qwylKa7m0DhDmlhGMVDQ_QYJxpT-ej8BwCTP5o08k1GyQxgDvfyilJm9LeSc-cPy9MKKvLDx8ECN3rAB7wtRSLGO69c4PmWnj3I9av1VEa5_qyq2f5YAsumd1nhvlFZn6gLz0RcLTKv48KUDfi6AQ2ReqUEp78dBH2P02i9s1pkxsfDyoQ1ItobFSM6mQ2Fz0K7f6AqVnQSRk4mBZmgF1Ezosx1_rfpx85cZYjLozbowPEEPbm2J_Ak1Fi95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی‌ نیوز:
مسعود پزشکیان، رئیس‌جمهور ایران، اظهار داشت که تهران خواهان احیای توافق آتش‌بس خود با ایالات متحده پیش از انتخابات میان‌دوره‌ای ماه نوامبر است.
پزشکیان گفت: «ما نمی‌خواهیم کار به انتخابات میان‌دوره‌ای بکشد. ما خواهان آن هستیم که آمریکایی‌ها پیش از انتخابات میان‌دوره‌ای به تفاهم‌نامه بازگردند.»
پزشکیان همچنین اعلام کرد که ایران برای بازرسی از تأسیسات هسته‌ای خود «آمادگی دارد» و هرگونه تلاش برای ترور ترامپ یا خانواده‌اش را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72251" target="_blank">📅 09:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72250">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72250" target="_blank">📅 09:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72249">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=M3BzZw25-1mRr31yKRQ6-Pa5c0iHq0FidFyyoRmcQNh9T0stvES2Y65xaJwj4snCIKR3gChxJ7KT4E-bKp39RRJJVRTALCW9SF4hkUnex0F8lDJhFk649aoFbfNYDa60OGf1LlPpp1HGN2_k2zdTu2xS09YY6OINyI-WlMBEScszOGOcVJYQTS5vAW3cxYVsTGPvESjph4Yh0wXosWlCsoIyWM7gr1qgq60ya43XiWWWaYSRJen17HtGeAkUPOoY1Pww2J2De5c1cKyv5QN6lx4WDUALmAMgxdYixZT-9ilGKD8u51qWkEhzHByTiKQbgE3j17mArIEvltSbXsgq6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=M3BzZw25-1mRr31yKRQ6-Pa5c0iHq0FidFyyoRmcQNh9T0stvES2Y65xaJwj4snCIKR3gChxJ7KT4E-bKp39RRJJVRTALCW9SF4hkUnex0F8lDJhFk649aoFbfNYDa60OGf1LlPpp1HGN2_k2zdTu2xS09YY6OINyI-WlMBEScszOGOcVJYQTS5vAW3cxYVsTGPvESjph4Yh0wXosWlCsoIyWM7gr1qgq60ya43XiWWWaYSRJen17HtGeAkUPOoY1Pww2J2De5c1cKyv5QN6lx4WDUALmAMgxdYixZT-9ilGKD8u51qWkEhzHByTiKQbgE3j17mArIEvltSbXsgq6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جناب نخست وزیر پیامتون برای مردم ایران چیه؟؟
بی‌بی نتانیاهو: ما با شما هستیم نا امید نشید
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72249" target="_blank">📅 08:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72248">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">با این جوابایی که پزشکیان به خبرنگار داد باید منتظر موج جدیدی از حملات طرفداران افراطی جمهوری اسلامی و تندرو ها به پزشکیان و دارو‌دستش باشیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72248" target="_blank">📅 07:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72247">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پزشکیان:
- انصارالله مسئول اقدامات خود است و از ما دستور نمی‌گیرد.
- ما اورانیوم غنی‌شده ۶۰ درصد را در چارچوب قوانین بین‌المللی و پیمان منع گسترش سلاح‌های هسته‌ای (NPT) واگذار خواهیم کرد.
- ما به تمامی تعهدات خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای پایبند خواهیم بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72247" target="_blank">📅 07:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72246">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=PbCK6nDK34WUecgYr-OLmsWSLAKwWTzoZkHLptvGbjAii2OVB071bQrNuNhEpifsQjx41rGJ0Lo4vum7h1fs8cYHWtO_XDjxB0FhZ2QWr2E_aLyzdIQaIF8mwVc8QU2rue63pzLbGyO2cBX13b0nsrog1vc4MUry0-GiJ6Th01PPjFMQt0IVGQ1zSQb0Jq5mNcSkQumG3PPnXS4bLUMnK8EKV6hnjMTaYiHifi0687FnsbrBUHR2StkMlZofvpk6edhhH817MU4xnXRboKzA2-a6cI3F04Uiim3k67SIrMFAFIG9hWT2Qv5dWsthbyOcWQ4AGOtLiAIQd9VLQJQa7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=PbCK6nDK34WUecgYr-OLmsWSLAKwWTzoZkHLptvGbjAii2OVB071bQrNuNhEpifsQjx41rGJ0Lo4vum7h1fs8cYHWtO_XDjxB0FhZ2QWr2E_aLyzdIQaIF8mwVc8QU2rue63pzLbGyO2cBX13b0nsrog1vc4MUry0-GiJ6Th01PPjFMQt0IVGQ1zSQb0Jq5mNcSkQumG3PPnXS4bLUMnK8EKV6hnjMTaYiHifi0687FnsbrBUHR2StkMlZofvpk6edhhH817MU4xnXRboKzA2-a6cI3F04Uiim3k67SIrMFAFIG9hWT2Qv5dWsthbyOcWQ4AGOtLiAIQd9VLQJQa7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس‌نیوز:
آژانس بین‌المللی انرژی اتمی می‌گوید شما ۴۴۰ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار دارید. این اورانیوم کجاست؟
پزشکیان:
آمریکا مدام می‌گوید ما همه‌چیز را نابود کرده‌ایم. خب، این ادعا یا درست است یا نادرست؛ کدام‌یک است؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72246" target="_blank">📅 07:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72245">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=bjCzm3P5wYeFND59TYaDXY9iRJuXXn-yYK2UStsdd05SPO3sJZ0y-PMOtW5STYpPkwtDr51LKleLJqgXgT5aTbypVi1GT2uCg5rnck6I1lUsNuBNhmrYgH6kxv1afVQcEsSc45kMDZI08ZE0Votr6lhnleDs5o89ztHuPdhbu0HAGWQtSr1q4kisIpBEzKvp6PvI9dGEPVtirVYIA4sRWQf6AwfkdvlRF_HkYD5YJ-yi1fGCj8rgnOTDtL7VSitiOhxwQeYtg8xZEACzNfh0xUcXsaHzk_ILj1UVKsgqKTYq6jAqrq46AyX4NWEwQlAtAqYhpqPvlQHsVST4_HVZV6V3Y5a6X0jM42i8LvkER5EYPmZ8rtGIjjhUpPLPQGFSbDO3sIR-lncPhYYn10h3muUuJpUnrCxMBHJynX3yuGIttRwlWF_gknplCHu-apYwTYR9o4wW-nzQ4TOb1rNvgenaMs_oErpllnstzp8AfEXXgbmjKZlzKYtoHEOmzVrLUkX5FGKl03ebV3sLl0hL6c7226p2Whc7l-PvYmYLiedMFmWSD05X3ZcoDckQC2-oxuxGhyK76bpCKWJUmzkEyW1hVghBvpgeI8pAf5P-5sy6O4zYPlbb7RrT5vYpxIRsoH_dvzgDVX8hCVCdotPCvW5_iY5dxSqsPLy350YWECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=bjCzm3P5wYeFND59TYaDXY9iRJuXXn-yYK2UStsdd05SPO3sJZ0y-PMOtW5STYpPkwtDr51LKleLJqgXgT5aTbypVi1GT2uCg5rnck6I1lUsNuBNhmrYgH6kxv1afVQcEsSc45kMDZI08ZE0Votr6lhnleDs5o89ztHuPdhbu0HAGWQtSr1q4kisIpBEzKvp6PvI9dGEPVtirVYIA4sRWQf6AwfkdvlRF_HkYD5YJ-yi1fGCj8rgnOTDtL7VSitiOhxwQeYtg8xZEACzNfh0xUcXsaHzk_ILj1UVKsgqKTYq6jAqrq46AyX4NWEwQlAtAqYhpqPvlQHsVST4_HVZV6V3Y5a6X0jM42i8LvkER5EYPmZ8rtGIjjhUpPLPQGFSbDO3sIR-lncPhYYn10h3muUuJpUnrCxMBHJynX3yuGIttRwlWF_gknplCHu-apYwTYR9o4wW-nzQ4TOb1rNvgenaMs_oErpllnstzp8AfEXXgbmjKZlzKYtoHEOmzVrLUkX5FGKl03ebV3sLl0hL6c7226p2Whc7l-PvYmYLiedMFmWSD05X3ZcoDckQC2-oxuxGhyK76bpCKWJUmzkEyW1hVghBvpgeI8pAf5P-5sy6O4zYPlbb7RrT5vYpxIRsoH_dvzgDVX8hCVCdotPCvW5_iY5dxSqsPLy350YWECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
خودِ آقای ترامپ اعلام کرد که آمریکا این افراد را تجهیز و مسلح کرده بود تا حکومت ایران را سرنگون کند.
اطرافیان نتانیاهو اعلام کرده بودند که نیروهایی از استان‌های کردستان و بلوچستان به مراکز کلان‌شهری نفوذ خواهند کرد تا حکومت را ساقط کنند.
آن‌ها تصور می‌کردند که این ماجرا سه روزه تمام می‌شود و حکومت سقوط می‌کند؛ اما حکومت استوار ماند و منسجم‌تر و متحدتر شد.
حتی کسانی که به دلایل گوناگون در برابر حکومت ایران ایستاده و با ما مخالف بودند، اکنون از ایران حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72245" target="_blank">📅 07:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72244">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=MvkfAKZs3Y8s8io_FEPTbvdqG62NH5oZGfIqD1f9FGmNoS2KXaCpjxOxdiU5SOa_eiJl0YVVmuV2sD5Hey4lHpr1jW91u7IQANwSb6cU2qFlHSfFDIP8X8l9zxXPLOT7Lz5fjI5jYrGzlekdN8bJ7MoczAHjf4-m86-HVAX5_lQSOZZCeeP-HTi_joPh-AhQNNaExZ5PjvRB2at-smkiQffF_alfCdp61i3g-KtkciTnaHLcxRn1_C32TwtbMeKOB07L5qMvUVcYnpXHktp6-NHIxBMOiHpx_cpAvdf-yQtEwh9uGz4A9ajZ-ryKSj9uyc3YTOackJstEe7EjBxjaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=MvkfAKZs3Y8s8io_FEPTbvdqG62NH5oZGfIqD1f9FGmNoS2KXaCpjxOxdiU5SOa_eiJl0YVVmuV2sD5Hey4lHpr1jW91u7IQANwSb6cU2qFlHSfFDIP8X8l9zxXPLOT7Lz5fjI5jYrGzlekdN8bJ7MoczAHjf4-m86-HVAX5_lQSOZZCeeP-HTi_joPh-AhQNNaExZ5PjvRB2at-smkiQffF_alfCdp61i3g-KtkciTnaHLcxRn1_C32TwtbMeKOB07L5qMvUVcYnpXHktp6-NHIxBMOiHpx_cpAvdf-yQtEwh9uGz4A9ajZ-ryKSj9uyc3YTOackJstEe7EjBxjaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما هرگز به مردم خودمان حمله نمی‌کنیم.
برت بایر (از شبکه فاکس):
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی علیه ما اقدامات تروریستی انجام داد؟ چه کسی مدارس ما را هدف قرار داد؟
بایر:
متوجه هستم، اما در روزهای ۸ و ۹ ژانویه، قطعاً نیروهای امنیتی شما شهروندان ایرانی را کشتند.
پزشکیان:
خیر اصلا اینگونه نبود.آنها تروریست هایی بودند که توسط آمریکا و موساد و کرد‌ها مسلح شده بودند.ما به مردم عادی آسیبی نزدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72244" target="_blank">📅 07:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72243">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=L20PWS_fEFVkx4L424yeOys9Eraqi2h1jxtrz3rTzhYFyOSFll8UyOjWMAZ2m69a6_DLkjBvxMYZzASMto8Pf74D4rLXuDozdY3N0Pqk3EsFPGO7zMn9Nk9QoZhdnjQ8qOTgDSs3fh2CSIRaAbxG17RzCEbTsy26s0yCjixRfjUwrYUfoiznVuzJAuYT846AIPbCmkG61s2SplKeR6YExf6PzuJGbugGd0qTlmFbVBP9VccomanYV-CX_0rHpT2p84KDx-14kAr2HU13-syqwKDu2yUwUJmVjo-8cpBdiQ88zsew4mJywiWN8kwJrFPWZyW-jaaxMYNtiZ_yfA-NPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=L20PWS_fEFVkx4L424yeOys9Eraqi2h1jxtrz3rTzhYFyOSFll8UyOjWMAZ2m69a6_DLkjBvxMYZzASMto8Pf74D4rLXuDozdY3N0Pqk3EsFPGO7zMn9Nk9QoZhdnjQ8qOTgDSs3fh2CSIRaAbxG17RzCEbTsy26s0yCjixRfjUwrYUfoiznVuzJAuYT846AIPbCmkG61s2SplKeR6YExf6PzuJGbugGd0qTlmFbVBP9VccomanYV-CX_0rHpT2p84KDx-14kAr2HU13-syqwKDu2yUwUJmVjo-8cpBdiQ88zsew4mJywiWN8kwJrFPWZyW-jaaxMYNtiZ_yfA-NPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
رئیس‌جمهور آمریکا اعلام کرد که ما تروریست هستیم.
اما در واقعیت، همه به‌راحتی می‌توانند تشخیص دهند که ما قربانی و هدف تروریسم بوده‌ایم؛ با این حال آن‌ها می‌گویند: «نه، ما چنین کاری نکردیم.»
آن‌ها حقیقتی آشکار را انکار می‌کنند، اما در عین حال ما را به چنین اقداماتی متهم می‌سازند.
ما خواهان زندگی در صلح و آرامش در منطقه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72243" target="_blank">📅 07:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72242">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=ZyPRvJtTDqrqgN3MOWXGmFrt8QAuPwCoNZfbHbacK2zYylKqrEpviqYxN1gVCVTfciuuqUNorX1DGEbIRzBtzyzSGmsJQeuiZHw8tIyNLHbxVhF7c1Yx7u9TIpj__pnLI-0Vf6kK3LTOhCuztRlxVCbN1Xr0ImXhHXMOc0aR242dnSLcTysn0HlkaLTU4cgpFfvV7Yriudy0z5jJiNrBb85huVHP84qtCiYQ-7b454tTsEhr6RPUeo3HwTwKp2fV2ShHWnCQJeNw7IxSq85jAha-Jl6Ayncvk27RiMFpxEDxpBdNxE7SfCHcCNNc7EFi2Cdd7dOXJQmUwKJ0lnCOYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=ZyPRvJtTDqrqgN3MOWXGmFrt8QAuPwCoNZfbHbacK2zYylKqrEpviqYxN1gVCVTfciuuqUNorX1DGEbIRzBtzyzSGmsJQeuiZHw8tIyNLHbxVhF7c1Yx7u9TIpj__pnLI-0Vf6kK3LTOhCuztRlxVCbN1Xr0ImXhHXMOc0aR242dnSLcTysn0HlkaLTU4cgpFfvV7Yriudy0z5jJiNrBb85huVHP84qtCiYQ-7b454tTsEhr6RPUeo3HwTwKp2fV2ShHWnCQJeNw7IxSq85jAha-Jl6Ayncvk27RiMFpxEDxpBdNxE7SfCHcCNNc7EFi2Cdd7dOXJQmUwKJ0lnCOYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما تا آخرین لحظه به مقاومت ادامه خواهیم داد.
بله، قطعاً مشکلات اقتصادی داریم؛ اما برای بقا، از هر سختی‌ای عبور خواهیم کرد و ایستادگی خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72242" target="_blank">📅 07:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72241">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=H3CSXcOCZPdNbMVcBRmq5jfpn-rLJNFkIOUH3V8W0XHI3ZAcqwWLiA05rnfAJFPp7uUxqdaNaYpRv9sh7DdKAroNUq4SHRsph6AHxhAaL6-FKZmPVagCYY32gr582lR21mJZt6ZiJ1Fvz7FOyS04FDeArrHjGljZPLrJfMhO4R310d97MTHS-WIoAUo8EeouHlLUGfZobmoNSbuBNoQ2pwXDNudGwtx2nIUFHpCQN8Naj03L1PGUjj4Hdf5RfGGb5vZpWk66ZH0-wtBkAlzgCHwnzzbSmUzAldsOHIqUlu9vZ4GpzOgic789yAN5ys6bk5kYGyqP7W10drR4bWWUWH0Clufo3zhcOpMQvTfOcwOR6QUTePbc5v_Y_Tecggut2cJshPuVqjhkNN4DQvk-FeN1iFSVdrxXJqSem5usGAJPRh5RmTtQk20AAsoGBJem3VAU0qnGmUJUYWdrhw07GVP0qVM1Xks8xQuwVE0Xt1WV5vUHsFvZ0X_tauTNWoFtDmFmW-rWxTf3l0tyQfSmI6Ubnk96ZiuXmajccZOvPvSPtqBxhwTvATUFnHizhIG_ELwG-kcThOoE16XuaJfu7xxdU3qVk6_ry2WqC8AiAr9MILGeouGy3kd7uO7hBgZ1_20qxJowQGtUMumRhq8DTmmuZA7AavHUvO0Nab8KTj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=H3CSXcOCZPdNbMVcBRmq5jfpn-rLJNFkIOUH3V8W0XHI3ZAcqwWLiA05rnfAJFPp7uUxqdaNaYpRv9sh7DdKAroNUq4SHRsph6AHxhAaL6-FKZmPVagCYY32gr582lR21mJZt6ZiJ1Fvz7FOyS04FDeArrHjGljZPLrJfMhO4R310d97MTHS-WIoAUo8EeouHlLUGfZobmoNSbuBNoQ2pwXDNudGwtx2nIUFHpCQN8Naj03L1PGUjj4Hdf5RfGGb5vZpWk66ZH0-wtBkAlzgCHwnzzbSmUzAldsOHIqUlu9vZ4GpzOgic789yAN5ys6bk5kYGyqP7W10drR4bWWUWH0Clufo3zhcOpMQvTfOcwOR6QUTePbc5v_Y_Tecggut2cJshPuVqjhkNN4DQvk-FeN1iFSVdrxXJqSem5usGAJPRh5RmTtQk20AAsoGBJem3VAU0qnGmUJUYWdrhw07GVP0qVM1Xks8xQuwVE0Xt1WV5vUHsFvZ0X_tauTNWoFtDmFmW-rWxTf3l0tyQfSmI6Ubnk96ZiuXmajccZOvPvSPtqBxhwTvATUFnHizhIG_ELwG-kcThOoE16XuaJfu7xxdU3qVk6_ry2WqC8AiAr9MILGeouGy3kd7uO7hBgZ1_20qxJowQGtUMumRhq8DTmmuZA7AavHUvO0Nab8KTj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ترامپ مدام می‌گفت «می‌خواهم برای مردم ایران هدیه‌ای بیاورم»، اما هدیه‌ای که آن‌ها برای ما آوردند، موشک‌های هدایت‌شونده، تسلیحات سنگین و ویرانی بود.
آنچه آن‌ها واقعاً به دنبال آن هستند، دامن زدن به وقایعی در کشور است که زمینه را برای فروپاشی نظام، جامعه و دولت فراهم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72241" target="_blank">📅 07:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72240">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=HG7JCt0pHXlYAWYX_jewmPNwL32rKgI0tqBd0OiU9Sc3Ro8sTInSdHIrVEOb-EsnvGuMiH7Ie-W8glayRB3YV9dfLjkkLHoQ8UuN3oFvlH2pPZkf7DnjQAMr7ug0-AcQFJR_QSLX33Sx0DS-kEf8Ll_T4qRYug7Fce8UPSj-AFwLxHg7XG2fQHzqnGPcflfr6tAaXPoRTh1QQxvgccI7rAmtcRZYeZTl8eCX-O1z5_d4Ac24vloaOVnW1-S0TEXpvTtFReNPLDeVbAZGSkX5O6mPT209fpPqTrRyR4YRb7N1WjnzHgUnvQY_lVJGC8tFXhMDHMB1_04wk40VnLxyDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=HG7JCt0pHXlYAWYX_jewmPNwL32rKgI0tqBd0OiU9Sc3Ro8sTInSdHIrVEOb-EsnvGuMiH7Ie-W8glayRB3YV9dfLjkkLHoQ8UuN3oFvlH2pPZkf7DnjQAMr7ug0-AcQFJR_QSLX33Sx0DS-kEf8Ll_T4qRYug7Fce8UPSj-AFwLxHg7XG2fQHzqnGPcflfr6tAaXPoRTh1QQxvgccI7rAmtcRZYeZTl8eCX-O1z5_d4Ac24vloaOVnW1-S0TEXpvTtFReNPLDeVbAZGSkX5O6mPT209fpPqTrRyR4YRb7N1WjnzHgUnvQY_lVJGC8tFXhMDHMB1_04wk40VnLxyDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
اگر دولت فعلی آمریکا بخواهد در چارچوب حقوق بین‌الملل به توافق برسد، بسیار خب.
اگر نه، چه پیش از انتخابات باشد و چه پس از آن، برای ما چه تفاوتی دارد؟
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72240" target="_blank">📅 07:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72239">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=arko8QocafeTC_ZLWRQ9yy4ZdqE-QV7lH2qAMPVGDXrOyB4Eh0XKkquDZtHB_d20Pd8x2OxBy7oiE3MxlpbgQgbs_AhPvqKRZmTuQd7FCcKbtBFZMOFntxmQepsORZC6seIA32PpG2FTU48ShukWYrxXAmZEC3lyAZT2c3xThyHTSkwMzJ4RaixFGAPpSieF_bsWTSHx3TZfilqhtkQxQJJMuyCVUSHsGKtC9nBztDZIt1tRzkA6gj9r3u35oGmXzUbjNN2NbHDl1Hk94ISayXikuTwI2W33gym1Ap2vx9J6RPvXNvvMRaLtfKcqz4TWEVLE5dvfgYw3GLvEZW_8ijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=arko8QocafeTC_ZLWRQ9yy4ZdqE-QV7lH2qAMPVGDXrOyB4Eh0XKkquDZtHB_d20Pd8x2OxBy7oiE3MxlpbgQgbs_AhPvqKRZmTuQd7FCcKbtBFZMOFntxmQepsORZC6seIA32PpG2FTU48ShukWYrxXAmZEC3lyAZT2c3xThyHTSkwMzJ4RaixFGAPpSieF_bsWTSHx3TZfilqhtkQxQJJMuyCVUSHsGKtC9nBztDZIt1tRzkA6gj9r3u35oGmXzUbjNN2NbHDl1Hk94ISayXikuTwI2W33gym1Ap2vx9J6RPvXNvvMRaLtfKcqz4TWEVLE5dvfgYw3GLvEZW_8ijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ما هرگز به دنبال جنگ نبوده‌ایم و نیستیم. من عمیقاً معتقدم که انسان‌ها نباید موجب مرگ انسان دیگری شوند.
قرار است ما موجودات برگزیده خلقت باشیم. وقتی می‌توانیم مسائل را از طریق گفتگو حل‌وفصل کنیم، نباید به کشتن یکدیگر متوسل شویم.
اما با اقداماتی که اسرائیل انجام داده، آن‌ها این جنگ را به ما تحمیل کرده‌اند.
با این حال، ما خواهان ادامه آن نیستیم. این آمریکاست که باید تصمیم بگیرد آیا می‌خواهد به این وضعیت پایان دهد یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72239" target="_blank">📅 07:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72238">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f631e90489.mp4?token=LdDQ2Xu7VxtUb8_9m904YtHNpVb6CUVNkdQP-WWFG_D68fybiai5bI1dvCaybuziZ1rFFPkWwyH3VYVXPKqqNcsgT8W_zDbP_8UTZtgcbhscCryMJrfTb9MkSSmyoDv2QlToQjSqMI92jfm7exORuir_TxbDJAWZm-y3fbJFhyd47PlrtwrmHUeB_FJcQl7y1kGBYmgI537EH-rigAjZSEH09of2kmvEtvK9cuacOx7jB-O2aNcx7ZcQK49qNLLJ1BwNCX9RcdZ79FdvvlzQ6pXMvPLinTTtqB0Ynn_Knktk5WD3M6eYCXnpA2qejfzdLMMVJMEJGdF4sTgq0c4HSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f631e90489.mp4?token=LdDQ2Xu7VxtUb8_9m904YtHNpVb6CUVNkdQP-WWFG_D68fybiai5bI1dvCaybuziZ1rFFPkWwyH3VYVXPKqqNcsgT8W_zDbP_8UTZtgcbhscCryMJrfTb9MkSSmyoDv2QlToQjSqMI92jfm7exORuir_TxbDJAWZm-y3fbJFhyd47PlrtwrmHUeB_FJcQl7y1kGBYmgI537EH-rigAjZSEH09of2kmvEtvK9cuacOx7jB-O2aNcx7ZcQK49qNLLJ1BwNCX9RcdZ79FdvvlzQ6pXMvPLinTTtqB0Ynn_Knktk5WD3M6eYCXnpA2qejfzdLMMVJMEJGdF4sTgq0c4HSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
یکی از مشکلاتی که با آن مواجه هستیم، مسدود بودن منابع مالی ما در چین است.
ما حتی نمی‌توانیم پول خود را از کشوری که به آن کالا صادر کرده‌ایم خارج کنیم، چه برسد به اینکه بخواهیم از آن وجوه برای پرداخت به طرفی دیگر در گوشه‌ای دیگر از جهان استفاده کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72238" target="_blank">📅 07:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72237">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=oNSXA04aivnT-_Q8Oe4n9NQcxdf_JEYvV_W3s8JjueZTt0E5fqLtczR1X_F31a2Q2w1rL4md-M4BsuLa-CWrdXV1VqbI3CgmjR8oV4wAvAODeiwU3gWTRHkgXaMENOTTZEQxhPdyDbDP3U1y8TpvVHkcyI8O9EAfX5koTHYofUMMRO8nE98Od_eAflBOozNB9dbG-DvSrVB4ozOQdvuRsP3RpvnPyofrWDCgE2kvs1DwoGwiIaEjm1QzCQwPKEs_RTZlaDbIIdfVzQHs-9m8cFz-9W6kH1V9UXpWbYNV3X6nFQ1qcFt14T7BTxZf5yj9jEtplQn02ej5OPtRakcv4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=oNSXA04aivnT-_Q8Oe4n9NQcxdf_JEYvV_W3s8JjueZTt0E5fqLtczR1X_F31a2Q2w1rL4md-M4BsuLa-CWrdXV1VqbI3CgmjR8oV4wAvAODeiwU3gWTRHkgXaMENOTTZEQxhPdyDbDP3U1y8TpvVHkcyI8O9EAfX5koTHYofUMMRO8nE98Od_eAflBOozNB9dbG-DvSrVB4ozOQdvuRsP3RpvnPyofrWDCgE2kvs1DwoGwiIaEjm1QzCQwPKEs_RTZlaDbIIdfVzQHs-9m8cFz-9W6kH1V9UXpWbYNV3X6nFQ1qcFt14T7BTxZf5yj9jEtplQn02ej5OPtRakcv4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در گفتگو با خبرنگار فاکس‌نیوز:
هر کس بخواهد اعتراض کند، کاملاً حق انجام این کار را دارد.
ما با بسیاری از این کارشناسان گفتگو کرده‌ایم. اما تبدیل اعتراضات به ابزاری برای تقابل (مسلح کردن معترضان)، مقوله‌ای کاملاً متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72237" target="_blank">📅 07:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72236">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72236" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72235">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE5q7NW_YdqlpVuoyXJoKuweQCn7dtwZHRhisMbq3mNVWtzuDpKaSfgbgy7uyQ6Gj6Z3Kv3AlqBEjdAnQ6_T-LlrByRIavQF47ETstqtPddOXYYUF9FWsYhdfLbyw3l3S9qVp1rZ3GizIfhAMjqJuzUwcJqAU837rcgnC5hBBsUxd_gSHVievrYdhNgmX9gNuQ0e4pVGf8e5EcxaRmo5PKFK8biw1ljt2csaoWm1S1zGR8jB4kpJFZezg5yrG7c2zZ-qVD7f1ICVr0DR-i_aqa3GtzFVq0hbpKET2tcgk6Gk15qMhXEHRFsQI2jx3a0ck270PwaPqI0IXobgekkAxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72235" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72234">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25201994ac.mp4?token=h0ei17YewjCHi9qAgqM8yCHXAOtygLWjpgJSQO_QLzcyAyUUcZ8ZvESBoVaBbDqT7dRo8TykfNnBAGjzDYegx0ZRDjZNh2UxfPeQLnd9CKF7T0vixQ729qmileaEjY7v8Wjgg0iBINqwdH5YWdkPs_I-jeyApl7AoddcOOCOFVWtQugiM8Lzbu3_PRNeTqKa0CZGrWGVQBaG7OfhhpNoxdoxDiWr32rCUIr9WFSUszYxoVZIcJv0gX0uNBjxb1tboXK7WG5TysnjuVdrilr3XJ1ivUron6haBJCwnSavc3Fv7cTswvhNZEYuz-jWiwDa6C41H4Tj6lSMpgLO4jNC5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25201994ac.mp4?token=h0ei17YewjCHi9qAgqM8yCHXAOtygLWjpgJSQO_QLzcyAyUUcZ8ZvESBoVaBbDqT7dRo8TykfNnBAGjzDYegx0ZRDjZNh2UxfPeQLnd9CKF7T0vixQ729qmileaEjY7v8Wjgg0iBINqwdH5YWdkPs_I-jeyApl7AoddcOOCOFVWtQugiM8Lzbu3_PRNeTqKa0CZGrWGVQBaG7OfhhpNoxdoxDiWr32rCUIr9WFSUszYxoVZIcJv0gX0uNBjxb1tboXK7WG5TysnjuVdrilr3XJ1ivUron6haBJCwnSavc3Fv7cTswvhNZEYuz-jWiwDa6C41H4Tj6lSMpgLO4jNC5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
🇮🇷
🇮🇱
🌟
نماینده اسرائیل در سازمان ملل دستگاه «استارلینک» را به نماینده اعزامی تهران داد و درباره «کمک به مردم ایران برای سرنوشت و آزادی با این دستگاه» صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72234" target="_blank">📅 01:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72233">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=K9CWWblKWlLL3NcVocM-eFKl7HAE0R4_-sapiABisGq8sSmnBuUqBPIjwP7JWkFB1xx_YqTi76rhyt3orPiu1CAyIk4mfDmkvDSLyHaQFLKDvxaWPx2tAwfVwLAVuuWEdTMxjL46RWj3prCLe3mupog7_bl0Z1W_FNjgX_HbaOkc58tGnYnFNdG-iS5sojKU4mFQFhJOanh5OA_AV9QPXzCWRgbjuwJ9c6u6oi9OplT2HdfUZLMHZ5KnyM8vP2wi_WosI3zt2XDk5JDS_Xss2ecbhXc9t55IrNoXEhvVFYQqVkNlDwAhzgTACigvbvp6srUkHjQDMcnYERu6u3fqqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=K9CWWblKWlLL3NcVocM-eFKl7HAE0R4_-sapiABisGq8sSmnBuUqBPIjwP7JWkFB1xx_YqTi76rhyt3orPiu1CAyIk4mfDmkvDSLyHaQFLKDvxaWPx2tAwfVwLAVuuWEdTMxjL46RWj3prCLe3mupog7_bl0Z1W_FNjgX_HbaOkc58tGnYnFNdG-iS5sojKU4mFQFhJOanh5OA_AV9QPXzCWRgbjuwJ9c6u6oi9OplT2HdfUZLMHZ5KnyM8vP2wi_WosI3zt2XDk5JDS_Xss2ecbhXc9t55IrNoXEhvVFYQqVkNlDwAhzgTACigvbvp6srUkHjQDMcnYERu6u3fqqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستربین ۷۱ ساله شد و جشن تولدشو با صدای بانو هایده جشن گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72233" target="_blank">📅 00:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72230">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=ioStx-Vf01lg_LEi_ryoSSe-udY1da8sKiPrkY3Gg7ufgYdmikF-_srAobK7tE7dcQqCI2_6wO30sAqFNI6s8QXzNTREuWuv7nx-14Yivktu_GvgEluKo60FtuohOnmAQ2TtMR5qP5aL-yHEdsimxdAdMt5t1aFcuPRPDLrpxZZB2l0Nb8rVL2ZHHPBoGnRI5UBX60mB994bmAZieLZ5wmh708U694eTqxpu7rGgF4PoLNrCgGjuRvUCK2-75fSguJUlo-dsW_rOm2AyH8bY5U-sesuNpj3xxfWDGV6Uu8RdazQg-qK2uRy4WzEcZmYOtSBO3DRckvxxPjigvuV6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=ioStx-Vf01lg_LEi_ryoSSe-udY1da8sKiPrkY3Gg7ufgYdmikF-_srAobK7tE7dcQqCI2_6wO30sAqFNI6s8QXzNTREuWuv7nx-14Yivktu_GvgEluKo60FtuohOnmAQ2TtMR5qP5aL-yHEdsimxdAdMt5t1aFcuPRPDLrpxZZB2l0Nb8rVL2ZHHPBoGnRI5UBX60mB994bmAZieLZ5wmh708U694eTqxpu7rGgF4PoLNrCgGjuRvUCK2-75fSguJUlo-dsW_rOm2AyH8bY5U-sesuNpj3xxfWDGV6Uu8RdazQg-qK2uRy4WzEcZmYOtSBO3DRckvxxPjigvuV6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش جالب رئیس جمهور چین  به اقدام ترامپ برای جاگزین کردن عکس بایدن با «خودکار»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72230" target="_blank">📅 00:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72229">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=RsxFHrW1KaOqOIv8WlXH_Npot1yMuOog1d0Tcna98oayMmNflAHfNJnz0wYKnjKdbb6CZ_IVcjahx3p4vlcvLcGLgT0GfbBOQ8rQsNeSF0OXhNjyefYWlrpioqsShMVXVYpSYpD45HJLUCc7FkvrlZrInvAPwMr4AFjvohplCzsskmWqLMpAf99x_dMAO6a6dyze93F7EQlW-nRfTGE3tbkIdkjVWltGeLqNlRB29dWe7YtcSXVKYPBUa8BIzV3fuLFBq-DobfQ2DMOvFcBtQebvrZHw-Yx1l5qc9tEid9QLQHdpMrvynrwItvSh9nKYmo72413IP5h3Kj_LwGGSYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=RsxFHrW1KaOqOIv8WlXH_Npot1yMuOog1d0Tcna98oayMmNflAHfNJnz0wYKnjKdbb6CZ_IVcjahx3p4vlcvLcGLgT0GfbBOQ8rQsNeSF0OXhNjyefYWlrpioqsShMVXVYpSYpD45HJLUCc7FkvrlZrInvAPwMr4AFjvohplCzsskmWqLMpAf99x_dMAO6a6dyze93F7EQlW-nRfTGE3tbkIdkjVWltGeLqNlRB29dWe7YtcSXVKYPBUa8BIzV3fuLFBq-DobfQ2DMOvFcBtQebvrZHw-Yx1l5qc9tEid9QLQHdpMrvynrwItvSh9nKYmo72413IP5h3Kj_LwGGSYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این تحرکات لجستیکی و نظامی آمریکا باید توافق رو قطعی بدونیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72229" target="_blank">📅 23:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72228">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عجب دنیاییه، پزشکیان رفت سازمان ملل از مردم غزه حمایت کرد، نتانیاهو هم رفت از مردم ایران حمایت کرد
#hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72228" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72227">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
می‌خواهم از شما بخواهم که با دقت به حرف‌های من گوش دهید. روزی خواهد رسید، و ممکن است این روز خیلی دور نباشد، که مردم ایران آزاد خواهند شد.
این رژیم خبیث، به دلیل دروغ‌هایش، فسادش و ظلمش، سقوط خواهد کرد. این رژیم ستمگر فرو خواهد پاشید و همه ما در آن روز جشن خواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72227" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72226">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
این یک دستگاه ارتباطی استارلینک است که به مردم اجازه می‌دهد به حقیقت دسترسی داشته باشند، آزادی اندیشه و آزادی بیان را تجربه کنند.
به همین دلیل است که رژیم ایران میلیاردها دلار برای سانسور اینترنت هزینه می‌کند.
آقای رئیس جمهور، من این دستگاه را پیش شما می‌گذارم تا بتوانید آن را به هیئت ایرانی بدهید.
بنابراین، وقتی آنها ناگزیر به ترک کشور شدند، آنها نیز می‌توانند آزادانه داستان خود را در رسانه‌های اجتماعی بیان کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72226" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72224">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو: خدا باماست
سخنرانی تموم شد
#hjAly‌</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72224" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72223">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتانیاهو: روز آزادی مردم ایران رو باهم جشن می‌گیریم
#hjAly‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72223" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72222">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو: یه روزی که خیلی دیر نیست، مردم ایران آزاد می‌شن
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72222" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72221">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتانیاهو: نیروی مردم ایران، آخوند رو شکست می‌ده
#hjAly‌</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72221" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72220">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: شما مدافعان قلابی حقوق بشرین
#hjAly‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72220" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72219">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: وقتی آخوندا هزاران معترض رو کشتن شماها کجاها بودین؟
#hjAly‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72219" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72218">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نتانیاهو: آخوندا می‌ترسن که مردمشون استارلینک داشته باشن
#hjAly‌</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72218" target="_blank">📅 22:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72217">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=K6ZgwR8MbSlYb6Hdmjo_TUvALahDJCE-0mMaPCvaRxiriLulvRUaCIiX8XAcSv12PUMiPmuhGtsq5AQXXWNocqxCVw85VoQokJiKtyVuKn24uaKFhSnH9tVKT06tf_Tgfb77CIzKgOBV9cWZCLh1yZQ894iLY7g9swx9qIcdcpwVGfJIRsw0yE-9fpSsuREc-GZ7dcy8nL3BBnT4ztlh2qZfVsdhlBu9RnMc_4Bs91VyF-jFoZrRNfucrx0wN-mky4gi6QhmU7zzINSH5kMu-tGme6Sh8D80_G-vpq8-UsQhLtgU-PnoBAFda11jGlEDj-94nDY9D7xDrLeVhONUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=K6ZgwR8MbSlYb6Hdmjo_TUvALahDJCE-0mMaPCvaRxiriLulvRUaCIiX8XAcSv12PUMiPmuhGtsq5AQXXWNocqxCVw85VoQokJiKtyVuKn24uaKFhSnH9tVKT06tf_Tgfb77CIzKgOBV9cWZCLh1yZQ894iLY7g9swx9qIcdcpwVGfJIRsw0yE-9fpSsuREc-GZ7dcy8nL3BBnT4ztlh2qZfVsdhlBu9RnMc_4Bs91VyF-jFoZrRNfucrx0wN-mky4gi6QhmU7zzINSH5kMu-tGme6Sh8D80_G-vpq8-UsQhLtgU-PnoBAFda11jGlEDj-94nDY9D7xDrLeVhONUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
اخلاقی‌ترین ارتش جهان؛ ارتش اسرائیل (IDF).»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72217" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72216">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتانیاهو: هرگز نسل‌کشی نکردیم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72216" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72215">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نتانیاهو: آقای ممدانی تلاش کردی من نیام نیویورک، دیدی کیر شدی؟
#hjAly‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72215" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72214">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو: کیرم تو ممدانی و زنش و دوستاش
#hjAly‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72214" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72213">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو: ما کلی واکسن و غذا به مردم غزه دادیم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72213" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72212">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نتانیاهو: اردوغانِ جاکش، تو هیچوقت حاکم قدس نمی‌شی
#hjAly‌</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72212" target="_blank">📅 21:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72211">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو: کیرم تو ترکیه
#hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72211" target="_blank">📅 21:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72210">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو: کیرم تو قطر
#hjAly‌</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72210" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72209">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=elvFXoVwRmvUX6SlxWGMYkqHY0hCpenXJZGROMGcRctsljHe8Y2HnRh7gqEkg8MmklG8Y8ulYokIoDKz_H6kJ_GIHghatheinn6qX2M6mXHp-m7WHmAAdIrGgPjamcwskqn403VY3tQZnzQhPWmXsVwIsAKqrLfRA_2t-dcr9YvVQJIU1XoHeWFdsv6VcEFXaAMT9OcmpQUBykvAaz6hiLRcwEaLztsgtvL2R6HpW5hXkYGj3aBBPRqV8MAHRRQc70UbKVx39QZvKUpVMOaWIOumGjccpO-xgNDfLXzv8AgFf3GnB9UcCnl3gqejA2JfzNm1R_nD3XmV-O2amuy1pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=elvFXoVwRmvUX6SlxWGMYkqHY0hCpenXJZGROMGcRctsljHe8Y2HnRh7gqEkg8MmklG8Y8ulYokIoDKz_H6kJ_GIHghatheinn6qX2M6mXHp-m7WHmAAdIrGgPjamcwskqn403VY3tQZnzQhPWmXsVwIsAKqrLfRA_2t-dcr9YvVQJIU1XoHeWFdsv6VcEFXaAMT9OcmpQUBykvAaz6hiLRcwEaLztsgtvL2R6HpW5hXkYGj3aBBPRqV8MAHRRQc70UbKVx39QZvKUpVMOaWIOumGjccpO-xgNDfLXzv8AgFf3GnB9UcCnl3gqejA2JfzNm1R_nD3XmV-O2amuy1pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
با دوستان آمریکایی خوبمان، ارتش، نیروی دریایی، نیروی هوایی و تأسیسات هسته‌ای ایران را در هم کوبیدیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72209" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72208">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=Tg36ttCToWUpV3TRd1vHgO9Ectco64N7QBkzDU9ECae7R5J5Munv0CWoFxQKf_uMcmTourtizvYxuILL3Um_ZAVM-EvxN881jKKCsKmJbf1afnk-FrsMMK4i8EUzj64w_w5A9GF_-G7vopIe1RY1N1dUMnZZIdG-435mvtyikdmiZFiynanyaaRj0jJd4nqxrX-u_iQnhX0hOKkurXN3yU4pSt2J_nLlTh1kHGCgu4Gngmt7trOxgdoIZlzL5rrpu21jSHu3pMqJgBe6o-JzHZbF8bxL5benxFNkSwIdhZaut2r35YCPE8JpPq--rZt8yFhsDP7xDF-HyK8nzS-ZZS-2dRSBBFMzuaLif0_m_f1acYB7EGgmr7LaKco69Zh563RqyFI07eIvoFTpmtapg3aGMd5b7jsjalt9LQEWCDOVuwk7_IAs5KObjZZdrGP-iucEQsb3_g1tz3CJs6ylccvRxMqgb2YHkBYaxGID3Nn8b9vrI-9wk2hZRkHsjdcQByKPnQxF234YULYUgzvYJhdGm0Xid0WbYBkJUxOc96yoB8SvkFuC812LJgGLKZH2AtvOUmjDl2oVd7izUlXLEGKnI8TbTBxPZa70CsXAiwBojaY8zexDOEk-jdXj1ta3lXBB5Nu5vSx_N2fjx1qND-P93hsB_gdmfsJrV5PJfn8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=Tg36ttCToWUpV3TRd1vHgO9Ectco64N7QBkzDU9ECae7R5J5Munv0CWoFxQKf_uMcmTourtizvYxuILL3Um_ZAVM-EvxN881jKKCsKmJbf1afnk-FrsMMK4i8EUzj64w_w5A9GF_-G7vopIe1RY1N1dUMnZZIdG-435mvtyikdmiZFiynanyaaRj0jJd4nqxrX-u_iQnhX0hOKkurXN3yU4pSt2J_nLlTh1kHGCgu4Gngmt7trOxgdoIZlzL5rrpu21jSHu3pMqJgBe6o-JzHZbF8bxL5benxFNkSwIdhZaut2r35YCPE8JpPq--rZt8yFhsDP7xDF-HyK8nzS-ZZS-2dRSBBFMzuaLif0_m_f1acYB7EGgmr7LaKco69Zh563RqyFI07eIvoFTpmtapg3aGMd5b7jsjalt9LQEWCDOVuwk7_IAs5KObjZZdrGP-iucEQsb3_g1tz3CJs6ylccvRxMqgb2YHkBYaxGID3Nn8b9vrI-9wk2hZRkHsjdcQByKPnQxF234YULYUgzvYJhdGm0Xid0WbYBkJUxOc96yoB8SvkFuC812LJgGLKZH2AtvOUmjDl2oVd7izUlXLEGKnI8TbTBxPZa70CsXAiwBojaY8zexDOEk-jdXj1ta3lXBB5Nu5vSx_N2fjx1qND-P93hsB_gdmfsJrV5PJfn8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
آنها به زنان باردار تیراندازی می‌کنند و خانواده‌های کامل را هدف قرار می‌دهند. البته هیچ‌کدام از این موارد در رسانه‌های بین‌المللی یا شبکه‌های اجتماعی پوشش داده نمی‌شود؛ هیچ‌کدام!
آنچه پوشش داده می‌شود، گروهی حدود ۱۵۰ جوان کم‌سن‌وسال بزهکار هستند که می‌روند و سنگ پرتاب می‌کنند و درختان زیتون را قطع می‌کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72208" target="_blank">📅 21:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72207">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو: هدف فقط پیروزیه، همونطور که داداشم یونی گفت، ما مجبوریم پیروز بشیم
#hjAly‌</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72207" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72205">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو: دم ترامپ گرم داداشیمه
#hjAly‌</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72205" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72204">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتانیاهو: خامنه‌ای دیگه مرده
🔥
🔥
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72204" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72203">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو: این پیجر های تو دستم رو می‌بینید؟ حزب‌اللهیا که خوب یادشونه، با همینا دهنشونو گاییدم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72203" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72202">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو: خدایی کیو دیدین مث ما که تو هفت جبهه همزمان بجنگه؟
#hjAly‌</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72202" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72201">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو: مث شیر می‌جنگیم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72201" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72200">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نتانیاهو: سال‌ها پیش داداشم یونی تو جنگ با اعراب بهم گفت ما پیروز می‌شیم، الان من همینو می‌گم، ما پیروز می‌شیم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72200" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72198">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو: اسرائیل کوچولوعه، انگلیسی های جاکش که خودشون استعمار رو اختراع کردن به ما می‌گن استعمارگر، کیرم دهنتون
#hjAly‌</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72198" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72196">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نتانیاهو: ما به کشورای زیادی کمک کردیم، یسری از همین جاکشایی که الان رفتن بیرون هم از ما تشکر کردن، کیر تو هرچی ریاکاره
#hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72196" target="_blank">📅 21:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72195">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو: نابود کردن تاسیسات هسته‌ای جمهوری اسلامی سخت بود ولی انجامش دادم، اگه این کارو نکرده بودیم همه مرده بودیم
#hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72195" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72194">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو: نمی‌زارم آخوندای قاتل به سلاح هسته‌ای برسن
#hjAly‌</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72194" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72193">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو: کیرم تو جمهوری اسلامی
#hjAly‌</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72193" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72192">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72192" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72190">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سخنرانی نتانیاهو از این لحاظ که قبل از انتخابات اسرائیله مهمه، می‌تونه از جنبه‌ی جنبه‌ی تبلیغاتی این تریبون استفاده کنه، کارهایی کرده و کارهایی که می‌خواد بکنه!  این سخنرانی تا دقایقی دیگه آغاز می‌شه #hjAly‌</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72190" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72189">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP3HEeKTCzM7cvpCFHQegtxmlBJPGHyJfXRSr0Xw5xuAUq5r3vxdyIWf9VMDJNQopjlu2p4Gj27Kkv60TaWjLp1A9GsqYP0sA8btfbD-RNi5aXfBV9Hq337GKpqmZyRA5_vtHCuD9g1ud6us4StaMbnnw3gThNDY1-_PTDAwIT_m4P_Za33TTfQsMsw7uS01fy7FRtqV9iSCforGcO4ueqye8367FbxovsnDrVKOsSZ6yu3LLlZI5M3PHnRxhFqMGbUOICeQKC6aYiFV9sYr6ymF9QE0ar5JyZTqDlwuR0TkzCNtX4wrwEzTDVAXHOaQMUyg9swpCFoKpA8LwKSi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان درحال مصاحبه با فاکس‌نیوز آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72189" target="_blank">📅 21:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72188">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7c569da6.mp4?token=v5TcyBKCvz-rpimMJMOf_K0tbczfNDrH7r0YOj3boO5JqPKri0p4BZP3tmK5cGnhXtcF5jUqfNh6eMdpKYUxj1sRWCy45XoWSNzrleDuB0wi4aNjYdduS5Ez7atA5ArfHMXpczO26ieo5ivCsJqm2qYtcIjWmDMNQzGLLCkXY6ZOFI4amWuv-bgsiQY5l0Ou_fdXVvHuecBPJNsXlbeFOnlq0nNBlQWVCm1NSeg1RMC877a4SbvX4PCT-nEfFymTVlExky6k4mlCAIjfyRi4V7WQ5LTjyrQw6kz7kzMzq8V5YMhtBSAaqvWuCOhTfVka3U7V5HiwYsvTl3D5TVx2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7c569da6.mp4?token=v5TcyBKCvz-rpimMJMOf_K0tbczfNDrH7r0YOj3boO5JqPKri0p4BZP3tmK5cGnhXtcF5jUqfNh6eMdpKYUxj1sRWCy45XoWSNzrleDuB0wi4aNjYdduS5Ez7atA5ArfHMXpczO26ieo5ivCsJqm2qYtcIjWmDMNQzGLLCkXY6ZOFI4amWuv-bgsiQY5l0Ou_fdXVvHuecBPJNsXlbeFOnlq0nNBlQWVCm1NSeg1RMC877a4SbvX4PCT-nEfFymTVlExky6k4mlCAIjfyRi4V7WQ5LTjyrQw6kz7kzMzq8V5YMhtBSAaqvWuCOhTfVka3U7V5HiwYsvTl3D5TVx2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوزوی‌ها به روش خودشان برای بهبود چهره روحانیت در اقشار میانی جامعه کارزار به روز شدن راه انداخته‌اند؛ آنهم با «جوانگرایی»!
یک آخوند مبلغ، طلبه جوانی به نام «رضایی» را به شهربازی مشهد برده و از هر فرصتی برای مالش و ملعبه با او استفاده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72188" target="_blank">📅 21:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72187">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfa6b3480.mp4?token=pKa5DfqP_Chuvq9n1qUKs-N0qGiqDTww6VLrkAW5c46DQQw2lie2I8Z7DLdQCxD-W88a3k_RnW0dUIF9vValNI0vBwCBbfeWCQrtmvxPmbpdAjnYmsKn5CM6d0K9NpqhyTXVj0-p6yCav1Lt9hr1ce_COABtthVoBN_xunyU9ufj1bFtxaSd3RPf9XRx0ZoZ3r1dKqpYqK1QKB0QWGnPNCG0rapxQxdERXzl_3cxY1g4D1BawpHP4Yit5GcCW0DwOrOU5r35oIf_LGNfZkEJlKwnDbnFg1x38EtZ5k4CNDdRd1yz8t3qIAkPtIBJ_ocwiyQioFL3pOrPnFXbkEIIeh8wFnJs5gnfajH7J7FBA3q3r6Td0Vgosy3HrDRr_pFVvtwsZkUtNW8ZNaJ9fJMJF9X0HeuCfPVWjJycTxnCqxHrkgHPKAgxnMquGSfUN4b1FdS2KS2LDe3MKVGcLw23SBaau_h6dh0WLfPGY7CD58UHQZ6FLxbY_XvH4NgFtOQfLbQhudDAkaYKxg-wBjw5OoPICrK96U6YfgwoPLa4DmDhzWI54ILGa58DqnPZv8m-XadCkbvfSkb6h3BPBoQTn-3eyyOcVaudoLJyQsmNeS6hXupf3v6QzgdbV2JriwFr22ggEgpsdZ0b4_V74IiEPbf9TI1XXj6fJrouQV3P2TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfa6b3480.mp4?token=pKa5DfqP_Chuvq9n1qUKs-N0qGiqDTww6VLrkAW5c46DQQw2lie2I8Z7DLdQCxD-W88a3k_RnW0dUIF9vValNI0vBwCBbfeWCQrtmvxPmbpdAjnYmsKn5CM6d0K9NpqhyTXVj0-p6yCav1Lt9hr1ce_COABtthVoBN_xunyU9ufj1bFtxaSd3RPf9XRx0ZoZ3r1dKqpYqK1QKB0QWGnPNCG0rapxQxdERXzl_3cxY1g4D1BawpHP4Yit5GcCW0DwOrOU5r35oIf_LGNfZkEJlKwnDbnFg1x38EtZ5k4CNDdRd1yz8t3qIAkPtIBJ_ocwiyQioFL3pOrPnFXbkEIIeh8wFnJs5gnfajH7J7FBA3q3r6Td0Vgosy3HrDRr_pFVvtwsZkUtNW8ZNaJ9fJMJF9X0HeuCfPVWjJycTxnCqxHrkgHPKAgxnMquGSfUN4b1FdS2KS2LDe3MKVGcLw23SBaau_h6dh0WLfPGY7CD58UHQZ6FLxbY_XvH4NgFtOQfLbQhudDAkaYKxg-wBjw5OoPICrK96U6YfgwoPLa4DmDhzWI54ILGa58DqnPZv8m-XadCkbvfSkb6h3BPBoQTn-3eyyOcVaudoLJyQsmNeS6hXupf3v6QzgdbV2JriwFr22ggEgpsdZ0b4_V74IiEPbf9TI1XXj6fJrouQV3P2TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇱
🇮🇱
شماری از نیویورکی‌ها در اعتراض به حضور بنیامین نتانیاهو در این شهر تظاهرات کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72187" target="_blank">📅 21:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72186">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سخنرانی نتانیاهو از این لحاظ که قبل از انتخابات اسرائیله مهمه، می‌تونه از جنبه‌ی جنبه‌ی تبلیغاتی این تریبون استفاده کنه، کارهایی کرده و کارهایی که می‌خواد بکنه!
این سخنرانی تا دقایقی دیگه آغاز می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72186" target="_blank">📅 21:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72185">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90322c0135.mp4?token=JTT2VJAcF0iTkGhw7QXjqNJ5Lb_sJhEJczPKXAEFbjvFZtqB48wWOQWzj0BEd-LeSJAl0aXKgf8bNaphZYnlOnEy4g4NyJM-jOo7dtCDqMfLfVahmWfJVzJcymue-jxqRndxpqBmN61Bht-h21mXV51xjo22Cy3T-2IL6R4xS_yfR0D_ejEMFEicXC8bORvazf0xJeGfYms1GasX0z9H_nSKEPZMyEAC9xdgJuYK6On49C7AeM0xDoEIkidK0bGlwVJuc40BKJ-lBs5kRhDaPrFlhleOdAV3790ud7oRpc5qfF8nZBuFOVnYWb_vuBJnPUvmsuI9bznutMQDN6IiJIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90322c0135.mp4?token=JTT2VJAcF0iTkGhw7QXjqNJ5Lb_sJhEJczPKXAEFbjvFZtqB48wWOQWzj0BEd-LeSJAl0aXKgf8bNaphZYnlOnEy4g4NyJM-jOo7dtCDqMfLfVahmWfJVzJcymue-jxqRndxpqBmN61Bht-h21mXV51xjo22Cy3T-2IL6R4xS_yfR0D_ejEMFEicXC8bORvazf0xJeGfYms1GasX0z9H_nSKEPZMyEAC9xdgJuYK6On49C7AeM0xDoEIkidK0bGlwVJuc40BKJ-lBs5kRhDaPrFlhleOdAV3790ud7oRpc5qfF8nZBuFOVnYWb_vuBJnPUvmsuI9bznutMQDN6IiJIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇺🇸
🇺🇸
🇨🇳
دونالد ترامپ درباره شی جین‌پینگ: «شی در زمینه سنگ‌ها متخصص است و عاشق گرانیت باکیفیت است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72185" target="_blank">📅 21:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72184">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d872351dfc.mp4?token=BoaH-TrYMqGXDlBijwITjZSlvT6kZM5x_E3wQ6z5tuPTJNfYolbH_doKgo_en-fN10TDGwKguyOelNea0TsjMWmqVKrWLj5fr_QuPP9mQbxK5uAOzHudNO_p1UtsrHFKk8zj4tnrzumkVV4zWU7InWvUhI7xkptgTkWEuKVtGvG4wtW66w8HHZBRAO9A0uAv_dt-Q163DMDIgF2FGnBE_IGcQKnsw--Z1qZYIJOCU9l9_MVi52ikPyIjGdINNRxUgtjTpio4xhk2f90e170JOBGG-74ctX3kUtp6CdsziftGxu7IScso--icqm7ecz7GCkHZEKrSapV8O9-u8fhwYGgisJHn6VvdPHWOcselactk91vWD_thiB94zIzvvKjC1ukzr9HRmhMh77tENOA4evBAHEadel94WDPFD5EQBxkGwOzPx6Qv35a58MCUheUxTaturJJ7EwGUTaLKl6LJkYELiD8nlaU8tZXgIUbVPXvzPD0iSVEPmcSsMoLFpjNUjQi_YM-VF74xueOx2weDhd8rTPWMGktyJj14YGez6F0wpj3c0LBc8ztEnEvnTPr24M8f5-2PgAwjlBRq1Ojt_UfxhlqCcVVd5sboA1uAZVlbjE33VcRmelC5iHPGxl7zuUXCK8ExJlrJW_eChE34wOxoawMtKWC3q9L-eyb2OgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d872351dfc.mp4?token=BoaH-TrYMqGXDlBijwITjZSlvT6kZM5x_E3wQ6z5tuPTJNfYolbH_doKgo_en-fN10TDGwKguyOelNea0TsjMWmqVKrWLj5fr_QuPP9mQbxK5uAOzHudNO_p1UtsrHFKk8zj4tnrzumkVV4zWU7InWvUhI7xkptgTkWEuKVtGvG4wtW66w8HHZBRAO9A0uAv_dt-Q163DMDIgF2FGnBE_IGcQKnsw--Z1qZYIJOCU9l9_MVi52ikPyIjGdINNRxUgtjTpio4xhk2f90e170JOBGG-74ctX3kUtp6CdsziftGxu7IScso--icqm7ecz7GCkHZEKrSapV8O9-u8fhwYGgisJHn6VvdPHWOcselactk91vWD_thiB94zIzvvKjC1ukzr9HRmhMh77tENOA4evBAHEadel94WDPFD5EQBxkGwOzPx6Qv35a58MCUheUxTaturJJ7EwGUTaLKl6LJkYELiD8nlaU8tZXgIUbVPXvzPD0iSVEPmcSsMoLFpjNUjQi_YM-VF74xueOx2weDhd8rTPWMGktyJj14YGez6F0wpj3c0LBc8ztEnEvnTPr24M8f5-2PgAwjlBRq1Ojt_UfxhlqCcVVd5sboA1uAZVlbjE33VcRmelC5iHPGxl7zuUXCK8ExJlrJW_eChE34wOxoawMtKWC3q9L-eyb2OgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به مقر سازمان ملل در نیویورک می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72184" target="_blank">📅 20:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72183">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=MX-c7_-NIhQ2WjupBZbIAcBNl70XoS9gReGUMuVSBRIv_CXPkVor0qQbqQD3AzNw2BaTiymrB3NNml0kvQKZ9hUT0fSjTe4vX1OqsRKCeBVIpcbswbtS5PFhuUFx3AgggnSB7QIPGLVAWRKJ7kN9kIjwzS3Gaon5AplvKLY43-FeWwbpl1QGUfM5EiX-vU6fRegYuT3GCB_Qk8Xmh3Ml-74h2iw6gHTAdvFUnqtjFJqv4bnXkinJzjnpGUaOUoW0KfGb_M90SoR82suuLbEKChMaAfBuXK7IR1ifwpYVmigLjfoX2yuDd8K7Bxva6EYL2ZChnhmFFbaU6l7EHmxIoRb5JYAkuEVc7ebP3jov8_VZueD5dFCVt5sLyDFX7mdjC8BNkhmY5sBza2KdlCRXf6JEjUcojMzLJ5B6YDY-f7-WdCRqiFO-78LP1HJB6AVmwhcE8_oiUVNZCyIAkObxCr7ONTXXFhN5A78HTOrIMAAUQxRU_DaoIRaxU4AQuc4v0FcliYNTeZLLlL8SXUpqaVGbKQo4yieRb5TbYnxoWo9ZnXyBgpgl_LXtEdY7TYez24wmtNJGfr6V4_SgZIFQI4pBXtBXt1evTcAav8XJB8xUoRg0-VuYKaHGf6kmER-7tbMnzU4t8S79rOfOrfVQ2z-W95JyeYrEzGZSHQSfiRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=MX-c7_-NIhQ2WjupBZbIAcBNl70XoS9gReGUMuVSBRIv_CXPkVor0qQbqQD3AzNw2BaTiymrB3NNml0kvQKZ9hUT0fSjTe4vX1OqsRKCeBVIpcbswbtS5PFhuUFx3AgggnSB7QIPGLVAWRKJ7kN9kIjwzS3Gaon5AplvKLY43-FeWwbpl1QGUfM5EiX-vU6fRegYuT3GCB_Qk8Xmh3Ml-74h2iw6gHTAdvFUnqtjFJqv4bnXkinJzjnpGUaOUoW0KfGb_M90SoR82suuLbEKChMaAfBuXK7IR1ifwpYVmigLjfoX2yuDd8K7Bxva6EYL2ZChnhmFFbaU6l7EHmxIoRb5JYAkuEVc7ebP3jov8_VZueD5dFCVt5sLyDFX7mdjC8BNkhmY5sBza2KdlCRXf6JEjUcojMzLJ5B6YDY-f7-WdCRqiFO-78LP1HJB6AVmwhcE8_oiUVNZCyIAkObxCr7ONTXXFhN5A78HTOrIMAAUQxRU_DaoIRaxU4AQuc4v0FcliYNTeZLLlL8SXUpqaVGbKQo4yieRb5TbYnxoWo9ZnXyBgpgl_LXtEdY7TYez24wmtNJGfr6V4_SgZIFQI4pBXtBXt1evTcAav8XJB8xUoRg0-VuYKaHGf6kmER-7tbMnzU4t8S79rOfOrfVQ2z-W95JyeYrEzGZSHQSfiRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز یک بمب‌افکن رادارگریز B-2 و چهار جنگنده F-35 Lightning II بر فراز کاخ سفید در جریان سفر رئیس‌جمهور شی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72183" target="_blank">📅 18:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72182">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MEST1bpLMF1o3sphTrC5v-APULdNzyOixSdf-5RYTxvS3laD_TVtoscmTnjgbvzweKkOlRFi2x17qSIwgehdeEsGJUHU7XcoHIPvzJTen4jNVSmyh4TWXQ9kr8aPBXQcRtNB3jz7hwZ3JIsa1KCy7FSiUNfcco6QvIJZt8vu48hoMRlZG5mD-uPhM3cwAw-GRyBXCvXDY1qFS85wfWChAlhXawbyIORSNxIWpTQWjpz5EQcEDfIiTClsoFjtA1TZmleFUk1UPKdYCwTZQxGwBHajlUX-w4IfBp5qKIj2QU771F90ZF3arWh4Ud59vjm1ttAHCCns_-mMHrD1fTfacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر ترکرز گزارش داده است که نزدیک به شش میلیون بشکه نفت خام توقیف‌ شده ایران به ارزش حدود (600 میلیون دلار) در حال عبور از اقیانوس اطلس به سمت خاک آمریکا است!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72182" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72181">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=vqPXVLNbGG_4snu4VpeRNP-SnpDXBiXzyaQn5mW6EHgRr0B53izAtAZ0jwMNI9VkiNBWf668Xe6wKnbPrXHHd5RgtXKasvH_k8wX5MHhi85uqpRcT2u_px2SERWWFAAQctzfAM0eyvJx6tq0A-NNnL5MdQV0HdjUe5FyOkKKgPB50troSnjDeMbZCSWBrpn-6n-VefQTGCE0I-92HUC95TP9PZ6KsTFmjtKMmhm8LRSLsEi2q-iVP2yyApJ-js3VDIoF2fjRcR_Sqy_4J31VPHqszh8pfYmsS1xwMy5NCcNFWX9SYgSnkMRmci2NSx6HOnEhdzEROLhASr9ETsVzrITHa3vGY0A_Qhx6EIvfjVrzBmI2o30qfNtzWKplkU7OaP9rVflgjkbkOv8Z_ujHdD01rdMJGbvj0YxuPwbjeiY6CNllJgoXqdN8ncyJwiSDsnH3UDSRF0fU5bX4gp8SNsvJHbbeu3H-z7NGZazUlooYssxvgNyZ0gxNp01neSgLCdoMEr56nY3sC4l8cVgJXcOwok3PZwJYxKKa6yeK3MDfhY2PJ9Lu6meg27vVoJIuIyjVJqAfwWcvVavjThP7ltC_13ccQWLJhfrFWzlHKWB96rbt0ayJYyqGKctnrDxpZovvnbus5A9lPo9pe-paiE8TZDKmOSrv8jMr48VhMqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=vqPXVLNbGG_4snu4VpeRNP-SnpDXBiXzyaQn5mW6EHgRr0B53izAtAZ0jwMNI9VkiNBWf668Xe6wKnbPrXHHd5RgtXKasvH_k8wX5MHhi85uqpRcT2u_px2SERWWFAAQctzfAM0eyvJx6tq0A-NNnL5MdQV0HdjUe5FyOkKKgPB50troSnjDeMbZCSWBrpn-6n-VefQTGCE0I-92HUC95TP9PZ6KsTFmjtKMmhm8LRSLsEi2q-iVP2yyApJ-js3VDIoF2fjRcR_Sqy_4J31VPHqszh8pfYmsS1xwMy5NCcNFWX9SYgSnkMRmci2NSx6HOnEhdzEROLhASr9ETsVzrITHa3vGY0A_Qhx6EIvfjVrzBmI2o30qfNtzWKplkU7OaP9rVflgjkbkOv8Z_ujHdD01rdMJGbvj0YxuPwbjeiY6CNllJgoXqdN8ncyJwiSDsnH3UDSRF0fU5bX4gp8SNsvJHbbeu3H-z7NGZazUlooYssxvgNyZ0gxNp01neSgLCdoMEr56nY3sC4l8cVgJXcOwok3PZwJYxKKa6yeK3MDfhY2PJ9Lu6meg27vVoJIuIyjVJqAfwWcvVavjThP7ltC_13ccQWLJhfrFWzlHKWB96rbt0ayJYyqGKctnrDxpZovvnbus5A9lPo9pe-paiE8TZDKmOSrv8jMr48VhMqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از شی جین‌پینگ در کاخ سفید استقبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72181" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72180">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72180" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72180" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72179">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLgrt3p_fIuy4tApptn5mDfKaGyfV16J0WjJz1nfR1T9W26dlzS1mf36VTiyN1xEvo8-WWwmLff76fcVKjTiFBWHwEkqtRQIu1jVCoj4fpE67ZR3MNOcxpFto3Ahd3sVESAYKb457od8X6rK3h2btOb98twLjPQzvTcfGZkj2Cj-m4UTk8biDjgGZF5YEwlVCgoJT_-1MjNkmuNXc6f4dBfOwq1tnaiAliHlJQEvLBnbpcH4bVgAIlj29h8x7d555wxMf5kymksFotFQR0gO9ByOeaRTkxrJy_TKAwJ4DgFRpIIFAokKKvpHBNsVtW2hq5HNXIvGssjzq_hD_4lW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
ولز
🆚
پرتغال
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ولز: ۱ برد، ۳ تساوی، ۱ شکست و ۱۱ گل زده
پرتغال: ۲ برد، ۲ تساوی، ۱ شکست و ۸ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72179" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72178">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRuNYzSKATspDEcs7haf2oVp3yBjaDoRygOfxIXe6vWpuAfD4OA6XB-2F9GdFQ0Ns_N5x2MHfDa7x2xf1dBsGrIlzrqtS4X5vflBO5HffuHa1Y5miLQRoCy-eQoEavcyAR9D-e86SEC-WDrpyaLQxJo58ypj5t6_jvoYe8QKAktZY7lX2YLKHX9Mrlsqg21B_qTudU94UfCz45WFvztb1BYzUj-HRcNN9cUilqFvruarKqDzPtcnCdWYqlqxJXZWd5yv-9TW4o2WoV5dvwd_NU-uSYpzEZZymaMpQaMLAIwbqExEpNNY5QWE-ftAxasTKF2F54HZ5bJgkvJ8obUHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو برای شرکت در مجمع عمومی سازمان ملل وارد آمریکا شده است.
او قرار است امروز در نیویورک سخنرانی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72178" target="_blank">📅 17:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72175">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQL6DLkiHv13fSWCj0F9hEq9YfKekaekZpdhDkL-TCIYrw-0AQYbBjRWOqw8mJmxA7uDYpFBzDzb5Ys7Cbp2yYz7PuLaZgy4QASo9WDPg1QHxYD_trk-BFdTbgSmEvMywNa-saDb2M82jUaQKhieKCW3Eoorgkmh-jbqi6Zc5rEyRxAiTdlpTnu2deh3FA3_nxdKE9CRLxIJ_C107iRlTCHNkLXRzdcKmq6RugZv09VeK5sIuvLGJK455Cmd_opRpwQ53aEpgp4pcSiEpDLdy4tiUevk1gMLc4dVMQ8uJHCN5zCXAHU8FjeyTomO1v_K5BvXTIgKs9oe4iFGEtZm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_iH_Hr_Og70JVtLUTTjYXkJkBUb4SOrb_6TyJttUkmEYHUyKvEpsqCg46KB5g7UKb1tlgboZHXh1QyMHRnmxFy558iWLx73T98aaNj2AKy_gYkKGstBpbisWnWboSyT1Hn8OVM5We_YlYV8dqiXjmKFkfeXmmClu-ohvBWmuxpExZuvBU3KjIvOxDiCB-RBPeWQx9C0h69MP9aR_QcQS1ItPmS_MAEjR2ShKH0wwAsL00stvgYwjBGTeEdLinOagitT-JPRi69_M4Zlx9l7W1ZPVEKwPA4kkfLmLxU-vKr9TVHxgNW2AKpsJLckJqF0Z-XTji98UT0k0bdvWzKyAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=aGav61ffWwXh-NzKfFgc8qz2Lj5d6MR7n59iui2OI_ngZ2Xr1dw8ON_muHTahH-nGIURfGKnXKCic-BKK5iu__bIfrNYywf6lctXDjdzYitgqyU8aOVt-9kI2bITftPPiFf7Az4RdSqekDcZLVnbT_WnqmsVI2zDmm_BUY0YO9QzMdEcxtPwJ-LX_NDWe3dX6lDL-LHuzTZJbYmSiLWzTnF5NWNHxVvggnYCncqBoAPiEGXPTe36oYn_6wiylq3M1xCsreZbD1hE8Z2NYXKp6f6j6CMe6LRd9m-xh53C-omk_xPYXJls_xcuuck36yxV9UrdbdFp-oSIk_JTczDUMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=aGav61ffWwXh-NzKfFgc8qz2Lj5d6MR7n59iui2OI_ngZ2Xr1dw8ON_muHTahH-nGIURfGKnXKCic-BKK5iu__bIfrNYywf6lctXDjdzYitgqyU8aOVt-9kI2bITftPPiFf7Az4RdSqekDcZLVnbT_WnqmsVI2zDmm_BUY0YO9QzMdEcxtPwJ-LX_NDWe3dX6lDL-LHuzTZJbYmSiLWzTnF5NWNHxVvggnYCncqBoAPiEGXPTe36oYn_6wiylq3M1xCsreZbD1hE8Z2NYXKp6f6j6CMe6LRd9m-xh53C-omk_xPYXJls_xcuuck36yxV9UrdbdFp-oSIk_JTczDUMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل منطقه «کفر تبنیت» در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72175" target="_blank">📅 16:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72174">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb1a6b62b.mp4?token=XLFdsXU2bMFt05BysfCeRpsHtaW_MeodH71ZqqYQWj8vLq20FvLpj-ovTy-TXAurILSe3FoFSGeeGSDEygeKMWSnhfQi3gVllqsHopKFwG_vRO6NzfUcrgqUddX2N3Oft9elIpxR6t6e1zOXwC8hzaeojXKdsBLSoEx2zQBVaGCcciVP7o3omJ9BEyFegxXOqW5HeTVtXC96HWad1dhAh06mGCJe_TDTgT-r7MD6nTxf5T8vZKkjLlwKK47Oq518E8UsU_BzgrjTH6NcXOqrZfvlEsLGVYAorqyDrZvxMgyztiZo6YjS8hzVmPiCgBaBr6HgOB85cAQe4HsiMyjNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb1a6b62b.mp4?token=XLFdsXU2bMFt05BysfCeRpsHtaW_MeodH71ZqqYQWj8vLq20FvLpj-ovTy-TXAurILSe3FoFSGeeGSDEygeKMWSnhfQi3gVllqsHopKFwG_vRO6NzfUcrgqUddX2N3Oft9elIpxR6t6e1zOXwC8hzaeojXKdsBLSoEx2zQBVaGCcciVP7o3omJ9BEyFegxXOqW5HeTVtXC96HWad1dhAh06mGCJe_TDTgT-r7MD6nTxf5T8vZKkjLlwKK47Oq518E8UsU_BzgrjTH6NcXOqrZfvlEsLGVYAorqyDrZvxMgyztiZo6YjS8hzVmPiCgBaBr6HgOB85cAQe4HsiMyjNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غذای مجلس ترحیم، اگر خود مرحوم. این نوع غذا رو خورده بود حداقل ده سال دیگه زنده می‌موند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72174" target="_blank">📅 16:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72173">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d6256f78.mp4?token=bhjKRgrF-uS7RHNWBVYAJZ7dU6eo6WfaEbObOmeednsULaoxEVqCPyQug37olJuUmi7OxYJuXQkFYRVSuVwc83XhTAay1bU4UV4zzc7EBQXHeB6QnW3bgrawe3Pr4-m6y1EfMEhIznFSDxOKC7HXuHf8Ar1ag53d44tNel4CJPKzpvVl6ZQiO3HOUdDVue3Oz6VUzWKkEsRsu6OmEuzZwwJVmdDLLGron_Bkx9aNYOiWU_23I1tyD0l6dLVxjT1Bg1RXoGL8-Mh2ptx1a_5ieV_KN7Nom1WtKSRmYXYTqh1UnC4D0oQQuQxPuqvsDHkXFQzL-HEfj1Q1rp4NY9XNmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d6256f78.mp4?token=bhjKRgrF-uS7RHNWBVYAJZ7dU6eo6WfaEbObOmeednsULaoxEVqCPyQug37olJuUmi7OxYJuXQkFYRVSuVwc83XhTAay1bU4UV4zzc7EBQXHeB6QnW3bgrawe3Pr4-m6y1EfMEhIznFSDxOKC7HXuHf8Ar1ag53d44tNel4CJPKzpvVl6ZQiO3HOUdDVue3Oz6VUzWKkEsRsu6OmEuzZwwJVmdDLLGron_Bkx9aNYOiWU_23I1tyD0l6dLVxjT1Bg1RXoGL8-Mh2ptx1a_5ieV_KN7Nom1WtKSRmYXYTqh1UnC4D0oQQuQxPuqvsDHkXFQzL-HEfj1Q1rp4NY9XNmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقا پسر برای تولد دوس دخترش ۲۰۶ خریده و اینجوری سورپرایزش میکنه :))
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72173" target="_blank">📅 16:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72172">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a803db071d.mp4?token=qv8iNRPi6l9P_8tCTKLiZV6aU6L3i6HKyZZx_T3s0hZ-bWLwAKIsYJTL8jFls6hbQoqs6pIDH9fwO0uZ91kF4Pf60sL1b3tUqWf5EvidJpOX_V45a5pST2n03RpwK6oe4VbDiV20F4TMb14cFOfCJnvp484JlocHoaqJO4dxNDIGhmJ_W2nqayo3DDduumhzmBvxFAX_koU2tjGyHw8oQM7CzoImeur8LHX5Bbn6RpP4ZKs0SsoiHZrJ8nmM5JJHSXE-MJCwZNQfcWmZEQq1N9eobLl_ktvWTwUiGxHdLtIOWdoS3ZnebhzyoF9AEi2NTkzA01bUVRwstP2z74Vxyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a803db071d.mp4?token=qv8iNRPi6l9P_8tCTKLiZV6aU6L3i6HKyZZx_T3s0hZ-bWLwAKIsYJTL8jFls6hbQoqs6pIDH9fwO0uZ91kF4Pf60sL1b3tUqWf5EvidJpOX_V45a5pST2n03RpwK6oe4VbDiV20F4TMb14cFOfCJnvp484JlocHoaqJO4dxNDIGhmJ_W2nqayo3DDduumhzmBvxFAX_koU2tjGyHw8oQM7CzoImeur8LHX5Bbn6RpP4ZKs0SsoiHZrJ8nmM5JJHSXE-MJCwZNQfcWmZEQq1N9eobLl_ktvWTwUiGxHdLtIOWdoS3ZnebhzyoF9AEi2NTkzA01bUVRwstP2z74Vxyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور هائیتی در مجمع عمومی سازمان ملل خیلی جدی، از پارچ آب نوشید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72172" target="_blank">📅 15:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72171">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b973e065b.mp4?token=KyUl8fzvA4U48gDMqGscwpRllcQBRWTrxQmZi4lhe_sK7oHLcA92_583p2FLzL9cxIfiOHbj5j24H-9ye7xLavZGUYHJimBaAg4heapnnVOIvZ7MuKLur1VH6j7YD0olFk387TlWgVmuw0OQ8NeMQCCYd3a-0dPU8TJT6r7U6quPxN3oPE6HxCxyOFBoSTOBNAYXD_UDKUDhz5eq8WXT0JcAuhj_G0EUfzm7uU3p8n_NwsmD_vWL9l5henEqjKYsyDjcISI3dCk62ZL67qzXpV_-bYurjlN-rcKtf7A7skamOXJDSvSlz9jSdUR57BzYuVNgTU-hCFJjQz8jJI9qgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b973e065b.mp4?token=KyUl8fzvA4U48gDMqGscwpRllcQBRWTrxQmZi4lhe_sK7oHLcA92_583p2FLzL9cxIfiOHbj5j24H-9ye7xLavZGUYHJimBaAg4heapnnVOIvZ7MuKLur1VH6j7YD0olFk387TlWgVmuw0OQ8NeMQCCYd3a-0dPU8TJT6r7U6quPxN3oPE6HxCxyOFBoSTOBNAYXD_UDKUDhz5eq8WXT0JcAuhj_G0EUfzm7uU3p8n_NwsmD_vWL9l5henEqjKYsyDjcISI3dCk62ZL67qzXpV_-bYurjlN-rcKtf7A7skamOXJDSvSlz9jSdUR57BzYuVNgTU-hCFJjQz8jJI9qgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماتون بریزه، ایران شده مهد عجایب خاورمیانه؛ این آقایی که می‌بينيد لاله گوشش رو سوراخ کرده و یه مار کرده توش.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72171" target="_blank">📅 15:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72170">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e89ab3721.mp4?token=BzpSEZFCdF-9mdOVLcNyZFFwYMo_DPZ3fLRTy3y6U8cSnt1u4Lpfw7xn0Z5ZH07sexEOno_7IuYKUk0XMC0jCvdjRZemVwi2wZJK6m9CKNttADf7bQk1tKDigd3OFxtkqWeTGS5j2wiXkQndT-h8BYP9cmukKZQb3UnPFZaTQsc3u5T3xyMiemlqLYMNX314A1rQWk3xDzO3iJ7us3cKm2Fu8koMeRQgPrO_PkhAmH-BSIABR1IzFFvn4x2cvkyEWJAs5Y-A-qbcsRrXB2zvXQMfft07XnvntnLMR-ZjfAywK4uCxASkX7W1jtIaICZR_ed_35kTrrqOeUbL_Fv1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e89ab3721.mp4?token=BzpSEZFCdF-9mdOVLcNyZFFwYMo_DPZ3fLRTy3y6U8cSnt1u4Lpfw7xn0Z5ZH07sexEOno_7IuYKUk0XMC0jCvdjRZemVwi2wZJK6m9CKNttADf7bQk1tKDigd3OFxtkqWeTGS5j2wiXkQndT-h8BYP9cmukKZQb3UnPFZaTQsc3u5T3xyMiemlqLYMNX314A1rQWk3xDzO3iJ7us3cKm2Fu8koMeRQgPrO_PkhAmH-BSIABR1IzFFvn4x2cvkyEWJAs5Y-A-qbcsRrXB2zvXQMfft07XnvntnLMR-ZjfAywK4uCxASkX7W1jtIaICZR_ed_35kTrrqOeUbL_Fv1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره ترامپ وقتی B-1 لنسر وحشیانه از بالای سرش رد شد دیدن داره
🤣
انگار اصلاً نمی‌دونست داره میاد
😂
قیافه شی رئیس جمهور چین دیدنیه
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72170" target="_blank">📅 14:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72169">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bxc1mE7kS0mlaHWw6tq10wDjz3fCDvyIekOz4Ojy0yttP44PHlvv242LuAwyhoqedYFW_gqQ5vvk6LTVu0CCOyp1ev54Jrqt_g6RBXq5t8QI0Rk1s1zQ63kthpMc05KlAfolwb8HNRJ0efFupPYOmQ49saQ2bZBElW2DfBPkm07s0XevLhXyB5ZjTYychaC7ClrK7JDodMlhlCq1nNhrteimzwKzF1Bh1DIhUafndXMlve2t2dw8bMhsGMCrb-cci6lBGyh0_6776FhyDp-BhBQJN6IpSmnXte7buvJgO5qbLCgs5sBQ3_CQGFbmmcobKdcNb3zJbSe1IIwFyKAyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ایسنا و به نقل از سازمان هواپیمایی کشوری ایران، تمامی پروازهای شرکت‌های هواپیمایی ایرانی به مقصد امارات از نیمه‌شب لغو شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72169" target="_blank">📅 13:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72168">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=Wqh0VGAeEYE2ss8Qpz8OP2kL7-cWutDjG5Xq4iraOH9b_QvqInujQXR4tV3pIvqutoK58-7-6pTmpHT6IhAy9l2oHb1U0ZcmHBCyXXiu0sxX1O5XZKQtrKNy6wbTZU2-24kEqjidvflrRGRFq_lUU7_X1LomfR0dqxMbm1f40cbz5dmlULP7potFfBb4a7hD9qTxX6Ee1rnynOp7No1G6Q994tiDyXLGG7pl9ypm-GUs9BH18MHm5DGXB2Ev6Ccu3zUL0k272uAAqkt2rZ10CVT8_o3AqbdBU0ZfZS9fKKLl4oXYuDeptbFyitMC92f_SzJp9v-RfnRc5Hxt9qkVkkn5VihEYp5h9Jfae9CIgf5_Mrd1PTLcqHDX6OKItITsN1PfpYzz8gOMQrzty_Ly5DHcXjSECLp_jEA045t-dU7TUYtkZlXk-pvH2QLceBu3RooZCsWc0l16aP65tbOtFC7GBKfgtyyDQdfyijjN8N42h026f8SGlJZ3-heyiMKoTOtiFvJivCRxJn8VZq02GmtHrdK17cmXZuFwvt9xPYQbdyXY3xrD-agnqlMUX2pHazkY76Spgk_5XT7EYeQ45-Z3s0WaDzpRrGbCkySaBSqARXe9zxZEO0mEdJq40pGhVnfd7lgkIheO7ambSRsHHd2JdG8rh9-jsHiPhkEabj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=Wqh0VGAeEYE2ss8Qpz8OP2kL7-cWutDjG5Xq4iraOH9b_QvqInujQXR4tV3pIvqutoK58-7-6pTmpHT6IhAy9l2oHb1U0ZcmHBCyXXiu0sxX1O5XZKQtrKNy6wbTZU2-24kEqjidvflrRGRFq_lUU7_X1LomfR0dqxMbm1f40cbz5dmlULP7potFfBb4a7hD9qTxX6Ee1rnynOp7No1G6Q994tiDyXLGG7pl9ypm-GUs9BH18MHm5DGXB2Ev6Ccu3zUL0k272uAAqkt2rZ10CVT8_o3AqbdBU0ZfZS9fKKLl4oXYuDeptbFyitMC92f_SzJp9v-RfnRc5Hxt9qkVkkn5VihEYp5h9Jfae9CIgf5_Mrd1PTLcqHDX6OKItITsN1PfpYzz8gOMQrzty_Ly5DHcXjSECLp_jEA045t-dU7TUYtkZlXk-pvH2QLceBu3RooZCsWc0l16aP65tbOtFC7GBKfgtyyDQdfyijjN8N42h026f8SGlJZ3-heyiMKoTOtiFvJivCRxJn8VZq02GmtHrdK17cmXZuFwvt9xPYQbdyXY3xrD-agnqlMUX2pHazkY76Spgk_5XT7EYeQ45-Z3s0WaDzpRrGbCkySaBSqARXe9zxZEO0mEdJq40pGhVnfd7lgkIheO7ambSRsHHd2JdG8rh9-jsHiPhkEabj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:جمهوری اسلامی در نهایت تسلیم خواهد شد.
نمی‌دانم یک هفته طول می‌کشد، یک ماه یا دو ماه، اما آن‌ها سرانجام تسلیم خواهند شد.
هدف در اینجا می‌تواند یکی از این سه حالت باشد:
اعضای رژیم به جان هم بیفتند؛
نوعی قیام مردمی در ایران شکل بگیرد؛
یا اینکه ایرانی‌ها را متقاعد کنیم که اگر خواهان توافق هستند، به آن پایبند بمانند.
این بار، اگر توافقی حاصل شود، تضمین می‌کنم که آن‌ها به آن پایبند خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72168" target="_blank">📅 13:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72167">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=K7ueSsyzuXOnecFRQukZeoBwcRJ3YO4BpBC6FW5Ju8HBv8OslV1CQ_CchWSLyLTYtgTFRTffTiyPV6yEcEEYOr7MmGidrNUFRJdEIayF1KKoII2Hl9SED0sV5AnMshWds5s5lqzZcWpwTkRNGf5d4OJMPm0c8qpwn-TVj-AOGGpMXkoJPZvImxLTlS6EXTtt6Bij_DEkfNHd2Taozw0C1e87sy_2I7QwsRjpyAsY96v7cUtK_iyguXZhm1B82JnIPw_3E1BYS5ImtVEcFRtmRcgM6cy0sqN3cXBz-seKb1Si3RF7WpF1bKmuk9dL_K8s1olQkQ7YJXOtB3Oz6upEyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=K7ueSsyzuXOnecFRQukZeoBwcRJ3YO4BpBC6FW5Ju8HBv8OslV1CQ_CchWSLyLTYtgTFRTffTiyPV6yEcEEYOr7MmGidrNUFRJdEIayF1KKoII2Hl9SED0sV5AnMshWds5s5lqzZcWpwTkRNGf5d4OJMPm0c8qpwn-TVj-AOGGpMXkoJPZvImxLTlS6EXTtt6Bij_DEkfNHd2Taozw0C1e87sy_2I7QwsRjpyAsY96v7cUtK_iyguXZhm1B82JnIPw_3E1BYS5ImtVEcFRtmRcgM6cy0sqN3cXBz-seKb1Si3RF7WpF1bKmuk9dL_K8s1olQkQ7YJXOtB3Oz6upEyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی رسما فرودگاههای کشورهای همسایه را تهدید به موشک‌باران می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72167" target="_blank">📅 12:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72166">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=tVlH9_IfOXIlD9EWLUZHxGOSSn3FZC5djgLBxzCvMJzdyxav3RZ3arONRCfm4gHfcCvt7Tx3cRpuyMFqTDhMxdwRL5rYJvok8W0E15Iisu5SbOfOIWqpmsPaih4mY72WBU3avfPXTuEz2vVrtdRVvouMNEffVKmzHEX8T222EpuT5g8577Ht5JzGS8YSBXXRMuBliujT9EuWwJGAv3dGmQoW8NiM3z8Gi_po0XbUZXNDk-hmdkVoUf6Im3Lo3bH03DzkxrqvduBCp_BqgdEoV_zL3xZsMx0ll3qbbKDBIORY6kxgWDGbI7qGbwmcKiv5fxHxq7zkLZNxg_175efh9p4Qq0jiaRFzFQsnCBdyUBIOEoZU1B4SF4gsgevTxpBui5FouTZQbe4DrotKsimswe_p4L758uHhpQYsY2YlA5KejT1wyrw__G5oPLQgEmU_s46xTGbX2FitlYhnvOXH8IOsIHsjzpNlUM685JtCDAQOHB7DjmciYNYuhsS9yWo6AHOi5EB5jhnrefgYw20DYvdEsQRzvaDA_Ago3yXn40DQDD64OBRQKGK_DVTLF6BH1O5BhXGJsXPqZgs_kh_DMa0-O4jB08nb9-itNkYbpzQTSKybsFBn2IT1ozXgGW3qu6BHHOViz1xfxz31_tCoRKk1aIENlSrLwt5qAr82jAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=tVlH9_IfOXIlD9EWLUZHxGOSSn3FZC5djgLBxzCvMJzdyxav3RZ3arONRCfm4gHfcCvt7Tx3cRpuyMFqTDhMxdwRL5rYJvok8W0E15Iisu5SbOfOIWqpmsPaih4mY72WBU3avfPXTuEz2vVrtdRVvouMNEffVKmzHEX8T222EpuT5g8577Ht5JzGS8YSBXXRMuBliujT9EuWwJGAv3dGmQoW8NiM3z8Gi_po0XbUZXNDk-hmdkVoUf6Im3Lo3bH03DzkxrqvduBCp_BqgdEoV_zL3xZsMx0ll3qbbKDBIORY6kxgWDGbI7qGbwmcKiv5fxHxq7zkLZNxg_175efh9p4Qq0jiaRFzFQsnCBdyUBIOEoZU1B4SF4gsgevTxpBui5FouTZQbe4DrotKsimswe_p4L758uHhpQYsY2YlA5KejT1wyrw__G5oPLQgEmU_s46xTGbX2FitlYhnvOXH8IOsIHsjzpNlUM685JtCDAQOHB7DjmciYNYuhsS9yWo6AHOi5EB5jhnrefgYw20DYvdEsQRzvaDA_Ago3yXn40DQDD64OBRQKGK_DVTLF6BH1O5BhXGJsXPqZgs_kh_DMa0-O4jB08nb9-itNkYbpzQTSKybsFBn2IT1ozXgGW3qu6BHHOViz1xfxz31_tCoRKk1aIENlSrLwt5qAr82jAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«پرواز هواپیمایی وارش» از «تهران» به «دوشنبه» _پایتخت تاجیکستان_ از مرز هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
این هواپیما سعی داشت از مسیر جایگزین و از سمت آذربایجان وارد تاجیکستان شود که مورد موافقت این کشور نیز قرار نگرفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72166" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72165">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72165" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
