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
<img src="https://cdn4.telesco.pe/file/kfHfrG-F7S42UZS4SkgpODQGFGeM6JtXVwaLEKrXz2mdlO-Cgb-pfo67mIceLgv44P1DqBVtlh6fVs5GhuWwu4GLWV7Li3W4MPlH9EExvyV4Wk4s-l74tje4kov7EsM33sLMjq1l8bTfH7cyWyJVWSJQmuvuRhFpf-3VMEK9fDYjvgVKsxIyNrnCfZxLlvscXVSeKm3ylgQRnz34821peSBPNmDQHaDTmjr4XZrkrQw_wnbKqc05FfDf0ATgongMfsOLQuZY_WrGhnfRYctuDDFIV4thZVHi-s2R-se_A7zBVHEFJ5acOXQEjh6AQyQQ73pRJySHt-Irw0FjCnwQmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 605K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 10:41:44</div>
<hr>

<div class="tg-post" id="msg-28894">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekUvmUmoXJje6BF0QPINMXO4b81rMFisCg742fEq-wtjun8d82orsoHe6xyIh07vnB6tuPT9iwIfmR4I2-clwOsqyUM99P2v7hOMWXX_cD3cooI1WfHciWpKB-R2vUio63Ck9PQ2ov4xoMKStt8kzdkfMWSibVKn-oeYqhn-aJvKFyjM-3ZTrptzaBlu3O7BfGP9ety8xNTMioEcDp2ABJjuNLbDnHxbeSsTKncBkngAOoUsC2mvBcVD7qnZbj-ap270jZoOsND6yCeHXeTswFTpqdBZL3_ttrqHJt2VzDHb8A4R_YTN01ZwS9mr03A9ys1Y_40yER7kB59hqzASoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtsCVx9moxWWHwrDVS3IG87eYHFvyH2cdEhbkwdl8PRd1WV57q6IwI2CH__sbQei96mAvgsXHGy5ss8-rgw6UflGnXUJbmS7meY8qeDlgeMzOTweaW7gwkhp3BKOXvTgj0VKLCfXjcHTxs95d3a_9UaV4JCZlGYVP9KXhUDxo5GzNvNFHiJXHunlO-U9GiRonl254htAiLVeKnhRFVVMXR-d0OALXbqE1_YLQbmhs7G2gGTn3pUg3QyB__6XcMhQL1JxrPGaD7nJ2SIwVYwi3uZDWOvDG9g_hcRv92bJWpv-PsRW3v1VOH1KibmXrky-knaNAHThFB99AdT4gPISZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/28894" target="_blank">📅 03:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28892">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1tUWmZN6WOQSPzHvHo93WmWZ7rXdAxpkyxESwa8fc5pgrukGhRyM1USBrRLkPNdOlsXVuXzdgqRnmkbtL3thO3ZN10OSgr9z_6Z45G7sJLgV5Trf6mH82vwrsaOlo3E0nYOXp1ciHIqjxHEmCoy029p710vMLDEHb1dXFcSB_E8TZAEQXaHCSwsCy_yUrFeKn3EJs0OOZmws-xJP5dQX1EqxgOlhTsxnK2rmhlba_BWy2xf4Vuxc5RVh71PpS9EVw8CIOvmc5pM_qpGE6NrtbR8I2s-nc-f1eWUMAxnxz9ujXr5-QiC8BpmIFH0m63Yuau-bHScD6dO9oPhu_2_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/28892" target="_blank">📅 02:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28891">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=U0yvJY2oVVN_FfT38MHbtH7U_ZwdbJuHC_aQe08Z_vuFJsWGuFRTbQ06JRYdTBkfP-abFE0g8of0paZIikHyIwalnF-IQbFWKFKUaHIUfbByJ-BbTShO8Xg_NaH-vIg1pNX44S3b5Kpnbm-m8y-C6QfDRGcsj0y_uSmo4j3tFIjbfxKLxJX5EfzX9KT36g97E6LGZF_hjrKkIVTeqlAfJO4FN1BBGxsPqCaYsEkDTdRvBuOS4BdHfEDgQ5Px5Oc1qW7cxxmtyilJzQLkXfmINafrFblYED2Q5GQHOZv7qP-2Eipcvm_P445pnYpYM4rOiI3gamwmHuo__33wbzcUvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=U0yvJY2oVVN_FfT38MHbtH7U_ZwdbJuHC_aQe08Z_vuFJsWGuFRTbQ06JRYdTBkfP-abFE0g8of0paZIikHyIwalnF-IQbFWKFKUaHIUfbByJ-BbTShO8Xg_NaH-vIg1pNX44S3b5Kpnbm-m8y-C6QfDRGcsj0y_uSmo4j3tFIjbfxKLxJX5EfzX9KT36g97E6LGZF_hjrKkIVTeqlAfJO4FN1BBGxsPqCaYsEkDTdRvBuOS4BdHfEDgQ5Px5Oc1qW7cxxmtyilJzQLkXfmINafrFblYED2Q5GQHOZv7qP-2Eipcvm_P445pnYpYM4rOiI3gamwmHuo__33wbzcUvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار!
شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/28891" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28890">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXJtfX4NGMm2Lb6BpkScU_SK6mkBuq7iSrUDuJj_RMgsoJwGfRq_vaz6GZlo489EbgxoauO8knzGtviXnqDG0Umof1dRukYBX8dBVBb09MNwl1wZ5A69AKMatAvfE2BHVfK9uS2qbpq7wrGfpDEPmyVpHwQeoiU42v2IimSRd5QMyBK-FClTiwEGw4hQn23bArr-Kjz6rCgBB-BwzDW3PFwgMnnBmIabGl_zCz2WsZy813l7ZY_yLj-ocCo5nZK45fz2Czr6mbIqMga45K19F0IhjLOGZnSMExfCbRzXPvBlJdhUX-UGRgE1eXwB5A7tgWWoi8CIZkyH0nJSMOrUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ دربی شماره 107 با جدال حساس استقلال و پرسپولیس در شهر اصفهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/28890" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28889">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT0hBqdIPZu31sSYqmGHWBDPXWIVa3pgWZrxyMcWeECCL3RZr2Kzze4m2eAOGZI7bpgrjfhNVLGiW9XjaTyIP2fmmnMkpvMPfqJ9SKqVCaFQR27OcFLtR6G3ongT6VNm1fZLx8OkZs8uNcp6XZvrbpPeb7Y4tJXlVOMYUE5CD-cy15oeMeRcAR-Oi862CeN4W-EW2VrLznC5tBRSTt5-zOKzohF0DvmJw4aDdjlqxJeag-oDBBKRCCwetbZIbEIWrBweIccuKWBe5NzSPcDt-37W_XTPQMpU096nVZagzjUbaZ0oIr3ijA3uu3gR0eCihHaspIzlIO3uIpNUoWFcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
ادامه روند بسته‌ ماندن دروازه تراکتور در این فصل و برد قاطع الهلالی‌ها در شب گلزنی تازه‌واردها؛ واتکینز نیومده گلزنی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/28889" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28888">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4s9xt-Rf_SPR7UxgwclfmCnRmpRbQPc41vlkBrRkmB25mV9fZfVAsrh8N28UJPpQySV7qW_URoY-BBUsWgHJzfo0-rzZQgs610ncD3Ouz42WkgqAO-SIKgcTRmRyxnuzatQ1zS-4aqIvybb-cDxdUPczTTx6NsyKFQBmcrY540jFecHOy8Xgk7cY2cng9Z9z3LyIGjURaEKpD1F4CW6pSit09DSJWq-6PxwyTF-9fxw-0Kc8NCj6jszVb1RCPN8GNkufmGuXV446ZkxiOp_T0JKwK783eJGo5DK7Z4UlxznsZpORekUmPDgMvMEFYhm5hCDFS2iGMbB73s097aoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
بعداز دست‌دادن‌فصل توسط ترابی؛ شهریار مغانلو و امیرحسین حسین‌زاده دو ستاره پرشورها در حاشیه دیدار امروز با شمس آذر نیز مصدوم شدند و میزان دقیق دوری آن‌ها از میادین مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28888" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28887">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNgqjHlehuxTGtBn2OomIrwHaTpl5SX0bUxMGj5KIROSI0zILYrC49oZ8cI_WXrAvI5w_N9gIor9bY4W_nX6VTOj_NhbfmCuZ0lBijuY6tInqB3IVgCYXkA4Ap6yX_bZkeMbqQOW2n6Qm15en0PEyG-YERu96Llxrc2QW71H3Lfjp-QSeNQWLTJKwtRVvk-CO8I7ZZESW2ppZQTHTyWngK1q-hL4EZXXbyQWTrpUNGB0vRvf6LJr5fk5IEld7mStnIq8g6zKFTsNbHO1zzAOavnK50rnND5mEJFe8aXJAmUCxz4aEX6YVCEieZ2NAhHA_LMF0_WUe6flInw_QdvtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28887" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28886">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTVbQD0PL6GlaeJI6QqMVx4VuwjLGjIYi_HVzW2t19bPstb496shik-xWWF8W15PrvilpTbJZjPlsAsqeq-9Felrawy6lvWC_uTS1ejJncAdsuESEUaNBf4n1SOakw-EDFwbDc3--l9xHlvWqyWyi7PZQT9eMG_76C9g-jh7VSfXaSudTgXfvmQZoY3aNuFZNQeB__G1ceHhYo_WY9Cs5_VASNRN_nZ5flIvrYlf7kOXVX8PECrMQ6D0-dQStqSZM6T1heiePyZ-pa4z5EA_zsmTx6WzxSER1-cb1zBtj07kBm_zMA_t7bsI_FTA7UE8yNsg2q2dnfH4wQ3kJb2j5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
لامین کامارا هافبک دفاعی 22 ساله موناکو با عقدقراردادی‌بلندمدت به‌چلسی پیوست. آبی‌های لندن برای این انتقال 65 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28886" target="_blank">📅 23:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28885">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGvJ7vhjw_cq2MMmtUxFL4K0D6ToamX1y_6l4p5fXa7TOqcO_pNDWzfXoMtu6hiHnjR7RDhObVZepw3ZwhMn-MdIQXUGUPGPbRo0daR3V-mV_QU7F_PbHjEpRp2YgmqC3D2F6BKSohN0mQCjBXKkMeI182-uMy9T2LiuOoCBrQrYaBK8hxLjrEuONKPs7tpZff1MRxYrW3lL2qJb0VIDLaTECGZE0ZTsEs6MyyY2K-BnjbcTPfChH16CAAAChTk0QwoGgOr_9SRi6nAo_pyDiFVXAYWAL4bZHArkWPai8LRvLcY-HeTrgOIcsKwnNArOR-uGgqR1SgmcuDriQZ1dZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره "9" های بارسلونا از فصل 2004 تا کنون؛ گابریل ژسوس صاحب جدید شماره 9 آبی اناری‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28885" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28884">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVxYxsm6_geS4DLu1zXQZM36ZRGOSXmL84D2GnTqwPtZifsAZlgcWYRNkDoEy1syB8ztTx2ShIb99fgqWXuvN35vlsh6uB9kC0WQYS4sD5UcQsBfjJGlPBEgcJ__pCE1Fxheq-0hk7JwjAksYGERUlqVHn7ForzbUMT928_Q9m0hUnuim_R8WFSiQFmD2bsYwNfqEtn3MSGHWEawmbSso6SFiCJ1qT4YCoMZVe3d6XcT-HOIaAv9QatRf1qX46EtDHCaOgroXkEF3wghziV_UoDZVlQQleol-ozx92IGaimDjsHXpe5ABG4M6-EhvaUCbMxPst7gyNc_ZR848MuhgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28884" target="_blank">📅 23:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28883">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrsLqwBxF7SanJ74t71By61vO-ztdouVTWyKgDD7cxt3XZ1OHlSOmgx2Y2pLfWTOXY4XBKZuyRMx71ER6eRmT2qNbpfBTjYh6Dv5NnUcRQxp-rBPBsfy7kJGi3eoVKoT6Zl3ylCwkZhFdznuVnFRX_QLBKcrIdRMVwtDJyEeV0snacJNdNd2pW9lXdNPpxLccuMCzr6muhtw4ifr4C8JNkFybt8BylFaV4XzRFIj0G0XaKBDa-OgiAjwHFxNRBjvFjbEVM7uk3CTpLfcxPvzN_Oela9je5mpfl0P0AhQKjzb7NWpzyIQNL2fMHDg22SgToFsJiSOPXDnbl13F9zKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28883" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28882">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1C8lrGBI6TYzONg72LO-zwhTqzHcfZIPkT08VLbSVzwgkMcQlXdJO6MidlbUscq1S6wU9-V3F5c0_ZGlLRBRHgpTq5sB5PSUhVwnoz2ncVLoegU7rw6Tu5Aq6TfKxIVI45CHMm5YAImbKQKjE2fJeR_2_BBt6GKummJes-rlsAKthskdfn9mP0O5LCutWcR9aB65nmyrHogld_2UY3y5vPUL1BoKuTGht1i6HnnBR68AxP6gxEJPTE6no6T2mmhxaKUeFgnffY2FAIArIMcLjFXHltm7PyixffpzhqOV6MQJO-4_BqnbDLSZ7ck2LRPoVhXxQreiPEuezUgliVxzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
به‌مناسبت‌مسابقه فردا؛
10 گلزن برتر تاریخ دربی تهران؛ علی‌علیپور تنها بازیکنی از این لیست که همچنان شانس گلزنی مجدد در این دیدار را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28882" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28881">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR_tKEc0aD2F9TUeMAAtegwwK9SBn_IOdAKlunsA9qTK3vNHXWnTnhnyJxfPNkdWcf3KbZ_ocm1tRnD2drldt7fTZewYd4eYNRpgkaKqtdfVh7fVCo2FTjQj2SBXcXcG-tfnNjIGMnBOvLByo0OoT0TV84YYODuwoUNb88vlN4jMnNsJ90GXldH2WyDbzTU4SYK3gbYivvOf9eco5P_a6abbOnn_ns0srTTCdC-NVm001as60AMfcqu4nsutRAzD65oQPgzwmC-32MLceXa69WjFsSxdLuRpw4E1sVqoqUW4swKqNRjjKGPh7x03gg66m_GhAR0uz6NRzz20F4u6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28881" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28880">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=NQZNMoiSZOZgQPR5z15448BcH-zp119nMxeANHsAkp8RSQB8qjuEAOT7mlR_n7rDfORePINEY8LB5zT9xXmMpZU8urkNVeZ9Qx2n1LSoZWQ7K2n_pPg0AV0--u3LQvqABeTbyDY3GrQEtlUVPhCWLpdg3pQNk3dBEZHRjj_ThpEcv3wG6McNZfyU6kKi5tX8FqW4T3H_dEAVoAHWmnbIFBKmG8KxZkaFcdye5mXb3O-IfSOkV3RUJFUGdu2kkMHQ3EdBh_lMBtRo-gGyyDtu8P74pf_wiqhyA0oBcAwSRC51M0WOqGmuFH9w46NCJMnot40ID8eD3f2UmkCtrFXoaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=NQZNMoiSZOZgQPR5z15448BcH-zp119nMxeANHsAkp8RSQB8qjuEAOT7mlR_n7rDfORePINEY8LB5zT9xXmMpZU8urkNVeZ9Qx2n1LSoZWQ7K2n_pPg0AV0--u3LQvqABeTbyDY3GrQEtlUVPhCWLpdg3pQNk3dBEZHRjj_ThpEcv3wG6McNZfyU6kKi5tX8FqW4T3H_dEAVoAHWmnbIFBKmG8KxZkaFcdye5mXb3O-IfSOkV3RUJFUGdu2kkMHQ3EdBh_lMBtRo-gGyyDtu8P74pf_wiqhyA0oBcAwSRC51M0WOqGmuFH9w46NCJMnot40ID8eD3f2UmkCtrFXoaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
الان رونبینیدکه بازیکنانِ ایتالیایی عرضه‌ی صعود به جام جهانی هم ندارن، یه زمانی وقتی می‌خواستی مقابلِ این‌تیم‌بازی‌کنی تنهاتاکتیک و راهت دعا کردن و کمک خواستن‌ازخدابود! به معنای‌واقعی‌رقباشون برای سلامتی ورزش میکردند. این ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28880" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28879">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWAwp4VD7vHtFBiRcRz4ma2DAvTaRNU5li7MvXS_KQfFGiHnD_ZrWEPGA5AeYEq9NOSmN1sphmBz4YxZ2yT-muoZBuKmKG-bynzjzSCVtYU8xGBJl91Uuav4zA321v10bgncTozRzjHZ7CCNGpZ3X0FmRMCt0msovtOg_-MpuDDLz3SDe-SCzmF3-oB9dVcSfGubkV4pdbCs80yAZCPv1aK5jTzoRoLVbTou41J0axPq9940jNCGMx8zPclyijg2ZU56Av6_w8stJAUkmj9tjLEo9WlDfxi6eLoCYV5jgihgKpLMKZ9ny45ORt0nVi8bS-MPFtZ44Q_QWMpNJTsYkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
به‌ درخواست ژوزه‌ مورینیو؛ باشگاه رئال مادرید قرارداد دنی‌سبایوس رو رسما فسخ‌ کرد و این بازیکن بعد از چند فصل حضور در این تیم جدا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28879" target="_blank">📅 21:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28878">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5pvp6B4IZ8_6AYS-XksGwKPuakspRGWKe1G9-x5BzWIfoy6W3Q5JfOb3vazuQ78D0EbnleUb8ew_9WntOHB-74pvdhn4tFg-qqGl9Ulo4-ixpgXuktZOa1YkonJKz199d4UmvPHzK_V4q5fz3D-mc6vT9hksa7Wg2FuRwd3lEEfdehkyUa7AyUFgQvswyOsPeXILqONTAETUv6rwBI7ixw1Z9VCTapzXHfQxUJYX99CnKN2wq6Oih2FR4c8a77NZHX720rwGpR_yzxmZMcnWLa7Z_j2yJyNkCx9AvImRTJcYg4nEEFBM-9_w1HdR01Th71f9ttk3UTTIjZhCpB-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر
؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28878" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28877">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=DhfNFiL7DOereb2J1XR9lAxhZrqC_oJVnEkEikqgG3apg0Mn_RGrUGjjQC4J8jPwGaYYszUrC1MWhHCODOjF6TR3LSzlv4VXtD9DrJSPpDiHN9Yk8z9DqHspZ52UeNdiHNMOwWX_FhjivjcWm04qul-gD3v4KZ6NAkuQ_T1x_jhoS64UUbk-TCo6Gd_DL7m6JO4QmQaq7kkX8KnuRCdUGxkGaZusqrsOdqQ_mhHz9Q2r4mN9IMvfQGfdLaRkeWKjHtcU7t3lFcYNMLTQdYWm_gunaos8oqZt-1tbVpSnzgwgRqenTl4nyAgllp1sA0u1C2EQMtM6CyoQhpjrhrdfdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=DhfNFiL7DOereb2J1XR9lAxhZrqC_oJVnEkEikqgG3apg0Mn_RGrUGjjQC4J8jPwGaYYszUrC1MWhHCODOjF6TR3LSzlv4VXtD9DrJSPpDiHN9Yk8z9DqHspZ52UeNdiHNMOwWX_FhjivjcWm04qul-gD3v4KZ6NAkuQ_T1x_jhoS64UUbk-TCo6Gd_DL7m6JO4QmQaq7kkX8KnuRCdUGxkGaZusqrsOdqQ_mhHz9Q2r4mN9IMvfQGfdLaRkeWKjHtcU7t3lFcYNMLTQdYWm_gunaos8oqZt-1tbVpSnzgwgRqenTl4nyAgllp1sA0u1C2EQMtM6CyoQhpjrhrdfdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نشریه‌‌بیلد: هکتور فورت برای پیوستن به‌‌‌بورسیا دورتموند به توافق رسیده بود اما مخااالفت پارتنر فورت برای زندگی در آلمان باعث شد که ستاره جوان بارساییا قید حضور در دورتموند رو بزنه و با قراردادی سه ساله به تیم رئال سوسیداد بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28877" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28876">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPKQ6WvuZgCdOlNiZbn5QVo7bdJIYNAyHjNkz2NfeOGM1AIOeslDW2nzVueLwmYJjKt2ejsPf6osYnaHtRJtizW2iKPiHLtZ-AbuKDgqUsAkiawbWaE_WSU6N73I5w7JndJPP3a4AevZE8w_q37omGdQJrk_R-8RvWTjurRgLn-YtiPKBk2X595WA0g5PAf76B27n3LWml0x-l7r7hA1MWc1VCWUKrnjC3gtl7nKbgi6TyhpdwZewZSpvqNtHbCfldKHfQJM-UcYusSgVSe-ujouwgCQMKjIOTQSCHEdUuzRK4FKlfAFSANDzTcXG3y61etNQ33GWEZO-YY9ragXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
نتیجه دربی رو پیش بینی کن !
استقلال
🔵
—  پرسپولیس
🔴
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
🟨
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی در ربات بتگرام :
https://t.me/betegram_bot?start=p12_r4EF37DCE</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/28876" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28875">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTmIZd4g-V4JrhhyF5kFKxV8sWEVe6xsmn4CkADL2BEog-bL2kGMV_jNz2JtpI85grJzf5FhhKJXkl6BbEUJ_HFeztBTDu4cYaOwGFNFKnbAFf6ZXXlYf5aZIXaFVBHzHAyhqgwkg7tDrdxtglUexKL5OaE5r7Yyr9zkx7Zy2u257cHhbUf-BBrGJKAUCAb7oOkcxAn2eEPI_rCMvHnosw7WemhazibVeFzkFG-aYqcl5xuPbaAMJvztrBhD0p9oPSfffSn2qPcdV1hdONNthAxw37n51D2AHU94BsNzG0ile_MHi4or7o4APxTEyS3hkZeXAdqd91l8_g9K0hUbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28875" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28874">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dx9GQFL3ZgG7zd2CskQdykgJjGmb-_sAIdnQFy70vqrt7CGywHAKnzKZSFaEZSS5HWDAtRHT3M3jJZNnvsdrXQBJPX2zkhcewmVXG8LC-UmvxKqTHrmLOMNVbcRgu7mVYBlJ1of4SXvDsLb9H9Kb3ksLxNl5UxxKa5ofCsaP1JGaqEaAFx4GWFf4Dgz5D5yccj2_3AQChv-ag1ki6uWZw98i1mwn8xwF8ReKfa8vfl6kYxpqJ-MPsms9MvpPVScKkLuI4xewIQnc__toDjXykPbNzE6mI3ylnS6_mogWo1kYsGsGc54m6EjaProZJgMZLb-vbJnmiLWFdF6Wq8stFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگا رسمی باشگاه چلسی که گفته مطمئن هستم با ژابی آلونسو قهرمان لیگ برتر میشیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28874" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28873">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNn_YzRhpHVFvQWDojWAsXA8BGJB3Nnxof8Ew_rz9UMpuXbZZkebd4-vp7v4nO9fUN-NPJ9JGk3iwk1VDgOyeE0OealxUQLLope-5p6yd0EpwUWYHUjrIBPionr-DPfSUUSaszj_oqfLOUs-U_3R5-XVcck6CrqC-oVs5L5FNDrmm861Pbi45jIim9-Wu1xKijekLhzx1oP3tQLmv3lppcBXFXIq5xzGkEwJqwdQEbGINQd44gRR2pvQ9Nk1dfFPsVaqrb-HPkQTG9hp54ANYXHeUKcRJBlZAA2mjFTdAB0wbOmVji6GlYvQAPcSoaYQqygc9CORKeNpMIPesNPpyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28873" target="_blank">📅 19:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28872">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2f5Zckp-YjIWV77EIonjaCiw09136VfIChFgGX7GCok-I4AUIsm5Gcnz7jCZAWUUvPAoojH8136-j8drL54cNrZu7wuizFbptRwp1xkxWMntG2Wo8g39Iy6Zi_lqr0oGP_GhCaqqnu-zG7uEdMbqfrCtkcrodWJ2hsP9eZ6tS4lzq3EMbQj9VS0o5fhXZjWe0rQjX3t4Le-myUmHQaC0eCC6o_4cck1EAUU6P73cCF0tLcuS4hTpJDW7ese7JgbOJ57l8twpUAyoN16edXXKngDv-mh0BSAP9BIa51QMn5FBC7rj7czlhHp0PqauztLSSy3IFvXOcrIBszDOBUGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ تا ساعات آینده انزو فرناندز ستاره آرژانتینی تیم‌چلسی با عقدقراردادی تا سال 2031 به منچسترسیتی خواهد پیوست. بند فسخ قرارداد انزو در منچستر سیتی 100 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28872" target="_blank">📅 19:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28870">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ke4a2T_6J-ihnd-ILqzrc6zJxedb0aRtkwVozg-4lzoXuo3N85UkT83Iqy-cEg9PJYpaO3Ia2usE2zLi4VcVGjMc9cpNzSSIX1W3OZEEfhMkYKDrW1SGqAErLCxXvOYSG0DXTxLdHcJWVTW4ROlxwVa7XwfrktL7lPbiWkkzwXSVLKcVAbsJdDII_8aJnYsyIK2iBVvvZmiGUYGVTieEh5P8GwRKuhVvJTrjUR-b0kiBvL96r3SzyeDuuDNBBn8WeSLR-zehKP2E0IYFQCQc9M_BppTx5ERIBVZip26DhH1qetrjoE-0uRUu1HSIFLJR_VXDV1B-_RTxgIUybOWAow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAd4KGm1oDzdG2Qf7rp2QF1mtyASIdy-u1y1pCdFGp-cqzjL4aaK0BWyBb9FsvvO-JL0MrHxmYTvlj3_ePThhRJwZt0VaT0UCjltqf64TJzkKLHWSX-b-FWkY8C5L5AeBjOHbvqTqI3rtI3X_MY3ryOn1x9TVKZVmjkRFFQRs9at2vl9drWc_10fMDyUh51_BHhGrqCp_XiHiG_J-VBYnx-SfgCqkQ0dxtlVVFxAk5k5AtmJUVlFZdbZWGIC3bVXgVnF1YPPSiJ6CGMgntu7wBOVuQ_hRw7oYB_jvoNhNeEsBqFx6hVR6Iay89KIxmFrSX6MGidEBCOu9d7HjFA9Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کاپل‌های‌ فوتبالی که رکورددار بیشترین تعداد دنبال‌کننده دراینستاگرام هستند؛ امباپه در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28870" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28869">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7QXSe9LMLuNd0sjHcrfzj2UbGw4iyyhzWxtaMlkbVu9qMp_lQApBWt6Hiy-ZjaNemTapreL667CfX1RxO854D-GhHDZF1qqhosprbBlLVUxkAiJqZ8uhmKSRSnGQUMp8RPtIN7u6PVg3im6aDtrLvtraXmgzukre92R6wchHC53gHJveLRilRPQHMsNixS548v_mw-TpEo3_7YCeVGErF9LGHMH9IpMj_j_D9tTKbdEzq2VA3s1jjqD-UTMOgeGPQh-goJ2HyAalLJsZnylWnqmz7iY2O4i4pTu5nwiFXxEOmnpmr1-rz4Rcnuz4jPA4SRi9NyMQBfvs4-T079gfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28869" target="_blank">📅 18:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28868">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fyo4EftLlhILiUxl5AYj6ckF8BFTbNwyoAiGbpIRdsGnmDrJ0sSPMzarxaQGTvZe2zKDAYiwEuQoiFcAaYR69P7V3XFt9J3JESiPtKh8_PTbV-OTSlirgUnpq_8Yn-z4_EIjjk4ziGdG-4z0xrUvv4ZnK0X7UBg7H5F_ECK_jgRBqsho0KPcLfr46NJ-gmMyqy_cBpVzKCe1n1L1Se7_1GMakvkLBp8_2XxjrOR4dGbKc2I1eLBHI3OXToGfiYtYDLCNt3VhgvtbC-3W9YThIw0XGLOtzPRo3jx7XkNpiz9afJH73yXwQXhrlN3Ug3Ua7kTrH7FPuVRu2MQm1q9-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تقویم
؛ سال 2017 در چنین روزی؛
کیلیان‌ امباپه باعقدقراردادی قرضی همراه بابند خرید دائمی به PSG پیوست و با به ثمر رساندن 256 گل زده با اختلاف‌بعنوان‌بهترین گلزن تاریخ PSG تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/28868" target="_blank">📅 18:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28867">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWbfj7bI4Ndsg3xD2dGIM2zCNHodauIRhHa8okHnB_QKJQk9lbALQShs-2etcAqvoiNC5YkHii46lhdFjuXtpLtdGfbNZhS73F9lqHm--izRd-sHlyTfWeSINHx-RvmoeRCFmCDtBIAb989blei5Yjf4DDjdRZOyXF7LAyaIU0mY-VPMgiGyOBhBxmbUjVHGzEfIupDSPGhCtDn97Qbqx6QFCnK1Ygw8-OxmGMztgE10Og3aX5lo3YM_FRPY2dpCFLEXw6b85-VLM78ouQWH4jn7OvLeOdIRyiChGnkgXH1iyCnESTSAiYLGBYPrIlI4fFUbJpLq7uoDji9kP1f63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدار با شمس آذر؛ ساعت 19:15 از شبکه ورزش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28867" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28866">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMTjNJZL7prIdiZqH32oiuspAr6kRthJAvlMtG2-Jxjq2-9Mf7IWxnfxapz6FagtWGC9RA0RCJOu7pKsu46y9AdnByguOKbEi332Mee6mKbMHxY66FiNC5JH2IVJBZAUGqi07okSrF4n_PCtG7l0_eyJ1m9HpBj_KP1P_84SM2JlpYQD-XDrn04PKxm6cZiycxXljSc_OcejDRGx4cEuhxco04G4-hd1JTkzhqRfsgEPPilGv1oenCQtZfGJJW7NFJDsIaZklRlMa-SZbKpNg3NLVUu4LWAa3cw2j_dd_AZhqys_lKWA5B_N5e7lhI6akVykWpFTE8AluebCI3tZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/28866" target="_blank">📅 18:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28865">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWJ1SJsoq119ruc6aptk9y9WwXR3DQ0Wu-ssh8y0_neBI18_il8TRc4fE5PKR-_WLGapZznPT_QEdZ1Vy6qLDD04LnhtlhkQ38c_-CpUf3TEIuOwxk6KROaFVKvqmWDd_TLKmu-o-gxsZXSctVhh5OzEEtubE23qNnpqLqGLNEFmzC3DGKtSGahVnUEFbMeywGodlMSJIV2YPdtVKOjfaNh6OxHoBT6T9my-r1tY8Yt8TZ8DjU65_e4653Lfpum2Y7Llxd-UgmXP4IhSyriBy3FXwt4IMoHmZjkGsrhqhHtIYsQNLphLc01qS0shjIU1wFWirjFH4AtW73TseciSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و پرسپولیس به بی اهمیت ترین موضوع‌بین‌مردم‌تبدیل‌شده و این‌حجم از بی‌تفاوتی قابلیت ثبت در تاریخ برای نسل‌های بعدی رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28865" target="_blank">📅 17:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28864">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ae770053.mp4?token=G5CFSnD7w-vK04iBVw-eH8XKtQ7rJhSjwQXX-X-axMU6hMkbJ0aUInWDsmYTcA07i2ciP6L0j3hZG9gzVCDlAjeS506IwrBU5eGDKCD__i0opDQK0T4Jfgx5ysMAZxxbHNGYFo7N15NtGUjW_LgV_A_raVB8wKhYwJauIKafZA9LQcg0FNAAlB3impw02-MFPK8-2LhAhLrDaJ7zjin0MIoSMZnUWKxKwvBzjqp4CdaSznlwF75nPe91117yggsGfsljpSqtMBCKn1MBvC14G0yymGWs9g-dk3CEMsR6zyoYxNCZiHTG8JrZCLH1J6qrLtBH8feRtA6gt-AXOFoBmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ae770053.mp4?token=G5CFSnD7w-vK04iBVw-eH8XKtQ7rJhSjwQXX-X-axMU6hMkbJ0aUInWDsmYTcA07i2ciP6L0j3hZG9gzVCDlAjeS506IwrBU5eGDKCD__i0opDQK0T4Jfgx5ysMAZxxbHNGYFo7N15NtGUjW_LgV_A_raVB8wKhYwJauIKafZA9LQcg0FNAAlB3impw02-MFPK8-2LhAhLrDaJ7zjin0MIoSMZnUWKxKwvBzjqp4CdaSznlwF75nPe91117yggsGfsljpSqtMBCKn1MBvC14G0yymGWs9g-dk3CEMsR6zyoYxNCZiHTG8JrZCLH1J6qrLtBH8feRtA6gt-AXOFoBmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28864" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28863">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN5R8OrChBtg7I1zmI6oJRosCfe33P6aoyBkgD07AbgPR7hoIwp8pZxtmR_olz1uj4mCEZBFLj9w4Wv_nHWtNptZrEUuOfkieV2ztAtNX3gC6WVFpxnCUp0GNE0_eWZoTDPHCOuD7FG27dvNnGlqbWgWapNU_zxvl1Gs_3MD10yznTotCTfX6oxsrWL8Tmxp8KirrCKx8r4_l8E3hKpvZrTq6XjZc4y0K4c5S6j0kN3wSNgT1_mB-k0AQ-OFbdFfJcPRjwcBwWmV5qADfsp0QyrXMsTzg_ABNwn1EpXdXHgf4NCFpbhTTbxmVNfvdllPx71Ky1hN07qZQECPy17VyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28863" target="_blank">📅 17:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28861">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQHNgsC773DbtFBq0PGVb1dXtpwWLmYUCLFGzqIXzuL1j-_zq6YAwcHA3-S7pP0qooryPv7PjnHDJGMh40s1nCX6P9vZmAaMOb3cyBPr3Vkw-nV0AKapn08GoB6StccLLJA8uoUQFoyAYDMTmZDT7Flhw7tc3Ctplxy9ivfvN8KcDu2-4MPhb4Sy77N0iJqeCjL31aPSJI4FUQuIZZnookqgTShnQpfTz3TVHn3Ktm6rMh1Fyp1u2oJwHkyalMXKGVVbBJsDGkzALM_u1g49ibNguorVbRRXDLU6ylUTm_Qz0M_yzc9ondTTECCMZ5OEFKj7dRW3O9-jVrRhyo00PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLgmkn0-zyt3FaCzsanWSttK2ExzjUtPzO6FOdcaWFcrAmLh6MK9G3SjyBwTnpUQY6FTJnK42dyCFd26TRLs2fQgL7ygEK7mr7ferGChnbD80SbtXTa-5VH1DkfLyExh9IxYkxT04vsddIXWVDt7uGxX3TvE89dDhGdd6WTz0ih290WRq4IWX-iVUr2u5SbgAUx2w1FK6yLpL_4hwKO0W03ZS8_WplImsB6nEhHmgwsT84utcXOvMcg1Zy6jE1ZnaTXAprmOCserJSbQdsNOzsobbq4yQghXKoUTRnmMS1vsIHouH7AT0yYiUfBBpguMK0Q23CIBF2Cw7_Xkz2xgNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
خبرنگار رسمی باشگاه‌شباب‌الاهلی امارات هستند که از نگاه‌او سعید عزت‌اللهی بهترین بازیکن این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28861" target="_blank">📅 16:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28860">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvTZJPax4b4guk2uxQqD9035aEyiNOiydr6Dh1tfz0DkcXeoQ-mGwh3pXFu_Zvj-0_ZlBNv4SVrf8hfiXnRb1E44t3BmGUUkWILr_wDd5xmwZ7xVfDr2hd1Y0cdSt0No8kIXAsRxkqLqS_ajtoaQwA9Oi2t-TsJikhhbo8X4WPwQeNw9HEJ773XMY88Oq4OGC6A96d2KVvFEzxpNYp2WMHiXKPFcGs4HghKS9VySjO8OzHM5BV2r-tqyF_YV98NUre5xXCuSDLN0kATCDtM0Nvmrbo80kTVwHue_7i80u9N9tWmGpVCH6gC11E2c25cipbxj21jE_DPLalY75gShew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28860" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BW5jnW7jswZsQpbQS-e8rHWqHh3Tx1qw3z0CRSYLnUxl8hgN2493pez9ktMjDVUjw-uV-mf3muMzyAmLYilwAVPGLbXGP8otIgcwqzDTV3YImpjSTg477WndmaqI2GW21-fbq3ayMfJkVmd-w-v17KmqEA7YU4FqbSJkScOdOCYJvOg_cmGcPQfBM41WLtMldwUqiTIioTDku-k08uyFDnMRCcUGn8NyObeF_4Rp3ZDTvBE-qZ-UDEKVAWwv8QFKeXAC5aIejwLrUKdKsbEIiAxR727pLgiPwE14a3MuGhRJYyqQvAcJaM9UsIowhcnRi5d4sO0VBtsKVZ30E5Ao5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28859" target="_blank">📅 15:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28858">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT4OAxXkjhRYduqEK15hw3NPw6dQMsT0ewVOFjOsSgYcnvXmcBCqXbdP2HDrVtvuUVYaiijkz53EEn8moJHrzV7XAsm6m-7RrJukw_s8YQ3S8_faoXGWOz_xmDgIoTSy6ErAnI2eL-WzvUm-Iz-9Flp1PEzxwmySTUNm3yGUZJSHVsJXR_bMRhUs_PyuvoaPLvlpSoTW44uHbRaXhsHTxeYPCVnBl0p9SGbgqtQY7AeOd27_Vi4Wd20rltcpDfm0JhRaYWD3-_LwDfc-pFMejUfO-_n3bzmBTsWTfRLMo6Mqs3kYDd-RwP69kgas-JSiZKPkZ1JbVKTyVoMelhGHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌رییکای‌کرواسی با انتشار این ویدیو خبر از عقد قرارداد با محمد محبی ستاره تیم ملی رو داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28858" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP69QO2_FYIMH1OZNahwJwuRBv_1f5wRFSRscuCy3bhxwO6cFHwq7uNVw8Vg-3GvZW6gkBZCuyKLEf8l_ZeqVWP4sc-fUcdWTD_hLsNapVdgefUmddanVhh2nSDDFrifHBk0D9c6a946n2Q01epmneBa_pneNd9oQov9bJzoFP5rNv-2CDsv62tsK3y1ma6YYZsX-FyceAnmHdjCuwL3t2QK-BeAWwVvoQowrWZDJ11me2_RAC2pm_mm9DIpJvdALCYrMB-cs6tQiIhDsESNv_tMphrlBZ-Q8QdT2npIx9FJH7rxUgdwvddkzqgfiw5xDjvfa5b-QbNUBPK-5Ldy0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28857" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28856">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9tPQAdYFoWWLNpUdMcJycC1EdMBvbOezl4bsG9mOSOFhWDB177B1JvDpaKe57v5dRf6wjmy0P_HZMwXMyG0DoZLHfP3BO6Pz7PeCIDghDY9iBcF_4gkbaSTYWmtFqerBS8AAtwFBgsq3uc0IF0l_LyTB4YD6xA7DykA9IQawTxpdZpJea-Nl73m_j_xK65XMpjAmdfQsz3pErv-if0H2TlieiwThT1FwkvVTCmEXV9lBBxFv5XxUvTi820QkQBFztwQpvBAi_yvVNAdnqfU9tFreZgNuiB2Ju-MPunMDUk63lmIqUviWnJ4B2YPg1IjQg-dXnFcE_0QxYizLtn3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته پنجم لیگ برتر ایران
🟣
شمس آذر
🆚
تراکتور
🔴
⏰
ساعت ۱۹:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ شرط رایگان بر روی اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/28856" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28855">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=Cd2uvhZr68jAqxbPewGXUrDAt1N-aibAcgB3U7_mgRtJR72nSqzVrEgJrf9iACMpNK8TrqkYpOsFd6MybLAjqQVARpYvgO-ghJpR4Qcp-dXMB5DdT24Dr_a02Sth26zr4dNoPmObzvkuBFyJSoxbW5PLQnWiCPk5VEodMecwiT9qntxMc3JJMkplDY9-51QKk0Oj3D_b9vNKXZABTXZggWVBmcXqK9pdIUGfHotYSJC0EbPouCc19VnmXlvd78ztl5sTLgSgmxfzI54rsdEi8fBNItv6X04d4J84ufisCyz0tLBrOwCXV93K5j7_qw4IAhnfdrrMZBWhfrJee8zKDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=Cd2uvhZr68jAqxbPewGXUrDAt1N-aibAcgB3U7_mgRtJR72nSqzVrEgJrf9iACMpNK8TrqkYpOsFd6MybLAjqQVARpYvgO-ghJpR4Qcp-dXMB5DdT24Dr_a02Sth26zr4dNoPmObzvkuBFyJSoxbW5PLQnWiCPk5VEodMecwiT9qntxMc3JJMkplDY9-51QKk0Oj3D_b9vNKXZABTXZggWVBmcXqK9pdIUGfHotYSJC0EbPouCc19VnmXlvd78ztl5sTLgSgmxfzI54rsdEi8fBNItv6X04d4J84ufisCyz0tLBrOwCXV93K5j7_qw4IAhnfdrrMZBWhfrJee8zKDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28855" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28854">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnMZ0nJ4LMsyxAJELKWDLt0UofnNPbKowPQPeZK8jViWEP4G5cJSV6ahRpcoR9G0sXSuCt3031TiMq3MMHuKJ04icJ-_IF3pb8i1tNQZkIkLKHv5VIot1Pd0VVbVdGHPxNaQc5h7Jyd7H2WDzhHl581dhvjJFbTDIvJSvJfabU8P1dCeHbzRsO4TOms4SIQx3fx4E-03XUAUSIh_9PLEf6bn8w0NTXb2hi8PZhx94gXp-Sz89gPB1-mvh7GBfkHzIXGUnTWZV7Nuf9WH_7l4HEtgMDCmS_qsS416a5BxaXGW2O_fGHLB-X6gTONAd73GAL16OI3likwN0l0T1J2Yig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28854" target="_blank">📅 14:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28853">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔵
🔴
درفاصله کمتر از 48 ساعت تا دیدار فرداشب استقلال
🆚
پرسپولیس؛نگاهی بیندازیم به زود هنگام ترین گل های تاریخ این تقابل بزرگ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28853" target="_blank">📅 14:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28851">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NL3kwRHbc7rFnrhUl9nAQ_fh1j75dtfQULw5D5kv_MMauhU8SckSBJUTcEf5kpzWwxIWjR0nWjqN92kjiFEzouhR9Ow-QEGwbZYemSqXISPrVkz8BqS7Bz31Jg3o_b8P1RaNs0wwsMkRMNBvbGFjNS0Gs7Jit7JVOql-_LGmXjYshhSAgIPEfQCIQMjdGDpH7WOEfN7DI7wZpo-DoLwPeksTd9gF3HGFUgZyR-i9_MRDdqkimIwusIpNV7njDzeKPcc0uRz0Op9yL5XErsK-YmL8DhfdDnhtceUXfXsXu9vw_y_4tHvmdI2Gu0WiEC-kovV0LTws7lX_9JikG5hRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0aOi-SMv-AY2oNZLmSjrtmD76rlQZS74gk66UmgJU0J-9yPvW_5N1zTHKYgfjKUjNmv28W-jRTza0pvulN0OOFttgvHURy8QeYEYamQdrV4Hc3z4ORCm2xSrBkGqf18nRcji597ojPzB8x-mAUQQZeuU12dhO9Z4pPd7gss77kYtI_ZDeZP8cYIduOM_t4w4Qh7H7IkRksYF46qX0aBusKRBrXoFFtfaGl25_SsAM648IrA2yGTAi05YBVmA9TnLbRoaX38mCtNCw4Md1YQ4wczUAqDU0fo7LWC7JTHG1Ls86-nnpXKk7EdUzX1AoO7ErhhAV7XlWDqDu8bsHOyVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28851" target="_blank">📅 13:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKlOW0u0omfCKBgU_3kvbytjW8OTKIO1li7d-kVyNM5tRO-qA2kpugjTMfIYMDoaOnyZ_xIAQYsVPG6JQsWtryVdpWUxR1bQ4HYjz4Z3oCzvLqabjK_SQiOnCfxkD80SEB0HVKAAe_c7pKgR1ktOnGLmKzwTJ129ajgRDS2F2fKCn0Es8cqQ_CvIPy78Cv-2TizILmEydEJqXVMnQhGOILVHXHaVu-Gxb5j6fK_q4kmIlWS65CnM4qsWTqU_RMKPJJeGQ9K6n8o_NW_CBRbCGuEQH9W0il4pmeee0EJ2yzueT1RNelDCtV73873m_aMo1t9mc_cYS61Pqs4dwOdLBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnpzI2BtCwd0uYDinneScpa6KgfQridaNYkOYWsFXRbHBk1k6PFAE3laoVfNwg-D8TjM7vyzvQDnt1AO9vZLLwPiiUeI5JcIDcjmvuHPL5taMhh8HmoGDE181WBj_xNcr_GHDN0VOaGVM_st2QFryHLR4nFyIimZD3A549APdJnZqONnFSlIRgbTvGOHET6EHlznpXz4N5bG5ZeLRRXDgYpjqMGFT1d6aZDrLwV3rzApM6ESQRUyLg3dwN3-rlMzVK2f1zjxrbvblFbz2cmFTjyGPr56gC0y2wmEirEdTFMrjtT2Ib9rUo5pmBwGflpPwKWckdTM_pkz8caVM2RPWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
پوستر فدراسیون فوتبال آفریقای جنوبی برای پیتسو موسیمانه سرمربی‌جدید تیم‌ملی این کشور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28849" target="_blank">📅 13:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqH5jplSoPKeWajcXsp0Grydrp5sod6NoCoGzlxXYMLPwWvD1mgQ5FiHLqmuwUtcnZKWSh_lueqorSIjQr4SiIknvpydxXAkPIog570KFe7a8Rf8En-qHlDD6-A_LWMzlbDaW8-VOUNl48Ht5vpRbbManzJsVu7lqmiXFb7s_uXKgLh-xcQYIewp0v7020K6I30Shnzv34tJvj0k4IUXvJfWqFdKqCB-UBei4iqQon6zP06qNTR3JcLCX1Hskbk_NTdSFs2IjAW81QZn5e8DbgEFDEOe5uRwVb7FSNdVjN_LYvKMLzPlmNHEYtUcyxlNTlKwKMbxHOU8pOnKnfW2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
فابریزیو رومانو: انتظار میره تا فرداشب که پنجره نقل‌وانتقالات‌تابستونی بسته میشه انتقال انزو فرناندز ستاره چلسی به منچستر سیتی نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28848" target="_blank">📅 13:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZez-INtnH5GE-fNIHinQxIx_u-ftKIgLkWgw86K7eZW5Iqis567376WN48eFZcb2eduOUASuxzXne88i2kUj-sKp0uJdMqX8PCphuVEV2TMWts2VejQWHIDS_Qao7pwbJshNlOo0-IFfq6E4LYM9GLm48fG_h5YgMkuJUvC__ytn0uvHpvdEC2XwCvJnJBkKE53Pn__rMTwHdZHiV9at_XM_VKtK8_M1pVIavs8WKrHNg8DK7o5pi92CLb7dAbV202V1j3vSf_WPA1Q2HdTuuypyGNY7y39RHz5XNs_f9a7CIsKc9Rlo8ZXduWAXyF3W8_WnQqejZSCtSVLan70rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مورد جذاب گابریل آرتتا پسر میکل آرتتا اینه که چشماش دو رنگیه؛یکی‌ تیره‌‌تر شبیه‌ پدر، یکی روشن و شیشه‌ای شبیه مادر که توجهات بسیار زیادی رو به خود جلب‌کرده. جالبه‌بدونید در دنیا تنها چهارصد نفر چشاشون‌دو رنگیه‌که پسر آرتتا یکی‌ازاین 400 نفره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28847" target="_blank">📅 12:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEi3dSblCkcyRGBTfaX8zOd2XyM6shTM5VS0PAiiSTfzY_oi3dGowSKeiyDOvhD1D6vsKPO8ez86crdMS01z7PgZwXN--nMpn44PViWgAEFGyyWdMcj30r8kmxZrxulG9rVRVcREiKUW8pNJG1E4T9G786FUwr8k_BERKt8O22ibvBGW2YjsMyzr9xHHkXETP7VOvck8tTaSM6x94CuxU-hMavZuEAMk_zSpBRo_hgdHt3zutKaFGKGhZxUi_VYbCibGNgPk6a4Og1jBzHgSsKBoHlzwwzd2nR9XQNjycUaVt0hecOyxJbaweu9NjqoYbtgYY36tjEO7ZNVwsLptFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
نشریه‌مارکا:خوزه‌مورینیو ازوضعیت ادواردو کاماوینگا هافبک‌فرانسوی رئال‌مادرید راضی نیست و به فلورنتینو پرز گفته او رو بفروشد. پرز برای فروش‌ کاماوینگا رقمی‌بین 60 الی 80 میلیون‌یورو میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28846" target="_blank">📅 12:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">▶️
ویدیوکامل ویژه برنامه شب گذشته عادل درباره اتفاقات اخیر چهار هفته ابتدایی لیگ برترو افشاگری‌ های عادل علیه فدراسیون فوتبالِ مهدی تاج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28845" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BueRucmrDWDb5mb6ROwfoLGW7QXRCAH483KiMA-5K_mFbu4cbPwJrphxx7IE5-P6zCZ_kRb_c1WXGoqEDICf-t41MA8v78M4ltoitfV4ow9v5r63YORDFj-wO4g_VJwIsJW_O0IrbQ08kTWfsIfW0h1U3WK7qYlHioqDfR5YRz9yRZJVA9AeewcCYjZhF5n1jR2OpHY0dGL2zx10aFOsmOhlJNxf530j850p-O-e8rITGCd98Z2z8MfDuc_8v8F8oq6xCQoM9U_Qc-V43ou_0-kRnZwKKE8V6gu1kXcHtJSfEtwSFFg23fxM29XRMAaxcrMgmcTi5_G7htAC88rzdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
دستیارسابق‌انریکه سرمربی تیم کره جنوبی شد
؛ روبرتو مورنو سرمربی۴۹ساله‌اسپانیایی‌ودستیار سابق لوئیس انریکه، به عنوان سرمربی تیم ملی فوتبال کره جنوبی منصوب شد تاجایگزین هونگ میونگ بو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28844" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBPohQg3B-P-bjBh2FqyrtKUKpKXnRawNV4SlEuexBdT6SmqQX0_TAZtbu796Z0ovi1_ShwOVINIVUay_noPQWHkk8bypL7whtbNT0zbGT3gnANTDPOhPzrC03qDeiw3ZsT66hKneksGOzzociOVW0eYkcNqdxprvp5TLVF1_13iEGKqyn289jeNzO8BPxY2gxrL8z26BlVKOlQhRkUFnsociavh3tuaH7jUojDkbummKyrrJpuj4n9odaqLGlYREe9m6NHLg4VPedQD1dMFBvkeDocpftTPTRp2SDyDN1RWjAvuq14AJtDOoIRJN_vvQl4t40B-EoG_zweaH0WH8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌کمیته‌انضباطی فدراسیون فوتبال: بعد از برسی‌های کامل مشخص‌شدکه قرارداد یاسر آسانی با استقلال قانونی‌است و او مشکلی‌برای‌همراهی آبی‌ها نخواهد داشت. بدین ترتیب پرونده شکایت باشگاه‌ها ازاین بازیکن بسته شد؛ خبر ریپلای شده هم بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28843" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=KbNbHvVSdq8w59gpP8SIQrXdW34iqZPFISgRHKsT3Ipa1Kqq_mLqlHi6Lr8NJnPrcC3I206Wn0FIqQJfLuOCIyirFBiwgGy3KA9HLr6GUul-mVFy7ta4w3gHjKJdL7woEUfWfmdFthI1K7_uIzDlT1TO2j7sIXHnSvX-yxVTu8d5mtV8wPbTmafLwdUwPwYZSkUm--Z_fLQD1s-3fnEIxXkH3ljYNMQlprQFPc8ylMB2pGxt-IHADSlURrhz_BUUYh3hRAXkokZzEA_MENn6mWPpfhbU38TriDcdUuhFML-4sG6K7fYzI57T5FwGXhE1dwTBHTnTrQbgdBgAGJABIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=KbNbHvVSdq8w59gpP8SIQrXdW34iqZPFISgRHKsT3Ipa1Kqq_mLqlHi6Lr8NJnPrcC3I206Wn0FIqQJfLuOCIyirFBiwgGy3KA9HLr6GUul-mVFy7ta4w3gHjKJdL7woEUfWfmdFthI1K7_uIzDlT1TO2j7sIXHnSvX-yxVTu8d5mtV8wPbTmafLwdUwPwYZSkUm--Z_fLQD1s-3fnEIxXkH3ljYNMQlprQFPc8ylMB2pGxt-IHADSlURrhz_BUUYh3hRAXkokZzEA_MENn6mWPpfhbU38TriDcdUuhFML-4sG6K7fYzI57T5FwGXhE1dwTBHTnTrQbgdBgAGJABIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های جالب کریس رونالدو فوق ستاره پرتغالی باشگاه النصر درباره سختی‌هایی که کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28842" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh1INdjyJQA7Fntp34cWZ54jue74ZNEfcuY2cyQRbL7A7zjPYmif9pzzUQBukdkvyjSJQkirW4ilDVneTRf1KNRkIUYBYJB7t2VAOCZ2rZSwkuM67XeLAuPE26i22M8uYzUZDAIKCMZAqhRn61w0bEbAbFIDc9QHI5mowdu4nSR4ZHaWi_Bq-FCqkE2aWtsqB2pDFY-89hq9moED-1FrrvSqATW7icAHRgbet2DXSFKOP-QA5Ef2L0BeBggZrRNgjtJM4SdTjbFxiMoEbx0gyFgbQgHwDF6C_D-Gt-ivrJX1j9lONMDzMcqSzbkjcGgWc5Ww-ljfQfe6cq7g6f8RdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28841" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28840">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWnBAeI7XH46G3RbxiJV7tbhdIlFn5kbYxeQq7DuUMJuH-sBKOb3VpGvWgt-1IbEAPLXv5XiG1KHsvcHKZqvKEEFvI3eLiS0M9Swu8wX7i1drzv0g5y652F_9CEuQUDlOy9yigyRYocnEQ-ygHYYcP-9vdJ-jJEA5ZV5IWRn3AuunstdCNhkikGXaTLH3FlVTAk7wUjYHJfecBqdGdxrbOpSw2WfXD6P5B9fglhCLW0lsCaLXpP2uV-ChxfcUBvQlfrERUQ1_sxNA2y8yo1GS14OT3S_5PfB7NPdj2oeHzJ6pIy8FPwzwyqy7RsuegyBHNLf5jpzyEwUXg1kLsWIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28840" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28839">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw0u3ZLTxdZtc_tLK31qg0rx20qO6BSPLIhRaFok7CRLjpQxqUPooUvWUSk6DXNkQOUfRLVAWa38XFgQY-VkbTeGDkC_OWkjP8_cy64rSMqlo5IO_0bohWJC7RYVXVkO1kqAVymZBrbntJtgLUUqDLIlDEGqGeGHlbuEWgiNM8zif2X3lqvvX6_J3mHV7IvEfqtPl1Uo2sDcqk7FGh7JiJ5VQkuQ4ifKbtP3uSX_xaAmXmGtU6921Q3C9abNoLamRwQ8iKkWVAJOWkBNIiy9bO-HmuLH8ER0PLhp4jekXISI0ec48xQzMKDIdRUh5hpMQtF9HzzoS3bzz3MlcEdTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تکلیف نهایی داکنز نازون دیگر بازیکن خارجی استقلال نیز ظرف72ساعت‌آینده مشخص خواهد شد. یا به جمع آبی‌ها برمیگرده یااونم‌توافقی فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28839" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28838">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQr6DDxrDUQ6VpsRBNr_GHm8MFkBBYCwGK6LukPEeeX0THRCIXeMEmNOgxzjwiaWt0mLnDzMhM3RdQ2crPEqStV0bHgPQ7NqftOmH9EWGPorFPa43Qi2ChMkU-RI9N_CFG3DMLVnSfoimV5eZCMoP64xZrq5GngGd7WQRkGRzlUpJcz2716Y6s3bXMSy6eBY-5CHdAY6S-023-2Leed94hAt4VAtZdqSciVckbFIo2atKxDJlFTBoZPi7XPoCXslo3NIq1v-4upyCCppXojff55FBqV5m2KPKR2Yd_jWOQqe_OvmielRNAojs7_DfYF9dbeppCRfU80VUkE_qiWFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو خرید برگ ریزون و فوق العاده الهلال ظرف 48 ساعت‌گذشته؛ گابریل مارتینلی و اولی واتکینز دو ستاره آرسنال و آستون ویلا به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28838" target="_blank">📅 10:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28837">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrCzd71N2gb3zMHXbRU65f3hd-Coe5_ZHDUukwMeSyqGiuW1u5y1YrO1lf7W7KUOdE7D6xxOg1AocxTrIbNJrnhQetMqXkQUjffy6ftYg6USihyq3itl7HCppjhe7Pqz4BX2gh518cZPegEaIjsgX3YI1eskfZqZblaoirhI7pqTjIWA2essbHRJuXXWi6fW2HgiBTqO2FPAiGTQpwulOU-iXR2cgfR0zpWd0OqUIHgoIT4NFc7BHtmczUvDSn3xQ_V5OU32cPqK0r9xZiW9OKOofgIglTDmuSDROql043AQChOEIySvw2lYvqGnshfKaliCMtJroW_d2nz7JZno_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فاطیمه یوسفی فوق‌ستاره 21 ساله فوتبال بانوان ایران هستن که با عقد قراردادی به ملوان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28837" target="_blank">📅 10:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28836">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3b46jLJUrQ0Ur7BtZRLCT-Tce-740LAwpcUv6hs76k5NRlVWwCUjiv8WMwas43dOTpbo1a4I2rORA4yc4Xpf98anxBgXl5ma9eGbEQiKx5Z9b8DFPNu5yW54xcuKNdYt5l-H3RW7buxdFI1_w2SFHgGWFf9L_KyBD7iU7lQYwB1Vcc5L7mYgv05v1uvJNX17bzZyZieaE6nKz93IAZpichzgqFdhbM6m69ZR3tE3b6mDibsRfZfTbifaGVga6iDTYRA0uAYClPsZpTcd_h7qbu-7-UOyHvQHJfSDZ3Ec0BU_Y9d-ZoCmNRo6jX4NjENgAiNi7UA2vDo2Ij3puA70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌ساعت02:30 پنجره‌نقل‌وانتقالات تابستونی تموم لیگ‌های‌اروپایی بسته خواهد شد و از این به بعد باشگاه ها میتونن تنها بازیکنان آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28836" target="_blank">📅 10:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28835">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=FaGlIh5d2wlFODpdw5UYClWg9kUPMkC2VcU5tBdjC6en70EJnh22NHB9cbTv6gPZqMUD1Y51c8HsPyjnRaEmqKV8mmQJuiUZXt-dWNp_ZZoHXUyb3ZT_JkPX-HFyHLdkfrPAkxp-8x7i5-phXvjjo1FLhPFpu8U4sTeXuwxhKEIb7obZXmpG2Kc0Jg0kHLlymgS0t1kXDALqYFMbKYkQRBiOPtdb4eCSTCvAxv94LTgNiMAUsxkw8R9Zx1IKhpojWf9FsHlTA9Pm9P839N27AFtYvSYhynZ76GIeYCJZJ4jbFOheKlrYVHEto2ViLkfG3ykhJr4XMH0ddeTitqd6ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=FaGlIh5d2wlFODpdw5UYClWg9kUPMkC2VcU5tBdjC6en70EJnh22NHB9cbTv6gPZqMUD1Y51c8HsPyjnRaEmqKV8mmQJuiUZXt-dWNp_ZZoHXUyb3ZT_JkPX-HFyHLdkfrPAkxp-8x7i5-phXvjjo1FLhPFpu8U4sTeXuwxhKEIb7obZXmpG2Kc0Jg0kHLlymgS0t1kXDALqYFMbKYkQRBiOPtdb4eCSTCvAxv94LTgNiMAUsxkw8R9Zx1IKhpojWf9FsHlTA9Pm9P839N27AFtYvSYhynZ76GIeYCJZJ4jbFOheKlrYVHEto2ViLkfG3ykhJr4XMH0ddeTitqd6ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28835" target="_blank">📅 01:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28833">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLNY0gv3Kjk8COzSAKI4BbRGyDaMWalcS7hiBn8dGHcBWRHpT1gyXX0_w_gfywOnSAu__3fx53AtGyijWZDQjRWhzcT_Ud-VrOBxp2pOdhrsPu-SZxPpLA_InIVU4Hcnm_uAdf523PmtNfysmA_QcZ7k5DmuL3GOhJyP3gkgKvIzsQVH0xtT8mq5hzXs1V7cbrtWWifTGlW0i3wJ9LHcjSD8Zw6SOU8w_yzjlONb8i73CcTj9byK6GjLsQRUBvDXcGcok9MgFRWyBab0_9gsOf9RdEM-DnhGCZty48l78mVuedYyjHmNSxDkS4lpCqzHA_7bYGseSEct4JLc8_fWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛شروع‌هفته‌پنجم‌لیگ برتر با جدال یاران نکونام باشمس‌آذر برای حفظ صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28833" target="_blank">📅 01:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28832">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYaqUyPeHOZo7C8zWwV9qX68jkYIriS3xHm17NgD4FIxDxWZqaVJZPzN0zLrsvlA_gJxQMKRCwXfmhBcs_RJPfiiwZy4peLCdVrRMOaQr1dLS6X9l1TYC7Y1EfCwXD0QkcC60piF9gGqeuZcIkFNeD8SGcIa0MWkfUEOHg0n-JwBXnf-UteYvBF5CSvm1opdxP_ujV5xTxwTe3UGp-LWOR4zScWnvoTy6iWax_co8XAHqnjI-fOqSHOm7_MGv794gat4sMyR1zzUqC34K_vsRKWQwj3bE1G7xynZKXeWOlR6C90kD0Xzib1BCblHUYD-3oiaY9M7I-F1gDINpXyCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
برد اقتصادی آرسنال و جشنواره‌گل بلوگرانا بانمایش‌بی‌نظیر رافینیا و یامال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28832" target="_blank">📅 01:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28831">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=MZ-65v8WLbv5x_BrwTx2rag1nSjIMbAGCwt8CHmaYMIydVpmcOXVVPmdVOAhnsXwdX9sHWY-eGM7fJfE2I7qI-X0J5qrFnt3Zfst4RSNa1EJcWsfbKgMitaytdmEjyWO52VLuaBOVtBuI803G5IyTtZJGqh-_fVuCu_rG7aL4034Npm7GnNA2bMZtumzPwe1kvLJPC_JmWpaJINwSD-ZhxMptwPhKVCjeK6-TCO6I5S1DF1LYBmNNmvUqE99hoU2zmfP4kHdQh5aPlNVQNG6vElXLEYgVAuuLraZlGjYM5OuCuaielLCwK2Mnsh9bLGIs2eqR-QUE7QBSL-gqQk3RIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=MZ-65v8WLbv5x_BrwTx2rag1nSjIMbAGCwt8CHmaYMIydVpmcOXVVPmdVOAhnsXwdX9sHWY-eGM7fJfE2I7qI-X0J5qrFnt3Zfst4RSNa1EJcWsfbKgMitaytdmEjyWO52VLuaBOVtBuI803G5IyTtZJGqh-_fVuCu_rG7aL4034Npm7GnNA2bMZtumzPwe1kvLJPC_JmWpaJINwSD-ZhxMptwPhKVCjeK6-TCO6I5S1DF1LYBmNNmvUqE99hoU2zmfP4kHdQh5aPlNVQNG6vElXLEYgVAuuLraZlGjYM5OuCuaielLCwK2Mnsh9bLGIs2eqR-QUE7QBSL-gqQk3RIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28831" target="_blank">📅 01:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28830">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1kFitCoEp30Q3jprxriHuc5_78V6ssz2uoOPeqZrnTStWCO9UrrcG56qcIskFGe18gDncCxSsb6il-l3Pe_aUYTbHoND2duPGp4osCaeCbpl0h6WF1QbY6_4CWTql8FL5GK2r_qp10U9uzN_pdKJGwTj2GgLUJd6B0eZFYx7IoZfIn5odUlwW2pOqVcfPoS8r_YaHz7gt8VPcZ7mPmSPCUrkwRD8PMvkUE5c6qJBVb6UNE9g5ENI44Bfiqjup0A8KVrHIyq28DSiP17zwksHln9QlCymKYyzdATfs8udOfPDCY4ymDo1M3nkfhNCzgaM6n28fn-IZoeFuyq6VKdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28830" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28829">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3x7GfICHxsZqpSm3D2mhkzL-jLub48002ylbTjUgEIcu60iqDq0jJaGaeY2rIzlk-ELzzG7XdetiS56vGiwG910gr_C46mO5ATkFqaG89Zi9qWmg0pxgFuol7nPCtnYIbsccgZvvo-bqvQn6RZuUhnUaai0MREoupLFB6-8ninuO4UfBnsfu-9TPUXIL_mKyz0l1xY2QtygNcYEbz6-ubaQDvAFsy773Zu8Zxh8lld5jnIhmY-IK-O93b9n7on2g_b_xzAUf_Dlg3fTOsSvB0zR54jmBHXhCiBgl_xJrhFzot5l5qaL8-BgWXzabMHKftYmx2puvCiCrv8TuBA43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28829" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28828">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=UAUI4h93nGTjC-8tUvx8wh4kRJJvsXgrWfamXPbwPmbWNdO4oPWTne2SBMu1RS20ppGn0xXhrdZqcMxSjyd6vs03aGvseuyIBKXQ-YYsPBlh65wh6mp232OFKUVykHzjYhrazPIcXUQngr25pn9d5gFv7s5ycvTYK-VXS1nuO5SvLTve3XAqvEPJMnKDXTsr6eOk_S-yOSrcpPtR48cG29bzYyLdU0qcPCuxrX3BLBK1lluBS8TopUt42ua_4Jd0MZKfmWF1WoPjJkJiWxqZ8qrwrSWMF9rLJ_q2TzYoCOsbPF_gGUMMZ_71pPGVGEOhgFNv1zXND9ID3ZUQBYw8tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=UAUI4h93nGTjC-8tUvx8wh4kRJJvsXgrWfamXPbwPmbWNdO4oPWTne2SBMu1RS20ppGn0xXhrdZqcMxSjyd6vs03aGvseuyIBKXQ-YYsPBlh65wh6mp232OFKUVykHzjYhrazPIcXUQngr25pn9d5gFv7s5ycvTYK-VXS1nuO5SvLTve3XAqvEPJMnKDXTsr6eOk_S-yOSrcpPtR48cG29bzYyLdU0qcPCuxrX3BLBK1lluBS8TopUt42ua_4Jd0MZKfmWF1WoPjJkJiWxqZ8qrwrSWMF9rLJ_q2TzYoCOsbPF_gGUMMZ_71pPGVGEOhgFNv1zXND9ID3ZUQBYw8tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه سپاهان از باشگاه‌استقلال و هواداران این تیم‌بابت‌حرکت‌زشت و زننده عارف حاجی عیدی عذر خواهی کرد؛ این باشگاه همچنیین موافقت خود را با قهرمانی باشگاه استقلال در فصل گذشته رقابت های لیگ به فدراسیون فوتبال و سازمان لیگ اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28828" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28825">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0v-w0vqxikZyhb3pPP80SJaxsKRPQh6-SCWL1xCDgFP3XcQFUtIXGOXpcPiM_8MOWEE7aeQ2DSSSoNqpFIEmt2jBBp7-XvWzigB_fVqHuCgpGsn1slFohH4AchVmHYBvZdGvQfwpJAU_jL9PEJA6QDOSOHdBDib8MxTQ4OcNruSnk5xbhgGRUiZXcdqNP2FroveBP8DYMPKL9uzycpn2-guGBAg8x-jIboS0aaIqZaI-gnc7r6v_93gtEQOyB5VISeoJv87CjP7WtG89MPDhf1QEyN6SESWaL63QWOgmJEyruuQi8MjFXllej0mIAOV9wPlS_Ls50U7gYQvkX7WaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت رسیدن شهرآورد پایتخت؛ مقایسه ارزشمند ترین بازیکن دو تیم استقلال
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28825" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28824">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=DEATNunMTATZWe_6KMTQWTub9w2Nce3AjHNU-N5dtyjdtKk5mDxt0iA9ACddymWjgSgOVJsqMd2_QBhTz0l6G7TgLW-C0Ax5G_u8ZvLQj-a07V5DK-h5lC-Khp2xXD2VADv4-sn7G8R3pM-b_XhMI8isWAMMyAiJLoo_03KhdoRgtuQNXw0ifw1k7IJyDhj6r7lxzvOAnRAqls72D0EPz_rvDjvhgSEppqJg0Tofd1vrS6rGSEnjlqprgFrsy4ye4-hfL2WBD_C39kEQigS7gS5zk95GMNjemURHxYImNkjhSR1XcrvUHzauk60kMJzoPGe0Wst_YjVDI1ogKwQGJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=DEATNunMTATZWe_6KMTQWTub9w2Nce3AjHNU-N5dtyjdtKk5mDxt0iA9ACddymWjgSgOVJsqMd2_QBhTz0l6G7TgLW-C0Ax5G_u8ZvLQj-a07V5DK-h5lC-Khp2xXD2VADv4-sn7G8R3pM-b_XhMI8isWAMMyAiJLoo_03KhdoRgtuQNXw0ifw1k7IJyDhj6r7lxzvOAnRAqls72D0EPz_rvDjvhgSEppqJg0Tofd1vrS6rGSEnjlqprgFrsy4ye4-hfL2WBD_C39kEQigS7gS5zk95GMNjemURHxYImNkjhSR1XcrvUHzauk60kMJzoPGe0Wst_YjVDI1ogKwQGJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28824" target="_blank">📅 00:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28823">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcKYNBo8-YqZAamKO0Uf07mv476zloFVhr_PqOYKcQmIzjPC5I36gOfhS2ESYqCdkmZMI1ajJAb_pUBW0NUloAWiWRWOP-EWeMR7MyigXSxRpX774xlCOZM8780_MXjyU4vmbsfjjrPgkm9svoBukqixnTu6tD4NMy2saF_rD8gjlPvxdhawafV1rBQQsdUaji1u-8KTRuLTA0Fc0HqQWwkmfSpr3y19V-NtMQf8ErE0b6E85DCm8O0s_k7igoJiZcD_LwYicxeLdsbU22SvDlXnzrK_h5hnNw36MNv7pVgJrMl2evqG4PG1IHN-B6fKyUNShmC3XuxqVroMk0FHtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌رسیدن شهرآورد 107 نگاهی بیندازیم به افتخارات دو باشگاه استقلال
🆚
پرسپولیس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28823" target="_blank">📅 23:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28822">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqFG2vgeZeoFsLmCMvCppfekwofqENFBWzzq8uNa11OxbAQAO2E9DaApbmkFOZj7b6yxHyO-uGEb2uBBu-A0ZipKj0a7v4xD693ORFTXOY7xexHDjFb74Xt6nrHC6h9BPFwFYL2JW2T1X3B8UH68NGnguJPIWXYcr5usqVMs8ICC9tlhz7U856Efbgc3TU8VY8zz3XzLovOHOUL6BCkGN-2rlpUlHyXvSFAaQ28tRRJaRPaGtX53hhcSy0CWhSG5i5jY9TQfyW-DdtMZuCJO3eN_L5pPFOF_jwiWyGmaYKGPzy9Ho6naeHW8Y_6tX_IV0rEeCzDqWdE67Ybka2MSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی؛ از کوچه‌های‌روزاریو تا قهرمان ملی آرژانتین در جام جهانی  دیگر لئو‌ را با لباس آلبی‌سلسته نخواهیم دید. "خداحافظی‌ام را در تاریخ ۲۱ ژوئیه ، ۲ روز پس از فینال جام جهانی نوشتم. امروز ، پس از فوت پدرم بیش از پیش به درستی این تصمیم اطمینان دارم"
⚪️
…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28822" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28821">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_Ty50dPAAhwJ-WkHEVhgpQNEiRKrnRTShyvfN8xMEOBVJo9qG8EkmM_kvdDhkynL-aCfLjHH0L5_Y8PmxB-f2PhD0GtAi_wqMjm3p1-7Q2pQNuuBvimKwy7KQwBYdJoraZ3uETUC4YQNP67V6ZmamXOFd86mnzffoWqpqGRjRSZonYtrLRre5jQKtRvEvs9nkx69eVmSzeCtQm8oXuJCsJfGjiZA8ysVWHWJ4LmkzpWK5Rtvzvb5dhFWy8vso9SQq7ZBA5b327ukOhR-7BioeyG1QipvVQsovnOcN9oilEZlO5yHA3BaDJrdiK5sIPthBvE3slPioTydCsC8lyRfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28821" target="_blank">📅 23:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28820">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=dGhf9Arc2Aqf5h1ebZqXQy9zcnyTJrHZknjcFncgSR0fU08_744yNiqGYv7Twmf21szsZDtSDREEsI-xzSOjUNm0fWtsIeBuwN8LU_P1acs_RogET1yKNIe_f-o6uNHQPA6EF5NpoV5zBATNOBT2gon2WunLqWs0ghvjsNk5KuiyNkyos3qExwYe-w48sns_yeqROGQVc3Y9WiGzsNpcI-TpOM64UvQLdPVYEpKef2yHhn3H77Ycs9KsuQrahZngGPfdYM3l1QgD7DhV8ToyxQcqJwOhQvvVdzmZxUJkbER8vo42sAkS3tcSj4Rf73s5Ey72ZDo094PuczN68Hpj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=dGhf9Arc2Aqf5h1ebZqXQy9zcnyTJrHZknjcFncgSR0fU08_744yNiqGYv7Twmf21szsZDtSDREEsI-xzSOjUNm0fWtsIeBuwN8LU_P1acs_RogET1yKNIe_f-o6uNHQPA6EF5NpoV5zBATNOBT2gon2WunLqWs0ghvjsNk5KuiyNkyos3qExwYe-w48sns_yeqROGQVc3Y9WiGzsNpcI-TpOM64UvQLdPVYEpKef2yHhn3H77Ycs9KsuQrahZngGPfdYM3l1QgD7DhV8ToyxQcqJwOhQvvVdzmZxUJkbER8vo42sAkS3tcSj4Rf73s5Ey72ZDo094PuczN68Hpj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28820" target="_blank">📅 22:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28819">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3gu_49n2IWFI77o3f5m5745NkJQYd78iE0nrrT3_07fwqfiAen0r9As_rfUmSrw3k_xCys7fBu6iKZri-8ka7wTh8ACLCqhd_zXDzFJb9XkofqXSs4ZDt4C9wSGQQU6K3XGt53M-545FUZzbW11855vvx6K2leSMB5pbodzhEbwxWylF2G6J9NOkfOo2r5OKNBWEajpl8bWs37e405BWQmOr-L72m3NLTPoUXnLueGRyOJrecAyWJcJljpuvfGoHIOYOxvOtHRDS6YBNhiQGIN9BNT3q9bHl7xvo_Z_-FKCEfcghqSsOTwvoK-PaO-uysAddyolblgwsAOX3pS4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28819" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28818">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVKJd2qeI83OiseDsf_q1qyk2Opga8oQ1svOCZC1jwGOeZtw-KFc4tufO90JZ0YMA5hosp_pUg4OGLNUJ4-u2pG7PMowBUd1vU11gjPt1uKPUBCxijmiVsKySO-H1GsKyUd_3BA4PTuVbFdkRyj8sBnJP_vxCdMb9QuSg_1mCJsexs2TpU12IKwRUEEswBjUTWPi_P7r_oTtGGAotC_U789ONDh0yoiPrpQKLmB4_DZYsnnUYWwqaS7ksVECAuPktwz6CZkvS_HcJXQmancDnhu0rK8X8N4ZK5cHOBkdP-CZZGmK52dHh9UJ08vs8eU__cbAYv_FRZqZmDk7nNceMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ایلیمان اندیایه وینگر راست 26 ساله سنگالی اورتون باقراردادی 5 ساله به منچسترسیتی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28818" target="_blank">📅 21:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28817">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS1IQC3__FQkCHNx4YzYwnvCoMjOAGEf28LigESBnNJO-AsOLUjM_PRF10pR4BTK9ZrH7gMey-MP2Jo64i6B6F4EB6TnjPpWqPf0-ozcmuEhySsJMjaGdKiUSa3RmLLn5CSahm4_SNDI1rEbp6epQTjGJjX0WVM5XF9m2x4R0cqtsc2N6jMEHaJi-0FYvF7gNWoU2JPCEm-BcVqsUe7JkV667qTj85kmflaWseZH_qTpxvCqWsghBgIh_-ftk9qrzPo7w9Yy1YGdqouqcQklJvsu3sRBHA0WWAoua5EP15mNZEYvVOmG8M7WEfHvi05oteK68n5uA55sbjYr94uSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28817" target="_blank">📅 21:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28816">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoNOw35JeTotPVBGJ1gwgFaqVyftl573Okhls3ykShLDfskddu8kEaTyTYd5UDkqgwQIm4gAyfGaF-k1M2zuVYEk-xFyfFmt1qhvxLizbNOGNcnPBBIBpvsseL2OTQ90A8o299ahxzKnQVE0BTOVLmp3aTz9pyIBkbyEajpEo862TTONoQ0602HmTUJsKEWzkagGlV9GfGL3lfwNGJT-1lcGiry6u0WhPtiHvkZYdeAu0IHtzlWkIxsXYb7vUMlBtJbeg38di6Fb7gbf40bF1NwK_QQcudDodJ6ZWz85sB3MrdkRlLFAcPvoLRPI3FG2QfJEuFFn-R0H16ETMcnS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28816" target="_blank">📅 21:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28815">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28815" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28814">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLKs5CNsZlp7HsM_BYzopByc-gqeKif952ySZ_7WaEsYXu-Ws-POGJ0919IGoBAVmTr19Wi0kQJGO4hMV5RY-8dzikNG_ZdQG-tgX8-_F2ehnyRCZq4-6ikEXf_E1q-APUJfW1IvD1eoJST_WrBsgNfeWmXck1jam1B76_TR_jbfF0fXdtdZgF7gpvDIPXnzap3Se4LFa9C9dLcMCyJWHo28ZuwyWjlTkchXghQvnMJ-a2LHrt09ZnLGSv0H1wRDSoI9kioZ2qcF6IIaLAWXKsOqN-Z0tvu8kYeG8_RpGdzY3fU4zzJWXE_0OSv3fKW85rI6BfwT4f_y7zq6-wM-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌اسامی داوران هفته پنجم لیگ برتر؛ موعود بنیادی فرد رسما داور شهرآورد 107 پایتخت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28814" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28813">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbqMsJ3sBTZXxrjRVT-Gbz5W0A495XSzg32b_nmBljebJqeD0eOJwSxIZ3Wd8NflwaD53XguPivF0f78YJ3zLdCEu1bOUrOlHcji3w07idIy1M7_-Jdb_TvCzjgWwfQBRfMPraL-qUmzgQTMxff9IHYr4vZcfDbC82w6anU9Jbjt46K-alFggRG30mhcjkb4MYOgCg7zv1uZEaVKkCJjgRUzkgiZ3-at49CO0x9iHu0bIig8ANrJbHD3Ae8sm7wVDulHQzkdFe3atiwjVp_B9HK5c6W-UBnog6Ty8jWK1d2kn75x67YivUpFziBx1odrseF41L7bFrRz89Uu_Qo2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
جای‌داوروسط و داوراتاق VAR شهرآورد پایتخت عوض شد؛ موعود بنیای‌فر بعنوان داور وسط دیدار روز چهار شنبه استقلال
🆚
پرسپولیس انتخاب شده و سازمان لیگ فردا این خبر رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28813" target="_blank">📅 20:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28812">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y09X-8j5Q2ruieEbc-UpvNFnf9KpIXFyNMmpxlhnbMipXGorRiQbDrtNzhTtzcWUJSL7RvI9-9FXLosh0BMMRP61wVtNb2kNC6q8GCe7k8b3M8CtR9wLErI9hSgeIBIwKEIbTy-e5HytFCj3AYT6T0iZCepVzMDqczu2h1ATBSu4syg4uvSaUKt3EwBW4Z1AX_W_XZyscmq_YFr3dcCzU2LnpUfe_ZCf_tbKld-B43mIAVir8lw2hacI_oBR5YMidzULv3PeI1jO9xFzicWRtN8yOK3UiPLoZVmPB55D6j05J73oVtW2ps8cqPpN79VCvOWCzZ-ZM-9CdDVTXHDWZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیوآدان دروازه‌بان‌فصل‌قبل استقلال رسما اعلام کرد که بخاطرشرایط‌جنگی به ایران باز نخواهد گشت و مطالبات فصل گذشته اش رو نیز بخشیده و هیچ شکایتی از آبی پوشان به فیفا نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28812" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28811">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWnkiKU8SmQlsK5QKTXukYyWcgbvrE8rAIbOwsO0OLVSVze7E9VN_keY04vf9jBc19FgL-EudSxscpJ8ug_Or8HuTzeQDZ5PyMivaXrTPyP_PKnUggTnWclKYSm0r6WKbyXp_cWYKm4r9-ZbmvBSG0wECkGED8koUPQp_USJ6iVdp_qMV7r8xuVO2KN0O5-GJoWq2e_A__Th-UeD0Wgg_m4AHyeQWUZ6eFY4sWEYTYc-WZfVnRqhGVS-njB7arBwxDYehvfKEpXOdOllmIBX10vu89A6o8-Kkk9JB2WJKf2rPRWsh_RoTLAm0P2TNGMkHxD0-lIATVuKcsUhyMHrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: اتفاقات‌مثبتی برای اهدای جام قهرمانی فصل گذشته لیگ برتر به باشگاه استقلال رخ داده و به زودی اخبار رسمی دراین باره منتشر خواهدشد. در تلاش هستیم که‌زودتر آنتونیو آدان و نازون رو به تیم اضافه کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28811" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28810">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5zsciRJU9x45u_Diw7c9FOtWAmfwSmE_icYicNXjtVVHk1pQ97RJhpHFsQYs7zMs0YCCrlA1uMlozJXgztW9S-6nPASiNDxEm8qDMSO15Kq6gnHs94efMYbac_G0H__8FxTmgdBw-XZqURMFr9tYRNAumrDCa5jfinAyFNhvxYee0yVWfsR9dMYlNhlRxZ2mMvOwCA4CvDrs6HQgR4jf3wcRuHWUyzFlslAvln3o4hwyrsuQZBToOmWUcHTCmfMPEfEsnGPokGu7z2Y41Neu74eCbOwbhNIEUUM6LLBZ8utd1eXwBsp6h9AdO6yHgX625COVk3KLwc_2bXXFRnL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی چهارساله به منچسترسیتی پیوست. فابریزیو رومانو بزودی هیر وی گو رو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28810" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28808">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJeLl1388cQL-U1XjpHEbtF7-8KZai1x4tHxyd47U7oUJEQW_AJdur27BumjIPn9uIKGRcnChJfVfK0XVZEdTa5ihT_GaCS_KG2bi16TKmoY-IXmNQMa7LOSXr9PfiFRVAbqEUcnkjSiwb4KERXeLCl79_zR_IMAjBvfu8q-iNOy4RlYIKfzHAU-ojrjepn4s6S-m7d88ILXi2Ymp664aY5J6pyKiDUc8RRnK13NbJ5QdXKpYMBL0ghBH4GWTkLZumsIfxTF4JX39X4aPOpR17ctt5rB_HKzDChbZ-0cg4RhznXVi5MmWGx7aeiiJI5nnFYDwBn2MQe9wxYv1u2pVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28808" target="_blank">📅 19:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28807">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=XYNh3fUpA76kZuPXzEh6O_hZsBWjMwJGXvbeDWN7Zm6CGxcrADmAFdqLEtsXSADR-4iJaFWjVx8Ily7uPZkzFtjQ2s0JprcfAMOHqysQmRM75OHhcPMr0IoPlg-tSQb9wP5KZEcB_CmcyKLNbE3fLLpWIl5djWUix9GutXWt_0-QI9VXeF9kacPHFmDskh4hf-f_tleTn_Dxq_HGfVgDxUOgh_M6Ntqs-K1IIQAsPSWLmq-97xHPBY9Pw2UmNUodtf56BG85h8tv3lTgxMVWwWhy3Q5_Ahoobkl521NqCIPMRRa9m7tcAbofNa6fHK9ptfjFc9ipd9O_IJKdlCYGiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=XYNh3fUpA76kZuPXzEh6O_hZsBWjMwJGXvbeDWN7Zm6CGxcrADmAFdqLEtsXSADR-4iJaFWjVx8Ily7uPZkzFtjQ2s0JprcfAMOHqysQmRM75OHhcPMr0IoPlg-tSQb9wP5KZEcB_CmcyKLNbE3fLLpWIl5djWUix9GutXWt_0-QI9VXeF9kacPHFmDskh4hf-f_tleTn_Dxq_HGfVgDxUOgh_M6Ntqs-K1IIQAsPSWLmq-97xHPBY9Pw2UmNUodtf56BG85h8tv3lTgxMVWwWhy3Q5_Ahoobkl521NqCIPMRRa9m7tcAbofNa6fHK9ptfjFc9ipd9O_IJKdlCYGiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28807" target="_blank">📅 19:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28805">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtwZRUAMRNGKMyrXRli0hYOfzkIKz5z0SPtquEBMasGA52FofPfocRnRavaE_oqPq13MKEr_eSMAVd9McwgCKqkExey3Wzn7vXjiJXBnA6q-S2q0N_XYcRY-G0biztAI8wOxUd3CjCzFczUKQsahM1WSQjjD4iBP-Oi_sNDPjKDO2x0dDg_INhfCPiDwm0wuSz1b4XdbIht0UgsvS0ZOKWME31D5TpBxb1dq2xbcB4X8VRumYZiC1mNC8JakyR5GBdENR2nElnnyFpixFJJgFDqLto1ER-4crmLJp3Pg3JVVy3-FMZtRXafqD6ny3jOQD4HFSq4cvnpYurIjmsd_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9kcqIOdvUGKV_hT8ZKOYdJub77sksHBEW2pJS-OEeS9t3CaTHD2y4HjL-U20IlHTeir3rmJOB18pawmok9G_ICUKB_RXAfAPBCfNEQhrwbk4TCk-Y2jfG7rtN7PfZN1QIjHmN-hzbaVfgYFN_v-KISzdo5dmhoyD7I8ZUrXC-Wue9wh0wyfnGDhyH6irrVrpMFaPRkBPcy2TtqCW9qwqANlBvzWDbr26v-6I234wW0nmSRww7I4CLQckl1Ec8EobdbBuCtklgVSL3y-XIM2OxASNYlkRw1hgHMpgQKGfteW4sd2vQzkDS3CbBpg3y-C7PDFZgYauJ8raSpsaRJe5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28805" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28804">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHUGmbGhVKJ2p6UyNXCIaV1iUrh9zGBZaXLxZSakSw5iJ-ssu7KXvut7HEFVknLFJx8cPvJjg1YVk_bfvo2gZl6OJKYMFwgGcfguCypFlsg3xfRXbDeYE6n6lcc5hRcO8_J24WMOxqDNkA3kYa8yz2p1luZghXAOY_KTxT2h1Bhctugqn9XwQaZoJ-KwxcpPIw_7cCizXxzRcwoKkdHYCqZcgd6YbdoR22dcw2S0sSLQqpCJpuyd9g87T9MoudJpldhfYEc_8KNzzjl7IHBXeftvGlk01Tv34NBpUncyga6UbdG6JPHP9NRmlzjQyCtKE4KBj5Hr7vsmQ9Z3aJPXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28804" target="_blank">📅 18:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28803">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKYwHJOsyvsxWBdO53hix1wAYCGW_8Rf9VI2oYVlU1Rk7P3wdWDqjUeR6rKg9rg0B58DRuvA0J9hpSx7W1bnHQBsARmD13IAVIiyDayDbiOFuweygIn2ImRAZgjy705s1EXmGE-BXwEOW3GHlps5MfD6AzcUmg_TasgJ-TubIo24SS1pCTvIxkBvUQpY_KhGUXGDqrc2bZ1zju6YXl9CRtCu0S5oGdoXXUpF6hJl9dTIFL6hGP-RhmVQXWnacejoS4dESajWaW4CO-YOdfCddx8Jw7BSZTq8gEcKk4afesmQmXh7uvPWmu5untOHUXZt6EJNKSKactuvz4Q88CrPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
عملکرد فوق العاده لیونل مسی 39 ساله با پیراهن اینترمیامی: 98 گل‌زده درتنها 111 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28803" target="_blank">📅 17:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28802">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9x7KntodcPz0MieASeySZcV8OhLepB13jT4Yy3Wpeku5QkYghXDEZ-5h2WPFjgPf9LzI_M8s-shvPBesY17RIFcGmZRSHD9Xb_qMSdALb69d5Gwj-FTPxgjUOq52n55KASAKCsVHsEbrrx_Lkn6VLj4Z6OcyHKQQBoQzNxSvSWCeV8l43BgeCnNke8ku9poTeYaQEFRcyMBNldp-sVo7_bpnbHGARn5VVvSnl2QBytoGbCy2BTHi0zWJJcmGKh75jmjQ6E-MiR_33tAMsKzgDROK8Ziuncmzhcx58gSuhd7XunrYzwDhhDyteYGwjdMFjucWX20sZcJ4jGaFBK-FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تکمیلی؛ سانتی‌آئونا: کریم بنزما ستاره 38 ساله فرانسوی‌قراردادش رو باباشگاه الهلال عربستان فسخ کرد و رسما از جمع آبی‌های عربستان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28802" target="_blank">📅 17:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28801">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orrggc_jlYn6EDABHryA4ax0mmo1M4pdtxnDpEAv4ZR2G-3AwhQlE13Zm_tW1JM7MeqNT_ZDkCfXSOaKkOiK-JwR2yrqzTJ4iActrOr_QISAnsdwKFJEPQKKcTtbkOKMwNbgJwz3IuidbP9wKu7pSk-kaJDWK9Kx7WoVt-ndf5fyn8fm52A6mGyalvBBJEqQMCytPzcy0Ehnr21UvLyF4mYL93YaUwUlMOjT06oqIfA8nDRKqLliAIDeB4fAe1Hr-CrqEPW3k5uadB5uZn0e155cOolnir-gkCACOGeoc85n7fvGVgPjsuG36OM-aBNR4DjmfU2GWPMl1UR6C6K1zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28801" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28800">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPYeyM4TVQ-pLoyysByZfSs1coD556IhealAoq5rZzqM-bU8D3vHFRb2RVtr2LZKGPKt97qPkQHcQkVX_Iw6AH8skX1RbZ2oMAh7_J-W3VK-bTHEFXMW3ZDNGyl6ronuI0KCAacSOOyeqq-rubuL-78iKA1XphfXl2oe2EvlEN49C8n2D2peopUeK6Dx96wS44wH-0GPHOFlI5qD-YO6mR2om5UEgiKQ2DxCpMg9wdnw2zfWzi6HRTiaJGRSnM_KDcJx6ITdjnIv6eumIo2F6tFyoYg8xhstLCiRlXaiR0OHVMQ91TSjXYJFo569MNOzF5LSvdjfRFE5o1XCBeCniQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی رسمی باشگاه لیورپول از بردلی بارکولا ستاره فرانسوی جدید لک لک‌ها. لیورپول برای این انتقال 106+ 17 میلیون پوند هزینه کرده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28800" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28799">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=nx7jn2XEm4WdJnrP5Dv9APVqCbVjEfe12Gy18tU0uvZWXvgj4eTN3rpq4Jy4AhHs3igM1LQRmhKnb_5EbqG7hS1uWGG5nyETrjJKy7azt5bINXIfQsXE1iC8nhobfaj7uqnRb9M9ZEzNbG-uNdPqGr9lCEve6gSBqmUrp9jX_735jZO4GY60nH3eelN9VXB0LJYpazPIQlBuuEW6uO7t5385FZqVe0A9mJzYwSE4oWhscm8_WgFsG9Lcfeb5SF_L-Dx2JUMLNUJyXyesnYt4YpIv3AC_vT1eG8Cth0kynUyJk6D5bSOqV8C6A10cz1It_KKbDujajt7m2oLEd0Z8SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=nx7jn2XEm4WdJnrP5Dv9APVqCbVjEfe12Gy18tU0uvZWXvgj4eTN3rpq4Jy4AhHs3igM1LQRmhKnb_5EbqG7hS1uWGG5nyETrjJKy7azt5bINXIfQsXE1iC8nhobfaj7uqnRb9M9ZEzNbG-uNdPqGr9lCEve6gSBqmUrp9jX_735jZO4GY60nH3eelN9VXB0LJYpazPIQlBuuEW6uO7t5385FZqVe0A9mJzYwSE4oWhscm8_WgFsG9Lcfeb5SF_L-Dx2JUMLNUJyXyesnYt4YpIv3AC_vT1eG8Cth0kynUyJk6D5bSOqV8C6A10cz1It_KKbDujajt7m2oLEd0Z8SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌جالب‌از استادیومی‌که.دولت تاجیکستان در عرض دو سال ساخته. اینجا هم ماشالله با وجود حدود سه سال هنوز ورزشگاه ازادی بازسازی نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28799" target="_blank">📅 16:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28798">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVWUJiKAfzmhDkorjxJTkGw4r4Ls118UW7lrgzjn3FzxX-5RgREolZvDBJHVKqfUUoWR7dhCHGpFvqHRXTgLucMTKLIqhad9qDQgXanoz2-GYD0v5RwUtGFe5OQ7YBZpQRIP46K4LNdU4fqcyJJwDA-g26AYuGwZXSH9GnS-1ykR1MsXdtAFIBRwblQey2aQwHB_AQNKN5j07jj1K0rfkuEyoPQDk0Zd4ufoWcqtGhRXDwSkBpyu9Az_CwWbbJHgl9Dv_KmcatI2nvOgaKwk1FZZakwN8CCqk5VqxMCnfl9uy-Mx0mUtShCQrXJpT4mIMTVW5NBTomRVJMN40fvrfhhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVWUJiKAfzmhDkorjxJTkGw4r4Ls118UW7lrgzjn3FzxX-5RgREolZvDBJHVKqfUUoWR7dhCHGpFvqHRXTgLucMTKLIqhad9qDQgXanoz2-GYD0v5RwUtGFe5OQ7YBZpQRIP46K4LNdU4fqcyJJwDA-g26AYuGwZXSH9GnS-1ykR1MsXdtAFIBRwblQey2aQwHB_AQNKN5j07jj1K0rfkuEyoPQDk0Zd4ufoWcqtGhRXDwSkBpyu9Az_CwWbbJHgl9Dv_KmcatI2nvOgaKwk1FZZakwN8CCqk5VqxMCnfl9uy-Mx0mUtShCQrXJpT4mIMTVW5NBTomRVJMN40fvrfhhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه پاریسن ژرمن در این پنجره با فروش پنج‌ستاره‌خود 335 میلیون یورو درامد کسب کرده‌. البته انتقال بردلی بارکولا هنوز رسمی نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28798" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28797">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lULRN2BeXMbWgJpLC4qzrbkpBOPAtY8pZs53qEuQSIKlSxj2i-OKQCBrv6QjWBuwXb75GOlqjh1likFJu75IdZn77x9K4CC091VxxXSP0nmwO52DTZxU7tCQM1Vo80n5qUenVl_sgpTHv5BSpAmFsvSjN-XUYe-PdLqkB92AXZjLO_s4fJWrv4Ff6-It432_CyYPnYPnqfPBfvdaRbF6mgwXQzbZIzWuBly1rJ3dL0miGr8F-aTtDSJFDXVkgDCGYOWgZiQDOvSa4HA6eDC079YLLyUx4mrOZIPmRCSZCY4Zr3jzD8L0D_o3mh9ROfwcdHfpGHs-5tdQIwEmbThK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28797" target="_blank">📅 15:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28796">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLd4GcUKbSkYKDbatojBOWXe6MDIthvZv5W05QoCDK0sKbGHkkt4GBFou4g-A_DSrtCKbNm3YlkyddW1hK2srt6xF9Js-38cfyf3lCqTcBNRg4cMkfAyn06ZWHc0dqc5ZxqlW5duf79vSnrC-M-CVCaK7jnC1Yd3QlgorbHhBVlfnZ2FF0W6gGyj8IdjGIx9VYKk4D5ujHZOEZfV-3CVeYrMxNPnHycvtS0-wVXMkkQZSD_30Z9EDseVnUFYbgYRqRSQuxLpRZoTnjAu2KwYkDnjQEASk73SRB9UDzoBf6a6K18DtZnO0fVo3F-mxvUQMio5OtCJwTWBpDhs3XaEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28796" target="_blank">📅 14:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28795">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVShqwLn0wzhiYE7P8rlqGj-Eb9V7JuACNbnUSBWnh0oNBVayDvAYawhr4c_u_zWYRz9gkcflWeezita87VkXLwrU2OCMsKQeK7X1n10gFeSTyvTlVpy6MPK7T09MxRzZZXVJCAeRcFo5w4BNqAm8fNFM9e-JXIRIFKTyWn_2VWfR2hOYi29rlDdemt6hUVJkfv6Y7-e6g4hMNqCmKUQNAjBnRYhXBSWjZf-f_ArZafoyc4g0gouxE58PMEIl-tIAuYIdU949I7gTywBahqJ1rL2cdoHjq0IytUW6is0hmqcYbKuVTbcEUTOVp7-gXThIWbmuavfusMYrKjj_tfw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28795" target="_blank">📅 14:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28794">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔵
🔴
درفاصله 48 ساعت تاشهراورد 107 پایتخت؛ ویدیویی ببینیم از زیباترین گل‌های تاریخ این مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28794" target="_blank">📅 14:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28793">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFuiTTFpBZ5_xs8-O1oizf7SxndIsDF2zlqJitbd6Babtq_T6UEH2GuCs6ymvogNY9uUwB1-rVyBGayYYXF49T4K-5yFr0ZRre9-0tBPnkwgx9OSIVPE3D-Xe3VuO6jt64QaQ6OfZhqQfvpjDOvjqSqZuS0eay_ZiLMlZvtUzeRXsx76p7LlL1Df5Uz678e4ri2lCoD8tIvU2kLMirkes5AjGexH_bJkblUPsCuQ7ebcHWCiHisCQAXuW5srastT34IGRY6dBXyEsM2_HP_qbj099nHyZ54z8x2Dsx2K-w0VawhTFbGqO8P-yENNHeVKfJGEaHvwG7eJVoiSSvhqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های کرواسی: آفر باشگاه رییکا به محمد محبی دو ساله به ارزش 1.6 میلیون دلار بوده. یعنی سالی 800 هزار دلار بود. پیشنهاد استقلال به محبی برای پیوستن‌درنیم‌فصل سالانه 1.2 میلیون‌دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28793" target="_blank">📅 13:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28792">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhaHMvd_TJ-raO_mB4L31_Tdkr0x_BhbPeQQk42PUHhPdCzssGK2NjVJZe5vsVptDEGGJiDiRRmbJbzyvJuk14RQq2GdUypgzp08EwG_JurbtxwF97Z7LYdldymaBONoom-cLFugu2ubaxsFVMPxlkDMa8jhdFlYgPMCLK1ArnBjDvkmEIdVEODNNqR3sIdXRgWSeOxTffRcG5ib_4UkXZ__rRGYv5ucOd5LDljXmHFVCZPucSGrMV7Fydvce63CC_rnvhp_GHJ4ZnZAgMVZ78x8LyEmSPirHYFpWtbV8WNgOqqqtTrNCAw83ibUwZlwb0GsWSP7pQwzyi8aVMY5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28792" target="_blank">📅 13:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28791">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627b425286.mp4?token=fwEs8YfxuJLF75UBx-jGUp9oIYFEQYNQYBZzlesqXUhsLGI1lrxQOa77QoKAf069fzGGpNZD2zyEQDpBbQ9hqmNx_RglAer3yj2l3fy7iReUNLDhbGqoHzDKuCI8XiVnEnItbxgA5WYXMaZ2yjV807TWGu5IWUOuXqMuQeiKxGV6UJV9NN-CjHGQSOt0khPAaXp_UL77Av4dBioW3puV8XEAxWdJaw02n-5KC_fiP59gOlZCs4yhxA_ca28HLB22u_vGvSKe49qZltNJiy65KwiS_uzziHL3WTJq--6MCgH4JSSfwn58hr_2BnsV-jMzOIEpCdXxh_PrHujujXQv4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627b425286.mp4?token=fwEs8YfxuJLF75UBx-jGUp9oIYFEQYNQYBZzlesqXUhsLGI1lrxQOa77QoKAf069fzGGpNZD2zyEQDpBbQ9hqmNx_RglAer3yj2l3fy7iReUNLDhbGqoHzDKuCI8XiVnEnItbxgA5WYXMaZ2yjV807TWGu5IWUOuXqMuQeiKxGV6UJV9NN-CjHGQSOt0khPAaXp_UL77Av4dBioW3puV8XEAxWdJaw02n-5KC_fiP59gOlZCs4yhxA_ca28HLB22u_vGvSKe49qZltNJiy65KwiS_uzziHL3WTJq--6MCgH4JSSfwn58hr_2BnsV-jMzOIEpCdXxh_PrHujujXQv4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
بااعلام فلورین‌پلتنبرگ: میکل بازا پسر خاله شانزده ساله یوناتان تاه مدافع آلمانی بایرن مونیخ با عقد قراردادی تا سال 2029 به بارسلونا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28791" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28790">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K28DnE4JxzU5TxNPklU7iL9XMqtps7q7UTOFbDNFOBxGhitHB5sS6uHhfP69Q0Hv6P4oTHqg70L-xcP9LC37H8ox03Lou70TeleVbUyTF-KlkMlB4vFrBWVDYPkfMqYMAocmv35CfExhdOltzN4OnsF0Qy_lSXashVEg3lNEb4UfIwStLFqrKEVO3iCI4r-lcvXO6s1RlVC9VG17vzcr-mKgPCovJVBqD12tTu9K5xv1tLw-yTY5In14HgyAcwBubtGYfWwXyT2jdBlxxh5V9v8tP7dA9KSG8qUtPAnJ3lTllS1sndzIQNvMGEwDPZfsZh4-J9c6IXTdVuyfNyZa_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت فوتبال تیکت اعلام کرد که بلیت فروشی دربی از این‌سایت انجام نمیشود: بلیت فروشی رو از طریق باشگاه استقلال و سازمان لیگ پیگیری کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28790" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28789">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0juTgObuzsTHES_4OT8fNB9bQcmGCSP2s60DgvtmLdxZpXDwYuUnlz8xuYtydTID2qnDaN--MbwnRX8I13PMndrMlrRuvB_Hfb7hf7QY3dTih712DNP-vOrtO8RHUG4Jg-tQu9Mpr0bx_gAJ6fgBuEG7nlqIBYDFzpmUifhiygYmpY1Brvsun4VptT_l8cqHefSmp0QfKEfqkYyn2OabVc7mK4h6-oIFyMheHxxoXwAekUi3I22KkcShQSwb_Ey5XYocTzLegm92HurF7zz663xDeWid_ddFaZt2-k9rapq34_VHX_oQNJnb0K0FDwVXUNGiZZK64c74HKWrpZ-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفت خرید بارسلونا دراین پنجره که بابت جذب شون مبالغی بعنوان رضایت نامه پرداخت کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28789" target="_blank">📅 12:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrKCYNsv4qWZ-lkhMMU7GE37_hMoj3u8vxHs5mwcqcmw9D0EamAT2XpsrUxIViZ2EixE3UqZ0ycGiM3C8GBwFbdQxtMQU3Z3FfxKS7ftWefBZJ0JYbCUHc3ZPrDnOqeTOb3v3C7_zNL1_IaLGzXouHa2V_2KezFkdIMwGvbP1gZQJTG_HNlTU6jV15NOrYX8SCGSejXPBnlct33AUd1J9CPQrgpgOSIv8ZE1n3hOSvy54xxQDvkdCF9psGnVT8syW4OKHVcG2ysNQA_LeK0eqEcN0YxccWKTz0S2gSb4fHAEphQcIfOIokDLzbKyKyqXHnq2LwoXcG2jlyVsd7lHXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28788" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs-zQF6IcOesK4obD_wnU5B5wxT7kgtXBxqAGZZS5uMUG-wxeyQgY7okmv1wNd7O3XNopcQ1T_iFHEb_REvlV-X5kkp1qLDAm-7sq4mD_ya36GuT1q2xNV5xBAlbtpkxXjgUBbjOTcGFpUklfGCuyHZsE6yoQCE1Sgj_J3l4z_5_A4lWvhqwHY91n39ngs6QR34xdo70-4ENE6-6UfCvjire1d0t14dNYmzTEjNvXgCGMQX3WGyrnh9voduHnP5jI9lvBnb07VjIaXEWs3vc-mSJurpYOUpN2944ZUCTsMU2vefwwkFKMk_Tbdxeh7HXGi6ZL3lz2jqPRtDPsS7uMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
🔵
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ درصورتیکه‌هلدینگ‌خلیج‌فارس‌تاپایان این هفته 400 هزاردلارپیش‌پرداختی به عزیز گانیف ستاره تیم ملی ازبکستان پرداخت کنه این بازیکن قید حضور در تیم تراکتور تبریز رو خواهد زد و آبی پوش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28787" target="_blank">📅 11:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdgWtxHl43Ymk1UnTVc0OkY4KEJoW1IqltA9GXCaifqDjS9Y_FZpTe6EZ7ZUR-pzYbm4DSfOnPS7jl1ThYJKQswOSdsQbmDPkdVl_iG3syD6S_3vFbq7sqW2XVTEqWvRRytIo98DpvWBKgu_9VmarQjS79qUliZyqH0ul9G826nvAkwO6I7DZTu4O4OZGXi8XXjeI-tnRDjElp4KoArWUR7PntYSOvtKLuR5KXjAdKYGXIv0h4GnXtQnd57TzpOEtXp1n6X2HlzJgq8_iNI4y5d7QRceUHORNgRHU5lCMlBgS9-q13xGepZwr0HA9vNlQkW87IpXVvwVysPlnq3N6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28786" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28785">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-AwSHjb2iA2Jj7-PPAUU-l4no9LbKKK-lrWo1XTDbJ-DrppLGQ6JtkZD5BOhF8VcrMMqZE93Twx_yQLCLBt3V19Ll7s3AtB195ctG7t1J27vgnnc2-0bmfa5bpSZ1zglc1YWh9FPdCeTYLPSVyJR15q_0B5YjFSH2Q562unY1ASh7cevaWpRrRLXAdXH20YUkIeCCKRXZKDcgCKTSMMyl9xhAfT9oqyOJA7GmOkJvXFusT0WrwesZwG9oJIUq1sumQpcBxl-45tNLJlGz9IlyRwdjoapj6b0Rl_STsamtwEYDmLfAez8qQfaJ0P22TRrkNKx3wWgTi2QnjOUZL8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28785" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
