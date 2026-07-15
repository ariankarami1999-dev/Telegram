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
<img src="https://cdn5.telesco.pe/file/Ti1O9aqglQnYjMQoZM_BoWTSryUcqq8TSN88pvfwLLu2wLv3XBC4qBZEsHSbVMbR_t6X-oJx9wg2t7hsPg87y4iHgmcqoNi0gKeJQRLDAdGzHL_1WrVTlrMTWsrnnXmz6XtNjm6eSNYjO0UQ8U2CW1wvzMy0cJtHYpidDiLuvq3oL197Zb-Uc2FBW53nU2Tc3zb3NFslsdKz65ThtoJpwxS0Uk7oKKGktdBXard5v8DOdsxk6Dn8kZOR3bM_ewciWjcwTWimJWjgnUgeFyCsUP7WMproGMjfWX_LffX7MLdOR6vnBxyJ7XCKWLoPbp6FPLS2bxWoCMYDsDdYoyYOVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 574K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 18:12:16</div>
<hr>

<div class="tg-post" id="msg-100274">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB7TG1c2KCk6ZT-DVUuXCF8O4BAYCstYVr4RFfYTiv1b63iOe7LQrdZZsRTqNGSF-B1K0fGXWS-3iKUCXv92V_oHBJ-n_MQSJYM0-j90k9431uD0j3Lq6C0RhByHNaxrCI1LVyBjKXl4ng6CBvMkq8qjx1y3QtN5b-MgLF77er5sUU_kRES3JLWB-ZmUKVU5tt0mndgACJiEzkGTeCq0XWye6Yu7ybBShpcu8aJ2VanfF5Z3v5TD_1_rDFQZ4lH7yK5eMib9CkRkWgB4CDgeYbzOrV6P62t_xDL5fqB-4rL1BQDhdLxZmTxESxmwiZ4FByECEMzNAhjcdQTLHsVSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇩🇪
#فوووووری
از سانتی‌اونا: مایکل اولیسه به سران بایرن‌مونیخ اطلاع داده که قصد داره در تابستون به رئال‌مادرید ملحق بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/100274" target="_blank">📅 18:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100273">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88663297fd.mp4?token=Kby126vv3NMIz8Z3VuJtzkTmqg7GLKOEc2vO0dnbGbqj_k7JZav6enG5LvWuCwTF-1myP9DTNx3Xw-j0DnNQNxd0LiWxTRZv4_HT2W_qoJv6rEazxlunM9N0hsxE_2bjXz6F_EqK5e5Sx1KRMcxBWuMKs5YwYEb3BcZKknVlnA3kXxttp5A1FcA0Tt-2lOr5yAgqM141XoIRC6uBK_thVa5vjs_J2nZxDQVkF-UaPrXa9xKchggFX1mg35l2V_3tjRsFGIR4AjVUJI-4eAa-8XX-zKydITcRVW0wnfNcoRLoZqbO8CIS0FsgxoW8z-z_bmyPhWOBPXhWc90rb7H0ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88663297fd.mp4?token=Kby126vv3NMIz8Z3VuJtzkTmqg7GLKOEc2vO0dnbGbqj_k7JZav6enG5LvWuCwTF-1myP9DTNx3Xw-j0DnNQNxd0LiWxTRZv4_HT2W_qoJv6rEazxlunM9N0hsxE_2bjXz6F_EqK5e5Sx1KRMcxBWuMKs5YwYEb3BcZKknVlnA3kXxttp5A1FcA0Tt-2lOr5yAgqM141XoIRC6uBK_thVa5vjs_J2nZxDQVkF-UaPrXa9xKchggFX1mg35l2V_3tjRsFGIR4AjVUJI-4eAa-8XX-zKydITcRVW0wnfNcoRLoZqbO8CIS0FsgxoW8z-z_bmyPhWOBPXhWc90rb7H0ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بنده‌خدا بعد گل یامال چرا غش کرد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/100273" target="_blank">📅 18:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100271">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRnB0PV2qAvlt7o-BfpHNnyrGhdtIXu6AEBCUtfuK7YqVFYXfNuuycMpIoXexYpmMf8vjJ2UkNvnT8bBLfEq2omRkeUWqHkhRm9xA1eSH5xiOdPfHX3AnugvD-Ed5WUCwegOGzs9-111AQHGeSkyh6-DoTl3l8XkBhkBw3lYJYWUC0-796eDC9zfynHKeVkMjCi-Vxue5hz_C9njf80IntJjhcyDwAjynstMZoJfgoyK3UrRh9ZpqPTczyAz4TU-HqIBVLwg_sbQqBV6qPzMeqR3FB7IJ8o3q2hfCHxoMQipxtFlYLeHqXM59xmILRyfaZWJ1NBLe6H443XqQ0F7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADq8xaLew7pHTV5e_a8aF-3J0uT4LISWpUVVhIhc-NLdGaRTW2NEzQESQX2oHsYffdQsII9gNVA0ya3uM98hNZBc94WSAVyhMB0pOEV4AiLHVg59onMi_fjDQuwooCX1XEEGJA9m9CMBjGYxlvqEDgFRSYtcOQ1UIK7etWdIoZPBGCWQr1xFl4AvYj_Zz23FYnMeDm3d8V9dF8DHAK3Jj_YNLItky3fGVYuCwX7XYG108u4jyivCjMpIAjGe_DFJF_DXfCSj6X_w_0Ck9iWf9q3tCkA3Ci1YtpHVDCwtZ3HhF1-kx_WTPWXex0W8nc8TAxjrCSVMi74H-M0GPnIuHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
👀
رامین‌رضاییان و آقازاده بدنام ساشا سبحانی ملاقات داشتن در اروپا و احتمالا کارهای جالبی انجام دادن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/Futball180TV/100271" target="_blank">📅 17:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100270">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73bc182d48.mp4?token=OPJN_kFuh9YSj8MNy_SwHzjJJ-X7KtpQtZB83O1OQO98_bGM0PfbOq8OWvwmqnulFOrt2xpi88AW5dtFdp5PagRYYeTOmRLesbP3--3_969YD75GZzu3CiAI6xTQMtpUl1Xai-7oM0QbwqlW_W7xwqPWt8z56rLIRRjfvnOhI-7o6VtEeUUTx7zxqeHJlh2k-vWTunBst01cTEhU3Y98-UlIakZnjuT4Kvn3KOHVrDSvbYCUkc64RSHa8-EJrs0jnwkEHw5HpP0xiumrnUsKarGUk1BNsXb7cvK9W34O1Br3L6mzPTTKQE1OvF2lv6EN6LgLhCcFOSUlJDBI-8hCkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73bc182d48.mp4?token=OPJN_kFuh9YSj8MNy_SwHzjJJ-X7KtpQtZB83O1OQO98_bGM0PfbOq8OWvwmqnulFOrt2xpi88AW5dtFdp5PagRYYeTOmRLesbP3--3_969YD75GZzu3CiAI6xTQMtpUl1Xai-7oM0QbwqlW_W7xwqPWt8z56rLIRRjfvnOhI-7o6VtEeUUTx7zxqeHJlh2k-vWTunBst01cTEhU3Y98-UlIakZnjuT4Kvn3KOHVrDSvbYCUkc64RSHa8-EJrs0jnwkEHw5HpP0xiumrnUsKarGUk1BNsXb7cvK9W34O1Br3L6mzPTTKQE1OvF2lv6EN6LgLhCcFOSUlJDBI-8hCkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
😁
و اینگونه بود که دیکتاتور با قهرمانی در جام جهانی 2026 خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/Futball180TV/100270" target="_blank">📅 17:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100269">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47647cae7c.mp4?token=drbJ_-utuniPgarT2UKSMtOzPRzcZkSmt_m_YDYywxbDFgLH_97POWymkH4toCKjbstD4FVyLL0njfakxE41dsnGT7smTziM-Mx0B-EV09tfZD4AGZw_hXH6eY_cTUaPrO29XFRSmTzNsDpRwdo758mHoufXxPn0j9pr2ySe1jAGoFmBn591v9xY_Fl-zxYf8-l6cwqTH-aa4khDHRugI1wb6gFbf1nPeWcgcFQshEFNhcvr5YO2VQ5fMv802ztjfkiJtX0zZOwFqhXAAQ5n6uH4U_5Tseb8nPrsaRuUAim0zEUyQj03CCwHIiw5leY9IuzU5QyiOuMfjbeKW4jQtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47647cae7c.mp4?token=drbJ_-utuniPgarT2UKSMtOzPRzcZkSmt_m_YDYywxbDFgLH_97POWymkH4toCKjbstD4FVyLL0njfakxE41dsnGT7smTziM-Mx0B-EV09tfZD4AGZw_hXH6eY_cTUaPrO29XFRSmTzNsDpRwdo758mHoufXxPn0j9pr2ySe1jAGoFmBn591v9xY_Fl-zxYf8-l6cwqTH-aa4khDHRugI1wb6gFbf1nPeWcgcFQshEFNhcvr5YO2VQ5fMv802ztjfkiJtX0zZOwFqhXAAQ5n6uH4U_5Tseb8nPrsaRuUAim0zEUyQj03CCwHIiw5leY9IuzU5QyiOuMfjbeKW4jQtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
👀
لامین‌یامال بعد از بازی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/100269" target="_blank">📅 17:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100268">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osvymxy85DrBJwlvfbQP5DsZzBsUDBT0IGmRCBaFTL_UIwGx8MG0tVr9FplM2HgNNLG-iIuAC5Vy3AskFdp2hHzwV4m5txUEKhZnKph6ovUcnpOKNTqVJgpsydp6dARw00whaWxPiH3eyFm0N_Upol6UPJTmPULIfrBS8KpNvoHmNVGodLQzPr9o1mICtkpdYe379pH-5u1T_17ThwvSLXhVlHLRoO2YzQov6bAR8kVpefN6cFrAN4_h2VpmtIC-S1x6e_n3f4dYxhKyTGwYHBZ7G1AUf4pTYksLeVrybLA0B-PX8Q33U_LRSW77YgBp3MmXZdamni1-Tos2YdpAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
براساس گزارش اوپتا، رودری در جام‌جهانی ۷۰۵ پاس ثبت‌کرده که ۹۳ درصد موفقت‌آمیز بوده و از سال ۱۹۶۶ تا امروز هیچ‌بازیکنی چنین آمار درخشانی نداشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/100268" target="_blank">📅 17:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100267">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbRNt9REepHf-lsZD1ice8sxQ16LPSBu39g_Vz_DrlP1ZTwEE26om-6copXNbqh8XIoNE7JbsaLE40IE7IFusi_r2SgddECDAH1IYzYh8BGHyU6NdjJfh6Yh0TOCEWHXssvl2BQffCahnYoxgO1_QASX5MpOns9NdjjLyLNvCbbTq3Kys_rFfJjCsuR3eYnx24I_pL15PfY1GdKC4fPQApF6mnTbZT7WuOkHDDqHPEd2GU6DKujHHBltE71p-nXlvxEvikjL1Sy-JmixvMdW2wk7IZbJTfe1EWtXv0bt-GKdDm3aWHEy_oW66DeHdtdRn58g1O7EUxFKSCdGwrAdzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🤯
🤯
🇪🇸
هیچ بازیکنی در مراحل حذفی جام جهانی موفق نشده یک بار هم مارک کوکورلا را دریبل بزند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/100267" target="_blank">📅 17:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100266">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3d1b8rYHxKZ7K1yuUlzoRTRrdvSMmdPAzp116REoTNRBpwtQu9RaqLcFxNMJsvOLdD2-y67ITEKMkCRSHUIv27UizmJCwmbd_IM1sFm9CCw_0zXiRAU5fNRwn9IKf8HaKvKbBFPhDNqMBWSZWXkKpWw2bQCqCb8vjnfO-kqLdSrPUErZCqEn_FJ3oML12LNWNoveM7CzXmVOHsyEeOhASgiODO5RAvoGb04yWUGoeGJ9_V8FTlquzI1i5XzsiMf8iwc2lJvKpOxvM64tfa49pFo-0vppTsUUo0BlIWAnv58h5GWc2hGq3cr_d1itigqYqTZN2odm9Cjzl6W63Nn2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
هیجان فوتبال با سود کریپتو میچسبه بهت
🎁
کد تخفیف روزانه مخصوص اعضای کانال
🫵
💸
سیگنال و تحلیل دقیق از برترین تحلیلگران بازار
🔥
مهمترین اخبار مالی
تخفیف روزانه در
👇
📢
کانال ایران‌اکسچنج
⚽
📢
کانال ایران‌اکسچنج
⚽
💵
🥇
خرید و فروش بیش از ۲۰۰۰ رمزارز با تضمین بهترین نرخ بازار در ایران اکسچنج
🌐
صرافی ایران‌اکسچنج
⚽
🌐
صرافی ایران‌اکسچنج
⚽</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/100266" target="_blank">📅 17:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100265">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSDt-rgg6DdKnKsdXuBbiU7SKhlRbJmS8DwrN6mV36giBaX7CIGCY8qGTnloxK9NlBT6pGEqVeLT44FCTmqaxKioY0usXFzrRYDpCWYdFAKLpy5cYW_-pgpCCtgtvh9w8CUcT-l-Kp50HKvnL0s3-EAVY03W4FA5GBDwsIK5iQV8vs97Ax8qnahvzpNuSlH8JzSfJGyMXJaCdstXFPuYe_GfG-t6LFEwdQ6QEvTbIGm7YrxD_aCEDXd0NNH14fdjReiKiE3EnH00I_CKCpZVWDkR0NLKXyG80dSGkjQBHrNxyHbu4jil6WyEQxtIEALGjUDGxr_d-kFqXDJGMWMKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزان‌ترین بلیط برای فینال: 4,451 یورو
📈
گران‌ترین بلیط برای فینال، 188,803 یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/100265" target="_blank">📅 17:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100264">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Doz-I4-wpneOEwdJMRRpZYzm26HRb9NigQTudRsdauoHpTY7kLm09MOd3m-vRda_3KVL53EHweasdxbWGAvJyblSmSDvza2j5OtLJRtRSqoJiCWEl9rL1GQX2bQiwUGxLw6Lqa_xGVGxHN-MTs6CdHgpwQQwHGzFUTgWvNfxNeFLbJENr0txe4fNjJvU1Jfmn3qq5fARLUlhS_mgbQGkXJu3U8k77-E7noNKCxatwvWqha9AXovkgzkRGLBAdhMjQQOCwctzVvXD6DPKU1_-SQEu8txq84GsVYMI4DPDDe6qZktme43nc_szf32VtqDwayHZv1iUtHduno0ra_h4Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
توماس توخل درباره مسی:
"مسی می‌تواند در هر لحظه‌ای درخشش فوق‌العاده‌ای داشته باشد. او یک قاتل خاموش است، می‌تواند شما را نابود کند در حالی که به آرامی حرکت می‌کند."
💀
💀
💀
💀
💀
💀
💀
💀
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/Futball180TV/100264" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100263">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/100263" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/100263" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100262">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCHncXugJLCVvM5f2CICTqbTwoGNZ70_qK-v4rtrzLMvwnOfsZJlqW0k6HORLi6D3dIcV-PXVyJyFP3CLL-PtCjjciOd0OeCUn4nEIxghOY76JQXZO1ecH_1tWSsCLYix9MZ0-V34zVpjRmlNDkrL-KTBpGUQmdzOeSRdNxPY9RDWsi8MCLKkvNnbUoZZBSX49W5q5sU2LPKXoKP7GDVuk4tBSuJSt59go_h1XWfc8tnExwPYrSyfUqOehFauAsCyXYxvHozTzBVd93-5miFxXix7_DvJakXS9Ld9QVm9-evT0NkYswuEET-IC4j_Cvqq-eLsyRSzxg75loHH2rnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
Stand for Victory |
مجموع کل جایزه  250,000€
🎁
جوایز برتر:
🥈
جای دوم — 33,000€
🥉
جای سوم — 20,000€
4️⃣
جای چهارم — 10,500€
5️⃣
جای پنجم — 8,000€
🏅
جایگاه 6 تا 10 — 4,000€ هر نفر
🎖
تا جایگاه 450 جایزه دریافت می‌کنند
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
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/100262" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100261">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f95d4ebb0.mp4?token=ZVkcHrnpi44I2N0fUNES7CvKGROubADc8gfj-komC3WJx8LJWdjr3Ng9Gxsj9wjM7QzdEe-i04WdayxvLtJT0BMR0PlST31aJKU1UZMH92dXdF1p_hxLsD9e39x3VW-eiX4_rRL4tmpOWXW5ECW5HIHZ-x25iO6ku4qSdZr-nzuoJioodgdC3ns9vv2f79x5ABAuWdhnyUUWnMfb_w5h8OMYKhPS9rSB-pAsdSQOrQDugUnQoF9bggRRBOzOjGLVZm-6dohpe-wJXeH2IZIk1p8d6iUSUvLK3uv-vCo7YsStgxDbRz3tqgfxoERHIWSz1WTVtaaDzj6nVqvlt0PL2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f95d4ebb0.mp4?token=ZVkcHrnpi44I2N0fUNES7CvKGROubADc8gfj-komC3WJx8LJWdjr3Ng9Gxsj9wjM7QzdEe-i04WdayxvLtJT0BMR0PlST31aJKU1UZMH92dXdF1p_hxLsD9e39x3VW-eiX4_rRL4tmpOWXW5ECW5HIHZ-x25iO6ku4qSdZr-nzuoJioodgdC3ns9vv2f79x5ABAuWdhnyUUWnMfb_w5h8OMYKhPS9rSB-pAsdSQOrQDugUnQoF9bggRRBOzOjGLVZm-6dohpe-wJXeH2IZIk1p8d6iUSUvLK3uv-vCo7YsStgxDbRz3tqgfxoERHIWSz1WTVtaaDzj6nVqvlt0PL2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
🇦🇷
جو پشم‌ریزون هواداران آرژانتین در آمریکا پیش از بازی امشب مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/100261" target="_blank">📅 17:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100260">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa988482.mp4?token=uDZHJwIbktDFDS70v4GeRIdBPsocgpOd3d3lir0FT8KRCC5khWBAJpwprY_e-wb1vczC4tJBeR2j2mIAf9duD9As4STnfIWYIJxoKtOmuzRDiov-MfB3ERTcSF1rMETm-SvfLB7tkRJkpg3hzph-KlnM0vvUhwAq3a7sbwXHVbPC3XKZa2pZeaA5R9iODmSuVeOPGHpmv4FZuX6VFAOf2Zy6VITQa5sh6M-3fFCOCglqiT8mU-FaMBiWVKQ_d-r9N8A87huU-Uo9Jr-rgGqKq6uDRzPr9QQiX3jMO9uvXbR3B19-tr7_rH93oHZSrQJ-aW0Mem5NnOIDx6T_u_N1Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa988482.mp4?token=uDZHJwIbktDFDS70v4GeRIdBPsocgpOd3d3lir0FT8KRCC5khWBAJpwprY_e-wb1vczC4tJBeR2j2mIAf9duD9As4STnfIWYIJxoKtOmuzRDiov-MfB3ERTcSF1rMETm-SvfLB7tkRJkpg3hzph-KlnM0vvUhwAq3a7sbwXHVbPC3XKZa2pZeaA5R9iODmSuVeOPGHpmv4FZuX6VFAOf2Zy6VITQa5sh6M-3fFCOCglqiT8mU-FaMBiWVKQ_d-r9N8A87huU-Uo9Jr-rgGqKq6uDRzPr9QQiX3jMO9uvXbR3B19-tr7_rH93oHZSrQJ-aW0Mem5NnOIDx6T_u_N1Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
شادی اسپانیایی‌ها از صعود به فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/100260" target="_blank">📅 17:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100259">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFTkhTrl_N0GiKGhKaK6zwiXz15AYoAciy8vgkJSpW5zwYEXZ4CWCaPTfGbSZV200y4SfF2jJZg6REcqIe33uU-ML9ullkCnQ0UBC1ketL7HMCPpDsXOPVssHHzw0KYYQiKGrF6N_4-fVVy0QNh6EK2bq3j0Uy2Kna7ijOisZj2KjXwj2kD0fON4stI9U9JC5MwvdqOIn3Kd_-dIg_R2wMkqQKNdcCuK-MmXPhy4MjJxdR_v2IX7hnqqpd1KrOC40UMix97MVNIi_zBk8BI67mg0tK-PSp0kXmW-jJKQVlGI39-Fy4czbyEp5sDUoBYCMVBel1c6DMSwdTh1MkQBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد تیم انگلیس در مرحله حذفی مسابقات در برابر تیم‌های آمریکای جنوبی:
تعداد بازی‌ها (9)
🏟
تعداد پیروزی‌ها (4)
✔️
تعداد شکست‌ها (5)
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/100259" target="_blank">📅 16:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100258">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6602b08c.mp4?token=WTQ2vRJ5q8Bzy-CxlmqG73J_37A7HoiTCiBmSgdAXlZmJxJZYvXvrfsme7WG2kFC_6-9QA7ulruajwKNA3T9F2pzd0ExYPaqRF1H_w8Nnx1fRh5fp-PUQLrySp-0N_KWaJm6FJUrdTL1_AVKoHWwQDnzbbv9jsN7Sg3vqagl1HUurELdjRs5Fou0n8Gyw0QEOZqShbncNqV80bbBXGZ0XuwagjUoiWLDcH4yJxgfJy7kS3A55v37zZQtOw2sYxEwG1y3nV4ELePcgoPM2Ubmc6sK_m7Yh8iAZELUSOPrNFlx2EX4Qkrk_b6XivFEXFYanTmh33Fwt842CN8UlmN1fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6602b08c.mp4?token=WTQ2vRJ5q8Bzy-CxlmqG73J_37A7HoiTCiBmSgdAXlZmJxJZYvXvrfsme7WG2kFC_6-9QA7ulruajwKNA3T9F2pzd0ExYPaqRF1H_w8Nnx1fRh5fp-PUQLrySp-0N_KWaJm6FJUrdTL1_AVKoHWwQDnzbbv9jsN7Sg3vqagl1HUurELdjRs5Fou0n8Gyw0QEOZqShbncNqV80bbBXGZ0XuwagjUoiWLDcH4yJxgfJy7kS3A55v37zZQtOw2sYxEwG1y3nV4ELePcgoPM2Ubmc6sK_m7Yh8iAZELUSOPrNFlx2EX4Qkrk_b6XivFEXFYanTmh33Fwt842CN8UlmN1fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال چرا پای خوان گارسیا رو ول نمیده
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100258" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100257">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOZUcFbxkTje1Jnu5ScBGX0RU3asS6FqfnfbRPVpLVrxJ9VNzdk6c0nJqD9h9GlXnimCYr81qROhiOqK0TuBxVBv9GnkUUSWqqbX543RBtBQU2r8Bcisf82BwGALHWuCKYs3wFy342yAz_HuEcpx28xcxF3jIBf0VFs0govBzF5JlTX1dKKNiBewurRQLqjuav_oREvjPC14RwoS2P5WajhJZbRkBJGOglhcX0-_6pjhTJNiK49YzKQjevQ1UKluegKsc3z-FFW7GpXW1rOuM5Tq6Aah4RvvFKXEVyDnVNnrTv7s66ImdujhoVnFZ2XHxOh4ims0lDnLhdi7nRM_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
👀
دوس‌دختر پدری در بازی دیشب فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100257" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100256">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ac68188c.mp4?token=MZUotni5CWtQLn-t2WTxUpig3jOVXvmybskbYtonPOmsTsWPcLhvsTDsPyD91OTP4Ggc5WCHEkGRRbWHdn50Ftvu_gPxErCo33pcCts9bYNEuYS_5SHOyUygvY5zvtDCm2AUHVg3eyqQt5tlBSl1ngXLf8tcb03vAkzwz2xsduZOE_sack0O_u2seFfFTpb5YfBh3vkIwl3lfqlnjhM_0lsktuw4Yxc4bNgPDI3CmIWCWCmYR2pI1tHbF8jpJnvvg4XV8YO6SWkG4buFgdO290N8wLcUcT0cPi-7WkV4IGfxHAolMNlLHC47vxn4wrAHhJfs3Vup3UBNcbEPgYdqWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ac68188c.mp4?token=MZUotni5CWtQLn-t2WTxUpig3jOVXvmybskbYtonPOmsTsWPcLhvsTDsPyD91OTP4Ggc5WCHEkGRRbWHdn50Ftvu_gPxErCo33pcCts9bYNEuYS_5SHOyUygvY5zvtDCm2AUHVg3eyqQt5tlBSl1ngXLf8tcb03vAkzwz2xsduZOE_sack0O_u2seFfFTpb5YfBh3vkIwl3lfqlnjhM_0lsktuw4Yxc4bNgPDI3CmIWCWCmYR2pI1tHbF8jpJnvvg4XV8YO6SWkG4buFgdO290N8wLcUcT0cPi-7WkV4IGfxHAolMNlLHC47vxn4wrAHhJfs3Vup3UBNcbEPgYdqWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
درس دیشب: کری میخونی بخون ولی بلد باش مثل یامال تو زمین هم پیاده‌ش کنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/100256" target="_blank">📅 16:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100255">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYAgiISj7wykm1gH_MzuVFi7-1ZXDSgDhZGMvb4r5WcofXKHtQX0d1a9xZJA4WMKGqpPHCgCluFNBrTk9EdtpYgz1oYVlLCEkZ34bOpOFX0wsQQZx5FifMraBAWqeiZG7bdUCEEyzBa1RyvCRsU4Bhzp0RcrlK2DkWsZ0j-TdyRwqr6d1MmhTc0NRAlbo-OQNxDRQMinkwZdsl7OT5u4bzGehcfb2wpvESOAIJyJl-mwCO6IYsTWPsieiwC-RhSqPpBdFYAkQ40ET7Zf5Npt9sB4scMMMiOeI0npK8rC7wlbXJoa6LhWGDKrhBhu5WN4z8bf8ksjb2xq0y04LBUgWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
نتایج تقابل‌های تاریخ انگلیس و آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100255" target="_blank">📅 15:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100254">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a487162a.mp4?token=QgULFqt8JGynXzJIwe3QQY74rH7kcx5QUp0ZS8zMsi1zNYpPG3R-Eccq7851Jdz_FYNgfC2NNdGyG-qibVyTqcpt8c4X3gKedxBaTG4XbU74fa3BZjeZopllOhktWk5hgY8gmbricMzi4GzbSFRXE3elXyef2ShG-exhlwvXfGkmrOjBb0DSlDNbkMxTlsYfSEGpEhSlYZm8ZbhPm347A3fW-EKUzGQI41F94OMHyG6xp9bLmZnu1kTAfoYzBY8DZb0vKSFKZtJOrlaox6akhWdQvTbuwbxp9SBcZC_almvXY9vLyBwF_ItzQEJgMx74-2pj4GUM6-vXBs67LcRiEB_tFYPxfjXkBivNEwoXiXXR49QsVTch4h86U2RElz3SGnr9YfGTzW6Y1X7v7uUdCwD9YhwtYu3AE-2yicsjaMzb05Awn-792cxRv8s38f41mClKQlGlQ71-74zatCDYhi7Ppbf2SobVWcTodvRV_2qllK-96EIqa7tEWZJhQAt2yUVQ-1CvSOWGWSVzpqlXgCOCecjMEYKG3EmjCTmzlE36tEjAyw7Vp60Swmlzmvtj5LhHmNzt-8lyQnAgbeVP4qYt0WPs_0AueJZtiTqBt9KeNnrZ8AQOfLhpbXivD-OMzDRxRrEhH_3c3_V8GqEO2beI6tQEAKeUYjwsXCO84N0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a487162a.mp4?token=QgULFqt8JGynXzJIwe3QQY74rH7kcx5QUp0ZS8zMsi1zNYpPG3R-Eccq7851Jdz_FYNgfC2NNdGyG-qibVyTqcpt8c4X3gKedxBaTG4XbU74fa3BZjeZopllOhktWk5hgY8gmbricMzi4GzbSFRXE3elXyef2ShG-exhlwvXfGkmrOjBb0DSlDNbkMxTlsYfSEGpEhSlYZm8ZbhPm347A3fW-EKUzGQI41F94OMHyG6xp9bLmZnu1kTAfoYzBY8DZb0vKSFKZtJOrlaox6akhWdQvTbuwbxp9SBcZC_almvXY9vLyBwF_ItzQEJgMx74-2pj4GUM6-vXBs67LcRiEB_tFYPxfjXkBivNEwoXiXXR49QsVTch4h86U2RElz3SGnr9YfGTzW6Y1X7v7uUdCwD9YhwtYu3AE-2yicsjaMzb05Awn-792cxRv8s38f41mClKQlGlQ71-74zatCDYhi7Ppbf2SobVWcTodvRV_2qllK-96EIqa7tEWZJhQAt2yUVQ-1CvSOWGWSVzpqlXgCOCecjMEYKG3EmjCTmzlE36tEjAyw7Vp60Swmlzmvtj5LhHmNzt-8lyQnAgbeVP4qYt0WPs_0AueJZtiTqBt9KeNnrZ8AQOfLhpbXivD-OMzDRxRrEhH_3c3_V8GqEO2beI6tQEAKeUYjwsXCO84N0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
دیشب دلافوئنته بعد بازی جلو فرانسه یه حال اساسی به بازیکنان اسپانیا داد و اجازه داد که با خانواده‌هاشون پیتزا بخورن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100254" target="_blank">📅 15:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100253">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01e8f0d16.mp4?token=vD25r4rdLS65Sy6B36diV8U8Cnkx9ZdCkbc4qn3I16f_HzlKyPR16phthlQwoEXN9QInbxvSxma-HdDzPQZIpr7f5CQ3qlBMSoQ92WP_xemcWGfSWCQpg3s6iPoe9c6VqpS1SDS8JmS3l0RWh7xpJrdf5oyjdmwjS2hFPOCxpRMuszZBdfDSAb7keqX26vycSBPy3vyiv-MO4BvKJIFIhazDwoHVbeMYeWkOdiIfUBbwQ0CsR6sDYoF8JLDmxCilMjW8u-UN9OcwlAwP6OGa5LS47ByKVQdU8_vsmQUsqaSuWBTsbwHYRH2rKxEgRH13GY9U-lX0YjIr_ChszQj1UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01e8f0d16.mp4?token=vD25r4rdLS65Sy6B36diV8U8Cnkx9ZdCkbc4qn3I16f_HzlKyPR16phthlQwoEXN9QInbxvSxma-HdDzPQZIpr7f5CQ3qlBMSoQ92WP_xemcWGfSWCQpg3s6iPoe9c6VqpS1SDS8JmS3l0RWh7xpJrdf5oyjdmwjS2hFPOCxpRMuszZBdfDSAb7keqX26vycSBPy3vyiv-MO4BvKJIFIhazDwoHVbeMYeWkOdiIfUBbwQ0CsR6sDYoF8JLDmxCilMjW8u-UN9OcwlAwP6OGa5LS47ByKVQdU8_vsmQUsqaSuWBTsbwHYRH2rKxEgRH13GY9U-lX0YjIr_ChszQj1UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
💥
آندرس اینیستا: مسی برای من بهترین بازیکن دنیاست و فراتر از کلماته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100253" target="_blank">📅 15:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100252">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/062e367521.mp4?token=baNAh7LRO2YqX5f097qO7GzbPSRn9-6TEHoQKWbSlNv8QcrbutLSqIzndrQ15yfZc8gxZ45gwzisVIgH_78dJi_AoqNy1mmeo1IDtsGoVx7HorJB35s18LSU0-oiDW4kJgLLj9Icu4UJ-HvXhi-pJuASRVZZXKYAdZfNTsfe3PRggj-r4i8wHMcuxbXz70CAClHzhtePPYZImltJwPqlkkdIgVtJwCVBnKHDaDdy9jF9pl82xzERmqopg_q4htng0akzH091nZxsF0FggU-6lFye2t4D-N9FgG1JDcmpZVgC4iwGXqMY48Upvhag4Iq9nRHummnQrJLxM9X2snSvdHm4Ev4OVEth9RLmagUfJLzhplgPHIO4QFZeIW-o1yC62ka_LvR5Sp5oBe3xP5zzDg6ZWCxKoOPW9KrfjwB12-H5II_AG7L9FxM6J9Msty6b2Ggcq92NqD9Tkeqxp9qmNUZv7uzONuyu43ahhgpUCIANmaDfZMx1fA3lKV9CMmlpeaS1bqYRZS1v3ACfv6o2g3auQNBwYf-MycKCNgvTEO7grqGFDYmnV9nLZecA8nssL_1dbym3gJEN1CUAIVOrGOYED20cIKeePY2o3viVDBeS8iJo2mItrobvgFVWcW_AFGQcaTmblbdOZINw0jSO-QkLuS2VxnhnAav8KBllzB8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/062e367521.mp4?token=baNAh7LRO2YqX5f097qO7GzbPSRn9-6TEHoQKWbSlNv8QcrbutLSqIzndrQ15yfZc8gxZ45gwzisVIgH_78dJi_AoqNy1mmeo1IDtsGoVx7HorJB35s18LSU0-oiDW4kJgLLj9Icu4UJ-HvXhi-pJuASRVZZXKYAdZfNTsfe3PRggj-r4i8wHMcuxbXz70CAClHzhtePPYZImltJwPqlkkdIgVtJwCVBnKHDaDdy9jF9pl82xzERmqopg_q4htng0akzH091nZxsF0FggU-6lFye2t4D-N9FgG1JDcmpZVgC4iwGXqMY48Upvhag4Iq9nRHummnQrJLxM9X2snSvdHm4Ev4OVEth9RLmagUfJLzhplgPHIO4QFZeIW-o1yC62ka_LvR5Sp5oBe3xP5zzDg6ZWCxKoOPW9KrfjwB12-H5II_AG7L9FxM6J9Msty6b2Ggcq92NqD9Tkeqxp9qmNUZv7uzONuyu43ahhgpUCIANmaDfZMx1fA3lKV9CMmlpeaS1bqYRZS1v3ACfv6o2g3auQNBwYf-MycKCNgvTEO7grqGFDYmnV9nLZecA8nssL_1dbym3gJEN1CUAIVOrGOYED20cIKeePY2o3viVDBeS8iJo2mItrobvgFVWcW_AFGQcaTmblbdOZINw0jSO-QkLuS2VxnhnAav8KBllzB8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح داور السالوادوری بازی دیشب ببینید
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100252" target="_blank">📅 14:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100251">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7124f6be27.mp4?token=SE78JC_IZ1t23UAApnjHegOjIJiMM8kbVVN51TOdlpKj3EIHR_dFgMs7SMIQNKE2yixCDqZBaAkpukj5UdqljoW5kGbmBLUaSrTEoYWNZe6cLRol-n-YU8bMQSKt7RD0mAVptiPcPkKw0P17SCi1EsUzHImPuFHSKewAJfnxGme2pb5qUXSG0QezFhkM0tpAxg7VFORw37qDatToHNvHAsV1F3NSum7x732kCCcA6Zm2HKESNLogwJorvxDjh_XCxFu8qEvJTrCkkjGtcz5Gl4qItc5kq3cy1WN8esbi9iGUWmiC_LYpaanlMfT7IreHsJkztCvrhu9jbPzzxDdqjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7124f6be27.mp4?token=SE78JC_IZ1t23UAApnjHegOjIJiMM8kbVVN51TOdlpKj3EIHR_dFgMs7SMIQNKE2yixCDqZBaAkpukj5UdqljoW5kGbmBLUaSrTEoYWNZe6cLRol-n-YU8bMQSKt7RD0mAVptiPcPkKw0P17SCi1EsUzHImPuFHSKewAJfnxGme2pb5qUXSG0QezFhkM0tpAxg7VFORw37qDatToHNvHAsV1F3NSum7x732kCCcA6Zm2HKESNLogwJorvxDjh_XCxFu8qEvJTrCkkjGtcz5Gl4qItc5kq3cy1WN8esbi9iGUWmiC_LYpaanlMfT7IreHsJkztCvrhu9jbPzzxDdqjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇫🇷
ویدیو لو رفته از رختکن تیم‌ملی فرانسه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100251" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100250">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlYFBxLoyZQh4He_pSvO_vx3vQeoCgF50FNzJzGr7pTnJEp09zHB1biAoD3XEuTLUz-Xv5bTfHlKAdvWd9dlQds42YBmoKFnvGtWoYKPBoaYHunyyEh-Fl8WJsc5MX8pxka2j4W_eIwZQJttNLCH2HsyWl4rYGfrUoA47LognM9i1VJ801VzzUmhPxYbVLpWxvVktWUFmfMG_fbpE0bpm1svrmEa9eUXTuznWewgyvcqEaFZcWtrVWyu0KjLQ7GTeAJnHZZHJw45o-NXyoNGXuLxf4icvp6oyvoDb0PNIaDmgJanM_pZdGrtKgFnEIw9-pKUIkQ9f63KGDdZwKZDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدین شکل
☠
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100250" target="_blank">📅 14:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100249">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea564e6cb.mp4?token=ZbJwMQThJrEWG5kelL_9lsVkT_kc4RmvjZsOC3kcxME_Rx_npm4H946d1X66b9WH-lhTABvnyOwjfoBbWN8bGEZtaEu7-JZYPxj_wMEyqzwUYQOR-yMnrNT_6JV5eXAO-Of7qGuIN20A1h-mwoLjJsDxbvex17z8Epp5qEdzXY9TkZxuX_TrFodMxSKQVY8jPqDpgE_Y_mydQYrTMRgBFHeS7JLyKd_f0Apgo2HDSg8iXkbAFaJqVsAjx5qbPYGXbajAy1cVlqqRGX7jLDVtdz7r8ljzw02TOWaVlDFvAsHLGt7IlfofIYp_C_DlVsivLFD8qhDyRPYe2up6I77rkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea564e6cb.mp4?token=ZbJwMQThJrEWG5kelL_9lsVkT_kc4RmvjZsOC3kcxME_Rx_npm4H946d1X66b9WH-lhTABvnyOwjfoBbWN8bGEZtaEu7-JZYPxj_wMEyqzwUYQOR-yMnrNT_6JV5eXAO-Of7qGuIN20A1h-mwoLjJsDxbvex17z8Epp5qEdzXY9TkZxuX_TrFodMxSKQVY8jPqDpgE_Y_mydQYrTMRgBFHeS7JLyKd_f0Apgo2HDSg8iXkbAFaJqVsAjx5qbPYGXbajAy1cVlqqRGX7jLDVtdz7r8ljzw02TOWaVlDFvAsHLGt7IlfofIYp_C_DlVsivLFD8qhDyRPYe2up6I77rkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تیکی‌تاکا ناب اسپانیا مقابل ستارگان فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100249" target="_blank">📅 14:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100248">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdavPxt7205WQGyZyaQu1v8aoJKlr8yoRlQy4lM_CkxYoTK9eZaS3EEiEztMxSKN_dkywpoT6mDo-Q9yktc_7OX-ewgkbhF9d4aoswLKcOLkfOBsFcuiax1EMGiTQvmyxS0xDiH0na8Ei6peM11HIpau-o9NF5CGg5Dyo77TLpL9QmXSezoHez-Veuo9W0nHwS5k-940gI_lrzciVEwYZvDQG-BIKGfyfB5Ag32lwRmCi2bIaPoyVOfpLOKajqcGio3cTs--6BvmbApESdaTzrVPxdMzaYwMhz6EP_dV0L_I8hXBN1irLcfVknzZ31TJGe-IltrFGExNV2CEiNr3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
با صعود به فینال جام‌جهانی، اسپانیا با عبور از فرانسه صدرنشین رنکینگ فیفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100248" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100247">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LON6AAr71d9ZD7QZMMbmhhfEzjjYReQwDVcXi7LgEwXRzZDdPz_Mhmy8qzcNeiLDuLQpVwORTCqrfmDTN6PsyiPNGTW_O5LKc0kkvCKKQ0JGzzfBjgU9Uu9SS-K94SowxgcE8PHvZBWReZ6wRQ_Qjav7R3Lj_fatkoa32bTh72_VsnRjcMsXV21i3PXDFjHpDSvByurF69206OTDi7kIc8SB7rGypex7MMDaPxNgi6dkwyQNfHGN49b5evIxby6CXqQoo_vi4BBm_N8Buy87MNqErHEyQXh64AEUDgEp1VPwhk9uS9PXMRb9eySOQobFsPfGcsIDrArZR48umRc2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میانگین تعداد گل‌های مورد انتظار برای تیم‌هایی که در جام جهانی 2026 با اسپانیا دیدار کردند:
🇨🇻
•
کیپ ورد (0.20)
🇸🇦
• عربستان سعودی (0.14)
🇺🇾
• اروگوئه (0.20)
🇦🇹
• اتریش (0.32)
🇵🇹
• پرتغال (0.63)
🇧🇪
• بلژیک (0.34)
🇫🇷
• فرانسه (0.31)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100247" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100246">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7bbd3518d.mp4?token=q5YZUlMTcy7QhXWfgIi7vWEZa9J5m26DhXYkFlGEq4IK7eGnb_Mvexo_ygbMqGtJzu3fyuPjJveA0iIhxmhpmbCv4WvyL9X1fZKE0-7xYkKPg8aD4hyvWjd9Nfslr7NflsxaNb8YGsscl3d2E8BZxD5-pIv5GfaubE51R0jmLicVxXThQ3PIix1i46LKNKvuGjJYEn85s2xb95fBtB1ApOuvnCYn2KDu3MdySqv_BJVwZbEU2S0_1vlxaE7beXl4r-ESvD4XsXpia-y7Nz3notd0PLlQ6PX2NkgOSYTmXuovZETBT3blnpi_XD7JODCfllqY-QTBLDBWUN6Gh61pdUV7VMiUu2K1DfTyEP8kMDhRFIJQwzor9xda_21A152n9gvnY9JO0uOpDiZF9mJZPk5cwMXygu7HqgOhi3RlW-4APopLFEUrHfNRCjrgIoFYZxEKGzP5Z8VSFpq07m2glqVpUDgpF75_XVdr5wb_cYU4vQREtnvFnKpIHQxd8wGF5X75NE1dq-D8XIwgUudSdq5kx7NCovPqNJT1pbFJMkuJjAQazoT01dCwRKCO6IEfruWAwiOmePap1TEvEY2U6ZQi_V90Jxos22lTfxjdAhgXrP_ek--CBZo3h3vAn3oo26KWbpY6Pp_gMvwwnKaGJexLyKVL81Le-n5NsAGO9Qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7bbd3518d.mp4?token=q5YZUlMTcy7QhXWfgIi7vWEZa9J5m26DhXYkFlGEq4IK7eGnb_Mvexo_ygbMqGtJzu3fyuPjJveA0iIhxmhpmbCv4WvyL9X1fZKE0-7xYkKPg8aD4hyvWjd9Nfslr7NflsxaNb8YGsscl3d2E8BZxD5-pIv5GfaubE51R0jmLicVxXThQ3PIix1i46LKNKvuGjJYEn85s2xb95fBtB1ApOuvnCYn2KDu3MdySqv_BJVwZbEU2S0_1vlxaE7beXl4r-ESvD4XsXpia-y7Nz3notd0PLlQ6PX2NkgOSYTmXuovZETBT3blnpi_XD7JODCfllqY-QTBLDBWUN6Gh61pdUV7VMiUu2K1DfTyEP8kMDhRFIJQwzor9xda_21A152n9gvnY9JO0uOpDiZF9mJZPk5cwMXygu7HqgOhi3RlW-4APopLFEUrHfNRCjrgIoFYZxEKGzP5Z8VSFpq07m2glqVpUDgpF75_XVdr5wb_cYU4vQREtnvFnKpIHQxd8wGF5X75NE1dq-D8XIwgUudSdq5kx7NCovPqNJT1pbFJMkuJjAQazoT01dCwRKCO6IEfruWAwiOmePap1TEvEY2U6ZQi_V90Jxos22lTfxjdAhgXrP_ek--CBZo3h3vAn3oo26KWbpY6Pp_gMvwwnKaGJexLyKVL81Le-n5NsAGO9Qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
کسخل‌بازیای اسپید تو بازی دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100246" target="_blank">📅 13:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100245">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b90102af4.mp4?token=qKAg9yXAwUTO6jFEf911--yBKcSLiIOoFFblKMAfY1ZjSJcXuMoV4K-jByFecIaiHx-mmrnR8q15wnICYuM1XcTG5YP4QDJmhAkmB_N3uRPtykvwHK6EVPNGWbEc7DVSB0WjlumBM286v5EDqS1ARMbxyfvZbwyJiG-GGiPZwwgMuNG_RNFlS4CROfTPwO-nbJtZjGpJ3BK_EkD4A5ohcsuoDIdX_bbMwetWU9kGzXmY0K6gDREaYEPE_trU_omaR64lPCfacYcfKs6vP1TGGqCEXD4Y-VVSVx4gwD3gTVNWeWs1yFnFaxsCwDntrEcPlJw87cOCP2NVVL2y_dcLkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b90102af4.mp4?token=qKAg9yXAwUTO6jFEf911--yBKcSLiIOoFFblKMAfY1ZjSJcXuMoV4K-jByFecIaiHx-mmrnR8q15wnICYuM1XcTG5YP4QDJmhAkmB_N3uRPtykvwHK6EVPNGWbEc7DVSB0WjlumBM286v5EDqS1ARMbxyfvZbwyJiG-GGiPZwwgMuNG_RNFlS4CROfTPwO-nbJtZjGpJ3BK_EkD4A5ohcsuoDIdX_bbMwetWU9kGzXmY0K6gDREaYEPE_trU_omaR64lPCfacYcfKs6vP1TGGqCEXD4Y-VVSVx4gwD3gTVNWeWs1yFnFaxsCwDntrEcPlJw87cOCP2NVVL2y_dcLkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
کیلیان امباپه که دیشب جهت پنالتی اویارزابال رو‌ به درستی نشون گلرشون داد هرچند اینقدر شوت خوبی زد که در نهایت توپ گل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100245" target="_blank">📅 13:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100244">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBZPO2SE4N3Pv3EWqh0RfoEkGh3Zj_QRFUSoXcZyObydcat95WV5P5ppWTwg3mpGL4IgyPix9eNsyI3Rgr4793UPj91hpDlIzDGglyuiBX0gih6EyRo566jSOVkkOMbZ46EfNgKCZsJMpQt-FfWKQG5rdOVIvGdJzOJ9BOkrLX7fXs3rs9REtApLM4yIEOymzsNacJc2gUt22T2fgxE6o-radTRbhUqPCFvK-06--ZoRy4HVWbKuqOWyxKloSE09912NmkFr59uqhtGLHaj-ZFX6EC0SSX7c6WHjqV2YFOfbvlfLR4aPOaNyvY1hvgU4gsYhtXR8pZEmnlVkb_Xr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌟
امروز، اولین بازی لیونل مسی در مقابل تیم ملی انگلیس خواهد بود.
📊
در لیگ قهرمانان اروپا، مسی 36 بار با تیم‌های انگلیسی بازی کرده است و در 33 گل نقش داشته (27 گل و 6 پاس گل)، که این رکورد، بالاترین تعداد گل‌های زده شده توسط یک بازیکن در برابر تیم‌های یک کشور خاص است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100244" target="_blank">📅 13:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100243">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJIyBKTRJCyR8pvMNLpU09yH26qOtRW69r2yNDjTo9TY_BWfdJzsbpalM5B36mmA6zFrtMES2-ffZGrq1rEmBQMAQDRjhh9zWBU1JliCBkwEQDwQ1Dor1o1F4mNRA9SZMmoCre-S0nfKzw7JyG6rf3JvWLb_A3oNUqXDyp4yZsswzYCaZvjdsbOJ3cs5yv-mmxX9MtI8AOTTHRVx-JZTBlhR7_tH0EhepDcBdLnw_28bUVi4IMQEwQgKSs7Eqaf9PrInlD0oqdmQQvFphrw2yC07yzaAf2pgHcs5lsoiZaMmjaSnaQqlqueyn_Js5TVrYN_vCxGvVN-wnEuFa_Fpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
وضعیت جسمانی شزنی تریاکی در شروع تمرینات پیش‌فصل بارسلونا
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100243" target="_blank">📅 13:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100242">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1e7076d2.mp4?token=q0yVHsSmOmMv9Vrcvi4P-3gQgW0M4wixY7W9zn4tiXet06zwna7KT5BFH0gzVIS0uq_LHFNdbznv4-Qa6Oy_jDux4sS2aM1zQPw-uCal50ZOjzneY3p-RGcX4CB2XkoqR6IZkT7R3XxSLtAzJ18FdS0r93gXCL5uxgpogHT_6HQpKyy143f1I4YIvipK0kz397hbdcvlEWvGAHJ_l7AlIq490QaM8gNEs6xXMY8Xw9WGEWS9rLUN_KIuUJOIFTcQSmo_8ZMzeJSJWXxw43iswRpanCE1q44NPfWKxwbrf67sdZxn0YBKaKhGvMC9LIa-H6KPDZitopWvpyHwz7z4GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1e7076d2.mp4?token=q0yVHsSmOmMv9Vrcvi4P-3gQgW0M4wixY7W9zn4tiXet06zwna7KT5BFH0gzVIS0uq_LHFNdbznv4-Qa6Oy_jDux4sS2aM1zQPw-uCal50ZOjzneY3p-RGcX4CB2XkoqR6IZkT7R3XxSLtAzJ18FdS0r93gXCL5uxgpogHT_6HQpKyy143f1I4YIvipK0kz397hbdcvlEWvGAHJ_l7AlIq490QaM8gNEs6xXMY8Xw9WGEWS9rLUN_KIuUJOIFTcQSmo_8ZMzeJSJWXxw43iswRpanCE1q44NPfWKxwbrf67sdZxn0YBKaKhGvMC9LIa-H6KPDZitopWvpyHwz7z4GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇦🇷
تصاویری از لیونل‌مسی در آخرین تمرین آرژانتین که حسابی خلوت کرده و فکر میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100242" target="_blank">📅 13:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100241">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
⭕️
🔴
#شایعات
؛ باشگاه تراکتور با یاسر‌آسانی به توافق اولیه دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100241" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100238">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqHKHjxEhSo_PdgdXauL8zDH7kE7IzNf3zdbhqGLIa8Mpvn2aJ3FPd_xAiSSIkqhWf1t6d_S1pHLzRJKAjdV-0JAHRn94tpbrnqQ6H-QPxiGoG5VPUNrTZSjRnRGeSTz8mB1xmL-I5y37TjZ2MHO5WDroCiiWJdENrnqeW0x5gtd8VOORBeGf9G7EiczgmLX38pfFNZnEbx5ITAadHb9i4g7sNPMLYH7HYwXCeRQwxNPKU1BITs_XPZezp-ygZn0DwY_qFfDJfXaJk1IaP7VMyhAukWuseMVGoGWg_EiTdirZLRNe4v7CoWyi5rVSe4NKAssNsLXKuJfWOAq8Y3FsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flqFFFytp8RgYGp8PcK11xNL68nULIbh_VUQ4ZoIBhZPAPj012m9Y8TkyVUGq7QcA7GrlOc3CZF2De5YnN8o4jilLnoN-0bDxEb7vFqb7s2eqowYizYADsKhqSelRB00PoOmVJLhQ5RsfWx0QVw7h_zOldo4r-DVjxJhGNyOBen-V_Iz5FPdJV1llMpz1-4oECSHtqXpJVlcGBKTFitszDb_8wibqS24vnKOchNx7gzYFUgscKGN1oZKQ8lkuAAs-7Fag1Jn5BCc5L8LAGb7CmAULX4BE7o11QAz1ZxSb2tIN6sBnD1I0bYNQWMBBzhgNsktqvlAgFxTnpEQIxR88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Imp5Y6_NlUHcUsoM73Fj45qeMVtZTsDcGdUzgEjsBf7CuUiuonRtHd1VHoxEYRCPh0RS9HECMJ8jn389hTZzFPHuqzgh1EpLCCj7jolVawlNW8_FKVSMjIc2y6gbj53n82yVt8dtaIe8tX6VPgnYZQE41Pz6nl9tXwIMpxtgqMJ2k5AuAyrnPZfAVFF8fgO4fUX7zelXfMKv0bJKBFb23UEEWkgs7kKT6LioiBt408KmR1Nx9R-Ws__Q4PtGWfXS_19TZr6eDb0iE-e1gSYvmts69-seb7xmVi_ba_yHyEFNdVV1WTic9SOP4YLEmMjhB47XUX_1hutesZnQsmwqtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
لامین‌یامال و زیدش بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100238" target="_blank">📅 12:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100237">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhrhake-fzdGrrdPykxfUh2Eotclq0IOV_q9XaiCmejQKtqOX5jIYucu5P_PN88zlH90-gzyQJ6wgJg_XRLoQXiz9P0j9ooojiZjtto7AD75UYgK9v5GZgQLCHgTA0wrUgDU88woQ2YqLkkH6M6XSoucGGIkrfEOnUoX09sn7fjfhBliXQSaDiIWPXlRsyQ8rAuv4NTwgOPYG91Gx7aznDnPQGtKo34DAqW2Jq-MPcc80ESXsaw0lyRxbvEsIjrNus9u1_LKzpT8hrcOHU76FQoUZrfAxKR9ormc45FcUUf4cH6TfE2acxXN0aWpq78tgUF7RDvKOKq_V6EQN_-FhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
هواداران بارسلونا حاضرن چند سال کمتر عمر کنن ولی این قاب رو فینال جام‌جهانی ببینن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100237" target="_blank">📅 12:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100236">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab89c95bfc.mp4?token=n5VVGuaONjbm2WulrINKrbK7WxinJsw50SBrK6W5xJDkJ5yJK2LZ5YECyNxy2LyQRfnyB2ZFwWKb798GUnV5t-heD3UPcIxg0jCXzRuLt7twP0n9EyT23RAVNLqyv31dZl-2I1h17DY7sdCbqyj69azgpI52wxVHeBDKbS1rslXbVgEYqRhy4drHMzVNekPHZe-JhKHlasL2R4_Oym3lQtkrZDSVDAY4Eh1gNywjvkDJPbSRz5smrEpDmpxzC7yZi2wdzsV-QND0xsBAoEW8cZkJt-JRocIYIci6IH1ybZ_bWxHvCFtTSYIEmAZbJ6aEwjPFl-f3KOVxmsZmPAVxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab89c95bfc.mp4?token=n5VVGuaONjbm2WulrINKrbK7WxinJsw50SBrK6W5xJDkJ5yJK2LZ5YECyNxy2LyQRfnyB2ZFwWKb798GUnV5t-heD3UPcIxg0jCXzRuLt7twP0n9EyT23RAVNLqyv31dZl-2I1h17DY7sdCbqyj69azgpI52wxVHeBDKbS1rslXbVgEYqRhy4drHMzVNekPHZe-JhKHlasL2R4_Oym3lQtkrZDSVDAY4Eh1gNywjvkDJPbSRz5smrEpDmpxzC7yZi2wdzsV-QND0xsBAoEW8cZkJt-JRocIYIci6IH1ybZ_bWxHvCFtTSYIEmAZbJ6aEwjPFl-f3KOVxmsZmPAVxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
در تاریخ بنویسید؛ جنوب فقط یک جغرافیا نیست، جنوب، نام صبوری این سرزمین است که بی هیاهو، سالهاست ایستاده است …
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100236" target="_blank">📅 12:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100235">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a0b012ed0.mp4?token=jGAyTD9axPrCQzGUWTHXQj-oDEUb-2lsy7y5nxrcFz8qeY2LsuM9lvtXgnHiW4CS66NYHBOlzLXHQO50tiFu-TGuGSkD3nWQ3JwKIpAvENTk6OA2SIfTCFI6sNybxOv8QwUQbCL3HYW6jfbjCt5zHMJGSzDAKW16NF01fAuTa_Mwh_mCVB13wl7RF57DhfzfScQ8oRvu6xdlADb_R-bnMBBaxt7JiWuyoeSJyGiF4Wz9ktYeV1I1hRwoOD_4kofXu2HOsMen9hiQAji6pC1TaaSfUqW_LxZUAPHKAd1p5IhpM80sWMpBmWaxGwDRv_pIk9G6ITe_ozyCMv1yFiPDiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a0b012ed0.mp4?token=jGAyTD9axPrCQzGUWTHXQj-oDEUb-2lsy7y5nxrcFz8qeY2LsuM9lvtXgnHiW4CS66NYHBOlzLXHQO50tiFu-TGuGSkD3nWQ3JwKIpAvENTk6OA2SIfTCFI6sNybxOv8QwUQbCL3HYW6jfbjCt5zHMJGSzDAKW16NF01fAuTa_Mwh_mCVB13wl7RF57DhfzfScQ8oRvu6xdlADb_R-bnMBBaxt7JiWuyoeSJyGiF4Wz9ktYeV1I1hRwoOD_4kofXu2HOsMen9hiQAji6pC1TaaSfUqW_LxZUAPHKAd1p5IhpM80sWMpBmWaxGwDRv_pIk9G6ITe_ozyCMv1yFiPDiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
رختکن تیم‌ملی اسپانیا بعد برد دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100235" target="_blank">📅 12:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100234">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG7MEHThpbuCsSayw_BGiR4gsf90o5WtKPG3REJHI2QR3kjAghM8QvjwVulF30QvO-DZz9GjNozXujcFL99HdUkXYxMiwM7IofY6DyapwnePJ7s8WFa1xqLJV78Lim2_2YF89VW0WrVZDorX78k7tRtIpj9EwppM2ojKWujeDzwjjLtp8QipAsv8puMJyuzjfQczdnZVwKDr7sskPz51ygyamjKjs12mgXuc6Pzn9gdgEtfECwk0mph6NjNSecPOLUnT0DweJnmKq9AITjBINK_-k-A93OMwD42wG8v9l9cjPlyARZ3aipzsdkWKBdwtHsKO4xkZi37mKi28Qbuqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فوووووری
: دیشب حین بازی منزل لامین‌یامال مورد سرقت گرفته که با تلاش نیروهای امنیتی اسپانیا فرد سارق دستگیر شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100234" target="_blank">📅 12:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100233">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2632f7587b.mp4?token=TgSkSB82Q3sjQsuKl5uF_AB_NWrsUKP84hKufncvQWNj1iIIohLqYZpmkCAI4qegjgoSfJ82gBuKptzWNmBcXo3c5ClURg3mDC3hvm1Q4TCXaUID40VSIA-mJRE82w3nfBEdM_rW_Su9_SW3oIWPrTflXELXgN7nzAu9bUqx2GGn_gpMH2nPE8ET7CIdFg3bkWMoPu6jBgfSgP6I2Hyp3-FrIrj3wciHpGbelqgkS7q6ENhRuZ_TgJdp0Z0Fe_nlYN7igK2_xDTpj64FUFCiU6e0WSrbZky3_CSCOFbbDa7rZ8X9KRS-wwVkC59VLxHOGZ551quNa5DtZxA3nAeTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2632f7587b.mp4?token=TgSkSB82Q3sjQsuKl5uF_AB_NWrsUKP84hKufncvQWNj1iIIohLqYZpmkCAI4qegjgoSfJ82gBuKptzWNmBcXo3c5ClURg3mDC3hvm1Q4TCXaUID40VSIA-mJRE82w3nfBEdM_rW_Su9_SW3oIWPrTflXELXgN7nzAu9bUqx2GGn_gpMH2nPE8ET7CIdFg3bkWMoPu6jBgfSgP6I2Hyp3-FrIrj3wciHpGbelqgkS7q6ENhRuZ_TgJdp0Z0Fe_nlYN7igK2_xDTpj64FUFCiU6e0WSrbZky3_CSCOFbbDa7rZ8X9KRS-wwVkC59VLxHOGZ551quNa5DtZxA3nAeTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
شغل جدیدی که یامال در جام‌جهانی پیدا کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100233" target="_blank">📅 12:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100232">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94662b4748.mp4?token=jz3XETgzJpkAcUtMD6aC8iZ7b8MVHBwKrFhUuQW334FWLmBazAUDJqh4-xbhSN3qGnrZX77HARt0vXnirD-sM9f2GMvzPxKZn2PxfbTpV0o3lVXgFiFjTjxStbqp-aw1SFSgwZ-UlQ1jhWO6r8KglCy56rAp94vSE5cBqZ43S1DL0QOspnv4L9xzftZYq_kTBalCYBhBLaC-g4yOf6gDLe19Hp_g3DNRQ4hhKw0RXQopuW0OiuJKuW3QH6KCTxZEER7yKN_8V1wTgc9Cjna6Yp8ne1i5iHtr0oFRHoFUAo2f9lyNB3giIEF-TivfU2I7-kCUBC29-_4zVc7SipN88w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94662b4748.mp4?token=jz3XETgzJpkAcUtMD6aC8iZ7b8MVHBwKrFhUuQW334FWLmBazAUDJqh4-xbhSN3qGnrZX77HARt0vXnirD-sM9f2GMvzPxKZn2PxfbTpV0o3lVXgFiFjTjxStbqp-aw1SFSgwZ-UlQ1jhWO6r8KglCy56rAp94vSE5cBqZ43S1DL0QOspnv4L9xzftZYq_kTBalCYBhBLaC-g4yOf6gDLe19Hp_g3DNRQ4hhKw0RXQopuW0OiuJKuW3QH6KCTxZEER7yKN_8V1wTgc9Cjna6Yp8ne1i5iHtr0oFRHoFUAo2f9lyNB3giIEF-TivfU2I7-kCUBC29-_4zVc7SipN88w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اووووعههه رو برا عمو ها بخونین
💔
😃
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/100232" target="_blank">📅 11:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100231">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9efva1-oXbSxBAYJuO_aNZSXEN5D1F7osJd-FWOMcLfiHiLvVturWve140VmCVWZxYXEFtSKIb66s2ESdeu0N992bPwnD6rgNbL6mlpKwqPeJUOOxY28Sa9Y0hOXKdqDrjpWFTFyiHIQB0PTv85u2T5j_UY4nhIe72nrx7-ZurefDJYaQIr5vk7AmAHx6CH93f61PulS6Yhg6htLVQkDIhycXggozgmVBw4A9jCN5sg_t8qAoIJcps0vYHTYYrpqJcmQ9lUK3xy7IsKa12qMfv7ssLERkuJJlKYbU9q1z_HaGaQRuA7ZpcBkHXHIfOFvhSCRlAgnSx15Cbp9KIrjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تنها سه‌مدافع در جام‌جهانی بیشتر از دو گل به ثمر رسانده‌اند:
🇮🇷
•
رامين رضاییان
🇨🇴
•
دنيل مونيوز
🇪🇸
•
پدرو بورو
🆕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100231" target="_blank">📅 11:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100230">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb46db2d6.mp4?token=D8_QrFHB7v5xf_hNrOVvsvTK6SGIQNDKsZPNHedqrxIXZZKnMq_f5LFLIRDqJNTNW-db_Oq-3WHnPThJ10Nt4aGlLTGva9dAbbMB-DyPQ95wK2aMxzT2plgKuYKfJA9aqokqNLslviChb9mDqs7hrjG6zZ4XC7TeaJW3HLwwZC47BpqD3Qysndqf4jQ6lPjoyOmfqry0AlyG7p-Js7lHdtU-54PVdqi7fhdisvtxLM1SyUt1m-PMnMIUOboL9OYV_LUPEd1Gb6tl1JhYKuDdsDgWNJtEv5CTcH6NdkK9qVkU-4LYkogASVVlBqiJ1EZFvFfHTKVNNNWjo3WxzLnc_rk1RDibx0-aIti7uZfirEfHOhi6XeYKXb0v1LhFPPaxBQ10pf3oUNUDdZ0SdybZDqZHqTEPO9cvGfakiQHW4OJcFmbhRNvZduHDsyhDQU1x0mej3i5CrUrv_98iweXvbM3jzeGWKRfDlh6bzIcc2IdcZ0-Vv0IaZxN3mlJiasOSOzsiuh4iwIHIS1Hmngds6hAJq6Vb7JIykxijfi3LnfBtupuW7Z8-sYkby0pVlZHiEWXKlWfotEjceOQ1zyyDFa3yzahQ2zvAkKGM4yQz7S9kx9_fEjli3wkoh1Khumjm0H-qb00eic_gaCu83p5P0AWluN1xrbMoma_WS4wtR6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb46db2d6.mp4?token=D8_QrFHB7v5xf_hNrOVvsvTK6SGIQNDKsZPNHedqrxIXZZKnMq_f5LFLIRDqJNTNW-db_Oq-3WHnPThJ10Nt4aGlLTGva9dAbbMB-DyPQ95wK2aMxzT2plgKuYKfJA9aqokqNLslviChb9mDqs7hrjG6zZ4XC7TeaJW3HLwwZC47BpqD3Qysndqf4jQ6lPjoyOmfqry0AlyG7p-Js7lHdtU-54PVdqi7fhdisvtxLM1SyUt1m-PMnMIUOboL9OYV_LUPEd1Gb6tl1JhYKuDdsDgWNJtEv5CTcH6NdkK9qVkU-4LYkogASVVlBqiJ1EZFvFfHTKVNNNWjo3WxzLnc_rk1RDibx0-aIti7uZfirEfHOhi6XeYKXb0v1LhFPPaxBQ10pf3oUNUDdZ0SdybZDqZHqTEPO9cvGfakiQHW4OJcFmbhRNvZduHDsyhDQU1x0mej3i5CrUrv_98iweXvbM3jzeGWKRfDlh6bzIcc2IdcZ0-Vv0IaZxN3mlJiasOSOzsiuh4iwIHIS1Hmngds6hAJq6Vb7JIykxijfi3LnfBtupuW7Z8-sYkby0pVlZHiEWXKlWfotEjceOQ1zyyDFa3yzahQ2zvAkKGM4yQz7S9kx9_fEjli3wkoh1Khumjm0H-qb00eic_gaCu83p5P0AWluN1xrbMoma_WS4wtR6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تنها چند‌ساعت تا نبرد خونین آرژانتین و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100230" target="_blank">📅 11:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100229">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nitR7Lef4EmGLJfrOcpAA3EJSQAQ96MNjusYZz0QJuszqBHKy0NhIE51wT0y6B9-wsKr53ZQGff6flMqresbGKVuwxqPI6bk_dA7TxHkbQmI9dvyg99fdUpD3PCbiikZ9dWO0wR0bwt2MD7ygCTQ007FJ1XBRWdJrfaLgnvos0prde70o-S366rS5H2Pu_YPtTzp79DS4LEwtdpUkop0SvOjTSwOqqZouolaZpnJIisln3v0ubaoTzOPgucLO5yyxaCQWFznMXMBXxepUXzsDNApbA8Rl70PZ5BZPRi5R-6J3M23fc_b05BLUppJYVGZolLFOjL-XcGRiLV0y6kIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملاقات مارک کوکوریا با کارلوس پویول در پایان بازی با فرانسه.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100229" target="_blank">📅 11:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100228">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e3ee053f.mp4?token=MRr3DzwLGMMrRN7aVNhhuwMbFx4rtr_nAfR0mVHJ0Xb3Sdodsko2tROGnbK4lH742AgA7elbIzk3CNtV-YjNgzGsFZyO16WgMcIRFb5xY_9fldzkj5P2TJygLRPB0qnFQWa4nZFBB34I00pWWA0-bz8Wz8U-8qmzyRiiV2b6i_SSMh7q6cScGnHT7v5sc__odtNur326PZ0rfjk2W3Lv1Ma7PAPmimQfF3vns7zQ_-Gg4Hh5Td0KKvM2Gg_9iC7SIKoOpkQLF1eBpB0qWhRGbvCgmtiWKE7a0YugymbRJGQw-Iq98DqZsPu0mU3XyuKbBZA8YyjGexGMFYUFR_rh7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e3ee053f.mp4?token=MRr3DzwLGMMrRN7aVNhhuwMbFx4rtr_nAfR0mVHJ0Xb3Sdodsko2tROGnbK4lH742AgA7elbIzk3CNtV-YjNgzGsFZyO16WgMcIRFb5xY_9fldzkj5P2TJygLRPB0qnFQWa4nZFBB34I00pWWA0-bz8Wz8U-8qmzyRiiV2b6i_SSMh7q6cScGnHT7v5sc__odtNur326PZ0rfjk2W3Lv1Ma7PAPmimQfF3vns7zQ_-Gg4Hh5Td0KKvM2Gg_9iC7SIKoOpkQLF1eBpB0qWhRGbvCgmtiWKE7a0YugymbRJGQw-Iq98DqZsPu0mU3XyuKbBZA8YyjGexGMFYUFR_rh7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری سمی امی‌مارتینز از آشپز‌های آرژانتین که درحال پخت‌غذا در اردوی این کشور هستن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100228" target="_blank">📅 11:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100227">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmvUMjv12uQJdMs_G0I6eJSEBNV3StcbRyWnvltpjuVmHdnvveqwh0O-p1KiKfmARV_V1azppzmr8RNHT9-Nv7QszmxHtM4ukBz3HFkDdRQyjloSXvpnWtr5aDl7GhrM4ozG4DcN4OoMjK-ORe6V9bA7d_KO_a-xB-4TR4gz80exGpirUVQIINJjjLcT7kZFmiztH_ZIs-LbFhbSjdiFyABd7WwSje2HDecu8M1Lznk-ekHf-Qz1MF_H2-llN4NLoapXPsxBeN6ceE2dj66eqvrUJyA9u-0jNeCZy7e7hHu7Hbgby3d2VTPtUok0okELmEiF3O7vFDPmGFgOtNMunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متوقف کردن مسی ؟
توماس توخل : حالا یه راهی براش پیدا میکنیم، امیدوارم سرما بخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100227" target="_blank">📅 10:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100226">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHaIPyuXqmwwXRSEscNaUZeu6vMoZAwdRIVgYzIGELfoudWnGRJnNxDthKFBjzLPD2a8klLXwZM20-kGnbWOozzqtTdZN9BYXohaf9Xy2bwKdVzhacB_REL37lqxVfJie-nQVO_jVHwowXh3q69TC0d-tEhOlejTyzrndTNmAh349A2Ydo-aUjFs76z8ur22KP_B-mQ7vDAt2Exh1Q43864lBYXjL38WJFXHsR0tHM-vBeUTrAMMLA4VKSoauStfeRbN4cerydb7A1CwzOHASjla59sYVvAiiLahgPzZG9RiTerm70Clo1DR36QoO14rDdr875u0bObShiaxINcuqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
انتقال مارک آندره تراشتگن از بارسلونا به آژاکس نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100226" target="_blank">📅 10:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100225">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d59df3b59.mp4?token=V23FcE4W5lB-X7OTxDbbhexYIE5h-5_BX6r_PHsu9oiEimSSlThcuKBE_HbWWHFUJzDhfo7DGpeKsjLOZKi3KPW5sAnK5DxcZXmzOa4ih38_Uxr7Ze2l_JA7By6PPV_WcShLJ45rQmmZY_0063uvSgy_GGH8L197QZO2d5pD7ACP-3QBqpnASzA_hdnCWAyCw8EU-5OFSG2xaGUBNJ8NuMlt-s_AzCv3lpzH8Vzhe_NW2q8gi_7OVQIyp7NbkvRGDSinv0EbbhE-Tu6oR1gRxoCD8jBM2LbWPZAyj_4XZjlcyKMw0qluyW1gvgyMxr03idCi4E0sonEsWVERG2d6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d59df3b59.mp4?token=V23FcE4W5lB-X7OTxDbbhexYIE5h-5_BX6r_PHsu9oiEimSSlThcuKBE_HbWWHFUJzDhfo7DGpeKsjLOZKi3KPW5sAnK5DxcZXmzOa4ih38_Uxr7Ze2l_JA7By6PPV_WcShLJ45rQmmZY_0063uvSgy_GGH8L197QZO2d5pD7ACP-3QBqpnASzA_hdnCWAyCw8EU-5OFSG2xaGUBNJ8NuMlt-s_AzCv3lpzH8Vzhe_NW2q8gi_7OVQIyp7NbkvRGDSinv0EbbhE-Tu6oR1gRxoCD8jBM2LbWPZAyj_4XZjlcyKMw0qluyW1gvgyMxr03idCi4E0sonEsWVERG2d6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ملینا بلیک نشون داد هیچ استعدادی تو گزارشگری فوتبال نداره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100225" target="_blank">📅 10:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100224">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67f731ecd.mp4?token=nE3GsaI2k34QD0m2HvKUk1Od8l5_DuL06ZUfrrzt0-g6RTmWHqx70nhJ_LcTf5pmshypkqmCcC8byd8zN1-CUW53EMF-n0sRQKlAudhxqv5pPtwbq08NtrAeElX6s0lVfu1RcLUNYq5UC358UM4IPtWZU3SOi9JJmomPvr0MoBnVT2U4eGxI3YsIrfikI6wRzlKS4l6upY_lO0rStlj7srHCLJY798FOoLeAsNvqF_PUfq10ZQJ3KRGWG0vkIaIuqaXqRpGKS3xfYPgXN9ov6Xknt4_1-vC-aRfkauccFbUSprHaR4mUNQhPYDZ3Tdm3eQyOXm2Jm5KBKBczR18sTxjlzNXh2VC180BeummjqIuZvXW1kTrXtD9nnABDlvUWKIbcV-ODF8oerfI9LdU5btJ7PHzc5BXX3AykMjFGW07fkfJwzxoVj5la1MVrmz-85wW1wOBp-oGXK6ZbnQub_5QUsiqELC8GVsQbBLsfPrxwGfsH-05PpqvLn61aTp-QgH6_26dpz893IKM7GJNJMslSc4Ol4ICoCS3Swab4OS17eCg2ku1d9OSjQjopV51gpEe0Q09QzJ2zg6NHJNN9j5j1B7KX8lCBik8W1BrH_v3BM7bxpYFO9VrDx2MAScer1HUrrbfyYeR7CXBaw03S1o2lEvIIfCzebKkSjae5CQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67f731ecd.mp4?token=nE3GsaI2k34QD0m2HvKUk1Od8l5_DuL06ZUfrrzt0-g6RTmWHqx70nhJ_LcTf5pmshypkqmCcC8byd8zN1-CUW53EMF-n0sRQKlAudhxqv5pPtwbq08NtrAeElX6s0lVfu1RcLUNYq5UC358UM4IPtWZU3SOi9JJmomPvr0MoBnVT2U4eGxI3YsIrfikI6wRzlKS4l6upY_lO0rStlj7srHCLJY798FOoLeAsNvqF_PUfq10ZQJ3KRGWG0vkIaIuqaXqRpGKS3xfYPgXN9ov6Xknt4_1-vC-aRfkauccFbUSprHaR4mUNQhPYDZ3Tdm3eQyOXm2Jm5KBKBczR18sTxjlzNXh2VC180BeummjqIuZvXW1kTrXtD9nnABDlvUWKIbcV-ODF8oerfI9LdU5btJ7PHzc5BXX3AykMjFGW07fkfJwzxoVj5la1MVrmz-85wW1wOBp-oGXK6ZbnQub_5QUsiqELC8GVsQbBLsfPrxwGfsH-05PpqvLn61aTp-QgH6_26dpz893IKM7GJNJMslSc4Ol4ICoCS3Swab4OS17eCg2ku1d9OSjQjopV51gpEe0Q09QzJ2zg6NHJNN9j5j1B7KX8lCBik8W1BrH_v3BM7bxpYFO9VrDx2MAScer1HUrrbfyYeR7CXBaw03S1o2lEvIIfCzebKkSjae5CQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
گرشا رضایی: بهترین صدا برای گزارشگری، جواد خیابانی بوده ، هست و خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100224" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100223">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏆
گوشه‌ای از بهترین سیوهای جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100223" target="_blank">📅 10:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100222">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f24ohMNDBKLJGXQjWvBTDCW9cwCJoeftSxnraprO6tsOKYJVvTa2AWQXaq3asRDpIYpd5Xe-q1bo78OFC9BFFLNB1FWt5O6MFzBuHC_FcwNiKFcopCiCHxMQmermwPHCXf95FMvF0qa43xfoZbwatxfBQPW86LbctbSph6OrqlmV5QPNjwxvuEJXLO6uSUiGa7THyj4YXaigA_HrmKtwP3Ok3WlRzzgLZdbYtduN8shFYSU03igKmG25wzGV6XLN1H17BdByOR4JOLPvTQEhMS5dXr0etD1yKAdMrgK3HcX374MWyD0w5lTmyt9SSd5K2WJhX9ZEnLunk7Rg5cvsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین رشد فالوور بازیکنان در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100222" target="_blank">📅 09:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100221">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👀
🇦🇷
آرژانتینی‌ها از سنین کودکی به فرزندانشون میفهمونن که لیونل‌مسی کی بوده و چیکار کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100221" target="_blank">📅 09:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100220">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">در حمله شب گذشته آمریکا بیش از ۱۰ موشک به تیپ ۳۸۸ ارتش در ایرانشهر - سیستان بلوچستان برخورد کرد که گزارش‌های اولیه به ده‌ها کشته در محل انفجار که عمدتاً سربازان وظیفه بودن و دست‌کم دو کشته‌ی دیگر پس از انتقال به بیمارستان حکایت دارند؛ تعداد بسیار زیادی هم مجروح شدن.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100220" target="_blank">📅 09:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100219">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pELxHSWEWLAruGWjGG0YEKaHtoSRNkngNp4WF6OEDKBIKv8X3YxdQLEqsJw0w1hWCEHKQsXbDts7p5s3HonbapP7ocARTdBWaekl5i93o-2P-YUehvOiOi6zn_IT9f-ccg-4nP1TRg6Tn8Y5AtrUhVcdjHYdmOnyIc2xue6c1zNziSByu5ux_INYO6xoZ1KlvvAV5Ag58l2h3lRB6tL00HgntJLXWfVypARs7JIqMJAdR0ZxxEU2cJtGI_XFivB74XKoOaF7x0WB3Lf7pSscaPwkPwzRctJ0NAMRbcEoWC-Qq0Do-I5KgIbDGt_OnBsIesF6MfI1tsN2kWug78RTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
با اعلام فدراسیون فوتبال فرانسه، زیدان رسما سرمربی خروس‌ها شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100219" target="_blank">📅 08:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100218">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxRZ4u1fLbmcNFY7YxUc0f8ZpeTj_5lQQbndzJWUNE4IDTAN9Do5cwYOsQNNNbTkXAysamdKZUqdB282n--HD3eo66huqad0V9jC79bFvXs1N--2opHkVmI5kHlv5EhkqEt7kfIggJc6HlhYcvLI9hDqkiC81oPoH1_pkLcBfZQHFzFKuoGya64YPTHq0xCMem3wp2DWDHWF791Qxu3tNYZHiTnZQgzBGz1BJybMA8koRKFR0a3ClofanWg2kxLOeO0Sm9Z8rRA-udlBSisTOB2fFuJWJzQWbTrFB7raUp6-9VlwW64Tuh0T9bcHbEirxnOQrnVB4sOJecBpxH__2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🧠
رودری با 11 بار پیروزی در دوئل‌های خودش در بازی با فرانسه به تنهایی از کل خط هافبک فرانسه (9) بیشتر دوئل موفق داشت
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/100218" target="_blank">📅 06:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100217">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d888d31120.mp4?token=WkPCyO6RQYa0srN3qKccw1pIvvqDcZmAEqTcm-ljFDwdrm0BTzZHXV6ODBj2GjeMVhOSp3wqQzsGQhfGHBXrtolLSpJcf4LauZ5elI_ILvy_717AFH7-davrbR94zvSqE6M6bjQYLgct0YunhARLzEo0MQ5CC6sbPyl-D_l-4Cf-jA7riE8LBvOCjuoy6kZwex_2Y1OFEcJx4PGc7a0H-heVHH87eeoOWQ__TLp-JKZ3s_JosXNBWymcyJTtGhmaEaCBF64RxyLua21GmMptnw27ULT0riUVMKdblgHCxXfUXXIT4ahhzQe-4YoBf2s7Vp-hEFkHzTvSwpFKypvXJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d888d31120.mp4?token=WkPCyO6RQYa0srN3qKccw1pIvvqDcZmAEqTcm-ljFDwdrm0BTzZHXV6ODBj2GjeMVhOSp3wqQzsGQhfGHBXrtolLSpJcf4LauZ5elI_ILvy_717AFH7-davrbR94zvSqE6M6bjQYLgct0YunhARLzEo0MQ5CC6sbPyl-D_l-4Cf-jA7riE8LBvOCjuoy6kZwex_2Y1OFEcJx4PGc7a0H-heVHH87eeoOWQ__TLp-JKZ3s_JosXNBWymcyJTtGhmaEaCBF64RxyLua21GmMptnw27ULT0riUVMKdblgHCxXfUXXIT4ahhzQe-4YoBf2s7Vp-hEFkHzTvSwpFKypvXJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇪🇸
شعار هواداران اسپانیا: امباپه کجاست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/100217" target="_blank">📅 04:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100216">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8960eb8b.mp4?token=J-Q3PKe36U4gFXC9gV1LPmzUK87ewnpAkBc_EzGPuRiVtbuHFDF8uXIpr7jli_zUASRHL4uGpzh6boCDn_apfqg4KlgiTxwfEVM-rYBwNTln09caFYjjTGPNE47aCwFdpsYDvVbl5MTSzBntpQhszNOV5aPjxWigkeGS7l3hL-wvXJpuEKlFkaAavK5R9OsFOfehckM2iUFZ4znx2Z-0NFq498m8vGUYL5Zh3xVVO0IIIVdUEPg_pKNVxm4sTRk-VBjqlGS05G9sX_qp6GC45QNv__C8rGsG4SYm6wzjjDVPOrOMEVvwCc9JIg_8EUWI2Ysampc23StKmWcy4ugeMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8960eb8b.mp4?token=J-Q3PKe36U4gFXC9gV1LPmzUK87ewnpAkBc_EzGPuRiVtbuHFDF8uXIpr7jli_zUASRHL4uGpzh6boCDn_apfqg4KlgiTxwfEVM-rYBwNTln09caFYjjTGPNE47aCwFdpsYDvVbl5MTSzBntpQhszNOV5aPjxWigkeGS7l3hL-wvXJpuEKlFkaAavK5R9OsFOfehckM2iUFZ4znx2Z-0NFq498m8vGUYL5Zh3xVVO0IIIVdUEPg_pKNVxm4sTRk-VBjqlGS05G9sX_qp6GC45QNv__C8rGsG4SYm6wzjjDVPOrOMEVvwCc9JIg_8EUWI2Ysampc23StKmWcy4ugeMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صعود اسپانیا به فینال جام جهانی 2026!
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/100216" target="_blank">📅 03:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100215">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bb44d472.mp4?token=lIla79vh4uP8YI4UumVMEMX_vhfgFWNHzqRMODwwkL4AQ614EnC6v8XPGEtGnz49mq1E15D79ggCpi3-zqdzkTcRrkXHL_jxlgwVjp-eCMBW9PB837JQAl4D-NdGBlQlu_sfHz30gxQai-MS6PMpsoab8ioYloZ_hMXhp32Soa8fZ5NvFkOdxjtSqs2XJ6PLdZ3eNsA-99Cy9mHlTWYcwl0eqTgbxbYmEIYLde22rLBlToR6z2CwLkqrGzRLldnFe0SO8HX-D4kCzkZ88fMiFSJpSWyp4zdPvdvH6d8bM6uQEnvoVyhqVivvpFUbxaKQlymqFwet-_UcY34fO2PPtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bb44d472.mp4?token=lIla79vh4uP8YI4UumVMEMX_vhfgFWNHzqRMODwwkL4AQ614EnC6v8XPGEtGnz49mq1E15D79ggCpi3-zqdzkTcRrkXHL_jxlgwVjp-eCMBW9PB837JQAl4D-NdGBlQlu_sfHz30gxQai-MS6PMpsoab8ioYloZ_hMXhp32Soa8fZ5NvFkOdxjtSqs2XJ6PLdZ3eNsA-99Cy9mHlTWYcwl0eqTgbxbYmEIYLde22rLBlToR6z2CwLkqrGzRLldnFe0SO8HX-D4kCzkZ88fMiFSJpSWyp4zdPvdvH6d8bM6uQEnvoVyhqVivvpFUbxaKQlymqFwet-_UcY34fO2PPtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/100215" target="_blank">📅 03:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100214">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f573ba753.mp4?token=S5pOjQ2SJ1JAG95LBetXzsom_M3t-P0tcOi0zVwiwY1zID8I_aryldGxEtWc9dMcupI9IvQDnIswJayUnV2BWvZS5SNgFGESFl8-AC9K7R5DxO4rLW8nAnZ5Qk1azmbRFhqBzo2FRfiCXsh_fGOY55NQu9rGpkNs8ADFqW8tM9lzCo3_Nt2SysX3fH5p-jMOZk4tIfFpN64ve88x3aMwf7rJZ06z2w8Mbcwehd77EOPNY9eYLbsCs9-qIAVzbKjdH4tRfU3JuVNB0nVe9tMCp5OdsRfupIMgpbyiQuvms5QBao9w_uWUM80QVtKAVoxJHtmQE02g7Xfa2ShTxus1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f573ba753.mp4?token=S5pOjQ2SJ1JAG95LBetXzsom_M3t-P0tcOi0zVwiwY1zID8I_aryldGxEtWc9dMcupI9IvQDnIswJayUnV2BWvZS5SNgFGESFl8-AC9K7R5DxO4rLW8nAnZ5Qk1azmbRFhqBzo2FRfiCXsh_fGOY55NQu9rGpkNs8ADFqW8tM9lzCo3_Nt2SysX3fH5p-jMOZk4tIfFpN64ve88x3aMwf7rJZ06z2w8Mbcwehd77EOPNY9eYLbsCs9-qIAVzbKjdH4tRfU3JuVNB0nVe9tMCp5OdsRfupIMgpbyiQuvms5QBao9w_uWUM80QVtKAVoxJHtmQE02g7Xfa2ShTxus1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تشویق تماشاگران فرانسوی توسط امباپه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/100214" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100213">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUyolGa4CdnKaUy09jEkG-Df6Ot6ektFBHQaQ0_J-fp051XeGLRAJ1ZH2lW9hBPURMZG8MgUDAdYrg2dIhD5Q22HCu_vzRXkEv_GYm1SnSew5bBry6OKJDtUBzWtXpqvLWGmrhH8G55a5uN_2z4GsjUM8zrA_0qmfA4GWesZAcBLgJjBcgX0VMKfHMS_CXlaHpAg3OIQRHswZSWNRvphXlU5eyCPfrTaPg9twXbundcvhj-48aQW5WNBAR_TwTIZplXwvSa0Alef2aTmbXkAUlGz0X7BqcQbr32z3_hmzXlThl1vVLK6zGuqCOYW2vmK_IeF1lzMkqZrBOg57oQkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
🏆
‼️
از میزان هوش داور بگیم که بنده‌خدا یادش رفته بود اسپری محو‌شونده خودشو بیاره و وسط بازی داور چهارم رسوند دستش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/100213" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100212">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری ترامپ: اگر ایرانی‌ها به مذاکرات وین نروند، هفته‌آینده تمامی پل‌ها و نیروگاه‌های برق ایران نابود می‌شود
❌
روز دوشنبه‌آتی دقیقا اولین روز هفته پس از پایان جام‌جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/100212" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100211">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری: ترامپ در مورد یک حمله زمینی به جزیره خارک: " کافیه کمی صبور باشید. من این کار را مطمئنآ خواهم کرد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/Futball180TV/100211" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100210">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60a4ce9f7.mp4?token=Glk_Hm9jhIzSdM178QJQmtk8BfnVU4CTSlql4BnSLf-L0JJoryO9vx9a5QBpCglczzLOoIWz1k8R6ylP6LKn9Cly2WJ2lclHLr8KUq3azqJcYnGy-pQHX28mB5xan5bu9xA8fxgg_8Ywh77BAUWl5y97IKXPN6JY3n0FkI8Y0nakG_9-9Pcs64kVaQdyvplneHFqISJv-Kjow3kXWdMUzjUsY-e2gKeL2iYFBbNMK0WVFAnA43XDaIGDxbg1OJsUdylrnYrfOB2nUl71YLe1VnvZcX5kUbVpNk-yPD_Q6omXejMKOmlWQfuCG9m-t3mzfjSz0Vvd0E7Z8WUwFYAUdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60a4ce9f7.mp4?token=Glk_Hm9jhIzSdM178QJQmtk8BfnVU4CTSlql4BnSLf-L0JJoryO9vx9a5QBpCglczzLOoIWz1k8R6ylP6LKn9Cly2WJ2lclHLr8KUq3azqJcYnGy-pQHX28mB5xan5bu9xA8fxgg_8Ywh77BAUWl5y97IKXPN6JY3n0FkI8Y0nakG_9-9Pcs64kVaQdyvplneHFqISJv-Kjow3kXWdMUzjUsY-e2gKeL2iYFBbNMK0WVFAnA43XDaIGDxbg1OJsUdylrnYrfOB2nUl71YLe1VnvZcX5kUbVpNk-yPD_Q6omXejMKOmlWQfuCG9m-t3mzfjSz0Vvd0E7Z8WUwFYAUdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/100210" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100209">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
: ترامپ در مورد یک حمله زمینی به جزیره خارک: " کافیه کمی صبور باشید. من این کار را مطمئنآ خواهم کرد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/100209" target="_blank">📅 01:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100208">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a1bfb1af.mp4?token=HidFCejDBllcssZeDNwsmAcrLh4IflrVvppg2Rz7JrN2ZWsraxAjKafPp6pcvN2ZC8eKvrxFAW5aN1XN7WMaUS26ay_DBUbmrVL2_CuEVD2qVkf_hRWlsgy_Bcux0A7108QFkJBwYDC2W6O2S0BFjVN0T3mwfUHLFC0AB2Cj_4pqHjBYxIEwGfwRheRjYZhKIwqgOzWoYVEeOfCLSmM0GszYYo9MqGQ6L_CeV7QCSYFl1DoUOLldOmz6ij2D2wN5fz9SPF_r4iSAqqXTd6Fxl6puO_VCaVQgh7TyMl-GWdJP4eUD9wcItOqvdxayJ81PQ-UDupBqN3c3d_uFea6GOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a1bfb1af.mp4?token=HidFCejDBllcssZeDNwsmAcrLh4IflrVvppg2Rz7JrN2ZWsraxAjKafPp6pcvN2ZC8eKvrxFAW5aN1XN7WMaUS26ay_DBUbmrVL2_CuEVD2qVkf_hRWlsgy_Bcux0A7108QFkJBwYDC2W6O2S0BFjVN0T3mwfUHLFC0AB2Cj_4pqHjBYxIEwGfwRheRjYZhKIwqgOzWoYVEeOfCLSmM0GszYYo9MqGQ6L_CeV7QCSYFl1DoUOLldOmz6ij2D2wN5fz9SPF_r4iSAqqXTd6Fxl6puO_VCaVQgh7TyMl-GWdJP4eUD9wcItOqvdxayJ81PQ-UDupBqN3c3d_uFea6GOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
داداش‌یامال بعد گلی که لامین زد و مردود شد حسابی زد زیر گریه و اشکاش بند نمیومد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/100208" target="_blank">📅 01:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100207">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErEjRgwolbSMjr-EekQLP-WQPxQyXa-kFTwq7AZp2ftxR38i8Dw2aqMNJjIffz2EzxelYrfgGEPxaAkxwuFMnWik4o6cgxLYkqJ4ShDC2NihdHhIktLTVeJZGyvkRtA3j-9u1xQDXw803KPkX-IVweaHxF5Sxj5o7RSCXyEbxecBLZpLRi4Owwm6reA4oMBrcsDFAL-Tq_j6XqSYHnzhJSojxqV31HimPMgeVigJDMFwiReVUNAL5eKd7035AnX2JxJuSU1l9JYZawSl5Olr-UR_G7Dgw31R4yWhu7003sztot7CTlL8L2MQc4mSt_AH78rqp2HHxY_U2RlOtP4-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
پدری، یک سال پیش، پستی با عنوان "19/7/2026" منتشر کرد، که به تاریخ فینال اشاره داشت.
و امروز، پدری به فینال صعود کرد.
🫡
🫡
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/100207" target="_blank">📅 01:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100206">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e25e4d415.mp4?token=cmJzXztMkdK_UhMEJYifTuKy9mXMbPaDZ_moN9bKOGhXCnEY8e8-aqTqUOZyv9oOSMwuyJgHyLhD11V47_Gxs_vnIvVBdBHFjEzTleEVhjvG4CjylqBxq7ygXTgOmirOXuRHkd_wRH7xKMUfPwzME7QQH9Z9GcPi3Z6kt0mguxIDkFhbmPNEkF9cBZtpXjajllh-jvMsK4McfkvlmMneAQum6_lqTKDtuKTiyx6o1G5lv2GRaA-EgKOJZUgczokg-ist6sBkKFbBchTAVxFgylMzaqL1NxO--tF2GAmwfG5PVPalf1SwqMkpJZ6NJNcRAXZ-rosTD5oA689iOP0-gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e25e4d415.mp4?token=cmJzXztMkdK_UhMEJYifTuKy9mXMbPaDZ_moN9bKOGhXCnEY8e8-aqTqUOZyv9oOSMwuyJgHyLhD11V47_Gxs_vnIvVBdBHFjEzTleEVhjvG4CjylqBxq7ygXTgOmirOXuRHkd_wRH7xKMUfPwzME7QQH9Z9GcPi3Z6kt0mguxIDkFhbmPNEkF9cBZtpXjajllh-jvMsK4McfkvlmMneAQum6_lqTKDtuKTiyx6o1G5lv2GRaA-EgKOJZUgczokg-ist6sBkKFbBchTAVxFgylMzaqL1NxO--tF2GAmwfG5PVPalf1SwqMkpJZ6NJNcRAXZ-rosTD5oA689iOP0-gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
خانواده سلطنتی اسپانیا خوشحال از صعود کشورشون به فینال جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/100206" target="_blank">📅 01:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100205">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a763ec0bd.mp4?token=bt9b6ZMGgiAgsrU5dWE05bmgyCxT3yD8PL5W_RIc4awbzd6J_IhKXpmGlJEj8fJys70sVfBzq3DV0ODlk2e12PubNl7axiaXXSNTlZ5YvglcdArzwr1V-C3qhDcRhMUsGzyaqm7H9T_jwjEuKIoaoJ9Ah1IWPIjyECQH_JY9s6sBQKVEjD7EtvDu915ZE8p5Kwtj1VHWAKyYxcJYPA85m2KumJ3tjIxGidnYWMwZQSenM_eampxMhx-jiuDwhz75SixwdVt1iRobXqwYPR8HBV2mxI1JFToj6O7RIvijkWnuu8j9clO2XthW3f1V-cQz0MGmqyiGerpydwPkHibYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a763ec0bd.mp4?token=bt9b6ZMGgiAgsrU5dWE05bmgyCxT3yD8PL5W_RIc4awbzd6J_IhKXpmGlJEj8fJys70sVfBzq3DV0ODlk2e12PubNl7axiaXXSNTlZ5YvglcdArzwr1V-C3qhDcRhMUsGzyaqm7H9T_jwjEuKIoaoJ9Ah1IWPIjyECQH_JY9s6sBQKVEjD7EtvDu915ZE8p5Kwtj1VHWAKyYxcJYPA85m2KumJ3tjIxGidnYWMwZQSenM_eampxMhx-jiuDwhz75SixwdVt1iRobXqwYPR8HBV2mxI1JFToj6O7RIvijkWnuu8j9clO2XthW3f1V-cQz0MGmqyiGerpydwPkHibYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
یکی جواد خیابانی رو بگیره. بعد بازی رد داده سرود خداحافظی میخونه برا امباپه
😂
😂
😂
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/100205" target="_blank">📅 01:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100204">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhdcoCjff2S9gEIm-3h1ec1z41SXom_elyXm8V16n0OHNJKHoB5az_hC9ipLB-SabMXldZFDL9A7XisgXxhY9WZvZHYf_UDiEh44h3oCz_j9MGwKyYknwbeFkj97uKdN12YkeV7DxcNd-utBPHAj0_8Vn6mDUgO1Sj34ID3o0FUnsribJhl2d9a6r9HNVUJpq1w6UbeLBNFzeLC4B8GYw-fF8DgPzJC2HLREblpokNqM-JmWstBoYdRTF5J29cU5u_z0Xm2hOygP_kHUo0yLKgwlAPhHGJCZt8gRBVuoqPcZ3EDh9IxZDKqqabq-_9YmWAYOC761w1qNuzYvItiyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">25 درصد از شکست‌های دشان به عنوان سرمربی فرانسه در بازی‌های رسمی مقابل اسپانیا بوده است
16 شکست
4 شکست مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/100204" target="_blank">📅 01:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100203">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4XRXLWPcRFjzbJDGhFMkdyMsjCv2dvmQTqdOyCXoxCcXS7d98NuIRQjE9ASQG9iHIzWS2KkAlBUDwBKmp_hYa3eFmhilEJ0rV5QzfeXe5d8qRxq1bNoKTKnGIDfOlMWKzJSxdYviZAGE0EzyYGe4xYpCqboWki0Omdp4S_xlORg5az8iVb-cJoUhYwUAVL8e-RRqLa-D3cydemrwCiytr1z_sQbkuijlN0LPBqK8DXEIM6q0DilYqZKDpG6vpPmlGC67kc2K4IbNueI3LHyAP-6P5tnshMlGqgWMtL0ejtJPTfwdGn_yNLQqZjfV6CknyYhtvxiD6bwowpP9rRvgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رایان‌چرکی علیه دشان: مشکل داوری؟ قبول ندارم چون اون باعث این نبود که ما گل نزنیم. ما به تاکتیک‌های خودمون و قدرت حریف باختیم نه داور مسابقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/100203" target="_blank">📅 01:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100202">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKjNkxsK8ZBSqACHglf7d-zPYWv-G-9n87Aa9Px5LWN4A3Zd6XuDBhpufBUcbkYr5EXt1OekU7TB2LVoCFz_am9ytRzWlyeX_hxAGqCdKve7m7QpV9NjALu1IZHZgCabwU_KdopDFNJnpR-jCI5Mm6f3a-MdH_M6ewN7NQQNoaxuKmRB0DipQPRb-ByC-iKV5ACBQsGYnhlCbGkvMLzbytOa7xTZtXOqbDopdcxEQNdNYicjrD_t5tZfUY1ZDALMx3HwGdx8MiCIywWBFOdZrlucajitqhkCOm67EzqK82_4ZcsSrC_2NT3Z7TLAeubrxuY9rbk8xUrdQBAYhU7Utg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👤
لامین یامال در 12 بازی، به عنوان بازیکن اصلی در مسابقات یورو و جام جهانی شرکت کرد و 12 پیروزی با نرخ 100% کسب کرد.
😮‍💨
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/100202" target="_blank">📅 01:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100201">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW2lo6NieMGeLSSvvix2J5iTH-XjV1KLu6BFH5g7fsdmFEipSnHxsJpquSdbFggk7-i9JjMdyqR6yxlY7q_ueqhiEx61p7DDXRxNmuAxDn00Qir877DH-7EjvUmL95SxAHfSnOimI1Vu5J1cZWTfKyofY2aVZd8ik36Knu1aDI_WdMTGmsZy88z1NVwnIuBte3HzD1HJkcrmWU_2Ce_kJK1vxUfLt1l97ZXoHHgS9A3pyZsfl4ciZLO7tHecExW_r3MWQM0v-9hcdjhzaETJE_0cOZty4E7Z5sbqlX8y1VyOYeqIs9ha8scri1aJPgwuxQQAQ4E4M9kkXw0hAY6Zdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
امباپه در تماس با اکسپوزیتو: امشب انتقام سختی در راه است. خواهیم دید چه خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/100201" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100200">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzYCXTuhBGyyTg0L_4OsEUS04tHOSPhQjZspv0NPaj6AtwfRAp4bROG5C9zbWIt9j1gdcivYf1X5LV-SLgpwPKFrwAca_JTCqxQYljmXm9czCidQB9LJyRyUwxRngUZNUP34Ox8Xidi90hFGWI86skLBpm5doWTZkK2hG2Fm_oHb0ASjy5lmJm8M5ZrY1tmo3euYtwc8JYUujWu-vBkcQS_b6ei0J_f2FPXT88KYTeHmjsPrctQ-iOksYhbbZYLGUvg6ImWprR0B-yDyfi12Tou8iFCbTJynO-PM5jsZnVkQhgeR1Dln6L4GLrJrvd_Ey9eYxn9uc8ItrXXEguLwag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/100200" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100199">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256044b0fc.mp4?token=uTtISjHYRKc-9pRupe3Dag9iXxgIXCkfdB-IwlwukjKG3PS8ry2loUHZMXVP5JpZmKy7YcxuqTpAzAtoeq4VSjaJPjCIowEoA1D4RkebwUilYThyuf1AR5c2VIZQgY0BmM9wEY07Dit6llMprtqpNwazuWXuWl1l0d1gorFxySgSxii1M3FjbTvR6el9entGrkWR8gze0IXFjT-KY94-7xOEOpM6BfiZpZGpTwp8U9uMm6TpaenysQe6g4HJ7wrA_Ms1YDAvWxxixfWAvZ3T2nzDLj9w3spuQa4zx5hI9LtHvcrumirJAmexT1cednOEmbXPxnhRWjZmz_8fWvZN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256044b0fc.mp4?token=uTtISjHYRKc-9pRupe3Dag9iXxgIXCkfdB-IwlwukjKG3PS8ry2loUHZMXVP5JpZmKy7YcxuqTpAzAtoeq4VSjaJPjCIowEoA1D4RkebwUilYThyuf1AR5c2VIZQgY0BmM9wEY07Dit6llMprtqpNwazuWXuWl1l0d1gorFxySgSxii1M3FjbTvR6el9entGrkWR8gze0IXFjT-KY94-7xOEOpM6BfiZpZGpTwp8U9uMm6TpaenysQe6g4HJ7wrA_Ms1YDAvWxxixfWAvZ3T2nzDLj9w3spuQa4zx5hI9LtHvcrumirJAmexT1cednOEmbXPxnhRWjZmz_8fWvZN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
ولی این صحنه خیلی حیف شد که اسپانیا گل نزد. یکی از بهترین کارای ترکیبی جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/100199" target="_blank">📅 00:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100198">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgrSDxK2NOEnOcsFlJRI5UAiDYCoIc_CVasyEDWUyStUZFjBFGtferZSQ61wSgl19mn99PcxqDTE2qlCwpGUY1_n_MYRQKpa9veJoOLXpqS7tAXgdX3tDIS2d0tXjVcGpI-6-YpbojehonMa3QF2hcPdHK36I0sbJB_9Gz2CMQPzlN-d-Oh8HqmLWDHzg-wQGLZOXvf0lGN6xZr84RvHAWIYHYcLJkhz1hudel6drw6OAba7DiJb8xqlxhOnUmwRTNiYfJAeo8SBXm0n6F5PvXmGASuKVzwRjKbYT-cGvbQvlBh6RfAJQfwMIt6HY1kztBbUk8dxKmywK67aFFRC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
رختکن اسپانیا بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/100198" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100197">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
❌
🇫🇷
دیدیه‌دشان: یک سوال جدی از اینفانتینو دارم. آیا داور امشب عقل سالم و صلاحیت کامل برای قضاوت در این دیدار مهم داشت؟؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/100197" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100196">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a2aabbea3.mp4?token=XJyJXKInZqpRDKukwFdirzg0Th_4hCBAhFKKOEOsY_uQftF9KpLH4T3qXs2UWMmK0KFfnQy-fL9FPFba7TyiC_SKZATpgnwAx7PSISl_8zhkEQ7s8PjLS5coH7SkWvah_XNSPGWssXka2b88y7-ZGeQT47bh2WpXh7OLgHQ3fBhtDm60casN2PSQCrTR-dGVBV-OkQ9s4pOhlMoJZ2Equ0dRv8uRXwiN_OQjLQI9jQYO-2-IF-G1NN_RsJv6nwMnKY_3iilFzyXRdDP41LUaxvTCUkbEzEW73TJpFxBNao7lLwl3I2vMoHmMBsmwPXm9DHZYqxNTj15E-l726uHVrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a2aabbea3.mp4?token=XJyJXKInZqpRDKukwFdirzg0Th_4hCBAhFKKOEOsY_uQftF9KpLH4T3qXs2UWMmK0KFfnQy-fL9FPFba7TyiC_SKZATpgnwAx7PSISl_8zhkEQ7s8PjLS5coH7SkWvah_XNSPGWssXka2b88y7-ZGeQT47bh2WpXh7OLgHQ3fBhtDm60casN2PSQCrTR-dGVBV-OkQ9s4pOhlMoJZ2Equ0dRv8uRXwiN_OQjLQI9jQYO-2-IF-G1NN_RsJv6nwMnKY_3iilFzyXRdDP41LUaxvTCUkbEzEW73TJpFxBNao7lLwl3I2vMoHmMBsmwPXm9DHZYqxNTj15E-l726uHVrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکراری ترین صحنه دو سال اخیر تقابل یامال و امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/100196" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100195">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🇪🇸
کری‌خوانی دلافوئنته سرمربی اسپانیا: امروز مقابل یکی از بهترین تیم‌های جهان بازی کردیم هرچند حریف مقابل بهترین تیم جهان شکست خورد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/100195" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100194">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiK1dR460RbyQ6lITdl8Jtzm5DRqotYOR0J9nViCW_ipMQ_C_y_drLQKlwwiL9lWSaeqUHpa99AkfMCIxNsE3Lhld1ZcTYQabdFzAU1drDKwwrV1s5xUIdEJGFUnAToR7vHpx_hs_XoV3layz7jsUXUm-yBCrx0BjqEfiDcJHScvz7BUad0TMb6H_S-1SHWtHQBXiduRsMmWMJjyPN8gobhiDQMjz-ChLlem3cLwMzQuQZiGJTDGVwbQ6Ft8ff-5EYeipu4tqufZsEHRlYjffF53HiVZ3Wu33I1bLGZX5na395gOoff_bHE5s8HSzqgFzfGnR7BZQndK7OfOmOzFLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
فرانسه در یک بازی برابر اسپانیا، کمترین میزان گل‌های مورد انتظار (0.30 xG) را از سال 1966 به بعد ثبت کرد.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/100194" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100192">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGX1f5VKAA_jsVeY-rVNMuuO_mlXh3y6qcIxztpL7S_vcb51cJJ1ZFIdIsWt05aYyWX0Thf1i0RYDIQ3ptTVJHWhP-BQ6ttpGhUrNiVHCiwZNPWwI7YfMRGWQ7r3qEy8E9MoLkvSZCpSAvzvXsCP-dgrb6sJZ8D7Wz9Am1zOvvLC8Z7Svwync95ZKDlWkLSUF1gqRDAJTgEwfmM045Dg8HNg_jaPGa3l3lV7ZuvolH1jifjiWuREgO1hKGUzp6TyprvwDEOaSfAFP8fODmnSU4XnJ1t0sy8wKys2MbWdRBupPfr1fpF-USTKGM_AmyG8ipvMwwtjF_g-C17CoLIM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
پائو کوبارسی: کیلیان امباپه ترسناک نبود. قبل از بازی هم گفتم که ترسی ندارم. من در لالیگا بارها وی را مهار کردم و برای از آب خوردن آسان تر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/100192" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100190">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/qacqBRGGefFXk_2RNhfG326zkJ-ulU80oWQl2Gq5LYHacVMAJe96T83SMIC1s-odadQALHP7tnthiX_ovikhy4pLmNeIHHUcly1xZDnoA9TS22uWIQjGfwwJI8W61udLtqx8XnLSd3Mti7m5raAKVSzFLMWGcawxLRBDpUrV82yA6xMueAwiofzALXe1fKoYLp78NryvtG5PcyGXFErfVkUOE0GkupdYZDwVAgHT5mQ_Fpm7a7_oMhr2bTLRArYhMF5xY1PNmUig9F-h8QpA10VXCAD_-7Kv0y4nlPq1XmMOTBwucsZ9YiDPT9O0wiidwMqOZcTD7V4w6ZYEyIYdGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/J4tf2ftX6cBP_z3Seahze1I0cFm0Km3Px8g-kkTiVE_0aTF3PMT6HHeTplMGrC5I_RmizFmBwlbLh0cLtwDCjDulhp4KE1zfU1AbNR4y8FeqmlbWK63vwsg-8KLn5D3A8NQc2Rc_ki4TM-QPNtlKiLuSPZrJ85V_OjUgBPHsePmt2mggeRQHqc-Zok0LQPh-IDIv7dxomETDWsi5k75KypOpe5eu53kAPRwQqFaWi0bvVPjit06bzzSesLJR57_ZnnP3H4HDqjnaEhNr2y_kmCZEhhygvfwLbfYqgQc36v6fQ89mhvLsqCddec2E0V22jPseie6Y2L44pwoZnqwsug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه و این حرفا
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/100190" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100189">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lVPaWokwh-DDg_kdIYKqeZNDp1Rnl_7uwdu_9lCG25AZvg-KWbgAkqxK-GXSJntZ1XeQGaMNGxFQenbpUdEo74-05-YZ_OkxqQtGRa83ggaJQCoVAgJXMy4lJ4M2Rz1GWdu92wsVzWLE6JUXBVpcbaS72_IaKGW9O2gK5Gsm_mlGAdf3O-hXZ5bEIrpvpmQA93u_5LD7ubBhYLkyBOWbKNrItxgFg8x9oUYAtMpJoGa_J-koDj7AEUTo9-SRGW_FBL7kXyQj0u-Shd0b-0XgZXqpFxvpms45rHt9HqOGxo8IKPQ3AlS1thTvRySJWWlt2gareqgyb9LXf5pl8K6lqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫡
🫡
🫡
🫡
🫡
🔥
Respect For Olmo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/100189" target="_blank">📅 00:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100188">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cvEmbyziu9Ky8-T2_d77PilhbHHKClILip0iGBmD7q3jgfYCaPe-pRTxN_Ri3vZqrFj6t-L9F4gcSJUEJucx5_OTX1Bo3aOHPD9kdrNVTpqwDOv13Bd7Nojp2Px1Sp5x60szItCEKoizbCmqqfPE3Dh_xn9dMyTv-QqpviT0PjOrSAkLY4UY6t607CKZmn1vh7WmG7ccXBL4RuAfP0qyvND9F0UqfF_8XI-bL_V56qvgeoIXzLCsZcTvnpIG2lpSjH3a1CY0DySvJFD9PbT2ZWpO17jw8jOHnRf4-vUuTd4sKnRV3ggMjKQLLH_LA2fbHq2Y10ig1SR3i4KZ39xwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو کورتوا امباپه بعدی بلینگهامه برا
شون
زانو بزنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/100188" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100187">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قابوووووو از دست نده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100187" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100186">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDQ6eYjTwumCi_88uyQa08I6kx63aoN4-nGaB1dCON1vj5ON60Iwrt90_Ss2BncaMdUYEkZUS2Lk5qay9Pvd94gqiEMfKP2vToSpqhe2Fg3_uqEjNDItsNtaTv5YoMV81PovxtqP34tePqcF8skceo-GkS82Kmv7mD61UiSRivVKUfTyMvmoQYZNX5EYPHiFuIA7Q58PGkACSRoCV3y97jou6pp0CxbDBtAzarSRuvgQZRR4YbUzU2nzW5LgoZbFktRFm5CqTKBBm6aQLHHgabUYMw4N9M065KBBsreNU4XWkWapWCVmZLlFJF9f5x6WD0KKVBad78nLMRb6Qrhp9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇫🇷
#فوووووری؛ دیدیه‌دشان از سرمربیگری فرانسه برکنار شد و بزودی زیدان جانشین وی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100186" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100185">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxp7pLIjsoiIzQ9h7Ie6AjbxNphC3eFW5xMbCcs-yYult12SD8ZzxEc2G1x0XYW7aqOPRDNxzwB1oZfq3OH5bfVC-k5XR-tYy0rtlZxKJIAptt8t5pbJqVcCfuOTCdLmDRRYvc7uNizeBCjPWpYAXDnEDatMh8SQYVFuE4_UNifo7ji0gAcoUExX0xCd4shlwjT9pEfSwbro8wixGRJf-k_xi81OFMSNjfPv63BmhpoZI2NDCH8K_njT7SMnvj3LVbXw44Dh_Zm5hqMMW8HDH14ktSrrO959QekLBeYmJdfATD3Jme13_K6zMOwydh3X0V5YyvvAlS7uVXg3r7gYvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابوووووو از دست نده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100185" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100184">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC9DjeomV3OSsCexl_GVar6fByfjyg6lfBk5SPnHWF6PUlAr2UxkE8M0NPRiyO0BvbzRQ37bKgiv5QHKKjTRoLfhYsaPlNE2mN4kar5wHpnSUGSXlJbgPM3Ml7MoM-R5hRUfEhlWshLfxuSD1hCaX3E3WKAFBYkni9krt2o8PgqB7JJ8CgWD4PDI2CdGYnmb8T3Z-zcCUX47cDzO1LENGudPkfi-L8nakmcnXHjiuhqTcgWDSY69gNCfyw2mE70oRboCr5HE9sxJIBcLeGIKqI9IQ-m4zJqz4O0FXYtOOx1bwfqrlWwpKlggJNVHSpi-m0t78QEbOABRll6UgibRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
نقل‌وانتقالات تابستونی رو رئال‌مادرید با خرید کوکوریاااااا بردددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100184" target="_blank">📅 00:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100183">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فک کنم تنها بلنگهام موند و نصف دنیا مهاجر شدن انگلیس 🫩</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100183" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100182">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇫🇷
#فوووووری
؛ دیدیه‌دشان از سرمربیگری فرانسه برکنار شد و بزودی زیدان جانشین وی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100182" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100181">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iANqX_7zR2V8wUO1x8P7Hknil8c1DvY5ZB32g7kVkYRLpmWmU-sxfCY8JLth-KcW8YbqIRDcOuPyHHrurYtblcLgfXhOmh48jkhSZW9CDWU3qr7zIsisGi3K1mWuJHyLepPDUvxWbbAbVRAru1GEfyAAndyCyjfpyBbrlJVliafS_iTDf36auRO-38arf7S6Hr1vrkg4VX4zsQh90ihEmi8wBYH_Nh5a3ie2V3X_kCklKlrQwf4H872Hr7Gs4FTSxIHiYeq1nBRXDUNuo6_D_LnT7DI0GNDDpu0I-GuNl7HHMK_1C0rbtG5QoKeMEf7ISw234v5C46lxhW-QegCyuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
#فکت
؛
کیلیان امباپه تا این سن هرگز از جام‌جهانی حذف نشده بود و اینجاست که یامال 19 ساله وارد می‌شود..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100181" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100180">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/h2AUXZR_FBAakWlNeVfENQUksybRFgGb-gmfguw50gmTd7TNtttp-kZM-DOOB3ijeADfHFGSYXi3vmBABTD9i6buipJoUN5irLhT8Hz6wJ79dTEjFdm5sbP7MAEflMQ5TvfyfWTs1oWWKGWHPUeSUCyD0ejTQH8oRqyxTBgeYX83Q0jKAqbjKgsrUKOLEXrwKFvz65yQBrGQCZTG43Z_7VRN9tmfPsZUyMyq3SLsw5I3SNJ3pnH-RrVzDf_v13_i6DcgGXNuYVX8ZTL2ruMUAFB75b0HAKDZgWPrY4x90-LSSHn43aaSYLYU6vVJp1u9JuErZMQTug9Cx9bQsTn3UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل یه مرد کری خوند و مثل یه مرد یه تنه گایید تموم تیم فرانسه رو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100180" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100179">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYbQ_8cXSVh9OlgdHhtcjq2sxHJqZFV32V6Wkyl3pdWxKoDcMvbIpdFZHmihB1tlI3ogIsYvvVY8-KIgGTd0Wmthn40mV4t6WNqnnO-mNgTHdnzCdoQZX_sb-kyvy8C9HZZX9tPtf9NVxKPuCF5xel-ahO10JjhRseqV3sWpE6k49yL_LjzaXhN80ZoArnRRUx4nCJXPAgInKz7klxoYXnxeahxytkqspb52BhRUdr7YW4zdYmuPv4hV_b7J3AFeUtD62BAqvzsGMk7RvNhBFIAx2uieupD-2FaAafaChQ__PrV64ch6iuxnXWHoFdtj1cOSM2jkuY5QTTBFCVa29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🔥
🔥
📊
اسپانیا با رکورد ایتالیا برای طولانی‌ترین نوار شکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد.
✔️
۳۷ بازی بدون شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100179" target="_blank">📅 00:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100178">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlWBzxM7RYmsuhhObUhht5NLWdV2xgFhF5BcmteMcdYruPDAgcM3KnKq5HE8DpeJLNFUjcZMyeCA_GXWWaIHoRB2zFmMGlW3rwZfdV8Ji5As0dmgYktVKZD_WB-cEOgUSuRIvc4cvUmCUuaB__7XLoHMMO4ndsScCvlWj6ZJUSNGD37wLFlclns1B3s3_BNg39WTP_-_QquQ4SkZQ-CM_HLCfbliwvvTXo9ranz8Yv5IZx6rn6_H5FIrHLpTkpAGbdqPOSeK6_XB-3X1oyl8LtPOdO1Hh6r8ypXW-DK-AqMbOqPPOhiktU-ijAkErOhTPKxav8_PWc4eydn650706Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
😆
۱۹ سالگی کری میخونه و حریفشو میگااااد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100178" target="_blank">📅 00:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100177">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVH3vdGKuyFcaAEbP1Pf-QQtc3nTuhKbshvEz1yohmBvGBhheyFKfnBQ0_WxVIhwbJQvmsv1rgx0w7mxGaukKtUFxAXpu6hhqxYyRJ_GYwrTfl2yXELDC1r1wisWzCtLrOnoHjLuVOSaiocSSVirHVKlCbf6yhcdLVJBudEWQevHy19-U6FwJVqboUiZsydb3cDxYL7tSW2m6794a30xWL-LUtjHJRwt969e57j_H0JkmMRF97ICSv6MA15UoT2ZtZqqjLJicRqEI4OJSxo1fW_vBo-P3CK5V24iPxh1-BxWnZoZxzjRynPMMY4nWX5rFP0TPhE9K7JpyhlgGkDB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
پدرو پورو بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/100177" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100176">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPh63wlPZLjLDWtW49mE_Y4OpD1rdHYhto9t4lJQskY-VLzU9KH-V7n_8L2O-qd_6lYCNF3JQmwTW6UtiCaTgY8RlxXiBi1dEyLP0NpXjktXL5oAzz7NVYIXi4TlDHQZDQA8EEKBWkKrjtYexITeqf7dI1Nstr4qRYdMDN0zjysrayVTfHRLkODGUSAZXosQXfW8oLB5mqGZoEmI_Td4PG8ZjCiSpMQBoW0XGv4IhQMlQn5O5dlT0bkGAB4G384S0FBx1daQH4fqQq6NSeJ0hyYgnnT_3iqydi85W-6uH050IhV8WmAF7KjTgqnR3GoyXClnp-qQJL1c5jZES4X3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه باااااای بااااااای
😆
😆
😆
😆
😆
😆</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100176" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100175">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🏆
پایان بازی | ۹۰ دقیقه شکوه اسپانیا؛ فرانسه قربانی فوتبال تماشایی ماتادورها شد. خروس‌ها با تمام توان جنگیدند اما اسپانیا برای فینال لایق تر بود!
🇪🇸
اسپانیا
😀
-
😏
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100175" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100174">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afxryLpmba8kU5oLXVC73Y5VXzvzf9FKeYs5AJzv06IIcngqcWy5tacVFCtyx3OVWPjI_iiM-RCRQHVjW0hFmYqkYUqH7h7oKvUDazPzBUcZOhJ490wq6_PixVPoVjcoR_YK6Spn-dEPMzPMEi3LnhSKv1jf7T6NX7yvq8HF2fTS_cSaltwJiGsOCc-0DNgpEuKAt5o30Y2OsGe21napN1b9st5XCuYGiBUGMzqUhG4TO7jokAKmJKQPbCxA2Mze-p_sqorLD9SW2o3XLpw7TGfnsJ4pVBtmjyB5Mpwjn4wt3tdyRf9fD3EY0jjceL-foQfZ8CQIpAIx39tZLxJIWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | ۹۰ دقیقه شکوه اسپانیا؛ فرانسه قربانی فوتبال تماشایی ماتادورها شد. خروس‌ها با تمام توان جنگیدند اما اسپانیا برای فینال لایق تر بود!
🇪🇸
اسپانیا
😀
-
😏
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100174" target="_blank">📅 00:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100173">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امشب یامال نشون داد ریس کییییه
😎
😎
😎
😎</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100173" target="_blank">📅 00:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100172">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">۷ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/100172" target="_blank">📅 00:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100171">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
🚨
🚨
🚨
🚨
عصام الشوالی:
‏به نظر من، توپ طلایی سال 2026 به سه نفر محدود خواهد شد:
‏لامین یامال، هری کین و لیونل مسی.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100171" target="_blank">📅 00:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100170">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">امباپه رید تو کاشته</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100170" target="_blank">📅 00:20 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
