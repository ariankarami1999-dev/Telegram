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
<img src="https://cdn4.telesco.pe/file/RB7jsSRsErKHaUH4E-YOuKK3iyxmnVoDJal7tEXsd31ndInj26JdZsN5DWeodzvKBtGxD6DhtlgS8hrJvD73NdOjjOLUKrbpTM_7XNfqmF5pTDPAjb4w_K1-hI9hVkJULmpqMaG-2IpysWUr_ayMm75Z9iXmgD5aGb8EYGGxzFCXqAlTDQoMP2jaY-iWdqYPqmQ85RhXJ-CwcpKVuk9pxOaWTVHApNaZuRqRlpGuS-QO0fYJOOTyuANU7zNNY0wOi4q3yznZSP2z-0UaOd5HOf2M0d_7jd-J0C2DbO3evPWQNHBazSG0QwoI9UVO3vqaB3S3IivPRDW2lFZJCLndWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 161K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 21:20:57</div>
<hr>

<div class="tg-post" id="msg-68557">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
استانداری خوزستان:
دقایقی پیش یکی از مناطق خارج از محدوده  شهر و حاشیه‌ شهرستان آبادان توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت. این حمله تلفات جانی در پی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/news_hut/68557" target="_blank">📅 21:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68556">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مسی و نتانیاهو
🇮🇱
یا یامال و فلسطین
🇵🇸
؟!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/news_hut/68556" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68554">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHZGDWBfFOp0nbdHKExJN2qlj5qkVW5L4fzYbZOagVj3iIIwLYkPLLmDH1WKUq8AvrOrUrUftU8kpYe9c6daFwAsfPI5N3wjq7xF_0IgsWKuJS5z6vl2EfLLGhMHMllM5W6dTbGMDSPCo58V-VMCQUx5Ui_2szKDJ6HpEo6j3H9DVpN7mOd95i59WNXv48efG7PX6xB1GOtLbTrxDCZm73aYypKNbFZV2v01oMG0sgqOPNyE3lSt76cbTDunD9akA5hOtaXNUn2pOVmMwa-xeKZjZRPO1GPXDExyPfIMNVqj6m95dugMIlLbuPGcgj253l-ZIHdHI24jFMf7EfmIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HakuTlevRBJq0prKzEmkh47d8J_wcDX1qaEt_aZfnhLiZ8RDqtULeZGzeosYZXBZB9piwP0d75Eo4xl2dj0ncHnfu6AKGbXNZy989nkhooL3Iw75eH6SnsD1zq9I2nYNMr5jluBHke8rpXLe4ZY_tTbOpZRgmUo73tWYm4E_FArJ7Bbhg3dmFXepV_X2-habVjV9_-3pCQdPCSbSLVqvfeXwkSFhhd_HAjkIksFtAiq_u4mdUmYnIcpQU_N7Ifza_EYU2P1hVLw7xwY4l68MAOzzvWXiFt2NDmPlIUt50CJhuoRPKxB-2doExCb4EjhJvF-aUSySiRnkq5R7ael9aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/news_hut/68554" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68553">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
یک پیشنهاد جدید آتش‌بس ده روزه از سوی قطر ارائه شده:
• ایالات متحده حملات را متوقف خواهد کرد.
• ایران دو مسیر دریایی در تنگه هرمز را به مدت 10 روز باز خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/news_hut/68553" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68552">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=o7KsnWtyht46vQguGrQDO-wCDSmMhu8oPbBnznH63plHDAIgGO9Z03dk9d5aAfFSGjbk9RW9I8jVb7bdDjildaN7uh9kImyf84Mpdbk5OtPU2Ruef2wI_dSfU_mUCPJHUjhjgumAI_VZoL85SCe19KlM47gx_NJ3wOU06xPxti3IXsCqCgq61IzOTriuAzCoggw-Lri7OJ94n4B62im0yyD9kr3tKEBT_l0I5ls_u_Cph3zZ8sgQJNELcuIYQGCcyk4uWesa8NN5_kDanG8S_ijhDdSwMFW1CM57EjxOodaZsAhmK5Z9wLMe6_qLeEBQ3dEDZ_N2Bfxl5zoqpCu0Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=o7KsnWtyht46vQguGrQDO-wCDSmMhu8oPbBnznH63plHDAIgGO9Z03dk9d5aAfFSGjbk9RW9I8jVb7bdDjildaN7uh9kImyf84Mpdbk5OtPU2Ruef2wI_dSfU_mUCPJHUjhjgumAI_VZoL85SCe19KlM47gx_NJ3wOU06xPxti3IXsCqCgq61IzOTriuAzCoggw-Lri7OJ94n4B62im0yyD9kr3tKEBT_l0I5ls_u_Cph3zZ8sgQJNELcuIYQGCcyk4uWesa8NN5_kDanG8S_ijhDdSwMFW1CM57EjxOodaZsAhmK5Z9wLMe6_qLeEBQ3dEDZ_N2Bfxl5zoqpCu0Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
رئیس هلال احمر:
در تشییع میلیونی نه تنها یک فوتی هم نداشتیم بلکه شاهد چندین تولد نوزاد نیز بودیم
👅
@News_Hut</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/news_hut/68552" target="_blank">📅 20:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68551">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=fMcJmR-n9nL1AG7Ro8GiM4CASjoXpybmIb7uVkrc0lx3aVNY243Aq78AxZV8yTyTnAhBWFZ1vHk7MSIMydoNsi0yc_0z_39mv6G2_23TyWf1ZnXc8wEwD4mHcBF255v-2T9yjkgrgRl3FDJqXRd0GBaJc6wICGzS6ALjMlTxoZ_mzX1dYAPCxPGzwDxqkWbjZGtPAcaCXS2OEIaZGCJuKNCdgk3Iy5xNUI7m7eafPMZAwUrujTaEBNQvRPTCB5Jjdjd6sckhGl_Orf7zauM3mgAv2G9a8-yVeGuBtJuhUQmPO5hQAbyawvFkJ-oqixXD1Stcj11Ph0S1Qgnfs_v7pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=fMcJmR-n9nL1AG7Ro8GiM4CASjoXpybmIb7uVkrc0lx3aVNY243Aq78AxZV8yTyTnAhBWFZ1vHk7MSIMydoNsi0yc_0z_39mv6G2_23TyWf1ZnXc8wEwD4mHcBF255v-2T9yjkgrgRl3FDJqXRd0GBaJc6wICGzS6ALjMlTxoZ_mzX1dYAPCxPGzwDxqkWbjZGtPAcaCXS2OEIaZGCJuKNCdgk3Iy5xNUI7m7eafPMZAwUrujTaEBNQvRPTCB5Jjdjd6sckhGl_Orf7zauM3mgAv2G9a8-yVeGuBtJuhUQmPO5hQAbyawvFkJ-oqixXD1Stcj11Ph0S1Qgnfs_v7pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو :
آرژانتین امشب قهرمان جام‌جهانی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/68551" target="_blank">📅 19:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68550">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i732u5z9bGcueAGlw6d2-Yxh-54mFWH8SKQNafcf3MClOUovxwCP6iHRwVTcmACw1MqcH9H6O4GmhRqMmQhqhvWpwLNKMAhOdLyMcDaUr1LCroRohr_JvsJkRULsvgO_B6_cBaDyseTIZc4ZfdP4R35iyVb2LGl1dqLE8PZzeKza9eLNIzw_d7JPtMZ4rD1OZgOENO3CQsOM0ecqCsB-P4hqbNTzb43UhW1Ath38i5z56RJeko-cYWtil1_VCp05wXCPAtHxFH0o_lEsHjskEsVMFwNWVEY4NdCADt_3xuJP8cBfDQ8S7FwGdSSZOiA87aNVluK4FXTEtzZZp7LyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه امشب نیروگاهی در ایران هدف قرار بگیره، مقصر اون فرماندهای زن‌جنده‌ی سپاهن که امروز برق کویت رو زدن. #hjAly‌</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/68550" target="_blank">📅 19:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68549">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
رسانه های عبری:
برآورد‌های امنیتی اسرائیل حاکی است که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/68549" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68548">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت  @News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68548" target="_blank">📅 19:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68547">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oivj52D0ZwgSea1d9bcywcjg0HaKwFj_XpohAblURth0dF8XUqYaJzE0bTV443r-LhfiNV8ZiDOQMGFDImQuz8HrcCIGC9ZNFIXc7kfQoFWSKRkyeQ9RKMAdH0RBfEYkHc0glu3g7pT5mDR-Twem-0MrRLqIWrytB2yl1bNK65Eo0WS9xb-EtBNhftH0B_C8t3N_TW-NI95n7NL1mhCAfKpnFxU1ILeMAx5dX7prPLEPIaBE8Bz6FcrLfHEBbN49bxXj9FiyUPUR1ICnsK36qiiYF6RLzEtqaz7ybiKgkDbcmiAk9_YQduVdI13eT2jSzv7gNyD8Wb3IhT0C1rxoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فینال جام‌جهانی ۲۰۲۶ فوتبال
🇦🇷
آرژانتین
🆚
اسپانیا
🇪🇸
امشب ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/68547" target="_blank">📅 19:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68546">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=hC-4wRdvmNOFAZlog6rQ5M5HL7DUlVjXNSPUfcIN86ZlN4MZBCo5Q_jNHjFhrIaowhrxIfiOl_U8uB8mwE-XTU-8bMwPzXvNVqXuJoeG_LNXQzlGEAFFqkBlF4cY2RNm66vMIFAiqZ5tuZE-t2S2QAbGi52iPCG79HwGx1XDuDYdo0xtFBPCGLTlhJeTjBphttxguzI-R5DR8imXmlg0XtSmUrixIhQ6TkbChXUh3gSSwuW_DjY-IV0sqlrr74erHv8YEKwVb96rrmjnSP1MrnPgX1MrVAWbp2T6CbScCA6dhObrpbHJXPHFAKiSr6W5oEcmNS8oXP7lHBTyI2gdgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=hC-4wRdvmNOFAZlog6rQ5M5HL7DUlVjXNSPUfcIN86ZlN4MZBCo5Q_jNHjFhrIaowhrxIfiOl_U8uB8mwE-XTU-8bMwPzXvNVqXuJoeG_LNXQzlGEAFFqkBlF4cY2RNm66vMIFAiqZ5tuZE-t2S2QAbGi52iPCG79HwGx1XDuDYdo0xtFBPCGLTlhJeTjBphttxguzI-R5DR8imXmlg0XtSmUrixIhQ6TkbChXUh3gSSwuW_DjY-IV0sqlrr74erHv8YEKwVb96rrmjnSP1MrnPgX1MrVAWbp2T6CbScCA6dhObrpbHJXPHFAKiSr6W5oEcmNS8oXP7lHBTyI2gdgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/68546" target="_blank">📅 18:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68545">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
«ما اعلام کرده‌ایم که اگر ایران جرات کند به اسرائیل حمله موشکی کند، ما با یک حمله قدرتمند، بدون هیچ قید و شرطی، پاسخ خواهیم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/68545" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68544">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68544" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68543">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkkThs2KygTF6VDJx5LcAyx28IQ9Qh33yWHn4F7vBrSH_E5Bglgo_ai4hMaL3a33n3MOMBc-iYvqpj0lK74-uMv5wZ3XjOMuXYW3mVIfFYrQ5zNNm_1UVg-8vUXNIPyOYbXF55JFkhZMRTgEyU7QaFSXAaLwpdbdxtlLKqeQbUHK-RHs0QnLiyzBIEFcByZDIZQQ0Hxn9Q2U2cq5jrBXdiADypfZ9iv3kNDHLLdaD6FgRLxyqKOnzSlouzm0pOncaWdi017SBFmrA44vOshFJkn9yvWl-l4NAVL0eO8x8eAqWw5Mvl5G-duqEOO1XIxuSgXZq5X1czBrhPTV-ExcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/68543" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68542">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=lbmuT-px4akxIZEo_Tx8mhOaxQivak3DDS6gWNx4dRnFwbR1ZJEy0dJJZtR89c7BVJTUJHv-x8mv7KERhf17hnh_cvAyijjFtDXPnirZx4MLgVo0uj3LvatrNXvx9zdF4QZLWj2j0ACx5NWQQcQQLhDvS3nSWMfXQ8P85u3irYFI57wOhyx97gEMZKXNzeH2eTVuVx8OaA0i67yW5F7dAgBwVjNlzNPtxxDApqZwJQUXAuimnVj7GaI_Qo1hFLgbc0ZUPQdXcGhsl8UFaR7JnpU300BS1TRhJR6Hr1MYoQ0admJ5xAaOmDc6gEagNi2Kg0ah9T8CbnragFd0pLnfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=lbmuT-px4akxIZEo_Tx8mhOaxQivak3DDS6gWNx4dRnFwbR1ZJEy0dJJZtR89c7BVJTUJHv-x8mv7KERhf17hnh_cvAyijjFtDXPnirZx4MLgVo0uj3LvatrNXvx9zdF4QZLWj2j0ACx5NWQQcQQLhDvS3nSWMfXQ8P85u3irYFI57wOhyx97gEMZKXNzeH2eTVuVx8OaA0i67yW5F7dAgBwVjNlzNPtxxDApqZwJQUXAuimnVj7GaI_Qo1hFLgbc0ZUPQdXcGhsl8UFaR7JnpU300BS1TRhJR6Hr1MYoQ0admJ5xAaOmDc6gEagNi2Kg0ah9T8CbnragFd0pLnfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در دزفول
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68542" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68541">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=pTrt05iZT3B0WElP7_U9drtO0qDarLfl8Zf-GeQCxXO_wCSak3jgc1BenYM6ug9tFI6MJIV3qCzUZSPdUB7mtoQjhZBPnr_K7qrkuOjbrhkozUmnp9MBHlIGcfzIBtpkPd2IHFl6bEVIetxT6ARXT4O3FgPGtB69vNoSjhW9MWFjwOREM7Am2vG2C7sXTKB86uZEZ9xYnynw9T8bLJW1fN4T7XAIF-P9IutFXiz-k5uP_cC-lafyUQHbfv13EgvFiIsRa9tdhKAIVo5Vtrq4UaBGPG0LTNkmLorHF3AfExEpxslpZ9lA6AqHGd9LlzClotutc5ZrJRQ5i68ZHiEBQjD3znV-MQIfbt2XnvG8Oon7cL6KoMi9yNTxiJRfDuqrCtxg1t4UU08m3rqBnuSdccI5X2KwcCJY7BKyUFER-23zX46Vovb7IiBGkkXgQ_hzbl-70PHaDgXdudqN0jXWpieLUlb29dfeSAHanoPAxw6tVp3yMDrVqKVnGQ-hBTerhYIoNqLsi_KMdt57Wb_ecIGP01m8NSAu_ZJUsPwZcKlQ9Al6S9iqJpKz9GbvdkjGWa2YS1rkn0oMdFgI6yRWz1y1VdFuMx_Xhv_FlwnG2HDKX9nrCq__BVIqA3cKj1dbb-eJOcZiRag4fDLNZblhEbTBG4BLKDfe99_rBZjdoes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=pTrt05iZT3B0WElP7_U9drtO0qDarLfl8Zf-GeQCxXO_wCSak3jgc1BenYM6ug9tFI6MJIV3qCzUZSPdUB7mtoQjhZBPnr_K7qrkuOjbrhkozUmnp9MBHlIGcfzIBtpkPd2IHFl6bEVIetxT6ARXT4O3FgPGtB69vNoSjhW9MWFjwOREM7Am2vG2C7sXTKB86uZEZ9xYnynw9T8bLJW1fN4T7XAIF-P9IutFXiz-k5uP_cC-lafyUQHbfv13EgvFiIsRa9tdhKAIVo5Vtrq4UaBGPG0LTNkmLorHF3AfExEpxslpZ9lA6AqHGd9LlzClotutc5ZrJRQ5i68ZHiEBQjD3znV-MQIfbt2XnvG8Oon7cL6KoMi9yNTxiJRfDuqrCtxg1t4UU08m3rqBnuSdccI5X2KwcCJY7BKyUFER-23zX46Vovb7IiBGkkXgQ_hzbl-70PHaDgXdudqN0jXWpieLUlb29dfeSAHanoPAxw6tVp3yMDrVqKVnGQ-hBTerhYIoNqLsi_KMdt57Wb_ecIGP01m8NSAu_ZJUsPwZcKlQ9Al6S9iqJpKz9GbvdkjGWa2YS1rkn0oMdFgI6yRWz1y1VdFuMx_Xhv_FlwnG2HDKX9nrCq__BVIqA3cKj1dbb-eJOcZiRag4fDLNZblhEbTBG4BLKDfe99_rBZjdoes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صحبت‌های وایرال شده سرباز آمریکایی خطاب به مردم ایران :
اگه حمله زمینی شد بهتره فاصله بگیرید از نیروهای آمریکایی
نه اینکه بیان شمارو اذیت کنن، چون ارتش آمریکا خیلی مواظبه از سپاه که بعضیاشون لباس نظامی نمیپوشن
سپاه میخواد با اینکار به نظر برسه که مردم ایران علیه ارتش آمریکا هستن
سپاه اصلا توانایی نداره علیه ارتش آمریکا بجنگه
پس اینا می‌خوان پناه بشن بین مردم و حمله کنن چون اصلا نمیتونن رودر رو پیروز بشن
خداوند ارتش ایالات متحده و مردم ایران را حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/68541" target="_blank">📅 18:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68540">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029372426.mp4?token=DZwtiiPc3y6oYiaEQKcEemxBeTtr3uvtEoFnJ5ommAybJ52tT2ALku7r8KTSkFII-xeW0H3LbdlabaKRHAPaixckwmo2UyUZfFuQGyaLTGgWmR5HEZ-RYihgPVmArPDIQPm9hwbr251eoGjX_Zo8caEIFuH-JgXgamBCbDO6qbNP9ZNdDnXmdNoiha18zT4bulDzguVRJPcxSoXSQaT5L8QWdYqztP7Cn6qxez5SO66GnicSaUvv55ZZa8JZ7TNR3ioFH3R4tOpybS6h7ot0JjlBM1H3VeoMxMpqLjm4Qw4x4VAYbM0_6k1tng3M0Oe2aOAZ4r1ZORCbFE5bTSrWnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029372426.mp4?token=DZwtiiPc3y6oYiaEQKcEemxBeTtr3uvtEoFnJ5ommAybJ52tT2ALku7r8KTSkFII-xeW0H3LbdlabaKRHAPaixckwmo2UyUZfFuQGyaLTGgWmR5HEZ-RYihgPVmArPDIQPm9hwbr251eoGjX_Zo8caEIFuH-JgXgamBCbDO6qbNP9ZNdDnXmdNoiha18zT4bulDzguVRJPcxSoXSQaT5L8QWdYqztP7Cn6qxez5SO66GnicSaUvv55ZZa8JZ7TNR3ioFH3R4tOpybS6h7ot0JjlBM1H3VeoMxMpqLjm4Qw4x4VAYbM0_6k1tng3M0Oe2aOAZ4r1ZORCbFE5bTSrWnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این مجری که اخیرا زیاد در صداوسیما حضور داره گویا اهل کشمیر هندوستان هست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68540" target="_blank">📅 17:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68539">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W60arxYoPItAbVRdP2vq5bwlGlFveyBxUJGpwZFX_fncLZwSSGDHdMNfjMdr1gMPQGObxT_RMPS7PfW89wYCTSU_F6xgtULG9BVsEskDqljGIl881PT5it9WiF6I_9-84F6ACzDHIbZd3gursAw09wkJjAHNwVKY6PIQL5-faoDx8eZGZPXVX32pB-jw-YDMkHC_H6KQAL3EZTDJBIWKwRzCDzSxsHzOwHXUMI5KS0uoU3htQjQvuVZphdxBXXQC6AGQEub2-RH_cHP2DNbS6FWnoCEUAqFMSJEl4z-JMFJtuakBCx2IT09ZkXymocVzhHSjsPwnvfjAJPwUThwtPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان انرژی اتمی جمهوری اسلامی:جت های آمریکا صبح امروز با شلیک چند موشک به سایت نیروگاه هسته ای درحال ساخت دارخوین در خوزستان حمله کردند.
ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68539" target="_blank">📅 17:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68538">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=tE5O5-k9QevOW1ek2vfUlK5BzGit7028Zkvt_xoy5G7cft4DNTdn-DbPhnkNbcmwF8jmCwS44cBB_DhM7EWTCjt9UeA1zKu70UnvJSTkBXe5m4EcLQcZ2gLStnKMLb-M6Jd3ZWQ_UovSwH5rC21NFiF5Br6eAxUkwaNx-FNoGxMTnCs6MWNeai0EVmOVfB5PaCfUSATnDsex9U8cWZA1acz6WGeVXzmQWcOHQLHILUX6ApYzDqodI_cJELd0DgLzpIiP8yHv8ksBOHx8fkuOFfDNcx8XnA6GVm4d_NvKNYGfehDEWLHuXFdMl-O_0WYtE1a4aw84PGeFWisx-2Cei7QVHBsRGl0YxVprP4nBX0WuXj0atAM3BF30ADbRqDYEEZXw2ZeyOd8XbpQrtsJTHyR3C5ahXvEiSiFnvK8WJwSd0wwaNxeqS91KHQNdJnmjv2NSdASOhIx6ZhuIWWV7zF8jaLvL7JpQFLQIHSu_7Z4QexBokNBrZJER2WurzBpp6GVdyii6ApmA3_P5L_LfWB9j4lCZU4Onf8lTiu_OtrF2VLH7n0vOCarL4TKrpyA9TQBTXMf8bKVwL6ipV-46rED_n19Jc_R1WmNxE_Do4my8CXKuO8zOt4sAcb2Lj735JVeIaGdDpylyXjQbXE0acJy0kb7hxTEUPLxmiVGnfYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=tE5O5-k9QevOW1ek2vfUlK5BzGit7028Zkvt_xoy5G7cft4DNTdn-DbPhnkNbcmwF8jmCwS44cBB_DhM7EWTCjt9UeA1zKu70UnvJSTkBXe5m4EcLQcZ2gLStnKMLb-M6Jd3ZWQ_UovSwH5rC21NFiF5Br6eAxUkwaNx-FNoGxMTnCs6MWNeai0EVmOVfB5PaCfUSATnDsex9U8cWZA1acz6WGeVXzmQWcOHQLHILUX6ApYzDqodI_cJELd0DgLzpIiP8yHv8ksBOHx8fkuOFfDNcx8XnA6GVm4d_NvKNYGfehDEWLHuXFdMl-O_0WYtE1a4aw84PGeFWisx-2Cei7QVHBsRGl0YxVprP4nBX0WuXj0atAM3BF30ADbRqDYEEZXw2ZeyOd8XbpQrtsJTHyR3C5ahXvEiSiFnvK8WJwSd0wwaNxeqS91KHQNdJnmjv2NSdASOhIx6ZhuIWWV7zF8jaLvL7JpQFLQIHSu_7Z4QexBokNBrZJER2WurzBpp6GVdyii6ApmA3_P5L_LfWB9j4lCZU4Onf8lTiu_OtrF2VLH7n0vOCarL4TKrpyA9TQBTXMf8bKVwL6ipV-46rED_n19Jc_R1WmNxE_Do4my8CXKuO8zOt4sAcb2Lj735JVeIaGdDpylyXjQbXE0acJy0kb7hxTEUPLxmiVGnfYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش امیر رولکس به حواشی ساعتش در جام‌جهانی:
به جا اینکه بگم فوتبال با ما سر ناسازگاری داره از کلمه خدا«داره مارو میکنه» استفاده کردم.
چهل چهلو پنج ساله ساعتمو دست راستم میبندم.
اگه یه سرمربی ساعت می بنده و لباس خوب می پوشه که اشکالی نداره.
اگر من زنجیر طلا مینداختم  و یقه پیراهنم رو باز میزاشتم آدم خوبی بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68538" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68537">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSsBCVPRuJapN6HZm4YSZJvmqekUsViBKdZvVhkSGHY97EvFGBOSD5RSEpdDOVix89CCZPn_hL89DT6HMNRAiMU1U6EQPKnNd53V5bqdVl2D8ZXJ8FobHPGqgR8yYxN21bC7V2xexsU2P9hGADosdcKHfK76rShX7ZpmlxUY_glHvqY1K_2BT69q-4VK4tddWHNEivtpa0IwxzqkWAWzovRDsFVAgsCm2FxC0Dq59_nt7uWbMRlYNZfdf0fuN7efaH-uMUqfaBL38h5DyRCnrx5C41qoOV_spwsbhXayVMSeZ_WjNM97JaJgCKvAzc2zBuawmCE2WfUjwNscDWT0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پرزیدنت ترامپ:
جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این همان کاری بود که لیندزی می‌خواست انجام دهد و قرار بود محقق شود. مهم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68537" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68536">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uykzaa_AqJ5BXAu2mC3fT4lp9DVQXDUz6Gv6mwqTPRvxsuK4XqEXRnAPVsjtyfbM_Ut3qRyTGYxYWiapa1IpIED6gMemuws4qKTqo8hzgO-KCpVcLXu5UChh2ykeO4atWH9Pv6OjepFs7-_B_Dj4_-5Z1G15QaTbNv6_9RcSBSFKnSqbeZJ8vEpSYCv2ChvvgBqr9uAKv1bvc9QJmV0kSs4zLgWPUIzyh4-t_VcNjz0HsuKPwIawg0Y7qxG_W69kx1eL4hasDpmDYif3c6Ug-v2IWf3BWRi_3Rey3ArWl_Q_du7QoHSVjjErwsrzcAg0JolEVHtRC16hLdvqRR6klw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛ این 12 نفر از متهمای پرونده میدان علیخانی هستن. +پرونده میدان علیخانی مربوط به  اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68536" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
عراقچی:
بمباران بیت از طریق حفره امنیتی صورت گرفته و این حفره امنیتی همچنان وجود دارد
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68535" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68533">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3548648f57.mp4?token=EngxXc3kUSX1LTEMlUTksaOcYtwSgR2808WXiCIDYXwdZggdLPH5KFdKgpDDW8OCFR01I6ExCEPvUewQtRdzv296vbgKVJMeWDzm5nU7zIuefNVMq6kMNXV9mpPnui9MWX8u0tiUKe1lvYb5LLowGFvoZDauTxleldf8LOUkO6UWAeftS9a8qpWm-5EEyRp5lMPAaddkoeQqx-VZawR7BNHkL9GgL6v1JIfwgH93PXSJwq5IIoirC4HYsg3NOt-G6XVicKnsWtbfK6c16yOWQPCnaXQVc9f7qHbWqs0ss6btwmgzgCQlasGfwUzrE67P8qchS-VUmo2qxZSNSkvMfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3548648f57.mp4?token=EngxXc3kUSX1LTEMlUTksaOcYtwSgR2808WXiCIDYXwdZggdLPH5KFdKgpDDW8OCFR01I6ExCEPvUewQtRdzv296vbgKVJMeWDzm5nU7zIuefNVMq6kMNXV9mpPnui9MWX8u0tiUKe1lvYb5LLowGFvoZDauTxleldf8LOUkO6UWAeftS9a8qpWm-5EEyRp5lMPAaddkoeQqx-VZawR7BNHkL9GgL6v1JIfwgH93PXSJwq5IIoirC4HYsg3NOt-G6XVicKnsWtbfK6c16yOWQPCnaXQVc9f7qHbWqs0ss6btwmgzgCQlasGfwUzrE67P8qchS-VUmo2qxZSNSkvMfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وضعیت ایستگاه مترو در کیف بعد از حملات سنگین روسیه به پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68533" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68532">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68532" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68531">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exzxR_1SF-itmE77JipijOZ4Ri-8puENs3_sEyaxBXWcgIXH1AkyWWD9vPVo2Fl4NyUcRK3dkwXLQTsyAP0yzjXQn2frRXUT4TzrMqXtlMgq1Na8x6043RyDWa5tSWlQbFmXFFCaW2bQD-HNea1rvRJ4hckl4y_2FExwZ0pMWWjFobCdowvpQRkZD3pV3zLs1m4QmN9hhmOlfhlQ6hf3oyGarP8HVCJzO4Ucvb7aSVlj_Gp7P4RC6MRkC-MKG7NBbtbLfxq2kW9x1b1M9sdWxO_SWVpclNqS7ChMFQ0_5eKTmfNEtE6RqIPQaXZAm8kZOFamycaN1jMLeOde4WPR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68531" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68530">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326d421018.mp4?token=e4LO0EsXbEeT-tygIxNGYDojeLUCI6pSg5QQKYA0vy_6_MidAjlyuq94Lu6CfdJjjn-i7w4yE-UuEyjOd12VmJNN_OHcAEU_MDvlQDSuQaEQxsHHxFkSxOeoBxlegccS2S8DB-jtcs-CDh2YCCgJnXXy7KokLndO1kgwdJFke0xzJXIV6suL85WMbhjNYD-YEkSy80Siw9XQpLvSTG6SRWEAU636qxXKNZ-2n8mDwW8NQPP93RLawXKjOlhr9VnviwCfjWlHYqlZQyX2F_UJm84sRr-w3CgyCQEdHU0DMFrkyjsizRTv8bzjZpzeEaUQA_IfDYHjAkwP3KsoJW5dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326d421018.mp4?token=e4LO0EsXbEeT-tygIxNGYDojeLUCI6pSg5QQKYA0vy_6_MidAjlyuq94Lu6CfdJjjn-i7w4yE-UuEyjOd12VmJNN_OHcAEU_MDvlQDSuQaEQxsHHxFkSxOeoBxlegccS2S8DB-jtcs-CDh2YCCgJnXXy7KokLndO1kgwdJFke0xzJXIV6suL85WMbhjNYD-YEkSy80Siw9XQpLvSTG6SRWEAU636qxXKNZ-2n8mDwW8NQPP93RLawXKjOlhr9VnviwCfjWlHYqlZQyX2F_UJm84sRr-w3CgyCQEdHU0DMFrkyjsizRTv8bzjZpzeEaUQA_IfDYHjAkwP3KsoJW5dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای امنیتی سوریه یک محموله تسلیحاتی دیگر ج.ا به حزب‌الله را توقیف کردند، این یک کامیون خیار بود که زیر آن ده‌ها موشک کورنت ضد تانک قرار داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68530" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68529">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
ملی‌گرایی از نگاه خمینی، بنیان‌گذار انقلاب اسلامی:</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68529" target="_blank">📅 14:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68528">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=SVrIsRSDiLCtB94da0rwcjajTvR9uQzqfMKZ_HvQ-OnJX__sHiM5rt5oaaHIzLPdicA_POVhAXR5sl3YIOOnhaTjWZZzNaNkGJO1RUN6FZ3iM9G49CgdhWO7YD5EENqBWxkDSwDRVH2a4kEc2hughY_Wzu9f_xCW8dny9QEndENHVrOLUOP2o-Mqh3nImp2gDhfGRS85IVAFJt08VPTFqxN8KoMG8ubA56S2WofE-4ntfv3ku54gXxLGc_ZVVjBkwx2tmL21NaGP7Z281NNTI7Z1gsAFRuAso1rHSHzurqtaY4N__Oy4JZtDUVPUszeBnt46cEui3QVGyNwUKGe_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=SVrIsRSDiLCtB94da0rwcjajTvR9uQzqfMKZ_HvQ-OnJX__sHiM5rt5oaaHIzLPdicA_POVhAXR5sl3YIOOnhaTjWZZzNaNkGJO1RUN6FZ3iM9G49CgdhWO7YD5EENqBWxkDSwDRVH2a4kEc2hughY_Wzu9f_xCW8dny9QEndENHVrOLUOP2o-Mqh3nImp2gDhfGRS85IVAFJt08VPTFqxN8KoMG8ubA56S2WofE-4ntfv3ku54gXxLGc_ZVVjBkwx2tmL21NaGP7Z281NNTI7Z1gsAFRuAso1rHSHzurqtaY4N__Oy4JZtDUVPUszeBnt46cEui3QVGyNwUKGe_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آتش‌بس با نظر آقا مجتبی بود؟
🎙
پاسخ
عراقچی:
این چایی برا خوردنه یا دکور صحنس؟
☕
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68528" target="_blank">📅 13:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68527">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران:
ساعاتی قبل، دو کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و دو کشتی دیگر از ادامه مسیر ناایمن منصرف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68527" target="_blank">📅 13:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68526">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=NnZNY146_4UQIX5sC7hnbSmomDrnKNUZWCgVa7ulxWrl4o34WSy1weGLPLosmMLCZWrQbcRpQIp72AjPX6XqSVqDIs7KHZj4EiEFJExY7uLs-_zSC2JDQgUSJIHkoKIRf5EIcfXBLoLCFzrEtEghiUKJ60vDDV7LOlr7vkusnXVxuxC9DnQt7nOVzYMfRH1AfWLVTweDsrOPRDn5uUMsOuffTXdFPeAD-3DA1Eo9qT6luMu-v776ledK3SQU_eQ6yM7wwlXIny5nZuBY7Zs4bwSOLDuld5dXPoFGJlTijsAoRpinRoAHRsD7OFr1l3FTQdjC9iiZG7uvMpvJXM4OpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=NnZNY146_4UQIX5sC7hnbSmomDrnKNUZWCgVa7ulxWrl4o34WSy1weGLPLosmMLCZWrQbcRpQIp72AjPX6XqSVqDIs7KHZj4EiEFJExY7uLs-_zSC2JDQgUSJIHkoKIRf5EIcfXBLoLCFzrEtEghiUKJ60vDDV7LOlr7vkusnXVxuxC9DnQt7nOVzYMfRH1AfWLVTweDsrOPRDn5uUMsOuffTXdFPeAD-3DA1Eo9qT6luMu-v776ledK3SQU_eQ6yM7wwlXIny5nZuBY7Zs4bwSOLDuld5dXPoFGJlTijsAoRpinRoAHRsD7OFr1l3FTQdjC9iiZG7uvMpvJXM4OpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویری از انهدام یک پهپاد نظامی مدل MQ9 متعلق به ارتش آمریکا در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68526" target="_blank">📅 13:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68525">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpmb9TlA_hwLq4ffdEU5z3BU9hyjvpfieh_fxk1mGiRXjL4XQCgXpu5le9xMS2oD40I4hT3ZXeEqJ4auEvmC7-z5fItpZ3L3Fm9wz8syeJBeOLUbkFKMqQgEVkXPwE9ShgudiU48Q34ChPH74weJhZd_EFBebsBLRBEhhAwTgfCkiBfWjni5Ggr_5fjrQWW9jQ5w3rYicaObLNxv7uREiE01vaNRqhAYMPvnosC3GiYIpSR0JBnB0u6W8jFW1avstuLHLI8d7tXD9V7TjcVmvLLo-gZbcuPcNDdCQ93QZlJjQZekY8sEgUWxTGgl9AeC6IFdTwzOmwCZQBLQo1mTLH_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpmb9TlA_hwLq4ffdEU5z3BU9hyjvpfieh_fxk1mGiRXjL4XQCgXpu5le9xMS2oD40I4hT3ZXeEqJ4auEvmC7-z5fItpZ3L3Fm9wz8syeJBeOLUbkFKMqQgEVkXPwE9ShgudiU48Q34ChPH74weJhZd_EFBebsBLRBEhhAwTgfCkiBfWjni5Ggr_5fjrQWW9jQ5w3rYicaObLNxv7uREiE01vaNRqhAYMPvnosC3GiYIpSR0JBnB0u6W8jFW1avstuLHLI8d7tXD9V7TjcVmvLLo-gZbcuPcNDdCQ93QZlJjQZekY8sEgUWxTGgl9AeC6IFdTwzOmwCZQBLQo1mTLH_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
مصاحبه عراقچی با جواد موگویی؛
جواد موگویی: دست فرمان شما دوباره باعث جنگ شد.
عراقچی: دست فرمان من نبود.
عراقچی:اگه ده روز زودتر آتش‌بس رو انجام میدادیم لاریجانی رو داشتیم خطیب رو داشتیم عسلویه رو داشتیم فولاد مبارکه رو داشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68525" target="_blank">📅 12:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68524">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=Rb4CJ_GmckZMg9uFnTfFm7vZdokB4z5MNpcYPyX-cP2OUVMEE70rreqlSrNS0N6njHjLDApskkNWvCt9IVpd3G-gPYBP7JlwBfNPEmQOoDx7sZ1sYUyN7om-TyFdgvqJygHjwVzghirUOta2Sfs0JhW_QYzsm_exoPxEgRePiHk0ri-PcCZUMIPCEkHvTTHMDPMpzgl5_voxSA0POG7Ialfzu_yBSmgMFudL7zEVvIQisPkGEnkw9zzyvgSI6TGzPomvC7eehvFAvcSe9QS9Aap9y-t4zjUX6JNdPT97bQvHDdPiunj2xBMe9ESVdKECmydI0IbSLFzyU-Dt6rpD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=Rb4CJ_GmckZMg9uFnTfFm7vZdokB4z5MNpcYPyX-cP2OUVMEE70rreqlSrNS0N6njHjLDApskkNWvCt9IVpd3G-gPYBP7JlwBfNPEmQOoDx7sZ1sYUyN7om-TyFdgvqJygHjwVzghirUOta2Sfs0JhW_QYzsm_exoPxEgRePiHk0ri-PcCZUMIPCEkHvTTHMDPMpzgl5_voxSA0POG7Ialfzu_yBSmgMFudL7zEVvIQisPkGEnkw9zzyvgSI6TGzPomvC7eehvFAvcSe9QS9Aap9y-t4zjUX6JNdPT97bQvHDdPiunj2xBMe9ESVdKECmydI0IbSLFzyU-Dt6rpD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68524" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68523">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇮🇷
فعال شدن آژیر خطر در بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68523" target="_blank">📅 11:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68522">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3dTHwDJE1eHwsWaNvZuLeL9X32J2h1URQGoIf3vUMIl0bi_ITo_UmdIxReUMIIf5BY4sRab3aSzUkSrgs4JlNR6F5QtemOI3OOfaz9GmirNeouBMsF2_tpMBuVPijX_y6oYpf20FuKYD2al0nsimhbFx6Ys8FwqKTcMZfSddX8pH3DtnxAjK5IlzldvAFUHDA86hMkfTEQg6mLhZBnXXb0M4Gv3dLUgkK0ThpmU2DVwJoIIYhOi-w2iRn9Jc_eiC5sZ3PDgSxh00uUKgUhP1j0X8nNl0IUAh6YDi6EjMlLnyMHyvb-tBvcYJTac_xKcxqzOFbWG-e88bnHYIiFVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛
این 12 نفر از متهمای
پرونده میدان علیخانی
هستن.
+پرونده میدان علیخانی مربوط به
اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی شد؛ چهار نفر از نیروهای بسیج و فراجا تو اون درگیری‌ها کشته شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68522" target="_blank">📅 11:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68521">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
در هشتمین شب متوالی حملات ایالات متحده، نیروهای CENTCOM با موفقیت به تأسیسات نظارت ساحلی و پدافند هوایی نظامی در ایران، قابلیت‌های دریایی و انبارهای موشک و پهپاد حمله کردند تا به تضعیف قابلیت‌های نظامی در ایران ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68521" target="_blank">📅 10:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68520">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
جدیدا تو جشن های تعیین جنسیت دیگه خبری از ترکوندن بادکنک نیست
الان پدر بچه رو میکنن تو منجنیق پرتش میکنن تو بادکنک و آب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68520" target="_blank">📅 10:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68519">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=F4jKt383PcCm37SyCgjCwgjMIGAZMTSLJRNPOYBaDwlxTfIv-XxfMi9zRD0hT47aIGWdWcHX2T-6xHAsEYfCQ1mK96MtB85m-hw8DyfsxPiYEzGqhxMUKsFH60M0xmcXIup2TztC9ZUfs5UA_WkzkXARIb7MAX_BhTYsr0bLVRbFBbGDRK9xHq8jc_ggac-31JJFw1DBGkv3bwRabhEw9fJOk5cAs4Gw4xpopz1FjQoEK-zfI3_AnzsBBjlBnXQPlep38fK9h_QxkdEEprLYZe9AAuElRLSr2tir-P8mP1LmV_MSmaAEvw0L0uQ_o688NqgT3gXrOwIrIeD5KsYQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=F4jKt383PcCm37SyCgjCwgjMIGAZMTSLJRNPOYBaDwlxTfIv-XxfMi9zRD0hT47aIGWdWcHX2T-6xHAsEYfCQ1mK96MtB85m-hw8DyfsxPiYEzGqhxMUKsFH60M0xmcXIup2TztC9ZUfs5UA_WkzkXARIb7MAX_BhTYsr0bLVRbFBbGDRK9xHq8jc_ggac-31JJFw1DBGkv3bwRabhEw9fJOk5cAs4Gw4xpopz1FjQoEK-zfI3_AnzsBBjlBnXQPlep38fK9h_QxkdEEprLYZe9AAuElRLSr2tir-P8mP1LmV_MSmaAEvw0L0uQ_o688NqgT3gXrOwIrIeD5KsYQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇱🇧
پس از ترور خامنه‌ای، یک گروه از حزب‌الله تلاش کرد تا پسر نخست‌وزیر اسرائیل، بنیامین نتانیاهو، به نام یایر نتانیاهو، را در خانه‌اش در میامی ترور کند.
⏺
سازمان امنیت اسرائیل، شین‌بت، این توطئه را در آخرین لحظه خنثی کرد، زمانی که این گروه از حزب‌الله به طبقه زیر آپارتمان او رسیده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68519" target="_blank">📅 09:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68518">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68518" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68517">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=iTvL29JICXu8WT3aJCTrxd_u1ss5OLCrU7tdYIHCMjYXIuWeqJtVKnaKVbOKWFWwcC0obRQ8dmVXX248NsGEMFPNQYuKBkwKotwvxl5vhSJY7a_GBOz7YaFB7Ix2SswCI_s8qXN40nah7DV5ORFTJBYPRzUirFabtEvtRX2gdVlyX_FYIrUCcxQfaZMaqSaa1WIcFpm9qzYl5jVLWGgxBpk31xPSOEleQhmwf_h5_nAefA5xnjJUPo7VZck3zCEE3srSk2CtMx9FdjDVcg-RuWdE1XJSxpr_n1MSM9h85MO9i5YOZfuokpNHgAIDF2EOANLjZLbjax--0RYF3lHuYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=iTvL29JICXu8WT3aJCTrxd_u1ss5OLCrU7tdYIHCMjYXIuWeqJtVKnaKVbOKWFWwcC0obRQ8dmVXX248NsGEMFPNQYuKBkwKotwvxl5vhSJY7a_GBOz7YaFB7Ix2SswCI_s8qXN40nah7DV5ORFTJBYPRzUirFabtEvtRX2gdVlyX_FYIrUCcxQfaZMaqSaa1WIcFpm9qzYl5jVLWGgxBpk31xPSOEleQhmwf_h5_nAefA5xnjJUPo7VZck3zCEE3srSk2CtMx9FdjDVcg-RuWdE1XJSxpr_n1MSM9h85MO9i5YOZfuokpNHgAIDF2EOANLjZLbjax--0RYF3lHuYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68517" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwJ7bMx_q8dEs_eOQoZCubZGiPMDqDPLxHQRLhceRdX--OBjyzmHNTy-GhScl0Epg_KM0ozm1F86VXLcLtv9-n-LtjRnS5xa05xZeP8U0wmcMGljo5Q6JkqCKiYDVncgC_orL2I4EaEoHa4JNk-dghdXHI0WMs2lXMXvK5xcUV87qp0PihCGdrFkFVkYuSD3Tp8KFft_R2OqKCtq5r7aQXdsHCdbueqDfy4FVWW-5TPJZaOvjCCqnu5359h030KyNWChePhTVvWboSxGS4YKSokzO4y30FuIGvK-smkiHzBQTH9391Au5yT_b7j2sx1jdklVqiXp6uQd56qr_8f-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlM56sZkxIWxPk_6uyfBfoZ5-nhnDz-MBPANYYCdbZEmhfuZR_kLHhuYmtJPQRy7qcmZaCU58yCofKRyKksiCdVRTRGksNOwySJ_SspoPOwWtMdrL-8hJPnQYSNJpdkpMLrXPLnVYUUT53D4UCHSQOzN_pTHR2ZfHWqJbpAoag6We-JRO2Oc291hAW5mISnR1tCgAgLk31dO6EfEEpjJMRdcQG3CawXMZIn4-oNEVpejRTlzghqAtWnIxmA2mSczFCR3tjEv16_8btzpvK-0RjL-2-4eO3Kj9z_oikp32P6Qbd8c_J7LifjPMnZ3c_vNaFl3qowVWgIbnjcEhFbLhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
حملات موشکی روسیه به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68515" target="_blank">📅 03:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🏆
رده‌بندی جام‌جهانی فوتبال|انگلیس برنده جدال بازندگان در یک رالی تماشایی گلزنی؛ دشان و تیمش در روز رکوردشکنی امباپه و اولیسه با مقام چهارم با جام ۲۶‌ام وداع کردند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
😃
-
😀
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68514" target="_blank">📅 02:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
تسنیم:
حملات نظامی دشمن آمریکایی به حوالی حاجی آباد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68513" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68512">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68512" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68511">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
دو انفجار در بندر‌لنگه
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68511" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68510">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
صدای جنگنده در آسمان کیش
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68510" target="_blank">📅 02:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68509">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=G9bRB2iZNmh3r3zYM3P7AlkgldaRm0Ez0kEwTcThaSr5T1pd496mL599sY-Ju4klRKtMgwkTmEYNzfJArD6Qcuau8Gz04VQ8BQww8r9a3DZcBonX2UCD9KsvBX6_cLByvrgDzDrmnFCSKF0o-cr7-_vRT1iL_GGC-XDS_iTiJRTQzbw4N1JLGwyrcjMEtVB9pGb0cfi9DOhYI_1ag9jMM3YyZi2S_6XRGVYv2eat6s3i198NP70lz6FWk28zEMhnn5i16M7dSmpVlNdVnfU_ejV8WjZCiK2HLsZwu_PaGW4B8S8uTxw79VX4XeYieOfi0WClo3gt0tMjoLseMRbhzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=G9bRB2iZNmh3r3zYM3P7AlkgldaRm0Ez0kEwTcThaSr5T1pd496mL599sY-Ju4klRKtMgwkTmEYNzfJArD6Qcuau8Gz04VQ8BQww8r9a3DZcBonX2UCD9KsvBX6_cLByvrgDzDrmnFCSKF0o-cr7-_vRT1iL_GGC-XDS_iTiJRTQzbw4N1JLGwyrcjMEtVB9pGb0cfi9DOhYI_1ag9jMM3YyZi2S_6XRGVYv2eat6s3i198NP70lz6FWk28zEMhnn5i16M7dSmpVlNdVnfU_ejV8WjZCiK2HLsZwu_PaGW4B8S8uTxw79VX4XeYieOfi0WClo3gt0tMjoLseMRbhzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68509" target="_blank">📅 02:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68508">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68508" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68507">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjZzphJaTzydWhmiKWPgoVo_lPIfr9AtvgXz_uQ7PPF1p06_bqY3aVQ_pxxGgUShWYIK1musR0rbMkAwhKGgG0zHixPqrPO3RYmNG2J0Glprd1Llbj-BmaMtGZkDIhkchPWZyqodKt1_kqxo6YZW4e8et0SXw3JBccCVbqvfN4-NQlTzfEfaJpRPm9hRFtjXer-SgM8tygL_5MqVnvimb1r8QhTvGohmafMwY7qXe_PQRcAFGgkatfh3NerDIdzguuSmIGCaMQoVE0yxk2fIi3KfsKjw0mR6ysnJkOXfLC9N4FxoXeR-Hwddsso_tQR7ImLoA47AlQLlKhfF1mghFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ عصر به وقت شرقی، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و تنبیه فوری نیروهای سپاه پاسداران انقلاب اسلامی است که شب گذشته به نظامیان آمریکایی در اردن حمله کرده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68507" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68506">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام اعلام کرد دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68506" target="_blank">📅 01:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68505">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm9llfHlOia3Hzh2XeNhHNa8_JxSZUmcIU_sP5iPn1FcWTnyHNB5mByMQj8JNKL8my83wLFg5U1NdBCzzD9WU6-oCaI0gIYiSM3KjJUvOomXH3x9eLbBNxq8_4rnNp-qOSHDlmMCerLLQ0x7d1Dq3QnkgVR_acHCj4vvG7kls_P_Sx4No_44Ref_OmQhTt2s5Ny4e74YgSrQTch5H3L6-rs3pGZ0JYCjC6ZAqUxbsBUSsbJYrDVrZWb_qdKqSuiT8w4whyriu8QQvO0ivGEqkKX72EPayqUIK3HGyIne-ieLJ68hUQdIPfvh7W_682dNL5ONBj-hbqxIjhrtu_3fgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
حداقل پل صراطو نزن بتونیم رد شیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68505" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68503">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdhbS5hEM61XaQMg6G6PHuNNWZFaoVCDK6PMueI-i6VFdCU4y0SbcvcQG3cAEZC7SGfp3scnpZUdvyBKanGOE7trzTYo4j6Tcz3TvT1-PTE1YQ2oqTEc8ED1GYylQdUiU3y_Oht5i2wtMUToUDHHWGZU1zyWpbNUc9gLRoxvAqQKXy_4H3S5Y0eL_MQ5aVM6dEM-bfNS3aaNQpLLDMYFdVSjwr62x43M9IXlyI0_7p-AlrqehdCRVzG211yZrhCpmPqK95HVpCIQynQ4lbewidnJZCidw4zPM1lDToQ-A8VuggL-zL0an_Cf268jzOpG__MwrH3i2dPbiB47djtsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwHNGBJ9pL6k_RcC3YI0Qm7qKDXI3XRttxc3YNlvCZVAgge5U0Pm6wMyQVOKxF7vfAc_Aya8Mpik2WNKDtOKnVmMGEcy0zF_W4ITRh0EtQ8bKNRr1lqiue8curyyo2vDoE_Zo0d0iZRXPwlzP_x0R4V5P7BIY_UbYGD3lmf4Sir0r0jhES_TZUHodH5QXCo3R6ZbDKQcfQNejVuze5lF03608mBrl2bcET93aMjiy2Ei_aRrkg0o8d38wm3E79WvDrZ1j_MRyvDENirwO6MiPF452FeBlJAjfKwmu9h2PFP2npXiSIBBEWl3o3TrEkxj08QpNspTPw-GqZtoHuGy7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
امارات خواستار توقف فوری تشدید تنش‌های منطقه‌ای، بازگشت به مذاکرات، حفاظت از کشتیرانی در تنگه هرمز و پایان دادن به حملات علیه زیرساخت‌های غیرنظامی است
🤟
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68503" target="_blank">📅 01:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68502">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرنگار: ایران اعلام کرده دیگه به تفاهم پایبند نیست نظرت چیه؟
ترامپ: خب بتخمم
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68502" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68501">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68501" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iIGejJH0P01GDeXzFjNhxXgBwSLhGciCVBNU-FiucVoTPPA6sUKidvn8Q83nwH9SCnilG6guXHFfliDwDoLBBbaJL4PPXrZpeXftoFhh4qxcuZNlkqqRPZFWMrW9EpMEhrzBeDNf4RsMPbkHS896raGmYdhqiJMvLH25we_vSI3sNpkoCeKTbcSy5Sk9Pya8cWTZntOroAaqCn1cvuCRcW2aQp6MrzBR9teuywXCzCWzAKm644KjpnuMiHKOW2eYX1BqTjKQQrSVrg1Yx08OZ3DaEduV0cCQlvSss05mlGU5j9L1SqplK3rebSM3gjEjbXBWwInk4ENies3a1Gg5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_e_ST1FyYhJ5wn1FBsspwaL0X8au-3-LGSV4Mi_xlQVq1pEXvMB5KfZ37OgijhRorn8XjPK9Buq7WlbyZbF7M1jTAjN41Zhl7xB4_-4iAQxDaYlvs45vrH3yHEJNpPgjZ3I9Nut0_X2VYcogQjh5xLv9IUICbLR_JQpKvb5gk62UVqKuV_DaSKVdyuU9E1ZNVikMlBYMlIW_nUyod0mZaXgJzzhZUxXeBPv2zQQGaPi9_hCeBb1QBfEGREBfV1JSUw9D7z2VN5pGCu_iNmiP3XMlqDzNXBZ7ZkTNzmmVRJRTyfbC1QKCSyT9ti3uaTF8MVp5fWqKceFM5SksWlbrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68499" target="_blank">📅 01:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsSevSUeOOlWns3TnPdcjPEfwTJl5dlL73Rl_vPekdsPu3yQpmUeHrCo5AGQCta1eE-v3iXkh0Cs-PpT-UFOZJJ5zmegSXv7FisjzlXhe2qc0eDgWissn_oupEkZQsbmO4_EE6xXrGiR_vo94semE8OT_kuckQq-ETlnCglWHMOc_KIaLPeV6mR4brT9BzUgonT8x4IIAjwO4XHp5_qBTL3J7ExPmS9Q0UryeNk7ERcN6GXexdUMWo3JgaxuxFqZSDIaydx-v8NJKCRXQz0ZvogoTJpkUQfSYyGPzF4Ow07C3hFlRRniuQORgg27-IWtJjXLAEjhWCToVS60UiZzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
دونالد ترامپ، رئیس‌جمهور آمریکا به «نیوزنیشن»، در واکنش به کشته شدن دو نیروی نظامی این کشور در حملات ایران در اردن:
«بسیار غم‌انگیز است؛ اتفاقی بسیار تأسف‌بار است. ما از وقوع چنین چیزی بیزاریم. آن‌ها در راه خدمت به کشورمان جان باختند.»
او بار دیگر تأکید کرد: «ما هرگز به ایران اجازه نخواهیم داد که به سلاح هسته‌ای دست یابد.»
ترامپ همچنین اظهار داشت که برایش «اصلاً اهمیتی ندارد» که ایران اعلام کرده دیگر به تفاهم‌نامه (MoU) پایبند نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68498" target="_blank">📅 01:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVpHRX3XcRuSYrKfbQ7ilPhCZnijBjA7aCApFeJSRvSaMQP858R_AkyzzNbK0Pja7jvkgZzyj-rtXrrlXS6Ug6x2M6bVfYHwM2Od7Uf0mgq8UNpZ5hPsUdqYSebKZlbZtLCe63nSPZLvLrrDjwAvzI78INJXhEQ-8lp6wwVsFbt3ywaLJa1VQNushHuHY5McK8OynPycK-j57egNBChK4jvYNT7ROFfRGlqHipS725hI24hAge7hAtVBCSnBKWJZFGXlVDUXm1kcliYQ61uhangugpPYs5JD0lA2vUvNwT-g0z5aX3U6eTM7SIyZ6YrohbHGb41FgUkbvmQY2-hiVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه المیادین گزارش داد که در پی حملات ایران در خاورمیانه طی هفته گذشته، ۳۰ سرباز آمریکایی مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68497" target="_blank">📅 00:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
بندرعباس زلزله!  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68496" target="_blank">📅 00:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
بندرعباس زلزله
!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68495" target="_blank">📅 00:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdAYU40XmOvy7VNjk3fGUZ0_S4P48IHNhHshQ-VQtEw7wra8u95ve1Tux58LEpwLNR8KQaR-LWD2gl23oSwuoMI_QZ43fG44bIO4Jayh-QyG0aU70WpHn_gY7KGm8Ty785G01NHyj8M836SG228nciSlNdB7ykK7fmVaZXa0jlBJavIN35uA8ict2_2P6MVkhW3L1cQ2BWl9_BIAUibnqZ5YBAXljZvNMP8lSGG0C2lLVD70yI6YlSQ4clRruK_hAdn-fDP1aYDOCcGRMj7YFgPqztrrSSzwSp7M_tN8Yf_5WECpJ1e2hbqhLJC_1uUes22__W2xOnUL4AqINSyEMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز: ایران در طول پنج روز، چهار حمله علیه نیروهای آمریکایی در اردن انجام داده است.
اولین حمله، یک مرکز مسکونی در پایگاه هوایی شاه فیصل را هدف قرار داد و تا پنج سرباز آمریکایی را مجروح کرد.
دومین حمله، یک پایگاه شرقی در اردن که توسط بالگردهای بلک هاوک آمریکایی استفاده می‌شد، را هدف قرار داد و به چندین فروند هواپیما خسارت وارد کرد.
دو روز بعد، موشک‌های ایرانی به پایگاه هوایی موافق سالتی در ازرق اصابت کردند و حدود ۲۰ سرباز آمریکایی که در پناهگاه‌ها پناه گرفته بودند، مجروح شدند.
یک حمله دیگر در روز جمعه به پایگاه هوایی موافق سالتی انجام شد که در نتیجه دو سرباز آمریکایی کشته شدند، یک نفر مفقود شد و چهار نفر دیگر مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68494" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68492">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7u1zb8qO1HMWLj5FBhcBPvdZUdMaMQ7_bSQrUvCKs56tRRnUbPsTvvDEbKhpa62h_FIqsW1j1XCn_nfpoOxW1niaJKbSjimaJnxukXIWpD5jktSLvooSf6tM6-9Th08PmCSmsU8nLSrZ5IYGBewAvjEuSjJQ9fopxeAOKmG9EbARps80ukQbrnlGvNtM_IsnZTMHVuCFf5BAJrE1tI0dwIelIs_9wN2n_E8ew_W9F7v3V0HTtlS0WqDUdWRW3OEUI-kNTnCFk9nVMlnWfqLeUyXGQYv-dJjyg3sem7yW5rUCVHBiu-3rwGMAZ1jz3DsW4tf-hhnwWYyqH-1PuCWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیومدن؟
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68492" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68490">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B4UaP-a-7-FET6RRB3REkGIPkImsiNaIGnDzu0-eaIhoDRGY3VdRFj-zEdzyACEiFcDNpiTRJmYmzCzb9yhbv0HyClZq0W8ZuKM5YNr4oJiYyrXJ1Z7g3c7wXDlK5JIBKLrtBvKgTijEXjC4CCbVrnr2Ng1j5VcVHJ89YAtEnVGb55Z_Y2x82wFmtQ_sE9JZ0MNYliYq4ANVL30zxNAy0Ms7IJN2U4BXrMFhG5Yi6S5pOiUFSttGE6jSiy04SjBfrJiLTgsEYTZOSkG09PiQtVDDrYpwHlfUDpcypAQqRQJXQ4Kfs4vRi-lISuPdjWHFxyeF_Omh6pGlgqlDiq36rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PcFYj9sHdtvCiyOEc9DNRqVTvlbmR-cMiLJkSNlN7QXKRCEWXRdgGBDoE6XWq1HzaJ9bF8r_jzArjJ1V_kBwXGOjgNymtTlMdLQYEeTtdMytQAEDazZ9cJFUelbUmW6gyLCgJdege0u2aoeG0i0uTEABhqcRUR8y_OitPF2L5tmcd1o16AxusEC23Z9YGkTBBPbsuihYdfYsIpuQT3fD3QfUqjmps0Q_57rej91MMI7AXdZpZxeoosw_J3YS6mNFWGchcH6G1Lmyb7PxpVP69_i0O_OKdaBCZOLZluxeZdf_3doGvggzQ4UCGlhwvc9OIJYW-SvfPOOovhnRTFC3VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیلی افشار دوست‌دختر سابق تتلو و پویان مختاری هم این وسط تصمیم گرفته پورن استار شه و یک کانال زده تلگرام که ورودیش 2500 استارز یعنی معادل 8 میلیون تومن پول می‌خواد، البته محتویات کانالش لو رفتن و کافیه کلیک کنید رو لینک های مدنظر پایین :)))
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part2)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part2)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part1)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part1)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part2)
🔥
🔗
مشاهده ویدیو های لو رفته جدید
(Part3)
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68490" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اماراتی های کاکولدزاده خواستار پایان درگیری ها شدند
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68489" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68487">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=DE4jzkoee16YgyLFDhw4bqbLEyb1AmPeENSe5uChCtnOQLir1sTNd6B_fehekkk2nZyuVDniwggkeeo-VKGsaIHGujSuLJQOFKKYFZ7CXBrYQSUnYOSIac9wxQkgRh85tcn-1v7kdQsCbZSZ6FV6tzqbsJwKyaaIs3DMviGsov-cpfBZDCdNqe1opII6ShRR_TbSu76_BWaVlZmDS4ljhl9RGl73WxBGe1Dcgp2e22-sZF45Kit7VulSrMWUsiZpcIa7Fd5J4Hp_eFOWlEQ5JfGMzm-LIYkpnhg5jYQHquMQ0kIdr9uU-YjnJQEZdZ4ASvvxmwKGyQMqe6tA-aJPSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=DE4jzkoee16YgyLFDhw4bqbLEyb1AmPeENSe5uChCtnOQLir1sTNd6B_fehekkk2nZyuVDniwggkeeo-VKGsaIHGujSuLJQOFKKYFZ7CXBrYQSUnYOSIac9wxQkgRh85tcn-1v7kdQsCbZSZ6FV6tzqbsJwKyaaIs3DMviGsov-cpfBZDCdNqe1opII6ShRR_TbSu76_BWaVlZmDS4ljhl9RGl73WxBGe1Dcgp2e22-sZF45Kit7VulSrMWUsiZpcIa7Fd5J4Hp_eFOWlEQ5JfGMzm-LIYkpnhg5jYQHquMQ0kIdr9uU-YjnJQEZdZ4ASvvxmwKGyQMqe6tA-aJPSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایونت ورزشی، ۲۶ تیر؛
پارک پردیسان پونک
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68487" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68486">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام آمریکایی به شبکه NPR گفت:
«رئیس‌جمهور ترامپ دستور داده است که فرماندهی مرکزی نیروهای آمریکایی (سنتکام) در ساعات آینده، «دروازه‌های جهنم» را به روی ایران باز کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68486" target="_blank">📅 23:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68485">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=aM44CdhgQpmitNnfHw5DPTKUxDGQOswF9-6KGze4hv3yoAr6Eh5M0LAAc9oYF_93gGdmxMIANBtyFiKkIvhYXD8LFeM5t9W7f0bQqZeBspp7fwHfW7hKsUJCt3nfsEyiKqYyNmfDJ_3_ZHdj0bvzOOJnw5zhrJ1lk8iZPuXOHBbC-EwmQLAb_jXwM4VHDLMYiYOVE76RJM1NGBxDIHZb8JV9nj-d2kXAPKQBHYi4GPllb_v5q8L9VlKsfW7XMz29e4gY603uqhyqzMOUikGJWfZ7BRs23hVJ9d2EsGs-Fzx70x3grCaMJzNi6-ILQ6SIrooDLGiP12rbHt0JYjQVng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=aM44CdhgQpmitNnfHw5DPTKUxDGQOswF9-6KGze4hv3yoAr6Eh5M0LAAc9oYF_93gGdmxMIANBtyFiKkIvhYXD8LFeM5t9W7f0bQqZeBspp7fwHfW7hKsUJCt3nfsEyiKqYyNmfDJ_3_ZHdj0bvzOOJnw5zhrJ1lk8iZPuXOHBbC-EwmQLAb_jXwM4VHDLMYiYOVE76RJM1NGBxDIHZb8JV9nj-d2kXAPKQBHYi4GPllb_v5q8L9VlKsfW7XMz29e4gY603uqhyqzMOUikGJWfZ7BRs23hVJ9d2EsGs-Fzx70x3grCaMJzNi6-ILQ6SIrooDLGiP12rbHt0JYjQVng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که دن اسکاویینو، از مقامات ارشد تیم ترامپ در پلتفرم ایکس منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68485" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68484">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68484" target="_blank">📅 22:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68483">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇱
نتانیاهو شیرِ یهود برای آرژانتین در فینال جام جهانی در مقابل چپول های اسپانیایی آرزوی موفقیت کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68483" target="_blank">📅 22:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68482">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68482" target="_blank">📅 22:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68481">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ پیت هگست: خدا نگهدار قهرمانان؛ فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68481" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68480">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖄𝖚𝖘𝖊𝖋</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=Cns9zVDr_wy5CatTwSO3c6OagAzO8uCFcCw_WzA1iSJwT43e0BerRf68UQxUv0qfUVw7Ru8ipjKWm47nc3wnw1UKEGFp-qlTaV_TVBe1Bar2UlKJOyGwavUxhTZ3eMyTvgHJ3miTv0fv2vO8Av63z2dt4shj07E_lbBz1bvmuKdalIqOkksRJ2-yVBr-J7itW09TaFuLYMMcqtrcR7IzMqtwRzPDkPcx5vIeSh7T30uu3QmP11cyJ5Sm2-Q1GXmHmgu2q9vsUhrpkwmkzZyulS-5VcAtwBCqQ2lto9mJnEJoJO82xmD0qXvpuJnfmuctlWIQvCfurfBVUzBTful_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=Cns9zVDr_wy5CatTwSO3c6OagAzO8uCFcCw_WzA1iSJwT43e0BerRf68UQxUv0qfUVw7Ru8ipjKWm47nc3wnw1UKEGFp-qlTaV_TVBe1Bar2UlKJOyGwavUxhTZ3eMyTvgHJ3miTv0fv2vO8Av63z2dt4shj07E_lbBz1bvmuKdalIqOkksRJ2-yVBr-J7itW09TaFuLYMMcqtrcR7IzMqtwRzPDkPcx5vIeSh7T30uu3QmP11cyJ5Sm2-Q1GXmHmgu2q9vsUhrpkwmkzZyulS-5VcAtwBCqQ2lto9mJnEJoJO82xmD0qXvpuJnfmuctlWIQvCfurfBVUzBTful_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش پیت هگست به کشته شدن ۲ تن از سربازان امریکایی</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/68480" target="_blank">📅 22:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68479">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=NqCE80rU7t0igNFrEIPDaxLlgvTb1TMUmJ2kTxQAReZsvo7CK_5OeywAWHHdgzPoNyJMwwFjLUHakbURnUR_-9ymLHimvoJOu-3BbXyQFuOg5Pl06zrx94w5Ua7OhJOtvtLnf-6ZNSp52JKjWw-WVUOIobWRAksbpilJNbxCSFumJEh6disNUihiLwfoSLHS-MEsRalBQRyAVcTxMoGR3IPteNQnPfhk-UxY_yyJhTsT4AqWGzkuzL1frfL_eVcejmsqyAwGjGz-JRu2IYWJsHRnHvsW2gJHq6ZhJ5Pp8kGCt0RK_Dgn8tW2dMJKJ2IOM0UIM09_9_tz9ZqKn9etuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=NqCE80rU7t0igNFrEIPDaxLlgvTb1TMUmJ2kTxQAReZsvo7CK_5OeywAWHHdgzPoNyJMwwFjLUHakbURnUR_-9ymLHimvoJOu-3BbXyQFuOg5Pl06zrx94w5Ua7OhJOtvtLnf-6ZNSp52JKjWw-WVUOIobWRAksbpilJNbxCSFumJEh6disNUihiLwfoSLHS-MEsRalBQRyAVcTxMoGR3IPteNQnPfhk-UxY_yyJhTsT4AqWGzkuzL1frfL_eVcejmsqyAwGjGz-JRu2IYWJsHRnHvsW2gJHq6ZhJ5Pp8kGCt0RK_Dgn8tW2dMJKJ2IOM0UIM09_9_tz9ZqKn9etuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه اصابت موشک‌های بالستیک به پایگاه موفق‌السلطی اردن که گویا منجر به کشته‌شدن دوسرباز آمریکایی و مفقود شدن چندتن دیگه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/68479" target="_blank">📅 22:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68478">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پیش‌بینی می‌کنم که حملات امشب، از دیشب هم شدیدتر خواهد بود... #hjAly‌</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68478" target="_blank">📅 21:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68477">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">همونطور که پیش‌بینی می‌شد، دامنه حملات امشب گسترده تر از شب های دیگه شده و حتی حملات به یزد هم کشیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68477" target="_blank">📅 21:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68476">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=bY5mj7Tasyp4A4eUGMfEp1SoCx-ONHCadS6MMVQl1V_AfAYjJl1D1wWHShhd0RAvwBVKdNxElXt-61Pxi3xP6AZFBLqqumWk6Lyws35i18W2Iw71SIfZTG6kt2M1AqlV4Ha4CvdDlaXTRRFqIv_CMG7gtZqpMJCmhE1K3nE1tB1CoRq4pSuuWvDOXBy-7Bxcfh25k_XmyxuyW6_NbsW0fatnrTwPRDIlKZlzl2MZO8VFgVYk8VNp4Wh7rOMQZh-zBdEzG4-WASRT4T6qgITDzz7bCcqE3--pzxFBf55gBtHXgxh6sIHsBfOqnchdOcAkxg4VtVKwAhm1LaYbvf-rtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=bY5mj7Tasyp4A4eUGMfEp1SoCx-ONHCadS6MMVQl1V_AfAYjJl1D1wWHShhd0RAvwBVKdNxElXt-61Pxi3xP6AZFBLqqumWk6Lyws35i18W2Iw71SIfZTG6kt2M1AqlV4Ha4CvdDlaXTRRFqIv_CMG7gtZqpMJCmhE1K3nE1tB1CoRq4pSuuWvDOXBy-7Bxcfh25k_XmyxuyW6_NbsW0fatnrTwPRDIlKZlzl2MZO8VFgVYk8VNp4Wh7rOMQZh-zBdEzG4-WASRT4T6qgITDzz7bCcqE3--pzxFBf55gBtHXgxh6sIHsBfOqnchdOcAkxg4VtVKwAhm1LaYbvf-rtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
یادی کنیم از این سکانس که ترامپ چند وقت پیش در تروث‌سوشال پست کرده بود: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68476" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68475">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:  در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68475" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq8WtkeTD6UK-NmNyYTGpgYHVdHBU1-R7BZMhdWEU-LW2ztDXVovElvgIuPDFaESq-ylA9YnaKRB7xVJjvJsVmT5xQetUt6V2ub9pYs9ixrnm5PSldbEbLvutFVjm7FBHtKlh37QFt-DkxsGejzhqUy51zdJfH4CwqgJSV_m7zLLYq2yjM5o4gZf6Nr7HIS066nkJVNIEAUX917rCaH-nPMMqKWWxQtPcSEJMmF7B2vgmJxnjX_O57jVOMRTqgH1pAH5zNCjvkDQwdmBYFuY7Mp0jfTRFhwBmnWt5XjC-rVBTjBxU_uMBWSjs1-t3kzYeVz-pJLZwuSfRf9UWJeJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.
همچنین، یک نیروی نظامی دیگر در حال حاضر مفقود است.
چهار نیروی نظامی آمریکایی برای مداوا به بیمارستان‌های اردن منتقل شدند که همگی تاکنون مرخص شده‌اند.
سایر پرسنلی که به دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به محل خدمت خود بازگشته‌اند.
سنتکام به احترام خانواده‌ها، از انتشار اطلاعات تکمیلی — از جمله هویت نظامیان جان‌باخته — تا ۲۴ ساعت پس از اطلاع‌رسانی به بستگان درجه‌یک آن‌ها، خودداری خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68474" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=oGZmPTREtTvhF7cT4LeMNiUsscGV7NvS1CZyy6G4f8Of9t5ZL2tufwn6fj-4mql6a8mDDlx6mDquX9f3H2dyXHMLwL5lqB1SYYv-LXRirtJ0_N_3IfPUcHIZoiGGwblojOPdz1UHoMrED97RZsSwVzXTn9zRqFAhZ0vBlSyY8Ez7YCDT-CI_SHrideeq_BEty1FJ3VNQ2TzAdASFOrXrmv-iJPtCdTfX87ERhQ9JDBcWuaVMvAOE3FNBA3_O2OPhE-9cqP_XXiu7lBv6wqmOde6TDRLEFVJAna0jxAmYd0Pa03AFfckPvnVJpFlhSSXHcuIzFoI8VnXNOTKArYDktw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=oGZmPTREtTvhF7cT4LeMNiUsscGV7NvS1CZyy6G4f8Of9t5ZL2tufwn6fj-4mql6a8mDDlx6mDquX9f3H2dyXHMLwL5lqB1SYYv-LXRirtJ0_N_3IfPUcHIZoiGGwblojOPdz1UHoMrED97RZsSwVzXTn9zRqFAhZ0vBlSyY8Ez7YCDT-CI_SHrideeq_BEty1FJ3VNQ2TzAdASFOrXrmv-iJPtCdTfX87ERhQ9JDBcWuaVMvAOE3FNBA3_O2OPhE-9cqP_XXiu7lBv6wqmOde6TDRLEFVJAna0jxAmYd0Pa03AFfckPvnVJpFlhSSXHcuIzFoI8VnXNOTKArYDktw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
اگه حملات آمریکا تا چند روز دیگه ادامه پیدا کنه، وارد مرحله تهاجمی کامل میشیم
اون موقع دیگه فقط جواب حمله رو نمیدیم و حملاتمون گسترده‌تر میشه همه جارو میزنیم
آمریکاس که ریده به مفاد تفاهم‌ نامه و همرو یکی‌یکی زیر پا گذاشته و عملا از تفاهم نامه فقط اسمش باقی موند
آمریکا از جنوب لبنان عقب‌ نشینی نکرد، توی تنگه هرمز مسیر غیرقانونی ایجاد کرد، به حاکمیت ایران احترام نذاشت، به سواحل ایران حمله کرد و اموال ایران رو هم آزاد نکرد
دیگه نه روی کاغذ و نه توی عمل چیزی به اسم تفاهم‌نامه اسلام‌آباد وجود نداره
اگه دوباره مذاکره‌ای شروع بشه، از طرف آمریکاست و اونه که دنبال نوشتن یه تفاهم‌نامه جدید با تغییرات تازه‌ست
اجازه نمیدیم نیروهای دژمن از تنگه هرمز رد شن و وارد خلیج فارس بشن، چون امنیت کشورمون به خطر میوفته
🌅
قبول نداریم آمریکا توی تنگه هرمز، که گلوگاه انرژی جهانه، نقش یا حضور داشته باشه
آمریکایی‌ ها منتظر موج موشک‌ ها و پهپادهای ایران باشن چون ما جواب حرف‌ های ترامپ رو توی میدون میدیم
فعلا سیاست ایران اینه که هر حمله موشکی رو با همون شدت جواب بده
انتقام خون فرمانده شهید و شهدای جنگ رو میگیریم
آمریکا میخواد با محاصره دریایی، مقاومت ایران رو بشکنه
ممکنه دوباره به سایت‌های هسته‌ای حمله کنه یا بعد از اقدام نظامی، ایران رو به مذاکره با شرایط جدید مجبور کنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68473" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68472" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68471">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=TBNgKSY_jEzBqVYoXLLauhTqn7-zrzmeTAAZEEc7Vw-QpH3ZmXe5LF3G3r6azNpE6WoQXm_E4r0VPgECapZGEbSIHxWfCQCoxAaSCpFJXyDodeIuechBfJyBA00KfXNqPMMF5WTm-mvot9XYJepSzctEjtkFPtlM_TfTeeXQNs3kC-LP5kXeiKnlTq7nu63zoB2MCx2CMK5KSZf3HTbDvolOrdXeRFSQetoEigKt_z_Cs2qR05ajqbXAz_9B7CXw0vMuj_1LqB9gxUfbTyllhFmlhcEWCBrhIz1kKMBCw-2cpkD9xVV0dNBAakC_RnecGJyG6EZkZguXTe21IdlNaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=TBNgKSY_jEzBqVYoXLLauhTqn7-zrzmeTAAZEEc7Vw-QpH3ZmXe5LF3G3r6azNpE6WoQXm_E4r0VPgECapZGEbSIHxWfCQCoxAaSCpFJXyDodeIuechBfJyBA00KfXNqPMMF5WTm-mvot9XYJepSzctEjtkFPtlM_TfTeeXQNs3kC-LP5kXeiKnlTq7nu63zoB2MCx2CMK5KSZf3HTbDvolOrdXeRFSQetoEigKt_z_Cs2qR05ajqbXAz_9B7CXw0vMuj_1LqB9gxUfbTyllhFmlhcEWCBrhIz1kKMBCw-2cpkD9xVV0dNBAakC_RnecGJyG6EZkZguXTe21IdlNaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68471" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی مبنی بر وقوع حادثه‌ای بین یک کشتی تجاری و نیروهای نظامی، در فاصله حدود ۱۰۰ مایل دریایی به شرق شهر الدقم در کشور عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68470" target="_blank">📅 20:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
تفاهم‌نامه بار دیگر ثابت کرد که امضای رئیس‌جمهور ایالات متحده هیچ ارزشی ندارد و هیچ اعتبار ندارد، و مردم ایران درس‌هایی فراموش‌نشدنی برای دشمن آمریکایی دارند.
امروز، "شیطان بزرگ" بار دیگر بدون هیچ پوششی، چهره واقعی خود را آشکار کرد. این تجربه تلخ از جنایات و نقض عهد، مدرکی جدید و قاطع بر دروغگویی، بی‌منطق بودن، عدم شایستگی اعتماد و فریبکاری ایالات متحده است.
اکنون که دشمن آمریکایی در تلاش است تا جنگ را شعله‌ور کند و هزینه‌های گزاف بیشتری را متحمل شود و اعتبار خود را بیشتر از دست بدهد، باید بداند که مردم عزیز ایران و جبهه مقاومت، درس‌هایی فراموش‌نشدنی برای او دارند. در این روزها، شجاعت رزمندگان اسلام و جوانان مناطق جنوبی، نمونه‌هایی از این درس‌ها را نشان داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68469" target="_blank">📅 20:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68468">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای ساعت ۲۰ پیامی را منتشر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68468" target="_blank">📅 19:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68466">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
هم‌اکنون زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68466" target="_blank">📅 19:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68465">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pr0uwYUZ2suFYvdN-_WhNoz5Q_FU83lMHxfj3PaPpM1eeFE51SuOgcMnCqK-qu6-A781dFm0yW5gTEkdyq3RQ4Hgduj8hPgTzwg8tKVmsPzHHJfpRvIgJ9zakvuuJHaErLvglDNW8brqYHPPa6-JW0OXHoiP-MAv2TU6aZTix6axoONhZ_OVimZKlK76q0jVFvVbNuEFBfQYrNUYBdGY-yXV4jmCA_IUv13QMWKK-vN-ZZ1IOVM0XXRwggGVqe4cehlR5dbRRVgj6OU2xW3R4QF0tFJGyWsyNvAq7BYDFMM8KNONKtxy3QQDDsfU9xyokD9_Vv8hIOwSm0yaX7_p6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68465" target="_blank">📅 19:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68464">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68464" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68463">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=vitlpCnnv5Mg_mic6mM87Nukv5UlHG--f3tn8AKXU0Zp-z1rjwN9Yj_MgjpbCOakE6opbUeCbSGwoLWy30YYYQs2BLaIOOiPFoD40ManaliEjoM-eD7Whf6mLN5NXoYhIf1At50-gaymsQqlzDVG4YwQyfyk3p9eE-8rACvT2UcrlWL2VvYSA476s8TpB5L37WmjfTHFXQprEDwrZVN5vz0w4YvkYq23YG7KZjIIVRq7-9ljDvqAfg0dVGHmiT7XqC3NRF_AFNmfF-Mf1G9w8it0Hd97CxISHqgaLzr4qbXcAiyC5t7SxR-fnKn5XybnERVj8axikqmRqRY3Hveqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=vitlpCnnv5Mg_mic6mM87Nukv5UlHG--f3tn8AKXU0Zp-z1rjwN9Yj_MgjpbCOakE6opbUeCbSGwoLWy30YYYQs2BLaIOOiPFoD40ManaliEjoM-eD7Whf6mLN5NXoYhIf1At50-gaymsQqlzDVG4YwQyfyk3p9eE-8rACvT2UcrlWL2VvYSA476s8TpB5L37WmjfTHFXQprEDwrZVN5vz0w4YvkYq23YG7KZjIIVRq7-9ljDvqAfg0dVGHmiT7XqC3NRF_AFNmfF-Mf1G9w8it0Hd97CxISHqgaLzr4qbXcAiyC5t7SxR-fnKn5XybnERVj8axikqmRqRY3Hveqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
این ویدیو کامل نشون میده که تحرکات هواپیماها های ترابری امریکایی از سمت اروپا به خاورمیانه بشدت افزایش داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68463" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68462">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFP2cvLSOzIi3wf-YqttS865VslZZEvzYrdcsZ5czu-PrfRs0ZrBdV6Zowid9OX75byKFFSlivhoNXMok1ZHl0eehWD22UfhlWeOIWphMvFqRFfJSxu-JH3GrcjrhuEz_felqcDqkdJAbvtZZ8eqA2nUif-f6h2V653IKhrYdNOpkCibRFKErNXoib43zLu_n7EODF7aI2B_11jWQXeF_5uGbZZCUm6A9U2D_xNZScdKNogNlwBnLlaNXDbfSaojQkuOZQFsro3qg_fc7E10qdgKv4RRoEBg38DAPpQMxUoTqSmPoGhbVOkC5S5kA2qwhX8lgoOPxXQXPs6-X-wltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز چندین جنگنده اضافی به پایگاه‌های آمریکا در خاورمیانه اعزام شدن و 4 فروند هواپیمای سوخت‌رسان KC-135R هم اونا رو همراهی کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68462" target="_blank">📅 18:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68461">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGfbaiSfYCrK2qRFJkgkLtwMD4w2AoWtOQC5pZFUc8Ia1FVRnpeBmWzCnSHyXT2wyqOgqjEK16eaKNez1dJAo6iMS0ZudnyABLuFr7Ixw9qJQcb9WQIl86XAz_6XYH7Xjqw25d43Fx6kQFOrYNp4kOccyJn2ZUKHw4XUSAUubqc5-qnKqD0ib1jHqbsA7Q5oyYHsrO-12QYG56xdA19IqMUDIV6ptoEF0FXtiC00JjHQrLWCvzHo9TF52EYQC9Ybyy5K0W2EFtpALSUa_FUCJxVjCdNxxY8OIRiTQkjI3iLhmx5hdnj6Lyym4-Kwa3zYebbpZoEn2jAb7I9L1Q0BUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نماینده مجلس:
بنزین گزان میشود؛لیتری 10 هزارتومان
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68461" target="_blank">📅 17:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68460">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:  «اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68460" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68459">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:
«اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68459" target="_blank">📅 17:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68456">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=PrBz7HHBvESl30LW1y40HkhKYotiMg1CGnqbPW7oSgI8K-BZcwgm86M9d4qvjP7wPpaNEu9Ii4xeWx_-LzVUWlfniOhjvzXWLtppCw0JSjNEGP3AAxcnSISsx-qSvhvGLaqBdx7BdR0VrBC1WjLx8IKqSwy3oouD4pDOfyzd4gyuftB9ovrKO2728ds3sF81K8JuGHsgU9jgJ9V5qHhzxE-4jOu-G81HwU6AzkvNiGZ8WTtVfjM2cNhgRGQUCRHZqEocOQcKb-NEWl-kTN51xZhY_KrtVOpjT4fStzsOCpK4SCRQ9lB6RdyicmJVHtvOB5P0nWIwuwbT52lfh9F_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=PrBz7HHBvESl30LW1y40HkhKYotiMg1CGnqbPW7oSgI8K-BZcwgm86M9d4qvjP7wPpaNEu9Ii4xeWx_-LzVUWlfniOhjvzXWLtppCw0JSjNEGP3AAxcnSISsx-qSvhvGLaqBdx7BdR0VrBC1WjLx8IKqSwy3oouD4pDOfyzd4gyuftB9ovrKO2728ds3sF81K8JuGHsgU9jgJ9V5qHhzxE-4jOu-G81HwU6AzkvNiGZ8WTtVfjM2cNhgRGQUCRHZqEocOQcKb-NEWl-kTN51xZhY_KrtVOpjT4fStzsOCpK4SCRQ9lB6RdyicmJVHtvOB5P0nWIwuwbT52lfh9F_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی در کویت به دلیل حملات موشکی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68456" target="_blank">📅 17:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68455">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUNQ2FqP1ymB3XogIDIC2WA4kMEbqae5DZtlmvv16RHsc1jSPCEcJrVqUl6OnfneDoiWTYlyWH7bIXTle342z2Ze-jPAh6Ei2s5B4FgNh9Ra9PS1t_PWnfrFuFwECKCqCGrRNOFexBgRvcPWoyQmkk2fghZZ05oG0I-J7sDEDPWXttrzL83bmgM-iO0svIePok55y9xDwWYjRHQwGtjxc3727sj7ix1CwHu0tQU4dwL97kHS1QTZdfW-pi2mTJn0thMcnj_4-l9I5tejnDTCsOzL-C5xyYD65vWBDbNGO-VFa-y31tfrVPJLATFqB5D-lxxZKTx2Ygevzyb9emBYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛معاون وزیر امور خارجه جمهوری اسلامی، کاظم غریب‌آبادی:
«از این لحظه به بعد، ایران اجرای تمامی تعهدات خود را بر اساس یادداشت تفاهم، به حالت تعلیق در می‌آورد.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68455" target="_blank">📅 16:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00f574479.mp4?token=t8ki37-3StpYVwrxiIqADvLo62WYmBlIqGooyqFUc13uScZi_fIO4XXuIQml5q1QuBbsT1u4pciwojQ397XnhWO5CjOANB6G2DZvjvUCKxs5Nnf1jK4bN7I0_Tr9f_-ajil0xj3Bwq86x_0s9J4_logYznonfr3HSAhm7CVcFsiyRWvRpFpTbzarBDYBwfLQRd98f4CqQZ4IG16w3mZaC1EYtR2LZ6OufliC2VxLLDgdvPo1vj_l_S7-8cWr187-0LBsasMitzX-Jv01B1b_4uXEYVsLKR0zwbmoewdMySWi7Nh8vu3YUd4pl9nyA5Gh3VgwWx2JyzWPTE-9yaELVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00f574479.mp4?token=t8ki37-3StpYVwrxiIqADvLo62WYmBlIqGooyqFUc13uScZi_fIO4XXuIQml5q1QuBbsT1u4pciwojQ397XnhWO5CjOANB6G2DZvjvUCKxs5Nnf1jK4bN7I0_Tr9f_-ajil0xj3Bwq86x_0s9J4_logYznonfr3HSAhm7CVcFsiyRWvRpFpTbzarBDYBwfLQRd98f4CqQZ4IG16w3mZaC1EYtR2LZ6OufliC2VxLLDgdvPo1vj_l_S7-8cWr187-0LBsasMitzX-Jv01B1b_4uXEYVsLKR0zwbmoewdMySWi7Nh8vu3YUd4pl9nyA5Gh3VgwWx2JyzWPTE-9yaELVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
چند روز پیش یه ویدئو از یه پسر نوجوون وایرال شد که از سرکار اومده بود و داشت موتورهای یه نمایشگاه رو با بغض نگاه میکرد و حسرت می‌خورد؛
⏺
این ویدیو خیلی دست به دست شد و نهایتا مردمِ نازنین ایران، تو کمتر از یک هفته پول جمع کردن و واسه آقا یاسین موتور خریدن و اینجوری سورپرایزش کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68452" target="_blank">📅 16:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون جنوبی:
همه دارن از جنوب صحبت میکنن که دمشون گرم ولی منی که خودم جنوبم نمیدونم چی بگم.
درمورد پمپ بنزینی که یکساعته داخلشم صحبت کنیم یا مثلا درمورد برقی که الان رفته و نمیتونم برم خونه صحبت کنم
درمورد ماشینی که نمیتونم خرجش کنم صحبت کنم؟
درمورد وسیله ای که میخواستم بخرم و امروز صاحابش 40 میلیون گذاشت روش صحبت کنم؟
یعنی حتی نمیدونم از کجا شروع کنم
ببین قبلا به موجودی کار نگاه میکنم میگم خب بعدا این چنین میشه اما الان تخمم نیست
الان میگم بتخمم ک میزنن نهایتش اینه منو میزنه و میمیرم
چرا برق بقیه شهر های دنیا نمیره برق ما میره ؟ ما اضافه ایم ؟
بدترین اب و هوا و اکوسیستم و بی برقی و جنگ مال ماست نمیدونم از چی باید بگم
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68451" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1r-lIbLa2OvUuuJYbSxn6FDSs-Ur6S2FV9xOJ2DZI66Qy6Xc2vhLkOkGZ8w1oEJ34dyBzpJw2lCpmYphrBvlCvNZ3wjMyrbwne78JYH1ZGi6Y1SEa7z1ovFGDB867KJOHkHb__D6JcQEuO41XLQsi7AYNbD3Cg1oKeNlj_FC2zPdULE5T4sQZaaNP7TunUzqjM_JPWURd9ZXDk6G4IWPNrkHYOxzZeeNYMdlxan9d-rNhFkNxhkX76qdj9bDCFVBr6NlR-BaP4LfV8K6o7uDkMHq6r3amk5WAYv8WFOjGbwzvkJHxIQFkAQbaufYIBb7ZbpHLAXSUpiHwm2bwvABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حکومت داره به جانفداها زنگ میزنه که بیان آموزش با اسلحه ببینن و برای جنگ آماده بشن
😂
😂
اگه کسیم بهونه بیاره که مثلاً مشکل دارم و نمیتونم بیام، میگن اشکال نداره، بیا آشپزی کن یا کارای دیگه انجام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68450" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=rbfm4-ejLHdY4Vnni7BI1Lg0t4UGlm443sMjBH4iaaJqeBPe0JXSaa3EoEwtp4wrlbEB48CJLiqP6xK1cUt1KI3Pk2KMgqNg2qHI1dNirNpoLE32u5KCCMIQL8VxveR-Ee_7Ra7zxulBAm4L0rrw4WNURGcanndA9_xs6gJPlHYvJsSYLQQWwt6w35S_v_CpVq5VpvkSSu-crUx3O6ubm3G6x7nzKblxe5whVauF1UqelAM39Kp60ImzCNX0ptwI-sxdUBOfuOov0tf0ZLdTXyiY3AEXcCTBZX328gBSSg1vVaPRwHVZ7umjeSDrzwvXd8Hl4-ets9VtIBul4O1nig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=rbfm4-ejLHdY4Vnni7BI1Lg0t4UGlm443sMjBH4iaaJqeBPe0JXSaa3EoEwtp4wrlbEB48CJLiqP6xK1cUt1KI3Pk2KMgqNg2qHI1dNirNpoLE32u5KCCMIQL8VxveR-Ee_7Ra7zxulBAm4L0rrw4WNURGcanndA9_xs6gJPlHYvJsSYLQQWwt6w35S_v_CpVq5VpvkSSu-crUx3O6ubm3G6x7nzKblxe5whVauF1UqelAM39Kp60ImzCNX0ptwI-sxdUBOfuOov0tf0ZLdTXyiY3AEXcCTBZX328gBSSg1vVaPRwHVZ7umjeSDrzwvXd8Hl4-ets9VtIBul4O1nig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واسه دومین بار طی دو روز گذشته، جمهوری اسلامی به نیروگاه برق و تأسیسات آب‌شیرین‌کن تو کویت حمله کرد و باعث آتش‌سوزی شد.
کویت حدود 90 درصد آب آشامیدنیش رو از طریق آب‌شیرین‌کن‌ها تأمین میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68449" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3Sy6Qm6Is6hmtwWUrOgoV7VuAjKBVgj7MP-SwaePix3V0b225Z_h_3xvXbSjF3Xh-vTNvDYQHXmvvyjvy-KZ0AjAGuthlxUQBnkt7xIUQTFd_hVoNS9CUa1oP6M4_k8lkq2UcfMyRbuvc_XQJoZuuRpe8pAOAuKuwXvn7VgwNqAao8HuJUtKqXKEzRswSPOJtMKRXpIpEXdiddl8ewHXoJtueNoxoTPUn1hlo5mlhuvg5ZU7_vu-s4JQWOFvPPt5R6CKhq2pHagBjh_7Y7vTkejYcoXf8b4U97pRTkCMJCRSwnPqayF13LDOzRViK1wAowjfKpftGpVbEqpbuQOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68448" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68447" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=jy4vK0f7kLHClN6QqMsjZ0I31yVWb-2Q40ec2xeBA-NAIl9ga_jCjBHDz3LTyiYEmjV3ADaoVxvfPMDlyEBLD-JgfVKLS29Y10_pgaMhZH06odZmJUxYSWFYIK6uAQAebfSBM5WnqruVHbpA5hZ58gCSZ926-YqEsQAkuj7TXRqxY1sjUSDQdeu7VG-l5fLK2YBEdGjc5Viw9Hqt-tRPPAN29OWgj5cHPaIftVBIK-3_aeEZ4cF6UBpWzv6d-XfQsuiaIQJpGUyUk6Hu2oj93ATzDgK502Jjk9g8s8Yu4y-povXKzN5ABayEmzEAHJmUlmiJDGUE8SWH1FmZna4Zsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=jy4vK0f7kLHClN6QqMsjZ0I31yVWb-2Q40ec2xeBA-NAIl9ga_jCjBHDz3LTyiYEmjV3ADaoVxvfPMDlyEBLD-JgfVKLS29Y10_pgaMhZH06odZmJUxYSWFYIK6uAQAebfSBM5WnqruVHbpA5hZ58gCSZ926-YqEsQAkuj7TXRqxY1sjUSDQdeu7VG-l5fLK2YBEdGjc5Viw9Hqt-tRPPAN29OWgj5cHPaIftVBIK-3_aeEZ4cF6UBpWzv6d-XfQsuiaIQJpGUyUk6Hu2oj93ATzDgK502Jjk9g8s8Yu4y-povXKzN5ABayEmzEAHJmUlmiJDGUE8SWH1FmZna4Zsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68446" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68445">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⏺
وزارت نفت کویت:
خسارات مالی سنگین در پی حمله‌ به یک تأسیسات نفتی‌مان رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68445" target="_blank">📅 13:44 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
