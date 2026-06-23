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
<img src="https://cdn5.telesco.pe/file/fKriYYvzTOiAeuufOsxubZX_fSB5eZK6sDHlveIFM3P0s3lutitTCmQbMztfOeGuuY8NM9VLh834NtwtuEaTCpofk_3CiMoG2MCQLDBdtoZ9anvYiZoAGueW9bhfia6EUZYZkqWrhT1pyrJiLe_LNK7OPUpdEM8teBgmz3BdSPI4QfjIQTuQMwPkXUoyJJ2_xTI31cmCErv1-lJ2uDX39YyhiYjb3gVbHYim-ZLMQsctTiekOJZAMlwV4X8IwwT3VO5PrYKmMvzkTfLpYvfyETOKNjtBenZsQctk6XUF0s_SeqQS4rz9S4537G58MF8_-apzpI2dqMUHNul-THt2tQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 725K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 15:06:33</div>
<hr>

<div class="tg-post" id="msg-95425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5UyrfckzpTWkryG2LZnGhc4ULlLkUttPRhrf8d8WeH63yZUQRHCj9yWA2RtLb9dYboEolGyzYTjQGZZoCXROxwv77-uLVU-GRdc8DgdsC4M-ME-tG6L6ZrDGnlbjvWrw9fBVWnf8oZrTA9OyQM3px8Y6ssZOzPivkcPBNBHpLCzTC-s-rxemNjY7yLF6UxCsXmf1UKasj0eeCICIRiJiWo9lCq8sgZiewnwdf7GoH047m3IhB0lg50MxBGLVxa6315ntAQZOkThaiajhh-bf3EzdHmhi3ehnPuac_IuQRp-J7CQfqiSPlGwhU2e2c_06fmXZ5rC1Q3zHInbPE71Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
روزنامه پرتغالی A Bola یه نظرسنجی گذاشته بود که حدود ۷۰٪ هوادارا گفته بودن دوست دارن رونالدو مقابل ازبکستان فیکس نباشه و حتی تو بعضی ترکیب‌های پیشنهادی اسمش حذف شده بود. خیلی از خبرنگارای همون رسانه هم رونالدو رو تو ترکیب اصلی نذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/95425" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d665bb9f8.mp4?token=QLwqP3KmkHkA995_vOGaeMWvW2Ybqr6bs1fXANuigSNljfh4kw7CFGMi_plRwe3ynA4SkVu_zPFOr-e1RcnaK9q528FLfbB7uo75RJWfvKtGvGP5T2xt0P38piAXtM-64hq5OADH0imIsXiluK4hz303ss0i9cgyaa4B5VQTuvcDZcUroHgBcMQpL9uqTrJFtacfVqHNmVazpzCVcgxxhaZFghQjnV_oE5eFmsruySSpL7UVyMBvdBlr7I3Qq2S3YuIJSl_AZ6ykQrPdtbK2p2-sJQaByi3m1gP27VQ5VbWBgnmAgIOiEgsW-JKV3RZ9e_0DsYkJUY12ZUiA-FhG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d665bb9f8.mp4?token=QLwqP3KmkHkA995_vOGaeMWvW2Ybqr6bs1fXANuigSNljfh4kw7CFGMi_plRwe3ynA4SkVu_zPFOr-e1RcnaK9q528FLfbB7uo75RJWfvKtGvGP5T2xt0P38piAXtM-64hq5OADH0imIsXiluK4hz303ss0i9cgyaa4B5VQTuvcDZcUroHgBcMQpL9uqTrJFtacfVqHNmVazpzCVcgxxhaZFghQjnV_oE5eFmsruySSpL7UVyMBvdBlr7I3Qq2S3YuIJSl_AZ6ykQrPdtbK2p2-sJQaByi3m1gP27VQ5VbWBgnmAgIOiEgsW-JKV3RZ9e_0DsYkJUY12ZUiA-FhG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏆
تو حاشیه بازی ایران و بلژیک، یه بلاگر خارجی تو استادیوم میخواست مخ یه دختر ایرانی رو بزنه که مادر دختره سر میرسه و پلن پسره میره رو هوا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/95424" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC86VlvY_W_0UyhbqQBB2nHZI02zAsdHivfrjRDwk5gLG5cjpK_ndjpJRnhezjZVTYyQvRLUIvA_egm-e8lp03XNYQS7fi8mMX7G4qOkuOLW7smMqztmalcw76GZkVjJjtir3JwIvxLzAhFqbMlUYHTyPKSz_RRRhGbro5TEEKuY4WSyGw5Pt1Y8cOtm5Dy-qx9nIaGioTjBnNJCQesxP_Wf0BfYoWZxgEqmlrX-VU-1P_qhXwI_yaBkeceeaIqPvyYIjeBaI0eMP-IKkYT6IWe5Pcf-nhepufXcvoypLlF3R45OhbHprXKB2t5lg72JE9ZqFslwlOrIPUkZ0Wc6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
آربلوآ با قراردادی سه‌ساله سرمربی فولام انگلیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/95423" target="_blank">📅 14:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5r-vCPBASfkgC-9osaUEfVVceCnVwG3Y5m5JnLI9T-litllrz-fgSCm5jP9PHL403rVkv5gD8tnH466Ja8Kim7SLmTm1jFGiLcspk6_hKcaQuWKW4GVDlX5TyyhglCeyPYIr_c7-dE1sgsxaWCd_DNLo8OuGZHRJ_VSzVoqhdKDsej6rep-ZDHMbB98CGr8QTjQLPcZ10qOmuwzyMePJ-ztoiGcMVnuHnIeYKoAfgBe2vjZWGJHn7pdmNHTBtDw5xsTsU7TcYXt3T0g-V4oyNGPUtyoAxD3grw6ir1BZT5ae5Yo158I1_-KWLwNY0DeuvykxwKBUgy3T-nMDIJH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
ستاره ها حسابی خوش درخشیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/95422" target="_blank">📅 14:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed268b84b.mp4?token=HZcUtuwVFpX9m7XsiKPU4sArp9-Dc1hSr78zroIUXEk9PhmZC6b0bY1_lJjHL1EpRAguPkl7KL26pq6XRgxzDSh_HiAgxymYFwY5k-_T6OtoDDOe5BuP6zSe5xgr7rt3adWHVH4AAwDdt7m6eqfIvZDjToJ_-tjolHU68R0IJEMS1hedhj1mtRgvllXHkzywuioVYV99Mx99goYln7eqz6mphybbdwrlM9oWwCEKkFrgkFqTgK0PoUJNekc0_usxINCF6IfJnwVW9tc9f7F4d1J_l0muS37FXkeepXtlSOG4Eqr2ydkaydwPAAWTpd3SgsBzGLRzhCBHeziUuU71JISX82JezfHQk3fT6IdyUe9YcFuMcKklDm95-I6VcVxo-sgL1pjFUOVbefdhZBOx7d9MWR_eqkpFRpZMQonGNUU-jE2IU6P0vwrzrcO8A41oG2JMh6ATdR23o0K4Pnqis7uwCrVRbSYqCGuNo0Bs0R7Xu0pmfmm2qjpXYH3vomaBqe_1CQgWVL2_WavB1WrW3ByC5LntbalAc4EcnbYetLWn-w_ML8GQ2izZglNTYX7h_EkNXI07xEOj2xzBcq_MoRmZm8R-0MM5lExLzX53eym4kYuVbI54A6VJfe2F6b-qFc2bNQoshad9VjPeY9bTQ8KmwiT24jUtDtsUpo4j1L0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed268b84b.mp4?token=HZcUtuwVFpX9m7XsiKPU4sArp9-Dc1hSr78zroIUXEk9PhmZC6b0bY1_lJjHL1EpRAguPkl7KL26pq6XRgxzDSh_HiAgxymYFwY5k-_T6OtoDDOe5BuP6zSe5xgr7rt3adWHVH4AAwDdt7m6eqfIvZDjToJ_-tjolHU68R0IJEMS1hedhj1mtRgvllXHkzywuioVYV99Mx99goYln7eqz6mphybbdwrlM9oWwCEKkFrgkFqTgK0PoUJNekc0_usxINCF6IfJnwVW9tc9f7F4d1J_l0muS37FXkeepXtlSOG4Eqr2ydkaydwPAAWTpd3SgsBzGLRzhCBHeziUuU71JISX82JezfHQk3fT6IdyUe9YcFuMcKklDm95-I6VcVxo-sgL1pjFUOVbefdhZBOx7d9MWR_eqkpFRpZMQonGNUU-jE2IU6P0vwrzrcO8A41oG2JMh6ATdR23o0K4Pnqis7uwCrVRbSYqCGuNo0Bs0R7Xu0pmfmm2qjpXYH3vomaBqe_1CQgWVL2_WavB1WrW3ByC5LntbalAc4EcnbYetLWn-w_ML8GQ2izZglNTYX7h_EkNXI07xEOj2xzBcq_MoRmZm8R-0MM5lExLzX53eym4kYuVbI54A6VJfe2F6b-qFc2bNQoshad9VjPeY9bTQ8KmwiT24jUtDtsUpo4j1L0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
خوشبختی برای خارجیا يعني اینکه آخرین جام‌جهانی مسی رو از نزدیک تماشا کنی و لذت ببری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/95421" target="_blank">📅 14:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS-d1vrMxt6ISQ9C4wxKc6vQKyYx_xUrlmcfERQNdRlklxqD1rC_ZsiN95mY22OM_3KryctMuErBTQ4Mn-IsnNLhTLYbl5-FH3CTehqj6Khb2SmHu4N1a9Vdk-8YfpjMAH8MICUjw8vT2-zWF79InMp1jGk0d0khkT1yP7l1cSmuz4pSEHQOBYMu6mCq9zapIBmb1CyIjTcS6gxN6mtDX5yXe6lnH773E2-swq_3ztfwgN1NJodES0wPQnXUDLHVXx9uBgnqmWFAwGucPgO9VvL9MNK2dMyPIn9_vnWrUdVhXJF3Z6vxRQCxGO9ol9CguuM5FQLZTzFKdwLsg2XcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دکلان رایس:
ما می‌توانیم هر حریفی را در دنیا شکست دهیم، اسم آن برایمان مهم نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/95420" target="_blank">📅 14:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95419">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raApuMSaDlgjBwJvKFDL8gpFitW7Dfd7MG_BFfzVI8wgCPHD38qI9PNqJVmJ0pR-F5UcYr3zPgJw02cFk6XOxQxv858WJKWLNGVx22FkjoVRywnpjNIDW65AGdybxW0Bct5KkfCcW5pUyD0cimPa77J14tvIcDIWO3VfBVvgqhA8GH9W8HRw47mbI3FumeUsY0ZHyoGZfW2H8FR3x7DON2fC_LDtAgHitxH6EnZE8DskUuTrC97LyLkf3DkDo14nD86JbH8LXf-RVTCsxArhJMs0v3DxZfZ4Mt19vJAQigQHD7a7UPCWnbBpPfMtVeyxsUdJhIoxwajVpn94a26tbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
آاس: انزو فرناندز به رئال اطلاع داده که از طریق وکلاش، تمام فشار خودش رو به چلسی برای جدایی میاره و مطمئنه که فصل بعدی به مادرید میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/95419" target="_blank">📅 14:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95418">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNLp0WtFb2ekjA-Irl61DD7bqvNbdPJ7qotUZbcJ09AsOOx3CT7vN8VITCZSejL9EnG7cRHqMT62rKrAZS7YhRSdzrmd5PG7t7jNbYA1_XOwKz_lHkJvaSfa3E4hImLswVaDWeas5NHIflLKRsOY0eMwNIpUI8T97EuebVnAxVSxXN70EVQVXVAkWI3a6fVFlaXrhWOW2cb9kHxei1y38YcBeQW5_3xdO4HzNohRI3KyxP5BKYk6RG-79oyLAwmWKRA7pM07mqX8SAePbMIVrrJyQV2ZaMLu922mZzy6GglGUdGCp8DESEmd9RwwCDD0AAFnMGTHxKOdAQkQfBIMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری
؛ منچستریونایتد در صورت دریافت چراغ سبز از رئال‌مادرید، قصد دارد برای جذب شوامنی به عنوان جانشین کاسمیرو اقدام کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/95418" target="_blank">📅 14:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95417">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a7dac311.mp4?token=kYJcP7oAf3IM3BTRSvGDENPDx1He2FXa0R938dseDhWoNEOPCygUp230vdYfEdcKu2YXRPp58mxHf3yGa-eCcYTH04hpdT1-N0_BbFKJmtVihaXLdTF3yWWT6XRUVPvbWcA-4e3gy17dAmSZ_0tfo1giKPPgU7CxvY_w_wryEwzWrfco_ypmhcWswax-zRe2Zk-jLc56aGkuWyLI9LFqS1zDDSAeZ2aVmJXEYCnC-sfzUsSMY4j1jCTVQYnBJzHhKBcvrAALRL872vl_9oDKg0S_goA00KL5RVQ3ph1Uc-XW9rBvAQh0hZLyaZcBrkF8rtBhYBHXb1wPY_Pi34viGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a7dac311.mp4?token=kYJcP7oAf3IM3BTRSvGDENPDx1He2FXa0R938dseDhWoNEOPCygUp230vdYfEdcKu2YXRPp58mxHf3yGa-eCcYTH04hpdT1-N0_BbFKJmtVihaXLdTF3yWWT6XRUVPvbWcA-4e3gy17dAmSZ_0tfo1giKPPgU7CxvY_w_wryEwzWrfco_ypmhcWswax-zRe2Zk-jLc56aGkuWyLI9LFqS1zDDSAeZ2aVmJXEYCnC-sfzUsSMY4j1jCTVQYnBJzHhKBcvrAALRL872vl_9oDKg0S_goA00KL5RVQ3ph1Uc-XW9rBvAQh0hZLyaZcBrkF8rtBhYBHXb1wPY_Pi34viGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
خونسردی خاص اسکالونی موقع گلزنی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/95417" target="_blank">📅 14:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95416">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaS49AT1ssMtRHnGAD4pmCFW_NGWi2OnEWaALl09gp9BlNNa4xnGrpiQnX9Il-Ce7bffQ_bvXhGnFwjpcyBTd6WPxD5DtgPKyyfQNjzcgpL-vdEiWL_2txnEh2_SyxJ_utxfiSU0LFOs_ZMvnaseUGYsoPJPowkOSBz4wSrWW35C4J62y9cU__2bEoh1ilttYdTCBxtSkG85ffqvmegijZKQP38U4k_DXla7lVsnYwCEIzJ0UNm3zPFBWs1Yk-15OZNgGT1u3Xr3x9UUIpo9bXTZrStWayNYxD826_KvzKyAUenl7EBZ1P0DaWuQ5gv6URjFb_l4252r2YdoV4Syjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏆
خبرنگار رسانه بین اسپورت در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/95416" target="_blank">📅 14:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95415">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTKWud0soaf-CiURftqHx0EBYsxhJY-6H0h74tRQzPN0r6SxJnfplKucwCO1-lXobyXcUhtKks9EMrGkkaUlX8gejTMjbwO_7BT9AIB16jZOQxOT8-tDRmrv2ihzwoUh246ifIklhOvyrv4826J_My99n4eGABVntcvlKBBjLao8PjUZC8DRcvz5vZVww7lzxDOCviHJRu6airZxVEdgHjC0zJXxZfJjb09K3X-U6jw9tP3I1Ly5GzKRk67Pj3qV0ZgBTCSC06zGjZbhJLRWmReYgoxU92SIj4HTqjwy00Bh-eQVKKtHLLRL0GnZb9raUpXu8PS7fIfQl9BDgNLnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🤣
هواداران خوشکل عراقی که باید زود با جام‌جهانی خداحافظی کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95415" target="_blank">📅 13:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95414">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCdKnjnb1iWlDNr_10r1dTF8_w6BTMkbHNYN_AEYC77qz8ZKe5tVscXpNSfizg2cpgA2Pcej2IqJvuIabJVcGhWiK-9omtjfnh3xBeyLLivL1kMkeyGpnKwQPRYMJQBPVQFoAn1_g6kqp4zmSFOp4NoQBXYH6BDO8HP2x6Mu6eloVXMPYQ0rcR6xYoCIyZzipcZpVkC7GTr0HUeo6nmhRA3lcE0s_QqTVbPxE7JJMAKwwJCf4Ae8f9rShcpaxB8o78BOLY0wFG6d8O1ZNgWpGnXaeoNj8uSDpzz-IpN0cnFFXn2r70lgtFypKeFUYEg25B6uxB8Dq-Ri-JedwRSJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
وقتی آرژانتینیا با بازی مسی ارضا میشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/95414" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95413">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/95413" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95413" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95412">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=aq6wS0S24Z5P3BSBy_GB5VdAECzJ_AMG42izD3_kdgwcCahMuS93C4IIHrdD29oKlO7DlGnHdUS7K9sZEVYruwMFJb1upknODrBP-BkAFOSFBApa9V7JDmFcj2FevGHsb3jx_2aK4hxwODE6T9nR8kNAiQXz_UwQud0K67r0VI7_VNhgsjDy4JOwRKxvpcrqc_TyRT0JaPaV-AeVYNrqoMZMpMTcEnsKdtybucS07xpVRt6u7eIaJIAIy41pyWcRsYemoAHWR0aMYGn6Kbgq8dJRj5PBR6Ilz-AKe8mXYWlrMWXtbwuOPfN-BHzBA82HzA7C5Q5-zib-4q7D_9scuGvKLiWBe5FFYy_i17Q9Cpc3KHVegn8XDvamTtCzRt075we4MId4pS0I_hyJNUQfODrNhKBHmY7lOjEdntc-cs0cnYmuzaWwhdE9GeUH7cXI8-quae_OxipWr6sPe-AFC3zxHd_ryABNRHP-wiJ57xm4caX0yASe_P0kzPL0VOnOeTrXDTYfXq8s83JaZHUxcJ3w06MuPQJBzyAk5AVfEsSjuu9qQnO0DKSo18M64gRDQpyBFGDcqNSutXkvQr4F-cHHOiUjkPtScwXZ8P3-Y-y5IJiLmzU6y5WyGTJDRCOotQ7MmWI1XH4twlCCt27_fERaULjLvhbcwhaX2XjZqvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=aq6wS0S24Z5P3BSBy_GB5VdAECzJ_AMG42izD3_kdgwcCahMuS93C4IIHrdD29oKlO7DlGnHdUS7K9sZEVYruwMFJb1upknODrBP-BkAFOSFBApa9V7JDmFcj2FevGHsb3jx_2aK4hxwODE6T9nR8kNAiQXz_UwQud0K67r0VI7_VNhgsjDy4JOwRKxvpcrqc_TyRT0JaPaV-AeVYNrqoMZMpMTcEnsKdtybucS07xpVRt6u7eIaJIAIy41pyWcRsYemoAHWR0aMYGn6Kbgq8dJRj5PBR6Ilz-AKe8mXYWlrMWXtbwuOPfN-BHzBA82HzA7C5Q5-zib-4q7D_9scuGvKLiWBe5FFYy_i17Q9Cpc3KHVegn8XDvamTtCzRt075we4MId4pS0I_hyJNUQfODrNhKBHmY7lOjEdntc-cs0cnYmuzaWwhdE9GeUH7cXI8-quae_OxipWr6sPe-AFC3zxHd_ryABNRHP-wiJ57xm4caX0yASe_P0kzPL0VOnOeTrXDTYfXq8s83JaZHUxcJ3w06MuPQJBzyAk5AVfEsSjuu9qQnO0DKSo18M64gRDQpyBFGDcqNSutXkvQr4F-cHHOiUjkPtScwXZ8P3-Y-y5IJiLmzU6y5WyGTJDRCOotQ7MmWI1XH4twlCCt27_fERaULjLvhbcwhaX2XjZqvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95412" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95411">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc538548d6.mp4?token=OLIHxcooOp9le98DDX7hDRhR9OJIRXzZqxtt8nWol4lexcFeb8EUym5cUiwTDO8o2xApdtfB2-75rlAGfmugJZSOfV2zopSwS7lFLUK5hpSpk45qQUIK4zB3y8zfF__hm-SjnDWRQIL3rmaREhZLZ-SsmkIP2CtXdpYJ_9342hrfY5CYf16JpCCY3vkcBYLUDhHJBBAByM-T1vN85MrOSPfpsVazcZS1jwmWUps8TWvmZ94nvMnRetB4Pv6y7foAh55dil6rZovZG5v75nl24e968nizKwJ4fG-YO4-eab_KfWaN1oi0_1KENWstY5pZh2zhBHp4wDC1Iakw9zU9ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc538548d6.mp4?token=OLIHxcooOp9le98DDX7hDRhR9OJIRXzZqxtt8nWol4lexcFeb8EUym5cUiwTDO8o2xApdtfB2-75rlAGfmugJZSOfV2zopSwS7lFLUK5hpSpk45qQUIK4zB3y8zfF__hm-SjnDWRQIL3rmaREhZLZ-SsmkIP2CtXdpYJ_9342hrfY5CYf16JpCCY3vkcBYLUDhHJBBAByM-T1vN85MrOSPfpsVazcZS1jwmWUps8TWvmZ94nvMnRetB4Pv6y7foAh55dil6rZovZG5v75nl24e968nizKwJ4fG-YO4-eab_KfWaN1oi0_1KENWstY5pZh2zhBHp4wDC1Iakw9zU9ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
🇲🇦
هوادار جذاب و خوشکل مراکشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/95411" target="_blank">📅 13:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95410">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎙
‼️
نظر مردم ایرانی ساکن آمریکا راجب تیم منتخب ایران. مصاحبه جالبیه ببینید حتما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95410" target="_blank">📅 12:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95409">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b6ab3616.mp4?token=Wh44oM7nK0Ylfdm4HNn0TkC5Hx-UqEBlsoZfAaOjkmCtTePvGDqUgTaudRK-FNR1KKplZJRTcvNtYXDMhnZuK6tlJR6Rg34eBVYNgk01CPEKMo-fQE9ukQ08-kE86mrOzCUkOtUGsNR40fSU2hv0PQfcWJvjJUsS5Oka0QA4wn10bILxgY7qHUdPqlb75DGoa7co9xcFIr9AxwMgv0u_UkEqjdPgygtFc4B-vpjUUftBQbGJy17Xbs5fl03v2NcVYyVSQelBnXdimmJbR18SmE2DZJ_tkXcoNre3aY6nNurCHlX7aOsMWdkndbEDv7Ln5N9ZX3R1IpUevCWXYJpgHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b6ab3616.mp4?token=Wh44oM7nK0Ylfdm4HNn0TkC5Hx-UqEBlsoZfAaOjkmCtTePvGDqUgTaudRK-FNR1KKplZJRTcvNtYXDMhnZuK6tlJR6Rg34eBVYNgk01CPEKMo-fQE9ukQ08-kE86mrOzCUkOtUGsNR40fSU2hv0PQfcWJvjJUsS5Oka0QA4wn10bILxgY7qHUdPqlb75DGoa7co9xcFIr9AxwMgv0u_UkEqjdPgygtFc4B-vpjUUftBQbGJy17Xbs5fl03v2NcVYyVSQelBnXdimmJbR18SmE2DZJ_tkXcoNre3aY6nNurCHlX7aOsMWdkndbEDv7Ln5N9ZX3R1IpUevCWXYJpgHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
حضور شیما کاتوزیان، اینفلوئنسر مشهور ایرانی در بازی منتخب قلعه‌نویی و بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95409" target="_blank">📅 12:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95408">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPpZBHZ12ODXOfSlzwQtyXZHAr9mJDevnjoXjBNK6ZEyaAptUGJ0kN_bz1lSBH0tndAUHl_vSSYusT31NnQIqkIUMiNrS8cJ7dihgy8pJ3eG4TBIrWAmmB0qZ6VMOEA5RuP7wmmu2fbtlZeg4HGrfzjuxjox8Pku1Je5TFSTsdyk-wGT21_X4sYMuFtWJkis3awyFgmVook4Jp73v6lkAx36moA5DsrSDmM-euXar_p453PSPVz5vRIPetM0NQGxmlQRo5ouPxbrhiLW3GzUV7jgMPDGuT459fV6PcRACuY7RjYdyM6Nnbqi4vKrxbzlWOCKGorIxCOXAwGdYI1kjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جادوگر غنایی:
هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95408" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95407">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d84bc94f.mp4?token=YujPpKjSoevs4bn4R70NI4Swd0LSCekdsWJS_zLWtEjFMORlamtu9NtsEUQVdirvSePtqaSIqpwqnrxACPW9cWiuQRbzl6-nVhvHFj1NOmmEl4-fxwlXB2FMqeVYzhtshE32BCbzjCMRNzNvDcljXwKa4UZwZbCb7OvEsa4lm3aMEbT-gc7cyfpOxU8M0qhR1CR2K66bq74128rLTghR4MQgfWxCjezxu_YSsd9wTAT9UiTtRgEutFdzHp29CBsw0rHANMLk2JWi4J1KtJq7Pldrb4TYnWPNW_JELk0k2sSlug-XMaP7WdA530Ik_qfj4MgGUQsj2lmsSbTWPPXoug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d84bc94f.mp4?token=YujPpKjSoevs4bn4R70NI4Swd0LSCekdsWJS_zLWtEjFMORlamtu9NtsEUQVdirvSePtqaSIqpwqnrxACPW9cWiuQRbzl6-nVhvHFj1NOmmEl4-fxwlXB2FMqeVYzhtshE32BCbzjCMRNzNvDcljXwKa4UZwZbCb7OvEsa4lm3aMEbT-gc7cyfpOxU8M0qhR1CR2K66bq74128rLTghR4MQgfWxCjezxu_YSsd9wTAT9UiTtRgEutFdzHp29CBsw0rHANMLk2JWi4J1KtJq7Pldrb4TYnWPNW_JELk0k2sSlug-XMaP7WdA530Ik_qfj4MgGUQsj2lmsSbTWPPXoug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تبلیغ پورن‌هاب وسط استادیوم جام‌جهانی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95407" target="_blank">📅 12:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95406">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10eab0b9.mp4?token=Dqsv_Yf860c4lSi1FTwr4ZMPbEKFJ-jl0OuS9ZSm2k-GGYIDbf3nuxrQK9pSRiLsq2FHNted-5pFcGmZQshUlDHrC4WU4UQtruebR4_PiwIfDwH4l2ysDVhVHz10_HIuSZ7G_y9LKElG5nlOtzzET7mk7FeiWS5SbT0nrlqLOpczgI5vanj5Td9CHfafPUxLTWNsoVDfIymJVc38VGDkM1dhyHyES-Y8oGVEsyZ1Dcrd2Jfcj0tBeOrcxwWtpDww5y9x9VfQG4iyFtKTmPIl0Y3gy8H5ATvABRlbGVlfnR3bGESLZIc4sD3P8TOutgJ3sF3NwGKg__5slQnJN9b0eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10eab0b9.mp4?token=Dqsv_Yf860c4lSi1FTwr4ZMPbEKFJ-jl0OuS9ZSm2k-GGYIDbf3nuxrQK9pSRiLsq2FHNted-5pFcGmZQshUlDHrC4WU4UQtruebR4_PiwIfDwH4l2ysDVhVHz10_HIuSZ7G_y9LKElG5nlOtzzET7mk7FeiWS5SbT0nrlqLOpczgI5vanj5Td9CHfafPUxLTWNsoVDfIymJVc38VGDkM1dhyHyES-Y8oGVEsyZ1Dcrd2Jfcj0tBeOrcxwWtpDww5y9x9VfQG4iyFtKTmPIl0Y3gy8H5ATvABRlbGVlfnR3bGESLZIc4sD3P8TOutgJ3sF3NwGKg__5slQnJN9b0eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هوادار مصری رو می‌بینید که بعد برد جلو نیوزیلند شورتو میکشه پایین
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/95406" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95405">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3c34fdff.mp4?token=Sv9yu1w6oDVu5T_JiSGr_3egBCELqDj00hWylPfIvkuIFkqT4ceV8p2YKyY0yFERLvZNqQGUBiN3zdWViBveYkXHMeNKHIsfr-VCwj_VRs18AEkAFVMv_5wzxvEnZ4KhgqZx0qRM_dLPdSycs814zc9SRSyuTIWpmiKJYBar0rizQGzRz5f7mHGDqvYrOIyd-TpA75Pe9AGLtLHuUjd4leE6-vnUMqwG0bvlBfoICvbeZJgVON8FZ2qCx_cAtvL4UqE5-rnzGvwnGMQUx_bkYHYKWt5KgAywYQvAWTsgRsMCFM1j5dzrwbJjUIfdOVJjCqyhpp7UNlUfmPTg9g-kpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3c34fdff.mp4?token=Sv9yu1w6oDVu5T_JiSGr_3egBCELqDj00hWylPfIvkuIFkqT4ceV8p2YKyY0yFERLvZNqQGUBiN3zdWViBveYkXHMeNKHIsfr-VCwj_VRs18AEkAFVMv_5wzxvEnZ4KhgqZx0qRM_dLPdSycs814zc9SRSyuTIWpmiKJYBar0rizQGzRz5f7mHGDqvYrOIyd-TpA75Pe9AGLtLHuUjd4leE6-vnUMqwG0bvlBfoICvbeZJgVON8FZ2qCx_cAtvL4UqE5-rnzGvwnGMQUx_bkYHYKWt5KgAywYQvAWTsgRsMCFM1j5dzrwbJjUIfdOVJjCqyhpp7UNlUfmPTg9g-kpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پشماممممم چرا بخاطر یه پرچم اینجوری بدبختو پهن زمین کرددد
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95405" target="_blank">📅 11:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95404">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde90ba169.mp4?token=GXR7l21KJwHSPdoNLaHOaTeFUdXl5-phjRO3ORKhsetaYXfqN87uEjGybCr5jfbccwzFlj_WPcPhJC79BvxcmctsI1tagTTsxLf5n7gm-vukhXcTvPGI_1glimsDOn512Jr0F4X5oIJww1aQPPKaT2CMtK9KEwB9YpW-dJsoPD1nSw58uVRueodEwYtMIDyblCMgvTKm6s5z1fTRqzZmkU5yRXgE1RafKZYBUSNegQDBj-Bm0SZjmEGKwweZIcwLXl8hNwqZ4NKWZ_sZWHa_-Ci42wN2EoYP6wm-nq5o5w0sqUuYJ3yYnywUEIqI2Xze6qQBudReJnae8Ahzqp3xHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde90ba169.mp4?token=GXR7l21KJwHSPdoNLaHOaTeFUdXl5-phjRO3ORKhsetaYXfqN87uEjGybCr5jfbccwzFlj_WPcPhJC79BvxcmctsI1tagTTsxLf5n7gm-vukhXcTvPGI_1glimsDOn512Jr0F4X5oIJww1aQPPKaT2CMtK9KEwB9YpW-dJsoPD1nSw58uVRueodEwYtMIDyblCMgvTKm6s5z1fTRqzZmkU5yRXgE1RafKZYBUSNegQDBj-Bm0SZjmEGKwweZIcwLXl8hNwqZ4NKWZ_sZWHa_-Ci42wN2EoYP6wm-nq5o5w0sqUuYJ3yYnywUEIqI2Xze6qQBudReJnae8Ahzqp3xHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از این زاویه ندیده بودم عالیی بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/95404" target="_blank">📅 11:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95403">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd135cd6d.mp4?token=BH7xWUOuH6O_z6jL-r0h7RzfiY_OCfRJ4v9FU_82p33bnDhlpmzPucP_ImLAG1zzw9oSWH0t-X4rS_yKtrJNvbwQ4F6ojsglrqBUoQvnpa8nu5zrgBjyffWmVfzITBOUofrypuSDMrkkvxOOFh-qlFlh3zYYtFcVfmbkRh1Of-x6P0ueIBeVsux6WFIhl9bWfOn30HfnHnFqlaXECtZ4-6sGCSTsEFC_h-Tb_zJatpE-qWkdKxZoXhv8xsvRZzA-Y1LI93-NkQ-qKPNkFz_RMUH-Xo8tDK7eBQTdb-BaKW880xA3sWDUja32eDRPaRjYz5-EreAQ8M2YKjdj-8hYSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd135cd6d.mp4?token=BH7xWUOuH6O_z6jL-r0h7RzfiY_OCfRJ4v9FU_82p33bnDhlpmzPucP_ImLAG1zzw9oSWH0t-X4rS_yKtrJNvbwQ4F6ojsglrqBUoQvnpa8nu5zrgBjyffWmVfzITBOUofrypuSDMrkkvxOOFh-qlFlh3zYYtFcVfmbkRh1Of-x6P0ueIBeVsux6WFIhl9bWfOn30HfnHnFqlaXECtZ4-6sGCSTsEFC_h-Tb_zJatpE-qWkdKxZoXhv8xsvRZzA-Y1LI93-NkQ-qKPNkFz_RMUH-Xo8tDK7eBQTdb-BaKW880xA3sWDUja32eDRPaRjYz5-EreAQ8M2YKjdj-8hYSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تقدیر جالب قلعه‌نویی از بیرانوند در بازی بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95403" target="_blank">📅 10:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95402">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2281627e22.mp4?token=RqIhewILbn4lvMFdddKEDX8XgrlNbZ057ukcxR4EvSMTajmoQXhnrbylvOZjJMCSIb2EhnKzgaL4xsiyjsBG2m9IfnJYv5cadLNWfLtnPKPdhRRXX8vuVF_I6KV_a1JAyi-JsQ-zHOT7qRsB6JiR2iKeBXv-vKzJblzrF4OdphL16UBWImu5QXqqRXarDH8YOzYpduH_dupdYh9a4omPMLyvoUpFW-D6h1J74MVJguC8qJQQVJxXUVdhdKffkqbzcfBhMwMsw0C9sZzl_hBcVzH8lKv2XNZs8Rbhvzmxv9Ex8GH0AqmPfJ77A8sTosMER4Wxb4ht7tLVmFDlBbvflg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2281627e22.mp4?token=RqIhewILbn4lvMFdddKEDX8XgrlNbZ057ukcxR4EvSMTajmoQXhnrbylvOZjJMCSIb2EhnKzgaL4xsiyjsBG2m9IfnJYv5cadLNWfLtnPKPdhRRXX8vuVF_I6KV_a1JAyi-JsQ-zHOT7qRsB6JiR2iKeBXv-vKzJblzrF4OdphL16UBWImu5QXqqRXarDH8YOzYpduH_dupdYh9a4omPMLyvoUpFW-D6h1J74MVJguC8qJQQVJxXUVdhdKffkqbzcfBhMwMsw0C9sZzl_hBcVzH8lKv2XNZs8Rbhvzmxv9Ex8GH0AqmPfJ77A8sTosMER4Wxb4ht7tLVmFDlBbvflg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
چالش هوادار ایرانی تیم‌منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95402" target="_blank">📅 10:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95401">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612c544153.mp4?token=A0-9acO33ie8OiTzjRRKtRg3feiMW9w067VwhHBFUdlGLHOnN70mD4hS4L2GHGSZ8xM-JtE0qQQAB8nh8ABbTOOW2WE2lNHKg5v_1zYhI8LhE1DTK_DJ2DZaj89a4zv1TL7JlLybqO_6ynOv6tCu6LkQsH6Sr3DJqwxxDPzfZKRCeeb7NllH_iI06V7owYrvAlXaZQMkVdqJvx8ux-j8P0H9xelfZ8Ygb0B9vc-C5vgea1hEUa7U3XiU_LrtoEd2AppyHwMZH06_r_gqxCjkg759XZe0UJDr2pCNH1NAxNZBVdjAnc6_mXMjtixtZRs9zgKNqxt1AeIbLTFALgl3Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612c544153.mp4?token=A0-9acO33ie8OiTzjRRKtRg3feiMW9w067VwhHBFUdlGLHOnN70mD4hS4L2GHGSZ8xM-JtE0qQQAB8nh8ABbTOOW2WE2lNHKg5v_1zYhI8LhE1DTK_DJ2DZaj89a4zv1TL7JlLybqO_6ynOv6tCu6LkQsH6Sr3DJqwxxDPzfZKRCeeb7NllH_iI06V7owYrvAlXaZQMkVdqJvx8ux-j8P0H9xelfZ8Ygb0B9vc-C5vgea1hEUa7U3XiU_LrtoEd2AppyHwMZH06_r_gqxCjkg759XZe0UJDr2pCNH1NAxNZBVdjAnc6_mXMjtixtZRs9zgKNqxt1AeIbLTFALgl3Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
پادشاه اردن امروز در ورزشگاه شاهد حذف کشورش از جام‌جهانی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95401" target="_blank">📅 10:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95400">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e962c1522.mp4?token=AL4tsnoCZPe9Mof6-QPhHbR63JTeJEUKkji_XxjfSJl-9THs6AdqCCX55Eyq9D27gg8wT8QqQGJr9QoEgmVbo9dP9b-TiCegY9fLXyQ3qaIpAFoJfngr4Q_vSG28tODUGrRvo0xSC-oDYCXuBD4QH9RYrd7zHRiY38NLMCWjgOWpD0lIUlxTj0i0M4RcxI1lav-QVGqMr9MnFoyNUrWLZprQbFpgFh2tbQFNINvoOZb_yw8ke2NooVt0iR9WK5LBc8GSRpsbUpSSRkfEQstr7KIeSUjkY3SSP-G23IbrS90vIpHr2KTYLUW5iEVfvUiJzHkPhj_CI7xcqZgpp1lYbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e962c1522.mp4?token=AL4tsnoCZPe9Mof6-QPhHbR63JTeJEUKkji_XxjfSJl-9THs6AdqCCX55Eyq9D27gg8wT8QqQGJr9QoEgmVbo9dP9b-TiCegY9fLXyQ3qaIpAFoJfngr4Q_vSG28tODUGrRvo0xSC-oDYCXuBD4QH9RYrd7zHRiY38NLMCWjgOWpD0lIUlxTj0i0M4RcxI1lav-QVGqMr9MnFoyNUrWLZprQbFpgFh2tbQFNINvoOZb_yw8ke2NooVt0iR9WK5LBc8GSRpsbUpSSRkfEQstr7KIeSUjkY3SSP-G23IbrS90vIpHr2KTYLUW5iEVfvUiJzHkPhj_CI7xcqZgpp1lYbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇪🇬
هواداران سوپر مصری در بازی دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/95400" target="_blank">📅 10:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95399">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
❌
🤩
#فوری #اختصاصی_فوتبال‌180
🔻
اگر اتفاق خاصی رخ‌ندهد، اوسمار ویرا سرمربی پرسپولیس طی یک‌هفته تا ده روز آینده از هدایت سرخپوشان جدا خواهد شد. اوسمار بدلیل مشکلات خانوادگی و البته درخواست حقوق بیشتر نسبت به فصل‌قبل، موانع مهمی در مسیر تمدید قراردادش گذاشته…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/95399" target="_blank">📅 09:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95398">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b71ff2a0f.mp4?token=tBRw8HHmYbw2J8Eh1KlKYUl9kICFtu_izTEbfKiKRUJxXCQytOtts8RXHjLS6AL8YZDNETDb1YVCEeZQCsc0ghuPq-E5TEdR-8p030KOQwD79dugS9awCWdaQUYQnjwzJ2QC91ZNIsKkK6gNJnI3Giwo-khJABSrtyfPh4jzd72CgTRI5RBNeku-L-3MiTPpK-jgRNKje8honGssfOX47niKLRflLiiyxR4E26a94rYnzr1ensV-KRe5y5Zn2gsoPu05KcEMz-xsB0JY-DgqRl_LWRn9xH-lsFflUA7CgyJcgCh9Zb9G5yAB1lp75AP2qaxPvkriMDo2CTn8wuYNzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b71ff2a0f.mp4?token=tBRw8HHmYbw2J8Eh1KlKYUl9kICFtu_izTEbfKiKRUJxXCQytOtts8RXHjLS6AL8YZDNETDb1YVCEeZQCsc0ghuPq-E5TEdR-8p030KOQwD79dugS9awCWdaQUYQnjwzJ2QC91ZNIsKkK6gNJnI3Giwo-khJABSrtyfPh4jzd72CgTRI5RBNeku-L-3MiTPpK-jgRNKje8honGssfOX47niKLRflLiiyxR4E26a94rYnzr1ensV-KRe5y5Zn2gsoPu05KcEMz-xsB0JY-DgqRl_LWRn9xH-lsFflUA7CgyJcgCh9Zb9G5yAB1lp75AP2qaxPvkriMDo2CTn8wuYNzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بررسی کیفیت تیم‌های آفریقایی با کاوه رضایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95398" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95397">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee4859e05.mp4?token=oja8wzEtq23AwOZw3Wf-hDHFDXOobBtyOFR3iOEbbu0P_qeLaEqjsjkR0y8oaiN7gL86FOAOy6ZTO6ktNBw5OKElOTFk8IHZAxV66hwflytUTLaAK7hhwzNh8nOBgLNYIR3UGH4xLM5ssz1e64M-ZCy2t-gT5RBvsC0Rw0sFFMn8N2Xu5BjgWHsqDiiMrySrE8M7z35KWhT5cSSX3OagmKsNItGMzm8DV6l3bd5zpAxumWl_7OnG5oCRw9EKfnqMElHB29o-MVoF-MXvgQtTZh09geUf9RKV7DAExFnWzPLxQKzqKy0rQC6LhnLV0yBAToZA9nTGgFp90lYpA0k4iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee4859e05.mp4?token=oja8wzEtq23AwOZw3Wf-hDHFDXOobBtyOFR3iOEbbu0P_qeLaEqjsjkR0y8oaiN7gL86FOAOy6ZTO6ktNBw5OKElOTFk8IHZAxV66hwflytUTLaAK7hhwzNh8nOBgLNYIR3UGH4xLM5ssz1e64M-ZCy2t-gT5RBvsC0Rw0sFFMn8N2Xu5BjgWHsqDiiMrySrE8M7z35KWhT5cSSX3OagmKsNItGMzm8DV6l3bd5zpAxumWl_7OnG5oCRw9EKfnqMElHB29o-MVoF-MXvgQtTZh09geUf9RKV7DAExFnWzPLxQKzqKy0rQC6LhnLV0yBAToZA9nTGgFp90lYpA0k4iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
طارمی تو رختکن قبل بازی بلژیک دقیقا چیزی که می‌خواستن اجرا کنن رو توضیح داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/95397" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95396">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119aca2671.mp4?token=PFS-k0vOy1VVaBD5XvICXWVk2Pj5lg0GBu0sAG_mHnoySyI-oDaZIvzSInsyKYQep9a8UtSIlNPbt4mK9Yn8yVmiNRVIwKIN0KEIIAS3mWJD-RRb2Lyekh_ptg3lAfkMm8zHWOPU46aPq3FoynrgDVi0fxecA5MRGZcxrobB6eWMbuZ2jN5drWscdP-5x9LHkarI5uMxw9oPEsfxUbkH7zI5PWS5Whv8hObiLPZnNOsbsy5N-2qFvSH0-_3GVI-pWmtOv4kRHS9vdG0GH_7WyRKtjIgnhRBJ3Npe741uJwjNXTyLsooM0PRFyTybfL0ETbftwjUfkGXEfQcAZdynOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119aca2671.mp4?token=PFS-k0vOy1VVaBD5XvICXWVk2Pj5lg0GBu0sAG_mHnoySyI-oDaZIvzSInsyKYQep9a8UtSIlNPbt4mK9Yn8yVmiNRVIwKIN0KEIIAS3mWJD-RRb2Lyekh_ptg3lAfkMm8zHWOPU46aPq3FoynrgDVi0fxecA5MRGZcxrobB6eWMbuZ2jN5drWscdP-5x9LHkarI5uMxw9oPEsfxUbkH7zI5PWS5Whv8hObiLPZnNOsbsy5N-2qFvSH0-_3GVI-pWmtOv4kRHS9vdG0GH_7WyRKtjIgnhRBJ3Npe741uJwjNXTyLsooM0PRFyTybfL0ETbftwjUfkGXEfQcAZdynOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇳🇴
احتمالا پس از موج مکزیکی و تشویق ایسلندی باید شاهد رواج شادی نروژی‌ها باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95396" target="_blank">📅 09:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95395">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOpYbSQuB_AzefRNLF2OB19DvCSLVcwj04vqwT5XmxqNf4A40DceMS8F1XHXMJ7KjePtj_2jvXiuBgZWPL0lBSBdHk5D_qYPsYYhDyOwgKyzgaA2ACaGII5ZR0i_S6yyvbMFT1H-dHJnJoH2cVWy6G31g67AGcrGGMC6PUxrCadI7gS87zKdyd4uZuMzYwzDS9boctUrWlY3FuV3hbB-9vrvJlroiACe4IWjKCsliZh0areJr_BZaSlkFpDfXXnbtdV4OjMn27IZI0wNcIMkKCDg-lmc06UPu37dGAwI2DTrwAe4nhL39xxQzGxEbNq58QnB68D8FRA2qWRR6dvssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇯🇴
تیم‌ملی اردن از جام‌جهانی حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/95395" target="_blank">📅 08:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95394">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇩🇿
گل‌دوم الجزایر به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95394" target="_blank">📅 08:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95393">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8863fc015f.mp4?token=p9n0kCRlpGX11jPAXdH89fpGYLR1eLtnYVzRKBiAGYOyYxSPCTyBBQ0LULcM6hzM1WhabBAPr2tCin0gcgZWwPUvhJDCsbaaRg-FR8htZ5Ahdqbn56ArGOnO_etH2b7mc4d6qUVsEUnqmStawFx0Xrmv0R20Qj3cvVBcykaIoX1HvqoBvNqzdu8CokprbWWUDtMQAtASmCPahfR60RFm5o8M1MJY0xsdwsUeAkhoWO9bo0LJZ5yPFJlnEVJcdKQo0PSXoszNX3jMUDph8P8Ad0mXuMNKW3xqhFdgPCmhh6nhU2OWrfXqh6RWGJknIiAfPlOhMJTf4Q6aatAzavfB9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8863fc015f.mp4?token=p9n0kCRlpGX11jPAXdH89fpGYLR1eLtnYVzRKBiAGYOyYxSPCTyBBQ0LULcM6hzM1WhabBAPr2tCin0gcgZWwPUvhJDCsbaaRg-FR8htZ5Ahdqbn56ArGOnO_etH2b7mc4d6qUVsEUnqmStawFx0Xrmv0R20Qj3cvVBcykaIoX1HvqoBvNqzdu8CokprbWWUDtMQAtASmCPahfR60RFm5o8M1MJY0xsdwsUeAkhoWO9bo0LJZ5yPFJlnEVJcdKQo0PSXoszNX3jMUDph8P8Ad0mXuMNKW3xqhFdgPCmhh6nhU2OWrfXqh6RWGJknIiAfPlOhMJTf4Q6aatAzavfB9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇿
گل‌دوم الجزایر به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95393" target="_blank">📅 08:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95392">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الجزایر کامبک زددددد</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95392" target="_blank">📅 08:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95391">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc4496f0cd.mp4?token=grjCt9uib7QbnpEVK4uGFHLt3XVPdEkk9eWLM_osBZ0CQU-G2M9xnA1KFMNcE3XrqdWkyTlPfHgFmXe5sRvglckUhyBj_s2kJ0RJnUjcPmMPuRt9ntuSIPwrbSXczOdzrllNEqzGopGPIs4QKM1R-lDQYIDgOyOcWTjmcosDTCkvt5SN4184uHQfhyWqe-Awt7CgZbHWrpLxS4gMlyD49e0K5uOrVdxvns_pemFZONPG630rwzG2uBwhPQf3n0GPor9_Z3_yhxj40J1lrOgyPndra1upuNdgOodIene04x-sWdfLOP6sub9PXGEGw2Ns8qeKbF2uGLsEZ3MVWkdyNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc4496f0cd.mp4?token=grjCt9uib7QbnpEVK4uGFHLt3XVPdEkk9eWLM_osBZ0CQU-G2M9xnA1KFMNcE3XrqdWkyTlPfHgFmXe5sRvglckUhyBj_s2kJ0RJnUjcPmMPuRt9ntuSIPwrbSXczOdzrllNEqzGopGPIs4QKM1R-lDQYIDgOyOcWTjmcosDTCkvt5SN4184uHQfhyWqe-Awt7CgZbHWrpLxS4gMlyD49e0K5uOrVdxvns_pemFZONPG630rwzG2uBwhPQf3n0GPor9_Z3_yhxj40J1lrOgyPndra1upuNdgOodIene04x-sWdfLOP6sub9PXGEGw2Ns8qeKbF2uGLsEZ3MVWkdyNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇿
گل‌تساوی الجزایر به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/95391" target="_blank">📅 08:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95390">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلگلگل اول الجزایر به اردنننن</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95390" target="_blank">📅 08:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95388">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4yUs2vdCnb51qvNBOZ3na6cxnx_Frk-VE-IAJsXeyFUl5gC6tREZew4t1FkVNZbEMvwOiWbEmxfyP-47eHLg2ddCpduPX24v0YWLgOGIyV9siWSQHAEoyCsAjguTH9LH0p5deIDPjSWKBFys1VI3qNqh-vkhjZQ2rTb5i-cVjhFu5hMzq7mE_o9usF10oEYHQXrCM4zlBp-yLtWBLLOGpzV2WJjGtxF2bR6vjDA6Zi0qDjmEP8LRDqd2rEvkK-4GSAFGu58tEPhJQYJQmt25F8xt-u0AlROKN8yimxNSdV978UY46hesHNSzluGhSCcgbsqCnEIW0mnEPH-GO44Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muf41K1WJcDJQcsOGFBiQNPXSVGLFntKiVrvP1W-0PnhMVOcWKgXHO4mIhn_fkNIqZykFQ3z7q-pMzjxcBZbwaYxNz0u3KjCDyDwu_1eYoandxkfqibmLVAMg8qAkbthU_gK9uq6zF3demr5ZnETvbdape5PwTcV4sYPHPfr5gb4mwKjjJZtAroosiQPA8KmzQ5B-ryQmf5eT8oQ1ewiE81kaNebiD1EM1Kw6bkZk96mXOs_tFWyWr1rHlCTfUQnpMetB8GPgwb1FCIMUze47mOR-sRExbzB8_zvNF07CZpnoQHMQqG7J9f7nhHraW0jUH-psclTBTYfYmdb49Mnkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
کارلو آنچلوتی: یک بازیکن هست که من او را خطرناک‌تر از کریستیانو رونالدو می‌دانم.
رونالدویی که در آخرین بازی‌اش گل نزده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/95388" target="_blank">📅 07:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95387">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09b400e516.mp4?token=uQuX_f-aEnVkLw72gPol6WV_28xckRvgK6BYR6Ht4AYq9RuX_33bb1wMhxhD2LnHOH9trIpFdl51nTmMfdqydFVAJcHq5etIWy3qUb9GnGcAxQgBJXPKIoLA0VeJY6CNubTHqaapeIctVtCxkWC633x0zquNpDUszlCKsnPca1_FjXqj-Sw6G8OOAJwdeI1PMRfUGe1tKw8X-c-Nhvhe6AyI07pKl2ovE0v_mYt6XEL5gH47I_MftVBCLjXVzPVA4Yr7L9OiFEGLXUvkr35U-MJdbx9sXem7ICGTPoL44e0Gzmya5kmg1QAXSm7ub_oZx4uBqnHk6IPBgmCAXz482w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09b400e516.mp4?token=uQuX_f-aEnVkLw72gPol6WV_28xckRvgK6BYR6Ht4AYq9RuX_33bb1wMhxhD2LnHOH9trIpFdl51nTmMfdqydFVAJcHq5etIWy3qUb9GnGcAxQgBJXPKIoLA0VeJY6CNubTHqaapeIctVtCxkWC633x0zquNpDUszlCKsnPca1_FjXqj-Sw6G8OOAJwdeI1PMRfUGe1tKw8X-c-Nhvhe6AyI07pKl2ovE0v_mYt6XEL5gH47I_MftVBCLjXVzPVA4Yr7L9OiFEGLXUvkr35U-MJdbx9sXem7ICGTPoL44e0Gzmya5kmg1QAXSm7ub_oZx4uBqnHk6IPBgmCAXz482w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل‌اول اردن توسط محمود الرشدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95387" target="_blank">📅 07:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95386">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گللللللل اول اردن</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95386" target="_blank">📅 07:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95385">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شروع بازی اردن - الجزایر</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/95385" target="_blank">📅 06:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95384">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069fb238ab.mp4?token=ifr98j7zbAtDeQ06fbPe_JCdpkal6wE_-A4WNevwQVY8vRVZf5VtgI7OQa4EQ5UXJoeSygI-BOngbvNIyzFqEYqQUumht3GVNLzMamHrA9_1K_WwV77qfm2eSWGwcXoFMzkWYiw2bIvdMELBkslhrNEHU0bDFH8-IH5wCCjUJkhPg9GC7gScR1TLXcHx8B-EgM_x1jKbuoc4pkcc_Li9FzIRTXTYtdGJNpm0H2dJb36ljyMKgCvZDCGKD1OXNSvJVq2ddtKysQFe4qBmfJ4R8bd6KRkBToBpEpBTojXXp9jmxTKkejlbEl9oeqW6MEcwPw-lm_2k1l_HWepLT23roQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069fb238ab.mp4?token=ifr98j7zbAtDeQ06fbPe_JCdpkal6wE_-A4WNevwQVY8vRVZf5VtgI7OQa4EQ5UXJoeSygI-BOngbvNIyzFqEYqQUumht3GVNLzMamHrA9_1K_WwV77qfm2eSWGwcXoFMzkWYiw2bIvdMELBkslhrNEHU0bDFH8-IH5wCCjUJkhPg9GC7gScR1TLXcHx8B-EgM_x1jKbuoc4pkcc_Li9FzIRTXTYtdGJNpm0H2dJb36ljyMKgCvZDCGKD1OXNSvJVq2ddtKysQFe4qBmfJ4R8bd6KRkBToBpEpBTojXXp9jmxTKkejlbEl9oeqW6MEcwPw-lm_2k1l_HWepLT23roQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتخاب سختتتت بین تماشای فوتبال و ..؟
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/95384" target="_blank">📅 06:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95383">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUOpiaKbMqLLkvv2tUK58eXXZrLOoGPXknCsBYFAwGiCW4Sq2R3ouI2PnsKsWAYItgw8TZpIVMmruA0fjVS7RVkdgS3o-b6urE0Xo9w9fb3HACxuR4-LeaH12MruhpdWdgOdbNX3CFCTlQBZC6qxKzR27_ooHTxlbnU7IhYnEopm2MF_vpIMKEEqHueY-GQ0o7z87nzeEomTQWYRiDfkuH0skd8EbpSYd9iBGHuigeLTV79TfDOXMHeBOT5p5REmfY7wU8bUCCh6lugFQJsSi1oQqU1gH1TT--jMwUmV75ci7hTjqbO5c00Bv8yd9-ocdlFK6wBRcsTqpsp4nIzaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی نروژم اینجوری بعد بردشون احساسی شد و از خانومی لب گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95383" target="_blank">📅 06:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95382">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFA-NNbe-A109Rox3oMBuD8LE9IicTlumUeDueiXI9b-VSYkdkWymLi_hQVklYU_nzXY73mJiGHd5JNADSdK4WOXX6BS5ZV281M8cjLwova08y4IykPX6y4sVJ_eLfeuYoQuWgbQMaVqCk0-zNfHewXj7EflV-RDjSBbabs12QjCFeh21Yq2efpxA5ngv7SSOtvxDjWosycY3tvn7ko0EVIbU976L_BaCCmbmm_0YsXTvsKw-hxO2WIxvmB1KtxQJSqHBgFQLrCpNkC_u5a5nS94RlllJPxtA0cykAsmfqr97uRld7UP7JuyFcdDngmtKb4kS9bXHBeVHlOFv8KJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقابلی که در صورت دوم‌شدن نروژ و پرتغال در گروهشون قراره ببینیم
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95382" target="_blank">📅 05:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95381">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxp9ll8uOIYi0R8ELAwQZr-aVTX86jQyKXN6l2G2vWrISK3geNTgkFxrJDg-i0tDiTPaaeuMtAuht23lbUymAodPBfZDKyHmfpkp-q1qH5o9QfqBnsOxpAynkgLmA6KXOVWUb6ZDpRh4Z9-_RNtrssu_P0074RkgQu8Q6hq3j1dchLoAiSbcVFXHwO-zeTylb5gaH-_0c0HGWye2NGdXgaTFgPQnM3Yq9fUDl2eyPCk-tgLAS9yxsDXg-sQLTbZEosaWOU2amqH8HxVVPqRHh_1y6CnNpa1ohJngzzWgqtitL6-qtZMQCDesZ430epzBX-CUUIeAt5eVh8oNObSZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
در جام‌جهانی ۲۰۱۴ و ۲۰۱۸، بهترین گلزن جام‌جهانی تنها شش گل به ثمر رساند درحالیکه بعد از گذشت تنها دو بازی در جام‌جهانی فعلی هر یک از این سه نفر حداقل چهار گل زدن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95381" target="_blank">📅 05:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95380">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7d89f979.mp4?token=T5mKIBR_QvCriTe0l2UvT8hbdy3XZnnebzha4pPqxVZABzQZmkRwsJkXuLH0qFt4HsV87kCC9G4ccIJ2GLfN5ReYgXb7xwOVXnuEPf51oteoeJ_wRo4Q8HUKTKofIuZ2SMz6vS0CLncICIArgopjSjW4sLPRgfY4FWhg-j_41PRXcfoxUHJaxc5kwio8aRgTgKFfumhjIiz9OEm1Un5MtYLGKWj4ZGWUWawFDwPxN6KeiBjV6qnCzZVspXMtPe16BC9iN-XdRlNlKJE3rpsDL5JXmbefcyGwpK7MWFresIW0LakKH1Tsk9_BN85Bga04XP693_feDrRXD8rdsOLISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7d89f979.mp4?token=T5mKIBR_QvCriTe0l2UvT8hbdy3XZnnebzha4pPqxVZABzQZmkRwsJkXuLH0qFt4HsV87kCC9G4ccIJ2GLfN5ReYgXb7xwOVXnuEPf51oteoeJ_wRo4Q8HUKTKofIuZ2SMz6vS0CLncICIArgopjSjW4sLPRgfY4FWhg-j_41PRXcfoxUHJaxc5kwio8aRgTgKFfumhjIiz9OEm1Un5MtYLGKWj4ZGWUWawFDwPxN6KeiBjV6qnCzZVspXMtPe16BC9iN-XdRlNlKJE3rpsDL5JXmbefcyGwpK7MWFresIW0LakKH1Tsk9_BN85Bga04XP693_feDrRXD8rdsOLISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم از جو پشم ریزونی که بازیکنا و هوادارای نروژ بعد بازی رقم زدن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95380" target="_blank">📅 05:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95379">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjIJtEXx2gEktVbDv_l0d3CiB4O3nqpvkg1uE69sC2r_eCTHh0jSLhJ117GjB5EW7Q5ShAfUUh2epKimnGgNmy9KnS1zOoPLAbeYht5LWbwezzmuK31B0-iHFiDP23Kz7FkskQaR1qWKAh5vUjWDd_zeiFli4dD5q_04Zv06xA3uH-aV_fQiMygb7vuRWJpJli_vnWBRSnPPm3nRh88Mb28WFmvEMWsAdXbcsz8Qy66XMK6-xwHMOCdjtwRGvIyzMmYqreb2zTOGf6siORCN7NNrFgh9ZytdSmjdD8CWp3gaHyMbNdtJnArP2trVYErsAYj9eFWIj0X_MxoOQYR5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
ارلینگ هالند در کریر فوتبالی خودش:
⚽️
‏• ۴۱۶ بازی
⚽️
‏• ۳۵۶ گل
🔥
‏• ۶۶ پاس گل
‏۴۲۲ مشارکت در گلزنی در ۴۱۶ بازی!
😒
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95379" target="_blank">📅 05:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95378">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmbiYlDLYi8WOjcf_StzJzLoKx3CocOBc_0YPVB2xyWY8FI6p3NUkqpXzcFfLg3BfMQZ9mpopL_CXdoa6_FeNekwNY_c8-0n5-9iFEruUSJRUc1IyzCo1UaL-nDAYI0vtCLeAALZeOr9uLijGPNn2CUmLNK_yXENqYnvxiEfAvgmsiJf4ODxWcLCrIlBqA1ha-A-g2juSNh7D7qfXpCliup__sOkq2IIhqKHi6iIlAGM8vtpOY_RROKI6QrjPdUHTXJ5nFpDofH9EQRIhTWFx55OZgqbWD8RrJr9AhdT65nKP1R9lyI232PlkfASELEav93vj-J-NbWtXjz9dJ3X6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه L جام‌جهانی پس از پایان هفته دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95378" target="_blank">📅 05:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95377">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVLTZkn0C_3ITka7r1id2--AAtbwVcgpqqdPVRdgilKCgAeua3s0RuJz7wsq_9lttjhzKYmMWNHilAjL2klEryC7hsATbgXr3FX0iFNq3p5Fp4HR88pnjDyIWFiw2_16Y316RNbPq6x3F16w_nBi_ZweBp9SscaplZTK28fSDt6qp_trRKx__XWGGZAy_v3iyuoj3qBp934BQrZ2Gsg9Ys7svi7oSaBymWa5BWpuRxQwQrWC24mqdHqh0bOoWLARFxQN0D6SKhL4VandzniYwNfr4izrfVhjbXblDf1ibM0dFyHvIq74AVqKSSSw6VtkNJPQNdmEZJzH1ro-e2Gg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود وایکینگ‌ها با دبل بچه‌غول
🇳🇴
نروژ 3 -
🇸🇳
سنگال 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95377" target="_blank">📅 05:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95376">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/03c1e0c349.mp4?token=rr8O0-8piGOMdKSdR4NW1Hu6PR0QDz5XEzBKE9N_Ke893xbC3dlNM3jdNCLFJ6iY5FBCjB2FjD4jtofym28ZFHu3cDmpMdPkn9KCllf8auwZ71SXhQrEODO1Qnq9KtE1F4_ndhcdhv0_IE9a75dWJ5Tyt0T6DORjSmBKRmBrS6sz5KNjuxe28Lpbp7iLMpuuD9934CuVc8AkRyzImRvP4kEMwtYM8wB1VvcnQFu8cK8atdVII7vkblvhwyoqZAR69qHdvUR2Rk8-l0N-QjcV0ED39-MCkzG8s1SyjoddsX2r7f-F8AYsbNBZ8aHI33hngYYfx23vJL72rOfhiAyCpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/03c1e0c349.mp4?token=rr8O0-8piGOMdKSdR4NW1Hu6PR0QDz5XEzBKE9N_Ke893xbC3dlNM3jdNCLFJ6iY5FBCjB2FjD4jtofym28ZFHu3cDmpMdPkn9KCllf8auwZ71SXhQrEODO1Qnq9KtE1F4_ndhcdhv0_IE9a75dWJ5Tyt0T6DORjSmBKRmBrS6sz5KNjuxe28Lpbp7iLMpuuD9934CuVc8AkRyzImRvP4kEMwtYM8wB1VvcnQFu8cK8atdVII7vkblvhwyoqZAR69qHdvUR2Rk8-l0N-QjcV0ED39-MCkzG8s1SyjoddsX2r7f-F8AYsbNBZ8aHI33hngYYfx23vJL72rOfhiAyCpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
دبلللللللل سار مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/95376" target="_blank">📅 05:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95375">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سنگال دومیییییییی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95375" target="_blank">📅 05:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95374">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلللللللللللللل</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/95374" target="_blank">📅 05:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95372">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rq7vyw-rrvvFlOigRz7yFeSMyvK2j-brjRgRzVk_PXhsX9nRhi5ya1XfHL5cdzkKmKcjGnZ4XIrM1EV5uhhEgBIQxJHi40YhwFrcU_SveOSjiN_wMZrpb-MHRrFJ0iaeL2l-LPWrCNKA6tCFkPBLtpubPc03XyTEUqHj3CTWcutJwTU_zBFpGpcbxO9FDR2rDoBt4v_cogFqiBYKr8WOsqhePsS3RtRyhbmEE--wQqy1VC68tYTJIQPo930DD8A7MnVvvm1GqftHCWgiTvYUrDqO_Qr3cq3TMKQarXhfMks_T5TO4-Yn5QHQdPApaIoYfZPggsBao7yl1JFQkqlAQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0ZKyMW0FJZd9TC1vifUZAu2zemXcBQJEjoAVqBc2SdOCVNEDK_Y03CapyAqf4bSzLaQDM86qs4U7YlAtl5xbgKUq7VBjbSmjqLpmWh3uXHGSqVcF9HHokMykeehxnh-fjT4rLpg0IqQwsxtEtb3bYEBmJ9TkTW8YkUbn9wslZxwJR98Aedhil9QJwl7cdtV4ZI3v7MdxVah1mfr0U_mMgP8nKpQsgFE50FyLw0opGb5HFjsFx696GMACAeaVUJN-2yznNVYy0Woc_37gyYQ-7ZnXNYwOoAa7DdD0aU7Sv1QU4myvB1Wf0P-TmqBvuFFOb41AtxRta6u781UC1cpuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇿
🇯🇴
ترکیب اردن
⚽️
الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95372" target="_blank">📅 05:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95370">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8wrq-NhoJE2EeXccdmRQlX8UinjxSNgy3lTY150eMJ2mKFyeI6ZSFgphBnCPnPxm5iII-MUqM2o9fLaApJNTcLS0VyyyScZ8b46RkE1CceWLGf41VLgV8u9QLEO_LyoBHOkHTzrGio6F8_hZV9B2A0DWGjAPD61hV-6H7j0GRJAaVAr4INTua3kbAWnsTv5jlOOHqdt3byZDtz1PiwHmyf80_E37z5-no2FO9mV6aK-ko4FtuwGlRwC24RU-QFkUl4tRO5pXUhmindyeuzLzp3epl_zj33Dr39OjnlaVWdB0ViKxvupPxpFpPgGYE0Ut1_nMM77kxisz0Tbcv0M-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FyJx-g0c8SZr9HisXZJqTbB833zyJzCeg0n7ZiAjnmfdOi5x_R6xRnwtM44d7nis78y4J9PS43NkPatjPP2TvKAtMpNFooDG9ZFNrypKbpHMcpl59KQqH0ZJkG8Wn7N8Q2P0MKIc0E4rThTObQKJANu8TCDj0NnALjQSZos9k8YyOMSvkI5VEipYNJpdoGvoztS0EBw4y12o4h2StYMf8UHTxgXkzb_Mbt9nlDaRjPkexr7I0l0awnBGzcC__VeHdEsP849QqMb_g8AsxLcC7P15W7pxOygFVnTy2M8fQi9NwBoaHefEOpHG4hc8lA244doatdWUR6Kgf9JCeLB-AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Haaland x Ødegaard
🇳🇴
💎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95370" target="_blank">📅 05:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95369">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZpUjtlDXMQawFyjYz77u16rH8-1KQuNcTnFMNFRDr0GuYbPqdEp2f6CGcfSzjsRhKjv7hNGN2sm1zWJH854ugXjkBM5hihmEr9vR_f-7DZUPAlAHeL6tNOm55K3Nfxr35g11xv3IfTJlR3XmD_dBp2sl2pUdH3Qw-63FW_YOAzfp-IIBBt5TQP08MSsccF1X87bbVzv91ci1P8-IiM5iuJpJCWDMNW9w7I1SWcChsB7HH8AQYk0rOFYQs50FCKUY3vAZaCzpbw8pb5njDQR-qXnzY_IY-N2-1rMI-Hm9-uO4T90zF62eoPPVkSuO97J_8ohjoy1sXttmzZYEMHtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وسط بحثاتون راجب مسی و امباپه این وایکینگ نروژی خیلی سوسکی تعداد گلاشو به 4 رسوند.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95369" target="_blank">📅 04:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95368">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مندی گلر سنگال مصدوم شد و دیا به جاش اومد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95368" target="_blank">📅 04:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95367">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwKpyB1vGCLSc678Uht2_kGE5vIFsCzyPrOqhBmeZg9fXpGRKNN0nwFOMT5ItKDzbmAoYAtY1I4pEHowV7131skL_BuDzGyqzs-ksBi_J65dcZefpZ_n1bSMAvMEyML16LUiop-D9MGi9SYj7zvh-vqLMnfGzyKlCNpT53XV1o1df2R05mxfF9fizqIxZw_l5KJb32LL75hPzNxxfkU7UK37ciOFLThdnEnDnU1-YocNwqgm51MsfB2hWHQSozryZPY9RjbvSl1U4As4p_jrDZTvE6kqZHFDWMvd2HHAta9D2UXLXPKe4j5HQ7CsFq3Qvb6II79H_zJ-SQFpb5nqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار پشم ریزون ارلینگ هالند در تیم‌ملی نروژ
❤️
🔺
ارلینگ هالند به بهترین گلزن تاریخ تیم‌ملی نروژ در جام جهانی تبدیل شد و در 2 بازی برای تیم ملی نروژ در جام‌جهانی 4 گل زده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95367" target="_blank">📅 04:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95366">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90bf733ce2.mp4?token=VNO83umva_L3ZawCEusYUvrApt55mCBQVPV3YVvpYnTcCyCmUTKTC487FDgrb_de06zP88hyhdOyHhpunCfvZf0N4bHJCNV8TzSfIKLwcd3j03mjuqyB4QHn_IINHpMw93DPVNEzoZPkWdnev26fAjDW5lBBuNHPnJdQw1kwf9xbK108FDjtX65tCHr3VWLGk3WMdh-2DnrsNwu9EW-nykvULXh-ibNvTWJEnP-hqRJ0t0KFSkAap_wAZtLQ3QOqA_To9yaCc_EqC5JQnn5XO8TTm-0RunFjB6EF_I1bZNKZLCX9Lq2dLWS0RBhRU71oEPUHsvlcsoawn2jJulzCBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90bf733ce2.mp4?token=VNO83umva_L3ZawCEusYUvrApt55mCBQVPV3YVvpYnTcCyCmUTKTC487FDgrb_de06zP88hyhdOyHhpunCfvZf0N4bHJCNV8TzSfIKLwcd3j03mjuqyB4QHn_IINHpMw93DPVNEzoZPkWdnev26fAjDW5lBBuNHPnJdQw1kwf9xbK108FDjtX65tCHr3VWLGk3WMdh-2DnrsNwu9EW-nykvULXh-ibNvTWJEnP-hqRJ0t0KFSkAap_wAZtLQ3QOqA_To9yaCc_EqC5JQnn5XO8TTm-0RunFjB6EF_I1bZNKZLCX9Lq2dLWS0RBhRU71oEPUHsvlcsoawn2jJulzCBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
دبل بچه غول مقابل سنگال
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95366" target="_blank">📅 04:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95365">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عجب شب سوپری شده امشب</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95365" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دبلللللل هالند
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95364" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95362">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d459d53d.mp4?token=oZSSxLKgRKc53kweVdKTP2Kgx3ywMsHDpTzLBkJKKD8hSjvUumNGROejSNm2lhKCFAtkiLt-M8YrTzeVhHdeGAHRRlQMOuremVcmKIZjvw46O3Z5MkKjefiydvf8uRK5-qn3BF8moIqjGjzqXn7-52fWhX4OdSVULtjyhoT1PsewsqBz1ErvKe9UFupyW0f-Pt1CYvYcs3-Ezemrz_ejb81QP_tPvoSbi6f3UHdvjjVcKY9r9yG2JPhqX_9ajUxIHKjfijQbra_OiVkQwx8o3sa0rbPkFWVCw8kF7RuWplLA_MDrU-2PdeszaRlC1hJ2IpWAxMc3gbWtNkVydYtf-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d459d53d.mp4?token=oZSSxLKgRKc53kweVdKTP2Kgx3ywMsHDpTzLBkJKKD8hSjvUumNGROejSNm2lhKCFAtkiLt-M8YrTzeVhHdeGAHRRlQMOuremVcmKIZjvw46O3Z5MkKjefiydvf8uRK5-qn3BF8moIqjGjzqXn7-52fWhX4OdSVULtjyhoT1PsewsqBz1ErvKe9UFupyW0f-Pt1CYvYcs3-Ezemrz_ejb81QP_tPvoSbi6f3UHdvjjVcKY9r9yG2JPhqX_9ajUxIHKjfijQbra_OiVkQwx8o3sa0rbPkFWVCw8kF7RuWplLA_MDrU-2PdeszaRlC1hJ2IpWAxMc3gbWtNkVydYtf-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به سنگال توسط پترسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95362" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95361">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxC5sWPTRKF297Brdlmif8N317sr72mOhyrnEhvEmiQPQn2FC-C-t0A6SMjMBYmcaTFlStKb7K1_GbX3GQp_4Zm160O5C28ea43sVaoBwyeseJhUKssP1zsbaYtjCpb30p8zQ8ezEkob2xEJNtfKG5GdDM6ocpGNR9pLYLzD2ZDkQiA4c-QGFW5RiNpM5cc0rvuAd1_RQIRtRgJt7doo2-tYLznzJpG0TaGA6a7Jnh9EPAeanCEbHyIVfHig61udPkAaoqN0wYybB4FCMhgzDOU1FAryu0vC_FHlL6QyGJzjreiy6CZs0AsjXWe0NwYxDmrF7hUaKpJ5CLg3hEUcgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امباپه با جایزه بهترین بازیکن زمین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95361" target="_blank">📅 04:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95360">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzMFvSV_8v2-SSE1eGHC04HSIUkLXqqrBvCU55MO3XMV4we8OrquvQtu7J_EEawa0ggZKhyCvqAihRanFDuMEffkLnt1VEpbZnfUwYQpJ_et0GHG1PXGrvPVH9EO4My6WfP8lHwEJ6PoAaPfOAgBUcLkGLoAsr5xLMMkcSsHZQhBpEcz16dSTl562ewX3I5LQ0M2SbhWw3fMxbjvc-Z0o9LuWjrhNaBARljAlRUQEgB7JiTi0Ye0oLdpGcjVA5nePPiIiQ7jGUDY0Vjb-MwWWA8yAVpijuhMkacPTmtbr9WNTkNjlB0gSjzlTBIQmnfvhjMyHYCyaI6aQwV28XXskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
مثلث توقف ناپذیر فرانسه مقابل عراق:
🔺
امباپه: 2 گل
🔺
دمبله: 1 گل + 1 پاس گل
🔺
اولیسه: 2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95360" target="_blank">📅 04:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95359">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TR24P_blXKb7NvwFckwn9UmOB3h3RePc_5mMWxgzJ4ucDoz0l1IMBYC9TVFEhvHkliyyqIrrNvFedBZG9Q7LiLeXDfehVIpEIQvuoShaYSnWD-9cSuC24DOJadkIq7Y3G2Zsb1Hk0Y4EFaHPDJxhz208rlthG4NhyW2hOcI-fBoKpIiWYG82g3SMYs6nbCvXcEA3kCTDpVIzsT3Lzkqw3KUskNibl7sIRZ5UtkjeUBQTmJb5ZeTWuWSy1_9F84-urSCf6utYiFEFd69fIESE5joVXyRZqaWf6U15swpvIVzbHFekCgAD9IlDGO_Fkoxd9yg-eFOT_MuYtxCoWgqkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیمهای صعود کننده به دور حذفی جام‌جهانی آپدیت شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95359" target="_blank">📅 04:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95358">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48292dcba2.mp4?token=GJMM9D3vMU6Tqr8H8xBx0AHU0Dw2cpPfu8gw-50ztnu28t8itw7Hdz26KYwvhuM90sQFbDQLN6cHbQg_MAsGWAyvvBALuokvSHMN_2yHHpgBqeBckAckuuuspGkrEliPSVefsPjlskYHiHcVqaJZRZR3H76aB6OUzeOY2bK8k9yOHbepxnynnHUD_ePrsq23NQoKcYgilV17TlNOe0UC1iqAukrs-j9jeAbRFD2G8klVq-wTIf_Sls8Ns9Oy6QMhlg6bU5xmaHSt8AzgE0_wzKZL31MlkqOVr863OwT5y7RHEgONgQBbdGMDO2m6l1Yuchfr2VexDJnq4zL9SEN6tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48292dcba2.mp4?token=GJMM9D3vMU6Tqr8H8xBx0AHU0Dw2cpPfu8gw-50ztnu28t8itw7Hdz26KYwvhuM90sQFbDQLN6cHbQg_MAsGWAyvvBALuokvSHMN_2yHHpgBqeBckAckuuuspGkrEliPSVefsPjlskYHiHcVqaJZRZR3H76aB6OUzeOY2bK8k9yOHbepxnynnHUD_ePrsq23NQoKcYgilV17TlNOe0UC1iqAukrs-j9jeAbRFD2G8klVq-wTIf_Sls8Ns9Oy6QMhlg6bU5xmaHSt8AzgE0_wzKZL31MlkqOVr863OwT5y7RHEgONgQBbdGMDO2m6l1Yuchfr2VexDJnq4zL9SEN6tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به سنگال توسط پترسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95358" target="_blank">📅 04:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95357">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdxMG0R-XZcwEGi4s9DQ27KY6CMTLOYn-fxmOJuHupXsLwRLKKd8hqpRc_W-ohMJYuV9kbKcSPkt34Ee0CCyDMgI5LJxuHayCqr5XadjHvPiebgOe-YubTAs6UFyRiXxLE3DjYFroyYGYQuQWstj0gPM0elUSjuIcXtqe5q-C0Z3bn_YntqZUqKBK3HkBqQAY33ocF-d3o50_cTAWoEzqS-vBU7SBrYQjtiWo9_-IjaXB4qb72xCnXB7851Kl8mXYsW4mgF79wJOIrrFuyX1JC2kWr-aixJlsHnsXybWbo3OJN35Xfu1yzk53KZ9LznmPMJR41GzGm23ZoAMp3LX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | جوابیه سریع و خشن به مسی؛ صاعقه‌‌ی اصلی امباپه بود
🇫🇷
فرانسه 3 -
🇮🇶
عراق 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95357" target="_blank">📅 04:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95356">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pxqb2V5OaASkIXc74iEps308ff_tzvAf2aF6QFZnAEeZvSkIRLUqzekj-BnoDxJlwEtFetZ7r_fh-UlkFD-vQ9d3UKjNm7_q0DzteJYR1kbM0zXmNtkpU0EPMN_8QK8lGGDL1Pr2KHp9m3_IZStQ2d5FSAYV-8nkJr0e422nMib4KAQ4gFmkvy3Io-DK2AqnkIbhdaZu5pUMaoM0k1tY27sWjJnymZ5akDLFyaA8IAN9Rji27u0aPbrtXixuxHPufbKe7KxszJDCMZuYs85-Ml4zSUWoI0bKKdPobZRfQaYp2RHCgIT32fCa-DAsYsE5xWKJypLnjXcqMppMO53Vyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از ابتدای فصل ۲۰۲۵/۲۶، اولیسه در بازی‌های باشگاهی و ملی ۳۰ پاس گل داده است
‼️
بیشتر از هر بازیکن دیگری در پنج لیگ معتبر اروپایی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95356" target="_blank">📅 04:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95355">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184c9dec10.mp4?token=C_rlJPxrRT3MRC7-wWdX4QeD2BTsEVPC9wVLugmwCkUJIWMCqui9sbdZCEd7TSoMuThWwXyGtbSkQa0AS_33EPPlGjoeYxQaMr0mdSuamuXq_lQgdvh466tC9m-FG5A306qGbZEiUfidfV4CrA_bD9VUwlD0zesJOFwBPAe0eyPR2QfwOscybOEUg46noyCWh-kGgvqi2d38nDdMyrEnb_AOPeWJfOfyZoSf9sXT9V6zgCNOUZLz5TyTwi1bUdF-SaGlP0sTMDab2GTcFSfWJuCwwBeyFsPxNmTv8Xi32re9dRu-eRgwZj58xioeOgxr_f8NaG3h860qJbjdNRtcCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184c9dec10.mp4?token=C_rlJPxrRT3MRC7-wWdX4QeD2BTsEVPC9wVLugmwCkUJIWMCqui9sbdZCEd7TSoMuThWwXyGtbSkQa0AS_33EPPlGjoeYxQaMr0mdSuamuXq_lQgdvh466tC9m-FG5A306qGbZEiUfidfV4CrA_bD9VUwlD0zesJOFwBPAe0eyPR2QfwOscybOEUg46noyCWh-kGgvqi2d38nDdMyrEnb_AOPeWJfOfyZoSf9sXT9V6zgCNOUZLz5TyTwi1bUdF-SaGlP0sTMDab2GTcFSfWJuCwwBeyFsPxNmTv8Xi32re9dRu-eRgwZj58xioeOgxr_f8NaG3h860qJbjdNRtcCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دمبوز هم به عراق رحم نکرد و اینجوری بهشون تقه زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95355" target="_blank">📅 04:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95354">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3e060451.mp4?token=BBqK4my6-T1g0Q4hpTmmpjU_9sU6BxllOMKgmKKf8_KGpisqMWW7biQZ-SHe3m3q5mQrJqEekyiF6zG3hZ0zXgLrr3Qs-bvaXRPHerO-LkA7fjWA7kyu9pV5KNbkWeHgLrc4TP_hY5U4rTsFlL8dPhZBGxrhnjcVnjzKRaqdLBGH7zPZgeHIaO16g_qPQ1x2lANbkk8WOA44GWnY_pMfrcCkMyR7aeKic03fKEVLQcxbqIvbH7xv4h8N-ylSmbRizmOrJwELtgcK1dv9UaYDvRaBIjiXljWnEgXEHxqfA2_FiZuXH-3WVLK9ig4d619litQH6AYV-muW3iN6E39xOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3e060451.mp4?token=BBqK4my6-T1g0Q4hpTmmpjU_9sU6BxllOMKgmKKf8_KGpisqMWW7biQZ-SHe3m3q5mQrJqEekyiF6zG3hZ0zXgLrr3Qs-bvaXRPHerO-LkA7fjWA7kyu9pV5KNbkWeHgLrc4TP_hY5U4rTsFlL8dPhZBGxrhnjcVnjzKRaqdLBGH7zPZgeHIaO16g_qPQ1x2lANbkk8WOA44GWnY_pMfrcCkMyR7aeKic03fKEVLQcxbqIvbH7xv4h8N-ylSmbRizmOrJwELtgcK1dv9UaYDvRaBIjiXljWnEgXEHxqfA2_FiZuXH-3WVLK9ig4d619litQH6AYV-muW3iN6E39xOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دبل امباپه مقابل عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95354" target="_blank">📅 04:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95353">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
با اعلام داور ، بازی ساعت 3:20 شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/95353" target="_blank">📅 02:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95352">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHdinqkjyF0wDeXAucR0XAl9d9RYT3IfuTtlO3UIebpgZUVvZKa6E91eoHgAQeHKUY5C3v-VH1tpn0guqB26feBtQemWkhgU-g2ri9aIdXrXo6oTTOi_uCfm39EqO73LiSP3UDsYF-4dapAZvpaVGiViNdfgEWxMjJkKQpxNX4KBwy4ijBBfpJsEYJsop0KCIaATW-w8OgPbi1I2eu5Y4nKtH6AVLr3ibKaUNbIQ1MVTtyGBb06v8R8hkDdBCMG_zgos8xdS6D-doFtjLS_n6UNKrneeqFXfzD5W7zeDoBjO-yidlrVs8E7fPuZoal6Qh0K9wrTXc4oZ6pQj2klU6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام داور ، بازی ساعت 3:20 شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95352" target="_blank">📅 02:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95351">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwjMpX157DW9vfYLVwxoa2ZzGriNs_dWg3rZ6R-iLZEkaiJ2MB7OSe98LSieKYe5yFXRKToaE0lp3WecSp-mePdIhEN-1fv0rZAbMc-sTD-ePK8XJgEGjFSTp0Cr6QXnMnrehyXsZH1rHGAsL9HOHQ00Q4lC8XDTkcvJfJgqSpyk6d9e-_2CYzh1EuOxUlytbi3c4gzndFCL08TM8gdUlqgpwixRUmXrJCC4D57CA7DV9RKDpK4w6mfQ0zz_moP_zp_SnpjbfYxnGYCHZbdNAX1JZPt8mdVXao3AOu1ZjeIhTEvTlLSJAui4QaLzYq5axTTuNmepTSqWYQM-FUT7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدو :
خدای من مسی 38 سالشه ؟ من از اون کوچیکتر بودم از فوتبال خداحافظی کردم و وزنم رسید به 120 کیلو، بیاییم اعتراف کنیم که لئو بهترین بازیکن تاریخ فوتباله، همه باید اعتراف کنن، غرور رو بزارید کنار و این جمله رو به زبون بیارید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/95351" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95350">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🏆
#فووووووری
؛ با اعلام فیفا، ادامه بازی عراق و فرانسه ساعت ۰۳:۲۰ به وقت ایران آغاز می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95350" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95349">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95349" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95348">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/At2n5bLwbevlIODy7vLBRdqpzLd1LEmx7fl4i_MQHULl0rTodR1hPeXKaHr9zSm6NZ678kOAuTfo8LyH8NGyReRZzExjCik03BYQlfN2rAk6DeYON1KKFmbXRVXZKBG-xwAhjxpzXAQQrt3QDX23JG1CUX5ZswalgSEOTAk8s5uW85fEltukI849BxD7cXCxGyhoCiuqJFpqzkCEHkdl3b8bk0j3emNEBbUGqU6OMRYkzzAxkHNbouoOCSVqJus_8UUzqiyMTqMjv14hoCf9klneEpVKWQ55iqGgp1Y5PJ0vIWTM-fqU4RCauiODagx_Aui1Te2EBuAyoM2Qp6g2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95348" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95346">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
#فوووووری؛ به گزارش منابع خبری، احتمال لغو بازی و موکول شدن به فردا زیاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95346" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95345">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QraNisGmDO15kY220ZE_ytYzxpTBTgfDW5HtQ3PhIQfMzGkuN7UZwpLvLz8t35IC4nKw9RXRO1ghngoKqiV8Hx53WRKJa0kO5UgHCXcWoEokAf16Y2FTGYYKbOnxDnQr50efHQ-VbqqPUt7wnh59h9bFxv7AmNMrnwP_FDuiTTuQBPB6VXCKmbfFm3_BsLn1uNz4X_DnMvhjA6TmxV_3ChrAlVwhaaN1ZhproxCnjdnzUVouEYASBozs-SN198jdvFEQVygknew6PE0inlmvvN_LeZAl5CMw9V0jrlDumMZdYYtRJCkeQ7fnnHhkH4Baf5ueFV6JNTwOKnEKiZNN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔴
سوزاندن پیراهن آلوارز توسط هواداران اتلتیکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95345" target="_blank">📅 02:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95344">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StR47lTkEmVytvmLax88GiwIvaZzqiiayFfBqbZ7r0ArDCjfPhmz-WTr479KPDbp2EWddoQTm2ZwB5dU9ujMnVSwokeBn_MRZd8AWHcx7FwHq9pfT3b70sVEE5kYN2p0O9YQ6uCmEbkaqZbobdMuONTKwNvLk7XkGf0qWVIr9kot8bTyTrDY-tDKDoeK1zlK26EoQvql62HsvZ7cQVHJ9r_lzO2RdQ5Xlowo_-lcqFLCjaxgXxR7g6RixJXaQa2c0mE6jQUxdCHM-9vZMi7Xe-aLKLHDvCZqLTamsAV4kDJjhqr_Zu7_kbLLfo_LFxvN9eerWhbSTcOSBwavy7wntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇪🇸
❌
تمرینات دقایقی‌پیش اسپانیا بدلیل شرایط جوی بد لغو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95344" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95343">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
تو بازی سنگال - نروژ هم بارون میباره اما فعلا شدید نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95343" target="_blank">📅 02:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95342">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
دوباره صاعقه تو ورزشگاه رخ داده و بازی تاخیر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95342" target="_blank">📅 02:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95341">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
دوباره صاعقه تو ورزشگاه رخ داده و بازی تاخیر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95341" target="_blank">📅 02:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95340">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am5UNt_lpGrR5jy9v5jLmT3pvrmGZTSljKkMtlQSLMEHIqwBBponyIs5i-9ehitNzWu41kG2zEUfb9niKO1xS0HnXPptejnLdFTHTC-diez_33spu7Jg9hwbAFnsP-cgaTVjzqUJSxMa-Xbe3mdk7GvfdSBgQLzZl-n9IS9jnfGruvUBgCmn8Qx00_QS75XIC1SFjl-sUKhwpygJKu9pkhOI-UUpZED_1onKrFk3NEfN2lMUxhpLHy4VuCn5zWOvn4THeDywb8jANR_KZBebWIm5E7oNcxfkBjGBCHewWacssbO_UigB6GuHdgXk5yVdUa0t9vr47xiTLYOgcBj1gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
ترکیب سنگال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/95340" target="_blank">📅 02:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95339">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
لکیپ : بازی حداقل با 50 دقیقه تاخیر شروع میشه، حدودا ساعت دو نیم به وقت ایران بازی شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/95339" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95338">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/95338" target="_blank">📅 02:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtumAJUI1bjU2h_MZejlAYtN9Zvrku4q2RcBULM7SsVqETSRY2nYCO8OWpKhxs7UIi_nifZEfICxGAurDiYqwCdckMpnQwb_VD6qEIgk-GcQUsJQe_1WiUPUPHfQpZcip9Workugf_OYBpfY-lcKP6EujD6uUAoEMNJ5GnAAuyyIT0xJDKwBZlX5qsS5kup1n0ib4J_N41d9nnq6FXg4cgEZ4xCxry1L9N9I7wKA4pDhENJ2YHD3wksYntDkdVlVTPIyPtg7yrUzkiG70lLjRHvIscNlJF43z7IMp_GgEJ3sOCW8CCvgaMGhHE0I4rX8DJutGNbFIxUuviAN47oFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری
؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/95337" target="_blank">📅 02:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95336">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgB_5ThXRsBLK2T-DUU4F5f7HNuHiV0IbnCuUfCTiOR6v6ue20z-ZRiWcazoxQxjEPF5CPIn17ZXxyiftfZDsIn3W09eMNfrnnzcIXW7OvkFvcWhZI14UJfaba9LPD2gLx7EithF5i9pV1tf6PZmpkb_ujavasEMWV0BOUEfXBkmIHYPnuLrpn7lkB7K2NAPz3lu9MCo4FjL7PGI2SokXzL87WRJPThj_UjAk84wRIVg7nJMQs4foiGZOJYd3eV7re_ymiYz8LLqBwlX0x_O682LOfw4cWUqzszvznjcffXBUQ52xEcY11z2FQZdgVCi4PcdDfk0bN3paP6ycfD1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چیپس پنیرو تو استادیومای آمریکا میدن 8 دلار
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95336" target="_blank">📅 02:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95335">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ اتلتیکومادرید با ارائه لایحه‌ای از بارسلونا بدلیل اغوای بازیکن تحت قرارداد به فیفا شکایت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95335" target="_blank">📅 02:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95334">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhMz-_OFH_GhjB-nN5W_CENPFMNbsRLkdL53xfaNU-6DjIhbUsTmiJhAmcrhlNKJ-HimSXTdqoEwn4CoVrwZ02OMWKah9RlsxeIQsawHKQgXtK8y4mWEmUTaBVKcXGuIwKsm8WgRRkuJG5PY69mHWmX_kn2d53oKF5HUh9MjjSD8x3-ssq17NkFojJc9csQKNYcsCwFZYZ_IIDxTSFpJkYl7ADkKcofIYHwKDhhvw2_qyA_qiHdBwMtHcxaJ_EXE1d7xzRwKqWg9r_lZi8bVSl_rf4gIaWo52s8PwN9L6KbCdXyTp6yV31BWPfbz57az7P3vpDpXGWfpDqiCaMloKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
ترکیب سنگال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95334" target="_blank">📅 02:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🏆
نیمه‌دوم بازی عراق و فرانسه حداقل با ۱۵ دقیقه تاخیر آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/95333" target="_blank">📅 01:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95332">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووری؛ باشگاه بارسلونا طی روزهای آینده پیشنهاد جدید ۱۲۰ میلیون یورویی را به اتلتیکومادرید ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/95332" target="_blank">📅 01:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHh2NQVy9vhJ6B-C977ce6VA39rbUBmp293qJkfCz1E3DAWVkYmOSIkSFgaSHb1iO-COwhbatSMmaPnUEeUwxV6QteujfVEfXEZe2afcfnZrmdL_o40LwVGPwWNahuesAbvKpwuo8Ea98a0aXTTrU2ij6E3ud3AX0xkmfHzOEdwfCMSQFY0aHm1PQMO78hJ6kSQriYL2LdzhZ9SGy8GMV1esua52eT07SvjEAybvpw_9LqsQvMY56YJs3vqv5Z9fC5DcTKC15wBfDj_juFSdZECzFbHqxKCeYqjWWFq6_dTKFFfyNjkjFKPw74HL-rWfGQbvias40xmeYj9AzrIa_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرشیو وار:
پنالتی فرانسه در نیمه اول سوخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/95331" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1vuswdoaepjzY5z0rHMZtREshkiaGJAOf69Z3q04ptwKFETj3DPhj6c0V2na-NoXTky7KV0L-shdZFZS7v-_-AitJfdeh1xjFqL1GAj4ijal7GDXKKhrlJFAlxjwrIYKYLMizRKEk2XDEmpfrhm6E27doS24UTrzPUea1LZjp4aKd9vRUN5sLalEdMNrwhNQPsNWW4TY6XjwJz2ZEZBctebOceirK_wqy1jc4x1SATq1Jqy5Cv-iB2Cx6-Lx9LWmmZZMEvcqEdkZZj-Tk2WqluDfLDdGrdMqz6-f24i0vGqiSdDkf4HnIimxk7kjEB9m-dIo45qIUUZcySlLr1HsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووری
؛ باشگاه بارسلونا طی روزهای آینده پیشنهاد جدید ۱۲۰ میلیون یورویی را به اتلتیکومادرید ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/95330" target="_blank">📅 01:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95329">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_YmPsDKNz43zAHTlGIL3mjpvQAdT9VH35q5ThRVJwVYLSK8sZQDf1RAXiVdpV1tVRHxO0I_YXCXm1OtDYH-xXYnoCduQzcsW4Z3NQY_GvWWKBGxUkw8CsM6_GNqJ5McP5z5IOhT9Z7McEvEwFnaslFufcvYrtPcj6vJQOOViOZ64rG0cOvqJ2IfoO_2tSJpHbzDFXgFQ30fgeuvrQlFWww_ezNGOe5d5lVJSZ8WQBfnY4eZs9mXbAkn2sgatlXKNHkqfJgMwXdmMCdnIS62jWBNiuovIApHRKV9_S0H1LLRbuk0fM34V_q867DHk1a66UtH0gQWaQkAEGYf6U00DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
نیمه‌دوم بازی عراق و فرانسه حداقل با ۱۵ دقیقه تاخیر آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/95329" target="_blank">📅 01:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95328">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🔥
🔥
🗞
#فوووووری از رومانو: بارسلونا با آلوارز به توافق شخصی رسیده و اتلتیکو از الان مجبور به مذاکره میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95328" target="_blank">📅 01:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95327">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پایان نیمه اول
🇫🇷
فرانسه 1 -
🇮🇶
عراق 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/95327" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95326">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxSODuoG-_gJ29NkyYUO5XgAnT1ExV8fyUQvOjNMeQEXQYbBSmYm7XUj_jGSYXjV72DeRQgkDY-uruuutIclnvP_QA1m2ByobJ2-5ee1tNabsUTIucqIYlGFxoP8lewkXVwWxRm_Y7Iz3wv8_-tRb0x6EhNkLyOFh5m9sLuQE-SBQsJOuZQ3RInszr8E1AkNWH-9CiuVDCfcYEuKzbyatJVYiOt9Zl-v_PW3QvO8khOxzahsgNlZ7HPVDip6Lz7OxoK3GM3AH1BxwOBQOYRyu0LZPUQSW4pVNHRWo5YWr8tRA8VI13UMsuOhYOOv4rtIAPW13Adtlhi0Wq89z7UUcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارون تو ورزشگاه شدت گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/95326" target="_blank">📅 01:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95325">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWhmxID5uWQ341V-1T0tXLTKYhMWlCjE0Eld_Eo-8nA4fx7ujwAfH0NXkyRx9WeG6sgsPCLhEu0qFDmsGgYvJkHxXGe9ulCyvyIOWaiqlXzBBPsC4PaNXT1OjekfCPwLvXMFvdTaZH0xgCMPEiKkJ6FA04T0ERFxGTz5t1GRG6XaeYmLJ44GluAlEwCwE_vcIryR424y53ObZNvJe1MxfyVyUiGQ7o5Bjfnzkgp7mGYkuIfR3OWSLD_eD11PsFftHMCKUWcpMpt7oZFGTECUHz7jT3RM-w60OMANlu0FNeJ6D_R29EuogAj1z-POoLxGhiwQdC5TMQt0m3Rh8YkrhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکل فوق‌العاده مدافع عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/95325" target="_blank">📅 01:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95324">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ اتلتیکومادرید از خولیان آلوارز به شدت شاکی شده و احتمال داره جریمه سنگینی برای این بازیکن در نظر بگیره. آلوارز اصلا قصدی برای حضور در فصل بعد در مادرید نداره و فقط و فقط میخواد همبازی لامین‌یامال بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/95324" target="_blank">📅 01:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95323">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYUIYQ9aCxgXILFSeIsupOobfAmhdiNjdXSinv0DOAmc6PLwowyWcHydFOF5vrpU4JNHe6N_82XgqDZ5ZA5FzBC5DsoA3jAaKnXYHAcVhNQebzLjM73MSU5zP6oBOvps5qj6M3gAtXR13_kOBRnSmzXyNjvpsn8YiWJg7c2DeE6sUyyZPRe2phiFnCt4hV4ezAa8LQtqmoAVA33agnE_hDzNYbx2ujY14-qniTxam57Ppejzz9hb3k0ts-qlnvpKPq_BJX6PMBKx8lfeI9aAg1-lCZ8Al3LT8oDberwrBeoz-Ps2-RHimaYUusLCSyMw_49oXvTUoftIvNiET9UEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه به جوان‌ترین بازیکن تاریخ جام جهانی تبدیل شد که به ۱۵ گل زده رسیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/95323" target="_blank">📅 01:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95322">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwMVFFoYxQ3Z05SMGAUMiIWe_wzdMgRcfAA6YIU-T1K3FMtvQTU3niOdRnhEE3kMmFuX-5-QKj6ghyLozEOKq0K3vIurPIvoPZLpWQHiwn0TEliloMxZhwtIpVgCKoTCRAjGHLH_fHJRkVeNU_wpolij5YfnnGDmVxPGkkUMLz9lK-jpPwUrVWjNItV2DwWSYwi0EvBmG3pWaieQXCo820uQTKF8XMDPFPIXZF2FOnrgiNzR4iLYf_LhEZWb4yD5y7yJfi5n2XIPXgFWhoHAH-UIFFhHkvFPFziQ0eno-v8bTkSSf8NsnM_bTNuQC-vYT1Ieybt5yG9t7V2klClcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه گلش رو به پدرش که توی جایگاه تماشاگرا بود تقدیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/95322" target="_blank">📅 01:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95321">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9ad943b75.mp4?token=qnthx5wNF_ykq4fIbhniRGDFtnv3vat3UFVu3MQSPhqc9vSWLHhcWay0vVszmgcwLKI44SbbP490us3nn5j6Sk1IBBnw1VRMjC1eZiaTVqjAIw-Krb_gsASiQVpI3Q7ikQwqFgbqgdndD9CKPaGze5NaT0kHAjEx8eEhQTnyHseLyKxMpzcYrKBe7L_uCzWiMVwbuJskYop5Tqpi1N2zqnaiPShYq08qh9PqqJb8TTZIcQaaTiDorgx7VG2iLMA_qQcR6JUCDlP_Yio4TqpeCtOZWP7C6KIjLhcG6ZNBsapce3_-UH4Riy-xB5ZGrtednodjpZOb08dzbgJTh5D2WX8w8RDPBa_psePY6icqIF3J8gN4AcEvLXCE4wIJVVu02BMeOC4oTreebi-hzqzW2tkTPIWACqqgpe0PsBdcP8ZRXWqX1Pvqpnp0_q8gGdXyYBazztFqy3YjxOn5gSgKP0WjikPkXNll1j9h6GHQA47fUzgDFUdVEC3tKALl-gSXMhVhrtcqE6usZBKXswNXH_v8YS7ftYXdsOYwyd79MR2SKqqCfyBQBekFCdlP3ZnTp7Ub265ae3UHkfeVdgSv_fjkW0whTmUvaps_Mzvt8ANVY6VhZ15GLoFNG1a6qrObo2mgMTpne9xo2BoA3T5vfpJx_KLU-4R2VMrruriTUno" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9ad943b75.mp4?token=qnthx5wNF_ykq4fIbhniRGDFtnv3vat3UFVu3MQSPhqc9vSWLHhcWay0vVszmgcwLKI44SbbP490us3nn5j6Sk1IBBnw1VRMjC1eZiaTVqjAIw-Krb_gsASiQVpI3Q7ikQwqFgbqgdndD9CKPaGze5NaT0kHAjEx8eEhQTnyHseLyKxMpzcYrKBe7L_uCzWiMVwbuJskYop5Tqpi1N2zqnaiPShYq08qh9PqqJb8TTZIcQaaTiDorgx7VG2iLMA_qQcR6JUCDlP_Yio4TqpeCtOZWP7C6KIjLhcG6ZNBsapce3_-UH4Riy-xB5ZGrtednodjpZOb08dzbgJTh5D2WX8w8RDPBa_psePY6icqIF3J8gN4AcEvLXCE4wIJVVu02BMeOC4oTreebi-hzqzW2tkTPIWACqqgpe0PsBdcP8ZRXWqX1Pvqpnp0_q8gGdXyYBazztFqy3YjxOn5gSgKP0WjikPkXNll1j9h6GHQA47fUzgDFUdVEC3tKALl-gSXMhVhrtcqE6usZBKXswNXH_v8YS7ftYXdsOYwyd79MR2SKqqCfyBQBekFCdlP3ZnTp7Ub265ae3UHkfeVdgSv_fjkW0whTmUvaps_Mzvt8ANVY6VhZ15GLoFNG1a6qrObo2mgMTpne9xo2BoA3T5vfpJx_KLU-4R2VMrruriTUno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول فرانسه به عراق توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/95321" target="_blank">📅 00:47 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
