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
<img src="https://cdn4.telesco.pe/file/ndtSLrz1COmALWAWEzqQRhSu4IPiVLMHp8zBgunBsh2FfAhH4YdIx5Fw2wUZr4JWQdw_zFXm_Ypvv-VbTmoczi-9PwEQoJ-2j43sk-tdvKdzdA6ysEkDDt8QJR7G9GGJt8DnjpyGHXrDbeWrV5eDEx0SeChFqg6_a9b55KyndRg3TyLYbubHfINyIlrkpzmvKu680ssIWZnumsCbasDiYBw2C2PVhGAz6tQ4mEUZd-dVATMe2WKoaTNEENsNwmojsCSgg9ixByxOBDKzNXZJOvCQEf3078KsjCfF2wEoe_qj9uRMQSLFzVfJd2GoBZX2M6BX-tl7K2WDZf7FENsFkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 601K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 12:21:40</div>
<hr>

<div class="tg-post" id="msg-26597">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE4c4mrzs_9Z2tUD32ogxI5Oe_F9sRVks_63tYzjXparFi531hBA7f_EelRyRBpD-G3CWNdTJ_Kko5NgLOBaOoMgneiL5wRQt2l_fqwDXZ8lRZF6hAPcOLDgBRRQSQNRUOhS2xmL8B7pJ_y4jHsI2tw_7Du3TiRPgF_JgXU5bZqt6ICmfNFJHvqJp4iaEMMy0aeVjdgEhhSyy0-yJb7Dy-w6feeR8D5TYY_AgRRqJ2OuQQvCr2fjtGNI3S_tZkKOx9oYuLyK7mhx6HcxfkWOTQ__35z4gHZnuhoyp5-kF9xCEPlHtNBTRLjbVV1GJ75j-mpauBiu2aL1PqylGE_rYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه‌گاتزتامدعی‌شده که آندره‌آ پیرلو درگیر یک پرونده شرط‌بندی درروسیه‌شده و به احتمال فراوان فدراسیون فوتبال ایتالیا قید توافق با او رو میزنه و روبرتو مانچینی پرافتخار سرمربی آتزوزی میشود.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/26597" target="_blank">📅 12:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26596">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=WH2Y8TC87HDJ1B3-Z2jxLbwGG_eRuqPc07AlIVNtAQXliYfBzweYVm2AUXUzMfi0tecMvIiamSjwrrrjU7Rl8vTVqqi2gAIEpw589ukyQBc6jETRIFTWveLDlPrjMnm8p61pODxEjvfhItlgPM8q7QSBzoNaD93CmfuvnIwb8jaQK_5_aFrpCDszS1xqwik_XPKdta4sVG1elTjfTFPlQdzJSPhawIr-aPyZUMc2c2_Ih1vl4nKC_7fAsb9TS0V6-wv-TB3F9bZhp3BSGvzU_pQCCkUke557t1UQCIBDWRm9RJ9KKYr8L6wgvbrsMDbgQzdpHIvA3ssolSeCrFwzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=WH2Y8TC87HDJ1B3-Z2jxLbwGG_eRuqPc07AlIVNtAQXliYfBzweYVm2AUXUzMfi0tecMvIiamSjwrrrjU7Rl8vTVqqi2gAIEpw589ukyQBc6jETRIFTWveLDlPrjMnm8p61pODxEjvfhItlgPM8q7QSBzoNaD93CmfuvnIwb8jaQK_5_aFrpCDszS1xqwik_XPKdta4sVG1elTjfTFPlQdzJSPhawIr-aPyZUMc2c2_Ih1vl4nKC_7fAsb9TS0V6-wv-TB3F9bZhp3BSGvzU_pQCCkUke557t1UQCIBDWRm9RJ9KKYr8L6wgvbrsMDbgQzdpHIvA3ssolSeCrFwzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از تمام‌کنندگی محشر لوئیز سوارز فوق ستاره سابق بارسا؛ یکی از بهترین مهاجم‌های تاریخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/26596" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26595">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpUlVK1JRkThEzdcLmr0fZVBxaxria-bNQPo8Pp9ekwYWvrlfTRWj5FyObImCcXOxSsGFFzbjib4knerWEdzpByRzhLnpljVfWvw8bTkiP6v0D2Trg0ReChfdbMxzkexsRtW5TaytH6D1DBxXzRTdDeZwP9ijCVi-EjSmvsza9BDPR3leChiPNKLgih2mQB2JXq4uTyLA4xVECkwxfW7xB5TlD7oTMUXgntW2VJGsM8wKrOr2cBurL1dNPvr_5SJMRJyMPTDyywq_vDf7ZKZBh4dhKKlOamu1_kqHeXONk4JpsJTBLmjRMhkE59uKVfwUZ9BaD7a4RJ8PF3zDja8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رودری اگه به رئال‌مادریدبپیونده؛ احوال‌پرسش با وینیسیوس جونیور در اولین جلسه تمرینی این تیم:
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/26595" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26594">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0k6y_BLrR7a4B3WsePdT3vCMKbNjAZJ7OzzlcxHPj7gHvU6LxxQ4R7zX3FTtdpu0Artw4INBfy5ul-Gg1OEBve6OBUxEAWdgd-5yJ3LToprTT53AGQJ2cPvOkEavAIanXxwCtqtscWPAJ5pkqyU17exUe4OZ5-VdJJObGO3eBbJ28Bsl1L4qHrydmstQL-u_ZOzPUQguPBymqPaBLXHdHhAzrL2f3MBzMCt_qmP-DVB6EEH6VJMH5Qv0fWIo2KWsVKJztApdH4EE4KfJSwdo_GO_mmGJm_cOMetUsWsUIETDWMsSkhurOC6a9j9iGTE9f0VhZe7pU6TGBlLdaznFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/26594" target="_blank">📅 10:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26593">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HslJPvibm3HdxE-aX-pjwEp5-PgaM374jFAe8zFSEUBS9cLn-uIQMRtEYjrtIaGCv3CW74T1zHh3D5l8Dt7q0BdVcS8v0Q4E4LNP8ijSJiMopvEHDQa-LzjzBndYqR_D1j49xNI3C4iKz1HeNoMSei5uZdWf9W8UgLVTthckmEIeffHd2Aw_PRjHOtTO6KNnVtPolv_oBitj1lDWDpvTzq_zTyEOgwyImfbV2sEbf8Vh_QJCbSJja9i2ZiIE5oWBAHr-FEgUBRndgaV9urEfwkCyt6Vp4d7g2tbJ3f9rdFcRfgjTKA6kwuVfu5j1qv8YyQI3hvexDmkC7gsI_x49iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/26593" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26592">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAumU0X3rfvjjN2ECsvyBRhvDItrS59ghaYlx7yuP9sdQvFrJn1b7KnsKHSjcpOKQKeWixPnzcjer_BPqiHg6xZwJOJNAcQb2j4UM-EJ7RiEA95Zmxx7zYLOigTvmC8RQqSs2XkwUe4qDRSTrqHVmoeBb9v7tRfGEBG7IaFjY041SaY0VqTSa90a2FIea57JUzN0No3ZlFFKhcQ_QGQxqKVMZRd3InepyO6Q_hp79vQXpv_RpplecuyRTdK1KeyVjlVsK_Tm6cAKidsEuI1iGW8mVIAmr7YAtKwHiP3DrNogJuaTTjWO6OHbPIufpp6__om3rhM1eEEifmLzgUA68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/26592" target="_blank">📅 10:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26591">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOnZTVqLknV5jGI62p0yFY6ID1GlENPFwDgAvoaNX7XWuMuKyqMeDxLJ2hE1XpWWHcLiinOupy5ZkHtsPn2oR9NPXBGRKLCMISMlH9DBbSJTVE0dz-6wu3Gq4kMxgCD7Bih_WPrYVtr13QwNa3auvTPI6uEhXV4Y9ZSf3xZnhgxWds35ERWHBLhw2SX61c58PBOWWcMClc8QgW8TI0aIGbXhcmbl9ydxvC1I3g_TSojL08quxsbgZbI6YgS_6BM12Gsq7oJqdnCXJNOGRGtaSWqjH37JsVzd_MC6gHayckWLk_xeW5ftB8WsqOSX72WGx6jzQ80QxkRj6USB-Dzudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/26591" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26590">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2PrcwgLo_WqXnvQQifbZW_q8DNkBps1L6j2vaDGSs8RcXqYryAQxhzxczUVq5JIpBF4GosGw5xpgIo6p4OSneRIn-ezKTOYN51soMeyh2mesMph2_X0As68E3UQOFMVBZyRUzbKqnKYDh4zTrpJLRZ4k-fHETZLBhMViUHbZr5sqI-I5mw4nGld-e92EVb3TSoe5AOEN8a54_Sev6lEpjyUm3CYkQtnim16Ip4_QFHucAK-1Yy1Lw0MB5mF496U3jIcc2hr-NcI2ngjB1_L0BZ3UYgsvRa9PX65TejYqH1FOzfj3y8KhUjcTqzxJwkrTOflZdZ7dWZNh0mJ7zJtrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/26590" target="_blank">📅 09:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26589">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXwD3vQJZQAgS4BWc4lmMdzI68eopIKiVDgXFLjFB3UPYIi3yW_KVGmLE-STf8rBc6WB9IxkhzAJgAdHP3ILe5-7gfiXSsk374q0DiS2SciRkI5DXLI6t8ZlBfscNXahbwFmd46l_I23I_ELK4vPCldY_u5L3NKfudQO5YfgdQad9hu6jwjxGju8dB84j1JdonPt50riUKtHb0q0Tczz-wcaGEN2ydScXYlwzkZXQXhG0IfQgONTWj65BUrNa3n-pLEKzuLTOg1TR_QhySCZvqxu-WIHv_JckvB4s1UpTpRwwUY6-XhX-nYoDu3lBQVkCq91iYeetfy-9j1bWmwXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام جوینده در ادامه‌ مصاحبه‌اش گفته که سپهر حیدری تو روابط‌جنسی کم‌کاری کرده و اونجوری که من میخواستم هیچوقت نتونسته من رو ارضا کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/26589" target="_blank">📅 09:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26588">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=jnjYl4_iWO_Pio88DSBKVzGey__kfacrxgS7zCsFiF-S4QT8wjhoaage4nQCu4OE7wqBtSDVBdUq7PYdB6e7A5lVdJjWtnApCBnIk4FC-yzpHz1PQmHEhmZ76RAw1ktGjXdQbxiCA__X7B5Hsh6lPqwkGfuC0IDf8V38PiSZse33T_rK8R30op-RNBxfZ7muJjXpg6lw049e-HZO__xus2esgHtRFDUIVpDmvcYI_XkGiaWCgXB9oVCmvw2Xlf0MKg4BOUSrWneZ8Bv3f7kkV4BL5w5QWbI22pgsF4Vz5s-a32f9gf1hYa-QXWE3e8ZlV9qbX-fktX7ccvYAQ21uCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=jnjYl4_iWO_Pio88DSBKVzGey__kfacrxgS7zCsFiF-S4QT8wjhoaage4nQCu4OE7wqBtSDVBdUq7PYdB6e7A5lVdJjWtnApCBnIk4FC-yzpHz1PQmHEhmZ76RAw1ktGjXdQbxiCA__X7B5Hsh6lPqwkGfuC0IDf8V38PiSZse33T_rK8R30op-RNBxfZ7muJjXpg6lw049e-HZO__xus2esgHtRFDUIVpDmvcYI_XkGiaWCgXB9oVCmvw2Xlf0MKg4BOUSrWneZ8Bv3f7kkV4BL5w5QWbI22pgsF4Vz5s-a32f9gf1hYa-QXWE3e8ZlV9qbX-fktX7ccvYAQ21uCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/26588" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26587">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbhINxONW0QDKsxETHIG9vDTXECNUORd1eZvK0n8ilNcj-wyEvNMCuZ2TitmrJPU19R3BuVcqtjoCR7cPt4Crk3TpaSmwl821RFpODXu38z-DmdANLd33ZfBt3X6nttKN9-ggEGuTWoeN241ooxt7Dne0XwsrLLXogRNwD6-PkdOz705JzTOKSZ9GCYZOw7E-Iu7LOf_PquXVy1tL5UFPHn_iGyer7PTmnZxydCnj9CXB2YCtcXnCQBmvlITOrJHMmQDxZ4wARr_9_VkMfvuS3i3xgudBAjjMkEKzZjolRkL4DfxNUPLlwe5B6cWnVzZbtNSjoW6otSUqmH0GwmlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جالب عملکرد رامین رضاییان و یکی از مدعیان توپ طلا درکنار کین و دمبله در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/26587" target="_blank">📅 09:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26585">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NC8sytmJ50R8xHgxZJSgm6fF2I5CMkLxXc0wOKRX4BvfJKMIFHDiWEO9JGa5VNgpkC2GMGfesbWVTR6kv1a3O6yem-IK977nr8xrX7c-CFpQDrlGkz16YGUklJ6EI_-MerMvn6CwC_y3QlcUSfIDrvoVk2Aaacpm3bnZseHW6yl1rZdhz2kfEuQZ5zLthWPu-KZCjOtaKNuGzkA1ii-JMuvBaA-usaxN2AM1ISMXMdKFk3X0Yr3642bPSOdba-VJeIH7T2AGocJyLb7qtlrdXXzVB2MMLow76ZWdNYruxe_9ow8KEIdeU_YdALijz4zBLr4xjVWT7819jt6Eta4XIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uldlrB74jdpp8f5Y62cKooY_pLmHsTW4m9Z0qyCXxefpBf7RaLFLfsdGnZin33csC9a4vMxsiQR_Oa3isQozeH3-6LNXy5qLeoiLfBxKM9pK_kWGkahb8Gjmty7godesuJGULlPuHz42_Tj_FQtv70xF8vkFwyRtui06im-S9wyuSN8Q0Wzd8p1OMIVQcCCv3wkcQVvAZKKKFbQELslNHfKdBQ3_RaK0fE80TMbDijqYe7HRrDCsDchTaa36-cxpDqpTRQpolsA_aTi-s7jFZa6SU8r15Bf6OgKbeNHP_Obm1JApbznzeOv1u6hXM-8M8GS-WWFmwwd-UraYCiqzPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/26585" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCD0Xd8yhvxTAPvNwu4IZC_NmDEvmxSq8ecCdw7kEujYODtaeQ6zMRKygbQYIhu2L5i4lBjwe_85J4mv8pWR4W4w0emT1g-IzmWRjG0Oydua_OjYRzmtc0kQFPjCJgP7AVH2ITEz3s7gfE4327NgBapAvNecLSPq_u06iAK3nNz_eH8twTxzZ59RKh42baknxThyNvhcBBxrd3NgZJcnUie2RCsR7nTqfGryqg02SDpOkS5hJ5DkIoZAuMI0xTGn6WxL_1R06p0HEPFav4_IQYHpylbRr2d61dSgJsGS1C50USA6VWlYRG83rTR0UojSy70pN2ScArlE7wJRttmd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y84w1ypiH9bDgdGr7nZLa-5QoVo1kgfEyU5k5N5f_GpHy7bQNYwK9rN6fEqntxM6hiiljGgCDI3DD0z621_pPuAts4Bbz4oCPMVXjmnBSE8i_yi9rGtKXsCmlycZO3x67Xa9sz5DzheFQ_7EFPbQrNjbvc9ewL6bIs6EMNVdpI_fAK6k7qac81ARyE7VWClND53cjCGbTantTkfZolS0IO365PJzE1Rq1PunJPVXTBY6Ml2Ol5oa2v7ZCrPsC66jl06psS_TBo1lteixQNOg3b-4TKB93q6FrAZ5tWeoceoNNK4i_6EMvCtW9Y5CbRDxTSEkwYmNQOlZoN2Ah8v54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1tNPGw1lFqIqi4dHtxAVhY7hGhq5o2f-ZjkEJKsskvX27yjIt1uTAorD9GrMJhXE4BcNSZWbE-0kE6shLHBmiN-VIDsKQSBfMQZlAi9X894gYuu_lyMmBt2vP9np5cOcF17IGJ2iLPejdX_hqZix6m_OeE9Mxle52Z6pCEGjroYQG--DGiLU4aQrhG2fqDw4i0SiIRFhgO7KiRQfX3ckfVHUveExxo0SD0CS6xz7iBLGRNCYLhawTJdQIANLeGIDW1GKYwBAB5_uyf8o-1VYnT4NhcFXuvjOJDYBbiJwEiDHSpV9K-k33zfkmYaM15RZOqJuHUt654o-T0A_aUFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cThRrhtJfJZcDg6P-4T7xXjJHacK2GHjDP1XIWT_qmj4ejfpZch2hdhTjrN9E2_mw0rrEBTYmdOLZqLrPcgpTR_0_Zs2bAKg3LLQvZBJcE0FbVej2bjQnPQMQrkwS3qNKikbjZ8vZSKCA0-o3q19C6VGbPssnCxtatDoLT8M7IFNnVKO8y3T6SHjJ9-_5lyeY8UkyE-gDGY1PIXRguqDm7boiQHHUNlHgbdU7i8EygZq6jMNHuAKKsTI_mnu48DOd8DXQ0a8U0ZqFptbJtQBhNzh6pNxdkBzU_XqdR0vBIMFK2FUkma9iUGKNrCPDT_J58qPu8FKUg4aynQwlybEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WERtbrd2RhFf6A9sDJHL0voPuVgtHSu1fCOM_q4174IqZI6M3rb-xlMJJUFybN1g1Ac82EvnOVSeS0zUnAWSzHvfgPigQLkwWctvRgqAF_LNzmEzGQnx2jMh_Upr1fcd5dajTS8cUrvgFZkNrxfg9H1_0pL3Xz0U1YubBMlWrXrO3Dhc5l-HX986hKogcyAMFe0utaRyRnh8FXf_EfoeXmQi6aWiKBmK2G31PH8yFdanze--01qdxXGcBrCs090PLDRCM6kDiW3MOUcVjqSuXZY1TdW4yu9nZ-zFxKGAMI7cLa6Jt0gv80pn6YN4GdMLeIGbKreORO_pawwloZbZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdD4-cWDITfS-FRe-AtfjsfEf5SVqxOOHGksCn7BGz6p-OQ-724LmOL7k07BrVnomp2LpGfE-yqOoPJZw_biIxFAS47uyNyr1a74_zX8urtHxdvzMxGdw7O8Z7TNrZ_pQE2Pbf7hALqFWoupl6k42jPXw-Pt4UqjptTK0PtndnA0AgngAwHc2pmJjtrTArHtGYRjiB9RYiV52DtdFWWKRyqlWM4__X8taDR0y1OqIyAqX9evsGwCdDprCIutU02WQ7F7y-f3dzRyTA2vrcDsT8bWNDo8GuSdOKtV04J9yr1w0qczOO4xAiT3ZRpIfQk-JI8tAQ_ovp4RrkhMxBzJKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26577">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKwevw1H-CkknGUWOqtfn-aQ5bT5s6fllVvhFAN11d0hzENx83OqTpTEmoa40E6X83oOdV9XkmjyN0Yp1Jqvxa5C000CMcfUkdd1ia3f9hzVOHf5FzyQGQ9w-LrGw4nsqSCzlDbiaxiob7sEfet6lZSUUCr9FFmWB1RByZIZXj3mt7F1w7lknkfEkAKRiL7_tfm3EzSSTtW38pAZtY-xgC2U7tqC1xV2E-93WgjVIGInI_nm0Ejgg3B3QVMvmhnVZfF0jFrZnKdWgED7Bs0rxTGIk0hmsP2aDS45836xE4AGuAdSk7ealfReHPcUn5IZasZjjqpUMvYc233D36d0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇮🇷
محمد قربانی ستاره ایرانی الوحده امارات: رقم‌رضایت‌نامه‌من 2 میلیون‌دلار تعیین شده. تا جایی که اطلاع‌دارم 3 باشگاه لیگ برتری به دنبال جذب من هستند. خودم‌علاقه دارم‌جایی‌برم‌که فرصت بازی بهم برسه. تکلیفم ظرف یک هفته اینده مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26577" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26576">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=ge755alZYJgBb5OHgyVcNKs-1Dgg5NUEEhhNm568qPFzMmDusXloeQGZcVg13nBcuxsVbMFV-yBSdGYR6F2dNJMb7n_PUr29k51Bma780s0D-np1XS-a2wmDMDh94iRYF7wRlDraW7Cite3ot-T-sB0s9q4uzsYDVKrY8j3qqDbFObZ8kc6pfFRqW1a8icmKEapI_gSlVQZ97u1g7pZwtrLMXBKA-ZTUYL7oEXfQG_ttGhjC_c-wyfK9jjTJb2nTzXz9YBWalVcFeYRd-lzwHCkrrjAja6rcxaXNUZZ5U4rPhyPKe1tiI6fBTYAteu3OPWaLqyqpU-gvxwGrmHMJFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=ge755alZYJgBb5OHgyVcNKs-1Dgg5NUEEhhNm568qPFzMmDusXloeQGZcVg13nBcuxsVbMFV-yBSdGYR6F2dNJMb7n_PUr29k51Bma780s0D-np1XS-a2wmDMDh94iRYF7wRlDraW7Cite3ot-T-sB0s9q4uzsYDVKrY8j3qqDbFObZ8kc6pfFRqW1a8icmKEapI_gSlVQZ97u1g7pZwtrLMXBKA-ZTUYL7oEXfQG_ttGhjC_c-wyfK9jjTJb2nTzXz9YBWalVcFeYRd-lzwHCkrrjAja6rcxaXNUZZ5U4rPhyPKe1tiI6fBTYAteu3OPWaLqyqpU-gvxwGrmHMJFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه نزنی ما احمد گوهری رو میاریم به جات!</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn5rHbb2iDJYtqEZsWL1Wi24oFbVUXj8w6pNjwpZaTUmnMCn0kZD9U7LDolPVgLL2r3MFkRRUQnD-pCij89W-4Mclktzq9O3hD-o8vU4fvcLnFryF_uoy9DTNd1jjTwT_utquwlNBUIfoBrTXGBBfCG9M6Ld0euvGnAGcjaW2FgzpFFK4B-tg-IinjkCztwIlyUSoJ5rUguP4XRyZJ4Dg86ccaGL0kaHK-J2b62qwQRYhzahYGcazQe6ajQ8bFRbVrabB1fzXP8BFUxBgr9oOnW0K2pdTLLm-0UNgUwnMwo7nzGeH2V2GrHc84LMp6jLaEyIl-yPfRPppR7aKe-rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhEHM7pxoBmg-k8u12Uxo3Uimsw-86XV_ZBKTriqzD14H-Z1vt55PT__RPpjIyYXcsc15ZUx2Ce185hoCo-yr8ThoK-Qnm0NGUbabarr6ycE_EwjsN1OlLRJGSCxGELOS9C2jKViheBO_bRkLl_MN3xEn1kXENngDC1xMCJw0rPVQC_aDi4kH2Oz3P8VOx10Bngo1xHVBaAhWzNelNTGFQmbRJ8Sm0fqMxUmZpETsX9PpQ4e7sOrq93DmodUT70dv5LN9Wtlg_Anf4voGF3rW1P5F81HtqkpAbjrNMLLG6qBosYBXVVWSxetknqTOCTKe1zPsJXexotglNCGOfQdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgcfWqFQGCeTroBY2gUDtGkBWlJI0hQgOoZwfGRLRpAMbaFsVSrvrdXaboRJTLimRutZLpAm43RFcmdX6kjWrcRRUtkjJtHJUnPv0fVupZ1RrTyu6sDXeg5Ey2FaZefNaUS638OKiFmfP6syWuWinxtAOGvy2uyiPK35bgllymWONJniperCCQQYxE8UkUlpJGUr6MOi_sBQm57Qso6O31NoD0p-I8REbxlSxTHImuL-wFTuOwylZBRqKl0XblJLy5U2Eb4ohuMLdM_eL2mCX_R-ItRS39HTr6VlO7ggFkGJ7Foe-ybvqNyJkXFr8J04IbqQTu_JTGrMgzzwvkxQtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxlERwWXMOLRw6poPo7RkUNwFlZrsp-kmMY6Cr_PdubSUOvDezPsn304pf2-jX2zg0H-4V1JS0-N_MYkweeQZ255ekJ1caBh7nrtgmAdUrlTS73TzMQGAl1IHdYk1KGSRBO8awzSEeY3M0Rt835qbfcJyJpHmZpUgsQg1G56_2dG87gMSetH9UitU3WaWEtkWBpQ2FNZtlxwH9y33oHTxgMavJAgVVeR-p9YjUF5H_oeIct3digvNrSx4GfN0NBHuV08vNwPril-HSG1lczUqFTpy48hxxVY6MBPqino_7WP1ewn4j60OLKCV5rIZn5xeC7_CAmboa_CqI30NIK5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk7Kj0l7oClhiOpVGMlkxH207lk4JoBaKoVlx1rddOvLr7kb63ifQUSctqU-uF7BHFW1EiPr-2uUczM6OeTW2xqkgyBWb_9J7dPUvYjUzXPR6ehsLlejQ7J1lGp-vEKmAAc5035-m_OigSkEoRQo3FwzFUoYGZRE4RO_axEImOLpV3xbA1YCdExjvZF8oGAXXU_dhlyyQTlJ7HOwwpaNNqezH_WPYMZrHpbVPhVPEcynSMDfREoAemaFI58W31WqeEcwRTclIb0grSiDKDkFcir4vE-zDNhnGW_grH9bIfL08xnXq1ooVYKMU1gaCmyLz5VK3SAwT-i-eccngX3wKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESAs00E-Znjy0hFzkf9tMGPklVqqUjYrqIlqh9hfwjXoZTiZQ4ffLCys5lMQ2dZmOnIh0cODD_BbXKQbeRzlSD7bNrx2C6ZoWa5Eladk4YMdVonarKt3JT4sY7ZyAEvCQPUnLVcR17gdsFfo-NqyeetKY2ta6d6QEAB0pCosRtWpXo8_KBjrPwybuKedewzPO3QODJ7Y4BiIMtcjfwgBabX5y0lDdhLwgGYvfaiVvK-vEy8qRnXCNRXq4uHtWGqJBV7dYVGs4m8KXwsRXRipxo97QlmaQkWjMwALMqtR8ko4643H_nxO2Gzty2LSIeY0ax7-bt5KMRspIb-c_BLfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDZFyFhLC7ZMyUfwXZl-QJhJTcgoz4tOGdOJX7WmAiLYSbzbr38eu96yRNvy6gWqyBA50VEKNp0Aa3SWkNZniohhqDUXIlXdk9H4VWvC0qJtX2nBms7qZCEwj76CiWfHwG-wuFIBvWLlg7I7QX-PI99rBFw0AvPj2RB106pPzVmExqp2euCmegUEJFuYLL5SuqyU31Puia22kk-ldPolwMvQWUoJMdEGTgslrkJaT6XNb63CMPL7vGLFZ7MZJ5p0tZvSfAep3Lt-lmu2X1O2_vTqlIHjrYRoW2MZJuKe3R5_MJy768hoScUGjrHUhHQFvvKE85IZgIut_yKbFzhHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKfARVaPzLqcYz9YwjHm-qpyiFyFp1xAenj9ZCscACUM2ua3AzGSu4IICvf002d5KhI3fmuZFrICbazASxLeREznPqvhEw50acdGRQYiADwAhjFxpDMgLEOId_c5MbExDoMQeMUBIu46Pa7FeUBUmtBPNDTxHsMoDoGB1wtwKHkLWVByHab_eXTgzsXVYGvxUjBQmkdt0kAPwdTVh0ytyHLEgBz-9xCqdOrX56RCDC-6WSKEHKaZ24VSIyYNR617ileSH2enPh9ir6eqe_7n1Mqw1xJ9kbgtVZtPNMreOawtiLvPpRbpqQlxdqlZlv6yEAmwvBWrixHhtTfUx-GVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeNwsgZOLMfrBt445WVvWRPgyJq3GogCTiyhmDiekcksCR2iTqlE8NrskKLF6JXuCpwMpkRkHXNvVoQINvHolLRb6t4ToWG7dXDQKmqKzySp6HkbaUAK5M6JtKtVedVTRYB6Yh7G574HiRXoXc7LEeVZSkjihbx4r0-p6JZQBn8prfdsJ8jySTaxpLt5Z8AFMgFkGtb8EqeERbFSueIjS3Jz-FkcFr9CnfbXGMZrRrB6LMx8HfkHt4cBvBW2XHbsKwfAjwrxewqsOFMpewu7WiQhfq14OCcR81LIOYn1yNcS5dnFMVctdNrtHLM1qu6MJIWm3B4tr0-4YBpXskrqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26564">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q834MzQ35G-9lP_SOq3moH1ESfiZKQyg_nJ8dxP6nG0_z7qLwrpTtTMlzTTURwMzM3PmUxzETAjGTsQUStngGUpyLWiCdzgaK1v_3rfxIzG3elNF5ww8UDR6wnUmOJWmHQy5LaIfFRho-kwc93v0bY9QaPqiS7Ri89fZLWie-e7gFv-a0NwFZ6BSPv3IQE4AkU_0QzVZtkAHF9R_atKuIrSoFXNzMmQUeAYqwjd6z0LjBqmnfxz_L1kpq0GbH5BvYcT1zDycEazyOnk4qtd04d1eG4Bgnq_DWMlxUGsbsnnthbAdKnfIw87Cp830Vywf4ZgbgGGI8bOvzfkrR85nwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26563">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=aKRXEQhdYPb07WsgD9IQDh8deMBiGACvpJJGHrh7GxyUwQMEXQkM-OC-UCmk5yR1qzHvdDyq3d_Ix1zOz9U-hFL9Y910OyB7EmD7MTqueWBYBWzWx4eaY88CdXc55IKDemkM6wY4tj1vfCOTRRIgR566gRhYd-GTNazgGKXEazn6lpd-LCF5ztt8BxtQegxT_YhBUQPZyJyNPZtdb-5tmmSO62GYbUky2Onp3eLj6tiTcNTIfX_r229_ghFuj5omwtr6R9JWqBK7znLARTpHSYgFB9-1Xdhrk5X6lCLrx34q6vhVzKrNWgbgZ4ucaFCHAOO5Leod0ZzyrxxlNAW_Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=aKRXEQhdYPb07WsgD9IQDh8deMBiGACvpJJGHrh7GxyUwQMEXQkM-OC-UCmk5yR1qzHvdDyq3d_Ix1zOz9U-hFL9Y910OyB7EmD7MTqueWBYBWzWx4eaY88CdXc55IKDemkM6wY4tj1vfCOTRRIgR566gRhYd-GTNazgGKXEazn6lpd-LCF5ztt8BxtQegxT_YhBUQPZyJyNPZtdb-5tmmSO62GYbUky2Onp3eLj6tiTcNTIfX_r229_ghFuj5omwtr6R9JWqBK7znLARTpHSYgFB9-1Xdhrk5X6lCLrx34q6vhVzKrNWgbgZ4ucaFCHAOO5Leod0ZzyrxxlNAW_Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4T6wgBc-RIueTeYE2SICWP_cYMvLFxpq3IQYawOlR5FMucvbBqM64yNuEWT5sSZYGfYIZhzMg_4_dUxSWNfInrc-IfpVbCyyYDJlYZ1mY1LZ4AVvAFUMabwOecS5VWirxVm9hh_QWaTn1BE7ibGi74EVn5Kp6WksQHZhlBl4E0sBmpP-yj8Qoiz145uhvGS-2muSMqJVcVHnLrkyCHfyn590BkvF35Sx1u8NI4u6f9gq1NasTVHrmIBKM64rleprbgHCcVZktMWH1Ur0AjRrcOmaEdiVppxi49sZtalTTsMjbmfX3Jt9ibgxA1SSJlPffXecAmu5B5RE3a388jtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=e10WOdqO7x4wi1FwOoU_FgqQSfA339OgHpqvqBDr-nlaj6iIfp7dpyXsuVSmwKOPuvF8j8J_mzyMs8Mwn_KVIn9lvj3lK4mT52Qzxm5BdXDKAvLVoqfNkozEQ2wjArY5i5_zfLOEitoQ6K5k7uJnlwqlJp85-kfnb_jc6s6D3WSkuKELhSNUF-I8G3YOW3rE0IEsyCcDZEC4-8lBHHq4NIa8-Z7Tq8zClUw4jjmNUEcVk_UnhVH0qkJZWVnc1kKvGOJ8OKpcFL4PZiudhxMFsNUj7cIqJexH0D-XfS01NItiVN3B1PoeQ9OHN0gJmR6wrYpEkM7V-VkSGlp4xb85jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=e10WOdqO7x4wi1FwOoU_FgqQSfA339OgHpqvqBDr-nlaj6iIfp7dpyXsuVSmwKOPuvF8j8J_mzyMs8Mwn_KVIn9lvj3lK4mT52Qzxm5BdXDKAvLVoqfNkozEQ2wjArY5i5_zfLOEitoQ6K5k7uJnlwqlJp85-kfnb_jc6s6D3WSkuKELhSNUF-I8G3YOW3rE0IEsyCcDZEC4-8lBHHq4NIa8-Z7Tq8zClUw4jjmNUEcVk_UnhVH0qkJZWVnc1kKvGOJ8OKpcFL4PZiudhxMFsNUj7cIqJexH0D-XfS01NItiVN3B1PoeQ9OHN0gJmR6wrYpEkM7V-VkSGlp4xb85jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEiocLCyJHjqOlvDbylqx0Jvw3QcszY19Fni9jf5VWap8qurqEz0RVMmvIIAkWRn5MeBFwxCnX-K-0rZ6oObz23ZJtXfpWivTLZsJRU89H-3Skdv-T0d3kKWxOowhGIHWjb0RTM4Fp2-QMJ0PFjDIpAI4k7fr6PdlujJ-jLD29HJPceRsEA_PxjfaycozUnSlLoPLdjGKoPEv_P0kEWZsmBckOHkJwSk34glA4GG3aM_pTCxZMQ9SewwRtNO67SSi5dx0suX2WVFoe9vX5WKFVx0iPi9HoRoKW8R6tIbl-s4Ubi52NUZLVcygNY2fihdIl6jvh8Yu7FJKxL2G9v0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj5CKAdE3yuhdm53PFQSAhkmRr0h-i_s7aKCWLmFs9zT9R7fdG9jdxlxGZ8rJ5JA4NZq7BRkzi-VcS3hYwvZXPA2kzlRQWVh1ViPlbY3Niwlq_P_NTwUOj72U58SgJZtj6sFyM_d4IcvUcohDWH-lBbhldy8K3G91WcBouxQDOWOopN-9LKnNtXbE9FtMifeC5HNT-TPayks6KphwWhqsewXamH6JNoHKFqm1Mg8kb6WwieBLzq-k4XbeCXplyDFeg4Bx9YkVGnWp8qZ1B41VPOEOEE4jBRNM6TJmsRQaEqVf0-sYmZmY6QwAuLk1RBkTHuQys-xhiLl6rF5C0ULQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26558">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKq4T1vZSP1je--aJiVhKfRaQfQR7DEhhrRZPmchhLHIs8VRwCuJIpeSbAntHFaEt1tk0ruB6GXh-h10gXetHvmA0ovMzo96dRhPpUthpssIqfm7i8d57d5Oz-INpKiokqUBHVop_sgDt15GUTjj_dPZ2o7v5kZ1cu6gcxKQvtWVgOFEEFYjDgqNQ9YfZhcp4B7lf6tOuX0yPuKO64DNqImDm4yhSlqF2GEmCRgkAOxQDJNDzAU5QYzbGQ4LL72qiDYkn1O3Ke0QRklaNG6ISLZAWn_uc5uQ7P1ursGPGRVdCUop1dnoVZMGqfbOa97QKajG6kTkLT9-N1QHdRwN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛طبق آخرین پیگیری‌ های رسانه پرشیانا؛ محمدرضا اخباری گلر 33 ساله سابق تراکتور و سپاهان تا ساعات آینده قرار داد ارسالی‌ باشگاه‌پرسپولیس روالکترونیکی‌ امضا خواهد کرد و رسما به جمع شاگردان تارتار اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjrIlwwzjYCy-iEpbXe1UdW51TGrbHy8uLuod6Xo9JhYlmBRPuZFNKReO8kl4uXt1ELceVv7vsrJ_sEQS4CfPpOyq0gFSqMmD5Ps0ia2XimAogI34cVEVylrou9Nfp5_-Uyxt1woCK9KOuWK53uhNGEipy1yLr0tPW2CFeNCtGfjP0ArEOk6q5WUsLzU2qIV5R_jx1tQtPPRR05uQfMkmALwB0fbkN2yl1-RqCIJ4ouGRW5TOZLrvUQ15EobCmqAt02E-nFhoKJi4NVwQNH6ET1syUsCm8F8h4-pJWWWgyWXgL07oC1A5xRFVy-nABLabASH5NFmsspUBT4pShCnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iolw8w1yInRPOEsHRPE8oUw3o4sjXqeGXTnzBlwy4jfpIf4meoqaQF6OrxbTNqBi74ykuYJ06lUV7T-TaKVo6eQvFB0oI6Hxx6I4zea3NAoiuhyfZN2XpJ5boe61TUevyNpckeK-80bMYNkCw3aUTmkOroP5SCaBgXRDN3Vxj-TE_0_2w9L1iNXNIRq-I5xR5MwFOeepG20x9A1ioMfEtB3CVGUvljLWd76yhKWzPiSUMdXNhmoMkc-cTa7MIwsoddH8thIFPz9rbASEbftEhiV2fmmtrC24L1NjG7DE1Yf1R6XTRtnhLjeAgseCfQnzyqQ-TfCCzq9ysYMyVde--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puOCMXyVAtQ7QFp8BHu6_EyAO3BO4oztpgx7ZyuNOfuCWhPpyyoL5NpxAUrSoLNLZdWDZCoKsUz0SUCDH7x9CWhS15SMY3xUMJAgwUrfkMFTRafgcFwQbL7s3NIavrBCOXdpbsRtzJ9qgFwaLjJKSccmPWo-NpoTQcZuCUQc3IFbiyg2j1rz-fDMteBjsWXNgquZ6ByeExX39e6qkCfhgB5X0JAdNoUz-CGUcxe200ZFoZ991WQmyOfbAEb9LFKpoX_U-WhkCh0wxowr6-g8ORio6u3N9lNCIuwlXyDob6Plb8CV1rQ7fLvjO-li9-XuV08pc0H9shrZMN3YLBQzmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=eHEcqcOJjBLMKNKNdvdk8DsnNae6WbozAr56f5Nzdt26wkl94uytWbf3tPKAXFAHi5cZvUimVRKX148se-AfqZjrtSsQdiQFTiG9tZ4nWBPoimOAPTQM3LgmrWpGFopSatPBKqPE1goltQ1wxdUXQGI2o1dsrQ4-GDx3hQ8703XPMYDkg3i21M87xPBlXzzwX0hPn5RP13g-F3zA1G7XQL6hpLMJqqiGxqiJL3s5205KDkbsmpTKrWtn1ezh01da_t0aswUAxQwdLnxTj2T2w-evr1eH1wNMAysAbCjGWoPJOs8-9u959oYeKpI_g-Emajot1LfWXZsLqwTzOnGLlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=eHEcqcOJjBLMKNKNdvdk8DsnNae6WbozAr56f5Nzdt26wkl94uytWbf3tPKAXFAHi5cZvUimVRKX148se-AfqZjrtSsQdiQFTiG9tZ4nWBPoimOAPTQM3LgmrWpGFopSatPBKqPE1goltQ1wxdUXQGI2o1dsrQ4-GDx3hQ8703XPMYDkg3i21M87xPBlXzzwX0hPn5RP13g-F3zA1G7XQL6hpLMJqqiGxqiJL3s5205KDkbsmpTKrWtn1ezh01da_t0aswUAxQwdLnxTj2T2w-evr1eH1wNMAysAbCjGWoPJOs8-9u959oYeKpI_g-Emajot1LfWXZsLqwTzOnGLlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFyIg9yz0mLAbJarvskX-v6b0-vGO8fs74pidC0m9FfjRMcbS3PGev05929daig8YJUsFFMnKPmbboHp4TvHGhphGbNNP7DIuPoasoSak-LfpYu07GjCAWAmwn2ug1Vmjxebm6enRy55SEsCitBaMnXbglLqic6nsNwMnd8IPlZyTvpPtfI8ehEpMY5xwmUtBTd_lKBEwsb-hKHnirNhZOwPfTnBrtwSDMm5C4WsjsEVAbsJhkFPY8GgkvDgjFV7f8i0l0vG7FycBLYoZ2_lFYbXPxlhakwNaJnX2ZUHYUyhfZ8xQj4EFrZQ-Bge94iRKfHIo3Jxf3FJpKp6LTG15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=iDL767TKor1mGwVwiziHRqUhiEbNvhUmCQ2dVBVDmgRf73d1bqYr79xCrh8jFmHJvTlr8llbj1CZMHHP6sUYOvnBDEAlg1k3cYMXumyOVRYeu3j-2eWTM7qqkug10F4LA25o45s4CS5KVq-90YrEVGH2JtmKpqecALBGDdrMjq0fguEgOvVErj4hqvV1igqRqJPkwu0xCVgN-5IyUpMjvUu0WvmGArLT6ahRHCs2fCAG4-7q4jdN3S1V7S7ydxWCQs5PHJPsH4-c7AJUE6qMv3SOrltWgU3fc0Dh_VmoEKOQlkgfXZtU5AE19_OBIvvs_Vk3sPxtd6erF8W2egqawG8oHyzSu1uckLRmLnbOHN1wLaM9n14uOm2WJgqFvGheHNuEU_NQnyXYOlxD7fJN1Eww8GR9h4K7mNQMMU8DB1GHZa-jkoljIfwkiyD56nP66TZwYh5-GmWSs-UVK4yjrdh30S8yCMKE_QuQ0KC4gLhimlIkJmMeaQruYF5jYj9YOsYXcWDYv5u7j_OQglYY8A_fKOUWP_nQUfStZwdpuhMKMW5G0gx0EdIBdzendj4JfDFTPA_tz-nOmjhYMY6FHUy5LDIxE7lC4Nz7-hWLCbc0f8Heg2r_sQTz9GtOZRIR2TIgQwcmYJAhQxpE9bCHChJd9M_pBMc59IRbilZDdTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=iDL767TKor1mGwVwiziHRqUhiEbNvhUmCQ2dVBVDmgRf73d1bqYr79xCrh8jFmHJvTlr8llbj1CZMHHP6sUYOvnBDEAlg1k3cYMXumyOVRYeu3j-2eWTM7qqkug10F4LA25o45s4CS5KVq-90YrEVGH2JtmKpqecALBGDdrMjq0fguEgOvVErj4hqvV1igqRqJPkwu0xCVgN-5IyUpMjvUu0WvmGArLT6ahRHCs2fCAG4-7q4jdN3S1V7S7ydxWCQs5PHJPsH4-c7AJUE6qMv3SOrltWgU3fc0Dh_VmoEKOQlkgfXZtU5AE19_OBIvvs_Vk3sPxtd6erF8W2egqawG8oHyzSu1uckLRmLnbOHN1wLaM9n14uOm2WJgqFvGheHNuEU_NQnyXYOlxD7fJN1Eww8GR9h4K7mNQMMU8DB1GHZa-jkoljIfwkiyD56nP66TZwYh5-GmWSs-UVK4yjrdh30S8yCMKE_QuQ0KC4gLhimlIkJmMeaQruYF5jYj9YOsYXcWDYv5u7j_OQglYY8A_fKOUWP_nQUfStZwdpuhMKMW5G0gx0EdIBdzendj4JfDFTPA_tz-nOmjhYMY6FHUy5LDIxE7lC4Nz7-hWLCbc0f8Heg2r_sQTz9GtOZRIR2TIgQwcmYJAhQxpE9bCHChJd9M_pBMc59IRbilZDdTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGZX0le1FOR5-aQbnKO1VO5Sk-PKLE4QoQMU50YJ-nts83Cwjv_9bUGNAm14wR6hLDZxBi5_ev2Z2DpO-QKVazGeteI58d2GeUmvSM_UnvUYolTH-KKAXB5pXRBVn-0GZEmo3IQvH-cEZs4eDOvuG0EkPHjH_qlJu-4DUyMCgdheTiSioKlzWoUzcsBhjlxCbkhfr5_HktJZ54Ob7bd_HCLpcmlaSo7FYnRnVO9J25R04OhUeD4vNi2HS6RlaHznAAifcVmLcW_P4Ub1ZKAAzPpcVwWVxKIxGXCjbpNJl4v2MlM6GLo5XW_epz6AB7lu2hy77WU9cgWa2RMqpclX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbhZR1BoX4-eQjDTnDGLpLLUT00-OdpL3yFrITxTCdkdnQ1zxPIPN4BBGG8HD8JNg0rBAFub-R9L5RCQvoD3njIT2w3FhTlf2u5SplF85YiD5anyJ5nVfddK49Bzl46hq41c7stERfpsb9UQxPTKzAErCVfwSQO--oyV1Zp4cnNYfUpd215N3Dp_w_a_XtS0Oeixz4_Pq6jjMSHLn8Kh9X39X2EqOTSTsBmFGZ4IQipJaPxhvjs2h5neUZ0KH_QH0r2T2WMClG_yI9VElZYMcn63U2tM-na0_5LkQP1xE6ixdPwOv8RAFr_VpDUnB2_PqnV8hxX9kA7H7iqWW6wJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGEZeRrLk7PRNp72zXr2btcaqiO5ailVi0DmCGH0fUsleHKvAVp6uNa4LYfXX1Zy4ik4gPJ16NitE-rXI-xDF29-bZy0FwBQaWJMN7My5lGxAsOhI5JFlIXHHCWO11EmT2ZhMzaDkxKevGFeHaciUMZIHn94qK3I2T-Rl2oF0h-Tp1wZN-OezcsswNEJkhY0BU75GuxeSrD6DrS5LtKSD24UW6zhf28SMdJm_j_Qtx1nNcBIQLGWYg8sG1CIFEWinBDqdXcZuXLyeVAYpnbiIfNyem0PCA_I3L7pWJM71OeZ9jG4k1Pjn4Ww_OWtc8eM8R-Sjr6B-AjCwL3qbAKsnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=XybYBMWXZcgUtuy2xgK-osHJqrlRyKgFGUo9uRpKupt0qy7CE28IiKxnctBBmPUqhedh_XMXL6-TKRuo4J11QD2gSO-B23ykFgxs3mU7qZZ9bbqt0HG4YeVAl57oE1klosH6Us_haTqGU3qJ5Th-tBV_7Ttu3ApwesvzyTZT55aNMCqCs5EVt9Fi4pfUKepGMUcNDy4pUqTnBiRWhIoLkUWxBS-p-QfyylsjRFYaCwLfSjUxbWGssZQzf0XjFmLOHcnYmVbo8N6TF42bBk-R6-vwCXHUyMl_9Lxg8oig6Wd4NDuzpBUtyh_9dRnxRlgPNroGp1uFi1gh3xyNIpE3i5vJaOW7UpiFsRueI9yGHRn5Ioo5dPRi2236NJFuIqruZk97J_X7fHMLTXHf2Jwq1hg1K2QuZKQrvKiDifKmSTHG410e2cWCCpN70EUYNAtoYo12B0xs531T_T8BjAotJjNDSsDgvO11Er5NwsViHKba3XL2BGiQJd-kelScWC_blwIBGYyT-2QhEHrr9BYOVtO-sKXaO9OCe4lYPq0x2HJpxFbrhdf6CzJStXlVrBwpnbywdik2Nn6_1WwC3OdUBZSUa3cpNxO9c3mSNMr2aIfTul4rTuDJNYhWOXeB7XdBiVZ3g12-smRqWYgD5rkIyqgHQc9FaatoQhTPH6L7BuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=XybYBMWXZcgUtuy2xgK-osHJqrlRyKgFGUo9uRpKupt0qy7CE28IiKxnctBBmPUqhedh_XMXL6-TKRuo4J11QD2gSO-B23ykFgxs3mU7qZZ9bbqt0HG4YeVAl57oE1klosH6Us_haTqGU3qJ5Th-tBV_7Ttu3ApwesvzyTZT55aNMCqCs5EVt9Fi4pfUKepGMUcNDy4pUqTnBiRWhIoLkUWxBS-p-QfyylsjRFYaCwLfSjUxbWGssZQzf0XjFmLOHcnYmVbo8N6TF42bBk-R6-vwCXHUyMl_9Lxg8oig6Wd4NDuzpBUtyh_9dRnxRlgPNroGp1uFi1gh3xyNIpE3i5vJaOW7UpiFsRueI9yGHRn5Ioo5dPRi2236NJFuIqruZk97J_X7fHMLTXHf2Jwq1hg1K2QuZKQrvKiDifKmSTHG410e2cWCCpN70EUYNAtoYo12B0xs531T_T8BjAotJjNDSsDgvO11Er5NwsViHKba3XL2BGiQJd-kelScWC_blwIBGYyT-2QhEHrr9BYOVtO-sKXaO9OCe4lYPq0x2HJpxFbrhdf6CzJStXlVrBwpnbywdik2Nn6_1WwC3OdUBZSUa3cpNxO9c3mSNMr2aIfTul4rTuDJNYhWOXeB7XdBiVZ3g12-smRqWYgD5rkIyqgHQc9FaatoQhTPH6L7BuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOVkt5oWbC11Gtq8YwTWAUq3XmCP1D8_VxYhNGsSIAEXYnuta6Dswv0QojwOqGqdw2gOoLkZCOLY6YSNGTKHOaDripBMiAGw87QfaMelVNghDWeZqqAZOFYwqGG3aHaQDUjiUDCCNalLdA6xeNPZtdHyCGlEU9yPfW-6imxMjjWHwmrtfIs3nbitxc45SGFUJ6kGLhdqovFW7fkkO0aPE4ST7plrAJkHO1Z9JMamDX1GuhxRt1Jh6r1mCqJpx_c6SRa5wEJUDahw1O2mpKLFLNthGyLESSAe0clTVtGjuGnAd9VW8jL3oSvG5z4J_HrqjP9i81NfYh1Wf7mnlMg6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g36of68ua5lMn12R2QEpJJfcdDOlHb4evFa_8L8iawR4te7QfV79cHW4ThVM25d60DeY1jT-m4_bOf6pQH9A3xjdTK1UIOHopF3R8FqTycxLR2bni3F8vOX5oyNB0nk4Eb99Q0QpqEEkV8BleoeLazOkdGWMvGTFBxbjnvZH-lCqeQpVHWI2sCOIEhzgnEoMQCa7NXZnvEuXi8eEM6NdXSLxRAYIZqtIRKoJPBTFgBZhcV43ikPvS94tXLnE9utRfu7MYtTlwgmS-qnsR7YjaTTKXFDU5afFcemGwcVscNq5jbXC5TyXLkOdefCO0AXaKodfqqAN-CmFwTN8rlbTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FASUWGNvYl_oCB02AJoVO2SqKjSkASIQiWOlXel2FcfeMAhViXL7YfZ3VYazBgE8LdpkWKXz5xIha7_JvY9BzEymRDv_3AOKrvzLs0eOuiijUtsdbnrdeyTdRUHC2bsmpDjaXVTCTiLu2fCqUUZQOiiJtd2acd_YZpFQgJRdOP1tsdML56OlctGe5gRilYKx5AfMtEb6JZMkwgLGT5Efr8kkok3SO_uYi8qCiz_yGnwJXR1CjwsdjCy_4Wxl8Q_OLMAXMFhkCzW69CHgETFE7u0YNmrkadUQDFO68DkkmIwXF0P7LZDba2Xom23RWpXD9HFk3pXhGSonbw8CKziF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIE-ux6xh627hF1ozUY8vmtQNrdFfIYOPsIuDD5f-I6KOUhGCzJRdNpLkewJ3rNjx1x1yDQXcvWrNGlVwcgsAKPD5Ncxav_FSTNdpjmkUi_0W64s-gJbz78d3vf0yymxgmH_tqBybW9iDhA-WChDYbHZg9L8G4fzwK4cGHi0FHM6P_va-kl9L1c-6eSr80Yc6nMq5QN6o-C_6cujDdF-Ln43pU7oZD0hiuLK29TQI_HY_SzQbQbL_L4UmKkzDZHKNIM0HdA6coEB91E8uCpqmokT7_UOD8VI7CKyT4jUhWWWe0TeS7O3fsx4aaAxmITmX-ps7dAvJKA7gXG3EpHW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRaXj3xPD9di2ZGuOiih6w9cu-XDJ5btZm3oGMMmNR3KyOLmKGRDalkeg_cRgR6YgkqNowBcem183pTcqQaFil-nQ0O4wu3PWlacFkvW-mvvBtl7V9milYE5cSSoPEHl895w9Y8uiWE8RO6eVmGexzFNVCE7x6w3_BltaqAT6VPDSFdJZh8AMvQNzn8RAoh4edfc_Ygs4ZcBk657eyZ_VkzCaKjOYdmdA1z-1ebKlucdObmU1SCiF9PJLQvhR8_cecJEj5OipEfgI8gKsPEo1KDO2YfreWPVWOGJST3lvAx075X9Q8V1mkiZR9G0A5Nvc3WNcDlwaokXKE2DPzdHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=iqMf-fmLwVYYeaw_ttcktT4rC_tasn7a8j4j8itOdzpKjrfPpPzBULDrY8g5tABRFsSlXMIJbQ2h12TrgKdJjlgVwOmdxLf9poF6F5aSzLO7rxHyRdYdXPHLl1X7V0QUMWaii_Jk5pXICPavvFxUU4wFkaNgcH5PmCyRccoQVB0E08G3v1hPPToV2-EGU35TwvoKqOwsAS8efavbWb1anQnmp9SX5XWAp4HJjyDH_S5SiTBbDVf7dnLfZZ0X5y7i2_JS-H_Wrvf_36BYXVPs_8m5hIN_6NNwDBFE0L487Xn4XoJ8lc_XB3lmbtaJ9JrlHFg4lIBTcSwIo_ppGvUuSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=iqMf-fmLwVYYeaw_ttcktT4rC_tasn7a8j4j8itOdzpKjrfPpPzBULDrY8g5tABRFsSlXMIJbQ2h12TrgKdJjlgVwOmdxLf9poF6F5aSzLO7rxHyRdYdXPHLl1X7V0QUMWaii_Jk5pXICPavvFxUU4wFkaNgcH5PmCyRccoQVB0E08G3v1hPPToV2-EGU35TwvoKqOwsAS8efavbWb1anQnmp9SX5XWAp4HJjyDH_S5SiTBbDVf7dnLfZZ0X5y7i2_JS-H_Wrvf_36BYXVPs_8m5hIN_6NNwDBFE0L487Xn4XoJ8lc_XB3lmbtaJ9JrlHFg4lIBTcSwIo_ppGvUuSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnDX84vwDsso9q1WwkOy9hJR6rtASMFRFE1qvrupKSXC3oG0qypg8TUMPSCfVb7Q_FOrbihW1oP1NsRmFBprfsDN_mKo0aXy9nHyDnIxs_2r63F01gBt0pxc0TqWchlZTd0XNOZM9H98FLYD_u0gC5AOYLoDMFMskN6K21B4d02Cune4KtC9gbH0v3j_T_5JVnzvj-KWJnMJPBAp8UxSTpE09ycmXP_DGCjNry9fyCrZFZi-ZaMySjXlPbc_pilWqsdxUKMEjtpMyFRoD1JjsTQ-lYBfgiFGLUr4QLvw0F9qgHtatxomrQxy_Of4dHh22n5DMtVmxo70EYUklCdoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfEKQAEgFcsKZabxiKEM5ZIMuL8QlGHLMT3PfVjG_XiyHZdiOzeDt3iVgfPdq0VhWcwN9oubb8bsZkYwfLrES73TUW5DqW9rszcPmHVoOhYeLwytmfKRVUxARqWdJAyTWsiyV5ybtJeUQDbXBlLPZ6VkM5klHboYwGahpR74OsWJH4zH2QLJ6_zEybdZcGnElXqlqijuIfL9W6MXASMef2OKxFKbykQLw321htFxgzWpSfaT08qh_rTBDcK8DmPygW6Y4CrQc-5WYCWSNm9g9zDo333xxnQ4P1tzmkXQGZn2aIDkIga0kAHVRP0RvCADeK575AFmxkPl2xthMCCRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX9ji10Huc48lOBPaMUOL5s_9U0pFUumgbN-YsoRrmnfZahUe8T0aJW9LwnoJWX7fcUO9aa9oJULZKDbqDS09a_bXE3zPbxjflZjDjNjeMRKwP3yQXGfdyyb74JUTKuA8hBWqDiHVNmWkjzcq2j4VEBBR0KhOTdyqNXSHfLh-VrPp1kTbPssTfKucWxQ3IZZGQbfS9eFelINwEbmPv7Q4h-L5l9c9qJL28JmSx2F9N3KVUisqGpTRPeymU2JZX3yDPxYywQLIS0Enp1oOQ2cbmjLmqhuto0W2OKxKGqhlCcUCUN0GvD3EzTdCaHxDVO5KeEhAzaROgOtl4-SPlufWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKH5hc4u9TlKxbvD1eQvDvPthO-uJkqogOCQV068kfu6N-rvX-G7YdCIV0UrokG0jQ93kPyRm3aka8LJcf_0jKSr8e1XDnnsco0ZavOUuTFTjIZhJWhhRB6e-L7G3q0JWyGa2m7OWXvVgsN3JYr0GVLcK__mILG7Eeyj4nSMyGDyDDAvO8F5JSlpInLZdirjyeTwwZgETI7nV81Olhv1DQ9IWoGBIkSb9F4KvyjDwCW2yMGXkCDHw2H7vadqRkR0C9EXkVCvFkwQEUZDl2jR_QMPGC1P32Ru7uxR-sHkkAu3PlB-tET4CjbkJVYhE_fwqd9Iqbe55QigcT7rCuln4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc2s4IvulcrwCZ4rL5BS91jUEdRRGWFFoHx9mXvQTUnSKPgSzxObX5DnuC_28DQVSg0eIJNKVApy_NFonXBy73RHngJ4g9TTQOt2q9yQOBeEClj8sLzTdS5P0uqxcj1s3xKovJ_b8iSz2zMdwH8HezLAC-Gx8dEsFwtfg_rtB1oozMLP9SzrVSscwuvGnVMNFs6BmydDd5PWkMFUPUrVC_3sLV5fDFHcw2snYsN0wmasUmSaoFLv-BPiRXj8wA2aTZzvlifjdMV7KoztLzU9yNamV94QDSKe4Tb_IyrN7KCWsbR2uCKppTTZpR0tNlmgPjht28vEW7LT5_n3zxzMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=J3EtT5UgzbW6cSsoguuqfa7aVJeV6iPdjhZPiiWSzF8DgXIUb7KHitv_oEIAIiEjqXkobp3o3exKASoPvdtnfGTTZdmxcSr5shWdoiyMDedeh4-BGtZJkhBV3Kl3sbyQHXBIznRQr809Tjt3_w6lOd2muSmkIzxdMMW5QvS-zJUXiIcx6eRNuiPKzFYlqKbtYb3l_LdAwoZAji3mzr4GG8S6DEg4YIfVUdHbHlRNsQoIHWvyLIQoZShgoCzRkGbT6M7c3XKWGLPKzfhVjYSqvDG7fysuivVTFjVicE6CG52SmkL1Lj86gMJzwoKL4NkIfu54m5mvNycDkMgsudECZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=J3EtT5UgzbW6cSsoguuqfa7aVJeV6iPdjhZPiiWSzF8DgXIUb7KHitv_oEIAIiEjqXkobp3o3exKASoPvdtnfGTTZdmxcSr5shWdoiyMDedeh4-BGtZJkhBV3Kl3sbyQHXBIznRQr809Tjt3_w6lOd2muSmkIzxdMMW5QvS-zJUXiIcx6eRNuiPKzFYlqKbtYb3l_LdAwoZAji3mzr4GG8S6DEg4YIfVUdHbHlRNsQoIHWvyLIQoZShgoCzRkGbT6M7c3XKWGLPKzfhVjYSqvDG7fysuivVTFjVicE6CG52SmkL1Lj86gMJzwoKL4NkIfu54m5mvNycDkMgsudECZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO4NnibrJKMLJA37q7DYk3h8IMOXqK-904m47shJlZy7P0RCq-dtupN8YF1zldYYg2NF3bzkdIXG2T4P-BqW9vv9P493lLt8_M0e2hTJ5DYhdeT0QQohQGEUexR5UHou1SFjJtaCD1wtmWcSJc2MdC_y5dbrFTl6hJ5N4cvH9LS2ZlS1hhLrOOo2m5xMX9WEyeNnmZZGsGg3Yd--TR0mMmpMj1ygtnqRm4gXyoyXqTdLYR4QiS_GHctV_LZaKnSJUACxSogaNNHB6Mg_STBxJtPY4zOmO15QwUWENJzWhB9R4iJaT1fDLcCBFOLk8IUc5c4ML9im7Fa1bNlIksLO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFXwHY4HMgFzRorm1LuBgX-wOCDinj04_sWF1xvokSn_nnLAHNOhTJmFE9A5rNcn0xPg69QomCWzkGYsqFqkaAbaaEq0IURtGJZdGaSXNO-SFfjMLiuOO1kY6hWYwm7cuRomrf7PSnvyAOe3Zns9y0JuaWhdABs7wTQfjX_ZFFbG5bXKkXuzjqXNMsjXXonht8Dsny_oAXahSFvtLZwn7JO_lJV_k_d78FlyqtTRdRGDVK8Q4i-Z69DM5MlfsCW0QaWXqljil7PIvPsI1N3j7_eLhodj6bdkzoB-Nn6616hqTsf8XpjLZsTDg3Qz1C3z0XF1vuCy_QjLJ3QaFojT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9vG6hcwmMDmqcwoGn739Fc2HGFj5TxJDZgjB6nUxTI0Km9uIqnZFMlPl5G1kDemrl2Fz9qMKjEDoGZJU7hUvktELbVTFmRGffmJylKDP3SzgTM0gDDbR53BKzcMHj40z0FIoBUnFDN2NeTkbdL4mSeQIIUR8kuaW0vEJlqWkGQefUihkkylqOPKi-cEwe9_4InMHl-On4C9wNA8QnKNAF2_u3Gj0EDPlXjKFGNfV75sAUQhfXAv4MkjoUAOOgv23mLcv0vrBmvTfy0glXTB8s9kLWMyZXPT8jxM83Zy2aYmARqxGTDLY_azDOrcZAt4Q9FNH8yZ23qalloHF_v3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8I69pMEdgIZH0ASEuUSojrM5dnHWNAfZNClKyaRE102fJXbEz6kerAOxEADE4mCSq4hctRAPloSeSC3wGFg6JO4PKLFA4QUv7ZBfQwa0nndhCN9Akt9hgDdZWTsJZnm2-HMiAoMJFN1RVBQ9mJtdpL3KSZ9aPzODx6H5l2xsullmreSnJgPb9cttdtMI7iUP-qIeYexN8-IY0xFTaijvIxjeYa36DnpvXib1AmMGGnSxk-isyXGbQ2ms70OdRUnuFVblfjNR6_w-TsUNI4RyrE93o71xVEXi5IGkAKQXpyVkFGkTwzKszskLTQhAtAQ4F1W_o09jo7rbojU4Gv8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzcnNuCgSIay4buxt6DtX64nSO2j7HiBcyweWPVfU5HyOedD_sHhOMl9NrFISH4WfOkDPBW1OfVDXuBzMgTXefba3iY8dEwYNNWVjOjA76tbHiDNCcQg0zRD99EjbZH5iT22lYe8In493cmNYAl6zyoOETi-TFaYmhQRNKqkx_RKvct05Gbf68KtBpy5oBKET_RuOdft7tuIA-mq2OyMFTO3JwG0Ty6CcCWoC1JYr-OclxhVWLPb6VKhdWxqMedCwQYFbTThOTa8yU83gBxP37KK9NkOeHKWaeoC64rHZVjQ7ZxVwTyjQzNZM4l_5xXRD1ZknO_lJqOHfWxZMczzhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3GJn1ls9BPeODBE4hFWYIz6pjK9Pr0F4iBSBrPTwxLRIXVWoIKQAraAjgExrfC3gtf-ANAiLlyyrkNfShjcJV6JE8oCWEr1XhgNy64Ub2mJSxakCGFa3TSZHbeK5Ir8gGtcMgA8mB69o4H-zwTqjHb9qdQhbEG_r11iv4I18vSArLUkI4f-LRK-MFV7W2F5AplIrk7FnFOLDozmdg7aQ71kgQoMRkKpCqIGwI7WG0UUkN13kxoDT-wWWOF8OuSRmngyR7FAz1Gq-nIdY-A8XNiAouYvu_AezHtBcYYivpxrlX9TzUMa0Vy_GHJi9EU-Oi7FCXGAyk6JJwOFbVaJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=KHd29hZQwViu1UXyRmpmuTeqvcGeVn3mjp3kFSI67_0rDgo_-KaFN3SHZo_CQ04gy9o2XDpjLZ-xXOtvbDt7Wj5s97P62V1ybLDvlCc6C01MTqJGIScHMhAAPAizQSAgdy7oIsa8ginzhS0qlpHVnXghqUr6FIabzCLdEsiwyk6jzoGW1q_1gAbn_gGtWBq_IRQXS4zCX-qwqN4O6dOsonvbjRm84p7w5ugGLnC5laHncB1KdSGt_3yLKEs_O8BXeGyDMwutzkuXSO7O9xuWuXU25uqUFjOK8hrBv8ciG-F_H5Rcivq1ZE9TYoDJ0xGCDT-8YVeLU5LH-B4QwIDea4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=KHd29hZQwViu1UXyRmpmuTeqvcGeVn3mjp3kFSI67_0rDgo_-KaFN3SHZo_CQ04gy9o2XDpjLZ-xXOtvbDt7Wj5s97P62V1ybLDvlCc6C01MTqJGIScHMhAAPAizQSAgdy7oIsa8ginzhS0qlpHVnXghqUr6FIabzCLdEsiwyk6jzoGW1q_1gAbn_gGtWBq_IRQXS4zCX-qwqN4O6dOsonvbjRm84p7w5ugGLnC5laHncB1KdSGt_3yLKEs_O8BXeGyDMwutzkuXSO7O9xuWuXU25uqUFjOK8hrBv8ciG-F_H5Rcivq1ZE9TYoDJ0xGCDT-8YVeLU5LH-B4QwIDea4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzvryLZr-AkV2HtEkRg8QoVI6vUUrMBfPfXSyIPKzntnR_Psukdwww6vNBcxB6BpnZFjoYh96UDTKPP_fnuqBV9xBreEbz0dgZUbQLxhuwJIPAXHgwWIlVpHi-PHhrS_Ty-8Tkcvt4xYaTcbQLavD1c33ZJqnxSQpdVndm5FA7_AEVaPuaY1srvb6bskquQ2bUabdDpwA4rssosYZ7Fi2sTxDJsa7aTDYEWg4enNu3Ymtqv5V1LyemH15IW9umYCpLryuX6A0eNwPgo5qOFmwABfXTospQoG2G3rVF8op8MoXKxW6dy4OxcvqpgF1y7syc48paiJpsUd1veIkk9c6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAM5ZxpRndd1RMrwDZ1i-s_e9hhExASRuHvcYZiSUWRMlSq6qGeCILozwmZX5FidM8mA8L1rGdW5x30zRfpqT8O_MWczM_u4qSgUwuNjvE_xKUFfQDyxQPScV9Ydsa2_spacBg-I-HLW6nZF_j6I3BTBnSciC04M5YdwirBmow6KbcyUicdVIG-XAB61hC06E3xZse-CJVZqHATXwsBAqEAab7L1gQ0ref_Xnvubgs6WTI2nQOKSV1cplGpApzKeU9SeLe96M4NB8sY97jPVEvYKZSEP2qt6snuyo0b__b3beBRV25Z_CfD15uAZ39qXXAvBb3XUTTFksjS6yJczkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atVN0sp2uQQU1NKawzs6G6p1wJAPgDSWXJpSddLigTPGoXoNsnHE8nqUwNExYPRw2umovWgDgXabUv5CHbX6G_1r97cD5gzpLfTiAq3nedciOze_UjvTIGsD_bnam-R3aVlmdP8Wm7c9eG7NofZAJfGCpdgtpDdhtS3Raka-_mDiOJOo4Z9NtoZppMHEh8-_4OtFhPTFe4t0k_ubeUKvQoxIiiAYwxF61fpCEgI8sWPEK4H4-OoUJMxBD8EWxpexXUEvg1zArnfVOFLlvzUiiN94Fai3clsYIsJ1gj5mQ5DOcA68gU0rF0h4DOig3XQsx89-I-OhidaakQFySUO4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPOM2j5yaz3ONBAfA9mHJH2Y962xatck_AX86Vyluos7-gtSKVetJtFCWZT9fzjFje3Q7MER6jq5KG7Z8nCz-rRoJsjX6-cIXerFMCrlA6qvVB17NQvMBMo191oV1gVZ5WFZUMVSj8DoPyxz5mVj1RAH7tMirNlQCC7plxE9c9W51vVWzdn_a6OhwbROP_S7p0J-7AWf3KCFYdK5zkxOXF9j2FgHD8Yf3Biq1F9hra33JU6bpBLZwCm9SQPFpzwz82lwQB0Noj2YKcTlHW3A47Z4OpVSyslImAmT7s4QnJcS0uzjQ2udNdQBIAWqRmDiyHwXUYv6PuYoicM1AUnklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OU6hvG9ALVkvOqNs5xEAQ9zSCfxz3l86Nclwj90u_kD7khhBKCERttEOS_jprQGhCf1kmsvdk1NQUKQO23f04Sjm5FH8g912lme8DaL4zXizC734DiiA1VQ8LStTlOLgfedM-xUYpfVnViVKTxVZZJTLAoClfp1tW07o0U6uuaIVi0_eypo8c9HB88FudGzggO_Pt78E2Y5V5XoQU1eWrH11MPK45vt-0yucW24hZ2rhSENdxBgUby-F_OVC5Zc0TxsntCLFIzEVld7QfFIAYbYkYHdCjd7hBn6zTAsrWDGNo2JSv7XVn9ghtW7ylDof5K6AuyY-_orpL_4Fpe8EdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG5nIXgc_tGjlLWQ7rI2ulx4x3uuiLvvYj20xWThjHT02FvMeoPvdfMqeQEMjQl_mIv_3FCglpars-I3T_nYDKOnADWGIQsKxWKczLCkT17upgFhrtZFp5kYmIuCqrRTrhAUCRsP513lWOGKNmix5OHTYSBNzUWd8Pfe3NKxshssN5s-_AikUWA5pK5ZW0ldvHkCirhQYIAwet617z_9thxSrgHtqvRIRlIAz-_37aZSRxZgvrosAMJpmh7VOTd4j2PzZ1vOvZYW3cXk2WLIXi9nIuctHgGvEd7khFLdfXBkg7pyPr35ZixO0fPKEB6RRR4qG_AkrLlbRIDp-vn9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs2qUon8yDFa37hwFl33MaAP9r6iuLLFlsfR4yQSgmI8uc_Dm8rPb9vz5h8x350yv_qc6xXCvKJtq4t4bifCRCrJ8JYetYI435gPMLDPxWIxUo_3gQnsR2MsC8S3L-Gj9twQfb7WybJ_hwpjAr6MXLMdqjqMAv7n97vxKcAW3O9hzlQGXEoh95rf9ZsL6Y1ULBFvll0W9fkYYjK687V48akn5liPp8a4tp0ilFYMGL4hpKw_I6bqnr-MSycqW7sDDA7_lmgUgyKzkir1bvoLz-QbsizZUKgpuoPlhU5ty3ip34QPTSLfbI23nSXd3IJTWGU14SdhNQASIhkNwQ3NIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpyoTSJLnpt1pN6Rirg3i3-2UDAmL_NXI59BsBrHtxbkAdhEwXa5ueONunU_vsR--ne1kDZ42TtyxT9NtmKFgyNuYpbkRrY8_0E7NS_iDh6vK3NgZADAGJFfq4tSMArZU5N3q2ln7FHbPZlwXmaSL_GJmPBzURnuzBzPH8Eni7oSQhayVFXGDzeKPV6y7xHZwEWgyAsY8YGifeb6jjZIZF8_7151xD65yyczaYPw86rJJacWuyy8nd67j_gr_qlXx6kMjLsK6_ejfpWOEOetXl6NSGRoxOSEVd3hDqtQGy6-fqjZhdMQRUhCYkITf6ZaPW6cMa4XiDISy8Qco-bFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlKqW5Q3Uj2fABl91N2z9D80rzu9Sa8Lms4xOZWnVLSnVuGKBTluQ1mIyXVNp5TSZASMVzsDySpBunzEgnJANprmI6oSdNf1B-Te4icDOJdS-JRsg3K_FMcH2NBmoQJ1d_J8fJysIlW4COSooOJ2hGR7UJzohvzcdcyVlxDfVMHGw9JONCMxhj4KMbtjKhq4htGlmZqtYUs6xm7ntVA-Fq1utDLUppRhry6B3WDdTQrHvFECsc5kqiAxMSluFFqclYfoYiip8FKVr4447U21c7Rjm_xVxpHvL59m1inBK_sqRYd0Xc2qf7PXGUozOnGt8SlZAe8zvdctVBhKBRdCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfTRhG2rlmgAHfBNZzeJlljWlkUHSYuf1C5FId00GzF_3lZfkJHj1j4rUqSmcqIBS3XCh3_eEIEhlkCLaZkiNEN1EW61OC_ZCj-4aGk2x-QPvFLLQi5puyoyWJfDA3BRGvqKsOrsz3vc6AcSFwkfayQ5zos-gcxWQno741HCbXbcJSi1tjuO7pVThc-QFyBK7247H2g3TSKI_QOVUrRBa0UaNXRvUmyMQlFRbMpTN0mF3amPfcgSomkvwJexwkyU_5Izx9xxwG2xYJztJKljPfnZATXHpBlQ8QMlYwOYzQvS_hJWQN8bvPAwzNp0xejJE2WVN4RFszP6KuV_k4ok7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ_jEEMWfc9M2DYBa96t2_Jk0Xps7e8x_sW7zs7BeYESGDYRQOHb6foJwisvD035TBdEQP1uIG3I5-PH2WjVb61_ZApbPi-X-kL94dv6hkA9XUUUZSBJP0zbYhuPa3KsZJ8WTrs1xqJtGpe1_bN5OkFsES-Lduz8urhpB9AMosxrFycChsSV4Zgm8L9umMQUOlMkO_7K0HU-vnM0Kw8zOM4K9opMpxmagO4C0CSFoiKsHQET8MOsSJ9w77W8_6YMpaliSBHsoY3MXczD1oZqCVvMQvwF3TNOxMNkG9tM9pYE-NfivpF-JnAxSbEZZjyPcWgynNGC_cEiXs1BbVLzYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXM3Pyd4Cp1F0KCxBNBC7W5zsCO-JYDDTfExH-GcrQ_gQHekBl1NhoK3F54NIce5G-qI4YIW5I8Aq5dOYUzrpbX4fgQ0I9tRW3dugZRicXFySawKrHX2zyWW2Nrz1jtbq2aj3tWLbotY01zTgMeNAhDAvQt-TifZPD0XAK6QzAQySoFC9jCPjNmdO_qUUYWsrzW9IM4iWQXoEOINijHTKTO7ZUayvZsIJuDKk9vVWd7W5nmk2iIMoSEGpr7VLMxFss1371ftBDYiLSpnrJCwq9GvbaAGNTcqQqnWrIemoloff1YaP0UQDJV8fOMNms5b3dvTXnLtEnrCB93zxwjBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKvE3fsufuOqR7XMDBmz3PRM2xpPjIbKaSQm6tItRafFUar_2jQAvHZlndastSUXcAIAttlH7dzp6Fg5a18sYTkXI6xXV2gI7vtUvJCOaMiMS2UBityoaY2EXxHQLQ69unCZE3_BT2TeFxWXgbL93mHjYAIf7kMSJ-sOhQnWD2VvlXYvVRtxFnHRmG2DTRuNdh4ImzscxGojT8GnfFcu5az11KhJKerQQtnNF2xQeIlgIckgwsgg0A5eJjCqKqyyxqt-Dm_Lsv7ZvWMnNLjKwhTwNC76E8CaPuQqX3GMhflkydT3ca4AIZyLgvzBAkOB_NMnG8rl-iAf_r9tEhG08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laa5cpNOeMOC06EgLKNs-oHJyn38rpKqn7AU93h8N1t_LHpTp8Dv6mCCVmsFck9zzawcdiXms6lsBJx5lL3yln0NmbVTYn7Zl2BxV_DYfTSwvtzIQWA6aRIWRhn9d47_-Mj2eRT8HP_DD7zpd5bIQluhn-38HObfyaTY5FB1tfSLwtUeb1alWplKOGCMLz-GLt81DSJPiMxV5irYvSmWbE66LFukQ59KHAU6f3RZ3U5GANKDKmrmnLu1xgxQe1wn3qcGeK8tE_RdVKk-TfUH6nfcHzI4Vzw_AxXMxTE_FR455fJPvhsWBN-1PGfMXBv8aJOwykX4TniUZTM3MqnKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq4GLXXnErL5GNjJOrNVuiCpzLwzCSoIkYTzEAe4MzI8znGe4zFQdM-K4KUE1V_xAQ_arhm-L7ZyJa6uDCt40H2f3DMvVsp-LEx1UiBkIcSt8OdgaZGdv7p5qVw1jG7I4MfmDoLkJMMMDLHv2c1zAP89qyy0Ow5ngm00b4-1sEXSYWzjpLGPfJkccgWWgjO_9hnMoeDTQ60_dgUZcvaafd0L7lb5Vekc-1UaMwNzt1kaFRMJ_jDM-JcVL8OCzeaTE2fKLfVVrMkIFz_k5ZnvI5Zc9pG8EkI1Px5khvJsaLw2K9HajBWYNSKE-xKxX2Tz32D4Ws96sytnNOe7c0he9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPup79dynF38cbZlflMorQqR1udAkXUYjPicHhdyRCDVbJZSP1FOVogF-5lIgAgEEe8HgAzNpZbHACwGuFpmBqGM3FvFHny6VU3EXAouigm95xKrujMwsyjOXPN8ZheJX5XxGwygBypI0-ByH3Gisb5tRqMyUauxQdaUh6TIhSOrRl_pAOgaAPHgT3W_7FSRJjoM6oKXHzKmFRRX1C66rQC2dvWQhkliezhMyqyXkjj7WkKOpkch___1LCgxKmw9roIx3LVBydQ9IKIryfZnvoY3Jj4VxzEqDa3PjljJiS-yd2AdHbheZAcBW8zR90IcUuCAlnS1AXVcd11nEdAVhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPXow_aH_RMQ-CT6gSttF7dHMBTpVbVzlLCmiRMmHn8qlrsN7jFNknaBJ74iXNplm0C3TiY27xgyaF3zEnq22TPvZUUMN5wb4pI2n2_gMHzpGGQD1p_bujsCPwTC-TgYjMh9gYx5cK_F029jHNJkTlGGgpl6L8-POuj8n6DNagslEiLPsL4rYxVVvcEq7N8iFHIOBAHUAj5fI7amVnFX4xHya_s9ySoP4pIc3dROOI4ISDAPZ9GeIiPy39K09YXViLuVDsOYQRrNNzbCxvoJ2j7AuXPc6R-sBho4mRxLVncyh4d02024mzqdyQE5fcx4uEpBeoYJqp_IsOGVgClkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=kxCsqgRpdDU-mVKboTqHu7GvYTFSrEI80ixISXXJb9ny2Ix3nM-PwMdUJyErrgdNbcD2V9BMdbtjCfB2NjJz8DQYzC8uju-sp09lOI9ie5Z3_fgI7p4KMkp033wEhPGedmFL2NtofWSYWF7bInsWvBrubI7b5Zph0i3c0DYECrAG9y-8_4p1aK-xHWj5oYMzS3ouYAWyyPJP51iq2swE_dcJBfgnxfT854pxN5_x4hgZqqdm4FOjdhN0AWIIlCA3saeeH8VMDAVye7VAn8s8OIEi5b9EVXnp4j2Vf7NDNu_4Dp1IWAGdaUAFls5KOHDmO2j8OGl02bqeJLJb0jHP5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=kxCsqgRpdDU-mVKboTqHu7GvYTFSrEI80ixISXXJb9ny2Ix3nM-PwMdUJyErrgdNbcD2V9BMdbtjCfB2NjJz8DQYzC8uju-sp09lOI9ie5Z3_fgI7p4KMkp033wEhPGedmFL2NtofWSYWF7bInsWvBrubI7b5Zph0i3c0DYECrAG9y-8_4p1aK-xHWj5oYMzS3ouYAWyyPJP51iq2swE_dcJBfgnxfT854pxN5_x4hgZqqdm4FOjdhN0AWIIlCA3saeeH8VMDAVye7VAn8s8OIEi5b9EVXnp4j2Vf7NDNu_4Dp1IWAGdaUAFls5KOHDmO2j8OGl02bqeJLJb0jHP5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5BQSyzhobujPVfIzBRvbSmyMMJAc1_h15si9TON-aZXHK6ZxdfyB_pzNwQci8z_yv7hhrR5CqlTB1unKfAHJqhQO03p4mfNlDX1oLIIfDpbeKvH9d0s9VFVGmrOKh_DS-0VJ2S8qozSrcJBnZra-KESBifQPSOYURDLBt64VZ_Ct2f2UEtlQXbchmQ12kXe8zYMIpv0zlvnePoT4lYzcmOyRJXqnmq43e_yY_9F9OHSvOTTYrRMuOPVPRYwIL-R_r4XpeMyxnwKpwCImjdOcatuINPHQEfFbPDLGASS_VSgYbWaYj4Uf7oyDSFqQAD_JX0B0CuT8C1468irZHypow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhvzQJ6Zbwq2m9dqFzD14Bgd7JRDP1ZSTQNobLNSEJ5WeloSIuCy9Bn0SZ6WBv_n0xIe-kZu3le69uf7_a6M2yv-SKr1Vj0IYaijqrTI2NxU_tma8QPwvF5gqLlsbvOF5uGZh-tNTts8Y9cRPEWclOtz50qfXwCW40jVciz_SKV0ZywShOJ7mEL-uRmp2ozee_SBNsorwKl5IFVFQrATGbpM5VOXTpwlRFD694VYlGwx3JzruyR6ti3hDGsy4fONWfe08ojOFJfxjZPY4jEdmD2eRmWLzzfCxvFvJZ2740SjmU_BUWWbEY_sEoyxgUPWpyRbo6fU1PKU4bT7FHz6Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTFrNKYoepuKeZ3QeVkUmW1HKeMTwYjmqEBdQrGTQcDNHLyMWeGXngr3soiVlYVx-oJjF6aQN7n9ViPT4cqIflJxEFUlthwacKLpPJZNj2QwTzu82dViGN1y0PrQP4Nqqxsq5FSk-A9c7NB8GkUO-dYu9pelYAOdLwAcAd22ocF0wU-hFyME8qgdpBzh4zSPBafG4-Q82Pp5NZe7X0Q9FCpvfnZqtLhPY0gKoXy_MWcAjE62qibbi9XqSieayunnRjaNIFarnpitpJh_3e4LXn4uEriHuMSZnwDc7lXoFVXeNIRD8ZVl9mgiRWXLoojz0Nj6Hwvk_r1UQ3gMICr4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=EY6YfBy-NOL4swjyjUUbwNQ88KUju9_4wWy7BgW53iXRcER7SMSfg4nKbRtGvAkHUUYxFg6ZWe5-1JBB9rMbJELCoSvJFzrpdBY2hIuHKrN2O-COLtxgAKa1y4kOSVHiBs_idUYkS324-yUI6A9-alFzsdSXqZvhHPLip_ri3xU2I_Wfbco2nStVigDqX-asYC7YLirHQkf8m-8iC2n6Jc7kWUlxte9mlY1kvfnya9pUJ08NjULT5elFy0TR8BsFC_xddN05d8r0pCIrUAYR2y2akI4rolSMqzEngaRC_w6kfcb7fWcvVc0HgqOUv0xEqhCCYBnMUhWxikpgVVRYjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=EY6YfBy-NOL4swjyjUUbwNQ88KUju9_4wWy7BgW53iXRcER7SMSfg4nKbRtGvAkHUUYxFg6ZWe5-1JBB9rMbJELCoSvJFzrpdBY2hIuHKrN2O-COLtxgAKa1y4kOSVHiBs_idUYkS324-yUI6A9-alFzsdSXqZvhHPLip_ri3xU2I_Wfbco2nStVigDqX-asYC7YLirHQkf8m-8iC2n6Jc7kWUlxte9mlY1kvfnya9pUJ08NjULT5elFy0TR8BsFC_xddN05d8r0pCIrUAYR2y2akI4rolSMqzEngaRC_w6kfcb7fWcvVc0HgqOUv0xEqhCCYBnMUhWxikpgVVRYjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fu6FvZWmRgsvIPWTRK8ERhie2ufvhvD6WsqRsW_7NnzSVs5-2v14VliiBLeY-J8Ppx446pe48smjNRrYrY1Cx3gNyh62XHUU7XZlSdfOHpC2zeRvkb_biypU6PV5EsQA1dpxupRdq2JzWuACqfv0kGjJmYe8qEcMDqF06GwF7sWwO092Jc0PCX6ZTZcK36fAgn4eXVb6xfKrX7YUgRN6Q6VBNXx4ZwR6CcY_nleOiq2g1-FmcLhYtMeWE9jZJVuTAjOCpMglJCDpx8owhlP_G9FpSDGof4U4Hrvv9qpdw1P7CZuR-6MBGFEy7W75D1safUUVGwDXWliWKklSf58y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=prVqLmfeJXHdDLteMuErW7bvnzH0Tz79i526Ps8ifQbkmSFHQJJoluzG8wlwzhCGpGmrkF520NvM7R4PjEpFhm-neEREtLn_1D_rHFPXCKCv9PdK1D_3hIahrl_htxfJsF-SIgkyHvEqcOA3wb-ias88l3yJ9d0RgpOTp3nHmQVObjy8IE5s-F7b1XE2xhAm3Ocj55AXOkvoblFUazMo8pH2Twz6GqRN_XN6GYvHHpMGCZbidGGdc4zMEMtmd43Q0QdOFY8g9OfV832VmJvlp7Vh-Z45CmrjgFIJ-OssZ6bfNVWWUW87049PyVFammQiZxQt4aDzhbenZgkBchnpcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=prVqLmfeJXHdDLteMuErW7bvnzH0Tz79i526Ps8ifQbkmSFHQJJoluzG8wlwzhCGpGmrkF520NvM7R4PjEpFhm-neEREtLn_1D_rHFPXCKCv9PdK1D_3hIahrl_htxfJsF-SIgkyHvEqcOA3wb-ias88l3yJ9d0RgpOTp3nHmQVObjy8IE5s-F7b1XE2xhAm3Ocj55AXOkvoblFUazMo8pH2Twz6GqRN_XN6GYvHHpMGCZbidGGdc4zMEMtmd43Q0QdOFY8g9OfV832VmJvlp7Vh-Z45CmrjgFIJ-OssZ6bfNVWWUW87049PyVFammQiZxQt4aDzhbenZgkBchnpcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MnXl4N3WHsIE0bZhrOXhdHanzimfebKYRMluk4u95aMfzdt0rX1YpwLfNK7dHShA5DWzRjYncgvoWpgiQFUFN3wANCGnjl7dl2_mOzJbNcsAQOCDxS8v3VAebo_61BKympo4S7Dx0yZxChSFpUusJhvRk9_qc3kHbUsVzd48hXLn0loT7IHJX8Fy8Nfj6PhqSE3Ei7DBYfzyMBMTBmYnWVuhcSqphoMgTur2g8CjMaN0NY66G_wiuy1_8hLn8z-6YqDabdu4rgHDxGpIM0uYECW6gKrG-hjD9yoIti4rc1_W2JDquqMn9hCxipYfVoTeGcNo9dkQwWVSlXeDRN3UbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHklZhEvJT851wZats1r02fwRINyD91QCijiBlJbAWmiTy_XyK2Yf40_SvSd-RWdIDJ6Vcm71pWYFumEdAbrArW1BLvAEkPLi_JcslFqu4AO_Dd3-4yJoTQjeQeuJE_yoLvGIdZ_HVl9OJ46fXmL1zYoEoy4-4GSVkmFqKHxXWaYPqhGyZbmeUM4AKrFywMw8NZL1e5H3nsW-8ASJq3kK1Fcf85QGVVi0gcCXKj2us7bHc5NCjSSVlgYKmkDnYswE55m2UAwVOogGHPONwIhSVGA2FS45BZyaUtqYpX1as_uxOmu1m5qrLmb9IpMwuyM2NUQhpQagOysH_KPI2F8TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6lb689b3cT__W-wkzDSVJ1W6_CQSh4XAV0EOsVOqhM1MeXbn2rPKVlAW80mUqaJzLg0dnTmlvqr9CN3P09f64qXO2ywvyt5A3tICnRBF5lsXXONHG1mtuWTbyfSGu2jM_xUkErWsrX_aWRk-OA4aYes8y1FGaTx2raezKrBG7DoqaHkT9FF66X_fH-U_Bda8NPuHZX1bTvjThiheXmmIYFdOjvEBy_7oBOgwtynJ7W2HpgabcDXbw-ek20kI6v5x2lNqXR_5y4beQT_AZHEYMyigeBs4yc5Iqlv-VJrHHagd5KTCwHRnWT8lbhDjvGFUPQdhEGrDvVrQOLFu7sLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDi2WgA_Mo9knaQf9L2GzSywA825VoVX_gyzAEMMYBsuSQcZejCzW0O53MW578qe579VJmQ466iMwtDYVCxWc9fuYmmpnlv7C6q9-HGKntVhIsf4r-FbZTwiY184FZAredsFzVjFkH6-OM3vK7TdlHbzU23g_oONS6lYIcdg2nTsKHwK8Lc_rLZOiBIA1aDh8cNX2336pUZFQgcPbtg7xwp8EX2Ok2Lq47wPUNzRRZNs0CxAxNdTbACN-Oa5Knvs96mRBfe6LQDKeFWkXAqK_uywGOJ3H95eDYgCxpemXNjqsjyPIiZhK3yuTrIfOI5knL2c8vO7HlMd4qPpm5YWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_RicvUyDgoZ7UK0o9ho7Qzhv6sKhAoYOisigyCwA10J2dOIPRtKJleUUuyQc_qn8J0RQdtYKdz-PkWEeSJjofYg5l585koHuRmlcQnCKpP0pJw1g0UgAV8V1uLq2_ObtiJeZGOqqWFUrv12cVZoRsJV30De_1BgHtyrMdlhAT2Aug0g3Bg852R9igymO8LnDen_6Oq5yLyVl-2BpYZ8J3aJyWpJnDhFhJGd38iEIK2z8TvRrerd20qfM9HJwfgm9aEYe8tRpaZfAVqH3CmFk4vmx7LuR1c7FJ-8ch8IxbPDtRMytosDpVBcVN4xiYK1t-LDFgmnyimkl_v1bwGFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9MA5CDCrXW7Yj91I8_LrLyVz8wovgltD7XsjOrb3x9GbNVUgk6cbGE4UPpmUjSFDgxfGAjeggkITxgJzXoamo5i8OdacUR6nqe2zyem2v6mknQ3DntxWu3AeLOtbDN6XCo_zFcHqPnBStsIWiLj0OZUh9uDLAfLhWXGqdDBXIqHLnSNcrKQKxMEw6tMEJaGXvS1ktxZJn0O5XIlsrTTWB9HKRqYmM9BeT346zDBwUdJKge1IO1cemM1lb3SoVKERU3MTLKvMRd-Ni17Foc6ktyXg2mH5bKp1We2-EY_OzGKqBehBeWEEsDlFz-0cUxFuTm6WLDuhe5MVV7QI_JNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvGmGBgK4jSlUH9lNhU9Gb6ujhcP5X5Pvg3bwcP4H45WxnSyiaRJvwISc5uDs4vtFc70KEsoMn4fMYVPDCYrhQCrrhHndysNb81gLJgMAIhg8Tp8fJFvAilEju4_WRu2avu5rrhXSqB4VKGdxHgLBGzrBIwRCERL2_tSv5VSAJanIvkyj5q1A9qZdxh-esBlbZnIjV9hVd_saS1PU3q-UMYvtumxu5DFyeZSuiGqFqZe3O7POzqTV96vE-oHBPZO6xU3jb9eE-qJ33brXqI5sxHlP9b9htZdGWacb9k2O_IMTem0JCuPPda1KM63Lp7QM6MtMGes6eoulnVqT00Nfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFQjrYIppGQEq1XjyADlIY2_D9C__zmfZ4OZ7lomxJyZHrp9uRZOvt-7yDxfX-0frACqNNOpOdvEIZNaHSOSVRgQjED0Zaz6bRrFB7m4Ywo68mLkBrJBIz9Z7HL29qXWAXQNsrQ6un7uzuKGF_XQ4e630txIYLXfs_x7iWcTSJF0HDOZ-dG9KilvHDW9OW0C6YIlBV7vez87RLFyOyjWUeB3-fZvZSXd972lPuXkZzXWMAPsRJuS0XM6leUaKTR9Iw239WXaoB9ME2Y-FhUiO31VdDeGIPI1vi0alpECPYqUN2NhbkUcLpKgZmy2_oaR55rTuETnEe36f9-TnmRRcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=iBUhc6D5K9JroP-17ntyaPloW-9gHmMsUk2PHIBHkj7lIue-5FQ1cwof6JEG1sBAffrJ0sK3KujFf7plY7ioSAQhQJHmv5_x4LBcw_DWEro0SwIfyvRMN6Wfvz4ZPo_dPBuB0rNbAJijbdC9qqCYvEWEOC5jSp3jOILsPEkaWYX_QLKsIQ75YGfj_sCn0_rGTwGFRcLoCfxSzUZiDxvSYojyabFwMzJJ6xJ76iU0wQ8WjuPuV-JklbbpXGNpjMNEsn7R_SRrNIUqPpbvUIxUEwYHzoi4Cq-TeaC-NeS25p0VFEtHVVkyPtGkc-6UhmHeeiFbveMufibzzHlrXouQyk9nwS_ZxFWyw5Zffh_ZyD4RVb-0ZF60UEsKS5_DlqxU2ahGqDBVFTF_o4lX3pBw2UTuP-d4VlcrtzddcBIDr-iUA3lKcZDBjFgbfXz6ePrY82mSeGnFQt951vBUAdBxkFIxLY9kcDQG--kOT8IAjQW-XC7dEE11dhq-IN0rfzs-AuIzhu0psQS8s8Uh3MfOqC7iaOf-2doxO0IEiz9TjApChAjUZTQ0TUcvS4sacZjlQ6Q6rb7HFq2uMm8HjaNnzXHVr4RX7ANPuI-P4HzeWyyGDwG-ZW7ixjRbEYkz_3dxwO92j1_IyofcTU5qy9MO0syPqs0M5B6WNpiHPfaDKU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=iBUhc6D5K9JroP-17ntyaPloW-9gHmMsUk2PHIBHkj7lIue-5FQ1cwof6JEG1sBAffrJ0sK3KujFf7plY7ioSAQhQJHmv5_x4LBcw_DWEro0SwIfyvRMN6Wfvz4ZPo_dPBuB0rNbAJijbdC9qqCYvEWEOC5jSp3jOILsPEkaWYX_QLKsIQ75YGfj_sCn0_rGTwGFRcLoCfxSzUZiDxvSYojyabFwMzJJ6xJ76iU0wQ8WjuPuV-JklbbpXGNpjMNEsn7R_SRrNIUqPpbvUIxUEwYHzoi4Cq-TeaC-NeS25p0VFEtHVVkyPtGkc-6UhmHeeiFbveMufibzzHlrXouQyk9nwS_ZxFWyw5Zffh_ZyD4RVb-0ZF60UEsKS5_DlqxU2ahGqDBVFTF_o4lX3pBw2UTuP-d4VlcrtzddcBIDr-iUA3lKcZDBjFgbfXz6ePrY82mSeGnFQt951vBUAdBxkFIxLY9kcDQG--kOT8IAjQW-XC7dEE11dhq-IN0rfzs-AuIzhu0psQS8s8Uh3MfOqC7iaOf-2doxO0IEiz9TjApChAjUZTQ0TUcvS4sacZjlQ6Q6rb7HFq2uMm8HjaNnzXHVr4RX7ANPuI-P4HzeWyyGDwG-ZW7ixjRbEYkz_3dxwO92j1_IyofcTU5qy9MO0syPqs0M5B6WNpiHPfaDKU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
