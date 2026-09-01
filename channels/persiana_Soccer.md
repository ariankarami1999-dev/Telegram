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
<p>@persiana_Soccer • 👥 607K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 03:11:27</div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/persiana_Soccer/28894" target="_blank">📅 03:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28892">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1tUWmZN6WOQSPzHvHo93WmWZ7rXdAxpkyxESwa8fc5pgrukGhRyM1USBrRLkPNdOlsXVuXzdgqRnmkbtL3thO3ZN10OSgr9z_6Z45G7sJLgV5Trf6mH82vwrsaOlo3E0nYOXp1ciHIqjxHEmCoy029p710vMLDEHb1dXFcSB_E8TZAEQXaHCSwsCy_yUrFeKn3EJs0OOZmws-xJP5dQX1EqxgOlhTsxnK2rmhlba_BWy2xf4Vuxc5RVh71PpS9EVw8CIOvmc5pM_qpGE6NrtbR8I2s-nc-f1eWUMAxnxz9ujXr5-QiC8BpmIFH0m63Yuau-bHScD6dO9oPhu_2_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/persiana_Soccer/28892" target="_blank">📅 02:48 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/28891" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28890">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXJtfX4NGMm2Lb6BpkScU_SK6mkBuq7iSrUDuJj_RMgsoJwGfRq_vaz6GZlo489EbgxoauO8knzGtviXnqDG0Umof1dRukYBX8dBVBb09MNwl1wZ5A69AKMatAvfE2BHVfK9uS2qbpq7wrGfpDEPmyVpHwQeoiU42v2IimSRd5QMyBK-FClTiwEGw4hQn23bArr-Kjz6rCgBB-BwzDW3PFwgMnnBmIabGl_zCz2WsZy813l7ZY_yLj-ocCo5nZK45fz2Czr6mbIqMga45K19F0IhjLOGZnSMExfCbRzXPvBlJdhUX-UGRgE1eXwB5A7tgWWoi8CIZkyH0nJSMOrUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ دربی شماره 107 با جدال حساس استقلال و پرسپولیس در شهر اصفهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/28890" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28889">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT0hBqdIPZu31sSYqmGHWBDPXWIVa3pgWZrxyMcWeECCL3RZr2Kzze4m2eAOGZI7bpgrjfhNVLGiW9XjaTyIP2fmmnMkpvMPfqJ9SKqVCaFQR27OcFLtR6G3ongT6VNm1fZLx8OkZs8uNcp6XZvrbpPeb7Y4tJXlVOMYUE5CD-cy15oeMeRcAR-Oi862CeN4W-EW2VrLznC5tBRSTt5-zOKzohF0DvmJw4aDdjlqxJeag-oDBBKRCCwetbZIbEIWrBweIccuKWBe5NzSPcDt-37W_XTPQMpU096nVZagzjUbaZ0oIr3ijA3uu3gR0eCihHaspIzlIO3uIpNUoWFcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
ادامه روند بسته‌ ماندن دروازه تراکتور در این فصل و برد قاطع الهلالی‌ها در شب گلزنی تازه‌واردها؛ واتکینز نیومده گلزنی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/28889" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28888">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4s9xt-Rf_SPR7UxgwclfmCnRmpRbQPc41vlkBrRkmB25mV9fZfVAsrh8N28UJPpQySV7qW_URoY-BBUsWgHJzfo0-rzZQgs610ncD3Ouz42WkgqAO-SIKgcTRmRyxnuzatQ1zS-4aqIvybb-cDxdUPczTTx6NsyKFQBmcrY540jFecHOy8Xgk7cY2cng9Z9z3LyIGjURaEKpD1F4CW6pSit09DSJWq-6PxwyTF-9fxw-0Kc8NCj6jszVb1RCPN8GNkufmGuXV446ZkxiOp_T0JKwK783eJGo5DK7Z4UlxznsZpORekUmPDgMvMEFYhm5hCDFS2iGMbB73s097aoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
بعداز دست‌دادن‌فصل توسط ترابی؛ شهریار مغانلو و امیرحسین حسین‌زاده دو ستاره پرشورها در حاشیه دیدار امروز با شمس آذر نیز مصدوم شدند و میزان دقیق دوری آن‌ها از میادین مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/28888" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28887">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNgqjHlehuxTGtBn2OomIrwHaTpl5SX0bUxMGj5KIROSI0zILYrC49oZ8cI_WXrAvI5w_N9gIor9bY4W_nX6VTOj_NhbfmCuZ0lBijuY6tInqB3IVgCYXkA4Ap6yX_bZkeMbqQOW2n6Qm15en0PEyG-YERu96Llxrc2QW71H3Lfjp-QSeNQWLTJKwtRVvk-CO8I7ZZESW2ppZQTHTyWngK1q-hL4EZXXbyQWTrpUNGB0vRvf6LJr5fk5IEld7mStnIq8g6zKFTsNbHO1zzAOavnK50rnND5mEJFe8aXJAmUCxz4aEX6YVCEieZ2NAhHA_LMF0_WUe6flInw_QdvtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/28887" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28886">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTVbQD0PL6GlaeJI6QqMVx4VuwjLGjIYi_HVzW2t19bPstb496shik-xWWF8W15PrvilpTbJZjPlsAsqeq-9Felrawy6lvWC_uTS1ejJncAdsuESEUaNBf4n1SOakw-EDFwbDc3--l9xHlvWqyWyi7PZQT9eMG_76C9g-jh7VSfXaSudTgXfvmQZoY3aNuFZNQeB__G1ceHhYo_WY9Cs5_VASNRN_nZ5flIvrYlf7kOXVX8PECrMQ6D0-dQStqSZM6T1heiePyZ-pa4z5EA_zsmTx6WzxSER1-cb1zBtj07kBm_zMA_t7bsI_FTA7UE8yNsg2q2dnfH4wQ3kJb2j5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
لامین کامارا هافبک دفاعی 22 ساله موناکو با عقدقراردادی‌بلندمدت به‌چلسی پیوست. آبی‌های لندن برای این انتقال 65 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/28886" target="_blank">📅 23:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28885">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGvJ7vhjw_cq2MMmtUxFL4K0D6ToamX1y_6l4p5fXa7TOqcO_pNDWzfXoMtu6hiHnjR7RDhObVZepw3ZwhMn-MdIQXUGUPGPbRo0daR3V-mV_QU7F_PbHjEpRp2YgmqC3D2F6BKSohN0mQCjBXKkMeI182-uMy9T2LiuOoCBrQrYaBK8hxLjrEuONKPs7tpZff1MRxYrW3lL2qJb0VIDLaTECGZE0ZTsEs6MyyY2K-BnjbcTPfChH16CAAAChTk0QwoGgOr_9SRi6nAo_pyDiFVXAYWAL4bZHArkWPai8LRvLcY-HeTrgOIcsKwnNArOR-uGgqR1SgmcuDriQZ1dZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره "9" های بارسلونا از فصل 2004 تا کنون؛ گابریل ژسوس صاحب جدید شماره 9 آبی اناری‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/28885" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28884">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVxYxsm6_geS4DLu1zXQZM36ZRGOSXmL84D2GnTqwPtZifsAZlgcWYRNkDoEy1syB8ztTx2ShIb99fgqWXuvN35vlsh6uB9kC0WQYS4sD5UcQsBfjJGlPBEgcJ__pCE1Fxheq-0hk7JwjAksYGERUlqVHn7ForzbUMT928_Q9m0hUnuim_R8WFSiQFmD2bsYwNfqEtn3MSGHWEawmbSso6SFiCJ1qT4YCoMZVe3d6XcT-HOIaAv9QatRf1qX46EtDHCaOgroXkEF3wghziV_UoDZVlQQleol-ozx92IGaimDjsHXpe5ABG4M6-EhvaUCbMxPst7gyNc_ZR848MuhgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/28884" target="_blank">📅 23:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28883">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrsLqwBxF7SanJ74t71By61vO-ztdouVTWyKgDD7cxt3XZ1OHlSOmgx2Y2pLfWTOXY4XBKZuyRMx71ER6eRmT2qNbpfBTjYh6Dv5NnUcRQxp-rBPBsfy7kJGi3eoVKoT6Zl3ylCwkZhFdznuVnFRX_QLBKcrIdRMVwtDJyEeV0snacJNdNd2pW9lXdNPpxLccuMCzr6muhtw4ifr4C8JNkFybt8BylFaV4XzRFIj0G0XaKBDa-OgiAjwHFxNRBjvFjbEVM7uk3CTpLfcxPvzN_Oela9je5mpfl0P0AhQKjzb7NWpzyIQNL2fMHDg22SgToFsJiSOPXDnbl13F9zKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/28883" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/28882" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28881" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/28880" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28879">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWAwp4VD7vHtFBiRcRz4ma2DAvTaRNU5li7MvXS_KQfFGiHnD_ZrWEPGA5AeYEq9NOSmN1sphmBz4YxZ2yT-muoZBuKmKG-bynzjzSCVtYU8xGBJl91Uuav4zA321v10bgncTozRzjHZ7CCNGpZ3X0FmRMCt0msovtOg_-MpuDDLz3SDe-SCzmF3-oB9dVcSfGubkV4pdbCs80yAZCPv1aK5jTzoRoLVbTou41J0axPq9940jNCGMx8zPclyijg2ZU56Av6_w8stJAUkmj9tjLEo9WlDfxi6eLoCYV5jgihgKpLMKZ9ny45ORt0nVi8bS-MPFtZ44Q_QWMpNJTsYkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
به‌ درخواست ژوزه‌ مورینیو؛ باشگاه رئال مادرید قرارداد دنی‌سبایوس رو رسما فسخ‌ کرد و این بازیکن بعد از چند فصل حضور در این تیم جدا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28879" target="_blank">📅 21:25 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/28878" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/28877" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/28876" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28875">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTmIZd4g-V4JrhhyF5kFKxV8sWEVe6xsmn4CkADL2BEog-bL2kGMV_jNz2JtpI85grJzf5FhhKJXkl6BbEUJ_HFeztBTDu4cYaOwGFNFKnbAFf6ZXXlYf5aZIXaFVBHzHAyhqgwkg7tDrdxtglUexKL5OaE5r7Yyr9zkx7Zy2u257cHhbUf-BBrGJKAUCAb7oOkcxAn2eEPI_rCMvHnosw7WemhazibVeFzkFG-aYqcl5xuPbaAMJvztrBhD0p9oPSfffSn2qPcdV1hdONNthAxw37n51D2AHU94BsNzG0ile_MHi4or7o4APxTEyS3hkZeXAdqd91l8_g9K0hUbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/28875" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28874">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2sEgu3eGWPCUVaxPiWtJ3LRNZi43y3_e9ibbJ-JxdyvQLwYsOfVZopo_h0H3RGU-FV2CDiKJ0QRAa6UMmkTzWYwjh-kGm21ANAjewYnEwSokOjd84D0uLuXNJWj1R6qo-5rvjEpkYKSVEf1mUeXboxA07vZEinVFBM-G3WYWnv256OtVblLBMFyVA7PT6BNGialaOGfVe28-1FjOaZ5EDdIaXybnWIomYXu0zphJ6a3BUGq1v3MdDuvPmmCZfA7evdhUckc2wYMYV4-qnIV7idCP2oXp5L7zCJksEtHHeohWlkq9Ubonc_BpG7AEVBhvqML5EKi1_doolVSvop5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگا رسمی باشگاه چلسی که گفته مطمئن هستم با ژابی آلونسو قهرمان لیگ برتر میشیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/28874" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28873">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNn_YzRhpHVFvQWDojWAsXA8BGJB3Nnxof8Ew_rz9UMpuXbZZkebd4-vp7v4nO9fUN-NPJ9JGk3iwk1VDgOyeE0OealxUQLLope-5p6yd0EpwUWYHUjrIBPionr-DPfSUUSaszj_oqfLOUs-U_3R5-XVcck6CrqC-oVs5L5FNDrmm861Pbi45jIim9-Wu1xKijekLhzx1oP3tQLmv3lppcBXFXIq5xzGkEwJqwdQEbGINQd44gRR2pvQ9Nk1dfFPsVaqrb-HPkQTG9hp54ANYXHeUKcRJBlZAA2mjFTdAB0wbOmVji6GlYvQAPcSoaYQqygc9CORKeNpMIPesNPpyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28873" target="_blank">📅 19:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28872">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZnN7NH5nVtnrOjkQ48jSn-KSHytogwHIl_vPNwGJeFS9WIK1O9-GhCcBtf--2bD7_d1WSgBhZ4xraTkz0792nnMCWRIytW2Oe84xHbdWDcbTRYMX1SaSk5mhCUfRPPEngMR_K6R3_-1lpfTj4strS3nN6jxmxmadPDesG2NXoOYN-VGViuU7XNCvzIzw4VM1FNf_5Z8kLBNYy63x_383UZOqlAj--Ds9ybtrVVYuUvfH4NcY_cyemT9utXAXGeDPn0ba7fJYahA52QU42y9SRvowE0tG0C31Hnlsea7_6EnMB8CjVTnel7JLWr3tFt8Cx-WKPFlYOaQSmZp0QfzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ تا ساعات آینده انزو فرناندز ستاره آرژانتینی تیم‌چلسی با عقدقراردادی تا سال 2031 به منچسترسیتی خواهد پیوست. بند فسخ قرارداد انزو در منچستر سیتی 100 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28872" target="_blank">📅 19:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28870">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cy9-8enC0EdoK029ZLbQIxSKfW0fhRh7Fyo_T08wTNSflGANaV7vkQS3vF1B6WcYaiEpV_dwOAFEXVeuVSTR0YXIPhz_sj6dqiBIsl4Zkj-9kzWohcdlCQEYT0GW8zJ5prQvld3iLLu6IUMZqpWOXxV3iE9aSYFg63ZlzmH2dIOYMZr3WE5ecrxF-2ka9nO9NveYaJFjduUjAQTgUMu9Pe1gaT7v3EotatKqjVUxMcPlgnnwaDCDSrLELFtnTYBCEALqrw83MBEw3iy2-pi-bZLdlvmLZz0_3YRAO9JuVKyshue-0Ih0GPPYpz5hiNrypPspszzeut16C54rJVd6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXGWOsgTKJ0ZNHX8cmysHUsm73pG9p44wWq0t3xOBr0FzQEnv7peFv-PoLK_Py-p6J9GCiMHBrlDBgLHXptQ17Ff1lkT4N0d7BMwkb0PJcd6IcPxQLtbBsuwZQOzqTOiAnW1Yd4C4uvRFiYEYePwFjehe-nqDhfit60kZg7WegefekGDSuzHf0MhHgVJAWqStflQ4S0rjpoN8gjZIeVaXATdDa-Gok0JcemRKl902A3yD8Dh3zMW_HNavWu1rvJq5DMP3tUqtdXtFywJ2fczQEDSZ7RQ6BiPBrFdO9NxRoOm0oSRivDj0_CVGYjsnlvonHgKZc3suAGq1E7otCFHoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کاپل‌های‌ فوتبالی که رکورددار بیشترین تعداد دنبال‌کننده دراینستاگرام هستند؛ امباپه در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/28870" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28869">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS_HxyVz3fSHjgWT27Jfd7xUiSDtAgnWllxsGEUeOO8yJf_t8crAnpsi5s-HOJ7UgSCifDIWJi4i2JqkCLQf7OzzIBIrSosVQr7PAFcnAsQhFQ9oO4ec-1weOvQMt-1Msa_EgtNFxP8QNlxxLlmVUlqq110rFajyuVsiDfdYWXB1_0dAgDMkEkiIUrM2SHXd5w1ZQEaOr0WyHOC2NW6zC60njLEDlEuF3O5vfUYNHgpb2seyw7sZkmQv4_sI2DoCeOcSuyjvO0mIRlcyToU1DZyTkFGgHkjhQiqClzV4uDnW9nksIMN_-qnzxmkutJ-5oLJEQMtfsfhnYhPR96khtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28869" target="_blank">📅 18:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28868">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHrKXNBa9K5o1cmTSerigXQ0xOuXOW083SaBMjTN1r7ISGVvQgIx_hleJlDXfhhVeTLA4AZK6XFcZuDMdKrJZaqJDwXhKxNWoStMwGGs_M0wvGb9WEp8JjXJH7DfmuJlZ6X1fsERqO0reQhMKZX5zRjKOgmpz81vq0Z4lnljGFqafnzAk9vuQHnPkhruxr24t3Luz7DIbtXBllpWRE443nwZCdSSem1FxJnvoE7oS_a_p4TtG_mt2FuXHJSNZ-i-5xMbzzaRJyMsbfqpmYNKVFVKIF0kVWVGdVktXm8NZOZvUQCQF9rNdkBy1252-7iHolesD52Q4s6yEvnYKflCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تقویم
؛ سال 2017 در چنین روزی؛
کیلیان‌ امباپه باعقدقراردادی قرضی همراه بابند خرید دائمی به PSG پیوست و با به ثمر رساندن 256 گل زده با اختلاف‌بعنوان‌بهترین گلزن تاریخ PSG تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/28868" target="_blank">📅 18:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28867">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADQjkDZyI9840VMJDkGygExKR6orhsb-8g3pUj2IFZ4DObLuxnhgwF6bgXxzw0cZq8LU4ZuOcIPPahN5YuedoOe_rG7DcAaSfHBsFD9qjFAcYCp2SSACoraMMd9iNj9529Ir9phqHFQCahL9-r0ihU672gSxrv9vkkOjLLzGUdQfrPq9Nt6JP25KSkdSKiiQ0tPFskioLyVyuVr9oKmjTyxJsYS8HAfqoJggpyIn29CvSzD18m2A7YDRqkmRLnKdp3Our9xn3WvljbaO65nLboeDt_iW42mkzod_WQwBmTQInHvE8PGVKJ7TaVkCl-Dvw6cdFlB2Jiazh_q7SQt5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدار با شمس آذر؛ ساعت 19:15 از شبکه ورزش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/28867" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28866">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGKya4txi0ijFYfRoNwgWuaNzmvHdsSZyflt4K6a0WhzCiAPOYBfhu7hRAzw8uVRBd2tYwvXYg_mKBKVvbLpRbae3--ZFNDpASUo4lDou-exWRhdPbm0iGZ2SYWu3S3dbPYX1A4K5cJAd_fEnE8PSKnqrq_EfmF6OG3UXr-fwX5fxnwx8Ow5YgWSQc8zKYsaEHNN7_o0gYLBmyrgF6hiZqPiqLLfjnYhIdE4Lbyv8Nr8YqUZAGjaax48IuZwG-kXG8ZLwy_hYE8rrVMrDYbcXBG-5zjRv-x0XOxJ7Cx1fvoRZtJNBm3XNBKOYI5KiMTNuvixQKFmSFdhet-nlnl4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/28866" target="_blank">📅 18:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28865">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc-kxHlQe0gjdzT3OcT8sbdLgYMbZF2dC7vXk72RGefRYUsWkrCRkbFRUZk3V5JLdpQx7Pf_roCUK0d88PA0sIAhxPjxonRt3bV2i0HFEZl462nibNeoRU-FInAXCOgAQXGiY9D8FrZwUdxxeeub8r_mJCGpkRDW5CqQex-2pRLmIUfUe5jy0hx0p5H3-okcIZNArG4VoaMyW4V46CgWPqrGI8TnMQ_mghM0U-gxTwjyX9HsH7DerbXYcbzbSpCDRxTmiW7x3Jpe1zLGbK7vMXSKrgaUYMEXfkM3fesjxOHLm8gUrdtof38LNLc2J6c76-_LrC2MdmEA-1GkFvhX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و پرسپولیس به بی اهمیت ترین موضوع‌بین‌مردم‌تبدیل‌شده و این‌حجم از بی‌تفاوتی قابلیت ثبت در تاریخ برای نسل‌های بعدی رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/28865" target="_blank">📅 17:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28864">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ae770053.mp4?token=FXAukTO4h9PNj_ezbqlkHcPKx7QiS08E0jgfiMGK8dQfTmNjfKZTHL8gOx9zJ8gV0BV0vHDjwpUwxzY5GI7yR__RPV3JmOLZTX8y2Hq1hnHMpYvE7KMqA_O1Rx91THTrLTJZ7TE0-qF6yEEnu8Fx0wmpgzFIEvXEWSoACfIqABqLiL7tgtiudPwPYHCJfGQ5-vyURDhbY0vpKMC_z2sOHnaKX7T40G3WaZuujWfNqS93RUbfB4DOy2Y_axwWAFTuYyD8hAgpBipyaYbXJpqTPnxOmw6Cff69fKMR9l8vumnMrGwG_brZkk7tgTRse4tvRQTgRGZI2-2KDSQ3sB-KnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ae770053.mp4?token=FXAukTO4h9PNj_ezbqlkHcPKx7QiS08E0jgfiMGK8dQfTmNjfKZTHL8gOx9zJ8gV0BV0vHDjwpUwxzY5GI7yR__RPV3JmOLZTX8y2Hq1hnHMpYvE7KMqA_O1Rx91THTrLTJZ7TE0-qF6yEEnu8Fx0wmpgzFIEvXEWSoACfIqABqLiL7tgtiudPwPYHCJfGQ5-vyURDhbY0vpKMC_z2sOHnaKX7T40G3WaZuujWfNqS93RUbfB4DOy2Y_axwWAFTuYyD8hAgpBipyaYbXJpqTPnxOmw6Cff69fKMR9l8vumnMrGwG_brZkk7tgTRse4tvRQTgRGZI2-2KDSQ3sB-KnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28864" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28863">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-FjyjqpezrRt6gLKqwOW3JpZQI_Ghs5NJmdQWvvZoz3sv057tDNPTWnCWeXGnwQP59ESfMGmvS9upVg123ZN3z01ImDnWEAcu-8dk0eKRflG95TA6WbxYLYK1CPFkjB8R3kk-2Ld6Gg2N4oeudkydrlMJ76rxHbktYnjHEhT_x_WrDEjDA6GGjtt89sUXDcSaB5milQE49irialqECBYu8DV51TJLfLbNNHlpOoLc_DFqUJPBRt3asBYAdRoFKYxY5uGT1Q-lsiZgGHc_PUTgEB0nGJEikskEskErk5jRBr1I89lJqTnko_U2HLJSzSDjD-snvcwDKctpFbVdMRCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/28863" target="_blank">📅 17:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28861">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQHNgsC773DbtFBq0PGVb1dXtpwWLmYUCLFGzqIXzuL1j-_zq6YAwcHA3-S7pP0qooryPv7PjnHDJGMh40s1nCX6P9vZmAaMOb3cyBPr3Vkw-nV0AKapn08GoB6StccLLJA8uoUQFoyAYDMTmZDT7Flhw7tc3Ctplxy9ivfvN8KcDu2-4MPhb4Sy77N0iJqeCjL31aPSJI4FUQuIZZnookqgTShnQpfTz3TVHn3Ktm6rMh1Fyp1u2oJwHkyalMXKGVVbBJsDGkzALM_u1g49ibNguorVbRRXDLU6ylUTm_Qz0M_yzc9ondTTECCMZ5OEFKj7dRW3O9-jVrRhyo00PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqxSGEj5JlXyiGsPUAO2o6WlZOkUYMiQM-EOB1pA0txEq9AXb0d4ZUQAA4FBTtmV9-GpU9oj4lZz4QVMppLADTlxM0lF6DeXN7kPQJNC9rh5Dd-tCQ5T0hXAyx-M6kjjZCEoYcErdYVePWIUVRFojHq3T5H_QqycxYdngnhmOqo46Rf7pMQ1ChCIvZQFMMsiSkPRluvNQuuUt-KBYwlMekbMS62DltqFwZKLbRIpBbNUG8EbPz3Hqra5YC3sbyDDw3pGYdgPCeVo0cK4tcEz0pLOj2XYW2INubn-VEpunRZHD0VOVCipbe6a0HS_17q8wbAxaLCjJ1Ks4gfYv6oemw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
خبرنگار رسمی باشگاه‌شباب‌الاهلی امارات هستند که از نگاه‌او سعید عزت‌اللهی بهترین بازیکن این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28861" target="_blank">📅 16:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28860">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvTZJPax4b4guk2uxQqD9035aEyiNOiydr6Dh1tfz0DkcXeoQ-mGwh3pXFu_Zvj-0_ZlBNv4SVrf8hfiXnRb1E44t3BmGUUkWILr_wDd5xmwZ7xVfDr2hd1Y0cdSt0No8kIXAsRxkqLqS_ajtoaQwA9Oi2t-TsJikhhbo8X4WPwQeNw9HEJ773XMY88Oq4OGC6A96d2KVvFEzxpNYp2WMHiXKPFcGs4HghKS9VySjO8OzHM5BV2r-tqyF_YV98NUre5xXCuSDLN0kATCDtM0Nvmrbo80kTVwHue_7i80u9N9tWmGpVCH6gC11E2c25cipbxj21jE_DPLalY75gShew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28860" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXBI1KipFtZDQbuXDSiaYZ17Z-exsHOz-XG32DUSoXFi2YhgWqQYLN_Fv3iXh3ytxGaMTMLvIBDRj9yaVSBMfHqlMSpreujhXmoD3NzprRLgjQ0scXV44zlG1evYGwE8gmgnODjOKyX82wE_rr8k9FCq9-qU7TqZKVn1ubekeL_p82TIwEKvIpNLHf_oAhydcCU4DIcY3j0H-mZ5ng0Z1qEqAPbHffko4NZwtTm_U3ymEEy7h8BjQyN1OyqiT6OfaetzV5C_teDSSx5ZHsZ43zq9uR3yomyaOxx3oNPwcNG1tWcuBVpgDK-KNZFQ-8MkDBhi5a01MOrGT08Hh6Hv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28859" target="_blank">📅 15:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28858">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W02yfgdcMFIkmTz5sk4Lo3J_y2yHs3GV-fcvFo87cE6RLxpYjcFKkj0eSYD6AQql-uLgLieY58y8LS5_b6V1zg9huFzGOdQwCfJq7h8mn6Qsj6NXvHbp_92qanDNJm0Uaf4-m7Y3FCixRhroBQaQvJeb9Ebc1_W1IyxqCNANd7O95tY64WgP54Llpl3QzYxLq8SvQyHjKS7sYfu2NRJa4mypILyw-7FVcpDCfZ8KuyDfZZRCxFzD7DH-6itQJvUfbY9PiVAAeXok_27EgBILg-AlBnftIJUezwUPceYA1GpEHRaXywWMwZ29YreMI-baAIXyU09iPTGcNy1Yv0zEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌رییکای‌کرواسی با انتشار این ویدیو خبر از عقد قرارداد با محمد محبی ستاره تیم ملی رو داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28858" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-nCDlQ2dalQeXaJ65we8GIjZDxVSFxy4j8kuHPk8ndX2aVFrUpvJcsJcpHQSwwhqcT5hV7K1-PIeXaZawPLBXjXG_8LE9iAXCp8omLcUzil9ingdHpuPwFMSEefyH1cZPFSUvYoe1oTrcKGzCf24biAswJ_ySTHwvl46pJnN0gn-MGwejv7QNUzrc2qHbVfR3Vvwu_iClBDQW040wOxixmmj8s0j2wkCKT1WpeVNSDOFrmf3LmPUTAt_MhZyuQANuSK3xiSNBnj3F7wzgSlsyXLVE9NlWLTYACyyc5uzZfXr15F8fC5pmI0ZXdTKNwtRZXni-SG_YO1zfTd5ctiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28857" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28856">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaBvsbX7tXflkel_rxujpbXukhy8nechIKHRWRofJnwK09ZazF3GPLo8fRmc32NQp2yh7Igp8GSP5hAzP0bvbxUZJEIXdftjI9rtinPftxASgzL69MfvUkbq08o2sai1tVB4rvTHMaPZLNr_PirEWH2zcd4b5eIhRf4p9U72usEQR51iiGwpOifr_ard1GVOx0LIupIHKHqcDU4qy6icFx2OhGamfNzLq7QAiL28vhz5ne2kjMCDlBy1MsoKl8akLG6liPF7UdDJ2jvJwf5BIvi_jXLLbosj3SAL--Zov6Eq8Lh9UcPDZ65Tuz_L5ZTnWkBCE0IhYOGBhwogr-D8nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/28856" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28855">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=Y9wthlNeuC1JP7DbJj3cqh70ct-VDl2za346TQrvEd9F61eZKPijtZlnzgQHSAz2gq9iQH52sHAN-kZk7DTSjq6bXe_Zf4yUEZSEIrp7Rp6Wpn2TZXg8ecI7ehbSM0NyCCyXYFPu8tlGp10bSgZjLm0q3bY0tP17rv-dI3W4OKZB4vEl7yFy3UICR0X1k-97n7RQvGh-3EAqzYDQtoJni3OD-084Ljr2rkGrxCNdCgLXwI_OvRcEcb6Six1iERWxm9IApy_wFDZxf_opVaOKRZ5q9DG89p7kNuTA2BtokHaPqzKatHz0w2ivaz_NIIZ-uuVv5spxYnlQ7t9VN3WhWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=Y9wthlNeuC1JP7DbJj3cqh70ct-VDl2za346TQrvEd9F61eZKPijtZlnzgQHSAz2gq9iQH52sHAN-kZk7DTSjq6bXe_Zf4yUEZSEIrp7Rp6Wpn2TZXg8ecI7ehbSM0NyCCyXYFPu8tlGp10bSgZjLm0q3bY0tP17rv-dI3W4OKZB4vEl7yFy3UICR0X1k-97n7RQvGh-3EAqzYDQtoJni3OD-084Ljr2rkGrxCNdCgLXwI_OvRcEcb6Six1iERWxm9IApy_wFDZxf_opVaOKRZ5q9DG89p7kNuTA2BtokHaPqzKatHz0w2ivaz_NIIZ-uuVv5spxYnlQ7t9VN3WhWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28855" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28854">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7ZaQely_A5VIuVorURWLgdzV3Eh1QGlpopXsCbh6TVRhZcIZEFJma04wdu7duYbpS-CCQcgf_teI5XPRR7lXXJifqjDPoGXQMC67Wl1tVELAjbdLTVV7IxGORV9im8LPvjDFn6HF6CcCRpnk6P4LBMHD0dIC-poMbGZ_WBhXFUjsJGudlxADKfuL2AQmPyMSwVW3RgSAxJ3jeV92uykgMEDA-A9BWzReodvMrWNEKURztWDQvLK61wTjtlc_T5je3o0y5fiCcOvlYvonY_C0plu7m-7wwssWMrpJgU3kGUEseIM86k5xDPco0b_1wfYhOnnkTJyJfmQ4bRsi3splw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28854" target="_blank">📅 14:18 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28853" target="_blank">📅 14:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28851">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6A8W42uTTooNiUEYU1FibXCqbAPQzjHGXgA7kFfiL2UfKS3JdSL4uj-iuF3XxlUF1E2jupvYE29BrYyNLuo9lgvgkFcPi90qJBgje_WoroIdmXEPGfGtK5jZgQpe4Bgo128mdS54jFl9NUzG67BgKx3Da98s8mDUJGwr42OotuQkXq6S3x8WjOe_MQ6lKnBXjPt5HZx9a95aDklsCTedrvxGRwj1Wal-OxKerqjjzFBcZUZ-fr2t9QuFB_-Kjfb1E9VfcqoweKNzNsilzzzXluKLVhVIfh60b-ACwNd-PhMuhI0PLAm8_STHNAYlbbChzKHg3jR5AbchxFZTiZOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISmwVAWb3_CcPpAtB3NW7BQzLuEPzz3dC8Omt_g199hdWoIuVeTBqtYE7S8KbDCBWj30OvsKLjGoYVV-iJ_bSiqD0azpp96EGw6ZRufjoaQX68J_0pKzJENnJ1D2U4uLpjLgJydB1M-2EWbId3GBh6OAQSYV6QnbO3aV-bX7qF7FH6on5KPlhLxlpqH-KCYdCRa1VDFkRB6w5PNGBE4Ywaq99PP9zHv2zwBvVXHF5kF9rudZ3SvPhWDj61-wtFQkV2qexOBmo1jKuOiNknGTKw4O0oeFe9g0dntYvLq4yNBcwafMjRW8sp0d3lB60jkdFPrcy91dUsJOE3GUw7j4MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28851" target="_blank">📅 13:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzMoV-nOIseJmRQaTg1I9i09O_7JvXXekbxnRwN994u6fpJoug5FJEzzBqk2jpzTV0D9bavjlflYgxkl6Kd111Kp4CGXNmHZykYNYTzwHq7n-gj6C3BooBRUFYFiFCC8Yl8rw3EUnhX8USLU2-Th2a_DIpcotDQ1Elxg64XeIwWaiQjUZtpXVdCx2QiF3cQM3jqZP2hoAGMTQfJyAq1pCHznCSnFGkMLBBb5mylwcd_fNyI0rrzvu9wFqW42PooKsCQZNtzz7LoBdzIVH2hyKSKXgrDlCisUHa6thIJTfHyoZAbnYL0qe6dhSWpY7Ekt8DMGd_1_0yEEfqQ7OTNxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jp2Wy2Bn_k6o3y1I2HiC4JsGPa4-b0hVHma62iiDi39lcHGFcitU3hvCI3qccrndThu4a0JavD7nN2y4fPAS_Ep3WeRRufia1bK3ZNOgENZQtqzg1NmfOAMYt1gJn2OEcddBuCgTBILodbIn_tbhI4q6TBeEuCjSY67jCFESp2N7Fe2FpC35zSEnzRWxBesFMbrl-FKNlyqD7in8VpRhN15IAbe03bcWn-SAkO7afH8Mg2yu43p6lVk-1yyWr0i7l37msXrb-xgKcQrCFmJpk7zCdieoXD-ynOrpz0sj0fsZsI8bGerh7rM8A-mF56GHAit3D91shSJaW1fHNfsCfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
پوستر فدراسیون فوتبال آفریقای جنوبی برای پیتسو موسیمانه سرمربی‌جدید تیم‌ملی این کشور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28849" target="_blank">📅 13:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bcl6m8NRr49-VCaJTgthM0C-lKddO6eb9-C8qegUZ9Zf5zJ65Y8jnxu1WEeMqy99sxMJbxqJkxx-hdDoRPhdT5oWo0Ync4Ql7T088ZZyX0tMBGGQ04za-bSKonp2Jdlgxs-vgnTC4Pxs-Wv9LGfT6QtHHZDXtaZuzc19RmOxkKxVDxgB9qnV7q1wisoyqLt5gz6Dhj9TtXCYPAAB4JpZHFxxalap1tmyapNfh3eVc0jyj8oAhv4JlsJzYGQqFwkT5ZZ-aFSQrwn1rTjOIArWDBTbaQaGr2tE94D9LbtI-bHgiVtB0si5i0z9-FyjMH2d92PGGyNOGX5xS4I3uP-fcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
فابریزیو رومانو: انتظار میره تا فرداشب که پنجره نقل‌وانتقالات‌تابستونی بسته میشه انتقال انزو فرناندز ستاره چلسی به منچستر سیتی نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28848" target="_blank">📅 13:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itvf-MnE1_OeBkUBrV6joIUVXN-4fjd8JY7G84tPrLUptCktHKy24UaSXa6OIFxIG5t33U602xIBZ_P3XHwQyvk0HORRKRtLDbCEthL-9dfC73foVaXbyVlDpk27-HMPRdQ_3gTOQVdNBjgboW7v5aWEYNu2B0XHGAtEz7mdNvYaN4Pi6_UotU4f0QaFHbKB-nacNPVv-NmRY0vZXIj6KQhyg-vCNjbssAlhdT6Pc8jsTEbmy3TCL9zcaVKSrWWS41LnljTxDl1IttqabLGte7OcfTtQbdJuqdBG5Q0sgkcktkBVX8HQh1f4X3fhvBRyzn-YolO8vQKNytMWTU4cQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مورد جذاب گابریل آرتتا پسر میکل آرتتا اینه که چشماش دو رنگیه؛یکی‌ تیره‌‌تر شبیه‌ پدر، یکی روشن و شیشه‌ای شبیه مادر که توجهات بسیار زیادی رو به خود جلب‌کرده. جالبه‌بدونید در دنیا تنها چهارصد نفر چشاشون‌دو رنگیه‌که پسر آرتتا یکی‌ازاین 400 نفره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28847" target="_blank">📅 12:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU8vBf73iOwRUt8jIvADZ4vOmqPPtu_l461vpN15zWFwtVUHdDmyS50yD14WPM9YdMzRPgfTI7jWBYMp-AgS3VkK-usXVgsrtNt0pdv9oGxAVcmml53tC9bazkstBn01pgLS3QQqK9ZgPVAvKdccjHMJhXtfBWNULulULt9wnJPz4m42eMFUG8kp-Rrvf9KEb--rR8PlPkdVyYCkEqyppYnDQAxnjQTE0SY0M96KgT06JXNG2kX60YveZCDp_oRMxwDHrq75T_31j-l4AUlsGYNcl1gniHjCGI2NKg-_HszjF2C6j-5FwvG7d5XbOICDVzpQRUfD9Q_1AkyFf_1slw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
نشریه‌مارکا:خوزه‌مورینیو ازوضعیت ادواردو کاماوینگا هافبک‌فرانسوی رئال‌مادرید راضی نیست و به فلورنتینو پرز گفته او رو بفروشد. پرز برای فروش‌ کاماوینگا رقمی‌بین 60 الی 80 میلیون‌یورو میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28846" target="_blank">📅 12:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">▶️
ویدیوکامل ویژه برنامه شب گذشته عادل درباره اتفاقات اخیر چهار هفته ابتدایی لیگ برترو افشاگری‌ های عادل علیه فدراسیون فوتبالِ مهدی تاج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28845" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGVP9Rf-M-qES3iwhIJyWzDwBnGjM5nPnHCn5LcC5ppBLDZK4HvSzE62Zfvs4Z_6hHFUKzH384HoZpA8WNIUpFfmukN7xf_mjv5E8Ze50zGcBRcWIbNO7upmdRYrPM2kWnrD7Z9rVAk8yCy_9CohmL6guatNqKtKBAXqXSpIQcVHnGoL5KzIjd25xqe1RFy8762n7q5mHGyCwPMeXMwG3_ZVhCxjP1TdnkdT2hqQQmUiA_dMGHWWpZ4L8etzBO_cvH1RtnD815DgSVDTmmIAa3PdQdgY2kPI1XpMjlMZjDYuc4y8byeD61daMpWmRlaUt2cIOdZ1ut0oZDjigmTJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
دستیارسابق‌انریکه سرمربی تیم کره جنوبی شد
؛ روبرتو مورنو سرمربی۴۹ساله‌اسپانیایی‌ودستیار سابق لوئیس انریکه، به عنوان سرمربی تیم ملی فوتبال کره جنوبی منصوب شد تاجایگزین هونگ میونگ بو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28844" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzLWVj5uP_1gHKFW38AiQYV8h181-0JfNOxFpM4aRXPA8_EPnGBTLpzkYGQVKBmkXZ2u-7lrvM6Hdky1aOdEhHUnGTcagTr2kse2jtWkqrp685yEeWd8zDKvZy1m8KgJ-tdZpDE07IY8tcDxn1vAdL0zJDNlwSa6WirpzVJb7axhELvordpmnkHSBVu-TOZYu4nbZagoozQ2Pxu9VlxJbWXkgOjAKRrUT81DT6huLzoiGAC9j-AAu9xZeOkOwBmgF5TpEUKgrPTxjrkwh40JFR9pKKEPx9EGxayzxg0GsR5jkily9vB9Tzhv0WDY_mPMsIl98J4obfrAFh357nOlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌کمیته‌انضباطی فدراسیون فوتبال: بعد از برسی‌های کامل مشخص‌شدکه قرارداد یاسر آسانی با استقلال قانونی‌است و او مشکلی‌برای‌همراهی آبی‌ها نخواهد داشت. بدین ترتیب پرونده شکایت باشگاه‌ها ازاین بازیکن بسته شد؛ خبر ریپلای شده هم بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28843" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=Ucb4I4WAmyvyT4YXsWd8m9t_Mre0f2DDutSDQu1aU4ljiNfHrT3Ub05Bwin6pwEJH_Rv4-uMmXu-pKE2HKLtkMVUPURiexUmmWvQd5xqUQmRdYIz0CEK8SbddW_WBiLuIGCRTzg_XzzklBnbarHYdvz3Su08avUHU7c97oR68vTvRF9l5n1gfpoaF-T5meJsfCZyN7MIedZ2pX9Hhyidxe4Dw8f6GkOnXTQQLbavMR-mhU_tp_HgLVMu5QfHoJvWzNF6R24XTlrTedR-IzujTYzeda3Iet7Q07Kvvst-fLKKjXbbPeeXsuxkRqofblBfjgOqSjiDPdA-ue9gyes76A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=Ucb4I4WAmyvyT4YXsWd8m9t_Mre0f2DDutSDQu1aU4ljiNfHrT3Ub05Bwin6pwEJH_Rv4-uMmXu-pKE2HKLtkMVUPURiexUmmWvQd5xqUQmRdYIz0CEK8SbddW_WBiLuIGCRTzg_XzzklBnbarHYdvz3Su08avUHU7c97oR68vTvRF9l5n1gfpoaF-T5meJsfCZyN7MIedZ2pX9Hhyidxe4Dw8f6GkOnXTQQLbavMR-mhU_tp_HgLVMu5QfHoJvWzNF6R24XTlrTedR-IzujTYzeda3Iet7Q07Kvvst-fLKKjXbbPeeXsuxkRqofblBfjgOqSjiDPdA-ue9gyes76A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های جالب کریس رونالدو فوق ستاره پرتغالی باشگاه النصر درباره سختی‌هایی که کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28842" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIHM_7YGfbG2aklxGVUdgaeU56Nc0KdhJnHcM2p0H4HUpCDJY_4tkl5c_2cHaUgUK20Gm43UwiA6woaP0RfBmgdV-58Bedvm3nhOvJXnFpwrFNRgGTfx9oFugk05DEimTiS16DV17pVDrGWYcCD1cfn7nmQXeAIMlXCLpL3GnQtjDUS0iieubY41FsD4BRLxi9_7O4mOVyQBbpK9ecaT7zZH6faPjI5wqgtbSjiD1cLxDrUOxstOAIRj_9E20J8mQr_HI6k7See1pK5Q7sL9a3h2BLEn7GEEF_vbJpXiAIL4RHu3Aza_pMvMduZ8DzyeZxq7y_PMogTONOBtM9qDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28841" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28840">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDp8NK_1zOPsSCqv5IJyVk2BO2jhGYtbeCOnyJR-BFW3NdG7wrPKJxkniW28pi4cQ11f6jSadgzzAOIC-zdW9_gigfSJ-2mCSY5Ttlj8GbwXEJHKzr8_5EpEy6wkBVXsDf_Li_cSDjDS_pIWr3COZ1yeTsa9y1T6G2Af9R6csK5khu2gBtGKxyFH7OnUtZZHPesiE2vYfb7DLTkOdA5MjUdbn8uvCyh4_dW0sgYc62IT6KUnv-BtgFkqZk4Q4BcKDe6XtWmr2YiYP4MCACiiEnPekVFyhghkPuD2fvzPMVDEmOG3vZY4v_yRe2LYGsrK1n9NOgXNT-sBvFLgt_SztA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/28840" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28839">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHqXJ7UzYIz3tha8c51dGulwzFy1hhVkV_yQs7S90PIu7aN9AFYOF9uGk03m1BGFmpIldsqRfGTdEMRZmpv0sYHOIF8DxTZ2iQmPB31N9bpkFG-MpID3w3kiCUSsmUjaWC9McP7OIWVbj85uvBjc1PEpRH9S8YdJA2RYWEkax2_Yo_xG5fHdI3--230gdb02ZEcSpP1_JGB_NzlVLfWQe2FUi7nKc2cF80ojoqlqAMCudu4Og2OZKLhwT6c0iiTgEbabk9R7_Mm-2BKDmJFXHyhTmpkkrJ89-Ib49DX7P4oaosCV8vkHkHADUb3prSqpntRwi3A6TYYrL6Tb3EBehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تکلیف نهایی داکنز نازون دیگر بازیکن خارجی استقلال نیز ظرف72ساعت‌آینده مشخص خواهد شد. یا به جمع آبی‌ها برمیگرده یااونم‌توافقی فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28839" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28838">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_8YUDr4XTVEvBctcs7oLYTSvbfRij57K-_k-hbvV5PrH7oUaytKFjhymHzzF7j2rnJi8qD2PwCSoeb8AZQ7GAordm6ilOD9OzAIFSP2ms9TqqW3wi2IAbyKaaJ0tEKz1gXRVWjSMXdM5AYbTY4uZT7FlIoVjU0OHYvllXjduPKdOwqB5wi3v4beA2_diFg1jngAy7fgXJaNzaiQcCeAXuI7I9sjZphRSMQE-fgZ1Q1EctCdtxUYM1GXE2t19xZIHJTkofSxt_XBJAYIek6xRO7pEAi7xqqw9QmSRuQL8RL8_l_czAFfapsY9PcchtvqllLYh16GatlcZV02jSd9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو خرید برگ ریزون و فوق العاده الهلال ظرف 48 ساعت‌گذشته؛ گابریل مارتینلی و اولی واتکینز دو ستاره آرسنال و آستون ویلا به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28838" target="_blank">📅 10:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28837">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqKI185HWCxiunZP8y7Xf4SZEcZ_LeuKI-d3Aia5998KHccr4cP_fjg_21XAQ3us47FPq9EbLTtpxS0AvgX-pghwv6LB_xyuN5uXAfx8uRo0VpDZHEk2iAnsknsY0pMI48jT8UZnmIO7zIRnO2xoZ-3O5adVpQxeUYEcm3LVkyuoaAPyfDui1y7elUK4NkwPvXtgr03LQChXm_sw5xQ8Yy4O9rNQV22gyFV-TgLQdMqpwppwarifzBKIssaYwowGk1kmdSLE6E6TUyY-mipwjOV8ui2VsWt5azKYOSkEhPc6UPiWdMiYZ3Ocq2JCaGNBM--IO4HKLCtSjiJsPfTXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فاطیمه یوسفی فوق‌ستاره 21 ساله فوتبال بانوان ایران هستن که با عقد قراردادی به ملوان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28837" target="_blank">📅 10:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28836">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfF9r3f2cEthEIq3ANI-LU2hJaSitZqo3Wm4K-j-bIx4bj79aXcF4mfSPeW2FC4Ml6weoe89FDeTQWHGfvHTvzjTTXYLPY9NO61bc_umXW1MBID4ARMx892iiSUpCPALNeLPYrlrJ1JjuJwxCIsQhE7Ts1IleGYDhCujZpVQx7hG8tZH30RVu6Hk7o7sNeiyUrLLfgJ1LUe3Kl4fOLps7VceVtXj_HZPjqd9jLvvgUUjrfYtm1fW_tcjEJsfyxMXVvWDcx-P4rLjn-3eQBUIWeSbwZs_ge2r8CHJoyyVkzKI7fC01GWh1lmpIhVY0dNEuBCGqac1ACQJHeTJsF5sGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌ساعت02:30 پنجره‌نقل‌وانتقالات تابستونی تموم لیگ‌های‌اروپایی بسته خواهد شد و از این به بعد باشگاه ها میتونن تنها بازیکنان آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28836" target="_blank">📅 10:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28835">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=eOqnCAXi0bjiETiMBqajVTPakrA-0i9VZPyLJNL8WY_RgaASx_zVlnlPnS7pILlNTu1MSCFnoa6A3w9zWtvQuVhfIckgiY-kbKXhVEpdS0MUmgclecTL8QTq9rEciu3XFexJpWvA8tRMWQIE6drCo8PBdSEfB-z1ixiDVINjXq_iRFQLBqmxH8Q5o90K9-KzMSecjK2Or7IeB4Nhc-UtoSmfsurEowCuOHlCqZ64PmdJC3hwBIP2jnC7clqVNhV5tuBg1-6MO7SCUzP-X1C2oOVGiw4BN5lnP1KLrC_KBPNXw0CV3QoVm7ke_MkC_VCUyNiw9xo6OFY1_sYUR9gb2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=eOqnCAXi0bjiETiMBqajVTPakrA-0i9VZPyLJNL8WY_RgaASx_zVlnlPnS7pILlNTu1MSCFnoa6A3w9zWtvQuVhfIckgiY-kbKXhVEpdS0MUmgclecTL8QTq9rEciu3XFexJpWvA8tRMWQIE6drCo8PBdSEfB-z1ixiDVINjXq_iRFQLBqmxH8Q5o90K9-KzMSecjK2Or7IeB4Nhc-UtoSmfsurEowCuOHlCqZ64PmdJC3hwBIP2jnC7clqVNhV5tuBg1-6MO7SCUzP-X1C2oOVGiw4BN5lnP1KLrC_KBPNXw0CV3QoVm7ke_MkC_VCUyNiw9xo6OFY1_sYUR9gb2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28835" target="_blank">📅 01:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28833">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIhbX6mL7Tao_lYy7xl2ifHQJMu2-idw2yQ4dhhNOtZN41ERZrSIjPfhPFI6pYI-N8pHOZ1I8CfYDpG2U54R1UUYXgdIyc-D5S6Ryc-f9gC68EKiEocJEQk9EIf50aXwSa6praUmoYYEeLKSwCTQBRgGorvoE34m-SqGZ850cIehH3xJIBIRiorVhqCXG9MJcOuY-IUyg8anU_QXfVWuum5-N4kULZvKMp2HjVfM8TKLv0Mb8duHSrjEoC5rldHrMeNzHJeDWE-VQ25ysfqnfE5QOj_hUbslOlXMAq4yZMo7qGcw5s1G6f6Q0_M86EBAYaXPAoenxopxRX284ITzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛شروع‌هفته‌پنجم‌لیگ برتر با جدال یاران نکونام باشمس‌آذر برای حفظ صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28833" target="_blank">📅 01:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28832">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvuETZKvf-H1J7IiD6845F7k8knwLHkpF1oX5Xw5TWiBXoovcQ9n4pFIMUqjhvYOoQNENiBon_Tsrq_oyVOxENFXsHRA6r2wr02VrvYqw2B6a1jrqb26zKrp8pStNO1OCFzr7XdvQ8qT2N_4nkpJ1TbNHX567WcCsgN8PpZlPm5CBjVien7QKD6qfLSL-PFkHe9idKmfQ2Ol1ZyFfcLdYX75c9rMbjBg7ACBkru4JOB5lo6cWKjgZgMKk8dpIbFAJKCy4M8SLtLRDpGgERfmXyTocFj2qguVDPu2Dlfxuyxlt2xHFxynLGypUpTBPGvGekxHmnYCHlP-Sg6FdjcoHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
برد اقتصادی آرسنال و جشنواره‌گل بلوگرانا بانمایش‌بی‌نظیر رافینیا و یامال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28832" target="_blank">📅 01:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28831">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=OdubQxqypOFxPOlm1hqUJqjs3WUdmZRqlVur3DYAvTqGsN2OPOznRkPs6hsJXfIYZzsx07MIXgXTTGtg5zlAuPMWELDz0V4aP5oOtGM7hdt1XGuCvDpejgwwEPAFOX4kYXEJUHPRTkounjeCwHYjO58hu31T2uHcBoNZ3a_vEFdaBmkbKf6l2vUhbls5Lllz3OCXzYXIJHY2esUM8cFugg2XONksB1Iur8yHBhUk49jy036gQpa1dqADDlcdi7idlgyJOy06QimhqubDwkPE2gSkHHtPuZ_6h3D-k6DBPLz4bxE4wWys4G3kN0tn2zW66D5a2gTsBPkBy8VXxxOaPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=OdubQxqypOFxPOlm1hqUJqjs3WUdmZRqlVur3DYAvTqGsN2OPOznRkPs6hsJXfIYZzsx07MIXgXTTGtg5zlAuPMWELDz0V4aP5oOtGM7hdt1XGuCvDpejgwwEPAFOX4kYXEJUHPRTkounjeCwHYjO58hu31T2uHcBoNZ3a_vEFdaBmkbKf6l2vUhbls5Lllz3OCXzYXIJHY2esUM8cFugg2XONksB1Iur8yHBhUk49jy036gQpa1dqADDlcdi7idlgyJOy06QimhqubDwkPE2gSkHHtPuZ_6h3D-k6DBPLz4bxE4wWys4G3kN0tn2zW66D5a2gTsBPkBy8VXxxOaPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28831" target="_blank">📅 01:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28830">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lacDLRwEJU1ruNhaRjwpxmKspjKv8isl9RKQHAQxfIuoOcyystnnFYajpjXvASh3jIdp8ASGdnJExTwRj3gL7znVIqfSHQudASXBTbNhoieFOw0nAafF1ZFPkW3zcdBbze0tUL-AIwL4YehqH38Lryb82C8d8W1quhTqVkW18usfU8YWDTOWWIf21eQLbRdvwEzAV9s_y5e9b9uMLorJmV7nKziR8guJ2SRAkoqLDO54uI9k5vRt0PAOmMef_Wy7CpATojwWD7rOD9-Kf8qsFewCKgOkaA6ru9QsY1bj4iCoCdIIapl44Q6EdqmZKo1PWwVa3HOpWtVWWJjjf6UehA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28830" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28829">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9mCSaOr7GYc_2WqWK8P8ZR1MRytPphDfGM-pa1YRZTOD_zV81ycLHSDdbVVwdlCRynEbUxnUSxUpRTxkbqb-dQfnimG0EFx9_uyrwHNpwBJAQDm1_9MrOu2NkmmXZWyaOoneI2-vCZHpzeXd9NQ8r2a4FUeiyIMi-RPsTDd3ylFEVlha149wybOE9wyQAcsVykGRj4m9bS1MdUF4McR9K8hTu_cMZfUJER0jFxMg3JUbQzFTdQ30x2lC9lF9pk6s01rRgLA6tw8-039XQbLweRIJWEMaOBwM36VedI5mH5eanMCImtFXrcuGCImYsP1MPKrTm0n1D1MhcIihvIkRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28829" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28828">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=RrtIyuU70MMaciHx36MkpNteDUCdJZTeMVtLaR7M28LLS-ETsd80qpuTXRI7tRsaY6qspcpGue5YqYrUaFD51r7A--JE3BrXTTnMqD2b03mzgeILpxbVRsIfoPHvBhE0qb4NOtfV8XdBa_j3GW8t78AjNIUj2iGaMf-DbuhUYjB7Fho0EVOJ7br3cdxXfkn8BRg-gRYKbzUCXo_dCJIuNbWmS-Y0DijEyNSIqnPYwk1baqh45F8Wv3Fmq5UpRQ0x7IkQlLMwiHmkl4M-MZHA5ZFvAGkhuvUxkSSMJDmr1cwEhu732CLRqjvAnsLoL3E1mrNDGILSXspYrjlT-toKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=RrtIyuU70MMaciHx36MkpNteDUCdJZTeMVtLaR7M28LLS-ETsd80qpuTXRI7tRsaY6qspcpGue5YqYrUaFD51r7A--JE3BrXTTnMqD2b03mzgeILpxbVRsIfoPHvBhE0qb4NOtfV8XdBa_j3GW8t78AjNIUj2iGaMf-DbuhUYjB7Fho0EVOJ7br3cdxXfkn8BRg-gRYKbzUCXo_dCJIuNbWmS-Y0DijEyNSIqnPYwk1baqh45F8Wv3Fmq5UpRQ0x7IkQlLMwiHmkl4M-MZHA5ZFvAGkhuvUxkSSMJDmr1cwEhu732CLRqjvAnsLoL3E1mrNDGILSXspYrjlT-toKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه سپاهان از باشگاه‌استقلال و هواداران این تیم‌بابت‌حرکت‌زشت و زننده عارف حاجی عیدی عذر خواهی کرد؛ این باشگاه همچنیین موافقت خود را با قهرمانی باشگاه استقلال در فصل گذشته رقابت های لیگ به فدراسیون فوتبال و سازمان لیگ اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28828" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28825">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS-G1abQtkemG_5Vows-_2j0gjOJfWejr1tW8TLvAE8yPoW4QRsKCb-Ywjz77TOpk2AjF1EfJQ31o7iXGbJim9Of1vJ1f7O9-Bw3BbKvGBrIpqNV4haUS5DAL0Z_XeRO7YggPCjjyux-VDKY4UwAJ4Wp0wia3G0fRaV0GJs4gwPP3eVmBR4Pd8XZPYM2VXoRrbXzpOCFFNERPlcTZulsledpaldgo18ivP7C5CbdXMkFSe5dW-kXjmP5fARtlyoQVdg32qtt67AFee1P0v-5HQdCKEgXkDLYrXIAwSIdwY0E1eXgJXdkA1FS0DZXs3NVPvFrPnGRtXge7JWHIlqYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت رسیدن شهرآورد پایتخت؛ مقایسه ارزشمند ترین بازیکن دو تیم استقلال
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28825" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28824">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=QVfF0fyMW6m8_6u_w58QBTxI2txo3vfpSCxYlMS8Zwbj-OR1tEVS9K0gcK6yv5sJ6cEM42SGWAOIzoCgPDMcBq8zd8IakxMQ5cimAfZo3Rh4cQkPa0HekDWK1dD5hNsmaxOmQ5QvUCqvKTH8-Ngg6EPQx8CYo-W-pCcwaOgsbQI0LdoicZaInCYP1_UMC1m3MwvRBh_Gh9_dYozjYfE8XJgche0na5H6ql5dngPL-WgiAXclh-wZFh5dAMhXpuciFebXyMmKNC5mmj-46ff-W75AYvUGVWjcBpZhyS1uKRLLQQBsmWgNovt3uwuqOZYUXrVK9l3rd2pLQyxn3DH0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=QVfF0fyMW6m8_6u_w58QBTxI2txo3vfpSCxYlMS8Zwbj-OR1tEVS9K0gcK6yv5sJ6cEM42SGWAOIzoCgPDMcBq8zd8IakxMQ5cimAfZo3Rh4cQkPa0HekDWK1dD5hNsmaxOmQ5QvUCqvKTH8-Ngg6EPQx8CYo-W-pCcwaOgsbQI0LdoicZaInCYP1_UMC1m3MwvRBh_Gh9_dYozjYfE8XJgche0na5H6ql5dngPL-WgiAXclh-wZFh5dAMhXpuciFebXyMmKNC5mmj-46ff-W75AYvUGVWjcBpZhyS1uKRLLQQBsmWgNovt3uwuqOZYUXrVK9l3rd2pLQyxn3DH0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28824" target="_blank">📅 00:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28823">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJKN5R5eH5SOjYLTQigt1slnQO0EuZR5DZE8IegJe9J5EAmsHEAUFaXYdfhzB3onmZeVmNqVcWDrdlL8tAeOb6z7ajr4kDMI168ZBkw1G1tVhrhaiPNdSrHIioHBgG8f6qq_sCIg54fvcIf0H0VAUFAEgOxFcfZ5PfbeButrX3Ms4LRGN9fD0FBbZG1HBpsrtOBd_hyaDnuWdf0fxSxkHj3bj3hf2YHH2G3GC9STUmoMb55uQvTardm9LEdYJ5bpjq21GFt0tzNY30KlOhEjSVHkIWU4InZG2w37PWogkIMbaDj9g_mXPf0poxDwRqOFYbO2EVrcl5JbltmniHgsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌رسیدن شهرآورد 107 نگاهی بیندازیم به افتخارات دو باشگاه استقلال
🆚
پرسپولیس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28823" target="_blank">📅 23:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28822">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_GXQXKljaLD2TlwQ9IcptpsAQ94vqy93P3S6Fzfh6hDS07FaRnt5CZqZgyWgIk81zx_ajVAs1NTgFMBVIbQAqmdGTyyTC_u1Z6VdoVEdQKlA2FqE_XHtalx9uS3mBnwTakf5VlxB3mUmkGWD9tcp3eyZItVQRe730w-YGRwMLmYWgYrZ23ZTm0tN1BLI79LLSxbwERHsq4e95kqNeQ2UBD-MG416Ffp9OGvHB7gyXpLRC9XIw95ICUIMK_UDxq_d-xHrLjtpStMBoCFmplLLxQbCOJnFxHcPSs5kejRVKGxjjx3gI_q3_hfwgQ7Rn08EsPRfkvAF7xA6-Dy9-M7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی؛ از کوچه‌های‌روزاریو تا قهرمان ملی آرژانتین در جام جهانی  دیگر لئو‌ را با لباس آلبی‌سلسته نخواهیم دید. "خداحافظی‌ام را در تاریخ ۲۱ ژوئیه ، ۲ روز پس از فینال جام جهانی نوشتم. امروز ، پس از فوت پدرم بیش از پیش به درستی این تصمیم اطمینان دارم"
⚪️
…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28822" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28821">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omOTWu7Np0O3wPjau0fHnr5_ul5kMA4x7oKYIbb4ZcoPt_jj5Nd14puwHmY84x7OaY0na1n5YWH4Qw1p1rHPGNtY5lFM8vaEWlyMP1TiqPeoOo69dpVgm37ORn-5iHq4XCxpHwMDGtYlFG42AG3wW85aITjdxyfiIK3h8tFFlJSWcCqynCV36P0_jupMZcwW4zHaoRHPXh625AYHqoGL6qKiR2R2x9MumTvALlgt1LyOJXKiol1IVg6fxuFQH7vyfcxs0gBpPztYmF2Q2FrnA7m-l-MmOOieQi9jnkCZWV8OnA8fNJZ76SLf32L8ESFc_Rxz8IG1npKdVhwJpFLmBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28821" target="_blank">📅 23:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28820">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=FMBpel6u6mrxbGRSCKtfeVL8_jlvRht2ckeZ6rYyFB3oh6lQlpum4RASXbeyq4-48WFhflAKjNuRwuF-3pmhvXxIa107s20c0DVC7O5k26vNitc853t9IjK-tV30jIAEsfVmILKOFhBEng3jUOZgfrtpPuqHDfiU7UlAFAyR5-WVJJU58LRfwWfO2tMpVEdbCNy2jpZdWoDTdUKE-DblaMLJCI02TkbhoriIKiiVlu0oXeggqVwTydbjb_CxTSxardThslBI30HNVUj20mEDmpxJk5aqWY6nmfNIMqwMnsDkbq9rVSdYebZbw_kXEhxqdtBjIjAgLtPc5z2mz6aqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=FMBpel6u6mrxbGRSCKtfeVL8_jlvRht2ckeZ6rYyFB3oh6lQlpum4RASXbeyq4-48WFhflAKjNuRwuF-3pmhvXxIa107s20c0DVC7O5k26vNitc853t9IjK-tV30jIAEsfVmILKOFhBEng3jUOZgfrtpPuqHDfiU7UlAFAyR5-WVJJU58LRfwWfO2tMpVEdbCNy2jpZdWoDTdUKE-DblaMLJCI02TkbhoriIKiiVlu0oXeggqVwTydbjb_CxTSxardThslBI30HNVUj20mEDmpxJk5aqWY6nmfNIMqwMnsDkbq9rVSdYebZbw_kXEhxqdtBjIjAgLtPc5z2mz6aqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28820" target="_blank">📅 22:45 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28819" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28818">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwaMjko3UUKA44BIAyuZSVFhArBX5cZfsdSjeMswGW6MvPfq-pXuWsWTKlZzBomDbtTeJnXjF-mfgCRASvKmDbzvjabyU_KxLHBQIIHcNZTV2eUISTo6yDmWs9QEe6zjg172i3uXKEauXEXLdI_xsvWzLJU27Dg1wxHJMQXig2x0ZH8H52HQvq8YsG2-RM0kNhXg4HH2QbDUCfE7qQTtdcwVWc0uQV6KIGuehE6BzesxVplz9zKWEtY1pa7RJZsZAznBpYIFonIFxs9y7DXt6tyBtKgqZPfvToh8EILzR-8l2jzaORemz2p5hxRlX_B_xCjU6Y3XJz120qUeNu9YtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ایلیمان اندیایه وینگر راست 26 ساله سنگالی اورتون باقراردادی 5 ساله به منچسترسیتی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28818" target="_blank">📅 21:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28817">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfdA7s0rMEe52OdUClV9_H2JOyzF5AY6hJr4FlS-rYpqwHYv0KRN9YyhIjaRIGAfjZkXhxSjxldbJpEEFwXmQj6DzyH1kvltFRdcL8l-hdF45S79EY75yy_v20uHi67_idIuUB3dSi46Y0LC1eAAtwt6gKtlihABRMZ7iSBqsx6xmxOtS_tYYNXjkESUr7l1rjWskvfGfpBLR-DkmWlTVNu3-AKy7YFSXx0k4GTYzNOCm1cRvD6guhIItbRmnmlNkxDQBgBDdMVxaKGOYKyfWCui9yJDL_oEWLKFfEAuVUyjCV9L11LA4EPmx3pkNZcj7rU1iarf5gquvbpVqoAioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28817" target="_blank">📅 21:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28816">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FriwYwxtGAEGz8gYkGgpw2gjWRnQp7xRB_K30seTC19ZhRaz3nV6IUW38ok_xcrtdtpDkA6prgbsLsI049qjgx1ivdhhRo4VNmuJqgQ02R7W-r7PEJ1T1Qot0s6wArEsp3oNIT8cQTL6LCZhFvY5Ei7QohkfARHCHFphyX99ZZ-o0A6q_CrVNZuOOI6sXlIRmIiTcS3sXu_xsIe2RWPKBiiZCqdd062FBHf5qyoT3mnkcuraXaXmI3CgPNWuGmsEPANhw-_ck2l9RJevzJw1UkFncWIrYE5Pm5KbsBvkDErUygnepqZGQEvudaZbC7meZ-bkzD00dy6i6HFQ_SyZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28816" target="_blank">📅 21:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28815">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28815" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28814">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxVLijH4xTvLwC5AzBsUYMCYdhAxWSdW5qzSbRZphjrkte0Dmt2_X5bKZmHmu8dLb5o4_x4sARfFH8IYSmhWDV1Dg5v3oXvbde-kBKLwjabdgfnl_9463Z0bi-nmJ0EuHvsCnQUt6OmaM1chTem0wdGG-BM8V3zJ-0LJlimP154IF18IwNQ5c9gVu9TyIlkzQa3mwR-sBhUGz1e1lOPoc1puopm2x4h6rq_oIas_Pjz6XpRulUHNrrpu6Vp9CpdKnHm3TxKOzjmowPobhhdMO8ygghY6NwRpfV5HGjxtW-bxGg8_N4BXgvkaB8hLlbuID9sWFGzkPglX4OeUqNPMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌اسامی داوران هفته پنجم لیگ برتر؛ موعود بنیادی فرد رسما داور شهرآورد 107 پایتخت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28814" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28813">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roNsu3drQ6y8_zKFDLVxli73fHvPkw9mh6jG9MoZP3HRhfwwET1jGR85RIo0dYZG49V3LAiC-qy6Orah2DCUrGWMXIsI4PmbR7uvMnYX7zFq302l5rGK82HXgaEy3zA4m2BgdyjxfCRhNyJ4bnffnRlllT5uknjz0T4b89LMqYbyIe7wpYeKJwLO8EPp4c7ElvCKKBNf4ofqFqBCD3PdHEFjxpAHcJ9mHl1dV_5RQ7GfGEO3pT_NOfuLOXa6QCuTWeyrRo61jPEUPcGDeA9Pi67ojUHtRDw4w35lwko9fSsD6yq1vrcW0O27meOpB8KoYmR7bRpxwLAP6S6evqvohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
جای‌داوروسط و داوراتاق VAR شهرآورد پایتخت عوض شد؛ موعود بنیای‌فر بعنوان داور وسط دیدار روز چهار شنبه استقلال
🆚
پرسپولیس انتخاب شده و سازمان لیگ فردا این خبر رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28813" target="_blank">📅 20:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28812">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xdeb_X7Dhu61vkA1IixY3yh_tezAT-pIl6RNbYoTJqjgflv1MMwbaOhNGSgp80-2TZjnTChCudT7zzAXlWhG_PTiDH-2_7vGRFmGxFQL8TAq4ErDOqo3GtltWp0Z5L64b2GJpYNlTxA_BI8NYwqJVWyCIRPrI0p1gl7l1khN3DcES-MFho57F_CJNdGFbz6y-NL-_Zlay2UAiS4tyvV3lxTCPYr6nKXKQa_J4VLOtMMGoI3b5zV2uc42_7Vn2GtrufbweT0LPpilgDRbr6teXzBQlyPk0kl4MbI6dcFU0SiNViERwoZDr-Kmhc-U2gxPAOdu5OrOm-dhAnUreHuZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیوآدان دروازه‌بان‌فصل‌قبل استقلال رسما اعلام کرد که بخاطرشرایط‌جنگی به ایران باز نخواهد گشت و مطالبات فصل گذشته اش رو نیز بخشیده و هیچ شکایتی از آبی پوشان به فیفا نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28812" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28811">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFYwvheOcCpJShUKsqsjmUev82R9V63O9Cbs0yL8XvB5F38Pf_mmNZFPYSWlXvJgS-dNpPSiVFtP__7q-GYzFXszDS7nTdcrh3BNK17X9Wcn8XqsX_C_5u7CwTsxJR9fYaiHt8rkn5lJDMV0ZEri0o8ct4qzHwLDJtZIiBHLJTwVfVVv8ZzSKZYRTMlRj-5rORYGzcQZEdRusKHzV8UksJ5Fpw89P_rToANalqe4eBzPUykEi81RgZ3wFQIoRhXfTAzu0PP4ZPMOBpPoWKs6lnXoVkHvNy8NIClsYnTgyeqfZafjgFnnUl5T5KnRWaqMsA7tobXhuC7MvA6T-dmq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: اتفاقات‌مثبتی برای اهدای جام قهرمانی فصل گذشته لیگ برتر به باشگاه استقلال رخ داده و به زودی اخبار رسمی دراین باره منتشر خواهدشد. در تلاش هستیم که‌زودتر آنتونیو آدان و نازون رو به تیم اضافه کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28811" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28810">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5zsciRJU9x45u_Diw7c9FOtWAmfwSmE_icYicNXjtVVHk1pQ97RJhpHFsQYs7zMs0YCCrlA1uMlozJXgztW9S-6nPASiNDxEm8qDMSO15Kq6gnHs94efMYbac_G0H__8FxTmgdBw-XZqURMFr9tYRNAumrDCa5jfinAyFNhvxYee0yVWfsR9dMYlNhlRxZ2mMvOwCA4CvDrs6HQgR4jf3wcRuHWUyzFlslAvln3o4hwyrsuQZBToOmWUcHTCmfMPEfEsnGPokGu7z2Y41Neu74eCbOwbhNIEUUM6LLBZ8utd1eXwBsp6h9AdO6yHgX625COVk3KLwc_2bXXFRnL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی چهارساله به منچسترسیتی پیوست. فابریزیو رومانو بزودی هیر وی گو رو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28810" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28808">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdlfqWdOosPgl1pTQLtCzAZwuVJj3aX4QNz2CvX4Nl4DT73kRgLXSgAKGBQudRuKrB_52Q9ghb-viNkpy-vuWpO_xZNuUcHN-NQb4uAp-LC-sykn-JGb61HGZgRtMZlwZdMFZcUMzWr_9NlSFaXFflX3vVsJqgCBDWz2PfqCkSq7hwrsYCWgbQp1nLbYXK2ZcILd_u1phafGCaIFcQNKN5TZmY1moKVzVJstJflUztWlqFPWsT0lQ6sDvDuc6ZsjDpbhChu7cJjdhuQ-UccF7jrcgs8ZQS58Kyw00VhjLGu9H6h1olUyVo9F9RBoAt9ipnB5a6Qkym8S-efFiyG_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28808" target="_blank">📅 19:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28807">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=soYlqxFLUcRE0ihPowBhu55VPYxnHX6hqANG-WtyBY9kzDv2zo_VSOzEThEtfe8pAH_bHgJ4b1Iux72Eo-m0Y0KmWspd_sUfNd9jVeEceZRJ8mMz3omm6tZK2h0gJGxWz09zfh0JEk1DfTa025rptsHmnTuaC8vUVWHj5Vq8EvSnVNHJ4mAUMl62XIqrsdYAsoHl5OxbvPPYLDA9deQClRym_JGWS7WzYtDMC7Z2d2-gqXPBPAEw_zYUUyNdQMfKAGMGlsXr3hf0Q_xBkRX-MOw83Y9nfYHiq5oj0RhD-DRPud9z8-XLXkzVRjzPcvcqGW-nQXwnL-0UQ7MrS6djMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=soYlqxFLUcRE0ihPowBhu55VPYxnHX6hqANG-WtyBY9kzDv2zo_VSOzEThEtfe8pAH_bHgJ4b1Iux72Eo-m0Y0KmWspd_sUfNd9jVeEceZRJ8mMz3omm6tZK2h0gJGxWz09zfh0JEk1DfTa025rptsHmnTuaC8vUVWHj5Vq8EvSnVNHJ4mAUMl62XIqrsdYAsoHl5OxbvPPYLDA9deQClRym_JGWS7WzYtDMC7Z2d2-gqXPBPAEw_zYUUyNdQMfKAGMGlsXr3hf0Q_xBkRX-MOw83Y9nfYHiq5oj0RhD-DRPud9z8-XLXkzVRjzPcvcqGW-nQXwnL-0UQ7MrS6djMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28807" target="_blank">📅 19:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28805">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtwZRUAMRNGKMyrXRli0hYOfzkIKz5z0SPtquEBMasGA52FofPfocRnRavaE_oqPq13MKEr_eSMAVd9McwgCKqkExey3Wzn7vXjiJXBnA6q-S2q0N_XYcRY-G0biztAI8wOxUd3CjCzFczUKQsahM1WSQjjD4iBP-Oi_sNDPjKDO2x0dDg_INhfCPiDwm0wuSz1b4XdbIht0UgsvS0ZOKWME31D5TpBxb1dq2xbcB4X8VRumYZiC1mNC8JakyR5GBdENR2nElnnyFpixFJJgFDqLto1ER-4crmLJp3Pg3JVVy3-FMZtRXafqD6ny3jOQD4HFSq4cvnpYurIjmsd_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Obg0nOJ_nXqmq0PIVdx-u9wD_N9uPad9qXtqi7L-XVrb9gAuxy7F_qiD2DHBXfzKG8cSa0YJNufFSJ_Sfv5togdNGd3w0WrBxXpF1dRxYQoHo_dNhXYTzWIlWfP0G0HYTb7UICb5KOCxPtlgxVtXfa1Rcb8CheGmKIoPFe-4c03d53EXOtpRFup9tuXziwISyL_ALO9M0NQpUW6jIWfua0w6oPLsw2vO_NiZWkA3wDNCDfgmJZgVig0jh_fJILHlEOzhgptKuQmWyLnZzS5QBNUIv5Px1eEFEMLe5Gyqo9UqJWMV1bHCYemYlTzipoZHo7vXqzkaDofBUqWN172ieQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28805" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28804">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHUGmbGhVKJ2p6UyNXCIaV1iUrh9zGBZaXLxZSakSw5iJ-ssu7KXvut7HEFVknLFJx8cPvJjg1YVk_bfvo2gZl6OJKYMFwgGcfguCypFlsg3xfRXbDeYE6n6lcc5hRcO8_J24WMOxqDNkA3kYa8yz2p1luZghXAOY_KTxT2h1Bhctugqn9XwQaZoJ-KwxcpPIw_7cCizXxzRcwoKkdHYCqZcgd6YbdoR22dcw2S0sSLQqpCJpuyd9g87T9MoudJpldhfYEc_8KNzzjl7IHBXeftvGlk01Tv34NBpUncyga6UbdG6JPHP9NRmlzjQyCtKE4KBj5Hr7vsmQ9Z3aJPXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28804" target="_blank">📅 18:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28803">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKYwHJOsyvsxWBdO53hix1wAYCGW_8Rf9VI2oYVlU1Rk7P3wdWDqjUeR6rKg9rg0B58DRuvA0J9hpSx7W1bnHQBsARmD13IAVIiyDayDbiOFuweygIn2ImRAZgjy705s1EXmGE-BXwEOW3GHlps5MfD6AzcUmg_TasgJ-TubIo24SS1pCTvIxkBvUQpY_KhGUXGDqrc2bZ1zju6YXl9CRtCu0S5oGdoXXUpF6hJl9dTIFL6hGP-RhmVQXWnacejoS4dESajWaW4CO-YOdfCddx8Jw7BSZTq8gEcKk4afesmQmXh7uvPWmu5untOHUXZt6EJNKSKactuvz4Q88CrPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
عملکرد فوق العاده لیونل مسی 39 ساله با پیراهن اینترمیامی: 98 گل‌زده درتنها 111 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28803" target="_blank">📅 17:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28802">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9x7KntodcPz0MieASeySZcV8OhLepB13jT4Yy3Wpeku5QkYghXDEZ-5h2WPFjgPf9LzI_M8s-shvPBesY17RIFcGmZRSHD9Xb_qMSdALb69d5Gwj-FTPxgjUOq52n55KASAKCsVHsEbrrx_Lkn6VLj4Z6OcyHKQQBoQzNxSvSWCeV8l43BgeCnNke8ku9poTeYaQEFRcyMBNldp-sVo7_bpnbHGARn5VVvSnl2QBytoGbCy2BTHi0zWJJcmGKh75jmjQ6E-MiR_33tAMsKzgDROK8Ziuncmzhcx58gSuhd7XunrYzwDhhDyteYGwjdMFjucWX20sZcJ4jGaFBK-FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تکمیلی؛ سانتی‌آئونا: کریم بنزما ستاره 38 ساله فرانسوی‌قراردادش رو باباشگاه الهلال عربستان فسخ کرد و رسما از جمع آبی‌های عربستان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28802" target="_blank">📅 17:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28801">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrS2SEZMAXypWHX9aEeOwHyG36EQ0A41OucprCdGYIhnLeTXA2fyvVdyGApNgleUORgAH5WNTdr37LHSeKGwtvd695vLk4XLe8x2ZjatM0OstnIR4mCtyk3Vt2up-2q42vwYH2umvWWZZKjpvHgB1KIVogoyJyuaIiswn4kJxvbxwPhrck32j4KPRZdzvuNmu-L01tGvj2CL-JEgv3J-w2AyIB6eEJY3nLr7n_YatSD5NgwxpwZ2CxWMVgejGh1TLjyza0A4U2zbi1e6zmpxMYoucf4RipKBfbUKxfmHUIFyXXk-0qbHIMmj6osk8Zq9ttVhqI_x6Q_orsEVr4ggdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28801" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28800">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPYeyM4TVQ-pLoyysByZfSs1coD556IhealAoq5rZzqM-bU8D3vHFRb2RVtr2LZKGPKt97qPkQHcQkVX_Iw6AH8skX1RbZ2oMAh7_J-W3VK-bTHEFXMW3ZDNGyl6ronuI0KCAacSOOyeqq-rubuL-78iKA1XphfXl2oe2EvlEN49C8n2D2peopUeK6Dx96wS44wH-0GPHOFlI5qD-YO6mR2om5UEgiKQ2DxCpMg9wdnw2zfWzi6HRTiaJGRSnM_KDcJx6ITdjnIv6eumIo2F6tFyoYg8xhstLCiRlXaiR0OHVMQ91TSjXYJFo569MNOzF5LSvdjfRFE5o1XCBeCniQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی رسمی باشگاه لیورپول از بردلی بارکولا ستاره فرانسوی جدید لک لک‌ها. لیورپول برای این انتقال 106+ 17 میلیون پوند هزینه کرده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28800" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28799" target="_blank">📅 16:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28798">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVZ1q8uaEasyMUhfPm70l_cgyK2MbsH-jJLvpPHyAOD7_vi37Q_l-FMk11qVTUyLGs3nR5KBC0vOqg1HtIr1j0Epfgp5TTPe8q5nond7GLJNNwCiZEQsI_3Q60LGrtq1p_QZH7RqaM4kRg7SqBpH2eXlxM2Ao5mnMc8_fEC35kRRX3QttQWq1WydUI_vO4s2vt7Gg-F9knvGFAHSmQ7twf6xr_IWiWXaA1QaHy8wpX_-PJWVhY1gDMBrx8PUxR3JI0dgAFaAPhbcgEENdNWZJxjDe7CtxpA3ir6itRLtTUeg7gW6LrW7vN38jeBAlIyCez4nbBf4mkQ61UxBwVTvm_9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVZ1q8uaEasyMUhfPm70l_cgyK2MbsH-jJLvpPHyAOD7_vi37Q_l-FMk11qVTUyLGs3nR5KBC0vOqg1HtIr1j0Epfgp5TTPe8q5nond7GLJNNwCiZEQsI_3Q60LGrtq1p_QZH7RqaM4kRg7SqBpH2eXlxM2Ao5mnMc8_fEC35kRRX3QttQWq1WydUI_vO4s2vt7Gg-F9knvGFAHSmQ7twf6xr_IWiWXaA1QaHy8wpX_-PJWVhY1gDMBrx8PUxR3JI0dgAFaAPhbcgEENdNWZJxjDe7CtxpA3ir6itRLtTUeg7gW6LrW7vN38jeBAlIyCez4nbBf4mkQ61UxBwVTvm_9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه پاریسن ژرمن در این پنجره با فروش پنج‌ستاره‌خود 335 میلیون یورو درامد کسب کرده‌. البته انتقال بردلی بارکولا هنوز رسمی نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28798" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28797">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lULRN2BeXMbWgJpLC4qzrbkpBOPAtY8pZs53qEuQSIKlSxj2i-OKQCBrv6QjWBuwXb75GOlqjh1likFJu75IdZn77x9K4CC091VxxXSP0nmwO52DTZxU7tCQM1Vo80n5qUenVl_sgpTHv5BSpAmFsvSjN-XUYe-PdLqkB92AXZjLO_s4fJWrv4Ff6-It432_CyYPnYPnqfPBfvdaRbF6mgwXQzbZIzWuBly1rJ3dL0miGr8F-aTtDSJFDXVkgDCGYOWgZiQDOvSa4HA6eDC079YLLyUx4mrOZIPmRCSZCY4Zr3jzD8L0D_o3mh9ROfwcdHfpGHs-5tdQIwEmbThK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28797" target="_blank">📅 15:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28796">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLd4GcUKbSkYKDbatojBOWXe6MDIthvZv5W05QoCDK0sKbGHkkt4GBFou4g-A_DSrtCKbNm3YlkyddW1hK2srt6xF9Js-38cfyf3lCqTcBNRg4cMkfAyn06ZWHc0dqc5ZxqlW5duf79vSnrC-M-CVCaK7jnC1Yd3QlgorbHhBVlfnZ2FF0W6gGyj8IdjGIx9VYKk4D5ujHZOEZfV-3CVeYrMxNPnHycvtS0-wVXMkkQZSD_30Z9EDseVnUFYbgYRqRSQuxLpRZoTnjAu2KwYkDnjQEASk73SRB9UDzoBf6a6K18DtZnO0fVo3F-mxvUQMio5OtCJwTWBpDhs3XaEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28796" target="_blank">📅 14:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28795">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOeBkZh6X4B5UFtR2_NIWe-cuIbnfmgoZFfxetRncvcN1N9GbneSHp5A1u3FFz7zc5_HXy6Op8apJSEBZRhcyCDZDUZxhPbLxIwG36sIkg-3_Pmqr1rm_YskX3FuTRsgkLF-46dGEVQTGBxe5a5CHcfiVNg79PCYCa6PNYRqHnXXXUgSXX4TvtW6ZWRFhUM-wLsY6gqTkiX6nkaRg9cqRTNtHkhcqxGamMW2SEfyeeTTw9IPQ6iV3nH9Uk6-jKCXcHBiIpgCZlMD8HbtzmUD-LZFuOhLQBaml_VhFmDyF1r-jJP3cX8SwJ2vGG1Hmizxi85i4QO23aSNfMqCR7AD8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28795" target="_blank">📅 14:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28794">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔵
🔴
درفاصله 48 ساعت تاشهراورد 107 پایتخت؛ ویدیویی ببینیم از زیباترین گل‌های تاریخ این مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28794" target="_blank">📅 14:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28793">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFuiTTFpBZ5_xs8-O1oizf7SxndIsDF2zlqJitbd6Babtq_T6UEH2GuCs6ymvogNY9uUwB1-rVyBGayYYXF49T4K-5yFr0ZRre9-0tBPnkwgx9OSIVPE3D-Xe3VuO6jt64QaQ6OfZhqQfvpjDOvjqSqZuS0eay_ZiLMlZvtUzeRXsx76p7LlL1Df5Uz678e4ri2lCoD8tIvU2kLMirkes5AjGexH_bJkblUPsCuQ7ebcHWCiHisCQAXuW5srastT34IGRY6dBXyEsM2_HP_qbj099nHyZ54z8x2Dsx2K-w0VawhTFbGqO8P-yENNHeVKfJGEaHvwG7eJVoiSSvhqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های کرواسی: آفر باشگاه رییکا به محمد محبی دو ساله به ارزش 1.6 میلیون دلار بوده. یعنی سالی 800 هزار دلار بود. پیشنهاد استقلال به محبی برای پیوستن‌درنیم‌فصل سالانه 1.2 میلیون‌دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28793" target="_blank">📅 13:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28792">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhaHMvd_TJ-raO_mB4L31_Tdkr0x_BhbPeQQk42PUHhPdCzssGK2NjVJZe5vsVptDEGGJiDiRRmbJbzyvJuk14RQq2GdUypgzp08EwG_JurbtxwF97Z7LYdldymaBONoom-cLFugu2ubaxsFVMPxlkDMa8jhdFlYgPMCLK1ArnBjDvkmEIdVEODNNqR3sIdXRgWSeOxTffRcG5ib_4UkXZ__rRGYv5ucOd5LDljXmHFVCZPucSGrMV7Fydvce63CC_rnvhp_GHJ4ZnZAgMVZ78x8LyEmSPirHYFpWtbV8WNgOqqqtTrNCAw83ibUwZlwb0GsWSP7pQwzyi8aVMY5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28792" target="_blank">📅 13:22 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28791" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28790">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K28DnE4JxzU5TxNPklU7iL9XMqtps7q7UTOFbDNFOBxGhitHB5sS6uHhfP69Q0Hv6P4oTHqg70L-xcP9LC37H8ox03Lou70TeleVbUyTF-KlkMlB4vFrBWVDYPkfMqYMAocmv35CfExhdOltzN4OnsF0Qy_lSXashVEg3lNEb4UfIwStLFqrKEVO3iCI4r-lcvXO6s1RlVC9VG17vzcr-mKgPCovJVBqD12tTu9K5xv1tLw-yTY5In14HgyAcwBubtGYfWwXyT2jdBlxxh5V9v8tP7dA9KSG8qUtPAnJ3lTllS1sndzIQNvMGEwDPZfsZh4-J9c6IXTdVuyfNyZa_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت فوتبال تیکت اعلام کرد که بلیت فروشی دربی از این‌سایت انجام نمیشود: بلیت فروشی رو از طریق باشگاه استقلال و سازمان لیگ پیگیری کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28790" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28789">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0juTgObuzsTHES_4OT8fNB9bQcmGCSP2s60DgvtmLdxZpXDwYuUnlz8xuYtydTID2qnDaN--MbwnRX8I13PMndrMlrRuvB_Hfb7hf7QY3dTih712DNP-vOrtO8RHUG4Jg-tQu9Mpr0bx_gAJ6fgBuEG7nlqIBYDFzpmUifhiygYmpY1Brvsun4VptT_l8cqHefSmp0QfKEfqkYyn2OabVc7mK4h6-oIFyMheHxxoXwAekUi3I22KkcShQSwb_Ey5XYocTzLegm92HurF7zz663xDeWid_ddFaZt2-k9rapq34_VHX_oQNJnb0K0FDwVXUNGiZZK64c74HKWrpZ-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفت خرید بارسلونا دراین پنجره که بابت جذب شون مبالغی بعنوان رضایت نامه پرداخت کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28789" target="_blank">📅 12:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrKCYNsv4qWZ-lkhMMU7GE37_hMoj3u8vxHs5mwcqcmw9D0EamAT2XpsrUxIViZ2EixE3UqZ0ycGiM3C8GBwFbdQxtMQU3Z3FfxKS7ftWefBZJ0JYbCUHc3ZPrDnOqeTOb3v3C7_zNL1_IaLGzXouHa2V_2KezFkdIMwGvbP1gZQJTG_HNlTU6jV15NOrYX8SCGSejXPBnlct33AUd1J9CPQrgpgOSIv8ZE1n3hOSvy54xxQDvkdCF9psGnVT8syW4OKHVcG2ysNQA_LeK0eqEcN0YxccWKTz0S2gSb4fHAEphQcIfOIokDLzbKyKyqXHnq2LwoXcG2jlyVsd7lHXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28788" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs-zQF6IcOesK4obD_wnU5B5wxT7kgtXBxqAGZZS5uMUG-wxeyQgY7okmv1wNd7O3XNopcQ1T_iFHEb_REvlV-X5kkp1qLDAm-7sq4mD_ya36GuT1q2xNV5xBAlbtpkxXjgUBbjOTcGFpUklfGCuyHZsE6yoQCE1Sgj_J3l4z_5_A4lWvhqwHY91n39ngs6QR34xdo70-4ENE6-6UfCvjire1d0t14dNYmzTEjNvXgCGMQX3WGyrnh9voduHnP5jI9lvBnb07VjIaXEWs3vc-mSJurpYOUpN2944ZUCTsMU2vefwwkFKMk_Tbdxeh7HXGi6ZL3lz2jqPRtDPsS7uMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
🔵
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ درصورتیکه‌هلدینگ‌خلیج‌فارس‌تاپایان این هفته 400 هزاردلارپیش‌پرداختی به عزیز گانیف ستاره تیم ملی ازبکستان پرداخت کنه این بازیکن قید حضور در تیم تراکتور تبریز رو خواهد زد و آبی پوش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28787" target="_blank">📅 11:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdgWtxHl43Ymk1UnTVc0OkY4KEJoW1IqltA9GXCaifqDjS9Y_FZpTe6EZ7ZUR-pzYbm4DSfOnPS7jl1ThYJKQswOSdsQbmDPkdVl_iG3syD6S_3vFbq7sqW2XVTEqWvRRytIo98DpvWBKgu_9VmarQjS79qUliZyqH0ul9G826nvAkwO6I7DZTu4O4OZGXi8XXjeI-tnRDjElp4KoArWUR7PntYSOvtKLuR5KXjAdKYGXIv0h4GnXtQnd57TzpOEtXp1n6X2HlzJgq8_iNI4y5d7QRceUHORNgRHU5lCMlBgS9-q13xGepZwr0HA9vNlQkW87IpXVvwVysPlnq3N6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28786" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28785">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2CyFAJsU10HzpL6w0XMcDKyOfkoMgAdqy4qOInZX4PkboGkYbGYB3hcjIqk1oL6lKb0yZAZZwiEGPoIGktOdXJkWjRiZM8AXrIMn42yyGF8AUmCAa9Zd_MvdT7DrVfI5aFIY4N4WtsyjivKBgSKy0BWw51cx6eO55NHtA1-aqSCkzt-52hflSfvAYN_4VL39Pf1nML0MK0pzRYxqNHAtyuUUMb0tJdhZw_-EPeBkqpdtXl-SMSxlMdm__OACkTGUYynX39pBR4D1NsDj4CECyYa3QfuhIkiDRY7WN3JvdDqnCT2X845qqMp6FmLAaffyKCvK_Sphv1B3ZbudltNeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28785" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
