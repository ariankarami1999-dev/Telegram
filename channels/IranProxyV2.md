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
<img src="https://cdn4.telesco.pe/file/dG2zjc1dnl9h8vT7T2uKhOMt_fSg2xmAJNz6oVT-qYvtilRKnL1b78OTzVaRy82dXDIhmw76if6MS5iGkLJVCJa82o6ecIjH_L2Z-ueFH65tGvDdV6tBtANpLqod7pTamW7blwZsyexO4nfVOWzO4p7KojUwci57oG7P5yAAb-avEPUhMWCIhg9nmYslEaDxgX987z2i0Kd0gamSFAgudMwk1A6hJViMn2I93JW-o8619dM8cmbOoBgp0AXsos3zUW-8J0bRmD4iwUZi_WXKQbm6Rlfa_SXtY_mzvwlvP3RQZB8e0dxfwr5zQH5_GzQd89pbUtcsUMorXxSaEm7efQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 37.6K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 11:50:17</div>
<hr>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 355 · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYVwnK64VO_eVRJrGKPECM_EFF7KcMTKPdrRcD3K5Qd5vrWpRTagkG_v5kNMvhwrFG9xIrc3mgV8ZbLYhtt0LfznQGVzNB1SNydxUMUr7V6telPr5HhS4ykRllIDJgvmeLoOA1y7vP3s0t4epM_dmLFm2aMvQmLvuA5j1rvJ0AUG-tkTk1R5a0HJFBg1vdjh2XUC7YBG4GfZhrZjFa97UDuGJZnmgQKBzRVADolmcTyWxWjSNkocttFIxOlCYZWdU1CSWQi4P1K2R5KQj9CSpWstt3jFktHJnanAP6TlctFiCCV67kdSXR8-rDaG7nwK2fqBp4tB1md3BN18o-JaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 444 · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8370">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بشدت، بشدت حجم سفارشات بالاس،صبور کنید دارم یکی یکی صحت سنجی میکنم و تایید میکنم قلبا
❤️</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/IranProxyV2/8370" target="_blank">📅 00:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=etmkIz7hNqGww1QC476GLdrGfLBA0bEWq0pXJesJrn8lpQ0GZaKbnIlydkiZ0jTvnaxNnZ-MtdpYiVMndpPLvzIfbG2cy8x-guq0og0JdEwYi5yqb2MZwnDJ-yjkFratTpyueIdBo8OcGvGF0VeHQBsoDqn5CPW-OZcDIxsRFtSvEdJiHKijYa4CdOOi8s_Ck7Pq4-ZQK-fU6Kzh3DUAuBeltQWyvRm-MRcv6MdbKomdC3_0tpY02HKizWTo06wwiLrVkWXRabxM7zeU6ej9HsiITP19VS1CMPr191s-x0WLL3zAjxKXLxRoZeyc2RCogYCi4Ou88qJRSRcH42kYo5Ib90KbbY-2tbZZMz_9Z2GX_h0BtBaMuhMYhF5f6DDv84OKC1QvgKU9NJjy1CajUQYbgtINz8THKyB5lJpinov1j6uixeVx0A18aDjwcCkuRZJZAFOUBOwvLjHKwdHuYj4RRhcY8N2MN5jTr7RfkJgHXCtaCpAi9DIOHju8d6aRe1gB01CbRAcshwMKLv7j1Cp-YWuTUD9B9zXR2HtM1saekxwoMVayiuFgJgCTf5I0JgTQj0GBWvkIToSYfasKoH6RVVP77ssjSBoQxhuM96yKV3IaJGlalZxId9vBw1e7CW1LjTHiduEPwVbYxLjnuju0M2WelAmJxePb3vfdOKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=etmkIz7hNqGww1QC476GLdrGfLBA0bEWq0pXJesJrn8lpQ0GZaKbnIlydkiZ0jTvnaxNnZ-MtdpYiVMndpPLvzIfbG2cy8x-guq0og0JdEwYi5yqb2MZwnDJ-yjkFratTpyueIdBo8OcGvGF0VeHQBsoDqn5CPW-OZcDIxsRFtSvEdJiHKijYa4CdOOi8s_Ck7Pq4-ZQK-fU6Kzh3DUAuBeltQWyvRm-MRcv6MdbKomdC3_0tpY02HKizWTo06wwiLrVkWXRabxM7zeU6ej9HsiITP19VS1CMPr191s-x0WLL3zAjxKXLxRoZeyc2RCogYCi4Ou88qJRSRcH42kYo5Ib90KbbY-2tbZZMz_9Z2GX_h0BtBaMuhMYhF5f6DDv84OKC1QvgKU9NJjy1CajUQYbgtINz8THKyB5lJpinov1j6uixeVx0A18aDjwcCkuRZJZAFOUBOwvLjHKwdHuYj4RRhcY8N2MN5jTr7RfkJgHXCtaCpAi9DIOHju8d6aRe1gB01CbRAcshwMKLv7j1Cp-YWuTUD9B9zXR2HtM1saekxwoMVayiuFgJgCTf5I0JgTQj0GBWvkIToSYfasKoH6RVVP77ssjSBoQxhuM96yKV3IaJGlalZxId9vBw1e7CW1LjTHiduEPwVbYxLjnuju0M2WelAmJxePb3vfdOKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=qPZxRaaP_QbdnfopYI8_HGg1tkJk8sxrRa484i_wVqVdD-fyR0GUPMOy_n434of2hxnX3bqfMVIjud99zGf4NdFkL5GJd1YgN_as2f4A4oZPN0DZENiFtYE57BGyjeEQNEGgDgoKT6xK0xHbKwj6oAmlhUkM2HuQoWC_Px1aTwaBB-1jNrM26w7eKzSgzmUVd7X5-RlhUpFnkeVLsRnrDtxcKckQpwcJx3DTZwPQl9A9x7Ti6kJ_uZX6plXrHfLE124PuvOpr80cEeHf97ZM-p3zhJDIVo-MWdUcYUjyxog5TndCIIt4tSCaQpeC4d-_WfPCM2TQIUlJDM1p_fAnmR7cfiBX-MJ9SGdEefNEVkrL5fzHkyT1xXBY2HmfObuSJ6vu0BtracKwK1lqv_-5lMBY392caON3UbjDqqEBu0I3kB99y1Uq7y3avN7yMNfLj7vcn19X-9VzM_m3Er5Pk6XzqKJ1mzRpbfJ7-lMqJL3HLsAdxJ91gye6MrfzGChpw1eDs7Sx5aeViIpWOu8b0ogYfifP1PGbgvzb8a4VW-QNxxRMNIEg_sg36m5gPhcxIEBdDjWfLjPCdPH_ltUcqbXWXQY-4_NHSaS137zXsRx7hs3FXDLNUOXmhTSxDBYXingWjhmQ2CyJ6dxrczmPPLotPZe8Qmpt2PUxWf66w5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=qPZxRaaP_QbdnfopYI8_HGg1tkJk8sxrRa484i_wVqVdD-fyR0GUPMOy_n434of2hxnX3bqfMVIjud99zGf4NdFkL5GJd1YgN_as2f4A4oZPN0DZENiFtYE57BGyjeEQNEGgDgoKT6xK0xHbKwj6oAmlhUkM2HuQoWC_Px1aTwaBB-1jNrM26w7eKzSgzmUVd7X5-RlhUpFnkeVLsRnrDtxcKckQpwcJx3DTZwPQl9A9x7Ti6kJ_uZX6plXrHfLE124PuvOpr80cEeHf97ZM-p3zhJDIVo-MWdUcYUjyxog5TndCIIt4tSCaQpeC4d-_WfPCM2TQIUlJDM1p_fAnmR7cfiBX-MJ9SGdEefNEVkrL5fzHkyT1xXBY2HmfObuSJ6vu0BtracKwK1lqv_-5lMBY392caON3UbjDqqEBu0I3kB99y1Uq7y3avN7yMNfLj7vcn19X-9VzM_m3Er5Pk6XzqKJ1mzRpbfJ7-lMqJL3HLsAdxJ91gye6MrfzGChpw1eDs7Sx5aeViIpWOu8b0ogYfifP1PGbgvzb8a4VW-QNxxRMNIEg_sg36m5gPhcxIEBdDjWfLjPCdPH_ltUcqbXWXQY-4_NHSaS137zXsRx7hs3FXDLNUOXmhTSxDBYXingWjhmQ2CyJ6dxrczmPPLotPZe8Qmpt2PUxWf66w5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
وضعیت سرعت سرورها
@RUSSIAPROXYY
🇷🇺
📌
آیدی ربات جهت ثبت سفارش
👇🏻
✉
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aq_VIkYvjZgJ9bsEcNzWMKaaa2nqWyS6vovvlIlwIuCcj4AfYBsPeIWvPivMUITwuhjnu03HapnUHftbxyYaB5UuCobIS9ExPgqoGDDpmvQea4vLXsI39CWsUSPAYKpJ3xNwNP4wi7hOTtqSvmoltBA-QgCuhVabkJshHZlMKeZfmCvCUzApU6tJQ2rDAnVrtVGVlJ3rhFmZTE4dsF5_9ocsP5YF-wrmd0xW1QpOfUkPZfcFgA2H8YwvcbCpxsAumaS5XZb8rVoBpqa9yIJcAX3DbjNg5n1DELpC7f0tgvl6C2tlAA7pXZdioMN6fjZnxh0C1wXW_81vGz7tLRjW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhXcFxRkjoF2EAVWjJViThs1qgyeLo3UGp8TQKUTw45Of3X1iRlVHeSRYG-x9aUyqOmr_1h4Wlb4WF124iPMrCKhwNN-X2RZIoBXrJVjBgl1-UEz6m7KukXG9AtRNAQEbcpxsqizkCYzdlZ8NuWP2ylJSWrGZDtAkBz8XWJAXGwgh_pvQhalhoaHd9Wn7YtHgiY_Fp9uSxQP8hYhzBc2vV1SavOHmwCQISkJXzeuXr5T37-bFJ0uxZtwRFM-SOHPJa9j9CCK0_XGffLhg-mqYxRg13m0_G5gA7LWErAGaWJ8XhMPjRbniCfGnbIHFSWMuzZExQu8lPByB-AtyurfVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=HakFbqZDpV7ppKn2k64v-2OJYVs3pzHNr_XYG7hg75v2lhudhQdjtnMNmkclflfeH_e8MbRgxo9Ci2RUXmT1ldCKml5lmB_6CkARXO84Cdo3Cww5_NLpXSQ1UxynxkOAz-YZ8IOfuziveQ-4H1qSdUVK48dczZ8H-QJyb7Xc3Yn_d7C4Qdv8OvR-dDb3EnpVzcmPo39KhvDrxOYmOZ0QMhtqYx-TYxfOi7eiGv3iv75U-xIs7m7WSvj9JlXTJ3vTJa0azB-Qle_vBqYwOLE67_RAvOoT9dfrJy7anHJFqQJ_E9cjLSltzqf8FXTw93FgC0GHR3F-Vk-K1_aLcGuOyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=HakFbqZDpV7ppKn2k64v-2OJYVs3pzHNr_XYG7hg75v2lhudhQdjtnMNmkclflfeH_e8MbRgxo9Ci2RUXmT1ldCKml5lmB_6CkARXO84Cdo3Cww5_NLpXSQ1UxynxkOAz-YZ8IOfuziveQ-4H1qSdUVK48dczZ8H-QJyb7Xc3Yn_d7C4Qdv8OvR-dDb3EnpVzcmPo39KhvDrxOYmOZ0QMhtqYx-TYxfOi7eiGv3iv75U-xIs7m7WSvj9JlXTJ3vTJa0azB-Qle_vBqYwOLE67_RAvOoT9dfrJy7anHJFqQJ_E9cjLSltzqf8FXTw93FgC0GHR3F-Vk-K1_aLcGuOyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O3Ywb10oFHCiI7cOqLf5XBrFHAoToX0P7E6dFL2bJhbuxp4lA6SIViUPbf-NcshhWyu42i7-WbR87YVngyDo29vKGv6jTyo7dMbbqoGR8dpfcbnRlar00y670uZadVHnjpgFfDs8dltViD2snmDjsE1PjN4_UlSgGKLJTmBK4wWZ43owDB1y2xBWDp6e3VaJu-rCtAKP_bTx3C9-feRB6s5dg-FGylkZ7dVn7AdL4foDUZXHH_zN7hMXPcMd0dBAmoQXAJJq64ydE-A4VN0YX2XBhwM806w8CWndTNQPUaD7a4rYNmmh7CWBxMlBRk_llgkHvVkacO2QcE-JYkfkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pmdrVSOWqzFcxNn3ynPQX5hgsKiJnFQ-zgkDgpCMN8ouWwjKV3WaGRy18Sk6HiWMeiG8woXlZbIwN7YqCcUwNf3R6g6NqOR9Wp7lQj7YDGTkMWG8tq0suk_NG1pzfJ1doAcmy4Q9s_0pzkQ2Clydcs5zvUt0wKUgqkK0NJJLqbtX16PgDe54rcHyZegY48fL4-183Gxr1SMGJ5qgRrGPwp8hMOJsGAE3a1dkbF3xY3sOUqojKa3Wy-EDMvtlUilHbUD2gdHyeSF6ibjTKUKUZASmWFEbWF9S4L0_hVr3GlxAbVNUk72gf_fVH4rvC-zL1o1dEn25oYcCFGxJuu3iOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CcUxQv-WXBKUH3sfCh1DvOVzqq92t9eZOpV-fxnY0gkKWv_zKpLwF6oZiqesxw3rJ7FuuKHgMngTfASlQoqHu6sXs1kwvYZhAW1CVnhkPDIhPvBCZHR5ggpztsn0-gWWXFn53TcH2q2hIcG6j3ELOT-_DafOUErrO3vFh_2S8peB_m_7yL6jwAA32VywZHE_or4wcl7xsYxqUIwrRTTfTCb_aDoKY1lw_vXIaFeJb0M4LIUQFZlPjqCEybKuXD_ZH5jr05w7S2x9u0j2C8GBIuY0QKrSSbyQUEoxXSF5kE0c7wm68C0AdgRiiCWAZfLvFg73ND81pcCh0PEfw_7gXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قیمت‌ «سیمکارت سفید» و «اینترنت پرو» در بازار سیاه چقدر است؟
🔹
اینترنت پرو و دسترسی بدون فیلتر از طریق کانال‌های غیررسمی و بازار سیاه فروخته می‌شود.
🔹
قیمت ۵۰ گیگ اینترنت پرو در بازار سیاه تا حدود ۱۲ میلیون تومان اعلام شده است.
🔹
سیمکارت‌های سفید با وعده اینترنت بدون فیلتر با قیمت‌هایی بین ۴۴ تا ۱۲۰ میلیون تومان فروخته می‌شوند.
🔹
فقط اقشار مرفه توان دسترسی به اینترنت بدون محدودیت را دارند و این مسئله شکاف دیجیتالی را تشدید کرده است.
🔹
کسب‌و کارهای آنلاین و دیجیتال از محدودیت اینترنت و هزینه‌های دسترسی آسیب جدی دیده‌اند /اقتصادنیوز
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvzLNch0E753rMDS_n22ipGan_XjCjrEuNLJfqjQJSTm7KvY0Fwv-1cXJ36nOTWMmdJWXRYAbUn8tgfZklivdGtOhbXhmwhRsrzG3d6_tQn4f-1wgaJbKQNXVbiMaPDvSnubbRVeNp6poy8vqXRaaf_3zkCjENXDI1zZfDjTwkqsLrb_Fcy1m_WKg05rL-LdQovrNv1R-sNd5UYxbb-2Xb9uubban5fy7FwijhRt2MMbEHRjy640iu6RHoeEenlW2e4RM2BrBvXT9VnDTPafyV-p8aff7ARYiaQTesz5KLpF0JO8hDXY7KP4MvS3RiXj-ld7DVcgeB1YU2-Poh6g1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره،
دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول بدین صورته که شما کانفیگتون رو برای پشتیبانی ارسال میکنید و همون حجم باقی مانده براتون با ضریب دیگ چنج میشه به سرور ثابت البته با سرعت کمتری
2⃣
- روش دوم سرورتون تبدیل میشه به سرور تانل با سرعت بالا مث سرویس هایی که درحال حاضر در ربات هستند ولی، ما به تفاوتی باید پرداخت کنید بلا عوض
3⃣
- روش سومم اینه که کانفیگ هاتونو نگه دارین بعد از این شرایط نت از حالت ملی به حالت بین المللی تغییر کرد به ازای هرگیگ، ده برابر اضافه تر حجم دریافت خواهد کرد
🔻
@RUSSIAPROXYY_Admin
📌
به این آیدی جهت رفع مشکل پیام بدین
👆🏻</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIqgZXkJWm9Smdif2e31uwv9vCMDzPl4iGf8rDt_WA9L9fGRwaf5kOqp_U5XUSXChO9jKiQ-Z49yEk5S6FVzQyzdg0LO-oZpaVVTomqhEyYdTnIIk40XOrnSyZwG0uPEsOD6MtqRYMaQl5lvGULM3LZHq2gc81AB0AhBvLeSkJ0YrXcnXgw2Zjf1rR8ePbV2mBs3-xC9GNlGdmLXeneeI987ryfZOw7yUZ1QY2JitzGd_QtUD3b1VCCpJcwkqxqGRzrclFnL8gdSipoUJYn_AWCpfll2eBFuugyPi1Hz9T7L1HIYyx2JocdaCaE9_pSDhnnPLh-9BEGSt0c2HqipbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✈️
دوستان نهایت تا امشب سعی میکنیم سرویس سرور تلگرامو اوکی کنیم، هواتونو داریم همونطور که وقتی هیچکس وصل نبود تو دوران جنگ با کمترین قیمت ممکن و کمترین سود ممکن بهتون بهترین سرویس ارائه میدادیم، سعی میکنم از جیب خودم هزینه کنم تا مشکلتونو برطرف کنم نگران نباشید
✈️
سرورای ثابت برای نت بین المللی و کلیه اپلیکیشن ها و سایت ها و... براتون تو ربات با کمترین قیمت ممکنه قرار دادم بازم امروز
قیمت هارو کاهش
دادم که دوستانی که شرایط مالی مناسبی ندارن هم بتونن کانفیگ تهیه کنند.
✈️
🎥
📸
💬
👾
📞
🤖
🔍
🕹
📱
⚡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de826422e1.mp4?token=puHtLXLUx68HoUL0-gzG8WO06fTaAPYvVkAXIvhZ74OKGDri5SOnDgZ2HiYmYWdVOurI8TCmgQBPoZgZ1ffzbygAZsfAsFcT1PyqP9nAZh3RFt5jAyeeMnZfxpCwtweRH1xTBIivuCEl5a8bZm6CMLBB4X5OrqGynawnywoRQqNcd_4BDmfSlUcmFL4DWrGBsV7C0HLGwizoKdh75KHLkPphEt8PFI8PLN5DXsD7vX05cv_XYbCTfXnsYiiCAOrq9fkMXJNhNckZqMsYHbKkgojRow415N10L_pxCqpXs---m9b1vqK4H0u_Bu8Ed-R63zpxjxFCtO6pSQ9XGaHDVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de826422e1.mp4?token=puHtLXLUx68HoUL0-gzG8WO06fTaAPYvVkAXIvhZ74OKGDri5SOnDgZ2HiYmYWdVOurI8TCmgQBPoZgZ1ffzbygAZsfAsFcT1PyqP9nAZh3RFt5jAyeeMnZfxpCwtweRH1xTBIivuCEl5a8bZm6CMLBB4X5OrqGynawnywoRQqNcd_4BDmfSlUcmFL4DWrGBsV7C0HLGwizoKdh75KHLkPphEt8PFI8PLN5DXsD7vX05cv_XYbCTfXnsYiiCAOrq9fkMXJNhNckZqMsYHbKkgojRow415N10L_pxCqpXs---m9b1vqK4H0u_Bu8Ed-R63zpxjxFCtO6pSQ9XGaHDVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شهبازی مجری صداوسیما خطاب به مردم ایران:
اگه اینترنت 5G که افغانستان داره و مسترکارت که سوریه داره اینقد براتون مهمه؛ خب برین همون افغانستان و سوریه زندگی کنین!
﻿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8316">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⭕️
اطلاعیه:
وزیر ارتباطات گفت در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم.
همچنین طی پیگیری‌ از ISP اعلام کردند که اینترنت بین المللی شبکه خانگی متصل شده است اما هنوز زمان مشخصی در مورد اتصال دیتاسنترها به اینترنت بین المللی وجود ندارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8316" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8315">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=D4FK1cab1GFaeFr2jK4qgbad4ocZgdF7iKReZn-r-RCO80FkkwtMkqPMuyIyeGZ7XZzcQrECGjWU7F-myWwZYV8fO14wGzRINwjthpmoa5hme_N2O09c0QaCEQI3ZOFemBs-5A9DcrFesWxi9ZpIdqDTylQR2exdPMT15yrOY07M6GDOjUSdZVGzK51s2-dmxfKX7CsMofrS4E17C5lJlbznKLNch65TQIN2pKJk-ko5vA1iSPkYaqGyuYpqyRbahEE45i2FYOq6zrcZ5n7No6Y33lDNpz6sxtxsxzzpHyoNf5zjs4pwi_mCXtVQu4Z1Z2X1AwLHFkaU7TC_zyD-og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=D4FK1cab1GFaeFr2jK4qgbad4ocZgdF7iKReZn-r-RCO80FkkwtMkqPMuyIyeGZ7XZzcQrECGjWU7F-myWwZYV8fO14wGzRINwjthpmoa5hme_N2O09c0QaCEQI3ZOFemBs-5A9DcrFesWxi9ZpIdqDTylQR2exdPMT15yrOY07M6GDOjUSdZVGzK51s2-dmxfKX7CsMofrS4E17C5lJlbznKLNch65TQIN2pKJk-ko5vA1iSPkYaqGyuYpqyRbahEE45i2FYOq6zrcZ5n7No6Y33lDNpz6sxtxsxzzpHyoNf5zjs4pwi_mCXtVQu4Z1Z2X1AwLHFkaU7TC_zyD-og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی:
اینترنت حق مردم است؛ عصبانیت مردم کاملا درست است/ عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8315" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8314">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اژه‌ای: اینترنت پرو و سفید مثل پتک در ذهن مردم شده است
🔹
رئیس قوه قضاییه در جلسه با وزیر ارتباطات: مسئله‌ اینترنت پرو و سفید مثل پتک در ذهن مردم شده و باید با موارد خلاف قانون در این موضوع برخورد شود.
🔹
در این جلسه دادستان کل کشور و وزیر ارتباطات به رئیس قوه‌قضائیه گفتند با بررسی‌های صورت‌گرفته، احراز تخلف در قضیهٔ موسوم به «خط‌های سفید و اینترنت‌پرو»، قطعی و حتمی است./جماران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8314" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8313">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">vless://8b7dbddf-fe0a-4405-b8e9-bfac4d9439ef@185.143.233.235:8080?path=%2F&security=none&encryption=none&host=MHI.ARTARONA.IR&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8313" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8312">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">V2ray + Psiphon:
vless://3728fc28-910c-4a9c-888c-c08c3e2f4a06@snapp.ir:2052?encryption=none&type=ws&path=%2Freq2&host=snapp1.gptpersian.ir#musiclovers85
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8312" target="_blank">📅 10:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8311">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">احتمالا اکه پروکسیا درست نشه با کانفیگ های ثابت جاشو براتون عوض کنیم اطلاع میدیم خدمتتون بابت صبوریتون متشکریم</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8311" target="_blank">📅 00:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8310">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حجم سفارشات ربات بسیار بالاست موجودیش تموم شده بود مجدد شارژ شد، صبور باشین، دارم یکی یکی رسیدارو صحت سنجی و تایید میکنم با تشکر
❤️
💲
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8310" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8309">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b69Qz81Q0nzZ47e0HXQHgRmWBCNGMvOBCW4Jx1AASkMLwTJ_cgnebUvO11Dh01YIMnXfULLJJuUzWToG3l4oFESdnZZ-4sekdBVrQfr9G0fXYBPdtnouCbADztPiUz8NkR2BTQTeqQocHGQagelE3p12QEc_X_04FJ7IBZHuEv2-dUdKLA4q3fh24PNUCKhS-2TSY7DxE5HMYBaWTNKnESxSEsEJ4lPC5Fk-mNCmYKxaOQTtvEkq4x5bAal7y-Up9QsYZIfbEgYuJKcOr2NsVztZdAuTce_p0UDpoHm7yJaMzcme9o0x1cYGxUEog_IYMfIAitEkaGztLU-3z9c_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه چالش دیشب، برد 2-0 بارسا درست پیش بینی کرده بود
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8309" target="_blank">📅 23:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8308">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
معاون علمی پزشکیان:
حتی در شرایط جنگی هم بستن اینترنت راهکار نیست، زیرا وقتی کامل بسته بود هم ترورها ادامه داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8308" target="_blank">📅 21:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8306">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⚠️
ترامپ به فاکس نیوز:
‼️
در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8306" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8305">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=qQiDrUgUO-mt0d0n7wxC8LyEDybRLIaVKqtARR5cUwCNoIrU8sFvIlyp9blySeYHSj6Pm7P5zDWIktqH4IhVy79Oijo3jCGVEnWuRgv7i8Cgq7lJIUr2vIRVpvuxdbRU5LYK3fbjJQpemm9ARznQKpUnW3upZcVlM6eX455IomMMf6YRTkoXV0cdGBpW4tD7JACmAZtqOX_bqkOiyj7UUZgEfAvZ7G7bi0ddnz5Xlfn_0EQv5w5wPqnmtlhO181v_4PAxFYQ0MLa4TNP-15UwXNDCeyhebbrgSTylacINFxZ7Qu60IXiUr6sTIHsw3lcWBA76N-j5RJs5TEx9x0XfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=qQiDrUgUO-mt0d0n7wxC8LyEDybRLIaVKqtARR5cUwCNoIrU8sFvIlyp9blySeYHSj6Pm7P5zDWIktqH4IhVy79Oijo3jCGVEnWuRgv7i8Cgq7lJIUr2vIRVpvuxdbRU5LYK3fbjJQpemm9ARznQKpUnW3upZcVlM6eX455IomMMf6YRTkoXV0cdGBpW4tD7JACmAZtqOX_bqkOiyj7UUZgEfAvZ7G7bi0ddnz5Xlfn_0EQv5w5wPqnmtlhO181v_4PAxFYQ0MLa4TNP-15UwXNDCeyhebbrgSTylacINFxZ7Qu60IXiUr6sTIHsw3lcWBA76N-j5RJs5TEx9x0XfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت زندگی مغازه دارا و آنلاین شاپا بعداز ۷۴ روز بسته بودن اینترنت!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8305" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8304">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
تصمیم‌گیری درباره بازگشت اینترنت به وضعیت عادی در دستور کار دولت
افشین، معاون علمی رئیس‌جمهور:
🔹
در دولت یک کارگروه زیر نظر معاونت اول رئیس جمهور برای تعیین تکلیف اینترنت در حال شکل‌گیری است. احتمالاً در این کارگروه تصمیمات قاطع خواهیم گرفت.
🔹
وضعیت اینترنت در دولت در حال پیگیری است. نظر دولت بازگشت اینترنت به وضعیت عادی است. قطعی اینترنت قطعاً به رتبه علمی ما ضربه می‌زند. در زمان قطعی اینترنت رتبه علمی ما پایین می‌آید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8304" target="_blank">📅 16:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8303">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">dalage pezeshkian 2.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8303" target="_blank">📅 15:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8302">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">داریم بروز رسانی هایی میکنیم که  سرور های مخصوص تلگرام مستقیم وصل بشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8302" target="_blank">📅 13:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8301">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8FNfWMESXhjNpU5TAw6rnRj2L73suaLyHDBDhhYDZ52cYfKEoZpdUhvo9axkm0zLh2XQgs1KpNOWcPoEpVPWL2xa-1k2yKVPaXQHhiIGCcJesIuscrNfsiceLkI_20467q_NnDKpUogSPEj2Pg8IlMGxIH4zKhv9ENRo5oUhdxtyVCn227Jf4Vx7X4C93hoGWs5ummBIJ05WBfPxM6P3s1XZhp8h-G7qTAFXQ-RbCfw5ZusgskYB2xBbhqMTUDa0HgI_lGVgSbKDIV7GSHlx_d4InDr-_RVEqDF46l3kZk3zjUkb0VxGjPlIvFAHotzU3ERE8jLgOuzhTAa62lqrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
جهت اطلاع رسانی مجدد همچنان در تلاشم، که مشکل دیتاسنتر خارجمون رو برطرف کنم برای سرویس سرورای تلگرام، درحال حاضر همچنان فروش سرورای تلگرام از دیروز تو ربات غیرفعال شده، نگران نباشید برطرف خواهد شد
✔️
فعلا درحال حاضر سرویس های تانل با بهترین کیفیت و سرعت ، تنها سرویسمون که روی تمامی اپلیکیشن های
🎥
📸
✈️
💬
📞
🤖
🕹
📱
🔍
قابل استفاده میباشد و برای تمامی دیوایس ها واپلیکیشن ها اوکی هست، در پلن های (1 گیگ، 2 گیگ،3 گیگ و 5 گیگ) تو ربات موجود میباشد برای ثبت سفارش
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8301" target="_blank">📅 03:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8300">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
صدا و سیما:
ایران آخرین پیشنهاد آمریکا را رد کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8300" target="_blank">📅 01:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8299">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اختلال شدید در اینترنت داخلی
🔵
متاسفانه از دقایق گذشته اختلال بسیار شدیدی در اینترنت ملی ایران رخ داده به طوری که cdn آروان ؛ سیستم شاپرک ؛ سیستم همراه بانک برخی از بانک ها همچون بلو(سامان) و... قطع شدند یا دچار اختلال شدند.
🔵
بسیاری از سایت های ملی و داخلی نیز باز نمیشوند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8299" target="_blank">📅 00:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8298">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رفقا پروکسیا مشکل خوردن مدیر فنیم داره هر جور شده مشکل حل میکنه از صبوریتون متشکریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8298" target="_blank">📅 00:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8297">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8297" target="_blank">📅 00:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8295">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8295" target="_blank">📅 00:14 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8294">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgZNNrMRrrG39qjCatmmroFYUWEhFNbRbiKnfiU2xqm4jhoLaNPdOl2Zd5eRyrp4o4vT_7pO045iKJGI3yrdqipdPxQ2YhodrJbv9voZPd8fYVKujmx2dNzNC9A_IM6HXz6cfMBWDXuy71RA1SEcgAytk_Dz2_x5bfmEQrMxuS34W6nTuwKSQWb7rEf3Ql63FAxFJ8wuHywFYSdno44AtCUUB0XHrOJOnws-HJdUXX3ik-FuE9zfggXhsMSgQth0qYgl4KVLVlV0MldGEMtgQ-ca3XKPyVKTFVAZ8mt12sWc5vTZt0r6J7m7ifgsO1E03xHQJqF_aO10SxBiLAkDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8294" target="_blank">📅 23:59 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8293" target="_blank">📅 23:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=batf0rGn4UhOX2FKFWz40K8Ln-w2ItdUqdoANn18C3rgcrEJptShbqo-Sc6-KPCfOiksUynzSygOb2x0T6cXc1fJKB-mtnA9fJ11ZZgFzbJo90tmc9atmpL7tdZtLuUoQsO7pArVFFNuZcWv4dOvPCLQ8oIzhUhqCCiTYqCtyub26vLV--3srryZh-hDXk2pZFOUNJMC-FWioSFRXSZQLY_vZoJVvk21sB4219VDWdSQDRdD5fGu_Ht0IO3Z_AhV1ClqFIB0Hxuo-9HPdTxqq9TpHnc6F3YLAjYSUCj3LzS9McS4uh09WIGdq66PstIjxknEI75hrOpEYkn2NFadQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=batf0rGn4UhOX2FKFWz40K8Ln-w2ItdUqdoANn18C3rgcrEJptShbqo-Sc6-KPCfOiksUynzSygOb2x0T6cXc1fJKB-mtnA9fJ11ZZgFzbJo90tmc9atmpL7tdZtLuUoQsO7pArVFFNuZcWv4dOvPCLQ8oIzhUhqCCiTYqCtyub26vLV--3srryZh-hDXk2pZFOUNJMC-FWioSFRXSZQLY_vZoJVvk21sB4219VDWdSQDRdD5fGu_Ht0IO3Z_AhV1ClqFIB0Hxuo-9HPdTxqq9TpHnc6F3YLAjYSUCj3LzS9McS4uh09WIGdq66PstIjxknEI75hrOpEYkn2NFadQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی و فرماندهای سپاه:
@
RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8292" target="_blank">📅 23:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8291">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv0EY5QD1J6ggBumnjoPiKrOv7eTmpmAB5hhbImfpuYhbY1bYuI1jwndUSedzroh2md9f27sy0ECdtI6vh8bJIPVpYl9RdJo4q8UDbIF1G-4Jj_2R7LkRBUlaYn-owbOnE5_Q2Y3jlH1YRdami4idPUYH6GDjsOkwDEAsVgqc18qAZcYeXX-lMAClbkhPziZrHSg7nw-mBvGyPdh8PnFG5efWHLpr8YlzeB5EdE_Mr7BRg7MPEaMo-mnkgTu-8GtP6K7fvapzN_zGMQ4oUcboTFAhEE7ABtntz-XUSqgbEH2mJLcyvBO1iUEcrRtq3AxT3sIBWVYb0CxT3vjNRCTQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)  و سپس سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» آنها رسیدند.   او نه تنها با آنها خوب بود، بلکه عالی بود، واقعاً به طرف آنها رفت، اسرائیل و همه…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/IranProxyV2/8291" target="_blank">📅 21:55 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8290">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLSLOC8oyyxvtalWoYxiiiBpDuVhn7btu3not_DC7fTWWM9J92ETTD3yP3fMnmeuknWyDTmJxMytEDj1SFU-RoBXB50ZMkYgx-6WRNpWtAYaw5whbKkGbd4KUv9sd8YGre6mMsVfKbxnah_Rz6kgXVeBldW5jZpjmrO42cDmsxtFEEY5M3p4VEsaddS_HPVpW9cK5muahh3qDq8ncRwMq2jCUAWFEm5zlLP4IjRAQOsNw8hrm7L1FdPKwUihu2C98uaqmdZIVCyL4pCnvVo1pl5Ft343oNN2L0fpBSfCEEUhntyAz4t0PnRZGRgK11b_kIvNHttFi0YCd_h9ezn5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)
و سپس سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» آنها رسیدند.
او نه تنها با آنها خوب بود، بلکه عالی بود، واقعاً به طرف آنها رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت جدید و بسیار قدرتمند برای زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد.
هر بانکی در واشنگتن دی‌سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شد و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور آمریکایی ضعیف و احمق. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
به مدت ۴۷ سال ایرانی‌ها ما را «گول زده‌اند»، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/IranProxyV2/8290" target="_blank">📅 21:51 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8289">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✈️
جدیدترین آپدیتِ تلگرام
🌐
[ ورژن : 12.7.2 ]
- لینکِ دانلودِ داخلی ( بدونِ فیلتر ) :
✉️
Telegram ( Direct ) [ v 12.7.0 ] :
https://uploadgirl.ir/d/c99c188e-57fe-469c-91ce-843a37e803f3
📌
خیلی مهم : فایلِ آپدیتِ نسخه ی Direct هست و در صورتی که نسخه ی Direct رو نصب دارید دانلود و نصب کنید ،
+ فایلِ نصبی داخلِ یه فایلِ Zip هست که باید استخراج کنید و سپس نصب کنید .
+ اعتبارِ لینکِ دانلود : 3 روز [ لینک آپدیت می‌شود . ]
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/IranProxyV2/8289" target="_blank">📅 20:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8288">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت…</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/IranProxyV2/8288" target="_blank">📅 20:02 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8287">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_2tEEx6P7tcNzXNR9qOXOWgg0qOrlzVxJaTzzGJZH6T8MwS6fCewLO6Tl_JBt3rQRLyzJuyVmG4sMgIzpCw_58S_n4scbcGyxwYFB1MaBbuRQGSMy1yNLcs8-J7Dcu0gcWipZMcBA5PPFeeg9wVrWo4UhwJWyItq_oYbyFOmOhflNWNg_nQ8yVz8qfTf8YJy6HwSlob7MQhT0ay-jlzjOIXKyyoStBlaYZkM_ZcAXQU1NqOTuoAr57R8uPIv4iqTl_zcCYRN0AYMINSVUY8gA9KATdsBDgA-WT6g_FTegItGrfpcvUW_3JXy9gyO7umCRs1NU0huW9-zd-9CuL3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت مناسب قابل سفارش هست، برای استفاده در تمامی اپلیکیشن ها و سایت ها
📹
✉️
📷
🐣
🔻
@RUSSIAPROXYY_Bot
⚠️
پشتیبانی از فردا ظهر ساعت ۱۸ تا ۲ شب پاسخگویی سئوالات و مشکلات شما میباشد
❕
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/IranProxyV2/8287" target="_blank">📅 19:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8285">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyqbThrp6sTDWRIsYk27vIZ7P-AOOjPB5tCBK_QxKXNkR7omVJaYh1blr-p9SP7iXutwJYtUg8SAKTMsrKTNOfOaRkI9Pv3iJracpcOv8PocoItK81Y612vpavYUiKw1YquIAwC5pAiWFsg6hA9LTSCOFYrbIG6p3rkAKgh8PEHb93LcnEI7U010RRlQipHiMbpHLLKFB4D0wAJxceQBYYMoKIh4A46qBz-qKnMEKpv0UJSgfRBql5gPCgXlA2MBZtZkbrPyFT4fkW1vhnJ0DTvyp5XTHv3tUcGqjfXO88DlOSO6sWZG-ibIHcp2UEwxSxGduRuWXk0ijDlL3uCOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رییس کمیسیون انرژی اتاق بازرگانی:
سال گذشته هر هفته ۳ تا ۴ روز خاموشی ۲ ساعته داشتیم ولی امسال تمامی روزهای هفته ۲ ساعت قطعی برق خانگی، تجاری و اداری داریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/IranProxyV2/8285" target="_blank">📅 13:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8284">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید
@RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/IranProxyV2/8284" target="_blank">📅 12:32 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8283">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کامنت هارو باز میکنم پست بعد حرف نزنید فقط نتیجه رو بنویسد به نفع کیه
از اونجایی که خودم بارساییم 3.1 به نفع بارسا میشه</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/IranProxyV2/8283" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8282">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه چالش میزاریم هر کس اولین نفر نتیجه امروز الکلاسیکو رو درست بگه بعد بازی جایزه میدیم</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8282" target="_blank">📅 12:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8280">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">‎⁨الکلاسیکوو🔥⁩.npvt</div>
  <div class="tg-doc-extra">2.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8280" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8280" target="_blank">📅 12:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8279">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پزشکیان جوری اومدی ریدی تو نتا جلیلی تو خوابشم نمیتونست همچین چیزی ببینه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8279" target="_blank">📅 10:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8278">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118c9f04cc.mp4?token=o46iijYXBI3z5ARhBzzUZk0XZbXVjdkz3kyVwX2IpIT1eyaIzV18xyRvVj2iLfVTViKPWm6GYTyHVpMJcZtOs-2EDOy8cM_13C2ncp_I7fTOjIAHMi7Qv8a0xZ9XDLQs0onEYZPnab-3uRvkh2g6_wkTiLWhdV6iNzb6__TSkht7WQQjF34vGR-noLn3zR3qEgsWd1T91yYnPpBwcRUdivZwEkCNP52NsU-6butkMYJjTeWp7LGwzXguW_TFJdZ60SJV07DXS4ZZ9i4UmIhFIO-SB17MHJSdDW5NZD4Oc7LHmvFuXZHaEl3TJqhFo6GPKbOwXukvGji_hUiS9aMNvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118c9f04cc.mp4?token=o46iijYXBI3z5ARhBzzUZk0XZbXVjdkz3kyVwX2IpIT1eyaIzV18xyRvVj2iLfVTViKPWm6GYTyHVpMJcZtOs-2EDOy8cM_13C2ncp_I7fTOjIAHMi7Qv8a0xZ9XDLQs0onEYZPnab-3uRvkh2g6_wkTiLWhdV6iNzb6__TSkht7WQQjF34vGR-noLn3zR3qEgsWd1T91yYnPpBwcRUdivZwEkCNP52NsU-6butkMYJjTeWp7LGwzXguW_TFJdZ60SJV07DXS4ZZ9i4UmIhFIO-SB17MHJSdDW5NZD4Oc7LHmvFuXZHaEl3TJqhFo6GPKbOwXukvGji_hUiS9aMNvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری علی صبوری که میگه به مرز فروپاشی رسیدم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8278" target="_blank">📅 09:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8277">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oquYL-sC0uu6Q6APjdyaBEbaMVGf-VBJPK6SnMF5SoBpfkedastYRA5GtpHbgpIcZ-hM3sO1w8xe8WAKtxQ7PF-H4DVMNDdcRFSuEJIkYAa2sSdc5A7PgZXPZlgYSbdFSrbaJv1IDYAPoVb9lLeKkXjIr8g1DOhehC5zpwEeaL8s6eCe6Ty8TtsTn_Mv4Q10bZ6xBtqDATkKcHK51jpCvJGJreHfdBKs6G1nFNqgzO4M0HrzYH2_bQOljez86crprWelqpDxyi8BbRAY1GNlz4asNFq71yNv__Ql3QwLdyCOUi5OA2yduR_yRZppJb_j2bQQ8pe7LKmkRlovrpWvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی صبوری بعد این که ویدیویی داد و فحش خار مادر به نظامو طرفداراش کشید
الان این استوری رو گذاشته و گفته بیاید منو بگیرید ببرید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/IranProxyV2/8277" target="_blank">📅 09:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8276">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYo8MfuAjjeoeD5KkrQYctVRYkyz3Dp8-xEzZmK6gxKBhTkwVEEKiaF-j-M1DgK9_-6gtFOKlJWzusDHELFWXInCBGdlM1N-hab3EeNgnAniQat6NVj2TbJA2p9Pqby3f6GDU99elTs8u5RsegcW5plnJE_pB6zRpLZzf8Ub_Q_d0bL-LCN3ACEOMfN1MB6t8Jldsjlk3Avd9Ci4bbLuYzT_9L51fGd29lr_oTcUlvAYUiTy1HWvGgZC7miSuspQ2r3TWBRDQA4jaYrFb1hTTpdWP8azAQ7ySPiH1MEfSaymacLF7CLXrp6MiU-kaNCtH_ZtPQCrBd8YpFNi5FMU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت مناسب قابل سفارش هست، برای استفاده در تمامی اپلیکیشن ها و سایت ها
📹
✉️
📷
🐣
🔻
@RUSSIAPROXYY_Bot
⚠️
پشتیبانی از فردا ظهر ساعت ۱۸ تا ۲ شب پاسخگویی سئوالات و مشکلات شما میباشد
❕
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8276" target="_blank">📅 04:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8275">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رفیقا پروکسیا اختلال دارن تیم فنیم در حال درست کردنه اختلاله. کانفیگ ها اکین مشکلی ندارن  میتونین خرید بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8275" target="_blank">📅 02:18 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💎
دوستان سرور های تانل که به اینترنت بین الملل وصلتون میکنه، هیچ مشکلی ندارن و قابل سفارش هستند از ربات
🔥
@RUSSIAPROXYY_Bot
ولی سرورای مختص تلگرام فعلا درحال حاضر سرور خارجمون به مشکل خورده پروکسیا وگرنه سرور خودش اوکیه، یه مقدار طول میکشه اوکی بشه، اطلاع رسانی میکنم همینجا
❤️
✨</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8273" target="_blank">📅 21:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8271">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مجدد اختلالی بوجود اومده رو سرورای مخصوص تلگرام، منتظر باشین رفع میکنم اطلاع میدم خدمتتون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8271" target="_blank">📅 18:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8269">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad3AivOfvZMdZ53uLxQHtYRoFPtAjaR-m12lU3iOckpeR7FzXsY4D7Sz0rVc7Pt4FvfOPKf4wvDDxnCHVYKcJ9v-ASgJ6iWWyrTR6bM1nI1RWWGDvG4TE7pSPYo4F2oeV_ULuTFAoPTHHXEm0st48-MMkxisa0WwUYd8-jSQjCfNvQrbwDjUwsCzcO1d8wSvP0PVk2hFc0u41Ekd4yqi98BrlE81LNc6ct5eF9tMSzr6_I0aLiQYuYrHF79AEDNvY-g2EgQzc5qunNIhon96ixJl8s4LdKx4QrnKVaYfXDN10StS479rvUC3qc2o9tQ4NwabA8eFUTGJBa6MqbyaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز تست خدمات اینترنت 5G در کابل افغانستان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8269" target="_blank">📅 17:05 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8268">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🤖
چند ربات کاربردی تلگرام
لینک مستقیم فایل رو میدی، تو تلگرام میفرسته:
@DirectUpBot
باهاش فایل فشرده zip بسازی:
@zipyourfilesbot
در تلگرام فایلت‌ رو میفرستی یا فوروارد میکنی لینک دانلود داخلیش رو میدن بهت:
@ICESENDBOT
@catuploadbot
ارسال فایل از گیت‌هاب به تلگرام:
@GithubGitlabDownloader_bot
هوش مصنوعی تایپ سپیک:
@TypespaceBot
دانلود از یوتیوب:
@YoutubeFiler_bot
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8268" target="_blank">📅 16:05 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8266">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کارزار اتصال مجدد اینترنت بین‌المللی:
www.karzar.net/291129
شرکت کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/IranProxyV2/8266" target="_blank">📅 13:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8265">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تلگرام
در عراق رفع فیلتر شد
🔻
سازمان رسانه و ارتباطات عراق از لغو ممنوعیت فعالیت اپلیکیشن تلگرام در سراسر این کشور پس از تعهد مدیریت تلگرام به رعایت قوانین داخلی و استانداردهای نظارتی عراق خبر داد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8265" target="_blank">📅 12:04 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یکم اختلال داریم رو پروکسیا به زودی حل میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8264" target="_blank">📅 11:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8263">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💎
تخفیف فوق العاده تا اخر فردا روی تمامی پلن ها اعمال شد
✨
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید، درضمن درنظر داشته باشین که سرور هامون پرسرعت تر شدن و بهنیه تر
😁
❤</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8263" target="_blank">📅 03:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8262">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⚡️
𝗣𝘀𝗶𝗽𝗵𝗼𝗻 𝗣𝗿𝗼𝘅𝘆
Host
:
37.152.190.145
Port
:
1082
Host
:
91.222.197.45
Port
:
8001
Host
:
45.148.250.241
Port
:
8080
Host
:
85.9.104.72
Port
:
4040
Host
:
37.152.190.145
Port
:
8080
Host
:
94.101.186.25
Port
:
8080
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8262" target="_blank">📅 02:13 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8261">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f40e23bb.mp4?token=MdwfVAqP9dV7V00_TrTJ5GRZLmXnHUfOZA9bpFQCfUDhLS4qWNEQgxdxgomN8d98Xv0Cox2h6TJ_4WIvBPUV-pWK8ueK-XnAjqAj0lWpW1yQ8om8kXDr8W5N2N8ITvOhQObUDLU4hhFsNLRguzfwDvfejh08uyiM_R5BXs5_deBG9JSy5NXUPSWlLjx85TQVJ6E2oHROPbTjjL5aYD_5dVdxq6mukLINsaUylfLJw_MTXxRvyiaR_hesJtELuvc5v9Jk-eGRdh-XfI_waOjIupZNzjwpMUQv_H7EKDBWnKVekPsFEoO9uYZ-aMxWLmw1XIOOdp4lutlDfCKPuATx7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f40e23bb.mp4?token=MdwfVAqP9dV7V00_TrTJ5GRZLmXnHUfOZA9bpFQCfUDhLS4qWNEQgxdxgomN8d98Xv0Cox2h6TJ_4WIvBPUV-pWK8ueK-XnAjqAj0lWpW1yQ8om8kXDr8W5N2N8ITvOhQObUDLU4hhFsNLRguzfwDvfejh08uyiM_R5BXs5_deBG9JSy5NXUPSWlLjx85TQVJ6E2oHROPbTjjL5aYD_5dVdxq6mukLINsaUylfLJw_MTXxRvyiaR_hesJtELuvc5v9Jk-eGRdh-XfI_waOjIupZNzjwpMUQv_H7EKDBWnKVekPsFEoO9uYZ-aMxWLmw1XIOOdp4lutlDfCKPuATx7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمارو نمیدونم ولی من دیگ از تک تک اینا خستم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8261" target="_blank">📅 02:03 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8260">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga5tpbxQ5EhT_OMcPEImkIv_C1xMprGOmtXE2Ca7xuii-Zu3sh1nP5LtYWs9vnhTRZ62SCuonJfyifXT6lLM0tODSHxPzCmn7bNp5DWumxGcwXgGJU1UmsfNAQINalyTbl0XO1TP59Uajm-eubABn8HyXIYBjWh_9jcnSsNpYNz65IQIl-mFTJ5OMzE-7pyk65qEaGJjFTGqHzOeEOg1EQedaOy4UIG6jQfkgc0_kDX_NODHoCq1lkdSC3BxCRfDTzM0Mqw84Uz8AQGV9z0QXgMhm7GLQmNUE-w7lhPDE1nicSyPF92SZDjp1ylfsL4tfvpqKfImMstHbDV4SHuDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
- ایران وارد روز 64ام از قطعی اینترنت شد.
47.500 ری‌اکشن فیک:
🤩
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8260" target="_blank">📅 20:25 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8259">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Injector.ehi</div>
  <div class="tg-doc-extra">14.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8259" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ اینجکتور مناسب ایفون و اندروید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8259" target="_blank">📅 20:20 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8258">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دلم برای هدر دادن وقتم تو اکسپلور تنگ شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/IranProxyV2/8258" target="_blank">📅 20:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8257">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXober_I8zD5cCRJDb0PRFDNIqeNR_vyOhAn6AABHnsHS8hvi1mcl-e7yGuMlX_MlK72h4gCMz5pnHHLaBOeS5wtYHca9QwOmTUgF6k-PJ9ojHAXcZtitfx_Twrg32Zt0VwVh-lsXc3XmMyvQ7Gbp5J919He2GhTwrRk7YKsQEoijnfqZJIgmk1IwTEqLeUU5ZsNuwIJ6agurxs_OLAWs_Jzr4vNwiwm328_xe_kaIpVurO8VZ7L8-uUwaDCbJCGay-3HdDFokcDYI-Qs6se7cIan_IfJwAbuYYLI--bf0nzUBmYxrJYtFjSih-NNZ9hrA3nuHLy8f0yLChgjltwWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر سال ٢٠٢٢ پیش‌بینی کرده که سال ٢٠٢۶ هانتا ویروس مثل کرونا شیوع پیدا می‌کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8257" target="_blank">📅 19:50 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
