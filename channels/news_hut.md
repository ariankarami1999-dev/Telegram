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
<img src="https://cdn4.telesco.pe/file/JkcmrJKE4WdavYJdmHBxrv6Bp0Ih1wPm_zhMBBiRFxmXFdPqKrI9Hs0LCRTbuq8jmWGp22wmfaoB3QSUCokxRQ07kOUj-ewfSbbRmZsDtXP6cX3ZPndaEVi3mPtQ2XCPq5AXkNs7uewLNks24EURkn-RKCAmVHsbaxrkp52rAQqFyZeyI-WXCASKY5_pR8nTMfK86EAWJM6ROudzAKsJbDONWA8CVQ_N0GEF_S4x-iMUEzMSgfjhBT0FO7rsKRfYXtcxYqh9CCHPAw2i9cax9DT-HpWaLWevug27rAtM_IeKlzX042F87o2dKfrZlkTmbsm1GEl7YxRJKGEpGif-rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 200K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 21:40:27</div>
<hr>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSY-X2EF8UTgN2_qkAK5hkqTY1VT82FDalU-AxPj5CKPQ95ZqDw85BKrx_brpZgfr7s0moL3kzDKI-ZNYcXloSdit3RvOnin_epxTEhWeJUiTPf2rjXk0OTqcTRNunEAQts2ubQHGiz3DKYPG1qQPMzVaJhECCX4NwKCAX17hY4Mh1Dh7bygAnBJjeR-hQ_u09wBz0UdIZW3HLCrQkoZm3-feJxMRodpePw6pBbV2zwzTy5EN7SQ9yc36JWZMhx_e0bOlt0HkJk8PFKIixa7fvoG6y8smoCCVmhyp0qzCk4ANEntk01TgOqK-6IbLeorO8uBChJEIENZSC-fQSz8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkvG6CuaqMHkUuzoApGzAhyZe0ehRo-rJRT4lu59bjh-7IOG5aK2LzRlo0GZp0dWLwFtzEjNR7Oh4DHZ5v2ga8gJeY3GmusHjdbut81O6UfJGUlXOfR6Rb4gkAcHLcMxK06mzh3RjQYbDkrDWZfE_5z5ZQtx9VmZ4TcCRVBwYi9I8lp-BY1CZNO2mVlvtGYETtlh6hsoxebZ5X64D8p0cF74HIR0qSx71qImMQUlvndPbyLl9fkP7ixn2K2LLBKBT7NvShX-UXw1SGUVHtV5eGjy4XKSWqiKNiW_W2pAzJ-l-j-2vXtiGrkmnNP5xtj1fOopbD3Rbhs4lvZ-9LawUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=HKYqC08KFpd6BiaF__GgTOZ8KbQR-6QVOB-7d11QJZjZVTowNYHFP9TP5jDsiobF_z-3_cT0RgFnlYB64dOaGqrTU2JzcDx1sAE9-iPcJuyBuEDjO653HMstyvji3Yv6VUjeCKVeb-Xphs4n44V4oNeogq6uojSe0QjR1kmsP0RaiJBRh1fKtLgWeGlRXonHdC1HyKpKur-81JgucINBxAIsXZSh5dPUAKmaYn83bpmFj-1TsoEyuFNXGkmiEjg4x8n6cIAyYKMtLw2zkulTUqFoWP_5vCx03KWHFgxAluTJYmtiNK21pBEjravXDTzp4ia9v_sk5bJlxvoGzRHmcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=HKYqC08KFpd6BiaF__GgTOZ8KbQR-6QVOB-7d11QJZjZVTowNYHFP9TP5jDsiobF_z-3_cT0RgFnlYB64dOaGqrTU2JzcDx1sAE9-iPcJuyBuEDjO653HMstyvji3Yv6VUjeCKVeb-Xphs4n44V4oNeogq6uojSe0QjR1kmsP0RaiJBRh1fKtLgWeGlRXonHdC1HyKpKur-81JgucINBxAIsXZSh5dPUAKmaYn83bpmFj-1TsoEyuFNXGkmiEjg4x8n6cIAyYKMtLw2zkulTUqFoWP_5vCx03KWHFgxAluTJYmtiNK21pBEjravXDTzp4ia9v_sk5bJlxvoGzRHmcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=cp1KQvesViQCLMXLLWAcoxleH0MWuYBIhp_3_gmWSUi5r_drGhdcWBjV0Q-qE-xNXwqNqJzC_DJKPhCW3BwAhtXBCFaTB1pygSjJWzOltnM8VnF-jcVERT6YZ1SIcJvv5kbcOOWDZceBlwQW98bocFL2o22hPmD9MmbkhJByS9lS0kIESOa8jqktmOWXjPx-pMMwQ4W4ZiiHVQxHJ3Ey4-K1mOlOPvqJbTXeNJopdOX3zyNBGxIlRlypHCgaVS40wumSJS2L-ykUJG5EGAyZSaG0OjpVnpAu1SMBXtXo2vvEblpL6vPBPMzJpixA324usA-3NFMCzRervjsSR0rcxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=cp1KQvesViQCLMXLLWAcoxleH0MWuYBIhp_3_gmWSUi5r_drGhdcWBjV0Q-qE-xNXwqNqJzC_DJKPhCW3BwAhtXBCFaTB1pygSjJWzOltnM8VnF-jcVERT6YZ1SIcJvv5kbcOOWDZceBlwQW98bocFL2o22hPmD9MmbkhJByS9lS0kIESOa8jqktmOWXjPx-pMMwQ4W4ZiiHVQxHJ3Ey4-K1mOlOPvqJbTXeNJopdOX3zyNBGxIlRlypHCgaVS40wumSJS2L-ykUJG5EGAyZSaG0OjpVnpAu1SMBXtXo2vvEblpL6vPBPMzJpixA324usA-3NFMCzRervjsSR0rcxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
می‌شنوم آنها میگویند که«بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
@News_Hut</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=pzxj6cPgT2GTuQiy-cF7gTrZqFwcgf_JpaaQ1QyU5KvDSPFxHj_PhIGgrxTGU8GcZSBlfop3Xi9EyI21AxfSWXbZWmJBJCPg197pzl2443l5Oy6rGG8Lbv5-VCMpMTZTBVx69QJ09G0kymKneY1_ZcqZ0bnDKl_QzhbbgEaS6sAAqsBQ_b50cm6GnowNAQLKmtxWG_tycmktLnivQZlIVhEDZ54bgE_xdJiOmQ37-63-0JF2KmlAHzmGxo1Qi_hPeFTK_ubwexKm0GfeeHZ5eyExgGBmmw0wmW1Snorh1SgVmaeQnRPRZa8G_5ofBVPxGZLE0nXfGzf8WlNucyNWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=pzxj6cPgT2GTuQiy-cF7gTrZqFwcgf_JpaaQ1QyU5KvDSPFxHj_PhIGgrxTGU8GcZSBlfop3Xi9EyI21AxfSWXbZWmJBJCPg197pzl2443l5Oy6rGG8Lbv5-VCMpMTZTBVx69QJ09G0kymKneY1_ZcqZ0bnDKl_QzhbbgEaS6sAAqsBQ_b50cm6GnowNAQLKmtxWG_tycmktLnivQZlIVhEDZ54bgE_xdJiOmQ37-63-0JF2KmlAHzmGxo1Qi_hPeFTK_ubwexKm0GfeeHZ5eyExgGBmmw0wmW1Snorh1SgVmaeQnRPRZa8G_5ofBVPxGZLE0nXfGzf8WlNucyNWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح عقل عرزشی رو ببین
😂
@News_Hut</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QL0_JW9igrdy62CoMf5qgwoZwos7uiOE7waADHhyAoF-8_LhlysGAEpnxL57YKxpbfuoSYkFUDGuJp_6fu_TYss1CEB7DYkQMy1KoDa8ExK2ruIdAmTUCDlTZQQOgoCvWcw4ys7HzL7FAnceNVtthOfuYcIPMQD9HoKv35IoNEnYSENnKfsUzt0IhG1NW_-2besoe6vR5GMKLk6E5Bah5neOxXVhfHMuox9XJqO3OuCVpdJmXDVtqNCyK2NzJr_3qQheArKDi21R7KcNfUe04QRO5zzdaEvMyEsKTQjbvpPOmznOy-8geMWFIpxxck36rvut8gy236KQaNQg5apYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhX6TvNKLyvH68G6xCUJKV8wslMf2C9eDldLCg1EzNM7p7zPpS6Bv8Ynk6enW_mIVBqvqMfOVNduH1QS-byDUh4c05kQ9Xzn1SjK3hoES6Fshw7Bj3sJ4yQvoMttEbsjWI2KqoRfXoyCMcNBolFqf2cRWStLV0Y6-8junPQqF93tCS9t8JEMqcgqDKYVh-b-iIQ-lNDcF4bE5x3KzTElpq8pUrkyva5gT0DFF2K_tOHC15pM2PDnwf7wF8cHbd2TCmSjiOVmagF9mF0wBeEBQXqFDZNdhOUeo2Bqlgn2EPyMD5xS6yGeTYHtuq2mUhJuPedXrW5k33rFHraRbz-MCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=fyyacducrAVsvgaBoqBJRUBqqv4oA5mF1goYXd42SCcKo8tSoQ5QOINjXEtFYPD-4B2D6Pc2aDNMp8cPFXxtjuuiHAQSQ9WSrGQhdltw5sRN6KsyzZdyskCTvTnsuAlR1T7pZVwS91cogYaQUgY8oUBRqbM9_KE9fHm_c2H0RSBMSgWK32BeJTvgsK5NmAZoZwhazU3moL-DEN_lXETl6TvaADIF_PmSIM4X0MF5eIO9e02deBvF7q3BixW7VtEmEs0s9Z2mq1S3dwcEFg1WqJ7GJMBargmx1gHCorRNz4ciN8BYG3ERYKAGyzrfmrqMDDVMpL-BKb8ZOzETe8Ms6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=fyyacducrAVsvgaBoqBJRUBqqv4oA5mF1goYXd42SCcKo8tSoQ5QOINjXEtFYPD-4B2D6Pc2aDNMp8cPFXxtjuuiHAQSQ9WSrGQhdltw5sRN6KsyzZdyskCTvTnsuAlR1T7pZVwS91cogYaQUgY8oUBRqbM9_KE9fHm_c2H0RSBMSgWK32BeJTvgsK5NmAZoZwhazU3moL-DEN_lXETl6TvaADIF_PmSIM4X0MF5eIO9e02deBvF7q3BixW7VtEmEs0s9Z2mq1S3dwcEFg1WqJ7GJMBargmx1gHCorRNz4ciN8BYG3ERYKAGyzrfmrqMDDVMpL-BKb8ZOzETe8Ms6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=bCx5QDu9oKEGm-MJoinJvu0kK5oKfu6wHKCrKnXwEY1oWR7PG8rhTe_bHeAl4nB4gKkbWgzREIoSw-dTb7N7QlbWXwmKOIhImwB1r8xnxRX9qqAM8MTezSSCZL7OFlI13NV2FbsUKiZbOFvm84JyYQkmCIkWytB6M7tgs6Oyv-MHKeLmxQUPLKms8bfEyKJW4ml82ZIf6mFM-eFfWGLpDzjaFjLc5YNcR4GCQ_4kqThozTM00k7qVHEzkUM88zuXzVOUrr9geCeHNzWTGt6iG12od088M7nuXoWFAB77WPYLSQ7lBE5H7dmhukQW_cJNffKZMMrKNh463enQXpJ41Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=bCx5QDu9oKEGm-MJoinJvu0kK5oKfu6wHKCrKnXwEY1oWR7PG8rhTe_bHeAl4nB4gKkbWgzREIoSw-dTb7N7QlbWXwmKOIhImwB1r8xnxRX9qqAM8MTezSSCZL7OFlI13NV2FbsUKiZbOFvm84JyYQkmCIkWytB6M7tgs6Oyv-MHKeLmxQUPLKms8bfEyKJW4ml82ZIf6mFM-eFfWGLpDzjaFjLc5YNcR4GCQ_4kqThozTM00k7qVHEzkUM88zuXzVOUrr9geCeHNzWTGt6iG12od088M7nuXoWFAB77WPYLSQ7lBE5H7dmhukQW_cJNffKZMMrKNh463enQXpJ41Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=qbaoIW3536WIEQ9v1zVKjtlmXLOOUkbks-TVidZ6DNCMUaEbEJC3a-6T0NW_jwKD7UBzCAQz2dc2V9E-gqtwssxS3jZ8-07XfBp4CpMU4P2plzGd6_jRK-kUhj6Tz82x3VlNiGghDABw60iEgEzGX1vpJXGUlyZU6INlTjjr6DPToNhqLCL-SgxuYMpprUJszXtwvUDKysUuXC44pVwYiT9iSe_JR4bKHc0aAbablQZKsTBTPixTSd5rQWnQwREx9OSh1kqjviyJbBCL5ccybO12CUstVlQbZAceiKUJLdy-KDYgUK0EhSJHI9hL3b17zfPNwYQb4ac-PUlXKwjltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=qbaoIW3536WIEQ9v1zVKjtlmXLOOUkbks-TVidZ6DNCMUaEbEJC3a-6T0NW_jwKD7UBzCAQz2dc2V9E-gqtwssxS3jZ8-07XfBp4CpMU4P2plzGd6_jRK-kUhj6Tz82x3VlNiGghDABw60iEgEzGX1vpJXGUlyZU6INlTjjr6DPToNhqLCL-SgxuYMpprUJszXtwvUDKysUuXC44pVwYiT9iSe_JR4bKHc0aAbablQZKsTBTPixTSd5rQWnQwREx9OSh1kqjviyJbBCL5ccybO12CUstVlQbZAceiKUJLdy-KDYgUK0EhSJHI9hL3b17zfPNwYQb4ac-PUlXKwjltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=pjC_DEJEPCMHqnfRvewQGpYGYFsIz95PFIVTSfFUR8btOGsP7oodDUfblt1c1b1Dtf5hGIj9ev_wESn3ZQC3LIS0MzMdPnq3Buz1piRhIGBVyoHp5bDCZbTahYGjc8te4uK9xmc4I5LjTp8SIm6sNcA7F9MyoFLqTuqbyqWjOjbIjpy4cGrsCelvI4kyGohSiZVlGNFTDJV0hf3B32jZBGZXW9tlwSHMlqS6N30SNFfVGYLO8Z-PsmPC1AmvoODvG8TfIFy8PlwlwTxeAqPV47vNYq6qs6XgvcbQ6Ni3zlFtyeV_N8L7anTiAbLP-dsF8qdf4zQmoHnjCFTdUVqpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=pjC_DEJEPCMHqnfRvewQGpYGYFsIz95PFIVTSfFUR8btOGsP7oodDUfblt1c1b1Dtf5hGIj9ev_wESn3ZQC3LIS0MzMdPnq3Buz1piRhIGBVyoHp5bDCZbTahYGjc8te4uK9xmc4I5LjTp8SIm6sNcA7F9MyoFLqTuqbyqWjOjbIjpy4cGrsCelvI4kyGohSiZVlGNFTDJV0hf3B32jZBGZXW9tlwSHMlqS6N30SNFfVGYLO8Z-PsmPC1AmvoODvG8TfIFy8PlwlwTxeAqPV47vNYq6qs6XgvcbQ6Ni3zlFtyeV_N8L7anTiAbLP-dsF8qdf4zQmoHnjCFTdUVqpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=VlmayypIcIKJpM_Q8MdwUyYzoz6xEc3RsOfDGeW1LwwsyfcTTjwUqWaU-2sdzwTj_B_47nyRsxdtIByTrZfP0xsKOfGEImWud5sUshbBPGuDcKx12msUmMPkuh_1Hu9yztCaOywDiqHxZ7c5KbL38SjYeDN7SHcVTh08KraVU_MIy_tLWtFDczuJ22L8Zd8AVYbhIkmgueLr1_OItV3RcdZnYHRbS6NLPNAy7XTzQ3NVolr_-frDzfDgmkqvQHEjUIzitclSV1hO-YJ06f6SjFZblLlMf5f8SZUlKVl7RgSIyv5CtkCOwLcIb-njVpxB8-Lqw66W40sOOXsSScUtnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=VlmayypIcIKJpM_Q8MdwUyYzoz6xEc3RsOfDGeW1LwwsyfcTTjwUqWaU-2sdzwTj_B_47nyRsxdtIByTrZfP0xsKOfGEImWud5sUshbBPGuDcKx12msUmMPkuh_1Hu9yztCaOywDiqHxZ7c5KbL38SjYeDN7SHcVTh08KraVU_MIy_tLWtFDczuJ22L8Zd8AVYbhIkmgueLr1_OItV3RcdZnYHRbS6NLPNAy7XTzQ3NVolr_-frDzfDgmkqvQHEjUIzitclSV1hO-YJ06f6SjFZblLlMf5f8SZUlKVl7RgSIyv5CtkCOwLcIb-njVpxB8-Lqw66W40sOOXsSScUtnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=MWPi6f1dieF6Mxft7ppZjdcwqwG6whkQMbD4CXRMwdCCJqVck5GcQXg5zbXXtrBx67juQyTyvHLWMRtJxM6cRk_BBMc8rc6avHyrzhUY0LeTHt0f8S5BGnjOB3v0xWEq2SqEsplLimRysicV53Lza2R4QV_tfhI5sEwriyQx-mGf2dKsEb74M0rKqpkgwx8U4aBmzGmI0U_6c_CitwCp2zUEogPBBrc7WU7m1OQNU5_hDJVBK7lbdtAZaZ6tWLjUqApJtiy1kyttNqIqE5LHqmbdL0b1kmODR39L10IzKa_kKrUmXwvbQt7dbHYX25do_72iBb4MIolrsl_y_YD3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=MWPi6f1dieF6Mxft7ppZjdcwqwG6whkQMbD4CXRMwdCCJqVck5GcQXg5zbXXtrBx67juQyTyvHLWMRtJxM6cRk_BBMc8rc6avHyrzhUY0LeTHt0f8S5BGnjOB3v0xWEq2SqEsplLimRysicV53Lza2R4QV_tfhI5sEwriyQx-mGf2dKsEb74M0rKqpkgwx8U4aBmzGmI0U_6c_CitwCp2zUEogPBBrc7WU7m1OQNU5_hDJVBK7lbdtAZaZ6tWLjUqApJtiy1kyttNqIqE5LHqmbdL0b1kmODR39L10IzKa_kKrUmXwvbQt7dbHYX25do_72iBb4MIolrsl_y_YD3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=DGfm8AuMlSxU-zVI8ftoIWkfIBAL8KbOaks0PHs5MrubQGMKaVuSKNCAK9oIwoFu9NUwDkHWQA6sd-vQCViBXwSPuse7Od22KksLd1i8JwDLv9Es9YgvLwhC2pMxeBRRxt36zuCVU1O4j3CDtmUBCT9wA0lspD9DuyGn8OFs9ViuIPJjby0LTSiXP5jgoO8Wd7hCXE6ue-r1scGtptFjTkVFd1bNrFYt0WWGyxUKI-krrVqaTVGT7U5PjjUEDMribwPdM6VYOimfv_scYZ1Lam0WOsxrp80nlgtFop7AedW0BzB6LXFlmgvW7UVf5aJAKlmPV7OUHGcNg2sbix0ZXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=DGfm8AuMlSxU-zVI8ftoIWkfIBAL8KbOaks0PHs5MrubQGMKaVuSKNCAK9oIwoFu9NUwDkHWQA6sd-vQCViBXwSPuse7Od22KksLd1i8JwDLv9Es9YgvLwhC2pMxeBRRxt36zuCVU1O4j3CDtmUBCT9wA0lspD9DuyGn8OFs9ViuIPJjby0LTSiXP5jgoO8Wd7hCXE6ue-r1scGtptFjTkVFd1bNrFYt0WWGyxUKI-krrVqaTVGT7U5PjjUEDMribwPdM6VYOimfv_scYZ1Lam0WOsxrp80nlgtFop7AedW0BzB6LXFlmgvW7UVf5aJAKlmPV7OUHGcNg2sbix0ZXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=hZq1KGW0DRg1Cr67bd24K9ZNHzY1a_LTAubyTuIDVhFHsa7exKsPG9KjDw1Mayzk0yO3HD-84HTFeZaLSZkKcYhm6TUzAlZeBIHHRHAE141mwkDkmEMSrs_JZa4P7VFj5NvK0cNsWfc6GCly9iss2C3qi8mJAGDRWwcTQU4hgYGuZubiq3HPI-rNLFjmxL9gdDwo4wIUh2noy-6vkagGCaTgg5D2sDq_X4m-9B7Dby2JKIRAAJ3qaQPeSLUCfZdASuxrugW7oSNK4NZ0wOksIdJgrI5HcpvxjgI7yzu8ar6uIA18X1-yNkaSPlVIo2hDD9Jk7PDZVrsgKpCoBVbf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=hZq1KGW0DRg1Cr67bd24K9ZNHzY1a_LTAubyTuIDVhFHsa7exKsPG9KjDw1Mayzk0yO3HD-84HTFeZaLSZkKcYhm6TUzAlZeBIHHRHAE141mwkDkmEMSrs_JZa4P7VFj5NvK0cNsWfc6GCly9iss2C3qi8mJAGDRWwcTQU4hgYGuZubiq3HPI-rNLFjmxL9gdDwo4wIUh2noy-6vkagGCaTgg5D2sDq_X4m-9B7Dby2JKIRAAJ3qaQPeSLUCfZdASuxrugW7oSNK4NZ0wOksIdJgrI5HcpvxjgI7yzu8ar6uIA18X1-yNkaSPlVIo2hDD9Jk7PDZVrsgKpCoBVbf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=g24nHF4OoOlFlidOh7RLSIvdATp7d7I7fJ_LAXMg4iE7A7S_DMgvpeKRJjGkjW5b2otyadtbs6qf7xgMclJycJJUC9ZLEZYFzgHkQotCn4CKfgiuhlxC-_IA2r7wxVDmjGF1Ck4eCosmhZWHLmBVxLqr1yCyHocJ4f84007XjJG7mE2wOTihUaLcHsVNRxEbIuqrMPGZK9WUH8eNz2ALQMq6O227hMK_gQm1zfH_OeelNpoBweDyHX_dJ7YujzRWDWWI0PHt7oXKMzsBkZ_p_wbsyt4CE010bkI7gMJpnONtQXuucw1A1zfpb0vq6iHf5DGb2PSTPlPpA_RBcFMKKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=g24nHF4OoOlFlidOh7RLSIvdATp7d7I7fJ_LAXMg4iE7A7S_DMgvpeKRJjGkjW5b2otyadtbs6qf7xgMclJycJJUC9ZLEZYFzgHkQotCn4CKfgiuhlxC-_IA2r7wxVDmjGF1Ck4eCosmhZWHLmBVxLqr1yCyHocJ4f84007XjJG7mE2wOTihUaLcHsVNRxEbIuqrMPGZK9WUH8eNz2ALQMq6O227hMK_gQm1zfH_OeelNpoBweDyHX_dJ7YujzRWDWWI0PHt7oXKMzsBkZ_p_wbsyt4CE010bkI7gMJpnONtQXuucw1A1zfpb0vq6iHf5DGb2PSTPlPpA_RBcFMKKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=SOPetZW1U6ZERDhJ2XYo8jPVtFiLY2lzhZYBxdQMKxsXRztt_e3ymCIq-D7seMUOWzEQcPzNMnhc05OeK7vqQw8lVpyAcuEbHBntHWOavfo7wODi2DeN_3S5BpQLBMnfH28ALMEEgP2T7EfE_h_qCds_P2XdGifzm1-Ae6atiE0YbOeYGNQ84M3EZUQsQLKhIJIMUgQQgy-1bFpOqLkzg_GPPAqqcuURiTwRZ73tOkkGujYK3IZ4XyCHHba4QBZv0Iqr01o8Pfxa9YOxTwLSojRCBa7kfL3Rddp-qnAKSAoNroMgYDPK3ebJcDekIJ0eiU5ytMFUUJMMVEweFGY5sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=SOPetZW1U6ZERDhJ2XYo8jPVtFiLY2lzhZYBxdQMKxsXRztt_e3ymCIq-D7seMUOWzEQcPzNMnhc05OeK7vqQw8lVpyAcuEbHBntHWOavfo7wODi2DeN_3S5BpQLBMnfH28ALMEEgP2T7EfE_h_qCds_P2XdGifzm1-Ae6atiE0YbOeYGNQ84M3EZUQsQLKhIJIMUgQQgy-1bFpOqLkzg_GPPAqqcuURiTwRZ73tOkkGujYK3IZ4XyCHHba4QBZv0Iqr01o8Pfxa9YOxTwLSojRCBa7kfL3Rddp-qnAKSAoNroMgYDPK3ebJcDekIJ0eiU5ytMFUUJMMVEweFGY5sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=Ns-Gqi_5XHS31UagR8AY_7yPEHLj5Y3y8x1fnv7tZVPM7cx_PG4FbAzPN9XsvjJi_M0454UBfGHsC8myUPRrdOqb6310s9RWHAILGqOvaP1-CiZZtY2qdiC4odyj8IEE8J0OC1KugVNJPgjJbL-DIVJZxiqXD4ia5XLNckLehb24qFthlqCHjPsToCoLJDntX7VJqV7TqrTPoTsJu-OXnyb9h86afhQl3BT79Tah03LgCBAbwSFKOTp9KmqzXh39dkATWLoilGx-WIoSVnVDW84dQ0CEsApyR43JPOxWMYZ3MfVFxbIigdGkF0xbGLRfFyKYZDQTr3l5x9VDfWem1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=Ns-Gqi_5XHS31UagR8AY_7yPEHLj5Y3y8x1fnv7tZVPM7cx_PG4FbAzPN9XsvjJi_M0454UBfGHsC8myUPRrdOqb6310s9RWHAILGqOvaP1-CiZZtY2qdiC4odyj8IEE8J0OC1KugVNJPgjJbL-DIVJZxiqXD4ia5XLNckLehb24qFthlqCHjPsToCoLJDntX7VJqV7TqrTPoTsJu-OXnyb9h86afhQl3BT79Tah03LgCBAbwSFKOTp9KmqzXh39dkATWLoilGx-WIoSVnVDW84dQ0CEsApyR43JPOxWMYZ3MfVFxbIigdGkF0xbGLRfFyKYZDQTr3l5x9VDfWem1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=k31tpFgMCjly3Qa-I8lXtIeb-HWBlQBW1Q_b17lu8VB-de2XsAdq2XGaogfUqVEJO-kVlJw4EYy12qQ6_cdX5DBbiSHixoCCOk3OqbmlLS1eaQP8m6i-VCwGgxUggxqvoe3c_ryK_6cwROTavY7QaNVXORL_9dYHKJhVnbRsqeXgCZUW9Hi_cA2BPDpTUfBbgXVms3ANI1uIXCaTzNSKAhCl1u8Ng646r9vlGrfHsJE6w2xeSqgCXDk2ox5yowPyqvKzB0I22KGuUqI2qP36lo440q4WvKVtWaFc3YTM6HmLI5eVFCgTaDmN67kUN3hcH-Jf3ror26FXiGBcs33jtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=k31tpFgMCjly3Qa-I8lXtIeb-HWBlQBW1Q_b17lu8VB-de2XsAdq2XGaogfUqVEJO-kVlJw4EYy12qQ6_cdX5DBbiSHixoCCOk3OqbmlLS1eaQP8m6i-VCwGgxUggxqvoe3c_ryK_6cwROTavY7QaNVXORL_9dYHKJhVnbRsqeXgCZUW9Hi_cA2BPDpTUfBbgXVms3ANI1uIXCaTzNSKAhCl1u8Ng646r9vlGrfHsJE6w2xeSqgCXDk2ox5yowPyqvKzB0I22KGuUqI2qP36lo440q4WvKVtWaFc3YTM6HmLI5eVFCgTaDmN67kUN3hcH-Jf3ror26FXiGBcs33jtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J__UM0vRWzdUx8buMz0w6fTQXWoC-BtIi5aquNRBkQz2XKksehrJZgfTpZeHKGGJAHH8vNrlDVHZ5F_q02_CFeAsBIINZZRPDq8Eb9BYSUVSaxSrMArJKkoE3kuhIxbY-n_Wbi6MK7FoqM9_1xXe0jij0qkVA59zitYTL-XfFnKtAmWOVth4Dj60wQReJTyiQ73UfyDy2JemZLchNBlENl4Aig6IlA70KIV7T7bIvLSCTnMnlKA4uTckwAhXRPOO20yX-S9LkX3xa_UfXSPl7_U6KM5q5PffqpQpETedSxWgIEOKdgCWqzaflnoVPmo5_f2XviNJACGTY7dMXaTAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E93PNiVU_9hhOJCexaJcs1_s3yy62SMIQXJMdX1lvOHEdgjOADHvM42atm04YT90mU0AeUMX3IXhWeWu2Q7s8M7tlccmTDs7nvHbkDMBwuuzKR5dKRVGCTGvxKYyz_T3ARxyk7h5cQVxacbxU5acOrcX1B_jKyhf9DFi0pZZP3wNrQmtygc_cAeJKk179jbG5jIgwH56QDgHClR9p4pMnxhFSG100hxVLqHOL38t-Ar4tWrZY3Zlvq7DH4lznphiUHmHZCWT0lh2WJJ8eLhkbhWy7O45-BhTQLHXR2oXsECdD7UTz5x4Vhu0qH5_yLu0vbI9SCt1Jf4M_t0aEz-OdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWjtWBUPbO7Ui-NAOQmhny9_Cq__42jgHDoI-ZQ7CcBMoDXpAS3dg0LtJIThAbFHQ1bEzKLRX0eoRqiFLvrIGBQ4ygHg7vSgLy92y3RETBU-YEkrq7hz2_Je5hwLl8D4-IV8An9cZsZefhqGWWlqje_FKeOIUou0kvml1sbrky-YYV1Ng3Ise2J23NtK9-GV86iVFS0mjP0F4uLBmHKxRFv51yjITW5-64Bo8Zj2wYh91szAGbxOEykaDSdiQl4shnihcmCMR08ggE2orKvU87jMnb7dzn2hzkqCi3vlrMgvzCnlMGEhWf7nMH_5dxvibbovah8CEf2LHOzp3MR5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW7Z8yWGz-97GTyWZj9uziA2dqsMLHsUFd471aia2isyuBEFBrKjeJdD-5GNDfvd7DYOpS6Nhpc1e-KgPB8yEQPXJvXRJWj41kh1iUqlavpGL12Gmqctn-zXHS6LyYAYPDH9plJN3jbiin9eHqm1J1oCok4C8HgjNoTSb3FhgJcZvK6e6tRQItJae8seYWld8h1SEpZyc5ay48KCwcaALOrYAwjfzH5SxDoO8IDquBAFxwk7iw4f8YDPoapri2UA6ynwCEJK_7LTBHJCf9JneZnp7UaZ81tFjBhw5IePgZBb_cKtIiaUlwdTvT_ur-JaiZbKDpTSv_L5aKhZ7gecww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvCkDSZ8O863B7T78ELG3EhQzhDfvnNJQSnpR4h0jE4soCC8mrfgK0yjBGzrr2BBTMx5ssu5gdazMGqRyL8jCwQOvGwURNXnNQc1inVeht6fzr3tOLfBMX1HFuFu5LK56h46HHT5iY_3EbfSosbttSEHhHRNvH_Er04azq-hTL43VfctQu5o07mpXVW_35lwzR3cY0KdwXCPMvR4eaRdSmRqaQ-mh2xyxc_GOU_hh_nwL9Lwh1Hp1aAHfoFkxfUS05ulbDEKLr8a3VvE41hiI8f7vieMIoBzKOfWcRXFYNHPNgzfLfqH-tS3RkfJda_aqgS3A-OB4JLAWII0FRn8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fssQ0jhqkUsS6dfJyUxUUlXdDK6hYuhPFnmDF9V0mRTIY4F8cH4KoeyR0LapBV_yHBg2t5AgfsuRxSG1odzogHO09x9fLrVZ_GNaNKMPhQlOybzYVneZagPykJ1dFRHuO495tPqupZgwqIhxFTkPpMcrqUVVMlISJyOTc_yFTYtO4vmUjqJIIeaFo2k5pBRAqo_9xtqQzYZlQtJ5NSLIv_owdN5e76fYo-0A4OqQYnHQNx2KMPYOnXwmd7NO7dsBszJNwdFq3twDz3AzTHAymX2DmpwoUdZlA36NOqJQSer-ctKf_1Elo8EIxdErY-7cCC26iavtENrB5Dtb4XaavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=ELPTg3BOo9WCUDTUBanhecTTLexAyC2bzZN_AvpK7o_J7WPUuMsj2TXCIfY6JxFacd8epZABjY3Bi-1J3wDcJFV7D1zbD9FB8-NQxPnIKfFzsEXI5LXON4FX-udtTcZrJ2UU0MI-025w3QKMP1oUry0TfRAGLti-bDJThYap3e3WFKJBil2gCXXLSSj6FktYd_uZ0mpcolJw9X-qSYz9N7rTiZaUbbfTL9KdGr4RGpekTIvAkJUJlvYw8fnyBMcxeWtpMoTGVWzNpU_nNEZFjrsWLPHOsksQmsj81FMDRf2TJHLeEatYfY0eeORwnchJMFacIS6nL5jHZwJP28bDrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=ELPTg3BOo9WCUDTUBanhecTTLexAyC2bzZN_AvpK7o_J7WPUuMsj2TXCIfY6JxFacd8epZABjY3Bi-1J3wDcJFV7D1zbD9FB8-NQxPnIKfFzsEXI5LXON4FX-udtTcZrJ2UU0MI-025w3QKMP1oUry0TfRAGLti-bDJThYap3e3WFKJBil2gCXXLSSj6FktYd_uZ0mpcolJw9X-qSYz9N7rTiZaUbbfTL9KdGr4RGpekTIvAkJUJlvYw8fnyBMcxeWtpMoTGVWzNpU_nNEZFjrsWLPHOsksQmsj81FMDRf2TJHLeEatYfY0eeORwnchJMFacIS6nL5jHZwJP28bDrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=XZ9i2QI_k_PqA-Ru7fhs3UiNP0NvhuZ6IJpurzo_QzaSPfpyfhknWqK4LTCnt3K-wI9tDnPOmmwkmLcuirUx7Azmb3OQzysZsm5KqgDv9AX4tc2QL3YHJRGjZr0LFe24rAFEbjGV-8gmVPMGRyWccxvyTL-Q6mDdcfgLcn3j0mPj_ft1ZnWPqtmdDA_r84HXvNB0MJDDI7NFAzOorJEcSQ-h2qpt9no4pn-02vzN93T9ycoQsn2tqJyFlXYTKSr628cT_SNynm6qp46_qSsSg1rVKHq4SZn1zqEkb2uoQSdZKR0szi4xhJTCwnzDUNoHihtb2-Lehj0976djwjTzFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=XZ9i2QI_k_PqA-Ru7fhs3UiNP0NvhuZ6IJpurzo_QzaSPfpyfhknWqK4LTCnt3K-wI9tDnPOmmwkmLcuirUx7Azmb3OQzysZsm5KqgDv9AX4tc2QL3YHJRGjZr0LFe24rAFEbjGV-8gmVPMGRyWccxvyTL-Q6mDdcfgLcn3j0mPj_ft1ZnWPqtmdDA_r84HXvNB0MJDDI7NFAzOorJEcSQ-h2qpt9no4pn-02vzN93T9ycoQsn2tqJyFlXYTKSr628cT_SNynm6qp46_qSsSg1rVKHq4SZn1zqEkb2uoQSdZKR0szi4xhJTCwnzDUNoHihtb2-Lehj0976djwjTzFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=l8bIBuFLbWqspOXBJDe4ShgmLmfVnA7qO5pFfo4JwL5cpGD7JOlpDrTTc20F2HLWe5dTMa5iYorJS__J-gkn7IZFb3PDNopFXrA5cTlKez-E8Kgz9P6vJ46YnS3kmUw-LwXf5VW8O0CkU2VU4CozaF8oHJs8Bd8M-5i6Og5ov6BmwPGWgq3ycYjvi2vJvOMFnkPk-V35_tpdiV91MdlSdbI-IIdqNvJkmR9UEqkYvdV03iGIU1uD2AsBe9dMvM2LMog22ywTpV9TzKPFt3JZBNF6KGgZLr1gscRHzO-BqCQp-YmvaQMM62fwfB9fzM85FKARrp-tPzrN8T_NfcSVjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=l8bIBuFLbWqspOXBJDe4ShgmLmfVnA7qO5pFfo4JwL5cpGD7JOlpDrTTc20F2HLWe5dTMa5iYorJS__J-gkn7IZFb3PDNopFXrA5cTlKez-E8Kgz9P6vJ46YnS3kmUw-LwXf5VW8O0CkU2VU4CozaF8oHJs8Bd8M-5i6Og5ov6BmwPGWgq3ycYjvi2vJvOMFnkPk-V35_tpdiV91MdlSdbI-IIdqNvJkmR9UEqkYvdV03iGIU1uD2AsBe9dMvM2LMog22ywTpV9TzKPFt3JZBNF6KGgZLr1gscRHzO-BqCQp-YmvaQMM62fwfB9fzM85FKARrp-tPzrN8T_NfcSVjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=rqGuEcJQAN2zLi1BeWtzcw17ZJfmmPe6Np9dFCPxofY8OVBMDjR3icJgVDN3FrjNqVwhc53Z3GjQIlceq3euv3OgQSUDHnVKrKEs_lWyeOl5-bxCKTHzIv_L6RdsxjhH7i2r6c8F3BA-AU_JgRHTdBexw71tlLBNETmNOHbwAXE54HaP6VDPugvoPYWSUMWpyRZKoxZa16Evcg9zPxX9Dk42g88pfg5iO4fFTwVtiAfBlMoTzcTxdgWcEB9drTT7bH2t9F_fPbg2PMu9SH1PfWyy_sQOOpLo64JP3CtCuN2QUXOEfxjiCPliyjtBVAiXC2VNx8F8g8s9X8Yw3CP5DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=rqGuEcJQAN2zLi1BeWtzcw17ZJfmmPe6Np9dFCPxofY8OVBMDjR3icJgVDN3FrjNqVwhc53Z3GjQIlceq3euv3OgQSUDHnVKrKEs_lWyeOl5-bxCKTHzIv_L6RdsxjhH7i2r6c8F3BA-AU_JgRHTdBexw71tlLBNETmNOHbwAXE54HaP6VDPugvoPYWSUMWpyRZKoxZa16Evcg9zPxX9Dk42g88pfg5iO4fFTwVtiAfBlMoTzcTxdgWcEB9drTT7bH2t9F_fPbg2PMu9SH1PfWyy_sQOOpLo64JP3CtCuN2QUXOEfxjiCPliyjtBVAiXC2VNx8F8g8s9X8Yw3CP5DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te6GViU2tc_bM8R-BZEvRlXXzi9Ul1VG8y6QGFwpNzMA724DkQWO97rxYD03xSweyf-WKW1BneYl380FOLtc7F0QaQrepDfZdBVHfKDuSzZf6heVFvsyqIDH5VokVgR0TMSTPfnHi_TxVozzO-vyJmVAT-VtgIjGdXMeucUSAraxMxJMQ6QA_bsy3-36fgWJIw_IFroC7g0VE43y_IBTDf-T4lHLytjmgS_noEFksZTNkSzWKBqN9KOVxxihKc2rmeiPOYbx2qRCzpPuPb61ZqTU883spXNOHPER9SWKkx515UT7Cm_XOCitASOagAvOWacB9Ppzyg6moGccljNGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=K0buqQjldarnVUPd59ZvUJ3tCS0eLY8h5Y0gseLjx7jfIz_WWSAJRoZ-Nxpjb49XepZ9pkgHng67ZMiOPSISGVaPugE5r6GRrTXTFNF9WrDKlIP1Xe2qqrewAVDcaKylFT76XhtBv_l4sY9FKrEd3iwxpfyHHY9MGwgK2J0W5Cz_I2hOUl0TkA_WeSRrOfHLvMScAzce05D1RfLLQ3B3enItjKLsJNcmYkmoWupcUYIEVOxG9AHo9BYK2qNjPPNOaUMoBt3PcZ4bUtxEh7GUQb8AA4FypWnD1SbO1u6Ef1wcJOX-2awHm6E6rC_RcTEUyY1t1RaD-aIrsTjvxCTKCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=K0buqQjldarnVUPd59ZvUJ3tCS0eLY8h5Y0gseLjx7jfIz_WWSAJRoZ-Nxpjb49XepZ9pkgHng67ZMiOPSISGVaPugE5r6GRrTXTFNF9WrDKlIP1Xe2qqrewAVDcaKylFT76XhtBv_l4sY9FKrEd3iwxpfyHHY9MGwgK2J0W5Cz_I2hOUl0TkA_WeSRrOfHLvMScAzce05D1RfLLQ3B3enItjKLsJNcmYkmoWupcUYIEVOxG9AHo9BYK2qNjPPNOaUMoBt3PcZ4bUtxEh7GUQb8AA4FypWnD1SbO1u6Ef1wcJOX-2awHm6E6rC_RcTEUyY1t1RaD-aIrsTjvxCTKCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=U8x_uRR98o0Z9oK165uOb6s-54E6qoZOHY-wTvVVtU4hXvIE9eF4oHPnuhZV9On8V-hOGofco2CtrZUe2Y8zJE80t0kEvJmyeVOAv89gIy4oklkqGcc5KBGX-x8zJ1bwr-Argbvih0JcAYLuX52zgxAjqpwdz8Hp-zVMDIKmp1qWvt7FaEyVcpXmxcktcRYYWY8ZiLih6iMmxhUIz9f_g5-Uk4nE2dSygDxS4X5XiBmFKBvtDM1ni0kv0-jhagve5R1Rw27diGF78AoTk_1CYUOThWC5JTlbUqLf2l1qqkfmoFH24_lWtW4SuHOCY43sQr6nwAUxtpEiHdX4dS5D-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=U8x_uRR98o0Z9oK165uOb6s-54E6qoZOHY-wTvVVtU4hXvIE9eF4oHPnuhZV9On8V-hOGofco2CtrZUe2Y8zJE80t0kEvJmyeVOAv89gIy4oklkqGcc5KBGX-x8zJ1bwr-Argbvih0JcAYLuX52zgxAjqpwdz8Hp-zVMDIKmp1qWvt7FaEyVcpXmxcktcRYYWY8ZiLih6iMmxhUIz9f_g5-Uk4nE2dSygDxS4X5XiBmFKBvtDM1ni0kv0-jhagve5R1Rw27diGF78AoTk_1CYUOThWC5JTlbUqLf2l1qqkfmoFH24_lWtW4SuHOCY43sQr6nwAUxtpEiHdX4dS5D-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWN7vOH3M_ztfrztKYa8v4Bi_984brixKeB8pdvkQZQJDQf4s3KikwjHvtLkG7CvgIRvHS-p1YN6gqesGLCtmTuHut_xW3LlpYAqUpRroWin-WzC0PgkdZQGkt5YegRlX6d2goSj1Js3yFRtFvOiO8GkEFbhOPRmNVVi8418B7q22Vr-SH3bbymNcBlIphmTwEmlRoyvAjNUCkRDhYuihYzw8sPufALQ99kOd5ZEGkPQPCJvF5mwuEenAYwIrR8OEtOeWpqr1KVZzQayngqmCyJLCiPCJNhbnaalvdZ6_f6XXUarB9qbuz72E57V7ySWtD5yWsE_4KP2GDn0jBihAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
قالیباف در گفتگو با محمد درویش، رئیس شورای حماس:صلحی با آمریکا وجود ندارد و اسرائیل را به رسمیت نمی‌شناسیم!
🔴
دیپلماسی باید در خدمت حفظ و تثبیت دستاوردهای نظامی باشد.
🔴
مذاکره زمانی موفق خواهد بود که کشور همزمان آمادگی دفاعی خود را حفظ کند.
🔴
ایران بر حفظ تمامیت ارضی کشورهای منطقه و پایان جنگ علیه متحدان خود در محور مقاومت تأکید کرده است.
🔴
جمهوری اسلامی صلحی با آمریکا ندارد و اسرائیل را به رسمیت نمی‌شناسد و حمایت از جبهه مقاومت را در قالب‌های مختلف ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NE9A8ayEqQ_g1hk5UNYLArotv1EakjxlTCgE8EjIBlTEZqYR6Iu2Sfq3udCOUnHIJyn3gKKdMgTIsAJ0sXsjt61AXtIIkBGZ33gvac4aLnCVP7fi34oK3qM56O8NueKzLTRK-3JlQeh1ttZSA1vcnkyVMXLj2ZP3Oa0lgFkFVFhv78cItNF6E3xm2dzW8hzm4dVzVc9eK0YSYkf96L8nMR2cWwLkdHgD_q2AulE2DntY-N9gC9mdJ4LINYUCOh6V1e01xQ6SKaWN5cUwNPrnfv4ORR-yjGb5jxK39MIoCrfy0rxShQ0nua_NEKpTfHIct809GA6jv9vNjD0yU3vgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=GySe9Hq7prK1b8r8xcdH4IEKHR_vy5op1fFQ3w8j4GthgeHoylfq6DftWULBoy0FDb9tVN7VLvkEDkS_w26iJgwzEg_627aGxT2Z6ID4IoFF4Eh56omZ9skAXZ1Gsh6tWEnHO06xZLtoGde-5ywCTikGJuntRiZjV1pTQ2mMURiKqksyY4X9Q1eoY4EZLbKePyJUhtbaYWvx-mHO_MVgFcGRGI2AYqW14bbIrVltW7PNSa6ESzLbWxo79vzFxkWMC4JIOBBzM4THQIjWGcqMuBmUsNWOrAONTsNvBDjbKYfi379hXlYNsgGh6-Jh0-2VM3-QZptoDTFGDDeHbi_Olg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=GySe9Hq7prK1b8r8xcdH4IEKHR_vy5op1fFQ3w8j4GthgeHoylfq6DftWULBoy0FDb9tVN7VLvkEDkS_w26iJgwzEg_627aGxT2Z6ID4IoFF4Eh56omZ9skAXZ1Gsh6tWEnHO06xZLtoGde-5ywCTikGJuntRiZjV1pTQ2mMURiKqksyY4X9Q1eoY4EZLbKePyJUhtbaYWvx-mHO_MVgFcGRGI2AYqW14bbIrVltW7PNSa6ESzLbWxo79vzFxkWMC4JIOBBzM4THQIjWGcqMuBmUsNWOrAONTsNvBDjbKYfi379hXlYNsgGh6-Jh0-2VM3-QZptoDTFGDDeHbi_Olg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ارتش دفاعی اسرائیل:
پس از فعالیت در نزدیکی نیروها: ارتش اسرائیل یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را در منطقه العقیده هدف حمله قرار داد
امروز (یکشنبه)، نیروهای تیپ کماندو یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را که با موتورسیکلت در منطقه العقیده، در نزدیکی منطقه امنیتی محل فعالیت نیروهای ارتش اسرائیل، در حال فعالیت بود شناسایی کردند.
فعالیت این تروریست‌ها تهدیدی برای نیروهای ما محسوب می‌شد.
پس از شناسایی، ارتش اسرائیل در یک حمله دقیق، این تروریست‌ها را با هدف رفع تهدید هدف قرار داد.
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود ادامه خواهد داد و به سازمان تروریستی حزب‌الله اجازه نخواهد داد به شهروندان اسرائیل و نیروهای ارتش اسرائیل آسیب برساند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzxSRm4eoVhB-SySzPOiRAxk_-vRTnV4Y_Y6ekiY3fxyiUaxIUob8uyMeioh0YTQCQf9ldDGBiD53vn2cJvvq9jZYEzGeBSnLssFpCl6vVRoZmgC5wxXecKF3Ubgnbw483fvOGqGHBdbz_toPb55qWS8BsNzxxUUf4cMliBcEM14H3I0LwWnemF0MZqyo0Rt4YIJGLc3iQAvF4roH612NZatREE9UGWY066M0J87FyBhpk4QjCOZiA9OpUEfwoMph7BCNjSiqHUGopa2EheEG8aU2X2iOjHlcwB93TbS0M7rEu2phDMUtn201lEDs5WismMxXrP9TakfeB78GNa7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=dVyosYfT3vZA8aiRJYKUiratASOCqDybuM5UaP5CQHrEPB2BJgR3jH7s3ymTDHnKydMrfXplsAzN7Va_JTwqhn2hy9j_-rTYshNG6E4Ag5YCe2rtUoyQ3xOGZeAE_wbzQ285uwHCAreM1k6NI15vZc9rTBqLCzAckoZoKpax4qt82PYvJdedtFDQ0rvFk9oZjIs7E1h_bHBdKlWOvH0haPzMT6lLv6yCyZljlLmGKSzt0BMkvbcZ7jJ3omx24iaR6r9rYWHkEWQxr0cMueOsU8tHwq4XxlB8pysBy_WOadxK-q5FtOGjT78gnKTO_E3yJD6D89tgP-uTbjvDLrbkNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=dVyosYfT3vZA8aiRJYKUiratASOCqDybuM5UaP5CQHrEPB2BJgR3jH7s3ymTDHnKydMrfXplsAzN7Va_JTwqhn2hy9j_-rTYshNG6E4Ag5YCe2rtUoyQ3xOGZeAE_wbzQ285uwHCAreM1k6NI15vZc9rTBqLCzAckoZoKpax4qt82PYvJdedtFDQ0rvFk9oZjIs7E1h_bHBdKlWOvH0haPzMT6lLv6yCyZljlLmGKSzt0BMkvbcZ7jJ3omx24iaR6r9rYWHkEWQxr0cMueOsU8tHwq4XxlB8pysBy_WOadxK-q5FtOGjT78gnKTO_E3yJD6D89tgP-uTbjvDLrbkNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=AlsN1BKTid6YKlGhg_i7FbS9ltXuECCvw9grH_o5rIKpR92RfRG_n3MjCBZxQeuf3ivOJcUe93e_wXcp4dFPrEPtesE6582qMmBh1imaD7eNyqIL1fXWAzUETVJJvIDGNu6JBMRaXP0hpmkwGgT30u-hH-GfsVfYy2VSkCWQp1PdPKaIZl3FfxIPpgfH8Xxu0zrQSsP3u3x7Zpo_wOc5X-UT1l_FyXq55otUMEAgrg653hvoMrcZD6L8KuGS_Gig-SBWvGsRJjo_5epeQW-VvoQQHmPGBJXuwYW2326Z1gww8ROt5NLOjfkXMVMtvbASx4KgC3ZhG9l8p3mQ5bdUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=AlsN1BKTid6YKlGhg_i7FbS9ltXuECCvw9grH_o5rIKpR92RfRG_n3MjCBZxQeuf3ivOJcUe93e_wXcp4dFPrEPtesE6582qMmBh1imaD7eNyqIL1fXWAzUETVJJvIDGNu6JBMRaXP0hpmkwGgT30u-hH-GfsVfYy2VSkCWQp1PdPKaIZl3FfxIPpgfH8Xxu0zrQSsP3u3x7Zpo_wOc5X-UT1l_FyXq55otUMEAgrg653hvoMrcZD6L8KuGS_Gig-SBWvGsRJjo_5epeQW-VvoQQHmPGBJXuwYW2326Z1gww8ROt5NLOjfkXMVMtvbASx4KgC3ZhG9l8p3mQ5bdUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8_IqTNODNMUAusP7tSryxOfzEvm1Kv3WUze451Upw8MqEgXUDZMNJ0HNjRlAoQ9WGDN_A1rr-vNQBEqwLOBrI5jgeR2eBH-OVHp3gTuJ5yATzlroIzUv-XU7Gz5_V4hHHIn_eZdz4HNwYm7koQ4KNow5JA1R9s-nTotRLyPkpL49ZqhSQRg9RyJtUPw41Lp-bUS1NeqvHaFDEb2HQbZopr7vuVNbF95da5o-_qN3ZjGXt0F7rHo0sR7Rdz2RpPToQpjuECir5irEPQrHudIAq6JnQ9wI9T2DZs3bT6y6QdMWOk_XlGRQT960lbMkuOBimeXD3v1XiEj858_MYeBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=QiEye07BSmHbzLSsvicIEkDGnWj9_oScwjpUtVf2CsuYecuiFLvQuCnJ_29OmxOXXNN_RCUDsVH6waS8aAP19rRgGPPtmPsHRZYonfpgBa63zMrIoveCoY7XmO9pZ4EGArPiiBRZ7MVmgCR0aUD0Ezi0x4YAdz95Wo3YaLcaNq53Mc9dKjCdgEAG0C3aLj4Rc9eix5hyA2u-jj6cXyAO7AzsPegUbmsfNA4l2TV8HatNTV9q6qKy61b7XGGvx0mCksY_ahmYQQ_DlKnrrcXiQSN28B921XVcI016xnsw_o1fUmOdunkqrffmncqE7aooukCOw_Sgs0Gy13EjWEfkhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=QiEye07BSmHbzLSsvicIEkDGnWj9_oScwjpUtVf2CsuYecuiFLvQuCnJ_29OmxOXXNN_RCUDsVH6waS8aAP19rRgGPPtmPsHRZYonfpgBa63zMrIoveCoY7XmO9pZ4EGArPiiBRZ7MVmgCR0aUD0Ezi0x4YAdz95Wo3YaLcaNq53Mc9dKjCdgEAG0C3aLj4Rc9eix5hyA2u-jj6cXyAO7AzsPegUbmsfNA4l2TV8HatNTV9q6qKy61b7XGGvx0mCksY_ahmYQQ_DlKnrrcXiQSN28B921XVcI016xnsw_o1fUmOdunkqrffmncqE7aooukCOw_Sgs0Gy13EjWEfkhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2u1msLxQKBGTmPMKTE2NNH39Q5_5dpEkNFtvZ0eq6k-GuTSwvQw-pNWBrGSI-Bm0iMfELEEU-c98hHPeE4213L_fz8aGgBYlJx1ZsVkQv4GML3AWL6yzXDW4553kIHD4o_3zfZmvynBVlElBXFZdIttxtjyW3BloOybhAmWdD5WfjtF3I7tRJ8D6FbH8sb7zYdBXKXxs71JGeK47pGdAiuxlyUrYibENCJhkmayfctQ7KhWxs7UOV4P-ENHg4-wVcewrOs1ySkPDYP3rA3osxM0PL7qIlt2JdaOpU60dWI07nDtd9JBAB5JbOICVMR1Wfp7TdPDoszZQsawf5WTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=WU0LPbXdULhNmPWeR5SiThwf0ePdfJ9in3ScUHw5xBhzOk4QGab2H_vBeqmXiRbs1f8aRfqtsC0t7UOj-yKIY71KVJXm9yfsOokpXIQ21-qSOIH_HpFwljP7Nqsofx9YUU4AAH5malFxsvhtaYZsUB3iDjfOER2btMX0ds9bpgGtZHgpjc96xeQH0jrRV-C6J6Ir_GkTT0_Y8-z2RBv_vqtpCj-RRfOlUwBSgIaJDm7QnlqiOFfTC8TOyqgcqfCwKhLumd3O9cl4uJ4ElDwxhgYKoPEHXETGrutC2_LFB-Z78ScRWpwN0SrEJ0jmVcGbV7UIGiOmK77nXMhqGM1Pvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=WU0LPbXdULhNmPWeR5SiThwf0ePdfJ9in3ScUHw5xBhzOk4QGab2H_vBeqmXiRbs1f8aRfqtsC0t7UOj-yKIY71KVJXm9yfsOokpXIQ21-qSOIH_HpFwljP7Nqsofx9YUU4AAH5malFxsvhtaYZsUB3iDjfOER2btMX0ds9bpgGtZHgpjc96xeQH0jrRV-C6J6Ir_GkTT0_Y8-z2RBv_vqtpCj-RRfOlUwBSgIaJDm7QnlqiOFfTC8TOyqgcqfCwKhLumd3O9cl4uJ4ElDwxhgYKoPEHXETGrutC2_LFB-Z78ScRWpwN0SrEJ0jmVcGbV7UIGiOmK77nXMhqGM1Pvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfiDFlIgPcxqEdrZMby8BEyMEWZQpV7-DscF4o38oUl4SEyL5IGuYU-kmtq1RZIKmSvHvAVWJ-bHjZcJkWxpCF9ilfRztdwWaje18z_kpxIctpANVkjzwCtx74Hq6Ih8XR5-Zi4Lrejiu5yTJAOe2Dfv4rU_CB2Fuu4XA7vpv8M-BUP7WEaPrNbPfvVIfyhqepS5ImxnxiTatPGLG6fD-EBUcBRXGkJb9ZpZgVV3BdbU7_wt6rAQ51Zht75oSw5wq4jUbgpKn_VFoZHtdWwcJfWaRrfMVFeWNh4iEuT1Mk20faCulL49agJlXhMkZxuQNjxRPZA0H2JakMjyeTLkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=qvhGjZPEKyEPd0daZQrthGdVwIsaNRLnmvhNF0mVDptdKB0roY3GwJTBOlAEmBSvZaXtXcCA-zDvxEgtlMVctGbwIgVF5gXGEGo5EUfjMHlnS2s2Qdblt1cwU1K0h3n-mm9D_EE_wWZ58pZLw1OwYlMiY1MeueFp6ZRtrzgeFomAVwQnMvslx33tS8YrQJLDXlNM5pXT6fh5R2IL--NArMlvYcBvXRSK01k9g5tOo7_b8Vv_-51Tgw_xznwTWgXvhYKagTAtjsTR7-kcJyUtk1rPqtKteEZetmIdH1jIeAfthV1JEAE3e5murlKUvfrd3_EWROzBdtLvBIqFoXEh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=qvhGjZPEKyEPd0daZQrthGdVwIsaNRLnmvhNF0mVDptdKB0roY3GwJTBOlAEmBSvZaXtXcCA-zDvxEgtlMVctGbwIgVF5gXGEGo5EUfjMHlnS2s2Qdblt1cwU1K0h3n-mm9D_EE_wWZ58pZLw1OwYlMiY1MeueFp6ZRtrzgeFomAVwQnMvslx33tS8YrQJLDXlNM5pXT6fh5R2IL--NArMlvYcBvXRSK01k9g5tOo7_b8Vv_-51Tgw_xznwTWgXvhYKagTAtjsTR7-kcJyUtk1rPqtKteEZetmIdH1jIeAfthV1JEAE3e5murlKUvfrd3_EWROzBdtLvBIqFoXEh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=CgrLXjbIQ31fGTa9Ne72aowsXAxLKhBxDaBtJ-iG7sp9tmoLjrIfAN-u0F50bXzxszvhNjPe-JoSDZn5hf63eZg3q18OSw3HORRQgf6RwTHXIG3XwKM_HO86WUOylvgyk-r_AmNr2Xf406hT-j3SI_JAhLeBxrq3O-J6Lg2mxZFI9tKWW2d8lNQTmWk9xAeJt_1faCYdIEg3TyeQmB8GetGULKmYTKhruNW6x6ItZ-I6uqCY_14Ar1b64e6waiZlh0_8D52PiXjh9tR-HqIRwDqIxWRXOSSZmM6d6tQXZR4fFaBXgBKlhITzJC1CnsEjV8hrE7PU0hAFq3vHIsi2ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=CgrLXjbIQ31fGTa9Ne72aowsXAxLKhBxDaBtJ-iG7sp9tmoLjrIfAN-u0F50bXzxszvhNjPe-JoSDZn5hf63eZg3q18OSw3HORRQgf6RwTHXIG3XwKM_HO86WUOylvgyk-r_AmNr2Xf406hT-j3SI_JAhLeBxrq3O-J6Lg2mxZFI9tKWW2d8lNQTmWk9xAeJt_1faCYdIEg3TyeQmB8GetGULKmYTKhruNW6x6ItZ-I6uqCY_14Ar1b64e6waiZlh0_8D52PiXjh9tR-HqIRwDqIxWRXOSSZmM6d6tQXZR4fFaBXgBKlhITzJC1CnsEjV8hrE7PU0hAFq3vHIsi2ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CcpxZkxbgjA-qZgEoj_qBECBH82xlGiDTfRlWIBQPHwRUL3QBsJKUtFOVAN2KJy4W1csBP3jvGw4pTmpx1gNxhU84Rw4iBsWNPGXL9Xl6DMBkjapFIlJ_Gcl-CcM09N_mwWERiuHUplR0rwvlhj_B3VG3lFqQTJoJNyjIv1vXuh4pHtSZZnqExSduydF2qXHLacUHNTLaoBQliPTbXhsKTvEG-1VhM1BmwH8iYHRDVYDPPThbV4kAEhKMST8B0O_Z4yGLEUbrWYG3IwUyL0MoYCHxO565ZoxFeTKssQXt-eEyqI1yBoC8SoVqQqHjYUnKjmWfqjsvVbXRcbrXGYdBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Enx5RalnwuEFfOpQw9ZFvianK83zkCFH4wV98WikTriBNQOTGwLfe3ZELUTXlrxxeT94FkRuF_Kmtpmx4GmiUEi0BzpfOhr0YbydhxWFGP0C6f4IZ06fTsUha4qQytd0-beNnmvzyqqWerzP9zzZMx6wjWbM7mFRgL_9JRMysiIMNn0ZWeAc3xIfNRwAU22VK4tDlPUeotsFlJqebjKq1R-tRiicwEsMuuHGkHWmlDBOoD8c1ph8miGghzc28_xoIoAyaWRoT_ZGGO_sP8U-5tAMcJzZmQvJFQppuBk-E8RbGpGFysOJZuzDaUXn6sSep6Cv1r9mHiZCbfGuC1wQuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=HJIPHMOFN3WoUV0nSif_DYF9oFCmcfgyfH6zCiC8GE-t-l4o0mt8Vpnu9LhjQ44B9ghCKnAlICsFTVnafLegEoQEEfZTwR2W0bv6VKfRihAnYo4vxiMAe5OawS1XeCGlmi8B43AjB7UGHxk9GEb1_pbAkhwAjVNPw4bpoxux0AYj9zz-f8rs0MSsp7JgvDIe4kVaHrN2SHq93jizSB8csK4rf99AJ6CsUPrDOjtfnh1br_UI-Oy0rHjcdO_qkg1UtVTNw81oF7VD2UVZx-MCxB5137yACVv2FXbU-DHKzYuUMg73qhhLSMgJc3OzXegVScOZzs0Be2V7DOSuUDwohg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=HJIPHMOFN3WoUV0nSif_DYF9oFCmcfgyfH6zCiC8GE-t-l4o0mt8Vpnu9LhjQ44B9ghCKnAlICsFTVnafLegEoQEEfZTwR2W0bv6VKfRihAnYo4vxiMAe5OawS1XeCGlmi8B43AjB7UGHxk9GEb1_pbAkhwAjVNPw4bpoxux0AYj9zz-f8rs0MSsp7JgvDIe4kVaHrN2SHq93jizSB8csK4rf99AJ6CsUPrDOjtfnh1br_UI-Oy0rHjcdO_qkg1UtVTNw81oF7VD2UVZx-MCxB5137yACVv2FXbU-DHKzYuUMg73qhhLSMgJc3OzXegVScOZzs0Be2V7DOSuUDwohg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=TymmbsMrEYDvcUVQ2k6Oapr8Ytjn7UhZkUyYXRiX4-PJ9GGlWeqrXjwm3HPu9VjzcBTMe3lKXsFYX5Cp5V9PW8gX_1yJTUv-hop5XFlMZh_wpWtJw4rOcQNAutRQ76zyTEsIUH6UtZ_bzQzQfsL7UX8pndTY_L1olNamEuSjmvrAabWPo99DEkWSWLSjvSiHtSBl_Q7aoKV2P9aVLEyyW3e-JThNwRO8e-npkfak6i9bgvwDnMR9pH9aCH-R1Jrx8M5kE_IOkAdbIN5F9cCM89GxC-11sGg-w0yRTxvaks_Hmxv3_0_vyPnsW3M_g3zB1X95U-3J7dgQyL1W9od2DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=TymmbsMrEYDvcUVQ2k6Oapr8Ytjn7UhZkUyYXRiX4-PJ9GGlWeqrXjwm3HPu9VjzcBTMe3lKXsFYX5Cp5V9PW8gX_1yJTUv-hop5XFlMZh_wpWtJw4rOcQNAutRQ76zyTEsIUH6UtZ_bzQzQfsL7UX8pndTY_L1olNamEuSjmvrAabWPo99DEkWSWLSjvSiHtSBl_Q7aoKV2P9aVLEyyW3e-JThNwRO8e-npkfak6i9bgvwDnMR9pH9aCH-R1Jrx8M5kE_IOkAdbIN5F9cCM89GxC-11sGg-w0yRTxvaks_Hmxv3_0_vyPnsW3M_g3zB1X95U-3J7dgQyL1W9od2DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما در وضعیت دائمی جنگ نیستیم.
من خودم، به همراه رئیس‌جمهور ترامپ، چهار توافق صلح را به پیش بردیم.
تنها مسیحیان لبنان نیستند که از ما درخواست حفاظت می‌کنند.
دروزی‌ها هستند، مسلمانان هستند، مسلمانان سنی هستند و حتی تعدادی از مسلمانان شیعه نیز همین‌طور.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=S5Cq9aP9INGXIZsgHYlIUP9EORpyz0H6MajxbeFrBMGpbakZOC8klMuhHza8gR63JN3pLAoqMzRxyPmW0YykWTU4F__sVlyqemB8sNsIPRoq4H6VTpgBuK9BY0DsVNM3tE6JOUMTYvjRt7hy6h8FELXsuCMwa42vjO49iSxwMFNyBAZ9U5bzibuRA9GLQy5vLjX4-1ltr6NgY0yKaSyDW3FKsk3J-9qCRbx1THv2gl_2s9LzADMie4PvcUgsqiLVoTw9_ZdY4cx6GURyfvfNwS8HT8B6hmIhoTNUC2x4R9CCNto6x21dNNVy_359l5Bg9X5HmCcj-Q3DWQ9YdBKoKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=S5Cq9aP9INGXIZsgHYlIUP9EORpyz0H6MajxbeFrBMGpbakZOC8klMuhHza8gR63JN3pLAoqMzRxyPmW0YykWTU4F__sVlyqemB8sNsIPRoq4H6VTpgBuK9BY0DsVNM3tE6JOUMTYvjRt7hy6h8FELXsuCMwa42vjO49iSxwMFNyBAZ9U5bzibuRA9GLQy5vLjX4-1ltr6NgY0yKaSyDW3FKsk3J-9qCRbx1THv2gl_2s9LzADMie4PvcUgsqiLVoTw9_ZdY4cx6GURyfvfNwS8HT8B6hmIhoTNUC2x4R9CCNto6x21dNNVy_359l5Bg9X5HmCcj-Q3DWQ9YdBKoKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=pWZ98FZ6ZpUdAZ1l1FxH0TlR6COfjiGHfRrVpHRqEYrWRC_kuh0cfiU8bk0laxIMDefvsNmjZLA8d1ykzuuaNzygri5qL0JPP4FZr-ZMmINmtlXAcZw8mYPLxE9pInlvEbXg3CfUtz8nalQ5MgO-fbmgQHW8UD_QImZsPp_H3XeZ6JCC00AT6k59lEGsAP12NLzrGX46ByDsG0FZN00JT5Q5pzn3Sdu3JobzuASvmKn-jHP-PRvvA3y2_CyU6Kv-N4b5IRNtjUFIXI3QUEw3XgjdLHpv1XDkHpKWcBl90gEU2icasdFhvnkiOWR5neQ1EfHzFvmccLl1GoIpcAaK7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=pWZ98FZ6ZpUdAZ1l1FxH0TlR6COfjiGHfRrVpHRqEYrWRC_kuh0cfiU8bk0laxIMDefvsNmjZLA8d1ykzuuaNzygri5qL0JPP4FZr-ZMmINmtlXAcZw8mYPLxE9pInlvEbXg3CfUtz8nalQ5MgO-fbmgQHW8UD_QImZsPp_H3XeZ6JCC00AT6k59lEGsAP12NLzrGX46ByDsG0FZN00JT5Q5pzn3Sdu3JobzuASvmKn-jHP-PRvvA3y2_CyU6Kv-N4b5IRNtjUFIXI3QUEw3XgjdLHpv1XDkHpKWcBl90gEU2icasdFhvnkiOWR5neQ1EfHzFvmccLl1GoIpcAaK7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=afv4HJBxdkDmhJdyEmvhgtnsnUd4ffU6LD26Sq6-oKiUlVthfEytcnk218hrLC-zdOXnNAkKEMv3XPhfIO9ubW02kAqiGP6CO6nPPLGH0jg6JmUBw9XWiHYvBWcAHvU8cNV1aMe-Yu7tVl--QAY1_7beFYsyq8lxjRMAnpibmC4hADneCn2lwOesCuqgYFpSfaxJM4yLARNu6MpY7Dol-4I_QuwUdXbjLeLP-J1u09hSAqQsd16hPiOc-F32DE1sxA8zr-luzGtuwmHALDj-rrT-G722PwAY5AK5oDuHm00f6hNvvbpmcalmKBUSt3WiFq_05Se4SQsFuK7cCIFjKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=afv4HJBxdkDmhJdyEmvhgtnsnUd4ffU6LD26Sq6-oKiUlVthfEytcnk218hrLC-zdOXnNAkKEMv3XPhfIO9ubW02kAqiGP6CO6nPPLGH0jg6JmUBw9XWiHYvBWcAHvU8cNV1aMe-Yu7tVl--QAY1_7beFYsyq8lxjRMAnpibmC4hADneCn2lwOesCuqgYFpSfaxJM4yLARNu6MpY7Dol-4I_QuwUdXbjLeLP-J1u09hSAqQsd16hPiOc-F32DE1sxA8zr-luzGtuwmHALDj-rrT-G722PwAY5AK5oDuHm00f6hNvvbpmcalmKBUSt3WiFq_05Se4SQsFuK7cCIFjKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-mC43zedWOxRJVlgqKKFPMiwlaYGTN4I5cp83Mee40bYOd-SFg8hoakOBq0btPp3X8Ym7TN99Ktfz9vUIrXIXN4cMqbAWxwNZOlgzh18YceGdJSXiGfGwc-MXHO22Tms-I40kKcp5xEANzv_Y7Ij5l016KGXCuEzPZ8fIhc5PMl6ffHsFk0MTxwiqJQ6Aw5t83rQNiDW4gHu5a4zXOG9YKCZRQZQs8-Qv0uSqsQl2-da2W4jip-WRntAWUSgXgBYoynW70Hw6_ykzCCTTvusbuIsgU5njCmt2nGpRvE2qLXUT6hyYOJU-_NAlaNcRk4hlYxxPTvyNfACqYvUXLcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=HNLnLSWO0jlZb7FE0PRhU1hKdGDfMBX-BSjv14qiO8u-Qx2zu1mqq2zuyGFBUSEFFSDJbq0omrs-MuIxqj_rfJLAD_MJKbWlrvDV4XbMFI9bdGQ3MOw6MqZjgd9VAOuoME0VolzQVWKJG6-kElJ4LAi3lm9R1_rRIprVKl9z-moTYSScQY_KouqD1LRJtJQEzRpm58Yg90QlIzmfGHfL-qamDXckwcrVWtbo3Wvx1brovBSjLXZclx9RG98y3XG2x6_WBCnXrwi5c_Kj_AI5UVvzXPczf4RFUYseziskfU0PK5hBAEMohu1IamdvRO7wcoA-xikJpgvdaE4j38xaYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=HNLnLSWO0jlZb7FE0PRhU1hKdGDfMBX-BSjv14qiO8u-Qx2zu1mqq2zuyGFBUSEFFSDJbq0omrs-MuIxqj_rfJLAD_MJKbWlrvDV4XbMFI9bdGQ3MOw6MqZjgd9VAOuoME0VolzQVWKJG6-kElJ4LAi3lm9R1_rRIprVKl9z-moTYSScQY_KouqD1LRJtJQEzRpm58Yg90QlIzmfGHfL-qamDXckwcrVWtbo3Wvx1brovBSjLXZclx9RG98y3XG2x6_WBCnXrwi5c_Kj_AI5UVvzXPczf4RFUYseziskfU0PK5hBAEMohu1IamdvRO7wcoA-xikJpgvdaE4j38xaYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amr6Gi0Lc31d_MBKTgjkIS0H0XH0Wv3bNgFwU3vPuH-vdZT-vHj27Swyl_mToK4hRznGJ7Y8w95ZAZdDHoRA-601423oTl_QMvyCCtW69ea7ju3gpbvOuegspgwWhPkPS-u60pYwgb59GjQDnXaOjRNeo0uvF3juKyqNA4TAcm645ezH608LMMynV4RAziCx7Vlo8sWsHcgf7sTiMvIjFRUxE6C49VohOTU5xC_AoSKtpaPbT6d_xgxpe3JCWdbk0UGVsfO2qZDIomzlmAhCsjpYg5igfI98vMELgflf3RvU8ovJ-DBcDMRsBj3ggQS51p5yQWoC3nrkNkAViqhn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=rSmUsg6Zytf0Ou9go4EP65xiJ-A8ytE17uH4zpfnjjbmtqiGgdhANsvku-8YbtYuBDpB--EJmo0hkuX7nj3pqTEjaSFXQCs-ZIFNmRjdmidQXpxqWOmVlWyot0NzY5wY1CimVi-2EelB35wJJdAsPysS4dbb1zo0wbFD4GLoSn_YJVYhcQfJRcHLmuJSUrUcsXpfWOmxXv2errv94SuKcr9tYojtdHxSYZQkbgADK7ENKi6g6DtIBH5ozrYgOBpwCBRXGgg8CXeKWV5Y3DkIGLx-LOPqQn1NhwMQS4wJUNoAiCJpa75kfNb1lu6XWHMcrR6zc-k9RUJemoyJ1LIA0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=rSmUsg6Zytf0Ou9go4EP65xiJ-A8ytE17uH4zpfnjjbmtqiGgdhANsvku-8YbtYuBDpB--EJmo0hkuX7nj3pqTEjaSFXQCs-ZIFNmRjdmidQXpxqWOmVlWyot0NzY5wY1CimVi-2EelB35wJJdAsPysS4dbb1zo0wbFD4GLoSn_YJVYhcQfJRcHLmuJSUrUcsXpfWOmxXv2errv94SuKcr9tYojtdHxSYZQkbgADK7ENKi6g6DtIBH5ozrYgOBpwCBRXGgg8CXeKWV5Y3DkIGLx-LOPqQn1NhwMQS4wJUNoAiCJpa75kfNb1lu6XWHMcrR6zc-k9RUJemoyJ1LIA0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqLC72kmDvOo5cPUJ-KKu54IcSlXpismztgtlA56ArbK3c9TERgFGNGiDJegDLUUfXmJH8yyJHWyE10xAEs9TVvXbvJW5HhQJOIUxEgbf6P-GEvEkEB2H4XGP96vsO4Za2NeckrTk0k2jgM4E_4I9ogEd2KqiFFvA_GZJ49ekbBFKnz_DpzZLs5ppHX3gEfRT1ZvyKnHYD4bKmb94YfDu00XE47j_5JYz3XyW7zSBiI0i-KelX_bfuP3m4ISHzcVkm4Xqpnh6k8BIhdch-UkCeR9tXysRkyom0hQW-_xFwOjHzGq_zLJCrwP-yWPrTNboamp_KQW1Nz4tVt8LLSHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq8iJQp-k-g-A4oxy3VEYvQoTPGw6lZDxu8VFoKFd7avaM6ikXYO0btq-CIdj4K0bbLAGyhf1IlO_78O0bVqp1DBfa26fSBVyc2x9UFOK74vviXcgxOuzjVIdH-sU5hdkV6ZzVlvuNihHgX1LzfRtE-jefVZHSL2Yb2DpKFJ3QPTwjxwEfGOXSOtejaWILAlFt9YbfYoRr0y1_gyiiiPRZEF598zYq9OYVKdjsyceYTfdHRhb8NrxLbZCAMGGab6q_NE9RybtFbuxBtsiOVV0l94IH4f-LibkyYP9M1b9G-6l4K4dpjOZuigQr1LIUKElykaRz1K4swnnLRBImfvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6FZm2Y3y1iiAJVBAV2SICrap-lIK6YpVZLERhERaFWka29jMJUluzVJmzEOvQ9jlIMR67IHX-2_301ky74ls2pphP-sxmpB-eDQ2NdyoEJMKpBhq54R6y_nJlGIjTivIYpCkww8r2GA15VBI4_fy_8mY9kSS09OZHjrzhrZsMuUMo9WlMJSeD28USPFgSJORPETI74ZqsIMlrMn1-wefWmnUGohsbw3QBFIN3M05t8uFaAnfmqfKprucD9FggPnFHpVKczR7p0EDis5Q98hcISj3CaSmWIVaRFeC26Ab5jqOPFnWUiIpe7jgbUuRD1q5nLNzici4yQQF2dhfEf1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBibLcEyKwqziFC6wI1tRo0svGahW4KVVeQT1nwThFSI70F9GM1nOAYfRufgYc_AqIZxMOmO36pseNZvwfM03nm4ZvkIRqEYQK49NcYQZWBZd3DpGwsvWIY2ehWxrTqwqGgX_TO4hdfvzCuR4k8iGPwy6Axiec6obLrUUQ78TK9GGGXLOtT_dD4DL2VfdVrlonW9mKsy81SQvKSEMuIYU6-DWeHEkO-CoLJGjwMhD-9eFYTMb9dQmNTRn7yXibjFVq-A1Nkeg9JtIOolX3iBwGoLWvO5jTaBQabIHKgbeyb755Cg-hOoEcapWGzp8BDfz62bYCfqFREbasQnGHKkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=WMlIf0yagE6Lhg2Ab9zsHRg9P-RNJvtiNGIcbS0-bbRQ-SaxtboxPgk6fj5tkLLWNw1HumkK9Cg8UI6lG2I6fiWAdOwRzaLAn-by0s9aVDUeOjBjrA9XiskD3Wo8pvu8Shi03Ir9Gm9ATy7X78SfKx4ti-AKRIlsELx1ByskTxUtgpJirvVUE3hMoVAOg_4BOJJJQOlzX2PMKWAc6DGsE5OfmnXj80ux-GwEaGKyaxfiJ77idQx9Ou86pxyFhFZjbXUcxtp3T6q-_4myjKbKDaSpI8FaHWv5YLx5m_9b38-SyFyeFdg9tZm4SNSCNF3GrlBKUlLfCz9KDve5Obncug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=WMlIf0yagE6Lhg2Ab9zsHRg9P-RNJvtiNGIcbS0-bbRQ-SaxtboxPgk6fj5tkLLWNw1HumkK9Cg8UI6lG2I6fiWAdOwRzaLAn-by0s9aVDUeOjBjrA9XiskD3Wo8pvu8Shi03Ir9Gm9ATy7X78SfKx4ti-AKRIlsELx1ByskTxUtgpJirvVUE3hMoVAOg_4BOJJJQOlzX2PMKWAc6DGsE5OfmnXj80ux-GwEaGKyaxfiJ77idQx9Ou86pxyFhFZjbXUcxtp3T6q-_4myjKbKDaSpI8FaHWv5YLx5m_9b38-SyFyeFdg9tZm4SNSCNF3GrlBKUlLfCz9KDve5Obncug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=syi7pcR-_Cn0RBwOB5qPBLg81MgYxaO7smEvDQ5_QdV6VCk_n3M8cKHK7Qi6MRAjzUdOpHkM-I9Viw9GAhDRNN32WxpsKPfdLxmsBL0OmDvz-BuYgbpSQqoKR1I-M9bqXo3Qv9dpwcq9hoS0vDdsi-J2lww9teJF9yhdrLVGz0yND_KsN-9icj2gtedRw0Im9qIzIatY9SQ1UvujrJS1Bu6K8GmylV7XJasr3eDsVwS1Xwhh_3nuiYlzQHvzE3C0ZM1lEfYa4TFwO8RDzqr24RiTwa_HIDzf6X8XF09LhNla4I7I3Tr97H1cwwK--_7tir36VpW4bmLWeuEiH8tKZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=syi7pcR-_Cn0RBwOB5qPBLg81MgYxaO7smEvDQ5_QdV6VCk_n3M8cKHK7Qi6MRAjzUdOpHkM-I9Viw9GAhDRNN32WxpsKPfdLxmsBL0OmDvz-BuYgbpSQqoKR1I-M9bqXo3Qv9dpwcq9hoS0vDdsi-J2lww9teJF9yhdrLVGz0yND_KsN-9icj2gtedRw0Im9qIzIatY9SQ1UvujrJS1Bu6K8GmylV7XJasr3eDsVwS1Xwhh_3nuiYlzQHvzE3C0ZM1lEfYa4TFwO8RDzqr24RiTwa_HIDzf6X8XF09LhNla4I7I3Tr97H1cwwK--_7tir36VpW4bmLWeuEiH8tKZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiKeEH-8_svXQ2sdgfHxufSINUJFcOpSA1Sn1uFS-rs7384H7JOR-Y9KGUW0Nu2FWp-8x49EeF82XAy1zZY2u1l7FzZwxBux1zdKNId84ZxyOgVz-2LFbKCLNKDdmxDXBpcicZ42gdndlDO9mrRu62WKo0Dkq60Mk9a_uIcanBRAVCEPMsQMzs5-4ElihMwUQPrA1EZoz3RvKobyDGdimTqRTtkTexe8_AJUxcP6QLxBlrxKxEc5stmmz3BmcjinckcQCPNzTcvjjSxibJpRjwYTN4MHt5KSGYup77jB7MseEcVTx5NAM5-tD8MoIDYB4isBubA0343IX87blRSe_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAT_qnqFtQ92cM6sGNkGWIAPo4k4bMGR6RwYrViQgj5zP1_gEk9pgdGxDk67yaloQKdAgePvaxG3Jbbj2ahClWtuhrzdpfzDcOmQg_2jp-qn-gKUrXmhG__D3dOnj_1nBGL8f_uvizUjwTQ7ahjjzc0lrI6Jf2YHMRLm8nTcAw3v174eAx18Sjkt97b0U4BBKi_f9eCmgtjHr6yJLkN4-6h6FK9prc-T2EnFjZCACiZmfqrGmhyrWhqHhjttVsZPKl16zKWn1dHeUMHS_tS-GgsWGB74oLmqAkhBQVELSTpwpmR-6yfGU2Zi4X0aQAF--7mbTI_3jwsG1V8poTo2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=ZE7865OVdJ4MOUj7UI6HnWMuPIrn0TDmsrveHoei09DsYyv968udzESEQF5KR4lJzK4jqckjHzfYB87ZPCzfmcvXc_vf9hwcC8RhKcU7kJJSlBqiBK4WclaygRgriyPAPj42Zx5slVIuo6rLQbxGRUQ3w32DWFSTR1w-Bvom0W5JGbJaLEhYp5pjeYsXo42BAlKbvajdL68-LMrWZ3sUeWvuaYqpSbdPIiU36oXEI_Kt5pEBBtXOFwTamzSRoYO-4T8JgPpXSPdKFh6RPJ7HcO77HVK0anmWxqmPWbyI70nNMw8usHGS1DuhIm4UG3L5_XDFBaXyDuknG1E2VlF3zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=ZE7865OVdJ4MOUj7UI6HnWMuPIrn0TDmsrveHoei09DsYyv968udzESEQF5KR4lJzK4jqckjHzfYB87ZPCzfmcvXc_vf9hwcC8RhKcU7kJJSlBqiBK4WclaygRgriyPAPj42Zx5slVIuo6rLQbxGRUQ3w32DWFSTR1w-Bvom0W5JGbJaLEhYp5pjeYsXo42BAlKbvajdL68-LMrWZ3sUeWvuaYqpSbdPIiU36oXEI_Kt5pEBBtXOFwTamzSRoYO-4T8JgPpXSPdKFh6RPJ7HcO77HVK0anmWxqmPWbyI70nNMw8usHGS1DuhIm4UG3L5_XDFBaXyDuknG1E2VlF3zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=dY9S3TnmPiZCwD7smrfuZP8bwhwTP6oihYmGcUzrLA4c71rrpmwhXdsUEyZStnpUmqO_56Q63oKWNVV1b1SuEmbhOHTEBk8wQybbER4JbqgJLY8KD8oJD90-0R9qvPmzmunL5osDE2-IbpqqXLQmzK8Y7cad2U2F76S-e0LU94FJmlEbS2csHkEnD9hcjTmpBtYAHniFDAZpjHrqbXs3n-HiN4S0iIxkBr3ftc4st3RFffSrRY38j81xphwEO2Zt8ospG5LVbyM0Qd2Cc-FAtnqABlAGGt1hGWaFE_4a2cwofoN3Sf78TvVPX5NR8JmhtNNptLK7s24E_UcyshRlvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=dY9S3TnmPiZCwD7smrfuZP8bwhwTP6oihYmGcUzrLA4c71rrpmwhXdsUEyZStnpUmqO_56Q63oKWNVV1b1SuEmbhOHTEBk8wQybbER4JbqgJLY8KD8oJD90-0R9qvPmzmunL5osDE2-IbpqqXLQmzK8Y7cad2U2F76S-e0LU94FJmlEbS2csHkEnD9hcjTmpBtYAHniFDAZpjHrqbXs3n-HiN4S0iIxkBr3ftc4st3RFffSrRY38j81xphwEO2Zt8ospG5LVbyM0Qd2Cc-FAtnqABlAGGt1hGWaFE_4a2cwofoN3Sf78TvVPX5NR8JmhtNNptLK7s24E_UcyshRlvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=REL9ARxdEDZlo9vcfz7Ci4jhnrPikdKmyr7uvzOzzPhUPR2DMBUSwXzLE0a20pkYrUeUUHzekzfkNLeCkY0vUk07nO4NL0-rhdERbTsJZX9kEaZpLxjUkwJnVJF4u-AvMU1Pmrc27Swvi9Ysko_xpanv1zuVKpQfYs-3ZHdDUKmiZI5z5KejF66x8sCEY3cf7Ip6ZbfAN5zj_1R0quzeaTLfh_DPyGR46PbKyiF_Uvo1vNf4sy21wXEUwnjZXJgSFz7m1V-MTDCyezECMZIDd9muHP9YbTXdNL5qXm9fNJGMEanxTq7CuxO4F26odqW_4IYe8PvPUmemWd95UmJrgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=REL9ARxdEDZlo9vcfz7Ci4jhnrPikdKmyr7uvzOzzPhUPR2DMBUSwXzLE0a20pkYrUeUUHzekzfkNLeCkY0vUk07nO4NL0-rhdERbTsJZX9kEaZpLxjUkwJnVJF4u-AvMU1Pmrc27Swvi9Ysko_xpanv1zuVKpQfYs-3ZHdDUKmiZI5z5KejF66x8sCEY3cf7Ip6ZbfAN5zj_1R0quzeaTLfh_DPyGR46PbKyiF_Uvo1vNf4sy21wXEUwnjZXJgSFz7m1V-MTDCyezECMZIDd9muHP9YbTXdNL5qXm9fNJGMEanxTq7CuxO4F26odqW_4IYe8PvPUmemWd95UmJrgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=k4zCY9c37NU9DALshTZIgvXEU7kKn7CyBxKdT0IRtUAAIBRC8md65OzCuZ9KECqNikIV5GAkkXq7ftHpGXzAKjiMXOFf736ARafeGyAZPhVsmlhR-6xv5s295L4x5sCu4MGopR0UWuTJFHFfuyhahIAmd9Y8DnMMcSbTTrlT2lKbtFNUfDigUho1kd8p7o0GkBieIKQjJubJNMnY3gPBGFxHg3NY5NMPiU77OW6Gu3WIRdwMGTuZIKJOfPNOJy713Uc0aMpp2se9a_1vhGEyPGOAiFJe1VLizydgx1B3dP-VIjqyB7-6_x6d_X1gPP5UTmEF8cuubirF3TNKT-NO5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=k4zCY9c37NU9DALshTZIgvXEU7kKn7CyBxKdT0IRtUAAIBRC8md65OzCuZ9KECqNikIV5GAkkXq7ftHpGXzAKjiMXOFf736ARafeGyAZPhVsmlhR-6xv5s295L4x5sCu4MGopR0UWuTJFHFfuyhahIAmd9Y8DnMMcSbTTrlT2lKbtFNUfDigUho1kd8p7o0GkBieIKQjJubJNMnY3gPBGFxHg3NY5NMPiU77OW6Gu3WIRdwMGTuZIKJOfPNOJy713Uc0aMpp2se9a_1vhGEyPGOAiFJe1VLizydgx1B3dP-VIjqyB7-6_x6d_X1gPP5UTmEF8cuubirF3TNKT-NO5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=YmPyJOWW3rYYAzUKJ1YcAcd3LZI0hiSHWzDsA2y5YOVaIihCqo2haT1N7KIYhSTE5aKQ133G5q_Zn4lIxi5mL3wXQwxKiAKOs4k2DvpWcTGuQoIh9tAe65YDjAVcLBR2fhgLUTbFn6Adm1l6YMluUKA0Me06vsCpXVZ_q0KM9ic5tI0xs3iJzs4n40yruV_gui0ukkfQM8eehZRrdbvYcBpiTBGbxkmX8YFnIx8YQW0yGe62xfZv3ixN5coic221wQQ0njjDepG7x12hYg95FswSzug4F5aeuu5RMbBqvqJZ6XD_QszkOjA8XYrKOWlcVzV79SKCSUAPAqSaDyt-Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=YmPyJOWW3rYYAzUKJ1YcAcd3LZI0hiSHWzDsA2y5YOVaIihCqo2haT1N7KIYhSTE5aKQ133G5q_Zn4lIxi5mL3wXQwxKiAKOs4k2DvpWcTGuQoIh9tAe65YDjAVcLBR2fhgLUTbFn6Adm1l6YMluUKA0Me06vsCpXVZ_q0KM9ic5tI0xs3iJzs4n40yruV_gui0ukkfQM8eehZRrdbvYcBpiTBGbxkmX8YFnIx8YQW0yGe62xfZv3ixN5coic221wQQ0njjDepG7x12hYg95FswSzug4F5aeuu5RMbBqvqJZ6XD_QszkOjA8XYrKOWlcVzV79SKCSUAPAqSaDyt-Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=uOzi4xYyvTcrGVHVM2kzgv4xw3lKNbmM7GLkFY09gBaVWUE-U31NcYRZsCkumqlDWfLl2wGmcJswZHW9Qr9OAdmpayZkLkLyG5WiJZ1lL0r6rTCWk5HmBPpnp-NaTHK7SuC--yyTP39MBIbzQyFR6D8EwdE9UK6IuB893LCaEFUF2E4_shdOYylRjlBiafOuXix0GMQE9g7vQeaV9gWKOGyrVbdHJI_0QyNkmIPtWptItPx__HYn385kfZeBemIhedGgrrifxTeiWXq0fXUgvjCHNyepgG8iwAxxYokvfd5EfBsIg-mA60Oxss97nS2sHWJxMwONPuZVVS_DABBh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=uOzi4xYyvTcrGVHVM2kzgv4xw3lKNbmM7GLkFY09gBaVWUE-U31NcYRZsCkumqlDWfLl2wGmcJswZHW9Qr9OAdmpayZkLkLyG5WiJZ1lL0r6rTCWk5HmBPpnp-NaTHK7SuC--yyTP39MBIbzQyFR6D8EwdE9UK6IuB893LCaEFUF2E4_shdOYylRjlBiafOuXix0GMQE9g7vQeaV9gWKOGyrVbdHJI_0QyNkmIPtWptItPx__HYn385kfZeBemIhedGgrrifxTeiWXq0fXUgvjCHNyepgG8iwAxxYokvfd5EfBsIg-mA60Oxss97nS2sHWJxMwONPuZVVS_DABBh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJeMiFEzUS6Hc1eQzVm9i5wteR5GvluiahQkAf7lJb9YPxRz8QELXhAuTL6KjGvF54dGf2Wv_vmIptZzwgMSdXXEtXCiS6CRuUrXrD-u9f47Vlx3A9xPCJ3ig2luY9J7uqq-rzF5a5xiQaxNZ-n5zbpaZt0HlmF3_rzxZPSyV8ttCgq3CaF5ET8feRiaSH8QEauZiKXuGo598WGIusQp7TZzPmp-BrSTSEUDqWJ-XwQdDsUEv2X2K_j_hQtti00B2ongUc0V0m80DT0sFsaWqxf0xDqqT4oAuTETDfUYrt8SdrJx-cDV2sYZpY4yWvg88Hnj4Nctdpu5557cZSqVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fpm6EfrxdzWbG5nxVdoAQv8Yhb2rh0659xs6Ae2rTc_DugrCZVBwtcRi2O_CtYNhK9xF1sI5W1LtCeRVXC_-CoJe-M0PH0iOCFMEKSZHZ9dlOL0BBzf9yNUJ1-fYoUS-PQn2PC6YzEVqtAdkZ07HYSbOFB2Sdk2PextMsB8xQAOfR1l8u8OlgAZnHYiAxR_nyY9ErDa4OoZG6_mkE2W1k2UMsyh7VLHOlJUv-jtAScAM6mzOlFMpOxzO3cbQPIQEdQbmPa22prrZ42MxcRrygCfgqSFfkOQvdmcal3PykRHnRgs0K0Iw8PWzEIfS53SZb7Twiag1haf-l9nYNa0Ttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2mLGmWd8LA1uT4K-8lwOw0RefmqUsjRX_U4ZpQZjz-SWBydpb6XaVaN9p6Xbw9xFVTNEVXnb3aUmvAhg4qncRJNUH_b3T23Ba6_4q42OkD5tFCa_D0KdcEJpPKc9uz6pYx-kNd_WClQp9t3gtxlqcNUsVlcAF9GFdk0dBYJIzWjRu6mv1d8wW7L9EYp4ZwzabpXe1E3D-AdzthALUS5XYwYwL2MO4IxMt1JLw92YfLvwIhaXAs4SYR-LueBTZGvJEzaUXUUFRO8be6PdFbIt_fB7wkZoRMUGISYL5LZVwPmI4w5de7liv7cvMpWbvn8_YmtdeMAC8EdRd-27PW-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=g-IaIbO8flnUbxvwFGOsD4_ErhQ2FODEA3VKPqsNsGSC5wy-DMldC00oCkCNsIqDOXRCb3KVGUFWaadahDH8byphWpTIRHOJJfCmSzALCjbESPx9PgcOJhNS-GKNyTPWIKQEjjIVn8adsfBZrz7u6Cza8AoYdnvS0R4PdpmEE-aVC7f71KW2IrVPIGDZ7g4oKJXzCJqQBEwJRaklWxiVQUC8AhHO-tfPWNFYd4KLDPBiCYbMeuohs_X256LK4giKCqeswyeH1LUpErXxTo24em37Uk3-S9jF-NvBkx3MFkQoLjJwbyvz6lzIJ-BSOgi1jKbw-6wn07bhIjcKpAKqFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=g-IaIbO8flnUbxvwFGOsD4_ErhQ2FODEA3VKPqsNsGSC5wy-DMldC00oCkCNsIqDOXRCb3KVGUFWaadahDH8byphWpTIRHOJJfCmSzALCjbESPx9PgcOJhNS-GKNyTPWIKQEjjIVn8adsfBZrz7u6Cza8AoYdnvS0R4PdpmEE-aVC7f71KW2IrVPIGDZ7g4oKJXzCJqQBEwJRaklWxiVQUC8AhHO-tfPWNFYd4KLDPBiCYbMeuohs_X256LK4giKCqeswyeH1LUpErXxTo24em37Uk3-S9jF-NvBkx3MFkQoLjJwbyvz6lzIJ-BSOgi1jKbw-6wn07bhIjcKpAKqFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNrtv725FhUj4RpaxuyhU3vzxlkGRjtqpqYLp3cL4e1eCm3FBgoWx3vfVyngCe9K1Kv8cTMGeeSbbP_6Rp_fhUYY7N2g6hZz8nNaz7hQy-ip5PuGG8H9RGCpGP-ZdrB99C1uDOQ7Fb0QvrPmzTplC7mMQA4QVs54G1gEHbXqXjPy0IanDELheKYr4vxsBJBKQNGcP4ZisVI5LW-mUP2cS1bRVhsyWr2k4vpOYZ1RM3l8vsjU9WB7kipsmZc2SPFOQ07OKrHMwCfNtEDSpFeNuDi7UHGy669beeMKXCqaCAL4sJ0V1Z5oTEnN8sqfHAmjt1_ZbOXRYBXbYkO9dhNdyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=WV3bxc0EPEI4Mh_myTbvHEi-xd_7VxS9DKEDLkMUHaAkwT742SJH9ova1BjvibiaXH_BQP0rNQ2GGUKvClG2_1adUnckOMVq8iIfYRQrP8sFdmU_LKQtMhvwOqVng4AJkzBi8CrBfUDoABTJY_-5FgoG9pCusVFuo45BLUBcn8NU8j-tsM-Bmhaz4_lYDXqTVERnMkXwTtsO7L0W45bjySqHS_d1pw91f_uBK34YKQX04ykBm1HHLDBHOBR8gOb7YaCFSP1mYBT5hwDlnu_qTkDnZPphCJY2wOqqJvDHIeXfZ3NiHg6Sbp0Z-xSfM4J8i81ss8o1vJuh2mrYKweYsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=WV3bxc0EPEI4Mh_myTbvHEi-xd_7VxS9DKEDLkMUHaAkwT742SJH9ova1BjvibiaXH_BQP0rNQ2GGUKvClG2_1adUnckOMVq8iIfYRQrP8sFdmU_LKQtMhvwOqVng4AJkzBi8CrBfUDoABTJY_-5FgoG9pCusVFuo45BLUBcn8NU8j-tsM-Bmhaz4_lYDXqTVERnMkXwTtsO7L0W45bjySqHS_d1pw91f_uBK34YKQX04ykBm1HHLDBHOBR8gOb7YaCFSP1mYBT5hwDlnu_qTkDnZPphCJY2wOqqJvDHIeXfZ3NiHg6Sbp0Z-xSfM4J8i81ss8o1vJuh2mrYKweYsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mluUgFiZmxbp9XWsOuLik5fzrbaAhI8liieuMXNcGTjw_drIjm1JL_gFZHLk5Vqme6C5zIk8l1ObjHaljr2qRo-OEdi-Btt5kvWVki189XzdXwqSd1rsK2EF1PantIGmtGb4-nTi9-9n1eVRrOBcFs4_AGfNedoypeLwND0NomLfhwCa0aDZXFvqQemsxVPVipgyzb_-6hyXcXGcyV67iN1wgvFcwKQZiVRoFu6BzFVv9MlI6gBiqgANPyHZCuq66Xtyby_PB4kXhHvj_B6VREJ4nA6SGPybg-0ULpBhVfujeUQCcrsPuyR_mtWje-Qv6Q6D5TqVorbhrApRYC_07w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=IyPAAazYG0AhlmdQf8m6mNIcJ0ReijSxQgHwKSAUcmYox_62HKdnPc-gqw1DtRSlHm-utjDKj8FX2ifj8KrjoquSRT5x3qAT1yCI2hgmb4AIGDY7VYNoX3yBJGN3IS-W5CkCLGdFI1MAZBm70P4ltLqNxiGqbJn_5Zatr94r6-hqvPgfXElK7ixZGPZYTCvesaWuntz4zU1wtEifvMTRQZ9qvwuYzaM0KU89oX4UiV0BRgonWWPUyOcxTebWX43zQEiChTlMS9CPJHbffNcDFSpR1iUAoWfPvLzPWw6YXJ1De5jJCqs-lv3hIz9093MPzdof6K9lOl-i04VDz5ts1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=IyPAAazYG0AhlmdQf8m6mNIcJ0ReijSxQgHwKSAUcmYox_62HKdnPc-gqw1DtRSlHm-utjDKj8FX2ifj8KrjoquSRT5x3qAT1yCI2hgmb4AIGDY7VYNoX3yBJGN3IS-W5CkCLGdFI1MAZBm70P4ltLqNxiGqbJn_5Zatr94r6-hqvPgfXElK7ixZGPZYTCvesaWuntz4zU1wtEifvMTRQZ9qvwuYzaM0KU89oX4UiV0BRgonWWPUyOcxTebWX43zQEiChTlMS9CPJHbffNcDFSpR1iUAoWfPvLzPWw6YXJ1De5jJCqs-lv3hIz9093MPzdof6K9lOl-i04VDz5ts1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpBbfUC3T6awKjvfeQLhF6F3NwEcJgJGlxSSdqGLRPGbWi8rl0HhG0TKt0qYdJW_xC1s0mr9pDpqi4hDtOeoqIRYZXOcU3NetaBaGoZayAAAO59VxbZWrWCBB9EWhjoHQF1GRUDP-3CK0h4_OpMLiV6cwySLzq4pOUbiPPvPBHSRIZnSyb0m7ogcAkj7d5DngApektiWMRNHdoA2DolemM-MS-x0MB5YZMQ6jeIuEnsOyCX56JI8sOJyHWvCRdkrlf0YoToQsv3wQoUCi6Q10UARdmQFEc1ckShRv4tmeB4VBKqyM7gB1AEf2Nz2KbJVA3hNiPB4z79o2Q9n5gLy8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=dQ3h8KbUSLDn5fhbs-pSXRC2uYA36WAxpji71qwMdToY6L9r9PozSvANgtetmKw0kDQG_YYSDNPxEvIb06wzgiwzt-ZIm-hk07PrCXwdsxWrUa5jDDmvPriZEwRElEPmRjDq6y0PZGXUzzlMgalDQ7Te5iNj0od5QxNITpiHS6rrGZ_o_x1k15z7q6jrJ0qLgnOQhvYj3g_wLz94urFbKgmEGER5f1GY3h5jhuo1wOzFyPV1v6m70Wp_UuGhpU16Z2Wej5MoPnicCAxa_2JI8rqZdDqJmt-aM2LgSCIoI6IPrHYBI0WfX-8lyvFjBA2HUIpu3y-eoLJOGIbuZ53t5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=dQ3h8KbUSLDn5fhbs-pSXRC2uYA36WAxpji71qwMdToY6L9r9PozSvANgtetmKw0kDQG_YYSDNPxEvIb06wzgiwzt-ZIm-hk07PrCXwdsxWrUa5jDDmvPriZEwRElEPmRjDq6y0PZGXUzzlMgalDQ7Te5iNj0od5QxNITpiHS6rrGZ_o_x1k15z7q6jrJ0qLgnOQhvYj3g_wLz94urFbKgmEGER5f1GY3h5jhuo1wOzFyPV1v6m70Wp_UuGhpU16Z2Wej5MoPnicCAxa_2JI8rqZdDqJmt-aM2LgSCIoI6IPrHYBI0WfX-8lyvFjBA2HUIpu3y-eoLJOGIbuZ53t5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=SbbNXMNWuF9tDolshpEqJ-cmbYYoDhAqOeV5h2wkBUhMFecTf4tYJ77Mziyk6MhDx4vPNP5BpZbWAbDTqvDKjk6gElYH622XhxUWRB6mGzSeAbzSkP82d2p5Njg3MtA81774ZD13XDzX1s2hPdeVwVK7xS1XrWFDBOyUTWS_8kuF_oXaDyve4_iynzf1wwJ2bHVvYqx30sE7mkwLh7d4qj6LfvJxJZWjIr-NJE0JTALIvD5gwBYp9RP6-9ZUkEqpWPqhOpGSkpIS5zW6Sw0Kw7UX2KOXqkR4PAP8hGGP6y3Y3KnO4jFEXFy9AZLxFVjc_GW7D3MYkI_GJO55oJuVSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=SbbNXMNWuF9tDolshpEqJ-cmbYYoDhAqOeV5h2wkBUhMFecTf4tYJ77Mziyk6MhDx4vPNP5BpZbWAbDTqvDKjk6gElYH622XhxUWRB6mGzSeAbzSkP82d2p5Njg3MtA81774ZD13XDzX1s2hPdeVwVK7xS1XrWFDBOyUTWS_8kuF_oXaDyve4_iynzf1wwJ2bHVvYqx30sE7mkwLh7d4qj6LfvJxJZWjIr-NJE0JTALIvD5gwBYp9RP6-9ZUkEqpWPqhOpGSkpIS5zW6Sw0Kw7UX2KOXqkR4PAP8hGGP6y3Y3KnO4jFEXFy9AZLxFVjc_GW7D3MYkI_GJO55oJuVSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G1wWMvRSCmMQ2NQNGkc6Gn5u6nIXjIF07zQT5q0aWne-CvAMI9rRCGzpIWUa1Q_10ql9xNPwlq12IWJu2iWDS5rXleUoBhCD_Pg2ZmjcWOKv9qJWQ7j97xO31nL5-xLYq84V483bBsE7t9bIWOU53aGQRmRXF5ulhhIDzUpL2Ouh0Sme-TXSzKEeVK8Xh5aYET9B9ZSMOvDKzhXvoAxlfGgXC0qfcRI2cHmHNnME9xPqiwiAKDYB5y8WMhxRsxGTh2ZHr7ZGZO6u0uyQLXXgtfBOz2fZrKKCK6HfcrKpEm0F8m7D3MQaemv8153fnobAAxfAt8cOT6gZ6FHJ6balnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5ha_tUu_iAoEhafvuVj2726e0Ng-7pETxOwSoUxXjHXckG8Yc2wUYpcKheUeQBXgQeYuvZ8unJDUK57_lg_mE27X8aUAWgi-NV1SdJZF4-lXlLTWLrqcDYeETSk6l4Q5fHJ1RvPxopN-Ui7QMDQUpwM0lbFbBp2nc-P3eBSPa1rgZDKQg2ZpMhJ31n6uhkdCumVbGXkhXKCp3GQmaOwr_7OGl3ClqRK55dD_T_iMn6bf5zaSkpFHmLdDJNkPZxifj-sBrJwLjE7NClPBoMQE4bbJ596p4aPZpzUWN3Yfloo0UxK76HxwM0-DK4bSMVdnkCQbVTD856oCZ55mRc7mQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h24uH02oiPI7h6vL41BlIzxVlRs1g04lONPOh7IQqD6jbedy7zG7IJLWQTmJ7o0MhMXORg0WMDa38La8owRv1CqeNrZ3CMK4P8CMr5EEpcFBmRAb2QBjZfYMap518u74BDtWgBde6scQyCMBSO12m4N0Vzg7sJUlk-zv7luqH24ld0-bIHzp6tIv5QbcrIlenczUzCG9-aL_b386Hkhid6LdW81RmCHd-B93k20j9d3ciWQWBdSdItrQUGEmgjhzrhFsuk3tCRelbIylZMVXKX_9Ll3GrsvdDaTydH5vjyK6Jrd3nLZ_6Xw7IS63sSI8q41UsI8ZeuyXMaq6vfHQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=rl9OjmfiyobCkA6GhXquag2lhUhWEOoEm8V_KO78cHWqu-1LBuimxC-TVmbmhr7aLB0JfeB2KMGx29kPDmgJJ0tNFQK7BZxgPlrkVSN1mVYPVljClgTcBQtN_L1uZSAQ-6zhHMXJYrtYS0-7A4QS9rmPNItY5YnnCAw-A2B95pfkCTw4-TFoYhxtzdjYYSdPjVgLezBFPxMccDAay6DD9axc_CF7eWl9kBmrCQJ40UFKu5oXAtDU4vybwnx7jjH59lbvVYpckIAcAlXWU4ZPMFYkd4fvLzpNNgFVOdkBi2_19ekWdVkiAfNR8kRUOEvv7jMMjlg_FMBLRw4bwKNuLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=rl9OjmfiyobCkA6GhXquag2lhUhWEOoEm8V_KO78cHWqu-1LBuimxC-TVmbmhr7aLB0JfeB2KMGx29kPDmgJJ0tNFQK7BZxgPlrkVSN1mVYPVljClgTcBQtN_L1uZSAQ-6zhHMXJYrtYS0-7A4QS9rmPNItY5YnnCAw-A2B95pfkCTw4-TFoYhxtzdjYYSdPjVgLezBFPxMccDAay6DD9axc_CF7eWl9kBmrCQJ40UFKu5oXAtDU4vybwnx7jjH59lbvVYpckIAcAlXWU4ZPMFYkd4fvLzpNNgFVOdkBi2_19ekWdVkiAfNR8kRUOEvv7jMMjlg_FMBLRw4bwKNuLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=CWWJrCgjfXI-wZBmrp3xRBr6wj55dZ8PbiP3FMU8psl7QKuDbEcIeK1Of-b8EwWEPtefY3hQGwQuE6mBnY3TatIeYtQTrRKn62ckO56ORrr0AoenAI_fdODQohxeQPDAmzZQZNiQg8kungpz8-EBPYbOl3LwZE-99nsai6OK_vcnZDzSvoeRgx6xkzzLqpnTcAVequpqVIK8gUHFx66qKyQFJ1dCuB48p90ryNyF6h1cmMov3Z4XJ02iZwRPvLTLGopWoVsBwZ4z_ZToQTj7la2cMJiEZQB4p-AHpagIGJvYhdDQIHAqjR1svxIEKoBmOBemOBtnATXrwkOmu-osLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=CWWJrCgjfXI-wZBmrp3xRBr6wj55dZ8PbiP3FMU8psl7QKuDbEcIeK1Of-b8EwWEPtefY3hQGwQuE6mBnY3TatIeYtQTrRKn62ckO56ORrr0AoenAI_fdODQohxeQPDAmzZQZNiQg8kungpz8-EBPYbOl3LwZE-99nsai6OK_vcnZDzSvoeRgx6xkzzLqpnTcAVequpqVIK8gUHFx66qKyQFJ1dCuB48p90ryNyF6h1cmMov3Z4XJ02iZwRPvLTLGopWoVsBwZ4z_ZToQTj7la2cMJiEZQB4p-AHpagIGJvYhdDQIHAqjR1svxIEKoBmOBemOBtnATXrwkOmu-osLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-8E5pqF-kWVL3hqvkmczndY1GIbStTl4n7HiszcBRnvbBJIH6vSW3MRhoxFzM4ZfbhR_RC29U10uG1e6UGt83gEMaVUw6bXsZ22qUMQMqw51mZnJhiVpC_PxWzPMSjYQt-NP98pP9KZb6qFx1CW-nsNJ2iBs1w_E7sOXD76uXEjgBpF2-weMQQ20xE_HzebaoqSPsYoO8c4BjwhdB-oGmZLkAi5XmApv6hEJ7i1b715Au5b1LKJ-XwWQxGUm2LEJ8Nx2Awl8M80Um33UGVdggsdKXhyLS3VmttVO0xidzBxOlH15WV7CnJdqbU3eZ1gBh5_ouaYSGeAi0hI5f8zKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEzIcHdQQwNW9a4APBfDA7xTzMyz4yvCkyi0fmoX1aKJtPpn-HC8T7H2mPgtI6ynHwLa6piiPAuA74uALBm9Kg1RNyVY0IfprSccCCeMQUDrIEjZpY4u4uVjotWSbCFfgygq5SBambKq6rOZwunKnU0M5SafFsxCq8IE8g2tOl7Bwf3bamnQEq28YvovQ3-fPQR76bSx_AqG8_AQUOhq_B0n4Li_0yDj8vmyhmM-VNkQH41FKD9HPh6qpXg6ukzglX3GZkNZDb0iJtcYMB2ms7ck5F80ZLYg_puAjywUxd_nTzjC6mvCe1GoAQOpbgExUrONTGUakP8mINoJ29cNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCjpHuGWn2dRj_6QnRJs35MIS7arV-6_Z2R2Xzd0z1OQo19FGXo1Cyn67CI2LE7_FkM_sxksUJya5IEQAudYOShPwWEQkfJ8mreCtGaWVLDM4a7q_oskZtpzHU4ULt9nLuWLrbqxgdzPzMP6l8pjdb90Kkyxyy49iSVdqvq3xTQA6aB8dLBfZl343-sf6i9LD3s87qevojx32eCZs15zB8-lXvLIOTJsXOtWxYfdWzN4ja9IB9pZ3DdNDPpRfS42DRGlS_KDRUmu9r4TsxO3Lzi2-48n-eodGfMmxFj4zReU5bHHHpbt7ayOVbpzaoyVo2bqFEwFYFgvz8ejgEep-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=sjTU8RRirtJifKeqleYvSLSWlmaRZJB36BZ_PNMNWf3vayLpLG-KiiAQ7adlq8liwSOr38yXaReIcmhBLb5NvQ6KFNppdqIDsbkowyEg9SnbrZR5bMPRiCnIThLh-aqmiSjq2QqefuSznlU5DhzCxHCbKjPGlW-p1G8fnN62lDQHqRacMZ83xnneHDpevANP2WEb5-0zzvpN6SYu9IKNw0dfRAw_HNG0t3xNjtxOTyIW6zOlDW3we1l23QyV8NCoLuUKPDaPKlZNl4KZt9ZbKewV1Hwag8FERLTdta04ndHtVFLY25vssFvSCIY0vE2xrqMMdoNhnI4FgLqd8jRRZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=sjTU8RRirtJifKeqleYvSLSWlmaRZJB36BZ_PNMNWf3vayLpLG-KiiAQ7adlq8liwSOr38yXaReIcmhBLb5NvQ6KFNppdqIDsbkowyEg9SnbrZR5bMPRiCnIThLh-aqmiSjq2QqefuSznlU5DhzCxHCbKjPGlW-p1G8fnN62lDQHqRacMZ83xnneHDpevANP2WEb5-0zzvpN6SYu9IKNw0dfRAw_HNG0t3xNjtxOTyIW6zOlDW3we1l23QyV8NCoLuUKPDaPKlZNl4KZt9ZbKewV1Hwag8FERLTdta04ndHtVFLY25vssFvSCIY0vE2xrqMMdoNhnI4FgLqd8jRRZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=QLD5t5a2V7hcWGdk6xwH8pMM6xwqSBAXQWXn8uMiENHxFXjvbuYl6_F3YZphsIJoaPG7Gc0B4i3bSOIt1SKeGz_lQyrzJSdBP3OooB7ozBOb_XB2w7vxWVVBxANLV5FSUge_lmZn1HIB24xx9fghvk21pvHtIoMlkqa0JKT-Wj2JOwzObJjc8cu0FgMcPTwn4kW1uWcnSlCflcEcN0LabjjC-ZYE0aBJOInhdyWLR79bcL26un8_wiXNrW9KUiBOKwWDfkJOhMag61NULybEcHClY51nICREQB6SaAMImQTHIvwXVSZVrqRxRxesMWsgd-2nxogxYTxomt7d50F_7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=QLD5t5a2V7hcWGdk6xwH8pMM6xwqSBAXQWXn8uMiENHxFXjvbuYl6_F3YZphsIJoaPG7Gc0B4i3bSOIt1SKeGz_lQyrzJSdBP3OooB7ozBOb_XB2w7vxWVVBxANLV5FSUge_lmZn1HIB24xx9fghvk21pvHtIoMlkqa0JKT-Wj2JOwzObJjc8cu0FgMcPTwn4kW1uWcnSlCflcEcN0LabjjC-ZYE0aBJOInhdyWLR79bcL26un8_wiXNrW9KUiBOKwWDfkJOhMag61NULybEcHClY51nICREQB6SaAMImQTHIvwXVSZVrqRxRxesMWsgd-2nxogxYTxomt7d50F_7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=S8rMSy1TneWqoOXRxeIgYSPdY9KNPA9HxzQTHW45xoEJHzc_nn6wlkRN2t8zyZSzNSS31L6KDub2wZXovQsa-Trta15gfEI58dUDQcn0RkamrJMoDwOIUlmczRki4XRi2NtZsPBfsCstecCWLlavKyVRTmY2QcZxggPm4oyCs2DAK2mjlP0T_3YQE5dswQ_yebPR_4ISVUOXfOVj1nfRTG-AN7Lr8zafucr00cM_KiZa9nnYzVQrdau_bmR93mkCLyX-gOOlKsfqR3ye_cQzjKtvTtcC6sS8_ZZR0INvOZEvgfGWYdLsa-S5Qe_GOZg2uIyKVOo6xSFMz_IMRkWJFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=S8rMSy1TneWqoOXRxeIgYSPdY9KNPA9HxzQTHW45xoEJHzc_nn6wlkRN2t8zyZSzNSS31L6KDub2wZXovQsa-Trta15gfEI58dUDQcn0RkamrJMoDwOIUlmczRki4XRi2NtZsPBfsCstecCWLlavKyVRTmY2QcZxggPm4oyCs2DAK2mjlP0T_3YQE5dswQ_yebPR_4ISVUOXfOVj1nfRTG-AN7Lr8zafucr00cM_KiZa9nnYzVQrdau_bmR93mkCLyX-gOOlKsfqR3ye_cQzjKtvTtcC6sS8_ZZR0INvOZEvgfGWYdLsa-S5Qe_GOZg2uIyKVOo6xSFMz_IMRkWJFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PD7JRC66THya0Dhiji6cUcw3pZciOkRwZXw1e-667_xaaNRskvEe8jVq1CbNdnH4V0K4wZWBya9XBmvMH4rr9wnED-TDsktx51bfKkzRoUJZvFo_c8i8lKD0_jpCyk9HwZrxPOBafKKPVMkB0ar-XJ4l9wQbXVS7juC-saUAiUR0v4I8cJhbkQ-Ei-YKrhcifK0CZo2fPDxY9ZRzfxslo9yCNWDpqJKolUwhagjpXEkdtHB2XxKJPNLMYij-ipILKIYwV-_YhND8v4XPlTDEXVbk5CQTlMhgUNqFOJyxoD-mLPWmZCCXpavUfOx6hnOWh3fiRrpBtK3y2Z7EURoxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=gMHmSBPZ5IvUYuAnyJMv6WPFHlnakEx20BhvSzA2pXDNftVMsd0a_IELKkyux9swMQmefe2cI13mzd5O9-wYtGtHz2u_03GpaNDkv6IKeFAo81_WAGkalVsFbtnfmDanff-hlALELlNP1oY7o_jux0O3kAa9AXa1DBjQv8H3nWUaEh7zYh7sUp_Eprqcv-h8Hu3R_q_AKGlmYc2rIFv59A38cPS-N2Z1U9nBhLl0olXnWoHmnQf4mlMH-4peHwV3wULZcT1IoPXR7b96k4wGQEQPewlYGZ15o7wuIBdobkZ88nfZlaWfNSUWxJD_HN8zpDnfgl390kmH4CTwN7r-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=gMHmSBPZ5IvUYuAnyJMv6WPFHlnakEx20BhvSzA2pXDNftVMsd0a_IELKkyux9swMQmefe2cI13mzd5O9-wYtGtHz2u_03GpaNDkv6IKeFAo81_WAGkalVsFbtnfmDanff-hlALELlNP1oY7o_jux0O3kAa9AXa1DBjQv8H3nWUaEh7zYh7sUp_Eprqcv-h8Hu3R_q_AKGlmYc2rIFv59A38cPS-N2Z1U9nBhLl0olXnWoHmnQf4mlMH-4peHwV3wULZcT1IoPXR7b96k4wGQEQPewlYGZ15o7wuIBdobkZ88nfZlaWfNSUWxJD_HN8zpDnfgl390kmH4CTwN7r-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=B1u2JwxVhUdikvxtVTyXlDZRcyG61a2SHQblYcE-JJLNoRF5Gvle2iMZ5DCCWDDlcipS5c8u_kuzptmmjRVSan-Ml0t1DY8FR5tu_vrnFZPyKUyEPCRPqnOnb9qRqdAGLfJkq6UfoOkHn56bQQlnxCsFUYy_GRZJQ7u5JtWdZc0f_hOstZSHCVWnsCp8XoImcV2olQSPLcDl7oAdSOFFATap58Ow3aN1RevKuVsX6iLKA08gi9Koi_-TeCO0SgRuU1904xpMM_CQBb0AIuj25qegvzHo3bEKVmOsKPrsbA4S64TqlFgk1PM2RSLFic0Hkjx1pKP6YDwcpjOgew6y-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=B1u2JwxVhUdikvxtVTyXlDZRcyG61a2SHQblYcE-JJLNoRF5Gvle2iMZ5DCCWDDlcipS5c8u_kuzptmmjRVSan-Ml0t1DY8FR5tu_vrnFZPyKUyEPCRPqnOnb9qRqdAGLfJkq6UfoOkHn56bQQlnxCsFUYy_GRZJQ7u5JtWdZc0f_hOstZSHCVWnsCp8XoImcV2olQSPLcDl7oAdSOFFATap58Ow3aN1RevKuVsX6iLKA08gi9Koi_-TeCO0SgRuU1904xpMM_CQBb0AIuj25qegvzHo3bEKVmOsKPrsbA4S64TqlFgk1PM2RSLFic0Hkjx1pKP6YDwcpjOgew6y-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=BKfDmR1swtEoMAGoI5kHn_tTeInzcpBxQBSbSEEmja0QnfEVTDNJiXkbKxjm-mmoYb0kTwxdmBd6TiyUOOF65w0qu8jyI3mjEz8lk7RLnqk__WEMZIbFKoZs2g_vVVyn07AlvJKmoZ7Dz9CmdI_h53TKS5woL1OK3VOs3noxScYIdTq28l527FcQQEDnhhMEMClhd_GlufOX_VfwnF8i6ZcqkTWD-XoFqZfgHfC54jRodZWnU4qWyumsUFaegAQ0dyVf-om40It-S0aBx_PuAuKSVirG69JH6Z2d-KPc1VTfqEgNFZxdJDuQLwe7Qw8CGDCS4IEfDWj1A_EIH6ZrRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=BKfDmR1swtEoMAGoI5kHn_tTeInzcpBxQBSbSEEmja0QnfEVTDNJiXkbKxjm-mmoYb0kTwxdmBd6TiyUOOF65w0qu8jyI3mjEz8lk7RLnqk__WEMZIbFKoZs2g_vVVyn07AlvJKmoZ7Dz9CmdI_h53TKS5woL1OK3VOs3noxScYIdTq28l527FcQQEDnhhMEMClhd_GlufOX_VfwnF8i6ZcqkTWD-XoFqZfgHfC54jRodZWnU4qWyumsUFaegAQ0dyVf-om40It-S0aBx_PuAuKSVirG69JH6Z2d-KPc1VTfqEgNFZxdJDuQLwe7Qw8CGDCS4IEfDWj1A_EIH6ZrRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
