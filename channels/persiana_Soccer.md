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
<img src="https://cdn4.telesco.pe/file/gP7Gih_e1TfWC7ws5IrNMdfbarMNY8CbuOJ2deizAjVUQR_Xjf1bv-PDumnegGfyZ4VMQj20Qatd-PPyMjymY4vmltHDziOOEiW3KbcbA8KPW-WKt8Ap9Akx7pKOo6f6lB_mt2IQLg5l8Whn9ZoW8O1Ya4IPzwAyr4PVD_80QG2uKe8-JQ6OWjO3buC9-nZ3C7XV45n-8uxVnLv_Z5UzwwhjoSue5B9uhlrSZbQTDbXx-k-4f0N6mim2Hjkwlfy7BpywY9FseToecF6-KMEM9abKQaYGCcQVtj5ASh2TQVO_gNGOvA2Crj2PafftzmqAygWB-4eglPuCgBHCCe3_bA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 607K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 12:12:47</div>
<hr>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWBPoERA5RHWCmZ5KRHLDzEjgAvie0vWTca_FYAjC6bexW8TEF0gL6vb19LpnOCvUaoak8vjM9jiw2aP5m8-gzzcirBF3dMIl-DJs68nKQo7-zd-tuoAn8Pv1OASrZTv08cwQEsb4XGE4zGDIx0VmcNMrFhQ_dPAGMbfecxE_Lxj5yon9NAU-Gcis3G-59LZgrhYWCsm9s_86DdapHrdnAykb172em40fPrX_WPyrpMVRmlyog_5yagCwyj5XcT0E5CC6Vodn5lw0UEBar7eWADo7DpImQ2F8DUOfELAxBBK_T7qEtsRdk9RKpTe2JlMZIDOqaPPfinR5H5qEl03_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMN3cQF4m3-4YETe41V1cWgskZ4yrNvZleefe3tL1E31olNGYao9I6YhIewYuOrdIKAlrIdG3xtrcheJBRKjnSpAzt2h1JB_gkIi1zqwySL-de-j0Skol-KdFUkZ_nm1rerjXm8kgz1n9Xw4mjMOSKlapVlzi4oFxRlXoLPZfrN9sHEsfZk0O-oRhl2aFXbGp6YsGjBlfNXI5VcobhMgK78rxutHqYhIQMqleVles80Nv5xaIAICD2d3-_V0kmQRsrTleE14Uq-AnQbPiDofx5AQf7cDNtAV1lL5WT_Q3hN9EQt6OqWe7WZbKGGUoWFxIenUCYh3k7dZvKiYaFKDNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpMBGldqEShvZ9vLaXcFOZliyouRRFdi77YgIRuorxgmvn5ca9fixuzZCdWWeuZlpfipN8AsOupjBbOTWSipxzCaRSSR2V8phtFZutnsF7xB_KAMsQ20oIj2rXUXdGnBU6WLIYB1f4h1N__eRp5DSvylUS6CN4MJkA6Bb2Nj9wEhEgU0Skb6emql5_VVDJUIPCH_pW19nhGeZiwmKHZTa-AndajpSdldIw7QTmNrhrREyxqXTE6w-V5YK_9uMPgJLs1oV99NgwulIfR1PhWoXYlkOF6NE9zWZCLFFHh0auwcs3t_HYvFe2xQfYiBjWuQMK-TkDYJ2IRuq0-wHTEV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4UZka2AF3bEJVIseKfllpqgHVgh_mLvOxLk8MbHgZqjpvKKqWcpBzWMScvfOj3JiIYXC0cAlhYRKlAiZ3kYMn4M8uAX0HNuflXf5PBLQi5h_6pVwi9xTsQSg__4olUozkmD00RR0UWSkuq-ITrRAjwAKkiyS3H9F9n-N43V7CDg5K73_IJWTuj2h2f3Mxg14q70vEfq-YaiSOOKyWAH1-7SrX4OoNRHBjCg79ADavEs0y1JGX3q20wcR9Sbm-fgz1chcBlXNXLfQM1ubrZhT9aTc27Owh3RYK-SEoRFYjtwBYb4TRHaRaJ1SdXKqzC0W8MpspzzMeKHhl63Nr37dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=R_ENGyQ9TAJAbFJQo9-kLWoJepHfPdPv_or1v1Wf3nA3MTx6efxiLs7xqgyy8t9u-mn0UGqNNu-sGWYTt0-6RMtpk30_eEUQhSGCBfIKl_FCrMEc82kcWmtHl3Nlg5dsSrnotVHgO3pLJ92sCUmN_48MA8sPugJ64CZFahDp_v2kQgy_Vz-ybo0hhorQ7eE4T4-k1NTcxmVX1A4bkPZRqkZow1tAXAkCF5dQMyvjeaex_m7StfGmd3CdfPapuNrerVSSC3Kk1fgZXZjnTH8YVnwlgwqhIXbQwFW7gBo95wNFzk_1nrBXLssIoNd0RnNWHnCpIo7mP_JjWdG4_AJPbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=R_ENGyQ9TAJAbFJQo9-kLWoJepHfPdPv_or1v1Wf3nA3MTx6efxiLs7xqgyy8t9u-mn0UGqNNu-sGWYTt0-6RMtpk30_eEUQhSGCBfIKl_FCrMEc82kcWmtHl3Nlg5dsSrnotVHgO3pLJ92sCUmN_48MA8sPugJ64CZFahDp_v2kQgy_Vz-ybo0hhorQ7eE4T4-k1NTcxmVX1A4bkPZRqkZow1tAXAkCF5dQMyvjeaex_m7StfGmd3CdfPapuNrerVSSC3Kk1fgZXZjnTH8YVnwlgwqhIXbQwFW7gBo95wNFzk_1nrBXLssIoNd0RnNWHnCpIo7mP_JjWdG4_AJPbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mir4HqA8BqUqAAaEaDLE4omq_Vsc8aWueg5UE_GH9snTBO4QQp00VfNvY4MpV62XdO03awFw312DF9LfTFr9sFfm6utJ2gFBNIxlqI-pFZkyY_sdPuahyINC3UpE3nIdB8rPS3z9cZhFL8TaTFzi4uyba6B8Q7FMGIrTzyzqpsizy6jOfW4Ai_F9aGPUbUzoXc2K1_XSn6tmAny-1KBF4_hFH5W-GL7UqLkOG5BtBg40r-6JVZE6epxUcwknX7q4rl75aFw941AdhgZRlXz9KU4WifR_GVCZdo-ank-tRn9xSNyX8Eg0rQ8vOky3pXD2uwXGWWou_1Z-Hav-PZ7yaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBJdqzV9UI9PUSFCnEQf3wh9RHkhwJR9YP_j4DOwe1KV2aUhwDrLAUkc5BPydZpVrTruR6dSMRd3mRxXs21ZggRU2YSeGGAFgJMI_FGunmxlbVLtjd8GLdZNtx8QoDJvHEm5e1fYafy0VRkrU92C0cHXN2uvumeJ7UciC5IoKL_qKSrEoMXTThpm9_uJBrc5sqkER30tkkpAgpRfiSpUEcLlBWizGbM71RiTt66H_jlzdfQI_L3iiN7FI9Pm1LZ2TjAEnZW7YOA6PH_s2YJlVYjHiCYi8WuJ-u6yFcrvEocnuu0rPUS-cAmvam11bdm2217H2akedOT4M17_3gDdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAsSy1IG2Hj0Q5YJ8GyEUUTaBllSncQdAePH6dXxRPoz0TPRaxdAfm28x9IMUSS7-jbTp2N-uKP7OMMi8eJ3NdvhVpTqiV2FwWt9G6HPkp05X0TW5DyeiBh0uWgefsNPuqcTJEkkDjttk1ypwxE9yVdjkaOaNHo9ZyvpoJG2YH6TROuynLC71FyM0XYHHQ6zq9QS2Jww3YxUZ3isj9iLVSJVZOJPpxHV28O3VLbaCJ86juWLG66Q6eVc38DSU5x44LmCA7wlg1cTOwRvR9iEdrnr2Gn_vN5Im3UALwEUZMJ61M14tH2b33vs7ZZlVtTen5nQggffFkHzLIxkeSk49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWbnaP1ACiXAKBxe5MaJEFIN0x2PkY-n-ppTlpHXNK34GihwgIFxZOBeV39AWk6kdjsbW_NPGYX8vuhaV_o4fMYVdXicEeUvGdCSFKcXztqGWuTc_2Np6VahfKVQD7u1LOfqbLQn1bzQcTaaEEX8lUKOBplXk6hnO_Za870PrRhMnlLONPj4pYFOMNP5GrGL2Up1PkCRI3yU9gvzGUX9_SwdN6wNJLj2AUiKbJr9btH0uXawHb9Ho6IBUe_H7dH3lv08w1oJF19Cknfx1yPat1GlKEFRRi0Vul5ZfCFthoUMAZxQFLDamcYWrFZXdjJFIHYNWAuBX-XsUHx5klssXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmnGHnr7PbmQ1wVrNn809iH_X2zLXW2LWxEi8wL8nK5_d-2XEA2vNahnyiOl9n-atrauq2IqhjDURjMffwY62TXXpKhCmz26KlP62Ho7V4_qqVKuuy0au0mHcqmZAz1hDj44CXUjUyoGOz-E61LFY7L_cAOwv0n1jK8jdczaSMgzyxYO2xFZPPqdLkXP4GA6gyPRWoMTa3BbgNhKNcnIsw8GKm47-9-msu48IhNRtGWYp3DMXCQ_dVhJJU5mb65x1x0PUphHzMZBzEiBMRKkRficIDqO2mD3beM2tJVZiIVOPV_LzYukWuHadqPIFdtuwLoAlXDPUEVN0LuWi4lB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLbnlz72t8ZjFqZUgCMwjYmEeggfC5xnvGDDXeMVBcdxx3QxZMWR_I8GORrLrfZm7EAm8SBWOOAAqP_9Y3M2fLy7CsHZsOWH2h7BrKK-4qR4i8edGes_7k20ac9Ut1nIwtQ0NuAHlIeMJmrgQS98EbvkFNcSM5To5OCNNXtHJuC_6iHmDXgec5xcAQk8HmUnj6iLImsZvLEcqxqTHwyqZDTELJFn5IPynna9jgoX1AwPpUTd1iNARBPDsANbs76TMlKhQzMByNNCUbBtWhAba9qiZkz_f0j5ADOv_mlIKnI-QSkwVhIFz3CIYbguY-NaqbpiV1NgSDhtTogwQYySbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpG5N-ZLDcL1B_PR7KwjAT-z4dil1syubaox35gB_s6lkKYofpjHAj1c1GVtIM2Vsav1iAIn79s7hW1up20iB4GQse0SKCMvcSXgnwi1ObrNl5vzDrBDtR7BOo-UQu_g4uJ6OM4fsawrSWAMEN7scdXHkb79Te6OnfywS0ntvp3-5X9H8jeSx-Pde4ZV7ZxeJDZjwh7NvPBrpO3MvoY4mtHoinTXp7QWB_Z3-JLpu8sxsN0kZPNg2vefSzu1swTjFFkdQcZNrYeZEkpKcR81r3c_SNaR--JSgcPXHd_6V0Ues8F356j_RQAXZrXc_VbVYnqocQnKe2lCeKXc2bCweQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBO-_Kwd4Xgzz9gj-f_SbV_bCITtVJuyDps2v4mF58J8gpPxUmAOWsKni0yv_LCFae5WL5XIwVECmSWceRVh3FtfPZ468U0pmhFKHqmuQ4e_OYfMEDWLLCkcC3OWb8zWDaOZxG7_vXlDqOat_fsFQD93oqTtnGHupcGvPti_HwDRVDOCxaqykd8TwfGiDulAfS0tIfl0aNJ4fXwuQzHkmrhALryF2KdH3Lnss3SE01HFJ1jTuEOfUeynPJDzm4EKAQ0oZzY2r-hspihrIefNNADOpY4N_WwMrBrnDkwRNBv434wAU76HrZ5_09pyKoBeG7pTcV6M0pSsv_t1gUfn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF_CCyMsZL-6p8RmSh2qpiy1gGFKMrYaQro3Tpw1yAWJ0rWEyajWQMapsyeZXq9b_zAxTIUQbj9CiB1lA7JAOrAgLYJexevucrgYkGjtuFoonso_BFpx6ZNQYeLka2CkjejLkUc51tXA7vMcQ7VnqHjcFYcsek3asFr2705lx4_5AiSGd9bWWFhfJvSQErdCSBgnVyAZbQ4HyxDCjlCAIupBTJwzHk74wjqFO9rEmtXyHmLfXdR1P5sM27XbZqePf3HQ-sxp5q-M1zSWAmNW27jojkpmV5p0uufSytQf5KbazBcuKy6C1ijtJ7UJWvbowktswF64jQUknq40GOhmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26851">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmMVJy9t-rZ_na5e5Rw95-kaFWNvd24Le2PPYJQpwlxjJWeqiLjZe6Lr1J05Ww4GztNtmnLM5A7pgJNe2q00OW24Ggo63V3lj2gS_jYU196fOwH0Cx91vHockfm3gwvLHtqYSWWhJzgwwBbT0YGSr6NTdxUDltPx4ORmUPckaooo-jSApis6UXod_BhD9CEXrvxHhe2ziriWoSHQxjDw3lGdlDhyuQiWVexB0Xl_fwzrU60X0EVadnpsILobOg1ybxJiqekKAmq1Dx7I4OPofbeUR9rDPZR1hXYSNO4ouTBH0sw4fnUr1qeoBrvi5duSx6VW_zubbKZjZFWcczwf9A.jpg" alt="photo" loading="lazy"/></div>
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
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26851" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLIuunfxjuG6ukPRieIfnqzIYpVncUqPPAD55msckHLO8f-907knZycd_UWMVSuC2S-DnIkzLgxuBBQi59QVnkShUatHr63do4H-ZS_M8EOVg6bc80YtMKXhPbw3-hGcK_wzy-gVr0v4DxVdKHGyd0fz2w-iEF4XiK_IeE_l9yVb-2ponoEgMRNLnlUdjuKOpjRiz4VnPYzJg3YxNcF3mDTIV1_LAX8Z_BdLMF46m_heidGgJtKk7cuSOf5Zugx2UB8XDbg9J5k3gX76zzQZ1Ajn9t5ZrqBxx52pmjUAIl80yyeLWEE5Bm6Lk7maaXfNgFQpiVQM1OeabCm5afwLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8wxWjSvo3G8glKAeIAAdEWP8A-htiAXQVUrvPS486QpjDRCbRhdMguexT1bp9HRGoGQmNFp9OzA6iQXOIwxzaJmvSRFk1OsnrviYlSD0CB9mtMHumOdK4lEhOMoEvQI7K2X2ckZ-ShZfLWZzzBsK4ViHi6KiLfwuhXuvI__ui1oAwGsVx2C3UYd5i14qgeQcl6z0SHcSQoZHzcmht9HNOO8B8ODs6uK0oPyUL3OenNMmKcN9rlPWTzjR3grn6Bn0DoQlPg9nMwpJIuaiM4djvR3B_ZpURzBFg7g3s8DLkwunJx9Qlk0D7uymtshU0Sk1VQ2VVOapb-N6SxQhGbS4Deo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8wxWjSvo3G8glKAeIAAdEWP8A-htiAXQVUrvPS486QpjDRCbRhdMguexT1bp9HRGoGQmNFp9OzA6iQXOIwxzaJmvSRFk1OsnrviYlSD0CB9mtMHumOdK4lEhOMoEvQI7K2X2ckZ-ShZfLWZzzBsK4ViHi6KiLfwuhXuvI__ui1oAwGsVx2C3UYd5i14qgeQcl6z0SHcSQoZHzcmht9HNOO8B8ODs6uK0oPyUL3OenNMmKcN9rlPWTzjR3grn6Bn0DoQlPg9nMwpJIuaiM4djvR3B_ZpURzBFg7g3s8DLkwunJx9Qlk0D7uymtshU0Sk1VQ2VVOapb-N6SxQhGbS4Deo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol-Wjk_y5vFzpU1A4ces-dPib-HLPV81VPYWQuRhPkLVOzsRFMQswsLodUP3dLd-O5AMj3EH1mOQmuUMXXNBwsnlxgyuYG5Sy6baZsruG4LWISIdt7hISKg1CcE_apV2BkNofsuhLTMeNnEjYlOQ1srYXQGRHjRyHQtJ9aWNn9TLXLALuWtbV8RSJgklrOQb57Dq7oseiyCLhFsA626tFo9mWqmjM3u2lfRhnLFbyTatdX2eBiYEHItem-GrwPW0VtZuwdizBVlgCIXJoDXhwbc8auufwahjJqYIvnhGIvBb8sRt-mZgSuXPIwverdSSp0V-1Prk7vbFR2ulvPWrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1Got-z9q1q3fd2Zi_UQOealoB_yIwPkPW70DZJkEgTYCiOuCzq6ad8DDrHczmgsBA5WOTzmlaQ5Cb-Yuqt0Y2XE1WkzDdvTwxdWU9B5NsZ_hWVHrS0UnZV45Bq-rn67C0KgYwOyzMHTpMGeXxQcfxw3z7_mcpHTgLN5uoowYp3ftRH-GtO035k3hjj-6izpvx2roo577MDDQZsVROJCS7zZSmPaYyfBZHrZKqWRklSEpbYB2bzmHbS9Hm7t6tIoDuWDAF07TaPvZeFcD4Qc-JsSTn6y9reC7FLKJSFfop_LIFFeBbbwu9rmtFmazWeyKzbkbzKdPhLSGeFyQnOdSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBX6P3XQ6KewSczJlS-jsyF6bEpG8m2TzqmkQYog4c5i62xKjpXy7tBvRZsihsemx9cQEttiIG5hUsXVGf1MXfKTL1aJhc2iSOI8fsx-O1T-afVbGKWEL_V51LBpqw78XKhDZcVKORFIXk9TQkFurTjA3-nbghei9eXUR0_ov2S0DDCOzM-9tHP4Py-b75n3DStIn2JwyFoGApXVPeTHlMaY1idiR6ElKCaZTNy1rsTBnSqE3AvNrJKdzhQeyQYXhxrva7k2uYu7hCxYpO6BjvBnKyblgt6Xiq4EXUFdgXIqNyExJ_IN82hH6QAkkBk0Ip3Udv4uaG9RdAjllG-Rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKhPC2kTVuKNFa5jO0OCEaIdjTqE02sZTArXVAT1S9ZCZRNzsYvwOYUTWxa4k7Uz4Me2Wwiy8RDqtshNROwup55Fi2YBnHz0L4lUfIx9yqFkl1X71Ci4CNtRJAEbWuetVjQcgUspOzQV9_dDb6X_mzBL_0qSHNW90MES0eMib5SaABihrzfJDzly-T4eSiHvC-IaAfg_jYS4wGLrNEwBUgyWFqJrXZNubtNAQ3FjuGSjI00h7KDvmEOGrdFZXq1qaeZ0N0TCbV_UAC3knjGRt98RNtZPNeUyEGAub-A3RJIEQiAqBpjgFpdGEgjZUUA87gUBjxnWk5WT6_jVXCdDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eniSSEHLNdYSVF-gF9hB-pN26jmHKmTRa0sGdcHyr4bnqH6y6aan1AmjeDcmGSlKheoh8XEK6SqoNNsxexePZRU0DKhgJ7eI__ZaswUoj2nnZaNHvPZ15Jj9qnEZmXlRNrWk9oq5nHEpoubYvDbNRuTw9m1nF6Gso_tmg67dBQva9j35GBlDjXlAn7O7C67nTcbGhll9b4R_3IagbUEc09YYGPkbJjarE04wVceLz-69k41VI6qTCqyp1-4S9nMHZS3NOQFLfsnhn3rDkRprAf9VKKU8CrkgwsuanzCblQS4X2zZbnjODxVrgU8ngQj9EhuieaY47G62pW6_z28Xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzI6gH2FyOllQAcazWbfOsqx0Xp-gqRycyCE62_LbLLOv0L2GWiRTVmGuvzgEswn8axgSIvuYsU4IZaFMgV5IwwjJCOLCf05e7PgRmHS-s8abKoNSLfOAoe-YpJ1K6WGZTQvr8NnMoCfU8gFHPibe4s-Vu5nD92IWmRicedaAbayQrFFC80tba5kxrIKTol07UknIohBSfIaRDnqTymZXi74PpJR3ncMAaj3TtECkjmtDRNuaeIBjhyB5zz8SyoRdjv8YXGP4dWNTaB6wERigu3AvFhlwulPdKbVis9C1awFiRdBAFOppjyVNffsESvpu1x-bh5nFPubPzItiYdeaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POPEdQE00uvwXeMSQ7Ki6XrKUZlG8qViZMyRQX3kW_wO2wmZYrdYhUVW-Q8cWv9AvMjtIDM_b3pqcrUW-g-0afTtv3qW4YNQwDx8sx2FOzjrC9oDlmK5ydtCCZ-pCqtlcdTSnuUZ7w7ftQWv06lATIcBADGUIjnjJDVuXfTolkbbvF2g-AUGb4S5u3uUnFCegjLYN0aatgTwE7ZVq5AKdI9dPkkiJFBqY1zX6KgS-DKHK52pyGio1mt8jRGzbNNnrI8TuQYdtyLzMLLzRcqLSVI61Yj8lCjrKhzYCx5yp4AK3KKZVrKDf1rfkWw_BGuc_GLeGLc7M8d9A3A-l0DLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqS8sRrVRy5vrVYFO8ANhfqpRkWS9p3x3-X4KV1BDmOGaESKaZkXr5edto7gGKY1VQrRfEoTM2sWVZlhXCVX7F75TiwPOn8fU7HDYOgLPbjmz0UmH6tzSiPD326MC2RILGFyGQUe4thglDrz-GLTsdRzsNfbbD7XiSghOHUiSj-u8uyzrYUmn4B5pCv5vaO1EQyQsQIpH6SghFVx4ZVL8179C83z-TfbfBveWFRI0QBHb11Vgx2AkZrm0zX6a3-S5JCFApSbxIdf3oxmiUDQkHXES75NbR4Si_6M1GIdCzmCI6TmoNicd8MWNWseepCky8idqt0JPxBSxCKyMbPTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4isEYp0s-xZLLlzq2Di7I2THPTywQ-Hb7i9wF45J4TGZOzoeVWSHWi2j3XW8Bc-f5llxw4nSbz5FKxW8gNryA2D4Dv4Et3c701QQ0ucVzmbGNqextyyPY_3V8MjWNu5enulXAPTSaEB1Vj08z0CvkvuveFphgGjoBEXUZPcKG9SYP8wL137q3EkbjbysWZjKKJi0gy_hG2KvVSntn88VHKVGaSWVDUpmXyTNYD0B3RDI7nCB9kjaw8ffGHPkr_7Bddn5E_E8PeJIdnZr78-FsvSaEN68ara5-Pc-jqJX0sApovSAhSmogRYDcuvWdX850MNjry4p3VqlxJuHnedhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDNLBSHn7CqbtP-LJH_IlkL51XrLIDj2vIldPRcc72f7Y6iRcr3nTcOrFRS_RSyN8TmTVvxhVGEXT1bpt-gluq1JRuU-mFD1DHfq7locnaiw7tS_xI3xajtbkfS8ZFbMLuDkryoAfggaqJGEZVPqqsNg_zlAnRZ6IwMJiegsDY3AMKIixAISi5P_hi1EF50OGOna4XFJnANmp2gHtWUBCtLPxrTReqExz4aVVmrReHwx-TI3yD9FTXUSEZ3DN9oDWr1PNuW2xDD1Vw1YCYfI9mkL0Nblq3S6txC81co3loGeHatqn2sRH5oxR4zBHXe-0zp2VVX_p4ZOCBk1i_yzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgakwr1s6-mQ5Y0r-t8g2SiHGm43u2XGxsxwnj9vRVAPP2E3TLPmb9ZwzzrK0OCBQKvFOXpy6cNIhwVDAXBVjZ-W0wrDn9-v3TYJSpuxFcFe8sUFlP0dHY-d9s4PHR2dD6na1fHRkM6nF9kNzimcGqKo-qNzF9-bYpseCeNJgIcrezh7gn-pS1cCANOEiBpYoRDVTeueQBtFwowcjqGpeGUUH6XzT4AI3OAnO4lprrsERZgT5QAG2lmfm6OuJgAp39w1la8Dme6d51aPkgvEXEdXM7YbKKGmd7QtZxhcFAiTpEZS2OwlfkjKPQ5VRh1ds5_-s5JC-eFMTH3Koo5LqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwaFqYb5pvwYCpJJqiQg4-q589168mhir3aIVBv9N6gzxOtKmRWdETp0Zt47Om18aQlHGDk_AD1JkagZq1GmLtwUNo8DA1FSzUUpwsVWNfDM4zNt5OVpbn47wZh-1oi6PhRU3h_CbuX21DOsK4hxGsSlzw3f3zASk8HgbfXb6cXCBNBmOvmZU4i8NHEQs221_ABDHrt9Mx01VEkGQMRrtcYi6y2nN2x-pX9OYEE96oISeUP22iZC9nWD6jnmWTRd5JUqvQwj-nDfzUIL5m3X21uOBRrht0ZhWwvtpMm4h7B1iNwQo3buGDuiq1_CmsudJNprfVlzxeiy3uAGQOSPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN-VoIX_PKsJKYMQnjmk-DJEJN5MjfVjxGB12oMT698r-NF2s89FUcTQ2G0n7Ygyo739Pji1h-IyYa2y0izIqgAh5nzRMoOOECyBknn8PbyQNascpF8GfBrqU6GL1CJ0ytl-20b2AwQlMNAaYsKpsO-QQuEOjFAJwHz3pEUTOGiQq1yi62p3JtwDaWBSk9O4URqBDH9sLf-p8TT7cRbOWcvZUvCw40m7-2TafufHSjRboNKGqreFGaVadnYgjifLTbDTWyx12LNPZ7G_nthtCO-K8nSHSYkt32U9NHCbyRlI8hmI2Bt3lmIuqElDOkp0ng8lxo8WiXG5Ya35VHKrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdQ5HU6xbeUIQEIYpsqQ63L7jB1yQWcNiTqqPbaCq9iQKl6O2cfqH1aLulBz-6UCaoDhTk409RoC-_nKPE66s-Xs7YrYfazYso9xaJY4hOxOWCgIzX4M9TwvGVjl8Kay4p-5nkfdsnb0_oyVs0AhqY56wj817aoc56NONMkBfk7vp9JAi4_rmRUEUxc_-fW0reZSRit_sAXKKzMsPSqXhwRyUDvtI_phrQ47_9yEbWneESvjsc8yup-H7B03F2h7zMERoUhsbiPP3-BZoD99XmWagB1J0Ykfes9agA5rIZUgSaWUq3Z7Dzu4C6qt2H9kN-WwXrpdQsXSOBs_Xc-f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRtqEdq0qkVD20Wp77paUnkfx_2rFhDb46Ev_jmQigViCpARdI7ZowrVqT0hG8z0ZqCaEm_pTs2LmbO_HeT75fhq2UVNgeLVmeoIU--d4maJf7Dkns2ZAAowJtkvmp9sRkdxYM-g2BkENbGjAEQPSXApI_Annimjqur-yh6F61sPfTF-1mq0hOZ6PTXz4UVKQQF6aqOfJE0zPrWaT_nXt7yh3laD6W8MxtemS27WLUWbwoDQTqy9eG9b1YPD_0ovRtI44i4TItwRuaavqkfQr5NtBS8LKom8UxZ4l9JTClBuaosvQShLkx3KfIszJlcMTyYek3ySBuasBKvrj3gCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeqhjGsS-1tR7VVlei0Sx5M4jKZT5oZrLY9zGwwDnMdtMWR4_PDa0qKIwDEEHCQMVxZsf2NzmnIFsUO1NJtQUCkw79fCYqPyDQemHVCEZkD8U46Mj7QUZtrGI2UVxhg1wGg44p40aUqATGuSpn2CAmvYf5a0G7OdqCfxVJ9ZYeJ_wKt9rSpdPGR9_BF99GOWrVCjrRrmTs-HK-lObDXv0bYDk06VoKsfipi4c5OIPzqM9FI3eQog8FMa85OlquP57K0CdyioLMgLl-8VJN5s_sN9srgpQ-9EYOgW0lpb9bm5_SEWnk6e7AENWeRrNfYCSdKRpd0wnBuoZfiT5qiAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWuiiR5v7JNVv90V62DUm6FBfSWwJjNMNhF5Io5kA5Rg99jN_lG_nL4sAcQK_ANYyJwu5Uu48tz--A8ziOMb1we627xMBXe9gXVpF8lOovWw2Y1w8XPGxd5ovHYQZyMFt5qs8Md8aUHDg5JKszZz87VjuN_JrR_A1VB2uTZ2zP7ii2S2bkATG8hVlThgEMWTdpHffG7grpErgIA_52uQSCA86uxP_9k3Pm6DQyIMjXQ9l9JRZjgLOD3UXINTYnrjblRhr20hGqCBANumqYgooxMJsY7njINWIth4Qq3aBwiK11utfwg64x0hvIRE4JJVnzyszBhJS_tKT5AQGJviaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDz7VcMTMIivY_0ieRuoVgg6DCyAY2I2fVk0GJItEPfp5cICzcW20F0G8V0CkZDoT7G3naWMfMEe-Fd_mky6-H2dg8EsZ5qzd5sZPStGSTOvgqrJ-uuX0SyPxzfH4nAwxWJjL9MDjRd4Impy6bPY18fS8ACSAvvBBczItMmNELtqJkYMkAPYs_fSyCjPCi1Exn6jF156gYzsTC1oykYYoNp-mbBRmr0QKRUcup2i1RQUTl5k2mgbMO3KqhF7SL1QpUSF83q_J7plrYFoj81plDuzNrMA8r2VWkEtm2NmT5L8Td481C969HXbyKTzU4O72Hz45DdlAWUMlIJdYuA1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKWme0TEH_Jg-8QPA4e9JThdX-Kt6NO_BBH2JIjrpJFlIkEuIgKwDlRXdQRL5DdaeyBwsq9ymEZb3pP02atK7Z0cCEwOApi7koEo2Lh7V2zrc6c06iTZom7dE5xbUYR5xIQTY6DxDISt-Rnpa7wvUuD2538LFSwmTFV_3EZ13111QRn2681mkO8w4qPtMA-CP-h9tAIIuTBcqCq34pzKxqt0sjftlLZGeY38IAuCY3ayi5bU4cgUhI5Nl9DvY20JJuUNuJcOx7Z2P4BkDjGRdjaGdJ51tBOmGhKy3G_HE-XoYIOSV2tg-wR6img9f-UAXYr06gjIih1fcExuRfPEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1HpVsRpDDNDUP4U7KBDjC0kJwcxnZZJ-X4l_zbYg8j4nrVMMBaurdJZJhE3wF5oFptXUHscqplyxKeWvMf7u9RbM_OGH_PC3dxpaXszOjQ2W9X09xz5vMp-MLbKWlWd24BE5Hh8RhoFryUtlVlGDwJzf3LeKpQKT1ye_-HXeB8bOHTko7fCQLDiZXgxTDcKDOnpDK7b5zGn6MvaAMgT21qhaK0AVjxsiLUFC4e1u6ak9mwgI809CfFpTYHIjZ37y_kf8qtrvui4VELJh5eWxItbQvWTwbtg7xDr7HfXXYxRQsXPB1iYrnrC8fQ8mJNZgEyAPKKbTNNY6gj1Wmxyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4W2fumHRq5cUrz5IA8jIb-CGoXV5mC1xXmfMHst50SYt420xy3qIHWr7osrg31Rp9naShJRKjx1Uiso6nrGQKwAO-v7270enVKQmM4XYQudmGlH53xQso1oOrIp_hC_2PMcdKmHPaAT7Dhk8YY9p1Ov0khQZfCfG968Q6O8uy4Cp0HVbU1UOaPWP9wqMGUgM4JD5jJjVCdmmmjyLuFMzgNdLuBscWUgbFfUb5ZETg2VDP_BneD83U8y6BL3PNk8qLgElId6BA7JVlGp4gSbxLguONEdXzxSDqGQc3HeCvZr599kwYM6HdCSg0STe1_oFzG6AsYYSPQTocuEKB4HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhGF50jp9ycu7cbd56G_4H_S8-Sw5pY-b0BlSEET8jkmjI1AMx1NXP5Om02v5S8W7_oRQ9H01n4IOER-HHG-qdYh0oYhVWzW3wRBoFKXrncPKPvVMYguQ5oonlt5wqnaMRSnLrvJfHfYA8NTqcVxZ8s5ZfBAQM-yQI_3MeJkcRvi0BXeO7AzEJZKDGmx_9RIeP-wGjjx9iS6JKfhpa4JbFRTWRAZz7efRXJZ5uLBuMhDSRonbiUL6OANsJZ5axzSRjZcUTm5vMMaVCYQNuryCdZEE6wgxrGjPNZYHg1Ooll02_GEUx_1XMOAJG8IXpK9XL7uDm4q0Lk_bv6WqMSlzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax5TwQhfiBtAaurLEcFU5J7YwVToA7hygV3yuUqqyfvwBbdaxwDfEE04XKtGBatwcXndzYXnD2cd_5gAwpx9vA4f2bXpr-v2hO6LsQiqjfQ5Va-180sfNmVxwcmPuP3Q1O3m5IBqwNRrUfiQULX0hoXmgUITqrRthKQqb6nNwRotQAjJT3F64GX6EjUKPqb3kuGBJiHNuZwDn6N6jy-iJlQCJ4IgnYYFaxzpyWryd8qI56f3lp0VwtaHigrpA8gM4QneO2ejghjYvj7I4Y0raZDuvn41114hA3BW4W0twpq4xqyIL-eka0b9s3cOGyoNiBmtyKL5VHCAsuIVxVAWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvsq_PqlYWkSFU142De9mrVd19dz73UXQyLk-RHXKxtWQ_mni4VinjAUOTI_-whrEA1_ngJ_cfRpqW9mHKwSSi_lkb2TlJo0ly3QLFpxqGQmjqircElMwtTarKX1feucjAVSTSf9QVlgpjeWCXuq_-Gg3QagVQYot7CfU_UeSnb7a6rfPitScvkURXKnBEZZ9qiGxV2M9bXSl432RGOzxUZ8hI_pQfqFOI60Sp6nl7hJRMuxM7gkGnUY7T_--WcMMdSN5KMq0HyPdgLyoh-I8-p3mVhCF9d42rqEpvelp199ZdVBxx4G7hOOgZvQMiip1glueJsr2WlblXa1l_Ydmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBBboIZ9tkmtvRtylfonoCZmohphIJZCdIVYmtrFFFMnx_onyAzhYZ5wPlbbWwbPvRuHx7ekybNTh7LL2BuNbnY92702ofp_O26n2TvxZC6XQXduDnPOIIsGImrhFsNaFgomiGzOZ8TXgqyFHIYRa5RkFHIBNtU9pdvN-fJjs7jSibz8f2CBBwLE_XxybQAgjizk8oT7gX0zc10aOHu98IqLiIcdmdReJRkr8otbpLpT8Rd9jYYl0amrg0QJ1xd794hPuDpbQCXRN6iGrtQn7F7p9MweRp7CInXy7eUgAbYNUliJXO3KWwnHpaThGU_s3LX-hCQwXwOTQ8mCLe_8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Npyhugm1aXj_xIW_9hFce3cSxEQDmrZRRE6HYI4Tvvl_f22guyqUIWVgBhVUnamJafTX0QBLdUXAGAa_BKZIqQ4dqFViOV_mKL_cZhGzphYWtYQEhS8QBpw-nope8cQrHSNNVNbdeVNt6dviwTic-Np5tSkTC8lYDrHB3aNnvAZFeK--2bv9Vb8JKhdhuBc9IhXWKH0JX-3L51wjzg7Ujd_qAVOkacvXqiRSJJTSeKrdPstZ0CVl7sUs9SSdahD_AUwZ3zGzvyQYGhx3o7sCdm134tUdcNwcYMG-ZTxFRDySeThqR77O9R5lBTF_Kji1fA_CAk2mqHjhqaMbguPvyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTmzBr7FiF1HG_p6RsmuixKe8f_1Yu61tJvsIYDaVyVEmVOx-Z7RMYP2ELnvHrlAkmcqg5VZIPGyy59SsVogycNKNobDwxpOsjvPUnf6ZeAHoi93qNhdTj0LpdxiUWyWmT1KmQ4alOAdLrGhFKqbw53IbJ-b8NxzXyszTfcVhFkVVh5myPqy_t67jMwpAxeyRKdeZXAv6TIY0RxCi4Z6qx6uIfiHx6P7R55uCLtJiQysWtkmIP_YwZE6wMwHiwyc7FAulMWfZM2VzD0Yt4Y-ig7_5SItN8HpayEP4gTo6xx-W_nRac9sI6OoH8Du4CXa3-vMYoPJSEj4daE5mM7KZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5i1i-WVyBerDsG67B1W4k1HnojH6xjirlNw_VNH4m0Bj-spejB6-VLdjKXG8BslwrhRDxL4kEDCnL7-V5SgDmX8anEM-LeNKCaV0z__vHHOpo-9ml9dsg8AO2bko71AzBWlA-rOAuSWTGnjZ6DMlTfZ9t3eFCQCQvGYP2BTqNbEL32_qjRsYG2pc9O-KQN94Zc3u-dlxwZ9l8X6XZaXu04VyX9wI8LlfOo4zYpNtlnanmSwfxR-mHJcws92SOVdnW5m__Eao2AQXhl3S3prTNrHfg-9RpjI_w9cZ1-y5vqOvF975MnhYvbRvAfghAjynDnDhanT06TstCUNdTKetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEoujU2QW28HpXPT-yPVJcOzLixNW1Z10eTvA_th-lo5rc_971i9-2ZubA_Daxn39lCmmPQnBz4h1uTKER9eqHuhfZGj69REVpajqmJIPbo7AjP4A5cTaBfEVB8ogF3BUeIXadTGpy-P-VFdAJBs5bC8lRjGkepuBkPew-iEoWHGxtuea32kJG3e9fsHs_Hroi2IDHGfdagSzacfBy4q522GGCDxrLGJ4PJHezDkWJ6c-xVBdSqSeQLQDzN0FGkaPMjjize5Hqdpb47Kx43R-Swjrx-icokMQWDax1FP2aenEUNB-rtzyJq5B38aWvNnPqLHknHU8Z63xAP3HCH_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7vZombwTJZvayKQ7KQs9Jv3LwT0RbTPZrNG11zVVdBRHuKL-JfxBiCfX5MK1vDtHaXX7oJJc2KjeyR6XWPnJZtOmzYuT7yIVmyZ1riKLcE-PmWV1ZAoRJDQ7h9NBppEaKWHX_dIS6lgG2Sujo0A0n9zgqjblwqd-CQOvkNBWBvRCsonHsm8IrJImNT_m1P5Y3ECGKBBYc5_BzyYUhklfLzFSFzVkeRUHKZMbLPTUbsvI1TTbmWwYn8qxAXBorBNTa5Tol6btyv-lZy047BZp_WyLA15pjcguOtLVJXI18ltsex_c_FEWn7tm3DoDaK4dAew_20KEETabDQDIbZsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huA82zj-VoqKNQ5BY7TIPJMoEo0qb6VLGDMYpin5d_X3OW0ha9yVaLA1XV79sCPeyW-_Vi0GDujE8RAavnqaSZgEfafDOGerhxQq0ZnW0gu33R1YUb-Ue5dLQYVN2CELYuIim7adGfTpjsjW6ux31hMWCegbVhSfbCj3C_-nJ2-pV2_-jp0lc0JeuUQiCwmYZGa8TEIHi4WEDGArxEeJEBZ-NlLps_aehBL7-8YM8Atcgj9VM2QEzkd5WbJi02DTKWCtj2cbf7WZzo7mUYETJY9-f74WvzI_YZc7cGklqrPU7KY_L1W-W4cFZFXBhBhNdgGMv7yKuSX3KFZMIiCFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=KZC4m5uNBF1IQvAgcH8HdKTg1dg3eD2y2PQtQJWkVHxIYRg1SpwDDTbOZzb_Ck0MQWpKJCxMU9OUSRceMpsbIOP4oyXFkN6YlktxLqREb9XiDFd7enZWkWAb4eS2lYDUM9nT6maDgyz0MarQ1kPHZA9BUDaeEA13w1XQq0uum4fCRPQRPq-dtr8Bc3JUeABH1GppBJ2WskH9mLr47O4vCtCuCstk8o5D_RhLezVrcaKLJMMlFkOI3wwyt7yEfzHFqExJApmpEbVFkGqsIs9dXTB35iryKBiFTpJkktZC3IQNMFZPfBwMkGjLh8Ukq0GQuk0-XkzOiTezchV5gh_ujQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=KZC4m5uNBF1IQvAgcH8HdKTg1dg3eD2y2PQtQJWkVHxIYRg1SpwDDTbOZzb_Ck0MQWpKJCxMU9OUSRceMpsbIOP4oyXFkN6YlktxLqREb9XiDFd7enZWkWAb4eS2lYDUM9nT6maDgyz0MarQ1kPHZA9BUDaeEA13w1XQq0uum4fCRPQRPq-dtr8Bc3JUeABH1GppBJ2WskH9mLr47O4vCtCuCstk8o5D_RhLezVrcaKLJMMlFkOI3wwyt7yEfzHFqExJApmpEbVFkGqsIs9dXTB35iryKBiFTpJkktZC3IQNMFZPfBwMkGjLh8Ukq0GQuk0-XkzOiTezchV5gh_ujQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7Z_6xDxhDkSFtKDDqOBt15dRk6ZaxEXwmuUJR9YtU2BFEp1DVdQqiOAWR4YbQFbBhPwQjfTJmb8hBkZ7uZpd7JmdnTkZxN9IxBPQJlaG7VwzhAiBv9Sk9d3XJjkgVyXwih6iPAGPZ3er4NBuGlJoy9jpGyxv_LwM1eRc28aO26Mq9EnHtbVb3U_336AD1UDFLqoe2uaYPAwjiLmxBvsAc__OLlHLlpZ0pH3pYB17n-NOKz483ogvdivdR3s9VJiBJ1TNANAzmBH3HSshTy_hEU29n-xaxEDvKzr9eItweDf0csPYb_Wbegap9dKGNkTfiu5dZWRwsnr--N0aC3jyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5CGJeJ0npwYqODFmVuMHHuYhYCunY7PD8P2Ym7sL0QHqe_rCQWae0dwDwMp39GPq0YtiJ_G36KK3hmPAhmW1vgrHgggHieKThmeK9RGng5-dUcGhEm6Q4RGoFzQzn7CDNvRqYOTayzi_rlU6XYSYCDol54xuEUcZm5VGdgZYRe8box9z5TySzmSNSfe2Ft0VAZd_uzbeAVU-8ugkSUdfBFvps8GWfdesAWGMe_QjRImGZ_3NCplaUKaR_0M3LQyMuZ_3qwoGQw58p2HfTMC_hjoCrZvljcTUzsn0b3n1I8rP1DA5ftbkLyCRY5kgk1tvGTm0J1qRdddkfrnJQWIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qx-wp0VQ93Wwsh8zShaPa-DwY8N9O4mKL2wFr5LiMruO5hmHwO_bN_NLMr5W3V2ao3hzaTTigA67Rb1NXqUCo0h51GDH5GAFnfyBvnYhK3d07XSRNUMdtDVBH8yOvyjmTTZYo5wG1u_Fp2OQ8E1Cf3WRhD1dYiwlOlDD9kq3fg61MP0KNazyD9LYJ3hp-59KxL7AzAdKEYsn5HPk4ydhu28ehchqGSL0aozTUu6gkb8pfUoFGhL9FwSjuYF9hMP5k_LzxTG5Z-uNdyjdHjqMBHuFJReMmBpbdkJX4OyrK1B-kjadshLMzyL860Lici40Aay4gnGAviAlD6NO0twymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=VdFSqbvij0iDp1-zgPfmOKlYfoOQJYmzs7MLf31sD-iXExxANZD27zM-AQLb-3ir6QBi-EF2VIeXF8rOmt_huyoHyH15oGDayXy0zJnWkGQCvMNOaIrh0ukNHNPLpJ05Cxudc9mu_pHmcizF9-XXGia5aDzxPOgY8hoybmi4j0dg_nkLadq22QoJZE6mVcaTpomu7bFr6tonJUbfDKabKAa6xpReajPR5chI1W_YyAwnnHpuzEKNbYtrVIDIuKxXRh0GPwQEmnASqlnf-Dowo4Hsr9CO8FB5y3RExE7EbuuH3LQf1iGqpEJ4FHTvTq2A5u74_Jsi2AABOc8c1as09g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=VdFSqbvij0iDp1-zgPfmOKlYfoOQJYmzs7MLf31sD-iXExxANZD27zM-AQLb-3ir6QBi-EF2VIeXF8rOmt_huyoHyH15oGDayXy0zJnWkGQCvMNOaIrh0ukNHNPLpJ05Cxudc9mu_pHmcizF9-XXGia5aDzxPOgY8hoybmi4j0dg_nkLadq22QoJZE6mVcaTpomu7bFr6tonJUbfDKabKAa6xpReajPR5chI1W_YyAwnnHpuzEKNbYtrVIDIuKxXRh0GPwQEmnASqlnf-Dowo4Hsr9CO8FB5y3RExE7EbuuH3LQf1iGqpEJ4FHTvTq2A5u74_Jsi2AABOc8c1as09g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTEETpeb2wNi6AkKVbhkfFD14SJmcWYfrhVD5lm9-j7CXxG0Svxcb-TxRiDDnUeaC0nJc6D_6520KDi1so5wadIPNPnKLNJoJj4tChWlmMz4o5Y4MJEbDfLZih-D7IHPs7qKTcaHVj4EZxTUkIOVO-4mpTMqjrdwzNaBGuJqZEK68_-afPfoGhiOgkZ2w3NZI8iS1g3sVau3Or8ydftL66wOKMjTD58K6POa2FUeEq09zGzNrXArBtMaz4yCZkHDegrvV-m0lOjk_tnL8VQc3H1Y-6BCZeSIln2fkUcQrfFY7q7HgWxvwmtxsO4JQ889XNKeExaZFAChcpnjNGzMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN7D-GQQh1MaVJEPP49YIU-LVA_YkmhB-c4-cZ9PHdZj0EnIJ5akoYc-7V174F3LEMSHzCoxzvrhmVnhSN-h0iZ0xcHCBmSv2r1BZHHepIsdmJkBhBXZTZp0gv81I1C7owysvcRltYoLLmyFRFRviJILbqlwXrs5iWUo3OjA4M0nsq6yfbwdi1kjw_F71vZliQMddr3vAn5tMjF9wmqti5zWY6sILLk_vsd7Lr0O4SolLjTtsunl7lC3NTlWF7Va39_SG7Ms-11xvKyfhjCxoatRm4Rz6ABJiH49sNOY-6wj8WF6AUI-EJTU1izsjblZveDIe-p_0xw2Hf0PUvHdXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FemRyut4Fr9rdB7m2_UzuGOlOGAzrthYHBEgXLCpttZ8V8vSn8KTLnKBFEGz1-uo7lrTdtNdXQjPv8F0Dgdx5iVnVYpLbCo5PEPHgK6uuJPOOoXWUSEgDXRE9Hj4Cq56-Mp9G18sKsfqlqXDAf08SyTL-zfmdzE5Cgp0aoWH2vkL4xd6t4SWNGs-jpvKrw9E8TY4qLutsBbsLdhj-ksYsgGStL2VFJUVHBaMIy6JdMseqZbjs9cCFqYLhp4H0zpcu__gxUDVcP82CEtArB84HigY9-twK0CIXfwdnZI4M-z5P7cBup1fZhbX9_oARZsvxGoYlMOpHEo_dm4saHiaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=N-ucy5v6dW30Yb1EoZ5j9JE-l565EC1n1_iy3ESe57Odh1fVIiTcM67HhApHZctzYSmvmKb8xCivJuxerOyaLLhECJQqNKfXdj7R1AcdN8IBAHEz1MH96WtjAyyba3RMi9tydwrN7NhOMI4nG8CGZLEsoiIt3TPLbY9fDuIQutKo4muagRuTgN3V2ruU1neR19Rnzmxc_CE0cnNKs74nuaoQrMXLVJi-_InKUnK0A1RFz2CanzPidn1wBoLg1n5DfpiC85QIY77xCZL60SlSc26EDrEI1jPfuCXOwpkJ0giCQhlwbOHl02r5xMV0ZOTq3cwWBWrJWZEN467_vW68YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=N-ucy5v6dW30Yb1EoZ5j9JE-l565EC1n1_iy3ESe57Odh1fVIiTcM67HhApHZctzYSmvmKb8xCivJuxerOyaLLhECJQqNKfXdj7R1AcdN8IBAHEz1MH96WtjAyyba3RMi9tydwrN7NhOMI4nG8CGZLEsoiIt3TPLbY9fDuIQutKo4muagRuTgN3V2ruU1neR19Rnzmxc_CE0cnNKs74nuaoQrMXLVJi-_InKUnK0A1RFz2CanzPidn1wBoLg1n5DfpiC85QIY77xCZL60SlSc26EDrEI1jPfuCXOwpkJ0giCQhlwbOHl02r5xMV0ZOTq3cwWBWrJWZEN467_vW68YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOgWGLcJI4VH-JNu28mkTvhZO-k_t0Zw9Zv68ASTsXg7xxdakk5MjhB2rOW3LUa9851w2qV2P5OUwOLqKRQ9reXK4n1C-dlGJwgHAdtULVSKF9cE3sGyz1pMnkBJp4VOgc_JGuLNA9MW5ZUL7e4yMhWD2ZEI4JIAYWXsYe9M2dHY4ok6L6yX0OSKga94Af5hBt65gfIuSj1rZshHLb6KIl9GWT-xg-3kCT_j0km1Q9DkjLZLxVAnW8LUmdA83tpvsJUObTABjBm8yOlopVOOTYWKSti2naISGzQP26-7CevMF2C2haOCSlHJ93Gik_a9caJUDCJ5RSQ9NoI1SX_vfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1-IZucE-ouA0B9Jd3_9WIEQRUti2fI0iGU1YVWIjtkHeQcqqJGxvLY0E0Lgi_6SyQGdfrqYcNUT85QsIdsZwMZr5-gDh725oBVfmL-ETJd_9tgXvBrz99DsF5Oex4jlYGxhMBhwfG8vqSqzN064fIpjvC3ffhryExnTwWJyBwK5g-iPkdu-DZVuNZMR5u2Kg9nNOVPK8KuvxZtOdjs8Dp-PfpxFJio8osaDMA9x48FfwSXGGgdEvpGoaYeZp0m-B2PDpjln10GU5Ito80zvpT-HbI9OapVze52e_88hBJYgNLGTjiMSOlCrL7LU0-KpEHKA9D9pZm-abzsD_Zw5pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/da46SwxnXJpd-dT0eyQUzVdYWefYv_IMYU89S3LXcg-vd4KNKfN9KghqeVrzVvofmZ6vNA_1oYURMmGfA31PqsysgAcBevYFNakSC-BBSVjlcmLSXgI-JCNgTn7NldqPfEtYvaJ6M7ga8Zw1sgoSHwzYaLAzWfzbgq3x5O4Qs1Nq5JjJf2SqaTJmgh7ZmRH0dy20hqv0OYr9EeR1oIanwFPp1lDNKwPZhE5PPfSYRM_S4C02cYumEbs3bRxvsM_Pf0x3PZa9vlSdSqJma3pCdNPv55tUoeWg05N7Yj6q-BbyduplJpqpq8NqsWcIgK-VAl3gcNQo1LHkS6AwDCHmng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uh0_kdrmPxsyE4ubur2BCDjcyZDwLK5CSYdE6bYb3tFu2ZO6vFMpcQcPxH_ZjV76YBNLqq8dIDyxHWo6D3cWyhQuDSMBLUgOSmEdaluv_pyMY2-PtQEeixAiJC2qCXe5eRAKw0hs5VBRtKzngk2AE9l34hwSs86t0PWeImSJ9Swc9CHBxo7Yxz2SNP-xYgxz5v62k7QcXAvfbvZLTd49iXqssCzne9FY5mqJB3JyCSOBxMHQTry0wTSq7ASSxOmCYU6Mkw1Hq_KNcpuInFi0nQiOybAMxe_hX9VnHI_-o3jQh6GG1TP706M2kTFdBAghLhDJWMHwGCJLk5akyWiXvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=Ac1LJL9sd_7UopEvQDv2jCSM0lHpGssYbcczHCv1O5xZ339YtrDbjHwVy_e0hRKIa_rrsUY1XHbZxyTGeSrWavm1y1xgopOp7ZNps5EvCYdppbM-vlepoS0MwiJuwmGBd_B8-K1kmJddszKHDvUnJGKZjZx0-5oYlfuzhGodAolbvHsBvhWobaxiAG9runUFhPrHmX7723g4rpclW04LWnDPaQoSFmE8ZQzbI7Finf-ngF5qPSLspxK0SycHXDETjrmUPa19DfArUivFZPYHtGDdLHUq4UVbG0H7CW6QjOtanwg45lvoSZIbOKWRunWF8MeIQx3m6GnXavvd9DI90g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=Ac1LJL9sd_7UopEvQDv2jCSM0lHpGssYbcczHCv1O5xZ339YtrDbjHwVy_e0hRKIa_rrsUY1XHbZxyTGeSrWavm1y1xgopOp7ZNps5EvCYdppbM-vlepoS0MwiJuwmGBd_B8-K1kmJddszKHDvUnJGKZjZx0-5oYlfuzhGodAolbvHsBvhWobaxiAG9runUFhPrHmX7723g4rpclW04LWnDPaQoSFmE8ZQzbI7Finf-ngF5qPSLspxK0SycHXDETjrmUPa19DfArUivFZPYHtGDdLHUq4UVbG0H7CW6QjOtanwg45lvoSZIbOKWRunWF8MeIQx3m6GnXavvd9DI90g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=dgggvXbEcGonEYF65aoNvpz-sY6AYr_qCgXlpAn38BXr-hCys4yv6-wMkQrp13HX1dSikJbv8BwcFdwxeFGAoDkTl85K67VHOOixw_PuRvK_SI_Vu772WhOHQViYRocO2BywCbKYQg8HEYJg-NolQ1yMEmlJqS9-QQjqitrsRdz230c8yGf98g4_O4FSQARKgLrNnMJtjfocJV3Bx9Uzkr9kyWy6cDSgu8sknuHtfURewyvaOPV83_rcUWh_Rcu0xOIkt1G2IuUmhWxVb1Gc13e4Fg9MvxFW2I1tjrHOQeUJcYXVH0Hdh_CpjvcKZhaJWFVAR5YZyGdgEpMqmXG36A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=dgggvXbEcGonEYF65aoNvpz-sY6AYr_qCgXlpAn38BXr-hCys4yv6-wMkQrp13HX1dSikJbv8BwcFdwxeFGAoDkTl85K67VHOOixw_PuRvK_SI_Vu772WhOHQViYRocO2BywCbKYQg8HEYJg-NolQ1yMEmlJqS9-QQjqitrsRdz230c8yGf98g4_O4FSQARKgLrNnMJtjfocJV3Bx9Uzkr9kyWy6cDSgu8sknuHtfURewyvaOPV83_rcUWh_Rcu0xOIkt1G2IuUmhWxVb1Gc13e4Fg9MvxFW2I1tjrHOQeUJcYXVH0Hdh_CpjvcKZhaJWFVAR5YZyGdgEpMqmXG36A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJgIOsS0JDCfnzvUNuKt5uCPQuYrbYsvwCRlT7hvaBreqtkG1XIOPGrmmqJvxtZfjSOdLibSwNQlFpVs53R873-tAdYOCHcV9GSnSNenNMHG9oItvbS9MdobMw98WXiCBFlhpGHK3jp-7ESff0NbIC9QOXPLffYSTpRuaygdBG7tcv8kJHRaA9torRykUepUz2zUgxb9VKNYJ5u4riydy8HqjXQVerCBoUCTSBlKleKyNX6wF7kVGTyp1L4Ro0secOVvsj82qmLIXPLqMKJxkyXIBFfsNwavwJo0W_uAnpSPYR1K8fbDcJghQjy6EXOivaNoVwVGNJ-clPJQeIFLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsb05nMXXUzBjqK1g4Xww1NBRhO-ncC4Y8hKeOjbsJriPdPKqEaZOO1TUFeTMpA-ySROrd22ucnrpH0nKrklvRBPzNn2-kn80zjnSHdGTIviDPXMBBGXOrPmh_dCi7UXcN-ojGUgSsrcsFnQeIwfPA6C1Qw5LXqS4AaopDbHrMkrpzKCp1vp8qs247y3iE2oHwl7DJLL3-Ba61QxFE95Nszo0pnK1Y30UvrpMbVbN-abOIsbUY_CqFpXpmt-HUXSANfdFsoKKyX_DgOENkkNHbVOt4Wna23gSE9-1JOR8fjueVk3iZ05someaG5hpHYk7Q03LrTBT25ZChko_Uog1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=ro41nhrMhh1pZMaBAKm32fCDVeKOf_qMzDXIBt9uDeqE2Wp9aPq-zbzuVVZO3NNxygzyoEVkZatXrO3tzuZxnzoDnG3K_5fqxspqouokchSLk0KrFat6QLxygUngmzrYCpjT_WuVkuXExzzrH4ibkACgxVoxPICfWcpvzp_7D7VTGk52yESBV_RVCNQ1LdZgWv1YVX7bd-7u0es3pnM39HMu8GlbFl-fUNzqgbrAWvv3h_cHg00bOdklTJnG0X883bgFWxiQJn0BoYLuC5Z7JYd2uK0EHFYFdyxYfim1PTXC2CXrxS_lwp50J53f1yKqZagZBuB_MUTWDvbxgyf2xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=ro41nhrMhh1pZMaBAKm32fCDVeKOf_qMzDXIBt9uDeqE2Wp9aPq-zbzuVVZO3NNxygzyoEVkZatXrO3tzuZxnzoDnG3K_5fqxspqouokchSLk0KrFat6QLxygUngmzrYCpjT_WuVkuXExzzrH4ibkACgxVoxPICfWcpvzp_7D7VTGk52yESBV_RVCNQ1LdZgWv1YVX7bd-7u0es3pnM39HMu8GlbFl-fUNzqgbrAWvv3h_cHg00bOdklTJnG0X883bgFWxiQJn0BoYLuC5Z7JYd2uK0EHFYFdyxYfim1PTXC2CXrxS_lwp50J53f1yKqZagZBuB_MUTWDvbxgyf2xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=YipOOcVZTW-a58SOuxZavvmrMioQq62X2KvgapxOToIAI2KMd0yOOyF8c0v07wKt4g_0c5su36pWxISCkT1m-Of6kYMtkyrZs9VCBleG_NsyNonXtK9X_SBVcbniEX9V0ibDU4REo9Dy4KRaiKOyE6DPOJeU5rUhsqUMazCX875dmecQ3IA-MCtNd1zZWjN2nY2_gzjS4yRvUkxR86P4yM_M4Mlw0WgZq8KtF3-CT4Gb92py3ipcPWvIH6JzJyNI4QjC7dABJHT88SYmECgFnTU2gp7AMNR4cRMRUYkHggyuzcZzF_Tb2ZG_K0aRFo0cxXdOYBLBB3H2IBQ7XnZXKGWmV1DWDKWF3mhFMGTYOoETo7xQjYjRRt1rSpXrQ7oAK_ucXaFLyBMVRSwaDHZUWf_WnUhJKSJxBfrYIbU-gX99FP2bdlUece1ZsfqKlXSSNv559Bd9AZPT6JjNwtRJ0RE9fY5AzjLEoAob3Kw5cTwUyiW-M6UHDVriPnXNKSOVm7D5a5Xp4oGDaatHME1j7w3_REYt-T9Ii-_yvooIsfY4I54xHdyM85QItBfn5Tk1XJHuzFEHahnqXu_gYZg1JZO8reJBjbNKFgwQMkF7tzVoAg4UPdD-x-mXg2N_ZXEPujjmVG7x7zFDtPCVotvjPSkvYonVGMl1QGuxk0jtw4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=YipOOcVZTW-a58SOuxZavvmrMioQq62X2KvgapxOToIAI2KMd0yOOyF8c0v07wKt4g_0c5su36pWxISCkT1m-Of6kYMtkyrZs9VCBleG_NsyNonXtK9X_SBVcbniEX9V0ibDU4REo9Dy4KRaiKOyE6DPOJeU5rUhsqUMazCX875dmecQ3IA-MCtNd1zZWjN2nY2_gzjS4yRvUkxR86P4yM_M4Mlw0WgZq8KtF3-CT4Gb92py3ipcPWvIH6JzJyNI4QjC7dABJHT88SYmECgFnTU2gp7AMNR4cRMRUYkHggyuzcZzF_Tb2ZG_K0aRFo0cxXdOYBLBB3H2IBQ7XnZXKGWmV1DWDKWF3mhFMGTYOoETo7xQjYjRRt1rSpXrQ7oAK_ucXaFLyBMVRSwaDHZUWf_WnUhJKSJxBfrYIbU-gX99FP2bdlUece1ZsfqKlXSSNv559Bd9AZPT6JjNwtRJ0RE9fY5AzjLEoAob3Kw5cTwUyiW-M6UHDVriPnXNKSOVm7D5a5Xp4oGDaatHME1j7w3_REYt-T9Ii-_yvooIsfY4I54xHdyM85QItBfn5Tk1XJHuzFEHahnqXu_gYZg1JZO8reJBjbNKFgwQMkF7tzVoAg4UPdD-x-mXg2N_ZXEPujjmVG7x7zFDtPCVotvjPSkvYonVGMl1QGuxk0jtw4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1FTK-lvgq5CkdzufHHnhRG5_baoKEBem8iWgIEM8wbSo2yOdIi-UpmiilUiRCNnVSg1QjrtSxxZF0WhrZPvi60XXyZqjp6rvTKvvgbdpeKvGdWpwzV1yKo1SKdcqZfMxoY_vjlyH675oI2XjCm5wFtiEIBLYdsAwQYHe42GNsahvYpUBg944RPCgEcYTpUKmXkU_SsxZBJ1lm6hStlCTsPZ2KT_Oi4WLy19sWrfhRc-S_65yrkJ-M7dYfB-IG1zGDpLn9V7d-BGTAFHy9Xa24jnB3_NbK2ofNmTkrxtJeXybSF4Ufr1hZ0eglvY-Y2ki_c5td8UnQWxzi7bEIY6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/un9P2mMQyOZssskrp5HIU4m9PF7WZs_Xn6BCwEdv0uYJnwvcisSQJ1y9bjrsYeixOVOXOezsryLBHakXEpN-KLdIq8jhdf2c65PxNnVmmnDjxEVrVLuGFmtZByaDYIe0UNrMvcVelXtvpOGDbOOr6Fkf2O9s97aLxivwfIeafN2fj3DRveIZ7hL7I0MB3peJKJSrF7XM1pQ7-d-ZQlOcmwyJnrFqoDixqUYRijDaynpu6hmhUbbtDNqQjd8OcI0Xc9eXPZO6Va7cEWu6lZbtBL0c8CHDMFwrT5yj5dlkviOAc0hnC0DrnsG-ptOrR1ddaPNcmHOdv7J0sY-ZN6kpHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdKcfhqUCwdeSzU-qmspsTgK0FBOddXOK2gKQ0ljfTr3x9nhY3rA9FB3yP7Zhd0p3Aju_QH7c8nmZblSCNtOO9A4FEUb0h2bgg3kM0jXW3rc0T2w3EPoTqcYkNtSUXj5LfRuk4S818F7AgTP3j0p9ouQbugSx1DMIwa1EtqrTj-d0XqmfHWBA0yog0sEzX4NKzScQUGSrmb-gVK0VHnAOcYvlvnQCt358Ds2aDkR1Dez8p0qewgfpH3BBR6hBacuC-Tb7KO7OE0izkmWjSdSG4NdfEMF-QD0N_sBAOq6F2xBtL9LAEdg1-Li7Z95xzelSA8wZhrAYp0lzG1NrhDeNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5i4rQMML2QdDLux-VNXsFbZwnNEdQvFg6DeX_lKwFnFD-QUf8WjreSgTKaW6dhg7efRRMF6r0whIGPRCCNkho1N-pNPnIi5TzcPrtokIGx649Si_f189C09jfC6T_1VKfp5nNWVsZYoe6YQPnP5jhazj3MWeXrvnAAm4omlDCWSSBCRIuR-Z6mQqnKzcofghy392cDXT4-S0x9HSzaToJjY8eazasl2b2Dt_mpYxi9MZWuRo_kZKATJ9kjnGEElAF0-yNo4MaiXT3GQrj4BrDl_JTYsADwhopaaKZ7A2ShBIb-sav3kuEQyVb_S-69_GXOFx-S6VHrIWDraaUK4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sw2H707HKvS2CW1mIMTgXDNR5m81iUQvi61VPjgDPsrLS0HJcfT3c3dqRWPjV-Hyl0XUb-hdAfShMZp216Fyb9CV-nm3HPdU_RCQ1nDOQtasJNvXY744Sm6qUskzUE-YbAQUqL35Fe24vz4wwzXgFBvMfAHpI8R7EqBGrTBM4vS1_meibq39s1RyY9GKcdCgGEw8aU06OzaWsgXe5apleWh881qFTRvjU4rDdtMSWLGutmSPSn7qy8FYCTyRLxQvrrRpps1VYCBmmOrCgyNkQKM2-XYDnKCS_V81bI8ggzyLw7EUjHKvDueKCh2Jn80QFQ9aweC6dTclW7exjtCplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyzuYJ9xPgMAUn3juygCx2rSqUHfaLsGoirYukZ9CZMwCJuwpwpnIoFVXtGv5NTOF3etxc_xCkjEn1yCjXfnu6PXElVINCt4OO-VMVbg8bwM48rb-jXRJ8iQY12TDeEZcr5MMSe_-KUgQzIN6Yu7eG01YELtkda8tmp_Qesce0ApRCGQTJhlzSKbfl5YIj8kapDN7s4PK5nXoCmItCxBvFxZ3JqOlhLhbhVcSmyTP6Cm2WYivQ-Cv2m5q9AwUEEdFzcCcyw9JXLrzla-nnELNbIZKUn63biJDLB18vCBS6EHDHKMIvW5g3YetOdSyvD4C8tupmA32U_ptnghqJ-Kuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=NRsrmksswIdteKMrTD5nIb4K6r1YljXudu7QTdM4ce1xRrwWzg9Hw-UWX0uGUKprcqmagUKJPZKunuDzq_c-az_UZbpVk6pC7aPwaYpQITmLvlBhFRI1ddtl5HFAOsR3BAmxWDeK6QTCNfCjTNPwa1ZXOHW0K1ix9oP8LC4-JYDIAtEUi8JKqSq4_ywPxV4U6ydDJEA2-m0EoLUbWTgxydMptDl2haEtDarkZnv-EJ9Y7H5zUlk17hSFBYQVTOw3J5wIAmGsMbTHU2ucHgG4U4FPD871B_ijPWtnr0o_Gq07VGQeZBtj4kQHoVjBm1rMHCmn6K26pvphlLTQ0aQTCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=NRsrmksswIdteKMrTD5nIb4K6r1YljXudu7QTdM4ce1xRrwWzg9Hw-UWX0uGUKprcqmagUKJPZKunuDzq_c-az_UZbpVk6pC7aPwaYpQITmLvlBhFRI1ddtl5HFAOsR3BAmxWDeK6QTCNfCjTNPwa1ZXOHW0K1ix9oP8LC4-JYDIAtEUi8JKqSq4_ywPxV4U6ydDJEA2-m0EoLUbWTgxydMptDl2haEtDarkZnv-EJ9Y7H5zUlk17hSFBYQVTOw3J5wIAmGsMbTHU2ucHgG4U4FPD871B_ijPWtnr0o_Gq07VGQeZBtj4kQHoVjBm1rMHCmn6K26pvphlLTQ0aQTCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=Ob8ozAJFpEv-qgCAiWIbYFLrU4M9AVvQsNYSnZxox7YKa85biIvQVolMMuBrxYjIL57O1szT9s0V7ZPQwaPhLZVnjA9x480kCSSQRDlYQHPABMzuS315nzTrvPgcndcd-rya7yOBbu8uvimqhdXI4EeptzJpNAv6DpouVXbyfGKzyQCpzZGRhkjvbcJT5yiaCC1yOTIlz6PKAx47XJq6Lz5M4k5ZKkH8ddf0x3tYorSbgY8vWfFKUiolwRiIGjv6KfrJ621UG3TGGkDmkJMM5ztWrWe26eEDzoZ6KZ40MFucMnStOHnxsLm2_khE5-inC8xiiPhybsJnD0wfR3XY4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=Ob8ozAJFpEv-qgCAiWIbYFLrU4M9AVvQsNYSnZxox7YKa85biIvQVolMMuBrxYjIL57O1szT9s0V7ZPQwaPhLZVnjA9x480kCSSQRDlYQHPABMzuS315nzTrvPgcndcd-rya7yOBbu8uvimqhdXI4EeptzJpNAv6DpouVXbyfGKzyQCpzZGRhkjvbcJT5yiaCC1yOTIlz6PKAx47XJq6Lz5M4k5ZKkH8ddf0x3tYorSbgY8vWfFKUiolwRiIGjv6KfrJ621UG3TGGkDmkJMM5ztWrWe26eEDzoZ6KZ40MFucMnStOHnxsLm2_khE5-inC8xiiPhybsJnD0wfR3XY4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lXO6geLVsRdhyGiEgFCPjG7wdRl-wwc2H4ILlP_5KnUqVCTdya-5OINvG5rIV3ZpF_CtHYLpvyKJKlBqdxRjj4e8OeoO18CU6DlmVLOqzdx0IHyyuyVaLwy52WDyVXU8wz4QRItDZlrggN1yQebptpuRl0Dnr-YRTu7dEM2FaJz0HpyusOF67ygBwsuZnW4eHM276TXZgbFUvIaZ0y9kGSZwtPdh2lGuPt_AVwjXZsBCe0Jwx4VNctG1EvuD_CISXDfJi-5qcCZtctzuO1JxndWEEIzVo7kqzNJULVJw0nqd3zHmFAM5R_ajlu1JFAJfqSysgjiqOdBTBDkN10t1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4maBMhZkao9nhyNIow5QmVDyXIyThUMJRKF5qHN1qXsdRghh80k66hu8OrQ2ei_TJBdQkBMqZFtXq6UFOZI41CiZBGru7zKqtjCmTre7-MYYk4QC3Dil6NzXUS0nkAjgOCVwEzUH6cvjV-86Fr4cK22M75t-J7AR_C-QnTFlKDw0qEHYxPwVFrgUyJT8qLnZtBI3LpfxhXvZPqHsbevnxiemkUNcNuHgZewde6UmTwFXPfOdde4fdJ3kVOP5JM-ic02zAFpSafeVSPKv8khzVOnIeah76LRnAbGBrno88-6_dlV40-rB8As1aHOIDwXg8aYmKlIn8MLTlgfuMpgGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=d302VNCrlys8s_vTKsPe2kA3NAZiIVAgDWlq5G5_YXCCICYUNH9h7Vn74RWPtxOUHnesokZ1X8yQGy6HXf1zT3lGO9PozBgGV3k3M9lmoUGKse_BRD4sAVRzOUbyRbxEf9-ZAWODqCKSql-fLn4SYQvb4Sglg5bKgdJoPZUvBsGurGNw2TNe6CrHGd1FVq5BpMhz6fw6KOBxoGcYHyFoWU7KMdQvawyoi7eQtURaATrWqriS20iHlLcsD4VovcFRlxoynLAacyT1MlTfTtkFpGvQgchQ4GhK2nfQfRBZSjVmId3cx5gqGnDe7SnA_FM05_7v6Fw01rUDtIKxWEq5bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=d302VNCrlys8s_vTKsPe2kA3NAZiIVAgDWlq5G5_YXCCICYUNH9h7Vn74RWPtxOUHnesokZ1X8yQGy6HXf1zT3lGO9PozBgGV3k3M9lmoUGKse_BRD4sAVRzOUbyRbxEf9-ZAWODqCKSql-fLn4SYQvb4Sglg5bKgdJoPZUvBsGurGNw2TNe6CrHGd1FVq5BpMhz6fw6KOBxoGcYHyFoWU7KMdQvawyoi7eQtURaATrWqriS20iHlLcsD4VovcFRlxoynLAacyT1MlTfTtkFpGvQgchQ4GhK2nfQfRBZSjVmId3cx5gqGnDe7SnA_FM05_7v6Fw01rUDtIKxWEq5bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHGlkhy9fguSa7vw-WNwnK8XN5vUjEMMENhcVR9W-fcUjQUPMyuE2XV07vNJXAwqGK5sCrywVUDE4NSCqsp3bdw98kDfIPTW6EWlmt3HAu8xy5RJWRPnUU-tb0G0a44CqG7JNkoIhRR-LeYhgr_bXx24DhqOlKUIYbtEUfJsyWFf5dOw7eDD7jhxrmNPESv-1tnWk6TQ4FMw_H0M1bJgG86RzeGAwWnx4i2K5eSFIKlj42dh89wSPX-i4N5eFA2Jnt84Uimerp5uO6aZoN0BgHgitYUIR9ozZo--PMDHIYvwtBitGwdV2zf4OZU92VtnN3jlwyBJpFXaMeFwuxgcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaJlYr_ff_WHo4iB9olBpWkPbX2laOvBkxnEfm4WSy7OKUWjIUrGCH95jlQa2CIPuQVEf0vFXvP7XS9zSRE3VznfWozYNehwmiuonijgZY0YdrtLNjekBxGROpFmie1lk2xjYwaZcNM1P7J_S-FWjL6TOeViRFosuhJ64f2J4DCogLIXwOtdcaDwQYky3SSttGgIuyk13PEy0i-U0OBWPD7yhDeJqkh0V5ebRxnrZyX73wKLjJ8rpsDvz-103lH3aqaTf-iqw0yntgHfxQ_uaXD0OFEc1lT2J1Qrk4wm2qh1P5nl2ctx93_GpCUIZtNH2idMA0QBZ65sginADfnoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=XV8hzkhpMieLVJ4QICBDQGup9lZOpPdM-D5Xdok3XXLNSqtOAkLafNCPQV8BOIpJMomHe-ouvyMZZRm-kxtqQVDKdCUiMRK6lGULwM60b_q9aHA_M6KfElX9q4wBPZQ8dFmX-wvbolqjedcSQmmb-PdGSvPzQuzNjUIOdGBEHuSmsJVNbIGbfVHODhYT30jqA-dGm5CZeDZb_pqRbhnfoPKQFEa3kZ15LlJ6tx0fSqc05m-chTj22O88_XyDynktI1BM_CIG0aKcRe9AaWIEU1DMzlo-hEB1YebYe5jiXvkMKCZZQMHizqSxQrdNK2m5KjfFa0dDDFpXVPlizlj0JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=XV8hzkhpMieLVJ4QICBDQGup9lZOpPdM-D5Xdok3XXLNSqtOAkLafNCPQV8BOIpJMomHe-ouvyMZZRm-kxtqQVDKdCUiMRK6lGULwM60b_q9aHA_M6KfElX9q4wBPZQ8dFmX-wvbolqjedcSQmmb-PdGSvPzQuzNjUIOdGBEHuSmsJVNbIGbfVHODhYT30jqA-dGm5CZeDZb_pqRbhnfoPKQFEa3kZ15LlJ6tx0fSqc05m-chTj22O88_XyDynktI1BM_CIG0aKcRe9AaWIEU1DMzlo-hEB1YebYe5jiXvkMKCZZQMHizqSxQrdNK2m5KjfFa0dDDFpXVPlizlj0JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va-X8Up0sJRjNz-wGK0xQcWcNPHOyR2oee7PHMKGTY_2ImvIDzyEQyJURKjRSVUfI11VmjvIL7pXI8Gzli836WKlHJ10RYKe_oMFcE1ZIyRX-Z2TEfRltfYbiSKBwELL_7U9ew8a3M0HVjSnfLdjVCNFFLZhbELMY8YpPlBXfI0YzLGdfrsgPxnSyZqdY2c9LIBHZ2ADgHyGONebHWX2EWwibSF57wLEWrm64e3MVDYKf7Bcvs6bJ7UhX1mzLuzitHcDIAyOAruoWVVXf5zA9guBSluoj8P7mVoL3QoQS9ZBGTKDcKAM-WE5NieVW52HiuCLxlPTynRmgAHhO3lvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA2SLqS97fW2ZuwjAdrpLaRlfuEdmEm5-N_hQCJlSrZUSZ6lVbuj0OJF1mcZpZ7UPNPTcZrHoaoukjFp9y8Yfm0oNm5YQMpULRIJXUx0IADRNm4lvhqjPTF242XSQGJlENH4mAY2p5b41zn0bazqvrJWan9-DP4oEfZOG1WD2VMBlbTn72zoL6cB5fOUTsaSr67ddJMgO-lg8VjTrd4V_raNMxaCTKRVADkAc9CzeCY2oYavcLbSx24ntJDaPIDiAggOm9qRh4-52uhOvg1PXBnozEAhKFxoXevp_UGrUXgtjAfG5zjhRZfBLpJKzOMCMDeHbqwJw20QgcQjTkUVJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=Vg82jguCk8aYNRPgMvaoWSnsmVtLEhr4VsEtUxgzWKJJs7BIkZ4axh2p1mqCXaMCUkLjj0BcM6EnDrVL0mpDffW7dECvaYtE7cMSHWl8H1DTm0Zqaxn55MuEMQbHK_wBCXJBFNLwclH93OQ7rp-ayH_VDpeoenmWORHYhkl5Snt5QBP1xGQXkAg_iLyL-0rnxGH_Lw5_rN_t8jEU_GV8WXA6JPWB5YtO7upgqXjDPluPlHD5gY39-7-tDml7xKNeIreJdliHRNeTAqEyT7SJSfkj6qbFLRHZw_FiL5gpPrrQxDQ2_nK9iYD00vEn0r7srFQb0l_u4EKB3VffhklhNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=Vg82jguCk8aYNRPgMvaoWSnsmVtLEhr4VsEtUxgzWKJJs7BIkZ4axh2p1mqCXaMCUkLjj0BcM6EnDrVL0mpDffW7dECvaYtE7cMSHWl8H1DTm0Zqaxn55MuEMQbHK_wBCXJBFNLwclH93OQ7rp-ayH_VDpeoenmWORHYhkl5Snt5QBP1xGQXkAg_iLyL-0rnxGH_Lw5_rN_t8jEU_GV8WXA6JPWB5YtO7upgqXjDPluPlHD5gY39-7-tDml7xKNeIreJdliHRNeTAqEyT7SJSfkj6qbFLRHZw_FiL5gpPrrQxDQ2_nK9iYD00vEn0r7srFQb0l_u4EKB3VffhklhNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdok7B7SRDOf6lgbyGintnSj8CIWI3m2jJ7ef5RSf28ggEDO6uLahdaypgGUAfNL5q0rayLKzV4UruVKH2OicC88lLUys9yqhb1CI0noH88-WBY-IxCXFuOeigdWadg_sGzJV_aktPZ2G8eba8ncJZzt7Kx12nghZ0oBFzY0SLetB-5kz1ZYotNc_cV0zF29TUV_er6CflnNtRm1iXsOrsVAyh5T0OrPI_nL_buoTqNNNnG5tIFX1yh2mIc-eRiHdAVs02zauzKfEpqA3HferXWjZ57c_dy7YfUDSP6Pgg9c2ovNaeNoAURTf0aYtaOwqyk9BpH8DylyEXEuXQHztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWErJ8h_JGzKbvdSsjlELN49cuGl4Z5BWac7O-jo_A3vG36DpMYAlcIVShui2o9GDpDnRuTGraHIJKHd67DK6llh2nOa7kJcCgxemg-XA8NXBFO2kSL9yMcL6SdxRUhmqQ9n5_YrmPUKK1syMxN9u1HDirRgEKoZycjMBdiZmDAGj1eO8ny-Hia9VyJwXZOrjJ6O_ejoUq_gb5MPuh4Whg1pUFqQVnB0XWx0z2AQKDdQLgXTqyizxmAVrXLU7Ou2e_KI1lPeGZQDRtY6s2t9QD7XFeDrsRlzcb_gvc4hHBecuh8RuOntBmxpf2SsnXJTD78cC6EKrRAQuB18lykpJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6E6s-gJgfAyddAYhopBWkTCRvtzHEwXnT1-MaGpuqf3IS_JKOQxSj1hCWgXfcYnTkLhUfUXklyRSZM2MtworkexFudJaGCq42dS_5KSdBkhgRFsVnxER3c_q8mh5UBwcsJMomgrhrj9cIainqz2z092MPJmCIRA7Je7wW7Ge_4ch0ChqrykMsv5qXliQHaPFL1rJg5uHDKKL2ekHX94Brh5ZDFCQbI0eaeQ9aU45ntlMATIAVjYBHYBw9swc-oL4Yi-Id3BP1diyJ8EggjeaDUdmiwDSkegXELkJ4cwZNTadkcyIj97rzk313QyK5oky1cW_2rZRhcfo6-HZ-WT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp4AKi-8Y0ah9skoGB3LjbxHRn56U49OdWiZxMxTXFiiE0DVdz7TclC-uy31Pn6yl5yVCbOb2PTHayLhKL_Bu9LpXm99ZZtqQaz6oEo8e2q_E6zpsMxyP7Mll-QCSxTlgipYlZLewN6wLaFxAf8XzAr6J05Z6S4SpXIR7GtJhA6p6CwSGvzbEuXDsRwg2trhnIpk61K565geQYcYJ59hnCAJPFWCukX-tipmY7saa3BymE_qK7oEgRy1IsObvCK7aqBiZquO9pkwMR5w253OkcMuSUh7h78uhNCftAyRzTGAoys_dLrTfxU977y9HRqrabx3AyvL1sCPL3EKgXIwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRzPBY3x1TuuV4Iri_l4oDVZQs9vUIGZsAinFmtXChSYpYiQJzs4vHjFOUccBJ4qluv4O47jZMQKrnfSCYSlMfBQGnK7WD-Y8pYbkHacto8KAPCIEytam0S2W3Br5U0stIiyZaHSNkuOT9XB7YkWmfYVmO0G5EcoBlKsMWyc_w-PLwTC3Md2A23OKZhSn5hmAmy7R4G4e2s8ipvyYXzCeT9Xh0HuJpE12zIA4EiWAgAhYr61e1S_2WgE-tEG1Mymhsc5xmbkPCkwt4YKdTfPDm84Rpc1sHFOGCq5bCr7nTNb6Sc20kUJi5Is94VtfYGa8rmQKUyodJwCs3lSWvyzDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnSX-aCmWjCs_Elg5z4TMJVqFA3-gwCxc4MuKfZEhIwnEHa2pj_A0xr31kPHPuHCsgld9P5x9uSuBBRHSiMJ8lX2SwhDjYePSW2385mjgGBMU-rO0vmQhPYv_KDF0w4KJbmaa4-IR1WgUWMVbkimmCbRIEdJ2S6M8qAbz2iCTpAdHFGOq-2zudgo0XKTS3hm9zpqnFpcjS3BuX_kUKxzc8SGZvEW6JPmb9mzbfbtLZt2BorhKtZuihnYLvYie3JGfNvNsRteUbe0sL52A-PyxxWLP6jJQoO-DMuKDTDRZsMJP39tJXHYVmGvUgX3OC-So6PXKPBXSQN-EkF3yhaFGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=ROyQ0IFgmjQGWZTRSajGBw6pCqOmeDWmnd_aprJfKKkkjps6WOaqk9Gpk36s5X5ruVPj0qvoDX44XHTvbap3HW1rysOVGggbCL2HUKrAdUWAd9U1tVh0NidjzeskcvNieHmExfr2Js3zElA5N3Zx9K-6kE_jx6Td0h2dyQaiWRG-cbKPrnYv6a9ObG0iQ6DfpuEGgXuBCRWjYmkgZbo50IsxlY9x14830swPgc_ao7yhuA_UdCBWVhxHN92oHD3etGzXnbDuSNEXlhqsd-TtObCuedUSFRy0oJjO87aP5lIR45a3E6aPWcrSoywwEh6Leb_9h9Bi7MeCzWAMuIYQcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=ROyQ0IFgmjQGWZTRSajGBw6pCqOmeDWmnd_aprJfKKkkjps6WOaqk9Gpk36s5X5ruVPj0qvoDX44XHTvbap3HW1rysOVGggbCL2HUKrAdUWAd9U1tVh0NidjzeskcvNieHmExfr2Js3zElA5N3Zx9K-6kE_jx6Td0h2dyQaiWRG-cbKPrnYv6a9ObG0iQ6DfpuEGgXuBCRWjYmkgZbo50IsxlY9x14830swPgc_ao7yhuA_UdCBWVhxHN92oHD3etGzXnbDuSNEXlhqsd-TtObCuedUSFRy0oJjO87aP5lIR45a3E6aPWcrSoywwEh6Leb_9h9Bi7MeCzWAMuIYQcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHgXgqE5SoGaLRLiaeOeJtSCbEWWZAtX01vn4qLJIaG12Wa-tEk98S-ApgxqaKEWX1xNbw0Rq6_ZeCxVVpV6vfMLYvzJv5ARBsEjGqhPvYLyVVvVDfEvzV5Oj_WQ9RR4H3dpZ11pwodUcX54faKo163_-udgoElz4s7sMmIr_NiZkvGDM_p8KaDY3itNhIZQmGcCzgkGC4EXdTXVg-YVs7Y0K1fyWkzV-kFx68Zwjy4b_MMQmKg2VBm2Ps023kkiOU1jSTq66GXPy6hK_jZf5NOCTXCfjiWS9K-gFCVy9Ujef4Atvtnuyk8Z8wrYjkJjRGsbQXykDM7ywcYdtdiHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpwPaPfvWyA60T21WATCTqmwfR2dfwxMlY0-mbjkGcLoEcQgqMVnuR3d7cefBBzFcElcfEvEobUM6C8fFEO3nzvCixB4dQ-mN5gvEThRxcfQcj-kQLiG61wyzOCWgTL2PUt4zk9pDGknULPmtsWCS2mG1YKMxJ0KttGknIbLIJGvGUlQXdOJySBRlydlbIttSV2hrW3phJoz8gssbRxOaT8ODE0NWQ233PKzAmElryYwyVR3ASXpvm9Iqh6lBcPGBsA3UMCytlvi7v93MmQD3Jj0i_LiHJ2VxlNnFMtMQsgJ1s4dw-tk8CdjX-gLVucjXlryMeHL4TPi2evDKepnmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=VUCUb-SrNgRA3pDgIM82Zx6Ws-gyYh7s6uFBYUQYVJNGrHUqdaIf9ueOMM4unzOvhbfS4QA8-fuSK-hkQfwq25JIW8-YiRhcht02kz1QXJASxQmbSyB6hZvLHhK5i70-fPQ_HWiXvd5xXZB8BArCo2gCUK2QFFrcbwmLIuo3k2mqoJQz1gfUJIWrboIgV1Y5Ox-Hfl_DgvW0wYx2myHog5GcqdCC9vL7tLJyB3OBUwNPm9OgbZ0cvHqzKea_02qfysZxyAcSN9RXF05H6Zac6SHzOxO3_IfNm02O_fPWYx1aB7d-YZab9MNE5pgMCIclgAGsZYE9UWk0hI_hBQ5eqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=VUCUb-SrNgRA3pDgIM82Zx6Ws-gyYh7s6uFBYUQYVJNGrHUqdaIf9ueOMM4unzOvhbfS4QA8-fuSK-hkQfwq25JIW8-YiRhcht02kz1QXJASxQmbSyB6hZvLHhK5i70-fPQ_HWiXvd5xXZB8BArCo2gCUK2QFFrcbwmLIuo3k2mqoJQz1gfUJIWrboIgV1Y5Ox-Hfl_DgvW0wYx2myHog5GcqdCC9vL7tLJyB3OBUwNPm9OgbZ0cvHqzKea_02qfysZxyAcSN9RXF05H6Zac6SHzOxO3_IfNm02O_fPWYx1aB7d-YZab9MNE5pgMCIclgAGsZYE9UWk0hI_hBQ5eqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz3-87VgvhtfxH0iC02EWOt_kVupqEqXUBx6bfeE6dunDWlpZPQONacXqq5d8omahIb8U_lPlwEi4HZ25VQFSDCEqnytq3Y9rZ1F6zTOP3wSdrAlSQFZxdercpWNTWmG5nAs7wE_zP4dkeLlDWDdIfTSM2UhG6rMEDW7trDbwuE_G9WK2Sh568KHG_jU7sO7_dRD5w7pWE4VwCRmvyxqnS-xR_lACmqTjvkQl-S2ZtsOFL7BkAFTHmIvOuOTLt-uWzaOjEVWVsQZo_AH0yu4Iq1YMOAbxBmDbENHTGZS9wV1Api9avMZpKRchdM5jPORuqCTa-YFbREimOdI3KfRPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MX6brAjEE8-LMAmZPvW528tPoKbXoQivspG90gIQvNKR5G34YpbGtvpUnhIRpT61hV0SNIzTkXIGk-EGtpCfxVeA2jUmb5k3cuDeUtDPQ5ZhiKdAgtK_-zF_iwHuaXRcbzLtXd92S30B9l26r1q6Bpi33FyZ7vaWt5oUY5te-_xTeAcnOIx0MP6Z5ruWqxYNopyRiHaffTTrtWsbF7YAfD6EsWR1GGt-LfnJe0DFo53x75GJ8P-YygPiKJv23N3i8bR05gLl0edJeXGt5QGU15K2gHX8Mc4QyRh_pEs1n-IKc1JOSadtvu7TCIvl-InhGIRMRCqjtmGHreJUoQ0JUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vfi45mPTAY9M7jUPvgqo3UiavVg3tK2B-ZbzYepFA3a8LVcMCCAffDQ5ZZKf3L1rL4PTXlPyR9yyJ34pBGyYtZ61JY5RyI3m1n3BQP7lpSLVuAyKVaExUJW1Kxd_H82CO4ccFwMa4jQVKpXBLKz043WlhyPveMIkcAFt4i5h6HsAevvxYqeKCG54aM22NcBGl-XTH4dHRvbTo4SoQaQFMaDLHg6c0KILhp5YMWbPOZpG6KMZxAQNC6AASM17iNgKETo8lwgm_0cTCR1Jwk4_bIQ0-z5on-e042Rx29qGXNGt8F08RjgNL-lYkdRhlJqEK9ymNs4v-6WxFVKkUFx5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZatSYXQif0p4XGpPYbreTVJSfoSr39_0WTMBxAP2r5yDYRJp8d4rtLtLDT-m5c3VvAVm1zSjSI-H3Sjp5GjXI3RSqZTxiyD_lWas1jz6M_mjgYTv0zf5YiiAzWoqrnCsbBlvjeca34u1FuLhCgQeXl-62jKCH-pzsGxGb5Gmyfw_wMSr0Jh7o8_P8VFpqxwZgbez_UWrDtgbEju99racOLhBihLQStmdm2GohJ-laiN91SfL36NxIjKhJhOJskJYZ5hl0l3xtFVSAG74j7LmxxvgINHt_GI70Zm0ONRTvaU0LoDxT1J3AubCYWK9uP5XXEw48b5KvMjj_yxXwsujQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
