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
<img src="https://cdn5.telesco.pe/file/K6A6FklcQdvUyDXl4teUjVznMqMGXQmSQjOao1di-qatbIz8PTQdis-hhs-ZOrkoeELgBBHxrjA12DVbCS7bwC299Fn7mfxOtVSl1PkinekO5VmaEeaiT7ZkfqOsT8vkggulucVVNYL0fJ8xgr7eHlyRVTmmWEMGq4bFe_ATH39uCSmVveiqTZVQ5aY7sbpc647Kz8-Wz6AweHVdvGmzm8zvfIuP1Bi-CWeRvExajDXzA3GTsHJKWhMu2ul_FOBq3TEhhTrw35fG5VbUj617Lwa61gEaUx3r7QLzAV6CDU3FZ_Ug1CCMKTP7or7eDNH8Z582IK7C9fZXx5lS6TIEbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 564K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 23:29:19</div>
<hr>

<div class="tg-post" id="msg-100674">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBRi3AR2VDIpbWXVwZxKQUvk64ELxz47PRbY7J9l5veEaa8q6wFp7fV_64EdiHApNDd8viQgtndmN-ox5-hhfQE2aTxpuVo5msusv4vW_S36NLm4UWN-RP5LPI8C6kkq-iDQ-WYbYlRfqK5bKA1O_GI3ui7M5KQYm1Ntfq_LA6Zs15d7XTiM6Qi50-T5rhDeVgiF3ToJ0dWO82lFTzpfNuYK5FW_Qfdw20mXt6_mo2Uk0QfSe1e3gJ3OstyQHykS6KygYMXIFAHTuFtOfbBs1RTglz_BOsSTOMr5aGdFLymoMh9b0Yfz5-vCk5yp1j6EcfpPyi4O02LfXk0BXCuLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: دور جدید حملات ما از الان شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/Futball180TV/100674" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100673">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INVUjjRydUedMw0JzhYpiZtRDNGawHQ2YEyEsueIUMoEGcmbYZLE3ddMadx3z6uNz0Ikwt2Lv9MiGlyQUzqsUxv0eTdFbf4bNJSwPyngWMQRACHG4psAfg1H7TDP4OPU19VyKX97elDdGeeIGZY5QCwSs9WsUuFaQYGDY_JzDnFHIePLPN7JDNDH3FaUJqU0KNeW0Xzs3NcQFuQqU7JyEWrcOAhOKB5vIb3j4-6nbFWntXBPzmZDhK3d-0Xw77GJTL02sxxDHraHbJ3WgGmWazJswHXRlYtPjCqA73cMz5tcOWXMgBuzFJmxeWAHOuM5r8hVQiSRs6HtDfBIkuZUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/Futball180TV/100673" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100672">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vpheum3ChsKGSI-tS3JEh3PSAWdrstpInEhdkxfCQyD6BvWxu0R3Z3pK3S9HQwNBI7YS1yra1YPp0D2XXlwBcSXMQTDJUUzGRqGJjfMU1fnjvp-UI9Smq0U6FZP4cwYIrLxbAsmMenn3Wi1HimNHs75U7-AyeWduC2nuxMlAqqOv1X6GccarXa9FZAdch-Hgq50mQitEFkioMU--_0_oxPMpYK2hSmdTbLSVlsGsoQK0dUtKjn_q6zI3sQWfRccqZV7YTOi2kTw1XMOKoLWuEiQHz_j6dto4ycGwpP6mDZvEHsMXUtV2N3O2hgP3kaiOITYyvMtAnHb5QbY6vW_kVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/100672" target="_blank">📅 23:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100671">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=YRMs4AQ5DQJV5oMUDYO6DYxoSsbsOUgPb5-8IjBnwN3qV1Ode2Etwt9vuYk92YCO5qTDvU15cD-bZC7-MaifbuvYXkcHARKhdOS4fUP996Gug1VaJAK19dBUlPOAulg-2PN8yDDBighIAa8B9TKpFM1vJgVxy0sNgzNLNafYxdkXDblwlrVL2ed3gdc997L3oWHh3rgUtPP2RTvvTczkSMnIM6tmQeQdY66dPdDXJ-OC3sP3P-BhMI4cvIk_6IqkVKswzf7S3EGxGOHlWLq6DHUhena5CCC4_CanDn0yn-lMekXiC7XxPmbP3o_RXoR5uHFf8keVqMYp5RSKwo5Kpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=YRMs4AQ5DQJV5oMUDYO6DYxoSsbsOUgPb5-8IjBnwN3qV1Ode2Etwt9vuYk92YCO5qTDvU15cD-bZC7-MaifbuvYXkcHARKhdOS4fUP996Gug1VaJAK19dBUlPOAulg-2PN8yDDBighIAa8B9TKpFM1vJgVxy0sNgzNLNafYxdkXDblwlrVL2ed3gdc997L3oWHh3rgUtPP2RTvvTczkSMnIM6tmQeQdY66dPdDXJ-OC3sP3P-BhMI4cvIk_6IqkVKswzf7S3EGxGOHlWLq6DHUhena5CCC4_CanDn0yn-lMekXiC7XxPmbP3o_RXoR5uHFf8keVqMYp5RSKwo5Kpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
علیرضا فغانی: بعید نیست در سن ۵۲ سالگی در جام جهانی باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/100671" target="_blank">📅 23:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100670">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=vbdzBEp0GU6hAeOGV17eqceGiPryotgwM7Ip4vqhx4sk6yjxkPX-gp4rHCsXKS_h953Y0J-zzqoe-v0E0xJvW9wf62ba_dtRubGS6e4_lE4fVUXXcEcf4WTBMlWuh1YmJITNZHtphKnrf4Bj8UaWTrJH-uHmz_FYyOSwnYywbkiMvn4OIaN5w3h9cEPvPUdxJThcGKZe8VoFAlOwSBSuyum4BqMtw50AYjm532fHmNSxmcf9RcERXllQe2tXVXx78aNRQlI4snw2MVRzeNJ1jjpdcLezv8K7FHDol2aR46GjkreyGdJ_lmeVhZej2wdCtDxOetPNn8oYilfhgf9kEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=vbdzBEp0GU6hAeOGV17eqceGiPryotgwM7Ip4vqhx4sk6yjxkPX-gp4rHCsXKS_h953Y0J-zzqoe-v0E0xJvW9wf62ba_dtRubGS6e4_lE4fVUXXcEcf4WTBMlWuh1YmJITNZHtphKnrf4Bj8UaWTrJH-uHmz_FYyOSwnYywbkiMvn4OIaN5w3h9cEPvPUdxJThcGKZe8VoFAlOwSBSuyum4BqMtw50AYjm532fHmNSxmcf9RcERXllQe2tXVXx78aNRQlI4snw2MVRzeNJ1jjpdcLezv8K7FHDol2aR46GjkreyGdJ_lmeVhZej2wdCtDxOetPNn8oYilfhgf9kEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🏆
علیرضا فغانی: برای اسلاوکو‌ وینچیچ هم خوشحالم، انگار خودم داور فینالم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/100670" target="_blank">📅 23:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100669">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZnuI5IU1lEQEABw1rGDgtT0GAaWT_DCctzEX-KMpPXtWPLba-X2gr3fjku9DTXzhFuXrih7drfqLlXvbbg16Ua0xWanpSMOU7Wz--qRoiIu_CqNbmP9MlDSG27ZbyooELzrUQ1mw7FjJB1Gk67yQOUXO-AszZrm2YhmNi3N-9tzmUKNXPrasV-mtCoLT6EXGtdnBrpqtelkHxiGEJ9IsGELHpcwGF9wxdaYw9UKqD55pm72fDGPYu1NQCLf9jhTRMR24UIoNvlgUcvQksgfdK9Vkd1UT6SiTgivITWs7-YjaUCopSWOQ9AfWMnnyAN8iYFkLh1TSMHnwTHMRABlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✔️
رودریگو ستاره برزیلی رئال‌مادرید پس از گذراندن دوران مصدومیت رباط‌صلیبی خود در اواخر ماه دسامبر به میادین بازخواهد گشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/100669" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100668">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6PBJSN6EwwT1C8zOrEFmrGaq1xC_DfDGcLhTAGF-UJ73ixMh10AtKfFcnO83V6wXWSublgaKrN4qa9ahjSsCutErIlMCGYGHRGppZgrWyotfmho5gbLEIaoU0BbzwdQ77j0oet3DDAUCNO_yiMZ9EwGM7HB7oMYdoK1bjw6ona2ShQLlZ5OW6U5GKKCyEPH9jyOhrp14WhsyJWmtDHwM-rlVHisRqnx2qGgH_RvMKnXpnHfQxpF_o1VoIlArA3-bL29SvVF7tAkHTXakK4rFEN8bufmpEpy39iaFfPBEzk0BT07S6JOzv2BnhfKvpAZAHMYi8w50yMitNOfNkeBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مکسنس‌لاکروا مدافع کریستال‌پالاس مورد توجه آرسنال قرار گرفته و مذاکرات ابتدایی میان دو باشگاه نیز آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/100668" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100667">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">لطفاااا فیک نیوز پخش نکنیدددددددد
خبرای دقیق رو اینجا پوشش میده براتون :
👉
@khabar
👉
@khabar
تهدید سنگین آمریکا برای حمله شدید به تهران!!!! نمیخوام بهتون استرس بدم ولی این کانال رو دا‌شته باشید
👇
Khabar
Khabar
اینجا موثقه
🖐️
🖐️</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/100667" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100666">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlxjaV3ykxL9I69ys1j2mAfUekLmoaooiV65gjYBB2gkl97yhbquSlAkbKSZxWMk5G3jlfu6FNMaOk_MtDvevv2h-vqdH7PZx_rLGzY3AgchZn25sOT2mqr2CM_OwSUQjem-ul1NJYpF7DI4X3YzamXhXsMIdRJoBv-IMTTGoDoxZd8rMxeaEoj-2arwvCcci5rH6Ips8PHhEojoR2atyVpf8W5T911HJqn1OwfUFkFQbkokUpe9D6RW35InvCV6PGyQ7g0T7PfKPfb7Z8H6HXsRCX0zAqzEAOOR0qaGboeWZbY9rJkrDFitkwpEIYgvo865lle9KG1l7pSwoHT75w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
والیبال ایران مقابل اسلوونی هم لنگارو هوا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/Futball180TV/100666" target="_blank">📅 23:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100664">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLb2htvBtjoHoLIwLTlBlAKr0TQgxJknr59P9YwLRyLDudtuU2Vs6CLWXhn_GP3r4nZTlzTDU8J16L4qV1dPU08W_phPkAFnYoAoCEAFF9n5Jeylv3G9EX8jx9mrDoZ1hH_ypS86_FFN91yjYIPhGm3jcq_a9wpMnrTS4bNSca0hdxeWpvFujv47YiYjZkR3VS3wdxPWRWD7FBFE9b-dkzSMylQQJeDkwXiQsD7-PwwRIwDugjyjprWIeX25aJUC8vvkMQVMZz2YDG1dshLAOn6gHRv1fgS46Z4DJlaT_CmdkTOwQWNO2I8C67fn2eb3qbDy_2W73nTlyBPt6Iuoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wp7OCrW_boBG5MWmy_PvgQKp_uf0EwpUxJTsvE_Fge8WXtFsNNUe1tgjl8v0LQ9ictIbW3jGlmsfTkCFp-7AQEcbaejtsYPfepBmhAPNHcUo6EyllnFg6b7cFvjKPcxnusjdlPOpgtozjgFmxCOWW0nweq3TCeEaVdUjsFSjFQ5Rmg2A1Nm0ovd7Em8y913Fuy_FB70F-TfaKb9SuTFuTJga4nS_JLeYJblkXdzHBQ8dm0AiAAzAvgT9Y8mXqtFgJCAVSnWaqXHTCLAiZ98IdfThnpVS6gq-iYac6UNVWzT4yT7RKjpF3rpjrwIWuE-VSw0WuldT7u885ttCjB5e2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زیبایی کاپ‌قهرمانی جام‌جهانی فوتبال
🏆
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/Futball180TV/100664" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100663">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu0n4Tla3eFKsoXqk2DxmCJcCdGSd6Y4Dd0En3H3t_hzxvAECsne_-Wkog4FDd2Bw5SOVb2Ly3k1Bn30gi-L4Nx85e4Md958jYGwZxvYGRxJMmAUsqv2rAIHUYkCrjSmCTfG8G-6PWA4cXW8i96W_vSTdSFkhmZjZwV0Ucrq5X2JK3VGiRhgmoWzwVQ4L1QTdIjAVoP1jJKUTSba1BPwDAYoGMawchU4rxOW5BU4OTX05T-yJwnQYwHxVXnC8CJe9bT1UnINRnsa_rB1HWdHgbs6kPTeDG--vufCLY6N4EffItDVkpI_2doGQq7f4diVVf5UaKuyqmRW-34ut15Lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حمله تند و بیشرمانه بیرانوند به صحبت‌های علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/100663" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100662">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpGyN4QD0ClYdTquyeXUMxfGBTjtiHSO6EtHq2RgSGyz9na6YXgi97nWrp9fKrXAKI_JsTkLn1-5GvFxjzVBHdk7Jfju-R7Vl6mQGaw6hd4lgj05scs4LzMcuNMMpPRfx58dk_63TK3I8BmT9G6swrFXXHqC2AT-hVeciTVj4pfd_YYNUZq7s-yhZQ3M8uE-dkiBjpGGkmwKTyoGq0bSKBDbq89QQKjLSuac5rro6DlaY0hcb9Pp6lAsGoM0jZ7EiUEHhcXSa3zfUD6t2gaEvo0mEOWGxuUVaJZpNOZ-VHsEmewumihAsBGSdflvs4xhQuiikoWzOQUfOieq9bG_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
بازیکنان انگلیس هم قبل بازی فرداشب رده بندی تمرین رو دایورت کردن و به خوردن فست‌فود سپری کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/100662" target="_blank">📅 22:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100661">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGSWMV1TwFrwxZVT3F1HkGLRIwebQvdeChSaJHiTakKvsBWfLd-MOSwSLsyHBvc4IWxagsIpFkhblk7hgIRVSAFsTLO6nuyjKQniZAudFrjrvJIC0Rx5waUpYDwUSDs_TnlYVYEHCdK_7sdjmZNEqNwP41td3Jftq5gYzPmeauB8v6VSwDn6G4EmKeaGIPaWfxklogm-qPjsX7ZD-GXkp7BI50vSoWL-xev18D0ZlA7fuHYTA_ElQrXfaz0XvrdaJlEC0o0rSKHlYsNkEKGrk-TYpjWIsGVYsDzhwzUdCTDx0dY5nEidq9RW9F_kNMPOPf09jkeAE47pHNRMzrH43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلور ناواس:
من فکر میکنم آرژانتین فینال رو میبره چون واقعا داشتنِ مسی یه برگ برندست و همین تفاوت مهمی رو در یه همچین بازی مهمی ایجاد میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/100661" target="_blank">📅 22:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100660">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L52VF8MIIaAd1DaqMV7kDQAjNgdFYpSCuj1wMkYhtcJfLA_g1LWAQwvStcR4srYvkX_gBiD6UH9kb1wHSaFifsVVAvNSvu6ku9ZLi8qlmcn4e2WV6oShCVyY4rsd3jbLn0h6jCblshtowo4KQ1Jk-3k0ddTizlX9F2WD0Mk730RMywplwfx9Q13JD-Y7t7QqKtKC-R-aqzRtiQm93A7gcoW2n_cJOyOUDP8p2dU2bbRO-6QbNosxYyuMBJPtQZvr_esDtHm3LfePl8DWFpqOWF9-_EHO8E_EGAtHZQhHdF_JMIRfI_EeEZXMHj2WQ4HbgiLcytnXSgwDG_4cuvtUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
دلافوئنته:
مسی و یامال
هر دو بازیکنان فوق‌العاده‌ای هستند، اما در حال حاضر هیچ مقایسه‌ای بین آن‌ها وجود ندارد. چون مسی سابقه بی‌نظیری دارد که هیچ بازیکنی در تاریخ فوتبال تا به حال به آن دست نیافته است، در حالی که لامین هنوز در ابتدای مسیر خود قرار دارد. امیدوارم مسی یکی از بازی‌های درخشان همیشگی خود را ارائه دهد. اما لامین هم می‌تواند یک بازی فوق‌العاده داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100660" target="_blank">📅 21:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100659">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu4A3P2k0PIkoWEPJbrxMbscUz8nKpwm6fSfSwwyQUQ3CiwIxGCLbfKIhvMJRs3eiEvOtW1LIKCG-2_iDS7iA0pJyj13-Vwzkg8LZtCY5_k0WdZaQMyZGHhUS9D9Kq_x0FnnU8Qv1kinK_mbp776WmlDCKng_gA9Lfhnpyw3IGPRbGjdoHHK1u5BYR4e5TwuJ1tTTN1QZEPKhpoL3Aq8P-jicx69lMF3URm3JeiZ2jEovyOk-OfnioUGsMXl2yYAjvL4xhMyecr2n3mHhPFirShOoCOpbvj6d1RzfaP4u5UL6kjr1sQ3VXa5jrCJWcr4cPKoJDykvfiiEBdfzvVs5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بارسلونا در یک تورنمنت دوستانه سه جانبه با تیم‌های ناتینگهام فارست و اودینزه به میدان خواهد رفت. این تورنمنت در تاریخ 8 آگوست در ایتالیا برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100659" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100658">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zz38XR9vkjyr2KGsWjMJHMhjR7QA4NaNugY_VVSWP1sSH87wNonPWAMVLL4q2tQfZ_f6Vc4fhdV-G3SgUs6xbgQZpruZtBuMCoaOpFO4JQqmufVSNjG-d3h5jZpYJNVkFCOmdYwuS_g4hZpjnqJOYlVGpxYAB0wky6baxiGClE6Y9i03H4bZxJjqUk89YOohw_NaP5mrZi7XfKO7sP-j2AlVagE91u9GrKdLM00FAiRUVVmNKYbCymoPHyDDOjolPCMA0AEUCrwt9ebkJe-f1ttsWgCKKDGs1jphzuWUwHrKYkg5SU-D2uepOqQ_XwmOZfnqRRC8_m5--hnbQFYS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
؛ لکیپ: اولین پیشنهاد رئال‌مادرید برای جذب اولیسه رقم ۲۰۰ میلیون است که تا ۲۵۰ میلیون یورو نیز قابل افزایش خواهد بود و هفته‌آینده تقدیم باواریایی‌ها می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100658" target="_blank">📅 21:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100657">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2KFWHUovQsGKTytz0yY9mAyeIrTLnmoP10wGVBiHdToLaY28kIyKCbEjep1F9gUVY0VMCBUnZGuhlz5pmVB8c9rLodv08vTT-IvuIRtnWL65vOKbX-aIoqNp02GEHaoJS2rNSXCi_qx4slJQD4VkuUoUFiBS1kWhmPxzxwo256e5N9vEaWVGdK1cD15WYKoktxkrq1BbH1bn6Wr11oRik1Agklmt9EHYMT_WWB6uzknL9kXyQyLc67Q5ocKMmYwst4dhrDp8FlTMnAcDAS0pNBPMsheqfA8tSf7Zj9UectooBxL4IO-12qqlhmFe6Oz14I4pwljlglpQc01aTsayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح برای عقد قرارداد با بشیکتاش ترکیه به توافق اولیه رسید. دستمزد ستاره مصری حدود ۱۰ میلیون دلار خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100657" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100656">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEP2tVekCUGDpt116UqOJQRjR0HAc4glW1hnI_fL86s2Mw9WorUsn_GTliPYkGJKV4Gmgv63kL4raj5dj-GcIdvIWNve4DN2rkMWavYVZFz0zgphQwzboeChOThFbLEHxZL6pdYBshc1zf67zBKs2uWJ-d_s0v9KxrHACQ1y0SDy5W-0L8xez2jmGU0T1JoZKWUoLPWaegccpM5mUkPNbnoGJkOW_UCZc8VA9CzHBUx3U_nwqcub8QvKZ8kowKd6PT4q4y5s54Ldrk8D9CmZifxfPb1SOSYSIB8X2hc-Sq89WqGX6gluvnpcfhdhFoECJ1J1zfvqIBwsD2xRazN-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
قرارداد ادرسون برزیلی با آتالانتا پس از عدم انتقالش به شياطين‌سرخ، تا سال ۲۰۳۱ تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100656" target="_blank">📅 20:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100655">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1mW2AsOXEPJ53696ivlIcbxgaYyldOvdeEKwQ0fXdSalfus6fXKzIMTNf8pB8zrRvqyNbW7Rq9cUNgfRZruglqPv_NzBgIPrIRR7u3MhZD1fWn1DgD8SiUkGyFbGPjPLLPut9uoCY129GDThosXNNMOD4dSDEdGPdRAQ3v0ndqJbRFf4zHzvwFnYY-iQixJWVBICqJPKGpCgk2lzfRac0wn5Z_nQeEI-ZgLANkq2P0XwBo-Y1XzrW9WKXjDa-RfFPiHLw7D0P8z0MuVZtexhn-NOFhIJj0YLT52Jx6DLIhFKCT20FL4FS0rBWKwbfC7Tf_zTXDlWkZfYLMWNA9pMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
طبق قرارداد زین‌الدین زیدان با فرانسه، این سرمربی در یورو ۲۰۲۸ و جام‌جهانی ۲۰۳۰ روی نیمکت خروس‌ها خواهد نشست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100655" target="_blank">📅 20:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100654">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7DR4Wbw86Kq1poFZZOFqsrJp5ifpcWNhZPnhX6Qd1UDGY9SFhLZ249NuIGTF8JcHNmLJZ8DOuDYng6HC4_eYBdvC5t9Z1IGIJjhsc_xqINI5_oPSTT_ZoSU8NBJ51KqEgaNgM6g04zH6DV2AMPVHUH92UkL9bfchn66OQCjlg-95-rp2TZPxaK_ZuOi7duaJrXobYiE8kZwNvFH9pBWHRj3W-PUfEg16Ea_Sfz6vOLbIw4gRULWZiB65UQhiCQO1UKmwHRLD7IZ_d_lM09pbgPJvA0jDbqPSUIOQxcNyIRZ4uAUzytdpmO7mtVKjDXk60Qz0cW89ZoVyqCwSS6rTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/100654" target="_blank">📅 20:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100653">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P15sksOK_Aa-cSLwgRIXGFy6CzSz0kA5Za1IWT2ZTEGYlCkxqOx39dwWgjykrnTnye1nTurGWVoWC8dG_ehawfCOkxVQTJbb8DBCJrC7P1BnJbAUkNDjUN21Eh59k5Vni7TeQDc3Faju1cnEshJVRIybCz1FKEkhc0BB7cpI0XBMy8vQ17r5v0NoKkFcWHZqJI3xccZT39IrVwS9IMtXdQABDhkNHxj7Oh0DNqjhHKxb1roLoXaJM2CQT95HfNT6HzgYjBuZrcXOu8mS9c3kkeIBfvddK5uTtA_xOrwpdOyQba3W6nLh4bwhuXItQaHsxYympMOMIzvHozNl5rzKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامبک‌خوردن انگلیس فقط به این جام‌جهانی خلاصه نمیشه؛ تو چند سال اخیر انگلیسیای لوزر تا میتونستن کامبک خوردن
😐
🔺
2018: 1-0 مقابل کرواسی
🔺
2020: 1-0 مقابل ایتالیا
🔺
2024: 1-1 مقابل اسپانیا
🔺
2026: 1-0 مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100653" target="_blank">📅 20:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100652">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o01iWjMqcFYTWNX-b2xGYlmemMttL-a-IE9tKgvM97Dve5_aPZvchtID_pdUF6mxa4hpT4ZTk7jB7TIXMeb494tO1ccedkk3FyxzGkIp3C7e-aRzyU7Jjn6W2HcTorrM1jQxr7cLGlOkdDA3J5VyAOINKgtpCcpoP9m-Fwfn1jcU8s9jNKFe5aw2th6P5uxLSIGerZ7FJaUyqQliHmYVtB4eIPvMXrXCFoHg11qq6tCGqSRDK_bUPeMXxS2vs4JMG5jDry2QqLbiQ45kq-QY0RfLUy1rvMYF_xI3v36VsUT1R7E7yZsZTb7arWpIIe-KV7TPxAoUwxOEabn4pVXCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
جیانی اینفانتینو در انتخابات سال ۲۰۲۷ فیفا آرا قاطعی داشته و به احتمال بسیار زیاد در سمت ریاست فیفا ابقا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100652" target="_blank">📅 20:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100650">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fttlorP7P-Opy6iDB9BJghG22Kq1Irno1j8PYlRE_QpV86d03gfg0a9cCKIJDi06jtnUJnaUX8j0WflvYwwxPiX4qLCCZm1Y5tD6rkjrrvlBzasJxejpu2w5GjF7meCYp-vZst_xlQ2g5opsesFZGA3a299JMkGFVoF7UwexiUa5JriKP3fPFdTBnmoR2DXjC1v9S44trowBQOILt07boVQML4QSq-qD4kRRa6dEFd1iiblAqoFkvddg9MN8HhhpD8x6_Qj-vJft5BuncUDkvhScxdJDsyEE1ioYcxiIvrOiXBMJZL9AzXNJ-DKQaqfwP_tEJK698UXnRE_tG0-mVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBLg3p-EQ4rqBF4tkWrxcd5lehL0RbNZKPzewTlK00r-mT-j9TK6YCJ--awV-V9XngwTz9iGEzO3FtbuYkckIYcZI255V4CuKIuUuBpypuJOkfTqS3KUTq00TcGl2RvMTSRETMdHcw9eQDe3SJkBwGbfxWQikcslqQkbfUeB7xRN6pb9P7Zh4OESrvmgB2AWwLQEvrPIwZbJ6LAEZ42Jb0mbY5ZvJ1IiLkGiCNG4HKqzojIVM6Vl-V-dcHOEUEDI2lLERQnLtHY4-7O1yhhW2yByEd5dGi3WCx-JyDI5TTQcx77HkV5vKEYehyd9qXfVodcaIx3mdqimEAavVEBOew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🏟
جام‌قهرمانی جهان در استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100650" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100649">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYQPnh9gWP6EmoFSHryCJoWL1F-bVtEnchHB5jNy1siWGp7_LO_vyXKQbKlJ9jgWQPCXMC8uEgYLCTviYDeFcjdsypI53z2H1hBGqLhsiDseOnwgFSY84fLpgYNrEKND3JQTFz5fTfQqyuRVofbvPfzFpVUy9GVQUKNMeuQ6XU0Vri5Nm6_IyBGjTbqORoLDOVrjikw8hGBR8m5DJpIQe0_CtfSiODWvDXKl-awxpcITR704i8-M-5MQFEQF11jeLqF-yrf68xrJIOKWuoMsxC0zpGnkf4q4tu2j7frIVgR3nm9EM8s6gNsaknfMyF4TpmK1FY8j9CfAPqUlmZ4Dhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یکی از جالب‌ترین اتفاقات در فوتبال:
- آخرین بازی که دیدیه دشان به عنوان بازیکن برای تیم ملی فرانسه انجام داد، مقابل تیم ملی انگلیس در ۲ سپتامبر ۲۰۰۰ بود، و آخرین بازی او به عنوان مربی نیز مقابل تیم ملی انگلیس خواهد بود، در ۱۸ جولای ۲۰۲۶. بعد از ۲۶ سال، این چرخه کامل می‌شود.
✅
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100649" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100648">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/100648" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100647">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cR_1Q9VZWjGZiPiyxn5hUz6qpfesOUfWd2v_z-xD-GPKzDoINkdniEjIE8xVpsOOJl-2ztrINN4OM99HzghMxgPrJ0xiE4buD3mFZwLeiZYVJHkA2JOITuv4tgeyKIpzCajieqprDUxgw4b9o1Qs7yXawcEXPGbw98fm6pNZIX35VBP7YjP706JkGMupFw-9l9VlLl8DtPiNiAWxyZRnFrHmUVL0dYkpvJ3oitcX-Q4ptW0hcnmITpiltrGJlN0Gfm6Knx0iUQeTEHcRD-35ZROnGzbGhyOG__IkkWCCS352ldswg_-xre_XqNfrjxWgzb8hxTFnEoumn_DEZynDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100647" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100646">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbOtOE4kTncDUXVt8lYwisL0egQCBU7pmgQ_KNAMBeV_Te8tjqSj2vekcb5LWP3DCedfLi8wrMp6kfqbW23L_T2E-c5OAKHxs4s2W0ivO5hc_CW1yGXKqpOsyK6_oszZ31CCYqMa73GAYPJhLxtkUC3AWBKnuJ81YP5U1h4qRtNXoCX0w_IuMf4iA0T_OQIl_oLv-A20GeNez90CDB7cjSzXWodOr5M9Yjk28Rk0i9v1rJMFY9uQpL3q_WSlEQEvqcszhYanf_FtQ8-kir6ZQzX-O4-swipdwf5u5i9QjZ9yQNP13ZRGACnRiVB5NT2h7FM3HWt0ht8o3PP_as5DQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فیفا رسما اعلام کرد نمایش بین دو نیمه فینال جام جهانی 17 دقیقه طول میکشه و نه 30 دقیقه! خود نمایش 11 دقیقه است و باقی زمان هم صرف جابجا کردن وسایل میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100646" target="_blank">📅 19:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6919a48b9.mp4?token=tNBKQkTDwlESM-y-TMWSavpG-EQe28sOhjDiG3DWLua2h16SdNfJi8ZJU5geR_tFGw-dTO-Qj2ijCcO8gsvsNpcnyWf6kgrVqrGAyGaHOmlGn96MJXxp5dLHftqrErCBPxCwnlGqDYRx6psc_aCVKaoK-cVDcELkwhNnMwqFjaJjhcMNUII9Pw5BlHI78WwntscXg_O8qhex6_K62QURRx0k3ZoWEC0SKMWcDla2aZdJjqgp597Ti6V7KszDB0_doioqx-27MFOskTHUwyeNHCj4ryACeIsq8avhdTy0RR3xq8lx4u8o_l-A089NW4NNpRHIMZw5aPtSRMGzxC_VLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6919a48b9.mp4?token=tNBKQkTDwlESM-y-TMWSavpG-EQe28sOhjDiG3DWLua2h16SdNfJi8ZJU5geR_tFGw-dTO-Qj2ijCcO8gsvsNpcnyWf6kgrVqrGAyGaHOmlGn96MJXxp5dLHftqrErCBPxCwnlGqDYRx6psc_aCVKaoK-cVDcELkwhNnMwqFjaJjhcMNUII9Pw5BlHI78WwntscXg_O8qhex6_K62QURRx0k3ZoWEC0SKMWcDla2aZdJjqgp597Ti6V7KszDB0_doioqx-27MFOskTHUwyeNHCj4ryACeIsq8avhdTy0RR3xq8lx4u8o_l-A089NW4NNpRHIMZw5aPtSRMGzxC_VLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
بهترین جایگاه برای تماشای شادی هواداران آرژانتین پس از صعود به فینال جام جهانی فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100645" target="_blank">📅 19:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G76Mj_1W1r-t_zHtbGZpJB0gssODKeaVqZoy2cxT1nj64eVZJw4EkxnOW_n3RTkaU_lpNlZKwLcqgVySiM5a9Z1kbHLuftXcayK6TZktpFtkUK6N107KD_l-maydwSc_pBt5GBBxLmvGt2STI4yN8CKrN3AIPjJqsr5OlpuKEc1JqccJE75mGo0mojYyYwNw-tMwRYOpg7z1T8H5bmu_GUt5UjYg7HTw-fwIhk786m0h9CjXoclnpRkwctulDPnCHJQlB_62oHqZDOFdef-pdia1XZo4j5UNhxBAQskVKQylUVWTBvaOcvfiFTMw8EiO4dgLTDpiQPfnG7OoNmPsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آرسنال به دنبال جذب مورگان راجرز،  پیش‌بینی می‌شود ارزش انتقال راجرز به آرسنال حدود 100 میلیون یورو باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100644" target="_blank">📅 19:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e37b8453.mp4?token=gTy4la9FR9DDdTumA6rO5TKk6L_J7QVvai-Xc8Tf4axEw6jW1NvOBcP-aIvTjhS9SPVkA3cCsknlL-DfSh2oNlvj_vyL1OBAPlfFmBa935LYZmnH3iHTuU5O9LRxvod0ucNrdK_mNp5s15PJodBx3hY-5veF4ibZNDI7tvXzqIPYzy9aqPtoHnU64v_t_tsWzG_V6dcOzDVx8HV6zzvf9Xf54it9jjz5m_s6U1jYY410xVvpASmqaTNT_A7oC9eeQxcWIHsJj792_LZuYPsiwL0k6H6iGtQN6cg3Yi54ZWkU3kb22DzLsF2q5__uQ0T_Ecrd5mIscLxt0ReNm2K1Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e37b8453.mp4?token=gTy4la9FR9DDdTumA6rO5TKk6L_J7QVvai-Xc8Tf4axEw6jW1NvOBcP-aIvTjhS9SPVkA3cCsknlL-DfSh2oNlvj_vyL1OBAPlfFmBa935LYZmnH3iHTuU5O9LRxvod0ucNrdK_mNp5s15PJodBx3hY-5veF4ibZNDI7tvXzqIPYzy9aqPtoHnU64v_t_tsWzG_V6dcOzDVx8HV6zzvf9Xf54it9jjz5m_s6U1jYY410xVvpASmqaTNT_A7oC9eeQxcWIHsJj792_LZuYPsiwL0k6H6iGtQN6cg3Yi54ZWkU3kb22DzLsF2q5__uQ0T_Ecrd5mIscLxt0ReNm2K1Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
در سال 2020 جناب وینچیچ داور فینال جام‌جهانی توسط پلیس بوسنی و هرزگوین به اتهام قاچاق سلاح و مواد مخدر بازداشت میشه و پس از تحقیقات گسترده و یکسال ممنوع‌الکاری مشخص شد که این داور بی‌گناه بوده و تبرئه میشه. حالا پس از  ۶ سال این داور با انتخاب فیفا قراره مهمترین بازی عمرش رو سوت بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100643" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100641">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1kR6gdTMlxnVnYpoU3aLWN3_SlZ9Vblcw02ujVaNfTMrpXp-S9KvlPso8yApwE8UUD9sVOIZiBHFU66HQcNj09dYvaWQOehgjR45u3gXb7xChbaO6YNm6GW_el7bD9WwzjuR8xTMEd-gjaN2KuRwk33X4DJvnWhcKoQEBjXkEnw49k2l5NlhVOX-vc1E964vbY1FqjJ6MnP5g6Ob5JMpK2RIZizj4ae0jqvk05OdKaPUaLbqwo-BHuOtEBzkQB0qJP0a4hJimJIdy2d7BpNoo5YHxv9F8cVKkNlF8Lr6rCFrZ5iv8k71wU6BwerTofRV00eJdozEbqm9Gys9r5x5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJ2vUtdGqlLg6hZfK2gvKjiPdatyuRL5yzxMRI_brSI8YI3whwP_-czFzn9DLFFHRt9emFBFNDZhbFPrKCz6Ay6VEb1T2Cr3ReqIIOPbmzlYwSoHJiNApDnUcRmL9I2eIOTZi7DF7BpmCcLQ5hD2Sv2PGrm8lZz33KMc0Mq0klXwKBZen0BLlBHpj0pNBOpP_z03w3AryceTbwQGxqVmZ0ffrTid5TseYCya5aedH4ESDe44DQm9GUIve8E8O0RsePV2embmUMgRXc_z0f_HHnBzvjqoqwzB95TFizoJWjwy9GNCt4aZzDLWVfDYyx3CM2o4gaTo8qOzisrZVlcwTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ووزینیا: من معتقدم که در آینده لامینه یامال، مسیِ نسل بعدی خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100641" target="_blank">📅 19:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100640">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA7ejRhSwAvqkjrluSonhS6xaFtAtvGIS_BnEd0gZ1pVDIDVF8iyDlhwV4zpS_wPs8cOHwDtil5GKwgn5Wz-YhehZhlJ2zdrZvBWDpXbXKmi2pZQhbqzhFjBhvJxExbmpN3AypAuc_P5kih5BJoAfghwJl3IVkMrG_g7FyFoaZdPyVxaMH186TPv07o9A5nwb2BhVd8rtia3IwiBGfC7OF6wbboGiGGOFXRUNMu2QXCcY-5DbNOeUb6gIlj3-NVnKcPmuiLxDA605hVUMnF7G41iyq2iup_rCkgvba6PwROe201sjloIpD8s_GyLWN6sDjp_HDUNVoJ-XoQqcdRcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌‌های‌ملی اسپانیا و آرژانتین در فینال جام‌جهانی با لباس اصلی خود بازی خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100640" target="_blank">📅 18:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100639">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2BMWhbhXp557qwaQfV7RPqcfjZ1-Hhs3e_MubC34AbIeneXsIZd6nkH8NITHJVxvINlQTd3kg_cNnkJ2ZlV_gLq1KGui6S68E0Q6y6tV-iGwkw3IrK8MhXJI8kHl3fV_N2FolihKsrFMibNfOS_71nvRL2C3Ty86rpzWKQgAPKtkB2WSQ3cJ1x_BNMYo_SjeFD-EDVludLNHlFyAKWuA1KH_Oo5eKckEJKnAVCvS6nHnrSMZfK7jyh7WyGQCRetmbTHSSgpz5BXacwoPW-q6ngG_KuymfUSDuCtdMy7ii2qPROWTsDjAWyFsL8zn4BOhnw4VA7TUKubeFXjAXb2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو گوگل Marc Cucurella رو سرچ کنید یه گربه با مدل موهای کوکوریا تو صفحه ظاهر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100639" target="_blank">📅 18:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100638">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hm2Ew1ZdA0zkO5WW34ShEXTrYgFv3WaUmMQR-DVBVw7SnAgqvexTgYzzlaVCceEdnkXnqZrQFNnoQ3v2q5eWAcqrUmmDIVceKV_AffdlgRdGc49i8UnjTxdZUQrx0NyBuTzG8CX8tvLJu2Z-IpHGabzR9gqBEAkUFvenUcx3MduRMbxbJy29IKWUCyNXfpU8Xdg9dOyDjAp4mwll3dufloxSqTugs2z4a3PtTWDV36LVtvavLYdUU4mjiyw3f4ZaTOIDfiPp_J-rwtW6EthEE_iizj_kj6emIKyab60JVPNrIhJK-J6ttbIqiTEUpFm6FlhxYEoAfzGtNhae1EapqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
• خبرگزاری فرانسه
🤩
:
🇪🇸
نخست‌وزیر اسپانیا، پدرو سانچز، که در جنگ اخیر بدلیل مواضع مخالف ترامپ اختلافاتی جدی با رئیس‌جمهور آمریکا، دونالد ترامپ دارد، در فینال جام جهانی 2026 بین اسپانیا و آرژانتین شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100638" target="_blank">📅 18:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100637">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b1d58aac.mp4?token=SztjLMAnxWPEUnWfUkCT7E8ESv8pkzSDjHC6rz8O-Y8PapVMCwuYgNRM6rjDNrD7fs9MQfynS9RO2vzwyKR5bVy4MsQnWsUUYPOxJVqEe5n_5PVMXd46FadcAx4AlYpcUutwR7wk2AG9X570fUwvhKPJGP_1f2SEdZMWO6OY2jXGWdlT3jPCwn8CVObhSpNYobZHJ-f3xR-bw1XI9b3vDlPO1XrFJSMWKYrksfxnVkDBDIkIgai2EGSxInKOlYioevphjls8v-isM1BXnTAy3QRexvwYaYuSdjyI9j0WGWnpeVmsc1yqS7QPmhepNfYsDzQ6Q54roSz2AH9bvhiOOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b1d58aac.mp4?token=SztjLMAnxWPEUnWfUkCT7E8ESv8pkzSDjHC6rz8O-Y8PapVMCwuYgNRM6rjDNrD7fs9MQfynS9RO2vzwyKR5bVy4MsQnWsUUYPOxJVqEe5n_5PVMXd46FadcAx4AlYpcUutwR7wk2AG9X570fUwvhKPJGP_1f2SEdZMWO6OY2jXGWdlT3jPCwn8CVObhSpNYobZHJ-f3xR-bw1XI9b3vDlPO1XrFJSMWKYrksfxnVkDBDIkIgai2EGSxInKOlYioevphjls8v-isM1BXnTAy3QRexvwYaYuSdjyI9j0WGWnpeVmsc1yqS7QPmhepNfYsDzQ6Q54roSz2AH9bvhiOOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
❌
ورزشگاه آتالانتا هم به خاطرات پیوست و زمین چمن این استادیوم برداشته شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100637" target="_blank">📅 18:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100636">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2ecdaedc.mp4?token=uobOLNM092azmga2i9bFalDw8CcrCO3Ia1wgvvjYxqP9Z5inD9E-_k4pd0NlgmiN11T-DFv6oLiq2r1Olqgu8NoKrMMZkevJ4a6IfwokCdEMZIS7oQhqU4ZxmZIabvC6XOjGLNq473g8I43n1TyVc_1l4c3yqIHlgpzhqFy4I18AB7YbULsmBCDyt5P2JPtZ12uIT6fFei9szA58iD4R4JAs2RyklUBcAwhC4hax6FuqHuof30hPagNbq56d8cM4OSuVxX9nqIAH2JlHl2dAIl2H85tKd4wRb75oQ5ds5C70_DLYWn-_niy_OqeUt2oUQHv0hPaCj9QYSppV-SbENDmpOTXt8mubJmrB5XL8YldH_8bnUiwhPp0IVZKr0tnLVZEjkMY2gCb9g5Pah1uBlmJ3vcwNTjWaAc2Ic7q7c8c3Le34eDMhHOJIbU62BbPt4B_Wa0a0wfiggzE0bkAV091A2CS0LFwLm6Nr0JXvYSvFgGxi9C_vXzJkrUCQJAIPlybx3TK1hCTGt-wGxyicKMDR9ulwtiXuRC8IzzMqKdDnbfwJLOPEl-85-8gqP6KAVnbXP_CZsfGDrCJddRau7RK1vvRdbOH0MbT1ZOazwFJvUrmtVBIG3d5sMg0CI6aMhC34WyFBFKk8dbdqt9TvbEmSH29N5d9YfR3KtVoB-jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2ecdaedc.mp4?token=uobOLNM092azmga2i9bFalDw8CcrCO3Ia1wgvvjYxqP9Z5inD9E-_k4pd0NlgmiN11T-DFv6oLiq2r1Olqgu8NoKrMMZkevJ4a6IfwokCdEMZIS7oQhqU4ZxmZIabvC6XOjGLNq473g8I43n1TyVc_1l4c3yqIHlgpzhqFy4I18AB7YbULsmBCDyt5P2JPtZ12uIT6fFei9szA58iD4R4JAs2RyklUBcAwhC4hax6FuqHuof30hPagNbq56d8cM4OSuVxX9nqIAH2JlHl2dAIl2H85tKd4wRb75oQ5ds5C70_DLYWn-_niy_OqeUt2oUQHv0hPaCj9QYSppV-SbENDmpOTXt8mubJmrB5XL8YldH_8bnUiwhPp0IVZKr0tnLVZEjkMY2gCb9g5Pah1uBlmJ3vcwNTjWaAc2Ic7q7c8c3Le34eDMhHOJIbU62BbPt4B_Wa0a0wfiggzE0bkAV091A2CS0LFwLm6Nr0JXvYSvFgGxi9C_vXzJkrUCQJAIPlybx3TK1hCTGt-wGxyicKMDR9ulwtiXuRC8IzzMqKdDnbfwJLOPEl-85-8gqP6KAVnbXP_CZsfGDrCJddRau7RK1vvRdbOH0MbT1ZOazwFJvUrmtVBIG3d5sMg0CI6aMhC34WyFBFKk8dbdqt9TvbEmSH29N5d9YfR3KtVoB-jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
🇪🇸
تیزر دیدنی از بازی آرژانتین و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100636" target="_blank">📅 18:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100635">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639f6b5b43.mp4?token=rIiGid8WTU0qD7MQ4lPFvtrEM8su8AiecxC6VGehSWRoamfnBZplpQckPrqBjxLwdoaIpPcaaJkq2y5-sJLce78zaf00f6Vsq6iH703qXegU75DNbu8RQnnv18rHuW0LvzYgpyzKQIzxxWLN2Jin1qmHSLkDNmPBzwdG5a3LQUZf0ZnhjYjCKS9xhuAKBjA0f7tdGVwIkIB5goHu08NKI4a_ECwxpncc9GNHbgksx6aQLU4LxPvI05pqvPdcsGbUcAf4piKSs5TzXTRPABElKIlqu0IRMuXG9RMmEqjeDqQKhyQvwfq_sFqYEra-VOKv82yfa3_FNpI9F1C0upr8oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639f6b5b43.mp4?token=rIiGid8WTU0qD7MQ4lPFvtrEM8su8AiecxC6VGehSWRoamfnBZplpQckPrqBjxLwdoaIpPcaaJkq2y5-sJLce78zaf00f6Vsq6iH703qXegU75DNbu8RQnnv18rHuW0LvzYgpyzKQIzxxWLN2Jin1qmHSLkDNmPBzwdG5a3LQUZf0ZnhjYjCKS9xhuAKBjA0f7tdGVwIkIB5goHu08NKI4a_ECwxpncc9GNHbgksx6aQLU4LxPvI05pqvPdcsGbUcAf4piKSs5TzXTRPABElKIlqu0IRMuXG9RMmEqjeDqQKhyQvwfq_sFqYEra-VOKv82yfa3_FNpI9F1C0upr8oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه تند پیروز قربانی خطاب به علیرضا جهانبخش: من چندین سال داخل باشگاه بزرگ استقلال بودم و نیازی به دیده شدن ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100635" target="_blank">📅 18:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100634">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=n3EwFBo4t91j6log9BB1DlqpTTErGkhyAcS99Jw57eH-NLIAKvHjmCrBcaemVmEav89dclrsLMfLeUYEhPVc-91mIk3k25SjUiIxeiAFEmcfcv8OfgTD_sOyRG3a0Jbsqy5ZfgROrIBygzwh7-UjqLmnq94nWYU6PkkDaHv_OGBs89RM7kWvykIK3yWJy69W6KHVKf493QoQClEeilVTBIwoI3z1hxLUMl7a_7K7D01vag4PZ0ZkezUdUUblh62Jkv9Stf_9yDMXM-Et7ZBzM8LE_XEna3xn2a-Tl2WIVAuhFbfvspar4aC9Jdd0h-qTlFLYlCmiWb45PvZlPjQCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=n3EwFBo4t91j6log9BB1DlqpTTErGkhyAcS99Jw57eH-NLIAKvHjmCrBcaemVmEav89dclrsLMfLeUYEhPVc-91mIk3k25SjUiIxeiAFEmcfcv8OfgTD_sOyRG3a0Jbsqy5ZfgROrIBygzwh7-UjqLmnq94nWYU6PkkDaHv_OGBs89RM7kWvykIK3yWJy69W6KHVKf493QoQClEeilVTBIwoI3z1hxLUMl7a_7K7D01vag4PZ0ZkezUdUUblh62Jkv9Stf_9yDMXM-Et7ZBzM8LE_XEna3xn2a-Tl2WIVAuhFbfvspar4aC9Jdd0h-qTlFLYlCmiWb45PvZlPjQCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صحبت‌های بامزه ابوطالب راجب سرمربی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100634" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100633">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giJ2srNG5khLszj7cp6H4VlfVV_HQxDoE9jz-oqUdXjiH05oXNhKFg486oFdwZIMJIFcefeT7LFOFtORcsUbzZ2FNyGLSbsSFignpNHxiRDG3wUGiDANg-TwT4q9RH69Tw9UeqPi5bMzJYvXfa7tNT_mTeES7IAp0k8v_G6gP_xK12RzIjTKmX61JId-HAf0GGa61tsu3So8enpcOWEhmdghnI_k7W7fqF6J92NmkyjYGqeOn-Q2p7MFL4rPiQCaqWjgR3I1FDPt1Vy_AZNvpyA-JTaC4M6LFG0PvJ_glSL7Xb_pGGY2RZpOriXft9WHvlLS2-Md0VXWN4Okul1uqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیورپول رسماً اعلام کرد که قرارداد دومینیک سوبوسلای را به مدت پنج سال تمدید کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100633" target="_blank">📅 17:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100632">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=QioU1fSsQ_qdozlMjXP4R0MztEJBt1a-BeqpU6iyEmZCoEH0ByhCzhGXUcU-phQ3n_Qr7aviNld9fcTynDOMPJw4Yrivu3to1gn2o2JVqgE0wwlBx6rpBOQWI_vuJNcnUSeqaM-5uVnrxDdMOWFi4l8HGlftbF9JBiDttVEwyVKX5oyl4CO8urPQMA8V9eXClS3qwQoZDiCl9XWj5J1BRLGQ_2KZWphw5YMYJDeB0BQbL6o96ve4HVbRMh6fVPj-k4J9joFayakuIG_C9Yn4pI_yze1DbGWxYgEjRnDaW1Mx6eHTcZOkjc1tyR9_yhpJT-sC1NMyp5G0KtA63gw-EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=QioU1fSsQ_qdozlMjXP4R0MztEJBt1a-BeqpU6iyEmZCoEH0ByhCzhGXUcU-phQ3n_Qr7aviNld9fcTynDOMPJw4Yrivu3to1gn2o2JVqgE0wwlBx6rpBOQWI_vuJNcnUSeqaM-5uVnrxDdMOWFi4l8HGlftbF9JBiDttVEwyVKX5oyl4CO8urPQMA8V9eXClS3qwQoZDiCl9XWj5J1BRLGQ_2KZWphw5YMYJDeB0BQbL6o96ve4HVbRMh6fVPj-k4J9joFayakuIG_C9Yn4pI_yze1DbGWxYgEjRnDaW1Mx6eHTcZOkjc1tyR9_yhpJT-sC1NMyp5G0KtA63gw-EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
به قول عادل فردوسی‌پور علیرضا فغانی متعلق به ایران بوده و خواهد بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100632" target="_blank">📅 17:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100631">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwqp658mOmx3EuKjwWc5B_II6O4445OMmr7UShV4pg1HsE4wDUMAtnV5ipWP8jZctv21wpyDqRIJZ7UvKBJ3HvvERXSkg_pJ0lY4tntHX0Atx_9nrvEmx9ZVTxBsfnsR1x4YLL7623f3weSDqW1aEPxZG_ajwPv-iDU0UCmTrunNNdCAwrT_N34VDAop9KWzGuWJ75JLLF0ncx6Z4avr0bFfNCMF3CmDBpr4PDqV2Zm6WgRkSmhe1w7d2vyXjHq_sIMZJNyn47WJTVgA36BZN47qUunIzZFuX6RY-o19Lc0yXmnlE_IdcDTLaV1L5aqMa43sA_Pm6_fNcq4M_0nsMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👀
سجده شکر داور آمریکایی بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100631" target="_blank">📅 17:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100630">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=L-eN-43UF3r32AWvUUWAClrid8pWdyVfbEAAivxRitfPJ4a0dhnaigQr6MrEq42COMKzr4fLkjPrmMcob-OvUVhCQoa02_Rk7qS0XYeo_eXlgmrzql0fcnjaKjZyoUzTr2b9TxXZ1xHKJE08E3mXnjwUZ9kcWef5o5gmISL8jYDN8u4qhY16YmwlCAo6rAGib42mTt5pZNIyl0BDXYoeExtFbJO7euPGiwMR5tDi8YkPMy6kQa9_0tgT4WX4fgE6GQ7hjyi86BAV8Cbfelq7CWsRRguHlSkfzeLKdaxak0ReAkxwYx7VtIJ12QibwgR14S_rEe2uDZ8uLsIO1KIDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=L-eN-43UF3r32AWvUUWAClrid8pWdyVfbEAAivxRitfPJ4a0dhnaigQr6MrEq42COMKzr4fLkjPrmMcob-OvUVhCQoa02_Rk7qS0XYeo_eXlgmrzql0fcnjaKjZyoUzTr2b9TxXZ1xHKJE08E3mXnjwUZ9kcWef5o5gmISL8jYDN8u4qhY16YmwlCAo6rAGib42mTt5pZNIyl0BDXYoeExtFbJO7euPGiwMR5tDi8YkPMy6kQa9_0tgT4WX4fgE6GQ7hjyi86BAV8Cbfelq7CWsRRguHlSkfzeLKdaxak0ReAkxwYx7VtIJ12QibwgR14S_rEe2uDZ8uLsIO1KIDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گلاره ناظمی داور فوتبال: لیونل‌مسی صدردصد باید در بازی مرحله گروهی اخراج میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100630" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100629">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1929090be.mp4?token=ERhFnwgAlktYaoU3gTCPIkyEGG54jRwBZfyZMWdgyhJq3XYweiB3mH45IHPlWM9yY7HWWJm-lSeM6Ee8mXCh7VgfzmdAw_pnuSnlIymfYFFw6y12nLG7VeQVaS4CexBWo1cXXJBQEHszwNE06E_0bEF8EosG3rK-umqdTnB1BVJjOsfX-VH8xkwreYOsE4Oa0uTHnRM2tQNKU5zP8vg8DwjQpiREWlJTg_I3DDODBnTxLIRINpV5Xdo3s6VzNHfDBtaN6ouc83In919RaFwRy5SgvszjNEJLocH3Yzie7BMDdUSot-WhMDLvfX-IgMo-k8o0kOmvx6pveriG2gRPomVvFyG7dBonX5Er-hyu0HH5Z94uWRGSShFFiEO0_Auw3NHwYOYHKLV0Enb8DCogtbc3kehL-9EEgsEFSsD9YRZatSQSfeVnKKQvQe9Zw0PYomoeSZmdXlELAEA2ljXiijm25ISzqBplKayEcPxcGOBWITDL6FEESaAmg-M3tXkTZxiQqlQFDvq62S8CGKOHXc4rYvJwbIJKib3Dg0ihC0FvG6LFUatSrXlGG8BIJfaNkmNDj_eEapGLJ2IdyHWUAdWX_3d3u_aQd-DNSZ74FBZmIxO3lCDuz5ThkeCENTVaS50lLRg6bRC8VDwPpYcqEKWrJXpobdRA8VeV9B4C_LU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1929090be.mp4?token=ERhFnwgAlktYaoU3gTCPIkyEGG54jRwBZfyZMWdgyhJq3XYweiB3mH45IHPlWM9yY7HWWJm-lSeM6Ee8mXCh7VgfzmdAw_pnuSnlIymfYFFw6y12nLG7VeQVaS4CexBWo1cXXJBQEHszwNE06E_0bEF8EosG3rK-umqdTnB1BVJjOsfX-VH8xkwreYOsE4Oa0uTHnRM2tQNKU5zP8vg8DwjQpiREWlJTg_I3DDODBnTxLIRINpV5Xdo3s6VzNHfDBtaN6ouc83In919RaFwRy5SgvszjNEJLocH3Yzie7BMDdUSot-WhMDLvfX-IgMo-k8o0kOmvx6pveriG2gRPomVvFyG7dBonX5Er-hyu0HH5Z94uWRGSShFFiEO0_Auw3NHwYOYHKLV0Enb8DCogtbc3kehL-9EEgsEFSsD9YRZatSQSfeVnKKQvQe9Zw0PYomoeSZmdXlELAEA2ljXiijm25ISzqBplKayEcPxcGOBWITDL6FEESaAmg-M3tXkTZxiQqlQFDvq62S8CGKOHXc4rYvJwbIJKib3Dg0ihC0FvG6LFUatSrXlGG8BIJfaNkmNDj_eEapGLJ2IdyHWUAdWX_3d3u_aQd-DNSZ74FBZmIxO3lCDuz5ThkeCENTVaS50lLRg6bRC8VDwPpYcqEKWrJXpobdRA8VeV9B4C_LU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشت‌پرده گلزنی تیم فیروز کریمی به پرسپولیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100629" target="_blank">📅 16:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100628">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=Nhy5dchRF2KSYAh2s8KHYMRzhk7mJ16utFR92TSK0A6ExmTitx1raV_vEHRvbm328bj_70Pksx7nvYOsbgU0FRn6ZlTBmBQeX8CKvO04awINgfTKu4Bsee3OmV0t9xZWXi99DeVUmgP1CK_02aMHcffLEMFEbdvYs6WrBi5RkOHiGafJhzUI-maw9QKC3j_J8iHOKQKWC0mo7vXdXvG6UM_5KKMyjaPKnWupfJk04AEZl5GBHDKUHgDvbWisATwCOq7k1SgCz0AAwfutANCcoc1Jzbt4KvFKvtCphLUIK6hfh_76IEfDt6JsNZ0VqW1rynxIk77UjT3YYVKiDE_Xgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=Nhy5dchRF2KSYAh2s8KHYMRzhk7mJ16utFR92TSK0A6ExmTitx1raV_vEHRvbm328bj_70Pksx7nvYOsbgU0FRn6ZlTBmBQeX8CKvO04awINgfTKu4Bsee3OmV0t9xZWXi99DeVUmgP1CK_02aMHcffLEMFEbdvYs6WrBi5RkOHiGafJhzUI-maw9QKC3j_J8iHOKQKWC0mo7vXdXvG6UM_5KKMyjaPKnWupfJk04AEZl5GBHDKUHgDvbWisATwCOq7k1SgCz0AAwfutANCcoc1Jzbt4KvFKvtCphLUIK6hfh_76IEfDt6JsNZ0VqW1rynxIk77UjT3YYVKiDE_Xgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری کفاشیان از تیم ملی: علی دایی با دستور احمدی‌نژاد رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100628" target="_blank">📅 16:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100627">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
پیشنهاد ابوطالب به مسی برای دوران بازنشستگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100627" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100626">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
⚠️
🇪🇸
مارک کوکوریا:
اگر قهرمان جام جهانی شویم، روز بعد با لوییس دلا فوئنته تماس می‌گیرم و به او می‌گویم که دیگر روی من حساب نکند و من با این قهرمانی خداحافظی می‌کنم! چون فکر می‌کنم که بعد از قهرمانی در یورو و جام جهانی، نمی‌توان بیشتر از این جام خواست
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100626" target="_blank">📅 15:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100625">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soy14pmHj2kN3ctuPAj01dNLNL_tWoGgTO7AeM1YIV4FP23Nca4FKRTnQ1pSyvPjfYytF3KKr-IB4urKUTXAfEBuzxgVbzB04Cd9QgoydqFYnQ7H0bTMUac4iKEJ07_3kvHfwqhHEarjwVv1V_7MMhOLPnUm_CDC9fLU1PmhDrXKbS-iumMtLeI5PIP9HwcXJ__v0fUtsmIOGbVYvHbJVlYtg9dSluzcXBmGl2bjEKIFOLJOFr2uxT-W6nSyH9s498lIVX-Log6o5jYj7A_VposfOEUSGCwalwTk5MlzOlEkEH0bHAOHILWm_LH_8q_VsXKaQ9RItGyHxzxWszaWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
آرشیو وار درباره انتصاب وینچیچ به عنوان داور فینال جام‌جهانی: فیفا تمام دنیا را مسخره می‌کند. این داور اسلوونیایی یک فصل فاجعه‌بار را در اروپا گذراند، جایی که در مسابقاتی که رقابت و تنش در آن‌ها بالا بود، کنترل خود را از دست می‌داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100625" target="_blank">📅 15:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100624">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6FITRaplIQdo6MVg6mJ2e35wjh1PW7pSe6YpIgWpUBK1tQyRMTILvMSbPlJLIiuh_5TgcHiaS72KucPrT6gbprVGpvqKw6MtUnwjbd-LDZLWA_e0i4_zAEtYUXOUlLQdt9i-TboDghK-dU5Lh0iYGHbvjLnZu3J06sfuH91YMH-Iskznif2-9b0iaExdWZjyefzFQlopdhuendvK8tpYZnwfEAxGeAwfqFjVVc84M13VNZcRo5H38Sz-oixteWO02yIl2Cujhs3Lxl8efWzsJ4FV5aRzyYWUR2qm9qL53toGTPjfqLpDotJCjc530jisNn3kfCaJZcZGj8pcy8g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جام‌قهرمانی جهان در شهر نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100624" target="_blank">📅 15:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100623">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK4sy83Byr-6tiYwqZH2iOcR7GOQsEBJ5pJQK3G3f22_VEowqXgoAWU1-q97TpAWRviq-vmibwHJ43K8XSOg942NAkWb_p2oOrqk0etLaLUuL5DZQ5-MrDW5t1zAS3QAI_H1mUDdyb7lxCDj-47jSWKJjxFaorAAIZj0lu-tC7fU9g1VAp_Qced9gdusQq-BfvSQ4wuQU-3wk-F7aJvmbP7W8EkV7EBCS1HOErz1gBetZS0_f5zjgxEmZ3sXPnuK5dcXr06Egautd3YTlZKzEF28iihP0Ux87xNVU6ByzN8dLwG2z8NfHkNr2hFVKf2Imcqcd83B4uUAb6n9Zkc5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
کشور قطر در آستانه کسب میزبانی سوپرکاپ اسپانیا در سال 2027 قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100623" target="_blank">📅 15:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100622">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-cNLBk4rla9FMMzFPV1NpIPsIpqqIv7_NuDqcc3OQvesYAsjCqUR8TJJjZ5hhcPBCOWWElNFu9eE3235rAGmlNgHoTz0RNIrNAl3e3xyJbWErzgg-yzhD3rxUiEItovX-_9U59cg0BTKc5I0nqs9VPseo9WOMi_YuIAvXEUohKpWZo4Ffr0UQMAc9cuMPwBG1ubd8_PzT4BhyvFBIOxEVO0pXdWBMjtVa3Hoj155aYHgrK6JvfLyP-u_I0AzfZF2okdjyiIo9g2pRCLNHCAn1Q0Vokdqk7uWNah4GTSvEHCWuBx6Ks4Uy4ffxl4CVJprvYzY53osrVa3_pTyn4E9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
رونالدو:
«کریستیانو رونالدو احتمالاً هنوز هم سطح کافی برای بازی در لیگ عربستان را دارد، اما شرکت در جام جهانی بسیار دشوارتر است.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100622" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100621">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100621" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100620">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZlBJTHLvNMqZ60o_yous-NehCHxFMGfKaGXgKYxt_4RiKi515MsFRoN4jKtpGvdLtTlwC3kAyudv9h68u3iIQoO5qzc_IgDUbbXtpd1WTyb0KgX7QLCFVgBlAzh1X7UU1YdUaiDY7BuGO4luVvFtVBaQXF15ykycKptlZ8qZBVnAjq-Nh7fYPsE7NYs4NDA9H5hKjArtNuOF_RPRYXT1hEbPL5sqG8FKLbklD6I8bAr9ejByPBAJ8yqqADzla7PzjXxFlbKrf6bek-uupd-Yqwg41fRY7AerSuT90v4Io-zLEGCli-o_0tcqfA72GYDRtwuOTTtwu2ef53WMbBsHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100620" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100619">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=rte2GJvYmCxLPAOQ9Jkg5Q1CZrII3qPAJuVRUxf7nBmSi-7VHtNCWqtymXsQ0SL00hMmdcs52-7DUCBVEHsPl6laap8YDYUtyibiB3HXejLOzzNGJJcQgNvJhQjFq9xpZ-OZ-kDudmlU5ZV3EH_Ma0dbmponOnMFaULgNjK7E5YrAlx075o2Du4qA7iWDEqQJgZ0hkZ1ArX4X8zQ5qOIkJrNbM1391HJBhoGmgCeViXud-oOVko5GMvzebnrvpcVQhzaeYytmAxWkJNjh-WrXmsY6kva2D-3S8KpZ6UHE7yirZZjbdBLr0FXoME_-Mqik-9kE89NrCsKg5LRPp71dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=rte2GJvYmCxLPAOQ9Jkg5Q1CZrII3qPAJuVRUxf7nBmSi-7VHtNCWqtymXsQ0SL00hMmdcs52-7DUCBVEHsPl6laap8YDYUtyibiB3HXejLOzzNGJJcQgNvJhQjFq9xpZ-OZ-kDudmlU5ZV3EH_Ma0dbmponOnMFaULgNjK7E5YrAlx075o2Du4qA7iWDEqQJgZ0hkZ1ArX4X8zQ5qOIkJrNbM1391HJBhoGmgCeViXud-oOVko5GMvzebnrvpcVQhzaeYytmAxWkJNjh-WrXmsY6kva2D-3S8KpZ6UHE7yirZZjbdBLr0FXoME_-Mqik-9kE89NrCsKg5LRPp71dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صحنه عالیه. عادل غیر مستقیم رید به پیروز قربانی و تهش داشت از خنده میمیرد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100619" target="_blank">📅 14:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100618">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی‌پور بنده‌خدا ذهنش هنوز تو برنامه ۹۰ گیر کرده
💔
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100618" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100617">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=dMn1NDRAXZZND75Uz8KtzwtdLx8LICjtclBzdRj1aLe3gFmBKdT2SXKY9kEXCqTq_jOFvf8egyG7DAiRCodLy9WnoASJkcRFQ5vDuEIdqARgPm7kK56NyTJyg9nNZby9aLv7u0i3bJYQ_Luq6fh_Fgzky-y1W-aqjCgtylAYlCpmv-MnYa8_lkn6dsy3oToplPDHl1YP1dgwp7a22g5BYKLPBZ5xEtT3_v_khKOoA_NR3Vs34tK7wSjkNuNqtLXz4pJAdtDcqLTDbPChdU0oIBIf0QYFRKvo-QewORGiRiia7ruB69ry4aJ5bnQpE9sm5SPkpkZjXgbeaTOsWT4Azw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=dMn1NDRAXZZND75Uz8KtzwtdLx8LICjtclBzdRj1aLe3gFmBKdT2SXKY9kEXCqTq_jOFvf8egyG7DAiRCodLy9WnoASJkcRFQ5vDuEIdqARgPm7kK56NyTJyg9nNZby9aLv7u0i3bJYQ_Luq6fh_Fgzky-y1W-aqjCgtylAYlCpmv-MnYa8_lkn6dsy3oToplPDHl1YP1dgwp7a22g5BYKLPBZ5xEtT3_v_khKOoA_NR3Vs34tK7wSjkNuNqtLXz4pJAdtDcqLTDbPChdU0oIBIf0QYFRKvo-QewORGiRiia7ruB69ry4aJ5bnQpE9sm5SPkpkZjXgbeaTOsWT4Azw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇦🇷
خلوت اسکالونی با خودش در نخستین تمرین بعد برتری قاطع مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100617" target="_blank">📅 14:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100616">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=J0AAh3VAm_UWCrBzRYpmBmgKS6NCeHmlXz-5g0wv3RrMwF1RImsyDN5dJLlA1_COdWms8N8F6vGuA3MFR3vRzFvEahlDNkuLfrU700mE0zQNDQhxCBL_wnH0PqFWyDDQxlCO4KRUT3HFcuq1XIEvWtKtKpljrgd8-A4wB8I7-2LZCURxsuU-9Ku0Rg5b0G5B5ttigOIoLf_xzkguG85kQsBcHmyjOXAgOs4XB4m5dK854uBcuWuBbMpeO8QnJXdO57L4_2Ef_8r8jacKSqijW3yZExA9ZvU6Sif9FkAjfmRfylqCE6aPiBqtjvtMkb5awkB-W_P4xoAjRAjwULdGwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=J0AAh3VAm_UWCrBzRYpmBmgKS6NCeHmlXz-5g0wv3RrMwF1RImsyDN5dJLlA1_COdWms8N8F6vGuA3MFR3vRzFvEahlDNkuLfrU700mE0zQNDQhxCBL_wnH0PqFWyDDQxlCO4KRUT3HFcuq1XIEvWtKtKpljrgd8-A4wB8I7-2LZCURxsuU-9Ku0Rg5b0G5B5ttigOIoLf_xzkguG85kQsBcHmyjOXAgOs4XB4m5dK854uBcuWuBbMpeO8QnJXdO57L4_2Ef_8r8jacKSqijW3yZExA9ZvU6Sif9FkAjfmRfylqCE6aPiBqtjvtMkb5awkB-W_P4xoAjRAjwULdGwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
خاطره خنده‌دار شیدا خلیق از خیابانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100616" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100615">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=pqQ6xC2Ek0RmgjONvqUomqy_9qAlvmLU4MDWlBifHKobo4keZt98PjWxgkQHrz-0z-uOlVEPXX2D3u9N4ljPe6hXZqcaFROF77oplY3Qj422B9BJ7DboVPLv_B9XYlkj03Huv1FeunvhA6Qr0iQqYo6QEFz5amjoV9B8T0CBuUZqAX5RHFVvUmoc6xt6sReqIesurd-ntztsrlWGEuKnLvlIY-S6_u0sGrmfSdXCVeP-DnB5RgVdC3Nbu9w7YDe_1ET-yFSEj4LW3uUoCCHL886q_sdMVQ3AX3Ozk6Ho7D9YdD2br6xM9LXKCyNY_6uCmsag-2JN6saGxi-XH6D6bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=pqQ6xC2Ek0RmgjONvqUomqy_9qAlvmLU4MDWlBifHKobo4keZt98PjWxgkQHrz-0z-uOlVEPXX2D3u9N4ljPe6hXZqcaFROF77oplY3Qj422B9BJ7DboVPLv_B9XYlkj03Huv1FeunvhA6Qr0iQqYo6QEFz5amjoV9B8T0CBuUZqAX5RHFVvUmoc6xt6sReqIesurd-ntztsrlWGEuKnLvlIY-S6_u0sGrmfSdXCVeP-DnB5RgVdC3Nbu9w7YDe_1ET-yFSEj4LW3uUoCCHL886q_sdMVQ3AX3Ozk6Ho7D9YdD2br6xM9LXKCyNY_6uCmsag-2JN6saGxi-XH6D6bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
لامین‌یامال و زیدی بعد از برد مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100615" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100614">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtmNaWF1IH5jAOIRFDSq9U4PdYaKfNIfosPhfOw60e7sllKiwia5s9ni7YSSU0ePIza_wMhRjB1aQlLy9oB26Ckw5csWSFKSD-Zz_I3q9B4KFONz86i2xuTIt6zXyDFWTjVVXfd6wocu5xW1M5bj-r60UDYDvKS1Oxei3rUpZGKe4PBklKVdPK3krdLcpf9By2_t5M7Mid-qfzCIohEq1KhjEY4nwqLMSIgo48VqT8kD2HRzxUbQZyY9okv9UgA36PrH1SW-sNfeGJH6m3J-NI9dibdIeJ3ZGgC7rIgrVkeh_1XDUNin3lUkigmTcoIVcVi5ND54yBybE7mqQYKkHjDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtmNaWF1IH5jAOIRFDSq9U4PdYaKfNIfosPhfOw60e7sllKiwia5s9ni7YSSU0ePIza_wMhRjB1aQlLy9oB26Ckw5csWSFKSD-Zz_I3q9B4KFONz86i2xuTIt6zXyDFWTjVVXfd6wocu5xW1M5bj-r60UDYDvKS1Oxei3rUpZGKe4PBklKVdPK3krdLcpf9By2_t5M7Mid-qfzCIohEq1KhjEY4nwqLMSIgo48VqT8kD2HRzxUbQZyY9okv9UgA36PrH1SW-sNfeGJH6m3J-NI9dibdIeJ3ZGgC7rIgrVkeh_1XDUNin3lUkigmTcoIVcVi5ND54yBybE7mqQYKkHjDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فراز و‌ نشیب لیونل‌مسی در بازی انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100614" target="_blank">📅 13:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100613">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پشت‌صحنه تصاویر پیج همسر لیونل‌مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100613" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100612">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=Q4IrIaIO_KhYG-YA-fdb6iJsQVW1EUm8k9gxgFodt16jg3d5UDtomITQIwn5DL9Qpgy97CJ4I-hBQhv06Xx_5tKUTJmbvNxhbVlkcEB4tS9fNmjXBvu1xjHU1oL3uQDgW5i2u8whtqU4DKfEfcLfVvkqEzRlUnFgCtl2q_UalXY_iPE0PGdE5GUu9WHp_gSizG65aFpZ6Iuh_4Co8uz44AyjP5HMfx9KztC7do1Om4N3We4E1JsL5QmdALR4xqlGn-joYhJ9NSPkzjfknZ14ipCDRZGIxQQQwbwVbYkavlnsXo3shLq2-KNOsPES83FUF9ggSpyUwpu3vQI7NKACXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=Q4IrIaIO_KhYG-YA-fdb6iJsQVW1EUm8k9gxgFodt16jg3d5UDtomITQIwn5DL9Qpgy97CJ4I-hBQhv06Xx_5tKUTJmbvNxhbVlkcEB4tS9fNmjXBvu1xjHU1oL3uQDgW5i2u8whtqU4DKfEfcLfVvkqEzRlUnFgCtl2q_UalXY_iPE0PGdE5GUu9WHp_gSizG65aFpZ6Iuh_4Co8uz44AyjP5HMfx9KztC7do1Om4N3We4E1JsL5QmdALR4xqlGn-joYhJ9NSPkzjfknZ14ipCDRZGIxQQQwbwVbYkavlnsXo3shLq2-KNOsPES83FUF9ggSpyUwpu3vQI7NKACXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه‌های سسک‌فابرگاس درباره سرمربیانی که پس از زدن یک‌گل وارد لاک دفاعی میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100612" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100611">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbCZPPPjRYbyQ00KX-9_kC1BaoyJWvcF3eKxmTXpJCFhHIPOUM5j0nKuYCF2ctJhyQUkrE6iobAUNRum6ndGC4KEjGKpRlTWUiQlCje7hNeuYxLRNmHDLWahvQoohrsJzGy_pp9gwIqUC4bgx67C4wb-DmaTwUjuc_Yx4xCA6OlgCj9wPvTIA_RMCLQr3OGlc_ciq89IJ1mYgFZjuW8GeFDxm_Mx6MSR4acGMB34pEiMQklsqvQRmJErkNuufbzOHmv_4BGOZ7o-20hSaf3IqNyLS7PJN3-9bH49CkpSxizeXjh4oo-nkGb4J_s78Hp5syrWwBeCevTBiV4epNC78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با توجه به صعود انگلیس به نیمه‌نهایی جام‌جهانی، بند فسخ قرارداد فدراسیون این کشور درخصوص قطع همکاری با توماس توخل از بین رفته و اگر سه‌شیرها بخواهند توخل را برکنار کنند، باید کل مبلغ قرارداد وی را پرداخت کنند هرچند تصمیم بر این شده که توخل حداقل تا یورو ۲۰۲۸ ابقا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100611" target="_blank">📅 12:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100610">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b380c91827.mp4?token=UZazAln6nHBj7hEw9_1r6VBJDKCBO95iFkyKKGZpECqQTLmCT766jvNqZm4PRxsFPdvI1H8JX8JaHCj0CFLfgy_dgrpnlp22cXotACk1lXRU7-is7RfTlG2HrJM7vWZD3KetDPp2yPSAotlu5XJpKciP44BaOOHsJHswXpIT_mNdZ6NK3ITl7SMZIKPuCUsBII4aVLtIP46zIcFYovcTD9Ahm5IFD_Qh0PBH5gYJjX_-UWHGu8WgFwD1TFbFqFR6G1koUG3XF74O24qQzbVkp8VnT2plYZxJClx6VWT1cNrlXspwL8AqSIHgducfc9yz3C8f4REYLie4T2WAN6968g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b380c91827.mp4?token=UZazAln6nHBj7hEw9_1r6VBJDKCBO95iFkyKKGZpECqQTLmCT766jvNqZm4PRxsFPdvI1H8JX8JaHCj0CFLfgy_dgrpnlp22cXotACk1lXRU7-is7RfTlG2HrJM7vWZD3KetDPp2yPSAotlu5XJpKciP44BaOOHsJHswXpIT_mNdZ6NK3ITl7SMZIKPuCUsBII4aVLtIP46zIcFYovcTD9Ahm5IFD_Qh0PBH5gYJjX_-UWHGu8WgFwD1TFbFqFR6G1koUG3XF74O24qQzbVkp8VnT2plYZxJClx6VWT1cNrlXspwL8AqSIHgducfc9yz3C8f4REYLie4T2WAN6968g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شوان‌اشتایگر اسطوره آلمان بعد صعود آرژانتین رفته بین مردم شادی میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100610" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100609">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=oFyledJKZEL9opCTqM-lrXJG1OH8jKaPqgaU9JT04RUnTKv3kUD1xeyLQelYCPQEyz-CBk3966TEfCASO6TVJ4BBkUE0KR2-HlrlUbv_fnF2c72F-K5ozPOQVaKdj_eFZUkGZ3kI4WhRm0aqJRDO6jyXCc6oiQyBLASp8GkfBQYvKTeC04Di5m-KdF8exJ06fcuD-hL1-OZjXmPGLAuWi11ruZ7Qg6VzMP3gdtj06Xhrke94Inn76y5FmTlewyxtTuhSsDlpMqoeful-sjis0whgrmhvgxtYho7UEX7hlOMw6SRI5jkK99eL8DQbQ81EsbtqE5yve-Es1npBLI4NZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=oFyledJKZEL9opCTqM-lrXJG1OH8jKaPqgaU9JT04RUnTKv3kUD1xeyLQelYCPQEyz-CBk3966TEfCASO6TVJ4BBkUE0KR2-HlrlUbv_fnF2c72F-K5ozPOQVaKdj_eFZUkGZ3kI4WhRm0aqJRDO6jyXCc6oiQyBLASp8GkfBQYvKTeC04Di5m-KdF8exJ06fcuD-hL1-OZjXmPGLAuWi11ruZ7Qg6VzMP3gdtj06Xhrke94Inn76y5FmTlewyxtTuhSsDlpMqoeful-sjis0whgrmhvgxtYho7UEX7hlOMw6SRI5jkK99eL8DQbQ81EsbtqE5yve-Es1npBLI4NZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
همسر لیونل‌مسی سرمست از برد کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100609" target="_blank">📅 12:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100608">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=P1i8DYLRfI84-iGizxUAKqqVTbAvfFjM5xsKxm2bp0zY_HWdk1EomA-xlAGyTK8Q0HAyXeDpqnLb8aKl2nzvjvFGDBIbQtbSoHPWhSEyOYrjHWevUWgr1aTJLe3njNyyWcrXFSj3ypV4b_5UrKanC1r_Fco3Kl62IUpZosx2H_LdwB4MVFkLQlQd9q8HC-CkBCrQ3YiUvQgRmSC_G1zkPKHvBorXWFHVufH4c2ylyWvxDMnmcA3RZPC4stUGVFBtnpjXe7I5iWO_rC_kb1vTlOxNB9B0WqtMI06hTMbeBz4aNVyYvLzkOOMHEJmqWIgnGja1qmDpEZNNZ16t43lp2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=P1i8DYLRfI84-iGizxUAKqqVTbAvfFjM5xsKxm2bp0zY_HWdk1EomA-xlAGyTK8Q0HAyXeDpqnLb8aKl2nzvjvFGDBIbQtbSoHPWhSEyOYrjHWevUWgr1aTJLe3njNyyWcrXFSj3ypV4b_5UrKanC1r_Fco3Kl62IUpZosx2H_LdwB4MVFkLQlQd9q8HC-CkBCrQ3YiUvQgRmSC_G1zkPKHvBorXWFHVufH4c2ylyWvxDMnmcA3RZPC4stUGVFBtnpjXe7I5iWO_rC_kb1vTlOxNB9B0WqtMI06hTMbeBz4aNVyYvLzkOOMHEJmqWIgnGja1qmDpEZNNZ16t43lp2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمایی از استادیوم محل برگزاری فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100608" target="_blank">📅 12:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100607">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=jp4ndBNqjS5cjUNjT21bNnjtb733JFLB8LMUW7ctQcE4okcEEA0-Bq1u6r4SkGBleJ_oMUTArGYHQqDai5KuS_9j_8lCeIcxB-g_zGgqYUEaijzp93ACW0ROplDlnFiK_p1aMYI5GyxuThgDpAYW83Ip59IDE9kH0HIV85v8uyOL0nQ24VTV-fybafM8nX1uFN3FblUgsyLTrc1phvnMMGKyHMvOE6evTz6k1bg468HfOmTydd4Gj8KaNaICe-8BcwDVlzpFk5Df0bHM5a2dMIy2lFUBN8AmHqOf8rpCM8YztrJAvB_ZZXGP0zkFoyxoRO84cQeu4Y1Nhye18u-aDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=jp4ndBNqjS5cjUNjT21bNnjtb733JFLB8LMUW7ctQcE4okcEEA0-Bq1u6r4SkGBleJ_oMUTArGYHQqDai5KuS_9j_8lCeIcxB-g_zGgqYUEaijzp93ACW0ROplDlnFiK_p1aMYI5GyxuThgDpAYW83Ip59IDE9kH0HIV85v8uyOL0nQ24VTV-fybafM8nX1uFN3FblUgsyLTrc1phvnMMGKyHMvOE6evTz6k1bg468HfOmTydd4Gj8KaNaICe-8BcwDVlzpFk5Df0bHM5a2dMIy2lFUBN8AmHqOf8rpCM8YztrJAvB_ZZXGP0zkFoyxoRO84cQeu4Y1Nhye18u-aDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ویدیو وایرال شده از گزارش بازی آرژانتین و انگلیس توسط یک پدر ایرانی برای فرزند نابیناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100607" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100606">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=ABigseJz6Ol9DRK_-QduetfvvmkIuw9w5PkwtWnceAU91SZTilDbceS06qOgEc7kn-SgBvm2QY4Po8tguTxZjdaNQyAD0cIpeo-q7ZHbtJmicNvtH_Fy8hgdOTECHedEYR4kr4j5grRvs0y-5t9f53wvMzfkpLVEUUVw8WKPeC58QWsokSLlJvV8o85ywunXTtk9MfudeLZqgtmyH0QqpzwagZ4O_ZmeczPh5pSFU1O233oidBzNiNs5eDHmahSqPiQAgxRb5UzdczuW933pFdHg1EsR7m8P_Sm-C221miJSwasL1rx6_Ewmc7uhqCj6Yk0vyaIsYIuh9XvH_8ODpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=ABigseJz6Ol9DRK_-QduetfvvmkIuw9w5PkwtWnceAU91SZTilDbceS06qOgEc7kn-SgBvm2QY4Po8tguTxZjdaNQyAD0cIpeo-q7ZHbtJmicNvtH_Fy8hgdOTECHedEYR4kr4j5grRvs0y-5t9f53wvMzfkpLVEUUVw8WKPeC58QWsokSLlJvV8o85ywunXTtk9MfudeLZqgtmyH0QqpzwagZ4O_ZmeczPh5pSFU1O233oidBzNiNs5eDHmahSqPiQAgxRb5UzdczuW933pFdHg1EsR7m8P_Sm-C221miJSwasL1rx6_Ewmc7uhqCj6Yk0vyaIsYIuh9XvH_8ODpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
کرم ریزی بارکو بازیکن آرژانتین که باعث شد بلینگهام کلش کیری بشه یه پس گردنی بهش بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100606" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100605">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=B1-eFJVOhSdbENJ5lU2fvBiYU1_PU5uSIMirYjdvC8azjdnNk4zdIEawztaZBJQMZFMtLl_2xdVaq6edjYBYsxG3xRcnttakmSYx7UkAQvr0eZXEdwAOFuGj0fAxhj0cbJgMDsIfgprwvgnhejVWulDN0SnuB1OCdbLEmtUbODPLe7wiKxYoDaeVL8xN5HOEBSRp3qqqUtTqBU5Fh39VEgK3XjudxpNVKfHbXMX7DalX4ht96jF8FIE4Sck0DqQWkNA4KlV1ydA1uYD4GtTqG-FR70JxyL5p_1YYO1Mx14v8ATmmkZT9W4v5PpBkAWx0GTmGYcxOGiZlRsOU6kTtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=B1-eFJVOhSdbENJ5lU2fvBiYU1_PU5uSIMirYjdvC8azjdnNk4zdIEawztaZBJQMZFMtLl_2xdVaq6edjYBYsxG3xRcnttakmSYx7UkAQvr0eZXEdwAOFuGj0fAxhj0cbJgMDsIfgprwvgnhejVWulDN0SnuB1OCdbLEmtUbODPLe7wiKxYoDaeVL8xN5HOEBSRp3qqqUtTqBU5Fh39VEgK3XjudxpNVKfHbXMX7DalX4ht96jF8FIE4Sck0DqQWkNA4KlV1ydA1uYD4GtTqG-FR70JxyL5p_1YYO1Mx14v8ATmmkZT9W4v5PpBkAWx0GTmGYcxOGiZlRsOU6kTtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلاوکو وینچیچ همون داوریه که امسال در بازی رئال بایرن یه کارت زرد سخت‌گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100605" target="_blank">📅 11:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100604">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=WvgnGmG-Qe__TC2HwJnYsCYA-0SqS--CXvzzX_hl1WLk-2QEWAo8Km73HqsskS0HT5hbK9XcIlfDptT5oT0kDxykyzvgdyXuVbcp7-SF9ufP072Xf0s5wTE96RX_NyU-Z3cxgKf7gCh2q42ubbl2IOXMRUVcD3CI3_hzQdzL47tX5tMWBOfwltZtDe144obCm_9f2jVyzX22DbcYE3QuZ2atbb07Hq3aZbvISM_pWgwvUl8gknTxMSJmRLJWY2KPAYzS9M_ZtBuzt7l44eULZsqUJ4xqii4p7G8pF9f8Gy1WByBj5vcp-lGq5gwhB0baP2E5kMk_CcfCf98XCgiuy5f0a7BzLJ6-aI9e3N02KSLc0CSK61mds733iXC9y3jx_Vkz266p11iZzu61VnFMdytNz8vmps26JlgaSALzeKoc95MVq5X_KyaNM86m-3s_yJhR-sYkpJECWTue7UG8A4p77V16QpF9WECB49c7iqcu-2N04IbuG-y5i4478Uhb5wNDJ3cVvrQse8lGiWyl_1ZOBcQgDw_3ztK0j5kACNtXtM0sFsJwvqWec8C0-ay5vp9Xpt_JskDXWDCthm_5ODMr6cdz5hLgjqbvo6lKD-ZeM1P_WCCTxDn1R-cLTOqdkPt8lVQ_wWdXdGgPS3OH8MXuFAt7W_z00aE_ibZbTYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=WvgnGmG-Qe__TC2HwJnYsCYA-0SqS--CXvzzX_hl1WLk-2QEWAo8Km73HqsskS0HT5hbK9XcIlfDptT5oT0kDxykyzvgdyXuVbcp7-SF9ufP072Xf0s5wTE96RX_NyU-Z3cxgKf7gCh2q42ubbl2IOXMRUVcD3CI3_hzQdzL47tX5tMWBOfwltZtDe144obCm_9f2jVyzX22DbcYE3QuZ2atbb07Hq3aZbvISM_pWgwvUl8gknTxMSJmRLJWY2KPAYzS9M_ZtBuzt7l44eULZsqUJ4xqii4p7G8pF9f8Gy1WByBj5vcp-lGq5gwhB0baP2E5kMk_CcfCf98XCgiuy5f0a7BzLJ6-aI9e3N02KSLc0CSK61mds733iXC9y3jx_Vkz266p11iZzu61VnFMdytNz8vmps26JlgaSALzeKoc95MVq5X_KyaNM86m-3s_yJhR-sYkpJECWTue7UG8A4p77V16QpF9WECB49c7iqcu-2N04IbuG-y5i4478Uhb5wNDJ3cVvrQse8lGiWyl_1ZOBcQgDw_3ztK0j5kACNtXtM0sFsJwvqWec8C0-ay5vp9Xpt_JskDXWDCthm_5ODMr6cdz5hLgjqbvo6lKD-ZeM1P_WCCTxDn1R-cLTOqdkPt8lVQ_wWdXdGgPS3OH8MXuFAt7W_z00aE_ibZbTYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو ساعاتی‌پیش از ترافیک در مسیر لار به بندرعباس بدلیل تخریب شب‌گذشته پل ارتباطی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100604" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100602">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=IsaV3mILGRbyGsFdyM8tzJy94CJpc8ao5POOklMrIRvaKz2PpfJJtNOQZkD0aDB6egbzBC6MBejgmH9DDq2hCHN95-GsTmfKADZLtTgdBrtp6Z1kH0PdukKIuIDFyeXJcosdDOPYa9BxDgRYiZYpNFLa5LfdLLQixG3cZ38fmhg9669hVk85_U88qIkZBr45UokTxd7HhvhsmYCRIy0BAPRx7F2W6ln2_WK0NvdAy8mT41dd_rar6k51t2DiTsWhV0JKRsb7mHOO79eUV6Hd6zjBaju4AIuc-jO9JYhuqmIo36H9g46RfvIQodUW-JjoEMvUI0s6hKJ0yZm_5CvFzihOkGxeBd0kbE2UAxntIpVPsQq5Q3szyNGgWnszMPWi6XW6DX__JjdVOhNL8M3R4nertVcf-z4SfTsXuOHqqJLdsg9Tw45ztLvGK8iKgKCAn3JGCFQew-Q8p7wiieP1AUct-d27d8uoGXWQGFaB_cRTp2eyf4zeJ9GIPgRYhxhtUBs1s4ut_ZTkYcWqO1eHLRObNQF5x5bl3Y_y6A26X_1gSg_VfifrGtCkAcqvKeyWv0EWboSgaRCNxaqE0gy0DzyZUQqj9ZXigcLdrADxxbZZvaiCVbDBiF4zUzY1bsgufQlBfAtqdpMc2s_DAKBE3qvhQCY8c9bUXa9MJhKtQA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=IsaV3mILGRbyGsFdyM8tzJy94CJpc8ao5POOklMrIRvaKz2PpfJJtNOQZkD0aDB6egbzBC6MBejgmH9DDq2hCHN95-GsTmfKADZLtTgdBrtp6Z1kH0PdukKIuIDFyeXJcosdDOPYa9BxDgRYiZYpNFLa5LfdLLQixG3cZ38fmhg9669hVk85_U88qIkZBr45UokTxd7HhvhsmYCRIy0BAPRx7F2W6ln2_WK0NvdAy8mT41dd_rar6k51t2DiTsWhV0JKRsb7mHOO79eUV6Hd6zjBaju4AIuc-jO9JYhuqmIo36H9g46RfvIQodUW-JjoEMvUI0s6hKJ0yZm_5CvFzihOkGxeBd0kbE2UAxntIpVPsQq5Q3szyNGgWnszMPWi6XW6DX__JjdVOhNL8M3R4nertVcf-z4SfTsXuOHqqJLdsg9Tw45ztLvGK8iKgKCAn3JGCFQew-Q8p7wiieP1AUct-d27d8uoGXWQGFaB_cRTp2eyf4zeJ9GIPgRYhxhtUBs1s4ut_ZTkYcWqO1eHLRObNQF5x5bl3Y_y6A26X_1gSg_VfifrGtCkAcqvKeyWv0EWboSgaRCNxaqE0gy0DzyZUQqj9ZXigcLdrADxxbZZvaiCVbDBiF4zUzY1bsgufQlBfAtqdpMc2s_DAKBE3qvhQCY8c9bUXa9MJhKtQA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اشک‌شوق وینچیچ پس از اعلام قضاوت وی در فینال جام‌جهانی در میان تشویق سایر داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100602" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100601">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh0w6D6bBcnkWxPPop5S59BVBqv7aJJ5bJoyVcKeVOCaAYRg7feQmPUz0HFacayvQZiqKkUh4e4NAjjeqIW_BeYPn6GtNpt2L5UytQ6R0zJmDPobBGVf2cI_gEwNIhpaUwYaShYgUWZEP80aIEUsAEwOkTtPYPnMYU5QZ6TzYrOK6HwnAOGmj04UNgU__wJf9_rYppyH6-4KI-Szdsr47REGD7MadLsB7y6vMhnj5KbbRkihxLgwwU4-olp83AANfy9mSF0tm-FpQ-dp7zj3ndqj6b7hATO4OLIJPKnb-Ely0COVMAe17FmqHUO_KEby0GCVoBOrXtRDYv2Yv4MxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آخرین رده‌بندی توپ‌طلا جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100601" target="_blank">📅 10:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100600">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=bj619vvq0IJeg8GqIcxb9aPTmcYjuWiqYfnLmmquRAgj2FHNW66Q1CgOM9v8EliYmgmnJr5Cbujbd8iFL13SiE4QRL_gy4z95s-xvp2gRDJsvdigrO11RXQ5JjyzPdQYFJo9gkd-Jo4g8jUfT9ZQQ9gGVgNjHxnNZXOOh6GL-McAQev8HMj2AO-FCj7Dqw6zorYbM0nAeYzudsJJr_L2d2iatocHn4OnypcekfdAn0qP_8j_itMhm9H5YFdipiYarel1__KPIaIYFgv7IXWdv2TwGsO9yJPd3aBbBR-b3Yyba5pbepKpLw9v8rUefw6ledOHs8rwMOgOoTHIYdCP5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=bj619vvq0IJeg8GqIcxb9aPTmcYjuWiqYfnLmmquRAgj2FHNW66Q1CgOM9v8EliYmgmnJr5Cbujbd8iFL13SiE4QRL_gy4z95s-xvp2gRDJsvdigrO11RXQ5JjyzPdQYFJo9gkd-Jo4g8jUfT9ZQQ9gGVgNjHxnNZXOOh6GL-McAQev8HMj2AO-FCj7Dqw6zorYbM0nAeYzudsJJr_L2d2iatocHn4OnypcekfdAn0qP_8j_itMhm9H5YFdipiYarel1__KPIaIYFgv7IXWdv2TwGsO9yJPd3aBbBR-b3Yyba5pbepKpLw9v8rUefw6ledOHs8rwMOgOoTHIYdCP5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
تعریف و تمجید فوق‌العاده علی‌دایی از اسطوره داوری دنیا علیرضا فغانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100600" target="_blank">📅 10:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100599">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-hu-AgAKaqpGN6V4jOaGWnBgcEljykL7fxccrKp6VwGPO8RCmSDF9iJ6GrZAHbvUROg0J6BJnZlJQMDdmCUrNYxg_otgCyobXzyAmmBbOV2SyjW6BqsvcN6729j0lONnZNHW_HqCVE7x6LnJHkyHvEuu3cM_TVk9Gs1wbKSrnfRu-b5y9J2qEpAzOK5--0a21bcv6N2DRTDRkYImPg2G73he53gkCdyuDWHM2cmFO6of1I1QQrMpFHxLZbvBiXouaDFgGbN3Qwmxmvrc8waF89QuDyz4XfxD1P0aeZxmsNck2BLGIPuAwu27jhh-msje9Nkyw66KCUtAH8mTxt9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
سن بازیکنان اسپانیا در دو جام‌جهانی آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100599" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clev_jEt-rpOi_WsmJ6uDCZVOl2anTf7Hy_nUVigH-hW61IZX4X6sQlUujw6h9yVJplAbemACvLa481dgVN83bD17UoS0DjfxTo0j8KVhZlU-e0BEXonnWJhAIPUxROmmWAaSDy3dLTQGy7EdYhw_aAUaxweEykd2IAOItE4Qlt3pfImcAynieveIS6p_o0mMNDi4qEvN21hWwTuXDHhCbDCGFS8QFfhzQ5LxZ6kAQAE72bYOQltWeYvcAdIlgusemvScFrUskuvpp1EbqQcx0Af5aDH3G4ppUce_kzm-1whOesAz-G_FhNpVlSBKPJyghAaTehKT3DX_LdbCEm0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZuZRRrPqGJqT7GIJe7e2qy6bRhesgJkdyiteScLT1-dVo4flCk9AidamU3z1TS1F6m86vIyG6oyTHfZhz6jqCLsR2Q2yyRDlaeIMBYvz5jDzdeJ9Qf7CA9GIqm5eoS6gUhN6o1pgr8imLNY9y_XR-g6Bpq5J5C2nfg8b6BbLlYH8limEwdX0XI36o_y10EiJmMZ3nOuZmX5F7QfVmYOoXO6CP-mTsDLmB3RYr8ksAksLmgYSK5pfUTJuXeeLRJup6g2D2DZBYNBpwD4xsxuWrCXh0p0qODImbgU6-yUnBvRvKx0RqZoinEU5C9i18GqTN-tRa9tOhCpx7o80nwRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7V64SVBTclIvsId_1yYdlXKGq1pBzlf7yzUOfUBIZaCGjeE7ZjFb8yzzJVBHHPQbJZHqK1gPd9GqK6INBlQP4x9l_FUrayED8jOO826PeRSNhgg-bKJsyhNC3mt_857S6UCpeSm2sb541rmMByyg3XOaeQ2_ccM6NxqFiC3jA5QVp_pcMqo434R_wyW-weAl9HM8mqUAYVppyQCgIxCvKLVBssBDxIVJQgsQbqPqH6VxicoXc-z2GaRTulvzTbvILogF8NRkRw4X95QfbkIlj-ke50KavIo7cc1ba-zZtkcykqmjeopMJHc2sM353HuoObNyLVSfZLYi7pH-xjGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sA2l0LPH0MC659R2ooDQSER5ra-PTdpi6kvs0DGwsE7GFxQJ20MFg19VUYdw5ujiXS3eXtewNHe4RPhlPJdSzhgMBC08vOxuhGTQftvayFbXTJ1yEWC3Gvd5uMuk6L_oPHToJtEA6_Boc-x7wCx0tS-17GoriXZRnFW9zbCbvS8KQ-c_MhJiJMbjqTYGA0GzW9AGi_UivFkzrwxVdk9rENLEFWNgBmsILQr8DJIgiTUgUGMynLLBF426x4wlPf1_UXiMbBoktuWcbCt0MU2PERlj79s4FtkOFPNpOiR3lnzM7nTSHrBypi29KpJU-Xfl7pfUdFS2wUHbmAFk2EUzRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
⚪️
12 سال پیش در چنین روزی، تونی کروس به رئال مادرید پیوست.
⚽️
465 بازی
⚽️
28 گل
✨
93 پاس گل
🪄
121 تاثیر مستقیم روی گل
🎖
34091 پاس
🎖
974 موقعیت ایجاد شده
🎖
94% دقت پاس
🔹
🎙
کروس: لازم نیست همیشه حرکات نمایشی انجام بدهی؛ اگر با دو لمس توپ بتوانی بازی را کنترل کنی، همان بهترین کار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100595" target="_blank">📅 09:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100594">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4324684be2.mp4?token=R41rh8o3pqsZiGulM3IEZfVI9joavVZsn7jFgT5QT6-4MjS69qwdZfk3cvEJ6NJLfVz9n5TEhFdNMZEs6gTu5yBmqAWsjAr7wXASLidymrxJkT0wO3v8WLg4kCtgVumuEnocSJuDIO_SO1bB6TFS0fIhSNx5CoQghPjrf48gWmo9kx9Z5feG0u1kBXt4wkFAxYUTbSSJwERQNctHwzqVHoBUkiMXZZ_0eJwuAfygB-qPyx5cAX0nc6X0iQHV2z8dPK3zAvtPxfF2ksXEqe6n0Cxq_wa7Xab88DkTzjHYmlP7EuHzGZEWtzt2-wsxqU3siTTuJwqp0OmowqJpOHqGug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4324684be2.mp4?token=R41rh8o3pqsZiGulM3IEZfVI9joavVZsn7jFgT5QT6-4MjS69qwdZfk3cvEJ6NJLfVz9n5TEhFdNMZEs6gTu5yBmqAWsjAr7wXASLidymrxJkT0wO3v8WLg4kCtgVumuEnocSJuDIO_SO1bB6TFS0fIhSNx5CoQghPjrf48gWmo9kx9Z5feG0u1kBXt4wkFAxYUTbSSJwERQNctHwzqVHoBUkiMXZZ_0eJwuAfygB-qPyx5cAX0nc6X0iQHV2z8dPK3zAvtPxfF2ksXEqe6n0Cxq_wa7Xab88DkTzjHYmlP7EuHzGZEWtzt2-wsxqU3siTTuJwqp0OmowqJpOHqGug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تمسخر مجری شبکه ورزش توسط ابوطالب و سوژه شدن آن در رسانه‌ها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/100594" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100589">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=SmADOarocl1o2fng5BPV1ZND11aMVDWyPB5VJpSipdfRgsAYyyYi-YyXR423xpqZy_2OCKHCQDiQt3suD-nvPjGQMrwuUZgylGp5BqnH-eFKI29XgQdzCgxN6Nhhklc7FNyjIy61fhN5J5TJOBO8cEommGxwMIJzUB251FOgCrF9sX7DxmjEQQyQMw5y8Ci6A3jWEYdtzP6E7e9ONFsQ-0EmYjpwS5UckgficoSwTXVqgY2Wjbt2JPLFQETnkyL_ud6IcWyWrBpuaG5zsSLLYE2f4GRRQw__wtY0OmwKZMhRKml8ix0eb8VSTjilOmUVZxIMllyxfdAUZpeaArJXxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=SmADOarocl1o2fng5BPV1ZND11aMVDWyPB5VJpSipdfRgsAYyyYi-YyXR423xpqZy_2OCKHCQDiQt3suD-nvPjGQMrwuUZgylGp5BqnH-eFKI29XgQdzCgxN6Nhhklc7FNyjIy61fhN5J5TJOBO8cEommGxwMIJzUB251FOgCrF9sX7DxmjEQQyQMw5y8Ci6A3jWEYdtzP6E7e9ONFsQ-0EmYjpwS5UckgficoSwTXVqgY2Wjbt2JPLFQETnkyL_ud6IcWyWrBpuaG5zsSLLYE2f4GRRQw__wtY0OmwKZMhRKml8ix0eb8VSTjilOmUVZxIMllyxfdAUZpeaArJXxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
خاطره بامزه خسرو حیدری از فتح‌الله‌زاده: روزی سه با گوشیشو میشوره
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100589" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100588">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=CeXxs3yEfyPXltIdwPrdcgRA7_jn1W2MpOX-WGINodcGQ2t_3M2YKPt8-FHBZRIOg3-zfzaisBoxwSAhbeBvH-q3375YhpCJnfwHcAIhunVqmYiPpDPWb7hQBKUUCsPfsei4bHPCoi10CapiDRYi_5XMwWITHgp8wlICyll0x1dbHGKgIqxC-8yxJXjzrkLp1yDlbtUzNanS4V_74y41vd0HRv6PflHoIdph0IgghTP0iG_cHoDXi91JqGfLQdBqqGZ67fo8ydxJaRvFddxN0QjQOJeMtrEOXsLxKwzLX-_6rNLa1ayLPFNYkEqKBC-_h9nrZzXl382LI8ou55ZKJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=CeXxs3yEfyPXltIdwPrdcgRA7_jn1W2MpOX-WGINodcGQ2t_3M2YKPt8-FHBZRIOg3-zfzaisBoxwSAhbeBvH-q3375YhpCJnfwHcAIhunVqmYiPpDPWb7hQBKUUCsPfsei4bHPCoi10CapiDRYi_5XMwWITHgp8wlICyll0x1dbHGKgIqxC-8yxJXjzrkLp1yDlbtUzNanS4V_74y41vd0HRv6PflHoIdph0IgghTP0iG_cHoDXi91JqGfLQdBqqGZ67fo8ydxJaRvFddxN0QjQOJeMtrEOXsLxKwzLX-_6rNLa1ayLPFNYkEqKBC-_h9nrZzXl382LI8ou55ZKJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
علی دایی در دفاع از مهدوی‌کیا: با او چه کردیم که با دلش ملی بیاید؟ مگر او را دعوت کردید؟ انسان‌ها با ارزش‌هایشان بزرگ می‌شوند، نه با مجسمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100588" target="_blank">📅 09:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100587">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZBpWUK-c0rStIInSuOu9pR8SC_7lYzcBnn9701h75FLXv0YeRFQAbwQ1FsIPSyMZYCQBvT5gJQAVOPVcLr2Zmg8tLNv2wk5rkVql5SxAQ0bm7Yw-OmpY4_aKda9adNeNlxzyrv-sTtXkCWJqppr8hMp6E58IoF-Kii4gpkSO8JnwvlYHolCHrQ8NgorguXSIB_c_dbAau2vFnJfk-RjvxgveSkdd5fG1e0U2axKvoVF-Fi5K4z-qIfXs8PvSRPY1kbJdvAwmq389BFw8LdTOM31e_E-GIkC3-hctwqT3VnrJxbWqP8lnYmu84GytFfXltlF0KlVOkfjQ6GXaskfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
فیفا اعلام کرد که برای اولین بار در تاریخ جام جهانی، "نشان‌های قهرمانی" به همراه جام و مدال‌های طلا اهدا خواهند شد، مشابه آنچه در NBA انجام می‌شود.
🔻
2026 عدد نشان قهرمانی تولید خواهد شد. تیم قهرمان جام جهانی 30 عدد از این نشان‌ها را دریافت می‌کنند، در حالی که 1996 نشان باقی‌مانده برای فروش به هواداران در سراسر جهان عرضه خواهد شد.
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/100587" target="_blank">📅 08:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100586">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB3Ccw8kKpco4fc3XygWcjumMU9gUNETureHzOwSn-qwQtxaN9KVfgLFFAUcZa2s2YlZWInPOKNTgatKpmdQc20VlPrglN0HW62nPcisvqEhbSXo4bxID0g3dKQ0es-ksjX95nN5U22Izmz_wn2ZHUmwWAaMeSDec0oB2Wjo7H11OTlIgImEO0oTMPPF4QP1PEGjsRHa-yrgkTtQiZGtxEaVOfJwT3OjRXumr2hy6tkfZpTDZWHdj3MTOhiE0nBY_pKUo_dwNUMfp-m3qmuCyKq8bPuFUJTymomnc7PNQm1rghzWlG_DRa7cCgcVT_JOi71t4LSnQ5zk2FwlYK0gBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#رسمی؛ با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/100586" target="_blank">📅 05:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100584">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHIctPbU4ynji0GN1F849NrpI7DLvJSLm4kjYK9Hhvfo0c3gd_ygJ43I-aMWfsQQEk3PixE3JtDAr6KbfVtGNj4S4LFY0p8xSWzMv_g-QTEuM2wmBW_wPOTT2-nNfdzuLfM7RGdDERa1h4FS8yx-J3Nl6sD78uXWROVg2fdRSTn01lSk2jz0frZxj3UPe77yzLxa6kz0C3-e7AgYzNT2mzUmSXrfTzSifoFfgeAH8gWYGyCNCwdU61ywHrwYJvaeW3NXFo6AhVygs5i0JKoXQMKwQDtYStQYrEToHHBlJVTtNQk_I2Zp0VZtn_aQPmO9sh4pVQwTpS5FCp4JEfG6Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o51X-Mri-9JLO6d1sy4mgSSRXGe6Pdt9UxFJU0em0Er0AW1hJ5G5Ad34jjteihgioA-HVQC6eHI2dBuuslJvrh1VXNQnE2YUnRKK1qXgEq9SAURjvDfDCdWygwbQB86jYOxAvLetO32kPtpNPFwOP42ooPGakFKTC5O-sgkGbFn_LH7lLl1IPHrT4NCL-bctRekGw4FeTe98Vhkv6e7qxCy1FxLoRnBaSWukVeRe_APr59M04UcnNpY4mgCh151GW7_PPvDUdK1j-4p-_tpZ5uNydE9wx3jYhXwpGXF2IYcV51K_QIkWoe4lwR2cpXTjB0k3b189ugL_U4A2Ev2wQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
لحظاتی پیش در پی حملات آمریکا، برج کنترل دریایی ۸۰ متری چابهار بطور کامل فرو ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/100584" target="_blank">📅 05:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100582">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ME4at6msWqzdnDJGSRy3w9NUYx0IQ8Z9IF96-GFhL6Ol75A5RoZ5cLFsYAW1g0c-8QpdrpxNMAGTAG9YlENvbvnvnCMYWTPrzNkyXayeUSjy53MrsnV77xE7xtAbA1nkMOwd_rzxpkgbXlSQZgKcPxNd5CK55u9auexdeAiD3oSyKzIRCl6YuOj3ESOnS-KUztBDj5QNT-TdUN5FkxpLWQykHhHz5lrlZUzlzmKnKg4ieqsf9GAAN-OhQFSLkn6AeWkw2YVnbTN9EHSsMecV6hxLbuwlvibLfhLs0NW53q5puAY0_aCX98LT6xKIwCkaRfyv-RQ4zGmVlfKwxoxEcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uaH88M9pYKnAFkeXJzcKecbi2qEi6NQkltzvvNPQlH0CMVQjWyX4d4lXBcdd3KKfaG7IIoLHktwOxaSUSzgOtBFo8p9F_K8s0EINVJPvvUwQraMGu6ftKy90QCaO_6J12zGBlbg4ncLosGgBcO9mqd0OEDHmZcQ4_qB3V9fbwIW09TERZiKAYfS7iVhWs5HPXKi0pgu2SwcyiIxkuZOCVWUiXBctkSzsF890lv6jZvScYTiAVnMvIoQtpsEIoXUENYiOiFjBn9hCaIYyoFO1tfs4yMiQulSOY2nIMU3njPhgNJG_4qp5NFRaZM8JcUfceOkMW0rcqZ-jZUekWbb7UA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#رسمی
؛
با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/100582" target="_blank">📅 05:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100581">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sh-dhOpoVT-ToKF0m0aX89-C53PZrtAw6u95KeuirVVTIWl7a6QvoRa31y3vuQUMBsnyWYylFdlylVgvwbklRSkXWqWLRCXLY1s9tvbsuurb5iMy10MQN41VJWN6g-51dBrXKWO-z9znaujjF0oAZGhL9rJaUUkB4iaAQTB9LQa53mSokYwMIjd8MigwuMKPRGqfmlxKjWok1CF88U5sAMHMm6n8-vTnGMED_ZGbrRJWZAzkt9FkzVPAob5HtOb28_n3sLxxNv0EuCrMV4SONxHhEgEY9_7OPJv5-b6kzxjhuxIvX9sja1ZpgiC0MxOQ4Rho7gfLli0JbluZXdpCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا: اگر داوری در فینال عادلانه باشد، اسپانیا 100٪ پیروز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/100581" target="_blank">📅 05:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100580">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIvc7dzW3Vt7KQNJim6TbSGxVqh8DwlLM8iZvTyZwTFxhjjMciR_NTRxnPOiLkuUqT0K3Ck5zc4yIpXulL04WeR_2jlvYD-KO3_zhFjsreL0mSulqpKLndjSH8ReyNCsOaeIN24TwSdiHrmIfP_vWaa74NL-AOO5ot8wE_7S2GPl96wf9b1mL0HaE1pL3JL740Ous_9vAaO81ishavzGzGKaF2R-Tb5aLrrSGd6HTIqTUNWlcXV6Sfb4wVqd1ayeW2FBbhfijnWO35GR9LlE8xgnNqM2vIqcwyMLSRpewg7lXQk5pGnxbXtsf9GL9n21hGMJnTnemU7AHnN3y4M2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پپ گواردیولا:
یکی از بزرگترین پشیمونیام توی دوران مربیگریم اینه که نتونستم توی دوران اوج نیمار توی بارسلونا سرمربیش باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/100580" target="_blank">📅 02:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100579">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPd1NjzN9HxCtyuqqjOZKJAYXWG-RaapdQeaGMb-pJYam-yTqHpxo5wceWSXFwESTCAywy5JbplLUZwYEreYIerHqE66nAXKKHuBECkkoOyihwmYDhOOJ5x3D_93fOv7Etf_h0BIQ5YWNUGhAPLsyz4b0PcPZhDE_S0Rpdmy2r4qpyRD4VK2oy2Jquxs-4I5yOfeW5m2lNFvrR42Sp-yjDZj-TI9A5OfjWss0b6fMttukUomo2FprJqHlzSBx0CF5VkR2RK75pVUodiUCGZCe0ot-tqv787FSQVCFVP7seMdWUlBEQeVg20s57BdwPF-xdCsvDbhIQnrhroeyYZ4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🔻
مارکا:
مصر درخواست میزبانی سوپرجام اسپانیا در سال 2027 را ارائه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/100579" target="_blank">📅 02:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100578">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🎙
🇪🇸
خوان لاپورتا:
- ما یک پیشنهاد ارائه دادیم و اکنون تصمیم با باشگاه اتلتیکو است.
- بازیکن(آلوارز) اعلام کرده که می‌خواهد جدا شود، اما پیشنهاد ما تا ابد باز نیست.
- در صورت تغییر موضع باشگاه اتلتیکو، ما یک مهلت نهایی تعیین خواهیم کرد.
- ما یک پیشنهاد بسیار خوب ارائه دادیم.
- این بازیکنی است که فلیک و دکو می‌خواهند.
- اما اگر این انتقال انجام نشود، باید روی گزینه‌های جایگزین دیگری کار کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/100578" target="_blank">📅 02:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100577">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-j3Gp5vJpY3sMUKXs6wjXcWUQmntQth3qPP1SHNwJxpo5RjRl4MSF1TI_uNKO0EMMcuqgOwzRle7hLicUbzqUs6Bo9f1TmGkJwQwdP1GClHjJv4c1ZCW_88To5aLTwM2SP3jJ43FLfeL3ydQlipdnerd6cWhT5oKy0PP8PlVeKSHoWA9srjzysLrlA9kKurhd4gka2JtFuG-6LMdiIHPJoS5RnTbQlyw19u7MstCDN9ElNn9REeE6YhoYoRL2Q0eZLj_I8Ej_7BOsuh3kdIX8h3oZWHeWWxrbGDkRm6aTP0wxt-x_4hVZrBAXZeOS7bzt5AW8GzTBAELUlXM6X1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه کیه بابا.
همون همیشگیو بیارید بایرنیا یکم حالشون خوب بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/100577" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100574">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
‼️
لکیپ: مدیران بایرن‌مونیخ از طریق اوپامکانو درخواست تمدید قرارداد به اولیسه ارائه کردن اما این بازیکن رد کرده و گفته فقط میخوام به رئال‌مادرید برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/100574" target="_blank">📅 01:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100573">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCC2J-3dT0tDeO7V37zyJo1AEqSRui4clv9mKQPDEnWu4QrObGGlNCDFLuzG6FhoErgEFX19YFnavxg3vl70x8BMYgLBIDCG_IeObha-9M3EHRsWVfAgyksS74J0eifGzZj3HdTCgx6Ob_0BLBcsCPe6oaI-4qSBXJ9swPwZobBw18Wq2c9SJeeKNkuOAzZzNwO50A7vP42PlWSrLc4syYBPfOVkSAGNERVedzVMM2DSbwj5jAby9X4Ma-Gz9A3M-lxA3AzQAqjhtIob0Vj9IR3eVbDIbtQNmnIDqreLdrG5EQ7pBOGqrpsAsz2emwTR4WujUYOpskKeWhWUHWJsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/100573" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100572">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQAA721pxUPzdoDX3_0DzJqalhLxhIzflJmj2qIjPWIREkzJAmFu-qkMIx5t0xkVQY7tq1SyPa6ORw8KNdCAHVt7-h7vvcC30r6nLZ6C-vz3ZG0OtM_EtfrYJaXJj3laQjXjc2zlxiI2Ys32PwwPE81RzcnxTsgj6W-SqMGIrFFFGvo1Sv4wP5n-yKCueTeeCecVzQ5EXWxoWCDyR3LvkL9de0UhWq1UXJf-704H1UIwgCLLJ6nlihbfFDbLj9cN_WyJD0dX75I1JM8C_WBCbNhRuDqc6WLW2HZfe55hx9foMwKdRsJoBzM8Xvh3R4hLWcMn5ItfRK35Jy4PMGIH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/100572" target="_blank">📅 00:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100571">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG3SH2TAEjDQlOqs1qZnxb_s1_gozUesXTO24xLHhFnaxobaragFOYYFz5HXxzNCSodT6Ujdqv0vxTl8A2xVdyTCEHnGjS_3RKqP5xw5leoaK8Fqt18C9D7sp0G_0eAH2-93urR3JMwpmZaXcqvqdaJznc1psv4CMfflCAb15dRCvjFgplCMKTVWNPpCZdpObBc6bJUu-ZSKaDH1pUh_gAXleQWEXJew_IW-jNNSUoHmTNO8FjfkJKNkDcXg4t2sLDwIav5YrB26KdU7_NgNVU1m47sgl0uM5SiVFp6SIVOwyn8MC_SxWY0TXuCo9RRuu81CjIbrE_z9LTVJ9ViulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رسانه‌های آمریکایی: مطابق صحبت‌های رئیس جمهور ترامپ، حملات به زیرساخت‌ها شروع شده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/100571" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100570">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on8mE2d9NkigIOZKYgpv1S4QG6e1rtF1F-Z0q933x36V0-PTxCi19Ar1qedV-bJudJtr9wxVHHrueG88YXwGRiqjPTPlbRJBtmnkLhdMvbM5DgIiMjM9nHIcW0gm31Ym981l6eaR2yusGxsKPh5u2m1iVtw4RZJ6lhF8g3vYENoxXawNA-YkXwvTyhR8Y-YP58l6rr31ySRle41Zxb3oviPDdJ47uhofRhEECsRUUcW0huGVOoOSOHC4QG6kksV8az6v7YMonfDuW_XhfIbDrWYFB6ZA53cFVajlukacqw0lhuEZi_bRBFBtOWQ2kqslb-yezUOn3zQhiqZ1UinbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/100570" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100569">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEGoyeHtntjW2WGPsWiXXnEHBzO6bR9k2rrh66ZpVVjLMVoXnQT4izDuEw6-2A56oNBdyQKoMIRhdde5hMIBpd9kMH5UrGwXRBmeELINzlSw2fIxQ10y63OY9NGFtzTmzuXkhzWyrAKznzD-MiKZAi68H-mhNQ1KfJiYLThlqmgKj79nvV2BWRWWs6OVREryi81uA1HOirpn8yAgMf1DfvxjdeKWm0wlc67Hq6VSGc2YHunl9uNnjky4H1kRPoTgdA3LWZF0GiMXtBQ2DP7uwleDom7WZ3h6JaIO7eZDa24rCl1m5oU4HYvzQw-Mt6FdOrNo2uXzi4yqFZgcU_Ye9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/100569" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100568">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
⭕️
ایستگاه راه‌آهن بندرعباس بمباران شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/100568" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100567">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4n9u6jXNZxemBpyEVBHcvD6S8o3OLL9s6mkcotBPxZi0r_BD6LviVamRsnyukjgVKcM2faO9zzbR2SqHXxDQ5rVU31EmDSAvxcZYcYMy9qQ-bWb5PX5hrAXsvpbR9Mz7u-vu6tQ0rajJ8RSje6fRpmLI7gonirhzRL5WxAGac0x81R6Q583dBSijTTblj5t6_9ekanFRJGLWrh3O8pI-N74Md2Pgz-PNjdZlh-fhhFzL6WjXHWAIjQQdnyJqFo3Jh9oexqWRfqrXXKORVTPDO-wKME14QpZ26TgHDkOSsROBd230nE5CSc8CMbj_C1TMvsabROocFmmICt8bwD61w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، تو فینال جام جهانی 2026 حضور داره و شخصاً جام رو به کاپیتان تیم برنده اهدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/100567" target="_blank">📅 00:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100566">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb2gRxoAbEMSSOPA4PoOa5pSnF3jAZ8_hWwyXC5E3qghDDEXv2u1AXO2u43EtkbxtlR8THo0Ql0JvRHo0Yox21CoSnmQQ-c1YIIi27Gn0_zNFdrIyUEwiGnXQXtCovnhgYQsAghHVR7khh8DbiS_VfSvuztNCXW59gqvpCC9GC8E5xnkDZyuHzR5gvIh4uBi7thO5z__qHoyZ-LubOnGWrZVSX2LVNQ9QJMmyv_ud1VHB9vKGGwZb27SNX3hIbPzPGpX_YJQIXdD-i44omoX3KaPlciBIO3dCwj4mt5ozTAUHpE9LA1Dbv7Ura6r6M_rJYAoWA4XsiqPtsal9w9e5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح قصد دارد در این تابستان با باشگاه بشیکتاش‌ ترکیه  قرارداد امضا کند. صلاح درخواست دستمزد ۱۵ میلیون یورویی داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/100566" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100565">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
گزارشات حمله شدید به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/100565" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100564">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=ZtwD3GW_cFwgSYlzhLPw4_zqn1i_07HXaZW0rtgvaUH03uMiLyfCS14Lk66LJ5JkDuUmLdrPj1PGhgsqejC3LSjpViAnTotwmwLkM7K_9tMbNGshxzERwGX5fsWRllDVwXmrTXM4WIPmE0JYIV3_AKaEtgQjsc9L4Av1aB8USFpKDp2prG-kkIkVM3PpssXz0SXxTGWSY8OzFky65-wwAVJKqVk7XLAhEYwcd3E_jTMA1Joseu6_diyHTPfPdeI3Z-sKRlUOMw2y8H-Ap08r0wu98UcwLHsXeX0OjOpPo5S0NbyiAJ2V8orZlJz4TE-pTvGSat77i4GM8Mcilbt0kg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=ZtwD3GW_cFwgSYlzhLPw4_zqn1i_07HXaZW0rtgvaUH03uMiLyfCS14Lk66LJ5JkDuUmLdrPj1PGhgsqejC3LSjpViAnTotwmwLkM7K_9tMbNGshxzERwGX5fsWRllDVwXmrTXM4WIPmE0JYIV3_AKaEtgQjsc9L4Av1aB8USFpKDp2prG-kkIkVM3PpssXz0SXxTGWSY8OzFky65-wwAVJKqVk7XLAhEYwcd3E_jTMA1Joseu6_diyHTPfPdeI3Z-sKRlUOMw2y8H-Ap08r0wu98UcwLHsXeX0OjOpPo5S0NbyiAJ2V8orZlJz4TE-pTvGSat77i4GM8Mcilbt0kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صدای پرواز جنگنده‌ها در ایرانشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/100564" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100563">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/100563" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100561">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=l48ZB10csoZYaB_pmb7VX-94lhmomJLMeXUubDPRfJNhdIiFoRnCX3sIef9jioVUnquJ--Ijuyg2ch5VGzfJY6nStq1Jup2pwulRjLM8DrVYhDyY-IWdphOKR5EZ9ViATO87mi-FS7bVAbLvh4CKzeGH_WqRAVNSzbaq2sO7AB3z3f2CEuWykfojuww_AL8soeEhN7anrjZv_fB4AJZc7ZyCp-d8UN6FvVAjdoQMgmUzaMQ6q0hHIxRfCgbTuTkoOTMHowncuzKvRAQUQu-kWfOraTFGfmpI9OUo3UXsVDptDitl9BVxYv2GI_-ccwrs0KnrNlQKZ9SOTivKgEzW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=l48ZB10csoZYaB_pmb7VX-94lhmomJLMeXUubDPRfJNhdIiFoRnCX3sIef9jioVUnquJ--Ijuyg2ch5VGzfJY6nStq1Jup2pwulRjLM8DrVYhDyY-IWdphOKR5EZ9ViATO87mi-FS7bVAbLvh4CKzeGH_WqRAVNSzbaq2sO7AB3z3f2CEuWykfojuww_AL8soeEhN7anrjZv_fB4AJZc7ZyCp-d8UN6FvVAjdoQMgmUzaMQ6q0hHIxRfCgbTuTkoOTMHowncuzKvRAQUQu-kWfOraTFGfmpI9OUo3UXsVDptDitl9BVxYv2GI_-ccwrs0KnrNlQKZ9SOTivKgEzW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/100561" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100560">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=EOZHmSd_fL2e-kblwH_NkiBSlQdZUXWy0MTLgo65l_xk3OszFKmUXiA-mjJjyQnjXQ4E4sZkvPQ_34B5q1xzDedrBnq2tLgn9QPAtUktvTpdeTUZ6_2_AhE-grF0GPecqHdIcKbUIt59L2QyLETzzawYg0fVKIAbJw-6F_aXXqcZ-wqWKm9l3SmjSvE0cbbBmMjlrOUTfvFloBf5NKTEgp1t-GDCBI_10M1Sfj0XvrD-C7EkDC8q37ACoXEUnsIK-MOZKxte_EvarTWCIA2mNzS1kOuxR8ZLb9ZS4vibShF_B7uqtZju4_A0qdxgrxhlJw6VjRsHna-qcAA0Bi9moQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=EOZHmSd_fL2e-kblwH_NkiBSlQdZUXWy0MTLgo65l_xk3OszFKmUXiA-mjJjyQnjXQ4E4sZkvPQ_34B5q1xzDedrBnq2tLgn9QPAtUktvTpdeTUZ6_2_AhE-grF0GPecqHdIcKbUIt59L2QyLETzzawYg0fVKIAbJw-6F_aXXqcZ-wqWKm9l3SmjSvE0cbbBmMjlrOUTfvFloBf5NKTEgp1t-GDCBI_10M1Sfj0XvrD-C7EkDC8q37ACoXEUnsIK-MOZKxte_EvarTWCIA2mNzS1kOuxR8ZLb9ZS4vibShF_B7uqtZju4_A0qdxgrxhlJw6VjRsHna-qcAA0Bi9moQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پل استراتژیک که شیراز را به بندرعباس متصل میکرد و مسیر اصلی حمل و نقل مرکز کشور به بندرعباس بود، مورد حمله آمریکا قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/100560" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100559">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/100559" target="_blank">📅 23:52 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
