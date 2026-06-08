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
<img src="https://cdn5.telesco.pe/file/VgNbf-e1ZHXDCRREoYooY-RC33BOoPlCj2W1jKXwT58HOf_-KZQNoJYpHJ9IMm5zr2kIbNdWaxzh_icZ3oe3DSyZJQKuT1HYmRwWlJJUYZ03VAEyesLwB-P2ep3t-KRO3LuyYSBvwa-qXVQfzRycYn5tm1xEhuLgviO-JabNdBbNAudgvMBU6c8rzK6o0FtRPvd-v0zUziZT_YTINCDe1G1xyAEChC08UbQFaBZdaPv6PkGMfZdre3Hyx9csnyZmr9pdzXvf1GguUzfBVcmZc_oTG0Udc-Tjgs9mv2BUqX6EwG8vecQR5fY3W6MKK4K-hDClRrzedsv9n7mE67iCwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 275K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
<hr>

<div class="tg-post" id="msg-91567">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0LVv3mYnZM0pTV8eLFkpZJDdFu5MKVXpA4gNRs4TogdqAfoR7OaeBujKiuO0ud4CLprZwBEXGLCHqjA-bO8IHbp81JExn3acEIgrO_-cjyDSpv3Tk5HpbC3wxuqy2eATdVlYEDrLRrnADXKR2zTpL8C7X54iDnHR35UEKwytbk4NQ2-9HwegbUfSB-c5QZKPdhLUylIUSH-ZcTQ0uBKfClH3VvHy7Mkl9flen1CBKLo_clUDHcf7sQV0IyXmSsdtvc_Qf7HKvxtQnU-53wgZVBiqzbUKKNzrZXc2fM2SeYW9uepjQZ-MeHAsW6hnG3NUBImbBNQE8oIGfWIIReO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه قاب تر و تمیزی حاجی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/Futball180TV/91567" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/585ec3a1b4.mp4?token=Aha_zYRDQzqfsGCoqZRHNNDyCcffW4nintzNHIu5VQBpUEXuArOaZ-m9UWvzGrCPFMoBteKN8FoY6zrKA-4NCRi2_fD912HqBqmepFIHbDbnAo1GwlYYqxiFEVHxXkudCzgaQjHcB5MC7DkfXqrdBHdo-gfvgSKTL0reTiBL1OZprkVhQKwRXH4IUBFPiExV_fakb8JYldKQsIOyEA-IEYkraSUWiGWKwHCr_XrqO6S7Yi1gq8paUdtYduePbis3r7MAtVRp87R6L5hIA_ctblZKOXSSVHLdbDNxADnzAJdGo_1F8dwlikxDHFVczQwRxdeo5FZz4YNeJWUh8ayXvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/585ec3a1b4.mp4?token=Aha_zYRDQzqfsGCoqZRHNNDyCcffW4nintzNHIu5VQBpUEXuArOaZ-m9UWvzGrCPFMoBteKN8FoY6zrKA-4NCRi2_fD912HqBqmepFIHbDbnAo1GwlYYqxiFEVHxXkudCzgaQjHcB5MC7DkfXqrdBHdo-gfvgSKTL0reTiBL1OZprkVhQKwRXH4IUBFPiExV_fakb8JYldKQsIOyEA-IEYkraSUWiGWKwHCr_XrqO6S7Yi1gq8paUdtYduePbis3r7MAtVRp87R6L5hIA_ctblZKOXSSVHLdbDNxADnzAJdGo_1F8dwlikxDHFVczQwRxdeo5FZz4YNeJWUh8ayXvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
نیمار جونیور ورژن برزیل در کوپا آمریکا 2021
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/91566" target="_blank">📅 18:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a249a370c.mp4?token=TwZb7Zpnn547rFMq0tKCjB300WCfAitQ4uh5D23eAu25GOwfWUyQRYRXK_QmVVe2QVOJ9wndcGdXxfj2z9JBVW-d448CVROugfvgBu0Au8Vc8Pcg0MmQUTc68rlf2V_yjAhiORcjX_7Z4RCo7dv7v9_xk2aY_hmoX0TugQkwH7quFNZvnCYLT8DHdjUfA8CtSCjStKRRzWBPHKb2kFIBbAHEKVeb-iWOy7FlXB-uGOo4btdijNrxqfd5_TMyMphlEomOao9lyC9FeZZALOoh8h7-QHn-nrpNk3QLeyyr4zSQ2rT6jjWUUvgX26n3qNt8KYxlPwlKgrO3Mye87-2yCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a249a370c.mp4?token=TwZb7Zpnn547rFMq0tKCjB300WCfAitQ4uh5D23eAu25GOwfWUyQRYRXK_QmVVe2QVOJ9wndcGdXxfj2z9JBVW-d448CVROugfvgBu0Au8Vc8Pcg0MmQUTc68rlf2V_yjAhiORcjX_7Z4RCo7dv7v9_xk2aY_hmoX0TugQkwH7quFNZvnCYLT8DHdjUfA8CtSCjStKRRzWBPHKb2kFIBbAHEKVeb-iWOy7FlXB-uGOo4btdijNrxqfd5_TMyMphlEomOao9lyC9FeZZALOoh8h7-QHn-nrpNk3QLeyyr4zSQ2rT6jjWUUvgX26n3qNt8KYxlPwlKgrO3Mye87-2yCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۶ سال از این ویدیو سمی بازیکنان تیم فوتبال منچستریونایتد گذشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/91565" target="_blank">📅 17:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq8p3xDUbgaj_TMLSckfm9NMci0DsJtMNI2V0rYYPeRxquWh25koQLbitltmkRe3r1bahQFFnB1CGDKwZ5uZD-YlMt7gqRDe-yljRWCe4kZxXB1KOWRDZqMEqgR9x0x37YFeJxlJtDnorEtYXAPC_yYpyq9D7QkHVayTuvC5E5BWKaHeifClJGqNJohOOX9NG4sEC5LDOsMO8u4chfgAhv6GBG54LGAkAYTkaaD0EfjYK2NFof3coxcDC-q0P25lip1009o5JuPlfs0jWFLjj2pc21vkb9pK98hhD3PNpwBdctE-JF0qeV5hD0zk7s5jDqVZCz9SCruODJ9D8NOtCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
متئو مورتو:
روبرتو مانچینی در آستانه کامبک به نیمکت تیم ملی ایتالیا قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/Futball180TV/91564" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d3e3015.mp4?token=WDATRp-kJCHgcUiD_ZlCH36fq3UNbz6GXrQwrSJ0ufYCZqnd41QQJ2qnp4dvxHnQP5_MOahVxja0-9gPtQfxU8dJ7K93J6tbho-xv_1RQq6kTUSeAaQAZR_M4XmLpS70Vdxvnezmu5qZ8yLfDxEnsKI2h5P9mQmA10kUoPUhVSmScXrS34lP6WIKgOBjPwBbPdWrYZbsYmijL2Do9bpksECP2vMriuEdObuu473jI8vk-_2fTU8qIKNk3kUUeRBK8WwAYnbrAh54MFJuLdXFh2tNsFfCPmid8TN708sRPp573c99d3yAN0xen1s5IxyfB7UaI6pIMzw8MQdvvtTtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d3e3015.mp4?token=WDATRp-kJCHgcUiD_ZlCH36fq3UNbz6GXrQwrSJ0ufYCZqnd41QQJ2qnp4dvxHnQP5_MOahVxja0-9gPtQfxU8dJ7K93J6tbho-xv_1RQq6kTUSeAaQAZR_M4XmLpS70Vdxvnezmu5qZ8yLfDxEnsKI2h5P9mQmA10kUoPUhVSmScXrS34lP6WIKgOBjPwBbPdWrYZbsYmijL2Do9bpksECP2vMriuEdObuu473jI8vk-_2fTU8qIKNk3kUUeRBK8WwAYnbrAh54MFJuLdXFh2tNsFfCPmid8TN708sRPp573c99d3yAN0xen1s5IxyfB7UaI6pIMzw8MQdvvtTtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اتحاد و همدلی بازیکنان اوکراین و دانمارک در صحنه بازی دیشب و سکته اریکسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/91563" target="_blank">📅 17:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKb23j63PJx5Ci6MlRQC1YjWAd4D2E2bWKu7R8fB_3i_2wdL8eOdCqBXLZpMZAmXPxGhCbpMohOa26cslrw9mg-ytbcovntmCeEj3yuSzFNCZoPkPo5NGT_vUsY-NCRbGUgfTcERYOtbtFH-FsjjguhDcPo3vniocmLaHEhi6A-AhZMqZyS-WURnpADuAufzutDWBq2xab2EEGYa3FiWs2x1sRf97CYzQrHtJAHpG8VCvLiHAojN13Ah0G7HvGS55kwbYVxW_UImvbmzCNiCgOGK4SABok_HK_HTp_3ZOFYiRE6CTmeTOFi36pcxgG4jeLVHbFyrwty3XCrPSw8rzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ۱۰۰ میلیونی، از اینجا ارزون‌تر درمیاد!
😎
💸
وام بانکی از اسنپ‌پی
با ۲۰% تخفیف
خرید اشتراک
📱
💙
✅
تا ۲۴ماه
مهلت پرداخت اقساط
✅
بدون ضامن!
ارزون‌تر از همه‌جا، آنلاین وام بگیر
👇
https://l.snpy.ir/aqijh
https://l.snpy.ir/aqijh
https://l.snpy.ir/aqijh</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/91562" target="_blank">📅 17:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7cfe2ee7b.mp4?token=Awstvrz43FosqCqgjWkxbHKs4cv-r4UgRtilmqI1cgRnEA8QeU8hJZgKd69RrPcKDaB7-_ZQzLMWLkIqYz1JVAVJzLbiW0LJhXH8GxCkrJ-UNeXkrRtm40fcC-IB6-FQ5yS_oR9wkMzUif_tZjaHuXFqixlI3wpZ92kFPG00Vns-hZ03A2sXzdFoUzUb8_MfmrWXjeSBy_uCd2GiBmYKfp_W-3KTn6OUuuouKBnhjqTSqQ85Av5MsarjPm_UHkkay_6ztOSdp6XxopSXdxiNpdiKjpIYWlsgtH5biMcrryfERknqmWsVd5euxcXvrvwX6gmm17Kscrg8vTt9fHl4IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7cfe2ee7b.mp4?token=Awstvrz43FosqCqgjWkxbHKs4cv-r4UgRtilmqI1cgRnEA8QeU8hJZgKd69RrPcKDaB7-_ZQzLMWLkIqYz1JVAVJzLbiW0LJhXH8GxCkrJ-UNeXkrRtm40fcC-IB6-FQ5yS_oR9wkMzUif_tZjaHuXFqixlI3wpZ92kFPG00Vns-hZ03A2sXzdFoUzUb8_MfmrWXjeSBy_uCd2GiBmYKfp_W-3KTn6OUuuouKBnhjqTSqQ85Av5MsarjPm_UHkkay_6ztOSdp6XxopSXdxiNpdiKjpIYWlsgtH5biMcrryfERknqmWsVd5euxcXvrvwX6gmm17Kscrg8vTt9fHl4IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ناصر الخلیفی در شبکه الکاس قطر : لوئیس انریکه به مدت ۸ ماه پیاپی از مرکز تمرینات باشگاه خارج نشد او هر روز از ساعت ۸ صبح تا ۹ شب کار می‌کرد؛ تا جایی که نگران شده بودیم مبادا از شدت فشار کار دچار مشکل روحی شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/91561" target="_blank">📅 17:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91559">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkrYJoGhQgJIfdIBTvSMJ_ScVjl6WNXfH54FoAIUi-uQftd9Wjp9YAgX-_8cQJboxTNNcEiGjT5RJQs9I4coSKJgFUDgZMrIOxxv1o5qK3-JT8ZbpLpsnlCXVM4MH0uI90qqhqqwf1ocEZLsUB4KVkXnDsgt9GhNHMLr34e7rGwy2J0zjx7sS7TxR8JDx-0d_4aylV3YbtQm8aXKlBe1kWqnqg1nLIWKPNW2DWtaD1WmbJUOQDdyGSpa8gejEv4yyYrdFKLCz84jXM4XaZzcXrDXBlsZXu1o-59nYT5si5-tJTkGNZxFozz8cPrHQtsasPYJHsPPNsD5Q0dMVcX_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUI4ZBOBCZOXpTSJ8-8dDr6apt2aYkqNO-JIadxfYaYbuF0kGZJ6-NNRkzrsxTveHp_l9XCoATPEyJ4TvvgeLzKiSVrZg5j3cCNqmL2EKzB7I5_m7e7Z7LSsCwC4Y3eO1ddcvsjY8OEewqbvHXwD2R-bDRc_v2aRrmLWCU8x2cpB7QK5tvnzfPmvpdaW8COOJ1z1eoUHI6IWe6YarjQyepobwrtZDH8F-0YFnLoWJKbviy53YXhYVMtp4HBKl5dS6a4hGb50pqlZFaR9Gu141df7D0rPg5z9JwRwTDMpyilaBo6Qqtq8grsxG7niG2EzTYq1_fR1aS4_RmFSvh2TfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خاله وندا بهتون سلام میرسونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/91559" target="_blank">📅 17:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91558">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw__kxP61KTNedmFCbsIkbWwzc1-UbgmM7l7ZY5mbRkmnvJuCmAF9fAS6tlJAFskLod3Au4Ma1LmAugoMB56DVbdGO0sAgJ7Lp_JYMt4wf6FoOzuoPdgNWn3kkWYkzB2LqVRB7T0v_V2ZmKwWSaj5OsYVkYbu1z8AqpidiByB6i2HXev-TWjFJw5-4_L_tBJu2UYNJZ8PABWL7UiTWWatIdAq8f57xF65E6Q_SX6XH_nGis9bMIRGAcNo_kzqsle8qvvvpSLkOy9F7kHG6BZYHj43gggLTCVj7O_yr66ymMf7r2B5iGqvMBRhmoWePoE4-rHwyApcHDEUDyxmgowBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
سانتی اونا:
⚠️
اولیسه در بایرن مونیخ موندگاره و به هیچ وجه راهی برای خروج از بایرن نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91558" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91557">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2681453adb.mp4?token=k3PnP8l9tVuZHGFAJZkb5AuaWGbxuWByW37mBlwdJaJyQkFcASD9hjOD6AoYchUQb10k9vr_pvGAsY386LsiIYNMhjonMvLaFIsAwAWQVbLFkTbp70kbdWVBSJlIzIP2wsvru6pnOmETVHml29B89zh4h57k3G2h07yTnVlWs-kDaN-qiCs80wJxJ2oksqPgIpyuDgMfO-ki0VkOBYkNuMLr92X22YMHK6mJ3fuLYhaWKd-RbSQjowgZU59CoHoFTJvZCyhSqPu7d1KaRjASxCdfD2PZvrr5X2Y0KK2xjVwkN5zID2RVyBgk-fI2UMXx0C9Gfr7QjmIDIqlRUYmY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2681453adb.mp4?token=k3PnP8l9tVuZHGFAJZkb5AuaWGbxuWByW37mBlwdJaJyQkFcASD9hjOD6AoYchUQb10k9vr_pvGAsY386LsiIYNMhjonMvLaFIsAwAWQVbLFkTbp70kbdWVBSJlIzIP2wsvru6pnOmETVHml29B89zh4h57k3G2h07yTnVlWs-kDaN-qiCs80wJxJ2oksqPgIpyuDgMfO-ki0VkOBYkNuMLr92X22YMHK6mJ3fuLYhaWKd-RbSQjowgZU59CoHoFTJvZCyhSqPu7d1KaRjASxCdfD2PZvrr5X2Y0KK2xjVwkN5zID2RVyBgk-fI2UMXx0C9Gfr7QjmIDIqlRUYmY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧑‍🎨
اثر هنری جدید حمید سحری: تاریخ دوباره برای اسپانیا تکرار میشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/91557" target="_blank">📅 16:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91556">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOadxMn50vXILKq6GsyqErupQFnyA0BwQEvoAE9ZjJDE1OZ2YhD4Nfhc68z0grLEYoV2TQqznDZ_aZrbc_InZbUWKcSccDUHjANpbSIXLhXpy7ajjHueW6GdyPQ0siTyqcJiYYajo42FTW67bQLrGj3EAaV1cCzlRSHGec0azLikJZ2poEmOLQ7pJHNjrhSd-0stijxLJ5d6i5qy9gkh60lHqLQ6V3O0ureuCAPizGhxc-kv-9_kW5Kskn7J9ZWW50mFaqI31TF3WU9yVP2Eb3CdhTJM18_Zepj7jJiefdZ5fzZhyF69-HGfiYCfNjLw_ivxv3XZLfrVn7t4Jcl-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زین‌الدین زیدان:
🔸
قبلاً بازیکنان آزاد شماره ده بازیکنان باهوشی بودند که بازی را به شکل دیگری درک می‌کردند. حالا همه چیز فیزیکی‌تر، منظم‌تر و کنترل‌شده‌تر شده است اما فوتبال بدون شماره ده شعر و شاعری‌اش را از دست می‌دهد. فوتبال بیش از حد فیزیکی و تاکتیکی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/91556" target="_blank">📅 16:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91555">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
اسرائیل دقایقی پیش جنوب لبنان رو زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91555" target="_blank">📅 15:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91554">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚪️
اونورم سانتی آیونا گفته که رئال مادرید به شدت روی مک آلیستر هافبک لیورپول کراش زده.  امروز عجب روز نقل و انتقالاتی جذابی شده
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91554" target="_blank">📅 15:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91553">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCuwOp46P8gXiUcD7LKXRrCBLws99XyTLaG6Vv_vL_ACYmR9ukTzIlQuOyvnlaCooQ1auI3Ig92Bg5wkPcB4-WvXdSHvfTeTEYuWkP_-Ff6vlwEWaTqFWlJukMph6qPoDi3E38qL9ouagmDll92l9olzO3JZyEyGIbC3hl-XPihtnC0pt3SAfDjmstNkcdC6yjrkMCPKrjqi-1wATwWoEyJIAxEZ8OpTyD7qmMt3BUc_luDjwh-vOl6ZQLThLVsyeOiJkKxbOjtgccd_i_ee8GH9CXL8PXMNlUuCj9IPflOR0TK_oUex8Pd7vGAd1tbjS949FGr__jKfTVbRYuWWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
دونالد ترامپ : یک جنگ دیگر را پایان دادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91553" target="_blank">📅 15:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91552">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XASx21bhGCyaT1nmqsc48RILbOlD1qE_XyUCmnKmQXxcMr2Wh7S6GAAPPu7ZYYqpg1-UtOagy33Z_KI2DurffoMMfXz9AxFI1nVP8vdZ1AyO_pgl6kD0P0EEo2BH8AyX81Z8y56QpYBZ-DN9qeKxxDDdZ8OMvegXshBKjzeAGFOpR2JEYZGltLQw2PPsK9tsjJQLcDe7CcsdCz6qSlx43D13bnrsORZS29nqnnV6cMfs5t8f1Eh7-FAsufYxmY4lbL7_tLaM58dsHuNI1_f0oez-bv-N17NQFl_qBR8sWrg1lJ6WqETUP1VMADqPxDPWsZ2Ja0sFtuDeO83tBhvz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اونورم سانتی آیونا گفته که رئال مادرید به شدت روی مک آلیستر هافبک لیورپول کراش زده.
امروز عجب روز نقل و انتقالاتی جذابی شده
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91552" target="_blank">📅 15:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91551">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4qOvb4fmhtFtB98DWcG3rrjm0VSUrG_oY_4DO3_lGTsvcKLnmjY1GhlUeNWtQBEQs7vJxMutr5axI9x80shrrwMhl4-jrBxMuw_q4yEN8PzhJ3amH3R9ciUcPr4O3drsJ0hkGBABW3SnsoLrhAo726qvdIG2mlTFoeQLrktmxEBIpyRRIACG6yk5ZY99R7bjuR8g-QDNAksaO6rTM-fCY3kbI_Q6ECIEO0fBNUT4sFXZ8IJ6vQDDkmKe2S1W35ox7NZyagHssWJGcKEyUBeV75sY66lAQm6u1f8yyQOS2PFFmd02uNiGBWNFgYb6vVOYd8KguZrABb8gHdhVEtq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خوزه لوئیز سانچز:
به شما می‌گویم بازیکنی که ارزشش ۱۵۰ میلیون یورو است و پرز زیر نظر دارد بمب است بمب
‼️
کاملاً باور نکردنیه و وقتی اسمش رو شنیدم بدنم یخ زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/91551" target="_blank">📅 15:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91550">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tShVAizH4_337LoG2kpRcKZmNnHPdBA6YcEcdxAzM1H32eCcWSWxPX5iC37aZifzLbZgNWejFhhTMV7poVQ8ZfEE4SiqH5bwkkR247EBVO-ESc8SwOSyaETIoN1-0xAxGJRxwbuyDILPmNIsw_237r9bYpIoMw-jL9PB7AS2ctjkhJ_a6pcnAq8AsSxLssfLzqgVzta3pGBsSBXHygfz91XlOHe4R-0EJSgwb5JRBUxBAApP0mecgADvTL1RdhYHZGzO-Om4lW6B7k-Tt5uT_xEHt5GF627imZWSRQ1SFxP8Nu5425p-GkwAxXpJ8YKuaqRZDeBmVBBAtyen41OZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
سانتی اونا
:
⚠️
اولیسه در بایرن مونیخ موندگاره و به هیچ وجه راهی برای خروج از بایرن نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91550" target="_blank">📅 15:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91549">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C8RuH9yxCGPGFlGfi7OImbdTsASS3ymaQu3_HUtMmrdfgPDT8Y9FFYYb_KqY9j3rRKHK2M7GH1eWrWZulzrGQtKS5rtX3XQhgQVVgx065yfbiL5vBhuTyFXVy2F1lsXO-qLymUDJmFKoewcLMEy730ocqYY7E8QrW9B25QHyVZ5FQew54AIa_y8sYuheLXBXS6K9anxGB2p5SywKbA_S3eonkvCOIvRtmXBi7xnUX3zh2KILCRUvXXHOR-qTc8w93ASHYRdyv6835NGV79rvGJObkfzBhoCZQ2muwCnG4yfKmucEV5ywdvWpRngtSdp2l7_WruapysMKLrzs0NCzQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
جرارد رومرو:
🔺
پیشنهاد آخر لاپورتا برای جذب آلوارز: 120 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91549" target="_blank">📅 15:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91548">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
‼️
دونالد ترامپ : یک جنگ دیگر را پایان دادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91548" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91546">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7Sp0Mo3Ss27BWtjb_ByLR7MEhTMVZ_nXNiq_ixr00tLkvY8_ddN3H9Sm5o6DtyuZl9z7m4b_C8YTszlCSSdD0ydWyifDWm5ktCKq2nFkP2L7UAHSPIJBQr8iZ58_b2Z4UBytwyaHb5AkDbr6hyt6pIhdTMPa81xcq0_bOEK_pq4VGqq1s2TxvDGKeqXpGz6zbKu2ayeRKd7Rr_WOiQOOR7mUEpRTcIp7cPUXg70P3QaY9oMND7x_n4iJMMfZqOB_sQpk9NJzSQaQJGQNXF8E7uu-BJGz9T3RkAdsp0qpTAF37GUrgnHBdl0huWM1XrcigpYejqDt--jNITz6mSlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrGOtefFxFW9BqE8bvV5LWgcNkiYCaPQTyL_jIINEvO0w8f5Ml6Gu0viiEJkDq5K8C6QFY0R4DJQ0Id6CQLJwZYVgem4fSC9H5l6baqRZrOMawjcSEMXGCR-4H0jar0KdTUENip_TXKVDawgCVk_MoSx8oV6_aT6BflURsGKRNkQB86lk9bai6LeiSeg3A89GoiZwepfHZ0L15vX2iJzl03_1x3_b7gYMslIySJoIEkgvrRubiEo2SzRVobmlVjJccMHmGw0YF0FZPJ6UMa8Qy_Kh7DJEJIXtoO3JiAQdig3Hv69OdkgXadlTAEPn4oWUlqp6rGA0FiOKgN5GpC72w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
#فورییییی از اسکای آلمان:
⚪️
رئال مادرید آلوارز رو بازیکن ارزشمندی میدونه.
🔴
اتلتیکو در صورت دریافت پیشنهاد 150 میلیون یورویی آلوارز رو خواهد فروخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91546" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91545">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqwpVGtYPZwgtk1Fy49cdpIYF6lhaJrZUnljh6SlL0DXIr3adTBCjuJfBqSrNHIem3JlM75Jd-_ka_VkSjehIgVSxGRbQ9c2wfD8KmZtmKNjrvMjhY9gBlpxg_mybFaxUTXMFmiPFczWjjoG_J-6QAFRn2GyTh64JaNJqUhSXv_0_vWudTKqpeE7HRg2IfePT119uAuQliDSNB2ftk-Y7oWncXNGu-Rm8Z0WPPglVp4hJ8JdD2VKOdrM4JxGchfTWY25FrAY6wwDnqc1yzBcOQa8BXlm6ZRGpxgxwzWunomEpSzndEGrP8JVcerQkOiXR3wS8Cdx_xgb_yfBarBnWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فورییییی
از اسکای آلمان:
⚪️
رئال مادرید آلوارز رو بازیکن ارزشمندی میدونه.
🔴
اتلتیکو در صورت دریافت پیشنهاد 150 میلیون یورویی آلوارز رو خواهد فروخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91545" target="_blank">📅 15:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91544">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJIOjYPG5dQOoO4zzNTfqAgtMIQ2-wrzq8XT60Dl9WAw0zukg9TpCrQzC0FnFZ_xPTOSlx61-GgEezThLy2UQIv_1-EZlUrOjqiMTonOCHyzvTWOEWNriiyjAcvUkSg-SnlptJ0UmHyWB-plI6ik0BiXhi8AmHpgLAgLzuN4KO1H6ONhYX_3FMo732Mm4Rc7xogXuRoddEFifv4i5Ku7zcrtHETOAWaPnf1SKspkiELSQgK3xmoDZfBx49lYPfgUr1-w6jWphtDWUsff76l6xtyTffsQaTzNms6V_o-xZjaMojI_hm9wEU0nZoRBOxrtC9AQQV84iHnF9ulrAFgf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
رومانو:
🔹
من درباره شایعاتی که آلوارز را به باشگاه رئال مادرید لینک میکنند پرس‌وجو کردم.
پاسخ رئال مادرید: هیچ نظری نداریم.
نزدیکان خولیان آلوارز: هیچ نظری نداریم.
باید صبور باشیم و ببینیم چه اتفاقی خواهد افتاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/91544" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91543">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rqa4NeQCUht1FAPm54nHJU3UAA0Ty2MZodWfzWNl_F0Uyn53XaYY9_UDK87zs4WLcIvNiRWKFu8m_qlGR95btFgm4zNo2UfJH0AwpGu3Z7mv9MQ50oeXVpymeW6by7chu8q_4VdebunJiBjSVDtwWeJiznBwoOPQweWt1rFxGbjTLxZf0fXGFor88pxQ1OiLz9OpY3edB1HYzZ2ImiAjsDTarePwQyw_Nu4hWg89eGMSUpRCUj6idERSmtpF8knfVG8m4g8ZUh9fntsRNMbPkjt9kEXB0H7C4n4LzXPjhcX5ADt-yl-GzpGue0R1-q9PtmrOiqDowGAloLTF74pL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
رومانو:
🔵
منچستر سیتی آماده ارائه پیشنهاد جدیدی برای الیوت اندرسون است. باشگاه به نهایی شدن این قرارداد اطمینان دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91543" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91541">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjFnzRzehCUy2niFR0je9XZp6Bz1g6YG3JsZYYAZ8113u5rTa7rCiYdzFNwudSbIkLIgxDkfVDyDoVUC361gGiboVxLLNc2zTs6Mw3b_grxtqX1AWlm3nD2wsWHITU5zgCxwwSptX3vVF9uABkOYorvYLcIVmzNuPeXnW7kpA1kwJBB9fJip5HW8Im1x97ACCOo_cgOM2LVJE2nKEiGAewPEpt77X36zD7gdITr0iJ1S0jq-L32vwsAh4Mmmaz4NHKJFpKc-OJ61E5m2MGgt9fNIYyTl0py0a1Z9oOCHE9Zty3_LNaIT50ktyySSZN_17zwnyPa4ha6Bp9DCkm3V-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BbuUUxX7JrPsjKPcT0tFRh7CGER7AzGcgsDMhoASg78SLTrVEehRiroy3gmbJzV5gtAhMvudRBJI4v0EaJJR2hebsxkt9hADIm7BTByBLFuqklveocxo2xJB5tePzzjuEAuXQ6pqAkXimfRXLY-3Seh_ZraolJ0MVyLqBvX-LbG4xLe8ZioaKg_bY0-Q5OULUh0VjW6tw-s5kPxgibPi4mgFcLzSQHljPuKanOnF-gTBcU1K1dKCFLHw38cc7roM21nco0pbI1FN1fKrEERE7dtN40uY_GS1_Q2Pj8EITX5vhXauWX9JgZonsraZBDcqYqWNWzXTWGB-6-ohMpiXtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇷
#فوری
؛ قرارگاه خاتم‌الانبیا: پاسخ دردناک داده شد و پایان عملیات اعلام می‌شود
.
🚨
🇮🇱
#مهم
؛ اسرائیل هیوم: اگر ایران حمله نکند، اسرائیل هم حمله دیگری نخواهد کرد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91541" target="_blank">📅 14:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91539">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
فوری | قرارگاه خاتم الانبیاء:
ما توقف عملیات نظامی را اعلام می‌کنیم و تأکید می‌کنیم که اگر حملات، به ویژه در جنوب لبنان، ادامه یابد، پاسخ ما بسیار قوی‌تر خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91539" target="_blank">📅 14:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91538">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDeTSxf5UrJ3jkifW16vGGXPF3U2K6nUnd8L3SENOHr2K3YSCcoqiIXOXz3e1dM0zDPxV1eAtqgaAYfi00UHdHYBb1gvruhFFCEhf4P8M5tPffxKFzEeJ9K9XdOkA0ZO4SxaSvjOvCo9CNR-d5f3DGuoCWVtkFOlUGMign4ODgCZOA0iIR0bFP08MvGTqH3huhqaPH7SNKrbkfpNkyobcvqp7lULNrP13EK_nipmdc_98990gp3sOHDlgjildnITHVm0c5rHk-XUyfk-UEuWHxW7qfEdeY34cdEuq2DT2oHMg3CXQHfRp51JIci0MveXqXffGc7z-oogEyUWs7Hr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حریف تو من هستم نتانیاهوی قمارباز
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91538" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91537">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOy0hisIknn1lsXhyFl6ARRKbe8857F6hcyTndiPuFxw6ArtR-SCRjYH6S63MehGCaD0YcrVNmYiWDvqNpuLW3a8JPTFXUZKcKEwFklRppIt34hyTBT_5ObXn8liniGbNRXRc9O337VjQfM0B8uMY1T3E-eZpmQ0xe2DMPrGtMGyLwG2RVb5pFvtRPEO-Aic4GaniDysScTImg4sr4SmuwnSS3_R_IJEm1vicFZiF2Gpv_dOXV0w2kxpU-bNj9kOxuqt63Vn9SD4Pmj72B6bjqpnfxkd3hWaZ91Iqj3e7I1zTAeeRh2IryWPj8bGtUFEa0cl2qNaxzCukSgWO2P6sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
‼️
🇪🇸
هفده‌سال پیش در چنین‌روزی کاکا با رقم 68 میلیون یورو به رئال‌مادرید اومد و‌ در 129 بازی با ثبت 29 گل، 39 پاس گل و 2 جام این تیم‌رو‌ ترک کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91537" target="_blank">📅 14:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91536">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662d05e7ae.mp4?token=J0H3mvDkVUljiMKqNdeBU7KzRiQWd6oIlqd58ZmZKKTlmtlyUUSvMuk5_9I6Z5BIGFYRha_dPYXfnpGkEN5Mtw_z3JDqd6zbCAqFOISRUZ1P1fyMQ1JvA0lANoRmE04pRFx7trRrbzhmmYYzABn37ky1vN-Wop5fDEz1ORK0K_Lpi7LdK2UUNe_Ti3PIFuBny9aUFC7C9UJOLHSN6ynTwU6308p-eL2tZBJttUwa8r5pIcACD5ToZhSLHy9wd2jUr1DPuRONLS33lev_Zr6Cs3sJKoURO4Oty0Tfo2u7evJ8iayjAa6uIJBuRUjdsYSqa-jtjkEFAc2Y5tCVSo_PGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662d05e7ae.mp4?token=J0H3mvDkVUljiMKqNdeBU7KzRiQWd6oIlqd58ZmZKKTlmtlyUUSvMuk5_9I6Z5BIGFYRha_dPYXfnpGkEN5Mtw_z3JDqd6zbCAqFOISRUZ1P1fyMQ1JvA0lANoRmE04pRFx7trRrbzhmmYYzABn37ky1vN-Wop5fDEz1ORK0K_Lpi7LdK2UUNe_Ti3PIFuBny9aUFC7C9UJOLHSN6ynTwU6308p-eL2tZBJttUwa8r5pIcACD5ToZhSLHy9wd2jUr1DPuRONLS33lev_Zr6Cs3sJKoURO4Oty0Tfo2u7evJ8iayjAa6uIJBuRUjdsYSqa-jtjkEFAc2Y5tCVSo_PGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد باقری هم سایدشو برای جام جهانی مشخص کرد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91536" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91534">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et-GqJH-TB82ibfxf89DT0B-9d98G4aOEQ9__YgdYkZsvc6dqpQiV12tSj1-Yl4fWeQmkxIQZs1gS-WBDtHRN0yhDD6bTRGpZSyv_BiVKhLgy9dPhBBaKXNqNmh9OWTyBI_DYQhTBG30JUUhvCTNGzmemqXu-z33VCHuFdTycMoSV4amrT2kgFLEXhAW4hcd4VO5G7btkoTT3GOkcBiSz6x4CVjpbYahuewdi_QKyw2x6w7Hl5vfzM_y191lYHWRAdFoCfE9ocfcaw1zIQrTo6gPTZGp4fhl_MZPhoVGCn06H0NWy2Lk05PbBoEhCBITVcn-629RM9mTCle0_WxQgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا یا من پولدار بشم یا دنیا جهانبخت تو روبیکا و بله چنل بزنه.
واکنش خدا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91534" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91532">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6kFUgyn2Xd4WZjOXCYA_o9rrGG5QU_oYNx3xkn3OvV4BTUnpjlHxrmqeQhJJA4b4DdgjIAxj85ZWZ-ufzEvxSNEph1R-GuxRgHjbZwF7bYWzjtBhepZZmuKeZjKqUtjsxQX_YcBojlb_XpZ4A3QPHhsEU6iFaDD0eQKkn-rFUfcXI-KtiTT1GX4Rw7WhNiCvOQsXyhEWxiZge3i-YrNbOY0ptodpvhMTLxw6VYILwAt3DdezFsvuTr6J63mN_MmSf63r3onnJATlxe5pZxKBY5xsf_lzGCd8qFN0crwiZMqW1gevRGQ3wHH33H0HAM-PPJ8YaCP3_tZCVuu9ww4ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⭕️
🚨
تنها 3 روز تا شروع جام جهانی
تلویزیون دولتی ترکیه مسابقات جام جهانی فوتبال را به صورت زنده و با کیفیت 4K و Super HD در ماهواره ترکست پخش خواهد کرد.
TRT 4K
TURKSAT 42°E
11767 V 15000
TRT SPOR HD
TRT 1 HD
TURKSAT 42°E
11054 V 30000
11794 V 30000
تلویزیون دولتی ترکیه با بهره‌گیری از تجهیزات مدرن پخش، استانداردهای فنی بالا و جلوگیری از فشرده‌سازی‌های مکرر به‌واسطه دسترسی به پهنای باند مناسب، تصاویری با کیفیت بسیار بالا ارائه می‌دهد. به همین دلیل، حتی در مواردی که بیت‌ریت برخی شبکه‌ها تقریباً برابر است، کیفیت تصویر TRT بالاتر به نظر می‌رسد. برای نمونه، شبکه TRT 1 HD با وجود بیت‌ریت نسبتاً مشابه با بین اسپورت، در بسیاری از برنامه‌ها تصویری شفاف‌تر، رنگ‌هایی طبیعی‌تر و جزئیات بیشتری را به بیننده ارائه می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91532" target="_blank">📅 13:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91529">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ملی شکن⚡🔥.npvt</div>
  <div class="tg-doc-extra">2.3 KB</div>
</div>
<a href="https://t.me/Futball180TV/91529" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
✅
به اشتراک بذارید دوستاتون وصل‌شن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91529" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91528">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJ7MFGzQ2xmyW8SDD03Cndy9tQRyIPd5d89VHQRWww0WhaEoRPa7yK0cw4oKUZ2XMvxccCIsFpXZwfhTVT0Pust_9pc3VGcxDwo185mVKTEKja03Ma8omxhgaP8qHc1WwafEFIVrdPd-NRQurt2nQymDu1FKUA_QOnM9CxdgN7cfOBC-g8QQaDuyrIhzI-eHhmt3z0-RfgqeA2-3ythgSj_6hISR7w2c2RTbUJXLzeWetuzQHj3cjv0mFAqPqdhOBrA7oQuZHi-bw2hzwZ9tkR9XfAv7CwXI9pRytD8JSVdu3Nc1q8XQlvm63Du0hsj2g9lHxrLi8ec0Y2teMOsxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سر صبحی خواهران منصوریان اینجوری به شکل عجیبی به دفتر رئیس فدراسیون ووشو حمله ور شدن و خیلی وضع بگایی رقم خورده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91528" target="_blank">📅 13:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91527">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
فورییییی ترامپ:   اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91527" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91525">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
فورییییی ترامپ:
اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91525" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91524">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سازمان ملل باز هم ابراز نگرانی کرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/91524" target="_blank">📅 12:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91523">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/91523" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91522">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdRHeHgbhszsKIqAF7QESl683Z-yOu2dyUGAKFPFWopVw6Ceb0ePdLLm49OBEOjXmLqJFpLC9k8_FyltCLiA_OJrq9IRK8VljmiFoQ7rBKDl94fmLWlEP2JnsvfADniw8DiF6FKDMI_XOfGxaegytwdpIpof-cSkQx3lWAfpjLVSrWuQ9VrHcQd9VzWTUOlhsuBGWY1eOnjgUPc79Jzf6pDKMlyOYBkr4ZsX4i3UJEHIHrl_NqESozvz2xUk5gOwwHuWri6WrjF1MQ_jDxlKXE5Ve_YkyGy4-6blvcc0WAFgSJDoZe2sz5vkHFFuKyF-SiBU_xOSwv8Di3PmpAz-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عموی ترامپ الانا زیر پتو کنار یا روی زنش خوابیده. تا بیدار بشه یه حرکتی بزنه یکی دو ساعت دیگه زمان میبره. احتمالا این سری علاوه بر ایران، کیرشو سفت حواله نتانیاهو هم بکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/91522" target="_blank">📅 12:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91521">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/91521" target="_blank">📅 12:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91518">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fePWtjbdNCU6-NRkaZxeXZgGC9byfPiyYT_6XIta1konDEp7cl-Wc7YpfBZJC_zHO_NM6yXor-v8eSlJqTCdkMaFTlBBdLpul52VLETDIQm6XLhb9r0WYHOzLEu06E5hKuOD7jCAqq-8WqJuyXS6EbYpu731EYTFuDvBmGx6ZUUzIVMYJ5Rz7jWLt3ada4DZPEKYpZdcoZSdFcfc8B9AOehDNXO8NymJHAcxytI1g6MUvtMrVKXBM9q31hcmQCWSOnalDIj1URTI2It2Am0AkM6oy1O4veOTaDaalKXHwn1BQIA1pqUlEutr3EN99549tHPPcKbHl8dzkpwqnZtMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
#فووووری
؛ عبدالصمد الزلزولی ستاره مراکش بدلیل مصدومیت از ناحیه رباط جانبی جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/Futball180TV/91518" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91517">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3302fb4017.mp4?token=cq6UcyB53PwegMWf4y7xA4ftSMJwZCgXGDEA4P-zKz2DLPjlyZokQb5JZdP-X592lZG9I0Z0PqF159P-FoT4KcwIOZaV7n_fE10d5iKZm1aKCAHiHRBpxCas7oUYBZRz8wSLZy025OmOQZFXMj3fUnG8E0aSbduJ36Va1AtrLJLH1tfFhmV7-HibSmz34AWX0rCYD7XETG-u8K27LKS67gxj395RaKtMcCyIg2qxKcztX9Pm70pJz_U8dZL9C8CPwpZjqOZgjtOJWIgYs1mECkKyD-ZgbtSsa4ANHAivqKIUFVZdhG4HC_yU9umbhP-hD3ZHS-kxcBkezHHZALzHKktQ-QidN04swz4IHChXjgstWom0jDM4_a5HmcJ5W0SLOVEmeg-_NDYeW7vkSU9KwoYODGif25WrWke2KhJYkIV0VOk_emncd5sVC5NDrX7ixF8BAVmuIr1bCWueePzyrNBzAtnjdASMoEbvxyC7dUpxW6GvA-wVvjX1Z9S9kdZiBNUSyqJEWvCLxFtFQN1kb_6CWgRe4ZXITTyM5S--ai8xyBintegSzOQ0rbFagWUHEUUX_oNRaNpYUPPdrnBWUvYuj65yM6BIezksfhhYAKjSPN49ndS34sDd5HNHL82dAqprlKHPcy3Fv5b8SnjephgISjg_4RbJ5_VUjhVOXT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3302fb4017.mp4?token=cq6UcyB53PwegMWf4y7xA4ftSMJwZCgXGDEA4P-zKz2DLPjlyZokQb5JZdP-X592lZG9I0Z0PqF159P-FoT4KcwIOZaV7n_fE10d5iKZm1aKCAHiHRBpxCas7oUYBZRz8wSLZy025OmOQZFXMj3fUnG8E0aSbduJ36Va1AtrLJLH1tfFhmV7-HibSmz34AWX0rCYD7XETG-u8K27LKS67gxj395RaKtMcCyIg2qxKcztX9Pm70pJz_U8dZL9C8CPwpZjqOZgjtOJWIgYs1mECkKyD-ZgbtSsa4ANHAivqKIUFVZdhG4HC_yU9umbhP-hD3ZHS-kxcBkezHHZALzHKktQ-QidN04swz4IHChXjgstWom0jDM4_a5HmcJ5W0SLOVEmeg-_NDYeW7vkSU9KwoYODGif25WrWke2KhJYkIV0VOk_emncd5sVC5NDrX7ixF8BAVmuIr1bCWueePzyrNBzAtnjdASMoEbvxyC7dUpxW6GvA-wVvjX1Z9S9kdZiBNUSyqJEWvCLxFtFQN1kb_6CWgRe4ZXITTyM5S--ai8xyBintegSzOQ0rbFagWUHEUUX_oNRaNpYUPPdrnBWUvYuj65yM6BIezksfhhYAKjSPN49ndS34sDd5HNHL82dAqprlKHPcy3Fv5b8SnjephgISjg_4RbJ5_VUjhVOXT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
سر صبحی خواهران منصوریان اینجوری به شکل عجیبی به دفتر رئیس فدراسیون ووشو حمله ور شدن و خیلی وضع بگایی رقم خورده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/Futball180TV/91517" target="_blank">📅 12:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91516">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/91516" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91515">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کاش یکی به این کصمشنگا بگه اگه با قطع اینترنت فکر می‌کنید اسرائیل حمله نمیکنه و فیلمی منتشر نمیشه از خر، خرترید  اونی که بخواد فیلم بفرسته نیاز به نت کسشر بین‌المللی که به خرد مردم میدید نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/91515" target="_blank">📅 12:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91514">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!  +منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/91514" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91513">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!
+منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/Futball180TV/91513" target="_blank">📅 12:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91512">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
لشکر10 سیدالشهداء سپاه کرج مورد حمله اسرائیل قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/91512" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91511">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uejpfCbXsEvH0DAzMmBhfB355eDfcHY64FXDCXtGX2GvHNzIcncynitKlbAL4ms0LPV-dxGNjnYqlby3QTNQLmdN-1rn_DwWfzbjgK2g-R58xn_6uo1Uri8RCpoNa5XfEqlt69gm4nS69CbNmzCS3MMbvqLNZ3G9TLvxvgU77ws1pEzRZWwkM-2eCeVGJGVvSE21q2SsYE13Ggp0SuS9aPq-jUlVVm3sLnZPWTstRNI-f0uoZyp7xemnt-FvRj8Bm62cr0fnMAPBIJO3ignIGeztXvo4NU8zoDLflXnWxLUm6rcaYoXEAYelsdaHwl8vjFttHlqmg2PFe3YDzq1HLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب ایتالیا در آخرین جام جهانی که حضور داشتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/91511" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91510">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/91510" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91509">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هنوز آتش بس نقض نشده!
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/91509" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91502">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAu1N3O1gNxdfu2C7OIv8kE1Oyu0fdg0doF7y0b_g4kYlhHSVKwoO_tcF9D8MjuVNDdbanolNF5LRP0niLyK-tboTyN0af-R_cgJDFIKxL7pR8g_RI7a6Px3FCeNCOpCLWuBYKAPLQNCdWsvobpFvKXyUGI6EMnKPpkwbOP9tEeZAwEZc7tJ1hHtt2wM7RNaulIKLgaWumvINT8iiX8DJE0FI6PjkEqx7wsjzUtcs1ok9V7mQBEqYcj0fIj1O4iwUN8lwjTgFA5DBbG--6YBE_-ZrwuQuMTUsVhpKNFs2RukBZPVkXmyAADx528_bTHO8hySBEPDnZZTfspdngt1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-VJuZwaiHVonNU10syijPUR2iFH340xXNWslavzYSWTfrCy3bDp5fMy0Zm4KGCc-vjEOYW3ixbzyuvBZmGv-plmq44Uu-10pH4sRDofg6trFkrhUBbAifDmuxIrTxjSpEp0HFt2qIyMqdsaaqGhS_qquuowhZT2vgrOedXadBQqlGUqEHg6lPEk_bYcikwxfIuTB3ugZYgXtMuRCjIATJBMVzs_32UW5Bc-rC_VGiv3_BuJxXwnjQy_2qbNZ7vSEQsgWL3RYTGOpyGIUMiIYaPq_fYadEAjehhtWCZ6LTntUq7du3yVSX_UU88Zi2hQtA_czaxb13vZvJThOK4t3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJt3eXT_nnNultz65T5Z9LfCSkYST53XerBerKz-V0P4XNo5VOmFViZGkXcQkXn00eugrux7Vy_vf1NGVxPdMAktVSWW7m1lWZlWa0C3x40HT2WBr5FWHZaY48DBJ65KhcwFXk62D5_KZvFuK1LocFZXKP3UBNs-Vin9iDky6V3jULrZ3mIOeJ59VQJHcur_x0UQ7Ct9SM7fnYsJ6MF2xl6nmngnvCGqFM-IfgHLbn-vU2WS9mDzhVHU9qwN4fRUfxYChC5mMSMvEbl5sk3XjuBoCJS7PSh11j2prMwRGIFa4fHYcOTKLlXFV_JQ2vPp8HwNb5Y0HelzEKGwUZhPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MP3lJo3DwungLjuo9xjvx2quGLUwSmYIj6es29_Qb-yiqNLrZnQ1SnwHUIq-ln0Eh0cUzmdTr1ZxXPoGXrOSsO1TwCymBKLriX8O1F0cgfzDcn1uSeSDlGBSCn03f5-EHGLX7sPUQBSkj2KceYrvf88TaAOsUu7K4atazndB-KWI480VbA3L7OqfFmNbP3C3Rg6k2sALy3WYopSuC5iDCJ_5hPeGDcoi6Wwz2zb7lnhgbAEvnnyflXd-LrYUNUnUCgWcrtvC6CjPFlIxrC7L5EZzWVAje4cHiCMFEhNALe5ALAG7vVv1wMJMrkrL_Yp4LcaJ24Sl8KrwJBNF1fmx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3qz0mE4yD0Ap5zckNYeBuzhnG_R-Au13rRqIHcGf-XGMo82YtddThk-4Z99ys96lKCIbprrVBQcJ8ceofivcYyzUF7SG55KlrEv_WkupdDlsrw_xfxMwZJgDp3Bho-Ms-Bx0QZPK-GbB_sIyOquNgQii9y9_OZjYGQAQPkl99511YiaOiTxCuICwQVU9ZutvL8fgEBZlMzTxQOLuB256lTcx3kT4mAm9G62SfpU32yW2mKMES5hHk8Tg7EyxAE_JJcBfLVzlVLgXusZzk3UO3hdpuHx4J_0FVeFS2wZH4CXU7CnR6eGAkAHfDiXGEg1SWMLbpBYqKNFkKLdCx-T6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QARl3EcN0QTtIWD4jWYundRkclxNiibNKcDt9XavURl3DX9FDDEqhB21uQ3D0sF9eldGv04Hh0YsEz0TSfDI1m_-_pM8vBfsBwqAWRrr4mYaiS-7yNUCOK3dRIrqTtS8qaRT0Rkmkq4Lds5eCx-Rkm7Q06u5T8WZiTaGjm0JZziw7kn-z2STbf0QlZsesD2DrnF2yalmPGPVvbR482oGwnfjVy0xzSvxbAnlrTAJHyDpjraZwmPel7NzxNk9Red5U4fFIah9lwmuVWGq6buS8BWBWcW1ROh-owWhkCCMOFtUCp-NXjgHEgbmcbctaxXNsq3env5tdG8ZC7k-Qr9yNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1tOKVohpdgs5FvRGQPdTuO7DDsEtmpsJQoELQ90zHQ90XoZEh8j0uO2prz8C9fFRpn7QFiXtYuH586W6doK6PjEHwWHxG-XNliY-iibt9US_5hjQfD3T-EusqbQCRxWzjiLAgZMHKfPelrrNUWGjdZUruHN9zdlykcH7mtZnOk0g8tqyyBz3RWZXpze4A3U190EzHXILpPbPNy5h1qiOFDxZPZrdio4GRnH6wdhAmU3t-LblyN4A7VVGa3I_OVbre_jmshELGGpk-hAISQIIj4IumeGArkzI5UzvY2Vohj9FBD-gEYtPRIqZAk-Q6qYr0iJzu995sQFxUhO9TJs6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
تیم افسانه‌ای رئال مادرید 2010/11 و وضعیت فعلی آن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/91502" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91501">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91501" target="_blank">📅 11:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91500">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی
صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91500" target="_blank">📅 11:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91499">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzTr989rsRMnQdPUAH7abnu4Sg3QcjRjjTFfm_AzJ0G9Y_gBA1XINyoA9vDfi6bTF-a0mWJ23TS84nhh-M7EL5BPQpOxHtnb2rUMaOjY-kE7eQjk_L5mX9_Y_C6eoavvm2m4lKbDucI1Hko1D281d0UIXXqFBM4ass3kNZ7Hl04Sld5kbnh_VPLthihSi9qrwDASxwoIwPJwPYCqL-WlUBFmbyITHSADiK79z7ZXCNtSPCJYI7GEYoAWrZ3QTdlx70nwU9DewUU2j_oXMnjagBQCWbRRk-fhhYhRSILD0y1otyIjnR8skE8fHxX21ZmPzbOQ-RzChz7VAS1lYNyj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووووری؛ فدراسیون دانمارک اعلام کرد که خطر از سر اریکسن رفع شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91499" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91498">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGqLhr5dPEGp7GFlUYDZEVcpU4KgqTGgKr3Nl5IhsBXfkbbLp8cDPCC0WyypZNBDbesdVlXstgaLU6HMoDw0PVUL-dYoYjIly-5tMIaj6F1TrkZUeWgSAGfMnWmUk580GUfwXLBGM9wtoyI2-b6Bw0Qssmv5iNBH0bBx-H1AYuSKTWg-XJpgJxi-FMzJadYP1xVNFDS-u6C5EQFvGrBYupNNhIINstqZ2jeyaW3taf68j7CJqmA1AOdakx8FmJqOYlrKPV5XA1GtAecw7IeKrf4bC3e9yD7vVpTbXdjw8dy8gOS5xEz6esXaTdMZTppwukcznq_joKzhNPo3mCnGIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
پوستر رسمی باشگاه استقلال پس از دریافت مجوز حرفه‌ای AFC و قطعی شدن حضورشان در فصل آینده لیگ نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91498" target="_blank">📅 11:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91497">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
موج بعدی حملات‌ اسرائیل شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91497" target="_blank">📅 11:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91496">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMzfc1lR2qyLgu5HyzvNnz9ft4s683CBHOkwckXxB4VuDFBgetAUM1iFbsQhAdKp5Pm72SxsCZXaUMm5jJxTS7QUwAf4kqLMKcvi-OErabQTiyATRRI34hE6uqQNJQdEhGBj21pxwH3ua0W6o8S_pyGZAiKc4mloHaCQcaxEjpwnD9oijp_fgdyA2qquOgcjQJemiFJ6JWEZE62KPUxdjiwIa0PtPvp-r4ErQi154ZdJTtAIAjQ4rL0WAXtqFyT1LCKxjg_QZ8fYImImDoep7B634EydM0g5QyG4NkRQ314rh925N0sNwXKAU5L2Qbo4FTKM4ReCTO3KWji46rn7mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایلان ماسک: تنگه هرمز به نام اهورا مزدا از آیین زرتشت نامگذاری شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91496" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91495">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚬
بیانیه اتحادیه اروپا: جنگ خوب نیست. متوقف بشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91495" target="_blank">📅 10:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91494">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی ایران به مرکز انرژی اسرائیل در حیفا و ناصره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91494" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91493">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st-w2W1N_K9wX-75-xFp-69oNsQ2ta-6tRWehY0wsCsxeSDfed04IcOK_zIWbLWcI1CW-7QD11cwIE7U024nWwIMxLfMILtodTkjgt0SrlWIVadi93oMRiUyONzO5jJMOVhwjQCnvrCcoTRlwADh2T5W0PNy_vLlk9g61k-9G6WF28lBqbCHMPSzC5bdne4mWoOf4bDl1UyLy608-GRlrduAv0yd-y_UpnyQLIpdwGgY_ystfkeze4HWgs4ppBHIMyEzJslFHjGW79aInVbDDPk2BsHUI7uzc3Up2xVtBHhsIDLMqul6GlvM3N-dmQoD-bm0GlPeDGujWxkagUpRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مرکز اسرائیل هم اکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91493" target="_blank">📅 10:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91492">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری؛ موج جدید حملات سپاه به اسرائیل هم‌اکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91492" target="_blank">📅 10:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91491">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN1tW1nbWGNPUkaASieMYyfPMn6oY7-6QLpI1CMEXx_RYLsNhGcFt7T0jp77jqwVDKbkpyvMa3JHXs-yMAH7_lUZr3ITFJyukjarw82xSTpL7QJAeoOEg4xal7ZXhMNEssfs4N4GCgGj8ivJSaE7SsBknuFq-00jPHBfflBlmlJyDDghAoh0aP2Ys5Xk4D5Imslj7KgDnplq0NfPsGGTW5ptyBjOcrDp4JAdM4GBx8HzcWHlh2TzjRNTQHE4h7KxxCCpnMm9CzugXv-XwbZ1AVcnlKKV6l5ptR4vWaImtOF_y9ZL3he19A4CIPEPXKPodYcKM9-V8sg3lLu00OUMZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تفاوت‌قدی عجیب هافبک و دروازه‌بان پاناما که در فضای‌مجازی حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91491" target="_blank">📅 10:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91490">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران: ثابت کردیم آسمان اسرائیل در اختیار ماست و هر جا رو که اراده کنیم میزنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91490" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
فوووووری از رویترز: با اعلام انصارالله یمن، یکی از مهمترین تنگه های جهانی باب‌المندب برای آمریکا و اسرائیل و متحدانش بسته شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/91489" target="_blank">📅 09:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91488">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14bce5f84.mp4?token=tPZj_KBG57uEeRqLJlmC46PFnO9Zk-zF7WpfxSb7yZPNc1s-6L1tjGdAry8_3-mcD6YrZUtQ8TKi-5oIYtz7mXs_d8CsBZb12ng98RwNQZAfSARdP6RbeQSrp0WyMooWBB9zOildtZ6YhBMxBozItZ86O3iV6DsaA5yuj8CXVZ2pvX9JaAeaJ-x6h6kasg1LsUBNxK9YHyPJSb5-RE2OqGp3xVjT9Fv5U19IbaWGWjcKY4pVf_bLKG5Z2LEaHrcRomE77XwXEPU79La9zlfxxus4OSSpPLfPR-J_kFcjm2VleWCABLS_lcS8mJQ6BCuV3-QNanW7oDywM8iofCbTIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14bce5f84.mp4?token=tPZj_KBG57uEeRqLJlmC46PFnO9Zk-zF7WpfxSb7yZPNc1s-6L1tjGdAry8_3-mcD6YrZUtQ8TKi-5oIYtz7mXs_d8CsBZb12ng98RwNQZAfSARdP6RbeQSrp0WyMooWBB9zOildtZ6YhBMxBozItZ86O3iV6DsaA5yuj8CXVZ2pvX9JaAeaJ-x6h6kasg1LsUBNxK9YHyPJSb5-RE2OqGp3xVjT9Fv5U19IbaWGWjcKY4pVf_bLKG5Z2LEaHrcRomE77XwXEPU79La9zlfxxus4OSSpPLfPR-J_kFcjm2VleWCABLS_lcS8mJQ6BCuV3-QNanW7oDywM8iofCbTIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ورزش عجيب و غريب تو اروپا اختراع شده به اسم اسب چوبی که هرچی از سم بودنش بگم کمه و تازه براش مسابقات قهرمانی اروپا هم گذاشتن. فقط این ویدیو رو ببینید
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91488" target="_blank">📅 09:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91487">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
رادیو ارتش اسرائیل:
تبادل آتش میان ایران و اسرائیل احتمالا چند روز ادامه خواهد داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91487" target="_blank">📅 09:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91486">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88d8579a12.mp4?token=EoMWmCSKLhFpVnQKBZ95FDO63dJAoQP_E1VEuI7b0oGBEbHxgCsvbzqY1VvffUvPQiK0-g54hjl2C1XLDh-UPbPFLKAAFYFcopYus1INpgz7BWsh6iYNYqwCBm6mHJWXcUvmVuvKpYvxEeP_Ml3GqFon6wQhBxpS3BjJEVmoIOzSh67bEBo45bbQt24rZtHyUcfs92-0kmdiNZXgUeonKqblSnHEhIqcPJVvEN7oZ1FVKCMIWFd5BV6DjiW-RJ7SI0gr8LoPPgmVpBhfVgaoYl-RM_SwZrCOIHCW-bpQWShe3MGLigBL2UWuAOagsQ_zxvrXwecA9-ZC_JAsaVtwMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88d8579a12.mp4?token=EoMWmCSKLhFpVnQKBZ95FDO63dJAoQP_E1VEuI7b0oGBEbHxgCsvbzqY1VvffUvPQiK0-g54hjl2C1XLDh-UPbPFLKAAFYFcopYus1INpgz7BWsh6iYNYqwCBm6mHJWXcUvmVuvKpYvxEeP_Ml3GqFon6wQhBxpS3BjJEVmoIOzSh67bEBo45bbQt24rZtHyUcfs92-0kmdiNZXgUeonKqblSnHEhIqcPJVvEN7oZ1FVKCMIWFd5BV6DjiW-RJ7SI0gr8LoPPgmVpBhfVgaoYl-RM_SwZrCOIHCW-bpQWShe3MGLigBL2UWuAOagsQ_zxvrXwecA9-ZC_JAsaVtwMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
خانم جورجینا درحال ترتیب دادن موهاش قبل سفر به آمریکا برای دیدن جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91486" target="_blank">📅 09:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91485">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران:
دقایقی پیش، عملیات نصر را با هدف قرار دادن مراکز مهم پایگاه های هوایی راهبردی نواتیم و تلنوف آغاز کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91485" target="_blank">📅 09:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91484">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a069e77f.mp4?token=ZFySDt-qhTk4a1TOUlbsdhn5VLNwYSxzSM6qIwDK1D6ZXiqzGUn4sbjMH53Isv_mub4QTRVHzVR11yNxoLV7x2-DzaYkksECnJfu7taW4Az9utpnzTPbb8xqevvBGT79AAPHc6URo7C1Fi4xcoYkUL4OEoboOMPBgppFR-UxYJ6W5nFFmscBtf_7wQ77S_zYQctReuFvEYcRsGbcBeirBsa7UnfQ-5IPrwg63yC2mtE_POed4kQrfuvRVlfCi5Vtr8S2XYP_jIa8YELThlhqJCm5eoAGCAJSDEqEM-c9aVGA_8b1xKuGAkWV_KG_ClXcHyn58EiC5qklLyhdOl-1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a069e77f.mp4?token=ZFySDt-qhTk4a1TOUlbsdhn5VLNwYSxzSM6qIwDK1D6ZXiqzGUn4sbjMH53Isv_mub4QTRVHzVR11yNxoLV7x2-DzaYkksECnJfu7taW4Az9utpnzTPbb8xqevvBGT79AAPHc6URo7C1Fi4xcoYkUL4OEoboOMPBgppFR-UxYJ6W5nFFmscBtf_7wQ77S_zYQctReuFvEYcRsGbcBeirBsa7UnfQ-5IPrwg63yC2mtE_POed4kQrfuvRVlfCi5Vtr8S2XYP_jIa8YELThlhqJCm5eoAGCAJSDEqEM-c9aVGA_8b1xKuGAkWV_KG_ClXcHyn58EiC5qklLyhdOl-1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صبح‌دوشنبه و پارت پنجم ورزش در خانه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/91484" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91483">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
احتمالا با دخالت ترامپ وضعیت جنگی ایران و اسرائیل موقتا تا بعد جام‌جهانی متوقف بشه. البته اگه ترامپ این‌سری واقعا بتونه خایه‌های نتانیاهو رو بکشه و مثل دیشب کیر نخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91483" target="_blank">📅 08:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91482">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از یک انفجار مهیب در پتروشیمی کارون ماهشهر حکایت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91482" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل: طی چندساعت اخیر به ۲۰ هدف تو ایران حمله کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/91481" target="_blank">📅 08:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91480">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=gJLdTZPHcIgcvbZF2MC8FAC6OX90xqMPrpQpgTuW0sfgedChtO9MAhSKwwVi0FkgRT5VEcq2za-WauBd97s-9Kta-q_VpfsE1phIHe6eZpFGfjgj_RIGkJS-axz6CRWHbd8Bcfc69EZKqofq1KJfUGxfydhEER09XlcWxHW20aUv9LhdQit0Hu60wXmcWAehQTN1KPCIVeIEUt3KDWdcAgckV0Uvzxxvc8O10tioJnrOvkA5BGWYu2Eli87mr_5WJ6KO-TSzNdf8ym1MoMIG1xuscJcVujiSWX-m5zqWRHjKg__EUJGj3AdYTRlfL1suFV9aYdPTq-nuqxNHnGJn7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=gJLdTZPHcIgcvbZF2MC8FAC6OX90xqMPrpQpgTuW0sfgedChtO9MAhSKwwVi0FkgRT5VEcq2za-WauBd97s-9Kta-q_VpfsE1phIHe6eZpFGfjgj_RIGkJS-axz6CRWHbd8Bcfc69EZKqofq1KJfUGxfydhEER09XlcWxHW20aUv9LhdQit0Hu60wXmcWAehQTN1KPCIVeIEUt3KDWdcAgckV0Uvzxxvc8O10tioJnrOvkA5BGWYu2Eli87mr_5WJ6KO-TSzNdf8ym1MoMIG1xuscJcVujiSWX-m5zqWRHjKg__EUJGj3AdYTRlfL1suFV9aYdPTq-nuqxNHnGJn7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از یک انفجار مهیب در پتروشیمی کارون ماهشهر حکایت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/91480" target="_blank">📅 08:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91479">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از یک انفجار مهیب در پتروشیمی کارون ماهشهر حکایت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/91479" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91478">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇱
گزارش‌ها از شلیک موشک از مبدا یمن به اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/91478" target="_blank">📅 06:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91477">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
آژیرهای هشدار در سراسر نقاط اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/91477" target="_blank">📅 06:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91476">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omjkqmDR6u0EvdFQVBtEFAtZ6TnsIn0ybX0XwgeBEzojqkuhtFHxw7DFqVAtBJ5Xulp8gg2iKaTyqLyb-uviIVv-vlgoz3Fv9725k7yMXtKdPAYHh8obHnLKb292dmWNQfYvzEs8rscIrdZnqnOz_e0b-m2HSaW68Nze8x_6GoNZVOY5FTov8xhrcyJ_OdPsaA0AYULQ7JUsBiNk4XC4LeiH17r7d-9qDzl9wMIYpyxeJ-Z9L8cwZ7raFd-IkPCm3qAMKKJPphdc4cVJrm9RLiEWtfau35dF3qJ4pH1D83s6rc4x1G3uUvCPlz3U2hhuZ0mQxNM57RRC6L_1Wnv9Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
آژیرهای هشدار در سراسر نقاط اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91476" target="_blank">📅 06:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02c5f07bd9.mp4?token=fgmWMVwRfWx-9IR7r-xti9Ld8QG16MMNSNHnZMGtagCXiOY6fx_4rTO8AvKa78Mx4fkOrMHlCunyVuxHGPbTcmcGlz5UGVkrBZ9lp_xS_6VE9t4Rrv7trUVnY8l4oOIs0VUDjuV1IE7d0dnrH0d7docTUIy8gnpBqagQ8RO0rugsQEgNvhgzlcvxB6T23kAVqLpO7cGxZnPVjUMZzAGlU2bO8T4XnvVq1ySQlGjWeWXBkhYT6OmsU6JNXYC4WXoWJW7XUF-5KyNN_1kYkKjKkObIVPh7oL0_qC5oSX90NVn38OvkMiZ6Nw9jT02mIlqPs-uL4LUCr0c7_9GNrGdVzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02c5f07bd9.mp4?token=fgmWMVwRfWx-9IR7r-xti9Ld8QG16MMNSNHnZMGtagCXiOY6fx_4rTO8AvKa78Mx4fkOrMHlCunyVuxHGPbTcmcGlz5UGVkrBZ9lp_xS_6VE9t4Rrv7trUVnY8l4oOIs0VUDjuV1IE7d0dnrH0d7docTUIy8gnpBqagQ8RO0rugsQEgNvhgzlcvxB6T23kAVqLpO7cGxZnPVjUMZzAGlU2bO8T4XnvVq1ySQlGjWeWXBkhYT6OmsU6JNXYC4WXoWJW7XUF-5KyNN_1kYkKjKkObIVPh7oL0_qC5oSX90NVn38OvkMiZ6Nw9jT02mIlqPs-uL4LUCr0c7_9GNrGdVzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انفجار و آتش سوزی در غرب تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91474" target="_blank">📅 05:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
⭕️
چند نکته ضروری هنگام وقوع انفجار
در این ویدیوی آموزشی، جمعیت هلال احمر چند نکته مهم برای جلوگیری از آسیب در زمان حمله هوایی و انفجار ارائه می دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/91473" target="_blank">📅 05:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i08uQgNfIk8FcsVBbfVkS8eheF7GRwstM67ZMqHm61mOyBbc7Kfrz4q0QEbe-3GrbtrEyFcqud0mPqtTu4kJpSBzlgh5FRlLsvSuBDESw8fLXZEdy6YBqcJUh7I7O-lzghUmhS1WZzOOX0TpPoPuWJ4UmZl0yDWs4LCZtHZ-bNLbaXNb207ULhd_S75IGVTThzj_0sqkdVeevDxs-ye6nNomw-avFkZ-_yL9Aki-cbGv6A5URnf_h7OD9o6QVQ-Uuk97BftvHMcUpWSc3l_-SV1cLBaa1hejlwORLECqhtZ4WR54v2hQIJcW4wul2jB3g82fh9NwXANPQZGhhMrUlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
♨️
انفجارهای شدید در نجف‌آباد اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91472" target="_blank">📅 05:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91470">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
💪
#فووووووری
؛ فرودگاه مهرآباد تهران مورد حمله قرار گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91470" target="_blank">📅 05:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91469">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کانال ۱۲ اسرائیل: پدافند اسرائیل در آمادگی کامل برای مقابله با حملات موشکی ایران است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91469" target="_blank">📅 05:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91468">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e78148f7.mp4?token=O45vfpKu32PS3NOwQpF0nnxRDWITsO-FPzLhGMN0HSVrXo3D8OmYOzHGWrbBrCe_sQb-KEtueulsNOGImcoJkdFvVi_PvRbcha6NgIDkB_qwBUTXa7iBfAwZL70tRa7TJ96p51tgmQ5SeTWPM4xt_imU9eJlVAtN2PxjtzKNvwaPfhRQtZ1pzaf2-hdRTaqIxo5qWjcnfvPsuSFvTlz4zuB807YMklq4rdaS-ida07TL3xfPpWOIjkP9ujhHYcsueGQcCEyOhDSby2liAi4PnY4WHtJNE97u4m1KV8j8A_b4NX8g_f0sudVkTSQybSLvCDylnv70w0r-Ys9IyyKQxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e78148f7.mp4?token=O45vfpKu32PS3NOwQpF0nnxRDWITsO-FPzLhGMN0HSVrXo3D8OmYOzHGWrbBrCe_sQb-KEtueulsNOGImcoJkdFvVi_PvRbcha6NgIDkB_qwBUTXa7iBfAwZL70tRa7TJ96p51tgmQ5SeTWPM4xt_imU9eJlVAtN2PxjtzKNvwaPfhRQtZ1pzaf2-hdRTaqIxo5qWjcnfvPsuSFvTlz4zuB807YMklq4rdaS-ida07TL3xfPpWOIjkP9ujhHYcsueGQcCEyOhDSby2liAi4PnY4WHtJNE97u4m1KV8j8A_b4NX8g_f0sudVkTSQybSLvCDylnv70w0r-Ys9IyyKQxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
🇮🇱
تصاویری از اصفهان، ایران، دود را نشان می‌دهد که از یک انبار تولید پهپاد پس از یک حمله اسرائیلی بلند می‌شود
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91468" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91467">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ld1ej2XQfkUOAnJ8s1_XARO3wJZY2RqfWezUgOtFA34OCk4pf8Gu4_du9KWKNJs1haSEixhCLAAyPd1m19Y35QtAEcIU73OCTiXCNvDzpFhVD4QCyjNLCzDDym6YazdxpvoAnRO-toOiqsuT2l0LUi_MvcNgdIl8yxr-rN0mg6reWcgtp6fO5srKD6e-difcsf-sh8WqcEpP2Cr0GWI9uT3Comamls-X9iB1HGY1S3jREbTOdZ3RkKMsS0sLywKtaiWhxDv_1BRA14zLQ1LfkaqqRQaM3JzG0LIVdoWBdXqFIPI7lRRwpWqWPHk7rYJqa_29x8FM5LtGVS2B0ohzxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری از انفجار در تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91467" target="_blank">📅 05:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91466">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
شنیده شدن صدای انفجار از سه شهر تبریز، اصفهان و تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91466" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91464">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXDSAVOdmN3OlijL5NXZMBdG2pBxJEXOLTztA7kdwZrY2sDaFJCl0EX7p3dcZHX4q289a8bWoAD4Y_C7n-_OgfiDp3C-kenhPgCvRcFvzt0pVd7NG4iBTYZC0nZOiHAky5RW1BKODW_blMfKVDnMhjcwT-QLl7tPemQOV6kuyGpVZWk3RtYbgkG1-FVI5tmdy1emBSTp9bxMYLSngoefWcqprX09iLc4x17CcqucsQJjKXbF5qOobQC3cGwYQJcIdqM4ZI9na1XeDjG6eTg8hvYOCpYtpi9X3nHsM1GGK_IUtrCYQxc0YZ80XxvQV97h5YGLfp7YL_Ch69JhH45J7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQZtv0kwGm71rG5kwE19XIMPW9zPfh3wKHeDE-e4DPpIMkDai6I54ExnrAYLIlXm2hMtJp0pg_oVAOw9c6YuqZRaXRPGUKY09I4hD2rpUz4BQqP3HBjmTEunsXSLPpGHNvKk1HgL1ECoINHku1y4NgwJoT7Dsruyix-cSyrP9UyUOz95EaQ1iNCwzWTYspAOepveNVMz2le1--iBDlW9TvYm2WuUrI01C_h_1EGCgdfo28cszb_hU3p2veU9ln4L8a6ajOx4eul3xSq74J1smo1INW29068u1x0a3-bb3nbqPEEJNcLin_osiv_pCOfR8oxrbQ5Ex7B4VvhrlFuMhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اولین‌تصاویر از انفجارهای شدید در اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91464" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91463">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
شنیده شدن صدای انفجار از سه شهر تبریز، اصفهان و تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91463" target="_blank">📅 05:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91462">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار محلی از آغاز حملات نظامی سپاه پاسداران به مواضع اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91462" target="_blank">📅 05:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91461">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR2VdaAkv_4fK-GiIjM1LNmKIHrd-DnWBLzjAfeyhIWIXtMCizEfrUdKDc1I24jlous0hn0NKZwEVJDx5b5rQn3wsohKJJ-ynBZld8XZYWvYmvJyOYXTG5L0pxw8_ovAci_cWtblKvF_p3fmO1E_0jhjJJf6hsf-zc0BBYhU0UXodjmFFJ2ZYXvSIvI6HTvKPFHZ83wwgpPI0sq-jCc0shSRj7Dt-rhy4_Fnz2n2QV_UsJsfRKF7vJquKGPrAE7Qh87oWmhexF9Oruz155GURHkAT8PEoXE-3R0whys2wjR0oRhVS8bIm0hL6whbKvGHeMlhGbD2CyeMjv_xE07ARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
ارتش‌اسرائیل از انجام عملیات نظامی در خاک ایران خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91461" target="_blank">📅 05:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91459">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_Sq7TXNz9YBk26W8c-9CtqiqFcFHDO_eIKao1uU0USc6TCQYxiXs1C0tCwFQchmyweuBLLXhhl6oGnJMGzj7MkHmt4ump_Tv11EMkV_eM_oucXI8C2u2WfdtGB0kPu6i3eNZE11d1lQjzmR24ZSBHdyHSuAIklCphUt62uM10hTRITRaS-jkP-V9KFVpk5i5E2_zrhdjorc81VAfzdDXAsolcnS9hc4nLI-e0E1O06A2SiIOkZecNgkVOozZY-ebkn0oyiEqdmoRHHcA2nfHL4L3J3aRLsjr72zF25jIKTUB9gvuYFt4Dq7kgbX8VPAEbmeeM4EsL3ag2TU8XASDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
👍
🏆
علیرضا فغانی شریف در مراسم تصویر برداری رسمی از داوران جام‌جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91459" target="_blank">📅 04:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovkRFM9pdJKZbVZLHPSQOy4PiFSugiZ-uexG2kzSfa8Sbbu58hqf-yYtsyFWooqYAovl2Lcov4Ef8VEp09sfo-AeCycoawSJYLXo3GE8bVwcicseQwE_ciBe9GLeSNpMnjPgXpM7odwuTuxG_KdZ7l8jcL5PE_28-mlXIkSI0zukQabawl7YIz7RTuVdLXxw3gUP6-nXUEKM9RPt7hJQ-feK-uWfraZhAA0yvFVFedmNglrkL0etKWr1yB4bA5S6Bea7sKGkhem4RUmIo3QYOnpW-b5tmbkR3Bbc6ufk1AjzF3BL-DnRhD8CduYW6PoVc6ae9hluTYaoFj9QqLbDoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgJqKwmm6NUNpvN1LW7OTR5c9LCvDMhpeL6Q5hdnACQjX4G6Yxv3m7mNjEF6GZFlUZW_xgMLyaYHB1EY3cg8kYDGDx191xVkVMXfvjswD66lMy_za_gK1vw9RkVHUNUwDmJy75de5PAkZ5ywV_NYvq_7vOrZLGMG0kB7YDSU3QppzpE73cFFs9buood3G5tnZUvC3PzkRbhwt_GlKLfbeLz_HMzdfKYh2j0aL_wU4uqF2DGrP2soQ6wnI2IZhTJfwIcc3Ihc0SEkRgv-je9kTw1WQ3rgQ71o8yMQPee4qg8MwsHnpTX9D1STv8ox1bhfU6tWCtqoKaU4cIjl5-c5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s79HeyV4w1YP_zB6x3AOmwZV3txJ7f9zOnkjfobv5ohJ0cUZU9ewwDIYG-xXjhk1NUglnrnqchoJv-JwXphVOzQVxbHBaeN6bBvFSbu0rsvFPqnG6CP2-WABgRGRQ_qeu-ymsGUw_1uKYRZYhNR8x-JhqgXcwCL1PptZGmxjfi57DwfxoYPy6gngHUrAjGM-RJNGAUeiC6KqdRVX5DhCU0FvkweV67LPC6ITJO2IDu758iupueblgdRWsVsiuQVlkn-7I24mlO_IWAb1eQorU-N-fppL-l6JzsCNo91ji7V1f9liWXr2KBwkXzAPGdn1QL_3mUAPZ6DGpkm9GJTLSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تیتر رسمی دیلی میل در ارتباط با این فاجعه اخلاقی
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91456" target="_blank">📅 03:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_m45A8lY5F8i3xb98CmnXiT4x0RMxYj6XYrJNvnW20bFXJkMGtJcx6FkGIdfnrxWNR7LaA-uJfvcqE5CVnS18rlKqAMMLebU7TwG8oEf9J4liG8ese2oKZAIkSFi8_Dv_47HQrJrsV0P3OMOiIICZN8HySiq-S8jyeZaAfr9KYhPAPENfsHcg44OsNouvmTPdE8z4DOSLZNy0mtyjfniIhw3K7o5wEQQTZ3JyUo10017mF4QsuZVueFT_MupPKmDLXNzZ9fVucaiGyEJbkLBHP9okqjpTA355K_CKctKaKvO7QAIY4MiIF-e0p3sPxQNRFtypIzZeKT52-6VibZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
فلورنتینو پرز:
آیا ریکلمه رقیب خوبی بود؟ نمیدونم اون کیه
😅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91455" target="_blank">📅 03:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQNibpkam6d8Q5B6O-aMQy1hj1R7XXI0mORem2cKw9XoQFS-QlDF0PdycxpSUIoH8mOG7bSDLi5C6z8AHD2GyGnpqkzB-wrVWihpaHFOpfjHXzhbpLobKqqCjmx_MVJ4apK6ICiHcIdHfkZah7w9CtzXjKAFzuLgw5rwEcKIDaMcAOO1CMtdobXUEJANSygFJ5kJ8wcuZYBG11rrkHKpw82Kan0nHhxtpcxwzs0fY5u-of2L8DmtWIo6GQP-4-nNP3Ej3LvmGNHLtS8wEL6-OAgk8izIY9WqtddujzvVlsd9IlcfyQbdGmMEgWM80TGkqULwXEtmwjDgGkr7YI8jSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فاجعه اخلاقی و آبروریزی بازیکنان هول تیم قلعه‌نویی در ترکیه
‼️
‼️
‼️
گزارش رسانه دیلی‌میل از فاجعه اخلاقی تیم جمهوری اسلامی در ترکیه  فوتبالیست یکی از تیم‌های جام جهانی که در ترکیه اردو زده بود، می‌خواست دختر ۱۴ ساله بریتانیایی را در هتل، برای تعرض به پشت…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91454" target="_blank">📅 03:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2ozAXz1M7BeKkyvhMMXOZYC4kdIB8ZDwESIwMjpp9KE8myjtzyZppvDUeZEGmwUkMoTs-huZJtC3Zi3woOmlktCAdjXyuEPBVYjHsU9rfRwp_BbUCBndeoagSYTnglo3GyCYTV97_6M3vmBc2Eoheyq648qzMfE-x-6nSyXDrcOrvK9vZXOEYy_xreLmHJGC2_UEplWCq1WSQ31qNcvHgAqinaxlz1IO2wtY2yLFnb98HyheIeroXsWu44vsWwoUsyZcausQb5YV2n1AmHe1CYcs92JYGv22L7pv5IChbT5Gv33bL2GZMZwSpXTnVYz5khKFnvvlFtORsEr4WI8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فاجعه اخلاقی و آبروریزی بازیکنان هول تیم قلعه‌نویی در ترکیه
‼️
‼️
‼️
گزارش رسانه دیلی‌میل از فاجعه اخلاقی تیم جمهوری اسلامی در ترکیه
فوتبالیست یکی از تیم‌های جام جهانی که در ترکیه اردو زده بود، می‌خواست دختر ۱۴ ساله بریتانیایی را در هتل، برای تعرض به پشت پرچین بکشاند.
این خانواده وقتی متوجه شدند در هتلی اقامت دارند که یک تیم فوتبال عازم جام جهانی است، به نظرشان هیجان‌انگیز بود. کودک بریتانیایی، با فوتبالیست سلفی گرفت.
آن بازیکن، اینستاگرام دختر را گرفت و با وجود اطلاع از ۱۴ ساله بودنش، پیام‌هایی مثل «hot» فرستاد و خواست روی پایش بنشیند. پدر این نوجوان گفت دختر وحشتزده‌ام پس از حادثه، در حالی که با خواهر ۱۰ ساله‌اش کنار استخر بود، می‌گریست.
پدر خشمگین، فوراً به هتل اطلاع داد. از پذیرش با او تماس گرفتند تا با مربی و مسئولین تیم ملاقات کند. آنها عذرخواهی کرده و گفتند بازیکن از هتل اخراج خواهد شد. پدر گفت روز بعد متوجه شدم آن بازیکن نه تنها از هتل خارج نشده، بلکه هرگونه تخلفی را انکار می‌کند!
مادر دختر می‌گوید: دختر دیگری در همین هتل، توسط همان فوتبالیست آزار دیده.
خانوادهٔ اول، نتوانستند خانوادهٔ دوم را برای شکایت به پلیس قانع کنند. از طرفی، مسئولین هتل به خانواده بریتانیایی گفتند هیچ فیلم دوربین مداربسته‌ای وجود ندارد.
باتوجه به اینکه تنها یک روز از تعطیلاتشان باقی مانده بود، پدر تصمیم گرفت در بریتانیا موضوع را بطور گسترده‌تری مطرح کند. می‌گوید «نگران بودم به محض اینکه آنجا را ترک کنیم، آن بازیکن دوباره به استخر برگردد و همین کار را با کودکان دیگر انجام دهد.
پدر از آن زمان با مقامات ترکیه و نماینده مجلس محلی خود تماس گرفته. می‌گوید: «هتل، آنها را در اولویت قرار داد. با آنها رفتار متفاوتی می‌شد و می‌توانستند از هر کاری که می‌خواهند قسر در بروند.»
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91453" target="_blank">📅 03:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpTAUFCp3MLllMRJOoNWa1iKAOtY87MWs1DWUrRI7J9vHl-stH0HIGKIjkNoGj1w7eYoKWEXBQsrXrR32coqJ4gD_iElC_MHuSnXg12JMczcPBqR9h8OBG8N8E5xfW7cbIrW79TK_YQF_rlUQ9rqzXZaZO4R3Tkq1o7iS38KngMmPRBzF9g9u2TVePJBMgAI1rH8VkBBApvjUqZf7wpzbMSIN38yhkrSQyuAdtqnaBKxKmRQVOYEgjk1Hn5IbVVFAgP8P0n_Su_s6zz6ufbBjTTJcbRqYSlOTTKjbt5xiOYGIvVVKrnpmqTGxrZaqvg_l7yDNwmc6X-7hHUmvl2cag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
💣
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91452" target="_blank">📅 02:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🇪🇸
#رسمییییییی؛ با اعلام باشگاه رئال‌مادرید، ژوزه‌مورینیو با عقد قرارداد دو ساله با قابلیت تمدید برای سال سوم، سرمربی کهکشانی‌ها در فصل‌آینده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91451" target="_blank">📅 02:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrYhTvCY6Q59G2q_XWu1aDDDDlUJFz6we1EmF0k66OWdAfIVvGye8lg52H5Fka7Pd6oDLGqYGjqDUR3chPKa1Ptuac82QXxfBfJX1g13pMl13Ul78ZcE42zqfnL8uqxpj6lknUIpMwEWFdTB-8AxU1fSd6g0u0NTw6m4tnMViXko4pqPSz-zXQeQFlH04Nco2VvmFJmDX_vq4oF3TL0lqK9IL7LP__ec3lA4f8xserPpakJOtYS9DJ5cpgJjl7JfslrroBrJsCGp5NnHFa5cO34XfOO7tN6eWoAiGRh5_S9LB647vTdk0kRIedcReyiiyAHOeYkRzB4BEHxWI7hVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
فوری و رسمی:  پرز برنده انتخابات شد و تا سال 2030 رئیس باشگاه رئال‌مادرید می‌مونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91450" target="_blank">📅 02:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U73u7CF7iyqkvE6OIKS5-JWb7MqeOtIxGmKVJv_2VtpWr707gwYNLxXhXx7_zRB4dc7l-3SuFzqCjFSR-jvsnqjMoCzTmQ_Mp5Gjos_j26uGu_TonngZoAsbqOBZIzoCjGuGrfuW2VaMI_NSSbNE7Ow3bNk_GcymbyViewzwObBYheZv0jKrGpp5MiIHo7lrJP2xSCDpPWEl09T4Zb_pL5A4qqlC2yNel7wnY26DL9ZEcFgq64yNwqVypdYYNbxJbW8a0HcyGQ4sdDEgqvO7Pr2YrdeDXObp51QMYKACFllavdLfz_jmbJ5uFrj9vF4hTV5lFruf2DoUszci7j7YjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
فوری و رسمی:
پرز برنده انتخابات شد و تا سال 2030 رئیس باشگاه رئال‌مادرید می‌مونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91449" target="_blank">📅 02:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gntm2lJ3xNapRB3jJbOTPomrTlq8okv8NZE3W89OTHwH4CqP8afvK4G5W3R5l5S-XgdbQV5vu1mrB7crS0xWiH7PlCwLEN_sDW1hz_f9OexngWK20cleilTJojbgKBKSldESjkNBUSsHbUyPRk2OxlExf65yMf4nd2hCaIqr3WUwDpRHHSpv8iHqCLJ6J27Kk5R9mW1XAO111Ci2cjhDiaKP95be3kJvs1VqHTkv9ftPorrGmK6B8eKKbvs5SOVJ9zCSy-PelmcYsVg6zrydO6pCMSxePguIlKTpCCK0_N--7Llosr7ttBeHXSWYbkXiSEfQ316zOJ6msuUCuJJ0mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خوزه فلیکس دیاز: پرز در تمام 60 میز انتخاباتی مقابل ریکلمه پیروز شد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91448" target="_blank">📅 01:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
ترامپ: نتانیاهو چاره‌ای نخواهد داشت جز اینکه توافق با ایران را بپذیرد.
من همه فرمان‌ها را صادر می‌کنم. نتانیاهو فرمان‌ها را صادر نمی‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91447" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ql6wDBr2zl9rSnOrQk2pGalNKHXjgpwayhHIJR5odu4FlWkUEcLKrifCA0GsmsGvmzSEOaYzLinQAKggzNHdq3P73t7o83rDvBHQXcrAsrD9_EnHhNxOry7aeHZvIrO25PJ6yKG4GVI2f7Fe5mqsmWbtEthYTO9FXHm0-slTUd55_ygZSmIEdgG6EuA8qBMCBC7d93edncQJKxSXeYCz7_CE1oWIRFwdB3vZjCzX4u_utWW9qrK5EgKN__foCVqYXQU-8Yu7IDivkITC_EUvtVed0pKwitqcm1u61r6f4aQ66OA3B5A0ESM8oMEMO7XIYXdBQ0Xt0Vc8qD8wOafBRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
منابع مختلف اسپانیایی مدعی شدند که پرز یه گزینه جذاب دیگه بجای اولیسه تو آب‌نمک داره که ارزش ۱۵۰ میلیون یورویی تعیین کرده و بزودی اگه اولیسه رو جذب نکنه، سراغ این بازیکن میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91446" target="_blank">📅 01:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91445">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/46b3a86a4f.mp4?token=i8GIiN1mai6Xgp9fO2KpNDoi_JTR3HpUbQvBOyeTyMpF4cT-NZvnUZDAIRm7Yldeqp_7Jp7U5ocRlAnLUbJduSVanleU8kNBKbXrBXSsodEpt-hDIQ1jdSNTUYCKGLALCrq7HqJdBTGH9Bs2Nae709k-OTlKIKW3cGF1qKNTtGng1lQACrxxk2X7ygs61SD6aChcPORZTbTeV9bCrtGy195cAafOyLYHiCg9nvW0gUwSQ2GifO7Yp-FS4m6dSmpcVjjH7sHWeGXOerujcXiYxk-tOLKr94ZqVHnxKgAfFpGeKSC2vrZD2wzDw16kWFNgbQRzWiRStda5gJO0C8sBeg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/46b3a86a4f.mp4?token=i8GIiN1mai6Xgp9fO2KpNDoi_JTR3HpUbQvBOyeTyMpF4cT-NZvnUZDAIRm7Yldeqp_7Jp7U5ocRlAnLUbJduSVanleU8kNBKbXrBXSsodEpt-hDIQ1jdSNTUYCKGLALCrq7HqJdBTGH9Bs2Nae709k-OTlKIKW3cGF1qKNTtGng1lQACrxxk2X7ygs61SD6aChcPORZTbTeV9bCrtGy195cAafOyLYHiCg9nvW0gUwSQ2GifO7Yp-FS4m6dSmpcVjjH7sHWeGXOerujcXiYxk-tOLKr94ZqVHnxKgAfFpGeKSC2vrZD2wzDw16kWFNgbQRzWiRStda5gJO0C8sBeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لامصب توی چهار دوره جام جهانی و در طول ۲۰ سال، انگار اصلاً پیر نشده و چهره‌اش هیچ تغییری نکرده!
🙄
کدوم آهنگش؟
۲۰۰۶
👍🏻
۲۰۱۰
❤️
۲۰۱۴
👎🏻
۲۰۲۶
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91445" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
