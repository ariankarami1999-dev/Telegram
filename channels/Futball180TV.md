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
<img src="https://cdn5.telesco.pe/file/Q9ju-4Oqm_lw00WxzMmgyUZk5Jeo7lqM-ZDBghPgnkcQWI0S48yKFphb9NmxOFi88r2_UaEqKM89SrnTAi7_L5ZIqO5WAXulhtSFVz5wbngaf3myJMBLnXeYRQWGDnYk98crWjMW_aCUeUc94BkyQsqfCMZbdsm34RsaKsckLMqk7Dk8VjOWkb0k73uxK-41Z93f9YtyyfKeDvICh7BOJyawxI8GFNyuoJcneqpCK03vtovT6JbQm1GrpYjPARbPskhMv9gu_zRSL0j1Rz_tLR379R6RxKwbmqyK3tjrjr6LHyKCe0a8XriGEIaiL1VMakWOSi4HRvzJiI24b4pd9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 164K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 00:03:17</div>
<hr>

<div class="tg-post" id="msg-90847">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ با اعلام ریکلمه، رودری ستاره سیتی در صورت برتری در انتخابات به رئال می‌پیوندد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/Futball180TV/90847" target="_blank">📅 00:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90846">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/Futball180TV/90846" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90845">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/90845" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90844">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/Futball180TV/90844" target="_blank">📅 23:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90843">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUC7qs-lCCuVlGLYrbazdTThzJBvJ4T5-w6NK-SeSo8sxzort-0lPqMlUr-ZfKI3boXRJ-voSdWFRQEs7SWioWdEQfdGEA455abZwI-FA01RU4I-oVTKwdhgwcPERGbS-AmEsC-efBRxcHfpycLIPlysy_GOiudigsvKxoY8cyOIDkBjFgHuHblmYQgTD2B_KVZ56-pN29mp0NQHwcCllOJLtRgpvzpAMQBkyvVS2rjnEWT5XQGXYI-MIpfxU8uqsTVQY27y9mLr-1a2H7LOVvAhLdMjUi0mk_lCgg6fInCcUSUSdul8hW6w6JrFJlfE-w7wfc5rZb2amoPrYOnD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ پرز فردا از کوناته رونمایی میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/Futball180TV/90843" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90842">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaTNvaaR8Yf06bPBqLaY2UJfCDExvwofb5vXjD3V9pYPlDc7fir-41EXybzjqJ7kF8BtSNgfQxKntZjsNwaGe6tm1rc39jwvlDXR6tByNlK5tUcUzG36nOzVMg2vDcNuUCUFi6lcT63jdFW5Yp14USuzQSWfLOze2ONrs9DPLtLJUXDVNbmj8goAcZfnhb-dvt1NHamoVu_A5CAuz6tFrfNXQtmiDNjcc4P-IY9PfpPjyB99BrUr6ZSeVQzw0PVgiYfi_xNZ-biAt7ZtyAU7VAsSoda9_QtYPh5DdhiUjPoJkUVJzQCuRLiAWeHmOSyeGAqm85nWIlT5KN_HP7qeOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/Futball180TV/90842" target="_blank">📅 23:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90841">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihfCaQDJkhHgHyvparS-NIjWHzYB5Hi4x7bKNp5ytOjZdD6OuJ-Ll9NyH6AzlCTxOL4gk83Mf_QFkPgvRveUeLyyrEztW7ZVdz7fkkhLygkDRpKlBa_3YpMcI7MO57HcIgLXIQkEH_3WKrBxlaRjwHN3Gd7xiAgfwjuEBOq6t2x6JWRphTWMd-6ESfTiHO6aLuPkiwIDrKBr_TiHd3JNK4Lr1mSrHoKlDtjKswADrZI1IiH2D7qyVkuep7_UPJ1djFIrKKN9mz4YTGOKV8KRKJzk43tZFJCHExjlxMG_326xch7bniCsLsyJtEjDLzy9TUIGoFkVF9jQlzM4WfWHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
14 خیابان در پاریس به افتخار بازیکنان پاریسن ژرمن تغییر نام داده شد
عثمان دمبله تبدیل به بلوار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90841" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90834">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZsglWCm0RGz2-B0EpsrXeaq8Sua5W0QN81nGC5yHEprgnjAygURT8mYfsIooknTA0t6JbzCdfacvZuGhRcyZoR01FshJcaKaA1n4ECboxH_99MzXk3Lc7k6nado0yOAJ2Mh9eQabLez0nxRHMo3bProkF2oRf8k9eMlNviWli4mj95PR1tmhLb_nFM1SgWcgZ1TFa84Uqi9tHPnm_TYaafwdUI8P_CM_Oy0NdY6kh-XWDtWl8t7xNcZHHr1Wk6eoWy_05BcJ4EUsJtrFsZA0UZ84caPVAucpOH4T0VgA7M7e8GZXmhqAJW7GFcYjekHcTzgjo1p3mSCffXveCL8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kaXovYSl6cNGiLvJNAxVaEI7D53lOU78fi0b5-7JQuFaaLy7YbLMHboJP-qIwz3fvOI1fNnUQnzOtb64qEcjFWHWSM64fT2QF7oG3pMoKx7VufcxqeJk0es-Nc2EOeLlJ91W_TqxD-EziPDJuX3HYcDy3kwEbVVEzXg24qNzHv4Xk0Yr_jE4w8DM9g8W2PQPTOe9skYR7do5Egn95xkT-1WZ3rAUTmtnUMmYMEuAtRLVF8qBElh8eko1KR_cGjGoigbl2E07UND1ZDcDz-rTLww_iN3OMBTBd4zrv_Edmw_zemgf0kI-GkN3fS29dipb_g2WFxL-U2-E83lrRXiFxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dAvfvtc2nIe___VywZg5wkQp6ZHfoSK5eGWLyS4gnHrGnn91VilTug6n1EwOOxB8KVlSg3_a2rpWITrAo9ljpBMkxLhJPjTF1CCIe09miyvx7iMhMONdPOz2GRPdrBcEPplUi8wO6TRhHIe-d0SMVrl2NhsxtWzgNNyBR8Vc4AFigNhiD8Uun5RG9jJFYDtPF4WlcFTOQV68AeAXNQrzwl4L8IDNry40qcVl9kgXgtb5eKZtDFyXecFLf1vyOd6mOsIpAnGrt2FVso4ipFCA3fR-VaLDU0tg9V9sW7gH-A4neLtn-yXAVzjlE7E9heMNEBP4DoRLLn5pXGm65G68vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtfsmFrQ-UGiklB7ikfZDwWZqb3iidm5ZA8_v6qewcS-rgE3QgWBwxDO9Kfb51dKi0IgQlcd16ePxx-YjtaTgDg2Rj6LHlrFZ53kjSKVpafnVehk2zqAD3R-miGrRLUGkAS37MUHjb-z-psEdO78R1fzaqaa1ImBGQ54xOPXi6J63jzI5S8Tcl_7YTrqla5T_RPTrm4AkAnP3lbfTruQStN1-KCGhjpElk6RGlMiu6KdIMh7Sr_nmuENmIjuNNvZWeTk_Iqo3YwM0wH1sKoWi2gwuXxEk8mV7PofDBj0jLAYFsLZ5LV_XBm_rjU9z8F5JbeC9TUlgcBxVrR8gNow8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oesGE-aNYOantEkxX-QhyF8151l96hoOjdI1RPzHJOv6L02nHuTokOINJHHxPhSo8onxY_nCYneVWujnZZYDXfhXXoSR8F1nOJ1Sd7P0HN-hD2rt0BdBgjRKQnYtRSbYuEULli0VYMUaPBgRJICpbfZwCBqWQWqaQUUxJk2l6rmrAGiATvkFgC2GhwLz5vnyEcjdjb07vD7PTpRQkZVjgn9bvfVPMzyCrbq1u_5fxu16ayWLbs_3sxuUYQnQsOJr93VruUPnvb97ID0wflCTLFXz1EQCGQm2Pgmjw2KDMP8TxZgkHjbJ27SoQq6L6prdvsC9UcU5nm6eld0ZZS--hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">8 روز مونده به شروع جام جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/90834" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90833">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVZ9pCTdJ-ShqhZkFrmZzxy5MIYPekYDqC2SLS19rh8DgVGslOjSOyWlA_YVKTMz_VWiUMDjesagfp80Jc-1BmwZRnOzFR79xaDEk4HO1Hi7EvcDT47nQB6fIwL-zuRK22rNQxReGlAmjJateH4I9zLa2HHEaHGlcA9C3toVsNvPnq4tTuWzRnjtXH0T1D02GXQlAbt859SbXMrKxA6Xy4i0dgyzHEKA9gvubrMVuz17jrTDQQ2L2qsz7VAjxdBu6RgApcWiBKrBzWS2sDQuh8yAPnuUBxrl-wgp7oCclgYH7iM5Gp1hKspIt2axCRQQFvxCjcltmwhPiRPM3yfB3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شجاع خلیل‌زاده با ارزش‌ ۱۰۰ هزار دلاری، جز کم‌ارزش‌ترین بازیکنان جام جهانی لقب گرفت.
🔥
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/90833" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90832">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIOLbYYsk0pRltWeGBBc-1DuPCuapR9ID_7LKoLD40LBee-XwNRzIMnFGRiq21gRqftw-uesbErPhQP8YatG8PVSTr6oF1aDsgYTwVSrjLpYe3Lfx7cuBHlQY-Sp0FHVfaJ1HTd_HWYSmfuBU3Q3tpFxqmaaH3xlKDdYV7X0oVuv6PBrwN0I2qUvHthz5Kj7j9IOL50sq9HsdlROS_Ac28dGRLyATV7duMQd4il-nirNtV1jmODU3l6EKWmVIoTCn6KGOmslJM9wMS5278296Io-QNXvvZXXpZ6eghVR9kcu_nXRMqmzLe1lxIJxSwDG6D4kt8vqNEfSMzkvEjjr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری باشگاه استقلال برای تبریک تولد فرهاد مجیدی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/Futball180TV/90832" target="_blank">📅 22:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90831">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGub1Zpv_rzO9Pt8piEor8sazV2dqksC5LoUt4qDgVZ6oP-HbBQEN9AocnRD8Vro0E-prPsXMDwKiHsGSGPXiwKVVgIa9r4VJ2GgVAVvPXe21VnWzvI4vjfirCXa2336xjD6K_zo0fzE00XPX43KC0RvlpqRvSPSsTINxhoO1DqcZmJQlisexXv-9MHCOoKvW922QgqfNkOsi-v1rdLuMLPk2YzaAzrYODuuK4m8hwTAwCgLKl3KAkrPlsR50JBfV-hBgHI0FMJwYzd3Jpvg8zcYR2vgtfYtYqD_hypsH6bZM3xQNZ2bqLKnm7zxnUezRhJvskiFTreWQIBJ5pxRPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در
۲۸
بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در
۷
بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در
۱۰
دیدار اخیر اسپانیا
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر عراق
۱.۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/Futball180TV/90831" target="_blank">📅 22:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90830">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWIKzLlmHmL57PixNWDKfULklqpDNLG-M1Eorla9Tq6blYhEDoUF0C8rywUWgsvBlhrzltZQW-tBiWdB9IVppNXldlcr9H4z_Mgidg2zg6TusOwNcuIW4cdi97MOFGy_dZBk61d9JdYgv-23mD9NrR_urRcq93fqZ0XoGJqShrybT-Bkd79xdkuekcL-ckLhFZbt6xALcyutOIMfdnRqJeoBJvSM0WK3nPx-gEU5vo5o2Gh6-in0jX5eW5Km7KaQJB2_vArYMQmbPcmN5bK22Bl3sH27cl9x-ZpPmFYyM3Knaf9uD_GPQMKEPHMVu8QqZflOwcIuzophNPPdqxBmwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TOO FUN🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/90830" target="_blank">📅 21:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90829">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRFqaEvvFCEjCdy7m4PJyP1XcTd1HTYyEsFcitkao18AXYF75EbSYTCzEAwf2v0tpfkY6COoCgIzIMa7Zm5AvN7uoyhk_WryYuC38p0r1BgHMt_F7FKPN_wBT9njm45S0gCJQ9fCZQMKltxEwU03oLX0uKwZgnd6Ok_ZUKyS9FytczIqPRJgaWWV4xALV_OcZksu2hKITHzbRdgT7TJlI_Q5TT0XjXqX86-ytydeoUNflDo9QdbUZIPpWGjzKqN-wqVWjCdSet0y7zeifdwMI0UvtpznNu6g06_xajUsKws8-VI_fOILtk6VHZD-TeEIacREXzvAgTokLFPOdBkLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو: برناردو سیلوا تصمیم‌گیری درباره آینده‌اش را به بعد از جام جهانی موکول کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/Futball180TV/90829" target="_blank">📅 21:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90826">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUGjmjy6tRz6pQdTcwrekSJCDlr0vcdazPhJqroaqTHVDeAn6gsMcB4udu5A-pgUuWxvGGdkbWsEeVDIpMDBihRUwp66dKEIQe2ot7sQmO725L_SyKq23-mysh4sArc1NDa3CRFUM5Lhx3c2KFjWYGTy49AV7aDMfHwmojCXJpzAI49gnEoWqAELtTKhRmfJLEFUTjw5v-YKnWXBBt6D9Oez8lHUavRJ_aAJPCG-raADR0IXhjYfPUNaqKQ3WFhhz7Uzks5HL5KCL8AYFQwx6_ftUTe63Sge_9kth9pyP-KJ8xIvv3Nq3AKgr6b9f8RVXUUjx1yghpxLg51hURH6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSThKHQiyI0dUv8tuXqfX6IVSujRowg8nmQvVwpui1EFasbWIX5qVK1g-OHZ4tFZq7kFAqbmWF6onEPASH2WFeohsTBvS-kxaTIElrcV1YdDDf6t2aM_CAN9cyuLOSVC2UFOrENXlLZ6h4CHY1JBe3oF9dsc2M53KscU_SBiSfWTCRK9_SpwwfGimiF1Ol2T4yR28uh4Yj8wGCx1mhsHyVaVRylinhh6mhD4byKbCQ2rNpAi64nHpgdfNA1sJ8qfoqfT3zIjyZpQj9OdCo0fYvTWQ6udlpgsPYgl74onb_gNU1F6V9RRhNqRl-ViTN-9mFd7I-pKYW1DtB_6DZphmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrHhzmt75_xAckRbMbJJab1tCRzFp9gGr487orzCjUfbVN15bu6--yXaf__-sjtEaFax3gLLwiKFWG9dP8X7kM2w8g-W4GCH1bONmaKr02i9YMWtj4BpcC6s_Ux4mplZtod39NyT6e7YHHKl-YT3VpfdW0yqoDOzM3odWylzJeSLk5V1wkYLruqbQulqbaUNF8md6m7M1EF5A-VLGIxBAto6pv6vvpGPJZFVc2xRSrEO0it4-8l-xTul1-3zKpU8HqRpZzvY2Q7AJVCBAGr2JuG3lL3tvwuQBsQcvPnOITqQhNRLlaDZDrA-gGDpWoW2UxM_333w4WZwmWRDbZ8t-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و حال امباپه و بانو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/Futball180TV/90826" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90825">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
موناکو در آستانه خرید کاسادو از بارسلونا است، به محض قطعی شدن برناردو سیلوا هم به بارسلونا میپیونده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/90825" target="_blank">📅 20:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90824">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKTrDeTWnLXq_WVylAs3YrhxgVlpkr1Dh9akhjg83543HFmjewkb_0C8EF8o41T4IQWJxsLSkKwEQRW0sn8Pfc4XdOpjy1WjSsObXgvIjIzRIzz_xkGYMtjSDW2BnA_npx7AorqhWhdHFFaUbp-uYY_kXJw4nHaSZClYhrop7-MLMQQovoB0ozY7rVnw54S6XitZmMa22ltpBv1gTicyzblQ5VdDWFsQRXE6a3DMZ8liWMWfzMl-N-Y4F52ultRdQjeTyLJxk3Vx76gpgfIKviXBIjiZkGB8q8aLMtbF8QXHhJK97bkN-t0Iy4OdFxkqxnFIfLYN4ssIJu2bkernGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ در صورت منتفی شدن جذب گواردیول، رئال‌مادرید با درخواست مورینیو بدنبال جذب کالافیوری ستاره آرسنال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/Futball180TV/90824" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90823">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=MRjUhCSvwXVnqB5KE6y6AcTr8liY8o354XlsTqhWDAOGTATfhHRJUEHeeDiFAFTiu5EFakPcp2SGBgsGKZM25AT0VJmGN43uqZx5jTYz1VlhfA_S1T7VTym2HPGvB7DMeYB8gui_DEGPMDcrInTbPolDrRAfTGSQWimgxqPqZHSr_x1X4uhdKWnzno4hcNh3TCKdWFNv4_PPnz5GOM1k00wWNNsbp2cUF-MhS4Gy5FH_jDEt2nBkcz8W01TYYVs2uGp6UvNTrhl29GLUci_O2ICXIim_Fd9jgBm48WX8yCrVcRN0sZYy8m4xZPcmE4GmeBI-DpmPqX89zigHZIvmE3AffcZXmzWCJhiLApnIolz1WMJxR5ByLX1v9K3v9BDm9TLVSujT2tUKm2fAOWsfiQnsQDyPHc4yIv-N1txs_q4O8cygP8yPHEAEVnTD-Enb6YL7US6CEuC4jkgRBh-HLDyZAhE2yW4LkBRqNJCK87DeZRr89XAMu4iBfmcdH8yXxvkMcAt5Sp8ro_sUVLc6a19Kx1q1x58zd5VZSNN2jRZumPmX6OZUORsi8ARO8HyYCeAeeOY-KKatIvU8OSN4LTwZvjj5lrHbJ5P8MqBWxCysAMhVxrwE39zki2BjRv84J87d0DWrHr3sN5YXRtglOICvJGTqCEEOqQr7tfz41UE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=MRjUhCSvwXVnqB5KE6y6AcTr8liY8o354XlsTqhWDAOGTATfhHRJUEHeeDiFAFTiu5EFakPcp2SGBgsGKZM25AT0VJmGN43uqZx5jTYz1VlhfA_S1T7VTym2HPGvB7DMeYB8gui_DEGPMDcrInTbPolDrRAfTGSQWimgxqPqZHSr_x1X4uhdKWnzno4hcNh3TCKdWFNv4_PPnz5GOM1k00wWNNsbp2cUF-MhS4Gy5FH_jDEt2nBkcz8W01TYYVs2uGp6UvNTrhl29GLUci_O2ICXIim_Fd9jgBm48WX8yCrVcRN0sZYy8m4xZPcmE4GmeBI-DpmPqX89zigHZIvmE3AffcZXmzWCJhiLApnIolz1WMJxR5ByLX1v9K3v9BDm9TLVSujT2tUKm2fAOWsfiQnsQDyPHc4yIv-N1txs_q4O8cygP8yPHEAEVnTD-Enb6YL7US6CEuC4jkgRBh-HLDyZAhE2yW4LkBRqNJCK87DeZRr89XAMu4iBfmcdH8yXxvkMcAt5Sp8ro_sUVLc6a19Kx1q1x58zd5VZSNN2jRZumPmX6OZUORsi8ARO8HyYCeAeeOY-KKatIvU8OSN4LTwZvjj5lrHbJ5P8MqBWxCysAMhVxrwE39zki2BjRv84J87d0DWrHr3sN5YXRtglOICvJGTqCEEOqQr7tfz41UE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدمممم ینی؛
مصاحبه شاهکار این مرد وایرال شده؛ نزدیک خونش رو زدن و اومدن باهاش مصاحبه کنن
😂
😂
😂
+ خبرنگار: شما که خونه نبودین.
_ نه ولی کیرم دهن اسرائیل.
+ خبرنگار عع این حرفا چیه آقا
_ خب الان چی بگم؟ بگم ببخشین آقای نیتینیاهو کصکش؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/Futball180TV/90823" target="_blank">📅 20:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90822">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=clORdQEpa0vE2F01JEUc9W0M-9aYpgPU4jNPNqMQ95sVM0YDXdtp6RoIyqiY6nNAEDr5vF8c-0upGLgGOT9_oyQEBIosQgxoUwlOpp4c1eaR9JMG5_wRs4YoxeXVOpkz6KP1ZEGzMR80y7LlgWCq8HGJOf_Cg9gsC48hPEz3cUKwnVyWJMrjU9tbQib3LHXMbZ7mG2hQgR8TErCOkOzPNoFsVOKkS3u2Q4ctHAAWS5vSJ7tHg_TFQ4FDbqmKLTQntpW-DV1y7M53nvHTU2nAuJtqw_4aU43R5soPMRHHKgxrFDJaad3haKeaBvlBz4C-rOr2Bu6x_kPFtjdG_r7Hdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=clORdQEpa0vE2F01JEUc9W0M-9aYpgPU4jNPNqMQ95sVM0YDXdtp6RoIyqiY6nNAEDr5vF8c-0upGLgGOT9_oyQEBIosQgxoUwlOpp4c1eaR9JMG5_wRs4YoxeXVOpkz6KP1ZEGzMR80y7LlgWCq8HGJOf_Cg9gsC48hPEz3cUKwnVyWJMrjU9tbQib3LHXMbZ7mG2hQgR8TErCOkOzPNoFsVOKkS3u2Q4ctHAAWS5vSJ7tHg_TFQ4FDbqmKLTQntpW-DV1y7M53nvHTU2nAuJtqw_4aU43R5soPMRHHKgxrFDJaad3haKeaBvlBz4C-rOr2Bu6x_kPFtjdG_r7Hdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ گواردیولا برای پپسی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/90822" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90821">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=Q5j3UW0xyxEk8PGwF2Y_2jCdLZ-AbXu8rpr9BatkTXtXymSD8F5qu3AE9hVNm6XBh01rc6Kac8_dne_NGAUFaNpFkpnF4LaPXsRUzz1RNlrMpZWeZqpdU9duS5fVQZkVH3mwjkTeGcNiT7JJ8gKA5jefQHFEfp_It14c18EnLcZT9XFh0nQA5LJMjvDIoIozlrQox1kKhGaAu0DqD5gtSW4612zET1OPJVK0PcHRAFO68xUN6g0TmskiGquJuQKeKk5OCOpKONvuAdkkd5LQn3pTK83V4T6kMX1RJ0b6EVG82ORXGEa-6RBcVcWHck29yCFtv1S3eqqSXiri2L4bhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=Q5j3UW0xyxEk8PGwF2Y_2jCdLZ-AbXu8rpr9BatkTXtXymSD8F5qu3AE9hVNm6XBh01rc6Kac8_dne_NGAUFaNpFkpnF4LaPXsRUzz1RNlrMpZWeZqpdU9duS5fVQZkVH3mwjkTeGcNiT7JJ8gKA5jefQHFEfp_It14c18EnLcZT9XFh0nQA5LJMjvDIoIozlrQox1kKhGaAu0DqD5gtSW4612zET1OPJVK0PcHRAFO68xUN6g0TmskiGquJuQKeKk5OCOpKONvuAdkkd5LQn3pTK83V4T6kMX1RJ0b6EVG82ORXGEa-6RBcVcWHck29yCFtv1S3eqqSXiri2L4bhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف عکاسی با رونالدو توسط بازیکنان زنان پرتغال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/90821" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90820">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=HMarxRj8nVCBb9VuvR3ovUvoiPaTPyUqDW2V8SJUv-hOhh-E-xD-mLbNqCy4plcUWGcqOcMofgJJoy4PIqPjxoDm_8kQ0knFVsSV8G1dhApDCUxfhJlh42a_D_Mn2YdLqklDjgQoEl90Q-bhCxxtLZklEEJm1v1THbipXmhOQ7AEETJDcxivi19fNWDAcSuQWU7QUtdEIoyIQ5G7ZZowCjvORzjlQFPBzbo8QDeDNY4xELVYvmQ05PsiE-63_-RaUeefuCdr5x0Qje2-9iuvmZH3Qp-hiJvm3hm6R2Zdg-2gcDLuq9vmYUIa34tsQx6xDD1GJBDnUUmBAUuw1C3MeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=HMarxRj8nVCBb9VuvR3ovUvoiPaTPyUqDW2V8SJUv-hOhh-E-xD-mLbNqCy4plcUWGcqOcMofgJJoy4PIqPjxoDm_8kQ0knFVsSV8G1dhApDCUxfhJlh42a_D_Mn2YdLqklDjgQoEl90Q-bhCxxtLZklEEJm1v1THbipXmhOQ7AEETJDcxivi19fNWDAcSuQWU7QUtdEIoyIQ5G7ZZowCjvORzjlQFPBzbo8QDeDNY4xELVYvmQ05PsiE-63_-RaUeefuCdr5x0Qje2-9iuvmZH3Qp-hiJvm3hm6R2Zdg-2gcDLuq9vmYUIa34tsQx6xDD1GJBDnUUmBAUuw1C3MeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
ویدیو منتشر شده عجیب از دولا پهنا شدن بازیکنای تیم قهرمان کره‌شمالی با حضور رهبر این کشور
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/90820" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90819">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNEX VPN</strong></div>
<div class="tg-text">⭕
محدودیتی که لازم بود برداشته بشه برای پایین اومدن قیمت کانفیگ برداشته شد
❗️
گرون نخرید
⭕
طی ساعات آینده قیمت هامون به قیمت های قبل از جنگ برمیگرده
😇
منتظر باشید …
آیدی کانال :
@nexphonevpn
آیدی ربات :
@nexvpnshop_bot</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/Futball180TV/90819" target="_blank">📅 19:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90818">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
#فوووووری
؛ باشگاه موناکو فرانسه بدنبال جذب مارک کاسادو هافبک  بارسا؛ احتمالا بارسلونا از فروش این بازیکن رقمی بیش از ۲۰ میلیون یورو درخواست کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/Futball180TV/90818" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90817">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/Futball180TV/90817" target="_blank">📅 19:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90816">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVCuhY9O6fkLMfaDwo_WI6jSFwjv2OO8KSAFFOyNl5MoPi_0NmF5vYyIGyN08YGXy5RJ9kUnJMKfSJPiOZeWM3bY5tnbxHAW2jv1KY1tySipFQunOC8Bs_xAqjkyLB2o7si_9fdKvOEv4mJEuQmSX_yLe-3C9-2tetyhewR7-syu-fHqM-1opAoga_hYx8CG3Z2pJHC5pt3xucl2RvMyEEZv4Vox5_uG_mqaAfCCNYJ94lOz0hKT_vbDRUoH3evGJR2aYo_sVqBtaF3OiAeiB4kUWVqEZdv8HL78xZASwiUBqO7kNfExSqvga0-L2iUEQRnk6Il-EHlJilVFcbYkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کونده :
«تا سال ۲۰۳۰ قرارداد دارم. در ذهن من ، موضوع تا حد زیادی روشن است. وقتی در اردوی تیم ملی فرانسه هستم ، این مسائل در حاشیه قرار می‌گیرند. فعلاً تمام تمرکزم روی مسابقات است. من در بارسلونا هستم و امیدوارم به حضورم در آنجا ادامه دهم.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/Futball180TV/90816" target="_blank">📅 19:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90815">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تهیه کننده برنامه پاورقی: خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/90815" target="_blank">📅 19:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90814">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8B7lb9jq2MMiaePoXTz8M3JXkb3J8IdZPsYnuREdof2w8f4UWPqgLXYkIJUS1FE77X2qlgZZBVVDUiGJWVZ0NTbJ49aW7vDwP1rTt0i4up8s-R3wSeIpSunJW0MMhQL8tVCje1YlfwGcNir2sBtJgGSSRP_QkVuKRyHecD8t5Mfo_JWZlaJEZ5juM6hyVMPROTyjUDmuoNvtL2ccwg1Dc3JD2eBNOcyMIjvRV8OTHdB9h-LDyu7hIZu_Qi0YiX6jeUyvBGj1KjGOVKJRM6MBwO8Zx6Szrgdj_mvFFYQ_j_eCAqOhSzorJf1Fhd_3UJ9vB5Sn-jkxgDGkO1dhKimPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز هیچکس نفهمیده چرا زبون ویتینیا آبیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/90814" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90813">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تهیه کننده برنامه پاورقی:
خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/90813" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90810">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH7vz_TPnPhWkq3GJXcIc8boXkGekdDgNcZ_pO_fr_-xsTnLrKQUHkxOoUKN3N0UyzG_WNOo_HxF31bPi2k6avRNRuv79ZsGxugZK8wOA8yzo6Yfcl2uiM_-88eZB3aqCjYdE_O9ug_e5uHyfy5AFUdYxMUQJEgRVnG9TP37ZuZe_ytzB33XhP8pVMGDKHPKSJZoWQVtdRpN_8kveEu8yEqG9mtI28qduvIYKqbkJ3IhtB3ALfh0kTrv1HKfG-ceM4B4mT5HIGGPRtI0LPDVDBMmvC7S0GcG20O4nU4wl1q380A6UrO7BAr-9IAoDVkIL6TpSb8YZ_h_3N02B9VvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/90810" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90809">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgUONS7IMXMtHJSuVERvqj1nd4pbFbiULXCwFiZBw2jv_6xkbDi5UommZ4VLG5l5JXNU4-MmztT9DysFn7DmQy9aZRR8YZs5tLQS3QDKWybhFZx_x24kYEzjw68AMSAMYQrYh_jzGbVnt_OK_t10ThUKutrNAgDVvS5j4KJD4UEj2wTCoWicv3PzZ90oWMlWxnXFcIzwRwl8NoLUETdlVx2aXOHq_iVweALYSs0j4VOyJRS_EATzW4mJnicwLrAWYYtCrRo9vbpUGwNiSArZ1gSWizehsf24g6jEzSafniw2bYoPEFfrK8WrRmmiuRnZ8L8ebWu7CI5dRbaoRmOC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل کمپ ۴۸ تیم حاضر در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/90809" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90808">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8q3av08lAIflX-OtTW3NjzOC0E6ywN7sb6gw1s08sa-vCusHzmsnJYFzmZHQvqAM5r3tL1H7NaI3s9xS-A06aa8ATTiVEjH2ERux2P_UQ8yMry3HwhyQxCjfABD7Mo-DZrSXI6rUtd6eFLxAAKp9KeDiwf4iS7OlOacP6-yJRH3sRXbuIFGts2bnSdxHAwPS93sB1JG5-glkd9HZ3fAmiF8fGTmumQKqjSYvVRTyf_72akJiCMxilpT6pUwqWVTMTY2ud85NCzhltgv2ABeVzL-bB-W9xzMv2290PDvJv5D3oyoqojBtWtR15oDF4Hx3HpbBbtG8UmSYKiE04cWMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی و ثابت تیم اردشیر تو جام جهانی طبق گفته رسانه ها:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/90808" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90807">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhjByIHmwxOBnpwB7oqF4LGcdrnuW-sHWLYogvnmsV7SIMKU7CkNtmZN8LIoJX-qfsmWpm0ycCkJa3AXlb-xZcGnqtYv37n9QapiLZ9XPl6NZ1ZXd7vtlAYGAgMGoIAqt_w3ehdWgLzAcBVpxmPQA16twLJMfZrAQkvjEuW-6jLHoUtZ6pXZGikUC14mb7bx2ML13eX5XTsYDYZRUwwm6Z8Goq0sPisya7YCEWLvE8BYPfi81RiOJaMAAsoU0mPylc12xRTuKuS8HbZ3yAmVb12k2ryztdggIKlyr04RXNcCvGsk6Wwp-r8sTUvKusQquDRMPOQoLAFsplh_aKkZTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یحیی گل‌محمدی در آستانه سرمربیگری تیم دهوک عراق قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/90807" target="_blank">📅 17:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90806">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqVsd_37xQm_cJwMumhhM-Sa5FRhawvyEJWRZuHRKOYV7aWiHx16fyi2KkxnFP5ib2IfNAfDkTwTw32T5EAyISmbFRMR-QUCDDxw3xvprwepBbtDfMHcA-UrQPv8SZEgyFfZmir1n4tkWVA1TiXwQ1RL6bbgwqSEQL6WiWHbxrz3q9cHryz6l3aUfVhbjCM6Du2JMSU_R_MyhP57-BEgKWMETX6Hx-MFsYA38BQYI-9TLXsvj0zn_AWGFcFSSOe0rbunK-FOuCB_D1hoU7np4Ccx3evcnn52AcvFpLem0yPgB0CtV_bKAlhvNbjeG4Repu57Z78ASQFDeu4T1X0cFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 مربی سابق چلسی که تو این جام جهانی هدایت تیمای مختلف رو به عهده دارن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/Futball180TV/90806" target="_blank">📅 17:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90805">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
یحیی گل‌محمدی در آستانه سرمربیگری تیم دهوک عراق قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/90805" target="_blank">📅 17:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90804">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-Nc3dFuOba024LTubrf7fLl9rchKpAqUH_Dwneh54iz00qB43DNGzIjyKQFi1U3gOqRQc64IbrvHujTZC86o4VVudQoGh4n4kALrVOKMFIBZPYMmhAOPo27cIpIRB0qxPnGbMuftOEkdIw2rFzbEAVZ31hWbNYXp1sM4qkpbjp4KnRAsAS5TkaA4lilitJhxFSOUZ6IqS7asEgpqMOLfjaCQDPDY3qCX0erOu9Wpjk7OW9bKcGOBJYCF6QS_xUvTN-ylh-x2IqrMIuCRZGpvaUx11IUIfwqFKOONWBAIlG1N673_cr1doWuai2PreCIgTq40gN0LuPJ0vTlMnPrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدربزرگ هالند مثل سیبیه که از وسط نصفش کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90804" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90803">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167838926a.mp4?token=IERyofkGDAi3P0CeliPsrUcAZQZG8-YmXpOPgJV5NpOEuG4EgGXXCmrfKQM8gt9uJDqdZfnTxzZKD-a4slvAq1TmHeTYTfiHWxSTcjShDVBfXwM8jdBSqQYKSkdfatI579DLXV2rz7lwdz9rUo1hIFEGwRP7fU_vCFEKQs8MlOZcqagH0TivF3QNID1pMuzqeAyZUvFdvu6wNxIkk4daVjm9_yyCNS4VFV5TauTYlqhZiGiriGejj4ZRVX4_AtfzeuagTiIe39rnJ2bcwuiznVI0HfuXWCUqqvcmvC6Llhf6KQjESYTlkAXBlc64Eqx41Lo6ilfmt_jrhPlkMOvirg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167838926a.mp4?token=IERyofkGDAi3P0CeliPsrUcAZQZG8-YmXpOPgJV5NpOEuG4EgGXXCmrfKQM8gt9uJDqdZfnTxzZKD-a4slvAq1TmHeTYTfiHWxSTcjShDVBfXwM8jdBSqQYKSkdfatI579DLXV2rz7lwdz9rUo1hIFEGwRP7fU_vCFEKQs8MlOZcqagH0TivF3QNID1pMuzqeAyZUvFdvu6wNxIkk4daVjm9_yyCNS4VFV5TauTYlqhZiGiriGejj4ZRVX4_AtfzeuagTiIe39rnJ2bcwuiznVI0HfuXWCUqqvcmvC6Llhf6KQjESYTlkAXBlc64Eqx41Lo6ilfmt_jrhPlkMOvirg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش پسر مارسلو با رفقاش به یاد پدر
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/90803" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90802">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e389c70190.mp4?token=kP1xRsrPqUF6Tc6M35AV-Y4nbISBUHfTqZzyoBrbpt6k4kds7tlhoR2AWFjq-zA9O0GxuK_6yWyxppLktP_ezOrkNE9iYRW5RF4iaUaP9W5KqBoTpy2vATBzpcx-bOXsrhlFiLRYsp0ygKvogvM5aZxLMxSyqir3JQOF8lmWFecU30CMoPTs1kFdVxE26aksHL_XyiBu_wwzIR3ey-ttH6hn8mngOd__1RooUrUzqbbl1MdYTjiX4MKAfH6SmyDV4LUF3oDRH1mui6WtoGH345JXTw_PcOnnm89RhsnehYF5VqitXI4E1eb5mWTztBxComB9JCMKbiD9jAf6TCrYBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e389c70190.mp4?token=kP1xRsrPqUF6Tc6M35AV-Y4nbISBUHfTqZzyoBrbpt6k4kds7tlhoR2AWFjq-zA9O0GxuK_6yWyxppLktP_ezOrkNE9iYRW5RF4iaUaP9W5KqBoTpy2vATBzpcx-bOXsrhlFiLRYsp0ygKvogvM5aZxLMxSyqir3JQOF8lmWFecU30CMoPTs1kFdVxE26aksHL_XyiBu_wwzIR3ey-ttH6hn8mngOd__1RooUrUzqbbl1MdYTjiX4MKAfH6SmyDV4LUF3oDRH1mui6WtoGH345JXTw_PcOnnm89RhsnehYF5VqitXI4E1eb5mWTztBxComB9JCMKbiD9jAf6TCrYBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
کاش برمیگشتیم به این دوران و این بازی و کلی هیجان و خیال آسوده فوتبال دیدن...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/90802" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90801">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6331bff84f.mp4?token=c-NURNNK_TnFIC5Z48vLKszS6Q6hJ2ITpSmNpHQKwu7dOCgY-6Udcj3nxS4GzwzqA2w7OBv3uoVIKvoWHB2sFmPw1yho1Hb6h3W-0Jt1dQYhnEDj3O34PDmzqaGlF5NYjy7oUDZ8ItB8IXq0JCEQc1bFWGXVvSJcM-mipCD8-ybj3yJCZSA5Bb6G58lQR1wYO2rm3eLJ50MRe5q1LdL9iu1ZYEbdHKDPtJfYc3FmPv239uKA8ZHviv7u9AghOJOWROzvRMt3ja2KThLztzphPcmY-78WNEmTZNSS8OQUoVbMAhjtNPA0BcPfpaM03aUwEl4op6PHqr8fBVazDSu0zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6331bff84f.mp4?token=c-NURNNK_TnFIC5Z48vLKszS6Q6hJ2ITpSmNpHQKwu7dOCgY-6Udcj3nxS4GzwzqA2w7OBv3uoVIKvoWHB2sFmPw1yho1Hb6h3W-0Jt1dQYhnEDj3O34PDmzqaGlF5NYjy7oUDZ8ItB8IXq0JCEQc1bFWGXVvSJcM-mipCD8-ybj3yJCZSA5Bb6G58lQR1wYO2rm3eLJ50MRe5q1LdL9iu1ZYEbdHKDPtJfYc3FmPv239uKA8ZHviv7u9AghOJOWROzvRMt3ja2KThLztzphPcmY-78WNEmTZNSS8OQUoVbMAhjtNPA0BcPfpaM03aUwEl4op6PHqr8fBVazDSu0zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم آسیا موقع دیدن جام‌جهانی:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/90801" target="_blank">📅 16:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90800">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgyyvzh1GaDI8ndcCQcTlLRWJ8Ek9ooUpOESxz0MbZePuv0lPG-thEzZ7WL8PrmfOrqDrTTD9Tl8hpzHkRSUpj6U5PM1dGXFRnTjT7TKirVsTIE8mVNPvIs3RwWqtc6_VRtgN8wIx0yD5vIE5LavVU9Mw1U4xlo_c0oaCFQObHQMMrBdHsW9-R2mcOr9T4Eq7R1s7dKaIqN9PIcF2WCgyDZfTy7aulE3yCnr6PgRsUTGhfyqWVoDAs6vj3HxWZD7UpXU9kQka5NMyKEIl5GJB-qUgrvO7_2Zia31G3yGVJxS9B3Bg8SzxxZyyTEupCURfH9P1cLMvlt5aTSW7s8TQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ایده 48 تیمه کردن جام جهانی واقعا مسخره بود؛ فک کن سه روز اول اینقدر بازی حساسی نداریم که باید 4.30 صبح پاشی آمریکا-پاراگوئه ببینی:)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/90800" target="_blank">📅 15:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90799">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e4e72992d.mp4?token=EA_OXKSWHL4p1m5TM5DjD3fAibJAIM4e9qiHo3YEPr7cvadMEjTVASpiH-Ddj-KU-M183Le3ApQiKPSmbM28cZzLoVti3URESr5jZ8nuuTwcaFuJc9wMq0JIk5pzB212j-pajFaSt9oMYgSpJiSRkQnw1dsLeW-5eOvbR5Z5LnrlXiofgj9-yQeO4E5q1zreTIKsI-BG8JGJqg30JuszrfOqIfU1il8tCcH3p1MnCS27719m-9QHNYZTky9ehDIdnTr084SakhDz72zAmH6QN9zw7NYlfYWKOBsW98vrN64XMr2xLIzSy_sC2zM7DTVBhVDL7Yypaph-uZ3Cn0CLwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e4e72992d.mp4?token=EA_OXKSWHL4p1m5TM5DjD3fAibJAIM4e9qiHo3YEPr7cvadMEjTVASpiH-Ddj-KU-M183Le3ApQiKPSmbM28cZzLoVti3URESr5jZ8nuuTwcaFuJc9wMq0JIk5pzB212j-pajFaSt9oMYgSpJiSRkQnw1dsLeW-5eOvbR5Z5LnrlXiofgj9-yQeO4E5q1zreTIKsI-BG8JGJqg30JuszrfOqIfU1il8tCcH3p1MnCS27719m-9QHNYZTky9ehDIdnTr084SakhDz72zAmH6QN9zw7NYlfYWKOBsW98vrN64XMr2xLIzSy_sC2zM7DTVBhVDL7Yypaph-uZ3Cn0CLwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروز قربانی: عاشق تتلو ام و آهنگاشو گوش میدم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/90799" target="_blank">📅 15:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90798">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRqXOj3W1gYKxlJXr7BxJrtupdNDZnEtgypWaqq6nMQYfKZiPcXICQIhYKkHIEG1ao2uShopIBRIp5VZW0Pr6YAvO8J_IjWGnlr4kmxEEwnfNNhS_EZQ1F6Ra-aVzKTze3MOKGyMOY_r95HyDlvd2-g3Pkfay7--d7bHtIgOE3xpQj3gSCGROaIZZMa89pUsiFmiLVE3nTCB22vgxT0CKhXtvxoPGDrByak0XWm5rxDHwRSTScURdktNtSyd4WiDjdCpaKmyOeyXVS7pkDAv4waNkpWBU8tCOH0dWnZA6C0WYxjIRYG58dEKBWnpevHcXsaBldTrkv-kcG4cFyqfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: افتخار دیدار با آیت‌الله خامنه‌ای را نداشته‌ام. به نظر می‌رسد که ما با آیت‌الله رابطه خوبی داریم و دوست دارم او را ملاقات کنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/Futball180TV/90798" target="_blank">📅 15:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90797">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=cIoMrO7oUw5HLe0dH5EA0Yjn3CA1YbPO6zta6yfox9pXoD2E3dI83EgeQcHS6tEy6Cm934LBo-HQ3ccPT2ajRqa29yDAC-4YwVYuxhz3E2puvKXkU-u6I6QVEYMhsWMVa1isQ6Xbu0S6bDwTwhZOQn09wwhYE8slNC7BnQmL7ItHMwSzSrNu4Ys-K4ZUQ1NmirTcdFPLgMEx-BnKUgG9raN_3uVi3XYb5_mYeuucdBjhwYQvo48mcJ2bIt287Nr1ajTtb664LomonXjLWvSwqI-5l7TAoUiFt3j4SLq9dWFg_-JjR3gEu5O-bk1BAID5NB6Y0EaPwExBnHbi3TWLQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=cIoMrO7oUw5HLe0dH5EA0Yjn3CA1YbPO6zta6yfox9pXoD2E3dI83EgeQcHS6tEy6Cm934LBo-HQ3ccPT2ajRqa29yDAC-4YwVYuxhz3E2puvKXkU-u6I6QVEYMhsWMVa1isQ6Xbu0S6bDwTwhZOQn09wwhYE8slNC7BnQmL7ItHMwSzSrNu4Ys-K4ZUQ1NmirTcdFPLgMEx-BnKUgG9raN_3uVi3XYb5_mYeuucdBjhwYQvo48mcJ2bIt287Nr1ajTtb664LomonXjLWvSwqI-5l7TAoUiFt3j4SLq9dWFg_-JjR3gEu5O-bk1BAID5NB6Y0EaPwExBnHbi3TWLQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردها اینجوری بعد باخت خنده و بعد برد گریه میکنن..
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/90797" target="_blank">📅 15:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90796">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7TgapUx_VyFyPk6QUZWZSJ_Z_yuaaUY7Tksegndhpl4WnPzwmSuPljedGYnRU0V_nXFoMpIgYQzvjxIIzWq8MlteP9ibJ9pyJ_GdqQZXTHH9pY95oq-UHMimTE2CLApxfyYB82jfIWS13b62cV1M6uiDZcHHsN38qvmDsY69BOvB3NeUVpSccMpzikHIeMdedBZu5UDEsXobLhL3xO09btfc-fYkdPS_E_OwtExFzXPZs9dNm5ACtK6h6eHyRH_hrUUlaRP-sDdX4MJBIRxgcjZMIF3iSHwAeTUQi8kv0YBd6rPeQnpySN26bOKBSSRX5gMikyxBNo-orz4ZNQsqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🏆
سامورایی‌های شگفتی‌ساز که طی چند سال اخیر حداقل یکبار تیم‌های مطرح دنیا رو شکست دادن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/90796" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90795">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
انریکه ریکلمه کاندید ریاست رئال: امشب اعلام خواهم کرد که یک ستاره جهانی درجه یک را جذب کرده‌ایم. من به طور رسمی یک سند قانونی الزام‌آور امضا خواهم کرد که تضمین می‌کند قرارداد با او را نهایی خواهم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90795" target="_blank">📅 14:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90794">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=lJtME-WJOZmoNBdb_I-165Sxi1P9zKAEuHNTvnJ-675WX3EvwFqJXrxcZ72xDuUTG2ekrn1iMVZSryfImsTgTq_VdBEcF2FxMUNTjNDXOAkFp4K9p-ExfAsQ6xPrAZgIOF2ZXGIBTyCBr-p__920szK7DKsAc6NJiulQn6CSArfbOWNXVTj-1Dfl37Au9JKd93BBbQLWoGZHimyKPrs5Ee25zCfjO9l7jc58zH7rTBcPYMIpCHajTMKFc0LETyBQTTSNKFHQjDjQFE0E1fZc3Z9dSvbG5XO16zckqW8FRJ13QJ5HF3R98TRQUj5Hq7b4avGrfvHUrpMrL1EaVQKsqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=lJtME-WJOZmoNBdb_I-165Sxi1P9zKAEuHNTvnJ-675WX3EvwFqJXrxcZ72xDuUTG2ekrn1iMVZSryfImsTgTq_VdBEcF2FxMUNTjNDXOAkFp4K9p-ExfAsQ6xPrAZgIOF2ZXGIBTyCBr-p__920szK7DKsAc6NJiulQn6CSArfbOWNXVTj-1Dfl37Au9JKd93BBbQLWoGZHimyKPrs5Ee25zCfjO9l7jc58zH7rTBcPYMIpCHajTMKFc0LETyBQTTSNKFHQjDjQFE0E1fZc3Z9dSvbG5XO16zckqW8FRJ13QJ5HF3R98TRQUj5Hq7b4avGrfvHUrpMrL1EaVQKsqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی که از هم‌باشگاهی هم شانس نیاوردی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90794" target="_blank">📅 14:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90793">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476676c77a.mp4?token=YjK-PJdUzWS5hA5KOUlAJO02V3Os2UcCuOV7IaOygYXq56WlPbRNnIuSSZQVpadgK6dxk6YNOG33Lvti3sQHN4ywt-aRCKi6PD2NdmpK_AS_RqahfoPDeQk_U3VVsurNwhbvd3XMZZQe9-HX2Zwmn-PvFzbk_RijFph2DsBxbGuLwMeSRyeGw8ymmxpMunPsf-Q_KYRuQS8MLq5qGo8Ary4LMH0AyFdE89Zf6FqreUOeWvVcqMaByTVNapr4cp3O7qKINymq6tjcITSB44sUS8z7-viBhUD0B7v8-dLf-nJ9yNBoS9L5bIODYr9KeXP3jyTSeeKSVo_nr-U5oijOVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476676c77a.mp4?token=YjK-PJdUzWS5hA5KOUlAJO02V3Os2UcCuOV7IaOygYXq56WlPbRNnIuSSZQVpadgK6dxk6YNOG33Lvti3sQHN4ywt-aRCKi6PD2NdmpK_AS_RqahfoPDeQk_U3VVsurNwhbvd3XMZZQe9-HX2Zwmn-PvFzbk_RijFph2DsBxbGuLwMeSRyeGw8ymmxpMunPsf-Q_KYRuQS8MLq5qGo8Ary4LMH0AyFdE89Zf6FqreUOeWvVcqMaByTVNapr4cp3O7qKINymq6tjcITSB44sUS8z7-viBhUD0B7v8-dLf-nJ9yNBoS9L5bIODYr9KeXP3jyTSeeKSVo_nr-U5oijOVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
🔥
Colombia
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90793" target="_blank">📅 14:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90792">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: احتمال داره بزودی با آیت‌الله دیدار و ملاقات داشته باشم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90792" target="_blank">📅 14:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90791">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9285a340b.mp4?token=Ve6Sa_x9WaomcgH5R493ZNLBtcYJrAZTf-G1gfDzFcRbNQROl_dSSUR4K7jwSbmqBXLgr6qGUEqzokVEBBX-ewuY2xEAX2wtGp0ImUy-57HVYt8EZ9e6FC-qFZ5UGOAV3dWzuhIG6sxZ1iYJ0oS8HZClMXcOQ6hLb00kL2Uzd15-rYqxkvAahIYLsEoEHOqN5tZo3_jUCOIhFeMbaAUHnjJQF19xn0JzN0-OOI0nGI60BestBiA9KzcTuy41TtLTP8-Jw3LGdPcD967UbVpNgsrw1JEcLXQxAF1isDzAqWufEltFnMPv3cOA6oEtwpCAV2JQ9__-sTg6aBPaw8Ti8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9285a340b.mp4?token=Ve6Sa_x9WaomcgH5R493ZNLBtcYJrAZTf-G1gfDzFcRbNQROl_dSSUR4K7jwSbmqBXLgr6qGUEqzokVEBBX-ewuY2xEAX2wtGp0ImUy-57HVYt8EZ9e6FC-qFZ5UGOAV3dWzuhIG6sxZ1iYJ0oS8HZClMXcOQ6hLb00kL2Uzd15-rYqxkvAahIYLsEoEHOqN5tZo3_jUCOIhFeMbaAUHnjJQF19xn0JzN0-OOI0nGI60BestBiA9KzcTuy41TtLTP8-Jw3LGdPcD967UbVpNgsrw1JEcLXQxAF1isDzAqWufEltFnMPv3cOA6oEtwpCAV2JQ9__-sTg6aBPaw8Ti8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات تابستونی دوستان در بلاد کفر
🚬
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90791" target="_blank">📅 13:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90790">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: احتمال داره بزودی با آیت‌الله دیدار و ملاقات داشته باشم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90790" target="_blank">📅 13:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90789">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw0-W0gFB517NmzdvWH6BZ7aQucY3wd0al4HApoc1o8fqkDQCS7Aui8Voa5DvEsLFlxQLmeKbNlSmlWqBKn4efrRKTo2dcgZCNM-FIuiwZfTLHGt9eFTCvhr2gFqMBnt_QJjpyD8MlMQju0V54QNJTU7zqrx9Nkheu047jHjj1JDFdpgb59Q889lrW9359T9QivCxjimHBZTFSTJ6ZrTBWsPThoh53Qf4yYHqNOVXDaDMtX83n2zhcG8fXrkCpP3_tTUxKnWUMPG4KZ14L7dozZiMPUQk0oWZikLTDAhP4bc_rDLRPqtjkloq9KHYRFPyxuX-HC10-uv2WrCowt6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ یونایتد، psg، آرسنال و لیورپول بدنبال جذب ماتئوس فرناندز ستاره وستهام. تیم لندنی خواستار دریافت ۸۰ میلیون یورو برای فروش این بازیکن شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90789" target="_blank">📅 13:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90788">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJR3U-nZDqyzNTtgUoTAcX8CHV1wSZqRdnq9WtPqy-XsmG5en4GBIP4n1AgqQiD2admcsOK9sxc9gVt8EZ3rZCZz8WA-_g8WQG3_HGDZh5FCRX3aj_BE2YQ3glSrZ1pL1wmUt17iLUru8kZUy9OkaU_I_E_RNfNty2Wb9L5DEl6gMapTUvGpqgUsu3VEeAIosutZXITVUCL-Srba5mQiaa4qmlOGQVmA6ZNvMok1StcREv3wegwIsezVJwR6pBPw__PTzyK_UcB2qejFbf7NB3AcGuodJR4qZvA2UnHa8igikAsfPx5k658kX_z5p4XGYhORDnqq97s8UZYIKFfnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
منچستر سیتی در صدر تیم‌های با بیشترین تعداد بازیکن در جام جهانی
2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90788" target="_blank">📅 13:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90787">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXYHH09m69B0U4eNDf6zFwxTuRauI3gcktBytaP9yuOIm06JPBCokTNZRWewwkInS2N3ZHrxWHUt_TPEMQXff6YlfcDI5wtkjpvvdytD0hEX-2bncsrBv5k6-UBUd4MjsHbJqO3KUTuwTr5zECmeX2ysoVWgQZ7OJJYX4WDmG3ozO0yAoO7YxjK46Xfdxw8qBJh9UhKm0JuQlP6aXwguphUrVsHRJknduTEkxGkazqIzwDXVRKQCyF789e4n9CDq_-jbW3gdUNULZCCQFka4IEfZeM0EDuItG_jcuyEUgbCymGtw9Q9GjqD2TV_dqJ6-aEcF3WaVeUCS2aSyU9jfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام جهانی واقعا برامون غم انگیزه..
پایان نسلی پر از اسطوره و پر از خاطره
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90787" target="_blank">📅 13:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90786">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری؛ ژوزه مورینیو خواستار عقد قرارداد با گواردیول شده‌است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90786" target="_blank">📅 13:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90785">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCxTc2NgsQxiHipLFJSi4wC4AAXXNYpRYhLft84TnFWTUyv4D1Y5kuSelh8z94b-KGVerWAAyaSNclV02mm5AiHor4kx4MkVQLpTzFS2Tp_QC3LecSJQ8NTpYgIR7bous7ivAjAO5Wic_Xoo-D8Pg8MOjeDbRxQ5gaWLD3gEGG_oRZ3T5hufbdRaiCnuLG2WyOY9ROPpI-g7GLN5HcZcUFj7oWsI4Ym1aWKiDGG5a7RIG0220HH7gb5hFECqoexuEzI0gQyMZM1jfY9SjSl-Kqz0ohyIGN5NPG8BWARMClUNbsqdUj75RLdOkxP2SEShQMALgz9lX5atGAXzYyCVUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری
؛ ژوزه مورینیو خواستار عقد قرارداد با گواردیول شده‌است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90785" target="_blank">📅 13:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90784">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJKfRcEmP7pXbpDFOsTZ3ykXzkGRTyemWM_mdcm7X7l7wKDtrAjo0ERMYPtte5ln77dHJOz86miNkrtH1bhAJ9F0l4B2F8ScHOaeZF1BG2dAUqCSUjGknXPoT3ygH3a-mmUXj_kEq2bHHVtqDba9yJGpCp5YQsd1p1txlxKmtajjymWZ1n3IGL1ea0GImKGhsg7lyoxRfCdmvSJ4A7PmZbzTjRFLgNMM0cv1bvY_oA9e1wvczk_M75l1UFNO0Wk9R1cGoLYFn6_pvdLcDvppjfVNXCaPGuzSHc8yaKj85VvJIus8vP2bLnveP2wloM--UGJuQ8AbDBq0oBwwLCLv7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستام وقتی میخوان تولدمو تبریک بگن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90784" target="_blank">📅 12:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90783">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8caed85c.mp4?token=N4K6vOba3Ytfn_zf-Ow5hiZUZCxnOU5CNLypSM5HFOmpwKaBKcQ0b5KJHCihwzZ9pbAKB0VNS5UroUqtVDGkH4m8DqnyQqWhAMlqNF4n5gPZQKhVdObacysiEE_KC8eIuxrHNaCdAh7IJFgP4VjV_0-vJaVS90WdgiRLB-kSKtmz1gCM88T3FOGyTzzMQG5GBzGfI7iIZOQQKKrTezqeX4DHYV5wLSfZu3pndY8bExmvkVLFvgs2PKyi5DL_bLbuxqhS7mkIzERYMNsz6OsXhKKkc1T9mZOeJUKQk_qk31m5hJHJVCsHq1Y86MRconL02SJofrhJxmAoFqn7nkCqOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8caed85c.mp4?token=N4K6vOba3Ytfn_zf-Ow5hiZUZCxnOU5CNLypSM5HFOmpwKaBKcQ0b5KJHCihwzZ9pbAKB0VNS5UroUqtVDGkH4m8DqnyQqWhAMlqNF4n5gPZQKhVdObacysiEE_KC8eIuxrHNaCdAh7IJFgP4VjV_0-vJaVS90WdgiRLB-kSKtmz1gCM88T3FOGyTzzMQG5GBzGfI7iIZOQQKKrTezqeX4DHYV5wLSfZu3pndY8bExmvkVLFvgs2PKyi5DL_bLbuxqhS7mkIzERYMNsz6OsXhKKkc1T9mZOeJUKQk_qk31m5hJHJVCsHq1Y86MRconL02SJofrhJxmAoFqn7nkCqOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇫🇷
تنها تیم‌ملی که تیم‌ملی نیست:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90783" target="_blank">📅 12:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90782">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQv9fX946hV1niYRCW9eAXYRfUEAHEZoAeaGpAZz0kX4ec3cigPdw4zQzoM3SyujqyVbyOyntYTfvyzYOM3ORkaod3b1PsOhc7H6Z0sfbWVcDkPWRSTm5HUnzX8-L6_8D4AofvilRJ5k7nh4kDRUXJdUFa-XcdottoxXKhYPbJcRWJH_4NQYcfoCIcZzXIE7TT_5mloQK9X_3Ftafn35JuVFE7ljtaY6H6_sRbLcxkxPs-Q-Qcy0Ynm1YF3-TjwUQedARIHS_y4wadLCmXFnRpukXix-2qjyNpkzw6gNHGZgoSs0HhXxMYtnQtiusSunh_qSbwzE6viGKCHoRMaDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پیراهن اول رئال مادرید برای فصل 27_2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/Futball180TV/90782" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90781">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c9a85cfef.mp4?token=Zh6UdityDVCyyTBYzc5yv0IyBtnXHD4_HN1FenXrsVC5c4cvVLXSsPbFksCFUpBK0vUqx6Cjsx728TXz66jETdkmfkTauiROn0JAMVGjU7HORLfb6hbVTOixwnVqGuKMS8JhLWsdIv2x-s3ThdISyDnLU8TCG0kl9JauUIWYvz1yXiZt_NsAH6nUk3GXIx7PubVsSEinkzhsdKDLyaTVK5ka_hK80AKSmUjH8iE6dYanX91DAqtGCyGdlGUTYqubqs-ltYHHLNxAPm6GX8Kl33LMUSM6_bGl7q8jUen8fwVqUNoPLF-g1YVORzOOdzOu3aMpR8jLolcMFBYl9i7rwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c9a85cfef.mp4?token=Zh6UdityDVCyyTBYzc5yv0IyBtnXHD4_HN1FenXrsVC5c4cvVLXSsPbFksCFUpBK0vUqx6Cjsx728TXz66jETdkmfkTauiROn0JAMVGjU7HORLfb6hbVTOixwnVqGuKMS8JhLWsdIv2x-s3ThdISyDnLU8TCG0kl9JauUIWYvz1yXiZt_NsAH6nUk3GXIx7PubVsSEinkzhsdKDLyaTVK5ka_hK80AKSmUjH8iE6dYanX91DAqtGCyGdlGUTYqubqs-ltYHHLNxAPm6GX8Kl33LMUSM6_bGl7q8jUen8fwVqUNoPLF-g1YVORzOOdzOu3aMpR8jLolcMFBYl9i7rwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇹🇳
این دختره که می‌بینید از بیکاری زده به سرش و رو قهرمانی ترکیه با شانس یک درصد، تو جام‌جهانی بیش از ۵ هزار دلار شرط بسته
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/90781" target="_blank">📅 12:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90780">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0dddef5c.mp4?token=OTXcSxrbF1jTpCnU2pJpM1S2U2Kn1ASttmv_0XFWmTuYecEqlX8NCPuhaj-X69n2InfkOeadAQRrPIde6bQ-uHyjrEqjgH93pSO1wB67h44aBuFnZleWohtz4TFy1RVm6z5GFjFhDddW8ZqTzwWEmy5He5t-1As424Z9mJkANtbx_gzJYUWpXG_tMfgA9Q5Wj322vz1iHHKn0dqNxGXrRdi_ZFYPVkKCg5rGQqHCCgXi-PVg3e1ImesCQSZtF4y15aWQGHbGx4tRxsnbdDJ-36r0N9CM7wrSYINWOE6z6sUvdRPtcdFnrG9wp1FuQyYWFi1QpitIeW7Am4pwXCG5Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0dddef5c.mp4?token=OTXcSxrbF1jTpCnU2pJpM1S2U2Kn1ASttmv_0XFWmTuYecEqlX8NCPuhaj-X69n2InfkOeadAQRrPIde6bQ-uHyjrEqjgH93pSO1wB67h44aBuFnZleWohtz4TFy1RVm6z5GFjFhDddW8ZqTzwWEmy5He5t-1As424Z9mJkANtbx_gzJYUWpXG_tMfgA9Q5Wj322vz1iHHKn0dqNxGXrRdi_ZFYPVkKCg5rGQqHCCgXi-PVg3e1ImesCQSZtF4y15aWQGHbGx4tRxsnbdDJ-36r0N9CM7wrSYINWOE6z6sUvdRPtcdFnrG9wp1FuQyYWFi1QpitIeW7Am4pwXCG5Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بسوزه پدر هوش‌مصنوعی که مردمو از راه به در کرده
😊
🎧
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90780" target="_blank">📅 11:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90779">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1b77wF4xLFLxk5RYjV4OoJxSIAo6JTaHib7jf_3hZLcvXFAuh3fQf259CB2G6r0O6YxH5UbBTmzlKqMVfUipgQJ_0a2Dmhlnu_2QkCnvM9gMSQTU1efQV2HDSv4kamZ2fvZycM8UaWWNCzxp-Reg_z60P8qcEnYzi-VWRtHTpPNknjcE0HoJWo5DBtr1FqFT08DCpRpOau6JLyrs4MkKZcl7SPdbhSshiVLSr-MKTyZ94WPgcJy2JTPUvHqSL1GUPnu_ijeOrlnJkgCNErEbvsje6Cmsbq53RtNoBL_PHDdm1GP2UMUm9DhTcx82TWA5o7tIG5dm_oIw48dD1LlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
توپ‌های مختلف ادوار جام‌جهانی؛ پیشرفت تکنولوژی قشنگ حس میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/90779" target="_blank">📅 11:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90778">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d071cdfe94.mp4?token=Jq9eOuA8sqmZa1AkLjQaAdlu96T5T86ir2WOr7QEppTJc0DxNNXIkF6vz49ELLgmggXpyyH1isSQkax1C8OBw-5MGYBdoFXqx6uGQ_8Eb-hW1J_R75jWkDGujr6BVZoHm_A731i1TwMf-lVs0ipgdAScesTtS5Ggbd9e05T3SXH22HbWe24vBMu_CzLOYhAvdaKGkQGmm1jQIXsizCHCMJ0wDgqs5xSj32kd6_RVailXbNMBdTQNcxJnYod07aIpNXPoMu1cR28qZ5nTPCM0X97J_p0CimU_EGq00m7jKbIQzyKhOIVJyDK9aYUR0R70TkrZEEDkhOjWY36qNP8aODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d071cdfe94.mp4?token=Jq9eOuA8sqmZa1AkLjQaAdlu96T5T86ir2WOr7QEppTJc0DxNNXIkF6vz49ELLgmggXpyyH1isSQkax1C8OBw-5MGYBdoFXqx6uGQ_8Eb-hW1J_R75jWkDGujr6BVZoHm_A731i1TwMf-lVs0ipgdAScesTtS5Ggbd9e05T3SXH22HbWe24vBMu_CzLOYhAvdaKGkQGmm1jQIXsizCHCMJ0wDgqs5xSj32kd6_RVailXbNMBdTQNcxJnYod07aIpNXPoMu1cR28qZ5nTPCM0X97J_p0CimU_EGq00m7jKbIQzyKhOIVJyDK9aYUR0R70TkrZEEDkhOjWY36qNP8aODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
▶️
تکنولوژی فوق‌پیشرفته توپ مسابقات WC که دیدنش خالی از لطف نیست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90778" target="_blank">📅 11:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90777">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omTSh1xX5eiYTYMsJQET0THh2CD_uny7BaFTqPuQUPjg4ouAXtO1ylwdMLRjz2t7GvIuyv1rWeyfJ_do8O-SidIyqiIvcegrwPlSL_BpJTYE8I60fLhdJXb-rG6rfAGaMsIFjRQdPru9vi3FHjUc_bS8kQNI-MzrcSI_24BrzyYoMc0Ow5EbkB5qoH3FiRo5oiSDaw6QFmzOWjNzK-hkOeCkqVB7FdGOjyzEtDCUDxPB9CA9G_n0LyifJhQs6jCNsjWggSa9gaX_JJG7NRCpGQNwIxthBz6ULuwY5P_5E-m48cEq09ICAq9N_7HmpgRBW8q169WiuTGMfLOmRm2o9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
اطلاعاتی مختصر درباره ورزشگاه‌های WC
😃
نیویورک/نیوجرسی (MetLife Stadium) – بزرگ‌ترین ورزشگاه آمریکایی میزبان و محل برگزاری فینال جام جهانی ۲۰۲۶.
😀
مکزیکو سیتی (Estadio Azteca) – ورزشگاهی تاریخی که فینال‌های ۱۹۷۰ و ۱۹۸۶ را میزبانی کرده و میزبان بازی افتتاحیه خواهد بود.
😆
دالاس (AT&T Stadium) – یکی از بزرگ‌ترین ورزشگاه‌های مسابقات با سقف بازشو و صفحه نمایش عظیم.
😀
لس آنجلس (SoFi Stadium) – جدیدترین ورزشگاه جام جهانی و یکی از پیشرفته‌ترین ورزشگاه‌های جهان.
😄
سان فرانسیسکو (Levi's Stadium) – ورزشگاهی مدرن در سانتا کلارا که میزبان چندین بازی مهم است.
😃
هیوستون (NRG Stadium) – ورزشگاهی کاملاً سرپوشیده و یکی از برجسته‌ترین ورزشگاه‌های تگزاس.
😁
کانزاس سیتی (Arrowhead Stadium) – مشهور به جو پرشور هواداران و رکوردهای تشویق قوی.
😄
آتلانتا (Mercedes-Benz Stadium) – با طراحی منحصر به فرد و سقف متحرک، میزبان نیمه نهایی خواهد بود.
😃
فیلادلفیا (Lincoln Financial Field) – ورزشگاهی مدرن با جو پرشور و موقعیت برجسته
😏
😃
سیاتل (Lumen Field) – یکی از بهترین ورزشگاه‌های آمریکا از نظر حضور تماشاگران و چشم‌انداز شهر.
💥
ورزشگاه‌های شماره ۱۱ تا ۱۶ عبارتند از: میامی، بوستون، مونتری، ونکوور، گوادالاخارا و تورنتو که همه میزبان بازی‌های مرحله گروهی و حذفی در جام جهانی ۲۰۲۶ خواهند بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90777" target="_blank">📅 10:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90776">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ntbTuin4LitTVwa8scFjsdJxQGJPc3-t4XCUrzxWPWYxXaYJo47avAGymWa4yegXfOHznWnrzfqFOQw8Narea6XlLFzsvXPuk_iJwpa2UvnvA9LcBL0GDIPKAwZ3-RS2NJyiGGecl8gZ04FNsJUbnwQXnFotejk2wg1VKfAal-ILoTFZbtN4JP-JhlMXc8ZcFEDY4vmX8oLD1yejdy9QmtVpTm3kZ1GoNK1GRO8rx_xDw1XKmubJCfJI449ogqXdq3lAIbeBmJvCkVA5l7i25OCf3ZPFckcsYnuKBbNBNhMEJ0T5Voiyh2gi9hmo_AOV1P2pkGHM5odDmxjG3iaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرز : فردا از اولین خرید رونمایی می‌کنم و همینطور این هفته از مربی جدید رونمایی میکنم، این تابستون حداقل ۵ خرید داریم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90776" target="_blank">📅 10:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90775">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f607323bfa.mp4?token=bvbAU5BpEqzytHSOy5NYEr4eRnyt1brUKF1MbLqDA17RVoXHYlHRyGSTC2lIERSpYU2AW0l31sFJNkWVQRFxTZzh0BCl5f2VCHLB8bNDt_l8kyCJeTsa79XtJ8eo_5LjoWfg4u3eI5R7RKYXuOPrpXog4HhPJHjg6eynqoobMaKqEpQ8kX2Flv7VOZyyyA_d1ca6APbnjpK7n3dOBUPoFiEbQ8aF_K-BVNg-rz3omLwxTGBz1T9sSR4epVAzNjcJsxgWz0qoP10beDKfZaQYm-WkF1iK7IAn87mQ7AH8sloqI0_jY0H50TJhjiXmdKNofJuaaOvTuT_jgW4tzJPBxQrGT_Rv4KlTv7xe-Qn8nPp1jvv02O5xDo4OJLXFVFMLa7OJ3StDCXbAghV3zZx9Vl7eZQv__66wWZxLumixOQYxG6DL8vi_149fgD9jfrVIPeFNrKE4Bzz2Hov7aKi3GwAvQ0JuOeQRZ-o3eY9eaQPHUl1GAt5CgwmAewoy44I0JLd6W7YDQzS9S3QlBt778THYOqO29pCxBplIq82bAUZGv71bEGhrjAhhLsWrDO6Eh9jh87b43uAbVFkhy1vDEEIWuM6tvWwoKTt8A2Qwz1lqn76EN6aG7r1U50QLAqQ3I7g2lCr9MAeRqXCgLMkas14kQgcF6LDkX5DieGBPMdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f607323bfa.mp4?token=bvbAU5BpEqzytHSOy5NYEr4eRnyt1brUKF1MbLqDA17RVoXHYlHRyGSTC2lIERSpYU2AW0l31sFJNkWVQRFxTZzh0BCl5f2VCHLB8bNDt_l8kyCJeTsa79XtJ8eo_5LjoWfg4u3eI5R7RKYXuOPrpXog4HhPJHjg6eynqoobMaKqEpQ8kX2Flv7VOZyyyA_d1ca6APbnjpK7n3dOBUPoFiEbQ8aF_K-BVNg-rz3omLwxTGBz1T9sSR4epVAzNjcJsxgWz0qoP10beDKfZaQYm-WkF1iK7IAn87mQ7AH8sloqI0_jY0H50TJhjiXmdKNofJuaaOvTuT_jgW4tzJPBxQrGT_Rv4KlTv7xe-Qn8nPp1jvv02O5xDo4OJLXFVFMLa7OJ3StDCXbAghV3zZx9Vl7eZQv__66wWZxLumixOQYxG6DL8vi_149fgD9jfrVIPeFNrKE4Bzz2Hov7aKi3GwAvQ0JuOeQRZ-o3eY9eaQPHUl1GAt5CgwmAewoy44I0JLd6W7YDQzS9S3QlBt778THYOqO29pCxBplIq82bAUZGv71bEGhrjAhhLsWrDO6Eh9jh87b43uAbVFkhy1vDEEIWuM6tvWwoKTt8A2Qwz1lqn76EN6aG7r1U50QLAqQ3I7g2lCr9MAeRqXCgLMkas14kQgcF6LDkX5DieGBPMdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
مکزیک، یکی از میزبانان جام‌جهانی هم حسابی با این طرفداراش خاطرخواه داره
😂
😊
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90775" target="_blank">📅 10:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90774">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c4dc141e.mp4?token=ZXXgxoWLgmOYmNg_rv3sVt6iP-jvOAYyFA2kRyDU549IEXB2RounHfr24ArE_KPR9bcH0z7Ps7LQqfASsx100UierkzUpYaQaPm4xpWEpMRz044241d4VFRdelXGIMxQx4mGCVMGnevzEGqJwdPcV3uHGWWCtV1BlwdW5ZLLs9NUOGpKGLT9Ue2CURum54kvTl06r0WgHm1xSaHqZ5QKDvILppKjsbAO_xC7X0YjO6oGyzQlw9Dd6kmsHZaZPeM3wj_q2sYzTjgQNPSJwWa-bRlQ893-TDP0uRREQhNp7OBIAVPjO8_MwEm4DduYD0OIoX97xMeLH_gaQsu52Eju4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c4dc141e.mp4?token=ZXXgxoWLgmOYmNg_rv3sVt6iP-jvOAYyFA2kRyDU549IEXB2RounHfr24ArE_KPR9bcH0z7Ps7LQqfASsx100UierkzUpYaQaPm4xpWEpMRz044241d4VFRdelXGIMxQx4mGCVMGnevzEGqJwdPcV3uHGWWCtV1BlwdW5ZLLs9NUOGpKGLT9Ue2CURum54kvTl06r0WgHm1xSaHqZ5QKDvILppKjsbAO_xC7X0YjO6oGyzQlw9Dd6kmsHZaZPeM3wj_q2sYzTjgQNPSJwWa-bRlQ893-TDP0uRREQhNp7OBIAVPjO8_MwEm4DduYD0OIoX97xMeLH_gaQsu52Eju4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بهترین‌گل‌های جام‌جهانی قبلی رو ببینیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90774" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90773">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ae696fa.mp4?token=a1LxW6aMLeNI-N1IsMlxznQvj1lTbQhc6Do95j08wquP1g6wJn9ajaeL9P-xYQxaOAq-m0BK1PrEjdb2LqRypU30VhJ8CS40tLGThmu8nh_PCI9PxuEjB8F_DiOXoihFH8ManGZPhk3PTxxe2lOkz-O5brWCfAoMYRjNIC2qVI2LaX3Bir6HvNb73gQMTgcdd4N8tV6B78SsU8NoApwOs84lj7AocpcmZrV81IcfMbU3LotjwPgOoEJyDTs99iC6CHBCiZTARhGLpMHYYfB7hunPSobfkCPdxYemyttdH7xierOsZOT-D93EGWzb278etcwPOUnCCQkAnm93itChZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ae696fa.mp4?token=a1LxW6aMLeNI-N1IsMlxznQvj1lTbQhc6Do95j08wquP1g6wJn9ajaeL9P-xYQxaOAq-m0BK1PrEjdb2LqRypU30VhJ8CS40tLGThmu8nh_PCI9PxuEjB8F_DiOXoihFH8ManGZPhk3PTxxe2lOkz-O5brWCfAoMYRjNIC2qVI2LaX3Bir6HvNb73gQMTgcdd4N8tV6B78SsU8NoApwOs84lj7AocpcmZrV81IcfMbU3LotjwPgOoEJyDTs99iC6CHBCiZTARhGLpMHYYfB7hunPSobfkCPdxYemyttdH7xierOsZOT-D93EGWzb278etcwPOUnCCQkAnm93itChZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پنج سیو برتر فصل پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90773" target="_blank">📅 09:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90772">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fh0FBoOJF3cW2UZ25b9DcXUm0iHeBbXIlfIBMwbqb-V7RlEm9KMcPK__JmnefHKw0ru2qm7uWYxX5RQeff_-yx42O6Pfw3_rwn73RTbnj-UFGE0_xxdAhAsV1JTmfEo1-HpQIz27AK-PClQezJ2p0B0MxzqGAEXMUR2APd_QgqVdC0aqOhKqKPq_oLB8OLZYW3rYT6UsPR3BPFfB4LsWAtZonbW0ZcwvWoyKcVw-hgG6IOERs8vNy1IYMMd8J38mWIGKIiYg73i_EW2JT9UZO38bmVIs13j53P9OQVsCdvJtFkp712Nbiwk05tXpIY5VUKW-7Labql76KQGPrrl_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🏆
۱۷ روز هیجان‌انگیز و متوالی که هرشب تا صبح فوتبال در پیش داریم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90772" target="_blank">📅 09:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90771">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLwcfl-bl3xAbkolsPYoGcMRf4JHegS9zabFdk9hEaoeKZumbC5XxEduXO4vNuNOyq2BCY_x9-H905CL7_abIgPgXG7idFsrNFVDqFovkinlOKT6yFIGmJTr46sN5AqvJajNJuMGue0tL-MEHIRaqcVBC03969y0WLLiUAqc9540c4Tk0nWIQopsKJSC6OhTjwJgZR-irWDMY_NcPZc6gPHqM32C9O79Zv-nEaX5_WgEa4uWuypy7cdWnyr6J_rTVKoH8JxUzdZJSfiDJOvZq3JpYsSPklmxcOy4ic5shuGAfQGdEydBKu5mcHaDYtdt3szTiPcWhUZ8Te3Pu9rLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ اینتر بدنبال جذب دنی کارواخال برای جانشینی دامفریز
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90771" target="_blank">📅 09:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90770">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ولش تهش هرچی شد، جام‌جهانی رو با اینهمه دلبرررررر از دست ندیددددددد
😍
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90770" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90769">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b603dc908.mp4?token=k0NvxG2ia7feD-Mi4l7TuvxWomkcJzvcfsmU_B7CESeLpJo14vRmMe7ONnPU5IdQqiE__zSvT-eQcQ7-C4ecdMXTLORtV4eZG6tThTWHY6cAeq5ClhbANN4ZwLYfH2YjJpwOYjvHArLydSpG5B4-1xdW_UW8KljQtGRuu-aVpRZbGqbZrjhrWPhne_-eeusUrMZzpROJOwmt-0YQP60qnMDGePs0I_hdXQ9SfX87AUCZELCNJXCa67yuwAYmeU5GVulfEicyKSWhn-ouWbW2pgLHEHYH_TevldGGhzliLOrfWFjYC001TEECtlxWarA_CoSVXoQhi5PodiTkFSiqTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b603dc908.mp4?token=k0NvxG2ia7feD-Mi4l7TuvxWomkcJzvcfsmU_B7CESeLpJo14vRmMe7ONnPU5IdQqiE__zSvT-eQcQ7-C4ecdMXTLORtV4eZG6tThTWHY6cAeq5ClhbANN4ZwLYfH2YjJpwOYjvHArLydSpG5B4-1xdW_UW8KljQtGRuu-aVpRZbGqbZrjhrWPhne_-eeusUrMZzpROJOwmt-0YQP60qnMDGePs0I_hdXQ9SfX87AUCZELCNJXCa67yuwAYmeU5GVulfEicyKSWhn-ouWbW2pgLHEHYH_TevldGGhzliLOrfWFjYC001TEECtlxWarA_CoSVXoQhi5PodiTkFSiqTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولش تهش هرچی شد، جام‌جهانی رو با اینهمه دلبرررررر از دست ندیددددددد
😍
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90769" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=LnC4gbDU20YtA9DuSacck-vDDbXwBwjgAbajPVaB0ZcpD4blemV-8XiKoZ7dap5se1empPZOJXPe4S16yoJhhQ4ePHUocOwOikTLF38BNu1PgzQ--e2iuMJfo0U_sl3Do462J0RTJvOsZ2Qxew_r4-B-hLbtORA6vYyeDW5IYHAyIbyHKTtQRCKpGZ8B9H54nUp0ZEupHNoA3L0z_Ux_7h39ks3jWCECbgChe9JAWYidLpILlpxGsVsuF-YZ0AFGkUg31MfmC-xsAxYI51caIqDJ3eyZ6_GRv2uYoYd38oYgrN9Nui4zh01a22_sdqww4W0FXd-jpr_mxtFfl2t4bkOoF_XK1Jmm1hkKAKgSEzrsUX53YBXQ_NJlo_iN0pxFa1Yx5Xv8PVrRhWg2wN-GeuTR7Y06p8nTfhi0MZaRqbz75DA7bP9GaZGm2TQPTswc3_EUqAcJ6hsXBd5n8nhFepjTwIlJFziQbXohx-b4D-9n6b7Ws8UQTZhJhvcniB-4fOnrTcw8quORqTLtyzsfS81LwLYLQgXbati4t-zP3S8Bu0leSVVAOH_S8lSOXoaKhdWW2KHmgY7XMiwCBe2mJf1P3vgH7zpmIPqm5-6G8BEZI4cgfJootP_RzycfEsIYCDZZweEeHk_cpZa86CwbLvRZkDotMT_kxv-uWEI0oLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=LnC4gbDU20YtA9DuSacck-vDDbXwBwjgAbajPVaB0ZcpD4blemV-8XiKoZ7dap5se1empPZOJXPe4S16yoJhhQ4ePHUocOwOikTLF38BNu1PgzQ--e2iuMJfo0U_sl3Do462J0RTJvOsZ2Qxew_r4-B-hLbtORA6vYyeDW5IYHAyIbyHKTtQRCKpGZ8B9H54nUp0ZEupHNoA3L0z_Ux_7h39ks3jWCECbgChe9JAWYidLpILlpxGsVsuF-YZ0AFGkUg31MfmC-xsAxYI51caIqDJ3eyZ6_GRv2uYoYd38oYgrN9Nui4zh01a22_sdqww4W0FXd-jpr_mxtFfl2t4bkOoF_XK1Jmm1hkKAKgSEzrsUX53YBXQ_NJlo_iN0pxFa1Yx5Xv8PVrRhWg2wN-GeuTR7Y06p8nTfhi0MZaRqbz75DA7bP9GaZGm2TQPTswc3_EUqAcJ6hsXBd5n8nhFepjTwIlJFziQbXohx-b4D-9n6b7Ws8UQTZhJhvcniB-4fOnrTcw8quORqTLtyzsfS81LwLYLQgXbati4t-zP3S8Bu0leSVVAOH_S8lSOXoaKhdWW2KHmgY7XMiwCBe2mJf1P3vgH7zpmIPqm5-6G8BEZI4cgfJootP_RzycfEsIYCDZZweEeHk_cpZa86CwbLvRZkDotMT_kxv-uWEI0oLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اساتید یه چنتا موشک سمت بحرین و کویت ول دادن. ایشالا که دم جام‌جهانی خیره
😐</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90768" target="_blank">📅 02:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90767">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این وسط که احتمالا خیلیا خوابیدن، دوباره خاورمیانه قهرمان درگیر آتیش بازی شده
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90767" target="_blank">📅 02:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90766">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این وسط که احتمالا خیلیا خوابیدن، دوباره خاورمیانه قهرمان درگیر آتیش بازی شده
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90766" target="_blank">📅 02:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90765">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">💠
سلام دوستان ! اسم من مبیناس صاحب کانال مبینابت
✅
👌
💠
اعضای کانالم روزانه 3-4 میلیون کسب درآمد میکنن
🤑
💠
میپرسی چجوری ؟ داخل کانالم عضو شید و شروع کنید
🔥
https://t.me/+vt7V5iY0jVhkNWU8
‼️
اگر سنگین شرطبندی میکنی عضو شو آمارش فوق العادس
🤑
🤑
👇
https://t.me/…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90765" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90764">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOM6GQlNmkZjjAO7bctlHoDQ1q3B3U7oXKKuEh8g0Mh1HBYR203GsKFFNZsYScc-uN2i9DlvZSPJTqVgDXOCzZIVT2Jdqq46E4-zReXG6eK50b3C8Xd7DC52faINFshKfN666rbBHb0HNUAs3tR8fdvQbsVdk9GXtVcCdc2snJv5unoOodN2tFF5XMpsUcOAmO8DJYvUUttsFsivFcLRlswfZoDUCMlg4m3DcP1J06fr_BQofqmXik9PhpTfTWA_RQoHU7QTG98g4x31g9Tc93lriHAYR4pHlGTkpma8KaSbOK7gZnpDXauX6rnzyLBcjMRbz-FKLADXkl5G9LAa_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
سلام دوستان ! اسم من مبیناس صاحب کانال مبینابت
✅
👌
💠
اعضای کانالم روزانه
3-4 میلیون
کسب درآمد میکنن
🤑
💠
میپرسی چجوری ؟ داخل
کانالم عضو
شید
و شروع کنید
🔥
https://t.me/+vt7V5iY0jVhkNWU8
‼️
اگر سنگین شرطبندی میکنی عضو شو آمارش فوق العادس
🤑
🤑
👇
https://t.me/+vt7V5iY0jVhkNWU8</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90764" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90763">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2rvCV7rKD8fTgHORh8CA67HPThenkAxw2hseny2nj62Rq9_jdg7ETuKwqKd4-qelUwN7ovizRnhKdzjFBZ-sNZoe9OcGnOAD2tjeIpxc2N3zFrgW-U6XE3-yu_6qXn0Qk2OPM2S_mm7gdkkcmGz1PRZDLVL3DhZjn9FUBjCjq8p8Nxdx9an9E1S7F6GxCAlwL5hwK4t-T5OwvZHRmtO9SXvTog9EVmdvpwdu0Kpbuvp1svhW8pB3O1HP2SXnYatkmAMyacK32bA-C02N2ILalIBgrrqAQBqGkQnx_rpgaQ5DsOpfHLVLsirFJKw2DhlNQS39oQ-mB91ZEmmBR8XqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مودریچ، رونالدو، مسی و اوچوا از جام‌جهانی 2006 تا الان حضور دارن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90763" target="_blank">📅 00:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90762">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGtiztD0CDOjabpnpYff1T2TnqFPqMIqzl1x7oh6-YKLfXEP7a_LwCTQztFQyeAleYCh1aU4zoAWAFAA3BgHZ0tjtJ1klN1qwUbwcJ2vWzTB71Vyyeys0TXQnhQfiRfzBJXMG5QqvG0FsHdSE0oNKIjeWWvdj1HGSxyVnVBuMv5cgVX7dhkxHjSdTSirYqTgXrM4Fd6IDpg1zGbFCOD9cAjtxocC1txjHJKm9kbDRQXztzKJP9jDtugzZf_wDzMUUX_FHTVWCZUZMf9cHtdQMoQ4XAPfrEcsQBspr_YCGwQ3fzJrn1dxxql7cOljNAtHWT9Xh8OqCgDumPBztMVtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوووریییی رومانو؛
دنزل دامفریز به رئال؛ 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90762" target="_blank">📅 00:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90761">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tse81M9xx1_Ljue2fwVxoD61nUMOFogw2QMhELASrp199J4OCg8v0LdG00ybtqJliQrRTLncWh3__UbhgiYqFd5R8T6R012qV8x8qtSfohb6MX-xrQz-CAMYTHEJD2EuvWef8TTrO-fLRHE6dpKs6RPNtpdB7KDJmDSsY0SHcZOhhqhfwCxD3_InHlZNYxgMo7e7IMsl73qciKjXYhPXqr9PRBTdiD8TnwG25VbDKWxt1bLmsN-S9B_E8USrjpiCauCO2sUamDkm2EVv4kPWnhhLeO7oONzW5hJfZqAPY7GYybhD8ZAb22RhKVZJ_z3aIaCNM6bWpJY2BrKZh-tZfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولدت مبارک کون عزیز
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90761" target="_blank">📅 00:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90760">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xrz5bzz9jAwS7PRVFAHdsJHE_E9fHDC0bXML2-sLWzyayZwrG5MbPSmSMlYDUW89BEPJTHequmc0QuEhggDGWTqxUkicWykOxocRQzwlRnKH1glcI_uzTvGBt_g0u4WsRnilRH8em-5NJpLFRfGgZh9jftNoD0PE4fDI33KuK96niKYLMOwlSq4qMfSm-Vlc2YLzi3h2YPjpba1kyzIUdTI2pW5jbyR-_wVT5_dMqBoLKzJP968h0ixDvVB-fNp7YyBTjVRDPTmzVwROPMnBKvlbsrij7_ywJzwNuRi1fb36Hv3rvCKrQrMGucJBtQ5GffqyoBKrOs1iPOnpt_-ZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎇
جشن‌تولد رضا شکاری با حضور همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90760" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90758">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90758" target="_blank">📅 23:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90757">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUheanwXStcqXF-yOYfAwlVPcAU6aWA1D2MBvidjjmQXJuzjgAIuA9uwI57AXZjqqBdzTNiMFIVEWdntCUT1nDE5wHJLARvgvd7FvwmlTe5TmkgBwUuH-0a0xIxBU7g90rvN_ZaME8TdYlGGgx0W4hZokPFoZu6DGRJ8rYiImBGr52F93kqE030agkpnzMtDlP0KyHGDldmquJ-yllD1VXLEsIHvrIrQcK9hfaSCo6ckj2I2qL3rH_ynnYaUwt1AZhVsmOTsetOK1QTUOmiZ0pDXi5sYyL8oYLJcSxhCLr2Ughv2lCoMDl-5v2xXXfMY-5xReNh6vWfdwIeu1AkDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین روش‌های سوپر اپلیکیشن روبیکا برای جذب مخاطب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90757" target="_blank">📅 23:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90756">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7127e40488.mp4?token=l39o8L2uZ5aM4Uv0mg80CjeQn9huffPOINHx6FekuOg92EDEeDXlIEK6PISQJydQKvn9KdJ8rrwyxUJ9PwVjXfA90T_CJk77nx74LKcV_0ywJrhiuqKP4u-JOYBsIdRc2JTrge05MCJO4VxQuaig8ITQljuRczysyPexYoe8W0bu8-1LN79mv5JMrZkmMYBWz16hvYx3P8A0Uu-gBtXl3PE7EXgQxDslPh-aPg9txfagsRIRm_T-CqF8YnKXEFxxb-0FiG5NYntIt2we3f0gdcExvH4Pw0G1UiIwPEY_QJaTFqXpNVoNW2JYEh6-7l1cJ2ncbNOX91DIrpK09WbaJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7127e40488.mp4?token=l39o8L2uZ5aM4Uv0mg80CjeQn9huffPOINHx6FekuOg92EDEeDXlIEK6PISQJydQKvn9KdJ8rrwyxUJ9PwVjXfA90T_CJk77nx74LKcV_0ywJrhiuqKP4u-JOYBsIdRc2JTrge05MCJO4VxQuaig8ITQljuRczysyPexYoe8W0bu8-1LN79mv5JMrZkmMYBWz16hvYx3P8A0Uu-gBtXl3PE7EXgQxDslPh-aPg9txfagsRIRm_T-CqF8YnKXEFxxb-0FiG5NYntIt2we3f0gdcExvH4Pw0G1UiIwPEY_QJaTFqXpNVoNW2JYEh6-7l1cJ2ncbNOX91DIrpK09WbaJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کفاشیان : آبشو دادیم آقای میثاقی بخوره
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90756" target="_blank">📅 23:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90755">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7fd2c5dbc.mp4?token=NTRGy8-aZMynZCUcvZQmavlV0pCli1dXRHGtfDiDjtvPwtGseDt2ReLprRwhejXB2QnUlRGVZsC0FUbh-OCyP5AdViGdwUaSUIs7LZAXrlA_CsaOU0LJu4IclMrSR3xlfqbv5ye4yFre6JXLM_clBeYbbcYPd5Q4ehiY7uJK81I-zFNT-rGR0jSPoboyvgHVYi-Voa4LAJPg0rxM51T6mvBrfBbCcdV7cST7f0HkoB0wkQqND_cyOU8GRl9F1_vYZvEHF-9v9r6mm-6J_es0Wjv5UCkJyTUTIF1BEWs31m4f0sAgKjCxk_QRRLEsaxDPBwcvFG2cRPHOKIoW28n47A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7fd2c5dbc.mp4?token=NTRGy8-aZMynZCUcvZQmavlV0pCli1dXRHGtfDiDjtvPwtGseDt2ReLprRwhejXB2QnUlRGVZsC0FUbh-OCyP5AdViGdwUaSUIs7LZAXrlA_CsaOU0LJu4IclMrSR3xlfqbv5ye4yFre6JXLM_clBeYbbcYPd5Q4ehiY7uJK81I-zFNT-rGR0jSPoboyvgHVYi-Voa4LAJPg0rxM51T6mvBrfBbCcdV7cST7f0HkoB0wkQqND_cyOU8GRl9F1_vYZvEHF-9v9r6mm-6J_es0Wjv5UCkJyTUTIF1BEWs31m4f0sAgKjCxk_QRRLEsaxDPBwcvFG2cRPHOKIoW28n47A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این شکل شیک و مجلسی تیم ملی ترکیه بدرقه شد
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90755" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90753">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt3zvP2HZH-TWtlgpfV5tEacQMuei3NKROMid9V6EQ0QWXLt4h6cp2yDLFuN6uRTUL5NGY9vwJc90DGmN2S-VBFvnTnpSjcEvwBFB1Trka3NpykkcdiG8l4_HVWmuh2JOLlI6BhIELnVu5_RQBrPXi5-hv8XnSemNYBQLTJZRLIF1e_it5MSyCPWuxyfZvFZtxpSgN3gu06gJepDnRE38YPvi7w1bJ1jZH7GsqT5n-tu3t_IP1UTKkvYo_tRYdDBvYoLaN9gZf3-y33kBTNqw16PIfgLUPBf9TSjhDi74dkZ3WwbZGufmj3CFQ7sD9lgrGxj3dMGQJHAxDVCglDyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اون ایونت‌هاس که ناهار میری اوین.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90753" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90751">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm-FRU4UaWPtztOuYPshZUWpNHcGFj0_DBhJd_OePnffqIGXjoHKpo3jNAj66uw38XNYDfCF_RlbzhNwatAnh9RVLXY7ESY2NR7vCTqUTh4NnlJdvHKDBgwNE3cgB3ACRhisMySH9IBqClNODu8F9823XKYtQm3DydPvDNLqcG6BN94hPjTPPRsvPrRc2Fu0RN0oBR70tVKtRZbKPsnIvlSiPG8xknqi8yFRvlZN58KzKySAoeMKngD7Mobiuat8kYGPPlPlZw_rjatPujZdBSLTdo8QYEHy1bqheqbfhcqFJneA8aqgk_iiwKNNDo6YKmu0UOZdZaZyj9ALOcH_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریکلمه بدون اینکه خندش بگیره:
میخوام بارسلونا رو در دسته دوم ببینم، خیلی خوشحال میشم حتی اگه کاملاً ناپدید بشن
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90751" target="_blank">📅 22:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90750">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-lrwkO6BR0eGGIyAARbV-dMCAnPWl5SgtT2EauCBV88D6doF6EX6VFUbgaztXucyAEJG9XZDVDduXzCmoMxA1AaL56OgMCategyjxzkTRrQxJSdJVFvFNNM0hS44_kaEnG-AwE0nYzlzD0869GpLHx3fYPZAdYdoBPkmpM18779Fobv5RiQY2LtdvshuqkHcdV2rEjBoT_0Ro3dLNxotwQ8gcSOiCSJpac1OgO6Q6xmKMjbYz3Nw6DfAwGuSkdm2_bVMyO5SlPbmYKvKei9wXjbuGxXSxHN4B5RD1ASoeZbjcMgy2FOq-xuPNgcpNoNLYPPQCjKBv-lUCRYj1SHHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنسو فاطمه دید تو فوتبال گوهی نمیشه زد تو کار خوانندگی
پست گذاشته ۲ هفته ی دیگه آهنگ میده بیرون
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90750" target="_blank">📅 22:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90748">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYcvc5OmLOq2U3LX_1qWYDaljMdiTP8UZZ4qKs8jrYF6QxoX9YUGydm1Ax0bWQP41pJKeFf7P9h9GmxsjSVT1OeUZ_5cytjo84aTbReftxdhXV9OqG5LIJm44SLMNDq4UlSSwIgsceJTgbw1Q3MFT5ifxrsesXDlFS8HSS-FBhK62Y9FQ3iaVvO9wJiYGi9EWIQ1Lo953EBkWEA1bwVbDudPY57p2ECLN92P9GDTZ-zbcga_yvPwl9VZj9PNOAiBuxF_-2vwRuSSbvy8IxYaIeHH6QIGsnvgYsuVPauRW9q6kwtwNJ1fs61tMvDHDE0zBdqqrBi-p9U_VcL6Us2-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید جدی برای یاران نیوکاسل
بلژیک با برتری ۲ بر صفر در یک بازی دوستانه مقابل کرواسی آماده جام جهانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90748" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90747">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromernesto SUPP</strong></div>
<div class="tg-text">🚨
فروش اشتراک V2Ray
✅
سازگار با تمام اپراتورها
✅
لینک ساب اختصاصی
✅
سرعت بالا و پایداری واقعی
💵
تعرفه‌ها 10 گیگ — 200 تومان 20 گیگ — 400 تومان 30 گیگ — 600 تومان 40 گیگ — 800 تومان 50 گیگ — 1.000 تومان
❗️
پشتیبانی ۲۴ ساعته  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90747" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90746">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKlo3GGQ5udNRWJJEvohYdp2Sd3sFCcX4CM_an55f7uwNA-8NrO5dagzcX0zRabbvXt6VQ5K235pOxsPBwhzFmDxTzgKEUOxsM2mlbb8FtTHJAzzTuPXD8Fq43tgrBsDWrR4fVp3DH8SKXgLh7q8FoZnw1s8mujWU0q9VFUl79YT50qpTT2Iqg3XsAzDwks7vC_YjDR4zjflV254UDLAJmRCpO3oEsPx62sTv5Giv2Hs01coV3SvJ4ernK21TTrRcLhjX2U_KThodmmfCcFFFQ2c2mg6XahR6F_67J5s6hwk1iKWXAY_xtD9fndWIf1fWwDA3FbsXBElMxk-IHL9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش اشتراک V2Ray
✅
سازگار با تمام اپراتورها
✅
لینک ساب اختصاصی
✅
سرعت بالا و پایداری واقعی
💵
تعرفه‌ها
10 گیگ — 200 تومان
20 گیگ — 400 تومان
30 گیگ — 600 تومان
40 گیگ — 800 تومان
50 گیگ — 1.000 تومان
❗️
پشتیبانی ۲۴ ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90746" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90741">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsSmIRjTB3oBB-9FXV-PIRRnjWxT5NYYniCZuyBNntEKHAUfFbFIHKPX6ZvOiU0mCulRwoGwnNTWLhXVN6RgKscZx8jvb2IaNRg1lrs6dXUNh16NrkUf17ezgoJg3VpJltml707ExoNu6ScK8wusUhJ8ehJ72tHfqRaBPo2zWaLEvSxeG0dBR_5Lmk8AgoZH7HUoErRqsEd8NT6ZwdHyRL4EQpLjzslL_m8v3yYmKgawPGncerMNcg8hYz9BRrNVInLXmyueHsuTeS6JSPqBmkAx2B_OwzTb8_svTkcLl36IrNoeUzJzXKONLym_w1O71PG2MM6OR9UsYz7koFlTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtnsYNaco7itci8Oq0lAIh9pNgS15i9PZbWzinZTVtRUOXf8dWBLcG9CMoqjTtmgiZNkojXkc8Ykt3iPLzGcW9dvD5HUPOCL7GNHtZcQtSoY-sWnQYELAvDWWFEiusmqGRcP2uslceUo2KIb0aFgRlodMsnqLIyGAZ8yRzt_WtWlyec1yIa0Nyk3JWw3oW9OZF9IAwo6Sw4bD18A8vKoTipyQQWjYfPcN2ZIO8WctdnNotFm3-EanqBsBHCmaSSo-a_V-afBoecJstP3c3jHmvVHmaAe6XVuHz4doTkWZ2RXsNxfTMJHNna1lvHNSRakFIOPT1kwae4Oc4XzCTTcOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیه اینجوری تیم ملی ترکیه رو به جام جهانی بدرقه کرد
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90741" target="_blank">📅 21:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90740">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akayqfD1PNeVkQyV6Km-G00F56U0VRNjeWaZHDHG_FPOlHXh02f_nPJV01tYbRyG9vBaabB0yrr7yuRyYwqD3ZoEWnof9OTKlSyaOBKks5UmccJRBxWUn2RSu9tYVPKjG4I2qD5ZWIIMxSOYLuAjlP7G-uVVZMNMCRAVTLX_SpS-nt2K6OIzV_gUA7gN78l3ANZoCQ-YvM0WtQOGmwXR4cK5hoKG0f1wiMtS1CP5A1KEXd4F4h_B14ZQI2HUIx0wW6PbQ4qWW_CcrN8U95fsFcyNjFI-a1sqDGkxdw9H4JEvy89ULMK4WB-MMeHbYhMr-6j5dkP2aN8ZY3xqwF-_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
شماره پیراهن بازیکنای انگلیس تو جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90740" target="_blank">📅 21:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90739">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=lSMEJvz2VZlR0duJlhzG_NmAw3oAEad7vnAopVwK2Z9kJ0sE8TT0-xSEsxhOB0gzvNwiEvzupSHg4olAE4lSagq8ncm9k_FQwB8KZ2ZjEQ0njcf9ZSLDMoWHEAzP-5L7CL6Ox9HwlmFSDaQv_Odfk9CKKzMnIBjAQR7kW0jSI-xpgy7d1yLsFe3vKSc0XjSR4AvUIStvfg60P-lU-EolQmBovOxxem8ZrxqgvqYAJDnaX-MyhZKiVLp2tFsyR-_UV2NGIcW12EU7VTK0uX6ABeTdJOGdW_rFqRH-1Sdi5eJkm31xI9zZRWabhWv6dX6XEVbkcIi4i0HXyxHgtaGYNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=lSMEJvz2VZlR0duJlhzG_NmAw3oAEad7vnAopVwK2Z9kJ0sE8TT0-xSEsxhOB0gzvNwiEvzupSHg4olAE4lSagq8ncm9k_FQwB8KZ2ZjEQ0njcf9ZSLDMoWHEAzP-5L7CL6Ox9HwlmFSDaQv_Odfk9CKKzMnIBjAQR7kW0jSI-xpgy7d1yLsFe3vKSc0XjSR4AvUIStvfg60P-lU-EolQmBovOxxem8ZrxqgvqYAJDnaX-MyhZKiVLp2tFsyR-_UV2NGIcW12EU7VTK0uX6ABeTdJOGdW_rFqRH-1Sdi5eJkm31xI9zZRWabhWv6dX6XEVbkcIi4i0HXyxHgtaGYNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هواداران عراق در انتظار جام‌جهانی؛ واقعا الله‌اکبر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90739" target="_blank">📅 21:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90738">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0CmaWc6zViwz1huFk2YqEUEL4QWaE0Q2IJWiNxR_24Lu7OYkPkFnRz6lHCJubrVs74mc5xQR9ZA8L9JWfFDFZApoFOcXpn_Kc2POemV9NARGKxX9dS_Bgse5lGt3YjMPr4AyWIKyeK1-HGstrv7zMGmfd674Tihx1obihRvjHAsx98LzrXV_kT2FARXOtF-DsZejtuHM8vzfgl5bXdm9c9yOS3TSCSAZRfi4UVGfo8tSABt8pIMkB2gcterW7eMbNA8zhLSAiwxSw-qc0P3Jxma1LUcbm8kOtSl3JGme8C9FrvWQq20OhtsHxjZlEIK1cnmKILdDRfn9kMTIMZYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مقایسه ویو موزیک ویدئو شکیرا و اسپید برای جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90738" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90734">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pni_u8t4PX1EBAWLrwuSf-2VrLsVFYmiB7VIhhN33i5esNm4RzHz3NDs4xlmBK7Vx-0SmPJ8JbuaEhBOO675dw1aAxNtNT8K-xswoivhstm4UFVBGNiKOeduKEUGuVKvcfHhkWXsKT7UI5YeJfbpLW7UoHu8V0_GRciEDpDbSoqzHT1vb7IieHZtTRTqNriDW2aq2_mSK3ZmBEbrmjarcbf_cVYRbcc0jsy8J5Zd7IJk-A9GLrqSZ8Ja86SiH7M3FKeFScggrXXEkhucxrwkxfA5XRgg7ReIRDyoiFUUcqiA2KL-Uc-sI7lajEK24d1cflXX3YHo7rirQ_BK_ZeifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sw04eJrAO0bFaoCTwD9p_dfWZ41-t51wyuKJYp4SVxNMoPMtDvuVx_PJrkP5bOXV7UqgKB6IacsTNQ6ezWWAA94uIRU2UxHn1be97J0XAkz7w5k0HJ7mVg6gsf019GGhHpSaatzuSdbIaR6YXBiz8weCvbGPfU9_rjK_4oS7Cq5NG7EaUWZdUzOhNC-nQqcXdlorl2xYnCdCqpFo7IHHff53u4xqUUdUGhjvIM8PaGmpdGXkrx085DDSKSXujvwLEBgSU_V3gb1qK7vPPqu0oanmw9Afv5nBEXDeeFRaS_u2cUlb_5E7j0GcKJ4fQIgag2YIjXV3pLWjScV9fT0AaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/st-lekpGThtP27sUVz9ZR2XVJKGhx-lc1ZgG41ZPiRMhkWzoKfvD1KmyO-7oDzbx1ptVFUxhvaUm_UuUHrQHLw6ypM9YgUEoXByodLxpWA4WZh72LwTr_v3O6qAK0spLi6-hJ8tjAi22tqwrjwABLzE2tBG0ds251dq5Oy9FCyjsjLxRGIMj3C6PltaeSiQk0oJg7ikOHc21Sp4e1HLlzTz_uNGm6bQMHgjTdrXpw3vghf2-ka1jkmvf_sJPcmbFRaCTRO7h6R1PpH1DUQVPJZu9szoFqXaiFnU7zHTCYbA7UxWyYyD2Vo3H2xZ7CwEtPH9OcGOQt8Cq15bfqDb_dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🙂
بلاگر خلاق برزیلی حوصلش سررفته اومده خودشو لخت کرده که عکس بازیکنان مهم جام‌جهانی رو چسبونده به بدنش. طارمی رو زده رو باسنش. وینیسیوس هم خودتون ببینید
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90734" target="_blank">📅 20:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90733">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇹
#فووووووری؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90733" target="_blank">📅 20:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90732">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNlnvKtTdYbTHv5izyEDLB3H8H1UTbWs08wm6cz2uL8ZaLJz0nDUIM6Op5nHEKgvunWNs5eFf1oZIOvjLYGnP9RHbNXbsbd2qr1WiiTbg-qh0E7Ym2xN5odggZFaFLxwzWey3ZLn6896YZuXzPKmprP_mxfkSs4oOzir7ulNBT5ry5XPIK5Pv7M1a9q6_dwqOEKd3FfzpNAKcDJtUIXjxo5ezzj-JUYZeR6-QH2lc_KZKoDf7EbfekOit53SiOEb6wf3h_4QswKf2_f2NbfQn0qIGQdCsNNp_mCGCeLsPbF4lHG2zW5Fuo6YufRse61L-Sv9bGX3NXzmLeTuDvvwnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90732" target="_blank">📅 19:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90731">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0YkVulrEzXIdGykDF7QP-5edZYERZFw28fkdHLjGN9bwkfqQmybDXuLi8GK-bj2kZRqfQT_ye2c-3hXdM_pLALhiiJayD5l0LxUB6RE9e3paqGEgJCDUq6UAMwvST-4rDMO81MCGIOjX-qwgFCygAvCUsAj_Oak6kD827MTHap-5CwqRwXdxsktWmGVCc4_Op7_8YCSo9LqIvIOIcH8JsgBsSn-2nIqmohAVQEnw_6x90Tnf6cWBATDLOSx8MH1-eOoTFL9n5gPgbgSSeN1WCfYQR61Ju4ApO_GAJP5_lA2a2TrcD87k7GGQ3hnifc1wSzND69XuiQdg0wfzP_Q1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🤩
تبلیغ جدید نایکی با رونالدو و لبران‌جیمز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90731" target="_blank">📅 19:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90730">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AldiYNiC1O_yXuPN26JCyHTD4gAu0c53hGPUhPhXC5uNj1880MTjODe67qIfJUNEnIXwtQeRNFcwI8DgxCBHhZRKhKc3LrFHC-rXaehx0s7CkGzbOWNhKLAeNyzO7ZH1gcGQScC8Xik2158BeNQthUk8ehAVMo94OsCSr6CQgjhvDu3J2F-w0rD-RQMKFK4alDsQv2jBDxDTcKDXQ5nY0VyD2CAbHDNA1_GEzxaB27qDmMNK4bjRAus9KyEjYnaAP9Qpv9PcmCoEZf47XMjAICxQQDqU9p-Frc1muYaFu69AksKAZjpxqciWF80f1sM2RSFBKxWMLtAqCUnYAN1_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
دوس‌پسر گلشیفته فراهانی امروز به تمرینات فرانسه سر زده و با امباپه و رفقاش صحبت کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90730" target="_blank">📅 19:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90729">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELafR-6muWJtFILZKYUiW5xcEoUlPYLuIJrenpi300a7nqqVdXwOW5xyYVXXvMRqYqb6_6btnQSO8dCR0ls-mqQYdNBygfkfRmbtGEhz9bE4SbMBRxjWfjAZHxTZSpBaQrt8ZXWQTeF8wgwSJIc4aLpkGrFWNRiX8PGeIvCxPOE78n2-OEarX0qbCLKYpvrW0Wy7wXPAQkg1rPqkAqaJm026lRGMoIQ_Psc5kzqyVEGtckdm8q7OxX3Y5_govT0ykOJ2gm4f-i4MpRkKk7lxPa3_f34D4m-iHNPIJEIOC0CNznnqIKSBB3I6m_eorzSTat7ctqxEWZG3L3DMWvJWWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ گستون آیدول ( معتبر در آرژانتین ):
‼️
من دوباره تأکید می‌کنم، موندن خولیان آلوارز در اتلتیکو مادرید برای فصل بعد خیلی خیلی سخته، در حدی که تقریباً غیرممکنه.
🇪🇸
پیشنهاد بارسلونا جدیه؛ ۱۰۰ میلیون یورو کامل و نقدی، بدون هیچ بازیکن معاوضه‌ای، ولی اتلتیکو این پیشنهاد رو رد کرده.
🇪🇸
الان اتلتیکو در ظاهر خیلی محکم و قاطع رفتار می‌کنه و از طریق شبکه‌های اجتماعی و پیام‌هایی که به رسانه‌ها میده، می‌خواد نشون بده که اصلاً قصد فروش آلوارز رو نداره و موضعش رو تغییر نمی‌ده.
❌
اما واقعیت اینه که نزدیکان باشگاه خوب می‌دونن نگه داشتن آلوارز برای فصل بعد خیلی سخت خواهد بود. برای همین انتظار میره مذاکرات طولانی و پیچیده‌ای بین اتلتیکو و بارسلونا شکل بگیره، و حتی شاید پاری‌سن‌ژرمن هم وارد رقابت بشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90729" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90728">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90728" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90728" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90727">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtxniAfKRHLmld_hi7owtvE5Jo2HQMFz-aO7B4_xnDNocVD3yz0Dg08eWaii74dYxc1sKkWE8fKnTlHeb4ATc15V21I6eYNJfFb_MsUCtGtsA7jQcZx67zPGtnOX_gPnQlVWoy2r4C77G2vbjd8bRArpGHLRejC2_d94a8rUqv1N8HxoFK9dxsJdnRVg7MP01D3IaCytvp_C9FVs3X7VttZ2JKm_U1ihlAOKrwPXTG-hPtz0QszJFCDYzEI4mQstkuMoEiitoSs17CHibB5bIb_6zJpflIgsZjW168NYuENPznpIFolb5qzNl-ix_5sNvPTnVcTfSborWaI_lDuZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90727" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
