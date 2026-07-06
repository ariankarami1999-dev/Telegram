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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 23:49:58</div>
<hr>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=crH_ZBmmMjbHk6ZeCPhCAVAj0P3giHM01Y2jQnF6xWYi8CDvBhFBYBDgR-bOuEUTsg0u2Al9JEkweu58QD-mUsN2xjOB6gHoneZfrMzySJcUYgT-UWWx8YWNsceNBdk-MfHpMum003qDqaxhso9vahPkISSmdEzz99bk736ect0cCpPsSW-uCZjLNlrfOESbkbrVL7KHhz9eG-NJGOup7my2J0ppm9SMI94ry2oe8pYZaUqAkmF1VWvJbUbJXNJPq1EpZ7adXY17ID4mdNneA68JdFGnep0IM_GVJTF9P2JGbAS2mv2cY_FhSK-IR6-elSmy7zHKF4eqbCUi_EvXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=crH_ZBmmMjbHk6ZeCPhCAVAj0P3giHM01Y2jQnF6xWYi8CDvBhFBYBDgR-bOuEUTsg0u2Al9JEkweu58QD-mUsN2xjOB6gHoneZfrMzySJcUYgT-UWWx8YWNsceNBdk-MfHpMum003qDqaxhso9vahPkISSmdEzz99bk736ect0cCpPsSW-uCZjLNlrfOESbkbrVL7KHhz9eG-NJGOup7my2J0ppm9SMI94ry2oe8pYZaUqAkmF1VWvJbUbJXNJPq1EpZ7adXY17ID4mdNneA68JdFGnep0IM_GVJTF9P2JGbAS2mv2cY_FhSK-IR6-elSmy7zHKF4eqbCUi_EvXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=Jdgotm308lj4ID9_cegzyhOhu0DVrefvROUXOI9edm2mZeN4QRcsTp6CiZKoM5Nt6uVL-hRw6Eu55yfXYgCziBQMWhhcTq8oDHkD30ELYEhpb2UEW5NdfiJqviZq921Hx6zGsfrdbF-4j4wtSzZDLw5wv-staOz3tNR5hKhfDQTsP67Euq-u2Xh94GFp7DbzSBs-vhIRPksAecCzscq8qk_jYyL1X2WXwKw-XsrRnJmmoElYgidR2bClIllCI5uAjAdfphmI7p3DqZX1iVK2m2DuVKNeGhEGh5zjRlTxhStwrKO_0UH5bZgrjUV7q9AXtro0X_RS8_xk2qdcpKIGJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=Jdgotm308lj4ID9_cegzyhOhu0DVrefvROUXOI9edm2mZeN4QRcsTp6CiZKoM5Nt6uVL-hRw6Eu55yfXYgCziBQMWhhcTq8oDHkD30ELYEhpb2UEW5NdfiJqviZq921Hx6zGsfrdbF-4j4wtSzZDLw5wv-staOz3tNR5hKhfDQTsP67Euq-u2Xh94GFp7DbzSBs-vhIRPksAecCzscq8qk_jYyL1X2WXwKw-XsrRnJmmoElYgidR2bClIllCI5uAjAdfphmI7p3DqZX1iVK2m2DuVKNeGhEGh5zjRlTxhStwrKO_0UH5bZgrjUV7q9AXtro0X_RS8_xk2qdcpKIGJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOr1MOaFc98ndHzbgebbH9dHc8bl97GDWmB6BDqnNKZGRPWAxJQvZpT1gtjgGF5J_B1QpMrQMqvc3EkUi9U6VxfK4ekCCG8tAluQEwMOhL8vxqxas4lnqQlMncI-O_ZQSWVzgDLay4elg0u0EOvnKjNRs1aQqVZ8nfwbWKgBKSkMz4Zgqwy836DOZ0Xp82YDyP7LFLQSX8b63F6yG1gWUODCJhvsKGUUs-CC3DCsjYlfx6FBrYVduCpS9ikgTZcRQ9lWFSPlttODFO98KhCF8qK_CZtr3yxWx3LACwQApCyaT-5c4LBbN9lPVo5o4S0LFiqzdVyoXc52Kd4_atbUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcC5f6xgDB_KStPgsFj4cWmxYsQMXqER_Y9urn5vUcZx56gIsdNxbfQImYwIhnEXiEqsHflxWznALrWWbLbx9PtMjhySDcw0kwT1Hey41frIL-kmeQ2WYh6FPpgDThk_iap81Rk-2b51nnT4pDQk3kSMp2CsQy-gQfE3NjoHZSNLTYxLyC9-yaecdVRzGD4yS8FACSQrqjfUQe8skcT8U2bp9X_DqXiQyJTEFDsP77P_5O6RhROBSnyNTt4d1oiXUdTk1X-LmYfmIQukNBwN-YA4NvXWo2WD1S1Zg2EfDgFF7B6Vve2bCAY_8peT27gRUJQ96rtoJ_QXxlwrmY050A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SC5bYfC72_8du0GMyw9JHDLnzdmxiK4rI4spNj0fVO8IT3qhxB74gwGVclyUaVnLCYoyflAa4D1V6a4K-ndLSnrNB2lCGjL2YwfxdA5xtXz_KidjCdYcPaUfetXmF4lHmWXyngp5_wpPPDCYLBBj3YW4e3MY3bT34e5pfLctoOdAjE_Ny2tDEcU9IkYB2UrVb5kjGEfB2vl3omD0YR4hd0PXCmPEitRbrxHIZ3IB4PPQoe-jsMkEnEBYX0wZsyZSXy4__2-PT1y1vZEGIz-cz5Qk4FYsrEgtgqoOnzV9MR8nAr2StguF5_3T3WYqNlnyoUCyOQBoDsvIRE_-XsPncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhFBFAN9Mmd5DRKlXqrnouQrzq1hhYO6OPsZQ6_ESz-tu4b6pA3Jx7tDkD9B5JbuSDX370zuLhtmMLWU_REYg0QiuembbG7gZjT-lnr9c1JT682dx910dXmbuhH9RJpwclCWa-NtqqTFdpSL6NyejsbauGKbacTvW-gDs2Z38VHLgna2KOAfxzIalzHOC0eZwyCkW2CwG3Si6sb4pWIANTWlhFb6RFy9BosdflWmGPmpVU-degU1MPjlL-uXpnyTyDP8ktRtC6BQv1XPEoaV0ifckDcyGKg9wGh4OnFP6ketWA131MNCMt0xTElGidjyFmJupx_eQhP45ae-gG7WOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvCkDSZ8O863B7T78ELG3EhQzhDfvnNJQSnpR4h0jE4soCC8mrfgK0yjBGzrr2BBTMx5ssu5gdazMGqRyL8jCwQOvGwURNXnNQc1inVeht6fzr3tOLfBMX1HFuFu5LK56h46HHT5iY_3EbfSosbttSEHhHRNvH_Er04azq-hTL43VfctQu5o07mpXVW_35lwzR3cY0KdwXCPMvR4eaRdSmRqaQ-mh2xyxc_GOU_hh_nwL9Lwh1Hp1aAHfoFkxfUS05ulbDEKLr8a3VvE41hiI8f7vieMIoBzKOfWcRXFYNHPNgzfLfqH-tS3RkfJda_aqgS3A-OB4JLAWII0FRn8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fssQ0jhqkUsS6dfJyUxUUlXdDK6hYuhPFnmDF9V0mRTIY4F8cH4KoeyR0LapBV_yHBg2t5AgfsuRxSG1odzogHO09x9fLrVZ_GNaNKMPhQlOybzYVneZagPykJ1dFRHuO495tPqupZgwqIhxFTkPpMcrqUVVMlISJyOTc_yFTYtO4vmUjqJIIeaFo2k5pBRAqo_9xtqQzYZlQtJ5NSLIv_owdN5e76fYo-0A4OqQYnHQNx2KMPYOnXwmd7NO7dsBszJNwdFq3twDz3AzTHAymX2DmpwoUdZlA36NOqJQSer-ctKf_1Elo8EIxdErY-7cCC26iavtENrB5Dtb4XaavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=CW2mYnE7kDvYhbvYpzjjSe0dGUrcyryhJ1K_BqcN58pfrDtkbqrTBhNqw-DGwJY1Y6oDgn0Tu0rUakaOnjtKH7dxgwSHj7HKL5Nib7RBtMZnJy_SMZcW0ng_ps7Gk2U3NrGTiBOGaaWmZs7ByiD5czcjLxuBvfKCRL_p2n0GIk5nLb1ry44vcwE4F9XneNpo0paiezorzXKkZS6URF4-mrL7hRdiI-lrVXoBt6Vlxgj-GynB3JCf1yJMA_uPLQFjMrPZFnGneIoQBRzoeW-H3eX77mXokeDqNoc09uKyRAXOedXa851SMhDGM67SPz0Cm2_w_dKm_FPPfdAUovW_0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=CW2mYnE7kDvYhbvYpzjjSe0dGUrcyryhJ1K_BqcN58pfrDtkbqrTBhNqw-DGwJY1Y6oDgn0Tu0rUakaOnjtKH7dxgwSHj7HKL5Nib7RBtMZnJy_SMZcW0ng_ps7Gk2U3NrGTiBOGaaWmZs7ByiD5czcjLxuBvfKCRL_p2n0GIk5nLb1ry44vcwE4F9XneNpo0paiezorzXKkZS6URF4-mrL7hRdiI-lrVXoBt6Vlxgj-GynB3JCf1yJMA_uPLQFjMrPZFnGneIoQBRzoeW-H3eX77mXokeDqNoc09uKyRAXOedXa851SMhDGM67SPz0Cm2_w_dKm_FPPfdAUovW_0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=K1hJ4lshMMFP2J8bmPVxdg7hTa8Th-dT1gdEppxdAeCG9GBOnu3-vFkYrKGulaqt1Hl1Sm9bfdDnP3zojBZRPdAvmzMF06Ypj8iSEddiW2oR3qtf3IOzEdVc_wcDey-2VnsABFDdwVffSCTbSENg901mGt81cZrtsfJjG-WFj8o3OgjKVqtm5GY70y8SaFw_c7kTdU-Zyireg4G6uO0WeD7GucPBar7_iXGzwx0ePca53EVTyowZHt5ItYPN0GhDik_vcUamV-afIHdOcskHvbu42yCniD2xwAP8_Xai1cZPLoAF3ZF_BqmOP09xu2F6ew6h-2RIB8RCjLmbl9issQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=K1hJ4lshMMFP2J8bmPVxdg7hTa8Th-dT1gdEppxdAeCG9GBOnu3-vFkYrKGulaqt1Hl1Sm9bfdDnP3zojBZRPdAvmzMF06Ypj8iSEddiW2oR3qtf3IOzEdVc_wcDey-2VnsABFDdwVffSCTbSENg901mGt81cZrtsfJjG-WFj8o3OgjKVqtm5GY70y8SaFw_c7kTdU-Zyireg4G6uO0WeD7GucPBar7_iXGzwx0ePca53EVTyowZHt5ItYPN0GhDik_vcUamV-afIHdOcskHvbu42yCniD2xwAP8_Xai1cZPLoAF3ZF_BqmOP09xu2F6ew6h-2RIB8RCjLmbl9issQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/om22OVgCFGjKzvAGemG4a_TA__sydmUAQ23d7JVb68VdRiroHxOahRrI8gYLc89K8LNl21Vt_9C-3R1LKDXJzric1EnfrfD1Z3eseVRREaBz9JgjI4eG71Hx8TrJfjGlnYPCFC3fKnABt9nSRRswFcu92tgXDYO2eFisbYjSDkpKORZOr4LcSOjJcgGH2_yghnDA5Jv9RkeMk5NIwxqvzixg9-X-ph8Bk4Kcqyt3qQ-HIi_zO5_DOiOoVc29fy3TcYFtMt3I4REJSEuuIGqNLTA-z5aLPd62IiNAESJ9CNlwVjwenHMgX784q7N7SAEE6kBIi2XtIOlIOC2OlXMxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=AveoCijfNwJrppOxypXpimjqb2T-qkc_0HK6jhdHTLObVAnWdth07igWEtYLSlG-GbYqneB4VuJqbJACdRZjlGx-idSkRgfnXcgkQM0TmHWyZR7zWrHZb2c_jlTSpb7kQ7_cYfpT99aAxZn16UEex0-ho6XIlv_vcSe3BQMK3A4UfQpZVzHJzFKuFvO1fA7IWT-K9roTNKjEjr8XPEo56aErTGGPXp8atjbFojsXxP1FBTaI5BfBXk-FxtbvgwkpnKSvDVg4UXOQO6bC8y6fkbVL513Ck6kI4kwpna1qHHCILXpYuOGzousk6nXqZoVUnkQgZQAg1Y1FORninMnc7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=AveoCijfNwJrppOxypXpimjqb2T-qkc_0HK6jhdHTLObVAnWdth07igWEtYLSlG-GbYqneB4VuJqbJACdRZjlGx-idSkRgfnXcgkQM0TmHWyZR7zWrHZb2c_jlTSpb7kQ7_cYfpT99aAxZn16UEex0-ho6XIlv_vcSe3BQMK3A4UfQpZVzHJzFKuFvO1fA7IWT-K9roTNKjEjr8XPEo56aErTGGPXp8atjbFojsXxP1FBTaI5BfBXk-FxtbvgwkpnKSvDVg4UXOQO6bC8y6fkbVL513Ck6kI4kwpna1qHHCILXpYuOGzousk6nXqZoVUnkQgZQAg1Y1FORninMnc7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQgoXBTBrt8f1XynZmfk-Q_OzdTGToUPBkBbqcXsbBevkzFFgxZxkEvgChK_tlMxH1XqwDeyWt7RqgnEzH5nogHCKTYUSxrlye0icxz-zOPNpd5voq1A-eIVg0ZYl6pF5lehyJ9LpL_Y1ZgWxGiITHBd2cquPRxkEUDJQFMg8O3TqHqCDwXN2SaBHhOb3XO_qE-TWQedZmlMKw5DTviNQdvULETAh62mw8bwn2tv2g66nCPu77rB1k8YlKx5d0IFF3W2RSliw1ZBqH7MvKqPCzBv55qUx9NBDcGyWScvj3kDgw6IKH8JvDTP6Bn12VmJWWBfGCdJKU1b2KPcxLD4Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uwSg055MbxA0hL9SrvTj8vFuIerDdrt12z5NgxRQ3AbTcuDLSyo-lO-ipyc9rFxjm9eOVdaWnx0QoKqfilbz2wMJiiJix5mCektDTLGaCeWf5ZEXPCuugSqbz7A3MMfhSXjEi8DbwsiQpNlvV3bDSYqUxd5JPq1IjMe_DNfSN7ddtvwUMDeyl6553NLCCiZecn5AcT1z_tS49B69LB3SG-EmAIu-q4wCljGkVzDXklcD2ybT3nQVgE20svNDZpi0wEy5kpiaMI_s-d9dHq7QKe1kHYcXrcly8CmUso3v9_dScHDhDco-ka3LjPRFLr8rbybJtvnWDGwqxRA-iMeUVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKVk8XuiK9DnRsKYFmw32sXwdamsOY8845TfAmwjMTjbl7iTVBrjCaMRMoC6jqUGUkxR-NPvw3-o-r75Ro3zfz_fKMnRdWTYPKq8POUKthk23L3BIWMbouQOTibRe1AwaBYJ4XcMOtqE5wP_cxy8mfK7O8xKIIpEg6_Sq4ND8kpz9ZGGrQwWvM9bN8bq68YeWG2CAQTR0O3gFQoQiqE3_3khCpDhYk92FT9tK_aEXWJCxFZ-fJqilaHHho9ON3mzPX-vlcl7KaGN3_Vq_xHTIRLovBQqltef9q2yzi-staJVOceI06pFJamYMA0G_zqZe3tQvJUdaUbWrhpzIFWdFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=sxtnyaDgkQGHo68be25DYazm0xIQjWLrjEPgbK8kgeHnM4iMz3FNxstK2YUzOBeca5DsNXQZvBbVZeWTAZoRfSpQSFTDMJpq3pDSdg3TJ7Bau7z0nuWBvGORH9MS8AgdBcbgI-3gWf6NU5L9PjYHcfe8pTFs3KRFdR5nR1IiBtn_Ojh_a0EElsJNpPKIdPMdq2BAgOpXD1FNM0bRzXNMlhdYrE1p_XDCvUMAR5zrub5cN5DgH7PFOS_5Xl8U-9C9EQRAP_aYCKfRzD62i10iPDaOWeDfVdMa-chfkyblcs4SEsXmvNNt5AzXuR4xugpdw0bXkTUgh-fjzcV4KKphYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=sxtnyaDgkQGHo68be25DYazm0xIQjWLrjEPgbK8kgeHnM4iMz3FNxstK2YUzOBeca5DsNXQZvBbVZeWTAZoRfSpQSFTDMJpq3pDSdg3TJ7Bau7z0nuWBvGORH9MS8AgdBcbgI-3gWf6NU5L9PjYHcfe8pTFs3KRFdR5nR1IiBtn_Ojh_a0EElsJNpPKIdPMdq2BAgOpXD1FNM0bRzXNMlhdYrE1p_XDCvUMAR5zrub5cN5DgH7PFOS_5Xl8U-9C9EQRAP_aYCKfRzD62i10iPDaOWeDfVdMa-chfkyblcs4SEsXmvNNt5AzXuR4xugpdw0bXkTUgh-fjzcV4KKphYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=Xi9VO_3b--09fuUHfUbg-Jn58WFDBp9wftiLte_JFx3h2rvqPmwFvGgH90vV4v-TdOnWF8zPao4LLhDdDMMsGii7fHdU7cAeay3MVqF3bHdhjKKheR5lO0SVPFVcUjFyzZH6r0CXXzpax0qI9roM0H6IVsCDZXGDKWEhL394QEJqXyWxPowWB_kKV1BBFnEyBZrBWrMyveDzY2TUbi2-qWri5_thzHBcHPO8G3uv02v4Kg_2JnyiAuBcw3qM_ph1GcvyJDdfR715R6NgptB5_ULnSbYVMG5Gp4_H0PrRjVf_skyN2z0gypnG375GDte9vDkQtVL7ZcZ1nf2d0qtqJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=Xi9VO_3b--09fuUHfUbg-Jn58WFDBp9wftiLte_JFx3h2rvqPmwFvGgH90vV4v-TdOnWF8zPao4LLhDdDMMsGii7fHdU7cAeay3MVqF3bHdhjKKheR5lO0SVPFVcUjFyzZH6r0CXXzpax0qI9roM0H6IVsCDZXGDKWEhL394QEJqXyWxPowWB_kKV1BBFnEyBZrBWrMyveDzY2TUbi2-qWri5_thzHBcHPO8G3uv02v4Kg_2JnyiAuBcw3qM_ph1GcvyJDdfR715R6NgptB5_ULnSbYVMG5Gp4_H0PrRjVf_skyN2z0gypnG375GDte9vDkQtVL7ZcZ1nf2d0qtqJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWtpt0SJGyLkhU65TWuD8WdhZRyi1npN7fHADfAivfBloDwD93JRf-oG0Nd84G_czEZsYHe6PfL4Q-WoP_VazvOu1ARYO8VNCyxiK22Opp0ekeHcepqQt5UVsKIealNEpQxrsfWEgQCb3DxyFejx40AIHURqqQPHVVJeNfxyLa4PEwKgVUK5IvTxDGwDHZG-nvWyaXzcraaFi4I33OJ6agGQzqQhp82rjgm_ZKQjahf7FK_xfxaM9bL879Ehg1MuR2ncEC5VSraXjSrzqlt8JEj1dj09KHVljCbPNeYdeGno481vCzgnCj7mQi0w1Qd_ZArJj9x99A2CNvJsqydiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=vZiWYCuclqINZircCjekzuWAvSgRrpUjYUJIk0-184jqZqgdxDox5fIjVuumwmkw2VTehvkjuG0kY8VIg3wDkHXwIvJQb16PSGXMAPiWXr5UACRIuEN2zWGK7CD7nhMsQIEGMQJEtzvs1Nqfns6VCjVDBg8fqEH3faC4BO_D5yl7efmGi1lmkfwpmY9MEMzA3PdL0glvFAFCej9H0l-OOlCZjX-XeeBlAuCa9YHYwI2iFKQ9q1vw0dsTFoSJZCem7MuQMpo9YpHwbxwvNxtch3J5qAQ5Ny1zBjE1M0w9RXiAEcZCONEV4Q4odRnvX8ytPOVGHCzPCxHHqUHhxTLGLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=vZiWYCuclqINZircCjekzuWAvSgRrpUjYUJIk0-184jqZqgdxDox5fIjVuumwmkw2VTehvkjuG0kY8VIg3wDkHXwIvJQb16PSGXMAPiWXr5UACRIuEN2zWGK7CD7nhMsQIEGMQJEtzvs1Nqfns6VCjVDBg8fqEH3faC4BO_D5yl7efmGi1lmkfwpmY9MEMzA3PdL0glvFAFCej9H0l-OOlCZjX-XeeBlAuCa9YHYwI2iFKQ9q1vw0dsTFoSJZCem7MuQMpo9YpHwbxwvNxtch3J5qAQ5Ny1zBjE1M0w9RXiAEcZCONEV4Q4odRnvX8ytPOVGHCzPCxHHqUHhxTLGLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnW3iV3giRE69BC6fp3Owmtp7kc0wh0udSXA3v6viXBYTQKoZq83yGb84vKQRQWV2gbZNrVt99D5hjqbYZK_MdStkRNWDAfiMsLA8OX_YAoQaZunXpzfgOSqUZ5UVItefX142ik_9pM5DLKfnJ_aIIsg0ot0FhT2H-aWLhTHhqOvmCSmVDPicBAuXLk_uGSPYJgobdCby88PSzfZVM2iCZUOQt-v-OAQIFBJipcwm8tZkkQZwhMt7qNF_4JtEzSL_V1_9LDmWL_JORuqatbzBrpWGospRfjAOiDAp2AaoG19mEf82vZo6Z_tMgeoHqokBhzWxFD835eXwT2BF-rAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=Lp5LErW39ApfnyL3ZyiXHf3ymvXQmVanCo4YFs7qCepLL9XZhaRF1EOraarkmSMN7XS5-XspC2qgL39TL6v97plBmjJF6OcSIRsnnL7flnwcdnQ_qfYcd6aEL8w_YEbtGqvRdcniCmM2Qnzuz5lsNuppCe14JqU6TIlYcdPB5sNwhUFKnwZyTR07kbuKmKtRWE949-W11mSVDZ9DD_u1AS0IiDQGxqw7nET4DySSkvnujyjCQztqV_I8K2XVGso6BVH9udFl7ggILhqA1wshSvmlsW-JOfCGHgb2cHdxooD5hS3a-SdFdkbdKCN1HCaGG2rbYWQPnBZgcFDSRvvEwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=Lp5LErW39ApfnyL3ZyiXHf3ymvXQmVanCo4YFs7qCepLL9XZhaRF1EOraarkmSMN7XS5-XspC2qgL39TL6v97plBmjJF6OcSIRsnnL7flnwcdnQ_qfYcd6aEL8w_YEbtGqvRdcniCmM2Qnzuz5lsNuppCe14JqU6TIlYcdPB5sNwhUFKnwZyTR07kbuKmKtRWE949-W11mSVDZ9DD_u1AS0IiDQGxqw7nET4DySSkvnujyjCQztqV_I8K2XVGso6BVH9udFl7ggILhqA1wshSvmlsW-JOfCGHgb2cHdxooD5hS3a-SdFdkbdKCN1HCaGG2rbYWQPnBZgcFDSRvvEwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN7zsjal9pDQrUVYjk2KUGAlgiBV-XxHhuj85-HSwEvvX7bh7kU7dvrDfAqjRq7pk8qCJ-yIKDK3K0mTyqx7UlCmqozGje0z0bjxURzWT2xHEjzqQQ5M793B9baUEQTglrU83Aqf8F6QYvYOr9SDfjV0O_jU7kEuu48REkpygUhhIc8ALTAZM964p05e4sFzirn8YzS_ymd7aWjwj7XLQN-HnaDV9pam7z7KgVaLn4bHJjXKvGLmgOMCCwJk_B6m_4dn-1Gu39_T855OuEf0sBMmjUjfCT9ob0yNgxgNt2PnWU5k-eyTO7JkCS1GlsJLgrLM3A56FjNQf4r6tQL-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=fJViNKjvWJiMat8Omf6hLupQt9AVSBUYFJWRZ5cmIlQ5f5OkX3Aobo_2dGALTGNEKCa5j0-PDtU-Njruti5GyUEtA785kdZRNRhmu9TZlaUSoZfStJZU5Y51LZmygKuMs9gYv2A_Whp2guDwUzvWKxvJN8Z1exPjpBHiw0ZHZFp7KsEU87sLgjPGMhAM4DY2ds_4qZxgfxSKDWIwUiBcsLsk8g5csa9ru37_0WSJk7vq8sWMDZVlzXtbegCreAP1tKhf1AdtPiyNPjyh0timbvR8JyK73lp4ZcOU2gOYa5quVSIA3ujkybq2nCqPkP2WSGmUczoDRrcy153AcnN71A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=fJViNKjvWJiMat8Omf6hLupQt9AVSBUYFJWRZ5cmIlQ5f5OkX3Aobo_2dGALTGNEKCa5j0-PDtU-Njruti5GyUEtA785kdZRNRhmu9TZlaUSoZfStJZU5Y51LZmygKuMs9gYv2A_Whp2guDwUzvWKxvJN8Z1exPjpBHiw0ZHZFp7KsEU87sLgjPGMhAM4DY2ds_4qZxgfxSKDWIwUiBcsLsk8g5csa9ru37_0WSJk7vq8sWMDZVlzXtbegCreAP1tKhf1AdtPiyNPjyh0timbvR8JyK73lp4ZcOU2gOYa5quVSIA3ujkybq2nCqPkP2WSGmUczoDRrcy153AcnN71A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=nifYgup53mA4L2LT9NIG0Fi7PiDF_I27DfYYsg8jd4KVQVOnsrc92WkNtJtF-LzWbLoI-n1PWo2KArTSc640geeQWV5kQTFFmiKtSBJY1tvqN7kRSlfe4AdKFVJ4IzEJ54mdmKkLxsaJYVbrEj2FjWIVBQK6TeMw-HQ8ZNQj_2l1DmR0FxlXgNTX1j6bIKlAJouDgxqTLV7izfAN2ekDOcsCh-L9m_C_JpsU415yeuwjwXiVsz2lcCnlfTRDh7BjJh13Wl5gE_rH0TMYpod06B_hIq75VIME-AkRjtcj6WjhxgQ42ck4S9TgXPlXLDS_nmt0S7DN4qeWBfR3ZOZV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=nifYgup53mA4L2LT9NIG0Fi7PiDF_I27DfYYsg8jd4KVQVOnsrc92WkNtJtF-LzWbLoI-n1PWo2KArTSc640geeQWV5kQTFFmiKtSBJY1tvqN7kRSlfe4AdKFVJ4IzEJ54mdmKkLxsaJYVbrEj2FjWIVBQK6TeMw-HQ8ZNQj_2l1DmR0FxlXgNTX1j6bIKlAJouDgxqTLV7izfAN2ekDOcsCh-L9m_C_JpsU415yeuwjwXiVsz2lcCnlfTRDh7BjJh13Wl5gE_rH0TMYpod06B_hIq75VIME-AkRjtcj6WjhxgQ42ck4S9TgXPlXLDS_nmt0S7DN4qeWBfR3ZOZV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NxhdILrplLMdWL8M9j7lnAvXWEIeaLbwHuP5cFpuOH5ozDTGvrQryVuWf0aj33U9ysGTnhi_lEz_jDeRymHfOahDyw6jMiBKagUtLImEoA1_I5yEN0b_hTDovJCtu9iwSywf7u0xNFOoq_jCLfR90jXeJa8-LbsckafQ2DSsLf45wbM0RymK7Mex_Ut0SHbWPE5HzZXc521j8AoDluD_Yc7L7Bg4k7LCUQUztvV6HoaDLjIF6iH4O6s5O7O6LfmWXx7bwFBN7WBehsl8F-uBgRhQGGNzPFcEnHjYuSu-8P2eRjoiqexgaZDNz09NAXefK3NKSx9Ac8eT9F1xGwXx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdeNw9wtbFBUeUL1GBDRNSYD6Bu9P3388tp8D4LpAIjvsrOGiEg6r1sdpZ7NcvWswA0dXcGEsYV_5fjVVgqFxG2pl_qKmtsquDdqxsEDZILLuD0STtR1UD-QZ75B7gLKPffsaMPGeZDXF0hCdVureYmOKqEGMeCM46I-tGGnvo5qlXM66_HeiZgeuoR_b8c5rksE67pApztfqD-CKqQfLwNzDZPIhTFHWf9b6oQ9Nl0P90PJ4uWBQnCPr2KoB1K0OQchlGHUk0i4Ml0BT2EMLkWz8WdIjkuhZaRIvnQJQqk_z9SgdCgSRPXE07iTYMknxwtptTI6M9FhWChfCubNKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=g5YmnVIz0rL3x6iTdyEU5gVbofW5I3ROu4d1igNTIfQff-lyNLGK10EOZT2r7L__cyA3JsFGiyd844wvoqjUHym1cOrQ7sNkiaU2md2gwE2dsLbg5s4MCyVoDdEadWHd3CHzakHed1VoL0R8xTMHlrP7UNBb7c28MpCY6_PNn62hMR8I-zomot49jBjYCvU6ibSofi0cZWbZf9StZ1_1lsjQ_V_O4-l5DU-m_tjKTwhTlP_Hergwdc1GdIAMWxCrK5cYeUn-2xaBBnFAU0fwG_sbUvQbSy95CgGPlmvDNpDxqc5aAXrKA_VhThfotTpeHWMjVTK9sbkklNwzr_yv5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=g5YmnVIz0rL3x6iTdyEU5gVbofW5I3ROu4d1igNTIfQff-lyNLGK10EOZT2r7L__cyA3JsFGiyd844wvoqjUHym1cOrQ7sNkiaU2md2gwE2dsLbg5s4MCyVoDdEadWHd3CHzakHed1VoL0R8xTMHlrP7UNBb7c28MpCY6_PNn62hMR8I-zomot49jBjYCvU6ibSofi0cZWbZf9StZ1_1lsjQ_V_O4-l5DU-m_tjKTwhTlP_Hergwdc1GdIAMWxCrK5cYeUn-2xaBBnFAU0fwG_sbUvQbSy95CgGPlmvDNpDxqc5aAXrKA_VhThfotTpeHWMjVTK9sbkklNwzr_yv5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=cBiD2EWcWXTmbnwlllkC9fHS4HY_mYnVBIgLnNjO045lDZ4VFqFmANtgggnZaay5Au66FWvIy9PRcACYxPTw1H2yjCfxd__1T3nvNwGKvxVTrjdAwJFJy-titI-mwUKbPcJ6V6jhYydVGhQyXWBhRVzDD9h6dXh3afmRsnc-p9wlByMxqU-42-JrS1LxMKxZ2URv5vTuPSNGZPYWpoc6YsTi9b6zewVm_3WWTxxfhQqlk9bYHismlyBxuAaxnhycwTe-8HWWgqkwqh55tPwrdDmPvXnSiOafwszN7pmMES1yipDcOGXfdI5ZGaZ_5xUWoayjmABKrAP-lSOKCv_2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=cBiD2EWcWXTmbnwlllkC9fHS4HY_mYnVBIgLnNjO045lDZ4VFqFmANtgggnZaay5Au66FWvIy9PRcACYxPTw1H2yjCfxd__1T3nvNwGKvxVTrjdAwJFJy-titI-mwUKbPcJ6V6jhYydVGhQyXWBhRVzDD9h6dXh3afmRsnc-p9wlByMxqU-42-JrS1LxMKxZ2URv5vTuPSNGZPYWpoc6YsTi9b6zewVm_3WWTxxfhQqlk9bYHismlyBxuAaxnhycwTe-8HWWgqkwqh55tPwrdDmPvXnSiOafwszN7pmMES1yipDcOGXfdI5ZGaZ_5xUWoayjmABKrAP-lSOKCv_2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=aovF47KQnSuwQJf0b6E1n6NYl3dl8FuYkafzAN4omhoI3FqGUXsVOCA4k19b03YBNRq6HVbkh791cwPgUWbIJoj9dJxXljJimQD3yGMhYLk73wDY90bvgFZkY7XpI5sTTKuQ7B5yg_PMCtaaW6-1_JMOs0o68U8Sm_z4qClzm28wqvjSTo7BmfAJp4ZGaNu5LDE-MtvfGczakB19etzyRS0XVMkWc8NJergWIdgdDLR8e4Bmf9k1emPzWElFsd6NUMurtBFx5TmJlwuwLu8d0GkcmAYmbueAL7_ZwEY2ZovUvao6r5pa90qHC-OJqjNpNPbfJaePECsb8ELTHwAUmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=aovF47KQnSuwQJf0b6E1n6NYl3dl8FuYkafzAN4omhoI3FqGUXsVOCA4k19b03YBNRq6HVbkh791cwPgUWbIJoj9dJxXljJimQD3yGMhYLk73wDY90bvgFZkY7XpI5sTTKuQ7B5yg_PMCtaaW6-1_JMOs0o68U8Sm_z4qClzm28wqvjSTo7BmfAJp4ZGaNu5LDE-MtvfGczakB19etzyRS0XVMkWc8NJergWIdgdDLR8e4Bmf9k1emPzWElFsd6NUMurtBFx5TmJlwuwLu8d0GkcmAYmbueAL7_ZwEY2ZovUvao6r5pa90qHC-OJqjNpNPbfJaePECsb8ELTHwAUmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=ZYM6IstswJnCtvaFJ1c-G8f5N278x97CKGNN8lbjOtgzcuAh6z-85s6QGAYj_gUwbUCh2MWnL5WsVWV-33-4pv10W2TkRtRxvpQLuvx65yBN95OthYGxSyGOSLa2GxA7wKB_GDfL27-G-mimn9Hnn9dlfBSJoys2NhRY8JbwibZLqwPk0eyGzv55qZ1sjB29PgjcS5LqDbDqZvV_buaNCDZesrhyu95-5lOP8ziID7AcUPdVNmBRCtVa7RWKm4-gdNPi_rK_Sh_jJuX043mm1HBuvcMmRO8pR2K3BMTFjUhHt5KQPSNNU2U4YxvAanEgiYLo1QH5tW7GuxF01G8BkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=ZYM6IstswJnCtvaFJ1c-G8f5N278x97CKGNN8lbjOtgzcuAh6z-85s6QGAYj_gUwbUCh2MWnL5WsVWV-33-4pv10W2TkRtRxvpQLuvx65yBN95OthYGxSyGOSLa2GxA7wKB_GDfL27-G-mimn9Hnn9dlfBSJoys2NhRY8JbwibZLqwPk0eyGzv55qZ1sjB29PgjcS5LqDbDqZvV_buaNCDZesrhyu95-5lOP8ziID7AcUPdVNmBRCtVa7RWKm4-gdNPi_rK_Sh_jJuX043mm1HBuvcMmRO8pR2K3BMTFjUhHt5KQPSNNU2U4YxvAanEgiYLo1QH5tW7GuxF01G8BkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=fGhgVLI26zWAPbzh-MJYTJXnKAY29GlbC4AjN41H9le72caHSaXCFHCNAKRFTrK9wS3Ymc0EVyGKYC5SrlZAQQAAGy0EF97blPTiIzJRkobLCd6G5_w9r4fSp5zlTp2FR6WwG0THpJCgMQx-q28WD_Typtw6PPqKeMwtsj5m1zf_FWKHB6TXxfFAPlR-xeMIyLmkKVIi9QW3VrmqERQl6hZdqcd7t1Rk4u9v06ewIxSVb8j9U8ecBx2PfTktrHRiXUnx5LRPp7KMWUioCPxcr-l8fYCPeo43UkN1chzWCEl3l3bf4XZWKs4GV0TLHF4TGQFb9G4VW-H9pa4pVcdf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=fGhgVLI26zWAPbzh-MJYTJXnKAY29GlbC4AjN41H9le72caHSaXCFHCNAKRFTrK9wS3Ymc0EVyGKYC5SrlZAQQAAGy0EF97blPTiIzJRkobLCd6G5_w9r4fSp5zlTp2FR6WwG0THpJCgMQx-q28WD_Typtw6PPqKeMwtsj5m1zf_FWKHB6TXxfFAPlR-xeMIyLmkKVIi9QW3VrmqERQl6hZdqcd7t1Rk4u9v06ewIxSVb8j9U8ecBx2PfTktrHRiXUnx5LRPp7KMWUioCPxcr-l8fYCPeo43UkN1chzWCEl3l3bf4XZWKs4GV0TLHF4TGQFb9G4VW-H9pa4pVcdf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_0D2N4EbDDYcg3GiDtwU6k0G_Q8FG55fEkDdIT4kSXla5tLInJX2qHB1q2yTiLuG76iYmi54YbyyZHZ0T-4tIvoemvsqoj04d9m68yy7KPLM_tNhjbp1SQxcl5DuoeXqBqPKNw9UWaNch4zCcc573EQwF73YnLcWH7DWpVNnCmwX7QiBp4IleIMCSfm6wrRG4Dr55t18OUpQyPjoDsvLbiXmZltEGEYgj0TYvogr_7f8_2esTCwE_SQS4XmxMbF0YyAu12T_z91RS4eAQZyoPFsQ1OWRy9Mm-a71Cg4OlHWO-lJmSKsjM4T41Nn7Eh7Ns274S7459FumgW14eUkwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=sJTnzNyztHGjB5GuyDvap_eADFESbxBEanHj8ipj80U-YkIfbsMFm1z6JsQlrrc2Cwvf8qUpOeBIPZOSLdMLwcENd8wEJc1e_wk417uUQDbpVFJPdRNwgchVcdJqLdoLOjH70v9XOw5-UTG0k05FeFfLe5I_zljOojENTpSONthRYJMeqycbj39-fVp_p5obB428ry7F5Ks-hcqFQwB4-ZtQ7isxebeD2FN7ObMaydhpIUNxlpfWR_1mbfkSDafEPlVg2vop9e_F06QUVmrJqeeaw86jhpjx2UwKlsIL0QexXHJVorlqAddIyZDLpwtPgxr4b-Re8x7C88BnubavZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=sJTnzNyztHGjB5GuyDvap_eADFESbxBEanHj8ipj80U-YkIfbsMFm1z6JsQlrrc2Cwvf8qUpOeBIPZOSLdMLwcENd8wEJc1e_wk417uUQDbpVFJPdRNwgchVcdJqLdoLOjH70v9XOw5-UTG0k05FeFfLe5I_zljOojENTpSONthRYJMeqycbj39-fVp_p5obB428ry7F5Ks-hcqFQwB4-ZtQ7isxebeD2FN7ObMaydhpIUNxlpfWR_1mbfkSDafEPlVg2vop9e_F06QUVmrJqeeaw86jhpjx2UwKlsIL0QexXHJVorlqAddIyZDLpwtPgxr4b-Re8x7C88BnubavZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1DON3OcHUi2iraAhBeOyLKFtOo6nTZFku8ag73zEhKaYY9z_KYzKyzMJt73_WR73txZ2mu5ICjA-GfpBwUql3nv18--l-cTqx_yYuiQ6K_ltEDGMi_uj8hjWhBJ0fXndYqTBWGJzIdAIHgmGw2p4R3m2yWDKFj_X5wUxFYJ69FzDWoChoj-ow-Jdv5-UcKS_2-ArdEmvq_r6KzWkjJPPduBogJIFXH9oGo-SqJNe4drECI96EP8fmQD9yUXy7jrFwybatJb93cOdyCiedeuqNqrPzaWG644LXysHgl0fam2hDwKhNHhWaPlvzYdNjpNR8UAiwW087sGpb_uYp5Djw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=WfXWpZhBl9TWH9XYUkjJHmI8EtkrM99kfMRuamEe7nudGW7VHkIk32jU_L-Yt41gK0uyP4z4NXbzZqHn03EBaDxli8kV6zfNvF127heLemePoZJMpCyjPagxVL5AbPuYSvcLGsqdceW8FPYF4yt1MlRnOoNBI_3MrAkCqvNJaKRLgOCg9L7r_UfM3EVZsS9HWAzE6UvCiZPQfZ92gsfHdqYIvkViNKqyWCF9l8grGUpAYl1xZysV6pdkwDTn-VkkCOZZRaR-tktWImgUNxR3ibJ5nARCHX34tUSxBORJtkqh61-WzJVcPK3estL4W_oqrwBOk7lwzvUS1ZAZ3pN_sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=WfXWpZhBl9TWH9XYUkjJHmI8EtkrM99kfMRuamEe7nudGW7VHkIk32jU_L-Yt41gK0uyP4z4NXbzZqHn03EBaDxli8kV6zfNvF127heLemePoZJMpCyjPagxVL5AbPuYSvcLGsqdceW8FPYF4yt1MlRnOoNBI_3MrAkCqvNJaKRLgOCg9L7r_UfM3EVZsS9HWAzE6UvCiZPQfZ92gsfHdqYIvkViNKqyWCF9l8grGUpAYl1xZysV6pdkwDTn-VkkCOZZRaR-tktWImgUNxR3ibJ5nARCHX34tUSxBORJtkqh61-WzJVcPK3estL4W_oqrwBOk7lwzvUS1ZAZ3pN_sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pen_7eVBvmXxH2RLDSe_yp-2A-ijbkuFLUAMvmlxlNn2oIQIzNrHe-GXsnHrIpODygabWVrnOximlUJQf5FlNV2tGMXeIgg9J2opPZF374MBkrb3B883VcCvaA8jSIbHNeF2MNb9G5PdhDABSwRcRMJtmP3OeWgMPlvc95HYxyYTNyBeckLOV2Vc7BRexZRZ66yvZ7TeI1HVtySrXMo-CJWxA2OnhyjGLQUk_qGkvSrAYLEikufoDKbR8V8Mjlhd_jw7MSxYfLHjDfMLoRmS6wUYkVdApAFUbCKv7blLFGGTM_LGVm6VS38h694FUpmx0meUkCn5qWmrZCA2R-SWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxJHMbzEYbhzMCpRN3v-hEdz67m9Z0L7uKX3Zq0MAVaUfVUrLFM7bsttuzu4gv2skBLhWRtZ8gvsQb0DnU62jzfW4qLFWH7VJUIJDI-FzVJ-b9pXlV54GmQ2cdxdVejFDUnPGQUNmyvSgs3r_XupryvTZwdPHXfrao451_LsEQYyQJN4X8lY3m3_9J8QsN6PYPvp1NDV5Q-MvBBmZM97ZmS4ElkNH2z6ywdoqznflOa8IFwbD636WJsvGVHuE8NYPfMWaepK080E88CzlZ6sIUoVXEnOupXsd3661GQlYbtBvin0NxN9K_W1Km1H789yge7gNy8-2PWzdUxHGN_bmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTyVB1PDtqgBDJa_H8CjlJRonBOF-3eZ86FurrOlm3H0NTpUBDZkMHhD6gpcfGkPPaLQAW4bBOmxMCbAtJj6B_UpRvM2ZNVYYbr9OXzqn-KwAK7D7ybDySkek4BhazC7Cm8pJ7h_GfQ_uZShGr2ZmEZKDM6x9SYFHFlAXyLTjeH7chjx1zHyZwBtIKZ7zIVjILi5JyvUep5Rx45h_acHQ-EEwD-HQXOc_RfhLuZI9U2agmXE6JJsVVmUKoH17Gj_0f_Eh2P8lHA-PVbOQCpgqg1cOvZO7YZevIIFNHcV_JUDVX8ii-ZNPfDIJIRk0PjoSR8hci_dWCc8EUZzXZ_C4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4flX42deNyxMBMGE3UtdsUcIMH74d8Oi76_VPqrtls5xRZLwTEASuskg1kS3QaG1s76zhbGoYfvpz4R3JvhsUSkmAWO8Po3-tTAWFDIJSw_Gthfc1iVJjBxGhRNF15z2FExXiVrRGcBrhHV8LJ_nH0xFJFlvBnThN46VzlKSM0ZAn6EzJxnxLg4okXQf90DrTDw8IRsFdT4otkk-PUzVWeTjBb5X4OzXtuvcKPzCtPImfDlX-wQ_cOat2SRTpPpoAGuT6D1A_0Gb-a8Qbx5zHjenljy9_e61uNE9C5mYm4eZ72Kc_WujPTnM7HvpI9CsJeT3X0U-VDau-uQLjbuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=OKf2Gk3x8KSFI7hdyRFxVfb9yqISqzb6mTOuXesKgajqwhH7ApAEB1WkRoniYHQmHZ0LTPQxMoaeGQj1OFhDJZUNhSh6If2HACRKxPNQjKFyterT9V8BLyGRsb8IfqE6YkmUP_LVOm-_BhOrtrEU_n9u714tKYjowSIwJG94u7qPD2pdUnSTQGtIHdEMppAKqVYlgVRxt3jStJzAvS9dO4ha9tDjJfqHS_Ww5mcK8PaD3Py7DJ0m1b7MoTrVM8GzsSsRQilT4DJvPNuTAFEd8kVTFy3akRndcgLvf8I5o-RCku-p7dn9bR9iSh9y0E4qgLIgtoCHc0qp-Q9qg9y-8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=OKf2Gk3x8KSFI7hdyRFxVfb9yqISqzb6mTOuXesKgajqwhH7ApAEB1WkRoniYHQmHZ0LTPQxMoaeGQj1OFhDJZUNhSh6If2HACRKxPNQjKFyterT9V8BLyGRsb8IfqE6YkmUP_LVOm-_BhOrtrEU_n9u714tKYjowSIwJG94u7qPD2pdUnSTQGtIHdEMppAKqVYlgVRxt3jStJzAvS9dO4ha9tDjJfqHS_Ww5mcK8PaD3Py7DJ0m1b7MoTrVM8GzsSsRQilT4DJvPNuTAFEd8kVTFy3akRndcgLvf8I5o-RCku-p7dn9bR9iSh9y0E4qgLIgtoCHc0qp-Q9qg9y-8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=XRhy0L-imRVVp8OEe7YBip-OgUsMmLXcYkCsKC4KQe1i4l4agi5pgctEPDF-_E1vSz6cx0WrkefWxMQn11Aub5J6RhChW0K24Y1nIQUbCNA58HFRZwAMO5k3Qws7rc17SFiZtRSNp-urtAky7N9qpswTaS0zQ116DSDzsM5VuDLsCfX3hGBnNt1LjJ5qHINp6fn_lTsi5U2k3-o_kgh4ZYwEpxJTCXQp7O1h7D295anCBBEGm00aRUCBQCm03t-xS4o38Knkia1V9aCmkpB9jjC24Q1emwJs8W7_Zy53wzNGdCle1NwtSleJSwPPv_le6Zr0W53j_xnhz7Am0DDAxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=XRhy0L-imRVVp8OEe7YBip-OgUsMmLXcYkCsKC4KQe1i4l4agi5pgctEPDF-_E1vSz6cx0WrkefWxMQn11Aub5J6RhChW0K24Y1nIQUbCNA58HFRZwAMO5k3Qws7rc17SFiZtRSNp-urtAky7N9qpswTaS0zQ116DSDzsM5VuDLsCfX3hGBnNt1LjJ5qHINp6fn_lTsi5U2k3-o_kgh4ZYwEpxJTCXQp7O1h7D295anCBBEGm00aRUCBQCm03t-xS4o38Knkia1V9aCmkpB9jjC24Q1emwJs8W7_Zy53wzNGdCle1NwtSleJSwPPv_le6Zr0W53j_xnhz7Am0DDAxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY9kKDonB5NLtfG84ZfrJyG5aR1xhXmWL2vB3M6GQgOwTQ-fkhFGIRsZzGak1BOkhgy80HWd0-jCF0nJ8K1Pt7yMqUx3ZjlfUBEVHaz3o9Dp9I7HI1cT6TYwG5revUcYS_iwKj9gwgfZ-MhVpRbpFvna9dyeuCQ3rx8FyattsS1G9RKbXgPYDYJwZD2b7SDCofs9oRoco1NhuN75WSsDb2hiqug8JvCWe9oM5sSuDrpQwEaUZif6qn9lg2g_FOFZvDHliXLXT_dFe2qvpFpVMskKh3byG8A8EL5Btk9ZfSZ4hfwR9SriO8Xyd-tES_GuT5iE_LxIUqRUckDQGua0cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhMGMiZ8Gpl1Q5rVJG014we60dfF5U7-v-rmJfoPhExupPKv3lpVKM4S_QTZ1briS1qNUAiDZQoBbqlJ6TICWH6sYKGux59P14ST04Q_rzReifnbO3nF2ktIIcT6OBlQZnEzfRFB3vqeD7JtCycHPHlnT8gykopwTIiDAVUE6CJyomSilh9vg4oBQLS_Uo_tT9fTUC1QmyyCMo-mpiLtGlGKOKR2E1uYlE9ptu72rrya92daO31obkPPclc3nebmQcLwPf08SzXgOJEbDMFagHGXkuvarjzZPglRgIUTKnmnwXbTTSjJyQ7aPd1_LYjOpbR-DNoW27LHEvFvNlh7IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=PnxQNd5V4vi0MwqbYfKV9YyYWwFFOa7zT1_KdhV95uiIlu1LeH7cs4af-V05BI0XVlM_dg379LxHne9Wc1jrySg2JeKwKUEUVZOg4jdHxN0VVMREIPA2pqyXmJukq09MNu1LNjEnpvtgMkiQs269X7FPrcv_ychZ50ai_CmjOfkUQBbm17riHQgmcggLiRJJBvNJAyzqSSbdK7f6qzQRHlBN1h9aEg_5Uc5S7O4RiP2jwZTnLoMmL53wOcSiI8hVGRT2XCCBTiYmNbP3wmPPyJXr4Iq4RlLewmNbrbis197CziJpOQp-xgip5igp-eBUb4hBZM7Q9A04zyEE4ILLuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=PnxQNd5V4vi0MwqbYfKV9YyYWwFFOa7zT1_KdhV95uiIlu1LeH7cs4af-V05BI0XVlM_dg379LxHne9Wc1jrySg2JeKwKUEUVZOg4jdHxN0VVMREIPA2pqyXmJukq09MNu1LNjEnpvtgMkiQs269X7FPrcv_ychZ50ai_CmjOfkUQBbm17riHQgmcggLiRJJBvNJAyzqSSbdK7f6qzQRHlBN1h9aEg_5Uc5S7O4RiP2jwZTnLoMmL53wOcSiI8hVGRT2XCCBTiYmNbP3wmPPyJXr4Iq4RlLewmNbrbis197CziJpOQp-xgip5igp-eBUb4hBZM7Q9A04zyEE4ILLuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=hNVFVIQ8Ge7k8jD1mu0RSrnBIerNze-2TzoCO5uFkTMWClS5yNJKwMZLoNaylUgjduztD7kwUzsdK4gyrZu90aRuW2w5arAr3ZnF0xwa7vRqowvfqHIh4BDpfUjIDc-pV9C3aVeWTWyGz_N8iBGBCkmVD3Tj4FF8ENHegrehXvAM85VJ2kXh_ZBC3QZhu8BhI-xpwKYO-A5n5AmiLTWC3pAurbNpPZnFRK1d_Ed4mB9USksssMLBwE6pWc2j0AnjU1ic0SWovqRuHOfEMbvhV9YI9k6B7sbI5w78XT-AvWN6Dpe4U3OhdUUn-2AxJiTAjItlowqRY7V8Up4yu4Pfpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=hNVFVIQ8Ge7k8jD1mu0RSrnBIerNze-2TzoCO5uFkTMWClS5yNJKwMZLoNaylUgjduztD7kwUzsdK4gyrZu90aRuW2w5arAr3ZnF0xwa7vRqowvfqHIh4BDpfUjIDc-pV9C3aVeWTWyGz_N8iBGBCkmVD3Tj4FF8ENHegrehXvAM85VJ2kXh_ZBC3QZhu8BhI-xpwKYO-A5n5AmiLTWC3pAurbNpPZnFRK1d_Ed4mB9USksssMLBwE6pWc2j0AnjU1ic0SWovqRuHOfEMbvhV9YI9k6B7sbI5w78XT-AvWN6Dpe4U3OhdUUn-2AxJiTAjItlowqRY7V8Up4yu4Pfpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=deiSyac-HesM00eH4TBg_5gVO3nGyv-fX316PmqSC4wQ5NihhEw8qZHqBDE5lgegeOYExKHdbbGQ5fRcu2buMfGkjzd9VOTPT7UzcxoMXedsi1C10CmAsIE7S2NPP2e1CJBOPBUKW-5vjvPCfitdQ7j-BFcudCkBKK8lYYCEYGfTeJxQ5MOg7BVfncOBg_rXY-DfiJjs3vX40ILAn3qJ_AByz5zxh-hQ8X4XDogKcBkzhm2ofruobF-rcnX2o8ZxbLFga-MuNoX5uiYxZ8lbHDf2FAAzYNALxjeTgsbQ0H7mCas3pHp7b1IfpIxKSgycjX6Ob1-7x0CxUe1vfcjyxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=deiSyac-HesM00eH4TBg_5gVO3nGyv-fX316PmqSC4wQ5NihhEw8qZHqBDE5lgegeOYExKHdbbGQ5fRcu2buMfGkjzd9VOTPT7UzcxoMXedsi1C10CmAsIE7S2NPP2e1CJBOPBUKW-5vjvPCfitdQ7j-BFcudCkBKK8lYYCEYGfTeJxQ5MOg7BVfncOBg_rXY-DfiJjs3vX40ILAn3qJ_AByz5zxh-hQ8X4XDogKcBkzhm2ofruobF-rcnX2o8ZxbLFga-MuNoX5uiYxZ8lbHDf2FAAzYNALxjeTgsbQ0H7mCas3pHp7b1IfpIxKSgycjX6Ob1-7x0CxUe1vfcjyxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=Tc_Tk0SGPSp7hSVhZencqiWlHLYeN9LFqNvinNnL29QDb5XRdgwzFz4RGUummF0LLbN3n7nVcqUqUjM4w1D-ouFk4yGfnBA29rb5ilmXeW6n1GF2J6mxJ51x3Rlq_CTPzvB1Owo0Yf1q9GdHx7xFglXKv-iPXFS5AZKfhJiYQ4xWPu5V5OIUNV49VJ_PljYBakQeZ0cyuYD_t1tB9hR4lF0-mu2jIVsYjbeliqJvrWz7xrEWHP7InKL_ZZUi9icLz2m4UY7V_08tjZokgOD31i9FucEwOr4hmLmuCaKnFLvGtYwjQVADUMp9w6NB8VD_ZRKVTuFm4WVEjmB8Mj05Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=Tc_Tk0SGPSp7hSVhZencqiWlHLYeN9LFqNvinNnL29QDb5XRdgwzFz4RGUummF0LLbN3n7nVcqUqUjM4w1D-ouFk4yGfnBA29rb5ilmXeW6n1GF2J6mxJ51x3Rlq_CTPzvB1Owo0Yf1q9GdHx7xFglXKv-iPXFS5AZKfhJiYQ4xWPu5V5OIUNV49VJ_PljYBakQeZ0cyuYD_t1tB9hR4lF0-mu2jIVsYjbeliqJvrWz7xrEWHP7InKL_ZZUi9icLz2m4UY7V_08tjZokgOD31i9FucEwOr4hmLmuCaKnFLvGtYwjQVADUMp9w6NB8VD_ZRKVTuFm4WVEjmB8Mj05Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=k5brcV5NIgSZOOdmooibbaX5hir40_cq3KNJV3Sztb4nGbzbkQZDMbpZFLE_JQc9x9HUIuf-u0UOLANta-JnvyelrCSXN3taN38K0lRECT864BmNPdssykRygG_5v6GXwt3fVcImYA7KXbrzB7WodIuEyEfTJjbNUevWIo42DTXOJEdDdyWNGgqHTdJvuFzgEPx9IYAyv8cv0lanjImjVXV8VkAwSUhoE9wxods_qnQeJ9mZwXEwir6P3O5HesqTgvuovlaVCTFzBNjLeydU9P1fOapFhNjKAbaT4cmw6Bhl-XPL47HVy0HkNbMZL7SJOY4I7a2rmTFUQU0CyGJH4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=k5brcV5NIgSZOOdmooibbaX5hir40_cq3KNJV3Sztb4nGbzbkQZDMbpZFLE_JQc9x9HUIuf-u0UOLANta-JnvyelrCSXN3taN38K0lRECT864BmNPdssykRygG_5v6GXwt3fVcImYA7KXbrzB7WodIuEyEfTJjbNUevWIo42DTXOJEdDdyWNGgqHTdJvuFzgEPx9IYAyv8cv0lanjImjVXV8VkAwSUhoE9wxods_qnQeJ9mZwXEwir6P3O5HesqTgvuovlaVCTFzBNjLeydU9P1fOapFhNjKAbaT4cmw6Bhl-XPL47HVy0HkNbMZL7SJOY4I7a2rmTFUQU0CyGJH4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=Q_J21YXEEfsPOlo60yfHroaXLU7jYVQVik_dpRhG-wAeS090lNmj0Nv6Yq8qdVKeNnzWirBci35VwlR16sqaxAnuDEYZGpKKPWSgnXrdGllQrG9P42UpgFSVcmFVrHqS0_caHY9vm1t2eEC1RxPwAxj25MUZG-v7qB5ba9g5AJmnUzK-P2FrWJ_cF4WPTWk7RasR7bxVLT9YS4cDAtlzNZ6FVIQBEKwAQP9qQleMp_jGhIKjDMpO9fTW9pcSwZvR6A8sdKhlMlX-m6NjdY5OwS-cqsSEfwnV4OJu3gBtt_0tMVvCK02jEmrM-bYLtn0k0ZcR5ID9GSljdijFCh1JZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=Q_J21YXEEfsPOlo60yfHroaXLU7jYVQVik_dpRhG-wAeS090lNmj0Nv6Yq8qdVKeNnzWirBci35VwlR16sqaxAnuDEYZGpKKPWSgnXrdGllQrG9P42UpgFSVcmFVrHqS0_caHY9vm1t2eEC1RxPwAxj25MUZG-v7qB5ba9g5AJmnUzK-P2FrWJ_cF4WPTWk7RasR7bxVLT9YS4cDAtlzNZ6FVIQBEKwAQP9qQleMp_jGhIKjDMpO9fTW9pcSwZvR6A8sdKhlMlX-m6NjdY5OwS-cqsSEfwnV4OJu3gBtt_0tMVvCK02jEmrM-bYLtn0k0ZcR5ID9GSljdijFCh1JZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8ntc6eTv4jKjYl9h8T4_-gwd1acjozOAVexvKKHzMd6sjkhxj5a5JQpMEL-hOchsrI8ecRHIeniJrN3N26c3hvicZo-rdhJ_5-bX0vs56d5yUwhzGp9ys9JG386r1eR5ClSS0sY-LZM442kqwAUufuOpPFdvwQI5p9gP9K3rb6QlQxfOn5oHOFVuMt6Bvw-z7akASRHqGvf7APKXmHARrU_TxJq4c-mMllicGMKWeL8vxlpNBLQZBglPSccUpZYePoD_9PtqHisySbQpd8ekh60AJLTRYwvDNuTwkp9imIk-2F663mR-W9lFfL0NCKUARHGis5Ppx_rrE4eTe5Wjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oCnsknIS0i9Gkn1lQpn8lTvzY6VRofwgScuZsD00PGMZ6mrMC2C4ZoI0VqkKFVb4JlGL3-LXE7Y3xTPLl6fTdsa2R4ITIrhhk0okNuCj-t8Uz9x7-pIXC5cNdaYE6EZNQrj4GNp9W-YfOMgowu4dITuc6I3DKxsJuHiXR9pBqvQ_ua_VKCdQzPbpqfGNG2HUGjtvJzvPITUFogPyk-P8zqr-kpNgl5kFWfdXNyPCl07To1A5DKgtRUzjck0VpXK8FIn9Tq8aXgfY77vjuJYosoyusrQ_iHS91coa1pE_BH0WVjpBDcxYZd4GKUWTxDBQv6fUqEJBQlFxKd9dhpAIkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aypPadtNERrAICPg_D2WN7v7ictYYKoBalHle8NMrcwj9BINn3MhtrqCUycxqN6C0AM9THDEJQ77vIFb6z-vZoiDy-_ZAEUarcBzDFnm3yJrS3w8ygt_LnJop394uAmFeDnU6iOO0JQ-zEbkr7i_XCXCwZqr__xewvr1DvQVN0ea-UQaNt0WepMSSwySZtXDizSurI4br7wEdWAeZOEVZpWgT-ktIbQ6YQ4UE5rJsC5RpWv1Z803m-aWlWlolR2dJUYI-ip47vNSfA_yV5sIQ7mR7C-4IHdoZ9UEIbKhgHxj_Y7sWaVfVqN-03SUFyejhsPsA3ykoeRJegg1_NWm7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=GRoFnto5v-rNbYl_LcxzNOmLi6GQhV6UbA_5Xuv9mk_duQ8-L0Dke1WQH-Fc0IUKrPD7D57e3H7cqxDICwaGmAAQwS-CCifAOZfnvsQ_3SPiZFQyxsnGm4FP7b9rNtYT1sPpuTB-imdMbuHo-Rg1DV8QWqYWQJh1VbK_QJ5q4sUWRyWkDgc2PSlbkki2NXWrVLpjWkUKk2sNcT8V8Tk7K7x7IRUjZY4TrUrJXHNnPr4eHI4IV-8mZYOEIxVVEmsAfh5hmndXFHQEgvIpZmJNysl4yCqBkRTPw_dGsN93O9DZwq__vPe9KCqjWDByh4vB03_L3fxBkZ6NPQZiFfZ0Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=GRoFnto5v-rNbYl_LcxzNOmLi6GQhV6UbA_5Xuv9mk_duQ8-L0Dke1WQH-Fc0IUKrPD7D57e3H7cqxDICwaGmAAQwS-CCifAOZfnvsQ_3SPiZFQyxsnGm4FP7b9rNtYT1sPpuTB-imdMbuHo-Rg1DV8QWqYWQJh1VbK_QJ5q4sUWRyWkDgc2PSlbkki2NXWrVLpjWkUKk2sNcT8V8Tk7K7x7IRUjZY4TrUrJXHNnPr4eHI4IV-8mZYOEIxVVEmsAfh5hmndXFHQEgvIpZmJNysl4yCqBkRTPw_dGsN93O9DZwq__vPe9KCqjWDByh4vB03_L3fxBkZ6NPQZiFfZ0Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG-7avjdm4LDWVesEu7D5Eu0z1_trJuGYjDNk-rPNk4Vq0xxVvlkX3CgCD31kWRVBx-x3kkYJvU1y3g5bvlfbADB3sYhW0zRx_j7pNtTvHFVfhM4uCyZpBuPcQlY0Ipr_JuMLhtCPT30xFpwsbLrX1fNzyRg_7W-GbP0V0iS7rD5463enA2gOoQb9XWV9rHzAYVJIASrNq0a5xnVvnSNoOHuDtpPVQ9DdZA3lTCWd9Cs17YjSpXThBE_2fJl6UelMbD1zznVUrpcVt0-0Ecb3FeUKWdyrc-ah3Afv3dx9wSJ8A_RVu5IHleAoI2mbi3DeAfUCL1t8bH5akH3y7qCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=Qmgf-oEVVcdiVL99jl4bu8ICQvfivqjWxFoOTNXB97PHP0OukywOKF8m3R4oDrgit1z3f9-ClzvrKjrv4gsx96AV3Hge0nU4SLa7kNPm7fo6Ep_z4umdZZsALvgjL7w-DLA_lpo-XN0Flfy2BKmDWlCxxRs_eBHSA2Y23LGnWz6pNvnmN5irRdwL6wd_baRNbnejTXlNXEc7HYzcpnmlkiPd3J2jWRWoChKxoRP_9jWhMoiPsJMMtTQ8beSU1MeCKqoErZJduNd32lYDWfMz60Ceq2iwjjFzgk4WZvbQF4wVGBa_gOXbDoDOaacEiy3EeQY17TmwO81QOFEHscxp7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=Qmgf-oEVVcdiVL99jl4bu8ICQvfivqjWxFoOTNXB97PHP0OukywOKF8m3R4oDrgit1z3f9-ClzvrKjrv4gsx96AV3Hge0nU4SLa7kNPm7fo6Ep_z4umdZZsALvgjL7w-DLA_lpo-XN0Flfy2BKmDWlCxxRs_eBHSA2Y23LGnWz6pNvnmN5irRdwL6wd_baRNbnejTXlNXEc7HYzcpnmlkiPd3J2jWRWoChKxoRP_9jWhMoiPsJMMtTQ8beSU1MeCKqoErZJduNd32lYDWfMz60Ceq2iwjjFzgk4WZvbQF4wVGBa_gOXbDoDOaacEiy3EeQY17TmwO81QOFEHscxp7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RTL3BW1IOHW-wuX1RKRpd1NY6LNu--AmJL-RO2_j4WtKUYyKoII0Jqmkg8QMz4hBJQocpjpiVYEUmGXW5Xt3jP-Hcv4VQQxiDINiU3hOzVsLAyuV9v6hb2oSVfONNk5HEejTzXjN5ZP_Noxs8felzC244VWMLmRV0W-Y6kqVPnmxlxvObSK9WFfRjdFJiv9HjtQ2gSVL3UaTv8eTCy5h8Klcwrn_Wf08-KTHpmQpVtncKrb1FKmiitKCwQcB_oeK307iPcv569_zXEKCoIYXPdbg9-dM_8BICMmgFRlh7UtHiR3qI_CiSgD7jwDPkfIm2gHQJtk5F9lqwmlRIetkHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=drBo5lUN9LKMF9ZwlHAS2e8jE2nVOCxlmnr7sdy8YzKphygVscfmyJ1g5wNQOTquVuh8wntMEqVr67TEAgbw3TcM52H1WTc8nM4bzhs7pABW4btt3a9YUEgBcbq4QaiNaLYMHkyOYVeLwPeb3_YXyvlC--aK5Te1jVxo5uJnFXHPD_3n6kLEvGZjPB7Y1ciZAYSX_Fh0q7T8sJ69tbcAjrhJZE4thviqiJA_zAoeGwF6Iy9T_zxxoihq2gaBbINP8hwxLOVS7QKQ_u0oGimcHskdLXaWLye26mTyKCzBWZSSo6tt7GI7Gva3hwHsbgRp1ZXVP07Dbh4rCWgG5HE_5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=drBo5lUN9LKMF9ZwlHAS2e8jE2nVOCxlmnr7sdy8YzKphygVscfmyJ1g5wNQOTquVuh8wntMEqVr67TEAgbw3TcM52H1WTc8nM4bzhs7pABW4btt3a9YUEgBcbq4QaiNaLYMHkyOYVeLwPeb3_YXyvlC--aK5Te1jVxo5uJnFXHPD_3n6kLEvGZjPB7Y1ciZAYSX_Fh0q7T8sJ69tbcAjrhJZE4thviqiJA_zAoeGwF6Iy9T_zxxoihq2gaBbINP8hwxLOVS7QKQ_u0oGimcHskdLXaWLye26mTyKCzBWZSSo6tt7GI7Gva3hwHsbgRp1ZXVP07Dbh4rCWgG5HE_5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf9A3oCdNEQm4tl7yFKn7btbwCJSvO_XjuRYhjbMWWmJGvWZKH6Iup_VKH75BKuyYdCWm0BnJckC8pnnhFvlOInIbXxjU3xV1-OvTKCB_dsaCKEdC60Uu3i92U7rPy3I12rGBzyilOxb-vTFZGEaaaEJh6EFWs8Dq-3lNVyNOTYAJRm4U4SdsCBs1WwZ89TTUseptnfUYv_2Q07o2LrM5oPezCnwH_WTJwawKfL5ay6_A3d8Zi_7NGOxMYzdw_GCBgB6vlS23lDBphfHoT6L3dPyeFZCgfnel2UPqjEfco14a1v-LRYmXRTZ5DOKVvCLxFMVkLH1Ti9AJhYQICz-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=gHcFqxIfsRdWClDte9jwxvhhO9aNvG-2dGvPsH5o8sS0wYxXckEKw6jDe9uWMvVzvLlvjOPykdSG7ys38Pru_pm0zs68M20mWh0gAuGgzCiw9KsEwUHeghdOhPC4pXTGXjErKpNxEoXKYs-neF8PKLFWmnt15qiKIX7BZzTCN-bwpILALvliyTKWtg9viu8Ko0cdCKfnF6Tx5v-y3Z3XwfrHhjvWm3sOFkRR8NAQfcY5lC2uGHToxsCTWrFQ07uCB7VA_AU7hKx_NZiE6c0YF3O5aKA3jwyuPUvoDJQ4kcvAjy6739J8MR7oFweVo0diCon7xc-ZEhjEXrav8m7Pig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=gHcFqxIfsRdWClDte9jwxvhhO9aNvG-2dGvPsH5o8sS0wYxXckEKw6jDe9uWMvVzvLlvjOPykdSG7ys38Pru_pm0zs68M20mWh0gAuGgzCiw9KsEwUHeghdOhPC4pXTGXjErKpNxEoXKYs-neF8PKLFWmnt15qiKIX7BZzTCN-bwpILALvliyTKWtg9viu8Ko0cdCKfnF6Tx5v-y3Z3XwfrHhjvWm3sOFkRR8NAQfcY5lC2uGHToxsCTWrFQ07uCB7VA_AU7hKx_NZiE6c0YF3O5aKA3jwyuPUvoDJQ4kcvAjy6739J8MR7oFweVo0diCon7xc-ZEhjEXrav8m7Pig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=I0CVjso4k2W5A83PQe1A7ah9rz3tT0RBjGEGNuEVi7U9TT3eLosGqNyZmPuUBvLcllpCRHurpxsnz4ls8YhLReCJeGGjFr4dIvJc8a0-ZyOzT2zKdL7lSVL93N2cf5PiNCKuAZoyxUZDvYxyMLwqmPYPwrTLpJWndTcRKcFRkXwD4aPZhS0bpt8f7c0Klm5B5t0mvf1gS3t-RKWfwv_jvWwGD03Eu-opHKQqGzVn5MRHxxSqylU1EEm5uN-0A1qvZNnZHGWv14MBIJaOro-Nepm4CBA03AuKSsQxnFJHccZY_DWXnBXONddTQnF-FHkc2iWTzXefprP8PfKkj_0_yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=I0CVjso4k2W5A83PQe1A7ah9rz3tT0RBjGEGNuEVi7U9TT3eLosGqNyZmPuUBvLcllpCRHurpxsnz4ls8YhLReCJeGGjFr4dIvJc8a0-ZyOzT2zKdL7lSVL93N2cf5PiNCKuAZoyxUZDvYxyMLwqmPYPwrTLpJWndTcRKcFRkXwD4aPZhS0bpt8f7c0Klm5B5t0mvf1gS3t-RKWfwv_jvWwGD03Eu-opHKQqGzVn5MRHxxSqylU1EEm5uN-0A1qvZNnZHGWv14MBIJaOro-Nepm4CBA03AuKSsQxnFJHccZY_DWXnBXONddTQnF-FHkc2iWTzXefprP8PfKkj_0_yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvWDUtj_OcZZMv4uGdlVUMxxRhHpxSON0inuYRyYL_Sqawdzz6xvjKXa5i3SQQ1FOKgWZE6MP7J2mB5iltyKJh93V7nhJoukzv0z72fkUHxp1rFaribta263BQAUgzG_PE5Toj-8acN0QmVEl0QLwNT0dlsfMY0o-2PD6lXBf1Zq-WcYg9Kv6syq3wQAcGfQkSlAm9zSr2qDDXvKnL3IpCobsHC7MFXmPrJoHVgMvLBqDXXxc4wNYS82CFTgqgOvc50QpiBnCvxB_wMVGyscLgz9_kJuxy2rYTU6r2PBH52wkY8Z0uXxIZioCgi2mLtGLHSppmarf2nva7ie9ABCYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csPBoPycb26thISnfe1CbZ2kc98YnQdQ6VhXA0Z5r2KpIG-DCtnIrXX7dtmU9iVqsNatrQD3vlnwugyv4voUrHXuNtRcfj700AMWFkCepKGRoQcDnYM74AJ4WZYGaXbmZAUC6f4SvVhrEbxvBDsn79tTG8V1N_BHaK4But02PevBBd5zTlCjhG34WGWr8J_1Qk7tQckiuGeqEEyM6yCTJWaPX44RWnWOCk0EdHQfrWmS8D4e7fZVfA3Pz9wxTXuIVexan20sqKX1Op8S8AYueUkXp06-6FBv4WHzIq2ITPIduWZtSC8wwQe1kfeuItKuc6ExH9-pNCbLbS8tJjOaJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lU2Qggrit34ddMba6HNjucxoAeHdW5S6t6TqUubNpjqO8OzTqm81FfpsRTtz8zl7EU848-gxHKVXpsOBHJlZ7huMKfY9XsyYUb87UoGL_1ih6Y6vBLvL_u1YCk3DXTpuvwP3sa_akWoUTE4eY9T7LdBzkx6x5rIlCmITQORweQWB1s9BMi31Tl-SepxIdIz4IuxZRv9QJg2LOz2UCwNc0DOO09-XOfA3oSYr6n96hTIsZMJzQ9tb6-LhowDNHq-E4K702AtBBQKOplabdtUsaJvjY8xfYo8gOg8U3hEB1yNeOM54rqOz2Uvxfot9y6vt4hDavrjcdiRBWIyei-FR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=M0zkTRywOVndjBl3VEUzNiHzhU5YEncXw0cj4tlKTG-sIgGNSTk1pvmCvXvEqgWvrwXq5BB3hBUCAZoUpypBwuwUhp32BNJFdjvbZRD7ihGotxblV1ZNuiRYjpWsRbWkObfvgQlgqvZYMEeyzm9uhjsfap2j93ZepcYywYR1hnluX3KZG2XkQQLsl7k24GsxjV9eVx9CoD8ziL7kJsqOLY0lrG9Xhp3Q6DAX03-nofan5CW6q6rj3dH3ASQqi3GE8vVqSHabKDYcmhDzyp6xwyUiaFYwGtSFds7AvsH3yO-Cm6sPTYENrm8cwb_90tZR9TjIyl-6gP-JeH-K_OmwbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=M0zkTRywOVndjBl3VEUzNiHzhU5YEncXw0cj4tlKTG-sIgGNSTk1pvmCvXvEqgWvrwXq5BB3hBUCAZoUpypBwuwUhp32BNJFdjvbZRD7ihGotxblV1ZNuiRYjpWsRbWkObfvgQlgqvZYMEeyzm9uhjsfap2j93ZepcYywYR1hnluX3KZG2XkQQLsl7k24GsxjV9eVx9CoD8ziL7kJsqOLY0lrG9Xhp3Q6DAX03-nofan5CW6q6rj3dH3ASQqi3GE8vVqSHabKDYcmhDzyp6xwyUiaFYwGtSFds7AvsH3yO-Cm6sPTYENrm8cwb_90tZR9TjIyl-6gP-JeH-K_OmwbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=H-jCmo82WN230lkE0JVB54STy6_Jgm9XZlB72RdZa3OYnYnTnLPLsYsbx4rHQ0eOVWJtXwhGv3RwkJbO7Jt2oEl10_lx8XbirtTv9yWqdOKNQWqWOCr3sStzEDxVCYulQo1K0LStp6QqIhF-SnD2wWea9ogXCxuFtS_GUPuUVgGwXm9vTAaYMSu4_CS0IjzMBy4g8W1902lTAw9r379P9UoSCD89yny2mq_36kWoFL-jOusXNhvtnmJNcMegKrivVoLyBl6Gw95sQp515bOCkYFTVYsfhOaJyUFlgI7cgUrrmSvRzFi5-hQin1xMn077g45X1SMwD4U5KJxiL3Q4qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=H-jCmo82WN230lkE0JVB54STy6_Jgm9XZlB72RdZa3OYnYnTnLPLsYsbx4rHQ0eOVWJtXwhGv3RwkJbO7Jt2oEl10_lx8XbirtTv9yWqdOKNQWqWOCr3sStzEDxVCYulQo1K0LStp6QqIhF-SnD2wWea9ogXCxuFtS_GUPuUVgGwXm9vTAaYMSu4_CS0IjzMBy4g8W1902lTAw9r379P9UoSCD89yny2mq_36kWoFL-jOusXNhvtnmJNcMegKrivVoLyBl6Gw95sQp515bOCkYFTVYsfhOaJyUFlgI7cgUrrmSvRzFi5-hQin1xMn077g45X1SMwD4U5KJxiL3Q4qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTnEJVWeNbjCtEyV3b4HraeTUilcDIYezKJRrOfC_L399Tp7IyoXDTRw1bYAZCOE4zPuICrwpGkn-EAI7p0Oi-l1d3tLwICoaAb5r2Rz_u5bM5212cjCM_vJLD_zP_u8pe3ghN4oAyRYyjwnEa10CEQXhUhQu0Q-d9a1pKFfVCm0P_gpNL0UpZhhpEJq_RTivsoGG6oNMfSUv8Jf3bhCGzMLu1Q6urxhKIkz56g29GhibPCfXp7xTkSWsJXkgsoBG4xQKi3tqFp_gW_cbs7TQ3cMLDkkQ-evePk1oqv4JYDLIdERWeYbQrxPqpA9NhVPaDyANpuTUqglZ6TrnoWlDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knTM7E4UYW8t_0t_aAPlb5cfvo8QaBqiscfCu5qt5lvM8BvrqaY3nJeCw_q6kt1c6ssmOPNciulg_Xx0w08n0p9aE7qciY26E6I1FOeP110gipiihJ8xdDpEvWGck4PDb-VhEY1atClXTi8tNCy4guBjG4sxf8RbIVEnHcdc5m0q0XUWWxOzTsVuMJ-LzWD0W0YHmOgWOezhbaYWlDyKn0aRJAq5e4a7d1YVQS16BkRgk5GHa62vppPlpyDm94-NB6asl32fB3gIxgDvieL-AlycgxeFfUwa9M5QMmuLssxWcj5qOCql9avlzdvoKnwyPyypD9yV0QVx0JCLV9wnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMoLu5Ypsn3CPlFAuCtfHHcw1bKHFHrHIBgkVvOap1IYi0c01Q5JCR__WHSfBHLeH4-42LdLclxR-Yv8eymdUmHApvcLY2v8sjKCUVdv7u3b-8q7sRLqiGcMIxzkYQf_QXPefVxEPdDTCcP_dqCKZVyBs_mPovVQE4G-UwSFX3HJvGcb2kCeAaYMy_XRzUCU1BcnHeZV-T8P0RZaTmgRiGYbZFWOznOQ-jxVqO0D7GrFEuscIiqYl7dRXSpNd-PDiM8swiMZwu3BQZ1BaceTpYBQdrKmEdPwwE2mPhsOLU-v2_7Y8Bf160GaRM-KDgcVTIT-ysVtzJvJtqYWUgQwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=bnOqYiHE_ArKyRRerIXWRfE889_7dgRCpkJiZ4E1GsoJztDsC6ReJonaoNYoc2LvXb1G3XG76ZC_NUOFTPLzK870fMUG3jaY5UW6kiIaL5SQq8udxab0t0etwyHuLB_Voc-qZyLN95ggGrBVjAiHVjyMt8DSQ7XSmQQE8Um7x5u_FvJ84kHAOCBIZf24IsJn8SyXmsSBm01a0LvXxh1M8XLTqe1KcX9zfNLs6tS2atLyGhFqrTEi3J2Bj9v0a-Ckl0HWwPdgEVY7J5hKYSiNrrDt1tyzkuSBNu9jf2Wi1fEE6BP6Ybe7k05ypsboTdiPY8DaH54V4I0aUgaJIk9fkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=bnOqYiHE_ArKyRRerIXWRfE889_7dgRCpkJiZ4E1GsoJztDsC6ReJonaoNYoc2LvXb1G3XG76ZC_NUOFTPLzK870fMUG3jaY5UW6kiIaL5SQq8udxab0t0etwyHuLB_Voc-qZyLN95ggGrBVjAiHVjyMt8DSQ7XSmQQE8Um7x5u_FvJ84kHAOCBIZf24IsJn8SyXmsSBm01a0LvXxh1M8XLTqe1KcX9zfNLs6tS2atLyGhFqrTEi3J2Bj9v0a-Ckl0HWwPdgEVY7J5hKYSiNrrDt1tyzkuSBNu9jf2Wi1fEE6BP6Ybe7k05ypsboTdiPY8DaH54V4I0aUgaJIk9fkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=CjvXLEpskEuwKeW4OETV-KRIEY3KFLJoVWNMDnTKC6ZUggTQ4JgRtp_bjdDe0Eu9cSPgmluRezfpHp8ZDIzoPzZyk3UaCRa-5GAMC1CKgOICWuXQE33TQnaCgMvDEXcdauQSRfB5GqUbOw3GAmLwqPRp-T5S209pCXscIs__Wes9yiQ6I4nxpdP_VAouA7CgaxLia_kifnOsNgIuFwrNzJVOe-CVMX5ntwyPU6txmW0jtabDbKgOCPXHNOlcNqfqZZTDt6jZ5YIxRiRD0JQyaXmkDV7mFvhw49YR9qobb93Me_OcmNijwjldLGomBkAHxqUlZ06cASP7AvNcYZl4IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=CjvXLEpskEuwKeW4OETV-KRIEY3KFLJoVWNMDnTKC6ZUggTQ4JgRtp_bjdDe0Eu9cSPgmluRezfpHp8ZDIzoPzZyk3UaCRa-5GAMC1CKgOICWuXQE33TQnaCgMvDEXcdauQSRfB5GqUbOw3GAmLwqPRp-T5S209pCXscIs__Wes9yiQ6I4nxpdP_VAouA7CgaxLia_kifnOsNgIuFwrNzJVOe-CVMX5ntwyPU6txmW0jtabDbKgOCPXHNOlcNqfqZZTDt6jZ5YIxRiRD0JQyaXmkDV7mFvhw49YR9qobb93Me_OcmNijwjldLGomBkAHxqUlZ06cASP7AvNcYZl4IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=Icz1G4BHLp_SIqa4Gr9VVtQqP7XO3Z1cKXCjhP5qOWhPAMKNAZBMXxJ--qtQ5QDO6AWpqq-FbktqNIZxGNdxz86mMW_j1B2g9pjXmFFA0vlAiV9k0hrUjFb2OIz8OX4ALpwz-q3iU2R5Xjp-OKQUyCUEJ4pC_N1gqNQveqkfrypvvH2PVSP6xBnCc5LL91cKKnvxx-Al_DNoJIXm_jR1Az0YAn-8D6yNIk0FFgQ0RcVypWpqB78xhT70GRwm7Tl8Xhq4nr1AgEg2EHUmvW2XYipwVItcJThQi0Q7HwTnZLuj8WXrVrcfk0v4qI9mNRwLd2evG3xHQ4XE76G_LzSyrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=Icz1G4BHLp_SIqa4Gr9VVtQqP7XO3Z1cKXCjhP5qOWhPAMKNAZBMXxJ--qtQ5QDO6AWpqq-FbktqNIZxGNdxz86mMW_j1B2g9pjXmFFA0vlAiV9k0hrUjFb2OIz8OX4ALpwz-q3iU2R5Xjp-OKQUyCUEJ4pC_N1gqNQveqkfrypvvH2PVSP6xBnCc5LL91cKKnvxx-Al_DNoJIXm_jR1Az0YAn-8D6yNIk0FFgQ0RcVypWpqB78xhT70GRwm7Tl8Xhq4nr1AgEg2EHUmvW2XYipwVItcJThQi0Q7HwTnZLuj8WXrVrcfk0v4qI9mNRwLd2evG3xHQ4XE76G_LzSyrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzrYzIsdmCZwY8xUFrXg8Ko1POihBXQ8b1W8ravX89alywoqKEcmUfyomvnTYgjUHjvxCUoshxKN8a7I5LNqw3AP0KuQ6wgfvGcb907YXM1YMP8DmLFhxfZx7cJMjHufC6fYy6IRD_T-WZx33dkjQmlhVLGjcPSnoNoAkeozL14c2dsH60yA6Q1neZvLdg8BSzmLSd2uC2f5fYDFFumB1po_RdTGdktZ7UFzLGMJ5G3dpjc8sp6OIWh-W0sBIgBMsG_LhohKaN8n6qbRqN0VEOSZ5BzsCSuMFWrm5kLTeAETLeXVoO712noabjOyC33jPo3G_3sc9JR7-mQO7Oq2NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=s6KLobbSHVzawsxfcHUrsksO0hROk7Zv2eSrsUqyz2r0YGgiSSYXvziPD3FOQj6M1uejoKRwAVEbxq-fU0U13fxFbuGZrLMErImBnB5UoGKzKrIPtceaNFr6QiXVzkSV1O6i7s3QaykQX9oF6-RxJp24WNGJckSsLCa3UTYRfdJFee1HPo-pT-iTiu63bjKnGiHzH6crVLYCdXj47KQ2xmqfYs8xPtHaddwGzDQSDPxa0-BwtyP0vS8xwijZk4i63wWVlXH7bUFwSjidUiaZllaxmHUrzrVspVJX-X7Mok2mZjUosZc1_WxzNDIM0ui5FTmStRMOHvD8nfL6WnEwkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=s6KLobbSHVzawsxfcHUrsksO0hROk7Zv2eSrsUqyz2r0YGgiSSYXvziPD3FOQj6M1uejoKRwAVEbxq-fU0U13fxFbuGZrLMErImBnB5UoGKzKrIPtceaNFr6QiXVzkSV1O6i7s3QaykQX9oF6-RxJp24WNGJckSsLCa3UTYRfdJFee1HPo-pT-iTiu63bjKnGiHzH6crVLYCdXj47KQ2xmqfYs8xPtHaddwGzDQSDPxa0-BwtyP0vS8xwijZk4i63wWVlXH7bUFwSjidUiaZllaxmHUrzrVspVJX-X7Mok2mZjUosZc1_WxzNDIM0ui5FTmStRMOHvD8nfL6WnEwkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
