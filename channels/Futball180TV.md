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
<img src="https://cdn5.telesco.pe/file/a6TQU73zpo7YSwFtau3smlKrkw8KjNq9ZO6rEtloE4-ELkmHJU859mNADUSa2RQLl0LYQD8H86HSqKqFlfxpEjNoHWYO4CtETlv3CIvcuGfXwDga7aykBMx-IPEExu--xBdkyz-FHXqBuwdoixSv-g2u7eYgPFX7PVNz31_jaSeYbRU1Qspi_MxrjsdMXz_JoncDCSdE5dUtoyuA_AB5SunzL6nJLD7dbzHoRO-z04t-ublL6CUdLjvntt7Th94_rG7qTv52GuWuaAzxpX9VcXgTUKJMyDmAK6RLnu5_hnecrgGIVcnLN2pfJj-ML3JrgmcaYeupBpzQUmWIAe1IGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 595K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 16:28:18</div>
<hr>

<div class="tg-post" id="msg-99561">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411cd56909.mp4?token=pul7SFEcjH2yfSQHUFU4Tb1sXqUA2hcZ1Jk9mJsfoFzbDSi_pAx3bHE9kVnMFijPvMiLOZIOCmaiPzJlsLw0wlLm4LHeH4TJbPIJ7UcGydBGXBEMts_KldKhqWe7b3noUNfDZ2cu51xx18FSN9WWg1RZ25iZAIdxt_JaXPsTi7k2K9gA-dhI3N-jXErMUrXnL9rj7Kkez73PGlLKMgrDhKseCDJOp-hgHAGiZrF_rlXzesnKCqnLIGrnSkQCPvu430F8z7F713gdxJ4qAoq4SXoExD6kpUOGAA-CjBZt_o09HfaEKjxY_3u-bxoZlE4fmCdUgRaFTdzbTIXxSDeKn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411cd56909.mp4?token=pul7SFEcjH2yfSQHUFU4Tb1sXqUA2hcZ1Jk9mJsfoFzbDSi_pAx3bHE9kVnMFijPvMiLOZIOCmaiPzJlsLw0wlLm4LHeH4TJbPIJ7UcGydBGXBEMts_KldKhqWe7b3noUNfDZ2cu51xx18FSN9WWg1RZ25iZAIdxt_JaXPsTi7k2K9gA-dhI3N-jXErMUrXnL9rj7Kkez73PGlLKMgrDhKseCDJOp-hgHAGiZrF_rlXzesnKCqnLIGrnSkQCPvu430F8z7F713gdxJ4qAoq4SXoExD6kpUOGAA-CjBZt_o09HfaEKjxY_3u-bxoZlE4fmCdUgRaFTdzbTIXxSDeKn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛂
سیستم VAR در مسابقات محلات شمال کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/99561" target="_blank">📅 16:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99560">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTZsxPXlrFNaUkbRo-MOmFhaNQ7bW9KzlZNTfDYR6t8O0r3Kh1jahLKWa7WOJBcFCUPYd3qOormvr985loRTrD6KtClwkazWhxQlbBM9-EOkEYXlbL0CGnGxxSaK41LVFBful1pnhV8sePLg9gyFx1htNtqxTTT2u2x62UdtrzFXmtU3535X24O-j-1CFiqhEIM5pcSKgq29GfzQajV9d_hPzi7I2QCqCrK6qTcQyOCl0s8tEOKrRla7kDF-UMsWs4yLVe_UQVys8Yv0qDm5zqLsb4xp-MHxOpuplXqrHzqqzUF46P7M4OOZTd2T2i-Mwkg2RETzkyF6sXXvk7zfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ ترجیح مردم کشور های مختلف در بازی امشب :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/99560" target="_blank">📅 16:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99559">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2fbd5dd7b.mp4?token=EQqgGHKbqh7C6pxazj4aCjm648n7aPH2vk6gxUyKUvn4-mBWeVZvIaGiSTbzgZfGe0SUk2JxBFsxIJhDusuQOd8DgDlZkUp80VRJAMz4q8gisPDW6PFPFZ1qNhoRkA5Qw3xPsPIdBSnODYwO1Xh1Daf6gGfCkEtJD1GWnDiNTItcSsIG35hyudvVw3yECVrKtLv2xvOoCdaEqrqTMWl2uOKVNpnB5Wdho6eadvBu01yF8ezVjydLo8BYduuMCin5JQJW6xtiKR958fA-GmJQYgSH9yUkGS6TR2mvv-MvGJByb46syeC1eyTt_0mt5jh-nQtqtnGPUi2kEqrKtdFvwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2fbd5dd7b.mp4?token=EQqgGHKbqh7C6pxazj4aCjm648n7aPH2vk6gxUyKUvn4-mBWeVZvIaGiSTbzgZfGe0SUk2JxBFsxIJhDusuQOd8DgDlZkUp80VRJAMz4q8gisPDW6PFPFZ1qNhoRkA5Qw3xPsPIdBSnODYwO1Xh1Daf6gGfCkEtJD1GWnDiNTItcSsIG35hyudvVw3yECVrKtLv2xvOoCdaEqrqTMWl2uOKVNpnB5Wdho6eadvBu01yF8ezVjydLo8BYduuMCin5JQJW6xtiKR958fA-GmJQYgSH9yUkGS6TR2mvv-MvGJByb46syeC1eyTt_0mt5jh-nQtqtnGPUi2kEqrKtdFvwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
مرینو کلا آخرین رقص و آخرین شانس و این چیزا حالیش نیستا.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/99559" target="_blank">📅 16:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99558">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1Aaw9qOI5VgaPqZOlPyLfS5FW3HCu2wS27EKdm9SdcPy8ePwogAtWbJKunrZRxvKtMJEjCu6yo3AqbQfT2FsuHMpEZQ16q0KPFwFtu_Uph0k5NoAgE-j8Vw7t1KureJAbchdScLOJNKYNxyPpjzOcp9TwyjxbCse2aV1cFZlIdBDy5EhA20Cp4sDFQ23wgBrKAA2MhWpAUcI5seEARBDBCMC8pJBS_OjY8-YZ4nSxIXPqADwWrH7i8yeQGhd574qJ1QvuwzgRgC1xLspJN3-iP_ki-8QJ704QUBelzCs6edyHaRDRGrbFbIEpBT80XlFzHaSYPhKu_hFOQWr40x3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇫🇷
سن خط‌حمله فرانسه در دو جام‌جهانی آینده جوری هست که به راحتی میتونن کنار هم بازی کنند!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/Futball180TV/99558" target="_blank">📅 15:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99557">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84faa7ffb.mp4?token=njd1oCoVmQpzHjBXSup6vuNXbS_qWsLBEYVA0qzM9rfv6-2faDyvsUvKVa-nb_OSciVbhGqOhZ8QRL0ueusmDdzf8FoSIBx_4jecDJurkNqIZjQMjHinquAy2nvMGtb-EB7S63q9VO7uChBUdS0YwQKLu0CU3UWKfpQJCDVzJMHFlkO3jWnWt4dHZF0IeKK7fOGnz2Ko0ZWgr6w7jwXkiEf0BuUYiRZ9TIeTlDdOqgzxIfZctjusnrXKVTXe66LP_cfQFR5Pq1YvmrhnbWpQOshk4t_OpWjkMP4OeAuKcLysYmTrSrsvP7tMR3eF6zHjUF8zAqnKBQFCNutiKejs1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84faa7ffb.mp4?token=njd1oCoVmQpzHjBXSup6vuNXbS_qWsLBEYVA0qzM9rfv6-2faDyvsUvKVa-nb_OSciVbhGqOhZ8QRL0ueusmDdzf8FoSIBx_4jecDJurkNqIZjQMjHinquAy2nvMGtb-EB7S63q9VO7uChBUdS0YwQKLu0CU3UWKfpQJCDVzJMHFlkO3jWnWt4dHZF0IeKK7fOGnz2Ko0ZWgr6w7jwXkiEf0BuUYiRZ9TIeTlDdOqgzxIfZctjusnrXKVTXe66LP_cfQFR5Pq1YvmrhnbWpQOshk4t_OpWjkMP4OeAuKcLysYmTrSrsvP7tMR3eF6zHjUF8zAqnKBQFCNutiKejs1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرگزاری مهر خبر داده که برای فیروز کریمی به دلیل حضور در شبکه ماهواره ای جم توسط نهادهای امنیتی پرونده قضایی تشکیل شده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/Futball180TV/99557" target="_blank">📅 15:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99556">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2e8d837a.mp4?token=lFFwICpqVJBn3KyMdRpvxjH1Au6Xo7HbEaaDywtrdmusnX-4v4KMp-WaeJs-iIVAfOUwtaR1Q8G8XX_31Q6eOAyQw8c-Llm935AcP748U58lCMosmIdwHjUqf45S5PB58oRR-vaCE2YSATlkhuX__dQMxX9GMWLNnfYYu1SeGX44stg_GWEDhjN73PvEJijrrPbZu1JbvO-0diYX5FBJgWgf84YgH2X0mAq1G-V-wDDThQMJI90YlEUxQJ5xq2ckWW_pqlUeXF8g0ENL7SMXA3ul13zMWVP7Va30nExBRHKn0QOz2KrWcRH8yC7620q5QH-6x3RpKbMjXfTbOOvlLJyA0ojgEyZhiSaGC2ZpNhx_1psSvVw7R1KeS3DZjGapRmz2djAm2P2N6opK-vyT0M9hVjfBsFViGSRyM2rbA4bQZAY0-NGNQrvzJGaCYNaM0MmrpamYQG6feRJbcUxz5DgO-dS-kv0-Cvdamte3AUWbJhIkLM-xFL71GQYYDbSwIgedMCeBPJLTPBudoMONtNcizcrg4ExK56WKZ5UwYwLks-5lGf-b_cbWZBcA4eTQlkEj9iOYRIG7GBWT3zY60t-RyQZdLexXJ7vL-96rEIHBl64zD_yEYsYgSL9PQh_eiDkZHYQnaG2lnnqD2QoaDvPlmXvI3H2bzI6IHnH31CY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2e8d837a.mp4?token=lFFwICpqVJBn3KyMdRpvxjH1Au6Xo7HbEaaDywtrdmusnX-4v4KMp-WaeJs-iIVAfOUwtaR1Q8G8XX_31Q6eOAyQw8c-Llm935AcP748U58lCMosmIdwHjUqf45S5PB58oRR-vaCE2YSATlkhuX__dQMxX9GMWLNnfYYu1SeGX44stg_GWEDhjN73PvEJijrrPbZu1JbvO-0diYX5FBJgWgf84YgH2X0mAq1G-V-wDDThQMJI90YlEUxQJ5xq2ckWW_pqlUeXF8g0ENL7SMXA3ul13zMWVP7Va30nExBRHKn0QOz2KrWcRH8yC7620q5QH-6x3RpKbMjXfTbOOvlLJyA0ojgEyZhiSaGC2ZpNhx_1psSvVw7R1KeS3DZjGapRmz2djAm2P2N6opK-vyT0M9hVjfBsFViGSRyM2rbA4bQZAY0-NGNQrvzJGaCYNaM0MmrpamYQG6feRJbcUxz5DgO-dS-kv0-Cvdamte3AUWbJhIkLM-xFL71GQYYDbSwIgedMCeBPJLTPBudoMONtNcizcrg4ExK56WKZ5UwYwLks-5lGf-b_cbWZBcA4eTQlkEj9iOYRIG7GBWT3zY60t-RyQZdLexXJ7vL-96rEIHBl64zD_yEYsYgSL9PQh_eiDkZHYQnaG2lnnqD2QoaDvPlmXvI3H2bzI6IHnH31CY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
لحظاتی با داداش بامزه لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/Futball180TV/99556" target="_blank">📅 15:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99555">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a53021254.mp4?token=jyTcd45nscKlgLCjegAGDp3_T5yhQmuM8N-BM3NE2jmFkWBYt1-LvnnFdyVm8-0dxR6uu7rNtP8TQE6wpP3GOZVeT86F46qQpm_m6XOg8eRUQeQvZpOWjxYaWp_o-pIDxzw59jOUn-j7mxMdwPPwLquVpsPkw4-Y4FrBY1XpS4gwNMFjmJiuqG8N2hr3HZn7cJvBafyRqSFGhT5w-q6nS4-QpOOcBmvGaWYWNIqpTbOoY6IDaLsFM_zEFYbkfMuD2gxHeL5iKbWGf_q4AxOUrah_5Tpv-ky_RIgcszoC1V1lEB2dTEwu6FLy3-pluhaTOBPvjwBhUfSG2voqRPvdPqD_MLPZXhUjj4d3BNWASrofRIVzPbc3a0TPqTzLYQQZsOtotpAmzmtYeXBVyqL1PdvIHDRGWg2ChQ2lYCSxx6quvfrB7wkrtFkKj_Dy43VnfrRBUxcAf-f3iUT_ItPkqHJJoNRcbhQ6I-4BqVC0aHO46H4f9rDKu0Acg3iszknBNba6neOh5c1zWeyH0U3JOFbHRbBDW4Wmcni1lw8Ho_8ooO3pTI4zKolCCdtemk9LlnjIL1Vdy-X0rJJo9Hl3f345FAsTZhY7DrxsuVvx7F79R1G7ihCIGZzv7XIpv69cir8RakwMYtNX0wnDRkj6JV6MICrUoFWU_jVsX7az2S0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a53021254.mp4?token=jyTcd45nscKlgLCjegAGDp3_T5yhQmuM8N-BM3NE2jmFkWBYt1-LvnnFdyVm8-0dxR6uu7rNtP8TQE6wpP3GOZVeT86F46qQpm_m6XOg8eRUQeQvZpOWjxYaWp_o-pIDxzw59jOUn-j7mxMdwPPwLquVpsPkw4-Y4FrBY1XpS4gwNMFjmJiuqG8N2hr3HZn7cJvBafyRqSFGhT5w-q6nS4-QpOOcBmvGaWYWNIqpTbOoY6IDaLsFM_zEFYbkfMuD2gxHeL5iKbWGf_q4AxOUrah_5Tpv-ky_RIgcszoC1V1lEB2dTEwu6FLy3-pluhaTOBPvjwBhUfSG2voqRPvdPqD_MLPZXhUjj4d3BNWASrofRIVzPbc3a0TPqTzLYQQZsOtotpAmzmtYeXBVyqL1PdvIHDRGWg2ChQ2lYCSxx6quvfrB7wkrtFkKj_Dy43VnfrRBUxcAf-f3iUT_ItPkqHJJoNRcbhQ6I-4BqVC0aHO46H4f9rDKu0Acg3iszknBNba6neOh5c1zWeyH0U3JOFbHRbBDW4Wmcni1lw8Ho_8ooO3pTI4zKolCCdtemk9LlnjIL1Vdy-X0rJJo9Hl3f345FAsTZhY7DrxsuVvx7F79R1G7ihCIGZzv7XIpv69cir8RakwMYtNX0wnDRkj6JV6MICrUoFWU_jVsX7az2S0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرمهدی ژوله: هوادار فوتبال و شور و حال آن را کاملاً درک می‌کنم / حرف من درباره فردوسی پور این بود که ماه نحوه شادی کردن را بلد نیستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99555" target="_blank">📅 15:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99554">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-v8lCcngHB5OkqNW2e9iTatJ4AJZnL2QWJFrErP_0fILzWNJNEnwrR7sq09nhMSTpmZMv2xd0aCc5KQViHnvcnKWyHN8i-ydnViytsuZoEfYJaYAV0s9Emitq5dqQC6fInYFVjmGLGv4kJRxvvvdBn_PETVWbxWVl39CD9vF97vcIj7hP21qg1pYipfG3lBV86BNuEglxUAZAYfcfTJJOu5WxaTV4GQWFtIEcaL7VKtt6l17y4wxldg-GcC1Pp_fJ_HnGYvgVXAUwgDp6jVt3luZ6im5ba1C4VuPFvQ2eASQuXP0dUD5v4brwcfWBaAhPIEO8Ty3yQVzExhHv1qhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیبو کورتوا:
برنده بازی اسپانیا-فرانسه بدون هیچ شکی قهرمان جام جهانی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/99554" target="_blank">📅 14:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99553">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735c75025b.mp4?token=RJ5hCY-J4MUR3nlqY8Ub4-tFdP5g6Ol_mc557I1Kdo52n5zxm-y7HWfm3Fk-3R75PVO4u8_XsgoreMQc79rO2kwh3oG4KnHZa9PES5iIe71yTA1zwerrcKEup_PNtGHVPzwoj4zCuSfi0sWhF3dMhoKxS4AtS1Uu43ZQITS5QOsIYD_y0w1ZXS_q2GorX4EzMMPYtuY2cD3E0rBogW1swhxqO55hJhM5zNafQVoqlnFVeCw7ziwBO_2bBsTr3j8HpyP8QvPjlmkqPwREjOuzphMKAwzWZs5fkDNkYMYdA40EClbF5vM6F5WV1YkGqO4ATY9tdsHxN97GYMNZEvVhIEuUz1E3niXIfBBRypIjy8wfjJF88ngn0J74WgmBAoFe0W4ylMMXELp9eR37WGPm-wlHxKxG0aBtN-VLUKR2uiBxpSV9sGk6WchmU39JtCIVIoXRKbQgmRggxeI-_zyM55dPhuEVnqoropduZXM67lBHE163332uqZxPC7j_ziV_lxA0aVKFh4dKEa9s1uMZw51Ox8eEq_al2OAMQN3-2GpOCtTgmHfGw_3f3mUPNkiE1eVz31n-BA7G8gcyHeNm05qDP9kT4u0-2W3LwAvEPzOhT_i8gY3TLZdXlRXzS7ufSd5RFak_P7bs5ufFChcx5b7jvRAevANMubBZ5DKqdEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735c75025b.mp4?token=RJ5hCY-J4MUR3nlqY8Ub4-tFdP5g6Ol_mc557I1Kdo52n5zxm-y7HWfm3Fk-3R75PVO4u8_XsgoreMQc79rO2kwh3oG4KnHZa9PES5iIe71yTA1zwerrcKEup_PNtGHVPzwoj4zCuSfi0sWhF3dMhoKxS4AtS1Uu43ZQITS5QOsIYD_y0w1ZXS_q2GorX4EzMMPYtuY2cD3E0rBogW1swhxqO55hJhM5zNafQVoqlnFVeCw7ziwBO_2bBsTr3j8HpyP8QvPjlmkqPwREjOuzphMKAwzWZs5fkDNkYMYdA40EClbF5vM6F5WV1YkGqO4ATY9tdsHxN97GYMNZEvVhIEuUz1E3niXIfBBRypIjy8wfjJF88ngn0J74WgmBAoFe0W4ylMMXELp9eR37WGPm-wlHxKxG0aBtN-VLUKR2uiBxpSV9sGk6WchmU39JtCIVIoXRKbQgmRggxeI-_zyM55dPhuEVnqoropduZXM67lBHE163332uqZxPC7j_ziV_lxA0aVKFh4dKEa9s1uMZw51Ox8eEq_al2OAMQN3-2GpOCtTgmHfGw_3f3mUPNkiE1eVz31n-BA7G8gcyHeNm05qDP9kT4u0-2W3LwAvEPzOhT_i8gY3TLZdXlRXzS7ufSd5RFak_P7bs5ufFChcx5b7jvRAevANMubBZ5DKqdEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
افشاگری رضا جاودانی مجری سابق مردان آهنین از پشت‌پرده این مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/99553" target="_blank">📅 14:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99552">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFY6q4H0c_uqBpeIOz03Rw1nY1pkU1hrOgu3v0fxPqiHP8vVDPmHmKACUYwBLggQSNwA4SAXE9mh1zSDeBg2gOlTxi7UgDRTVUGozWu415DBFbkSlzPfL7HqAPcMEcsD9ZQddSA5zZzRZeQlkfdW0XBtDQeZEXGcO8fRKW64zFMuQx1VyyGBO0y3XsgsAoyq41oxlGqmHWglhk9D-BG09WBAW1cetjuMHMmVn3wyJqvbGIpI3jfAKGLBpQYuhrdwsKoGHi6v89c-ZGSQu0SwhL_GhoNX2Unw-XDGGs5IQSwJAf1eX5NsfaVh27U9pMuJQOR-2KugXmR4pAtUC4lrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇳
اسپید:
هند به کمک نیاز داره! اگه این هندی‌ها واقعا دوست دارن تو جام جهانی 2030 حاضر باشن فقط یک راه حل داره اونم اینکه من رو جذب کنن تا واسشون بازی کنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99552" target="_blank">📅 14:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99551">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTD8yAzzxVGZHa1lQYGVnUbEc2lSNC80l89WRXop5NMe1NpnFvMEHF53nBRNTnCXZH0-V5DbPTEkQkQAtoPDPuztpt5Km-CN1flhQjbAZMu9A-9Z4WFho0xvvYqBkkskFK8T6n7z-XosllqmuWn3n-2Mw9Hs0HdqiN4a5i9Gjfra8dZCfBmjzxxPO6TstVN8O8Z1QsnFz6J7sMj0-K3f4ATXsqhQbs71pucJkvoXNV6e5otjQQjFyPmHD9gQkntBc2G0GqlskTBTm4X2s5SjlehO2aJUNk4UY3DzfAzEma1VH3q_zeIQHYcR-BWZPV9_2HsaGGqr1vhzYmb9DsrnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال‌مادرید و وینیسیوس تقریبا به این نقطه اشتراک رسیده‌اند که تمدید قرارداد بزودی حاصل می‌شود و ستاره برزیلی ستون اصلی پروژه بازسازی رئال‌مادرید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/99551" target="_blank">📅 14:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734fedf32f.mp4?token=mr6DIR1VyNsCxlbqUjAu5hvQPxFO5q-lck6Bi74loRFjBo5WmBR9eNrGCELgP71m1Cp0iGiRYm-6JXkqyTjrNFfBByaXPfGD32G7aCtP54dF_d9ijvluqJbyUIldojnrFm8y5NYp8dYbGoCwpIfp46hoY-g1cvDnSdFfcSe1v5JrJlwEs7Qb2rEp1ia1i7MIIZOMcPpPgbvb7ly6cTGRzxs1-gHIDBL8jYULYm0e6jUAWkFdEeceK0ZTkKIP6pguQ6KzLvuB4pQ8t9k8vfDFd2A1_kbpJkKYjHoyrl2fw-8uhDCh4cZu0dtTtH572VRK5mi8xkx-AmsIQhRGaXdFfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734fedf32f.mp4?token=mr6DIR1VyNsCxlbqUjAu5hvQPxFO5q-lck6Bi74loRFjBo5WmBR9eNrGCELgP71m1Cp0iGiRYm-6JXkqyTjrNFfBByaXPfGD32G7aCtP54dF_d9ijvluqJbyUIldojnrFm8y5NYp8dYbGoCwpIfp46hoY-g1cvDnSdFfcSe1v5JrJlwEs7Qb2rEp1ia1i7MIIZOMcPpPgbvb7ly6cTGRzxs1-gHIDBL8jYULYm0e6jUAWkFdEeceK0ZTkKIP6pguQ6KzLvuB4pQ8t9k8vfDFd2A1_kbpJkKYjHoyrl2fw-8uhDCh4cZu0dtTtH572VRK5mi8xkx-AmsIQhRGaXdFfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
چه اطلاعات مفیدی مهدی‌رحمتی بهمون داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/99549" target="_blank">📅 14:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8suwO8oHF9JMEO3JF7m-I3daiK7ccUmlVncxiIhRKxlWlWrSvBfk3sd-VhcVx3fBW4LSzGazhxDgoy8IairVAhE29c2Ho-8_pPRN7MW89R0A7XQY_Ka4TSxKlMAA8JZNbphebFWDuX4L5l7YEhMzRTcU6GqSUmgFgMRXFqmpeNmQ4DOefxnGOLY8gxQUAY6GuOJbc-MiRnol65JpxsDMbRmxPd3msacDAY8Ci9haMe-O29KOszLtqN5g_DIZCH46-sVyxd914n45D_Jdz8QHQb39AbHj0JGT1m8qZ1nCYumBvi27LZ33bvUIxjamdLBaF8NZoQWl_tSKWbgxzI9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال‌مادرید و وینیسیوس تقریبا به این نقطه اشتراک رسیده‌اند که تمدید قرارداد بزودی حاصل می‌شود و ستاره برزیلی ستون اصلی پروژه بازسازی رئال‌مادرید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99548" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LWdm3xH584JU8aMuu2jWfmYkBXbGg1uObugtuIAWIboXDeUcak2U_S0L4uaYSf9lxp3LuJb8Ybkkjo7g6oGALBw6jX4G6hhvNGQ_7s7o8vn6p00MWxQjY4RY51FK1ig6eJbb1Qx8QQuq0pQhejAFwrUNBkBVq6tzNgcqQvwHyGF0Qt6BlIul-bCFnqshx75HeDGhHb_drJZS8HlE6Qg8vr-Hh1qIEvcrxRuzBum0rhXM3O08crDqR2r_pB8g_p7Kd6yIUMoIE6rdXtmH5vGmcsHdgXy9iA2523WA-wwxDNrbh_suHNSCqpWPtgHB4rpe2BDm_e5AYQGvlpYLODBztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‏فابریزیو رومانو:
🔵
بارسلونا آماده ارائه یک پیشنهاد جدید به کلوب‌بروژ برای جذب جسی بیسیو، وینگر 18 ساله با استعداد بلژیکی است.
✅
بیسیو با انتقال به بارسلونا موافقت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/99547" target="_blank">📅 14:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQn5H_wkBoFC_XXclhZRKgLbXcyBfyZgazceGyHCCXPhevAKMoeIAoEPdVIp3VXWz66ryGAjZjhpi_U4xatgYl-AIcy7-7ghegsQG1zjbYc_V_x8t-YPdW6PcXB6d-zwnccaGQX3n5URssbPtheC-zntDSl-PTVLn4b8KhOE5HoGD8WDQg3SjvscbigdsqJkzmh4mBiVeWjRIac89ElQYIOaBo6E3jbKkWgt2cekYbebbcp2BFAUOFeQrns5lsbCwu-YSwExrR2fPNGg8y7xed00SoS3DNRT72t533rPmFrLLhwMruKzhzbj9NWZTRNTnbpskKn8rpuJky7oX5eV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل مرینو اولین بازیکن تاریخ جام جهانی است که در دو بازی حذفی مختلف به عنوان بازیکن تعویضی گل پیروزی را به ثمر میرساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/99546" target="_blank">📅 13:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_X2Hsf4HcjKCjBbrt4JKU639H26BFpzxwjZBH3tbzb7S8RhFvDcSpTkSo5uGfoQo8L7nmkyZmV0UaMUEfxQYQPxzmAYrL2uGReJMi31O7rDp4pWrXSgx7yDNOewixMysRuqZI6IbKyrkUnJi7R76oa3RjiIsnkoj8JiaBQjS1sOmnsEgITKdn0HYzvPftEZacwoxgOqS1TuSYr66PdiH644RVVWPeZHEnY7pP2OpGE3YzKf3j7dkkVPqOIPzkgVDQFBEfaD_F0Lh6luw6z_ieuw56SuuRvSfDldff28IKD3NGK54ljvgJ3Rq2-KLI9ZIryXoqyWjR5b-7kzdzY5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شانس صعود انگلیس و نروژ از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/99545" target="_blank">📅 13:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyVteCPAaxv0AT35NkMKLQphED9ku0ySwjt2VRxZztgSvUk3Gvf9Ih6mdGoc0Kp_QXHoHRDP4qvWCXzVmpQ2vAoGAKrZMKnO9uZanFjfZhuf2ZrVDksc25Ak19Ah4ESONoHVnLV_h1LjY5v2ECi_tw-EAGl2CefOC977QbCVfWyOoGljeghgT6qrrHyCfADpMv3n1vubWbl3kMbdeqQtrTzIzMGMC2nAvZBLcFT0XyGXUkbklZz--whq-0D8PlrPGW2kHgtEjrI8c1ofnZCclZsyPDOGPCjBsJvLH-l1FUqN1EsL_D-6G1WTyjtrd1vywyJS_92G0t0bhRVVT_3TFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کشور آفریقایی که از جام‌جهانی حذف نشده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/99544" target="_blank">📅 13:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm11zx5UD_qcAe-E_gsZjB3LyIuo_nMK0J4qRDHRjT2K98dEglOxrLY_46AKfBrsgx6hNmmfq5AkzndqX0y2geTYantVkQvtm_Y5j6cK7rbCAzHt4p3QhVULyw6AvsKahToOBPT7JRIjXykVbCvZERuQboTTWl0fHrXvnmbpkthSIcn76avpRs2NglA7Az5OKCu1E0sZeMRDAVjXjPNDxdMrPLMs3hahFjyGJ80X3HrtIk6KTjkkSXnQhEFhCAgq6MAdf0mrZhQaabV3NkptSf_G55U2ATtpkmZwiHZF2ragE-agJ5pyFIJJxwCdr-f3CEVH1xKkwTr4xm408-Gpsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
| رودری، بیشترین تعداد پاس موفق رو در یک‌سوم دفاعی حریفان در طول جام جهانی 2026 داشته است.
⌛
از 180 پاس، 170 پاس او موفق بوده است. همچنین، او بهترین درصد دقت پاس را در بین تمام هافبک‌هایی که 100 پاس یا بیشتر انجام داده‌اند، با نرخ 93.41٪ داراست.
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99543" target="_blank">📅 13:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99542">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fji_TqT2XiSlsiQQmtCCbEzolHPfMP53FbFnkqOQGdC-MCtkSwSvmX4vafmy7JOqS-mK4Ck8NbYMR3OfV5Zow69qPBmDGHs8XkmeIhZoJVHEgIQvbs7pWkkSKQX-5e1wQa_zHkCM751SoQ0PkuanjE5lV89pUoWS1SltlUVTQzIIc0iObVpy_MsTkgyrMP6kQl7Ec0aEJ9PmPZK-DKRiHFlDN5ogxyMrhC5XI0biS5Ih7RrSY1a53cwlXG0VvjJxKWa0C1fxSQBCagOb7QkqMpc0qTZqZCwvo-BWDifYbHUD4tEbCgAdiEtifOXfO96lNjUcHDwnTkbFPFdgLOtT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا دیگه چیه برا هالند میسازن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/99542" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99541">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYZsr2rO11kavClTFXY7BlZZ6fOSFx1hcHazV9RSEWgSdT_ZUjpgFmoDCE3C8SMdaQXlvRZuqxlvJELz8d3sBjomI9i2BDGkiLkHjnAYtlhpp5V_zQKm7Ej4XLqSAYoS_MgY495ZvusFnfP2yX24rrnNtk4zfgUS8cOAojHYpmDXhRKOpytezDhC1aPlTxKrUz3at1j1VIW2j3j3Q7p-2HlA0V7f_MzUgE37HaLr5VbTsSafCC-0JBAy55s3_SytKJjN5ifAlm1rw4SoRzVn2DIi_0bwE0NcQgjIdmr62N-Kky-FPdSwpoU8Ei-hgBWVVz0KzjJIiiJ3k1eg4toMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99541" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99540">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn8EMPychJBExuIeMHkVgRljfTexT_qkkLuEIkHQ1YgVgrfFpH882yXjfaRl_VGz_0IV300ssA8iVddIsWQghTUtG-p4vypOXHsD7p5bPKn_-rFtwk5aMO_0LU2xKGzT6-OAu7E8LoEDo--1ALjDvNy81KrPxDM-HzzUcbSnSGF94WlUglnJ6irqnM2IXq1oyS4OSPd1kmjRrcbXt5_P1oElv4sB044t9GvTsxVJyhEt_QE_fp802O_uHBvJpFttP_ArAydOpcwZyYDkvGRwomoP4v3XKOfaIyrlz4nyeNuAj6dEiwwNYcfz5Wt7ePo4CFQIxKAN4EwO1HFm69_FBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
همسر جذاب و دوست‌داشتنی آقای نیمار هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99540" target="_blank">📅 13:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99539">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fb9f73e4.mp4?token=tgVFvcsjhdJSiKkvYCYBonsQbuvZOZ76ZcKmugvNZxvjoVlg-Xm_zjs9-tP-k4Bsz62EWkL4_Nf8CW--yxPCyl-p1jzgvTZWe49LoeuXycypK63_-G0nBmT-kO61lzoNAcUnRNBTSSePuSt2GioDhhQDk1U57Kjo5i0wpfSP86DByRFfy_3YkoxnsDza6zwQPhRfKlu1_rSrbhmGZh0c-pTEHsVbu44EsGa1hHHmdeXVEPQzBaLdioMlYZzMeogDrHhzBqTjbP_KViraOe1XDzOBu08VuS61UXdOKeVYFsdIdOwOZOTWXtcTImNbKYH4IpiOgUGtmzBtTycEg4JfYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fb9f73e4.mp4?token=tgVFvcsjhdJSiKkvYCYBonsQbuvZOZ76ZcKmugvNZxvjoVlg-Xm_zjs9-tP-k4Bsz62EWkL4_Nf8CW--yxPCyl-p1jzgvTZWe49LoeuXycypK63_-G0nBmT-kO61lzoNAcUnRNBTSSePuSt2GioDhhQDk1U57Kjo5i0wpfSP86DByRFfy_3YkoxnsDza6zwQPhRfKlu1_rSrbhmGZh0c-pTEHsVbu44EsGa1hHHmdeXVEPQzBaLdioMlYZzMeogDrHhzBqTjbP_KViraOe1XDzOBu08VuS61UXdOKeVYFsdIdOwOZOTWXtcTImNbKYH4IpiOgUGtmzBtTycEg4JfYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا دیگه چیه برا هالند میسازن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/99539" target="_blank">📅 13:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99538">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
‼️
🔵
🔴
جزئیات لحظه زندان رفتن ستاره‌های پرسپولیس و استقلال از زبان ناصر ابراهیمی: من که لُخت نشدم. به هاشمی‌نسب گفتم پاشو خودت رو به غش کردن نزن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99538" target="_blank">📅 13:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99537">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d194f8eb6.mp4?token=OOVlweOTi-jHDCmU9j2Y1VedWGbexuRU3_IWUXrWT-ileRP3VW01PdWCEVu1vL7UV_Fxdm_N2tMn3pXsUzrIIaNe_Jrq7ygDRERJkXzpW5hMx1TlCGb6iHld8BIzzfS-jlR7Yhoq7AK4pLdhwT3QCi5aB5dxG8i9Dv3xOOEtiKEZ1EESlg2yK2BtgjiFuvrGblwLwsWsCXVQoV2jm7_B7VCS2AEc-J8_GoIrqvIeQHQ5N_CbMjVR3HxumOE3hKxR9qHL6zLyYKTCY7WfAkEZux9ASqrq8VKwYyNF6TD7Dqs5GuUOhf4FNA4RFnOvTdDNdjJbYskwOwDDCJUWc53F4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d194f8eb6.mp4?token=OOVlweOTi-jHDCmU9j2Y1VedWGbexuRU3_IWUXrWT-ileRP3VW01PdWCEVu1vL7UV_Fxdm_N2tMn3pXsUzrIIaNe_Jrq7ygDRERJkXzpW5hMx1TlCGb6iHld8BIzzfS-jlR7Yhoq7AK4pLdhwT3QCi5aB5dxG8i9Dv3xOOEtiKEZ1EESlg2yK2BtgjiFuvrGblwLwsWsCXVQoV2jm7_B7VCS2AEc-J8_GoIrqvIeQHQ5N_CbMjVR3HxumOE3hKxR9qHL6zLyYKTCY7WfAkEZux9ASqrq8VKwYyNF6TD7Dqs5GuUOhf4FNA4RFnOvTdDNdjJbYskwOwDDCJUWc53F4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇪🇸
لحظاتی‌کوتاه با آدیمی‌ستاره جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99537" target="_blank">📅 13:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99536">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbw5pj5sv21pS-8ElSveR7fylVrXMJ4TfS72HfW95c_D4bt9GENPIEYWFTHLycY6YYkSZOPYN7_8QFhBb99TLoKPWznNFhslSslg3HXCp5b4D39ymjL6nt7GeGNUwMOEzUJIVkM7TQ4khabtCIPVWcA12PoT2STTOGQ4vT4T65Ap7xMqsVFPXIFdOXEp3tVJ17ffNS78e0eC3p1a6WDC3p6ssnyIE7nKTytYtq_vbhmQFbpa9FEsmC1jAxqnZKih1jsYKfgU6HidtLGEoixHWD6jt37KEieNphI8gLfIZ0ZI7RmIRNFCdwetw-YhuaSpE7uCZUeEu4fl_klfJM6etg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">12 سال پیش تو چنین روزی لوییز سوارز به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99536" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99535">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔴
1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99535" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99534">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgYGNphDqpjj4Me8CwwPKHuWIYronqQ5EM_eh2cJKomWXqqnWvxd6QCBFDSHiMtpijWqvn1QOR7qIKw6cXHNsBq0km0FUdNsTwoKntkZ-L4xe8fOUBrp86uU04Y7ZBiCVPkWR7k07M7PXW2ltefjoNg-yjNx0G1hWuNPCwsCqviITQdsYjKy0TZK1rWyuxfxqi8ZHttvIS4ZxaGr-zomfuXXGh_pE2076TBnXxf_1o_FNNne6LBOs9kcxlDftwmB2Ht-jiyQyotosNJ57Kor6rvAmnDfVQiyhvbQtrClBBzDzzj9if94zlfDewkkUz99eLqF6YetY27Ixdoz7IFKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✊
برای یک بار هم که شده بدون استرس شرط ببند!
❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
0️⃣
2️⃣
🔣
بابت هر شارژ موجوی اضافی بگیر
0️⃣
2️⃣
🔣
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r20
@betinjabet</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99534" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99533">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bdae855b9.mp4?token=vQNrxQ47UT-ljnvsVzJ87JMfJ2BwhpNFun439SMVI80fPPRavu734We8da_H6djMbSoW4V3977IS213dm4_9mEEBMNT7uykYUZysFC_BHFHPiWaRiFi_LoidKugWKsF20qXcrvJl9mtJyRr9BMjDjq_5NjE62sT5ji_bEBd0ZuJwHgcwg_4TocMXN4byFCgkuvNXizx5RN-IDkQrN05iKnRLWHSIBebqjKR1Vikk6FTjy8px3pgZKnMcUn4uq-7-8K7VkiblRu8AOV2SQUt8NdloPD7A6K1doDzCukwIIP-7AzU4LCfObYQ973DUpPkXQCksYiUn6aQrNugTREdM3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bdae855b9.mp4?token=vQNrxQ47UT-ljnvsVzJ87JMfJ2BwhpNFun439SMVI80fPPRavu734We8da_H6djMbSoW4V3977IS213dm4_9mEEBMNT7uykYUZysFC_BHFHPiWaRiFi_LoidKugWKsF20qXcrvJl9mtJyRr9BMjDjq_5NjE62sT5ji_bEBd0ZuJwHgcwg_4TocMXN4byFCgkuvNXizx5RN-IDkQrN05iKnRLWHSIBebqjKR1Vikk6FTjy8px3pgZKnMcUn4uq-7-8K7VkiblRu8AOV2SQUt8NdloPD7A6K1doDzCukwIIP-7AzU4LCfObYQ973DUpPkXQCksYiUn6aQrNugTREdM3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇵🇹
ژرژ ژسوس در مراسم معارفه به عنوان سرمربی تیم ملی پرتغال: برای من اسامی مهم نیستند و هر کاری که برای تیم ملی بهتر باشد، انجام خواهم داد.⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99533" target="_blank">📅 12:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99532">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad73d33a3.mp4?token=V_rtCLCi3HZPk39dyOUbyI5P_lrKO7kqBSd7cZxusELG8AT2pMb6NfVI7kcbrElQJKw1uqNGNEUVoMQRrR9nMFuINYZi8To4iN4qkxBAD0kpxqv_kHL78YDR1hAaGJdqDoZhRtaAMf5V6-KCippL5xoQJ5tAF42BSDGoqZsgwEReeOHmbIQ_v6wH0xMBGQZ_WpLzmKlZDNMDK6XXiFDxRXXNfESYZWS0xvlWYlZ8o45oSXrDbN7RzP8De7IhZvHUXDxqf-WPYicw532lOIFlm68cFC8HM7LRTToKXJwrf8uycNpgGjotRejyWsKOtPfzq3D3rn81eJ7jupcpTR8zKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad73d33a3.mp4?token=V_rtCLCi3HZPk39dyOUbyI5P_lrKO7kqBSd7cZxusELG8AT2pMb6NfVI7kcbrElQJKw1uqNGNEUVoMQRrR9nMFuINYZi8To4iN4qkxBAD0kpxqv_kHL78YDR1hAaGJdqDoZhRtaAMf5V6-KCippL5xoQJ5tAF42BSDGoqZsgwEReeOHmbIQ_v6wH0xMBGQZ_WpLzmKlZDNMDK6XXiFDxRXXNfESYZWS0xvlWYlZ8o45oSXrDbN7RzP8De7IhZvHUXDxqf-WPYicw532lOIFlm68cFC8HM7LRTToKXJwrf8uycNpgGjotRejyWsKOtPfzq3D3rn81eJ7jupcpTR8zKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بعضی وقتا اتفاقات تلخ و سخت باعث تغییر مسیر و زندگی ستاره‌ها میشه...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99532" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99531">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/882a067f73.mp4?token=JP6eYT8E-lrXKXFeeJ1Ukz7wfKacheiZz7PuL-cew932fpwpjyPDlc58Il6e61kbUmsp90CkHnyssg_Omsn3StuFEsag_WDbPAOsYGVsMZfo8eYTyWMH5mI9Z6RAAdQ_E6rdA9p2iOle0mSSLfb48Q_7ruqg6KBFy-zbATQOB7SJNT5wpPGcEbqYgVwP6ahRWGkEEB0SdfdKZQewSUfc5gVHSdBi4rqGuev1e80gmQbrRjjB5tBVkKn6di0b-JHsxUyRCuLXVSrXUExpH272nBINDqjsNSZPxQ3wmYIrflPIBpiXvD4wpQCXspQuiXmIB107sR-rzCEmU9zQSWzV1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/882a067f73.mp4?token=JP6eYT8E-lrXKXFeeJ1Ukz7wfKacheiZz7PuL-cew932fpwpjyPDlc58Il6e61kbUmsp90CkHnyssg_Omsn3StuFEsag_WDbPAOsYGVsMZfo8eYTyWMH5mI9Z6RAAdQ_E6rdA9p2iOle0mSSLfb48Q_7ruqg6KBFy-zbATQOB7SJNT5wpPGcEbqYgVwP6ahRWGkEEB0SdfdKZQewSUfc5gVHSdBi4rqGuev1e80gmQbrRjjB5tBVkKn6di0b-JHsxUyRCuLXVSrXUExpH272nBINDqjsNSZPxQ3wmYIrflPIBpiXvD4wpQCXspQuiXmIB107sR-rzCEmU9zQSWzV1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
ماجرای شماره گرفتن امیر کاظمی از وریا غفوری: رفیقم گفت آخه بی‌شعـ ـور تو وریا غفوری رو نمی‌شناسی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99531" target="_blank">📅 12:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99530">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrPcvoSRcRIL1AImVh1a_9NnLCudK574NQWXKxBLRHwy7keVMOnsWzLNjG-8ODWtDw1K5BBvsHkxhCTwgtpA_V3SYawtkomnpHC2L0Ghj_vg0AUh62uqS5E-X2XzSz98LePq6Z5GJWQK3p7I1mxtp3Uir4YqVX__TKoN5QhDkXkZrCrKAwt_Q2zmanAdfcz-CE2kZ5r7Oor6-b_H8nyrZtv-16YuqcZAvcwv9n96O1QZSOeDdwUF50eHKcGuDvBELoIP-O1jVAOYZZRpQvmdZtqhbZkn0BgUsEY-oKtXvo35HDCbXNIrbbgH3oyUqJNXIrZghFud8sP2TOwILkvHJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
دی‌مارزیو: کورتیس‌جونز هافبک لیورپول مدنظر اینتر قرار گرفته و در صورت انجام این معامله باید رقمی بین ۳۵ تا ۴۰ میلیون یورو به لیورپول پرداخت شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99530" target="_blank">📅 11:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99529">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180
#فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان به‌توافق خوبی با این دو برای تمدید قرارداد رسیده‌اند و با توجه به تعدد وینگرهای ترکیب پرسپولیس، شایعات در این زمینه صحت ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99529" target="_blank">📅 11:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=MNGDntjKq7EgWhZZKFXf1OFvUBDLtNKMBGCZuWqLmNGMqoML5euyoiyjwl4GUVTkqq4zg7ygiUaYleJ9SCv2YqkSUV2qNzkZ8rC3TjjXEDo6oxKR5Fty6LWjtLQxUk8UDSmeGn4jX7oq2MbwOfTVPuWMT6SAxDj2iahk9tPCBkYwIYJrDdxLxnb4kH_ar1z4RjFdFP2q1VFsWYesuofmWHw1rOw_pS_pLn_LM_CY7tXa6gBSu0JQueDlUVCQHsSypWMqV6HX2zwxeIQLBu1soxQn5CExFF9T-UMx7J5znTJAWii8f36Q2xMz_G8e3U6ylIH50_tEPQzOMsE_ofBQPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=MNGDntjKq7EgWhZZKFXf1OFvUBDLtNKMBGCZuWqLmNGMqoML5euyoiyjwl4GUVTkqq4zg7ygiUaYleJ9SCv2YqkSUV2qNzkZ8rC3TjjXEDo6oxKR5Fty6LWjtLQxUk8UDSmeGn4jX7oq2MbwOfTVPuWMT6SAxDj2iahk9tPCBkYwIYJrDdxLxnb4kH_ar1z4RjFdFP2q1VFsWYesuofmWHw1rOw_pS_pLn_LM_CY7tXa6gBSu0JQueDlUVCQHsSypWMqV6HX2zwxeIQLBu1soxQn5CExFF9T-UMx7J5znTJAWii8f36Q2xMz_G8e3U6ylIH50_tEPQzOMsE_ofBQPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
پست جدید صفحه رئال‌مادرید که نوشته شمارش معکوس آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99528" target="_blank">📅 11:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99527">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08f3a463c.mp4?token=vdXGsZLD_fo57WO9kkkAORR__fUvUW2ztYSEjgaW9AngBD16UGOz5o6d8BCWUt5NoQEnjzHnx825ncrBzrS7RVNBbtJiYOU3axPHghhwrP8jvHSbtBAJ7tryb8fgnYidZ7w-Kimyb3xrGlxcdjD770Wwc8-7bFjxkr31H2kD_7yOMds4WMTn_XN4mlM0vEix3MNM2FA2ka8Iy09LSpK6HGtZuA6c3J1A4MELDPTci_bckrvFjEwUuE3E1U0l0QedZN_TvIjg9LsIBbFCdIb-0aCOSTWM5M7_5ZZXxlYRWWfSw4qcLFTjmdEsyUiLGhTSNiulfXkTjLIXADKzgqAzuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08f3a463c.mp4?token=vdXGsZLD_fo57WO9kkkAORR__fUvUW2ztYSEjgaW9AngBD16UGOz5o6d8BCWUt5NoQEnjzHnx825ncrBzrS7RVNBbtJiYOU3axPHghhwrP8jvHSbtBAJ7tryb8fgnYidZ7w-Kimyb3xrGlxcdjD770Wwc8-7bFjxkr31H2kD_7yOMds4WMTn_XN4mlM0vEix3MNM2FA2ka8Iy09LSpK6HGtZuA6c3J1A4MELDPTci_bckrvFjEwUuE3E1U0l0QedZN_TvIjg9LsIBbFCdIb-0aCOSTWM5M7_5ZZXxlYRWWfSw4qcLFTjmdEsyUiLGhTSNiulfXkTjLIXADKzgqAzuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
پشت‌پرده زندگی جادوگر معروف غنایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99527" target="_blank">📅 11:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99526">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4raELVTegc2uvgVC9_SYvJmfN26TgscgvoBBSDAKsRBJPQBSfbthl19G_LPEHL9FKhdLBnHttH26HHGkh97lVQRYO7kWwjNlVktM8qSUi02i30OIE5jNSn8eHlk0GfMze-9fBN7hxrmNadJUwPDvuJ8hhJ9K22-t1j7d7N_YqmW3zjCQUxh3Z2THmTcbYp6QO2L0SDYLRcg-9Sgb_jvoEqYlMrMdgHCcls4S0XaNaZYfqbOmH1AHS-L1VBQXeZiZXVawzotQTuyEvZVjuqx67ruEGTOIHG9kvB-Gc2lMLfP5BHHoPMuJOAA0b8JAKwxi96siK_OsIadaOMQoDypqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
رامین‌رضاییان که برای گذراندن تعطیلات خود به اسپانیا سفر کرده، هیچگونه پیشنهادی از تیم‌های لالیگایی ندارد و صرفا برای ماندن در استقلال خواستار افزایش رقم دستمزدش شده که باید دید هلدینگ‌خلیج‌فارس با درخواست وی موافقت میکند یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99526" target="_blank">📅 11:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c662948346.mp4?token=dlJs5d-nWTTRO-y-FKdrNAS124e2x-Gx7RfMbe_tKI5Nltm6RqK08yZgBWprWJUr2VGQfIaBpyUXGcskD5SO-PCezZzkHQlkXwTHgUpRVvZnN1ueLHVxcXKheVgQCVAQ80gchrJcAFY8XMrIi8gQZuvFEgT8qBrElTQKbUOQ21mo2-lXeZEouRwlAf5bsrxuZSgKMt8P_KlqmoTDMbvj2Bbykcn_h2gW2gSYt6an7-YPgxLPqJONbykHktTXrug4GCjPSyU4g8uOVNGmznimeA2_vAHrTMeRyLHXSUCHiCVmMyatVZ0xnC5CTqoW89mJDGNB33CKX3s2ZlH_HHBZOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c662948346.mp4?token=dlJs5d-nWTTRO-y-FKdrNAS124e2x-Gx7RfMbe_tKI5Nltm6RqK08yZgBWprWJUr2VGQfIaBpyUXGcskD5SO-PCezZzkHQlkXwTHgUpRVvZnN1ueLHVxcXKheVgQCVAQ80gchrJcAFY8XMrIi8gQZuvFEgT8qBrElTQKbUOQ21mo2-lXeZEouRwlAf5bsrxuZSgKMt8P_KlqmoTDMbvj2Bbykcn_h2gW2gSYt6an7-YPgxLPqJONbykHktTXrug4GCjPSyU4g8uOVNGmznimeA2_vAHrTMeRyLHXSUCHiCVmMyatVZ0xnC5CTqoW89mJDGNB33CKX3s2ZlH_HHBZOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی‌پور هم به ۱۰ سانت و ۲۰ سانت معروف قلعه‌نویی کنایه زد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99525" target="_blank">📅 11:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChQaH8x3eAFrFF_yBhhVvVOrAgR8q1v-5h3pk9VHpJezGND1HSVEWRlvaozprVM6Hayt9dOQH5N1AEzYtOOvXWRuLZOp5GA7otZsS9kXisEOnd4JIzfFOovG3VDvhNoKEnQbeX57zfsnbp0YTK_BNoDvJhNeZ-DvpKpkgbRAku9i-76FkRnblxbpQqOtVC4r5ETzOii-mMKguVDjNlBBodhDVSJksUPrqlhVbIGsgGtAC6pW6lYhJh__8P0R-JuewY5-KGiJnndcGU99KWh2rSB2VTPqUyliZ9CxlrxkAoW4bnemD32Aoz11neadYJSDiq8SU-sTxxMErh3e9lpSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
کوین دیبروینه و عیالش در بازی دیشب
🤍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99524" target="_blank">📅 11:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99523">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53dd4678ff.mp4?token=bcjD1mWAnbAHHqGMFDlENVY8Mu_9n-qg6u6bXPBF7NIuBT0ai0biE7vc3za2uZ8RKrn4Za2aTRXsZA0YCCCbA5Y_htMvyXDGTxIfpDHgIobztVBYlA5XzMzPkxI37PVdnPxYzxt9Nd-iK_JMYEewgMI67x3DFQgFVGwA8cthS0AfQufMOF2A8nynOL91ofKbkMQnL1SYdUPz_EzyruwN38Dw_sPAmxIP0mRwGFdmrqPmeL_q1ZqsuFAPn45ZaaDWanEdj2NsAZnMedVcmQfL990hAuUKHvqBZr_edMoT3TulcKqyVAzH6VPZW6EwvQeCzbyMVkSGcfmJeHAMeEWQkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53dd4678ff.mp4?token=bcjD1mWAnbAHHqGMFDlENVY8Mu_9n-qg6u6bXPBF7NIuBT0ai0biE7vc3za2uZ8RKrn4Za2aTRXsZA0YCCCbA5Y_htMvyXDGTxIfpDHgIobztVBYlA5XzMzPkxI37PVdnPxYzxt9Nd-iK_JMYEewgMI67x3DFQgFVGwA8cthS0AfQufMOF2A8nynOL91ofKbkMQnL1SYdUPz_EzyruwN38Dw_sPAmxIP0mRwGFdmrqPmeL_q1ZqsuFAPn45ZaaDWanEdj2NsAZnMedVcmQfL990hAuUKHvqBZr_edMoT3TulcKqyVAzH6VPZW6EwvQeCzbyMVkSGcfmJeHAMeEWQkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
رضا جاودانی استقلالیه یا پرسپولیسی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99523" target="_blank">📅 10:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0798a162.mp4?token=XVPY9ekOQ14HWq40Vd4lVMzsPfi9vuLIcIDo5qD4gCKWrVB3tUCUJa3EI9cEnO7LxcDxKlenNessv7X0knv7pBIWeJS2ZtNyt9RcQszjgjrov9uVoxyfJV24qGINpSsl5Hqu7M6LM723_-DejqkewTgBsjN2SzJsJHGwB68UVmwxIgV8B8Ou7WPZNtf_nL8CDMGFynxMlrVyffLWlndqG2pQWTDhQuTk8h8jVqbjCAoA3icKH3JZp5xds7DqlfXaR9hmJQVlacq7TiohlTsmTP-7gEwnmqGxgwqk2sbVCXaXFSDwtvHBEFausgq6c5OJc1hPkSwPvoUSF8DkDvOA9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0798a162.mp4?token=XVPY9ekOQ14HWq40Vd4lVMzsPfi9vuLIcIDo5qD4gCKWrVB3tUCUJa3EI9cEnO7LxcDxKlenNessv7X0knv7pBIWeJS2ZtNyt9RcQszjgjrov9uVoxyfJV24qGINpSsl5Hqu7M6LM723_-DejqkewTgBsjN2SzJsJHGwB68UVmwxIgV8B8Ou7WPZNtf_nL8CDMGFynxMlrVyffLWlndqG2pQWTDhQuTk8h8jVqbjCAoA3icKH3JZp5xds7DqlfXaR9hmJQVlacq7TiohlTsmTP-7gEwnmqGxgwqk2sbVCXaXFSDwtvHBEFausgq6c5OJc1hPkSwPvoUSF8DkDvOA9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
رقابت بر سر توپ طلا هم امسال خیلی جالب شده.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99522" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
⚠️
شکیل اونیل ستاره سابق بسکتبال NBA مهمان برنامه ناتالی فریدمن بازیگر و مجری آمریکایی شده که برای او پدیکور فوری میده. هرچقدر از سم بودن ۳ دقیقه بگم کمه
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99521" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99520">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🎙
🔵
🔴
جزئیات قاپ زدن علی‌کریمی الماس فوتبال ایران از دست استقلالی‌ها: فتح‌الله زاده به من گفت دزد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99520" target="_blank">📅 09:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99519">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6aa61c60.mp4?token=ud8_GGUhIrhTMy23mm_xqAwW-_PVFfw1enFg0po9ILGGJRnlqikZWuraW2bAHVXVA5au88uWwHEwPPeu4vGRQdVBQI3BQDxEM9fvFBOTP-gkJWAI728E9Yy8TNNHqToJFg-bmEIE7XoZL5rhU7GdJ4EFOb8uj4tl8fs0FCzuIWAV5ZhtT58JJr48mAXh4-F1Qmx8HgrjmSgVyhyoylLdiiI8wGRBtoeVBUBVr5LIrM_yf8I6gdlP0wp2Hwz7B4FPfe2Bgbb2FvKTMc1Z-0BSlzMz0xggMt2D5wB24fQR7VurL7V3p0Xd1pjCcSNiaLLGMHIauxfJfLqg6LRUbYtWzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6aa61c60.mp4?token=ud8_GGUhIrhTMy23mm_xqAwW-_PVFfw1enFg0po9ILGGJRnlqikZWuraW2bAHVXVA5au88uWwHEwPPeu4vGRQdVBQI3BQDxEM9fvFBOTP-gkJWAI728E9Yy8TNNHqToJFg-bmEIE7XoZL5rhU7GdJ4EFOb8uj4tl8fs0FCzuIWAV5ZhtT58JJr48mAXh4-F1Qmx8HgrjmSgVyhyoylLdiiI8wGRBtoeVBUBVr5LIrM_yf8I6gdlP0wp2Hwz7B4FPfe2Bgbb2FvKTMc1Z-0BSlzMz0xggMt2D5wB24fQR7VurL7V3p0Xd1pjCcSNiaLLGMHIauxfJfLqg6LRUbYtWzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
میثاقی دیشب ناینگولان رو آورده بود آنتن زنده که یه لحظه از دستش دررفت تبلیغ شراب کرد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99519" target="_blank">📅 09:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99518">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29484b00cb.mp4?token=S2JY59v1yJgKlez8AMjHjnffvh7yaBof5ez5u6AoLTUwrfAiaOCW3nCPjMUSy-XGy0bLHTQvsc8YkTSKjnlavy-qAoldt0AJ2tI35ynXTr3yl_ae8PJGCh0lnzP0I3KlwlF4eozTCOPrtMCU7aVL5KFe_o5Tk98wZF5GCCKIDLVnLalXKphsXD1TKRqxQeuxLh9tkNkUvozmbEss13JACZd5IvIdhpQ9RfSZWDPnI5eiTRzrLGXMU6d-QQaTXwZg4gHQ3hboKo-G0iiGiufYOw7xkqm_94aTSgCgS7jvoWX4PMVZvjKHmz3qgNnLp7QR4BtJC8Z4NPDrgmTacDB0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29484b00cb.mp4?token=S2JY59v1yJgKlez8AMjHjnffvh7yaBof5ez5u6AoLTUwrfAiaOCW3nCPjMUSy-XGy0bLHTQvsc8YkTSKjnlavy-qAoldt0AJ2tI35ynXTr3yl_ae8PJGCh0lnzP0I3KlwlF4eozTCOPrtMCU7aVL5KFe_o5Tk98wZF5GCCKIDLVnLalXKphsXD1TKRqxQeuxLh9tkNkUvozmbEss13JACZd5IvIdhpQ9RfSZWDPnI5eiTRzrLGXMU6d-QQaTXwZg4gHQ3hboKo-G0iiGiufYOw7xkqm_94aTSgCgS7jvoWX4PMVZvjKHmz3qgNnLp7QR4BtJC8Z4NPDrgmTacDB0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🏆
تکلیف اولین دیدار نیمه نهایی جام جهانی مشخص شد: اسپانیا-فرانسه!
🇪🇸
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99518" target="_blank">📅 09:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99517">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovu4gkPkjRyHC8ttvoTuq0JSBKkMmQ-BrG83v2FP5ndm2wZGvY1WXyP5f4D5fwkCzRvNt2VC_LIxHI8V8grihAm5pouh4UFruhMNApSz87zSq2RCZ0bdQ51kL7jNml5ZaB50IhQ-07LSaxH9JTQw5ln6BetPf7-tM7Dq_e63x-BSHIQaBSA5l21DUC-g8ez4_CC6ZIDdF5gx_l9e_iJaHcTY3xqYU5VQ9j8UFPYo-rWCDODhoxjZX-cBpd3r2nvsyZmHaeVju7i9YAx8cbTuAVhhI1Mn3VMbbDdzojVUjQzQf-zRHSKL5RSnXmxNihLnIYwSKTxrQGRBlRgxZIxCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
نیمار دیشب در تمجید از لامین‌یامال یه کیت با امضای خودش رو به دست ستاره اسپانیا رسوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99517" target="_blank">📅 08:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99516">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f60623d0f.mp4?token=Ou-H-ugxpNk_JMhM_By6RPi2W8os0Is0uatYGTqCPgUWHNuxNQsIgUkrdITPI1J1auWjUq4ddnrB5YojSQ0ZUdRJRvyTp4j9oMvVtC-EKRunrhjYcWXL3-H_JfX9QayNzLfIijJdroFXVYCmmbKYaVSd6XlaoYugZiBXYGYpt5o9O5Ju1k4LCec8WNgfwtyMcO9TheXnd55DkbqstwYKrbFpls5j70PFyKCySbfzXfCTeZSLqtGPA1VAxZw7Pe9-Wrc5laAhPGA9W27VZ8fGBuj29qLR1uR6GXAikPPgF-vQT9YVdW1mLM7ErHwDC2m6EJtfY3eIiZP88GYfnAwtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f60623d0f.mp4?token=Ou-H-ugxpNk_JMhM_By6RPi2W8os0Is0uatYGTqCPgUWHNuxNQsIgUkrdITPI1J1auWjUq4ddnrB5YojSQ0ZUdRJRvyTp4j9oMvVtC-EKRunrhjYcWXL3-H_JfX9QayNzLfIijJdroFXVYCmmbKYaVSd6XlaoYugZiBXYGYpt5o9O5Ju1k4LCec8WNgfwtyMcO9TheXnd55DkbqstwYKrbFpls5j70PFyKCySbfzXfCTeZSLqtGPA1VAxZw7Pe9-Wrc5laAhPGA9W27VZ8fGBuj29qLR1uR6GXAikPPgF-vQT9YVdW1mLM7ErHwDC2m6EJtfY3eIiZP88GYfnAwtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
آغوش گرم لامین‌یامال و تیبو کورتوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99516" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99515">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99515" target="_blank">📅 03:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99514">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi2xn7TvFn-e8-j7tzPg_43W8UV0G_5gpRwzDxAnye7eWV5VOe2WZB2pxe9ImUwzLOoTAQm_-rk_yALN3VobD6vFFqc9nOKICLOIqDkcD2P8-fZu3efPxb7JFqccweJ4gt8WNdV8hWRz7jlLDXtp1Mbh4tuFhfNzGizBevGYufMeuEDpkxRLpVyJEwYO9ZJ08q7lPC1A9rnVLMxp3z6KT2oBh4ekvX4Pn99_I4a_H7kx_-IXP45O_A3BZWNeB9Su0kUxmycKtFiBOClpRabt1MV9g5yHbEVj5Z7mLYLgSAhYgGVQvUkcvbdZyXzWLujyQgewhIZOeBnUssAEMUVzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/99514" target="_blank">📅 03:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99512">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfNx7ANWIxc7-LQJuVidzlUbw432kkw1FeeFRackU15ymPtsxVDgQd0nPaAn34mCBPrfCUESjpzKVDzgRxd1tIIOtdpyMpwWTYJhzCEKEiK54cTznZsI8U7AYkD_eVDthbo1lfZT-aY8NbPBzaTrCk9Mn9X88xTi-2ua0mWJg2RC6ur7OfJ8cRDaFegq32y7Vk2sNvSBHQCqBNeYwmmI4SExtIAYsUIc-ECIqA3utfYheupl15zccaw1BbiO2Z-0onuggPWLCiIQfsO5XB-WKmY_EUd2RciCjUX1u9gOgejix94m1E2zw-CqVOSsZTeQrLU0R7l7Mi_KpPHVD_tJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
رومانو:
پاریس سن ژرمن به شدت به جذب فران تورس علاقه‌منده و اونو برای جایگزینی گونزالو راموس زیر نظر داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/99512" target="_blank">📅 03:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99511">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pziDmPVadVDxwSCuJi86xylSPw9yNp5jX7jeCvdTQ3j58xePPXgOnEoubb2J21Z3fXAgQAxoH-TMF2xvTPWEm0aEGNoxWnZddOU9rH4HQP1SpFaQbdUzU0gZpc1RzaTZVvlG6-cBFJQ4heKz0220yBaOUQw87dniZURg4uwBy1oVldKo_9m5CZ4SFV5D-EUd5eb2bdLckT9q6ySNBK5whrZKo81B81AX_zHktSsBooTKiQDCMgHYVoIBUA-ZTs38HL3VitEu0ibiplP_4FJ0VH7Bn672DrJSTXhPqNpiNfN-8a5CziCWgELdlg8ig5D9tmMNQhUEjm7xcJMb5aK2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند پیش زیدی بوده که یکی یواشکی میخواسته ازشون عکس و فیلم بگیره بعد هالند زودتر طرفو دیده و از یارو و زنش عکس گرفته گذاشته استوری و نوشته هی یو
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/99511" target="_blank">📅 03:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99510">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=Qr9uFYepKtEmtEhTL9gXwvUUWA3VIScJUEF4pvS78-k0AJhr6NUxSIrCBRiT46-CiRzd1lUqzsxyTlu9TU6zA3jIbBlDsSzPKe-BmCp0jeBRT-t4HtOSiaKyNEfr7dVs3Cnb2x-63pg1Ry_KLmljD0G9jOS_QlWbGLoeYXgt3YAE44dJxcDpGkucpJZDX0RTOF8msxvp9q0kJWEtI-KwN-tf5n2B7WKYjdDgS6JY0p2FDGdtN7GX10lUQVnuF2esFV4xMcGyo9O6fxK663qefR1mGIEhCm0dwbHs_B6WRCeJKPaqENhCsCm9fmeDL6X75Rypk4-lsc5jJEdh4lA1pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=Qr9uFYepKtEmtEhTL9gXwvUUWA3VIScJUEF4pvS78-k0AJhr6NUxSIrCBRiT46-CiRzd1lUqzsxyTlu9TU6zA3jIbBlDsSzPKe-BmCp0jeBRT-t4HtOSiaKyNEfr7dVs3Cnb2x-63pg1Ry_KLmljD0G9jOS_QlWbGLoeYXgt3YAE44dJxcDpGkucpJZDX0RTOF8msxvp9q0kJWEtI-KwN-tf5n2B7WKYjdDgS6JY0p2FDGdtN7GX10lUQVnuF2esFV4xMcGyo9O6fxK663qefR1mGIEhCm0dwbHs_B6WRCeJKPaqENhCsCm9fmeDL6X75Rypk4-lsc5jJEdh4lA1pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
گاهی پایان، با یک سوت آغاز می‌شود...
🔻
امشب فقط بلژیک حذف نشد؛ آخرین جام جهانی نسلی به پایان رسید که سال‌ها از آن به عنوان «نسل طلایی» یاد می‌شد. نسلی با ستاره‌هایی مثل کوین دی‌بروینه، روملو لوکاکو، تیبو کورتوا و اکسل ویتسل؛ تیمی که روی کاغذ، توانایی فتح دنیا را داشت اما بدون حتی یک جام بزرگ، صحنه را ترک می‌کند.
🔻
سال‌ها امید ساختند، لحظه‌های فراموش‌نشدنی خلق کردند و بلژیک را به جمع قدرت‌های فوتبال رساندند، اما جامی که شایسته‌اش بودند، هیچ‌وقت به دستانشان نرسید. اما بعضی نسل‌ها با جام‌ها به یاد آورده نمی‌شوند؛ با خاطرات، با احترام و با تأثیری که برای همیشه در تاریخ فوتبال بر جای می‌گذارند.
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99510" target="_blank">📅 02:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99509">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN1Uff_9ILyiPEo7cw8ujHxsAYOIm22Jrz6Q2jXqKzuy5pHE5y2TacdxG7sJs1KqnUn7KrE0IADmk-O41bjodp9h9Z97_RW-98Mdhw3HCBZMmESU2_QFD9-5AlQ6JCCqNN_cqr1eIg6oEHQtZhcBC4utxJsODxM6-hIw94s3cfwngqahL9YUzbp6eHcZ7hkqHnrG1t_Ep8KvEkq9zlbLLMhWNR5-PZX3pIMH1kUk8sOUs76Qc6Nji6_2IcWwglR9MmG67aZU4aoGdisdpWAgh2YXL3odNSXNWGa24yeVl5Tipa2U1V6FU24prXMV9Y-3QorXi_gC3Ec6EB3P-3IJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/99509" target="_blank">📅 01:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99508">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99508" target="_blank">📅 01:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99507">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl9snllZUUePjLsclFdwdvSXXhz1b-3wIudxBcVbCHPA76DE2dR1Y6yriWc2IFfGKaLxLuCY5ry5RvHxzHClvG3YVNvTS70MM_p4qxhXOpplyrOuAefn2G2EyHED3sfYzbTl648002iQytrlrfE7wkcZYggx8P0Qnm-vvoKjsp5bhPujV__iRWUDUYD2lFzPbTYZnUJdSXKlGml0aPEbO4HEHbgCkS039_i0DHuzjpO4xCAcTaitvnN2KTvxggwZx7Kd1KXoihU8tzGDQo_NumFsaGAJ5_SbXpnCYiB44IYqUkE4pZw4Q-Jtu68bEZRSnF38LLC-xKFMPnLl6iV7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
16 سال پیش تو چنین روزی اسپانیا با شکست دادن هلند قهرمان جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/99507" target="_blank">📅 01:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99506">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLXN0HoXo9pLliHkqLdaEj8sK4HDbQCDVa-l7T1pBadMe_hvnz-ZnUDXg2DQLvBk54GQeVcadcSagl_mXzTWwa-FsqGesYecw3WjRZL0NbC4lM-_2nmQHizXfhG-HdimxI2StGXBMcIxe55xaf7e0OCip3UryzLA_UtIbaO5pL5yj2aXN6zpJdsm-LEZ07gOVsUMkrV5wRQi24_smt4hjoIm7xKPf8qqemP-FPCiHvxPzhmfIdV7XsisdL6efTJMfbNEMKB1MRA_DXcbYt56LPjka7A1_kDmqCzQYRpRM1-rSqjBc8o6Paiq5HhpEUd0fonoeijwXD_WDiO_YwLbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇧🇪
تیبو کورتوآ: «می‌خواهم یک سال کامل استراحت کنم و در هیچ مسابقه‌ای با تیم ملی بلژیک شرکت نکنم، و سپس در مسابقات مقدماتی جام ملت‌های اروپا و خود جام ملت‌های اروپا در سال ۲۰۲۸ شرکت کنم. نمی‌دانم که آیا بلژیک با این موضوع موافقت خواهد کرد یا خیر.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99506" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99505">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm_E1hxn6MrrYhYfu1tGX38mg5Itoz0eMhxmtAJcX3EJSOoylTQE0rra_EPYSBC1RHqHsK2bz2Gs-xoRPQ-wYNHIcFGsWsLTUIc0rnhY6jzAhHCBw4dRI5GQMuPRwOPhGuEBQugRrJ_O6scVur92Dc05hhfiv6HOs9OKGjD67CKZLiAWHnqAFNXaPyPTtRAjiTOgeYVAdqYMWsznKXephL-voqHcmZqsCJzEuv64zrWIQrB3uBhCScgw4RS6C0OQi9NJm4BT4IY8VDK4sHjzLWS8GIxeIskcpciLVtJC2Nn1RZjLP5ROXcc1oKmnH-ZNbVXAd1f96NtLnidxppGQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🚨
🔥
🚨
🔥
🇫🇷
🇪🇸
لامین یامال:
‏فرانسه یا برای بار سوم متوالی به مرحله فینال جام جهانی می‌رسد، یا ما آن‌ها را برای بار سوم متوالی شکست خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99505" target="_blank">📅 01:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99503">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
💔
💔
اشک های تیبو کورتوآ پس از تعویض در دیدار بلژیک مقابل اسپانیا به دلیل مصدومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99503" target="_blank">📅 01:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99502">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqpNpKAT04G9W2yWGC95yAwcvfvDx7Q7EX7OaTJGXLcfW4IFUJt57OnttByk3Eyyjrwe7soxNJMi5znIIeIhMQ1eXD1w7g-N_TgFRiRIeX94uVYn0UCl6Bwu3SxsdelfAsgcRPH1yyhnyueL1i3b_bWUSLhdTkHuRIhJ0D_M1JfOIes05fahsfigqKOYwATPuzLjHl2irgzQ8Y0J-rLN-xO7wUKUa-8qM8mzQ-b5uy7ebo7X0vhu9Mw7VMyHT0VtWlE0Wf1pTaYpClBxEpM8b10vvT0W9QG3zyszPoIwW5pzHvDk2ZGeAeQPe7opam4wiI8n6m9rkgIvrgwhGKf1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🎙
استارت رجزخوانی لامین یامال: « فکر می‌کنم اگر فرانسه قرار باشه از تیمی بترسه، آن تیم ما هستیم ، چون این ما بودیم که آن‌ها را حذف کردیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/99502" target="_blank">📅 01:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99501">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961be455f.mp4?token=dEu72Oa7R5uEig2mw7uQelQPnnWEyHJ3fvuoqw8x7ooAG3UpYkJphtkuCgQfiCupdjYQ-J_NrI69nl3Pe_MVKvWU0s5ftaIRnk7eq1XVDjYlwEeW_GuTInSvtvbeq98GWs_JLN4sWzAaeCbOJL5C6Q2RvAnPqRCSHrsOYnCTiuMLLa6_UT_6N1QqgIhjDLqPmagupv0DesUQpjbD76WIDEPvFchrsTuS9wFGWiTh-FLuhhsOs7RKRC6lP-P2LGsHFtaqi6gySQSdjD2XHCzwoC6Z7lX3yrb3RvHdUu6IIywY244WSYPTudoRvNO95P6UnrhKuWqYZj1Mpd9RIxuT4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961be455f.mp4?token=dEu72Oa7R5uEig2mw7uQelQPnnWEyHJ3fvuoqw8x7ooAG3UpYkJphtkuCgQfiCupdjYQ-J_NrI69nl3Pe_MVKvWU0s5ftaIRnk7eq1XVDjYlwEeW_GuTInSvtvbeq98GWs_JLN4sWzAaeCbOJL5C6Q2RvAnPqRCSHrsOYnCTiuMLLa6_UT_6N1QqgIhjDLqPmagupv0DesUQpjbD76WIDEPvFchrsTuS9wFGWiTh-FLuhhsOs7RKRC6lP-P2LGsHFtaqi6gySQSdjD2XHCzwoC6Z7lX3yrb3RvHdUu6IIywY244WSYPTudoRvNO95P6UnrhKuWqYZj1Mpd9RIxuT4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال چرا اینجوری میکنه
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/99501" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99500">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=S14J4m3IIfErTXe6_6TN9BBHLuJGa0nM29QuLhhl7hJHeg1LhUvd2VtpM-LogPgR0wHBkVLYbSm3mi5HhXA1o1DZuadq1WZlu8SGqbDHexXYpnxnnwrgXsSsC2tn99DM7wRIdN2tvd6a39OMz0iL1INKYoQyMS2z3xHCkKV1uLNkHIh8P2_15StNeKYHmA3125_I3DoM4P1BTQ6fBnv_7cMGhhxzbUQXWJyy1LZ4QM5NqOu0F479GkY-I_rS0XCo3obTEd76ELNN6YsS3Sqsrx27hUWSJa8w43RLPfqG8cH-JhNYszLX0_UcjucAvsgjHPk1j_nzEFdSXOz-q9p-JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=S14J4m3IIfErTXe6_6TN9BBHLuJGa0nM29QuLhhl7hJHeg1LhUvd2VtpM-LogPgR0wHBkVLYbSm3mi5HhXA1o1DZuadq1WZlu8SGqbDHexXYpnxnnwrgXsSsC2tn99DM7wRIdN2tvd6a39OMz0iL1INKYoQyMS2z3xHCkKV1uLNkHIh8P2_15StNeKYHmA3125_I3DoM4P1BTQ6fBnv_7cMGhhxzbUQXWJyy1LZ4QM5NqOu0F479GkY-I_rS0XCo3obTEd76ELNN6YsS3Sqsrx27hUWSJa8w43RLPfqG8cH-JhNYszLX0_UcjucAvsgjHPk1j_nzEFdSXOz-q9p-JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
MOTM
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99500" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99499">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG3hGOt6vt2ATwBWqHA6PwyQcmQrPit-5CfjDvEvs-GM_K5N50vmtpb1JCX0LRCx0jeigtP1QsgRMSn6JIBXGrvlCLPKhyaK7WIUyGtbt3VZt1s-Q3SwWBtQ_yyfX7uijB3F8tu2h-wCy8a_OjGU5RQ4k7PL7FTyI8HNXv6lFZ6YCaLqQ-DoGTjj49_dETF5FhC1VSM5ljEo6CRtL6xWlnrIo_w51sjHv5JIp8VHhsITGzq_eEvinTp7x1We0cl3PiKWi9uZXa1LiDy3AOdxvJlxGZFjW3tVYESdhIy19WYjNqW7DM0jFTBzbAnT-mnyIuk_rZKjDbGYHxHx4bntyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🤯
🇪🇸
فابیان رویز تا به امروز هیچ مسابقه‌ای را با پیراهن تیم ملی اسپانیا نباخته است:
‏
📊
48 مسابقه؛ 33 پیروزی؛  15 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99499" target="_blank">📅 00:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99498">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📊
🇪🇸
مرينو در دو بازی آخر در جام جهانی:
🇵🇹
در دقایق پایانی بازی مقابل پرتغال، او یک گل زد و باعث شد اسپانیا به دور یک‌چهارم نهایی راه پیدا کند.
🇧🇪
همچنین، در 5 دقیقه پایانی بازی مقابل بلژیک، او یک گل زد و اسپانیا به نیمه‌نهایی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99498" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99497">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQw9-x08b7-dzCEsaYxfWP3vV8-lj_xKmH3Q3_oq77AHVfSYtGUWWq88xq8fW5AWtUS9PGLwvmvGy0TytnnaWHHfs03r9nQ0nCxF6Symn9vRRF2M4Lr3Q17ewAWiq4WWa2uNiriDdqmhCgQ11QaqVhb6sTkaZS2nBbNqDmRhhxhvOU-cUMmrS7kao36EBQnPaaACqIog9V78A4y0N_mrNhHSXdbnoNb6np7rNXk31lZ5j8rArKbTBG4XriIolEj-s7gd1_gkE_rg-O3sLO5rv3LGya8qUtZYxe-VNgR3i7PfoXx3jkSQywMMiILpF0C87yCd0NsvewLLS9VldOGQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
اسپانیا با پیروزی در این مسابقه، برای 36 بازی متوالی، بدون شکست باقی ماند و یک رکورد جدید در تاریخ این تیم را به ثبت رساند.
✔️
‏آمار این روند: ‏27 برد؛ ‏9 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99497" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99496">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99496" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99496" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99495">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GU-DRcnGFGTWsBum_XP8hMZUWx9Hi3PNjQ3Lo5BGZXjSIir_6ajzRESaRRuyY-nIZgwje2TRgLA0nCQvFZzn0IlextctdX82w8D7DxuSUYCdP8d2Z-Afw0gdE6qoBm16ONOvf41IwEYHKj53Gtp5s5GNAomqTKwiAY93J7nU1a7xf4oxrHpgx8nfujQg8lA8_uDYui4KgNb7lzVGwup-e4okQOKog6T20EMx8_Syb1fVKvx4H-m_hO_Kep1Q1DiLnx4Bcixcc-q2tz6VV9RnwF1sscHlmn5R8Z2jJhTXFxCan4-MAM4jV7ahdSLNsM1MUXnnU2WtSw20-E5nluAydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99495" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99494">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX_z5giJKQyhdZGs7tptq8GKq0yL6tS9fRcCrJaS7KGfm90OZH2MMqqapDncr1n1jC2xNu991MAX5-P2U0jQMxjCelbGExql-AdTwkbu839-5vw10DlcGmjqi1q_Tz9dL7urvHMu1Yfh0gqWTG26gvf_MX_8Za9PmsJTL9IrKHJ7rkuMSOLz8gbf63SXnX8mJXcJNoLVj5wTED0TC0zF4-1Z_dDYdTJIUq95hMpy57MD08Fdp9cfqVgRSszA5ZTs9HBXn0pLnv_BWhf-rh1TMd12cvRohq-ILdaZcKBGOxbn8quBud5AqBwLCpsPAdBoHSCRu1mQsLgbKEJ3iPLcBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
در 11 بازی اخیر که لامین یامال از ابتدا در ترکیب اصلی تیم ملی اسپانیا حضور داشته، اسپانیا در مسابقات بزرگ (یورو + جام جهانی) پیروز شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99494" target="_blank">📅 00:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99493">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ دکلان‌رایس، مارک‌گهی و ریس جیمز در آستانه بازی با نروژ به تمرینات انگلیس بازگشتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99493" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99492">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ19yw9IwsLO3utvqpr4QfNfeqIF_iihLC5h6FLyiOrQV-4OaTQMU1B3IpJ_5RnSA4iwaoC6ZEZZ6bcFKgnYJHI7KqIRviZPv2EURIH9an7cMhg3okRMsaVwufBxVkwG2bs85A7qaOmoRHBun_iut3nrYJ2l-42ULkIlOCncNeCojQCMiQUNC14rmVdLDmZ9R6t9rimtoaIX_yUDl9P_6a27UBuYWpf-Ezihupi_1Ma3SRQCPAPzEGsn3Iwd1fTdWX6mkQxKGwzMTmMcr0SemG1cCcWRt7G76DJUq4klpYAznDL6i6TaNCpyrred_iu27g0lyKBTXS5MyuM7Pnq7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مرينو در دو بازی آخر در جام جهانی:
🇵🇹
در دقایق پایانی بازی مقابل پرتغال، او یک گل زد و باعث شد اسپانیا به دور یک‌چهارم نهایی راه پیدا کند.
🇧🇪
همچنین، در 5 دقیقه پایانی بازی مقابل بلژیک، او یک گل زد و اسپانیا به نیمه‌نهایی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99492" target="_blank">📅 00:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99491">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMQKsjuyVGVF8_EvhXJFkq9FC1EAWwAoDgvkHO7tacW0fX5emuDzEeRk7zj6F6ahOi711m6erZjCBKxhfO6OYIO73KAQvCUZjkAs3PasY4_7ZO6l2PO4Az8ri0YaQY1Iwtq_r4jpSsNpdNgVMdoIcH8EHGm-NT3O5rPPkD0WA5ED_DwLskun9zFRpa598WVcqJwYsXPZkVfHG3Q3iYqZKF4GXbP2mVZ0MSXmp5HVWu4OmCU5zwMV2pz_YiAhcXAXXK98XXh2M7COqPJB7tBMxL53VZjaWgmJQWpuxu3qm200blDdeyPQhcy7lzornYvuLkwL7pgg34JGoJxNDwIZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا پس از سال 2010 برای دومین بار در تاریخ به نیمه نهایی جام جهانی رسید
‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99491" target="_blank">📅 00:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99489">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgDAG3PTGCUZ_Vh-uvow4eElQdWdcTRRhMPjI74W8TXrAffCFBM2ktPKXtegv1XHIwwoFk_CsQm-cLI_iQscdcNHsTVJPy14jPWA-RukdwG_HaN1RjHsuriUFUI5tlIK-lEGg80kKIwmrAirdnJ4Jgtve1Cz5qRTJ_8r_nm1q6BxLInfxOw5cksXa54Aui38zJQ2A0wt_6F87mtaxtbnGI9xiVB2bZJG7v0WtJ1B6S6KUuHlzMfIBdz_Jr3B42hZOp8kBHkCbIshI5PBki4D7t_3nRSK_8x_mqF0u-CeB_GrUpW-LAnZyeDn--iBT9A3xkatGUD2ix_hSb3oIkUNQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYCHNfrFSuAeGZNdBK37iPn-DIFkWZQW2IznPEZKu3CriJTkO2vCvEsRvIsomFZ3Mxk1tmGjK3uBazns-m2gpeRJ8msU0gr_1Gl-aFgyNWX1DUuk0XMUXmNbYZOkm1cPRKU8I-IGM9K4TXgx6tl8RlyzYJChF2wBoNl7BrW7xU_jheYe5vwoyS7ZaRKA1C2v8v31NF9bQ5Vd3UDGQN55Uvztvd1x_jGCOG2OlGyy6bilwTUQs5yonqGqofmVPStJkNgmz1yC-62GJOSBEB0XZgNYj29obHrO_7boX1sWuEWTcfuXNfjX3kLC9nrGCD1I5HCcffmeWzl1WzFXoTBerg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داش یامال تو استادیوم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99489" target="_blank">📅 00:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99487">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNG2DCaVWykovAbN7cPRyO8Hax8zN3kZWPxHQjB77bGOs1OJDOUzdZOOHEITmWcTu03z3V0qByLdoSJSyVv582EjSeRsNgRIRzIPjzZ-F7RQxb76wCLVRg9CScfFAP2dUDCviYimL15gNxj7rlZDsCVvl1gh6M8pLyj8vRgraLR2p8-RMCGnnyg83LmZuSqUb1YD_WymPPepNtHq7_xxuoTkkY-cpXgKnP-0cnIQln8NgK3AIZvJmqGH-pnIj4Yq8ObLdzhvHWmvgihGEXfpt1fwNX4o-WRsTDfeOy_a-NIEnd1R_jVsCeaQRwlGGEiuUSm4_nQJFEiTAdAqpetkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
🏆
🇪🇸
آمار بازی امشب بلژیک و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99487" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99486">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlFRcyEcDwCxBw0qRATnYsiLpAOqy2-VJob8NIXE_P4DRok9mT-z-lBTj0QgPn00-dfbstiI_yWcSoy-OkuLCopRwWMDVqYnPovwHTtt5I_P5jLjMk-QSukSwhg1l6jNLM1USuIkR0G0KVcwmGWzTJNbuinTtfZYOM_gDIxfL7jXEe9YYnSJ63tgyRqIT7PE-IXnHf7DRBV4YSzDooART7JXsMRRreMOrogOeM-ne01naLHDPEj89iYjCWFIeNVScvCW5H_rzx6LCrE1BWbF_0E440oex4oTOV-_w_eI7HduvnJiOdOFmzmxPTmgcMU07WA9RmD76fq8hpqQXqFabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار جام جهانی؛ این سمت که واقعا جذاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99486" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99485">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMiqiM3_vH1szlnH36JHBKnnWhK6xQTy5fcGQhm3TRyXzqJ66G8tw87zUbBKB2-LoRcYOw-7d8NBcB00KBSoREESYTEuAu0bZhYJRxcGIKkHUaDU6cQZPlgoG5BjoGY2KW7xo2_TmQBjEvnMWIfZoX417IBTCRo1UxUOvLG5bb2Ls5U5-tJhClVaxSXqMdNuGCJ9C2r3ljfltwYtcLjJIBhbdSwUJsSGbd4tLIOO5QRjN8oib4Z5tb2PLy5juMLr1E2XWeOjEhsQF9oVTmDjU0wtGvrzDARukE7FvqP8nxeNi0wAm5rc9iy9fGfh4Uadj5Y19l07Qc5xmdRqjvws7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|داستان اسپانیا در جام‌جهانی همچنان ادامه دارد؛ راوی قصه ستاره آرسنال است! بلژیک در کمال شایستگی حذف شد
🇧🇪
بلژیک
😃
😀
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99485" target="_blank">📅 00:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99484">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXI9CsYu70PHEym7mnEy3Z0N3w8jmxVPVheVOOKBgvLBx7UYz4m-bWEXCppQT_nkASzKJPoFWW7uEGeMwd7HiW0ArqMafemmZucYf4QfQ0DxTDAKnHtK0cDv1JaF-ittXr7xL5otnxzL0HzWYsUiB38G6bYqFh0vR0_lqUMIPxxmCzJNBRCuLTljkQuXF-P12kMtz4vVfutdbcEAzVtwFu_YXUn4pE1R20SDvKCLz7ht3hx7dveopEnrnyBmeEDFr-R9GmRyDn1TC2EYorvg9UvKaiqf40-yxAde3KY41ZUE71wpyECE2nufUFZpJRodiHCVeEAceO8Prb30TTCS-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99484" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99483">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHO1G1gLpUG7IeHU5T5j4ckzf0T1VlVoSPsFiD9VYagtIruUzdOYGbyzI5vhqBKTn4cvfrsqoYHwlyeiYnLPl0kqMtJ_hBVOGQgfJGPwMut0uq8J4WY5bLJzD9LD2zq_0ghZBwwXRM0DZoycuBQ71-q5cqTsnIASGJFq19P6iGIbZGqBcnmV7k_UTr3YYoiiV9MolZxRheyITTL_3fq1P4n0RaGbGRLTaMRAyuywAUwYq9MBEvcc5j1Fx0OWD6nHPP5L2UtD2Atss0an3w2Y9c2UrvNGSCiP1WhEqE8KoKdgEKSlnrvMZwkKlwTycP9IH49MMGexWVi3jUL2v8ao5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|داستان اسپانیا در جام‌جهانی همچنان ادامه دارد؛ راوی قصه ستاره آرسنال است! بلژیک در کمال شایستگی حذف شد
🇧🇪
بلژیک
😃
😀
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99483" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99482">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پدری ریدددددد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99482" target="_blank">📅 00:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99481">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چه توپییییی در آورد لاپورتتتتتتتت</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99481" target="_blank">📅 00:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99480">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99480" target="_blank">📅 00:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99479">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هفتتتتت دقیقه فقط تا پایان</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99479" target="_blank">📅 00:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99478">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بلژیک اونجایی که کورتوا مصدوم شد بازیو باخت</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99478" target="_blank">📅 00:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99477">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4b3fe7a64.mp4?token=PtjeS38ETg7GFwUek9gDST3nlTl9nHfyFfhFdGnPrQgFhAUq-EzP1KeyVR_HbQY3SS2hY-wWjQyK6sUON-MmOKrDX2Rh3qQFAVfuhUXolB6NiESQIwF5PwdIboEV7palqwSlLXA8Vy40bMPkWP89BZGwBxCTxDF1kV8KvNhqOcZMsujN9rFYnZOZEHMSrHf2EXDy2khA_lwstc5Q0gm_YpVHOVqRqgkZO8M55-Y83MRAkv1kfR70-edW-g3P3KfBt-Fek-2OWLrOGLCGuGIqlh2y-TeDFQdcegGOudUGQk7T9Ru9-tIe54oNR0tC8gJzYr1Nldx5GTY9LXOEyq9b1RLtaZNkn_zVmJr5stft-znRC3ugD15Em5NCgrGo_cE5EU9O9HqwWqQipiAhNoV9rbi_pl1GdNdEdcyK6Ym1Y1vdWO-PAbj5qMCfnIVLIRda7CJCKgx-ckCKx4LdfUNvjKaOC8616CjRGf1DqwPk4EaC1k68EGZ_aqu6oGwBtDCOGmqvQnaMeIWEvxCoEDHoChW__2c3oNoPiqHyENz_en7e1-g2pQYWjV5BUDQxhgAiHljIgH0K5AyYyXO4LLWey8R6AsBOt9wxVDVrJ_iEG2DvvvTecI7BH2gPe4o_gMvnhTT_deKdqgKmAiZEbdWIi_AGMbeYl04W9yrGui7Cs4I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4b3fe7a64.mp4?token=PtjeS38ETg7GFwUek9gDST3nlTl9nHfyFfhFdGnPrQgFhAUq-EzP1KeyVR_HbQY3SS2hY-wWjQyK6sUON-MmOKrDX2Rh3qQFAVfuhUXolB6NiESQIwF5PwdIboEV7palqwSlLXA8Vy40bMPkWP89BZGwBxCTxDF1kV8KvNhqOcZMsujN9rFYnZOZEHMSrHf2EXDy2khA_lwstc5Q0gm_YpVHOVqRqgkZO8M55-Y83MRAkv1kfR70-edW-g3P3KfBt-Fek-2OWLrOGLCGuGIqlh2y-TeDFQdcegGOudUGQk7T9Ru9-tIe54oNR0tC8gJzYr1Nldx5GTY9LXOEyq9b1RLtaZNkn_zVmJr5stft-znRC3ugD15Em5NCgrGo_cE5EU9O9HqwWqQipiAhNoV9rbi_pl1GdNdEdcyK6Ym1Y1vdWO-PAbj5qMCfnIVLIRda7CJCKgx-ckCKx4LdfUNvjKaOC8616CjRGf1DqwPk4EaC1k68EGZ_aqu6oGwBtDCOGmqvQnaMeIWEvxCoEDHoChW__2c3oNoPiqHyENz_en7e1-g2pQYWjV5BUDQxhgAiHljIgH0K5AyYyXO4LLWey8R6AsBOt9wxVDVrJ_iEG2DvvvTecI7BH2gPe4o_gMvnhTT_deKdqgKmAiZEbdWIi_AGMbeYl04W9yrGui7Cs4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌دوم اسپانیا به بلژیک توسط مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99477" target="_blank">📅 00:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99476">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مرینو عشققققققق</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99476" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99475">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چه شاهکاریه این مرینوووووو</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99475" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99474">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلگلگگلگلگلگلگلگلگلگلگلگللللللللللللللللل</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99474" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99473">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گلگلگگلگلگلگلگلگلگلگلگللللل</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99473" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99472">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گل دومممممممممم</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99472" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99471">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسپانیااااااااا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99471" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99470">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مرینوووووووو</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99470" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99469">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گللللللللللللل دوممم</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99469" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99468">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99468" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99467">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مرینو عشق پرتغالیا اومد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99467" target="_blank">📅 00:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99466">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6497dfae.mp4?token=S874iBUGgXqWQOVZ6QJpelXRx5ywsBAqOeMSdLQQVHUu1_WA_VVJrUcpxmxatMwzBZ4W8bxoqI9KGDL831fGj9zPrkJnuZzFduXe0vB5i6dIx4E9qmxF0thZO-xcEq0K6wjJGGe3caCUdu9UHSiy12X6xVtsLT1uWw_Gs9HE-VSZ3DDHHwhTnAne5ODOJGrehwIv6bYHzOG4S-lw_kjvuHv3HXClatX-jlWMTj844d59mnuf_inaHL-DB_ENjrualT-sC4jp3A3SXIYo5EXAcNU7R1UEoNlC-3XgqvBblGcbUycafs1t2rT5IKbBtioPff-DUZ-PbHYP_gThM9sZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6497dfae.mp4?token=S874iBUGgXqWQOVZ6QJpelXRx5ywsBAqOeMSdLQQVHUu1_WA_VVJrUcpxmxatMwzBZ4W8bxoqI9KGDL831fGj9zPrkJnuZzFduXe0vB5i6dIx4E9qmxF0thZO-xcEq0K6wjJGGe3caCUdu9UHSiy12X6xVtsLT1uWw_Gs9HE-VSZ3DDHHwhTnAne5ODOJGrehwIv6bYHzOG4S-lw_kjvuHv3HXClatX-jlWMTj844d59mnuf_inaHL-DB_ENjrualT-sC4jp3A3SXIYo5EXAcNU7R1UEoNlC-3XgqvBblGcbUycafs1t2rT5IKbBtioPff-DUZ-PbHYP_gThM9sZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
💔
💔
اشک های تیبو کورتوآ پس از تعویض در دیدار بلژیک مقابل اسپانیا به دلیل مصدومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99466" target="_blank">📅 00:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99465">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0c-FrgS-StytFTc-0gSQio5aFW0nxi0LByFpBGQTVmXcGHlFRx_wbDldWIQFYm1dysmeNrHUDsl6-LZ06aFV8UC6piaGoX8ylaIzI3nkZTPJWqsULQcn7RGZ9NmlONIt-3KL5zHAgQpm2yZdqKd8c-vHf_mUJC9ca8xsNyvZiSJvNm2_ma6Hlf32JkC7dkerojTqM_B8nuUgaLd9rHuDDqPkaVg8eO3JaLaX0rGSUEONpkW-4FLA6X0YU-UHOJRPckg4Ow1g5CycSMKHkTN8rrDHllJQjFVNu-Eskx8qp0-35jfYWarsoJN96TRDdxXO--flpEJo863Z1YsT9HRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گریه‌های شدید تیبو کورتوا
🚨
🚨
🚨
🚨
😐</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99465" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99464">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کورتوا تعویض شدددددد
😐
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99464" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99463">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دو تیم خوب بازی میکنن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99463" target="_blank">📅 23:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99462">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بلژیک چه ضدحمله هایی میزنه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99462" target="_blank">📅 23:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99461">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آغاز نیمه‌دوم بازی اسپانیا و بلژیک</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99461" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99460">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
❌
📰
فابریزیو رومانو: انتقال ادرسون ستاره برزیلی آتالانتا به منچستریونایتد منتفی شد. این بازیکن به این تیم نخواهد پیوست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دلیل لغو قرارداد، بروز نگرانی‌های پزشکی پس از انجام بخش اول معاینات پزشکی بود. (این نگرانی‌ها به ویژه مربوط به آسیب قبلی زانو، به…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99460" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99459">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇪🇸
🏆
• 10 گلی که اسپانیا در جام جهانی 2026 به ثمر رساند:
6 گل در نیمه اول.
4 گل در نیمه دوم.
🇧🇪
🏆
گل‌های تیم بلژیک در جام جهانی 2026:
‏4 گل در نیمه اول.
‏9 گل در نیمه دوم.
‏1 گل در وقت‌های اضافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99459" target="_blank">📅 23:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99458">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRNfpfMfh-S-unuKPRr8Fr7AxL5_LtE4rwrA8p4vdBQytj1HmetLxIiNc48Q5HwBSJCUtQTZOu3o9vyXa4WOHRC4wktLInx-x0usK6Kllv30HYm3t7SHAuBNza5mexpNcdzrLZQBIFnD9T9_wQDzkArk-dJaeuZmLcR0DxyBy4q9UWQ6ULmEpFJYVv7X32wOhUUmKXmpVTkeN6Qz-OWWhEJn0S8dfPxNXIOLqMo310Qe53DTeTvDwjZq1A36-m6kAGXT6e-4lFtGLNJM_e8obXxhkGhskLM7uXMgwDLKxg-xQswziYUWjdnWZTBImtPiR0s7O6eLSbxvzEzc_XF78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
دکتلاره (با ۳ گل) به عنوان بهترین گلزن تاریخ بلژیک در مسابقات حذفی جام جهانی، با روملو لوکاكو هم‌رتبه شد.
🇧🇪
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99458" target="_blank">📅 23:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99456">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
پایان نیمه اول؛ اسپانیا 1 بلژیک 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99456" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
