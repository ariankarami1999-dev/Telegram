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
<img src="https://cdn4.telesco.pe/file/GmHYsPgcrWS5yFbcFptC0uJreU35ZemWTOx83Ixs-2O86jlg6fJ9RtFENtoXzcMRbrIvJwI1sAYBA4-BL8W0Nes7Ah_kFRBcg9rZglRv-EV15yx4eEEgTmAiYYlUXXPIXIlttWmJyUMrkazomgA_FnvBY2Enuozd0yhGmQihlyANZsZThCkL6d4nndzqTi3Cv3jyyiC_xTe8_VreNFaT6_y98bEmD_1CLvMiAN4_VsUVG5ZInqZAiPeYwx0ysGYmdPF29xBpQSnr3pKabr3WrEad5IYszNcI-joA6U8BqZTyyvMf0g44VkvGatMYg1UKlTp67tGL_8A-A7pSzl1FTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 23:20:31</div>
<hr>

<div class="tg-post" id="msg-445209">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0d9e2eb96.mp4?token=vwrYu-zzVcie4RRsU8SgR-0GauYTsKNo5O8UlliC-F5xGOOrBH1Yi62qhsZ8zwmZJHeNeTwQT0FnEdaDd7G806g49gCpnaNRcx7IPhp3nMlIyFikq8Q4GV5L1X__9MutyxZSm8yUY5GBxL1o1ws7cD1eYUciHFRyzOpXRwTLxQ21PaWUh_imVAnRikBmeiI-_-AGN43t9yrgqlDjF2Lea-CRUEe64Q4FNt5YVyv3f_xARWnrCMjCl5rynWhX4ERNbOMqthPefL4qmAwPey3uh-yUxOlw7MFmP48NLjmur6xi5G6X2Og1OvdcpGom6aiTX4RHKQYMF2tRB1ClASRxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0d9e2eb96.mp4?token=vwrYu-zzVcie4RRsU8SgR-0GauYTsKNo5O8UlliC-F5xGOOrBH1Yi62qhsZ8zwmZJHeNeTwQT0FnEdaDd7G806g49gCpnaNRcx7IPhp3nMlIyFikq8Q4GV5L1X__9MutyxZSm8yUY5GBxL1o1ws7cD1eYUciHFRyzOpXRwTLxQ21PaWUh_imVAnRikBmeiI-_-AGN43t9yrgqlDjF2Lea-CRUEe64Q4FNt5YVyv3f_xARWnrCMjCl5rynWhX4ERNbOMqthPefL4qmAwPey3uh-yUxOlw7MFmP48NLjmur6xi5G6X2Og1OvdcpGom6aiTX4RHKQYMF2tRB1ClASRxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان انقلاب تهران در ۱۱۹ روز حماسه
🔸
امروز روز وحدتِ میهن است
🔸
هر اختلاف از جانبِ دشمن است
@Farsna</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/farsna/445209" target="_blank">📅 23:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445208">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8645d7b23a.mp4?token=ZAhyyT3s6UKsNg1hf84GADXt21YDCaAmF7wlqFYulzrwu4B7IBYG4q8nltHGFjDVtBsnP1hQNZ9djvpv60E04pe6rR4i4CITbOxA8rQfYnzdjtSufNnO1fkdvqhdRpnFXUSxxpyhqgyAbTve5DRHy2XNpL4DGKTE-40o0EoKwpbewC7whVALcnp5zzc90tTaP7Rp7Ea8MEOyEEP37WXGPeBaosfO6t_pgDIb_dxzv9VZF2pxBkqrjeOpBV01sE_a1uWf9GfPl6sME7HMZ4UFY5MFfkBFCmsSR5NQSK2ZuFos6q9xP7Ym8FLbQCRrhv9lwPUHWVkUV8HlzfB86EIqsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8645d7b23a.mp4?token=ZAhyyT3s6UKsNg1hf84GADXt21YDCaAmF7wlqFYulzrwu4B7IBYG4q8nltHGFjDVtBsnP1hQNZ9djvpv60E04pe6rR4i4CITbOxA8rQfYnzdjtSufNnO1fkdvqhdRpnFXUSxxpyhqgyAbTve5DRHy2XNpL4DGKTE-40o0EoKwpbewC7whVALcnp5zzc90tTaP7Rp7Ea8MEOyEEP37WXGPeBaosfO6t_pgDIb_dxzv9VZF2pxBkqrjeOpBV01sE_a1uWf9GfPl6sME7HMZ4UFY5MFfkBFCmsSR5NQSK2ZuFos6q9xP7Ym8FLbQCRrhv9lwPUHWVkUV8HlzfB86EIqsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: مسیر اصلی مراسم تشییع رهبر شهید در تهران، خیابان دماوند-خیابان انقلاب-خیابان آزادی-اتوبان شهید لشگری-اتوبان آزادگان است.  @Farsna</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/farsna/445208" target="_blank">📅 23:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445207">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
سردار حسن‌زاده: ما نمی‌توانیم در مراسم وداع با رهبر شهید توقف جمعیت داشته باشیم
🔹
برنامه‌ریزی این‌گونه است که مردم از یک نقطه وارد مصلی شوند و پیکر مطهر را ببیند و ظرف ۱۵ دقیقه از آن بخش خارج شوند. @Farsna</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/farsna/445207" target="_blank">📅 23:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445206">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ce2fd43a9.mp4?token=EpJZponimlXfTc3KvWyDeaC6nlxyLjRy6WB_Zf-fb9V7K22_Pwyh_OBy-wgg2n9ggod9EzZeZMpDTHAij-nFR4XDY6CNWs3BPPCmpwcVYrBzLumX-csDzKtRisgF1sOtqnFDnRD0vqXHSo9EZ0OQeVNX40L9n-m-3zUdElTssTfsFrKZLlnWl1OOPeY-BHbcjcr_HfNyq0BSbE4pdJIILrkoIn6UjXnQamYXZDmZlRpMsLtjkvOb6p756ZcALo9-e_PiPwT5btxvrPPWZY7if6XhhAbYxiLYw260v_MhLl6o5pSm0Ik4zOqbLP3kOC3Yxai8E67gSqXto-YazV1I5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ce2fd43a9.mp4?token=EpJZponimlXfTc3KvWyDeaC6nlxyLjRy6WB_Zf-fb9V7K22_Pwyh_OBy-wgg2n9ggod9EzZeZMpDTHAij-nFR4XDY6CNWs3BPPCmpwcVYrBzLumX-csDzKtRisgF1sOtqnFDnRD0vqXHSo9EZ0OQeVNX40L9n-m-3zUdElTssTfsFrKZLlnWl1OOPeY-BHbcjcr_HfNyq0BSbE4pdJIILrkoIn6UjXnQamYXZDmZlRpMsLtjkvOb6p756ZcALo9-e_PiPwT5btxvrPPWZY7if6XhhAbYxiLYw260v_MhLl6o5pSm0Ik4zOqbLP3kOC3Yxai8E67gSqXto-YazV1I5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: برای مراسم تشییع رهبر شهید انقلاب در تهران حضور حداقل بین ۱۲ تا ۱۵ میلیون نفر برآورده شده است.  @Farsna</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/445206" target="_blank">📅 22:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445205">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عارف: تشییع رهبر شهید انقلاب یکی از مهمترین حوادث قرن ۲۱ است
🔹
معاون اول رئیس‌جمهور: باید مستندسازی، روایت‌سازی و پوشش رسانهٔ مناسبی و در ابعاد جهانی از مراسم انجام شود.
🔹
با توجه به گرمای هوا، لازم است تمهیدات مناسبی برای ارائه خدمات مختلف به مردم در نظر گرفته شود و کادر درمان نیز در آمادگی کامل باشند.
@Farsna</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/445205" target="_blank">📅 22:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445204">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d91acc8.mp4?token=WoATxA4DAl4yuK4F-qIiBp4bf-rpdnz0in9BCZnFzHDEsF1iFKhYv91gD5aScWEH9CenbX6Kg65EY5k05Owcg1eQILMVhg3Q5sUdQARfuhrJVGDjylPKDik0apDy7-nbW249s153C8t1rPPBjGdo1OdX8a_iexQTwYqZL1x9ad85kkoiNSw3py7jeLDJiebFvvm6JQhckIJDApofnRNycGaGoe6cVJ6YxKdEJOGKrrIosKqoyH_fPGOXVN7VL3_ORKGsJ1KLFGW_3qWDyItt-dDNVAZurKrVIHeCIXMnUqXj1RGLouV5_8EfUZpmSnTDi37kMyQ_F1iP5ib2ffFOxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d91acc8.mp4?token=WoATxA4DAl4yuK4F-qIiBp4bf-rpdnz0in9BCZnFzHDEsF1iFKhYv91gD5aScWEH9CenbX6Kg65EY5k05Owcg1eQILMVhg3Q5sUdQARfuhrJVGDjylPKDik0apDy7-nbW249s153C8t1rPPBjGdo1OdX8a_iexQTwYqZL1x9ad85kkoiNSw3py7jeLDJiebFvvm6JQhckIJDApofnRNycGaGoe6cVJ6YxKdEJOGKrrIosKqoyH_fPGOXVN7VL3_ORKGsJ1KLFGW_3qWDyItt-dDNVAZurKrVIHeCIXMnUqXj1RGLouV5_8EfUZpmSnTDi37kMyQ_F1iP5ib2ffFOxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: در مصلای تهران بر پیکر رهبر شهید انقلاب نماز اقامه خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/445204" target="_blank">📅 22:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445203">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cb911549f.mp4?token=rneMZhhB4ptpKmMORuDjO7ZFBuEZB3rfYDS2vQ8MSCDYVbuOhIaw6dSixM1JnwPME7GcWkphG61GesLo89t01A3CfAqMkGiVvc1Ful3d67V7YCSZV7NXJkk3M762ixbNvW467fuHtzrcZ7ayctj_ONzgfXtzcJ0iQopbsrQtpxuXN8pqcClcFKOeK2F3t3r4ucdn29YU8Un5TWfQMdC-Z0BHUeND6qbpKImtdV_05BvZHydwv7uRPhCQCbvbrTnEo-0A0vuN7kxtGRJ8WrReUP9QksknwDLpkCeyE6ca_TAqKC_3wkPpKUU0Gw5kWYFJ_8ZPBK_XhPoOkWoGxMLdeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cb911549f.mp4?token=rneMZhhB4ptpKmMORuDjO7ZFBuEZB3rfYDS2vQ8MSCDYVbuOhIaw6dSixM1JnwPME7GcWkphG61GesLo89t01A3CfAqMkGiVvc1Ful3d67V7YCSZV7NXJkk3M762ixbNvW467fuHtzrcZ7ayctj_ONzgfXtzcJ0iQopbsrQtpxuXN8pqcClcFKOeK2F3t3r4ucdn29YU8Un5TWfQMdC-Z0BHUeND6qbpKImtdV_05BvZHydwv7uRPhCQCbvbrTnEo-0A0vuN7kxtGRJ8WrReUP9QksknwDLpkCeyE6ca_TAqKC_3wkPpKUU0Gw5kWYFJ_8ZPBK_XhPoOkWoGxMLdeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: در مصلای تهران بر پیکر رهبر شهید انقلاب نماز اقامه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/445203" target="_blank">📅 22:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445202">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f80eb42d.mp4?token=P8OxWS3H-JUmV-yrVMWecTii1F9DJVEI2lVrjkwz7Wd9wWuk0XkZf1ZODrQIDxVgJr0P30kPsxJhGRN1dpWLAB7uO9b_mODq31-vYSHy_Ft1uPuRP81jLFpfkeuSXN9ECk6tLyATfOu6vzfGfhFeJy4pxkVZr1wYon4pMceDw3Md3Eed56dKYvCS-kRKcwkFQbkdm-UhvAZDp1WgI0G_BdoGUJy-LT6gHb30p5zu_5olq9nokwBkzFUo0d7DAr2PqsaXZ6P6PvtKHTl0PeSE-tj_k2Rccv3sq8Mf4SBm4xbFHuBcdEVJPgFUlbMoiOhuaYKPsRpZckvCLyg66SaoFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f80eb42d.mp4?token=P8OxWS3H-JUmV-yrVMWecTii1F9DJVEI2lVrjkwz7Wd9wWuk0XkZf1ZODrQIDxVgJr0P30kPsxJhGRN1dpWLAB7uO9b_mODq31-vYSHy_Ft1uPuRP81jLFpfkeuSXN9ECk6tLyATfOu6vzfGfhFeJy4pxkVZr1wYon4pMceDw3Md3Eed56dKYvCS-kRKcwkFQbkdm-UhvAZDp1WgI0G_BdoGUJy-LT6gHb30p5zu_5olq9nokwBkzFUo0d7DAr2PqsaXZ6P6PvtKHTl0PeSE-tj_k2Rccv3sq8Mf4SBm4xbFHuBcdEVJPgFUlbMoiOhuaYKPsRpZckvCLyg66SaoFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم گرگان در شب ۱۱۹ نیز پای عهد خود ایستادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/445202" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445201">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_6-MkFSmMeepAFKV5ro3GAixEZIhC3aGX6sHWRtuGwVv1U9M4RkN9DyanJ9DTVmR0N78B72XYsTADph-8c0MVK7nN5ulyHvetZuFnL42uFVvZGl1lhB87Yx1V-S-WffbwnldxgZpfiGSzVj0QT0hfQOgAKi6RMrJMws4IFUlWpky9McfSMz0WozaYc0vsvbbGa6MjGQkswVy5M4a_eZMnMHaGHmqaXTJ1ZmiofDlH2GsqUlLsDDJmmWyBsIgvgHEYvY2Z8tSu8KbDURIcgTjTVodqMONoxJ08NMvQvTkES4Tga7D9fPO0vIcYV7JlC53mXbhhKa3ugY6TeG3nsvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مس شهربابک به لیگ برتر صعود کرد
🗣
مس شهربابک با برد ۱-۰ نیروی زمینی تهران ۶۱ امتیازی شد و ۳ هفته مانده تا پایان لیگ دسته یک، صعودش به لیگ برتر را قطعی کرد. پیش‌تر نساجی هم به لیگ برتر صعود کرده بود.
@Sportfars</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/445201" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445200">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3980fcb351.mp4?token=cZMOscarAcY16gLWgaPPyKokGgX6jyyomiFk8bqdrm-qbq4ovduzxYYX80nWAm5qVUcyOG2ghIDasTl0PjIFSlAWjQe1EFQ_cIp1X4BsSgHh-a_ebivSpGyCYmNHzdlq0LdC5pAVglRv6sQMB0G30StLrSfQGn-g7KsLKjVuXuPIKC5QJ_yyxp4fVEgLQQ-eB5_SMzEAj_DZxx0f--SI7quvFAtapSTBL9LRwEog2d0B-9xEaK8Zqn5c302kkt6uB4gPjiQKmiO3pHkgZYYY9U9a8bl00-WDobGgXTHeR0XjsFgcltFJeiHT0wT_u4cse_0vz8SqjczfZ7hYFedbVI6xFJ4zf3CvkbyENKtcvNSd7YJNudjS1wd1F7D9SdrJQYbfsbKaMeIzgmJP4uk6RHvbtk82dawrmCUPzq5i3BEorILFj3dhDAxil7gByjD9TBjqksryphIxVFlt8NAITOD7YnhB0I5xT2Y3RZ_JsEkejiuYhCvDG9ZJ81aO8TB-PeFpIr9SMeQ2Xpid5wlzs057hJy3xoG4_e3v8TZkCMvsOLpS-bNKsHKlM8hls6kucU--k8cf6uGsPQvqGL7FLhT0kmxEZw6R3odQzYR09ee2Xuvqso--gJ5HdgY0rGF9uw0nIl3VNTCu4fIiDSWWw9IqjgbRooPY7j5g01n8PXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3980fcb351.mp4?token=cZMOscarAcY16gLWgaPPyKokGgX6jyyomiFk8bqdrm-qbq4ovduzxYYX80nWAm5qVUcyOG2ghIDasTl0PjIFSlAWjQe1EFQ_cIp1X4BsSgHh-a_ebivSpGyCYmNHzdlq0LdC5pAVglRv6sQMB0G30StLrSfQGn-g7KsLKjVuXuPIKC5QJ_yyxp4fVEgLQQ-eB5_SMzEAj_DZxx0f--SI7quvFAtapSTBL9LRwEog2d0B-9xEaK8Zqn5c302kkt6uB4gPjiQKmiO3pHkgZYYY9U9a8bl00-WDobGgXTHeR0XjsFgcltFJeiHT0wT_u4cse_0vz8SqjczfZ7hYFedbVI6xFJ4zf3CvkbyENKtcvNSd7YJNudjS1wd1F7D9SdrJQYbfsbKaMeIzgmJP4uk6RHvbtk82dawrmCUPzq5i3BEorILFj3dhDAxil7gByjD9TBjqksryphIxVFlt8NAITOD7YnhB0I5xT2Y3RZ_JsEkejiuYhCvDG9ZJ81aO8TB-PeFpIr9SMeQ2Xpid5wlzs057hJy3xoG4_e3v8TZkCMvsOLpS-bNKsHKlM8hls6kucU--k8cf6uGsPQvqGL7FLhT0kmxEZw6R3odQzYR09ee2Xuvqso--gJ5HdgY0rGF9uw0nIl3VNTCu4fIiDSWWw9IqjgbRooPY7j5g01n8PXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشف ۵۴ هزار تن گندم و آرد قاچاق در رباط‌کریم
@Farsna</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/445200" target="_blank">📅 22:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445199">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خرید طلای دولتی رکورد زد
🔹
آمارهای شورای جهانی طلا نشان می‌دهد حجم طلای تحت مالکیت نهادهای رسمی اکنون از ۳۶ هزار تن فراتر رفته که بالاترین میزان در ۵۱ سال گذشته است.
🔹
آمارهای بلومبرگ اواخر اردیبهشت نشان داد که برای نخستین‌بار ذخایر طلای بانک‌های مرکزی در جهان از دارایی‌های ذخیره‌ای دلار آمریکا پیشی گرفته است.
🔹
ذخایری که در چین در ۵ ماه نخست امسال ۷۶ درصد از مدت مشابه سال گذشته بوده است؛ نظرسنجی از ۷۴ بانک مرکزی در جهان نشان داده که همچنان قصد خرید دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/445199" target="_blank">📅 22:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445198">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
‌
کیفرخواست پروندهٔ رضا پهلوی و عوامل اینترنشنال و من‌وتو صادر شد
🔹
دادستان تهران: کیفرخواست رضا پهلوی و تعدادی از عوامل شبکه‌های اینترنشنال و من‌وتو به اتهام زمینه‌سازی برای اغتشاشات روزهای ۱۸ و ۱۹ دی‌ماه سال ۱۴۰۴ صادر شده است.
🔹
پرونده ظرف چند روز آینده برای رسیدگی قضایی به دادگاه ارسال خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/445198" target="_blank">📅 22:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445197">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎥
آیین تشییع نمادین شهدای کربلا در پیشوا برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/445197" target="_blank">📅 22:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445196">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌ نتانیاهو: به ارتش اسرائیل بر داشتن آزادی عمل کامل برای دفع هرگونه تهدید در لبنان تاکید کرده‌ام
🔹
ما به اقدامات خود در لبنان علیه هرگونه تهدید فوری ادامه می‌دهیم؛ روز گذشته ۷ تن از نیروهای حزب‌الله را که در خانه‌ای دور از نیروهای ما بودند، هدف قرار دادیم.…</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/445196" target="_blank">📅 21:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445195">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتانیاهو: آمریکا و دولت لبنان با ماندن ما در منطقهٔ امنیتی جنوب لبنان موافقت کرده‌اند
🔹
اسرائیل و لبنان بر سر دو منطقه امنیتی برای راستی‌آزمایی و خلع سلاح حزب الله توافق کردند.
🔹
توافق با لبنان را به لطف ضربات مهلکی که به حزب‌الله وارد کردیم، به سرانجام رساندیم.…</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/445195" target="_blank">📅 21:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445194">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نتانیاهو: آمریکا و دولت لبنان با ماندن ما در منطقهٔ امنیتی جنوب لبنان موافقت کرده‌اند
🔹
اسرائیل و لبنان بر سر دو منطقه امنیتی برای راستی‌آزمایی و خلع سلاح حزب الله توافق کردند.
🔹
توافق با لبنان را به لطف ضربات مهلکی که به حزب‌الله وارد کردیم، به سرانجام رساندیم.
🔹
ما درحال نابودی زیرساخت‌های حزب‌الله در جنوب لبنان هستیم و هنوز کارهای زیادی برای انجام دادن داریم.
🔹
حدود ۹۰ درصد از ذخایر موشکی حزب‌الله را نابود کرده‌ایم.
🔹
ما منطقه الشقیف در جنوب لبنان را تحت کنترل درآورده‌ایم و در آنجا باقی خواهیم ماند.
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/445194" target="_blank">📅 21:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445193">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6393750eb.mp4?token=eTJ0dywsYvph6aWzpP8BPWHyrGzlbdpkCoOk2QILbTWsgLIpO9nc0z3m5DU4QeTmMrCOeft1PZxGNTTVp5Pkb4uBw3HNH_mqAlBCLYW5hxyfYsz01riFmdm0iUmx0W64tCP6ab4RhLf6rCqcqV-eEWtM0xaqzwG35iUsaftcosIyFAOyHl4E2VT1t0K9LFeEQ5iNjTTpWgBZmVsMI0tHLbE7bG2njyAS5JQrvhOEV5Sr431wALO7AFxo6XsbGIGvZq057dQpz8CptvXWBYxGVaM3THMsGcwoqFcxMXuJCHK6ujyACZXUBLFVXMZkKz2UYwlYFU07doFnUaekXzmN9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6393750eb.mp4?token=eTJ0dywsYvph6aWzpP8BPWHyrGzlbdpkCoOk2QILbTWsgLIpO9nc0z3m5DU4QeTmMrCOeft1PZxGNTTVp5Pkb4uBw3HNH_mqAlBCLYW5hxyfYsz01riFmdm0iUmx0W64tCP6ab4RhLf6rCqcqV-eEWtM0xaqzwG35iUsaftcosIyFAOyHl4E2VT1t0K9LFeEQ5iNjTTpWgBZmVsMI0tHLbE7bG2njyAS5JQrvhOEV5Sr431wALO7AFxo6XsbGIGvZq057dQpz8CptvXWBYxGVaM3THMsGcwoqFcxMXuJCHK6ujyACZXUBLFVXMZkKz2UYwlYFU07doFnUaekXzmN9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلدادگان شهدا بر مزار حاج رمضان و سپهبد موسوی گرد هم آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/445193" target="_blank">📅 21:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445192">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
لطفا به این‌هایی که برای اجاره‌خانه برنامه‌ریزی می‌کنند بفرمایید می‌دانید افزایش ۲۵ درصدی یعنی چی؟ واقعا توی تهران خانه‌ای که دو ميليارد رهن بوده با این فرمول می‌شه ۲ میلیارد و پانصد میلیون و مستاجر از کجا باید ۵۰۰ میلیون بیاره؟
🔹
متاسفانه چند وقتی هست در بنیاد شهید عملا واریزی‌های بیمه چه به جانبازان و چه مراکز درمانی و پزشکی قطع شده و مراکز پزشکی و افراد از این امر گلایه‌مند هستند.
🔸
لطفا و خواهشا یک خبرنگار زبده رو پیگیر تهیه گزارش از بابت این شرکت‌های صدور بارنامه باربری کنید.
🔹
گویا برخی از مدارس در یک لیگ دیگه بازی می‌کنند و حرف وزیر رو هم گوش نمی‌دهند. مدرسه علامه‌حلی ۷ ثبت‌نام رو منوط به پرداخت ۲۰ میلیون از شهریه کرده است. لطفا اطلاع‌رسانی کنید برسه به دست وزیر.
🔸
متاسفانه ایران‌ایر از استرداد وجوه بلیط پروازهای کنسل شده خارجی خودداری می‌کند ممنون می‌شم این خبر را کار کنید.
🔹
تو رو خدا یه فکری کنید برای هرمزگان. روزی دو ساعت قطع برق حق ما نیست.
🔸
صدای مردم که به جایی نمیرسه ولی چرا انحصار خودرو داده شده به چند شرکت معلوم‌الحال که جنس بی کیفیتو به هر قیمتی میفروشن به مردم؟ چرا به جای افزایش تعداد مناطق آزاد، واردات خودرو آزاد نمیشه؟
🔹
دو سه روز هست برق شهرستان کوچک مثل عجب‌شیر توی آذربایجان‌شرقی رو بدون اطلاع‌رسانی قطع می‌کنن اونم بعضاً ۲ ساعت بعضی روزها ۴ ساعت. هر زمان که خواستند برق رو می‌برن. لطفاً بگید اطلاع‌رسانی کنن برنامه‌ریزی کنیم.
🔸
با توجه به تعدیل بالای نیروی کار متخصص در شرکت‌های هوایی در این جنگ، این افراد متخصص که سال‌ها بار تحریم و ماندن در کشور با حقوق یک دهم کشورهای همسایه را تحمل و در خدمت این کشور بوده‌اند برای دریافت بیمه بیکاری منتظر تایید و مجوز جهت نیروهای هر شرکت به صورت مجزا هستند این درحالی‌ است که چند ماهی هست درآمدی ندارند و اکنون بیمه درمان هم غیرفعال شده است.
🔹
پیگیر نیروهای شرکتی باشید. چند ساله قراره تبدیل وضعیت کنند. با مدرک فوق لیسانس کارمند شرکتی دانشگاه الزهرا هستم، در مرخصی زایمان هستم و دانشگاه حقوقی پرداخت نمی‌کند، تامین اجتماعی هم که بعد از سه ماه قرار است ماهی ۷ تومان بپردازد! واقعاً شرایط خجالت‌آوری هست. مستاجر هم هستم...  شما را به‌خدا به فکر نیروهای شرکتی باشید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/445192" target="_blank">📅 21:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445191">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شمار شهدا و مجروحان حملات اسرائیل در غزه به ۳۱ نفر رسید
🔹
منابع پزشکی در بیمارستان‌های غزه به شبکهٔ الجزیره گفتند طی حملات هوایی اسرائیل از صبح امروز تا به الان، ۴ نفر شهید و ۲۷ نفر زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/445191" target="_blank">📅 21:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445190">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/108917ce65.mp4?token=dFjFEYPDGeOZErck6Y320FfFcYxcigbOdifyvhBpbXlPSwSpu3DDNk2njPoqDFmlB5OLz__LzsFOWOa9fFYejF9yEycsruVDdbMFyeUXCcUlZt-aGTW6flFn4f9S56J_Vg4uYajQRxFcwkalPPHYF-qlL7ntNQINGHwz6PdFJ4t4VYKDgRydyqm9jNsxkbtUiEdy0ul8OD7YlSipS7dCdGb7w3AkIuJ2ZnzM1h_aLBAsyfvPGim1vPPPawF99nK0OUvaA0ama6ZQHcc5YWVJy0Mx3akOgRq_3Hm32UMDpASPrqE-iMdzLMcPWXN_RqpxinlqpivmI7ttPXsGA6ZPiSo0aYs3dSIpX3e2VuMIDw12xjV-QrDwflzW-t8u88objbLBElVpYGqUPfA7p8_z0oNfsPyFkwAGD4e2pHm_B2cHu1FrK5cB6kR7AOnBlUDXZHDjw62BgXGQtcwPWPPDsE9KtlnuSrJk39fxFUfxC7ASZzXwrwGDTDaAdC1Hj2sqV5ra-3MwFUJSy3Cg7wYSHulZpjOhWnPKi4FFJTfetH60P6Q4_JQ5z2nHM3XYoqakiW3xwIIflUt4Xywu5_u-KKA81GICN1VRpkKhjfAhuta49CEthZF9lmk3Fcyl_KAI9Y93FZ4qI4CADTyaOc-w6Hgj5MvvF1UC49qN2JERk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/108917ce65.mp4?token=dFjFEYPDGeOZErck6Y320FfFcYxcigbOdifyvhBpbXlPSwSpu3DDNk2njPoqDFmlB5OLz__LzsFOWOa9fFYejF9yEycsruVDdbMFyeUXCcUlZt-aGTW6flFn4f9S56J_Vg4uYajQRxFcwkalPPHYF-qlL7ntNQINGHwz6PdFJ4t4VYKDgRydyqm9jNsxkbtUiEdy0ul8OD7YlSipS7dCdGb7w3AkIuJ2ZnzM1h_aLBAsyfvPGim1vPPPawF99nK0OUvaA0ama6ZQHcc5YWVJy0Mx3akOgRq_3Hm32UMDpASPrqE-iMdzLMcPWXN_RqpxinlqpivmI7ttPXsGA6ZPiSo0aYs3dSIpX3e2VuMIDw12xjV-QrDwflzW-t8u88objbLBElVpYGqUPfA7p8_z0oNfsPyFkwAGD4e2pHm_B2cHu1FrK5cB6kR7AOnBlUDXZHDjw62BgXGQtcwPWPPDsE9KtlnuSrJk39fxFUfxC7ASZzXwrwGDTDaAdC1Hj2sqV5ra-3MwFUJSy3Cg7wYSHulZpjOhWnPKi4FFJTfetH60P6Q4_JQ5z2nHM3XYoqakiW3xwIIflUt4Xywu5_u-KKA81GICN1VRpkKhjfAhuta49CEthZF9lmk3Fcyl_KAI9Y93FZ4qI4CADTyaOc-w6Hgj5MvvF1UC49qN2JERk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای حضور تکنسین‌های شرکت برق در یک مقر امنیتی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/445190" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445189">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2e44f614.mp4?token=dkTyuAWHW3OBqIoFJjlG6fERogCngR4Niu6iBRkkfTwboWumQ9CM7afNlvn8QQrbRYxLmYQJ-tz-Pof29IWjM22wYO479Xhf4T2Vv4X5PQui0ax64UayyJRBYBy_um40Mb8NTGpUAGh1t7eDFqsKMrLp7Arnj5eSkcTXCydwYl_IOubJrO-QL0IFGeu6BYQ6E4V863hMPMk8eawQXl98LS1Muy9BxXXG90dE8PGjBpTrVMf4H8jLbG4PucX9P5mmLE35zS7joFz6RFPtU_QdQ8-Ht_apKhpdR1JVv86iM0J8xu7tDCEOmknfq4FFxaagwHR6t916uhLuPNZqFc2y6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2e44f614.mp4?token=dkTyuAWHW3OBqIoFJjlG6fERogCngR4Niu6iBRkkfTwboWumQ9CM7afNlvn8QQrbRYxLmYQJ-tz-Pof29IWjM22wYO479Xhf4T2Vv4X5PQui0ax64UayyJRBYBy_um40Mb8NTGpUAGh1t7eDFqsKMrLp7Arnj5eSkcTXCydwYl_IOubJrO-QL0IFGeu6BYQ6E4V863hMPMk8eawQXl98LS1Muy9BxXXG90dE8PGjBpTrVMf4H8jLbG4PucX9P5mmLE35zS7joFz6RFPtU_QdQ8-Ht_apKhpdR1JVv86iM0J8xu7tDCEOmknfq4FFxaagwHR6t916uhLuPNZqFc2y6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی متفاوت از عزاداری حیدریون زنجان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/445189" target="_blank">📅 21:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445188">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
🔹
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
🔹
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
🔹
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/445188" target="_blank">📅 20:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445187">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0882779176.mp4?token=kzc2yp3Q4Lun2zL5pBeo4Y0xP-JuAXBmn-TWrDln18bUnBkfGEpar568suxyqpEwUjCBGWSjmBeokpn4OeVsppRh9VvO5Y_yK1tFKbhz3LU7hUPa3MJWXAWQOOBL2ziIPVMIaOZwD6xtHLKocyeQEhlXR9CrQRPH3G2_K-xE48Qb7y1J30l9ZCnDhXpDLSL7hqbYTqmuqDWxzBVnv3t4NWhB_ngTxzZNq_AsDHbOhQDJ4VnFGrbZx39x-iJWstkKE5o-abgUfaECvWyuv5cRpyB_GMBmiCT4wMbU2OmF8QgVrBMQS5t-VdSUu8WAwUAx91_AjCgMP1er4dEhq4QfspP6Hs53hAYQGwnFwVU6XljOP1ip-gQoagSHgQPCMvn8unoHNqVaGoDF8QE55LjQKkczbHIEopCipiVR1Ky-iX1t0RvhZeOVwjH2l53jYKxN7rcouDu2s40dTYZKXrPfGW07lHu-1hjlPHjlIEKuTRiH8H5YrfpPSVyZhOfcuwCPXfMRgavhEVi8CBngQN9hGktbcSYMNbcyTzLIIvZEJpxjnLng7oZqA6lJyrCzJLrtL_sZZnDmjjsJNrhnp3i-oz5Qml3Eik54tHtDtM9tNjObBgdz2MgimPnwPRX-MepK8PYRIXc4D9rl7UUr6KmrLTphALqesQnP01X9u8Tpq04" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0882779176.mp4?token=kzc2yp3Q4Lun2zL5pBeo4Y0xP-JuAXBmn-TWrDln18bUnBkfGEpar568suxyqpEwUjCBGWSjmBeokpn4OeVsppRh9VvO5Y_yK1tFKbhz3LU7hUPa3MJWXAWQOOBL2ziIPVMIaOZwD6xtHLKocyeQEhlXR9CrQRPH3G2_K-xE48Qb7y1J30l9ZCnDhXpDLSL7hqbYTqmuqDWxzBVnv3t4NWhB_ngTxzZNq_AsDHbOhQDJ4VnFGrbZx39x-iJWstkKE5o-abgUfaECvWyuv5cRpyB_GMBmiCT4wMbU2OmF8QgVrBMQS5t-VdSUu8WAwUAx91_AjCgMP1er4dEhq4QfspP6Hs53hAYQGwnFwVU6XljOP1ip-gQoagSHgQPCMvn8unoHNqVaGoDF8QE55LjQKkczbHIEopCipiVR1Ky-iX1t0RvhZeOVwjH2l53jYKxN7rcouDu2s40dTYZKXrPfGW07lHu-1hjlPHjlIEKuTRiH8H5YrfpPSVyZhOfcuwCPXfMRgavhEVi8CBngQN9hGktbcSYMNbcyTzLIIvZEJpxjnLng7oZqA6lJyrCzJLrtL_sZZnDmjjsJNrhnp3i-oz5Qml3Eik54tHtDtM9tNjObBgdz2MgimPnwPRX-MepK8PYRIXc4D9rl7UUr6KmrLTphALqesQnP01X9u8Tpq04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش باران سیل‌آسا در مشگین‌شهر اردبیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/445187" target="_blank">📅 20:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445186">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2Ts5NrXWHfMjOrZq0okqDlbveJZKuImpjn46t21CNcT9enimn9L1SZfvgvUETJR2iRAS3gMyooCsyX9hevmxnPeIE9_eqGUW7Z8jh7Nav8FNEhuYCsz7QBQ3ascSb4KRlmwbdEw20uIDxSC-veY1DXezJdRaYagTuUmC-0WdgU38trf13adtR81_IXC9dtNx5PPAmp3Eg4-L2Q5yhb5-9SU1IHtlFfOyMb3NbhLJjjkh7gELA5HvDceHAXzC844QnN1aogCdUaysnqLA2rxBKDsu9p8qLF9UjiCPc0OXgBjYiwhE2y95Ttzec7gRq3W07bTMV3cOrrbZ-lVSPwj5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاندار خراسان‌رضوی: محل خاکسپاری رهبر شهید در حرم رضوی هنوز نهایی نشده است
🔹
به تأکید رهبر شهید انقلاب محل تدفین باید به‌گونه‌ای انتخاب شود که زیارت حرم امام رضا(ع) تحت تأثیر قرار نگیرد. محل تدفین هنوز به‌طور قطعی تعیین نشده و چند گزینه در دست بررسی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445186" target="_blank">📅 20:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445185">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=gMUNvVqKnGo4_tgf7BUSV9Wm4Dhp1XHYveZQSDp0xlT3GwT6Uc6ObWj5O2UXDCz5H3yrr86nqwz_l0dfFo1fzjwn4tYKtEmgcEENbWkmQWIN-7vSJjImukoSTsSJdmjhdtrd8vdsCv9ne79nkPP3uNxfNojlYqEuIorrPDeLrB1jWnI8x2SnraM8XTOHMkI8ev_fxoSTGaQbmEklqzWm0Ih6JJjgFIwxzQUzfrtPQcuuMPKTZXfNUwYn5LitOhY6t8HQp3b0GMf6FqArmxg7C7bay8YudJ-RxrZ8tXFuMY1THjdsXt1CpSMx4xo3q6Lp7-oEPAiRdhMOHNmank8SXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=gMUNvVqKnGo4_tgf7BUSV9Wm4Dhp1XHYveZQSDp0xlT3GwT6Uc6ObWj5O2UXDCz5H3yrr86nqwz_l0dfFo1fzjwn4tYKtEmgcEENbWkmQWIN-7vSJjImukoSTsSJdmjhdtrd8vdsCv9ne79nkPP3uNxfNojlYqEuIorrPDeLrB1jWnI8x2SnraM8XTOHMkI8ev_fxoSTGaQbmEklqzWm0Ih6JJjgFIwxzQUzfrtPQcuuMPKTZXfNUwYn5LitOhY6t8HQp3b0GMf6FqArmxg7C7bay8YudJ-RxrZ8tXFuMY1THjdsXt1CpSMx4xo3q6Lp7-oEPAiRdhMOHNmank8SXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیدپوشی سبلان در نخستین روزهای تابستان
🔹
در ششمین روز از فصل تابستان و در شرایطی که اغلب نقاط کشور دمای بالایی را تجربه می‌کنند، بارش برف قله مرتفع سبلان را در استان اردبیل سفیدپوش کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/445185" target="_blank">📅 20:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445178">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ABbZCRRU29wFda2z7AoTgMTBdabfX1sVtMMmBmCHe4Phrn_N9LRwjUb2slBbrdT2ebgAG6dcHiizOz0B7lwFw2XlAvo_avswJh_smzkNXhTBvPuxSSd2bwJJwuPrvnNeZf4Gs042ceNPiaOjDyuxjHdffG7SE19dg-Rp9BZAsu9VAk69S9omuUqtuRX6kW1sVyn3GBSYelTeAUNZ2lXmI4uQ-zAP4sxD7_cN30GERm_V-913dvKi2wlLuw9sR_R42SL_p_kvfF4dWqFQ-uNMTeitMFZy2aIWr874_FyWdSz5WXxkeobBlbsCaNZlg8mn1hJG4jqO9sDHM_geY8bGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uaBKqkEuxGp4ymJDj8GuGnfDPi-SlGWDJ9mfypWonQXy40NI7mpj_XayxJMmPMnlPggAW3GlFFAqQWqt-CaLiobVz9mPjsLGjjE-L4VuWwGFCa2rf9Qxa0vfubNMCoeKDkgDjwdFV8zArMLHvfXi0FCaUq06jd_h8811DEUX86gHwKYSwxfmExAgEHpd4xOZlvGEECymPy-wMezOoZMKaCV6lxX-u3HF8_tgVeh968MHEDvKNhiVY2iGTuy_sZvu3zWKXGh8jzk3S5B69-qdt22FE0SrD_F_HVtRT0PamtyJkcfKquPyxsmqcHfLsbTgDM3m_hqsInZVw_44K4Jsnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8AQl1pvCeulHrWs2wcbM9uMkb2q-3Zus_lH0ik17cDnpNXV97jLmCwlee7DsTF7AIey0UPigmgGnTefg4lmHYx3rrDrLUlR-XYfWL_sqcx7_mheRieX8fsUvjXuxFoJSOFpTRF9AWMfnnGTEMBvw9jcskG5Ln2jxgwYoa_8C76cKphMDK2eCWuqCUZ7iJO6lt5ImeaZo9CMFGd-xVpG-PSR9PzRjkfxqlqEX-SvV3WOR0b2sV8Q6C_o-bQgSKnvhKxFtvyTd7zMutZaJALlOL23uoxb6_RqL38JAKF-XZS-nPt4Rfl3KTBGHeJhejZdWY5dizggCS6N8dBN9xofeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjmkCpLwOQ2YP2eD2TnlVkdrFN8felZqXv1UfAWjcYdlZks4lZ0vsXQg9-rH9auEdDHq-VfnimRwiy0dks2wJ4cr1CACaFkjbGXdCwUL0LGfhseskcUhupvmyZRLpgubTYxTFtGwdLHJ--qxwN0I5DCDZb5Tgofcp_8KDL5OhBLEoTHNFqyhW-VTeEEIWvxT_0SIJuJVNMezYcC2H7LaQFBix7BvA43QwnKNwZAhJF8hdr15yUnWnxkbsh0GZguWgD1dnTrwlXhbrqVjoQngLTix3ZupXEpvfkSSAuUwirx6CxWtfIfHOTA6FHKPrnQUFaxLERXg7X1xBiG9SpD97w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAdagOoBMyFmfUqlz-NiRKMOJXMBQNGLt1PnSuI-FGzarU8rKX5lkzaje0H7IvBtf8It2RR-4tSAknuoO6DHAUa8PbcfVdcsocLNNJ_a1px9FG2wNbagTvWLZLX2vwl_BbSsUorUmX4JhtxeKPWQnj81xchus2CNWaEcSe6m5axy5cJ6kKc2y37hJ4w5m5YQ17PKZXQAX6jJpPZ7ZqeWat6tCwSeY6mr3hMOOAC18G8g0qUEa4RQiVcF70uIoBRPgniwjMbjQFpc9E81Ot94-1CLERcOdqVW4XTuFWRV2f0LGHzy1jAtS0EbzKgSRYSFnon8YOQncTay9L7dBhy02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQgjMC6WbuEYO9EMg6KBcWJcVdq7kpNCpY0IC_nrCQL5HM3Qufydi_jVBIthnKEAK0_7CTFdyQwOUbx1u5yk3p3JMSvQK3Vs77WqsIxnwIJMztuo_3ywSh6EndfAR4z4Sex6G8pfR6TSt910HNqxDE6YMoU8ft4UpcJWa6YARsKd3JcJqO1F6qFVqV4kZ6EOX1kOI5eSyG2pBjst0_WUlKscxsqso0mBdnTYHyuSU-v8TTSSybmtEufnI1R8E_wJd0g8QrUVGF5eMWCqLlzTqgiDZc8NwI7kYNrwayxxx2Mo4ofWSvG5y0wJhE-anmYiZj_cdBeBUhzUbLctte_5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqAbW5TUIQMO6BR5sEI_mYMsfAIqJW28QuY4loCqZnLgyC_W_4vqCKm6zXv0QkwPBVPg8ocmVUY6v5-mJoA3Ret1wMjyO-rCNRX4V9D_mPa4gZVzpyFcYDFMw0ABsSTe6YSBiKAwqtFpVNIg9C9Ni2wd6xGi7cBaZlKmFCiYeK2bYAkDfUJ9o1sznWa7gKDanEW1csN8PGHKF0GHbQHbha__67bDPpewRahNCLVEd9fY8r92eQhPr9z8NUPGNQNtUNz6fqSt7T7CieycnsL4R49GzwjvIevayx_j8d4pNzoWp5l28M-KFp5eiyhUyxpJH23JKWyVagWQIiw9OQOtRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری سومین روز شهادت سالار شهیدان در بازار تبریز
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/445178" target="_blank">📅 20:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445177">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb474387e.mp4?token=c4sAkmTvrw1qgtv3edrczEk6z1HfxQp1bB_05SZv74fBB0E8q8kXtzAfGWJihT6I7rz74R4wh-qqXsKb9kK5bdcUNTB4oVtA6IBPSQj4_-wU9kRSnz4Z1kcGK2K97eY-vJrizKPhCOBUL0uyov8wxoyGqbeM2fd9sdR20yjVzlY_iYfzORbboLVrJbOemwWmQwnPlfbTwZ_Uqgh_OOvtmfnxEWGbT4vQDDqkf9rbiUCpP78Iyz9VqU3diy8uzqbGJJQlkFBGAqdqOZwEBlzYSnBsrIrYql4QOQQmF-xqudaAHNgtszT9lreK0y-pZ6186rSb8p0PbayI5Ewj9C5ldA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb474387e.mp4?token=c4sAkmTvrw1qgtv3edrczEk6z1HfxQp1bB_05SZv74fBB0E8q8kXtzAfGWJihT6I7rz74R4wh-qqXsKb9kK5bdcUNTB4oVtA6IBPSQj4_-wU9kRSnz4Z1kcGK2K97eY-vJrizKPhCOBUL0uyov8wxoyGqbeM2fd9sdR20yjVzlY_iYfzORbboLVrJbOemwWmQwnPlfbTwZ_Uqgh_OOvtmfnxEWGbT4vQDDqkf9rbiUCpP78Iyz9VqU3diy8uzqbGJJQlkFBGAqdqOZwEBlzYSnBsrIrYql4QOQQmF-xqudaAHNgtszT9lreK0y-pZ6186rSb8p0PbayI5Ewj9C5ldA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عکاس سنگال هم قربانی ویزا شد
🔸
مشکلات ویزا در جام جهانی ۲۰۲۶ این بار عکاس رسمی تیم ملی سنگال را از حضور کنار تیمش محروم کرد.
🔸
«سیدی تالا» به‌دلیل نداشتن ویزای چندبار ورود آمریکا، از همراهی کاروان سنگال بازماند و مسابقه را از اتاق هتل تماشا کرد. او با پوشیدن جلیقۀ رسمی عکاسان فیفا، تصاویر بازی را از روی صفحۀ تلویزیون ثبت کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/445177" target="_blank">📅 20:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fedcf4d0b8.mp4?token=cGb6sSdT4lB5oO6pFShcHUqWzug6KSU8neTRxpfANC5tvSVJgnTXRR-NWkxH-frS0tO5BMcw3_gW67dkTFdYYdYlTvZNATcGmy4lxQa46T_yAD6FS1LnyrDweRQSqvZQt_clchl-OoWD6xiwGqM_71M9zAg6MFPKFwnhROiY-Z_h3UF13ZAa3bT94JGGI4oat1LQb45Kc5c7j-ZedsTtRU-ZQCkgFam21XPopRSE9jPE_Jp-xawtzXXlZs08QuG8pSd068vN1bIpgQegjq019plWDfog_epnf-VLJX1Ec8yhRNWwCwact5WV__StvlEblBfMDpK0ApchlES411hYmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fedcf4d0b8.mp4?token=cGb6sSdT4lB5oO6pFShcHUqWzug6KSU8neTRxpfANC5tvSVJgnTXRR-NWkxH-frS0tO5BMcw3_gW67dkTFdYYdYlTvZNATcGmy4lxQa46T_yAD6FS1LnyrDweRQSqvZQt_clchl-OoWD6xiwGqM_71M9zAg6MFPKFwnhROiY-Z_h3UF13ZAa3bT94JGGI4oat1LQb45Kc5c7j-ZedsTtRU-ZQCkgFam21XPopRSE9jPE_Jp-xawtzXXlZs08QuG8pSd068vN1bIpgQegjq019plWDfog_epnf-VLJX1Ec8yhRNWwCwact5WV__StvlEblBfMDpK0ApchlES411hYmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری دستهٔ «شاه‌حسین‌گویان» مردم چالدران در جوار مقبرهٔ سیدصدرالدین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/445176" target="_blank">📅 20:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445175">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4716d6a5.mp4?token=PY5XvT-KNHrW-AlziW4KW0clNyv6GXbYB-mGcA8usTgLwLqhy9FH8Gyrmx8TqI1MxDadrR3hv8qX2pG0P-mV6VO2HCG4ZBhMOMWtzcflk_ZM4ZrdnHfCv9zG0eqH--dyIeVyj9sYT63D2jzt91udkdvrZtz2OVHgnWi4uVbfeQ_WNSBArZzaaB2RcBKcdjswAnWKeJijw1bsDO9HMOAqRqybNkOPDPKkYziw_gH_XljpLk2QJd-9okhfoYGSQ1lLg6lv_TWGSY3mBVxpunTUVSxXtC5MDycbGPBj57uz7UMp00ZinSshb_uILI_PiihJYI-BuZLRjZhRYdyQzsXILw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4716d6a5.mp4?token=PY5XvT-KNHrW-AlziW4KW0clNyv6GXbYB-mGcA8usTgLwLqhy9FH8Gyrmx8TqI1MxDadrR3hv8qX2pG0P-mV6VO2HCG4ZBhMOMWtzcflk_ZM4ZrdnHfCv9zG0eqH--dyIeVyj9sYT63D2jzt91udkdvrZtz2OVHgnWi4uVbfeQ_WNSBArZzaaB2RcBKcdjswAnWKeJijw1bsDO9HMOAqRqybNkOPDPKkYziw_gH_XljpLk2QJd-9okhfoYGSQ1lLg6lv_TWGSY3mBVxpunTUVSxXtC5MDycbGPBj57uz7UMp00ZinSshb_uILI_PiihJYI-BuZLRjZhRYdyQzsXILw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کپی‌برداری سلطنت‌طلبان از منافقین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/445175" target="_blank">📅 19:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445174">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9hYTUmNCILwlF_127GJRzK5gYMbAgebXCxYfi1uu9fh2-NaBgoGsM6bBDLGFCto23j-EXCK46AoGs7JMJnjwomW4U1Bxvio4UrbUYqMgJLs8v3IZgIywD6n6UysOA9vCxwxXc5qsUc-t0dXU_WoIi_KB6ng6Bh77kNTIbEHTh7aL_VSXhjQf3YP561TQw5eE4AoKM_FjY5ZNeOAPIK_GuAc3eY5FsHIHIHTZwrDLa-GlaZKaAd3AS5v3i58PcIspWDQkUZaVRfKl_in7rB6I3X2uCINuOv7yUkQm148V2BSpKcrqMVA0SHKRWNxPg--55rQM_wtbkTvawzeUFrPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از خون‌های آلوده فرانسوی تا گندم‌های آمریکایی
🔹
شاید بعضی‌ها بپرسند بعد از سال‌ها بخشی از دارایی‌های مسدودشده ما دارد آزاد می‌شود. خب چه اشکالی دارد این پول‌های آزادشده را صرف خرید کالاهای مصرفی موردنیاز مثل گندم کنیم؟ حالا از هر کشوری که فروشنده بود.
🔹
جواب این شبهه را قرآن کریم در ۱۴۰۰ سال قبل بیان فرموده است.
🖼
اما در کدام آیه؟
پاسخ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/445174" target="_blank">📅 19:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445173">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-rl-ROe2R-5mAxfDkILzY9J5ysiFAf5PAIE4krrRYh-1oABRm93dERArUk1wawQgHMrfRqu_DA8Dwrnns14AU7GUV1jeIPb8K8CTsIqpizI1PisQ5waYa4Djryxr2Qe-YQDmkxysfqJOwdEXo83rtHU5hFM1wBGMdFnRYq_OFNCJrtyKBwXOERpVDnDlxqaLkcC_Uv3xXG_KM_-D2Fl4QD9PEKQGR7ylcw6lLUxRI1IG3KZc-kK9IWv2otn4x17_gsDllsW6fyhIuCuj7BT2ZWHQrHRzifBIe9tsQtxmnbFRTNT9vYjSwDa6EOgMkn4sfgxh-tVQlNK6qO9UMPG9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی هیئت‌رئیسهٔ مجلس: صحن علنی پس‌از تشییع پیکر رهبر شهید انقلاب برگزار می‌شود
🔹
گودرزی: در جلسهٔ صبح امروز هیئت‌رئیسه با حضور رئیس و سایر اعضا مقرر شد با توجه به هماهنگی‌های به‌عمل‌آمده و رعایت سایر ملاحظات، هفتهٔ پس‌از تشییع پیکر رهبر شهید انقلاب، مجلس…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/445173" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445171">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/715049e7c6.mp4?token=oh-426XX_eIFriJ7-iARKpdID3OOQGeLyPDMZ3p2k_vrvhrnu_TjMaWQ-NMAx8gdhpkf_a1g2Dq1bpMCLAFLXc1elsGWON8Iqu1tcxR2frGlb_5AjrTIAcTOj_Az77f46MOkAE_X_XA1qPfwteMA9ljUULY9u9vjGBLMQJvzxhdnyYxkqP-FANv-VYg8wVlpLd-8To7ZG0hzbNCkDmcg6Jq9ReJf4qGKmlw0jZBy_r5k0_P4bJbCPInHiGylluZEOue_Rhg9dQa1iYjerbxvjxjUqW8WNgRt4hUhjZeBLD3M1ZoRPCKJDnuV9ndsFucNNPkSTHPpRMTFjbIP98JmpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/715049e7c6.mp4?token=oh-426XX_eIFriJ7-iARKpdID3OOQGeLyPDMZ3p2k_vrvhrnu_TjMaWQ-NMAx8gdhpkf_a1g2Dq1bpMCLAFLXc1elsGWON8Iqu1tcxR2frGlb_5AjrTIAcTOj_Az77f46MOkAE_X_XA1qPfwteMA9ljUULY9u9vjGBLMQJvzxhdnyYxkqP-FANv-VYg8wVlpLd-8To7ZG0hzbNCkDmcg6Jq9ReJf4qGKmlw0jZBy_r5k0_P4bJbCPInHiGylluZEOue_Rhg9dQa1iYjerbxvjxjUqW8WNgRt4hUhjZeBLD3M1ZoRPCKJDnuV9ndsFucNNPkSTHPpRMTFjbIP98JmpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعلام وضعیت اضطراری در ایالت یوتا در آمریکا
🔹
هم‌زمان با وقوع چندین آتش‌سوزی در ایالت‌های غربی آمریکا، مقام‌های ایالت یوتا دستور تخلیۀ بخش‌هایی از این ایالت را صادر کرده‌اند.
🔹
به‌نوشتۀ سی‌بی‌اس، بزرگترین آتش‌سوزی آمریکا درحال گسترش در جنگل‌های خشک‌تر است و آتش‌نشانان در تلاش برای مهار آتش‌سوزی‌های جدید در این ایالت هستند.
🔹
این آتش‌سوزی یکی از ۶ آتش بزرگ در یوتا و در حال حاضر بزرگترین آتش‌سوزی فعال در آمریکاست.
@Fatsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/445171" target="_blank">📅 19:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445170">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شهادت و جراحت ۳ لبنانی در حملات صهیونیست‌ها
🔹
رسانه‌های لبنانی اعلام کردند در حملات هوایی رژیم صهیونیستی به منطقه النبطیه‌ الفوقا‌ یک نفر شهید و ۲ نفر زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/445170" target="_blank">📅 19:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445169">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e0492d90.mp4?token=R781XyEc9l86v_nJf3YznJhwbcYUk5bQYn1Xa6TjAIZVcfGtjYDTGt3_g_ro1nZAwVBhw2dK00z-VtzFLZOqjRCS19gdX3Tq-2HhYe3I7jTlLNweKFO7EslwmZUikobrLjDy7V7MUTsaa-HHDUtPIRjKF_pD_9M65L9dmy5CfHDHrKcInq_RA_pk1z9Peu6RgHSSesScMhuaTwlUZU3qTsP_taCrQrhn9EKk1N_sDHqS119aH5Rys7Q1B8-rqolfc8r7bWErsS6tV1yGnCKN6DsYWU7D0SSKoQX0HG9mzPvDV2ekQ4mAzigrwSP_r7qDVGS-dpu9w_GxYxV4yIguxwAWdC_mURGQ1Z8w1JeuiXu9hJ0LU3TmSh8bguCm7Lel07VSMP2Fmk3-mILKXSkJBwPQFraTXdA3x_KLP-MN8pIZ_TmqsI4paNnh9f41wsQ05c4ynizWSLEhIwimbn5l0FJbnxptMf98GTZW0jjb6K6XA6jSBzS9Dz774FhVUzlBpJTj__wQ0nLUjXLHdoKO3VXdtNGzMyZTr29HZrMCDEsMxBMrI8GgpqPhw4fUFNy4tTuAUnQqmIOgWsy_vO2yByXviYpn-Y0-qUO9HfKIuAQOdZMNqZpkUah-FzhLb3ldUnu1fxQBtafm7IrhrbL6a4_q0D69AhzpWkl7Ih5gDsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e0492d90.mp4?token=R781XyEc9l86v_nJf3YznJhwbcYUk5bQYn1Xa6TjAIZVcfGtjYDTGt3_g_ro1nZAwVBhw2dK00z-VtzFLZOqjRCS19gdX3Tq-2HhYe3I7jTlLNweKFO7EslwmZUikobrLjDy7V7MUTsaa-HHDUtPIRjKF_pD_9M65L9dmy5CfHDHrKcInq_RA_pk1z9Peu6RgHSSesScMhuaTwlUZU3qTsP_taCrQrhn9EKk1N_sDHqS119aH5Rys7Q1B8-rqolfc8r7bWErsS6tV1yGnCKN6DsYWU7D0SSKoQX0HG9mzPvDV2ekQ4mAzigrwSP_r7qDVGS-dpu9w_GxYxV4yIguxwAWdC_mURGQ1Z8w1JeuiXu9hJ0LU3TmSh8bguCm7Lel07VSMP2Fmk3-mILKXSkJBwPQFraTXdA3x_KLP-MN8pIZ_TmqsI4paNnh9f41wsQ05c4ynizWSLEhIwimbn5l0FJbnxptMf98GTZW0jjb6K6XA6jSBzS9Dz774FhVUzlBpJTj__wQ0nLUjXLHdoKO3VXdtNGzMyZTr29HZrMCDEsMxBMrI8GgpqPhw4fUFNy4tTuAUnQqmIOgWsy_vO2yByXviYpn-Y0-qUO9HfKIuAQOdZMNqZpkUah-FzhLb3ldUnu1fxQBtafm7IrhrbL6a4_q0D69AhzpWkl7Ih5gDsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکرار این بازی برای همه وحشتناک است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/445169" target="_blank">📅 19:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445168">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ab4c87b6.mp4?token=fiCWpbZYvV1NMwz29BPr-2ahvBQFqonnhBDdsaHAKvMAdBK9_d6z7R5d8xsD6X3uBlHZ2mrizuB4Yrlkf1D_UliMiiigsJfHwlq9ywsoU96099JMfsaleFp6h593Vp4Uioh9fguEhI6OxH0z9T7PAey1rRynDaBYpWj8ePPhMytWm-7IPu6U3Qkd5tYs3pGbFZIPfP9z1pE0U2hDqs0-a4agn3JWkE6jQIbQ914X-ORpcLM72AstULWkjAMa5JArk2KIltapl-s59ijym2WqY5uMNtm5RQ-rOMZPOYto91jFxU4LEpQ-5nOnlcEi8Qac5A-Kfw3Lvuo8RuIwh8rXxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ab4c87b6.mp4?token=fiCWpbZYvV1NMwz29BPr-2ahvBQFqonnhBDdsaHAKvMAdBK9_d6z7R5d8xsD6X3uBlHZ2mrizuB4Yrlkf1D_UliMiiigsJfHwlq9ywsoU96099JMfsaleFp6h593Vp4Uioh9fguEhI6OxH0z9T7PAey1rRynDaBYpWj8ePPhMytWm-7IPu6U3Qkd5tYs3pGbFZIPfP9z1pE0U2hDqs0-a4agn3JWkE6jQIbQ914X-ORpcLM72AstULWkjAMa5JArk2KIltapl-s59ijym2WqY5uMNtm5RQ-rOMZPOYto91jFxU4LEpQ-5nOnlcEi8Qac5A-Kfw3Lvuo8RuIwh8rXxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستهٔ عزاداری زنجانی‌ها در سوم شهدای کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445168" target="_blank">📅 19:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445167">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dR3ZCoN-NUJm5QslSPKMrcMKlcT9traMqIHx_mRpj09JHVeFWXnZD3yN4Ea1m96f0TpwtH4WXneoSWm8ZwQ33wOF-0VhHtP6PfQkTm3pwerQAm5yIhQlal5sPadvo9NLhcNMkDAkd7qiaqY8TLAGknMLRa_za67gLek2dvZ09vr15cK-Mxs5JBBVUxXFxuvhT0ttm_yQS4vrcb3c2BFdnq50Vv61udYO5fJOz08id7i9LK7Zg7WZs4UkMNwXwrXrotZt8kkpkDMg5T35rd8mo7uHMFtrRaJcDjUHewngaAj41-O1JYlR4AbHqaV0M1icbMJuBYQljXbNQFCC0dm2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بازرسی: گرانی خودرو فقط تقصیر خودروسازان نبود
🔹
بخشی از گرانی‌ها ناشی از افزایش هزینه خدمات دولتی و تصمیمات برخی دستگاه‌های اجرایی بوده است.
🔹
بخش دیگری از افزایش قیمت‌ها نیز به تخلفات برخی خودروسازان و واردکنندگان مربوط می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445167" target="_blank">📅 18:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445166">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjVNFLWTpb0rYo-kd6-1fpKT4T7syTuCZqI_-bipvxZCwwsrQVXsh_VcNdKub14-x6VhlkCT--IBwDn_0mKQ7SfSAiRBv8Wdq1lqTT-RwyM5LBFQ5LP9wXXs3OGNKQgZ1JX144veXLOntrwZAnQAa_jpJK5xC4176Nj128fzDCsMPlreN7WMc3T-I7KzvZ-2xmx4tvnQwkF7dTOhL4vM7jXjr28C9E0ENlcPxouzpA0V881PDl6ftOLaSK5C1lxyq-q121G27saj1sScwX0B090afhxjwa_BBZ7_hiOykeQ57vga-iA8wgpZNH5hkC83McYCvOu5PHw0Tc4-KBRihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمدید ثبت‌نام دوره تربیت پژوهشگر
🔹
ثبت‌نام دورۀ تربیت پژوهشگر معارف انقلاب اسلامی، تا تاریخ ۲۰ تیرماه تمدید شد.
‌
🔹
داوطلبان می‌توانند با مراجعه به پایگاه اطلاع‌رسانی دوران نسبت به شرایط پذیرش، آگاهی کسب نموده و مراحل درخواست ثبت‌نام را تکمیل نمایند.
‌
🔹
برای ثبت‌نام و دریافت اطلاعات بیشتر صفحه فراخوان دوازدهمین دوره تربیت پژوهشگر را در پایگاه اطلاع‌رسانی دوران مطالعه نمایید.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445166" target="_blank">📅 18:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445165">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3fdbb8a67.mp4?token=KnFR4ooOYsI1jJDsxdnWfLfGCMH0z-yNCAMn6QX67HlTorcwMju1ttd6CnMtbmpuG4RlY0m9V0ClktkJdSH9XO-mEB84q1JaWTUGj-geNekH8NLz4fDOScctZMKkZmlUwTflkBt5DA_lghCzz4VU4mvP_WtEX55MLrR0TGXibTnUFA4L9FnS98sXOUoTROYlE3BMKdGZN0yfoMDhtMGgwhUt0-d5kEn63k_i2uI4dltMdYN7lZgHKPfwYsZMMXssO9CxdnS70Z79n8cIgx2qY3eW37phmVRi8cfvtCoSUU4NLFsirjG2v8CdR-14SXNGzMj6t4xOBxZcsijnmeG9SGbtMydiCV5-eauptDNbYOxn86Kt-M12UKVKgb7vMdKzKYT_oRsKAKStYYfXqTij8cNbtcfraOc-vSlaNhYk_4T8sQi71QLYOt5wC2N9mDzzUr3PJu7zxLGAThBbeLNifix1h1fv42tDIfKWY7srjP9bj5ALZ44EJfebSuM1uhwVDuUPqYBKlJK67kzwmJP2bPqBzPk3NsZmXwWQ3GYmPXfSNy0Ql4HhQBiFGHhnU04jCIj30v4TkCaKcH0aeyv27dTeHqWu5GNqGshym4A0azeSVyPZsVHGNH4n5bopAppV3fDW67-c6mARx5si9V7miqZuqkylQkDIVt0Hq20X8EU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3fdbb8a67.mp4?token=KnFR4ooOYsI1jJDsxdnWfLfGCMH0z-yNCAMn6QX67HlTorcwMju1ttd6CnMtbmpuG4RlY0m9V0ClktkJdSH9XO-mEB84q1JaWTUGj-geNekH8NLz4fDOScctZMKkZmlUwTflkBt5DA_lghCzz4VU4mvP_WtEX55MLrR0TGXibTnUFA4L9FnS98sXOUoTROYlE3BMKdGZN0yfoMDhtMGgwhUt0-d5kEn63k_i2uI4dltMdYN7lZgHKPfwYsZMMXssO9CxdnS70Z79n8cIgx2qY3eW37phmVRi8cfvtCoSUU4NLFsirjG2v8CdR-14SXNGzMj6t4xOBxZcsijnmeG9SGbtMydiCV5-eauptDNbYOxn86Kt-M12UKVKgb7vMdKzKYT_oRsKAKStYYfXqTij8cNbtcfraOc-vSlaNhYk_4T8sQi71QLYOt5wC2N9mDzzUr3PJu7zxLGAThBbeLNifix1h1fv42tDIfKWY7srjP9bj5ALZ44EJfebSuM1uhwVDuUPqYBKlJK67kzwmJP2bPqBzPk3NsZmXwWQ3GYmPXfSNy0Ql4HhQBiFGHhnU04jCIj30v4TkCaKcH0aeyv27dTeHqWu5GNqGshym4A0azeSVyPZsVHGNH4n5bopAppV3fDW67-c6mARx5si9V7miqZuqkylQkDIVt0Hq20X8EU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنالتی لحظه آخری ایران مقابل مصر دزدیده شد
🎙
حیدر سلیمانی، کارشناس داوری فارس:
🗣️
صحنه گل را چندین مرتبه دیدم. بله نوک کفش شجاع خلیل‌زاده در آن لحظه در آفساید قرار داشت اما در بازبینی مکرر متوجه شدم پنالتی تیم ملی دیده نشده.
🗣️
در صحنه گل دوم ایران که آفساید اعلام شد باید 2 فاز عقب‌تر از لحظه گل هم مورد بررسی قرار می‌گرفت. در شروع حمله دروازه‌بان مصر و سعید عزت اللهی باهم به هوا پریدند که دست دروازه‌بان به توپ نرسید و دست چپ او با سر عزت الهی برخورد کرد.
🗣️
این صحنه به دلیل لمس بازیکن حریف در محوطه جریمه پنالتی است همان‌طوری که در نیمه نخست داور به دلیل لمس پای مهدی طارمی توسط پای مدافع مصر اعلام پنالتی کرد در این صحنه هم بر اساس همان قوانین باید پنالتی اعلام می‌شد زیرا برای تکنولوژی لمس مهم است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/445165" target="_blank">📅 18:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445164">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هند نفت و گاز بیشتری از ایران می‌خرد
🔹
رویترز: از فروردین ۱۴۰۵ با معافیت ۳۰ روزه آمریکا، هند خرید نفت از ایران را پس از ۷ سال ازسرگرفت.
🔹
سهم ایران از گاز مایع هند از ۱.۶ به ۶.۵ درصد رسید و روزانه ۷۳ هزار بشکه نفت وارد این کشور می‌شود.
🔹
شرکت ملی نفت ایران از طریق کارگزاران و واسطه‌های مستقر در سنگاپور و دبی، با پالایشگاه‌های هندی وارد مذاکره شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/445164" target="_blank">📅 18:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445162">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5010747f8.mp4?token=jsRy1abzOWD3xeBJyH-3sEs7D0BVze2i9vebgCkON5m8rC5h4x4aeiyOKg-MW5RZ8QCcNuvKUZ8SI4nLGII6_r19ahfOoUgRfGTPXLt6SOhIqbiy3ITluNTxTkoY_kBwaAdxDc5ZeFq5FczLMg4SxOPg4i-VYqfCRfy_ABizMs_whH9Z8dCD28z0tlXChME5T9o3QOHBod8iMDlEGww7drYDJNyOdVVJwnRZQTaxCupR-6h0LM8BESG3HZdW4MWC0X_Y6D16-rSL0qt1sIk4jr5WP19OipGoulGHAcWEzSSrEqmrxAhRLw_-u0Tz62Pq5KZXpwL8QvVHgX2INcCOEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5010747f8.mp4?token=jsRy1abzOWD3xeBJyH-3sEs7D0BVze2i9vebgCkON5m8rC5h4x4aeiyOKg-MW5RZ8QCcNuvKUZ8SI4nLGII6_r19ahfOoUgRfGTPXLt6SOhIqbiy3ITluNTxTkoY_kBwaAdxDc5ZeFq5FczLMg4SxOPg4i-VYqfCRfy_ABizMs_whH9Z8dCD28z0tlXChME5T9o3QOHBod8iMDlEGww7drYDJNyOdVVJwnRZQTaxCupR-6h0LM8BESG3HZdW4MWC0X_Y6D16-rSL0qt1sIk4jr5WP19OipGoulGHAcWEzSSrEqmrxAhRLw_-u0Tz62Pq5KZXpwL8QvVHgX2INcCOEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم ایران ما خیلی دوستتان داریم.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445162" target="_blank">📅 18:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445161">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfowSeIDNLc8010E7Y3G7PlP77nj01zKIS8lymw7lnsWuZFSzcnTJoxmnRlQ4NpZuNO_CmRPoJlFM6CIeUeQl5D-b1l4awyLNadZ3SoLYuxSf9MGxBwnT4Qtnwmk421OB7iz1I9ivrl2T1CAW7HR-wNBu-aS62007oR1_HgZT4Djin_XiAKT_P6Lo9R1r0YKSZwHNg6HEJ4s_nIM1cLf6gXNmtjBvBRCoSchsLob4Zw5qSL8UAWmUDLSGc_DMdZ2Ac1OEH2khVSiqnFJ9uOdbR0J5spaB-AhVjAXkHxEHewazPOiEsyI-KZz-DQhhpq4_9NZLMfBaUL6Kpg7EcbQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریب دود ملایم سیگار الکترونیکی را نخورید
🔹
زهرا سرباز حسینی، متخصص طب ایرانی: تصور بی‌ضرر بودن سیگار الکترونیکی به‌دلیل نداشتن احتراق، یک باور اشتباه است و این محصول می‌تواند آسیب‌های جدی به ریه وارد کند.
🔹
ویپ حاوی ترکیبات خطرناکی مانند فرمالدهید، آکرولئین، فلزات سنگین و مواد شیمیایی طعم‌دهنده است که باعث التهاب و تخریب بافت ریه می‌شوند و حتی وابستگی بیشتری ایجاد می‌نند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/445161" target="_blank">📅 18:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445160">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55484b4b76.mp4?token=HHKP2IGe9XzAN4qDSkskiiKe87QX5vKnhI87vfP5f5fkB1Jch3NBfYZbJahaiM2radFFQ7vlKtsi7Y9m5_WFXNAvT2CWkQq9S4N3pIgEjkJZZrHgV5989dgYzjZ26mXlxFgVvp7U28pRH6s_ENFXN0ZAvWFNfyT1IcLSpNna8S7MBjrX6VyU5eLSqVLbbTdPyKypiClbdQUb34XTAXbViq4770CJAHZHF6KNJgeLrboL3-DUR9A0csPaDFR-JMljz3UFZQb5bxMvrRCGhRYwnE-z4NIYfqegCAVdgYRjr643rl_l5-zjdvUjV9HMkfVftQzDFxZBnFoPmULjwzzLokCk2rvUkOaMgzpYpZ1Tzf3_py7Nv4XgsQmrRouoGtWe-8bBenp_p1H5QKHE6I0KA_hVhZ3myjr62yU5m634irh9odbS4NLOchnelxB2yJGhPYOi1iSp0BemhmRZvZn_SvpRDIqmg3yzMa_cs6ZcRz4o2qs9PGQsehG-lejZRPZ4_fiZxqmxR__wBXEYHnYBiqZuzIpuMSZDxv3RRIubrEkR1iliJrE7TSfjKmNlEeKEpdf8g6PksBhBd0pA3YVt7uMUQWU3UtIcChy-VmFvNY-IVUqHG5cgdciIzR0n0Pg2lssGt0uJMxQT2APdNPL6oddkdQppJKdPUc_9JAKmi4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55484b4b76.mp4?token=HHKP2IGe9XzAN4qDSkskiiKe87QX5vKnhI87vfP5f5fkB1Jch3NBfYZbJahaiM2radFFQ7vlKtsi7Y9m5_WFXNAvT2CWkQq9S4N3pIgEjkJZZrHgV5989dgYzjZ26mXlxFgVvp7U28pRH6s_ENFXN0ZAvWFNfyT1IcLSpNna8S7MBjrX6VyU5eLSqVLbbTdPyKypiClbdQUb34XTAXbViq4770CJAHZHF6KNJgeLrboL3-DUR9A0csPaDFR-JMljz3UFZQb5bxMvrRCGhRYwnE-z4NIYfqegCAVdgYRjr643rl_l5-zjdvUjV9HMkfVftQzDFxZBnFoPmULjwzzLokCk2rvUkOaMgzpYpZ1Tzf3_py7Nv4XgsQmrRouoGtWe-8bBenp_p1H5QKHE6I0KA_hVhZ3myjr62yU5m634irh9odbS4NLOchnelxB2yJGhPYOi1iSp0BemhmRZvZn_SvpRDIqmg3yzMa_cs6ZcRz4o2qs9PGQsehG-lejZRPZ4_fiZxqmxR__wBXEYHnYBiqZuzIpuMSZDxv3RRIubrEkR1iliJrE7TSfjKmNlEeKEpdf8g6PksBhBd0pA3YVt7uMUQWU3UtIcChy-VmFvNY-IVUqHG5cgdciIzR0n0Pg2lssGt0uJMxQT2APdNPL6oddkdQppJKdPUc_9JAKmi4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلایلی که نمی‌گذارد تهران صاحب یک ورزشگاه خوب شود!  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/445160" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445159">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e464dc72.mp4?token=Oaoq4cNOwly0M8iKr92xzhY6KkHt0xQEa-GWbOTYE5-KuJMn1pGosUS_NemUKp7p7m6MwDzGPEt1htP7-21vY93_TyLqCXrOfg0pUQVaNOxUo4o6fC5WjGYBMIHQYwIx7mZSjnNr9-VPujOP5_F5HkYOOvZSs0XGcVzNNC_uUjXvoTFURMSeGXUKyB5JVo7aRaG9JBwviaK8H0qSsN9wR3Vcn2xxgVjfpAAxo197PUf-eLn2kXcIdw3vrgykcL1jIfKwjGz0dCg57zQbDVvpDB1stC2Z-WhfIWP-ll3SLEGITC51J0lJ4B1NWvEIBP2FJ_hCl0577ZOlQ60G0vzSWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e464dc72.mp4?token=Oaoq4cNOwly0M8iKr92xzhY6KkHt0xQEa-GWbOTYE5-KuJMn1pGosUS_NemUKp7p7m6MwDzGPEt1htP7-21vY93_TyLqCXrOfg0pUQVaNOxUo4o6fC5WjGYBMIHQYwIx7mZSjnNr9-VPujOP5_F5HkYOOvZSs0XGcVzNNC_uUjXvoTFURMSeGXUKyB5JVo7aRaG9JBwviaK8H0qSsN9wR3Vcn2xxgVjfpAAxo197PUf-eLn2kXcIdw3vrgykcL1jIfKwjGz0dCg57zQbDVvpDB1stC2Z-WhfIWP-ll3SLEGITC51J0lJ4B1NWvEIBP2FJ_hCl0577ZOlQ60G0vzSWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ثبت تصویر سیاه‌گوش در جنگل‌های ارسباران
🔹
سیاه‌گوش، گربه‌سانی وحشی و کمیاب با گوش‌های نوک‌تیز و دسته‌موهای سیاه است که از گونه‌های ارزشمند حیات‌وحش ایران محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/445159" target="_blank">📅 17:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445158">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akLwIz6S2DNJoGvLQu-6QehKt3cRlpareqtG2z7j31SIkX6334k4Gg0Ekk-MhN8WVUkzzMFed1mV21osC5j-6ARcHUmXuIpcF3XxQyPr_BYkv-7l-8woeQmFD4mC2w1d3Fg_W5phoOS1pfEQgeabja-q43Hq0Nh8Obddf01Zkb442-N2uCtQzamRr_3Y3hDVsfMD7TjlsoZoX3nFGIyMQOhpb7SUYXzB9FvzR7j91EcKZqWb8E5PR7lxhTSB0dYhdmK9x1pjznMG4uaI65X2Q91HmwYLOUi-0JfHLVri3iilUZoxoqKzARKBMqs1tl6LxaOJza-6kwqN6KJ1FIddLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
ایران با برآورده‌شدن یکی از این شروط بالا می‌رود:
🔸
بازی الجزایر-اتریش برنده داشته باشد.
🔹
غنا پیروز بازی با کرواسی باشد.
🔸
کنگو مقابل ازبکستان پیروز نشود.  @Sportfars</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/445158" target="_blank">📅 17:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445157">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw1fWQHj3Bf1jA7bpG3Ynjrdy4ZqR43Xt1k1JY5RkmxTVB9kf7iUwE80n7knx3hI4Imz6d74bkzHi9FM0qVJbWOOr_BqoAKSq7lH8nz_oTYDPxXKrfx10YDzkaE3s6H7OYnOze5JSz6sQoJCdzmQqWFW9tfwuUnHLr9aGnYHWKeRH2VifeSUElPKn6lyp5xBRD-XbGJkuWeb0OYqdtAcZvzNjSa_rH5foHirHX1oPPpHwjycadkGo6qSSrKyQRMIAT7xMJDtXnED5HCsw9iws555kwUgBOUNNNWY7ft_HCxbh79kuHfnNqHS3EG3b9w7G8id8gNxhGgn59QhrYN-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا دسترسی خارجی‌ها به ۲ مدل هوش مصنوعی را محدود می‌کند
🔹
رویترز: دولت آمریکا قصد دارد دسترسی کاربران غیرآمریکایی به دو مدل جدید «فیبل ۵» و «میتوس ۵» شرکت آنتروپیک را به دلایل امنیتی مسدود کند.
🔹
این مدل‌ها برای کارهای پیشرفتۀ تولید و تحلیل متن، برنامه‌نویسی…</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/445157" target="_blank">📅 17:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445156">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4c78429d.mp4?token=V80ATrG-tYXEFsMzTmBrc95XlkmvKbWxgpDq7OiW_dtHsA-zVy6jA1tDSnIrljuI4jGRDxpru4to0KdjLGagg6k9m8DPPzDs95tQliY80I3Rq31s79AbrbeOtUy9GNq3YlHmCd7sLyASts2cLVBviU77DWsHrM_pCL8FtNFJ7y6-m-3caw3tc0wkNxpF_2harH4Qc5xwpnjC6w8hdw_rKDyIictqWO3yN_C6Cg_TljSit5NNlWnQyD7apnAmdCGScaNo8oRFyxFpBVaBoBD6Um5wCrYmmLu-VvEqBEKNAw8aYbm-opCYm4GdOEIvsOfShItNXCXdUMlHqKNS8O4O_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4c78429d.mp4?token=V80ATrG-tYXEFsMzTmBrc95XlkmvKbWxgpDq7OiW_dtHsA-zVy6jA1tDSnIrljuI4jGRDxpru4to0KdjLGagg6k9m8DPPzDs95tQliY80I3Rq31s79AbrbeOtUy9GNq3YlHmCd7sLyASts2cLVBviU77DWsHrM_pCL8FtNFJ7y6-m-3caw3tc0wkNxpF_2harH4Qc5xwpnjC6w8hdw_rKDyIictqWO3yN_C6Cg_TljSit5NNlWnQyD7apnAmdCGScaNo8oRFyxFpBVaBoBD6Um5wCrYmmLu-VvEqBEKNAw8aYbm-opCYm4GdOEIvsOfShItNXCXdUMlHqKNS8O4O_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم امام حسین(ع) بر فراز دومین قلۀ بلند جهان
🔹
جمعی از کوهنوردان شیعه پاکستانی همزمان با ایام محرم، در بیس‌کمپ K2، دومین قله مرتفع جهان، مراسم عزاداری حضرت اباعبدالله الحسین(ع) را برگزار کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/445156" target="_blank">📅 17:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445155">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جزئیات معافیت سربازی در قانون جوانی جمعیت اعلام شد
🔹
رئیس کمیسیون حمایت از خانواده و جوانی جمعیت: براساس اعلام نیروهای مسلح افراد اعم از اینکه غایب باشند یا غیرغایب،اگر دارای ۴ فرزند باشند معاف هستند و اگر ۳ فرزند داشته باشند و ۴۰ سال سن داشته باشند معاف هستند،…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445155" target="_blank">📅 17:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riVuy-0zxU_W9i05U1HwCrZCjiT9utcM_pl55rHO7U3Rr9oWjPaWL4niLUJ7621DNYjJMOo262U1dQdtvSGSutV5pWWZaIQH8zpQoCHvzD0ZejpEKf0kIo_SI__yX1krbTKP1H2VdKYmLgQgx0WuM3kyIAaKR88W2_ECRXzro59YzW8_GkdsKK1kq_vBgzY3yTlX11rg-j-Ef16XXi4wCgOdWdqSRDMr7I5YZP3fnZFbbtK3oGadf65CkZ-08Ep_p4ZdlfnnqkLincAhS_Kj2GEBWd_L6_nkK5ukNURMwYNRIzKUsytCrOcnlM9lNmrH81UthBBh4fMzAjESZuAGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WB-K-o6HfslpFG6790a6_H6FoYMJ0o29JGiyKsbwiiJ8F84rQzvWUYI2o5HdcmSphmAajUH9To27QiBa3HixgGK5xCQXYR90ZGxUQ4-Hc5tM77AS-VkOmhaj5l-qrWXiwz6HUzp-2QRxLxA4P7kMkFysy7u0osVzrk07mRi9VGP6aybCy4c4R2FiRuNjnNFEB4fzaxnv2Rvia1AmkGvwMNCwCzbchhEWPg6YVE4MuvpP_gQqwdDtrxO7NBPNPEct-AFk7zngmZjz3Yur3VRLyd651NO5-8oL44E8ihEyoOIucQatGUJm8sMMWMKnWNc6JLZGQAmoWBeNowrHE11JTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDLqWsfW3vlFG_8SDqttdetlIC477OAX45WHYilNpiyi2CDARyw-Bw9qffZR-nw1zMCDqCQEcIRaYfkHCENzzFNUpsL2DOMivI3nV3QTNQpQyFi4Gi3L5n5utXl5trAqYAUW4FbjVjbbLuV5XMxfu4GCR65FQOC5ERuXCIukPMB_NNykJeWkjTf1enlw7daVICN0Lo19iGFpqtSjuRyFuvpQv3zUX_ZL1Wdeqr9SdUy4zdwO5gY8Dnh2cI7DGv3T5qsEZjFyEeeOq-4xVLZF_8l3_dQnLQL9CiQfk0cdB0oW9y8Th-L1puLl96y4Qpjux2ZIR-4Tn61WQnBmOxwYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_wG7gyGOS4i6RVjrNqKVJy2ZdKoKnDVUe4noSR4_eONAuyZnRrTuA-yh1KarDIm2bJJMQEyTRNw6hLdsexgpaZZWweJ8klq4LwSYKiJ-_A-evMk2vHyCMCTe5Q-_B5HEMBoodeqCWTK61iUcojBbOCcHh0kaAf7YhL7MNqqmikbybz8dB58oKcrCb-aar5IIvLMmSkettu5_QI2mjYKMuKLsl_Ys49rDEpnV7-wsHLjVsEY7A8HReljDS1L-IPEtDQurbx9SiNUGpGIFrxn1vafZO7zRpQfXregKUnhmVyyrAycIO3suIsswqwKiCTNRf1GZdld4OtDoS1b61JsAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست سران سه‌قوه به‌میزبانی پزشکیان برگزار شد
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445151" target="_blank">📅 17:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445150">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما با تمام ابزارهای لازم و فشارهای بین‌المللی و عربی پیگیری خواهیم کرد تا دشمن اسرائیلی به بند اول تفاهم‌نامهٔ آمریکا و ایران و عقب‌نشینی از لبنان پایبند شود. @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/445150" target="_blank">📅 16:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445149">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: دشمن باید از خاک لبنان عقب‌نشینی کند، زیرا متجاوز و اشغالگر است. @Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/445149" target="_blank">📅 16:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445148">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: توافق دولت لبنان و اسرائیل، محروم کردن لبنانی‌ها از بازگشت به سرزمینشان است
🔹
دشمن اسرائیلی چه ارتباطی به امور داخلی ما در لبنان دارد؟ هرگونه توافقی باید صرفاً محدود به جنوب رودخانه لیتانی باشد و هیچ ارتباطی به مسائل داخلی لبنان اعم از…</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/445148" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: توافق دولت لبنان با اسرائیل، مایهٔ ذلت، ننگ و واگذاری حاکمیت لبنان است
🔸
این توافق از نظر ما باطل و بی‌اعتبار است و به‌جای آن باید مفاد تفاهم‌نامهٔ ایران و آمریکا اجرا شود.
🔸
تفاهم‌نامهٔ ایران و آمریکا «تمامیت ارضی و حاکمیت لبنان» را تضمین…</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/445147" target="_blank">📅 16:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: سلاح مقاومت هرگز برچیده نخواهد شد و هیچ‌کس حق ندارد لبنانی‌ها را از حق دفاع از خود و سرزمینشان در برابر اشغالگران و قاتلان ملت محروم کند. @Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/445146" target="_blank">📅 16:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: گره‌زدن عقب‌نشینی اسرائیل به خلع سلاح مقاومت در سراسر لبنان، طرحی بسیار خطرناک است که از تمامی خطوط قرمز عبور و لبنان را به بازیچه‌ای در دست دشمن اسرائیلی تبدیل می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/445145" target="_blank">📅 16:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445144">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مجلس اعلای شیعیان لبنان: توافق با اسرائیل اجرا نخواهد شد
🔹
نایب‌رئیس مجلس اعلای شیعیان لبنان: توافق مقدماتی میان دولت لبنان و رژیم صهیونیستی «تسلیم در برابر خواسته‌های اسرائیل» است و راه به جایی نخواهد برد.  مشروط‌کردن عقب‌نشینی کامل اسرائیل به خلع سلاح حزب‌الله…</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/445144" target="_blank">📅 16:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445143">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvYHyCKekjhXRo46kvoLKFDyqpICxZbiWr3Y04uNKQJtD-3ze6WG4ft9j9OzNUYCLla3M4XLv0a9Xsh4TEhq0Sx0GRx8BY-pvg-1HlJGRx4cOYAhY30hz66M2I2gcv_KkBR_QoE5R68iMVKwb2S4po0oFLVvOt-49k4fY8oE7rWQCva35GQWorACoQFTHmw_FJZ8mYX-5sJ4HkKo4u57-78gn4iK6UTFas_tS1zsm37cQ2Vfgx8VQLw9_y05hcSVGLTa1gwhCF6RK9aKlZSrhI98vBJmPyPh1FAepTkE6ZVbA_MSYPM5UY44rwBt6Im8qIGHtIMWuWoF4cxO1kJCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصیحت جولانی به لبنان: اشتباه ما در مذاکره با اسرائیل را تکرار نکنید
🔹
روزنامۀ لبنانی الاخبار نوشت: جولانی رئیس‌جمهور خودخواندۀ سوریه، در دیدار اخیر خود با نخست‌وزیر لبنان به او هشدار داده در مذاکره با اسرائیل «اشتباه سوریه» در دادن امتیاز بدون دریافت تضمین…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445143" target="_blank">📅 16:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445142">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg0hoCr-xN8xMRlBYdPuogMz8JpWHxAqkVd7S9S9Qcp0LOjrpnwjkZCa9xlaNi6qVW6953LIcwJrj3Cw7jVOpaHdHVMmSEdq_9hU4tOqhFbJ9oqj2k_sB7f1hHcaVvAkpqSUFRG0X3nvwWP9gjAaidTXTMkuJi9fNd47nNhLVQPb6o6lSHyGKuLb1mNTuGZBMzQ41NVnMjt1F7k47I4MZSfOyYNDBhtlPeJbPWYyrj-oKFZz5nTtvWgE6g4JeQPIqMMs7rAJDu76nxmBX5MT5mbi4-nLIATTHYBgW4mUgCVyNx0KTJVD_k6OJh_tHRwibJhf2E4DfTAXFSmUZsssVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان ثبت اسناد: اموال وطن‌فروشان با دستور قضایی فوراً توقیف می‌شود
🔹
دادستانی کل کشور دسترسی برخط به سامانه‌های ثبتی دارد و با دستور مقام قضایی، اموال این افراد شناسایی و بلافاصله توقیف می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/445142" target="_blank">📅 16:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445141">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/073ee0c888.mp4?token=E1KDgt42XcvccZUG6EiVQsxT48caiZOnh8hYfd7wT5hHZej31Ze2flnHLkgx-ibjJoByVC4benFugcHzQTRBIQJKr69Fe7Tczxtn31067d9HOO1OqGDulrQndV4NniPi7rG1yKK4dymfPq5-C9yVj5jiVmM5rYHEMSV0N95YP2EBA80krQdCIIJJw6HmhXw4gNVobohKUE_RQARzEUD2OOr6VNt6_MZ1mOIr7oKxYngrSrlj5yGPlJUp6Xsgvdz5JiJxi3GKuO17wCZia_w2xLko66KI2L51WL7kuAX591bh20PizRttZl1G-XQInxwwttSIYvoOpvglyVEKfeZeJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/073ee0c888.mp4?token=E1KDgt42XcvccZUG6EiVQsxT48caiZOnh8hYfd7wT5hHZej31Ze2flnHLkgx-ibjJoByVC4benFugcHzQTRBIQJKr69Fe7Tczxtn31067d9HOO1OqGDulrQndV4NniPi7rG1yKK4dymfPq5-C9yVj5jiVmM5rYHEMSV0N95YP2EBA80krQdCIIJJw6HmhXw4gNVobohKUE_RQARzEUD2OOr6VNt6_MZ1mOIr7oKxYngrSrlj5yGPlJUp6Xsgvdz5JiJxi3GKuO17wCZia_w2xLko66KI2L51WL7kuAX591bh20PizRttZl1G-XQInxwwttSIYvoOpvglyVEKfeZeJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: مدیران پرسپولیس ابر و باد و ماه و فلک و خورشید را دیدند تا این تورنمنت برگزار شود که شاید سهمیه آسیا بگیرند و بعد به چادرملویی باختند که حتی تمرین هم نکرده بود.  @Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/445141" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445140">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ok9qX523OrJb4f5plZ24_DVAYe2w4kuW49KopGPH7p0_AY5xIDF4WgQxqobzv4da_q5hYexIdChxks-QeU7M0lJNi9mbX2YqqGOLbsSRcxqIefxr2XllXvf39AhaNPzl9sSD_oXxsraUMXxxzjUZ9GuNeA06HO4pm4sONFw3kSr3FJUdxUW6tT7wCpm290cfhgQS9kptwKCFE8bUD_oYRfDKIE2QFoAUGAxGAiKOnxsWoQLTrxQxMB63zdlOzKnKk0B4LvDka3FYVYKdo-T0B0vw7potqTKWKU9ONPdeQlxtpivLiVAPJN0RmFURoPKzlmKMMBlBTLfMZXc2rS-pXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از توافق لبنان و رژیم صهیونیستی چه می‌دانیم؟
🔹
توافق اولیه میان لبنان و رژیم صهیونیستی را عملا باید طرحی برای خلع سلاح حزب‌الله و پایان حضور مقاومت در جنوب لبنان توصیف کرد؛ توافقی که حزب‌الله می‌گوید با آن مقابله خواهد کرد.
🔹
لبنان و اسرائیل شامگاه جمعه، پس…</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/445140" target="_blank">📅 16:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a45b79dc9.mp4?token=CUSipGrRJpYEAkuP7vL53Tur13auv9zOebUSWFCrk7BR5pFv6bu2gTZQug6BD-LeGZS8OEQ35RKSMRsdccRgAMFh2y0_TNEmzFNh1fMXYC1JCEu88Nhv8CC0AyldH-1W18bZZxlop2S4dwaSxinszHXuusnhFzOG65FD20eMzqCebEknTPmcsnf2MDAHwjCEWs0XE1rOr9BcNd70Ot4ZaJaFnUn8vTtqwjOwot5t9lxY1x_J5GjsUoPdVsiPai-aXLuEm1hgQb-9PtvDAnf-WEdwjdA6TzuQ5ZhLtgM813emkVnNWGzjng_BoLN7ytdKhaOTmJLUaUH_tPy3U6KfcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a45b79dc9.mp4?token=CUSipGrRJpYEAkuP7vL53Tur13auv9zOebUSWFCrk7BR5pFv6bu2gTZQug6BD-LeGZS8OEQ35RKSMRsdccRgAMFh2y0_TNEmzFNh1fMXYC1JCEu88Nhv8CC0AyldH-1W18bZZxlop2S4dwaSxinszHXuusnhFzOG65FD20eMzqCebEknTPmcsnf2MDAHwjCEWs0XE1rOr9BcNd70Ot4ZaJaFnUn8vTtqwjOwot5t9lxY1x_J5GjsUoPdVsiPai-aXLuEm1hgQb-9PtvDAnf-WEdwjdA6TzuQ5ZhLtgM813emkVnNWGzjng_BoLN7ytdKhaOTmJLUaUH_tPy3U6KfcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مستند ۵ قسمتی فیلسوف جنگ
🔸
درباره زندگی و زمانۀ شهید سپهبد غلامعلی رشید
🔹
از امروز ۶ تیر حدود ساعت ۱۷:۴۵ شبکه یک
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/445139" target="_blank">📅 15:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3yQN4c16KpX1GXEbDOcIHXhbEWQ8u6ogjsmZ_x8z2cgr2aD_94bP5bCJyK9xmbva0ttkoIbxh8JOreo5tTcKvnkjsgFyx08TTovdPVvJuUISaQt31vJ6HbplrdqFFYGpBbTRpJLmF019ke6RO3NxNbZi7TI4EHwL-Jb77sEIV_oc_nqr5NbOkF6sGo8qixuM5LArID1B8fPpLiklzLHObtCIiILq4oYVUh82w3ykd7HtE7Mn0HFi0_tJluNlhHNqohfqGi2jZb_ZHUmYFEJ7fxzcwnEN6KsV5UvpMzHeHDWO5C238V7FAZDaM_6xB-naU3mp71SKLKlLN1cHprGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
سرمایه‌گذاری ویستا در مدریک
🔸
ویستا، هلدینگ سرمایه‌گذاری ایرانسل همسو با استراتژی‌های کلان خود برای ورود مؤثر به بازارهای نوین و با هدف توسعه صنعت بازی‌های دیجیتال ایران، به صورت مستقیم در استودیو بازی‌سازی «مدریک» سرمایه‌گذاری کرد.
🔸
هلدینگ ویستا با این سرمایه‌گذاری، مالک ۱۷ درصد از سهام شرکت مدریک شده است. منابع حاصل از تزریق این سرمایه، صرف توسعه زیرساخت‌های فنی، گسترش تیم‌های تولید، ارتقای پلتفرم‌های انتشار بازی و صادرات محصولات دانش بنیان در مدریک خواهد شد.
🔸
هلدینگ سرمایه‌گذاری ویستا، با تمرکز بر استارتاپ‌ها و شرکت‌های نوآور در حوزه‌های هوش مصنوعی و کلان داده، فین‌تک، سلامت دیجیتال، تجارت الکترونیک، رسانه و سرگرمی، شبکه و زیرساخت و نرم‌افزارهای سازمانی، مأموریت دارد تا زیست‌بوم نوآوری کشور را تقویت کرده و زنجیره ارزش دیجیتال را توسعه دهد.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/445138" target="_blank">📅 15:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgdEcqtBPwLZqq58We7Sk4KQIy1X4Hfl_nGbIi8N9zWhUIqS8I5YB2PYvJfhLC1AzQSlFYdADXQxBjTXy3SdAPh5u1ohC2HAXtdKJi4dr8o8_kLyu4PuExo5oipJQHt-My7QS7VWOZPXktBenqnP-U601-KXcB9xuB2j8swb7xt4FcKIHOT0w5FFdHdCS1bPGtUlhGKiBYnTCljDVdxe4TXqIg9S2gLhpBb3lNk3Zb-rTAiRrFuUyDVubYnAu2oLEM6yngvWzAbVbbX7SASN4HB_OhLiSjRf6Zu6ENxMQc6ckeXOF8MjqLC6IvlNjERIk8nQVkUAyzGf6HkAhh46tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏢
آگهی مزایده املاک مازاد بانک سرمایه در تیر ماه ۱۴۰۵ با شرایط نقدی و اقساطی منتشر شد.
🌐
برای مشاهده جزئیات، لطفا کلیک فرمائید.
#بانک_خوب_سرمایه_است
‌
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/445137" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/445136" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445135">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a7cb7c8f.mov?token=OQeCg4uFsv0u1iq3epzBL0iI0JmrH-VomuMeMHkuYH2HDt4MhSODxCndpbRIIdVAv9V49LXxMg2rA61rM6folNQQFocgMVHhPys0rTSKUofoHmPb1QCGkheiq9J-KLDMp-08VsBI4dIYRzOmyM9z9Erc-JUK4ddZOAdepVWMcnSj8F3im2uQ3PsRYJwD-_esMiM46PNLM7_qKtjXHPZDJ39IMHypLg2_jVS0LjdApE98Bf9kig9oPyBkngCIEI5vfVG78FEosnDVo-4CoWDZ6y_TkOwSEjaEwTpPTmBw_uentuHWPyKwe1C_20pI42F4941UyL7GkB06qlkRD1qY0ZPdVOTW_6RamwLWBXj0D9lLOw8qiUxk_7V-TPChfMQ97Jb9GyTZFkKHBYIuXq3pV6-SO4WuC0TRFNpH0NjRwQEx-k4B1bAm1SzeJAIJKYQFvcK8pyU6GpVmu5w83kYg28oPnxXG67WX5z-4YikJv190ps947W0OX-BJTzYq8OQrXSmdrOCg8ad1yRsk5yqnNEe4wYoF-bYsJD7Bk4JLVgyrCJqmLE3Gs-JOBwJ_XBp1Q1Mfw2tfnFA2j2pOuyMFv1ueruUhz_qMkKfoUcnWIip3abfSmaC3BECHaf53z9sp0r9WAkTcq9hC2VEygKXn90JjrJm9IMe3MrjXndPMpzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a7cb7c8f.mov?token=OQeCg4uFsv0u1iq3epzBL0iI0JmrH-VomuMeMHkuYH2HDt4MhSODxCndpbRIIdVAv9V49LXxMg2rA61rM6folNQQFocgMVHhPys0rTSKUofoHmPb1QCGkheiq9J-KLDMp-08VsBI4dIYRzOmyM9z9Erc-JUK4ddZOAdepVWMcnSj8F3im2uQ3PsRYJwD-_esMiM46PNLM7_qKtjXHPZDJ39IMHypLg2_jVS0LjdApE98Bf9kig9oPyBkngCIEI5vfVG78FEosnDVo-4CoWDZ6y_TkOwSEjaEwTpPTmBw_uentuHWPyKwe1C_20pI42F4941UyL7GkB06qlkRD1qY0ZPdVOTW_6RamwLWBXj0D9lLOw8qiUxk_7V-TPChfMQ97Jb9GyTZFkKHBYIuXq3pV6-SO4WuC0TRFNpH0NjRwQEx-k4B1bAm1SzeJAIJKYQFvcK8pyU6GpVmu5w83kYg28oPnxXG67WX5z-4YikJv190ps947W0OX-BJTzYq8OQrXSmdrOCg8ad1yRsk5yqnNEe4wYoF-bYsJD7Bk4JLVgyrCJqmLE3Gs-JOBwJ_XBp1Q1Mfw2tfnFA2j2pOuyMFv1ueruUhz_qMkKfoUcnWIip3abfSmaC3BECHaf53z9sp0r9WAkTcq9hC2VEygKXn90JjrJm9IMe3MrjXndPMpzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اعضای تیم ملی پس از یک بازی سنگین و بدون انجام استراحت ساعت ۴ صبح روز شنبه به وقت محلی به تیخوانا رسیدند
@Sportfars</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/445135" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445134">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c57c7e4f9.mp4?token=EfjLm2n1Tj9qyqiNRjoCzqNwcg4ngN8XeayrZxqcPVL09aRVFXw5lly54N0Xy6tJ77I0y_ckiAt_CMHgwXK4EMizhRgPtJgOZ6Qc28sBq6T4fPkKAHc-a85dDrTcb1xh4dHRm3NJIM6A3hCZgHBDWewTf0dj1_7wWQRmXOg5I5D5cWb602cM97bqWyMc3NG9l4P8XpYPNFcyZSJLwBAR4CI_zOwLE2HlJ4sBT_lA7io17JK0VHuo3XMTnzmp8BFfbAOUCYXkIz72o4rFhvt0-MAmqoWEVPrrGbIWfoF28ExuOWUe9JkJiw5pnF6CkXvdD8CHjpe031nJbTFS7HB8eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c57c7e4f9.mp4?token=EfjLm2n1Tj9qyqiNRjoCzqNwcg4ngN8XeayrZxqcPVL09aRVFXw5lly54N0Xy6tJ77I0y_ckiAt_CMHgwXK4EMizhRgPtJgOZ6Qc28sBq6T4fPkKAHc-a85dDrTcb1xh4dHRm3NJIM6A3hCZgHBDWewTf0dj1_7wWQRmXOg5I5D5cWb602cM97bqWyMc3NG9l4P8XpYPNFcyZSJLwBAR4CI_zOwLE2HlJ4sBT_lA7io17JK0VHuo3XMTnzmp8BFfbAOUCYXkIz72o4rFhvt0-MAmqoWEVPrrGbIWfoF28ExuOWUe9JkJiw5pnF6CkXvdD8CHjpe031nJbTFS7HB8eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیس با اسکوچیچ بسته است
🔹
مدیرعامل پرسپولیس وعده داده بود که اگر پرسپولیس قهرمان نشود کل حقوق و مزایای ۳ سال گذشته‌اش را پس بدهد. @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/445134" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445133">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrbXy9v5au67zTEAJ-OKTw_gk0Zg7f4m2nl23tQ4UMjQD3bIAmDAzWXXOXBjbBPYkj0bEplEKX8wgLVXohmHxtfWgcFBllhJfqCEeXTZRH6KU1n_A-uSXJx3Np24b_VnMQQWCkMlP_m9RwY2ptoBNuPCSbZe5D-xCCM-RvH-rC5FmUFoJEUtNWXW7_fc0UJbaMMj3EEzGc3_gMpB3MLzI8m7TU_n4sG0EuRUOWV57hPxxrtxp4t8mogz_84oqBkCvAfQW09bGaw4_BgOkXAJ6XMymxYqXtCMfy-zLpMEXgGWV5uRSaNoTlCDdGTrNkkAmM7c1GDHhAlfjv3sKPe3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸ کشور بازی جی‌تی‌ای۶ را ممنوع کردند
🔹
هم‌زمان با آغاز پیش‌فروش بازی GTA ۶، در بخش پرسش‌های متداول صفحهٔ فروشگاه پلی‌استین، فهرست ۸ کشور ممنوعه برای عرضهٔ این بازی منتشر شد.
🔹
تاکنون کشورهای بحرین، چین، کویت، لبنان، عمان، قطر، روسیه و تایوان این بازی را ممنوع اعلام کرده‌اند.
🔸
نسخه‌های قبلی این بازی هم به دلایلی از جمله ترویج خشونت و رفتار مجرمانه، مصرف الکل و موادمخدر، قمار و محتوای جنسی، در تایلند، عربستان، امارات، تاجیکستان، چین، آلمان و استرالیا با محدودیت یا ممنوعیت مواجه شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445133" target="_blank">📅 15:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445132">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7aff68a8c.mp4?token=GK9d6JAPoSGR1Jc51K46-1JRiLB8Tq8WUC8bNaea-xxSmCxdyCZRUfAW44HCEAbYxbwINpL9irspXoIdlPekjPGr5J0tDTJI4crOLFwyKOYroQMWmupHILzQgbdhNMQh9vR8xUhYqwlxGT0DyLAMh1cuM8FuChXmJqAMbD37Qz6xr5DAvg217Q9L-jrCtvUzXzsbswuVDrFPCw3YToMSXsINOtwVFTKMNvbNAelAQCNi6PtANSnwKdtudz9ZMOD8eCdRE9c-mEEkobOcHejn577OajDoRZjpc4WyzGZM7Ox9BjyRLreTJ1b8ns0AntpeGnrpP1JiDJ-0Fmn_tR1YFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7aff68a8c.mp4?token=GK9d6JAPoSGR1Jc51K46-1JRiLB8Tq8WUC8bNaea-xxSmCxdyCZRUfAW44HCEAbYxbwINpL9irspXoIdlPekjPGr5J0tDTJI4crOLFwyKOYroQMWmupHILzQgbdhNMQh9vR8xUhYqwlxGT0DyLAMh1cuM8FuChXmJqAMbD37Qz6xr5DAvg217Q9L-jrCtvUzXzsbswuVDrFPCw3YToMSXsINOtwVFTKMNvbNAelAQCNi6PtANSnwKdtudz9ZMOD8eCdRE9c-mEEkobOcHejn577OajDoRZjpc4WyzGZM7Ox9BjyRLreTJ1b8ns0AntpeGnrpP1JiDJ-0Fmn_tR1YFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از بعدازظهر امروز در نوار شمالی کشور بارش رخ می‌دهد
🔹
در جنوب شرق کشور با افزایش ابرهای همرفتی، شاهد بارش‌های موسمی خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/445132" target="_blank">📅 15:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445131">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVnxoPiJlTJyiMnFNOGKEv0XOMkIDYTjGNGLSoERjALVMHC_H4cuG9CYj0BIHB5ZG6Pt1kwBY24OK8GVFYZxz5MEk-_FJyFOVGme7CE110qHfVUVxbEkmWsWZTy8n-UHRE29lbk_ymOK5UehgIy2bEhWGI4_7jUoB01k2rqOV9lM97DDmMxV5mim0b6jIQ4ya5BxMy64iKsdiJMjTheo-xnSy930d42LWONDMJu0NHudTvCmVv86Cn4w5y2il8VjxmIkZAp4ytQw41V5VgyEuRrzUwdjltWbMBFjoF8ktLZ9beqUe93e0sGdVba9D2WbQbW_GnscU-TxlZV5DQeVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران نگران تکرار تاریخی تبانی در جام جهانی
🔹
۴۴ سال پس از یکی از جنجالی‌ترین اتفاقات تاریخ جام‌های جهانی، بار دیگر نام اتریش و الجزایر کنار هم قرار گرفته است.
🔹
رسوایی خیخون به جام جهانی ۱۹۸۲ اسپانیا بازمی‌گردد؛ جایی که آلمان غربی، اتریش، الجزایر و شیلی در گروه دوم این رقابت‌ها حضور داشتند. الجزایر در نخستین حضور خود در جام جهانی، ابتدا آلمان غربی را با نتیجه ۲ بر یک شکست داد، اما در دومین مسابقه با نتیجه ۲ بر صفر مغلوب اتریش شد. شاگردان محی‌الدین خالف در ادامه با برتری ۳ بر ۲ مقابل شیلی، چهار امتیازی شدند و امیدوار به صعود ماندند.
🔹
اتریش پیش از دیدار پایانی، شیلی را شکست داده بود و با چهار امتیاز مقابل آلمان غربی قرار گرفت. شرایط جدول به شکلی بود که پیروزی یک یا دو گله آلمان، هر دو تیم اروپایی را راهی دور بعد می‌کرد و الجزایر حذف می‌شد. آلمان در دقیقه ۱۰ به گل رسید و پس از آن، دو تیم بدون حملات جدی تنها به حفظ نتیجه پرداختند.
🔹
این نمایش با اعتراض شدید هواداران و رسانه‌ها روبه‌رو شد و آن مسابقه با عنوان «ننگ خیخون» در تاریخ فوتبال ماندگار شد. در پی این اتفاق، فیفا از جام جهانی ۱۹۸۶ به بعد تمامی دیدارهای هفته پایانی مرحله گروهی را به‌صورت همزمان برگزار کرد تا از تکرار چنین سناریوهایی جلوگیری شود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445131" target="_blank">📅 15:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445130">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=ZFFMOxiy0Y1LVbHTL0R1VQtvlATg7xoB5sp4d3diFupO5iHZsPT2SO6t2Yac-04-_pCm5iqk1zMP0FjvQLpLWnkTeQiyaKS0szmS4r0C4qarkOHpduNjuUl-Lp-6nE3YWcgkISTlBXFZg_NApcF8S-SDk5hi9PpTVh_5Py3iht5j-z7acV24yv8W2euZ4kA8lUKQUIuJ8ShqIfg6DJy7QlQL886z8LieIpJQzmGnGMaebkIO-0aFx7g7CnDRbUUdAk9tRwL8Zr95hlYsvhhqCpHbPXPZmZTpR4lRwjuiqpl3ir0Ga8Xr0xL5ah3BUsSOxPYMWd_emO65fsvmNE35yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=ZFFMOxiy0Y1LVbHTL0R1VQtvlATg7xoB5sp4d3diFupO5iHZsPT2SO6t2Yac-04-_pCm5iqk1zMP0FjvQLpLWnkTeQiyaKS0szmS4r0C4qarkOHpduNjuUl-Lp-6nE3YWcgkISTlBXFZg_NApcF8S-SDk5hi9PpTVh_5Py3iht5j-z7acV24yv8W2euZ4kA8lUKQUIuJ8ShqIfg6DJy7QlQL886z8LieIpJQzmGnGMaebkIO-0aFx7g7CnDRbUUdAk9tRwL8Zr95hlYsvhhqCpHbPXPZmZTpR4lRwjuiqpl3ir0Ga8Xr0xL5ah3BUsSOxPYMWd_emO65fsvmNE35yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل پرسپولیس: برخی بازیکنان پرسپولیس باید فردا خودشان قرارداد را فسخ کنند
🔹
کارتال، هاشمیان، گاریدو همه آمدند و رفتند، واقعا کادر فنی‌ها مشکل داشتند؟ نیمی از این تیم مدعی است باید در تیم ملی باشد ولی مدل بازی آن‌ها چه بود؟
🔹
بازیکنی که دنبال کسب‌وکار…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445130" target="_blank">📅 15:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445129">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10cf0269e.mp4?token=AYF6_NG5VxcWvlPLH-_jFFsjDkY4hSvX3sOsjGDh6BfXY4Uruy926ThRH28Z__a9C0yL2S9RgdkqqQj6uyVOsUTb0ev8_trdcAxa2nOiVTZJXwP_gN8n4ARGC4jGos28NQ8hixg5aUMfoNtHnRt6oCD54v0CcTM3oMFbMMaOQ7R2M1ByzGCge60dJ7FN1Dr6_BitQUF7joO7KoYUV0zUv9qC6Vy2O0u230BHcleNVgq7yxQdUatgV9ULD_h4cVfQdIGtvAlt9hLMGyECYnnYN2dEe5o_rDTGxquptrXPaWPHeZ3XxMUMGMEHWHhWF_RT_gg-UFmuRQxTe5wUgXArGAMgaQCUrvzHZNkhWm8_Xbdn1qLEHwTHFUjLZyAoDImja5ePd5MzVKl9au73ZM8aIaB2SFTxVgPc0lsH6QoxkdoY7stT2OVv_zJDL0DTKhquSoNcSMlR-S38cn6wVtBAp6Cg2-2kuOTR_6Fpra-M-ExM6gCifl5Vde7JQ8F0jEMNWbIj5yhyXGufjyhoXX1KD8djT2uPrR-dZzO_GXkwz_wp2ToGw9UfAxzhZiRNP4pdzvMwN4nFFO8mdUZH0a50QM18ic2Ioo7ViyWxs0j_72cFvJwm5OYjuLy3oCW-Nvd29k-8PnoIvMa1Y2X48NmDI1AVG1dlMWtFRV4aNEMy3yo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10cf0269e.mp4?token=AYF6_NG5VxcWvlPLH-_jFFsjDkY4hSvX3sOsjGDh6BfXY4Uruy926ThRH28Z__a9C0yL2S9RgdkqqQj6uyVOsUTb0ev8_trdcAxa2nOiVTZJXwP_gN8n4ARGC4jGos28NQ8hixg5aUMfoNtHnRt6oCD54v0CcTM3oMFbMMaOQ7R2M1ByzGCge60dJ7FN1Dr6_BitQUF7joO7KoYUV0zUv9qC6Vy2O0u230BHcleNVgq7yxQdUatgV9ULD_h4cVfQdIGtvAlt9hLMGyECYnnYN2dEe5o_rDTGxquptrXPaWPHeZ3XxMUMGMEHWHhWF_RT_gg-UFmuRQxTe5wUgXArGAMgaQCUrvzHZNkhWm8_Xbdn1qLEHwTHFUjLZyAoDImja5ePd5MzVKl9au73ZM8aIaB2SFTxVgPc0lsH6QoxkdoY7stT2OVv_zJDL0DTKhquSoNcSMlR-S38cn6wVtBAp6Cg2-2kuOTR_6Fpra-M-ExM6gCifl5Vde7JQ8F0jEMNWbIj5yhyXGufjyhoXX1KD8djT2uPrR-dZzO_GXkwz_wp2ToGw9UfAxzhZiRNP4pdzvMwN4nFFO8mdUZH0a50QM18ic2Ioo7ViyWxs0j_72cFvJwm5OYjuLy3oCW-Nvd29k-8PnoIvMa1Y2X48NmDI1AVG1dlMWtFRV4aNEMy3yo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تثبیت اشغال‌گری در پشت نقاب پایان جنگ
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445129" target="_blank">📅 15:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445128">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
خواسته‌های مردم در صدوهجدهمین شب اقتدار چه بود؟
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445128" target="_blank">📅 15:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445127">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO8bN0-fd0JH3bKmhYi8n4wYhpBgEhtWVoWKaqgNIBrnkR-rGlnA6LGCae8WxYVJLDnjPMsc8FfQH3zQuhLUKXaDkQqYDlFhmyT8-ev_4be96FGjBTAEaeAzjonvv_5KmcDqB9n6OuA-sU9yL-D9iWMPKqDcdWB49thL9WEP8bLkJG1fYWhlPmhYGdcySzHwDCWj_2FVB-I-siGmj3NX_Q96A2Y7kAf4DxFq2bpt0narOSyZeoR3mSfhLDUyhp8XxTvsmO04_ClNpnCNgFssC4JZB4Hfs3rxOVGJMWKFjq6AGM72whzROr6kQFV7o4zi1SHdX6N6pVott6MwKmVoDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سازمان غذا و دارو دربارۀ مکمل ON
🔹
سازمان غذا و دارو اعلام کرد مکمل ورزشی ON هیچ‌گونه مجوزی از این سازمان ندارد.
🔹
این هشدار پس از ثبت شکایتی دربارۀ تقلبی‌بودن این محصول صادر شده و موضوع برای بررسی به مراجع ذی‌ربط ارجاع شده است.
🔸
سازمان غذا و دارو تأکید کرد مکمل‌های ورزشی را فقط از داروخانه‌ها و مراکز مجاز تهیه کنید و برای اطمینان از اصالت آن‌ها، کد رهگیری محصول را در سامانۀ تی‌تک استعلام بگیرید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445127" target="_blank">📅 14:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445126">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4936499a.mp4?token=fMQTbPklm7YG6pJ3pYObTrqznQ30Ddmk2EfPw6j6SkEAQcMhqcfDgNBYL-_KEvfUIFxNIXYtZXtwVkOVY7_AcSo3VI3l4C2b2hBcTmojd0V8mrEUkYmh1OElJY9OOzTojhZZMUVprPcqIqWMmvcswMkTxcqFwQsgesSyPy5iAr4Q-y6nscqivdTkavIrl9iGcMr6mgx12xRdcq1BJvv_Pb6B8BhmMz-HTe0JLT-2HogXcfRcFAb-xLN68wkOPWfgvPgvrWbtbxXaE_wIo-EntydgGifnIL9IqgOoVGlurJKGs1UHS1Ao-Rqpjly8OwcrAA7pBiSJpX0TccgMUL5Hp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4936499a.mp4?token=fMQTbPklm7YG6pJ3pYObTrqznQ30Ddmk2EfPw6j6SkEAQcMhqcfDgNBYL-_KEvfUIFxNIXYtZXtwVkOVY7_AcSo3VI3l4C2b2hBcTmojd0V8mrEUkYmh1OElJY9OOzTojhZZMUVprPcqIqWMmvcswMkTxcqFwQsgesSyPy5iAr4Q-y6nscqivdTkavIrl9iGcMr6mgx12xRdcq1BJvv_Pb6B8BhmMz-HTe0JLT-2HogXcfRcFAb-xLN68wkOPWfgvPgvrWbtbxXaE_wIo-EntydgGifnIL9IqgOoVGlurJKGs1UHS1Ao-Rqpjly8OwcrAA7pBiSJpX0TccgMUL5Hp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با هشدار سپاه تقاضای کشتی‌ها برای تردد در تنگهٔ هرمز افزایش یافت
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445126" target="_blank">📅 14:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445120">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrmuteerMi7AdIojFUoTV1NKs_cbmXLcvJpCjssHOPJNaorMuY7KltFiVNVr33bzsp-byHmLBvw_LQA3sQM1jjq8AQbzpGr7TLBwoR5hNxf9ts-cMqqzN3rZnq_CKkLiTJ1oi3hnMwCCBTpyW7kprOLrMGgfWGSZw0ZLzVt9kEz462dWaJBnZCO2IY2ZCKlrMOJrtZPauaQXhPFsuiTIX_SJ_eXpTfjpwpNj04zw0m4tFYerkpXmY3C0JS0hrTk4I3jfM3DtA6mcqrGkm5QVqgziD9sndy7b5lFs0_2Awr1Qa3ZpUCQpsSCOzpuICMOO1Ojam3tuqI7vTB3fmtLjlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCLXkv9YCz88GlAWHgd8Ttfr-GajtQjZ2i3L5Gju6dOrVTDIP6knixBTXeSJlIBJ9l3iFxPyWsgoVZrM_OoYHAIyFNMujcjda0XexQr8dC6wYP4ABTW-qoLYj10vOsaJgPSoD0GhYSRtFe09T1X6RqowASytLXyDc-60pV9oict1vV_MGTPuS6hfGXUiXWCN3B002aGX2q10UeDMpW1IwKvlNi596IhaB9f7W8eWGS2bKqeHpSUxpKQBkUM6wyoLj2kjlIw2OkPR5q-s6gP3DVjYNFTHUyFmcelb3_bacppqVPj6eeUgLO9L9DeOmmCyl3TL17ofsZYK6Zsnuo-cyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwbQFCPvUoxAO2Rtevynv5i_4Hx-Yskf6VRYvKJ6gsCTaAHrDws72JxRdsfb86NWPBIa-ZP9gC-ONkwbH4TfvcEg9LrJ4fO4l6Gnx3KG9y8wrQRTEbeHC0gJUlLeUUYpx6-UmsMoveH7kwjG_DxfF6QHCssUqX8RM1U8Byn2KOYrQCB1c_ryMVQ9EULQqkcX_LwKC893McHkJPvbt6slTs6-heDeWod8-EUZxyCwmvVqpwI8H0SYCMH4A6XYGmbwg6_wlq0j8Oj3dCTz0m_kgWfiR8h3WILDka6NbC24XmQKo3Yu1nRPM8f0aPK9GFmfxKPptyKA6bud9Z_ArTaxBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P73o7ryUshff7G8WuNzsjHo6I8_CNJ85BrnMC9kluVt7jz7buDw3wB_NcHbftOZYErGUVJ6sk5HlJsa_9U6icnGDPYwR613kXnMhuXdh8r4gL99_pcNSyXfYTQE16t4MuCuJwr0KR4cm6Xan5iFlYeFE4s_R8Un_DQ55Et7k1DBZ6paDm7Sl5yQCgtqi-Lqsm6IjLJWwhsg3IEzrf_k2bSTq8hNaeGi_MEWVdLMTqwbz0Z2UEXx_XvtYo5VszRrTMnRBN-UKSk7qo3Doq7xryM5-vz5vAIFMTyBStkO7y8_lFgHoeRXDvsbHZzcyc0rC8yOEDX74uHbaQt5J9FfqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hI7U-VYzof0JSfvy7q1FdqXYFmFgsGvDAHE8VplLQWxj5Fw3N3Pjsdr3K8mM7hvKuwXQ-9iLapMu94kFIaFca9GH_vs6aS_zi5RYDjZkj9TSckF8oPVKyhDvB3AOj77yYSWlTVT9ZbJm7FLiEhPJCe2IMmI8Vo2wqGyx7-zq1wrwqkPV5PDG1WvXQOWCyhArJ7mvtZdJLDHFIW2SmjrHFk3j8FFioCaDMug5q3dpy8T7Td3cbR1PsXQkW4pv0xWwx_3PO07znpblza5eMJ2m3oIq4l26C6YNsqYm6ZSRF5Cp7W-XbzSP8Fsiv8I_oqVoJcp7KMsyumIgX2LX6mVXXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYUTB1vQ4YtP7x8UABY6ihy8Nlsvas4D2b4trYdVya9C5z9Go-d16xn55DFM0fcuB76W8a5bwPIEe7F0G5WxppI-tFw-HpJueXMUs1-8dhtfrvXXnTeK8DkdQsXTVaeMziOKROOK13kMPPRwkerVuithhE0-EquahzBVjKsVDm1p9FF2njRhNGvreT8TcP6U1sOGJHPhSrCDVzhXSFdPj6ppp1vgP5Ob9TMDai3UgSSxFrE3ZJmngbkyA1TakZ_05xzahJeXAKmL4NvKSgXr7UdAKhorkJy9mnDCPE10L6V2oiZ03xlNuRWlJ5aTFnt_lngA0aFBlx2M8rx_yEGtOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حرکت نمادین طایفهٔ بنی‌اسد در همدان
🔸
طایفهٔ بنی‌اسد یکی از قبایل اطراف کربلا بود که پس از واقعهٔ عاشورا و خروج سپاه عمر بن سعد، با راهنمایی و حضور امام سجاد(ع)، پیکرهای امام حسین(ع) و یارانش را شناسایی و به خاک سپردند.
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445120" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445119">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e4635e5.mp4?token=TMnUvsIA5Y4F4mKzgjMfOa_tkAYBIHXm-Rcc7m_mTWaz1cCYe3qz1qzZFuuVMIrJa_-Wmqq74HQiBwWZPAVoNO1RFh4v8C1qFHYyGyaNKhILd_k7RZScsOg4v6U8WRdHL2f8SP-cNHPlcAbt0IdSc2_MWlXG0R3vZR27pOyTO-IRkXkM1eYj1VI3ewCr36T6b_nDApQK9SnWDQLq64GHv8BcObsSjvfy3vP8dwgrwBEcQnvjUlEfpBU_ZhJN9H9Eio8JWBTdZ_AohYbc1h4oXbfegN82NVbPdn0XETHEXNWMY9OrIo-Vvg9YIDjYj3A1d3i_tSjIrHYN9YoiO0kQyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e4635e5.mp4?token=TMnUvsIA5Y4F4mKzgjMfOa_tkAYBIHXm-Rcc7m_mTWaz1cCYe3qz1qzZFuuVMIrJa_-Wmqq74HQiBwWZPAVoNO1RFh4v8C1qFHYyGyaNKhILd_k7RZScsOg4v6U8WRdHL2f8SP-cNHPlcAbt0IdSc2_MWlXG0R3vZR27pOyTO-IRkXkM1eYj1VI3ewCr36T6b_nDApQK9SnWDQLq64GHv8BcObsSjvfy3vP8dwgrwBEcQnvjUlEfpBU_ZhJN9H9Eio8JWBTdZ_AohYbc1h4oXbfegN82NVbPdn0XETHEXNWMY9OrIo-Vvg9YIDjYj3A1d3i_tSjIrHYN9YoiO0kQyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصری‌ها سلطنت‌طلب‌ها را از میان خود بیرون کردند
🔹
در حاشیۀ دیدار ایران و مصر، تعدادی از حامیان پهلوی با در دست داشتن پرچم‌های اسرائیل تلاش کردند وارد جمع هواداران مصر شدند اما مصری‌ها با سر دادن شعارهای «غزه آزاد» و «فلسطین آزاد» باعث شدند این افراد از میان جمعیت عقب‌نشینی کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445119" target="_blank">📅 14:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445118">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7adc9a29.mp4?token=lRc94IV_cP_HRlIQndqmIDyUunMQ9TGGGKW8UrdWqqpf6v8QpkOosWljmuM6vF5J39Z34Yyyq96d6y_seTNP0as4m2UFjoOVhh9ycuKzGJqr2XKrQgjvZbOYugFn0cgn1ljZ5UZcs6bcU-Jm1zklyK-UVLZ1ABn8Xp4gA8HIJvKTBBiUHO1knH2_CxmSk5W18qvLOXddWoUVdS7cQIFjibAEOxNS9OLyBvQA-hWU_yEvzCDCcxmnxwYqh5v3okWK3K-IUWFq8Z0OJNeOf1fJB7G1Vm-PQ_dBC4Cu8g62_wQ9RRwHUE5-ZKaRKPMlfdOWb3iBWAOgtpBqQo5gFFDJyLbsZaUVn4FDg9YCDorgD019ZKr7H1q2PMYYiff7oUF__ChoDSo31fJnMm2yDf3mkQOUBegAQwErOhRFnNQlqK1okIx0YASBUHeO1eXxg4ovh1xeLb-E2lZPvW9j_DfRKdASWBOpY6GedupQt1kEEZoGbeI52Ekab6PAHhJQATpuI8wOe0pYKqJ3wQlma82OxMDFtU0YHYl3IE0ODD14K9Kx-beBBUJwJseJfNEBLsS30u5NV_WpuT1Bhv6HlOjzU3f4KEN0FiZ2_LVfa7VwCaZggHA6A6B0Vo73RIdLW5p6i91oZ8LWB2ghtO60KIV2w9AW3QnzMJ7PAMFoKoLkhi4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7adc9a29.mp4?token=lRc94IV_cP_HRlIQndqmIDyUunMQ9TGGGKW8UrdWqqpf6v8QpkOosWljmuM6vF5J39Z34Yyyq96d6y_seTNP0as4m2UFjoOVhh9ycuKzGJqr2XKrQgjvZbOYugFn0cgn1ljZ5UZcs6bcU-Jm1zklyK-UVLZ1ABn8Xp4gA8HIJvKTBBiUHO1knH2_CxmSk5W18qvLOXddWoUVdS7cQIFjibAEOxNS9OLyBvQA-hWU_yEvzCDCcxmnxwYqh5v3okWK3K-IUWFq8Z0OJNeOf1fJB7G1Vm-PQ_dBC4Cu8g62_wQ9RRwHUE5-ZKaRKPMlfdOWb3iBWAOgtpBqQo5gFFDJyLbsZaUVn4FDg9YCDorgD019ZKr7H1q2PMYYiff7oUF__ChoDSo31fJnMm2yDf3mkQOUBegAQwErOhRFnNQlqK1okIx0YASBUHeO1eXxg4ovh1xeLb-E2lZPvW9j_DfRKdASWBOpY6GedupQt1kEEZoGbeI52Ekab6PAHhJQATpuI8wOe0pYKqJ3wQlma82OxMDFtU0YHYl3IE0ODD14K9Kx-beBBUJwJseJfNEBLsS30u5NV_WpuT1Bhv6HlOjzU3f4KEN0FiZ2_LVfa7VwCaZggHA6A6B0Vo73RIdLW5p6i91oZ8LWB2ghtO60KIV2w9AW3QnzMJ7PAMFoKoLkhi4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز خوب بودیم اما روز «بردن» نبود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445118" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445117">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
آخرین وضعیت پروندۀ ابربدهکاران بانکی
🔹
سخنگوی قوه‌قضائیه: بر اساس گزارش دادگستری استان تهران دربارۀ ابربدهکاران بانکی، پرونده‌های متعددی در استان تهران در سال‌های اخیر از جمله پروندۀ گروه ایروانی، دبش، رستمی، مولی‌الموحدین، تعاونی وحدت و...  تشکیل و رسیدگی…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/445117" target="_blank">📅 13:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445116">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up9jbxRXzUEVgYe4DYB7pkNXyHmZ5r6ItBY_tQcarw4Hb5RWOm5D7pNTKoa2oOWkYvAN27jUFExr_DQwKx96702Csl6ZN3AD6FXWooivwODIfAzT6mgeoXv1ndZIJVTsdZJ8Wb03o9J5_eNSzZKSZNMxz9qWx__PWNxe7j2kV0oh5AswHz4Y23-zXoSxevuA6rZPrcrsNO4by86fCD6rR41yovgWAzLdvCH7FBI7TLK86dY3hQarZdGKh-0wb_FVU5PXfoxiEytBVPRBKJp4YsHaS33Ce1Ms_x7DVedrk284pWjAYF1hZY8CcK6wMEPoF1IMh6IpkgDtMYj5Zc6ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل ایران به مصر  آفساید اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/445116" target="_blank">📅 13:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445115">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حملهٔ پهپادی به مواضع تروریست‌های ضد ایرانی در شمال عراق
🔹
رویترز به‌نقل از منابع امنیتی گزارش کرد که یک اردوگاه متعلق به کُردهای تجزیه‌طلب ضدایران در شمال اربیل هدف حمله پهپادی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445115" target="_blank">📅 13:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445114">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQoAoHjQuDjX1NsxyfMQCLfovPANXp0nNUZU-3nnh7Nqoe23PK183YFLWDmMEoaAOvYlUZaL4nnR1nhTH4O4KZunoOu4SWpYMXuWeOKCnQGHRAd8kIitDfDhVJkCCQ3Wg-Vbt8UDocuvoHdssqlNYI08tZuYNT32Ox2EtiR9-ZO3kgyK_KL9vtXSRKx4tvDJ0VhksRDRNnEyfvc9fgr3apz9j6Nb0x8zVUFEVD3uWd1sP7bS8npj5UaSgUSVXCgRYt7hsHgLf9LthJoNpX6LAsAOBXEg-pz-BFiOCRM8q9cd6GEL_axseojGie-4pHQRBdINpZ9ErbOZ3wzi39VfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمان بازگشایی مصلای تهران برای وداع با رهبر شهید
🔹
ستاد برگزاری مراسم وداع با رهبر شهید: درهای مصلای تهران از ساعت ۶ روز شنبه برای حضور مردم در مراسم وداع با رهبر شهید بازگشایی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/445114" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445113">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس: گزارشی دربارهٔ وقوع یک حادثه در تنگهٔ هرمز دریافت کرده‌ایم که براساس آن، یک نفت‌کش هدف حمله یک پرتابه قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445113" target="_blank">📅 13:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی در پاسخ به این تجاوز نقاط استقرار ارتش تروریستی آمریکا در منطقه را مورد اصابت قرار داد.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/445112" target="_blank">📅 13:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آزمون‌های امروز و فردای دانشگاه علمی کاربردی لغو شد
🔹
رئیس دانشگاه علمی-کاربردی: در پی اختلال در سامانهٔ ویونا و برای اطمینان کامل از امنیت و سلامت بستر آزمون، برگزاری امتحاناتِ مبتنی بر این سامانه به‌مدت ۲ روز به‌تعویق افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/445111" target="_blank">📅 12:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1418eeae.mp4?token=e9E_eR1FrHuxCStai6qBDpXbUXDxGu95PVzy6P8eiE5jUHmxv5PfxstRgZWWUZnZlFdyRpsG6y6D2lDb9Pfe5-1HLqeuRcWl-F2reEuYJPj5lPOd1ADV_uKGPTrEj-y04Dl7OqwKiTCeGdb1PRXaL7sHpShHfnZmuw58cJNFu-zbU5CN9YUmJ3mFeCAUcMkFr8kjYCBMnN0qqu2DSA8NElY9TryZ1avJUJtDkj_j51kPzDjHlaKLsIsvv6oVxtWz3tg-vNPSZBJQBCoNmEhI4FV6-gQOLdkjZ7twsMOpsSSEOb70-hpaEaFQ3OVqRJZNoO4dvkDO17ivDc7Zyu0Enw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1418eeae.mp4?token=e9E_eR1FrHuxCStai6qBDpXbUXDxGu95PVzy6P8eiE5jUHmxv5PfxstRgZWWUZnZlFdyRpsG6y6D2lDb9Pfe5-1HLqeuRcWl-F2reEuYJPj5lPOd1ADV_uKGPTrEj-y04Dl7OqwKiTCeGdb1PRXaL7sHpShHfnZmuw58cJNFu-zbU5CN9YUmJ3mFeCAUcMkFr8kjYCBMnN0qqu2DSA8NElY9TryZ1avJUJtDkj_j51kPzDjHlaKLsIsvv6oVxtWz3tg-vNPSZBJQBCoNmEhI4FV6-gQOLdkjZ7twsMOpsSSEOb70-hpaEaFQ3OVqRJZNoO4dvkDO17ivDc7Zyu0Enw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احتمال وقوع سیلاب و بارش‌های شدید در ۹ استان کشور
🔹
سازمان مدیریت بحران: استان‌های آذربایجان‌غربی، آذربایجان‌شرقی، اردبیل، گیلان، مازندران، گلستان، سیستان‌وبلوچستان، کرمان و هرمزگان در معرض بارش‌های شدید و خطر سیلاب قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/445110" target="_blank">📅 12:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445109">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i339ZDwxFi0geEgHNvgym9XNKC03_cDr-StVlrSfX2GRA94NUwEbXR_ZT8AgVDSgBX_q5CqKa-fqHuJNxaxiCM_HDCc2XhzRHMNH3UDiDf9sDYu64cRUFxC1w64VUXRzJ9fvfE5Cq-qAcDNxT5xPm9drlYNoQI1c7ypxHclErVKwOGunvOV9uJU1-rZx1Ttv9g8EkMM5Sh-fa0bp6zyVE6TRFpdRwPQKTDjVYMwJ_kU3nP51J7jGBpXD5nFkATVEuOvggxVsfcZ95ETWqI9mpeDwRxUtDjQZN79crxpzoGh8wU1irQFZv3x3mRKJJVpPoyJH2SrSHzXi354x4aWyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۱۵ هزار واحدی به ۵ میلیون و ۱۷۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/445109" target="_blank">📅 12:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445108">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d94bea0d.mp4?token=Qt86pX_ThKlDUQTkOr5ac2_Sh317BFd-4AVpoyP87b3CE6L-OerZqya9D_2j5jxa4Mutv0KvT1s2S8_emMn2CbRyJl2DM9OWWmB-XXudVrGSywcYB-SnPIQfOjmsvoeEanoM0m3Gaclu8EaZUlW0KjEDhuKlIY0IY8b1vjKAkIgnv7NwC0E0JPxNW4IUQOZD5r95WQbu1EPPc7bo4SWb1jzo5jVtaZbdczQBzOY0b63xldwb3_RyaKmQF0ZlfPawTTgDEHOTVu9BnaKan3l3mkugsYR7kjO7IRoceUua4uPqUhOFnebXolf8Mk8DRq0H-0z8LRN3UICwFjrNerZ6IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d94bea0d.mp4?token=Qt86pX_ThKlDUQTkOr5ac2_Sh317BFd-4AVpoyP87b3CE6L-OerZqya9D_2j5jxa4Mutv0KvT1s2S8_emMn2CbRyJl2DM9OWWmB-XXudVrGSywcYB-SnPIQfOjmsvoeEanoM0m3Gaclu8EaZUlW0KjEDhuKlIY0IY8b1vjKAkIgnv7NwC0E0JPxNW4IUQOZD5r95WQbu1EPPc7bo4SWb1jzo5jVtaZbdczQBzOY0b63xldwb3_RyaKmQF0ZlfPawTTgDEHOTVu9BnaKan3l3mkugsYR7kjO7IRoceUua4uPqUhOFnebXolf8Mk8DRq0H-0z8LRN3UICwFjrNerZ6IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا امروز همه سحرخیز بودند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445108" target="_blank">📅 12:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445107">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445107" target="_blank">📅 12:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445106">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حکم بدوی اخراج دانشجوی دانشگاه امیرکبیر به‌دلیل اهانت به پرچم ایران صادر شد
🔹
در پی بررسی پرونده دانشجویان متخلف در تجمعات غیرقانونی دانشگاه امیرکبیر، کمیتهٔ انضباطی این دانشگاه در حکمی بدوی حکم اخراج یکی از دانشجویان را به‌دلیل اهانت به پرچم جمهوری اسلامی ایران از دانشگاه صادر کرد.
🔹
انجمن اسلامی دانشگاه امیرکبیر پیش‌تر در پیامی اعلام کرده بود که «دست‌کم ۶ نفر در ماجرای آتش‌زدن پرچم ایران در اسفند نقش داشته‌اند». براساس اطلاعات به‌دست‌آمده، بررسی پرونده سایر افراد در جلسات آتی کمیتهٔ انضباطی ادامه خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/445106" target="_blank">📅 11:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445105">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cviSMuJe2hJkpekq5wNscOD2UvJSw00NVQoEssXHXQ5IUiwEMCbI_q3gmV3-WXQzmA-6PmLjagXZhOvfkbwf5o_W67zmbjQSHatDg54Pu8lZuNkefb7iOuLIpKCATJVYMuzE1toFiT24MvkGfzjlpVBfmTdy4dZV7sK8pUt5AqrAfvwwKKWx8DnJtzqPkWVKTU7zL_-Yph4NFfj-WLeGo-_iO8hznVO1NBDj4a1pIrryRJ6J91fbaslJdVpabflrsHFeCFWuB18MkxIPm7z01NL-51XnR17RazHasipZrzRwQBvVlj0LSyX1GCPPazFe5V_-mZ1alTTRhI-Dw0FKEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رایگان بودن مترو و اتوبوس در تهران تا ۱۹ تیر تمدید شد
🔹
با تصویب اعضای شورای شهر تهران مترو و اتوبوس تا پایان مراسم تشییع رهبر شهید انقلاب ۱۹ تیر رایگان باقی ماند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/445105" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445104">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsgIN_3Od6VdcH5ewgHgg9d5MycIDIBHvaEhDPtrUK9JrQ_oChQ4foVC-e_JZ_om3xkfJ--tJoh8a6yuW0BtiVdXQqOWM6TfXBn-MLDMcKSuSJLmUpvs0tee2-uw3_mpi_mbC2-Ltm7nGucDhVQEDyZgO9CM9s07Xw1eOQ3EQHsroUyiM6tKw77UQnLBaeBvW-6I0B17smabNy1wfYNohulpNbzW79w8do75yhhf35ctVu-CCIlEtngGAUpBdF6k4eSps9hTCUGskU0QfZKziNityYNnSUnxYWebREuO_doK8TBpX7hKWpnBaD0boUkGAti3wIvZLoGhJ4nkW793fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پاسخ نیروی دریایی سپاه به تجاوز و عهدشکنی آمریکا
🔹
سپاه پاسداران: به‌دنبال نقض آتش‌بس رژیم صهیونیستی در جنوب لبنان، ساعاتی پیش رژیم پیمان‌شکن آمریکا نیز مانند همیشه دست به نقض تعهدات خود زد و به بهانۀ ممانعت از تردد یک کشتی متخلف از مسیر غیرمجاز در تنگۀ…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445104" target="_blank">📅 11:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445103">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph_UZlVRcGCxa6U269kLe-LgUL8ugK5uKtquW6bn-pikFYKoEtCMSwKg2oH7JZ1GVcA8O5jWaEXonjntU1eqYJxnLDkfg3aW1WRmJdvM10wK5os0NCGIkCL6iHXody4ilBba3dLS_81ogGKKYSRpdE9yyac4_6PnhwyfEVFyzdSvQknF_xBDf1xBAwQb2aMqCxEmYov1A5DVj-EZTa4ayo4xYmKgb1lDfBGCjFtUoJAzcj6ovbWmmZHlhcXukbo5uXD5GRIRVFfo5ZiXgWsjqlJFB1i3v4OqwrN0pcV-p7phUYR57wCm0bV_9pduMUT3E4AQcRLQEw4HQ0zQ4gxmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو هیئت‌رئیسۀ مجلس: صحن به زودی بازگشایی می‌شود
🔹
سلیمی، نمایندۀ تهران: با توجه به تغییر شرایط، آن دلیل ابتدایی که موجب می‌شد صحن تعطیل باشد، دیگر منتفی شده و ان‌شاءالله به زودی شاهد بازگشایی صحن خواهیم بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445103" target="_blank">📅 11:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445102">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1wKbI_hT5l21WIb-0PbORVynqktrXmYv4BX6vZaS2yu3J9QRBT0gMhRT8i49s4Tqx45Vjq_mnSeqDFwo9xjLue1NTxtMQ_sNUi0z6F-aeiPTLfq6ZTKPNk_4ohW_mWkiUkj8gezgd8kFVoLbhElhfq4LJPNU09AE6dWNrjPQvBRl-YBuB1xXckOaKjuQirq7lhbfY6NPBm4PH8F_Ex-VwoSM_fi4zBePOBkOl2aUqr1rGtOxQC07_J-6KLHFlGouD_E14NUArWtyQLRcRLO8s0GeFo99atO6Rh36fLUXkMu7DxBxmcMZKY-dgFA4oRwwGdrgWj9V7hUF1jylQGfVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهداری کرمانشاه: از ابتدای ماه محرم ۲۱ هزار و ۶۷۱ زائر از پایانهٔ مرزی خسروی تردد داشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445102" target="_blank">📅 11:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fL4F4mwdq2gmiak-hmIO9R1uxww3pbqhhfRAUVPmIFb6ymfJKeaRESIPEpm2fW97APaUC5SLAmgxggJm6OiOsDAf7BWSdwyh2Otan66viwg2iDZ885LzcTNPk34sX_gLNmK_f-JzVZTQum8j1X2gs_Puk-wVMzjOB7iTD1StkZoUKlaOwAaquVd50sZmH6s_NgRyDsSD0jpq2qVy-66MXwY40aEFPMdzNblgf20JrSpfDbXxAgX4-mPgpYFV_oh0kPduViA8c7zlOqOVYR4bOjq_YO0xmcdY_n827TESqk7YUZW9xVvy6Mv-w4PWbgSs54Lr76N51WWWiXDvnynYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLOC_l0WkL1_5kn-yIFLg-IvKvynuzxSiSOjHSpl4yN1msv2mwm5rmE6IPBouXtAKdBhVwtMlBuILc--YTrlWrqhpbfdk9lNB910dCuRMg-84GyBiQyK_sNXNFtY265PamT8Gbpxh2oN77Sm0_l9X_tilWG5DDJNYhvCFDrsBxet1JBu8qYIbxYrB5m7azcoUnI1_XepTxUagOV7W2P_A5ebyrhwJmyXQuQtE3tJyG0bmHF3s3u-YrGb-Q-ZYN8bdOuFXhBXwG7JejxsMZDpiES-F7yfYSr_ulRHs_v64Pxar19BkDSUkAkhsH2EHFgBjZt-_JFBq_AzcQsQoTx6qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
پرچم یازینب(س) در ورزشگاه سیاتل  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445100" target="_blank">📅 10:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ1DyR2HgkfjEigw40xYwSdwpc_fRlP7Tcu4TEu5HlYMGMOZGUnta6xVWuC5L7j1z_cCLxIjBqLnaJEiz_VuZWG_mlfV9md3hR3SpPEzcmR-eWw3XWbLsf4ybVjXZ6p6pTQc8iWaB5s73fXXMk5zELknHWPZ86r02sHtr3WrB-z6j6QwYD8jrhswsUY-Dz5OIabSiLk0u8LuFbwkR1wZVJ44JpDrL1aW3VlXKRYuqVMz5ZSKQ-15BGPL18fsWaeVwN7Nz2i0q-fCqSAnvoAsw4EljBsjCcpq9YAZhn7RlsUGSfD7_YTu1qO86bSFFA2E3acw1ELtcIplZMc9Abd1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز آمار: تورم نقطه‌به‌نقطهٔ خانوارهای کشور از خرداد پارسال تا خرداد امسال ۸۸.۶ درصد بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445099" target="_blank">📅 10:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=AVX4CiyYjBaHIr9N8GGEoUmEDo1CBJxJxks7ThAJzaCZTWLSlXxuLaeE0J6i7BIl0LUkjqCmg-hVXAJ8iPskOjE87Zku2xtaE4IjkE4QprZ-6vE1zhAvbv8csGfFx1-x5tP1oECKskr73fM74raBhq0Nvqy9JnItA4HB2Pqec_RfuBkany3IVuXzF2NnfEbwLCocc-UjP85di_jL0TnyiX0YIXg5HzWyCx6aqksXGMMJOdz1ZjMf2jx8ZbpMQc3zbNe8bIkdQ4Nxzh6c26h45u39y3f4VEUp8wJpVGifLL47yeb7AEekhblcx0dZKaV9BSVl8jn5JSnxRNbkTImeTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=AVX4CiyYjBaHIr9N8GGEoUmEDo1CBJxJxks7ThAJzaCZTWLSlXxuLaeE0J6i7BIl0LUkjqCmg-hVXAJ8iPskOjE87Zku2xtaE4IjkE4QprZ-6vE1zhAvbv8csGfFx1-x5tP1oECKskr73fM74raBhq0Nvqy9JnItA4HB2Pqec_RfuBkany3IVuXzF2NnfEbwLCocc-UjP85di_jL0TnyiX0YIXg5HzWyCx6aqksXGMMJOdz1ZjMf2jx8ZbpMQc3zbNe8bIkdQ4Nxzh6c26h45u39y3f4VEUp8wJpVGifLL47yeb7AEekhblcx0dZKaV9BSVl8jn5JSnxRNbkTImeTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمار کشته‌های زلزلهٔ ونزوئلا از ۹۰۰ نفر گذشت و ۵۰ هزار نفر همچنان مفقودند
🔹
عملیات جست‌وجو و امداد در ونزوئلا چند روز پس‌از وقوع ۲ زمین‌لرزهٔ ویرانگر همچنان ادامه دارد و کمبود امکانات و تجهیزات سنگین، جان صدها گرفتار زیر آوار و هزاران مفقودشده را تهدید می‌کند.…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445098" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a605d47d03.mp4?token=nyQN6aqIeJuBcT_8LBCjPl_Ku4uLh6HfMWwYHIDCTMEQWtKNofwp8oRBSaS6nxE4-ZpZf_WLVq6dj9viieYTFwNFQ00KvwQCk56vjlKoC83fLVpEKCrULFfka_HSI41I0FSrqNMtvV79h86p2Q0Zd6ww8uoS5ZvmftUykhp87uATkBpTm40epOIPKGDljBHK3cytZkx9IK2axvLeSLl6SsH_n7RgyDZL8f4Nc3CFEPIxiTfyOWrfINpigiMPvcTFQnYChzVMfwPadzXai1Vq-LrOKCZdC4jI0a5xO3qlcXCHV5RTGPrb-Iot5KdR50nKDtpb8gfXtosJuEdxZerQew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a605d47d03.mp4?token=nyQN6aqIeJuBcT_8LBCjPl_Ku4uLh6HfMWwYHIDCTMEQWtKNofwp8oRBSaS6nxE4-ZpZf_WLVq6dj9viieYTFwNFQ00KvwQCk56vjlKoC83fLVpEKCrULFfka_HSI41I0FSrqNMtvV79h86p2Q0Zd6ww8uoS5ZvmftUykhp87uATkBpTm40epOIPKGDljBHK3cytZkx9IK2axvLeSLl6SsH_n7RgyDZL8f4Nc3CFEPIxiTfyOWrfINpigiMPvcTFQnYChzVMfwPadzXai1Vq-LrOKCZdC4jI0a5xO3qlcXCHV5RTGPrb-Iot5KdR50nKDtpb8gfXtosJuEdxZerQew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای در منزل شهید لاریجانی: کسی غیر از خدا نمی‌توانست مزد تلاش‌ها و رنج‌های ایشان را بدهد؛ شهید لاریجانی سرمایه‌ای بود که یک ایران او را از دست داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445097" target="_blank">📅 10:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzrJvw8M7rIFj0krRK59uHqrhtU8U0NWAqseAz8swfPW-AGoBCIpQHlayxuWgCgfcryNBqW-_2q89ply4ki97TUAo3ecHzE-gBbSFY8QitfpdQYFAj-P8V6QyQUWC8hXnQv7mkbHOxyWJsyXjq8JbYgtXlfg3r6kYkO8nIMvjS9gEwZqb7PvRDRwxJAMkT7gmqwhCrkpheJRxM-Ium_fRhUZSzlhXHGQ-PZuBrZGkMANPQxHjd-fd8PBEnwsDzyJsNvkMnhfi0r17CyqvXKt3p1Z1lu5XaQgcPAXwRM4ycucRz2LFoJ1ASnR830h0vkTdj8-H6ry7ln7IWXIQwtFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFJRR3SAkPREkGK2q1bg5GEZnBEFfBejpXhkg3oLw2b0bLbfxogn117b8x-jV94XXIRKtUJUxtRgK1_MPfZr4ZFka1RCUut678bJWxRpw2_qCj_2skHnhUJlPAZrXYUYvq6TFM9hv1J5j0JsRV65gVkEtuhqt_A6tqnNflnOITNoARrBQ-fcmBB6ufVBNNkeB8U8MgDxFQwhBhYVkRbPo6rLRT8MUObsZgGvnkYkhwbvPLvEch3_TtCxpmKDogTaBh8AG6V5FSteTRVtUsw2I7IXA5PqUfVKKJWnf0kautLV-NX8BptuGbC314fQSMPIxDMfoKRvMsD6x7HjaGJNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jN2JFUhh2A9Cmyn-hkQF_Zx8rmz-9EbfuVmYOeSi9t4sRlsimH2MKh6-sr1RM_XUoEw5hv8opn-cSkou5CqN0uwgspL7nJxz6ct6prdg4Xj4DgRDTs7IAyjOTHhByZrbs6t3QcMfhJXCL2J7Gp8aZ0zJX7b6WHCM0ioJuDJ3SrGFHDzbaIsvZ6ibuOroyu1KugOOam3ZRUEaQ8vw9OKZ_dU9v5WEi_aPt1aBz-1MtcQMpyc79hhPXPljIInmvhGHdp7CqbDgW91xlTgy4HjxtOdRbvZHDwE5r45ZOfcrddPfc59vxNpZ9zTU1bLYQ-Bl4eBFySIVs89k1QnDhFKTYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V04nykkLsjvlQa6dV02NvfYEuQiHRxHSAAsnnFhu7UFkKsGgpB24RnWkOQqVTtJ6SdLk_wOXQOPdtD-1an7izn2eKqNvakdKs8STHJZDqqnCq7CExe6nGkf3O34hfz-xTj7YUa2chRXo5p_gcP44qCeJkLdRyJG-QMHqZ7a_rJNRRSQuB6rB96zD7GOKH5mKIhzkkCJZTEduYoD-uq2j48CTvSbyL_GaFKUp7N2ImTaaY-2nRchDT_AOTajBcJ4PXHVfQ_jcxqJoCSuo6BXhJTIKOKZ-I7O0UROHjF5mbRrv6u9GmPE6TpiWS1VdI0BMZOJ2Dl2S92ugfnjuQJbnKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
تلفات زلزله‌های ونزوئلا به ۵۹۸ نفر رسید
🔹
دلسی رودریگز، رئیس‌جمهور موقت اعلام کرد که درپی وقوع ۲ زمین‌لرزه پیاپی در این کشور، دست‌کم ۵۸۹ نفر جان باخته و ۲ هزار و ۹۸۰ نفر دیگر زخمی شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/445093" target="_blank">📅 10:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445086">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uo8flduF0ntuaXeiyP4LjbIzLMHl1McM-zfu3MqZsIzn54nm2cfmtei7_ONai5LBN1Cx6y7UBcIzL898oiM9u8lBSv0R_ceUj3_xD_k5Ait2mepEVCaKeSBqcQoVSGaFHwUyr5G81l8jbobdKR9jt7rAeVKj4uOVIeP1J0MyoHnJTQkY5_HPrV4P9HClryUvy-adI4EjiPPYVMzRDu_QwqIgd_CYFmQziypeFIQHKzJ4pVETGQnBPfv-raJMxDCT8zuti2S8ZmTP6j7SO34xreAv-yVj4gXlzhzreAA0VkCfW4qNU3qPSCusAsI_2eiRfPzAOSPyMMHGfqACsL9_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMGugm50WshpBlH8aBdlHSDMsO6eFsR1buG43qGkwldO44wve78eIYGTbeokM8HpmtfIWDS-j-88h5foTTJvpRqzDVOY9UGQHULl6f9yID8Rgge8-vGvoMLODG8X0TuKAW8hNc3ejL7JstntFnF9v8Az5ptt5xqFbEI0dQ3sX9AIpKLTtRqvs5axLrPdNa2zzWteDsq3t9sUwDtOBKXVH3Z2q1hGy2vbF8WV0yJaIR7pzrCPb-LLJfUF49VEHPegFrF9qX4hxGKOjvcFRnFD9D9ch6_tjJ7aIwTw3yybyFjAC9AxtuLvWj6_1pXx9RQZdDZTfTxUZfeo9tgn_Z-n5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AalIDxm9iRjJKJflfzLSkIEk8j7aZjQulU8hP_8viLdSO5-T81KMJgDC_gFjMdMLHFBGW59LFFfTB77jyBt25jz1wkTT23sQMh-sHEMjQ-N3twodDhu0sdprGWSj3na9euI5o1sOeaFxdqXwkpxMpZ37LOkyX3ii96AGqpzQCYcYU4x0Sr2mA_ZZQvm0XF9SsLkQf_0Jt_8KY4K3spf32CKIiiAdwXo0LSG3p-svmLUYlQ-V9PgDEPJsQj_y2BBcUpT33DkpS2VtxsZTXjDi3Y8d80W3f4bXQs8Zji8O3cDqwueDeup4l-Qpecewt0Crbh23T5dZUmFW5ZaldhPVrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQ-qV5-kMJIAkWTNmNKaKNmQvquBu4--4EUQUk_ldlEjncDfi76i-H9gPCXLdFY62fAl98uUlV4sa_erM57gUX6z7X_gjTQaajB0MoN0W4-ZA7Wr47RD_NanZdm7J6SgyBuOajwOKVl-KKQx27gy_Y_WiqRAxKafplhUndsNTVS-cIFXpCI_9p82a7x7jSW0xXqvNUYP_94EUw-MeLbIZAACsuX8KHDeHO881qFtG9kROynpQ2w7BVX3Zv26RRvSDGw6KvevFEN7Vn5kO7qwWYKwrvNbZ_ivApX1IA3mvPk3Ub5Dn1pVd5qC5bKRlyNLA_SGY97Ewnyg4kreM80T1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOieb67SSDzT1i7ZeeUarnCwa4u_5uwWeqwDSaJAnrMlDgr69iOs9BwbPQW5-5QC5vsXs3xfsrTyR1ynACB00ZQ2Zhr_sy34K0IIcQFUcOamqUGH-Oj0KHEdx33ddIHrtpBDTID3iWM6qjHyBV3Xl077RrM60_3-hLt1C7iNhkf8ijMXeNR6mEAEOOer0S_5zLYBbBSqLAAOxCPVMV1Yk4hTdBvTI1gTQoFB2kwchaY59t03zDsUcZjJ_HkHlWvmBE6jpo-P8gYN0YyiSZGW0FC5_QZCJR5b1QBdFY1ZO3WDastagsaOQdHZyFRHbePugXipDWaBwAxHKSFZqbjYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7oEBCzpLgrkctbfel_-sp7q7_f7LDRi9i_wN7RlAW1srWM1DYyY3baYvmfazqYhNE1-o20zgXDAmF0zm1ItIMzvool1lG6kZ2GZ3aawyDr-EkLYDbClEM7lF6QZJun3EWFE1sTIZzijKxUzw4dhWCKEG19J8RRMNZHWjU6uQkjphBcd_BMbkNsfcN27NoCyMDcElxHxHad1u4XBUej1o6Tcny3OKeA70gJ-E3T-Ft3xtx0xg5rIT1601Xg5QWFyoZhgIiQH3v5GFuvZAMTuQxHAaKnCv0QhglDRwFVLliYs6zJNlLbj-_lts_K_sa9pKGy9m6EqfqbNojXaQB79SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nM7kqK3v0bxw1Q2jUDu_dZ61_laIkW6iihuyhEzV-CTXTODgQEhE3cT2UHgocggzoVKoWafGT3meKKBLCPhx3gKKp3dH-k0DG9mncnK200NIuiQemAmxMsyuNXc9dD0Rp8tbf4vBdcrSyHXXxEIxl_Jgng5bK8h_f1e59EzuJZodmQJqMKJPor0oZRGsFCBfQuPjSva6uGQ6q_wKilUcB8biCzkNe5IasipFzqxFIY7AtGs6FRsxa7ZJZjnlvmjIEloEAYovhUSA7RpmbdJGXpXDWrTI73vhB0Dbp6Lp_wFXrHEJE_1W-7gPJvSbKL8L15Kko5jVXuj98A1g4WV_zA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تماشای بازی ایران - مصر؛ از نانوایی تا کله‌پزی
🔸
همزمان با دیدار تیم‌های ملی فوتبال ایران و مصر، مردم در نقاط مختلف شهر از جمله نانوایی، کله‌پزی، املت‌فروشی، سوپرمارکت، ایستگاه راه‌آهن و ایستگاه‌های تاکسی، با تماشای این مسابقه از طریق تلویزیون و تلفن همراه، بازی تیم ملی را دنبال کردند.
عکس:
محمد‌مهدی دهقانی
@farsimages</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445086" target="_blank">📅 10:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445085">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ugjd-Qs4t-m6LxOmSLC46RIyGgxXQlOt_C4u0SUA1Ej711sjPVsfzAX44LhXyoAWGLyJkawsFT9hOVeFMiIpw3GHvwn9JmNQKX0zsuJHO5zVXIqENTIPZKt5JOawwOLM-Al7dFNBijvNK9_pITtliQ_sylEw2OBvHnQIbKRrR_NTUwRQ4tQPuajNFWqml_GYlxeKdNTYdPNdNTy8rZu5T8NQhtEdtkwrcS6nU-VRg5qbXgY9gLXIMeoGriSKkcvqJ6zgYURKrILo1mkO0wI2-sOjO4HTfMs5JwE--VhBrTRXmcSOCztQu4qXUeOSBdqc2HsPkAJzYyCdP1JeakXcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران و بلژیک رکورد مصرف اینترنت کشور را شکست
🔹
براساس آمار شرکت ارتباطات زیرساخت، همزمان با برگزاری دیدار ایران و بلژیک در جام جهانی پیک مصرف اینترنت کشور به ۷.۵۶ ترابیت بر ثانیه رسید که نسبت به سقف ۵.۵ ترابیتی هفته‌های گذشته، افزایش ۳۷.۵ درصدی را نشان…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445085" target="_blank">📅 10:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445080">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgJxHI_3ptXXedCq9LE7FSdTOvSJ_ZOarasUJaX-QXIdE_qbzqkHVsjvzGQd6MvggdR3BBv4SpDlw_XBuVqdNszDrZQyaffW1oT4L0V8OO0lh95aIHCok7vYGQUmKekLiCHLkO1KIhsCCVATEudETiI9Qio_ut69TBefW2yrRI51RKPK1isUFQ6h0bMw2bxipgXSEm22u99BCDTnXgGo77z9zcWGsaJdboYpeFWvjQTQ36AraTC2chJYzgSbwi2wsBraYCQWCtI-GOE475qQ7NpdWtlzeaxX7RtR-JXYPSKbksP-SGOXyKiKD7an9J_im75AN8XLd8-ufGap937RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMhe6FYtidjIsb4F1XIXFW2f2D9SldLCiF0fdv-3kaTaerbTdv6VUNy7JHfVyGZZQremxh9qH2EBlvaElmp_I_4dj-9VKhWRoZwXwO1BFhb_S0NHXooCO8smrQBMxr54QF9hr_YrT_6gwop-OUH0J_dyhNxjEIsqWoxzXB0Vj9dnDSrgi7I25xyR4mJV66_ImCmgh3FcmUY2gbjk6yge84SIR_0AQKINbB5WuMBYSuwHOxly3VtOZyxX2lmNFyB1vE7HAbRnMonKXBPG506UIyaICKV3js8CouCJAWh4jyXDi3dlbItnF98Qxif2N2QP0KibBIE6ne4GfzAKy2mbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWtof20HhLYZ1A4GzYxUX9ZTvnKVYCHqvC8fQnRvTvA9d0hyM8eX_dE_EVlqeThgDU2suLuq4VXOd-R85UsMpSFTGE-n2XgVd-rOTjsmexsZKFN-40QeKKlGqfKrVR0j3_tx6IndocZj-V0-qdRGB7BdmDX6c1-bU02_1mFtpKeKkfI5NLACKkU2edmWZZLnrO0uxZpGfP-rOiMCzO0_JtjteHpexh9DRdYlqYlT52-r-F3FwjKXhfGMGMezjyVh0FTjg_xwJkyQZXcAz4zBBQhpteh1rxX1OU5eGgcbmOKkm44vxZEI4-jNrG7DV3GQuBwBU8PvGyOnOkc4ZI9A6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5e12dSTz7jkQQD2p9Q9BQIhcTToam_AtZTtpJAvVrttSR-WiZ10J0-Zj7cvzofaJIx2oCBcjM1s_1xdPyIpDuS1pdBNlvCs7ZHE3CQgTAjeKi02CeyB6v96n7QNcNkAaV9yL1ibOHcLyjKs2dzqRZNvaxTy6Dpn5ggyGXOA_Yb5gtCFQU7MN8t1fdJNTsyB78UD-uPe3olAkk6vfManufSoG1Xz2j3-N3jihDgSwv8343BHgJ52jhtJIdDh45EOruT7irXZZ52iaMW07IX0jTGrZNlAE7LTymR1YacGoaO5FthMX7rQ3AY-Z35O_wZ8yYJ_uwWZJNqVFiTYp-Lq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OaQMzHi-CZnr2koGL1hXKu4_52u2pDU0f1fZ_R-0iyoUcSMYIigN6KGmg900NK-R0auNemx03u49lLQjn2RKPdFCRKZ3ztYdp1VLvDtySpRBXXN-oPy9PZWY8bN9XiZ8PueB-sHK02VhAL3iP3efiJctkOxipJ8gZ_V3INhFwc2Q8ZRBPdxbIlRDE1yP_e19ZGzOtKGRT6PnpJRE9GFlyMf_K0Z26ciVu-SpOk9iCGLtKqASgkf0vpXZWSgsCsR74HXduy3zWzvdHbqxxwi94U-b5IjCDItn-dr6Gk44I6ftxuV-BS-4n-wyJ-l8yGRvCb-iwQA3kMpGv4x3aA8QvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
همدانی‌ها در هر شرایطی پیگیر بازی تیم ملی بودند
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/445080" target="_blank">📅 09:38 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
